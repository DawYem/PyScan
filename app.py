import socket
ports = []
print("How many port(s) do you want to check?")
answer=int(input())
for i in range(answer):
 print("Enter port number to check:")
 port = int(input())
 ports.append(port)
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Current Device Name: " + hostname + " | IP Address: " + IPAddr)
def scan_port(ip, port):
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result=sock.connect_ex((ip,port))
    if result==0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
print("Scanning ports on " + IPAddr+ "...")
for port in ports:
    scan_port(IPAddr, port)