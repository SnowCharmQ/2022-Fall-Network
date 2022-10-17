from socket import *

server_name = "127.0.0.1"
server_port = 12000

client_socket = socket(AF_INET, SOCK_STREAM)
while True:
    message = input("Input the qname and rdtype:")
    client_socket.sendto(message.encode(), (server_name, server_port))
    rec_msg, server_addr = client_socket.recvfrom(2048)
    print(rec_msg)
