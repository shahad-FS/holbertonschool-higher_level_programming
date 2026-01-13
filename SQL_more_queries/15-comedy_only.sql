-- script that lists all Comedy shows
SELECT s.title
FROM tv_shows AS s
JOIN tv_show_genres AS sg
ON s.id = sg.show_id
JOIN tv_genres AS g
ON sg.genre_id = g.id
WHERE g.name = 'Comedy'
ORDER BY s.title ASC;
