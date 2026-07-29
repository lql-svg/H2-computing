select competitor.name, sum(scores.score),
total(scores.score) > 250
from competitor, scores
where competitor.id = scores.id
group by competitor.id, competitor.name
order by sum(scores.score) desc