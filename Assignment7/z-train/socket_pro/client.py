import socket

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost' , 12345)
socket_client.connect(server_address)

while True:
    message = input("Enter a message or 'exit' to quit: ")
    
    if message == 'exit':
        break
    
    socket_client.sendall(message.encode('utf8'))
    
    response = socket_client.recv(1024)
    print(f"Received from server: {response.decode('utf-8')}")


socket_client.close()

