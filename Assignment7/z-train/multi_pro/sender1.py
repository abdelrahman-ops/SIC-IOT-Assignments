import socket
import struct

message = b'very important data'
multicast_group = ('224.10.10.10' , 10000)

multi_socket = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

multi_socket.settimeout(0.2)

ttl = struct.pack('b' , 1)

multi_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
