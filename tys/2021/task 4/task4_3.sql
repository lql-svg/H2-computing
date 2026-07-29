select competitor.name, round(avg(scores.score), 2)
from competitor, scores
where competitor.id = scores.id
group by competitor.id, competitor.name
order by competitor.name asc