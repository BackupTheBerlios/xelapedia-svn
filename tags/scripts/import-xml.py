from pysqlite2 import dbapi2 as sqlite
from xml.sax import make_parser, saxutils, ContentHandler
from sys import argv, exit, stderr

class WikipediaDump(ContentHandler):
	def __init__(self, db):
		self.con=sqlite.connect(dbfile)
		self.cur=self.con.cursor()
		self.cur.execute('DELETE FROM articles')
		self.inTitle = False
		self.inId = False
		self.inContents = False
		self.counter=0

	def startElement(self, name, attrs):
		#print "<%s>" % name
		if name == 'page':
			self.inTitle = False
			self.inId = False
			self.inContents = False
			self.id = u''
			self.title = u''
			self.contents = u''
		elif name == 'title':
			self.inTitle = True
		elif name == 'id':
			self.inId = True
		elif name == 'text':
			self.inContents = True

	def characters(self, ch):
		#print ("'%s'" % ch).encode('utf-8')
		if self.inTitle:
			self.title += ch
		elif self.inId:
			self.id += ch
		elif self.inContents:
			self.contents += ch

	def endElement(self, name):
		#print "</%s>" % name
		if name == 'page':	
			self.inTitle = False
			self.inId = False
			self.inContents = False

			self.cur.execute('INSERT INTO articles(id,title,contents) VALUES(?, ?, ?);', (self.id, self.title.encode('utf-8'), self.contents.encode('utf-8'),))
			self.con.commit()
			stderr.write('.')
		elif name == 'id':
			self.inId = False
		elif name == 'title':
			self.inTitle = False
		elif name == 'text':
			self.inContents = False

def usage():
	print 'Aufruf import-xml.py <db file name> <xml file name>'


if __name__=='__main__':
	if len(argv) != 3:
		usage()
		exit()
	dbfile=argv[1]
	file=open(argv[2], 'r')
	parser = make_parser()
	parser.setContentHandler(WikipediaDump(dbfile))
	parser.parse(file)


