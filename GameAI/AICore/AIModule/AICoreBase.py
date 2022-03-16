#-- coding: utf-8 --
# @author Mayuki
# @brief AICoreBase
# @file AICoreBase.py

class AICoreBase:

    # receive_data_queue : サーバープロセスから受け取るデータキュー
    # send_data_queue    : サーバープロセスにデータ送信するキュー 
    def __init__(self, receive_data_queue, send_data_queue):
        pass

    # メイン実行
    # サーバープロセスから並列実行されます
    def execute(self):
        pass

    # シャットダウンコマンドがきた時の終了処理
    # サブプロセスの終了など
    def shutdown(self):
        pass

    # サーバーへのコマンド送信キューにput
    def _send_command_to_server(self, command):
        pass

    # サーバーからのコマンド受信キューからget
    def _receive_command_from_server(self):
        return None
