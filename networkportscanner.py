import socket

def scan_ports(target):
    # Common ports to check: 21 (FTP), 22 (SSH), 80 (HTTP), 443 (HTTPS)
    common_ports = [21, 22, 80, 443]
    print(f"Starting scan on host: {target}")
    
    for port in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) # Wait 1 second for response
        result = sock.connect_ex((target, port))
        
        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED")
        sock.close()

if __name__ == "__main__":
    # You can replace this with a local IP or 'google.com'
    target_host = "127.0.0.1" 
    scan_ports(target_host)
