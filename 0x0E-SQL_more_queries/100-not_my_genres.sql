-- Select the genre name from the tv_genres table
SELECT tv_genres.name
FROM tv_genres

-- Filter out genres that are linked to the show Dexter
WHERE tv_genres.name NOT IN (
    -- Subquery to select genres linked to Dexter
    SELECT tv_genres.name
    FROM tv_shows
    JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
    JOIN tv_genres ON tv_show_genres.tv_genre_id = tv_genres.id
    WHERE tv_shows.title = 'Dexter'
)

-- Sort the results in ascending order by genre name
ORDER BY tv_genres.name ASC;
