create database if not exists pizzariadb;
use pizzariadb;

create table if not exists pizza (
id_pizza int primary key auto_increment,
sabor varchar(30),
preco_base decimal(5,2)
);

insert into pizza values
(default, 'Calabresa', 35.00),
(default, 'Frango com Catupiry', 40.00),
(default, 'A moda', 30.00),
(default, 'Portuguesa', 45.00),
(default, 'Quatro Queijos', 50.00);

select * from pizza;


create table if not exists tamanho (
id_tamanho int primary key auto_increment,
nome_tamanho varchar(20),
fator_preco decimal(5,2)
);

insert into tamanho (id_tamanho, nome_tamanho, fator_preco) values
(default, 'Broto', 17.90),
(default, 'Pequena', 27.90),
(default, 'Media', 39.90),
(default, 'Grande', 49.90),
(default, 'Gigante', 59.90);

select * from tamanho;

create table if not exists bebida (
id_bebida int primary key auto_increment,
nome_bebida varchar(30),
preco decimal(5,2)
);

insert into bebida (id_bebida, nome_bebida, preco) values
(default, 'Coca-Cola Lata', 6.50),
(default, 'Coca-Zero Lata', 6.50),
(default, 'Guaraná Lata', 7.50),
(default, 'Suco Del Valle', 4.00),
(default, 'H2OH! Limão', 6.80);

select * from bebida;

create table if not exists pedido (
id_pedido int primary key auto_increment,
nome_cliente varchar(100),
data_pedido date,
id_pizza int,
id_tamanho int,
id_bebida int,
foreign key (id_pizza) references Pizza(id_pizza),
foreign key (id_tamanho) references Tamanho(id_tamanho),
foreign key (id_bebida) references Bebida(id_bebida)
);

insert into pedido (id_pedido, nome_cliente, data_pedido, id_pizza, id_tamanho, id_bebida) values
(1, 'Lucas Pereira', '2025-07-01', 1, 2, 1), 
(2, 'Ana Costa', '2025-07-01', 5, 3, 5), 
(3, 'Laryssa Siqueira', '2025-07-01', 4, 1, 3), 
(4, 'João Castro', '2025-07-01', 2, 2, 4);

select * from pedido;