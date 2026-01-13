-- script that lists all genres by their rating
SELECT g.name, SUM(r.rate) AS rating
FROM tv_genres AS g
INNER JOIN tv_show_genres AS sg 
ON sg.genre_id = g.id
INNER JOIN tv_shows AS s 
ON s.id = sg.show_id
INNER JOIN tv_show_ratings AS r 
ON r.show_id = s.id;
