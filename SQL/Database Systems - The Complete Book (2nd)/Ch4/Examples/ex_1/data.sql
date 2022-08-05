insert into drinkers(name, addr) values
    ('John Doe', '123 Fake Street'),
    ('Jane Doe', '123 Fake Street'),
    ('Bob Kazamakis', '1500 Glengrove Street'),
    ('Jim Halpert', '125 Johannasburg Rover');

insert into beers(name, manf) values
    ('Pure', 'Sapporo Breweries'),
    ('Ale', 'Anheuser-Busch'),
    ('Lager', 'Anheuser-Busch'),
    ('Light', 'Sapporo Breweries');

insert into buddies(buddy1, buddy2) values
    ('Bob Kazamakis', 'Jim Halpert');

insert into married(husband, wife) values
    ('John Doe', 'Jane Doe');

insert into likes(drinker, beer) values
    ('Bob Kazamakis', 'Pure'),
    ('Jim Halpert', 'Light');

insert into favorite(drinker, beer) values  
    ('Bob Kazamakis', 'Light'),
    ('Jim Halpert', 'Pure');
