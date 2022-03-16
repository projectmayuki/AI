# -- coding: utf-8 --
# @author Mayuki
# @brief プレイヤーAI
# @file PlayerAI.py

import queue

from GameAIBase import GameAIBase
from AICore import PlayerAICore

class PlayerAI(GameAIBase):

    PLAYER_SERVER_ADDR = "127.0.0.1"

    def __init__(self):
        super().__init__()
    # __init__

    def _create_ai_core(self, receive_data_queue, send_data_queue):
        return PlayerAICore.PlayerAICore(receive_data_queue, send_data_queue)
    # _create_ai_core

    # 受信データに対する対応
    # @param[in] receive_data : pickleでパース済み
    def _receive_and_reply_as_server(self, receive_data, client_addr, socket):

        # プレイヤー情報の解析
        if "PlayerInfo" in receive_data:
            self._receive_data_queue.put({"PlayerInfo" : receive_data["PlayerInfo"]})
        elif "ReceivePlayerOrder" in receive_data:
            # ゲーム側への返答
            player_commands = []
            # player_commands = ["Up", "A"]
            try:
                commands = self._send_data_queue.get(timeout=GameAIBase.GAME_FPS * 2) # タイムアウトはゲームに支障ないように2フレーム分
                for command in commands:
                    player_commands.append(command)
            except queue.Empty:
                pass
            
            self._send_to({"PlayerInput" : player_commands}, client_addr, socket)
        
    # _execute

if __name__ == '__main__':
    print("PlayerAI Start")
    ai = PlayerAI()
    ai.execute()
