create table vacinado
(
    cns          VARCHAR(15)
        primary key,
    cpf          VARCHAR(11)  not null,
    nome         VARCHAR(128) not null,
    dtNascimento DATE         not null,
    comorbidade  INTEGER,
    qtdDose      INTEGER,
    unique (cpf, cns)
);

