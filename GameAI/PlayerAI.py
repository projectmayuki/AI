# @author Mayuki
# @brief プレイヤーAI
# @file PlayerAI.py

import multiprocessing
import queue

from AI import SampleAI

class PlayerAI:

    def __init__(self):
        self._process_mgr = multiprocessing.Manager()
        self._receive_data_queue = self._process_mgr.Queue() # ゲームからプレイヤー情報を受信
        self._send_data_queue = self._process_mgr.Queue() # ゲーム側に送る送信コマンド

        self._ai = SampleAI.SampleAI()
    # __init__

    def execute(self):
        pool = multiprocessing.Pool(2)
        pool.apply_async(self._ai.execute, args=())

        pool.close()
        pool.join()

        print("shutdown")
    # execute

if __name__ == '__main__':
    ai = PlayerAI()
    ai.execute()
