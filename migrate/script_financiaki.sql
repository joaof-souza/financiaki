CREATE DATABASE IF NOT EXISTS financiaki;
USE financiaki;


CREATE TABLE usuarios (
 login VARCHAR(50) NOT NULL PRIMARY KEY,
 senha VARCHAR(200) NOT NULL
);


CREATE TABLE categorias (
 cod_categoria INT NOT NULL auto_increment,
 login VARCHAR(20) NOT NULL,
 categoria VARCHAR(30),

 PRIMARY KEY (cod_categoria,login),

 FOREIGN KEY (login) REFERENCES usuarios (login)
);


CREATE TABLE despesas (
 cod_despesa INT NOT NULL auto_increment,
 login VARCHAR(20) NOT NULL,
 descricao VARCHAR(100),
 data DATE,
 hora TIME(10),
 valor DECIMAL(2),
 cod_categoria INT NOT NULL,

 PRIMARY KEY (cod_despesa,login),

 FOREIGN KEY (login) REFERENCES usuarios (login),
 FOREIGN KEY (cod_categoria,login) REFERENCES categorias (cod_categoria,login)
);


