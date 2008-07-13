#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Sun Jul 13 12:51:58 2008

import wx

# begin wxGlade: extracode
from wx.html import HtmlWindow
from wx.html import HtmlWindow
# end wxGlade



class MainFrameBase(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainFrameBase.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.splitterWindow = wx.SplitterWindow(self, -1, style=wx.SP_3D|wx.SP_BORDER)
        self.mainNotebook = wx.Notebook(self.splitterWindow, -1, style=wx.NB_BOTTOM)
        self.notebookSourcePanel = wx.Panel(self.mainNotebook, -1)
        self.notebookPreviewPanel = wx.Panel(self.mainNotebook, -1)
        self.leftPanel = wx.Panel(self.splitterWindow, -1)
        self.searchCtrl = wx.TextCtrl(self.leftPanel, -1, "")
        self.titleList = wx.ListBox(self.leftPanel, -1, choices=[])
        self.previewCtrl = HtmlWindow(self.notebookPreviewPanel, -1)
        self.sourceCtrl = wx.TextCtrl(self.notebookSourcePanel, -1, "", style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH2)
        
        # Menu Bar
        self.menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        self.menuOpen = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), _("&Open..."), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.menuOpen)
        wxglade_tmp_menu.AppendSeparator()
        self.menuQuit = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), _("Quit"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.menuQuit)
        self.menubar.Append(wxglade_tmp_menu, _("&File"))
        wxglade_tmp_menu = wx.Menu()
        self.menuCopy = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), _("&Copy"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.menuCopy)
        wxglade_tmp_menu.AppendSeparator()
        self.menuFind = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), _("&Find..."), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.menuFind)
        self.menubar.Append(wxglade_tmp_menu, _("&Edit"))
        wxglade_tmp_menu = wx.Menu()
        self.menuAbout = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), _("&About..."), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.menuAbout)
        self.menubar.Append(wxglade_tmp_menu, _("&Help"))
        self.SetMenuBar(self.menubar)
        # Menu Bar end

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.menuOpenHandler, self.menuOpen)
        self.Bind(wx.EVT_MENU, self.menuQuitHandler, self.menuQuit)
        self.Bind(wx.EVT_MENU, self.menuCopyHandler, self.menuCopy)
        self.Bind(wx.EVT_MENU, self.menuFindHandler, self.menuFind)
        self.Bind(wx.EVT_MENU, self.menuAboutHandler, self.menuAbout)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MainFrameBase.__set_properties
        self.SetTitle(_("Xelapedia Creator"))
        self.SetSize((600, 400))
        self.searchCtrl.SetMinSize((200, 27))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainFrameBase.__do_layout
        topSizer = wx.BoxSizer(wx.VERTICAL)
        notebookSourceSizer = wx.BoxSizer(wx.VERTICAL)
        notebookPreviewSizer = wx.BoxSizer(wx.VERTICAL)
        leftSizer = wx.BoxSizer(wx.VERTICAL)
        leftSizer.Add(self.searchCtrl, 0, wx.EXPAND, 0)
        leftSizer.Add(self.titleList, 1, wx.EXPAND, 0)
        self.leftPanel.SetSizer(leftSizer)
        notebookPreviewSizer.Add(self.previewCtrl, 1, wx.EXPAND, 0)
        self.notebookPreviewPanel.SetSizer(notebookPreviewSizer)
        notebookSourceSizer.Add(self.sourceCtrl, 1, wx.EXPAND, 0)
        self.notebookSourcePanel.SetSizer(notebookSourceSizer)
        self.mainNotebook.AddPage(self.notebookPreviewPanel, _("Preview"))
        self.mainNotebook.AddPage(self.notebookSourcePanel, _("Source"))
        self.splitterWindow.SplitVertically(self.leftPanel, self.mainNotebook, 100)
        topSizer.Add(self.splitterWindow, 1, wx.EXPAND, 0)
        self.SetSizer(topSizer)
        self.Layout()
        # end wxGlade

    def menuOpenHandler(self, event): # wxGlade: MainFrameBase.<event_handler>
        print "Event handler `menuOpenHandler' not implemented!"
        event.Skip()

    def menuQuitHandler(self, event): # wxGlade: MainFrameBase.<event_handler>
        print "Event handler `menuQuitHandler' not implemented!"
        event.Skip()

    def menuCopyHandler(self, event): # wxGlade: MainFrameBase.<event_handler>
        print "Event handler `menuCopyHandler' not implemented!"
        event.Skip()

    def menuFindHandler(self, event): # wxGlade: MainFrameBase.<event_handler>
        print "Event handler `menuFindHandler' not implemented!"
        event.Skip()

    def menuAboutHandler(self, event): # wxGlade: MainFrameBase.<event_handler>
        print "Event handler `menuAboutHandler' not implemented!"
        event.Skip()

# end of class MainFrameBase


class AboutDialogBase(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: AboutDialogBase.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.notebook = wx.Notebook(self, -1, style=0)
        self.panelLicense = wx.Panel(self.notebook, -1)
        self.panelAbout = wx.Panel(self.notebook, -1)
        self.bitmapLogo = wx.StaticBitmap(self, -1, wx.Bitmap("logo.png", wx.BITMAP_TYPE_ANY), style=wx.SUNKEN_BORDER)
        self.textAbout = wx.TextCtrl(self.panelAbout, -1, _("About Xelapedia Creator"), style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH2)
        self.textLicense = wx.TextCtrl(self.panelLicense, -1, _("GPLv3"), style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH2)
        self.buttonOK_copy = wx.Button(self, -1, _("&OK"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.buttonOKHandler, self.buttonOK_copy)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: AboutDialogBase.__set_properties
        self.SetTitle(_("About Xelapedia Creator"))
        self.SetSize((400, 300))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: AboutDialogBase.__do_layout
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        topSizer = wx.BoxSizer(wx.HORIZONTAL)
        sizerLicense = wx.BoxSizer(wx.VERTICAL)
        sizerAbout = wx.BoxSizer(wx.VERTICAL)
        topSizer.Add(self.bitmapLogo, 0, 0, 0)
        sizerAbout.Add(self.textAbout, 1, wx.EXPAND, 0)
        self.panelAbout.SetSizer(sizerAbout)
        sizerLicense.Add(self.textLicense, 1, wx.EXPAND, 0)
        self.panelLicense.SetSizer(sizerLicense)
        self.notebook.AddPage(self.panelAbout, _("About"))
        self.notebook.AddPage(self.panelLicense, _("License"))
        topSizer.Add(self.notebook, 1, wx.EXPAND, 0)
        mainSizer.Add(topSizer, 1, wx.EXPAND, 0)
        mainSizer.Add(self.buttonOK_copy, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.SetSizer(mainSizer)
        self.Layout()
        # end wxGlade

    def buttonOKHandler(self, event): # wxGlade: AboutDialogBase.<event_handler>
        print "Event handler `buttonOKHandler' not implemented!"
        event.Skip()

# end of class AboutDialogBase


class XelapediaCreatorAppBase(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        mainFrameBase = MainFrameBase(None, -1, "")
        self.SetTopWindow(mainFrameBase)
        mainFrameBase.Show()
        return 1

# end of class XelapediaCreatorAppBase

if __name__ == "__main__":
    import gettext
    gettext.install("app") # replace with the appropriate catalog name

    app = XelapediaCreatorAppBase(0)
    app.MainLoop()