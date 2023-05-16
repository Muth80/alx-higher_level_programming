-- This script sets the database context to mysql
USE `mysql`;

-- This script lists all the tables in the current database
SELECT table_name AS Tables
FROM information_schema.tables
WHERE table_schema = DATABASE();
