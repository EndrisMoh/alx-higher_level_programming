-- A script that lists number of records with the same score in second_table of db 'hbtn_0c_0'
-- The result should display: the score & the number of records for this score with label number
-- The list should be sorted by the number of records (descending)
-- The database name will be passed as an argument to the mysql command
SELECT score, COUNT(1) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
