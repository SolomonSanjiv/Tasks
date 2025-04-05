import socket
# ARP Table: A dictionary representing IP-MAC mappings in a network
ARP_TABLE = {
    '192.168.1.1': '00:0A:95:9D:68:16',
    '192.168.1.2': '00:0A:95:9D:68:17',
    '192.168.1.3': '00:0A:95:9D:68:18',
    '192.168.1.4': '00:0A:95:9D:68:19',
    '192.168.1.5': '00:0A:95:9D:68:1A',
}
def arp_request(ip_address):
    if ip_address in ARP_TABLE:
        return ARP_TABLE[ip_address]
    else:
        return "MAC Address not found"
def main():
    print("ARP Simulation")
    while True:
        ip = input("Enter an IP address to resolve (or type 'exit' to quit): ")
        if ip.lower() == 'exit':
            break
        mac_address = arp_request(ip)
        print(f"IP Address: {ip}, MAC Address: {mac_address}")
if __name__ == "__main__":
    main()