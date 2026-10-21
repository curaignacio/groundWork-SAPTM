Create Purchase Order and Review the Freight Unit

Create Purchase Order and Review the Freight Unit

Explanation

## Screenshot

1. The search term
## CREATE
PURCHASE was
entered to search for
available apps
around purchase
order creation.

Choose Create
Purchase Order -
Advanced to
continue.

2. The supplier data
and organizational
data were already
entered for your
convenience.

Expand the item
overview to enter the
item details next.

Check the item
details already
entered for youre
convenience.

For the purpose of
this demonstration,
see the material, the
quantity, the delivery
date and the plant
maintained.

Choose Next to
continue.

1


Create Purchase Order and Review the Freight Unit

Explanation

Screenshot

3. You want to
receive an inbound
delivery for further
processing in
transportation
management.

Choose Inbound
Delivery from the
confirmation control
value list to proceed.

Note that purchase
order 4500000069
has a type that allows
integration with
transportation
management.

Choose Next to
continue.

4. Choose the Order
Integration Worklist
app to proceed.

2


Create Purchase Order and Review the Freight Unit

Explanation

## Screenshot

5. Choose freight unit
5105, which was
created for the
previously entered
purchase order, to
proceed.

Note, that freight unit
5105 was created
based on the freight
unit building rule
FUBR_S4TM1.

Choose Next to
continue.

The details entered in
the purchase order fill
in the source and
destination locations,
the dates at the
destination, the
materials, and the
quantities in the
freight unit.

Click Next to
continue.

3


Create Purchase Order and Review the Freight Unit

Explanation

## Screenshot

6. Choose Document
Flow to proceed.

The document flow
can be reviewed to
trace the complete
sequence of related
documents.

When a subsequent
document, like a
freight unit, is created
based on a preceding
document, such as a
purchase order, the
system generates a
document flow. This
document flow shows
the entire sequence
of related documents
and their statuses,
indicating whether
they are completed,
open, in process, or
in another state.

This concludes the
simulation.

4


Review Freight Unit Building Rules

Review Freight Unit Building Rules

Explanation

## Screenshot

1. Choose the app
Display Freight Unit
Building Rule to
proceed.

2. The freight unit
building rule
FUBR_S4TM1 was
already selected for
your convenience.

 Choose Continue.

## The system
considers the Freight
Unit Building Rule
(FUBR) when
creating and editing
freight units.

The FUBR specifies
which type of
document will be
generated. Users can
either enter a
document type
directly or set a

1


Review Freight Unit Building Rules

Explanation

Screenshot

condition to
determine the
appropriate
document type.

Choose Next to
continue.

In the FUB rule, the
method for
consolidating freight
units is defined
through several
strategies known as
FUB strategies:

•  Consolidate as

Much as
Possible: The
system groups
items from
various
business
documents into
as many freight
units as
possible

•  Consolidate per

Item: The
system
generates one
freight unit for
each item in a
business
document

•  Consolidate per

## Request
(Compatible
Parts): The
system
consolidates all
items within a

2


Review Freight Unit Building Rules

Explanation

Screenshot

business
document into a
single freight
unit.

This concludes the
simulation.

3


Review Package Building

Review Package Building

Explanation

## Screenshot

1. Choose the Create
Sales Orders - VA01
app as part of the
Sales Document
group.

2. The sales order
type and the
organizational data
were already entered
for your
convenience.

Choose Continue to
proceed.

3. Sales order header
data as well as two
sales order items
were already entered
for your convenience.

Choose Save to
proceed.

1


Review Package Building

Explanation

## Screenshot

4. Note the sales
order number
displayed at the
bottom of the screen.

Choose Back to
return to the home
screen.

5. Choose the Order
Integration - Worklist
app as part of the
Logistics Integration
group.

6. Choose the freight
unit number 5110
associated with the
sales order 381.

2


Review Package Building

Explanation

## Screenshot

7. Choose in the area
below the scroll bar
to scroll down.

8. In the Item
Hierarchy, you can
observe the results of
the automatic
package-building
process.

Instead of seeing 100
pieces of material
TM-MAT-P1 entered
into the sales order,
you will notice
several packages,
each weighing less
than 500 kg, that
have been created by
the automatic
packaging logic.

Scroll up by choosing
the scroll button.

3


Review Package Building

Explanation

## Screenshot

9. Choose the freight
unit building rule
FUBR-PB-00 to
explore the
configuration for
package building
next.

A unified package
building profile
assigned to the
freight unit building
rule manages the
automatic logic for
building packages.

This concludes this
simulation.

4
