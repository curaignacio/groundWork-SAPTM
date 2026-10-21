1/14/26, 2:18 PM

Transportation Management (TM)

Generated on: 2026-01-14 14:18:16 GMT+0000

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


1/14/26, 2:18 PM

Freight Order Management

## Use

You can use the Freight Order Management component in Transportation Management (TM) to create and edit the following

business documents:

Business Document

Transportation Modes

Freight order

Road and rail

Freight booking

Air and sea

Shipment

Trailer unit

Railcar unit

Road

Road

## Rail

Container unit

Independent

Package unit

Independent

## Integration

The TM component Freight Order Management is integrated with the following other TM components:

Component

Master Data

## Integration Type

As a prerequisite for creating freight orders and freight bookings,

you must have created the necessary master data.

## Forwarding Order Management

The system either copies the values from the forwarding orders

## Planning

directly or from the freight units in the freight orders.

Freight orders are the result of transportation planning and serve as

the basis for carrier selection. Freight bookings serve as the basis

for transportation planning.

## Freight Settlement

You can have the system calculate the transportation charges from

your freight orders and freight bookings.

## Dangerous Goods

You can perform a dangerous goods check for freight orders and

freight bookings.

## Global Trade

Freight orders and freight bookings form the basis for the

Basic Functions

## Features

integration with global trade.

In output management you define the possible outputs for your

business documents, for example, print documents.

This is custom documentation. For more information, please visit SAP Help Portal.

2


1/14/26, 2:18 PM

You can use the business documents in freight order management to enter all the information required for transportation planning

and execution, such as source and destination locations, dates/times, product information, and resources used.

You can create freight orders directly or in transportation planning. For example, you can assign freight units to the freight orders

and have the system calculate the transportation charges. You can then perform carrier selection (see Carrier Selection), assign

the freight orders directly to a carrier as a suborder (see External Communication in Overland Transportation) or perform

tendering (see Freight Tendering).

You can use freight bookings to book freight space in advance, for example, with a shipping company. You can then perform the

execution on the same documents.

You can have deliveries created in SAP ERP for order-based transportation requirements contained in a freight order or a freight

booking (see Creation of Delivery Proposals).

Freight order management is integrated with Extended Warehouse Management (EWM) and SAP Extended Warehouse

Management (EWM) in different ways. It is also part of Advanced Shipping and Receiving, which allows information to move freely

between the components EWM, Stock Room Management, Inventory Management (MM-IM), and Logistics Execution (LE). For

more information, see Integration with Extended Warehouse Management and Advanced Shipping and Receiving.

Freight orders and freight bookings also form the basis for tracking with SAP Event Management and Reporting (see Integration

with SAP Event Management).

In addition, you can estimate the freight charges (see Charge Estimation).

You can distribute the charges in a freight order, freight booking, or service order in order to distribute the charges in the freight

document to the underlying distribution items. For more information, see Cost Distribution Management.

You use trailer units, railcar units, and container units to carry out planning with trailers, railcars, and containers.

Freight Order

## Definition

Order for which execution is planned by a carrier or the shipper. The freight order contains the following:

Plan for the logistical processing, for example when and onto which vehicle, freight units are to be loaded

Planned departure times for the vehicle

Execution data

## Use

You use freight orders primarily for land transportation (road freight order) and rail transportation (see Rail Freight Order).

You define the most important settings for the freight order in the freight order type. For more information, see Customizing for

Transportation Management under  Freight Order Management

## Freight Order

 Define Freight Order Types .

You can create freight orders in various ways (see Creation and Editing of Freight Orders).

You can plan loads for freight orders (see Load Planning). You can also select carriers (see Carrier Selection). You can then either

subcontract freight orders directly to a carrier or you can first perform tendering (see External Communication in Overland

Transportation and Freight Tendering).

This is custom documentation. For more information, please visit SAP Help Portal.

3


1/14/26, 2:18 PM

You can use the change controller to define how the system is to react to changes (see Change Controller).

## Structure

Freight orders contain the following information:

Planning information, for example, planned means of transport and stages (transportation stops)

This comprises information about what is to be transported with the freight order as well as hierarchical dependencies

(packaging information). For more information, see Freight Document Overview.

You can also define appointments. For more information, see Appointment.

## Business partner

Driver (see Use of Drivers in Freight Order Management)

## Locations and dates/times

At stage level you can enter one-time locations and additional addresses (one-time addresses). The system stores these

new locations and addresses and adjusts stages in the document. It also adjusts the locations or addresses in the assigned

requirements (freight units).

  Note

However, you should continue to make changes to existing locations in the master data.

## Items

The following information is displayed here:

Quantities and weights (see Quantities and Capacities)

Goods information (see Goods Information)

Corresponding freight orders (see Pick-up and Delivery Freight Orders)

Dangerous goods information (see Considering Dangerous Goods)

Seal information (see Use of Seals)

Information about foreign trade (see Integration with SAP Global Trade Services)

House bill of lading (see Building of House Bills of Lading and House Air Waybills)

You can use Change Hierarchy to decide whether all or only specific items are displayed. This includes:

Service items (see Service Items)

Cargo items (see Cargo Management)

The Items tab page replaces the Cargo tab page. You can personalize your user interface in such a way that the system

displays the old Cargo tab page.

Information about transportation stages, for example, durations and distances

## Diagrams

You can display the utilization of a freight order for each stage and each relevant dimension. This function is also available in

the transportation cockpit.

Subcontracting information, for example, carriers and their prices as well as tendering information

This is custom documentation. For more information, please visit SAP Help Portal.

4


1/14/26, 2:18 PM

You can also enter a freight agreement, freight agreement version, and freight agreement item. The freight agreement and

freight agreement version are used to calculate the charges. The freight agreement item is relevant for service items (see

Service Items).

Execution information, for example, actual departure times

Furthermore, you can directly report events.

Transportation charges (see Charge Calculation) and cost distribution (see Cost Distribution Management)

Customs-relevant information (see Integration with SAP Global Trade Services)

Status information and blocking information (see Statuses of Business Documents and Blocking Information)

## Communication history

Here all information regarding communication with your carriers is displayed, for example inbound and outbound

messages, carrier's document number, and stage information from the XML messages. You can also jump directly to the

XML messages.

## Output management, for example, print documents

As a prerequisite, you have configured the settings for output management in the freight order type (for example, output

profile). For more information, see Printing.

To print the parcel manifest and label, you must enter output profile /SCMTMS/TOR_LBL_PRINT in the freight order type.

Document dependencies as well as predecessor and successor documents (document flow)

## Transportation dependencies, in other words, logistical dependencies

For road freight orders, you can view calculated CO  emissions for each stage, and display calculated and reported

2

emissions per stage as a chart. You can also view calculated CO  emissions at item level. For more information about how

2

CO  emissions are calculated, see Calculation of CO2 Emissions.

2

Other information

Attachments

## Notes

Document references (in other words, additional external references)

Administration information

Change documents (see Change Tracking)

More Information

## Use of Seals

Freight Orders with Non-Linear Stages

Creation of Forwarding Orders from Freight Orders

Classification of Goods

Nature of Goods

## Scheduling

This is custom documentation. For more information, please visit SAP Help Portal.

5


1/14/26, 2:18 PM

Transportation Service Levels

Creation and Editing of Freight Orders

## Use

You can use this function to create, edit, and display freight orders.

## Prerequisites

You have defined freight order types in Customizing. You define the most important settings for the freight order in the freight

order type. For more information, see Customizing for Transportation Management under  Freight Order Management

 Freight

## Order

 Define Freight Order Types .

## Features

Creation of Freight Orders

You have the following options:

## Manual Creation

For more information, see Manually Creating Freight Orders.

## Creation Using an Inbound Message

Your business partner can send you the freight order using EDI communication. You then receive the message using the

service interface TransportationOrderGenericRequest_In. Based on this message, the system automatically

creates a freight order.

For more information, see Creation or Update of Consignment or Freight Orders on Inbound Messages.

If the inbound freight order contains errors, it is usually still saved as a document in TM. The errors are displayed on the

Document Errors tab page and can be corrected here. For more information, see Correction of Errors in Business

Documents.

External Planning with Carrier (B2B)

You can use EDI messages to send freight units to your carrier and receive one or more freight orders with the freight units

assigned to them.

For more information about these services, see Web Services for External Planning Scenarios.

## Creation from Transportation Planning

In manual planning and VSR optimization and in planning in the background, freight orders are created as a result of

transportation planning.

For more information, see Planning and Planning Run.

Alternatively, you can choose New in the transportation cockpit to create a freight order directly. You can also create, for

example, a freight order for a trailer in this way. For more information about creating freight orders for trailers, see Use of

Trailers.

Direct Creation from a Business Document in Forwarding Order Management (FWM Business Documents)

This is custom documentation. For more information, please visit SAP Help Portal.

6


1/14/26, 2:18 PM

For more information, see Direct Creation of Freight Orders and Direct Creation of Freight Documents and Selection of

Schedules.

## Creation from the Freight Unit

You can create freight orders directly from the freight unit. When you do this, you can select whether you want to create a

freight order for each transportation stage or whether you want to group consecutive transportation stages in one freight

order.

## Creation by Copying

You can create a freight order by copying an existing one (reference document). The system copies the header data and the

logistical data. However, it does not copy references to freight units and execution information.

You can also create more than one copy of an existing freight order at the same time. In addition to the number of copies,

you can specify whether the numbers of the created documents are to be displayed in the dialog box.

If you copy an existing freight order, you can enter a different freight order type for the new freight order that is created. This

is useful if you want to copy certain attributes of an existing document into a new one, such as the location or carrier. For

example, you can copy an existing road freight order with the type Freight Order with Subcontracting and create a new

road freight order with a different document type, such as Freight Order with Internal Processing that is executed by your

own trucks.

However, when copying with a different freight order type the following settings for both documents must match:

The sequence type of stages. For example, you cannot copy a freight order that has a linear sequence type to a

freight order that has a non-linear sequence type. For more information about the sequence type of stages, see

Customizing for Transportation Management under  Freight Order Management

 Freight Order

 Define Freight

Order Types .

The setting for Freight Order for Customer Self-Delivery or Pick-Up. For more information, see Customizing for

Transportation Management under  Freight Order Management

## Freight Order

 Define Freight Order Types .

## Creation Based on a Schedule

You can use the report /SCMTMS/MP_SCHED_CREATE_TOR to create a freight order based on a schedule. For more

information, see the system documentation.

## Editing and Displaying Freight Orders

You can edit and display freight orders on the following user interfaces:

## Freight Order Table

Open the following app on the launchpad:

## Freight Orders

User Interfaces for Editing and Displaying

Open one of the following apps on the launchpad:

Edit Road Freight Order

Edit Rail Freight Order

## Transportation Cockpit

Open the Transportation Cockpit app on the launchpad.

Freight orders are only displayed in the transportation cockpit if they match the criteria of the selection profile for freight

orders and freight bookings (see Use of Profile and Layout Sets).

This is custom documentation. For more information, please visit SAP Help Portal.

7


1/14/26, 2:18 PM

Manually Creating Freight Orders

## Use

The following is a description of an example process for manually creating a freight order. In this example, it is assumed that you

already know the most important transportation data, such as source location, destination location, and business partner, because

you regularly transport goods for a certain customer using a certain carrier.

  Note

To create a road freight order manually, open the Create Road Freight Order app on the launchpad. To create a rail freight order

manually, open the Create Rail Freight Order app.

## Process

1. Entering the general data

You first enter the general data for your freight order, for example:

Transportation data, such as shipper, consignee, carrier

## Used resources

Locations and dates/times

## Schedules

For more information, see Use of Schedules.

## Driver

You can enter drivers for road freight orders. For more information, see Use of Drivers in Freight Order Management.

Terms of payment

## Notes

2. Defining additional intermediate stops

You can optionally define additional intermediate stops. You do so on the Overview tab page by choosing the Insert

pushbutton and then Location.

3. Defining the items

You have the following options:

You add freight units to your freight order. You do so on the Overview tab page by choosing the Insert pushbutton

and then Freight Unit.

You directly enter items to be transported that are not based on a forwarding order, for example, when transporting

empties. You can do so by choosing the Insert pushbutton under Freight.

You can build packages. For more information, see Unified Package Building in TM.

4. Calculating transportation charges

Optionally, you can have the system calculate the expected transportation charges for your freight order. For more

information, see Charge Calculation.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

8


1/14/26, 2:18 PM

You use the report Mass Cost Calculation Report for Freight Orders to calculate transportation cost for multiple

freight orders. You call the report from the SAP Easy Access screen under  Logistics

 Transportation

Management

 Administration

## Background Processing

 Calculate Charges for Freight Orders .

The system doesn’t support item level charge calculation for a freight order with consignment orders as items.

5. Checking and saving

Once you have entered all the important data, you can check the consistency of the data. You then save your freight order. In

addition to the consistency check, you can also perform a capacity check and a dangerous goods check. For more

information about the dangerous goods check, see Considering Dangerous Goods.

6. Sending the freight order

You send the freight order to your carrier. You do so by choosing Subcontracting and then Send to Carrier.

When you subcontract a freight order, the system recalculates the charges. If these charges differ from the previously

calculated charges, the system cancels subcontracting. You must then check the charges manually and adjust them, if

necessary. Subsequently, you can resend the freight order to the carrier.

For more information, see External Communication in Overland Transportation and Charge Calculation.

7. Confirming or rejecting the freight order

You confirm the freight order in the name of the carrier, or you reject it. It is also possible to confirm or reject the freight

order using a message.

8. Sending loading and unloading instructions

You send loading and unloading instructions to the warehouse. For more information, see Message-Based Communication

with a Warehouse Management System.

9. Printing

Optionally, you can print the corresponding print documents. For more information, see Printing.

10. Fixing the freight order

You can fix your freight order to protect it from undesirable changes arising from background processing (planning runs or

carrier selection).

11. Creating a freight settlement document

After execution, you create a freight settlement document (see Freight Settlement Document and Enablement of Freight

Settlement Documents for Creation). This serves as the basis for checking the invoice or issuing a voucher. If you have

created additional business partners with the role Additional Agreement Party in your freight order, the system

automatically creates freight settlement documents for this partner.

  Note

A possible variant of this process is that you simply enter the general data. You then call the transportation cockpit and assign

freight units to your freight order. You subsequently perform all additional planning steps in the transportation cockpit, for

example, you have the system calculate the transportation charges and you perform carrier selection or tendering.

## More Information

## Deviating Business Partner Addresses

This is custom documentation. For more information, please visit SAP Help Portal.

9


1/14/26, 2:18 PM

Direct Creation of Freight Orders

## Use

You can use this function to create freight orders directly from a business document in forwarding order management (FWM

business documents). The following describes the aspects that are specific to freight orders. For more information about the

aspects that are specific to forwarding orders, see Direct Creation of Freight Documents and Selection of Schedules.

## Features

The system creates a freight order directly when you save an FWM business document (forwarding order, order-based or delivery-

based transportation requirement) if the following requirements have been met:

The FWM business document is subcontracted and not consolidated with other FWM business documents.

The FWM business document can be delivered in one freight order, meaning there is no pre-carriage or on-carriage.

The FWM business document only has one source location and one destination location.

The following options exist:

## FWM business document type determines the freight order creation

A freight order is to be created directly for FWM business documents of a certain FWM business document type (for

example, a certain business document type for forwarding orders that are subcontracted directly or for delivery-based

transportation requirements that are always delivered directly).

This is the case if a freight unit building rule is found in which you have assigned a freight order type to your FWM business

documents (for example, forwarding order type).

## FWM business document attributes determine the freight order creation

Depending on the FWM business document attributes, for example, ERP document type, the system decides whether a

freight order can or cannot be created.

This is the case if the condition for determining the freight order type finds a freight unit building rule in which you have

defined a freight order type as a business document type. You have assigned this condition to your FWM business

document type, for example, forwarding order type, for cases in which the FWM business documents, such as a forwarding

order, are to be directly converted to a freight order.

## Quantity determines freight order creation

An FWM business document, for example, a forwarding order, can have a total quantity that exceeds the truck size. As a

result, the system creates several freight units where the split quantity determines the number of freight units in the freight

unit building rule. This can also include cases in which a freight unit is created in truck size and a freight unit is to be

consolidated.

This is the case if a freight unit building rule is found in which you have assigned a condition for determining the freight

order type or freight unit type to the business document type. This condition is then called for the freight units created.

Based on the condition, the system decides whether to create a freight order or a freight unit. If the condition finds a freight

unit type dependent on the size of the freight unit, for example, the system converts the freight unit to a freight order.

You cannot add further freight units to such directly created freight orders.

## Creation of Forwarding Orders from Freight Orders

This is custom documentation. For more information, please visit SAP Help Portal.

10


1/14/26, 2:18 PM
## Use

You can use this function to create freight orders without reference to existing forwarding orders. You then create forwarding orders

at a later stage on the basis of these freight orders. This is recommended in the following scenarios:

## Customer Self-Delivery

A customer truck enters the yard. It is not until the truck is unloaded, that you can identify what goods it contains. In this

scenario, you do not create the freight order and enter the items until after the truck has arrived.

## Collective Goods Traffic

Your own truck travels a specific route daily and collects goods. It is not until the truck is unloaded, that you can identify

what goods it contains. In this scenario, you can create the freight order with the main information before the truck arrives.

However, you cannot create the items until the truck arrives.

## Prerequisites

You need to have defined a shipper and a consignee for the freight order item.

You have assigned item types to your forwarding order type. For more information, see Customizing for Transportation

Management under  Forwarding Order Management

## Forwarding Order

 Assign Item Types to Forwarding Order Types

.

## Features

You create a freight order and select the required items. You then create a forwarding order from the freight order for the selected

items. Here the following applies:

The shipping type specified in the forwarding order type must correspond to the selected items. If you have specified the

shipping type LCL, you cannot select any container items in the freight order.

The movement type must match the scenario. In the case of customer self-delivery, for example, the first stage type that

you specify in the stage type sequence for the movement type has to be Customer Self-Delivery. In collective goods traffic,

the stage type has to be Pre-Carriage.

The system creates the forwarding order as well as the freight units and the transportations stages. Moreover, the system connects

the first transportation stage of the freight unit with the freight order.

## Activities

To create a freight order, open one of the following apps on the launchpad:

Create Road Freight Order

## Create Rail Freight Order

To create a forwarding order from the freight order, choose the Create Forwarding Order pushbutton on the Items tab page in the

freight order.

  Note

The Items tab page replaces the Cargo Management tab page. You can personalize your user interface in such a way that the

system displays the old Cargo Management tab page.

This is custom documentation. For more information, please visit SAP Help Portal.

11


1/14/26, 2:18 PM

Rail Freight Order

## Definition

Rail freight orders make up the logistic processing of transports with trains.

## Use

A rail freight order can model a train with one or more locomotives and one or more railcars. You can execute rail freight orders

yourself or award them as a subcontract.

A rail freight order includes the following items:

Locomotives (vehicle resources)

If a train has several locomotives, you can model them using multi-items. Note that during planning, the system considers

only the main locomotive that you have specified at header level. The other locomotives are not taken into account during

scheduling or when considering incompatibilities.

Railcars (passive vehicle resources)

Railcar items can either result from the assigned railcar units (see Railcar Unit) or be created directly in the rail freight

order. The latter is true in less complex scenarios.

You can also work with multi-items in this case. For more information, see Items and Capacities and Utilization in Rail

Freight Orders.

## Freight

You assign cargo items to your railcars.

In the freight order type, you configure the most important settings for the rail freight order. For more information, see Customizing

for Transportation Management under  Freight Order Management

## Freight Order

 Define Freight Order Types .

You can create rail freight orders in various ways (see Creation and Editing of Freight Orders).

You can select a carrier for rail freight orders (see Carrier Selection). You can then award the rail freight orders directly to a carrier

as a subcontract.

You can assign schedules to your rail freight orders at header or transportation stage level (see Use of Schedules). Note that after

you have assigned a schedule you can no longer apply default routes.

You can use the change controller to define how the system is to react to changes (see Change Controller).

Rail freight orders with non-linear transportation stages are not supported.

## Structure

Rail freight orders contain the same information as freight orders (see Freight Order). The following points are variances:

## General Data

Here, you can enter the following data:

Source location and destination location (rail)

This is custom documentation. For more information, please visit SAP Help Portal.

12


1/14/26, 2:18 PM

## Number of railcars

The actual number of railcars is displayed here. If you have agreed scale prices with your carrier, you can enter the

number of railcars for the respective scale as the rating value once you have confirmed this with the carrier. The

system then calculates the tariff based on this amount instead of the actual value. When doing so, it considers the

calculation basis and rate table that you have defined.

  Example

You have nine railcars available to you. This actual value is automatically transferred from the Equipment tab

page. However, the tariff in the agreed scale is for ten railcars. If the carrier is in agreement, you can enter these

ten railcars.

Indication whether there are multiple executing carriers

## Invoicing carrier level

Here, you specify whether there are one or more invoicing carriers.

## Items

This area contains information about your train, locomotives, and railcars, for example:

Position of a railcar in the train

## Equipment group and equipment type

Railcar details such as whether the railcar belongs to the shipper or the carrier

You can use Change Hierarchy to decide whether all or only specific items are displayed. This includes:

Service items (see Service Items)

Cargo items (see Cargo Management)

The Items tab page replaces the Cargo and Equipment tab pages. You can personalize your user interface in such a way

that the system displays the old tab pages.

## Stages

Here, you can enter the following data:

## Invoicing carrier

The invoicing carrier is the carrier that invoices the shipper (or another designated bill-to party) for the charges

calculated for the corresponding stages. This is a common situation in rail scenarios in North America, commonly

referred to as “rule 11”. In rule 11 scenarios, the electronic bill of lading is sent to just one carrier. This is usually the

carrier responsible for the first or last main stage. In turn, this carrier sends the routing instructions to all of the

invoicing carriers and executing carriers involved.

Invoicing carrier level (at stage level)

Here, you specify whether the carrier that you entered at header level or stage level is to be used for freight

settlement.

Each stage is classified as a pre-carriage, main carriage, or on-carriage stage in accordance with the stage types you

have defined. For example, a switching move to the source location would be a pre-carriage stage and a switching

move to the destination location would be an on-carriage stage. All of the stages in between would be considered to

be main carriage stages.

Bill-to party

## Agreement party

This is custom documentation. For more information, please visit SAP Help Portal.

13


1/14/26, 2:18 PM

## Assigning Carriers by Stage

You can assign different carriers at stage level and create multiple invoices for each rail freight order. This is particularly important

for North America since different carriers can be responsible for the different stages. In the rule 11 scenarios mentioned above, one

carrier accepts the actual order but the invoices for the individual stages are submitted by all of the carriers involved.

## Applying Default Routes

You can search for possible routes in your rail freight order based on the carrier, source location, and destination location (Default

Route pushbutton). The system uses the default routes, rates, and tariffs that you have defined to identify the various routes and

sorts them by price. If multiple invoicing carriers can be used for a route, the system displays them as alternatives. For more

information along with an example, see Rail Transportation.

## Document References

You can enter document references at header level, stage level, and item level. For example, you can enter approval numbers for the

use of stages or other reference numbers.

## Status

On the Items tab page (hierarchy type Cargo Management for All Locations for the transportation mode Rail) you can set the

handling execution status of your cargo and the cargo execution status of your railcars:

## Multi-item

If you set the cargo execution status for a multi-item, the system automatically adjusts the cargo execution status of all

subitems (that is, railcars) as well as the handling execution status of all cargo items that are assigned to the multi-item or

to the railcars.

  Example

If you select Set to “Cargo Loaded” for the multi-item, the system automatically sets the cargo execution status of all

subitems (the railcars) to Cargo Loaded and the handling execution status of all cargo items to Loaded.

If you set the handling execution status for a cargo item that is assigned to the multi-item or to a subitem (a railcar), the

system automatically adjusts the cargo execution status of the railcar and of the multi-item.

  Example
Let us assume that you have a multi-item with two subitems (two railcars), each of which is assigned a cargo item.

If you select Set to “Loaded” for one of the cargo items, the system automatically sets the cargo execution status of the

corresponding subitem to Cargo Loaded and the cargo execution status of the multi-item to Cargo Partially Loaded.

If you select Set to “Loaded” for the second cargo item, the system automatically sets the cargo execution status of the

corresponding subitem and of the multi-item to Cargo Loaded.

  Example

Let us assume that you have a multi-item that is directly assigned a cargo item.

If you select Set to “Loaded” for the cargo item, the system automatically sets the cargo execution status of the multi-

item to Cargo Loaded.

## Single item

If you set the handling execution status for a cargo item, the system automatically adjusts the cargo execution status of the

single item (the railcar), and vice versa.

This is custom documentation. For more information, please visit SAP Help Portal.

14


1/14/26, 2:18 PM

  Example

If you select Set to “Loaded” for the cargo item, the system automatically sets the cargo execution status of the railcar

to Cargo Loaded.

For more information about statuses, see Statuses of Business Documents.

More Information

## Freight Settlement

Creation and Transfer of Freight Settlement Documents

Creation and Editing of Transportation Units

Rail Transportation

## Use

This example process describes a typical rail transportation process for shippers.

## Prerequisites

You have defined one or several default routes (Create Default Route app). For more information, see Default Route.

You have defined transportation zones. For more information, see Transportation Zone.

You have configured the prerequisites for freight agreements (see Agreement Maintenance). Freight agreements represent

the contracts you have signed with your carriers. They are equipment-based and must contain the following data:

Source and destination location or transportation zones that contain these locations

## Equipment

External reference number

External item number

## Commodity codes

You have created a freight order type for rail and the corresponding item types in Customizing. For more information, see

Customizing for Transportation Management under  Freight Order Management

## Freight Order

 Define Freight Order

Types .

If you want the system to automatically create railcar units in freight unit building, you must create a transportation unit

type in Customizing and assign it to your freight unit building rule. For more information about creating transportation unit

types, see Customizing for Transportation Management under  Planning

 Transportation Unit

## Define Transportation

Unit Types . For more information about freight unit building rules, see Freight Unit Building Rule.

You have configured the prerequisites for freight settlement (see Freight Settlement).

You have configured the prerequisites for charge management (see Charge Management and Service Product Catalogs). At

a minimum, the rate tables need to have scale items including source and destination rail locations or zones. Moreover, you

must have defined the charge type as the leading charge type in order for through rates to be considered.

This is custom documentation. For more information, please visit SAP Help Portal.

15


1/14/26, 2:18 PM

Optionally, you have indicated parameter /SCMTMS/RAIL_ROUTE in your user profile to specify whether the routing

options with a rate equal to zero are to be displayed. The user parameter has the following values:

'A' = The system displays all routing options.

'X' = The system displays routing options with a rate not equal to zero only.

' ' (default value) = The system filters out the routing options with a rate equal to zero within the default route. At

least one routing option is displayed. The system applies the default value even if you have not indicated the

parameter.

Note that the system takes into account the user parameter when you select Default Route in the rail freight order. The

system displays a message if you have set the user parameter to 'X'.

## Process

1. You define master data (equipment, for example) and create a delivery in SAP ERP and transfer them to TM. Thus, the

required master data and a railcar are available in TM. Moreover, a delivery-based transportation requirement has been

automatically created in TM. For more information, see Internal TM Component Integration. In freight unit building, a railcar

unit has been created instead of a freight unit if you have indicated a transportation unit type in your freight unit building

rule. For more information, see Creation and Editing of Freight Units.

2. You manually create a rail freight order and assign the railcar unit to it. You need to indicate at least the source and

destination rail location, the carrier, and the equipment. On the launchpad, open the Create Rail Freight Order app.

Alternatively, you can create the rail freight order in the transportation cockpit by dragging the railcar unit to a locomotive.

3. In your rail freight order, you choose Default Route to search for possible routing options based on the source and

destination rail locations. The system executes the following steps:

a. It searches for all default routes where the first and last location (or transportation zone) of the default route

matches the source and destination rail locations.

b. For each default route found, it searches for all freight agreement items for each executing carrier defined in the

default route, filtering on trade lanes and commodity codes.

c. For each default route, it searches for rates in all of the rate tables of the selected freight agreement items for each

location combination within the default route.

d. It proposes a list of routing options for each default route and rating alternative. A rating alternative includes any

combination of rates from different executing carriers that can get from the source to the destination rail location.

4. You select a routing option from the list. The system automatically generates transportation stages in the rail freight order

according to the stage information in the selected routing option. This includes the stage types and executing carriers from

the default route as well as the invoicing carriers and freight agreement items determined according to the rating results.

5. You send your rail freight order to your carrier.

For more information about the rail transportation process from the point of view of the carrier, see Creation of a

Forwarding Order for Rail Transportation.

6. You use the standard freight settlement process to settle your rail freight order.

If you have a different invoicing carrier for each transportation stage of a rail freight order, the system creates one freight

settlement document for each of the different carriers in the rail freight order. For more information on freight settlement,

see Freight Settlement.

## Example

This is custom documentation. For more information, please visit SAP Help Portal.

16


1/14/26, 2:18 PM

You have created a rail freight order from source rail location A to destination rail location C with a rail junction in B. You have also

defined default route 100:

## Location

Executing Carrier

A

B

C

X

Y

## Not applicable

Based on this default route and the rates and tariffs that you have defined, the system determines the following routing options:

Routing Option

## Default Route

Transportation Stage

Executing Carrier

Invoicing Carrier

1

1

2

2

100

100

100

100

A -> B

B -> C

A -> B

B -> C

X

Y

X

Y

X (rate for carrier X for A -> B)

Y (rate for carrier Y for B -> C)

X

X (through rate for carrier X for

A -> C)

You decide to select routing option 1. You send the rail freight order to carrier X. Carrier X carries out transportation for the first

transportation stage itself and sends the routing instructions for the second transportation stage to carrier Y. You will receive

invoices from both carriers for their respective transportation stages.

More Information

Rail Freight Order

## Railcar Unit

Capacities and Utilization in Rail Freight Orders

## Use

The following describes how the system determines the capacities and utilization of rail freight orders.

## Prerequisites

In Customizing you have defined equipment types and groups as well as capacities for your locomotives and railcars. For

more information, see Customizing for Transportation Management under  Master Data

 Resources

## Define

Equipment Groups and Equipment Types  and see Equipment Groups and Equipment Types.

You have defined vehicle resources and adjusted the capacities where necessary. For more information, see Vehicle

Resource.

In Customizing you have defined item and subitem types and assigned these to your freight order types. For more

information, see Customizing for Transportation Management under  Freight Order Management

## Freight Order

 Define Freight Order Types  and see Items.

This is custom documentation. For more information, please visit SAP Help Portal.

17


1/14/26, 2:18 PM
Features

## Capacities

Whether and how the system aggregates capacities depends on how you have created your item hierarchy and, more specifically,

your multi-items.

The locomotive is predefined automatically in the rail freight order if you have created the transportation mode Rail in your freight

order type.

You then insert your railcars. You have the following options:

## Insert a railcar as an individual item

When you enter a resource the system automatically fills the equipment type and group as well as the relevant weights.

## Insert a railcar as a multi-item

When you enter the equipment type and group the system automatically fills the relevant weights. You have the following

options when you create a multi-item:

Create with expansion - this means that the individual railcars are displayed as separate subitems

You can change the equipment type and group of the individual subitems and you can enter a resource.

Create without expansion - this means that the multi-item represents all railcars and does not have any subitems

You cannot enter a resource. However, you can expand the multi-item later.

The system aggregates the capacities as follows:

## Multi-item with expansion

The capacity is the sum of the capacities of the individual subitems. The equipment type and group displayed for the multi-

item are no longer important for the calculation. The capacity displayed for the multi-item is only a subtotal.

## Multi-item without expansion

The multi-item behaves like a large railcar (a double freight car, for example). The capacity is the product of the capacity

entered in the multi-item and the number of railcars.

The table below shows how the system calculates the individual weights of locomotives and railcars (classic packaging hierarchy).

Resource

Gross Weight

Net Weight

Tare Weight

Maximum Payload

## Weight

## Locomotive

Net weight plus tare

Net weight of cargo plus

Tare weight of

Maximum weight that

weight of locomotive

net weight of railcar

locomotive

the locomotive can pull

## Railcar

Net weight plus tare

Weight of loaded cargo

Tare weight of railcar

Maximum weight that

weight of railcar

can be loaded onto the

railcar

For more information about quantity totaling in the classic packaging hierarchy, see Quantities and Capacities.

## Utilization

The utilization of the train or locomotive is displayed under Train Capacity:

This is custom documentation. For more information, please visit SAP Help Portal.

18


1/14/26, 2:18 PM

## Maximum utilization in percent

This is the utilization of the locomotive in terms of its trailing load. The system calculates this utilization taking into

consideration the maximum trailing load that you have entered manually here.

  Note

The maximum trailing load is displayed automatically as the maximum payload weight of the locomotive on the

Equipment tab page.

## Length utilization in percent

This is the utilization of the locomotive in terms of its length. The system calculates this utilization from the maximum train

length that you have entered manually here and from the length of the railcar (Cargo Information).

Use of Drivers in Freight Order Management

## Use

If you work with vehicle resources and drivers, you can assign drivers to freight orders and take them into account during planning.

Note that this function is supported for road freight orders and trucks only.

## Prerequisites

To use master data based drivers, you have defined your drivers as business partners and indicated validity, non-working

times and absences. For more information, see Definition of Business Partners and Driver.

You have optionally defined a default driver. You do so by assigning a driver to your default vehicle resource (resource

master data, Transportation tab page). If you use this vehicle resource in your freight order, the assigned driver is

automatically copied to the freight order if you have not yet assigned another driver to it. For more information, see

Definition of Resources.

In your freight order type, you have made the relevant driver settings:

You have indicated if one driver or a driver team (two drivers per stage) are to be assigned. Note that indicating the

number of required drivers is a prerequisite for the driver-specific fields to be displayed on the freight order user

interface.

You have indicated if drivers are to be assigned per transportation stage or per freight order.

You have indicated whether these settings can be changed in the freight order or not.

For more information, see Customizing for Transportation Management under  Freight Order Management

 Freight

## Order

 Define Freight Order Types .

## Features

You have the following options:

## Assigning a single driver or a driver team

Assigning a driver team is recommended for time-critical orders, for example, rush orders. In this scenario, two drivers are

in the cabin and take turns driving and sleeping.

Assigning drivers to the entire freight order or to individual transportation stages

This is custom documentation. For more information, please visit SAP Help Portal.

19


1/14/26, 2:18 PM

You assign a driver to an entire freight order if this driver covers the entire freight order from source location to destination

location. You assign a driver to individual transportation stages if this driver covers a certain number of transportation

stages but then another driver takes over. In this scenario, only one driver is in the cabin at a time (that is, per

transportation stage).

## Assigning drivers not defined in master data

You can assign a driver who you have not defined in master data to your freight order. For example, this is useful if a driver is

only entered at check-in or check-out, or if a driver is not employed by your company.

  Note
Drivers who are not defined in master data are not supported by standard implementations of the Information Retrieval

Framework (IRF). You can use the Freight Orders – Worklist app to search for road freight orders that have been

assigned a driver not defined in master data.

When you assign drivers and save your freight order, the system performs a number of checks. For example, a driver must not be

assigned several times to a transportation stage or to two overlapping freight orders. Moreover, the system checks the driver's

validity and availability within the time frame of the freight order. You can also perform these checks by selecting  Check

## Document

 or Resources. The Driver Assignment Status indicates if you have assigned the number of required drivers to your

freight order.

## Activities

You can assign drivers on the following tab pages of the Freight Order user interface:

General Data

Overview

## Drivers

On the General Data and Drivers tab pages, you also find general information about the assigned drivers.

If you mark a driver on the Drivers tab page, you can view the Driver Details, Qualifications, and Notes. Buttons in the Actions

column allow you to start communication with the driver, such as sending emails or calling.

  Note

For drivers who are not defined in master data, Qualifications are not displayed

For drivers who are defined in master data, only communication data that you have defined in your business partner on

the Address tab page under Communication is displayed in the driver details of the freight order. Address-independent

communication data is not displayed.

To enter a driver who you have not defined in master data on the Drivers tab page, you need to do the following:

1. Select the No Master Data Defined checkbox.

2. In the Actions column, select Edit Deviating Address to enter driver information in a pop-up, including optional

communication data.

The Driver Description field is derived from the driver's name, but you can enter an alternative description in the free-text

field. This does not overwrite the name you entered in the pop-up.

This is custom documentation. For more information, please visit SAP Help Portal.

20


1/14/26, 2:18 PM

How the system sorts and displays drivers on the Overview tab page depends on the locations to which you have assigned these

drivers.

## More Information

For more information about using drivers in manual planning, see Use of Drivers in Planning.

Service Items

## Use

In your freight order and freight booking, you can define service items to order additional services along with transportation

services. Examples of additional services are fumigation of a container or insurance. These services can be provided by the carrier

or by an alternative service provider.

## Prerequisites

You have defined internal service types in Customizing. For more information, see Customizing for Transportation

Management under  Basic Functions

 General Settings

 Define Service Types .

You have assigned these internal service types to your carrier or alternative service provider’s service types. You assign

internal service types to your business partner in the Define Business Partner app (Carrier role, Transport Data tab page).

You have assigned your internal service types to an item type of category Service in Customizing. For more information, see

Customizing for Transportation Management under  Freight Order Management

 Define Item Types for Freight Order

Management

.

In your freight agreement, you have defined freight agreement items and the corresponding services. If you want to make

sure that a service must not be deleted, select the Mandatory Service checkbox for your agreement item. If you want the

system to automatically display the services in your freight order or freight booking when you enter the freight agreement

item, select the Flow Service checkbox for your freight agreement item. For more information about freight agreements,

see Agreement Maintenance.

## Features

You can define service items as subitems of a cargo item or as separate items (main items). You can enter the requested quantity,

service location, and duration for a service item.

You have the option to enter a carrier in your freight order or freight booking. If you do so, the input help contains only those

internal service types that you have assigned to the carrier. If you do not enter a carrier, the system offers you all internal service

types. Alternatively, you can specify an alternative service provider and select an internal service type that has been assigned to

them.

If in addition you enter a freight agreement, freight agreement version, and freight agreement item in your freight order or freight

booking (Subcontracting tab page), the corresponding services are copied to the freight order or freight booking or offered in the

input help. The freight agreement and freight agreement version are also used for charge calculation.

  Note

Service items that you have defined in a related forwarding order are not taken into account or copied to the

corresponding freight order or freight booking.

This is custom documentation. For more information, please visit SAP Help Portal.

21


1/14/26, 2:18 PM

If you enter a freight agreement that is invalid for the freight order or freight booking, the system will only detect this

during charge calculation.

You can distribute costs for a service item that references a logistics item in a freight document. You can only distribute costs in a

freight document where you have a logistics item that comes from an ERP item or a forwarding order. For more information, see

Cost Distribution Management.

## Activities

If you have selected the Generic Item View hierarchy type, service items are displayed on the Items tab page of the freight order or

freight booking. If you want to display service items only, select the Service Items Only hierarchy type in the Change Hierarchy

field. For more information, see Use of Hierarchical Views in FOM.

If you require a service that is provided by a service provider that is not the carrier, select the Item-Specific Service Provider
checkbox, enter the name of the business partner under Business Partner, and select the service type.

Transportation Service Levels

## Use

You use transportation service levels to describe the priority of transportation services. Examples are Express or Standard.

## Features

A distinction must be made between the transportation service levels for the sales side and the purchasing side:

## Sales side

On the sales side, you specify transportation service levels for your customers. To do this, you define transportation service

level codes in Customizing. For more information, see Customizing for Transportation Management under  Forwarding

## Order Management

 Define Transportation Service Level Codes . If you then create one of the following documents the

system offers you the transportation service level codes defined in Customizing for selection:

## Forwarding order

Forwarding agreement (item level)

Forwarding quotation

## Forwarding agreement quotation

If you are working with order- and delivery-based transportation requirements, you do not have to define any transportation

service level codes. In this case, these are taken from the sales order (Shipping Condition field).

## Purchasing side

On the purchasing side, you define carrier service codes in the master data for your carriers. You do this on the SAP Easy

Access screen under  Transportation Management

## Master Data

 Maintain Business Partner

 (Carrier role, Vendor

Data tab page). If you then create a freight document and enter one of these carriers the system offers you the

corresponding values in the Service Level field for selection. This also applies to freight agreements (item level).

  Note

If you are a logistics service provider and can commit all the carriers who work for you to the same transportation service level,

we recommend you make the following settings:

This is custom documentation. For more information, please visit SAP Help Portal.

22


1/14/26, 2:18 PM

Define transportation service level codes in Customizing. For more information, see Customizing for Transportation

Management under  Forwarding Order Management

 Define Transportation Service Level Codes .

Enter one of these values as the standard service level when you define your freight order type. For more information,

see Customizing for Transportation Management under  Freight Order Management

 Freight Order

## Define Freight

Order Types . The system then uses this value when you create a freight order.

Parcel Shipment

## Use

Transportation Management (TM) enables you to commission a carrier to transport parcels from a shipping point to several

consignees. You can create parcel shipments in TM based on deliveries from an ERP system. You can then select a direct shipment

option for the parcel shipment and plan and execute the transportation of shipments to the consignees. The direct shipment

option involves selecting a carrier with the relevant transportation services while taking into account the applicable charges.

The following section provides an example of the parcel shipment process in TM.

## Prerequisites

In addition to the general settings for freight order management and the determination of direct shipment options, you have

configured the following settings that are particular to the parcel shipment process:

In Customizing for the freight unit type, you have configured the settings for determining direct shipment options. A parcel

shipment is a freight unit in TM.

For the parcel shipment process, you have populated the DSO Result Rule field in such a way that the system assigns

freight units to a freight order if it identifies direct shipment options. The system assigns the freight units to an existing

freight order that meets the requirements in terms of source location, carrier, and pick-up date. If the system cannot find a

suitable freight order, it creates a new one.

You can also configure the following options in the Direct Shipment Strategy field:

Default strategy DSO_RESULT: The system determines the direct shipment options and assigns the freight units

automatically to a freight order.

Default strategy DSO_DEF: The system only determines the direct shipment options for the freight units, that is, no

further processing takes place. You can then manually assign the freight units on the user interface or run batch

report /SCMTMS/DIRECT_SHIPMENT_BATCH.

The process described below assumes that you use this setting.

For more information, see Customizing for Transportation Management under  Planning

 Freight Unit

## Define Freight

Unit Types  and also Determination of Direct Shipment Options.

In Customizing for the freight order type, you have configured the settings required for the parcel shipment process. SAP

provides the default freight order type 3000, which contains all of the settings required for the standard parcel shipment

process. In particular, the following default values are provided:

## Sequence Type of Stops: Star-Shaped Based on FU Stages

The default setting in this field specifies that all stages for the freight order have the same start location but different

end locations. This corresponds to the transportation stages in a parcel shipment process.

Draw Bill of Lading Number: Draw Automatically When Item Is Changed

This is custom documentation. For more information, please visit SAP Help Portal.

23


1/14/26, 2:18 PM

This default setting specifies that bill of lading numbers (that is, the shipment numbers) are automatically taken

from the waybill stock.

## HBL Building Strategy: PRCL_SHP

This is the default strategy that the system uses to create parcel shipments.

## Web Dynpro Application Config.: /SCMTMS/FRE_ORDER_MANIFEST

If you create a freight order with this default freight order type and a Web Dynpro application configuration, the user

interface for the freight order is automatically adjusted to meet the requirements of the parcel shipment process.

Note that the UI elements are neutral so that the document can be used for similar processes with shipment type

LTL.

## Add. Output Profile: /SCMTMS/TOR_PRINT_PARCEL_ROOT

If you use this output profile, you can print parcel manifests and labels from the Output Management tab page of

the freight order item details.

For more information, see Customizing for Transportation Management under  Freight Order Management

 Freight

## Order

 Define Freight Order Types .

In Customizing for the item type, you have specified that tracking numbers are to be drawn automatically from the waybill

stock for freight order management. This applies to both shipment items and package items. For more information, see

Customizing for Transportation Management under  Freight Order Management

 Define Item Types for Freight Order

Management

.

You have defined waybill stock for bill of lading numbers and tracking numbers in the master data. For more information,

see Waybill Stock Definition.

To calculate charges when direct shipment options are determined, you have specified the carrier prices in a rate table. The

system can also calculate the charges directly based on Web service offerings from parcel service providers.

In the parcel shipment process, you can also create freight agreements with multiple agreement items, which represent

carrier service products. In the agreement items, you can define attributes such as the length, height, and width on the

Package tab page. If the system calculates charges when determining the direct shipment options, it compares these

attributes with those in the delivery-based transportation requirement and selects a suitable agreement.

For more information, see Rate Determination for Direct Shipment of Parcels.

## Process

1. Creation of delivery-based transportation requirements

TM creates delivery-based transportation requirements (DTRs) based on the deliveries that you have created in your ERP

system. For more information, see Integration of Deliveries.

2. Creation of parcel shipments

The system creates parcel shipments based on the DTRs. For each DTR, it creates exactly one parcel shipment (that is, one

freight unit).

3. Determination of direct shipment options

The system determines the direct shipment options of carriers with carrier service products that meet the requirements of

the shipment (for example, the pick-up and delivery times or the service level). When doing so, it identifies the freight

agreements with the carriers and the service products that are defined therein. The user interface for the parcel shipment

(that is, the freight unit) displays a list of available direct shipment options. The cheapest option is displayed first by default.

This is custom documentation. For more information, please visit SAP Help Portal.

24


1/14/26, 2:18 PM

You can configure the Customizing settings for the freight unit type in such a way that this step is carried out automatically.

Otherwise, you can trigger the determination of direct shipment options manually on the user interface for the freight unit.

For more information, see Determination of Direct Shipment Options.

4. Selection of an option and assignment to a parcel freight order

You select an option and assign the shipments to an existing parcel freight order that meets the requirements in terms of

the source location, pick-up date, and carrier. If the system cannot find a suitable freight order, it creates a new one. In this

case, it transfers the data from the freight unit and the direct shipment option to the new freight order.

5. Editing of the package freight order

You open the freight document. Freight orders that were created with the shipment type Package in addition to the relevant

freight order type are displayed in your personal object worklist (POWL) for parcel freight orders (under Overview Road

Freight Orders).

The freight order contains the parcel shipments and the corresponding packages. The shipment numbers and tracking

numbers for the shipments and packages have been drawn from the waybill stock and assigned automatically in

accordance with your Customizing settings.

6. Shipment of the parcel freight order

You send the freight order to your carrier.

7. Confirmation of parcel freight order

You confirm the freight order in the name of the carrier, or you reject it. It is also possible to confirm or reject the freight

order using a message.

8. Document printing

You print the parcel manifest and labels from the Output Management tab page in the freight order item details. For more

information, see Output Management.

9. Execution of parcel freight order

You set the status of the parcel freight order to Cargo Ready for Loading and start execution and tracking. Once this status

has been set, no further parcel shipments (freight units) can be assigned automatically to the parcel freight order. However,

you can still assign parcel shipments manually.

The parcel freight order is processed further in the same way as a standard freight order. For more information, see

Manually Creating Freight Orders.

Appointment

## Use

You can also define your own appointments in the freight order. These are time windows that you use to define when the delivery or

pick-up at the customer is to take place. You can define start and end times.

If the carrier makes an appointment with a customer on your behalf and includes this in his or her tendering response, it is also

displayed in the freight order.

The appointment is a hard constraint for scheduling. During scheduling the system compares the acceptable times and the

requested times for the freight units with the appointment. If the acceptable times do not lie within the appointment, the system

generates an error message.

This is custom documentation. For more information, please visit SAP Help Portal.

25


1/14/26, 2:18 PM

The acceptable start time of loading and the acceptable end time of unloading are decisive factors here. These must lie within the

appointment. If this is not the case, the system generates an error message. Note that the acceptable end time of loading and the

acceptable start time of unloading can lie outside the appointment.

## Activities

You can define appointments in the freight order on the Overview and Stages tab pages. To do this, double-click a transportation

stop. In this case, a tab page for dates/times is displayed in the lower section where you can define your appointments.

You can also define and change appointments for road freight orders in the transportation cockpit (road freight order list and

hierarchy). You can use user parameter /SCMTMS/SCH_FORCE to force automatic forward scheduling after you have changed

order data.

## Example

## Appointments

For day 1, you have negotiated an appointment between 10:00 and 13:30 with your customer for the loading of a freight order (FO).

For day 2, you have negotiated an appointment between 11:00 and 14:30 to unload the same freight order.

The acceptable start time for loading freight unit 1 (FU1) is earlier than the start time of the appointment for loading the freight

order. As a result, the system generates an error message. The acceptable end time for unloading freight unit 1 also lies outside the

appointment for unloading the freight order. The system also generates an error message for this.

The acceptable start time for loading freight unit 2 (FU2) lies within the appointment for loading the freight order. The acceptable

end time for unloading also lies within the appointment for unloading the freight order.

## Scheduling of Freight Orders

This is custom documentation. For more information, please visit SAP Help Portal.

26


1/14/26, 2:18 PM
## Use

The following process describes how you can determine dates and times in a freight order.

  Note

Transportation units are scheduled together with the freight orders. In schedule-based freight bookings, the system determines

the dates/times from the schedule.

## Prerequisites

You have entered the required master data, such as resources and transportation lanes. For more information, see Master

Data. You have also made the settings needed to determine the lane, distance, and duration. For more information, see

Lane, Distance, and Duration Determination (LDDD).

If required, you have specified in the freight unit type how you want the dates/times to be transferred (Rule for PU/DLV

Window and Cond. for PU/DLV Window Determ. fields). For more information, see Customizing for Transportation

Management under  Planning

## Freight Unit

 Define Freight Unit Types .

## Process

1. Create a forwarding order and enter your requested and acceptable dates/times. For more information, see Creation of a

Forwarding Order and Time Windows. You do not have to enter dates/times. If you do not enter any dates/times, the system

determines these during scheduling.

2. You save the forwarding order. The system creates freight units automatically if you have defined this in Customizing for

your forwarding order type. For more information, see Creation of a Forwarding Order. According to the settings for the

freight unit type, the system copies the dates/times from the forwarding order to the freight units.

3. Create a freight order in the transportation cockpit or from the forwarding order. For more information, see Creation and

Editing of Freight Orders. The system copies the dates/times to the freight order as planned departure and arrival

dates/times.

4. You can also enter the following dates/times:

Cut-off dates/times (such as cargo cut-off date/time) and availability dates/times

Appointments (see Appointment)

5. Schedule your freight order. The system adjusts the departure and arrival dates/times in the freight order and determines

the loading and unloading dates/times for the related freight units. During scheduling, the system takes into account a set

of constraints.

  Note

In the case of schedule-based freight orders and freight bookings, the system does not take into account loading and

unloading durations.

It determines the duration of transportation when it determines the distance and duration. It determines the loading and

unloading durations based on the durations you entered in the planning profile or using the condition entered here. The

determination of durations using the condition are based on the freight unit, the means of transport, or both.

You can use user parameter /SCMTMS/SCH_FORCE to force automatic forward scheduling after data has been changed.

The system then fixes the departure date/time.

For more information, see Scheduling.

This is custom documentation. For more information, please visit SAP Help Portal.

27


1/14/26, 2:18 PM

The system takes into account dependencies between the dates/times of freight unit stages and the related freight orders

regardless of whether you schedule a freight order. This means that it calculates the acceptable end date of a freight unit

stage by considering the start date of the following stage and the goods wait time that you defined for the location. If there

are conflicting dates/times, it sets the corresponding status automatically when it checks all the documents (cross-

document check status). For more information, see Explanation of Statuses of Business Documents.

6. If you change the requested and acceptable dates/times in the forwarding order, the system copies the changes

automatically to the freight units. If your freight order is not yet in execution, the changes are also copied automatically to

the freight order. If your freight order is already in execution, the system sets an execution block if there are conflicting

dates/times.

If you change the planned departure and arrival dates/times in the freight order, the system adjusts automatically the

loading and unloading dates/times in the freight unit.

  Note

In the change controller you specify how you want the system to react to changes to your business documents. For more

information, see Change Controller.

## Example

The table below contains example dates for this process (for the sake of simplicity, only dates are used).

Business

## Document

Dates Entered

## Dates Copied

Result of Scheduling

## Dates Changed

Dates Updated by the

## Manually

by the System

Manually

## System

Forwarding

Not applicable

Not applicable

Not applicable

Not applicable

Not applicable

order:

Requested pick-

2013-10-06

Not applicable

Not applicable

2013-10-07

Not applicable

up date

Freight units:

Not applicable

Not applicable

Not applicable

Not applicable

Not applicable

Requested pick-

Not applicable

2013-10-06

Not applicable

Not applicable

2013-10-07

up date (start)

Requested pick-

Not applicable

2013-10-06

Not applicable

Not applicable

2013-10-07

up date (end)

Acceptable pick-

Not applicable

2013-10-06

Not applicable

Not applicable

2013-10-07

up date (start)

## Requested

Not applicable

2013-10-08

Not applicable

Not applicable

2013-10-09

delivery date

(end)

Loading date

Not applicable

Not applicable

2013-10-07

Not applicable

2013-10-08

(start)

Loading date

Not applicable

Not applicable

2013-10-07

Not applicable

2013-10-08

(end)

Unloading date

Not applicable

Not applicable

2013-10-09

Not applicable

2013-10-09

(start)

Unloading date

Not applicable

Not applicable

2013-10-09

Not applicable

2013-10-09

(end)

This is custom documentation. For more information, please visit SAP Help Portal.

28


1/14/26, 2:18 PM

Business

## Document

Dates Entered

## Dates Copied

Result of Scheduling

## Dates Changed

Dates Updated by the

## Manually

by the System

Manually

## System

Freight order:

Not applicable

Not applicable

Not applicable

Not applicable

Not applicable

## Planned

Not applicable

2013-10-07

2013-10-07

2013-10-08

Not applicable

departure date

Planned arrival

Not applicable

2013-10-09

2013-10-09

2013-10-10

Not applicable

date

Freight Orders with Non-Linear Stages

## Use

This function allows you to describe, for example, the following scenarios:

A less than truck load (LTL) consolidation scenario, in which the deliveries are consolidated into one container at the

transshipment location (such as the port of loading). In such an LTL consolidation scenario, you can create a freight order

for disconnected transportation stages in order to perform freight settlement.

An LTL deconsolidation scenario in which the goods are deconsolidated at the transshipment location (such as the port of

discharge). This transshipment location is supplies all successor stops (that is, the delivery locations) with goods.

## Prerequisites

You have defined a stop sequence type for your freight order type in Customizing. For more information, see Customizing

for Transportation Management under  Freight Order Management

## Freight Order

 Define Freight Order Types .

You have selected the Stage Split checkbox in your freight settlement profile in Customizing. For more information, see

Customizing for Transportation Management under  Settlement

 Define Settlement Profile .

In Customizing, you have also selected the Calculation at Stage Level option in the Calculation Level field of your

calculation profile. For more information, see Customizing for Transportation Management under  Basic Functions

 Charge Calculation

## Basic Settings

 Define Calculation Profiles .

## Features

You can only create freight orders with non-linear stages using customer-specific functions or ERP shipments. This results in the

following limitations:

You cannot create this type of freight order from a forwarding order.

You cannot create freight units from such ERP shipments.

You cannot carry out any planning activities.

You can create freight settlement documents for individual stages.

## Example

For an LTL deconsolidation scenario, you have defined three locations:

Source location A

This is custom documentation. For more information, please visit SAP Help Portal.

29


1/14/26, 2:18 PM

Destination location B

Destination location C

The stages look as follows:

## Stage

Source location

Destination location

10

20

A

A

B

C

External Communication in Overland Transportation

## Use

You can use this process to send freight orders directly to a carrier without first having performed tendering. The following section

contains a description of an example process:

## Prerequisites

You have configured your sending system, that is Transportation Management (Transportation Management).

The carrier has configured its receiving system, for example TM.

You have configured your XI system, for example, SAP NetWeaver Process Integration (SAP NetWeaver PI).

Freight orders exist.

## Process

1. If you choose Subcontracting and then Send to Carrier on the user interface for freight orders, the sending system, for

example TM, sends the freight orders with the service operation TransportationOrderRequest_Out to your carrier.

2. The receiving system, for example TM, receives the freight orders as forwarding orders via the service operation

TransportationRequestRequest_In.

3. The receiving system confirms the freight orders via the service operation

TransportationRequestConfirmation_Out. The carrier uses the confirmation to either accept the freight order

(possibly with changes) or reject the freight order.

4. The sending system receives the confirmation with the service operation TransportationOrderConfirmation_In.

5. The sending system can cancel the freight order via the service operation

TransportationOrderCancellationRequest_Out.

  Note

The service operations named above can also be used for direct tendering.

You can then also send freight orders to your carrier directly in direct tendering. Alternatively, the system sends your

freight orders resulting from a freight request-based tendering automatically to your carrier.

This is custom documentation. For more information, please visit SAP Help Portal.

30


1/14/26, 2:18 PM

The Communication History tab page in the freight order provides an overview of all outbound and inbound messages

relating to the freight order. For more information, see Freight Order.

Freight Booking

## Definition

Order for which execution is planned by a carrier, for example, a shipowner. The freight booking contains the plan for the logistical

processing, for example, fixed departure times of the ship.

## Use

You use a freight booking to reserve freight space on a ship or in an airplane. The freight booking is also the document for the

actual execution.

You define the most important settings for the freight booking in the freight booking type. Furthermore, you specify the

transportation mode, for example, air, for which a freight booking is to be used. For more information, see Customizing for

Transportation Management under  Freight Order Management

## Freight Booking

 Define Freight Booking Types .

For more information about creating freight bookings, see Creation and Editing of Freight Bookings.

If you have entered geography and times in your ocean freight booking, you can perform carrier selection (see Carrier Selection). In

this case, the system looks for the most suitable carriers, taking into account transportation allocations.

You can use SAP Event Management to track and monitor freight booking events (see Tracking of Freight Orders and Freight

Bookings).

You can use the change controller to define how the system is to react to changes (see Change Controller).

  Note

Separate user interfaces are available for both ocean freight bookings and air freight bookings. The following special user

interfaces are also available:

User interfaces for management of air freight bookings for airlines (see Management of Air Freight Bookings for Airlines)

User interface for management of loose cargo (only for ocean freight bookings; see Creation and Editing of Freight

Bookings)

## Structure

Freight bookings contain the following information:

General data

## Business partner

## Locations and dates/times

At stage level you can enter one-time locations and additional addresses (one-time addresses). The system stores these

new locations and addresses and adjusts stages in the document. It also adjusts the locations or addresses in the assigned

requirements (freight units).

This is custom documentation. For more information, please visit SAP Help Portal.

31


1/14/26, 2:18 PM

  Note

However, you should continue to make changes to existing locations in the master data.

## Transportation stages

Here the system displays times, locations and their sequence, as well as transit countries, among other things. You can add

transportation stages, for example, in order to add another port between New York and Amsterdam.

In addition, you can add transportation stages between the pick-up location and the port of loading or between the port of

discharge and the delivery location. This means that there can be several pre-carriage transportation stages and several on-

carriage transportation stages. However, you cannot use these additional transportation stages to model a multiple pick-up

scenario. Instead, you can only model locations, at which additional activities (such as weighing) are to be executed. The

freight unit transportation stage remains unchanged. Another option is to add locations on the Overview tab.

  Note

The Stages tab is only available for ocean freight bookings. You can find information about air freight bookings under

Carrier Routing.

Document dependencies as well as predecessor and successor documents (document flow)

Information about transportation charges (see Charge Calculation) and cost distribution (see Cost Distribution

Management)

## Items

The following information is displayed here:

Quantities and weights (see Quantities and Capacities)

Goods information (see Goods Information)

Corresponding freight orders (see Pick-up and Delivery Freight Orders)

Service orders (see Service Order)

Dangerous goods information (see Considering Dangerous Goods)

Seal information (see Use of Seals)

Information about foreign trade (see Integration with SAP Global Trade Services)

House bill of lading (ocean freight) or air waybill (air freight)

For more information, see Building and Printing of House Bills of Lading and House Air Waybills.

You can use Change Hierarchy to decide whether all or only specific items are displayed, for example service items (see

Service Items) or cargo items (see Cargo Management). The Items tab page replaces the Cargo Management tab page in

the ocean freight booking. You can personalize your user interface in such a way that the system displays the old tab page.

  Note

If you choose the option Generic Item View in an air freight booking on the Capacity and Cargo tab page under Change

Hierarchy, the system displays all items. If you choose Cargo Management, the system displays cargo items only. If you

choose Service Items Only, the system displays service items only.

## Capacity requirements

For air and ocean transportation processes, you may need to reserve capacity with a carrier before the planning is done, for

example, of the number of containers required for the transport.

This is custom documentation. For more information, please visit SAP Help Portal.

32


1/14/26, 2:18 PM

You can reserve capacity by entering, for example, the equipment type, equipment group, and container count.

You can see the reserved capacity in the Cargo Management hierarchy on the Items tab page or on the Overview tab page.

As a prerequisite, you must create a new entry in the Customizing for the Overview hierarchy type and make this setting.

For more information, see Customizing for Transportation Management under  Freight Order Management

## Define

Hierarchical Views for Business Documents .

On the Overview tab page, you can see the utilization of the reserved capacity, for example, how many of the reserved

containers are being used. This helps you determine whether, for example, you have exceeded the total capacity and need

to ask the carrier to remove some containers or assign them to another capacity reservation item. You can also see the

maximum utilization of a container at the level of the freight booking or at the stop level.

## Subcontracting information

You can also enter a freight agreement, freight agreement version, and freight agreement item. The freight agreement and

freight agreement version are used to calculate the charges. The freight agreement item is relevant for service items (see

Service Items).

  Note

In the air freight booking you find the freight agreement, freight agreement version, and freight agreement item under

the general booking data.

## Communication history

Here all information regarding communication with your carriers is displayed, for example inbound and outbound

messages, carrier's booking number, and stage information from the XML messages. You can also jump directly to the XML

messages.

Information about output management (for example, print documents)

As a prerequisite, you have configured the settings for output management in the freight booking type (for example, output

profile) For more information, see Printing.

Transportation dependencies, in other words, logistical dependencies such as related freight orders (ocean freight bookings

only)

Information about the carrier ranking (ocean freight bookings only)

Status information and blocking information (see Statuses of Business Documents and Blocking Information)

Other information

Attachments

## Notes

Document references (in other words, additional external references)

Change documents (see Change Tracking)

## More Information

Consideration of Equipment Data During FU Creation

Buyer's Consolidation

LCL Freight Bookings

## FCL Freight Bookings

This is custom documentation. For more information, please visit SAP Help Portal.

33


1/14/26, 2:18 PM

Export/Import Processing

Classification of Goods

## Nature of Goods

Transportation-Mode-Specific Codes

Interaction Between Organizational Units

## Freight Document Overview

Creation and Editing of Freight Bookings

## Use

You can use this function to create, edit, and display freight bookings.

## Prerequisites

You have defined freight booking types in Customizing. You define the most important settings for the freight booking in the

freight booking type. For more information, see Customizing for Transportation Management under  Freight Order

Management

## Freight Booking

 Define Freight Booking Types .

If you want to create ocean freight bookings for loose cargo, you have made the following settings in your freight booking

type:

You have specified /SCMTMS/FRE_BOOK_OCEAN_LOOSE as the Web Dynpro application configuration.

In the Container Item Source field, you have chosen the Container Item Is Taken from Predecessor Documents

option.

When you create ocean freight bookings with this freight booking type, you can enter a capacity on the related user

interface instead of the container data, meaning a certain weight or volume (or both), and calculate the utilization.

If you want to create ocean freight bookings for multi-pickups or multi-deliveries (for bulk material scenarios, for example),

you have made the following settings in your freight booking type:

In the FB for Multi-PU/DL field, you have specified that several ports of loading and ports of discharge are allowed.

In the Consolidation (Source) and Consolidation (Dest.) fields, you have selected the option Without

Consolidation.

You have specified /SCMTMS/FRE_BOOK_OCEAN_BULK as the Web Dynpro application configuration. A specific

user interface is then available for creating and changing these ocean freight bookings. In addition, there is a specific

object type in your personal worklist for selecting these ocean freight bookings.

You have assigned the predefined shipping type Bulk Material to your ocean freight booking. You have selected the

Cargo Items Must not Be Assigned to Equipment Item option in the Assignment to Equipment Item field in this

shipping type. This means that the Not Relevant option is automatically selected in the Container Item Source field

of your freight booking type.

## Features

## Creation of Freight Bookings

This is custom documentation. For more information, please visit SAP Help Portal.

34


1/14/26, 2:18 PM

You have the following options:

## Manual Creation

For more information, see Manually Creating Freight Bookings.

## Creation from a Forwarding Order

You can create freight bookings directly when creating forwarding orders. For more information, see Direct Creation of

Freight Documents and Selection of Schedules.

The further steps, for example, sending the freight booking to the shipping company or the airline, are done in manual

creation.

## Creation from the Transportation Cockpit

You can create a freight booking manually in the transportation cockpit. To do this, choose New and then the required

option, depending on whether you want to create a freight booking for sea or air transportation. Enter the required data

(based on the creation from a forwarding order).

For more information about the transportation cockpit, see Manual Planning.

## Creation from the Freight Unit

You can create freight bookings directly from the freight unit. When you do this, you can select whether you want to create a

freight booking for each transportation stage or whether you want to group consecutive transportation stages in one freight

booking.

## Creation by Copying

You can create a freight order by copying an existing one (reference document). The system copies the header data and the

logistical data. However, it does not copy references to freight units and the confirmed capacity.

If you copy an existing freight booking, you can enter a new freight booking type for the new freight booking that is created.

This can, however, lead to inconsistencies with copied data if, for example, the copied data has been determined from the

Customizing settings for the freight booking type (such as the transportation mode and the shipping type). If the data for

the new freight booking type is unique, the system updates the data automatically. Otherwise you have to change the

inconsistent data manually.

You can also create more than one copy of an existing freight booking at the same time. In addition to the number of copies,

you can specify whether the numbers of the created documents are to be displayed in the dialog box.

  Note

You cannot create an ocean freight booking by copying an air freight booking, and vice versa.

You cannot create an ocean freight booking for multi-pickups or multi-deliveries from a normal freight booking,

and vice versa.

## Creation Based on a Schedule

You can use the report /SCMTMS/MP_SCHED_CREATE_TOR to create a freight booking based on a schedule. For more

information, see the system documentation.

## Editing and Displaying of Freight Bookings

You can edit and display freight bookings on the following user interfaces:

## Freight Booking Table

This is custom documentation. For more information, please visit SAP Help Portal.

35


1/14/26, 2:18 PM

Open the Freight Bookings app on the launchpad.

## User Interfaces for Editing and Displaying

Open the Edit Air Freight Booking app on the launchpad for air transportation, for example.

  Note

You can display various task-specific views of the air freight booking using the Page function.

## Transportation Cockpit

You can assign freight units in the transportation cockpit of a freight booking, which you have already created manually or

created from a forwarding order. You can assign the freight units either manually or automatically. In the second case, select

the freight booking, the resource, and the freight units and then start VSR optimization for the selected objects.

Open the Transportation Cockpit app on the launchpad.

Freight bookings are displayed only in the transportation cockpit if they match the criteria of the selection profile for freight

orders and freight bookings (see Use of Profile and Layout Sets).

Manually Creating Freight Bookings

## Usage

The following is a description of an example process for manually creating an ocean freight booking. In this example, it is assumed

that you use a certain ship every week to transport goods from a certain source location to a certain destination location.

  Note

To create an ocean freight booking manually, open the Create Ocean Freight Booking app on the launchpad.

## Prerequistes

You have defined freight booking types in Customizing. You define the most important settings for the freight booking in the freight

booking type. For more information, see Customizing for Transportation Management under  Freight Order Management

## Freight Booking

 Define Freight Booking Types .

## Process

1. Entering the general data

You first enter the general data for your ocean freight booking, for example:

## Shipper, consignee, and carrier

Locations, for example, port of loading and port of discharge

Dates and times, for example, departure date and expected arrival date

## Number of containers

The containers are displayed in the item overview. You can add freight units manually by specifying a forwarding

order, for example.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

36


1/14/26, 2:18 PM

If you specify several different types of containers, the total number of containers is displayed in the upper

section. The system creates the items for the individual containers in the lower section. You can add additional

containers or items to existing freight bookings at any time. If you receive a confirmation in which not all

containers and items are confirmed, the system deletes the non-confirmed containers and items.

## Schedule

For more information, see Use of Schedules.

## Freight terms

You can control how the system creates a statement in an international transport. If you enter prepaid, the system

creates a statement for export freight booking. If you enter collect, the system creates a statement for import

freight booking.

2. Calculating transportation charges

Optionally, you can have the system calculate the expected transportation charges for your ocean freight booking. For more

information, see Charge Calculation.

3. Checking and saving

Once you have finished entering all the important data, you optionally check the consistency of your data and then you save

your ocean freight booking.

4. Sending the ocean freight booking

You send your ocean freight booking to a shipping company. For more information, see External Communication in Sea

Traffic and Air Traffic.

5. Confirming or rejecting the ocean freight booking

You confirm the ocean freight booking in the name of the shipping company, or you reject it. It is also possible to confirm or

reject the freight order using a message.

6. Changing the ocean freight booking (optional)

You optionally change the details of your ocean freight booking, for example, the number of containers. You then repeat

steps 4 and 5.

7. Sending loading and unloading instructions

You send loading and unloading instructions to the warehouse. For more information, see Message-Based Communication

with a Warehouse Management System.

8. Sending the shipping instruction

You enter additional data, for example, the amount to be insured, and then you send the shipping instruction.

9. Creating a freight settlement document

After execution, you create a freight settlement document (see Freight Settlement Document and Enablement of Freight

Settlement Documents for Creation). This serves as the basis for checking the invoice or issuing a voucher. If you have

created additional business partners with the role Additional Agreement Party in your ocean freight booking, the system

automatically creates freight settlement documents for this partner.

10. Printing

Optionally, you can print the corresponding print documents. For more information, see Printing.

11. Canceling the ocean freight booking (optional)

You can cancel your ocean freight booking. For more information, see External Communication in Sea Traffic and Air Traffic.

This is custom documentation. For more information, please visit SAP Help Portal.

37


1/14/26, 2:18 PM
## More Information

Deviating Business Partner Addresses

Pick-up and Delivery Freight Orders

## Use

In sea transportation, you use freight orders for pick-up to transport containers from the container freight station to the loading

port. You use freight orders for deliveries to transport containers from the unloading port to the container freight station.

In air transportation, you use freight orders for pick-up to transport unit load devices or loose goods from the source gateway to

the airline's delivery address. You use freight orders for delivery to transport unit load devices or loose goods from the pick-up

address of the airline to the target gateway.

## Prerequisites

You have created and saved sea freight bookings.

You have defined a standard order type for your freight orders for pick-ups and deliveries in Customizing. For more

information, see Customizing for Transportation Management under  Freight Order Management

## Freight Booking

 Define Freight Booking Types .

## Features

You create freight orders for pick-up and delivery of one or more containers or ULDs or for loose goods (air cargo only) from your

freight bookings. A container, a ULD, or loose goods can be assigned to one freight order only.

You can create several freight orders for a sea freight booking. Moreover, you can create a freight order for multiple air freight

bookings. This is also possible if you use a mixed ULD for air cargo the goods of which are from different air freight bookings but for

the same flight (see Mixed Unit Load Device). You can also assign additional air freight bookings or individual air freight booking

items to the freight orders retroactively. Multi-pickup and multi-delivery scenarios are supported. This means that the source

gateways and delivery addresses can be different for a freight order for pick-up. Similarly, the pick-up addresses and destination

gateways can be different for a freight order for delivery.

The corresponding documents are displayed in the document flow of the freight order and the corresponding sea freight booking.

The corresponding freight order is also displayed in the freight booking in the container details or in the air freight container details

(Items tab page (sea), Capacity and Cargo (air) tab page). In both cases you have to select one of the hierarchy types for cargo

management.

  Note

The Items tab page replaces the Cargo Management tab page in the ocean freight booking. You can personalize your user

interface in such a way that the system displays the old Cargo Management tab page.

The system copies the seal information from the sea freight booking to the corresponding freight order. You can enter more seals in

the freight order.

The system automatically copies the following changes to the sea freight bookings to the corresponding freight order:

## Item changes

This is custom documentation. For more information, please visit SAP Help Portal.

38


1/14/26, 2:18 PM

## Location changes

The system copies the following changes to the corresponding freight order for the pick-up:

## Pick-up location

## Port of loading or airport of departure

Delivery address at port of loading (ocean freight) or delivery address of carrier (air freight)

The system copies the following changes to the corresponding freight order for the delivery:

## Delivery location

## Port of discharge or airport of destination

Pick-up address at port of discharge (ocean freight) or pick-up address of carrier (air freight)

## Changes to dates/times

The system copies changes to the pick-up date and cargo cut-off date/time to the corresponding freight order for pick-up.

The system copies changes to the delivery date and port pick-up date/time (ocean freight) or availability date/time (air

freight) to the corresponding freight order for delivery.

## Changes to the seals

If you change the handling execution status of your sea freight booking, the system also adjusts this status automatically in the

corresponding freight order. Conversely, it adjusts the status of the corresponding transportation stop in the sea freight booking if

you change this status in the freight order.

The system automatically copies the following changes to a freight order to the related freight booking:

Change of the cargo receipt status

## Entering or solving discrepancies

In the air freight booking, you can display in the related freight or when the freight for the delivery is ready for unloading.

## Activities

You create freight orders for the pick-up and delivery from your freight booking (Items tab page). In addition, you can create freight

orders for pick-up and delivery for your freight bookings from your personal worklist. In the freight order for the pick-up or delivery,

you can add additional freight booking retroactively.

Freight Orders for Customer Self-Delivery and Pick-Up

## Use

If your customers want to organize their own delivery or pick-up, you as a logistics service provider can create the following freight

orders for the related transportation stages:

Customer order for customer self-delivery, for example, from the customer to the container freight station (CFS)

Customer order for customer pick-up, for example, from CFS to the customer

## Prerequisites

This is custom documentation. For more information, please visit SAP Help Portal.

39


1/14/26, 2:18 PM

In Customizing you have defined your own freight order type and have made the following settings:

In the Freight Order Can Be Subcontracted field, you have selected the option Not Relevant for Subcontracting.

In the Shipper/Consignee Determination Rule field, you have selected the option Shipper/Consignee Not

Relevant.

For freight orders for customer self-delivery, you have selected the option Star-Shaped Based on FU Stages

(Reversed) in the Sequence Type of Stops field. For freight orders for customer pick-up, you have selected the

option Star-Shaped Based on FU Stages.

In the Self-Delivery/Customer Pick-Up field, you have selected Freight Order for Customer Self-Delivery or Pick-

Up.

In the Web Dynpro Application Config. field, you have entered the application configuration

/SCMTMS/FRE_ORDER_SDCP.

The SAP standard system provides the freight order types 4000 for customer self-delivery and 5000 for customer pick-up.

For more information, see Customizing for Transportation Management under  Freight Order Management

 Freight

## Order

 Define Freight Order Types .

The following prerequisites are valid only if you create the freight orders from forwarding orders or from your personal worklist.

You have defined the stage types with the stage category Customer Self-Delivery and Customer Pick-Up. For more

information, see Customizing for Transportation Management under  Forwarding Order Management

 Define Stage

Types .

You have defined movement types. For more information, see Customizing for Transportation Management under

Forwarding Order Management

 Define Movement Types .

You have defined the stage type sequence for the movement types that you created. For more information, see Customizing

for Transportation Management under  Forwarding Order Management

 Define Stage Type Sequence for Movement

Types .

You have defined a default freight document type for stages and activated the creation of freight documents. For more

information, see Customizing for Transportation Management under  Forwarding Order Management

## Forwarding Order

 Define Default Capacity Document Types for Stages .

In the freight order type, you specified that you want to use customer pick-up or self-delivery. For more information, see

Customizing for Transportation Management under  Freight Order Management

## Freight Order

 Define Freight Order

Types .

## Features

You have the following options for creating freight orders for customer self-delivery and pick-up:

Creation on the user interface for creation of freight orders

Creation from a forwarding order for sea or air transportation

Creation from your personal worklist for forwarding orders for sea or air transportation

The system automatically includes changes to the forwarding order in the freight orders. Subcontracting und charge calculation

are not supported for these freight orders.

As the customer schedules and executes the freight orders, they are not relevant for scheduling by logistics service providers.

This is custom documentation. For more information, please visit SAP Help Portal.

40


1/14/26, 2:18 PM
## Activities

To create freight orders directly, open the Create Road Freight Order app on the launchpad.

If you want to create freight orders from a forwarding order, on the Actual Route tab page in your sea or air forwarding order, select

a transportation stage with the Customer Self-Delivery or Customer Pick-Up stage type and choose  Freight Document

 Create

.

To create freight orders from your personal worklist, select one or more sea or air forwarding orders in your worklist with the

relevant movement type and then choose  Follow-Up Actions

 Create Freight Order for Customer Pick-Up  or  Follow-Up

## Actions

 Freight Order for Customer Self-Delivery .

Service Items

## Use

In your freight order and freight booking, you can define service items to order additional services along with transportation

services. Examples of additional services are fumigation of a container or insurance. These services can be provided by the carrier

or by an alternative service provider.

## Prerequisites

You have defined internal service types in Customizing. For more information, see Customizing for Transportation

Management under  Basic Functions

 General Settings

 Define Service Types .

You have assigned these internal service types to your carrier or alternative service provider’s service types. You assign

internal service types to your business partner in the Define Business Partner app (Carrier role, Transport Data tab page).

You have assigned your internal service types to an item type of category Service in Customizing. For more information, see

Customizing for Transportation Management under  Freight Order Management

 Define Item Types for Freight Order

Management

.

In your freight agreement, you have defined freight agreement items and the corresponding services. If you want to make

sure that a service must not be deleted, select the Mandatory Service checkbox for your agreement item. If you want the

system to automatically display the services in your freight order or freight booking when you enter the freight agreement

item, select the Flow Service checkbox for your freight agreement item. For more information about freight agreements,

see Agreement Maintenance.

## Features

You can define service items as subitems of a cargo item or as separate items (main items). You can enter the requested quantity,

service location, and duration for a service item.

You have the option to enter a carrier in your freight order or freight booking. If you do so, the input help contains only those

internal service types that you have assigned to the carrier. If you do not enter a carrier, the system offers you all internal service

types. Alternatively, you can specify an alternative service provider and select an internal service type that has been assigned to

them.

If in addition you enter a freight agreement, freight agreement version, and freight agreement item in your freight order or freight

booking (Subcontracting tab page), the corresponding services are copied to the freight order or freight booking or offered in the

input help. The freight agreement and freight agreement version are also used for charge calculation.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

41


1/14/26, 2:18 PM

Service items that you have defined in a related forwarding order are not taken into account or copied to the

corresponding freight order or freight booking.

If you enter a freight agreement that is invalid for the freight order or freight booking, the system will only detect this

during charge calculation.

You can distribute costs for a service item that references a logistics item in a freight document. You can only distribute costs in a

freight document where you have a logistics item that comes from an ERP item or a forwarding order. For more information, see

Cost Distribution Management.

## Activities

If you have selected the Generic Item View hierarchy type, service items are displayed on the Items tab page of the freight order or

freight booking. If you want to display service items only, select the Service Items Only hierarchy type in the Change Hierarchy

field. For more information, see Use of Hierarchical Views in FOM.

If you require a service that is provided by a service provider that is not the carrier, select the Item-Specific Service Provider
checkbox, enter the name of the business partner under Business Partner, and select the service type.

Buyer's Consolidation

## Use

As a carrier, you can use this function if your customers regularly buy goods in a particular country or region. You can then

consolidate goods from different suppliers that are intended for one consignee before the main carriage and load them into one

container. The goods are not deconsolidated after the main carriage, they remain together in the container in the on-carriage stage

also. This keeps the transport costs cheaper than with the LCL scenario for example (LCL = Less Than Container Load).

You can define rates for consolidated transportation in a separate calculation sheet.

## Features

You create a container in your ocean freight booking, in other words, the container does not exist in the corresponding forwarding

order. You specify that you want to use the container for Buyer's Consolidation in the container details. You then create a freight

order for the container for the consolidated on-carriage from the ocean freight booking. The system automatically assigns the

affected freight units to this freight order and copies seal information, quantities, and references from the ocean freight booking to

the freight order.

  Note

If you try to plan the on-carriage stage in the transportation cockpit before creating the freight order, the system issues an error

message.

If no ocean freight booking exists for your forwarding order, you can specify directly in the forwarding order that it should be

Buyer's Consolidation (Tab General Data). If you create an ocean freight booking for this forwarding order later on, the system

copies this information to the ocean freight booking. If an ocean freight booking exists for your forwarding order, the corresponding

checkbox in the forwarding order is not ready for input.

## Forwarding Settlement Documents

You can create a forwarding settlement document (FWSD) for a buyer’s consolidation in your ocean freight booking. The system

uses the Consolidation Container field for an individual line item on the  Cargo Management

 Container Details  tab pages to

This is custom documentation. For more information, please visit SAP Help Portal.

42


1/14/26, 2:18 PM

identify buyer’s consolidation cargo in the ocean freight booking. You can also create an FWSD for an unplanned party in an ocean

freight booking. This enables you to invoice for any unplanned charges or services that are associated with the ocean freight

booking.

To calculate the charges for the cargo items on stages that are consolidated as a buyer’s consolidation in the ocean freight

booking, the system uses an agreement item with the consolidation type Buyer’s Consolidation. If you have not defined an

agreement item with the consolidation type Buyer’s Consolidation, the system uses a standard calculation sheet defined for full

truck load (FTL) road transportation or full container load (FCL) sea transportation. If you have not defined a calculation sheet for

FCL or FTL transportation, the system chooses an agreement with no shipping type. The system does not consider the calculation

sheet for LCL or less than truck load (LTL) transportation.

The following restrictions apply to the use of the sales organization in all the forwarding orders that are linked to a cargo line item in

a buyer’s consolidation:

If the sales organizations in all the forwarding orders are the same, then the system uses this sales organization in the

FWSD.

If the sales organizations are different, the system tries to use the purchasing organization in the ocean freight booking. The

purchasing organization has the organizational unit function that you have defined as a forwarding house (organizational

unit function – 89) in the organization set up. The system uses this organization as the sales organization for the FWSD.

If none of these options apply, the system displays an error when it attempts to create the FWSD in the ocean freight booking.

For more information, see Buyer's Consolidation Settlement.

## Example

As a carrier, you want to transport three different products for your customer from three different manufacturers from Asia to

Germany. You organize the consolidation of the goods in Shanghai port. This means that the pallets are loaded into a container in

Shanghai. The container is then transported by sea to Hamburg. In Hamburg the container is loaded onto a truck. The truck then

drives with the container to the distribution center in Hanover. This is where the container is deconsolidated.

The customer is invoiced at consolidated rates if you have defined an agreement item with the consolidation type Buyer’s

Consolidation. If you have not defined an agreement item with the consolidation type Buyer’s Consolidation, the system uses the

FCL rates for the stages by sea from Shanghai to Hamburg and for the onward journey from Hamburg to Hanover. You can create

these FWSDs from the ocean freight booking.

## More Information

Buyer's Consolidation in Export/Import

External Communication in Sea Traffic and Air Traffic

## Use

In this process, you can use a freight booking to book freight space, for example, with a shipping company or an airline. The

following section contains a description of an example process:

## Prerequisites

You have configured your sending system, that is Transportation Management (Transportation Management).

This is custom documentation. For more information, please visit SAP Help Portal.

43


1/14/26, 2:18 PM

You have configured your XI system, for example, SAP NetWeaver Process Integration (SAP NetWeaver PI).

Freight bookings exist.

Optional: You have defined an EDI communication profile in Customizing for Transportation Management. For more

information, see Customizing under

## Integration

## Enterprise Services

 Define EDI Communication Profile .

## Process

1. You assign a master bill of lading number (sea transportation) or a master air waybill number (MAWB number, air

transportation) to your freight booking.

2. The sending system, for example, TM, sends the freight booking to the shipping company or airline with the service

operation TransportationOrderBookingRequest_Out.

3. The sending system receives the confirmation with the service operation

TransportationOrderBookingConfirmation_In. The carrier can accept the freight booking provisionally (waiting

list), accept it permanently, or reject it.

4. You plan freight units and assign these to your freight booking (consolidation).

5. When you have completed the planning and consolidation, you send a shipping instruction to the shipping company or

airline. The system sends a message using the service operation

TransportationOrderBookingWaybillNotification_Out..

6. In some cases, the carrier also sends a confirmation for the shipping instruction. This confirmation is also received using

the service operation TransportationOrderBookingConfirmation_In.

7. If you cancel a freight booking, the sending system cancels the freight booking with the service operation

TransportationOrderBookingCancellationRequest_Out.

  Note

Some shipping companies or airlines accept only one of the two specified messages (booking message or shipping

instruction). You can enter this information by defining an EDI communication profile in Customizing for Transportation

Management and assigning this to the shipping company or airline in your business partner master data. If you do not

assign an EDI communication profile to your shipping company or airline, TM supports both of the specified messages.

However, the shipping instruction must be sent after the booking message.

The Communication History tab page in the freight booking provides an overview of all outbound and inbound

messages related to the freight booking. For more information, see Freight Booking.

Recording of VGM Data

## Use

You can record the verified gross mass (VGM) and all related data manually and electronically and send it to your business

partners. Since July 1, 2016 this has been a requirement under the International Convention for the Safety of Live at Sea,1974

(SOLAS) before a freight container can be loaded onto a ship.

In addition to the VGM, you can also record the following data:

The person responsible and the related partner role

## The weighing date and the weighing location

This is custom documentation. For more information, please visit SAP Help Portal.

44


1/14/26, 2:18 PM

Notes and attachments, such as weighing records

## VGM cut-off dates/times

You can also specify which method you use to determine the VGM:

You can weigh the packed container.

You can weigh the contents of the container, for example, all packages and pallets as well as the dunnage and other

securing material. To calculate the VGM, you sum up all these individual weights and then add the tare weight of the

container.

If you need to weigh the container again at a later date, you can record the new VGM data in your ocean freight booking. The VGM

with the latest weighing date is displayed as the relevant weight. You can display previously recorded VGM data in a history. You can

also overwrite VGM data in your ocean forwarding order; for example, if you have received updated data from the shipper.

## Prerequisites

If you want to record notes for VGM data, you need to transport the VGM Text Schema for VGM text schema (delivery

Customizing in client 100) into your clients. For more information, see Customizing for Cross-Application Components

under  Processes and Tools for Enterprise Applications

 Reusable Objects and Functions for BOPF Environment

 Dependent Object Text Collection

 Maintain Text Schema .

If you want to use the weighing methods mentioned above, you need to transport the methods Weighing the Packed

Container and Weighing Content and Adding Tare Weight (delivery Customizing in client 100) into your clients. For more

information, see Customizing for Transportation Management under  Forwarding Order Management

 Forwarding

## Order

 Define Transportation Activities

.

## Process

Two example processes are described below.

Shipper Is Responsible for Weighing a Container (For Example When an FCL Container Is Ordered from a Logistics Service

Provider)

1. The logistics service provider (LSP) sends the ocean freight booking to the executing carrier.

2. The executing carrier specifies by when they need the VGM data at the latest from the LSP and informs the LSP of this VGM

cut-off date/time electronically or by telephone. If they inform the LSP of this date/time electronically, this date/time is

recorded in the ocean freight booking. Otherwise, this information has to be entered manually.

3. The LSP specifies when they need the VGM data from the shipper. This VGM cut-off date/time must be before the VGM cut-

off date/time specified by the executing carrier. The LSP records the date/time in the ocean forwarding order and informs

the shipper electronically or by telephone.

4. The shipper weighs the freight container and sends the VGM data to the LSP electronically or by telephone before the VGM

cut-off date/time.

5. The LSP records the VGM data in the ocean forwarding order (partner role Shipper). If the shipper has sent the VGM data

electronically this data is recorded automatically in the ocean forwarding order. The system copies the VGM data into the

container unit and updates the gross weight in the planned quantities. The system also copies the VGM data into the ocean

freight booking.

6. The LSP sends the shipping instruction containing the VGM data to the executing carrier before the VGM cut-off date/time.

LSP Is Responsible for Weighing a Container (For Example If They Are Consolidating Loose Cargo (LCL))

This is custom documentation. For more information, please visit SAP Help Portal.

45


1/14/26, 2:18 PM

1. The LSP sends the ocean freight booking to the executing carrier.

2. The executing carrier specifies by when they need the VGM data at the latest from the LSP and informs the LSP of this VGM

cut-off date/time electronically or by telephone. If they inform the LSP of this date/time electronically, this date/time is

recorded in the ocean freight booking. Otherwise, this information has to be entered manually.

3. The LSP weighs the freight container and records the VGM data in the ocean freight booking.

4. The LSP sends the shipping instruction containing the VGM data to the executing carrier before the VGM cut-off date/time.

Management of Air Freight Bookings for Airlines

## Use

You as a logistics service provider use this function to book capacity directly with an airline and then to manage the air freight

bookings. Due to the different task-specific views for air freight bookings, the function will be explained here.

## Prerequisites

If you want to print a security manifest, you need to have made the country-specific settings in Customizing for Transportation

Management. For more information, see  Freight Order Management

## Freight Booking

 Define Country-Specific Settings for

Security Manifest

.

## Features

## Capacity Management

This includes the following functions:

Use of air freight-specific codes, for example, location codes and handling codes

For more information, see Transportation-Mode-Specific Codes and Handling Codes.

## Entering Capacities

You can define the mass or volume of the required capacity and display the whole utilization. In addition, you can define the

ULD type of your unit load devices, the pivot weight, and the loading instructions for ULDs. For more information, see Rate

Definition and Maintenance.

## Drawing MAWB Numbers

You can draw master air waybill numbers from a stock. Depending on the process, you either draw these numbers manually

or the system draws them automatically:

If you create the air freight booking by using report Creating Schedule-Based Freight Documents

(/SCMTMS/MP_SCHED_CREATE_TOR), the MAWB number is drawn automatically. For more information, see

Schedule.

If you create an air freight booking directly, you can draw the MAWB number manually (under Follow-Up Actions)

When you assign a schedule to an air freight booking by specifying an air waybill stock ID, an MAWB number is

drawn automatically. For more information, see Use of Schedules.

You can also enter MAWB numbers manually. The system checks whether the number is valid.

If the number has been drawn from a stock, you can no longer change the following data:

This is custom documentation. For more information, please visit SAP Help Portal.

46


1/14/26, 2:18 PM

MAWB prefix

## Local carrier

## Purchasing organization

If you want to change this data, you must first return the MAWB number to the stock.

If you are dealing with a number that does not come from stock, or if you do not have any stock, the system displays a

checkbox in order to permit the entry of this number. For more information about MAWB stocks, see Waybill Stock

Definition.

Use of carrier categories, for example, airline codes (see Carrier Categorization)

Classifying goods, for example, with commodity item numbers (see Classification of Goods)

Printing a master air waybill or security manifest

For more information, see Printing.

Operations/Operations Outbound

This includes the following functions:

## Assigning documents to unit load devices

You can assign your carrier orders and freight units to your unit load devices. Furthermore, you can also show mixed unit

load devices (see Mixed Unit Load Device).

## Communicating with the warehouse

After you have received confirmation from the warehouse, you can set the appropriate status.

For more information about the air freight-specific status, see Statuses of Business Documents.

Entering discrepancies (see Discrepancies and Events)

Entering actual quantities (see Quantities and Capacities)

Creating freight orders for pick-up and delivery (see Pick-up and Delivery Freight Orders)

In addition, the following functions are available for both levels:

Functions in the area of air cargo security (see Air Cargo Security)

The system derives the IATA agent code, the agent's CASS account, and the regulated agent from the issuing carrier. For

more information, see Business Partner and Definition of Business Partners.

The complete overview of the booking contains all of these functions. The following functions are also available:

Charge Correction Advice Management

## More Information

Air Freight-Specific Consolidation Processes

## Co-Load

## Publication and Locking of Air Freight Bookings

This is custom documentation. For more information, please visit SAP Help Portal.

47


1/14/26, 2:18 PM

## Nature of Goods

Business Partners and Related Data in Air Bookings

## Concept

In air freight scenarios, different business partners play a role. They can differ to which of the following scenarios you use:

Standard scenario (consolidation, B2B, or direct shipment) or

## Co-load scenario

The following graphic shows the relevant business partners in each scenario:

The following table shows air-specific fields that are available on the Booking tab page of the air booking. For the business partner

fields, the table maps the business partners to the corresponding business partner roles in Transportation Management (TM).

Further, it explains their meaning and provides examples.

## Field Name

Business Partner Role on

Meaning

## Example

## Header Level

Consolidator (only relevant for

## Carrier

Business partner number of the

XYZ_ATL (sales office of partner

co-load scenario)

consolidator. The consolidator

LSP XYZ in Atlanta)

is the partner LSP of the

This is custom documentation. For more information, please visit SAP Help Portal.

48


1/14/26, 2:18 PM

## Field Name

Business Partner Role on

Meaning

## Example

## Header Level

coloader (LSP who uses TM).

The consolidator books the

required capacity with the

airline and has to settle for it

with the airline. Note that the

consolidator is only relevant in

co-load scenarios. The coloader

creates the air booking in TM

and sends it to the consolidator.

Typically, the coloader prints the

air waybill (AWB) and sends the

Cargo-IMP/XML message FWB

(electronic message

representing the AWB) to the

airline. Further, the coloader is

responsible for the hand-over of

the cargo to the airline. The

coloader settles the AWB with

the consolidator. In this

scenario, the contract is

between the coloader and the

consolidator. The consolidator

has a contract with the airline.

Note that in the standard

scenario, the business partner

role Carrier is used differently.

For more information, see

Issuing Carrier Airline

Code/Local Carrier below.

Issuing Carrier Airline

n/a

Worldwide unique IATA airline

XX (representing airline XX)

Code/Local Carrier

Issuing Carrier Airline

Code/Local Carrier

code of the “commercial”

carrier (airline). The

"commercial" carrier is

responsible, for example, for

accepting the air booking and

providing AWB number ranges.

The export booking is

subcontracted to the local

branch of this airline.

Standard scenario:

Executing Carrier,

Carrier (cannot be

edited)

Co-load scenario:

## Executing Carrier

Business partner number of the

XX_ATL (business partner

local branch of the

representing the sales office of

“commercial” carrier (airline) at

airline XX in Atlanta)

the airport (see Issuing Carrier

Airline Code/Local Carrier).

It is either the sales office of the

airline at the airport or the

general sales agent (GSA) who

presents the airline.

In standard scenarios, it is the

party to whom the air booking is

subcontracted by the LSP who

uses TM. In a co-load scenario, it

This is custom documentation. For more information, please visit SAP Help Portal.

49


1/14/26, 2:18 PM

## Field Name

Business Partner Role on

Meaning

## Example

## Header Level

is the party to whom the air

booking is subcontracted by the

consolidator.

Local carriers can have one or

multiple warehouses for

receiving the cargo of their

customers at or near the

airport. For the physical

handling of the cargo they

frequently use ground handler.

Note that this is not the carrier

who actually executes the flight.

The local carrier is responsible

for the administrative execution,

for example, issuing the AWB.

MAWB No.

n/a

This field contains two parts:

AWB prefix: 999 representing

First Carrier Airline

n/a

Code/Flight No./Global Carrier

AWB prefix: IATA AWB

airline XX

prefix of the issuing

Master air waybill number:

carrier, that means, the

12345675 (serial number plus

first 3 numbers of the

check digit)

AWB or MAWB.

Master air waybill

number: A 7 digit serial

number plus check digit

(modulus-7 check digit)

of AWB or MAWB.

Export Booking:

ZZ (representing the airline ZZ)

Worldwide unique IATA airline

code of the carrier that

executes the first flight.

Identical to the information in

the first stage of the Carrier

Routing table. This simplifies

entering this code if only one

flight exists. If you change this

code on the Booking tab page,

the value in the Carrier Routing

table is updated automatically

and vice versa.

Last Carrier Airline Code/Flight

n/a

Import Booking:

ZZ (representing the airline ZZ)

## No./Global Carrier

Worldwide unique IATA airline

code of the carrier that

executes the last flight. Identical

to the information in the last

stage of the Carrier Routing

table. This simplifies entering

this code if only one flight

exists. If you change this code

on the Booking tab page, the

This is custom documentation. For more information, please visit SAP Help Portal.

50


1/14/26, 2:18 PM

## Field Name

Business Partner Role on

Meaning

## Example

## Header Level

value in the Carrier Routing

table is updated automatically

and vice versa.

First Carrier Airline Code/Flight

n/a

Export Booking:

4711 (representing the flight

No./Global Carrier

number of airline ZZ)

Flight number of the first flight.

Identical to the information in

the first stage of the Carrier

Routing table. This simplifies

entering this number if only one

flight exists. If you change this

number on the Booking tab

page, the value in the Carrier

Routing table is updated

automatically and vice versa.

Last Carrier Airline Code/Flight

n/a

Import Booking:

4711 (representing the flight

No./Global Carrier

number of airline ZZ)

Flight number of the last flight.

Identical to the information in

the last stage of the Carrier

Routing table. This simplifies

entering this number if only one

flight exists. If you change this

number on the Booking tab

page, the value in the Carrier

Routing table is updated

automatically and vice versa.

First Carrier Airline Code/Flight

n/a

Export Booking:

ZZ_GC (business partner

## No./Global Carrier

representing the headquarters

of airline ZZ)

Business partner number of the

carrier that executes the first

flight. Identical to the

information in the first stage of

the Carrier Routing table. This

simplifies entering this number

if only one flight exists. If you

change this number on the

Booking tab page, the value in

the Carrier Routing table is

updated automatically and vice

versa.

Last Carrier Airline Code/Flight

n/a

Import Booking:

ZZ_GC (business partner

## No./Global Carrier

Business partner number of the

carrier that executes the last

of airline ZZ)

representing the headquarters

flight. Identical to the

information in the last stage of

the Carrier Routing table. This

simplifies entering this number

if only one flight exists. If you

change this number on the

Booking tab page, the value in

the Carrier Routing table is

This is custom documentation. For more information, please visit SAP Help Portal.

51


1/14/26, 2:18 PM

## Field Name

Business Partner Role on

Meaning

## Example

## Header Level

updated automatically and vice

versa.

Origin Organization

## Export Organization

Business partner number of the

ABC_ATL (export purchasing

purchasing organization

organization in Atlanta of LSP

responsible for the air booking

ABC who uses TM)

at export side. The origin

organization creates the export

booking in TM.

Destination Organization

Import Organization

Business partner of the

ABC_FRA (import purchasing

purchasing organization

organization in Frankfurt of LSP

responsible for the air booking

ABC who uses TM)

at import side. The destination

organization creates the import

booking in TM.

Issuing Carrier's Agent

Issuing Carrier's Agent

Business partner number of the

Standard scenario: ABC_ATL

Co-load scenario: XYZ_ATL

IATA cargo agent who issues the

AWB as agent of the airline,

handles other shipping

formalities and hands over the

cargo to the airline. The issuing

carrier’s agent is registered in

the IATA Cargo Agency list and

has an IATA agent number.

In a standard scenario, it

is the origin

organization of the LSP.

In a co-load scenario, it

is the consolidator.

IATA Agent Code/Agent’s CASS

n/a

IATA agent code representing

01-1 7015

## Account

the company of the issuing

carrier's agent. It contains the

first seven digits of the IATA

agent number:

Country or region

designator consisting of

the 2-digit IATA country

or region and the 1-digit

CASS area.

4-digit IATA number

representing the

company.

This code is derived from the

business partner master data of

the issuing carrier’s agent.

IATA Agent Code/Agent’s CASS

n/a

IATA CASS account of the

1234

## Account

issuing carrier's agent. It

contains the four last digits of

the IATA agent number:

This is custom documentation. For more information, please visit SAP Help Portal.

52


1/14/26, 2:18 PM

## Field Name

Business Partner Role on

Meaning

## Example

## Header Level

3 digit CASS address

code representing the

branch office or branch

offices of the IATA agent

1 check digit

This number is derived from the

business partner master data of

the issuing carrier’s agent.

Account No. with Carrier

n/a

Account number of the

## XX_ABC_ATL

purchasing organization with

the issuing local carrier.

This number is derived from the

business partner master data of

the local carrier for the

responsible purchasing

organization (Vendor Company

Org. Data tab page).

Regulated Agent

n/a

Regulated agent number of the

US/RA/00123-19/0219

issuing carrier’s agent.

This number is derived from the

business partner master data of

the issuing carrier’s agent.

More Information

## Co-Load

Direct Shipment

Air Cargo Security

## Use

The air cargo security function in Transportation Management (TM) helps you to ensure that official security requirements for air

cargo have been met prior to transportation.

## Features

## Air Cargo Security Check and Statuses

If you enable the air cargo security check, the air cargo security status and the country-specific or region-specific security status

must be specified in the relevant forwarding order, freight units, and air freight booking. You also activate automatic checks that

prevent further processing if data is missing or inconsistent. You enable the air cargo security check for your business document

types in Customizing for Transportation Management. In addition, you define the required country-specific or region-specific

security statuses and you assign an air cargo security status to each of them. The following air cargo security statuses are

available:

This is custom documentation. For more information, please visit SAP Help Portal.

53


1/14/26, 2:18 PM

Secure for Passenger Aircraft (High Risk Cargo) (SHR)

Secure for Passenger Aircraft (SPX)

Secure for Cargo Aircraft (SCO)

Not Secure (NSC)

  Note

The status Secure for Passenger Aircraft (High Risk Cargo) (SHR) is relevant for freight units only, not for freight bookings

In Customizing for Transportation Management, you can specify that planning and execution are to be blocked if a freight unit has

a specific air cargo security status. In addition, planning is automatically blocked if the air cargo security status has not been set in

the freight units or the air freight booking. During planning, the system checks if the air cargo security status of the freight units

and the air freight booking are compatible. If the statuses are incompatible, the system blocks planning in the case of automatic

planning, or issues error or warning messages depending on the user’s authorizations in the case of manual planning.

When you enable the air cargo security check for road freight orders, you can set the security status of a road freight order to

either Secure or Not Secure. If a road freight order has manifest status Created and you set the security status to Not Secure,

then for all freight units assigned to that freight order, the system changes the air cargo security status to Not Secure.

## Cargo Handover Party

Information about the cargo handover party is specified in the forwarding order on the Air Cargo Security tab page. This data

comprises the security status of the cargo handover party (for example, known shipper or regulated agent); the official code used

to identify the cargo handover party (for example, known shipper code or regulated agent code); and the expiry date of the security

status.

You can store this data in the master data for the pick-up location or the business partner and have the system copy the data to the

forwarding order. The regulations in the countries or regions to which you transport cargo determine whether you choose the

location or business partner master data. For example, in the United States, the authorities are interested in the security status of

the cargo handover party for a specific pick-up location. In other countries or regions, the authorities are interested in the overall

security status of the cargo handover party, regardless of the pick-up location.

## Shipper Known Long Enough

The system can calculate automatically whether you have known a shipper long enough in order to accept cargo from the shipper

as secure. For example, the relevant authority in the United States has defined that if cargo is to be transported to the United

States, a logistics service provider (LSP) must have known a shipper for a minimum of 180 days on the date the cargo is picked up.

If the LSP has not known the shipper long enough, the LSP must treat the cargo as non-secure, even if the shipper is registered as a

known shipper in the United States.

If you have made the required settings in Customizing for Transportation Management, information about whether you have

known a shipper long enough is automatically displayed in the forwarding order on the Air Cargo Security tab page. The system

also checks if you have known a shipper long enough during planning, and after planning if relevant changes are made. Note that

the system checks if an LSP has known a shipper long enough only if a country-specific or region-specific offset has been entered

for the country or region of the destination location, transit location, or intermediate stop.

Change the Country-Specific or Region-Specific Air Cargo Security Status for Multiple Freight Units

Previously, the system allowed you to change the Country-Specific or Region-Specific Air Cargo Security Status of individual

freight units only – it was not possible to simultaneously change this status for multiple freight units. It is now possible to set the

Country-Specific or Region-Specific Air Cargo Security Status of two or more freight units in a single action.

## Air Cargo Security Authorization Check

This is custom documentation. For more information, please visit SAP Help Portal.

54


1/14/26, 2:18 PM

You can manage the group of persons authorized to manually assign unsafe items to an air freight booking.  The Air Cargo Security

Authorization Check works in conjunction with the Air Cargo Security (ACS) Check.

The ACS Check verifies a user's authorization according to organization unit.  If you enable the Air Cargo Security Authorization

Check for a freight booking type, the system instead runs an authorization check on any user working with that freight booking

type, according to the user's role assignment.

## More Information

Configuration of Air Cargo Security

Air Cargo Security in Business Document Processing

## Configuration of Air Cargo Security

The following settings enable you to use the air cargo security function for your business documents.

## Air Cargo Security Check

You have selected the Enable Air Cargo Security Check checkbox in Customizing for the forwarding order type and air freight

booking type. You define the business document types in Customizing for Transportation Management as follows:

Forwarding Order Management

## Forwarding Order

 Define Forwarding Order Types

Freight Order Management

## Freight Booking

 Define Freight Booking Types

Freight Order Management

## Freight Order

## Define Freight Order Types

Note that if you do not enable the check, the air cargo security fields are not available in the business documents.

## Air Cargo Security Statuses

You have defined country-specific or region-specific security statuses and assigned an air cargo security status to each of them in

Customizing for Transportation Management under  Basic Functions

## Security

 Define Air Cargo Security Statuses .

For each combination of country-specific or region-specific security status and air cargo security status, you can define that

planning and execution are to be blocked for the relevant freight units. You can also define that the cargo has been screened by the

logistics service provider (LSP). If you select this checkbox, the system does not check if you have known the shipper long enough

during and after planning.

Note that the system checks if an LSP has known a shipper long enough only if a country-specific or region-specific offset has

been entered for the country or region of the destination location, transit location, or intermediate stop.

## Air Cargo Security Status in Schedules

If you create air freight bookings from master flight schedules, you have specified a default air cargo security status in the master

flight schedule. Note that if you change the air cargo security status in the schedule after the system has created an air freight

booking, the booking is not automatically updated.

To create master flight schedules, open the Create Schedule app form the launchpad.

For more information about schedules, see Creating Schedules.

This is custom documentation. For more information, please visit SAP Help Portal.

55


1/14/26, 2:18 PM
## Regulated Agent Code of LSP

If you are a regulated agent and you want the system to enter your regulated agent code automatically when you create a

forwarding order, you have entered the code in the business partner master data for the sales organization.

To define business partners, open the Define Business Partner app from the launchpad. Using the business partner role

Organizational Unit, you enter the regulated agent code on the Identification tab page.

When you create a forwarding order, the system copies the code to the General Data tab page under Organizational Data. If

required, you can change this value in the forwarding order.

## Cargo Handover Party

If you want the system to enter the details of the cargo handover party automatically when you create a forwarding order, you have

entered the data in the master data for the pick-up location or the business partner (shipper) as follows:

To define locations, open the Define Location app from the launchpad. You enter the data on the TM tab page.

To define business partners, open the Define Business Partner app from the launchpad. Using the business partner role

Vendor, you enter the data on the Vendor Data tab page.

In addition, you have defined that the air cargo security master data for the pick-up location or the business partner is to be copied

to the forwarding order. You do this by selecting the Copy Air Cargo Security Data checkbox in Customizing for the forwarding

order type.

In the business partner master data for the shipper, you can also specify the date as of which you have known the shipper. This

enables the system to calculate whether you have known the shipper long enough.

## Shipper Known Long Enough

To enable the system to calculate whether you have known a shipper long enough in order to accept cargo from the shipper as

secure, you have made the following settings:

In the business partner master data for the shipper, you have specified the date as of which you have known the shipper.

In Customizing for Transportation Management under  Basic Functions

## Security

## Define Offsets for Calculating

Known Shipper Status , you have defined country-specific or region-specific offsets.

The system checks if an LSP has known a shipper long enough only if a country-specific or region-specific offset has been entered

for the country or region of the destination location, transit location, or intermediate stop.

Note that these settings relate to shippers that are classified as known shippers by the relevant authority.

## Screening Methods

To ensure compliance with security and safety regulations, you have defined air cargo screening methods in Customizing for

Transportation Management under

 Basic Functions

## Security

  Define Air Cargo Screening Methods .

You enter a description for each screening method. In addition, you can specify that a text is required. This ensures that you have to

enter an additional text specifying the screening method on the Air Cargo Security tab page within the forwarding order or the

freight unit.

## Screening Exemptions

This is custom documentation. For more information, please visit SAP Help Portal.

56


1/14/26, 2:18 PM

To indicate exemptions from screening or identify alternative screening methods required by cargo and mail of a special nature,

you have defined air cargo screening exemptions in Customizing for Transportation Management under  Basic Functions

## Security

 Define Air Cargo Screening Exemptions .

You enter a description for each screening exemption.

Air Cargo Security in Business Document Processing

## Use

If you enable the air cargo security check, the system checks that the required air cargo security data is entered during business

document processing and that the air cargo security statuses of the relevant business documents are compatible.

## Prerequisites

You have enabled the air cargo security check and made the required settings. For more information, see Configuration of Air Cargo

Security.

## Process

1. You create a forwarding order with one or more freight units.

You use a forwarding order type for which the air cargo security (ACS) check is enabled and for which the master data for

the pick-up location or business partner is to be copied to the forwarding order.

The system does the following in the forwarding order:

Enters the regulated agent code for the sales organization on the General Data tab page under Organizational Data.

If required, you can change this value.

Enters the master data for the pick-up location or business partner on the Air Cargo Security tab page under Cargo

Handover Party. If required, you can change these values.

Shows whether you have known a shipper long enough in order to accept cargo from the shipper as secure. The

system checks if an LSP has known a shipper long enough only if a country/region-specific offset has been entered

for the country or region of the destination location, transit location, or intermediate stop.

On the Air Cargo Security tab page under Known Shipper Details, the system displays the date as of which you

have known the shipper. If you have known the shipper long enough based on this date and the relevant

country/region-specific offset defined in Customizing for Transportation Management, the system selects the

Known Long Enough checkbox. If you have not known the shipper long enough or if you have not specified a

country/region-specific offset, it does not select the checkbox.

2. You select the country/region-specific security status and the system determines the required air cargo security status.

You select the country/region-specific security status as follows:

If the forwarding order contains only one freight unit, you select the country/region-specific security status in the

forwarding order on the Air Cargo Security tab page. The freight unit inherits the country/region-specific security

status and the air cargo security status from the forwarding order.

If the forwarding order contains more than one freight unit, you select the country/region-specific security status in

each individual freight unit. The forwarding order inherits the country/region-specific security status and the air

cargo security status from the freight units. If the freight units have different country/region-specific security

statuses, the system displays the value Multiple as the country/region-specific security status in the forwarding

This is custom documentation. For more information, please visit SAP Help Portal.

57


1/14/26, 2:18 PM

order. If the freight units have different air cargo security statuses, the system displays the least secure air cargo

security status in the forwarding order.

In the forwarding order, the air cargo security status is displayed on the Air Cargo Security tab page and on the Statuses

tab page. In the freight unit, the country/region-specific security status is displayed on the General Data tab page, and the

air cargo security status is displayed on the Statuses tab page. Note that prior to determining the air cargo security status,

the system displays the status Not Checked.

If you have specified in Customizing that planning and execution are to be blocked for a specific air cargo security status,

the system blocks planning and execution as soon as the relevant status is set in the freight unit.

3. You select one or more air cargo security screening methods, if applicable, provided that no air cargo security screening

exemption code applies. In both the forwarding order and the freight unit, you insert screening methods on the Air Cargo

Security tab page and add an additional free text, if required.

You select the air cargo security screening methods as follows:

If the forwarding order contains only one freight unit, you select the screening methods in the forwarding order. The

freight unit inherits the screening methods from the forwarding order.

If the forwarding order contains more than one freight unit, you select the screening methods in each individual

freight unit.

4. You select an air cargo security screening exemption code, if applicable. In this case, you cannot select any screening

methods. You can select a maximum of two screening exemption codes. In both the forwarding order and the freight unit,

you select screening exemption codes on the Air Cargo Security tab page.

You select the air cargo security screening exemption codes as follows:

If the forwarding order contains only one freight unit, you select the screening exemption codes in the forwarding

order. The freight unit inherits the screening exemption codes from the forwarding order.

If the forwarding order contains more than one freight unit, you select the screening exemption codes in each

individual freight unit.

5. You create an air freight booking.

You select the air cargo security status in the air freight booking on the Booking tab page. If you have created an air freight

booking from a master flight schedule and you have specified an air cargo security status in the schedule, the system

automatically enters this default status. You then select the corresponding country/region-specific security status on the

Booking tab page.

The air cargo security status and the country/region-specific security status are displayed on the Statuses tab page in the

air freight booking.

6. You carry out planning for the freight units.

Automatic planning can be performed only if the air cargo security statuses of the freight units and the air freight booking

are compatible. For example, the freight unit has the status Secure for Passenger Aircraft (SPX) and the air freight booking

has the status Secure for Cargo Aircraft (SCO).

If you carry out manual planning and the statuses are not compatible, the system issues either warning messages or error

messages depending on your user authorizations. If you are assigned to the execution organization that is specified in the

air freight booking, the system issues warnings. If the Air Cargo Security Authorization Check for a freight booking type has

been enabled, the system instead runs an authorization check according to your role assignment. If you have been assigned

a role that is allowed to manually assign unsafe items to an air freight booking the system issues warnings. Otherwise, the

system issues errors and planning is blocked.

Note that if the freight unit or the air freight booking has the air cargo security status Not Checked, planning is restricted to

authorized users. If you enable the Air Cargo Security Authorization Check for a freight booking type, the system checks

users’ role assignments to determine if that user is authorized to work with that freight booking type.

This is custom documentation. For more information, please visit SAP Help Portal.

58


1/14/26, 2:18 PM

If you have specified a country/region-specific offset for the country or region of the destination location, transit location, or

intermediate stop, the system checks if you have known a shipper long enough during planning, and also after planning if

you change the route or if you change the air cargo security status or country/region-specific security status of a business

document. If you have not known the shipper long enough, the system issues an error message. The system skips this

check if you have specified in Customizing for the relevant air cargo security status that the cargo has been screened by the

logistics service provider.

Freight Order Security Status

## Use

This function determines whether the security status of all of the freight units assigned to a freight order is secure or not secure.

A freight order, when created, has the security status “Initial”. A user must set the freight order security status to either Secure or

Not secure. Once a user sets the freight order security status the system records the identity of the user and the date and time at

which the user made the assignment.

The Regulated Agent Code (RAC) of the carrier can determine the security status of a freight order. A freight order identifies the

carrier and, where that carrier uses a subcontractor, the executing carrier. Depending on the laws in your country or region, the

RAC of a carrier, executing carrier, or carrier who has signed a valid haulier agreement can be an indicator that the freight order is

secure. If an executing carrier is defined for a freight order, the system determines the RAC value for that executing carrier from

Master Data. Otherwise, the system uses the RAC of the carrier.

A carrier with a valid regulated agent code, is permitted to transport cargo under secure conditions and hence keep the security

status of the individual cargo intact. However this has to be verified upon delivery, for example, an employee must inspect any seal

change and verify that it is appropriately documented. If there are any irregularities, all cargo is considered as not secure and the

business user must record this in the system.

## Prerequisites

You have defined freight order types in Customizing for Transportation Management under  Freight Order Management

 Freight

## Order

 Define Freight Order Types .

## Activities

Once you have created a freight order, you can either first set the freight order’s air cargo security status to Not Secure and then

set its Manifest Status to Created, or alternatively, first set its Manifest Status to Created, and then set its air cargo security status

to Not Secure. At all times the last user to change the Cargo Security Status is recorded.

First set the Security Status to not Secure and then set the Manifest Status to Created

1. You set the Security Status of the freight order to Not Secure.

2. The system records the assignment and records you as the user responsible for changing the freight order security status.

3. You set the Manifest Status of the freight order to Created.

4. The system asks you to confirm that you want to change the Air Cargo Security Status of assigned freight units to Not

Secure. If you confirm:

a. The system sets the Air Cargo Security Status of all assigned freight units to Not Secure.

b. The system deletes the country/region-specific security status for all assigned freight units.

This is custom documentation. For more information, please visit SAP Help Portal.

59


1/14/26, 2:18 PM

c. The system records you as the user responsible for changing the air cargo security status of all assigned freight

units.

d. If the affected freight units are assigned to air bookings, these air bookings are blocked for execution as the freight

units are now not secure.

5. Otherwise: The Manifest Status remains unchanged.

First set Manifest Status to Created and then set Security Status to Not Secure

1. You set the Manifest Status of the freight order to Created.

2. You set the Security Status of the freight order to Not Secure.

3. The system asks you to confirm that you want to change the Air Cargo Security Status of assigned freight units to Not

Secure. If you confirm:

a. The system records the assignment and records you as the user responsible for changing the security status of the

freight order.

b. The system sets the Air Cargo Security Status of all assigned freight units to Not Secure.

c. The system deletes the country/region-specific security status for all assigned freight units.

d. The system records you as the user responsible for changing the air cargo security status of all assigned freight

units.

e. If the affected freight units are assigned to air bookings, these air bookings are blocked for execution as the freight

units are now not secure.

4. Otherwise: The security status of the freight order remains unchanged.

Co-Load

## Use

In this process, you as the logistics service provider can use the air waybill stock and contract of another logistics service provider

who is carrying out a consolidation or making a direct shipment (consolidator). This means that you want to transport goods with a

specific flight, however, you don't book directly with the carrier but instead with the consolidator.

The following restrictions apply to this process:

You may not send the air freight booking yourself. The consolidator does this on your behalf.

You may not draw the MAWB numbers from the stock yourself or return them to the stock.

This process does not support any schedules.

## Prerequisites

In Customizing for the freight booking type, you have specified that this is a co-load. For more information, see Customizing

for Transportation Management under  Freight Order Management

## Freight Booking

 Define Freight Booking Types .

You have defined a business partner with the Carrier role. You have also specified the IATA agent code, the regulated agent,

and the agent's CASS account for the business partner. For more information, see Definition of Business Partners and

Business Partner.

This is custom documentation. For more information, please visit SAP Help Portal.

60


1/14/26, 2:18 PM
## Process

1. Creating the air freight booking

Create an air freight booking manually. Here you specify the following:

Consolidator

## MAWB number

You get this number from the consolidator. The system checks the MAWB number for validity.

## Issuing carrier's agent

Enter the consolidator. In this scenario the issuing carrier's agent is the consolidator. The system automatically

draws the IATA agent code, the the regulated agent, and the agent's CASS account.

The airline (issuing carrier) is displayed as the communication party because the message is to be sent to the airline.

2. Scheduling the air freight booking

You schedule the air freight booking. This means that you assign freight unit stages (that is house air waybills) to the air

freight booking and then distribute these to the unit load devices if necessary.

3. Sending the message

You send the message to the airline.

Handling Codes

## Use

You can use handling codes to model certain properties of your freight, such as whether unit load devices can only be loaded on the

lower deck. Handling codes are supported for air freight bookings and freight orders only.

  Note
The relevant tab page is not displayed on the user interface for freight orders until you have personalized your user interface

accordingly.

## Prerequisites

You have defined handling codes in Customizing for Transportation Management. For more information, see Customizing

under  Basic Functions

## General Settings

## Define Handling Codes . You can also specify here whether handling codes

are to be used internally only or also externally. Only external handling codes are transferred when air freight bookings are

sent.

You have optionally defined a handling code constraint profile in Customizing for Transportation Management. For more

information, see Customizing under  Basic Functions

## General Settings

 Define Handling Code Constraint Profiles .

## Features

If your forwarding order contains handling codes, the system copies these to the corresponding freight units automatically. If you

assign this forwarding order to a freight order or an air freight booking, the system checks the handling codes for the freight units

based on the handling code constraints in the freight order or air freight booking. For more information, see Creation of a

Forwarding Order.

This is custom documentation. For more information, please visit SAP Help Portal.

61


1/14/26, 2:18 PM

You can restrict the handling codes permitted for freight orders and air freight bookings by defining constraints. You enter

handling codes and constraints either manually or copy them:

## Manual entry

You can enter handling codes and constraints manually in the freight order or air freight booking.

Copying from the schedule (air freight booking only)

If you create an air freight booking by assigning freight units to a departure, the system copies the handling codes and

constraints automatically from the flight schedule-based allocation. For more information about transportation allocations,

see Transportation Allocation.

Copying from the handling code constraint profile (freight order only)

If you have defined a handling code constraint profile and assigned it to a means of transport in Customizing, the system

applies the handling codes and constraints from this profile when you specify this means of transport in your freight order.

If you subsequently change these handling codes, the system treats the handling codes as though they were entered

manually.

Publication of Air Freight Bookings

## Use

You can make air freight bookings for particular organizational units and business partners visible, or restrict the visibility.

## Prerequisites

You have made the following settings in the freight booking type:

You have specified the creation strategy PUBL_CREA (only for automatic publication). This creation strategy is part

of the standard system. For more information about this creation strategy, see SAP Note 1803372

.

To be able to fix air freight bookings, you have selected the Fix Document if Capacity Planning Closed option in the

Fix Booking field.

  Note

You have not chosen the option Initial Status "Unpublished" (Planning Block) in the Immediate Processing field, as

otherwise the air freight booking cannot be published due to the planning block.

For more information, see Customizing for Transportation Management under  Freight Order Management

 Freight

## Booking

 Define Freight Booking Types .

The air freight booking must cover the following data so that you (or the system) can to publish it:

Capacity (weight and volume)

Origin organization

Flight number and date

IATA location code

Local carrier

## Loading type

This is custom documentation. For more information, please visit SAP Help Portal.

62


1/14/26, 2:18 PM

Contract basis

## Service level

For automatic publication, this data originates either from the forwarding order or the master flight schedule.

In addition, you must have defined a waybill stock so that the system can automatically draw master air waybill numbers

(see Waybill Stock Definition).

You have defined the required forwarding house both as organizational unit and business partner, and assigned them to

each other. You have also selected the Consider Organization Unit of User field in the freight booking type. These two

prerequisites are only required for automatic publication with restriction. For more information, see Customizing for

Transportation Management under  Master Data

 Organizational Management

 Organizational Model

## Create

Organizational Model

.

If you want to use automatic publication with report /SCMTMS/MP_SCHED_CREATE_TOR, you must have specified a

document type in your schedule type that allows publication.

## Features

## Manual Publication

Whether an air freight booking has already been published or not, you can see in the Set Status field which publishing options are

available.

If the air freight booking has not yet been published, the system sets a planning block for the air freight booking, meaning other

organizational units and business partners can no longer use it as they cannot assign freight units. It also prevents you from

selecting it in a forwarding order.

If you select either the option Set to Published or Set to Published with Restriction for a non-published air freight booking, the

system checks whether the fields mentioned under prerequisites contain valid data. If all checks are successful, the system

removes the planning block. The air freight booking is now either visible for all organizational units and business partners, or for

only particular organizational units and business partners:

## Unrestricted visibility

If you have not made an entry on the Restriction to Organizational Units tab, the air freight booking is visible without

restriction.

## Restricted visibility

If you have made at least one entry on the Restriction to Organizational Units tab, the air freight booking is visible for only

particular organizational units and business partners. You can enter the forwarding houses from the forwarding order. If you

have specified an origin organization in the air freight booking, the system automatically copies this to the air freight

booking.

If you want to reset the publication, choose Set to Not Published.

Once capacity planning has been completed, you can choose the Set to Capacity Planning Finished option. The system fixes your

air freight booking. This means it is no longer available for other organizational units and business partners and you can no longer

use it in planning.

Automatic Publication

You have the following options:

Automatic publication when creating the air freight booking from the forwarding order

This is custom documentation. For more information, please visit SAP Help Portal.

63


1/14/26, 2:18 PM

You create an air freight posting for the main carriage. The system publishes it automatically. However, the visibility is

restricted to the forwarding house that the system has copied from the forwarding order.

Automatic publication when creating the air freight booking using report /SCMTMS/MP_SCHED_CREATE_TOR

You execute the report to create air freight bookings based on a particular master flight schedule. In doing so, you specify

that master air waybill numbers are to be drawn. The system creates the air freight bookings based on your master flight

schedule, and draws the master air waybill numbers. It automatically publishes the air freight bookings. However, the

visibility is restricted to the forwarding house drawn. For more information about this report, see Schedule.

## More Information

Interaction Between Organizational Units

For more information, see also SAP Note 1806463

.

LCL Freight Bookings

## Use

If the quantities contained in your LCL forwarding orders (LCL = Less Than Container Load) for a destination location are

insufficient for processing as an FCL freight booking (FCL = Full Container Load), you can give them to another carrier. In this case

you create an LCL freight booking to be able to specify or display all relevant data, for example:

Port of loading and discharge

## Freight terms

## Port of entry and exit

The scenario described here relates to sea traffic.

## Features

In this case, the subcontracted carrier consolidates the goods into one container. You receive the container ID and the name of the

carrier electronically. Alternatively, you can enter this data manually in the LCL freight booking. This way you can recognize which

container contains your goods and who is responsible for them.

If you set the status Ready for Transportation Execution manually or the system sets it automatically, the system performs a

check. If the freight booking contains containers, an error message is issued.

Buyer's Consolidation is not supported for LCL freight bookings. Cargo management is not advisable for LCL freight bookings.

You can convert an LCL freight booking into a FCL freight booking by changing the shipping type of the freight booking.

FCL Freight Bookings

## Use

You can create FCL freight bookings in the following ways:

Creating them from an FCL forwarding order (FCL = Full Container Load)

This is custom documentation. For more information, please visit SAP Help Portal.

64


1/14/26, 2:18 PM

Creating them for the consolidation of LCL forwarding orders (LCL = Less Than Container Load)

The scenario described here relates to sea traffic.

## Features

## Creation from an FCL Forwarding Order

In this scenario, the customer has already requested FCL, that is, the forwarding order is an FCL forwarding order that has the

shipping type FCL. You create the FCL freight booking directly from the FCL forwarding order by creating a new freight booking for

the main carriage transportation stage or by choosing an existing freight booking. The carrier confirms the FCL freight booking and

may already communicate certain details, such as the container ID. In addition, the carrier informs you about changed container

categories, for example. Container categories are defined by linking equipment types (such as CN) and equipment groups (such as

20G0). If you now change this data in the FCL freight booking, the system automatically adopts the data in the freight units

belonging to the freight booking and in all relevant documents. The changed data is displayed in the FCL forwarding order along

with the original data. If you then change the original data in the FCL forwarding order, it is no longer adopted in the follow-on

documents (freight booking, freight unit, and freight order).

## Creation for Consolidation of LCL Forwarding Orders

In this scenario, you consolidate multiple LCL forwarding orders (forwarding orders that have shipping type LCL) into one FCL

freight booking. You create the FCL freight booking in one of the following ways:

In the transportation cockpit; you also assign freight units there.

On the user interface for creating freight bookings, you assign freight units on the Items tab page (sea transportation) or

the Capacity and Cargo tab page (air transportation).

From the LCL forwarding order; you create an FCL freight booking on the Actual Route tab page by choosing  Freight

## Document

 Create . For more information, see Direct Creation of Freight Documents and Selection of Schedules.

  Note

The Items tab page replaces the Cargo Management tab page in the ocean freight booking. You can personalize your user

interface in such a way that the system displays the old Cargo Management tab page.

Depending on the movement type of the FCL freight booking, you can create freight orders for pick-up and delivery (see Pick-up

and Delivery Freight Orders).

If you have created the container, you can create a freight order from the sea freight booking for this container for the consolidated

on-carriage (see Buyer's Consolidation).

Shipper's Declaration

## Use

The system can create a shipper's declaration for dangerous goods in a freight booking. The International Air Transport Association

(IATA) requires that all shipments tendered to air carriers and air freight forwarders classified by regulation as dangerous goods

are accompanied by the IATA shipper's declaration for dangerous goods. The shipper is responsible for correctly and accurately

completing the form in accordance with current IATA requirements and for ensuring that all requirements have been met including

packaging, labelling, and product information.

This is custom documentation. For more information, please visit SAP Help Portal.

65


1/14/26, 2:18 PM

Based on the freight booking, the system looks up the relevant dangerous goods master and generates a declaration that specifies

the nature and quantity of dangerous goods. The shipper's declaration also provides information about the type of packing

material.

You can view this document in the Output Management tab of the freight order.

In endorsing this document, you declare that all applicable air transport requirements have been met.

As the IATA shipper's declaration for dangerous goods is a complex document, SAP provides a template which must be

implemented and reviewed by the shipper. The shipper must adapt the form according to its own processes, with particular

attention to the packing function and to country-specific or region-specific deviations.

## Integration

Shipper's declaration is integrated with Sales and Distribution (SD) and Materials Management (MM) based on the sales order

business object.

## Prerequisites

You have completed the necessary configuration of Output Management.

You have specified the necessary output profile for the freight booking. For more information see Customizing for Transportation

Management under  Freight Order Management

## Freight Booking

## Define Freight Booking Types

You have specified the correct action definition for post processing framework (PPF) settings. For more information see

Customizing for Transportation Management under  Cross-Application Components

 Processes and Tools for Enterprise

## Applications

 -> Reusable Objects and Functions for BOPF Environment

 PPF Adapter for Output Management

 Maintain

## PPF Settings

You have specified the necessary action setting and action definition (/SCMTMS/PRINT_SHPRS_DCL) for the output agents of

relevant business objects, for example transportation order. For more information see Customizing for Transportation

Management under  Cross-Application Components

 Processes and Tools for Enterprise Applications

## Reusable Objects

and Functions for BOPF Environment

 PPF Adapter for Output Management

 Maintain Output Management Adapter

Settings

## Example

As a shipper, you create a forwarding order and assign freight units that contain dangerous goods items. You assign the forwarding

order to an air freight booking. The system assesses the contents of the freight units, determines that the freight booking contains

dangerous goods and generates a shipper's declaration document that includes information on the dangerous goods from the

dangerous goods master. The shipper's declaration is available to the shipper.

Export/Import Processing

## Use

Logistics service providers (LSPs) who transport freight across customs borders on behalf of an sold-to party have to handle the

relevant export and import processes for the freight. In many cases, separate organizational units are responsible for each process,

that is, there is a separate export organization and import organization. Usually, the export organization is responsible for the pre-

carriage and main carriage stages, and the import organization is responsible for the on-carriage stages.

This is custom documentation. For more information, please visit SAP Help Portal.

66


1/14/26, 2:18 PM

You can use export/import processing to ensure that the export organization and the import organization have the required data

and business documents. The business documents created by the export organization (that is, one or more forwarding orders and

a freight booking) form the basis of the business documents that are used by the import organization.

## Features

## Supported Scenarios

You can use export/import processing in the following scenarios:

Full container load: The number of business documents on the export side is matched on the import side. For example, one

export forwarding order (FWO) and one export freight booking (FB) results in one import FWO and one import FB.

Less than container load: The number of business documents on the export side is matched on the import side. For

example, two export FWOs and one export FB results in two import FWOs and one import FB.

Buyer’s consolidation (n shippers and one ship-to party/destination): Several export FWOs are consolidated into one export

FB for the main carriage stage. On the import side, there is only one import FB and one import FWO.

Transit: You create a forwarding order that contains two main stages The system creates the standard Export/Import

documentation and also creates the transit FWO and transit FB, for the additional stage. The system automatically

determines the traffic direction “Transit” during the creation of import documents for this kind of forwarding order.

Empty Provisioning and Empty Return: In addition to transporting goods, you provide your customer with empty equipment

such as containers or railcars and/or facilitate their return. With empty provisioning, the export organization is responsible

for planning and execution (because the empty containers or railcars are required before transportation starts), but the

import organization may be responsible for the transportation charges. For empty returns, the import organization is

responsible for planning and execution (because the empty containers or railcars are returned after transportation has

taken place), but the export organization may be responsible for the transportation charges. For more information see:

Empty Provisioning and Return in Export/Import Processing.

You can also use export/import processing for forwarding orders in which different import organizations are assigned at item level.

For example, if you have one shipper with several ship-to partys and a different import organization is responsible for each ship-to

party. In this case, there is one export FWO and one export FB. On the import side, there is one import FB, and one import FWO per

import organization. The system creates the required import FWOs with the corresponding import organization entered as the

sales organization at header level. If the import organization is not entered at item level or if the same import organization is

entered for each item, the system creates one import FWO.

  Note

The relationship between the business partner and the organizational unit is defined in the organizational model. The

assignment of different import organizations at item level in the export FWO can be used for shipper’s consolidation, for

example.

## Internal Communication

If the export organization and the import organization both use Transportation Management (TM), the export organization creates

export forwarding orders, export freight bookings, and export freight units, and triggers the creation of the import business

documents. The system creates the import freight bookings first. It then creates the import forwarding orders and freight units

based on the import freight bookings. The import organization can then process the import business documents.

For more information, see Export/Import Processing: Internal Communication.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

67


1/14/26, 2:18 PM

The import business documents contain only the relevant execution information and are therefore not an exact copy of the

export business documents. In addition, you can use different freight unit building rules and stages for the export business

documents and import business documents.

## External Communication

If either the export organization or the import organization uses an external transportation management application, enterprise

services are used to transfer the required data between the external application and TM as follows:

If the import organization uses an external application, the export organization creates the export business documents in

TM and triggers the creation of the import business documents. TM sends the export business documents to the external

application. For more information, see Export/Import Processing: External Communication (Outbound).

If the export organization uses an external application, TM creates the import freight bookings based on data received from

the external application. It then creates the required import forwarding orders and freight units based on the import freight

bookings. For more information, see Export/Import Processing: External Communication (Inbound).

## Export FWOs Created by Other Organizational Units

In some cases, users who do not belong to the export organization have to create export FWOs. For example, where a customer

places orders at the import organization, a user in the import organization would create the export FWO.

A member of the import organization can create an export FWO in one of two ways:

## A member of the import organizational unit directly creates an export FWO

For this purpose, you can restrict user authorizations so that a user can create export forwarding orders with the status

Draft, but cannot trigger any follow-on processes such as freight unit building or charge calculation. The relevant function is

Set to In Process (DO) in authorization objects Functions for Forwarding Order (ext. Org.ID) (T_TR_FWOF2) and

Functions for Forwarding Order (T_TRQ_FWOF).

A member of the import organizational unit is not authorized for the function “Set to In Process” and therefore can only

create orders with status “Draft”. To activate this FWO, a member of the export organizational unit must set the order to “In

Process”. This means that the export organizational unit has full control over which orders are processed.

The import organizational unit creates the export FWO based on an import forwarding quotation (FWQ)

The import organizational unit starts the process by creating an import FWQ. The quotation is communicated to the

customer and the customer accepts the quotation. In the export organizational unit you can now use this quotation to

create an export FWO. During Customizing you should specify a forwarding quotation type for export. For more information

see Customizing for Transportation Management under  Forwarding Order Management

## Forwarding Quotation

## Define Forwarding Quotation Types

Using the import FWQ, the system creates an export FWO, with status “Draft”. The system transfers the header information,

the item information and the stage information (if available) from the FWQ to the export FWO. If available, the system also

transfers the service items from the import FWQ to the export FWO. (The customer might have contracted for services

which need to be applied on the export side).

The system does not transfer charges from the import FWQ to the export FWO (Unlike the creation of an import FWO out of

an import FWQ). The system transfers the import agreement from the import FWQ to the export FWO. A new agreement

field is added in the FWO for this purpose.

After planning and processing on the export side the system creates the import documents, including the import FWO.

When creating the import FWO, the system copies charges and service items from the referenced import FWQ. The system

does not by default transfer services which are created in the export FWO from the export FWO into the import FWO.

This is custom documentation. For more information, please visit SAP Help Portal.

68


1/14/26, 2:18 PM

You can define which service items in an export FWO are to be transferred to the corresponding import FWO. For more

information, see Customizing for Transportation Management under  Business Add-Ins (BAdIs) for Transportation

Management

## Basic Functions

 Export/Import Processing  .

Variants of FWO Creation

Cross Trade FWO :

A user can create an export forwarding order with reference to a cross-trade forwarding order. The ID of the cross-trade

forwarding order is entered on the General Data tab page in the export forwarding order. This feature can be used, for

example, by users in a central organization who are responsible for entering orders from specific customers. The cross

trade FWO is created by a central unit, such as a sales unit, which receives all orders from specific customers. These orders

are not relevant for planning and execution. The FWO in the exporting org. unit can be created by the central org. unit

specifying the cross trade FWO as a reference.

You can define whether planning and execution are to be blocked in a forwarding order by restricting follow-on processing in

the forwarding order type. This setting can be used for cross-trade forwarding orders, for example. For more information,

see Customizing for Transportation Management under  Forwarding Order Management

 Forwarding Order

## Define

Forwarding Order Types  .

## Manual Creation of Import Freight Bookings

You can also create import freight bookings manually. For more information, see Manual Creation of Import Freight Bookings.

## Customs Processing

The export organization and the import organization are responsible for the respective customs processes (for example, export,

import, or transit). For more information about customs processing in TM, see Global Trade. In addition, SAP Note 1757454

provides information about the required settings for the transit process in the context of export/import processing.

Export/Import Processing: Internal Communication

## Use

If the export organization and the import organization both use TM, the export organization creates export forwarding orders,

export freight bookings, and export freight units, and triggers the creation of the import business documents. The system creates

the import freight bookings first. It then creates the import forwarding orders and freight units based on the import freight

bookings. The import organization can then process the import business documents.

## Prerequisites

If required, you have specified the business document type that the system uses to create import business documents. You

have the following options:

You can define conditions. For the freight booking type, you use condition type /SCMTMS/FRB_TYPE_IMP. For the

forwarding order type, you use condition type /SCMTMS/FWO_TYPE.

You can specify the required business document type in Customizing for Transportation Management:

In the forwarding order (FWO) type that you use for export FWOs, you specify the relevant import FWO type

in the Import FWO Type field. You define FWO types in Customizing for Transportation Management under

Forwarding Order Management

## Forwarding Order

 Define Forwarding Order Types .

This is custom documentation. For more information, please visit SAP Help Portal.

69


1/14/26, 2:18 PM

In the freight booking (FB) type that you use for export FBs, you specify the relevant import FB type in the

Import Booking Type field. You define FB types in Customizing for Transportation Management under

Freight Order Management

## Freight Booking

 Define Freight Booking Types .

If you do not specify the import business document types or define conditions, the system uses standard logic to determine

the required business document types.

You have made the standard settings for forwarding orders (see Forwarding Order) and freight bookings (see Freight

Booking).

  Note
You can use a stage profile to define different stages for the export business documents and import business documents

(see Determination of the Route). In addition, you can use different freight unit building rules for the export business

documents and import business documents (see Freight Unit Building Rule).

If you want to transfer service items from the export forwarding order to the import forwarding order, you must

implement the Business Add-In (BAdI) BAdI: Service Item Processing for Import Forwarding Orders

(/SCMTMS/BADI_EXIM_SRV_PROC). For more information, see Customizing for Transportation Management under

Business Add-Ins (BAdIs) for Transportation Management

## Basic Functions

 Export/Import Processing

 BAdI:

Service Item Processing for Import Forwarding Orders .

You have made the standard settings for the relevant customs processes. For more information, see Global Trade. For

information about the required settings for the transit process in the context of export/import processing, see SAP Note

1757454

.

You have deactivated external communication for export freight bookings.

In the standard system, both internal communication and external communication are active. Communication is controlled

using the following standard PPF actions in output management:

Internal communication: Copy Export Freight Booking to Import Freight Booking

(/SCMTMS/COPY_EXP_BOK_IMP_BOK)

External communication: Send Export Freight Booking (Export/Import Scenario)

(/SCMTMS/TOR_BKWBIL_NTF_EXT)

If you use internal communication, you must deactivate the PPF action for external communication in the business partner

master data for the import organization on the Output Management tab page.

## Process

1. The export organization creates one or more export forwarding orders using the standard functions for creating forwarding

orders.

You can make the following optional settings:

You set the traffic direction of the forwarding order to Export. This can be specified in Customizing for the

forwarding order type or directly in the forwarding order.

You assign an import organization to the export forwarding order on the Business Partner tab page.

In the export forwarding order, the export organization is the sales organization on the General Data tab page. In the

corresponding import forwarding order, the import organization is the sales organization on the General Data tab

page, and the export organization is automatically entered on the Business Partner tab page.

Note that the relationship between the business partner and the organizational unit is defined in the organizational

model.

You can assign a different import organization to each item in the export forwarding order, if required.

This is custom documentation. For more information, please visit SAP Help Portal.

70


1/14/26, 2:18 PM

2. The export organization creates a freight booking using the standard functions for creating freight bookings.

The following settings are required:

You must set the traffic direction of the freight booking to Export. This can be specified in Customizing for the freight

booking type or directly in the freight booking.

You must assign an import organization to the export freight booking on the Business Partner tab page.

In the corresponding import freight booking, the import organization is the purchasing organization on the General Data

tab page, and the export organization is automatically entered on the Business Partner tab page.

Note that the relationship between the business partner and the organizational unit is defined in the organizational model.

The export organization performs the required customs processes for the exported goods. For more information about

customs processing in TM, see Global Trade.

3. The export organization triggers the creation of the import business documents by setting the status of the export freight

booking to Shipped on Board (ocean freight booking) or Uplift Confirmed (air freight booking).

Output management is used to create the import business documents. Information about created or updated import

business documents is displayed on the Output Management tab page in the export freight booking.

4. The system creates the import freight booking and then the import forwarding orders based on the import freight booking.

The system sets the life cycle status of the import business documents to Draft. In business documents with this status,

you can change the purchasing organization and sales organization, but all other changes are blocked until the status is

changed. The relevant block reason is displayed on the Statuses tab page in the business document.

The import business documents contain only the relevant execution information and are therefore not an exact copy of the

export business documents. The import business documents differ from the export business documents as follows:

The traffic direction is Import instead of Export.

The document type is defined according to the relevant condition, the setting in Customizing for the business

document type, or standard logic.

The import business document contains only the shipper, ship-to party, and carrier. It does not contain any

additional business partners from the export business document.

The purchasing organization specified in the export freight booking is displayed on the Business Partner tab page as

the export organization. The import organization specified in the export freight booking on the Business Partner tab

page or at item level is displayed as the purchasing organization in the import freight booking.

The sales organization specified in the export forwarding order is displayed as the export organization on the

Business Partner tab page in the import forwarding order. The import organization specified in the export

forwarding order on the Business Partner tab page or at item level is displayed as the sales organization in the

import forwarding order.

The relevant scenario determines whether there is a 1:1 relationship between the export forwarding order and the import

forwarding order. For example, in the buyer’s consolidation scenario, the export forwarding orders are consolidated into one

import forwarding order.

5. The system creates the import freight units.

The system creates the import freight units based on the import forwarding orders and assigns the freight units to the

relevant import freight bookings.

6. The import organization processes the import forwarding orders and import freight bookings.

To process the business documents, you must remove the Draft status as follows:

This is custom documentation. For more information, please visit SAP Help Portal.

71


1/14/26, 2:18 PM

By choosing  Set Status

 Set to In Process  in the import freight booking. The system sets the life cycle status of

the freight booking to In Process.

By choosing the Set to In Process pushbutton in the import forwarding order. The system sets the life cycle status

of the forwarding order according to the status of the related business documents (for example, import freight

booking).

The import organization performs the required customs processes for the imported goods. For more information about

customs processing in TM, see Global Trade.

## Result

If the export organization changes the export forwarding order, the export freight booking is automatically updated. The export

freight booking can also be updated manually. When an updated export freight booking is saved, the system automatically updates

the corresponding import freight booking provided the export freight booking still meets the prerequisites mentioned above (for

example, the required status and traffic direction) and provided the import freight booking has the life cycle status Draft.

You can use the Business Add-In (BAdI) BAdI: Update Mode for Import Business Documents

(/SCMTMS/BADI_EXIM_UPDATE_MODE) to adapt the update of import freight bookings to your own requirements. For example,

you can define that the system does not update any import freight bookings even if their life cycle status is Draft; or you can define

that the system updates certain parts of the import freight bookings regardless of their life cycle status. For more information, see

Customizing for Transportation Management under  Business Add-Ins (BAdIs) for Transportation Management

## Basic

## Functions

## Export/Import Processing

 BAdI: Update Mode for Import Business Documents .

Export/Import Processing: External Communication (Outbound)

## Use

If the import organization uses an external application, the export organization creates the export business documents in TM and

triggers the creation of the import business documents. TM sends the export business documents to the external application.

## Prerequisites

You have connected your TM system to the external application and implemented the required enterprise services.

You have made the standard settings for forwarding orders (see Forwarding Order) and freight bookings (see Freight

Booking).

If you want to transfer service items from the export forwarding order to the import forwarding order, you must implement

the Business Add-In (BAdI) BAdI: Service Item Processing for Import Forwarding Orders

(/SCMTMS/BADI_EXIM_SRV_PROC). For more information, see Customizing for Transportation Management under

Business Add-Ins (BAdIs) for Transportation Management

## Basic Functions

 Export/Import Processing

 BAdI:

Service Item Processing for Import Forwarding Orders .

You have made the standard settings for the relevant customs processes. For more information, see Global Trade.

You have deactivated internal communication for export freight bookings.

In the standard system, both internal communication and external communication are active. Communication is controlled

using the following standard PPF actions in output management:

Internal communication: Copy Export Freight Booking to Import Freight Booking

(/SCMTMS/COPY_EXP_BOK_IMP_BOK)

This is custom documentation. For more information, please visit SAP Help Portal.

72


1/14/26, 2:18 PM

External communication: Send Export Freight Booking (Export/Import Scenario)

(/SCMTMS/TOR_BKWBIL_NTF_EXT)

If you use external communication, you must deactivate the PPF action for internal communication in the business partner

master data for the import organization on the Output Management tab page.

## Process

1. The export organization creates one or more export forwarding orders using the standard functions for creating forwarding

orders.

You can make the following optional settings:

You set the traffic direction of the forwarding order to Export. This can be specified in Customizing for the

forwarding order type or directly in the forwarding order.

You assign an import organization to the export forwarding order on the Business Partner tab page.

In the export forwarding order, the export organization is the sales organization on the General Data tab page.

You can assign a different import organization to each item in the export forwarding order, if required.

2. The export organization creates a freight booking using the standard functions for creating freight bookings.

The following settings are required:

You must set the traffic direction of the freight booking to Export. This can be specified in Customizing for the freight

booking type or directly in the freight booking.

You must assign an import organization to the export freight booking on the Business Partner tab page.

The export organization performs the required customs processes for the exported goods. For more information about

customs processing in TM, see Global Trade.

3. The export organization triggers the creation of the import business documents by setting the status of the export freight

booking to Shipped on Board (ocean freight booking) or Uplift Confirmed (air freight booking).

TM sends the export freight booking to the external application using the Notify of Transportation Order Booking Waybill

(TransportationOrderBookingWaybillNotification_Out) outbound enterprise service in the Transportation

Order Processing process component. The service is triggered by the corresponding PPF action in output management.

Information about created or updated import business documents is displayed on the Output Management tab page in the

export freight booking.

4. The external application creates the import business documents.

The import organization processes the import business documents.

## Result

If the export organization changes the export forwarding order, the export freight booking is automatically updated. The export

freight booking can also be updated manually. When an updated export freight booking is saved, the system automatically sends

an update to the external application, provided the export freight booking still meets the prerequisites mentioned above (for

example, the required status and traffic direction).

Export/Import Processing: External Communication (Inbound)

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

73


1/14/26, 2:18 PM

If the export organization uses an external application, TM creates the import freight bookings based on data received from the

external application. It then creates the required import forwarding orders and freight units based on the import freight bookings.

## Prerequisites

You have connected your TM system to the external application and implemented the required enterprise services.

You have made the standard settings for forwarding orders (see Forwarding Order) and freight bookings (see Freight

Booking).

You have made the standard settings for the relevant customs processes. For more information, see Global Trade. For

information about the required settings for the transit process in the context of export/import processing, see SAP Note

1757454

.

If required, you have defined conditions to enable the system to determine the required business document types for the

import business documents. For the freight booking type, you use condition type /SCMTMS/FRB_TYPE_IMP. For the

forwarding order type, you use condition type /SCMTMS/FWO_TYPE.

If you do not define conditions, the system uses standard logic to determine the required business document types.

## Process

1. TM creates an import freight booking based on data received from an external application.

TM receives the data and creates the import booking using the Maintain Transportation Order Based On Transportation

Order Booking Waybill Notification (TransportationOrderBookingWaybillNotification_In) inbound

enterprise service.

2. TM creates the required import forwarding orders based on the import freight booking.

The system sets the life cycle status of the import freight booking and import forwarding orders to Draft. In business

documents with this status, you can change the purchasing organization and sales organization, but all other changes are

blocked until the status is changed. The relevant block reason is displayed on the Statuses tab page in the business

document.

The import business documents contain only the relevant execution information and are therefore not an exact copy of the

export business documents. The import business documents differ from the export business documents as follows:

The traffic direction is Import.

The document type is defined according to the relevant condition or standard logic.

The import business document contains only the shipper, ship-to party, and carrier. It does not contain any

additional business partners from the export business document.

The purchasing organization is displayed as the export organization on the Business Partner tab page in the import

freight booking. The import organization is displayed as the purchasing organization in the import freight booking.

The sales organization is displayed as the export organization on the Business Partner tab page in the import

forwarding order. The import organization is displayed as the sales organization in the import forwarding order.

The relevant scenario determines whether there is a 1:1 relationship between the export forwarding order and the import

forwarding order. For example, in the buyer’s consolidation scenario, the export forwarding orders are consolidated into one

import forwarding order.

3. The system creates the import freight units.

The system creates the import freight units based on the import forwarding orders and assigns the freight units to the

relevant import freight bookings.

This is custom documentation. For more information, please visit SAP Help Portal.

74


1/14/26, 2:18 PM

4. The import organization processes the import forwarding orders and import freight bookings.

To process the business documents, you must remove the Draft status as follows:

By choosing  Set Status

 Set to In Process  in the import freight booking. The system sets the life cycle status of

the freight booking to In Process.

By choosing the Set to In Process pushbutton in the import forwarding order. The system sets the life cycle status

of the forwarding order according to the status of the related business documents (for example, import freight

booking).

The import organization performs the required customs processes for the imported goods. For more information about

customs processing in TM, see Global Trade.

## Result

If the export organization sends an updated export freight booking, the import business documents are updated accordingly. Note,

however, that an import freight booking can be updated only if it has the life cycle status Draft.

You can use the Business Add-In (BAdI) BAdI: Update Mode for Import Business Documents

(/SCMTMS/BADI_EXIM_UPDATE_MODE) to adapt the update of import freight bookings to your own requirements. For example,

you can define that the system does not update any import freight bookings even if their life cycle status is Draft; or you can define

that the system updates certain parts of the import freight bookings regardless of their life cycle status. For more information, see

Customizing for Transportation Management under  Business Add-Ins (BAdIs) for Transportation Management

## Basic

## Functions

## Export/Import Processing

 BAdI: Update Mode for Import Business Documents .

Manual Creation of Import Freight Bookings

## Use

If there is no export freight booking in your system and you have received the relevant data by fax, for example, you can create the

corresponding import freight booking manually.

## Prerequisites

In Customizing for Transportation Management, you have created a freight booking type with the transport direction Import. For

more information, see Customizing under  Freight Order Management

## Freight Booking

 Define Freight Booking Types .

## Features

An import freight booking that you create manually is the same as an import freight booking that is created automatically. Unlike

with import freight bookings created automatically, all fields are ready for input. You can also enter a free-of-charge storage period.

You can create one or more forwarding orders directly from the import freight booking created manually. This is assigned to the

import freight booking automatically.

The following constraints apply to import freight bookings that are created manually:

You cannot perform subcontracting.

Import freight bookings are not relevant for planning.

Schedules are not supported.

This is custom documentation. For more information, please visit SAP Help Portal.

75


1/14/26, 2:18 PM

You cannot draw master air waybill numbers from stock or return them to stock. You can enter MAWB numbers manually,

however. The system checks the accuracy of these numbers.

You cannot create freight orders for pick-up and can only create freight orders for delivery.

The booking confirmation status and uplift confirmation status are not supported.

More Information

## Export/Import Processing

Buyer's Consolidation in Export/Import

## Use

In Export/Import, you use Buyer's Consolidation (BCO) to amalgamate orders from different suppliers that are all destined for one

ship-to party. You can consolidate multiple export forwarding orders into an export freight booking. At the consolidation point, the

packages are loaded into a container for shipping to the ship-to party.

For import, the system creates one import freight booking and one import forwarding order for each ship-to party. The import

forwarding order contains a consolidation container and the items that were consolidated within this container.

## Prerequisites

You have specified an agreement item for BCO including the calculation sheet for BCO.

## Features

## Export Forwarding Order

Export forwarding orders destined for the same ship-to party are eligible for BCO.

For each forwarding order that is to be consolidated, you must set the shipping type to Less than Container Load (LCL).

Each export forwarding order has a number of stages defined. For BCO, the stages between the shipper and the consolidation point

can differ for each export forwarding order. The stages between the consolidation point and the ship-to party are identical.

## Export Freight Booking

In the Export booking order you can flag a container as a BCO Container. Before assigning the export freight unit/forwarding orders

the system checks whether all assigned forwarding orders have the same ship-to party. The system can only initiate a BCO process

if all assigned forwarding orders have the same ship-to party.

When you set the status of the export freight booking to Shipped on Board in an ocean scenario or to Uplift Confirmed in an air

scenario, the system creates an import freight booking and a single consolidated import forwarding order.

## Import Freight Booking

The import freight booking contains one import forwarding order for each ship-to party. The system sets the initial document

status for the import freight booking to Draft.

## Import Forwarding Order

This is custom documentation. For more information, please visit SAP Help Portal.

76


1/14/26, 2:18 PM

The import forwarding order includes the container from the export booking and also contains sub-items from the export freight

booking.

For the consolidated import forwarding order, the system sets the initial shipping type set to Full Container Load (FCL).

As there are multiple shippers, the system displays the business partners and locations in the item details.

Both the actual and the ordered route are copied from the export documents. Since there are different routes per consolidated

item, the actual and the ordered route is shown per forwarding order item.

The system sets the initial document status to Draft.

## Charges

The system calculates charges using the agreement item configured for BCO. If you have not configured a specific agreement item

for BCO, the system uses the standard calculation sheet for full container load transportation. For more information, seeBuyer's

Consolidation .

## Settlement

For settlement, the system creates one consolidated settlement for all the forwarding orders in the container item for the main

carriage on the export side. On the import side, the system uses the information in the import forwarding order to create the

settlement. The system uses an agreement line item configured for BCO. If such a line item does not exist, the system tries to find

an agreement line item with a shipping type of FCL.

For more information, see Shipper's Consolidation Settlement

## Example

As a carrier, you want to transport products from three different manufacturers from China to Germany. There are three export

forwarding orders – one for each of the three products. You create an export freight booking and specify that it is to be handled in

BCO mode. At Shanghai port, the pallets are loaded into one container. The container is then transported by sea to Hamburg. The

system creates a single import freight booking for the container and a single import forwarding order. The import forwarding order

contains an item for the container and sub items for each of the three export forwarding orders. In Hamburg the container is

loaded onto a truck. The truck delivers the container to the ship-to party in Hanover.

## More Information

Consolidating Orders Using Buyer's Consolidation

Consolidating Orders Using Buyer's Consolidation

## Use

In Export/Import, you can use buyer's consolidation (BCO) to amalgamate orders from different suppliers that are all destined for

one ship-to party.

## Prerequisites

You have defined freight booking types in Customizing. You define the most important settings for the freight booking in the freight

booking type. For more information, see Customizing for Transportation Management under  Freight Order Management

## Freight Booking

## Define Freight Booking Types

This is custom documentation. For more information, please visit SAP Help Portal.

77


1/14/26, 2:18 PM

You have made the settings required for the forwarding order. For more information, see Settings for the Forwarding Order

## Process

1. Create a freight booking

You first enter the general data for your freight booking, for example:

## Shipper, ship-to party, and carrier

Locations, for example, port of loading and port of discharge

Dates and times, for example, departure date and expected arrival date

## Number of containers

You must specify an Import Organization.

For more information see Creation and Editing of Freight Bookings

2. Create a forwarding order for each shipper.

For each forwarding order:

You specify the forwarding order type and transportation mode.

From the Buyer's or Shipper's Consolidation dropdown, you choose BC.

You specify LCL (Less than Container Load) as the Shipping Type

Specify intermediate stages, the port of loading and port of discharge

For more information see Creation of a Forwarding Order

3. Assign the forwarding order to the export freight booking

a. Set the status of the export freight booking to Shipped on Board in an ocean scenario, or to Uplift Confirmed in an

air scenario.

Once you save the freight booking, the system creates the import documents – one import freight booking containing multiple

import forwarding orders, at least one for each ship-to party.

## More Information

Buyer's Consolidation (BCO) in Export/Import

Shipper's Consolidation in Export/Import

## Use

In Export/Import, you can use shipper's consolidation (SCO) to amalgamate orders that are destined for different ship-to partys

but originating from a single supplier. At the deconsolidation point, the packages are separated for shipping to the various ship-to

partys.

You can create one export forwarding order containing sub-items for each of the ship-to partys. For import, the system creates one

import freight booking containing multiple import forwarding orders – at least one for each ship-to party.

This is custom documentation. For more information, please visit SAP Help Portal.

78


1/14/26, 2:18 PM
## Prerequisites

You have specified an agreement item for shipper's consolidation including the calculation sheet for SCO.

## Features

## Export Forwarding Order

Export forwarding orders originating from the same shipper to different ship-to partys are eligible for SCO.

You create a forwarding order containing a consolidation container and sub-items for each of the deliveries that are to be

consolidated. You specify that the forwarding order is to be handled in SCO mode. You must set the shipping type to Full Container

Load (FCL).

Each ship-to party has a number of stages defined. For SCO the stages between the shipper and the deconsolidation point are

identical for each ship-to party sub-item. The stages following deconsolidation – between the deconsolidation point and the ship-to

party – can differ as the items are delivered to their respective ship-to partys.

## Export Freight Booking

When you set the status of the export freight booking to Shipped on Board in an ocean scenario or to Uplift Confirmed in an air

scenario, the system creates an import freight booking and multiple import forwarding orders – at least one for each ship-to party.

## Import Freight Booking

The import freight booking contains an import forwarding order for each ship-to party. The document status for the import freight

booking is set to draft.

## Import Forwarding Order

The system creates an import forwarding order for each ship-to party of the sub-items on the export forwarding order.

For the deconsolidated import forwarding orders, the shipping type is set to Less Than Container Load (LCL).

## Charges

The system calculates charges using the agreement item configured for SCO. If you have not configured a specific agreement item

for SCO, the system uses the standard calculation sheet for FCL transportation.

## Settlement

For settlement, the system creates the settlement document for the pre-paid agreement party based on the export forwarding

order on the export side. For a forwarding order with incoterms such as DDP, the system creates the settlement items for the pre-

paid agreement party and for the delivery legs – one each per destination location or one per delivery date in a case where the

delivery location is the same for multiple items. The system creates a settlement for each import forwarding order on the import

side. The system uses an agreement line item configured for SCO for pre-carriage and main carriage. If such a line item does not

exist, the system tries to find an agreement line item with a shipping type of Forwarding Order, for example, FCL on the Export side,

and LCL on the import side).

## Example

As a carrier, you want to transport three products from the same manufacturer in China to separate ship-to partys in Germany.

There is one export forwarding order with three sub-items – one for each of the three products. You create an export freight

booking and specify that it is to be handled in SCO mode. At the factory, the pallets are loaded into a single container. From there

This is custom documentation. For more information, please visit SAP Help Portal.

79


1/14/26, 2:18 PM

the container is moved to the port at Shanghai, and then transported by sea to Hamburg. The system creates a single import

freight booking for the container and three import forwarding orders – one for each of the ship-to party sub-items. In Hamburg the

container is deconsolidated. The three individual pallets are loaded onto different trucks then delivered to their respective ship-to

partys.

## More Information

Consolidating Orders Using Shipper's Consolidation

Consolidating Orders Using Shipper's Consolidation

## Use

In Export/Import, you can use shipper's consolidation (SCO) to amalgamate orders originating from a single supplier that are

destined for different ship-to partys.

## Prerequisites

You have defined freight booking types in Customizing. You define the most important settings for the freight booking in the freight

booking type. For more information, see Customizing for Transportation Management under  Freight Order Management

## Freight Booking

## Define Freight Booking Types

You have made the settings required for the forwarding order. For more information, see Settings for the Forwarding Order

## Process

1. Create a freight booking

You first enter the general data for your freight booking, for example:

## Shipper, ship-to party, and carrier

Locations, for example, port of loading and port of discharge

Dates and times, for example, departure date and expected arrival date

You must specify an Import Organization.

For more information see Creation and Editing of Freight Bookings

2. Create a forwarding order

a. You specify the forwarding order type and transportation mode.

b. From the Buyer's or Shipper's Consolidation dropdown, you choose SC.

c. You specify FCL (Full Container Load) as the shipping type.

d. You specify Door to Door as the movement type.

e. You create a container – this has no ship-to party as it will be deconsolidated prior to any deliveries.

f. You create package items in the container – one for each ship-to party. On package level define business partner and

ship-to party.

For more information see Creation of a Forwarding Order

This is custom documentation. For more information, please visit SAP Help Portal.

80


1/14/26, 2:18 PM

3. Assign the forwarding order to the export freight booking

a. Set the status of the export freight booking to Shipped on Board in an ocean scenario, or to Uplift Confirmed in an

air scenario.

Once you save the freight booking, the system creates the import documents – one import freight booking containing multiple

import forwarding orders, at least one for each ship-to party.

## More Information

Shipper's Consolidation (SCO) in Export/Import

Ocean Freight Bookings for Shippers (Outbound)

With Transportation Management (TM) you can manage multimodal transportation scenarios with multiple transportation stages

and different transportation modes. This topic provides details for shippers on outbound transportation with ocean freight. The

scenario is designed for Advanced Shipping and Receiving.

You can model end-to-end scenarios with container units and the message exchange between you, as the shipper, and the carrier.

For a high-level sample, see Sample Ocean Freight Process for Shippers (Outbound).

## Prerequisites

If you want to save freight bookings that contain errors, you have activated this function for the ocean freight booking types

you want to use. You do so in Customizing for Transportation Management under  Freight Order Management

  Freight

## Booking

  Define Freight Booking Types . In section Integration Settings, choose Enable saving of documents with

errors for dropdown box Handling of incorrect inbound messages.

The activation is only valid for freight bookings you create after the activation.

The usage of container units is mandatory for the ocean freight process for shippers and doesn’t support local container

items.

The process supports full container load (FCL) cargo. Less than container load (LCL) cargo is not supported.

When using Advanced Shipping and Receiving with Extended Warehouse Management for outbound processes, you must

create a pick-up freight order for each container unit. The system requires these freight orders for the loading process.

The system can handle cargo that was left behind at the port. To use this function, you have activated the Itm Load. Stat.

Port checkbox for the event profile and assigned it to the freight booking type you use. You do so in Customizing for

Transportation Management under  Freight Order Management

  Execution Settings

  Define Event Profiles .

For more general information, see Cargo Left Behind at Port/Airport.

When creating container units, the system can automatically check if the container registration number for the container is

correct according to ISO 6346. To use the check, configuration is necessary. For more information, see section "container

units".

To communicate via EDI with your carrier, you need to configure the for sending of container update messages to the (pre-

carriage) carrier. For more information, see the corresponding section below.

## Ocean Freight Bookings

This is custom documentation. For more information, please visit SAP Help Portal.

81


1/14/26, 2:18 PM

The ocean freight scenario for shippers supports door-to-door (D2D) and door-to-port (D2P) shipping. As usual, you use an ocean

freight booking to reserve freight space on a vessel.

You can receive the confirmation for the oceanfreight booking from the carrier using EDI communication. Alternatively, you enter

the confirmation manually in the ocean freight booking by setting the status to Set to Confirmed by Carrier.

## Container Units

You create container units and assign freight units. The freight units can originate from sales orders or outbound deliveries. After

creating the container units, you assign them to an ocean freight booking. Finally, you create pick-up freight orders (pick-up FOs).

In case you need to change the assignment of container units to pick-up or delivery freight orders, you can also assign or unassign

the container units in the freight booking.

When creating container units, the system can automatically check if the container registration number for the container is

correct according to ISO 6346. The system runs the check when you enter the container registration number together with an

equipment type. To use the check, you need to specify the equipment type in Customizing for Transportation Management under

Master Data

## Resources

## General Settings

  Define Equipment Groups and Equipment Types . Set the resource class for the

container group to 10 Container.

You plan the container units on the ocean freight booking. To assign container units, you can search for the containers using their

registration numbers.

On the Booking Data tab in the container unit, you can display the booking information.

## Pick-Up Freight Orders and Delivery Freight Orders

When you create a pick-up FO for the pre-carriage or a delivery FO for the on-carriage, you can assign one or several container

units to it.

## Define Transportation Mode

On the Stages tab of the freight order, you can display the transportation mode column.

When a pick-up FO or delivery FO is created out of an ocean freight booking, the system considers a couple of settings to find out

the transportation mode that is to be used. You configure if the system creates a road freight order or a rail freight order for the

pre-carriage or on-carriage. You can define freight order default types in the freight order type or freight booking type in

Customizing.

You have several setting options. Here are two examples:

The transportation mode you need varies from time to time. Sometimes you need a road freight order, sometimes a rail

freight order. You want to be flexible and easily adjust the transportation mode to your needs.

To achieve this, you configure a freight order default type for pick-up FOs or delivery FOs in section Default Types in

Customizing for Transportation Management under  Freight Order Management

  Define Freight Booking Types .

In the pre- or on-carriage stage of the ocean freight booking, you have then the option to adjust the default transportation

mode.

In addition, you can define freight oder default types in the freight order type Customizing or in the freight booking type

Customizing. The system uses these FO default types when creating a pick-up FO or delivery FO for a freight booking.

The transportation mode you need is always the same.

To achieve this, you define a freight order type for road (and one for rail) that is defined as Default FO Type for FB. You do so

in section Default Types in Customizing for Transportation Management under  Freight Order Management

## Define

This is custom documentation. For more information, please visit SAP Help Portal.

82


1/14/26, 2:18 PM

Freight Order Types .

## Loading Cargo

You have several options to set the loading status in the system:

## In the Load or Unload Freight Orders app

In the Edit Road Freight Order app or Edit Rail Freight Order App

Via Radio Frequency (RF)

As storage location, you can use an inventory-managed (IM) storage location for Lean Warehouse Management or a storage

location for Extended Warehouse Management (EWM).

## Consignment Orders

You can create consignment orders for pick-up FOs associated with an ocean freight booking. The consignment orders include

booking information from the assigned ocean booking, for example, vessel, voyage, IMO Ship ID, UN/LOCODE, expected arrival

date and time at the port of destination or at the customer (depending on the scenario in use, that is door-to-door or door-to-port).

## Automatic or Manual Creation of Consignments

For the creation, you can choose to manually create consignment orders, or you can use the automatic consignment building. For

more information, see Automatic Consignment Building.

You manually create consignment orders in the pick-up FO under  Follow up

  Build Local Consignment Orders

 or  Follow

up

## Create Consignment Order

. For more information about consignment orders in general, see Consignment Order.

You can display the booking data on the Booking Data tab in the consignment order.

  Note

When consignment orders are created in the ocean freight process, the container units on the pick-up FO must contain only a

single container item.

Additional Infos About Ocean Freight Bookings

## Port of Destination and Incoterms

When the agreed Incoterm location with the customer is “port”, use a door-to-port freight booking. The door-to-port scenario has

some impacts:

Depending on the settings in the logistics integration profile the Incoterm is considered during freight unit building. You can,

for example, configure the freight units to have a planning-relevant stage from the shipper’s location to the port of

destination and a statistical stage (not in the shipper’s responsibility) from port of destination to the consignee.

The consignment order will still have one stage from the shipper’s location to the port of destination. The planned arrival

date refers to the date at the port of destination.

You can set the port of destination to Unloaded. The system prevents setting a container unit to Unloaded in the ocean freight

booking if the container unit has a document error. Once the error is resolved by setting the container unit to Loaded, the system

automatically updates the unloading status for the container unit.

## Handle Containers Left Behind at the Port

This is custom documentation. For more information, please visit SAP Help Portal.

83


1/14/26, 2:18 PM

The ocean freight process can handle containers that were left behind at the port of loading. For more information, see Cargo Left

Behind at Port/Airport.

## Invoicing

The invoicing process starts only after the ocean vessel's departure. It also requires that there are no pending decisions for any

containers left behind. For more information, see Carrier Invoice.

## Message Exchange Between Shipper and Carrier

The ocean freight scenario offers an end-to-end process with container units and message exchange between you and the carrier.

## Sending Container Units to (Pre-Carriage) Carrier

The container message is sent to the carrier when all the following conditions are met:

When the container unit (CU) is assigned to an ocean freight booking and important information such as steamship line

booking number, vessel ID, and container registration number is available.

When goods movement is posted and the status changes to Completely Processed.

When loading is completed in the pick-up FO.

  Note

If multiple container units are assigned to a freight order, the system can only send the respective container message to the

carrier after all containers have been loaded.

## Settings for Sending CU-Update Messages to (Pre-Carriage) Carrier

The following settings are necessary to automatically send EDI messages to the (pre-carriage) carrier:

You have configured the Post Processing Framework (PPF) in Customizing for Cross-Application Components under

Processes and Tools for Enterprise Applications

  Reusable Objects and Functions for BOPF Environment

  PPF

Adapter for Output Management

  Maintain PPF Settings .

In application /SCMTMS/TRANSPORTATION you activated the action definition TOR_TPNOR_NTF (Send Notification) of

action profile /SCMTMS/TOR.

In addition, you have assigned the output profile /SCMTMS/TOR to the container unit type you use. You assigned the

output profile in Customizing for Transportation Management under  Freight Order Management

## Transportation Unit

Define Transportation Unit Types  in Section Output Options.

With the following status changes the systems sends a notification to the carrier:

Execution status changes to Ready for Transportation Execution

Execution status changes to In execution

Departure event is posted

## Checkout event is posted

If the status change takes place in the freight booking, a TransportationOrderGenericRequest_Out message (with

business scope "Notification”, categoryCode "BO" (booking)) is sent to the main-carriage carrier.

This is custom documentation. For more information, please visit SAP Help Portal.

84


1/14/26, 2:18 PM

If the status change takes place in the pick-up FO, a TransportationOrderGenericRequest_Out message (with business

scope “Notification”, categoryCode "TO" (freight order)) is sent to the pre-carriage carrier.

For companies that store containers in a local container depot, it might be useful to send an EDI message when the container is

loaded to inform the pre-carriage carrier about the necessary pick-up of the container.

Receiving Freight Booking Updates from the Carrier

  Note
The EDI messages you receive from the carrier must contain certain information. For some XML samples, see SAP note

3514066

.

The carrier can send you an freight booking update using EDI communication. You can, for example, receive the house bill of lading

as well as updates for the departure dates from the port of loading, the containers that were loaded, the expected time of arrival, or

change the port of destination in a door-to-door scenario. The system supports updates for freight bookings and for individual

container units within a freight booking.

Based on this inbound message, the system updates the freight booking with the received information. The message can include

information, such as vessel, voyage number, house bill of lading, expected time of arrival, general booking information like freight

booking reference (that is freight booking ID in the shipper's system), freight booking type and document category (that is the

business object for freight booking), item information like item category and container registration number. To identify the

location, the message can contain a UN/LOCODE.

  Note
A separate message for each container can be sent (single container update messages).

Alternatively, you can manually enter updates in the freight booking.

## Identifying Locations by UN/LOCODES

The system finds locations using the UN/LOCODES that were sent with an inbound message. If the handling of errors for business

documents is activated for the freight booking type, the system displays document errors if the UN/LOCODE couldn't be found,

isn't unique or is wrong.

To enable this check, you need to activate the handling of errors for business documents in Customizing for the ocean freight

booking type.

## Update Port of Destination

The port of destination can be updated by inbound messages.

When you change the port of an ocean freight booking manually in a door-to-door scenario, the system checks if a delivery freight

order already exists. You need to confirm that the corresponding location in the delivery freight order can be changed too.

In some situations, such as weather conditions, breakdowns, or repairs, it might be necessary to change the port of discharge for

an ocean freight booking. This allows the shipper to make necessary adjustments in the system and to inform involved parties.

Changing the port of destination is allowed in the following cases:

The delivery freight order is not in execution.

The delivery freight order is not assigned to multiple freight bookings. This might be the case if a truck picks up deliveries of

two different vessels.

This is custom documentation. For more information, please visit SAP Help Portal.

85


1/14/26, 2:18 PM

## Sending ASN to Customer

In the following cases, the system sends a separate advanced shipping notification (ASN) message for each consignment order to

the customer when the vessel departed. At this point in time, additional booking information is available and can be included in the

ASN to the customer.

When goods movement status on consignment order is set to Completely Processed.

When the ocean freight booking is set to Departed From Port of Loading.

Alternatively, when manually requested in the consignment order under  Follow Up

  Send Advanced Shipping

Notification .

Especially in a door-to-port scenario, consignments, and their updates are useful for customers. Depending on the Incoterms, they

might need to know the voyage number, and the expected date and time of arrival to organize the pickup and transport of the

goods for the last stage.

## Related Information

Sample Ocean Freight Process for Shippers (Outbound)

## Consignment Order

Cargo Left Behind at Port/Airport

Air Freight Bookings for Shippers (Outbound)

Sample Air Freight Process for Shippers (Outbound)

## Advanced Shipping and Receiving

Sample Ocean Freight Process for Shippers (Outbound)

This topic describes a sample ocean freight process for shippers. It involves a door-to-door ocean freight booking and includes

transportation stages for the pre- and on-carriage. The process is also available for door-to-port scenarios. It is designed for

Advanced Shipping and Receiving.

For the process, we assume the following:

The planning of the main stage is done by the carrier. The freight units originate from outbound deliveries. The shipper initiates the

ocean freight process with pre-booking capacity, meaning they create an ocean freight booking. Furthermore, consignment orders

are created manually and ocean freight booking updates from the carrier are received via EDI communication.

This process gives you a high-level overview with the most important process steps. For more background information and

prerequisites about the process in general, see Ocean Freight Bookings for Shippers (Outbound).

## Creating Ocean Freight Booking

1. Creating an ocean freight booking to reserve capacity (pre-booking)

A couple of weeks in advance, you create an ocean freight booking to request booking capacity, for example, to reserve two

20 feet containers.

To do so, open the Create Ocean Freight Booking app from the launchpad.

2. Sending the booking request

You send the ocean freight booking to the main-carriage carrier, for example a shipping company.

This is custom documentation. For more information, please visit SAP Help Portal.

86


1/14/26, 2:18 PM

The capacity reservation is done using the TransportationOrderBookingRequest_Out service. The message contains the

document ID of the ocean freight booking in your system (the shipper’s system). The carrier can use this ID to refer to the

ocean freight booking throughout the communication.

3. Receiving booking confirmation from the carrier

You receive the booking confirmation from the carrier via EDI message. The message contains information, such as voyage

number, vessel, or IMO ship identification number, reference number for the ocean freight booking and a house bill of lading

(HBL) number.

## Creating Transportation Requirements

You create outbound deliveries. The system automatically creates freight units.

You can, for example, use the Create Outbound Deliveries app from the launchpad.

## Transportation Planning

You plan the freight units on a container unit, then you plan the container unit on an ocean freight booking. Later in the process, the

pre-carriage carrier is informed about the necessary pickup via EDI communication. Container units are mandatory for the sample

ocean freight process and a prerequisite for this communication.

1. Creating container units

You can use the Create Container Unit app from the launchpad.

You plan your delivery-based freight units on a container unit.

2. Assigning container units to ocean freight booking

You plan the container units on the ocean freight booking. You can use the container registration number to search for

them.

## Performing Warehouse Activities

Picking (and possibly packing) is carried out by the warehouse workers. It is performed in the respective storage location, for

example for Lean Warehouse Management in an inventory-managed (IM) storage location or a storage location for Extended

Warehouse Management (EWM).

Processing Pick-up Freight Orders

1. Creating freight orders for pick-up

If necessary, you can adjust the transportation mode for the pick-up freight order on the Stages tab of the ocean freight

booking. This has an impact on the creation of the pick-up FO. You can choose either road or rail.

You create a pick-up freight order in the ocean freight booking.

You assign one or several container units to a pick-up freight order.

2. Reporting truck arrival and check-in

You set the Checked In status for the pick-up freight order.

3. Loading cargo

This is custom documentation. For more information, please visit SAP Help Portal.

87


1/14/26, 2:18 PM

The cargo items for the oversea transport are loaded onto the truck. Before loading, the pick-up freight order must have the

Ready for Transportation Execution status.

You have several options to set the loading status in the system:

## In the Load or Unload Freight Orders app

In the Edit Road Freight Order or Edit Rail Freight Order app

In the container unit

## Via Radio Frequency (RF) in EWM

4. Creating consignment orders to inform the customer

You create consignment orders manually for each pick-up freight order under  Follow up

  Build Local Consignment

Orders or Follow up

## Create Consignment Order

. You then create consignment order documents for the local

consignment orders under  Follow up

  Create Consignment Order

.

5. Posting goods issue

You post goods issue for the pick-up freight order. When you post goods issue, the system sends an advanced shipping

notification (ASN) based on the consignment order to inform the customer.

Posting goods movement updates the respective warehouse management system (independent of the kind of warehouse

management you use). You can display an overall status overview in the freight order, under the Advanced SR tab.

6. Departure of Truck

You set the status Departure for the pick-up freight order.

## Departure of the Vessel

1. Receiving status updates for the container units from the carrier

After the vessel departs, the main-carriage carrier can send you a subsequent EDI message containing updates for the

ocean freight booking. The update messages can include data, such as all containers loaded onto the vessel or departure

information.

The carrier might send one message for each container unit that is loaded, known as single container update messages.

They can also send a single update message for multiple container units.

With departure of the vessel from the port of loading, the status Shipped on Board and Departed are set in the ocean

freight booking.

Departure of the vessel from port of loading:

The system automatically sends an updated ASN message to the customer when the ocean freight booking has status

Departed. The ASN, based on the consignment order, also contains information about the ocean freight booking that might

not have been available when the ASN message was sent the first time when goods movement was posted, for example

information such as vessel, voyage, and planned arrival date/time.

2. Optional: Multiple Containers left behind at port

If one or several containers were not loaded to the vessel and the status of the ocean freight booking is Departed, the

system displays a document error for the container. Meanwhile, the invoicing process is blocked. You can either reassign the

container unit to another ocean freight booking, or you set the execution status of the container to Loaded (for instance,

when a container update message could not be received properly). An error might also be temporary. For more information,

see Cargo Left Behind at Port/Airport.

This is custom documentation. For more information, please visit SAP Help Portal.

88


1/14/26, 2:18 PM
## Reporting Arrival of Vessel

The carrier might send a message per ocean freight booking to confirm the arrival at the airport of destination.

## Processing Delivery Freight Orders

In a door-to-door scenario, you create a delivery freight order for the further transport.

To do so, you select the relevant freight units in the Edit Ocean Freight Booking app on tab Capacity and Cargo, and choose

## Create

  Create Freight Order for Delivery with Default FO Type .

This order facilitates the collection of goods from the port of discharge. The goods are then transported to the destination location,

which is typically the customer's address.

## Related Information

Ocean Freight Bookings for Shippers (Outbound)

Air Freight Bookings for Shippers (Outbound)

With Transportation Management (TM) you can manage multi-modal transportation scenarios with multiple transportation stages

and different transportation modes. This topic provides details for shippers on outbound transportation with air freight. The

scenario is designed for Advanced Shipping and Receiving.

You can model an end-to-end process with the message exchange between you, as the shipper, and the carrier in which

consignment orders play an essential part.

For a high-level sample process description, see Sample Air Freight Process for Shippers (Outbound).

## Prerequisites

If you want to save freight bookings that contain errors, you must activate this function for the air freight booking types you

want to use. You do so in Customizing for Transportation Management under  Freight Order Management

  Freight

## Booking

  Define Freight Booking Types . In section Integration Settings, choose Enable saving of documents with

errors for dropdown box Handling of incorrect inbound messages.

The activation is only valid for freight bookings you create after the activation.

When you decide to work with local consignment building based on top-level packages, some configuration is necessary.

For more information, see section "Settings for Consignment Building on Top-Level Packages".

To communicate via EDI with your carrier, you need to configure the sending of consignment orders to the carrier. For more

information, see section "Settings for Sending Consignments to the Carrier".

## Pick-Up Freight Orders and Delivery Freight Orders

The air freight scenario for shippers supports door-to-door (D2D) and door-to-port (D2P) shipping. You can model the transport of

goods for a customer by airplane and order the transport service (D2D or D2P) from a carrier. The carrier organizes the air freight

bookings on its own and informs you once it is decided which flight the freight will be on.

The air scenario starts with creating a road pick-up freight order (FO). The pick-up FO includes all goods (freight units) that need to

be transported via the same airport and can be created before the air freight booking exists. The freight units can originate from

sales orders or outbound deliveries.

This is custom documentation. For more information, please visit SAP Help Portal.

89


1/14/26, 2:18 PM

  Note

Only freight units destined for an airport are allowed. This means you can’t combine air freight cargo with other truck deliveries,

such as requirements for direct transport to customers.

You create pick-up FO orders without reference to an air freight booking in the Freight Bookings Work List or the Freight Orders

Work List. Choose query Pick-Up/Delivery, and then  New

  Road Freight order for Pick-Up/Delivery .

## Consignment Orders for Carriers and Customers

Out of the pick-up FO to the airport, you create consignment orders to be able to communicate with the carrier. Based on these

consignment orders, you inform the carrier about the goods that need to be transported.

## Carrier Plans Consignments on Flights

The consignment orders are sent to the carrier. The carrier plans the consignment orders on appropriate flights, creates the

corresponding air freight bookings, and informs you which consignment orders are planned on which flight. The carrier may send

this information via EDI communication or email. The consignment orders of a pick-up FO can be distributed over several air freight

bookings.

  Note

The system doesn’t support splitting consignment orders. In air freight operations, such a split becomes necessary when a

carrier allocates cargo items from a single consignment order across multiple air freight bookings. If the carrier communicates

such an allocation situation, the system can’t process the air freight booking message.

Due to this restriction, it is important that all cargo items of a consignment order are assigned to the same flight.

To ensure that no consignment order split is needed, you can either define an appropriate process in the system or configure the

system so that consignment orders contain only one cargo item when they’re created. To do this, use the consignment order

creation based on the top-level package.

## Consignments Based on Top-Level Package

When you configure the consignment order creation based on the top-level package, each consignment order contains only one

package item or unpacked product. This means, the system creates one consignmentorder per handling unit (pallet). By that, the

package-based consignment orders (pallets) of one pick-up FO can be transported on different flights.

## Settings for Consignment Building on Top-Level Packages

To enable local consignment building based on the top-level package, you need to configure your consignment building profile in

the Create Consignment Building Profile app. As grouping rule, you define TOP_CARGO Topmost Cargo Item (Package or

Unpacked Product).

## Automatic or Manual Creation of Consignments

For the creation, you can choose to manually create consignment orders, or you can use the automatic consignment building. For

more information, see Automatic Consignment Building.

You manually create consignment orders in the pick-up FO under

 Follow up

  Build Local Consignment Orders . You then

create consignment order documents for the local consignment orders under  Follow up

  Create Consignment Order

.

For more information, see Consignment Order.

This is custom documentation. For more information, please visit SAP Help Portal.

90


1/14/26, 2:18 PM

The consignment orders include booking information from the assigned air freight booking, for example, airline code, flight number

and airport of destination, expected arrival date and time at the port of destination or at the customer (depending on scenario in

use, that is door-to-door or door-to-port).

You can display the booking data on the Booking Data tab in the consignment order.

## Air Freight Booking

If you want to change the assignment of a consignment order to an air freight booking, you first need to unassign it from the

original freight booking. After that, you're able to assign the consignment order to a different freight booking.

You can receive messages regarding freight bookings from the carriers using EDI communication. Alternatively, you manually enter

the data you received.

## Document Errors

As described in the prerequisites, you can save freight bookings that contain errors. If activated, the system reports document

errors, in the following situations, for example:

For the pick-up FO or consignment order if consignment orders aren’t yet assigned to an air freight booking. This shows

that there are still consignments orders or parts of deliveries that are not transported yet.

This happens, for instance, in a door-to-door scenario where the delivery's destination location is the customer's side, but

the freight order is destined for the airport. The document errors are resolved automatically when the consignment order is

assigned to a freight booking.

For a freight unit if the locations don’t match and the freight unit and its successor document have a different destination

location. The error is automatically resolved once the consignment order is created.

## Invoicing

The invoicing process starts only after the departure of the airplane . For more information, see Carrier Invoice

## Message Exchange Between Shipper and Carrier

The air freight process offers a message exchange between you, as the shipper, and the carrier.

## Sending Consignments to the Carrier

Consignments are automatically sent to the carrier when the goods issue is reported and the goods movement status for the pick-

up FO and the consignment order is set to Completely Processed.

## Settings for Sending Consignments to the Carrier

When goods issue is posted and the system sets the goods movement status of the freight order and the consignment order to

Completely Processed, the system sends a TransportationOrderGenericRequest_Out message (with Business Scope

“EXTERNAL_PLANNING”) to the main-carriage carrier. The status in the consignment order is the status that is relevant for

sending this message.

The following settings are necessary to send the consignment orders to the carrier for external planning:

You have defined a consignment order type with transportation mode “air”, to automatically send ASN messages to the

carrier.

This is custom documentation. For more information, please visit SAP Help Portal.

91


1/14/26, 2:18 PM

You define the transportation mode in section Service Definition in Customizing for Transportation Management under

Freight Order Management

## Consignment Orders

  Define Consignment Order Types .

You have configured the Post Processing Framework (PPF) in Customizing for Cross-Application Components under

Processes and Tools for Enterprise Applications

  Reusable Objects and Functions for BOPF Environment

  PPF

## Adapter for Output Management

  Maintain PPF Settings . In application /SCMTMS/TRANSPORTATION, you activated

the action definition TOR_TPNOR_CO (Replication of Consignment Order) of action profile /SCMTMS/TOR.

In addition, you have assigned the output profile /SCMTMS/TOR to the consignment order type you use. You assign the

output profile in Customizing for Transportation Management under  Freight Order Management

## Consignment Order

  Define Consignment Order Types  in section Output Options.

Receiving Air Freight Bookings from the Carrier

  Note
The EDI messages you receive from the carrier must contain certain information. For some XML samples, see SAP note

3514066

.

The carrier can send you EDI messages with information about the air freight bookings. The message can be used for creating and

updating the air freight booking in your system. It can be used for creating the air freight booking when the planning of the freight

booking by the carrier is done. Alternatively, it can be used for updating the air freight booking.

First Message from the Carrier (Creating)

With the first message, the carrier informs you which consignment orders are planned on which flight. The message for creating

the air freight booking must contain information, such as:

## Carrier number

Stage information, such as stage between airport of departure and airport of destination, source and destination location

specified by IATA code, stage category, flight code, expected departure time, expected arrival time

Item information, such as item category, referenced consignment orders, house air waybill (HAWB) per customer

Event information (optional), event type, stop identification specified by IATA code

When the carrier sends the message before flight departure, the event information is not necessary.

With this information, the air freight booking with the referenced consignment orders can be created in your system.

## Update Messages

When the flight departed, the carrier can send you an update message. Maybe the planning was changed, or some cargo was not

transported with the flight.

The messages can include information such as the referenced consignment orders, uplift confirmed status when the airplane

departed or additional event updates when the airplane arrived at the destination airport.

Alternatively, you can manually enter updates in the freight booking.

## Identifying Locations by IATA Codes

The system finds locations using the IATA codes that were sent with an inbound message. If the handling of errors for business

documents is activated for the freight booking type, the system displays document errors if the IATA code couldn't be found, isn't

unique or is wrong.

This is custom documentation. For more information, please visit SAP Help Portal.

92


1/14/26, 2:18 PM

In exceptional cases, creating a freight booking on an inbound message fails, for example, when the message contains a non-

unique IATA code and at the same time, the departure is already set for the air port of loading. Such a message will fail, and the air

freight booking will not be created as the system can’t identify the location and therefore can’t set the departure status for the

location.

To enable this check, you need to activate the handling of errors for business documents in Customizing for the air freight booking

type.

## Update Port of Destination

Changing the port of destination on inbound messages works the same in the ocean and in the air process. For more information,

see Ocean Freight Bookings for Shippers (Outbound).

## Sending ASN to Customer

The consignment orders and their updates are also sent to the customer to inform them about the transport.

In the following cases, the system sends a separate advanced shipping notification (ASN) message for each consignment order to

the customer when the airplane departed. At this point in time additional booking information is available and can be included in

the ASN.

When the goods movement status on consignment order is set to Completely Processed.

When the air freight booking is set to Departed from port of loading.

Alternatively, when manually requested in the consignment order under

 Follow Up

  Send Advanced Shipping

Notification .

Especially in a door-to-port scenario, consignment orders and their updates are useful for customers. Depending on the Incoterms,

they might need to know the voyage number and the expected date and time of arrival to organize the pickup and transport of the

goods for the last stage.

## Related Information

Sample Air Freight Process for Shippers (Outbound)

## Consignment Order

## Cargo Left Behind at Port/Airport

Sample Ocean Freight Process for Shippers (Outbound)

Ocean Freight Bookings for Shippers (Outbound)

## Advanced Shipping and Receiving

Sample Air Freight Process for Shippers (Outbound)

This topic describes a sample air freight process for shippers. It involves a door-to-door air freight booking that includes

transportation stages for the pre- and on-carriage. The process is also available for a door-to-port scenario. It is designed for

Advanced Shipping and Receiving.

For the process, we assume the following:

The planning of the main stage is done by the carrier. The freight units originate from outbound deliveries. The shipper initiates the

air freight process without pre-booking capacity, meaning they don't create an air freight booking. Instead, the process begins with

creating a pick-up freight order. Furthermore, consignment orders are created manually and air freight booking updates from the

carrier are received via EDI communication.

This is custom documentation. For more information, please visit SAP Help Portal.

93


1/14/26, 2:18 PM

This process gives you a high-level overview with the most important process steps. For more background information and

prerequisites about the process in general, see Air Freight Bookings for Shippers (Outbound).

## Creating Transportation Requirements

You create outbound deliveries. The system automatically creates freight units.

You can, for example, use the Create Outbound Deliveries app from the launchpad.

## Performing Warehouse Activities

Picking (and possibly packing) is carried out by the warehouse workers. It is performed in the respective storage location, for

example for Lean Warehouse Management in an inventory-managed (IM) storage location or a storage location for Extended

Warehouse Management (EWM).

Processing Pick-Up Freight Orders

1. Creating Pick-Up Freight Order to the Airport

You create a pick-up freight order for a road transport.

On this freight order, you plan all goods (all packed freight units) that need transportation via the same airport. You assign a

carrier.

You do so in the Freight Bookings Work List or the Freight Orders Work List, you choose query Pick-Up/Delivery, and then

## New

  Road Freight order for Pick-Up/Delivery  or  New

  Rail Freight order for Pick-Up/Delivery .

2. Creating Consignments

Out of the pick-up freight order to the airport, you create consignment orders to be able to communicate with the carrier.

Based on these consignment orders, you inform the carrier about the goods that need to be transported.

In this example, the consignment orders are created based on the top-level package, this means, each consignment order

contains only one package item (for example, “pallet”) or unpacked product. This allows different handling units to be

transported on different flights. Settings in the consignment building profile are necessary.

In the pick-up freight order, you create consignment orders manually under  Follow up

## Build Local Consignment Orders

. You then create consignment order documents for the local consignment orders under  Follow up

## Create

Consignment Order

.

3. Loading Cargo

Before you load the cargo, the pick-up freight order must have the Ready for Transportation Execution status.

You have several options to set the loading status in the system:

In the Load or Unload Freight Orders app

In the Edit Road Freight Order app

Via Radio Frequency (RF) in EWM

4. Posting Goods Issue

You post goods issue for the pick-up freight order. When you post goods issue, the system sets the goods movement status

of the freight order to Completely Processed. It also propagates this status to the assigned consignment order.

As result, the system automatically sends an Advanced Shipping Notification (ASN) to the customer.

This is custom documentation. For more information, please visit SAP Help Portal.

94


1/14/26, 2:18 PM

In addition, the system sends a TransportationOrderGenericRequest_Out message (with Business Scope

“EXTERNAL_PLANNING”) to the main-carriage carrier.

Additional configuration is necessary for this message. For more information, see Air Freight Bookings for Shippers

(Outbound).

Assignment of Consignment Orders to Air Freight Booking by Carrier

1. Receiving Freight Booking from the Carrier (Create Freight Booking)

The carrier decides which cargo is transported with which flight and plans the received consignment orders. As each

consignment order includes only one package item (a pallet), the consignment orders can be flexibly distributed on suitable

flights.

The carrier creates the corresponding air freight bookings and informs you, the shipper, which consignment orders (goods)

are planned on which flights. You receive the air freight booking with the assigned consignment orders from the carrier via

message. The message includes data, such as carrier number, house airwaybill (HAWB), referenced consignment orders,

expected date and time of arrival.

With the information from the message, the air freight booking with the referenced consignment orders is created in your

system.

Once an air freight booking is assigned, you can display the booking information on the Booking Data tab in a consignment

order.

When consignment orders aren’t yet assigned to an air freight booking, the system displays a document error in the pick-

up freight order and in the consignment order.

These errors disappear once an air freight booking is assigned to the consignment orders.

2. Receiving Updates for Freight Booking from the Carrier (Update Freight Booking)

After a flight departs, the carrier sends you subsequent EDI messages containing updates for the air freight booking. The

message can include data, such as HAWB, Uplift Confirmed status, and information about the consignment orders that

were planned on the flight.

## Departure of the Airplane from the Port of Loading

With the air freight booking departure, the system also sends an Advanced Shipping Notification (ASN) to the customer for

each consignment order. These ASNs include the updated flight information.

## Reporting Arrival of Airplane

The carrier might send a message per air freight booking / HAWB to confirm the arrival at the airport of destination.

## Processing Delivery Freight Orders

In a door-to-door scenario, you create a delivery freight order for the further transport.

To do so, you select the relevant consignment orders (or freight units) in the Edit Air Freight Booking app on tab Capacity and

Cargo, and choose  Create

  Create Freight Order for Delivery with Default FO Type .

This order facilitates the collection of goods from the airport of discharge. The goods are then transported to the destination

location, which is typically the customer's address.

## Related Information

This is custom documentation. For more information, please visit SAP Help Portal.

95


1/14/26, 2:18 PM

Air Freight Bookings for Shippers (Outbound)

## Cargo Left Behind at Port/Airport

For various reasons, for example, a capacity shortage on a vessel or an airplane, it can happen that cargo that was already

transported to a port or an airport can't be shipped on the initially planned voyage or flight. In ocean and air freight transportation,

you have different ways to handle cargo that was left behind at the port or airport of loading.

## Prerequisites

The following prerequisite is relevant when you decided to use the left behind function:

To enable the loading status on item level at the port/airport you've selected the Itm Load. Stat. Port checkbox for the event profile

used for the freight booking type in Customizing for Transportation Management under  Freight Order Management

  Execution

## Settings

  Define Event Profiles .

You've then assigned the event profile to the freight booking in Customizing for Transportation Management under  Freight Order

Management

## Freight Booking

  Define Freight Booking Types .

When you activated the function, make sure, that only one main carriage is defined for the freight booking type.

For ocean freight booking types, you can define this setting in Customizing for Transportation Management under  Freight

Order Management

## Freight Booking

  Define Freight Booking Types . Set the dropdown list FB for Multi-PU/DL

(Freight Booking for Multi-Pickup and Multi-Delivery) to One Port of Loading and One Port of Discharge.

For air freight booking types, check that just one port of loading and one port of discharge is defined.

## Activating the Left Behind Function

If you want to use the left behind function, you activate the loading status on item level checkbox at the port/airport in the event

profile.

This scenario is useful in ocean freight processes for shippers. It enables the replanning for containers that weren’t loaded to the

vessel. As a prerequisite, you need to receive freight booking departure updates for each container from the carrier. For more

information about this process, see Sample Ocean Freight Process for Shippers (Outbound) .

When only some of the items on a freight booking can be loaded and shipped as planned, you can set the status Loaded for those

items individually during loading.

When container items in an ocean freight booking don't have the Loaded status as the vessel leaves the port (or the airplane the

airport) and the stop is marked as Departed, the system identifies a status mismatch. This discrepancy triggers the creation of a

document error.

## Document Errors

In your freight booking worklist, you can search for freight bookings containing document errors for items that weren't loaded.

You can view these errors on the Document Errors tab in the freight booking. Containers that haven’t received a loading update

yet, or those with unrecorded status, remain on the ocean freight booking. An error might be temporary if not all container update

messages have arrived or have been processed yet.

You can resolve the document errors in one of the following ways:

This is custom documentation. For more information, please visit SAP Help Portal.

96


1/14/26, 2:18 PM

On the Documents Errors tab in the ocean freight booking, you can assign the left behind container units to a different

ocean freight booking with a later departure date or time. Regarding the document chain, the container unit is then still

assigned to the pick-up freight order but will be assigned to the new ocean freight booking.

Alternatively, you can set the container to Loaded if the items were loaded but the status wasn't recorded in the system.

This might occur if the “loaded” setting wasn’t reported due to an oversight, or the container update message hasn’t arrived

yet.

The container unit remains on the ocean freight booking until it is reassigned to a different ocean freight booking either manually

or by an update message from the carrier.

## Invoicing Blocks

You can trigger the invoicing and subsequent settlement of a freight booking only after the departure of a vessel or airplane.

For freight bookings with document errors, the system sets an invoicing block to prevent the invoicing processes and restrict the

subsequent settlement processes.

For freight bookings with invoicing blocks, the freight carrier invoice (FCI) is created with lifecycle status as Draft and you can’t

release the invoice until you remove the invoicing block. You can view the invoice block details in the Blocking Information tab of

the freight booking.

To remove the invoicing block, you have to report the departure by updating the shipped on-board status of the ocean or air freight

booking. Changing the status reports the departure and removes the invoicing block. For an ocean freight booking set the status to

Shipped on Board and for an air freight booking set the status to Set to Uplift Confirmed.

Once the invoice block is removed from the freight booking, the draft freight carrier invoice is automatically released.

Once you report the departure, check document errors to confirm loading status of all the container units. If there are no document

errors, then there is no invoice block and the system can do the invoicing and subsequent settlement.

For more information about settlement, see Freight Settlement.

For more information about invoicing, see Carrier Invoice.

## Not Activating the Left Behind Function

If you don’t activate Loading Status on Item Level in the event profile that you assigned to your ocean or air freight booking type,

the cargo items are automatically unassigned from the freight booking when they aren’t loaded, and the vessel or airplane already

departs.

This scenario is especially useful in air freight processes. It helps you avoid working with error messages that occur due to

mismatched statuses and block the invoicing process until they are resolved.

  Note

If you don’t activate the left behind function, consider the following system behavior:

The system automatically unassigns cargo items from a freight booking when you, as a shipper, receive single container

updates from your carrier via EDI communication. If you prefer the cargo items to stay on the freight booking, you should

activate the left behind function.

If you use the air freight process that starts without a freight booking but with a pick-up freight order and you don't activate the

left behind function, the system also unassigns the consignment orders or freight units from the freight booking. However, the

This is custom documentation. For more information, please visit SAP Help Portal.

97


1/14/26, 2:18 PM

assignment to the pick-up freight order persists. For more information about this process, see Sample Air Freight Process for

Shippers (Outbound).

## Example

The following figure shows an example of how to manage cargo that was left behind at a port.

You want to ship two container units, CU1 and CU2. You create an ocean freight booking, 2410, and assign both container units to it.

Once the transportation planning is finished, the freight orders for pick-up are created and executed, and the cargo is transported

to the port. You send a notification to your carrier. It contains the information that the two container units are planned on ocean

freight booking 2410.

During loading, the carrier notices that there is only enough room for CU1 on vessel 1234. After CU1 is loaded, the carrier sets its

status to Loaded. The vessel departs, and the carrier sends you a shipped-on-board confirmation. It contains the information that

CU1 was loaded onto vessel 1234 and that CU2 was left behind at the port and needs to be reassigned.

A document error is created. On the Document Error tab, you can see that CU2 wasn't shipped as planned. You reassign CU2 to

ocean freight booking 1005.

At the port, the carrier loads CU2 on vessel 5678 (freight booking 1005), and sends a notification once the vessel departed.

## Transportation Unit

This is custom documentation. For more information, please visit SAP Help Portal.

98


1/14/26, 2:18 PM
## Definition

With this business document you can depict transport requirements or capacity, for example:

## A trailer and its load

The capacity of a railcar or several railcars that are transported together

## A container and its load

A package, such as a pallet or a carton, and its load

## Use

You use the transportation unit to consolidate freight units. You can then plan the transportation unit as a unit for several

transportation stages, in other words you can assign it to one or more freight orders.

A transportation unit always represents a transportation requirement and is therefore a requirement document that you can assign

to a capacity document. However, a transportation unit can also represent transportation capacity if it was not created during

freight unit building. In this case, it is also a capacity document.

Within the transportation unit type, you configure the most important settings for the transportation unit. For example, you use the

transportation unit category to indicate whether you want to create the transportation unit type for a trailer, a railcar, a container,

or a package. When you then create the related business document (for example, a trailer unit), the system offers you only the

relevant transportation units. For more information, see Customizing for Transportation Management under  Freight Order

## Management

## Transportation Unit

 Define Transportation Unit Types .

More Information

Trailer Unit

Railcar Unit

Container Unit

## Package Unit

Creation and Editing of Transportation Units

Trailer Unit

## Definition

Trailer units make up the logistic processing of transports with trailers.

## Use

You need a trailer unit if a trailer is moved by more than one tractor.

You configure the most important settings for the trailer units in the transportation unit type. For more information, see  Freight

Order Management

## Transportation Unit

 Define Transportation Unit Types .

You cannot perform subcontracting for trailer units.

This is custom documentation. For more information, please visit SAP Help Portal.

99


1/14/26, 2:18 PM
## Structure

Trailer units contain the following information:

## General data such as locations and dates

You can enter one-time locations at stage level. The system stores these new locations and adjusts stages in the document.

It also adjusts the locations in the assigned execution documents.

  Note

However, you should continue to make changes to existing locations in the master data.

## Transportation stages

On the Stages tab, you see the following information:

Assignment of the trailer to one or more tractors

Route the trailer will take

## Transportation stage types

You can also apply a standard route here (see Standard Route) and perform a simple scheduling.

You can also define appointments. For more information, see Appointment.

## Freight

On the Freight tab page, the following information is displayed:

Quantities and weights (see Quantities and Capacities)

Goods information (see Goods Information)

Dangerous goods information (see Considering Dangerous Goods)

Seal information (see Use of Seals)

Information about foreign trade (see Integration with SAP Global Trade Services)

For more information, see Cargo Management.

## Overview

The Overview tab is an integrated view of the Stages and Freight tabs. It contains the following information:

Assignment of the trailer to one or more tractors

## Route the trailer will take

The maximum utilization as well as planned departure and arrival times

You can also define appointments. For more information, see Appointment.

Execution information, for example, actual departure times

Furthermore, you can directly report events.

Document dependencies as well as predecessor and successor documents (document flow)

Status information and blocking information (see Statuses of Business Documents and Blocking Information)

Change documents (see Change Tracking)

This is custom documentation. For more information, please visit SAP Help Portal.

100


1/14/26, 2:18 PM
## More Information

Creation and Editing of Transportation Units

Trailer Handling During Trailer Swap

Internal Settlement for Resources

## Triangulation

Trailer Handling During Trailer Swap

## Use

You can determine the ideal location in your transportation chain at which to swap trailers.

## Prerequisites

In your master data, you have created transportation zones that contain the source location and target location for the

transport. You define transportation zones by opening the Define Transportation Zone app on the launchpad.

You have defined a strategy for trailer handling for the locations within these transportation zones. You define strategies for

trailer handling at a specific location by opening the Define Location app on the launchpad and selecting a strategy for

trailer handling on the TM tab page.

## Features

The system checks each location to determine whether trailers can be swapped and if so, under which conditions. It does so for

each location in the transportation zone containing the source location, and for each location in the transportation zone containing

the destination location, by using the trailer handling strategy defined for each location. The following options exist for each

location:

## Coupling not possible

At these locations, coupling and decoupling is not permitted. This strategy applies, for example, to customer locations.

## Coupling possible

At these locations, coupling and decoupling is generally permitted. This strategy is often used for production plants,

distribution centers, and other secure locations at which a trailer can be left unguarded for a short amount of time.

## Coupling possible only during pickup or delivery

At these locations, coupling and decoupling is permitted only if a freight unit is collected from or delivered to this location at

the same time. This strategy is often used at customer locations at which the trailer is parked for the duration of the pickup

or delivery process.

## Only trailer swap possible

At these locations, coupling and decoupling is permitted only if the trailer is not left unguarded at any time. As soon as a

trailer is decoupled from a truck, it must be coupled to another truck. This strategy is often used at insecure locations such

as parking lots or service stations.

## Activities

This is custom documentation. For more information, please visit SAP Help Portal.

101


1/14/26, 2:18 PM

You determine the optimal coupling location for a trailer swap by opening the Transportation Cockpit app on the launchpad and

starting Optimizer Planning (see VSR Optimization).

More Information

Example: Trailer Swap

## Example: Trailer Swap

The following example describes a simple trailer swap.

First, you create the following trailer units and specify the sequence of locations, that is, the route:

## Document

Location sequence

## Creation type

Trailer unit 40 (TRL40)

Trailer unit 41 (TRL41)

A-B-C

## C-B-A

Creation in the transportation cockpit

Creation from the user interface for

creating trailer units

In this example, truck 01 drives from A to B with trailer X. There it meets truck 02, which has driven trailer Y from C to B. The trailers

are switched in B. Truck 01 then drives trailer Y from B back to A. Truck 2 drives trailer X from B back to C.

The documents and assignments look like this:

## Document

Location sequence

Assigned trailer units

Freight order 20 (FO20) C-B-C

TRL41 (C-B)

TRL40 (B-C)

Freight order 21 (FO21)

## A-B-A

TRL40 (A-B)

TRL41 (B-A)

The following figure shows this type of trailer swap:

This is custom documentation. For more information, please visit SAP Help Portal.

102


1/14/26, 2:18 PM

Trail swap illustrated in an example with two trucks with trailers

Railcar Unit

## Definition

A railcar unit makes up the logistic processing of transports with railcars. It describes the assignment of cargo to a railcar.

## Use

A railcar unit can comprise one or more railcars. If a customer orders a full carload and you have already defined the railcar items in

the forwarding order, the system can create a railcar unit instead of a freight unit during freight unit building. The relevant item in

the forwarding order must be of type Passive Vehicle Resource and you must have entered a transportation unit in the freight unit

building rule.

If you have not already created the railcar items in the forwarding order, you can use the railcar unit as a consolidation document.

This means that the freight unit is created based on a product item, for example. You then assign this product freight unit to the

railcar unit. Alternatively, you can assign the freight unit directly to a railcar that you have created in the rail freight order.

You can define several main items for railcar units. You can also work with multi-items (see Items).

A railcar unit must be assigned to a rail freight order (see Rail Freight Order) before you can carry out the follow-on processes. You

can assign the individual stages for the railcar unit to one or more rail freight orders. You cannot subcontract railcar units. The

railcar unit is used only for logistical purposes and for the assignment of different subcontracting documents.

This is custom documentation. For more information, please visit SAP Help Portal.

103


1/14/26, 2:18 PM

Within the transportation unit type, you configure the most important settings for the railcar unit. For more information, see

Customizing for Transportation Management under  Freight Order Management

 Transportation Unit

 Define Transportation

Unit Types .

## Structure

Railcar units contain the same information as trailer units (see Trailer Unit). The following points are variances:

## General Data

Here, you can enter the following data:

Source location and destination location (rail)

## Number of railcars

Number of assigned rail freight orders

## Resources/Equipment

Information about your railcar is displayed here:

Position of a railcar in the train

## Equipment group and equipment type

Railcar details such as whether the railcar belongs to the shipper or the carrier

## Seal information

The handling execution status and the cargo execution status behave in the same way as for rail freight orders. For more

information, see Rail Freight Order.

## Applying Default Routes

You can search for possible routes in your railcar unit based on the source location and destination location (Default Route

pushbutton). The system uses the default routes to identify various routes, from which you can choose one.

More Information

## Triangulation

Creation and Editing of Transportation Units

Container Unit

## Definition

A container unit models the logistical handling of the transportation of one or several containers. Each of these containers can

contain several freight units.

## Use

If a customer orders a full container and you have already defined the container items in the forwarding order, the system can

create a container unit instead of a freight unit during freight unit building. The relevant item in the forwarding order must be of

This is custom documentation. For more information, please visit SAP Help Portal.

104


1/14/26, 2:18 PM

type Container and you must have entered a transportation unit in the freight unit building rule.

If you have not already created the container items in the forwarding order, you can use the container unit as a consolidation

document. This means that a freight unit is created based on a product item, for example. You then assign this product freight unit

to the container unit. Alternatively, you can assign the freight unit directly to a container that you have created in the freight

document.

You can define several main items for container units. You can also work with multi-items (see Items).

A container unit must be assigned to a freight document before you can carry out the follow-on processes. You can assign the

individual stages for the container unit to one or more freight documents. You cannot subcontract container units. The container

unit is used only for logistical purposes and for the assignment of different subcontracting documents.

Within the transportation unit type, you configure the most important settings for the container unit. For more information, see

Customizing for Transportation Management under  Freight Order Management

 Transportation Unit

 Define Transportation

Unit Types .

To create container units, open the Create Container Unit app on the launchpad.

## Structure

Container units contain the same information as trailer units (see Trailer Unit). The following are only special features:

## General Data

Here, you can enter the following data:

Source location and destination location

## Number of containers

## Number of assigned freight documents

Information about whether container provisioning and return is required

## Freight

## Container Details

## Transportation unit resource

If you have defined your container as a transportation unit resource in the master data you can jump directly

to the master data here.

## Equipment group and equipment type

Information about whether the container is owned by the shipper

  Note

If you have created a container as a multi-item, the system displays fewer details because the container is simply

a "grouping".

## Equipment

Seal information

## Document references

This is custom documentation. For more information, please visit SAP Help Portal.

105


1/14/26, 2:18 PM
## Restrictions

VSR optimization (VSR = vehicle scheduling and routing) including scheduling can take container units into account only as

requirement documents and not as capacity documents. This means that VSR optimization can plan, in other words assign,

container units in freight documents and other transportation units. It cannot, however, assign freight units to a container

unit. This is possible in manual planning only.

VSR optimization including scheduling takes into account the pickup and delivery windows for freight units assigned to a

container unit. However, if you have defined times at a given stop of a container unit, VSR optimization takes these times

into account and ignores the time windows of all assigned freight units at this stop.

## More Information

Creation and Editing of Transportation Units

## Package Unit

Transportation Management (TM) allows you to consolidate freight units in package units so that they can be transported together

across several transportation stages and freight documents. You can deconsolidate the packages in the last transportation stage of

your route. A package unit can comprise one or more packages as main items. Packages can be pallets, pallet cages, or cartons, for

example.

## Prerequisites

For more information about the required settings in Customizing, see Creating a Package Unit.

## Use

A package unit has essentially the same structure as a container unit and can be used in the same way (see Container Unit).

However, it has special features that are described below.

## Assignment to Other Transportation Units

You can assign package units to other transportation units such as container, trailer and railcar units.

Route with Linear Stages and Delivery Tour (Distribution Stops)

You can create the route of a package unit in such a way that the packages are transported together across several transportation

stages, but can be deconsolidated on one delivery tour. This means that you can unload packages and individual products from the

packages at individual locations on the delivery tour.

In addition to the linear, consecutive transportation stages, your route contains a kind of placeholder stage (virtual stage) that

represents a group of stops in the delivery tour (distribution stops). These stages appear in the stage table as substops of the

virtual stage, but they can be served in any sequence.

## Assignment of a Freight Unit to Several Package Units

If you create package units from a freight order, the system can also assign a freight unit to several package units. This means that

the items of a freight unit can be divided among several package units. Not only individual items can be assigned to several

package units, but also subsets of an item. For example, if an item of a freight unit contains 10 units, 6 units can be assigned to one

package unit and the remaining 4 units to another package unit.

This is custom documentation. For more information, please visit SAP Help Portal.

106


1/14/26, 2:18 PM

You do not have to split the freight unit if the different package units to which a freight unit is assigned are transported with the

same freight documents. If they are transported with different freight documents per stage, the system splits the freight unit

accordingly and distributes it among the freight documents.

To avoid unnecessary splits or the unnecessary creation of deliveries, the system only considers a freight order for the delivery

creation if the load planning for the freight units in this freight order has been completed. For more information, see Delivery

Creation and Split for Package Units with Multiple Assignments.

In the stage details of a freight unit or in the transportation cockpit, you can display the package units to which a freight unit is

assigned on the Assignment to Package Units tab page.

## Display the Exact Position of Products in a Package

You can display and change information about the exact position of products in a package (for example, on a pallet) on the Items

tab page in the Load Plan hierarchy view. This information can be determined during unified package building by optimization.

You must have first activated the Detailed Mixed Package Building in the unified package building profile. For more information,

see Detailed Mixed Package Building.

You also get a 3D visualization of the package. For more information, see Load Plan.

## Integration with Material Master Data

Information from the material master data for the packaging material is decisive for the calculation of volume and weight

information (and not the resource master data which is the case for the other transportation units).

Related Information

## Creating a Package Unit

Transportation Planning with Mixed Packages and Deconsolidation

## Creating a Package Unit

You have different options in Transportation Management (TM) for creating a package unit. For example, you can create package

units when you create freight units or later in the freight order based on the packages that exist there. The different options are

described below.

## Prerequisites

You have made all the required settings for package building. For more information, see Unified Package Building in TM.

You have defined a transportation unit type so that you can model packages. You can specify the following in this type:

## Whether package building has been activated for this document type

Whether a freight unit can be assigned to several packages (Assgnmt of Pred.Docs (Assignment of Predecessor

Documents) field)

For more information, see Customizing for Transportation Management under  Freight Order Management

## Transportation Unit

 Define Transportation Unit Types .

You have defined a default package unit type in Customizing for the freight order type. For more information, see

Customizing for Transportation Management under  Freight Order Management

## Freight Order

 Define Freight Order

Types .

This is custom documentation. For more information, please visit SAP Help Portal.

107


1/14/26, 2:18 PM
## Features

## Manual Creation of a Package Unit

Open the Create Package Unit or Package Units - Worklist app on the launchpad. The worklist gives you an overview of all existing

package units and from there you can also create new package units.

When a package unit is created, a main item for the package is entered on the Items tab page. You can add more main items for the

package and product subitems and assign freight units. You can select freight units based on a forwarding order or the freight unit

ID, for example.

You can specify a linear sequence of transportation stages as well as a delivery tour on the Stages tab page. You can also assign a

default route or a transportation proposal and select a schedule.

To model a delivery tour, you can specify in the Customizing settings for the transportation unit type that the package unit contains

a special (virtual) stage with distribution stops (field:  Seq. Type of Stages (Sequence Type of Stages)

## Linear with Distribution

). In this case, the following applies:

The system automatically creates a transportation stage as a virtual stage with a distribution stop in the stage table. You

can then create as many additional distribution stops as you want.

You can create a start location but not an end location for the virtual stage. You can create only one end location at a time

for the distribution stops. The start location of the distribution stops is always the location of the virtual stage.

The route can contain any number of linearly consecutive transportation stages before the virtual stage, but the virtual

stage must be the last stage of the route.

## Creation of a Package Unit from a Forwarding Order

You can create package units for transportation stages on the Actual Route tab page in forwarding orders. For more information,

see Direct Creation of Capacity Documents and Selection of Schedules.

## Creation of Package Units from a Freight Order

After you have set the load plan status of the packaging to "Finalized” for a freight order or individual packages of the freight order,

you can let the system create package unit documents for these packages. To do this, select the Create Package Units option

either under Follow Up (for the entire freight order) or on the Items tab page of the freight order in the Load Plan hierarchy view

(for individual packages). You can also select this option in the transportation cockpit.

This function has the following prerequisites:

You have selected the value Linear with Distribution in the Seq. Type of Stages (Sequence Type of Stages) field in the

default package type that you assigned to the freight order type of your freight order.

You have indicated in the Default Package Unit Creation Rule field whether the system is to create one package unit per

package (default) or one package unit for all selected packages.

Note that a package unit created in this way is fixed. This means that you can no longer make any changes to the package unit.

However, you can also undo the creation of package units if you want to make changes, for example. You can let the system cancel

the package units and merge the individual packages back into the item hierarchy. To do this, select the Cancel Package Units and

Merge option either under Follow Up (for the entire freight order) or on the Items tab page of the freight order in the Load Plan

hierarchy view (for individual package units).

The creation of package units from a freight order is part of the planning process with mixed packages and deconsolidation. For

more information, see Transportation Planning with Mixed Packages and Deconsolidation.

This is custom documentation. For more information, please visit SAP Help Portal.

108


1/14/26, 2:18 PM

Automatic Creation of a Package Unit Using the Freight Unit Building Rule

You can create package units using the freight unit building rule (FUB rule) as follows:

If you want the system to create package units directly based on the items that already exist in the order documents or

delivery documents (such as forwarding orders or sales orders), you can choose a document type for package units in the

FUB rule. To do this, open the Create Freight Unit Building Role app on the launchpad.

If you want to create package units with a complete package hierarchy using the FUB rule, enter a profile for package

building in addition to the document type for package units on the Advanced Settings tab page of the FUB rule. Then select

the maximum number of higher-level packages that a package unit can contain and select the Create Complete Package

Hierarchy option in the Package Building Result field.

Certain data, such as capacity information, can no longer be changed in the automatically created package units. The system also

sets the status Load Plan Finalized and the fixing indicator for these package units so that they are fixed for further planning.

When you assign one of these package units to a freight order, the status and the fixing indicator remain unchanged.

For more information, see Freight Unit Building Rule.

## Manual and Automatic Creation of a Package Unit Using the Transportation Cockpit

You can create and schedule package units in the transportation cockpit. You can, for example, assign freight units to the package

units and then assign the package units to freight documents. Moreover, you can schedule the package units with optimization.

For more information, see Use of Package Units in Planning and Planning with Distribution Stops.

## Displaying the Origin of a Package Unit

You can see in the package unit document how it was created. This is displayed in the Origin of Package Unit field on the General

Data tab page. For more information, see the field help.

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

This is custom documentation. For more information, please visit SAP Help Portal.

109


1/14/26, 2:18 PM

More specifically, you have entered a unified package building profile in the planning profile that is assigned to the

document type or that you use to call the transportation cockpit. If you want to determine and display the exact position of

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

110


1/14/26, 2:18 PM

Planning Process with Mixed Packages and Deconsolidation

Planning of Delivery Tours

1. Creating freight units

You have the system automatically create freight units based on your order documents (such as forwarding orders or sales

orders) and using the freight unit building rule you defined. For more information, see Creation and Editing of Freight Units.

2. Creating a freight order for the delivery tour

You create a freight order for the unplanned stages of the freight units that belong to your delivery tour. You can also use the

VSR optimizer to do this. If you have specified this in your freight unit building rule, the system takes into account the

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

111


1/14/26, 2:18 PM

The following applies to package units created by the system:

The system creates the package units in such a way that a freight unit can be assigned to several package units. You

can display the package units to which a freight unit is assigned in the stage details of a freight unit or in the

transportation cockpit on the Assignment to Package Units tab page.

The system determines the type of package unit created and the way in which package units are built from packages

(1:1 or 1:n) from the Customizing settings for the freight order type and the planning profiles used.

The package units contain both the linear transportation stages and a special stage with the distribution stops of the

delivery tour. These stops are displayed as substops, but their sequence is arbitrary. The transportation stages of

the freight orders and freight units remain unchanged.

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

The package units created by the system can contain freight units that are assigned to several package units. If the different

package units to which a freight unit is assigned are transported with different freight orders in the main carriage, the

system splits the freight unit accordingly and distributes it among the freight documents. Note that you must have set the

load plan status (load planning) to "Finalized".

## Related Information

Use of Package Units in Planning

## Planning with Distribution Stops

This is custom documentation. For more information, please visit SAP Help Portal.

112


1/14/26, 2:18 PM

Use of Normalized Quantities and Capacities

## Load Plan Status Changes

Many of the steps of the "Transportation Planning with Mixed Packages and Deconsolidation" process have an effect on the load

plan status. The following sections describe how the load plan status changes after each process step. Note however that they only

refer to the first part of the process ("Planning of Delivery Tours").

## Initial situation

Let's assume the freight order created in this process has three freight units assigned to it (FU1, FU2, and FU3).

On item level, for example in the load plan hierarchy, the load plan status looks like this:

Load Plan Item Status (Cargo) (Description)

Load Plan Status (Capacity) (Description)

1. Vehicle Resource

1.1 Product 1 (FU 1)

1.2 Product 2 (FU 2)

1.3 Product 3 (FU 3)

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

Load Plan Item Status (Cargo) (Description)

Load Plan Status (Capacity) (Description)

1. Vehicle Resource

2. Package (local)

2.1 Product 1 (FU 1)

3. Package (local)

Not Relevant

Not Planned

## Planned

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

Load Plan Item Status (Cargo) (Description)

Load Plan Status (Capacity) (Description)

1. Vehicle Resource

Not Relevant

2. Package (local)

2.1 Product 1 (FU 1)

Planned

Planned

Planned

## Planned

## Not Relevant

This is custom documentation. For more information, please visit SAP Help Portal.

113


1/14/26, 2:18 PM

3. Package (local)

3.1 Product 2 (FU 2)

4. Package (local)

4.1 Product 3 (FU 3)

Finalizing packaging

Planned

Planned

Planned

Planned

## Planned

Not Relevant

## Planned

## Not Relevant

After you have finalized packaging for all items of your freight order, the load plan status looks like this:

Load Plan Item Status (Cargo) (Description)

Load Plan Status (Capacity) (Description)

1. Vehicle Resource

Not Relevant

2. Package (local)

2.1 Product 1 (FU 1)

3. Package (local)

3.1 Product 2 (FU 2)

4. Package (local)

4.1 Product 3 (FU 3)

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

Load Plan Item Status (Cargo) (Description)

Load Plan Status (Capacity) (Description)

1. Vehicle Resource

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

## Use of Normalized Quantities and Capacities

If you are using different packaging materials for planning in a road scenario, you can use normalized load consumption quantities

and capacities in Transportation Management (TM) to optimize the use of the loading space. If, for example, your packaging

This is custom documentation. For more information, please visit SAP Help Portal.

114


1/14/26, 2:18 PM

material consists of pallet cages and europallets, you can convert and plan these into europallets or loading meters. The capacity of

a truck can also be defined as a normalized capacity.

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

unit of measure of the NLQ and the unit of measure of the ALQ in the Customizing activity Define Conversion Between NLQ

and ALQ UoM.

For more information, see Customizing for Transportation Management under  Basic Functions

## Normalized Quantities

(NLQ) and Additional Normalized Quantities (ALQ)

 Define Conversion Between NLQ and ALQ UoM .

You have entered the capacity for the NLQ in the default unit of measure in the master data for the resources you are using.

For more information, see Definition of Capacity.

This is custom documentation. For more information, please visit SAP Help Portal.

115


1/14/26, 2:18 PM

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

The system then takes into account the full package definition of the product master data that you have defined in the transactions

for creating or changing materials. It divides 1 by the defined full package quantity. For example, 1 EPL divided by 100 pieces results

in 0.01 EPL per piece of the product. It then takes into account the full package definition of the reference product master data in

one of these apps.

  Note

The system iteratively moves up in the reference product hierarchy until it finds a value.

If the system can determine a value in one of these steps, this is the result and subsequent steps are not evaluated anymore. If the

system can’t determine a value in any of the steps, it returns value 0.

This is custom documentation. For more information, please visit SAP Help Portal.

116


1/14/26, 2:18 PM

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

The system calculates the maximum utilization, taking into account the most critical transportation stage and the most critical

unit of measure (mass, volume, or normalized quantity).

## Check Normalized Quantities in Documents

You can check whether the normalized quantities in your documents are current. You can cancel documents with obsolete

normalized quantities. For more information, see Check Normalized Quantities in Business Documents.

This is custom documentation. For more information, please visit SAP Help Portal.

117


1/14/26, 2:18 PM
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

Creation and Editing of Transportation Units

## Use

You can use this function to create, edit, and display transportation units.

## Prerequisites

You have defined the transportation unit types in Customizing. Within the transportation unit type, you configure the most

important settings for the transportation unit. For more information, see Customizing for Transportation Management under

Freight Order Management

## Transportation Unit

 Define Transportation Unit Types .

## Features

Creating Transportation Units

You have the following options:

## Manual creation in the transportation cockpit

You can create transportation units using drag and drop or using the relevant pushbutton. For example, you create a trailer

unit by assigning existing transportation stages (that is, freight units) to a trailer. For more information, see Use of Trailers.

Manual creation on the user interface for creating trailer units, railcar units, container units, and package units

You create the transportation unit and enter the items. To do this, open one of the following apps:

Create Trailer Unit

Create Railcar Unit

Create Container Unit

## Create Package Unit

You can create a forwarding order and freight units from the transportation unit. For more information, see Creation of

Forwarding Orders from Freight Orders. You can also create a capacity document, such as a freight order.

## Automatic creation from a forwarding order

This is custom documentation. For more information, please visit SAP Help Portal.

118


1/14/26, 2:18 PM

If, instead of creating freight units, you want to create transportation units automatically from your forwarding order, enter a

transportation unit type in the freight unit building rule. This function is also available for order-based and delivery-based

transportation requirements. For more information, see Creation and Editing of Freight Units.

Automatic creation in VSR optimization (road transportation only)

When you execute a VSR optimizer run with trucks, trailers, and freight units, the system generates trailer units and assigns

these to particular trucks.

## Manual creation by copying

You can create a transportation unit by copying an existing one (reference document). The system copies the header data

and the logistical data. However, it does not copy references to freight units and the confirmed capacity.

You can also create more than one copy of an existing transportation unit at the same time. In addition to the number of

copies, you can specify whether the numbers of the created documents are to be displayed in the dialog box.

  Note

You cannot copy transportation units that were created automatically during freight unit building (for a shortcut

scenario, see Freight Unit Building Rule).

## Defining Logistical Processing

After you have created the transportation unit, enter the following information:

## Route

You can either enter a route manually or apply a standard route (see Default Route).

Assignment to capacity documents and vehicle resources

## Trailer unit

You define at which locations coupling or uncoupling takes place. You also define to or from which tractor the trailer

is coupled or uncoupled. Moreover, you assign the trailer unit to a freight order. You make these assignments in the

transportation cockpit, for example. For more information, see Use of Trailers.

## Railcar unit

From your railcar unit, you create a rail freight order with a locomotive item (or one rail freight order for each

transportation stage). Alternatively, you can also create the rail freight order separately and then assign the railcar

unit. For more information, see Rail Freight Order and Rail Transportation.

## Container unit and package unit

You can assign the container unit and package unit to different capacity documents depending on the required

transportation mode:

Freight bookings

Rail freight orders

Freight orders

Railcar units

## Trailer units

You can also assign the package unit to a container unit.

This is custom documentation. For more information, please visit SAP Help Portal.

119


1/14/26, 2:18 PM

You then enter the required vehicle resource in the capacity document, such as the ship or airplane to be used to

transport the container unit. You can create the capacity document directly from the container unit or you can

create it separately and then assign the container unit.

If you assign a transportation unit to a capacity document, the system automatically transfers the transportation unit

items. For more information, see Transfer of Transportation Unit Items.

## More Information

Trailer Handling During Trailer Swap

Deviating Business Partner Addresses

## Creating a Package Unit

Transfer of Transportation Unit Items

## Use

The following describes how transportation unit items can be transferred to other business documents. For the sake of simplicity,

this function is explained for railcar units only and it is assumed that there is only one railcar unit and one product. However, this

function also supports trailer units and container units as well as more complex scenarios with several railcar items, railcar units,

and products.

## Features

## Forwarding order already contains railcar item

In this case, you already create a railcar item when you create the forwarding order. If you have made the necessary settings

in Customizing, the system automatically creates a railcar unit instead of a freight unit when it builds the freight unit (see

Creation and Editing of Freight Units). This contains the railcar item from the forwarding order. You then create a rail freight

order with a locomotive item and assign the railcar unit. The system automatically transfers the railcar item to the rail

freight order.

Forwarding order contains product only; one rail carrier is responsible for the entire transportation chain

In this case, you create a forwarding order and enter a pallet and a product. The system automatically creates a freight unit

during freight unit building that contains the product. You then create a rail freight order with a locomotive item and a railcar

item. If you assign the freight unit to the railcar unit, the system automatically transfers the pallet and the product as well.

This is custom documentation. For more information, please visit SAP Help Portal.

120


1/14/26, 2:18 PM

Forwarding order contains product only; several rail carriers are responsible for the transportation chain

In this case, you create a forwarding order and enter a product. The system automatically creates one or more freight units

during freight unit building. These units contain the product. You then create a railcar unit with a railcar item and assign the

freight units and the product. Next, you create a rail freight order with a locomotive item for each transportation stage of

the railcar unit. You can do this directly from the railcar unit, for example. The system automatically transfers the railcar

item and the product item to the rail freight order. In this scenario, the railcar remains stable across several transportation

stages (that is, in several rail freight orders). For the sake of simplicity, the figure below shows only one rail freight order.

Service Order

## Definition

An order that provides details of tasks that are to be carried out for individual items in a business document (for example, cleaning

and fumigating containers) or for the entire business document (for example, customs clearance for a freight booking).

## Use

A service order enables you to do the following:

Enter information about services that are to be carried out for a freight booking or items in a freight booking

## Calculate charges for the services

This is custom documentation. For more information, please visit SAP Help Portal.

121


1/14/26, 2:18 PM

Create settlement documents for the services after they have been executed

You can create service orders in two ways:

Create service orders from freight bookings, freight orders, freight booking items, or freight order items. With such a service

order you can:

Enter service items related to the freight booking, freight order, freight booking item, or freight order item.

Add service items that are not related to the freight booking, freight order, freight booking item, or freight order item.

You can do this using the “Add Service” action without marking another item.

Create stand-alone service orders without reference to any  freight booking, freight order, freight booking item, or freight

order item. You can use the “Create Service Order” function to create a service order by entering the service order type.

You make the required settings for service orders in Customizing for Transportation Management under:

## Freight Order Management

 Define Item Types for Freight Order Management

Freight Order Management

## Service Order

 Define Service Order Types

Basic Functions

 General Settings

 Define Service Types .

You can use the change controller to define how the system reacts to changes (see Change Controller).

## Structure

A service order contains the following information:

General data including the service provider, service order type, and status of the service order (see Statuses of Business

Documents)

Item overview that contains the following information:

Link to the freight booking or freight order for which the service order was created. (Applies only for service orders

created from freight bookings, freight orders, freight booking items, or freight order items).

IDs of the original freight booking items or freight order items for which services are to be carried out, for example,

containers or products. (Applies only for service orders created from freight bookings, freight orders, freight booking

items, or freight order items).

Services to be carried out

Location at which the services are to be executed and time period in which they are to be executed

Transportation charges (see Charge Calculation)

Document dependencies as well as predecessor and successor documents (document flow)

Other information such as the following:

## Notes

## Attachments

Change documents (see Change Tracking)

## Administrative data

## Output management information

This is custom documentation. For more information, please visit SAP Help Portal.

122


1/14/26, 2:18 PM

## Service Order Types, Service Item Types, and Service Types

In Customizing, when defining service order types, you can specify the allowed service item types (these must be item types of

category Service). You make the required settings for service order types in Customizing for Transportation Management under

Freight Order Management

## Service Order

 Define Service Order Types

.

For each service item type you can specify the allowed service types. For more information, see Customizing for Transportation

Management under  Freight Order Management

 Define Item Types for Freight Order Management

.

Then, you can use the service order type you defined to create a service order. You can specify one of the allowed item types for the

order and the system proposes the default service type for that item type. You can specify a different service type. If you change

this service type to a type that you have not specified in Customizing as allowed for this item type, the system returns a warning

message.

More Information

## Service Items

Creation and Editing of Service Orders

## Use

You can use this function to create, edit, and display service orders.

## Prerequisites

You have defined service types (for example, customs clearance, container cleaning, or checking container seals) in Customizing

for Transportation Management under  Basic Functions

 General Settings

 Define Service Types .

You have made the following settings in Customizing for Transportation Management under  Freight Order Management

 Service Order

:

You have defined service order types and specified a default type that the system uses for all service orders. Note that you

can also:

assign a default type to a freight booking type in Customizing for Transportation Management under  Freight

Order Management

## Freight Booking

 Define Freight Booking Types .

assign a default type to a freight order type in Customizing for Transportation Management under  Freight Order

Management

## Freight Order

 Define Freight Order Types .

You have defined which services can be carried out for a freight booking or freight order and for individual freight booking or

freight order items such as containers or products.

## Features

## Creation of Service Orders

You can create service orders in two ways:

You can create a service order from the freight booking or freight order user interface.

This is custom documentation. For more information, please visit SAP Help Portal.

123


1/14/26, 2:18 PM

You can create stand-alone service orders without reference to any freight booking, freight order, freight booking item, or

freight order item. To do so, open the Create Service Order app from the launchpad.

You create a service order from the freight booking or freight order user interface.

For more information, see Creating Service Orders.

## Editing and Displaying of Service Orders

On the Service Orders tab page in the freight booking or freight order, you can display an overview of service orders created for the

freight booking or freight order and for all freight booking or freight order items. A Service Orders tab page is also available in the

Details area of the Items tab page. This provides an overview of all service orders created for a specific item that you have selected

on the Items tab page.

  Note

The Items tab page replaces the Cargo Management tab page. You can personalize your user interface in such a way that the

system displays the old Cargo Management tab page.

You can also edit service orders using the following apps on the launchpad:

Service Orders

Edit Service Order

## Distribution of Costs

You can distribute costs in a freight order. As a logistics service provider (LSP) you can use the distributed freight cost from a

service order to settle with your external customers and to settle with your internal organizations. You can distribute costs for a

service item that references a logistics item in a freight document. You can only distribute costs in a freight document where you

have a logistics item that comes from an ERP item or a forwarding order. For more information, see Cost Distribution Management.

Creating Service Orders

## Use

The following is an example process for manually creating a service order.

## Prerequisites

You have made the required Customizing settings.

For more information, see Creation and Editing of Service Orders.

You have created a freight booking.

For more information, see Freight Booking.

## Process

1. You create a service order in one of the following ways:

You create a service order from a freight booking.

This is custom documentation. For more information, please visit SAP Help Portal.

124


1/14/26, 2:18 PM

To create a service order for the entire freight booking, choose the Create Service Order button at the top of the

freight booking UI. To create a service order for individual items in the freight booking, select the items on the Items

tab page and choose the Create Service Order button on this tab page. Note that you cannot create a combined

service order for a freight booking and items in a freight booking.

  Note

The Items tab page replaces the Cargo Management tab page. You can personalize your user interface in such a

way that the system displays the old Cargo Management tab page.

You create a standalone service order

Open the Create Service Order app from the launchpad.

The system displays the service order creation screen. The system automatically enters the following data, according to

your Customizing settings:

## Service order type

Purchasing organization and type

## Service order number

If you are creating a service order from a freight booking, in the Services screen area, the system automatically creates an

empty service item for the freight booking or for each freight booking item.

2. You enter the service provider and the services.

If you are creating a service order from a freight booking, you can assign one or more services to the freight booking or to

each freight booking item. The available services depend on which service types you have assigned to the freight booking or

item categories in Customizing for service orders.

You also enter the location and time at which each service is to be carried out. If required, you can enter a service item

description.

3. You calculate the charges.

For more information, see Charge Calculation.

You distribute costs. For more information, see Cost Distribution Management.

4. You check the service order and save it.

5. You inform the service provider about the required services.

You can use the generic output management framework to communicate with the service provider.

6. If you are creating a service order from a freight booking, you create a freight settlement document.

When the service provider has executed the services, you can create a freight settlement document (see Freight Settlement

Document). This serves as the basis for checking the invoice received from the service provider.

7. You cancel the service order (optional if you are creating a service order from a freight booking).

Note that if you cancel a freight booking, the system automatically cancels all related service orders.

## Consignment Order

In Transportation Management (TM), a consignment order represents a business document that you can use to group several

transportation requirements based on certain criteria, such as the same source and destination location, the same delivery

date/time, and the same business partner.

This is custom documentation. For more information, please visit SAP Help Portal.

125


1/14/26, 2:18 PM
## Use

A consignment order serves as an important basis for the communication between the partners that are involved in a business

process. For example, as a supplier you can communicate to your ordering party which products you will deliver to a certain

destination on a specific delivery date. The consignment order receives an ID that serves as a reference for the business partners.

Based on a consignment order, you can also perform subcontracting, charge calculation, settlement with the carrier, and shipment

tracking. It is not, however, possible to perform tendering based on a consignment order.

You can then assign the consignment order to a road freight order and in doing so stipulate on which truck the products contained

in the consignment order are to be transported. A consignment order can be assigned to only one freight order at a time and must

be completely assigned. A freight order can, however, contain several consignment orders. The transportation is then planned and

executed based on the freight order.

You can choose whether to perform subcontracting, charge calculation, settlement, and so on, for the freight order or the

consignment order. You can do this in Customizing for the consignment order type or freight order type by enabling charge

calculation and settlement or by indicating that the documents of this document type are relevant for subcontracting. For more

information, see Customizing for Transportation Management under  Freight Order Management

  Freight Order

## Define

Freight Order Types  and  Freight Order Management

## Consignment Order

  Define Consignment Order Types .

You can also assign a consignment order to a transportation unit, such as a container or trailer unit, and then assign this to the

freight order. However, the container or trailer unit must then contain a transportation stage that corresponds to that of the

consignment order.

Creating consignment orders for capacity documents that refer to requirement documents containing multiple main items is not

supported. Examples for requirement documents with multiple main items are:

Container unit with several container items

Package unit with several package items

## Consignment Order Creation Based on Top-Level Packages

You can use consignment order creation based on the top-level package (handling unit). When you use this function, each

consignment contains only one package item or unpacked product. This means, the system creates one consignment order per

handling unit (pallet).

For this function, the grouping rule TOP_CARGO Topmost Cargo Item (Package or Unpacked Product) is available in the

Consignment Building Profile app.

The consignment order creation based on top-level packages is, for example, useful in air freight processes for shippers. For more

information, see Ocean Freight Bookings for Shippers (Outbound) and Air Freight Bookings for Shippers (Outbound).

## BAdI to Determine Consignment Order Type

In the Consignment Building Profile app you can configure how the system determines the consignment order type. You can either

choose Document Type Defined in Profile or Document Type Defined by BAdI. This is useful especially if you need two

consignment order types that might have a different custom profile to be used in one freight order, for example to distinguish

consignment order for "normal" deliveries from consignment orders for deliveries with empties.

You can use BAdI /SCMTMS/CNS_EXTR_DET_DOC_TYPE to determine the consignment order type in the Consignment

Building Profile app. For more information, see Customizing for Transportation Management under  Business Add-Ins (BAdIs)

for Transportation Management

  Freight Order Management

  Consignment Building

  BAdI: Consignment Order Type

Determination .

This is custom documentation. For more information, please visit SAP Help Portal.

126


1/14/26, 2:18 PM
## Structure

You include requirements in a consignment order, that is, freight units or package units that are based on predecessor documents,

such as sales orders, scheduling agreements, or deliveries. These requirements must have the same source and destination

location as well as the same delivery date/time. Moreover, the business partners involved, such as shipper, consignee, and carrier,

must be the same.

A consignment order can contain only one transportation stage between the source and destination location, that is, no

intermediate stages. This stage must be strictly linear. The consignment order can also have only one shipper and one consignee.

The main item of the consignment order has the category “Consignment Order”. Freight units and package units, packages, and

products appear below the consignment order in the item hierarchy. You can also perform package building for the items of the

consignment order.

## Creating a Consignment Order

You can create a consignment order either manually or automatically using an inbound message (an advanced shipping

notification via EDI). To create the consignment order manually, open the Create Consignment Order app on the launchpad.

In the consignment building profile, you can also specify that consignment orders are automatically built locally in a freight order

when a freight order is created and saved, and that the corresponding consignment order documents are created later.

For more information, see Creation and Editing of a Consignment Order and Automatic Consignment Building.

## Worklist and Search Options for Consignment Orders

You can display your consignment orders in your personal worklist for consignment orders and call them from there. Open the

Consignments - Worklist app on the launchpad. You can also search for consignment orders by freight order, for example.

## Related Information

Creation and Editing of a Consignment Order

## Automatic Consignment Building

Ocean Freight Bookings for Shippers (Outbound)

Air Freight Bookings for Shippers (Outbound)

## Creation and Editing of a Consignment Order

In Transportation Management (TM), you can create consignment orders automatically using inbound messages as well as

manually. The options for creating consignment orders and an example of how to create and edit consignment orders are

described below.

## Prerequisites

You have defined consignment order types in Customizing. Within the consignment order type, you configure the most important

settings for the consignment order. For more information, see Customizing for Transportation Management under  Freight Order

## Management

## Consignment Order

 Define Consignment Order Types .

## Creation Options

You have the following options for creating a consignment order:

This is custom documentation. For more information, please visit SAP Help Portal.

127


1/14/26, 2:18 PM

## Manual creation

To create the consignment order manually, open the Create Consignment Order app on the launchpad. For more

information, see the process description below.

## Creation from a freight order

On the Items tab page in a freight order, choose Create Consignment Order. The system uses the consignment order type

that was defined in the freight order type. If a consignment order type was not defined in the freight order type, the system

uses the consignment order type that you have defined in the consignment building profile or planning profile or it uses the

default consignment order type predefined in the system (in this sequence). For more information, see Customizing for

Transportation Management under  Freight Order Management

## Freight Order

 Define Freight Order Types .

## Creation using an inbound message

Your business partner can send you the consignment order as an advanced shipping notification using EDI communication.

You then receive the message using the service interface TransportationOrderGenericRequest_In. Based on this

message, the system automatically creates a consignment order.

For more information, see Creation or Update of Consignment or Freight Orders on Inbound Messages.

If the inbound consignment order contains errors, it is usually still saved as a document in TM. If the freight units (FUs) in

the consignment order contain errors, the system first creates deliveries for the FU without errors. After you have corrected

the errors, the system either assigns the remaining FUs to existing deliveries or creates new deliveries for FUs with different

external delivery numbers. The errors are displayed on the Document Errors tab page and can be corrected here. For more

information, see Correction of Errors in Business Documents.

## Creation during manual planning using the transportation cockpit

In the transportation cockpit, you have different options for creating a consignment order and assigning it to a freight order

or truck, for example. For more information, see Use of Consignment Orders in Planning.

## Creation by copying

You can create a consignment order by copying an existing one (reference document). The system copies the header data

and the logistical data. However, it does not copy references to freight units.

You can also create more than one copy of an existing consignment order at the same time. In addition to the number of

copies, you can specify whether the numbers of the created documents are to be displayed in the dialog box.

If you copy an existing consignment order, you can enter a different consignment order type for the new consignment order.

This is useful if you want to copy certain attributes of an existing document into a new one, such as the location or carrier.

For example, you can copy an existing consignment order with the type Consignment Order for Load Consolidation and

create a new consignment order with a different document type, such as Consignment Order for Load Planning.

## Automatic building for freight units of a freight order

You can let the system group freight units in a freight order into consignment orders based on grouping rules. For more

information, see Automatic Consignment Building.

The Origin of Consignment Order field in the general data of the consignment order shows you how the consignment order was

created.

## Process

The following is a description of an example process for manually creating a consignment order. It is assumed that you already

know the most important transportation data, such as source and destination location and business partners.

1. Entering the general data

This is custom documentation. For more information, please visit SAP Help Portal.

128


1/14/26, 2:18 PM

You first enter the general data for your consignment order, for example:

Transportation data, such as shipper, consignee, carrier

Locations and dates/times

## Notes

2. Defining the items

You have the following options:

You add freight units or package units to your consignment order. You do so on the Overview tab page by choosing

the Insert pushbutton and then Freight Unit or Transportation Unit.

When you add freight units, note that a consignment order can contain only one transportation stage, in other

words, only one source and destination location. If you add freight units that have the same goods supplier, the

system copies this data to the consignment order. If the freight units have different goods suppliers, you can

manually enter the required goods supplier for this consignment order as a business partner. The goods suppliers

and the corresponding source locations of the freight units are automatically adjusted. The predecessor documents,

such as purchase orders, remain unchanged.

You directly enter items to be transported. You do so on the Items tab page by choosing the Insert pushbutton.

You can have the system build packages. For more information, see Unified Package Building in TM.

3. Calculating transportation charges

Optionally, you can have the system calculate the expected transportation charges for your consignment order. They are

displayed on the Charges tab page. For more information, see Charge Calculation.

4. Checking and saving

Once you have entered all the important data, you can check the consistency of the data. You then save your consignment

order.

5. Sending the consignment order

You send the consignment order to your carrier. You do so by choosing Subcontracting and then Send to Carrier. You can

also assign the consignment order to a freight order first and perform subcontracting there.

When you subcontract a consignment order, the system recalculates the charges. If these charges differ from the previously

calculated charges, the system cancels subcontracting. You must then check the charges manually and adjust them, if

necessary. Subsequently, you can resend the consignment order to the carrier. For more information, see Charge

Calculation.

6. Confirming or rejecting the consignment order

You receive a confirmation or rejection of the consignment order from your carrier in the form of electronic messages. If you

have not set up message communication with your carrier, you can also enter this information manually in the system.

7. Printing

Optionally, you can print the corresponding print documents. For more information, see Printing.

8. Fixing the consignment order

You can fix your consignment order to protect it from undesirable changes arising from background processing (planning

runs or carrier selection).

9. Creating a freight settlement document

This is custom documentation. For more information, please visit SAP Help Portal.

129


1/14/26, 2:18 PM

After execution, you can create a freight settlement document (see Freight Settlement Document and Enablement of

Freight Settlement Documents for Creation). This serves as the basis for checking the invoice or issuing a voucher.

You can also perform freight settlement for the freight order after you have assigned the consignment order to it.

10. You assign the consignment order to a freight order. To do this, open the Edit Road Freight Order app on the launchpad.

Then choose the Insert option on the Items tab page. You can insert consignment orders based on the ID, the external ID, or

your selection.

The consignment order is displayed in the document flow of the freight order, from where you can call it up. It is also

displayed in the item hierarchy on the Items tab page of the freight order and on the Overview tab page, where you can

perform further planning steps.

For more information, see Freight Order.

  Note

A possible variant of this process is that you simply enter the general data. You then call the transportation cockpit and assign

freight units to your consignment order. You subsequently perform all additional planning steps in the transportation cockpit

(for example, you have the system calculate the transportation charges). For more information, see Manual Planning and Use of

Consignment Orders in Planning.

Related Information

## Consignment Order

Additional Business Document Attributes in FOM

Automatic Consignment Building

## Automatic Consignment Building

In Transportation Management (TM), you can let the system build consignment orders for freight orders automatically. Based on

rules that you have specified in a profile as well as default rules, freight units of the freight order are grouped into consignment

orders.

## Features

If you want to build consignment orders for an existing freight order that you need for follow-up processes, such as a customs

declaration, you can let the system execute this operation automatically. You can specify that the system first creates the

consignment orders locally in the freight order and creates the corresponding consignment order documents later. The freight

units can be grouped into consignment orders based on a profile in which you have specified the grouping rules for the freight

units. Furthermore, the system applies predefined default rules that belong to the prerequisites of a consignment order in TM (for

example, the rule that the freight units must have the same source and target location).

## Consignment Building Profile

In the consignment building profile, you can select grouping rules for freight units that are already predefined in the system, such

as grouping by loading point or Incoterm. You can also combine several rules. The system then groups only those freight units into

a consignment order that correspond to these rules (for example, freight units that have the same loading point and the same

Incoterm). You can also specify the following in the profile:

You can select your own rules that you have defined in Customizing. For more information, see Customizing for

Transportation Management under  Freight Order Management

 Consignment Order

 Define Grouping Rules for

Automatic Consignment Building .

This is custom documentation. For more information, please visit SAP Help Portal.

130


1/14/26, 2:18 PM

You can specify whether incompatibilities are to be considered as a grouping rule. To do so, enter the name of the settings

that you have defined in the Create Incompatibility Settings app in the Incompatibility Settings field. Note, however, that

you must have selected the Identical Values Only checkbox in your incompatibilities for them to be considered.

You can specify the consignment order type of the consignment orders that are created automatically. The consignment

order type also determines the number range from which the system takes the consignment order number. This number is

then retained consecutively in the system, even if consignment order documents are created later for local consignment

orders.

You can specify whether the system automatically builds consignment orders locally in the freight order or updates only

existing consignment orders. For more information, see Creating Local Consignment Orders below.

You can specify whether the system automatically creates consignment order documents. For more information, see

Creating Consignment Order Documents below.

To create the profile, choose the Create Consignment Building Profile app on the launchpad. The system takes the profile into

account if you enter it in Customizing for the freight order type. For more information, see Customizing for Transportation

Management under  Freight Order Management

## Freight Order Type

 Define Freight Order Types .

## Creating Local Consignment Orders and Consignment Order Documents

You have the following options for automatically building consignment orders locally and creating consignment order documents in

the freight order:

Creating local consignment orders

Manual triggering from the freight order UI

Select the menu option  Follow-Up

 Build Local Consignment Orders  in the Create Freight Order or Edit Freight

Order app. The system then groups the freight units of the freight order into consignment orders based on the

default rules and according to any rules defined in the consignment building profile and creates local consignment

orders with the item type SHP and the item category Consignment Order. The consignment orders are also marked

with the qualifier local in the item hierarchy.

If you do not enter a profile in the freight order type and trigger the automatic building of consignment orders

manually from the UI of the freight order, the system applies only the default rules and uses the consignment order

type.

## Automatic building when the freight order is created and saved

In the Automatic Building field of the consignment building profile, you can specify that the system automatically

builds consignment orders locally when a freight order is created and saved manually or based on an inbound

message.

## Manual triggering with subsequent automatic update

In the Automatic Building field of the profile, you can also specify that although you have to trigger the initial

building of local consignment orders manually on the freight order UI, the update takes place automatically.

Depending on the setting, the system then only updates the local consignment orders for consistency reasons

according to the defined grouping rules, or it updates the consignment orders completely, taking into account newly

added freight units. For more information, see the field help.

The advantage of local consignment orders is that changes can still be made to the freight order after consignment building

that are taken into account when the consignment order documents are generated. The consignment order documents are

then no longer updated with freight order changes. You can, for example, add freight units to the freight order and have the

consignment building executed again. The system then assigns new freight units to the existing consignment orders or, if

this is not possible according to the grouping rules, it groups them into new consignment orders.

Note that the system does not take local consignment orders into account during further planning.

This is custom documentation. For more information, please visit SAP Help Portal.

131


1/14/26, 2:18 PM

## Creating consignment order documents

## Manual triggering of document creation for all consignment orders

If you do not expect any further changes to the freight order and you need the consignment order documents for

follow-up processes, save your freight order data again and choose  Follow-Up

 Create Consignment Order

 to

create the relevant documents for all local consignment orders of the freight order.

Manual triggering of document creation for individual consignment orders

You can select individual local consignment orders from the item hierarchy of the freight order and create

documents only for these consignment orders.

## Automatic document creation based on the profile settings

In the Create Consignment Documents field of the consignment building profile, you can specify that consignment

order documents are created automatically by the system following specific actions, status changes, or events. You

can, for example, specify that the consignment order documents are created automatically when you save the

freight order, when the execution status is set to Ready for Transportation Execution, or when the truck has

departed from the company premises. When the freight order is saved and the execution status is set to Ready for

Transportation Execution, the documents are created for all consignment orders of the freight order. In the case of

events, only the consignment order documents are created for the location for which the event is executed.

However, the prerequisite for this automatic document creation is that the consignment orders have already been

built locally in the freight order. For more information, see the field help.

Related Information

## Consignment Order

Creation and Editing of a Consignment Order

## Consignment Orders for Customer Pick-Up

If your customers want to organize their own pick-up, you as a logistics service provider can create consignment orders for

customer pick-up. When the consignment order is ready for shipping, the customer receives a notification that the freight has been

made available. All transportation planning activities are carried out by the customer.

Consignment orders for pick-up are relevant for consignment orders with Incoterms EXW (Ex Works) and FCA (Free Carrier).

## Prerequisites

You have selected the Advanced stage building variant to consider Incoterm locations 1 and 2 for building stages for freight

units in Customizing for Transportation Management under

## Integration

  Logistics Integration

## Internal TM

## Component Integration

  Define Logistics Integration Profile for SD, MM, and LE . This staging variant includes the use

of statistical stages.

For more information on stage building variants, see Logistics Integration Profile for SD, MM, and LE.

You have selected Relevant for Customer Self-Delivery or Pick-Up in the Self-Delivery/Customer PU field in Customizing

for Transportation Managementunder

 Freight Order Management

 Consignment Order

  Define Consignment Order

Types .

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

132


1/14/26, 2:18 PM

You can only assign freight units with Incoterm EXW or FCA with a statistical stage to freight orders for self-delivery or pick-up or

to consignment orders for customer pick-up.

## Process

The following figure shows how consignment orders for customer pick-up are handled, highlighting the most important process

steps.

1. The consignee sends a purchase order with Incoterm EXW (Ex Works) to the shipper.

This is custom documentation. For more information, please visit SAP Help Portal.

133


1/14/26, 2:18 PM

2. The shipper creates a sales order and a freight unit with one statistical stage.

3. The shipper creates a consignment order with consignment order type Relevant for Customer Self-Delivery or Pick-Up.

4. When warehouse processing is completed, the shipper sets the status Ready for Shipping.

5. An advanced shipping notification is sent to the consignee to inform them that the goods are available for pick-up and how

they are packed.

6. The shipper posts goods movement without any additional checks.

7. The consignee is responsible for all follow-up steps, for example, transportation planning and loading.

## AI-Assisted Goods Receipt Analysis

Automatically check delivery documents using AI technology, reduce manual checks at the gate, and improve operational

efficiency at goods receipt.

  Note

Use of this AI-assisted feature may require additional entitlement and authorization. Please consult your account

executive for more information.

The features described here are only available in SAP S/4HANA Cloud Private Edition.

To onboard AI-Assisted Goods Receipt Analysis, you need to request an SAP Business Technology Platform (SAP BTP)

service key with the intelligent scenario SCMTMS_DOX_DLV_NOTE for the delivery note and SCMTMS_TMDOX for the

shipping document. For more information, see SAP Delivered Document Information Extraction Scenario and

Requesting Access to SAP AI Services on SAP Business Technology Platform (SAP BTP).

In Transportation Management in SAP S/4HANA Cloud Private Edition, you can use Document Information Extraction with

generative AI technology to analyze delivery documents attached to a consignment order, extract their header data, item data and

item reference data, and insert it into a consignment order.

Document Information Extraction helps you to process large numbers of business documents that have content in headers and

tables. You can use the extracted information, for example, to automatically process payables, invoices, or payment notes while

making sure that invoices and payables match. After you upload a document file to the service, it returns the extraction results

from the header fields and line items.

## Related Information

What is Document Information Extraction

Automated Processing of Delivery Document Data

## Working with Attachments

## Automated Processing of Delivery Document Data

Automated extraction of delivery document data using generative AI technology. Reduces manual efforts, compares extracted data

to existing system data, and stores errors for user evaluation and correction. Use to streamline data entry and improve accuracy in

consignment orders.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

134


1/14/26, 2:18 PM

Use of this AI-assisted feature may require additional entitlement and authorization. Please consult your account

executive for more information.

The features described here are only available in SAP S/4HANA Cloud Private Edition.

## Prerequisites

An integration with the Document Information Extraction service was set up using the Intelligent Scenario Lifecycle

Management (ISLM) framework.

For more information, refer to Introduction to Intelligent Scenario Lifecycle Management.

The Delivery Note Extraction – Version 01 extraction schema is assigned to your attachment types for delivery notes in

Customizing for Transportation Management.

The Shipping Document Extraction - Version 01 extraction schema is assigned to your attachment types for shipping

documents in Customizing for Transportation Management.

An automated processing option is set for your attachment types in Customizing for Transportation Management.

For more information, see Customizing for Transportation Management under  Basic Functions

 Document Information

## Extraction

 Assign Extraction Schemas to Attachment Types .

You are using attachments in PDF format or single-page document files in JPEG, PNG, or TIFF format.

## Process

## Overall Process

This is custom documentation. For more information, please visit SAP Help Portal.

135


1/14/26, 2:18 PM

In SAP S/4HANA Cloud Private Edition, you scan and upload your delivery documents to a consignment order, for example, as PDF

documents. If you created a consignment order based on an advanced shipping notification (ASN), it might already have the

delivery documents attached. You send your attachments to the extraction service. In the background, the following is created: a

trigger_data entry containing an extraction job ID and a processing status, and a bgRFC trigger to check the processing status

of the extraction result in predefined intervals. You monitor the processing status in Document Information Extraction directly.

Since Document Information Extraction doesn't send any success messages, you retrieve your extraction results by refreshing the

consignment order. The system compares the extracted data to any existing data for your consignment order. Based on the

extraction and comparison results, the data is filled into your consignment order.

## Document Errors

During the process, you might run into errors. You can view and resolve any document errors related to this process on the

Document Errors tab of the consignment order. Depending on the error solution, you can continue with the consignment order

data or with the extracted data. You must resolve all document errors before the system can determine the correct requirement

documents to continue.

  Note

If there are critical document errors for your consignment order before you start the data extraction, for example, master data

errors or reference errors, your attachments can't be automatically sent for data extraction.

For more information on document errors related to the extraction and comparison of data, refer to Error Handling.

For general information on document errors, refer to Correction of Errors in Business Documents.

## Example

The following is an example of how to automatically process data from delivery documents that are attached to consignment

orders.

1. You scan a delivery document and attach it as PDF document to a consignment order.

2. You submit your attachment to the extraction service using the Extract Attachment Data function.

In the confirmation dialog box you confirm that you want to save the consignment order to continue. Your consignment

order is blocked for planning.

  Note

You can disable the confirmation dialog box if this better suits your needs. To do this, set the user

parameter /SCMTMS/DOX_AUT_SAVE to X. If you disable the confirmation dialog box, the consignment order is

automatically saved when you submit your attachments to the extraction service.

3. Document Information Extraction receives the data from the attachment and starts the extraction.

4. While the extraction is running, you check the processing status in Document Information Extraction.

In the system, you use the Check function to see whether there are any unprocessed triggers for extraction.

5. You refresh the consignment order and see that the extraction is done.

6. The system retrieves the extracted data and enters it in your consignment order.

Subsequently, several checks are run, for example, for missing master data. Depending on the check results, processing

document errors might be created.

7. The extracted data is compared to the data in the system.

This is custom documentation. For more information, please visit SAP Help Portal.

136


1/14/26, 2:18 PM

You are notified that a document error is created because of an item mismatch. You view the error message on the

Document Error tab.

The data comparison results show that one of the items in the consignment order is missing in the extracted data. You

check the information in the attachment and see that there was a typo in the corresponding item in the delivery document.

Because of the typo, the extraction service couldn't read the data correctly. On the Document Error tab, you choose Delete

to delete the error and continue with the consignment data.

8. The processing block for the consignment order is removed.

9. The system determines the correct requirement documents based on the extracted data.

## Related Information

What is Document Information Extraction

AI-Assisted Goods Receipt Analysis

## Error Handling

Correction of Errors in Business Documents

Working with Attachments

## Error Handling

Learn how to monitor and resolve document errors related to the extraction and comparison of delivery document data. This topic

provides examples of errors and how to handle them, ensuring smooth processing and accurate data comparison. Use it to

troubleshoot and resolve errors efficiently.

You can monitor and resolve document errors related to the data extraction and comparison of attachment data in the Document

Errors tab of your consignment order. The following are examples of errors that might occur and how to handle them.

## Connection Errors

If the connection to Document Information Extraction can't be established when you are submitting an attachment for extraction

or retrieving the extraction results, you receive an error message. The service might be temporarily unavailable or there might be

authorization issues. Try the extraction again later. If the problem persists, contact SAP Support.

For more information, refer to Monitoring and Troubleshooting in Document Information Extraction in the Related Information

section below.

## Extraction Errors

It may happen that the extraction job fails. There might be technical problems or the data in your attachment might be

inconsistent. Check that the file format of the attachment complies with the formatting requirements and make sure the

information you want to extract is included in the attachment.

For more information on file format requirements, refer to Supported Document Types and File Formats in the Related

Information section below.

## Processing Errors

Even when the extraction runs technically successful, some of the data may not be identified correctly by the document extraction

service, or there might be errors such as typos on the printed document. If the extraction results contain wrong, incomplete, or

unknown data, the system creates a document error.

This is custom documentation. For more information, please visit SAP Help Portal.

137


1/14/26, 2:18 PM

If the extraction results, for example, contain an unknown material, unit of measure, or business partner, you can manually correct

these values. A help text for document errors is displayed when you choose Error Details. It gives you more information on how you

can correct the error.

Data Comparison Errors

## Item Mismatch

During data comparison, the items of the consignment order and the data extracted from the delivery document are compared

based on the following criteria:

## Product ID

Purchase order reference

External delivery note reference

## External delivery note's item ID

Sometimes, the number of items in the consignment order might not match the extracted data, there might be items present in

the consignment order that are not in the extracted data or the other way around. It could also be that the individual items are not

the same. In both cases, you can choose to continue either with the consignment order data or with the extracted data.

## Quantity Mismatch

In the consignment order, items with the same product ID, purchase order reference, and external delivery reference are

aggregated. The sum of the aggregated items is compared to the quantity extracted from the attachment. All aggregated items are

displayed under a quantity mismatch document error.

If the item quantity in the consignment order doesn't match the item quantity in the extracted data, you can either continue with

the consignment order data or manually adjust the quantity in the consignment order to match the extracted data. The error is

removed as soon as the quantities match.

## Header Data Mismatch

If the extracted data contains different header data than the consignment order, the system doesn't start the comparison of the

items. In this case, make sure the correct attachment was uploaded, and manually check the data in the consignment order and in

the attachment.

If you find that, for example, a wrong attachment was uploaded, you can simply delete the error and start a new analysis with the

correct attachment. If you want to run the comparison with the current attachment regardless of the header data mismatches, you

can also do so from the Document Errors tab.

## Related Information

Monitoring and Troubleshooting in Document Information Extraction

Supported Document Types and File Formats in Document Information Extraction

Creation of Consignment Order Item Hierarchy Using Document
## Information Extraction

When you create a consignment order through Document Information Extraction, the unified package building function

automatically generates the item hierarchy and corresponding quantities of packaged items and products.

This is custom documentation. For more information, please visit SAP Help Portal.

138


1/14/26, 2:18 PM
## Example

The shipping document includes 5 units of product A and 1 unit of packaging material B. In the unified package building engine, 5
units of product A are packaged in 1 unit of packaging material B. The consignment order will create items from the shipping
document as follows:

Packaging Material B: 1

Product A: 5

## Worklist

In the Consignment Order Worklist app, the Comparison Status determines the overall comparison status between document

data and consignment order data.

The Comparion Status includes the follwing 4 status values:

## Not Started

Check in Progress

Check Completed

Manual Completed

Related Information

Unified Package Building

## Unified Package Building Engines

## Application Log for Document Information Extraction

You can use this function to collect messages, exceptions, and errors that occur during the intelligent processing of the document.

## Enable Log

To enable the Document Information Extraction functionality for log monitoring in Transportation Management (TM), follow these

steps:

Open the SAP system and access transaction code SU3.

In the Parameter tab, add /SCMTMS/DOX_LOG and set its value to X.

## Check Log

To enable and monitor logs for the Document Information Extraction function in Transportation Management (TM), follow these

steps:

After processing delivery documents through AI-Assisted Goods Receipt Analysis, the system created a log in the application log.

1. Open transaction code SLG1 in the SAP system.

2. Enter the following details:

## Object: /SCMTMS/GENAI

This is custom documentation. For more information, please visit SAP Help Portal.

139


1/14/26, 2:18 PM

## Sub Object: TMDOX

Other optional conditions, such as username

3. Execute the query.

## Additional Business Document Attributes in FOM

The following documents list additional attributes and functions that are available in the business documents of freight order

management:

## Items

## Transportation Stops

Dates/Times in Freight Order Management

Quantities and Capacities

Cargo Management

Goods Information

Carrier Categorization

Use of Schedules

## Use of Seals

Use of Hierarchical Views in FOM

Use of Customer Numbers

Statuses of Business Documents

Blocking Information

Items

## Use

In freight order management, you can enter items in your business documents.

  Note

You cannot change items that are transferred from business documents in forwarding order management. For more

information about creating items in forwarding order management, see Creation of Forwarding Order Items or Forwarding

Quotation Items.

## Features

With the exception of containers, items represent either capacity or demand.

## Capacity

## Vehicle resource

This is custom documentation. For more information, please visit SAP Help Portal.

140


1/14/26, 2:18 PM

You can enter the vehicle ID, the country of registration, and the registration number.

Passive vehicle resource (for example, trailer or railcar)

For trailers, you can enter the trailer ID, the country of registration, and the registration number.

## Container

You can enter the number of containers, the capacity, and the equipment group and type.

Demand

## Container

You can enter the container ID and seal, as well as information about the container such as the ventilation or

humidity.

Package (for example, pallet)

You can enter the package ID. You can also enter the external package ID if it is available. You can also specify

whether the transport involves overdimensional cargo or non-stackable packages.

## Packaging material

Auxiliary packaging material

## Product

You can enter the product ID, the product freight group, and the transportation group.

You can enter the following information for all demand items:

Content identification

## Quantities

Customs and dangerous goods information

Document references and notes

Commodity codes

## Discrepancies

Each business document can contain only one main item but any number of subitems. Railcar units and container units are an

exception. They can have several main items. The item hierarchy determines which item can be loaded into which other item. For

example, you cannot load a trailer unit or railcar unit into a package.

Items are displayed on the user interface in the following locations:

Cargo and Cargo Management

Demand items are displayed here.

## Equipment

Capacity items are displayed here.

## Overview

All items are displayed here.

## Stages

This is custom documentation. For more information, please visit SAP Help Portal.

141


1/14/26, 2:18 PM

The locations in which items are loaded and unloaded are displayed here.

For more information about weights and quantities, see Quantities and Capacities.

For more information about transportation stops, see Transportation Stops.

## Item Types

You can define item types in Customizing. The item type enables you to predefine various parameters for an item, for example,

whether the item is a multi-item. For more information, see Customizing for Transportation Management under  Freight Order

## Management

 Define Item Types for Freight Order Management

.

By assigning an item type to a document type (such as a freight order type), you can specify which item types are valid for the

document type. You can also define a default item type.

You can create a condition to determine item types for specific items of a business document. You can assign a different text

schema to each of these item types. For more information, see Text Collection.

For more information, see Customizing for Transportation Management under:

Freight Order Management

## Freight Order

 Define Freight Order Types

Freight Order Management

## Freight Booking

 Define Freight Booking Types

Planning

## Freight Unit

 Define Freight Unit Types

Freight Order Management

## Transportation Unit

 Define Transportation Unit Types

Freight Order Management

## Consignment Order

 Define Consignment Order Types

## Multi-Items

You can define multi-items for the following item categories:

Passive vehicle resource

Product

Package

## Container

In the case of rail freight orders and railcar units, you use multi-items to model the following objects:

## Multiple railcars of the same category

In this case, you define the main item as a multi-item in your railcar unit. This enables you to define the railcars and the

cargo item assignment approximately. (Alternatively, you can assign the cargo items to the individual railcars.) You can then

assign passive vehicle resources to the multi-item as subitems. These represent the individual railcars and can be used, for

example, to assign a seal.

## Multiple locomotives in a train

In this case, you define the main item as a multi-item in your rail freight order. You can then assign the vehicle positions to

the multi-item as subitems that represent the individual locomotives. Note that during planning, the system considers only

the main locomotive that you have specified at header level. The other locomotives are not taken into account during

scheduling or when considering incompatibilities.

This is custom documentation. For more information, please visit SAP Help Portal.

142


1/14/26, 2:18 PM

In the case of packages, you use multi-items when you have to define the exact position of each lower-level item in your truck

during load planning, for example. For more information about load planning, see Load Planning.

You specify whether an item is to be a multi-item in Customizing when you define the item type. You can also specify whether

subitems are to be generated automatically (or expanded) as soon as you enter a multi-item in a business document. You can

select the items types from Customizing on the user interface. For more information, see Customizing for Transportation

Management under  Freight Order Management

 Define Item Types for Freight Order Management

.

For more information about creating multi-items in rail freight orders, see Scheduling of Freight Orders.

## Related Information

Use of Auxiliary Packaging Materials

## Use of Auxiliary Packaging Materials

You can also use auxiliary packaging materials in the business documents of Transportation Management (TM), such as freight

orders and consignment orders. Auxiliary packaging materials include lining in cartons, foil, protective paper, and pallets used to

secure the load, for example.

## Prerequisites

The packaging material type Auxiliary Packaging Material has been defined in the material master data. You have made the

following settings in Customizing for Transportation Management to be able to use this packaging material type in TM:

You have assigned a packaging material category to the packaging material type in the product master data. Only the

packaging material categories Packaging Materials (C) and Auxiliary Packaging Material (D) can be assigned to auxiliary

packaging materials.

For more information, see Customizing for Transportation Management under  Master Data

## Product

 Define Packaging

Material Types .

You have defined an item type and assigned the item category Auxiliary Packaging Material to it. In the item type, you can

also specify that for items in the business document the system checks whether you have entered a valid packaging

material or auxiliary packaging material. You can then define this item type as an allowed item type for your freight order

type or consignment order type.

For more information, see Customizing for Transportation Management under  Freight Order Management

## Define Item

Types for Freight Order Management

.

If you have defined your own item hierarchy in Customizing, you have added the auxiliary packaging material to this

hierarchy under Hierarchy Levels. The auxiliary packaging material is already contained in the standard item hierarchy All

Items (ITEM).

For more information, see Customizing for Transportation Management under  Freight Order Management

## Define

Hierarchical Views for Business Documents .

## Features

You can add auxiliary packaging materials to the item hierarchy of a business document manually or transfer these automatically

using EDI messages, such as an advanced shipping notification. In addition, items for auxiliary packaging materials can be

automatically created under package items during package building. Note, however, that auxiliary packaging materials must always

be created as the lowest item in an item hierarchy, meaning that no further items may be assigned below the auxiliary packaging

material. Since auxiliary packaging materials do not have their own capacity, they cannot contain any further items.

This is custom documentation. For more information, please visit SAP Help Portal.

143


1/14/26, 2:18 PM

If the auxiliary packaging material is a main item, it is considered during load planning.

The packaging material type and packaging material category are displayed in the detailed information for the auxiliary packaging

material items in the business documents.

Auxiliary packaging materials are also taken into account when integrating TM with Extended Warehouse Management (EWM).

When EWM deliveries are created by the system, the related handling units also contain the auxiliary packaging materials. For more

information, see Advanced Shipping and Receiving.

Related Information

## Items

Defining Auxiliary Packaging Materials

Transportation Stops

## Definition

For a business document in freight order management (in other words freight order, freight booking, freight unit, and

transportation unit), a transportation stop describes the following:

An action that is performed at a particular location

## The time at which this action is performed

Each business document includes at least two transportation stops.

The sequence of transportation stops is defined solely using the stop successor.

The stop successor is a subnode of a transportation stop.

The stop successor can be viewed as a transportation stage.

## Current Transportation Stop

The current transportation stop is the stop where you are working at a particular time. In freight order management, the concept of

the current transportation stop supports multi-pickup and multi-delivery scenarios.

  Example

You have created a freight order for a multi-pickup going from A to B to C. Goods are to be loaded at A and B. Goods are to be

unloaded at B and C.

In the course of transportation planning, the system views A, B, and then C as the current transportation stop:

First, A is the current transporation stop.

After you have reported that the truck has left A, the system views the inbound stop at B as the current transportation

stop, as the unloading at B will be the next activity.

After you have reported the end of unloading, the outbound stop at B becomes the current transportation stop.

After you have reported that the truck has left B, the system views the inbound stop at C as the current stop.

This is custom documentation. For more information, please visit SAP Help Portal.

144


1/14/26, 2:18 PM

If there were additional transportation stops, the system would view them one after the other as the current

transportation stop.

The concept of the current transportation stop has the following consequences:

## Items tab page

On this tab page, the current transportation stop is displayed. In the Change Hierarchy field, you can choose between the

following views:

Display cargo that is only relevant for the current transportation stop

Display cargo that is relevant for all transportation stops

  Note
The Items tab page replaces the Cargo Management tab page in the freight order and in the ocean freight booking. You

can personalize your user interface in such a way that the system displays the old tab page.

This information is displayed on the Capacity and Cargo tab page in the air freight booking. This information is

displayed on the Cargo tab page in the transportation unit (trailer unit, railcar unit, and container unit).

## Execution activities

If, for example, you set a freight order to Departed at header level, the system automatically triggers the departure event for

the current transportation stop.

## Structure

The transportation stop comprises the following data:

Stop ID

## Stop type

Each intermediate stop has an inbound and an outbound stop.

Stop role, for example standard stop or freight unit stop

## Fixing

Information about whether the stop can be used as capacity

Location data, in other words logistical location and address

Times, for example pickup and delivery times, planned transportation times, appointments

For more information, see Dates/Times in Freight Order Management.

## Assignment to capacity

For freight units, trailer units, and railcar units, the assignment to resources and freight documents is displayed in the

transportation stop.

Dates/Times in Freight Order Management

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

145


1/14/26, 2:18 PM

The table below contains an overview and explanation of all the dates/times used in freight order management. Since the names of

dates/times may vary on the user interfaces, only examples are used here.

## Dates/Times

Acceptable dates/times

Requested dates/times

Appointment

## Meaning

Time window for pick-up at the customer and time window for

delivery at the customer. For more information, see Time Windows.

Time window for pick-up at the customer and time window for

delivery at the customer. For more information, see Time Windows.

Time window for pick-up at the customer and time window for

delivery at the customer (in the freight order, for example). For

more information, see Appointment.

## Planned departure and arrival dates/times

Planned departure date/time and planned arrival date/time. For

## Loading/coupling times

example, in the freight order this is the departure date/time at the

source location and the arrival date/time at the destination

location.

Time window for loading and time window for unloading or time

window for coupling and time window for uncoupling. In the freight

unit these are the loading and unloading dates/times. In the trailer

unit these are the coupling and uncoupling dates/times.

Loading times (cargo)

Time window for loading and time window for unloading the

assigned cargo (in a freight order, for example).

Coupling times (trailer/railcar)

Time window for coupling and time window for uncoupling the

trailers or railcars assigned in the freight order or in the rail freight

order.

## Times for preparation and finalization

Time window for the preparation and finalization of a loading or

Cut-off dates/times

## Availability dates/times

unloading process, such as the checking, refueling or cleaning of

the truck, the completion of the required documents, and so on.

The latest date/time by which cargo or documents have to be

accepted. In an ocean freight booking, for example, this is the

date/time by which the cargo has to be delivered to the port of

loading.

The earliest date/time as of which cargo or documents have to be

available. In an ocean freight booking, for example, this is the

earliest date/time as of which the cargo is available at the port of

discharge.

## Dates/times confirmed by carrier

An appointment confirmed by the carrier. For example, the start

and end date confirmed by the carrier are displayed in the road

freight order.

More Information

## Transportation Stops

## Deviating Business Partner Addresses

You can change the address data of your business partners in your business documents.

This is custom documentation. For more information, please visit SAP Help Portal.

146


1/14/26, 2:18 PM
## Use

This overwrites the address data that you entered for the business partner in the master data and that was copied automatically to

the business document.

You can use this function in the following business situations:

You entered only very general address data for your business partner. You then change this data in the document and enter

more specific address data, such as the telephone number.

If you are using one-time customers, you must enter a deviating address in the document.

If you always communicate with a specific contact person, you can overwrite the address data copied from the master data

with the address data for this contact person. This is possible either for the entire document or for individual items.

This function is available for the following business documents in freight order management and forwarding order management:

Forwarding orders

Freight orders

Freight bookings

Transportation units

Freight units

## Features

You can change the following address data:

## Name

## Address

Telephone number and cell phone number

E-mail address

Fax number

## Propagation

Deviating business partner addresses are propagated in the forwarding order from the header level to the items. They are also

propagated from the forwarding order items to the freight unit items and transportation unit items and then to the freight order

items or freight booking items.

Deviating business partner addresses are aggregated in the freight order and in the freight booking from the items at header level,

provided the following prerequisites are met:

In the Shipper/Consignee Determination Rule field in the freight order type or freight booking type, you have selected the

option Determination Based on Predecessor Documents.

The shipper ID or consignee ID (or both) are identical for all items.

The business partners and address data are identical for all items.

You can overwrite the aggregated address data for shippers and consignees in the freight order and in the freight booking at

header level.

This is custom documentation. For more information, please visit SAP Help Portal.

147


1/14/26, 2:18 PM

If you overwrite address data that deviates from the master data again in a forwarding order item, these changes are propagated to

the follow-up documents. However, the shipper and consignee are not determined again.

Deviating business partner addresses are also displayed in the stage-based lists for requirement documents in the transportation

cockpit.

## Print Documents

Deviating business partner addresses are also included in print documents. The address to be printed is displayed on the Printing

Address tab page for each business partner in the forwarding order. You can also see where this address comes from. For example,

this may be the address that you entered in the business partner master data or it may be a deviating address that you entered at

header level in the forwarding order.

You can overwrite this address.

## Activities

To enter a deviating business partner address in the forwarding order, select the Deviating Address checkbox on the Business

Partner tab page. The address data fields for the business partner are then ready for input. A change symbol also appears in the

Actions field. When you select this, a dialog box appears in which you can also change the required address data.

By selecting the corresponding symbol in the Actions field you can call the contact person directly from the system or send an e-

mail, for example.

If you want to enter a deviating address at item level in the forwarding order, select the option Manual Entry in the Origin of Entry

field. The relevant fields are then ready for input.

If you want to change the aggregated address data for the shipper or consignee or for the business partner at header level in the

freight order or freight booking, select the option Manual Entry in the Origin of Entry field. The relevant fields are then ready for

input.

## International Address Versions

You can display and maintain international address versions in Transportation Management (TM).

## Features

In the General Data tab for freight orders, freight bookings, freight units, consignment orders, and transportation units, you can

display international address versions in a dialog box. The international address version is a version of the location address entered

in a different character set, for example, Kanji characters or Latin letters.

You can see the international address version for the source and destination location on the Stages tab of these business

documents. If an international address version has been entered for a business partner, you can see it on the Business Partner tab,

in the Actions column. It is visible as a globe icon that you can select to view the international address versions dialog box.

For more information about international address versions in Business Address Services, see International Address Versions.

## Activities

To enable the use of international address versions, you need to activate this in Customizing for Flexible Real Estate Management

(RE-FX). Go to  Address Management

## International Settings

 Activate International Address Versions - Cross-Client

 or

Activate International Address Versions - Client-Specific.

This is custom documentation. For more information, please visit SAP Help Portal.

148


1/14/26, 2:18 PM

You can maintain international address versions in the following apps:

## Define Business Partner

In the Address tab, you can enter or update international address versions by selecting the button International Versions.

## Define Location

In the Address tab, you can enter or update international address versions by selecting the button International Versions.

You can enter addresses in multiple international versions, for example, Arabic and Hebrew.

You can also enter an international address when creating a sales order or purchase order, by selecting Business Partner Master

Data and navigating to the Address tab and then International Versions.

## Transportation Distance and Transportation Duration

You can enter the transportation distance and transportation duration manually in the business documents in freight order

management or let the system determine this information. For more information about this determination, see Determination of

Transportation Distance and Transportation Duration.

The transportation distance and transportation duration are displayed at header level and at transportation stage level. The

following table shows which fields are displayed at which level:

## Field

Distance

## Level

## Definition

Transportation stage level

The distance between two transportation

stops.

## Net duration

## Transportation stage level

The actual travel time, in other words the

Total distance

Header level

Total net duration

Header level

Gross duration

## Header level

time needed by the vehicle resource, a truck

or ship for example, to get from one

transportation stop to the next. The system

does not include activities, such as loading

and unloading, coupling and uncoupling, or

driving and rest periods. For this reason,

this duration is a theoretical value.

The sum of the distances of all

transportation stages.

The sum of the net durations of all

transportation stages.

The duration between the first activity at

the first transportation stop and the last

activity at the last transportation stop in the

business document. The system includes

only scheduled dates.

## Display Format

In the standard system, the transportation distance is displayed in kilometers. You can select a different unit of measure in the

display settings. You can also indicate in the display settings in which format durations are to be displayed. For more information,

see Display Settings.

This is custom documentation. For more information, please visit SAP Help Portal.

149


1/14/26, 2:18 PM

Determination of Transportation Distance and Transportation
Duration

## Use

The distance and duration determination (DDD) function is used to determine the transportation distance and transportation

duration in freight order management. The system runs this function based on your selected business document type

automatically for the transportation stages in the following business documents:

Freight orders

Freight bookings

Transportation units

Freight units

## Prerequisites

In the standard system, the determination of transportation distance and duration is activated for the following business

documents:

## Freight orders

Ocean freight bookings for multi-pickups and multi-deliveries

## Transportation units

For all other business documents, you have to activate this function in the corresponding business document type. For more

information, see Customizing under:

Freight Order Management

## Freight Order

 Define Freight Order Types

Freight Order Management

## Freight Booking

 Define Freight Booking Types

Freight Order Management

## Transportation Unit

 Define Transportation Unit Types

Planning

## Freight Unit

 Define Freight Unit Types

## Features

The system runs this function automatically if you make one of the following changes in one of these business documents:

Change a location or means of transport

## Add a transportation stage

You can also manually trigger this function on the user interfaces for the business documents for one or more transportation

stages. For example, this makes sense in the following cases:

You want to perform the determination again.

You have switched the geographical information system.

You can also manually trigger the determination of transportation distance and transportation duration for one or more

transportation stages in the transportation cockpit, but only for freight units and transportation units.

This is custom documentation. For more information, please visit SAP Help Portal.

150


1/14/26, 2:18 PM

## Interaction with Default Route and Schedule

If you have entered a default route for one of the abovementioned business documents or have assigned a schedule to it, the

system copies the transportation distance and duration from the default route or schedule. If the data is incomplete or you make

one of the abovementioned changes to the business document, the system runs the distance and duration determination function

automatically. Depending on the situation, it does this as follows:

## Locations are not identical or the default route contains a transportation zone

If the locations in the business document and in the default route or schedule are not identical, the system ignores the

transportation distance and duration from the default route or schedule and overwrites these values in the business

document with the values from the distance and duration determination function. If a transportation zone has been defined

for a transportation stage in the default route to a transportation stop, the system runs the distance and duration

determination function for the resulting transportation stages in the business document and overwrites the values in the

business document.

## Transportation distance or duration is identical

If a transportation distance or duration has been defined in the default route or schedule and this is identical to the value in

the business document, the system does not run the distance and duration determination function. The value copied from

the default route or schedule into the business document remains unchanged. In this case, you can trigger the distance and

duration determination function manually.

## Default route or schedule do not contain any values

If neither the transportation distance or the transportation duration have been defined in the default route or schedule, the

system copies the values from the distance and duration determination function.

The system copies the values from the sequence of stops to the default route and it copies the values from the departure locations

(transportation stops) to the schedule. If both a default route has been entered and a schedule has been assigned, the schedule

takes priority.

  Note

The transportation duration in the schedule and in the default route corresponds to the net duration in the business

documents.

## More Information

Transportation Distance and Transportation Duration

Distance and Duration Determination (DDD)

Quantities and Capacities

## Use

The following describes how quantities and capacities are used in freight documents such as freight orders, freight bookings, and
consignment orders. Quantities include weights.

Features

## Quantities

This is custom documentation. For more information, please visit SAP Help Portal.

151


1/14/26, 2:18 PM

The system copies planned quantities from the predecessor document, for example, a forwarding order, to your freight documents.

You can enter actual quantities manually in your freight documents. In the following cases, the system adds the actual quantities

automatically:

## If you set a business document item to Quantity Received as Planned

Direct integration with Extended Warehouse Management (see Integration Based on EWM Transportation Units and Transit

Warehousing)

## Integration with SAP Event Management

The table below illustrates how the system totals the quantities:

## Level

Gross Weight

Gross Volume

Net Weight

Number of

Tare Weight

Tare Volume

Outer Volume

Pieces

Booking

(Header)

N/A

N/A

Weight of all

Total number

N/A

N/A

containers,

of containers

products and

packages

Outer volume

of all main

package items

Container

Weight of all

Volume of

Weight of all

Number of

packages and

container

packages and

containers

Weight of

container

N/A

N/A

products in

this container

plus the

weight of the

container

products in

this container

## Package

Weight of all

Volume of

Weight of all

N/A

packages and

package

products and

Weight of

package

Volume of

Outer volume

package

of package

products in

this package

plus the

weight of the

package

Weight of

product

## Product

packages in

this package

Volume of

N/A

Number of

N/A

N/A

N/A

product

products

The gross weight is made up of the net weight and the tare weight. The net weight corresponds to the gross weight of the

underlying item.

For air freight bookings, the system does not take into account the tare weight when it calculates the gross weight.

For more information about outer volume, see Outer Volume.

The total number of TEUs is displayed in the header level of the posting.

The totaling takes place from item level to header level. For more information about totaling, see Example of Quantity Totaling.

You can enter discrepancies (see Discrepancies and Events).

You can enter shipper's load and count (SLAC) for freight bookings. For freight bookings with reference to a forwarding order, the

system copies SLAC from the forwarding order. SLAC denotes the total number of pieces of the smallest packaging unit in a

This is custom documentation. For more information, please visit SAP Help Portal.

152


1/14/26, 2:18 PM

container. The system also displays SLAC at container level. The system automatically calculates the total number of pieces of the

largest packaging unit in a container (packages contained).

  Example
A forwarding order comprises 3 pallets, each with 25 boxes. Each box contains 12 plates.

Packages contained: 3 (pallets)

SLAC: 75 (3 x 25 boxes)

You can define an overdelivery tolerance as a percentage for the ordered items in the purchasing document (for example, the

purchase order or scheduling agreement). Depending on the setting you have made in Customizing for the freight order type or

consignment order type, a document error is created if the item quantity of the consignment order or freight order exceeds the

specified overdelivery tolerance. For more information, see Example Checks to Find Errors in Business Documents.

## Capacities

For freight orders, the system copies over the capacities from the vehicle resource that you enter in the freight order (also applies

to passive vehicle resources).

You have the following options for freight postings:

You enter the equipment group and the equipment type. The system uses the corresponding capacities that you defined in

Customizing (see Consideration of Equipment Data During FU Creation).

You specify the number of TEUs.

## Utilization

To calculate the utilization of a freight order, the system compares the planned quantities and actual quantities. The relevant

utilization is displayed at stage level. The maximum utilization of the most critical quantity of the most critical stage is displayed at

header level. If confirmed quantities exist for an item, the system uses these to calculate the utilization.

You can display the utilization of a freight order for each stage and each relevant dimension in the form of a diagram. This function

is also available in the transportation cockpit.

The utilization of a freight posting refers to the number of containers used. A container is classed as used in the following cases:

You have loaded it with goods. It does not matter if the container is full or not.

It is a FCL container (FCL = Full Container Load). This means the customer has already included the container as a FCL

container in the forwarding order.

  Example

A freight posting is made up of five containers. You load three containers with goods. This means the utilization of the freight

posting is 60%.

On header level, the system displays the utilization of all loaded forwarding orders (that is, freight units) with regards to the total

booked capacity for air freight bookings.

## More Information

## Capacities and Utilization in Rail Freight Orders

This is custom documentation. For more information, please visit SAP Help Portal.

153


1/14/26, 2:18 PM

## Example of Quantity Totaling

The following figure shows an example of the totaling of quantities in freight orders and sea freight bookings.

## Quantity totaling

The net weight of the freight booking (380 kg) corresponds with the gross weight of the container (380 kg).

The gross weight of the container (380 kg) is made up of the gross weight of the pallet (180 kg) and the tare weight of the

container (200 kg).

The net weight of the pallet (160 kg) is made up of the gross weight of box A (55 kg) and box B (105 kg).

The net weight of box A (50 kg) is the gross weight of product A (50 kg). Accordingly, the net weight of box B (100 kg) is the gross

weight of product B (100 kg).

The following table gives an overview of the different values:

## Level

Gross Weight

Gross Volume

## Net Weight

Number of Pieces

Tare Weight

Booking (Header)

N/A

Container

380 kg

N/A

N/A

380 kg

180 kg

N/A

1 EA

N/A

200 kg

This is custom documentation. For more information, please visit SAP Help Portal.

154


Gross Weight

Gross Volume

## Net Weight

Number of Pieces

Tare Weight

1/14/26, 2:18 PM

Level

Pallet

Box A

Box B

180 kg

55 kg

105 kg

Product A

50 kg

Product B

100 kg

0.5 m3

N/A

2 m3

2 m3

1 m3

160 kg

50 kg

100 kg

N/A

N/A

N/A

N/A

N/A

34 EA

17 EA

20 kg

5 kg

5 kg

N/A

N/A

The total of the packages (pallets) in the container is 1. Shipper's Load and Count (SLAC) is for both the container and pallet 2.

  Note

For air freight bookings, the system does not take into account the tare weight of the unit load device when totaling the

quantities. If, for example, a unit load device has a tare weight of 100 kg, and you have loaded it with 1 ton, only one ton is taken

into account for totaling the quantities.

Discrepancies and Events

## Use

You can enter the following discrepancies in your business documents in freight order management (freight order, freight booking,

container unit, trailer unit, and railcar unit):

Quantity discrepancies (see Quantity Discrepancies)

Other discrepancies (see Other Discrepancies)

Unplanned events such as delays

## Prerequisites

You have defined discrepancy types in Customizing for Transportation Management. For more information, see Customizing under

Freight Order Management

 Define Discrepancy Profile .

## Features

When you enter discrepancies for a transportation stage, the system automatically adjusts the actual quantities in the documents

of following transportation stages. However, the cargo receipt status for these transportation stages is not displayed, because they

are still not in execution. In addition, the system adjusts the related freight units and displays information about discrepancies in

these freight units.

If there are unresolved discrepancies, the system automatically sets a planning and execution block for the following

transportation stages. In Customizing (Define Discrepancy Profile) as well as in your freight order, freight booking, trailer unit, or

railcar unit, you can select a checkbox to prevent the block from being set:

Execution block or invoicing block for the freight order, freight booking, container unit, trailer unit, or railcar unit

## Planning and execution block for freight units

This is custom documentation. For more information, please visit SAP Help Portal.

155


1/14/26, 2:18 PM

  Note

You can search for forwarding orders that have discrepancies.

If there are any unsolved discrepancies in a document, you cannot set the load plan status to Unload Plan Finalized. If there is a

block on an unsolved discrepancy, no goods receipt may take place.

If you remove a freight unit with a discrepancy from a business document, in other words, if you remove the assignment, the

discrepancy and the block still remain in the freight unit. However, the discrepancy and the block are removed in the business

document.

In a discrepancy profile, you can assign only one discrepancy type for each discrepancy subcategory and stop category. You can

use the stop category to define different behavior for inbound and outbound stops for a discrepancy subcategory of a discrepancy

profile.

The following special features apply to the assignment of discrepancy profiles to document types in Customizing:

If there is no discrepancy profile assigned to the document type and there are no discrepancy profiles in the system

because you have not used them so far (compatibility mode), the system creates the discrepancies according to the

existing discrepancy types.

If there is no discrepancy profile assigned to the document type and there are discrepancy profiles in the system, but they

do not apply to the current document type, the system does not create discrepancies for this document type.

If there is a discrepancy profile assigned to the document type, only discrepancies for the document types assigned to the

discrepancy profile are created.

## More Information

Handling Discrepancies (forwarding order)

## Resolution of Discrepancies

Handling Discrepancies in Transit Warehousing Process (Integration with Extended Warehouse Management)

Quantity Discrepancies

## Use

You can enter quantity discrepancies in the business documents in freight order management.

You can enter discrepancies in the following situations, for example:

The actual quantity, the actual weight, or the actual volume is lower than expected.

The actual quantity, the actual weight, or the actual volume is larger than expected.

You have received unexpected cargo.

For more information about the different quantity discrepancies (such as Missing Cargo or Unexpected Cargo), see Handling

Discrepancies in Transit Warehousing Process.

## Prerequisites

This is custom documentation. For more information, please visit SAP Help Portal.

156


1/14/26, 2:18 PM

If you want to work with tolerances, you have defined a tolerance range in Customizing. For more information, see Customizing for

Transportation Management under  Freight Order Management

 Define Discrepancy Profile .

## Features

If you have received the planned quantity, you set the corresponding business document item to Quantity Received as Planned.

The system adds the actual quantity to the business document item automatically and changes the cargo receipt status to On

Hand.

If there is a quantity discrepancy, however, you enter the actual quantity for the relevant business document item. The system

automatically performs the following steps:

It automatically changes the cargo receipt status to On Hand.

It adjusts the actual quantities in the related freight units.

You can deselect this checkbox if the discrepancy has been resolved.

You can also observe tolerances in your quantity discrepancies. If the quantity discrepancy entered is found within the tolerance

range defined in Customizing, the system does not set a lock for this quantity discrepancy.

The following special features apply to individual discrepancy subcategories:

The discrepancy subcategories Missing Cargo and Unexpected Cargo refer to the number of pieces while the subcategories More

Weight/Volume than Expected and Less Weight/Volume than Expected refer to weight or volume. If there is a discrepancy in the

number of pieces as well as in the weight or volume for the same item, the system creates only one discrepancy for the number of

pieces.

## Activities

You enter quantity discrepancies on the Quantities tab page of the respective business document item.

More Information

Discrepancies and Events

## Other Discrepancies

Handling Discrepancies (forwarding order)

## Resolution of Discrepancies

Handling Discrepancies in Transit Warehousing Process (integration with SAP Extended Warehouse Management)

Other Discrepancies

## Use

You can enter discrepancies in the following situations, for example:

There is a dangerous goods item you have not designated as such.

This is custom documentation. For more information, please visit SAP Help Portal.

157


1/14/26, 2:18 PM

Packaging of an item is damaged.

You have received overdimensional or high-value cargo.

A different equipment type or package type has been used.

For more information about other discrepancies and the discrepancies of attributes (such as Damaged Cargo or Overdimensional

Cargo), see Handling Discrepancies in Transit Warehousing Process.

## Prerequisites

You have defined discrepancy types in Customizing for Transportation Management. For more information, see Customizing under

Freight Order Management

 Define Discrepancy Profile .

## Features

You enter a discrepancy by making entries including the following:

## Discrepancy type

Discrepancy subcategory (optional)

## Discrepancy date

Notes and attachments (optional)

Or you can enter a discrepancy by selecting the item and choosing Report Discrepancies. The system creates a discrepancy with

the standard discrepancy type and discrepancy subcategory that you specified in Customizing.

You can enter more than one discrepancy for an item. The discrepancies are displayed in the discrepancy log of the item.

## Activities

You enter discrepancies on the Discrepancies tab page of the respective business document item.

More Information

Discrepancies and Events

## Quantity Discrepancies

Handling Discrepancies (forwarding order)

## Resolution of Discrepancies

Handling Discrepancies in Transit Warehousing Process (integration with SAP Extended Warehouse Management)

Resolution of Discrepancies

## Use

You can resolve discrepancies and undo the resolution of discrepancies.

This is custom documentation. For more information, please visit SAP Help Portal.

158


1/14/26, 2:18 PM
## Prerequisites

You have defined discrepancy types in Customizing for Transportation Management. For more information, see Customizing under

Freight Order Management

 Define Discrepancy Profile .

## Activities

You can resolve discrepancies on the Discrepancy tab page for a forwarding or freight order as follows:

If you want to resolve a discrepancy, choose  Resolve

 Resolve Discrepancy .

If you split the freight units for missing cargo and keep the split items but want to remove them from the freight order so

that they can be redelivered at a later date, choose  Resolve

 Resolve (Retain Missing Cargo)

.

If you want to split the freight units for missing cargo and delete the split items, choose  Resolve

 Resolve (Delete

Missing Cargo)

.

If you have received unexpected cargo that does not have an item and is not assigned to a freight unit in the forwarding

order, choose  Resolve

 Resolve Unexpected Cargo (Assign FWO Item)

.

If you have received unexpected cargo and this already has an item and is assigned to a freight unit in the forwarding order,

choose  Resolve

 Resolve Discrepancy .

If you have resolved a discrepancy by mistake and want to undo this, choose Undo Resolve.

If you have entered a discrepancy by mistake, choose Delete.

More Information

Discrepancies and Events

Quantity Discrepancies

## Other Discrepancies

Handling Discrepancies (forwarding order)

Handling Discrepancies in Transit Warehousing Process (integration with SAP Extended Warehouse Management)

## Outer Volume

The outer volume specifies how much space a package (for example, a pallet or a carton) consumes on a capacity (for example, a

truck).

## Use

The outer volume is determined and taken into account for package items only. It is calculated automatically in the following cases:

During package building (see Unified Package Building in TM)

## During the manual creation of package units

If you create a package item and specify a packaging material for which you have entered a tare volume in the product

master, the system automatically calculates the outer volume. In the case of open packaging, the outer volume consists of

This is custom documentation. For more information, please visit SAP Help Portal.

159


1/14/26, 2:18 PM

the tare volume of the packaging material and the gross volume of the package. When the packaging is closed (such as

pallet cages), the outer volume always corresponds to the tare volume.

  Note

You indicate in the product master whether the packaging material is closed (under  Sales: General/Plant

 Closed ).

The gross volume corresponds to the outer volume of the underlying items. If the outer volume of individual

underlying items is not available, the gross volume is used for these items instead.

The outer volume is also taken into account in VSR optimization and scheduling.

## Display of Outer Volume

The outer volume is displayed in the package unit on the Items tab page.

The system adds the outer volume of the main package items and displays it as the outer volume at header level (on the General

Data tab page under  Required Capacity

 Outer Volume ). This value corresponds to the minimum space required by the

package depending on how the package items are arranged on the level above (for example, in the container or on the truck). The

capacity that you can load on the package is displayed under  General Data

 Package Capacity . These values (weight and

volume) are the sum of the capacities of all lower-level packages (main package items). These are displayed for each package item

on the Details tab page under Capacity (Maximum Payload Weight and Cubic Capacity). These values originate from the product

master (under  Sales: General/Plant

## Packaging Material Data

 Allowed Pkg. Weight/Allowed Pkg. Volume ).

The outer volume is also displayed in the following list and hierarchies in the transportation cockpit:

Package unit list and package unit hierarchy

Package unit stage list and package unit stage hierarchy

Freight unit stage list and freight unit stage hierarchy

Combined list and hierarchy for freight unit stages and package unit stages

## Utilization

In Transportation Management (TM) you can display in capacity documents, such as freight orders and transportation units, the

utilization of the capacities belonging to a document. On a dedicated tab page, you can view the detailed calculation of the

utilization for the document based on the individual capacities.

## Prerequisites

In Customizing you have defined equipment types and groups as well as capacities. For more information, see Customizing

for Transportation Management under  Master Data

## Resources

 Define Equipment Groups and Equipment Types

and see Equipment Groups and Equipment Types.

You have defined vehicle resources and you have adjusted the capacities, if necessary. For more information, see Vehicle

Resource.

You have defined a means-of-transport combination for trucks and trailers, if necessary. For more information, see

Customizing for Transportation Management under  Master Data

## Resources

 Define Means-of-Transport

Combination .

This is custom documentation. For more information, please visit SAP Help Portal.

160


1/14/26, 2:18 PM
## Use

“Utilization” Tab Page

On the Utilization tab page of a capacity document, you can display the utilization of the capacities that exist in the document,

such as vehicle resources, containers, and packages. The utilization is displayed in a hierarchical view for the transportation stages.

The following two default views are available:

## Utilization

The hierarchy contains utilization data for the physical objects, such as vehicle resources, containers, and packages.

## Utilization with complete context

The hierarchy also contains the utilization data for the individual subdocuments, such as containers and package units.

In addition to the default views, you can also define your own hierarchical views. For more information, see Use of Hierarchical

Views in FOM.

In addition to the hierarchical view, you can also display a graphical view of the utilization.

  Note
This tab page is also available in the transportation cockpit, where it is called Utilization Overview.

“General Data” and “Overview” Tab Pages

In a freight order document, the maximum utilization is displayed on the General Data and Overview tab pages in addition to the

Utilization tab page:

## General Data

The maximum utilization for a truck and trailer is displayed separately on this tab page. You can also display the total,

consumed, and remaining capacity for the truck and trailer. Under Capacity you can view the combined data for the truck

and trailer. If you have defined special data for this means-of-transport combination in Customizing, this data is considered.

## Overview

The maximum utilization for the hierarchy levels you have configured is displayed on this tab page.

The maximum utilization for the document is displayed on the General Data tab page of transportation unit documents.

## Calculation of Utilization

The system calculates the utilization using the capacity information and load (for example, the package units and freight units in a

container). The system determines the capacity information from the master data for the vehicle resources and the equipment

data defined for containers in Customizing. In the case of packages, the system considers either the packaging material master

data or the results of package building, if this was carried out (see Unified Package Building in TM).

The following capacity information is displayed on the Utilization tab page for the individual stages and objects (for mass and

volume):

Total capacity

Consumed capacity

## Remaining capacity

This is custom documentation. For more information, please visit SAP Help Portal.

161


1/14/26, 2:18 PM

When it calculates the maximum utilization, the system considers the tare weight of packages and containers as well as the outer

volume of packages. The system determines the outer volume during package building or, if this was not carried out, as the sum of

the volumes of items and packaging. For more information, see Outer Volume.

  Note

Capacity information (the total capacity as well as the consumed and remaining capacity) is displayed in all lists and hierarchies

for capacity documents as well as in the load plan hierarchy.

Cargo Management

## Use

This function enables the following features:

## Distributing Freight Units

You can distribute a freight unit that is to be transported with the same freight order or the same freight booking over

several containers (sea freight booking), unit load devices (air freight booking), compartments (freight order), or packages

(package units). This means that you can use this function to distribute a business document (for example, a forwarding

order) over two containers of the same freight booking. This is a description of the function for containers only; the same

also applies for compartments, unit load devices, and packages in package units.

## Splitting Partial Quantities

You can split partial quantities of freight units that are to be transported with the same freight order or the same freight

booking and distribute them in this way over several containers (sea freight booking), unit load devices (air freight booking),

or compartments (freight order). In other words, you can use this function to distribute partial quantities of items in a

business document (such as a forwarding order) over multiple ULDs of the same freight booking, for example.

## Deleting Items

You can delete items from freight orders and freight bookings.

## Features

## Distributing Freight Units

To distribute a freight unit over two containers for example, you move the items you want from one container to the other by using

drag and drop in the sea freight booking. A symbol shows that the forwarding order is distributed across several containers or sea

freight bookings. This function is available for packages, product and container items, however not for container items that already

exist in the forwarding order.

You can use this function if you get a message from the warehouse saying that a freight unit was loaded into two containers.

However, this is advisable only for LCL orders (LCL = Less Than Container Load) with FCL freight bookings, that is when you have

defined your containers in your sea freight booking. If the system has copied the container from the preceding document, such as

a forwarding order, it is not advisable to use this function. This is the case when the shipper has made a fixed order for a container

in an FCL scenario (FCL = Full Container Load).

If you add a new package or product item to a forwarding order, the system assigns these automatically to the main container in

the sea freight booking. The main container is the container to which the freight unit was originally assigned. If you move the entire

content of the main container to a different container in the sea freight booking, then this automatically becomes the main

container. If a container comprises a package item at top-level and a lower-level product item, you can only move the package item.

If the container only comprises a product item at top level, you can move this.

This is custom documentation. For more information, please visit SAP Help Portal.

162


1/14/26, 2:18 PM

## Splitting Partial Quantities

If you get a message from the warehouse saying that a freight unit did not fit into a unit load device during loading, for example,

and that a partial quantity was therefore loaded to another ULD, you can enter this information into the air freight booking

manually. To do so, change the amount of the relevant item and then move the item to the desired ULD using Drag&Drop. A symbol

shows that the item is distributed across multiple unit load devices. The system does not copy amounts and weights automatically.

You need to adjust them manually.

You can split partial quantities as often as required.

When you enter the actual amounts in a freight order or freight booking, the system updates the actual amounts in the item of the

related freight unit only when you have entered all items in the freight order or freight booking.

After a split, the system does not copy changes to the business document (for example, the forwarding order) to the related freight

bookings.

You can undo the split by moving the split item back to its original position by using Drag&Drop. In this case, the changes to the

business document are copied back to the freight booking automatically.

You cannot delete a split item. In this case, the system splits the related freight unit. The freight unit for the split quantity

automatically receives the status Unplanned.

The splitting of partial quantities plays an important role in transit warehousing, for example. For more information, see Transit

Warehousing.

## Deleting Items

If one or more items (container, package or product item) cannot be transported with a freight order or freight booking, you can

delete these items from the freight order or freight booking. This makes sense when a pallet remains in the container freight

station because the container is full. Here the following situations can arise:

## Items do not belong to a freight unit

In this case, the system deletes the item, all lower-level items and the requirement.

## Items belong to a freight unit

If you delete the highest item, the system deletes the corresponding stage that is assigned to the freight order or the freight

booking.

## Delete individual items of a freight unit

If you do not want to delete all items of a freight unit, the system splits off the items to be deleted and consolidates them in

a new freight unit. The system creates this new freight unit as a copy of the existing freight unit. This means you must

reschedule the new freight unit except for the stage that is assigned to the previous freight order or previous freight

booking.

Constraints:

You are only allowed to delete items of freight units from the top level. If you try to delete a lower-level item, the system

issues an error message.

You can only delete items from freight units that are assigned directly to a freight order or a freight booking. If you plan a

truck with a trailer, you cannot delete any items from the freight order of the truck if these belong to one freight unit that

will be transported on the trailer.

This is custom documentation. For more information, please visit SAP Help Portal.

163


1/14/26, 2:18 PM

If you delete a container that you have created directly in the freight booking, in other words, the container is not an item in the

corresponding forwarding orders, the system moves the items in the container up a level into the freight booking. To be able to

execute the freight booking, you must reassign these items to a container.

The corresponding forwarding order is displayed at item level.

## Activities

A tab page for cargo management is available in the transportation cockpit. Custom hierarchy types for cargo management are

available on the Items tab page in the ocean freight booking and in the freight order. These hierarchy types are available on the

Capacity and Cargo tab page in the air freight booking.

  Note

The Items tab page replaces the Cargo Management and Cargo tab pages. You can personalize your user interface in such a

way that the system displays the old tab pages.

More Information

Mixed Unit Load Device

Mixed Unit Load Device

## Use

In certain situations, it may be necessary to load goods from various air freight bookings for the same flight in a unit load device.

You can use this function to represent this in the air freight booking.

## Features

If you choose the option Cargo Management in your air freight booking on the Capacity and Cargo tab page under Change

Hierarchy, the system displays cargo items only. Here you can define a unit load device as a mixed unit load device (mixed ULD).

On the lower-level tab page Mixed ULD, the system displays all air freight bookings that belong to this mixed unit load device. You

can for example check which quantities from the other air freight bookings were loaded to this unit load device.

You create a mixed unit load device by selecting the Mixed ULD checkbox as described above in the relevant unit load devices in

the associated air freight bookings. The unit load devices must use the same ULD number and the same flight.

If you enter the weight of a unit load device for an associated air freight booking, the system also displays this weight in the other

associated air freight bookings.

You can also create a freight order for pick-up and delivery for all associated air freight bookings (see Pick-up and Delivery Freight

Orders). In this freight order, the checkbox field Mixed Usage indicates that this type of scenario is involved.

Goods Information

## Use

Goods information includes the following:

This is custom documentation. For more information, please visit SAP Help Portal.

164


1/14/26, 2:18 PM

Goods value

## Insurable value

## Goods value for customs

The system copies goods information to the freight booking or freight order from the predecessor document, for example, the

forwarding order. You cannot change goods information in the freight booking or in the freight order.

## Prerequisites

You have defined goods information in the predecessor document.

If the system is to convert currencies, you have defined exchange rates in charge management.

## Features

The system totals goods information from item level to header level, just as it does for quantities (see Quantities and Capacities).

If the checkbox for high-value goods is set for an item, this information is also displayed for the item above it and at header level.

For different currencies, the system proceeds as follows:

If there is a document currency from charge management, the system converts other currencies to the document currency.

If there is no document currency, the system converts the other currencies to one of the currencies used in the document.

Carrier Categorization

## Use

Using this function, you can differentiate between carrier categories and business partners in freight order management.

## Prerequisites

You have defined the following for your business partner:

## Relationships

Standard Carrier Alpha Codes (SCACs) (for freight orders and sea freight bookings only)

Airline codes and MAWB prefixes (for air freight bookings only)

Open the Define Business Partner app on the launchpad.

For more information, see Definition of Business Partners.

In Customizing, you have defined airline codes and assigned MAWB prefixes. For more information, see Customizing for

Transportation Management under  Master Data

## Business Partners

 Define IATA Airline Codes .

## Features

The following functions are available:

SCAC (for freight orders and sea freight bookings only)

This is custom documentation. For more information, please visit SAP Help Portal.

165


1/14/26, 2:18 PM

If you enter an SCAC in your freight order or your sea freight booking, the system automatically determines the related

carrier and vice versa. You can assign an SCAC to several carriers that are related to each other.

  Example
Carrier A (carrier category Carrier) has two subsidiaries (carrier category Subsidiary):

A_US

## A_EU

Moreover, carrier A has an agent AG (carrier category Agent). Carrier A, subsidiaries A_US and A_EU, and agent AG are

related via the following relationships:

Has Subsidiaries/Agents

Is Subsidiary/Agent Of

Due to these assignments, the two subsidiaries and the agent have the same SCAC as carrier A. Agent AG is also

assigned to carrier B. Due to this assignment, agent AG has two SCACs, that is, the SCAC of carrier A and the SCAC of

carrier B.

For more information about using the SCAC in forwarding order management, see Determination of the Route.

Airline code (for air freight bookings only)

If you enter an airline code in your air freight booking, the system automatically determines the related carrier and vice

versa. You can assign an airline code to multiple carriers that are related to each other (see the example under SCAC).

The MAWB prefix is a result of the airline code.

## Communication Party

If you enter a communication party in your freight order or freight booking and choose Send to Carrier (freight order) or

Send Booking (freight booking), the system sends messages to this communication party instead of to the carrier. In

tendering, if you have assigned a communication party to a carrier in the business partner master data, the system sends

messages (for example, B2B messages, e-mails, or text messages) to the contact person of the communication party and

not the contact person of the carrier.

Executing carrier (for freight orders and sea freight bookings only)

You can enter an executing carrier in your freight order or sea freight booking for information purposes. For example, you

can let your NVOCC (non-vessel operating common carrier) know that you want the goods to be transported by a special

carrier.

First carrier (for air freight bookings only)

You can enter a first carrier in your air freight booking for information purposes. The first carrier is the carrier who carries

out the first stage of the main carriage. In the case of an import freight booking, you can enter the last carrier, that is, the

carrier responsible for the last stage of the main carriage. For more information, see Manual Creation of Import Freight

Bookings.

  Note

You use Business Add-In (BAdI) /SCMTMS/TOR_ASSIGN_SCAC to bypass or enhance the standard logic for the determination

of carriers from the SCACs, airline codes, and MAWB prefix.

  Note
By using a block, you can prevent the system from assigning a business partner to a freight booking or to a freight order as the

carrier. Open the Define Business Partner app on the launchpad. Display the business partner in the Carrier role and then

This is custom documentation. For more information, please visit SAP Help Portal.

166


1/14/26, 2:18 PM

select the Central Posting Block checkbox on the Vendor Company Org. Data tab.

## Company Codes

Company codes are used in freight documents, freight units, and transportation units to support the freight settlement process

during the subcontracting of transportation services to carriers or transportation service providers (TSP). Before communication

with the carrier or TSP, the system checks, for example, whether a company code has been entered in the header data of the

freight document.

## Prerequisites

You have specified in Customizing for the freight order type, freight booking type, or consignment order type that the freight

document is relevant for subcontracting.

You have specified in Customizing for the freight order type, freight booking type, or service order type in the Subcontract.

Checks field that the system is to perform additional basic checks automatically.

For more information, see Customizing for Transportation Management under:

Freight Order Management

## Freight Order

 Define Freight Order Types

Freight Order Management

## Freight Booking

 Define Freight Booking Types

Freight Order Management

## Service Order

 Define Service Order Types

Freight Order Management

## Consignment Order

 Define Consignment Order Types

## Features

## Procuring Company Code

The procuring company code is responsible for the procurement of a transportation service from the carrier or transportation

service provider of a freight order. This is the company code to which the accruals for the freight costs are booked in financial

accounting.

If a unique company code has been assigned to a purchasing organization, the system uses this company code automatically as

the procuring company code of the freight document. The field in the general data of the freight document is filled automatically by

the system. If the system cannot determine a unique company code, the field remains empty.

If you have defined additional checks in Customizing and want to perform subcontracting actions for the freight document (such

as Send to Carrier or Carrier Selection), the system checks whether a company code has been entered. If the field has not yet

been filled automatically, you can also enter the company code manually.

If you want to change the automatically determined company code, you must change the corresponding purchasing organization.

Once communication with the carrier or TSP has been started, the company code can no longer be changed.

## Paying Company Code

The paying company code is responsible for paying the transportation requirement. It is determined by the system from the

predecessor document (for example, the sales order) and is displayed for the transportation stages of a freight unit or

transportation unit.

The following applies if you want to assign freight units or transportation units with a paying company code to a freight document:

This is custom documentation. For more information, please visit SAP Help Portal.

167


1/14/26, 2:18 PM

## Intercompany settlement is allowed

Freight units or transportation units with a paying company code that is not the same as the procuring company code of the

freight document can be assigned to the freight document until subcontracting actions are started from the freight

document. After this, only freight units or transportation units whose company code is the same as the company code of

the freight document can be assigned to the freight document.

## Intercompany settlement is not allowed

Freight units or transportation units can only be assigned to the freight document if their paying company code is the same

as the procuring company code of the freight document.

## Company Codes in the Transportation Cockpit

In the transportation cockpit, the procuring company code is displayed for freight orders, freight bookings, and consignment

orders. The purchasing organization and purchasing group are also displayed. You can change these values.

The paying company code is displayed for freight units and transportation units on stage level. You cannot change this value. The

system does not perform any checks.

These fields are available in all relevant lists and hierarchies as well as in the Gantt chart. Note, however, that you need to

implement SAP Note 2937249

 so that these fields are displayed.

Checks in Freight Order Management

## Use

A series of checks is provided in Freight Order Management. Some of these checks are described in detail below. You can start

most of these checks manually. However, note that in the case of transportation units you can start only the document check

manually.

## Features

## Document Check

This check includes the following checks:

Check for cross-document time conflicts

Incompatibility check

Dangerous goods check

Capacity check

## Resource check

The system runs the check automatically when you save the business document. However, you can also start the check manually.

In both cases, the system sets the Document Check Status automatically. If you have made relevant changes to your business

document since the last check, the system runs another check when you save the business document and sets the status. For

more information about this status, see Explanation of Statuses of Business Documents.

## Check for Cross-Document Time Conflicts

This is custom documentation. For more information, please visit SAP Help Portal.

168


1/14/26, 2:18 PM

The system checks if there are time conflicts between a business document and its predecessor or successor business

documents. Time conflicts occur in the following situations:

A freight booking arrives too late for the subsequent freight order.

Transportation times do not lie within the pick-up and delivery window.

The system runs the check automatically when you save the business document. However, you can also start the check manually.

In both cases, the system sets the Cross-Document Check Status automatically. If you have made relevant changes to your

business document since the last check, the system runs another check when you save the business document and sets the

status. For more information about this status, see Explanation of Statuses of Business Documents.

## Incompatibility Check

You can check your business documents for incompatible data. For more information about incompatibilities, see Incompatibilities.

## Dangerous Goods Check

You can run a dangerous goods check for your business documents. For more information about dangerous goods, see

Considering Dangerous Goods.

## Capacity Check

You can run a capacity check for your business documents. For more information about capacities, see Quantities and Capacities.

## Resource Usage Check

The system checks whether a resource used in a business document is being used in another business document at the same

time. The system also checks the following:

Validity of the resource

## Downtimes

Existence of a planning lock

This check is run in the following cases:

It is run automatically when you enter a resource and save the business document.

You can start the check manually.

It is run automatically in the background when you change the resource availability in the resource master data.

You can still save the document if a resource is already used in a different document. The Document Check Status is set to red on

the Status tab page and in the personal object worklist. When you choose Check, the system displays more detailed information to

help you resolve any overlaps.

The system supports this check for all freight documents and transportation units that use resources. This check is also supported

for individual resources and for multi-resources with a defined number of individual resources. Note that you can run this check for

air freight and ocean freight bookings only as part of the document check.

## Check Readiness for Transportation Execution

The system runs this check when you choose Set to Ready for Transportation Execution. It is a preliminary check or simulation,

and checks the following:

This is custom documentation. For more information, please visit SAP Help Portal.

169


1/14/26, 2:18 PM

If it is subcontracting-relevant, that the subcontracting process for the document has been completed

## That there are no execution blocks

## That the load plan for multi-assigned package units has been finalized

when in an Advanced SR process: when setting the status in the container unit, that the container unit is assigned to a

freight order that is in Ready for Transportation Execution or further in the process.

That its condition allows this status's transition

Also, if you have indicated so in Customizing:

That all container items have an equipment group and type

## Whether a driver has been assigned

That an full-container load (FCL) booking only has container items below the main item

That an less-container load (LCL) booking has at least one cargo item

And if you want to reverse the status:

That no handling execution status-relevant event is set in the freight document

## Air Cargo Security Check

You can run an air cargo security check for your business documents. For more information, see Air Cargo Security.

## Activities

You can start these checks manually in the document under Check.

## Related Information

Example Checks to Find Errors in Business Documents

Use of Schedules

## Use

You can assign schedules to your freight orders and freight bookings (see Schedule).

## Prerequisites

You have defined schedules and schedule types. For more information, see Schedule Creation.

You have assigned the same transportation mode to the schedule and the freight booking or freight order.

## Features

The system copies the relevant data (for example, locations and times/dates as well as the carrier) to the freight booking or the

freight order. If you have defined capacities in the schedule, these are also copied automatically to the freight booking or freight

posting.

This is custom documentation. For more information, please visit SAP Help Portal.

170


1/14/26, 2:18 PM

If you have not created the schedule as a template and you change data in the schedule, the system does not automatically update

the freight booking or the freight order. As there is a connection between the schedule and your freight booking or freight order,

you cannot change the relevant data in the freight booking or freight order manually. However, it is displayed in the document when

an assigned schedule or a departure has changed (Schedule Data Status). You can display whether data has changed and, if so,

which data that was. To do so, click the status in the Schedule Data Status field or click the traffic light. You can update the data in

the document using Update from Schedule. For more information, see Schedule.

  Note

If you require an automatic update, you can create your own strategy and then specify this in your schedule type (CC strategy).

If you have created the schedule as a template, the system does not update the freight booking or freight order. In this case, there

is no connection to a schedule so you can change the relevant data in the freight booking or in the freight order.

When you assign a schedule to an air freight booking, a master-air-waybill number is drawn automatically. The prerequisite is that

you have entered an air waybill stock ID.

## Assignment of schedules at transportation stage level

You can assign a carrier schedule to one or more transportation stages of a freight booking. The system copies all carrier

information and the planned dates/times into the freight booking. If the freight booking contains several transportation stages,

you only have to select the first and last transportation stage. Depending on which carrier schedule you assign, the system adjusts

the transportation stages of the freight booking automatically. This function is only supported for schedules without gateways. For

more information, see Schedule.

## Activities

You assign schedules on the following user interfaces:

User interfaces for creating freight orders and freight postings

Open one of the following apps on the launchpad:

Create Road Freight Order

Create Rail Freight Order

Create Air Freight Booking

Create Ocean Freight Booking

## Transportation cockpit

For more information, see Creation of Freight Documents from Resources .

Use of Seals

## Use

You use seals in order to protect containers or unit load devices from unauthorized access during transportation. The number of

seals used depends on the type of container. A container with three doors, for example, has three seals. They also depend on the

partners used, as the seals can be put on by different partners.

## Shipper

This is custom documentation. For more information, please visit SAP Help Portal.

171


1/14/26, 2:18 PM

Carrier

## Customs

Which partner puts on which seal depends on the scenario. In sea transportation, the following partners are for example involved:

In the case of FCL (full container load), the shipper puts on the seal. The carrier only puts on another seal if the first seal is

damaged.

In the case of LCL (less than container load), the carrier consolidates the goods in the container freight station and puts on

a seal. Customs also puts on a seal if the goods are relevant for customs.

## Features

You can enter the following seal information for your business documents:

## Seal numbers

The seal numbers are displayed on the corresponding house bills of lading, master bills of lading and export declarations.

Date, time and time zone of the sealing and unsealing

## The partner who seals and unseals

You can enter more than one seal per container or unit load device.

If your forwarding order already contains seals, they are copied automatically to the corresponding business documents (for

example, the freight booking or freight order).

## Activities

In your business document, select a container item or unit load device item and enter the seal information.

Use of Hierarchical Views in FOM

## Use

Creating hierarchical views for freight order management (FOM) allows you to organize the view for freight orders and freight

bookings as well as for trailer units, railcar units, and container units.

## Prerequisites

You have configured the relevant Customizing settings to allow you to use hierarchies in the individual documents. The following

hierarchy types are predefined by default:

CRGRD for cargo management (road)

CRGRA for cargo management (rail)

CRGAC for cargo management (air freight)

CRGOC for cargo management (ocean freight)

## EQUI for equipment

This is custom documentation. For more information, please visit SAP Help Portal.

172


1/14/26, 2:18 PM

HBL for house bills of lading

SERV for the service items view

ITEM for a generic view of all items

STAM for status management

## LSO for the display of load plans

You can also define hierarchies with separate hierarchy types and groupings. You can specify the function (consumer) that each

hierarchy type can use. Furthermore, you can specify a UIBB configuration to structure your user interface to meet your

requirements. For more information, see Customizing for Transportation Management under  Freight Order Management

 Define Hierarchical Views for Business Documents .

  Note

View switches are not relevant for freight order management.

## Features

You can select the required hierarchy type in the individual documents. This allows you to specify how the items are to be

displayed. This includes which hierarchy levels are displayed and according to which attributes items are to be grouped.

## Activities

You change the hierarchy type by selecting the required hierarchy type in the Change Hierarchy field on the Items tab page on the

user interface of your business document.

  Note

The Items tab page replaces the Cargo, Cargo Management, and Equipment tab pages. You can personalize your user

interface in such a way that the system displays the old tab pages.

This field is available on the Capacity and Cargo tab page for air freight bookings.

## More Information

Hierarchical views are also used in planning (transportation cockpit). For more information, see Use of Hierarchical Views.

Use of Account Numbers

## Use

If an executing carrier has created one or more account numbers for you, you can enter and change these on your freight

documents.

## Prerequisites

Optional: You have entered your account numbers in the Define Business Partner app on the launchpad (in the role of

Carrier). You enter account numbers for individual purchasing organizations on the Vendor Org. Data tab page and account

This is custom documentation. For more information, please visit SAP Help Portal.

173


1/14/26, 2:18 PM

numbers for your company on the Vendor Company Org. Data tab page.

If the executing carrier has created an account number for your company, you can assign the purchasing organizations to

your company. For more information, see Customizing for Transportation Management under  Master Data

 Organizational Management

 Organizational Model

 Create Organizational Model

.

## Features

You can enter account numbers manually in your freight documents (in the Account No. with Carrier field).

The system can also determine account numbers automatically, provided that you have configured the settings mentioned in the

prerequisites above. If you enter or change the purchasing organization or carrier in your freight document (in an air freight

booking, this applies to the issuing carrier or local carrier), the system uses the organizational model to determine the

corresponding account number and displays it in the freight document. You can overwrite the account number. For air freight

bookings, the account number is also displayed in the master air waybill.

In co-load scenarios, you must enter the account number manually.

## Use of Batches and Serial Numbers

In Transportation Management (TM), you can store and display information about products, such as batch information and serial

numbers in business documents. This information is received from the supplier via an advanced shipping notification (ASN) and

helps you track the product. You can also transfer this information to the inbound deliveries or receive them from the outbound

deliveries.

In the consignment order and road freight order, you can manually enter or edit the batch and serial number information.

## Batch Management

You can specify whether you want to manage the product in batches. To do so, select the Batch Management setting in the Display

transaction. This enables you to get batch information in TM, store it and transfer it to warehouses such as Logistics Execution (LE)

and Extended Warehouse Management (EWM). To do so, on the SAP Easy Access screen choose  Logistics

 Equipment and

Tools Management

 Master Data

 Material

## Display

 Display . In the transaction, go to the General Data section of the Sales:

General/Plant tab page.

## Serial Numbers

You can define serial number profiles for deliveries created in TM.

The serial number profile has Serializing Procedures. You can define whether the use of serial numbers for a serializing procedure

should, for example, be mandatory or optional. To do so and for more information, go to Customizing for Logistics - General under

Handling Unit Management

## Basics

## Serial Numbers

 Define Serial Number Profiles .

Statuses of Business Documents

## Use

This section contains the list of statuses that the following business documents can have:

Freight order (see Freight Order)

This is custom documentation. For more information, please visit SAP Help Portal.

174


1/14/26, 2:18 PM

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

Fully Assigned

Overassigned

Planning status

## Not planned

Partially Planned

## Planned

Not Ready for Planning

Not Published

## Status

Freight order

Freight booking

## Freight unit

Transportation unit

Service order

## Freight order

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

## Update Sent, No Confirmation Yet

This is custom documentation. For more information, please visit SAP Help Portal.

175


1/14/26, 2:18 PM

## Status

Tendering status

## Status Values

Business Documents That Can Have This

## Status

Document Changed After Confirmation

Document Changed After Rejection

Not Published

## Published

Review Required

## Completed

Freight order (not supported for rail

freight order)

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

Confirmed by Carrier with Deviations

Canceled by Shipper and Acknowledged by

Carrier

Picked Up

Missing Cargo

On Hand

Shipped

## Delivered

Delivery Failed

Freight order

Freight booking

## Freight unit

Transportation unit

## Cargo receipt status

This is custom documentation. For more information, please visit SAP Help Portal.

176


1/14/26, 2:18 PM

## Status

## Status Values

Business Documents That Can Have This

Execution status

Not Relevant

## Status

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

## Cargo Unloaded

This is custom documentation. For more information, please visit SAP Help Portal.

177


1/14/26, 2:18 PM

## Status

## Status Values

Business Documents That Can Have This

## Status

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

Cargo Partially Loaded/Coupled

## Cargo Loaded/Coupled

Load plan status/unload plan status (on

## Not Planned

stop and item level)

Not Relevant

Invalidated

Planned

Finalized

Freight order

Freight booking

Transportation unit

## Consignment order

Load plan item status/unload plan item

Not Planned

## Freight order

status (on item level)

This is custom documentation. For more information, please visit SAP Help Portal.

178


1/14/26, 2:18 PM

## Status

## Status Values

Business Documents That Can Have This

Not Relevant

Invalidated

Planned

Finalized

## Not Sent

Transmission-to-EWM status

## Status

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

Freight booking

Delivery status

Not Delivered

Partially Delivered

## Delivered

Freight unit, transportation unit, and

freight order if freight order or

transportation unit is automatically

created instead of freight unit (see

“Automatic Creation of Freight Orders” in

Freight Unit Building Rule)

Customs status

N/A

For more information, see Global Trade.

This is custom documentation. For more information, please visit SAP Help Portal.

179


1/14/26, 2:18 PM

## Status

## Status Values

Business Documents That Can Have This

Invoicing status

Not Invoiced

Partially Invoiced

Completely Invoiced

Over-Invoiced

Not Up-to-Date

## Status

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

The fixing only prevents the change of already existing planning results, that is, a fixed subcontractable document is allowed

to be subcontracted until a carrier is assigned. If a fixed document is already assigned to a carrier, no more change is

allowed in the planning results.

In VSR optimization, a fixed freight order must not be deleted and assigned freight units must not be unassigned.

For manual planning, you can specify in your planning profile whether you are allowed to change a fixed freight order or not

(Consider Fixing Status).

This is custom documentation. For more information, please visit SAP Help Portal.

180


1/14/26, 2:18 PM

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

Planning and execution of transportation is canceled. You can set this status manually at any time in the planning process

by selecting the Cancel Document pushbutton.

## Driver Assignment Status

This status is set automatically by the system on header level when you assign drivers to your entire freight order or individual

transportation stages of a freight order. This status is based on the number of required drivers that you indicate in the freight order

This is custom documentation. For more information, please visit SAP Help Portal.

181


1/14/26, 2:18 PM

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

## Planned

The transportation stage has been planned.

## Planned, Conflict Between FU and Freight Order/Booking Times

The transportation stage has been planned, but there exist conflicts with time constraints regarding the predecessor or the

successor transportation stage.

This is custom documentation. For more information, please visit SAP Help Portal.

182


1/14/26, 2:18 PM

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

## No Confirmation Yet

The carrier hasn’t sent a confirmation yet.

## Invalid Confirmation Received

The confirmation sent by the carrier cannot be interpreted.

## Rejected

This is custom documentation. For more information, please visit SAP Help Portal.

183


1/14/26, 2:18 PM

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

The freight request for quotation has been created in the tendering plan, but it has not been published yet.

## Open

The freight request for quotation has been published and sent to a carrier. Freight quotations can be submitted for

this freight request for quotation.

## Closed

This is custom documentation. For more information, please visit SAP Help Portal.

184


1/14/26, 2:18 PM

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

At least one freight request for quotation assigned to this step had been sent to a carrier. No more freight quotations

can be submitted to the assigned freight requests for quotations.

## Omitted

The tendering process was completed before the tendering step started.

## Booking Confirmation Status

This status is either set automatically by the system or manually by the user.

The status has the following values:

## Not Sent to Carrier

The freight booking hasn’t been sent to the carrier.

## Sent to Carrier

The freight booking has been sent to the carrier.

## Rejected by Carrier

The freight booking has been rejected by the carrier.

## Confirmed by Carrier

The freight booking has been confirmed by the carrier.

## Canceled by Shipper

This is custom documentation. For more information, please visit SAP Help Portal.

185


1/14/26, 2:18 PM

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

quantity (in pieces) is lower than the planned quantity. In this case, the system executes a freight unit (FU) split. This means

that it updates the existing FU and its predecessor documents with the actual quantity, and creates a new FU for the

missing pieces.

## On Hand

The cargo has been received. This status is set automatically when actual quantities are reported. After this status has been

set, only the actual quantities in the freight order or freight booking are taken into account. You can change these quantities

in the freight order or freight booking. If changes are subsequently made in the forwarding order, they are not copied to the

freight order, freight booking, or freight unit.

## Shipped

The cargo has been shipped. This status value is used in the direct integration of Transportation Management (TM) and

Extended Warehouse Management (EWM) in SAP S/4HANA or SAP Extended Warehouse Management (SAP EWM).

## Delivered

The cargo has been delivered.

## Delivery Failed

The cargo item could not be delivered.

After you remove a freight unit from a freight order, the system allows you to keep the items without reference to the

predecessor document in the freight order if the cargo receipt status of the items is at least On Hand. In this case, the cargo

receipt status is set to Delivery Failed for these items. As a prerequisite, you must have selected the Enable Additional

Execution Checks checkbox in the Customizing activity for defining freight order types.

This is custom documentation. For more information, please visit SAP Help Portal.

186


1/14/26, 2:18 PM

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

Finalized (Air). This triggers when either the first execution-relevant event is reported or the first stop's execution

status in the freight document is updated. For more information, see Customizing for Transportation

Management under  Freight Order Management

 Execution Settings

 Define Event Profiles .

Not Ready for Transportation Execution/MAWB Not Finalized (Air)

Transportation execution cannot be started yet because either the check for readiness of execution failed or you set the

status manually to this value.

## In Execution

Execution was started.

You can specify in Customizing for the business document type that the business document is set immediately to In

Execution after creation.

This is custom documentation. For more information, please visit SAP Help Portal.

187


1/14/26, 2:18 PM

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

In addition, the execution status on stop level considers the handling execution status. For example, the execution status on stop

level is only set to a green traffic light if the handling execution status has been set to Unloaded.

For air freight bookings, the handling execution status is also displayed on the Operations tab page and indicates the logistical

execution status. It contains the following:

Location ID (location code)

Status at last location at which freight units were picked up or delivered

## Date/time when the status was set

This is custom documentation. For more information, please visit SAP Help Portal.

188


1/14/26, 2:18 PM

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

In the outbound part of the Advanced Shipping and Receiving process, you can use the handling execution status option Set

Items to Loaded to manually set the status of the items at the warehouse loading stop to Loaded.

## Not Coupled

The trailer unit or railcar unit hasn’t been coupled at the current stop.

## Coupled

The trailer unit or railcar unit has been coupled at the current stop.

## Not Uncoupled

The trailer unit or railcar unit hasn’t been uncoupled at the current stop.

## Uncoupled

The trailer unit or railcar unit has been uncoupled at the current stop.

The handling execution status on stop level has the following values:

## Not Determined

The system sets this initial status value after you have created the business document. It indicates that no execution

activities have been performed for the containers at a stop.

If you change the status from Arrived to Set to Not Arrived, the status is displayed again.

## Cargo Ready for Loading

The goods are ready to be loaded and you have set the warehouse processing status to Completed. You can initiate

customs processes and have the good cleared before the truck's arrival and check in. Any items whose status is not set to

This is custom documentation. For more information, please visit SAP Help Portal.

189


1/14/26, 2:18 PM

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

unloading stop level. The system will automatically set the Checked In status. When you set the Checked In status manually

or the system sets it automatically, all the inbound deliveries for that stop get the status In Yard (for EWM deliveries) or In

Plant (for Logistics Execution (LE) deliveries).

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

The truck has arrived at the destianation location of the items to be unloaded, but the unloading has not been completed.

## Not Loaded

The cargo items have not been loaded.

## Loaded

The cargo items have been loaded.

In the outbound part of the Advanced Shipping and Receiving process, after you have finished loading the truck, you can

use the handling execution status option Set Stop to Loading Completed to set the status of the warehouse loading stop to

Loaded. After this status has been set, no further items can be loaded onto the truck, and the system automatically

removes all the items that do not have the status Loaded from the road freight order.

This is custom documentation. For more information, please visit SAP Help Portal.

190


1/14/26, 2:18 PM

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

The container hasn’t been unloaded at the current stop.

## Cargo Partially Unloaded

The container has been partially unloaded at the current stop.

## Cargo Unloaded

The container has been unloaded at the current stop.

## Cargo Not Loaded

The container hasn’t been loaded at the current stop.

## Cargo Partially Loaded

This is custom documentation. For more information, please visit SAP Help Portal.

191


1/14/26, 2:18 PM

The container has been partially loaded at the current stop.

## Cargo Loaded

The container has been loaded at the current stop.

Furthermore the status contains values that show for a truck not only the status of loading and unloading (as described above), but

also whether all its assigned trailers are coupled or uncoupled (or only some of them). For example, you have the status values

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

execution and the handling execution status are only changed when EWM or SAP EWM sends an LDAP notification to TM, when you

change the status manually, or when an execution event is reported, for example, by SAP Event Management.

The status has the following values:

## Not Planned

The plan hasn’t been started. This is the initial status value.

## Not Relevant

The plan is not relevant for this stop or item.

## Invalidated

The plan has changed (for example, items have been added or deleted); you have to set the status to Finalized again on

stop level to send an LDAP request to EWM or SAP EWM.

## Planned

The plan is in a preliminary state.

## Finalized

The plan is complete. The system automatically sends an LDAP request to EWM or SAP EWM, when the status value is set

on header or stop level of the freight document.

The load plan status for referenced capacity items (package items, container items, trailer items, and railcar items) is displayed in

the assigned successor document and can be set there as well. For example, if you have a road freight order with an assigned trailer

unit, you can set the load plan status for the referenced trailer item hierarchy in the road freight order directly.

This is custom documentation. For more information, please visit SAP Help Portal.

192


1/14/26, 2:18 PM

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

This is custom documentation. For more information, please visit SAP Help Portal.

193


1/14/26, 2:18 PM

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

The business document has been published and can be used by other users.

## Waybill/Bill of Lading Finalized Status

You set this status for freight units via your air forwarding orders.

This status has the following values:

## Not Finalized

The waybill or bill of lading hasn’t yet been finalized.

## Finalized

The waybill or bill of lading has been finalized.

Partially Finalized (only for freight bookings)

This is custom documentation. For more information, please visit SAP Help Portal.

194


1/14/26, 2:18 PM

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

## Master-Bill-of-Lading Status

You set this status manually after a master bill of lading has been created for an ocean freight booking. If you want to change the

master bill of lading number after having set this status, you first have to reset this status.

The status has the following values:

Master Bill of Lading Not Received

No master bill of lading has been received yet.

Master Bill of Lading Received

A master bill of lading has been received.

## Manifest Status

This is custom documentation. For more information, please visit SAP Help Portal.

195


1/14/26, 2:18 PM

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

This is custom documentation. For more information, please visit SAP Help Portal.

196


1/14/26, 2:18 PM

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

the calculated costs in the order and the invoiced values in the freight settlement document. An invoice is completed if the invoiced

values equal the calculated costs. An order is partially invoiced if the invoiced values are less than the calculated costs. An invoice is

over-invoiced if the invoiced values are more than the calculated costs.

## Schedule Data Status

This status is set automatically if a referenced schedule has been changed. For more information, see Use of Schedules.

The status has the following values:

## Data Is Up-to-Date

The referenced data is up-to-date.

## Data Is Not Up-to-Date

A referenced schedule has been changed and the referenced data is not up-to-date.

## Document Check Status

This status is set automatically, If you start the check manually and save the business document. The status has the following

values:

This is custom documentation. For more information, please visit SAP Help Portal.

197


1/14/26, 2:18 PM

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

The status has the following values:

## Not Archived

The business document hasn’t yet been archived.

## Archiving in Process

The business document has been selected for archiving and processed by the archiving pre-processing.

## Archived

The business document has been written to the archive. It can still be accessed in display mode.

For more information about archiving, see Archiving in Transportation Management (TM)

## More Information

This is custom documentation. For more information, please visit SAP Help Portal.

198


1/14/26, 2:18 PM

For information about statuses in Advanced Shipping and Receiving, see Statuses in Advanced Shipping and Receiving.

For information about statuses in the integration of a TM system with SAP GTS, see Statuses in the Integration with SAP

GTS (Inbound Process) and Statuses in the Integration with SAP GTS (Outbound Process).

Automatic Status Updates (Simple Scenario)

## Use

When you set a status for a freight document with two transportation stops, the system automatically updates related statuses

based on the status that you set. The sections below explain how the various statuses are updated.

## Features

## Handling Execution Status on Stop Level and Item Level

When you set the handling execution status on item level to Loaded, the system automatically sets the handling execution

status on stop level to one of the following values:

## Loaded

This status value is set if all items are loaded.

## Partially Loaded

This status value is set if only some items are loaded.

When you set the handling execution status on item level to Unloaded, the system automatically sets the handling

execution status on stop level to one of the following values:

## Unloaded

This status value is set if all items are unloaded.

## Partially Unloaded

This status value is set if only some items are unloaded.

When you set the handling execution status on stop level to Loaded, the system automatically sets the handling execution

status on item level to Loaded for all items.

When you set the handling execution status on stop level to Unloaded, the system automatically sets the handling

execution status on item level to Unloaded for all items.

## Load Plan Status on Item Level and Load Plan Status on Stop Level

When you set the load plan status or unload plan status on item level to Load Plan Finalized or Unload Plan Finalized, the system

automatically sets the load or unload plan status on stop level to Invalidated.

## Handling Execution Status on Stop Level and Execution Status

When the system sets the handling execution status on stop level to Loaded or Partially Loaded, the execution status on

header level is automatically set to Loading in Process.

When you set the handling execution status on stop level to Departed, the system automatically sets the execution status

on header level to In Execution.

This is custom documentation. For more information, please visit SAP Help Portal.

199


1/14/26, 2:18 PM

The execution status on stop level considers the handling execution status.

More Information

## Transportation Stops

Automatic Status Updates (Multi-Pickup and Multi-Drop
Scenario)

## Use

When you set a status for a freight order with more than two transportation stops, the system automatically updates related

statuses based on the status that you set.

The system provides additional logic compared to that described for the simple scenario (see Automatic Status Updates (Simple

Scenario)). This logic is described below by using the following example.

You have three full container load (FCL) freight units with two transportation stages, which are all planned on one freight order:

Freight unit 1 contains two stages: A -> BB' -> C

Freight unit 2 contains one stage: B' -> C

Freight unit 3 contains one stage: A -> B

The freight order contains two stages: A -> BB' -> C

  Note

In this example, B is the inbound stop at which unloading takes place, whereas B' is the outbound stop at which loading takes

place.

## Features

## Handling Execution Status and Cargo Receipt Status

When you set the handling execution status of the outbound stop to Departed, the system automatically sets the cargo

receipt status of the items to Picked Up if it has not been set already.

In the example, when you set the handling execution status of outbound stop A to Departed, the system automatically sets

the cargo receipt status of the items of freight unit 1 and freight unit 3 to Picked Up.

When you set the handling execution status of any outbound stop to Departed, the system automatically sets the handling

execution status of the previous outbound stops to Departed if any previous stops exist. If there are items for which the

destination stops match the previous stops, the cargo receipt status for these items is automatically set to Delivered. If

there are items for which the source stop matches the previous stops, the cargo receipt status is automatically set to

Picked Up.

In the example, when you set the handling execution status of outbound stop B' to Departed, the system automatically sets

the handling execution status and the cargo receipt status of the items of freight unit 2 to Picked Up and all items assigned

to freight unit 3 to Delivered. The handling execution status of outbound stop A is automatically set to Departed.

When you set all items to Picked Up on document header level, the system automatically considers the current stop to be

the outbound stop corresponding to the last location at which freight units are picked up (in this example, the outbound

This is custom documentation. For more information, please visit SAP Help Portal.

200


1/14/26, 2:18 PM

stop B').

When you set all items to Delivered or On Hand or you select Set to Quantity Received as Planned on document header

level, the system automatically considers the current stop to be the inbound stop corresponding to the last location at

which freight units are delivered (in this example the inbound stop C). The handling execution status of the items assigned

to the current inbound stop is automatically set to Unloaded and the handling execution status of the stop is automatically

set to Unloaded. All previous outbound stops are automatically set to Departed and the corresponding items (in this

example, the items assigned to freight unit 3) are automatically set to Delivered.

More Information

## Transportation Stops

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

Also, you have assigned the profile in Customizing to the document types (freight unit type, freight order type, freight booking type,

and transportation unit type). For more information, see Customizing for Transportation Management under  Freight Order

## Management

 Define Block Profile .

## Features

You can display all the automatic blocks on the Block Information tab page. Furthermore, you can set or remove blocks manually:

## Manual setting of blocks

When you set blocks manually, you can select a block reason from the values defined in Customizing. You can also set, for

example, multiple planning or execution blocks and choose different block reasons. All the block reasons are displayed both

in the aggregated view of the blocks next to the block status and in the successor documents.

You can set manual blocks for an entire business document or only for individual document items or stages.

## Automatic setting of blocks

If blocks were set in a predecessor document (this means in a forwarding order or freight unit), blocks are set by the

system. Automatic blocks can also be created after checking dangerous goods and approvals as well as during integration

This is custom documentation. For more information, please visit SAP Help Portal.

201


1/14/26, 2:18 PM

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

Mass Changes

## Use

You can make mass changes in the personal object worklist of the following business documents:

Freight orders

Freight bookings

Trailer units

Railcar units

## Container units

You can also make masse changes in the lists and hierarchies of the transportation cockpit.

## Features

If you select several business documents and then choose Mass Change, a dialog box appears. You can change general data in the

upper area of this dialog box. You can change locations and dates in the lower area. The lower area relates to the first and last

transportation stop in the business document.

You can also delete values by leaving the corresponding field entry and selecting the checkbox to its right.

This is custom documentation. For more information, please visit SAP Help Portal.

202


1/14/26, 2:18 PM

Whether a field can be changed corresponds to whether it can be changed in the individual business documents. This means that

even if all the fields in the dialog box are ready for input, the system can change the values in the individual business documents

only if these values can also be changed on the user interfaces for the individual business documents. For example, you cannot

change locations in a schedule-based freight booking. This means that the system cannot change a location during a mass change

even if you can enter a location in the dialog box.

The system tries to make as many changes as possible. If there are any changes it cannot make it displays a corresponding

message.

Calculation of CO  Emissions

2

You can view calculated carbon dioxide (CO ) emissions for each stage in a freight order, as well as as on freight unit item level.

2

## Use

On the CO  Emissions tab page of a road freight order, you can view calculated CO  emissions for each stage of the freight order,

2

2

manually enter actual CO  emissions for each stage, and display calculated and reported emissions per stage as a chart.

2

After the freight order has been executed, you can view the calculated CO  emissions for each item in a freight unit. On the freight

2

unit Items tab page, select an item and then navigate to the CO  Emissions tab page.

2

Calculated CO  emissions at stage level can also be used in planning. For details, see Greenhouse Gas Emissions.

2

## Prerequisites

You have defined CO  emission values for vehicle types.

2

You must enter the CO  emission factor for empty and fully laden trucks and specify a weight and distance unit. The

2

emission factors for the empty and the fully loaded truck are average emission values, determined from the average

consumption of the empty truck and the fully loaded truck during a mixture of road types (for example, express way or

town) and the elevation profile of the travelled roads (for example, flat or mountainous).

You have entered a payload weight and a corresponding unit of measure for the vehicle type.

For more information, see Customizing for CO2 Emissions Calculation.

## Calculation Method at Stage Level

The system uses a distance weight-based calculation method to calculate CO  emissions for each stage in a road freight order. This

2

is the cumulative total for each stage based on the distance travelled and weight of the load.

The following information is used in the calculation:

E

empty

: CO  emissions factor for an empty vehicle. For example in kg/km.

2

E : CO  emission value for a fully loaded vehicle. For example in kg/km.

full

2

Distance: The distance between the starting location and destination location of the stage.

w

maxload

: Maximum load

This refers to the payload weight defined for the vehicle type.

w : Load

load

This is custom documentation. For more information, please visit SAP Help Portal.

203


1/14/26, 2:18 PM

The load weight is derived from the products assigned to the freight unit.

For each stage in the freight order, the system calculates the emissions using the following formula:

(E

empty

 + (E  - E
full

empty

) * (w /w

load

maxload

)) * Distance

  Example
You have defined the following settings for a truck:

E

empty

: 0.2 kg/km

E : 0.3 kg/km

full

w

maxload

: 500 kg

Stage

Stage 1

Stage 2

## Example

Distance (km)

Total weight of items (kg)

Calculated CO  emissions (kg)
2

200

100

356

203

42.72

24.36

The system calculates the CO  emissions for stage 1 as follows:

2

(0.2 + (0.3 - 0.2) * (356/500)) * 200 = 42.72 kg

## Calculation Method at Freight Unit Item Level

The emissions at freight unit item level are calculated after the CO  emissions for each freight order stage have been calculated

2

and aggregated for the freight order. This total CO  emissions value is then allocated to individual freight unit items based on the

2

item weight and the straight line distance travelled for each stage.

The following information is used in the calculation:

The total CO  emissions for the freight order.

2

The total weight of the freight unit.

The straight line distance for the stage.

The weight of each item in the freight unit.

First, the system calculates which proportion of the overall CO  emissions for the freight order is to be allocated to each freight unit

2

using the total weight of the freight unit and the straight line distance travelled for the stage. This emissions value is then allocated

to the individual items in the freight unit based on the weight of each item.

Related Information

Sustainability

Freight Tendering

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

204


1/14/26, 2:18 PM

You can use this component to tender a road freight order (road FO) or ocean freight booking (FB) to one or more carriers. You can

use a tendering process based on a freight request for quotation (freight RFQ), or a direct tendering process.

You can execute a freight RFQ-based process manually or automatically. In this process, the tendering manager sends out a freight

RFQ to one or more carriers to tender an FO. The carrier either accepts or rejects the freight RFQ. If the carrier accepts, they send

back a freight quotation (FQ). You can either award or reject the FQ in the evaluation process. If you award the FQ, the system sends

the updated FO to the awarded carrier.

You can use the direct tendering process to send a road freight order (road FO) or ocean freight booking (FB) directly to a specified

carrier without creating a freight RFQ. Carriers can confirm or reject the FOs or FBs.

The tendering process described in the preceding section is depicted in the following figure:

## Features

The freight tendering component has the following features:

Multi-step tendering in a tendering plan

## Mix tendering types

For example, you can first use peer-to-peer tendering, and if this is unsuccessful you can use broadcast tendering.

E-mail, short message service (SMS), and business-to-business (B2B) communication channels for carriers

  Note
Short message service (SMS) isn't available for tendering of ocean freight bookings.

This is custom documentation. For more information, please visit SAP Help Portal.

205


1/14/26, 2:18 PM

## Tendering to one or more carriers

Manual and automatic tendering with carrier selection

## Background execution of tendering

Direct sending of FOs or ocean FBs to preferred carriers

This can reduce messages between ordering parties and carriers.

Flexible use of freight agreements (FA) to calculate price limits

Automatic reaction to changes in the FO or ocean FB

For example, you can stop tendering when changes are made to the FO.

To create freight RFQs, you must define the following master data:

Business partner to which the Carrier role is assigned

Business partner in which the Contact Person role is assigned to a carrier

Transportation lane to which a carrier is assigned (only for freight orders)

For ocean freight bookings, you can do either of the following to assign carriers:

Manually enters the carrier into the tendering plan for the freight booking.

Specify one or more carriers in a tendering profile and uses this as a basis for the tendering plan.

Define a Carrier Ranking List in the freight booking and use it for proposing carriers in the tendering plan. Select the

Carrier Assignment Method accordingly.

## Charge Management to calculate price limits

For more information, see Charge Management and Service Product Catalogs.

Carrier selection settings

## Freight agreements

For more information, see Agreement.

Basic Settings for Tendering

## Use

Before you can start tendering, you must have specified the following items:

Customizing settings for tendering

A tendering plan

## Prerequisites

You've defined the freight order or freight booking types that are relevant for subcontracting. For more information, see the

following Customizing for Transportation Management:

Under  Freight Order Management

## Freight Order

## Define Freight Order Types

This is custom documentation. For more information, please visit SAP Help Portal.

206


1/14/26, 2:18 PM

Under  Freight Order Management

## Freight Booking

## Define Freight Booking Types

If you've enabled lean service-based integration, you've to map the carrier's proposed amount to a valid charge type using

the BAdI, Determine the Default Charge Type. For more information, see Customizing for Transportation Management

under  Business Add-Ins (BAdIs) for Transportation Management

## Basic Functions

 Charge Calculation . You use this

mapping only when there are no existing charges in the relevant freight document. The carrier's proposed amount is then

considered as the final charge relevant to a transportation service and not as an Adjusted/Quoted Amount (ADJ) charge.

This final amount is then subsequently used in the posting of the freight document.

If there's a valid charge, the system creates an ADJ charge to represent the delta amount. In this case, mapping of the

carrier's response to a valid charge type using the BAdI isn’t required.

## Process

You specify the following Customizing settings:

Visibility settings

Rejection reason codes

Notification e-mail settings

Process settings

## Communication settings

Carrier-specific communication settings

## Default settings

For more information about tendering settings, see Customizing for Transportation Management under  Freight Order

Management

## Tendering

 Define General Settings for Tendering .

You can also specify freight order or booking type settings for tendering. You must have specified the process settings and

communication settings for tendering before you can specify the freight order or booking type settings.

If you want the system to use the default settings to determine the Customizing settings, select the Use Default checkbox.

If you want the system to use conditions to determine the Customizing settings, select the Use Condition for Sett. Determ.

checkbox.

If you want the system to use the freight order or booking type to determine the Customizing settings, select the Use Type-

Specific Settings checkbox. You must create a condition definition for the /SCMTMS/TEND condition type. This definition includes

the following details:

The condition definition itself

The following details in the condition table:

## The value of the attribute you've defined with the data access definition

The two result columns for tendering process settings and communication settings, which contain the names of the

settings you've created in Customizing for tendering

The system determines the tendering settings according to the type of freight order or booking.

If you want to use tendering in the background, separately from carrier selection, you can use the

/SCMTMS/TOR_TENDERING_BATCH program. For more information, see Tendering.

This is custom documentation. For more information, please visit SAP Help Portal.

207


1/14/26, 2:18 PM

Tendering Profile

## Definition

Can be used to define a tendering plan. It contains basic tendering data and is a prerequisite for automatic tendering. You can use a

tendering profile when you manually create a tendering plan.

## Use

You can use an existing tendering plan to create a new tendering profile. You can also create a new tendering profile without

reference to an existing tendering plan.

To use an existing plan to create a new profile, open the Road Freight Order or Ocean Freight Booking app from the launchpad and

open the required road freight order (road FO) or ocean freight booking (ocean FB). On the Tendering Execution area of the Edit

screen, choose the existing tendering plan. On the Tendering Plan area of the Edit screen, choose the Tendering Profile push

button, and select Save as Tendering Profile.

To create a new tendering profile without reference to an existing plan, choose  Application Administration

## Create Tendering

Profile  from the launchpad.

You can manually load a tendering profile to a tendering plan, or you can enable to system to load a profile automatically. The

system loads a profile according to the freight order or freight booking type that you have defined, or the settings you've defined in

the Customizing for tendering.

To manually load a profile, choose Load. To enable the system to load a profile, choose Load and Determine.

## Structure

The following are the main parts of a tendering profile:

## Tendering step

You can specify one or more tendering steps.

## Tendering type

The following are the tendering types:

Peer-to-Peer Tendering — Response Required

Peer-to-Peer Tendering — No Response Required

Broadcast Tendering — Best Offer

Broadcast Tendering — First Acceptable Offer

## Tendering process mode

The following are the tendering process modes:

Freight RFQ Based, Award Manually (only for freight orders)

Freight RFQ Based, Award Automatically (only for freight orders)

Direct Tendering, Send Freight Order Directly

## Carrier

This is custom documentation. For more information, please visit SAP Help Portal.

208


1/14/26, 2:18 PM

The assignment of a carrier is optional in a tendering profile. When you use a profile to create a new tendering plan, the

system can retrieve a carrier according to the carrier assignment strategy.

The following are the standard carrier assignment strategies:

## Get Carriers from Ranking List

Get Carriers from the Transportation Lane Master Data (only for freight orders)

Get Assigned Carrier from Freight Order

Assign Carriers Manually

## Relative price limit

You can set a relative price limit for each tendering step.

## Maximum response duration

This is the longest period of time within which a carrier must respond.

## Manual evaluation

This requires the tendering manager to manually evaluate each freight quotation (FQ).

## Price details

You can choose between the following options:

## Price Limit Only

Charge Hierarchy (only for freight orders)

For information about how price limits are calculated, see Calculation of Price Limits.

Carrier-specific freight agreement (only for freight orders)

For more information, see Agreement Maintenance.

## Visibility settings

For more information, see Visibility Settings.

## Communication Channels in Tendering

This function enables you to use the following communication channels in your tendering process:

## Communication using e-mail

The system supports e-mail communication. You must define the following criteria:

Assign a contact person to the business partner that you've defined with the role Carrier

## Enter a valid e-mail address for the contact person

For more information about creating and managing business partners, see Business Partner.

For more information about using e-mails in tendering, see Customizing for Transportation Management under  Freight

Order Management

## Tendering

 Define General Settings for Tendering .

## Communication using B2B messages

This is custom documentation. For more information, please visit SAP Help Portal.

209


1/14/26, 2:18 PM

The TM system of a carrier receives a freight RFQ as a forwarding quotation (FWQ). The carrier sends the FWQ back to the

sold-to party. The TM system of the sold-to party receives the FWQ as an FQ.

Transportation Lanes in Tendering

## Use

For road freight orders, you can use this function to enable the system to automatically assign carriers to tendering steps.

## Prerequisites

You've specified the following master data settings:

Means of transport

## Carriers

You specify business partners with the Carrier role.

## Locations

At least one transportation lane with carrier assignment

Carrier selection settings

## Features

You can enable the system to automatically assign carriers to peer-to-peer tendering steps and broadcast tendering steps. You can

use a Business Add-In (BAdI) to specify priorities.

## More Information

For more information about BAdIs, see Customizing for Transportation Management under  Business Add-Ins (BAdIs) for

Transportation Management

 Freight Order Management

 Tendering .

## Change Controller in Tendering

The change controller is a tool in Transportation Management (TM) that reacts dynamically to changes in your documents.

You can use this feature to manage your tendering process if you need to make changes to road freight orders (road FOs) or ocean

freight bookings (ocean FBs). The following are the change controller strategies available for the freight order type in Customizing:

Stop tendering and cancel the road freight order or ocean freight booking

Stop tendering and reset the planning

Restart current tendering

## Stop current tendering

For more information about the features of the change controller, see Change Controller.

This is custom documentation. For more information, please visit SAP Help Portal.

210


1/14/26, 2:18 PM

For more information about change controller strategies, see the following Customizing for Transportation Management under

Freight Order Management

## Freight Order

 Define Freight Order Types .

Under  Freight Order Management

## Freight Order

 Define Freight Order Types .

Under  Freight Order Management

## Freight Booking

 Define Freight Booking Types .

Calculation of Price Limits

## Use

This function enables the system to propose price limits for your tendering process. The system uses the features of

transportation charge management (TCM) to propose the price limit.

The system estimates price limits for a freight request for quotation (freight RFQ) according to the following criteria:

An individual freight agreement with a particular carrier

## The default freight agreement

To determine the default freight agreement, the system uses the purchasing organization assigned to the road freight order. In the

tendering plan, you can decide whether to use individual freight agreements or default freight agreements.

The system sends the price details according to the following criteria:

## Price Limit Only

The total amount mentioned in the Absolute Price Limit in a freight order or ocean freight booking column is sent to the

carrier as a price limit only.

Charge Hierarchy (only for freight order)

The total amount mentioned in the Absolute Price Limit column in a freight order is sent to the carrier as a price limit,

along with the complete charge hierarchy created during charge calculation.

After proposing the price limit, you can view the charge hierarchy before publishing the freight order. Save the freight order

and then under Tendering Execution, in the Published Freight Order Version column, click on the freight RFQ link. This

action displays the charge hierarchy information.

Depending on the visibility settings, the carrier can change either the total amount (if Price Limit Only chosen), or the total value of

the individual elements in the charge hierarchy via EDI.

## Prerequisites

You've defined the TCM features. For more information, see Charge Management and Service Product Catalogs.

## Activities

For an automatic tendering process, the system always proposes the price limit.

For a manual tendering process, to enable the system to automatically propose a price limit, open the Road Freight Order or Ocean

Freight Booking app from the launchpad and choose the freight order or freight booking . In the Subcontracting tab, under

Tendering Plan, select the tendering step, and choose  Propose

 Price Limit

.

This is custom documentation. For more information, please visit SAP Help Portal.

211


1/14/26, 2:18 PM

  Note

For a freight order, if you want to send the price limit or the whole charge hierarchy to the carrier, you must propose a price limit.

To set the price manually, in the tendering plan, enter a price in the Absolute Price field.

E-mail Processing for Tendering

## Use

This function allows you to manage the communication between a tendering manager and a carrier in a freight request for

quotation (freight RFQ) tendering process, exclusively by e-mail. This means that the system sends a freight RFQ to a carrier by e-

mail. The carrier responds to the e-mail using a regular e-mail client. The system treats the response to a freight RFQ e-mail as a

freight quotation (FQ).

  Note

The system doesn't support freight RFQ e-mails in a direct tendering process.

When tendering by e-mail, a carrier can perform the following tasks:

## Accept or reject a freight RFQ

Enter a rejection reason if they reject a freight RFQ

## Propose a price, if allowed by the visibility settings of the tendering process

A carrier must follow certain rules when responding to a freight RFQ by e-mail. They must use predefined keywords in the response

that are used by the Transportation Management (TM) system.

  Note

Freight RFQ e-mails are different from notification e-mails. A carrier can respond to a freight RFQ e-mail, but can't respond to a

notification e-mail. For more information, see Carrier Notification Process Management.

## Prerequisites

You've enabled your system to send and receive e-mails. You've enabled SAPconnect to facilitate this.

You've specified the following requirements:

## Text content for e-mails

You can specify these texts as general text documents in transaction SE61.

## Keywords to enable the system to process FQs received by e-mail

For more information, see Customizing for Transportation Management under  Freight Order Management

## Tendering

 Define Settings for Tendering by E-mail

.

You've specified the following settings in Customizing for Transportation Management under  Freight Order Management

## Tendering

 Define General Settings for Tendering :

Text documents that the system uses to e-mail carriers at particular events in the tendering process

This is custom documentation. For more information, please visit SAP Help Portal.

212


1/14/26, 2:18 PM

Communication settings for your tendering process, so that the system creates e-mails for freight RFQs, under 05 –

## Communication Settings

Business Workplace inbox for a system user to receive FQ e-mails from carriers

You can specify the e-mail address of the system user under 03 – E-mail and SMS Content.

  Note

You can't use short message service (SMS) message as a communication channel in tendering for ocean freight bookings.

## Features

The system sends a freight RFQ e-mail to a carrier when it publishes the associated freight RFQ. If the carrier responds to the

freight RFQ e-mail, they send the response back to the TM system. The system uses the Process Tendering Inbound E-mails

background report to convert the e-mail into an FQ. The system can then use the Process Freight Quotations and Overdue Freight

RFQs background report.

If your system supports sending secure e-mails, you can apply encryption or digital signatures to all freight RFQ e-mails. You can do

this by selecting the Encrypt E-Mails and Sign E-mails checkboxes in Customizing for Transportation Management under

Freight Order Management

## Tendering

 Define General Settings for Tendering .

  Note

These flags only add tags to the subject fields of the relevant e-mails. The encryption or digital signatures are applied by an

external secure e-mail proxy, if one is connected to your system.

## More Information

Communication Channels in Tendering

## Carrier Notification Process Management

For more information about using e-mail exchange between the SAP system and any SMTP mail server, see  SAP NetWeaver

## Library

 SAP NetWeaver by Key Capability

 Application Platform by Key Capability

 Platform-Wide Services

## Connectivity

 Communication Interfaces for Mail and Telephony

 SAPconnect (BC-SRV-COM)

 SMTP Configuration Guide .

For more information about secure e-mail proxies, see  SAP NetWeaver Library

 SAP NetWeaver by Key Capability

 Application Platform by Key Capability

 Platform-Wide Services

## Connectivity

 Communication Interfaces for Mail and

## Telephony

 SAPconnect (BC-SRV-COM)

 Administration

 Secure E-Mail

.

Carrier Notification Process Management

## Use

You can use this function to manage the process of notifying a carrier about particular events in the tendering process. The system

notifies a carrier by e-mail or short message service (SMS) message. Notification events include publishing freight requests for

quotation (freight RFQs), canceling a tendering process, and awarding or rejecting a freight quotation (FQ).

  Note

You can't use short message service (SMS) message as a communication channel in tendering for ocean freight bookings.

This is custom documentation. For more information, please visit SAP Help Portal.

213


1/14/26, 2:18 PM
## Prerequisites

You've enabled your system to send and receive e-mails. You've enabled SAPconnect to facilitate this.

You've specified the text content for e-mails as general text documents in transaction SE61.

You've specified the following prerequisites in Customizing for Transportation Management under  Freight Order Management

## Tendering

 Define General Settings for Tendering :

Text documents that the system uses to e-mail carriers at particular events in the tendering process

Communication settings for your tendering process under 05 – Communication Settings

This enables the system to create notification e-mails and SMS messages when particular events occur.

## Features

When a notification event occurs, the system creates a notification e-mail or SMS message. You can specify the notification events

in Customizing for Transportation Management under  Freight Order Management

## Tendering

 Define General Settings for

## Tendering

 05 – Communication Settings .

If you select the No Bundling of E-Mails checkbox in the Customizing settings for 03 - E-Mail and SMS Content, the system sends

an e-mail immediately after a specified notification event occurs.

For a freight order, if you select the No Bundling of SMS checkbox, the system sends an SMS message immediately. If you don't

make a selection, the system processes the e-mail or SMS message when it runs the Tendering E-mail and SMS Message

Processing report. The system collects the triggers for the same event for each recipient and creates one summary e-mail or SMS

message (for freight orders). For example, this enables you to send a summary e-mail that contains information on a number of

freight RFQs to a carrier.

If your system supports sending secure e-mails, you can apply encryption or digital signatures to all freight RFQ e-mails. You can do

this by selecting the Encrypt E-Mails and Sign E-mails checkboxes in Customizing for Transportation Management under

Freight Order Management

## Tendering

 Define General Settings for Tendering .

  Note
These flags only add tags to the subject fields of the relevant e-mails. The encryption or digital signatures are applied by an

external secure e-mail proxy, if one is connected to your system.

## More Information

## Communication Channels in Tendering

For more information about using e-mail exchange between the SAP system and any SMTP mail server, see  SAP NetWeaver

## Library

 SAP NetWeaver by Key Capability

 Application Platform by Key Capability

 Platform-Wide Services

## Connectivity

 Communication Interfaces for Mail and Telephony

 SAPconnect (BC-SRV-COM)

 SMTP Configuration Guide .

For more information about secure e-mail proxies, see  SAP NetWeaver Library

 SAP NetWeaver by Key Capability

 Application Platform by Key Capability

 Platform-Wide Services

## Connectivity

 Communication Interfaces for Mail and

## Telephony

 SAPconnect (BC-SRV-COM)

 Administration

 Secure E-Mail

.

## Creation of a Tendering Plan

This is custom documentation. For more information, please visit SAP Help Portal.

214


1/14/26, 2:18 PM
## Use

This process enables you to create a tendering plan, so that you can send out freight requests for quotation (freight RFQs) to

carriers. You can create a plan manually, or enable the system to create a plan automatically.

You can run automatic tendering in the background. After you start an automatic tendering process, the system determines a

tendering profile automatically. Depending on your settings, the system can propose the price limit and a carrier.

You can also create the tendering plan manually. You can use the steps and carriers of a previously used tendering profile in the

plan.

## Prerequisites

To determine a profile automatically, you've defined one of the following Customizing activities:

Process settings in the Customizing activity Define General Settings for Tendering.

The system uses these as the default settings.

Freight order or freight booking type settings in the Customizing activity Define Freight Order Types or Define Freight

Booking Types.

These settings use the process settings to determine the profile for a freight order or freight booking type.

## Process

To manually create a tendering plan, you need a road freight order or ocean freight booking for which you've started tendering but

which you haven't yet published. Use the following steps:

1. Open the Road Freight Order or Ocean Freight Booking app from the launchpad.

2. Set the Tendering Process Mode.

3. Create a tendering plan by defining the individual tendering steps.

If you select a profile, you can define the steps and carriers that the system automatically copies from the profile.

4. Specify the attributes of each tendering step.

For example, when you add a carrier, define carrier attributes such as maximum response duration and price limit.

For automatic tendering, the system loads a defined tendering profile, carriers, and price limits when you start the tendering

process.

## Result

You've set up a tendering plan. When you publish the tendering plan, the system sends the first freight RFQs. You can save the

tendering plan as a new tendering profile.

## More Information

For more information about tendering settings, see Customizing for Transportation Management under  Freight Order

Management

## Tendering

 Define General Settings for Tendering .

For more information about freight order settings, see Customizing for Transportation Management under  Freight Order

Management

## Freight Order

 Define Freight Order Types .

This is custom documentation. For more information, please visit SAP Help Portal.

215


1/14/26, 2:18 PM

For more information about freight booking settings, see Customizing for Transportation Management under  Freight Order

Management

## Freight Booking

 Define Freight Booking Types .

For more information about master data, see Master Data.

Tendering Step

## Use

You can use this function to structure a tendering plan. A tendering plan can contain one or more tendering steps. The system

executes the steps in sequence. However, it only starts a new step if the previous step hasn't led to an acceptable freight quotation

(FQ). A tendering step is always related to a specific tendering type.

## Example

The tendering manager enters a road freight order (road FO) or ocean freight booking (ocean FB) with two tendering steps:

1. Specifies a peer-to-peer tendering type and adds the three best carriers.

2. Defines a broadcast tendering type and assigns five carriers.

The first acceptable quotation is awarded the road FO or ocean FB.

Broadcast Tendering

## Definition

Simultaneous tendering to preselected carriers.

## Use

Carriers must respond to the freight request for quotation (freight RFQ) within the maximum response time defined by the

tendering manager.

Depending on the tendering type, the system performs one of the following tasks:

Use one of the freight RFQs to award the first acceptable freight quotation (FQ).

Evaluate the acceptable FQs and select the carrier that has submitted the lowest price, after the maximum response time

has elapsed

If a tendering step ends with no acceptable FQ, the system continues with the next tendering step that you have configured.

Peer-to-Peer Tendering

## Definition

Sequential tendering to preselected carriers.

This is custom documentation. For more information, please visit SAP Help Portal.

216


1/14/26, 2:18 PM
## Use

Peer-to-peer tendering involves the sequential sending of freight requests for quotation (freight RFQs) to each proposed carrier.

The system waits until the carrier sends a freight quotation (FQ) or until the maximum response time has passed.

The system evaluates the FQs according to the criteria you have defined in your tendering plan. The evaluation leads to one of the

following outcomes:

If you selected the tendering type Peer-to-Peer Tendering - Response Required and if you do not receive an acceptable FQ,

the tendering process continues and the system sends out of a new freight RFQ.

If you selected the tendering type Peer-to-Peer Tendering - No Response Required and if you receive an unacceptable FQ

or a rejected freight RFQ within the maximum response time, the tendering process continues and the system sends out a

new freight RFQ.

If the evaluation returns a Quotation Review Required result, you review the FQ. The tendering process continues.

If there is at least one FQ with a Quotation Acceptable evaluation result, the system preselects the FQ of the awarded

carrier. The tendering process ends successfully.

## Visibility Settings

The settings that control the information from a freight request for quotation (freight RFQ) that’s visible to a carrier, and that can

be edited by a carrier.

By default, carriers can view the price limit, and can submit a new price, and earliest and latest stop date times.

The settings for the price limit and submitting a new price also apply to the charge hierarchy (only for freight orders).

  Example

The tendering manager can use the following visibility settings, to match their business needs:

Disclose the price limit to carriers A and B.

Don't disclose the price limit to carrier C.

Don't allow any carrier to quote a different price.

Freight Request for Quotation

## Definition

A request containing information that is sent to a specific carrier to quote the quantities of a road freight order or ocean freight

booking that they can transport and the delivery dates to which they're capable of adhering. In addition, it can be used to request

pricing information from the carrier.

## Use

Depending on whether you choose broadcast or peer-to-peer tendering, you can send out one or multiple freight requests for

quotation (freight RFQs) at the same time.

This is custom documentation. For more information, please visit SAP Help Portal.

217


1/14/26, 2:18 PM

Tendering

## Use

For a freight order, you can use this process to send out freight requests for quotation (freight RFQs) to one or more carriers,

according to a tendering plan.

You can use a freight RFQ tendering process to send out one or more freight RFQs. You can send the freight RFQs manually, or

enable the system to send them out automatically.

You can also use a direct tendering process to send a road freight order (road FO) or ocean freight booking (ocean FB) directly to a

specified carrier without creating a freight RFQ. Carriers can confirm or reject the road FOs or ocean FBs. Unlike the freight RFQ

process, the system generally awards a carrier if they don't reject the road FO or ocean FB within a given time limit.

Direct tendering can be created and started manually by the user, or automatically by the system.

  Note

You can use only the direct tendering process for ocean freight bookings.

The related subcontracting process must not be in In Tendering status.

For more information on statuses, see Statuses of Business Documents.

## Prerequisites

You've defined the specific settings for freight order or freight booking type and tendering in Customizing for Transportation

Management.

You've set up a consistent tendering plan.

## Process

1. To plan and publish a new automatic tendering process, on the Edit screen of a freight order or freight booking, choose the

Subcontracting pushbutton, and select Automatic Tendering.

  Note
When you start the tendering process, the subcontracting process is at In Tendering status.

2. If you want to start the process manually, you must perform the following tasks:

a. Identify the FO or FB that you want to tender.

b. Enter the name of the tendering manager.

c. If you select a tendering profile on the popup screen, the system uses it directly in the tendering plan.

3. Set up one or more tendering steps in the tendering plan. You can define attributes in each tendering step, including the

following attributes:

## Tendering type

You want the carrier to formally respond

## Response time

This is custom documentation. For more information, please visit SAP Help Portal.

218


1/14/26, 2:18 PM

Absolute price limit

Price details

Visibility settings

## One or more carriers

4. You can enable the system to propose suitable carriers, a price limit, and visibility settings. For more information, see

Creation of a Tendering Plan.

5. You can save the tendering plan as a tendering profile that you can use for tendering processes in the future.

6. For your freight order, publish the first freight RFQ or all freight RFQs, depending on the tendering type you've selected for

your tendering step.

7. The tendering process runs automatically if you've performed the following tasks:

Set up the system and Customizing settings for automatic processing

The system determines a tendering profile automatically, according to your Customizing settings.

Scheduled the /SCMTMS/TEND_CONT_PROCESS report to run regularly

Documents and Notifications

## Use

This function enables you to send out documents or notifications to communicate with your business partners.

## Features

The table explains how you can use the following communication channels:

  Note

For the business-to-business (B2B) message communication channels, the relevant enterprise services have been mentioned.

Tendering Activity

## Communication Channel

Tendering manager publishes a freight request for quotation

(freight RFQ)

Tendering manager stops a tendering process

Freight RFQ by e-mail

## Notification e-mail

Notification short message service (SMS) message (only

for freight orders)

## Freight RFQ by B2B message

RFQ-based tendering (only for freight orders):

Request Transportation Order Quotation Creation

Direct tendering: Request Transportation Order

## Notification e-mail

Notification SMS message (only for freight orders)

This is custom documentation. For more information, please visit SAP Help Portal.

219


1/14/26, 2:18 PM

Tendering Activity

## Communication Channel

Freight RFQ cancellation by B2B message

Tendering manager awards a carrier

Carrier accepts or rejects a freight quotation (FQ)

RFQ-based tendering (only for freight orders):

Request Transportation Order Quotation

## Cancellation

Direct tendering: Request Transportation Order

## Cancellation

## Notification e-mail

Notification SMS message (only for freight orders)

Road freight order (road FO) and ocean freight booking

(ocean FB) by B2B message

RFQ-based tendering (only for freight orders):

Notify of Transportation Order Quotation

Direct tendering: Request Transportation Order

FQ by e-mail

## FQ by B2B message

RFQ-based tendering (only for freight orders):

Change Transportation Order Based on

Transportation Order Quotation Confirmation

Direct tendering: Change Transportation Order

Based on Transportation Order Confirmation

## Tendering Alerts

You can use this function to subscribe to Alerts for Tendering Managers using transaction ALRTCATDEF.

In the communication settings in Customizing, you can enable the system to send alerts to the relevant tendering managers, even

if the managers do not subscribe to the alert categories.

For more information, see Customizing for Transportation Management under  Freight Order Management

 Tendering

## Define

General Settings for Tendering .

Change Handling

## Use

You can use this process to change a road freight order, ocean freight booking, or tendering plan, while you're running a tendering

process.

## Prerequisites

You've defined conditions on the launchpad in the Create Condition app.

This is custom documentation. For more information, please visit SAP Help Portal.

220


1/14/26, 2:18 PM
## Process

You change a road freight order or ocean freight booking. This triggers the change controller to take a particular course of action.

For example, it can stop the tendering process.

1. If you change some information in a road freight order or ocean freight booking while you're running a tendering process,

the system chooses follow-on processes according to the strategy you've selected for the change controller.

  Example

The Trans company accepts changes of 1% to the quantity in a road freight order, without impacting the tendering

process. However, if the quantity in a road freight order changes by more than 2%, the system stops the tendering

process. A new process must be set up.

For more information on change controller settings for freight orders, see Customizing for Transportation Management

under  Freight Order Management

## Freight Order

 Define Freight Order Types .

For more information on change controller settings for freight bookings, see Customizing for Transportation Management

under  Freight Order Management

## Freight Booking

 Define Freight Booking Types .

2. If you need to change your tendering process, follow these steps:

a. Stop the tendering process by choosing the Stop Tendering pushbutton.

b. Start the tendering process again and make the changes.

Acceptance or Rejection of a Freight Request for Quotation

## Use

A carrier must respond to the sold-to party within the time limit given in the freight request for quotation (freight RFQ). The carrier

must accept or reject the freight RFQ before the response time ends.

Depending on the visibility settings defined in Customizing for tendering, the carrier can propose a different price or change stop

dates. The carrier can select one of the defined rejection reason codes to document a reason for rejecting a freight RFQ.

## Prerequisites

You've performed the following tasks:

Created collaboration user and have assigned the respective carrier organization.

Defined the visibility settings in Customizing for tendering to allow a carrier to change attributes such as price or stop

dates.

Defined rejection reason codes in Customizing for tendering.

## Features

The carrier can access the worklist containing the relevant freight RFQs and can also perform the following tasks:

## Accept or reject freight RFQs

Review previously submitted freight quotations (FQs)

This is custom documentation. For more information, please visit SAP Help Portal.

221


1/14/26, 2:18 PM

  Note

A carrier can create more than one FQ for the same freight RFQ. The system considers only the last FQ that the carrier submits

within the given time limit.

If the carrier accepts a freight RFQ, the system creates and submits an FQ. The system automatically copies attributes such as

stop dates and price to the FQ. If the charge hierarchy is used, the charge hierarchy submitted by the carrier overwrites the charges

of the freight order.

If the carrier wants to make a change, for example to the stop dates, and accept the freight RFQ, they must follow the following

procedure:

Open the FQ.

Create a new FQ with different stop dates.

Send the FQ.

If the carrier rejects the freight RFQ, the system creates a new FQ. The FQ contains one of the reason codes that have been defined

in Customizing. The system includes the reason code with the new FQ.

## More Information

For more information about visibility settings and rejection reason codes, see Customizing for Transportation Management under

Freight Order Management

## Tendering

 Define General Settings for Tendering.

Evaluation of Freight Quotations

## Use

You can use this process to enable the system to preselect freight quotations (FQs) according to the evaluation criteria you've

defined. The process ends when you award a carrier with a road freight order (road FO) or ocean freight booking. You have the

following options:

You can evaluate freight quotations immediately after they've been submitted.

You can use the /SCMTMS/TEND_CONT_PROCESS program to evaluate FQs and to detect that the maximum response

time for a freight request for quotation (freight RFQ) is over. Moreover, you can evaluate freight quotations that couldn't be

evaluated immediately due to a lock or other technical issues. For more information, see Processing of FQs and Overdue

## RFQs

You can use the following as evaluation criteria:

## Lowest price

Carrier who commits to stop date

  Note

If the carrier responds with different start and end dates or times, then as a shipper you've to accept the proposed date

and time before you award the quotation to the carrier.

## Fastest carrier

This is custom documentation. For more information, please visit SAP Help Portal.

222


1/14/26, 2:18 PM
## Prerequisites

To evaluate freight quotations immediately, the system administrator must have entered a system user name in the Quotation

Evaluation User field in Customizing. For more information, see Customizing for Transportation Management under  Freight

Order Management

## Tendering

 Define General Settings for Tendering

 07 - Default Settings . Make sure that the quote

evaluation user has sufficient authorizations. In addition to the authorizations that are specific to Transportation Management, the

quote evaluation user needs the following authorizations:

Authorization Object

Authorization Value

S_BTCH_JOB

Release

## S_BTCH_NAM

Quote evaluation user name

## Process

1. The system evaluates the FQs according to the criteria that you've defined.

2. The system preselects the most suitable carrier.

3. You either accept the preselected carrier or you award a different carrier with the FO.

  Note

If you set up the tendering process mode as Freight RFQ Based, Award Manually or Direct Tendering, Send Freight

Order Directly, the system performs this step automatically.

## Update of a Freight Order or Freight Booking

This function updates a road freight order (road FO) or ocean freight booking (ocean FB) immediately after you award a freight

quotation (FQ).

The system copies the new information from the awarded FQ to the road FO or ocean FB, including updates to the following

information:

Selected carrier

## Submitted price

Charge hierarchy (only for road freight orders)

Confirmed stop dates and times

Tendering Execution

## Use

The tendering manager can view all freight requests for quotation (freight RFQs) and freight quotations (FQs) that were sent to, or

received by, a carrier. The manager can use queries to search for and open freight RFQs and FQs.

You can tender a road freight order (road FO) or ocean freight booking (FB) more than once. This means that you can execute more

than one tendering process in sequence for a road FO or ocean FB.

This is custom documentation. For more information, please visit SAP Help Portal.

223


1/14/26, 2:18 PM

You can tender a road FO or ocean FB more than once in the following circumstances:

If a tendering process didn't determine a suitable carrier

If changes are made to a road FO or ocean FB when a tendering process is running

## Process

Open the Freight Order or Freight Booking app from the launchpad and perform the necessary tasks.

Creation or Update of Consignment or Freight Orders on Inbound
## Messages

You can create or update a consignment order or freight order either manually or by an inbound message using EDI.

Your business partner can send you a consignment order as an advanced shipping notification (ASN) or a freight order using EDI

communication. You then receive the message using the service interface TransportationOrderGenericRequest_In. Based on this

message, the system automatically creates or updates a consignment order or freight order.

For more information about manual creation of consignment orders, see Creation and Editing of a Consignment Order.

## Prerequisites

In Customizing for the freight order type or consignment order type, you can configure your settings for the handling of inbound

messages. For more information, see the following Customizing activities in Customizing for Transportation Management:

Freight Order Management

## Freight Order

  Define Freight Order Types

Freight Order Management

  Freight Order Management

## Consignment Order

  Define Consignment Order Types

## Separate or Combined Inbound Messages

You have the following options to create or update freight orders or consignment orders:

Separate Inbound Messages (Consignment-Based Freight Order)

Information for freight orders and consignment orders can be sent in separate inbound messages (ASN). The freight order

contains references to the related consignment orders. Ideally, the consignment order is sent first.

If a consignment order is error-free, the system can automatically create an inbound delivery in Logistics Execution (LE) if

the Customizing is set accordingly. If a consignment order or freight order that was sent in separate inbound messages

contains errors, it is usually still saved as a document in TM as long as the consignment order contains at least a source and

destination location. The errors are displayed on the Document Errors tab and can be corrected there. Whether the system

creates errors, depends on the setting that you have made in the Customizing for the freight order type or consignment

order type. If the freight order message is sent before the consignment order was created, and the consignment order is

created later, the assignment of the consignment order is done automatically by choosing the respective external

consignment ID.

TM creates deliveries for error-free FUs when you create or save a consignment order. Upon correction of errors in FUs, the

system will either asign these FUs to an existing delivery or create new deliveries for FUs with different external delivery

numbers. Once FUs are assigned to a delivery, the system cannot make changes to these deliveries during an MRP run and

the subsequent freight unit building step. As with consignment order errors, you can find and correct errors on the

Document Errors tab.

This is custom documentation. For more information, please visit SAP Help Portal.

224


1/14/26, 2:18 PM

For more information, see Example Checks to Find Errors in Business Documents and Correction of Errors in Business

Documents.

Combined Inbound Messages (Transport-Based Freight Order)

Information for freight orders and consignment orders and their item structure can be combined and sent in a single

inbound message. With combined inbound messages you can create freight orders and consignment orders and all the

related items underneath.

A combined inbound message contains both freight order header data and information about the full item structure (such

as, information about the active vehicle resource, shipment items, and references to the requirement documents). With this

information the system creates consignment orders with assigned freight units and a freight order with references to the

consignment orders. The consignment order type is then the default consignment order type defined in Customizing.

The system checks to make sure the information of the inbound message is error-free. If a combined message contains

serious errors, the system rejects the inbound message and no freight order is created.

It is not possible to share items of a consignment order between an active and a passive vehicle resource. Such item

structures can currently not be sent with EDI-messages.

Creating or Updating Consignment Orders (Information in Separate Inbound
Messages)

You can create or update consignment orders using inbound messages.

## Creating Consignment Orders

You receive, for example, an ASN from your supplier. The inbound message informs you about the expected cargo and contains

information about the external consignment. When your system receives the ASN, it creates a new consignment order including a

reference to the external consignment number that the supplier's system uses to identify the consignment. The relevant freight

units are determined on the basis of search criteria and assigned to the new consignment order.

Freight Unit Determination (Inbound)

How does the system find existing freight units? First, the system checks if the ASN contains references to a purchase order or

scheduling agreement.

If no purchase order or scheduling agreement reference is available for searching, the system searches for the freight units based

on the following search criteria:

## A combination of material number and vendor

Unloading point (optional additional search criteria, used if the result is not clear)

## No Matching Freight Units Found

If the system does not find any matching freight units, the new consignment order is marked as erroneous but can still be saved in

the freight order. The errors are displayed on the Document Errors tab and can be corrected by assigning a freight unit manually

later. For more information, see Correction of Errors in Business Documents.

## Updating Consignment Orders

The ASN can also be used to update consignment orders. You can, for example:

Update to correct item data like material master errors or reference errors

Update with changes in deliveries, for example, new product items were added or removed

This is custom documentation. For more information, please visit SAP Help Portal.

225


1/14/26, 2:18 PM

## Update product or package data

Creating or Updating Freight Orders (Information in Separate Inbound Messages)

You can create or update freight orders using inbound messages.

You receive, for example, an EDI message from your carrier with information about a freight order (bordero, bill of lading). When

your system receives the EDI message, it creates a new freight order and assigns the corresponding consignment orders to the

new freight order. The relevant consignment orders are determined on the basis of external references (such as external

consignment number and supplier).

Freight Unit Determination (External Transportation Planning)

For external transportation planning, the system searches the freight units with the following search criteria: First, the system

checks if the EDI message contains references to freight units, if not, the outbound delivery is taken as search criteria.

## Fixing of Packages

For consignment orders that are created or updated via EDI message (ASN), it is necessary, during the inbound process, to prevent

unintended changes to package information that might happen either manually during the check-in process at the gate or by

package building.

Therefore, the system automatically sets the load plan status of the packages and the load plan item status of the product items to

Finalized.

After the status has been set, the packages are fixed for further planning. This means that once a consignment is planned on a

freight order, you can only change the packages if you manually reset the status of the respective items within the freight order or

consignment order from Finalized to Planned. After changing (for example, updating data or adding new package items in the item

hierarchy) you set the load plan status back to Finalized. The status of the predecessor documents (either consignment order or

freight order) is also updated.

If an ASN message contains a package-related error (for example, a packaging material typo or a wrong packaging material) the

system sets the load plan status of the package to Invalidated. You can correct the error on the Document Errors tab. Once the

error is corrected the status of the packages and the package items is set to Finalized.

For more information about the check for package-related errors, see Example Checks to Find Errors in Business Documents.

## Handling of Updates by Inbound Messages After Manual Changes

When customizing a freight order or consignment order type, you can specify whether further updates of a business document by

inbound messages are allowed after you have already made manual changes in that document.

For more information, see Customizing for Transportation Management under  Freight Order Management

## Freight Order

 Define Freight Order Types  or  Freight Order Management

## Consignment Order

 Define Consignment Order Types .

## Displaying External ID Numbers

You can display external ID numbers your business partner sent, such as:

Number of external consignment (on tab Subcontracting)

External delivery note number (Select a product item and navigate to Document Reference (field External).

## External package ID

This is custom documentation. For more information, please visit SAP Help Portal.

226


1/14/26, 2:18 PM
## Related Information

Automatic Consignment Building

## Correction of Errors in Business Documents

You can use this function to display errors in freight orders and consignment orders that were created based on incorrect EDI

messages in Transportation Management (TM). You can then correct the errors manually.

## Prerequisites

In Customizing for the freight order type or consignment order type, you have selected the Enable Saving of Documents with
Errors value in the Handling of Incorrect Inbound Messages field. For more information, see the following Customizing activities in
Customizing for Transportation Management:

Freight Order Management

## Freight Order

 Define Freight Order Types

Freight Order Management

## Consignment Order

 Define Consignment Order Types

Freight Order Management

## Freight Booking

 Define Freight Booking Types

  Note

The system determines whether it creates a document with errors depending on the error. For some errors, documents are still

not created despite your Customizing setting.

## Features

In Transportation Management (TM), you can create freight orders or consignment orders automatically based on inbound

messages (such as advanced shipping notifications or transfers from an external TM system). However, these messages can

contain errors. As a result of some of the possible errors, the documents cannot be created in TM.

If you have activated the Customizing setting described above and the errors belong to the following error categories, the system

creates the documents despite the errors contained in the messages:

## Master data error

Reference error (references to predecessor documents)

You can then display and correct the errors on the Document Errors tab page.

You can use the Business Add-In (BAdI) BAdI: Addition of Categories for Error Handling to add your own error categories to the

Transportation Order (TO) business object in addition to the standard error categories. For more information, see Customizing for

Transportation Management under  Business Add-Ins (BAdIs) for Transportation Management

 Freight Order Management

## Freight Order Management

 BAdI: Addition of Categories for Error Handling .

## Correcting Master Data Errors

Errors can occur for the following master data:

Products

Resources

## Locations

This is custom documentation. For more information, please visit SAP Help Portal.

227


1/14/26, 2:18 PM

## Business partners

The errors are often related to IDs of products or other master data that are not known in the TM system. This could be because

the product has not yet been created, for example. The ID may also have been spelled incorrectly. You can correct both types of

error on the Document Errors tab page. You can do this as follows:

A product does not (yet) exist:

You choose the pushbutton for an action next to the description of the error. If the product has been created in the

meantime, the error is corrected automatically.

The product ID is incorrect:

You can enter the correct ID directly in the Correct Value column. A search help is also available.

You can first choose Error Details. The system selects the incorrect products on the Items tab page. You can also

enter the correct values here.

This same behavior also applies to locations, business partners, and so on. In this case, you can enter the correct

values in the relevant places in the document, such as on the Business Partner tab page.

  Note

A help text for the error message is also displayed when you choose Error Details. It explains how you can correct the master

data error.

If you have activated the function of intelligent error resolution in Customizing for Transportation Management, the system

provides the user with suggestions on how to solve errors based on previous solutions. For more information, see Intelligent

Resolution of Document Errors.

## Correcting Reference Errors

Document errors can also relate to references to predecessor documents, such as freight units, that are not known in the TM

system. To correct these errors, you can choose the pushbutton for an action next to the description of the error. A dialog box

appears in which you can, for example, select existing freight units.

## Automatic Correction of Document Errors

You can use the report /SCMTMS/TOR_RETRY_ERRORS to automatically resolve document errors in freight orders so that you do

not have to resolve them manually in each freight order individually. For example, you can resolve reference errors to an unknown

consignment order that is now available in the system.

We recommend that you run the report as a background job using a variant. However, you can also use the report UI to run it.

For more information, see the system documentation for the report.

## Automatic Correction of Reference Errors in Related Documents

If you correct errors, for example, on the Document Errors tab page of a consignment order or in the product item itself, the

system tries again to resolve reference errors in the related freight order. It checks if reference errors for an unknown consignment

order can be resolved. If the consignment order is now available in the system, the missing reference is automatically added in the

freight order.

## Blocking the Document

If the document contains errors, the system automatically sets planning, execution, and invoicing blocks for the document. These

blocks are displayed on the Block Information tab page with the corresponding block reasons.

This is custom documentation. For more information, please visit SAP Help Portal.

228


1/14/26, 2:18 PM

As soon as you have corrected the errors as described above, the system automatically removes the blocks.

For more information, see Blocking Information of Freight Units and Capacity Documents.

Related Information

Freight Order

## Consignment Order

Example Checks to Find Errors in Business Documents

## Example Checks to Find Errors in Business Documents

The system runs various checks when freight orders or consignment orders are created or changed either manually or by an

inbound message using EDI (for freight orders) or advanced shipping notification (ASN) (for consignment orders). Some checks

are also run for freight orders when events are updated by transportation event bulk notifications during execution.

## Overdelivery of Quantity

In the inbound process the system checks for an overdelivery of quantity when the system creates or updates a consignment order

on the basis of an inbound message or when you manually change quantities in a consignment order or freight order.

## Prerequisites

In the Advanced Shipping and Receiving inbound process, you must enable the setting for Enable Synchronization of Predecessor

Documents in the Customizing for freight order type and consignment order type to be able to update the item quantity in the

document. For more information, see Customizing for Transportation Management under  Freight Order Management

 Freight

## Order

 Define Freight Order Types  or  Freight Order Management

## Consignment Order

## Define Consignment Order Types

. For more information about the Advanced Shipping and Receiving process, see Advanced Shipping and Receiving.

## Features

For purchasing documents (such as purchasing orders or scheduling agreements) you can define a quantity tolerance for a

product item, a percentage by which the quantity can be exceeded. You can also specify that there is no limit on overdelivery

quantities (Unlimited).

You maintain these settings in the purchase order or scheduling agreement on the Delivery tab page.

For the quantity calculation, the system considers the product item quantity of the inbound message (or a manually entered value),

the open quantity, the tolerance, and the unlimited flag:

If the open quantity of an item plus the sent or manually entered quantity is below or within the tolerance, the system

creates the consignment order without an error message. "Open quantity" means quantity not yet assigned by a freight unit

to a consignment order or quantity already executed within a freight order.

If the open quantity of an item plus the sent or entered quantity exceeds the tolerance, the system creates the consignment

order despite the errors and saves the respective item locally. You can display and resolve the errors on the Document

Errors tab page. When the error is resolved (by changing the purchasing document or the quantity of the item in the freight

order or consignment order) the system automatically assigns the corresponding freight units to the consignment order.

If unlimited overdelivery is defined in the related purchase order or scheduling agreement, the system creates the

consignment order without an error message. The system adjusts the quantity in the latest freight unit and assigns it to the

consignment order.

This is custom documentation. For more information, please visit SAP Help Portal.

229


1/14/26, 2:18 PM

If no further freight unit exists, the system creates an error message and you need to adapt the purchasing document. For

scheduling agreement you need to create more call-offs. The system then generates more related freight units due to the

automatic freight unit building.

How to Resolve Errors?

Send a new inbound message (advanced shipping notification, ASN) to update the quantity with a quantity within the

tolerance.

Enter a new item quantity within the overdelivery tolerance limit on the Document Errors tab page in the business

document.

Increase the quantity of the ordered items or increase the overdelivery tolerance limit in the purchase order or scheduling

agreement.

Vendor, Goods Supplier

## Features

When an inbound message (ASN) arrives to update a consignment order, the system checks the sent vendor. It checks if the

vendor of the ASN matches the vendor of the referenced purchasing document (purchase order or scheduling agreement).

How to Resolve Errors?

If the vendor does not match, the consignment order is created with a document error.

You can then correct the vendor information in the purchase order or consignment order.

Alternatively, you can copy the vendor information from the predecessor document, or enter a new purchasing document

that contains the correct vendor information.

Or, you decide to save the new goods supplier sent with ASN, for example, if the original supplier cannot deliver. The stage

in the related consignment order and freight units is then adjusted accordingly.

## Package-Related Errors

When a consignment order is created or updated either manually or with an inbound message (ASN), the system checks for

package-related errors.

## Prerequisites

You have enabled the packaging material check for item types. For more information, see Customizing for Transportation

Management under  Freight Order Management

  Define Item Types for Freight Order Management

.

## Features

If errors are found, the consignment order is saved with a document error. Packages with errors are saved locally in the

consignment order. If one of the packages in a nested package has an error, the system also saves the top-level package locally,

though the top-level package doesn’t contain errors.

If, for example, one of the packages in a nested package contains the wrong packaging material, the system saves the top-level

package locally though the top-level package doesn’t contain errors. You can display and resolve the error on the Document Errors

tab page.

Examples for package-related errors:

This is custom documentation. For more information, please visit SAP Help Portal.

230


1/14/26, 2:18 PM

The package information contains a “real” product instead of a packaging material.

It contains an auxiliary packaging material instead of a packaging material.

It contains a packaging material instead of an auxiliary packaging material.

The package information is empty or has a typo.

How to Resolve Errors?

You can display and correct the errors on the Document Errors tab page of the consignment order.

If an ASN message contains a package-related error (for example, a packaging material typo or a wrong packaging material) the

system sets the load plan status of the package to Invalidated. Once the error is corrected, the status of the packages and the

package items is set to Finalized.

For more information about the load plan status and the fixation of packages against changes, see Creation or Update of

Consignment or Freight Orders on Inbound Messages.

Customs Reference Number

## Features

In the inbound process, the system checks the customs reference number that you receive from the carrier as part of the freight

order with assigned consignment orders, or that you enter in the business documents. This number is displayed in the Previous

Document field. If the format of the check digit in the customs reference number is not in compliance with the ISO standard 6346,

the system creates a document error on the Document Errors tab page in the freight document.

How to Resolve the Errors?

You can resolve the error by providing the correct customs reference number of the previous document. You can do so in the

following ways:

In the Items details for the consignment order, on the Customs tab page, you can enter the correct customs reference

number in the Previous Document field.

You can enter the correct number on the Document Errors tab page in the business document.

If the customs reference number was sent using an inbound message, you can request a new version of the inbound

message with the correct customs reference number.

For more information about the customs processes, see Global Trade.

Delivery-Related Errors

## Features

Certain process steps, such as an update from a TM freight order to an LE delivery, or the posting of goods movement to an LE or

EWM delivery are asynchronous. For example, users in different areas may attempt to update the same delivery at the same time

or post goods movements before warehouse processing is possible. This can cause errors, for example locking of business

documents, inconsistent data in busines documents, or failed updates to business documents.

You can use the Document Errors tab page to view details of errors. The following are some examples of possible errors when

working with the freight order:

## Goods Movement Posting

This is custom documentation. For more information, please visit SAP Help Portal.

231


1/14/26, 2:18 PM

If a TM user attempts to post goods movement on the freight order before the warehouse processing status of the EWM or

LE delivery is set to Ready for Warehouse Processing the system cannot post the goods movement.

## Freight Unit Building

If a TM user changes a freight order to update, for example, date information, while at the same time a user in LE makes a

change to the same delivery the system cannot make both of the updates. One of the changes has to be prioritized. The

system determines which update should be prioritized based on the warehouse processing status. During planning, the

system gives priority to updates from TM. Once transportation planning is completed and the warehouse processing status

is set to Ready for Warehouse Processing, warehouse tasks can begin, so an update from LE takes priority.

## Delivery update from TM to LE

For example, a user in TM makes a change to the freight order and saves it but the system is not able to update the

information in the LE delivery due to a technical fault.

## Delivery Update from EWM to TM

For example, a user in EWM updates a delivery but the system is not able to update the information in the TM system due to

a technical fault.

In all cases the system records the error on the Document Errors tab page with additional details from the application log.

Estimated Time of Arrival or Departure

## Features

If an inbound transportation event bulk notification updates the planned arrival or departure dates in a freight order or freight

booking, the system creates a corresponding event Estimated Time of Arrival or Estimated Time of Departure.

In a freight booking, the system takes over the updated times because there is no scheduling.

In a freight order, the system performs scheduling to check the updated dates and times within the document and then saves the

freight order with the updated times. If the time conflict can't be resolved using scheduling, the system creates document errors.

For example, the event Estimated Time of Departure is reported for the source location, but the departure time from the source

location of the freight order is later than the arrival time at the destination location of that freight order. The system performs

scheduling but the time conflict is not resolved. The system then creates a document error.

The planned arrival or departure dates can be updated several times with transportation event bulk notifications. You can also see

the original planned dates and time.

How to Resolve the Errors?

You can resolve the document error in the following ways:

You can correct the planned departure or arrival times manually to remove the time conflict.

You can send another transportation event bulk notification with the correct dates and times.

## Related Information

Correction of Errors in Business Documents

## Intelligent Resolution of Document Errors

This is custom documentation. For more information, please visit SAP Help Portal.

232


1/14/26, 2:18 PM

For master data errors in freight orders or consignment orders that have been caused by faulty inbound messages, you can save an

error history and get suggestions from the system on how to resolve errors based on previous solutions.

## Prerequisites

You have activated the function of intelligent error resolution in Customizing. You can decide if the error history is only

saved for analytical purposes or if the system also provides suggestions for solving errors on the user interface of the

business documents.

For more information, see Customizing for Transportation Management under  Basic Functions

 Error History

## Define

Basic Settings for Error History .

You have specified error reason codes and procedure categories in Customizing. For more information, see Customizing for

Transportation Management under  Basic Functions

## Error History

 Define Error Reason Codes for Error History  and

Define Procedure Categories for Error History.

## Features

On the Document Errors tab of freight order and consignment order business documents, you can resolve document errors that

have been caused by inbound messages. If, for example, a product ID has a spelling error or doesn't exist at all, you have several

options to resolve these errors. For more information, see Correction of Errors in Business Documents.

For master data errors, you have the additional option of intelligent error resolution. If you have activated this function in

Customizing, you get suggestions from the system on how to resolve such errors. Based on the error history, the system checks if

an error has occurred before and how it was resolved at that time. It then suggests the most frequent, the most efficient, or the last

resolution of the error. You can choose the suggestion that fits best for you or enter your own solution.

Using the search help in the Correct Value field you can display the different solutions based on the sender of the inbound

message and the error category.

Furthermore, you can specify in Customizing as of which number of identical solutions for the same error the system provides

suggestions.

## Additional Information About Error Resolution

On the Resolved Master Data Errors tab, you can enter additional information about how you resolved an error. You can select a

reason for the error and a procedure category. Furthermore, you can enter a comment. This information is stored in the error

history for analytical purposes (without indicating the user). It is also displayed in another business document if this document

contains the same error.

## Clean-Up Report

When two users resolve an error for the first time and at the same time, the system stores two identical entries of the error solution

in the error history. This consumes unnecessary storage space. Therefore, you can run the /SCMTMS/ERH_TRIGGER_CLEAN_UP

report to delete duplicates.

## Web Services for External Planning Scenarios

The integration of Transportation Management (TM) with the external transportation management system of a carrier allows you

to run order-to-cash or procure-to-pay processes and, at the same time, delegate the transportation planning processes to the

carrier.

This is custom documentation. For more information, please visit SAP Help Portal.

233


1/14/26, 2:18 PM

You can use TM output management to send A2A or B2B messages. TM output management is based on the Post-Processing

Framework (PPF) which is integrated in the Business Objects Processing Framework (BOPF).

## Prerequisites

You have activated Replication of Freight Unit in your Action Profile in Customizing for Cross-Application Components

under  Processes and Tools for Enterprise Applications

 Reusable Objects and Functions for BOPF Environment

 PPF

Adapter for Output Management

 Maintain PPF Settings .

You have assigned output profiles to freight unit types in Customizing for Transportation Management under  Freight

Order Management

## Freight Order

 Define Freight Unit Types .

You have defined a specific PPF action definition. The integration within the BOPF application is defined in the Customizing

activity Maintain Output Management Adapter Settings as described in Output Management.

  Remember

Only one-stage freight units (FU) are supported.

Currently, web services are only available for road freight orders as well as ocean and air freight bookings.

Web service TransportationOrderGenericRequest_In uses referenced requirement documents such as the

freight unit or delivery document to build up its stage sequence.

To reference freight units, you can use the freight unit ID and don’t need to specify all freight unit item IDs in the

message.

## Process

The following graphic gives you an overview of the communication and documents exchanged between TM and an external TM

system. The documents are exchanged by using web services based on the SOAP protocol.

This image is interactive. Hover over each area for a description. Click highlighted areas for more information.

Please note that image maps are not interactive in PDF outputs.

  Note

You should not use other web services to update the freight order during the transportation planning phase because a

subsequent freight order update from the external TM system with web service

TransportationOrderGenericRequest_In could overwrite these updates.

Instead, necessary updates to the freight order must be performed in the external TM system first and then sent with web

service TransportationOrderGenericRequest_In.

This is custom documentation. For more information, please visit SAP Help Portal.

234


1/14/26, 2:18 PM

The following table explains the process steps and web services in each process step.

## Phase

Process Step

## Details

## Web Service

Description of Web Services

Transportation Planning

Step  1:  Send  freight  unit

If  a

freight  unit

is

TransportationOrderGenericRequest_Out

or  consignment  order  to

created,

it

is  sent  to

the

external  planning

carrier  once  warehouse

system of the carrier

processing is completed.

Freight  unit  updates  can

be sent as long as the FU

is not planned.

Return to Diagram

Transportation Planning

Step  2:  Receive  freight

The  carrier  plans  the

TransportationOrderGenericRequest_In

order

freight unit onto a freight

order  and  returns  the

planning result.

Return to Diagram

## Sample XML Payloads

In the following, sample XML payloads are provided for the communication from the connected, external TM system to TM.

  Note

The sample XML payloads use sample data. You must replace these with the concrete data you set up.

Sample Code for Process Step 2: Replicate Freight Order (Transportation Planning)

The sample code creates a new freight order with external ID6599000001 and with standard carrier alpha code (SCAC) XYZ and

assigns freight unit 4200000001. Also, registration country and number are provided.

You can reference freight units by the freight unit ID and don’t need to specify all freight unit item IDs in the message. The related

freight unit data, which includes item information, is added during message processing.

  Sample Code

<glob:TransportationOrderGenericRequest xmlns:glob="http://sap.com/xi/SAPGlobal20/Global">
  <MessageHeader>
    <CreationDateTime>2024-01-12T13:00:00Z</CreationDateTime>
    <SenderParty>
      <StandardID schemeAgencyID="182">TM43</StandardID>
    </SenderParty>
    <BusinessScope>
      <TypeCode>3</TypeCode>
      <ID>EXTERNAL_PLANNING</ID>
    </BusinessScope>
  </MessageHeader>
  <TransportationOrder actionCode="04" completeTransmissionIndicator="true">
    <TypeCode>EF01</TypeCode>
    <CategoryCode>TO</CategoryCode>
    <TransportMeansTypeCode>0001</TransportMeansTypeCode>
    <CarrierParty>
      <StandardID schemeAgencyID="182">XYZ</StandardID>
    </CarrierParty>
    <TransportationStage>
      <ID>10</ID>
      <OrdinalNumberValue>1</OrdinalNumberValue>

This is custom documentation. For more information, please visit SAP Help Portal.

235


1/14/26, 2:18 PM

      <ExpectedDepartureDateTime>2024-01-17T08:59:00Z</ExpectedDepartureDateTime>
      <ExpectedArrivalDateTime>2024-01-18T10:59:00Z</ExpectedArrivalDateTime>
      <MainLoadingLocation>
        <InternalID>FU_SOURCE_LOC</InternalID>
      </MainLoadingLocation>
      <MainLoadingStopID>10</MainLoadingStopID>
      <MainUnloadingLocation>
        <InternalID>FU_DEST_LOC</InternalID>
      </MainUnloadingLocation>
      <MainUnloadingStopID>20</MainUnloadingStopID>
      <ItemAssignment>
        <ItemID>10</ItemID>
      </ItemAssignment>
      <ItemAssignment>
        <ItemID>1000000</ItemID>
      </ItemAssignment>
    </TransportationStage>
    <BaseBusinessTransactionDocumentReference>
      <ID>6990000001</ID>
      <TypeCode>1122</TypeCode>
    </BaseBusinessTransactionDocumentReference>
    <Item>
      <ID>1000000</ID>
      <CategoryCode>AVR</CategoryCode>
      <VehicleResource>
        <TransportMeansID>15N-J13</TransportMeansID>
        <TransportMeansHomeCountryCode>US</TransportMeansHomeCountryCode>
        <TransportMeansTypeCode>0001</TransportMeansTypeCode>
      </VehicleResource>
    </Item>
    <Item>
      <ID>10</ID>
      <CategoryCode>PRD</CategoryCode>
      <HierarchyRelationship>
        <ParentItemID>1000000</ParentItemID>
      </HierarchyRelationship>
      <BaseBusinessTransactionDocumentReference>
        <ID>4200000001</ID>
        <TypeCode>1122</TypeCode>
      </BaseBusinessTransactionDocumentReference>
    </Item>
  </TransportationOrder>
</glob:TransportationOrderGenericRequest>

## More Information

For more information about implementation, see SAP Note 1517523

.

## Related Information

Transportation Generic Ordering Out

Transportation Generic Ordering In

## Execution of Freight Documents

The handling execution status is used to manage the execution of freight documents. Changes to the handling execution status are

always accompanied by an event.

The user or external event reporting service reports an event, which triggers the handling execution status update at stop or item

level. When you change the handling execution status manually, an event is always reported in the background first. This means

that handling execution status changes are handled in a harmonized way, independently of whether they are triggered manually or

caused by the propagation of a relevant event into the document.

This is custom documentation. For more information, please visit SAP Help Portal.

236


1/14/26, 2:18 PM
## Event Profiles

The event profile contains all the events in the order in which they must be executed for the business document. Events can be

reported at internal locations, external locations, or Advanced Shipping and Receiving locations. You can classify events as

mandatory or optional and set an event as a default event..

## Handling of Skipped and Recalled Events

In Customizing for event profiles, you can define that a mandatory event can be derived and reported automatically. In this case,

when the next event defined in the event profile is reported, the system automatically reports the skipped event. This ensures that

all relevant events are reported in the correct order.

All these events can also be recalled, which reverts the status change to the last reported event and its status value.

For more information, see Event Profiles.

## Checks and Post Processing

For each event, the system performs checks in order for the event to be reported. Events can also trigger follow-up processes. This

supports different business scenarios where different actions might be required based on an event report, or where different

checks are required, such as in a customs-relevant scenario.

For more information, see Checks for Handling Execution Status-Relevant Events and Follow-Up Processes.

## Propagation to Related Documents

Events which are reported are also propagated to relevant assigned documents. If an event for a requirement item is reported, such

as Load End for Item, this event is also propagated from the capacity document to the requirement document. This ensures that

the documents are synchronized with each other. In general, transport execution is capacity-based, which means that most events

are only reported on the capacity document. On requirement documents such as freight units, it is not possible to report events.

For transportation units such as container units, you can report loading and unloading for its assigned cargo.

For more information, see Rules for the Propagation and Aggregation of Events

## Related Information

Statuses of Business Documents

## Event Profiles

Event profiles form the basis of event processing and define the order in which events are reported.

## Prerequisites

You have defined events in Customizing for Transportation Management, under

## Integration

 Tracking and Tracing of

## Processes and Documents

 Define Transportation Activities for Tracking and Tracing  or alternatively under  Freight

Order Management

## Execution Settings

 Define Transportation Activities and Event Codes .

You have defined event profiles in Customizing for Transportation Management, under  Freight Order Management

 Execution Settings

 Define Event Profiles .

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

237


1/14/26, 2:18 PM

SAP delivers events for standard transportation activities in an event profile, for example, Cargo Ready for Loading, Arrival, Check-

In, Unloading Begin, Unloading End for Item, Unloading End, Loading Begin, Loading End for Item, Loading End, Checkout, and

Departure. These are all events that affect the handling execution status of transportation order stops and transportation order

items. When creating new event profiles, this standard set of events for transportation activities is included, and you can add your

own events.

There are many more events that can be reported which do not affect the handling execution status, such as Estimated Time of

Arrival, Estimated Time of Departure, Record Actual Quantities, Record Verified Gross Mass Data, Schedule, and Delay. These are

processed but do not set a status value. These are mostly used to keep track of relevant information during transport execution.

Furthermore, there are also other status values which exist and are connected to the handling execution status, such as the cargo

receipt status, the handling cargo status, and the warehouse door status. These non-handling execution status-relevant events can

be included in the event profile, but are not directly derived during the processing of the handling execution status-relevant events.

Events can be reported at internal locations, external locations, or Advanced Shipping and Receiving locations. You can classify

events as mandatory or optional and set an event as a default event.

The following types of event reporting can be selected for an event:

## Mandatory: Event is derived and reported automatically

This means that while the event is mandatory it does not need to be reported explicitly by a user or service, but can instead

be reported automatically, when the next explicitly reported event in the sequence is reported.

For example, the event Arrival (EP_ARRIVAL) is set as “Mandatory: Event is derived and reported automatically”, the system

reports this event automatically when the next event in the sequence, Check In (EP_CHECK_IN), is reported manually by a

user.

Mandatory: Report event manually or via a service

The event must be reported manually by a user or by a service.

## Optional: Report event manually or via a service

For optional events, the event reporting is not required and will be skipped unless reported manually or by a reporting

service.

SAP provides the default event profiles DEF_CAPA for capacity documents and DEF_REQ for requirements documents. You can

also create your own event profiles for different scenarios, for example, road, rail, or ocean. After creating an event profile, you must

assign it to the document type for which it should be used. You do this in the Customizing activity for the transportation order type.

For example, in Customizing for Transportation Management, under  Freight Order Management

 Freight Order

 Define Freight

Order Type .

Rules for the Propagation and Aggregation of Events

## Propagation of Events

Transportation execution is done on the topmost executable level of the capacity document. From there the events are propagated

to the assigned requirement documents.

In case of item-related loading or unloading events, the event is propagated only to those requirement documents that also contain

the item referenced by the event.

For item-related loading or unloading events, the event is propagated only to the requirement documents that contain the item

referenced by the event. Note that an event is only propagated into requirement documents that are assigned to the stop at which

This is custom documentation. For more information, please visit SAP Help Portal.

238


1/14/26, 2:18 PM

the event is reported.

If item loading events are reported on an intermediate document level, such as the loading of items into a container unit, the events

are also propagated to the capacity document: in this case the capacity document of the container unit, for example, a freight

order or freight booking.

The propagated events then update the corresponding handling execution status on transportation order stop or transportation

order item level in the requirement document.

  Note

## Exceptions to Event Propagation

The Arrival and Check In events on the first stop of a freight order as well as the Check Out and Departure events on the last

stop of a freight order are exceptions to the above rule. These events are not propagated to freight units, package units, and

consignment orders.

Arrival and Check In events, and Check Out and Departure events are propagated to railcar units, trailer units, and container

units only if the stop at which the event is reported is also respectively the first or last stop of the transportation unit. The

system checks the stop category of the stop in the target document against the stop category maintained for the event in

Customizing and if it is not the first or last stop then the event is not propagated..

For more details, see Customizing for Transportation Management under

## Integration

 Tracking and Tracing of Processes

and Documents

 Define Transportation Activities for Tracking and Tracing . Select Event for Business Document. For each

event, such as EP_ARRIVAL, you can see the stop category.

Therefore, an event will be propagated if the following applies:

The stop category of the stop in the target document matches the stop category of the event maintained in the

Customizing activity Define Transportation Activities for Tracking and Tracing, or

The stop in the target document is a booking pick-up stop (that is, it is the first stop of a booking) or booking delivery stop

(that is, it is the last stop of a booking), or

The stop in the target document is the overall first or last stop of a container unit, trailer unit, or railcar unit.

  Note

## Event Propagation for Bookings

Events that occur multiple times in a booking, for example, when multiple pick-up FOs exist, are propagated to the booking

without dates. Additionally, the propagation only happens when all pick-up or delivery FOs have reached the minimal required

execution status.

Furthermore, events belonging to the transportation activities Cargo Ready for Loading, Loading Begin, Loading End, Unloading

Begin, Unloading End are currently not propagated. These events are always locally aggregated from the individual

LOAD_END_ITEM, UNLOAD_END_ITEM events.

## Aggregation of Events

In general, LOAD_BEGIN, LOAD_END, UNLOAD_BEGIN, and UNLOAD_END events on stop level refer to the loading or unloading

activities at a stop. They represent the aggregated loading status of the items being directly loaded into the capacity document.

  Example

This is custom documentation. For more information, please visit SAP Help Portal.

239


1/14/26, 2:18 PM

For a freight order with two container units, each containing two freight units, the events are aggregated as follows:

Load End on the freight order stop level means that all (both) container items are loaded on to the freight order.

Load End on the container unit stop level means that all loading- and unloading-relevant freight unit items (generally

speaking the top-level cargo items) are loaded into the container.

Load End on the freight unit stop level means that all loading- and unloading-relevant items of the freight unit are

loaded into or unloaded from the capacity document.

Loading freight units into a container does not affect the loaded status of the freight order stop (or its corresponding events), as

the freight units can be loaded into a container before the container is part of a freight order.

The following rules therefore only include the items of a document that are directly relevant for loading or unloading. For freight

orders, freight unit items are not included if a container unit is in between the freight order and the freight unit: that is, if there is a

document chain with three or more levels where the freight unit items are on a container unit which is assigned to a freight order. If

the freight order has a local container which has some items on it, both the items of the local container (the cargo) and the local

container itself are considered.

LOAD/UNLOAD_BEGIN: is aggregated for a stop if at least one loading- or unloading-relevant item at the stop is loaded or

unloaded.

LOAD/UNLOAD_END: is aggregated for a stop if all loading- or unloading-relevant items at the stop are loaded or unloaded.

  Note
On Advanced Shipping and Receiving shipping point level, no aggregation takes place, except for freight units. No aggregation

takes place at all on warehouse loading and unloading stop level.

## Checks for Handling Execution Status-Relevant Events

For each event that updates the handling execution status, the system can perform checks in order for the event to be reported.

In general, when an event that updates the handling execution status is reported, the system checks that the following basic

prerequisites are met:

There are no execution blocks on the document.

The document must have the execution status Ready for Execution or a later execution status, such as In Execution.

The stops must have locations assigned.

## Events Requiring Different or Extra Checks

The following events have different or additional prerequisites to the basic prerequisites listed above:

## Cargo Ready for Loading

At least one Item must have warehouse processing status Completed.

Can only be reported for warehouse loading stops.

## Unload end for item

This is custom documentation. For more information, please visit SAP Help Portal.

240


1/14/26, 2:18 PM

When there is no Advanced Shipping and Receiving, the following conditions apply:

There are no execution blocks on the document.

The document must have the execution status Ready for Execution or a later execution status, such as In

Execution.

For Advanced Shipping and Receiving, the following conditions apply:

There are no execution blocks on the document.

The document must have the execution status Ready for Execution or a later execution status, such as In

Execution.

The item must have the warehouse processing status Ready for Warehouse Processing.

The item must be assigned to a warehouse unloading stop.

## Load end for item

When there is no Advanced Shipping and Receiving, the following conditions apply:

There are no execution blocks on the document.

The document must have the execution status Ready for Execution or a later execution status, such as In

Execution.

For Advanced Shipping and Receiving, the following conditions apply:

When using Cargo Ready for Loading, we also ensure that there is no pending or failed delivery split before we allow

the event to be reported.

There are no execution blocks on the document.

The document must have the execution status Ready for Execution or a later execution status, such as In

Execution.

The item must have the warehouse processing status Completed.

The item must be assigned to a warehouse loading stop.

## Load end for stop

When there is no Advanced Shipping and Receiving, the following conditions apply:

Any updates sent to an integrated logistics solution, such as SAP Extended Warehouse Management (SAP EWM), must be

successful before the event can be reported.

For Advanced Shipping and Receiving, the following conditions apply:

Any updates sent to an integrated logistics solution, such as SAP Extended Warehouse Management (SAP EWM), must be

successful before the event can be reported.

When using Cargo Ready for Loading, we also require, that all items are loaded before Load End for Stop can be reported.

Check out

For Advanced Shipping and Receiving, the following conditions apply if you defined settings on how to handle not

completed warehouse loading stops:

There are no execution blocks on the document.

This is custom documentation. For more information, please visit SAP Help Portal.

241


1/14/26, 2:18 PM

Warehouse loading stops have the execution status Loaded.

No loading activities have started for warehouse loading stops without the execution status Loaded.

At check out, execution continues according to the settings defined for handling not completed warehouse loading

stops in Customizing under  Freight Order Management

## Execution Settings

## Define Event Profiles . For more

information, see the section Advanced Shipping and Receiving in Follow-Up Processes.

No pending or failed delivery split must be present when reporting Checkout.

## Recalling Events

To recall an event, the following basic conditions must be met:

There are no execution blocks on the document.

The stops must have locations assigned.

Additional checks are in place for the following scenarios:

Recalling Item Load End in an Adv. SR scenario is also possible if the warehouse loading stop has the status Cargo Ready

for Loading.

Recall Check-In in an Advanced Shipping and Receiving scenario

No item can have the warehouse processing status Ready for Warehouse Processing or later.

Recall Item Load End or Item Unload End events in an Advanced Shipping and Receiving scenario

This is only possible if the status of the warehouse loading or unloading stop to which the item is assigned is Not Loaded or

Not Unloaded.

## Processing of Customs-Relevant Documents

In case of integration with SAP Global Trade Services (SAP GTS), the checks for certain events differ from the standard to allow for

the processing of customs-relevant documents.

In an Advanced Shipping and Receiving outbound scenario, this is done by relaxing the check for execution blocks. Cargo Ready

for Loading, Arrival, Check-In, Load End for Item, and Load End for Stop can be reported in an export-relevant document even if

there is a customs execution block in place that states that an export declaration is required. Checkout and successive events are

prevented, which ensures that an export declaration is only created for the goods actually loaded and that the export declaration is

created before the transport leaves the yard. The same applies for the recall of the above events.

In inbound scenarios which are relevant for advanced customs integration, Check-In can be set even if there is a customs block

present. Unloading is prevented until unloading permission is granted.

## Follow-Up Processes

Event reporting can trigger follow-up processes or actions, depending on your settings.

## By Freight Order Type

In Customizing for freight order types, you can activate follow-up processes for events. Go to Customizing for Transportation

Management under Freight Order Management > Freight Order > Define Freight Order Types. Here, you can define the following

under Execution Settings:

This is custom documentation. For more information, please visit SAP Help Portal.

242


1/14/26, 2:18 PM

If it is the last expected event, the system sets the execution status to Executed.

The event triggers a goods issue posting.

The event triggers a goods receipt posting.

The event triggers a customer invoice.

## Consignment Orders

Based on settings made in the consignment building profile assigned to the freight order type, you can trigger the creation of

consignment orders.

For more information, see Automatic Consignment Building.

## Advanced Shipping and Receiving

The following processes can be triggered by either of the following statuses Warehouse Loading Stop – Loading Completed and

Cargo Ready for Loading:

In the case of Loading Completed, any items that have not been loaded are unassigned; in the case of Cargo Ready for

Loading, items whose warehouse processing status is not Completed are unassigned.

If settings have been maintained in the Customizing activity Define Customs Activities and Profiles, the status Ready for

Customs Invoice is set and a customs invoice is created.

For more information, see Configuration of Customs Processing.

The following processes can be triggered by the status Checked Out if settings have been maintained for handling not completed

warehouse loading stops (Hdl Not Cmpl Stops) in the Customizing activity Define Event Profiles:

A business document error is created if the status for one or more warehouse loading stops doesn't match the status

Loaded of the main stop. Execution continues.

Any items that have not been loaded are unassigned and have to planned again.

Any items that have not been loaded are reassigned.

A new stop for the shipping point is added to the freight document later in the sequence. The truck can check out and come

back later to pick up the remaining goods.

  Note

The settings for handling not completed warehouse loading stops only apply, if the event profile for Loading End events is set to

Optional: Report Event Manually or Via Service for Advanced Shipping and Receiving Locations. Other event profile settings

might lead to a check out block.

The settings only apply to freight orders.

Location Changes

## Use

You can change the location of a transportation stage that has already been scheduled. This can be necessary in the following

cases:

This is custom documentation. For more information, please visit SAP Help Portal.

243


1/14/26, 2:18 PM

You have accidentally created the forwarding order with the incorrect location data. You discovered this mistake during

scheduling and want to correct it.

The actual route has been scheduled correctly, however, a discrepancy arises during execution, for example, the truck does

not drive to the scheduled pre-carriage location. It goes to another location instead. You want to change this in the related

execution document.

After you have created the forwarding order and scheduled the transportation stages, you realize that the goods need to be

transported to another location. You want to adapt this in the actual route of the forwarding order.

## Features

You can change locations in the freight unit or in the related execution document, in other words, in the freight order, freight

booking, trailer unit, or railcar unit. If you change a location, the system checks automatically whether the it can transfer the

changes to all related documents and then executes one of the following actions:

The system adapts the locations in the documents.

It adds new locations.

If the system cannot adapt the locations, it deletes the existing assignments.

Moreover, the system adapts the following data automatically:

It automatically recalculates the durations and distances.

If you have changed the location in a freight booking, the system adapts pick-up and delivery in the related freight

documents.

If you change the locations in a freight unit and the related execution document is locked, the system automatically undoes the

change.

Example

Example 1:

Example 1

A freight order with one freight unit goes from A to C via B.

The truck now goes to X instead of B. In the freight order, you replace location B by X. The system checks whether it can replace B

with X in the freight order. As the freight order consists of only one freight unit, the freight unit can be adapted accordingly.

This is custom documentation. For more information, please visit SAP Help Portal.

244


1/14/26, 2:18 PM

Example 2:

Example 2

Freight order 1 for pre-carriage goes from A to B; follow-on freight booking 1 for the main carriage goes from B to C. Freight unit 1

goes from A to C.

During scheduling, you realize that freight booking 1 should not go from B to C. Instead it should go from X to C. Therefore, in freight

booking 1, you replace location B with X. The system checks whether it can also replace B with X in the freight unit. It adds an in-

between transportation stage from B to X, so that freight unit 1 goes from A to C via B and X.

Example 3:

Example 3

A freight order goes from A to C via B. Two freight units are loaded.

Freight unit 1 goes from A to C via B

## Freight unit 2 goes from A to B

During planning you realize that freight unit 1 is to be delivered via X instead of via B. Adapt freight unit 1 accordingly. The system

then tries to adapt the freight order. This is not possible due to freight unit 2. For this reason, the system automatically removes the

This is custom documentation. For more information, please visit SAP Help Portal.

245


1/14/26, 2:18 PM

scheduling for freight unit 1. Freight unit 2 is still assigned to the original freight order.

Enablement of Freight Settlement Documents for Creation

## Use

There are conditions in which you cannot create a freight settlement document under  Freight Document

 Follow Up

## Create

## Freight Settlement Document

. The tables below give you guidance on what the conditions are, and what you can do to enable

the freight document for settlement.

Incorrect Statuses

## Condition

Where You Can Review the Condition

## Your Response

Tendering status is not Carrier Assigned,

Freight Document

## Subcontracting

Finalize the tendering process.

Sent, or Completed (tendering has started,

 Tendering Overview

but has not completed).

Life cycle status of freight order or freight

Freight Document

 Statuses

## General

You cannot create a freight settlement

booking is Canceled.

document for a canceled freight document.

Freight order has an invoicing block

Freight Order

 Statuses

## Blocking

Resolve the reason for the invoicing block.

## Information

Charge correction advice document (CCAD)

Air Freight Booking

## Document Flow

You cannot create a freight settlement

exists

document from a freight booking when an

active CCAD exists against the booking.

Active means you have created but not yet

posted the CCAD to MM.

## Condition

Where You Can Review the Condition

Your Response

## Missing Information

If you have defined additional checks in

Freight Document

## General Data

If the field has not been filled automatically,

Customizing for the freight order type,

## Organizational Data

you can also enter the procuring company

freight booking type, or service order type

in the Subcontract. Checks field that the

system is to perform additional basic

checks automatically, the system checks

whether a procuring company code has

been entered.

code manually.

In a freight order there is no cargo, passive

For cargo on the UI:  Freight Order

Add at least one cargo item, passive vehicle

vehicle resource, and active vehicle

 Cargo

## Items

resource, or active vehicle resource.

resource.

For resources on the UI:  Freight Order

 General Data

 Resource Capacity

## Carrier not specified

Business partner for the partner function

Enter a carrier.

Carrier on the UI  Freight Document

## Business Partner

No document currency specified in freight

On the UI  Freight Agreement

## General

Enter a document currency or a local

agreement or in business partner and local

## Data

## Document Currency

currency in at least one of the currency

currency not specified in organization

master data

On the SAP Menu under  Logistics

 Transportation Management

## BP –

fields.

This is custom documentation. For more information, please visit SAP Help Portal.

246


1/14/26, 2:18 PM

## Condition

Where You Can Review the Condition

## Your Response

Maintain Business Partner

 Display in BP

role: Carrier

 Vendor Org. Data

## Currency

Customizing for Transportation

Management under  Basic Functions

 Charge Calculation

## Basic Settings

 Define Charges Profile

## Local Currency

No container item in a freight booking with

On the UI  Freight Booking

## Cargo

Add the container item in the freight

a shipping type of full container load (FCL)

## Items

booking if the shipping type is FCL.

Alternatively change the shipping type to

less than container load (LCL).

## Condition

Where You Can Review the Condition

## Your Response

Settings not Enabled in Customizing

Subcontracting not enabled in freight order

Customizing for Transportation

Enable the type for subcontracting.

type or freight booking type Customizing

Management under  Freight Order

activity

Management

.

For freight order types, see  Freight Order

 Define Freight Order Types .

For freight booking types, see  Freight

## Booking

 Define Freight Booking Types .

Settlement not enabled in freight order type

Customizing for Transportation

In Customizing, enable the type for

or freight booking type Customizing

Management under  Freight Order

settlement.

activity.

Management

.

For freight order types, see  Freight Order

 Define Freight Order Types .

For freight booking types, see  Freight

## Booking

 Define Freight Booking Types .

Related Information

## Freight Tendering

## Charge Correction Advice Management

Freight Settlement Integration using MM External Services Management

Cost Distribution Management

## Use

Freight costs are an important part of financial reporting in your businesses. You need the ability to allocate freight costs at charge

element level across a number of charge sources to manage the following business processes:

Freight costs

## Material valuations

Profitability of customers, products, and lines of business

This is custom documentation. For more information, please visit SAP Help Portal.

247


1/14/26, 2:18 PM

Customer billing for logistics service providers (LSPs)

As an LSP, you can use cost distribution to meet the following business needs:

Manage and assess the cost of executing freight orders, including an analysis of the following elements:

## Your own company resources

Subcontracted costs such as the cost of resources and base freight

Create customer settlements based on distributed internal and subcontracted costs

Use distributed costs from a freight order for the following activities:

## Customer billing for LSPs

Profitability analysis of forwarding orders

As a shipper, freight costs cover the following stock movements:

Inbound

Purchases

## Sales returns

Intercompany or intracompany stock transfers

## Outbound

Customer sales

## Purchase returns

## Intercompany or intracompany stock transfers

As an LSP, you can use the freight cost from external sources, such as a freight order, freight booking, or service order, and internal

costs, such as the cost of providing internal resources such as trucks and trailers, as a basis for creating settlement documents.

You can base settlement documents on costs as follows:

Use the distributed cost as a basis of settling with your customers. For more information, see Cost Pull.

Use a mixture of distributed cost, such as the cost of providing internal resources, and rate tables to settle with your

customers. For more information about rate tables, see Standard Charge Calculation.

Use the distributed cost, or a mixture of the distributed cost and rate tables, to create internal settlements between your

internal companies. For example, you can create an internal settlement based on the distributed cost, between the

purchase organization in the freight order or freight booking that provided the freight service, and the sales organization in

the forwarding order. For more information, see Internal Settlement Management.

Use the distributed cost for a profitability analysis of your forwarding orders. For more information, see Profitability

Analysis.

The system uses the freight charges in the freight order, freight booking, service order, and freight settlement document as the

basis for distributing freight costs from external sources, such as carriers or LSPs.

The system uses the internal freight charges that you incur when you use internal resources as a basis for distributing internal

costs. The system calculates internal freight charges in the freight order.

This is custom documentation. For more information, please visit SAP Help Portal.

248


1/14/26, 2:18 PM

You can distribute costs in a freight document where you have a logistics item that comes from a sales order, purchase order,

delivery item, or a forwarding order.

## Prerequisites

For both shippers and LSPs, you have specified the cost distribution settings in Customizing for Transportation

Management under  Basic Functions

 Cost Distribution .

For both shippers and LSPs, you have used the following settings to assign the distribution profile to the relevant

organization:

1. Assigned the distribution profile to the relevant charges profile in Customizing for Transportation Management

under  Basic Functions

 Charge Calculation

## Basic Settings

## Define Charges Profiles

2. Assigned the charges profile to the relevant purchasing organization in Customizing for Transportation

Management under  Master Data

 Organizational Management

 Organizational Model

## Change

## Organizational Model

. You assign the charges profile on the Org. Data (Organization Data) tab page of the relevant

purchasing organization.

For LSPs who want to use the freight cost in a freight document for internal settlement, you must enable freight document

for cost distribution.

For more information, see the following Customizing activities:

For freight orders, see Customizing for Transportation Management under  Freight Order Management

 Freight

## Order

 Define Freight Order Types .

For freight bookings, see Customizing for Transportation Management under  Freight Order Management

## Freight Bookings

 Define Freight Booking Types .

For service orders, see Customizing for Transportation Management under  Freight Order Management

 Service

## Order

 Define Service Order Types .

For shippers who want to transfer the freight cost at order/delivery item level, you must enable the freight settlement

document for cost distribution. For more information, see Customizing for Transportation Management under

## Settlement

## Freight Settlement

 Define Freight Settlement Document Types .

  Note
You cannot enable internal cost distribution for a freight booking. You can use an internal resource such as a truck or a

trailer to execute a freight order. You can distribute costs for an internal resource in a freight order.

You cannot distribute costs in a consistent way where you have a freight order, freight booking, service order, or freight

settlement document that contain a mix of forwarding order items and order/delivery items. In these cases, you can only

distribute costs to one distribution level, the forwarding order level or the order/delivery item level.

## Features

## Method, Rule, and Level

You can view the results of a cost distribution on the user interface (UI). You can only change the distribution settings in

Customizing. The following are the main cost distribution features:

## Distribution method

The system distributes costs in a direct or hierarchical distribution. In a direct distribution, the system distributes costs

according to the attributes you specify in the distribution rule and distribution level without reference to where in the item

This is custom documentation. For more information, please visit SAP Help Portal.

249


1/14/26, 2:18 PM

hierarchy you package a product. In a hierarchical distribution, the system uses a step-by-step approach to take each level

of the packaging hierarchy into account in the distribution.

## Distribution rule

The system uses criteria such as gross weight, net weight, gross volume, and distance times gross weight to perform a cost

distribution.

## Distribution level

The system uses a target level of forwarding orders or order/delivery items in a distribution.

## Service Orders

You can distribute costs in a service order to allocate the cost of the service order to the underlying distribution item.

More Information

Topic

## Link

Use cost distribution for shippers, including individual prerequisites

## Cost Distribution for Shippers

Use cost distribution for LSPs, including individual prerequisites

## Cost Distribution for LSPs

Use cost distribution in service orders for both shippers and LSPs,

Cost Distribution in Service Orders for Shippers and LSPs

including prerequisites and business case examples

Use of cost distribution in a group logistics scenario

## Group Logistics Company Process

Transfer distributed costs from the freight side to the forwarding

## Cost Pull

side, and use the costs as a basis for settling with a customer or an

internal organization.

Configure agency business documents

SAP Note 2535942

Handling of Failed Deliveries

## Use

If a carrier or driver fails to deliver goods to a location you can react as follows:

Instruct the same carrier or driver to attempt to redeliver the goods later (and keep the freight until this delivery)

Instruct the carrier or driver to return the loaded goods to the loading location so that a new delivery attempt can be

prepared

Transportation Management (TM) provides you with several options to plan the next steps accordingly. These options also depend

on whether you want to settle the cost of the failed delivery attempt later or are planning to perform a profitability analysis or cost

distribution, for example.

## Features

You can define in the freight document how you now want to plan the goods being transported after the failed pickup or delivery.

The options are described in detail below.

This is custom documentation. For more information, please visit SAP Help Portal.

250


1/14/26, 2:18 PM

## Retry Delivery

If you select this option, the transportation stage is kept in the freight unit and is rescheduled by the system. The system adds an

additional stage to the freight document, which is a duplicate of the original stage for the delivery to the location. Note, however,

that a freight booking can be adjusted only if the sequence of stops is not fixed by a schedule or in the booking itself. This also

applies to the next option.

Since the stage in the freight unit and the reference to the freight document are kept, the cost of the delivery attempt can be

calculated and then settled in the forwarding order based on the freight document. It is also possible to perform a cost distribution

and profitability analysis.

## Return to Loading Location

If you select this option, the system creates two new stages in the freight unit. The first stage plans the return of the goods to the

loading location. The second stage is created as described above to represent the new delivery attempt.

The system creates an additional stage in the original freight document to represent the return of the goods to the loading location.

The items are assigned the cargo receipt status Delivery Failed. Later, a stage is created in a different or new freight document to

represent the new delivery attempt.

It is possible to perform a charge calculation as described above.

## Remove Freight Unit, Keep Items in Freight Document

If you select this option, the system decouples the freight unit from the freight document. However, the items are kept in the freight

document. They are assigned the cargo receipt status Delivery Failed.

Since there is no longer a reference to the original freight document in the freight unit, you can no longer calculate the cost of the

delivery attempt in the forwarding order based on the freight document and perform any further settlement or cost distribution.

  Note

You can also decouple the freight unit manually from the freight document. To do this, you must remove the freight document

from the freight unit.

If you have configured this in Customizing and the cargo receipt status of the items in the freight document is at least On Hand,

the system sets the status automatically to Delivery Failed for the items. For more information, see Explanation of Statuses of

Business Documents.

## Activities

You can select the options in the freight document in the Status Management view of the Items tab page under Delivery Failed.

This dropdown menu is also available in the transportation cockpit.

If you want to decouple the freight unit and the freight document manually in the cockpit, you have to select the freight unit there

and remove the freight document.

## Example

In this example, goods are being delivered from a location in Boston to a location in New York. The delivery has failed, however,

because of a delay that means that the goods can no longer be delivered on the same day.

The carrier is to return the goods to Boston, where they were loaded. A different carrier will then attempt to redeliver the goods to

New York the next day. To plan this scenario, the planner selects the option Return to Loading Location, described above, in the

This is custom documentation. For more information, please visit SAP Help Portal.

251


1/14/26, 2:18 PM

freight document. The system creates the following new transportation stages in the freight unit and freight document:

Freight unit:

A stage from New York to Boston to schedule the return transport of the goods to the loading location

A stage from Boston to New York to schedule the new delivery attempt in New York

Original freight document:

A stage from New York to Boston for the return transport of the goods

The items are assigned the cargo receipt status Delivery Failed.

Other freight document:

A stage from Boston to New York for the new delivery attempt

  Note

If the goods are delivered across multiple stops, the return transport is processed also across the different stops in reverse

order.

Nature of Goods

## Use

The nature of goods is a short and meaningful description of the cargo to be transported. Although you can enter the nature of

goods only in business documents that are relevant for air transportation, the information is used along the entire transportation

chain. The business documents (for example, air forwarding orders and air bookings) and the corresponding print documents (that

is, air waybills and manifests) can contain the same nature of goods information or different information, according to your

requirements.

You enter the nature of goods as free text within the allowed space on the UI, which reflects the requirements for the number of

lines and characters. You can also define standard texts for nature of goods information that you use on a regular basis.

In Transportation Management (TM), there are two types of nature of goods:

## Nature and quantity of goods

This information can be entered in air forwarding orders and air bookings. You enter it on header level on the Nature of

Goods tab page in the air forwarding order and on the Operations tab page in the air booking. You can enter 12 lines with a

maximum of 20 characters per line.

The nature and quantity of goods specified on the Nature of Goods tab page in the air forwarding order or on the

Operations tab page in the air booking are synchronized with the Air Waybill View on the Charges tab page. When you

modify the nature and quantity of goods information on one of the UIs, the system automatically updates the other UI (for

example, if you update the nature and quantity of goods on the Air Waybill View in the freight booking, the system

automatically updates the nature and quantity of goods on the Operations tab page in the freight booking). The system not

only updates the UIs, but also centrally updates the nature of goods data in the backend system for the relevant business

document.

The nature and quantity of goods is printed in the house air waybill (HAWB), master air waybill (MAWB), and air waybill for a

direct shipment. It is used to provide additional information about the weight-based charge items in air waybills.

## Nature of goods for manifest

This is custom documentation. For more information, please visit SAP Help Portal.

252


1/14/26, 2:18 PM

This information can be entered in air forwarding orders, freight units, air bookings, and freight orders that cover pre-

carriage or on-carriage for the air booking. You can enter 9 lines with a maximum of 65 characters per line. In the air

forwarding order, you enter this information on header level on the Nature of Goods tab page. In the air booking, you enter it

on item level on the Capacity and Cargo tab page, and in the freight order, on item level on the Items tab page (Generic

Item View hierarchy type).

The nature of goods for manifest is printed in the security manifest and cargo manifests, which you print from the air

booking.

Note that you can also enter the nature of goods on the Notes tab page of the air forwarding order or air booking. However, we

recommend that you use the dedicated screen areas for nature of goods (for example, the Nature of Goods tab page in the air

forwarding order).

## Prerequisites

To use standard texts, you have done the following:

Assigned the text schema FWOAIRHDR to the relevant forwarding order types (Text Schema field)

Assigned the text schema CBAIR to the relevant booking types (Text Schema field)

## Defined standard texts in transaction SO10 using text type ST

For information about defining your own text types for the nature of goods, see SAP Note 2006789

. This SAP Note also

contains information about enhancing the pushbuttons for copying the nature of goods in air forwarding orders and air bookings.

## Process

1. You enter the nature and quantity of goods as well as the nature of goods for manifest on the Nature of Goods tab page in

your air forwarding order.

You can copy the nature of goods for manifest from the nature and quantity of goods. When you do this, the system

concatenates the text, but you can then adjust it as required.

The nature and quantity of goods is printed in the house air waybill (HAWB), which you print from the air forwarding order.

After you have calculated the charges, you can use the Air Waybill View on the Charges tab page to align the nature and

quantity of goods text so that it appears next to the correct weight-based charge items in the HAWB printout.

The nature of goods for manifest is not used to print documents from the air forwarding order, but is transferred

automatically to the follow-on documents.

2. You create freight units (FUs).

The nature of goods for manifest from the air forwarding order is displayed in the corresponding freight units. If required,

you can edit the text to create FU-specific information.

3. You create an air booking and you create a freight order for pre-carriage and on-carriage.

The nature of goods information is created as follows:

Nature and quantity of goods (air booking only)

You enter this information on the Operations tab page. If required, you can copy it from the air forwarding order to

the air booking (Copy from Requirement Documents). If more than one air forwarding order is assigned to the air

booking, the system copies the first 2 lines of text from the first 6 air forwarding orders. The text on the Operations

tab page is then also displayed on the Charges tab page.

Nature of goods for manifest (air booking and freight order)

This is custom documentation. For more information, please visit SAP Help Portal.

253


1/14/26, 2:18 PM

This information is copied automatically to the air booking and freight order from the freight unit. It is displayed in

the details area of a freight unit that you have selected on the Capacity and Cargo tab page in the air booking or on

the Items tab page in the freight order (Generic Item View hierarchy type).

For both types of nature of goods, you can change the copied text. For example, you can replace the text with something

that is specific to a certain stage, country or region, or you can write the text in another language. You can also insert a

standard text that you have defined beforehand.

4. You print the air waybill (master air waybill or air waybill for a direct shipment) or manifest (security manifest or cargo

manifest) from your air booking.

Similar to the air forwarding order, you can use the Air Waybill View on the Charges tab page to align the nature and

quantity of goods text so that it appears next to the correct weight-based charge items in the air waybill printout.

Note that when you print an air waybill or manifest from the air booking, the system uses the following logic to derive the

nature of goods:

a. It checks the air booking.

b. If the air booking does not contain any nature of goods information, it checks the freight units.

c. If the freight units do not contain any nature of goods information, it checks the air forwarding order.

The HAWB always contains the nature and quantity of goods from the air forwarding order.

  Note

You can specify the nature and quantity of goods only for weight-based charge lines under charge items with the

transportation mode Air.

If there are two stages with the transportation mode Air, then there can be two charge lines in the air waybill view for the

same logistical item. In order to avoid printing the duplicate charge line in the master air waybill or house air waybill, you

must mark one of these charge lines as inactive in the Grouped View or Ungrouped View and adjust the amount in the

other charge line manually, so that the overall charges remain the same.

The order of charge lines in the Grouped View or Ungrouped View and the Air Waybill View are not the same. In the Air

Waybill View, the charge lines are sorted by the position numbers and the nature of goods lines remain as defined in the

data of the air forwarding order or air booking. In the Grouped View or Ungrouped View, charge lines are sorted based

on the charge line numbers and the nature of goods lines align with the air waybill view.

More Information

## Printing

Building and Printing of House Bills of Lading and House Air
Waybills

## Use

You can use this function to create and print house bills of lading (HBLs) and house air waybills HAWBs) for the following business

documents:

This is custom documentation. For more information, please visit SAP Help Portal.

254


1/14/26, 2:18 PM

## Document

Supported Business Documents

House bill of lading

## Freight orders

Ocean freight bookings

Freight units

House air waybill

Air forwarding orders

Air freight bookings

Freight units

## Prerequisites

## Building of House Bills of Lading and House Air Waybills

In Customizing, you have specified a process controller strategy for your forwarding order type, freight order type or

freight booking type for the building of house bills of lading and house air waybills. For more information, see Customizing

for Transportation Management under:

Forwarding Order Management

## Forwarding Order

## Define Forwarding Order Types

Freight Order ManagementFreight OrderDefine Freight Order Types

## Freight Order ManagementFreight BookingDefine Freight Booking Types

Which strategy is used depends on the business document from which you build the house bill of lading or house air waybill.

If you do not define a strategy in Customizing, the system uses the relevant standard strategy for forwarding orders or

freight documents (see below).

You have defined a waybill stock. For more information, see Waybill Stock Definition.

You have activated the use of waybill stocks in forwarding order type Customizing (see below). If you deactivate this

function, you can only enter waybill numbers in the forwarding order manually, and the system does not check waybill

numbers entered against the waybill stock.

## Printing of House Bills of Lading and House Air Waybills

You have made the general settings for printing documents. For more information, see Output Management and Printing.

In Customizing for the freight unit type, which you use for freight unit building, you have defined the output profile

/SCMTMS/TOR_PRINT_AIR_FU. If you do not specify a freight unit building rule in Customizing for your forwarding order

type, and consequently do not define a special freight unit type, the system uses the standard freight unit type. For more

information, see Customizing for Transportation Management under  Planning

## Freight Unit

 Define Freight Unit Types

.

You have made the basic settings for the charge calculation that you need for your business process. For more information,

see Charge Management and Service Product Catalogs. You have made the following particular settings for printing the

house bills of lading and house air waybills:

In Customizing you have defined and appropriately classified charge types for weight-dependent charges, for other

charges and for valuation charges. This classification is necessary as the charge types appearing in the printing of a

house bill of lading or house air waybill are detailed separately. Note that the charge types classified as other

charges must contain the two digit code for IATA other charges and also entries for the charge due (carrier or

agent).

For more information, see Customizing for Transportation Management under  Basic Functions

## Charge

Calculation

## Basic Settings

 Define Charge Types , and also under Charge Calculation.

This is custom documentation. For more information, please visit SAP Help Portal.

255


1/14/26, 2:18 PM

You have created a calculation profile in Customizing. You should note in this connection that the system for

printing a house bill of lading or a house air waybill supports both the calculation of charges at stage level and the

calculation at item level. If you use an Incoterm in the forwarding order, the system switches to a calculation of

charges at stage level irrespective of the setting in the calculation profile.

For more information, see Customizing for Transportation Management under  Basic Functions

## Charge

Calculation

## Basic Settings

 Define Calculation Profiles , and also under Calculation Profiles.

You have created a calculation sheet. To do this, open the Create Calculation Sheet app on the launchpad under

Charge Management. If you want to print house bills of lading or house air waybills, you must have entered one of

the following values as the calculation resolution base for weight-dependent charge items:

PRODUCT (product)

MAIN_ITEM (main item of the document)

PACKAGE (package)

CONTAINER (container)

The weight charges for products, packages or containers are listed depending on the calculation resolution basis

that you have defined. The calculation resolution basis should be the same for all charge items, as otherwise you

may experience a mixture of package and product items, and the totals formation is rendered incorrect.

For more information, see Calculation Sheet.

## Features

## Building of House Bills of Lading and House Air Waybills

The system automatically groups all items that do not already belong to a fixed house bill of lading or house air waybill in

accordance with the process controller strategy you chose.

SAP provides the following strategies as part of the standard delivery.

Build House Bill of Lading or House Air Waybill by Shipper/Consignee (HBL_SHPCNS)

With this strategy, the system groups together all items that have the same shipper and consignee.

This is the standard strategy that the system uses for freight documents if you do not specify a strategy in Customizing of

the freight order type or the freight booking type. The system also uses this strategy if you build house bills of lading or

house air waybills for freight units or items.

Build House Bill of Lading or House Air Waybill by Forwarding Order (HBL_TRQID)

With this strategy, the system groups together all items that belong to the same forwarding order.

This is the standard strategy that the system uses for forwarding orders if you do not specify a strategy in forwarding order

type Customizing.

Build House Bill of Lading or House Air Waybill by Shipper/Consignee/Container (HBL_SCCONT)

With this strategy, the system groups together all items that have the same shipper and consignee, and are to be

transported in the same container.

Build House Bill of Lading or House Air Waybill by Freight Documents (HBL_FDOC)

With this strategy, the system groups together all items that have the same freight documents in the main carriage.

Build House Bill of Lading or House Air Waybill by Shipper/Consignee with Address (HBL_SHPCNA)

This is custom documentation. For more information, please visit SAP Help Portal.

256


1/14/26, 2:18 PM

With this strategy, the system groups together all items in which the shipper’s and consignee’s addresses are identical.

## Printing of House Bills of Lading and House Air Waybills

You can print of dispatch the house bills of lading or house air waybills you have built from the Output Management tab. For more

information, see Output Management.

The printout also contains information about the transport charges. You can define in an air forwarding order on the Charges tab

that the transportation charges as agreed or the other charges and their totals are to be printed. If the transportation charges as

agreed are printed, then all weight-dependent charges, charges, valuation charges and rates as agreed between the business

partners are printed (meaning not their currency amounts).

## Activities

You create house bills of lading or house air waybills as follows:

## Forwarding orders

You can create house air waybills by entering the waybill number manually or with  HAWB

 Draw HAWB Number

 from

the waybill stock. You can only draw a house air waybill (HAWB) number from the waybill stock if this involves an internal

number range and you have activated waybill stocks in Customizing (see under Prerequisites).

You can display data for bills of lading on the HBL or HAWB tab, and make individual allocations of waybill numbers to

freight units or items or remove the allocations again.

## Freight orders

You create house bills of lading by choosing  Follow-up Actions

 Build House Bill of Lading . You display house bills of

lading on the Items tab page by choosing Bill of Lading as the hierarchy type.

  Note

The Items tab page replaces the Cargo tab page. You can personalize your user interface in such a way that the system

displays the old Cargo tab page.

## Ocean freight bookings

You create house bills of lading by choosing  Follow-up Actions

 Build House Bill of Lading . You display house bills of

lading on the Items tab page by choosing Bill of Lading as the hierarchy type.

  Note

The Items tab page replaces the Cargo Management tab page. You can personalize your user interface in such a way

that the system displays the old Cargo Management tab page.

## Air freight bookings

You create house air waybills by choosing  Follow-up Actions

 Build House Bill of Lading . You display house air waybills

on the Capacity and Cargo tab page by choosing Air Waybill as the hierarchy type.

## Freight units

You create house bills of lading or house air waybills by choosing  Follow-up Actions

 Build HBL or HAWB . The

information for the house bill of lading or house air waybill is displayed at header level. A house bill of lading or house air

waybill can have one or more freight units.

For more information about hierarchy types, see Use of Hierarchical Views in FOM.

This is custom documentation. For more information, please visit SAP Help Portal.

257


1/14/26, 2:18 PM
## More Information

## Process Controller Configuration

Message-Based Communication with a Warehouse Management
System

## Use

You use this process to send loading and unloading instructions to an external system and to receive confirmations from an

external system. The following section contains a description of an example process:

## Prerequisites

You have configured your sending system, for example, Transportation Management (Transportation Management).

Your receiving system, for example, an external warehouse management system, can receive messages.

You have configured your XI system, for example, SAP NetWeaver Process Integration (SAP NetWeaver PI).

Freight bookings or freight orders exist.

## Process

1. You send a loading instruction to the warehouse by choosing one of the following actions in the freight order or in the freight

booking:

## Follow-Up

 Send Loading/Unloading Instruction

## Load Plan Status

 Set Load Plan to Finalized  and save the document

## Load Plan Status

 Set Unload Plan to Finalized  and save the document

TM sends the TransportationOrderLoadingAppointment_Out message to the receiving system, for example, an

external warehouse management system. This message contains the following information:

All relevant containers or unit load devices

## All assigned forwarding orders including the items

If necessary, the assignment of individual items to containers or unit load devices, if these exist

## Seal information, if this exists

Information about the status of cargo items with regard to air cargo security and compliance with foreign trade

regulations, if this exists

Information about the position and orientation of cargo items that are to be loaded into the freight space of a vehicle

or into a container, if this exists

Information about the settings that apply to the containers or unit load devices as regards temperature, humidity,

and ventilation

2. The warehouse loads the containers, unit load devices, or vehicles. This means the warehouse assigns the individual items

or, if necessary, changes the specified assignment. The warehouse then returns this information to the TM system. TM

receives the confirmations with the TransportationOrderLoadingAppointmentNotification_In message. In

TM, the status of the items that, according to the message, were loaded, is automatically set to Loaded.

This is custom documentation. For more information, please visit SAP Help Portal.

258


1/14/26, 2:18 PM

3. Once a vehicle (that might be loaded with one or multiple containers or unit load devices) has arrived at the receiving

warehouse, you send the unloading instruction to the warehouse by choosing  Follow-Up

 Send Loading/Unloading

Instruction  or  Load Plan Status

 Set Unload Plan to Finalized  in the freight order or in the freight booking. TM sends

the TransportationOrderLoadingAppointment_Out message to the receiving warehouse management system.

This message contains the current contents of the freight order or freight booking.

4. The warehouse unloads the containers or unit load devices and confirms this to you. TM receives the confirmations with the

TransportationOrderLoadingAppointmentNotification_In message. In TM, the status of the items that,

according to the message, were unloaded, is automatically set to Unloaded.

The TransportationOrderLoadingAppointmentNotification_In message also contains the following

information:

## Discrepancies

## Updated seal information, if this exists

Assignment of forwarding orders that were not originally assigned to the freight booking or the freight order and

that were assigned in the warehouse retroactively

Assignment of items from other freight orders or freight bookings

Items that were split between multiple containers or unit load devices

## References to business transaction documents

This is custom documentation. For more information, please visit SAP Help Portal.

259
