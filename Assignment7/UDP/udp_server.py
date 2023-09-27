import socket

# Define the server's IP address and port
server_ip = '127.0.0.1'
server_port = 12345

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_socket.bind((server_ip, server_port))

print(f"UDP server listening on {server_ip}:{server_port}")

while True:
    data, client_address = udp_socket.recvfrom(1024)
    print(f"Received message from {client_address}: {data.decode('utf-8')}")
