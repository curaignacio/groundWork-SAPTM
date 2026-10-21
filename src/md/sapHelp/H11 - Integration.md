1/14/26, 2:44 PM

Transportation Management (TM)

Generated on: 2026-01-14 14:44:53 GMT+0000

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


1/14/26, 2:44 PM

## Integration

You can integrate Transportation Management (TM) with the following applications:

Application

More Information

## Logistics Integration

Integration of orders and deliveries:

Logistics Integration

Integration with settlement:

Forwarding settlement

## Freight settlement

Advanced Shipping and Receiving

Advanced Shipping and Receiving

## Extended Warehouse Management

Integration with Extended Warehouse Management

## SAP Event Management

Integration with SAP Event Management

## SAP Global Trade Services

Integration with SAP Global Trade Services

## Advanced Shipping and Receiving

Advanced Shipping and Receiving is an integrated, end-to-end process that allows users to send, receive, and transport products.

It supports mixed and multi-warehouse scenarios within one freight order. It helps you, to coordinate the process steps from

arrival of trucks at the gate to the final goods receipt in the warehouse. A truck that has posted arrival at a checkpoint can carry

out both loading and unloading activities at a location, or it can deliver goods at several warehouses at the same location. The

process is also supported for rail freight orders.

Advanced Shipping and Receiving simplifies communication between the Transportation Management (TM), Extended Warehouse

Management (EWM), Stock Room Management (STRM), Inventory Management and Physical Inventory (MM-IM), and Logistics

Execution (LE) application components. You need Materials Management (MM) and Sales and Distribution (SD) to create

transportation requirements.

Communication is simplified by using a harmonized data model, by applying the EDIFACT standard to EDI messages, and by

providing dedicated apps and expanding existing apps and RF transactions for shipping and receiving processes. Information

moves freely between the components and allows users to gain insights into the status of the products during the process.

## Storage Location

The freight order can contain both EWM-managed and IM-managed storage locations, for example at a production location, and

the two storage locations can share a loading point.

In Advanced Shipping and Receiving you can integrate TM with the following warehouse management applications in the same

system:

## Lean Warehouse Management

You can use a very simple warehouse where inventory management takes place solely at storage location level. You need to

create a place holder warehouse that ensures the document flow in TM.

This is custom documentation. For more information, please visit SAP Help Portal.

2


1/14/26, 2:44 PM

## Stock Room Management

You can use Stock Room Management for small warehouse operations and for warehouse operations with low complexity.

## Extended Warehouse Management

You can use EWM for a flexible, automated support for processing various goods movements and for managing stocks in

your warehouse complex.

## Integration Based on Freight Order

The Advanced Shipping and Receiving process is based on the freight order and does not use the EWM transportation unit (TU)

or the EWM vehicle.

Both integration processes, integration based on the freight order or integration based on the EWM transportation unit, can run in

parallel. For warehouse-driven outbound processes, you start in EWM.

For information about restrictions, see SAP Note 3289977

.

For information about the integration of TM with EWM based on the EWM TU and about possible system combinations, see

Integration with Extended Warehouse Management and Integration Based on EWM Transportation Units. This integration is based

on two objects: the TU on EWM-side and the freight order on TM-side.

## Consignment Orders

In the Advanced Shipping and Receiving process you can use consignment orders to group transportation requirements based on

certain criteria, such as the same source and destination location, the same delivery date/time, and the same business partner.

You can create consignment orders using inbound messages as well as manually.

For more information, see Consignment Order.

## Detailed Organization of Loading and Unloading Activities

It is possible to deliver goods to or pick up goods from several warehouses at the same location.

If you have a large warehouse with multiple loading or unloading points and several doors, and you use more than one application

component for warehousing, you can organize your loading and unloading activities in detail, and decide which door, loading or

unloading point can be used by which application component. A loading point or unloading point is defined in master data as a

location and represents a group of doors where goods are delivered or picked up. This allows greater control over where trucks

load or unload cargo.

For more information, see Delivering Goods to Several Warehouses Within a Location and Assignment of STRM Doors to EWM

Doors or Loading Points.

## Integration with decentralized Extended Warehouse Management

Decentralized EWM and TM enables you to conduct transportation logistics solely on the basis of an outbound delivery.

Decentralized EWM and TM is embedded in SAP S/4HANA. The arrangement requires integration between TM and EWM, and

EWM integration with an ERP system in turn. You have the options of carrying out the outbound delivery process as either

transport-driven or warehouse-driven.

Customizing is required. For more information, see Advanced SR for Decentralized EWM and TM.

## More Information

For a setup guide, see SAP note 3225241

.

This is custom documentation. For more information, please visit SAP Help Portal.

3


1/14/26, 2:44 PM

For best practice scenarios, see SAP note 3512117

.

For a detailed end-to-end example process, see End-to-End Process (E2E) for Advanced Shipping and Receiving.

For an overview about available features, see Overview of Features in Advanced Shipping and Receiving.

For information about prerequisites, see Prerequisites for Advanced Shipping and Receiving.

For information about logistics integration (such as, integration of orders, deliveries or scheduling agreements), see

Logistics Integration.

For information about EWM-specific topics in the Advanced Shipping and Receiving process, see Advanced Shipping and

Receiving for Embedded EWM.

For information about decentralized EWM-specific topics in the Advanced Shipping and Receiving process, see Advanced

## Shipping and Receiving for Decentralized EWM and TM

For information about LE-specific topics in the Advanced Shipping and Receiving process, see Integration with Advanced

Shipping and Receiving.

For information about master data replication, see Master Data Replication.

For more information about the freight booking process with Advanced Shipping and Receiving, see Ocean Freight

Bookings for Shippers (Outbound) and Air Freight Bookings for Shippers (Outbound).

## Advanced SR for Decentralized EWM and TM

This deployment option is an outbound delivery-based arrangement in an Advanced Shipping and Receiving setup. The process is

based on outbound deliveries that stem from sales orders.

Decentralized EWM and TM enables you to conduct transportation logistics solely on the basis of an outbound delivery. The

arrangement requires integration with Extended Warehouse Management (EWM), and EWM integration with an ERP system in

turn. You have the options of carrying out the outbound delivery process as either transport-driven or warehouse-driven.

Additionally, to manage foreign-trade activities, ensure ongoing trade compliance, and optimize the cross-border supply chain, you

can integrate your decentralized EWM and TM system with SAP GTS.

Customizing is also required. For more information about Customizing, see Prerequisites for Advanced Shipping and Receiving.

  Restriction

Decentralized EWM and TM enables you to execute the outbound process. Inbound features in Advanced Shipping and

Receiving are not supported by decentralized EWM and TM.

In addition, integration of Dangerous Goods is not supported.

Supported Systems

ERP System:

SAP ERP 6.0 (EhP7 or higher)

SAP S/4HANA

## More Information

This is custom documentation. For more information, please visit SAP Help Portal.

4


1/14/26, 2:44 PM

For more information about the end-to-end outbound process, see End-to-End Process (E2E) for Advanced Shipping and Receiving

(Decentralized).

For more information about integration with SAP GTS, see Integration with SAP Global Trade Services in Advanced Shipping and

Receiving and SAP Global Trade Services.

## Related Information

SAP GTS Integration for the Outbound Process

## Global Trade

Logistics Integration Profile for Decentralized EWM

SAP GTS Integration in Decentralized EWM and TM

## Prerequisites for Advanced Shipping and Receiving

To work with Advanced Shipping and Receiving you must configure some settings in the system.

## Master Data

You have made the following settings in the location master data on the SAP Easy Access screen under  Logistics

Transportation Management

## Master Data

 Transportation Network

 Location

 Location :

You have activated Advanced Shipping and Receiving.

You do this, by indicating in the master data for your source or destination location (location type 1003, shipping point),

that the location is relevant for Advanced Shipping and Receiving. This setting is mandatory.

You have defined a location with location type 1200 (loading point). The setting is mandatory.

## Assignment of Doors

Assign Stock Room Management (STRM) doors or Lean Warehouse Management (Lean WM) doors to Extended Warehouse

Management (EWM) doors or loading points. This setting is mandatory for all scenarios using shared doors and multiple

warehousing components. The setting is not required for a scenario that only uses EWM.

To assign doors in scenarios that only use EWM, open the EWM app Assign Storage Bin to Door from the launchpad.

For more information about prerequisites in EWM, see Prerequisites for Advanced Shipping and Receiving in EWM.

## Customizing Activities

For more information about Customizing settings for Advanced Shipping and Receiving, see Customizing for Transportation

Management under

Integration .

For more information about Customizing settings for decentralized EWM and Transportation Management (TM), see Customizing

for Transportation Management under

## Integration

## Logistics Integration

 Decentralized EWM-TM Integration .

For more information about Business Add-Ins for decentralized EWM and TM, see Customizing for Transportation Management

under  Business Add-Ins (BAdIs) for Transportation Management

## Integration

 Advanced Shipping and Receiving

 Decentralized EWM-TM Integration .

## More Information

This is custom documentation. For more information, please visit SAP Help Portal.

5


1/14/26, 2:44 PM

For a setup guide, see SAP note 3225241

.

For information about LE-specific topics in the Advanced Shipping and Receiving process, see Integration with Advanced

Shipping and Receiving.

For information about master data replication, see Master Data Replication.

## End-to-End Process (E2E) for Advanced Shipping and Receiving

This example describes an end-to-end process for Advanced Shipping and Receiving (Advanced SR) in which both the customer

and the supplier use Transportation Management (TM). In case the systems are not integrated, you can use the inbound or

outbound process separately.

## Prerequisites

For more information, see Prerequisites for Advanced Shipping and Receiving.

Customer Side: Inbound Process

1. Creating a purchasing document

Create a purchasing document in Materials Management (MM), for example, a purchase order or scheduling agreement

(SA), to define which products have to be purchased.

You can use the Create Scheduling Agreement app from the launchpad, for this example process.

Enter necessary data, such as agreement type, purchasing organization and purchasing group (all defined for

integration with TM). Enter a supplier, define validity dates and insert materials that must be procured. In addition, it

is important that you enter a confirmation control key.

In the scheduling agreement item you can add a TM loading or unloading point as additional data. To define where

exactly in the warehouse the goods shall be unloaded.

2. Creating schedule lines in the scheduling agreement

Create schedule lines in the scheduling agreement (usually done by a report).

To create them manually, open the Manage SA Delivery Schedule app from the launchpad.

For every schedule line, the system creates one or more freight units in TM.

3. Creating a scheduling agreement release

Create a scheduling agreement release (usually done by a report).

To create them manually, open the Create Scheduling Agreement Releases app from the launchpad.

The system creates intermediate documents (IDocs) and sends a call off (a release against the outline agreement) to the

supplier’s system.

## Supplier Side: Outbound Process

With the call off, the supplier receives information about the products ordered. In the supplier's system you can display the ordered

products in the corresponding scheduling agreement in Sales and Distribution (SD). In the forecast delivery schedule, the call off

appears as a schedule line.

1. Creating outbound deliveries

This is custom documentation. For more information, please visit SAP Help Portal.

6


1/14/26, 2:44 PM

Create manually or automatically an outbound delivery in Logistics Execution (LE) and Extended Warehouse Management

(EWM).

You can use the Create Outbound Deliveries app from the launchpad.

a. Defining a warehouse

In the delivery, choose a storage location to define the kind of warehouse you want to use, for example, EWM-

managed.

b. Displaying TM information in the delivery

You can use the Manage Outbound Deliveries app from the launchpad.

In the delivery, choose the TM Status tab to display the assigned freight units.

2. Performing warehouse activities

Picking (and possibly packing) is carried out by the warehouse workers. You create handling units (HU) or cross-delivery

HUs.

You can use the Load or Unload Freight Orders app from the launchpad.

For more information about statuses, see Statuses in the Outbound Process and Statuses in Advanced Shipping and

Receiving.

For more information about cross-delivery HUs, see Cross-Delivery Handling Units

All warehouse-relevant tasks are now completed for the freight units. You can start with the TM process: You can plan by

assigning the freight units to a consignment order, to a freight order and then start with the execution.

1. Creating a road freight order

Create a road freight order. You can use the Create Road Freight Order app or Transportation Cockpit app from the

launchpad.

2. Creating consignment orders

Create consignment orders or have the system create them automatically. For more information, see Consignment Order

and Automatic Consignment Building.

You can use the Create Consignment Order app from the launchpad.

3. Check-In process at the gate

You can manage the check-in of the truck in the freight order.

To open the Freight Order app from the launchpad.

After the check-in, you can perform warehouse activities. Again, you can use the Load or Unload Freight Orders app

or the Freight Order app from the launchpad. You can assign doors to the truck (assign loading point and warehouse

door), load cargo, set the execution status accordingly, and post goods movement.

For more information about statuses, see Statuses in the Outbound Process and Statuses in Advanced Shipping

and Receiving.

Post goods movement to update the respective warehouse management system (independent of the kind of

warehouse management you use). The system displays an overall status overview in the road freight order, under

the Advanced SR tab page.

4. System communication using advanced shipping notifications (ASN)

This is custom documentation. For more information, please visit SAP Help Portal.

7


1/14/26, 2:44 PM

The system sends an ASN from the supplier's to the customer's system. This ASN is a web service based on the

consignment order to inform the customer about the expected cargo.

For more information, see Creation or Update of Consignment or Freight Orders on Inbound Messages.

The supplier can also communicate with the carrier, so the carrier is aware of the consignment orders to be transported.

Customer Side: Inbound Process

1. Creating consignment orders using ASN

When the customer's system receives the ASN, it creates a new consignment order including a reference to the external

order number that the supplier's system uses to identify the consignment. The relevant freight units are determined on the

basis of criteria such as purchasing reference, supplier or material number, and assigned to the new consignment order.

The ASN can also be used to update consignment orders.

2. Displaying unplanned freight units

You can display all order-based and unplanned freight units related to the scheduling agreement you created at the

beginning of the process.

You can use the Freight Units Worklist app from the launchpad, and enter the scheduling agreement number under

Original Order.

Once the related ASN message arrives and the systems has assigned the freight units to the consignment order, the freight

units are no longer displayed in your list.

3. Creating inbound deliveries

The system can automatically create an inbound delivery in LE and EWM. The deliveries are blocked.

To view the inbound deliveries, open the Display Inbound Delivery app or the Maintain Inbound Delivery app on the

launchpad.

4. Displaying consignment orders

You can open the document flow of the consignment order to display further information, such as related purchasing

document, assigned freight units and automatically created inbound deliveries. The item structure shows the package

information that has been transferred.

To display information, open the Consignment Orders app from the launchpad.

5. Creating road freight order

Create a road freight order based on consignment order stage.

You can use the Create Road Freight Order or Transportation Cockpit app from the launchpad.

Alternatively, this can be an automatic step when the freight order is sent as load message from the carrier. For more

information, see Creation and Editing of a Consignment Order.

6. Set execution status to Set to Ready for Transportation Execution.

7. Check-In process of trucks at the gate

You can manage the check-in of the truck in the freight order.

To do this, open the Freight Order app from the launchpad.

After the check-in, you can begin with warehouse activities.

You can use the Load or Unload Freight Orders app or Freight Order app from the launchpad.

This is custom documentation. For more information, please visit SAP Help Portal.

8


1/14/26, 2:44 PM

When a truck arrives at the gate you can compare the transportation documents of the truck with the freight order

in system. (Earlier, you might have received planning information via EDI message from the carrier.)

The packages in consignment orders and freight orders that are created using EDI messages are automatically

fixed, to avoid accidental changes. The system automatically sets the load plan status of the packages to "Finalized”.

This means that you can only change the packages if you reset the status.

If the load of the truck differs from the freight order data in the system, you can directly change discrepancies in the

business document. As an example, changing the data is necessary, if the truck contains more, less or other cargo

than expected.

The system can automatically update the referenced predecessor documents of the freight order and keep them

up-to-date. For more information, see Synchronization of Predecessor Documents.

You can assign doors, assign unloading point for a location (with warehouse number and warehouse door) and guide

the truck to the right place.

You can set different statuses for the freight order. Once the gate check-In process is finished, you can set the

warehouse processing status to Ready for Warehouse Processing. The receiving process is now completed, so

warehouse activities, such as unloading or posting goods movement can start. The EWM delivery is unblocked. The

document flow now shows warehouse requests.

For more information about statuses, see Statuses in the Inbound Process and Statuses in Advanced Shipping and

Receiving.

## Displaying Information

You can display the complete document flow in the inbound delivery.

The system displays a status overview in the road freight order, under the Advanced SR tab page. For more

information, see Delivering Goods to Several Warehouses Within a Location.

## More Information

For more information, see the SAP Best Practices for solution scenario at https://me.sap.com/processnavigator/SolS/EARL_SolS-

055

. Navigate to Supply Chain.

For more information about of EWM-specific topics in the Advanced Shipping and Receiving process, see Advanced Shipping and

Receiving for Embedded EWM.

For information about LE-specific topics in the Advanced Shipping and Receiving process, see Integration with Advanced Shipping

and Receiving.

For more information about processes in the integration with SAP Global Trade Services, see Integration with SAP Global Trade

Services.

## Related Information

Correction of Errors in Business Documents

Example Checks to Find Errors in Business Documents

## Transport-Driven Execution

A transport-driven process prioritizes transportation planning while warehouse activities are blocked until manually released.

This is custom documentation. For more information, please visit SAP Help Portal.

9


1/14/26, 2:44 PM

A transport-driven outbound process takes place in the context of internal logistics integration between Transportation

Management (TM) and Delivery Management as well as TM and Extended Warehouse Management (EWM), Lean Warehouse

Management, and Stock Room Management. A transport-driven execution prioritizes transportation planning. After delivery

creation, the delivery is blocked for warehouse execution until transportation preparations have begun and a block on warehouse

activities has been removed. When you release the delivery for warehouse processing, it is then unblocked, and warehouse

execution can start.

You must set the warehouse processing status to Ready for Warehouse Processing manually. Consequently, the warehouse

receives the information needed to plan and execute its warehouse activities accordingly.

## Prerequisites

You have defined the following criteria for the determination of outbound deliveries that are relevant for transport-driven

processes:

Warehouse Number

Shipping Point

## Delivery Type

When a delivery meets the criteria set in the Customizing activity, the transport-driven process is automatically enabled.

For more information, see Customizing for Transportation Management under

## Integration

 Logistics Integration

## Internal TM

## Component Integration

 Determine Relevance for Transport-Driven Process .

To afford you more flexibility, we provide a Business Add-In (BAdI). With this BAdI, you can establish your own criteria for the

determination of transport-driven deliveries when saving a Delivery Management delivery.

For more information, see Customizing for Transportation Management under  Business Add-Ins (BAdIs) for Transportation

Management

## Integration

## Advanced Shipping and Receiving

 BAdI: Change of Data Related to Transport-Driven Process .

Executing a Transportation-Driven Process

1. Creating an Outbound Delivery

Start with an outbound delivery. Based on Customizing, the system determines whether a delivery is relevant for the

transport-driven scenario.

At this stage, the Warehouse Execution Status of the delivery is set to Blocked.

2. Setting the Warehouse Processing Status to Ready for Warehouse Processing

Create a freight order in the Create Road Freight Order app in TM.

Up to now, the delivery status is set to Blocked so information about transportation planning is not transferred to the

delivery.

You can change the status to Ready for Warehouse Processing in the freight order (FO) using the Edit Road Freight Order

app. Alternatively, you may choose to trigger warehouse activities directly from the freight unit (FU) by setting the

warehouse processing status in the FU to Ready for Warehouse Processing.

In a transport-driven scenario, the default settings require you to execute the trigger manually so that the blocking of

warehouse processing is determined by the executer.

3. Enabling and Halting Warehouse Processing

This is custom documentation. For more information, please visit SAP Help Portal.

10


1/14/26, 2:44 PM

It is possible to operate both of the Advanced Shipping and Receiving (Advanced SR) scenarios: the default Advanced SR

warehouse-driven scenario and the Advanced SR transport-driven scenario. The transport-driven scenario is an extension

of the warehouse-driven processes. Hence, once a block is removed, warehouse activities can be carried out as usual.

If, for any given reason, warehouse execution must be stopped, you can reverse the Ready for Warehouse Processing

status as long as execution has not yet begun.

4. Updating Deliveries

When you change the status of an order to Ready for Warehouse Processing, carrier, delivery date, and loading point are

transferred to the delivery.

## Compliance Checks

In transport-driven cases where compliance checks need to be conducted, processing is blocked until a successful compliance

check is carried out. You can set the status to Ready for Warehouse Processing manually once compliance is met. Should a

second compliance check be required, the Ready for Warehouse Processing status is automatically reverted to Not Started.

Similarly, when compliance is later met, the status is automatically updated, and that information is forwarded to Delivery

Management and retrieved by EWM.

Once warehouse activities begin, it is no longer possible to revert the status to Not Started.

You can find the compliance status in the Edit Freight Unit app.

## Customer Returns: Inbound Process

This example describes an inbound process for handling customer returns in Advanced Shipping and Receiving (Advanced SR).

## Prerequisites

For more information, see Prerequisites for Advanced Shipping and Receiving.

Supplier Side: Inbound Process

1. Creating a customer returns order

Create a customer returns order in Sales (SD), to define which products are being returned.

2. Creating freight units

For every schedule line, the system creates one or more freight units in TM.

Customer Side: Outbound Process

The return is processed at the customer.

## Supplier Side: Inbound Process

1. Creating consignment orders using an advanced shipping notification (ASN)

When the supplier's system receives the ASN, it creates a new consignment order. The relevant freight units are

determined on the basis of criteria such as returns reference (customer returns order number), supplier or material

number, and assigned to the new consignment order. The ASN can also be used to update consignment orders.

This is custom documentation. For more information, please visit SAP Help Portal.

11


1/14/26, 2:44 PM

2. Displaying unplanned freight units

You can display all order-based and unplanned freight units related to the customer returns order you created at the

beginning of the process.

You can use the Freight Units Worklist app from the launchpad, and enter the customer returns order number under

Original Order.

Once the related ASN arrives and the system has assigned the freight units to the consignment order, the freight units are

no longer displayed in your list.

3. Creating returns deliveries

The system can automatically create a delivery for customer returns in Logistics Execution (LE) and Extended Warehouse

Management (EWM). The deliveries are blocked for warehouse execution in a first step.

To view the customer returns deliveries, on the launchpad open the Change Outbound Delivery app in LE or the Maintain

Inbound Deliveries app in EWM.

4. For all subsequent steps, please refer to End-to-End Process (E2E) for Advanced Shipping and Receiving.

End-to-End Process (E2E) for Advanced Shipping and Receiving
(Decentralized)

Decentralized EWM and TM is an outbound delivery-based arrangement embedded in the same system. The process must be

executed based on a sales order.

Decentralized EWM and TM conducts transportation planning and execution based exclusively on outbound deliveries. Outbound

deliveries reach Transportation Management (TM) via Extended Warehouse Management (EWM), and you have the ability to

conduct the process as either warehouse-driven or transportation-driven.

Additionally, you can carry out compliance checks and export declarations by integrating your system with SAP Global Trade

Services. For more information, see SAP GTS Integration in Decentralized EWM and TM.

Communication between TM and an ERP system is routed via EWM.

## Prerequisites

For more information, see Prerequisites for Advanced Shipping and Receiving.

## Decentralized Sample Process

## Decentralized EWM and TM Outbound Process and Integration

The placement of an order leads to transportation requirements. As a result, the shipper creates an outbound delivery.

1. Creating an Outbound Delivery

In Logistics Execution (LE), create an outbound delivery from a sales order.

To create an outbound delivery, open the Create Outbound Delivery app from the launchpad.

2. Creating an Outbound Delivery Order

The ERP system communicates the outbound delivery to the decentralized system automatically, where EWM creates an

outbound delivery order.

This is custom documentation. For more information, please visit SAP Help Portal.

12


1/14/26, 2:44 PM

EWM replicates the outbound delivery order to TM. And TM creates freight units (FU) based on the outbound delivery order.

3. Planning and Processing

With FUs, TM can then propose a transportation plan.

From this point onward, you can conduct activities that either prioritize warehouse execution or transportation planning.

## Transport-Driven Process

In a transport-driven process, transportation planning takes precedence.

1. Performing Transportation Planning

EWM creates an outbound delivery order from an outbound delivery from Delivery Management. The outbound delivery

order is blocked for processing until transportation planning is complete.

At this stage, create a road FO and insert the FUs in the order.

You assign FUs to a freight order (FO) by entering the outbound delivery order, delivery, or FU number.

To create an FO, open the Create Road Freight Order app or Transportation Cockpit app from the launchpad.

2. Releasing the Freight Order

Next, you change the status of the FO to Set to Ready for Warehouse Processing.

With the change of status in TM from In Process to Ready for Warehouse Processing, the outbound delivery order is

released, and the execution of warehouse activities can proceed.

For more information about the transport-driven process, see Transport-Driven Execution.

3. Performing Warehouse Activities

TM automatically communicates the change in status to EWM.

Warehouse specialist can proceed with warehouse activities as described below.

## Warehouse-Driven Process

In a warehouse-driven process, warehouse activities take precedence.

1. Performing Warehouse Activities

Upon creation of an outbound delivery order, the warehouse can proceed with its activities. Warehouse workers carry out

activities such as picking and packing.

With the completion of warehouse activities, EWM communicates the delivery status to TM.

For more information about statuses, see Statuses in the Outbound Process and Statuses in Advanced Shipping and

Receiving.

2. Performing Transportation Logistics

Once warehouse activities are complete, you can conduct transportation planning and execution in TM.

Once transportation planning is complete, you can set the status to Ready for Shipping in the EWM Outbound Delivery

Order.

## Execution

Finally, transportation of goods can take place.

This is custom documentation. For more information, please visit SAP Help Portal.

13


1/14/26, 2:44 PM

1. Reporting Truck Arrival and Departure

In your FU, you will find the warehouse status is now set to Completed. Also, information regarding the package is now

available. On the Item tab, you will find information such as the package ID and packaging.

Navigate to the Execution Status tab to change the status to Ready for Transportation Execution.

With the arrival of the truck, you can set the status in TM to Set to Arrived, and after, Checked In on the Overview tab.

Loading activities are recorded in EWM. At the gate, the warehouse operators load the goods onto the truck.

To set delivery statuses, open the Load or Unload Freight Orders app from the launchpad.

To manage the check-in and -out of the truck, open the Edit Freight Order app from the launchpad.

Change the Goods Movement status to Goods Issued to report the truck's departure.

## More Information

For more information, see the SAP Best Practices solution scenario at https://me.sap.com/processnavigator/SolS/EARL_SolS-

055

. Navigate to Supply Chain.

## Related Information

Prerequisites for Advanced Shipping and Receiving

Overview of Features in Advanced Shipping and Receiving

Advanced Shipping and Receiving for Decentralized EWM and TM

## Overview of Features in Advanced Shipping and Receiving

The table gives an overview of features in the Advanced Shipping and Receiving process.

  Remember

In a decentralized EWM and TM deployment, only outbound processes and functions are enabled.

## Feature

Good to Know

## More Information

Delivering goods to several warehouses

You can give detailed information to a

Delivering Goods to Several Warehouses

within a location

delivery truck driver about warehouses

## Within a Location

within the company premises. You need this

information when a truck driver has to

deliver goods to or pick up goods from

several warehouses at the same location.

Detailed organization of large warehouses

You can organize your loading and

Assignment of STRM Doors to EWM Doors

unloading activities in detail and decide

or Loading Points

which door, or which loading or unloading

point is used by which warehousing

component. This allows greater control over

where trucks load or unload cargo.

Late changes to capacity documents

You can make changes to a capacity

Late Changes to Capacity Documents

document, for example, a road freight order,

even after the execution at the stop in the

This is custom documentation. For more information, please visit SAP Help Portal.

14


1/14/26, 2:44 PM

## Feature

Good to Know

## More Information

capacity document has started or been

completed.

## Status management

Several statuses are used in Advanced

Statuses in Advanced Shipping and

Shipping and Receiving for the inbound and

## Receiving

outbound processes.

Statuses in the Inbound Process

Statuses in the Outbound Process

## Consignment order

A consignment order represents a business

Consignment OrderCreation and Editing of

document that you can use to group several

a Consignment OrderAutomatic

transportation requirements based on

## Consignment Building

certain criteria, such as the same source

and destination location, the same delivery

date/time, and the same business partner.

You can create consignment orders

automatically using inbound messages as

well as manually.

Creating or updating of consignment orders

Your business partner can send you a

Creation or Update of Consignment or

using ASN

consignment order or freight order as an

Freight Orders on Inbound Messages

advanced shipping notification (ASN) using

EDI communication. The related freight

units are determined and assigned to the

new consignment order.

Creation and Editing of a Consignment

## Order

## Freight unit determination

Relevant freight units are determined on

Creation or Update of Consignment or

the basis of certain criteria (such as

Freight Orders on Inbound Messages

supplier or material number).

Using web services for external planning

You can use TM output management to

Web Services for External Planning

send A2A or B2B messages. TM output

## Scenarios

management is based on the Post-

Processing Framework (PPF) which is

integrated in the Business Objects

Processing Framework (BOPF).

Creating freight orders using EDI messages

Your business partner can send you a

Creation or Update of Consignment or

freight order (bordero, bill of lading) with

Freight Orders on Inbound Messages

assigned consignment orders using EDI

communication. The related consignment

orders are determined and assigned to the

new freight order.

Freight unit split and mass data changes

When you receive an external delivery note

Freight Unit Split and Mass Data Changes

number from a supplier, you can change it

in business documents, such as freight

orders or consignment orders, with or

without an FU split.

Correction of errors in business documents

If the inbound consignment order contains

Correction of Errors in Business Documents

errors, it is usually still saved as a document

in TM. The errors are displayed on the

Document Errors tab page and can be

corrected here or in the corresponding

worklist.

This is custom documentation. For more information, please visit SAP Help Portal.

15


1/14/26, 2:44 PM

## Feature

More Information

Good to Know

## With the report

/SCMTMS/TOR_RETRY_ERRORS you can

automatically resolve document errors in

freight orders without opening and retrying

each freight order manually. You can resolve

reference errors to an unknown

consignment order that is now available in

the system.

Synchronization of predecessor documents

For the inbound process you can enable the

Synchronization of Predecessor Documents

synchronization of predecessor documents

referenced in a consignment order or

freight order. You can, for example, change

the data of a freight order during the check-

in process of a truck at the gate and update

the predecessor documents with the

changes.

Handling units (EWM), package ID (TM),

In the inbound part of the Advanced

and external package ID (TM)

Shipping and Receiving process, the

package information received from the

vendor (either via ASN or entered manually

in the system, for example, during the

check-in process) is used to create handling

units. In the outbound part, the handling

unit information received from the

warehouse is used to create package

information. Throughout the process the

integration ensures that all information is

synchronized between TM and the

warehouse.

A vendor provides a package ID and

confirms that it is a standardized number,

such as a global transport label (GTL) or a

serial shipping container code (SSCC). The

system checks the number to ensure that it

is unique across systems and displays it as

a package ID in a business document, such

as a road freight order or a consignment

order. If the vendor says that the package ID

is not a standardized number, then the

system displays it as an external package

ID. The system also creates a unique,

standardized number for the external

package ID and displays it in the Package

ID field. This is the number that is used for

handling units in the warehouse.

Auxiliary packaging material

The system includes auxiliary packaging

Use of Auxiliary Packaging Materials

materials, that have been defined in TM

business documents, in the corresponding

handling units when creating LE and EWM

deliveries.

Serial numbers and batch management

You can store and display information about

Use of Batches and Serial Numbers

materials, such as batch information and

serial numbers, in business documents.

This is custom documentation. For more information, please visit SAP Help Portal.

16


1/14/26, 2:44 PM

## Feature

Good to Know

## More Information

This information is sent by the supplier. You

can also transfer this information to the

inbound deliveries or receive them from the

outbound deliveries. In the consignment

and road freight order, you can manually

enter or edit the batch and serial number

information.

## Deliveries

You can split deliveries from TM across a

## Delivery Split

number warehouse management

applications. Also, you can delete deliveries

Delivery Deletion

created in LE from TM.

Displaying detailed warehouse information

In the road freight order, under the

Delivering Goods to Several Warehouses

(on the user interface)

Advanced SR tab page, you can see the

## Within a Location

planned and actual warehouse details

where a truck has loaded or unloaded

goods. This tab page is for the product in

the road freight order.

Integration with SAP Global Trade Services

Integration between TM and SAP GTS

Integration with SAP Global Trade Services

(SAP GTS)

enable you to conduct customs processes

from TM.

SAP GTS Integration for the Outbound

## Process

SAP GTS Integration for the Inbound

## Process

Statuses in the Integration with SAP GTS

(Inbound Process)

Statuses in the Integration with SAP GTS

(Outbound Process)

Performing warehouse activities in EWM

To perform warehouse activities, you can

Load or Unload Freight Orders

app (on the user interface)

use the Load or Unload Freight Orders app.

Subcontracting a purchase order

Integration between MM and TM enable you

Subcontracting of Purchase Order

to subcontract purhase orders.

Air freight bookings for shippers

You can model an air freight booking

Air Freight Bookings for Shippers

process for shippers with message

(Outbound)

exchange between the shipper and the

carrier in which consignment orders play an

essential part.

Ocean freight bookings for shippers

You can model an ocean freight process

Ocean Freight Bookings for Shippers

with container units and message exchange

(Outbound)

between the shipper and the carrier.

Cross-delivery handling units

The integration of TM with EWM based on

Cross-Delivery Handling Units

outbound deliveries supports cross-delivery

handling units (HU) in the outbound

process.

Delivering Goods to Several Warehouses Within a Location

This is custom documentation. For more information, please visit SAP Help Portal.

17


1/14/26, 2:44 PM

In the Advanced Shipping and Receiving process in Transportation Management (TM), you can handle mixed and multi-warehouse

scenarios within one road freight order. This means that you can give detailed information to a delivery truck driver about

warehouses within the company premises, which is necessary when a truck driver has to deliver goods to or pick up goods from

several warehouses at the same location.

At the gate, the truck driver gets the information about where to deliver the goods, either from predecessor documents or on the

spot.

## Features

To provide more information about the warehouse to facilitate transportation execution in the Advanced Shipping and Receiving

process, you can use the following features:

## Warehouse Loading Stops and Warehouse Unloading Stops

You or the system can define the exact warehouse number, loading point or unloading point, and warehouse door that the truck

needs to drive to. This information is contained in a more detailed loading or unloading stop called the warehouse loading stop (for

the source location) or warehouse unloading stop (for the destination location). For intermediate stops, if the warehouse loading

stop and the warehouse unloading stop are identical, that is, they have the same warehouse number, loading point or unloading

point, and warehouse door, you can define a Warehouse Unloading/Loading Stop. You can see the warehouse loading stop or

warehouse unloading stop on the Overview tab page. As a prerequisite, you need to configure this in the Customizing for the

Overview hierarchy type. For more information, see Customizing for Transportation Management under  Freight Order

## Management

 Define Hierarchical Views for Business Documents .

The warehouse loading stops and warehouse unloading stops can be added to business documents, such as road freight orders,

consignment orders, freight units, and transportation units. All items of a road freight order must be assigned to a warehouse

loading stop or warehouse unloading stop and its assigned loading point or unloading point and warehouse door. A loading point or

unloading point is defined in master data as a location and represents a group of doors where goods are delivered or picked up.

This allows greater control over where trucks load or unload cargo.

You can manually assign items to different warehouse loading stops or warehouse unloading stops if the warehouse number of the

item matches the warehouse number of the warehouse loading or unloading stop.

You or the system can create warehouse loading stops or warehouse unloading stops at stop level in the following ways:

The system can derive the stops in the road freight order based on the information provided in the predecessor documents,

such as a sales order or a scheduling agreement.

You can manually create or change the stops in the capacity document, for example, a road freight order, in the Loading

Details or the Unloading Details tab page in the Overview section. You might need to do so if, for example, the planned

loading point and warehouse door can no longer be used because they are occupied. However, the predecessor document

is not updated with this information.

In the hierarchy, a loading stop or unloading stop may have one or more substops (warehouse loading stops or warehouse

unloading stops that are defined as substops). You can assign documents such as consignment orders, freight units, and packages

to the warehouse loading stops or warehouse unloading stops.

You can update the derived warehouse loading stops or warehouse unloading stops with information about the warehouse door

that was actually used.

## Handling Warehouses with Multiple Warehousing Components

If you have a warehouse where you use two different components to manage two different parts of the warehouse, for example,

Stock Room Management (STRM) and Extended Warehouse Management (EWM), you can determine the assignment of doors and

loading or unloading points for loading or unloading activites.

This is custom documentation. For more information, please visit SAP Help Portal.

18


1/14/26, 2:44 PM

You can assign the STRM door to the EWM door. You can also assign STRM doors to loading points or unloading points.

For more information, see Assignment of STRM Doors to EWM Doors or Loading Points.

## Detailed Warehouse Information

In the road freight order, under the Advanced SR section, you can see the planned and actual details for warehouses where a truck

has loaded or unloaded goods. This tab page is for the product in the road freight order.

When a truck arrives at the gate and is checked in, in the Planned section, the system displays information derived from

predecessor documents about where the item is planned to be loaded or unloaded. This includes, for example, the warehouse

number and the loading point or unloading point.

If the planned loading points or unloading points or doors cannot be used, you can enter new loading points or unloading points or

doors in the Overview section. In the Actual section, the system displays the actual assignment to warehouse loading stops or

warehouse unloading stops.

Warehouse Loading Stops and Warehouse Unloading Stops in the Transportation Cockpit

Warehouse numbers, loading points and unloading points, and warehouse doors are also displayed for road freight orders,

consignment orders, freight units, and transportation units in the transportation cockpit.

If there are multiple warehouse loading stops or warehouse unloading stops beneath a loading stop or unloading stop, the value

Multiple is displayed in the corresponding fields and a quick view lists the individual warehouse numbers, loading points or

unloading points, and warehouse doors.

  Note

In the transportation cockpit, only the current warehouse loading stop or warehouse unloading stop is displayed. This means

that, if you have changed the warehouse loading stop or warehouse unloading stop in TM, the original warehouse loading stop

or warehouse unloading stop from the sales order, for example, is not displayed.

You can do various manual planning actions, such as:

## Inserting a warehouse loading stop or warehouse unloading stop

The new substop is then displayed as a separate line (hierarchy level) in the location hierarchy.

## Changing a warehouse loading stop or warehouse unloading stop

A dialog box is displayed in which you can change the warehouse number, the loading point or unloading point, and the

warehouse door.

Assigning a stage of a requirement document to a capacity document or reassigning a planned stage of a requirement

document to a capacity document

When assigning or reassigning a stage, the system considers warehouse loading stops and warehouse unloading stops.

## Package Building

If you build packages for these business documents and the items have different warehouse numbers or loading points or

unloading points, then these items are packaged in different mixed packages. This is also the case if no warehouse number, loading

point, or unloading point has been defined for an item.

Assignment of STRM Doors to EWM Doors or Loading Points

This is custom documentation. For more information, please visit SAP Help Portal.

19


1/14/26, 2:44 PM

In the Advanced Shipping and Receiving process in Transportation Management (TM), if you have a large warehouse with multiple

loading points or unloading points and multiple doors, and you use more than one application component for warehousing, such

as Stock Room Management (STRM), Lean Warehouse Management (Lean WM), and Extended Warehouse Management (EWM),

you can organize your loading and unloading activities in more detail by deciding which warehouse door or loading point is used by

which application component.

To do so, open the Assign STRM Doors to EWM Doors or Loading Points app from the launchpad. Alternatively, on the SAP Easy

Access screen choose  Logistics

 Transportation Management

## Master Data

 Transportation Network

 Location

## Assign

STRM Doors to EWM Doors or Loading Points .

You can make the following assignments using this app:

If you use both an STRM or Lean WM warehouse and an EWM warehouse in one warehouse building, and they share a

common warehouse door, you must set up the system to select the EWM warehouse door for loading or unloading

activities. You can do so by assigning the STRM or Lean WM warehouse door to the EWM warehouse door. When you do

this, the system uses the EWM warehouse door as the main door for loading or unloading activities and automatically

replaces the STRM or Lean WM warehouse door with the assigned EWM door in the warehouse loading stop or warehouse

unloading stop details. For example, one part of your warehouse uses an STRM system for bulk goods and the other uses an

EWM system for liquids. They share a common door for some of their activities. Using the Assign STRM Doors to EWM

Doors or Loading Points app, you assign the STRM door to the EWM door, ensuring that in the system the door used for

unloading liquids is also used for bulk goods.

If you want to change the warehouse door that is assigned for loading or unloading activities, you can do so only if it is

shared by the same pair of EWM and STRM or Lean WM warehouses. For example, you cannot assign a door that is only

used by EWM or that is used by the same EWM warehouse but by a different STRM warehouse.

If the EWM warehouse door already has a loading point or unloading point assigned to it, the system also uses the EWM

loading point or unloading point as the main one and overwrites any existing assignment.

You can assign STRM or Lean WM warehouse doors to loading points or unloading points if they are not already assigned to

one.

  Note

The following restrictions apply:

If you use a Lean WM warehouse, you need to create a placeholder warehouse with one loading point or unloading point

and one warehouse door.

You can only assign one STRM or Lean WM warehouse door to one EWM warehouse door. The same EWM warehouse

door cannot be assigned to multiple STRM or Lean WM warehouse doors.

You can only assign one loading point or unloading point to an STRM or Lean WM warehouse door.

## Late Changes to Capacity Documents

In the Advanced Shipping and Receiving process in Transportation Management (TM), you can make changes to a capacity

document, for example, a road freight order, even after the execution at the stop in the capacity document has started or been

completed.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

20


1/14/26, 2:44 PM

The following decribes a situation where you need to correct a capacity document to reflect what is actually happening, or has

already happened. If you need to insert extra locations or stops in a capacity document, please see Document Assignment

When Execution Has Already Started.

## Features

During the loading or unloading process at the warehouse, sometimes additional cargo items that are not assigned to the road

freight order are loaded on the truck or unloaded at the warehouse along with the items that are already assigned. This results in a

mismatch between the information in the road freight order and what actually happened at the time of loading or unloading. To

correct this, you can update the road freight order by assigning the additional items to the same warehouse loading stop or

warehouse unloading stop at which the other items were loaded or unloaded. For example, you can add one or more requirement

documents to the warehouse unloading stop in the road freight order, even after the truck has departed from that stop. You need

to do this, for example, for charge calculation or settlement with the carrier.

## Assignment of a New Requirement Document

You can assign a requirement document, such as a consignment order or freight unit, to the road freight order when the truck has

arrived at the gate or stop but the processing of items has not yet started. In this case, the statuses of the new items match the

statuses of the other items in the road freight order.

However, if you add a requirement document after the truck has loaded or unloaded the goods at the warehouse loading stop or

warehouse unloading stop, has checked out, or has departed, then the status of the items added later doesn't match the status of

the stop and of the other items in the road freight order. In this case. the system creates a document error. You cannot revoke the

status of the stop in the road freight order. But you can update the statuses of the items in the new requirement document to

match it.

To do so, see the Document Errors tab page in the road freight order. A document error is created and the Document Error tab

page is enabled. To correct these errors, you can use the actions available next to the description of the error. After you have

corrected the error, the Document Errors tab page is disabled.

  Note

The Document Error tab page is enabled even if you haven't made the corresponding settings, that is, you haven't selected the

Enable Saving of Documents with Errors value in the Handling of Incorrect Inbound Messages field in the Customizing for the

freight order type. For more information, see Correction of Errors in Business Documents.

When you add a new freight unit to a road freight order that is relevant for a customs process, you must enter the same external

delivery note number for the freight unit that was used for one of the other items of the road freight order. In the inbound process,

the freight unit is added after the execution at the stop is completed; therefore, the TM system then sends the customs-relevant

information about the products in the freight unit to the integrated SAP Global Trade Services (SAP GTS) system.

## Unassignment of a Requirement Document

You can unassign a requirement document from a capacity document after the execution at the stop has started but before goods

movement is posted. You need to do this if, for example, in the outbound scenario you have a consignment order that could not be

loaded at the warehouse loading stop as planned but that, according to the road freight order, is loaded.

If you want to remove a requirement document from the capacity document after loading is completed and the check-out is

already reported, the following prerequisites must be met to allow the late removal process:

The warehouse loading stop must have the handling execution status Not Loaded.

The status of the corresponding warehouse loading stop must be reverted to Not Loaded. This will not affect the logistical

execution status of the document, that is, the check out and later events and statuses will not be reverted. This creates a

This is custom documentation. For more information, please visit SAP Help Portal.

21


1/14/26, 2:44 PM

document error indicating the temporary status mismatch between the warehouse loading stop, where loading is not

completed, and the already checked out shipping point.

The items may not have goods movement posted or requested.

Goods movement postings for the related items must be cancelled.

The items may not have an export declaration requested or approved

Any approved or requested export declarations must be cancelled.

The items may not have a customs invoice created.

Any existing customs invoices need to be cancelled.

Now, the loading of the items can be reverted by setting the handling execution status back to Not Loaded and the requirement

can be unassigned from the capacity document. This can also be done by reporting the loading completion of the corresponding

warehouse loading stop, as this will also remove all requirements that do not have the handling execution status Loaded.

The system performs the following steps when you unassign the requirement document:

It sets the handling execution status to Not Loaded for all the items of the requirement document that is unassigned.

In the unassigned requirement document, the system revokes all Loading and Unloading events related to these items.

## Examples

The following examples describe a scenario where a requirement document is assigned to a capacity document after the truck has

departed, and another scenario where you correct a requirement document error resulting in the late processing of the document.

Late Assignment of Requirement Documents

The following is an example for the inbound scenario:

A truck arrives at the company premises with a freight unit assigned to its road freight order. The road freight order items have a

warehouse unloading stop defined. After you set the handling execution status to Checked In, the truck drives to the warehouse

unloading stop to unload the goods. While unloading, the truck driver discovers that there is an extra pallet on the truck that is not

assigned to the road freight order. The truck driver nevertheless unloads this pallet at the stop along with the other items, checks

out, and departs. You update the status of the road freight order accordingly.

In the system, you now want to assign the additional pallet that was unloaded to the warehouse unloading stop in the road freight

order, after the truck has departed. You can assign a new freight unit to the road freight order. But the statuses of the new item do

not match the statuses of the rest of the items assigned to the stop that have already been processed. For example, the handling

execution status of the new item is Not Unloaded while the other items have the status Unloaded. The system creates document

errors on the Document Errors tab page.

If the inbound stop of the freight document has the handling execution status Unloaded or a status value that follows Unloaded in

the inbound process, such as Checked Out or Departed, then on the Document Errors tab page, you must use the actions

available next to the error description to do the following:

1. You set the warehouse processing status of the item to Ready for Warehouse Processing. However, to do so the item in the

requirement document must be assigned to a delivery. It must be based on inbound documents like the inbound delivery.

You therefore need to first create a delivery by choosing  Follow Up

 Create Deliveries .

When you set the status of the item to Ready for Warehouse Processing, the inbound delivery for the item to be delivered

at that stop gets the status In Yard (for Extended Warehouse Management (EWM) deliveries) or In Plant  (for Logistics

Execution (LE) deliveries).

This is custom documentation. For more information, please visit SAP Help Portal.

22


1/14/26, 2:44 PM

Once the delivery is created, you see the action to post goods movement on the Document Errors tab page.

2. You set the handling execution status of the item to Unloaded.

3. You post goods movement.

The statuses of all the items in the road freight order are now consistent.

## Document Errors in Requirement Document

The following example describes how an Execution Block can be overruled to process the capacity document while the errors

contained in one of the requirement documents in that capacity document are corrected.

You receive a road freight order with several consignment orders assigned to it via an EDI message. One of the consignment orders

has document errors. It has a master data error because the product ID is wrong and a reference error that indicates that the

system could not assign the freight unit to the consignment order. The system sets an Execution Block for the corresponding stop

in the road freight order. As a result, you cannot process the road freight order at that stop and the truck is not allowed to enter the

yard and start the execution at the warehouse unloading stop. However, you can overrule the block for the stop in the road freight

order on the Blocking Information tab page.

Once you overrule the block, the consignment orders without document errors can be processed and the truck can drive into the

yard and unload the cargo. The statuses of the consignment orders are set as they are processed, and the truck departs. You don't

need to unassign the consignment order that has an error from the road freight order in the system. The cargo assigned to this

consignment order is unloaded already and you just need to update the document in the system.

You do the following to process the consignment order:

1. You correct the errors in the consignment order. On the Document Errors tab page, you correct the master data error by

entering the correct material. This also automatically resolves the reference data error and a freight unit is assigned to the

consignment order. The consignment order is automatically assigned to the road freight order.

2. You now have a consignment order assigned, but its statuses do not match the statuses of the road freight order. You can

create a delivery by choosing  Follow Up

 Create Deliveries .

Using the actions available on the Document Errors tab page in the road freight order, you set the warehouse processing

status to Ready for Warehouse Processing, set the handling execution status of the item to Unloaded, and post goods

movement.

The statuses of all the items in the road freight order are now consistent.

## Statuses in Advanced Shipping and Receiving

The table below lists the statuses used in the Advanced Shipping and Receiving process in Transportation Management (TM) and

links them to their descriptions in the Explanation of Statuses section below the table.

Statuses

## Status

## Status Values

Handling Execution Status

Cargo Ready for Loading

Arrived

Checked In

## Loaded

This is custom documentation. For more information, please visit SAP Help Portal.

23


1/14/26, 2:44 PM

## Status

Warehouse Door Status

Warehouse Processing Status

Status Values

Unloaded

Checked Out

## Departed

Arrived at Door

Departed from Door

Not Determined

## Not Started

Ready for Warehouse Processing

In Process

Completed

## In Transit

Partially Ready for Warehouse Processing

Partially In Process

Partially Completed

## Partially In Transit

Goods Movement Status (see below, under Statuses in the Goods

Not Relevant

Movement Process)

Not Processed Yet

Partially Processed

## Completely Processed

Goods Movement Processing (see below, under Statuses in the

No Processing Requested

Goods Movement Process)

Cancellation Requested

## Posting Requested

Posting/Cancellation Failed

Posting Partially Requested

Cancellation Partially Requested

Posting/Cancellation Requested

Posting/Cancellation Partially Requested

## Explanation of Statuses

The statuses used in the Advanced Shipping and Receiving process are explained below:

## Handling Execution Status

For more information about the handling execution statuses, see Explanation of Statuses of Business Documents.

This is custom documentation. For more information, please visit SAP Help Portal.

24


1/14/26, 2:44 PM

For more information about checks for handling execution status-relevant events, see Checks for Handling Execution Status-

Relevant Events.

## Warehouse Door Status

This status indicates whether a warehouse door is currently physically occupied by a truck or is available to load or unload goods.

You can get an overview of warehouse doors that are presently available and can be used.

You can set the warehouse door status manually or the system sets it automatically at the level of the warehouse loading stop or

warehouse unloading stop. If you have set the status to the wrong value by mistake, you can reverse the changes that you have

made.

The status has the following values:

## Arrived at Door

You can set this status value to indicate that the truck has reached the warehouse door to load or unload goods and that

the door is now occupied. The door cannot be used by other trucks until the loading or unloading is completed and the door

is made available again.

You can only set the status value if the door is not currently occupied. You can only set it for one warehouse loading stop or

warehouse unloading stop at a time and only if the handling execution status of the stop is set to Checked In. However, if

the same door is being used for both loading and unloading activities, then the door of the warehouse loading stop and the

warehouse unloading stop is set to Arrived at Door at the same time. You cannot set the status to Arrived at Door for the

same door at the same time in another business document.

However, if you select the Allow Multiple Door Assignments checkbox for a loading point in the Define Location app, the

system does not check if a warehouse door has the Arrived at Door status in other business documents. The warehouse

door for that location is always available, even if it is occupied and has the Arrived at Door status in another business

document. This can be used if, for example, you have created a placeholder warehouse door.

After you set the Arrived at Door status, the system reports the event Arrival at Door.

## Departed from Door

You can set this status value to indicate that the truck has finished loading or unloading the goods and has driven away

from the warehouse door. The door is available again and can be used by another truck.

The system automatically sets the Departed from Door status if you directly set the handling execution status to Checked

Out or Departed.

After you set this status, the system reports the event Departure from Door.

## Warehouse Processing Status

You can use the warehouse processing status to track the progress of an item or business document through the warehouse and

to determine the next steps in the transportation process based on the status. This status is from the perspective of TM. For

information on the warehouse processing status from the perspective of Extended Warehouse Management (EWM), see Transport

Plan.

In the inbound process, the warehouse processing status helps control the handover of responsibility for the cargo items from TM

to the warehouse. In the outbound process, this status can be used to track if the cargo items are ready to be shipped from the

perspective of the warehouse. Once the items are ready to be shipped, TM can start the loading process or trigger follow-on

processes, such as subcontracting and requesting customs declarations.

The following warehouse processing status values are available on the item level. They apply to single items or single documents.

Note that the status values have a slightly different connotation in the inbound and outbound processes.

This is custom documentation. For more information, please visit SAP Help Portal.

25


1/14/26, 2:44 PM

## Not Determined

This status value is the initial value that the system displays in both the inbound and outbound process.

## Not Started

This status value indicates that the warehouse has not started processing the cargo items. Depending on the loading

direction, one of the following scenarios may apply:

Inbound: In the inbound scenario, this status value is displayed in TM when the business documents of the truck

have not been checked against the documents in the system. In the warehouse, the inbound delivery is blocked and

cannot be processed until the documents have been checked.

Outbound: In the outbound scenario, this status value is optional and is not relevant for processing cargo items in

TM. Transportation planning can start irrespective of the warehouse processing status, but it is recommended to

wait until the warehouse processing status is Completed and the warehouse has prepared the handling units that

are to be shipped.

## Ready for Warehouse Processing

This status value indicates that the cargo items can be processed by the warehouse, but the processing hasn’t started yet.

Depending on the loading direction, one of the following scenarios may apply:

Inbound: In the inbound scenario, the business documents of the truck are checked at the gate, and if they match

the system documents, the truck arrives at the warehouse door. You then set this status value to transfer the

responsibility for the cargo items from TM to the warehouse in the system. After this status value is set, the delivery

is unblocked in the warehouse and the possibility of making changes to items is limited in TM.

Outbound: In the outbound scenario, this status value is optional and is not relevant for the processing of cargo

items in TM. Transportation planning can start irrespective of the warehouse processing status, but it is

recommended to wait until the warehouse processing status is Completed and the warehouse has prepared the

handling units that are to be shipped.

## In Process

This status value indicates that the warehouse has created warehouse tasks and is actively working on the cargo items.

Depending on the loading direction, one of the following scenarios may apply:

Inbound: In the inbound scenario, this status value is optional and is not relevant for processing cargo items in TM

because the responsibility for the cargo items was handed over to the warehouse after the Ready for Warehouse

Processing status was set.

Outbound: In the outbound scenario, this status value indicates that the warehouse is working with the cargo items.

You can start cargo planning but cannot change the items.

## Completed

This status value indicates that the warehouse has completed the activities related to the processing of the cargo items.

Depending on the loading direction, one of the following scenarios may apply:

Inbound: In the inbound scenario, this status value is optional and is not relevant for processing cargo items in TM

because the responsibility for the cargo items was handed over to the warehouse after the Ready for Warehouse

Processing status was set. Warehouse activities, such as re-packaging received cargo items, are not relevant for

transportation.

Outbound: In the outbound scenario, this status value indicates that from the perspective of the warehouse, the

cargo items are ready to be shipped. The responsibility for the cargo is transferred from the warehouse to TM in the

system.

## In Transit

This is custom documentation. For more information, please visit SAP Help Portal.

26


1/14/26, 2:44 PM

This status value is only relevant for the stock transport order (STO) process. Handling is performed at the outbound

warehouse and the document progresses through the different warehouse processing statuses as normal. However, in the

case of an STO, once outbound handling is completed, the freight unit is reassigned from an outbound delivery to an

inbound delivery. The freight unit has the inbound delivery as its direct predecessor document, though the outbound

delivery still appears in the list of predecessor documents. At this moment the warehouse processing status is set to In

Transit. The inbound transport will arrive in the inbound warehouse.

After this switch, you are able to set the warehouse processing status for the inbound warehouse and the document

progresses through the different warehouse processing statuses as any other inbound delivery.

For more information about STO, please see Integration of Stock Transport Orders.

The warehouse processing status also has aggregated status values. The status is aggregated from the item level to the next

higher level in the hierarchy. The status also appears on the header level of the business document. For example, if all the items in

the road freight order have the status Ready for Warehouse Processing, the status on the header level will also be Ready for

Warehouse Processing.

However, if all items do not have the same status, then the system displays the aggregated status of these items on the header

level, indicating partial processing. For example, if one item has the status Completed, one has the status In Process, and one has

the status Not Started, then the system displays the highest aggregated status for these items, that is, Partially Completed.

The following are the aggregated warehouse processing statuses:

## Partially Ready for Warehouse Processing

The system displays this status value when one or more of the items or documents have the status Ready for Warehouse

Processing and at least one other item or document has a lower status indicating that it is at an earlier stage in the

warehouse processing lifecycle. For example, the other items may have the status Not Started.

The Partially Ready for Warehouse Processing status can change to Partially In Process or Partially Completed if the

status of one of the items or documents in the road freight order changes to In Process or Completed.

## Partially in Process

The system displays this status value when one or more of the items or documents have the status In Process and at least

one other item or document is at an earlier stage in the warehouse processing lifecycle. For example, the other items may

have the status Ready for Warehouse Processing.

The aggregated status can change to Partially Completed when the status of one or more items changes to Completed.

## Partially Completed

The system displays this status value when one or more of the items or documents have the status Completed and at least

one other item or document is at an earlier stage in the warehouse processing lifecycle. For example, the other items may

have the status In Process.

## Partially In Transit

This status value is only relevant for the stock transport order (STO) process. The system displays this status value when

one or more of the items or documents have the status In Transit and at least one other item or document is at an earlier

stage in the warehouse processing lifecycle. For example, the other items may have the status In Process.

## Statuses in the Goods Movement Process

In TM, you can trigger the posting or cancellation of goods movement for a delivery assigned to a warehouse loading stop or

warehouse unloading stop. You can do so using the Post or Cancel options in the Goods Movement drop-down menu. The request

is sent from TM to the warehouse and the warehouse posts or cancels goods movement. TM waits for the goods movement

posting to be confirmed or cancelled by the warehouse.

This is custom documentation. For more information, please visit SAP Help Portal.

27


1/14/26, 2:44 PM

In the inbound process, you can trigger the posting or cancellation of goods movement only after the warehouse processing status

of the items or business documents assigned to the warehouse unloading stop is set to Ready for Warehouse Processing.

In the outbound process, you can trigger the posting or cancellation of goods movement only after the warehouse processing

status of the items or business documents assigned to the warehouse loading stop is Completed and the handling execution

status of the warehouse loading stop is Loaded.

The posting request or cancellation request is sent to the warehouse in the system after you save the changes in the business

document. Until you save, the posting or cancellation request is saved locally in the business document and you can cancel the

changes using the Reverse Changes option in the Goods Movement drop-down menu.

Goods movement for a handling unit or a delivery can also be triggered by the warehouse itself and this information is

communicated to the related item, such as a pallet or container.

The goods movement information is displayed in the Goods Movement Status field and the Goods Movement Processing field in

the business document. The Goods Movement Status field displays the overall status of goods movement processing in the

warehouse. The Goods Movement Processing field gives you more information about the intermediate stages during the

processing. For example, if you have not posted goods movement, the goods movement status is Not Relevant, and the goods

movement processing status is No Processing Requested. After you post goods movement, the goods movement status is Not

Processed Yet because only a request has been received, and the goods movement processing status is Posting Requested.

Eventually, once the warehouse has processed the request, it updates the goods movement status to Completely Processed. The

status values are explained in detail below.

## Goods Movement Status

In TM, the system displays the information communicated by the warehouse about the goods movement status of an item.

The goods movement status is displayed on the item and header level of a road freight order, consignment order, and

freight unit (FU).

The status has the following values:

## Not Relevant

This status value indicates that the item is not yet considered for goods movement.

## Not Processed Yet

This status value indicates that TM has sent the request for goods movement processing of an item to the

warehouse, but the warehouse has not processed that item yet. The warehouse has also not communicated the

current status to TM yet because, for example, the request is in the queue.

## Partially Processed

This status value indicates that the warehouse has performed goods movement for some of the items, but not for

all.

## Completely Processed

This status value indicates that the warehouse has sent a goods movement confirmation for all the subitems.

## Goods Movement Processing

This status is from the perspective of TM. The status values indicate the intermediate stages in the goods movement

process. The goods movement processing status is displayed on the item level of a road freight order.

The status has the following values:

## No Processing Requested

This status value indicates that goods movement processing has not been requested yet.

This is custom documentation. For more information, please visit SAP Help Portal.

28


1/14/26, 2:44 PM

## Posting Requested

This status value indicates that TM has triggered goods movement posting, and the warehouse has received the

request and is working on it. But it has not posted goods movement yet.

## Cancellation Requested

This status value indicates that TM has triggered goods movement cancellation, and the warehouse has received

the request and is working on it. But it has not cancelled goods movement yet.

## Posting/Cancellation Failed

The system displays this status when the posting or cancellation of goods movement by the warehouse is not

successful.

The goods movement processing status is also aggregated from the item level to the next higher level in the hierarchy. It

has the following aggregated status values:

## Posting Partially Requested

The system displays this status value for an item or business document. This status value indicates that goods

movement posting has been requested for one or more items, but not for all. For example, in the outbound process,

you have created a consignment order with two FUs for a warehouse loading stop. If one of the FUs has the handling

execution status Loaded, warehouse processing status Completed, and the goods movement status Posting

Requested and the other has the statuses Not Loaded, In Process, and No Processing Requested, the aggregated

goods movement processing status of the consignment order will be Posting Partially Requested.

## Cancellation Partially Requested

The system displays this status value for an item or business document. This status value indicates that goods

movement cancellation has been requested for one or more items, but not for all. For example, in the outbound

process, you have created a consignment order with two FUs for a warehouse loading stop. If one of the FUs has the

handling execution status Loaded, warehouse processing status Completed, and the goods movement status

Cancellation Requested and the other FU has the statuses Not Loaded, In Process, and No Processing Requested,

the aggregated goods movement status of the consignment order will be Cancellation Partially Requested.

## Posting/Cancellation Partially Requested

The system displays this status value for an item or business document, such as a consignment order, when, for

example, one FU belonging to the consignment order has the goods movement processing status Posting

Requested, the second FU has the status Cancellation Requested, and the third FU has the status No Processing

Requested.

The system can also display this status value as an aggregation of the statuses of the business documents. For

example, if one consignment order of the warehouse loading stop has the goods movement status Posting Partially

Requested and the other consignment order has the status Cancellation Partially Requested, then the aggregated

status of the warehouse loading stop will be Posting/Cancellation Partially Requested.

## Posting/Cancellation Requested

The system displays this status value if all the items or business documents have the goods movement processing

status Posting Requested or Cancellation Requested and there are no items with the status No Processing

Requested. For example, two of the three FUs belonging to a consignment order have the goods movement

processing status Posting Requested and one has the status Cancellation Requested. In this case, the aggregated

status of the consignment order will be Posting/Cancellation Requested.

## Statuses in the Inbound Process

This is custom documentation. For more information, please visit SAP Help Portal.

29


1/14/26, 2:44 PM

The inbound part of the Advanced Shipping and Receiving process in Transportation Management (TM) covers the activities that

take place between the time that a loaded truck arrives at the warehouse gate, unloads the goods at the warehouse door, and

departs from the company premises. The responsibility for the goods is handed over from TM to the warehouse. Below is a sample

sequence of activities in terms of the statuses used in the inbound process.

You can see the statuses on the Statuses tab page on the product level or the header level of the business document or in the

fields in the Overview section. For more information about statuses in general, see Statuses in Advanced Shipping and Receiving.

For more details about statuses in a road freight order that is relevant for a customs process, see Statuses in the Integration with

SAP GTS (Inbound Process).

The basic sequence of statuses and activities in the inbound process is as follows:

1. When the truck arrives at the gate, you set the handling execution status for the stop to Arrived. The warehouse processing

status of the items is Not Started.

2. If the business documents of the goods on the truck match the documents in the system, you set the handling execution

status to Checked In. All the inbound deliveries for the goods to be delivered at that stop get the status In Yard (for

Extended Warehouse Management (EWM) deliveries) or In Plant (for Logistics Execution (LE) deliveries), thus

communicating to the warehouse that the ordered stock has reached the company premises. If you set the Checked In

status without first setting the Arrived status, then the system sets the Arrived status automatically.

If the documents of the goods don't match the documents in the system, you can make changes manually in the business

document. The referenced predecessor documents are also updated if you have enabled this in the Customizing of the

document type. You can make changes that affect the warehouse process until the warehouse processing status is set to

Ready for Warehouse Processing.

3. The truck drives to the assigned warehouse unloading stop to unload the goods. When it reaches the door, you set the

warehouse door status to Arrived at Door. This status value indicates that until this truck departs, the door cannot be used

by other trucks. You can allow a door to be used in several business documents at the same time using the Define Location

app. For more information, see "Warehouse Door Status" under Statuses in Advanced Shipping and Receiving.

After you set this status, the system reports the event Arrival at Door.

4. You then set the warehouse processing status to Ready for Warehouse Processing at the warehouse unloading stop level

to signal to the warehouse that they can begin their activities. With this status value, you transfer the responsibility for the

goods from TM to the warehouse in the system. After this status value is set, the delivery is unblocked in the warehouse

and the possibility of making changes to items is limited in TM. In an EWM integration scenario, after you set the Ready for

Warehouse Processing status for the freight units or for the inbound delivery from LE, the freight units that were initially

assigned to the inbound delivery from LE are assigned to the warehouse inbound delivery from EWM. You can track the

progress of this assignment on the Unloading Details tab of a warehouse unloading stop in the Overview section of the

road freight order.

If you don't have an explicit check-in process at your company gate, you can directly set the status to Ready for Warehouse

Processing at the warehouse unloading stop level. The system will automatically set the Checked In status at the stop level

and In Yard (for EWM deliveries) or In Plant (for LE deliveries).

When you set the Ready for Warehouse Processing status for LE inbound deliveries, the system checks if it's defined for

the product that it must be packed or unpacked, before you can set the status.

5. If information about the unloading activities cannot be electronically communicated, you can use the handling execution

status option Set Items to Unloaded to manually set the status of the items that are unloaded from the truck to Unloaded.

6. When unloading is completed, you can use the handling execution status option Set Stop to Unloading Completed to set

the status of the warehouse unloading stop to Unloaded. If you set this status without setting the status of the items at this

stop to Unloaded, the system creates document errors. On the Document Errors tab, you can use the actions available

next to the error description to set the handling execution status of the items to Unloaded. For information about making

changes to a capacity document even after the execution at the stop has started or been completed, see Late Changes to

Capacity Documents.

This is custom documentation. For more information, please visit SAP Help Portal.

30


1/14/26, 2:44 PM

7. You can post goods movement at the warehouse unloading stop level only after the warehouse processing status is set to

Ready for Warehouse Processing. The system displays the status value Posting Requested and triggers goods receipt by

the warehouse. After the warehouse has successfully processed the request, the system updates the goods movement

status to Completely Processed. If the posting of goods movement by the warehouse is not successful, the system

displays the goods movement processing status Posting/Cancellation Failed. In the freight order, you can view the details

of the errors related to posting of goods on the Document Errors tab page.

8. Irrespective of the result of the goods movement posting, you can manually set the warehouse door status to Departed

from Door. The door is available again for other trucks to use. After you set this status, the system reports the event

Departure from Door.

9. At the stop level, you set the handling execution status to Checked Out. If you set the Checked Out status without first

setting the warehouse door status to Departed from Door, the system automatically sets the Departed from Door status.

10. You set the handling execution status to Departed.

## Statuses in the Outbound Process

The outbound part of the Advanced Shipping and Receiving process in Transportation Management (TM) includes those activities

that occur from the start of planning to the time the truck departs from the company premises after loading. The responsibility for

the goods is handed over from the warehouse to TM. Below is a sample sequence of activities in terms of the statuses used in the

outbound process.

You can see the statuses on the Statuses tab on the product level or the header level of the business document or in the fields in

the Overview section. For more information about statuses in general, see Statuses in Advanced Shipping and Receiving. For more

details about statuses in a freight order that is relevant for a customs process, see Statuses in the Integration with SAP GTS

(Outbound Process).

The sequence of statuses and activities in the outbound process depends on which scenario for transportation planning and

warehouse processing is used. The following scenarios are supported:

Warehouse-Driven Scenario - In this scenario, warehouse processing takes places before transportation planning.

Transportation planning can start irrespective of the warehouse processing status, but it is recommended to wait until the

warehouse processing status is Completed and the warehouse has prepared the handling units that are to be transported.

When the warehouse creates outbound deliveries and freight units but doesn't start its warehouse activities, such as

picking and packing, the system displays the warehouse processing status Ready for Warehouse Processing in TM.

Transport-Driven Scenario - In this scenario, transportation planning takes place, in whole or in part, before warehouse

processing.

In a transport-driven scenario, you have to manually set the new freight units or the road freight order to Ready for

Warehouse Processing. For more information, see Transport-Driven Execution.

The basic sequence of statuses and activities in the outbound process is as follows:

1. Warehouse processing and transportation planning take place.

2. When the warehouse starts packing handling units, the system displays the warehouse processing status In Process in TM.

You can start planning the transport of the cargo items but cannot make changes to the items.

3. When the warehouse tasks have been completed and the handling units are ready, the warehouse sets the shipping

readiness status of the delivery to Ready for Shipping in Extended Warehouse Management (EWM) or sets the warehouse

execution status to Delivery is Ready for Shipping in Delivery Management (LE-SHP). This updates the freight units with

This is custom documentation. For more information, please visit SAP Help Portal.

31


1/14/26, 2:44 PM

the packing details of the handling units and triggers the warehouse processing status Completed in TM. This means that

you can begin your activities, such as creating a consignment order or a road freight order from the freight units.

If you use a logistics service provider (LSP) to ship your goods, then information about the updated freight units is sent to

the LSP. The LSP creates a road freight order from the freight units.

4. You can set the handling execution status to Cargo Ready for Loading in the freight order. With this, you can initiate

customs processes and have the good cleared before the truck's arrival and check in. Any items whose warehouse

processing status is not set to Completed at this point are removed from the freight order.

Status Cargo Ready for Loading as a prerequisite and automatic trigger for customs processes requires customizing. For

more information, see SAP GTS Integration for the Outbound Process and Integration with SAP Global Trade Services in

Advanced Shipping and Receiving.

5. You can then assign the freight unit to a freight order and specify on which truck the products contained in the delivery are

to be transported. Additionally, the system can automatically create a consignment order, which bundles all deliveries that

have the same ship-to party. The truck then drives to the warehouse to load the goods. When it arrives at the gate, you set

the handling execution status for the stop to Arrived.

For more information about automatic consignment creation, see Creation and Editing of a Consignment Order and

Automatic Consignment Building.

6. After the documents of the truck are verified, you set the handling execution status for the stop to Checked In. The system

automatically defines the loading point and warehouse door from which the truck has to pick up the goods, if this

information is provided in the predecessor documents. You can also manually define a loading point and warehouse door.

7. When the truck reaches the warehouse door, you set the warehouse door status to Arrived at Door and the warehouse can

start loading the truck. After you set this status, the system reports the event Arrival at Door. You can allow a door to be

used in several business documents at the same time using the Define Location app. For more information, see

"Warehouse Door Status" under Statuses in Advanced Shipping and Receiving.

8. You can use the handling execution status option Set Items to Loaded to manually set the status of the items at the

warehouse loading stop to Loaded.

9. After you have finished loading the truck, you can use the handling execution status option Set Stop to Loading

Completed to set the status of the warehouse loading stop to Loaded. After this status has been set, no further items can

be loaded onto the truck, and the system automatically removes all the items that do not have the status Loaded from the

road freight order.

10. You can post goods movement at the warehouse loading stop level only after the warehouse processing status is set to

Ready for Warehouse Processing. The system displays the status Posting Requested and triggers goods issue by the

warehouse. After the warehouse has successfully processed the request, the system updates the goods movement status

to Completely Processed. If the posting of goods movement by the warehouse is not successful, the system displays the

goods movement processing status Posting/Cancellation Failed. In the freight order, you can view the details of the errors

related to posting of goods on the Document Errors tab.

11. Irrespective of the result of the goods movement posting, you can manually set the warehouse door status to Departed

from Door. After you set this status, the system reports the event Departure from Door.

12. At the stop level, you set the handling execution status to Checked Out. If you set the Checked Out status without first

setting the warehouse door status to Departed from Door, the system automatically sets the Departed from Door status.

13. You set the handling execution status to Departed.

## Consignment Order

In Transportation Management (TM), a consignment order represents a business document that you can use to group several

transportation requirements based on certain criteria, such as the same source and destination location, the same delivery

This is custom documentation. For more information, please visit SAP Help Portal.

32


1/14/26, 2:44 PM

date/time, and the same business partner.

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

In the Consignment Building Profile app you can configure how the system determines the consignment order type. You can

either choose Document Type Defined in Profile or Document Type Defined by BAdI. This is useful especially if you need two

consignment order types that might have a different custom profile to be used in one freight order, for example to distinguish

consignment order for "normal" deliveries from consignment orders for deliveries with empties.

You can use BAdI /SCMTMS/CNS_EXTR_DET_DOC_TYPE to determine the consignment order type in the Consignment

Building Profile app. For more information, see Customizing for Transportation Management under  Business Add-Ins (BAdIs)

This is custom documentation. For more information, please visit SAP Help Portal.

33


1/14/26, 2:44 PM

for Transportation Management

  Freight Order Management

  Consignment Building

  BAdI: Consignment Order Type

Determination .

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

This is custom documentation. For more information, please visit SAP Help Portal.

34


1/14/26, 2:44 PM
## Creation Options

You have the following options for creating a consignment order:

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

This is custom documentation. For more information, please visit SAP Help Portal.

35


1/14/26, 2:44 PM

The following is a description of an example process for manually creating a consignment order. It is assumed that you already

know the most important transportation data, such as source and destination location and business partners.

1. Entering the general data

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

When you subcontract a consignment order, the system recalculates the charges. If these charges differ from the

previously calculated charges, the system cancels subcontracting. You must then check the charges manually and adjust

them, if necessary. Subsequently, you can resend the consignment order to the carrier. For more information, see Charge

Calculation.

6. Confirming or rejecting the consignment order

You receive a confirmation or rejection of the consignment order from your carrier in the form of electronic messages. If

you have not set up message communication with your carrier, you can also enter this information manually in the system.

7. Printing

Optionally, you can print the corresponding print documents. For more information, see Printing.

8. Fixing the consignment order

This is custom documentation. For more information, please visit SAP Help Portal.

36


1/14/26, 2:44 PM

You can fix your consignment order to protect it from undesirable changes arising from background processing (planning

runs or carrier selection).

9. Creating a freight settlement document

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

This is custom documentation. For more information, please visit SAP Help Portal.

37


1/14/26, 2:44 PM

You can select your own rules that you have defined in Customizing. For more information, see Customizing for

Transportation Management under  Freight Order Management

 Consignment Order

 Define Grouping Rules for

Automatic Consignment Building .

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

You have the following options for automatically building consignment orders locally and creating consignment order documents

in the freight order:

Creating local consignment orders

Manual triggering from the freight order UI

Select the menu option  Follow-Up

 Build Local Consignment Orders  in the Create Freight Order or Edit

Freight Order app. The system then groups the freight units of the freight order into consignment orders based on

the default rules and according to any rules defined in the consignment building profile and creates local

consignment orders with the item type SHP and the item category Consignment Order. The consignment orders

are also marked with the qualifier local in the item hierarchy.

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

The advantage of local consignment orders is that changes can still be made to the freight order after consignment

building that are taken into account when the consignment order documents are generated. The consignment order

documents are then no longer updated with freight order changes. You can, for example, add freight units to the freight

This is custom documentation. For more information, please visit SAP Help Portal.

38


1/14/26, 2:44 PM

order and have the consignment building executed again. The system then assigns new freight units to the existing

consignment orders or, if this is not possible according to the grouping rules, it groups them into new consignment orders.

Note that the system does not take local consignment orders into account during further planning.

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

## Define Consignment Order Types

This is custom documentation. For more information, please visit SAP Help Portal.

39


1/14/26, 2:44 PM
## Separate or Combined Inbound Messages

You have the following options to create or update freight orders or consignment orders:

Separate Inbound Messages (Consignment-Based Freight Order)

Information for freight orders and consignment orders can be sent in separate inbound messages (ASN). The freight order

contains references to the related consignment orders. Ideally, the consignment order is sent first.

If a consignment order is error-free, the system can automatically create an inbound delivery in Logistics Execution (LE) if

the Customizing is set accordingly. If a consignment order or freight order that was sent in separate inbound messages

contains errors, it is usually still saved as a document in TM as long as the consignment order contains at least a source

and destination location. The errors are displayed on the Document Errors tab and can be corrected there. Whether the

system creates errors, depends on the setting that you have made in the Customizing for the freight order type or

consignment order type. If the freight order message is sent before the consignment order was created, and the

consignment order is created later, the assignment of the consignment order is done automatically by choosing the

respective external consignment ID.

TM creates deliveries for error-free FUs when you create or save a consignment order. Upon correction of errors in FUs, the

system will either asign these FUs to an existing delivery or create new deliveries for FUs with different external delivery

numbers. Once FUs are assigned to a delivery, the system cannot make changes to these deliveries during an MRP run and

the subsequent freight unit building step. As with consignment order errors, you can find and correct errors on the

Document Errors tab.

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

This is custom documentation. For more information, please visit SAP Help Portal.

40


1/14/26, 2:44 PM

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

This is custom documentation. For more information, please visit SAP Help Portal.

41


1/14/26, 2:44 PM

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

External package ID

## Related Information

Automatic Consignment Building

## Web Services for External Planning Scenarios

The integration of Transportation Management (TM) with the external transportation management system of a carrier allows you

to run order-to-cash or procure-to-pay processes and, at the same time, delegate the transportation planning processes to the

carrier.

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

This is custom documentation. For more information, please visit SAP Help Portal.

42


1/14/26, 2:44 PM

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

the  external  planning

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

This is custom documentation. For more information, please visit SAP Help Portal.

43


1/14/26, 2:44 PM

## Phase

Process Step

## Details

## Web Service

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

This is custom documentation. For more information, please visit SAP Help Portal.

44


1/14/26, 2:44 PM

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

## Creation of Packages Across Freight Unit Items

In consignment orders or freight orders you can create packages across freight unit items. The system splits and merges the

freight units as needed, and updates the existing item hierarchy and the successor documents, that is the corresponding capacity

documents.

## Use

In the Advanced Shipping and Receiving inbound process you can assign product items from different freight units to the same

package, for example, by packing them on a single pallet. In consignment orders this can be done manually on the UI or by inbound

messages. For freight orders this can be done manually on the UI or by combined inbound messages (transport-based freight

order). If possible, the system performs a freight unit merge for these packages that contain items across several freight units.

Merging means, that all items of a freight unit are moved to another freight unit. The empty freight unit is then cancelled. In all

other cases only single items are moved to another freight unit.

## Example

Repacking might be necessary when a truck arrives at the gate and the load of the truck differs from the data in the system. The

load has, for example, two product items (from different freight units) packed on one pallet. In the consignment order or freight

order you can directly reassign product items to other packages to reflect the truck load. When you save, the system performs a

freight unit merge: the two freight units are merged into one freight unit. Now empty freight units are canceled.

Based on predefined criteria, such as a delivery being referenced to a freight unit, the system then determines which freight unit is
to be kept after the merge. The existing item hierarchy in the business documents is updated accordingly.

The system does not support the building of packages across freight unit items with different deliveries (cross-delivery).

This is custom documentation. For more information, please visit SAP Help Portal.

45


1/14/26, 2:44 PM
## Prerequisites

You have activated the synchronization of predecessor documents. For more information, see Synchronization of Predecessor

Documents.

## Example

## Freight Unit Split and Mass Data Changes

In the inbound process of Advanced Shipping and Receiving in Transportation Management (TM), your supplier can send you

external delivery note numbers with a consignment order using an advanced shipping notification (ASN). You can change the

number in business documents, such as freight orders or consignment orders.

## Use

The external delivery note number is the number that identifies the supplier's delivery note and groups all the items of this delivery

note.

In the business document, the external delivery note number is displayed in the Document References tab page of a product or

package. You can also see it in the details section of a freight unit.

All freight unit items in an inbound delivery must have the same external delivery note number. If you assign a freight unit to a

capacity document, for example, a road freight order, after the execution at the stop in the capacity document has started or been

completed, you must enter the same external delivery note number for the freight unit that was used for one of the other items of

the road freight order. This is only relevant for road freight orders that have customs-relevant goods. For more information, see

Late Changes to Capacity Documents.

If a consignment order is sent as ASN containing one or several freight units with different external delivery note numbers,

the system automatically splits the freight unit. No further manual split is needed.

If the external delivery note number of one or all freight unit items sent as ASN does not match the number provided in the

documents of the carrier, you can change the numbers in the business document. A mass change of data is also possible.

The predecessor documents (such as a purchase order or scheduling agreement) are updated accordingly.

You can change the external delivery note numbers in the following ways:

## Change Number Without FU Split

In a business document, you can change the external delivery note number for a freight unit and its underlying items all at

once. When you enter the new external delivery note number in the details section of the freight unit, the freight unit and its

underlying items are updated with the new number.

## Change Number With FU Split

If one or several of the external delivery note numbers differ, you can change them for those freight unit items by splitting

the freight unit. The system splits the original freight unit and creates a new one with the items that have the new external

delivery note number. It also creates a new inbound delivery in the hierarchy.

## Example

In a freight unit, only 50 product items of 100 have the same external delivery note number as provided in the documents of the

carrier. On the Items tab page of the business document, you can select the items with a different number and initiate a manual

This is custom documentation. For more information, please visit SAP Help Portal.

46


1/14/26, 2:44 PM

freight unit split for them. After entering the new external delivery number, you then have two different freight units and inbound

deliveries in the hierarchy.

## Correction of Errors in Business Documents

You can use this function to display errors in freight orders and consignment orders that were created based on incorrect EDI

messages in Transportation Management (TM). You can then correct the errors manually.

## Prerequisites

In Customizing for the freight order type or consignment order type, you have selected the Enable Saving of Documents with
Errors value in the Handling of Incorrect Inbound Messages field. For more information, see the following Customizing activities
in Customizing for Transportation Management:

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

47


1/14/26, 2:44 PM

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

This is custom documentation. For more information, please visit SAP Help Portal.

48


1/14/26, 2:44 PM

If the document contains errors, the system automatically sets planning, execution, and invoicing blocks for the document. These

blocks are displayed on the Block Information tab page with the corresponding block reasons.

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

In the inbound process the system checks for an overdelivery of quantity when the system creates or updates a consignment

order on the basis of an inbound message or when you manually change quantities in a consignment order or freight order.

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

For the quantity calculation, the system considers the product item quantity of the inbound message (or a manually entered

value), the open quantity, the tolerance, and the unlimited flag:

If the open quantity of an item plus the sent or manually entered quantity is below or within the tolerance, the system

creates the consignment order without an error message. "Open quantity" means quantity not yet assigned by a freight

unit to a consignment order or quantity already executed within a freight order.

If the open quantity of an item plus the sent or entered quantity exceeds the tolerance, the system creates the

consignment order despite the errors and saves the respective item locally. You can display and resolve the errors on the

Document Errors tab page. When the error is resolved (by changing the purchasing document or the quantity of the item in

the freight order or consignment order) the system automatically assigns the corresponding freight units to the

consignment order.

This is custom documentation. For more information, please visit SAP Help Portal.

49


1/14/26, 2:44 PM

If unlimited overdelivery is defined in the related purchase order or scheduling agreement, the system creates the

consignment order without an error message. The system adjusts the quantity in the latest freight unit and assigns it to the

consignment order.

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

This is custom documentation. For more information, please visit SAP Help Portal.

50


1/14/26, 2:44 PM

If, for example, one of the packages in a nested package contains the wrong packaging material, the system saves the top-level

package locally though the top-level package doesn’t contain errors. You can display and resolve the error on the Document Errors

tab page.

Examples for package-related errors:

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

This is custom documentation. For more information, please visit SAP Help Portal.

51


1/14/26, 2:44 PM

or post goods movements before warehouse processing is possible. This can cause errors, for example locking of business

documents, inconsistent data in busines documents, or failed updates to business documents.

You can use the Document Errors tab page to view details of errors. The following are some examples of possible errors when

working with the freight order:

## Goods Movement Posting

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

This is custom documentation. For more information, please visit SAP Help Portal.

52


1/14/26, 2:44 PM
## Related Information

Correction of Errors in Business Documents

## Synchronization of Predecessor Documents

In the Advanced Shipping and Receiving inbound process you can enable the synchronization of predecessor documents

referenced in a consignment order or freight order. You enable this setting, for example, if you want to compare the transportation

documents of the truck with the system entries at the gate.

## Prerequisites

For more information, see Customizing for Transportation Management under

## Integration

 Settings for Advanced Shipping

and Receiving .

## Check-In Process at the Gate

When a truck arrives at the gate you can compare the transportation documents of the truck with the freight order in the system. If

the load of the truck differs from the freight order data in the system, you can directly change discrepancies in the freight order. As

an example, changing the data is necessary, if the truck contains more, less, or other cargo than expected.

You can change the item structures in the freight orders or consignment orders until the Ready for Warehouse Processing status

is set. The status is relevant for changes that affect the warehouse process. After the Ready for Warehouse Processing status is

set, you can still change data that does not affect the warehouse process.

The system can automatically update the referenced predecessor documents of the consignment order or freight order and keep

them up-to-date.

For a freight order or consignment order you can change data such as:

Add unplanned freight units or remove freight units. The systems unassigns the removed freight units.

Change goods supplier in consignment order. The goods supplier and its source location are then changed accordingly in

the corresponding freight unit.

Change fields related to unit of measure

Change product item quantity (decrease or increase quantity)

If you decrease the quantity, the freight unit is split and a new freight unit with the leftover-quantity is created.

Add or delete product items

Add or delete package items

Change or delete package data

Change nested packages (package hierarchy)

## Change packaging material

This might be necessary if a different packaging material was used. After the change, the amount of products stays the

same and is not recalculated automatically. The package hierarchy above or below remains unchanged.

## Change auxiliary packaging material

This is custom documentation. For more information, please visit SAP Help Portal.

53


1/14/26, 2:44 PM

Add or delete a delivery note item, change delivery note item fields (which results in add or delete freight units or product

items)

Change fields related to Materials Management (MM), such as:

Number of handling unit (package ID)

Serial number

Batch-related data

## Related Information

Correction of Errors in Business Documents

Example Checks to Find Errors in Business Documents

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

 Product

## Define

Packaging Material Types .

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

automatically created under package items during package building. Note, however, that auxiliary packaging materials must

This is custom documentation. For more information, please visit SAP Help Portal.

54


1/14/26, 2:44 PM

always be created as the lowest item in an item hierarchy, meaning that no further items may be assigned below the auxiliary

packaging material. Since auxiliary packaging materials do not have their own capacity, they cannot contain any further items.

If the auxiliary packaging material is a main item, it is considered during load planning.

The packaging material type and packaging material category are displayed in the detailed information for the auxiliary packaging

material items in the business documents.

Auxiliary packaging materials are also taken into account when integrating TM with Extended Warehouse Management (EWM).

When EWM deliveries are created by the system, the related handling units also contain the auxiliary packaging materials. For

more information, see Advanced Shipping and Receiving.

Related Information

## Items

Defining Auxiliary Packaging Materials

## Delivery Split

In Advanced Shipping and Receiving you can split deliveries from TM across the following warehouse management applications

located in the same system:

Lean Warehouse Management

Stock Room Management

## Extended Warehouse Management

When you split a delivery, the system creates a new delivery and assigns the relevant freight units to it. If you split a delivery that

contains just one freight unit, the system also splits the freight unit. The activities in the process are as follows:

## Planning activities

During planning you can change assignments of freight units, for example assign a freight unit from an existing delivery to a

different freight order. If you make such a change, a new delivery is required for the new freight order.

## Warehouse Activities

Warehouse activities can start once the Warehouse Processing Status is set to Ready for Warehouse Processing. During

warehouse activities, delivery split is not possible.

As soon as picking starts, this is communicated to TM and the Warehouse Processing Status of the freight unit changes to

In Process. After completion of all warehouse activities (picking, packing, staging) an update is sent to TM to confirm that

the warehouse activities are completed, and the deliveries are ready for shipping. At this point the Warehouse Processing

Status is set to Completed. After this point a delivery split is again possible.

## Loading Activities

When loading a freight order, it may also be necessary to split deliveries, for example if the truck cannot accommodate all

of the handling units assigned to the delivery on the freight order. For loading a freight order, you can use the Load or

Unload Freight Orders app to select the handling units from a delivery that have been loaded and change the Execution

Status to Set Items to Loaded.

Once you set the Execution Status of the stop to Set Stop to Loading Completed, the system removes from the freight

order any handling unit that has not been loaded, then creates:

a new freight unit to which the handling unit is assigned

This is custom documentation. For more information, please visit SAP Help Portal.

55


1/14/26, 2:44 PM

a new delivery

## Delivery Deletion

In the Advanced Shipping and Receiving process, you can delete LE inbound and outbound deliveries in Transportation

Management (TM) in SAP S/4HANA.

You can delete unneeded deliveries in customer and supplier returns.

Certain requirements must be met. The deletion of deliveries is available in an embedded setup. Deliveries must originate in

Logistics Execution (LE). Finally, freight units (FU) must be delivery-based and unplanned.

  Restriction

The deletion of LE deliveries is available for specific processes. For technical and practical reasons, 2-step stock transport

orders (STO) and side-by-side setups are both excluded.

In scenarios involving EWM (in- and outbound) delivery orders and EWM TU-based deliveries, deleting LE deliveries is not

supported.

## Use

Please note that image maps are not interactive in PDF outputs.

## Scenario

You create inbound deliveries based on an external delivery note number.

Shortly after, the truck arrives at the gate, and the team unloads the goods. During their administrative cargo processing, the team

discovers a missing external delivery note, which has also been removed from the consignment order in the system.

Supposing the supplier cannot deliver the note within a certain time horizon, or the new delivery date is undetermined, you would

want to delete the inbound deliveries created based on the aforementioned note.

This is custom documentation. For more information, please visit SAP Help Portal.

56


1/14/26, 2:44 PM
## Procedure

1. To delete deliveries, open your Freight Units – Worklist app from the Launchpad.

2. In the worklist, select the FUs in the delivery you wish to delete. If there are two or more FUs in a delivery, you must select

all FUs in a delivery.

3. Select Delete Delivery.

4. A pop-up window will appear, prompting you to confirm your choice. Choose OK.

5. If an FU is planned, you must first remove it from the freight order (FO).

6. Open the FO, select Edit, select the FU checkbox, and select Delete and Save.

## Related Information

## Advanced Shipping and Receiving

End-to-End Process (E2E) for Advanced Shipping and Receiving

Overview of Features in Advanced Shipping and Receiving

Prerequisites for Advanced Shipping and Receiving

## Delivery Updates

You can update specific header and item level fields in LE outbound deliveries that are relevant for Transportation Management

(TM) after the deliveries have been transferred to Extended Warehouse Management (EWM) and freight units (FU) have been

created in TM.

The updates are possible up to certain points in the process and depend on the specific scenario.

When updating a delivery, you must consider both the stage and process type. First, you must note what stage you have reached in

the process. In TM's case, communication is routed via EWM, and therefore, depends at times on EWM statuses. And second, you

must consider whether you are in a transport- or warehouse-driven process.

## Features

## Transport- and Warehouse-Driven Processes

The following fields can be updated and changed. The updates can take place before the process reaches the status Ready for

Warehouse Execution in transport-driven scenarios; or while in status In Warehouse Execution, but no warehouse task has been

created and the FUs have not yet been assigned to a freight document in warehouse-driven scenarios.

Header Level

Delivery Date

Shipping Type

Incoterm Version

Incoterm 1

Incoterm 2

Incoterm Location 1

This is custom documentation. For more information, please visit SAP Help Portal.

57


1/14/26, 2:44 PM

Incoterm Location 2

## Item Level

## Delivery Quantity

You can also add new items to your outbound delivery.

## All Processes and Statuses

The following fields can be updated at any point in time regardless of the execution status or scenario:

Header Level

## Text

Item Level

Batch Number

## Texts

Material Freight Group

Customer Material Number

Material Description

## Related Information

Delivery Updates in TM Triggered by Logistics Execution

## Subcontracting of Purchase Order

In the subcontracting process, a company outsources certain stages in the manufacturing process to subcontractors.

The component parts of the final product are transported to the subcontractor, where the next step of the manufacturing process

takes place. After, the subcontractor returns the finished products to the original manufacturer. In a subcontracting process where

the subcontractor is in another country, compliance check and customs clearance must be considered during the transportation

process.

The subcontracting purchase order contains the final product and its components, which are listed in a bill of material (BOM) with

item category L for subcontracting. The BOM is used to define the relationship between one component and several

subcomponents and contains information such as the ratio of the component to the subcomponents.

## Sample Process

The following is an example of how a subcontracting process might develop from the perspective of the manufacturer:

This is custom documentation. For more information, please visit SAP Help Portal.

58


1/14/26, 2:44 PM

Figure 1: The Subcontracting of a Purchase Order

1. Creating a purchase order

The manufacturer creates a subcontracting purchase order or scheduling agreement with item type L.

  Remember

Run transaction ME21N to create a subcontracting purchase order.

2. Creating an outbound delivery

They run transaction me20n to open the Subcontracting Cockpit. They enter the supplier and plant to find the

subcontracting purchase order and create the outbound delivery.

Integration between Transportation Management (TM) and Materials Management (MM) triggers the creation of a freight

unit for the expected finished material in TM. This freight unit, which also lists the subcomponent, is relevant for the later

inbound process from the subcontractor.

The manufacturer assigns the freight unit to a freight order.

In a subcontracting process where the subcontractor is located across borders, compliance and customs must first be

checked during the transportation process.

3. Creating an inbound delivery

Finally, the subcontractor uses the consignment order to send an ASN to the manufacturer.

The manufacturer relies on the ASN from the subcontractor to create a consignment order for the inbound delivery. The

consignment order contains the freight unit created in step 1, which is now used to conduct the inbound process and the

subsequent unloading activities.

Related Information

## Integration of Orders

## Configuring Integration of Orders and Deliveries

This is custom documentation. For more information, please visit SAP Help Portal.

59


1/14/26, 2:44 PM

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

The ocean freight scenario for shippers supports door-to-door (D2D) and door-to-port (D2P) shipping. As usual, you use an ocean

freight booking to reserve freight space on a vessel.

You can receive the confirmation for the oceanfreight booking from the carrier using EDI communication. Alternatively, you enter

the confirmation manually in the ocean freight booking by setting the status to Set to Confirmed by Carrier.

## Container Units

You create container units and assign freight units. The freight units can originate from sales orders or outbound deliveries. After

creating the container units, you assign them to an ocean freight booking. Finally, you create pick-up freight orders (pick-up FOs).

In case you need to change the assignment of container units to pick-up or delivery freight orders, you can also assign or unassign

the container units in the freight booking.

This is custom documentation. For more information, please visit SAP Help Portal.

60


1/14/26, 2:44 PM

When creating container units, the system can automatically check if the container registration number for the container is

correct according to ISO 6346. The system runs the check when you enter the container registration number together with an

equipment type. To use the check, you need to specify the equipment type in Customizing for Transportation Management under

Master Data

## Resources

## General Settings

  Define Equipment Groups and Equipment Types . Set the resource class for

the container group to 10 Container.

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

To achieve this, you define a freight order type for road (and one for rail) that is defined as Default FO Type for FB. You do

so in section Default Types in Customizing for Transportation Management under  Freight Order Management

## Define

Freight Order Types .

## Loading Cargo

You have several options to set the loading status in the system:

## In the Load or Unload Freight Orders app

In the Edit Road Freight Order app or Edit Rail Freight Order App

Via Radio Frequency (RF)

As storage location, you can use an inventory-managed (IM) storage location for Lean Warehouse Management or a storage

location for Extended Warehouse Management (EWM).

This is custom documentation. For more information, please visit SAP Help Portal.

61


1/14/26, 2:44 PM

## Consignment Orders

You can create consignment orders for pick-up FOs associated with an ocean freight booking. The consignment orders include

booking information from the assigned ocean booking, for example, vessel, voyage, IMO Ship ID, UN/LOCODE, expected arrival

date and time at the port of destination or at the customer (depending on the scenario in use, that is door-to-door or door-to-

port).

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

Depending on the settings in the logistics integration profile the Incoterm is considered during freight unit building. You

can, for example, configure the freight units to have a planning-relevant stage from the shipper’s location to the port of

destination and a statistical stage (not in the shipper’s responsibility) from port of destination to the consignee.

The consignment order will still have one stage from the shipper’s location to the port of destination. The planned arrival

date refers to the date at the port of destination.

You can set the port of destination to Unloaded. The system prevents setting a container unit to Unloaded in the ocean freight

booking if the container unit has a document error. Once the error is resolved by setting the container unit to Loaded, the system

automatically updates the unloading status for the container unit.

## Handle Containers Left Behind at the Port

The ocean freight process can handle containers that were left behind at the port of loading. For more information, see Cargo Left

Behind at Port/Airport.

## Invoicing

The invoicing process starts only after the ocean vessel's departure. It also requires that there are no pending decisions for any

containers left behind. For more information, see Carrier Invoice.

## Message Exchange Between Shipper and Carrier

The ocean freight scenario offers an end-to-end process with container units and message exchange between you and the carrier.

This is custom documentation. For more information, please visit SAP Help Portal.

62


1/14/26, 2:44 PM

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

If the status change takes place in the pick-up FO, a TransportationOrderGenericRequest_Out message (with business

scope “Notification”, categoryCode "TO" (freight order)) is sent to the pre-carriage carrier.

For companies that store containers in a local container depot, it might be useful to send an EDI message when the container is

loaded to inform the pre-carriage carrier about the necessary pick-up of the container.

Receiving Freight Booking Updates from the Carrier

  Note

The EDI messages you receive from the carrier must contain certain information. For some XML samples, see SAP note

3514066

.

This is custom documentation. For more information, please visit SAP Help Portal.

63


1/14/26, 2:44 PM

The carrier can send you an freight booking update using EDI communication. You can, for example, receive the house bill of lading

as well as updates for the departure dates from the port of loading, the containers that were loaded, the expected time of arrival,

or change the port of destination in a door-to-door scenario. The system supports updates for freight bookings and for individual

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

The delivery freight order is not assigned to multiple freight bookings. This might be the case if a truck picks up deliveries

of two different vessels.

## Sending ASN to Customer

In the following cases, the system sends a separate advanced shipping notification (ASN) message for each consignment order to

the customer when the vessel departed. At this point in time, additional booking information is available and can be included in the

ASN to the customer.

When goods movement status on consignment order is set to Completely Processed.

When the ocean freight booking is set to Departed From Port of Loading.

Alternatively, when manually requested in the consignment order under  Follow Up

  Send Advanced Shipping

Notification .

This is custom documentation. For more information, please visit SAP Help Portal.

64


1/14/26, 2:44 PM

Especially in a door-to-port scenario, consignments, and their updates are useful for customers. Depending on the Incoterms, they

might need to know the voyage number, and the expected date and time of arrival to organize the pickup and transport of the

goods for the last stage.

## Related Information

Sample Ocean Freight Process for Shippers (Outbound)

## Consignment Order

Cargo Left Behind at Port/Airport

Air Freight Bookings for Shippers (Outbound)

Sample Air Freight Process for Shippers (Outbound)

Advanced Shipping and Receiving

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

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

65


1/14/26, 2:44 PM

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

this information via EDI communication or email. The consignment orders of a pick-up FO can be distributed over several air

freight bookings.

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

The consignment orders include booking information from the assigned air freight booking, for example, airline code, flight

number and airport of destination, expected arrival date and time at the port of destination or at the customer (depending on

This is custom documentation. For more information, please visit SAP Help Portal.

66


1/14/26, 2:44 PM

scenario in use, that is door-to-door or door-to-port).

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

You define the transportation mode in section Service Definition in Customizing for Transportation Management under

Freight Order Management

## Consignment Orders

  Define Consignment Order Types .

This is custom documentation. For more information, please visit SAP Help Portal.

67


1/14/26, 2:44 PM

You have configured the Post Processing Framework (PPF) in Customizing for Cross-Application Components under

Processes and Tools for Enterprise Applications

  Reusable Objects and Functions for BOPF Environment

  PPF

## Adapter for Output Management

## Maintain PPF Settings . In application /SCMTMS/TRANSPORTATION, you

activated the action definition TOR_TPNOR_CO (Replication of Consignment Order) of action profile /SCMTMS/TOR.

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

In exceptional cases, creating a freight booking on an inbound message fails, for example, when the message contains a non-

unique IATA code and at the same time, the departure is already set for the air port of loading. Such a message will fail, and the air

This is custom documentation. For more information, please visit SAP Help Portal.

68


1/14/26, 2:44 PM

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

Especially in a door-to-port scenario, consignment orders and their updates are useful for customers. Depending on the

Incoterms, they might need to know the voyage number and the expected date and time of arrival to organize the pickup and

transport of the goods for the last stage.

## Related Information

Sample Air Freight Process for Shippers (Outbound)

## Consignment Order

## Cargo Left Behind at Port/Airport

Sample Ocean Freight Process for Shippers (Outbound)

Ocean Freight Bookings for Shippers (Outbound)

Advanced Shipping and Receiving

## Cross-Delivery Handling Units

The integration of Transportation Management (TM) with Extended Warehouse Management (EWM) based on outbound deliveries

supports cross-delivery handling units (HU) for the outbound process.

## Use

You can create handling units like cartons or pallets for items from two or more outbound deliveries. This information is passed on

to TM and reflected in the freight unit (FU).

Transportation-driven scenario: Outbound delivery orders are blocked until transportation planning is complete and the status is

set to Ready for Warehouse Processing in the FU, which releases the outbound delivery order. Once you create cross-delivery HUs

and set the status to Ready for Shipping, the system updates TM.

This is custom documentation. For more information, please visit SAP Help Portal.

69


1/14/26, 2:44 PM

Warehouse-driven scenario: Outbound deliveries are released upon creation so you can proceed with warehouse tasks. Once you

set the execution status to Ready for Shipping, EWM updates TM with the cross-delivery HUs' packaging information. In a

warehouse-driven scenario, it is also possible to do transportation planning in parallel. If freight orders (FO) already exist, the

system also updates them with the packaging information.

The system handles the merging of FUs whose items have been packed in cross-delivery HUs in the same way as HUs that contain

items from the same delivery. In TM, a cross-delivery HU is represented as package item in the FU. Therefore, once warehouse

activities are completed, the system merges FUs with identical package items.

Splits can occur at two points in the process. First, an FU would be split after planning if only some items in the order are planned

on the FO and Ready for Warehouse Processing is set. Second, any items not loaded before handling execution status Loading

Completed is set are removed, resulting in an FU split. The FU split subsequently leads to the split of the corresponding outbound

delivery.

Additionally, deliveries packed into cross-delivery HUs can have different sold-to parties but must have the same ship-to party.

Integration with SAP Global Trade Services in Advanced Shipping
and Receiving

Advanced Shipping and Receiving (Advanced SR) supports integration between Transportation Management (TM). and SAP

Global Trade Services (SAP GTS).

## Prerequisites

For both inbound and outbound processes, you can activate the compliance check in the logistics integration profile. For

more information, see Customizing for Transportation Management under

## Integration

 Logistics Integration

## Internal

## TM Component Integration

 Define Logistics Integration Profile for SD, MM, and LE .

Once you activate the compliance check, the system determines compliance for each freight unit. If the criteria for

compliance aren't met, the system prevents any subsequent warehouse steps. For additional information on this status,

see Statuses in Advanced Shipping and Receiving.

You've defined customs activities and customs profiles, and assigned one or more customs activities to each customs

profile. For more information, see Customizing for Transportation Management under  Basic Functions

## Global Trade

 Define Customs Activities and Profiles .

Optionally, you've defined an event profile with Cargo Ready for Loading and defined its settings. For more information, see

Customizing for Transportation Management under  Freight Order Management

 Execution Settings

 Define Event

Profiles .

## GTS Integration in Advanced Shipping and Receiving

Communication between TM and GTS includes compliance relevant checks for, for example, embargos or sanction party lists, and

obtaining clearances such as unloading permits and customs clearance after approval of the export declaration. SAP GTS

performs compliance checks based on freight units and freight orders and export declarations based on consignment or freight

order.

In the outbound process, customs activity is based on either consignment or freight order. In the inbound process, customs

activity is based on the freight order.

The following sections detail the steps in the Advanced SR process that are relevant for GTS integration. For full details of the

process, see End-to-End Process (E2E) for Advanced Shipping and Receiving. For additional information on the statuses

mentioned, see Statuses in Advanced Shipping and Receiving.

This is custom documentation. For more information, please visit SAP Help Portal.

70


1/14/26, 2:44 PM
## Related Information

Integration with SAP Global Trade Services

SAP GTS Integration for the Outbound Process

SAP GTS Integration for the Inbound Process

Statuses in the Integration with SAP GTS (Inbound Process)

Statuses in the Integration with SAP GTS (Outbound Process)

Global Trade

## Event Profiles

## SAP GTS Integration for the Outbound Process

Several steps in the outbound part of the Advanced Shipping and Receiving process are relevant for the integration of a

Transportation Management (TM) system with a SAP Global Trade Services (SAP GTS) system. These steps are detailed below as

a sample process.

For full details of the process, see End-to-End Process (E2E) for Advanced Shipping and Receiving. For additional information on

the statuses mentioned, see Statuses in Advanced Shipping and Receiving.

1. When you save or update a sales order that you have created, the SAP GTS system creates the customs documents and

runs a trade compliance check. SAP GTS returns an overall status for the order with details on the embargo check, watch

list screening status, and legal control statuses. These three statuses are visible on item level, and the system aggregates

these statuses in the header status in the sales order. You can see additional information on a blocked sales order on the

Status tab in the sales order. You can configure the system to assign compliant items of a sales order to an outbound

delivery order.

Each sales document can include a legal split indicator. When you create a freight unit from a sales document, the system

considers the legal split indicator and groups items in freight units accordingly. All items in a freight unit have the same split

indicator. When creating or splitting deliveries, the system considers the legal split indicator on header level of the sales

order and groups the items accordingly.

2. In the delivery-based scenario, when you create the delivery, TM creates the freight units. The SAP GTS system creates the

customs documents and runs a compliance check for all freight unit items. If the trade compliance check hasn't been

completed or if the freight unit is not compliant, the delivery is blocked for warehouse execution. From the delivery, you can

see the document flow on the TM Status tab. The compliance status is listed with a status for a planning block, execution

block, delivery block, and invoicing block.

  Note

In a decentralized EWM and TM setup, the outbound delivery leads to the creation of an outbound delivery order in

EWM. Therefore, TM relies on the outbound delivery order as an indicator of delivery completeness to trigger the

creation of freight units. From there, the process is identical to the one described above.

For freight units that meet the requirements for compliance, the Warehouse Execution status is unblocked and the delivery

is released for warehouse execution.

In the transport-driven process, you must manually set the warehouse processing status of the freight unit to Ready for

Warehouse Processing once compliance is met. For more information, see Transport-Driven Execution.

3. You then create a freight order and can create a consignment order from the freight order. The system runs a compliance

check for the freight order. If you've activated the compliance check in Customizing and, for example, you create a freight

order from a delivery, the system considers the compliance status of the freight units of that delivery. Any blocks affecting

the freight units are displayed on the Blocking Information tab of the freight order.

This is custom documentation. For more information, please visit SAP Help Portal.

71


1/14/26, 2:44 PM

For more information on the creation of freight orders and consignment orders, see Creation and Editing of Freight Orders

and Creation and Editing of a Consignment Order.

4. After you've set the handling execution status of the stop to Checked In, you can start the export declaration process (on

customs group level) for customs groups to be built and assigned to the stop. If you've configured the system to require

loading completion, the export declaration process can be triggered automatically once Set Stop to Loading Completed is

set. TM considers the legal split indicator when it builds customs groups. Once the export declaration processing status is

set to Ready for Export Declaration, the system can send a request to SAP GTS to create a customs declaration. You can

configure the system to include customs invoice data in the request. Alternatively, if you have not configured the automatic

request of customs declarations, choose Request Customs Invoice in the consignment order. If there is a missing customs

clearance, you have the option of preventing the Checked Out status for the stop in the freight order.

Alternatively, if you use handling execution status Cargo Ready for Loading, the system can trigger customs invoice and

export declaration requests before the truck checks in or has even arrived. Depending on your customizing settings in your

Customs Profile, the requests are triggered automatically. You can set Cargo Ready for Loading after the warehouse

processing status is set to Completed. After the truck arrives and items have been loaded, you set the handling execution

status to Loading Completed.

5. Once SAP GTS has approved the customs declaration, the system updates the TM document with a customs reference

number (CRN). With the CRN in place, TM can post goods issue and the freight order can be checked out.

## Related Information

SAP GTS Integration for the Inbound Process

Statuses in the Integration with SAP GTS (Outbound Process)

Integration with SAP Global Trade Services

Explanation of Statuses of Business Documents

## SAP GTS Integration for the Inbound Process

Several steps in the inbound part of the Advanced Shipping and Receiving process are relevant for the integration of a

Transportation Management (TM) system with a SAP Global Trade Services (SAP GTS) system. These steps are detailed below as

a sample process.

For full details of the process, see End-to-End Process (E2E) for Advanced Shipping and Receiving. For additional information on

the statuses mentioned, see Statuses in Advanced Shipping and Receiving.

1. When you create a purchase order, scheduling agreements, or a scheduling agreement delivery schedule, the system

creates freight units. The system checks these freight units for trade compliance and, if the freight unit is not compliant,

the system places a planning block or execution block on them.

2. You create a freight order, and you can create a consignment order from the freight order. For more information on the

creation of freight orders and consignment orders, see Creation and Editing of Freight Orders and Creation and Editing of a

Consignment Order.

If you have configured the system in such a way, it runs a compliance check for the freight order. You can only set the

handling execution status for the stop to Checked In if the freight order is compliant.

3. You must assign a customs reference number (CRN) for each consignment order that is assigned to the freight order

before you can set the warehouse processing status to Ready for Warehouse Processing.

4. To set the warehouse processing status of the warehouse unloading stop to Ready for Warehouse Processing, you need an

unloading permission. The TM system creates a request for unloading permission for each consignment order of the freight

order and sends it to SAP GTS. In addition, the freight unit needs an assignment to the external delivery note number

(document reference with type code 1137) and to the item number.

This is custom documentation. For more information, please visit SAP Help Portal.

72


1/14/26, 2:44 PM

For more information about the receipt of the unloading permission and the related setting of the Ready for Warehouse

Processing status, see Statuses in the Integration with SAP GTS (Inbound Process).

5. After the unloading permission is received, the goods are unloaded. For a basic customs process, you set the status of the

customs groups from the freight order to Ready for Import Declaration. A prerequisite for this step is that the goods

receipt has been performed for all the items of the customs group.

6. You set the handling execution status of the stop to Checked Out.

## Related Information

SAP GTS Integration for the Outbound Process

Integration with SAP Global Trade Services

## SAP GTS Integration in Decentralized EWM and TM

Integration between decentralized EWM and TM and SAP GTS supports the execution of the outbound, or export, process. It

enables you to conduct compliance checks for freight unit and freight order and complete export declaration for consignment and

freight order.

## Supported Systems

The central ERP system must be an S/4HANA system.

## Prerequisites

You have selected the Enable Compliance Check checkbox in your logistics integration profile for decentralized EWM and

TM to activate compliance check at a freight unit level. For more information, see Customizing for Transportation

Management under

## Integration

## Logistics Integration

 Decentralized EWM-TM Integration

## Define Logistics

Integration Profile for EWM .

You have indicated the transportation relevance for sales orders and assigned a logistics integration profile. For more

information, see Customizing for Transportation Management under

## Integration

 Logistics Integration

## Internal TM

## Component Integration

 Define Transportation Relevance of Sales Documents .

You have indicated your output profile under Output Options. Optionally, you can define a customs profile so as to enable

customs activity at the freight unit level. For more information, see Customizing for Transportation Management under

## Planning

 Define Freight Unit Types .

You have enabled compliance check for freight orders and, optionally, entered the customs profile to make your customs

profile relevant for certain customs activities. For more information, see Customizing for Transportation Management

under  Freight Order Managment

## Freight Order

 Define Freight Order Types .

You have indicated your output profile so the PPF actions that send the customs and compliance messages to GTS are

triggered automatically. For more information, see Customizing for Transportation Management under  Freight Order

Managment

## Freight Order

 Define Freight Order Types .

You have indicated your customs and output profiles for consignment orders. For more information, see Customizing for

Transportation Management under  Freight Order Managment

 Consignment Order

 Define Consignment Order

Types .

You have defined your customs activities and profiles. For more information, see Customizing for Transportation

Management under  Basic Functions

## Global Trade

 Define Customs Activities and Profiles .

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

73


1/14/26, 2:44 PM

In a decentralized setup, the Customs Invoice Required checkbox is mandatory and must remain activated.

  Caution

In a decentralized setup, GTS is integrated with TM. To prevent processing errors, you must disable the following functions in

Logistics Execution (LE):

Legal Control Check

Customs Invoice Creation

Export Declaration Request

## Context

## Compliance Check

To check for compliance, GTS carries out the following three checks:

1. Sanctioned Party List Screening: Checks if a business partner is listed on a Sanctioned Party List. If a business partner is

listed, GTS returns a negative compliance confirmation.

2. Embargo Check: Checks if there is an existing embargo between source and destination countries. If an embargo prohibits

trade between those two countries, GTS returns a negative compliance confirmation.

3. Legal Control Check: Some goods require legal control licenses. In case the goods sent to GTS do not comply with the

licensing requirements, GTS returns a negative compliance confirmation.

The legal control check is based on material data including quantities, weights or exchange rates.

## Export Declaration

The export declaration request in TM triggers the creation of the customs documents needed for exporting the goods in the SAP

GTS system.

The customs authorities need data like parties, items, and predecessor documents to confirm the export of the items in a freight

or consignment order. You can resort to your customs invoice, also known as a proforma invoice, to export your goods, but it is not

mandatory. In its absence, the export declaration is based on the goods value of the items in question.

You can cancel an existing export declaration either directly from GTS or request a cancellation from TM.

## Export Declaration Statuses

You will encounter the following status while working with export declarations:

## Status

## Description

## Loading Not Finalized

The loading of goods is yet to be reported

## Pending Customs Invoice Preparation

The loading has been finalized, but the deliveries are not yet up-to-

date

## Ready for Customs Invoice Creation

All requirements are met, the loading has been finalized, and

deliveries are up-to-date

This is custom documentation. For more information, please visit SAP Help Portal.

74


1/14/26, 2:44 PM

## Status

## Description

## Customs Invoice Requested

The request for the creation of a customs invoice has been sent to

the ERP system

## Ready for Export Declaration

Customs invoice has been created, and export declaration request

can be sent to the GTS system

  Note
The export declaration statuses are linked to your customs profile. To set requirements and automate creation, you must first

customize your system. In Customizing, you have the option to activate the following requirements:

Loading Completed Required for Export Declaration

Customs Invoice Required for Export Declaration

Enable Automatic Customs Invoice Creation

## Automatic Export Declaration Request

To enable Customs Invoice Required for Export Declaration, you must first enable Loading Completed Required for Export

Declaration. Furthermore, for Enable Automatic Customs Invoice Creation to function, you must first enable Customs Invoice

Required for Export Declaration.

For more information, see Customizing for Transportation Management under  Basic Functions

 Global Trade

## Define

Customs Activities and Profiles .

## Customer Invoice

In a decentralized EWM and TM setup, you create a customer invoice from your ERP system.

## Sample Process

You can find a sample outbound process description and information concerning statuses under Related Information.

## Related Information

Integration with SAP Global Trade Services

SAP GTS Integration for the Outbound Process

Statuses in the Integration with SAP GTS (Outbound Process)

## Advanced SR for Decentralized EWM and TM

End-to-End Process (E2E) for Advanced Shipping and Receiving (Decentralized)

## Statuses in the SAP Global Trade Services Integration

When Transportation Management is integrated with SAP Global Trade Services as part of the Advanced Shipping and Receiving

process, a specific set of customs processing statuses is used, depending on whether the inbound or outbound process is active.

## Related Information

Statuses in the Integration with SAP GTS (Inbound Process)

Statuses in the Integration with SAP GTS (Outbound Process)

This is custom documentation. For more information, please visit SAP Help Portal.

75


1/14/26, 2:44 PM

Export Declaration Processing Statuses and Customs Profile Customizing

Statuses in the Integration with SAP GTS (Outbound Process)

If a road freight order, consignment order, or freight unit is relevant for a customs or compliance process, the following sample

sequence of activities takes place in Transportation Management (TM) during integration with an SAP Global Trade Services (SAP

GTS) system.

The activities are described in terms of the statuses used in the outbound process. For full details about statuses in the outbound

process of Advanced Shipping and Receiving, see Statuses in the Outbound Process.

## Prerequisites

You have made the following settings:

You have assigned a customs profile in the Customizing for a freight order type and consignment order type. A customs

profile contains one or more customs activities that control customs handling for a specific process (for example, export or

transit). For more information, see Customizing for Transportation Management under  Freight Order Management

## Freight Order

 Define Freight Order Types  or  Freight Order Management

 Consignment Order

## Define

Consignment Order Types .

You have enabled a compliance check in the road freight order and freight unit.

For more information on setting up customs activities, for example, to display customs statuses in a document, see Configuration

of Customs Processing.

To determine whether a business document is relevant for a customs process, see Customs Relevance Check.

Outbound Process

## Compliance Check

In the outbound process, when you create or modify freight units, a compliance check is started by the SAP GTS system for all

freight units. If SAP GTS can’t complete the compliance check or if the freight units are not compliant, the outbound delivery order

and the freight units are blocked for execution. The system doesn't set the warehouse processing status of the freight unit to

Ready for Warehouse Processing.

A freight unit that was previously compliant may also receive an update that makes the freight unit non-compliant. For example, a

business partner is placed on the sanctioned party list after a screening has taken place. In this case, if the warehouse processing

status is Ready for Warehouse Processing, the status will be reversed and set to Not Started. If the warehouse processing status

was already set to In Process, it cannot be reversed.

After the compliance-related block is resolved, the system automatically sets the status of the freight unit to Ready for Warehouse

Processing and you can proceed with the warehouse execution.

In the transport-driven process, you must manually set the warehouse processing status of the freight unit to Ready for

Warehouse Processing. You can also manually reverse the warehouse processing status to Not Started, as long as warehouse

activities have not begun. For more information about the transport-driven process, see Transport-Driven Execution.

If you use the compliance process and the transport-driven process together, you must manually set the status to Ready for

Warehouse Processing, after compliance has been met. However, if there is a need for a second compliance check, the system will

automatically set the Ready for Warehouse Processing status after compliance is met again, and only if you had manually set it

before.

This is custom documentation. For more information, please visit SAP Help Portal.

76


1/14/26, 2:44 PM

## Customs Process

For the customs processes, if a road freight order has several shipping points, then the consignment order can be used as the main

document.

The basic sequence of statuses and activities in the outbound process is as follows:

1. When you set the execution status of the road freight order to Ready for Transportation Execution, the system checks all

the execution blocks that are set for the road freight order and the consignment order. If the execution block is only

relevant for customs processes, you can proceed with execution of the road freight order and allow the truck to load. You

can see the blocks and the block reasons on the Blocking Information tab in the document. The reason for the block for

customs processes can be, for example, that there's a missing export declaration for the road freight order.

  Remember

You have the option of using handling execution status Cargo Ready for Loading, which allows you to trigger customs

invoice and export declaration requests before the truck checks in or has even arrived. With Cargo Ready for Loading,

the requests are triggered automatically after the warehouse processing status is set to Completed instead of after

Loading Completed.

2. After the truck arrives at the gate, you set the handling execution status for the stop to Arrived.

3. If the documents of the goods on the truck match the documents in the system, you set the handling execution status for

the stop to Checked In.

4. After the goods are loaded on the truck, you can set the handling execution status of the items and the warehouse loading

stop to Loaded, even if there's a block that's relevant for customs processes. If you've configured the system to require

loading completion, when the status is set to Loaded, the export declaration status changes to Pending Customs Invoice

Preparation. Once the deliveries are up-to-date, the export declaration status changes to Ready for Customs Invoice

Creation, and TM requests a customs invoice from the ERP.

After receiving the customs invoice, the export declaration processing status changes to Ready for Export Declaration. TM

sends a request to SAP GTS to create a customs declaration and includes a customs invoice in the request.

You can see the export declaration processing status and the customs status on the Customs tab of the road freight order

or consignment order.

  Note

In a decentralized EWM and TM setup, you will find one additional status: Customs Invoice Requested, which indicates

that a request for a customs invoice has been sent to the ERP system.

5. If the export declaration is missing or incomplete, you can't set the handling execution status for the stop to Checked Out

because the block related to the customs process still exists. After the customs authorities approve the customs

declaration, SAP GTS updates the road freight order and the assigned consignment order. You can then set the status to

Checked Out.

For more information about SAP GTS integration in the outbound process of Advanced Shipping and Receiving, see SAP

GTS Integration for the Outbound Process.

6. After you post goods movement for the complete road freight order, you can create a customer invoice for the Logistics

Execution (LE) or Extended Warehouse Management (EWM) outbound delivery order assigned to the road freight order.

You can also cancel the customer invoice.

For more information about SAP GTS, see SAP Library for SAP Global Trade Services on SAP Help Portal at

http://help.sap.com/grc under SAP Global Trade Services.

This is custom documentation. For more information, please visit SAP Help Portal.

77


1/14/26, 2:44 PM
## Related Information

Integration with SAP Global Trade Services

Statuses in Advanced Shipping and Receiving

Statuses in the Integration with SAP GTS (Inbound Process)

SAP GTS Integration in Decentralized EWM and TM

Statuses in the Integration with SAP GTS (Inbound Process)

If a road freight order or consignment order is relevant for a customs process, the following sample sequence of activities takes

place in Transportation Management (TM) during integration with an SAP Global Trade Services (SAP GTS) system.

The activities are described in terms of the statuses used in the inbound process. For full details about statuses in the inbound

process of Advanced Shipping and Receiving, see Statuses in the Inbound Process.

## Prerequisites

You have assigned a customs profile in the Customizing for a freight order type and consignment order type. A customs profile

contains one or more customs activities that control customs handling for a specific process (for example, export or transit). For

more information, see Customizing for Transportation Management under  Freight Order Management

 Freight Order

## Define

Freight Order Types  or  Freight Order Management

## Consignment Order

 Define Consignment Order Types .

For more information on setting up customs activities, for example, to display customs statuses in a business document, see

Configuration of Customs Processing.

To determine whether a business document is relevant for a customs process, see Customs Relevance Check.

## Inbound Process

The basic sequence of statuses and activities in the inbound process is as follows:

1. If the documents of the goods on the truck match the documents in the system, you set the handling execution status for

the stop to Checked In. This triggers the building of customs groups. The system sends a request for unloading permission

to the SAP GTS system and sets an execution block for the road freight order because the approval for the unloading

permission is pending. The system automatically sets the status of the customs activity to Unloading Requested on the

Customs tab in the road freight order.

If you reverse the Checked In status after a block caused by a missing unloading permission is set for the road freight

order, the block is not reversed.

For more information on the process to secure approval from SAP GTS to unload a road freight order, see Customs Transit

Discharge.

2. You set the warehouse processing status to Ready for Warehouse Processing at the warehouse unloading stop level to

signal to the warehouse that they can begin their activities. However, because the unloading permission from the customs

authorities hasn't been received yet, the system creates the Ready for Warehouse Processing event but also blocks it from

being processed. You can see the events under the Execution tab of the road freight order. The warehouse processing

status is Not Started.

If you don't have an explicit check-in process at your company gate, you can directly set the warehouse processing status

to Ready for Warehouse Processing at the warehouse unloading stop level. The system automatically sets the Checked In

status at the stop level, creates the Ready for Warehouse Processing event, and blocks it from being processed.

This is custom documentation. For more information, please visit SAP Help Portal.

78


1/14/26, 2:44 PM

3. After SAP GTS sends an approval for the unloading permission, the system sets the status of the customs activity to

Unloading Approved. The system then processes the Ready for Warehouse Processing event and sets the warehouse

processing status of the warehouse unloading stop to Ready for Warehouse Processing. Alternatively, you can manually

overrule the block under the Blocking Information tab to trigger the processing of the Ready for Warehouse Processing

event.

On the item level, you can set the Ready for Warehouse Processing status for freight units only if you have entered an

external delivery note number.

4. When unloading is completed, you can set the handling execution status for the items and the warehouse unloading stop to

Unloaded. You can then create the customs import declaration for the stop.

You can see the import declaration status and the unloading permission status on the Overview tab.

For more information about SAP GTS integration in the inbound process of Advanced Shipping and Receiving, see SAP GTS

Integration for the Inbound Process.

For more information about SAP GTS, see SAP Library for SAP Global Trade Services on SAP Help Portal at

http://help.sap.com/grc under SAP Global Trade Services.

## Related Information

Integration with SAP Global Trade Services

Statuses in Advanced Shipping and Receiving

Statuses in the Integration with SAP GTS (Outbound Process)

Export Declaration Processing Statuses and Customs Profile
## Customizing

The export declaration processing statuses indicate what stage of the Advanced Shipping and Receiving export process you find

yourself in and what steps you need to take to progress the process.

The statuses appear based on your Customizing settings. For example, if you set a customs invoice as a prerequisite to the export

declaration. Additionally, you can choose to automate both customs invoice and export declaration requests. For more

information, see Customizing for Transportation Management under  Basic Functions

 Global Trade

## Define Customs

Activities and Profiles .

Export Declaration Processing Statuses

## Status

## Description

## Loading Not Finalized

The handling execution status of the relevant stop has not been set

to loading completed.

## Pending Customs Invoice Preparation

The LE and EWM deliveries have not been updated so the

warehouse distribution status (LIKP-VLSTK) is not yet C.

Ready for Customs Invoice Creation

The customs invoice can be requested.

When EWM is not involved, this stage is reached after loading has

been completed. When EWM is involved, the status shows after you

have created the final outbound delivery order and the LE delivery

has been updated.

In a decentralized set-up, EWM updates LE after you create the

outbound delivery order in EWM, LE confirms, and EWM updates

This is custom documentation. For more information, please visit SAP Help Portal.

79


1/14/26, 2:44 PM

## Status

## Description

TM. In TM, you can find the final outbound delivery number under

item document reference.

## Customs Invoice Requested

The request for a customs invoice has been sent via web service.

This status is only visible in decentralized EWM and TM.

## Ready for Export Declaration

The final status indicates that all prerequisites have been met, and

the export declaration can be requested.

## Related Information

Integration with SAP Global Trade Services

## Integration with Extended Warehouse Management

You can integrate Transportation Management (TM) with Extended Warehouse Management (EWM) in various ways:

## Direct integration

Within the direct integration, you have the following options:

Integration based on freight orders (this type of integration is often used by shippers)

Integration based on deliveries and EWM transportation units (this type of integration is often used by shippers)

Integration based on execution documents resulting from forwarding orders (transit warehousing; this type of

integration is often used by logistics service providers)

Warehouse billing

## Systems

Integration Based on Freight Orders (Advanced Shipping and Receiving)

For an integration based on freight orders, you can integrate TM inSAP S/4HANA with EWM in SAP S/4HANA, both located in the

same system.

For more information, see Advanced Shipping and Receiving.

## Integration Based on EWM Transportation Units

For an integration based on EWM transportation units, you can integrate TM in SAP S/4HANA with the following EWM systems:

## EWM embedded in SAP S/4HANA

Decentralized EWM based on SAP S/4HANA (as an external system)

SAP EWM (decentral SAP EWM as an external system)

For more information about EWM integrated as an external system, see SAP Note 2952651

.

The integration of TM and EWM both embedded in SAP S/4HANA and the integration of TM with EWM as an external system

support the same processes.

This is custom documentation. For more information, please visit SAP Help Portal.

80


1/14/26, 2:44 PM

For more information about the processes in EWM in SAP S/4HANA, see https://help.sap.com/s4hana under  Product

## Assistance

 Enterprise Business Applications

## Supply Chain

 Extended Warehouse Management

.

For more information about the processes in SAP EWM, see http://help.sap.com/ewm  under  Application Help

 SAP

Extended Warehouse Management (SAP EWM)

.

## Features

Integration Based on Freight Order (Advanced Shipping and Receiving)

Advanced Shipping and Receiving is a streamlined and integrated, end-to-end process that allows users to send, receive, and

transport products. It supports mixed and multi-warehouse scenarios within one freight order. It helps you, to coordinate the

process steps from arrival of trucks at the gate to the final goods receipt in the warehouse.

For more information, see Advanced Shipping and Receiving.

## Integration Based on EWM Transportation Units

You can integrate TM and EWM directly. Communication is based on the deliveries that are sent from Logistics Execution (LE) to

EWM and TM. The TM planning results are transferred directly to EWM. Transportation units are automatically created in the

warehouse. Together with the delivery information, these form the basis for warehouse planning and execution. Confirmations of

the execution results (such as loading and quantity discrepancies) are sent directly from EWM to TM.

For more information, see Integration Based on EWM Transportation Units.

## Transit Warehousing

You can integrate TM and EWM directly. Communication is based on execution documents resulting from forwarding orders. The

TM planning results are transferred directly to EWM. Transportation units and deliveries are automatically created in the

warehouse and form the basis for warehouse planning and execution. Confirmations of the execution results (such as loading and

quantity discrepancies) are sent directly from EWM to TM.

For more information, see Transit Warehousing.

## Warehouse Billing

You can sell and purchase warehouse services using the direct integration of TM with EWM. Integration is based on agreement

documents, service orders, and forwarding orders.

For more information, see Warehouse Billing.

## Integration Based on EWM Transportation Units

You can integrate Transportation Management (TM) with Extended Warehouse Management (EWM) based on the EWM

transportation unit (TU).

## Prerequisites

For more information, see Prerequisites for Integration Based on EWM TUs.

## Supported Processes

This is custom documentation. For more information, please visit SAP Help Portal.

81


1/14/26, 2:44 PM

The integration is based on the EWM-TU. For more information about the integration based on the freight order, see Advanced

Shipping and Receiving.

For the integration based on the EWM TU, the following processes are supported for road freight orders:

Delivery-Based and Order-Based Planning (Outbound)

In TM, you can plan your transportation activities based on an outbound delivery or based on an order and send your

freight orders to EWM. In EWM, the warehouse workers carry out the steps relating to the warehouse, for example, loading,

picking, packing and staging. Because the two systems are integrated with one another, EWM sends a message to update

TM when the truck departs. TM updates the freight order and the associated freight units.

In addition, you can enable updates from EWM to TM with status Loading Finished. For more information, see Early

Updates from EWM.

A detailed standard sample process is available. For more information, see Example Process: Delivery- and Order-Based

Planning (Outbound).

For more information about delivery-based and order-based integration in Logistics in general, see Integration of Orders

and Deliveries in Transportation Planning.

Delivery-Based and Order-Based Transportation Planning (Inbound)

In TM, you can plan your transportation activities based on an inbound delivery or based on an order and send your freight

orders to EWM. In EWM, the warehouse workers carry out the steps relating to the warehouse, for example, unloading.

For more information, see Example Process: Delivery- and Order-Based Planning (Inbound).

  Note

In the inbound scenario, EWM does not send information on cargo back to the freight order in TM when the truck

departure is posted in EWM. Therefore the item hierarchy is not changed in the freight order, even if the items were not

all received in EWM.

Further processes:

Transportation Planning with Trailers

Stock Transport Order Process

## Early Picking

Multi-Pickup, Multi-Drop

Cross-Delivery Handling Units

Execution-Driven Planning (Outbound)

  Note
When you define the freight unit building rule, make sure that freight units are not split for order items or delivery items.

  Example

You have defined a freight unit building rule with a split quantity of 1,500 kg. If you have an item that weighs 2,000 kg, TM

creates two freight units: one freight unit with 1,500 kg and another with the remaining quantity of 500 kg. If a

LoadingAppointment message is then sent to EWM as part of the integration, the request cannot be executed correctly.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

82


1/14/26, 2:44 PM

Deliveries to a transportation stop that originate from warehouses with different warehouse numbers are not supported. It is

not relevant whether the warehouse numbers are from the same EWM system or from different EWM systems.

For information about the supported functions and the restrictions, see SAP Note 3018355

.

## DTR and OTR

Some features, like delivery-based transportation requirements (DTR) or order-based requirements (OTR), are only relevant if TM

is integrated with external logistics systems. This means, the logistic systems (such as Logistics Execution, Sales and

Distribution, or Materials Management) are not located in the same system as TM. For more information, see External TM System

Integration.

## Features

When is the System Updated?

TM

EWM

When you have finished planning your transportation activities, you set the load plan status or unload plan status on

stop level to Finalized. The system automatically sends a loading or unloading instruction to EWM with the message

LoadingAppointmentRequest.

When you choose  Follow Up

 Send Loading Instruction or Send Unloading Instruction . The system sends a

LoadingAppointmentRequest message to EWM.

If you enable “early updates", the system sends an additional LoadingAppointmentNotification message to

TM when the warehouse workers set the status Loading Finished.

When the warehouse workers set the status Arrival at Checkpoint and Departure from Checkpoint. The system

sends a LoadingAppointmentNotification message to TM.

When the warehouse workers post the goods issue or goods receipt. The system updates the outbound or inbound

delivery in Logistics Execution (LE).

Only the messages sent with Finish Loading and Departure from Checkpoint are content-related and contain a full image of the

item hierarchy. All other messages and reversals only contain status and event information.

## Displaying Data

The warehouse numbers from EWM are displayed in the following locations:

Delivery-based transportation requirement: Locations and Dates/Times tab page

Freight order: Overview tab page for the stop

## Changing Data

Data changes in EWM are replicated to TM, for example:

Item hierarchy

## Carrier

Relevant dates and times, such as arrival time at the yard

## Gross weight of the vehicle

This is custom documentation. For more information, please visit SAP Help Portal.

83


1/14/26, 2:44 PM

Packaging material

## Updating Data

The item hierarchy of the freight order is updated with the information about the EWM transportation unit. Associated

freight units are updated accordingly.

## Updates on Freight Units

If the warehouse workers have packed items in different handling units in EWM, the items for these handling units

are created automatically in TM.

Reassignment of freight units: If the warehouse workers load deliveries from a different freight order, the system

automatically changes the assignment of the corresponding freight units. This means that these freight units are

removed from the other freight order and reassigned to the new freight order.

If you assign a freight unit to a transportation unit in EWM but the freight unit is not assigned to a freight order in

TM, this information is also transferred to TM. The system then automatically assigns the freight unit to the

corresponding freight order.

If you reassign a complete delivery in EWM from one transportation unit to another, EWM reports the reassignment to TM.

In TM, the delivery is automatically reassigned from the original freight order to the other freight order (corresponding to

the assigned transportation unit im EWM).

Actual quantities from EWM are automatically transferred to TM. For more information, see Quantity Deviation.

Actual dates are also reported automatically to TM.

## Status Updates

## LoadingAppointmentRequest

If you set the load plan status on stop level to Load Plan Finalized for your freight order, the system automatically

triggers the event Ready for Loading. The system transfers the event to the predecessor document and changes its

status to Load Plan Finalized. If so, the freight unit is no longer updated from LE but from EWM.

The same applies for the load plan status Unload Plan Finalized and the event Ready for Unloading.

## LoadingAppointmentNotfication

If TM receives the LoadingAppointmentNotfication message during outbound-delivery-based

transportation planning, the cargo receipt status for the item is automatically set to Shipped. If the item in question

is to be unloaded at the next transportation stop, the handling execution status is automatically set to Not

Unloaded. In the associated freight unit, the cargo receipt status is also set automatically to Shipped. As a result,

the freight unit is no longer updated from the freight order or the delivery-based transportation requirement.

The communication history for inbound documents is updated regarding arrival at checkpoint and departure of

checkpoint.

The execution status is set to In Execution.

## Reversal of Departure From Checkpoint

Reversal of the departure and the sending of a second departure message from EWM to TM is enabled for inbound and outbound

processes. For more information, see Reversal of Departure.

## Canceling Documents

For inbound processes you can still cancel freight orders up until the goods have arrived in the warehouse and have been reported

by EWM as Arrived. If the status Unload Plan (Stop) Finalized has already been set and you cancel the freight document, the

This is custom documentation. For more information, please visit SAP Help Portal.

84


1/14/26, 2:44 PM

system sends a cancellation request to EWM. This request is checked and processed by the EWM system as follows:

If the goods have not yet arrived in the warehouse, EWM confirms the cancellation, and the life cycle status of the freight

document is changed to Canceled.

If the handling execution status at stop level has already been changed to Arrived, the system sets the Transmission-to-

EWM Status to Partially Received or Received. Execution of the transportation continues and the freight document cannot

be canceled. In some cases, you can reverse the arrival and then cancel the freight document.

The freight document in TM can be canceled only if cancellation has been confirmed by EWM and reported to TM.

For more information about canceling freight orders and stops in multi-pickup, multidrop scenarios, see Multi-Pickup, Multi-Drop.

## Messaging

Transmission-to-EWM Status provides information about the status of the exchange of messages. For more information, see

Explanation of Statuses of Business Documents.

More Information

Logistics Integration

## Transportation Stops

## Prerequisites for Integration Based on EWM TUs

This topic describes prerequisites for the integration of Transportation Management (TM) with Extended Warehouse Management

(EWM) based on EWM transporation units (TU).

## Prerequisites for Special Functions

Prerequisites for special functions that need to be set in the system are described under these functions. For example:

Stock Transport Order Process

Early Updates from EWM

## Delivery Split

Transportation Planning with Trailers

## Early Picking

Multi-Pickup, Multi-Drop

Execution-Driven Planning (Outbound)

## General Prerequisites

The use of deliveries is a prerequisite for the TM-EWM integration.

## Settings for Freight Order Type

You have configured the following settings in your freight order type:

You have selected the Transportation Activity Creation in EWM option in the Document Creation Relevance field.

This is custom documentation. For more information, please visit SAP Help Portal.

85


1/14/26, 2:44 PM

You have assigned an existing EWM integration profile or have created your own profile.

You have specified an output profile that contains actions for sending loading/appointment messages, for example,

/SCMTMS/TOR.

In section Basic Settings, you have defined the stage sequence type by selecting one of the following options:

## Defined and Linear

## Star-Shaped Based on FU Stages

For more information, see Customizing for Transportation Management under  Freight Order Management

 Freight

## Order

 Define Freight Order Types .

Settings for Codes and Event Reason Codes

## Predefined Codes

SAP provides the following, predefined event codes for cancelations as well as the corresponding event reason codes.

These event codes are set as default codes:

Event Code

## Name

Event Reason Code

## Name

## CANCEL_EXEC_DOC

Cancel Execution Document

CANCELLED_BY_CARRIER

Canceled by Carrier

CANCEL_STATUS_RESET

Cancel and Reset Cargo

TM_PLAN_NOT_READY

TM Planning Not Yet Ready

Execution Status

CANCEL_UNASSIGN_FUS

Cancel and Unassign FUs of

STOP_CANCELLED

Loading Appointment

## Current Stop

Canceled (loading cannot be

executed in the warehouse as

planned)

## Definition of Own Codes and Event Reason Codes

You can define your own event codes and event reason codes. For each event type, you must specify at least one of your

event codes as the default code.

For more information, see Customizing for Transportation Management under  Basic Functions

## General Settings

 Define Event Reason Codes .

## Prerequisites for Logistics Integration with External Systems

The following settings are only relevant if TM is integrated with external logistics systems.

In Customizing you have activated the direct integration with EWM for your delivery-based transportation requirements. This

means that you have set the option Direct EWM Integration in the Dir. EWM Int. Active field. For more information, see

Customizing for Transportation Management under

## Integration

  Logistics Integration

  External TM System Integration

Delivery-Based Transportation Requirement

  Define Delivery-Based Transportation Requirement Types .

For more information, see External TM System Integration.

## Early Updates from EWM

The integration of Transportation Management (TM) with Extended Warehouse Management (EWM) based on EWM

transportation units (TUs) supports sending early updates from EWM to TM. “Early update” means updating the item hierarchy in

This is custom documentation. For more information, please visit SAP Help Portal.

86


1/14/26, 2:44 PM

TM with status change Finish Loading, which is earlier than with status Departure from Checkpoint.

## Prerequisites

Make the following settings in EWM Customizing to enable early updates for the integration based on EWM TUs:

In the settings for TM message processing define that messages are sent multiple times for your logical system.

For more information, see Customizing for SCM Extended Warehouse Management under  Extended Warehouse

Management

  Interfaces

## TM Integration

  Make Settings for TM Message Processing .

For the used process profile mark HU Update.

For more information, see Customizing for SCM Extended Warehouse Management under  Extended Warehouse

## Management

  Cross-Process Settings

  Delivery – Warehouse Request

  Process Management and Control

## Define

Process Profile for Document Header

.

## Use

With “early updates” in TM-EWM integration customers can print the documents earlier in the process.

By default, the data in TM is updated with the departure of the EWM transportation unit from the checkpoint.

In EWM Customizing you can define that this additional, earlier LoadingAppointmentNotification (LDAP) message is sent

from EWM to TM with loading completion. The item hierarchy of the freight order is updated with the information about the EWM

transportation unit. Associated freight units are updated accordingly. The LDAP message signalling departure from checkpoint is

still sent, even though an earlier LDAP message was sent. The deliveries in Logistics Execution (LE) are also updated before Goods

Issue.

It is possible to withdraw the status Finish Loading. This gives a chance to perform last minute changes to the load.

## Update Check for Delivery or DTR

Check to verify that content-related messages are not processed before the delivery has been updated. For more information, see

Reprocessing of Failed Loading Appointment (LDAP) Messages.

## Reprocessing of Failed Loading Appointment (LDAP) Messages

In the integration of Transportation Management (TM) with Extended Warehouse Management (EWM) based on EWM

transportation units (TUs), you can run into issues with the LDAP message processing. Temporary issues cause errors when an

LDAP message is processed. The temporary issue resolves by itself, but the LDAP message remains in a failed state.

  Example

The freight order is locked by another user and is not updated by the LDAP message.

Update check for delivery or DTR: There is a check to verify that content-related messages are not processed before

the delivery has been updated.

For the LDAP messages sent with Loading Finished or Departure from Checkpoint, the system checks if all relevant

deliveries in Logistics Execution are already updated by EWM. In distributed system scenarios, the system checks if all

delivery-based transportation requirements (DTRs) are already updated. If the up-to-date check fails, an error message

with the reason for the failure is displayed, and the system will not update the TM data.

This is custom documentation. For more information, please visit SAP Help Portal.

87


1/14/26, 2:44 PM
## Reprocess Failed LDAP Messages

If an LDAP message fails, we recommend using the Forward Error Handling service (FEH). FEH is a concept that enables errors

that are detected during the execution of asynchronous services to be processed on the provider side. This concept is

implemented using the Error and Conflict Handler (ECH).

Define a regular automatic retry in a resolution strategy to process the LDAP message as soon as the issue is resolved (for

example, the delivery or DTR has been updated). For more information, see Customizing for Cross-Application Components under

Processes and Tools for Enterprise Applications

  Enterprise Services

  Error and Conflict Handler

  Define Resolution

Strategy .

To define the resolution strategy use component CA-SOA-ESM-SCM-SCE and define the retry conditions for error category

PRE.TEE.LRE.

For more information, see SAP Note 3372289

.

Related Information

Early Updates from EWM

## Multi-Pickup, Multi-Drop

Example Process: Delivery- and Order-Based Planning
(Outbound)

In Transportation Management (TM), you can plan your transportation activities based on an order or a delivery and send your

freight orders to Extended Warehouse Management (EWM). In EWM, you can then carry out the steps relating to the warehouse,

for example, loading, picking, packing and staging.

Because the two systems are integrated with one another, EWM sends a message to update TM when the truck departs. The

example process below describes a standard outbound process for TM-EWM integration.

If you enabled “early updates" the system sends an additional LoadingAppointmentNotification message to TM when the

warehouse workers set the status Loading Finished.

## Prerequisites

For more information, see Prerequisites for Integration Based on EWM TUs.

## Preparation in SD

You create a sales order in Sales and Distribution (SD).

Order-Based Planning

## Delivery-Based Planning

Outbound deliveries are created later on.

You create outbound deliveries for the sales order and distribute

them to TM and EWM.

Transportation Planning in TM

1. Freight units are created automatically.

This is custom documentation. For more information, please visit SAP Help Portal.

88


1/14/26, 2:44 PM

Order-Based Planning

## Delivery-Based Planning

Once the sales order is saved, TM creates freight units.

With the delivery in Logistics Execution (LE), freight units are

automatically created in TM, and an outbound delivery order is

created in EWM.

As an optional step the system can create packages when freight units are created. For more information, see Unified

Package Building in Integration Based on EWM TUs.

Only relevant for integration with external logistics systems: In TM, a delivery-based transportation requirement is

automatically created along with the associated freight units. For more information, see External TM System Integration.

2. You create a road freight order.

You plan your transportation activities by creating a road freight order based on the freight units created in the previous

step.

3. You create an outbound delivery.

Order-Based Planning

## Delivery-Based Planning

You create outbound deliveries for the freight order.

Deliveries have already been created.

The deliveries are then transferred back from LE to TM and the

delivery reference is added automatically to the freight order.

The delivery reference is displayed in the document references

for the item. In EWM, an outbound delivery order is created.

  Note

The deliveries are only created if enough stock is available in

the plant or storage location defined in the sales order.

4. You finalize the load plan.

When you have finished planning your transportation activities, you set the load plan status of the freight order on stop

level to Load Plan Finalized. The system automatically sends a loading instruction to EWM with the message

LoadingAppointmentRequest.

  Note

In this step, the system checks whether outbound deliveries have already been created. The system can change the

status and send the message only if outbound deliveries have already been created.

You can plan multiple warehouses on one road freight order. For more information, see Multi-Pickup, Multi-Drop.

## Execution in EWM

When the LoadingAppointmentRequest message is received from TM, EWM automatically creates a transportation unit.

1. Picking (and possibly packing) is carried out by the warehouse workers.

2. When the truck arrives at the yard, the warehouse workers assign a door to it and report its arrival.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

89


1/14/26, 2:44 PM

By posting Arrival at Door, Arrival at Checkpoint is posted automatically (if not already done manually).

3. The warehouse workers load the truck.

The following functions are supported:

Cross-Delivery Handling Units

Quantity Deviation

Delivery Split

Batch Split

## Seals

Optional, if configured: Warehouse workers post when they finish loading the truck. EWM sends an additional

LoadingAppointmentNotification message to TM. For more information, see Early Updates from EWM.

For more information about loading, see Loading and Unloading.

4. The warehouse workers post the goods issue. The outbound delivery is automatically updated in LE.

5. The warehouse workers post the departure of the truck. EWM sends the LoadingAppointmentNotification

message to TM.

Update and Further Steps in TM

## Freight Order

1. When the LoadingAppointmentNotification message is received, TM updates the item hierarchy of the freight

order with the EWM transportation unit data and updates the associated freight units.

Order-Based Planning

## Delivery-Based Planning

Only relevant for integration with external logistics systems:

Only relevant for integration with external logistics systems:

When the data is updated in LE, the order-based transportation

When the data is updated in LE, the delivery-based

requirement (OTR) is automatically updated in TM.

transportation requirement (DTR) is automatically updated in

TM.

For more information about the data and status updates, see Integration Based on EWM Transportation Units.

2. You complete freight order execution.

## More Information

For more information about the processes in EWM, see https://help.sap.com/s4hana under  Product Assistance

 Enterprise Business Applications

## Supply Chain

 Extended Warehouse Management

.

For more information about the processes in SAP EWM, see http://help.sap.com/ewm  under  Application Help

 SAP

Extended Warehouse Management (SAP EWM)

.

Example Process: Delivery- and Order-Based Planning (Inbound)

The integration of Transportation Management (TM) with Extended Warehouse Management (EWM) supports delivery-based

planning and execution of products.

This is custom documentation. For more information, please visit SAP Help Portal.

90


1/14/26, 2:44 PM

In TM, you can plan your transportation activities based on an inbound delivery and send your freight orders to EWM. In EWM, you

can carry out the steps relating to the warehouse, for example, unloading. The example below describes a process for delivery-

based and order-based transportation planning (inbound).

## Prerequisites

For more information, see Prerequisites for Integration Based on EWM TUs.

## Process

## Preparation in MM

You create a purchase order in Materials Management (MM).

Order-Based Planning

## Delivery-Based Planning

You can plan in MM and distribute it to TM.

You create inbound deliveries for the purchase order and distribute

them to TM and EWM.

With the delivery in Logistics Execution (LE), freight units are

automatically created in TM, an inbound delivery order is created in

EWM.

Only relevant for integration with external logistics systems: In TM,

Only relevant for integration with external logistics systems: In TM,

an order-based transportation requirement (OTR) is automatically

a delivery-based transportation requirement (DTR) is automatically

created along with the associated freight units.

created along with the associated freight units.

## Transportation Planning in TM

1. You plan your transportation activities by creating a freight order based on the freight units created in the previous step.

2. When you have finished planning your transportation activities, you set the load plan status of the freight order on stop

level to Unload Plan Finalized. The system automatically sends an unloading instruction to EWM with the message

LoadingAppointmentRequest.

  Note

In this step, the system checks whether inbound deliveries have already been created. The system can change the

status and send the message only if inbound deliveries have already been created.

You can plan multiple warehouses on one road freight order. For more information, see Multi-Pickup, Multi-Drop.

## Execution in EWM

1. When the LoadingAppointmentRequest message is received from TM, EWM automatically creates a transportation

unit.

2. When the truck arrives at the yard, the warehouse workers post its arrival.

3. The warehouse workers unload the truck. For more information, see Loading and Unloading.

4. The warehouse workers post the goods receipt. The inbound delivery is automatically updated in LE.

5. The warehouse workers carry out any additional steps in EWM, such as putaway.

6. With posting truck departure, EWM sends an LoadingAppointmentNotification message to TM.

This is custom documentation. For more information, please visit SAP Help Portal.

91


1/14/26, 2:44 PM

## Update in TM

When the LoadingAppointmentNotification message is received, TM updates freight order.

  Note

In the inbound scenario, EWM does not send information on cargo back to the freight order in TM when the truck departure is

posted in EWM. Therefore the item hierarchy is not changed in the freight order, even if the items were not all received in EWM.

Order-Based Planning

## Delivery-Based Planning

Only relevant for integration with external logistics systems: When

Only relevant for integration with external logistics systems: When

the data is updated in LE, the order-based transportation

the data is updated in LE, the delivery-based transportation

requirement (OTR) is automatically updated in TM.

requirement (DTR) is automatically updated in TM.

More Information

Quantity Deviation

Delivery Split

Batch Split

## Seals

## Stock Transport Order Process

The integration of Transportation Management (TM) with Extended Warehouse Management (EWM) based on EWM

transportation units (TUs) supports processes with stock transport orders (STOs). If a relocation of stock is necessary, you can

use STOs to move stock between two plants within one company (code).

## Use

The stock transport order process can be used, for example, by shippers that own more than one EWM warehouse and use the TU-

based integration with EWM installed on a separate system.

For an order-based STO process, you start with a stock transport order (a purchasing document). You plan the resulting freight

units on a road freight order and create an outbound delivery. The reason the first delivery in the process is an outbound delivery is

because the outbound process from the supplying EWM warehouse is processed first. Posting goods issue then initializes the

creation of an inbound delivery that is needed for the follow-on inbound process in the receiving EWM warehouse.

For a delivery-based STO process, the outbound delivery is created directly from the STO. You then plan the resulting freight units

on a road freight order. The rest of the process works like the standard order-based STO process described below.

In the end, there are two EWM transportation units (TUs) created in the STO process: one outbound TU in the sending, issuing

warehouse, and one inbound TU in the receiving warehouse.

For information about restrictions on the STO process, see 3158252

.

## Prerequisites

## General Prerequisites

This is custom documentation. For more information, please visit SAP Help Portal.

92


1/14/26, 2:44 PM

Delivery Management and Transportation Management must run on the same system.

Other Prerequisites

## Materials Management

You have defined a stock transport order type with an item category that allows stock transfer.

For more information, see Customizing for Materials Management under  Purchasing

## Purchase Order

Define Document Types for Purchase Order

.

You have configured the delivery type for the combination of the STO type and plant.

For more information, see Customizing for Materials Management under  Purchasing

  Purchase Order

  Set up

## Stock Transport Order

  Configure Delivery Type & Availability Check Procedure by Plant

.

## Delivery Management

For the stock transport order process, you have defined the inbound delivery creation in the receiving plant. For the delivery

creation, you need to enter a confirmation control key that allows the creation of inbound deliveries in the STO tab

Confirmation.

You can automate the determination of the confirmation control key in the STO. For more information, see Customizing for

Logistics Execution under  Shipping

## Deliveries

  Define Order Confirmations for Inbound Deliveries .

## Transportation Management

In the EWM integration profile, you have defined the specific settings for STO processes.

You have defined whether the system automatically sends additional unloading instructions in stock transport

order (STO) processes, for example, on truck departure. This means that the shipping warehouse does not have to

send the unloading instructions manually.

Furthermore, you have defined whether you want to send partial unloading instructions for multi-pickup, multi-drop

scenarios. The sending of partial unloading instructions is relevant for multi-pickup scenarios when STOs are

delivered from different warehouses to a single receiving warehouse. The unloading instruction is then sent to the

receiving warehouse, although the pickup from all sending warehouses is not complete yet.

For more information, see Customizing for Transportation Management under

Integration

  Integration with

Extended Warehouse Management

  Define EWM Integration Profile .

In the logistics integration profile that you use for the stock transport order process, you have configured the

improved location determination. To do this, select the Improved Location Determination checkbox in the Order-

Related Settings section of the logistics integration profile.

For more information, see Customizing for Transportation Management under

Integration

  Logistics

## Integration

## Internal TM Component Integration

  Define Logistics Integration Profile for SD, MM, and LE .

If you want to use early updates from EWM, make sure you have configured the system as described in the

prerequisite section in Early Updates from EWM.

## Extended Warehouse Management: Handling Unit (HU) Number Ranges

For STO processes, the HU number ranges of the issuing and the receiving EWM warehouses must not have any overlaps.

Make sure that the HU number ranges are disjunct.

For more information, see Customizing for SCM Extended Warehouse Management under  Extended Warehouse

## Management

  Cross-Process Settings

## Handling Units

  External Identification

  Define Number Range for HU

Identification .

This is custom documentation. For more information, please visit SAP Help Portal.

93


1/14/26, 2:44 PM
Outbound Process (Sending Warehouse)

This sample process for the integration based on EWM transportation units describes a high-level STO process with its combined

inbound and outbound processes.

For more information about the outbound process, see Example Process: Delivery- and Order-Based Planning (Outbound).

## Preparation in Materials Management

For an order-based STO process, create a purchase order (PO) with PO type Stock Transport Order. Freight units are created

automatically and assigned to the STO.

## Transportation Management

1. Plan your transportation activities by creating a road freight order based on the freight units created in the previous step.

2. Create an outbound delivery for the freight order.

The system automatically creates an outbound delivery in Delivery Management (LE-SHP) that triggers the creation of an

outbound delivery in EWM, that is, in the sending warehouse.

3. When you have finished planning your transportation activities, you set the load plan status of the freight order on stop

level to Finalized.

The system automatically sends a loading instruction to EWM with a LoadingAppointmentRequest message.

## Extended Warehouse Management

When the LoadingAppointmentRequest message is received from TM, EWM automatically creates an outbound

transportation unit.

1. The standard EWM activities (such as truck arrival, picking, packing, and loading) take place in EWM, that is, in the sending

warehouse.

2. The warehouse worker posts goods issue for the truck. The LE outbound delivery is automatically updated.

In the STO process, posting goods issue initiates the creation of an LE inbound delivery for the STO. The LE inbound

delivery is then replicated to the receiving warehouse.

3. The warehouse worker posts the departure of the truck. EWM sends the LoadingAppointmentNotification message to TM.

## Transportation Management

1. When TM receives this message, it updates the item hierarchy of the freight order with the EWM transportation unit data

and updates the associated freight units. The freight units are then reassigned from the LE outbound delivery to the LE

inbound delivery. The status of the freight order is set to Departed for the stop of the sending location.

2. Sending unloading instructions to the receiving warehouse

Now the combined inbound process continues for the STO: Once the freight order has been posted Departed, TM can

assume that the LE inbound delivery is available for the STO items that are loaded on the truck and informs the receiving

warehouse.

This means: A LoadingAppointmentRequest message with unloading instructions is sent to the receiving warehouse,

and an inbound transportation unit is created in the receiving EWM-managed warehouse.

If you configure the Automatic Sending of Unloading Instructions on Departure in STO Customizing, the system

automatically sets the Unload Plan (Stop) status to Finalized when departure is posted in EWM, and then automatically

This is custom documentation. For more information, please visit SAP Help Portal.

94


1/14/26, 2:44 PM

sends unloading instructions to EWM. In a multi-pickup scenario, the Unload Plan (Stop) status for the receiving EWM-

managed warehouse will be set to Finalized only when the last departure of all sending EWM-managed warehouses is

posted.

If you don’t configure the Automatic Sending of Unloading Instructions on Departure, you need to set the Unload Plan

(Stop) status manually to Finalized.

Inbound Process (Receiving Warehouse)

For more information about the inbound process, see Example Process: Delivery- and Order-Based Planning (Inbound).

## Execution in EWM

1. In EWM, you can carry out the steps that are relevant for the warehouse, such as truck arrival, unloading, posting goods

receipt, and truck departure.

2. When goods receipt is posted, the LE inbound delivery is updated automatically.

3. When the departure of the truck is posted, EWM sends the LoadingAppointmentNotification message to TM.

## Update in TM

1. When the LoadingAppointmentNotification message is received, TM updates the freight order.

  Note

In the inbound scenario, EWM does not send information on cargo back to the freight order in TM when the truck

departure is posted in EWM. Therefore the item hierarchy is not changed in the freight order, even if the items were not

all received in EWM.

In the STO process, you cannot activate the sending of LoadingAppointmentNotification messages with item

details, as described in SAP note 2355948

.

2. You complete freight order execution.

## Related Information

## Integration of Stock Transport Orders

## Unified Package Building in Integration Based on EWM TUs

The integration of Transportation Management (TM) and Extended Warehouse Management (EWM) is based on the EWM

transportation unit (TU) and supports unified package building during freight unit building and unified package building based on

capacity documents.

## Use

You can have the system create packages as follows:

## When freight units are created

This type of unified package building takes place early in the process when the system creates freight units based on order

documents (for example sales orders).

## Based on capacity documents

This is custom documentation. For more information, please visit SAP Help Portal.

95


1/14/26, 2:44 PM

This type of unified package building takes place late in the process when capacity documents exist already.

The process steps are optional. In EWM, information about packages is represented by a handling unit (HU).

## Prerequisites

For more information about prerequisites for unified package building, see Unified Package Building in TM.

If you want to use planned shipping handling units (PSHUs), make sure the delivery item has a process profile for

cartonization planning in which the Create Planned Shipping HUs for Outbound Delivery Orders checkbox is selected.

For more information, see Customizing for Extended Warehouse Management under  Goods Issue Process

## Cartonization Planning

 Define Process Profiles for Cartonization Planning .

For more information about PSHUs in EWM, see Planned Shipping Handling Unit.

## Features

## Unified Package Building During Freight Unit Building

Saving a sales order initiates the unified package building process during freight unit building. The system creates a complete

hierarchy of package and product items that is displayed in the items list of a freight unit. Alternatively, you can configure the

system to initiate unified package building once a delivery, created to a sales order in SD or LE, is saved. For more information

about the integration options between TM and logistics, see Logistics Integration Profile for SD, MM, and LE.

## Unified Package Building Based on Capacity Documents

If you select Build Packages in a capacity document or in the transportation cockpit, the system creates a complete hierarchy of

package and product items that exist only locally in the document.

## Send Loading or Unloading Instruction to EWM

With the LoadingAppointmentRequest the system automatically sends a loading or unloading instruction to EWM when planning

in TM is finished. The system creates PSHUs in EWM based on the sent information about package items. The PSHUs are created

during cartonization planning.

PSHUs offer a packing suggestion from TM. They can be used as templates to create shipping HUs during picking or packing.

Warehouse workers can either pick and pack as suggested, modify or reject the suggestion (and pick and pack differently). The

changes will be updated accordingly in TM.

For more information about an example process, see Example Process: Delivery- and Order-Based Planning (Outbound).

## Cross-Delivery Handling Units

The integration of Transportation Management (TM) with Extended Warehouse Management (EWM) based on Extended

Warehouse Management transportation units (TUs) supports cross-delivery handling units (HUs) for outbound processes. The

feature is relevant for shipper scenarios.

## Use

You can cross-pack and fill up handling units like cartons or pallets with freight units resulting from two or more deliveries. This

helps to improve packing and saves volume if a package or pallet has less than a full load from only one delivery. Single-stage

freight units are supported.

This is custom documentation. For more information, please visit SAP Help Portal.

96


1/14/26, 2:44 PM

TM-driven scenario: In a freight order you can build packages for product-items from different deliveries in the same package and

process them in EWM in the corresponding EWM-TU. The EWM-TU has then a cross-delivery HU as suggested packing instruction.

EWM-driven scenario: In EWM you can cross-pack packages or product-items resulting from different deliveries in the same

package. As usual, the system transfers the actual item data to TM to update the corresponding freight order.

The system uses local packages in the freight order to store the freight units with their document references to the different

deliveries. The cross-delivery package is kept local in the freight order, thus the cross-delivery related package is not referenced

into the freight unit.

In the EWM transportation unit you can identify HUs that are cross-delivery HUs.

## Related Information

Example Process: Delivery- and Order-Based Planning (Outbound)

Execution-Driven Planning (Outbound)

## Quantity Deviation

With the integration of Transportation Management (TM) and Extended Warehouse Management (EWM) you can manage

situations where you need to deliver more or fewer products than the planned quantity.

## Prerequisites

For more information, see Prerequisites for Integration Based on EWM TUs.

## Use

When goods are loaded in EWM, warehouse workers may be able to load only a fraction of the planned quantity onto the truck.

Sometimes less than the planned quantity of a product is available in stock. Another reason may be that the truck is different to

the one planned and has a lower capacity. In both cases the quantity deviates from the planned quantity.

Quantity deviation in the TM-EWM integration:

## You Deliver Remaining Amount Later

You want to deliver the available products now and plan to deliver the remaining products at a later point in time. This

generates a delivery split in Logistics Execution (LE), a freight unit split, and also impacts the freight order in TM. For more

information, see Delivery Split.

For more information about delivery splits in EWM, see Delivery Split for Outbound Deliveries.

## You do not Deliver Remaining Amount Later

You want to deliver the available products now and for whatever reason do not plan to deliver the rest at a later point in

time. In that case, the product amounts can be adjusted in EWM, indicating that the missing products will not be delivered

in the future. The related delivery will be adjusted accordingly.

## Delivery Split

The integration of Transportation Management (TM) with Extended Warehouse Management (EWM) supports delivery splits.

This is custom documentation. For more information, please visit SAP Help Portal.

97


1/14/26, 2:44 PM
## Use

When goods are loaded in EWM, warehouse workers may only be able to load a fraction of the planned quantity on to the truck.

The quantity deviates from the planned quantity.

You want to deliver the available products now and plan to deliver the remaining products to a later point of time. This generates a

delivery split in Logistics Execution (LE), a freight unit split and also impacts the freight order in (TM).

As an example, a freight order with an unpacked product item is sent to EWM. There, the product is loaded, but not all pieces are

available. On posting goods issue, EWM initiates the creation of a new delivery. Both the old and the recently created split delivery

are assigned to the freight order in TM. A freight unit split is executed accordingly and freight units (FUs) are assigned as follows:

The old FU is assigned to the new split delivery.

The new split FU is assigned to the old delivery.

For more information, see Quantity Deviation.

For more information about delivery splits in EWM, see Delivery Split for Outbound Deliveries.

## Prerequisites

For more information, see Prerequisites for Integration Based on EWM TUs.

You have set the entry for subsequent delivery split in customizing:

In customizing choose,

 Logistics Execution

 Shipping

## Deliveries

 Subsequent Delivery Split

. Select a Split Profile and

doubleclick Per Delivery Type to assign a profile to the delivery type.

## Process

A sample process is described below on the basis of a sales order:

## Execution in EWM

1. When loading the truck, warehouse workers can only load some of the overall quantity and have to leave an entire delivery

item.

2. The warehouse workers report the change in quantity and post goods issue. A new delivery in LE (split delivery) is created.

3. The warehouse workers post the departure of the truck. EWM sends the LoadingAppointmentNotification

message to TM. With this message EWM reports the change in quantity or the delivery items that are not included (or

both) to TM.

## Update and Further Steps in TM

1. In TM, the quantity in the freight unit is automatically reduced. If the warehouse workers could not include an item, TM sets

the remaining quantity to zero.

If required, the system also splits the freight unit. This means that the system reduces the quantity in the original freight

unit and creates an additional freight unit with the remaining quantity. You must then reschedule this freight unit. The

system assigns the new freight unit to the old delivery and the old freight unit to the new split delivery.

2. Both the old and the recently created split delivery are assigned to the freight order in TM.

Updates in Sales and Distribution (SD)

This is custom documentation. For more information, please visit SAP Help Portal.

98


1/14/26, 2:44 PM

The sales order is updated and includes links to both freight units and both deliveries.

## Batch Split

The integration of Transportation Management (TM) with Extended Warehouse Management (EWM) supports batch splits.

Batches do not have to come from Logistics Execution (LE) but can instead be determined in EWM.

Warehouse workers load for example the rest of one batch (50 items of a product) on a truck, the other 50 items are loaded

from another batch. This causes a line item split in the system when reported. In TM, the batch information for the product

items is stored in the freight order as subitem of a product item.

A delivery can also be split at the same time as a batch. Warehouse workers load for example 50 items of a product of one

batch on a truck, the other 50 items from the same batch will be delivered at a different point in time. For more information,

see Delivery Split.

It is possible to load one batch per pallet or distributed/split batches per pallet. You can also load distributed batch-managed

product items and non-batch-managed product items on a pallet.

## Prerequisites

For more information, see Prerequisites for Integration Based on EWM TUs.

## Process

A sample process is described below on the basis of a sales order:

1. Create a freight order in TM with items that do not have any batch numbers.

2. Picking of certain batch numbers is possible. You can also enter the batch number in the warehouse task.

3. When the message LoadingAppointmentRqeuest is received from TM, EWM determines automatically whether there

are any batches. If there is more than one batch and these batches need to be split, EWM creates subitems.

4. When EWM reports the data to TM using the message LoadingAppointmentNotification, TM automatically creates

any required subitems in the freight order and in the related freight units. The batch number is then visible on the Content

Identification tab page (details of the cargo item).

## Seals

The integration of Transportation Management (TM) with Extended Warehouse Management (EWM) supports the usage of seals.

You use seals in order to protect vehicle resources and containers from unauthorized access during transportation. Sealing

information can be entered in EWM or in TM.

## Prerequisites

For more information, see Prerequisites for Integration Based on EWM TUs.

## Entering Seals in EWM

This is custom documentation. For more information, please visit SAP Help Portal.

99


1/14/26, 2:44 PM

1. EWM: In the outbound delivery order, open the transportation unit and then enter the sealing information, for example, a

seal number, the partners who seal or unseal, and the date and time for sealing or unsealing. For more convenience, switch

to the Form View.

EWM reports the data automatically to TM using the message LoadingAppointmentNotification when the status

Departure from Checkpoint is set.

2. TM: After processing the message in TM, the item hierarchy and sealing information are updated in the freight order.

## Entering Seals in TM

You can enter sealing information for vehicle resources and containers.

1. TM: Enter the sealing information on the seals tab page of the freight order, for example, a seal number, the partners who

seal or unseal, and the date and time for sealing or unsealing.

TMreports the data automatically to EWM using the message LoadingAppointmentRequest when the status Load Plan

(Stop) Finalized is set.

2. EWM: In the outbound delivery order, open the transportation unit and display or update the sealing information that was

transferred from TM. For more convenience, switch to the Form View.

EWM reports the data automatically to TM using the message LoadingAppointmentNotification when the status

Departure from Checkpoint is set.

3. TM: After processing the message in TM, the item hierarchy and sealing information are updated in the freight order.

Related Information

## Use of Seals

## Transportation Planning with Trailers

The integration of Transportation Management (TM) with Extended Warehouse Management (EWM) supports planning and

execution with trailers.

Data that is received from EWM is confirmed to all affected business documents across several document levels. This means that
in addition to the freight order, the data is also confirmed to one or more trailer units and freight units.

## Prerequisites

In the resource master data you have defined a vehicle resource for your tractor (truck) and a passive vehicle resource for your

trailer.

In customizing for Transportation Management, choose  Master Data

## Resources

  Means of Transport and Compartment

Define Means of Transport

.

For more information, see Prerequisites for Integration Based on EWM TUs.

## Process

A sample process is described below for transportation planning with a trailer based on outbound deliveries.

## Preparation in SD

This is custom documentation. For more information, please visit SAP Help Portal.

100


1/14/26, 2:44 PM

1. You create a sales order in Sales and Distribution (SD).

2. You create outbound deliveries in SD and distribute them to TM and EWM.

With the delivery, freight units are automatically created in TM, in EWM an outbound delivery order is created.

Only relevant for integration with external logistics systems: In TM, a delivery-based transportation requirement

(DTR) is automatically created along with the associated freight units. In EWM, an outbound delivery request and an

outbound delivery order are created automatically. For more information, see External TM System Integration.

## Transportation Planning in TM

1. You plan your transportation activities. When you do so, you create a freight order manually or the system creates one

automatically. Also create a trailer unit and assign a passive vehicle resource (trailer) to it. Then assign the trailer unit to the

freight order.

2. You set the load plan status of the freight order on stop level to Load Plan Finalized. The system automatically sends a

loading instruction to EWM with the message LoadingAppointmentRequest.

## Execution in EWM

1. When the LoadingAppointmentRequest message is received from TM, EWM automatically creates transportation

units. The updated delivery has then two transportation units: one transportation unit representing the truck and one

representing the trailer.

2. Picking is carried out by the warehouse workers. The system can create handling units automatically.

3. When the truck arrives at the yard, the warehouse workers report its arrival and assign a door to it.

4. The warehouse workers load the truck and the trailer. For more information, see Loading and Unloading.

5. The warehouse workers post the goods issue. The outbound delivery is automatically updated in Logistics Execution (LE).

6. The warehouse workers post the departure of the truck. EWM sends the LoadingAppointmentNotification

message to TM.

## Update and Further Steps in TM

1. Only relevant for integration with external logistics systems: When the data is updated in LE, the delivery-based

transportation requirement (DTR) is automatically updated in TM.

2. When the LoadingAppointmentNotification message is received, TM updates the freight order and the

corresponding freight units and sets the execution status to In Execution. The cargo receipt status at item level is

automatically set to Shipped. If the item in question is to be unloaded at the next transportation stop, the handling

execution status is automatically set to Not Unloaded.

3. Complete freight order and trailer unit execution.

More Information

Quantity Deviation

Delivery Split

Batch Split

## Seals

This is custom documentation. For more information, please visit SAP Help Portal.

101


1/14/26, 2:44 PM

## Early Picking

The integration of Transportation Management (TM) with Extended Warehouse Management (EWM) supports early picking of

products.

In this process, picking in EWM starts early - before a freight order is created and TM therefore before a transportation unit is

created in EWM. Without having a transportation unit in the system, warehouse workers already start picking (and possibly

packing) on basis of the delivery. In the early picking process, the delivery in Logistics Execution (LE) and the freight units in TM

are updated right after picking (for example with batch information).

## Prerequisites

For more information, see Prerequisites for Integration Based on EWM TUs.

You have defined that executive steps in EWM can be performed without planning for the outbound delivery.

In Customizing choose,  SCM Extended Warehouse Management

 Extended Warehouse Management

 Goods Issue Process

## Outbound Delivery

## Integration with Transportation

 Allow EWM Execution Without Transportation Planning (Outbound)

.

## Process

A sample process for the early picking process is described below.

## Preparation in SD

1. You create a sales order in Sales and Distribution (SD).

2. You create outbound deliveries in SD and distribute them to TM and EWM.

The system creates an outbound delivery order in EWM and freight units in TM.

## Execution in EWM

1. You open the outbound delivery order.

2. You unblock the delivery and set the status for transportation planning to Fixed Manually.

3. The warehouse workers start early picking (and packing) prior to the transportation unit being created in EWM.

  Note

Note that the delivery in Logistics Execution (LE) and the freight order in TM are not yet updated with the package

information. The delivery in LE is updated when warehouse workers post goods issue for the delivery in EWM. Freight

order and freight units in TM are updated when the departure of the truck is posted in EWM.

## Preparation in TM

1. You create a freight order and assign the freight units.

2. You set the load plan status of the freight order on stop level to Load Plan Finalized. The system sends the data

automatically to EWM using the message LoadingAppointmentRequest.

## Execution in EWM

1. When the message is received from TM, EWM automatically creates transportation units.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

102


1/14/26, 2:44 PM

The freight units and freight order still do not contain the packing information. This information is sent later with the

LDAP notification message from EWM.

2. Warehouse workers pack (if not yet done) and load on the transportation units. For more information, see Loading and

Unloading.

3. After the warehouse workers post the goods issue, the outbound delivery is updated in LE.

4. When the warehouse workers post the departure of the truck, EWM sends the LoadingAppointmentNotification

message to TM.

## Update and Further Steps in TM

1. When the message is received, TM updates the freight order with the corresponding freight units.

2. You complete the freight order execution.

## Multi-Pickup, Multi-Drop

The integration of Transportation Management (TM) with Extended Warehouse Management (EWM) based on EWM

transportation units (TUs) enables you to plan for multiple warehouses on one road freight order. This is also known as a multi-

pickup and multi-drop scenario. It is relevant for inbound and outbound scenarios.

## Prerequisites

In EWM, you have defined a warehouse with a shipping point to enable the multi-pickup and multi-drop scenario for the integration

based on EWM TUs. In TM, the warehouse is represented as a main stop and can be used as the start or end point of a stage in the

freight order.

Shipping points in EWM can be defined for Advanced Shipping and Receiving and for the integration based on EWM TUs. This topic

describes the multi-pick, multi-drop scenario in the integration based on EWM TUs. For more information about Advanced

Shipping and Receiving, see Advanced Shipping and Receiving.

Optional: You can combine the use of multiple warehouses in one road freight order with “early updates from EWM”. For more

information about prerequisites, see Early Updates from EWM.

## Features

By using multiple warehouses for picking up or dropping off handling units, you can improve your freight order planning.

You can use the Overview tab in the freight order to update the status values for the multi-pickup and multi-drop scenario. Here

you can mark single main stops, and set the status Load Plan Finalized or Unload Plan Finalized for outbound or inbound

scenarios.

This status initiates the sending of the message LoadingAppointmentRequest (LDAP request) to the relevant warehouses.

This is not restricted to the current main stop. You can also send LDAP requests for all main stops representing warehouses at

once. Nevertheless, the stop sequence that was planned in TM must be kept in order when warehouse activities are executed in the

multiple warehouses.

If you set the main stop status in the freight order on top level, the system still sets the status for the next stop only.

Canceling Freight Orders, Canceling Stops (Stages)

This is custom documentation. For more information, please visit SAP Help Portal.

103


1/14/26, 2:44 PM

You can cancel freight orders or stops in a multi-pick, multi-drop scenario. Canceling might be necessary if a transportation plan

changes in the middle of the process. You can cancel whole freight orders, or one or several stops (stages) of a freight order.

## Canceling Freight Orders or Stops in TM

You can cancel a freight order if it is not yet in execution.

You cannot cancel a freight order if a truck (an EWM transportation unit) has already arrived at the gate of one of the

multiple warehouses, and the handling execution status at the stop level has been changed to Arrived. In some cases, you

can reverse the arrival of the truck, and then cancel the freight order or stop.

You cannot cancel a freight order if the load plan status on stop level was set to Load Plan Finalized or Unload Plan

Finalized, and the loading or unloading instructions have already been sent to EWM. In this case, the system needs to

cancel the EWM-relevant stops first. This is done in the following way: When you choose Cancel Document in the freight

order, the system sends a sequence of cancellation requests for all stops of the freight order to EWM, for one stop after the

other. The system waits for a cancel confirmation from EWM before the next cancellation request is sent to EWM. EWM will

not confirm a cancellation if arrival has already been posted.

The freight order is still in process until the cancellations for all stops have been sent and confirmed. When the cancellation

is confirmed for all stops, the system sets the Life Cycle Status of the freight order to Canceled.

You cannot reverse the canceling of a freight order document or stop.

Canceling Transportation Units in EWM (Canceling Single Stops in TM)

It happens that a freight unit is not shipped with the planned freight order, but will be planned to another freight order, for

example, if a driver does not pick up any material at one customer stop and drives directly to the next stop. In such a case,

EWM cancels the single transportation unit, which triggers the cancellation of the corresponding stop in TM and an update

of the stage list. In addition, the system unassigns the corresponding FUs. If the last existing stop in TM is canceled, the

system will cancel the whole freight order.

## Combinations and Features

Various features are available for the multi-pick, multi-drop scenario, such as:

For shipper scenarios, you can plan multiple warehouse-related main stops in one road freight order.

The TU-based integration only supports main stops. Sub-stops are not supported.

You can plan inbound- and outbound deliveries in one freight order when they are planned for different main stops or

shipping points.

At a warehouse, you can either load or unload items.

Scenario Examples:

Multi-pickup and single drop (outbound): You can pick up handling units at multiple warehouses, for example pick

up some handling units at warehouse A, pick up more handling units at warehouse B, and deliver (drop) all items at

one customer’s stop.

Single pickup and multi-drop (inbound): You can pick up handling units at your supplier’s stop, drop handling units

at your TU-managed warehouse A, and drop the rest of the handling units at your TU-managed warehouse B.

You can combine inbound and outbound scenarios in one freight order.

You can combine stops from TU-based integration with IM-managed warehouses in one road freight order. IM-managed

means warehouses managed by Inventory Management and Physical Inventory (MM-IM).

You cannot combine stops from TU-based integration with stops related to Advanced Shipping and Receiving.

This is custom documentation. For more information, please visit SAP Help Portal.

104


1/14/26, 2:44 PM

Multi-pickup, multi-drop is not supported for logistics service providers (LSP), Transit Warehousing, and Stock Room

Management (STRM).

For information about the supported functions and the restrictions, see SAP Note 3158252

.

## Example Process

Proceed as follows, to enable a multi-pickup and multi-drop scenario for the TU-based integration.

For more information about the overall process, see:

Example Process: Delivery- and Order-Based Planning (Outbound)

Example Process: Delivery- and Order-Based Planning (Inbound)

Transportation Planning in TM

1. You create a freight order (FO).

You create a road freight order with a FO type for an inbound or outbound scenario. Enter a carrier.

2. You assign freight units (FUs).

To assign FUs to the freight order, choose deliveries for different warehouses with TU-based shipping points. As a result, the

system creates two or more stages. You can display them on the Overview tab.

3. You reschedule the freight order.

After inserting deliveries or freight units for different warehouses to a freight order, you need to reschedule the stage data

manually. Choose Backward Scheduling or Forward Scheduling. Save your freight order.

4. You finalize the load plan.

You set the load plan status of the freight order on stop level to Load Plan Finalized or Unload Plan Finalized.

Set the status for the next stop only:

If you set the stop status on top level in the freight order, the system sets the status for the next stop only.

Set the status for one or several stops at once:

If you mark one or several main stops, and set the status on the Overview tab, the system sets the status for the

selected stops (no matter which stop is next in sequence). This allows the warehouse workers to already start with

picking and packing in any of the warehouses.

After you set the status on stop level to Load Plan Finalized or Unload Plan Finalized, the system automatically sends a

loading instruction to EWM with the message LoadingAppointmentRequest.

## Execution in EWM

When the message is received from TM, EWM automatically creates a transportation unit, one TU for each stage.

1. Perform EWM tasks including truck departure as usual. With the departure of the truck, EWM sends the

LoadingAppointmentNotification message to TM.

The handling execution status of the stop in the freight orders is adjusted accordingly.

2. Check whether all messages to TM were sent correctly:

Display the PPF actions to check if you need to trigger the resending manually.

This is custom documentation. For more information, please visit SAP Help Portal.

105


1/14/26, 2:44 PM

Enable the Update Check for Deliveries. The check verifies that content-related messages are not processed before

the delivery has been updated. For more information, see Reprocessing of Failed Loading Appointment (LDAP)

Messages.

## Update and Further Steps in TM

1. When the LoadingAppointmentNotification message is received, TM updates the item hierarchy of the freight

order with the EWM transportation unit data and updates the associated freight units.

2. You complete freight order execution.

## Related Information

Automatic Status Updates (Multi-Pickup and Multi-Drop Scenario)

Execution-Driven Planning (Outbound)

The integration of Transportation Management (TM) with Extended Warehouse Management (EWM) supports execution-driven

processes.

In an execution-driven process, an empty freight order is sent from TM to EWM. The transportation unit (TU) created in EWM

contains no predefined items and the warehouse execution is done without a planning suggestion from TM. The warehouse

workers pick, pack, and load the products on the empty transportation unit. The transportation units are assigned to the freight

order when it is finally updated after the process is completed.

## Prerequisites

For more information, see Prerequisites for Integration Based on EWM TUs.

You have created an EWM Integration Profile where Send (Un)Loading Instructions Only Once is defined as Delta

Handling Setting.

You have created a freight order type with the integration profile created above assigned to it.

In Customizing for Transportation Management, choose  Freight Order Management

 Freight Order

 Define Freight

Order Types .

You have defined that processing the outbound delivery in EWM can be performed without planning in TM. This means that

you allow the outbound delivery in EWM to be processed before the status Load Plan Finalized on stop level is set in the

freight order (even before a freight order in TM and a transportation unit in EWM is created).

In Customizing for SCM Extended Warehouse Management, choose  Extended Warehouse Management

 Goods Issue

## Process

## Outbound Delivery

 Integration with Transportation

 Allow EWM Execution Without Transportation

Planning (Outbound)

.

In customizing for Transportation Management, choose

## Integration

 Integration with Extended Warehouse Management

Define EWM Integration Profile .

## Process

A sample process is described below based on an outbound delivery created as successor document of a sales order.

## Preparation in SD

This is custom documentation. For more information, please visit SAP Help Portal.

106


1/14/26, 2:44 PM

1. You create a sales order in Sales and Distribution (SD).

2. You create outbound deliveries in SD and send them to TM and EWM.

In EWM, an outbound delivery order is created. In TM, freight units are created automatically. The freight units are not yet

assigned to a freight order.

## Preparation in TM

1. You create a freight order and enter at least a source location (shipping point), destination location and a delivery date.

You set the load plan status of the freight order on stop level to Load Plan Finalized. The system automatically sends the

empty freight order to EWM with the message LoadingAppointmentRequest. For your convenience, you can create a

stock of such empty freight orders.

2. After sending the message, the freight order is blocked for editing (see prerequisites).

## Execution in EWM

1. When the message is received from TM, EWM automatically creates an empty transportation unit. The system chooses the

relevant EWM warehouse based on the information in the shipping point.

2. The warehouse workers use this empty transportation unit, search manually for the delivery, and assign it to the empty

transportation unit.

3. Picking, packing, and loading are done as usual. For more information, see Loading and Unloading.

In addition, you can enable updates from EWM to TM with status Loading Finished. For more information, see Early

Updates from EWM.

4. The warehouse workers post the goods issue. The outbound delivery is automatically updated in Logistics Execution (LE).

5. The warehouse workers post the departure of the truck. EWM sends the LoadingAppointmentNotification

message to TM.

## Update and Further Steps in TM

1. When the message is received, TM updates the freight order with the corresponding freight units. The freight order item

hierarchy then includes packages and product items from the delivery items that have been packaged in EWM.

2. You complete the freight order execution.

More Information

Quantity Deviation

Delivery Split

Batch Split

## Seals

## Reversal of Departure

The integration of Transportation Management (TM) with Extended Warehouse Management (EWM) supports the reversal of the

status Departed from Checkpoint in EWM.

This is custom documentation. For more information, please visit SAP Help Portal.

107


1/14/26, 2:44 PM

Reversal of the departure and the sending of a second departure message from EWM to TM is available for inbound and for

outbound processes. For information about the supported functions and the restrictions, see SAP Note 3018355

.

## Prerequisites

You have activated reversal of the departure in the Customizing for Extended Warehouse Management under  SCM Extended

Warehouse Management

  Extended Warehouse Management

  Interfaces

  TM Integration

  Make Settings for TM

Message Processing .

## Features

In an outbound process, it is sometimes necessary to reverse the departure of a truck from the checkpoint.

## Example 1: Departure Was Set Too Early

Reversing the departure is necessary when, for example, a departure was set for the wrong truck, or the departure was

unintentionally posted too early although the truck has not yet left the location.

In such cases, a warehouse clerk can reverse the departure in EWM, and the system sends an update message for the

freight order to TM. In TM, the current departure event is deleted, and the handling execution status is set back to Loaded.

Everything in the freight order is reverted to the state it had after Finished Loading.

Later, when the second, actual departure event is posted in EWM, the system again sends an update message to TM. In TM,

a new departure event with the new date is created, and the handling execution status is set back to Departed.

If the truck has not yet arrived at the next stop, the reversal of the departure can be used to update the departure time. If the truck

has already arrived at the next stop, the reversal of the departure is mainly used to initiate a correction of the truck load.

## Example 2: Transportation Unit or Delivery Needs to be Corrected

Reversing the departure is also necessary when, for example, pallets were loaded or not loaded but were already reported to the

system, or when a truck load is too heavy and the load needs to be adjusted. The reversal of the departure is a prerequisite for the

changes to a transportation unit or delivery.

When you reverse the departure of the truck, you can correct the data, for example, add or remove deliveries or handling units, or

decrease or increase product quantities.

In the case of a multi-pickup scenario from EWM-managed warehouses, reversal of the departure is only possible if the arrival at

the next EWM-managed warehouse was not reported yet. If the arrival has already been reported, you must reverse the arrival

before you can reverse the departure.

The freight order execution information is used to determine which changes that were made in EWM are reflected in TM. This

means which events and statuses are to be updated in the freight order.

Updates to deliveries, handling units, or product quantities are always reflected in TM.

Note the following:

## Truck has already arrived at the next stop

The system will not update the freight order with any event or status changes for the first stop as it is not relevant anymore.

For example, it does not make sense to correct the truck departure when the truck has already arrived at the next stop.

Event dates for Loading Complete and Departure remain the same as when they were posted for the first time.

This is custom documentation. For more information, please visit SAP Help Portal.

108


1/14/26, 2:44 PM

The handling execution status is not changed.

## Truck has not yet arrived at the next stop

If no arrival at the next stop is posted, the event dates and the handling execution status are updated when the departure

reversal message and update messages (like the reversal of the loading end or reversal of goods issue) are received from

EWM.

For newly added items, the handling execution status is set to Loaded.

A new departure event with the new date is created, and the handling execution status is set back to Departed.

If the unloading of the receiving stop is reported already, the assumption is that the new items are also unloaded

and get the same status.

Transit Warehousing

## Use

Transit warehousing enables you to seamlessly integrate the planned flow of goods in Transportation Management (TM) and the

physical flow of goods in Extended Warehouse Management (EWM) over the entire transportation chain. The integration is based

on execution documents resulting from forwarding orders.

With this process you can store cargo temporarily in transit warehouses or gateways (air freight) or in container freight stations

(ocean freight) until it is transported. You can also organize cargo over the entire transportation chain and get transparency over

warehouse-specific data. The process of handling cargo at a location can be repeated for several locations.

In EWM, the warehouse-specific processes are based on business documents that are sent from TM using a loading or unloading

instruction. You can also configure the warehouse layout according to the requirements of the transit warehousing process. For

example, specific storage types are available and a product master is no longer necessary. The handling of cargo is based on

package level and not on product level.

For more information about the processes in EWM, see SAP Help Portal:

For EWM, see https://help.sap.com/s4hana under  Product Assistance

 Enterprise Business Applications

 Supply

## Chain

 Extended Warehouse Management

 Transit Warehousing .

For SAP EWM, see http://help.sap.com/ewm  under  Application Help

 SAP Extended Warehouse Management (SAP

EWM)

 Transit Warehousing .

## Prerequisites

You have defined your transportation network. You have also defined a logical system (EWM system) and a warehouse

number for the locations whose warehouses you manage using EWM. You have sent this data to EWM using report

/SCMTMS/BUPA_SEND_TRANS_WH.

You have defined an EWM integration profile and assigned it to your document types (that is, to your freight order types

and freight booking types). Among other things, you can specify in the EWM integration profile whether loading and

unloading instructions are to be sent manually or automatically and whether they can be sent once or multiple times.

Moreover, you have to specify in this profile that item changes are propagated by the system. This means that you can still

change the forwarding order until the goods have physically arrived in the warehouse and the actual quantities and

attributes have been reported by EWM. The changes are propagated to the freight order.

For more information, see Customizing for Transportation Management under:

This is custom documentation. For more information, please visit SAP Help Portal.

109


1/14/26, 2:44 PM

## Integration

 Integration with Extended Warehouse Management

 Define EWM Integration Profile

Freight Order Management

## Freight Order

 Define Freight Order Types

Freight Order Management

## Freight Booking

## Define Freight Booking Types

You have defined a discrepancy profile and assigned it to your document types (that is, to your freight order types and

freight booking types). For more information, see Customizing for Transportation Management under:

Freight Order Management

 Define Discrepancy Profile

Freight Order Management

## Freight Order

 Define Freight Order Types

Freight Order Management

## Freight Booking

## Define Freight Booking Types

You have made the following additional settings in your document types (that is, in your freight order types and freight

booking types):

You have selected the Transportation Activity Creation in EWM option in the Document Creation Relevance field.

This setting is optional if in the EWM integration profile in the Send. (Un)Load. Instr. field ("Sending of

(Un)Loading Instructions") you have selected the option Manual Sending of (Un)Loading Instructions or

Automatic and Manual Sending of (Un)Loading Instructions.

This setting is required if in the EWM integration profile in the Send. (Un)Load. Instr. field ("Sending of

(Un)Loading Instructions") you have selected the option Automatic Sending of (Un)Loading Instructions.

You have specified an output profile that contains actions for sending loading/appointment messages, for example,

/SCMTMS/TOR.

If you are working with freight orders for customer self-delivery and pick-up, you have configured the following

settings in your freight order type:

In the Freight Order Can Be Subcontracted field, you have selected the option Not Relevant for

Subcontracting.

In the Shipper/Consignee Determination Rule field, you have selected the option Shipper/Consignee Not

Relevant.

For freight orders for customer self-delivery, you have selected the option Star-Shaped Based on FU Stages

(Reversed) in the Sequence Type of Stops field. For freight orders for customer pick-up, you have selected

the option Star-Shaped Based on FU Stages.

In the Self-Delivery/Customer Pick-Up field, you have selected the option Freight Order for Customer Self-

Delivery or Pick-Up.

In the Web Dynpro Application Config. field, you have entered the application configuration

/SCMTMS/FRE_ORDER_SDCP.

The SAP standard system provides the freight order types 4010 for customer self-delivery and 5010 for

customer pick-up in the transit warehousing process.

For more information, see Customizing for Transportation Management under:

Freight Order Management

## Freight Order

 Define Freight Order Types

Freight Order Management

## Freight Booking

## Define Freight Booking Types

SAP provides the following, predefined event codes for cancelations as well as the corresponding event reason codes:

This is custom documentation. For more information, please visit SAP Help Portal.

110


1/14/26, 2:44 PM

Event Code

## Description

Event Reason Code

Description

## CANCEL_EXEC_DOC

Cancel Execution Document

CANCELLED_BY_CARRIER

Canceled by Carrier

CANCEL_STATUS_RESET

Cancel and Reset Cargo

TM_PLAN_NOT_READY

TM Planning Not Yet Ready

Execution Status

CANCEL_UNASSIGN_FUS

Cancel and Unassign FUs of

STOP_CANCELLED

Loading Appointment

Current Stop (cancel and

unassign the freight units for

the current stop)

Canceled (loading cannot be

executed in the warehouse as

planned)

These event codes are set as the default codes.

You can define your own event codes and event reason codes. For each event type, you must specify at least one of your

event codes as the default code.

For more information, see Customizing for Transportation Management under  Basic Functions

## General Settings

 Define Event Reason Codes .

## Features

The following processes are supported:

Transit Warehousing Process (see Transit Warehousing Process)

Planning with trailers (see Planning with Trailers)

## Handling Discrepancies

Discrepancies and exceptions may occur during the transit warehousing process. For more information, see Handling

Discrepancies in Transit Warehousing Process.

## Handling Unexpected Package Items

If the confirmation from EWM contains unexpected package items and you have configured your TM system in such a way that no

discrepancies are to be created, TM automatically reassigns these package items. For more information, see Automatic

Reassignment of Package Items.

## Splitting Package Items for Distribution to Several Transportation Units

When goods are being transported between transit warehouses or to a gateway they may have to be redistributed to other

transportation units, such as trailers. You can do this by splitting the package item of a freight order that has already been

assigned to a transportation unit and assigning it to several transportation units. You can also drag and drop package items

between transportation units.

Once EWM has posted the goods as received, the system updates automatically the item hierarchy in the freight order with

information about the handling units from EWM. Note, however, that this splitting function is integrated with EWM only for trailer

units.

For more information, see Cargo Management.

## Message Exchange with EWM

This is custom documentation. For more information, please visit SAP Help Portal.

111


1/14/26, 2:44 PM

Loading and unloading instructions are sent automatically from the freight document. This is triggered by a status change (see

Transit Warehousing Process). You can also trigger the sending of these instructions manually and multiple times provided you

have made the required settings in your EWM integration profile (see Prerequisites). You can also cancel a sent loading or

unloading instruction.

You can receive multiple updates in TM from EWM and update the freight documents and transportation units to which the

message from EWM refers.

Transmission-to-EWM Status provides information about the status of the exchange of messages. You can get an overview of all

the status values relevant for the transit warehousing process, such as load or unload plan status, load or unload plan item status,

handling execution status, and cargo execution status, in the freight document item table in the Status Management hierarchy

view. For more information, see Explanation of Statuses of Business Documents.

  Note

You can send a loading or unloading instruction for a future stop (for example, a transit warehouse) even if execution of

the transportation has not finished at the present stop. If you set the load or unload plan status at header level of the

freight order to Finalized, the system searches for the next relevant stop, sets the status for this stop, and automatically

sends a message to EWM. If you set the status at stop level, the system automatically sends a message to EWM for this

stop.

The location master data determines which stops are relevant for loading or unloading. You can use the BAdI

Determination of Warehouse Relevance to change this standard logic and add locations, for example. For more

information, see Customizing for Transportation Management under  Business Add-Ins (BAdIs) for Transportation

## Management

 Freight Order Management

 Freight Order Management

 BAdI: Determination of Warehouse

Relevance .

You can also send and cancel loading and unloading instructions for transportation units if these transportation units

are included in a freight document.

## Canceling Freight Documents

In the transit warehousing process, you can still cancel freight orders and freight bookings up until the goods have arrived in the

warehouse and have been reported by EWM as Arrived. If the status Unload Plan Finalized has already been set and you cancel

the freight document, the system sends a cancellation request to EWM. This request is checked and processed by the EWM

system as follows:

If the goods have not yet arrived in the warehouse, EWM confirms the cancellation, and the life cycle status of the freight

document is changed to Canceled.

If the handling execution status at stop level has already been changed to Arrived, the system sets the Transmission-to-

EWM Status to Partially Received or Received. Execution of the transportation continues and the freight document cannot

be canceled.

The freight document in TM can be canceled only if cancellation has been confirmed by EWM and reported to TM.

## Document Flow

In TM you can navigate directly to the associated EWM documents from your freight documents. For example, you can jump

directly to the associated EWM freight order from a freight order. However, note that the system does not support the navigation

from these EWM documents to other EWM transactions.

## Transit Warehousing Process

This is custom documentation. For more information, please visit SAP Help Portal.

112


1/14/26, 2:44 PM
## Use

First, you perform transportation planning in Transportation Management (TM) and then you send your freight documents and the

associated transportation units to Extended Warehouse Management (EWM). In EWM, you can then carry out the steps relating to

the warehouse (loading or unloading, for example). You can bring the cargo to a staging area in transit warehouses or gateways (air

freight) or in container freight stations (ocean freight) where it is stored temporarily until it is transported. Because the two

systems are integrated with one another, TM informs you whether the truck or the trailer in EWM has already been loaded or

unloaded, for example, and whether there are any discrepancies such as quantity discrepancies.

## Prerequisites

For more information, see Transit Warehousing.

## Process

A sample process for air freight is described below. For the sake of simplicity, it is assumed that each freight order does not have

transportation units, in other words this is a truck without trailer. Only the export side is described. The import side runs in the

same way. However, during the import process you send the freight booking first to EWM, even though the freight order for pick-up

has to be processed by EWM first.

This process is also supported in the same way for ocean freight.

## Creation of Order Documents in TM

1. The customer service agent creates a forwarding order in TM.

  Note

If the customer delivers the goods themselves, you have the following options for this process step:

## Expected customer self-delivery

In this case, you know that the customer is delivering the goods themselves. Therefore, the customer service

agent creates a forwarding order for customer self-delivery. From this forwarding order, the transportation

planner creates a freight order for customer self-delivery.

## Unexpected customer self-delivery

In this case, the customer is delivering the goods themselves without your knowledge. Therefore, you create the

freight order for customer self-delivery directly in TM and send it to EWM.

For more information, see Handling Discrepancies in Transit Warehousing Process (the last section under "Unexpected

Cargo").

For more information about freight orders for customer self-delivery, see Freight Orders for Customer Self-Delivery and

Pick-Up.

2. The transportation planner creates an actual route manually or has the system determine this route. The actual route

contains one or more locations that are relevant for transit warehousing. A location is relevant for transit warehousing if you

have entered a warehouse number and a logical system (EWM system) in the location mater data.

3. From the forwarding order, the transportation planner creates a freight order for picking up the goods at the shipper and

transporting them to the transit warehouse.

4. The transportation planner sets the execution status of the freight order to Ready for Transportation Execution, which

means that the transportation activities can now start.

This is custom documentation. For more information, please visit SAP Help Portal.

113


1/14/26, 2:44 PM

5. The transportation planner sets the unload plan status of the freight order for the transit warehouse to Unload Plan

Finalized. The system automatically sends an unloading instruction to EWM with the message

LoadingAppointmentRequest.

If you have specified in the Customizing settings for the EWM integration profile that changes are propagated to the follow-

up document and that loading and unloading instructions can be sent multiple times, you can continue to make changes to

the forwarding order. The changes are then copied automatically to the freight order. When you set the unload plan status

back to Unload Plan Finalized, the system sends another unloading instruction to EWM. Once the cargo receipt status has

been set to On Hand, the system no longer copies any changes made to the forwarding order to the freight order and the

freight units.

  Note

You can set the unload plan status for the freight order either at header level or at stop level. If you set the status at

header level, the system automatically searches for the next relevant stop, sets the status for this stop, and sends an

unloading instruction to EWM. It does this regardless of the extent to which execution has progressed at the present

stop and regardless of the value of the handling execution status.

Unloading in the Transit Warehouse (EWM)

1. When the LoadingAppointmentRequest message is received from TM, EWM automatically creates a transportation

unit and the related handling units, as well as an inbound delivery.

2. When the truck arrives at the yard, the warehouse workers report its arrival and assign a door to it. EWM sends the

LoadingAppointmentNotification message to TM. When the message is received, TM updates the freight order

automatically with information about the successful arrival.

3. The warehouse workers unload the truck and post the goods receipt. For more information about possible discrepancies

and how to handle them, see Handling Discrepancies in Transit Warehousing Process.

If the warehouse workers have received the cargo in its entirety and without discrepancies, EWM sends the

LoadingAppointmentNotification message to TM. When the message is received, TM updates the freight order and

the freight units automatically with information about the received cargo.

4. The warehouse workers post the departure of the truck. EWM sends the LoadingAppointmentNotification

message to TM. When the message is received, TM updates the freight order automatically with information about the

successful departure.

5. The warehouse workers bring the cargo to the putaway bin in the transit warehouse or to the staging area that is provided

for further transportation of the cargo.

## Planning the Pre-Carriage in TM

1. From the forwarding order, the transportation planner creates a freight order for the transportation of goods from the

transit warehouse to the gateway.

2. The transportation planner sets the execution status of the freight order to Ready for Transportation Execution, which

means that the transportation activities can now start.

3. The transportation planner sets the load plan status of the freight order for the transit warehouse to Load Plan Finalized.

The system automatically sends a loading instruction to EWM with the message LoadingAppointmentRequest.

Loading in the Transit Warehouse (EWM)

1. When the LoadingAppointmentRequest message is received from TM, EWM automatically creates a transportation

unit and an outbound delivery order and assigns the required handling units to the outbound delivery order.

This is custom documentation. For more information, please visit SAP Help Portal.

114


1/14/26, 2:44 PM

2. When the truck arrives at the yard, the warehouse workers report its arrival and assign a door to it. EWM automatically

specifies in the order that handling units, such as dangerous goods, will be brought into the staging area assigned to the

door. Furthermore, EWM sends the LoadingAppointmentNotification message to TM. When the message is

received, TM updates the freight order automatically.

3. The warehouse workers bring the handling units into the staging area.

4. The warehouse workers load the truck from the staging area and other storage areas. For more information about possible

discrepancies and how to handle them, see Handling Discrepancies in Transit Warehousing Process.

EWM sends the LoadingAppointmentNotification message to TM. When the message is received, TM updates the

freight order and the freight units automatically with information about the loading process.

5. The warehouse workers post the departure of the truck and post the goods issue. EWM sends the

LoadingAppointmentNotification message to TM. When the message is received, TM updates the freight order

automatically.

Preparation for Unloading at the Gateway (TM)

1. While the truck is on its way to the gateway, the transportation planner sets the execution status of the freight order to

Ready for Transportation Execution and the unload plan status of the freight order to Unload Plan Finalized. The system

automatically sends an unloading instruction to EWM with the message LoadingAppointmentRequest.

Unloading at the Gateway (EWM)

1. When the LoadingAppointmentRequest message is received from TM, EWM automatically creates a transportation

unit, planned handling units, and an inbound delivery.

2. When the truck arrives at the yard, the warehouse workers report its arrival and assign a door to it. EWM sends the

LoadingAppointmentNotification message to TM. When the message is received, TM updates the freight order

automatically.

3. The warehouse workers unload the truck and post the goods receipt. For more information about possible discrepancies

and how to handle them, see Handling Discrepancies in Transit Warehousing Process.

EWM sends the LoadingAppointmentNotification message to TM. When the message is received, TM updates the

freight order and the freight units automatically.

4. The warehouse workers post the departure of the truck. EWM sends the LoadingAppointmentNotification

message to TM. When the message is received, TM updates the freight order automatically.

5. The warehouse workers bring the goods into the area in which they will later be consolidated.

## Planning the Main Carriage in TM

1. From the forwarding order, the transportation planner creates an air freight booking.

2. The transportation planner sets the load plan status of the air freight booking to Load Plan Finalized. The system

automatically sends a loading instruction to EWM with the message LoadingAppointmentRequest.

Loading the Unit Load Devices in the Gateway (EWM)

1. When the LoadingAppointmentRequest message is received from TM, EWM automatically creates an outbound

delivery order, planned handling units, and planned handling unit containers. Furthermore, EWM assigns the required

handling units to the outbound delivery order.

2. The warehouse workers bring the handling units and the unit load devices to the outbound staging area.

This is custom documentation. For more information, please visit SAP Help Portal.

115


1/14/26, 2:44 PM

3. The warehouse workers load the handling units into the unit load devices. The system creates handling unit containers.

EWM sends the LoadingAppointmentNotification message to TM. When the message is received, TM updates the

freight booking and the freight units automatically.

  Note

The warehouse workers can distribute partial quantities of items to different unit load devices.

Preparation for the Transportation of Unit Load Devices from the Gateway to the Airport (TM)

1. From the air freight booking, an employee in the shipping office creates a freight order for the pick-up.

2. This employee sets the execution status of the freight order to Ready for Transportation Execution, which means that the

transportation activities can now start.

3. The employee sets the load plan status of the freight order for the gateway to Load Plan Finalized. The system

automatically sends a loading instruction to EWM with the message LoadingAppointmentRequest.

Loading the Truck at the Gateway (EWM)

1. When the LoadingAppointmentRequest message is received from TM, EWM automatically creates a transportation

unit. If handling unit containers have been reported by TM, EWM assigns these to the transportation unit automatically.

2. When the truck arrives at the yard, the shipping office employee reports its arrival and assigns a door to it. EWM sends the

LoadingAppointmentNotification message to TM. When the message is received, TM updates the freight order

automatically.

3. The warehouse workers load the unit load devices onto the truck. EWM sends the

LoadingAppointmentNotification message to TM. When the message is received, TM updates the freight order, the

air freight booking, and the freight units automatically.

4. The warehouse workers post the departure of the truck and post the goods issue. EWM sends the

LoadingAppointmentNotification message to TM. When the message is received, TM updates the freight order

automatically.

Completion of the Export Side (TM)

1. The transportation planner receives the information from the airline that the aircraft has departed and sets the uplift

confirmation status of the air freight booking to Uplift Confirmed.

Planning with Trailers

## Use

The transit warehousing process supports planning and execution with trailers. Data that is received from Extended Warehouse

Management (EWM) is confirmed to all associated business documents across several document levels. This means that in

addition to the freight order, the data is also confirmed to one or more trailer units and freight units.

## Prerequisites

In the resource master data you have defined a resource for your tractor (truck) and a passive vehicle resource for your

trailer.

This is custom documentation. For more information, please visit SAP Help Portal.

116


1/14/26, 2:44 PM

You have made the settings for the transit warehousing process. In particular, you have specified in your EWM integration

profile that related transportation units are to be included when loading or unloading instructions are sent. For more

information, see Transit Warehousing.

The trailer must have been coupled before the warehouse-specific steps are executed.

## Process

A sample process (inbound) for a transportation stop and a trailer is described below. If your freight order comprises several

transportation stops, the process is repeated for each stop if the stop contains unloading locations relevant to EWM. Note,

however, that multiple pickup and multiple delivery scenarios are not supported.

## Transportation Planning in TM

1. The customer service agent creates a forwarding order in Transportation Management (TM) and creates the freight units.

2. The transportation planner creates a trailer unit and assigns the freight units.

3. The transportation planner creates a freight order and assigns the trailer unit.

4. The transportation planner sets the execution status of the freight order to Ready for Transportation Execution, which

means that the transportation activities can now start.

5. The transportation planner sets the handling execution status of the freight order to Departed.

6. The transportation planner sets the cargo execution status of the freight order to Cargo Ready for Unloading. The system

automatically sends an unloading instruction to EWM with the message LoadingAppointmentRequest. This message

includes the assigned trailer unit.

## Execution in EWM

1. When the LoadingAppointmentRequest message is received from TM, EWM automatically creates a transportation

unit and the related handling units.

2. When the truck arrives at the yard, the warehouse workers report its arrival and assign a door to it.

3. The warehouse workers unload the trailer and uncouple it (optional).

4. The warehouse workers post the goods receipt (optional).

5. The warehouse workers post the departure of the truck. EWM sends the LoadingAppointmentNotification

message to TM.

## Update and Further Steps in TM

1. When the LoadingAppointmentNotification message is received TM updates the freight order, the trailer unit, and

the associated freight units.

2. Complete freight order and trailer unit execution.

  Note
If you receive the message from EWM that the trailer was uncoupled, the corresponding item in the freight order and in the

trailer unit is assigned the handling execution status Uncoupled. You can also set these values manually.

## Handling Discrepancies in Transit Warehousing Process

This is custom documentation. For more information, please visit SAP Help Portal.

117


1/14/26, 2:44 PM
## Use

Discrepancies and exceptions may occur during the transit warehousing process in Transportation Management (TM). For

example, during execution in Extended Warehouse Management (EWM) you can determine discrepancies between the actual

quantities and the quantities that have been ordered. Furthermore, exceptions can occur such as missing or damaged cargo. This

data is sent from EWM to TM and copied automatically into the freight order or freight booking.

The customer service agent or transportation planner must decide together with the ordering party how to proceed with the

discrepancies. For example, will missing cargo be delivered at a later date or will the customer stick with the quantity of cargo that

has been delivered? Depending on this decision, the customer service agent can adjust the ordered data entered in the forwarding

order to the actual data or can plan the subsequent delivery of missing cargo.

Examples of discrepancies and exceptions that may occur in the transit warehousing process are described below. This document

also describes how the customer service agent or transportation planner can handle these cases.

## Prerequisites

For more information, see Transit Warehousing and Resolution of Discrepancies. To handle discrepancies you have created a

discrepancy profile in Customizing for Transportation Management with the required discrepancy types and discrepancy

subcategories.

## Features

## Determining Discrepancies

The system enters any discrepancies between the quantities and attributes of the goods that are to be transported and the data

that has been ordered in the freight document and displays this in the forwarding order. The actual quantities compared against

the ordered quantities are displayed in the item details of the forwarding order. These details also show whether an attribute such

as Overdimensional Cargo or Dangerous Goods differs from the order data.

You can also search for specific discrepancies. You can display the discrepancies together with all the relevant data in your

personal object worklist for discrepancies. Furthermore, you can solve discrepancies directly and access the related documents

such as forwarding orders and freight orders.

For more information, see Handling Discrepancies (forwarding order) and Discrepancies and Events (freight order).

Handling and Resolving Discrepancies

## Missing Cargo

If goods are reported as missing by the EWM system and were entered in the freight document in TM, the system sets the cargo

receipt status to Missing Cargo. This status is displayed in the forwarding order and freight document. It is also highlighted in the

forwarding order that the discrepancy Missing Cargo needs to be resolved. You can view details of the discrepancy on the

Discrepancies tab page in the forwarding order and freight document.

If the quantity reported by the EWM system has changed in the meantime, the system adjusts the actual quantity that is displayed.

Once you have finally decided with the ordering party whether to redeliver the goods or not, you have the following options on the

Discrepancies tab page:

## Goods are redelivered

In this case, the missing goods are delivered with the next freight order. Even if not all the goods can be loaded, they can be

scheduled for the next freight order. Proceed as follows:

This is custom documentation. For more information, please visit SAP Help Portal.

118


1/14/26, 2:44 PM

1. On the Discrepancies tab page or in your personal object worklist for discrepancies, choose  Resolve

## Resolve

(Retain Missing Cargo)

 for the forwarding order or freight order item.

2. The system splits the freight unit into a freight unit containing the available quantity and a freight unit containing

the missing quantity. The freight unit containing the missing quantity can be transported with the next freight order,

and the capacity of the means of transport remains reserved.

3. The system resolves the discrepancy and resets the cargo receipt status.

## Goods are not redelivered

In this case, the ordering party accepts that the missing cargo will not be delivered. You can copy the actual quantities to

the forwarding order as the ordered data. Proceed as follows:

1. On the Discrepancies tab page or in your personal object worklist for discrepancies, choose  Resolve

## Resolve

(Delete Missing Cargo)

 for the forwarding order or freight order item.

2. The system adjusts the planned quantity to the actual quantity and resolves the discrepancy.

If all of the goods of a forwarding order item are missing (the quantity is 0) and you resolve the discrepancy for missing cargo, the

system deletes all associated freight units. To ensure that it does not create new freight units for this item when you save the

forwarding order, the system marks them with the processing status S - Statistical Item; No Logistical Relevance. This means

that the item exists only in the forwarding order.

Note that if cargo is missing you can resolve discrepancies only at main item level, and not at subitem level.

## Unexpected Cargo

The discrepancy Unexpected Cargo is displayed on the Discrepancies tab page in the forwarding order or freight document as

well as in your personal object worklist for discrepancies. You can resolve this discrepancy as follows:

If the discrepancy was reported by the EWM system to TM and there is already an item in the forwarding order for the

unexpected cargo, the system creates a cargo item and assigns it to a freight unit. You can resolve this discrepancy by

choosing  Resolve

 Resolve Discrepancy .

Unexpected cargo can also be dangerous goods. Dangerous goods information that was entered first in the EWM system is

marked accordingly on the user interface. You must check and complete this information before you resolve the

discrepancy.

If the unexpected cargo has not been assigned to an item in the forwarding order yet, the system creates a local item in the

freight document. You can resolve this discrepancy by assigning the local cargo item to a freight unit item of an existing

forwarding order. To do so, choose  Forwarding Order

 Assign Forwarding Order Item . On the Discrepancies tab page

or in your personal object worklist for discrepancies, you can also choose  Resolve

 Resolve Unexpected Cargo (Assign

FWO Item)

.

In both cases, a dialog box appears in which you can assign each of your local cargo items to an item of a freight unit. Make

sure, however, that a cargo item is assigned to each item of the freight unit. Otherwise, specific criteria must be met. For

example, the route and the item category of the two items must be identical. The freight unit must also not yet be split.

If the unexpected cargo includes not only a single item but all items, for example an entire truck arrives at the warehouse

unexpectedly, you create a freight order for customer self-delivery in TM and enter the items. You create the forwarding

order from this freight order. You then send the freight order to SAP EWM. The warehouse employees who work with SAP

EWM execute the warehouse-specific steps and send the freight order back to TM. Depending on your settings in the

discrepancy profile, discrepancies for unexpected cargo are created automatically in TM. You have to resolve this

discrepancy as described above.

## Damaged Cargo

This is custom documentation. For more information, please visit SAP Help Portal.

119


1/14/26, 2:44 PM

The discrepancy Damaged Item or Damaged Cargo is displayed in the item details of the forwarding order and freight document

as well as in your personal object worklist for discrepancies. You can resolve this discrepancy as follows:

1. You can split the freight unit manually to create an additional freight unit for the damaged item. You can then assign this

freight unit to another freight document to return the goods or plan a later delivery. You do this on the user interface of the

freight unit by choosing Split/Merge.

If you select Adopt Stops, the system copies the stops from the existing freight unit. The system also copies the planning

results (routing and assignments to freight orders) from the existing freight unit if it has already been planned.

2. You can resolve the discrepancy by choosing  Resolve

 Resolve Discrepancy  on the Discrepancies tab page or in your

personal object worklist for discrepancies.

The damage to cargo can also affect a package subitem that was not created in the forwarding order but was created only in the

EWM system. The TM system enters these cargo items in the freight document after they have been reported by the EWM system.

The corresponding freight units are not assigned to any forwarding order item and are therefore not displayed in the forwarding

order. However, the damage is displayed in the forwarding order as a discrepancy for the overlying package. You can also split the

freight units manually and assign the freight unit for the damaged item to a different freight document.

You can still split freight units manually after you have started executing the transportation (once the cargo receipt status has

been set to On Hand). Note, however, that the forwarding order is no longer adjusted accordingly.

You can also apply the process of manually splitting freight units that is described here to other exceptions in the transit

warehousing process. For example, other cases are possible:

Some of the goods are to be sent to a different consignee.

It is discovered in a transit warehouse that not all the goods can be loaded onto a means of transport and that some of the

goods have to be transported using a different means of transport and freight order.

## Subsequent Corrections in TM Following Message from SAP EWM

You can make manual corrections in TM after you have received a message from SAP EWM. This may be useful in the following

cases:

After a message is sent to TM, the warehouse workers discover that something has been forgotten and forward the

corrections by telephone to the customer service agent or transportation planner in TM.

The delivery of an automatic message from SAP EWM has failed.

You have the following options:

## Delete items

The system automatically creates a discrepancy called Missing Cargo. You have to resolve this discrepancy as described

above.

## Reassign items

You can use drag and drop to reassign items easily.

## Add items

The system automatically creates a discrepancy called Unexpected Cargo. You have to resolve this discrepancy as

described above.

## Discrepancies Between Quantities and Attributes

This is custom documentation. For more information, please visit SAP Help Portal.

120


1/14/26, 2:44 PM

Quantity discrepancies and discrepancies in attributes, such as Overdimensional Cargo or Dangerous Goods, are entered in the

freight document after confirmation from the EWM system. These are then also displayed in the forwarding order. In the details of

the forwarding order items you can see whether the quantities and attributes still correspond to the data originally ordered in the

forwarding order. If this is no longer the case, you can discuss this with your ordering party. If the ordering party accepts the

discrepancies you can proceed as follows:

1. You copy the actual data to the order data. You do this in the item table by choosing  Copy Actual Data

 Copy Quantities

and Attributes .

2. You resolve the discrepancies on the Discrepancies tab page by choosing  Resolve

 Resolve Discrepancy .

In other cases, such as for missing cargo as described above, you first resolve the discrepancy and then you copy the actual data

to the order data. You can also change the order data manually.

Some restrictions apply to the copying or manual changing of some attributes. These include:

## Dangerous goods

Before you can copy the data for dangerous goods you have to define a dangerous goods profile in Customizing for the

forwarding order type and a dangerous goods UI profile in Customizing for the item type. For more information, see

Customizing for Transportation Management under  Forwarding Order Management

 Forwarding Order

## Define

Forwarding Order Types  and  Forwarding Order Management

 Define Item Types for Forwarding Order Management

.

Otherwise you have to enter any missing data for dangerous goods to the forwarding order at a later date. If a dangerous

goods number (UN number) has already been entered in the transit warehouse, this can be used as advance information.

You must then complete this data in the forwarding order either using dangerous goods template data or manually.

If you copy the attribute for dangerous goods without the corresponding data or with incomplete data from the freight

document and if you have already resolved the discrepancy, this attribute may be overwritten by the system the next time

you run the dangerous goods check.

## Overdimensional cargo

If you want to change this attribute manually, you have to set the method of checking overdimensional cargo to Manual

Check in Customizing for the item type (see above). Otherwise you can copy attributes only for package items.

## High-value cargo

It is only possible to change this attribute if you have set the High-Value Cargo checkbox at subitem level. It cannot be

changed at a higher level in the item hierarchy.

## Non-stackable packages

You can copy the attribute only for packages.

## Equipment group and equipment type

You can copy the attribute only for container items and ULD items.

If there are several freight units for a forwarding order item (this is displayed in the item details) and some of the attributes for

these freight units differ, the system splits the forwarding order items according to the freight units and copies the attributes to

the different forwarding order items.

The Processing Status of Item field indicates whether you have already copied actual data to your order data (it contains the

value Actual Data Was Copied).

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

121


1/14/26, 2:44 PM

You can also still change data in the forwarding order after execution has started and the cargo receipt status has been set to

On Hand. However, these changes are not copied to follow-on documents. If a settlement document already exists, first you

have to cancel this document, then you change the data, and finally you create a new document.

## Canceling Warehouse Activities

When warehouse workers cancel their posted activities in SAP EWM and report these again, the system automatically updates the

freight order in TM with this information. In some cases, however, you still have to make manual changes. For example, you may

need to resolve new discrepancies. For more information, see Cancellation of Warehouse Activities in Transit Warehousing Process.

## More Information

Handling Discrepancies (forwarding order)

Discrepancies and Events (freight order)

Quantity Discrepancies (freight order)

Other Discrepancies (freight order)

## Resolution of Discrepancies

Cancellation of Warehouse Activities in Transit Warehousing
Process

## Use

In SAP Extended Warehouse Management (SAP EWM), you can cancel many activities that have already been reported as finished.

For example, you can reset loading or unloading processes and report them again. In the transit warehousing process, this impacts

the integration with Transportation Management (TM).

SAP EWM reports most activities, such as the arrival of goods in the transit warehouse or the completion of the unloading process,

to TM by sending messages. In TM, the freight order and the freight units are then automatically updated with information about

the received cargo. If a warehouse worker cancels these activities and posts them again, the freight order and the freight units are

updated automatically again in TM. In some cases, however, the transportation planner has to resolve any discrepancies in TM that

may be caused by the updated information (such as missing or unexpected cargo).

The examples below describe the most common cancellations, explain how data is updated in TM, and tell you what you have to do

to resolve any blocks and discrepancies.

## Prerequisites

For more information, see Transit Warehousing and Resolution of Discrepancies. To handle discrepancies, you have to create a

discrepancy profile in Customizing for Transportation Management with the required discrepancy types and discrepancy

subcategories.

## Example

The following examples describe cancellations made by warehouse workers in SAP EWM during loading and unloading processes.

The cancellations themselves are not reported directly to TM. However, TM receives a message when the warehouse worker

This is custom documentation. For more information, please visit SAP Help Portal.

122


1/14/26, 2:44 PM

updates the unloading data and reports again that the loading or unloading process is finished.

## Example 1: Missing Handling Units During Unloading

A warehouse worker accidentally reports only part of the pallets of a freight unit as unloaded and closes the unloading process in

SAP EWM. The worker then cancels the completion of the unloading process and reports all the pallets as unloaded.

The process in TM is as follows:

1. The freight unit originally contains five subitems; the three handling units that were first reported as unloaded are displayed

with the cargo receipt status On Hand. The two unreported handling units are given the cargo receipt status Missing Cargo.

This freight unit also contains the discrepancy Missing Cargo, which refers to the two missing handling units.

The freight order and the two freight units are blocked for further planning.

2. Once the warehouse worker has reported the two missing pallets as unloaded, these two handling units are displayed in the

freight unit with the cargo receipt status and the discrepancy Unexpected Cargo. The freight unit is still blocked due to the

discrepancy.

3. To remove the block and resolve the discrepancy, choose  Resolve

 Resolve Discrepancy  on the Discrepancies tab

page in the item details.

## Example 2: Missing Handling Units During Loading

A warehouse worker accidentally loads two pallets fewer than the intended five pallets onto a truck and reports the loading

process as completed. The worker then cancels this process and reports another pallet as loaded. Finally, the worker cancels the

process again and reports all five pallets as loaded.

The process in TM is as follows:

1. The freight unit originally contains five subitems; the three handling units that were first reported as loaded are displayed

with the status Shipped. The main item also contains the discrepancy Missing Cargo as well as the two unreported

handling units with the status Missing Cargo.

The freight order and the two freight units are blocked by the system.

2. Once the warehouse worker has reported another pallet as loaded, this handling unit is also displayed in the freight unit as

Shipped. The freight unit now contains only one handling unit with the status Missing Cargo.

3. Once the warehouse worker has reported the last of the five pallets as loaded, all five handling units are displayed in the

freight unit as Shipped.

The system also automatically deletes the discrepancy Missing Cargo and removes the blocks.

## Example 3: Exchange of a Missing Handling Unit with Another Handling Unit

During the unloading process, a warehouse worker has reported a pallet as missing. The worker then cancels the process and

reports as unloaded a different pallet to that which is missing.

The process in TM is as follows:

1. The system creates a discrepancy called Missing Cargo. The missing handling unit is displayed in the freight unit with the

status Missing Cargo.

2. Once the warehouse worker has canceled the process and reported as unloaded a different handling unit to that which is

missing for this freight unit, the system resolves the discrepancy. The main item of the freight unit is displayed with the

status On Hand. The missing handling unit is displayed at subitem level with the status Missing Cargo and the new

handling unit is displayed as On Hand.

This is custom documentation. For more information, please visit SAP Help Portal.

123


1/14/26, 2:44 PM

## Other Discrepancies

Discrepancies in attributes, such as quantity and weight discrepancies, are automatically updated in TM after cancellations and

new notifications in SAP EWM.

## More Information

Handling Discrepancies in Transit Warehousing Process

Automatic Reassignment of Package Items

## Use

If the warehouse workers have finished unloading in the transit warehouse, gateway, or in the container freight station and the

truck has left the yard, the system automatically sends the message LoadingAppointmentNotification from Extended

Warehouse Management (EWM) to Transportation Management (TM) (see Transit Warehousing). This message may contain

unexpected package items, in other words items other than those that are planned. If you have configured your TM system in such

a way that no discrepancies are to be created, TM automatically reassigns these package items.

## Prerequisites

For more information, see Transit Warehousing.

## Features

The following describes how the TM system handles unexpected package items contained in the message from EWM.

## Reassignment across freight orders without freight unit split

Initial situation: One or more package items belonging to the same freight unit are assigned to a different freight order than

that referred to in the message from EWM.

In this case, TM removes the package items from this freight order and assigns them to the freight order referred to in the

message from EWM.

## Assignment of unplanned freight units without freight unit split

Initial situation: One or more package items belong to an unplanned freight unit for the current transportation stage.

In this case, TM assigns the package items to the freight order referred to in the message from EWM.

## Removal of the assignment of freight units

Initial situation: One or more package items are assigned to the freight order referred to in the message from EWM.

However, they no longer appear in the message.

In this case, TM removes the package items from the freight order. In other words, it removes the assignment of the freight

unit to the freight order for the current transportation stage.

## Assignment of unplanned freight units with freight unit split

Initial situation: One or more package items belong to an unplanned freight unit. However, the freight unit has other

package items that are not contained in the message from EWM.

This is custom documentation. For more information, please visit SAP Help Portal.

124


1/14/26, 2:44 PM

In this case, TM first splits the freight unit. TM assigns the package items contained in the message to the freight order

referred to in the message from EWM.

## Reassignment across freight orders with freight unit split

Initial situation: One or more package items are assigned to a different freight order to that referred to in the message from

EWM. The corresponding freight unit has other package items that are not contained in the message from EWM.

In this case, TM removes the package items from the other freight order and assigns them to the freight order referred to in

the message from EWM. TM then splits the freight unit. This means that after reassignment not all package items in the

freight unit are assigned to the freight order contained in the message; only those package items that are contained in the

message from EWM are assigned. You have to reschedule the other package items that are not contained in the message

from EWM for the current transportation stage.

## More Information

For more information about handling discrepancies, see Handling Discrepancies in Transit Warehousing Process.

Warehouse Billing

## Use

You can perform the following activities:

Sell warehouse services to a customer and periodically bill the customer for the services you have provided for a time

period.

Purchase warehouse services from an external service provider and self-bill to pay the service provider for the services you

have used for a time period.

Warehouse billing uses the agreements, charge calculation, and settlement features in Transportation Management (TM).

  Note

You can also integrate TM with an external SAP Extended Warehouse Management.

## Agreement Management

You can create a freight agreement with an external service provider for the warehouse services that you want to purchase, or you

can create a forwarding agreement with a customer for the warehouse services that you want to sell. TM transfers the agreement

information to Extended Warehouse Management (EWM) and automatically creates warehouse billing measurement requests in

EWM. For more information, see Creation of Agreement.

## Charge and Settlement Management

In EWM, you can measure and determine the quantity of warehouse services used for a time period. EWM transfers the quantity

information to TM. TM uses this feature for warehouse services charge calculation and settlement. For more information, see

Charge Calculation and Settlement.

## Integration

## Creation of Forwarding Orders

This is custom documentation. For more information, please visit SAP Help Portal.

125


1/14/26, 2:44 PM

TM creates a forwarding order for billing a customer by Web services. EWM sends warehouse billing measurements using the

service proxy TransportationRequestRequest_Out. TM receives the data and creates a forwarding order using the service

proxy TransportationRequestRequest_In.

To change or extend the data transferred through the service interface TransportationRequestRequest_In, use the

Business Add-In (BAdI) in Customizing for Transportation Management under  Business Add-Ins (BAdIs) for Transportation

Management

## Integration

 Enterprise Services

  Forwarding Order Management

  Forwarding Order

 BAdI for

TransportationRequestRequest_In .

## Creation of Service Orders

TM creates a service order for self-billing for a service provider by Web services. EWM sends warehouse billing measurements

using the service proxy TransportationOrderGenericRequest_Out. TM receives the data and creates a service order

using the service proxy TransportationOrderGenericRequest_In.

To change or extend the data transferred through the service interface TransportationOrderGenericRequest_In, use the

BAdI in Customizing for Transportation Management under  Business Add-Ins (BAdIs) for Transportation Management

## Integration

 Enterprise Services

  Freight Order Management

  Freight Order

 BAdI for

TransportationOrderGenericRequest_In .

For more information, see http://help.sap.com/s4hana under  Product Assistance

 Enterprise Business Applications

 Supply

## Chain

## Warehousing

 Extended Warehouse Management (EWM)

 Warehouse Billing .

More Information

Agreement Maintenance

## Charge Calculation

Freight Agreement Maintenance

Forwarding Agreement Maintenance

## Settlement

Creation of Agreement

## Use

You can create a forwarding agreement for selling warehouse services to a customer or a freight agreement to purchase

warehouse services from a service provider. Subsequently, you can bill or self-bill for the warehouse services used.

You can create an agreement with items that are assigned a calculation sheet for charging services for a specific warehouse.

In the charge line of the calculation sheet, you can specify a measurement remark to describe how to measure the warehouse

service. When Transportation Management (TM) sends the agreement information to Extended Warehouse Management (EWM), a

warehouse expert can view the measurement remark and decide how the item should be measured.

When you release the agreement, TM automatically transfers the agreement data to EWM for warehouse billing measurement. You

cannot edit the item after you have released the agreement. You must change the status of the agreement to In Process to make

any changes.

## Prerequisites

This is custom documentation. For more information, please visit SAP Help Portal.

126


1/14/26, 2:44 PM

In Master Data, you have performed the following actions:

Specified the EWM logical system and the warehouse number in a location as the warehouse location

Specified the billing period for the customer or service provider.

## For more information, see Master Data

You have performed the following actions in Customizing:

You have selected the SAP EWM Integration checkbox and specified an output profile in Customizing for Transportation

Management under  Master Data

  Agreements and Service Products  in the following Customizing activities:

Define Freight Agreement Types for freight agreements

Define FWAs and Service Product Catalog Types for forwarding agreements

  Note

When you release the agreement, the output profile executes a B2B message that enables the system to transfer

agreement data to EWM.

In Customizing for Transportation Management under Basic Functions, you have performed the following actions:

Defined service types for the warehouse services in the Customizing activity Define Service Types under

## General Settings

Defined charge types for the warehouse services in the Customizing activity Define Charge Types under

## Basic Settings

Assigned the charge types to the service types in the Customizing activity Assign Charge Types to Service

Types under Basic Settings

  Note
Ensure that both of the charge type and the service type have the same name.

## Process

1. From the launchpad, open one of the following apps to create a forwarding agreement or freight agreement:

To create a forwarding agreement, open the Create Forwarding Agreement app.

To create a freight agreement, open the Create Freight Agreement app.

2. Specify the agreement type and create the agreement. Specify the header information and create the agreement item with

the relevant service type. You can specify the warehouse in the Preconditions tab page for the item. In the Trade Lane tab

page, specify the following:

## Field

Orientation

Value

From

Source Type

Location

## Source

<Warehouse Location>

This is custom documentation. For more information, please visit SAP Help Portal.

127


1/14/26, 2:44 PM

3. You specify calculation sheet details for the charge type associated with the service type for the item. You specify rates

based on the quantity of the service.

You can specify a single rate in the following format in the calculation sheet:

Field

## Value

Charge Type

<Charge Type>

## Amount

<Rate Amount>

Currency

<Currency>

Calculation Base

QUANTITY_VAL

Quantity

<Quantity>

Unit

AU

For multiple rates, you can create a rate table. In the rate tale, you specify QUANTITY_VAL as the dimension and

specify the rate vales based on the quantity.

  Example

You specify the following:

A charge type for the storage service according to the daily stock in tons

A currency of USD and calculation method type of Clipping

You specify the following rate table details:

Scale Type

Scale from

Calculation Base

QUANTITY_VAL

Quantity

Unit

1

AU

You define the following scale:

QUANTITY_VAL Rate

0

100

1000

1.1

1

0.8

Depending on the calculation method of the charge line, if 450 tons of stock are measured from July 12,

2014 to July 19, 2014, one of the following occurs:

The first 100 tons of stock is charged at 1.1 USD per ton, and the second 350 tons are charged as 1

USD per ton.

A standard rate of 1.1 USD per ton is applied to all 450 tons.

This is custom documentation. For more information, please visit SAP Help Portal.

128


1/14/26, 2:44 PM
## More Information

For more information, see http://help.sap.com/s4hana under  Product Assistance

 Enterprise Business Applications

## Supply Chain

 Extended Warehouse Management (EWM)

## Warehouse Billing

 Request for Warehouse Billing

Measurement

.

Agreement Maintenance

Freight Agreement Maintenance

Forwarding Agreement Maintenance

## Settlement

Assigning Billing Periods for Business Partners

Charge Calculation and Settlement

## Use

You use Transportation Management for automatically calculating charges for the warehouse services used and for settlement in

Sales and Distribution (SD).

You can periodically transfer the quantity of warehouse services used from Extended Warehouse Management to Transportation

Management (TM). TM creates a forwarding order or a service order when you transfer the quantity. You can use these documents

to display the calculated charges and for settlement in SD.

## Integration

EWM determines the quantity of services used for a billing period. For more information, see http://help.sap.com/s4hana under

## Product Assistance

 Enterprise Business Applications

## Supply Chain

 Extended Warehouse Management (EWM)

 Warehouse Billing .

## More Information

Charge Calculation of Warehouse Services

Settlement of Service Orders and Forwarding Orders

Creation of Agreement

## Warehouse Billing

Charge Calculation of Warehouse Services

## Use

When you distribute a warehouse billing measurement (WBM) from Extended Warehouse Management (EWM) to Transportation

Management (TM), TM creates a service order or forwarding order corresponding to the distributed WBM.

The forwarding order or service order automatically calculates charges for the warehouse services used based on the agreement

you have defined with the customer or service provider in TM.

This is custom documentation. For more information, please visit SAP Help Portal.

129


1/14/26, 2:44 PM
## Integration

EWM determines the quantity of services used for a billing period. For more information, see http://help.sap.com/s4hana under

## Product Assistance

 Enterprise Business Applications

## Supply Chain

 Extended Warehouse Management (EWM)

 Warehouse Billing .

## Prerequisites

In Customizing for Transportation Management under

## Master Data

 Agreements and Service Products , you have

performed one or more of the following activities:

Assigned a default service order type to a freight agreement type in the Customizing activity Define Freight

## Agreement Types

Assigned a forwarding order type to a forwarding agreement type in the Customizing activity Define FWA and

## Service Product Catalog Types

In the Customizing for Transportation Management under  Basic Functions

 Charge Calculation

## Basic Settings , you

have performed the following activities:

You have specified a Calculation Date Type of Order Date in the Customizing activity Define Calculation Profiles

for a calculation profile.

You have assigned this calculation profile to the relevant charge profile in the Customizing activity Define Charges

Profile.

This enables the system to use the execution end date from the service order or forwarding order as the charge calculation

date instead of the system date.

## Features

A forwarding order for billing a customer, or a service order for warehouse service procurement for a service provider contains the

following warehouse billing relevant information:

Items with quantity for a time period

Service Type of the warehouse services

Warehouse numbers

## Billing periods

Service providers, or the customers as the External Sold-to parties

The warehouse billing measurement document in the Document Flow tab page

## Activities

To find forwarding orders for warehouse billing, enter the warehouse billing measurement document number in the field Buyer’s

Reference Number in the quick criteria maintenance screen in the Forwarding Orders app. Then choose Show Quick Criteria

Maintenance.

To find service orders for warehouse billing, enter the warehouse billing measurement document number in the field Document in

the quick criteria maintenance screen in the Service Orders app. Then choose Show Quick Criteria Maintenance.

You can perform the following activities and recalculate charge:

This is custom documentation. For more information, please visit SAP Help Portal.

130


1/14/26, 2:44 PM

## Change the quantity

Specify new items for warehouse services

Delete or add new charges

## More Information

Charge Calculation and Settlement

Warehouse Billing

Forwarding Order

Service Order

## Charge Calculation

Settlement of Service Orders and Forwarding Orders

## Use

You can use the forwarding settlement document for billing a customer. You can use the freight settlement document to credit a

service provider. Subsequently, you can send this to Sales and Distribution (SD) for final settlement.

You can create settlement documents from service orders or a forwarding orders relevant to warehouse billing. For more

information about finding service orders and forwarding orders relevant for warehouse billing, see Charge Calculation of

Warehouse Services

## Integration

Extended Warehouse Management (EWM) determines the quantity of services used for a billing period. For more information,

http://help.sap.com/s4hana under  Product Assistance

 Enterprise Business Applications

 Supply Chain

## Extended

Warehouse Management (EWM)

 Warehouse Billing .

## Prerequisites

You have enabled invoice Integration of Transportation Management (TM) with SD.

In Customizing for Transportation Management under  Settlement

## Define Settlement Profiles , you have specified

weather you want to create a collective settlement or individual settlements based on the billing period.

You have activated the business add-in implementation /SCMTMS/CFIR_DATES_WB_IMP for invoice date determination

in Customizing for Transportation Management under  Business Add-Ins (BAdIs) for Transportation Management

## Settlement

## Forwarding Settlement

 BAdI: Determination of Invoice Date for FWSDs .

You have activated the business add-in implementation /SCMTMS/SFIR_DATES_WB_IMP for settlement date

determination in Customizing for Transportation Management under  Business Add-Ins (BAdIs) for Transportation

Management

## Settlement

## Freight Settlement

 BAdI: Determination of Settlement Date for Freight Settlement

Documents .

You can modify warehouse billing forms in the PPF action profile for printing in Customizing for Cross-Application

Components under  Processes and Tools for Enterprise Applications

 Reusable Objects and Functions for BOPF

## Environment

 PPF Adapter for Output Management

## Maintain PPF Settings

This is custom documentation. For more information, please visit SAP Help Portal.

131


1/14/26, 2:44 PM
## Features

The system can take into account the billing period to create either a collective settlement document or individual

settlement documents for service orders and forwarding orders.

You can print warehouse billing forms from the settlement document. You can print the forms using the action profile

/SCMTMS/PRINT_PFCFI_WB in the Output Management tab page of a settlement document.

The system uses the service period of the service order or the forwarding order as the invoice date of the settlement

document. The system usually uses the end date of the period as invoice date.

You can post the settlement document in SD for final settlement.

After the settlement document is posted in SD, you can create additional credit memos or forwarding settlement

documents to adapt any changes to the charge and post it in SD for correction.

More Information

## Settlement

Forwarding Settlement

## Freight Settlement

Charge Calculation of Warehouse Services

## Charge Calculation

Assigning Billing Periods for Business Partners

## Use

You assign a billing period for a customer or a service provider to specify the periods that the system uses to calculate charge for

the warehouse services that are used.

In the Extended Warehouse Management (EWM) system, the system generates a warehouse billing measurement document for a

billing period and transfers quantity data to the Transportation Management (TM) system for charge calculation and settlement.

## Prerequisites

Integration of Billing Schedule with Extended Warehouse Management (EWM)

When you save a forwarding agreement or freight agreement and the agreement status is Released, TM sends the calendar ID and

the forwarding agreement to EWM. You must specify a calendar in EWM that has the exact same settings as the TM calendar that

you transfer to EWM. You can specify a factory calendar for EWM in Customizing for SAP NetWeaver under  General Settings

 Maintain Calendar

.

  Example

You have a forwarding agreement or freight agreement in place with a business partner for a warehouse service where you pack

a pallet with goods. You charge USD 1 to pack a single pallet. You have a weekly billing schedule in place with the business

partner. When the weekly billing schedule reaches its due date, EWM sends the number of pallets it packed during the week for

the business partner to TM. You can then calculate the amount due and include the charge in a forwarding settlement

document in TM.

This is custom documentation. For more information, please visit SAP Help Portal.

132


1/14/26, 2:44 PM
## Procedure

## Specifying Billing Periods for a Customer

1. Go to the Maintain Business Partner transaction (transaction BP).

2. Enter the business partner.

3. Display the BP role Sold-to Party.

4. In the Sales Org. Settings screen area on the Customer Org. Data tab page, specify a sales organization.

5. Enter the factory calendar in the Billing Schedule field, for example, Weekly Settlement.

Specifying Billing Periods for a Service Provider

1. Go to the Maintain Business Partner transaction (transaction BP).

2. Enter the business partner.

3. Display the BP role Carrier.

4. In the Purchase Org. Settings screen area on the Vendor Org. Data tab page, specify a purchasing organization.

5. Enter the factory calendar in the Billing Schedule field, for example, Monthly Settlement.

## More Information

The EWM system determines the quantity of services used for a billing period. For more information, see

http://help.sap.com/s4hana_op_1709 under  Product Assistance

 Enterprise Business Applications

## Supply Chain

 Extended Warehouse Management (EWM)

 Warehouse Billing .

## Creation of Agreement

Integration with SAP Event Management

## Use

This function enables you to integrate Transportation Management (TM) with SAP Event Management, and to track and monitor

events for business objects in business processes.

## Prerequisites

You have installed SAP Event Management, and made the settings in Customizing for Event Management integration.

You have made the necessary Customizing settings in TM. For more information, see Customizing for Transportation

Management under

## Integration

 Tracking and Tracing of Processes and Documents

 Prerequisites for Tracking and

Tracing .

You have maintained the system connection to TM.

## Features

SAP Event Management offers visibility processes to monitor transportation execution in connection with TM.

This is custom documentation. For more information, please visit SAP Help Portal.

133


1/14/26, 2:44 PM

The transportation execution visibility processes enable users in roles such as transportation dispatcher, shipper, or sold-to party,

to track and monitor planned events or to report an actual event. Tracking and tracing is provided for the following business

document types in TM:

Freight units

Freight orders

Freight bookings

Transportation unit

## Resources

Instruction execution for standard operating procedures

## More Information

## Tracking of Freight Units

Tracking of Freight Orders and Freight Bookings

Tracking of Transportation Units

Tracking of Resources

Tracking of Instructions

Tracking of Freight Units

## Use

You can use this function as a tracking process to track freight units. It is one of the functions that monitor the execution of

transportation processes managed by Transportation Management (TM).

Execution tracking can be done with or without SAP Event Management:

For information about tracking executions without an external event management system, see Execution Tracking.

If you connect to SAP Event Management, you can use this visibility process to integrate TM and SAP Event Management.

For more information, see Integration with SAP Event Management.

In transportation planning, the shipper or sold-to party asks you to transport goods from one location to another location. On

receiving the order, your transportation dispatcher creates a transportation requirement in TM. TM creates freight units to fulfill

the transportation requirement. If you have connected SAP Event Management, you can monitor the execution phase of the freight

units by tracking the corresponding event handlers in SAP Event Management. SAP Event Management enables the following

features:

Your shipper or sold-to party can monitor the status changes of freight units.

Your transportation dispatcher, shipper or sold-to party, ship-to party, and carrier can monitor the expected and actual

events for freight units, from loading the goods to the proof of delivery at the ship-to party.

Your ship-to party can report the proof of delivery.

Your carrier can report events, including unexpected events, for example, a delay.

This is custom documentation. For more information, please visit SAP Help Portal.

134


1/14/26, 2:44 PM

Your transportation dispatcher can receive an alert when an unexpected event is reported, for example, damage to an item.

## Features

You can track the following expected events for freight units in SAP Event Management:

Scheduled

Loading Begin

Loading End

## Departure

Arrival at Destination

Unloading Begin

## Unloading End

There are two ways of reporting the expected event:

When your carrier sends an event message from the SAP Event Management Web user interface to TM, TM updates the

freight unit with the information in the event message.

When you update the freight unit directly in TM, TM sends an event message to SAP Event Management. SAP Event

Management updates the data for the freight unit.

SAP Event Management can also track the following unexpected events. When these events occur, SAP Event Management sends

an alert to TM:

Delay

## Damage

Tracking of Freight Orders and Freight Bookings

## Use

You can use this function as a tracking process to track freight orders and freight bookings. It is one of the functions that monitor

the execution of transportation processes managed by Transportation Management (TM).

Execution tracking can be done with or without SAP Event Management:

For information about tracking executions without an external event management system, see Execution Tracking.

If you connect to SAP Event Management, you can use this visibility process to integrate TM and SAP Event Management.

For more information, see Integration with SAP Event Management.

When connected to SAP Event Management, this function enables the following features:

Your shipper or sold-to party can monitor the expected events for their freight orders and freight bookings.

Your transportation dispatchers can monitor all events including unexpected events for freight orders and freight bookings

in their organizational unit. For example, they can receive an alert if there is a delay.

This is custom documentation. For more information, please visit SAP Help Portal.

135


1/14/26, 2:44 PM
## Features

You can track the following expected events for freight orders and freight bookings in SAP Event Management:

Loading Begin

Loading End

Proof of Pick-up

Departure

## Clear Customs

Arrival at Destination

Unloading Begin

Unloading End

## Proof of Delivery

There are, for example, the following ways of reporting the expected event:

When your carrier sends an event message from the SAP Event Management Web user interface to TM, TM updates the

freight order or freight booking with the information in this event message.

When you update the freight order or freight booking directly in TM. SAP Event Management updates the data for the

freight order or freight booking.

You can display the source of execution information on the Execution tab page of a freight order or freight booking in TM.

SAP Event Management can also track unexpected events. You can report these unexpected events for an item of a freight order or

freight booking in TM (Discrepancies and Events tab page). When delays occur, SAP Event Management issues an alert.

Tracking of Transportation Units

## Use

You can use this function as a tracking process to track transportation units. It is one of the functions that monitor the execution of

transportation processes managed by Transportation Management (TM).

Execution tracking can be done with or without SAP Event Management:

For information about tracking executions without an external event management system, see Execution Tracking.

If you connect to SAP Event Management, you can use this visibility process to integrate TM and SAP Event Management.

For more information, see Integration with SAP Event Management.

In transportation planning, the shipper or sold-to party asks you to transport goods from one location to another. On receiving the

order, your transportation dispatcher creates a transportation requirement in TM. TM creates freight units to fulfill the

transportation requirement. If you have connected SAP Event Management, you can monitor the execution phase of the

transportation units by tracking the corresponding event handlers in SAP Event Management. SAP Event Management enables the

following features:

Your shipper or sold-to party can monitor the status changes of transportation units.

This is custom documentation. For more information, please visit SAP Help Portal.

136


1/14/26, 2:44 PM

Your transportation dispatcher, shipper or sold-to party, ship-to party, and carrier can monitor the expected and actual

events for transportation units, from loading the goods to the proof of delivery at the ship-to party.

Your transportation dispatcher, shipper or sold-to party, ship-to party, and carrier can monitor the expected and actual

events for transportation units.

Your carrier can report events, including unexpected events, for example, a delay.

Your transportation dispatcher can receive an alert when an unexpected event is reported, for example, delay of the

transportation unit.

## Features

You can track the following expected events for transportation units in SAP Event Management:

Loading Begin

Loading End

Coupling

## Departure

Arrival at Destination

Decoupling

Unloading Begin

## Unloading End

There are two ways of reporting the expected event:

When your carrier sends an event message from the SAP Event Management Web user interface or any other external

interface to SAP Event Management, SAP Event Management updates the data of the corresponding event handler and

sends an update to TM. Then TM updates the transportation unit with the information in the event message and if

applicable propagates the event to related freight documents such as freight units.

When you update the transportation unit directly in TM, TM sends an event message to SAP Event Management. SAP Event

Management updates the data for the transportation unit.

SAP Event Management can also track the following unexpected events:

## Delay

When these events occur, SAP Event Management can send an alert to TM.

Tracking of Resources

## Use

You can use this function to track resources that are defined as master data in Transportation Management (TM). This tracking

process is part of the functions to monitor the transportation execution of processes managed by TM. The visibility process

integrates TM and SAP Event Management. For more information, see Integration with SAP Event Management.

You can use this resource tracking visibility scenario to track resources over their entire lifecycle:

This is custom documentation. For more information, please visit SAP Help Portal.

137


1/14/26, 2:44 PM

Tracking starts when the resource is entered into the TM master data with the SAP Event Management system connected.

Further, you must set the resource attribute Relevant for Event Management and assign a Means of Transport that is not

marked as Multiresource.

Tracking ends when the attribute Relevant for Event Management is removed.

If you have connected SAP Event Management, you can monitor the execution events that are related to a certain resources by

tracking the corresponding event handlers in SAP Event Management. SAP Event Management enables the following features:

Your transportation dispatcher can check the availability of a certain resource or can get an overview over all available

resources.

Your carrier can report events directly for a resource, for example to update the actual position.

Your transportation dispatcher can receive an alert when an unexpected event is reported, for example, the damage of a

resource

## Features

The following resource types are supported:

Active vehicle resources such as trucks or locomotives

Passive vehicle resources such as trailers or railcars

## Transportation units such as containers

You can track the following expected events for resources in SAP Event Management:

Coupling (only relevant for vehicle resources)

## Departure

## Arrival at Destination

Decoupling (only relevant for vehicle resources)

There are three ways of reporting the expected event:

When your carrier sends an event message for the related freight document via SAP Event Management to TM, TM

propagates this event message back to the related resource event handler(s) in SAP Event Management. SAP Event

Management updates the data for the resource event handler(s) accordingly.

When you update the execution information of a freight document directly in TM, TM sends an event message to the related

resource event handler(s) in SAP Event Management. SAP Event Management updates the data for the resource event

handler(s) accordingly.

When your carrier sends an event message directly for the resource via SAP Event Management. SAP Event Management

updates the data for the resource event handler accordingly. However there is no automatic propagation of the event to the

related freight document(s) in TM.

SAP Event Management can also track the following unexpected events:

Sighting (to update the actual position of the resource)

## Damage

This is custom documentation. For more information, please visit SAP Help Portal.

138


1/14/26, 2:44 PM

Tracking of Instructions

## Use

You can use this function to track and monitor the execution of instructions that are assigned to forwarding orders or freight units

in Transportation Management (TM). Instructions are introduced with TM 9.0 SP02 in what are known as standard operating

procedures (SOP) in the transportation industry. The visibility process integrates TM and SAP Event Management. For more

information, see Integration with SAP Event Management.

Typically, instructions are pre-defined in forwarding agreements and serve as templates. Once a forwarding order is created from a

forwarding agreement, the corresponding instructions are copied into the forwarding order and where applicable, also propagated

to the related freight units. If you have connected SAP Event Management, you can monitor the execution of these instructions by

tracking the corresponding event handlers in SAP Event Management. SAP Event Management enables the following features:

Your transportation dispatcher can monitor the status changes of an instruction.

If the alert framework has been set up, your transportation planner can receive an alert when the alert date of the

instruction is reached before the execution of the instruction is completed

## Features

You can track the one expected event for instructions in SAP Event Management:

## Instruction Execution

For each instruction there is an alert date and a due date, both of which are set in TM. Each instruction has one of the

following six statuses in TM:

Pending (initial value) – can be set manually in TM

In progress – can be set manually in TM

## Completed – can be set manually in TM

Completed after Due Date – automatically set by TM if completion date is after due date

Alert – set by SAP Event Management or

## Overdue – set by SAP Event Management

The expected event date of the expected event is determined as follows:

Until the alert date is reached, the expected event date is the alert date.

After the alert date, the expected event date is changed to the due date.

Monitoring of the status of the instruction is done in SAP Event Management. The monitoring sequence is as follows:

After the alert date until the due date, if the instruction has not been completed, the status of the instruction is set

to alert (in TM and SAP Event Management).

After the due date if the instruction has not been completed, the status of the instruction is set to overdue (in TM

and SAP Event Management).

Immediately a change to the status of an instruction is made manually in TM, SAP Event Management is informed, and the

corresponding event handler status is updated. Similarly if the status of the instruction changes due to monitoring in SAP

Event Management, the corresponding event handler status is updated and the changed status is sent to TM.

This is custom documentation. For more information, please visit SAP Help Portal.

139


1/14/26, 2:44 PM

  Note

There are no unexpected events supported for instructions.

## Integration with SAP Global Trade Services

Integration with SAP Global Trade Services (GTS) allows for customs processing, trade compliance checks, and customs transit

discharges declarations for Transportation Management (TM). This integration ensures compliance with embargos, sanction party

lists, and customs clearance, and supports outbound and inbound processes for trade compliance.

You can integrate GTS with your TM system in an internal, external, and decentalized setup.

## Use

The integration of with the GTS application enables you to do the following:

Handle customs processing for TM business documents in SAP Global Trade Services

Perform trade compliance checks for TM business documents in SAP Global Trade Services

Handle customs transit discharges declarations for TM freight orders in SAP Global Trade Services.

You can find more information about these topics under Related Information.

## Related Information

Integration with SAP Global Trade Services in Advanced Shipping and Receiving

SAP GTS Integration for the Outbound Process

SAP GTS Integration for the Inbound Process

Integration Scenarios for SAP Global Trade Services

## Global Trade

SAP GTS Integration in Decentralized EWM and TM

## Integration Scenarios for SAP Global Trade Services

You can integrate Transportation Management (TM). and SAP Global Trade Services (GTS) by using SAP NetWeaver Process

Integration (SAP NetWeaver PI) or a point-to-point connection (Web Services Reliable Messaging). Data is exchanged using

enterprise services.

## Integration

The following integration scenarios and enterprise services are available in TM:

## TM_GTSExportDeclarationIntegration

The following enterprise services are available for this scenario in the Transportation Order Processing process component:

Request Export Declaration

## Request Export Declaration Cancellation

Change Transportation Order Based on Export Declaration Confirmation

This is custom documentation. For more information, please visit SAP Help Portal.

140


1/14/26, 2:44 PM

## TM_GTSTradeComplianceCheckIntegration

The following enterprise services are available for this scenario in the Transportation Order Processing process component:

Request Trade Compliance Check

## Request Trade Compliance Check Cancellation

## Change Transportation Order Based on Trade Compliance Check Confirmation

The following enterprise services are available for this scenario in the Transportation Request Processing process

component:

Request Trade Compliance Check

## Request Trade Compliance Check Cancellation

Change Transportation Order Based on Trade Compliance Check Confirmation

## TM_GTS CustomsTransitDischargeDeclarationIntegration

The following enterprise services are available for this scenario in the Transportation Order Processing process component:

## Request Customs Transit Discharge Declaration

Change Transportation Order Based on Customs Transit Discharge Declaration Confirmation

## Enterprise Services Without Integration Scenario

The following enterprise services are not assigned to an integration scenario:

## Request Customs Invoice

Change Transportation Order Based on Customs Invoice Confirmation

## Related Information

Advanced Shipping and Receiving

Integration with SAP Global Trade Services

## Master Data Replication

You use this function to replicate master data from a source system, such as an ECC system or an SAP S/4HANA system, to the

Transportation Management (TM) component of an SAP S/4HANA system (target system).

## Data Replication Framework

You can use the Data Replication Framework (DRF) to replicate master data such as business partners, products, and locations

between source systems and target systems.

The DRF uses a Key Mapping Framework to map the IDs of the corresponding objects in the source and the target system when

replicating master data. This allows the target system to determine the IDs of local master data entities based on the IDs of the

master data objects in the source system. This is to ensure that an object in the target system can be assigned the same value as

the corresponding object in the source system, even if the object IDs in the two systems are not identical. Key mapping is essential

if a target system receives data from several source systems which may contain the same objects with different IDs or where the

usage of the same key for different entities in different source systems might occur.

This is custom documentation. For more information, please visit SAP Help Portal.

141


1/14/26, 2:44 PM
Related Information

Set Up Data Replication

Data Replication

## Business Partner

To replicate business partner master data, you set up a replication model in your source system using the DRF customizing

transaction DRFIMG, and define the target system as part of the replication model.

You use outbound implementation 986_3 – Outbound Impl. for BP/REL Services for the business object 986 –

Business Partner.

The replication uses the business partner service BusinessPartnerSUITEBulkReplicateRequest and the system

activates unified key mapping automatically.

To activate key mapping you use transaction IDMIMG. The target system uses confirmation message

BusinessPartnerSUITEBulkReplicateConfirmation to transfer key mapping information back to the source system.

For business partners, the key mapping supports the two object identification types 888 – Business Partner ID and 889

– Business Partner UUID.

The following business partner roles are replicated with the Data Replication Framework:

000000 Business Partner (Gen.)

BUP004 Organizational Unit

CRM010 Carrier

SLLCOF Customs Office

TM0001 Driver

FLVN01 Supplier

FLVN00 FI Supplier

FLCU01 Customer

FLCU00 FI Customer

  Note

If you need locations for business partners in the target system you create these locally in the TM component of your SAP

S/4HANA system.

## Customer/Vendor Integration

In SAP S/4HANA the business partner is the central object to hold partner data. Customer/Vendor Integration (CVI) creates

customer master data or vendor master data, if required, based on a business partner. This means a business partner is always

available for handling customer or vendor data in an SAP S/4HANA system.

This is custom documentation. For more information, please visit SAP Help Portal.

142


1/14/26, 2:44 PM

## Product

You replicate product master data for products which do not depend on organizational levels such as plant, storage location, sales

organization, distribution channel, warehouse number, or storage type. The master data replicated in TM includes client-

dependent data, language-dependent material descriptions, and conversion factors for units of measure.

For the replication of products, you set up a replication model in your source system using the DRF customizing, transaction

DRFIMG, and define the target system as part of the replication model.

If the source system is an SAP S/4HANA system, you use the existing outbound implementation 194_3 – Outbound Impl.

for Product via Services for the business object 194 – Material.

If the source system is an SAP ECC system, you use outbound implementation 194_1 – Material through IDoc. Note that if

you use SAP ECC enhancement package 7 or 8, you first need to implement SAP Note 3313230

## Enable Outbound

Implementation 194_1 (Material via iDoc) for DRF.

You activate the unified key mapping for products in the customizing of the target system, transaction IDMIMG, to enable the

identification of local product entities.

The key mapping information is transferred back to the source system with confirmation message

ProductMDMSUITEBulkReplicateConfirmation.

The key mapping for products supports the two object identification types 20 – Material ID Internal Format and 924

– Material ID External Format.

## Location

Plants and shipping point customizing data exist in SAP S/4HANA and SAP ECC systems but in TM processes this information is

represented in Location master data. To replicate plant and shipping point information the source system creates location master

data which it then replicated to the target system. However if the source system is an ECC system, no location object is available

and so the plant and shipping point Customizing settings are replicated to TM where the locations can then be created based on

this data.

For the replication of locations, you set up a replication model in your source system via the DRF customizing, transaction DRFIMG,

and define the target system as part of the replication model.

If the source system is an SAP S/4HANA system, you use the outbound implementation 189_1 which is the outbound

implementation for locations using service 189 - Location.

If the source system is an SAP ECC system, you use the following outbound implementations:

464_L

The outbound implementation to replicate plants into locations, based on the business object 464 (Plant)

## DRF_0045_L

The outbound implementation to replicate shipping points / receiving points into locations, based on the business object

DRF_0045 (Shipping Point / Receiving Point)

The target system uses confirmation message LocationBulkReplicateConfirmation to transfer key mapping and status

information back to the source system.

This is custom documentation. For more information, please visit SAP Help Portal.

143


1/14/26, 2:44 PM

  Note

If the source system is an SAP ECC system the key mapping information is not stored in the source system.

You activate the unified key mapping for locations in the customizing of the target system, transactionIDMIMG, to enable the

identification of local product entities.

The key mapping for locations supports the two object identification types 198 - Location Number and 580 - Location

UUID. In this case the source system is an SAP S/4HANA system.

  Note

If you need locations for business partners in the target system you create these locally in the TM component of your SAP

S/4HANA system.

This is custom documentation. For more information, please visit SAP Help Portal.

144
