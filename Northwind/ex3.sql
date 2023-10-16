SELECT o.OrderID, o.OrderDate
FROM Orders AS o
INNER JOIN Employees AS e ON o.EmployeeID = e.EmployeeID
INNER JOIN EmployeeTerritories AS et ON e.EmployeeID = et.EmployeeID
INNER JOIN Territories AS t ON et.TerritoryID = t.TerritoryID
WHERE t.TerritoryDescription = 'Chicago';