/*
    Title: db_init.sql
    Author: Heather Maynard
    Date: March 2, 2023
    Description: initialization script for WhatABook database
*/

--create database 
create database whatabook;

-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create user and grant privileges
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant privileges to database to whatabook_user on the localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    insert store 
*/
INSERT INTO store(locale)
    VALUES('9571 Hollyview lane, Tennessee, TN 68465');

/*
    insert books
*/
INSERT INTO book(book_name, author, details)
    VALUES('The Once Long Gone', 'Kelly Wildwood', 'The first book of the Gone series');

INSERT INTO book(book_name, author, details)
    VALUES('The Forgotten', 'Kelly Wildwood', 'The second book of the Gone series');

INSERT INTO book(book_name, author, details)
    VALUES('The Memories', 'Kelly Wildwood', 'The third book of the Gone series');

INSERT INTO book(book_name, author)
    VALUES('The Gone Girl', 'Kelly Wildwood');

INSERT INTO book(book_name, author)
    VALUES('Happiness is Near', 'Abby Lilly');

INSERT INTO book(book_name, author)
    VALUES("Houses Undone", 'Kyle Left');

INSERT INTO book(book_name, author)
    VALUES('Hey There Darling', 'Jerald Houseing');

INSERT INTO book(book_name, author)
    VALUES('Beach Please', 'Ashley Lewis');

INSERT INTO book(book_name, author)
    VALUES('The Great Debacle', 'Spencer Hash');

/*
    insert users
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('Kent', 'Wakesfield');

INSERT INTO user(first_name, last_name)
    VALUES('Michelle', 'Haddings');

INSERT INTO user(first_name, last_name)
    VALUES('Sophia', 'Littlesworth');

/*
    insert wishlists
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Kent'), 
        (SELECT book_id FROM book WHERE book_name = 'The Gone Girl')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Michelle'),
        (SELECT book_id FROM book WHERE book_name = 'Beach Please')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Sophia'),
        (SELECT book_id FROM book WHERE book_name = 'Hey There Darling')
    );
