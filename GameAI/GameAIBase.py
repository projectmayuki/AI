# @author Mayuki
# @brief Game用AIの共通インターフェース
# @file GameAIBase.py

import time
import multiprocessing
from Server.IServerProcess import IServerProcess

class GameAIBase(IServerProcess):

    def __init__(self):
        self._process_mgr = multiprocessing.Manager()
        self._receive_data_queue = self._process_mgr.Queue() # ゲームからプレイヤー情報を受信
        self._send_data_queue = self._process_mgr.Queue() # ゲーム側に送る送信コマンド

        self._ai_core =  self._create_ai_core(self._receive_data_queue, self._send_data_queue) # AI用プロセス
    # __init__

    def execute(self):
        pool = multiprocessing.Pool(1)
        pool.apply_async(self._ai_core.execute, args={})
        pool.close()

        self.execute_server(self._get_server_port())

        pool.join()

        print("shutdown")
    # execute

    def _create_ai_core(self, receive_data_queue, send_data_queue):
        return None
    # _create_ai_core

    def _get_server_port(self):
        return 7010
    # _get_server_port

    # 受信データに対する対応
    # @param[in] receive_data : pickleでパース済み
    def _receive_and_reply_as_server(self, receive_data, client_addr, socket):
        pass
    # _execute

if __name__ == '__main__':
    pass
    #ai = GameAIBase()
    #ai.execute()
