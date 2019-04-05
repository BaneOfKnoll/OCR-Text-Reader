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
    print("Hello there, I got to Waiting on connection")
    print(sys.stderr, 'waiting on connection')
    connection, client_address = sock.accept()

print("Hello there, I got to Up to the try function")
print(sys.stderr, 'connection from', client_address)
#recieve data and bounce it

try:
        print(sys.stderr, 'connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print("hello there")
            print(sys.stderr, 'received "%s"' % data)
            if data:
                print(sys.stderr, 'sending data back to the client')
                connection.sendall(data)
            else:
                print(sys.stderr, 'no more data from', client_address)
                break
except:
    print("Nothing yet")

#print("Hello World")

finally:
    #clean connection
    connection.close()
