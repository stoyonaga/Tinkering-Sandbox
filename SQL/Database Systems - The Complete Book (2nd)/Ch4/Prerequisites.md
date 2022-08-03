# Introduction

In this section, we will look at how the structure of a database is visually represented.
That is, our main focus will be on learning how to develop **entity-relationship** diagrams, and then converting them into relational  designs.  

**Note:** This is an accelerated review of the prerequisites of this chapter. To understand the entire picture, refer to your lecture slides and the relevant textbook reading(s).

# Useful Resources
- [draw.io](https://app.diagrams.net/) is a great tool for creating your E/R diagrams! It has a nice and clean UI, and is easy to save your work and edit again.
- [LibreOffice Draw](https://www.libreoffice.org/) is another great drawing tool to generate your E/R diagrams. 

# Principal Elements
1. **Entity:** Think of this as an abstract object, which can have attributes. A collection of these abstract objects forms an **entity set**. They are represented by a rectangle in our entity-relationship diagram.
2. **Attributes:** Think of these as properties of an entity-set. Thet are represented by ovals.
3. **Relationships:** A relationship is used to make connections / association between two or more entity sets. Really, it mirrors what you would expect in real life! It is represented by a diamond.
4. **Edges** are used to connect an entity set to its attributes, and also connect a relationship to its entity sets. There's a little more complexity to this, but we will discuss in the future. 

# Multiplicity of (Binary) E/R Relationships
1. Many-One: i.e., A person has a favourite tv show.
2. One-One: i.e., An electronics company has a best-selling product.
3. Many-Many: i.e., A person has friends.

# Subclasses
- Synonymous with what you would expect with the concept of inheritance in programming.
- The parent class connects to its subclasses by using the, "isa" relationship, rather than our traditional diamond one. 

# Design Principles
1. Faithfulness
2. Avoiding Redundancy
3. Simplicity 
4. Choosing the Right Relationships 
5. Picking the Right Kind of Element

# Constraints in our E/R Model
**1. Key Specifics**
- Every entity set must have a key. We will stick to the convention of initializing a primary key.
- In an inheritance situation, the parent (root) must have all the attributes needed for a key that is sufficient in all of its subclases.

**2. Degree Constraints**
- Refer to the textbook for more information.

# Weak Entity Sets 
A weak entity set is used when it requires help from other entity sets, which are connected by supporting relationshps. 
- If an entity set is weak, it is represented by a double-border rectangle.
- If a relationship is supporting, it is represented by a double-border diamond with a rounded arrow.

# Key Concepts for Review
1. How would we remove attributes from relationships, while also providing an equivalent database schema?
2. How would we convert a multiway relationship into a set of binary many-one relationships?
3. Why are the design principles important? Explain the consequences of failing to abide by each rule.
4. What are some real-world applications where a weak entity set may be useful and/or applicable? Implement the database schema for your example and provide the source code. That is, write a main.sql and drop.sql script for PostgreSQL.
