-- Task 17: Not my genre
-- Use hbtn_0d_tvshows to list all genres not linked to the show Dexter
SELECT tvg.name
FROM tv_genres tvg
LEFT JOIN tv_show_genres tvsg
ON tvsg.genre_id = tvg.id
JOIN tv_shows tvs
ON tvs.id = tvsg.show_id
WHERE tvg.name NOT IN (
	SELECT tvg.name
	FROM tv_genres tvg
	INNER JOIN tv_show_genres tvsg
	ON tvsg.genre_id = tvg.id
	INNER JOIN tv_shows tvs
	ON tvs.id = tvsg.show_id
	WHERE tvs.title = 'Dexter')
GROUP BY tvg.name
ORDER BY tvg.name ASC;
