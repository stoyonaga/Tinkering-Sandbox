create table characters(
    name varchar(25),
    affiliation varchar(25),
    rating int,
    skill varchar(25),
    primary key(name, affiliation)
);

insert into characters(name, affiliation, rating, skill) values
    ('Andy', 'Orange Star', 8, 'Beginner Friendly'),
    ('Max', 'Orange Star', 7, 'Beginner Friendly'),
    ('Sami', 'Orange Star', 7, 'Situationally Strong'),
    ('Eagle', 'Green Earth', 9, 'Situationally Strong'),
    ('Jess', 'Green Earth', 6, 'Beginner Friendly'),
    ('Javier', 'Green Earth', 7, 'Beginner Friendly'),
    ('Sensei', 'Yellow Comet', 9, 'OP!!'),
    ('Grimm', 'Yellow Comet', 10, 'Situationally OP!!'),
    ('Hawke', 'Black Hole', 10, 'OP!!'),
    ('Lash', 'Black Hole', 10, 'OP!!');

insert into characters(name, affiliation) values
    ('Isabelle', 'Animal Crossing'),
    ('Biff', 'Animal Crossing'),
    ('Chief', 'Animal Crossing'),
    ('Slider', 'Animal Crossing'),
    ('Max', '????'),
    ('Chloe', '????'),
    ('Warren', '????'),
    ('Rachel', '????'),
    ('Papyrus', 'Undertale'),
    ('Red', '????'),
    ('Tracer', 'Overwatch'),
    ('Soldier 76', 'Overwatch');
