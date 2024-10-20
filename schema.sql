CREATE TABLE "user" (
    id SERIAL PRIMARY KEY,
    username VARCHAR(35) UNIQUE, 
    email VARCHAR(200),
    password VARCHAR(300),
    bio VARCHAR(500),
    role_id INTEGER REFERENCES "role"(id),
    date_added TIMESTAMP(0)
);

CREATE TABLE role (
    id SERIAL PRIMARY KEY,
    role_name VARCHAR(50)
);

CREATE TABLE following (
    follower_id INTEGER REFERENCES "user"(id)
    ON DELETE CASCADE,
    followed_id INTEGER REFERENCES "user"(id)
    ON DELETE CASCADE
);

CREATE TABLE post (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    content VARCHAR(2500),
    date_added TIMESTAMP(0),
    author_id INTEGER REFERENCES "user"(id)
    ON DELETE CASCADE
);

CREATE TABLE comment (
    id SERIAL PRIMARY KEY,
    content VARCHAR(1000),
    author_id INTEGER REFERENCES "user"(id)
    ON DELETE CASCADE,
    date_added TIMESTAMP(0),
    post_id INTEGER REFERENCES post(id)
    ON DELETE CASCADE
);