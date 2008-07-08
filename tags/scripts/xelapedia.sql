DROP TABLE IF EXISTS titles;
CREATE TABLE titles(
  title text UNIQUE PRIMARY KEY,
  anchor text,
  article_id integer NOT NULL);
DROP TABLE IF EXISTS redirects;
CREATE TABLE redirects(
  title text UNIQUE PRIMARY KEY,
  redirect text,
  anchor text);
DROP TABLE IF EXISTS articles;
CREATE TABLE articles(
  id integer UNIQUE PRIMARY KEY,
  contents TEXT,
  compressed BLOB);
DROP TABLE IF EXISTS version;
CREATE TABLE version(
  id integer UNIQUE PRIMARY KEY,
  type text);
INSERT INTO version (id, type) VALUES(0, 'plain');
