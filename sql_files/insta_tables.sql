
create database ig_clone;
use ig_clone;

create table users (
id int auto_increment primary key,
username VARCHAR(255) UNIQUE,
created_at TIMESTAMP DEFAULT NOW());


create table photos ( id int auto_increment primary key,
image_url varchar(255) NOT NULL, user_id int NOT NULL, 
created_ad TIMESTAMP DEFAULT NOW(), foreign key(user_id) references users(id));

create table comments (
id int auto_increment primary key,
comment_text varchar(255) NOT NULL,
user_id int NOT NULL,
photo_id int NOT NULL,
created_at TIMESTAMP DEFAULT NOW(),
FOREIGN KEY(user_id) REFERENCES users(id),
FOREIGN KEY(photo_id) REFERENCES photos(id)
);

create table likes (
user_id int not null,
photo_id int not null,
created_at TIMESTAMP DEFAULT NOW(),
foreign key(user_id) references	users(id),
foreign key(photo_id) references photos(id),
primary key(user_id, photo_id)
);

create table follows(
follower_id int not null,
followee_id int not null,
created_at TIMESTAMP DEFAULT NOW(),
foreign key(follower_id) references users(id),
foreign key (followee_id) references users(id),
primary key(follower_id, followee_id)
);

create table tags(
id int auto_increment primary key,
tag_name varchar(255) unique,
created_at TIMESTAMP DEFAULT NOW()
);


CREATE TABLE photo_tags (
    photo_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    FOREIGN KEY(photo_id) REFERENCES photos(id),
    FOREIGN KEY(tag_id) REFERENCES tags(id),
    PRIMARY KEY(photo_id, tag_id)
);

