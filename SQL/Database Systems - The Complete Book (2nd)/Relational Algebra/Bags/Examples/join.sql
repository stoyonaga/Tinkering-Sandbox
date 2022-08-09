-- Left Outer Join
select u.a, u.b, u.c, v.d
from u left outer join v
on u.b = v.b and u.c = v.c;

-- Right Outer Join
select u.a, v.b, v.c, v.d 
from u right outer join v 
on u.b = v.b and u.c = v.c;

-- Full Outer Join Example
select u.a, u.b, v.b, u.c, v.c, v.d
from u full outer join v 
on u.b = v.b and u.c = v.c;

-- Natural Join 
select a, b, c, d
from u natural join v;
