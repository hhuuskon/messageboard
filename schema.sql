CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    role_id INTEGER
);

CREATE TABLE topics (
    id SERIAL PRIMARY KEY,
    subjects TEXT,
    user_id INTEGER REFERENCES users,
    sent_at TIMESTAMP DEFAULT Now(),
    visibility INTEGER
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    topic_id INTEGER REFERENCES topics,
    content TEXT,
    user_id INTEGER REFERENCES users,
    sent_at TIMESTAMP DEFAULT Now(),
    modified_at TIMESTAMP DEFAULT Now(),
    visibility INTEGER
);

CREATE TABLE submessages (
    id SERIAL PRIMARY KEY,
    message_id INTEGER REFERENCES messages,
    user_id INTEGER REFERENCES users,
    content TEXT,
    sent_at TIMESTAMP DEFAULT Now(),
    modified_at TIMESTAMP DEFAULT Now(),
    visibility INTEGER
);

CREATE TABLE reputation (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    amout INTEGER

);