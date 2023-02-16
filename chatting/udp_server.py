# 소켓 프로그래밍에 필요한 API를 제공하는 모듈
import socket

ip = '192.168.0.232'
#ip = 'localhost'
port = 50001

# 소켓 객체 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 소켓 주소 정보 할당
server_socket.bind((ip,port))

# 클라이언트로 받은 데이터 수신
while True:
    data, address = server_socket.recvfrom(1024)
    print('클라이언트 IP 주소 :', address[0])
    print('받은 메시지 :', data.decode('UTF-8'))

# 소켓 닫기
server_socket.close()
print('[연결 종료]')
