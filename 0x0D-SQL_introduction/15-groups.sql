-- script that lists the number of records with the same score in the
-- table second_table of the database hbtn_0c_0 in MySQL server.
-- The result displays:
-- the score
-- the number of records for this score with the label number
SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score
ORDER BY score DESC;