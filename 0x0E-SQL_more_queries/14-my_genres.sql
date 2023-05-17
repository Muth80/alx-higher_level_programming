-- Select the genre name from the tv_genres table
SELECT tv_genres.name

-- Join the tv_shows, tv_show_genres, and tv_genres tables
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
JOIN tv_genres ON tv_show_genres.tv_genre_id = tv_genres.id

-- Filter the records where the title is 'Dexter'
WHERE tv_shows.title = 'Dexter'

-- Sort the results in ascending order by genre name
ORDER BY tv_genres.name ASC;

