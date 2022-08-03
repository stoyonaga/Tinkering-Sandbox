# Introduction

- In the context of this course, we will only be concerning ourselves with the **relational model**, which is a database that consists of one or more **relations (tables)**.
- In our table, each row represents a separate entry into our database. The columns represent the properties of the relation. 

# Prerequisite Terminology

1. **Attributes** represent the header of a relations column. That is, the aforementioned properties of the relation. 
2. **Schemas** can be thought of as a blueprint for a relation. They are denoted by writing the name of a relation followed by a parenthesized, comma separated list of its attributes.
3. A **relational database** is the set of all the schemas for the relations of a database. It is also sometimes referred to as a **database schema**.
4. A **tuple** represents a row entry of a relation. Do note that we do not consider the header row as a tuple.
5. A **domain**, similar to mathematics, is used to represent the range of values that an attribute may take. It requires that each component of a tuple be **atomic**. This means that each component must be of an elementary type. The domain can be illustrated in a schema by following each attribute by a semicolon and its elementary type.
6. We will say that a set of attributes forms a **key** for a relation if we do not allow any two tuples in the relation instance to have the same vajues in all the attributes of the key. It must pertain to all possible instances of the relation.

# SQL Syntax Introduction

We can create a relation in SQL, by using the following code template:
```sql
create table table_name(
 column_header1 attr_type,
 column_header2 attr_type,
 column_header3 attr_type,
 column_header4 attr_type
);
```

We can delete a relation in our database, by using the following SQL command:
```sql
drop table table_name;
```

We can alter the properties of a relation, by using the following SQL commands:
**1. Adding a New Column**
```sql
alter table relation_name add attr_id datatype;
```
**2. Removing an Existing Column**
```sql
alter table relation_name drop attr_id;
```

**Note:** If we want to assign a default value to our new column, rather than having it set to NULL, we can use the following SQL command:
```sql
alter table relation_name add attr_id datatype default default_value;
```

# Key Declaration

**1. Primary Key**
 ```sql
 primary key(-----)
 ```
**2. Unique Key**
```sql
unique(-----)
```

If a primary key is used, then all attributes in the key definition cannot be allowed to have a value of NULL in their components.

