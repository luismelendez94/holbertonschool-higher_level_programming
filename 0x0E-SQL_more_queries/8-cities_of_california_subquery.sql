-- Task 8: Cities of California
-- Lists all cities of California that can be found in database hbtn_0d_usa
SELECT cities.id, cities.name
FROM states, cities
WHERE states.id = cities.state_id
ORDER BY cities.id ASC;
