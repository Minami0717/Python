# 소켓 프로그래밍에 필요한 API 제공
import socket

ip = '192.168.0.230'
#ip = 'localhost'
port = 50001

# 소켓 객체 생성 AF_INET = IPv4
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 서버로 데이터 전송
while True:
    message = input('보낼 메시지 : ')
    client_socket.sendto(message.encode('UTF-8'), (ip,port))

# 소켓 닫기
client_socket.close()
print('[연결 종료]')
