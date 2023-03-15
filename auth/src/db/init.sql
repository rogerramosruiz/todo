CREATE TABLE IF NOT EXISTS users(
    id SERIAL primary key,
    usernmae VARCHAR(25) UNIQUE,
    hashed_password VARCHAR(255)
);


-- DROP TABLE IF EXISTS users;