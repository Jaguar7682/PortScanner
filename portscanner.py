import socket
import termcolor



def scan(target, ports):
	print('\n' + ' Starting Scan For ' + str(target))
	for port in range(1, ports):
		scanport(target, port)



def scanport(ipaddress, port):
	try:
		newsocket =  socket.socket()
		newsocket.connect((ipaddress, port))
		print("[+] Port Opened " + str(port))
		newsocket.close()

	except:
		pass



targets = input("[*] Enter Targets to scan (If you have multiple targets, split them by using ','): ")
ports = int(input("[*] Enter the number of ports you want to scan: "))


if ',' in targets:
	print(termcolor.colored(("[*] Scanning Multiple Targets..."), 'green'))
	for ip in targets.split(','):
		scan(ip.strip(' '), ports)
else:
	scan(targets,ports)
