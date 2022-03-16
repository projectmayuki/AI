#-- coding: utf-8 --
# @author Mayuki
# @brief TestPlayerAICore
# @file TestPlayerAICore.py

import multiprocessing
import queue

class TestPlayerAICore:

    def __init__(self, receive_data_queue, send_data_queue):
        # ゲームから受け取ったデータと送信データのバッファキュー
        self._receive_data_queue = receive_data_queue
        self._send_data_queue = send_data_queue

        # AIモジュール同士でやりとりするデータ
        self._process_mgr = multiprocessing.Manager()
        self._blackboard_queue = self._process_mgr.Queue()

        self._is_stop = False
    # __init__

    def execute(self):
        # 受け取ったデータをもとに対極的視点の思考をするモジュール(ゲーム時間とは別軸で動く)
        #  -> 次の目的を考える(目的地点Aに向かう、敵Bを倒す
        # 受け取ったデータをもとに短期的視点の思考をするモジュール(ゲーム時間とは別軸で動く)
        #  -> 目的地まで向かうための移動方法、敵を倒すための詳細行動決定(ex. 後ろに下がってから、敵を殴る)
        # 短期的思考をもとにゲーム時間の1フレーム内に返答するモジュール(メインスレッド)
        #  -> 後ろに下がる、敵を殴る、上キーを押す
        process_list = []
        p1 = multiprocessing.Process(target=self._test_func, args=(0, self._blackboard_queue))
        p1.start()
        process_list.append(p1)

        for p in process_list:
            p.join()
        print("shutdown ai process")

    # execute

    def _test_func(self, worker_idx, blackboard_queue):
        while self._is_shutdown_command(blackboard_queue) == False:
            player_commands = ["Up", "A"]

            # 未送信データがあれば上書きするために一度ポップ
            try:
                delete_commands = self._send_data_queue.get(timeout=0.1)
            except queue.Empty:
                pass

            self._send_data_queue.put(player_commands)
        
    # _test_func

    def shutdown(self):
        # 適当にshutdownメッセージで埋める
        for i in range(100):
            self._blackboard_queue.put({"AdminCommand" : "Shutdown"})
        

    def _is_shutdown_command(self, blackboard_queue):
        try:
            command = blackboard_queue.get(timeout=5)
        except queue.Empty:
            return False

        if ("AdminCommand" in command) == False:
            return False
        if ("Shutdown" in command["AdminCommand"]) == False:
            return False
        return True
