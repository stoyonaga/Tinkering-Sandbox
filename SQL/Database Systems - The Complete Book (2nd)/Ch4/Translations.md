# Introduction

In this section, we will review how to convert E/R diagrams to Relational designs. This will be another accelerated review, so please refer to the lecture slides and textbook for further brevity and information.

1. **Non-Weak Entity Sets to Relations**
- Simply create another relation of the same name, and with the same set of attributes. 
- Do note that this relation will not have any indication of relationships in which it presently participates in the E/R diagram.

2. **Non-Weak Relationships to Relations**
- For each entity set that is involved in the relationship, take its corresponding key attributes as part of the schema of the relation, R. These will serve as the relations key set as well.
- If the relationship also has its own attributes, we must include this in the schema. Recall that we may be able to remove the attribute on the relationship, if we so desire to.

3. **Weak Entity Sets to Relations**
- We must include the attributes of the weak entity set, in addition to the key attributes of the supporting entity sets. 
- Do note that a supporting relationship from the weak entity set does not need to be converted into a relation, unless it has its own attribute.

4. **Subclass Entity Sets to Relations**
- For each entity set in the hierarchy (in this course, we only allow for one subclass...), create a relation that includes the key attributes from the parent (root), and any attributes that it personally uses.



# Combining Relations

Recall in the Prerequisites section where the issue around design principles was addressed. 
In some situations, which will be described below, the advantages of combining relations will produce greater efficiency in queries. That is, we work to optimize our queries in the future.

We will consider combining relationships in the case where we have an entity set E, which participates in a many-one relationship, R, with another relation, F.
We can combine them into one relation, producing a schema, which contains:
- All the attributes of E 
- The key attributes of F, which are now classified as regular attributes 
- Any attributes which belong to R.
