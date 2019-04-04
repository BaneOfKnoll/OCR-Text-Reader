import socket
import sys

#create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to the port where the server
server_address = ('localhost', 10000)
print(sys.stderr, 'connecting to %s port %s'  % server_address)
sock.connect(server_address)

try:
    #send data packet
    message = 'this is the transmitted message'.encode()
    print(sys.stderr, 'sending "%s"' % message)
    sock.sendall(message)

    #Wait and look for response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print(sys.stderr, 'received "%s"' % data)

finally:
    print(sys.stderr, 'closing socket')
    sock.close()
