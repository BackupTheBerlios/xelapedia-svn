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
import re
from os.path import exists

SQL='''CREATE TABLE titles(
  title text UNIQUE PRIMARY KEY,
  anchor text,
  article_id integer NOT NULL);
CREATE TABLE redirects(
  title text UNIQUE PRIMARY KEY,
  redirect text);
CREATE TABLE articles(
  id integer UNIQUE PRIMARY KEY,
  contents BLOB);
CREATE TABLE config(
  id integer UNIQUE PRIMARY KEY,
  main_page TEXT,
  image_tag TEXT,
  category_tag TEXT,
  type text);
INSERT INTO config (id, main_page, image_tag, category_tag, type)
VALUES(0, 'Main Page', NULL, NULL, 'empty');'''

class InvalidFilenameException(Exception): pass
class FileExistsException(Exception): pass

def createXelapedia(filename):
  if not filename.endswith('.xelapedia'):
    raise InvalidFilenameException()

  if exists(filename):
    raise FileExistsException()

  con=sqlite.connect(filename)
  cur=con.cursor()

  for statement in SQL.split(';'):
    cur.execute(statement)

  con.commit()


if __name__=='__main__':
  if len(sys.argv) != 2:
    usage()
    sys.exit(1)
  else:
    try:
      createXelapedia(sys.argv[1])
    except InvalidFilenameException:
      print 'Invalid filename!'
      sys.exit(1)
    except FileExistsException:
      print 'File exists already!'
      sys.exit(1)
    except KeyboardInterrupt:
      print "Interrupted!"
      sys.exit(1)
