CREATE TABLE "user" (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE, 
    email VARCHAR(255),
    password TEXT,
    role TEXT, 
    date_added TEXT
);

CREATE TABLE post (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50),
    content TEXT,
    author TEXT REFERENCES "user"(username),
    author_id INTEGER REFERENCES "user"(id),
    date_added TEXT
);

CREATE TABLE comment (
    id SERIAL PRIMARY KEY,
    content TEXT,
    author_id INTEGER REFERENCES "user"(id),
    author TEXT REFERENCES "user"(username),
    post_id INTEGER REFERENCES post(id),
    date_added TEXT
);