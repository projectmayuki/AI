# -- coding: utf-8 --
# @author Mayuki
# @brief プレイヤーAI
# @file PlayerAI.py

from GameAIBase import GameAIBase

from AI.PlayerAICore import PlayerAICore
from Server.PlayerAIServer import PlayerAIServer

class PlayerAI(GameAIBase):

    def __init__(self):
        super().__init__()
    # __init__

    def _create_ai_core(self, receive_data_queue, send_data_queue):
        return PlayerAICore(receive_data_queue, send_data_queue)
    # _create_ai_core

    def _create_server_process(self, receive_data_queue, send_data_queue):
        return PlayerAIServer(receive_data_queue, send_data_queue)

if __name__ == '__main__':
    ai = PlayerAI()
    ai.execute()
