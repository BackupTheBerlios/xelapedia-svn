DROP TABLE IF EXISTS titles;
CREATE TABLE titles(
  title text UNIQUE PRIMARY KEY,
  anchor text,
  article_id integer NOT NULL);
DROP TABLE IF EXISTS redirects;
CREATE TABLE redirects(
  title text UNIQUE PRIMARY KEY,
  redirect text);
DROP TABLE IF EXISTS articles;
CREATE TABLE articles(
  id integer UNIQUE PRIMARY KEY,
  contents TEXT,
  compressed BLOB);
DROP TABLE IF EXISTS config;
CREATE TABLE config(
  id integer UNIQUE PRIMARY KEY,
  main_page TEXT,
  image_tag TEXT,
  category_tag TEXT,
  type text);
INSERT INTO config (id, main_page, image_tag, category_tag, type) 
VALUES(0, 'Main Page', NULL, NULL, 'plain');
-- End Of File --
