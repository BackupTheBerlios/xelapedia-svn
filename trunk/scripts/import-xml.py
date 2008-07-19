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
from xml.sax import make_parser, saxutils, ContentHandler
from sys import argv, exit, stderr
import re

class XelapediaImport(ContentHandler):
  def __init__(self, db):
    self.con=sqlite.connect(dbfile)
    self.cur=self.con.cursor()
    self.cur.execute('DELETE FROM articles')
    self.cur.execute('DELETE FROM titles')
    self.cur.execute('DELETE FROM redirects')
    self.con.commit()
    self.inTitle = False
    self.inId = False
    self.inContents = False
    self.id=1

  def checkForRedirect(self):
    REDIRECT='#REDIRECT'

    # is this a redirect page?
    if self.contents[:len(REDIRECT)].upper() != REDIRECT:
      return None
    else:
      # yes, so extract the redirect title
      m=re.match(r'[^[]*\[\[([^]#]+)', self.contents[len(REDIRECT):])
      if m:
        return m.group(1)
      else:
        stderr.write("Warning: Illegal redirect in page %s:\n%s\n"
          % (self.title, self.contents))
        return None

  def findArticleIdForTitle(self, title):
    self.cur.execute('SELECT article_id FROM titles WHERE title=?', (title,))
    return self.cur.fetchone()[0]

  def createArticle(self):
    #stderr.write("Processing article %s\n" % self.title)
    stderr.write('.')
    redirect = self.checkForRedirect()

    if redirect == None:
      # No redirect
      # article...
      self.cur.execute('INSERT INTO articles(id,contents) VALUES(?,?)',
        (self.id, self.contents,))
      # title entry...
      self.cur.execute('INSERT INTO titles(article_id, title) VALUES(?,?)',
        (self.id, self.title,))
      self.con.commit()
      self.id += 1
    else:
      stderr.write("Info: Found redirect to %s\n" % redirect)
      self.cur.execute('INSERT INTO redirects '
        '(title, redirect) VALUES(?,?)',
        (self.title, redirect,))
      self.con.commit()

  def startElement(self, name, attrs):
    #print "<%s>" % name
    if name == 'page':
      self.inTitle = False
      self.inContents = False
      self.title = u''
      self.contents = u''
    elif name == 'title':
      self.inTitle = True
    elif name == 'text':
      self.inContents = True

  def characters(self, ch):
    #print ("'%s'" % ch).encode('utf-8')
    if self.inTitle:
      self.title += ch
    elif self.inContents:
      self.contents += ch

  def endElement(self, name):
    #print "</%s>" % name
    if name == 'page':
      self.inTitle = False
      self.inContents = False
      self.title = self.title.encode('utf-8')
      self.contents = self.contents.encode('utf-8')

      self.createArticle()

    elif name == 'title':
      self.inTitle = False
    elif name == 'text':
      self.inContents = False

def usage():
  print '''Usage:
  python import-xml.py <db file name> <xml file name>
    imports a wikipedia dump into the database'''

if __name__=='__main__':
  try:
    if len(argv) != 3:
      usage()
      exit(1)

    dbfile=argv[1]
    xmlfile=argv[2]
    file=open(xmlfile, 'r')
    parser = make_parser()
    parser.setContentHandler(XelapediaImport(dbfile))
    parser.parse(file)

    exit(0)
  except KeyboardInterrupt:
    stderr.write('Interrupted!\n')

# End Of File
