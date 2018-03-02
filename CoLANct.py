# !/usr/bin/python
# -*- coding: UTF-8 -*-

from socket import *
from threading import Thread
import thread
import os
import time
import sys
import curses
import Main
from wx.lib.pubsub import pub
import wx

class Sender(object):
    def __init__(self, parent):
        self.parent = parent
        self.Socket_init()
        while True:
            pub.subscribe(self.Send_message, 'SEND')
        pass

    def Socket_init(self):
        dest_addr = (self.parent.des_ip, self.parent.des_port)

        self.socket = socket()
        while True:
            try:
                self.socket.connect(dest_addr)
                print 'succed'
                break
            except error:
                time.sleep(1)

    def Send_message(self,message):
        self.socket.sendall(message)

    pass

class Listener(object):
    def __init__(self, parent, frame):
        self.parent = parent
        self.frame = frame
        self.Socket_init()
        self.count = 0
        while True:
            self.conn,addr = self.socket.accept()
            self.Recv()
        pass

    def Socket_init(self):
        listen_addr = ('' ,self.parent.local_port)

        self.socket = socket()
        try:
            self.socket.bind(listen_addr)
        except socket.error:
            self.socket.close()
        self.socket.listen(10)

    def Recv(self):
        self.new_mess = self.conn.recv(1024)
        pub.sendMessage('RECEIVE',message = self.new_mess)
        self.conn.close()
    pass

class App(object):
    def __init__(self,des_ip,local_port,des_port):
        self.message = []
        self.new_message = ''
        self.count = 0

        self.des_ip = des_ip
        self.local_port = local_port
        self.des_port = des_port

        self.app = wx.App()
        self.mainFrame = Main.MainFrame(self)
        self.mainFrame.Show()

        self.Thread_init()

        self.app.MainLoop()  


    def Thread_init(self):
        sender = Thread(target=Sender,args=(self,))
        listener = Thread(target=Listener,args=(self, self.mainFrame))
        sender.start()
        listener.start()


def main():
    app = App('127.0.0.1',int(sys.argv[1]),int(sys.argv[2]))


if __name__ == '__main__':
    main()