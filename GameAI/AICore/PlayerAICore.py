#-- coding: utf-8 --
# @author Mayuki
# @brief PlayerAICore
# @file PlayerAICore.py

import time

class PlayerAICore:

    def __init__(self, receive_data_queue, send_data_queue):
        self._receive_data_queue = receive_data_queue
        self._send_data_queue = send_data_queue
        self._is_stop = False
    # __init__

    def execute(self):
        while self._is_stop == False:
            start_t = time.time()

            # 受け取ったデータをもとに対極的視点の思考をするモジュール(ゲーム時間とは別軸で動く)
            #  -> 次の目的を考える(目的地点Aに向かう、敵Bを倒す
            # 受け取ったデータをもとに短期的視点の思考をするモジュール(ゲーム時間とは別軸で動く)
            #  -> 目的地まで向かうための移動方法、敵を倒すための詳細行動決定(ex. 後ろに下がってから、敵を殴る)
            # 短期的思考をもとにゲーム時間の1フレーム内に返答するモジュール
            #  -> 後ろに下がる、敵を殴る、上キーを押す
            self._execute_core()

            elapsed_t = time.time() - start_t # sec
            diff = self._frame_time - elapsed_t
            if diff > 0:
                time.sleep(diff)

            
    # execute

    def stop(self):
        self._is_stop = True
    # stop

    def _execute_core(self):
        pass
    # _execute_core

    def _frame_time(self):
        return 1.0 / 60.0 # 60fps
