SELECT product_id
        , 10 AS price
FROM products
GROUP BY product_id
HAVING MIN(change_date) >= '2019-08-16' AND MIN(price) >- 10

UNION

SELECT product_id
        , new_price as price
FROM (
    SELECT *
            , ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY change_date DESC) as new_date
    FROM products
    WHERE change_date <= '2019-08-16'
) as t
WHERE new_date = 1

ORDER BY product_id ASC;
