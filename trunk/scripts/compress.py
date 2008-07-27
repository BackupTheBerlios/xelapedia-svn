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

''' create a lzma compressed xelapedia file from an uncompressed file'''

import sys
if sys.version_info[:2] > (2,4):
  from sqlite3 import dbapi2 as sqlite
  from sqlite3 import Binary
else:
  from pysqlite2 import dbapi2 as sqlite
  from pysqlite2 import Binary
import re
from create import createXelapedia
from pylzma import compress
from array import array
from sys import stdout

def compressFunction(uncompressed):
  '''This function takes the @param uncompressed an uses LZMA to
  compress it'''

  stdout.write('.')
  try:
    print type(uncompressed)
    #compressed=compress(array('B', uncompressed))
    print uncompressed[0:5]

    return 'foo' #compress(uncompressed)
  except:
    print "Unexpected error:", sys.exc_info()
    raise



def compressXelapedia(source, dest):
  createXelapedia(dest)

  # connect with the database with the compressed articles
  con = sqlite.connect(dest)
  con.text_factory=str

  # connect the database with the uncompressed articles
  con.execute('ATTACH ? AS source', (source,))

  # update the configuration
  con.execute('UPDATE config SET type=\'lzma\' WHERE id=0')

  # copy the titles
  con.execute('INSERT INTO titles(title, article_id) ' +
    'SELECT title, article_id FROM source.titles')
  con.commit()

  # we dont need the table attached directly anymore
  con.execute('DETACH source')
  conSource = sqlite.connect(source)
  conSource.text_factory=str

  # now copy and compress the articles

  #con.create_function('compress', 1, compressFunction)
  #con.execute('INSERT INTO articles(id, contents) ' +
  #  'SELECT id, compress(contents) FROM source.articles ORDER BY id')
  cur=conSource.execute('SELECT id, contents FROM articles ORDER BY id')
  for id, uncompressed in cur:
    compressed = Binary(compress(uncompressed))
    con.execute('INSERT INTO articles(id, contents) VALUES(?,?)',
      (id, compressed,))

    stdout.write('.')
    stdout.flush()
    con.commit()


USAGE='''compress.py <file1> <file2>
  <file1> path to uncompressed xelapedia
  <file2> path to compressed xelapedia'''

if __name__=='__main__':
  if len(sys.argv) != 3:
    print USAGE
    sys.exit(1)

  try:
    compressXelapedia(sys.argv[1], sys.argv[2])

  except KeyboardInterrupt:
    print 'Interrupted!'
  except:
    raise
