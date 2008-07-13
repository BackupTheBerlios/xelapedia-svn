#
# Copyright (C) 2008 Alexander Mueller
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
from generated import *
from about_dlg import AboutDialog

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
