-- script that lists all genres and displays the number of shows linked to each
SELECT g.name AS genre, COUNT(sg.show_id) AS number_of_shows
FROM tv_show_genres AS sg
JOIN tv_genres AS g
ON sg.genre_id = g.id
GROUP BY g.id
ORDER BY number_of_shows DESC;
