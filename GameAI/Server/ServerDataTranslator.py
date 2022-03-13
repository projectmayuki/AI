# -- coding: utf-8 --
# @author : Mayuki
# @brief : データ送受信の際のencoder / decoder
# @file : ServerDataTranslator.py

import pickle
import json

class ServerDataTranslator:

    DATA_FORMAT = 0 # json
    
    def __init__(self):
        pass
    # __init__

    @classmethod
    def set_mode_json(self):
        ServerDataTranslator.DATA_FORMAT = 0
    # set_mode_json

    @classmethod
    def set_mode_pickle(self):
        ServerDataTranslator.DATA_FORMAT = 1
    # set_mode_pickle

    @classmethod
    # pythonで扱えるオブジェクトからbyteに変換
    def encode(self, raw_data):
        if self._is_mode_json() == True:
            return self._encode_json(raw_data)
        elif self._is_mode_pickle == True:
            return self._encode_pickle(raw_data)
        return None
    # encode

    @classmethod
    # byteデータからpythonで扱えるオブジェクトに変換
    def decode(self, raw_data):
        if self._is_mode_json() == True:
            return self._decode_json(raw_data)
        elif self._is_mode_pickle == True:
            return self._decode_pickle(raw_data)
        return None
    # decode

    @classmethod
    def _is_mode_json(self):
        return ServerDataTranslator.DATA_FORMAT == 0
    # _is_mode_json

    @classmethod
    def _is_mode_pickle(self):
        return ServerDataTranslator.DATA_FORMAT == 1
    # _is_mode_pickle

    @classmethod
    def _encode_json(self, raw_data):
        return json.dumps(raw_data).encode()
    # _encode_json

    @classmethod
    def _encode_pickle(self, raw_data):
        return pickle.dumps(raw_data)
    # _encode_pickle

    @classmethod
    def _decode_json(self, raw_data):
        return json.loads(raw_data.decode())
    # _encode_json

    @classmethod
    def _decode_pickle(self, raw_data):
        return pickle.loads(raw_data)
    # _encode_pickle
    
# class ServerDataTranslator
