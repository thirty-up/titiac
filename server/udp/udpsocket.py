#coding=utf-8
"""
@since: 2018-12-28
@version: 0.0.1
@author: LIUJG
@contact: 575616873@QQ
"""

import socket
import threading

class Server(threading.Thread):
    """
    udp server
    """
    
    _server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    _host = socket.gethostname()
    print (_host)
    
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.threadID = 1199
        self.name = 'upd-server-thread'
        self._server.bind(('', port))
        pass
    
    def run(self):
        print ("开始线程：" + self.name)
        while True:
            try:
                data, addr = self._server.recvfrom(self.buffersize)
                print('Receive from: %s data: %s.' % (addr, data))
                self.callback(data, addr)
            except:
                print('Receive data error')
                pass
        print ("退出线程：" + self.name)
    
    def listen(self, func, buffersize=1024):
        self.callback = func
        self.buffersize = buffersize
        self.start()
        pass
        
    def send_to(self, address, data):
        self._server.sendto(data, address)
        pass
    
    
class Client:
    """
    udp client
    """
    
    def __init__(self):
        self._client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
    def send(self, address, data):
        self._client.sendto(data, address)
        
    def close(self):
        self._client.close()