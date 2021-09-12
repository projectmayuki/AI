
import socket
import pickle

if __name__ == '__main__':
    # サーバー設定
    server_addr = "127.0.0.1"
    server_port = 7010
    server_max_client_num = 5
    server_buffer_size = 4096
    
    # ソケット作成 # SOCK_DGRAM = UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as _socket:
        _socket.bind( (server_addr, server_port) )

        # Clientからの要求待ち
        while True:
            recieve_raw_data, client_addr = _socket.recvfrom(server_buffer_size)
            receive_data = pickle.loads(recieve_raw_data)

            if isinstance(receive_data, dict) == False:
                _socket.sendto('Error : Send data was invalid format.'.encode(encoding='utf-8'), client_addr)
                print("receive_data(Failed):" + str(receive_data))
                continue
            # if

            if "AdminCommand" in receive_data:
                if "AdminPassword" in receive_data == False:
                    _socket.sendto('Error : AdminCommand needs AdminPassword.'.encode(encoding='utf-8'), client_addr)
                    print("receive_data(Failed)" + str(receive_data))
                    continue
                #
                if receive_data["AdminCommand"] == "ShutdownServer":
                    _socket.sendto('AdminCommand was receiverd. Server shutdown start.'.encode(encoding='utf-8'), client_addr)
                    print("Server shutdown" + str(receive_data))
                    break
            elif "Data" in receive_data:
                _socket.sendto('Send data was recieved.'.encode(encoding='utf-8'), client_addr)
                print("receive_data(Success):" + str(receive_data))
                pass
            else:
                _socket.sendto('Error : Send data was invalid format.'.encode(encoding='utf-8'), client_addr)
                print("receive_data(Failed):" + str(receive_data))
                pass


        # While
    # with socket
