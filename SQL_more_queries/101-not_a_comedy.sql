-- script that lists all shows without the genre 'Comedy'
SELECT s.title
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS sg
ON s.id = sg.show_id
AND sg.genre_id = (
	SELECT id
	FROM tv_genres
	WHERE name = 'Comedy'
)
WHERE sg.genre_id IS NULL
ORDER BY s.title ASC;
