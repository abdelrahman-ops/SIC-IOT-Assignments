import socket

socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 12345)

try:
    while True:
        message = input("Enter your message: ")
        
        print("Sending {!r}".format(message))
        
        sent = socket_client.sendto(message, server_address)

        print("Waiting to receive")

        data, server = socket_client.recvfrom(4096)

        print('Received {!r}'.format(data))

finally:
    print("Closing socket")
    socket_client.close()
