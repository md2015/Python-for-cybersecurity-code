from __future__ import annotations

import importlib.util
import pathlib
import socket
import sys
import threading
import types
from unittest.mock import patch

ROOT = pathlib.Path(__file__).resolve().parents[1]

FILES = {
    "password_checker": ROOT
    / "tools/01-password-strength-checker/password_checker.py",
    "scanner": ROOT / "tools/02-network-scanner/scanner.py",
    "banner": ROOT / "tools/03-banner-grabber/banner.py",
    "username_search": ROOT
    / "tools/04-osint-username-tracker/username_search.py",
    "generate": ROOT / "tools/05-password-generator/generate.py",
    "monitor": ROOT
    / "tools/06-file-integrity-monitor/monitor.py",
    "log_analyzer": ROOT / "tools/07-log-analyzer/log_analyzer.py",
    "subdomain_finder": ROOT
    / "tools/08-subdomain-finder/subdomain_finder.py",
    "sniffer": ROOT / "tools/09-packet-sniffer/sniffer.py",
    "web_scanner": ROOT
    / "tools/10-web-vulnerability-scanner/web_scanner.py",
}


def load(name: str):
    path = FILES[name]
    module_name = f"book_code_{name}"
    spec = importlib.util.spec_from_file_location(module_name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_password_checker():
    module = load("password_checker")
    assert module.check_password("hello")[0] == 0
    assert module.check_password("Hello123!abc")[0] == 5
    assert module.get_verdict(5) == "VERY STRONG"


def test_scanner_local_server():
    module = load("scanner")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("127.0.0.1", 0))
    server.listen(1)
    port = server.getsockname()[1]

    try:
        assert module.scan_ports(
            "127.0.0.1", port, port, 0.5
        ) == [(port, "Unknown")]
    finally:
        server.close()


def test_banner_local_server():
    module = load("banner")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("127.0.0.1", 0))
    server.listen(1)
    port = server.getsockname()[1]

    def serve_once():
        connection, _ = server.accept()
        with connection:
            connection.sendall(b"TEST BANNER\r\n")
        server.close()

    worker = threading.Thread(target=serve_once, daemon=True)
    worker.start()
    assert module.grab_banner("127.0.0.1", port, 1) == "TEST BANNER"
    worker.join(timeout=2)


def test_username_search_mocked():
    module = load("username_search")

    class Response:
        def __init__(self, status_code: int):
            self.status_code = status_code

    codes = iter([200, 404, 302, 200, 404, 302, 500])
    with patch.object(
        module.requests,
        "get",
        side_effect=lambda *args, **kwargs: Response(next(codes)),
    ):
        results = module.search_username("valid_user", timeout=1)

    assert len(results) == len(module.SITES)
    assert results[0].startswith("Possible match:")
    assert results[1].startswith("Not found:")


def test_password_generator():
    module = load("generate")
    for _ in range(25):
        password = module.generate_password(16, True, True, True)
        assert len(password) == 16
        assert any(character.isupper() for character in password)
        assert any(character.isdigit() for character in password)
        assert any(character in module.SYMBOLS for character in password)


def test_file_integrity_monitor(tmp_path):
    module = load("monitor")
    sample = tmp_path / "sample.txt"
    sample.write_text("version one", encoding="utf-8")
    before = module.scan_directory(str(tmp_path))
    sample.write_text("version two", encoding="utf-8")
    after = module.scan_directory(str(tmp_path))
    assert before["sample.txt"] != after["sample.txt"]


def test_log_analyzer(tmp_path):
    module = load("log_analyzer")
    lines = [
        (
            '192.0.2.10 - - [15/Jan/2026:10:20:45 -0500] '
            '"POST /login HTTP/1.1" 401 512\n'
        )
        for _ in range(5)
    ]
    lines.append(
        '198.51.100.20 - - [15/Jan/2026:10:21:00 -0500] '
        '"GET / HTTP/1.1" 200 1024\n'
    )
    log_file = tmp_path / "access.log"
    log_file.write_text("".join(lines), encoding="utf-8")
    total, alerts = module.analyze_log(str(log_file), threshold=5)
    assert total == 6
    assert alerts == {"192.0.2.10": 5}


def test_subdomain_finder_mocked():
    module = load("subdomain_finder")

    def resolve(hostname: str):
        if hostname == "www.example.com":
            return "127.0.0.1"
        raise socket.gaierror()

    with patch.object(
        module.socket, "gethostbyname", side_effect=resolve
    ):
        results = module.find_subdomains(
            "example.com", ["www", "missing"], workers=2
        )

    assert results == [("www.example.com", "127.0.0.1")]


def test_sniffer_synthetic_packet(tmp_path):
    fake_all = types.ModuleType("scapy.all")
    ip_key = object()
    tcp_key = object()
    udp_key = object()
    icmp_key = object()
    fake_all.IP = ip_key
    fake_all.TCP = tcp_key
    fake_all.UDP = udp_key
    fake_all.ICMP = icmp_key
    fake_all.sniff = lambda **kwargs: []
    fake_all.wrpcap = lambda *args, **kwargs: None
    fake_package = types.ModuleType("scapy")
    fake_package.all = fake_all

    old_scapy = sys.modules.get("scapy")
    old_scapy_all = sys.modules.get("scapy.all")
    sys.modules["scapy"] = fake_package
    sys.modules["scapy.all"] = fake_all

    try:
        module = load("sniffer")

        class Layer:
            def __init__(self, **values):
                self.__dict__.update(values)

        class Packet:
            def __init__(self):
                self.layers = {
                    ip_key: Layer(src="192.0.2.1", dst="198.51.100.2"),
                    tcp_key: Layer(sport=12345, dport=443),
                }

            def __contains__(self, key):
                return key in self.layers

            def __getitem__(self, key):
                return self.layers[key]

        module.TEXT_LOG = str(tmp_path / "capture.txt")
        module.COUNTS = {"TCP": 0, "UDP": 0, "ICMP": 0, "Other": 0}
        module.handle_packet(Packet())
        output = pathlib.Path(module.TEXT_LOG).read_text(encoding="utf-8")
        assert module.COUNTS["TCP"] == 1
        assert "HTTPS" in output
    finally:
        if old_scapy is None:
            sys.modules.pop("scapy", None)
        else:
            sys.modules["scapy"] = old_scapy

        if old_scapy_all is None:
            sys.modules.pop("scapy.all", None)
        else:
            sys.modules["scapy.all"] = old_scapy_all


def test_web_scanner_mocked():
    module = load("web_scanner")

    class Response:
        def __init__(self, headers=None, text=""):
            self.headers = headers or {}
            self.text = text

    responses = iter(
        [
            Response({"Server": "Demo/1.0"}),
            Response(text="Index of /\nParent Directory"),
            Response(text="You have an error in your SQL syntax"),
        ]
    )

    with patch.object(
        module,
        "get_page",
        side_effect=lambda *args, **kwargs: next(responses),
    ):
        findings = module.scan("https://example.com")

    assert any("Missing security header" in item for item in findings)
    assert any("directory listing" in item.lower() for item in findings)
    assert any("sql error disclosure" in item.lower() for item in findings)
