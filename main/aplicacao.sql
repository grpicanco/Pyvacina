create table aplicacao
(
    id        INTEGER
        primary key autoincrement,
    cns       VARCHAR(15) not null
        references vacinado
            on update cascade on delete restrict,
    crm       VARCHAR(13) not null
        references vacinador
            on update cascade on delete restrict,
    id_vacina INTEGER     not null
        references vacina
            on update cascade on delete restrict
);

