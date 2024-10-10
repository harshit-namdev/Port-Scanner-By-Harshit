import socket
from termcolor import colored, cprint

def scan(target, ports):
    cprint('\n\n' + 'Starting Scan For : ' + str(target),'blue')
    for port in range(1, ports + 1):  
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        cprint("[*] Port {} is open".format(port), 'red')  
        sock.close()
    except:
       cprint("[*] Port {} is Closed".format(port), 'yellow')

targets = input('[#] Enter your target/s IP address/s (use "," to differentiate between them): ')
colored_targets = colored(targets, 'green')
print(colored_targets)

ports = int(input('[#] Enter the Number of ports you want to scan: '))
colored_ports = colored(str(ports), 'green')
print(colored_ports)

if ',' in targets:
    cprint('[+++] Scanning Multiple Targets ','magenta')
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    cprint('[+] Scanning Single Target ','magenta')
    scan(targets, ports)
