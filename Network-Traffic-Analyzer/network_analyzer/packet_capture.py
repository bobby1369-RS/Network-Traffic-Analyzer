from scapy.all import sniff

def capture_packets(interface, packet_count, timeout):
    # Captures packets using Scapy
    packets = sniff(iface=interface, count=packet_count, timeout=timeout)
    return packets

