CREATE TABLE "user" (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE, 
    email VARCHAR(255),
    password TEXT,
    role_id INTEGER REFERENCES "role"(id),
    date_added TIMESTAMP
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
    title VARCHAR(50),
    content VARCHAR(2000),
    date_added TIMESTAMP,
    author_id INTEGER REFERENCES "user"(id)
    ON DELETE CASCADE
);

CREATE TABLE comment (
    id SERIAL PRIMARY KEY,
    content VARCHAR(500),
    author_id INTEGER REFERENCES "user"(id)
    ON DELETE CASCADE,
    date_added TIMESTAMP,
    post_id INTEGER REFERENCES post(id)
    ON DELETE CASCADE
);