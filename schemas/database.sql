-- Active: 1696921476499@@127.0.0.1@3306@gym_db
DROP DATABASE IF EXISTS gym_db;

CREATE DATABASE gym_db DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE gym_db;

CREATE TABLE permissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    UNIQUE KEY (name)
);

INSERT INTO permissions (name)
 VALUES 
 ('admin'),
  ('trabajador'),
   ('cliente');

CREATE TABLE worker_admins (
    id INT AUTO_INCREMENT PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    name VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    permission_id INT NOT NULL,
    FOREIGN KEY (permission_id) REFERENCES permissions(id),
    UNIQUE KEY (email)
);

CREATE TABLE clients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    name VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    permission_id INT NOT NULL DEFAULT 3,
    FOREIGN KEY (permission_id) REFERENCES permissions(id),
    UNIQUE KEY (email)
);

CREATE TABLE is_membership (
    code_membership INT(6) PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    client_id INT NOT NULL,
    have_membership_id TINYINT(1) NOT NULL DEFAULT 0,
    expiration_date DATE,
    FOREIGN KEY (client_id) REFERENCES clients(id)
);

DELIMITER $$
CREATE TRIGGER generate_code_membership
BEFORE INSERT ON is_membership
FOR EACH ROW
BEGIN
    DECLARE new_code INT(6);
    SET new_code = FLOOR(RAND() * 900000) + 100000;
    WHILE EXISTS (SELECT * FROM is_membership WHERE code_membership = new_code) DO
        SET new_code = FLOOR(RAND() * 900000) + 100000;
    END WHILE;
    SET NEW.code_membership = new_code;
END$$
DELIMITER ;

