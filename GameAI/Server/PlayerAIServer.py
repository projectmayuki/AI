# -- coding: utf-8 --
# @author : Mayuki
# @brief : プレイヤーデータ受信・返信サーバーのインターフェース
# @file : PlayerAIServer.p

from IServerProcess import IServerProcess

class PlayerAIServer(IServerProcess):

    def __init__(self, receive_data_queue, send_data_queue):
        super().__init__()
        self._receive_data_queue = receive_data_queue
        self._send_data_queue = send_data_queue
    # __init__

    # データ受信
    def _execute(self, receive_data, client_addr, socket):
        # このフレームのデータをキューにバッファ

        # 前フレームまでのデータを使って思考した送信コマンドをキューから取得して送り返す
        pass
    # _execute

if __name__ == '__main__':
    pass
