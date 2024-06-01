CREATE FUNCTION getNthHighestSalary(nHighestSalary INT) RETURNS INT
BEGIN
    SET nHighestSalary = nHighestSalary - 1;
    RETURN(
        SELECT DISTINCT salary
        FROM employee
        ORDER BY salary DESC
        LIMIT 1
        OFFSET nHighestSalary
        );
END
