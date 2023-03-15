-- A script that creates a new database @hbtn_0d_2 and user @user_0d_2
-- This query creates the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- This query creates the new user
CREATE USER IF NOT EXITS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd'
-- This query grants @SELECT privileges in the database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost'
