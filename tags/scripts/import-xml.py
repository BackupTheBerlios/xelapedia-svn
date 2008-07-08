from sqlite3 import dbapi2 as sqlite
from xml.sax import make_parser, saxutils, ContentHandler
from sys import argv, exit, stderr
import re

class WikipediaDump(ContentHandler):
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
      m=re.match(r'[^[]*\[\[([^]#]+)(#([^]]+))?\]\]', self.contents[len(REDIRECT):])
      if m:
        return [m.group(1),  m.group(3)]
      else:
        raise Exception("Warning: Illegal redirect in page %s:\n%s\n"
          % (self.title, self.contents))

  def findArticleIdForTitle(self, title):
    self.cur.execute('SELECT article_id FROM titles WHERE title=?', (title,))
    return self.cur.fetchone()[0]

  def createArticle(self):
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
      anchor=redirect[1]
      if anchor == None: anchor=""
      stderr.write("Info: Found redirect to %s %s\n" % (redirect[0],  anchor))
      self.cur.execute('INSERT INTO redirects '
        '(title, redirect, anchor) VALUES(?,?,?)',
        (self.title, redirect[0], redirect[1]))
      self.con.commit()

    stderr.write('.')

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
  python import-xml.py import <db file name> <xml file name>
    imports a wikipedia dump into the database
  python import-xml.py redirectes <db file name>
    processes an existing database and resolves redirects'''

def processRedirects(dbfile):
  return

if __name__=='__main__':
  try:
    if len(argv) < 2:
      usage()
      exit(1)

    cmd=argv[1]
    if cmd == 'import':
      if len(argv) != 4:
        usage()
        exit(1)

      dbfile=argv[2]
      file=open(argv[3], 'r')
      parser = make_parser()
      parser.setContentHandler(WikipediaDump(dbfile))
      parser.parse(file)

    elif cmd == 'redirects':
      if len(argv) != 2:
        usage()
        exit(1)
      processRedirects(argv[2])

    else:
      usage()
      exit(1)

    exit(0)
  except KeyboardInterrupt:
    stderr.write('Interrupted!\n')
