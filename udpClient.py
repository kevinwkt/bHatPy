import socket

target_host="127.0.0.1"
target_port=80

#1.Create socket client obj
client=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#2.Send data
client.sendto(b'AAAAAABBC',(target_host,target_port))

#3.Receive data
data,addr=client.recvfrom(4096)

print(data)
