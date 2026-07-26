# scanner.py
# Authorized TCP port scanner with labels, timing, and file
# output

import socket
import time

# change only to a system you are authorized to scan
TARGET = "127.0.0.1"
START_PORT = 1
END_PORT = 1024
TIMEOUT = 0.5
OUTPUT_FILE = "scan_results.txt"

PORT_LABELS = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    1433: "MSSQL",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    6379: "Redis",
    8080: "HTTP-Alt",
}


def scan_ports(target, start_port, end_port, timeout=0.5):
    if not 1 <= start_port <= end_port <= 65535:
        raise ValueError(
            "Ports must satisfy "
            "1 <= start <= end <= 65535."
        )

    target_ip = socket.gethostbyname(target)
    found_ports = []

    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM,
            ) as sock:
                sock.settimeout(timeout)
                if sock.connect_ex((target_ip, port)) == 0:
                    label = PORT_LABELS.get(port, "Unknown")
                    found_ports.append((port, label))
        except OSError as error:
            print(f"Port {port}: scan error: {error}")

    return found_ports


def main():
    print(f"Scanning {TARGET} ...")
    start_time = time.time()

    try:
        found_ports = scan_ports(
            TARGET, START_PORT, END_PORT, TIMEOUT
        )
    except (ValueError, socket.gaierror) as error:
        print(f"Scan could not start: {error}")
        return
    except KeyboardInterrupt:
        print("\nScan stopped by user.")
        return

    duration = round(time.time() - start_time, 2)

    for port, label in found_ports:
        print(f"Port {port} --- OPEN ({label})")

    print(
        f"\nDone. {len(found_ports)} open port(s). "
        f"Time: {duration}s"
    )

    with open(OUTPUT_FILE, "w", encoding="utf-8") as report:
        report.write(f"Scan: {TARGET}\n")
        report.write("=" * 40 + "\n")
        for port, label in found_ports:
            report.write(f"Port {port} OPEN ({label})\n")
        report.write(
            f"\nTotal: {len(found_ports)} open | "
            f"Time: {duration}s\n"
        )

    print(f"Results saved: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
