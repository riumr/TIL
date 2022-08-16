CREATE TABLE members(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
SELECT * FROM members

INSERT INTO members VALUES 
(1, 'A'), 
(2, 'B'),
(3, 'C'),
(4, 'D'),
(5, 'E');

DELETE FROM members WHERE rowid=4;
INSERT INTO members (name) VALUES ('D'); 
SELECT * FROM members;
-- id	name
-- 1	A
-- 2	B
-- 3	C
-- 5	E
-- 6	D 

