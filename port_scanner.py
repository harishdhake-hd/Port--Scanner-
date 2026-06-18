import socket
import sys
from datetime import datetime

def scan_ports(target, start_port, end_port):
    print("-" * 50)
    print(f"Scanning Target: {target}")
    print(f"Scanning started at: {datetime.now()}")
    print("-" * 50)

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Could not resolve hostname.")
        sys.exit()

    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "unknown"
            print(f"[OPEN] Port {port} -- {service}")
            open_ports.append(port)
        sock.close()

    print("-" * 50)
    print(f"Scan complete. {len(open_ports)} open ports found.")

if __name__ == "__main__":
    target = input("Enter target IP or hostname: ")
    start = int(input("Start port: "))
    end = int(input("End port: "))
    scan_ports(target, start, end)
