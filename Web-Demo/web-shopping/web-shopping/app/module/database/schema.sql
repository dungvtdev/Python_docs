DROP TABLE IF EXISTS users;
CREATE TABLE users (
    user_id INTEGER NOT NULL PRIMARY KEY autoincrement,
    user_firstName VARCHAR(30) NOT NULL,
    user_lastName VARCHAR(30) NOT NULL,
    user_username VARCHAR(30) NOT NULL,
    user_email VARCHAR(30) NOT NULL,
    user_password VARCHAR(30) NOT NULL,
    user_phone VARCHAR(15) NOT NULL,
    user_role VARCHAR(2) NOT NULL
  );


DROP TABLE IF EXISTS product;
CREATE TABLE product (
    product_id INTEGER NOT NULL PRIMARY KEY autoincrement,
    product_name VARCHAR(30) NOT NULL,
    product_description VARCHAR(255) ,
    product_type VARCHAR(50) NOT NULL,
    product_color VARCHAR(30) NOT NULL,
    product_price FLOAT NOT NULL,
    product_sale FLOAT NOT NULL,
    product_bought INTEGER NOT NULL,
    product_time_up DATE NOT NULL
);

DROP TABLE IF EXISTS product_image;
CREATE TABLE product_image (
    img_id INTEGER NOT NULL PRIMARY KEY autoincrement,
    product_name VARCHAR(30) NOT NULL,
    img_name VARCHAR(50) NOT NULL,
    isMain VARCHAR(2) NOT NULL,
    isBig VARCHAR(2) NOT NULL,
    FOREIGN KEY (product_name) REFERENCES product(product_id)
);


DROP TABLE IF EXISTS comments;
CREATE TABLE comments(
    comments_id INTEGER NOT NULL PRIMARY KEY autoincrement,
    product_id INTEGER NOT NULL,
    comments_time DATE NOT NULL,
    comments_user VARCHAR(30) NOT NULL,
    FOREIGN KEY (product_id) REFERENCES product(product_id)
);