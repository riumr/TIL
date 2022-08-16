-- Table : people
-- name : text
-- age : INT
-- address : TEXT

CREATE TABLE people (
    name TEXT,
    age INT,
    address TEXT
);

INSERT INTO people (name, age) VALUES ('A', 23);
SELECT * FROM people;

INSERT INTO people (name, age, address) VALUES ('A', 23, '서울');
INSERT INTO people VALUES ('B', 30, '서울');

SELECT rowid, * FROM people;

DROP TABLE people;