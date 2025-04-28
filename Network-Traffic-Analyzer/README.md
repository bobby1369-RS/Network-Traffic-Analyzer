# Network Traffic Analyzer

This tool allows you to capture and analyze network traffic to detect malicious activities such as SYN floods, port scans, and ICMP pings. It uses the Scapy library for packet capture and analysis.

## Features
- Capture network packets using Scapy.
- Analyze captured packets for suspicious activities like DoS, SYN Floods, and Port Scanning.
- Logs the analysis to a file (`logs/traffic_analysis_log.txt`).
- View detailed reports from captured traffic.

## Installation

1. Clone the repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
