import socket
import threading

bind_ip="0.0.0.0"
bind_port=9999

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

#Max backlog connection of 5
server.listen(5)

#Tell we're listening
print("[*] Listening on %s:%d"%(bind_ip,bind_port))

def handle_client(client_socket):
    #Receive bytesize
    request=client_socket.recv(1024)
    print("[*] Received: %s"%request)

    #Send back an ACK
    client_socket.send(b"ACK!")
    #Close socket
    client_socket.close()

while True:
    #Accept client connection
    client,addr=server.accept()
    print("[*] Accepted connection from %s:%d"%(addr[0],addr[1]))

    #Client thread to handle incoming data
    client_handler=threading.Thread(target=handle_client,args=(client,))

    #Start client
    client_handler.start()
