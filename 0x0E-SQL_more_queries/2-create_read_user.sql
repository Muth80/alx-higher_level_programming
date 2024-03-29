-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS 'hbtn_0d_2';

-- Use the database
USE 'hbtn_0d_2';

-- Create the user with the SELECT privilege
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON 'hbtn_0d_2'.* TO 'user_0d_2'@'localhost';

