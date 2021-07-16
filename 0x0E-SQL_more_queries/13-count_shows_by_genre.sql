-- Task 13: Number of shows by genre
-- Lists all genres from hbtn_0d_tvshows and display the number of shows linked to each
SELECT tvg.name AS "genre", COUNT(tvs.title) AS "number_of_shows"
FROM tv_show_genres tvsg
LEFT JOIN tv_genres tvg
ON tvg.id = tvsg.genre_id
JOIN tv_shows tvs
ON tvs.id = tvsg.show_id
GROUP BY tvg.name
ORDER BY COUNT(tvs.title) DESC
