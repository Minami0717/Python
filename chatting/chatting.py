import socket

ip = '192.168.0.222'
port = 50001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip,port))

client_socket.send('aa'.encode('UTF-8'))

client_socket.close()
print('연결 종료')
