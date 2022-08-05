# Introduction

This folder contains some examples how to convert very basic entity-relationship diagrams into relational designs.
All of the diagrams have been generated through the use of [draw.io](https://app.diagrams.net/)

Effectively, in each example, we are:
1. Providing the original entity-relationship diagram
2. Translating the entity-relationship diagram into an appropriate database schema
3. Taking the database schema, and then systematically building the database by translating each component into an appropriate relation
4. Reviewing the database, and making any further optimizations (i.e., Combining the relations where applicable)
5. Generating tuples to insert into our database for testing reasons
6. Generating a drop.sql script, to clear our database after we are done tinkering with it!
