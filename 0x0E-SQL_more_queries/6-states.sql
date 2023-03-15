-- A script that creates a database @hbtn_0d_usa that contains a table @states
-- A query that creates the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- A query that creats the table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id),
	UNIQUE(id)
);
