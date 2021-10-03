#-- coding: utf-8 --
# @author Mayuki
# @brief PlayerAICore
# @file PlayerAICore.py

import multiprocessing

class PlayerAICore:

    def __init__(self, receive_data_queue, send_data_queue):
        # ゲームから受け取ったデータと送信データのバッファキュー
        self._receive_data_queue = receive_data_queue
        self._send_data_queue = send_data_queue

        # AIモジュール同士でやりとりするデータ
        self._process_mgr = multiprocessing.Manager()
        self._blackboard_queue = self._process_mgr.Queue()
    # __init__

    def execute(self):
        # 受け取ったデータをもとに対極的視点の思考をするモジュール(ゲーム時間とは別軸で動く)
        #  -> 次の目的を考える(目的地点Aに向かう、敵Bを倒す
        # 受け取ったデータをもとに短期的視点の思考をするモジュール(ゲーム時間とは別軸で動く)
        #  -> 目的地まで向かうための移動方法、敵を倒すための詳細行動決定(ex. 後ろに下がってから、敵を殴る)
        # 短期的思考をもとにゲーム時間の1フレーム内に返答するモジュール(メインスレッド)
        #  -> 後ろに下がる、敵を殴る、上キーを押す
        pool = multiprocessing.Pool(2)
        pool.apply_async(self._test_func, args={})
        pool.close()

        pool.join()
    # execute

    def _test_func(self):
        pass
    # _test_func
