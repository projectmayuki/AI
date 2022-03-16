# -- coding: utf-8 --
# @author Mayuki
# @brief AIサーバーにシャットダウンコマンドを送信
# @file ShutdownCommond.py

import socket

# 親ディレクトリをimportパスに追加
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Server.ServerDataTranslator import ServerDataTranslator

import TestServerSetting

if __name__ == '__main__':
    # 接続先サーバー設定
    server_setter = TestServerSetting.TestServerSetting()
    server_addr = server_setter.addr()
    server_port = server_setter.port()
    msg_buf_size = server_setter.msg_buf_size()

    #
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect( (server_addr, server_port) )

        # サーバーシャットダウンコマンド
        send_raw_data = { "AdminCommand" : "ShutdownServer", "AdminPassword" : "**" }
        encode_data = ServerDataTranslator.encode(send_raw_data)
        s.sendall(encode_data)
        data = s.recv(msg_buf_size)
        print(ServerDataTranslator.decode(data))
