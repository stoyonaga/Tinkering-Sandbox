# Introduction

In this chapter, we will be learning how to write queries. 
In the most basic sense, you will be covering how to initially translate our basic operations of relational algebra into SQL.

**Note:** Please refer to the recitation notes for the more detailed notes. This file is simply being provided as a reference to the main lesson.

# Simple Queries

The most basic kind of query in SQL consists of three chained clauses:
```sql
select attribute(s)
from relation_R
where condition; 
```

Do note that the **where condition** is optional!

In effect, what we are doing is simply selecting certain tuples from R, and then projecting a list of attributes that is specified in our select clause. 
In the case where you are given a select-from-where clause, it is sometimes easier to read it in the following order:
1. From
2. Where
3. Select

# Query Conditioning 

As a helpful note, SQL uses some rather unintuitive conditionals. Some examples have been provided below.
* = is used in lieu of == 
* <> is used in lieu of != 
* || is used for string concatenation

We can also use the concept of Regular Expressions that was taught in your **Theory of Computation** course!
Using the notion of **str like pattern**, we can use:
* % to represent the, "zero or more characters" // Universal Set --> * 
* _ to represent a singular wildcard

# Renaming 
Recall, using the keyword, **as**, followed by a new attribute header in our select clause. 
```sql
select name as identifier 
from r;
```

Also, remember that we can use, **as**, to implement the concept of extended projection to our relations / views.

# Null Values 
The null value in SQL can represent three possible scenarios:
1. Value Unknown
2. Value Inapplicable 
3. Value Withheld

Please do not forget that **NULL** is not a constant. Thus, you must use the, **var is NULL** syntax to check for null. 

# Boolean Determination

Recall the following cases:
1. 1 = True 
2. 0 = False 
3. 1/2 = Unknown

Also, do note that:
1. NULL as an operand in an arithmetic operation will produce a NULL result
2. NULL as an operand in a comparison operation will produce an UNKNOWN result

If we have two operands, OP1 and OP2, which are of a boolean value, then:
1. OP1 AND OP2 = min(OP1, OP2)
2. OP1 OR OP2 = max(OP1, OP2)
3. NOT OP1 = 1 - value(OP2)

The value in (3) refers to its String to float mapping that is listed above.

# SQL Sorting 

To get the output in sorted order, we may add the following clause, **order by attr(s)...;**. By default, it has the value of ascending (ASC). You can also set it to descending (DESC) at will.

# Additional Homework 

1. Complete the blank table of boolean determination / consequences, and doublecheck your answers in PostgreSQL.

2. Given the characters database, determine what the output will be if we run the following query:

```sql
select * 
from characters 
where rating > 7 or rating <= 7
order by rating;
```

3. Given the character database, determine what the output will be run if we run the following query:
```sql
select name, rating 
from characters
where affiliation like 'Orange %'
order by name;
```

4. Given the characters database, determine what the output will be if we run the following query:
```sql
select name, affiliation
from characters 
where name like 'B%B';
```

5. Write a query for our characters database that returns all of the users with a name ending with, 'le'. Additionally, they must have a valid rating attribute that has been pre-set.

6. Implement all of the recitation examples in PostgreSQL, and test them on your local environment. One of the queries can be optimized. Find which one it is and then provide the more computationally-efficient alternative query.  
