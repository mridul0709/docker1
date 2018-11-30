CREATE USER docker WITH PASSWORD 'docker';
CREATE DATABASE docker;
GRANT ALL PRIVILEGES ON DATABASE docker TO docker;
\c docker
CREATE TABLE docker (string varchar);
INSERT INTO docker VALUES ('Hello World');
GRANT ALL PRIVILEGES ON TABLE docker TO docker;
