import socket
import sys

#create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind the socket to the port
server_address = ('localhost', 10000)
print(sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)


# listen for incoming connections

sock.listen()

while True:
    #wait for connection
    print(sys.stderr, 'waiting on connection')
    connection, client_address = sock.accept()

try:
    print(sys.stderr, 'connection from', client_address)

    #recieve data and bounce it

    while True:
        data = connection.recv(16)
        print(data)
        print(sys.stderr, 'received "%s"' % data)
        if data:
            print(sys.stderr, 'Bouncing data back to client')
            connection.sendall(data)
        else:
            print(sys.stderr, 'End of data stream', client_address)
            break
finally:
    #clean connection
    connection.close()

