CREATE TABLE people (
    name TEXT NOT NULL,
    age INT NOT NULL,
    address TEXT NOT NULL
);

INSERT INTO people VALUES 
('A', 30, '서울'), 
('B', 30, '제주'),
('C', 26, '인천');

SELECT * FROM people;
-- name	age	address
-- A	30	서울
-- B	30	제주
-- C	26	인천

SELECT rowid, address FROM people;
-- rowid	address
-- 1	서울
-- 2	제주
-- 3	인천

SELECT rowid, name FROM people LIMIT 2;
-- rowid	name
-- 1	A
-- 2	B

SELECT rowid, name FROM people LIMIT 1 OFFSET 2;
-- rowid	name
-- 3	C

SELECT * FROM people WHERE address='제주';
-- name	age	address
-- B	30	제주

SELECT name FROM people WHERE age >= 30;
-- name
-- A
-- B

SELECT DISTINCT address FROM people;
-- address
-- 서울
-- 제주
-- 인천

-- 삭제 
DELETE FROM people WHERE rowid=2;
SELECT rowid, name FROM people
-- rowid	name
-- 1	A
-- 3	C

INSERT INTO people VALUES ('D', 30, '강원'); 
SELECT rowid, * FROM people;
-- rowid	name	age	address
-- 1	A	30	서울
-- 3	C	26	인천
-- 4	D	30	강원

-- 수정
UPDATE people SET name='C', address='서울' WHERE rowid=4;
SELECT rowid, * FROM people;
-- rowid	name	age	address
-- 1	A	30	서울
-- 3	C	26	인천
-- 4	C	30	서울

SELECT rowid, name FROM people LIMIT 100;
-- rowid	name
-- 1	A
-- 3	C
-- 4	C

DROP TABLE people;