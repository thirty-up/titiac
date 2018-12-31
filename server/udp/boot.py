#coding=utf-8
"""
@since: 2018-12-28
@version: 0.0.1
@author: 1949.LIU
"""

from server.udp.udpsocket import Server

_UDP_PORT = 9999
_UDP_BUFFER_SIZE = 1024

def start():
    """
        init a instance of the udp server
    """
    
    global server 
    server = Server(_UDP_PORT)
    server.listen(receive, _UDP_BUFFER_SIZE)
    
def receive(data, addr):
    """
        deal with the message of received from aps
    """
    
    print(data)