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
    
  def replaceBold(self, what, opentag, closetag):
    i=0
    for line in self._lines:
      changed=False
      opening = True

      pos = line.find(what)
      newline=''
      while pos >= 0:
        changed=True
        if opening:
          newline+=line[:pos] + opentag
        else:
          newline+=line[:pos] + closetag

        line=line[pos+len(what):]
        pos=line.find(what)
        opening=not opening

      newline += line

      if changed:
        self._lines[i] = newline

      i += 1

  def replaceLinks(self):
    i=0
    for line in self._lines:
      changed=False
      newline=''

      pos1=line.find('[[')
      while pos1 >= 0:
        pos2=line.find(']]',pos1+2)

        if pos2 < 0:
          break

        changed=True
        link=line[pos1+2:pos2].partition('|')
        url=link[0]
        text=link[2]
        if len(text) == 0:
          text=url

        newline+=line[:pos1] + "<a href=\"%s\">%s</a>" % (url, text)
        line=line[pos2+2:]

        pos1=line.find('[[')

      newline+=line
      if changed:
        self._lines[i] = newline

      i += 1
  
  def replaceHeadings(self):
    i = 0
    for line in self._lines:
      hlevel=4
      while hlevel >= 2:
        what='='*hlevel
        if line.startswith(what):
          endpos=line.find(what, len(what))
          if endpos>=0:
            self._lines[i]="<h%d>%s</h%d>" % (hlevel,line[len(what):endpos].strip(),hlevel)
            break
        hlevel -= 1
      i += 1

  def toHtml(self):
    self.replaceBold("'''''", '<b><i>', '</i></b>')
    self.replaceBold("'''", '<b>', '</b>')
    self.replaceBold("''", '<i>', '</i>')
    self.replaceLinks()
    self.replaceHeadings()

    html='\n'.join(self._lines)

    start = "<html><head><title>%s</title></head><body><h1>%s</h1>" % \
      (self._title, self._title)

    return start + html + '</body></html>'

if __name__=='__main__':
  conv=Converter('title',"This is a '''text''', and '''another one'''")
  print conv.toHtml().encode('utf-8')
  conv=Converter('title',"""Link1: [[Einfacher Link]] und so
  aber nun [[Link|mit alternativem Text]]""")
  print conv.toHtml().encode('utf-8')

  conv=Converter('title',
    """'''Majuskel''' (vvun [[Latein|lat.]]: ''majusculus'' = a bisl groesser)""")
  print conv.toHtml().encode('utf-8')
