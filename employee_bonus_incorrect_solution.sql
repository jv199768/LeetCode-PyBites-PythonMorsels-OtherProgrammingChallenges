# Write your MySQL query statement below
SELECT
name, bonus
FROM Bonus b
INNER JOIN Employee e
ON b.empId = e.empId
WHERE bonus < 1000 or bonus is NULL
