# !/usr/bin/python
# -*- coding: UTF-8 -*-

import thread
import os
import time
import sys
import curses
import wx
from wx.lib.pubsub import pub
from socket import *
from threading import Thread

class Sender(object):
    def __init__(self, parent):
        self.parent = parent
        self.dest_addr = (self.parent.des_ip, self.parent.des_port)
        self.socket = socket()
        pub.subscribe(self.Send_message, 'SEND')
        time.sleep(86400)

    def Send_message(self, message):
        self.socket = socket()
        while True:
            try:
                self.socket.connect(self.dest_addr)
                print 'succed'
                break
            except error,e:
                print e
                time.sleep(1)
        self.socket.sendall(message)
        self.socket.close()

class Listener(object):
    def __init__(self, parent):
        self.parent = parent
        self.Socket_init()
        self.count = 0
        while True:
            self.conn,addr = self.socket.accept()
            self.Recv()

    def Socket_init(self):
        listen_addr = ('' ,self.parent.local_port)

        self.socket = socket()
        try:
            self.socket.bind(listen_addr)
        except:
            self.socket.close()
        self.socket.listen(10)

    def Recv(self):
        self.new_mess = self.conn.recv(1024)
        wx.CallAfter(pub.sendMessage,'RECEIVE',message = self.new_mess)
        # pub.sendMessage('RECEIVE',message = self.new_mess)
        self.conn.close()

class App(object):
    def __init__(self,des_ip = '127.0.0.1',local_port = 22000, des_port = 22000):
        self.message = []
        self.new_message = ''
        self.count = 0

        self.des_ip = des_ip
        self.local_port = local_port
        self.des_port = des_port

        self.Thread_init()

    def Thread_init(self):
        sender = Thread(target=Sender,args=(self,))
        listener = Thread(target=Listener,args=(self,))
        sender.start()
        listener.start()