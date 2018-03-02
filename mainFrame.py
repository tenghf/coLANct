# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Feb 16 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from wx.lib.pubsub import pub
from wx.lib.expando import ExpandoTextCtrl, EVT_ETC_LAYOUT_NEEDED

###########################################################################
## Class message
###########################################################################

class messagePanel(wx.Panel):

    def __init__(self, parent, messageData):


        parent_width,parent_height = parent.GetSize()


        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition , size = (parent_width * 0.4 , -1),
                          style=wx.TAB_TRAVERSAL)

        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))

        message_sizer = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl7 = ExpandoTextCtrl(self, wx.ID_ANY, value=messageData, style = wx.TE_MULTILINE | wx.NO_BORDER | wx.TE_READONLY )
        self.m_textCtrl7.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.m_textCtrl7.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        #self.m_textCtrl7.Enable(False)

        message_sizer.Add(self.m_textCtrl7, 1, wx.ALL | wx.EXPAND, 7)
        print self.GetBestSize().Get()

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
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Setting", pos=wx.DefaultPosition, size=wx.Size(395, 232),
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.Size(-1, -1), wx.Size(-1, -1))

        SettingDialog_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"设置"), wx.VERTICAL)

        self.SettingItemPanel = wx.Panel(SettingDialog_sizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition,
                                         wx.DefaultSize, wx.TAB_TRAVERSAL)
        SettingItemPanel = wx.FlexGridSizer(4, 2, 0, 0)
        SettingItemPanel.SetFlexibleDirection(wx.BOTH)
        SettingItemPanel.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.SendPort_label = wx.StaticText(self.SettingItemPanel, wx.ID_ANY, u"发送端口号", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.SendPort_label.Wrap(-1)
        SettingItemPanel.Add(self.SendPort_label, 0, wx.ALL, 5)

        self.SendPort_input = wx.TextCtrl(self.SettingItemPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        SettingItemPanel.Add(self.SendPort_input, 0, wx.ALL, 5)

        self.recvPort_label = wx.StaticText(self.SettingItemPanel, wx.ID_ANY, u"接收端口号", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.recvPort_label.Wrap(-1)
        SettingItemPanel.Add(self.recvPort_label, 0, wx.ALL, 5)

        self.recvPort_input = wx.TextCtrl(self.SettingItemPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        SettingItemPanel.Add(self.recvPort_input, 0, wx.ALL, 5)

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

        # Connect Events
        self.confirm.Bind(wx.EVT_BUTTON, self.onConfirm)
        self.drop.Bind(wx.EVT_BUTTON, self.onDrop)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def onConfirm(self, event):
        event.Skip()

    def onDrop(self, event):
        self.Close()


###########################################################################
## Class MainFrame
###########################################################################

class MainFrame(wx.Frame):

    def __init__(self, parent):
        #UI part
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Touch", pos=wx.DefaultPosition, size=wx.Size(877, 641),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        MainFrame_sizer = wx.BoxSizer(wx.VERTICAL)

        self.ToolBarPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        ToolBarPanel_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.connect = wx.Button(self.ToolBarPanel, wx.ID_ANY, u"连接", wx.DefaultPosition, wx.DefaultSize, 0)
        ToolBarPanel_sizer.Add(self.connect, 0, wx.LEFT | wx.RIGHT, 3)

        self.disconnect = wx.Button(self.ToolBarPanel, wx.ID_ANY, u"断开", wx.DefaultPosition, wx.DefaultSize, 0)
        ToolBarPanel_sizer.Add(self.disconnect, 0, wx.LEFT | wx.RIGHT, 3)

        self.setting = wx.Button(self.ToolBarPanel, wx.ID_ANY, u"设置", wx.DefaultPosition, wx.DefaultSize, 0)
        ToolBarPanel_sizer.Add(self.setting, 0, wx.LEFT | wx.RIGHT, 3)

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

        self.InputArea = wx.TextCtrl(InputPanel_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.DefaultSize, wx.TE_MULTILINE)
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

        # Connect Events
        self.setting.Bind(wx.EVT_BUTTON, self.onSetting)
        self.send.Bind(wx.EVT_BUTTON,self.onSendMessage)

        # communication
        pub.subscribe(self.onReceiveMessage,'RECEIVE')

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def onSetting(self, event):
        d = SettingDialog(self).Show()


    def onReceiveMessage(self,message):
        sizer = self.RecordView.GetSizer()
        messageData = message
        sizer.Add(messagePanel(self.RecordView, messageData), 0, wx.ALIGN_LEFT | wx.ALL, 10)
        sizer.Layout()

    def onSendMessage(self,event):
        sizer = self.RecordView.GetSizer()
        messageData = self.InputArea.GetValue()

        pub.sendMessage("SEND",message = messageData)

        self.onReceiveMessage('nice to meet you')
        sizer.Add(messagePanel(self.RecordView, messageData),0,wx.ALIGN_RIGHT|wx.ALL,10)
        self.Layout()




def main():
    app = wx.App()
    mainFrame = MainFrame(None)
    mainFrame.Show()
    app.MainLoop()
    pass


if __name__ == '__main__':
    main()