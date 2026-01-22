# Network Traffic Analysis & Anomaly Detection Tool

A Python-based tool for analyzing network packet captures and identifying basic traffic anomalies using interpretable statistical methods.

## Motivation
Large-scale scientific and computing infrastructures depend on reliable network behavior.
This project demonstrates how packet-level traffic can be analyzed programmatically
without relying on heavy GUI-based tools.

## Features
- PCAP file parsing
- Protocol-level traffic statistics
- Packet size analysis
- Simple anomaly detection
- Visualization of protocol distribution

## Tech Stack
- Python
- Scapy
- Pandas
- Matplotlib

## Project Structure
- `parser.py` – Extracts packet-level features
- `stats.py` – Computes traffic statistics
- `anomaly.py` – Detects anomalous packets
- `visualizer.py` – Generates traffic plots

## Execution Environment
Packet captures were collected locally using Wireshark.
The analysis pipeline was developed and tested using Google Colab due to limited local storage.

## Validation
Traffic statistics were cross-verified using Wireshark’s built-in
protocol hierarchy and packet length statistics.

## Usage
```bash
pip install -r requirements.txt
python main.py
