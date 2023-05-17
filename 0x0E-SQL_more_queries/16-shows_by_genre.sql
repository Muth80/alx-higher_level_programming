-- Select the title of the shows and the genre name from the tv_shows and tv_genres tables
SELECT tv_shows.title, tv_genres.name

-- Left join the tv_shows, tv_show_genres, and tv_genres tables
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
LEFT JOIN tv_genres ON tv_show_genres.tv_genre_id = tv_genres.id

-- Sort the results in ascending order by show title and genre name
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
