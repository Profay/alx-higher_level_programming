-- script that lists all records with a score >= 10 in the table second_table
-- of the database hbtn_0c_0 in MySQL server
-- Results display both the score and the name
-- Records are ordered by score in descending order
SELECT score, name FROM second_table WHERE score >= 10
ORDER BY score DESC;
