# -- coding: utf-8 --
# @author : Mayuki
# @brief : データ受信・返信サーバーのインターフェース
# @file : IServerProcess.py

import socket
import pickle

class IServerProcess:

    ADDR = "127.0.0.1"
    
    def __init__(self):
        pass
    # __init__

    def execute(self, port, opt = {"ServerMaxClientNum" : 5, "ServerBufferSize" : 4096}):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as _socket:
            _socket.bind( (IServerProcess.ADDR, port) )

            while True:
                recieve_raw_data, client_addr = _socket.recvfrom(opt["ServerBufferSize"])
                receive_data = pickle.loads(recieve_raw_data)

                if self._receive_admin_command(receive_data, client_addr, _socket):
                    break
                
                self._execute(receive_data, client_addr, _socket)
            # while
        # with socket
    # execute

    # 受信データに対する対応
    # @param[in] receive_data : pickleでパース済み
    def _execute(self, receive_data, clent_addr, socket):
        pass
    # _execute

    def _send_to(self, send_data_raw, client_addr, socket):
        socket.sendto(pickle.dumps(send_data_raw), client_addr)
    # _send_to

    def _receive_admin_command(self, receive_data, client_addr, socket):
        if not isinstance(receive_data, dict):
            return False
        if not ("AdminCommand" in receive_data):
            return False
        if not ("AdminPassword" in receive_data):
            return False
        # FIXME : AdminPassword照合

        if receive_data["AdminCommand"] == "ShutdownServer":
            self._send_to("Shutdown start.", client_addr, socket)
            return True
    # _receive_admin_command

if __name__ == '__main__':
    server = IServerProcess()
    server.execute(7010)
