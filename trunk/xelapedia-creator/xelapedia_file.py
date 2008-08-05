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
import sys
if sys.version_info[:2] > (2,4):
   from sqlite3 import dbapi2 as sqlite
else:
   from pysqlite2 import dbapi2 as sqlite

class Config:
  def __init__(self, mainPage='Main Page', imageTag=None, categoryTag=None):
    self.mainPage = mainPage
    self.imageTag = imageTag
    self.categoryTag = categoryTag

class XelapediaFile:
  def __init__(self, filename):
    self._con = sqlite.connect(filename)
    self._cur = self._con.cursor()
    self._config = self._readConfiguration()

  def _readConfiguration(self):
    result=self._cur.execute('SELECT main_page, image_tag, category_tag, type '
      'FROM config WHERE id=0').fetchone()

    return Config(result[0], result[1], result[2])

  def findTitlesFrom(self, startsWith, count=10):
    return self._cur.execute('SELECT article_id, title FROM titles WHERE title>=?'
      'ORDER BY title ASC', (startsWith,)).fetchmany(count)

  def findTitlesBefore(self, title, count=10):
    return self._cur.execute('SELECT article_id, title FROM titles WHERE title<?'
      'ORDER BY title DESC', (title,)).fetchmany(count)

  def readArticle(self, id):
    return self._cur.execute('SELECT contents '
      'FROM articles WHERE id=?', (id,)).fetchone()[0]

  def mainPage(self):
    return self._config.mainPage

