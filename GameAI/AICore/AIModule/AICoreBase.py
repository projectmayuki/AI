#-- coding: utf-8 --
# @author Mayuki
# @brief AICoreBase
# @file AICoreBase.py

class AICoreBase:

    def __init__(self):
        pass

    # メイン実行
    # サーバープロセスから並列実行されます
    def execute(self):
        pass

    # シャットダウンコマンドがきた時の終了処理
    # サブプロセスの終了など
    def shutdown(self):
        pass
