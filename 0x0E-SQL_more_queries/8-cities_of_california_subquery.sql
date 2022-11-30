-- A script that lists all the cities of California that can be found in the database hbtn_0d_usa
-- The 'states' table contains only one record where 'name = California' (but the id can be different
-- Results must be sorted in ascending order by cities.id
-- Not allowed to use the JOIN keyword
-- The database name will be passed as an argument of the mysql command
SELECT id, name
FROM cities
WHERE state_id = ( 
      SELECT id
      FROM states
      WHERE name = "California")
ORDER BY cities.id ASC;;
