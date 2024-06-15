# Write your MySQL query statement below

select requester_id as id,
       (select count(*) from RequestAccepted
            where id=accepter_id or id=requester_id) as num
from RequestAccepted
group by accepter_id
order by num desc limit 1
