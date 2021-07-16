-- Task 14: My genres
-- Use hbtn_0d_tvshows to list all genres of the show Dexter
SELECT tvg.name
FROM tv_genres tvg
LEFT JOIN tv_show_genres tvsg
ON tvsg.genre_id = tvg.id
JOIN tv_shows tvs
ON tvs.id = tvsg.show_id
WHERE tvs.title = 'Dexter'
ORDER BY tvg.name ASC;
