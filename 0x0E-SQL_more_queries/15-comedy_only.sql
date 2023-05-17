-- Select the title of the shows from the tv_shows table
SELECT tv_shows.title

-- Join the tv_shows, tv_show_genres, and tv_genres tables
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
JOIN tv_genres ON tv_show_genres.tv_genre_id = tv_genres.id

-- Filter the records where the genre name is 'Comedy'
WHERE tv_genres.name = 'Comedy'

-- Sort the results in ascending order by show title
ORDER BY tv_shows.title ASC;

