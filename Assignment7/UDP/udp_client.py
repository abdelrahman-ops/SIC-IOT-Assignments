import socket

server_ip = '127.0.0.1'
server_port = 12345

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Enter a message to send to the server (or 'exit' to quit): ")
    if message == 'exit':
        break
    udp_socket.sendto(message.encode('utf-8'), (server_ip, server_port))

udp_socket.close()
