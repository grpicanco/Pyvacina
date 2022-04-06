create table vacinador
(
    crm          VARCHAR(13)
        primary key,
    cpf          VARCHAR(11)  not null,
    nome         VARCHAR(128) not null,
    dtNascimento DATE         not null,
    unique (cpf, crm)
);

