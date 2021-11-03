import socket
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
#server_name = sys.argv[1]
server_name = '0.0.0.0'
server_address = (server_name, 10000)
#print ('starting up on %s port %s' % server_address, file=sys.stderr)
sock.bind(server_address)
sock.listen(1)

while True:
    try:
        print ('{"level":"info","name":"fred2","home":"bedrock2"}', file=sys.stderr)
        print ('not json log entry', file=sys.stderr)
        time.sleep(60)
    finally:
        print ('{"level":"info","name":"exit","home":"exit"}', file=sys.stderr)
        
