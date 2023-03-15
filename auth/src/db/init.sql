CREATE TABLE IF NOT EXISTS users(
    id SERIAL primary key,
    username VARCHAR(25) UNIQUE,
    hashed_password VARCHAR(255)
);


-- DROP TABLE IF EXISTS users;