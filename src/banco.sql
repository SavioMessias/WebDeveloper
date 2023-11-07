drop database if exists contacts;

create database contacts;

use contacts;

CREATE TABLE contatos (
    con_id int primary key auto_increment,
    con_email varchar(100) not null,
    con_assunto varchar(100) not null,
    con_desc varchar(255) not null
)