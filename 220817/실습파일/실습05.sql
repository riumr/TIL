-- SQLite
-- 테이블 생성

CREATE TABLE people (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

-- 데이터를 추가
.mode csv
-- 같은 디렉토리에 있는 users.csv 파일을 users 테이블로
.import users.csv people


-- 쿼리
-- 조회
-- 30세 이상인 사람들
SELECT * FROM people WHERE age >= 30;
-- 30세 이상인 사람들의 이름
SELECT first_name FROM people WHERE age >= 30;
-- 30세 이상인 사람들의 이름 2명만
SELECT first_name FROM people WHERE age >= 30 LIMIT 2;
-- 30세 이상이고 성이 김인 사람
SELECT age, first_name FROM people WHERE age >= 20 AND last_name = '김';

-- 30세 이상인 사람들의 숫자 : 414
SELECT COUNT(*) FROM people WHERE age >= 30;
-- 전체 중에 가장 작은 나이 : 15
SELECT MIN(age) FROM people;
-- 이씨 중에 가장 작은 나이 : 15
SELECT MIN(age) FROM people WHERE last_name = '이';
-- 이씨 중에 가장 작은 나이를 가진 사람의 이름과 계좌잔고 : 15	은영    78000
SELECT MIN(age), first_name, balance FROM people WHERE last_name = '이';
-- 20세 이상인 사람들의 평균 나이 : 30.1588310038119
SELECT AVG(age) FROM people WHERE age >= 20;
-- 계좌 잔액이 가장 높은 사람 : 1000000	순옥
SELECT MAX(balance), first_name FROM people;

-- 지역번호가 02인 사람 : 249
SELECT COUNT(*) FROM people WHERE phone LIKE '02-%';
-- 준으로 끝나는 사람 : 31
SELECT COUNT(*) FROM people WHERE first_name LIKE '%준';
-- 중간번호가 2114 : 0
SELECT COUNT(*) FROM people WHERE phone LIKE '%-2114-%';

-- 나이 오름차순 10명의 성
SELECT last_name FROM people ORDER BY age ASC LIMIT 10;
-- 나이, 성 순으로 오름차순 10명
SELECT * FROM people ORDER BY age, last_name LIMIT 10;
-- 계좌 잔액 순 내림차순 10명
SELECT last_name, first_name, balance FROM people ORDER BY balance DESC LIMIT 10;
-- 계좌 잔액 내림차순(높은->낮은 것), 성 오름차순(ㄱ->ㅎ)
SELECT last_name, first_name, balance FROM people ORDER BY balance DESC, last_name ASC LIMIT 10;