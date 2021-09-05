
import socket

if __name__ == '__main__':
    # サーバー設定
    server_addr = "127.0.0.1"
    server_port = 7010
    server_max_client_num = 5
    server_buffer_size = 4096
    
    # ソケット作成 # SOCK_DGRAM = UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as _socket:
        _socket.bind( (server_addr, server_port) )

        # socket待機 TCP
        #_socket.listen(server_max_client_num)

        # Clientからの要求待ち
        while True:
            # 接続確立 TCP
            #conn, addr = _socket.accept()

            # データ受信 TCP
            #data = conn.recv(server_buffer_size)
            #print('data -> {}, add -> {}'.format(data, addr))

            # データ送信
            #conn.sendall(b'Receive client message. By server')

            message, client_addr = _socket.recvfrom(server_buffer_size)
            message = message.decode(encoding='utf-8')
            print('message : ' + message)

            _socket.sendto('Success to receive message'.encode(encoding='utf-8'), client_addr)


        # While
    # with socket
