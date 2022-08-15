create table product(
    name varchar(100),
    type varchar(100),
    price float,
    rating float,
    availability boolean,
    primary key(name, type, price)
);

insert into product values
    ('Lenevo ThinkBook 15 Gen 4 <AMD>', 'Laptop', 987.35, 4.0, true),
    ('Lenevo ThinkPad L15 Gen2 <Intel>', 'Laptop', 1053.47, 4.0, false),
    ('CyberPowerPC Gamer Supreme Liquid Cooled SLC10800CPG', 'Desktop', 2889.99, 3.5, null),
    ('HP OMEN 25L Tower', 'Desktop', 1499.99, 3.8, true),
    ('HP 15-ef2024ca FHD', 'Laptop', 929.99, 3.5, true),
    ('Razer Firefly V2', 'Mouse Mat', 59.99, 3.0, true),
    ('HyperX Cloud Core + 7.1', 'Gaming Headset', 49.99, 4.0, true),
    ('HyperX Alloy Core RGB Membrane', 'Gaming Keyboard', 59.99, 3.5, false),
    ('Anne Pro 2 60%', 'Mechanical Keyboard', 100.93, 4.0, true),
    ('Corsair Vengeance RGB PRO DDR4', '15GB (2 * 8GB) RAM Sticks', 88.99, 4.0, true);
    
