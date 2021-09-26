# @author Mayuki
# @brief Game用AIの共通インターフェース
# @file GameAIBase.py

import multiprocessing

class GameAIBase:

    def __init__(self):
        self._process_mgr = multiprocessing.Manager()
        self._receive_data_queue = self._process_mgr.Queue() # ゲームからプレイヤー情報を受信
        self._send_data_queue = self._process_mgr.Queue() # ゲーム側に送る送信コマンド

        self._ai_core =  self._create_ai_core(self._receive_data_queue, self._send_data_queue) # AI用プロセス
        self._server_process = self._create_server_process(self._receive_data_queue, self._send_data_queue) # データ受信・返信用サーバープロセス
    # __init__

    def execute(self):
        pool = multiprocessing.Pool(2)
        pool.apply_async(self._ai_core, args={})
        pool.apply_async(self._server_process, args={})

        pool.close()
        pool.join()

        print("shutdown")
    # execute

    def _create_ai_core(self, receive_data_queue, send_data_queue):
        return None
    # _create_ai_core

    def _create_server_process(self, receive_data_queue, send_data_queue):
        return None
    # _create_server_process

if __name__ == '__main__':
    pass
    #ai = GameAIBase()
    #ai.execute()
