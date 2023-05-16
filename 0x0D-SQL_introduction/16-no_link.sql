-- This script lists all records of the table second_table of the hbtn_0c_0 database
-- Rows without a name value are not listed
-- Results display the score and the name, sorted by descending score
SELECT score, name
FROM hbtn_0c_0.second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
