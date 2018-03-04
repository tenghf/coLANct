#!/usr/bin/env python
# -*- coding: utf-8 -*-

###########################################################################
## 
## Python code PARTLY generated with wxFormBuilder (version Feb 16 2016)
## http://www.wxformbuilder.org/
##
###########################################################################


import wx
import wx.xrc
from common import *
import thread
from wx.lib.expando import ExpandoTextCtrl

def info(info):
    print '@@@@@@ frontend:' + info + ' @@@@@@'


##################################
# Class wxtl
##################################
class wxtl(object):
    '''
    该类提供wx下的一些实用的小功能
    '''
    @staticmethod
    def GetTextDisplayLen(str):

        print 'messure length'
        print str
        print type(str)

        frame = wx.Frame(None)
        panel = wx.Panel(frame)
        panel_sizer = wx.BoxSizer()
        panel.SetSizer(panel_sizer)
        text = wx.StaticText(panel, wx.ID_ANY, label=str)
        panel_sizer.Add(text, 1, wx.EXPAND)
        text_width, text_height = panel.GetBestSize()
        frame.Destroy()
        return text_width

###########################################################################
## Class messagePanel
###########################################################################

class messagePanel(wx.Panel):

    def __init__(self, parent, messageData, nickname = u'王小明'):

        #计算合适的宽度
        border_width = 18
        parent_width,parent_height = parent.GetSize()
        max_width = parent_width * 0.5
        min_width = wxtl.GetTextDisplayLen(nickname) + border_width

        '''
        panel = wx.Panel(parent)
        panel_sizer = wx.BoxSizer()
        panel.SetSizer(panel_sizer)
        text = wx.StaticText(panel, wx.ID_ANY, label = messageData)
        panel_sizer.Add(text, 1, wx.EXPAND)
        text_width, text_height =  panel.GetBestSize()
        panel.Destroy()
        '''

        text_width = wxtl.GetTextDisplayLen(messageData)


        if text_width > max_width:
            width = max_width
        elif text_width < min_width:
            width = min_width
        else:
            width = text_width + border_width

        print text_width
        print min_width
        print width

        #开始初始化用于显示消息的panel
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition , size = (width , -1),
                          style=wx.TAB_TRAVERSAL)

        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))

        message_sizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, nickname ), wx.VERTICAL )

        self.m_textCtrl7 = ExpandoTextCtrl(self, wx.ID_ANY, value=messageData, style = wx.TE_MULTILINE | wx.NO_BORDER | wx.TE_READONLY )
        self.m_textCtrl7.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.m_textCtrl7.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        #self.m_textCtrl7.Enable(False)

        message_sizer.Add(self.m_textCtrl7, 1, wx.ALL | wx.EXPAND, 7)

        self.SetSizer(message_sizer)
        self.Sizer.Fit(self)

        self.Layout()




    def __del__(self):
        pass



###########################################################################
## Class SettingDialog
###########################################################################

class SettingDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Setting", pos=wx.DefaultPosition, size=wx.Size(395, 252),
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.Size(-1, -1), wx.Size(-1, -1))

        SettingDialog_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"设置"), wx.VERTICAL)

        self.SettingItemPanel = wx.Panel(SettingDialog_sizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition,
                                         wx.DefaultSize, wx.TAB_TRAVERSAL)
        SettingItemPanel = wx.FlexGridSizer(4, 2, 0, 0)
        SettingItemPanel.SetFlexibleDirection(wx.BOTH)
        SettingItemPanel.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Port_label = wx.StaticText(self.SettingItemPanel, wx.ID_ANY, u"端口号", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Port_label.Wrap(-1)
        SettingItemPanel.Add(self.Port_label, 0, wx.ALL, 5)

        self.Port_input = wx.TextCtrl(self.SettingItemPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        SettingItemPanel.Add(self.Port_input, 0, wx.ALL, 5)

        self.Nickname_label = wx.StaticText(self.SettingItemPanel, wx.ID_ANY, u"昵称", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.Nickname_label.Wrap(-1)
        SettingItemPanel.Add(self.Nickname_label, 0, wx.ALL, 5)

        self.Nickname_input = wx.TextCtrl(self.SettingItemPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.Size(150, -1), 0)
        SettingItemPanel.Add(self.Nickname_input, 0, wx.ALL, 5)

        self.IP_label = wx.StaticText(self.SettingItemPanel, wx.ID_ANY, u"目标IP", wx.DefaultPosition, wx.DefaultSize, 0)
        self.IP_label.Wrap(-1)
        SettingItemPanel.Add(self.IP_label, 0, wx.ALL, 5)

        self.IP_input = wx.TextCtrl(self.SettingItemPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.Size(250, -1), 0)
        SettingItemPanel.Add(self.IP_input, 1, wx.ALL, 5)

        self.FilePath_label = wx.StaticText(self.SettingItemPanel, wx.ID_ANY, u"文件保存地址", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.FilePath_label.Wrap(-1)
        SettingItemPanel.Add(self.FilePath_label, 0, wx.ALL, 5)

        self.FilePath_input = wx.TextCtrl(self.SettingItemPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.Size(250, -1), 0)
        SettingItemPanel.Add(self.FilePath_input, 0, wx.ALL, 5)

        self.SettingItemPanel.SetSizer(SettingItemPanel)
        self.SettingItemPanel.Layout()
        SettingItemPanel.Fit(self.SettingItemPanel)
        SettingDialog_sizer.Add(self.SettingItemPanel, 1, wx.EXPAND | wx.ALL, 5)

        self.ButtonPanel = wx.Panel(SettingDialog_sizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                    wx.TAB_TRAVERSAL)
        ButtonPanel_sizer = wx.GridSizer(0, 2, 0, 0)

        self.confirm = wx.Button(self.ButtonPanel, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0)
        ButtonPanel_sizer.Add(self.confirm, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.drop = wx.Button(self.ButtonPanel, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0)
        ButtonPanel_sizer.Add(self.drop, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        self.ButtonPanel.SetSizer(ButtonPanel_sizer)
        self.ButtonPanel.Layout()
        ButtonPanel_sizer.Fit(self.ButtonPanel)
        SettingDialog_sizer.Add(self.ButtonPanel, 0, wx.EXPAND, 0)

        self.SetSizer(SettingDialog_sizer)
        self.Layout()

        self.Centre(wx.BOTH)


        #########################
        # Connect Events
        #########################

        self.confirm.Bind(wx.EVT_BUTTON, self.onConfirm)
        self.drop.Bind(wx.EVT_BUTTON, self.onDrop)


        ##############################
        #loading setting from backend
        ##############################

        self.parent = parent
        messager = parent.messager
        messager.f2b_signal.put('read_setting')
        setting = messager.b2f_signal.get()
        ip = setting['address'][0]
        port = setting['address'][1]
        filePath = setting['file_path']
        nickname = self.parent.nickname
        self.IP_input.SetValue(ip)
        self.Port_input.SetValue(str(port))
        self.FilePath_input.SetValue(filePath)
        self.Nickname_input.SetValue(nickname)
    
    def __del__(self):
            pass

    # Virtual event handlers, overide them in your derived class
    def onConfirm(self, event):
        messager = self.parent.messager
        ip = self.IP_input.GetValue()
        nickname = self.Nickname_input.GetValue()
        port = int(self.Port_input.GetValue())
        filePath = self.FilePath_input.GetValue()

        self.parent.nickname =nickname

        newSetting = {
            'address' : (ip, port),
            'file_path' : filePath
        }
        messager.f2b_signal.put('save_setting')
        messager.f2b_buff.put(newSetting)
        result = messager.b2f_signal.get()
        if result != 'ok':
            wx.MessageDialog(self, result, u'提示', style = wx.OK).ShowModal()
        else:
            self.Close()


    def onDrop(self, event):
        self.Close()


###########################################################################
## Class MainFrame
###########################################################################

class MainFrame(wx.Frame):

    def __init__(self, parent, messager):

        ###################
        #intial UI
        ###################

        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"CoLANct", pos=wx.DefaultPosition, size=wx.Size(877, 641),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.Size(500, 511), wx.DefaultSize)

        MainFrame_sizer = wx.BoxSizer(wx.VERTICAL)

        self.ToolBarPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        ToolBarPanel_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.connect = wx.Button(self.ToolBarPanel, wx.ID_ANY, u"连接", wx.DefaultPosition, wx.DefaultSize, 0)
        ToolBarPanel_sizer.Add(self.connect, 0, wx.LEFT | wx.RIGHT, 3)

        self.disconnect = wx.Button(self.ToolBarPanel, wx.ID_ANY, u"断开", wx.DefaultPosition, wx.DefaultSize, 0)
        ToolBarPanel_sizer.Add(self.disconnect, 0, wx.LEFT | wx.RIGHT, 3)

        self.setting = wx.Button(self.ToolBarPanel, wx.ID_ANY, u"设置", wx.DefaultPosition, wx.DefaultSize, 0)
        ToolBarPanel_sizer.Add(self.setting, 0, wx.LEFT | wx.RIGHT, 3)

        self.stopListen = wx.Button(self.ToolBarPanel, wx.ID_ANY, u"停止监听", wx.DefaultPosition, wx.DefaultSize, 0)
        ToolBarPanel_sizer.Add(self.stopListen, 0, wx.LEFT | wx.RIGHT, 3)

        self.startListen = wx.Button(self.ToolBarPanel, wx.ID_ANY, u"启动监听", wx.DefaultPosition, wx.DefaultSize, 0)
        ToolBarPanel_sizer.Add(self.startListen, 0, wx.LEFT | wx.RIGHT, 3)

        self.ToolBarPanel.SetSizer(ToolBarPanel_sizer)
        self.ToolBarPanel.Layout()
        ToolBarPanel_sizer.Fit(self.ToolBarPanel)
        MainFrame_sizer.Add(self.ToolBarPanel, 0, wx.EXPAND, 0)

        self.RecordPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        Record_sizer = wx.StaticBoxSizer(wx.StaticBox(self.RecordPanel, wx.ID_ANY, u"聊天记录"), wx.VERTICAL)

        self.RecordView = wx.ScrolledWindow(Record_sizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.HSCROLL | wx.VSCROLL)
        self.RecordView.SetScrollRate(0, 5)
        self.RecordView.SetBackgroundColour(wx.Colour(255, 255, 255))

        RecordView_sizer = wx.BoxSizer(wx.VERTICAL)

        self.RecordView.SetSizer(RecordView_sizer)
        self.RecordView.Layout()
        RecordView_sizer.Fit(self.RecordView)
        Record_sizer.Add(self.RecordView, 1, wx.EXPAND | wx.ALL, 5)

        self.RecordPanel.SetSizer(Record_sizer)
        self.RecordPanel.Layout()
        Record_sizer.Fit(self.RecordPanel)
        MainFrame_sizer.Add(self.RecordPanel, 2, wx.EXPAND, 0)

        self.InputPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        InputPanel_sizer = wx.StaticBoxSizer(wx.StaticBox(self.InputPanel, wx.ID_ANY, u"输入"), wx.VERTICAL)

        self.FilePanel = wx.Panel(InputPanel_sizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                  wx.TAB_TRAVERSAL)
        FilePanel_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.File_label = wx.StaticText(self.FilePanel, wx.ID_ANY, u"添加附件", wx.DefaultPosition, wx.DefaultSize, 0)
        self.File_label.Wrap(-1)
        FilePanel_sizer.Add(self.File_label, 0, wx.LEFT, 5)

        self.File_picker = wx.FilePickerCtrl(self.FilePanel, wx.ID_ANY,
                                             wx.EmptyString, u"Select a file",
                                             u"*.*", wx.DefaultPosition, wx.DefaultSize,
                                             wx.FLP_DEFAULT_STYLE | wx.FLP_USE_TEXTCTRL)
        FilePanel_sizer.Add(self.File_picker, 1)

        self.sendFile = wx.Button(self.FilePanel, wx.ID_ANY, u"Send", wx.DefaultPosition, wx.DefaultSize, 0)
        FilePanel_sizer.Add(self.sendFile, 0, wx.LEFT | wx.RIGHT, 5)

        self.FilePanel.SetSizer(FilePanel_sizer)
        self.FilePanel.Layout()
        FilePanel_sizer.Fit(self.FilePanel)
        InputPanel_sizer.Add(self.FilePanel, 0, wx.EXPAND, 5)


        self.InputArea = wx.TextCtrl(InputPanel_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.DefaultSize, wx.TE_MULTILINE)
        self.textInputEnable = True
        InputPanel_sizer.Add(self.InputArea, 1, wx.ALL | wx.EXPAND, 5)


        self.InputPanel.SetSizer(InputPanel_sizer)
        self.InputPanel.Layout()
        InputPanel_sizer.Fit(self.InputPanel)
        MainFrame_sizer.Add(self.InputPanel, 1, wx.EXPAND, 0)

        self.BottomToolBarPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        BottomToolBarPanel_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.send = wx.Button(self.BottomToolBarPanel, wx.ID_ANY, u"发送", wx.DefaultPosition, wx.DefaultSize, 0)
        BottomToolBarPanel_sizer.Add(self.send, 0, wx.ALL, 3)

        self.clear = wx.Button(self.BottomToolBarPanel, wx.ID_ANY, u"清空", wx.DefaultPosition, wx.DefaultSize, 0)
        BottomToolBarPanel_sizer.Add(self.clear, 0, wx.ALL, 3)

        self.BottomToolBarPanel.SetSizer(BottomToolBarPanel_sizer)
        self.BottomToolBarPanel.Layout()
        BottomToolBarPanel_sizer.Fit(self.BottomToolBarPanel)
        MainFrame_sizer.Add(self.BottomToolBarPanel, 0, wx.EXPAND, 0)

        self.SetSizer(MainFrame_sizer)
        self.Layout()

        self.Centre(wx.BOTH)

        ########################
        # Load front atrributes
        ########################

        self.nickname = u'王小明'


        ######################
        # shortcut
        ######################
        accel_tbl = wx.AcceleratorTable([(wx.ACCEL_CTRL, ord('\r'), self.send.GetId())])
        self.SetAcceleratorTable(accel_tbl)


        ######################
        # Connect Events
        ######################
        self.setting.Bind(wx.EVT_BUTTON, self.onSetting)
        self.Bind(wx.EVT_BUTTON, self.onSendMessage, self.send)
        self.connect.Bind(wx.EVT_BUTTON, self.onConnect)
        self.disconnect.Bind(wx.EVT_BUTTON, self.onDisconnect)
        self.clear.Bind(wx.EVT_BUTTON, self.onClearInput)
        self.sendFile.Bind(wx.EVT_BUTTON, self.onSendFile)
        self.Bind( wx.EVT_CLOSE, self.onClose )
        self.stopListen.Bind(wx.EVT_BUTTON, self.onStopListen)
        self.startListen.Bind(wx.EVT_BUTTON, self.onStartListen)



        ########################
        # communication part
        ########################

        self.messager = messager
        thread.start_new_thread(self.ReceiveMessageHandler, empty_tuple)
        thread.start_new_thread(self.ReceiveNotice, empty_tuple)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def onConnect(self, event):
        self.messager.f2b_signal.put('connect')
        result = self.messager.b2f_signal.get()
        if result == 'ok':
            wx.MessageDialog(self, u'连接已建立', u'提示', style = wx.OK).ShowModal()
        else:
            wx.MessageDialog(self, result, u'提示', style = wx.OK).ShowModal()

    def onDisconnect(self, event):
        self.messager.f2b_signal.put('disconnect')
        result = self.messager.b2f_signal.get()
        if result == 'ok':
            wx.MessageDialog(self, u'连接已断开', u'提示', style = wx.OK).ShowModal()
        else:
            wx.MessageDialog(self, result, u'提示', style = wx.OK).ShowModal()

    def onSetting(self, event):
        d = SettingDialog(self).ShowModal()

    def onClearInput(self, event):
        self.InputArea.SetValue('')


    def ReceiveMessageHandler(self):
        while True:
            messageByte = self.messager.b2f_buff.get()
            messageData = messageByte.decode(encoding='utf-8')

            info('receive ' + messageData)

            thread.start_new_thread(self.UpdateUI,(self.DisplayMessage,messageData, wx.ALIGN_LEFT))
    def ReceiveNotice(self):
        while True:
            notice = self.messager.b2f_notice.get()
            thread.start_new_thread(self.UpdateUI,(wx.MessageBox, notice , u'提示', wx.ICON_EXCLAMATION))


    def onSendMessage(self,event):

        messageData = self.InputArea.GetValue()
        if messageData != '':
            self.messager.f2b_signal.put('send')
            self.messager.f2b_buff.put(messageData.encode(encoding = 'utf-8'))
            result = self.messager.b2f_signal.get()
            if result != 'ok':
                wx.MessageDialog(self, result, u'提示', style = wx.OK).ShowModal()
                return

            self.DisplayMessage(messageData, wx.ALIGN_RIGHT)
            self.InputArea.SetValue('')
        else:
            wx.MessageBox(u'没有待发送的消息', u'提示')

    def onSendFile(self, event):
        sendFilePath = self.File_picker.GetPath()

        wx.MessageBox('努力开发中...','提示')

        if sendFilePath != '':
            self.messager.f2b_signal.put('send')
            self.messager.f2b_buff.put(sendFilePath.encode(encoding = 'utf-8'))
            result = self.messager.b2f_signal.get()
            if result != 'ok':
                wx.MessageDialog(self, result, u'提示', style = wx.OK).ShowModal()
                return

            filename = sendFilePath.split(r'/')[-1]
            self.DisplayMessage(u'文件:' + filename , wx.ALIGN_RIGHT)
        else:
            wx.MessageBox(u'没有选择文件', u'提示')

    def onClose(self, event):
        self.messager.f2b_signal.put('exit')
        result = self.messager.b2f_signal.get()

        exit()

    def onStopListen(self, event):
        self.messager.f2b_signal.put('stop_listen')
        result = self.messager.b2f_signal.get()
        if result == 'ok':
            wx.MessageDialog(self, u'监听已停止', u'提示', style = wx.OK).ShowModal()
        else:
            wx.MessageDialog(self, result, u'提示', style = wx.OK).ShowModal()

    def onStartListen(self, event):
        self.messager.f2b_signal.put('start_listen')
        result = self.messager.b2f_signal.get()
        if result == 'ok':
            wx.MessageDialog(self, u'监听已启动', u'提示', style=wx.OK).ShowModal()
        else:
            wx.MessageDialog(self, result, u'提示', style=wx.OK).ShowModal()


    #######################
    # common tool methods
    #######################

    def DisplayMessage(self, message, pos = wx.ALIGN_LEFT):
        '''
        :param message: 传入需要显示的消息
        :param pos: 显示在左边或右边
        :return: 显示消息的panel对象
        '''
        sizer = self.RecordView.GetSizer()
        message_panel = messagePanel(self.RecordView, message, nickname=self.nickname)
        sizer.Add(message_panel, 0, pos | wx.ALL, 10)
        self.Layout()

        # 滚动窗口到当前位置
        current_posY = self.RecordView.GetScrollPos(wx.VERTICAL)
        message_panel_posY = message_panel.GetPosition()[1]
        self.RecordView.Scroll(0, (message_panel_posY / 5) + current_posY)
        return message_panel

    def UpdateUI(self, method, *arg):
        wx.CallAfter(method, *arg)

class Frontend(object):
    def __init__(self, messager):
        self.messager = messager
    def start(self):
        app = wx.App()
        mainFrame = MainFrame(None, self.messager)
        mainFrame.Show()
        app.MainLoop()
