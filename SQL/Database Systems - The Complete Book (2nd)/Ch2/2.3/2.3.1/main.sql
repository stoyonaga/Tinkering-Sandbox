create table product(
    maker varchar(20),
    model int,
    type varchar(7),
    primary key(model)
);

create table pc(
    model int,
    speed double precision,
    ram int,
    hd int,
    price double precision,
    primary key(model)
);

create table laptop(
    model int,
    speed double precision,
    ram int,
    hd int,
    screen double precision,
    price double precision,
   primary key(model) 
);

create table printer(
    model int,
    color boolean,
    type varchar(7),
    price double precision,
    primary key(model)
);
