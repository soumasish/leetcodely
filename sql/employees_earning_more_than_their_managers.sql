SELECT Employee FROM
(SELECT e1.Name AS Employee, e1.Salary, e1.ManagerId, e2.Salary AS ManagerSalary
FROM Employee AS e1, Employee AS e2
WHERE e1.ManagerId = e2.Id) AS T
WHERE T.Salary > T.ManagerSalary;