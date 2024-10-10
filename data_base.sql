CREATE DATABASE blog;
USE blog;

CREATE TABLE usuario (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(108) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL
);

CREATE TABLE post (
    id_post INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT,
    conteudo TEXT NOT NULL,
    data_post DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
);