SELECT p1.product_id, 
       p1.new_price AS price 
FROM   products p1 
WHERE  p1.change_date <= '2019-08-16' 
       AND (product_id, Datediff('2019-08-16', p1.change_date)) 
       IN (
            SELECT product_id, 
                   Min(Datediff('2019-08-16', change_date)) 
            FROM   products 
            WHERE  change_date <= '2019-08-16' 
            GROUP BY product_id
          )
UNION
SELECT product_id,
       10 AS price
FROM   products
GROUP  BY product_id
HAVING Min(change_date) > '2019-08-16'
ORDER  BY price DESC 
