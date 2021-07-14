-- Task 16: Say my name
-- Lists all records in a table in your MySQL server
SELECT score, name FROM second_table WHERE name IS NOT NULL AND TRIM(name) <> '' ORDER BY score DESC;
