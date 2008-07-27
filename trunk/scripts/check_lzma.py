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

'''check the integrity of a lzma compressed xelapedia file'''

from pylzma import decompress
from sqlite3 import dbapi2
import sys

def checkCompression(file):
  con=dbapi2.connect(file)
  con.text_factory=str

  cur=con.execute('SELECT id, contents FROM articles')
  for id, contents in cur:
    #print contents
    dummy=decompress(contents)
    print dummy

if __name__=='__main__':
  checkCompression(sys.argv[1])
