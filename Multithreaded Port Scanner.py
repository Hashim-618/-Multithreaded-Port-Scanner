# scripts/port_scanner.py
import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(target, port):
    try:
        with socket.socket() as s:
            s.settimeout(1)
            s.connect((target, port))
            print(f"[+] Port {port} is OPEN")
    except:
        pass

def main():
    target = input("Enter Target IP or Domain: ")
    ports = range(1, 1025)

    print(f"[*] Scanning {target}...\n")

    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in ports:
            executor.submit(scan_port, target, port)

if __name__ == "__main__":
    main()
