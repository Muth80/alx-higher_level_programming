-- Select the title of the shows from the tv_shows table
SELECT tv_shows.title
FROM tv_shows

-- Filter out shows that have the genre Comedy
WHERE tv_shows.id NOT IN (
    -- Subquery to select the show IDs with the genre Comedy
    SELECT tv_show_genres.tv_show_id
    FROM tv_show_genres
    JOIN tv_genres ON tv_show_genres.tv_genre_id = tv_genres.id
    WHERE tv_genres.name = 'Comedy'
)

-- Sort the results in ascending order by show title
ORDER BY tv_shows.title ASC;
