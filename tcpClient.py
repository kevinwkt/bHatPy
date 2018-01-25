import socket

target_host="www.google.com"
target_port=80

#1.Create Socket Obj
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#2.Connect to server
client.connect((target_host,target_port))

#3.Send data
client.send(b'GET / HTTP\1.1\r\nHost: google.com\r\n\r\n')

#Receive data
response= client.recv(4096)

print(response)
