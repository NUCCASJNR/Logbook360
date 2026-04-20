 -- sql script
CREATE DATABASE IF NOT EXISTS log_db;
       CREATE USER IF NOT EXISTS 'log_user'@'localhost' IDENTIFIED BY 'Log_pwd123@';
              GRANT ALL PRIVILEGES ON log_db.* TO 'log_user'@'localhost';
                                      GRANT SELECT ON performance_schema.* TO 'log_user'@'localhost';
FLUSH PRIVILEGES;