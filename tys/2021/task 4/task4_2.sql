select competitor.name, scores.score
from competitor, scores
where competitor.id = scores.id
and scores.round = 1
order by scores.score desc