import socket

multicast_group = '224.0.0.1'
multicast_port = 5000

multicast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

multicast_socket.bind(('', multicast_port))

multicast_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(multicast_group) + socket.inet_aton('0.0.0.0'))

print(f"Listening for multicast messages on {multicast_group}:{multicast_port}")

while True:
    data, sender_address = multicast_socket.recvfrom(1024)
    print(f"Received multicast message from {sender_address}: {data.decode('utf-8')}")
