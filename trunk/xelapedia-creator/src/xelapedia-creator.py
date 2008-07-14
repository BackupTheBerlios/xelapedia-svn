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
import wx
from main_frame import MainFrame

class App(wx.App):
  def OnInit(self):
    wx.InitAllImageHandlers()
    mainFrame = MainFrame(None, "")
    self.SetTopWindow(mainFrame)
    mainFrame.Maximize(True)
    mainFrame.Show()
    return 1


if __name__=='__main__':
  import gettext
  gettext.install("xelapedia-creator") # replace with the appropriate catalog name

  app = App(0)
  app.MainLoop()
