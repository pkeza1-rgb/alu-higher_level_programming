-- Creates database hbtn_0d_2 and read-only user

-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';

-- Grant only SELECT privilege
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
