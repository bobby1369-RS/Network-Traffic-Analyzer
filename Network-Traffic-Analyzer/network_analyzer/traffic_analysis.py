def analyze_traffic(packets):
    # Simple packet analysis: Print packet summary
    for packet in packets:
        print(packet.summary())

def print_report():
    # Print a pre-saved report or analysis results
    with open("reports/traffic_report.txt", "r") as file:
        print(file.read())

