from scapy.all import rdpcap
import pandas as pd


def parse_pcap(file_path):
    packets = rdpcap(file_path)
    records = []

    for pkt in packets:
        if pkt.haslayer("IP"):
            records.append({
                "src_ip": pkt["IP"].src,
                "dst_ip": pkt["IP"].dst,
                "protocol": pkt["IP"].proto,
                "packet_size": len(pkt)
            })

    return pd.DataFrame(records)
