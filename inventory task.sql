create database inventory_store;
use inventory_store;
create table if not exists users (
    username varchar(50),
    password varchar(50)
);

-- Create inventory table
create table if not exists inventory (
    id int primary key auto_increment,
    item varchar(100),
    qty int
);

insert into users (username, password)
select 'admin', 'admin123'
from dual
where not exists (select 1 from users where username = 'admin');
show databases;
select* from inventory;
select* from users;