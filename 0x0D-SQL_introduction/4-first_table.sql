-- A script that creates a table called first_table in the current database, 'hbtn_0c_0'
-- 'first_table' should have (id INT) and (name VARCHAR(256))
-- db name will be passed as argument of mysql cmd
-- If table 'first_table' already exists, should not fail.
-- Not allowed to use SELECT or SHOW statements
CREATE TABLE IF NOT EXISTS first_table (id INT,
name VARCHAR(256));
