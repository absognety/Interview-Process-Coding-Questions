Consider the below employee table where ManagerID is mapped to each EmployeeID:

Input:
| EmployeeID | EmployeeName | ManagerID |
|------------|--------------|-----------|
|    400     |    A1        |    null   |
|    401     |    A2        |    400    |
|    500     |    A3        |    401    |
|    501     |    A4        |    401    |
|    502     |    A5        |    501    |

Write the SQL query that identifies the level of each manager as mentioned in the below output:

| EmployeeID | EmployeeName | ManagerID | Level |
|------------|--------------|-----------|-------|
|   400      |   A1         |   null    |   0   |
|   401      |   A2         |   400     |   1   |
|   500      |   A3         |   401     |   2   | 
|   501      |   A4         |   401     |   2   |
|   502      |   A5         |   501     |   3   |


### Solution:
               400
                  |
              401 (depth from 400 = 1)
              /   \
          500  501 (depth from 400 = 2)
                         \
                          502 (depth from 400 = 3)

400 -> 401  
401 -> 500, 501  
501 -> 502  

**What we want to do here is use RECURSIVE CTE to traverse the tree in SQL and compute the depth at every level.**
