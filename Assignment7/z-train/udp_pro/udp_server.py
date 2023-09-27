import socket

udp_socket = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

server_address = ('localhost' , 12345)
print("starting up on {} port {} ".format(*server_address))

udp_socket.bind(server_address)

while True:
    print("waiting to receive message")
    data , client_address = udp_socket.recvfrom(4096)
    
    print("Received {} bytes from {}".format(len(data) , client_address))
    print(data)
    
    
    if data:
        sent = udp_socket.sendto(data, client_address)
        
        print('sent {} bytes back to {}'.format(sent , client_address))