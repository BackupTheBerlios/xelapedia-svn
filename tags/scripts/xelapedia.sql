DROP TABLE IF EXISTS titles;
CREATE TABLE titles(
  title text UNIQUE PRIMARY KEY,
  article_id integer NOT NULL);
DROP TABLE IF EXISTS articles;
CREATE TABLE articles(
  id integer PRIMARY KEY AUTOINCREMENT,
  contents TEXT);
DROP TABLE IF EXISTS version;
CREATE TABLE version(
  id integer PRIMARY KEY,
  type text);
INSERT INTO version (id, type) VALUES(0, 'plain');
