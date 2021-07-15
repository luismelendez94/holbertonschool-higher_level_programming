-- Task 1: Root user
-- Create the MySQL server user user_0d_1
DROP USER 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL ON * . * TO 'user_0d_1'@'localhost';
