-- Task 15: Only Comedy
-- List all Comedy shows in hbtn_0d_tvshows database
SELECT tvs.title
FROM tv_genres tvg
LEFT JOIN tv_show_genres tvsg
ON tvsg.genre_id = tvg.id
JOIN tv_shows tvs
ON tvs.id = tvsg.show_id
WHERE tvg.name = 'Comedy'
ORDER BY tvs.title ASC;
