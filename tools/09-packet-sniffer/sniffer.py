# sniffer.py
# Authorized packet sniffer with text summaries and PCAP output

import datetime

from scapy.all import ICMP, IP, TCP, UDP, sniff, wrpcap

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
TEXT_LOG = "capture.txt"
PCAP_FILE = "capture.pcap"
PACKET_MAX = 50


def label_service(source_port, destination_port):
    if destination_port in PORT_LABELS:
        return PORT_LABELS[destination_port]
    if source_port in PORT_LABELS:
        return PORT_LABELS[source_port]
    return "Unknown"


def handle_packet(packet):
    if IP not in packet:
        return

    source_ip = packet[IP].src
    destination_ip = packet[IP].dst
    timestamp = datetime.datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    if TCP in packet:
        protocol = "TCP"
        source_port = packet[TCP].sport
        destination_port = packet[TCP].dport
    elif UDP in packet:
        protocol = "UDP"
        source_port = packet[UDP].sport
        destination_port = packet[UDP].dport
    elif ICMP in packet:
        protocol = "ICMP"
        source_port = "-"
        destination_port = "-"
    else:
        protocol = "Other"
        source_port = "-"
        destination_port = "-"

    COUNTS[protocol] += 1

    if (
        isinstance(source_port, int)
        and isinstance(destination_port, int)
    ):
        service = label_service(source_port, destination_port)
    else:
        service = "-"

    line = (
        f"{timestamp} {protocol} "
        f"{source_ip}:{source_port} -> "
        f"{destination_ip}:{destination_port} ({service})"
    )
    print(line)

    with open(TEXT_LOG, "a", encoding="utf-8") as log:
        log.write(line + "\n")


def main():
    print(
        f"Capturing {PACKET_MAX} packets. "
        "Press Ctrl+C to stop."
    )

    try:
        packets = sniff(
            prn=handle_packet,
            count=PACKET_MAX,
            store=True,
        )
    except PermissionError:
        print(
            "Packet capture requires administrator "
            "or root privileges."
        )
        return
    except KeyboardInterrupt:
        print("\nCapture stopped by user.")
        return

    wrpcap(PCAP_FILE, packets)

    print("Summary:")
    for protocol, count in COUNTS.items():
        print(f"{protocol}: {count}")

    print(f"Text summary saved as {TEXT_LOG}")
    print(f"Packet capture saved as {PCAP_FILE}")


if __name__ == "__main__":
    main()
