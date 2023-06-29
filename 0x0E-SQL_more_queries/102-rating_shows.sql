-- Select the title of the shows and the sum of ratings
SELECT tv_shows.title, SUM(tv_show_ratings.rating) AS rating_sum

-- Join the tv_shows and tv_show_ratings tables
FROM tv_shows
JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.tv_show_id

-- Group the records by show title
GROUP BY tv_shows.title

-- Sort the results in descending order by rating sum
ORDER BY rating_sum DESC;
