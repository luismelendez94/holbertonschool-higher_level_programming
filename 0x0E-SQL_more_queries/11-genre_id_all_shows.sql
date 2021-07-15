-- Task 11: Genre ID for all shows
-- Lists all shows contained in the database hbtn_0d_tvshows
SELECT tvs.title, tvsg.genre_id
FROM tv_show_genres tvsg
RIGHT JOIN tv_shows tvs
ON tvs.id = tvsg.show_id
ORDER BY tvs.title ASC, tvsg.genre_id ASC;
