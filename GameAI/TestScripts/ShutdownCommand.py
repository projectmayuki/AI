# -*- coding: utf-8 -*-

import socket

# 親ディレクトリをimportパスに追加
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Server.ServerDataTranslator import ServerDataTranslator

if __name__ == '__main__':
    # 接続先サーバー設定
    server_addr = '127.0.0.1'
    server_port = 7010
    msg_buf_size = 4096

    ServerDataTranslator.set_mode_json()

    #
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect( (server_addr, server_port) )

        # サーバーシャットダウンコマンド
        send_raw_data = { "AdminCommand" : "ShutdownServer", "AdminPassword" : "**" }
        encode_data = ServerDataTranslator.encode(send_raw_data)
        s.sendall(encode_data)
        data = s.recv(msg_buf_size)
        print(ServerDataTranslator.decode(data))
