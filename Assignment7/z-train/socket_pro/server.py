import socket

socket_server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

server_address = ('localhost' , 12345)
socket_server.bind(server_address)

socket_server.listen(1)

print("Echo server is ready to receive messages...")

while True:
    socket_client, client_address = socket_server.accept()
    print(f"Accepted connection from {client_address}")
    
    
    data = socket_client.recv(1024)
    
    if not data:
        break
    
    received_message = data.decode('utf-8')
    print(f"Received from {client_address}: {received_message}")
    
    socket_client.sendall(data)
    socket_client.close()
    
socket_server.close()