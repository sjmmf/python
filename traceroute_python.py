import socket        #导入socket模块
import time          #导入time模块
import struct        #导入struct模块

def trace(dest_name):
    dest_addr = socket.gethostbyname(dest_name)   #获取目的网站ip
    print('dest host is:\n%s'%dest_addr)
    port = 20000     #设置端口
    max_hops = 30   
    ttl = 1          #初始化ttl
    start_time = time.time()

    while True:
        recv_socket = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
        send_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)
        send_socket.setsockopt(socket.SOL_IP,socket.IP_TTL,ttl)

        timeout = struct.pack('ll', 2, 0)
        recv_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVTIMEO,timeout)
        recv_socket.bind(("",port))
        send_socket.sendto(bytes("","utf-8"),(dest_name,port))
        
        curr_addr = None
        curr_name = None

        judge = False
        tries = 1
        
        while not judge and tries > 0 :
            try:
                _, curr_addr = recv_socket.recvfrom(512)
                judge = True
                curr_addr = curr_addr[0]
                try:
                    curr_name = socket.gethostbyaddr(curr_addr)[0]
                except socket.error:
                    curr_name = curr_addr
            except socket.error:
                tries -=1
        
        send_socket.close()
        recv_socket.close()

        if not judge:
            pass

        if curr_addr is not None:
            curr_host = "%d midway:%s  %dms"%(ttl,curr_addr,(time.time()-start_time)*1000)
        else:
            curr_host = '%d midway:can not trace this one'%(ttl)

        print(curr_host)
        ttl +=1

        if curr_addr == dest_addr or ttl >max_hops:
            break        

if __name__ == '__main__':
    dest_name = input('请输入目标网址：')
    trace(dest_name)
