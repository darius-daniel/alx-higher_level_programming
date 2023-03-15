-- A script that creates a new database @hbtn_0d_usa and a table @cities
-- A query to create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- A query to create a table @cities inside @hbtn_0d_usa
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id)
);
