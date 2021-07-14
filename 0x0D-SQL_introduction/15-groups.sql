-- Task 15: Number by score
-- Lists the number of records with the same score in a table in your MySQL server
SELECT score, COUNT(score) AS 'number' FROM second_table GROUP BY score DESC;
