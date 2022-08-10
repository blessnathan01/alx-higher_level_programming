-- Script to create databases, user
-- and grant user privileges
-- CREATE DB
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- CREATE USER
CREATE USER IF NOT EXISTS user_0d_2@localhost
IDENTIFIED BY 'user_0d_2_pwd';

-- GRANT USER privileges
GRANT SELECT
ON hbtn_0d_2.*
TO user_0d_2@localhost;
