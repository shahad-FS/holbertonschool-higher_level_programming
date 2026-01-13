-- script that list all genres not linked to the show 'Dexter'
SELECT g.name
FROM tv_genres AS g
LEFT JOIN tv_show_genres AS sg
ON g.id = sg.genre_id
AND sg.show_id = (
	SELECT id
	FROM tv_shows
	WHERE title = 'Dexter'
)
WHERE sg.show_id IS NULL
ORDER BY g.name ASC;
