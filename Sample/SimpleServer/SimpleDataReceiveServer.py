
import socket
import pickle

if __name__ == '__main__':
    # サーバー設定
    server_addr = "127.0.0.1"
    server_port = 7010
    server_max_client_num = 5
    server_buffer_size = 4096
    
    # ソケット作成 # SOCK_DGRAM = UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as _socket:
        _socket.bind( (server_addr, server_port) )

        # Clientからの要求待ち
        while True:
            recieve_raw_data, client_addr = _socket.recvfrom(server_buffer_size)
            receive_data = pickle.loads(recieve_raw_data)
            print("receive_data:" + str(receive_data))

            _socket.sendto('Success to receive message'.encode(encoding='utf-8'), client_addr)


        # While
    # with socket
