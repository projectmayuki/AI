
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

        # Data型の送信
        send_raw_data = { "Data" : {"Trans" : (0, 1, 2), "Name" : "サンプルオブジェクト"} }
        s.sendall(pickle.dumps(send_raw_data))

        data = s.recv(msg_buf_size)
        print(data.decode())

        # 不正フォーマットデータの送信
        send_raw_data = "AAAA"
        s.sendall(pickle.dumps(send_raw_data))
        data = s.recv(msg_buf_size)
        print(data.decode())
        

        # サーバーシャットダウンコマンド
        send_raw_data = { "AdminCommand" : "ShutdownServer", "AdminPassword" : "**" }
        s.sendall(pickle.dumps(send_raw_data))
        data = s.recv(msg_buf_size)
        print(pickle.loads(data))
