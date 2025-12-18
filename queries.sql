
-- create
CREATE TABLE Student (
  name varchar(15),
  continent varchar(10)
);

-- insert
INSERT INTO Student (name, continent) VALUES ('Jack', 'America');
INSERT INTO Student (name, continent) VALUES ('Pascal', 'Europe');
INSERT INTO Student (name, continent) VALUES('Xi', 'Asia'); 
INSERT INTO Student (name, continent) VALUES ('Jane', 'America'); 
-- fetch 
WITH
  StudentWithIdInContinent AS (
    SELECT
      *,
      ROW_NUMBER() OVER(PARTITION BY continent ORDER BY name) AS id
    FROM Student
  )
SELECT
  MAX(CASE WHEN continent = 'America' THEN name END) AS America,
  MAX(CASE WHEN continent = 'Asia' THEN name END) AS Asia,
  MAX(CASE WHEN continent = 'Europe' THEN name END) AS Europe,
  id
FROM StudentWithIdInContinent
GROUP BY id;
