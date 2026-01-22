from analyzer.parser import parse_pcap
from analyzer.stats import compute_statistics
from analyzer.anomaly import detect_anomalies
from analyzer.visualizer import plot_protocol_distribution
import os

PCAP_FILE = "data/sample.pcap"
OUTPUT_DIR = "output"


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    df = parse_pcap(PCAP_FILE)

    stats = compute_statistics(df)
    print("=== Traffic Statistics ===")
    for k, v in stats.items():
        print(f"{k}: {v}")

    anomalies = detect_anomalies(df)
    anomalies.to_csv(f"{OUTPUT_DIR}/anomalies.csv", index=False)

    plot_protocol_distribution(stats["protocol_distribution"])


if __name__ == "__main__":
    main()
