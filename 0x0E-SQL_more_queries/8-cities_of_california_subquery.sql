-- Retrieve the state_id for California from the states table
SET @state_id := (SELECT id FROM states WHERE name = 'California');

-- List all the cities of California
SELECT * FROM cities WHERE state_id = @state_id ORDER BY id ASC;

