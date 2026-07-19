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
    service = label_port(dport) if isinstance(dport, int) else "-"
    line = f"{timestamp} {proto} {src}:{sport} -> {dst}:{dport} ({service})"
    print(line)

    with open(LOGFILE, "a") as f:
        f.write(line + "\n")


print(f"Capturing {PACKET_MAX} packets. Press Ctrl+C to stop.")
sniff(prn=handle_packet, count=PACKET_MAX, store=False)
print("Summary:")
for proto, count in COUNTS.items():
    print(f"{proto}: {count}")
