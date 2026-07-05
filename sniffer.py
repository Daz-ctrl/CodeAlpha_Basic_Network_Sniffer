from scapy.all import sniff, IP, TCP, UDP, conf
   #USING SCAPY TO SNIFF NETWORK PACKETS AND PRINT BASIC INFO
   #TO INSTALL SCAPY: pip install scapy
def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = "UNKNOWN"
        
        if TCP in packet:
            proto = "TCP"
        elif UDP in packet:
            proto = "UDP"
            
        print(f"[+] {proto} Packet: {ip_src} -> {ip_dst}")
        
        if packet.haslayer(TCP) or packet.haslayer(UDP):
            payload = bytes(packet.getlayer(2)).hex() 
            if payload:
                print(f"    Payload Snippet: {payload[:50]}...")

def main():
    print("========= Starting Basic Network Sniffer =========")
    print("Press Ctrl+C to stop sniffing.\n")
    
    # FORCE SCAPY TO USE WINDOWS NATIVE L3 SOCKETS TO BYPASS WINPCAP REQ
    conf.L3socket = conf.L3socket
    
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
    #TO RUN: python sniffer.py