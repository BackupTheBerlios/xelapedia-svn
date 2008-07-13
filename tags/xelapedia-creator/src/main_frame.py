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
from generated import MainFrameBase
from about_dlg import AboutDialog
import wx
from xelapedia_file import XelapediaFile

class MainFrame(MainFrameBase):
  _file = None
  _ids = []

  def __init__(self, parent, title):
    MainFrameBase.__init__(self, parent, -1, title)

  def openFile(self, filename):
    self.searchCtrl.SetValue("")
    self.titleList.Clear()
    #self.previewCtrl.SetValue("")
    self.sourceCtrl.SetValue("")

    self._file = XelapediaFile(filename)
    self.searchCtrl.SetValue(unicode(self._file.mainPage()))

  def searchCtrlTextHandler(self, evt):
    if self._file == None:
      return

    titles=self._file.findTitles(self.searchCtrl.GetValue().encode('utf-8'))
    items=[]
    self._ids=[]
    for id, title in titles:
      items.append(unicode(title))
      self._ids.append(id)

    self.titleList.Set(items)

  def titleListHandler(self, evt):
    self.sourceCtrl.SetValue('')
    if evt.IsSelection():
      id=self._ids[evt.GetSelection()]
      contents=unicode(self._file.readArticle(id))
      self.sourceCtrl.SetValue(contents)

  def menuOpenHandler(self, evt):
    dlg = wx.FileDialog(self, message='Choose a Xelapedia file',
      wildcard='*.xelapedia')
    if wx.ID_OK == dlg.ShowModal():
      self.openFile(dlg.GetFilename())

  def menuQuitHandler(self, evt):
    self.Close()
    evt.Skip()

  def menuAboutHandler(self, evt):
    dlg=AboutDialog(self)
    dlg.ShowModal()