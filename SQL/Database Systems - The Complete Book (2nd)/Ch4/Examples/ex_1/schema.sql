create table drinkers(
    name varchar(25),
    addr varchar(25),
    primary key(name)
);

create table beers(
    name varchar(25),
    manf varchar(25),
    primary key(name)
);

create table buddies(
    buddy1 varchar(25),
    buddy2 varchar(25),
    primary key(buddy1, buddy2),
    foreign key(buddy1) references drinkers(name),
    foreign key(buddy2) references drinkers(name)
);

create table married(
    husband varchar(25),
    wife varchar(25),
    primary key(husband, wife),
    foreign key(husband) references drinkers(name),
    foreign key(wife) references drinkers(name)
);

create table likes(
    drinker varchar(25),
    beer varchar(25),
    primary key(drinker, beer),
    foreign key(drinker) references drinkers(name),
    foreign key(beer) references beers(name)
);

create table favorite(
    drinker varchar(25),
    beer varchar(25),
    primary key(drinker, beer),
    foreign key(drinker) references drinkers(name),
    foreign key(beer) references beers(name)
);
