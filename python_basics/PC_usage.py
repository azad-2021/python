import requests
import socket

def check_localhost():
	host = socket.gethostbyname('localhost')
	print(host)
	if host == "127.0.0.1":
		return True
	pass

print(check_localhost())

def check_connectivity():
	status_code = requests.get("http://www.google.com")
	status_code = str(status_code)
	print(status_code)
	if status_code == "<Response [200]>":
		return True
	pass

print(check_connectivity())