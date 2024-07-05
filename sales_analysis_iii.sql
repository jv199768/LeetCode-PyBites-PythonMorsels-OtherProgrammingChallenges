# Write your MySQL query statement below
# Write your MySQL query statement below

Select product_id, product_name as product_name
From(
Select Product.product_id, product_name,sale_date
From Product left join Sales on Product.product_id = Sales.product_id
Group by Product.product_id
Having sale_date between '2019-01-01' and '2019-03-31') as product_name
