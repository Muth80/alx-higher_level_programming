-- This script lists all records with a score >= 10 in the table second_table of the hbtn_0c_0 database
-- The results display both the score and the name columns, ordered by score (top first)
SELECT score, name
FROM hbtn_0c_0.second_table
WHERE score >= 10
ORDER BY score DESC;
