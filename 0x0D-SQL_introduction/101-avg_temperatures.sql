-- Task 18: Temperatures #0
-- Import in database the dump table temperatures
SELECT city, AVG(value) AS 'avg_temp'
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
