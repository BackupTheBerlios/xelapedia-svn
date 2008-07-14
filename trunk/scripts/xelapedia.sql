--
-- Copyright (C) 2008 Alexander Mueller
--
-- This program is free software: you can redistribute it and/or modify
-- it under the terms of the GNU General Public License as published by
-- the Free Software Foundation, either version 3 of the License, or
-- (at your option) any later version.
--
-- This program is distributed in the hope that it will be useful,
-- but WITHOUT ANY WARRANTY; without even the implied warranty of
-- MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
-- GNU General Public License for more details.
--
-- You should have received a copy of the GNU General Public License
-- along with this program.  If not, see <http://www.gnu.org/licenses/>.
--
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
