-- Oracle solution

WITH RecursiveCTE (lvl, ManagerID, EmployeeID) AS (
   SELECT 1 AS lvl, ManagerID, EmployeeID
   FROM employees
   WHERE ManagerID IS NULL
   UNION ALL
   SELECT lvl + 1, employees.ManagerID, employees.EmployeeID
   FROM employees
   JOIN cte
     ON employees.ManagerID = cte.EmployeeID
)
SELECT *
FROM cte;
