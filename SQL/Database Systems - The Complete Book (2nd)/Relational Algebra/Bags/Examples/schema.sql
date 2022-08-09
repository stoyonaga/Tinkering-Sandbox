create table u(
    a int,
    b int,
    c int
);

create table v(
    b int,
    c int,
    d int
);

insert into u(a, b, c) values
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9);

insert into v(b, c, d) values
    (2, 3, 10),
    (2, 3, 11),
    (6, 7, 12);
