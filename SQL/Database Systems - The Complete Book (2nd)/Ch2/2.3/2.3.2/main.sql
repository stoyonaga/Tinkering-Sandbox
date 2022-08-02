create table classes(
    class varchar(20),
    type char(2),
    country varchar(20),
    numGuns int,
    bore float,
    displacement float,
    primary key(class, type, country)
);

create table ships(
    name varchar(20),
    class varchar(20),
    launched int,
    primary key(name, class)
);

create table battles(
    name varchar(20), 
    date DATE, 
    primary key(name, date)
);

create table outcomes(
    ship varchar(20),
    battle varchar(20),
    result varchar(7),
    primary key(battle, result)
);
