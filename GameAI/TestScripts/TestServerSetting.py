# -- coding: utf-8 --
# @author Mayuki
# @brief テスト用サーバーの一通りの設定
# @file TestServerSetting.py

# 親ディレクトリをimportパスに追加
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Server.ServerDataTranslator import ServerDataTranslator

class TestServerSetting:

    def __init__(self):
        ServerDataTranslator.set_mode_json()
    #

    @classmethod
    def addr(self):
        return '127.0.0.1'
    #

    @classmethod
    def port(self):
        return 7010
    #

    @classmethod
    def msg_buf_size(self):
        return 4096
    #
#
    
