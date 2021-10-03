# -- coding: utf-8 --
# @author Mayuki
# @brief プレイヤーAI
# @file PlayerAI.py

from GameAIBase import GameAIBase

from AICore.PlayerAICore import PlayerAICore

class PlayerAI(GameAIBase):

    PLAYER_SERVER_ADDR = "127.0.0.1"

    def __init__(self):
        super().__init__()
    # __init__

    def _create_ai_core(self, receive_data_queue, send_data_queue):
        return PlayerAICore(receive_data_queue, send_data_queue)
    # _create_ai_core

    # 受信データに対する対応
    # @param[in] receive_data : pickleでパース済み
    def _receive_and_reply_as_server(self, receive_data, clent_addr, socket):
        pass
    # _execute

if __name__ == '__main__':
    ai = PlayerAI()
    ai.execute()
