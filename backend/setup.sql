 -- sql script
CREATE DATABASE IF NOT EXISTS sabirent_db;
       CREATE USER IF NOT EXISTS 'sabirent_user'@'localhost' IDENTIFIED BY 'Sabirent_pwd123@';
              GRANT ALL PRIVILEGES ON sabirent_db.* TO 'sabirent_user'@'localhost';
                                      GRANT SELECT ON performance_schema.* TO 'sabirent_user'@'localhost';
FLUSH PRIVILEGES;