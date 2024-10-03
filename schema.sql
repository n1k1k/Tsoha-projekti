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
    follower_id INTEGER REFERENCES "user"(id),
    followed_id INTEGER REFERENCES "user"(id)
);

CREATE TABLE post (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50),
    content VARCHAR(2000),
    author_id INTEGER REFERENCES "user"(id),
    date_added TIMESTAMP
);

CREATE TABLE comment (
    id SERIAL PRIMARY KEY,
    content VARCHAR(500),
    author_id INTEGER REFERENCES "user"(id),
    post_id INTEGER REFERENCES post(id),
    date_added TIMESTAMP
);