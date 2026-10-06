
create table clube(
    id number generated always as identity,
    nome varchar(30),
    vitorias number,
    empates number,
    derrotas number,
    primary key(id)
)

create table partida(
    id number generate always as identity,
    id_mandante number,
    id_visitante number,
    gols_visitante number,
    gols_mandante number
)

