-- script that creates the MySQL server user user_0d_1
-- Create user if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhot'
IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;
