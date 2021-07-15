-- Task 12: No genre
-- Lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT tvs.title, tvsg.genre_id
FROM tv_show_genres tvsg
RIGHT JOIN tv_shows tvs
ON tvs.id = tvsg.show_id
WHERE tvsg.genre_id IS NULL
ORDER BY tvs.title ASC, tvsg.genre_id ASC;
