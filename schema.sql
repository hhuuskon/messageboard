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
    modified_at TIMESTAMP,
    visibility INTEGER
);