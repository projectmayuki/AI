# -*- coding: utf-8 -*-

import socket
#import pickle
import json

if __name__ == '__main__':
    # 接続先サーバー設定
    server_addr = '127.0.0.1'
    server_port = 7010
    msg_buf_size = 4096

    #
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect( (server_addr, server_port) )

        # サーバーシャットダウンコマンド
        send_raw_data = { "AdminCommand" : "ShutdownServer", "AdminPassword" : "**" }
        #encode_data = pickle.dumps(send_raw_data)
        encode_data = json.dumps(send_raw_data).encode()
        s.sendall(encode_data)
        data = s.recv(msg_buf_size)
        #print(pickle.loads(data))
        print(json.loads(data.decode()))
