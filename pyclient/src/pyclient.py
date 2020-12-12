import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port on the server given by the caller
server_address = (sys.argv[1], 10000)
target_number = sys.argv[2]

print ('connecting to %s port %s' % server_address, file=sys.stderr)

sock.connect(server_address)
sock_ip, sock_num = sock.getsockname()
print("{} {} {}".format(sock_ip, sock_num, target_number))

while int(sock_num) <= int(target_number):
  sock.close()
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect(server_address)
  sock_ip, sock_num = sock.getsockname()
  print("{} {}".format(sock_ip, sock_num))

  try:

    message = 'This is the message.  It will be repeated.'
    print ('sending "%s"' % message,file=sys.stderr)
    sock.sendall(message.encode())

    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
      data = sock.recv(16)
      amount_received += len(data)
      print ('received "%s"' % data,file=sys.stderr)

  finally:
     sock.close()
     print ('closing connection {} {}'.format(sock_ip, sock_num),file=sys.stderr)

