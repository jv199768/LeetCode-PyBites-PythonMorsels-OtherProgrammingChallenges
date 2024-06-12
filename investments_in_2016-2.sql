# Write your MySQL query statement 
WITH tab AS (
    SELECT
        TIV_2016,
        COUNT(*) OVER (PARTITION BY TIV_2015) AS tiv_freq,
        COUNT(*) OVER (PARTITION BY LAT, LON) AS place_freq
    FROM
        insurance)

SELECT
    ROUND(SUM(TIV_2016), 2) AS TIV_2016
FROM
    tab
WHERE
    tiv_freq > 1 AND
    place_freq = 1
