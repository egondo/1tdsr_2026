CREATE TABLE TR_VEICULO(
    marca varchar(20),
    modelo varchar(20),
    ano number(4),
    placa varchar(10),
    valor number(5, 2),
    id number generated always as identity,
    primary key(id)
);

CREATE TABLE TR_CLIENTE(
    id number generated always as identity,
    nome varchar(50),
    telefone varchar(15),
    documento varchar(20),
    primary key(id)
);

create table TR_LOCACAO(
    id number generated always as identity,
    retirada date,
    devolucao date,
    valor number(6, 2),
    cliente_id number,
    veiculo_id number,
    status number(2),
    primary key(id),
    foreign key (cliente_id) references TR_CLIENTE(id),
    foreign key (veiculo_id) references TR_VEICULO(id)
);