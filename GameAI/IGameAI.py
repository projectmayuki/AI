# @author Mayuki
# @brief Game用AIの共通インターフェース
# @file IGameAI.py

class IGameAI:

    def __init__(self):
        self._server = None # データ受信・返信用サーバープロセス
        self._core = None # AI用プロセス
        pass
    # __init__

    def execute(self):
        print("AI process start.")
        pass
    # execute

if __name__ == '__main__':
    ai = IGameAI()
    ai.execute()
