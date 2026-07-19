# 03 Network Scanner

Raw code, terminal commands, sample output, and monospaced templates extracted from the PDF text layer. Page wraps and teaching-snippet indentation are preserved as closely as possible. Use the cleaned scripts in `../tools/` for runnable versions.

## PDF page 38

```python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET = use IPv4 addresses
# SOCK_STREAM = use TCP (connection-based, reliable)
result = s.connect_ex(('127.0.0.1', 80))
# result == 0 means connection succeeded = port is OPEN
# result != 0 means connection failed = port is CLOSED or FILTERED
import socket
target = "127.0.0.1"
port = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1)
result = s.connect_ex((target, port))
if result == 0:
```

## PDF page 39

```python
    print(f"Port {port} is OPEN")
else:
    print(f"Port {port} is closed")
s.close()
s.settimeout(1): wait at most 1 second for a response. Without this, 
a scan can hang indefinitely on unresponsive ports.
s.close(): always close the socket after using it. Leaving sockets 
open wastes resources.
import socket
target = "127.0.0.1"
start_port = 1
end_port = 1024
print(f"Scanning {target} ...")
for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(0.5)
result = s.connect_ex((target, port))
if result == 0:
    print(f"Port {port} --- OPEN")
s.close()
port_labels = {
21: "FTP", 22: "SSH", 25: "SMTP", 53: "DNS",
80: "HTTP", 443: "HTTPS", 3306: "MySQL", 8080: "HTTP-Alt"
}
# Inside the port loop:
label = port_labels.get(port, "Unknown")
print(f"Port {port} --- OPEN ({label})")
# scanner.py
# Port scanner with service labels, timing, and file output
import socket
import time
```

## PDF page 40

```python
target = "127.0.0.1"  # change this to your target
start_port = 1
end_port = 1024
output_file = "scan_results.txt"
port_labels = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-Alt",
}
print(f"Scanning {target} ...")
start_time = time.time()
open_ports = 0
found_ports = []
for port in range(start_port, end_port + 1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            label = port_labels.get(port, "Unknown")
            print(f"Port {port} --- OPEN ({label})")
            open_ports += 1
            found_ports.append((port, label))
        s.close()
    except KeyboardInterrupt:
        print("\nScan stopped.")
        break
    except Exception:
        pass
duration = round(time.time() - start_time, 2)
print(f"\nDone. {open_ports} open port(s). Time: {duration}s")
with open(output_file, "w") as f:
    f.write(f"Scan: {target}\n")
    f.write("=" * 40 + "\n")
    for port, label in found_ports:
        f.write(f"Port {port} OPEN ({label})\n")
    f.write(f"\nTotal: {open_ports} open | Time: {duration}s\n")
print(f"Results saved: {output_file}")
```

## PDF page 41

```python
# banner.py
# Grabs service banners to identify software and version information
import socket
def grab_banner(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((ip, port))
        banner = s.recv(1024).decode("utf-8", errors="ignore").strip()
        s.close()
        return banner
    except Exception:
        return None
target = "127.0.0.1"
ports_to_check = [21, 22, 25, 80, 110, 143]
for port in ports_to_check:
    print(f"Checking port {port}...")
    banner = grab_banner(target, port)
    if banner:
        print(f" Banner: {banner[:100]}")
    else:
        print(" No banner received")
```

