-- GROUP BY

-- 성별 갯수
SELECT last_name, COUNT(*)
FROM users
GROUP BY last_name;

-- last_name으로 구분한 값들의 avg(age)와 개수 출력
SELECT last_name, AVG(age), COUNT(*)
FROM users
GROUP BY last_name;

SELECT last_name, COUNT(*)
FROM users
GROUP BY last_name
LIMIT 5;
-- last_name	COUNT(*)
-- 강	         23
-- 고	         10
-- 곽	         4
-- 구	         2
-- 권	         17

-- WHERE은 GROUP BY 앞에 쓴다
SELECT last_name, COUNT(last_name)
FROM users
WHERE COUNT(last_name) > 100
GROUP BY last_name;
-- > 오류 
-- Parse error: misuse of aggregate: COUNT()
--   LECT last_name, COUNT(last_name) FROM users WHERE COUNT(last_name) > 100 GROUP

-- 조건에 따른 GROUP은 HAVING
SELECT last_name, COUNT(last_name)
FROM users
GROUP BY last_name
HAVING COUNT(last_name) > 100;
-- last_name	COUNT(last_name)
-- 김	         268
-- 이	         179