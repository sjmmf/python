import socket

if __name__ == "__main__":

    #创建客户端套接字对象
    tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    