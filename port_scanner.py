import socket


def scan_port(host, port):
    try:
        # Create a socket object
        conn_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn_socket.connect((host, port))
        print(f'[+] {port}/TCP open')
        conn_socket.close()
    except:
        print(f'[-] {port}/TCP closed')


def port_scan(target_host, target_ports):
    try:
        # Resolve the target host to its IP address
        target_ip = socket.gethostbyname(target_host)
    except:
        print(f'[-] Cannot resolve {target_host}')
        return

    try:
        # Get the hostname associated with the IP address
        target_name = socket.gethostbyaddr(target_ip)
        print('')
        print(f'[+] Scan Result for: {target_name[0]}')
        print('')
    except:
        print(f'[+] Scan Result for: {target_ip}')

    socket.setdefaulttimeout(1)

    for port in target_ports:
        print(f'Scanning Port: {port}')
        scan_port(target_host, port)


if __name__ == '__main__':
    print('')
    print('WELCOME TO PORT SCANNER')
    print('')
    # Define a dictionary of well-known ports and their descriptions
    well_known_ports = {
        20: "FTP (File Transfer Protocol) - Data",
        21: "FTP (File Transfer Protocol) - Control",
        22: "SSH (Secure Shell)",
        23: "Telnet",
        25: "SMTP (Simple Mail Transfer Protocol)",
        53: "DNS (Domain Name System)",
        80: "HTTP (Hypertext Transfer Protocol)",
        443: "HTTPS (HTTP Secure)",
        110: "POP3 (Post Office Protocol)",
        143: "IMAP (Internet Message Access Protocol)",
        3389: "RDP (Remote Desktop Protocol)",
        137: "NetBIOS Name Service",
        138: "NetBIOS Datagram Service",
        139: "NetBIOS Session Service",
        161: "SNMP (Simple Network Management Protocol)",
        162: "SNMP Trap",
        445: "Microsoft-DS (Microsoft Directory Services)",
        3306: "MySQL Database",
        5432: "PostgreSQL Database",
        1521: "Oracle Database",
    }

    print("Well-known ports and their descriptions:")
    for port, description in well_known_ports.items():
        print(f"{port}: {description}")
    print('')
    target_host = input("Enter the target host (e.g. google.com): ")
    target_ports_input = input("Enter the target ports (comma-separated) (e.g. 80, 20, 443): ")
    target_ports = [int(port) for port in target_ports_input.split(",")]
    port_scan(target_host, target_ports)
