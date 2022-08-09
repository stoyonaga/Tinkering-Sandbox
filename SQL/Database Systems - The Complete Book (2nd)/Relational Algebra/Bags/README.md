# Introduction 
Recall that in the former recitation, we covered Relational Operations on Sets. In this section, we will extend our notion of relational algebra to bags (multisets).

# Why Should We Use Bags?
1. Some operations (i.e., Union, Projection) are considerably more optimized, when we work with bags. This is because we do not need to compare each tuple, multiple times when doing basic operations.
2. Bags are required if we want to be able to calculate expected answers in terms of aggregation operations.

# Bag Operations 
Please refer to the recitation slides for a more detailed explanation of the operations. 
So far, you should be familiar with the following operations.

* Bag Union **(n + m)**
* Bag Intersection **(min(n, m))**
* Bag Difference **(max(0, n - m))**
* Projection
* Selection
* Products
* Joins

# Extended (Bag-Only) Operations

* **Duplicate Elimination** 
  * Effectively, this turns a bag into a set by eliminating any duplicates of each tuple. 
  * One could rewrite this as a special case of the grouping operator. 
* **Aggregation Operators**
  * SUM 
  * AVG
  * MIN: On strings, this will return the lexicographically first value.
  * MAX: On strings, this will return the lexicographically last value.
  * COUNT
* **Grouping**
  * Groups tuples according to their value in one or more attributes. After doing so, aggregation can then be applied to columns, within each group.   
* **Extended Projection**
  * Allows one to compute computations of various kinds, which will produce new columns.    
* **Sorting**
  * Turns a relation into a sorted list of tuples.
  * Execution of most queries is optimized if we initially sort the relation.
* **Outer Join**
  * A variant of our set-based join. It avoids the loss of dangling tuples.
    * **Left Outer Join**: Only the dangling tuples on the left argument are added to our natural join.
    * **Right Outer Join**: Only the dangling tuples of the right argument are added to our natural join.

# Additional Exercises

- No additional exercises outside of the recitation are available at this time. However, if you wish, you may:
  - Implement the examples into PostgreSQL to familiarize yourself with the software environment, and doublecheck your Join questions by implementing the database and queries.
  - Determine which laws are shared between the relational algebra variants
  - Determine which laws are not shared between the relational algebra variants.
  - Provide a rationale on which operations run faster, slower, or the same for relational algebra, using bags versus the set implementation.
  - Determine the best and worst-case running time of the operations implementation.
