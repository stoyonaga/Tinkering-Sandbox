# Queries Involving Multiple Relations

In SQL, we can couple relations in one query. We simply list the relations in the FROM clause. 
In the select and where clause, we can then refer to the attributes of any of these relations through dot notation. 

# Subqueries 

We will define a subquery as a query, which is part of another query. 
In one such example, a subquery can take on the role ofa scalar value in the WHERE clause.

# Condition Operations on Relations 

There are multiple operations that we can apply to a relation, returning a boolean result. We will focus on:

1. **EXISTS R**
    - This operator will return true if and only if the number of tuples in the relation is greater than 0.   
2. **S IN R**
    - This operator will return true if and only if the tuple, S, is in the relation R.
3. **S ? ALL R**
    - **Note:** The ? is a placeholder for any of the supported SQL comparison operators.
    - his operator will return true if and only if the conditional operator is true for all tuples in R.
4. **S * ANY R**
    - **Note:** The ? is a placeholder for any of the supported SQL comparison operators.
    - This operator will return true if and only if the conditional operator is true for at least one tuple in R.

# The General Time Complexity for Queries
- Single-Relation Query = $O(n)$
- Multi-Relation Query = $O(n^2)$

# Aggregation Operators 
- We will only consider operations that act on a relation as a whole. 
- An aggregation operator applies to entire columns of a table, thus producing a single result.
- The aggregation operators that you will be expected to know are:
    1. SUM
    2. AVG
    3. MIN
    4. MAX
    5. COUNT 

# Grouping Aggregation, and NULLS
When dealing with NULL values, SQL has a set of particular rules that you should be aware of. They are listed below:
1. The value NULL is ignored in our aggregation operators.
2. NULL is treated as a normal value when we form groups from attributes.
3. An aggregation that is applied over an empty relation produces NULL, unless we use COUNT. In the latter case, it will return a value of integer 0.

# Order of Clauses in SQL Queries 
1. SELECT
2. FROM
3. WHERE
4. GROUP BY 
5. HAVING 
6. ORDER BY 

Please remember the following rules:
- Any attribute of relations that appear in the (2) may be aggregated in the (5) clause.
- Only the attributes in (4) may be unaggregated in (1), (5).

# Additional Practice

1. Given schema.sql, write a query which returns the sum of price values for each type of item in our product database. Your query should return the following table:
```
           type            |        sum
---------------------------+--------------------
 Desktop                   |            4389.98
 Mechanical Keyboard       |             100.93
 15GB (2 * 8GB) RAM Sticks |              88.99
 Mouse Mat                 |              59.99
 Laptop                    | 2970.8100000000004
 Gaming Headset            |              49.99
 Gaming Keyboard           |              59.99
 
 (7 rows)
```

2. Given schema.sql, write a query which returns a table that contains the most expensive product.
Your query should return the following table:

```
                         name                         |  type   |  price  | rating | availability
------------------------------------------------------+---------+---------+--------+--------------
 CyberPowerPC Gamer Supreme Liquid Cooled SLC10800CPG | Desktop | 2889.99 |    3.5 |
(1 row)
```

3. Given schema.sql, write a query which returns a table that contains the average price of each type of product.
Your query should return the following table:

```
---------------------------+-------------------
 Desktop                   |           2194.99
 Mechanical Keyboard       |            100.93
 15GB (2 * 8GB) RAM Sticks |             88.99
 Mouse Mat                 |             59.99
 Laptop                    | 990.2700000000001
 Gaming Headset            |             49.99
 Gaming Keyboard           |             59.99
(7 rows)
```

4. Given schema.sql, write a query which returns the maximum rating for each type of item in our Product database. Your query should return the following table:
```
           type            | rating
---------------------------+--------
 Mechanical Keyboard       |      4
 15GB (2 * 8GB) RAM Sticks |      4
 Laptop                    |      4
 Gaming Headset            |      4
 Desktop                   |    3.8
 Gaming Keyboard           |    3.5
 Mouse Mat                 |      3
```
