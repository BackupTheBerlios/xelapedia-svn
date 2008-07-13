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
import re

class Converter:
  _lines=[]
  _title=None

  def __init__(self, title, contents):
    self._lines = contents.splitlines()
    self._title = title

  def replaceBold(self):
    i=0
    for line in self._lines:
      changed=False
      opening = True

      oldpos = 0
      pos = line.find("'''")
      newline=''
      while pos >= 0:
        changed=True
        if opening:
          newline+=line[oldpos:pos] + '<b>'
        else:
          newline+=line[oldpos:pos] + '</b>'

        oldpos=pos+3
        pos=line.find("'''", oldpos)
        opening=not opening

      if changed:
        self._lines[i] = newline

      i += 1


  def toHtml(self):
    self.replaceBold()

    html='\n'.join(self._lines)

    start = "<HTML><HEAD><TITLE>%s</TITLE></HEAD><BODY><H1>%s</H1>" % \
      (self._title, self._title)

    return start + html + '</BODY></HTML>'

if __name__=='__main__':
  conv=Converter('title',"This is a '''text''', and '''another one'''")
  print conv.toHtml().encode('utf-8')
