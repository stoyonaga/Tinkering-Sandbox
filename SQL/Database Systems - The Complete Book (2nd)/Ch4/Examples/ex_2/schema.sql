create table beers(
    name varchar(25),
    manf varchar(25),
    primary key(name)
);

create table ales(
    name varchar(25),
    manf varchar(25),
    colour varchar(25),
    primary key(name),
    foreign key(name) references beers(name)
);
