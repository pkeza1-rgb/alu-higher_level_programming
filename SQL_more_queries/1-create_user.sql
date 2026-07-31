-- Creates the MySQL user user_0d_1

-- Create user if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

-- Give all privileges to user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
