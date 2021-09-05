DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS amazon;
DROP TABLE IF EXISTS camel;

CREATE TABLE user (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    username TEXT NOT NULL
);

CREATE TABLE amazon (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chat_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    product_name TEXT NOT NULL,
    url TEXT NOT NULL,
    price REAL NOT NULL
);

CREATE TABLE camel (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chat_id INTEGER NOT NULL,
    url TEXT NOT NULL,
    type TEXT NOT NULL,
    supplier TEXT NOT NULL,
    price REAL,
    FOREIGN KEY (id) REFERENCES amazon(id)
);