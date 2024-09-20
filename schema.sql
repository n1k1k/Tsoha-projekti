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
    author TEXT REFERENCES testuser(username),
    author_id INTEGER REFERENCES testuser(id),
    date_added TEXT
);

CREATE TABLE comment (
    id SERIAL PRIMARY KEY,
    content TEXT,
    author_id INTEGER REFERENCES testuser(id),
    author TEXT REFERENCES testuser(username),
    post_id INTEGER REFERENCES testpost(id),
    date_added TEXT
);