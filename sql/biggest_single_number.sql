# Write your MySQL query statement below
SELECT max(num) AS num FROM
(SELECT num from my_numbers
GROUP BY num
HAVING count(num) = 1) AS temp;
