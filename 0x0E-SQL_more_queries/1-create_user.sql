-- A script that creates a new user @user_0d_1 on the MySQL server
-- This query create a new user named @user_0d_1 only if the user doesn't exist
-- already
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost'
