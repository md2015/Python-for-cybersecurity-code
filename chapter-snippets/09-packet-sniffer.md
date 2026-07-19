# 09 Packet Sniffer

Raw code, terminal commands, sample output, and monospaced templates extracted from the PDF text layer. Page wraps and teaching-snippet indentation are preserved as closely as possible. Use the cleaned scripts in `../tools/` for runnable versions.

## PDF page 91

```python
from scapy.all import sniff
def process_packet(packet):
    print(packet.summary())
    sniff(count=10, prn=process_packet, store=False)
```

## PDF page 92

```python
from scapy.all import IP, TCP, UDP, ICMP
def process_packet(packet):
    if packet.haslayer(IP):
        src = packet[IP].src # source IP
        dst = packet[IP].dst # destination IP
        if packet.haslayer(TCP):
            sport = packet[TCP].sport # source port
            dport = packet[TCP].dport # destination port
            if packet.haslayer(UDP):
                sport = packet[UDP].sport
                dport = packet[UDP].dport
```

## PDF page 93

```python
# sniffer.py
# Live packet sniffer with protocol labeling and capture file output
import datetime
from scapy.all import ICMP, IP, TCP, UDP, sniff
PORT_LABELS = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-Alt",
}
COUNTS = {"TCP": 0, "UDP": 0, "ICMP": 0, "Other": 0}
LOGFILE = "capture.txt"
PACKET_MAX = 50
def label_port(port):
    return PORT_LABELS.get(port, "Unknown")
def handle_packet(packet):
    if IP not in packet:
        return
    src = packet[IP].src
    dst = packet[IP].dst
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if TCP in packet:
        proto = "TCP"
        sport = packet[TCP].sport
        dport = packet[TCP].dport
    elif UDP in packet:
        proto = "UDP"
        sport = packet[UDP].sport
        dport = packet[UDP].dport
    elif ICMP in packet:
        proto = "ICMP"
        sport = "-"
        dport = "-"
    else:
        proto = "Other"
        sport = "-"
        dport = "-"
    COUNTS[proto] += 1
```

## PDF page 94

```python
    service = label_port(dport) if isinstance(dport, int) else "-"
    line = f"{timestamp} {proto} {src}:{sport} -> {dst}:{dport} 
({service})"
    print(line)
    with open(LOGFILE, "a") as f:
        f.write(line + "\n")
print(f"Capturing {PACKET_MAX} packets. Press Ctrl+C to stop.")
sniff(prn=handle_packet, count=PACKET_MAX, store=False)
print("Summary:")
for proto, count in COUNTS.items():
    print(f"{proto}: {count}")
# Linux / Mac - requires sudo:
sudo python3 sniffer.py
# Windows - run Command Prompt as Administrator, then:
python sniffer.py
```

## PDF page 96

```python
tcp.port == 80 # all HTTP traffic
ip.addr == 192.168.1.5 # all traffic to or from this IP
http.request.method == 'POST' # only HTTP POST requests
tcp.flags.syn == 1 # TCP connection initiations
dns # all DNS traffic
```

