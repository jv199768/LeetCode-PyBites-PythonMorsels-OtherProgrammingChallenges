# Write your MySQL query statement below
WITH
  EmployeesWithMaxSalaryInDepartment AS (
    SELECT
      Department.name AS department_name,
      Employee.name AS employee_name,
      Employee.salary,
      MAX(Employee.salary) OVER(
        PARTITION BY Employee.departmentId
      ) AS max_salary
    FROM Employee
    LEFT JOIN Department
      ON (Employee.departmentId = Department.id)
  )
SELECT
  department_name AS Department,
  employee_name AS Employee,
  salary AS Salary
FROM EmployeesWithMaxSalaryInDepartment
WHERE salary = max_salary;
