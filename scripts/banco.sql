create table clientes(
cod_cliente serial primary key NOT NULL,
Nome        varchar(50) not NULL,
Sobrenome   varchar(50) not NULL,
CPF         varchar (11) not null,
email       char (100) not null,
senha       char (50) not null,
endereco    char (100),
telefone    char (11));


create table Produtos(
cod_produto serial primary key not null,
nome varchar(50) not null,
descricao varchar(200) not null,
preco numeric (16,2));


create table Pedidos(
cod_pedido serial primary key not null,
data_pedido char(50) not null,
valor numeric (16,2) not null,
cod_cliente serial,
    CONSTRAINT fk_pedido_client FOREIGN KEY (cod_cliente) REFERENCES clientes (cod_cliente));


create table itens_pedido(
cod_item serial primary key not null,
cod_pedido integer,
    CONSTRAINT fk_itens_pedidos FOREIGN KEY (cod_pedido) REFERENCES Pedidos (cod_pedido),
cod_produto integer,
    CONSTRAINT fk_compras FOREIGN KEY (cod_produto) REFERENCES Produtos (cod_produto),
Quantidade numeric(16,2), --TODO foi mudado para numeric - recriar
valor_unitario numeric(16,2));

