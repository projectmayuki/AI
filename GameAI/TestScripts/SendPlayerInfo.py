
import socket
import pickle

if __name__ == '__main__':
    # 接続先サーバー設定
    server_addr = '127.0.0.1'
    server_port = 7010
    msg_buf_size = 4096

    #
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect( (server_addr, server_port) )

        # サーバーシャットダウンコマンド
        send_raw_data = { "PlayerInfo" : {"Trans" : (0, 0, 0)} }
        s.sendall(pickle.dumps(send_raw_data))
        data = s.recv(msg_buf_size)
        print(pickle.loads(data))
