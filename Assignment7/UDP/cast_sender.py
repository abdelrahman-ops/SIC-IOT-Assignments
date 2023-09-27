import socket

multicast_group = '224.0.0.1'
multicast_port = 5000

multicast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

multicast_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

while True:
    message = input("Enter a multicast message to send (or 'exit' to quit): ")
    if message == 'exit':
        break
    multicast_socket.sendto(message.encode('utf-8'), (multicast_group, multicast_port))

multicast_socket.close()
