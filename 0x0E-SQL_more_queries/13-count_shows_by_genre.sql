-- Script that lists all genres
-- and displays number of shows linked
SELECT tv_g.name AS genre, COUNT(show_id) AS number_of_shows FROM tv_genres tv_g
INNER JOIN tv_show_genres tvs_g
ON tv_g.id = tvs_g.genre_id
GROUP BY tvs_g.genre_id
ORDER BY number_of_shows DESC;
