-- sqlite3
-- 테이블 생성
CREATE TABLE practice (
    name TEXT,
    age INTEGER
);
-- 테이블 목록 조회
.tables
-- 특정 테이블 스키마 조회
.schema
-- 값 추가
INSERT INTO practice VALUES 
("A", 22),
("B", 23);
-- 테이블 조회
SELECT * FROM practice
-- 테이블 삭제
DROP TABLE practice