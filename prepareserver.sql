
CREATE DATABASE login;
USE login;
CREATE TABLE loginDatabase(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    usertype VARCHAR(255) NOT NULL
)