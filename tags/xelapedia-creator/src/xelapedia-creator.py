from generated import *

class AboutDialog(AboutDialogBase):
  def __init__(self, parent):
    AboutDialogBase.__init__(self, parent, -1)

  def buttonOKHandler(self, evt):
    self.Close()

class MainFrame(MainFrameBase):
  def __init__(self, parent, title):
    MainFrameBase.__init__(self, parent, -1, title)

  def menuQuitHandler(self, evt):
    self.Close()
    evt.Skip()

  def menuAboutHandler(self, evt):
    dlg=AboutDialog(self)
    dlg.ShowModal()

class XelapediaCreatorApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        mainFrameBase = MainFrame(None, "")
        self.SetTopWindow(mainFrameBase)
        mainFrameBase.Show()
        return 1


if __name__=='__main__':
  import gettext
  gettext.install("xelapedia-creator") # replace with the appropriate catalog name

  app = XelapediaCreatorApp(0)
  app.MainLoop()
