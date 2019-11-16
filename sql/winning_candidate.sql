SELECT c.name FROM Candidate as c
INNER JOIN
(SELECT CandidateId, COUNT(CandidateId) AS ct FROM Vote
GROUP BY CandidateId
ORDER BY ct DESC LIMIT 1) AS t
ON c.id = t.CandidateId;