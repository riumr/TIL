SELECT smoking,COUNT(*) FROM healthcare GROUP BY smoking;

SELECT is_drinking, COUNT(*) FROM healthcare GROUP BY is_drinking;

SELECT is_drinking, COUNT(*) FROM healthcare 
WHERE blood_pressure>=200 GROUP BY is_drinking;

SELECT sido, COUNT(sido) FROM healthcare
GROUP BY sido HAVING COUNT(sido)>=50000;

SELECT height, COUNT(*) FROM healthcare
GROUP BY height ORDER BY COUNT(*) DESC LIMIT 5;

SELECT weight, height, COUNT(*) FROM healthcare
GROUP BY height, weight ORDER BY COUNT(*) DESC LIMIT 5;

SELECT is_drinking, AVG(waist),COUNT(*) FROM healthcare
GROUP BY is_drinking;

SELECT gender,
ROUND(AVG(va_left),2) '평균 왼쪽 시력', 
ROUND(AVG(va_right),2) '평균 오른쪽 시력'
FROM healthcare
GROUP BY gender;

SELECT age,
AVG(height) '평균 키',AVG(weight) '평균 몸무게'
FROM healthcare
GROUP BY age HAVING '평균 키'>=160 and '평균 몸무게'>=60;

SELECT is_drinking, smoking,
AVG(weight/(height*height*0.00001)) AS '평균 BMI' 
FROM healthcare
WHERE is_drinking!='' and smoking!=''
GROUP BY is_drinking, smoking;