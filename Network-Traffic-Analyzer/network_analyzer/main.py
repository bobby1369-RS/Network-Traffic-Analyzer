from packet_capture import capture_packets
from traffic_analysis import analyze_traffic, print_report
from utils import log_action
from scapy.all import get_if_list

def list_available_interfaces():
    # Get the list of available network interfaces using Scapy's get_if_list
    interfaces = get_if_list()
    if not interfaces:
        print("No interfaces found! Please check your network setup.")
        return None
    
    print("Available network interfaces:")
    for idx, iface in enumerate(interfaces, 1):
        print(f"{idx}. {iface}")
    
    # Let the user choose an interface by number
    try:
        choice = int(input("Select an interface by number: "))
        if 1 <= choice <= len(interfaces):
            return interfaces[choice - 1]
        else:
            print("Invalid selection. Exiting.")
            return None
    except ValueError:
        print("Invalid input. Exiting.")
        return None

def menu():
    print("Network Traffic Analyzer Tool")
    print("1. Start Packet Capture")
    print("2. View Traffic Analysis Report")
    print("3. Exit")

def start_packet_capture():
    interface = list_available_interfaces()
    if not interface:
        print("Exiting due to interface selection failure.")
        return
    
    packet_count = int(input("Enter the number of packets to capture: "))
    timeout = int(input("Enter the timeout in seconds: "))
    
    print(f"Capturing {packet_count} packets on interface: {interface}")
    packets = capture_packets(interface, packet_count, timeout)
    
    log_action(f"Started capturing {packet_count} packets on {interface} for {timeout} seconds.")
    
    analyze_traffic(packets)
    print("Traffic analysis complete. View report with option 2.")

def view_report():
    print_report()

def main():
    while True:
        menu()
        choice = input("Select an option: ")

        if choice == '1':
            start_packet_capture()
        elif choice == '2':
            view_report()
        elif choice == '3':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

