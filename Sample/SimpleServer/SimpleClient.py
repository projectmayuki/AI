
import socket

if __name__ == '__main__':
    # 接続先サーバー設定
    server_addr = '127.0.0.1'
    server_port = 7010
    msg_buf_size = 4096

    #
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect( (server_addr, server_port) )

        s.sendall(b'Send message. by client')

        data = s.recv(msg_buf_size)
        print(data.decode())
