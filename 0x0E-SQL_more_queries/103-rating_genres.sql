-- Select the name of the genres and the sum of ratings
SELECT tv_genres.name, SUM(tv_show_ratings.rating) AS rating_sum

-- Join the tv_genres, tv_show_genres, and tv_show_ratings tables
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.tv_genre_id
JOIN tv_show_ratings ON tv_show_genres.tv_show_id = tv_show_ratings.tv_show_id

-- Group the records by genre name
GROUP BY tv_genres.name

-- Sort the results in descending order by rating sum
ORDER BY rating_sum DESC;
