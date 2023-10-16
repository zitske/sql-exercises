SELECT e.FirstName, e.LastName
FROM Employees AS e
INNER JOIN EmployeeTerritories AS et ON e.EmployeeID = et.EmployeeID
INNER JOIN Territories AS t ON et.TerritoryID = t.TerritoryID
WHERE t.TerritoryDescription = 'Chicago';
