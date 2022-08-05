# Introduction

We use the concept of **foreign keys** to implement the concept of **referential integrity** from our E/R diagrams.

# Implementation Standards

In SQL, we may declare a list of attributes of one relation to be a foreign key, referencing some attributes of another relation.
The implication of using two keys is that:

1. The referenced attributes of the second relation must explicitly be declared as keys (either primary, or unique.)
2. Values of the foreign key appearing in the first relation must also appear in the referenced attributes of some given tuple.

# SQL Implementation

We can declare a single-attribute foreign key in SQL by using the following code:
```sql
foreign key(attr_1, attr_2, ...) references relation(attr_a, attr_b, ...)
```

# Assignment Notes

You now have all the pre-requisite information to complete A1 and A2!! 
However, you will need to also know how to populate your relations with tuples. It also helps to know how to edit tuples, and remove them, just for future reference!

## Tuple Insertion

In SQL, we can insert tuples into our database / relations by using the following code:

```sql
insert into R(...) values (...), ... ,(...);
```
## Tuple Removal

In SQL, we can remove tuples from our database / relations by using the following code: 

```sql
delete from R where condition_boolean;
```
## Tuple Updating 

In SQL, we can update tuples from our database / relations by using the following code:


```sql
update R set value_assignments where condition_boolean;
```
