1/14/26, 2:19 PM

Transportation Management (TM)

Generated on: 2026-01-14 14:19:13 GMT+0000

SAP S/4HANA | 2025 (Oct 2025)

## Public

Original content: https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2?locale=en-

US&state=PRODUCTION&version=2025.000

## Warning

This document has been generated from SAP Help Portal and is an incomplete version of the official SAP product documentation.

The information included in custom documentation may not reflect the arrangement of topics in SAP Help Portal, and may be

missing important aspects and/or correlations to other topics. For this reason, it is not for production use.

For more information, please visit https://help.sap.com/docs/disclaimer.

This is custom documentation. For more information, please visit SAP Help Portal.

1


1/14/26, 2:19 PM

## Planning

In planning, freight documents and transportation units are created on the basis of business documents, for example, forwarding

orders, from which freight units have been created, and by assigning capacities. Various constraints are taken into account, for

example, requested delivery dates.

## Integration

The component Planning of Transportation Management (TM) is integrated with the following other TM components:

## Component

## Integration Type

## Forwarding Order Management

The system creates freight units from forwarding orders. These

freight units form the basis for planning.

## Freight Order Management

Freight documents and transportation units are the result of the

planning.

## Charge Calculation

You can have the system calculate the transportation charges for

your freight orders and freight bookings.

## Master Data

You need to create the required master data as a prerequisite for

planning.

## Features

## Freight units

Planning is based on freight units. For more information, see Creation and Editing of Freight Units.

## Unified package building

Unified package building allows you to package your products. For more information, see Unified Package Building in TM.

## Profiles and settings

By defining profiles and settings, you can determine which objects are available for planning and you can influence the

planning results. For more information, see Profiles and Settings.

## Manual planning and automatic planning

Manual and automatic planning (sometimes also referred to as interactive planning) offer you a wide variety of planning

options. For more information, see Manual Planning and Automatic Planning.

## Scheduling

You can determine the start and end dates for a set of activities. For more information, see Scheduling.

## Carrier selection

You can assign a suitable carrier to your subcontractable business documents (for example, freight orders). For more

information, see Carrier Selection.

## Creation and Editing of Freight Units

This is custom documentation. For more information, please visit SAP Help Portal.

2


1/14/26, 2:19 PM
## Use

The system automatically creates freight units from the following business documents:

## Forwarding orders

Order-based transportation requirements

## Delivery-based transportation requirements

Other order-based business documents, such as sales orders or purchase orders from Sales and Distribution (SD) or

Materials Management (MM) or outbound delivery orders from Extended Warehouse Management (EWM)

Other delivery-based business documents, such as inbound and outbound deliveries

## JIT calls

The system can split and merge the product quantities of the requirements when it creates freight units based on the freight unit

building rules used.

The creation of freight units in turn affects planning. The larger the freight units are, the simpler the planning activities in VSR

optimization. If the freight units are smaller, there may well be a higher theoretical potential for optimization, but in practice,

planning in VSR optimization is made more difficult due to the higher number of freight units. To achieve the best planning result,

you are advised to aim somewhere in the middle.

  Example

You have a truck with a capacity of 20 tons. You are planning to transport 20 tons of flour in 1 kg packages. Neither extreme is

advisable here for the reasons given above. You should not create a single freight unit with a weight of 20 tons, nor should you

create 20,000 freight units with a weight of 1 kg each.

## Prerequisites

Business documents exist.

If you would like the system to automatically create freight units when business documents are saved, you have specified

this in Customizing:

In the case of forwarding orders, you have selected the checkbox for automatic freight unit building in the

forwarding order type. For more information, see Customizing for Transportation Management under  Forwarding

Order Management

## Forwarding Order

 Define Forwarding Order Types .

In the case of order-based business documents, such as sales orders or purchase orders, you have selected the

checkbox for automatic freight unit building in the logistics integration profile. For more information, see

Customizing for Transportation Management under

## Integration

 Logistics Integration

## Internal TM

## Component Integration

 Define Logistics Integration Profile for SD, MM, and LE .

If required, you have extended the standard checks that the system executes to decide whether a freight unit or

transportation unit must be rebuilt during business document maintenance. For more information, see Customizing for

Transportation Management under  Business Add-Ins (BAdIs) for Transportation Management

 Forwarding Order

## Management

## Freight Unit Building

 BAdI: Extension of Checks for Triggering FU Building from TRQ .

You have defined freight unit types in Customizing. For more information, see Customizing for Transportation

Management under  Planning

## Freight Unit

 Define Freight Unit Types .

You have defined freight unit building rules (FUB rules) and assigned freight unit types to them (see Freight Unit Building

Rule).

This is custom documentation. For more information, please visit SAP Help Portal.

3


1/14/26, 2:19 PM

Optionally, you have defined incompatibilities (see Incompatibilities).

If goods have been entered in the freight document as missing, you can specify in Customizing that the system

automatically splits the associated freight unit into a freight unit containing the actual quantity and a freight unit that has

the cargo receipt status Missing Cargo. You can then assign the freight unit for the missing cargo to a different freight

document so that the goods can be redelivered at a later date. For more information, see Customizing for Transportation

Management under  Freight Order Management

 Define Discrepancy Profile .

If you want to use normalized load consumption quantities (normalized quantities, NLQ) and additional normalized load

consumption quantities (additional normalized quantities, ALQ) as split criteria, you have made the following settings:

You have defined an alternative quantity for the unit of measure of the normalized quantity in your material master

or you have specified an individual quantity per product or reference product in the Define Normalized Quantity

app.

You have defined a condition with the condition type /SCMTMS/NLQ_UOM.

You have defined the conversion between the units of measure of normalized and additional normalized quantities

in the Customizing activity Define Conversion Between NLQ and ALQ UoM.

Optionally, you have defined the relevance of units of measure for normalized and additional normalized quantities

in the Customizing activity Define UoM Relevance of NLQs and ALQs.

In your freight unit building rule, you have defined normalized or additional normalized quantities or both as the

planning quantity.

For more information, see Use of Normalized Quantities and Capacities.

## Features

## Automatic Creation of Freight Units

First, the system groups all business document items under consideration of the following parameters:

Hard constraints (such as source location and destination location, carrier, and pick-up and delivery dates, see Hard

Constraints)

Business document attributes (such as delivery group) and packaging information

Incompatibilities

## FUB rules

Here the system takes into account freight units that already exist for these business documents.

The system then creates one or more freight units from these groups. If you have defined a split quantity and have selected the

checkbox for the item split, the system takes these entries into account when creating multiple freight units.

The business document item attribute Delivery Group is used to consolidate all items with the same delivery group into one

freight unit. It is also possible to consolidate items with different delivery groups into the same freight unit based on the above

grouping parameters.

In the case of automatically creating freight units, you can specify an FUB rule. If you do not specify an FUB rule, the system

automatically determines the FUB rule. For more information, see Determination of Freight Unit Building Rules. In the FUB rule you

can enter, for example, that freight orders or transportation units are created automatically instead of freight units (see

Transportation Unit) (shortcut scenario). For more information, see Freight Unit Building Rule and Direct Creation of Freight

Orders.

This is custom documentation. For more information, please visit SAP Help Portal.

4


1/14/26, 2:19 PM

When freight units are built, the main cargo items in the forwarding documents can have different categories as defined by the

shipping type. Items with different categories form a compatibility group, which means that these items cannot be grouped into

one freight unit or transportation unit.

A distinction is made between the following groups:

Package, product, and schedule line

Container

Railcar

Trailer

  Example

A forwarding order has a container, package, and railcar as its main cargo items. All of these items have a different compatibility

group, which means that the system will create three freight units or transportation units.

You can also create freight units in the background (see Forwarding Order Management Preparation). However, we recommend

that you use automatic creation.

You can use strategies to create freight units in accordance with your own requirements. SAP delivers the standard strategy

FUB_AUTO for freight unit building. For more information, see Process Controller Configuration.

The system automatically creates, for example, freight units when you save your forwarding order. For more information, see

Editing of a Forwarding Order.

## Creation of Freight Units Based on Normalized and Additional Normalized Quantities

You can have the system build freight units based on normalized and additional normalized quantities as split criteria. You can

define several units of measure for normalized and additional normalized quantities as the planning quantity in your freight unit

building rule. The system determines the relevant unit of measure to be used based on the condition that you have defined.

For more information, see Use of Normalized Quantities and Capacities.

## Manual Splitting and Merging of Freight Units

You can manually split or merge the freight units that the system has created automatically. You can do this on the user interface

of the freight unit, for example. After you have selected Split/Merge, the system proceeds as follows:

When freight units are split, the target freight unit is the one that takes on the product items (or partial quantities of these

items) that are split off and that is created during the split.

When merging freight units, the target freight unit is the existing freight unit that takes on the product items (or partial

quantities of these items) that are split off.

If you select Adopt Stops, the system copies the stops from the existing freight unit. The system also copies the planning

results (routing and assignments to freight orders) from the existing freight unit if it has already been planned.

If you want to prevent the freight units from being changed after a manual split or merge by the automatic creation of

freight units, select Fix Source Freight Unit or Fix Target Freight Unit.

In the case of product items, you can split off or merge partial quantities. When doing so, you must specify the required quantity.

You can split or merge package items and container items if they do not have any subitems, for example, products.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

5


1/14/26, 2:19 PM

If empty freight units are created during splitting, the system does not immediately delete them. You can fill them again.

If they are still empty when you save, the system deletes them.

You can split a freight unit several times. If your freight unit contains, for example, 100 tons, you can enter 10 tons as the

split quantity and 5 as the number of item splits. The system splits the freight unit into 5 freight units, each containing

10 tons. The original freight unit then still contains 50 tons.

You can still split freight units manually after you have started executing the transportation (once the cargo receipt

status has been set to On Hand). Note, however, that the forwarding order is no longer adjusted accordingly.

If a cargo item has subitems that are not assigned to a forwarding order, you can also split the associated freight units

manually (so that you can assign a damaged item to a different freight document, for example).

For manual splitting and merging, the system checks the following parameters:

## Source location, destination location, Incoterms, and dates/times

The system can only split or merge freight units if these parameters match the source freight unit and target freight unit.

Incompatibilities for which you have specified in the Manual Violation field that the incompatibility must not be violated

during manual planning

## Partial quantities

You are not allowed to split off or merge partial quantities for package items or container items.

These “hard” checks are mandatory.

The function for splitting and merging is available on the following user interfaces:

## Transportation cockpit

User interface for displaying freight units

Freight unit table in the planning overview

## Related Information

Consideration of Equipment Data During FU or TU Creation

## Time Windows

Integration of Next Generation Just-In-Time

## Hard Constraints

The input for the creation of freight units is taken from the predecessor documents. Freight unit building tries to consolidate the

items of the predecessor documents as much as possible taking into account freight unit building rules. Further, certain attributes

on item and header level of the predecessor documents may prevent this consolidation and lead to the creation of separate freight

units for the predecessor documents and their items. These attributes are considered as hard constraints and may apply to both

order-based and delivery-based business documents.

The following list contains the main hard constraints using the sales order as an example:

Freight Unit Hard Constraint

## Constraint Level

Predecessor Document Type

Example: Sales Order

## Hard Constraints

This is custom documentation. For more information, please visit SAP Help Portal.

6


1/14/26, 2:19 PM

Freight Unit Hard Constraint

## Constraint Level

Predecessor Document Type

Example: Sales Order

## Carrier

## Header/item

Order-based, delivery-based,

Forwarding agent/carrier

forwarding order

Incoterms

## Item

Order-based, delivery-based,

Incoterms attributes

forwarding order

Service level (shipping

## Item

Order-based, delivery-based,

Shipping condition

condition)

forwarding order

Shipping type

## Header

Forwarding order

n/a

Transportation mode

## Item

Order-based, delivery-based,

Mode of transport of shipping

forwarding order

type

Pick-up and delivery window

## Item

Order-based, delivery-based

Delivery date rule

specification

Unloading point

## Item

Order-based

## Unloading point

Warehouse-related information

## Item

Order-based, delivery-based

n/a

No ADR Exemption Allowed

## Item

Order-based, delivery-based,

Determined by dangerous

indicator

forwarding order

goods check

Empty provisioning information

## Item

Forwarding order

n/a

Block

## Item

Order-based, delivery-based,

Based on delivery block

forwarding order

## Customizing

Legal Control License Indicator

## Item

Order-based, delivery-based

Legal Control License indicator

Source location

## Item

Order-based, delivery-based,

Shipping point (alternatively:

forwarding order

plant)

Destination location

## Item

Order-based, delivery-based,

Ship-to party (alternatively:

forwarding order

buyer)

Acceptable start date

## Item

Order-based, delivery-based,

Pick-up date

forwarding order

Requested start date

## Item

Order-based, delivery-based,

Delivery date

forwarding order

Logical system

## Header

Order-based, delivery-based,

System in which sales order was

forwarding order

created

Base document type code

## Item

Order-based, delivery-based,

Sales order

forwarding order

Base document type code of

## Header

## Order-based

Outbound delivery, for example

successor document

Order combination indicator

## Header

## Order-based

Order combination

Fixed date/time indicator

## Item

## Order-based

Delivery date and quantity fixed

Product transportation group

## Item

## Order-based

## Product-specific attributes

This is custom documentation. For more information, please visit SAP Help Portal.

7


1/14/26, 2:19 PM

Determination of Freight Unit Building Rules

## Use

When creating freight units, the system determines which freight unit building rule (FUB rule) it is to take into account for a

business document item. To find out which business documents are supported, see Creation and Editing of Freight Units.

## Prerequisites

Optionally, you have defined FUB rules. For more information, see Freight Unit Building Rule.

You have defined conditions with the condition type /SCMTMS/FUBR. For more information, see Condition.

## Features

To determine FUB rules, the system does the following:

1. The system checks whether you have specified a condition in the business document type, for example, forwarding order

type. There can be only one condition per business document type.

2. If the system does not find a condition or if this condition does not return a result, the system checks whether you have

specified a standard FUB rule in the business document type.

3. If you have not specified one, the system uses default settings.

  Note

You can see which FUB rule the system has used in the freight unit.

Freight Unit Building Rule

## Use

The system takes into account freight unit building rules (FUB rules) when creating and editing freight units (see Creation and

Editing of Freight Units).

## Features

## Freight Unit Building Strategy

In the FUB rule, you define how the system is to consolidate freight units. To do this, you can use various freight unit building

strategies (FUB strategies):

## Consolidate as much as possible

In this case, the items come from different business documents, for example, forwarding orders. The system groups the

items in freight units.

  Note

In addition to forwarding orders, other possible business documents are forwarding quotations, order-based

transportation requirements, and delivery-based transportation requirements.

This is custom documentation. For more information, please visit SAP Help Portal.

8


1/14/26, 2:19 PM

## Consolidate per item

In this case, the system generates one freight unit per business document item.

Consolidate per request (compatible parts)

In this case, the system groups all items of a business document to form a freight unit.

For all three FUB strategies, the system takes into account hard constraints and incompatibilities (see Incompatibilities).

  Note

The FUB strategy also applies to the creation of transportation units and freight orders (see below under Document Type and

Automatic Creation of Freight Orders).

## Planning and Split Quantities

In the FUB rule, you enter planning quantities (for example, gross weight and gross volume) with the corresponding units of

measure. The system copies the units of measure to the freight units that it creates. The units of measure form the basis for

checking the capacity of resources. You define the maximum capacity of a freight unit using the split quantity.

  Note

If you create equipment-based freight units or transportation units, the system automatically fills the planning and split

quantities from Customizing for the equipment. For more information, see below under Equipment-Based Freight Units

and Transportation Units.

You can also create freight unit building rules without indicating a unit of measure. For more information, see UoM

Setting for Quantity and Alternative Quantity below.

  Example

You want to transport 5 tons of cement, but you can only transport it in batches of 500 kg. In this case, you define a split

quantity of 500 kg. The system generates 10 freight units.

If the system cannot find the planning unit in the business document, it converts the unit using the values that you have defined in

the product master.

  Example

You want to transport 5 tons of cement, but you can only transport it in batches of 0.5 m . In the product master, you have

3

defined that 0.8 m  of cement is equivalent to 1 ton of cement. The system then converts 5 tons of cement into 4 m  and

3

3

generates 8 freight units.

In addition to the split quantity, you can also specify a rounding value. In this case, the system calculates the freight unit quantity

as a multiple of the rounding value.

  Example

You define the following values:

Product

3
1 computer = 1 piece = 0.06 m

Split quantity

3
1 m

This is custom documentation. For more information, please visit SAP Help Portal.

9


1/14/26, 2:19 PM

Rounding value

1 piece

Since 1 m  divided by 0.06 m  makes 16.67 m , with this split quantity, the freight unit can contain a maximum of 16 computers.

3

3

3

If you enter 3 pieces as the rounding value, for example, because you can only pack three computers in a box, the freight unit

can contain a maximum of 15 computers, since 15 is a multiple of 3 and is less than 16.67.

In the FUB rule, you can use the item split checkbox to control whether items are allowed to be split if the split quantity is

exceeded.

  Example

You have defined the following values:

Freight unit building strategy

Consolidate as much as possible

Critical quantity

Gross weight

Item split allowed

No

Split quantity

20 tons

You want to schedule four items with a total weight of 21 tons. Items 1 to 3 each contain 5 tons and item 4 contains 6 tons.

Taking into account your settings, the system creates two freight units:

Freight unit 1 with items 1 to 3

Freight unit 2 with item 4

## Freight Unit Update Strategy

You can specify whether it is possible to move items from one freight unit to another when freight units are updated. You do so by

defining the freight unit update strategy in the freight unit building rule.

  Example

There are two cargo items in a forwarding order. The system creates one freight unit for each item. One freight unit is planned

(FU1) and the other freight unit is not planned (FU2). Item 1 belongs to FU1 and item 2 belongs to FU2.

If item 1 is deleted from the forwarding order, the following occurs:

In the standard system (that is, Item Swap Allowed (Standard Behavior) is selected in the freight unit building rule),

item 2 is moved to FU1 and FU2 is canceled.

If you have selected Item Swap Not Allowed in the freight unit building rule, item 2 stays in FU2 and FU1 is canceled.

## UoM Setting for Quantity and Alternative Quantity

You can indicate which units of measure are allowed for the quantity and alternative quantity that are to be used as planning

quantity. You can either allow dimensionless units of measure only, such as EACH, Pieces, and PAL, or units of measure of all

dimensions. You can also indicate that no unit of measure is required. The system then uses the units of measure defined in the

predecessor document items. In this case, splitting of freight units is not supported.

Other planning quantities are not affected by this setting.

This is custom documentation. For more information, please visit SAP Help Portal.

10


1/14/26, 2:19 PM

  Note

Quantities or alternative quantities that have a unit of measure with a dimension are ignored by vehicle scheduling and routing

(VSR) optimization, transportation proposal, and load consolidation in the respective requirement documents, such as freight

units.

## Document Type

You can control which document type is to be created by the freight unit builder, that is, freight unit type, transportation unit type,

or freight order type. You can either enter a document type directly or enter a condition for determining the document type in the

advanced settings. You define freight unit types, transportation unit types, and freight order types in Customizing. For more

information, see Customizing for Transportation Management under the following:

Planning

## Freight Unit

 Define Freight Unit Types

## Planning

## Transportation Unit

 Define Transportation Unit Types

Freight Order Management

## Freight Order

## Define Freight Order Types

If the system determines a freight order type as the document type, it automatically generates freight orders without generating

freight units or transportation units (see below under Automatic Creation of Freight Orders).

## Default Business Document Categories

During freight unit building, the system can create different categories of transportation units. If you do not specify a freight

document type in the freight unit building rule (either directly or using a condition), the system creates the following business

document categories:

Item Category

Product / package

Package

Container

Railcar

## Trailer

Business Document Category

## Freight unit

Package unit as an instance of the transportation unit with TU

category “Package”

Container unit as an instance of the transportation unit with TU

category “Container”

Railcar unit as an instance of the transportation unit with TU

category “Railcar”

Trailer unit as an instance of the transportation unit with TU

category “Trailer”

In this case, the system reads the default document type from Customizing. You must therefore ensure that a default type has

been defined in the Customizing activities Define Freight Unit Types and Define Transportation Unit Types.

If you want the system to create “Freight unit” instead of “Container unit” as the business document category for container items,

you must specify the document type of the freight unit in the freight unit building rule (either directly or via a condition).

## Equipment-Based Freight Units and Transportation Units

If you enter an equipment type and group in the freight unit building rule, the freight unit builder creates equipment-based freight

units or transportation units. Depending on the equipment type, the freight unit builder creates transportation units of the

category container, railcar, or trailer.

This is custom documentation. For more information, please visit SAP Help Portal.

11


1/14/26, 2:19 PM

The system automatically derives the planning quantities, units of measure, and split quantities from Customizing for the

equipment (Customizing activity Define Equipment Groups and Equipment Types). You can delete or change these quantities in

the freight unit building rule. This enables you to create transportation units or freight orders (shortcut scenario) with multiple

items (see Example: Freight Unit Building for Railcar Units).

If you want the system to create “Freight unit” instead of “Container unit” as the business document category for container items,

you must specify the document type of the freight unit in the freight unit building rule (either directly or via a condition). We

recommend that you enter it directly, rather than using a condition.

For more information, see Consideration of Equipment Data During FU or TU Creation.

## Automatic Creation of Freight Orders

If you want a freight order to be created automatically instead of a freight unit (shortcut scenario), enter a freight order type as the

document type or a condition for determining this freight order type. This function is also supported for transportation units (see

Transportation Unit).

  Example
You specify in a condition that if the quantity exceeds 20 tons, freight order type 1 is to be used; otherwise freight unit type 1 is

to be used.

This function is suitable, for example, for the following cases:

In general you want to send small orders that are below one of the upper limits you have defined with an express delivery

company.

You always have to transport orders as a full load due to their size.

## Process Controller Strategies

You can use strategies to define the way in which freight units are created in accordance with your own requirements. SAP delivers

the standard strategy FUB_AUTO for freight unit building. For more information, see Process Controller Configuration.

## Unified Package Building

On the tab page Advanced Settings you can specify if during freight unit building the system creates freight units, freight orders,

or package units with a complete hierarchy of package and product items based on the information from the order documents.

Moreover, the system determines the exact position of each product in the package and displays these positions in the load plan.

Alternatively, you can define that the system calculates only a rough estimation of the number of packages that can be built. This

estimation is displayed in the header data of a freight unit on the General Data tab page. It can also be used by the VSR optimizer

during planning.

As a prerequisite, you must have entered a unified package building profile. For the determination and display of the exact product

positions, you must have selected Detailed Mixed Package Building as the mixed package building mode in your unified package

building profile.

Whether the system creates a freight unit, freight order, or package unit during freight unit building depends on which document

type you enter on the General Data tab page of the freight unit building rule. If you want the system to create a complete package

hierarchy, you can choose a document type of the categories FU, FO (Freight Order), or TU (Transportation Unit). If you use a TU

type, the category must be Package (that means package unit). We recommend to use a TU type with category Package instead of

an FU type.

This is custom documentation. For more information, please visit SAP Help Portal.

12


1/14/26, 2:19 PM

You can also specify the maximum number of top-level packages that a freight unit, freight order, or package unit may contain

when the system creates them during freight unit building. The system considers this number when it creates a complete package

hierarchy.

Further, you can specify that a separate freight unit, freight order, or package unit is to be created for unpackaged items, that

means, one common business document is created for all unpackaged items that contains no other items. The system considers

this checkbox when it creates a complete package hierarchy. If you use the package builder as your unified package building

engine, you must select the Only Full Packages in PB Result checkbox in your unified package building profile as a prerequisite. In

this case, the system builds full packages for a product and the remaining quantities of this product stay unpackaged.

For more information, see Unified Package Building in TM.

## Activities

You can define FUB rules by opening the app Create Freight Unit Building Rule from the launchpad.

## More Information

Determination of Freight Unit Building Rules

Definition of Dimensions and Units of Measurement

Example: Freight Unit Building for Railcar Units

## Use

There are different ways of creating railcar units using the freight unit builder, as shown in the examples below.

  Note

The examples cover railcar units only, but you can also use the freight unit builder to create containers and trailers.

## Prerequisites

In the freight unit building (FUB) rule, you have specified the FUB strategy Consolidate per Request (Compatible Parts).

You define FUB rules by using the Create Freight Unit Building Rule app, which is available from the Launchpad.

To enable the system to create multi-item railcar units, you have defined item types with multi-items in Customizing for

Transportation Management under  Freight Order Management

 Define Item Types for Freight Order Management

.

You have assigned the item types with multi-items to the transportation unit type for the railcar unit in Customizing for

Transportation Management under  Planning

## Transportation Unit

 Define Transportation Unit Types . If you use the

shortcut scenario, you have assigned them to the freight order type in Customizing for Transportation Management under

Freight Order Management

## Freight Order

 Define Freight Order Types .

Note that if you do not assign the item types, the system creates only single items for the required number of railcars or

containers. It does not create a multi-item with subitems.

Activities

3
The following examples are based on a forwarding order with a product item that weighs 500 tons and has a volume of 200 m .

This is custom documentation. For more information, please visit SAP Help Portal.

13


1/14/26, 2:19 PM

Example 1: Equipment-Based Transportation Units (TUs) as Single-Item Railcar Units

You have configured the freight unit building rule as follows:

Freight Unit Building Rule

Split Quantity

Document Type

## Value

100 tons

## Not specified

Equipment or Vehicle Group / Equipment or Vehicle Type

3
Railcar (maximum payload 100 tons, cubic capacity 50 m )

Result of freight unit building: Five railcar units, each with a capacity of 100 tons and a cubic capacity of 50 m

3

Example 2: Equipment-Based TU as Multi-Item Railcar Unit

You have configured the freight unit building rule as follows:

Freight Unit Building Rule

Split Quantity

Document Type

Value

0

## Not specified

Equipment or Vehicle Group / Equipment or Vehicle Type

3
Railcar (maximum payload 100 tons, cubic capacity 50 m )

Result of freight unit building: One multi-item railcar unit with a capacity of 500 tons and a cubic capacity of 200 m . The railcar

3

unit has five subitems, each of which represents one railcar.

Example 3: Equipment-Based TU as Multi-Item Rail Freight Order (Shortcut Scenario)

You have configured the freight unit building rule as follows:

Freight Unit Building Rule

Split Quantity

Document Type

Value

0

## Freight order type

Equipment or Vehicle Group / Equipment or Vehicle Type

3
Railcar (maximum payload 100 tons, cubic capacity 50 m )

Result of freight unit building: One freight order with a capacity of 500 tons and a cubic capacity of 200 m . The freight order has

3

five subitems, each of which represents one railcar.

  Note

The system calculates the required number of railcar or container items based on the maximum payload and cubic capacity of

the equipment or vehicle type. The total product quantity is consumed by the railcars or containers created, for example, as

follows:

The vehicle type has a maximum payload of 100 tons and a cubic capacity of 50 m . The product (coal) has a total

3

weight of 450 tons and a volume of 200 m . The required number of railcars is therefore 5.

3

The vehicle type has a maximum payload of 100 tons and a cubic capacity of 50 m . The product (cotton) has a total

3

weight of 200 tons and a volume of 220 m . The required number of railcars is therefore also 5.

3

This is custom documentation. For more information, please visit SAP Help Portal.

14


1/14/26, 2:19 PM

Unified Package Building in TM

You can use this function to create packages.

## Use

In Transportation Management (TM) you can have the system create packages as follows:

## When freight units are created

This type of unified package building takes place early in the process if the system creates freight units based on order

documents (for example, forwarding orders or sales orders).

When freight units are created, you can have freight orders or package units created instead of freight units. You make this

setting in the freight unit building rule (see "Prerequisites").

## Based on capacity documents

This type of unified package building takes place late in the process if capacity documents exist already. You can start from

the user interface of an individual capacity document or from the transportation cockpit. It is offered for road freight

orders, trailer units, container units (Road transportation mode only), and package units.

## During the automatic creation of package units

You can create package units based on unified package building for freight units.

Before you build packages, you can check whether your settings are consistent. For more information, see Consistency Check of

Package Building Constraints.

You can use the built packages in load planning. For more information about load planning, see Load Planning.

You can simulate unified package building. For more information, see Test Cockpits for Unified Package Building.

  Note
Several Business Add-Ins (BAdIs) are available for unified package building. For more information, see Customizing for

Transportation Management under  Business Add-Ins (BAdIs) for Transportation Management

 Planning .

## Prerequisites

## Unified Package Building Using the Package Builder

If you want to build packages using the package building engine (package builder), you must have made the required settings. For

more information, see Package Building.

  Note

Some of the SCM Basis transactions are available on the SAP Easy Access screen or in Customizing for TM:

Customizing activity for defining unified package building profiles:

## Planning

## Unified Package Building

## Define Unified Package Building Profile

Customizing activity for defining product orientation profiles:

Master Data

## Product

## Define Product Orientation Profile

This is custom documentation. For more information, please visit SAP Help Portal.

15


1/14/26, 2:19 PM

Customizing activity for defining profiles for the package building optimizer:

## Planning

 Unified Package Building

## Package Building

## Define Profile for Package Building Optimizer

Customizing activity for defining rule profiles for the package building optimizer:

## Planning

 Unified Package Building

## Package Building

 Define Rule Profile for Package Building Optimizer

SAP Easy Access transaction for defining products:

## Logistics

 Transportation Management

 Master Data

## Material

 MM01 - Create  For information about defining

product master data for package building, see SAP Note 2842396

.

SAP Easy Access transaction for checking the consistency of your settings:

## Logistics

 Transportation Management

## Administration

 Unified Package Building

 Package Building

## Check

Consistency of Package Building Constraints

Unified Package Building During Freight Unit Building

You have made the following settings in TM:

You have defined a freight unit building rule with the following settings:

You have entered a unified package building profile (see Unified Package Building Profile).

You have specified whether the system is to create freight units, freight orders, or package units.

You have specified whether the system is to create freight units, freight orders, or package units with a complete

hierarchy of package and product items based on the information from the order documents or only a rough

estimation of the number of packages that can be built. Note that an estimation of the number of packages is

supported only for freight units.

Optional: You have specified the maximum number of top-level packages that a freight unit, freight order, or package

unit may contain. The system takes this number into account only if you have specified that a complete hierarchy of

package and product items is to be created (see above).

For more information, see Freight Unit Building Rule.

You have entered your freight unit building rule in one of the following places:

In the document type of the order document, such as in the forwarding order type in Customizing for TM if you are

working with forwarding orders

In the logistics integration profile if you are working with the “Internal TM Component Integration” (see Logistics

Integration Profile for SD, MM, and LE and Internal TM Component Integration)

Unified Package Building Based on Capacity Documents

You have made the following settings in TM:

You have defined a subprofile Settings for Unified Package Building in your planning profile and entered your unified

package building profile in it (see Planning Profile).

You have assigned your planning profile to the document type of your capacity documents (for example, the freight order

type in Customizing for TM). You have also activated unified package building in the document type. There you can also

specify whether you want the system to update the load plan automatically if you change items again after unified package

building.

Unified Package Building During Automatic Creation of Package Units

This is custom documentation. For more information, please visit SAP Help Portal.

16


1/14/26, 2:19 PM

For more information, see Use of Package Units in Planning (“Automatic Creation of Package Units” section).

## Features

## Unified Package Building During Freight Unit Building

Depending on your settings in the freight unit building rule, the system creates either a complete hierarchy of package and product

items (that exist only locally in the document) or only a rough estimation of the number of packages that can be built. This

estimated number of packages is displayed in the header data of the freight unit and can be used later during VSR optimization.

## Unified Package Building Based on Capacity Documents

If you select Build Packages in a capacity document or in the transportation cockpit, the system creates a complete hierarchy of

package and product items that exist only locally in the document. In doing so, the system does not change packages that

originate from preceding documents, such as forwarding orders.

If you select several capacity documents in the transportation cockpit, the system creates the packages for each document only,

and not for all documents.

You can use Remove Packages to remove the local packages. This action does not remove packages that originate from preceding

documents such as forwarding orders.

The results of unified package building are displayed on the Items tab page in the Load Plan hierarchy view of the capacity

document as well as in the load plan hierarchy in the transportation cockpit. You also get a 3D visualization of the package. For

more information, see Load Plan.

You can also build packages in the background on the basis of capacity documents. For more information, see Unified Package

Building.

To improve performance, you can perform unified package building for multiple capacity documents in parallel. To do this, you have

to define a parallel processing profile and assign it to your planning profile (in the subprofile Settings for Unified Package

Building). For more information, see Definition of Parallel Processing Profiles.

## Unified Package Building During Automatic Creation of Package Units

For more information, see Use of Package Units in Planning (“Automatic Creation of Package Units” section).

## Related Information

Transportation Planning with Mixed Packages and Deconsolidation

Unified Package Building in Integration Based on EWM TUs

Freight Unit

## Definition

A set of goods that are transported together across the entire transportation chain. A freight unit can include transportation

constraints for transportation planning.

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

17


1/14/26, 2:19 PM

The freight unit is used to merge items in the following business documents that are to be transported together:

## Forwarding order

Order-based transportation requirement

## Delivery-based transportation requirement

The freight unit is the smallest unit that can be transported. The business document data and the freight unit building rules form

the basis for building freight units.

You define the most important settings for the freight unit in the freight unit type. For more information, see Customizing for

Transportation Management under  Planning

## Freight Unit

 Define Freight Unit Types .

After the freight units have been created automatically, you can display them on the user interface for the freight unit. You can also

split and merge freight units there (see Creation and Editing of Freight Units). Furthermore, you can also split or merge freight unit

stages on this user interface and in the transportation cockpit. When splitting a stage, you manually insert a transshipment

location. When merging stages, transshipment locations are deleted automatically.

You can create a freight document for a freight unit. For more information, see Creation and Editing of Freight Orders and Creation

and Changing of Freight Bookings.

You can create a house bill of lading or a house air waybill for a freight unit (see Building and Printing of House Bills of Lading and

House Air Waybills).

You can use SAP Event Management to track and monitor freight unit events (see Tracking of Freight Units).

You can use the change controller (see Change Controller) to check whether freight units were changed and how the system reacts

to these changes.

## Structure

The freight unit data is taken automatically from the business document. However, you can still change some of the data. You can

access the following data from the freight unit, for example:

## Items

The freight unit items can stem from different business documents, such as forwarding orders, but a freight unit item is

assigned to only one business document item, such as a forwarding order item.

## Locations

You can enter one-time locations at stage level. The system stores these new locations and adjusts stages in the document.

It also adjusts the locations in the assigned execution documents.

  Note

However, you should continue to make changes to existing locations in the master data.

## Transportation stages

The system displays loading and unloading times, transshipment locations, and means of transport, for example.

## Quantities and deviations

You can display actual quantities and deviations, for example.

## Transportation constraints

This is custom documentation. For more information, please visit SAP Help Portal.

18


1/14/26, 2:19 PM

The system copies this data about the transportation stages from the business document or from the transportation

stages that were created manually or by the system during planning. Depending on how the stage was created, you can

make changes to them. For more information, see Transportation Stages and Dates/Times in the Freight Unit.

## Document flow

The system displays the corresponding business documents with the relevant status information.

Dangerous goods information (see Considering Dangerous Goods)

Status information and blocking information (see Statuses of Business Documents and Blocking Information)

Instructions (see Management of Instructions)

Change documents (see Change Tracking)

CO  emissions (see Calculation of CO2 Emissions)

2

## More Information

## Freight Unit Building Rule

Determination of Direct Shipment Options

Interaction Between Organizational Units

## Nature of Goods

## Deviating Business Partner Addresses

Transportation Stages and Dates/Times in the Freight Unit

## Use

Transportation stages and dates/times are copied from the forwarding order to the freight unit. Only the dates/times are copied

from order-based and delivery-based transportation requirements.

The following section describes special features related to transportation stages and dates/times in the freight unit.

## Features

## Transportation Stages

If a freight unit contains transportation stages because they were predefined in the business document, transshipment must take

place. In this case, you cannot delete the related transportation stops at a later point in time.

If transportation stages result from manual planning or VSR optimization for a freight unit, these transportation stages reflect the

transshipment. In this case, you can change the related transportation stops at a later time, for example, delete or add further

transportation stops. You can only delete if the transportation stage has not been planned (that is, you have to cancel the

assignment to a freight order or a freight booking for the transportation stage).

  Example

For a forwarding order, goods must be transported from A to Z. The freight unit generated from the forwarding order also goes

from A to Z. In planning you refine this, since it is to be a multimodal transport. This results in the freight unit being transported

This is custom documentation. For more information, please visit SAP Help Portal.

19


1/14/26, 2:19 PM

from A to Z via B. These transportation stages are mapped to the freight unit accordingly. This applies for manual planning and

for VSR optimization.

## Dates/Times

After the freight units are generated, the dates/times of the business document are available in the freight unit (in the

transportation stages). Windows for pickup and delivery are also copied to the freight unit from the business document.

You can overwrite windows for pickup and delivery. To do this, you must define a condition (see Condition) and enter it in the

freight unit type in Customizing or enter a corresponding rule in the freight unit type. The system then calculates the window when

generating the freight unit and displays it in the freight unit.

You cannot change dates/times that are copied from the business document. These dates/times can only be changed using the

condition you defined for your window.

Interaction Between Organizational Units

## Use

You can use this function to model how organizational units interact with each other, for example, how a sales organization

interacts with a planning and execution organization. This interaction is especially important if you have to transport certain goods

in a specific transportation stage, for example, dangerous goods.

## Features

The sales organization is responsible for entering the order, for example, but is not allowed to create freight bookings for specific

transportation stages or send them to a carrier. It can therefore propose how to transport the goods (by specifying a route and a

schedule, and assigning a freight order or a freight booking) and sets the organization interaction status to transfer the affected

stages to the planning and execution organization to be checked. The planning and execution organization checks the proposal

and the transportation stage details in the transportation cockpit. It can then confirm the data exactly as proposed in the

forwarding order, change data such as the departure and then confirm the proposal, or reject the proposal outright. The status for

the stage in the forwarding order then changes to Confirmed, Confirmed with Deviations, or Rejected respectively.

  Note

The functions for confirming or rejecting proposals are not displayed as standard, and so the planning and execution

organization must first select an appropriate layout set in the transportation cockpit. For more information, see Use of Profile

and Layout Sets.

The planning and execution organization can also create a freight booking or a freight order for the transportation stage in the

transportation cockpit, or assign the transportation stage to a document that already exists. In this case, the system sets the

organization interaction status automatically from To Be Checked to Confirmed. The sales organization can then confirm the

transportation stages with the sold-to party.

Furthermore, the planning and execution organization can select an existing freight booking in addition to the route and schedule

and confirm the details for the carrier.

Even if a stage has already been confirmed, the sales organization can still make changes to the order. In this case, the system sets

the status of the stage to Changed After Confirmation.

If the planning and execution organization rejects a stage, the sales organization can submit a new proposal by changing the status

of the stage back to To Be Checked.

This is custom documentation. For more information, please visit SAP Help Portal.

20


1/14/26, 2:19 PM

  Note

If the planning and execution organization rejects unconfirmed stages that are assigned to a freight booking via an auto-

confirmation profile these unconfirmed stages are automatically unplanned.

If the sales organization wants to cancel a stage, this must also be approved by the planning and execution organization. The sales

organization therefore sets the status of the relevant stage in the forwarding order to Cancellation Requested. In the

transportation cockpit, the planning and execution organization chooses Confirm for the stage and the status in the forwarding

order subsequently changes to Cancellation Approved.

The sales organization can also remove the default route from a stage in the forwarding order by selecting the stage and choosing

Schedule

 Unassign .

If the sales organization wants to delete the stages of the default route from the actual route, it can do so by selecting one of the

relevant stages and choosing Delete Stage. The system then replaces the stages containing the default route by the original

stages.

## Automatically Setting the Organization Interaction Status

The sales organization can set the organization interaction status manually from Confirmed or Rejected to To Be Checked, Not

Yet Requested, or Cancellation Requested.

You define criteria for automatic confirmation in a profile, which the system determines based on the freight booking type. These

criteria can include, for example, the security status, volume, or weight. If a transportation stage meets the criteria defined in the

profile, the stage can be confirmed automatically (for example, if the volume and weight defined in the profile are less than the

volume and weight defined in the transportation stage).

You can use the Business Add-In BAdI: Change Organization Interaction Status (/SCMTMS/TOR_ORG_INT_STATUS) to control

the following cases:

A transportation stage can be confirmed automatically (that is, the organization interaction status is set automatically from

To Be Checked to Confirmed), such as when the forwarding order does not contain any dangerous goods.

A confirmed transportation stage must be rechecked (that is, the organization interaction status is set automatically from

Confirmed or Rejected to To Be Checked), for example, when quantities are changed.

## Aggregated Organization Interaction Status

The Statuses tab page of the forwarding order shows the aggregated organization interaction status of the forwarding order. This

is an overall status that is based on the statuses of the individual stages.

If all of the stages have the same status, this status is shown as the aggregated organization interaction status (unless all stages

have the status Confirmed with Deviations, in which case the aggregated organization interaction status is set to Confirmed). If all

of the stages have a status that is either To Be Checked or Changed After Confirmation, the aggregated organization interaction

status is set to Changed After Confirmation.

In cases where the status of one stage differs from all of the others, the system sets the aggregated organization interaction status

based on the following rules, which it applies in the sequence specified:

## Sequence

Status of at Least One Stage

Aggregated Status

1

2

Cancellation Approved

Cancellation Partially Approved

Cancellation Requested

## Cancellation Partially Requested

This is custom documentation. For more information, please visit SAP Help Portal.

21


1/14/26, 2:19 PM

## Sequence

Status of at Least One Stage

Aggregated Status

3

4

5

6

7

8

Rejected

## Confirmed

Partially Rejected

Partially Confirmed

Confirmed with Deviations

Partially Confirmed

Changed After Confirmation

Changed After Confirmation

To Be Checked

To Be Checked

Not Yet Requested

Not Yet Requested

## More Information

## Auto-Confirmation Profile

Coordination Between Customer Service Agent and Gateway Agent

Consideration of Equipment Data During FU or TU Creation

## Use

  Note

In the following documentation, the term "equipment" refers to equipment and vehicles, unless otherwise stated.

You can use this function to take into account equipment groups and equipment types as well as the physical properties of your

equipment when creating freight units (FUs) and transportation units (TUs). During freight unit building, the system consolidates

the business document items into containers, railcar units, or trailer units and displays them as freight units or transportation

units. For these FUs and TUs, the system copies the physical properties as well as the equipment type and equipment group that

you defined in Customizing.

  Note

If you later change the equipment type in Customizing (for example, the physical properties), you must trigger an update in the

freight unit building rule based on the equipment type. The system then updates the planning-relevant quantities in the freight

unit building rule based on the changed equipment type.

## Prerequisites

Business documents (forwarding orders, order-based or delivery-based transportation requirements) exist.

You have defined equipment groups, equipment types, and physical properties in Customizing for Transportation

Management. For more information, see  Master Data

## Resources

 Define Equipment Groups and Equipment Types .

## Features

Automatic Creation of Freight Units and Transportation Units

This is custom documentation. For more information, please visit SAP Help Portal.

22


1/14/26, 2:19 PM

You can influence the automatic creation of freight units and transportation units by defining equipment, that is, an equipment

group and an equipment type, in your freight unit building rule.

If you want to use the equipment type and the equipment group contained in the business document item (except for container

item), you must make a customer-specific implementation. For more information, see SAP Note 1552874

.

The system automatically derives the planning quantities, units of measure, and split quantities from Customizing for the

equipment. It uses the maximum payload weight as the maximum gross weight and the cubic capacity as the maximum volume.

All of the other physical properties that you have defined in Customizing are not considered by the system when you create freight

units and transportation units.

If required, you can change the planning quantities and split quantities. This enables you to create transportation units or freight

orders (shortcut scenario) with multiple items (see Example: Freight Unit Building for Railcar Units).

If the capacity is exceeded, the system splits a business document item according to the standard process, provided that the

freight unit building rule and the item type allow a split.

The system only considers equipment for the business document items of the type Package Item and Product Item (schedule

line). The system does not consider equipment for container items, railcar items, and trailer items. If the system determines a

freight unit building rule for these types of item, and you have specified in this freight unit building rule that the system is to copy

the equipment from the business document item, an error message appears and the creation of the freight units or transportation

units is canceled.

## Manual Splitting and Merging of Freight Units

You also have the option of using manual splitting and merging to create empty containers based on equipment. Here you specify

the following:

## Source location and destination location

Freight unit building rule, equipment group, and equipment type

You have the following options:

You enter a freight unit building rule in which you have defined an equipment group and an equipment type.

You enter the equipment group and the equipment type.

In this case, the system uses the standard freight unit building rule.

You enter a freight unit building rule as well as an equipment group and an equipment type.

If the freight unit building rule contains a different equipment group and equipment type, the system overwrites the

values in the freight unit building rule with the values you enter here.

The system creates a freight unit that represents the container. You can then move freight units into this container.

Alternatively, you can mark freight units and merge them in a container. You enter a freight unit building rule as well as an

equipment group and an equipment type. The system creates a container and assigns the freight units to this container.

The system deletes empty containers when you save.

## Example

You have a forwarding order with the following two items:

This is custom documentation. For more information, please visit SAP Help Portal.

23


1/14/26, 2:19 PM

## Item

Quantity

Gross Weight

Item 10

10 Pallets

10,000 kg

Item 20

9 Pallets

9,000 kg

If you use equipment type CNT_EXAMPLE, the system creates the following item:

## Item

Equipment Type

Gross Weight

## Tare Weight

Item 10 (1 container)

CNT_EXAMPLE

22,000 kg

3,000 kg

This item has two subitems that correspond to the items of the forwarding order.

## Related Information

Equipment Groups and Equipment Types

Statuses of Business Documents

## Use

This section contains the list of statuses that the following business documents can have:

Freight order (see Freight Order)

Freight booking (see Freight Booking)

Freight unit (see Freight Unit)

Transportation unit (see Transportation Unit)

Service order (see Service Order)

Consignment order (see Consignment Order)

## Features

The following table lists the statuses that business documents can have.

## Status

## Status Values

Business Documents That Can Have This

Life cycle status

## New

In Process

Completed

## Canceled

Driver assignment status

Not Relevant

Underassigned

## Status

Freight order

Freight booking

## Freight unit

Transportation unit

Service order

## Freight order

This is custom documentation. For more information, please visit SAP Help Portal.

24


1/14/26, 2:19 PM

## Status

Planning status

## Status Values

Business Documents That Can Have This

## Status

Fully Assigned

Overassigned

## Not planned

Partially Planned

## Planned

Not Ready for Planning

## Not Published

All plannable business documents, such

as freight units or transportation units

Subcontracting status

## No Subcontracting Result

All subcontractable business documents

In Tendering

Carrier Assigned

## Sent

Changed After Sending

Confirmation status

## No Confirmation Yet

All subcontractable business documents

Invalid Confirmation

Rejected

## Confirmed

Confirmed with Changes

Update Sent, No Confirmation Yet

Document Changed After Confirmation

Document Changed After Rejection

Not Published

## Published

Review Required

## Completed

Freight order (not supported for rail

freight order)

## Tendering status

Booking confirmation status

Not Sent to Carrier

Freight booking

Sent to Carrier

Rejected by Carrier

Confirmed by Carrier

## Canceled by Shipper

Partially Confirmed by Carrier

Shipping Instruction Sent to Carrier

Acknowledged by Carrier, Confirmation Is

## Pending

## Confirmed by Carrier with Deviations

This is custom documentation. For more information, please visit SAP Help Portal.

25


1/14/26, 2:19 PM

## Status

Cargo receipt status

Execution status

## Status Values

Business Documents That Can Have This

Canceled by Shipper and Acknowledged by

Carrier

Picked Up

Missing Cargo

On Hand

Shipped

## Delivered

Delivery Failed

Not Relevant

## Status

Freight order

Freight booking

## Freight unit

Transportation unit

## Freight order

Not Started/MAWB Open (Air)

Freight booking

## Freight unit

Transportation unit

Consignment Order

In Execution

Executed

Interrupted

## Canceled

Ready for Transportation Execution/MAWB

Finalized (Air)

Not Ready for Transportation

Execution/MAWB Not Finalized (Air)

Loading in Process

Capacity Planning Finished

Handling execution status

Not Determined

## Freight order

Cargo Ready for Loading

## Freight booking

Arrived (only on stop level)

## Transportation unit

Not Unloaded (only on item level)

## Consignment order

Partially Unloaded (only on stop level)

Unloaded

## Not Loaded

Partially Loaded (only on stop level)

## Loaded

Departed (only on stop level)

Not Coupled (only on item level and only for

freight orders, trailer units and railcar units)

Coupled (only on item level and only for

freight orders, trailer units and railcar units)

Not Uncoupled (only on item level and only

for freight orders, trailer units and railcar

units)

This is custom documentation. For more information, please visit SAP Help Portal.

26


1/14/26, 2:19 PM

## Status

## Status Values

Business Documents That Can Have This

## Status

Uncoupled (only on item level and only for

freight orders, trailer units and railcar units)

Checked In (only on stop level)

Checked Out (only on stop level)

Cargo execution status

Not Determined

Cargo Not Unloaded

Freight order

## Freight booking

Cargo Partially Unloaded

Transportation unit

Cargo Unloaded

Cargo Not Loaded

Cargo Partially Loaded

Cargo Loaded

## Not Uncoupled

Cargo Not Unloaded/Not Uncoupled

Cargo Partially Unloaded/Not Uncoupled

Cargo Unloaded/Not Uncoupled

## Partially Uncoupled

Cargo Not Unloaded/Partially Uncoupled

Cargo Partially Unloaded/Partially

## Uncoupled

Cargo Unloaded/Partially Uncoupled

## Uncoupled

Cargo Not Unloaded/Uncoupled

Cargo Partially Unloaded/Uncoupled

Cargo Unloaded/Uncoupled

## Not Coupled

Cargo Not Loaded/Not Coupled

Cargo Partially Loaded/Not Coupled

Cargo Loaded/Not Coupled

## Partially Coupled

Cargo Not Loaded/Partially Coupled

Cargo Partially Loaded/Partially Coupled

Cargo Loaded/Partially Coupled

## Coupled

Cargo Not Loaded/Coupled

## Cargo Partially Loaded/Coupled

This is custom documentation. For more information, please visit SAP Help Portal.

27


1/14/26, 2:19 PM

## Status

## Status Values

Business Documents That Can Have This

Load plan status/unload plan status (on

## Not Planned

Cargo Loaded/Coupled

stop and item level)

Not Relevant

Invalidated

Planned

## Finalized

Load plan item status/unload plan item

## Not Planned

status (on item level)

Not Relevant

Invalidated

Planned

Finalized

## Not Sent

Transmission-to-EWM status

## Status

Freight order

Freight booking

Transportation unit

Consignment order

Freight order

Freight booking

Transportation unit

Consignment order

## Freight order

Partially Sent (only on stop level)

Freight booking

## Sent

Partially Received

## Received

## Cancellation Requested

Cancellation of TM Document Requested

(only on stop level)

Cancellation Confirmed

Published

Not Published

## Publishing status

Waybill/bill of lading finalized status

Not Finalized

## Finalized

Partially Finalized (only for freight bookings)

Transportation unit

Freight booking (air)

Freight unit

## Freight booking

Shipped-on-board status

Not Shipped on Board

Freight booking (ocean)

## Shipped on Board

Uplift confirmation status

Uplift Not Confirmed

Freight booking (air)

## Uplift Confirmed

Master-bill-of-lading status

Master Bill of Lading Not Received

Freight booking (ocean)

Master Bill of Lading Received

Manifest status

Manifest Not Created

Freight order

Manifest Created

## Freight booking

This is custom documentation. For more information, please visit SAP Help Portal.

28


1/14/26, 2:19 PM

## Status

## Status Values

Business Documents That Can Have This

Delivery status

Not Delivered

Partially Delivered

Delivered

## Status

Freight unit, transportation unit, and

freight order if freight order or

transportation unit is automatically

created instead of freight unit (see

“Automatic Creation of Freight Orders” in

Freight Unit Building Rule)

Customs status

Invoicing status

N/A

For more information, see Global Trade.

Not Invoiced

Partially Invoiced

Completely Invoiced

Over-Invoiced

Not Up-to-Date

Freight order

Freight unit

## Service order

Transmission-to-ERP status

New — Not Yet Transmitted

## Freight order

Initial Transmission Started, Not Yet

Freight Booking

Confirmed by ERP

## Transmission Successful

Retransmitted after Changes in TM, Not Yet

Confirmed by ERP

Schedule Data Status

Data Is Up-to-Date

## Freight order

Data Is Not Up-to-Date

Freight booking

Document check status

Last Check with Errors

## Freight Order

Last Check Without Errors or Warnings

## Freight Booking

Last Check with Warnings

## Not Yet Checked

Cross-document check status

Last Cross-Document Check with Green

Freight Order

## Traffic Light

Last Cross-Document Check with Yellow

Freight Booking

Traffic Light

Not Yet Checked

Archiving Status

## Not Archived

Archiving in Process

## Archived

## Fixing of Business Documents

You can unfix the business document and then change it.

Freight order

Freight booking

## Freight unit

## Transportation unit

This is custom documentation. For more information, please visit SAP Help Portal.

29


1/14/26, 2:19 PM

The fixing only prevents the change of already existing planning results, that is, a fixed subcontractable document is

allowed to be subcontracted until a carrier is assigned. If a fixed document is already assigned to a carrier, no more change

is allowed in the planning results.

In VSR optimization, a fixed freight order must not be deleted and assigned freight units must not be unassigned.

For manual planning, you can specify in your planning profile whether you are allowed to change a fixed freight order or not

(Consider Fixing Status).

You can specify in Customizing for the business document type (that is, freight order type and freight booking type) that the

business document is to be fixed automatically each time you save it. In case of one-step planning, the system saves the business

documents only at the very end of the planning process, the fixing takes place at the very end accordingly.

## More Information

For more information about the statuses listed above, see Explanation of Statuses of Business Documents.

For information about statuses in Advanced Shipping and Receiving, see Statuses in Advanced Shipping and Receiving.

For information about statuses in the integration of a TM system with SAP GTS, see Statuses in the Integration with SAP

GTS (Inbound Process) and Statuses in the Integration with SAP GTS (Outbound Process).

Explanation of Statuses of Business Documents

## Use

This section contains an explanation about how the various statuses of business documents in Freight Order Management are set

and what effects these statuses have.

## Features

The following statuses are available:

## Life Cycle Status

This status has the following values:

## New

The business document has been created, but hasn’t been considered in planning and execution yet.

## In Process

Planning, execution, subcontracting, or invoicing was started.

You can specify in Customizing for the business document type that the life cycle status is to be set to In Process

immediately after creation of the business document (that is, even if none of the mentioned processes were started yet).

This setting is required for business documents resulting from a planning process.

## Complete

The transportation execution is finished and the invoicing status is set to Completely Invoiced (or no invoice is expected).

This status is set automatically by the system. You can set this status manually if the business document has the life cycle

status In Process.

## Canceled

This is custom documentation. For more information, please visit SAP Help Portal.

30


1/14/26, 2:19 PM

Planning and execution of transportation is canceled. You can set this status manually at any time in the planning process

by selecting the Cancel Document pushbutton.

## Driver Assignment Status

This status is set automatically by the system on header level when you assign drivers to your entire freight order or individual

transportation stages of a freight order. This status is based on the number of required drivers that you indicate in the freight order

and the number of drivers that you assign to the freight order.

The status has the following values:

## Not Relevant

The freight order is not relevant for driver planning.

## Underassigned

At least one transportation stage of the freight order has too few drivers assigned to it.

## Fully Assigned

The required number of drivers has been assigned to all transportation stages.

## Overassigned

All transportation stages of the freight order have too many drivers assigned to them.

## Planning Status

This status relates to the different planning states of the individual transportation stages. The planning status is set automatically

by the system and is determined based on the planning status of the individual stages.

The status has the following values:

## Not Planned

No transportation stage is planned.

## Partially Planned

At least one transportation stage is planned.

## Planned

All transportation stages are planned.

## Not Ready for Planning

No transportation stage is ready for planning.

## Not Published

No transportation stage is published.

The planning status can relate to an individual transportation stage (not only to a business document). In this case, the planning

status can have the following values:

## Unplanned

The transportation stage hasn’t been planned yet.

This is custom documentation. For more information, please visit SAP Help Portal.

31


1/14/26, 2:19 PM

## Planned

The transportation stage has been planned.

## Planned, Conflict Between FU and Freight Order/Booking Times

The transportation stage has been planned, but there exist conflicts with time constraints regarding the predecessor or the

successor transportation stage.

## Not Ready for Planning

The transportation stage is not ready for planning because a location is missing. The system automatically sets a planning

block.

## Subcontracting Status

This status is set automatically by the system and is relevant for subcontractable business documents. You define the

subcontracting relevance in Customizing for the business document type.

The status has the following values:

## No Subcontracting Result

The carrier hasn’t been determined for the business document.

## In Tendering

The carrier hasn’t been determined, but a tendering process is already in process.

## Carrier Assigned

The carrier was assigned.

## Sent

The business document was sent to the assigned carrier.

The value Carrier Assigned is a prerequisite for this value.

## Changed After Sending

A relevant change was made to the business document after it was sent to the assigned carrier. Relevant changes are:

Quantity changes

## Changes to dates/times

Changes to source locations, intermediate stops, and destination locations

Changes to the transportation service level

For more information, see Change Controller.

## Confirmation Status

This status is either set automatically by the system or manually by the user and is relevant for subcontractable business

documents. You define the subcontracting relevance in Customizing for the business document type.

This status can only be set automatically by the system if the subcontracting status has the value Sent.

The status has the following values:

This is custom documentation. For more information, please visit SAP Help Portal.

32


1/14/26, 2:19 PM

## No Confirmation Yet

The carrier hasn’t sent a confirmation yet.

## Invalid Confirmation Received

The confirmation sent by the carrier cannot be interpreted.

## Rejected

The carrier rejected the business document.

## Confirmed

The carrier confirmed the business document.

## Confirmed with Changes

The carrier confirmed the business document with some changes.

## Update Sent, No Confirmation Yet

The business document was changed and an update was sent but the carrier hasn’t sent a confirmation yet.

## Document Changed After Confirmation

The business document was changed after having been confirmed by the carrier.

## Document Changed After Rejection

The business document was changed after having been rejected by the carrier.

## Tendering Status

This status is set automatically by the system and is relevant for subcontractable business documents that are tendered, that is,

the subcontracting status has the value In Tendering. You define the tendering relevance in Customizing for the business

document type.

The status has the following values:

## Not Published

The user or the system has started tendering for a freight order, but no requests for quotation to carriers have been

published yet.

## Published

The user or the system has started tendering for a freight order, and has published one or several requests for quotation to

carriers.

## Review Required

Review is required by tendering manager.

## Completed

Tendering is completed.

There are also the following statuses:

Freight Request for Quotation: Life Cycle Status

## Not Sent

This is custom documentation. For more information, please visit SAP Help Portal.

33


1/14/26, 2:19 PM

The freight request for quotation has been created in the tendering plan, but it has not been published yet.

## Open

The freight request for quotation has been published and sent to a carrier. Freight quotations can be submitted for

this freight request for quotation.

## Closed

The freight request for quotation has been published and sent to a carrier, but no more freight quotations can be

submitted for it.

## Omitted

The tendering process was completed before the freight request for quotation was sent. In other words, an omitted

freight request for quotation has never been published.

Freight Quotation: Life Cycle Status

## Draft

The freight quotation has been created in the tendering worklist for carriers, but it has not been submitted. It is not

considered in the corresponding tendering process.

## Sent

The freight quotation has been created and submitted for a freight request for quotation. It is considered in the

corresponding tendering process and the evaluation of submitted freight quotations.

Tendering Step: Life Cycle Status

## Not Started

The tendering step has been created in a tendering plan, but not started yet. All freight requests for quotations

assigned to this step are in status Not Sent.

## In Process

At least one freight request for quotation assigned to this step has been published and is in status Open.

## Completed

At least one freight request for quotation assigned to this step had been sent to a carrier. No more freight

quotations can be submitted to the assigned freight requests for quotations.

## Omitted

The tendering process was completed before the tendering step started.

## Booking Confirmation Status

This status is either set automatically by the system or manually by the user.

The status has the following values:

## Not Sent to Carrier

The freight booking hasn’t been sent to the carrier.

## Sent to Carrier

The freight booking has been sent to the carrier.

This is custom documentation. For more information, please visit SAP Help Portal.

34


1/14/26, 2:19 PM

## Rejected by Carrier

The freight booking has been rejected by the carrier.

## Confirmed by Carrier

The freight booking has been confirmed by the carrier.

## Canceled by Shipper

The freight booking has been canceled by the shipper.

## Partially Confirmed by Carrier

The freight booking has been confirmed by the carrier with quantity changes.

## Shipping Instruction Sent to Carrier

A shipping instruction has been sent to the carrier for the freight booking.

## Acknowledged by Carrier, Confirmation Is Pending

The carrier has received the freight booking but has not confirmed it yet.

## Confirmed by Carrier with Deviations

The carrier has confirmed the freight booking with changes.

## Canceled by Shipper and Acknowledged by Carrier

The shipper has canceled the freight booking and the carrier has received this cancellation.

## Cargo Receipt Status

This status is set automatically by the system. It cannot be set manually.

The status has the following values:

Picked Up

The cargo has been picked-up and is now in transit.

## Missing Cargo

The cargo has not yet been received at all or has only been partially received. This status value is set when the actual

quantity (in pieces) is lower than the planned quantity. In this case, the system executes a freight unit (FU) split. This

means that it updates the existing FU and its predecessor documents with the actual quantity, and creates a new FU for the

missing pieces.

## On Hand

The cargo has been received. This status is set automatically when actual quantities are reported. After this status has

been set, only the actual quantities in the freight order or freight booking are taken into account. You can change these

quantities in the freight order or freight booking. If changes are subsequently made in the forwarding order, they are not

copied to the freight order, freight booking, or freight unit.

## Shipped

The cargo has been shipped. This status value is used in the direct integration of Transportation Management (TM) and

Extended Warehouse Management (EWM) in SAP S/4HANA or SAP Extended Warehouse Management (SAP EWM).

## Delivered

This is custom documentation. For more information, please visit SAP Help Portal.

35


1/14/26, 2:19 PM

The cargo has been delivered.

## Delivery Failed

The cargo item could not be delivered.

After you remove a freight unit from a freight order, the system allows you to keep the items without reference to the

predecessor document in the freight order if the cargo receipt status of the items is at least On Hand. In this case, the

cargo receipt status is set to Delivery Failed for these items. As a prerequisite, you must have selected the Enable

Additional Execution Checks checkbox in the Customizing activity for defining freight order types.

  Example
You have planned a freight unit on the freight order and execution of the freight order has started. During execution, not

all cargo could be delivered to the ship-to party, for example. Therefore, you have removed the freight unit from the

freight order. If you have selected this checkbox, the cargo items without reference to the freight unit will remain in the

freight order and the cargo receipt status of the items is set to Delivery Failed. If you have not selected the Enable

Additional Execution Checks checkbox in the Customizing activity for defining freight order types, such cargo items are

removed from the freight order.

  Note
You have also other options to handle a transport when the delivery has failed and to set the status of a transportation

stage to Delivery Failed. For more information, see Handling of Failed Deliveries.

## Execution Status

This status is set automatically by the system for business documents that are subject to tracking. You can specify the tracking

relevance in Customizing for the business document type. For more information, see Execution Tracking.

You can also set this status manually.

The status has the following values:

Not Started/MAWB Open (Air)

Execution hasn’t started yet.

Capacity Planning Finished

Capacity planning was finished.

Loading in Process

Loading was started.

Ready for Transportation Execution/MAWB Finalized (Air)

Transportation execution can be started, that is, loading was finished or a carrier accepted an order.

  Note

A business document with status MAWB Finalized can no longer be planned manually or automatically.

In Customizing, you can enable the automatic derivation of Ready for Transportation Execution/MAWB

Finalized (Air). This triggers when either the first execution-relevant event is reported or the first stop's

execution status in the freight document is updated. For more information, see Customizing for Transportation

Management under  Freight Order Management

 Execution Settings

 Define Event Profiles .

This is custom documentation. For more information, please visit SAP Help Portal.

36


1/14/26, 2:19 PM

Not Ready for Transportation Execution/MAWB Not Finalized (Air)

Transportation execution cannot be started yet because either the check for readiness of execution failed or you set the

status manually to this value.

## In Execution

Execution was started.

You can specify in Customizing for the business document type that the business document is set immediately to In

Execution after creation.

## Executed

Execution has finished.

If you have specified in Customizing that your business document type is relevant for execution tracking, we recommend

that you specify a last expected event. If this event is reported, the execution status is set automatically to Executed.

## Interrupted

Execution has been interrupted.

## Canceled

Execution was canceled.

## Not Relevant

You can specify in Customizing for the business document type that the business document is not relevant for execution

tracking. The system automatically sets this status. The status does not change anymore.

## Handling Execution Status

This status is either set automatically by the system or manually by the user.

For more information about how the handling execution status is set by event reporting, see Execution of Freight Documents

You can set the handling execution status on the following levels:

On item level for cargo items at the current stop

  Note

A cargo item can be a product, a package, or a container.

For example, this status can indicate that a package has been loaded into a container.

You can also set this status on item level for passive vehicle resource items. However, this is only possible for the status

values Coupled, Uncoupled, Not Coupled, and Not Uncoupled.

## On stop level

On this level, this status indicates the progress of the execution activities at a stop. It refers to a container (capacity item or

cargo item) or a cargo item.

The handling execution status is related to the cargo execution status. If all cargo items have been loaded into the container, for

example, the system automatically sets the cargo execution status of the container to Cargo Loaded. Moreover, the handling

execution status on item level and the handling execution status on stop level are related to each other.

This is custom documentation. For more information, please visit SAP Help Portal.

37


1/14/26, 2:19 PM

In addition, the execution status on stop level considers the handling execution status. For example, the execution status on stop

level is only set to a green traffic light if the handling execution status has been set to Unloaded.

For air freight bookings, the handling execution status is also displayed on the Operations tab page and indicates the logistical

execution status. It contains the following:

Location ID (location code)

Status at last location at which freight units were picked up or delivered

## Date/time when the status was set

For ocean freight bookings and freight orders, this information is displayed on the Statuses tab page.

For example, if a freight order for pick-up is assigned to the air freight booking and you change the status of this freight order from

Arrived to Unloaded, the logistical execution status of the air freight booking will indicate Unloaded.

The handling execution status on item level has the following values:

## Not Determined

The system sets this initial status value after you have created the business document. It indicates that no execution

activities are to be performed for the cargo item at the current stop.

## Not Unloaded

The cargo item hasn’t been unloaded at the current stop.

## Unloaded

The cargo item has been unloaded at the current stop.

In the inbound part of the Advanced Shipping and Receiving process, you can use the handling execution status option Set

Items to Unloaded to manually set the status of the items that are unloaded from the truck to Unloaded.

## Not Loaded

The cargo item hasn’t been loaded at the current stop.

## Loaded

The cargo item has been loaded at the current stop.

In the outbound part of the Advanced Shipping and Receiving process, you can use the handling execution status option

Set Items to Loaded to manually set the status of the items at the warehouse loading stop to Loaded.

## Not Coupled

The trailer unit or railcar unit hasn’t been coupled at the current stop.

## Coupled

The trailer unit or railcar unit has been coupled at the current stop.

## Not Uncoupled

The trailer unit or railcar unit hasn’t been uncoupled at the current stop.

## Uncoupled

The trailer unit or railcar unit has been uncoupled at the current stop.

This is custom documentation. For more information, please visit SAP Help Portal.

38


1/14/26, 2:19 PM

The handling execution status on stop level has the following values:

## Not Determined

The system sets this initial status value after you have created the business document. It indicates that no execution

activities have been performed for the containers at a stop.

If you change the status from Arrived to Set to Not Arrived, the status is displayed again.

## Cargo Ready for Loading

The goods are ready to be loaded and you have set the warehouse processing status to Completed. You can initiate

customs processes and have the good cleared before the truck's arrival and check in. Any items whose status is not set to

Completed at this point are removed from the freight order.

To revert the status, select Cargo Not Ready for Loading. The customs invoice and export declaration must not have been

requested.

## Arrived

The goods have arrived.

The Arrival at Destination event is sent to all relevant document in TM automatically.

Checked In

The business documents of the goods that have arrived at the gate match the documents in the system. The truck is

allowed to drive to the yard to unload or load the goods.

If you set the Checked In status without first setting the Arrived status, then the system sets the Arrived status

automatically.

The system automatically reports the Check-In event to the relevant document in TM. The system also automatically

reports the Arrival at Destination event if the Checked In status is set before the Arrived status.

In the inbound part of the Advanced Shipping and Receiving process, if you don't have an explicit check-in process at your

company gate, you can directly set the warehouse processing status to Ready for Warehouse Processing at the warehouse

unloading stop level. The system will automatically set the Checked In status. When you set the Checked In status

manually or the system sets it automatically, all the inbound deliveries for that stop get the status In Yard (for EWM

deliveries) or In Plant (for Logistics Execution (LE) deliveries).

When you set the Checked In status for a stop in a road freight order or consignment order that is relevant for a customs

process in the inbound part of Advanced Shipping and Receiving, the system sends a request for unloading permission to a

SAP Global Trade Services (SAP GTS) system that is integrated with a TM system. The TM system also sets an execution

block for the business document.

To revert the status, select Not Checked In. The system sets the handling execution status back to Arrived.

If a road freight order or consignment order that is relevant for a customs process in Advanced Shipping and Receiving has

an execution block due to a pending unloading permission, the block is not reversed when you reverse the Checked In

status.

## Unloaded

The cargo items have been unloaded.

In the inbound part of the Advanced Shipping and Receiving process, when unloading is completed, you can use the

handling execution status option Set Stop to Unloading Completed to set the status of the warehouse unloading stop to

Unloaded.

## Not Unloaded

This is custom documentation. For more information, please visit SAP Help Portal.

39


1/14/26, 2:19 PM

The truck has arrived at the destianation location of the items to be unloaded, but the unloading has not been completed.

## Not Loaded

The cargo items have not been loaded.

## Loaded

The cargo items have been loaded.

In the outbound part of the Advanced Shipping and Receiving process, after you have finished loading the truck, you can

use the handling execution status option Set Stop to Loading Completed to set the status of the warehouse loading stop

to Loaded. After this status has been set, no further items can be loaded onto the truck, and the system automatically

removes all the items that do not have the status Loaded from the road freight order.

Checked Out

The goods have been unloaded from the truck or loaded onto the truck. The truck is checked to make sure that, for

example, the doors are closed. The documents of the truck are also checked.

The system automatically reports the Checkout event in the assigned freight units and in the business document.

In the Advanced Shipping and Receiving process, if you set the Checked Out status without setting the Departed from

Door status, the system automatically sets the Departed from Door status.

If the export declaration is missing or incomplete for a road freight order or consignment order that is relevant for a

customs process in the outbound part of Advanced Shipping and Receiving, the system sets a block. You cannot set the

handling execution status of the stop to Checked Out until the block is resolved.

To revert the status, select Set to Not Checked Out. The system sets the handling execution status back to Unloaded or

Loaded.

## Departed

This status value indicates that the truck has departed.

If you set the source stop of the main carriage to Departed, the vessel is loaded and has departed (Shipped on Board).

The Departure event is automatically sent to all documents in TM. Similarly, if you report a Departure event, the system

automatically sets the handling execution status at stop level to Departed.

To revert the status, select Set to Not Departed. The system sets the handling execution status back to Checked Out.

For more information about the handling execution status in rail freight orders, railcar units, and container units, see Rail Freight

Order.

## Cargo Execution Status

This status is either set automatically by the system or manually by the user. It indicates the execution status of a container

(capacity item or cargo item) at the current stop, for example a container has been fully loaded at the source stop of the main

carriage.

The status has the following values:

## Not Determined

The system sets this initial status value after you have created the business document. It indicates that no execution

activities are to be performed for the container at the current stop.

## Cargo Not Unloaded

This is custom documentation. For more information, please visit SAP Help Portal.

40


1/14/26, 2:19 PM

The container hasn’t been unloaded at the current stop.

## Cargo Partially Unloaded

The container has been partially unloaded at the current stop.

## Cargo Unloaded

The container has been unloaded at the current stop.

## Cargo Not Loaded

The container hasn’t been loaded at the current stop.

## Cargo Partially Loaded

The container has been partially loaded at the current stop.

## Cargo Loaded

The container has been loaded at the current stop.

Furthermore the status contains values that show for a truck not only the status of loading and unloading (as described above),

but also whether all its assigned trailers are coupled or uncoupled (or only some of them). For example, you have the status values

Cargo Loaded/Coupled or Cargo Partially Loaded/Partially Coupled. For a complete list of all status values, see Statuses of

Business Documents.

For more information about the cargo execution status in rail freight orders, railcar units, and container units, see Rail Freight

Order.

## Load Plan Status and Unload Plan Status

You can set this status to indicate that goods are ready for loading or unloading at a stop. You can set the status on header, stop,

and item level of a freight document with the following effects:

Header level: The system searches for the next relevant stop for loading or unloading of the goods, sets the status on stop

level, and sends a loading or unloading request (LDAP request) to EWM or SAP EWM for the relevant stop.

Stop level: The system sends an LDAP request to EWM or SAP EWM for this stop.

Item level: The system does not send an LDAP request.

You can set the load plan or unload plan status independently from the handling execution status. By setting this status, for

example, you notify the next relevant stop for loading or unloading goods that the truck will arrive soon. The next relevant stop is

usually the next stop after the current stop that has been modelled in the location master data as a warehouse. The current stop of

execution and the handling execution status are only changed when EWM or SAP EWM sends an LDAP notification to TM, when

you change the status manually, or when an execution event is reported, for example, by SAP Event Management.

The status has the following values:

## Not Planned

The plan hasn’t been started. This is the initial status value.

## Not Relevant

The plan is not relevant for this stop or item.

## Invalidated

This is custom documentation. For more information, please visit SAP Help Portal.

41


1/14/26, 2:19 PM

The plan has changed (for example, items have been added or deleted); you have to set the status to Finalized again on

stop level to send an LDAP request to EWM or SAP EWM.

## Planned

The plan is in a preliminary state.

## Finalized

The plan is complete. The system automatically sends an LDAP request to EWM or SAP EWM, when the status value is set

on header or stop level of the freight document.

The load plan status for referenced capacity items (package items, container items, trailer items, and railcar items) is displayed in

the assigned successor document and can be set there as well. For example, if you have a road freight order with an assigned

trailer unit, you can set the load plan status for the referenced trailer item hierarchy in the road freight order directly.

A status change can be triggered by the following actions:

You can set the status manually.

You can perform unified package building.

You can perform load planning.

In freight bookings and freight orders for pick-up or delivery, the load plan status of the referenced container item hierarchy is

displayed but you can't change it.

## Load Plan Item Status and Unload Plan Item Status

This status shows whether the plan has changed at item level. It enables you to establish, for example, whether new items have

been added to or deleted from the plan. If the plan has changed, the load or unload plan item status is set to Invalidated.

The status has the same values as the load or unload plan status.

Note that you can set this status for items or packages of a business document in the context of load planning and packaging. For

more information, see Transportation Planning with Mixed Packages and Deconsolidation. In this context, an additional status

value is available for the load plan item status:

## Packaging not Relevant

The item does not need to be packaged.

## Transmission-to-EWM Status

This status describes the message exchange with an external warehouse management system, for example, SAP EWM. The status

is automatically set when the LoadingAppointmentRequest message is sent to SAP EWM or the

LoadingAppointmentNotification message is received from SAP EWM. The system can set it on item level or on stop level.

On stop level, the system sets it separately for an inbound or an outbound stop. On item level, the status refers to the inbound or

outbound stop respectively.

The status on item level has the following values:

## Not Sent

The item hasn’t been sent at the current stop.

## Sent

This is custom documentation. For more information, please visit SAP Help Portal.

42


1/14/26, 2:19 PM

The item has been sent at the current stop.

## Partially Received

A partial quantity has been received at the current stop and further updates are to be expected. The status won't change

until the truck departs, even if all items have already been loaded.

## Received

The item has been received at the current stop and the truck has departed.

## Cancellation Requested

A cancellation has been requested for the business document at the current stop.

## Cancellation Confirmed

The cancellation for the business document has been confirmed at the current stop.

The status on stop level has the following values:

## Not Sent

No items have been sent.

## Partially Sent

Some of the items have been sent.

## Sent

All items have been sent.

## Partially Received

At least one of the items has been received or partially received.

## Received

All items have been received.

## Cancellation Requested

A cancellation has been requested for all items.

## Cancellation of TM Document Requested

A cancellation of a freight order or freight booking has been requested.

## Cancellation Confirmed

The cancellation for the items has been confirmed.

## Publishing Status

This status controls whether a business document can be used by other users, for example, other organizational units.

The status has the following values:

## Not Published

The business document has not yet been published and cannot be used by other users.

## Published

This is custom documentation. For more information, please visit SAP Help Portal.

43


1/14/26, 2:19 PM

The business document has been published and can be used by other users.

## Waybill/Bill of Lading Finalized Status

You set this status for freight units via your air forwarding orders.

This status has the following values:

## Not Finalized

The waybill or bill of lading hasn’t yet been finalized.

## Finalized

The waybill or bill of lading has been finalized.

Partially Finalized (only for freight bookings)

This status is set for a freight booking if its freight units have different waybill or billl of lading statuses, for example, if one

freight unit is finalized and another freight unit is not finalized.

## Shipped-on-Board Status

You set this status manually after the vessel has departed the source stop of the main carriage. The shipped-on-board date must

not lie in the future.

As a prerequisite, the execution status is to be set to Ready for Transportation Execution.

The status has the following values:

## Not Shipped on Board

The vessel hasn’t departed yet.

Shipped on Board

The vessel has departed.

The system automatically sets the handling execution status of the source stop of the main carriage and all previous

outbound stops to Departed.

## Uplift Confirmation Status

You set this status manually after the aircraft has departed the source stop of the main carriage. The uplift date must not be in the

future.

As a prerequisite, the execution status is to be set to MAWB Finalized.

The status has the following values:

## Uplift Not Confirmed

The aircraft hasn’t departed yet.

## Uplift Confirmed

The aircraft has departed.

The system automatically sets the handling execution status of the source stop of the main carriage and all previous

outbound stops to Departed.

This is custom documentation. For more information, please visit SAP Help Portal.

44


1/14/26, 2:19 PM

## Master-Bill-of-Lading Status

You set this status manually after a master bill of lading has been created for an ocean freight booking. If you want to change the

master bill of lading number after having set this status, you first have to reset this status.

The status has the following values:

Master Bill of Lading Not Received

No master bill of lading has been received yet.

Master Bill of Lading Received

A master bill of lading has been received.

## Manifest Status

You set this status manually after loading has been finished.

The status has the following values:

## Manifest Not Created

No manifest has been created yet.

## Manifest Created

A manifest has been created.

## Delivery Status

This status is set automatically by the system. It is derived from the cargo receipt status on item level:

If you set the first item to Delivered, the system automatically sets the delivery status of the freight unit to Partially

Delivered.

If you set the last item to Delivered, the system automatically sets the delivery status of the freight unit to Delivered.

The status is also automatically set to Delivered, if the Proof of Delivery event is reported.

The status has the following values:

## Not Delivered

The freight unit hasn’t been delivered.

## Partially Delivered

The freight unit has been partially delivered.

## Delivered

The freight unit has been delivered.

## Transmission-to-ERP Status

This status is only relevant if you use transportation data from an ERP system and if you want to create ERP shipments based on

the planned freight order.

This is custom documentation. For more information, please visit SAP Help Portal.

45


1/14/26, 2:19 PM

The transmission-to-ERP status is set automatically by the system when the data exchange is processed.

As a prerequisite, you have set the shipment creation relevance in Customizing to Shipment Creation in SAP ERP for the business

document type (freight order type and freight booking type).

The status has the following values:

## New - Not Yet Transmitted

Business document is new, and no data was transmitted to the ERP system yet.

## Initial Transmission Started, Not Yet Confirmed by ERP

Initial transmission of business document information to the ERP system has been started, but no confirmation has been

received yet from the ERP system.

## Transmission Successful

Business document information was successfully transmitted to the ERP system.

## Retransmitted after Changes in TM, Not Yet Confirmed by ERP

Retransmission of business document information to the ERP system has been started after business document has been

changed. New confirmation has not been received yet from the ERP system.

## Invoicing Status

This status is only relevant if an invoice is expected from the carrier for a subcontractable business document.

The status is set automatically by the system once a cost calculation has been performed.

The status has the following values:

## Not Invoiced

No invoicing request was created.

## Partially Invoiced

Partial invoicing request was created.

## Completely Invoiced

Invoicing request was created for the total costs.

## Over-Invoiced

Invoicing request was created for additional costs.

## Not Up-to-Date

Invoicing request was created for a settlement document to accommodate the changes in the final amount of any charge

item of an order.

Once a freight settlement document is created either manually or in background processing, the invoicing status can change to

Partially Invoiced, Completely Invoiced, Over-Invoiced, or Not Up-to-Date. The system determines the invoicing status based on

the calculated costs in the order and the invoiced values in the freight settlement document. An invoice is completed if the

invoiced values equal the calculated costs. An order is partially invoiced if the invoiced values are less than the calculated costs. An

invoice is over-invoiced if the invoiced values are more than the calculated costs.

## Schedule Data Status

This is custom documentation. For more information, please visit SAP Help Portal.

46


1/14/26, 2:19 PM

This status is set automatically if a referenced schedule has been changed. For more information, see Use of Schedules.

The status has the following values:

## Data Is Up-to-Date

The referenced data is up-to-date.

## Data Is Not Up-to-Date

A referenced schedule has been changed and the referenced data is not up-to-date.

## Document Check Status

This status is set automatically, If you start the check manually and save the business document. The status has the following

values:

## Last Check with Errors

The last check was performed with errors.

## Last Check Without Errors or Warnings

The last check was performed without errors or warnings.

## Last Check with Warnings

The last check was performed with warnings.

## Not Yet Checked

The check hasn’t been performed yet.

## Cross-Document Check Status

The system checks if there are time conflicts between a business document and its predecessor or successor business

documents. This check is performed automatically and the status set automatically when you save a business document. You can

also start the check manually. In this case, the status is also set automatically.

Examples:

A freight booking arrives too late for the subsequent freight order.

Transportation times do not lie within the time windows for pickup and delivery.

The status has the following values:

Last Cross-Document Check with Green Traffic Light

The check was performed without errors.

Last Cross-Document Check with Yellow Traffic Light

The check was performed with warnings.

## Not Yet Checked

The check hasn’t been performed yet.

## Archiving Status

This is custom documentation. For more information, please visit SAP Help Portal.

47


1/14/26, 2:19 PM

The status has the following values:

## Not Archived

The business document hasn’t yet been archived.

## Archiving in Process

The business document has been selected for archiving and processed by the archiving pre-processing.

## Archived

The business document has been written to the archive. It can still be accessed in display mode.

For more information about archiving, see Archiving in Transportation Management (TM)

## More Information

For information about statuses in Advanced Shipping and Receiving, see Statuses in Advanced Shipping and Receiving.

For information about statuses in the integration of a TM system with SAP GTS, see Statuses in the Integration with SAP

GTS (Inbound Process) and Statuses in the Integration with SAP GTS (Outbound Process).

Blocking Information of Freight Units and Capacity Documents

## Use

You can set planning, execution, and invoicing blocks for business documents, such as freight units, freight documents, and

transportation units. The blocks can be set as follows:

Automatically, for example if a dangerous goods check indicates an error

Automatically, by being copied from a predecessor document

## Manually

## Prerequisites

You have defined block reasons in Customizing. For more information, see Customizing for Transportation Management under

Basic Functions

## General Settings

 Define Block Reason Codes .

You have defined a block profile in Customizing. You can define tolerances for time conflicts in this profile and specify which blocks

are copied to which specific successor documents.

Also, you have assigned the profile in Customizing to the document types (freight unit type, freight order type, freight booking

type, and transportation unit type). For more information, see Customizing for Transportation Management under  Freight Order

## Management

 Define Block Profile .

## Features

You can display all the automatic blocks on the Block Information tab page. Furthermore, you can set or remove blocks manually:

## Manual setting of blocks

This is custom documentation. For more information, please visit SAP Help Portal.

48


1/14/26, 2:19 PM

When you set blocks manually, you can select a block reason from the values defined in Customizing. You can also set, for

example, multiple planning or execution blocks and choose different block reasons. All the block reasons are displayed both

in the aggregated view of the blocks next to the block status and in the successor documents.

You can set manual blocks for an entire business document or only for individual document items or stages.

## Automatic setting of blocks

If blocks were set in a predecessor document (this means in a forwarding order or freight unit), blocks are set by the

system. Automatic blocks can also be created after checking dangerous goods and approvals as well as during integration

with SAP Extended Warehouse Management, for example. The following detailed information is displayed on the Block

Information tab page:

The predecessor document that caused the block

You can use a link to navigate to this document.

## The type and reason for the block

## The date on which the block was created and the person responsible

When you view the block details, the system displays more information about a block, such as why a forwarding order is still

incomplete for planning or the item for which there is a discrepancy.

## Removal of blocks

When you remove a block, you can enter a comment. The system also logs and displays who removed the block and when.

Note that you require the authorization to remove blocks.

If you have created a block profile in Customizing and you have defined tolerances for time conflicts, the system ignores

these conflicts when it sets planning blocks. The system can also ignore consecutive time conflicts that arise after an initial

time conflict has been ignored. For example, a system update can have led to a worsening of the conflict. Time conflicts can

arise if a requested pick-up or delivery date/time is exceeded.

For freight orders and freight bookings, only the execution block is copied from the freight unit. The invoicing block is set

automatically or manually. It cannot be copied from a predecessor document.

## More Information

Blocking Information of a Forwarding Order

## Handling of External Freight Units

In Transportation Management (TM), you can also plan freight units that originate from an external system (for example from TM

in SAP S/4HANA Cloud Public Edition). However, restrictions apply to these freight units.

Freight units can be replicated from an external system to TM in SAP S/4HANA, where they can be planned and sent back to the

external system. For example, freight units can be created in TM in SAP S/4HANA Cloud based on sales orders and sent to SAP

S/4HANA for planning. The freight orders to which the freight units were assigned are sent back again to SAP S/4HANA Cloud

Public Edition after planning. All changes to the freight orders in SAP S/4HANA are sent to SAP S/4HANA Cloud Public Edition

until accruals have been posted there for the freight orders. Changes to the freight units in SAP S/4HANA Cloud Public Edition are

also sent continuously to SAP S/4HANA.

To ensure that changes to the freight units in TM are not overwritten by updates from the original system, most of the fields of the

freight units cannot be edited and certain actions cannot be performed. This should also ensure that the freight units still fulfill the

requirements of the external system after planning in TM. Examples of permitted and not permitted changes and actions are

detailed below.

This is custom documentation. For more information, please visit SAP Help Portal.

49


1/14/26, 2:19 PM
## Possible Changes and Actions

When you plan external freight units in TM, you can change the following data and perform the following actions:

## Adjusting times and dates

## Assigning freight units to freight orders

Certain actions, such as assigning freight units to other capacity documents, assigning freight units to trailers, or creating package

units for a freight unit, are basically possible but might cause problems in the external system if this system does not support the

corresponding function.

## Changes and Actions That Are Not Permitted

You cannot change the following data or perform the following actions for freight units from an external system:

Changing quantities

## Freight unit building

Splitting and merging freight units

Changing, splitting, and merging stages

Canceling freight units

Building house bills of lading

## Identification of External Freight Units

The Origin of Freight Unit field shows in your personal worklist (POWL) as well as on the user interface of a freight unit if a freight

unit originates from an external system (External) or was created in TM in SAP S/4HANA (Internal). In addition, the system

displays how the freight units were created (for example, during freight unit building or in the export or import process).

Furthermore, the original freight unit is displayed in the document flow.

## Unified Package Building

Unified package building is a generic packaging layer that allows the creation of packages.

The input for unified package building are items, such as products. The result is a possible packaging hierarchy consisting of

packages and auxiliary packaging materials. This packaging hierarchy is saved in the corresponding business documents in the

application from which you have called unified package building.

Unified package building supports alternative packaging approaches. These packaging approaches are called unified package

building engines and process different sets of packaging master data and Customizing settings. The following unified package

building engines are supported:

Package building with the package builder

Packing instruction

## Packaging specification

For more information, see Unified Package Building Engines.

This is custom documentation. For more information, please visit SAP Help Portal.

50


1/14/26, 2:19 PM

You can freely choose, which of these unified package building engines you want to use. You specify this in the unified package

building profile. Depending on the unified package building engine you select, you can define specific settings. Further, you can

specify generic settings for unified package building. For more information, see Unified Package Building Profile.

The following graphic illustrates the different components and their relationship as explained above:

Unified package building offers several execution modes:

The default execution mode is the building of packages. The system uses the best set of packaging master data or

Customizing settings it can find.

Further, the system provides the option to determine, which packing instructions or packaging specifications (unified

package building rules) are available for certain products.

Optionally, you can start the building of packages with specific unified package building rules.

Note however, that the last two execution modes are only available in certain processes. For more information, see SAP Note

3076865

.

You can test the different execution modes independent from an application in the test cockpits for unified package building. For

more information, see Test Cockpits for Unified Package Building.

  Note

You can use the Business Add-In BAdI: Unified Package Building (/SCMB/EX_PB_UNIFIED) to adjust both the items to be

packaged and the result items after packaging.

Unified package building is used in the following components of SAP S/4HANA:

Transportation Management (TM)

For more information, see Unified Package Building in TM.

Extended Warehouse Management (EWM)

For more information, see Unified Package Building in Extended Warehouse Management.

Logistics General (LO)

For more information, see Unified Package Building in Logistics General (LO).

This is custom documentation. For more information, please visit SAP Help Portal.

51


1/14/26, 2:19 PM

Unified Package Building in TM

You can use this function to create packages.

## Use

In Transportation Management (TM) you can have the system create packages as follows:

## When freight units are created

This type of unified package building takes place early in the process if the system creates freight units based on order

documents (for example, forwarding orders or sales orders).

When freight units are created, you can have freight orders or package units created instead of freight units. You make this

setting in the freight unit building rule (see "Prerequisites").

## Based on capacity documents

This type of unified package building takes place late in the process if capacity documents exist already. You can start from

the user interface of an individual capacity document or from the transportation cockpit. It is offered for road freight

orders, trailer units, container units (Road transportation mode only), and package units.

## During the automatic creation of package units

You can create package units based on unified package building for freight units.

Before you build packages, you can check whether your settings are consistent. For more information, see Consistency Check of

Package Building Constraints.

You can use the built packages in load planning. For more information about load planning, see Load Planning.

You can simulate unified package building. For more information, see Test Cockpits for Unified Package Building.

  Note
Several Business Add-Ins (BAdIs) are available for unified package building. For more information, see Customizing for

Transportation Management under  Business Add-Ins (BAdIs) for Transportation Management

 Planning .

## Prerequisites

## Unified Package Building Using the Package Builder

If you want to build packages using the package building engine (package builder), you must have made the required settings. For

more information, see Package Building.

  Note

Some of the SCM Basis transactions are available on the SAP Easy Access screen or in Customizing for TM:

Customizing activity for defining unified package building profiles:

## Planning

## Unified Package Building

## Define Unified Package Building Profile

Customizing activity for defining product orientation profiles:

Master Data

## Product

## Define Product Orientation Profile

This is custom documentation. For more information, please visit SAP Help Portal.

52


1/14/26, 2:19 PM

Customizing activity for defining profiles for the package building optimizer:

## Planning

 Unified Package Building

## Package Building

## Define Profile for Package Building Optimizer

Customizing activity for defining rule profiles for the package building optimizer:

## Planning

 Unified Package Building

## Package Building

 Define Rule Profile for Package Building Optimizer

SAP Easy Access transaction for defining products:

## Logistics

 Transportation Management

 Master Data

## Material

 MM01 - Create  For information about defining

product master data for package building, see SAP Note 2842396

.

SAP Easy Access transaction for checking the consistency of your settings:

## Logistics

 Transportation Management

## Administration

 Unified Package Building

 Package Building

## Check

Consistency of Package Building Constraints

Unified Package Building During Freight Unit Building

You have made the following settings in TM:

You have defined a freight unit building rule with the following settings:

You have entered a unified package building profile (see Unified Package Building Profile).

You have specified whether the system is to create freight units, freight orders, or package units.

You have specified whether the system is to create freight units, freight orders, or package units with a complete

hierarchy of package and product items based on the information from the order documents or only a rough

estimation of the number of packages that can be built. Note that an estimation of the number of packages is

supported only for freight units.

Optional: You have specified the maximum number of top-level packages that a freight unit, freight order, or package

unit may contain. The system takes this number into account only if you have specified that a complete hierarchy of

package and product items is to be created (see above).

For more information, see Freight Unit Building Rule.

You have entered your freight unit building rule in one of the following places:

In the document type of the order document, such as in the forwarding order type in Customizing for TM if you are

working with forwarding orders

In the logistics integration profile if you are working with the “Internal TM Component Integration” (see Logistics

Integration Profile for SD, MM, and LE and Internal TM Component Integration)

Unified Package Building Based on Capacity Documents

You have made the following settings in TM:

You have defined a subprofile Settings for Unified Package Building in your planning profile and entered your unified

package building profile in it (see Planning Profile).

You have assigned your planning profile to the document type of your capacity documents (for example, the freight order

type in Customizing for TM). You have also activated unified package building in the document type. There you can also

specify whether you want the system to update the load plan automatically if you change items again after unified package

building.

Unified Package Building During Automatic Creation of Package Units

This is custom documentation. For more information, please visit SAP Help Portal.

53


1/14/26, 2:19 PM

For more information, see Use of Package Units in Planning (“Automatic Creation of Package Units” section).

## Features

## Unified Package Building During Freight Unit Building

Depending on your settings in the freight unit building rule, the system creates either a complete hierarchy of package and product

items (that exist only locally in the document) or only a rough estimation of the number of packages that can be built. This

estimated number of packages is displayed in the header data of the freight unit and can be used later during VSR optimization.

## Unified Package Building Based on Capacity Documents

If you select Build Packages in a capacity document or in the transportation cockpit, the system creates a complete hierarchy of

package and product items that exist only locally in the document. In doing so, the system does not change packages that

originate from preceding documents, such as forwarding orders.

If you select several capacity documents in the transportation cockpit, the system creates the packages for each document only,

and not for all documents.

You can use Remove Packages to remove the local packages. This action does not remove packages that originate from preceding

documents such as forwarding orders.

The results of unified package building are displayed on the Items tab page in the Load Plan hierarchy view of the capacity

document as well as in the load plan hierarchy in the transportation cockpit. You also get a 3D visualization of the package. For

more information, see Load Plan.

You can also build packages in the background on the basis of capacity documents. For more information, see Unified Package

Building.

To improve performance, you can perform unified package building for multiple capacity documents in parallel. To do this, you have

to define a parallel processing profile and assign it to your planning profile (in the subprofile Settings for Unified Package

Building). For more information, see Definition of Parallel Processing Profiles.

## Unified Package Building During Automatic Creation of Package Units

For more information, see Use of Package Units in Planning (“Automatic Creation of Package Units” section).

## Related Information

Transportation Planning with Mixed Packages and Deconsolidation

Unified Package Building in Integration Based on EWM TUs

## Unified Package Building Profile

The unified package building profile is a collection of parameters with which you control the creation of packages.

In the unified package building profile, you can define generic settings for unified package building (UPB):

You can control UPB in a way that items belonging to different locations or containing different products, for example, must

not be packaged together.

You can indicate that auxiliary packaging materials are treated as separate items in the result of UPB. For more information,

see Defining Auxiliary Packaging Materials.

This is custom documentation. For more information, please visit SAP Help Portal.

54


1/14/26, 2:19 PM

You can activate the application log and indicate the logging severity.

You can choose, which UPB engine the system is to use. The following engines are available:

Package building with the package builder

Packing instruction

## Packaging specification

For more information, see Unified Package Building Engines.

  Note

In the test cockpits for UPB, you can see, which packing instruction or packaging specification was used. This

information is provided in the Unified Package Building Rule field. The UPB rule is an abstraction of the used packing

instruction or packaging specification, which both work based on rules. If you use package building as your UPB engine,

this field is empty because package building does not work based on rules.

The determination of UPB rules, that is, which packing instructions or packaging specifications are available for certain

products, is only supported in certain processes. For more information, see SAP Note 3076865

. This SAP Note also

contains information about other technical restrictions.

In the following, the settings for these UPB engines are described:

## Settings for the Package Builder

You can make general settings, such as a product relationship profile. You can also indicate, for example, that remaining quantities

of a product stay unpackaged and you can activate package level aggregation.

Under the mixed package building settings, you can indicate whether the system is to create mixed packages or not and you can

specify various attributes for mixed package building.

Under the grouping settings, you can indicate a location hierarchy for grouping and specify whether products belonging to

different location groups must not be packaged together (hard constraint) or are not to be packaged together if possible (soft

constraint). A location group could be all products to be delivered to a certain area or region, for example. In addition, you can

specify utilization thresholds for products to be delivered to certain soft location groups or business partners. Based on these

thresholds, the system checks if the utilization of a package is sufficient related to its weight, height, or volume so that a separate

package can be built. If the utilization is not sufficient, the products are consolidated with products for other soft location groups

or business partners.

Under the layer settings, you can specify for layer-based mixed package building that no mixed layers are built, for example, or

that the system is not allowed to create crowns.

Further settings are available for the embedded layer-based mixed package building (ABAP-based heuristic), which can also be

disabled. In this case, layer-based mixed package building is based on the package building optimizer (if you select detailed mixed

package building as your mixed package building mode (see below)) or no layers are built (if you select volume-based mixed

package building as your mixed package building mode).

Finally, under the mode settings, you can specify the mixed package building mode, that is, whether packages are to be built

based on volume (volume-based mixed package building) or whether the exact positions of the products are to be determined

(detailed mixed package building). For detailed mixed package building, you can make further settings. For example, you can

indicate how the products will be arranged. Further, you can disable stacking, grouping, and overhang. And finally, by indicating a

profile and a rule profile for the package building optimizer, you can let the system take into account further technical settings and

predefined rules.

This is custom documentation. For more information, please visit SAP Help Portal.

55


1/14/26, 2:19 PM

For more information, see the system documentation.

  Note

You do not have to define any of these parameters. The package building will then run in standard mode.

Some of these parameters are also available in the Change Package Type Assignment app. However, the parameters in

the UPB profile are global settings and are taken into account only if you have not defined more specific values in the

Change Package Type Assignment app.

To define a UPB profile, enter transaction code /SCMB/UPB_PROFILE in the command field.

For more information, see Package Building.

## Settings for the Packing Instruction

You indicate a packing transaction profile. For more information, see Packing with Packing Instructions.

  Note

The following parameters of the packing transaction profile are not taken into account during UPB:

Packing Instruction Selection Dialog

Start Automatically

## Display Mode

Further, you can make UPB-specific settings, such as the relevant packaging level. With this setting, you can control whether the

system is to determine the innermost packaging material or the outermost packaging material (default value) when determining

UPB rules.

## Settings for the Packaging Specification

You indicate a determination procedure. For more information, see Packaging Specification.

Further, you can make UPB-specific settings. You can specify whether the system is to consider all relevant levels of the packaging

specification irrespective whether you have selected the HU Creation checkbox for a level in the packaging specification or not.

This setting can influence which of the packaging materials is determined as the innermost or the outermost packaging material.

By indicating the relevant packaging level, you specify whether the system is to determine the innermost packaging material or the

outermost packaging material (default value) when determining UPB rules.

## Related Information

Defining Package Type Assignments

Rule Profile for the Package Building Optimizer

Detailed Mixed Package Building

Reference Products for Package Building

## Test Cockpits for Unified Package Building

This is custom documentation. For more information, please visit SAP Help Portal.

56


1/14/26, 2:19 PM

## Defining Auxiliary Packaging Materials

Unified package building takes into account auxiliary packaging materials, such as filling material or slip sheets.

Depending on the unified package building engine you use, different auxiliary packaging materials are taken into account.

## Prerequisites

If you want auxiliary packaging materials to be treated and displayed as separate items in the item hierarchy, you have selected the

Include Auxiliary Packaging Materials in UPB Result checkbox in the unified package building profile. If you do not select this

checkbox, the weight and volume of auxiliary packaging materials are still taken into account during unified package building.

## Package Builder

If you perform unified package building using the package builder, the system takes into account the following auxiliary packaging

materials:

## Packaging materials per layer

These packaging materials are used if a separate packaging material is required for each product in a mixed package.

During package building, the system considers the weight and height of these additional packaging materials when

calculating the total weight and height of the package.

The system takes these packaging materials into account when building mixed packages based on layers.

## Separation materials

Separation materials are product-specific packaging materials that are placed on top of a product in a mixed package, for

example, slip sheets. During package building, the system considers the weight and the dimensions of this separation

material when checking the limits of the mixed package. You can indicate that a separation material is mandatory.

The system takes separation materials into account when building mixed packages based on layer and volume.

You define these packaging materials in the Change Package Type Assignment app. For more information, see Defining Package

Type Assignments.

## Packing Instruction and Packaging Specification

If you perform unified package building using the packing instruction or packaging specification, the system takes into account the

auxiliary packaging materials that you defined in the packing instruction or packaging specification.

For more information, see Packing with Packing Instructions and Packaging Specification.

## Related Information

Unified Package Building Profile

## Unified Package Building Engines

Unified package building (UPB) engines are alternative packaging approaches supported by unified package building. They use

different processing logics to create packages based on different sets of master data and Customizing settings.

The following unified package building engines are supported:

This is custom documentation. For more information, please visit SAP Help Portal.

57


1/14/26, 2:19 PM

Package building with the package builder

For more information, see Package Building.

## Packing instruction

For more information, see Packing Instruction.

## Packaging specification

For more information, see Packaging Specification.

  Note

In the test cockpits for unified package building, you can see, which packing instruction or packaging specification was used.

This information is provided in the Unified Package Building Rule field. The unified package building rule is an abstraction of

the used packing instruction or packaging specification, which both work based on rules. If you use package building as your

UPB engine, this field is empty because package building does not work based on rules.

  Note

You can enhance these UPB engines with the following Business Add-Ins (BAdIs):

BAdI: Enhancements for Package Building (/SCMB/EX_PB_ENGINE_PB)

BAdI: Enhancements for Packing Instruction (/SCMB/EX_PB_ENGINE_PI)

BAdI: Enhancements for Packaging Specification (/SCMB/EX_PB_ENGINE_PS)

## Related Information

Test Cockpits for Unified Package Building

## Package Building

You can use this function to create packages out of products.

## Use

Package building is performed with the Supply Chain Execution (SCE) package builder in SCM Basis. In the unified package

building profile, you need to select package building with the package builder as the unified package building engine.

During package building, the system bundles products into packages based on specific constraints, while also keeping the total

number of packages to a minimum. The system can also specify the exact position and orientation of each product item.

You can define these constraints for different combinations of product, business partner, equipment, and location. If several

constraints apply, the system always uses the most specific constraint. For more information, see Determination of Package Type

Assignments.

You can use the constraints that you define within this function to create packages in Transportation Management (TM) and in

Extended Warehouse Management (EWM).

For more information about creating packages in TM, see http://help.sap.com/s4hana under  Product Assistance

## Enterprise

Business Applications

## Supply Chain

 Transportation Management (TM)

## Planning

 Unified Package Building

## Unified

This is custom documentation. For more information, please visit SAP Help Portal.

58


1/14/26, 2:19 PM

Package Building in TM .

For more information about creating packages in EWM, see http://help.sap.com/s4hana under  Product Assistance

## Enterprise

Business Applications

## Supply Chain

 Extended Warehouse Management (EWM)

## Goods Issue

 Cartonization Planning

 Configuring Package Building .

## Prerequisites

You have defined product master data. For more information, see Defining Product-Specific Master Data.

You have defined package type assignments. For more information see Defining Package Type Assignments.

You have defined a unified package building profile and indicated Package Building as the unified package building engine

you want to use. For more information, see Unified Package Building Profile.

If you want to use mixed package building, you have optionally defined a product relationship profile in the Change Product

Relationship Profile app. In this profile, you can define incompatibilities and stacking rules. Moreover, you can define the

sequence in which the products are to be packaged.

If you want to use detailed mixed package building, you have done the following:

You have optionally defined a profile for the package building optimizer. This profile contains technical settings like

runtimes, dump and trace levels. To define this profile, enter view /SCMB/V_PB_OPT in transaction SM30.

You have optionally defined a rule profile for the package building optimizer. This profile allows you to select

predefined rules and define values and priorities. To define this profile, enter view cluster /SCMB/VC_PB_OPTRP in

transaction SM34. For more information, see Rule Profile for the Package Building Optimizer.

You have optionally defined a product orientation profile. In this profile, you define how a product can be positioned

in a package. To define this profile, enter view /SCMB/V_MAT_ORNT in transaction SM30.

## Features

When creating packages, the system can split the quantity of a product using the following criteria:

Quantity per package

Maximum height of the package

## Maximum weight of the package

If different products are to be packaged, the system considers the lowest maximum height and the lowest maximum weight for a

product or a packaging material. For example, if each product has a different maximum height, the system uses the lowest

maximum height.

The system creates mixed packages based on one of the following consolidation types:

## Volume

## Layer definitions

Incompatibilities, stacking rules, and product orientations (based on these values, the system determines the exact

positions of each product item in the package (detailed mixed package building))

The result of package building is different types of packages:

## Packages that contain only a single type of product

This is custom documentation. For more information, please visit SAP Help Portal.

59


1/14/26, 2:19 PM

Mixed packages that contain several different products

## Packages that consist of several layers

The layers within a package can also contain different products, which results in mixed layers.

## Nested packages, that is a package in another package

For example, you can plan 24 cans in one box and 100 boxes in ten layers on one pallet.

## Full packages or incomplete packages

Incomplete packages provide room for further consolidation.

## Flat or uneven packages

Flat packages are a prerequisite for stackability.

These package types can be combined. For example, the result of package building can be an incomplete, uneven mixed package

with mixed layers.

You can simulate the package building. For more information, see Test Cockpit for Unified Package Building.

You can check whether you have defined your package building constraints in a consistent way. For more information, see

Consistency Check of Package Building Constraints.

For more information about best practices and the processing logic, see SAP Note 2581421

.

  Note

You can use the Business Add-In BAdI: Package Building (/SCMB/EX_PACKAGE_BUILDER) to change the standard settings

of package building.

## Example

You have 105 laptops and 117 mini hi-fi systems. 90 laptops and 80 mini hi-fi systems form a complete package, while 10 laptops

and 16 mini hi-fi systems form one layer. If you allow mixed packages to be created with mixed layers, the system plans to put the

remaining 15 laptops and 37 mini hi-fi systems in a mixed package with one layer consisting of 10 laptops, two layers each

consisting of 16 mini hi-fi systems, and one mixed layer consisting of 5 laptops and 5 mini hi-fi systems.

## Related Information

Detailed Mixed Package Building

## Unified Package Building

## Defining Product-Specific Master Data

In the master data of a product, you define product-specific attributes that the system considers when creating packages.

## Procedure

To create a product, in the command field enter MM01.

On the  Additional Data

 Units of measure  view, define the following:

## Dimensions (length, width, height) of the product

This is custom documentation. For more information, please visit SAP Help Portal.

60


1/14/26, 2:19 PM

## Weight of the product

Definitions for full packages, that is, the product quantity that fits into one package as well as the height and weight

of the package

Definitions for full layers, that is, the product quantity that fits into one layer as well as the height and weight of the

layer

Maximum stacking factor (see Stacking Factor)

Maximum top load, that is, the maximum weight that you can place on top of a full package of this product

A conversion factor between the base unit of measure and the unit of measure for normalized quantity (see

Determination of Normalized Load Consumption Quantities).

Layer definitions are typically used for mixed packages. If you do not define any layer definition for your product, the

system creates packages based on the available volume of the packaging material.

You can define multiple layer and package definitions for a product. To do so, you need to define packaging-specific units of

measure in Customizing for SAP NetWeaver under  General settings

 Check Units of Measurement

. In the Change

Package Type Assignment app, you can indicate in which cases these different layer and package definitions are to be

used. For example, you can use different layer definitions for different business partners.

On the Sales: General/Plant view, define the following:

Maximum level (that is the filling level for volume-based mixed package building)

Stackability factor (see Stacking Factor)

Allowed packaging volume (for packaging materials only)

It is used to calculate the maximum height:

Max. height = all. pack. volume / ((max.) length * (max.) width)

The maximum height is needed to calculate the capacity volume, which is the main volume considered during

package building:

Capacity volume for closed packages = (max.) height * (max.) length * (max.) width

Capacity volume for open packages = (max. height – height of packaging material) * (max.) length * (max.) width

In addition, the existing maximum height values defined in the material master data and the Change Package Type

Assignment app need to be considered and the minimum is taken into account.

Closed (closed packaging material)

On the WM Packaging view, define settings for the packaging material. Note that these settings are only relevant if the
physical attributes of the packaging material are to be taken into account during package building. In this case, you need to
define a product for the packaging material and define the following settings:

## Maximum height and weight

Note that these are global limits that apply for your entire company, for example. You can set lower limits, for

example on a product-specific basis, in the Change Package Type Assignment app.

On the WM Packaging view, define settings for package building:

A reference product for package building

A product orientation profile

## The shape of the product

## Thresholds for overhang, and absolute height

This is custom documentation. For more information, please visit SAP Help Portal.

61


1/14/26, 2:19 PM

For more information, see the system documentation and SAP Note 2581421

.

## Related Information

Defining Package Type Assignments

## Stacking Factor

The stacking factor defines how products and packages, for example pallets, can be stacked.

The following logic applies:

A stacking factor of zero or an initial field means that the product or package can be stacked an infinite number of times on

itself.

A stacking factor of one means that the product or package can't be stacked on itself.

A stacking factor greater than one, such as six, means that the product or package can be stacked up to six times on itself.

On the  Additional Data

 Units of measure  view of the product master data, you can define a maximum stacking factor per

base unit of measure. If, for example, you define a maximum stacking factor of six for the alternative unit of measure of the

product (for example PC (Piece) or EA (Each)), it means that the product can be stacked up to six times on itself. This is taken into

account during detailed mixed package building. Detailed mixed package building also takes into account maximum stacking

factors that you have defined for reference products.

The maximum stacking factor that you define for the alternative unit of measure of the packaging material (for example PAL

(Pallet)) is determined in package building and taken into account during load planning and load consolidation. If you want the

packaging material to be marked as stackable, you need to specify a maximum stacking factor of zero or greater than one.

For closed packaging, only the stackability of the packaging material is relevant, the stackability of the products within the

packaging material does not matter. For example, a pallet cage is considered as the outer packaging and thus the system checks

the maximum stacking factor that you defined for the pallet cage and takes it into account during load planning and load

consolidation. If a product is packaged in a carton, the stackability of the carton is relevant for detailed mixed package building

since the carton will be packaged further.

If an open package, such as a pallet, contains layers only (no matter if these layers consist of the same product or different

products), the system takes into account and applies the maximum stacking factor (Units of measure view) that you have defined

for full packages of the contained products or the stackability factor (Sales: General/Plant view) that you have defined on product

header level. This is valid for layer-based mixed package building (embedded and based on detailed mixed package building).

  Note

If you have defined a stackability factor, the maximum stacking factor is not considered anymore.

An open package is only stackable if all contained products are stackable.

## Defining Package Type Assignments

By defining package attributes, for example the packaging material, you specify what kind of packages the system is to create for

your products.

This is custom documentation. For more information, please visit SAP Help Portal.

62


1/14/26, 2:19 PM
## Context

You have the following options:

You define package attributes for multiple different combinations of product, business partner, location, contained

material, and equipment.

You define package attributes for multiple different combinations of business partner, location, and equipment.

You define an exclusive package for a business partner.

You define alternative packaging materials and the sequence in which they are to be used. This allows you to define the

packaging material depending on the product quantity.

  Note

If you define more specific attributes for a specific product (first option), the system considers these attributes and ignores the

more global attributes (second option).

You can define the following package attributes:

## Packaging material and package type

Limits to be applied, for example, the maximum height and weight of the package

Note that the lowest limits (that is, the maximum height of the (mixed) package, the maximum weight of the (mixed)

package, and the maximum number of products) of all affected product items are considered.

Product-specific attributes, for example, a separation material or if mixed packages and mixed layers are to be created

In the Packaging Material field, you enter the product ID of the packaging material that you defined in the product master data.

This packaging material is used for full packages and mixed packages unless you have specified an additional product ID in the

Packaging Material (Mixed) field. In this case, all remaining product items are packaged in mixed packages using this additional

packaging material.

The package type can be either the packaging material, or the unit of measure, or both. You can enter the packaging material, or

the package type, or both:

If you only enter the packaging material and not the package type, the system uses the base unit of measure that you

defined in the product master data.

If you only enter the package type and not the packaging material, the weight and dimensions that you defined in the

product master data are not considered. The system only considers limits that you specify in this transaction.

If you enter both a packaging material and a package type, the system overrides the base unit of measure that you defined

in the product master data with the package type that you specify in this transaction.

If you want the system to create layers, you have to indicate a unit of measure for layers. If you do not indicate such a unit of

measure, the system creates packages based on your settings in the unified package building profile (either volume-based

package building or detailed mixed package building).

Some of these attributes can also be defined in the unified package building profile. However, the parameters in the unified

package building profile are global parameters and are taken into account only if you have not defined more specific attributes

here.

For more information about the individual attributes, see the system documentation.

For more information about best practices and the processing logic, see SAP Note 2581421

.

This is custom documentation. For more information, please visit SAP Help Portal.

63


1/14/26, 2:19 PM

To define package attributes, you need to do the following:

## Procedure

1. Open the Change Package Type Assignment app from the launchpad.

2. Define the package attributes.

Note that you have to define attributes on the Product-BP-Location tab page. The other tab pages are optional.

## Related Information

## Unified Package Building Profile

Determination of Normalized Load Consumption Quantities

## Determination of Package Type Assignments

During package building, the system determines package type assignments to decide how to best package a product.

The system always uses the most specific value that it can find for a parameter.

To determine this value, the system does the following:

1. The system checks if you have defined a value for a specific parameter on the Product-BP-Location tab page. On this tab

page, you define product-specific package attributes for different combinations of key fields, that is, product, business

partner, location, contained material, as well as equipment type and group.

2. If the system does not find a value or if you selected Undefined for the parameter on the Product-BP-Location tab page,

the system looks for a value on the BP-Location tab page. On this tab page, you define product-independent package

attributes for different combinations of key fields, that is, business partner, location, as well as equipment type and group.

3. If the system does not find a value for the parameter on the BP-Location tab page either, it uses the initial value (0).

If you also selected Undefined for the parameter on the BP-Location tab page, the system checks if you made a global

setting for the parameter in the unified package building profile.

4. If the system has found a package type assignment in one of the previous steps, it tries to find alternative packaging

materials for the corresponding key fields by applying the sequence defined on the Alternative Packaging Materials tab

page.

Note that the system can only determine alternative packaging materials, if you have deselected the No Mixed Packages

checkbox in the unified package building profile and if you have defined consistent physical dimensions and their

corresponding conversion factors in the material master.

5. On the BP tab page, the system checks if you indicated that an exclusive package is to be built for the business partner.

  Recommendation
Please use placeholder (*) for the key fields very carefully. For products and locations, we recommend that you use reference

products for package building and location hierarchies instead. For the contained material, you can't use placeholders.

If several products are to be packaged in the same way, we recommend that you define reference products for package

building. You define reference products for package building in the product master data.

If the same attributes apply for a large number of locations, we recommend that you define a location hierarchy in the

unified package building profile.

This is custom documentation. For more information, please visit SAP Help Portal.

64


1/14/26, 2:19 PM

  Note

The key fields Equipment Type and Equipment Group allow you to indicate the resource to which the product is

assigned.

You can use these fields if the way a product is packaged depends on the resource with which it is going to be

transported. For example, if you need to transport frozen goods, placing them on a pallet would be fine if the resource is

a refrigerated truck. If the resource is a regular truck, however, you would need to package the goods into a refrigerated

compartment.

## Related Information

Defining Product-Specific Master Data

Defining Package Type Assignments

## Unified Package Building Profile

## Determination of Normalized Load Consumption Quantities

During package building, the system determines normalized load consumption quantities (normalized quantities, NLQ) to get

accurate values regarding the load consumption of products and unit of measures (UoM) in top-level packages (that is, the outer

packaging). Based on these values, vehicle scheduling and routing optimization is able to choose the most suitable resources later

in the process.

To determine the normalized quantity for each product and UoM, the system does the following:

1. The system first checks if a value is available for each product and UoM in the Normalized Quantity field of the Define

Normalized Quantity app. These values can have the following source:

You have entered the values manually.

You have determined NLQs with the Determine Normalized Quantity Based on Randomized Data app. The results

are copied in this field automatically. For more information, see NLQ Determination Based on Randomized Data.

You have determined NLQs with the Determine Normalized Quantity Based on Documents app. The results are

copied in this field automatically. For more information, see NLQ Determination Based on Documents.

You have uploaded a spreadsheet that contains the values.

2. If the system finds an NLQ for a product and UoM, it multiplies this value with the planned quantity indicated in the freight

unit item for this product.

The system saves the results for all products in the freight unit items. In addition, it displays the sum of the normalized

quantities of all items on header level of the freight unit.

3. If the system does not find an NLQ in this field, it checks the product master data. If it finds a conversion factor between the

base UoM and the UoM for normalized quantity for a product and UoM, it uses this conversion factor to determine the

normalized quantity for this product.

4. If you have not defined conversion factors in the product master data, the system does not determine normalized

quantities during package building.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

65


1/14/26, 2:19 PM

The system only determines normalized quantities if you have defined a UoM for normalized quantity in your unified

package building profile.

In step 2 and 3, if the system finds an NLQ for a product and UoM, it uses this value. If it does not find an NLQ, it

continues to search from bottom to top in the product hierarchy, starting with the reference product at the lowest level.

## Related Information

Reference Products for Package Building

Use of Normalized Quantities and Capacities

NLQ Determination Based on Randomized Data

## Use

You can use this report to determine a value for the normalized load consumption quantity (normalized quantity, NLQ) per product

and unit of measure (UoM) by using a statistical approach. This value indicates how much space (footprint) a single product

consumes in a top-level package (that is, the outer packaging).

The report determines this value in the following way:

1. Based on your selection, the report creates SPBUs (that is, units created by separate package building) with a random

number of product items that contain a random quantity of products. Each SPBU represents a transportation demand, that

is, a set of goods that are transported together across the entire transportation chain within a specific period of time (for

example, one delivery day).

2. The report creates one CPBU (that is, a unit created by capacity-document-based package building) with an infinite

capacity for all product items of these SPBUs. The CPBU represents a transportation order.

3. The report performs package building based on this CPBU and builds the best possible packages.

4. Based on the package building results, the report calculates a value for the normalized quantity for each product.

5. The report repeats step 1-3 as many times as you have indicated (number of calculation runs).

6. By evaluating the values calculated during these calculation runs, the report determines a unique weighted value for the

normalized quantity per product.

## Prerequisites

You have defined dimensions for your products.

We recommend that you check the consistency of your package building constraints before you run this report. For more

information, see Consistency Check of Package Building Constraints.

For more information about prerequisites for package building, see Package Building.

Features

## Selection

You need to indicate the following:

This is custom documentation. For more information, please visit SAP Help Portal.

66


1/14/26, 2:19 PM

A UoM for the normalized quantity

A unified package building profile

## The number of calculation runs

The level on which normalized quantities are to be determined (on product level or reference product level, or both)

We recommend that products belonging to the same reference product have the same dimension.

The number of SPBUs, that is, the number of transportation demands (average and standard deviation)

The number of items to be created per SPBU (average and standard deviation)

The update mode, that is whether the system is to save the results or run the report in simulation mode (default setting)

The input mode, that is whether the report is to run based on the input options or based on a spreadsheet upload

At least one input option. For each input option, you can indicate the following:

## A product or reference product

The absolute frequency of the product (the relative frequency is determined by the system)

A product quantity per item (average and standard deviation)

By indicating more than one input options, you can influence the weighting of specific products related to one SPBU.

When you execute the report, the NLQ determination screen is displayed:

On the left, you can change the input data, for example, you can exclude certain products or change the quantities, and

then execute or schedule the NLQ determination.

On the right, the normalized quantities are displayed.

## Outputs

The report determines a value for the normalized quantity for each product, which is saved in the Normalized Quantity field of the

Define Normalized Quantity app, if you have indicated that the system is to save the results.

If you have executed the report in simulation mode, you can save the results by selecting Update Selected Normalized Quantities.

If the Define Normalized Quantity app already contains entries for combinations of product number and UoM for the normalized

quantity, these entries are overwritten.

## Activities

To start the report, open the Determine Normalized Quantity Based on Randomized Data app from the launchpad.

On the selection screen, choose  Program

 Execute in Background  to execute the report in the background. Note however,

that this is not supported if the input is based on spreadsheet upload. You need to execute the report based on spreadsheet upload

if you have more than five input options. On the NLQ determination screen, you can then schedule the NLQ determination for

execution in the background.

We recommend that you check afterwards whether the normalized quantities n your business documents are up to date. For more

information, see Check Normalized Quantities in Business Documents.

## Related Information

This is custom documentation. For more information, please visit SAP Help Portal.

67


1/14/26, 2:19 PM

Determination of Normalized Load Consumption Quantities

Unified Package Building Profile

Defining Package Type Assignments

## Detailed Mixed Package Building

You can use this function to create mixed packages for products.

## Prerequisites

You have installed the package building optimizer. For more information, see SAP Note 1686826

.

In your unified package building profile in Customizing, you have selected Detailed Mixed Package Building in the Mixed

Package Building Mode field. By doing so, additional fields are made editable, which allow you to make further settings. To

define a unified package building profile, enter view /SCMB/V_PB_PROFX in transaction SM30.

## Use

During package building, the package building optimizer creates mixed packages for products taking into account the constraints

you have defined. Moreover, it determines the exact position of each product item and its orientation.

The package building optimizer takes into account the following constraints:

Unified package building profile (settings for detailed mixed packaging)

## Package type assignments

Note that the lowest limits (that is, the the maximum height of a (mixed) package, the maximum weight of a (mixed)

package, and the maximum number of products) of all affected product items are considered.

Product-specific master data (settings for package building)

Product orientation profile

Product relationship profile

Profile for the package building optimizer

Rule profile for the package building optimizer

Related Information

## Package Building

Defining Product-Specific Master Data

Defining Package Type Assignments

Unified Package Building Profile

Rule Profile for the Package Building Optimizer

## Reference Products for Package Building

You can define reference products to simplify the process of defining package building attributes.

This is custom documentation. For more information, please visit SAP Help Portal.

68


1/14/26, 2:19 PM

If you have a group of products that need the same packaging attributes, you can define the attributes once for a reference

product and then assign the reference product to each product of the group. By doing so, all of the products inherit the attributes

of the reference product.

The following attributes can be defined for reference products:

Definitions for full packages

Definitions for full layers

Package type assignments

Incompatibilities

## Stacking rules

Consolidation sequence

  Note

You define full packages and full layers in the product master data. You define incompatibilities, stacking rules, and the

consolidation sequence in the product relationship profile.

When creating packages, the system first tries to create full packages with one product. If this is not possible, the system adds

other products from the group with the same reference product.

You can define reference products on more than one level.

  Note

If you want to change the reference product for multiple products, we recommend to use the test cockpit for unified package

building. For more information, see Test Cockpit for Unified Package Building.

## Related Information

Defining Package Type Assignments

Defining Product-Specific Master Data

Unified Package Building Profile

## Rule Profile for the Package Building Optimizer

SAP offers a number of predefined rules that you can use for detailed mixed package building. For each rule, you can indicate a

value and a level. Indicating levels allows you to define a hierarchy between several rules.

Rule Number

Rule Description

Explanation

1110

Minimize height difference on capacity (in

With this rule, you can minimize the height

mm)

differences of the surface of the package.

This objective is defined as standard

deviation of the heights of the different

cartonized or non-cartonized products that

form the surface of the package, weighted

by the sizes of these individual product

surfaces.

This is custom documentation. For more information, please visit SAP Help Portal.

69


1/14/26, 2:19 PM

Rule Number

Rule Description

## Explanation

You can indicate the deviation from the

standard deviation that the package

building optimizer is to reach. This value is

considered as a threshold, that means, all

height differences above are penalized. It is

always measured in millimeter.

3010

Minimize distance of center of mass from

With this rule, you can minimize the

capacity center

distance between the center of mass of the

load (that is, the products) and the center

of a package, for example, a pallet.

You can indicate a threshold value that

defines the maximum deviation above

which the package building optimizer

penalizes distances.

3020

Minimize height of center of mass on

With this rule, you can minimize the height

capacity

distance between the center of mass of the

load (that is, the products) and the bottom

side of a package, for example a pallet.

You can indicate a threshold value that

defines the maximum deviation above

which the package building optimizer

penalizes height distances.

Note that these rules only apply to top-level packages, that is, to the outer packaging.

## Consistency Check of Package Building Constraints

With this report, you can check whether you have defined your package building constraints in a consistent way.

## Use

Package building takes into account a wide range of constraints, such as master data and various profiles. When package building

is complete, you might wonder why the system has built packages in a certain way. This report lets you check your constraints to

discover any potential inconsistencies.

A number of individual checks are available. They are grouped in predefined categories, such as:

## Products

Package type assignments

Normalized quantities

## Integration

By selecting Open Ref. Mat. Hierarchy (Up) (Open Reference Material Hierarchy (Up)) in the check results area, you can directly

open the test cockpit for unified package building and analyze the product hierarchy. For more information, see Test Cockpit for

Unified Package Building.

This is custom documentation. For more information, please visit SAP Help Portal.

70


1/14/26, 2:19 PM
Features

## Selection

To run the report, you need to select the following:

A product, a reference product, or a range of products

## One or several check categories

Moreover, you can specify how the output should look. You can indicate whether the report is to focus on products or checks and

whether successful check results are to be displayed as well. Note that you can change these output settings on the consistency

checks screen after you have executed the checks.

When you execute the report, the consistency checks screen is displayed:

On the left, you can select the individual checks and execute them.

On the right, the check results are displayed.

## Output

The check results are displayed according to your output settings. A red check result indicates a critical inconsistency that might

lead to a package building run failure. A yellow check result indicates that the system might not build the packages as you expect

it.

From the check results area, you can directly open the following:

## Product master

Test cockpit for unified package building (see Integration)

Package type assignment transaction

## Activities

Enter transaction code /SCMB/CHECK_PB_CONS in the command field to start the report /SCMB/CHECK_PB_DEFINITIONS.

On the selection screen, choose  Program

 Execute in Background  to execute the report in batch mode. The system executes

all checks of the categories, which you selected.

## Related Information

Defining Package Type Assignments

Defining Product-Specific Master Data

## Packing Instruction

This unified package building (UPB) engine processes a set of master data that you have defined in your packing instruction. For

more information, see Packing with Packing Instructions.

In the UPB profile, you can define additional, UPB-specific parameters. For more information, see Unified Package Building Profile.

This is custom documentation. For more information, please visit SAP Help Portal.

71


1/14/26, 2:19 PM

UPB applies the following stackability logic. A top-level package item in the resulting packaging hierarchy is marked as stackable if

the following prerequisites are met:

The underlying rule contains a stacking factor of zero (or initial value) or greater than one.

The package is considered being complete.

If these prerquisites are not met, the top-level package item is considered as being non-stackable.

## Packaging Specification

This unified package building (UPB) engine processes a set of master data that you have defined in your packaging specification.

For more information, see Packaging Specification.

In the UPB profile, you can define additional, UPB-specific parameters. For more information, see Unified Package Building Profile.

## Test Cockpits for Unified Package Building

The test cockpits for unified package building allow you to simulate the building of packages and the determination of unified

package building rules. You can then analyze the result. You can also display and analyze the master data for products and display

products or reference products in the product hierarchy. The result shows the outcome of unified package building without any

additional processing in Transportation Management.

Two variants are available:

## Document-based test cockpit

For more information, see Test Cockpit for Unified Package Building (Document-Based).

## Product-based test cockpit

For more information, see Test Cockpit for Unified Package Building.

## Activities

To start the document-based test cockpit from the SAP Easy Access menu, choose  Transportation Management

## Administration

## Unified Package Building

 Unified Package Building - Test Cockpit (Document-Based)

.

You can also use the transaction code /SCMTMS/TEST_PLN_CPB.

To start the product-based test cockpit from the SAP Easy Access menu, choose  Transportation Management

## Administration

## Unified Package Building

 Unified Package Building - Test Cockpit

.

You can also use the transaction code /SCMB/TEST_UPB.

Test Cockpit for Unified Package Building (Document-Based)

With this report, you can simulate the building of packages and analyze the result. You can also display and analyze the master

data for products and display products or reference products in the product hierarchy. The result shows the outcome of unified

package building (UPB) without any additional TM-specific processing.

With this report you can do the following:

This is custom documentation. For more information, please visit SAP Help Portal.

72


1/14/26, 2:19 PM

You can simulate the building of packages out of business documents (for example freight orders).

Optionally, select a UPB profile. If you don't select a UPB profile, the system checks if a planning profile is defined, for

example in the corresponding freight order type, and if this planning profile contains a UPB profile.

The document-based test cockpit for UPB offers the same functionality as the Build Packages mode of the product-based test

cockpit for UPB. For more information, see Test Cockpit for Unified Package Building.

To start the document-based simulation of UPB from the SAP Easy Access menu, choose  Transportation Management

## Administration

## Unified Package Building

 Unified Package Building - Test Cockpit (Document-Based).

You can also use the transaction code /SCMTMS/TEST_PLN_CPB.

## Related Information

Unified Package Building in TM

## Package Building

Unified Package Building Profile

## Test Cockpit for Unified Package Building

With this report, you can simulate the building of packages and the determination of unified package building rules (UPB rules).

You can then analyze the result. You can also display and analyze the master data for products and display products or reference

products in the product hierarchy.

The test cockpit for unified package building (UPB) offers several execution modes. You can do the following:

Build Packages: Simulate the building of packages out of products and analyze the result

Determine UPB Rules: Simulate the determination of UPB rules and analyze the result

Read UPB Rules: Display the details of a UPB rule.

(Ref.) Prod. Hier: Top->Down/Bottom->Up: Display a hierarchy for products or reference products

Determine Pkg. Type Assignment: Display the package types assigned to a product or reference product

## Build Packages

You can simulate the building of packages out of products and analyze the result. You have the following options to start the

simulation:

## Select products by various product-based selection criteria

Select a UPB profile. The system executes UPB using the engine that you select in the unified package building profile.

Activate the 3D scene to display a 3D visualization of the packages that were built during UPB

Start the report with an empty input section and select products later

You can navigate to the product master data and change data, if needed.

Messages from the UPB, like error messages, warnings or success messages, are displayed to help you understand and analyze

the result of UPB.

This is custom documentation. For more information, please visit SAP Help Portal.

73


1/14/26, 2:19 PM

In the result, you can see, for example, which UPB engine and UPB rule (that is, packing instruction or packaging specification) the

system used. For more information, see Unified Package Building.

The simulation of UPB includes the following functions:

Function

Add products

Where to Find

Further Information

## Toolbar of input section

Insert rows to add (further) products to the

input list, then execute the simulation and

analyze the result.

Get Products per Reference Product

## Toolbar of input section

Add all products in one go to the input list

that are located below the entered

reference product.

Export/Import data

## Toolbar of input section

Download currently displayed input list.

Open Product Master

## Result section

Display Product Hierarchy (Bottom->Up)

## Result section

If you plan to upload data, you should first

download data, to get the data structure.

Double-click the icon to navigate to the

product master data. You can change the

data, if needed.

Double-click the icon to display all products

of the hierarchy that are above the entered

product.

## Determine UPB Rules

This execution mode determines UPB-engine specific UPB rules based on your settings in the UPB profile, such as the relevant

packaging level. For the UPB engines "packing instruction" and "packaging specification", the system determines the defined sets

of packaging master data and indicates their sequence (main UPB rule and alternative UPB rules). For the UPB engine "package

building", however, the system returns a dummy entry only.

From the result screen, you can select one of the determined UPB rules and start the Build Packages mode.

  Note

The UPB rule is an abstraction of the used packing instruction or packaging specification, which both work based on rules. If

you use package building as your UPB engine, the system does not determine UPB rules because package building does not

work based on rules.

## Read UPB Rules

This execution mode provides the details of UPB rules and their levels. You can use it to read information regarding the content of a

packing instruction or packaging specification.

## Display Hierarchy for Product or Reference Product

With the product hierarchy, you can display products (or reference products) and their location in the product hierarchy. Data like

product master data, package type assignment or the alternative unit of measure is displayed in the hierarchy. You can navigate to

the transactions and change the data, if needed.

You have the following options to start the product hierarchy:

This is custom documentation. For more information, please visit SAP Help Portal.

74


1/14/26, 2:19 PM

Hierarchy Bottom->Up: Show all (reference) products in a hierarchy tree that are located above the entered product.

Hierarchy Top->Down: Show all (reference) products that are located below the entered product. The entered product

serves as top node.

The product hierarchy includes the following functions:

Function

Add products

Where to Find

Further Information

## Toolbar of input section

Insert rows to add (further) (reference)

products to the input list and then display

the hierarchy trees of the added (reference)

products.

## Remove products

## Toolbar of input section

Remove rows to delete (reference) products

from the input list and then display the

hierarchy trees of the remaining (reference)

products.

Open Product Master

Result section (tree)

Double-click the icon to navigate to the

UoM

PTA

product master data. You can change data,

if needed.

Result section (tree)

Double-click the icon to display the

alternative unit of measure (UoM) of the

corresponding (reference) product.

Result section (tree)

Double-click the icon to display the package

type assignment of the corresponding

(reference) product.

Show Assigned Package Types

## Toolbar of result section

Mark one or several nodes to display the

package type assignment. The symbol in

column PTA shows if a package type is

assigned to a (reference) product.

Show Alternative UoM

## Toolbar of result section

Mark one or several nodes to display the

alternative unit of measure (UoM) of a

product.

Open Package Type Assignment

## Toolbar of result section

Navigate to the transaction where you can

## Transaction

define package type assignments for

products (/SCMB/PB_PKG_ASS).

## Show Alternative UoM

Toolbar of package type assignment section Mark one or several rows to display the

alternative unit of measure (UoM) of a

packaging material.

## Display Package Type Assignments

With this execution mode you can display the package types assigned to a product. Select your products by various product-based

selection criteria.

## Activities

To start the test cockpit for UPB (program /SCMB/TEST_PB), enter transaction code /SCMB/TEST_UPB in the command field.

This is custom documentation. For more information, please visit SAP Help Portal.

75


1/14/26, 2:19 PM

Note that when you select Execute on the selection screen of the Build Packages mode and the Determine UPB Rules mode, a

second screen is displayed that allows you to change your selection. You start UPB by selecting Build Packages on this second

screen. Similarly, you start the determination of UPB rules by selecting Determine UPB Rules.

## Related Information

Defining Product-Specific Master Data

Defining Package Type Assignments

Unified Package Building Profile

Reference Products for Package Building

Profiles and Settings

## Use

A number of profiles and settings are available with which you can perform transportation planning. You can use them to group

planning-relevant settings, for example, capacities and planning costs. The use of profiles and settings makes it easier for you to

start manual and automatic planning and is a prerequisite for VSR optimization in the background (see VSR Optimization).

## Features

The following is a list of the profiles and settings that are available to you:

## Profiles

Two profiles are available to which you can assign attributes and settings. These attributes and settings represent a type of

subprofile with its own ID that you define once and can then assign to multiple profiles.

Selection profile (see Selection Profile)

Time-related selection attributes

Geographical selection attributes

Additional selection attributes

Planning profile (see Planning Profile)

Capacity selection settings

Capacity availability settings

Settings for capacity document creation

Settings for manual planning

Scheduling settings

## Optimizer settings

Constraints and costs settings

Incompatibility settings

Settings for carrier selection

## Load planning settings

This is custom documentation. For more information, please visit SAP Help Portal.

76


1/14/26, 2:19 PM

Settings for unified package building

Settings for the transportation cockpit

Decreasing capacities (see Capacity Decrease)

Freight unit building rules (see Freight Unit Building Rule)

Incompatibilities and settings for incompatibilities (see Incompatibilities)

  Note

Note that the profiles and settings involve Customizing that you can transport into the production system.

You transport your profiles and settings by choosing the appropriate pushbutton and entering a transport request. If

your administrator has activated automatic change recording (transaction SCC4), a dialog box will automatically appear

if you make changes to your profiles and settings. Here you must select a transport request. The automatic change

recording ensures that all changes to profiles and settings are assigned to a transport request. We recommend that you

activate automatic change recording, otherwise it will be difficult for you to ensure consistency between the different

profiles and settings.

If profiles and settings are only to be changeable in the Customizing system and not in the production system, you must

control this via the corresponding roles.

The following authorization objects are relevant in this case:

T_PRF_CR for the creation of profiles and settings

T_PRFOPPID for the planning profile

T_PRFSELID for the selection profile

T_PRFINCID for incompatibility settings

T_FUBRID for freight unit creation rules

T_COND for conditions

Selection Profile

## Definition

A user-specific grouping of business documents (that is, forwarding orders, freight units, and freight orders) that is taken into

account during transportation planning.

## Use

The system takes into account the settings that you make in the selection profile during manual planning, during VSR

optimization, during planning in the background, and during carrier selection.

  Note
You can define an authorization check for the change and usage requirements of each selection profile. You can configure the

relevant settings using authorization object T_PRFSELID.

This is custom documentation. For more information, please visit SAP Help Portal.

77


1/14/26, 2:19 PM
## Structure

In the selection profile and in the assigned selection attributes, you define which business documents the system is to take into

account as well as the maximum number of documents. You can assign the following selection attributes to a selection profile:

## Time-related selection attributes

Here you define the demand horizon, for example (see Demand Horizon).

## Geographical selection attributes

Here you define source and destination locations, for example.

## Additional selection attributes

Here you define additional attributes for database queries (see Additional Selection Attributes).

You can use your selection profile as follows:

As a selection profile for freight units

The system uses the profile to select freight units.

## As a selection for freight orders and freight bookings

The system uses the profile to select existing freight orders and freight bookings that are to be taken into account in

planning.

This means that the selection of business documents made by the system depends on where and how you use your selection

profile. For example, if, when calling the transportation cockpit, you specify your selection profile as a selection profile for freight

units in your profile and layout set (see Use of Profile and Layout Sets), the system selects freight units. However, if you specify

your selection profile as a selection profile for freight orders and freight bookings, the system selects freight orders and freight

bookings.

  Note

To define selection profiles, open the Create Selection Profile app on the launchpad.

Note that the selection criteria in the geographical and additional selection attributes have an effect on performance.

Demand Horizon

## Definition

Period containing all demands that are to be taken into account in planning.

## Use

You define the demand horizon in the time-related selection attributes that you assign to your selection profile (see Selection

Profile). You can define a demand horizon for pickup and a demand horizon for delivery. The system chooses all freight units and

freight orders whose pick-up date/time or delivery date/time lies within the relevant demand horizon.

## Structure

You can define the demand horizon as absolute or relative:

This is custom documentation. For more information, please visit SAP Help Portal.

78


1/14/26, 2:19 PM

## Absolute

You define the demand horizon precisely by defining a start and end date and a start and end time.

## Relative

You do not define the demand horizon with precise dates and times, but specify instead a duration starting from the

current date. The system then automatically determines the start and end date and the start and end time. If the demand

horizon is not to start on the current date, but instead at a later time, you can define an offset. According to this, the relative

demand horizon is defined as follows:

## Start of demand horizon = current date + defined offset

Here, the offset is made up of the offset in days and the additional offset (in hours and minutes).

End of demand horizon = start of demand horizon + defined duration of demand horizon

Here, the duration of the demand horizon is made up of the duration in days and the additional duration (in hours

and minutes).

If you specify a factory calendar, the system takes into account non-working days when calculating the start of the horizon.

In this case, the planning horizon always begins on a working day.

You can simulate the relative demand horizon. You enter a reference date that the system uses to determine and display the

start and end date and the start and end time for the pick-up or delivery.

## Relative horizon with a fixed start time or a fixed end time

You define a relative demand horizon as described above. You also enter a fixed start time as of which you want the horizon

to start or a fixed end time by which you want the horizon to end. You can also simulate this demand horizon.

The following figure shows how the demand horizon is defined:

This is custom documentation. For more information, please visit SAP Help Portal.

79


1/14/26, 2:19 PM

## Demand Horizon

Additional Selection Attributes

## Use

To restrict the selection of requirements data even more specifically, you can define additional attributes for database queries.

## Features

Definition of Additional Attributes for Database Queries

Here you define an additional filter for certain business documents:

Business documents in forwarding order management (forwarding orders, forwarding quotations, order-based

transportation requirements and delivery-based transportation requirements)

Business documents in freight order management (freight orders, freight bookings, consignment orders, transportation

units, freight units)

## Activities

To define additional selection attributes, open the Create Additional Selection Attributes app on the launchpad.

This is custom documentation. For more information, please visit SAP Help Portal.

80


1/14/26, 2:19 PM

To assign your additional selection attributes to a selection profile, open the Edit Selection Profile app on the launchpad and then

open the required selection profile.

Planning Profile

## Definition

A user-specific grouping of parameters that are taken into account during transportation planning.

## Use

The system takes into account the settings that you configure in the planning profile during manual planning, load planning, and

VSR optimization (interactive and in the background; see VSR Optimization).

  Note

You can define an authorization check for the change and usage requirements of each planning profile. You can

configure the relevant settings using authorization object T_PRFOPPID.

A planning profile is selected as a standard profile. If the system does not find a planning profile, it uses the values from

this standard profile.

## Structure

The planning profile comprises a range of settings (subprofiles) for which own apps are also available. The planning profile and the

settings are described below.

## Planning Profile

In the planning profile, you define the following, for example:

Planning horizon (see Planning Horizon)

## Subprofile assignments

Here you assign existing settings and selection profiles to your planning profile. You can also create new subprofiles from

scratch or by copying an existing subprofile. For each assigned subprofile (except selection profiles and carrier selection

settings), you can specify whether profile data can be changed during planning sessions.

## Parallel processing profiles

Here you can enter parallel processing profiles for different functions, such as distance and duration determination.

Planning strategies (see Process Controller Configuration)

You can either specify the standard strategy or use your own strategy. You can add additional methods to the standard

strategy.

Manual planning (standard strategy VSRI_SCH)

You define this strategy in the manual planning settings.

Scheduling (standard strategy VSS_EMBED)

You define this strategy in the scheduling settings.

This is custom documentation. For more information, please visit SAP Help Portal.

81


1/14/26, 2:19 PM

Checks (standard strategy VSR_CHECK)

The system checks capacities, incompatibilities, and multiresources, and it performs a dangerous goods check.

VSR optimization (standard strategies VSR_DEF and VSR_1STEP)

You define this strategy in the optimizer settings.

Load planning (standard strategy ALP_DEF)

You define this strategy in the settings for load planning.

Generating transportation proposals (standard strategies VSR_DEF and VSR_1STEP)

You define this strategy in the optimizer settings.

Integrating real-time execution data (see Integration of Real-Time Execution Data)

## Handling empty stages

Here you specify how the system is to handle empty transportation stages when solving warnings about missing

transportation stages in the Gantt chart (see also "Settings for manual planning" below).

## Capacity Selection Settings

Here you choose the required capacities, such as resources. If you use resources for which you have defined an ADR limit, VSR

optimization takes into account the number of ADR points for this resource during the optimization run (see ADR 1.1.3.6 Points

Check Calculation). Moreover, you can specify that resources for which you have set a planning block are displayed in the resource

lists of the transportation cockpit.

If you want to carry out your planning based on equipment types, enter your vehicle and container types here under Vehicle Types

and Container Types. For more information, see Planning Based on Equipment Types.

## Capacity Availability Settings

Here you can restrict the availability of resources and equipment types. Using rules that you define here, the system determines

when certain resources or equipment types are available based on shift sequences and factory calendars. For more information

about planning based on equipment types, see Planning Based on Equipment Types.

You can also assign driving and working constraint profiles to your vehicles (truck resources or vehicle types) and drivers. For more

information, see Considering Driving Time and Working Hours Constraints.

## Capacity Document Creation Settings

Here you can specify a standard business document type or a condition with which the business document type is to be

determined.

Moreover, you can enter a requirement grouping profile that is used to create capacity documents based on requirement groups.

For more information, see Creation of Capacity Documents Based on Requirement Groups.

## Optimizer Settings

For example, you can define the following here:

## Optimizer runtime

Maximum number of transshipment locations and processes

Freight order building rule (see Freight Order Building Rule)

This is custom documentation. For more information, please visit SAP Help Portal.

82


1/14/26, 2:19 PM

## Required process controller strategy

Settings for generating transportation proposals (see Generation of Transportation Proposals)

Settings for incremental planning (see Incremental Planning)

Whether you require rough or detailed information for your planning activities (see Rough-Cut Planning)

Whether the system is to consider a subsequent planned transportation stage as a hard time constraint

## Whether freight orders that are ready for execution or in execution can be changed

How default routes are to be used when freight units, container units, railcar units, and package units are processed in the

## VSR optimization run

In the advanced settings, you can also specify whether the main aim in your transportation proposals is to ensure the lowest

transportation costs possible or the shortest transportation duration possible based on the planned delivery date/time. You can

also define preferences in relation to your relative weighting of the variance of carriers, routes, and departure dates, or activate or

deactivate capacity constraints at transportation mode level. You can also specify whether the system is to ignore certain settings

such as the capacity or ADR limit of a resource during VSR optimization.

Unified Package Building Settings

## Unified package building

Here you enter a unified package building profile and a profile for parallel processing. You can also specify whether the

items are to be filtered (for example, outbound delivery only or pick-up only). In this way, you can filter out returns and leave

them unpackaged, for example. For more information, see Unified Package Building in TM.

## Creating package units based on unified package building for freight units

Here you enter a default package unit type (mandatory) and a default rule for the creation of package units (optional). In

addition, you can enter a package unit type for package units with only one destination location and a corresponding rule.

These settings are taken into account if the system creates first packages and then package units for freight units for which

you have selected Exclusive Package for Customer. This means that the package units only receive products for a specific

customer. To use the function, you must also enter a unified package building profile. For more information, see Use of

Package Units in Planning.

## Load Planning Settings

Here you can define the optimizer runtime, the planning strategy, and various rules for load planning. For example, you can define

the maximum height difference between stacks in a row.

## Constraints and Costs Settings

Here you define costs related to freight units and means of transport. In most cases, these costs are not actual costs. They simply

offer a means of controlling the result of the optimization run (for example, earliness costs and lateness costs). For more

information, see Constraints and Costs Settings.

## Incompatibility Settings

Here you define settings for your incompatibilities (see Incompatibilities).

You can also specify whether the constraints for loading (loading direction and attached equipment) are to be taken into account

in VSR optimization, load planning and load consolidation, and for the creation of transportation proposals. The system considers

these as incompatibilities between location and resource. For manual planning, you can specify whether the system is allowed to

violate the incompatibilities or not or whether it should issue a warning if they are violated.

This is custom documentation. For more information, please visit SAP Help Portal.

83


1/14/26, 2:19 PM

As soon as you define these constraints, we recommend that you add the profiles for loading direction and attached equipment to

the locations and vehicle resources that are to take these constraints into account. For more information about defining profiles

for loading direction and attached equipment, see Loading Requirements for Locations and Loading Requirements for Vehicle

Resources.

## Carrier Selection Settings

Here you specify whether the system is to use transportation allocations or business shares, for example.

## Manual Planning Settings

Here you specify how you want the system to behave when it assigns documents and resources:

## Assignment of documents

You use these settings to control how the system is to assign one or more requirement documents to a capacity document.

For more information, see Assignment of Requirement Documents to Existing Capacity Documents.

## Removal of the assignment of documents

You use this setting to control how the system is to remove the assignment of requirement documents to capacity

documents.

## Assignment of resources and creation of documents

You use these settings to control how the system is to assign resources to documents and how it is to create and assign

reference documents.

## Assignment of drivers

You use this setting to control whether a default truck is to be assigned together with the default driver.

## Solving of warnings

You use this setting to control how the system is to handle empty transportation stages when solving warnings about

missing transportation stages in the Gantt chart.

For more information, see the corresponding field help.

## Scheduling Settings

Here you can control how the system schedules documents. For example, you can define loading and unloading durations,

coupling and uncoupling durations, and the durations required to prepare and finalize a stop based on locations and resources.

You can specify whether driving time and working hours constraints are to be considered. For more information, see Considering

Driving Time and Working Hours Constraints. You can also override operating times to be used for a location based on the

resource. For more information, see Consideration of Scheduling Constraints.

## Transportation Cockpit Settings

Here you define settings that control the behavior of the transportation cockpit. For example, you can activate context

determination for the selection. For more information, see Context Determination. You can also specify that your selection is to be

deleted after an action has been executed successfully. For more information, see SAP Note 3181915

.

## Activities

To define a planning profile, open the Create Planning Profile app on the launchpad.

This is custom documentation. For more information, please visit SAP Help Portal.

84


1/14/26, 2:19 PM

Planning Horizon

## Definition

Planning period in which transportation activities are to be executed.

## Use

You define the planning horizon in the planning profile (see Planning Profile). The planning horizon defines the possible period of

time in which the system can schedule transportation activities (for example, loading and unloading, transport).

## Structure

You can define the planning horizon as absolute or relative:

## Absolute Planning Horizon

Enter a start and end date and a start and end time.

## Relative Planning Horizon

You do not define the planning horizon with precise dates and times, but enter instead a duration starting from the current date.

The system then automatically determines the start and end date and the start and end time. If the planning horizon is not to start

on the current date, but instead at a later time, you can define an offset. Here you can specify whether the system is to round the

planning horizon to complete days. For the planning horizon, you can specify the time zone in which the system is to calculate the

horizon.

According to this, the planning horizon is defined as follows:

## Start of planning horizon = current date + defined offset

Here, the offset is made up of the offset in days and the additional offset (in hours and minutes).

End of planning horizon = start of planning horizon + defined duration of planning horizon

Here, the duration of the planning horizon is made up of the duration in days and the additional duration (in hours and

minutes).

If you specify a factory calendar, the system takes into account non-working days when calculating the start of the horizon. In this

case, the planning horizon always begins on a working day.

You can simulate the relative planning horizon. You enter a reference date that the system uses to determine and display the start

and end date and the start and end time.

## Relative Planning Horizon with a Fixed Start Time or a Fixed End Time

You define a relative planning horizon as described above. You also enter a fixed start time as of which you want the horizon to start

or a fixed end time by which you want the horizon to end. You can also simulate this planning horizon.

  Recommendation
You always define the planning horizon in the future. Otherwise, the system takes into account documents that lie in the past,

which can lead to performance problems. You can define a planning horizon in the past to correct documents that lie in the

This is custom documentation. For more information, please visit SAP Help Portal.

85


1/14/26, 2:19 PM

past, for example. However, we recommend in this case that you define a separate planning profile with its own planning

horizon that takes the past and the future into account.

The following figure shows how the planning horizon is defined:

## Planning Horizon

Constraints and Costs Settings

## Use

You can define freight-unit-dependent and equipment-dependent costs and constraints. These costs do not refer to real costs.

They can be used to influence the optimization run so that certain solutions are prioritized. By defining higher lateness costs than

earliness costs, for example, you can indicate that delivering earlier than requested is the preferred solution (see VSR Optimization

and Load Consolidation).

## Features

## Requirement Document-Dependent Costs

These are non-delivery costs as well as earliness costs and lateness costs that the system calculates for each requirement

document used in the VSR optimization run.

  Note

VSR optimization understands requirement documents to be freight units, container units, railcar units, and consignment

orders.

This is custom documentation. For more information, please visit SAP Help Portal.

86


1/14/26, 2:19 PM

You can enter non-delivery costs, earliness costs, and lateness costs directly or by specifying a condition (see Condition) with the

condition type /SCMTMS/FU_PNLT_COST.

Equipment-Dependent Costs

## Fixed Costs

These are costs that the system calculates once for each capacity (for example, vehicle type or schedule) used in the VSR

optimization run.

  Note

For schedules, the fixed costs are incurred per departure.

  Recommendation

You can use fixed costs for each capacity document and optionally combine them with variable costs to estimate the

effort required when using different equipment types.

Example: You want to transport one freight unit that fits into two vehicle types. If you define fixed costs for each capacity

document, you can influence the optimization result in such a way that the smaller vehicle type is selected.

If you want to influence the optimization result so that as few vehicle resources are used as possible, we recommend

that you define fixed costs for each vehicle resource.

In VSR optimization, the costs are applied for each instance of a vehicle resource:

The VSR optimizer adds the costs once for each single resource to which at least one freight order is assigned

within the planning horizon. This means that these costs are not added again when another freight order is

assigned.

In the case of multiresources and equipment types, VSR optimization ignores these fixed costs because freight

documents on multiresources and equipment types are independent of each other and the number of instances

is usually unlimited.

You can find an example in the input help.

## Dimension-Relevant Costs

These are variable transportation costs per unit for the following dimensions:

Time (duration)

## Distance

Transported quantity per distance

## Intermediate stop

These costs refer to the use of the dimensions of a capacity (including empty runs) during the VSR optimization run.

These costs and constraints are described in detail in the following sections:

## Costs per duration

The costs per duration define the time-dependent costs that are calculated per unit of measure for a specific means of

transport during VSR optimization. You can also define a maximum duration of an order.

This is custom documentation. For more information, please visit SAP Help Portal.

87


1/14/26, 2:19 PM

You can also define the maximum duration between the first and last pick-up stop and the maximum duration between the

first and last delivery stop that the VSR optimizer must consider when creating a freight order or a trailer unit using this

means of transport. In this way, you can control that all pick-up or delivery stops are served within a certain time period,

such as on the same day.

## Costs per distance

The costs per distance define the distance-related costs that are calculated per unit of measure for a specific means of

transport during VSR optimization. You can choose from various cost bases. You specify whether the system is to use the

costs per distance from the planning costs in the planning profile (that is, from the Distance Costs per Unit of Measure

field) or from the transportation lane. Alternatively, you can specify that the system takes into account the total of both

values.

If the system is to take into account the distance costs from the planning profile or from the planning profile and the

transportation lane, you can define a maximum value and unit. The unit refers to both the costs and the maximum value. If

you do not specify a unit, the system uses the unit Kilometer.

  Example

You want to model a case where means of transport MT1 is to be used everywhere and with constant costs per distance.

Means of transport MT2 is to be used primarily in region A, and it is to be used in region B for bottleneck situations.

Therefore, choose Yes in the Consider Distance Costs from Constraints and Costs Settings field (calculation basis:

planning costs) for MT1, and define distance-dependent costs per unit of measure. You choose No in the Dist. Costs

from Transportation Lane field.

For MT2, you choose No in the Consider Distance Costs from Constraints and Costs Settings (calculation basis:

planning costs), and Yes in the Distance Costs from Transportation Lane field.

In this case, the system adds the costs from the planning costs and the costs from the transportation lane.

If the system is to take into account the distance costs from the transportation lane only, you can choose between two

types of distance costs, each of which applies a different geographical basis in its calculation logic:

## Route-based distance costs

Route-based distance costs are determined using a calculation logic that adds up the costs for the transportation of

the goods from the source location to the destination location via a number of transshipment locations based on

the costs for each stage.

## Destination-based distance costs

Destination-based distance costs are determined using a calculation logic that adds up the distances between the

source and target locations, including all distances between transshipment locations, and multiplies the result by a

cost factor. This cost factor is part of the direct transportation lane between the source location and target location

and is based on the geographical location of the destination. The probability that the destination location of a

transportation is the source location of the next transportation determines the value of the cost factor.

  Note
You must have defined a direct transportation lane between the source location and the target location before

the system can take this calculation logic for distance costs into account in the VSR optimization run.

  Example

You want to transport goods from New York City to Minneapolis via Chicago. The distance between New York and

Chicago is 800 and the distance between Chicago and Minneapolis is 400. The total distance that the system is

to take into account in the VSR optimization run, for both the route-based distance costs and the destination-

based distance costs, is therefore 1200 (800 + 400).

This is custom documentation. For more information, please visit SAP Help Portal.

88


1/14/26, 2:19 PM

In the case of the route-based distance costs, the cost factor for the transportation of the goods from New York

to Chicago is 3. The cost factor for the transportation of the goods from Chicago to Minneapolis is 4.

In the case of the destination-based distance costs, the cost factor for the transportation of the goods from New

York to Minneapolis is 2.

If you select route-based distance costs for your VSR optimization run, the system calculates the transportation

charges as follows: 800*3 + 400*4 = 4000.

If you select destination-based distance costs for your VSR optimization run, the system calculates the

transportation charges as follows: (800 + 400)*2 = 2400.

You can also define the maximum distance between the first and last pick-up stop and the maximum distance between the

first and last delivery stop that the VSR optimizer must consider when creating a freight order or a trailer unit using this

means of transport. In this way, you can control that all pick-up or delivery stops are within a specific radius. Here, too, the

system uses the unit Kilometer if you do not specify a unit.

## Costs per quantity

You define the costs per quantity for each VSR optimization run. You must also define a unit. You cannot define a maximum

value for the costs per quantity. However, you can specify the cost basis, in other words, whether the system is to use the

costs per quantity from the transportation lane or from the schedule, or from the planning costs of the planning profile

(that is, from the Costs per Quantity field).

In the case of costs per quantity from the transportation lane or the schedule, you can specify whether the system is to

calculate the costs in a distance-independent way or whether it is to multiply them by the distance.

For nonscheduled means of transport, you take the costs per quantity from the transportation lane. For a means of

transport of a schedule, you take the costs per quantity from the schedule.

In the case of costs per quantity from the planning costs, you can specify whether the system is to calculate the costs per

freight document stage (in a distance-independent way) or whether it is to multiply them by the distance.

  Example
The following example shows how the system calculates the costs in the case of costs per quantity from the planning

costs per freight document stage (in a distance-independent way):

You want to transport a freight unit (FU) with a weight of 10 kg from A to B. You have defined costs of 5 per KG. In this

case, the system calculates costs per quantity to the amount of 50.

If you transport the FU from A via C to B, the system calculates costs per quantity to the amount of 100, in other words,

50 per stage.

Costs per intermediate stop

You can define the following:

Maximum number of intermediate stops

Costs per intermediate stop

Maximum number of pickup stops

Maximum number of delivery stops

## Utilization

You can enter in percent the minimum target utilization of a means of transport that is to be taken into account for the generation

of road freight orders during the VSR optimization run. Moreover, you can specify whether this utilization should be a hard or soft

This is custom documentation. For more information, please visit SAP Help Portal.

89


1/14/26, 2:19 PM

constraint.

## Cost Factors for Penalty Costs

You can use these cost factors to weight the earliness and lateness costs that you have defined for each freight unit on the basis of

the means of transport. The VSR optimization multiplies these cost factors by the earliness costs or lateness costs of each freight

unit. The following cost factors are available:

Cost factor for premature pickup

Cost factor for delayed pickup

Cost factor for premature delivery

Cost factor for delayed delivery

  Note

You define earliness costs and lateness costs by either entering them directly or by specifying a condition with the condition

type /SCMTMS/FU_PNLT_COST. You specify this condition when you define time windows for the pickup and delivery. You

must then assign these time windows to a planning profile.

For more information, see Time Windows.

## Costs for Greenhouse Gas Emissions

You can define costs for greenhouse gas emissions (measured in CO  equivalents) to set the priority of such emissions during VSR

2

optimization.

For more information, see Greenhouse Gas Emissions.

## Capacity Adjustment

You can define adjustment factors for mass, volume, and normalized quantity. These factors determine to what extent the actual

vehicle capacity available for planning can be increased or reduced. These factors are considered in VSR optimization and when

generating transportation proposals. They are not considered for the following:

Manual planning

## Schedules

Load consolidation

Capacity decrease

## Compartments

## Combinations of vehicle resources

For the adjustment factor for the normalized quantity, you have to define a unit of measure for the normalized quantity in the

settings for the transportation cockpit.

## Activities

To define constraints and costs settings, open the Create Constraints and Costs Settings app on the launchpad.

This is custom documentation. For more information, please visit SAP Help Portal.

90


1/14/26, 2:19 PM

To assign your constraints and costs settings to a planning profile, open the Edit Planning Profile app on the launchpad, and then

select the required planning profile.

Freight Order Building Rule

## Use

The system takes into account freight order building rules when creating and changing more than one freight order on one

resource during VSR optimization (VSR = Vehicle Scheduling and Routing).

You use freight order building rules to control how the system assigns activities on one resource to different freight orders.

## Features

VSR optimization can build freight orders according to the following rules:

## New Freight Order when Resource Is Empty

VSR optimization creates a new freight order if the resource is empty, that is, no freight units and no trailers are assigned to

the resource.

Note that if one or several outbound freight units are assigned to a freight order and there is one consecutive inbound

freight unit that is delivered to the source location of the freight order, the freight order also contains the transportation

stage of the resource to which the inbound freight unit is assigned.

## New FO when Resource Is Empty and Depot Location Reached

VSR optimization creates a new freight order when the following prerequisites are met:

The resource is empty, that is, no freight units and no trailers are assigned to the resource.

The resource has reached the depot location.

  Note

An exception to these rules are schedules. The system creates a freight order for every departure of a schedule. Empty

runs within the route of the schedule are part of the freight order as well.

If you have selected Empty Stage Should Be Last Stage of Capacity Document in the Preferred Position of Empty

Stage field in your planning profile, the empty stage is added to a preceding freight order even if this means that the new

freight order doesn't start directly after the resource is empty but after the empty stage.

## Activities

You can define freight order building rules in the Optimizer Settings screen area of a planning profile (see Planning Profile).

## Example

For examples of how the system builds freight orders depending on the freight order building rule, see Examples of Freight Order

Building Rules in Use.

## More Information

This is custom documentation. For more information, please visit SAP Help Portal.

91


1/14/26, 2:19 PM

## VSR Optimization

## Examples of Freight Order Building Rules in Use

The following examples demonstrate how the system builds freight orders for a given set of freight units based on the selected

freight order building rule.

Example 1

You have the following freight units:

Freight Unit

From

To

1

2

3

A

C

E

B

D

F

You have a resource with enough capacity and a depot location.

The figure below illustrates the transportation plan that a truck uses to transport the freight units, as well as the empty runs, and is

followed by an explanation:

The truck uses the following transportation plan to transport the freight units:

This is custom documentation. For more information, please visit SAP Help Portal.

92


1/14/26, 2:19 PM

It starts at the depot location and drives to location A without any load (empty run). At location A, freight unit 1 is loaded onto the

truck. The truck then drives to location B, where freight unit 1 is unloaded. The truck continues to location C without any load

(empty run). At location C, freight unit 2 is loaded onto the truck. The truck then drives to location D, where freight unit 2 is

unloaded. After that, the truck returns to the depot location without any load (empty run).

The truck then drives to location E without any load (empty run). At location E, freight unit 3 is loaded onto the truck. The truck

then drives to location F, where freight unit 3 is unloaded. Finally, the truck returns to the depot location without any load (empty

run).

The system builds the following freight orders depending on which freight order building rule you have selected:

New Freight Order when Resource Is Empty

The system builds the following freight orders:

Freight order 1 that contains freight unit 1.

Freight order 2 that contains freight unit 2.

Freight order 3 that contains freight unit 3.

New FO when Resource Is Empty and Depot Location Reached

The system builds the following freight orders:

Freight order 1 that contains freight unit 1 and freight unit 2.

Freight order 2 that contains freight unit 3.

Example 2

You have the following freight units:

Freight Unit

From

1

2

3

A

A

C

To

B

C

A

## Comment

This freight unit is an outbound

freight unit.

This freight unit is an outbound

freight unit.

This freight unit is an inbound

freight unit. It contains an

empty crate that needs to be

returned to location A.

You have a resource with enough capacity for transporting the freight units. Further, you have selected the following freight order

building rule:

## New Freight Order when Resource Is Empty

The figure below illustrates the transportation plan that a truck uses to transport the freight units and is followed by an

explanation:

This is custom documentation. For more information, please visit SAP Help Portal.

93


1/14/26, 2:19 PM

The truck uses the following transportation plan to transport the freight units:

At location A, freight unit 1 and 2 are loaded onto the truck. The truck drives to location B, where freight unit 1 is unloaded. The

truck then drives to location C where freight unit 2 is unloaded and freight unit 3 is loaded onto the truck. The truck then returns to

location A, where freight unit 3 is unloaded.

The system builds one freight order for the roundtrip that contains freight unit 1, 2, and 3.

Capacity Decrease

## Use

When you transport goods for multiple customers on a vehicle resource (including passive vehicle resources), in other words, the

vehicle resource stops at multiple intermediate stops on the way from the source location to the destination location, you can use

partitions to separate the goods. However, this results in a reduction of the total capacity of the vehicle resource since each

partition consumes capacity itself. You can use this function to define how the capacity is to decrease.

  Note

This function refers only to the capacity of the vehicle resource. It is independent of compartments (see Compartment)

that you have defined for the vehicle resource.

You define decreasing capacities once for your system. You do not assign them to a profile.

You cannot define decreasing capacities for schedule vehicles.

Features

## Fixed Value

You can define a fixed value or a percentage by which the capacity is to decrease for each loading-relevant intermediate stop where

loading, unloading, or transshipment activities take place. The system continues to reduce the capacity for the VSR optimization

(see VSR Optimization) until one of the following conditions is met:

This is custom documentation. For more information, please visit SAP Help Portal.

94


1/14/26, 2:19 PM

The total capacity is consumed, in other words, it is zero.

The maximum number of intermediate stops defined for the means of transport has been reached (user interface for the

definition of planning costs).

The maximum number of intermediate stops defined for the capacity decrease (end of intermediate stop area) has been

reached.

## Single Values

You can define a value by which the capacity is to decrease for a specific number of loading-relevant intermediate stops. If you do

not define a value for a certain number of loading-relevant intermediate stops, the capacity remains the same.

  Note

Note that in both cases the capacity decrease refers to the capacity that the vehicle resource has before the transportation

start, in other words, the capacity with which you can load the vehicle resource at the source location.

## Activities

To define capacity decreases, open the Create Decreasing Capacity Settings app on the launchpad.

## More Information

Definition of Decreasing Capacities

Definition of Decreasing Capacities

You have defined the following data:

Means of transport 0001

## Load unit KG

Vehicle resource RES1 with means of transport 0001 and a capacity of 10,000 kg

## Fixed Value or Fixed Percentage

If you want to use a fixed percentage, specify the following values for the capacity decrease:

TM

Load Unit

Stop Range:

Stop Range: End

Value Type

0001

KG

Start

2

Capacity

Decrease

Percentage

11

Fixed Value

10

## Capacity

Decrease Is a

## Percentage

If you want to use a fixed value, specify the following values for the capacity decrease:

This is custom documentation. For more information, please visit SAP Help Portal.

95


1/14/26, 2:19 PM

TM

Load Unit

Stop Range:

Stop Range: End

Value Type

Capacity

Decrease

Percentage

11

Fixed Value

1000

## Capacity

Decrease Refers

to Load Unit

0001

KG

Start

2

  Note

In the case of the value type Fixed Value, only one entry (one line) is possible for each means of transport.

Only when using the value type Fixed Value does it make sense to enter a value in the Stop Range: End field.

In both cases, the reduced capacity is as follows:

Number of Loading-Relevant Intermediate Stops Reduced Capacity

1

2

3

4

5

6

7

8

9

10

11

10.000

9.000

8.000

7.000

6.000

5.000

4.000

3.000

2.000

1.000

0

If, on the way from the source location to the destination location, the means of transport makes two intermediate stops where

loading, unloading, or transshipment activities take place, you can load it with a capacity of 9,000 kg at the destination location.

However, if the means of transport makes 10 intermediate stops where loading, unloading, or transshipment activities take place,

the available capacity is only 1,000 kg. If the number of loading-relevant intermediate stops is greater than 11, the capacity remains

at zero.

## Single Values

If you want to define single values, specify the following values for the capacity decrease:

Stop Range: Start

## Value Type

Capacity Decrease

Percentage

2

4

Single Value

Single Value

1000

500

Capacity Decrease Refers to

## Load Unit

Capacity Decrease Refers to

## Load Unit

This is custom documentation. For more information, please visit SAP Help Portal.

96


1/14/26, 2:19 PM

Stop Range: Start

## Value Type

Capacity Decrease

Percentage

5

6

8

9

10

  Note

Single Value

Single Value

Single Value

Single Value

Single Value

500

700

2000

2300

1000

Capacity Decrease Refers to

## Load Unit

Capacity Decrease Refers to

## Load Unit

Capacity Decrease Refers to

## Load Unit

Capacity Decrease Refers to

## Load Unit

Capacity Decrease Refers to

## Load Unit

In the case of single values, it does not make sense to use the option Capacity Decrease Is a Percentage in the Percentage

field.

In this case, the reduced capacity is as follows:

Number of Loading-Relevant Intermediate Stops Reduced Capacity

1

2

3

4

5

6

7

8

9

10

11

10.000

9.000

9.000

8.500

8.000

7.300

7.300

5.300

3.000

2.000

2.000

If, on the way from the source location to the destination location, the means of transport makes two intermediate stops where

loading, unloading, or transshipment activities take place, you can load it with a capacity of 9,000 kg at the destination location.

However, if the means of transport makes 10 intermediate stops where loading, unloading, or transshipment activities take place,

the available capacity is only 2,000 kg. Note that the value by which the capacity is reduced each time always refers to the value in

the previous line and not to the original capacity. Only the first entry refers to the original capacity.

If the number of loading-relevant intermediate stops is greater than 11, the capacity remains at 2,000 kg.

## Freight Unit Building Rule

This is custom documentation. For more information, please visit SAP Help Portal.

97


1/14/26, 2:19 PM
## Use

The system takes into account freight unit building rules (FUB rules) when creating and editing freight units (see Creation and

Editing of Freight Units).

## Features

## Freight Unit Building Strategy

In the FUB rule, you define how the system is to consolidate freight units. To do this, you can use various freight unit building

strategies (FUB strategies):

## Consolidate as much as possible

In this case, the items come from different business documents, for example, forwarding orders. The system groups the

items in freight units.

  Note

In addition to forwarding orders, other possible business documents are forwarding quotations, order-based

transportation requirements, and delivery-based transportation requirements.

## Consolidate per item

In this case, the system generates one freight unit per business document item.

Consolidate per request (compatible parts)

In this case, the system groups all items of a business document to form a freight unit.

For all three FUB strategies, the system takes into account hard constraints and incompatibilities (see Incompatibilities).

  Note

The FUB strategy also applies to the creation of transportation units and freight orders (see below under Document Type and

Automatic Creation of Freight Orders).

## Planning and Split Quantities

In the FUB rule, you enter planning quantities (for example, gross weight and gross volume) with the corresponding units of

measure. The system copies the units of measure to the freight units that it creates. The units of measure form the basis for

checking the capacity of resources. You define the maximum capacity of a freight unit using the split quantity.

  Note

If you create equipment-based freight units or transportation units, the system automatically fills the planning and split

quantities from Customizing for the equipment. For more information, see below under Equipment-Based Freight Units

and Transportation Units.

You can also create freight unit building rules without indicating a unit of measure. For more information, see UoM

Setting for Quantity and Alternative Quantity below.

  Example

This is custom documentation. For more information, please visit SAP Help Portal.

98


1/14/26, 2:19 PM

You want to transport 5 tons of cement, but you can only transport it in batches of 500 kg. In this case, you define a split

quantity of 500 kg. The system generates 10 freight units.

If the system cannot find the planning unit in the business document, it converts the unit using the values that you have defined in

the product master.

  Example

You want to transport 5 tons of cement, but you can only transport it in batches of 0.5 m . In the product master, you have

3

defined that 0.8 m  of cement is equivalent to 1 ton of cement. The system then converts 5 tons of cement into 4 m  and

3

3

generates 8 freight units.

In addition to the split quantity, you can also specify a rounding value. In this case, the system calculates the freight unit quantity

as a multiple of the rounding value.

  Example
You define the following values:

## Product

Split quantity

Rounding value

3
1 computer = 1 piece = 0.06 m

3
1 m

1 piece

Since 1 m  divided by 0.06 m  makes 16.67 m , with this split quantity, the freight unit can contain a maximum of 16 computers.

3

3

3

If you enter 3 pieces as the rounding value, for example, because you can only pack three computers in a box, the freight unit

can contain a maximum of 15 computers, since 15 is a multiple of 3 and is less than 16.67.

In the FUB rule, you can use the item split checkbox to control whether items are allowed to be split if the split quantity is

exceeded.

  Example

You have defined the following values:

Freight unit building strategy

Consolidate as much as possible

Critical quantity

Gross weight

Item split allowed

No

Split quantity

20 tons

You want to schedule four items with a total weight of 21 tons. Items 1 to 3 each contain 5 tons and item 4 contains 6 tons.

Taking into account your settings, the system creates two freight units:

Freight unit 1 with items 1 to 3

Freight unit 2 with item 4

## Freight Unit Update Strategy

This is custom documentation. For more information, please visit SAP Help Portal.

99


1/14/26, 2:19 PM

You can specify whether it is possible to move items from one freight unit to another when freight units are updated. You do so by

defining the freight unit update strategy in the freight unit building rule.

  Example
There are two cargo items in a forwarding order. The system creates one freight unit for each item. One freight unit is planned

(FU1) and the other freight unit is not planned (FU2). Item 1 belongs to FU1 and item 2 belongs to FU2.

If item 1 is deleted from the forwarding order, the following occurs:

In the standard system (that is, Item Swap Allowed (Standard Behavior) is selected in the freight unit building rule),

item 2 is moved to FU1 and FU2 is canceled.

If you have selected Item Swap Not Allowed in the freight unit building rule, item 2 stays in FU2 and FU1 is canceled.

## UoM Setting for Quantity and Alternative Quantity

You can indicate which units of measure are allowed for the quantity and alternative quantity that are to be used as planning

quantity. You can either allow dimensionless units of measure only, such as EACH, Pieces, and PAL, or units of measure of all

dimensions. You can also indicate that no unit of measure is required. The system then uses the units of measure defined in the

predecessor document items. In this case, splitting of freight units is not supported.

Other planning quantities are not affected by this setting.

  Note

Quantities or alternative quantities that have a unit of measure with a dimension are ignored by vehicle scheduling and routing

(VSR) optimization, transportation proposal, and load consolidation in the respective requirement documents, such as freight

units.

## Document Type

You can control which document type is to be created by the freight unit builder, that is, freight unit type, transportation unit type,

or freight order type. You can either enter a document type directly or enter a condition for determining the document type in the

advanced settings. You define freight unit types, transportation unit types, and freight order types in Customizing. For more

information, see Customizing for Transportation Management under the following:

Planning

## Freight Unit

 Define Freight Unit Types

## Planning

## Transportation Unit

 Define Transportation Unit Types

Freight Order Management

## Freight Order

## Define Freight Order Types

If the system determines a freight order type as the document type, it automatically generates freight orders without generating

freight units or transportation units (see below under Automatic Creation of Freight Orders).

## Default Business Document Categories

During freight unit building, the system can create different categories of transportation units. If you do not specify a freight

document type in the freight unit building rule (either directly or using a condition), the system creates the following business

document categories:

Item Category

## Product / package

Business Document Category

## Freight unit

This is custom documentation. For more information, please visit SAP Help Portal.

100


1/14/26, 2:19 PM

Item Category

Package

Container

Railcar

## Trailer

## Business Document Category

Package unit as an instance of the transportation unit with TU

category “Package”

Container unit as an instance of the transportation unit with TU

category “Container”

Railcar unit as an instance of the transportation unit with TU

category “Railcar”

Trailer unit as an instance of the transportation unit with TU

category “Trailer”

In this case, the system reads the default document type from Customizing. You must therefore ensure that a default type has

been defined in the Customizing activities Define Freight Unit Types and Define Transportation Unit Types.

If you want the system to create “Freight unit” instead of “Container unit” as the business document category for container items,

you must specify the document type of the freight unit in the freight unit building rule (either directly or via a condition).

## Equipment-Based Freight Units and Transportation Units

If you enter an equipment type and group in the freight unit building rule, the freight unit builder creates equipment-based freight

units or transportation units. Depending on the equipment type, the freight unit builder creates transportation units of the

category container, railcar, or trailer.

The system automatically derives the planning quantities, units of measure, and split quantities from Customizing for the

equipment (Customizing activity Define Equipment Groups and Equipment Types). You can delete or change these quantities in

the freight unit building rule. This enables you to create transportation units or freight orders (shortcut scenario) with multiple

items (see Example: Freight Unit Building for Railcar Units).

If you want the system to create “Freight unit” instead of “Container unit” as the business document category for container items,

you must specify the document type of the freight unit in the freight unit building rule (either directly or via a condition). We

recommend that you enter it directly, rather than using a condition.

For more information, see Consideration of Equipment Data During FU or TU Creation.

## Automatic Creation of Freight Orders

If you want a freight order to be created automatically instead of a freight unit (shortcut scenario), enter a freight order type as the

document type or a condition for determining this freight order type. This function is also supported for transportation units (see

Transportation Unit).

  Example

You specify in a condition that if the quantity exceeds 20 tons, freight order type 1 is to be used; otherwise freight unit type 1 is

to be used.

This function is suitable, for example, for the following cases:

In general you want to send small orders that are below one of the upper limits you have defined with an express delivery

company.

You always have to transport orders as a full load due to their size.

## Process Controller Strategies

This is custom documentation. For more information, please visit SAP Help Portal.

101


1/14/26, 2:19 PM

You can use strategies to define the way in which freight units are created in accordance with your own requirements. SAP delivers

the standard strategy FUB_AUTO for freight unit building. For more information, see Process Controller Configuration.

## Unified Package Building

On the tab page Advanced Settings you can specify if during freight unit building the system creates freight units, freight orders,

or package units with a complete hierarchy of package and product items based on the information from the order documents.

Moreover, the system determines the exact position of each product in the package and displays these positions in the load plan.

Alternatively, you can define that the system calculates only a rough estimation of the number of packages that can be built. This

estimation is displayed in the header data of a freight unit on the General Data tab page. It can also be used by the VSR optimizer

during planning.

As a prerequisite, you must have entered a unified package building profile. For the determination and display of the exact product

positions, you must have selected Detailed Mixed Package Building as the mixed package building mode in your unified package

building profile.

Whether the system creates a freight unit, freight order, or package unit during freight unit building depends on which document

type you enter on the General Data tab page of the freight unit building rule. If you want the system to create a complete package

hierarchy, you can choose a document type of the categories FU, FO (Freight Order), or TU (Transportation Unit). If you use a TU

type, the category must be Package (that means package unit). We recommend to use a TU type with category Package instead of

an FU type.

You can also specify the maximum number of top-level packages that a freight unit, freight order, or package unit may contain

when the system creates them during freight unit building. The system considers this number when it creates a complete package

hierarchy.

Further, you can specify that a separate freight unit, freight order, or package unit is to be created for unpackaged items, that

means, one common business document is created for all unpackaged items that contains no other items. The system considers

this checkbox when it creates a complete package hierarchy. If you use the package builder as your unified package building

engine, you must select the Only Full Packages in PB Result checkbox in your unified package building profile as a prerequisite. In

this case, the system builds full packages for a product and the remaining quantities of this product stay unpackaged.

For more information, see Unified Package Building in TM.

## Activities

You can define FUB rules by opening the app Create Freight Unit Building Rule from the launchpad.

## More Information

Determination of Freight Unit Building Rules

Definition of Dimensions and Units of Measurement

Determination of Freight Unit Building Rules

## Use

When creating freight units, the system determines which freight unit building rule (FUB rule) it is to take into account for a

business document item. To find out which business documents are supported, see Creation and Editing of Freight Units.

This is custom documentation. For more information, please visit SAP Help Portal.

102


1/14/26, 2:19 PM
## Prerequisites

Optionally, you have defined FUB rules. For more information, see Freight Unit Building Rule.

You have defined conditions with the condition type /SCMTMS/FUBR. For more information, see Condition.

## Features

To determine FUB rules, the system does the following:

1. The system checks whether you have specified a condition in the business document type, for example, forwarding order

type. There can be only one condition per business document type.

2. If the system does not find a condition or if this condition does not return a result, the system checks whether you have

specified a standard FUB rule in the business document type.

3. If you have not specified one, the system uses default settings.

  Note

You can see which FUB rule the system has used in the freight unit.

Definition of Dimensions and Units of Measurement

## Use

You use dimensions to group units of measurement. You need units of measurement to display product quantities, for example, for

freight unit building rule (FUB rules), and to describe the capacity of vehicle resources (see Freight Unit Building Rule and Vehicle

Resource).

  Note

The system might display quantities with 14 decimal digits. If you want the system to round quantities to a specific number of

decimal digits, follow the instructions described in SAP Note 1132219

.

## Prerequisites

You have checked in Customizing under  General Settings

 Check Units of Measurement

 that the dimensions

delivered as a standard and the associated units of measurement are complete.

When using FUB rules, the system checks if the forwarding order contains the relevant quantities based on the FUB rules. If

the forwarding order does not contain the relevant quantities, the system uses the product data. For this purpose, you have

defined the following in the product master data:

Base unit of measure (BUoM)

## Conversion factors

You need conversion factors to convert the base units of measure into the required units of measurement. You

define these in the product master on the Units of Meas. tab page. For more information, see Definition of Products.

If you have not defined a conversion factor, the system cannot take split quantities or rounding values into account

when building freight units from business documents (forwarding orders, for example). In this case, it sets the

quantities to zero.

This is custom documentation. For more information, please visit SAP Help Portal.

103


1/14/26, 2:19 PM
## Example

## Examples for Dimensions and Units of Measurement

The following table provides you with examples of dimensions and of some units of measurement you can assign to them.

## Dimension

Units of Measurement

Mass

## Volume

## Kilogram; milligram

## Cubic centimeter; cubic decimeter

Example for the Conversion of Units of Measurement

The following units of measurement are predefined as a default:

Kilogram (dimension mass)

Cubic decimeter (dimension volume)

You also define the following unit of measurement:

Pallet (no dimension)

Your forwarding order contains product A and product B each of which have the quantity "1 piece". You have defined piece as

BUoM for both products.

You have defined the following conversion factors for product A:

1 piece = 2 kg

1 piece = 3 dm³

You have defined the following conversion factor for product B:

1 piece = 0.5 pal

In this case, product A is displayed with quantity 2 kg or 3 dm³. In the unit of measurement pallet (pal), the quantity 0 is displayed

because you have not defined a conversion factor.

Product B is displayed with the quantity 0.5 pal. Since you have not defined conversion factors for kilogram or cubic decimeter, no

conversion occurs. The system displays the value 0.

Incompatibilities

## Use

You use incompatibilities to define the compatibility of planning data that the system is to take into account during transportation

planning, for example:

Freight units with different Incoterms must not be transported together.

A container of a certain equipment type cannot be transported on a particular resource because it is too small.

Refrigerated goods must only be transported in appropriate means of transport (refrigerated trucks).

This is custom documentation. For more information, please visit SAP Help Portal.

104


1/14/26, 2:19 PM

A certain means of transport cannot be unloaded at a location since the location does not have a suitable loading ramp.

A truck that needs to be unloaded from the side cannot be unloaded at a location since the location does not offer the

prerequisites for unloading from the side.

A driver must not transport dangerous goods or must not drive a truck because he does not have the corresponding

license.

In this way, you can control how freight units or container units are assigned to vehicle resources or vehicle types in manual

planning, for example.

  Note
For consistency reasons, you can define incompatibilities only. To define a compatibility, you have to define an incompatibility

with all other attribute values.

## Features

You can define incompatibilities in different ways.

On the one hand, you can define incompatibilities between any two attributes of two business object nodes. To do so, you define

two conditions and specify the relevant results. Two business object instances are then incompatible if the result of the condition

matches these relevant results.

On the other hand, you can enter only one condition and select the Ident. Values Only (Identical Values Only) checkbox. In this

way, you can define an incompatibility between two instances of the same business object (BO), for example, two freight units. The

two BO instances are then only incompatible if their values differ. If a planning run comprises many business objects and the

attribute can have many values, performance might be reduced. In this case, we do not recommend that you use this option.

Alternatively, you can use customer-specific logic to determine the pairs of incompatible objects. To do so, choose the option

External Determination Strategy in the Determination Method field and specify the required strategy in the External

Determination Strategy field. For more information, see External Strategies. If you define incompatibilities with conditions and a

freight unit has several products, the system only determines the first product, and it does this randomly. You can avoid this

restriction by using example strategy TM_INCOMP. In this case, you specify two products that are incompatible in your

incompatibility. The example strategy then checks whether the freight units contain these products. TM_INCOMP serves as an

example strategy for incompatibilities, the class assigned describes the interface and serves as reference implementation for

customer-specific classes. The unit tests serve documentation purposes.

The example strategy shows that condition-based incompatibilities are not always suitable. However, if a freight unit has only a

single product item (package items or container items can, however, also exist), a filter on the item type Product in the condition is

sufficient.

You use the incompatibility area to define the area in which the system is to take into account an incompatibility:

Automatic planning (that is, VSR optimization, load planning and load consolidation, and generating transportation

proposals) and manual planning

## Creating freight units

Carrier selection (including continuous move)

## Creating delivery proposals

VSR optimization considers incompatibilities as hard constraints.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

105


1/14/26, 2:19 PM

VSR optimization does not support planning with drivers. Therefore, VSR optimization supports driver incompatibilities with

default drivers only.

You use the incompatibility type to define the BOs between which an incompatibility is to be valid. For example, you can use the

incompatibility type FU – Compartment to ensure that a freight unit is not transported in a certain compartment. You can also use

the incompatibility type to define the incompatibility level.

  Note

You can define incompatibilities between both freight units and container units on the following incompatibility levels:

Vehicle level (this means that the two freight units must not be transported in the same vehicle or in the same

compartment)

Compartment level (this means that the two freight units must not be transported in the same compartment)

Means-of-transport combination level (this means that the two freight units must not be transported in the same

vehicle, in the same compartment, or in the same means-of-transport combination)

Consignment order level (this means that the two freight units must not be transported with the same

consignment order)

Conditions for the compartment level must use data access definitions with the following data access classes:

/SCMTMS/CL_COND_DAD_COMP_DATA: Data access class for compartment data, for example, compartment

type, sequence

/SCMTMS/CL_COND_DAD_COMP_ATTR: Data access class for compartment attributes to extract the attribute

values as defined for the compartment type

Conditions for the means-of-transport combination level must use data access definitions with the following classes:

/SCMTMS/CL_COND_DAD_MTR_COMB: Data access class for means-of-transport combination data

/SCMTMS/CL_COND_DAD_MTR_CO_ATT: Data access class for means-of-transport combination attributes

A condition type exists for each BO node that the system uses in an incompatibility type.

Furthermore, when defining your incompatibility, you can specify whether the system is allowed to violate incompatibilities during

manual planning, VSR optimization, or background processing. You can override this setting in the incompatibility settings. You can

also specify if the incompatibility applies to vehicle resources or vehicle types or both. Note however that this is only possible for

incompatibility types that involve vehicle resources or vehicle types.

In the incompatibility settings, you specify which incompatibilities the system is to consider in a certain incompatibility area. You

can assign them to your planning profile, your carrier selection settings, and, for freight units, your freight unit building rule.

Moreover, you can define default incompatibility settings, for example, for a certain incompatibility area. This system considers

these if you have not assigned any incompatibility settings to the specified profiles.

  Note

When you access the transportation cockpit, the system checks for incompatibility settings in the following order: in the profile

and layout sets, in the planning profile, and in the default incompatibility settings.

If you then create a freight order or a freight booking directly in the transportation cockpit, the incompatibility settings that

were identified when you accessed the cockpit are assigned to the business document. When you open the freight order or

freight booking document directly, these settings are then used for the incompatibility check.

This is custom documentation. For more information, please visit SAP Help Portal.

106


1/14/26, 2:19 PM

After you have defined an incompatibility, you can perform a simulation.

If you want to simulate an incompatibility with the incompatibility type Freight Unit – Freight Unit (Vehicle Level), for example,

you specify two freight units. In this case, the system checks whether an incompatibility exists between the two freight units.

## Activities

You can define incompatibilities by opening the app Create Incompatibility from the Launchpad.

You can define incompatibility settings by opening the app Create Incompatibility Settings from the Launchpad.

## Related Information

Definition of Incompatibilities

Planning Profile

## Condition

## Definition of Incompatibilities

## Incompatibility Between Two Freight Units with Different Transportation Groups

You want to prevent freight units with the transportation group Liquid and Solid from being delivered together. In this case, you

define a condition (see Condition) with the condition type for freight unit incompatibilities. Here the output value is the

transportation group for the item.

You then define an incompatibility with the incompatibility type FU-FU (Vehicle Level), which specifies that freight units with these

two transportation groups must not be delivered at the same time on one truck. You choose the incompatibility area for manual

planning, VSR optimization, and for generating transportation proposals.

You then specify the condition that you defined before twice. You specify Liquid as the relevant result of the first condition. You

specify Solid as the relevant result of the second condition.

## Incompatibility Between Certain Freight Units and a Certain Means of Transport

All freight units with the transportation group Non-Liquid are to be incompatible with the means of transport Tanker. In this case,

you define two conditions: one for the freight unit (with the condition type for freight unit incompatibilities) and one for the

capacity, in this case, the vehicle resource, for example (with the condition type for vehicle resource incompatibilities).

You then define an incompatibility with the incompatibility type FU-Vehicle Resource. You specify Non-Liquid as the relevant result

for the condition for the freight unit. You specify Tanker as the relevant result for the condition for the vehicle resource.

  Note

Alternatively, you can specify Liquid as the relevant result for the condition for the freight unit and Not a Tanker as the relevant

result for the condition for the vehicle resource.

Incompatibility Between Freight Units with Different Transportation Groups

You want to prevent freight units with different transportation groups from being delivered together.

This is custom documentation. For more information, please visit SAP Help Portal.

107


1/14/26, 2:19 PM

In this case, you define an incompatibility and specify only one condition in which the system determines the transportation group

for the freight unit. You also select the Ident. Values Only (Identical Values Only) checkbox. Freight units with different

transportation groups are then incompatible.

  Note

You can define the incompatibilities listed here in the same way for container units.

Context Determination

## Use

This function allows you to expand your selection of resources, drivers, and documents to be displayed in the transportation

cockpit. The expanded selection includes resources, drivers, and documents that, within the planning horizon, are assigned to the

resources, drivers, and documents you selected on the selection screen of the transportation cockpit.

You can use context determination to expand your selection to all documents assigned to the following resources:

Truck

Trailer

Driver

Container

Locomotives

## Railcars

You can use context determination for the following documents:

## Road freight orders

Your selection includes all trucks and drivers that transport the selected road freight orders as well as the container and

trailer units that are assigned to the selected road freight orders.

## Trailer units

Your selection includes all trailers that transport the selected trailer units as well as the road freight orders and container

units that are assigned to the selected trailer units.

## Container units

Your selection includes all containers that are assigned to the selected container units as well as the freight orders, trailer

units, and railcar units to which the selected container units are assigned.

## Rail freight orders

Your selection includes all locomotives that transport the selected rail freight orders as well as the container and railcar

units that are assigned to the selected rail freight orders.

## Railcar units

Your selection includes all railcars as well as the rail freight orders and container units that are assigned to the selected

railcar units.

## Package units

This is custom documentation. For more information, please visit SAP Help Portal.

108


1/14/26, 2:19 PM

Your selection includes all trucks, trailers, and containers as well as the freight orders, trailer units, and container units that

are assigned to the selected package units.

## Activities

In your planning profile you set the Context Determination checkbox in order to activate context determination. To edit your

planning profile, open the Edit Planning Profile app on the launchpad. For more information, see Planning Profile.

## Example

You have three road freight orders in your planning horizon that you want to transport with the same truck. You have activated

context determination in your planning profile.

You select the truck and enter the Transportation Cockpit. All three road freight orders are added to the selection. Alternatively,

you can select one of the road freight orders and enter the Transportation Cockpit. The truck and the other two road freight orders

are added to the selection.

Context Determination in VSR Optimization

## Use

This function ensures that the system processes all dependent objects, in other words, freight units and road freight orders,

together during VSR optimization. It cannot be switched off.

By taking the context into account, the system creates a transportation plan that is consistent with regard to all possible

dependencies. Possible dependencies include:

Incompatibilities between freight units

Windows of the freight units

Capacity decrease

## Features

The system performs context determination automatically when you start VSR optimization in the transportation cockpit. In

addition to the objects that you have selected for VSR optimization in the transportation cockpit (that is, either individual objects

or all objects), it also considers indirectly linked objects. The system determines the following objects as context and hands them

over to VSR optimization:

The system determines indirectly linked freight orders from freight units.

  Example
A freight unit is to be delivered from A via B and C to D. You have selected the freight unit for the stage from B to C in the

transportation cockpit. A freight order exists for each of the stages A to B and C to D. The system determines these two

freight orders as context.

The system determines indirectly linked freight units and transportation units from freight units. Here, the system transfers

the entire transportation chain to VSR optimization, even if you have selected only one freight unit for a stage.

  Example

This is custom documentation. For more information, please visit SAP Help Portal.

109


1/14/26, 2:19 PM

A freight unit is to be delivered from A via B and C to D. You have selected the freight unit for the stage from B to C in the

transportation cockpit. Additional freight units exist for the stages A to B and C to D. The system determines these

freight units as context.

The system determines indirectly linked freight orders from resources. However, this applies to finite resources only (for

multiresources, you must have specified the number of individual resources).

  Example

A vehicle resource is to travel from A via B and C to D. A freight order is planned for each of the stages A to B and C to D.

The system determines these two freight orders as context.

  Note

The system determines only those objects as context that you have not explicitly selected.

VSR optimization uses the objects that the system has determined as context for information purposes only. VSR

optimization is not permitted to change these objects.

The system determines the context for multiresources if, in Customizing for the related means of transport, you have

selected the checkbox for blocking multiresources and have entered a number of single resources that is greater than

zero.

The system determines the following objects as additional changeable input and hands them over to VSR optimization:

VSR optimization determines indirectly linked freight units from road freight orders that have already been planned. That

means it adds freight units that are already planned on a selected road freight order to the selection.

  Example

You have selected a road freight order. Two freight units are already planned on this road freight order. The system adds

these two freight units to the selection.

Related Information

Context Determination

Manual Planning

## Use

Manual planning allows you to manually create or change a transportation plan. To create a transportation plan, you assign

requirement documents, for example freight units, to capacities, for example vehicle resources. The system creates capacity

documents, for example freight orders, which you can process further. For example, you can assign drivers to your freight orders or

perform load planning. If you assign freight units to a container, for example, a container unit is created that you can directly assign

to a freight booking.

Planning strategies determine the steps that the system is to carry out during the planning process and the order in which it does

so. In the planning profile, you can specify which planning strategy you want to use. We provide the following standard planning

strategies, for example:

## VSRI_DEF for manual planning

This is custom documentation. For more information, please visit SAP Help Portal.

110


1/14/26, 2:19 PM

## VSRI_SCH for manual planning with subsequent scheduling

Manual planning is done in the transportation cockpit. Profile and layout sets as well as page layouts let you configure the data

used for planning and the layout of the transportation cockpit (see Starting the Transportation Cockpit). You can display areas of

the transportation cockpit in more than one window (see Planning with Multiple Windows).

  Note

Note that the tools and checks provided for manual planning are intended to provide support only. You, as the planner, remain

responsible for ensuring that the planning results are consistent.

## Prerequisites

You have specified a planning strategy in the planning profile. For more information, see Planning Profile.

You have configured the settings for freight orders in the Customizing activity Define Freight Order Types under

Transportation Management

 Freight Order Management

 Freight Order

.

You have configured the settings for freight bookings in the Customizing activity Define Freight Booking Types under

Transportation Management

 Freight Order Management

 Freight Booking .

You have configured the settings for transportation units in the Customizing activity Define Transportation Unit Types

under  Transportation Management

## Planning

 Transportation Unit

.

If you work with schedules, you have configured the settings in the Customizing activity Define Schedule Types under

Transportation Management

## Master Data

 Transportation Network

 Schedule .

If you work with vehicle resources, you have created active and passive vehicle resources. To do so, on the SAP Easy Access

Screen, choose  Logistics

 Transportation Management

 Master Data

 Resource

 Resource .

If you want to undo and redo the manual planning actions you perform in the transportation cockpit and in carrier

selection, you have configured the settings in the Customizing activity Define Maximum Number of Consecutive Undo and

Redo Actions under  Transportation Management

 Basic Functions

 General Settings .

## Features

You have the following options, for example:

You can create capacity documents directly from freight units (see Creation of Capacity Documents from Freight Units).

You can assign freight units to existing capacity documents (see Assignment of Requirement Documents to Existing

Capacity Documents) or remove freight units from capacity documents.

You can create capacity documents from vehicle resources, trailers, railcars, containers, or schedules. You can also create

them as blank documents, that is, with no freight units assigned to them (see Creation of Capacity Documents from

Resources).

You can create capacity documents based on requirement groups (see Creation of Capacity Documents Based on

Requirement Groups).

You can assign a resource (for example, a trailer) to an existing capacity document (for example, a freight order) to create a

requirement document (for example, a trailer unit). Alternatively, you can first create the requirement document (for

example, the trailer unit) and assign it to the capacity document (for example, the freight order) or the resource (for

example, the truck) in which case a capacity document (for example, a freight order) is created.

You can assign freight units to an equipment type, such as a vehicle type, to create a capacity document, such as a road

freight order. For more information, see Planning Based on Equipment Types.

This is custom documentation. For more information, please visit SAP Help Portal.

111


1/14/26, 2:19 PM

You can have the system create local transportation unit items. For more information, see Manual Planning with Local

Transportation Unit Items.

You can perform various planning and reassignment activities using drag and drop (see Reassignment).

You can manually overwrite some of the results of your manual planning or an automatic planning run. For example, you can

change the vehicle resource, the carrier, or departure date in a freight order.

You can generate multiple alternative transportation proposals, that is, transportation plans, for each freight unit and then

choose one of these proposals (see Generation of Transportation Proposals).

You can create delivery proposals, which you can send to Logistics Execution (LE) where deliveries are then created (see

Creation of Deliveries from TM).

You can calculate charges for your freight orders and freight bookings (see Charge Calculation).

You can combine a transportation unit for empty provisioning and a transportation unit for empty return in a single

transportation unit (triangulation transportation unit). This feature is only available for container units and railcar units. For

more information, see Triangulation.

During manual planning, the system makes sure that two freight unit stages or two freight units with different paying

company codes are not planned on the same freight document. For more information, see Transportation Management in

Advanced Intercompany Business Processes.

The system can calculate greenhouse gas (GHG) emissions during manual planning. For more information, see Greenhouse

Gas Emissions.

You can carry out various planning operations using natural language. For more information, see Conversational Planning.

You can display and evaluate key performance indicators (KPIs). For more information, see Key Performance Indicators in

the Transportation Cockpit.

You can define and change appointments for freight orders. For more information, see Appointment.

More Information

Utilization

## Outer Volume

Considering Dangerous Goods

Change Controller

## Company Codes

Starting the Transportation Cockpit

## Context

The transportation cockpit is the main user interface for transportation planning.

## Prerequisites

If you want to start the transportation cockpit with a predefined set of fields, you can define field catalogs according to your

needs and assign them to your page layouts. For more information, see Field Configuration for the Transportation Cockpit.

This is custom documentation. For more information, please visit SAP Help Portal.

112


1/14/26, 2:19 PM

If you want to use profile and layout sets, you have defined profiles according to your needs, for example a planning profile

and several selection profiles. For more information about profiles and settings, see Profiles and Settings.

Requirements and capacities exist.

## Procedure

1. Open the Transportation Cockpit app from the launchpad. Note that you can control the behavior of the transportation
cockpit by defining transportation cockpit settings in the planning profile. For more information, see Planning Profile.

2. The Profile and Layout Sets screen is displayed. Select an existing profile and layout set or create a new one and then

choose Continue. For more information, see Use of Profile and Layout Sets. Alternatively, you can switch to the
Transportation Cockpit: Selection Criteria screen using Switch Start Screen. This screen allows you a quick start of the
transportation cockpit without having to define several selection profiles. Enter your selection criteria and choose
Continue. For more information, see Selection Criteria for Transportation Cockpit.

If you want to bypass the Profile and Layout Sets screen the next time you call the transportation cockpit, mark one

profile and layout set as the default set by selecting the checkbox in the Default Set column. Then select the Hide

Screen checkbox below the table. When you next call the transportation cockpit, the system loads the planning data

using the criteria that you specified as the default set. You can return to the Profile and Layout Sets screen by

choosing  Change Profile Selection

 Profile Selection Screen .

You can assign page layouts to your profile and layout sets. They allow you to define which buttons and functions,

for example, are available in the transportation cockpit and on the result screen of vehicle scheduling and routing

(VSR) optimization. For more information, see Page Layouts.

3. In the transportation cockpit, you have the following options:

Planning with lists and hierarchies

For more information, see Manual Planning.

## Planning on the geographical map

For more information, see Interactive Planning on the Map.

## Planning in the Gantt chart

For more information, see Gantt Chart for Transportation Planning.

Selection Criteria for Transportation Cockpit

## Use

Selection criteria enable you to carry out your planning activities without having to configure selection profiles.

## Prerequisites

Transportation demands (freight units, for example) and capacities exist.

We recommend that you have defined a planning profile. If you do not define one, the system uses default values that might

not meet your planning needs.

## Features

On the Transportation Cockpit: Selection Criteria screen, you have the following options:

This is custom documentation. For more information, please visit SAP Help Portal.

113


1/14/26, 2:19 PM

Function

Continue

## Description

Starts the planning function

## Switch Start Screen

Toggles the view between the Selection Criteria and the Profile

and Layout Sets screen

## Layout Personalization

Enables you to customize the layout of the transportation cockpit

## Display Settings

Enables you to change the settings for the time zone, unit for

distances, and alternative identification types

## Saved Searches

Enables you to load or delete a search variant that you previously

Clear Entries

Save Search As

Default Start Screen

Activities

saved

Clears all of the search criteria that you entered

Saves the criteria that you entered as a search variant

Specifies the screen that is displayed by default when you start the

transportation cockpit. Note that if you change the default start

screen, you have to restart the app for the change to be applied.

To access the Transportation Cockpit: Selection Criteria screen, open the Transportation Cockpit app from the launchpad.

Use of Profile and Layout Sets

## Use

When starting the transportation cockpit, carrier selection and delivery creation apps, you can select a profile and layout set (PLS)

to define the layout of the apps and which objects are available in the app for you to work on.

## Features

## Central PLS Creation and Management

The PLS management applications enable an administrator to centrally create and manage PLSs for a team or organization and

assign users to them. This approach simplifies the process of working with PLSs by removing the need for individual users to

create and maintain their own.

When an administrator creates a PLS and assigns a user to it, the PLS is available for the user to select on the relevant application

start screen.

The administrator can create and manage PLSs using the following apps:

PLS Management for Transportation Cockpit

PLS Management for Carrier Selection

## PLS Management for Delivery Creation

Tip: To help the administrator, Quick Help is available on the PLS management apps. To display Quick Help, on the UI, right-click

and select Display Quick Help.

This is custom documentation. For more information, please visit SAP Help Portal.

114


1/14/26, 2:19 PM

When creating a PLS, the following recommendations should be considered:

## Transportation cockpit

You are recommended to enter a selection profile for freight units as well as a planning profile to which you have already

assigned a selection profile for freight orders and freight bookings.

Optionally, you can also specify other settings, such as incompatibility settings or settings for capacity selection. If you

have already assigned incompatibility settings or settings for capacity selection to the specified planning profile, for

example, the system overwrites these settings with the settings that you specified here.

The system considers the profiles that you specify in your PLS for all planning options available in the transportation

cockpit.

  Note

In the transportation cockpit, the user can use the Change Planning Settings function to temporarily change the

planning settings and load planning settings in the selection profiles. The system discards these changes when you

leave the transportation cockpit or change the profile selection.

## Carrier selection

You are recommended to enter a selection profile for freight orders and freight bookings as well as carrier selection

settings.

For more information, see Carrier Selection.

## Creating delivery proposals

You are recommended to enter a selection profile for freight units, freight orders and freight bookings as well as a delivery

profile.

For more information, see Creation of Delivery Proposals.

## PLS Selection on Application Start Screens

On the Transportation Cockpit, Carrier Selection and Delivery Creation app start screens the user can select the profile and layout

sets that the administrator has assigned them to.

If authorized, on the app start screen the user can create a new PLS or edit a PLS that they are assigned to. If the user has already

assigned settings to the specified planning profile, the system overwrites these settings with the settings that the user specified

here. In addition, the user can edit the page layout used in a PLS by clicking Layout Personalization.

Tip: To help the user, Quick Help is available on the app start screens where the user selects the PLS they want to use. To display

Quick Help, on the UI, right-click and select Display Quick Help.

## Activities

The administrator can use the authorization object T_PL_SETS to define if the user has authorization to create, edit and assign

PLSs. The authorization applies to the app start screens and the PLS management apps.

More Information

## Page Layouts

## Field Configuration for the Transportation Cockpit

This is custom documentation. For more information, please visit SAP Help Portal.

115


1/14/26, 2:19 PM

As a power user or administrator, you can predefine the fields that are offered in the lists and hierarchies of the Transportation

Cockpit app as well as their sequence and names.

## Use

SAP delivers maximum user interface (UI) structures for the lists and hierarchies of the Transportation Cockpit app that contain

all possible fields for these lists and hierarchies. Based on the respective maximum UI structure, you create a field catalog for each

list and hierarchy. Each field catalog defines which fields are to be displayed; whether they are displayed by default, using

personalization, or not at all; and the sequence in which they are to be displayed. You can also specify the names (labels) of the

fields and tooltips. Configuring the fields can improve the response time of the transportation cockpit, which mainly depends on

fields displayed by default but also on fields that you can display using personalization. Fields that are not displayed at all, that is,

neither by default nor using personalization, do not have an impact on the response time.

You assign these field catalogs to your page layouts. When you start the Transportation Cockpit app with a certain page layout, the

assigned field catalogs are taken into account and the corresponding fields are displayed for the lists and hierarchies. You can

create several field catalogs per list and hierarchy if you want to support several scenarios for this list or hierarchy. You can also

copy and delete field catalogs. Note that the maximum user interface structures also contain the fields that you could add using

the enhancement concept for the Transportation Cockpit app in the past.

SAP delivers field catalogs for lists and hierarchies of the Transportation Cockpit app. These are the default field catalogs. You

can't change or delete them. You can copy them and then change them. If you create new page layouts, the system automatically

assigns the default field catalog defined for the corresponding list or hierarchy. Note that for your existing page layouts, you have

to assign the field catalog manually. For more information about the available default field catalogs, see SAP Note 3362076.

If you extend one of the nodes ROOT, STOP, STOP_SUCCESSOR, or ITEM_TR of business object TOR with your own fields, these

fields are automatically inserted into the corresponding field catalogs. You can then edit them in the field catalog as any other field.

For example, you can add or change a label or indicate that they are to be displayed by default on the user interface.

You can transport your field catalogs to other systems.

## Prerequisites

To define field catalogs, use the authorization object T_LAYOUT, activity Administer.

## Activities

1. You define field catalogs for your lists and hierarchies in the Define Field Catalogs for Transportation Cockpit app based

on the maximum UI structures. You specify, which fields are to be displayed by default in the Transportation Cockpit app

and which are to be displayed using personalization. Additionally, you specify the sequence of the fields as well as their

names and tooltips.

You can mark one field catalog as the default field catalog per content object, for example road freight order list or

hierarchy.

2. You assign your field catalogs to your page layouts in the Define Page Layouts for Transportation Cockpit app.

If you have marked a field catalog as the default field catalog, this field catalog is automatically assigned to the page layout

when you add the corresponding content object to the page layout.

3. When you start the Transportation Cockpit app with a certain page layout, the assigned field catalogs are taken into

account and the corresponding fields are displayed for the lists and hierarchies.

## Page Layouts

This is custom documentation. For more information, please visit SAP Help Portal.

116


1/14/26, 2:19 PM

A page layout defines the buttons, functions, levels and hierarchies that are displayed in the Transportation Cockpit, Carrier

Selection and Delivery Creation app UIs.

To create and manage page layouts, use the following apps:

Define Page Layouts for Carrier Selection

Define Page Layouts for Delivery Creation

Define Page Layouts for Transportation Cockpit

## Define Page Layouts for Transportation Proposal

On the start screen of these apps, you can mark a page layout as your default page layout. In the Define Page Layouts for

Transportation Cockpit app and the Define Page Layouts for Carrier Selection app, you can also specify that quick views are not

to be displayed for a specific page layout. Note that you need to add the Hide Quick View field from the Settings first. If you work

with multiple windows, you can activate this function for each of the corresponding page layouts.

After creating a page layout, you can include it in a profile and layout set. The app for which you have defined a page layout (for

example, the transportation cockpit), is then always opened with this page layout. Note that you can also switch to another page

layout from within the app. In the page layout, you can define the page layouts that should be available for switching.

You can transport your page layouts to other systems.

For an overview of the page layouts delivered by SAP for the transportation cockpit, see SAP Note 2358887

 and SAP Note

3155675

.

## Activities

To define page layouts for all users, specific user roles, or an individual user, use the authorization object T_LAYOUT,

activity Manage, Administer.

To define a selection of available functions for your page layouts, use the settings in Customizing under  Transportation

Management

## Planning

## General Settings

 Define Settings for Page Layouts .

To synchronize page layouts with the Customizing settings, use the app Synchronize Page Layouts with Customizing. This

will synchronize all page layouts.

Note that you can also synchronize an individual page layout. To do so, select Show Configuration Data for the local toolbar

within the page layout. Then select Restore Pushbutton Data. For the global toolbar, select Restore Pushbutton Data

within the page layout.

To improve the overview of your rescheduling activities and the coupling and uncoupling of trailers, you can define a layout

for which you select the Dual View checkbox on the Orders Area or Transportation Units Area tab page. You define this

layout in the layout settings for the transportation cockpit. In the transportation cockpit, you can display the list with the

documents to be rescheduled in two views. Alternatively, you can select the Dual View checkbox on the Hierarchies Area

tab page. For more information about reassignment and coupling and uncoupling trailers, see Reassignment and Use of

Trailers.

## Related Information

Use of Profile and Layout Sets

Profiles and Settings

## Planning with Multiple Windows

This is custom documentation. For more information, please visit SAP Help Portal.

117


1/14/26, 2:19 PM

You can display areas of the transportation cockpit in up to three separate and flexible windows that you can position across

multiple monitors and can resize independently. This means you can display areas such as the geographical map and the Gantt

chart in separate windows, and drag and drop objects between windows.

## Context

Complete the following steps to enable multiple windows. For more information about restrictions, see SAP Note 2551221

.

## Procedure

1. Create a page layout for an additional window.

Standard SAP page layouts that are compatible with multiple windows use the following naming convention:

The suffix "MW" indicates the page layout is for the main window.

The suffix "A1" and "A2" indicate the page layout is for additional window 1 and additional window 2.

2. In the (main) page layout for the transportation cockpit, add the additional-window page-layout in the Additional Windows

area.

3. To display the additional window, in the transportation cockpit, on the application toolbar, click Open Additional Window.

The additional window is displayed and "Additional Window 1" is displayed on the title bar; similarly, "Main window" is

displayed on the title bar of the original window that has become the main window.

## Key Performance Indicators in the Transportation Cockpit

In the transportation cockpit, you can display and evaluate key performance indicators (KPIs).

As a transportation planner, KPIs help you evaluate whether your transportation plan is efficient and optimized. For example, if you

create road freight orders that are subcontracted, these road freight orders should be optimized regarding utilization and costs. If

you plan your own fleet, minimizing the distances that are traveled without load might be another KPI you are interested in. In both

cases, you want to see the impact of your planning decisions immediately for the relevant KPIs in the transportation cockpit.

## Prerequisites

You have defined a transportation KPIs profile and selected at least one KPI from a list of predefined KPIs. The KPIs profile

controls which KPIs are displayed in the transportation cockpit and how they are displayed. The predefined KPIs cover

areas such as distance and duration, utilization, weight, volume, quantity, normalized quantity, charges, and CO  emissions.

2

Optionally, you have defined filter criteria, threshold values, and semantic colors for the KPIs. For example, for a utilization

KPI, you could define that a utilization of 90 % and higher is fine (positive). The corresponding value is then displayed in

green. You can also indicate whether the previous value and the delta value are to be displayed for a KPI.

For each KPI, you can show details and documentation.

Nested KPIs, that is KPIs that consist of more than one KPI, such as CO  emissions per distance, are displayed on the

2

Nested KPIs tab.

For each KPI (including nested KPIs), you need to specify the unit of measure in which you want the KPI values to be

displayed.

You can change the heading and subheading of the predefined KPIs according to your needs or even define your own KPIs.

For more information, see SAP Note 3612870

.

To create a transportation KPIs profile, open the Create Transportation KPIs Profile app from the launchpad.

This is custom documentation. For more information, please visit SAP Help Portal.

118


1/14/26, 2:19 PM

You have specified the transportation KPIs profile on the Profile and Layout Sets screen or the Transportation Cockpit:

Selection Criteria screen. By doing so, the transportation cockpit will contain a KPIs screen area and the KPIs will be

determined automatically after each planning operation.

In the field catalogs for road freight orders and freight unit stages, you have selected fields that allow you to see whether a

road freight order or freight unit stage is critical for a specific KPI. Further, you have indicated whether these fields are to be

displayed by default or using personalization. For example, you can display the calculation status, the duration per weight,

or the number of pick-up stops per distance for road freight orders. For more information about field catalogs, see Field

Configuration for the Transportation Cockpit.

## Features

The KPIs screen area is collapsible and expandable. It is visible for a planning session all the time, even if you maximize the

transportation cockpit or work in dual view mode.

The KPIs displayed within the KPIs screen area are updated immediately after each planning operation, undo, or redo operation.

Further, you can see how a KPI changes when you perform a planning operation. The delta value for the KPI, such as +1.5% or

-2.0%, lets you easily see whether the KPI has improved or deteriorated or not changed at all. An arrow indicates the trend based

on the delta value. It’s either red or green depending on the KPI objective. The previous value of a KPI allows you to compare a KPI

before and after a planning operation. Using the context menu, you can display documentation and a log for each KPI.

In the lists and hierarchies of the transportation cockpit, you can see whether a road freight order, freight unit stage, or truck

resource is critical for a specific KPI. You can also display the calculation status, which indicates whether a certain document was

taken into account by the KPI calculation.

  Note

KPIs are supported for road freight orders, truck resources, and freight unit stages only.

The display of KPIs allows you to analyze the data of selected freight unit stages, road freight orders, and truck

resources. This feature is not intended to be used as a pure analytical tool that allows analyzing data such as all freight

orders of the last half year. Therefore, technical limitations such as the KP calculation horizon and warning messages are

implemented to prevent the use of the transportation cockpit as a pure analytical tool.

The system takes into account selected documents only if they lie within the KPI calculation horizon (partly or

completely). This horizon is determined automatically based on the planning horizon. It starts seven days before the end

date of the planning horizon and ends at the same date as the planning horizon. If the planning horizon is less than

seven days, the calculation horizon starts with the planning horizon. If the planning horizon lies entirely in the future, the

start date of the KPI calculation horizon is moved to the current date.

KPIs that are not displayed in the transportation cockpit don't have a negative impact on the performance.

If you work with multiple windows, the KPIs screen area is displayed on the main window only.

## Related Information

Calculation of Distances Traveled With or Without Load

Use of Hierarchical Views

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

119


1/14/26, 2:19 PM

You organize the view in the transportation cockpit by creating hierarchical views for freight orders, freight bookings, and

transportation units (trailer units, railcar units, container units, and package units).

If you organize these business documents into hierarchies, you can filter and sort various areas in the transportation cockpit

according to specific criteria, such as the vehicle resource.

Defining hierarchical views simplifies your rescheduling activities and the coupling and uncoupling of trailers. For more

information, see Reassignment and Use of Trailers.

## Prerequisites

In Customizing, you have made the relevant settings so that you can configure your standard layout for rescheduling in the

layout settings for the transportation cockpit.

The following hierarchy types are predefined by default:

FBSEA for planning activities in sea transportation

FBAIR for planning activities in air transportation

FOLD for planning activities in overland transportation

FORAI for planning activities in rail transportation

FUSTG for planning freight unit stages

## PUSTG for planning package unit stages

FPSTG for planning freight unit stages and package unit stages

TUTRL for location-based planning of trailer units with the assigned freight units

TUTRS for stage-based planning of trailer units with the assigned freight units

TURAI for location-based planning of railcar units with the assigned freight units

TURAS for stage-based planning of railcar units with the assigned freight units

TUCNT for location-based planning of container units with the assigned freight units

TUCLD for location-based planning of container units with the assigned freight documents

TUCNS for stage-based planning of container units with the assigned freight units

TUCSD for stage-based planning of container units with the assigned freight documents

TUPCK for location-based planning of package units with the assigned freight units

TUPLD for location-based planning of package units with the assigned freight documents

TUPUS for stage-based planning of package units with the assigned freight units

TUPSD for stage-based planning of package units with the assigned freight documents

## TUCO for planning consignment orders

## TUCOC for capacity document-based planning of consignment orders

You can also define hierarchies with separate hierarchy types and groupings and a view switch. You can specify the function

(consumer) that each hierarchy type can use. For more information, see Customizing for Transportation Management

under  Planning

## General Settings

 Define Hierarchical Views for Business Documents .

This is custom documentation. For more information, please visit SAP Help Portal.

120


1/14/26, 2:19 PM

You have defined a layout in the layout settings for the transportation cockpit in which you have assigned a hierarchy type

to the corresponding hierarchies on the Transportation Units Area, Orders Area; Requirements Area or Hierarchies Area

tab pages.

If you do not make this assignment, the system uses the applicable default hierarchy type. For more information, see Use of Profile

and Layout Sets.

## Features

In the transportation cockpit, you can show hierarchies as alternative order lists. You can define grouping levels for each hierarchy

level and specify whether the grouping level in question is expanded by default when displayed in the transportation cockpit.

If you organize freight orders, freight bookings, or transportation units into hierarchies, you can filter and sort various areas in the

transportation cockpit according to specific criteria, such as the vehicle resource.

Creation of Capacity Documents from Freight Units

## Use

When planning manually, use this process to assign freight units to any of the following documents:

Freight documents:

Road freight order

Rail freight order

Air freight booking

Ocean freight booking

Transportation units:

Container unit

Trailer unit

Railcar unit

Package unit

## Prerequisites

For more information, see Manual Planning.

## Process

1. In the transportation cockpit, select the freight units you want to assign to a capcity document, that is a freight document

or a transportation unit. You can select the freight units either in the freight unit hierarchy or on the map, if displayed.

Alternatively, you can also select freight unit stages.

2. On the respective toolbar, click the Create Capacity Document or Create Multiple Capacity Documents pushbutton to

display the list of documents you can create.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

121


1/14/26, 2:19 PM

The number of multiple documents created depends on how the setting Rule for Creating Capacity Documents

is configured ( Edit Planning Profile

 Manual Planning Settings tab ). The system creates either a document

per freight unit (default) or a document for each freight unit stage.

If you have multiple types of a capacity documents, you can specify which type is used by default in the planning

profile. Alternatively, you can use the Change Planning Settings to temporarily overrule the default setting for

the duration of the session.

3. In the menu, select the capacity document you want to create.

The capacity documents are created but you can still edit and add to them as you continue planning. For more information,

see Manual Planning.

  Note

If you create a freight document for one or more freight unit stages generated from a delivery-based or order-

based transportation requirement, the system determines the freight document type from the information about

the respective default business document type that you entered in the planning profile. However, if you have

assigned a schedule to one of the stages, the system determines the freight document type from the

Customizing activity Define Schedule Types. For more information, see the Creation of a Freight Document for

Several Stages section of Direct Creation of Freight Documents and Selection of Schedules.

If execution information already exists for a business document such as a freight order, the system cannot

change the corresponding transportation stop during manual planning or vehicle scheduling and routing (VSR)

optimization. Examples of execution information include a freight unit that has already been loaded or a freight

order that has already been delivered to a location.

Creation of Capacity Documents from Resources

## Use

You use this process to create capacity documents in the transportation cockpit on the basis of resources (such as trucks, trailers,

railcars, containers, and schedules). If required, you can also create blank capacity documents (that is, capacity documents that

do not contain a freight unit), which you can then process at a later time.

## Prerequisites

See Manual Planning.

## Process

1. You open the Transportation Cockpit app on the launchpad. For more information, see Starting the Transportation Cockpit.

2. On the relevant tab page, you select one or more resources and choose the corresponding pushbutton to create a capacity

document for your resource type. Alternatively, you assign freight units to the required resources using drag and drop or

Assign Selected Items.

If you create capacity documents from vehicle resources, railcars, trailers, or containers, the system displays a

dialog box in which you must enter the appropriate capacity document type (the system proposes the document

type specified in the planning profile or, if no document type is specified here, it proposes the default document type

from the corresponding Customizing activity (Define Freight Order Types or Define Freight Booking Types for

This is custom documentation. For more information, please visit SAP Help Portal.

122


1/14/26, 2:19 PM

freight orders and freight bookings and Define Transportation Unit Types for transportation units)). Note that you

do not have to enter the location data at this point. You can create capacity documents without location data.

If you create blank capacity documents from schedules or departures, the system displays a dialog box in which you

must enter the appropriate capacity document type (the system proposes the document type specified in the

Customizing activity Define Schedule Types). Note that if you create capacity documents on the basis of a

schedule, the system creates one capacity document for each departure belonging to the selected schedule.

Alternatively, you can create freight documents for one or more schedule departures.

When you create a capacity document by assigning a freight unit to a schedule or schedule departure, the system

adds the locations specified in the freight unit to the capacity document.

  Note

You can also create blank freight orders in the Freight Orders/Freight Bookings area of the transportation

cockpit by choosing the New pushbutton and then the Freight Order option.

You can create blank road freight orders in the Road Freight Order Hierarchy and in the Road Freight Orders

area of the transportation cockpit by choosing the New Road Freight Order pushbutton.

You can create blank road freight orders in the Road Freight Order Hierarchy and in the Road Freight Orders

area of the transportation cockpit by choosing the New Road Freight Order pushbutton.

3. You carry out any subsequent planning activities.

For more information, see Manual Planning.

4. You check your planning.

The system performs a consistency check during which it checks incompatibilities, for example.

5. You start scheduling.

The system performs backward or forward scheduling. Note that if you do not complete this step, dates and times may be

incorrect.

6. You save the planning results.

## Creation of Capacity Documents Based on Requirement Groups

You can create capacity documents based on requirement documents that are grouped according to specific attributes.

## Prerequisites

You have defined requirement grouping profiles in the Create Requirement Grouping Profile app on the launchpad and

specified grouping rules and capacity limits. SAP delivers several grouping rules but you can also define your own grouping

rules in Customizing (see below).

For example, you can indicate in your requirement grouping profile that requirement documents are to be grouped by

source or destination location when you want to create road freight orders.

You have defined capacity document creation settings in the Create Capacity Document Creation Settings app and

specified a requirement grouping profile per capacity document category.

Note that if you do not specify a requirement grouping profile, all requirement documents are placed into the same group.

Optionally, you have defined your own grouping rules. For more information, see Customizing for Transportation

Management under  Planning

## General Settings

 Define Grouping Rules for Requirement Grouping .

This is custom documentation. For more information, please visit SAP Help Portal.

123


1/14/26, 2:19 PM
## Use

## Requirement grouping

The generic grouping framework first groups requirement document stages, such as freight unit stages, based on a list of

attributes, for example, source location or carrier. The attributes are represented by grouping rules.

The system applies the maximum capacity limit to these groups of requirement document stages. That means, groups above the

maximum capacity limit are split into smaller groups so that the resulting freight document that is created for each group fits into

a vehicle resource or equipment type. A set of grouping rules and capacity limits is bundled in a requirement grouping profile.

In the requirement grouping profile, you can also specify incompatibility settings as a further criterion for the grouping. Note,

however, that you must have selected the Identical Values Only checkbox in your incompatibilities for them to be considered.

## Creation of capacity documents

For all groups of requirement document stages that are above the minimum capacity limit, the system creates a capacity

document. All groups of requirement document stages that are below the minimum capacity limit remain unplanned that means,

no freight document is created for them. Single requirement document stages that are bigger than the maximum capacity limit

also remain unplanned.

## Activities

In the transportation cockpit, select requirement document stages. For these stages select Create Capacity Documents Based on

Groups and then the requested capacity document category, for example Create Road Freight Orders Based on Groups.

For more information about the allowed combinations of requirement documents and capacity documents, see Supported

Combinations of Document Types.

To run the creation of capacity documents based on requirement groups in the background, on the SAP Easy Access screen,

choose  Logistics

 Transportation Management

 Administration

 Background Processing

## Create Capacity Documents

Based on Groups . For more information, see Creation of Capacity Documents Based on Requirement Groups.

Related Information

Planning Profile

## Incompatibilities

## Supported Combinations of Document Types

The type of requirement document selected affects the type of capacity document allowed.

The following combinations of requirement document types and capacity document types are allowed during capacity document

creation based on requirement groups:

Freight units (FUs):

All capacity document types are allowed.

Package units (PUs):

Road freight orders

## Consignment orders

This is custom documentation. For more information, please visit SAP Help Portal.

124


1/14/26, 2:19 PM

Trailer units

Container units

Trailer units (TUs):

Only road freight orders are allowed.

Railcar units (RUs):

Only rail freight orders are allowed.

Container units (CUs):

Road freight orders

Rail freight orders

Ocean freight bookings

Air freight bookings

Trailer units

## Railcar units

Consignment orders (COs):

Road freight orders

Rail freight orders

Ocean freight bookings

Air freight bookings

Trailer units

Railcar units

## Container units

The table below displays the supported combinations of document types: green indicates a supported combination, while yellow

indicates an unsupported combination.

Supported combinations

Requirement

Road FOs

Rail FOs

Ocean

Air FBs

COs

TUs

RUs

CUs

## PUs

Docs/Capacity

Docs

FBs

FUs

PUs

TUs

RUs

CUs

COs

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

## Yes

This is custom documentation. For more information, please visit SAP Help Portal.

125


1/14/26, 2:19 PM

## Manual Planning with Local Transportation Unit Items

In the transportation cockpit, you can create transportation units as freight document items instead of separate business

documents.

This is useful in scenarios in which you don’t need a separate business document for your trailer, railcar, or container. The freight

document contains all relevant information.

## Prerequisites

In the manual planning settings of your planning profile, you have selected Create TU as Freight Document Item in the

Create TU Item or TU Document field.

If you work with containers, you have also specified the target document category of the freight document, such as Air

Freight Booking, in the Target Document Category for Container field of the manual planning settings.

## Use

If you perform manual planning by assigning freight units to railcar resources, trailer resources, or container resources or railcar

types, trailer types, or container types using drag and drop or Assign Selected Items for example, the system creates a

transportation unit (TU) item in the corresponding freight document locally (a local trailer item, for example) instead of a separate

TU document, such as a trailer unit.

Examples:

You assign a freight unit to a trailer type by selecting Assign Selected Items. The system creates a road freight order with a

local item for the trailer.

You assign a freight unit to a container resource using drag and drop. The system automatically creates an ocean freight

booking with a local item for the container if you have selected Ocean Freight Booking as the target document category in

the manual planning settings.

You assign a railcar type to a rail freight order using drag and drop. The system automatically creates a railcar item in the

rail freight order locally.

In the rail freight order hierarchy, you can manually insert a railcar with or without a railcar type:

## Insert Railcar with Railcar Type

You insert a railcar with a railcar type into the rail freight order and indicate the number of railcar items that the system is to

create. The system creates the indicated number of railcar items in the rail freight order locally.

## Insert Railcar

You insert a railcar without a railcar type into the rail freight order. The system creates a railcar item in the rail freight order

locally. Then you can assign a railcar type to this railcar item using drag and drop, for example.

In the same way, you can insert a trailer with or without a trailer type in the road freight order hierarchy or insert a container with

or without a container type in the air freight booking hierarchy or ocean freight booking hierarchy.

Once the local TU item is created, you can do the following, for example:

You can assign a container type to a local container item using drag and drop.

You can reassign a container item from one air freight booking to another using drag and drop.

This is custom documentation. For more information, please visit SAP Help Portal.

126


1/14/26, 2:19 PM

You can change the railcar type, trailer type, or container type in the freight order or freight booking hierarchy using the

Equipment Type and Equipment Group fields. You can also use these fields to add railcar types, trailer types, or container

types or remove them.

Unified package building considers product items and package items in local trailer items and local container items. You can

perform unified package building either for the entire road freight order or for selected local trailer items or local container items.

You can also remove packages from selected local trailer items and local container items.

  Note

Load planning doesn't support local TU items.

Load consolidation doesn’t support local TU items. That means, the system always creates a separate TU document

even if you have specified in the manual planning settings that a local TU item is to be created.

Vehicle scheduling and routing and the generation of transportation proposals don’t support local TU items.

Related Information

## Planning Profile

Assignment of Requirement Documents to Existing Capacity
Documents

## Use

You use this process to assign requirement documents, such as freight units, to existing capacity documents, such as freight

orders.

## Prerequisites

See Manual Planning.

## Process

1. You open the Transportation Cockpit app.

For more information, see Starting the Transportation Cockpit.

2. You can select how the requirement documents are to be assigned by making settings in Manual Planning Settings, under

Document Assignment.

For example, you can control how the location sequence of the capacity document is to be extended. For more information,

see the corresponding field help.

3. You choose one or more requirement documents and assign them to an existing capacity document by using drag and

drop. Alternatively, you can enter a command in the command field or select one or more requirement documents and a

capacity document and choose Assign Selected Items.

4. You carry out any subsequent planning activities.

For more information, see Manual Planning.

This is custom documentation. For more information, please visit SAP Help Portal.

127


1/14/26, 2:19 PM

5. You check your planning.

The system performs a consistency check during which it checks incompatibilities, for example.

6. You start scheduling.

The system performs backward or forward scheduling. Note that if you do not complete this step, dates and times may be

incorrect.

7. You save the planning results.

## Related Information

Document Assignment When Execution Has Already Started

## Document Assignment When Execution Has Already Started

You may need to assign a requirement document, such as a freight unit, to a capacity document, such as a road freight order, even

after the execution of the capacity document has already started or has already been completed.

  Note

These features also apply to warehouse loading and unloading stops in Advanced Shipping and Receiving.

## Correcting the Capacity Document

One reason this situation occurs is when there is a mismatch between the information in the capacity document and what is

actually happening, or has already happened, at the time of loading or unloading. Sometimes during loading or unloading,

additional cargo items that are not assigned to the capacity document are loaded or unloaded along with the items that are

already assigned. To correct this, you can update the capacity document by assigning the additional items to the same stop.

If the processing of the items has not yet started, the statuses of the new items match the statuses of the other items in the

capacity document.

However, if you add a requirement document after the vehicle has loaded or unloaded the goods at the stop, has checked out, or

has departed, then the status of the items added later doesn't match the status of the stop and of the other items in the capacity

document. You can correct these errors using document error handling.

For further information, see Late Changes to Capacity Documents.

## Creating New Stops

A different reason this situation occurs is if cargo items have not been loaded or unloaded where and when they should have been,

and you want the vehicle to return to load or unload these items.

If you were to follow the same procedure as above, and correct the capacity document, the status of the items would not reflect

reality. Therefore, instead of reusing a stop that has already been executed, you create a new stop for the same location. The

system automatically adapts the routing of the capacity document so the vehicle can return and load or unload a second time at

the location.

To do this, under Manual Planning Settings, choose Consider Handling Execution Status. This means that when you assign a

requirement document to a capacity document during manual planning, the system disregards those stops where the status is

This is custom documentation. For more information, please visit SAP Help Portal.

128


1/14/26, 2:19 PM

Checked Out or Departed. If necessary, it creates a new stop for the same location. This means that the handling execution status

of stops and the requirement items is consistent.

  Note
The setting only takes effect when you assign the requirement document to the capacity document header. If, for example, you

assign a freight unit directly to a freight order location, the system uses the freight order location you choose.

You can make further settings as to where exactly the stop should be inserted under Extension Strategy for Location Sequence

of Capacity Documents; for example, you can choose to insert the new stop where the distance added to the total is the least. For

more information, see the corresponding field help.

## Advanced Shipping and Receiving

If you are using this feature in Advanced Shipping and Receiving, the system also considers the handling execution status of

warehouse loading and unloading stops. For example, if loading is completed for a warehouse loading stop, but you want to add

another freight unit, the system creates a new warehouse loading stop for the same location, if the truck has not yet checked out

from the shipping or receiving point.

However, in the Advanced Shipping and Receiving inbound scenario, the system ignores the Consider Handling Execution Status

setting if it can only determine stops that have already been executed with the correct location in the stop sequence. In this case,

the system assigns the freight unit to a previously executed stop. The procedure is then as described in Late Changes to Capacity

Documents. However, if the system determines a stop that has not yet been executed at the correct location, then it assigns the

freight unit to this stop.

Reassignment

## Use

In the transportation cockpit, you can use this function to reschedule freight documents by using drag and drop. Alternatively, you

can reassign freight documents by selecting the relevant rows and choosing the Reassignment pushbutton. For example, you can

assign a freight unit to a new freight order if the scheduled delivery date is moved.

## Prerequisites

In the layout settings for the transportation cockpit, you have defined a layout for which you have selected the

Reassignment checkbox on the Orders Area or Transportation Units Area tab page. Alternatively, you can select the

Reassignment checkbox on the Hierarchies Area tab page. For more information, see Use of Profile and Layout Sets.

In Customizing, you have made the relevant settings so that you can configure your standard layout for rescheduling in the

layout settings for the transportation cockpit.

The standard system contains a range of predefined hierarchy types. In addition, you can define your own hierarchy types.

For more information, see Customizing for Transportation Management under  Planning

 General Settings

## Define

Hierarchical Views for Freight Documents .

## Features

Once you have configured the relevant settings in Customizing and in the layout settings for the transportation cockpit, you can

also use various hierarchy levels as drag and drop sources and targets in the hierarchy in question. For more information, see

Reassignment Activities.

This is custom documentation. For more information, please visit SAP Help Portal.

129


1/14/26, 2:19 PM
## Activities

You select the layout that you have defined in the layout settings for the transportation cockpit. In the Freight Orders/Freight

Bookings screen area, you choose the Dual View pushbutton. You can now execute your reassignment activities.

Related Information

Use of Hierarchical Views

## Reassignment Activities

Once you have configured the relevant settings in Customizing and in the layout settings for the transportation cockpit (see

Reassignment), you can use the following hierarchy levels as drag and drop sources and targets within the various hierarchies:

  Note

The drag and drop source and the drag and drop target is always interchangeable.

Freight Order Hierarchies (Road Freight Order Hierarchy and Rail Freight Order Hierarchy)

Drag and Drop Source

Drag and Drop Target

System Activity

Freight order

## Transportation unit

You couple the part of the transportation

unit that is not yet coupled to the freight

order.

  Note

The coupling locations must already be

available in both documents.

Location in freight order

Another location in the freight order

You change the positions of the locations in

question in the location sequence. This also

transfers the requirements assigned to the

location to the location in its new position in

the sequence. This type of planning enables

you to stop at the same location twice in

succession in the same freight order.

  Note

If you add a location at which a freight

unit is unloaded to the location

sequence of another freight order, the

system checks whether the location at

which the relevant freight unit is loaded

also exists in the freight order.

If this location is already included in the

freight order, the system enhances only

those requirements for this location.

If the location is not included in the

freight order, the system adds it to the

freight order with the corresponding

requirements.

This is custom documentation. For more information, please visit SAP Help Portal.

130


1/14/26, 2:19 PM

Drag and Drop Source

Drag and Drop Target

## System Activity

The same applies if you add a location at

which a freight unit is loaded to the

location sequence of another freight

order. In this case, the system checks

whether the location at which the freight

unit is unloaded already exists in the

freight order and carries out the relevant

planning operations.

Location in freight order

Same location in freight order

You transfer the requirements assigned to

the location acting as the drag & drop

source to the location acting as the drag &

drop target. If the location does not exist in

the freight order, this action adds the

location to the location sequence of the

freight order. At the same time, you delete

the location acting as the drag & drop

source from the location sequence of the

freight order to which the location and its

requirements was originally assigned.

  Note

If you add a location at which a freight

unit is unloaded to another freight order,

the system checks whether the location

at which the relevant freight unit is

loaded also exists in the freight order.

If this location is already included in the

freight order, the system enhances only

those requirements for this location.

If the location is not included in the

freight order, the system adds it to the

freight order with the corresponding

requirements.

The same applies if you add a location at

which a freight unit is loaded to another

freight order. In this case, the system

checks whether the location at which

the freight unit is unloaded already

exists in the freight order and carries out

the relevant planning operations.

You transfer the requirements assigned to

the location acting as the drag & drop

source to the same location in the freight

order acting as the drag & drop target. At

the same time, you delete the location

acting as the drag & drop source from its

original position in the location sequence.

  Note

If you add a location at which a freight

unit is unloaded to the location

Location in freight order

## Freight order

This is custom documentation. For more information, please visit SAP Help Portal.

131


1/14/26, 2:19 PM

Drag and Drop Source

Drag and Drop Target

## System Activity

sequence of another freight order, the

system checks whether the location at

which the relevant freight unit is loaded

also exists in the freight order.

If this location is already included in the

freight order, the system enhances only

those requirements for this location.

If the location is not included in the

freight order, the system adds it to the

freight order with the corresponding

requirements.

The same applies if you add a location at

which a freight unit is loaded to the

location sequence of another freight

order. In this case, the system checks

whether the location at which the freight

unit is unloaded already exists in the

freight order and carries out the relevant

planning operations.

You assign the freight order stage to the

transportation unit and add missing

locations to the location sequence for the

transportation unit.

You assign the freight unit stage to the

freight order and add missing locations to

the freight order.

Freight order stage

Transportation unit

Freight unit stage

Freight order

## Freight unit stage

Compartment of a freight order

You assign the freight unit stage to the

compartment of a freight order and add

missing locations to the freight order.

Freight unit stage

## Location in freight order

You assign the freight unit stage to the

Freight unit stage

## Transportation unit

freight order and add missing locations to

the freight order. At the same time, you

integrate the newly assigned location into

the location sequence at the position

predefined by the location.

You assign the freight unit stage to the

transportation unit and add missing

locations to the transportation unit.

Transportation Unit Hierarchies (Trailer Unit Hierarchy and Railcar Unit Hierarchy)

Drag and Drop Source

Drag and Drop Target

System Activity

Transportation unit

## Freight order

You couple the part of the transportation

unit that is not yet coupled to the freight

order.

  Note

The coupling and uncoupling locations

must already be assigned to both

This is custom documentation. For more information, please visit SAP Help Portal.

132


1/14/26, 2:19 PM

Drag and Drop Source

Drag and Drop Target

System Activity

documents.

Location in the transportation unit

Other location in the transportation unit

You change the positions of the locations in

question in the location sequence. At the

same time, you transfer the requirements

assigned to the location to the location in

its new position in the sequence.

  Note

If you add a location at which a freight

unit is unloaded to the location

sequence of another transportation unit,

the system checks whether the location

at which the relevant freight unit is

loaded also exists in the transportation

unit.

If this location is already included in the

transportation unit, the system

enhances only those requirements for

this location.

If the location is not included in the

transportation unit, the system adds it

to the transportation unit with the

corresponding requirements.

The same applies if you add a location at

which a freight unit is loaded to the

location sequence of another

transportation unit. In this case, the

system checks whether the location at

which the freight unit is unloaded

already exists in the transportation unit

and carries out the relevant planning

operations.

Location in the transportation unit

Same location in the transportation unit

You assign the freight units that were

assigned to the drag & drop source to the

drag & drop target. At the same time, you

delete the drag & drop source from the

location sequence.

  Note

If you add a location at which a freight

unit is unloaded to the location

sequence of another transportation unit,

the system checks whether the location

at which the relevant freight unit is

loaded also exists in the transportation

unit.

If this location is already included in the

transportation unit, the system

enhances only those requirements for

this location.

This is custom documentation. For more information, please visit SAP Help Portal.

133


1/14/26, 2:19 PM

Drag and Drop Source

Drag and Drop Target

## System Activity

If the location is not included in the

transportation unit, the system adds it

to the transportation unit with the

corresponding requirements.

The same applies if you add a location at

which a freight unit is loaded to the

location sequence of another

transportation unit. In this case, the

system checks whether the location at

which the freight unit is unloaded

already exists in the transportation unit

and carries out the relevant planning

operations.

Location in the transportation unit

## Transportation unit

You transfer the requirements assigned to

the location acting as the drag & drop

source to the same location in the

transportation unit acting as the drag &

drop target. At the same time, you delete

the location acting as the drag & drop

source from its original position in the

location sequence.

  Note

If you add a location at which a freight

unit is unloaded to the location

sequence of another transportation unit,

the system checks whether the location

at which the relevant freight unit is

loaded also exists in the transportation

unit.

If this location is already included in the

transportation unit, the system

enhances only those requirements for

this location.

If the location is not included in the

transportation unit, the system adds it

to the transportation unit with the

corresponding requirements.

The same applies if you add a location at

which a freight unit is loaded to the

location sequence of another

transportation unit. In this case, the

system checks whether the location at

which the freight unit is unloaded

already exists in the transportation unit

and carries out the relevant planning

operations.

You assign the freight unit stage to the

transportation unit and add missing

locations to the transportation unit. At the

same time, you integrate the newly

Location in the transportation unit

## Freight unit stage

This is custom documentation. For more information, please visit SAP Help Portal.

134


1/14/26, 2:19 PM

Drag and Drop Source

Drag and Drop Target

System Activity

Freight order

Transportation unit

Transportation unit stage

## Freight order

assigned location into the location

sequence at the position predefined by the

location.

You couple the part of the transportation

unit that is not yet coupled to the freight

order.

  Note

The coupling and uncoupling locations

already exist in both documents.

You couple the transportation unit stage to

the freight order and add missing locations

to the freight order.

## Freight unit stage

Compartment in the transportation unit

You assign the freight unit stage to the

compartment of a transportation unit and

add missing locations to the transportation

unit.

Freight unit stage

## Transportation unit

You assign the freight unit stage to the

transportation unit and add missing

locations to the transportation unit.

## Freight unit stage

Location in the transportation unit

You assign the freight unit stage to the

Freight unit stage

## Freight order

transportation unit and add missing

locations to the transportation unit. At the

same time, you integrate the newly

assigned location into the location

sequence at the position predefined by the

location.

You assign the freight unit stage to the

freight order and add missing locations to

the freight order.

  Note
The freight order is included in the transportation unit hierarchy as information only. All of the planning operations listed in the

table above that have a freight order as the drag & drop source or target are exclusively cross-hierarchy planning operations

between the freight order hierarchy and the transportation unit hierarchy. These planning operations cannot be carried out in

the transportation unit hierarchy using drag & drop.

Freight Booking Hierarchies (Air Freight Booking Hierarchy and Ocean Freight Booking Hierarchy)

Drag and Drop Source

Drag and Drop Target

System Activity

Freight unit stage

## Freight booking

You assign the freight unit stage to a freight

booking.

Freight unit stage

## Capacity reservation

You assign a full-container-load freight unit

stage to the capacity reservation. At the

same time, you replace the container from

the capacity reservation with the full-

This is custom documentation. For more information, please visit SAP Help Portal.

135


1/14/26, 2:19 PM

Drag and Drop Source

Drag and Drop Target

System Activity

Freight unit stage

## Container

container-load freight unit if the container

type matches.

You assign a less-than-container load

freight unit stage to a container.

  Note

The container must be part of the freight

booking.

Drag and Drop Source

Drag and Drop Target

System Activity

Freight Unit Hierarchy

Freight unit stage

## Freight order

You assign the freight unit stage to the

freight order and add missing locations to

the freight order.

Freight unit stage

## Location in freight order

You assign the freight unit stage to the

freight order and add missing locations to

the freight order. At the same time, you

integrate the newly assigned location into

the location sequence at the position

predefined by the location.

Freight unit stage

## Transportation unit

You assign the freight order stage to the

transportation unit and add missing

locations to the location sequence for the

transportation unit.

## Freight unit stage

Compartment of a freight order

You assign the freight unit stage to the

compartment of a freight order and add

missing locations to the freight order.

## Freight unit stage

Location in the transportation unit

You assign the freight unit stage to the

transportation unit and add missing

locations to the transportation unit. At the

same time, you integrate the newly

assigned location into the location

sequence at the position predefined by the

location.

## Freight unit stage

Compartment in the transportation unit

You assign the freight unit stage to the

compartment of a transportation unit and

add missing locations to the transportation

unit.

Freight unit stage

## Freight booking

You assign the freight unit stage to a freight

booking.

Freight unit stage

## Capacity reservation

You assign a full-container-load freight unit

stage to the capacity reservation. At the

same time, you replace the container from

the capacity reservation with the full-

container-load freight unit if the container

type matches.

This is custom documentation. For more information, please visit SAP Help Portal.

136


1/14/26, 2:19 PM

Drag and Drop Source

Drag and Drop Target

System Activity

Freight unit stage

## Container

You assign a less-than-container load

freight unit stage to a container.

  Note

The container must be part of the freight

booking.

  Note

All of the planning operations listed here are possibly only if either the drag & drop source or the drag & drop target do not

originate from the freight unit hierarchy.

Drag and Drop Source

Drag and Drop Target

## System Activity

Container Unit Hierarchy

Container unit stage

## Freight order

You assign the container unit stage to the

freight order and add missing locations to

the freight order.

Container unit stage

## Location in freight order

You assign the container unit stage to the

freight order and add missing locations to

the freight order. At the same time, you

integrate the newly assigned location into

the location sequence at the position

predefined by the location.

Container unit stage

Compartment in freight order

You assign the container unit stage to the

Container unit stage

## Railcar unit

compartment of a freight order and add

missing locations to the freight order.

You assign the container unit stage to the

railcar unit and add missing locations to the

location sequence for the railcar unit.

Container unit stage

Location in the railcar unit

You assign the container unit stage to the

Container unit stage

## Trailer unit

railcar unit and add missing locations to the

railcar unit. At the same time, you integrate

the newly assigned location into the

location sequence at the position

predefined by the location.

You assign the container unit stage to the

trailer unit and add missing locations to the

location sequence for the trailer unit.

Container unit stage

Location in the trailer unit

You assign the container unit stage to the

Container unit stage

## Freight booking

trailer unit and add missing locations to the

trailer unit. At the same time, you integrate

the newly assigned location into the

location sequence at the position

predefined by the location.

You assign the container unit stage to a

freight booking and add missing locations

to the container unit.

This is custom documentation. For more information, please visit SAP Help Portal.

137


1/14/26, 2:19 PM

Interactive Planning on the Map

## Use

This function allows you to switch to a display of a map in the transportation cockpit (visual transportation cockpit) and perform

planning there.

## Prerequisites

In Customizing for Transportation Management under  Basic Functions

 Geographical Map

 Define Settings for

Geographical Map , you have activated the map display.

You have defined a georouting strategy (optional). You can define georouting strategies in Customizing for Transportation

Management under  Basic Functions

## Geographical Map

 Define Settings for Geographical Map . Note that the

system ignores these strategies if you have defined more specific georouting strategies under  Master Data

 Transportation Network

## Transportation Lane

 Distance and Duration Determination

## Define Strategy for Distance

and Duration Determination and Georouting . For more information, see Settings for Distance and Duration

Determination.

If you want to use the map in the transportation cockpit, you have defined a page layout that includes the map. You do this

by opening the Define Page Layouts for Transportation Cockpit app on the launchpad. For more information about page

layouts for the transportation cockpit, see Use of Profile and Layout Sets.

If you want to use your own layout for the map display in the transportation cockpit, transportation network cockpit, or in

the document overviews, you must have created your own layout for the map display in Customizing for Transportation

Management under  Basic Functions

## Geographical Map

 Define Layouts for Geographical Map . In your layout, for

example, you can do the following:

You can activate the display of the Aggregated Information window and specify whether only requirement

documents or requirement documents and freight documents are to be considered.

You can specify which colors are to be used on the map.

You can specify that certain information is to be displayed as a tooltip or label.

You can specify that the first or last stage of a freight order, or both stages, are to be hidden.

You can specify that a specific map content is used for this layout by entering a country in the Context "Country"

field.

## Features

## Adding Objects to the Map

All objects listed in the transportation cockpit can be displayed on the map for reference and interactive planning.

You can use the following methods for adding objects to the map individually or in combination with each other:

Using the Update Map dropdown list.

The dropdown list on the application toolbar includes multiple functions for adding and removing objects to and from the

map.

Toggling an object’s action button.

In the transportation cockpit tables, toggling an object's action button adds or removes the object to or from the map. (To

display the actions buttons, in the transportation cockpit page layout, click the details button in the area's Actions column

This is custom documentation. For more information, please visit SAP Help Portal.

138


1/14/26, 2:19 PM

and then select the options Add to Map and Remove from Map.)

Selecting the object.

In Customizing, you can specify that when you select an object in the transportation cockpit, it is immediately displayed on

the map and remains displayed until deselected. You can activate this function under  Transportation Management

 Basic Functions

## Geographical Map

 Define Layouts for Geographical Map  and select the option Quick Add.

If you select the Quick Add option, you can specify the selection behavior:

o Selection on the map overrules the selection on the transportation cockpit by document or resource type only.

Selection on the map overrules the selection on the transportation cockpit completely.

To specify that the objects you add to the map continue to be displayed even after you refresh the transportation cockpit, select

the KeepObject setting in Customizing under  Transportation Management

 Basic Functions

 Geographical Map

## Define

Layouts for Geographical Map

 Layouts .

To ensure the map fulfills your requirements, you can use the Display Profile dialog (on the map toolbar, click Show Display

Profile) to specify how objects are represented on the map and what object information is displayed. Additionally, you can specify

if the objects you add to the map are displayed or hidden depending on their status.

Also, when adding objects to the map, the Aggregated Information window in the map area updates automatically to display the

current total weight and volume of the displayed objects (requirement documents). If you have selected Consider All Documents

in Aggregated Information Window in Customizing, freight documents are considered as well. If you select a freight document, all

stops and stages of this freight document are selected. The weight and volume of the most critical stage of the freight document

are considered. If you only select a stop, the weight and volume of the assigned requirement documents (that are loaded or

unloaded at this stop) are considered.

## Planning Functions

You can carry out your planning on the map. If you select unplanned freight units and start planning from the context menu, for

example, the system shows the possible assignments of the freight units to the resources. Select the assignments that you

require.

You can also assign unplanned freight units or multirelations that contain unplanned freight units to resources by using drag and

drop. When you do so, you can either assign the freight units to the resource or the resource to the freight units. You can use the

proximity search in the context menu to find unplanned freight units and transportation units that are within a specific radius of a

resource or a location.

If you want to split a stage that is displayed on the map, you can assign an unplanned freight unit or multirelation to a location

using drag and drop. Once you have selected the required planning option, the system adds the selected location to the freight unit

stage and updates the map accordingly. This process also applies to freight orders.

You can also display transshipment locations that are not part of your currently selected planning activities. You display these

locations by choosing Show Assigned Transshipment Locations from the context menu.

In the context menu for a freight unit, you can add locations.

If a freight order does not have a vehicle assigned to it, you can also assign the vehicle by using drag and drop. To do so, you assign

the freight order to a single vehicle resource or a multispot that contains at least one vehicle resource or passive vehicle resource

and select the relevant planning option from the menu. You can use the proximity search in the context menu to find available

resources that are within a specific radius. You can also specify the exact position of a resource at any time in the context menu of

the map.

You can also assign a road freight order to another road freight order using drag and drop. Its stages are added to the target road

freight order and then it is deleted.

This is custom documentation. For more information, please visit SAP Help Portal.

139


1/14/26, 2:19 PM

In the case of resources on the map, you can find the assigned business documents by selecting the corresponding option from

the context menu for the resource. The system searches for already planned freight orders and adds these to the map.

You can use the context menu of the map to do the following for example:

Display different colors for multiple business documents selected simultaneously. This enables you to better differentiate

between the documents. The color of each respective document is displayed in the Color column in the document list.

Hide the first or last stage of a freight order or both stages.

The system displays all of your transportation planning activities on the map. When you leave the display of the map, your

planning activities are also displayed in the table view of the transportation cockpit.

More Information

Map Display

## Map Functions

Gantt Chart for Transportation Planning

## Use

The Gantt chart provides a visual platform for performing transportation planning. With an intuitive and graphical user interface,

the Gantt chart enables you to perform transportation planning visually, interactively, and more efficiently.

## Prerequisites

You have defined the following for the Gantt chart:

Color schemes and patterns

Label schemes and tooltips

Fields and field lists

## Hierarchies, views, and layouts

For more information, see Customizing for Transportation Management under  Basic Functions

 Gantt Chart

.

## Features

The Gantt chart has the following features:

## Transparent availability of resources and drivers

The chart panel presents you with an overview of the availability of vehicle resources, handling resources, and drivers over

time. For example, different colors indicate whether a truck has a document assigned to it, or whether it is traveling, in

downtime, or in non-working time. You can also check whether a handling resource is available or in downtime at a location

and if a drivers is available or if he is absent. Not just handling resources, you can use the Operating Time Calendar

hierarchy to visualize the operating time configured for a specific location. The Operating Time Calendar displays the non-

working times and activities occurring in that location. These activities are: loading, unloading, prepare, and finalize. The

hierarchy also displays the overlaps of loading activities.

This is custom documentation. For more information, please visit SAP Help Portal.

140


1/14/26, 2:19 PM

For more detailed information on how to enable operating times in Gantt Chart, see SAP Note 2671572

## Visibility of utilization of resources

You can display the level of consumed capacity of a vehicle resource at a specific point in time by choosing

. The system

displays the utilization curve of the selected vehicle resource in the chart panel. The tooltip along the utilization curve

displays the loading utilization of a vehicle resource in terms of volume, weight, alternative quantity, or normalized quantity,

depending on your settings in Customizing. The tooltip along the utilization line of a handling resource presents you with

information on the available capacity, required capacity, and over-capacity of this handling resource at a specific point in

time. By choosing

, you can display loading or unloading activities that are planned for a handling resource at different

times.

## Option to display or hide document separators in the Gantt chart

The Gantt chart presents you with document separators indicating the precise document start and document end.

Document separators are shown as square brackets (“[]”) with the left square bracket (“[”) representing the document

start and the right square bracket (“]”) representing the document end.

You can choose to display or hide document separators in the Gantt chart by selecting the corresponding checkbox in the

legend area.

Document separators apply to the following types of resources:

truck

trailer

driver

locomotive

railcar

container

For more detailed information on how to enable document separators, see SAP Note 2502946

## Option to display or hide time windows in the Gantt chart

The Gantt chart presents you with time windows indicating when goods are to be picked up and delivered. In the Gantt

chart, time windows are shown as dotted lines and solid lines. You can choose to display the time windows by using the

corresponding checkboxes in the legend area.

For more detailed information on how to enable document separators, see SAP Note 2502910

## Option to display and solve warnings in the Gantt chart

The Gantt chart presents you with warnings such as the Missing Stage warning or the Incorrect Driver Assignment

warning that are indicated by a warning icon. You can solve a warning using the context menu. You can choose to display or

hide this type of warning in the Gantt chart by selecting the respective checkboxes in the legend. The legend area also

displays the number of warnings for each warning type. Moreover, the number is dynamically updated once a warning of a

certain type is solved or generated. Besides of the legend area, the Number of Warnings column in the table area presents

you the total number of warnings on each row in a real-time manner. You can also deselect a certain warning type in the

legend area so that warnings of that type are not considered when calculating the total number.

Insights into planning and execution status of documents and transportation activities

If you transfer event-related data from Event Management to Transportation Management, you can gain real-time insights

into the planning status and execution status of the documents and transportation activities in the chart panel. The

statuses of documents and activities are presented in predefined colors and patterns, as described in the legend. Note that

the Gantt chart automatically hides a legend item in the legend area if no corresponding documents or activities are shown

in the chart area.

This is custom documentation. For more information, please visit SAP Help Portal.

141


1/14/26, 2:19 PM

## Flexible and dynamic switch between different views

You can switch between a single view and a dual view (with its horizontal and vertical versions). In the chart panel of each

view, you have the option to switch between a document view and an activity view. The dropdown lists and the related

pushbuttons in the toolbar enable you to switch dynamically between views and hierarchies that are pre-defined in

Customizing. For example, in a horizontal dual view, you can choose to display freight orders in the upper view and trucks in

the lower view, so that you can assign unplanned freight orders to trucks using drag and drop.

## View all objects with one click

Bird Eye provides you with the capability to have a panoramic view of all objects with one simple click. With this feature

turned on, the system intelligently adjusts the zoom rate so that all items are displayed on the chart without a need to move

the horizontal scroll bar.

This feature can be implemented on all rows or just on visible rows, which can be configured in Gantt Chart Customizing.

For more information, see SAP Note 2671506

You can also use the Bird Eye feature on a specific row using the Bird Eye on Row context menu. In this case, the zoom level

will be adjusted to fit all objects on that row.

## Personalize table area appearance

You can personalize the appearance of the table area with the following options:

Display or hide a column

Modify the column sequence

## Adjust the column width

Moreover, you can save all personalization settings as a variant so that the table area is presented with the saved settings

for the next time you load the Gantt chart.

## Configurable visualization of notifications

You can define the color and height of a certain type of notifications in the Gantt chart. Moreover, you can configure when to

display the following types of notifications by specifying a utilization range value of vehicle resources:

## Empty run

Low utilization

## Overcapacity

Interactive planning in the Gantt chart

## Drag and drop

You can use drag and drop to perform planning in the Gantt chart. For example, you can assign documents to

resources, change the location sequence of a document, and perform reassignments by using drag and drop in the

chart panel.

To use resources more efficiently, you can simultaneously drag multiple capacity documents and then drop them to

another one. For example, if you drag two freight orders and drop them to another one, the freight units previously

assigned to the orders being dragged will be assigned to the order where you drop them. Additionally, you can

perform cross-type drag and drop. For example, you can drag two ocean freight bookings and drop them to an air

freight booking if needed.

You can perform drag and drop operations in the following modes:

Assign and schedule based on drop time (default)

This is custom documentation. For more information, please visit SAP Help Portal.

142


1/14/26, 2:19 PM

In this mode, the start time and end time of the object you drag and drop is determined by the position

where you drop it. If you drag a document and drop it very close to another one, the system will automatically

move the document you dropped right after or right before the other document.

## Assign and schedule based on original time

In this mode, you explicitly keep the original start time and end time of a freight unit or freight order when

you drag and drop it to a resource. This mode makes sure that the schedule of the object you drag and drop

remains intact while the default mode may cause a discrepancy in the timeline even if you try to avoid it.

This mode is typically used in a scenario where you want to assign a scheduled order to a vehicle resource,

such as a driver or a truck. In this scenario, you usually want to keep the schedule of the order.

For more information on drag and drop options, see Activities.

## Attribute-based planning

In attribute-based planning, loading and unloading activities are color-coded to differentiate one freight unit from

another. For example, the loading activities for freight units carrying chemical products and those for freight units

carrying foods are in different colors. This helps you efficiently group or split freight units based on their visual

appearances and thus generate optimized transportation plans from a holistic view.

For more information about how to enable attribute-based planning, see SAP Note 2671540

.

## Hyperlink and context menu

In the selection panel, the hyperlink allows you to navigate directly to the detailed screen of the selected item. In the

chart panel, you can double-click a document or an activity of a document to go to the detailed screen of the

document. Alternatively, you can use the Show Document or Show Resource context menu in the chart panel to

display the details of a document or a resource. The context menu in the chart panel offers you options that provide

easy navigation in a row, such as Jump to First and Jump to Last. There are also context menus that allow you to

remove an assignment, split or merge freight unit stages, insert or remove a location, assign or unassign a driver,

and solve warnings. Moreover, you can use the Assign Schedule context menu to plan a freight unit or a container

unit. This feature enables you to assign a freight unit or container unit to a scheduled flight, voyage, road trip, or rail

trip that you have found by search. This feature also plans loading and unloading activities for the freight unit or

container unit. For example, in air freight bookings and ocean freight bookings, the loading time and the unloading

time are set to the cutoff time and the available time in the schedule.

## Quick view

Gantt Chart presents a quick view page for both objects in the table area and in the chart area if you hover the

mouse over an object for about one second or more. The quick view page displays basic information on the object.

Take the railcar unit as an example - the quick view page displays the following information:

Source Location

Destination Location

Departure Date

Arrival Date

Resource Capacity

Remaining Capacity

## Equipment Type

Hyperlinks on the quick view page enable you to perform various operations depending on its type. For example:

You can click the Location hyperlink to navigate to the details page of a location.

This is custom documentation. For more information, please visit SAP Help Portal.

143


1/14/26, 2:19 PM

You can click the Show on Map hyperlink to display the object on the Map.

You can also click the Email hyperlink to launch an email program.

For more information about how to configure quick view, see SAP Note 2671529

.

## Selection of items in the Gantt chart

In the chart panel, you can select two or more items using the  CTRL  key. You can also select all items in a row by

choosing the Select All context menu. If you select one document or activity that appears more than once in

multiple rows of the Gantt chart, the system automatically selects the same document or activity in all rows. In a

dual view, selection in one view does not influence selection in the other view, and you can select items in both views

at the same time.

## Editable fields for capacity documents

You can edit certain fields for a capacity document directly in the table area of a Gantt chart without needing to

open the capacity document. Further , depending on how you update the field, the Gantt chart dynamically updates

the corresponding row in the chart area to reflect the change. For certain fields, you can also specify their value

using search results.

The following table lists the fields that can be edited directly in Gantt charts.

Capacity Document

Editable Field

Road freight order

Departure date

Freight booking

Departure time

Arrival date

Arrival time

## Carrier

Means of Transport

## Vehicle

Departure date

Departure time

## Carrier

## Means of Transport

Airline code (air booking only)

Flight number (air booking only)

Voyage ID (ocean booking only)

Train number (rail freight booking only)

Vessel (ocean booking only)

Availability date

Availability time

## Cargo Cut off date

This is custom documentation. For more information, please visit SAP Help Portal.

144


1/14/26, 2:19 PM

Capacity Document

## Editable Field

Trailer Unit / Container Unit / Railcar Unit Departure date

Cargo Cut off time

Departure time

## Carrier

Trailer/Railcar/Container

Train number (railcar unit only)

Equipment Type (container unit only)

Equipment Group (container unit only)

## Means of Transport

For more detailed information on how to enable editable fields for capacity documents, see SAP Note 2502783

## Integration with the transportation cockpit

The Gantt chart, integrated into the transportation cockpit, interacts well with other existing functions. For example, you

can select one or more freight units in the freight unit list, and a resource in the Gantt chart, and then choose Plan Selected

Items to assign the selected freight units to the resource. You can also update maps, generate transportation proposals,

and run optimizer planning for the selected items in the Gantt chart and in the lists and hierarchies of the transportation

cockpit.

If you enable the Smart Add function, any capacity documents or requirement documents that have been selected in other

UIBBs, for example the freight units list, in the Transportation Cockpit are automatically visualized in the Gantt chart.

Furthermore, the Gantt chart also displays the objects related to those selected documents. For example, if a freight unit is

selected in the freight units list, in addition to the freight unit itself, the Gantt chart also displays the freight order related to

the freight unit and the vehicle resource assigned to the freight order. If the vehicle resource has other freight orders

assigned, those freight orders are also displayed. This function also works in a multi-window environment.

  Note

If you enable the Smart Add function, the Gantt chart does not show any shapes until you select one or more

items in other UIBBs. This makes it very likely that the Gantt chart shows nothing when the cockpit is initially

loaded as no items are selected in any UIBBs at that time.

If you enable the Smart Add function, you can specify the selection behavior:

Selection on the Gantt chart overrules the selection on the transportation cockpit by document or

resource type only.

Selection on the Gantt chart overrules the selection on the transportation cockpit completely.

For more information about the Smart Add function, see SAP Note 2671518

.

## Configurable visual appearance and layout

You can define color schemes and patterns, field lists, hierarchies, views, and layouts for the Gantt chart. For more

information, see Customizing for Transportation Management under  Basic Functions

 Gantt Chart

.

## Activities

This is custom documentation. For more information, please visit SAP Help Portal.

145


1/14/26, 2:19 PM

You can perform the following planning operations in the activity view of the chart panel in the Gantt chart using drag and drop:

You can assign an unplanned trailer unit stage to a road freight order by dragging the travel activity of the unplanned trailer

unit stage and dropping it on the travel activity of the road freight order.

You can change the location sequence including source or destination location of a document by dragging one travel

activity and dropping it on another travel activity. Alternatively, you can change the location sequence of a document by

dragging a loading or unloading activity and dropping it on a travel activity.

You can reschedule a document by dragging any activity of the document and dropping it on the desired time in the chart

panel.

You can couple a truck and a trailer by dragging the travel activity of the trailer unit and dropping it on the travel activity of

the road freight order.

In a multi-pick scenario, you can change the sequence of loading locations in a document by dragging the loading activity at

one location and dropping it on a travel activity.

In a multi-drop scenario, you can change the sequence of unloading locations in a document by dragging the unloading

activity at one location and dropping it on a travel activity.

You can reassign freight units from one road freight order to another by dragging the loading or unloading activity of one

road freight order and dropping it on a travel activity, loading activity, or unloading activity of another freight order.

  Note

By dragging the loading or unloading activity of one road freight order, you remove all the loaded or unloaded freight

units.

You can move a location from one road freight order to another, including any freight units that are planned to be

transported from or to this location. You do this by dragging the loading or unloading activity of one road freight order and

dropping it on a travel activity, loading activity, or unloading activity of another freight order. The location and the freight

units are then deleted from the original road freight order.

You can reassign the resource of one or more documents by dragging one travel activity of the document and dropping it

on the chart panel of another resource.

  Note

In this case, you can drop the travel activity on the chart panel of a resource in the document view.

You can create a trailer unit and couple it to an existing road freight order by dragging a travel activity of the road freight

order and dropping it on the chart panel of the trailer.

  Note

In this case, you can drop the travel activity on the chart panel of a resource in the document view.

You can create a trailer unit and assign a freight unit by dragging a travel activity of the freight unit and dropping it on the

chart panel of the trailer.

You can create a freight order and assign a freight unit by dragging a travel activity of the freight unit and dropping it on the

chart panel of the truck.

You can reassign one or more freight units by dragging the travel activities of the freight units and dropping them on the

chart panel of another document.

You can assign one or more transportation stages of a road freight order to a driver by dragging the travel activity of the

transportation stages and dropping them on the chart panel of a driver.

This is custom documentation. For more information, please visit SAP Help Portal.

146


1/14/26, 2:19 PM

  Note

This function is only available for drivers who are to be assigned to road freight orders per transportation stage.

You can perform the following planning operations in the document view of the chart panel in the Gantt chart using drag and drop:

You can assign an unplanned trailer unit stage to a road freight order by dragging the unplanned trailer unit stage and

dropping it on the road freight order.

You can reschedule a document by dragging that document and dropping it on the desired time in the chart panel.

You can reassign the resource of one or more documents by dragging a document and dropping it on the chart panel of

another resource.

You can reschedule a document by dragging it and dropping it on another position in the chart panel of the same resource

or driver.

You can create a trailer unit and couple it to an existing road freight order by dragging a road freight order and dropping it

on a trailer.

You can create a trailer unit and assign a freight unit by dragging a freight unit and dropping it on the chart panel of the

trailer.

You can create a freight order and assign a freight unit by dragging a freight unit and dropping it on the chart panel of the

truck.

You can reassign one or more freight units by dragging the freight units and dropping them on the chart panel of another

document.

You can reassign the driver of one or more road freight orders by dragging the freight orders and dropping them on the

chart panel of the new driver to be assigned to these freight orders.

  Note

This function is only available for single drivers who are assigned to entire freight orders.

You can create a road freight order with a driver already assigned to it by dragging freight units or trailer units and dropping

them on the chart panel of the driver.

  Note

This function is only available for drivers who are assigned to a particular truck by default.

Additionally, in the context menu, you can insert locations to and remove locations from trailer units, freight orders, and freight

units. You can also use default routes for the transport of trailer units and freight units. For more information on default routes, see

Use of Default Routes in VSR Optimization.

## More Information

Overview of the Gantt Chart Functions

Overview of the Gantt Chart Functions

## Use

The Gantt chart screen provides different functions that allow you to work effectively.

This is custom documentation. For more information, please visit SAP Help Portal.

147


1/14/26, 2:19 PM
## Features

The following table lists and explains some of the available functions:

Icon on the User Interface

Function

Description

n/a

## Display Single View

A view that comprises the following elements:

Selection panel that refers to the left pane

of the Gantt chart and is constructed as a

hierarchy

Chart panel that shows the planning status

over time for each item on the left

Time axis above the chart panel

n/a

## Display Multiple Views

A view that consists of multiple single views that are

aligned either vertically or horizontally. You can

choose to display different items in the views, for

example, freight orders in the first view and trucks

in the second view. You can drag and drop items in

the chart panel of one view to the chart panel of

another view.

You can switch between display of single view and

multiple views using the Add Gantt Chart and

Remove Gantt Chart functions.

n/a

## Synchronize Scrollbars

If you have multiple views displayed, you can

choose whether the displayed views are scrolled

simultaneously when you move the horizontal

scrollbar of either of the views or not. This function

enables you to display the same time frame of the

views when moving the scrollbar of either of them

or to display different time frames in different views.

## Document View

The chart panel displays documents such as freight

orders and trailer units. You can switch to an activity

view at any time.

## Activity View

The chart panel displays transportation activities

such as loading, coupling, and traveling. You can

switch to a document view at any time.

## Rescheduling Mode

In the rescheduling mode, you can drag one activity

and drop it to another position in the same row. The

system reschedules the document by scheduling

the dragged activity to the desired time, without

changing the stop sequence of the document.

## Resequencing Mode

In the resequencing mode, you can drag one activity

and drop it to another activity in the same row. The

system changes the stop sequence of the

document.

## Settings

You can switch on and off specific functions for your

current session, for example, Display Current Time,

Display Cursor Time, Show Planning Horizon

Boundaries.

This is custom documentation. For more information, please visit SAP Help Portal.

148


1/14/26, 2:19 PM

Icon on the User Interface

Function

## Legend

## Description

The legend shows the color schemes and patterns

for the documents, transportation activities,

planning and execution statuses, notifications,

nonavailable times, vehicle load utilization, handling

resource utilization, and warnings.

Also, you can choose to display or hide the following

types of legend items:

Notifications

## Warnings

Document separators

Time windows

n/a

n/a

Zoom In

This function enables you to gain a closer view of

the items in the chart panel across shorter time

intervals.

Zoom Out

This function enables you to gain a broader view of

the items in the chart panel across longer time

intervals.

## Bird Eye

You can use this pushbutton to make the system

intelligently adjust the zoom rate so that all items

are displayed on the chart without a need to move

the horizontal scroll bar.

## Sort Sequence

In the selection panel, you can sort the sequence of

entries in the table/hierarchy by one individual

column (ascending or descending) for each view.

## Filter

You use this function to find entries that meet

certain filter conditions. You can apply one or more

filter conditions to a list in the Gantt chart. If a list

consists of two or more levels, you can only filter at

the root level. For example, the system displays a

“truck with driver” list. The truck is the root level of

the list. The drivers that are assigned to the truck

are a sub level. You can only filter the list by truck.

To delete your filter, choose the Filter pushbutton.

In the Change Filter dialog box, choose Delete

Filter.

Note that you can filter by the following date

formats:

DD.MM.YYYY

MM/DD/YYYY

MM-DD-YYYY

YYYY.MM.DD

YYYY/MM/DD

## YYYY-MM-DD

This is custom documentation. For more information, please visit SAP Help Portal.

149


1/14/26, 2:19 PM

Icon on the User Interface

Function

## Description

You can also filter by the 24-hour time format

“HH:MM:SS” (for example 14:05:10).

We recommend you enter the date and time in the

filter in the same format that you use in the date

and time column of the selection panel in the Gantt

chart. When you enter both a date and a time, you

must leave a space between the date and the time.

## Show Utilization

The system displays the utilization curve of the

selected vehicle resource in the chart panel. The

tooltip along the utilization curve shows the

percentages of consumed weight, volume,

alternative quantity, or normalized quantity,

depending on your settings in Customizing. You are

notified of low load utilization and over-capacity by

pre-defined colors, as shown in the legend.

## Hide Utilization

The system hides the utilization curve of a vehicle

resource.

## Show Details

You can use this pushbutton to display the

documents or transportation activities of a vehicle

resource that overlap at a particular period of time.

You are notified of an overlap by a pre-defined color,

as shown in the legend. Alternatively, you can

double-click the overlap bar to display overlap

details.

For handling resources, you can use this

pushbutton to display the loading and unloading

activities that are planned for a handling resource

at different times.

## Hide Details

You can use this pushbutton to hide the documents

or transportation activities that overlap for a vehicle

resource. You can only see the overlap notification

in a pre-defined color. Alternatively, you can double-

click the overlap bar to hide overlap details.

You can also use this pushbutton to hide loading

and unloading activities that are planned for a

handling resource at different times.

## Fix

This pushbutton fixes the documents and

transportation activities to prevent them from

being changed by automatic and manual planning.

## Unfix

This pushbutton removes the fixed status of the

documents and transportation activities.

## Scheduling

Scheduling determines start and end times for

transportation activities, considering multiple

constraints such as time windows for the activities.

Scheduling is triggered for freight orders and is

based on your settings in the planning profile. If you

run scheduling for a resource, all freight orders

assigned to this resource are scheduled. For more

information, see Scheduling.

n/a

n/a

n/a

This is custom documentation. For more information, please visit SAP Help Portal.

150


1/14/26, 2:19 PM

Icon on the User Interface

Function

## Cancel

## Description

This pushbutton deletes freight orders and trailer

units. It also removes assignment of freight units,

stops, and trailer units from documents. You can

delete a freight order or a trailer unit either by

deleting the whole document or by deleting all of its

travel activities. You can unassign a freight unit from

a document by deleting the freight unit's load,

unload, or travel activity. You can unassign a trailer

unit from a freight order by deleting the coupling or

uncoupling activity. If you delete a travel activity

from a freight order or a trailer unit, all loaded and

unloaded freight units are removed from both stops

of this stage. The stops are also removed from the

freight order or the trailer unit. Note that if you

delete the travel activity of the first stage, only the

first stop is removed; if you delete the travel activity

of the last stage, only the last stop is removed. If

you remove load or unload activity from a freight

order or a trailer unit, you unassign freight units

from a stop, but the stop is not removed.

## Create Road Freight Order

You use this pushbutton to create a new road

freight order from scratch. If you select a truck and

use this pushbutton, the system creates a new road

freight order and assigns the truck to the new road

freight order.

## Create Trailer Unit

You use this pushbutton to create a new trailer unit

from scratch. If you select a trailer and use this

pushbutton, the system creates a new trailer unit

and assigns the trailer to the new trailer unit.

## Create Freight Unit

You use this pushbutton to create a new road

freight order for an unplanned freight unit stage.

## Create Air Booking

You use this pushbutton to create an air freight

booking from scratch. You can then plan the loading

and unloading activities for the air freight booking.

To do this, save the newly created freight booking,

click the corresponding hyperlink in the selection

panel to navigate to the detailed screen, and then

edit the loading and unloading activities in the

Locations section. Alternatively, you can assign the

air freight booking to a scheduled flight. The system

then plans the loading and unloading activities

automatically according to the data specified in the

schedule.

## Create Ocean Booking

You use this pushbutton to create an ocean freight

booking from scratch. You can then plan the loading

and unloading activities for the ocean freight

booking. To do this, save the newly created ocean

freight booking, click the corresponding hyperlink in

the selection panel to navigate to the detailed

screen, and then edit the loading and unloading

activities in the Locations section. Alternatively, you

can assign the ocean freight booking to a scheduled

This is custom documentation. For more information, please visit SAP Help Portal.

151


1/14/26, 2:19 PM

Icon on the User Interface

Function

## Description

voyage. The system then plans the loading and

unloading activities automatically according to the

data specified in the schedule.

## Copy

You use this pushbutton to copy one ore more

objects, such as a road freight order and a trailer

unit.

## Display Planning Horizon

You can display vertical lines in the chart panel that

## Boundaries

indicate the start and end date and time of your

planning horizon.

## Display Current Time

You can display a vertical line in the chart panel that

indicates the current time.

## Display Cursor Time

You can display the time to which the cursor points

in the chart panel. The time is indicated by a vertical

line that moves with the cursor.

## Resize Panels

You can adjust the size of the selection panel and

the chart panel by moving the divider between them

for each view.

## Resize Views

You can resize the views by moving the divider

between them.

n/a

n/a

n/a

n/a

n/a

## More Information

Gantt Chart for Transportation Planning

Freight Document Overview

## Use

You can use this function to display a location-based view of your resources and requirements (for example, freight units,

transportation units (passive vehicle resource), and compartments):

## All transportation stops of a freight unit as well as their sequence

All activities performed at these transportation stops, for example, loading and unloading of freight units and containers or

coupling and uncoupling of railcars and trailers

Information, for example, the start of the loading and unloading, as well as of the transport

In addition, you can use various editing options.

## Features

You have the following editing options:

Change the sequence of the transportation stops (not possible for freight orders that are based on a schedule)

Add transportation stops (not possible for freight orders that are based on a schedule)

This is custom documentation. For more information, please visit SAP Help Portal.

152


1/14/26, 2:19 PM

Delete transportation stops (not possible for freight orders that are based on a schedule)

## Add freight units (that is, stages) to a freight order

Delete freight units and transportation units (that is, stages) from a freight order

Move freight units and container units from one compartment to another (within a freight order)

Change assignment of freight units and transportation units to transportation stops

For all of these options, the system performs a series of checks. This allows the system to check, for example, dependencies

between freight units as well as incompatibilities (see Incompatibilities).

## Activities

The freight document overview is available on the user interfaces for the freight order and the freight booking as well as in the

transportation cockpit. To display the freight document overview in the transportation cockpit, open the Transportation Cockpit

app on the launchpad. Note that the freight document overview is only displayed for one freight order.

Generation of Transportation Proposals

## Use

The VSR optimizer (see VSR Optimization) uses this function to generate alternative transportation proposals for the selected

freight unit of which you can then use one. Unlike in the case of an optimization run, here the VSR optimizer searches for

alternative transportation proposals.

## Prerequisites

You have defined optimizer settings and have assigned them to your planning profile (see Planning Profile). For example,

you have made the settings for generating transportation proposals and have specified which planning strategy you want

to use. If you want to specify your transportation proposal preferences in more detail, you have selected the Do Not Create

Transp. Prop. Immediately checkbox. You do this by opening the Create Transportation Cockpit Settings app on the

launchpad.

  Note

You can use the settings from your planning profile and adjust them for each transportation proposal generation. To do

this, select the Change Proposal Settings checkbox.

If you want to personalize the page layout to display transportation proposals, open the Define Page Layouts for

Transportation Proposal app on the launchpad.

You can then include the personalized page layout in the page layouts of the transportation cockpit.

  Note

If you want to specify and change specific transportation proposal preferences for planning a freight unit in the

transportation cockpit, you have selected the Calculate and Reset Preferences checkboxes in the page layouts for the

transportation proposals. You previously made the Transportation Proposal Preferences screen area visible in your

page layouts.

## Features

This is custom documentation. For more information, please visit SAP Help Portal.

153


1/14/26, 2:19 PM

A transportation proposal contains the following information:

Route (sequence of locations of a freight unit)

## Freight order

## Assignment of freight unit to freight order

When it generates transportation proposals, the system considers the selected freight unit as well as indirectly linked freight

orders, transportation units, and freight units (see Context Determination). The system does not change these indirectly linked

freight orders and freight units. However, it does consider them as a constraint for the selected freight unit, which means that they

can result in restrictions for the selected freight unit. For example, no vehicle resources are available for the selected freight unit if

they are used by indirectly linked freight units.

The system generates transportation proposals only for the unplanned transportation stages of a freight unit that you have

selected in the transportation cockpit. In doing so, the system generates either new freight orders or, if you have selected existing

freight orders in the transportation cockpit, it upsizes these existing freight orders for the transportation proposal and adjusts

them to the times specified in the transportation proposal.

In the case of the transportation stages of a freight unit that have already been planned, the system only generates transportation

proposals if these transportation stages are not fixed.

  Note

Planned transportation stages that the system determines using context determination are always fixed in the VSR

optimizer.

The generation of transportation proposals for multiple transportation stages is only supported if these transportation

stages belong either to the same requirement document or to multiple requirement documents that were created

during freight unit building for the same preceding document.

SAP delivers the standard planning strategies VSR_DEF and VSR_1STEP for generating transportation proposals. You use the

standard planning strategy VSR_1STEP to specify that carrier selection is to be performed directly after transportation proposals

have been generated. For more information, see One-Step Planning and Planning Strategies.

When transportation proposals are generated, a dangerous goods check is performed if you have activated it. For more

information, see Considering Dangerous Goods.

You can use the route planner to display the connections between the locations in the transportation proposal on a geographical

map. For more information, see Path Finder.

To plan a freight unit with one or more freight unit stages in the transportation cockpit, you can specify in detail your preferences

for the transportation proposal in question. For more information, see Planning Profile.

If you want the system to generate transportation proposals for a package unit, container unit, or railcar unit to which freight units

are assigned, the VSR optimizer only takes the package unit, container unit, or railcar unit into account. However, if you have not

defined time windows for the package unit, container unit, or railcar unit, the VSR optimizer takes the time windows of the

assigned freight units into account.

## Activities

You can generate transportation proposals as follows:

## From interactive planning

This is custom documentation. For more information, please visit SAP Help Portal.

154


1/14/26, 2:19 PM

From the user interface for creating forwarding orders

From the user interface for creating forwarding quotations

Command Line Planning

## Use

Within the transportation cockpit, you can carry out various planning operations without having to use the mouse.

## Prerequisites

In the page layouts for the transportation cockpit, you have activated the command line. You do this by opening the Define Page

Layouts for Transportation Cockpit app on the launchpad.

## Features

You define the commands for carrying out the required planning operations according to the following rule:

<Input Element ID> – <Target Element ID>

The element ID is defined in the Index column, which is available for all tables in the transportation cockpit. The element ID is a

number that is unique for every element on the user interface. An element ID that is used for a freight unit, for example, is not also

used for the resource. This means that the element ID identifies the source and the target uniquely.

To decrease the time required for entry, you can combine multiple commands into a single entry. To combine multiple commands,

you enter them in the command line and separate each command with a plus (+). These commands are then processed

sequentially after you press ENTER.

## Activities

Enter the required command in the command line.

## Example

## Example 1: Simple Planning of Freight Units on a Vehicle Resource

The freight units to be planned have the indexes 5, 6, and 7. The vehicle resource that you want to use to transport the freight units

has the index 2. To assign the freight units to the vehicle resource, you enter the following command in the command line:

5 6 7 – 2

For more examples, see the system documentation.

## Conversational Planning

Within the transportation cockpit, you can carry out various planning operations using natural language.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

155


1/14/26, 2:19 PM

Use of this AI-assisted feature may require additional entitlement and authorization. Please consult your account

executive for more information.

The features described here are only available in SAP S/4HANA Cloud Private Edition.

## Prerequisites

You have configured the settings related to Intelligent Scenario Lifecycle Management (ISLM) that are required to use

generative AI in Transportation Management (TM).

First, you have requested an SAP Business Technology Platform (SAP BTP) service key for the intelligent scenario

GENAI_TM_COPL_GPT40. Make sure you have noted down the name of the intelligent scenario, as you will need it later in

the setup process. For more information, see Requesting Access to SAP AI Services on SAP Business Technology Platform

(SAP BTP). Then you have performed the subsequent steps. For more information, see Customizing for Transportation

Management under  Basic Functions

 Generative Artificial Intelligence .

For more information about ISLM setup, see SAP Delivered Generative AI Scenarios.

You have defined a generative AI profile of type Conversational Planning (conversational planning profile). In this profile,

you have indicated one or several capabilities, that is, planning operations, that you would like to perform in the

transportation cockpit using generative AI.

For more information, see Customizing for Transportation Management under  Basic Functions

 Generative Artificial

## Intelligence

 Define Generative AI Profile .

You have assigned your conversational planning profile to your page layout. By doing so, a new area will be available at the

top of the transportation cockpit including an input field that allows you to enter your prompts. To assign the profile to the

page layout, open the Define Page Layouts for Transportation Cockpit app from the launchpad.

If you want to enrich certain lists and hierarchies of the transportation cockpit with information provided by generative AI,

you need to indicate in the corresponding field catalogs whether the field Conversational Planning Response is to be

displayed by default or using personalization.

For more information, see Field Configuration for the Transportation Cockpit.

For more information about setting up conversational planning, see SAP Note 3573759

 (AI use case Conversational Planning in

S/4HANA Cloud Private Edition).

## Features

A new screen area at the top of the transportation cockpit allows you to enter your prompts. You can do the following:

You can select one or several of the following objects using natural language:

Freight unit stage

Freight order

Truck type

Truck resource

  Example

## Select all freight orders going to Spain

This is custom documentation. For more information, please visit SAP Help Portal.

156


1/14/26, 2:19 PM

Select the truck with the highest weight capacity

You can perform the following planning operations using natural language:

Assign freight units to freight orders

Assign freight units to trucks

Assign trucks to freight orders

  Example

Assign all freight units from New York to the small truck

Assign all freight unit stages from Paris to freight order 123

You can fill an extra column Conversational Planning Response in some lists and hierarchies with additional information

generated by generative AI. The benefit of this extra column consists in providing information, which is not visible otherwise

saving you from the time-consuming task of manually checking all objects for the required information.

The following lists and hierarchies are supported:

Road freight order list and hierarchy

Freight unit stage list and hierarchy

Truck resource list

  Example

Which freight units contain milk?

Which freight units go to Bavaria?

Several Business Add-Ins (BAdIs) are available to enhance this function according to your needs. For example, you can use these

BAdIs to adjust data, such as model parameters, associated with your ISLM scenario or data that is associated with the generative

AI calls, such as messages and responses. Or you can enhance the context that is taken into account for a given capability for

example by adding additional object information. For more information, see Customizing for Transportation Management under:

Business Add-Ins (BAdIs) for Transportation Management

## Basic Functions

## Generative Artificial Intelligence

Business Add-Ins (BAdIs) for Transportation Management

## Planning

 Conversational Planning

## Activities

Enter your prompt in the input field and select Submit. The system performs the requested capability and displays the result in the

corresponding lists and hierarchies.

  Note

The system only considers selected entries as context.

The system considers entries in the order that is given by the object index.

This is custom documentation. For more information, please visit SAP Help Portal.

157


1/14/26, 2:19 PM

## Additional Information

This chapter contains additional information that is relevant for using conversational planning, such as supported context

information.

The following context information can be made available to the large language model (LLM):

Supported Context Information

Freight Unit Stage

Road Freight Order

Truck Resource/Truck Type

## Index

Selected

## Index

Selected

## Index

## Selected

Destination City

Destination City

Registration Number *

Destination Country

Destination Country

Temperature Control

Destination Location

Destination Location

Home Location *

Source City

Source City

Weight Capacity

Source Country

Source Country

Volume Capacity

Source Location

Source Location

Quantity Capacity

Weight

Products

Status

Weight

## Status

Weight Capacity

Equipment Group

Volume Capacity

Equipment Type

Earliest Pick-Up Date

Quantity Capacity

Latest Pick-Up Date

Location Sequence

Earliest Delivery Date

Registration Number

Latest Delivery Date

Products

-

-

-

## Status

Departure Date

Arrival Date

-

-

-

-

-

-

-

*= only supported for truck resources

## Automatic Planning

Automatic planning offers the following functions:

Vehicle scheduling and routing (VSR) optimization

For more information, see VSR Optimization.

## Load consolidation

For more information, see Load Consolidation.

This is custom documentation. For more information, please visit SAP Help Portal.

158


1/14/26, 2:19 PM

## Load planning

For more information, see Load Planning.

VSR Optimization

## Use

The aim of VSR optimization (VSR = vehicle scheduling and routing) is to assign freight units to capacities (for example, vehicle

resources) in a cost-effective way while adhering to constraints (see Constraints for VSR Optimization), and to determine the

sequence of deliveries and transportation dates/times.

## Prerequisites

You have defined the master data for VSR optimization, for example, the network connections to the optimization server

and the maximum number of users. You do this on the SAP Easy Access screen under  Cross-Application Components

 Remote Control and Communication Framework

  Administration

## Settings

 Edit Destinations .

You have created a planning profile (see Planning Profile) and have assigned the following settings to it:

## Optimizer settings

For example, you have specified the planning strategy (see Planning Strategies) that you want to use. Open the

Create Optimizer Settings app on the launchpad.

## Constraints and costs settings

To do this, open the Create Constraints and Costs Settings app on the launchpad.

## Capacity selection settings

Open the Create Capacity Selection Settings app on the launchpad.

You can also assign a selection profile for freight orders and freight bookings as well as incompatibility settings. If you want

to perform one-step planning, you must also assign carrier selection settings (see One-Step Planning).

You have defined transportation lanes. Open the Define Transportation Lane app on the launchpad.

In the case of multimodal transportations or transshipments, you have defined transshipment locations (see

Transshipment Location) or default routes (see Use of Default Routes in VSR Optimization). Open the Assign

Transshipment Location or the Create Default Route app on the launchpad.

If you want to control the input or the results of the VSR optimization, you have made the settings for the Business Add-Ins

(BAdIs) BAdI: VSR Optimizer Preprocessing and BAdI: VSR Optimizer Postprocessing.

For more information, see Customizing for Transportation Management under  Transportation Management

## Business

Add-Ins (BAdIs) for Transportation Management

## Planning

## VSR Optimizer

 VSR Optimizer Preprocessing and

Postprocessing .

## Features

VSR optimization generates a transportation plan consisting of planned freight orders from the optimization data (freight units

and capacities, see Optimization Data). When doing this, it processes freight orders already available from a previous VSR

optimization run or manual planning. VSR optimization inserts the freight units step-by-step into the transportation plan. Then

VSR optimization modifies these initial solutions step-by-step, for example, by loading a freight unit on to another capacity or by

changing the delivery sequence of a capacity. When doing this, the optimizer tries to minimize the total costs (see Total Costs)

This is custom documentation. For more information, please visit SAP Help Portal.

159


1/14/26, 2:19 PM

while adhering to the constraints. At the end of the planning run, VSR optimization returns the best solution found. For example, if

the costs defined for non-delivery of a freight unit are lower than the costs for transporting the freight unit, the freight unit is not

delivered.

  Recommendation

To achieve the best possible planning result, we recommend that you find a happy medium between creating extremely large

freight units and extremely small ones. The larger the freight units are, the simpler the planning activities in VSR optimization. If

the freight units are smaller, there may well be a higher theoretical potential for optimization, but in practice, planning in VSR

optimization is made more difficult due to the higher number of freight units.

  Example

You have a truck with a capacity of 20 tons. You are planning to transport 20 tons of flour in 1 kg packages. Neither extreme is

advisable here for the reasons given above. You should not create a single freight unit with a weight or 20 tons, nor should you

create 20,000 freight units with a weight of 1 kg each.

Furthermore, you can generate multiple alternative transportation proposals, in other words, transportation plans, for each freight

unit and can then choose to use one of them. For more information, see Generation of Transportation Proposals.

SAP delivers the planning strategies VSR_DEF and VSR_1STEP as standard for the optimization. You can use the planning

strategy VSR_1STEP to control whether the system is to perform carrier selection immediately after VSR optimization. For more

information, see One-Step Planning and Planning Strategies.

The results of the VSR optimization run are explained in the explanation tool. For more information, see Explanation Tool.

## Activities

You start VSR optimization in the transportation cockpit with Optimizer Planning. You have the following options:

You can perform VSR optimization for all entries.

You can perform VSR optimization for selected entries only. In this case, if you do not choose any capacities, the system

takes into account all capacities. If the system is to consider freight orders and freight bookings, you must also specify this.

You can perform VSR optimization for selected entries as well as for all resources and equipment types. If the system is to

consider transportation units, freight orders, and freight bookings, you must also specify this.

To perform VSR optimization in the background, call report /SCMTMS/PLN_OPT. Choose a planning profile and a requirements

selection profile (and a freight order selection profile, if required), and execute the report in the background. The system displays

the generated freight orders as the result. For more information, see Planning Run.

To end a VSR optimization run prematurely, on the SAP Easy Access screen choose  Cross-Application Components

## Remote

Control and Communication Framework

## Administration

 Display Active Session . Then choose the pushbutton to stop the

process.

## Related Information

Consideration of Scheduling Constraints

Validity of Objects

## Optimization Data

This is custom documentation. For more information, please visit SAP Help Portal.

160


1/14/26, 2:19 PM
## Definition

Data for which the system optimizes planning during VSR optimization (see VSR Optimization).

## Structure

Optimization data includes the following data:

## All selected freight units

All freight units (planned and unplanned) that lie within the planning horizon

All data that the system determines using context determination

The VSR optimizer does not change this data.

## All capacities that match your settings for capacity selection

In addition, transportation lanes between all the relevant locations of the VSR optimization run (source and destination locations

of the chosen freight units, transshipment locations, and depot locations) are part of the optimization data.

The following example describes the effects of transportation lanes on vehicle resources (that is, vehicle resources for which you

have not selected the Passive checkbox for the relevant means of transport) without a schedule. These restrictions do not apply to

schedule vehicles.

If a vehicle with means of transport 'truck' transports a freight unit from A to B, then you must define a direct transportation lane

from A to B for the defined validity period for the means of transport 'truck'. It is not sufficient to have defined transportation lanes

from A to C and from C to B, for example. The VSR optimizer does not combine these to create the transportation lane A to B.

This is also the case if you want to deliver one freight unit from A to C and one freight unit from A to B. It is also not sufficient in this

case to have defined transportation lanes from A to C and from C to B. The freight unit can only be delivered from A to B if you have

defined a direct transportation lane from A to B.

We also recommend that you define a direct transportation lane between A and B in the following case: You want to deliver a freight

unit from A to B. There is no direct transportation lane defined between A and B but there is a transfer location. The freight unit can

only be delivered if it is transferred at the transshipment location. To avoid unnecessary loading and unloading at a transshipment

location, if a freight unit is shipped in a single vehicle on both transportation stages, we recommend that you define a direct

transportation lane.

Total Costs

## Definition

Costs that the system minimizes during VSR optimization (see VSR Optimization).

## Structure

The total costs comprise the following costs:

Freight unit-dependent costs

Earliness costs

## Lateness costs

This is custom documentation. For more information, please visit SAP Help Portal.

161


1/14/26, 2:19 PM

Costs for non-delivery

Capacity-related costs

## Fixed costs per freight order

Fixed costs per vehicle resource or equipment type

## Load costs

Variable transportation costs per unit for the following dimensions:

## Time

## Distance

## Intermediate stops

Transported quantity per distance

CO  emissions (see Greenhouse Gas Emissions)

2

You define these costs in the constraints and costs settings that you assign to a planning profile (see Planning Profile).

Initial Solution

## Definition

Solution that is generated, evaluated, and then optimized in VSR optimization (see VSR Optimization). There are two types of initial

solution:

The existing transportation plans from a previous VSR optimization run or manual planning form an initial solution.

VSR optimization generates additional initial solutions by distributing freight units to capacities (for example, vehicle

resources) using heuristic criteria.

## Use

VSR optimization can only process, and, where necessary, improve existing transportation plans from a previous VSR optimization

run or manual planning as an initial solution, if they meet the following prerequisites:

They must use connections with transportation lanes.

They must lie in selected capacities.

They must not violate any incompatibilities (unless you have permitted this in the Incompatibilities field in the optimizer

settings).

If they are part of a multimodal transportation, this transportation must be valid for VSR optimization (for example, the

transshipment locations must correspond to the transshipment locations defined in the hierarchy).

If the initial solution is invalid, VSR optimization tries to rebuild it as much as possible.

## Constraints for VSR Optimization

This is custom documentation. For more information, please visit SAP Help Portal.

162


1/14/26, 2:19 PM
## Use

VSR optimization (see VSR Optimization) takes into account constraints when it assigns freight units to capacities. You can

differentiate between hard and soft constraints:

VSR optimization always adheres to hard constraints.

You model soft constraints using penalty costs, for example, lateness costs that are part of the total costs.

## Features

VSR optimization minimizes the total costs in the VSR optimization run while adhering to the hard constraints. By appropriately

weighting the penalty costs in the total costs, you can influence the priority of adhering to the soft constraints. If, for example, you

give a greater weighting to the lateness costs, this might lead to longer distances to fulfill the requested dates/times.

  Example

Hard constraints: Loading capacities of a vehicle resource. VSR optimization can only schedule freight units within the existing

transportation capacities.

Soft constraints: Requested dates/times of freight units. VSR optimization can also schedule a freight unit after the requested

delivery date. In this case, delay costs are incurred.

The following table shows the planning data that VSR optimization considers as constraints:

Planning Data

Constraint

## Remark

Handling resources for loading and

## Hard

unloading as well as operating times

Incompatibilities (see Incompatibilities)

Hard

Pickup

Soft

Pickup

## Hard

In addition to the operating times, VSR

optimization also takes into account

loading capacities for the handling

resources.

N/A

VSR optimization can also schedule the

pickup of the freight unit before or after the

requested pick-up date/time. In this case,

earliness or delay costs are incurred. You

can define tolerances for the premature or

delayed pickup without penalty costs (see

Time Windows).

VSR optimization can only schedule the

pickup for the acceptable pick-up

date/time. You can define tolerances within

which a premature or delayed pickup is

allowed (see Time Windows).

Pickup

## Delivery

## Soft and hard

A combination of the options described

Soft

above

VSR optimization can also schedule the

delivery of the freight unit before or after

the requested delivery date/time. In this

case, earliness or delay costs are incurred.

## You can define tolerances for the premature

This is custom documentation. For more information, please visit SAP Help Portal.

163


1/14/26, 2:19 PM

Planning Data

Constraint

Remark

Delivery

## Hard

or delayed delivery without penalty costs

(see Time Windows).

VSR optimization can only schedule the

delivery for the acceptable delivery

date/time. You can define tolerances within

which a premature or delayed delivery is

allowed (see Time Windows).

## Delivery

## Soft and hard

A combination of the options described

Journey to depot for own means of

## Hard

transport

Loading and unloading durations

## Hard

Driving time and working hours constraints

Hard

above

N/A

In the case of schedule-based freight orders

and freight bookings, the system does not

take into account loading and unloading

durations.

You must specify in your scheduling

settings that the system is to consider

these constraints (see Considering Driving

Time and Working Hours Constraints).

Schedules of means of transport (trains,

Hard

N/A

ships, aircraft, and trucks)

Minimum goods wait time at the

## Hard

transshipment location

Maximum goods wait time at the

## Hard

transshipment location

If there is a freight unit stage before or after

the schedule and if additional cut-off times

have been defined in the schedule or freight

booking, VSR optimization takes these cut-

off times into account instead of the

minimum goods wait time at the

transshipment location.

If there is a freight unit stage before or after

the schedule and if additional cut-off times

have been defined in the schedule or freight

booking, VSR optimization takes these cut-

off times into account instead of the

maximum goods wait time at the

transshipment location.

Distance traveled

## Soft

VSR optimization attempts to minimize the

Distance traveled (for each freight order)

## Hard

distance.

The distance must not be greater than the

value defined in the constraints and costs

settings.

Distance traveled (for each freight order)

## Soft and hard

A combination of the options described

Duration

## Soft

Duration (for each freight order)

Hard

above

VSR optimization attempts to minimize the

duration of the road freight orders.

The duration must not be greater than the

value defined in the constraints and costs

This is custom documentation. For more information, please visit SAP Help Portal.

164


1/14/26, 2:19 PM

Planning Data

Constraint

Remark

settings.

Duration (for each freight order)

## Soft and hard

A combination of the options described

Number of intermediate stops

## Soft

Number of intermediate stops (for each

## Hard

freight order)

above

VSR optimization attempts to minimize the

number of intermediate stops.

The number of intermediate stops must not

be greater than the value defined in the

constraints and costs settings.

Number of intermediate stops (for each

## Soft and hard

A combination of the options described

freight order)

Decreasing capacities (see Capacity

## Hard

Decrease)

Compartment capacities

Capacities of means-of-transport

combinations

ADR limit

Hard

Hard

## Hard

Explanation Tool

## Use

above

N/A

N/A

N/A

The number of ADR points for a resource

must not be exceeded (see ADR 1.1.3.6

Points Check Calculation).

You can obtain a detailed overview of the data that flowed into the VSR optimization run and the results that were output. In this

way, you can quickly and easily recognize how the VSR optimization has optimized the costs.

In the same way, you can obtain a detailed overview of the data that flowed into the load optimization run and the results that were

output. In this way, you can quickly and easily recognize how the load optimization has optimally used the loading space while

taking into account various restrictions such as the maximum axle load.

## Prerequisites

You have set user parameter /SCMTMS/EXP to X to allow for the logging of the optimizer data for optimization runs that

you start interactively.

You have the authorization to work with the explanation tool (authorization object T_EXP_USR).

## Features

The explanation tool for VSR optimization displays the following information:

Input for the VSR optimization run, for example, information about the following objects:

Incoming business documents (freight documents or requirement documents)

## Network

This is custom documentation. For more information, please visit SAP Help Portal.

165


1/14/26, 2:19 PM

## Resources

Results of the VSR optimization run, for example:

Status information about business documents (freight documents or requirement documents, or newly created

business documents)

Analysis data, for example, reasons why business documents could not be delivered

## Solution overview

All planning-relevant costs per transportation plan are listed here. If you created transportation proposals, the costs

for each transportation plan are displayed. You can see a breakdown of the costs.

In addition, you receive information about the utilization of the solution and the freight documents.

From the explanation tool you can, in part, go to the associated business documents directly. You can use the pushbutton for

calling customer functions to call the Business Add-In (BAdI) /SCMTMS/PLN_EXP, to execute your own functions for particular

selected objects.

The explanation tool for load optimization and load consolidation displays the following information:

Input for the load optimization or load consolidation run (incoming business documents and resources)

## Results of the load optimization or load consolidation run

Here, the exact position of each package in the loading space is displayed. In addition, the stack, level, and row of

each package is displayed.

Furthermore, the current weight and the maximum permitted weight of the vehicle are displayed along with the

current and maximum axle load for each axle group.

You can use the pushbutton for calling customer functions to call the Business Add-In (BAdI) /SCMTMS/PLN_EXP, to execute your

own functions for particular selected objects.

## Activities

To call the explanation tool for VSR optimization and load optimization, choose Explanation in the transportation cockpit. To call

the transportation cockpit, open the Transportation Cockpit app on the launchpad.

You can call the application log from the SAP Easy Access screen by choosing  Cross-Application Components

 Processes and

Tools for Enterprise Applications

 Remote Control and Communication Framework

 Log Display .

For more information about the planning run in the background, see Planning Run.

We recommend scheduling the deletion program /SCMTMS/PLN_EXP_DELETE regularly in the background.

Incremental Planning

## Use

You can use this function to plan freight orders and freight bookings in automatic planning incrementally and to assign freight

units to existing freight documents. This function is available for VSR optimization and the transportation proposal.

## Prerequisites

This is custom documentation. For more information, please visit SAP Help Portal.

166


1/14/26, 2:19 PM

In the optimizer settings of your planning profile, you have specified which type of incremental planning you want to use. To do this,

open the Edit Optimizer Settings app on the launchpad.

## Features

You can use incremental planning for the following automatic planning functions:

## Transportation proposal

You use this function to consider existing freight documents in the generation of transportation proposals for new freight

units. The system adds the capacities and locations of the freight units that you want to assign to the existing freight

documents. If the new locations do not fit in the location sequence of the existing freight document or if there is not enough

capacity to assign the new freight units to the existing freight documents, the system creates a new freight document with

the new freight units and a new location sequence.

## VSR optimization

You use this function to specify whether the VSR optimizer can delete existing freight documents or only enhance them.

You have the following options:

## VSR optimization without incremental planning

The VSR optimizer does not plan incrementally. Instead, it deletes existing freight documents and automatically

creates new ones.

## VSR optimization with incremental planning

The VSR optimizer cannot delete existing freight documents. Instead, it adds the capacities and locations of the

freight units that you want to assign to the existing freight documents. If the new locations do not fit in the location

sequence of the existing freight document or if there is not enough capacity to assign the new freight units to the

existing freight documents, the system creates new freight documents.

## Incremental planning without inserting new locations

The system assigns freight units to existing freight documents only if there is enough capacity. Furthermore, the

system assigns freight units to existing freight documents if the locations of the freight units fit into the existing

location sequence. For example, a freight unit from A → C can be added to a freight order from A → B → C but not to

a freight order from A → D or from B → A. You are not permitted to insert new locations into existing freight

documents.

## Incremental planning without new capacity documents

The system assigns freight units to existing capacity documents until the existing capacity has been reached. New

capacity documents are not created. As a result, some freight units may remain unplanned.

## Incremental planning with changes to location sequence

During incremental planning the system adjusts the existing location sequence in the capacity documents. Only the

first and last locations cannot be changed.

For example, you have a location sequence with four locations: location A in the west, location B in the southwest,

location C in the northeast, and location D in the east. If you have planned the location sequence manually the

locations could have the sequence A → C → B → D.

This is custom documentation. For more information, please visit SAP Help Portal.

167


1/14/26, 2:19 PM

## Incremental Planning Without Changes to Location Sequence

The VSR optimizer can now swap the locations B and C so that the sequence is A → B → C → D.

## Incremental Planning with Changes to Location Sequence

Note, however, that the VSR optimizer must not change the location sequence in such a way that B or C is at the

beginning or end of the sequence. This means, for example, that the following location sequences are not allowed:

## B → A → C → D

This is custom documentation. For more information, please visit SAP Help Portal.

168


1/14/26, 2:19 PM

## A → C → D →B

However, the VSR optimizer is allowed to insert a new location X at any point, such as X → A → C → B → D or A → C

→ B → X → D. The prerequisite for this is that you have not chosen incremental planning without inserting new

locations.

The VSR optimizer is not allowed to move the locations A and D.

## Activities

Select the freight units and freight documents to be planned in the transportation cockpit and choose Optimizer Planning. For

more information about optimizer planning, see VSR Optimization.

Select the freight units and freight documents to be planned in the transportation cockpit and choose Transportation Proposals.

For more information, see Generation of Transportation Proposals.

Rough-Cut Planning

## Use

You can use rough-cut planning to schedule the pre-carriage and on-carriage of a transportation without having to define specific

transportation lanes.

## Prerequisites

You have assigned a transshipment location to your transportation zone or a location in the master data and have defined a

fixed duration for the rough-cut planning. To assign transshipment locations, open the Assign Transshipment Location app

on the launchpad.

You have configured the relevant settings and assigned the optimizer settings to your planning profile in the optimizer

settings under Consider Constraints. For more information, see Planning Profile.

## Features

Rough-cut planning is based on a fixed transportation duration within which you can reach the transshipment location assigned to

specific location from this location.

  Note

When rough-cut planning is used, it must be used for both the pre-carriage and on-carriage. You cannot use rough-cut planning

for the pre-carriage and detailed planning for the on-carriage, or vice versa.

If you have made assignments at various levels such as transportation zone or location level, the system uses the value for the

most precise geographical location.

## Example

You want to transport goods from Walldorf to Minneapolis. The source location Walldorf is in the transportation zone Southern

Germany. Frankfurt airport is the transshipment location assigned to the transportation zone Southern Germany. The

destination location Minneapolis is in the transportation zone Midwest. Chicago airport is the transshipment location

assigned to the transportation zone Midwest.

This is custom documentation. For more information, please visit SAP Help Portal.

169


1/14/26, 2:19 PM

You have a master flight schedule that connects Frankfurt and Chicago airports but do not have a transportation lane for

transporting the goods between the source location in Walldorf to Frankfurt airport or between the destination location in

Minneapolis and Chicago airport.

In the master data for the transportation zone Southern Germany, you have specified a rough-cut planning duration of six

hours, and for the location Walldorf two hours.

If you select the Use Rough-Cut Planning Where Defined option in the Rough-Cut Planning selection list in the Optimizer

Settings screen area in the planning profile, the system takes the rough-cut planning duration of two hours into account during

planning for the transportation of goods to Frankfurt airport.

## Validity of Objects

You can define a validity for transportation lanes and default routes. However, this cannot be displayed in VSR optimization.

When you start VSR optimization and VSR optimization comes across a transportation lane or default route, it assumes that this is

valid across the whole planning horizon.

In optimizer preprocessing, the system uses the start of the planning horizon as a reference and transfers to VSR optimization all

objects that are valid on this date and are relevant for the scenario. This results in the following behavior:

VSR optimization does not consider objects that only become valid during the planning horizon.

VSR optimization may still use objects that become invalid during the planning horizon for the whole planning horizon.

For more information, see SAP Notes (SAP Knowledge Base Article) 2997556

 and 3071626

.

  Note

The validity of vehicle resources can be displayed in VSR optimization.

## Related Information

Definition of Transportation Lanes

## Default Route

Use of Default Routes in VSR Optimization

Load Consolidation

## Use

You can use this function to optimize the distribution of freight units and package units to the following resources: trucks,

containers, trailers, and railcars. The system then generates the corresponding business documents: freight orders, container

units, trailer units, and railcar units.

  Note

This function is available only for freight units and package units with the same start and destination location.

## Prerequisites

This is custom documentation. For more information, please visit SAP Help Portal.

170


1/14/26, 2:19 PM

If you want to work with load planning-based consolidation, you have to fulfil the prerequisites for load planning. For more

information, see Load Planning.

You have made the settings for load consolidation, for example, you have made a consolidation strategy. You do this by

opening the Create Load Planning Settings app on the launchpad.

If you want to take the orientation of your products into account during load consolidation, you have to define product

orientation profiles for your products and assign these to your products (WM Packaging view in the material master data).

For more information, see Customizing for Transportation Management under  Master Data

## Product

## Define Product

Orientation Profile . Note that load consolidation supports only the row-stack approach and the orientations Bottom

Straight and Bottom Turned. If you have not defined a product orientation profile for your product or for the corresponding

reference product, the system uses the two standard orientations Bottom Straight and Bottom Turned.

If you want to take the stackability of products into account during load consolidation, you have to make the required

settings. For more information, see Stackability.

## Features

The following modes are available for load consolidation:

## Capacity-based consolidation

With this form of load consolidation, the system creates freight orders or transportation units taking the dimensions of the

affected resources, such as weight or volume, into consideration.

## Load planning-based consolidation

With this form of load consolidation, the system creates freight orders or transportation units and then executes load

planning.

For more information, see Load Planning.

The system takes incompatibilities into consideration in both modes (see Incompatibilities).

## Activities

You start load consolidation in the transportation cockpit. You have the following options:

The system is to consolidate only the selected freight units and resources.

The system is to consolidate the selected freight units and all resources.

The system is to consolidate all freight units and resources.

You can also run load consolidation in the background. For more information, see Load Consolidation Run.

Load Planning

## Use

You can plan the loading space of box trucks, trailers, semi-trailers, and containers in the transportation cockpit or directly in one

of the following business documents:

## Road freight order

This is custom documentation. For more information, please visit SAP Help Portal.

171


1/14/26, 2:19 PM

Trailer unit

## Container unit

Planning is carried out at the level of business document items.

  Note

Load planning returns an approximate calculation of how the available loading space can be optimally used, taking into account

the maximum axle loads and the maximum weight of a vehicle resource. The calculation is based on the master data that you

enter for the resource. It is essential that you check the results calculated during load planning.

## Prerequisites

You have entered master data for the resources such as the height, width, and length of the loading space. For more

information about the master data for load planning, see Master Data in Load Planning.

You have specified in the business document the height, width, and length of the items to be planned.

To define the dimensions of a freight order item in the forwarding order, open the Edit Forwarding Order app on the

launchpad. In the item hierarchy on the Details tab page, you can enter various package details such as the height, width or

length for each package.

To define the dimensions of a freight order item in the freight order, open the Edit Road Freight Order app on the

launchpad. In the item hierarchy on the Details tab page, you can enter various package details such as the height, width or

length for each package.

To define the dimensions of an item in the container unit, open the Edit Container Unit app on the launchpad. In the item

hierarchy on the Details tab page, you can enter various package details such as the height, width or length for each

package.

To define the dimensions of an item in the trailer unit, open the Edit Trailer Unit app on the launchpad. In the item

hierarchy on the Details tab page, you can enter various package details such as the height, width or length for each

package.

To define the dimensions of an item in the package unit, open the Edit Package Unit app on the launchpad. In the item

hierarchy on the Details tab page, you can enter various package details such as the height, width or length for each

package.

Alternatively, you can define the dimensions of a business document item in the transportation cockpit by using drag and

drop to assign a freight unit to a business document. The system automatically copies the dimensions of the freight unit

item to your business document.

In the page layouts for the transportation cockpit, you have activated the following functions:

In the Orders Area, you have activated load planning for freight orders and freight bookings

In the Area for Transportation Units, you have activated load planning for container units and trailer units

In the Order Details Area, you have activated the display of the load plan

To edit page layouts for the transportation cockpit, open the  Define Page Layouts for Transportation Cockpit

 app on

the launchpad. For more information, see Use of Profile and Layout Sets.

Optionally, you have defined your own layouts for the 3D load plan in Customizing for Transportation Management under

Basic Functions

## Load Planning

 Define Layouts for 3D Load Plan  and assigned them to your page layout. This is

necessary, for example, to adjust the display and to activate manual load planning or drag and drop. For more information

about the different layout settings, see Load Plan.

This is custom documentation. For more information, please visit SAP Help Portal.

172


1/14/26, 2:19 PM

If you want to display layers as a separate hierarchy level in the load plan hierarchy, you have selected the Display Layers

checkbox in Customizing for your hierarchy type for the load plan (Consumer of the Hierarchy: Freight Document: Load

Plan). For more information, see Customizing for Transportation Management under  Planning

## General Settings

 Define Hierarchical Views for Business Documents .

You have also specified this hierarchy type for the load plan in your page layout (under  Pushbuttons for Content Toolbar

 Embedded Configurations of Load Plan ).

If you want to take the orientation of your products into account during load planning, you have to define product

orientation profiles for your products and assign these to your products (WM Packaging view in the material master data).

For more information, see Customizing for Transportation Management under  Master Data

## Product

## Define Product

Orientation Profile . Note that the row-stack approach supports Bottom Straight and Bottom Turned only. If you have

not defined a product orientation profile for your product or for the corresponding reference product, the system uses the

two standard orientations Bottom Straight and Bottom Turned.

If you want to take the stackability of products into account during load planning, you have to make the required settings.

For more information, see Stackability.

You are using a pure inbound or outbound scenario. Load planning supports the following scenarios:

Single pickup and multi-drop (outbound)

Multi-pickup and single drop (inbound)

However, “multi-pickup and multi-drop” is not supported. If you have an outbound scenario with returns or empties, “multi-

pickup and multi-drop” can be supported. In this case, load planning ignores returns and empties (see SAP Note 3382660

).

## Features

When you plan a road freight order on a box truck, trailer, or semi-trailer, the system takes into account capacity restrictions in

terms of the height, width, length, and weight of the loading space. The same capacity restrictions also apply to the planning of a

trailer unit on a trailer or semi-trailer. It also takes into account the maximum axle load of your box truck.

Furthermore, in the system you can add a split deck to your trailer or semi-trailer and consequently plan two decks.

When you plan a container unit on a container, the system also takes into account capacity restrictions in terms of the height,

width, and length of the loading space as well as the total weight and the empty weight of the container.

In both the transportation cockpit and in the freight order, you can check the results of load planning as a 3D load plan or a

hierarchical table (load plan hierarchy) containing the business document items. In the 3D load plan, you can show or hide

individual objects as well as entire rows, columns, or stacks. The system also provides you with information about the current load

distribution and utilization of the loading space. You can also create a load chart using the 3D load plan that shows the exact

weight restrictions for each area of the resource, provided you have entered a value for the maximum axle load in the Max. Weight

on Axle Group field. To display the load chart, right-click the load plan and choose Switch Load Chart.

## More Information

Master Data in Load Planning

Automatic Load Planning

## Load Plan

## Rules in Automatic Load Planning

This is custom documentation. For more information, please visit SAP Help Portal.

173


1/14/26, 2:19 PM

Double-Deck and Split Deck Resources

## Double-Deck and Split Deck Resources

Transportation Management supports planning with both fixed and flexible split deck (double-deck) resources.

## Prerequisites

In the master data of your vehicle resource, you have specified the split deck position under  Load Optimization

 Basic

Data .

In the Resource Viewer app under Sections, you have specified information about the split deck, including the type

(platform or beam), size, weight, and movement range. To assist you, there is help available for each input field.

If there are packages that cannot be stacked, you have selected the setting Non-Stackable Package in the requirement

document.

  Note

Only flexible beam split-decks are supported. (The vertical position of a platform split-deck is fixed.)

Flexible split decks are only supported in load planning and not in load consolidation.

All packages must have the same footprint (length & width).

Only one split deck per resource is supported, which must cover the length of the cargo body.

All packages are planned with a straight orientation unless the package width is the longest dimension, in which case

the package is planned with a turned orientation to ensure the package fits safely upon the beams of the split deck.

For example, a standard Europallet (length: 1.20m, width: 0.80m) is placed with a straight orientation to fit on the beam.

If the pallet has a length of 1.0m and a width of 1.20m, it is placed with a turned orientation.

Master Data in Load Planning

## Definition

You can enter various information about your vehicle resources in the master data for load planning. The figures below show a box

truck and a trailer with some sample measurements:

This is custom documentation. For more information, please visit SAP Help Portal.

174


1/14/26, 2:19 PM

## Box Truck

The following table explains the measurements from the figure above:

Measurement in Figure

Name in Master Data

Description

a1

c

a2

d

s2

h

l

  Note

Axle Group Distance 1

Distance between axle group 1 and the front

of the box truck

## Cargo Body Distance

Distance between the start of the loading

space and the front of the box truck

Axle Group Distance 2

Distance between axle group 2 and the

front of the box truck

## Connector Distance

Distance between the trailer coupling of the

box truck and the front of the vehicle

Distance Between Axles

Distance within axle group 2

Interior Height

## Interior Length

Height of the loading space

## Length of the loading space

You must also specify the width of the box truck so that the system can include the loading space of the box truck in automatic

load planning.

This is custom documentation. For more information, please visit SAP Help Portal.

175


1/14/26, 2:19 PM

## Trailer

The following table explains the measurements from the figure above:

Measurement in Figure

Name in Master Data

Description

c

a1

a2

d

h

l

  Note

## Cargo Body Distance

Distance between the start of the loading

space and the front of the trailer

Axle Group Distance 1

Distance between axle group 1 and the front

of the trailer

Axle Group Distance 2

Distance between axle group 2 and the

front of the trailer

## Connector Distance

Distance between the trailer coupling of the

Interior Height

## Interior Length

trailer and the end of the trailer

Height of the loading space

## Length of the loading space

You must also specify the width of the trailer so that the system can include the loading space of the trailer in automatic load

planning.

This is custom documentation. For more information, please visit SAP Help Portal.

176


1/14/26, 2:19 PM

## Tractor

The following table explains the measurements from the figure above:

Measurement in Figure

Name in Master Data

Description

c

a1

a2

d

  Note

## Cargo Body Distance

Distance between the start of the loading

space and the front of the tractor

  Note

Since a tractor does not have any

loading space, Cargo Body Distance

designates the length of the driver's cab

as the start of the loading space.

Axle Group Distance 1

Distance between axle group 1 and the front

of the tractor

Axle Group Distance 2

Distance between axle group 2 and the

front of the tractor

## Connector Distance

Distance between the tractor coupling and

the front of the vehicle

You must also specify the width of the tractor so that the system can display the tractors in the 3D load plan.

This is custom documentation. For more information, please visit SAP Help Portal.

177


1/14/26, 2:19 PM

## Semi-Trailer

The following table explains the measurements from the figure above:

Measurement in Figure

Name in Master Data

Description

a1

s1

k

h

l

p

  Note

Axle Group Distance 1

Distance between axle group 1 and the front

of the trailer

Distance Between Axles

Distance within axle group 1

## King Pin Distance

Distance between the king pin and the front

Interior Height

Interior Length

of the trailer

Height of the loading space

Length of the loading space

## Split Deck Position

Position in the trailer at which you have

added the split deck

You must also specify the width of the semi-trailer so that the system can include the loading space of the semi-trailer in

automatic load planning.

## Container

This is custom documentation. For more information, please visit SAP Help Portal.

178


1/14/26, 2:19 PM

The following table explains the measurements from the figure above:

Measurement in Figure

Name in Master Data

Description

## Interior Height

Height of the loading space

## Interior Length

Length of the loading space

h

l

  Note

You must also specify the width of the container so that the system can include the loading space of the container in automatic

load planning.

## Activities

To define this and other master data, open the Define Resource app on the launchpad.

Alternatively, on the SAP Easy Access screen choose  Transportation Management

 Master Data

 Resources

## Define

Resources .

Automatic Load Planning

## Use

In automatic load planning, also known as load optimization, the optimizer for load planning and load consolidation creates a load

plan for your business document. When it does so, it takes into account capacity restrictions in terms of the height, width, and

length of the loading space as well as the weight. For vehicle resources with two axle groups, it also takes into account the

maximum axle load.

You can perform automatic load planning based on different optimization approaches:

## Row-stack approach

This approach is grid-based. It is recommended for homogeneous loads, that means, packages with the same or similar

footprint, such as Euro pallets.

## Free positioning

This approach allows positioning of the objects independent from rows and stacks. The goal is to both reduce the used

loading space and improve the overall utilization of the truck by avoiding gaps between packages. This approach is

recommended for heterogeneous loads, that means, packages with different footprints, such as boxes, cartons, and

individually packaged large products.

For more information, see SAP Note 3349183

.

  Note

Load consolidation only supports the row-stack approach.

Free positioning does not support all rules and functions of automatic load planning.

## Prerequisites

This is custom documentation. For more information, please visit SAP Help Portal.

179


1/14/26, 2:19 PM

You have created master data for the resources for which you want to optimize the load. For more information about the

master data for load planning, see Master Data in Load Planning.

You have defined the master data for load optimization, for example, the network connections to the optimization server

and the maximum number of users. You can do this on the SAP Easy Access screen under  Cross-Application

## Components

 Processes and Tools for Enterprise Applications

  Remote Control and Communication Framework

 Administration

## Settings

 Edit Destinations .

You have created a planning profile (see Planning Profile) and have assigned the following settings to it:

## Settings for load optimization

You have specified the optimizer engine that you want to use for load planning. You do this by opening the Load

Planning Settings app on the launchpad. Here you can also define various rules for load optimization. For example,

you can specify the maximum difference in height between two adjacent stacks or define a loading pattern (see

Rules in Automatic Load Planning). You can also specify the strategy and the optimizer runtime here.

## Capacity selection settings

You do this by opening the Create Capacity Selection Settings app on the launchpad.

Two Business Add-Ins (BAdIs) are available that you can use to change the results of the optimizer for load planning

and load consolidation. For more information, see Customizing for Transportation Management under  Business

Add-Ins (BAdIs) for Transportation Management

## Planning

 Optimizer for Load Planning and Load

Consolidation :

BAdI: Optimizer for Load Planning and Load Consolidation - Preprocessing

BAdI: Optimizer for Load Planning and Load Consolidation - Postprocessing

For more information, see SAP Note 3349184

.

During an upgrade from an older release in which the old interface for the load planning optimizer was the default, the

checkbox Use Old Interface for Load Planning Optimizer is automatically selected. If you want to use the optimizer engine

for free positioning, you need to deselect this checkbox. For more information, see Customizing for Transportation

Management under  Basic Functions

## General Settings

 Define General Settings for TM .

If you still want to use load planning with the old interface, see SAP Note 3349183

 for more information.

## Features

You can start automatic load planning from the transportation cockpit or directly in a business document. You can check the

results of automatic load planning in a 3D load plan or in a hierarchical table (load plan hierarchy) containing all the planned items.

For more information, see Load Plan.

If automatic load planning was successful, the system automatically sets the load plan item status in the business document to

Planned. If some items cannot be planned due to reasons of capacity, the system automatically sets the load plan status to

Invalidated. For more information, see Explanation of Statuses of Business Documents.

You can use the explanation tool for automatic load planning to compare your entries for automatic load planning with the results

of the optimizer run. You can also use the explanation tool to view information on the current status of a load optimization run. For

example, you can view the actual axle load of your box truck and trailer or your tractor and semi-trailer based on the business

document items that were previously planned. For more information, see Explanation Tool.

## Activities

To start automatic load planning in the transportation cockpit, choose Load Planning.

This is custom documentation. For more information, please visit SAP Help Portal.

180


1/14/26, 2:19 PM

To start automatic load planning from a business document, choose  Follow-Up Actions

 Perform Load Planning .

To start automatic load planning from your worklist, select the business document to be planned and choose Perform Load

Planning.

You can call the explanation tool for automatic load planning using transaction RCC_LOG.

Rules in Automatic Load Planning

## Use

In automatic load planning, you can define rules to be considered by the system during a load optimization run. You can choose

between the following types of rules:

Rules that apply to automatic load planning for all resource types. For more information, see Load Planning Rules

Independent of the Resource Type.

Rules that apply only to the automatic load planning of the upper decks of double-deck trailers. For more information, see

Rules for the Load Planning of Upper Decks.

You can define different rules for the lower and upper deck of double-deck trailers.

However, you cannot combine one rule with another rule if the two rules contradict each other logically. For example, you cannot

define two rules that simultaneously specify that you want the system to load all packages turned and all packages straight in

automatic load planning.

## Structure

The combination of stack, row, and line indicates the exact position of each package loaded onto the resource.

The figures below show the meaning of the terms "stack", "row", and "line" in automatic load planning when viewed from above.

## Stack

This figure shows several packages that are loaded onto the resource one above the other. In automatic load planning, these

packages form a stack.

This is custom documentation. For more information, please visit SAP Help Portal.

181


1/14/26, 2:19 PM

## Row

This figure shows several packages that are loaded onto the resource next to each other from left to right. In automatic load

planning, these packages form a row. The first row of a deck is always towards the start of the loading space.

## Line

This figure shows several packages that are loaded onto the resource one behind the other from front to back. In automatic load

planning, these packages form a line. The first line of a deck is always on the left side of the deck in the direction of travel.

## Features

In your rules you can specify a combination of loading pattern and orientation for each row of your vehicle resource. The system

considers this combination during a load optimization run.

## Loading Pattern

You can define different loading patterns for each vehicle resource that apply to the entire resource. You can define different

loading patterns for the upper and lower deck of a double-deck trailer that both apply to the entire deck. Alternatively, you can

define rules for each resource that apply only to one adjacent row or to several adjacent rows.

When you define the rules for automatic load planning, you can select the following loading patterns:

S (straight)

This loading pattern comprises only packages that are loaded onto the resource straight.

T (turned)

This loading pattern comprises only packages that are loaded onto the resource turned.

E

This is custom documentation. For more information, please visit SAP Help Portal.

182


1/14/26, 2:19 PM

This loading pattern comprises the combination of several same-sized packages that are loaded straight and several same-

sized packages that are loaded turned. The straight and turned packages sit flush at the end of the loading pattern. In

loading pattern E, the packages that are loaded straight are on the left of the packages that are loaded turned.

F

This loading pattern comprises the combination of several same-sized packages that are loaded straight and several same-

sized packages that are loaded turned. The straight and turned packages sit flush at the end of the loading pattern. In

loading pattern F, the packages that are loaded straight are on the right of the packages that are loaded turned.

P (pinwheel)

This loading pattern comprises a total of four same-sized packages that are loaded straight and turned in alternation so

that they form a square with a small area that is free in the middle. As such, the shape of this loading pattern is similar to a

chimney or a pinwheel.

The following figures show examples of the different loading patterns. In each of the selected examples, the loading pattern applies

to the entire resource or the entire deck. The orientation of the packages is always centered.

## Loading Pattern S

This figure shows how all packages are loaded onto a resource in each row straight.

## Loading Pattern T

This figure shows how all packages are loaded onto a resource in each row turned.

This is custom documentation. For more information, please visit SAP Help Portal.

183


1/14/26, 2:19 PM

## Loading Pattern E

This figure shows how all packages are loaded onto a resource in line 1 straight and in line 2 turned. Loading pattern E always

comprises several same-sized packages in line 1 that are loaded straight and several same-sized packages in line 2 that are loaded

turned. The straight and turned packages sit flush at the end of a loading pattern. The loading pattern E is shown twice in this

figure.

Depending on the resource type, you have to enter the following formula in the corresponding rule to get the loading pattern

shown in this figure: E; E

## Loading Pattern F

This figure shows how all packages are loaded onto a resource in line 1 turned and in line 2 straight. Loading pattern F always

comprises several same-sized packages in line 1 that are loaded turned and several same-sized packages in line 2 that are loaded

straight. The straight and turned packages sit flush at the end of a loading pattern. The loading pattern F is shown twice in this

figure.

Depending on the resource type, you have to enter the following formula in the corresponding rule to get the loading pattern

shown in this figure: F; F

This is custom documentation. For more information, please visit SAP Help Portal.

184


1/14/26, 2:19 PM

## Loading Pattern P

This figure shows how four same-sized packages are loaded onto a resource straight and turned in alternation so that they form a

square with a small area that is free in the middle. As such, the shape of this loading pattern is similar to a chimney or a pinwheel.

## Orientation

You can define each of these loading patterns with a specific orientation for all packages that are loaded in a row onto the resource.

You can choose the following orientations:

R - right

L - left

C - centered

## D - distributed

The following figures show examples of the different orientations. In each of the selected examples, the orientation always applies

to the entire resource or the entire deck.

## Orientation R

This figure shows how all packages are oriented on a resource in each row on the right in the direction of travel.

This is custom documentation. For more information, please visit SAP Help Portal.

185


1/14/26, 2:19 PM

## Orientation L

This figure shows how all packages are oriented on a resource in each row on the left in the direction of travel.

## Orientation C

This figure shows how all packages are centered on a resource. If you do not enter any other orientation, during a load optimization

run the system plans all packages on the resource with orientation C.

## Orientation D

This figure shows how all packages are distributed across the row on a resource.

## Activities

To define rules for your load optimization run, open the Create Load Planning Settings app on the launchpad.

To define a specific combination of loading pattern and orientation for the individual rows of a deck, insert a semicolon in the

corresponding rules after each combination of loading pattern and orientation. This means that the first combination always

This is custom documentation. For more information, please visit SAP Help Portal.

186


1/14/26, 2:19 PM

relates to the first row of the deck.

## Example

This figure shows the result of a load optimization run using a rule that comprises different combinations of loading pattern and

orientation for a single deck:

## Example

You have to define the following rule to get the loading pattern shown in this figure: PC; TR; SSD; TL; SSC.

Load Planning Rules Independent of the Resource Type

## Use

You can define the following rules for the optimizer runs for load planning and load consolidation for a specific combination of

equipment group, such as truck or trailer, and equipment type, such as 12-ton box truck or 40-ton trailer.

## Features

Load Planning Rules Independent of the Resource Type

## Number

Explanation

Comment

1000

Stack height increases in

Violation of this rule is liable to penalty costs.

the direction of travel

You cannot combine this rule with rule 1001.

1001

## Stack height decreases

Violation of this rule is liable to penalty costs.

in the direction of travel

You cannot combine this rule with rule 1000.

1100

## Maximum height

Any deviations that are greater than the value defined in this rule are liable to penalty costs.

difference of adjacent

stacks

You cannot combine this rule with rules 1101 and 1102.

1101

## Maximum height

Any deviations that are greater than the value defined in this rule are liable to penalty costs.

difference of stacks

within a row

You cannot combine this rule with rule 1100.

1102

## Maximum height

Any deviations that are greater than the value defined in this rule are liable to penalty costs.

difference of stacks

within a line

You cannot combine this rule with rule 1100.

This is custom documentation. For more information, please visit SAP Help Portal.

187


1/14/26, 2:19 PM

## Number

Explanation

Comment

2000

## Prioritize weight over

You can use this rule to load the heaviest packages and products first instead of loading the

volume, and load

biggest packages and products first.

packages and products

from heaviest to lightest

You cannot combine this rule with rule 2001.

  Note

Packages and products that cannot be loaded are penalized based on their weight. The

default is to penalize based on volume. If you do not define this rule, the system

automatically calculates penalty costs based on the volume of the packages and products

that were not loaded.

  Note

You cannot define this rule for a specific combination of equipment group and equipment

type; instead, you can define this rule only for all resources in an optimizer run.

2001

Prioritize weight and

You can use this rule to load the packages and products that are both the heaviest and the

volume instead of

biggest first instead of loading the biggest packages and products first.

volume only, and load

packages and products

that are both big and

heavy first

You cannot combine this rule with rule 2000.

  Note

Packages and products that cannot be loaded are penalized based on their weight and their

volume. The default is to penalize based on volume only. If you do not define this rule, the

system automatically calculates penalty costs based on the volume of the packages and

products that were not loaded.

  Note

You cannot define this rule for a specific combination of equipment group and equipment

type; instead, you can define this rule only for all resources in an optimizer run.

2100

## Packages and products

You cannot combine this rule with rule 2101.

with high density should

be at bottom of the

  Note

stack

If you do not define a rule for the stacking of packages and products, the system considers

only the weight of each package and product when it builds stacks.

If the maximum weight that can be loaded in a specific package or product falls below the

results of an optimizer run using these rules, the system does not consider this rule for the

package or product in question.

  Note

You cannot define this rule for a specific combination of equipment group and equipment

type; instead, you can define this rule only for all resources in an optimizer run.

2101

## Packages and products

You cannot combine this rule with rule 2100.

can be positioned

anywhere in stack

regardless of weight and

density

  Note

If you do not define a rule for the stacking of packages and products, the system considers

only the weight of each package and product when it builds stacks.

This is custom documentation. For more information, please visit SAP Help Portal.

188


1/14/26, 2:19 PM

## Number

Explanation

## Comment

If the maximum weight that can be loaded in a specific package or product falls below the

results of an optimizer run using these rules, the system does not consider this rule for the

package or product in question.

  Note

You cannot define this rule for a specific combination of equipment group and equipment

type; instead, you can define this rule only for all resources in an optimizer run.

2102

Heavy packages and

The system tries to position heavy packages and products on the floor of the vehicle as far as

products should be

possible.

positioned at the bottom

You cannot combine this rule with rules 2100 and 2101.

2130

Maximum deviation of

You can use this rule to allow stacking of a smaller package or product on top of a larger

dimensions of smaller

package or product in the same stack if the deviation of the package or product dimensions

packages and products

(length and width) is within the given tolerance. However, if you do not use this rule during

on top of larger

automatic load planning or if you enter the value 0 as the maximum deviation, the optimizer

packages and products

plans only identically-sized packages and products on top of each other within a stack.

within a stack

  Note

You cannot use this rule for packages and products in stacks within loading patterns E, F

and P. For more information about loading patterns, see Rules in Automatic Load Planning.

2140

## Packages and products

You can use this rule to ensure that the optimizer also builds stacks with packages and

that are unloaded at

products for different destination locations.

different stops can be

loaded in a stack

  Note

You cannot combine this rule with rule 2150.

2150

Ignore last in first out

You can use this rule to bypass the application of the LIFO principle during automatic load

(LIFO) principle

planning, otherwise the optimizer always applies this rule when you plan packages and

products on a resource.

  Note

You cannot define this rule for a specific combination of equipment group and equipment

type; instead, you can define this rule only for all resources in an optimizer run.

2151

Load packages for a

This rule considers only packages that you have created as exclusive packages for customers.

specific customer at the

For more information, see the section “Automatic Creation of Package Units” under Use of

back of the truck

Package Units in Planning.

2152

## Minimum width for last

The system tries to provide a corridor between each package or product and the vehicle’s back

in first out (LIFO)

door that doesn't contain any packages or products that will be unloaded at a later stop

corridor

2160

Load resource as

The system tries to position all packages and products as close as possible to the driver’s cab

compactly as possible

and the roof of the vehicle. This can result in a lower number of stacks in order to minimize the

used length of the resource.

  Note

You cannot combine this rule with rule 2165.

This is custom documentation. For more information, please visit SAP Help Portal.

189


1/14/26, 2:19 PM

## Number

Explanation

Comment

2161

Minimize number of

The system tries to keep the number of stacks as low as possible.

stacks

2162

2165

## Reduce gaps

The system tries to keep the gaps between the packages and products as small as possible.

## Load resource as broadly

The system tries to position all packages and products as close as possible to the floor of the

as possible

vehicle. This can result in a higher number of stacks in order to maximize the used length of the

resource.

  Note

You cannot combine this rule with rule 2160.

2180

## Disable stacking

If this rule is activated, no packages and products are stacked in the resource.

2200

## Maximum weight per

In the case of a double-deck trailer, the maximum weight per stack that you define here applies

stack

to both decks. You can define an alternative maximum weight for the upper deck of your

double-deck trailer in rule 2201.

3000

Maximum deviation of

You can use this rule to control the left-right weight balance of the load. You define the

weight from center of

maximum deviation of the center of gravity of the load from the center of the cargo body that

cargo body to left and

is allowed. Any deviation that is greater than the value defined in this rule is liable to penalty

right in percent

costs.

3050

Maximum deviation of

The automatic load planning minimizes the deviation of axle utilization between a vehicle’s axle

axle utilization in percent

groups. Penalty costs are incurred for deviations that are higher than the defined maximum

limit (parameter value). The utilization of the king pin is taken into account in the case of semi-

trailers. For a combination of tractor and semi-trailer, only the second and third axle group are

taken into consideration.

3100

Minimum weight on

If you have defined an axle as a driving axle in the master data, the axle load must not fall

driving axle relative to

below the percentage of the current total weight of the loaded resource that you have specified

total weight of vehicle

here.

resource in percent

3101

Minimum weight on

If you have defined an axle as a steering axle in the master data, the axle load must not fall

steering axle relative to

below the percentage of the current total weight of the loaded resource that you have specified

total weight of vehicle

here.

resource in percent

4000

## U.S. Federal Bridge

In the Federal Bridge Formula, the U.S. government defines specific rules that have to be

## Formula

considered for road transportation in the United States. For more information, see

http://ops.fhwa.dot.gov/freight/publications/brdg_frm_wghts/index.htm .

  Note

You cannot define this rule for a specific combination of equipment group and equipment

type; instead, you can define this rule only for all resources in an optimizer run.

8001

Load all packages and

The combination of loading pattern and orientation that you define in this rule applies to your

products with same

entire resource.

loading pattern

You cannot combine this rule with the following rules: 8011, 8021, 8022, 8023, 8024, 8025,

8026, 8052, and 8056.

This is custom documentation. For more information, please visit SAP Help Portal.

190


1/14/26, 2:19 PM

## Number

Explanation

Comment

8011

Load all packages and

In this rule you can define a specific combination of loading pattern and orientation for each

products with a loading

row of your resource.

pattern specific to each

row

You cannot combine this rule with the following rules: 8001, 8021, 8022, 8023, 8024, 8025,

8026, 8052, and 8056.

8021

Load all packages and

You cannot combine this rule with the following rules: 8001, 8011, 8022, 8023, 8024, 8025,

products turned

8026, 8052, and 8056.

8022

Load all packages and

If you use this rule for your automatic load planning, the system plans all packages and

products in each row

products in your resource in straight rows. If there is not enough space for other straight rows,

straight; if not enough

the system turns the remaining packages and products in the first rows of the resource.

space turn packages and

products in first rows

You cannot combine this rule with the following rules: 8001, 8011, 8021, 8023, 8024, 8025,

8026, 8052, and 8056.

8023

Load all packages and

If you use this rule for your automatic load planning, the system plans all packages and

products in each row

products in your resource in straight rows. If there is not enough space for other straight rows,

straight; if not enough

the system turns the remaining packages and products in the last rows of the resource.

space turn packages and

products in last rows

You cannot combine this rule with the following rules: 8001, 8011, 8021, 8022, 8024, 8025,

8026, 8052, and 8056.

8024

Load all packages and

You cannot combine this rule with the following rules: 8001, 8011, 8021, 8022, 8023, 8025,

products straight

8026, 8052, and 8056.

8025

Load all packages and

If you use this rule for your automatic load planning, the system turns all packages and

products in each row

products in your resource. If there is not enough space for other turned rows, the system plans

turned; if not enough

the remaining packages and products in the first rows of the resource in straight rows.

space load all packages

and products in first

rows straight

You cannot combine this rule with the following rules: 8001, 8011, 8021, 8022, 8023, 8024,

8026, 8052, and 8056.

8026

Load all packages and

If you use this rule for your automatic load planning, the system turns all packages and

products in each row

products in your resource. If there is not enough space for other turned rows, the system plans

turned; if not enough

the remaining packages and products in the last rows of the resource in straight rows.

space load all packages

and products in last rows

straight

You cannot combine this rule with the following rules: 8001, 8011, 8021, 8022, 8023, 8024,

8025, 8052, and 8056.

8052

Load all packages and

If you use this rule for your automatic load planning, the system turns all packages and

products in first row

products in the first row in your resource regardless of your remaining loading patterns.

turned

You cannot combine this rule with the following rules: 8001, 8011, 8021, 8022, 8023, 8024,

8025, 8026, and 8056.

8056

Load all packages and

If you use this rule for your automatic load planning, the system turns all packages and

products in last row

products in the last row in your resource regardless of your remaining loading patterns.

turned

You cannot combine this rule with the following rules: 8001, 8011, 8021, 8022, 8023, 8024,

8025, 8026, and 8052.

8060

## Stabilize load by turning

You can use this rule to reduce the risk of packages and products shifting during

packages and products

transportation. However, you cannot use this rule for the last rows of loading patterns E, F, and

in last rows if necessary

P.

## Rules for the Load Planning of Upper Decks

This is custom documentation. For more information, please visit SAP Help Portal.

191


1/14/26, 2:19 PM

You can define the following rules for the load optimization runs for the upper decks of double-deck trucks and double-deck

trailers.

Number

2201

2211

2221

Rules for the Load Planning of Upper Decks

Explanation

## Comment

Maximum weight per stack on the upper

You can use this rule to define a maximum

deck

weight per stack for the upper deck of your

resource that differs from the maximum

weight per stack for the lower deck of your

resource that you defined in rule 2200.

Maximum weight per row on the upper deck

The maximum weight per row for the upper

deck does not apply to rows that are part of
the loading patterns P, E, and F.

Maximum weight per stack in the middle of

This rule applies only to rows with at least

a row on the upper deck

three stacks. The rule does not apply to

rows that are part of the loading patterns P,

E, and F.

If you combine this rule with rule 2201, the

system considers the lower of the two

specified maximum weights.

8002

Upper deck: Load all packages and

The combination of loading pattern and

products with same loading pattern

orientation that you define in this rule

applies to the entire upper deck of your

resource.

You cannot combine this rule with the

following rules: 8012, 8031, 8032, 8033,

8034, 8035, 8036, 8053, and 8057.

8012

Upper Deck: Load all packages and

In this rule you can define a specific

products with a loading pattern specific to

combination of loading pattern and

each row

orientation for each row of the upper deck

of your resource.

You cannot combine this rule with the

following rules: 8002, 8031, 8032, 8033,

8034, 8035, 8036, 8053, and 8057.

8031

8032

Upper deck: Load all packages and

You cannot combine this rule with the

products in each row turned

following rules: 8002, 8012, 8032, 8033,

8034, 8035, 8036, 8053, and 8057.

Upper deck: Load all packages and

If you use this rule for your automatic load

products in each row straight; if not enough

planning, the system plans all packages and

space turn packages and products in first

products on the upper deck of your

rows

resource in straight rows. If there is not

enough space for other straight rows, the

system turns the remaining packages and

products in the first rows of the upper deck.

You cannot combine this rule with the

following rules: 8002, 8012, 8031, 8033,

8034, 8035, 8036, 8053, and 8057.

This is custom documentation. For more information, please visit SAP Help Portal.

192


1/14/26, 2:19 PM

Number

8033

8034

8035

Explanation

## Comment

Upper deck: Load all packages and

If you use this rule for your automatic load

products in each row straight; if not enough

planning, the system plans all packages and

space turn packages and products in last

products on the upper deck of your

rows

resource in straight rows. If there is not

enough space for other straight rows, the

system turns the remaining packages and

products in the last rows of the upper deck.

You cannot combine this rule with the

following rules: 8002, 8012, 8031, 8032,

8034, 8035, 8036, 8053, and 8057.

Upper deck: Load all packages and

You cannot combine this rule with the

products in each row straight

following rules: 8002, 8012, 8031, 8032,

8033, 8035, 8036, 8053, and 8057.

Upper deck: Load all packages and

If you use this rule for your automatic load

products in each row turned; if not enough

planning, the system turns all packages and

space load all packages and products in

products on the upper deck of your

first rows straight

resource. If there is not enough space for

other turned rows, the system plans the

remaining packages and products in the

first rows of the upper deck in straight rows.

You cannot combine this rule with the

following rules: 8002, 8012, 8031, 8032,

8033, 8034, 8036, 8053, and 8057.

8036

Upper deck: Load all packages and

If you use this rule for your automatic load

products in each row turned; if not enough

planning, the system turns all packages and

space load all packages and products in last

products on the upper deck of your

rows straight

resource. If there is not enough space for

other turned rows, the system plans the

remaining packages and products in the

last rows of the upper deck in straight rows.

You cannot combine this rule with the

following rules: 8002, 8012, 8031, 8032,

8033, 8034, 8035, 8053, and 8057.

8053

Upper deck: Load all packages and

If you use this rule for your automatic load

products in first row turned

planning, the system turns all packages and

products in the first row on the upper deck

of your resource regardless of your

remaining loading patterns.

You cannot combine this rule with the

following rules: 8002, 8012, 8031, 8032,

8033, 8034, 8035, 8036, and 8057.

This is custom documentation. For more information, please visit SAP Help Portal.

193


1/14/26, 2:19 PM

Number

8057

Explanation

## Comment

Upper deck: Load all packages and

If you use this rule for your automatic load

products in last row turned

planning, the system turns all packages and

products in the last row on the upper deck

of your resource regardless of your

remaining loading patterns.

You cannot combine this rule with the

following rules: 8002, 8012, 8031, 8032,

8033, 8034, 8035, 8036, and 8053.

## Stackability

During load planning and load consolidation, the system takes stackability of products into account.

You can define the following settings:

## Stackability between two products

You define stacking settings for your products or reference products in a product relationship profile, which you then

indicate in your load planning settings.

  Note

Only the stacking settings defined in the product relationship profile are taken into account, not the

consolidation settings.

These stacking settings only indicate whether a product can be directly stacked on another product. The system

doesn't check whether this product can be indirectly stacked on another product, that means, with a third

product inbetween. If you want the system to also check indirect stacking, you can enable this with a Business

Add-In (BAdI) for the row-stack approach.

To define a product relationship profile, open the Change Product Relationship Profile app from the launchpad. To indicate

the profile in your load planning settings, open the Edit Load Planning Settings app from the launchpad.

## Stackability of products on themselves

You indicate the maximum stacking factor for your products and packaging materials in your master data.

To create a product, on the SAP Easy Access screen, choose  Logistics

 Transportation Management

 Master Data

## Material

 MM01 - Create . You can define the maximum stacking factor in the following places:

On product header level

On the  Additional Data

 Units of measure  view

  Note

Due to compatibility reasons, load planning and load consolidation ignore the maximum stacking factor defined on the

Units of measure view if a maximum stacking factor greater than zero is defined on product header.

For example, you can specify a maximum stacking factor of two for pallets (PAL). This means, that up to two pallets can be

stacked on top of each other. If you don't indicate a maximum stacking factor or indicate a maximum stacking factor of

zero, this means that the product or package can be stacked an infinite number of times on itself. A maximum stacking

factor of one means that the product or package can't be stacked on itself.

This is custom documentation. For more information, please visit SAP Help Portal.

194


1/14/26, 2:19 PM

You can define different maximum stacking factors per unit of measure.

## Weight put on top of a package

The system checks the maximum top load that you have defined in the master data of your products. The maximum top

load describes the maximum weight that you can place on top of a product's full package.

## Load planning rules

You can define load planning rules that control stackability, such as rule 2180. For more information, see Rules in Automatic

Load Planning.

The system considers these settings in the following way:

## Stacking settings

Stacking settings are considered for products and packages. For packages, the handling is different depending on whether

a closed packaging material or open packaging material is used.

The stacking settings are considered for closed packaging materials, such as pallet cages. However, stacking settings for

products inside closed packages are ignored.

The stacking settings are also considered for top-level packages with open packaging material and all products inside. The

stacking settings for reference products are considered, too.

Package A can be stacked on package B if the following prerequisites are met:

All products in package A can be stacked on all products in package B.

The packaging material of package A can be stacked on the package material of package B.

Package B is stackable (defined by unified package building), that is, UPB allows that something can be stacked on

it.

However, stacking settings for products contained in cartons put on pallets are ignored.

## Maximum stacking factor

The maximum stacking factor is considered for products and packages. However, stacking is only allowed for top-level

packages that have been defined as stackable by unified package building (or by a customer enhancement).

For closed packaging materials, only the maximum stacking factor defined for the packaging material and the unit of

measure of the package item is considered. Thus, the content of the package does not matter.

For an open packaging material, its maximum stacking factor is only considered if empty packages are stacked on each

other. If the package contains at least one product or another package, the maximum stacking factor of the packaging

material is ignored by load planning and load consolidation, and the maximum stacking factor of the product or package

inside is considered.

The maximum stacking factor on reference product level is considered, too. However, only the reference product level

directly above the real products is considered. Maximum stacking factors defined for reference products of reference

products are ignored.

Load Plan

## Definition

The load plan is the result of load planning. It provides you with an overview of how the loading space available for transporting a

business document is currently used. A load plan is also created for detailed mixed package building. It provides you with an

This is custom documentation. For more information, please visit SAP Help Portal.

195


1/14/26, 2:19 PM

overview of the loading of a package or a pallet, for example.

In both the transportation cockpit and in the business document, you can display the complete load plan as a 3D load plan or as a

hierarchical table (load plan hierarchy).

You have the following options in the 3D load plan:

You can show and hide gridlines in your decks.

You can show and hide individual objects as well as entire rows, columns, or stacks and fill with different colors. You can

define colors for your 3D load plan in Customizing for Transportation Management under  Basic Functions

## Colors

 Define Colors for Gantt Chart, Load Planning, and Geographical Map .

You can also specify colors for the x, y, and z axis. These colors are then used when you drag objects along these axes. For

more information, see Customizing for Transportation Management under  Basic Functions

 Load Planning

## Define

Layouts for 3D Load Plan  (Colors view).

You can display labels for higher-level packages (outer packaging). The labels can contain up to three package attributes.

You can also display a ruler for resources (such as trucks) and equipment types. You must have selected the Show Item

Labels or Show Ruler for Resources/Equipment Types checkbox in Customizing for Transportation Management under

Basic Functions

## Load Planning

 Define Layouts for 3D Load Plan . You have also defined the required attributes for

item labels under Additional Texts. You can define these separately for loaded and not loaded items.

You can adjust a load plan manually using pushbuttons in the toolbar, keyboard shortcuts, or drag and drop to move

products and packages on a truck. The status and the axle load are adjusted accordingly. You must have selected the

Enable Manual Load Planning checkbox in Customizing for Transportation Management under  Basic Functions

## Load

## Planning

 Define Layouts for 3D Load Plan  and have also selected Enable Drag and Drop for drag and drop. You can

also define in this Customizing activity which combination of keys execute which command and how far an object should

be moved (length of the movement increment).

Drag and drop also allows you to create a load plan, that is, to move one or more unplanned objects into the truck’s loading

space or to remove them from the truck again.

You can also define your own toolbar in this Customizing activity. First, you create an ID for the toolbar, which you can

optionally enter in the Layouts view under Display Settings. Then you select the items for your toolbar, such as buttons

and button choices, as well as the sequence in which they are to be displayed. You can select these items from a list of

predefined actions and change their description. For a button choice, you must also specify the subitems.

For example, you can arrange items in the 3D load plan flat or in stacks, lift them up, and drop them down again.

Actions such as positioning items in the 3D load plan as well as selecting and deselecting items can be performed for

several items at the same time. In addition, you can select all items with the same source or destination location, product,

or items in the same stack or row.

You can change the orientation of your top-level products in the load plan using the context menu, the Orientation

pushbutton, or keyboard shortcuts. You must have selected the Enable Manual Load Planning checkbox in Customizing for

Transportation Management under  Basic Functions

## Load Planning

## Define Layouts for 3D Load Plan . You can also

define in this Customizing activity which combination of keys execute which change of orientation. Note that you can only

change the orientation according to the product orientation profile that you have defined for the product (see

"Prerequisites" under Load Planning).

If you have created your load plan with layer-based mixed package building based on the package building optimizer (that

is, if you have selected detailed mixed package building as the mixed package building mode), each layer is represented as

a block instead of the individual products on the layer.

You can use a Business Add-In (BAdI) to display products as COLLADA models. For more information, see SAP Note

3478427

.

You have the following options in the load plan hierarchy:

This is custom documentation. For more information, please visit SAP Help Portal.

196


1/14/26, 2:19 PM

You can create a load plan manually by entering a value greater than zero for a product in the Loading Sequence column.

You can also specify the position and orientation. If you work with split deck resources, you must also specify whether the

product is to be loaded onto the upper or lower deck. The system recalculates the axle loads.

You can adjust the position and orientation of products and packages by manually changing the coordinates.

For combination resources, you can move the items from one trailer to the other using drag and drop.

You can display which profile, which engine (that is, which package builder, packing instruction, or packaging specification),

and which rule (that is, which packing instruction or packaging specification) was used for unified package building. If you

make changes to the package item itself or to the packed items that result in the load plan status of the package item being

automatically set to Not Planned or Invalidated, the information in these fields is deleted. For more information, see

Unified Package Building.

You can add items for auxiliary packaging materials manually. Top-level auxiliary packaging material items are considered

in load planning.

You can set the load plan item status (cargo) for auxiliary packaging materials manually. Alternatively, the system can set it

automatically during unified package building or load planning.

The load plan status (capacity) is not relevant for auxiliary packaging materials because auxiliary packaging materials do

not have their own capacity.

For more information about packaging materials, see Use of Auxiliary Packaging Materials.

You can change the orientation of your products in the Orientation field. For more information about the prerequisites, see

the corresponding paragraph for the 3D load plan.

Note that there are dependencies between some actions in the load plan and the load plan status value Finalized. For

example, you cannot delete the load plan if the load plan status of a resource has the value Finalized. For more information,

see the section "Fixing of Packages" under Creation or Update of Consignment or Freight Orders on Inbound Messages.

You can display layers as separate hierarchy levels.

## Structure

The load plan hierarchy contains the following information about the business document item:

## Item

## Loading sequence

Row, stack, and level in the loading space

## Gross weight

Height, width, and length

## Stackability

You also get information about the load distribution as well as additional statistical data about the current load on separate tab

pages. This includes the following:

Number of loaded business document items

Used area on the lower deck of your double-deck trailer

Utilization of the loading volume in percent

Used area on the upper deck of your double-deck trailer

This is custom documentation. For more information, please visit SAP Help Portal.

197


1/14/26, 2:19 PM

Maximum weight for each axle group compared to the current weight for each axle group

## Maximum trailing load compared to the current trailing load

A load plan that was created for detailed mixed package building also contains the following information:

Products and product items in the package (product hierarchy)

Exact position of the products in the package

You can overwrite this exact position.

## Orientation of the products in the package

Parent location, in other words the parent location of the location hierarchy that you have defined in your unified package

building profile

You can also display packages graphically in the 3D load plan. You can use Switch Package Details to change the display so that

the exact contents of the package are displayed (the individual products and product items).

You must have selected the Show Package Details checkbox in Customizing for Transportation Management under  Basic

Functions

## Load Planning

 Define Layouts for 3D Load Plan .

You can print the load plan with or without the 3D load plan. For more information, see Load Plan Printing.

## Related Information

Detailed Mixed Package Building

Unified Package Building Profile

## Utilization

## Load Plan Printing

You can print the hierarchical table of the load plan (load plan hierarchy) with or without 3D images (3D load plan).

First, a PDF file of the load plan is created for each business document. You can then print this PDF file on paper, for example, or

send it as an e-mail attachment. This printout can be used by the warehouse staff or the truck driver, for example, while loading or

unloading at the warehouse door.

## Prerequisites

To print the load plan with one or more 3D images, you need a subscription to the image creation service provided by SAP

Enterprise Product Development (EPD).

You have made the following settings in Customizing for Transportation Management under  Basic Functions

## Load

Planning

 Printing :

You have defined a load plan printing profile in the Customizing activity Define Load Plan Printing Profile.

In the load plan printing profile, you specify a load plan printing layout and a layout for the 3D load plan as well as

whether the 3D load plan is to be printed as one or more 3D images that represent the individual loading steps.

You have assigned your load plan printing profile to the desired business document type, such as the freight order

type, in the Customizing activity Assign Load Plan Printing Profile.

You have defined a load plan printing layout in the Customizing activity Define Load Plan Printing Layout.

This is custom documentation. For more information, please visit SAP Help Portal.

198


1/14/26, 2:19 PM

You have specified the sections that are to be contained in the load plan printing layout in the Customizing activity

Configure Load Plan Printing Layout.

You have made the settings for output management in your freight order type and container unit type in Customizing

(Output Options area); for example, you have entered the additional output profile /SCMTMS/TOR_PRINT_ROAD. For

more information, see Output Management.

## Features

You print the load plan from the business document or from the transportation cockpit. A background report is also available. The

system creates one PDF file for each business document.

Depending on how you have configured the load plan printing layout and on which type of business document you want to print,

the PDF file can contain the following sections:

Header, for example, document number, page number, and logo

General information, for example, carrier name and departure date

Stop sequence, in other words, location and address data as well as arrival and departure times

Capacity and cargo overview, for example, information about available capacity and utilization

Packaging material overview, in other words, the aggregated quantities of the top-level packaging materials and the

number of unpackaged products

Item list, in other words, top-level packages and unpackaged products in their loading sequence

Detailed item list, in other words, an expanded view of the items including the complete packaging hierarchy

## One or more 3D images

The following business documents are supported:

Road freight order

## Container unit

Load plan printing is based on the standard printing framework (output management).

## Activities

You start load plan printing via the output management of the relevant business document (Output Management tab page,

Loading/Unloading Instruction (Loading Plan) action).

## Personal object worklist for freight orders

You start load plan printing using the Mass Output button (Loading/Unloading Instruction (Loading Plan)(Archived

Issue) action).

## Transportation cockpit

You start load plan printing using the Print button.

## Background report

On the SAP Easy Access screen, choose  Logistics

 Transportation Management

 Administration

 Background

## Processing

 Print Load Plan .

This is custom documentation. For more information, please visit SAP Help Portal.

199


1/14/26, 2:19 PM

After the report has been executed, you can open the PDF files with the respective load plan in the following places:

## Business document

Choose Open Archive Link on the Output Management tab page under Communication Data.

## Application log

Copy the link in the Archive Link field or choose Open Archive Link.

Related Information

Load Plan

Load Planning

Output Management

One-Step Planning

## Use

In the case of one-step planning, the system performs a complete planning run that comprises any combination of VSR

optimization, carrier selection, and load optimization.

## Features

For one-step planning, SAP delivers the standard planning strategy VSR_1STEP. This combines the two standard planning

strategies VSR_DEF for VSR optimization and TSPS_DEF for carrier selection.

You can use VSR_1STEP for VSR optimization and for the generation of transportation proposals. When transportation proposals

are generated, carrier selection is performed for each transportation proposal generated. If you then want to perform a load

optimization, you can add method VSR_ALP to VSR_1STEP. Alternatively, you can define your own planning strategy that

comprises any combination of the methods of VSR optimization, carrier selection, and load optimization. The following methods

can be used, for example:

VSR_PRE for preprocessing the VSR optimization run

VSR_OPT for the VSR optimization run

VSR_POST for postprocessing the VSR optimization run

VSR_TSPS for carrier selection

## VSR_ALP for load planning

You can define planning strategies in Customizing under  Transportation Management

 Basic Functions

 Process Controller

 Define Strategy .

  Note

SAP also delivers the standard planning strategy VSRI_1STEP for one-step planning in manual planning. If you enter this

strategy as a strategy for manual planning in your planning profile, the system automatically performs carrier selection at the

end of manual planning (that is, if you assign a freight unit to a resource). Here you can also add load optimization to the

standard planning strategy. Alternatively, you can also define here your own planning strategy that comprises any combination

of VSR optimization, carrier selection, and load optimization.

This is custom documentation. For more information, please visit SAP Help Portal.

200


1/14/26, 2:19 PM
## Activities

If you want to use the standard planning strategy VSR_1STEP, specify it in the optimizer settings. To do this, open the Create

Optimizer Settings app on the launchpad.

More Information

Planning Strategies

VSR Optimization

Carrier Selection

Load Planning

Scheduling

## Use

Scheduling determines start and end times for a set of dates and times such as departure and arrival of a freight order as well as

the pick-up and delivery of the assigned freight units or the coupling and uncoupling of trailers. In scheduling, the system

considers multiple constraints like a predefined relative ordering among the activities of the freight order as well as the pick-up

windows and the delivery windows of the assigned freight units or the availability of the driver that is to transport a particular road

freight order. Scheduling can be triggered for one or more selected freight orders and is based on your settings in the planning

profile (see Planning Profile).

  Note

For schedule-based freight orders and freight bookings, scheduling does not consider loading and unloading durations.

## Prerequisites

You have made the following settings in the planning profile:

You have specified a planning horizon. If you do not do so, the system uses the values defined in the default profile.

You have specified loading and unloading durations for your freight units. If you do not do so, the system sets the loading

and unloading durations for your freight units to 0. For more information, see Loading and Unloading Durations.

You have specified coupling and uncoupling durations. If you do not do so, the system sets the coupling and uncoupling

durations to 0.

You have specified if the system is to consider requested or acceptable pick-up and delivery dates for your freight units.

You have specified if you want to use scheduling in a forward or in a backward direction. By default, the system uses

forward scheduling.

You have specified a scheduling strategy.

## Features

## Scheduling Strategy

This is custom documentation. For more information, please visit SAP Help Portal.

201


1/14/26, 2:19 PM

In the scheduling settings of your planning profile, you can specify which scheduling strategy you want to use. We provide the

following standard scheduling strategies:

Scheduling (Embedded) (VSS_EMBED)

This is the default scheduling strategy. It doesn't require a remote communication and control framework (RCCF) call. You

can indicate in the scheduling settings, that the system is to take into account cost-based requested dates/times. However,

this strategy doesn't take into account scheduling constraints that you have defined in Customizing.

Scheduling (Optimizer Server) (VSS_DEF)

## Forward and Backward Scheduling

You can use scheduling in a forward or in a backward direction:

In forward scheduling, the system first defines the start and end time of the first activity to be scheduled. Afterwards, the

system assigns start and end times for all succeeding activities.

In backward scheduling, the system first defines the start and end time of the last activity to be scheduled. Afterwards, the

system assigns start and end times for all preceding activities.

For both types of scheduling, the system tries to schedule the activities with as little idle time between the individual activities as

possible. Equally, the system considers the coupling and uncoupling of trucks and trailers as well as the availability of drivers and

vehicle resources. In this case, the system considers the coupling of the trailer to a vehicle and the loading of a freight unit into the

trailer as separate activities.

## Constraints

Scheduling considers the following constraints:

Time windows for loading and unloading activities for your freight units

Loading and unloading durations of your freight units

Appointments for the freight order your freight units are assigned to

Location sequence of your freight order

Existing freight orders on resources

  Note

This does not apply to multiresources.

Fixed departure time of a freight order stage

## Coupling and uncoupling durations

Absences and non-working times of the involved drivers

## Downtimes and non-working times of the involved vehicle resources

Calendar resources as well as the calendars and capacities for the loading and unloading activities of handling resources

Calendars of the involved vehicle resources and drivers for loading, unloading, transportation, coupling, and uncoupling

activities

Minimum and maximum goods wait times defined for transshipment locations

This is custom documentation. For more information, please visit SAP Help Portal.

202


1/14/26, 2:19 PM

Additionally, you can specify specific scheduling constraints such as working times. For more information, see Customizing for

Transportation Management under  Planning

## General Settings

 Define Scheduling Constraints .

  Recommendation

We recommend that you define driving and working constraint profiles instead of scheduling constraints. While the scheduling

constraints can lead to longer travel or waiting times, which are hard to understand, the advantage of driving and working

constraint profiles is that rests of a certain duration are scheduled without interruption and that these rests can be displayed

on the user interface. Further, scheduling constraints are no longer supported by embedded scheduling. Weitere Informationen

finden Sie unter Considering Driving Time and Working Hours Constraints.

## Scheduling in the Freight Order User Interface

If you start scheduling from the user interfaces for freight orders, the system calculates the planned dates for your freight orders.

You can select the scheduling direction either in the freight order or in the planning profile.

For the scheduling of freight orders, you have the following options:

## Scheduling based on the planning profile

With this option, the system determines the scheduling direction based on the planning profile. If you have not defined a

planning profile, the system uses forward scheduling by default.

## Forward scheduling

With this option, the system uses forward scheduling irrespective of the planning profile. If you have specified a departure

date/time, the system then fixes this and carries out forward scheduling starting from this date. In doing so, the system

always refers to the current transportation stop.

## Backward scheduling

With this option, the system uses backward scheduling irrespective of the planning profile. If you have specified an arrival

date/time, the system then fixes this and carries out backward scheduling starting from this date. In doing so, it always

relates to the last transportation stop, meaning the destination location.

## Execution-Based Scheduling

If a business document is already in execution and an event is reported for an activity, the system fixes this activity at the reported

position. During scheduling, the system ignores all activities before the last executed activity.

Note that if at least one activity at a stop has status In Execution or Executed, the system ignores all activities of this stop.

## Explanation Tool for Scheduling

You can analyze your scheduling results. For more information, see Explanation Tool for Scheduling.

## Activities

To start scheduling, you have the following options:

You can start scheduling from the transportation cockpit by choosing Scheduling in the transportation cockpit areas for

freight orders and transportation units or in the Gantt chart of the Transportation Cockpit app. Additionally, in the Gantt

chart, you can schedule road freight orders and trailer units per drag and drop.

You can start scheduling from the user interfaces for freight orders by choosing Scheduling and then selecting one of the

options listed above. For more information, see Scheduling of Freight Orders.

This is custom documentation. For more information, please visit SAP Help Portal.

203


1/14/26, 2:19 PM

If you have activated the user parameter /SCMTMS/SCH_FORCE, you can start scheduling automatically by entering the

departure date of a freight order and pressing ENTER. Here, you can choose between the following options:

X activates this function for freight orders on all user interfaces where you can use scheduling.

T activates this function for freight orders in the transportation cockpit only.

## Example

## Forward Scheduling

Customer A orders 50 pallets of product X. Customer A asks for a delivery date in three weeks. Currently, the capacity of your

depot is 100 m³. Product X takes up 95 m³ of your depot. Therefore, you decide to move the goods out of your depot as soon as

possible in order to minimize your inventory. That is why you decide to use forward scheduling.

## Backward Scheduling

Customer B orders 50 pallets of product Y. Customer B asks for a delivery date in three weeks. Currently, the capacity of your

depot is 100 m³. Product Y takes up 5 m³ of your depot. Therefore, you decide to stick to the delivery time window as closely as

possible. That is why you decide to use backward scheduling.

More Information

SAP Note 1908165

## Schedule Unplanned Requirement Documents

To improve your planning decisions, you can quickly generate the approximate transportation time for requirement documents

without needing to plan the documents. In addition, the Gantt chart can display the stage sequence to provide a useful visual aid.

## Prerequisite

In Customizing, under  Transportation Management

 Planning

## Freight Unit

## Define Freight Unit Types , you have selected

Enable Automatic Determination from the Distance/Duration dropdown list.

## Use

There are multiple ways to schedule an unplanned requirement document:

Applying a default route to the document

## Clicking Schedule

## Starting the freight unit building process

You can view the scheduling results on the Gantt chart and in the requirement document (see Activities below).

## Features

After scheduling, the requirement document contains the transportation times for each stage (planned arrival and planned

departure times) but the document is still unplanned.

This is custom documentation. For more information, please visit SAP Help Portal.

204


1/14/26, 2:19 PM

Stop activities are used to calculate the transportation times of the stages but the stop data is not contained in the

requirement documents (and therefore not visible on the Gantt chart.)

Stop durations consider the following activities:

Preparing for the stop

Loading and unloading

## Finalizing the stop

In addition, operating times of the location and the handling resource are considered

Scheduling ignores the handling resource capacity.

Scheduling can run forwards or backwards. The direction is defined in Scheduling Settings.

Scheduling uses the requested and accepted loading or unloading time-windows of the requirement document and uses

the settings defined in Scheduling Settings.

Scheduling considers minimum and maximum wait-time constraints defined either in the location master or in the default

route – if a default route is applied.

Stages that are already planned in the requirement document are unaffected by this scheduling process. Additionally,

newly scheduled stages do not overlap planned stages.

## Activities

To view the scheduling results in the requirement document, complete the following steps:

1. Display a requirement document by opening a requirement document worklist app from the lauchpad, for example Freight

Units and then selecting a freight unit.

2. In the Stages tab, select a stage.

The stage information is displayed.

3. Select the Planning/Execution Data tab.

4. Optionally, you can save the schedule to the requirement document.

Consideration of Scheduling Constraints

## Use

You can use this function to consider additional constraints during scheduling. This allows the system to extend the trip durations

in transportation plans so that a driver can take their required breaks.

  Note

The system considers scheduling constraints both during scheduling and during vehicle scheduling and routing (VSR)

optimization. However, it does not consider scheduling constraints during scheduling if you are using the scheduling strategy

Scheduling (Embedded).

  Example

This is custom documentation. For more information, please visit SAP Help Portal.

205


1/14/26, 2:19 PM

A truck would require two days for a trip from the east coast to the west coast of the United States. However, since the driver

must take breaks along the way, a longer trip duration must be scheduled.

  Note

No legal regulations are delivered with this function.

The aim of this function is not to map legal regulations. It only allows the system to extend the trip durations in

transportation plans that give the driver a sufficient buffer and allow them to take the required breaks.

This function only applies for vehicle resources. Passive vehicle resources and schedules are not supported.

  Recommendation
We recommend that you define driving and working constraint profiles instead of scheduling constraints. While the scheduling

constraints can lead to longer travel or waiting times, which are hard to understand, the advantage of driving and working

constraint profiles is that rests of a certain duration are scheduled without interruption and that these rests can be displayed

on the user interface. Further, scheduling constraints are no longer supported by embedded scheduling. For more information,

see Considering Driving Time and Working Hours Constraints.

## Prerequisites

You have defined constraints for scheduling in Customizing. These constraints represent your rules. You combine several

constraints in one set. You can assign this set to one or more means of transport. For more information, see Customizing

for Transportation Management under  Planning

## General Settings

 Define Scheduling Constraints .

In the scheduling settings of your planning profile, you have indicated in the Consider Time Constraints field that

scheduling constraints are to be considered. In your transportation cockpit session, you can overrule this setting in the

Change Planning Settings dialog box.

You have defined the duration of the activities:

## Transportation

You define this duration in the transportation lane. To do so, on the SAP Easy Access screen, choose

Transportation Management

## Master Data

 Transportation Network

 Define Transportation Lane .

## Loading/Unloading

You define this duration in the scheduling settings of your planning profile. Open the Edit Scheduling Settings app

on the launchpad. For more information, see Loading and Unloading Durations.

## Coupling/Uncoupling

You define this duration in Customizing. For more information, see Customizing for Transportation Management

under  Master Data

## Resources

 Define Coupling/Uncoupling Duration .

Features

Constraints

## Fixed constraint

For fixed constraints, you define the exact start time of the rule.

  Example

This is custom documentation. For more information, please visit SAP Help Portal.

206


1/14/26, 2:19 PM

Example 1: You want to specify that a driver is not to work more than 10 hours per day. In Customizing, you first define

an activity group "Work". You define work as driving, coupling, and uncoupling. You therefore assign the activity types

"transport" and "coupling/uncoupling" to your activity group. If a transportation plan consists of more than 11 hours per

day, the system extends it to the next day by adding an additional duration to an activity or pushing it between activities.

Example 2: You want to specify that a driver may only spend a maximum of 8 hours behind the wheel. In this case, you

define an activity group "steering" in Customizing and assign the activity type "transportation". If the transportation

plan takes longer than 8 hours per day, the system extends it to the next day by adding an additional duration to an

activity or pushing it between activities.

## Rolling constraint

For rolling constraints, you do not define a start time of the rule. This means that the rule must be valid at any given time on

the time axis.

  Example

You specify that a truck may drive a maximum of 4 hours within 5 hours. However, you do not define when these 5 hours

begin. This rule must therefore be valid for any 5-hour segment on the time axis. If an activity takes longer, the system

also extends the transportation plan here.

  Note
The fulfillment of scheduling constraints does not necessarily lead to a connected break per rule.

For example, you have planned two freight units with two delivery locations. You have also defined a scheduling

constraint that allows a maximum travel time of eight hours within 24 hours. If there are opening hours that lead to a

wait time of one hour before delivery of the first goods, this hour can be reused as a break. Therefore, the trip from the

start location to the first delivery location is extended by one hour. In addition, a break of 15 hours is added on the return

trip from the second delivery location. This is sufficient to fulfill the constraint that requires a non-travel time of 16 hours

within 24 hours.

You can define multiple fixed and rolling constraints. The scheduled additional duration can be used to fulfill several constraints. If

there is idle time between activities, this time is also used to adhere to rest periods.

  Example

Example 1: You have defined two scheduling constraints:

Constraint 1: A maximum of four hours and 30 minutes of working time is permitted within five hours.

Constraint 2: A maximum of eight hours of working time is permitted within 24 hours.

This results in a transportation plan in which 30 more minutes are scheduled after four and a half hours of travel.

After another three and a half hours, an additional 15 hours and 30 minutes are scheduled.

Example 2: You have specified in Customizing that a truck may drive a maximum of eight hours per day. Now the system

is to schedule an activity with 10 hours. In this case, the system extends the transportation plan. This means it

schedules eight hours on the first day, shifts an additional activity duration for the rest of the day, and schedules the

remaining two hours on the following day.

Example 3: In Customizing, you have specified that only eight hours may be planned for activities per day. The system is

now to schedule two activities of a freight order, each of five hours. In this case, the system schedules the first activity

on the first day. It schedules the second activity with three hours on the first day, and it moves the remaining two hours

to the next day.

This is custom documentation. For more information, please visit SAP Help Portal.

207


1/14/26, 2:19 PM

You cannot tell in the system when exactly the additional duration was inserted. You can only see that the activities took

longer than the durations that you defined.

## Consideration of Context

The system considers the constraints for the scheduling per resource, not per freight order. Freight orders that are determined as

context (and are not explicitly included in the scheduling or VSR optimization run) as well as fixed freight orders are ignored in any

case during the determination of the new transportation plan.

  Example
The system schedules two freight orders for one truck, each with six hours, one after the other. You have specified in

Customizing that the truck may drive a maximum of eight hours per day. In this case, the system extends the second freight

order, that is, it adds an additional duration. If the first freight order was determined as context, however, the system does not

extend the second freight order.

## Considering Driving Time and Working Hours Constraints

Based on different sets of constraints (rules), rests are scheduled during planning.

To prevent accidents caused by driver fatigue, many countries have implemented official driving time and working hours

regulations for drivers. When using planning functions such as scheduling and vehicle scheduling and routing (VSR) optimization,

driving time regulations can have a significant impact on the planning process.

Driving time and working hours constraints are a set of planning constraints that allow modelling and consideration of a variety of

requirements related to driving time and working hours. These constraints enable the system to produce meaningful scheduling

and planning results that are beyond pure approximation.

For more information on modeling of regulations see Examples of Constraints.

## Prerequisites

You have defined profiles for driving time and working hours constraints (driving and working constraint profiles) in

Customizing.

For more information, see Customizing for Transportation Management under  Planning

 General Settings

## Define

Driving and Working Constraint Profile .

For more information about defining driving time and working hours constraints, see Definition of Driving Time and Working

Hours Constraints.

In the capacity availability settings of your planning profile, you have assigned your driving and working constraint profiles

to your vehicles (truck resources or vehicle types) and drivers.

To do so, you need to create entries for your vehicles on the Vehicle tab, or entries for your drivers on the Driver tab, or

both. You can indicate vehicles by specifying a means of transport, a vehicle group and type, or a resource. You can indicate

drivers by specifying a driver ID.

On the Activities (Local Staff) tab, you can optionally indicate locations at which certain activity groups are handled by the

local staff and are thus not considered by the driving time and working hours constraints.

The system evaluates and applies the entries in the capacity availability settings from top to bottom. Wildcards are allowed.

In the scheduling settings of your planning profile, you have indicated in the Consider Time Constraints field that driving

and working constraint profiles are to be considered. In your transportation cockpit session, you can overrule this setting in

This is custom documentation. For more information, please visit SAP Help Portal.

208


1/14/26, 2:19 PM

the Change Planning Settings dialog box.

Note that you need to select scheduling strategy Scheduling (Embedded) (VSS_EMBED) in the scheduling settings for the

system to consider driving time and working hours constraints during scheduling.

In Customizing, you have added the following fields if you want to display rests in the Gantt chart:

Total Driving Time

Total Working Time

Total Rest Time

Total Idle Time

## Total Unavailability

They are available for the truck list, the driver list and the road freight order list.

For more information, see Customizing for Transportation Management under  Basic Functions

  Gantt Chart

## Define

Field Lists and Label Schemes for Gantt Chart

.

You have optionally defined color settings for rest s in the Gantt Chart.

For more information, see Customizing for Transportation Management under  Basic Functions

  Gantt Chart

## Define

Color Schemes and Patterns for Gantt Chart

.

You have optionally defined label schemes for rest s in the Gantt Chart. You can also define tooltips as labels. The standard

tooltip for rests displays the duration only. However, you can configure it so that the rest type and the start and end time are

displayed as well.

For more information, see Customizing for Transportation Management under  Basic Functions

  Gantt Chart

## Define

Field Lists and Label Schemes for Gantt Chart

.

You can use user parameter /SCMTMS/SCH_FORCE to force automatic forward scheduling after data has been changed.

## Use

Driving time and working hours constraints are the rules that define when drivers need to take a rest, such as a lunch break or a

night's rest. You define them in Customizing as driving and working constraint profiles. In the capacity availability settings and the

scheduling settings of your planning profile, you enable planning to take these constraints into account. Scheduling and vehicle

scheduling and routing (VSR) optimization can then schedule rests in road freight orders based on these constraints. You can see

the duration of the scheduled rests in the corresponding lists and hierarchies of the transportation cockpit. They are also

graphically visualized in the Gantt chart.

You can define several sets of constraints, that is, driving and working constraint profiles, to consider different requirements, such

as requirements from different countries.

The system considers driving and working constraint profiles in the following way:

If you have assigned a multiresource or vehicle type to your road freight order, the system considers the driving and

working constraint profile assigned to this multiresource or vehicle type. It ignores all activities from other road freight

orders assigned to the same resource but assumes that the driver (vehicle) is well rested and the constraint calculation can

start afresh before the road freight order is executed.

If you have assigned a single resource to your road freight order, the system considers the driving and working constraint

profile assigned to this single resource. It also considers activities from other road freight orders assigned to the same

resource (within the planning horizon).

This is custom documentation. For more information, please visit SAP Help Portal.

209


1/14/26, 2:19 PM

If you have assigned a driver to your road freight order, the system considers the driving and working constraint profile that

belongs to this driver. The system ignores driving and working constraint profiles of an additional truck resource assigned

to the road freight order. It also considers activities from other road freight orders assigned to the same driver (within the

planning horizon).

A rest can only interrupt a travel activity. It can't interrupt other activities, such as loading, unloading, or preparing but can occur

between these activities at a stop. For example, a rest can occur between loading and coupling.

The system assumes that a driver (vehicle) is well rested at the beginning of the first road freight order in the planning horizon. No

explicit rest is planned before the first scheduled road freight order.

Whenever a road freight order overlaps with unavailability, the unavailability is filled with the largest rest available in the current

driving and working constraint profile. An unavailability can also be used to enforce a rest within a certain time slot.

Scheduling and VSR optimization consider other road freight orders that are planned on the same resources before and within the

planning horizon when determining rests.

If you want the system to consider other road freight orders that are planned on the same single resource before the planning

horizon when determining rests, you need to select the Consider Road Freight Orders Before Planning Horizon checkbox in your

scheduling settings.

If you want subsequent road freight orders assigned to the same truck resource within the planning horizon to be re-scheduled too

when you re-schedule a road freight order, you need to select the Reschedule Subsequent Documents checkbox in your

scheduling settings.

  Note

Considering driving time and working hours constraints leads to a longer duration of the road freight order due to the

included scheduled rests.

Driving and working constraint profiles are not taken into account during scheduling if you use scheduling strategy

Scheduling (Optimizer Server) (see Prerequisites).

VSR optimization doesn’t support the following functions:

## Rolling constraints

Accumulation constraints at the start of the week

## Drivers

VSR optimization only considers driving and working constraint profiles assigned to vehicle types or resources.

For vehicles with a default driver, the profile assigned to the default driver is used instead of the profile assigned

to the vehicle.

If a truck resource with an assigned default driver has a road freight order assigned which is not assigned to the

default driver, the truck resource is blocked for further use in optimization.

Driver teams aren’t supported.

When you use driving and working constraint profiles in scheduling, there is no guarantee, that scheduling finds a

solution if one exists.

## Display of Rests

The following times related to driving time and working hours are displayed in the road freight order list and hierarchy, in the truck

list, and in the driver list of the transportation cockpit:

This is custom documentation. For more information, please visit SAP Help Portal.

210


1/14/26, 2:19 PM

Total Driving Time

## Total Working Time

Total Rest Time (the quick view offers a list of individual rests )

Total Idle Time

Total Unavailability

  Note

For multiresources and equipment types, the total unavailability is displayed only.

Rests are displayed in the Gantt chart in the following way:

## Resource- and driver-based lists

In the Document view, only rests between documents are shown.

In the Activity view, all rests are shown.

## Document-based lists

In the Document view, no rests are shown.

In the Activity view, all rests inside the document are shown.

Rests are graphically visualized as rectangles in the Gantt chart.

  Note

If service activities, such as loading or coupling, are allowed during a rest, the "true" rest is visualized only. That means, no rest

is shown in parallel to the service activities because the driver is actually working and not resting. For more information, see

Definition of Driving Time and Working Hours Constraints.

## Definition of Driving Time and Working Hours Constraints

You define driving time and working hours constraints based on activity groups and rest types.

## Activity Groups

Activity groups are sets of activity types. Available activity types are traveling, loading, unloading, etc.

  Example

## Activity group Driving with activity type Travel

Activity group Work with activity types Travel, Pickup, Delivery, Couple, Uncouple, Prepare, Finalize, Prepare First

## Stop, Finalize Last Stop

Activity group Service with activity types Pickup, Delivery, Couple, Uncouple, Prepare, Finalize, Prepare First Stop,

Finalize Last Stop

## Rest Types

This is custom documentation. For more information, please visit SAP Help Portal.

211


1/14/26, 2:19 PM

Rest types describe a time period in which certain activities can’t be executed and are used to reset the limits of a constraint. By

default, a rest type doesn't allow any activities but you can overrule that by specifying an activity group to allow certain activities

during a rest.

  Example

In the EU, a daily rest lasts at least 11 hours.

In the EU, a break lasts at least 45 minutes, but can be split into at least 15 minutes followed by at least 30 minutes

break.

In the US, a driving break needs to last at least 30 minutes, but service activities, such as loading or coupling, are

allowed during the rest.

  Note

In your driving and working constraint profile, you can indicate that it’s possible to split a rest into two shorter rests, for

example, due to legal regulations. However, split rests are supported for constraint type Accumulation only.

## Constraint Types

A constraint can enforce rests during scheduling and therefore defines the rules for driving times and working hours. This will

increase the duration of a road freight order.

Constraint types determine how constraints are calculated. The following constraint types are available:

## Accumulation constraints

Accumulation constraints are used to model rules, where the sum of certain activities must not exceed a specific limit. The

constraint only sums up specific activity types (that are defined by an activity group) and hence the end point of the limit is

not a fixed point in time but depends on the scheduled activities. Formally, an accumulation constraint is defined by an

accumulation limit, a restricted activity group, an accumulated activity group, and a rest type. Given a specified limit

(capacity), the total duration of accumulated activity types (that are part of the activity group) must not exceed the limit. If

the limit is exceeded, a rest of the defined rest type is scheduled before continuing scheduling restricted activities.

The accumulation constraint can sum up a group of activities since a defined starting point, which is either after the last

rest or at the start of the week.

Vehicle scheduling and routing (VSR) optimization only supports constraints that start after the last rest.

  Example

After accumulating nine hours of driving since the last rest, all work is restricted until a night's rest of 11 hours is

taken.

After accumulating four and a half hours of driving since the last rest, all work is restricted until a 45-minute rest

is taken.

## Horizon constraints

Horizon constraints are used to model rules, where activities are only allowed within an interval of a fixed length (time

horizon). The constraint requires a rest after the time interval (limit) has passed. The horizon constraint always counts the

time that has elapsed since the last rest. Formally, a horizon constraint is defined by an interval limit, a restricted activity

group, and a rest type. Given a specified limit (time horizon), and a starting point of the interval, activities can only be

scheduled within the interval. If the interval boundaries are exceeded, a rest of the defined rest type is scheduled before

continuing scheduling restricted activities.

This is custom documentation. For more information, please visit SAP Help Portal.

212


1/14/26, 2:19 PM

  Example

14 hours after the last rest, a night's rest of 10 hours is required.

## Rolling constraints

Rolling constraints are used to model rules, where the sum of certain activities must not exceed a specified limit within any

arbitrary interval of a defined duration. The constraint ensures that in any possible interval within the planning horizon, the

accumulated (summed up) duration of a group of activities doesn’t exceed the defined limit. Optionally, a rest type can be

specified. If specified, a rest of this rest type can reset the constraint. Formally, a rolling constraint is defined by an

accumulation limit, a restricted activity group, an accumulated activity group, a rest type, and a rolling interval length.

This constraint type isn't supported by VSR optimization.

  Example

Within any interval of seven consecutive days, a maximum accumulated driving time of 60 hours is allowed. A rest of 34

hours or more can be planned to restart the consecutive day period.

  Note

If a certain constraint enforces a rest of a certain duration, the system uses this rest to fulfill all other constraints with rests of a

shorter duration.

For example, you have two accumulation constraints:

After accumulating nine hours, a night's rest of 11 hours is needed.

After accumulating four and a half hours, a 45-minute rest needed.

When the system plans the night’s rest of 11 hours, it also considers the 45-minute rest as planned without planning an

additional rest for it.

Several constraints are bundled in a driving and working constraint profile. For more information, see Customizing for

Transportation Management under  Planning

## General Settings

 Define Driving and Working Constraint Profile .

## Examples of Constraints

You can use driving time and working hours constraints to model requirements related to driving time and working hours.

## Examples: EU

In the following, examples that are relevant for the EU are described. Note that the solution provided in the system is

recommended for short planning horizons. Further, it contains continuous rest periods, which implies that the scheduled activities

and freight orders are valid with respect to the examples listed below.

EU 1 (Daily Rest): Within each period of 24 hours after the end of the previous daily rest period, a driver shall have taken a

new daily rest period of at least 11 hours. A rest is any uninterrupted period during which a driver may freely dispose of his

or her time.

EU 2 (9h Driving Time): The accumulated driving time between two rests of 11 hours shall not exceed 9 hours.

EU 3 (4.5h Driving Time): After a driving period of 4.5 hours, a driver shall take an uninterrupted break of minimum 45

minutes unless he takes a rest period. A break is any period during which a driver may not carry out any driving or any other

work and which is used exclusively for recuperation.

This is custom documentation. For more information, please visit SAP Help Portal.

213


1/14/26, 2:19 PM

Split breaks: The break may be replaced by a first break of at least 15 minutes followed by a second break of at least 30

minutes each distributed over the period in such a way as to comply with the provisions of the first paragraph.

EU 4 (6h Working Time): The driver needs to take a break of at least 30 minutes after maximum 6 hours working time (not

only driving time).

Note that waiting times that occur inside a freight order can be used for rest periods.

## Examples: US

In the following, examples that are relevant for the US are described. Note that the solution provided in the system is

recommended for short planning horizons. Further, it contains continuous rest periods, which implies that the scheduled activities

and freight orders are valid with respect to the examples listed below.

US 1 (Daily On-Duty Limit): A truck driver may not drive beyond the 14th consecutive hour after coming on duty, following

10 consecutive hours off duty. Off-duty time doesn't extend the 14-hour period.

US 2 (11h Driving Time): The accumulated driving time between two rests of 10 hours shall not exceed 11 hours.

US 3 (8h Driving Time): Drivers must take a 30-minute break when they have driven for a period of 8 cumulative hours

without at least a 30-minute interruption. The break may be satisfied by any non-driving period of 30 consecutive minutes

that is, on-duty not driving, off-duty, or any combination taken consecutively.

  Note

Breaks in this chapter are not related to the break calendar but to the rests that you can define in the driving and working

constraint profile.

## Frequently Asked Questions

The following is a list of frequently asked questions (FAQs) regarding driving time and working hours constraints.

Can I combine multiple accumulation, horizon, and rolling constraints?

Yes, any reasonable number of different constraint types can be combined. Note that a larger number of constraints

increases the complexity and may, hence, have an impact on the runtime.

Can I use driving time and working hours constraints to model EU and US regulations?

Yes, you can use driving time and working hours constraints to model official regulations. All constraints are considered as

hard constraints during scheduling (scheduling strategy Scheduling (Embedded) (VSS_EMBED)) and vehicle scheduling

and routing (VSR) optimization and therefore always lead to results that comply with the defined constraints. Since rests

are scheduled with minimal durations as defined in the rest types, results should be executable in reality.

What is the difference between driving time and working hours constraints and scheduling constraints?

Driving time and working hours constraints have two major advantages. They enable you to model more general

constraints, and the scheduled activities and freight orders require the rests to be continuous, which implies that they fulfill

the official regulations. Note that the costs of a solution with driving time and working hours constraints and costs of a

solution with similar scheduling constraints can't be directly compared. In particular, driving time and working hours

constraints are more restrictive, which may lead to a solution with increased costs.

What happens if I combine scheduling constraints and driving time and working hours constraints?

In this case, only driving time and working hours constraints are considered during scheduling (scheduling strategy

Scheduling (Embedded) (VSS_EMBED)) and VSR. Scheduling with this scheduling strategy doesn't support scheduling

This is custom documentation. For more information, please visit SAP Help Portal.

214


1/14/26, 2:19 PM

constraints.

Can I create different sets of rules for different types of vehicles?

Yes, this is possible by using different driving and working constraint profiles. In the capacity availability settings of your

planning profile, you can assign the profiles to your vehicle types and resources.

Are driving time and working hours constraints also supported by scheduling strategy Scheduling (Optimizer Server)

(VSS_DEF)?

Please use scheduling strategy Scheduling (Embedded) (VSS_EMBED). This scheduling strategy fully supports driving

time and working hours constraints. Scheduling strategy Scheduling (Optimizer Server) (VSS_DEF) doesn't support

driving time and working hours constraints.

Are rests and breaks in already planned road freight orders considered by driving time and working hours constraints

when subsequent tours, that is road freight orders, are planned?

Rests and breaks in already planned road freight orders are considered by driving time and working hours constraints if you

have activated context determination in the transportation cockpit settings.

Is it possible to exclude specific activities at certain stops such as loading and unloading from the working hours

calculation because they are done by local staff such as warehouse workers?

Yes, it is possible to define activities that are done by local staff per location. You can define them in the capacity availability

settings of your planning profile. These activity types aren't considered during driving time and working hours calculation.

There are no rests in the solution obtained by scheduling strategy Scheduling (Embedded) (VSS_EMBED). What could

be a possible cause?

First of all, check whether the obtained activity sequence is long enough to require rests. If this is the case, check in the

scheduling settings and the capacity availability settings whether driving time and working hours constraints have been

activated and relevant for your vehicle or driver. Further, you could check your driving and working constraint profile in

Customizing.

There are no rests in the solution obtained by VSR optimization. What could be a possible cause?

First of all, check whether the obtained activity sequence is long enough to require rests. If this is the case, check in the

explanation tool, whether driving time and working hours constraints have been activated. If this is the case, compare the

output of the optimizer displayed in the explanation tool with the solution displayed in the freight order overview. If they are

different, scheduling strategy Scheduling (Optimizer Server) (VSS_DEF) might have been called after the VSR

optimization run. This scheduling strategy doesn't support driving time and working hours constraints. We recommend to

use scheduling strategy Scheduling (Embedded) (VSS_EMBED) instead.

How can I analyze the impact of driving time and working hours constraints on scheduling?

You can use the Gantt chart to display the activities and rests of your road freight orders. If you want to analyze scheduling

(scheduling strategy Scheduling (Embedded) (VSS_EMBED)), you can use the Explain Scheduling Results app.

## Transportation Requirement Routing and Scheduling

Transportation requirement routing and scheduling (TRS) is a foundation module that supports various functions, such as route

determination, transportation duration determination, and scheduling of transportation requirements.

You can use TRS for the following:

Determination of Transportation Durations for BPS-Based Scheduling

This is custom documentation. For more information, please visit SAP Help Portal.

215


1/14/26, 2:19 PM

Routing for a given request from source to destination location is performed based on master data, such as transportation

lanes and default routes. In Transportation Management (TM), durations are determined based on the routing results.

In order-based sales order scheduling, you can use this function to determine the durations of load, travel, and unload

activities. Based on these durations, scheduling is then performed in Business Process Scheduling (BPS). For more

information, see Integration of Sales Order Scheduling.

## Routing and Scheduling of Transportation Requirements

Routing for a given request from source to destination location is performed based on master data, such as transportation

lanes and default routes. Based on the routing results and a reference date, forward or backward scheduling is performed.

In order-based sales order scheduling, you can use this function to delegate scheduling of load, travel, and unload activities

to TM using BPS. For more information, see Integration of Sales Order Scheduling.

You can use the TRS test cockpit to simulate TRS. For more information, see Test Cockpit for Transportation Requirement Routing

and Scheduling.

Determination of Transportation Durations for BPS-Based
## Scheduling

Transportation requirement routing and scheduling (TRS) enables you to determine the transportation durations of your

requirements in an order-based scheduling scenario. Based on this information, scheduling is performed in Business Process

Scheduling (BPS), a flexible configurable scheduling solution in advanced Available-to-Promise (aATP).

## Prerequisites

You have defined a transportation duration determination profile. In this profile, you can indicate one or several routing

methods and the sequence in which the system is to perform them. You can also indicate a planning profile if you want to

use the fixed loading durations and durations for prepare and finalize that you have defined there. To create a profile, open

the Create Transportation Duration Determination Profile app from the launchpad.

  Note

If the system determines durations using one routing method, these durations are not changed by any

subsequent routing method that you indicated.

Note that the system uses the default means of transport for determining the loading duration.

If you want to use this function for order-based sales order scheduling, you have set up the integration of sales order

scheduling. For more information, see Integration of Sales Order Scheduling.

## Use

In TRS, travel durations as well as loading and unloading durations are determined based on the routing methods that you selected

in your transportation duration determination profile. For more information, see Routing Methods.

For the determination, the scheduling settings of the assigned planning profile are used.

Note that the system uses the default means of transport as the basis for the determination.

## Activities

This is custom documentation. For more information, please visit SAP Help Portal.

216


1/14/26, 2:19 PM

When you create a sales order in Sales and Distribution (SD), scheduling takes place automatically in BPS based on your settings

when you enter a material and press ENTER. Based on the transportation durations determined in TRS, BPS calculates the

delivery date. For more information about sales order scheduling based on TM durations, see Integration of Sales Order

Scheduling.

You can simulate this function in the TRS test cockpit. For more information, see Test Cockpit for Transportation Requirement

Routing and Scheduling.

## Related Information

Business Process Scheduling (BPS)

## Routing and Scheduling of Transportation Requirements

For a given request from a source to a destination location and a reference date, routing and scheduling are performed.

## Prerequisites

You have created a requirement routing profile. To do so, open the Create Requirement Routing Profile app from the

launchpad. You have specified the following:

## Planning profile

Routing methods (see Routing Methods)

If you want to use this function for order-based sales order scheduling, you have set up the integration of sales order

scheduling. For more information, see Integration of Sales Order Scheduling.

## Use

Routing tries to determine a possible route from a source to a destination location for a transportation requirement. Scheduling

determines dates and times for loading, traveling, and unloading. Scheduling considers a reference date as requested delivery date

in backward scheduling or as requested loading date in forward scheduling.

The system determines loading and unloading durations based on the scheduling settings of the assigned planning profile. The

system uses the default means of transport as the basis for the determination.

Optionally, scheduling can try to find the next possible schedule departure for stages that have been assigned to a schedule during

routing.

  Note

Embedded scheduling (VSS_EMBED) is supported only.

## Activities

When you create a sales order in Sales and Distribution (SD), scheduling takes place automatically in Transportation Management

(TM) based on your settings when you enter a material and press ENTER. For more information about sales order scheduling

based on TM scheduling, see Integration of Sales Order Scheduling

You can simulate this function in the TRS test cockpit. For more information, see Test Cockpit for Transportation Requirement

Routing and Scheduling.

This is custom documentation. For more information, please visit SAP Help Portal.

217


1/14/26, 2:19 PM

## Routing Methods

Routing methods can be used in transportation requirement routing and scheduling (TRS) processes to determine routing for

requests from a source location to a destination location.

In the transportation duration determination profile and the requirement routing profile, you can define a sequence of multiple

routing methods. The system processes the methods one after the other. If a method determines a result, this result is not

changed anymore by the succeeding methods.

The following methods are available:

Default route determination (see Default Route)

The system searches for default routes. If it finds any, it copies the routing information and the travel durations into the

result. If it finds a default route without a duration in any of the stages, subsequent routing methods can determine the

duration for these stages.

Lane, distance, and duration determination (LDDD) (see Lane, Distance, and Duration Determination (LDDD))

The system searches for durations using the lane, distance and duration determination. Note that the standard

configuration of LDDD first checks transportation lanes and then uses straight-line determination as fallback.

## Straight-line determination

The system determines straight-line distances and durations based on the speed of the default means of transport.

## Network path determination

The system tries to determine a path from source to destination location based on the transportation network.

To do so, it determines transshipment locations as well as schedules taking into account parameters that you have

indicated in the requirement routing profile, such as the search depth for these locations or schedules.

You can indicate whether the system tries to determine the path with the shortest duration or distance.

  Note

If you indicated that the path with the shortest duration is to be determined, the system adds an expected

waiting time until the next possible schedule departure for a schedule.

The system doesn't evaluate default routes.

The system doesn't evaluate the capacity of schedules.

You can simulate network path determination using the test cockpit for network path determination. For more

information, see Test Cockpit for Network Path Determination.

In the following section, you find various examples of how these routing methods are applied.

Let's assume you have indicated in your TRS profile that the following three routing methods are to be executed in the following

sequence:

Default route determination

## Network path determination

Lane, distance and duration determination

Example 1:

This is custom documentation. For more information, please visit SAP Help Portal.

218


1/14/26, 2:19 PM

There is a requirement from A to C1.

There is a default route from A via B to C1, in which the stage from A to B has a duration of one 1 day and the stage from B to C1 has

a duration of one hour.

The system determines the default route and neither changes the routing during network path determination nor the durations

during lane, distance and duration determination anymore.

Example 2:

There is a requirement from A to C2.

There is a default route from A via B to a zone that includes C2, in which the stage from A to B has a duration of one day and the

stage from B to the zone has no duration defined (that means, the duration is set to zero).

The system determines the default route and doesn't change the routing during network path determination anymore but adds a

duration for the stage from B to C2 during lane, distance and duration determination since the duration was still missing.

Example 3:

There is a requirement from A to C3.

There is no default route. There is no direct lane between A and C3 but B is a transhipment location between both and there are

lanes from A to B and B to C.

The system doesn't determine a default route. Therefore, network path determination determines the possible path from A to C3

via B and already determines the durations. Lane, distance and duration determination doesn't need to add a duration.

Example 4:

There is a requirement from A to C4.

There is neither a default route nor a network connection between the locations.

The system neither determines a default route nor a network path. However, during lane, distance and duration determination,

after an unsuccessful search for a lane, the system adds a distance and a duration based on the straight-line determination

(fallback).

Test Cockpit for Transportation Requirement Routing and
## Scheduling

The test cockpit for transportation requirement routing and scheduling (TRS test cockpit) allows you to simulate either

transportation duration determination or requirement routing and scheduling. You can then analyze the result.

## Prerequisites

For more information, see Determination of Transportation Durations for BPS-Based Scheduling and Routing and Scheduling of

Transportation Requirements.

Features

## Input

This is custom documentation. For more information, please visit SAP Help Portal.

219


1/14/26, 2:19 PM

On the initial screen, you first need to select a TRS process category to indicate whether the system is to simulate transportation

duration determination or requirement routing and scheduling.

Based on the TRS process category, you can indicate the following:

## TRS profile

## Scheduling direction

Whether the system is allowed to parallelize

Whether intermediate results are to be displayed as well

Time zone in which all dates/times of the result are to be displayed

## Unit of measure for distances

Further, you can indicate up to three request items which are defined by the following:

A document ID (optional)

The document ID is used to group request items. It doesn't have any reference to business documents.

The source and destination location

## A reference date and time

A time zone, which is applied to the reference date and time

## Output

The result screen contains the following areas:

## General Input

In this area, you find the input data that you entered on the initial screen. You can change this information.

## Item Input

In this area, you can change your input. For example, you can change the source location of one request item or change the

number of request items to be considered.

## Model Assignment

The system assigns each request item to an entity called "model". Each item needs to be assigned to a model but a model

can have several items assigned to it. In this area, you should be able to find each of your items in one of the models.

## Result Overview

In this area, you find an overview of the result per model. If you have selected the Show Intermediate Results checkbox, the

system displays the intermediate result for a routing method after the system executed this method. By selecting Show

Details, you can display details for each model in the Result Details area. By selecting Show Network Path Determination,

you can switch to the test cockpit for network path determination. For more information, see Test Cockpit for Network Path

Determination.

## Result Details

In this area, you can display details for each model.

If you have selected Transportation Duration Determination as the TRS process category, you can see loading durations or

stages that the system added, for example.

This is custom documentation. For more information, please visit SAP Help Portal.

220


1/14/26, 2:19 PM

If you have selected Requirement Routing and Scheduling as the TRS process category, you can see the following

information, for example:

Loading start date/time

Loading end date/time

Departure date/time

Arrival date/time

Means of transport

## Messages

In this area, you find execution information.

## Activities

To start the TRS test cockpit (program /SCMTMS/TEST_TRS_ENGINE), on the SAP Easy Access screen choose  Transportation

Management

## Administration

 Transportation Requirement Routing and Scheduling

 TRS - Test Cockpit

.

## Test Cockpit for Network Path Determination

The test cockpit for network path determination allows you to simulate the determination of network paths. You can then analyze

the result.

## Prerequisites

If you want the system to consider transshipment locations, you have defined transshipment location assignments. To do so, on

the SAP Easy Access screen, choose  Logistics

 Transportation Management

## Master Data

 Transportation Network

## Location

 Define Transshipment Location Assignments .

For more information about other prerequisites, see Determination of Transportation Durations for BPS-Based Scheduling and

Routing and Scheduling of Transportation Requirements.

Features

## Input

On the initial screen, you can indicate the following information:

## Routing option

Search depth for transshipment locations

Search depth for schedules

## Expected waiting time of schedule

Alternatively, you can select a transportation requirement routing and scheduling (TRS) profile. By doing so, the above fields are

filled automatically as defined in the selected profile.

For more information, see Routing Methods and the system documentation.

This is custom documentation. For more information, please visit SAP Help Portal.

221


1/14/26, 2:19 PM

Further, you can indicate up to three path requests which are defined by the following:

The source and destination location

A reference date and time

A time zone

## Output

The result screen contains the following areas:

## General Settings

In this area, you find the input data that you entered on the initial screen. You can change this information.

## Path Requests

In this area, you can change your input. For example, you can change the source location of one path request or change the

number of requests to be considered.

## Locations

In this area, the system displays all locations from your network that are relevant for your requests. This network includes

both the source and destination locations from your requests and the transshipment locations that connect these source

locations with the destination locations.

## Connections

In this area, the system displays all transportation lanes and schedules that are available for the connections between

these locations. In addition, two buttons are available to display a detailed calculation of the expected waiting time for

schedule connections and to convert durations from hours to seconds and vice versa.

## Path Results

In this area, the system displays results for each path request. Each path request can consist of multiple connections.

Depending on your routing option, the result can either be the path with the shortest distance or the path with the shortest

duration.

## Activities

To start the test cockpit (program /SCMTMS/TEST_NPD_ENGINE), on the SAP Easy Access screen choose  Transportation

Management

## Administration

 Transportation Requirement Routing and Scheduling

 Test Cockpit for Network Path

Determination .

Effects of Date/Time Deviations During Execution

## Use

You can check the effects that deviations in dates/times during the execution of freight orders have on the rest of your planning.

Deviations in dates/times can occur if a delay is reported.

## Features

If a freight order cannot be executed as planned, for example, because the truck left late, you can adjust your planning. You do this

by performing forward scheduling. The system reschedules the freight order.

This is custom documentation. For more information, please visit SAP Help Portal.

222


1/14/26, 2:19 PM

Scheduling only takes place for the resource that is assigned to the freight order. If there are dependencies to other resources or

freight orders, this can lead to conflicts, for example, for multimodal transports. You must solve this conflict manually or using VSR

optimization. We recommend solving conflicts manually. If you use VSR optimization, you must make sure that all objects are in

the planning horizon.

## Activities

You can start scheduling on the following user interfaces:

## Transportation cockpit

We recommend scheduling from the transportation cockpit if the system is to consider not only the late freight order but

also all of the other freight orders at the resource during scheduling. To start scheduling, open the Transportation Cockpit

app on the launchpad.

## User interface for changing freight orders

We recommend scheduling from this user interface if you only want to schedule late freight orders. To start scheduling,

open the Edit Road Freight Order or Edit Rail Freight Order app on the launchpad.

## Freight order overview

To start scheduling, open the Freight Orders app on the launchpad.

Loading and Unloading Durations

## Use

Loading and unloading (stop) times are calculated by the system during manual planning and during VSR optimization based on

the rule-set specified in the Create Scheduling Settings app. The app also gives you the ability to export the rule-set to a

spreadsheet so that you can share it with someone who does not use the app. This feature lets you use a spreadsheet application

to analyze or modify the rule-set. You can then import the data modified in the spreadsheet application back to the app. This can

be used as an alternative to modifying the data directly in the app.

## Features

The rule-set lets you specify the following:

A fixed duration for loading and unloading activities at a location

A variable duration (time per unit) for loading and unloading activities at a location

The duration required for preparing and finalizing a location. This duration can be used to account for activities such as

completing paperwork and driving through the depot.

## Operating times and handling resources for loading and unloading

Note that these values overwrite operating times and handling resources that you have defined in master data.

Operating times for loading and unloading based on requirement document attributes, such as dangerous goods

The fields for entering the details are categorized by the direction of travel (inbound and outbound):

## Outbound tab

Use the tab to enter details for loading durations, the duration for finalizing stops, and preparing the first stop.

This is custom documentation. For more information, please visit SAP Help Portal.

223


1/14/26, 2:19 PM

## Inbound tab

Use the tab to enter details for unloading durations, the duration for preparing stops, and finalizing the last stop.

The figure below shows how stops and activities are categorized.

  Note

For schedule-based freight orders and freight bookings, scheduling does not consider loading and unloading durations.

If you specify multiple rules, the system uses the first rule that matches the location and resource.

The loading and unloading durations are calculated by a fixed duration that is applied once per capacity document stop,

plus the variable durations per requirement document stop. The overall duration is applied to both the capacity

document and the requirement document stops.

## Activities

To specify a rule-set, on the Launchpad, open the Create Scheduling Settings app.

To export the rule-set to a spreadsheet, click Download. Then you can analyze and modify the rule-set in the spreadsheet

application and import the file back to the app by clicking Upload.

Time Windows

## Use

You use time windows to control when goods are to be picked up and delivered. VSR optimization (see VSR Optimization) then

schedules the pickup or delivery exactly in the time window that you have defined.

You can also control how the system is to deal with cases in which these time windows are not taken into account during VSR

optimization, that is, whether VSR optimization is to calculate penalty costs. You can model the following cases:

The goods are picked up too early or too late.

The goods are delivered too early or too late.

## Features

You create time windows by defining tolerances within which a premature or delayed pickup or delivery is to be allowed. For each

tolerance, you specify whether VSR optimization is to consider the tolerance as a hard, soft, or hard and soft constraint (see

Constraints for VSR Optimization). In this way, you control whether VSR optimization calculates penalty costs when the

constraints are not adhered to.

You can define the following tolerances:

This is custom documentation. For more information, please visit SAP Help Portal.

224


1/14/26, 2:19 PM

Maximum earliness

## Maximum delay

Delay without penalty costs

## Earliness without penalty costs

The dates and times that you have defined for the pickup and delivery in the business document, for example, the forwarding

order, form the basis for calculating the tolerances. For more information, see Definition of Delivery Windows.

You can also specify that the system is to take into account the exact time for the pick-up date or delivery date. The system always

uses the current point in time and rounds up or down to full days.

For more information about the link between tolerances and constraints, see Delivery Window.

  Note

The system also takes into account windows for pickup and delivery in manual planning (see Manual Planning).

However, this applies to hard constraints only. If it cannot adhere to the tolerances, it simply issues a warning message.

The system already takes time windows into account when creating freight units and determines the dates of the freight

units. It does not evaluate the time windows further when you access planning.

The system takes into account a factory calendar of a calendar resource assigned to a location when creating freight

units.

## Activities

You define your time windows by entering a rule for windows for pickup and delivery in the freight unit type or a condition

(condition type /SCMTMS/TOR_TIMEWIND). For more information, see Customizing for Transportation Management under

Planning

## Freight Unit

 Define Freight Unit Type .

For more information about defining conditions for time windows, see Definition of a Condition for Time Windows.

## Delivery Window

You have defined the following tolerances:

Delta premature = 2 days (tolerance for premature delivery without penalty costs)

Delta earliest = 3 days (tolerance for maximum earliness)

Delta delayed = 1 day (tolerance for delayed delivery without penalty costs)

Delta latest = 2 days (tolerance for maximum delay)

The requested delivery date/time (from date/time) is 10.01., 12:00. The solid red curve in the following figures specifies that you

do not want to take into account the exact time of the delivery date. The dotted blue curve specifies that you want to take into

account the exact time.

The following figures show how these tolerances affect the delivery date, depending on whether you define them as hard, soft, or

hard and soft constraints.

This is custom documentation. For more information, please visit SAP Help Portal.

225


1/14/26, 2:19 PM

## Soft Constraints for Premature and Delayed Delivery

In this case, a delayed delivery is allowed until 12.01. (solid red curve). Since the system is not to take into account the exact time

for the delivery date, it rounds up to the full day, in other words, from 11.01., 12:00 to 12.01., midnight. No penalty costs are

calculated. A delivery after 12.01. is allowed, but penalty costs are incurred.

A premature delivery can occur at the earliest on 08.01. without penalty costs being incurred. If the delivery occurs before 08.01.,

penalty costs are incurred. Since the system is not to take into account the exact time for the delivery date, it rounds down to the

full day, in other words, from 08.01., 12:00 to 08.01., midnight.

If you have specified that the system is to take into account the exact time of the delivery date (dotted blue curve), penalty costs

are incurred for a delayed delivery after 11.01., 12:00 and for a premature delivery before 08.01., 12:00.

## Hard Constraints for Premature and Delayed Delivery

In this case, a delayed delivery is not allowed after 13.01. (solid red curve). The delivery can occur at the earliest on 07.01. Since the

system is not to take into account the exact time for the delivery date, it rounds up or down to the full day, in other words, from

12.01., 12:00 to 13.01., midnight and from 07.01., 12:00 to 07.01., midnight.

If you have specified that the system is to take into account the exact time of the delivery date (dotted blue curve), a delivery is not

allowed after 12.01., 12:00 and before 07.01., 12:00.

This is custom documentation. For more information, please visit SAP Help Portal.

226


1/14/26, 2:19 PM

## Hard and Soft Constraints for Premature and Delayed Delivery

In this case, a delayed delivery is allowed after 10.01. (solid red curve). Since the system is not to take into account the exact time

for the delivery date, it rounds up to the full day, in other words, from 11.01., 12:00 to 12.01., midnight. However, penalty costs are

incurred if the delivery occurs on 12.01. A delivery after 13.01. is not allowed.

A premature delivery is allowed from 07.01. Since the system is not to take into account the exact time for the delivery date, it

rounds down to the full day, in other words, from 08.01., 12:00 to 08.01., midnight. However, penalty costs are incurred if the

delivery occurs on 07.01. A delivery before 07.01. is not allowed.

If you have specified that the system is to take into account the exact time of the delivery date (dotted blue curve), a delayed

delivery is not allowed after 12.01., 12:00. Penalty costs are incurred for a delivery between 11.01., 12:00 and 12.01., 12:00.

A premature delivery before 07.01., 12:00 is not allowed. Penalty costs are incurred for a delivery between 07.01., 12:00 and 08.01.,

12:00.

## Definition of Delivery Windows

The following examples show the options that you have when defining time windows. First of all, the relevant settings that you

make are shown. A figure is then used to show how the system interprets your entries. The examples all refer to the delivery.

However, they also apply in the same way to the pickup.

Example 1

In the forwarding order, you have defined the following date/time for the delivery at the destination location:

Earliest delivery (acceptable dates/times)

N/A

Delivery date/time (from) (requested dates/times)

17.09.07 00:00:00

Delivery date/time (to) (requested dates/times)

N/A

Latest delivery (acceptable dates/times)

N/A

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

227


1/14/26, 2:19 PM

You define dates/times for delivery on the user interface for defining the forwarding order (Locations and Dates tab).

You have also defined the following tolerances:

Tolerance for early delivery

24:00 hrs

Tolerance for earliest delivery

48:00 hrs

Tolerance for late delivery

24:00 hrs

Tolerance for latest delivery

48:00 hrs

  Note

You define penalty costs for earliness and lateness in the costs settings for the planning profile either directly or by entering a

condition (condition type /SCMTMS/FU_PNLT_COST).

The following figure shows how the system takes these values into account and what the time window looks like:

Time Window (Example 1)

In this case, the system takes into account all tolerances. A delayed delivery up until 18.09 does not incur any costs. Penalty costs

are incurred between 18.09 and 19.09. A delivery is not permitted as of 19.09. A premature delivery can occur at the earliest on

16.09. without penalty costs being incurred. If the delivery occurs between 15.09 and 16.09, penalty costs are incurred. A delivery is

not permitted before 15.09.

Example 2

In the forwarding order, you have defined the following dates/times for the delivery:

Earliest delivery (acceptable dates/times)

N/A

Delivery date/time (from) (requested dates/times)

17.09.07 00:00:00

This is custom documentation. For more information, please visit SAP Help Portal.

228


1/14/26, 2:19 PM

Delivery date/time (to) (requested dates/times)

17.09.07 00:00:00

Latest delivery (acceptable dates/times)

N/A

You have also defined the following tolerances:

Tolerance for early delivery

24:00 hrs

Tolerance for earliest delivery

48:00 hrs

Tolerance for late delivery

24:00 hrs

Tolerance for latest delivery

48:00 hrs

The following figure shows how the system takes these values into account and what the time window looks like:

Time Window (Example 2)

In this case, the system does not take into account the tolerances for early and late delivery, since it takes into account the

dates/times that you have defined in the forwarding order. A delayed delivery is possible until 19.09, but penalty costs are incurred.

A delivery is not permitted as of 19.09. A premature delivery can occur at the earliest on 15.09. If the delivery occurs between 15.09

and 17.09, penalty costs are incurred. A delivery is not permitted before 15.09.

Example 3

In the forwarding order, you have defined the following dates/times for the delivery:

Earliest delivery (acceptable dates/times)

N/A

Delivery date/time (from) (requested dates/times)

16.09.07 00:00:00

Delivery date/time (to) (requested dates/times)

18.09.07 00:00:00

Latest delivery (acceptable dates/times)

N/A

This is custom documentation. For more information, please visit SAP Help Portal.

229


1/14/26, 2:19 PM

You have also defined the following tolerances:

Tolerance for early delivery

24:00 hrs

Tolerance for earliest delivery

48:00 hrs

Tolerance for late delivery

24:00 hrs

Tolerance for latest delivery

48:00 hrs

The following figure shows how the system takes these values into account and what the time window looks like:

Time Window (Example 3)

In this case, the system only takes into account the tolerances for early and late delivery. A delayed delivery up until 18.09 does not

incur any costs. Penalty costs are incurred between 18.09 and 20.09. A delivery is not permitted as of 20.09. A premature delivery

can occur at the earliest on 16.09. without penalty costs being incurred. If the delivery occurs between 14.09 and 16.09, penalty

costs are incurred. A delivery is not permitted before 14.09.

Example 4

In the forwarding order, you have defined the following dates/times for the delivery:

Earliest delivery (acceptable dates/times)

15.09.07 00:00:00

Delivery date/time (from) (requested dates/times)

16.09.07 00:00:00

Delivery date/time (to) (requested dates/times)

18.09.07 00:00:00

Latest delivery (acceptable dates/times)

19.09.07 00:00:00

You have also defined the following tolerances:

Tolerance for early delivery

24:00 hrs

This is custom documentation. For more information, please visit SAP Help Portal.

230


1/14/26, 2:19 PM

Tolerance for earliest delivery

48:00 hrs

Tolerance for late delivery

24:00 hrs

Tolerance for latest delivery

48:00 hrs

The following figure shows how the system takes these values into account and what the time window looks like:

Time Window (Example 4)

In this case, the system does not take any of the tolerances into account, since it takes into account the dates/times that you have

defined in the forwarding order. A delayed delivery up until 18.09 does not incur any costs. Penalty costs are incurred between

18.09 and 19.09. A delivery is not permitted as of 19.09. A premature delivery can occur at the earliest on 16.09. without penalty

costs being incurred. If the delivery occurs between 15.09 and 16.09, penalty costs are incurred. A delivery is not permitted before

15.09.

Example 5

In the forwarding order, you have defined the following dates/times for the delivery:

Earliest delivery (acceptable dates/times)

N/A

Delivery date/time (from) (requested dates/times)

16.09.07 00:00:00

Delivery date/time (to) (requested dates/times)

18.09.07 00:00:00

Latest delivery (acceptable dates/times)

N/A

In this case, you have not defined any tolerances.

The following figure shows how the system takes these values into account and what the time window looks like:

This is custom documentation. For more information, please visit SAP Help Portal.

231


1/14/26, 2:19 PM

Time Window (Example 5)

Penalty costs are incurred for a delayed delivery as of 18.09. Penalty costs are not incurred for a delayed delivery between 17.09

and 18.09. Penalty costs are incurred for a premature delivery before 16.09. Penalty costs are not incurred for a premature delivery

between 16.09 and 17.09.

Example 6

In the forwarding order, you have defined the following dates/times for the delivery:

Earliest delivery (acceptable dates/times)

16.09.07 00:00:00

Delivery date/time (from) (requested dates/times) N/A

Delivery date/time (to) (requested dates/times)

N/A

Latest delivery (acceptable dates/times)

18.09.07 00:00:00

You have also defined the following tolerances:

Tolerance for early delivery

24:00 hrs

Tolerance for earliest delivery

48:00 hrs

Tolerance for late delivery

24:00 hrs

Tolerance for latest delivery

48:00 hrs

The following figure shows how the system takes these values into account and what the time window looks like:

This is custom documentation. For more information, please visit SAP Help Portal.

232


1/14/26, 2:19 PM

Time Window (Example 6)

In this case, the system does not take any of the tolerances into account. Penalty costs are not incurred for a delayed delivery

between 17.09 and 18.09. A delivery is not permitted after that. Penalty costs are not incurred for a premature delivery between

16.09 and 17.09. A delivery is not permitted before that.

Example 7

In this example, the system interprets the dates/times from the forwarding order as hard constraints without you having to define

hard constraints. In the forwarding order, you have defined the following dates/times for the delivery:

Earliest delivery (acceptable dates/times)

N/A

Delivery date/time (from) (requested dates/times)

16.09.07 00:00:00

Delivery date/time (to) (requested dates/times)

18.09.07 00:00:00

Latest delivery (acceptable dates/times)

N/A

You have also defined the following tolerances:

Tolerance for early delivery

N/A

Tolerance for earliest delivery 00:00 hrs

Tolerance for late delivery

N/A

Tolerance for latest delivery

00:00 hrs

The following figure shows how the system takes these values into account and what the time window looks like:

This is custom documentation. For more information, please visit SAP Help Portal.

233


1/14/26, 2:19 PM

Time Window (Example 7)

In this case, the system only takes into account the tolerances for earliest and latest delivery. Penalty costs are not incurred for a

delayed delivery between 17.09 and 18.09. A delivery is not permitted after that. Penalty costs are not incurred for a premature

delivery between 16.09 and 17.09. A delivery is not permitted before that.

## Definition of a Condition for Time Windows

This example shows how you define a condition for a time window depending on the freight unit type.

In this case, you define a condition with the condition type /SCMTMS/TOR_TIMEWIND based on a decision table.

As the data access definition, enter /SCMTMS/TOR_TYPE (business document type of freight order management).

Depending on the freight unit type, you specify in the decision table which durations and rounding rules the system is to use when

calculating the times for the time window.

## Earliness and Lateness

In the Earliness and Lateness fields, you specify whether the system is to treat an earliness or lateness as a constraint and, if yes,

as which sort of constraint:

As a soft constraint

As a hard constraint

## As a soft and hard constraint

If you have entered Soft Constraint or Soft and Hard Constraint, in the Prem. Stay (premature stay) field and the Del. Stay

(delayed stay) field, enter the required time period in the format HH:MM.

If you entered hard constraint or soft and hard constraint, in the EarlstStay (earliest stay) field and the Lat. Stay (latest stay)

field, enter the required offset in the format HH:MM.

This is custom documentation. For more information, please visit SAP Help Portal.

234


1/14/26, 2:19 PM
## Round

In addition, you can specify whether and how you want the system to round (to complete days, for example).

## Operating Times

You can also specify whether you want the system to consider the operating times of a location. As a prerequisite, you must have

defined a calendar resource with operating times in the master data and assigned this to the location.

Note that VSR optimization (VSR = vehicle scheduling and routing) only takes the operating times into account if you have defined

loading and unloading durations that are greater than zero.

## Delivery and Pickup

You can enter different values for the delivery and the pickup. To do so, enter a second data access definition

/SCMTMS/TOR_STOP_CAT.

In the decision table, specify the following values for pickup:

Stop Type

Earliness

## Lateness

EarlstStay (earliest

Round

stay)

O (pickup)

2 (hard constraint)

0 (no consideration as

0

## True

constraint)

This means that the pickup may not take place earlier than agreed. A late pickup is acceptable. The system is to round the pickup

date to complete days.

You specify the following values for the delivery:

Stop Type

Earliness

## Lateness

Lat. Stay (latest stay)

## Round

I (delivery)

0 (no consideration as

2 (hard constraint)

0

## False

constraint)

This means that the delivery may not take place later than agreed. An early delivery is acceptable.

Since the time of the delivery date defined by the customer is to be adhered to, specify that the system is not to round it to full

days.

## Calculation Base

You can specify how loading and unloading activities are to be scheduled in terms of the pick-up/delivery windows of the freight

unit or transportation unit, that is, whether the activities must start or end in the time window.

The following values are possible:

Start of (Un-)Loading Activity

## End of (Un-)Loading Activity

Default (this is the start of the loading activity for outbound scenarios and the end of the unloading activity for inbound

scenarios)

This is custom documentation. For more information, please visit SAP Help Portal.

235


1/14/26, 2:19 PM

## Explanation Tool for Scheduling

With this app, you can analyze your scheduling results to better understand how the system has scheduled your objects.

## Prerequisites

You have the authorization to work with the explanation tool (authorization object T_EXP_USR).

You have set user parameter /SCMTMS/EXP to X to allow the logging of scheduling data.

The explanation tool for scheduling uses a Gantt chart for visualization. The system uses the colors defined in the default

layout for the Gantt chart. If you want to use other colors that are defined in another layout, you need to select the VSS

Expl Tool Layout checkbox for this other layout. For more information, see Customizing for Transportation Management

under  Basic Functions

## Gantt Chart

 Define Layouts for Gantt Chart

.

For more information about prerequisites for scheduling, see Scheduling.

## Features

## Overview Page

On this page, all explanation logs are displayed in a table with basic information, such as the following:

Planning profile

Scheduling settings

Planning horizon

Scheduling direction

## Scheduling strategy

Scheduling status, that is, whether the scheduling run was successful or not

## Action that called scheduling, for example freight unit building

You can filter the content using different search criteria such as the planning profile and search for a specific explanation log. You

can also directly navigate to a planning profile or specific scheduling settings.

By selecting an explanation log for a successful scheduling run, you can navigate to the detail page.

## Detail Page

On this page, detailed scheduling results are displayed both in a table view on the left side and a Gantt chart on the right side.

You can do the following:

## Iterate through the individual solution steps

For example, you can display the results after the system has scheduled the activities as early as possible or you can

display the final results.

## Switch between activity groups to check the results per activity

An activity group is a chain of activities that need to be scheduled and do not have a relationship with any other activity

outside of this chain. For each activity group, the system performs scheduling separately. You can iterate through the

This is custom documentation. For more information, please visit SAP Help Portal.

236


1/14/26, 2:19 PM

solution steps for each activity group.

Switch between different views:

## Activity

Truck resource or truck type

## Handling resource

Display different solution steps for different views

Visualize relationships between activities in the Gantt chart

Visualize constraints such as downtimes and non-working times in the Gantt chart

Display the current start and end time of each activity as well as the allowed time period in which the activity can be

scheduled

## Activities

To analyze scheduling results, open the Explain Scheduling Results app from the launchpad.

## Related Information

Gantt Chart for Transportation Planning

## Additional Planning Options

Planning offers various other planning options. For example, you can assign drivers to your freight orders or you can use package

units, trailers, or multi-resources.

## Planning Based on Equipment Types

If you regularly subcontract your transportation demands, you are usually not interested in physical resources, such as the actual

truck with a plate number on your yard, but rather in resource types, which you can order from your carriers.

For such scenarios, we recommend that you define equipment types. That means, you don't need to define and assign resources

anymore. You just need to specify or assign equipment types. The system treats equipment types similarly to unlimited

multiresources.

## Prerequisites

You have defined equipment types (that is, vehicle types and container types) in Customizing under  Master Data

## Resources

## General Settings

 Define Equipment Groups and Equipment Types

For more information, see Equipment Groups and Equipment Types.

  Note

For these vehicle types and container types, you must not select the Restricted Use in Planning checkbox.

Optionally, you can use Business Add-In (BAdI) /SCMTMS/FU_STAGE_MODIFY to determine the preferred equipment type

and group for freight unit stages.

This is custom documentation. For more information, please visit SAP Help Portal.

237


1/14/26, 2:19 PM

For more information, see Customizing for Transportation Management under  Business Add-Ins (BAdIs) for

Transportation Management

## Planning

 BAdI: Determination of Freight Unit Stages . For more information about

using preferred equipment types and groups, see Preferred Equipment Groups and Types.

Optionally, in the Capacity Selection Settings of your planning profile, you have indicated your equipment types on the

Vehicle Types tab page and the Container Types tab page. For more information, see Planning Profile.

Optionally, in the Capacity Availability Settings of your planning profile, you have restricted the availability of your

equipment types. For more information, see Planning Profile.

Optionally, in the Constraints and Costs Settings of your planning profile, you have indicated costs for your equipment

types. For more information, see Constraints and Costs Settings.

If you want to display your objects grouped by equipment type in the hierarchies of the transportation cockpit, you have

selected the standard grouping attribute Equipment Type in Customizing.

For more information, see Customizing for Transportation Management under  Planning

 General Settings

## Define

Hierarchical Views for Business Documents .

If you work with incompatibilities, you have specified that your incompatibilities apply to equipment types. You do so in the

Validity section of the Edit Incompatibilities app. Note that this field is only displayed for incompatibilities that involve

vehicle resources or vehicle types.

## Features

In the transportation cockpit, you can work with equipment types in the same way as you work with resources. For example, you

can do the following:

You can select a vehicle type and several freight unit stages and then select Assign Selected Items. The system creates a

road freight order.

You can select a trailer type and then select Create Capacity Document. The system creates a trailer unit.

You can select a freight unit stage and a truck type and a trailer type and then select Assign Selected Items. The system

creates a road freight order and a trailer unit.

You can select a road freight order and then select Remove Truck Type to remove the truck type.

Drag and drop is also supported.

Further, the following planning actions are supported for equipment types:

## Scheduling

## Load planning and load consolidation

Load planning considers combination vehicle types similarly to combination resources.

## Gantt chart

Vehicle scheduling and routing (VSR) optimization

Generation of transportation proposals

  Note

By default, equipment types are considered as being always available. You can restrict their availability by indicating a

shift sequence and a factory calendar in the Capacity Availability Settings of your planning profile (see "Prerequisites").

This is custom documentation. For more information, please visit SAP Help Portal.

238


1/14/26, 2:19 PM

Equipment types can't be displayed on the geographical map.

The following equipment types are supported:

Vehicle type

Truck type

Trailer type

Locomotive type

Railcar type

## Container type

In the transportation cockpit, the most specific term is used on the user interface where possible. If this is not possible, the generic

term "equipment type" or "vehicle type" is used.

## Preferred Equipment Groups and Types

When you assign freight unit stages to capacity documents or create capacity documents based on freight unit stages, you can

use preferred equipment groups and types to automatically create local items such as container items in capacity documents.

## Prerequisites

You have implemented the Business Add-In (BAdI) Determination of Freight Unit Stages

(/SCMTMS/FU_STAGE_MODIFY). For more information, see Customizing for Transportation Management under

Business Add-Ins (BAdIs) for Transportation Management

## Planning

 BAdI: Determination of Freight Unit Stages .

You have defined your preferred equipment groups and types as master data in the system. For more information, see

Customizing for Transportation Management under  Master Data

## Resources

 General Settings

## Define Equipment

Groups and Equipment Types .

In the manual planning settings of your planning profile, you have selected Create TU as Freight Document Item in the

Create TU Item or TU Document field.

Note that if you have selected Create TU Document in this field for other purposes, the system does not consider the

preferred equipment group and type of a freight unit stage when you assign it to a freight document. Transportation unit

documents (TU documents) can't be created automatically by the system when you assign freight unit stages to freight

orders or freight bookings. You can, however, first assign the freight unit stage to a TU document and then assign this

document to the freight document (in separate steps).

## Features

## Determination of the Preferred Equipment Group and Type

After freight units have been created during freight unit building or have been updated, the system determines the preferred

equipment groups and types using the Determination of Freight Unit Stages BAdI. The BAdI considers the following information

as an input:

Material freight group of each requirement item

## Material of each requirement item

This is custom documentation. For more information, please visit SAP Help Portal.

239


1/14/26, 2:19 PM

Transportation mode of the requirement stages

Source and destination location of the requirement stages

Requested and acceptable time windows

You can enhance and adjust this input.

The result of the determination is displayed in the fields Preferred Equipment Group and Preferred Equipment Type in the freight

unit stage. The fields are not displayed by default, but you can select them in the UI settings.

You can manually change the preferred equipment groups and types in the capacity document item.

## Creation of Capacity Document Items Using the Transportation Cockpit

When you assign freight unit stages to a capacity document in the transportation cockpit or when you create a capacity document

based on freight unit stages, the system automatically creates local items in the capacity document based on the preferred

equipment groups and types that the system has determined using the BAdI. Examples:

When you create a road freight order for a freight unit stage with a preferred equipment group and type, this road freight

order is based on the preferred equipment group and type.

When you create a road or rail freight order or an ocean freight booking for a freight unit stage that has a container group

and type defined as a preferred equipment group and type, the system automatically creates a local container item with

this container group and type in the new freight order or ocean freight booking.

When you create a rail freight order for a freight unit stage that has a railcar group and type defined as a preferred

equipment group and type, the system automatically creates a local railcar item with this railcar group and type in the new

rail freight order.

To ensure that the system considers the preferred equipment group and type, please note the following restrictions. If you ignore

these restrictions, the system displays a warning message:

If several stages of the same freight unit are planned together, the preferred equipment groups and types of these stages

must be the same.

The preferred equipment groups and types must be compatible with the document types. If you have, for example,

specified a railcar equipment group and type for the freight unit stage as preferred equipment group and type and you want

to assign the stage to an ocean freight booking, this equipment group and type don't match and are therefore ignored by

the system.

If an equipment group and type have already been specified for the capacity document to which you assign a freight unit

stage, the system doesn't consider the preferred equipment group and type of this freight unit stage.

Values of the preferred equipment group and type that have been specified for the freight unit stages must be predefined

as equipment groups or types in the system (see Prerequisites). Furthermore, equipment groups and types with restricted

use in planning are not considered by the system.

If the system creates a new local item in a capacity document, it does not check the capacity of the corresponding

equipment type. This can lead to the equipment type being used above its capacity. However, the utilization of the item is

displayed so that you can easily identify whether the capacity is exceeded.

## Creation of Capacity Document Items Using the Capacity Document Apps

The feature described above for manual planning in the transportation cockpit can also be used in the different apps for creating

and editing capacity documents, such as the Edit Ocean Freight Booking app. For example, when you assign a freight unit stage to

an ocean freight booking in the Edit Ocean Freight Booking app, the system also considers the preferred equipment group and

This is custom documentation. For more information, please visit SAP Help Portal.

240


1/14/26, 2:19 PM

type that has been determined for this freight unit stage. For example, it can then create a local container item in the ocean freight

booking if the prerequisites are met.

## Related Information

Manual Planning with Local Transportation Unit Items

Use of Package Units in Planning

You can create, edit, and display package units.

## Prerequisites

You have configured the relevant settings in Customizing so that you can configure your standard layout for the use of

package units in the layout settings for the transportation cockpit. Several hierarchy types are predefined by default for the

planning of package units.

In addition, you can define your own hierarchy types in Customizing for Transportation Management under  Planning

## General Settings

 Define Hierarchical Views for Business Documents . For more information, see Use of Hierarchical

Views.

You have defined a transportation unit type in Customizing with the transportation unit category Package. The

transportation unit type PKG is predefined by default for package units. For more information, see Customizing for

Transportation Management under  Planning

## Transportation Unit

 Define Transportation Unit Types .

## Use

## Manual Creation of Package Units

You choose Package Unit to create a new package unit. The system proposes the business document type that you entered

for package units in your planning profile. You can overwrite this.

You can also create package units based on freight unit stages. To do this, select one or more freight unit stages and then

choose  Create Capacity Document

## Create Package Unit

. The system creates a new package unit. If you want to

create a package unit for each freight unit stage, choose  Create Multiple Capacity Documents

 Create Multiple

Package Units .

You can assign freight unit stages to existing package units. To do this, select one or more freight unit stages and a package

unit and then choose Assign Selected Items. Alternatively, you can use drag and drop.

  Note

You can use default routes during the manual creation of package units. For more information, see Default Route.

## Manual Creation of Capacity Documents from Package Units

You can create capacity documents based on package unit stages. To do this, for example, select several package unit

stages and a truck and then choose Assign Selected Items. The system creates a new road freight order. Alternatively, you

can use drag and drop or choose Create Capacity Document.

You can assign package unit stages to existing capacity documents. To do this, for example, select several package unit

stages and a road freight order and then choose Assign Selected Items. Alternatively, you can use drag and drop.

This is custom documentation. For more information, please visit SAP Help Portal.

241


1/14/26, 2:19 PM

## Automatic Creation of Package Units

You can create package units based on unified package building for freight units. To do this, choose Create PUs Based on

UPB in the freight unit stage list or hierarchy. First the system creates packages for the freight units and then it creates

package units for these packages.

In doing so, it includes first all freight units for which you have selected Exclusive Package for Customer. This means that

the package units only receive products for a specific customer.

It then groups the remaining freight units that can be consolidated into soft and hard location groups according to your

setting in the unified package building profile. Then it creates packages for these freight units. As the final step, the system

checks the utilization threshold value that you have specified in the planning profile for the location groups. If the utilization

of the package exceeds the threshold value, the system creates a package unit for this package. If a freight unit is contained

in both a soft and a hard location group, the system first checks the threshold value for the soft location group and then the

threshold value for the hard location group.

If you have also specified a utilization threshold value for business partners, this is ignored (that is, the location groups take

priority).

If you have specified a utilization threshold value for business partners, the system groups the remaining freight units that

can be consolidated based on the business partner and creates packages. The system checks the utilization threshold

value that you have specified in the planning profile for the business partner. If the utilization of the package exceeds the

threshold value, the system creates a package unit for this package.

Note that if several packages are created for one group during unified package building, only one of these packages needs

to have a utilization above the threshold for the system to be able to create a package unit for all these packages. This

applies to all the threshold values mentioned above.

In the planning profile, you can define a maximum number of packages up to which the system creates package units. If

this value is exceeded, the system does not create any package units. This parameter is valid for all the above steps.

Package units that were created with this function are taken into account and planned in the next VSR optimization run, but

the packing information is not changed. Freight units that cannot be planned in package units using this function are

planned by the VSR optimization run as before.

As a prerequisite for this function, you must have entered the following in the planning profile in the settings for unified

package building:

## A unified package building profile

A default package unit type and, optionally, a default rule for the creation of package units

This rule controls whether the system is to create one package unit for each package item (standard setting) or one

package unit for all package items.

In addition, you can enter a package unit type for package units with only one destination location and a

corresponding rule.

The prerequisite for considering the maximum number of packages per package unit is that you have selected the

value Create One PU for all Package Items for one of the two package unit types.

For more information, see Planning Profile.

The sample planning strategy CEPU_ONLY is provided for creating package units on the basis of unified package building

for freight units. It contains the planning method VSR_CEPU. You can include this method in your own planning strategies

according to your needs.

You can also create package units in parallel processes. To do this, you have to define a parallel processing profile and

assign it to your planning profile (in the subprofile Settings for Unified Package Building under  Unified Package

## Building

 Parallel Processing Profile ). For more information, see Definition of Parallel Processing Profiles. You can also

This is custom documentation. For more information, please visit SAP Help Portal.

242


1/14/26, 2:19 PM

execute this function in the background (see Creation of Package Units Based on Unified Package Building for Freight

Units).

  Note

In the default package unit type, you must have selected Linear with Distribution as the sequence type of

stages. In the package unit type for package units with only one destination location, you must have selected

Defined and Linear as the sequence type of stages. In addition, you must have specified in the Assgnmt of

Pred.Docs (Assignment of Predecessor Documents) field that freight units have to be assigned completely to a

package unit.

If you have specified in the default package unit type that freight units have to be assigned completely to a

package unit (Assgnmt of Pred.Docs field (“Assignment of Predecessor Documents”)) and the system has then

had to distribute a freight unit to several package units during the creation of package units, it splits this freight

unit. If you undo the creation of the package units, these freight units remain split.

You cannot change the packaging hierarchy in these package units manually. Nor can you manually add or

remove freight units to or from these package units.

If you assign two of these package units containing product quantities from the same freight unit to different

freight orders, the system splits the freight unit.

If you want to undo the creation of package units, you must reverse the created package units. Alternatively, you

can use the Undo pushbutton.

## Automatic Planning of Package Units

VSR optimization (VSR = vehicle scheduling and routing) including scheduling takes package units into account in the

same way as container units, that is, only as requirement documents and not as capacity documents. This means that VSR

optimization can plan, in other words assign, package units and container units in freight documents and other

transportation units. It cannot, however, assign freight units to a package unit or container unit. This is possible in manual

planning only (see above).

VSR optimization including scheduling takes into account the pickup and delivery windows for freight units assigned to a

package unit. However, if you have defined times at a given stop of a package unit, VSR optimization takes these times into

account and ignores the time windows of all assigned freight units at this stop. The same is true for container units.

Scheduling ignores the loading and unloading times of freight units assigned to package units. Only the loading and

unloading times of package units assigned to freight documents or transportation units are taken into account.

  Note
You can use default routes during the automatic creation of package units. For more information, see Use of Default Routes in

VSR Optimization.

## Editing and Displaying Package Units

You can display package units in a tabular and graphical format.

You can display and edit package units on the map, in the same way as container units and trailer units. For more

information, see Interactive Planning on the Map.

## Activities

You create and edit package units in the transportation cockpit. Open the Transportation Cockpit app on the launchpad.

This is custom documentation. For more information, please visit SAP Help Portal.

243


1/14/26, 2:19 PM
Related Information

## Package Unit

Creating a Package Unit

Planning with Distribution Stops

## Planning with Distribution Stops

You use package units with distribution stops to map the transportation of mixed pallets in delivery tours, for example. The goods

are then unloaded directly from the truck one after the other at different locations.

## Prerequisites

You have defined a transportation unit type in Customizing that allows the use of distribution stops. For more information

about this and about distribution stops, see Package Unit.

To display distribution stops in the transportation cockpit in your hierarchy for package units or package unit stages, in

Customizing you must select the Distribution Stops hierarchy level and set the Show Level (Show Hierarchy Level)

checkbox. For more information, see Customizing for Transportation Management under  Planning

## General Settings

 Define Hierarchical Views for Business Documents .

Note that this setting may lead to increased runtime. To avoid this, you can alternatively specify in your page layout that you

want to display distribution stops (detail area for demand). For more information, see Page Layouts.

## Display of Distribution Stops

In the transportation cockpit, you can display distribution stops in the hierarchies for package units and package unit stages. If you

have configured your page layout accordingly, you can display the list of distribution stops for a package unit stage (hierarchy for

package units or package unit stages) using Show Details (Actions columns).

## Manual Planning

You can plan package units with distribution stops in manual planning like any other package unit. This means that you can, for

example, drag and drop a distribution stop to assign it to another freight order, another package unit, or another resource (truck,

trailer, or container). Alternatively, you can assign it using the Assign Selected Items pushbutton.

  Note

Note that if you have created a package unit from a freight order (see Transportation Planning with Mixed Packages and

Deconsolidation), you can only assign all distribution stops together to another freight order or resource. This means

that the corresponding stage of the package unit is assigned to the other freight order.

You cannot process package units with distributed freight units in manual planning in the transportation stage for the

delivery tour. However, you can process them in the pre-carriage transportation stage.

## Planning on the Map

You can display and plan package units with distribution stops on the map.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

244


1/14/26, 2:19 PM

For example, if you drag and drop the stage for a distribution stop to another freight order all the other stages for further

distribution stops are also assigned to the other freight order.

## Automatic Planning and Scheduling

Package units with distribution stops are included in automatic planning (VSR optimization). Package units are included in

scheduling only if they are assigned to another document (such as a freight order).

You can display the package unit in the explanation tool.

During scheduling, the quantities of freight units or package units (if the package unit is assigned to a container unit) are taken

into account at all distribution stops to determine the variable unloading times. At all other stops, the quantities of the package

unit are taken into account to determine the variable unloading times.

  Note

When the variable loading times are calculated for a freight order and a partial quantity of a distributed freight unit is

assigned to a distribution stop of a package unit, the system includes only the partial quantity assigned to this package

unit in the calculation.

VSR optimization cannot create, change, or delete package units with distributed freight units.

Related Information

## Package Unit

## Creating a Package Unit

Transportation Planning with Mixed Packages and
## Deconsolidation

In Transportation Management (TM), you can transport orders from different customers together across several transportation

stages and deconsolidate them on the last transportation stage in a “delivery tour”. With the help of mixed packages, you can

optimize resource utilization and so reduce the freight costs.

You can use package units in TM to consolidate packages for different customers. Once the system has created packages using the

unified package building function, you can group them together in package units and assign them to several freight orders. To

optimize the utilization of the packages, a freight unit can be assigned to several package units. You do not have to split the freight

unit provided the different package units to which a freight unit is assigned are transported with the same freight document for

each stage. For more information, see Package Unit.

Below is an example of how SAP TM supports you in the planning process. You first plan the delivery tour(s) and then the linear

transportation stages of your route.

## Prerequisites

You have made all the required settings for unified package building. For more information, see Unified Package Building in

TM.

More specifically, you have entered a unified package building profile in the planning profile that is assigned to the

document type or that you use to call the transportation cockpit. If you want to determine and display the exact position of

This is custom documentation. For more information, please visit SAP Help Portal.

245


1/14/26, 2:19 PM

the products in the package, you have to activate the Detailed Mixed Package Building function in this profile. For more

information, see Detailed Mixed Package Building.

You have defined a transportation unit type for packages. Here you have made the following settings:

You have activated unified package building for this document type.

You have specified that, in addition to linear, consecutive transportation stages, your route contains a delivery tour

for the deconsolidation of packages. To do this, select the value Linear with Distribution in the Seq. Type of Stages

(Sequence Type of Stages) field.

You have specified that a freight unit can be assigned to multiple packages. To do this, select the value Partially or

Completely in the Assgnmt of Pred.Docs (Assignment of Predecessor Documents) field.

For more information, see Customizing for Transportation Management under  Freight Order Management

## Transportation Unit

 Define Transportation Unit Types .

In Customizing for the freight order type, you have defined a default package unit type that contains the settings described

above. For more information, see Customizing for Transportation Management under  Freight Order Management

## Freight Order

 Define Freight Order Types .

In Customizing for the freight order type, you have indicated in the Default Package Unit Creation Rule field whether the

system is to create one package unit per package or one package unit for all selected packages.

You have created a freight unit building rule (FUB rule). If you want to use the VSR optimizer later to create freight orders

and a rough estimation of the number of packages is to be taken into account, enter a unified package building profile on

the Advanced Settings tab page of the FUB rule. Then, select the Estimate Package Count Only option in the Unified

Package Building Result field.

For more information, see Freight Unit Building Rule.

If you want to use the VSR optimizer or manual planning in the planning process described here, you can define planning

strategies to combine the process steps and have them performed automatically by the system. The following planning

strategies are available:

VSRI_CPB for manual planning with unified package building based on capacity documents

VSRI_PBLP for manual planning with unified package building based on capacity documents and load planning

CPB_ONLY for unified package building based on capacity documents

VSR_CPB for VSR optimization with unified package building based on capacity documents

VSR_CPBALP for VSR optimization with unified package building based on capacity documents and load planning

For more information, see Planning Strategies.

## Process

The following figure provides an overview of an example process:

This is custom documentation. For more information, please visit SAP Help Portal.

246


1/14/26, 2:19 PM

Planning Process with Mixed Packages and Deconsolidation

Planning of Delivery Tours

1. Creating freight units

You have the system automatically create freight units based on your order documents (such as forwarding orders or sales

orders) and using the freight unit building rule you defined. For more information, see Creation and Editing of Freight Units.

2. Creating a freight order for the delivery tour

You create a freight order for the unplanned stages of the freight units that belong to your delivery tour. You can also use

the VSR optimizer to do this. If you have specified this in your freight unit building rule, the system takes into account the

number of packages estimated when the freight units were created. The optimizer also takes into account the maximum

number of packages for each truck as well as weight and volume restrictions.

For more information, see Creation and Editing of Freight Orders and VSR Optimization.

3. Unified package building

You have the system create packages for the items in the freight order. These packages are then available locally in the

freight order. For more information, see Unified Package Building in TM.

4. Load planning

You execute a load planning for these packages in the freight order. For more information, see Load Planning.

5. Finalize the packaging

After you have checked the results of unified package building and made any necessary manual adjustments, you set the

load plan status of the packages to "Finalized” for the freight order. You do this at header level in the freight orders under

Load Plan Status (Packaging)

 Set All Top-Level Packages to Finalized . Alternatively, you can also select the vehicle

resource on the Items tab page in the Load Plan hierarchy view and select the Set All Top-Level Packages to Finalized

option or select individual packages and select the Set to Completed option.

After the status has been set, the packages are fixed for further planning. This means that you can only change the

packages if you reset the status.

6. Creating package units

If you want to be able to use and plan these packages in other freight documents as well, you must create package units.

You do this at header level in the freight order under  Follow Up

## Create Package Units . Alternatively, as described

under step 5, you can also select individual packages and select the Create PUs option. However, note the following: You

must always select complete freight units. In other words, all items in the freight units selected with the packages must be

included in the selected packages of this freight order. The system supports you with warning messages and input help.

This is custom documentation. For more information, please visit SAP Help Portal.

247


1/14/26, 2:19 PM

The following applies to package units created by the system:

The system creates the package units in such a way that a freight unit can be assigned to several package units. You

can display the package units to which a freight unit is assigned in the stage details of a freight unit or in the

transportation cockpit on the Assignment to Package Units tab page.

The system determines the type of package unit created and the way in which package units are built from

packages (1:1 or 1:n) from the Customizing settings for the freight order type and the planning profiles used.

The package units contain both the linear transportation stages and a special stage with the distribution stops of

the delivery tour. These stops are displayed as substops, but their sequence is arbitrary. The transportation stages

of the freight orders and freight units remain unchanged.

The package units also contain information about the exact position of products in a package.

The package units that were created from a freight order cannot be changed. If you want to make any changes you

have to cancel the package units (see step 7).

For more information, see Package Unit and Creating a Package Unit.

7. Canceling package units (optional)

You can cancel the package units created by the system in step 6. You do this at header level or for individual packages by

selecting the Cancel Package Units and Merge option. The system then integrates these packages back into the item

hierarchy of the freight order as local packages.

However, the package units must not have already been assigned to other freight orders. Moreover, the same prerequisites

apply to the selection of package units as described above for the creation of package units.

For more information about how the load plan status changes after the process steps described above, see Load Plan Status

Changes.

## Planning of Main Carriage Stage

1. Creating a freight order for the main carriage stage of the package units

You manually create one or more freight orders for the main carriage stage of your package units or have these created by

the VSR optimizer.

2. Load planning

You execute a load planning for the package units in the freight orders.

3. Finalizing the load plan

After you have made any necessary manual adjustments, you set the load plan status of the load planning to "Finalized” for

the freight orders. You do this at header level in the freight orders under  Load Plan Status (Load Planning)

## Set Load

Plan to Finalized .

4. Splitting the freight units

The package units created by the system can contain freight units that are assigned to several package units. If the

different package units to which a freight unit is assigned are transported with different freight orders in the main carriage,

the system splits the freight unit accordingly and distributes it among the freight documents. Note that you must have set

the load plan status (load planning) to "Finalized".

## Related Information

Use of Package Units in Planning

## Planning with Distribution Stops

This is custom documentation. For more information, please visit SAP Help Portal.

248


1/14/26, 2:19 PM

Use of Normalized Quantities and Capacities

## Load Plan Status Changes

Many of the steps of the "Transportation Planning with Mixed Packages and Deconsolidation" process have an effect on the load

plan status. The following sections describe how the load plan status changes after each process step. Note however that they only

refer to the first part of the process ("Planning of Delivery Tours").

## Initial situation

Let's assume the freight order created in this process has three freight units assigned to it (FU1, FU2, and FU3).

On item level, for example in the load plan hierarchy, the load plan status looks like this:

Load Plan Item Status (Cargo)

Load Plan Status (Capacity) (Description)

1. Vehicle Resource

1.1 Product 1 (FU 1)

1.2 Product 2 (FU 2)

1.3 Product 3 (FU 3)

(Description)

Not Relevant

Not Planned

Not Planned

Not Planned

Not Planned

Not Relevant

Not Relevant

## Not Relevant

Note that the status changes after each step are marked in bold below.

## Package building

After you have performed package building for all items of your freight order, the load plan status looks like this:

Load Plan Item Status (Cargo)

Load Plan Status (Capacity) (Description)

1. Vehicle Resource

2. Package (local)

(Description)

Not Relevant

## Not Planned

2.1 Product 1 (FU 1)

## Planned

3. Package (local)

## Not Planned

3.1 Product 2 (FU 2)

## Planned

4. Package (local)

## Not Planned

4.1 Product 3 (FU 3)

## Planned

Load planning

Not Planned

## Planned

Not Relevant

## Planned

Not Relevant

## Planned

## Not Relevant

After you have performed load planning for all items of your freight order, the load plan status looks like this:

1. Vehicle Resource

(Description)

Not Relevant

## Planned

Load Plan Item Status (Cargo)

Load Plan Status (Capacity) (Description)

This is custom documentation. For more information, please visit SAP Help Portal.

249


1/14/26, 2:19 PM

2. Package (local)

2.1 Product 1 (FU 1)

3. Package (local)

3.1 Product 2 (FU 2)

4. Package (local)

4.1 Product 3 (FU 3)

Finalizing packaging

Planned

Planned

Planned

Planned

Planned

Planned

## Planned

Not Relevant

## Planned

Not Relevant

## Planned

## Not Relevant

After you have finalized packaging for all items of your freight order, the load plan status looks like this:

Load Plan Item Status (Cargo)

Load Plan Status (Capacity) (Description)

1. Vehicle Resource

2. Package (local)

2.1 Product 1 (FU 1)

3. Package (local)

3.1 Product 2 (FU 2)

4. Package (local)

4.1 Product 3 (FU 3)

(Description)

Not Relevant

Planned

Finalized

Planned

Finalized

Planned

Finalized

Planned

Finalized

Not Relevant

Finalized

Not Relevant

Finalized

## Not Relevant

Note that the requirement assignments of local packages with status value Finalized are automatically fixed.

Creating package units (PUs)

After you have created package units for the freight order, the load plan status looks like this:

Load Plan Item Status (Cargo)

Load Plan Status (Capacity) (Description)

1. Vehicle Resource

(Description)

Not Relevant

2. Package (PU 1)

## Planned

2.1 Product 1 (FU 1)

Not Relevant

3. Package (PU 2)

## Planned

3.1 Product 2 (FU 2)

Not Relevant

4. Package (PU 3)

## Planned

4.1 Product 3 (FU 3)

## Not Relevant

## Related Information

Transportation Planning with Mixed Packages and Deconsolidation

## Planned

Not Relevant

Not Relevant

Not Relevant

Not Relevant

Not Relevant

## Not Relevant

This is custom documentation. For more information, please visit SAP Help Portal.

250


1/14/26, 2:19 PM

## Use of Normalized Quantities and Capacities

If you are using different packaging materials for planning in a road scenario, you can use normalized load consumption quantities

and capacities in Transportation Management (TM) to optimize the use of the loading space. If, for example, your packaging

material consists of pallet cages and europallets, you can convert and plan these into europallets or loading meters. The capacity

of a truck can also be defined as a normalized capacity.

## Prerequisites

To activate the use of normalized quantities (NLQ) and additional normalized quantities (ALQ), you have indicated in your

business document type whether the relevant unit of measure for the NLQ or ALQ is determined based on a condition (with

condition type /SCMTMS/NLQ_UOM) or on the default unit of measure for the NLQ or ALQ that you have specified in

Customizing for your freight unit type, transportation unit type, and freight order type. We recommend that you use

consistent unit of measures within one scenario.

For more information, see Customizing for Transportation Management under the following Customizing activities:

Planning

## Freight Unit

 Define Freight Unit Types

Freight Order Management

## Transportation Unit

 Define Transportation Unit Types

Freight Order Management

## Freight Order

## Define Freight Order Types

In the Customizing activity Define UoM Relevance for NLQ and ALQ, you have optionally specified whether a unit of

measure is relevant for NLQs or ALQs.

For more information, see Customizing for Transportation Management under  Basic Functions

## Normalized Quantities

(NLQ) and Additional Normalized Quantities (ALQ)

  Define UoM Relevance for NLQ and ALQ .

If you specify a unit of measure, the system offers it for selection in the corresponding user interfaces. If you don’t specify a

UoM in this Customizing activity, the system offers dimensionless UoMs.

You have indicated a unit of measure for NLQ and ALQ in the Define Transportation Cockpit Settings app. The system

needs this to be able to display NLQs on the map as well as for trucks, trailers, and containers in the transportation cockpit.

For more information, see Planning Profile.

Some of the values related to the normalized quantity can be displayed in a series of lists and hierarchies in the

transportation cockpit using the corresponding field catalogs. For more information, see Field Configuration for the

Transportation Cockpit.

If you are working with schedules, you must also enter a default unit of measure for the NLQ in the schedule type. The NLQ

is copied from the schedule departure into the freight order only if this unit of measure corresponds to the default unit of

measure in the freight order.

For more information, see Customizing for Transportation Management under  Master Data

 Transportation Network

## Schedule

 Define Schedule Types .

You have defined an alternative quantity for the unit of measure of the normalized quantity in your material master. To do

so, on the SAP Easy Access screen, choose  Logistics

 Transportation Management

  Master Data

 Material

## Create

 or Change. Alternatively, you have specified an individual NLQ per product or reference product and unit of measure in

the Define Normalized Quantity app.

For more information, see Determination of Normalized Load Consumption Quantities.

If you want a conversion into an additional normalized unit of measure, you need to define a conversion factor between the

unit of measure of the NLQ and the unit of measure of the ALQ in the Customizing activity Define Conversion Between

NLQ and ALQ UoM.

This is custom documentation. For more information, please visit SAP Help Portal.

251


1/14/26, 2:19 PM

For more information, see Customizing for Transportation Management under  Basic Functions

## Normalized Quantities

(NLQ) and Additional Normalized Quantities (ALQ)

 Define Conversion Between NLQ and ALQ UoM .

You have entered the capacity for the NLQ in the default unit of measure in the master data for the resources you are using.

For more information, see Definition of Capacity.

You have specified the number of units and alternative number of units as well as the NLQ UoM and ALQ UoM for your

equipment types in the Customizing activity Define Equipment Groups and Equipment Types.

For more information, see Customizing for Transportation Management under  Master Data

 Resources

 General

## Settings

  Define Equipment Groups and Equipment Types .

If you want an overview of the packaging material used in a document, you must activate the option Aggregate Load

Consumption Quantities in Customizing for the freight unit type, transportation unit type, and freight order type. For more

information, see the Customizing activities mentioned above.

To display a compressed view in the lists and hierarchies of the transportation cockpit, you need to add the corresponding

fields to your lists and hierarchies using field catalogs. For more information, see Field Configuration for the Transportation

Cockpit.

To display a compressed view in the Gantt chart, you must assign the corresponding fields to the specific lists. For more

information, see Customizing for Transportation Management under  Basic Functions

## Gantt Chart

## Define Field Lists

and Label Schemes for Gantt Chart

.

To display the utilization of the capacity in relation to the NLQ and to display the remaining capacity in the packaging

material overview, you must define the method for calculating these values in the NLQ Utilization Rule field in Customizing

for the freight order type.

For more information, see Customizing for Transportation Management under  Freight Order Management

 Freight

## Order

 Define Freight Order Types .

If you want to use the NLQ and ALQ as split criteria in freight unit building, you have defined the NLQ or ALQ or both as

planning quantity in your freight unit building rule.

For more information, see Creation and Editing of Freight Units.

## Features

## Determination of Normalized Quantity

The NLQ is used to allow the comparison of different packaging materials that are planned within the same scenario. The different

units of measure of the packaging material are converted to a standard unit of measure to facilitate comparison.

The system determines NLQs in the following way:

First, the system takes into account the NLQs that you have defined individually for the product and UoM in the Define Normalized

Quantity app. It then takes into account the NLQs that you have defined individually for the reference product in this app.

  Note

The system iteratively moves up in the reference product hierarchy until it finds a value.

The system then takes into account the full package definition of the product master data that you have defined in the

transactions for creating or changing materials. It divides 1 by the defined full package quantity. For example, 1 EPL divided by 100

pieces results in 0.01 EPL per piece of the product. It then takes into account the full package definition of the reference product

master data in one of these apps.

This is custom documentation. For more information, please visit SAP Help Portal.

252


1/14/26, 2:19 PM

  Note

The system iteratively moves up in the reference product hierarchy until it finds a value.

If the system can determine a value in one of these steps, this is the result and subsequent steps are not evaluated anymore. If the

system can’t determine a value in any of the steps, it returns value 0.

The system also determines the load consumption quantity (LCQ) for the items based on the normalized quantity and the

conversion factor that you defined in the master data of the packaging material.

The values determined by the system are displayed in the item details. The values for the entire freight unit document,

transportation unit document, or freight order document are also aggregated. The aggregated values for the normalized quantity

are displayed on the General Data tab page and the values for the LCQ are displayed on the Packaging Material Overview tab page

(see below).

For more information, see Determination of Normalized Load Consumption Quantities.

## Determination of Additional Normalized Quantity

The system determines ALQs by multiplying the value for the NLQs with the conversion factor that you have defined in the

Customizing activity Define Conversion Between NLQ and ALQ UoM. If you haven’t defined an appropriate conversion factor, the

value for ALQs remains empty.

While the system determines the NLQs on product item level and then on document level, it determines ALQs on document level

only.

For example, you can specify in Customizing that 1 europallet corresponds to 0.4 loading meters. If you have entered 20

europallets in the document, 8 loading meters are displayed as the additional normalized quantity of the document.

## Packaging Material Overview

You can use the packaging material overview to get an overview of the packaging material contained in a document. If you have

configured this in Customizing, a tab page appears in freight units, transportation units, and freight orders showing the packaged

and unpackaged LCQ as well as the number of unpackaged freight items for a document.

In the case of freight units, the system displays the values determined during freight unit building in the Unpackaged Load

Consumption Quantity field. The actual values that were calculated during planning and unified package building are displayed in

freight order documents in the Packaged Load Consumption Quantity field.

The remaining capacity of the freight order document is also displayed. Depending on your Customizing settings, the system also

takes into account the remaining capacity of the individual packages.

The system displays a compressed view of this information in your personal object worklist for freight orders. This is also displayed

in the lists and hierarchies of the transportation cockpit and in the Gantt chart if you have completed the steps mentioned in the

prerequisites.

## Normalized Loading Space Capacity and Calculation of Maximum Utilization

If you have specified the number of units and alternative number of units as well as the NLQ UoM and ALQ UoM for your resources

(in the transaction for creating resources in the SAP Easy Access menu) or your equipment types (in the Customizing activity

Define Equipment Groups and Equipment Types), the system displays the utilization of the resources or equipment types with

regard to the normalized quantity in the header data of the freight order. You can also specify this normalized loading space

capacity for trailers. The utilization is then displayed separately for the truck and trailer and together for both resources.

This is custom documentation. For more information, please visit SAP Help Portal.

253


1/14/26, 2:19 PM

The system calculates the maximum utilization, taking into account the most critical transportation stage and the most critical

unit of measure (mass, volume, or normalized quantity).

## Check Normalized Quantities in Documents

You can check whether the normalized quantities in your documents are current. You can cancel documents with obsolete

normalized quantities. For more information, see Check Normalized Quantities in Business Documents.

## Example

The following example illustrates the calculation of an NLQ, taking into account the data that you have defined in the material and
resource master data:

Two different packaging materials are used in a road scenario. The first packaging material is a europallet (unit of measure

is PA1). The second packaging material is defined in a unit of measure that is half the size of the europallet (PA2).

You can now define the normalized unit of measure PAN in the master data of the packaging material as follows:

PAN = PA1 * 1

PAN = PA2 * 2

If a resource, for example, has a capacity of 33 PAN (as the NLQ), different combinations of PA1 and PA2 can be checked so

that the total capacity is not exceeded. For example, 23 PA1 and 20 PA2 would fit, but also 33 PA1 or 66 PA2.

NLQ Determination Based on Documents

## Use

You can determine a value for the normalized load consumption quantity (normalized quantity, NLQ) per product and unit of

measure (UoM) based on historical consolidation data. This value indicates how much space (footprint) a single product

consumes in a top-level package (that is, the outer packaging).

The system determines this value in the following way:

1. For all products contained in the selected set of road freight orders, the system reads the NLQs, which are currently stored

in the Define Normalized Quantity app.

2. The system determines NLQs for all products based on the packaging information from the selected road freight orders.

  Note

The system only takes into account selected road freight orders that were created after the last change of the NLQ in

the Define Normalized Quantity app. If you have indicated a weighting factor of 100% on the selection screen, the

system considers all selected road freight orders without any time restriction.

3. The system calculates the average NLQs taking into account the maximum tolerance for outliers that you have indicated on

the selection screen.

4. The system calculates the new NLQ for these products according to the following formula:

New NLQ = Weighting Factor × Average NLQ from Road Freight Orders + (1 - Weighting

## Factor) × Current NLQ

5. Finally, the system saves the new NLQs in the Define Normalized Quantity app, taking into account the threshold that you

have indicated on the selection screen.

This is custom documentation. For more information, please visit SAP Help Portal.

254


1/14/26, 2:19 PM

For more information about the determination of NLQs, see Determination of Normalized Load Consumption Quantities.

## Prerequisites

Road freight orders with NLQs exist in the system.

You have created a selection profile.

For more information about prerequisites for package building, see Package Building.

## Features

On the selection screen, you indicate the following:

## A selection profile

## A UoM for the normalized quantity

The level on which normalized quantities are to be determined (on product level or reference product level, or both)

We recommend that products belonging to the same reference product have the same dimension.

## A weighting factor for real data

This factor specifies to what extent the system uses the average NLQ determined from existing road freight orders when

calculating the new NLQ for a product.

## A maximum tolerance for outliers

This tolerance defines the maximum percentage for NLQs that the system considers when averaging the NLQs from

existing road freight orders.

## A threshold for saving the newly calculated NLQs

With this threshold, you can prevent saving NLQs with insignificant changes.

When you select Continue, the NLQ determination screen is displayed:

On the left, the selected road freight orders are displayed. By selecting one or a small number of road freight orders and

then selecting Determine Products, you can restrict the number of products for which you calculate the NLQs.

On the right, the normalized quantities for the determined products are displayed. With Calculate Normalized Quantity,

you can calculate the new NLQs.

The system saves the new NLQs in the Normalized Quantity field in the Define Normalized Quantity app. If this app

already contains entries for combinations of product number and UoM for the normalized quantity, these entries are

overwritten.

## Activities

Open the Determine Normalized Quantity Based on Documents app from the launchpad. Alternatively, you can execute this

function in the background. For more information, see Determine NLQs Based on Documents.

We recommend that you check your business documents for outdated NLQs in regular intervals. For more information, see Check

Normalized Quantities in Business Documents.

## Related Information

This is custom documentation. For more information, please visit SAP Help Portal.

255


1/14/26, 2:19 PM

Defining Package Type Assignments

## Check Normalized Quantities in Business Documents

You can check whether the normalized load consumption quantities (normalized quantities, NLQs) in your business documents

are up to date and, if not, cancel these business documents.

## Use

If the normalized quantities in the Define Normalized Quantity app have changed (for example, because you have changed them

manually or have executed the report for determining normalized quantities based on randomized data), this change is not

reflected in existing business documents, such as freight orders or freight units.

Planning with business documents that are based on outdated normalized quantities might lead to unexpected results, such as

over-utilization or under-utilization. This function helps you to analyze such results, which would otherwise be very difficult - if not

impossible.

## Features

You need to select the following:

A document category (that is, road freight orders, container units, trailer units, package units, consignment orders, or

freight units)

One or several business documents using a selection profile and additional selection criteria, such as the document ID or

the document type

Moreover, you can define a threshold for canceling business documents. By doing so, you can prevent cancellation of business

documents in case of insignificant NLQ changes.

You can specify that documents with empty NLQs are to be determined and displayed.

The system returns all business documents that fulfill the following criteria:

Documents with changed normalized quantities taking into account the threshold that you have defined

## Documents with empty NLQs if you have selected the corresponding checkbox

You can select one or several of these business documents and cancel them. Note that you can only cancel road freight orders and

unplanned requirement documents (that is, freight units, package units, container units, and trailer units) with this function.

If you want to cancel planned requirement documents, you first need to unassign them from the assigned capacity document from

within the function. Then you need to restart the function, select the corresponding document category and run the function again

to cancel them.

  Note

If you cancel a road freight order, the status of the assigned requirement documents changes from Planned to

Unplanned.

If the unplanned requirement documents were created by automatic freight unit building, the cancellation triggers

another freight unit building run that takes into account the most up-to-date normalized quantities.

This is custom documentation. For more information, please visit SAP Help Portal.

256


1/14/26, 2:19 PM

If you have several levels of assignments, check and cancel the business documents in the sequence of their

assignment.

For example, you have a freight unit, which is assigned to a package unit, which is assigned to a container unit, which is

assigned to a trailer unit, which is assigned to a road freight order. In this case, first cancel the road freight order, then

the trailer unit, then the container unit, then the package unit, and finally the freight unit.

This function is based on the standard cancellation function. This means that business documents with other statuses,

such as In Execution, can't be canceled.

## Activities

Open the Check NLQs and Cancel Documents app from the launchpad.

Alternatively, you can execute the function in the background Check NLQs and Cancel Documents.

## Related Information

Use of Normalized Quantities and Capacities

Determination of Normalized Load Consumption Quantities

Defining Package Type Assignments

Use of Consignment Orders in Planning

You can use consignment orders in planning.

## Prerequisites

If you want to display and plan consignment orders on the geographical map and in the Gantt chart, you must have made

the settings for the geographical map and the Gantt chart. For more information, see Map Functions and Gantt Chart for

Transportation Planning.

If you want to work with hierarchies for consignment orders, you must have defined a hierarchical view in Customizing for

Transportation Management under  Planning

## General Settings

 Define Hierarchical Views for Business Documents .

For more information, see Use of Hierarchical Views.

## Use

The following manual planning operations are possible:

You can assign one or several consignment orders to a road freight order.

  Note

The Enable Settlement checkbox must be selected only in the related freight order type or consignment order.

You can assign one or several consignment orders to a truck. The system creates a road freight order.

You can assign a freight unit stage to a consignment order.

You can create a road freight order from within a consignment order.

You can create a consignment order from a freight unit stage or package unit stage.

This is custom documentation. For more information, please visit SAP Help Portal.

257


1/14/26, 2:19 PM

You can create a transportation unit, such as a container unit, for one or more consignment orders.

You can assign a consignment order to a transportation unit.

You can create packages for consignment orders.

  Note

If you create packages for a road freight order to which two consignment orders are assigned, the system creates

two separate packages for the two consignment orders.

The system packs items in one consignment order that belong to different external delivery notes into different

packages.

Consignment orders are taken into account in load planning and load consolidation.

You can display a hierarchy for a consignment order or display consignment orders as part of a freight order hierarchy.

During manual planning, the system considers incompatibilities between freight units at consignment order level. This means that

you can make sure that dangerous goods and non-dangerous goods are not planned in the same consignment order, for example.

Similarly, VSR optimization cannot plan consignment orders with incompatible content.

Scheduling considers consignment orders in the same way as container units or package units. This means that the system

considers the times of the assigned freight units if no requested and acceptable dates/times are defined for loading or unloading

in the consignment order.

You can also display and plan consignment orders on the geographical map and in the Gantt chart.

Consignment orders are also taken into account in VSR optimization.

  Note

It is possible that the system assigns consignment orders with different carriers to a freight order during manual planning or

VSR optimization. In this case, make sure that you edit the freight order manually.

Related Information

## Consignment Order

Creation and Editing of a Consignment Order

Use of Drivers in Planning

## Use

You can assign drivers to existing freight orders and vehicle resources. You can also create freight orders to which the system

assigns drivers as soon as they are created.

This function is available only for road freight orders and trucks.

## Prerequisites

In your master data, you have created drivers as business partners with the role Driver and you have defined absences and

non-working times for each driver. To define drivers, open the Define Business Partner app on the launchpad. For more

This is custom documentation. For more information, please visit SAP Help Portal.

258


1/14/26, 2:19 PM

information, see Definition of Business Partners.

In Customizing, you have created a freight order type with the relevant settings for the use of drivers. For example, you have

made the following settings:

You have specified whether you want to assign a single driver or a driver team (consisting of two drivers) to your

freight orders. If you want to create freight orders with assigned drivers in the transportation cockpit in the road

freight order hierarchy or in the road freight order list, you have to enter the number of required drivers.

  Note

If you want to change the number of required drivers in the road freight order hierarchy or in the road freight

order list, you have to select the Settings Can Be Changed in Freight Order checkbox.

You have specified whether you want to assign your drivers for entire freight orders or for the individual

transportation stages of a freight order.

For more information, see Customizing for Transportation Management under  Freight Order Management

## Freight Order

 Define Freight Order Types .

If you want to use the list of drivers in the transportation cockpit, you have to define a page layout in which you have made

the following settings for the driver in the resources area:

If you want to create freight documents from the list of drivers in the transportation cockpit, you have to select the

Create Freight Document checkbox.

If you want to add additional drivers to your list of drivers in the transportation cockpit, you have to select the Insert

checkbox.

If you want to use context determination in the transportation cockpit to display other orders within a specific

planning horizon that are assigned to a driver, you have to select the Context Determination checkbox. For more

information, see Context Determination.

If you want to use the Driver Assignment tab page in the details of your freight orders in the transportation cockpit, you

have to define a page layout in which you have selected the driver assignment in the order details area.

To define page layouts, open the Define Page Layouts for Transportation Cockpit app on the launchpad.

If you want to use the driver as a grouping attribute in the freight order hierarchy, you have to define a hierarchy type in

Customizing with the following settings:

## Transportation mode category: Road

Consumer: Transportation Cockpit: Freight Orders/Freight Bookings

Grouping rule: Standard Grouping Attribute

## Standard grouping attribute: Driver

For more information, see Customizing for Transportation Management under  Planning

 General Settings

## Define

Hierarchical Views for Business Documents  and Use of Hierarchical Views.

Optionally, in the capacity availability settings, you have restricted the availability of your drivers (see Planning Profile). You

can also indicate in these settings if the unavailability of your drivers is to be considered as a an absence or a break. Breaks

can be within the freight order, that is, the freight order can overlap with the driver’s break. Absences cannot lie within the

freight order, that is, the freight order cannot overlap with the driver’s absence (this may lead to a split of the freight order).

  Note

Absences of drivers, downtimes of vehicles, and validity periods of vehicles and drivers that you have defined in

the master data are always considered as downtimes independent from the settings that you make in the

This is custom documentation. For more information, please visit SAP Help Portal.

259


1/14/26, 2:19 PM

capacity availability settings.

The unavailability of your drivers is considered only during scheduling and VSR optimization (for the default

driver; VSR = vehicle scheduling and routing).

## Features

You can assign one or more drivers to an existing freight order or to the individual transportation stages of an existing freight order.

You can also create a freight order to which you can directly assign one or more drivers. In a driver team, the individual drivers take

turns to drive. The person who is not driving sleeps. You can also assign a driver to several existing freight orders.

  Note

If you assign the default driver of a specific vehicle resource to an existing freight order that has not yet been assigned a vehicle

resource, the system automatically assigns this freight order to the vehicle resource to which this driver is assigned as the

default driver. If a different vehicle resource has already been assigned to the freight order, this resource is kept. For more

information, see Driver.

  Note

If you have specified one driver per freight order as the number of required drivers in Customizing and a driver is already

assigned to your freight order in the system, when you assign a different driver to the freight order the system replaces the

driver originally assigned and assigns the new driver to the freight order.

## Activities

You can assign one or more drivers to an existing freight order in the transportation cockpit as follows:

## Drag and drop

You can drag and drop drivers from your list of drivers in the transportation cockpit to the freight order being planned in

your road freight order hierarchy or in your road freight order list. If you have specified in your freight order type that you

want to assign your drivers per transportation stage, you can also drag and drop drivers in the road freight order hierarchy

to the individual transportation stages.

## Manual creation and change

You can enter or change drivers manually in the Driver column in your road freight order hierarchy or in your road freight

order list. If you have specified in your freight order type that you want to assign drivers per transportation stage, you can

enter or change drivers for individual transportation stages in the Driver column in your road freight order hierarchy.

If you have activated driver assignment in the order details area in your layout for the transportation cockpit, you can select

a freight order in the road freight order hierarchy or in the road freight order list and manually enter or change a driver in

the details for this freight order.

## Dialog box

You can select a freight order in the road freight order hierarchy or in the road freight order list and choose the Assign

Driver pushbutton. A dialog box appears in which you can enter drivers. You can decide in the dialog box whether to replace

the currently assigned drivers with new drivers or whether to add drivers to the existing drivers.

You can create a freight order in the transportation cockpit to which you can directly assign one or more drivers as follows:

You can select drivers in the list of drivers and choose the Create Freight Document pushbutton. A dialog box appears in

which you can enter additional data. The system creates a freight document for each driver that you selected in the list of

This is custom documentation. For more information, please visit SAP Help Portal.

260


1/14/26, 2:19 PM

drivers.

In the road freight order hierarchy or in the road freight order list, you can choose the Road Freight Order pushbutton. A

dialog box appears in which you can directly assign drivers to the freight order as soon as they are created.

You can select freight units in the freight unit list and trucks on the Truck tab page in the resources area and choose the

Optimizer Planning pushbutton. The system generates freight orders to which the default driver of the corresponding

resource is automatically assigned. The system considers the driver’s non-working times and absences according to your

capacity availability settings.

In the Freight Orders/Freight Bookings list, you can choose  New

## Road Freight Order

. A dialog box appears in which

you can directly assign drivers to the freight order as soon as they are created.

You can drag and drop drivers from your list of drivers to one or more freight units in the freight unit list. The system then

automatically creates a freight order with the selected freight units that is assigned the selected driver with the vehicle

resource to which it is assigned as the default driver. Alternatively, you can choose the Assign Selected Items pushbutton.

  Note

This function is available only for drivers who are assigned to a vehicle resource as the default driver.

Alternatively, you can assign drivers in the Gantt chart. For more information, see Gantt Chart for Transportation Planning.

In the freight order hierarchy, you can use the standard grouping attribute Driver to display all freight orders that are assigned to a

driver. You can then continue to plan. For example, you can assign all these freight orders to a truck resource or vice versa.

Alternatively, you can display all freight orders for a driver on the geographical map.

If you want to display information about a second driver in the road freight order list, you must select the corresponding fields in

your field catalog. For more information, see Field Configuration for the Transportation Cockpit.

## More Information

For more information about the use of drivers in freight order management, see Use of Drivers in Freight Order Management.

Use of Multiresources

## Use

You can use multiresources, for example, if an unknown number of vehicle resources of a means of transport are available, but you

only want to make the settings for these vehicle resources once. You can define multiresources for vehicle resources and container

resources.

## Restrictions

In the case of schedules, the system takes multiresources into account for the capacity only.

We recommend that you assign a means of transport for which you have selected the Multiresource checkbox to one

vehicle resource only.

Container resources are not taken into account in VSR optimization and for the generation of transportation proposals.

## Prerequisites

This is custom documentation. For more information, please visit SAP Help Portal.

261


1/14/26, 2:19 PM

For vehicle resources, you have selected the Multiresource checkbox in Customizing for your means of transport and have

optionally specified the number of individual resources (Number of Individual Resources field).

For more information, see Customizing for Transportation Management under  Master Data

 Resources

 Define Means

of Transport.

By selecting the Lock Multiresource checkbox for the means of transport, you can prevent multiple planners from using

the multiresource in parallel in multiple sessions. Using the multiresource in multiple sessions can, for example, result in the

maximum number of individual resources being violated.

You have defined a vehicle resource or container resource. To do so, on the SAP Easy Access screen, choose

Transportation Management

 Master Data

## Resource

## Resource . You have assigned a means of transport to your

vehicle resource. You have selected the Multiresource checkbox for your container resource.

In the optimizer settings, you have optionally specified how the system is to react if the number of parallel freight orders

exceeds the number of individual resources of the multiresource. To do this, open the Create Optimizer Settings app on the

launchpad.

## Features

## Vehicle Resources

During VSR optimization, the system assumes that as many vehicle resources exist as you have specified in Customizing in the

Number of Individual Resources field. In accordance with this number, the system can plan parallel freight orders for this vehicle

resource.

If you have not specified a value in Customizing in the Number of Individual Resources field, the system assumes that an

unlimited number of vehicle resources are available. Depending on the settings that you have made in Customizing and in the

optimizer settings, the number of individual resources of a multiresource can be violated.

During manual planning for vehicle resources and container resources, the system checks whether the number of individual

resources of a multiresource is violated. The system only performs this check if the method VSR_CHECK is contained in your

planning controller strategy or if you have selected the pushbutton for checking. The system checks all resources belonging to the

business documents for which you have called the check. During the check, the system interprets the number of individual

resources as maximum. If this number is violated, the system generates an error message.

When it executes the report /SCMTMS/VSR_MULTIRES_CHECK, the system checks whether the number of individual resources

of a multiresource is violated. During the check, the system interprets the number of individual resources as maximum. If this

number is violated, the system generates an error message or an alert.

Only individual resources of vehicle resources and container resources are displayed on the geographical map. Multiresources

cannot be displayed.

Use of Trailers

## Use

You can create, edit, and display trailer units. You can also calculate charges based on trailers.

## Prerequisites

You have configured the relevant settings in Customizing so that you can configure your standard layout for the use of trailers in

the layout settings for the transportation cockpit. Hierarchy type TUTRL is predefined by default for the planning of trailer units. In

This is custom documentation. For more information, please visit SAP Help Portal.

262


1/14/26, 2:19 PM

addition, you can define your own hierarchy types. For more information, see Customizing for Transportation Management under

## Planning

## General Settings

 Define Hierarchical Views for Business Documents .

You have defined a transportation unit type in Customizing. Transportation unit type TRTL is predefined by default for trailer units.

For more information, see Customizing for Transportation Management under  Planning

 Transportation Unit

## Define

Transportation Unit Types .

## Features

## Creation of Trailer Units

You use drag and drop to assign a freight unit to a trailer. The system creates a trailer unit for this trailer. You can continue

planning it by, for example, assigning further freight units.

To couple and uncouple the trailer unit to vehicle resources, you use drag and drop to assign this trailer unit to the freight

order of the selected vehicle resource. The system checks whether the coupling and uncoupling locations exist in both

documents. If there are several coupling and uncoupling locations, you can choose one.

In an alternative scenario, your trailer is not yet assigned to a vehicle resource, but you already want to plan the trailer. We

recommend that you use this procedure, for example, if you have a trailer in the yard and you want to load freight units onto

it. However, at the time of planning, it is not yet clear or it is not important with which vehicle resource the trailer is to be

moved or which route the vehicle resource is to take. In this case, you create a trailer unit as described above. You later

assign the vehicle resource to this trailer unit using drag and drop. The system creates a new freight order for the vehicle

resource and couples the trailer automatically.

You use drag and drop to assign a trailer to an existing freight order. The system creates a new trailer unit and couples the

trailer automatically to the vehicle resource of the existing freight order.

You choose New Trailer Unit. You assign freight units and trailers to this trailer unit in any sequence you prefer. The system

then carries out consistency checks, such as for the following attributes:

Means of transport

Transportation mode

## Carrier

You can create an empty trailer unit and assign a trailer to it in this way, for example. However, you assign the freight units

later on. We recommend that you use this procedure, for example, if you know that the trailer will be picked up the next day

but, at the time of planning, it is not yet clear which goods it is to transport.

You select a trailer and choose Create Trailer Unit. You assign a document type, a source and destination location, and

departure and arrival dates to this trailer unit.

## Editing and Displaying Trailer Units

You can define separate hierarchies for trailer units. For more information, see Use of Hierarchical Views and Use of Profile

and Layout Sets.

You can remove the assignment of a trailer to a vehicle resource by selecting both documents and choosing Remove

Trailer.

  Note
If this pushbutton is not displayed, check your layout.

If you add an additional location for a trailer unit that is already coupled to a vehicle resource, the system automatically

adds it to the freight order for the vehicle resource, since the location sequence for the vehicle resource and the coupled

This is custom documentation. For more information, please visit SAP Help Portal.

263


1/14/26, 2:19 PM

trailer must be identical.

## Charge Calculation Based on Trailers

You consolidate freight units from multiple forwarding orders into a trailer unit and charge the customer based on a standard rate,

the weight of the trailer, or any other criteria. You can maintain a charge line in the forwarding order for the trailer using the

resolution base Resource. You maintain rates for different types of trailers using the Means of Transport calculation base.

## Activities

You create trailer units in the transportation cockpit. To call the transportation cockpit, open the Transportation Cockpit app on

the launchpad.

More Information

## Trailer Unit

Creation and Editing of Transportation Units

Example: Trailer Swap

## Use of Combination Resources

A combination resource is the fixed amalgamation of one vehicle resource and one or more passive vehicle resources that are

coupled in a fixed sequence and are always used together. An example of a combination resource is a tractor with two semi-

trailers.

## Use

Combination resources are an example of vehicle combinations and are different from vehicle-resource combinations. For more

information about the difference between combination resources and vehicle-resource combinations, see Vehicle Resource.

The use of combination resources in planning is especially recommended if you do not have your own fleet. In this case, you can

perform VSR optimization on the level of the combination resource. This means that VSR optimization does not have to deal with

the coupling and uncoupling of the individual components of the combination resource. The trailers are important for load

planning, however. This means that the individual components of the combination resource and their attributes are considered in

load planning.

## Prerequisites

You have defined combination resources in the resource master data. For more information, see Definition of Combination

Resources.

You have also made the following planning-relevant settings in the resource master data:

In the Capacity view, you have defined the planning-relevant capacities for the combination resource (quantities and

weights). These values are important for VSR optimization.

You have also defined additional capacities for the components of the combination resource (length, width, and

height of the loading space).

In the Phys. Properties (Physical Properties) view, you have manually defined the tare weight and the maximum

gross weight not only for the components but also for the combination resource because the system does not

This is custom documentation. For more information, please visit SAP Help Portal.

264


1/14/26, 2:19 PM

automatically aggregate the values of the individual components.

In the Load Optimization view, you have defined axles, empty weight and maximum weight as well as dimensions for

the components of your combination resource. These values are important for load planning and pre-checks in VSR

optimization. For more information, see Master Data in Load Planning.

You have defined incompatibilities in the incompatibility settings of your planning profile (optional). VSR optimization

considers incompatibilities for the combination resource, whereas load planning considers them for the individual

components.

If you want simple load planning checks to be performed for your combination resource during VSR optimization, you must

select the value Partially in the Consider Load Planning field in the optimizer settings of the planning profile. For more

information, see the F1 Help for this field.

## Features

## Single Documents and Transportation Cockpit

In the road freight order, combination resources are marked as such by a corresponding indicator.

The trailers of a combination resource are displayed as local items in the road freight order. However, information about coupling

and uncoupling is displayed on the Overview tab page because trucks and trailers always travel together.

In the transportation cockpit, the resource list shows only the combination resource. You can see the individual components in the

load plan hierarchy, for example.

You cannot plan the components of a combination resource individually, that is, outside of the combination resource. If you want to

do this, you must copy the combination resource, meaning that you have to define it twice. However, you can assign the individual

components to several, different, combination resources.

You also cannot change combination resources in planning. For example, you cannot remove or add a trailer. Similarly, you cannot

change the sequence of the trailers.

If you have your own fleet and want to dynamically couple or uncouple a tractor and trailer, we recommend that you work with

vehicle-resource combinations. VSR optimization can dynamically combine the individual components for vehicle-resource

combinations. This is based on the prerequisite that you have defined means-of-transport combinations in Customizing under

Master Data

## Resources

 Means of Transport and Compartment

 Define Means-of-Transport Combination .

## Load Planning

Combination resources are considered in load planning. The individual components are also displayed here.

During load planning, the system considers incompatibilities between freight units and incompatibilities between freight units and

the truck and its trailers.

Load consolidation is not supported for combination resources.

Related Information

## Load Planning

## Integration of Real-Time Execution Data

In the transportation cockpit, you can display real-time execution data, such as delays or accidents, for freight documents.

This is custom documentation. For more information, please visit SAP Help Portal.

265


1/14/26, 2:19 PM
## Use

Real-time execution data helps you to identify delays during the execution of your transports at an early stage and to adapt the

transportation plan if necessary.

## Prerequisites

You are working with the process controller. Predefined services and the following standard strategies are available for this

function:

TES_D_TM - Real-Time Exec. Data: Delay Determination

TES_R_TM - Real-Time Exec. Data: Resource Pos. Deter.

In the standard system, delays for a specific freight document stage are calculated based on the estimated time of

arrival (ETA). The system derives the ETA of the next stop from the estimated event date of the Delay event, which is

stored in the freight order on the Execution tab page. If you want to have the ETA determined by an external

provider, you must define your own strategy.

The resource position is sent by default for each event to Transportation Management and is considered in TM as the last

reported position of the resource. If you want to have the resource position determined by an external provider, you must

also define your own strategy.

There is no standard strategy for the determination of events. You need to define your own strategy.

  Note

Delays and events can be determined only for freight documents that have the status In Execution.

For more information about the process controller, see Process Controller Configuration.

You have made the following settings in the planning profile:

You have entered the standard strategies or your own strategies.

Optional: You have entered a threshold value starting from which a delay is to be classified as critical and is to be

displayed on the geographical map and in the Gantt chart.

Optional: You have specified how long the real-time execution data is to be kept in the cache.

Optional: You have defined in Customizing how real-time data is to be displayed on the geographical map and in the Gantt

chart. For more information, see Customizing for Transportation Management under:

Basic Functions

## Geographical Map

 Define Layouts for Geographical Map

Basic Functions

## Gantt Chart

 Define Layouts for Gantt Chart

## Features

On the geographical map, you can determine delays by choosing Show Delays in the context menu. All freight document stages

with a delay are marked in a special color. The quick info and the label provide more details about the delay.

You can remove all real-time execution data from the geographical map by choosing Remove Execution Data in the context menu.

For an individual freight document, you can display the reason for the delay by choosing Show Events. The system can determine

and display the following types of events:

## Traffic events, such as accidents or road works

This is custom documentation. For more information, please visit SAP Help Portal.

266


1/14/26, 2:19 PM

Weather events

## Other events

For an individual freight document, you can also determine and display delays by choosing Show Delays in the context menu.

In the Gantt chart, delayed freight documents are marked with a warning icon. The quick info provides more details about the

delay.

## Greenhouse Gas Emissions

Transportation Management (TM) allows you to calculate greenhouse gas (GHG) emissions during manual planning and vehicle

scheduling and routing (VSR) optimization.

GHG emissions cover a range of gases, such as carbon dioxide (CO ) and methane (CH ). These GHG emissions are measured in

2

4

CO  equivalents. On the user interfaces, GHG emissions are simply referred to as CO  emissions.

2

2

## Use

When you assign freight unit stages to a road freight order (FO) manually or by selecting Assign Selected Items, the CO

2

emissions of the road FO are calculated automatically based on the settings that you made in Customizing for your vehicle types.

The same holds true when you use VSR optimization. In this case, the CO2 emissions costs that you defined in your constraints

and costs settings are taken into account in addition.

The calculated CO  emissions with their unit of measure are displayed in the road FO list. The road FO hierarchy (both in the

2

business document and in the transportation cockpit) provides the CO  emissions with their unit of measure on document and on

2

stage level. Using the aggregation row, you can easily identify the total CO  emissions of all road FOs in the transportation cockpit.

2

In the truck list and the equipment types list, you can see the CO  emissions that you have defined in Customizing for your empty
2

and fully loaded vehicles. Further, the CO  emissions per loaded weight are displayed. This value indicates the increase in CO

2

2

emissions per distance if you add one unit of load, such as one ton or kg, to the vehicle. In other words, it describes the gradient of

the linear curve between the CO  emissions per distance of the empty vehicle and the fully loaded vehicle. The formula used is:

2

CO  emissions of the fully loaded vehicle minus CO  emissions of the empty vehicle divided by the capacity, that is the maximum

2

2

allowed weight of the load

Note that the fields in the truck list and equipment types list are not displayed by default but need to be added using

personalization.

You can display the CO  emissions for road FOs on the geographical map. They can be included in the tooltip or as a label. In the

2

Gantt chart, you can also display the CO  emissions for road freight orders in the corresponding list and as a tooltip and a label in

2

the chart panel.

## Prerequisites

You have indicated CO  emissions for your vehicle types. You can indicate CO  emissions both for empty and fully loaded

2

2

trucks and specify a weight and distance unit of measure. Further, you have indicated a payload weight and a corresponding

unit of measure. For more information, see Customizing for Transportation Management under  Master Data

## Resources

## General Settings

 Define Equipment Groups and Equipment Types .

To define the priority of CO  emissions for VSR optimization, you have optionally defined CO  emissions costs per unit of

2

2

measure in your constraints and costs settings using the Edit Constraints and Costs Settings app.

This is custom documentation. For more information, please visit SAP Help Portal.

267


1/14/26, 2:19 PM

If you want to display the CO  emissions as tooltip and label in the chart panel of the Gantt chart, you have made the

2

required settings in Customizing.

For more information, see Gantt Chart for Transportation Planning.

If you want to display the CO  emissions as tooltip and label in the geographical map, you have made the required settings

2

in Customizing.

For more information, see Map Functions.

## Related Information

Constraints and Costs Settings

Customizing for CO2 Emissions Calculation

## Calculation of CO2 Emissions

## Calculation of Distances Traveled With or Without Load

Transportation Management (TM) provides visibility on loaded and empty transportation stages.

## Prerequisites

You have activated the calculation of distances in Customizing for Transportation Management under  Basic Functions

## General Settings

 Define General Settings for TM .

In the field catalogs for the lists and hierarchies for road and rail freight orders as well as trailer, container, and railcar units

and the lists for trailer, container, and railcar unit stages, you have selected the following fields and indicated whether they

are to be displayed by default or using personalization:

Distance (Empty)

Distance (Loaded)

For more information, see Field Configuration for the Transportation Cockpit.

You have added the following fields to the Gantt chart for road and rail freight orders as well as trailer, container, and railcar

units:

Total Distance

Total Distance UoM

Distance (Empty)

Distance (Loaded)

For more information, see Customizing for Transportation Management under  Basic Functions

 Gantt Chart

## Define

Field Lists and Label Schemes for Gantt Chart

.

## Use

TM provides visibility regarding distances that are traveled either with or without load and whether the corresponding

transportation stages are empty or not. This information is available in the corresponding lists and hierarchies of the

transportation cockpit, the Gantt chart, and the single document user interfaces for road and rail freight orders as well as trailer,

container, and railcar units.

This is custom documentation. For more information, please visit SAP Help Portal.

268


1/14/26, 2:19 PM

Based on this information, you are able to do settlement, for example, or measure the efficiency of your fleet by calculating the

ratio of the distance traveled with load and the total distance.

Further, TM provides dedicated key performance indicators (KPI).

The following assumptions are made when it comes to whether a vehicle resource or container is considered empty:

A container is empty if it doesn’t carry any product items or package items.

A trailer is empty if it doesn’t carry any product items, package items, or container.

A truck is empty if it doesn’t carry any product items, package items, or container and doesn’t have a trailer attached to it.

However, a combination resource is considered as empty even though it has a trailer attached to it.

A truck transporting an empty container or having an empty trailer attached to it across a stage is considered as follows:

From the truck’s viewpoint, the stage is not empty.

From the container’s and the trailer’s viewpoint, the stage is empty.

## Related Information

Key Performance Indicators in the Transportation Cockpit

Customer-Specific Functions

## Use

You can use this function to access planning data and to model your own planning processes, such as the following:

Visually represent freight orders and freight units

Remove forwarding orders from planning

Add freight units to freight orders

## Prerequisites

You have defined at least one strategy of your own and at least one method of your own, and have assigned this method to

your strategy. For more information about the process controller, see Customizing for Transportation Management under

## Planning

## General Settings

 Configure Process Controller for Planning .

You have defined a customer-specific function and have assigned your strategy to this function. For more information, see

Customizing for Transportation Management under  Planning

## General Settings

 Define Customer-Specific Functions

for Planning .

## Features

You model your planning processes using strategies that consist of one or more methods. Each method represents an individual

planning step. The process controller is the framework used for defining strategies and methods.

Once you have defined customer-specific functions in Customizing and assigned a strategy to each of them, these functions are

automatically available for selection on the user interface for transportation planning. When you choose a function, the system

automatically performs the corresponding planning steps.

This is custom documentation. For more information, please visit SAP Help Portal.

269


1/14/26, 2:19 PM

For this, the process controller passes the planning request object /SCMTMS/CL_CUS_REQUEST or a customer-specific object

derived from it, on through the methods. You can enhance your customer-specific object with your own data.

You can specify a request object class in Customizing. This class must be derived from the /SCMTMS/CL_CUS_REQUEST class. If

you do not specify a class, the system uses the /SCMTMS/CL_CUS_REQUEST class. For more information, see Customizing for

Transportation Management under  Planning

## General Settings

 Define Customer-Specific Functions for Planning .

## Activities

To perform transportation planning using customer-specific functions, open the Transportation Cockpit app on the launchpad

and then start planning. Use the corresponding pushbutton to choose the customer-specific function you want to perform.

## More Information

Process Controller Configuration

Parallel Planning

## Use

In manual planning and in VSR optimization, multiple planners can work simultaneously. If there are conflicts with dates or times,

the system issues a message.

## Features

If several planners access the same object in manual planning or in VSR optimization, such as a resource or a schedule, the system

issues a message that the object is locked. For multiresources, you can specify whether the multiresource is to be locked for the

means of transport.

If several planners perform separate pre-carriage, main carriage, or on-carriage planning and unplanned stages exist (for example,

because you specified that only the route is to be copied when transportation proposals are generated), VSR optimization creates

new stages and tries to adjust the dates and times of the stages to the ones determined in the transportation proposal. If a planner

plans a stage (such as the main carriage) manually and a planned freight order or freight booking exists, the system copies the

dates and times to the predecessor and successor stage. It considers them a hard constraint (acceptable values). If

inconsistencies occur, for example, because acceptable dates overlap, the system issues a message. If two planners plan a freight

unit at the same time, for example, pre-carriage and main carriage, and conflicts arise, the system also issues a message. For time

conflicts, the system sets the appropriate planning status for the freight unit stage (see Explanation of Statuses of Business

Documents).

  Recommendation

We recommend that you first plan stages that are critical in terms of date and time, and then the remaining stages.

## Definition of Carriers

Transportation Management (TM) offers various options for defining or determining carriers for business documents.

Planning offers the following options:

## Carrier determination

This is custom documentation. For more information, please visit SAP Help Portal.

270


1/14/26, 2:19 PM

The system determines a unique carrier based on a set of simple rules that you define in the carrier determination profile.

Carrier determination is supported for freight units, freight orders, and consignment orders.

For more information, see Carrier Determination.

## Carrier selection

The system assigns the carrier with the lowest costs based on specific constraints to a given freight document. Carrier

selection can be performed manually or automatically. It takes into account your carrier selection settings.

Carrier selection creates a ranking list of all available and relevant carriers based on decision criteria. You can then

manipulate the ranking list according to your needs. Finally, the carrier that is ranked first can be assigned to the freight

document automatically or manually or the result can be used in a subsequent tendering process.

Carrier selection is supported for freight orders and freight bookings.

For more information, see Carrier Selection.

In addition, the following options are available in TM:

## Manual definition

You can manually enter a carrier in the transportation cockpit for freight units, freight orders, freight bookings, and

consignment orders. In addition, you can manually enter the carrier for freight units, freight documents, and consignment

orders on the respective user interfaces.

## Direct shipment options

Direct shipment options can be determined automatically for freight units during creation or can be generated manually for

a freight unit on the user interface based on the freight unit type. Direct shipment options are generated for each

carrier/service level combination based on a freight agreement. The costs for the direct shipment options come from

charge management. Direct shipment options take into account your settings in the carrier selection settings.

Direct shipment options are supported for freight units.

For more information, see Determination of Direct Shipment Options.

## Carrier propagation

The carrier is propagated from a predecessor document, such as the delivery, into the first TM document, between TM

documents, and from the top-level TM document into the predecessor document.

## Using the carrier from the schedule

When you create a freight document based on a schedule, the carrier of the schedule is copied into the freight document.

For more information, see Schedule.

## Default route

A default route can be applied to requirement documents (freight units or transportation units) and impose a carrier

constraint per stage of the default route.

For more information, see Default Route.

## Freight tendering

The freight tendering process can be used to tender freight orders to one or more carriers.

Tendering is performed based on a tendering profile. In this profile, you define the individual steps of the tendering process.

For example, you can specify the tendering type, such as peer-to-peer or broadcast tendering, the tendering process based

on request for quotation or direct, the relative price limit, or the maximum response time.

This is custom documentation. For more information, please visit SAP Help Portal.

271


1/14/26, 2:19 PM

When a suitable and valid carrier is found and made responsible for execution, the respective carrier is stored on freight

order root level.

For more information, see Freight Tendering.

## Carrier Determination

Carrier determination lets you automatically determine a carrier for freight units, consignment orders, and freight orders based on

simple rules.

## Prerequisites

You have defined a carrier determination profile.

In your carrier determination profile, you define determination rules. A determination rule consists of a number of

document attributes that are used to determine a unique carrier, such as gross weight, source and destination location, or

transportation mode. Note that some of these fields need to be made visible using personalization. If data is available in

hidden fields, a corresponding warning is displayed in a dedicated field of the affected determination rule.

There are checks in place that prevent duplicate entries and unreachable determination rules.

You can download your carrier determination profile as a spreadsheet or upload a spreadsheet to your carrier

determination profile.

Finally, you can simulate carrier determination either by a specific business document or by document attributes, such as

source and destination location, gross weight, or transportation group. You can see which carrier the system would choose

based on which rule.

To define carrier determination profiles, open the Create Carrier Determination Profile app from the launchpad.

You have activated carrier determination by assigning your carrier determination profile to your business document type in

Customizing. For more information, see Customizing for Transportation Management under:

Freight Order Management

## Freight Order

 Define Freight Order Types

Freight Order Management

## Consignment Order

 Define Consignment Order Types

Planning

## Freight Unit

## Define Freight Unit Types

If you want to display information messages about which carrier was determined and when a carrier was changed in the

application log, you have defined message settings in Customizing. For more information, see Customizing for

Transportation Management under  Basic Functions

## User Interface

 Define Message Settings .

## Features

Carrier determination is performed automatically after creation or update of a business document (that is, a freight unit,

consignment order, or freight order). The system first evaluates whether the document is relevant for triggering carrier

determination. Based on the assigned carrier determination profile, it checks whether relevant data was changed on root, item, or

stop level. In a second step, the system determines or redetermines the carrier if necessary. To do this, it evaluates the

determination rules of the assigned carrier determination profile from top to bottom according to the specified processing

sequence. It applies the first matching determination rule and assigns the specified carrier to the business document. If no carrier

is defined in this rule, it is also a valid result. If none of the rules match, the system takes the carrier from the predecessor

document.

You can manually change the carrier in the business document. Note, however, that a manually changed carrier won't be changed

by carrier determination anymore. Similarly, a carrier determined by carrier selection won't be changed by carrier determination

This is custom documentation. For more information, please visit SAP Help Portal.

272


1/14/26, 2:19 PM

anymore.

The Business Add-In (BAdI) Enhancements for Carrier Determination (/SCMTMS/EX_TSPD) allows you to do the following:

Adjust the carrier determination profile to be used for a given business document, for example, to activate or deactivate

carrier determination for certain business documents

Adjust the decision on whether a redetermination is needed, for example, to react to other changes in a custom

determination

## Adjust the determined carrier, for example, to create a custom determination

In the application log, you can see the processing relevance of business documents. Further, it shows the carrier determination

results, including the determination rule that was used. Finally, the log shows adjustments made by the BAdI.

  Note

Carrier determination is performed on document level only.

Only the first and the last stop are evaluated.

Carrier Selection

## Use

You can use carrier selection to assign a suitable carrier to your subcontractable business documents (for example, freight orders

or freight bookings) either manually or automatically. The aim is to find a carrier with the lowest costs under consideration of

constraints.

Prerequisites

## Basic Settings

You have defined transportation lanes in the master data and, in doing so, you have defined means of transport and carriers,

including carrier profiles (optional).

## Optimization Options

You use one or more of the following optimization options:

Strategies (only relevant to automatic carrier selection)

## Costs

## Priority

For more information, see Strategies.

## Continuous Move

For more information, see Continuous Move.

Business share (only relevant to automatic carrier selection)

For more information, see Business Share.

This is custom documentation. For more information, please visit SAP Help Portal.

273


1/14/26, 2:19 PM

Check against transportation allocations (relevant to both automatic carrier selection and manual carrier selection).

For more information, see Check Against Transportation Allocations.

## Detailed Settings

In Customizing, you have specified that your business document types (for example, freight order types) are relevant to

subcontracting. For more information see, for example, for freight orders, Customizing for Transportation Management

under  Freight Order Management

## Freight Order

 Define Freight Order Types .

You have made further settings in the carrier selection settings. In the carrier selection settings, you define, for example,

the process in which carrier selection is to be executed:

Regular carrier selection

Tendering (see Freight Tendering)

Determination of direct shipment options (see Determination of Direct Shipment Options)

To make the carrier selection settings, open the Create Carrier Selection Settings app on the launchpad.

If you want to consider external freight charges during carrier selection, you have to specify in the settings for carrier

selection that you want charges from charge management to be considered. In this case, you must configure charge

management accordingly (see Charge Management and Service Product Catalogs).

## Features

## Manual Carrier Selection

In manual carrier selection, you manually assign the required carrier to your business documents. If you have configured the check

against transportation allocations, the system takes into account and checks transportation capacities (transportation

allocations) that you have defined for the individual carriers. If, during the allocation, the system finds relevant transportation

allocations without capacity or transportation allocations are violated by the allocation, warning messages appear.

## Automatic Carrier Selection

A separate optimization is available for the automatic carrier selection. It takes into account the selected optimization options

when determining the most cost-effective carrier for all business documents that you have selected. If none of the carriers are

available, the system does not assign a carrier to the relevant business documents.

Note that automatic carrier selection does not support consignment orders.

## Determining Available Carriers

In this case, the system determines all available carriers. If you have specified in the carrier selection settings that transportation

allocations are not to be considered, even those carriers without any free capacity are displayed.

## Business Documents with Multiple Stops

In the case of business documents with multiple stops, the system tries to find a direct transportation lane between the source

and destination locations and uses it as the starting point for the determination of available carriers.

  Example

A freight order goes from A via B and C to D. In the carrier selection settings, you have selected the checkbox for overall carrier

availability.

This is custom documentation. For more information, please visit SAP Help Portal.

274


1/14/26, 2:19 PM

The system determines the most concrete transportation lane (using the same technique as for strategy determination) for

each stage (A to B, B to C, and C to D). The result is a list of all possible carriers for each stage. The system also uses strategy

determination to determine the strategy for the main carriage (direct connection from A to D). The result is a list of possible

carriers. The system now creates the intersection from all these lists. The result is no carriers, one carrier, or multiple carriers

that can serve all the stages including the main stage. The consideration of stages and stops is used therefore as a filter.

The system first checks which carriers cover all the stages of the freight order (A to B, B to C, and C to D). In a second step, the

system chooses the carrier from those found in the first step with a direct transportation lane between A and D.

If you have not selected the checkbox for overall carrier availability in the carrier selection settings, the system uses strategy

determination to determine the strategy for the main stage only.

SAP delivers the standard planning strategy TSPS_DEF for carrier selection. You can specify this strategy in the carrier selection

settings. SAP also delivers the standard planning strategy VSR_1STEP. For more information, see One-Step Planning and Planning

Strategies.

## Activities

To call carrier selection, open the Carrier Selection app on the launchpad.

First, a user interface is displayed where you can define profile and layout sets. For more information, see Use of Profile and

Layout Sets.

To perform carrier selection in the background, schedule report /SCMTMS/TSPS_OPT_BGD. For more information, see

Selection of Carriers.

More Information

Full Map Display

Strategies

## Use

Strategies are optimization options for the carrier selection. The system takes into account strategies during the automatic carrier

selection. You define strategies either in the transportation lane or in carrier selection settings. In the first case, the system

considers the appropriate transportation lane for each freight order. This allows it to consider different settings in one run.

## Features

You can choose one of the following strategies or a combination of these strategies:

## Priority

The system determines the carrier on the basis of a priority that you have defined. This means that the system chooses the carrier

with the highest priority first from the transportation lane, taking into account the various restrictions.

## Costs

The system determines the carrier on the basis of the lowest total costs. You can take into account either internal costs or charges

calculated in charge management:

This is custom documentation. For more information, please visit SAP Help Portal.

275


1/14/26, 2:19 PM

## Internal costs

Transportation costs and carrier costs that you define for your carriers:

You define transportation costs per business document, for example, freight order (EA), weight, or volume.

You define carrier costs per kilometer or mile.

You can define internal costs in the transportation lane (see Transportation Lane) and, in the case that no internal costs are

defined in the specific transportation lane, you can define them in the carrier profile (see Carrier Profile).

  Note

The costs used here are not real costs. They are simply internal costs that are used for weighting.

## Charges Calculated in Charge Management

You have to create a charge calculation that is set up in charge management. For more information, see Charge

Management and Service Product Catalogs.

For more information about how the system takes into account strategies during the carrier selection, see Strategy Determination.

## Activities

1. Choose the required strategy for the means of transport in the transportation lane or in the carrier selection settings.

To choose the required strategy in the transportation lane, open the Define Transportation Lane app on the launchpad.

To choose the required strategy in the carrier selection settings, open the Create Carrier Selection Settings app on the

launchpad.

2. If you want to use priorities, define the required priorities for the individual carriers in the transportation lane.

3. If you want to use internal costs, define transportation costs and carrier costs for the individual carriers either in the

transportation lane or in the carrier profile.

## Strategy Determination

The system tries to find the transportation lane that, out of all the transportation lanes that are relevant for the carrier selection,

most closely corresponds to the business document (for example, freight order) . For more information, see Transportation Lane.

  Example

You have defined the following transportation lanes:

## Transportation lane between source location A and destination location B

Transportation lane between source location A and destination transportation zone B’ (contains destination location B)

Location Transportation Lane at source location A

The freight order is to go from A to B. In this case, the system chooses the transportation lane between source location A and

destination location B. This is the most concrete transportation lane, since it runs between two specified locations. The

transportation lane between source location A and destination transportation zone B’ is less concrete since a transportation

zone can contain multiple locations. The location transportation lane at A is also less concrete since a transportation lane

between two locations is more concrete that a location transportation lane. Using the strategy that you have defined for this

transportation lane, the system determines the carrier.

This is custom documentation. For more information, please visit SAP Help Portal.

276


1/14/26, 2:19 PM

The system takes into account the carriers in the transportation lane only. If you have a freight order with multiple stops, you

can use these stops as an additional filter. For more information, see Carrier Selection.

Continuous Move

## Use

Continuous moves are optimization options for carrier selection. The system takes into account continuous moves during

automatic carrier selection only.

## Prerequisites

You have set the Continuous Move checkbox in the carrier profile of the suppliers. You define a carrier profile on the SAP

Easy Access screen under  Logistics

 Transportation Management

## Master Data

 Transportation Network

## Define

Carrier Profile . For more information see Carrier Profile.

You have made the settings relevant to the continuous move in the carrier selection settings or in the transportation lanes.

To define the settings for carrier selection, open the Create Carrier Selection Settings app on the launchpad. For more

information, see Transportation Lane.

## Features

As part of automatic carrier selection, the system tries to combine subcontractable business documents (for example, freight

orders) by forming continuous moves. The aim is to reduce the costs of the business documents by assigning additional business

documents to a carrier. The following types of continuous moves are available:

Simple continuous move: The carrier accepts one or more additional business documents and, after executing the first

business document, directly executes the following business documents one after the other.

Round trip: A round trip is a simple continuous move for which the following additional prerequisites must be met: The

source location of the first business document and the destination location of the second business document are identical.

A round trip can only consist of exactly two business documents.

  Note

The system cannot take into account complex round trips where multiple source locations (pickup) or destination locations

(delivery) are served.

The system can combine two or more business documents in a continuous move if the following conditions are met:

The relevant carrier is available for both business documents.

The arrival date/time of the first business document lies in the departure window of the second business document.

The departure date/time of the second business document lies in the arrival window of the first business document.

The system performs a check of incompatibilities for the business documents if you have activated this function in the settings for

carrier selection.

Furthermore, the distance between the destination location of the first business document and the source location of the second

business document must not exceed the smaller maximum distance that you have defined for the carrier in the transportation

lanes.

This is custom documentation. For more information, please visit SAP Help Portal.

277


1/14/26, 2:19 PM

The system checks the type of continuous move. In the case of a round trip, the system checks if the destination location of the

first business document and the source location of the second business document are identical, for example. In the case of a

simple continuous move, the system can combine multiple business documents without the vehicle having to return to the source

location.

For more information, see Cost Calculation for Continuous Moves.

## Activities

1. Choose the continuous move type for the means of transport in the Contin. Move Type field of the transportation lane.

2. Define the following values, as required, for the individual carriers:

Arrival and departure windows

Maximum distance

## Discount

## Cost Calculation for Continuous Moves

The system first determines the costs per business document (for example, freight order). Here it considers the strategy and

origin of the carrier costs that you defined in the carrier selection settings. The system then determines the discount per business

document. When doing so, it takes into account the settings that you have made in the transportation lane for the carrier and the

means of transport. The system deducts this discount from the costs determined previously for each business document.

  Example

You have defined the following data:

Carrier A is to receive a discount of 10% on the transportation lane A->B for means of transport 0001.

Carrier A is to receive a discount of 20% on the transportation lane B->C.

There are two freight orders (FRT1 for A->B and FRT2 for B->C). The costs for FRT1 are 1000, the costs for FRT2 are 2000. The

optimizer has determined that both freight orders are suitable for a continuous move.

The optimizer now calculates costs of 900 (1000 minus 10%) for FRT1 and 1600 (2000 minus 20%) for FRT2. If the optimizer

were to assign the continuous move to carrier A, the total costs would therefore be 2500. The optimizer compares these costs

with carrier B, for example, who offers lower costs for each freight order (for example, 950 for FRT1 and 1800 for FRT2). If the

optimizer were to assign the continuous move to carrier B, the total costs for the continuous move would then be 2750.

Therefore, the best solution is to assign both freight orders as a continuous move to carrier A.

## Recalculation of Costs from Charge Management

If you specified in the carrier selection settings that the system is to perform a recalculation of costs from charge management for

continuous moves, the system considers the discounts for continuous moves for the business documents from charge

management in the recalculation, however, only for the carriers that offer continuous moves. The system saves the result in the

ranking list. For more information, see Charge Management and Service Product Catalogs.

## Business Share

This is custom documentation. For more information, please visit SAP Help Portal.

278


1/14/26, 2:19 PM
## Use

Business shares are optimization options for the carrier selection. The system takes into account business shares during the

automatic carrier selection.

## Prerequisites

You have defined business shares. To do this, open the Create Business Shares app on the launchpad.

## Features

For each business share, you can define tolerances as well as penalty costs that the optimizer calculates when an excess or

shortfall of the target value plus or minus these tolerances occurs. However, the penalty costs are not real costs, but instead are

used for weighting purposes only.

  Recommendation

It only makes sense to use business shares if you have defined penalty costs. We recommend that you also always define

tolerances to give the optimizer a certain amount of leeway.

The optimizer takes into account the following when assigning the carriers in accordance with the defined business shares:

## Transportation zone hierarchies

Hierarchical relationships between means of transport

## Historical business shares

## Documents to which a carrier has not yet been assigned

In the tendering profile, you can define whether the system, when it is checking the target value of a business share or

allocation, includes only the business documents already assigned to the relevant business share or allocation or whether it

also includes the corresponding freight requests during carrier selection. For more information, see the system

documentation.

  Example

Carrier A is to receive 50% of all freight orders that are transported from source location DC_FRANKFURT with any means of

transport of the transportation mode Street in June 2010.

## More Information

Creation of Business Shares and Transportation Allocations

Creation of Business Shares and Transportation Allocations

## Use

You can use this function to create business shares and transportation allocations. The system uses business shares and

transportation allocations during carrier selection or for capacity management in the air cargo scenario, for example.

## Prerequisites

This is custom documentation. For more information, please visit SAP Help Portal.

279


1/14/26, 2:19 PM

You have configured the transportation allocation settings in Customizing – for example, you have activated the use of

transportation allocations and business shares. For more information, see Customizing for Transportation Management under

## Planning

## General Settings

 Define Transportation Allocation Settings .

## Features

## Creation of Trade Lanes

You need trade lanes both for business shares and transportation allocations. A trade lane comprises the following:

Geography, that is, a combination of zones or locations (see Use of Transportation Orientations)

Means of transport or transportation mode (optional)

  Example

Examples of trade lanes include:

All transports from Hamburg to New York

All transports within Germany

## All transports that leave Bavaria

You can use trade lanes to define geographical data with different degrees of detail. Furthermore, you can work with placeholders.

Each business share and each transportation allocation is only valid for exactly one trade lane.

  Note

Trade lanes do not represent connections between objects in the transportation network, for example, locations or

zones. They are a context-independent classification of any transportation-related activities.

Trade lanes can form a hierarchy. This means that more generic trade lanes can contain more specific trade lanes (for

example, Within Germany Using Means of Transport Truck contains Along the Way from Frankfurt to Hamburg with

Means of Transport Refrigerated Truck and Within Bavaria with Means of Transport Truck for Liquids.

Trade lanes may overlap, for example, From Germany Using Airplane and Within Europe Using Airplane.

Trade lane hierarchies contain the following:

Transportation zone hierarchies, for example, From Germany contains From Bavaria, and this contains From

## Plant_MÜNCHEN

Hierarchical relationships between means of transport, for example, Within Germany Using Means of Transport

Truck contains Within Germany Using Means of Transport Refrigerated Truck

Means of transport/transportation mode relationship, for example, Within Germany Using Transportation Mode

Street contains Within Germany Using Means of Transport Refrigerated Truck

## Creation of Business Shares

When you create a business share, you define the following:

## Creation options

This is custom documentation. For more information, please visit SAP Help Portal.

280


1/14/26, 2:19 PM

You can specify, for example, whether a business share is to refer to a transportation lane, that is, is only to be created if the

corresponding transportation lane already exists. Additionally, you can specify whether time buckets can be overwritten.

Trade lane (see above)

## Business share details

Here you define, among other things, tolerances and penalty costs that are incurred when an excess or shortfall of these

tolerances occurs. You also define the unit for your target value.

## Target value

Here you define the actual business shares, for example, 40 % for carrier A and 60 % for carrier B.

You can use this user interface for mass creation. You can create, for example, a daily time bucket for a whole year.

## Creation of Transportation Allocations

When you create a transportation allocation, you define the following:

## Creation options

You can specify, for example, whether a transportation allocation is to refer to a transportation lane and whether time

buckets may be overwritten.

Trade lane (see above)

## Scope of transportation allocation

Here you enter, for example, the planning period (yearly, weekly, and so on). You are free to choose the start of the planning

period. For example, you can define a bucket from Monday 14:00 until Tuesday 14:00.

## Buckets

Here you can define, for example, a sub-bucket distribution. If a carrier can only deliver, for example, in the morning, you

can define two sub-buckets (Morning and Afternoon) for the bucket Daily. As the percentage of the assigned business

documents (for example, freight orders), you define 100% for Morning and 0% for Afternoon.

In addition, you can specify the minimum and maximum product allocation quantity.

Furthermore, you can create multiple transportation allocations by defining specific parameter combinations, for which you can

define specific creation options. You can specify, for example, whether a transportation allocation is to refer to a transportation

lane, that is, is only to be created if the corresponding transportation lane already exists. Additionally, you can specify whether

time buckets can be overwritten.

## Activities

To create business shares, open the Create Business Shares app on the launchpad.

To create carrier selection allocations, open the Create Transportation Allocation app on the launchpad.

To create flight schedule-based allocations, open the Edit Schedule app on the launchpad. You then choose the “Create

Transportation Allocation” pushbutton in your master flight schedule. You can access and edit the transportation allocation from

your personal object worklist (POWL). To do this, open the Transportation Allocations app on the launchpad.

To create air freight agreement allocations, open the Edit Freight Agreement app on the launchpad. You can now create a

transportation allocation at item level in your freight agreement, assuming you have previously defined a corresponding trade lane.

This is custom documentation. For more information, please visit SAP Help Portal.

281


1/14/26, 2:19 PM

Additionally, you can upload allocations from an external data source to Transportation Management (TM) by executing report

/SCMTMS/TAL_IMPORT. If there are changes in existing buckets of allocations, you can adapt these buckets with this report, too.

You call the report from the SAP Easy Access screen under  Transportation Management

 Administration

 Background

## Processing

 Allocation Upload . Alternatively, you can upload allocations in the Allocations worklist and in the allocation UI.

More Information

Carrier Selection

## Transportation Allocation

Check Against Transportation Allocations

Check Against Transportation Allocations

## Use

The check against transportation allocations is an optimization option that you can use as part of both the manual and automatic

carrier selection.

In the check against transportation allocations, you assign transportation capacities (transportation allocations) to carriers for a

certain period. You can define the following:

The maximum number of business documents (for example, freight orders) for a carrier per transportation lane or free

transportation lane for a certain period (day, week, month, quarter, or year), validity, and a certain means of transport. You

define this by entering quantity unit EA for the transportation allocation.

## An allocation unit and quantity unit for each transportation allocation

The minimum number of business documents that defines the number of agreed business documents per period (day,

week, or month) and validity.

## Prerequisites

You have made the settings for transportation allocations in Customizing, for example, you have activated the use of

transportation allocations. For more information, see Customizing for Transportation Management under  Planning

## General Settings

 Define Transportation Allocation Settings .

You have defined carrier selection allocations. To do this, open the Create Transportation Allocation app on the launchpad.

In the carrier selection settings, you have defined whether you want to use transportation allocations or whether the

system is to consider the settings for the transportation lane. In the second case, you must have marked the Use Transp.

Allocations checkbox for your means of transport.

## Features

The system checks all relevant transportation allocations during the check against transportation allocations. This means that you

can define restrictions.

  Example
You have defined the following capacities (transportation allocations):

This is custom documentation. For more information, please visit SAP Help Portal.

282


1/14/26, 2:19 PM

Transportation allocation belonging to a freight order from source location A to destination location B (maximum

quantity = 3 EA). This is the most specific transportation allocation since the freight order runs between two specific

locations (direction Along).

Transportation allocation that belongs to a freight order from source transportation zone A’ and destination

transportation zone B’ (maximum quantity = 10 EA)

Transportation allocation for source location A (maximum quantity = 10 EA). This is the least specific transportation

allocation.

The system can only assign capacities if capacities are free in all of the transportation allocations (you can override this in

manual planning). In this case, the system can assign, at the most, three business documents between A and B even if a greater

capacity is available for the transportation allocation between the source and destination transportation zones, and at the

source location. The reason for this assignment is that the system takes into account the lowest available capacity.

The system also takes into account transportation zone hierarchies and hierarchies between means of transport. You define

hierarchies between means of transport by specifying higher-level means of transport when defining means of transport. This

means that you can also use hierarchical relationships to define restrictions, since the system takes into account the

transportation allocations in all higher-level means of transport.

## More Information

## Transportation Allocation

Creation of Business Shares and Transportation Allocations

Transportation Allocation

## Definition

You can store information about transportation allocations of carriers in geographical areas with specific means of transport or

about specific departures of a schedule. A transportation allocation defines constraints on the minimum or maximum quantity

available within a certain bucket and stores the assigned quantities.

Transportation Management distinguishes between three transportation allocation types:

## Air freight agreement allocation

Stores information about transportation allocations of carriers that act as constraints for air freight agreements. You can

create air freight agreement allocations directly from an air freight agreement.

## Carrier selection allocation

Stores information about transportation allocations of carriers in a specific trade lane. The system uses carrier selection

allocations when optimizing the carrier selection.

## Flight schedule-based allocation

Stores information about transportation allocations of carriers at schedule departure level in a master flight schedule. You

can create flight schedule-based allocations directly from a master flight schedule.

If changes are made to the departure times and arrival times of the schedule departures in the corresponding master flight

schedule, and if these no longer match the bucket-from date and bucket-to date of a period in your flight schedule-based

allocation, the system changes the status of the referenced data for the corresponding period from Data Is Up-to-Date to

Data Is Not Up-to-Date.

This is custom documentation. For more information, please visit SAP Help Portal.

283


1/14/26, 2:19 PM

If the bucket-from date and the bucket-to date of your period are no longer current, you can update them directly in the

period. To do so, choose Update from Schedule.

If the schedule to which you refer from your flight schedule-based allocation creates new departures, you can add a period

to your allocation that contains the dates and times of the new departures of the corresponding schedule. To do so, choose

## Add Bucket

 From New Sched. Dep.

.

You can use transaction WUF to display a list of schedules and schedule-based allocations that reference a specific

schedule.

  Note
If you have defined multiple buckets for a schedule departure and execute report /SCMTMS/MP_SCHED_CREATE_TOR

to generate air freight bookings, the system creates a separate air freight booking for each bucket.

You can define transportation allocation types in Customizing. For more information, see Customizing for Transportation

Management under  Planning

## General Settings

 Define Transportation Allocation Types .

For more information about creating transportation allocations, see Creation of Business Shares and Transportation Allocations.

  Note

You can enter multiple capacity units and units of measure in parallel for all transportation allocation types. Carrier selection,

however, takes just one unit into account for each transportation allocation. You therefore need to specify for carrier selection

allocations in Customizing which unit is to be taken into account during carrier selection.

For example, you can specify a maximum weight of 500 tons and a maximum volume of 45 cubic meters for a transportation

allocation. If you have already planned 500 tons and 40 cubic meters of this transportation allocation, you cannot use this

allocation further. If you have defined cubic meters as the relevant unit for carrier selection, however, carrier selection ignores

the weight that has been fully used up and determines that five cubic meters of capacity are still available.

When you create transportation allocation types, you can specify whether a particular transportation allocation type is to use

attributes or carrier selection.

The following attributes can be used, for example:

Shipping type, such as unit load device

Each shipping type is assigned to a transportation mode.

## Contract basis

You can create just one freight booking for each shipping type/contract basis combination.

## Periodicity

Depending on the transportation allocation type, you can specify various periodicities, such as daily, monthly, or departure

of a schedule.

## Handling code

You can define buckets with handling codes for a transportation allocation. Within the validity period for a transportation

allocation, you can define a number of buckets with different handling codes in parallel. For more information about

handling codes, see Handling Codes.

  Example

You create a flight schedule-based allocation from a master flight schedule for which you define two buckets. One

bucket has the handling code Upper Deck and the other period has the handling code Lower Deck. If you now generate

This is custom documentation. For more information, please visit SAP Help Portal.

284


1/14/26, 2:19 PM

an air freight booking with the handling code Upper Deck from this master flight schedule, the system assigns the air

freight booking to the bucket with the corresponding handling code automatically.

You can create a transportation allocation with the handling code Dangerous Goods in the same way. Any air freight

bookings that you post to this transportation allocation must also have Dangerous Goods as the handling code.

## Integration

Business documents (for example, freight orders) do not have a direct link (cross-business-object association) to the

transportation allocation. However, if you change business document details that are relevant for the transportation allocation

process, the system transfers the corresponding information to the transportation allocations. Relevant changes can be, for

example:

The assignment of a carrier to a business document

The cancellation of a business document that has a carrier assigned to it

## Changes to the quantities

When you assign a carrier to a business document, the system books existing transportation allocations if the following data

concurs in the business document and the existing transportation allocations:

Source and destination

Means of transport

## Carrier

Requested dates (The system does not consider accepted dates.) In the case of overlapping periods, start and end dates

are required.

  Note

If you create a booking for a specific schedule departure, the system also posts the relevant bucket of the transportation

allocation assigned to the schedule, assuming you have previously made this assignment.

The system stores references to business documents in allocated capacities.

## More Information

Creation of Business Shares and Transportation Allocations

Check Against Transportation Allocations

Creation of Business Shares and Transportation Allocations

## Use

You can use this function to create business shares and transportation allocations. The system uses business shares and

transportation allocations during carrier selection or for capacity management in the air cargo scenario, for example.

## Prerequisites

This is custom documentation. For more information, please visit SAP Help Portal.

285


1/14/26, 2:19 PM

You have configured the transportation allocation settings in Customizing – for example, you have activated the use of

transportation allocations and business shares. For more information, see Customizing for Transportation Management under

## Planning

## General Settings

 Define Transportation Allocation Settings .

## Features

## Creation of Trade Lanes

You need trade lanes both for business shares and transportation allocations. A trade lane comprises the following:

Geography, that is, a combination of zones or locations (see Use of Transportation Orientations)

Means of transport or transportation mode (optional)

  Example

Examples of trade lanes include:

All transports from Hamburg to New York

All transports within Germany

## All transports that leave Bavaria

You can use trade lanes to define geographical data with different degrees of detail. Furthermore, you can work with placeholders.

Each business share and each transportation allocation is only valid for exactly one trade lane.

  Note

Trade lanes do not represent connections between objects in the transportation network, for example, locations or

zones. They are a context-independent classification of any transportation-related activities.

Trade lanes can form a hierarchy. This means that more generic trade lanes can contain more specific trade lanes (for

example, Within Germany Using Means of Transport Truck contains Along the Way from Frankfurt to Hamburg with

Means of Transport Refrigerated Truck and Within Bavaria with Means of Transport Truck for Liquids.

Trade lanes may overlap, for example, From Germany Using Airplane and Within Europe Using Airplane.

Trade lane hierarchies contain the following:

Transportation zone hierarchies, for example, From Germany contains From Bavaria, and this contains From

## Plant_MÜNCHEN

Hierarchical relationships between means of transport, for example, Within Germany Using Means of Transport

Truck contains Within Germany Using Means of Transport Refrigerated Truck

Means of transport/transportation mode relationship, for example, Within Germany Using Transportation Mode

Street contains Within Germany Using Means of Transport Refrigerated Truck

## Creation of Business Shares

When you create a business share, you define the following:

## Creation options

This is custom documentation. For more information, please visit SAP Help Portal.

286


1/14/26, 2:19 PM

You can specify, for example, whether a business share is to refer to a transportation lane, that is, is only to be created if the

corresponding transportation lane already exists. Additionally, you can specify whether time buckets can be overwritten.

Trade lane (see above)

## Business share details

Here you define, among other things, tolerances and penalty costs that are incurred when an excess or shortfall of these

tolerances occurs. You also define the unit for your target value.

## Target value

Here you define the actual business shares, for example, 40 % for carrier A and 60 % for carrier B.

You can use this user interface for mass creation. You can create, for example, a daily time bucket for a whole year.

## Creation of Transportation Allocations

When you create a transportation allocation, you define the following:

## Creation options

You can specify, for example, whether a transportation allocation is to refer to a transportation lane and whether time

buckets may be overwritten.

Trade lane (see above)

## Scope of transportation allocation

Here you enter, for example, the planning period (yearly, weekly, and so on). You are free to choose the start of the planning

period. For example, you can define a bucket from Monday 14:00 until Tuesday 14:00.

## Buckets

Here you can define, for example, a sub-bucket distribution. If a carrier can only deliver, for example, in the morning, you

can define two sub-buckets (Morning and Afternoon) for the bucket Daily. As the percentage of the assigned business

documents (for example, freight orders), you define 100% for Morning and 0% for Afternoon.

In addition, you can specify the minimum and maximum product allocation quantity.

Furthermore, you can create multiple transportation allocations by defining specific parameter combinations, for which you can

define specific creation options. You can specify, for example, whether a transportation allocation is to refer to a transportation

lane, that is, is only to be created if the corresponding transportation lane already exists. Additionally, you can specify whether

time buckets can be overwritten.

## Activities

To create business shares, open the Create Business Shares app on the launchpad.

To create carrier selection allocations, open the Create Transportation Allocation app on the launchpad.

To create flight schedule-based allocations, open the Edit Schedule app on the launchpad. You then choose the “Create

Transportation Allocation” pushbutton in your master flight schedule. You can access and edit the transportation allocation from

your personal object worklist (POWL). To do this, open the Transportation Allocations app on the launchpad.

To create air freight agreement allocations, open the Edit Freight Agreement app on the launchpad. You can now create a

transportation allocation at item level in your freight agreement, assuming you have previously defined a corresponding trade lane.

This is custom documentation. For more information, please visit SAP Help Portal.

287


1/14/26, 2:19 PM

Additionally, you can upload allocations from an external data source to Transportation Management (TM) by executing report

/SCMTMS/TAL_IMPORT. If there are changes in existing buckets of allocations, you can adapt these buckets with this report, too.

You call the report from the SAP Easy Access screen under  Transportation Management

 Administration

 Background

## Processing

 Allocation Upload . Alternatively, you can upload allocations in the Allocations worklist and in the allocation UI.

More Information

Carrier Selection

## Transportation Allocation

Check Against Transportation Allocations

Use of Transportation Orientations

## Use

You can use this function to create the transportation orientation for a trade lane. For more information about trade lanes, see

Creation of Business Shares and Transportation Allocations.

## Features

The following transportation orientations are available (the parameters that are relevant for each orientation are in brackets):

Along (parameter: Source and Destination; parameter type: Location or Zone)

Both the source and the destination are restricted. If the parameter type is Zone, the corresponding location of the relevant

business document (for example, freight order) must be within the transportation zone defined. If the parameter type is

Location, the location of the relevant business document must correspond to this parameter.

  Example
## From PL_FRANKFURT To ITALY

If the source location is PL_FRANKFURT and the destination location belongs to transportation zone ITALY, each object

is considered as context (and is therefore relevant).

Within (parameter: Source; parameter type: Zone)

Both the source and the destination are restricted. Both locations of the relevant business document (for example, freight

order) must be within the defined transportation zone.

  Example
## Within GERMANY

If both the source location and the destination location belong to transportation zone GERMANY, each object is

considered as context (and is therefore relevant).

From (parameter: Source; parameter type: Zone or Location)

If the source parameter type is Zone, the source location of the relevant business document (for example, freight order)

must be in the defined transportation zone, and the destination location must be outside of the transportation zone. If the

source parameter type is Location, the source location of the relevant business document must correspond to this

parameter. The destination is not restricted.

This is custom documentation. For more information, please visit SAP Help Portal.

288


1/14/26, 2:19 PM

  Example

## From GERMANY

If the source location belongs to transportation zone GERMANY and the destination location is outside of this

transportation zone, each object is considered as context (and is therefore relevant).

Outbound (parameter: Source; parameter type: Zone)

Only the source is restricted. The source location of the relevant business document (for example, freight order) must be

within the defined transportation zone. The destination is not restricted and it can be within or outside of the transportation

zone.

  Example

## Outbound GERMANY

If the source location belongs to transportation zone GERMANY, each object is considered as context (and is therefore

relevant).

To (parameter: Destination; parameter type: Zone or Location)

If the destination parameter type is Zone, the destination location of the relevant business document (for example, freight

order) must be in the defined transportation zone, and the source location must be outside of the transportation zone. If

the destination parameter type is Location, the destination location of the relevant business document must correspond to

this parameter. The source is not restricted.

  Example

## To GERMANY

If the destination location belongs to transportation zone GERMANY and the source location is outside of this

transportation zone, each object is considered as context (and is therefore relevant).

Inbound (parameter: Destination; parameter type: Zone)

Only the destination is restricted. The destination location of the relevant business document (for example, freight order)

must be within the defined transportation zone. The source is not restricted and it can be within or outside of the

transportation zone.

  Example

## Inbound GERMANY

If the destination location belongs to transportation zone GERMANY, each object is considered as context (and is

therefore relevant).

The following graphic shows the transportation orientations described:

This is custom documentation. For more information, please visit SAP Help Portal.

289


1/14/26, 2:19 PM

## Transportation Orientations

## Optimization as Part of Carrier Selection

Optimization as part of the carrier selection determines the assignment of carriers with the lowest costs to business documents

(for example, freight orders).

It aims to achieve the following goals:

Reduction in total costs (discounts for continuous moves)

Consideration of all capacity restrictions for means of transport and carriers (minimum and maximum capacities are hard

constraints)

Consideration of business shares (soft constraints; from the transportation lane)

Incompatibilities

## Carrier Activity

The total costs represent the weighted total of the following individual costs:

Non-delivery costs for business documents that the optimizer for carrier selection cannot assign

Costs for the assignment of carriers to business documents

## Penalty costs for violating business shares

This is custom documentation. For more information, please visit SAP Help Portal.

290


1/14/26, 2:19 PM

## Discounts for continuous moves

The total of all the discounts for continuous moves is subtracted from these total costs.

The optimizer for carrier selection takes into account transportation zone hierarchies and hierarchical relationships between

means of transport. You define hierarchies between means of transport by specifying higher-level means of transport when

defining means of transport.

The optimization problem is solved by mixed-integer linear programming.

Determination of Direct Shipment Options

## Use

You can use this function to have direct shipment options for each carrier/service level combination determined when generating

freight units. In this case, the freight units are not consolidated, but rather assigned directly to the carrier (LTL or FTL). This

carrier/service level combination is also then shown as the LTL price, even if it is an FTL case without consolidation.

The VSR optimizer considers the most cost-effective LTL price to be the reference cost. If the VSR optimizer finds a consolidated

solution with even lower costs during the comparison, it uses this one. If the LTL price is lower, you can convert the freight unit to a

freight order automatically, manually, or by using a background report.

Alternatively, you can use this function for scenarios in which a carrier transports products from a shipping point to several

consignees. One example of this is the parcel shipment process. The system can automatically determine the direct shipment

options for freight units and then assign the freight units to a suitable freight order that meets the requirements in terms of the

source location, carrier, and pick-up date. For more information, see Parcel Shipment.

Constraints:

The LTL price is determined and saved for the entire transportation chain of the freight unit, and not on the level of the

stage. For this reason, this function does not support scenarios in which an LTL decision is made for one stage and FTL is

used for a second stage. For such scenarios, a separate FTL freight order must be generated and the LTL price is not

transferred to the VSR optimizer.

LTL prices are determined for a freight unit. If a consolidated LTL price is different from the sum of the FTL prices for a

freight unit, it is not taken into account. It is therefore important for you to define and use the appropriate freight unit

building rules.

  Note

The costs for the direct shipment come from charge management.

However, since the costs in VSR optimization do not usually correspond to the actual costs, but rather only represent an option

for controlling the result of the optimization run, you have to select the costs for the direct shipment in such a way that they are

comparable to the costs used by VSR optimization.

## Prerequisites

You have defined the carrier selection settings and specified there that they are to be used to determine the direct

shipment options. To define the carrier selection settings, open the Create Carrier Selection Settings app on the

launchpad.

In Customizing for your freight unit type, you have made the following settings:

This is custom documentation. For more information, please visit SAP Help Portal.

291


1/14/26, 2:19 PM

You have assigned your freight unit type to the carrier selection settings previously defined.

You have optionally assigned a strategy for determining carrier selection settings to your freight unit type. The

system first evaluates the condition (if available). If this condition does not return a result or if no condition exists,

the system uses the carrier selection settings you assigned to your freight unit type.

You have assigned a strategy for determining direct shipment options to your freight unit type. You use this strategy

to specify that the system is to continue processing the freight units automatically once it has determined the direct

shipment options.

In the DSO Result Rule field for your freight unit type, you have specified how the system is to continue processing

freight units for which it has determined direct shipment options. The following options are available:

The system converts the freight units into freight orders for direct shipments.

The system assigns the freight units to a freight order that meets the requirements in terms of source

location, carrier, and pick-up date. If the system cannot find a suitable freight order, it creates a new one and

copies the freight unit data and the direct shipment option to this order.

You have assigned a freight order type (directly or using a condition) to your freight unit type.

If you want the system to automatically recalculate the direct shipment options when relevant changes are made to

the freight unit, in the Type DirectShipOpt. field (type of direct shipment options), choose the corresponding

option.

For more information, see Customizing for Transportation Management under  Planning

 Freight Unit

 Define Freight

Unit Types .

In the costs settings for the planning profile, you have defined a currency that is to be used when direct shipment options

are determined. Open the Create Constraints and Costs Settings app on the launchpad.

## Features

The direct shipment options are determined based on process controller strategies DSO_DEF or DSO_RESULT as described in the

following section. You can replace these strategies with your own strategies.

1. Execution of Carrier Selection

The system identifies a list of direct shipment options and carrier service products for each combination of carrier and

service level. When doing so, it takes into account transportation lanes and freight agreements. The system considers

incompatibilities based on your carrier selection settings.

  Note

To restrict your results even further, you can define VSR incompatibility settings for incompatibilities between freight

units and means of transport. In the carrier selection settings, you can specify that you want to use these settings for

determining direct shipment options. Since the vehicle resource represents the means of transportation during the

incompatibility determination (see Incompatibilities), you have to create a dummy vehicle resource and define an

incompatibility for it with the incompatibility type FU-Vehicle Resource.

2. Determination of Transit Durations

The system determines transit durations based on the duration determination type defined in the freight agreement of the

corresponding carrier. The following duration determination types are supported:

## Duration determination based on conditions or freight agreements

Transit duration and calendar are either determined based on a condition (if a condition has been entered in the

freight agreement), or taken directly from the freight agreement or the freight agreement type.

This is custom documentation. For more information, please visit SAP Help Portal.

292


1/14/26, 2:19 PM

## Consideration of freight unit dates only

In this case, the transit duration results from the pickup and delivery dates at the transportation stops of the freight

unit.

## Duration determination with external strategy

Transit duration and calendar are not determined and are part of an external scheduling (see next step). The name

of the external strategy (see External Strategies) is also contained in the freight agreement or the freight agreement

type.

The result is a transit duration and calendar that are assigned to the freight unit.

3. Scheduling

The system performs scheduling based on the transit duration and calendar. The result is the earliest pickup date and the

latest delivery date. The scheduling calculation depends on the duration determination type:

## Duration determination based on conditions or freight agreements

Backward scheduling is performed starting from the requested delivery date of the destination stop. Here the

system considers the calendar of the source and destination location and the transit calendar.

## Consideration of freight unit dates only

Pickup and delivery dates correspond to the requested dates of the source and destination locations

(transportation stops of the freight unit).

## Duration determination with external strategy

The external strategy defined in the freight agreement or the freight agreement type is called for the execution of an

external scheduling. If an external strategy has not been entered, the process controller strategy DSO_EXTSCH is

executed. It contains the method DSO_EXTSCH. You can replace it with your own method.

4. Any direct shipment options that have a pickup date that occurs before the pickup date of the freight unit are removed

from the list of direct shipment options by the system. You can replace this step with your own implementations.

5. Selection of the most cost-effective direct shipment option

The system chooses the most cost-effective direct shipment option by selecting it. You can replace this step with your own

implementations.

6. Postprocessing

## Activities

On the user interface for freight units, you can display the direct shipment options that have been identified. Open the Freight Unit

app on the launchpad.

Depending on your Customizing settings, you can trigger the identification of direct shipment options manually from this user

interface. You can also select direct shipment options here and convert freight units into freight orders for direct shipment or

assign them to suitable freight orders.

Alternatively, you can schedule the conversion or assignment of freight units to run in the background. For more information, see

Processing of FUs for Direct Shipment.

  Note
In your personal object worklist for road freight orders and in the transportation cockpit, you can display the total of all selected

DSO amounts for all freight units that are planned as part of a freight order. This amount specifies how high the costs would be

This is custom documentation. For more information, please visit SAP Help Portal.

293


1/14/26, 2:19 PM

if each freight unit were to be transported individually. The difference between the total amount and the amount calculated in

the freight order indicates the potential savings in the case of consolidation.

## More Information

Process Controller Configuration

## Agreement

This is custom documentation. For more information, please visit SAP Help Portal.

294
