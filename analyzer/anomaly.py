def detect_anomalies(df, size_threshold=1500):
    return df[df["packet_size"] > size_threshold]
