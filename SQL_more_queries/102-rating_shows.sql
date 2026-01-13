-- script that list all shows by their rating
SELECT s.title, SUM(r.rate) AS rating
FROM tv_shows AS t
INNER JOIN tv_show_ratings AS r
ON s.id = r.show_id
GROUP BY s.title
ORDER BY rating DESC;
