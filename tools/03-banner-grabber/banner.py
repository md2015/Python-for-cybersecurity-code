# banner.py
# Passively reads service banners from authorized TCP services

import socket


def grab_banner(host, port, timeout=2):
    try:
        with socket.create_connection(
            (host, port), timeout=timeout
        ) as sock:
            sock.settimeout(timeout)
            data = sock.recv(1024)
        banner = data.decode("utf-8", errors="replace").strip()
        return banner or None
    except (OSError, TimeoutError):
        return None


def main():
    target = "127.0.0.1"
    ports_to_check = [21, 22, 25, 80, 110, 143]

    for port in ports_to_check:
        print(f"Checking port {port}...")
        banner = grab_banner(target, port)

        if banner:
            print(f"  Banner: {banner[:100]}")
        else:
            print("  No passive banner received")


if __name__ == "__main__":
    main()
