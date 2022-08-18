
-- 문자열 합치기 ||
-- (성+이름) 출력, 5명만
SELECT 
    last_name || first_name 이름,
    age,
    country
FROM users
LIMIT 5;
-- 이름	   age country
-- 유정호	40	전라북도
-- 이경희	36	경상남도
-- 구정자	37	전라남도
-- 장미경	40	충청남도
-- 차영환	30	충청북도

-- 문자열 길이 : LENGTH
SELECT 
    LENGTH(first_name),
    first_name
FROM users
LIMIT 5;
-- LENGTH(first_name)	first_name
-- 2	                정호
-- 2	                경희
-- 2	                정자
-- 2	                미경
-- 2	                영환

-- 문자열 변경 REPLACE
-- 016-7280-2855 => 016 7280 2855
SELECT 
    first_name,
    phone,
    REPLACE(phone, '-', ' ')
FROM users
LIMIT 5;
-- first_name  phone	       REPLACE(phone, '-', ' ')
-- 정호	        016-7280-2855	016 7280 2855
-- 경희	        011-9854-5133	011 9854 5133
-- 정자	        011-4177-8170	011 4177 8170
-- 미경	        011-9079-4419	011 9079 4419
-- 영환	        011-2921-4284	011 2921 4284

-- 숫자 활용
SELECT MOD(5, 2) FROM users;

-- 올림, 내림, 반올림
SELECT CEIL(3.14), FLOOR(3.14), ROUND(3.14)
FROM users
LIMIT 1;

-- 9의 제곱근
SELECT SQRT(9)
FROM users
LIMIT 1;

-- 9^2
SELECT POWER(9, 2)
FROM users
LIMIT 1;