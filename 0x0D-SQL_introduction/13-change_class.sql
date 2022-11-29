-- A script that removes all records with a score <= 5 in the'second_table' of db 'hbtn_0c_0'
-- The database name will be passed as an argument of the mysql command
DELETE FROM second_table
WHERE score <= 5;
