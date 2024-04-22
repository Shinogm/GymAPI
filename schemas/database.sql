-- Active: 1696921476499@@127.0.0.1@3306@
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
    permission_id INT NOT NULL,
    FOREIGN KEY (permission_id) REFERENCES permissions(id),
    UNIQUE KEY (email)
);

CREATE TABLE is_membership (
    code_membership INT(6) AUTO_INCREMENT PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    client_id INT NOT NULL,
    have_membership_id TINYINT(1) NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(id),
    UNIQUE KEY (code_membership)
);
