.schema

.table

SELECT * FROM albums ORDER BY Title DESC LIMIT 5;

SELECT COUNT(*) '고객 수' FROM customers;

SELECT FirstName '이름', LastName '성' FROM customers
WHERE country='USA' ORDER BY '이름' DESC LIMIT 5;

SELECT COUNT(*) '송장수' FROM invoices
WHERE BillingPostalCode IS NOT NULL;

SELECT * FROM invoices
WHERE BillingState is NULL ORDER BY InvoiceDate DESC LIMIT 5;

SELECT COUNT(*) FROM invoices
WHERE strftime('%Y',InvoiceDate)=2013;

SELECT 
CustomerId '고객ID', FirstName '이름', LastName '성'  FROM customers
WHERE substr(FirstName,1,1)='L' ORDER BY '고객ID';

SELECT Country '나라', count(*) '고객 수' FROM customers GROUP BY Country 
ORDER BY COUNT(Country) DESC LIMIT 5;

SELECT ArtistId, COUNT(*) '앨범 수' FROM albums
GROUP BY ArtistId
ORDER BY COUNT(*) DESC LIMIT 1;

SELECT ArtistId, COUNT(*) '앨범 수' FROM albums 
GROUP BY ArtistId HAVING COUNT(*)>=10;

SELECT Country, State, COUNT(*) '고객 수' FROM customers
WHERE State IS NOT NULL
GROUP BY Country, State
ORDER BY '고객 수' DESC, Country DESC LIMIT 5;

SELECT 
LastName, FirstName, (strftime('%Y','now')-strftime('%Y',BirthDate)+1) '나이'
FROM employees
ORDER BY EmployeeId;

SELECT 
    CustomerId, 
    CASE
        WHEN FAX IS NULL THEN 'X'
        ELSE 'O'
    END AS 'FAX 유/무'
FROM customers
ORDER BY CustomerId LIMIT 5;

SELECT Name FROM artists
WHERE ArtistId=(SELECT MAX(ArtistId) FROM albums);

SELECT Name FROM genres
WHERE GenreId=(SELECT MIN(GenreId) FROM tracks);

SELECT InvoiceId, UnitPrice FROM invoice_items
ORDER BY UnitPrice DESC LIMIT 5;

SELECT FirstName, COUNT(*) FROM customers
GROUP BY FirstName ORDER BY COUNT(*) DESC LIMIT 10;

SELECT FirstName, Company FROM customers
WHERE substr(Company,1,1)='G' LIMIT 5;