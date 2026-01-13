-- script that lists all shows contained in hbtn_0d_tvshows
SELECT sh.title, g.genre_id
FROM tv_shows AS sh
JOIN tv_show_genres AS g
ON sh.id = g.tv_show_id
ORDER BY sh.title ASC, g.genre_id ASC;
