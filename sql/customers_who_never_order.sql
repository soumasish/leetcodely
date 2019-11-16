SELECT c.name AS Customers from Customers as c
LEFT JOIN orders AS o ON c.Id = o.CustomerId
WHERE o.id is NULL;