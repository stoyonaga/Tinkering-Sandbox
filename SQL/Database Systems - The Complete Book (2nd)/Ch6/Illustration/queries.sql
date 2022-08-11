-- Q5 Solution
select * 
from characters
where name like '%le' and not rating is null
order by name asc;
