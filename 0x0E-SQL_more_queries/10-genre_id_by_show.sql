-- Task 10: Genre ID by show
-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT tvs.title, tvsg.genre_id
FROM tv_show_genres tvsg
JOIN tv_shows tvs
ON tvs.id = tvsg.show_id
JOIN tv_genres tvg
ON tvg.id = tvsg.genre_id
ORDER BY tvs.title, tvsg.genre_id ASC;
