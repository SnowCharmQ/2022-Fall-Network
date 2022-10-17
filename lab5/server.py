import dns.resolver
from socket import *

server_port = 12000
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('127.0.0.1', server_port))
print("The server is ready to receive")

while True:
    message, client_addr = server_socket.recvfrom(2048)
    modified_message = message.decode()
    qname, rdtype = modified_message.split(" ")
    ans = dns.resolver.resolve(qname=qname, rdtype=rdtype, raise_on_no_answer=False)
    msg = ""
    for i in ans.response.answer:
        for j in i.items:
            msg += str(j)
            msg += " "
    server_socket.sendto(msg.encode(), client_addr)
