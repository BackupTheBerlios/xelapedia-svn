from pysqlite2 import dbapi2 as sqlite
from sys import argv, exit

if len(argv) != 2:
	print "Usage: python create-db <db file>"
	exit(0)

db=argv[1]
conn = sqlite.connect(db)
cur = conn.cursor()

ops=[
'''DROP TABLE IF EXISTS articles''',
'''CREATE TABLE articles(
  id text PRIMARY KEY,
  title text UNIQUE,
  contents TEXT,
  compressed_contents BLOB)''',
'''DROP TABLE IF EXISTS tags''',
'''CREATE TABLE tags(
  name text PRIMARY KEY)''',
'''DROP TABLE IF EXISTS articles_tags''',
'''CREATE TABLE articles_tags(
  article_id text,
  tags_name text,
  PRIMARY key(article_id, tags_name))'''
]
for op in ops:
	try:
		cur.execute(op)
	except:
		print op
		raise

