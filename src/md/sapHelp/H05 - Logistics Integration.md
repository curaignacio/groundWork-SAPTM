1/14/26, 2:17 PM

Transportation Management (TM)

Generated on: 2026-01-14 14:17:34 GMT+0000

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


1/14/26, 2:17 PM

## Logistics Integration

You can integrate Transportation Management (TM) with components in the same system or an external system. Alternatively, you

can integrate a decentralized EWM and TM system with an external system.

For more information see:

Internal TM Component Integration

External TM System Integration

Advanced Shipping and Receiving

Advanced SR for Decentralized EWM and TM

Internal TM Component Integration

## Use

You use integration of orders, deliveries, and JIT calls to facilitate transportation planning and execution in Transportation

Management (TM) based on orders created in Sales and Distribution (SD), Materials Management (MM), deliveries created in

Logistics Execution (LE), and JIT calls created in Next Generation Just-In-Time (nJIT).

With the Advanced Shipping and Receiving process, you can have enhanced integration between Transportation Management

(TM) and Extended Warehouse Management (EWM). A new or updated sales order or sales scheduling agreement triggers the

creation of LE deliveries. The integration uses the warehouse request and its handling units in EWM and freight units in TM to allow

TM to update predecessor documents and also trigger actions such as goods movements or reversal of goods movements.

Integration with nJIT enables you to conduct the entire process on the basis of a JIT call. This includes the execution of sequenced

and forwarded JIT calls. A JIT call can also trigger the creation of inbound deliveries, and integration between components ensures

that changes status updates are communicated between nJIT, LE, and EWM.

For more information, see Advanced Shipping and Receiving.

You can also integrate a decentralized EWM and TM system with an external ERP system and perform transportation planning

based on outbound delivery orders.

The TM component creates or updates freight units directly for orders or deliveries which you have defined in Customizing as

relevant for TM integration. If such orders or deliveries are created or changed, the system creates or updates freight units in the

TM component once you save the order or delivery. The integration allows you to continuously react to changes made to orders

and deliveries in SD, MM and LE. In particular, integration with these components enables you to:

## Collectively plan transportation for all orders and scheduling agreements

Perform transportation planning in TM based on sales or purchase orders, prior to delivery creation, thus enabling you to

get an earlier forecast of future transportation and resource demands

Perform tendering, subcontracting, and execution in TM based on sales and purchase orders

## Perform sales order scheduling

Propose and create deliveries based on dates and quantities according to transportation planning results, taking into

account transportation constraints such as resource availability and transportation durations.

This is custom documentation. For more information, please visit SAP Help Portal.

2


1/14/26, 2:17 PM

Perform transportation planning and execution of JIT calls.

## Features

## Order Integration

Orders that are created in SD or MM can be integrated into TM. The following types of order can be integrated into TM:

Sales order

Customer returns

Purchase order

Stock transport order

Returns purchase order

Returns stock transport order

## Scheduling Agreement Integration

Scheduling Agreements that are created in SD or MM can be integrated into TM. The following types of order can be integrated

into TM:

Sales Scheduling Agreement

Purhcase Scheduling Agreement

Stock Transport Scheduling Agreement

## JIT Call Integration

JIT calls created in nJIT can be integrated into TM. The following types of calls can be integrated into TM:

Sequenced JIT Call

Forwarded JIT Call

## Delivery Proposals

TM can generate a proposal for a delivery to be created in LE based on the order-based transportation requirement. For more

information, see Creation of Deliveries from TM.

## Delivery Integration

Outbound deliveries and inbound deliveries that are created in LE can be integrated into TM, regardless of whether the delivery

creation was triggered by TM or not. Deliveries can also be integrated into TM, even if an order that relates to the delivery has not

been sent to TM.

You can also define the transportation relevance of your deliveries.

## Transportation Relevance

You can define the transportation relevance of sales, purchase, and delivery documents.

## Integration Time Range

This is custom documentation. For more information, please visit SAP Help Portal.

3


1/14/26, 2:17 PM

You can define an integration time range for purchase scheduling agreements, which includes an integration start date, to control

the creation of freight units (FU) in TM.

## Dangerous Goods

If a product contained in an order or delivery is classified as dangerous goods, TM considers this information to ensure a safe and

compliant transportation of the product. For more information, see Dangerous Goods Checks.

Transportation Management in Advanced Intercompany
## Business Processes

Transportation Management (TM) supports the business processes advanced intercompany sales and advanced intercompany

stock transfer.

TM supports these advanced intercompany business processes in the following ways:

One freight unit is created across the various business documents.

Incoterm handling is harmonized between Sales, Sourcing and Procurement, Logistics Execution and TM.

You use the Incoterm locations to build freight unit stages in TM.

TM sets the transfer of control dates and times in the Logistics Execution delivery (LE delivery), based on transportation

planning and actual events.

Freight cost allocation posting is enabled for the advanced intercompany sales process and advanced intercompany stock

transfer process. For more information, see Posting of Allocated Freight Costs in an Advanced Intercompany Business

Process.

## Prerequisites

1. To use TM as part of the advanced intercompany sales process and advanced intercompany stock transfer process, you

first need to set these processes up. For further information, see Prerequisites for Advanced Intercompany Sales and

Prerequisites for Advanced Intercompany Stock Transfer.

2. Set up your TM processes, such as making settings in the Customizing activity Define Logistics Integration Profile for SD,

MM, and LE.

## Advanced Intercompany Sales

The process for advanced intercompany sales provides functions that allow two affiliated companies to participate in a single

intercompany process.

A sales organization assigned to the selling company creates a standard sales order, ordering goods from a plant assigned to

another company code, which acts as the delivering company. To keep financial and material ledger postings in sync, a purchase

order is created in the selling company that triggers the creation of an intercompany sales order in the delivering company. The

delivering company delivers the goods to the customer. The delivering company invoices the selling company, and the selling

company invoices the customer.

A standard sales order can initiate the entire process, which is integrated into value chain monitoring. For the transfer of control of

goods between the affiliated companies and to the customer, the system uses valuated stock in transit.

## Advanced Intercompany Stock Transfer

This is custom documentation. For more information, please visit SAP Help Portal.

4


1/14/26, 2:17 PM

A purchasing organization assigned to the receiving company code creates an intercompany purchase order, ordering goods from

a plant assigned to another company code.

The plant in the delivering company code delivers the goods to the plant for which the purchasing organization ordered the goods.

Because the two companies codes balance their accounts independently and have to fulfill legal requirements, the delivering

company must bill the receiving company for the goods. This internal billing transaction is carried out by means of an

intercompany billing document, that is, an intercompany customer invoice. Based on the intercompany customer invoice, the

system automatically posts an intercompany supplier invoice.

## Incoterms and Incoterm Locations

Incoterms, short for international commercial terms, are a codification of international rules for the interpretation of the

commonly used terms in international trade. An Incoterm defines the terms of sale and the passing of risks for import and export

of merchandise. The International Chamber of Commerce publishes Incoterms, and regularly releases new versions for the set of

Incoterms allowed.

The following duties have to be differentiated in planning, cost and risk responsibility:

Planning responsibility means that the respective party (shipper, consignee) organizes the transport.

Cost responsibility means that the respective party has the obligation to pay the costs of the transport.

Risk responsibility describes the duty of taking the risk for the respective transport section.

Therefore you need to define Incoterm locations at which these responsibilities are transferred from the shipper to the consignee.

Planning and cost responsibility are both transferred at Incoterm location 1. For non-C-clauses, risk responsibility is also

transferred at Incoterm location 1. For C-clauses such as CIF, CIP, CFR and CPT, it is transferred at Incoterm location 2.

## Stage Building

Transportation stages show the stops (start/end locations) of a freight unit or a freight order. Stages indicate that certain locations

must be visited in a certain sequence, or that certain transportation activities such as loading or unloading must be performed.

TM considers Incoterms during transportation planning for the purposes of stage building. TM uses Incoterm locations to build

freight unit stages.

## Transfer of Control

The transfer of risk responsibility is known as transfer of control. In the advanced intercompany sales process, internal transfer of

control occurs when goods are delivered from the delivering company to the selling company within the same group. External

transfer of control occurs when the goods are delivered from the group to the customer.

For internal and external transfer of control, there is planned and actual transfer of control. The transfer of control dates and times

in the LE delivery are set by TM, based on transportation planning and actual events. You can find the planned and actual internal

and external transfer of control dates and times in the Shipment tab in the LE delivery. For more information, see Transfer of

Control of Goods.

## Example of an Advanced Intercompany Sales Process

This is custom documentation. For more information, please visit SAP Help Portal.

5


1/14/26, 2:17 PM

A local sales office in Germany (as part of selling company 1010) receives a purchase order from a customer and creates a sales

order. The sales order contains all relevant information for selling company 1010 to organize the transport and to deliver the sold

goods to the customer in Walldorf, Germany.

This information comprises the following:

Plant/shipping point (source location of the transport)

## Customer

Ship-to (final recipient/final destination location of the transport)

Incoterm and Incoterm location(s)

Material (goods sold)

## Material availability date and requested delivery date

In this example, the sales order contains Incoterm DDP (Delivery Duty Paid). This means that the group is responsible for

organizing the whole transportation route. In the sales order, Incoterm location 1 (in this case, the customer’s address) is relevant

for stage building in TM. The group carries the planning and cost responsibility for transporting the goods to the customer’s

address in Walldorf.

During sourcing, it is determined that the material shall be shipped from a plant in Palo Alto, California, which belongs to a

company code different from the company code of the selling company in Germany.

An additional intercompany purchase order and intercompany sales order are created. The intercompany purchase order and

intercompany sales order carry all information relevant for selling company 1010 and delivering company 1710 to (jointly) organize

the transport and to deliver the sold goods to the customer.

This information comprises the following:

Supplier (determines the delivering company)

Plant (virtual plant which is only used for stock in transit postings)

This is custom documentation. For more information, please visit SAP Help Portal.

6


1/14/26, 2:17 PM

Incoterm and Incoterm location(s)

Material (goods procured from delivering company)

## Loading date and delivery date

In this example, the Incoterm on the intercompany purchase order is CIF (Cost, Insurance and Freight), which means that

delivering company 1710 is responsible for organizing the transport section from the plant to the port of discharge in Hamburg,

Germany, while selling company 1010 is responsible for organizing the transport section from the port of discharge to the

customer in Walldorf.

In the intercompany sales order, Incoterm location 1 (here the port of discharge) is relevant for stage building in TM.

Consequently, two freight unit stages are created:

1. The first stage from the plant in Palo Alto to the port of discharge in Hamburg (Incoterm location 1 in the intercompany

sales order), performed by delivering company 1710

2. The second stage from the port of discharge in Hamburg to the customer in Walldorf (Incoterm location 1 in the sales

order), performed by selling company 1010

As the Incoterm in the intercompany sales order is CIF in this case, there is an internal transfer of control at Incoterm location 2.

This is when the goods are loaded on to the vessel in New York. At this point, the risk responsibility is transferred from delivering

company 1710 to selling company 1010. While the goods are on the vessel and until they reach the port of discharge in Hamburg,

delivering company 1710 is still responsible for planning and cost, but no longer for risk.

The port of discharge is Incoterm location 1 for the intercompany sales order, so the remaining responsibilities of delivering

company 1710 end there, and selling company 1010 takes over responsibility for planning and cost.

There is an external transfer of control when the goods are delivered to the customer at Incoterm location 1 for the sales order,

which in this case is the customer’s address in Walldorf. The responsibilities of selling company 1010 end there.

This is custom documentation. For more information, please visit SAP Help Portal.

7


1/14/26, 2:17 PM
## Related Information

Posting of Allocated Freight Costs in an Advanced Intercompany Business Process

Advanced Intercompany Sales

Advanced Intercompany Stock Transfer

Configuring Integration of Orders and Deliveries

## Use

This section describes the additional settings that you need to configure to integrate orders, scheduling agreements, deliveries,

and JIT calls.

## Prerequisites

You have run the location creation report /SAPAPO/CREATE_LOCATION.

## Activities

You must complete the activities in Customizing for Transportation Management under

## Integration

## Logistics Integration

 Internal TM Component Integration  as follows:

## Define Control Keys for Document Integration

You can define control keys that determine which documents in a document chain are to be integrated into TM. You can

define as many control keys as required, with different combinations of relevant documents. You need to specify the

integration mode: you can select the internal TM component or choose to work with an external TM system.

## Define Logistics Integration Profile

You can use the Logistics Integration Profile for SD, MM, and LE to control the integration of SD, MM, and LE documents

into TM. You can create multiple profiles and assign these to TM relevant business document types.

For more information, see Logistics Integration Profile for SD, MM, and LE.

You can use the Logistics Integration Profile for nJIT to control the integration of JIT calls into TM.

For more information, see Logistics Integration Profile for nJIT.

## Activate Integration of Sales Documents

You activate the integration of sales documents into TM by assigning a control key to a combination of the required sales

document types, sales area (sales organization, distribution channel, division), and shipping condition. The sales

documents can be sales orders, or customer returns. The control key determines whether a sales document and the

corresponding outbound delivery are to be integrated into TM.

When you create a sales document for which the integration has been activated, the system assigns the control key to the

sales document (parameter TM_CONTROL_KEY) and to all relevant documents in the document chain, for example, the

outbound delivery.

## Activate Integration of Purchasing Documents

You activate the integration of purchasing documents into TM by assigning a control key to a combination of the required

document types, purchasing order, purchasing organization, and purchasing group. The purchasing documents can be

purchasing orders, stock transport orders, returns, or scheduling agreements. The control key determines whether a

purchasing document and the corresponding inbound delivery or outbound delivery are to be integrated into TM.

This is custom documentation. For more information, please visit SAP Help Portal.

8


1/14/26, 2:17 PM

When you create a purchasing document for which the integration has been activated, the system assigns the control key

to the document (parameter TM_CONTROL_KEY) and to all relevant documents in the document chain, for example, the

inbound delivery.

## Activate Integration of Delivery Documents

You activate the integration of delivery documents into TM by assigning a control key to a combination of the relevant

shipping point, delivery types and shipping condition.

Note that you can also activate the integration of the delivery using the control key assigned to the preceding document in

the document chain, for example, a sales order or a purchase order. In this case, the delivery inherits the control key from

the preceding document and the system ignores any settings that you make in this Customizing activity. This is needed

only in cases where a delivery is to be integrated into TM but the corresponding order has not been integrated into TM.

## Determine Transport-Driven Process Relevance for Deliveries

You can define which outbound deliveries are relevant for the transport-driven process. In a transport-driven process, the

delivery is blocked for warehouse execution while transportation planning takes places. When you release the delivery for

warehouse processing, it is then unblocked, and warehouse execution can start.

For more information about the transport-driven process, see Transport-Driven Execution.

Define Rule Groups to Determine Integration Time Range of Purchase Scheduling Agreements

You can create rule groups and assign rules to rule groups. Your rule groups determine the span of the integration time

range of your purchase scheduling agreement. Integration time ranges, on the other hand, define the time span within

which freight units for purchase scheduling agreements are created.

For more information, see Integration Time Range for Purchase Scheduling Agreement.

## Assign SD/MM Text Types to TM Text Types for SO/PO

You can define which types of text entered in a Sales and Distribution (SD) or Materials Management (MM) document are

displayed on the Notes tab page of the corresponding order in Transportation Management (TM).

## Assign Logistics Execution Text Types to TM Text Types for Deliveries

You can define which types of text entered in a Logistics Execution (LE) document are displayed on the Notes tab page of

the corresponding delivery-based transportation requirement (DTR) in Transportation Management.

## Define Usage of Packaging Information

By configuring shipping planning and delivery blocks, you define how delivery blocks are handled for specific document

types in TM, specifying whether a delivery block is a planning block, an execution block or both. Blocks prevent further

planning and/or execution in TM.

Delivery Profile

## Definition

A group of user-specific settings that the system takes into account during delivery creation.

## Structure

A delivery profile enables you to make the following settings:

This is custom documentation. For more information, please visit SAP Help Portal.

9


1/14/26, 2:17 PM

You can specify that during delivery creation the system fixes the planning results for freight units, freight orders, or freight

bookings that have already been planned.

You can define how the system creates deliveries when a user triggers delivery creation in Logistics Execution (LE) for

freight units that have not been planned. You can choose to create deliveries according to:

freight unit (default)

order

order item

You can specify incompatibility settings. In the incompatibility settings, you can define attributes that prevent freight units

from being combined into one delivery, for example. For more information about incompatibilities, see Incompatibilities.

You can include or exclude freight units and freight orders that are blocked for planning or blocked for execution in the

delivery creation process.

For freight unit items belonging to the same order item, you can amalgamate into the same delivery item or create separate

delivery items.

You can indicate when packaging information is to be transferred from a freight order or consignment order to an LE

delivery:

When you create or update an LE delivery or when an LE delivery is created automatically

When you set the Warehouse Processing Status to Ready for Warehouse Processing for a freight order or

consignment order

Note that this field is only relevant in the Advanced Shipping and Receiving inbound process. For more information, see

Advanced Shipping and Receiving.

For more information about these settings, see the corresponding field help.

  Note

You define delivery profiles in the Create Delivery Profile app, which you can open from the launchpad.

## Source and Destination Location Determination

Source and destination determination refers to the technical process in logistics integration by which software logic identifies and

transmits business entities and their locations from ERP documents, such as purchase orders, to the corresponding freight units.

Specifically, these can be business partners, plants, shipping points or storage locations in ERP documents from SD, MM, LE, or

nJIT – the latter only in Advance Shipping and Receving (Adv. SR) scenarios. In some cases, you can specify a document-specific

address in the business transaction document, which is also considered in the source and destination determination.

With the details extracted from ERP documents, the determination identifies and can, if necessary, updates the corresponding

locations or creates new locations.

## Prerequisites

Optionally for stock transport orders (STO) and returns STOs, you have specified an address for your storage location in

Customizing for Enterprise Structure under  Definition

 Materials Management

 Maintain Storage Location .

Optionally, in an internal setup, you have activated Improved Location Determination in Customizing for Transportation

Management under

## Integration

## Logistics Integration

 Internal TM Component Integration

## Define Logistics

This is custom documentation. For more information, please visit SAP Help Portal.

10


1/14/26, 2:17 PM

Integration Profile for SD, MM, and LE .

## Improved Location Determination / Advanced Shipping and Receiving

The customizing setting provides improvements concerning the determination of the receiving location in non-Adv. SR scenarios.

In Advanced Shipping and Receiving (Adv. SR) scenarios, these improvements are active by default.

Stock Transport Orders, returns Stock Transport Orders, Stock Transport Scheduling Agreements

By default, the determination will select business partner addresses as destination location. But you have the option of activating

Improved Location Determination to use shipping points as destination location.

Purchase Orders, Stock Transport Orders, returns Stock Transport Orders, Purchase and Stock Transport Scheduling

## Agreements

By default, when an address for the storage location is available, a one-time location with the respective address is used as

destination location. But you have the option of activating Improved Location Determination to use shipping points as destination

location. In such cases, the item's delivery address tab in the purchase document displays the address of the storage location,

while the freight unit displays the address of the receiving point, which can differ.

## One Time Locations

You can enter new addresses in your business transaction documents. As a result, the system creates a one-time location, which is

used as source or destination in the freight unit.

Related Information

## One-Time Location

Logistics Integration Profile for SD, MM, and LE

Logistics Integration Profile for SD, MM, and LE

## Definition

A group of user-specific settings that control the integration of Sales and Distribution (SD), Materials Management (MM), and

Logistics Execution (LE) documents into Transportation Management (TM).

## Structure

You define logistics integration profiles in Customizing for Transportation Management under

Integration

  Logistics

## Integration

 Internal TM Component Integration .

When working with the internal TM component you can control the integration of documents from LE, SD, or MM using the

logistics integration profile. In the profile you can configure order-related settings and common settings, which are both order-

related and delivery-related:

## Common Settings

## Freight Unit Building Rule

Specifies the freight unit building rule that is used when freight units are automatically created for business documents.

This is custom documentation. For more information, please visit SAP Help Portal.

11


1/14/26, 2:17 PM

## Condition for Freight Unit Building Rule Determination

Specifies settings that are used when freight units are created for business documents. The corresponding condition

determines a freight unit building rule (FUB rule) based on the business document details. For more information, see

Freight Unit Building Rule.

## Automatic Freight Unit Building

Specifies whether freight unit building is performed automatically after the system saves the relevant business document

(order or delivery), or if it needs to be triggered manually in a separate step.

## Stage Building Variant

Specifies whether you use the Static or Advanced stage building variant.

Specifies whether you use the Static or Advanced stage building variant.

If you select the Static stage building variant, you can specify a stage profile and stage profile condition to determine how

the system creates stages for freight units. You can define which stage(s) will be built if the Incoterm location is used for

stage building.

If you select the Advanced stage building variant, the system considers Incoterm locations 1 and 2 when it builds the stages

for freight units. You can also choose whether to use only planning-relevant stages in stage building, or static stages as well.

## Order-Related Settings

## Plan on Requested or Confirmed Quantities

Specifies whether freight units are built based on requested or confirmed quantities.

## Feight Unit Building for Partly Complete Sales Documents

Enables the creation of freight units for complete items in a partly complete sales document.

Rule Group to Determine Time Range of Purchase Scheduling Agreements

Enables the use of time ranges that limit the creation of freight units for scheduling agreements.

## Integration Based on Actual Quantity

Allows delivery integration based on actual quantities, which are determined during the execution phase.

## Improved Location Determination

Designates the destination location based on the shipping point.

Advanced Shipping and Receiving

Advanced Shipping and Receiving(Advanced SR)

Enables compliance checks for business documents in the Advanced Shipping and Receiving process.

Logistics Integration Profile for nJIT

## Definition

A group of user-specific settings that control the integration of nJIT with TM.

This is custom documentation. For more information, please visit SAP Help Portal.

12


1/14/26, 2:17 PM
## Structure

You define logistics integration profiles in Customizing for Transportation Management under

Integration

 Logistics

## Integration

 Internal TM Component Integration .

When working with the internal TM component you can control the integration of S2P calls from nJIT using the logistics integration

profile. In the profile you can configure common settings and stage building:

## Common Settings

## Freight Unit Building Rule

Specifies the freight unit building rule that is used when freight units are automatically created for business documents.

## Condition for Freight Unit Building Rule Determination

Specifies settings that are used when freight units are created for business documents. The corresponding condition

determines a freight unit building rule (FUB rule) based on the business document details. For more information, see

Freight Unit Building Rule.

## Stage Building Variant

The system considers Incoterm locations 1 and 2 when it builds stages for freight units. You can choose whether to only use

planning-relevant stages in stage building or both planning-relevant and static stages as well.

Logistics Integration Profile for Decentralized EWM

## Definition

A group of user-specific settings that control the integration of decentralized EWM with TM.

## Structure

You define logistics integration profiles in Customizing for Transportation Management under

Integration

## Decentralized

EWM-TM Integration .

When working with the internal TM component you can control the integration of outbound delivery orders from decentralized

EWM using the logistics integration profile. In the profile you can configure common settings, stage building, and compliance

checks:

## Common Settings

## Freight Unit Building Rule

Specifies the freight unit building rule that is used when freight units are automatically created for business documents.

## Condition for Freight Unit Building Rule Determination

Specifies settings that are used when freight units are created for business documents. The corresponding condition

determines a freight unit building rule (FUB rule) based on the business document details. For more information, see

Freight Unit Building Rule.

## Stage Building Variant

This is custom documentation. For more information, please visit SAP Help Portal.

13


1/14/26, 2:17 PM

The system considers Incoterm locations 1 and 2 when it builds stages for freight units. You can choose whether to only use

planning-relevant stages in stage building or both planning-relevant and static stages as well.

## Compliance Check

Enables compliance checks for business documents in the Advanced Shipping and Receiving process.

## Related Information

Advanced SR for Decentralized EWM and TM

## Reports for Logistics Integration

This overview lists reports available in the logistics integration area of Transportation Management (TM). These reports assist with

integration and post-integration processes between TM and Sales and Distribution (SD), Materials Management (MM), Logistics

Execution (LE), and nJIT (Just-In-Time).

Along side the report names, the list contains technical names and short descriptions. For more information, see the individual

report documentation in the system.

You can access the reports through your SAP Easy Access screen under  Logistics

  Transportation Management

## Administration

 Logistics Integration .

## Reports

Activation of Purchase Scheduling Agreements Without Delivery Integration

## Technical Name: /SCMTMS/ACTIVATE_MMSAG_WO_DLV

Description: Run to activate the integration of purchase scheduling agreements without integrating the corresponding

inbound deliveries.

Activation of Documents for Transportation Management

## Technical Name: /SCMTMS/LI_ACTIVATE

Description: Run to activate the integration of business transaction documents into TM in an internal integration setup.

Adjustment of Integration of Purchase Scheduling Agreements Without Delivery Integration

## Technical Name: /SCMTMS/ADAPT_START_MM_WO_DLV

Description: Run to adjust the integration start date and reduction quantity for a purchase scheduling agreement item

without delivery integration.

Create Deliveries in ERP

## Technical Name: /SCMTMS/DLV_BATCH

Description: Run to create deliveries based on existing freight units.

Deactivation of Purchase Scheduling Agreements

## Technical Name: /SCMTMS/DEACTIVATE_MMSAG_W_DLV

This is custom documentation. For more information, please visit SAP Help Portal.

14


1/14/26, 2:17 PM

Description: Run to deactivate your purchase scheduling agreements.

Prepone End Dates for Items in Purchase Scheduling Agreement

## Technical Name: /SCMTMS/UPDATE_INT_TIMERANGE

Description: Run to verify end dates and reschedule them for an earlier date.

Reactivation of Purchase Scheduling Agreements

## Technical Name: /SCMTMS/REACTIVATE_MMSAG_W_DLV

Description: Run to reactivate the integration of purchase scheduling agreements into TM.

Setting and Fixing of Integration Time Range End Date for Purchase Scheduling Agreements

## Technical Name: /SCMTMS/FIX_INT_TIMERANGE

Description: Run to set a fixed end date for the end of the integration of purchase scheduling agreements.

Subsequent Freight Unit Building in Internal TM Component Integration

## Technical Name: /SCMTMS/SUBSEQENT_FUB_LOGINT

Description: Run to trigger the creation of freight unit in an internal TM component integration setup.

Update of Purchase Scheduling Agreements Based on TM Planning Results

## Technical Name: /SCMTMS/TM_SAG_PLANNING_SYNC

Description: Run to synchronize the transportation planning date of freight unit items with the delivery date of the

corresponding schedule line in the purchase scheduling agreement.

Integration of Orders and Deliveries in Transportation Planning

## Use

You can integrate orders and deliveries from Sales and Distribution (SD), Material Management (MM), and Logistics Execution (LE)

into Transportation Management (TM).

You can view status and block information, and document-flow information for TM-relevant SD/MM orders and TM-relevant

deliveries as follows:

Consolidated status information on header and item level displaying

life cycle status

execution status

confirmation status

tendering status

subcontracting status

invoicing status

This is custom documentation. For more information, please visit SAP Help Portal.

15


1/14/26, 2:17 PM

execution block information

planning block information

Document flow which includes

SD/MM orders

deliveries

follow-on TM documents

You can navigate into any document that you display.

## Process

The process for integrating SD/MM orders and LE deliveries with transportation planning in TM is as follows:

1. Create order (SD/MM)

An order is created in SD or MM containing items and schedule lines. When the order has been created, it is sent to the

system, which creates freight units in TM. For more information, see Integration of Orders.

2. Perform transportation planning (TM)

TM performs transportation planning based on the freight units. The planning results include pickup dates and delivery

dates, resource assignments, and routes. For more information about transportation planning see Planning.

3. Create delivery proposal (TM)

TM creates delivery proposals based on the transportation planning results, triggering the creation of deliveries in LE to

create a delivery. It is also possible to create delivery proposals based on freight units, if transportation planning has not

been performed. For more information, see Creation of Delivery Proposals.

4. Create deliveries (LE)

When LE receives the request to create a delivery, LE creates the delivery. This can be an inbound delivery or an outbound

delivery. For more information about the process of creating deliveries in Logistics based on delivery proposals from TM,

see Creation of Deliveries from TM. It is also possible to create deliveries in LE without having sent a proposal from TM. For

more information, see Integration of Deliveries.

5. Reassign freight units (TM)

TM determines the order that corresponds to the delivery order and reassigns the freight units from that order to the

delivery.

6. Execute transportation

Transportation is executed based on the planning results.

  Note

The TM document flow for a specific order or delivery can be displayed in SD, MM or LE. TM provides information about the

documents created for an order or delivery, for example, freight units, freight orders, and freight settlement documents, and

the status of the documents, for example, life cycle status and execution status. This gives the user an overview of the entire

process for an individual document and enables the user to track the status of document processing in TM from SD, MM or LE.

## Integration of Orders

This is custom documentation. For more information, please visit SAP Help Portal.

16


1/14/26, 2:17 PM
## Use

In this process, a customer bases their transportation processes on an order created in Sales and Distribution (SD) or Materials

Management (MM).

## Prerequisites

For information about setting up Transportation Management (TM) for order integration, see Configuring Integration of Orders and

Deliveries.

## Process

The process for transportation planning based on an SD/MM order is as follows:

1. Create order (SD/MM)

An order is created in SD/MM containing items and schedule lines. The item contains information regarding the material

and the requested/confirmed quantity, and the desired delivery date. The quantity of an item can be subdivided into

multiple schedule lines, which, for example, can have different delivery dates. When the order has been created, it is

integrated into TM.

2. Create freight units (TM)

Once the order is saved in LE, TM creates freight units containing items that correspond to the schedule line items of the

SD/MM order. Depending on your settings in Customizing for the logistics integration profile, TM can build freight units

automatically when the order is created and saved; can use either the requested quantities or the confirmed quantities in

an order when creating freight units; and can create freight units for complete items in a partly complete sales document.

TM only creates freight units for transportation-relevant orders.

3. Perform transportation planning (TM)

TM can consolidate FUs from multiple orders, even if the base documents in SD/MM have different order types. For

example, the transportation demands of purchase orders and sales orders can be consolidated during transportation

planning.

## Result

After transportation planning, TM can either execute transportation or trigger the creation of deliveries in LE. For more

information, see Creation of ERP Deliveries from TM.

## Related Information

Subcontracting of Purchase Order

## Integration of Stock Transport Orders

In Transportation Management (TM), a stock transport order (STO) enables the transfer of goods and materials from one plant to

another with the same company code.

In a two-step process, outbound and inbound deliveries are created, and the freight units are reassigned from the outbound to the

inbound delivery. This process affords you visibility once goods issue has been posted and goods are in transit.

This is custom documentation. For more information, please visit SAP Help Portal.

17


1/14/26, 2:17 PM
## Prerequisites

## General Prerequisites

Delivery Management (LE-SHP), Extended Warehouse Management (EWM), and TM must run on a single system.

## Other Prerequisites

You have activated the improved location determination used for stock transport orders. To do this, select the Improved

Location Determination checkbox under the Order-Related Settings section of the logistics integration profile. For more

information, see Customizing for Transportation Management under

## Integration

 Logistics Integration

## Internal TM

## Component Integration

 Define Logistics Integration Profile for SD, MM, and LE .

You have defined the control keys that determine system behavior after integration. For more information, see Customizing

for Transportation Management under

## Integration

## Logistics Integration

 Internal TM Component Integration

 Define Control Keys for Document Integration .

You have determined purchase document relevance for TM by assigning control keys to the required document types.

Optionally, you can assign a logistics integration profile. For more information, see Customizing for Transportation

Management under

## Integration

## Logistics Integration

 Internal TM Component Integration

## Define Transportation-

Relevance of Purchasing Documents .

You have defined a profile for the direct integration with Extended Warehouse Management (EWM) or an external

warehouse management system. For more information, see Customizing for Transportation Management under

## Integration

 Integration with Extended Warehouse Management

 Define EWM Integration Profile .

You have defined the shipping point in Logistics Execution. For more information, see Customizing for Transportation

Management under  Logistics Execution

## Shipping

 Basic Shipping Functions

 Shipping Point and Goods Receiving

## Point Determination

 Assign Goods Receiving Points for Inbound Deliveries .

## Use

You can execute an STO as order- or delivery-based processes. After you create an STO, the system can either create freight units

(FU) automatically or based on the outbound delivery depending on your customizing settings. Additionally, you can choose

between warehouse- and transport-driven executions.

## STOs in the Advanced Shipping and Receiving Scenario

The posting of goods issue triggers the creation of an inbound delivery and the automatic reassignment of the FUs from the

outbound to the inbound delivery.

As soon as the FU is assigned the inbound delivery as its predecessor document, the warehouse processing status is set to In

Transit. For more information about this, see Warehouse Processing Status in Statuses in Advanced Shipping and Receiving.

  Note

You must deselect the One Step checkbox for the process to occur. For more information, see Customizing for Materials

Management under  Purchasing

## Purchase Order

 Set Up Stock Transport Order

 Assign Document Type, One-Step

Procedure, Underdelivery Tolerance .

At both ends of the process, outbound and inbound, you can choose between an EWM- or LE-managed warehouses or storage

locations, or a combination of both. FUs grouped in a delivery, however, must be assigned to the same warehouse or storage

location — that is, either EWM- or LE-managed.

This is custom documentation. For more information, please visit SAP Help Portal.

18


1/14/26, 2:17 PM

For more information about the STO process in Warehouse Integration based on EWM transportation units (TU), see Stock

Transport Order Process.

## STOs in Other Scenarios

Here, there is no communication between the inbound delivery and the freight order. An inbound delivery is created but not shown

under the Document Flow tab in TM. Therefore, FUs are not reassigned to the inbound delivery.

Creation of Deliveries from TM

## Use

You use this process if you want to create a delivery proposal in Transportation Management (TM) and send the proposal to

Logistics Execution (LE) where the delivery is created. The delivery proposal is based on the results of transportation planning

such as consolidation and dates, taking into account transportation-planning-relevant information such as resource availability

and transportation durations. TM can also trigger the creation of deliveries prior to transportation planning.

## Process

The process for creating delivery proposals in TM and the subsequent creation of deliveries in LE is as follows:

1. Select input (TM)

The user can start delivery creation by using a background report or interactively. For more information, see Creation of

Delivery Proposals.

TM considers data for delivery creation from the available freight units, freight orders, and freight bookings..

2. Generate delivery proposals (TM)

Based on the chosen input, TM creates delivery proposals. A proposal consists of groups of freight units that can be

delivered together. Depending on the input method used, TM either sends the proposals automatically to LE to create

deliveries, or the user can check the proposals and then send them to LE.

If the user specified a delivery profile that requires the planning results to be fixed for planned freight units, freight orders,

or freight bookings, the system fixes the planning results during delivery proposal creation. Otherwise, the system does not

fix the planning results.

3. Create deliveries (LE)

When LE receives the request to create deliveries, LE creates the deliveries. These can be inbound or outbound deliveries.

LE might split the proposed deliveries further, for example, based on additional split criteria. However, LE does not change

the dates that were proposed by TM nor consolidate proposed deliveries.

Creation of Delivery Proposals

## Use

Transportation Management (TM) can propose inbound deliveries and outbound deliveries and, based on such proposals, trigger

the creation of deliveries in Logistics Execution (LE).

Delivery creation is possible:

This is custom documentation. For more information, please visit SAP Help Portal.

19


1/14/26, 2:17 PM

through a dialogue process based on the selection of freight units that are assigned to Sales and Distribution (SD) or

## Materials Management (MM) orders

as a batch process based on the selection of SD/MM orders

out of the transportation cockpit based on the selection of freight orders

out of the freight order UI

## Prerequisites

Freight units exist for SD/MM orders.

The order is not blocked for delivery.

A delivery is expected for the order in LE. In Customizing for TM you have specified a control key for the order that has been

configured to make deliveries TM-relevant.

If you want to use a selection profile to select the relevant input for the delivery proposal, you have defined a selection

profile (see Selection Profile).

If you want to use a delivery profile during delivery creation, you have defined a delivery profile (see Delivery Profile).

If you want to send delivery proposals to LE from the freight order UI, you have assigned a delivery profile to the relevant

freight order types. You do this in Customizing for Transportation Management under  Freight Order Management

## Freight Order

 Define Freight Order Types .

If you want to handle actual amounts that differ from the planned amount, you have to activate this functionality in the

relevant logistics integration profile. For more information see Logistics Integration Profile for SD, MM, and LE

When using the background report, a delivery proposal must not have already been made for the freight units. This includes freight

units for which a delivery failed to be created.

## Features

## Background Report

The user can create delivery proposals for order-based transportation requirements by using a background function (program

/SCMTMS/DLV_BATCH). The user can enter selection criteria or use selection profiles. In both cases, the user can also enter a

delivery profile. The system selects the documents, creates the delivery proposals, and creates the deliveries.

For more information about the background function, see Creation of Deliveries in SAP ERP.

## Interactive Delivery Creation

The user can create deliveries interactively as follows:

From the Delivery Proposal Builder app, which you can open from the launchpad..

The user specifies one or more profiles according to which the system selects and displays a list of business documents.

The user then selects the relevant documents in the list and triggers delivery proposal creation. The user can review the

delivery proposals before creating the deliveries.

From the Freight Orders - Worklist app, which you open from the launchpad.

The user selects the relevant business documents in the overview and chooses the Create Deliveries pushbutton. The

system displays a list of freight units related to the selected business documents. The user selects the relevant freight units

and triggers delivery proposal creation. The user can review the delivery proposals before creating deliveries.

This is custom documentation. For more information, please visit SAP Help Portal.

20


1/14/26, 2:17 PM

## From the Transportation Cockpit

The user triggers delivery proposal creation for specific business documents after carrying out planning in the

Transportation Cockpit. The user selects the business documents in the Transportation Cockpit and chooses the Create

Delivery Proposals pushbutton. The system automatically creates and displays the delivery proposals. The user can review

the delivery proposals before creating deliveries.

## Source of Data

TM collects data from the relevant documents as follows:

## Dates

TM uses dates from the freight order or freight booking. If no freight order or freight booking exists, then TM uses dates

from the freight units.

## Quantities

TM uses quantities from the freight units.

## Consolidation

If freight orders or freight bookings exist for the transportation requirements, TM uses only one freight order or one freight

booking for each delivery proposal. That is, only freight units that belong to the same freight order or freight booking can be

consolidated into a single delivery proposal. In this way, freight units from various orders can be consolidated into a single delivery

proposal if they belong to the same freight order or freight booking. If, however, freight units from a single order were distributed

across multiple freight orders or freight bookings, then multiple deliveries are proposed for the freight units of this one order.

If order combination is not allowed for an order, TM does not group freight units from this order together with freight units from

other orders. If freight units for such orders have been consolidated into the same freight order or freight booking during planning,

TM does not include them in the same delivery proposal, but instead creates multiple delivery proposals.

In addition, freight units can only be consolidated into the same delivery proposal if the following data is the same:

Source location

Destination location

## Incoterms

## Shipping conditions

Document type, such as purchase order or sales order

Start stop (if planning has already been done)

Destination stop (if planning has already been done)

If an order has not been planned in TM, and no freight order or freight booking exists, TM can also create delivery proposals for the

corresponding freight units. In this case, TM creates delivery proposals according to the settings in the delivery profile. For more

information about the delivery profile, see Delivery Profile.

Bill of Materials (BOMs)

Either a BOM header or BOM items can be goods-movement-relevant. If a BOM header is goods-movement relevant, TM can, if

necessary, distribute the quantity across multiple delivery proposals. If BOM items are delivery relevant, TM expects a common

delivery group for all items and does not distribute the items or their quantities across multiple delivery proposals.

## Consumption of Schedule Lines in LE

This is custom documentation. For more information, please visit SAP Help Portal.

21


1/14/26, 2:17 PM

The delivery proposal in TM takes into account that LE consumes order schedule lines in chronological order. Therefore, TM does

not propose a delivery for a schedule line before another schedule line of the same order item that has an earlier delivery date has

been used for a delivery proposal. If freight unit selection results in this situation, TM excludes the affected freight units from the

selection.

If an error occurs in LE when creating a delivery, then LE does not create deliveries that correspond to later schedule lines of the

same order item, or the delivery is created but excludes the later schedule lines of that item.

## Execution and Planning Blocks in LE

You can use the delivery profile to determine how, during delivery creation, the TM system deals with objects that are blocked for

planning or execution. You can choose either or both of the following options:

Exclude freight units or freight orders that are blocked for planning

## Exclude freight units or freight orders that are blocked for execution

The system considers freight units and freight orders to check whether they are blocked for planning or blocked for execution. If a

freight order or its assigned freight units are blocked, the system – depending on the settings you have chosen in the delivery

profile and depending on how you start delivery creation – prevents the user from creating a delivery. The system runs the check

based only on the object (freight orders, bookings, transportation units, freight units) that you have selected as the starting point

for creation of delivery proposals.

  Example

A freight unit is assigned to a pre-carriage and a main-carriage freight order. The main-carriage freight order is blocked for

execution, but the freight unit has no blocks. The delivery profile has been configured to exclude freight units or freight orders

that are blocked for execution.

If you start creation of delivery proposals with the pre-carriage freight order, the system allows creation of deliveries.

If you start creation of delivery proposals with the main-carriage freight order, which is blocked for execution, the system

prevents you from creating a delivery.

The system checks for blocks in freight orders only when you start delivery creation in a freight order context, for example, from

the freight order POWL or the freight order UI or by using a freight order selection profile in the report /SCMTMS/DLV_BATCH.

Otherwise only the blocks in freight units are considered.

## Delivery Proposals with Freight Document Hierarchies

With transportation units, TM provides a three-tier hierarchy of freight documents. This can comprise a freight order on the

highest level, transportation units on the middle level, and freight units on the lowest level. For two-tier hierarchies, the highest

level can include freight orders, freight bookings and transportation units. On the lowest level, you can have freight units and

automatically generated transportation units. In addition, automatically generated transportation units and automatically

generated freight orders can represent a one level hierarchy.

You can create delivery proposals for each of these hierarchy types. If not explicitly stated, the term freight unit can also mean

automatically generated freight order or automatically generated transportation unit, in order to represent objects on the

lowest hierarchy level. In the same way the term freight order can also mean freight booking or transportation unit in order to

represent objects on the highest hierarchy level.

## Delivery Proposals for Bulk Material

Bulk materials are fluids and materials like sand or coal, that are given in base units of measure of volume or weight. You can use

TM to deal with the differences in actual and planned quantity that occur naturally during the loading of liquid or dry bulk material.

This is custom documentation. For more information, please visit SAP Help Portal.

22


1/14/26, 2:17 PM

In the Freight Order UI you can enter the volume and/or the weight of the actual quantities that were measured during or after

loading. If these quantities differ from the planned quantities that were received from the order, the system creates a delivery

proposal with the actual quantities. Subsequently, LE creates a delivery accordingly. Differing quantities do not lead to split Freight

Units.

Integration of Deliveries

## Use

You use this process if a customer creates a delivery in Logistics Execution (LE) and integrates it into Transportation Management

(TM).

## Process

## Integration of LE Deliveries Without Integrating Order into TM

The process for a delivery that is created in LE for an order that is not relevant for TM runs as follows:

1. Create order (SD/MM)

An order is created in SD/MM, but is not relevant for TM dues to seetings in Customizing.

2. Create deliveries (LE)

Deliveries for the order are created in LE.

3. Create freight units (TM)

Since the order is not TM-relevant, TM creates new freight units for the delivery according to the freight unit building rule

specified.

4. Perform transportation planning (TM)

5. Execute transportation (TM)

Integration of Changed and Deleted Orders and Deliveries

## Use

Logistics integration supports changes to and deletion of orders in Sales and Distribution (SD) and Materials Management (MM),

and changes to, deletion, and splitting of deliveries in Logistics Execution (LE). If an order or delivery is changed the freight units

are updated accordingly in Transportation Management (TM). If an order is deleted, the corresponding freight units in TM are

deleted. If a delivery is deleted, the corresponding freight units are either reassigned to the order if the order is TM-relevant, or if

there is no preceding order, they are deleted.

## Prerequisites

You have specified whether TM deletes or cancels empty freight units. You make this setting in Customizing for Transportation

Management under  Planning

## Freight Unit

 Define Freight Unit Types .

## More Information

This is custom documentation. For more information, please visit SAP Help Portal.

23


1/14/26, 2:17 PM

For more information see the following sections:

Processing Changed or Deleted Orders

Processing Changed, Deleted, or Split Deliveries

Processing Changed or Deleted Orders

## Use

If a user changes the data in an order in Logistics Execution (LE), (for example, quantities, dates and locations can be changed),

Transportation Management (TM) creates the required freight units.

If an order is deleted in LE, TM deletes the corresponding freight units.

## Process

## Update of an Order

The process when an order is changed is as follow:

1. Change order (Sales and Distribution (SD) / Materials Management (MM)

Changes are made to an order in SD/MM.

2. Adapt freight units (TM)

TM updates the freight units according to the assigned freight unit building rule. If the order quantity has been increased

and a delivery has already been created, TM creates new freight units to cover the resulting open quantity of the order.

## Deletion of an Order

The process when an order is deleted runs as follows:

1. Delete order (Sales and Distribution (SD) / Materials Management (MM)

SD/MM triggers the deletion of the freight units in TM. Note that if a delivery has already been created in Logistics

Execution (LE), the order cannot be deleted in SD/MM.

2. Adapt freight units (TM)

If the freight unit was only relevant for the canceled order the freight unit becomes empty. If the freight unit was assigned

to multiple orders, the quantity in the freight unit is reduced according to the canceled order.

3. Delete or cancel freight units (TM)

If the freight unit is empty, TM either deletes or cancels the freight unit according to your settings for the freight unit type.

Processing Changed, Deleted, or Split Deliveries

## Use

If a delivery is changed, split, or deleted in Logistics Execution (LE), Transportation Management (TM) adjusts the corresponding

freight units accordingly.

This is custom documentation. For more information, please visit SAP Help Portal.

24


1/14/26, 2:17 PM

Note that changes or splits can originate in LE or in Extended Warehouse Management (EWM). Changes or splits in EWM are

always integrated into TM via LE.

The following sections describe how TM handles these changes.

## Process

## Update of a Delivery

The process for updating a delivery in LE after delivery creation is as follows:

1. Update delivery (LE)

2. Adapt freight units (TM)

TM adjusts the freight units according to the changes in the delivery.

If the quantity of the delivery has changed and the delivery is assigned to freight units that were consumed from an order,

TM processes the freight units as follows:

If the quantity of the delivery has decreased, the open quantity of the corresponding order is increased accordingly.

It is necessary to reflect this in TM, so the freight units of the delivery are adapted and because the open quantity of

the order has changed, the freight units of the order are also adapted.

If the quantity of the delivery has increased, and there are still open quantities in the corresponding order, the

system reassigns the freight units from the order to cover this increased delivery quantity. The system then reduces

the open quantity of the freight units that are assigned to the order.

## Deletion of a Delivery

The process for deleting a delivery in LE after delivery creation is as follows:

1. Delete delivery (LE)

2. Reassign freight units to order (TM)

If corresponding order-related freight units exist, the freight units are reassigned to this order.

  Note

If the process runs without order integration, the freight units are adapted and, if necessary, are canceled or deleted

depending on your settings for the freight unit type.

## Split of a Delivery

For more information, see the following:

Delivery Splits Triggered by SAP ERP

Delivery Splits Triggered by Logistics Execution (LE)

## Use

You can split an outbound delivery in Logistics Execution (LE) or in Extended Warehouse Management (EWM) and trigger the

required changes in Transportation Management (TM). If EWM triggers the split, the delivery split is processed in LE.

This is custom documentation. For more information, please visit SAP Help Portal.

25


1/14/26, 2:17 PM
## Prerequisites

You have created freight units in TM based on an outbound delivery from LE.

## Process

1. Split delivery (LE)

LE splits a delivery for which TM has already created freight units. The existing delivery is changed and a new delivery is

created in LE.

2. Adapt freight units (TM)

TM deletes the freight units which represent the items / quantities which are to be split. TM then creates new freight units

and assigns these to the new delivery.

Delivery Splits and Updates in Logistics Execution Triggered by
TM

You can split an outbound delivery in Logistics Execution (LE) based on planning changes in Transportation Management (TM). You

can also update inbound deliveries and outbound deliveries from TM.

When LE receives a request for a split or update, it makes the necessary changes in outbound delivery processing and sends the

delivery data back to TM. TM can then make the required changes to the freight units.

TM can trigger the split or update of outbound deliveries only. It cannot trigger the split or update of inbound deliveries.

## Prerequisites

You have created freight units in TM based on an LE outbound delivery.

The Distribution status of the outbound delivery in LE is not set to “distributed”.

## Process

## Outbound Delivery Split

1. Perform transportation planning (TM)

You perform planning or change the existing planning of freight units that are based on an outbound delivery. When you

save the planning results, the system determines the delivery split relevance. If planning assigns freight units of a delivery

to different transports for the first or last stage those freight units are not transported together on these stages so a split is

necessary.

TM determines whether the LE delivery can still be changed by checking the delivery status. If the delivery can be changed,

TM sends the required delivery split to LE.

2. Split outbound delivery (LE)

Based on a split request received from TM, LE creates a new outbound delivery and changes the original outbound delivery

(that is, it removes the relevant items from the original delivery and creates one or more new deliveries for these items). LE

splits the delivery according to the settings in the split profile.

3. Create new delivery and update original delivery (TM)

This is custom documentation. For more information, please visit SAP Help Portal.

26


1/14/26, 2:17 PM

TM updates the freight units of the original delivery and reassigns the appropriate freight units to the new delivery.

## Outbound Delivery Update

1. Perform transportation planning (TM)

You perform planning or change the existing planning of freight units that belong to an outbound delivery. Dates are

changed during planning. Alternatively, you change the dates of the relevant freight order.

When you save the planning results or the changed freight order, TM determines that the dates in the freight order no

longer match the dates in the freight units and the original LE delivery.

TM determines whether the LE delivery can still be changed by checking the delivery status. If the delivery can be changed,

TM sends the changed dates to LE and requests the update of the outbound delivery

2. Update outbound delivery (LE)

LE updates the relevant deliveries.

3. Update Freight Units (TM)

TM updates the freight units.

Delivery Creation and Split for Package Units with Multiple
## Assignments

You can configure the system to allow a freight unit to be assigned to several package units when you create package units from a

freight order.

This means that the items of a freight unit may be spread across multiple package units and multiple freight orders. If load

planning is not finalized, this can lead to:

unnecessary delivery splits

unnecessary freight unit splits

creation of unnecessary deliveries

To avoid unnecessary splits, or creation of unnecessary deliveries, the system does not consider a freight order for delivery

creation until load planning for the freight units of that freight order is finalized. The system treats such freight units as unplanned

freight units. When load planning is finalized for all freight units of a freight order, the system considers that freight order and can

create, split, or update deliveries.

## Prerequisites

You have specified that a freight unit can be assigned to multiple packages. For more information see Customizing for

Transportation Management under  Freight Order Management

## Transportation Unit

## Define Transportation Unit Types

(Assgnmt of Pred.Docs (Assignment of Predecessor Documents) field)

## Features

When load planning for a freight order is finalized, the system identifies all required delivery splits, and then splits and updates

deliveries accordingly.

## Related Information

This is custom documentation. For more information, please visit SAP Help Portal.

27


1/14/26, 2:17 PM

Creating a Package Unit

Package Unit

## Load Planning

## Delivery Updates in TM Triggered by Logistics Execution

You can change specific fields in outbound deliveries in Delivery Management (LE-SHP) after freight units (FU) have been created

in Transportation Management (TM) and deliveries have been distributed to Extended Warehouse Management (EWM).

In embedded and decentralized scenarios, two aspects of the process influence whether the specific fields can be edited. First, you

must consider whether you are in a warehouse- or transport-driven process, and second, what the execution status is at that point

in time. If any fields can be edited, both the outbound delivery document and the FUs are locked to ensure no data is lost. Any

changes your make to the outbound delivery in LE are communicated to TM via Extended Warehouse Management (EWM).

You can find a comprehensive list of the changeable fields in Delivery Updates.

## Prerequisite

You have created outbound deliveries in LE.

You have defined text types in TM in Customizing for Cross-Application Components under Processes and Tools for

Enterprise Applications under  Reusable Objects and Functions for BOPF Environment

 Dependent Object Text

## Collection

 Maintain Text Schema .

You have assigned EWM text types to TM text types in Customizing for Transportation Management under

## Integration

## Logistics Integration

## Internal TM Component Integration

 Assign EWM Text Types to TM Text Types for Deliveries .

## Process

The process varies depending on whether you are in a tranportation- or warehouse-driven scenario.

1. Update Outbound Deliveries

To make changes to an outbound delivery the system first checks whether TM allows these changes.

If, for example, you want to update textual information, you can do so at any point in time regardless of the execution status

or scenario. If, however, you would like to change the shipping type, the system will allow it as long as the execution status is

not yet set to Ready for Warehouse Execution in a transport-driven scenario. In a warehouse-driven scenario, the same is

true if the status is In Warehouse Execution and no warehouse tasks exists.

2. Update Outbound Delivery Order

EWM updates the outbound delivery orders and communicates the changes to TM.

3. Update Freight Units

TM updates the freight units.

## Goods Movement in Logistics Execution (LE) Triggered by TM

The goods issue of an outbound delivery can be triggered as soon as the execution of a freight order starts. For inbound deliveries,

goods issue can be triggered once the execution of a freight order ends.

You can use transportation-related events to control and trigger the execution of goods movements automatically.

This is custom documentation. For more information, please visit SAP Help Portal.

28


1/14/26, 2:17 PM

You can control goods issue of a freight order using transportation-related events such as:

Loading begin

Loading end

## Departure

Goods issue for an outbound delivery can only be associated with the execution of a freight order covering the first stage of the

transport.

You can control goods receipt of a freight order using transportation related events such as:

Arrival at destination

Unloading start

## Unloading end

Goods receipt for an inbound delivery can only be associated with the execution of a freight order covering the last stage of the

transport.

## Prerequisites

You have defined the transportation-related events in the freight order type. For more information see Customizing under

Transportation Management

 Freight Order Management

## Freight Order

 Define Freight Order Types .

## Integration of Scheduling Agreements

Integration between Materials Management (MM), Sales and Distribution (SD), and Transportation Management(TM) enables the

integration of purchase, sales, and stock transfer scheduling agreements.

## Features

Integration enables the planning and execution of scheduling agreement schedule lines, which contain the required quantities and

delivery dates. You can perform the following operations:

## Forecasts

Just in Time (JIT)

Just in Sequence (JIS)

## Planning Delivery

In addition to new scheduling agreements, you can also integrate existing scheduling agreements with TM. Deliveries are created

for requirements in a schedule line that lie outside the scheduling horizons. The system automatically calculates and updates the

open quantity.

## Related Information

Integration of Purchase Scheduling Agreements

Integration of Sales Scheduling Agreements

## Integration of Stock Transport Scheduling Agreements

This is custom documentation. For more information, please visit SAP Help Portal.

29


1/14/26, 2:17 PM

## Integration of Purchase Scheduling Agreements

A scheduling agreement is an outline agreement containing delivery quantities and dates within a specified time period. These are

then entered as schedule lines in a delivery schedule.

You can integrate purchase scheduling agreements from Materials Management (MM) with Transportation Management (TM). The

integration is based on delivery schedules.

The integration can be triggered by the creation or change of schedule lines.

With the Advanced Shipping and Receiving process, you can have enhanced integration between Transportation Management

(TM) and Extended Warehouse Management (EWM). For more information see Advanced Shipping and Receiving.

## Prerequisites

You have completed Customizing for integration of purchase scheduling agreements. For more information, see Customizing for

Transportation Management under

## Integration

## Logistics Integration

 Internal TM Component Integration

## Define

Transportation-Relevance of Purchasing Documents .

## Features

## Create or Update Schedule Lines

Use an MRP run or manual planning to create, change, or delete schedule lines of an purchase Scheduling Agreement. Once

changes to the purchase scheduling agreement are saved, TM creates, changes or deletes freight units according to the schedule

lines of the scheduling agreement items.

## Process Planning

Plan freight units on, for example, existing or newly created freight orders. The planning can be done manually or by the optimizer.

After transportation planning has finished, the planning result can, optionally, be synchronized with the materials planning using a

batch run. MM creates, updates, or deletes schedule lines based on the TM planning results. You can use the planning time fence to

restrict the updates from TM to schedule lines. Updates are only allowed within the horizon fixed by an MRP run. Update of

schedule lines based on TM planning results is possible only for freight units that are not assigned to a delivery. Once deliveries are

created for freight units, no further update to schedule lines is possible.

## Communication to Suppliers

MM creates releases, based on schedule lines then sends these releases to a supplier. This means that the information the supplier

receives is based on TM planning results, rather than on material planning results.

## Create Deliveries

MM creates or updates inbound deliveries based on an ASN received from the supplier. When a new delivery is saved, TM reassigns

freight units, which are assigned to the related scheduling agreement, from the scheduling agreement to the inbound delivery.

## Integration with JIT and nJIT

In a standard process, TM creates FUs for items in schedule lines of a scheduling agreement that is relevant for TM. However, if a

purchase scheduling agreement has Kanban indicator Z and has been assigned to a control cycle with TM relevance, TM creates

FUs based on the S2P JIT call regardless of the scheduling agreement's TM relevance.

This is custom documentation. For more information, please visit SAP Help Portal.

30


1/14/26, 2:17 PM

For a control cycle to have TM relevance, its Replenishment Strategy field must have a TM control key. A Z in the Kanban field in

the scheduling agreement indicates that the agreement is relevant for nJIT processing.

Communication between supplier and customer happens via ASNs. In the standard process, the supplier sends the buyer JIT call

number (BTD type code 3018) as internal JIT Call number in the ASN. When the internal JIT Call number is not available, the

outbound messages sends the external JIT Call number in the internal JIT Call number field.

In an nJIT-based scenario, however, only the internal, or buyer, JIT call number is used.

## Restrictions

1. Acknowledgments of internal SA releases have no influence on which data is transferred to the TM system.

2. Replenishment with summarized JIT calls is out of scope.

3. Replenishment based on outbound sequenced JIT calls is out of scope.

4. Two-level goods receipts process is supported only in the Advanced Shipping and Receiving Process for agreements that

are relevant for TM. For more information, see Advanced Shipping and Receiving.

## Integration Time Range for Purchase Scheduling Agreement

You can control the number of freight units (FU) Transportation Management (TM) creates for a purchase scheduling agreement

by setting an integration time range that controls the number of schedule lines taken into account during freight unit building.

Time ranges enable you to you limit the number of schedule lines you integrate, and thus the number of FUs the system creates.

Doing so reduces the number of FUs created which have distant delivery dates and are not immediately relevant for transportation

planning.

## Prerequisites

You have defined your rules and rule groups in Customizing for Transportation Management under

## Integration

## Logistics Integration

## Internal TM Component Integration

## Define Rule Groups to Determine Integration Time Range

of Purchase SAGs . For more information, see Setting an Integration Time Range: Rule Groups and Rules below.

You have indicated your preferred rule group for purchase scheduling agreements in Customizing for Transportation

Management under

## Integration

## Logistics Integration

 Internal TM Component Integration

## Define Logistics

Integration Profile for SD, MM, and LE .

## Concept

## Determining an Integration Time Range

Customizing enables you to set an integration time range for schedule lines. Integration time ranges are implemented through the

determination of integration start and end dates, which in turn, determine or limit the number of freight units created within this

time interval.

For every purchase agreement, the start date determination happens once when the purchase scheduling agreement is integrated

and processed for the first time.

To determine the start date, the system takes into account open quantities at the schedule line level. The system locates the

ealiest schedule line with an open quantity and uses its date as the upper limit. If you have set a safety margin, the system will

choose the earliest of the two dates.

This is custom documentation. For more information, please visit SAP Help Portal.

31


1/14/26, 2:17 PM

The start date is usually set before the current date and never in the future.

## Figure 1: How the Start Date is Determined

To determine the end date, the system considers the number of schedule lines within the Integration Time Range for Schedule

Line Count. Based on the number of schedule lines counted, the system identifies the corresponding rule and then sums the

number of days comprised by the integration time range offset and the additional offset.

End date determination runs daily.

## Figure 2: How the End Date is Determined

To establish the integration time range, first, you must customize your system so that it can determine start and end dates.

## Setting an Integration Time Range: Rule Groups and Rules

Setting up your rule groups will enable the system to determine the start and end dates. To define your rule groups you will need

the following:

An integration time range offset in calendar days

## An additional offset type

The additional offset is an number of days added to the integration time range offset as a safety measure.

You can select between Planning Time Fence and Planned Delivery Time in Days. Alternatively, you can choose not to set

an additional offset.

## A safety margin

This margin is set as the start date whenever there are no schedule lines with open quantity that predate the date

determined by the safety margin, in which case, the start date is set back to the earliest of the two dates. The safety margin

always precedes the current date.

Rule groups consist of a set of rules. And to set up your rules, you will need the following:

This is custom documentation. For more information, please visit SAP Help Portal.

32


1/14/26, 2:17 PM

A minimum number of schedule lines

The integration time range offset in days

## Correcting Customizing Errors

If there is an error in Customizing, and the end date is too far into the future, you can bring the end date forward using report

/SCMTMS/UPDATE_INT_TIMERANGE. It is recommended that you adjust the end date in Customizing before running the report.

Running the report results in the preponing of the integration time range end date.

## Example

The following is an example of start and end date determination:

## Start Date

The current date is 17 May. Your chose a safety margin of seven days so it falls on 10 May. The earliest schedule line with open

quantity is 8 May. Because the earliest schedule line with open quantity precedes the safety margin, the system chooses 8 May as

the start date.

## End Date

Let's say you have selected Planned Delivery Time in Days as Additional Offset Type. The planned delivery time for this

combination of plant and material is five days. And you have set the following rules:

Time Range for Schedule Line Count in Days

30

Rule Group 1

Additional Offset Type

Planned Delivery Time in Days

Number of Days as Safety Margin

7

Rule 1

Minimum Number of Schedule Lines 0

Integration Time Range in Days

40

Rule 2

Minimum Number of Schedule Lines

6

Integration Time Range in Days

20

Rule 3

Minimum Number of Schedule Lines

21

Integration Time Range in Days

15

The determination would proceed as follows:

1. With a time rage for schedule line count of 30 days, the schedule lines within this 30-day time range are counted. Let's

imagine this time range holds ten schedule lines.

2. Next, the relevant rule is determined. Because there are more than six schedule lines, the system selects rule 2.

This is custom documentation. For more information, please visit SAP Help Portal.

33


1/14/26, 2:17 PM

3. The integration time range offset in days for rule 2 is 20 days, and the additional offset, because of planned delivery time, is

five days.

4. Therefore, the system determines the end date is 25 days in the future from the current day.

Integration of Purchase Scheduling Agreements without Inbound
## Delivery Integration

In an order-only integration scenario, freight units are created for items in a purchase scheduling agreement without inbound

delivery integration. Since the freight units (FU) that are created for items in such purchase scheduling agreements are never

transferred to a delivery, transportation execution must rely on the order-based FUs and the purchase scheduling agreement.

Unlike in delivery-based integration, order-based FUs are never transferred to the corresponding deliveries, even when they have

been created.

To integrate existing purchase scheduling agreements based only on the order, you must consider how you wish to deal with order

quantities that have already been delivered. You can do this by deciding on a start date and setting a reduction quantity.

## Prerequisites

You have defined transportation relevance of sales documents. For more information see Customizing for Transportation

Management under

## Integration

 Logistics Integration

 Internal Component Integration

## Define Transportation

Relevance of Purchase Documents .

You have defined your rules and rule groups in Customizing for Transportation Management under

## Integration

## Logistics Integration

## Internal TM Component Integration

 Define Rule Groups to Determine Integration Time Range

of Purchase SAGs .

You have indicated your preferred rule group for purchase scheduling agreements in Customizing for Transportation

Management under

## Integration

## Logistics Integration

 Internal TM Component Integration

## Define Logistics

Integration Profile for SD, MM, and LE .

## Key Features

Report Activation of Purchase SAGs Without Delivery Integration (/SCMTMS/ACTIVATE_MMSAG_WO_DLV) enables you to

activate purchase scheduling agreements without integrating existing or future deliveries. It also enables you to indicate the

integration start date and reduction quantity.

In an order-only integration scenario, the system does not reduce open quantity based on goods receipt or existing deliveries.

However, if you decide to activate purchase scheduling agreements with existing deliveries into TM, you probably don't want to

create freight units for order quantities that have been delivered and completely processed before the activation is done. For the

remaining deliveries, you should decide whether order-based FUs should be built for the corresponding quantities in the

agreement. This is done in the following way:

While running the activation report, a start date is automatically determined. When the agreement is integrated and FUs

are built, the report doesn't build FUs for order quantities from dates before the start date. The start date usually

corresponds to the next date with order quantity for which goods receipt isn't yet booked.

It might be that there are delivered quantities on or after the start date, either with or without goods receipt booked. As the

system builds, by default, order-based FUs for all quantities after the start date you need to decide whether the system

should ignore some of the already delivered quantities. In order to do this, you can choose a reduction quantity strategy

when you integrate the purchase scheduling agreement. The reduction quantity dictates which quantities the system takes

This is custom documentation. For more information, please visit SAP Help Portal.

34


1/14/26, 2:17 PM

into account when calculating open quantity for schedule lines. The reduction quantity influences the creation of FUs upon

every integration. You can use one of the following strategies when running the report:

## Don't consider any deliveries

Consider only goods receipt quantities at or after the start date as reduction quantity

Consider all delivered quantities (goods receipt and deliveries) at or after the integration start date as reduction

quantity

Every time FUs are created for your purchase scheduling agreement the system checks whether a reduction quantity was

set during activation. From the start date on, in that order, the system substracts the reduction quantity before it builds FUs

for the remaining quantity.

Functionality regarding end date determination remains unchanged. In case your customizing allows the application of an

integration rule and its corresponding rule groups, an end date is also set during every integration which prevents the

creation of FUs for quantities beyond the end date.

Report Adjustment of Integration of Purchase SAG Without Delivery Integration (/SCMTMS/ADAPT_START_MM_WO_DLV)

enables you to adjust the integration start date and reduction quantity for a purchase scheduling agreement without delivery

integration. In the activation report, you can't change the start date and only have limited options for determining reduction

quantity. However, in this report, you can freely adjust both the start date and the reduction quantity.

## Related Information

Integration of Purchase Scheduling Agreements

Integration Time Range for Purchase Scheduling Agreement

Deactivation and Reactivation of Purchase Scheduling
## Agreement Integration

You can deactivate and reactivate the integration of purchase scheduling agreements (PSA) with integrated deliveries into

Transportation Management (TM).

## Prerequisites

PSAs must have integrated deliveries.

## Use

There are various scenarios in which you might want to deactivate or activate the transportation relevance of your document. For

instance, when you deactivate a PSA because your supplier delivers the goods by the truckload without a separate transportation

plan in TM. Or you want to transition from a PSA-based integration to an nJIT-based integration.

Note that the complete business document must be integrated. Item-specific integration is not supported.

Since existing PSAs are likely in execution and could have existing FUs, which could have already been planned, we recommend

taking the following steps to avoid having duplicated FUs:

## Establishing an Integration Time Range End Date

Before you deactivate the integration of PSAs, we recommend setting a fixed integration time range end date. The fixed end date

ensures that all freight units (FU) are created up to but not beyond the fixed time point. That includes all FUs that had not yet been

This is custom documentation. For more information, please visit SAP Help Portal.

35


1/14/26, 2:17 PM

created within the integration time range, but fall within the fixed end date. It is important to perform this step in advance to avoid

planning or delivering schedule lines beyond the fixed end date.

To set an end date, use report Setting and Fixing of Integration Time Range End Date for PSA

(/SCMTMS/FIX_INT_TIMERANGE).

## Deactivating the Integration of Purchase Scheduling Agreements

Use report Deactivation of Purchase Scheduling Agreements (/SCMTMS/DEACTIVATE_MMSAG_W_DLV) to deactivate the

integration of PSAs into TM.

If there are order-related freight units that have already been planned, the deactivation process will not be executed. Instead, the

report will generate a list of the PSAs that have planned order-based freight units which are preventing the deactivation. You can

proceed in one of the following ways:

Create deliveries for the planned FUs

## Remove the freight units from your transportation plan

Adjust the quantities on the relevant schedule lines, which leads to the deletion of the corresponding planned FUs

In the report, choose to delete all planned order-based FUs without delivery assignment when deactivating the PSA

Additionally, the report can also be used to generate a list of PSAs that have not yet been deactivated and still have active control

cycles.

This is custom documentation. For more information, please visit SAP Help Portal.

36


1/14/26, 2:17 PM

Having ended the integration and deactivated your PSAs, you can proceed with the activation of nJIT integration. For more

information about nJIT integration, see Integration of Next Generation Just-In-Time.

## Reactivating the Integration of Purchase Scheduling Agreements

Since previously deactivated PSAs are blocked for activation, they are not automatically reactivated upon integration of business

documents. First, use report Reactivation of Purchase Scheduling Agreements (/SCMTMS/REACTIVATE_MMSAG_W_DLV) to

remove the block set on deactivated PSAs. You can reactivate your PSAs as long as they are not assigned to an nJIT control cycle.

You must deactivate all PSAs used in the bill of materials (BOM) for the component group material linked to a control cycle, before

you activate the control cycle. Likewise, you must deactivate all nJIT control cycles whose BOMs include materials in the PSAs you

want to activate.

## Activities

You can call the reports from the SAP Easy Access screen under  Logistics

 Transportation Management

## Administration

 Logistics Integration .

This is custom documentation. For more information, please visit SAP Help Portal.

37


1/14/26, 2:17 PM

Setting and Fixing of Integration Time Range End Date for PSA (/SCMTMS/PSA_FIX_EDT)

Deactivation of Purchase Scheduling Agreements (/SCMTMS/PSA_DEACTIVT)

Reactivation of Purchase Scheduling Agreements (/SCMTMS/PSA_REACTIVT)

## Related Information

Integration of Purchase Scheduling Agreements

Integration Time Range for Purchase Scheduling Agreement

Integration of Next Generation Just-In-Time

## Integration of Sales Scheduling Agreements

You can integrate sales scheduling agreements from Sales and Distribution (SD) with Transportation Management (TM).

Delivery quantities and dates in a scheduling agreement are entered as schedule lines in a delivery schedule. The integration is

based on delivery schedules and can be triggered by the creation or change of schedule lines.

With the Advanced Shipping and Receiving process, you can have enhanced integration between TM and Extended Warehouse

Management (EWM). For more information, see Advanced Shipping and Receiving.

## Prerequisites

You have completed Customizing for integration of sales scheduling agreements. For more information, see Customizing for

Transportation Management under

## Integration

## Logistics Integration

 Internal TM Component Integration

## Define

Transportation-Relevance of Sales Documents .

## Features

## Create or Update Schedule Lines

The customer uses an MRP run or manual planning to create, change, or delete schedule lines of a Materials Management (MM)

scheduling agreement.

Once, the customer transfers changes to the supplier, the sales scheduling agreement and schedule lines are updated. TM then

creates, changes, or deletes freight units (FU) accordingly.

## Freight Unit Building

TM builds freight units (FU) based on the relevant schedule line requirements and customizing. There are multpile ways in which

you can arrange the creation of FUs. For example, when only JIT delivery schedules are designated relevant, TM only creates FUs

for scheduled deliveries within the JIT horizon.

You set the freight unit building rules in your logistics integration profile. For more information, see Logistics Integration Profile for

SD, MM, and LE.

## Create Deliveries

You create outbound deliveries directly from the sales or freight order document. When you save a new delivery, TM reassigns

freight units from the scheduling agreement to the outbound delivery. Subsequently, data is transferred to an inbound delivery on

the customer side.

This is custom documentation. For more information, please visit SAP Help Portal.

38


1/14/26, 2:17 PM

## Integration of Orders

You can also integrate existing sales scheduling agreements into TM. Integration into TM requires the creation and assignment of a

logistics integration profile with order type, sales organization, distribution channel, and division. You can always reverse the

integration of a scheduling agreement while no deliveries have been created.

For more information, see the corresponding customizing activity under Prerequisites above.

## SACO

Transaction SACO allows you to copy schedule lines together with header and item data from an existing sales scheduling

agreement to a new sales scheduling agreement. You can use the transaction to improve performance by reducing the number of

documents referenced in the document flow.

## Related Information

Integration of Purchase Scheduling Agreements

## Integration of Stock Transport Scheduling Agreements

A stock transport scheduling agreement is an internal (or intracompany) outline agreement containing delivery quantities and

dates within a specified period. These are then entered as schedule lines in a delivery schedule.

Stock transport scheduling agreements cover internal procurement processes, such as when a production plant receives

components from another plant within the same company. The requirements of such an agreement are defined by a material

requirement planning (MRP) run.

You can use stock transport scheduling agreements in an Advanced Shipping and Receiving (Advanced SR) process. For more

information see Advanced Shipping and Receiving.

  Note

Freight units (FU) can be assigned to either an Advanced SR or other warehouse or storage location. Combining FUs

that are relevant and not relevant for Advanced SR in a single outbound order is not supported.

In a stock transport scheduling agreement scenario, TM calculates open quantities based on schedule lines. The open

quantity calculation is identical to that in external procurement.

As with stock transport orders, TM considers receiving plants and their Advanced SR relevance.

## Prerequisites

Delivery Management and TM must run on the same system.

Optionally, you have activated the improved location determination. To do this, select the Improved Location

Determination checkbox under the Order-Related Settings section.

For more information, see Customizing for Transportation Management under

## Integration

## Logistics Integration

## Internal TM Component Integration

 Define Logistics Integration Profile for SD, MM, and LE .

You have defined the control keys that determine system behavior after integration.

For more information, see Customizing for Transportation Management under

## Integration

## Logistics Integration

 Internal TM Component Integration

 Define Control Keys for Document Integration .

This is custom documentation. For more information, please visit SAP Help Portal.

39


1/14/26, 2:17 PM

You have assigned control keys to the required document types to determine whether purchase documents are relevant for

TM. Optionally, you can assign a logistics integration profile.

For more information, see Customizing for Transportation Management under

## Integration

## Logistics Integration

## Internal TM Component Integration

 Define Transportation-Relevance of Purchasing Documents .

You have defined a profile for direct integration with Extended Warehouse Management (EWM) or an external warehouse

management system.

For more information, see Customizing for Transportation Management under

## Integration

 Integration with Extended

## Warehouse Management

 Define EWM Integration Profile .

## Sample Process

The following are the possible steps in a standard process:

1. Creating a stock transport scheduling agreement

In Material Management (MM), run transaction ME37 to create a stock transport scheduling agreement.

After, run transaction ME38 and fill in the scheduling agreement’s delivery schedule. Enter schedule lines with quantity and

delivery dates.

  Note

You must have set the confirmation control key at item level for the inbound delivery to receive a confirmation of the

delivery date when the advanced shipping notification is sent. For more information, see the Prerequisites section

above.

2. Creating freight units

Step 1 triggers the automatic creation of FUs in TM. You can open your Freight Units Worklist app to check that the FUs for

the delivery schedules of the stock transport scheduling agreement have been created.

Additionally, go to the Stages tab in the FU and check the location determination for source and destination location is

correct.

3. Planning transportation

You can assign the FU to a freight order (FO) in the Transportation Cockpit or the Create Road Freight Order apps.

4. Performing carrier subcontracting

Optionally, either select a carrier or tender the FO. For more information about tendering, see Freight Tendering.

5. Changing the freight order status

In your FO, set the execution status to Ready for Transportation Execution.

6. Editing the outbound delivery

Optionally, proceed with packaging the goods.

Insert the storage location first.

Pick the outbound delivery.

7. Changing the freight order status

In your FO, report the truck's arrival, check-in, check-out and departure at and from the supplying plant accordingly.

8. Posting goods issue

This is custom documentation. For more information, please visit SAP Help Portal.

40


1/14/26, 2:17 PM

In Logistics Integration (LE), post goods issue.

The system creates the corresponding inbound delivery and reassigns the FUs automatically.

9. Managing the freight order

In the FO, check the truck in at the destination location.

If you are in the Advanced SR process, select Set Ready for Warehouse Execution to report the truck's departure from the

destination location.

10. Making changes to the schedule lines

Adjust the schedule lines by changing the delivery date or quantity or by deleting or adding schedule lines.

Check whether the FU, FO, and outbound delivery have been updated or created accordingly.

## Integration of Sales Order Scheduling

You can use Transportation Requirement Routing and Scheduling (TRS) when calculating the delivery dates of a sales order in

Sales and Distribution. The scheduling of a sales order uses the determination capabilities of BPS, which rely on Transportation

Management (TM) for duration determination and scheduling logic.

## Prerequisites

You've defined a control key and indicated your TRS profile, that is, either a transportation duration determination profile or

a requirement routing profile. For more information, see Customizing for Transportation Management under

## Integration

 Logistics Integration

 Internal Component Integration

 Define Control Key for Document Integration .

Optionally, you've defined the transportation relevance of sales documents. For more information, see the Customizing for

Transportation Management under

## Integration

 Logistics Integration

 Internal Component Integration

## Define

Transportation-Relevance of Sales Documents .

  Note

Sales order scheduling only supports sales orders of the following sales document categories:

## Order

## Order Without Charge

You can use the scheduling capabilities of TM without having integrated your sales document.

For more information, see Customizing for Sales and Distribution under  Sales

 Sales Documents

 Sales Document

## Header

 Define Sales Document Types .

You've defined either a transportation duration determination profile or a requirement routing profile:

If you want to do sales order scheduling based on TM durations, you've defined a transportation duration

determination profile. In this profile, you can indicate one or several routing methods and the sequence in which the

system is to perform them. You can also indicate a planning profile if you want to use the fixed loading durations and

durations for prepare and finalize that you've defined there. To create a profile, open the Create Transportation

Duration Determination Profile app from the launchpad.

  Note

If the system determines durations using one routing method, these durations aren't changed by any

subsequent routing method that you indicated.

This is custom documentation. For more information, please visit SAP Help Portal.

41


1/14/26, 2:17 PM

Note that the system uses the default means of transport for determining the loading duration.

If you want to do sales order scheduling based on TM scheduling, you've defined a requirement routing profile. In

this profile, you can indicate one or several routing methods and the sequence in which the system is to perform

them. Further, you can define additional parameters that influence routing and scheduling. You can also indicate a

planning profile if you want to use the fixed loading durations and durations for prepare and finalize that you've

defined there. To create a profile, open the Create Requirement Routing Profile app from the launchpad.

You've activated advanced Available-To-Promise (aATP).

  Note

Activating aATP is a prerequisite for the use of the RACR screen.

For more information about the activation of aATP, see Customizing for Cross-Application Components under

Advanced Available-to-Promise (aATP)

 Define Availability Checking Groups

 Define Availability Checking Group

and Behavior

.

You've defined activities for BPS, such as loading or transport. For more information, see Customizing for Cross-

Application Components under  advanced Available-to-Promise (aATP)

 Business Process Scheduling (BPS)

## Scheduling Schema

 Define Activities for BPS .

You need to define a BPS schema. In the BPS schema, on the Attribute Determination view, you've indicated, for each of

these activities, that the duration from TM should be used. For more information, see Customizing for Transportation

Management under  Basic Functions

## General Settings

 Business Process Scheduling (BPS)

 Maintain BPS Schema

.

For more information, see Activity Attributes for Business Process Scheduling (BPS).

You've activated BPS for sales documents with TM. For more information, see Customizing for Transportation

Management under  Basic Functions

## General Settings

 Business Process Scheduling (BPS)

## Activate BPS for Sales

Documents with Transportation Management

.

  Remember

Transportation Management (TM) and Sales and Distribution (SD) must operate in a single system.

The function provides an estimate for relevant sales documents only. Relevance can be established through

Customizing.

TRS settings must match the settings of the corresponding TM control key.

Your choice of scheduling can impact system performance. Employing BPS's scheduling can result in longer runtimes.

For TM-based sales order scheduling to run, the sales order must not have any LE-TRA routes assigned.

In the Customizing activity Define Control Key for Document Integration, you define whether you use TM for

scheduling. By selecting a TRS profile, you determine whether scheduling is to be based on TM duration or based on TM

scheduling.

## Use

When a customer places an order, the system first tries to deliver on the requested date. It does this through backward scheduling,

working backward from that date to determine when the goods need to be shipped to arrive on time. However, if that delivery date

can't be met, for example, because there isn't enough stock and part of the order is on backorder, the system switches to forward

scheduling. In this case, it starts from today and calculates the earliest possible delivery date based on when the products are

available.

This is custom documentation. For more information, please visit SAP Help Portal.

42


1/14/26, 2:17 PM

You can perform scheduling in BPS or in TM.

## Sales Order Scheduling Based on TM Durations

You can use the scheduling service of BPS when creating, changing, or rescheduling sales orders in Sales and Distribution.

To schedule an order, BPS requests durations for activities from TM. Specifically, TM provides loading, transport, and

unloading durations that are determined based on the routing methods that you've selected in your transportation duration

determination profile. Scheduling takes the requested delivery date and material availability into account when estimating

the delivery date. Based on TM data, a sales order is scheduled for delivery.

For more information, see Determination of Transportation Durations for BPS-Based Scheduling.

## Sales Order Scheduling Based on TM Scheduling

BPS delegates the scheduling of the loading, transport, and unloading activities to TM. As a result, TM delivers a date and

time of delivery for each activity.

  Note

Scheduling happens for the combination of the loading, transport, and unloading activities.

Routing is performed based on the routing methods that you selected in your requirement routing profile. Based on the

routing results and a reference date, forward or backward scheduling is then performed.

For more information, see Transportation Requirement Routing and Scheduling.

## Backorder Processing

You can process backorders. You can run backorder processing to check material availability when demand or supply in the order

fulfillment process has changed, and it's necessary to check whether previously calculated confirmations for requirements in sales

orders are still feasible.

## Customizing Input Data

You can implement BAdI /SCMTMS/IF_LI_TRS_BTD_CHG (Input Data Changes for TRS Functionality) to adapt input data of

business transaction documents arriving in TM before the scheduling and routing starts.

## Business Process Scheduling

Business Process Scheduling (BPS) is a flexible configurable scheduling solution that can be used within different business

documents. BPS relies on its BPS schema to estimate delivery dates. BPS schemas model business processes from planning to

unloading. In this case, BPS resorts to TM for certain determining attributes in the calculation, namely, loading, unloading, and

transport durations.

In sales order scheduling based on TM durations, sales orders resort to BPS, which in turn calls TM for the above-mentioned

durations.

For more information about BPS, see Business Process Scheduling (BPS).

For more information about BPS Schemas, see Defining Business Processes (Schemas).

For more information about BPS determining attributes, see Determining Attributes.

For more information about the scheduling process with Available-to-Promise, see Use BPS with Available-to-Promise, Sales, Stock

Transport, and Outbound Delivery.

This is custom documentation. For more information, please visit SAP Help Portal.

43


1/14/26, 2:17 PM
## Process

1. Create a sales order (VA01)

  Note

If you're using sales order scheduling based on TM durations, press ENTER after entering the material and the related

details to run the scheduling and receive a delivery date. If you're using sales order scheduling based on TM scheduling,

you can choose Item Availability Check after selecting an item to register the entry so that the scheduling happens

when you save the document. Alternatively, choose either Document Check or Group Check to receive a delivery date.

In all cases, the system performs a group check when you save the document.

2. After scheduling, the system displays the Review Availability Check Result (RACR) screen, where you can see the

durations of the different stages.

For more information about Review Availability Check Result, see Review Availability Check Result.

3. Save your sales order. Saving triggers the creation of freight units, and the delivery date is passed on.

  Note

Changing the sales order (VA02) triggers a recalculation of the delivery date.

## Integration of Stock Transport Order Scheduling

You can use Transportation Requirement Routing and Scheduling (TRS) when calculating the delivery dates of stock transport

orders (STO) in Materials Management (MM). The scheduling of stock transport orders uses the determination capabilities of BPS,

which rely on Transportation Management (TM) for duration determination and scheduling logic.

## Prerequisites

## Prerequisites in Transportation Management

In Customizing activity Define Control Key for Document Integration, you've defined a control key and selected

transportation duration determination as your TRS profile.

For more information, see Customizing for Transportation Management under

## Integration

## Logistics Integration

 Internal TM Component Integration

 Define Control Key for Document Integration .

You've defined a transportation duration determination profile.

In this profile, you can specify one or more routing methods and the sequence in which the system processes them. You can

also assign a planning profile if you want the system to use the fixed loading durations and durations for prepare and

finalize activities defined there.

To create a profile, open the Create Transportation Duration Determination Profile app from the launchpad.

  Note

If the system determines durations using one routing method, it doesn't overwrite them with results from any later

methods defined in the sequence. The system determines the loading duration based on the default means of transport.

## Prerequisites in ATP

You've activated advanced Available-To-Promise (aATP).

This is custom documentation. For more information, please visit SAP Help Portal.

44


1/14/26, 2:17 PM

For more information about activating aATP, see Customizing forCross-Application Components under  Advanced

Available-to-Promise (aATP)

 Define Availability Checking Groups

 Define Availability Checking Group and Behavior

.

Prerequisites in Business Process Scheduling (BPS)

You've activated BPS for STO scheduling.

For more information, see Customizing for Cross-Application Components under  Advanced Available-to-Promise

(aATP)

 Business Process Scheduling (BPS)

 Activate BPS for Stock Transport Documents .

You've defined activities for BPS, such as loading or transport.

For more information, see Customizing for Cross-Application Components under  Advanced Available-to-Promise

(aATP)

 Business Process Scheduling (BPS)

## Scheduling Schema

 Define Activities for BPS .

You've defined a BPS schema.

For more information, see Customizing for Transportation Management under  Basic Functions

## General Settings

 Business Process Scheduling (BPS)

 Maintain BPS Schema .

In the Maintain BPS Schema activity, on the Attribute Determination view, you've specified that each activity uses

durations calculated by TM.

For more information about activity attributes, see Activity Attributes for Business Process Scheduling (BPS).

  Remember

TM and MM must operate in a single system.

The function provides an estimate for relevant documents only. You can establish the relevance in Customizing.

The TRS settings must match the settings of the corresponding TM control key.

The choice of scheduling can impact system performance. Using BPS scheduling can result in longer runtimes.

## Use

When you initiate a stock transfer to another storage location, the system attempts to organize the delivery for the requested

delivery date. If it can't, for example, due to missing inventory, it schedules the delivery for the next available date.

Business Process Scheduling (BPS) performs the actual scheduling. It uses TM and ATP data to determine when the stock

transport order can be delivered and sets the date in the order. If you change the stock transport order, the system recalculates

the delivery date.

## How Scheduling Works

Scheduling takes both the requested delivery date and material availability into account when determining the delivery schedule.

TM provides BPS with information about the durations of loading, transport, and unloading. To calculate the loading, transport,

and unloading durations, it uses the routing methods that you selected in the TRS profile. For more information, see Determination

of Transportation Durations for BPS-Based Scheduling.

ATP provides information about the availability of materials. For more information about the scheduling process with ATP, see Use

BPS with Available-to-Promise, Sales, Stock Transport, and Outbound Delivery.

To calculate whether it can meet the requested date, the system uses backward scheduling. During backward scheduling, the

system works backwards from the requested delivery date to determine the latest possible shipping time. It does this by

This is custom documentation. For more information, please visit SAP Help Portal.

45


1/14/26, 2:17 PM

considering how long each activity in the process takes and whether materials are available at the calculated times.

If that requested delivery date can't be met, the system uses forward scheduling. During forward scheduling, the system starts

from the current date and calculates the earliest possible delivery date based on the material availability and transportation

durations.

## Customizing Input Data

You can implement BAdI /SCMTMS/IF_LI_TRS_BTD_CHG (Input Data Changes for TRS Functionality) to adapt input data of

business transaction documents arriving in TM before the scheduling and routing starts.

## Business Process Scheduling

Business Process Scheduling (BPS) is a flexible, configurable scheduling solution used in various business documents. BPS relies

on its BPS schema to estimate delivery dates. These schemas model the process from planning through to unloading.

For more information about BPS, see Business Process Scheduling (BPS).

For more information about BPS schemas, see Defining Business Processes (Schemas).

For more information about BPS determining attributes, see Determining Attributes.

## Process

1. Create a stock transport order using Create Purchase Order (ME21N).

  Restriction

Scheduling doesn't work if you create a stock transport order in a different app or transaction.

2. Save your stock transport order.

The system sets the calculated delivery date in the order.

## Integration of Next Generation Just-In-Time

Integration between Next Generation Just-In-Time (nJIT) and Transportation Management (TM) enables the creation of freight

units (FU) based on sequenced JIT calls.

Integration with nJIT supports the execution of the inbound process in Advance Shipping and Receiving. As part of the Advanced

Shipping and Receiving process, a key difference lies in the creation of FUs, which is based on the component group materials in a

sequenced JIT call. The outbound process is conducted based on outbound deliveries from Delivery Management (LE-SHP) and

doesn't require direct integration with JIT.

  Note

All solutions must operate on a single system.

SET materials from a summarized process are supported. The next generation JIT integration scenario centers around

the integration of sequenced JIT calls. SET scenarios represent the only summarized calls supported in the integration

between JIT and TM.

For more information about nJIT processes and setup, see Next Generation Just-In-Time (JIT) Supply to Production.

This is custom documentation. For more information, please visit SAP Help Portal.

46


1/14/26, 2:17 PM
## Prerequisites

For more information, see nJIT: Prerequisites.

Features

## General

FU created out of a sequenced JIT call are built out of the call's component group material and not the individual components.

They contain JIT call reference number, receiving point, and unloading point. Updates and deletion of FUs based on changes to the

JIT call are also enabled.

Supply to Production (S2P)

Supply to Production (S2P), or inbound process, represents the procurement process for acquiring manufacturing materials. In an

S2P nJIT scenario, there is no initial package building available. Instead, packaging information and slot number are transferred

together with the advanced shipping notification (ASN).

However, it is possible to do an initial freight unit building based on component group materials. Upon receipt of the ASN in the

customer system, the system updates FUs built for S2P calls. You can make changes to or delete these FUs.

Supply to Customer (S2C)

Supply-to-customer (S2C), or the outbound process, represents the logistical process for delivering manufacturing materials to a

customer.

In an S2C scenario, the system automatically creates FUs out of the outbound delivery in Delivery Management (LE-SHP).

  Note

The outbound process is a delivery-based integration only. As such, freight unit building can't be based on the S2C call.

## Deliveries

You can trigger the creation of inbound deliveries from your consignment and freight orders.

Inbound deliveries display the package information based on the item structure. In the case of sequenced JIT, after you set the

status to Ready for Warehouse Execution, Delivery Management (LE-SHP) converts components to delivery items and transfers

them to the inbound delivery. That includes component group material and components. Additionally, deliveries contain JIT call

internal and external reference IDs, slot number, and Incoterms.

Outboud deliveries are based on the S2C call, and the FUs built on its basis are created for component group materials. The FUs

are updated whenever you make changes to the outbound delivery and include the S2C call reference number, slot number,

unloading point and delivery address from the ship-to-party business partner.

  Note

In the S2C scenario, creating deliveries via report /SCMTM/DLV_BATCH is not available.

## Forwarded JIS Call

A forwarded JIS call represents the outsourcing of component manufacturing from one supplier to another. The process runs in

the same manner as an S2P, but the communication takes place between two suppliers.

This is custom documentation. For more information, please visit SAP Help Portal.

47


1/14/26, 2:17 PM

## Advanced Shipping Notification

An advanced shipping notification (ASN) contains the component group material and JIT call number. An ASN can also be mixed. A

single ASN can contain materials at component group level and others at component level. However, ASN data must have a one-to-

one correspondence to the FU.

The receiving system relies on the internal or external JIT call number, supplier number, and unloading point to locate the

preliminary FUs and update them. The update includes packaging information and package slot numbers.

In a forwarded JIS call, call numbers diverge. The second supplier has their own internal JIT call and uses the first supplier's

forwarded JIS call number as the external number. Also, the second supplier has the original JIT call number from the customer.

Business Add-Ins (BAdI)

You can use the following BAdIs to further customize your system's behavior:

## BAdI: Change Transient TRQ Data

BAdI: Adaptation of Incoming Business Transaction Document Data in TM

## BAdI: Changing Source / Destination of Business Transaction Documents

For more information, see Customizing for Transportation Management under  Business Add-Ins for Transportation

Management

## Integration

 Logistics Integration .

Related Information

nJIT: Inbound Process

nJIT: Forwarded Inbound Process

nJIT: Creating Deliveries

nJIT: Web Services

nJIT: Prerequisites

To work with Next Generation Just-In-Time (nJIT) you must have configured your system settings.

## Logistics Integration

You have set your Transportation Management (TM) Control Key to Internal TM Component and selected the relevant

control keys. For more information, see Customizing for Transportation Management under

Integration

 Logistics

## Integration

 Internal TM Component Integration

 Define Control Keys for Document Integration .

  Tip

To activate supply to production (S2P) nJIT integration, you must have selected the S2P nJIT to TM and Inbound

Delivery to TM checkboxes. You can use standard control key 0065 or create your own control key.

If a purchase scheduling agreement has been assigned to a control cycle that is TM-relevant, freight unit (FU)

creation is suppressed for the purchase scheduling agreement. Instead, TM creates FUs based on the S2P JIT

call.

If the scheduling agreement has not been assigned to a TM-relevant control cycle but has a TM control key, the

system builds freight units based on the purchase scheduling agreement.

This is custom documentation. For more information, please visit SAP Help Portal.

48


1/14/26, 2:17 PM

To activate TM integration for an agreement with FUs already built for items in its schedule lines, the integration

time range must be adapted to end before integration with TM starts. Otherwise, FUs are built twice. Shrinking

the integration time range triggers the deletion of existing FUs that lie beyond the range. For more information

about the integration time range, see Integration Time Range for Purchase Scheduling Agreement.

  Note

For transportation-relevant nJIT calls, Materials Management (MM) integration via scheduling agreement must be

deactivated. Otherwise, this could lead to the creation of duplicate freight units.

You have configured your logistics integration profile for nJIT. For more information, see Customizing for Transportation

Management under

## Integration

## Logistics Integration

 Internal TM Component Integration

## Define Logistics

Integration Profile for nJIT .

You have defined the required actions. For more information, see Customizing for Logistics Execution under  Just-In-Time

Processing (Next Generation)

 Action Control

 Define JIT Actions .

  Note

Actions are provided, among others, to create, update, cancel, or to set a certain processing status for an nJIT call.

Actions are assigned to the respective action controls. The action controls represent the different nJIT scenarios for S2P

and S2C.

nJIT: Supply-to-Production

You have activated TM integration via the control cycle in nJIT. Fill out the Replenishment Strategy for External

Procurement and Integration Relevance fields in the respective control cycle. Assigning a TM control key will trigger TM

integration for component group materials assigned to the control cycle. TM builds freight units accordingly.

To create and modify control cycles, open the Manage JIT Control Cycles app from the launchpad.

  Tip

When creating a sequenced JIT call, select the control cycle category Sequenced and set the Action Control to

S2P_ACTRL. For a forwarded JIS call, use action control S2P_ACTFWD instead.

The system conducts an initial check to assure that the TM control key and logistics integration profile have been

configured correctly.

A Z in the Kanban field at item level in the purchase scheduling agreement indicates that the agreement is

assigned to a control cycle. The plant and storage location in the purchase scheduling agreement must match

that in the control cycle.

Attempting to remove the TM control key and logistics integration profile will raise a warning message as it would

lead to disruptions in execution. Also, we recommend creating a new replenishment strategy instead of making

changes to the Customizing activities as any changes made after integration could lead to errors.

To switch integration type from a purchase scheduling agreement-based to an nJIT-based integration with TM,

see Deactivation and Reactivation of Purchase Scheduling Agreement Integration

You have defined the required communication groups using the Manage Communication Group app. Communication

groups provide supplier and, when available, carrier information to the control cycle.

For more information about S2P configuration, see Configuration.

nJIT: Supply-to-Customer

This is custom documentation. For more information, please visit SAP Help Portal.

49


1/14/26, 2:17 PM

You have defined your supply control using the Manage JIT Customer Supply Controls app from the launchpad.

You have created packing group specifications. To create packing group specifications, open the Manage Packing Group

Specification for Sequenced JIT Calls app from the launchpad.

You have created delivery sequence groups. To do so, open the Manage Packing Group Specification for Sequenced JIT

Calls app from the launchpad. To create a delivery sequence group, you must have first defined your supply control and

created packing group specifications.

You have assigned sequenced JIT call and packing teams. To do so, open the Manage Teams and Responsibilities app from

the launchpad.

For more information about S2C, see Configuration.

  Note

Stock transport orders and intercompany processes are not available within the scope of nJIT integration.

## Related Information

Integration of Next Generation Just-In-Time

nJIT: Inbound Process

nJIT: Forwarded Inbound Process

nJIT: Creating Deliveries

nJIT: Web Services

nJIT: Inbound Process

The inbound process, also known as Supply to Production (S2P), represents the procurement process for acquiring manufacturing

materials.

## Sample Process

The following is an example of how an inbound process might develop:

1. Creating a Purchase Scheduling Agreement

Create a scheduling agreement with its corresponding confirmation control key number. Go to Additional Details and

select the item. Then go to Additional Data and insert a Z under Kanban Indicator.

  Note

Whether a purchase scheduling agreement is TM relevant or not, TM builds freight units (FU) for agreements that are

nJIT-relevant and have been assigned to a TM-relevant control cycle.

2. Creating Schedule Lines

Enter your schedule lines to be delivered within the integration time frame. In an nJIT scenario, the system doesn't create

FUs for items in schedule lines. Instead, the system creates FUs based on the component group materials in an S2P call.

This step is described below.

3. Creating an nJIT Control Cycle

Component group materials must be assigned to a control cycle before you execute the S2P process.

This is custom documentation. For more information, please visit SAP Help Portal.

50


1/14/26, 2:17 PM

If you haven't yet, open your Manage JIT Control Cycles app to create a control cycle. For a sequenced JIT call, select the

control cycle category Sequenced and set the Action Control to S2P_ACTRL. For a forwarded JIS call, use action control

S2P_ACTFWD instead.

You must fill the Replenishment Strategies and Logistics Integration Relevance fields to activate TM relevance.

4. Creating a Sequenced JIT Call

A sequenced JIT call is created based on the planned order or automatically, as soon as a planned order is generated. Open

your Manage JIS Calls and Reorder app from the launchpad to find the call.

For more information, see Next Generation Just-In-Time (JIT) Supply to Production.

5. Finding Freight Units

The creation of an S2P JIT call triggers the creation of FUs. To confirm, open your Freight Units Worklist app from the

launchpad, and enter the JIT call number into one of three search fields: JIT Call, External JIT Call, or Predecessor

Document.

Your FUs contain component group materials for a sequenced JIT call.

6. Planning Transportation

Create a freight order (FO) and insert your FUs.

Create a consignment order (CO) and insert your FO. As do FUs, COs contain the component group materials.

Alternatively, you can customize your system so that consignment orders are created and FUs updated with the receipt of

an advanced shipping notification (ASN).

7. Receiving an Advanced Shipping Notification

The supplier creates and sends an ASN, which contains such details as the corresponding JIT call number, package slot

number, and component group materials.

If you have customized your system, when the supplier sends an ASN, the system creates a consignment order.

Additionally, integration between TM and nJIT facilitates the exchange of ASN status information so when TM creates a

consignment, the status is reflected in nJIT. The internal processing status under Component changes from JIT/JIS Call

Created to Advanced Shipping Notification Received. If you delete the consignment, the system sends an update, and

nJIT reverts the status.

8. Creating Inbound Deliveries

In your FO or CO, choose  Follow-Up

 Create Delivery  to create an inbound delivery. Once created, you can find the

inbound delivery in the Document Flow.

9. Advanced Shipping and Receiving

The remaining process steps correspond to the standard Advanced Shipping and Receiving process steps. For more

information, see Advanced Shipping and Receiving.

## Related Information

Integration of Next Generation Just-In-Time

nJIT: Prerequisites

nJIT: Forwarded Inbound Process

nJIT: Creating Deliveries

nJIT: Web Services

This is custom documentation. For more information, please visit SAP Help Portal.

51


1/14/26, 2:17 PM

nJIT: Outbound Process

The outbound process, also known as supply-to-customer (S2C), represents the logistical process for delivering manufacturing

materials.

## Sample Process

The following is an example of how an outbound process might develop:

1. Creating Outbound Deliveries

In the outbound process, the outbound delivery is created based on the S2C call directly from the Manage Customer JIT

Calls by Component Groups app.

Your can start the creation by selecting all component group materials to be delivered and choosing Create Outbound

Delivery – Sequenced.

For more information about the outbound delivery, see Integration of Next Generation Just-In-Time.

2. Creating Freight Units

The system automatically creates freight units (FU) for component group materials based on the outbound delivery. The

FUs contain the S2C call number, slot number, unloading point and the ship-to-party's delivery address.

3. Planning Transportation

With FUs created, you can proceed with transportation planning. The execution can take place either as warehouse-driven

or transport-driven.

For a description of the following stages of the process, see End-to-End Process (E2E) for Advanced Shipping and Receiving

and Transport-Driven Execution.

## Related Information

Integration of Next Generation Just-In-Time

nJIT: Prerequisites

nJIT: Inbound Process

nJIT: Forwarded Inbound Process

nJIT: Creating Deliveries

nJIT: Web Services

nJIT: Forwarded Inbound Process

A forwarded JIS call is a type of inbound call based on a supply-to-customer (S2P) JIT call, where the primary supplier procures

materials from a secondary supplier.

## Sample Process

The following is an example of how a forwarded inbound process might develop:

1. Creating a Forwarded JIS Call

To create a forwarded JIS call, you must have first created a supply-to-customer (S2C) JIT call. The S2C call must have

transmitted external status Z and call type Sequenced JIT Call. The system creates the forwarded JIS call out of the S2C

This is custom documentation. For more information, please visit SAP Help Portal.

52


1/14/26, 2:17 PM

JIT call automatically.

2. Finding a Forwarded JIS Call

Open your Manage Forwarded JIS Calls app from the launchpad. The status of the call should be set to JIT/JIS Call

Created.

3. Finding Freight Units

Once the forwarded JIS call is created, TM creates freight units (FU), which you can find using your Freight Units – Worklist

app.

4. Planning Transportation

Create a freight order (FO) and insert your FUs.

Create a consignment order (CO) and insert your FO. As do FUs, COs contain the component group materials.

Alternatively, you can customize your system so that consignment orders are created and FUs updated with the receipt of

an advanced shipping notification (ASN).

5. Receiving an Advanced Shipping Notification

The supplier creates and sends an ASN, which contains such details as the corresponding JIT call number, package slot

number, and component group materials.

If you have customized your system, when the supplier sends an ASN, the system creates a CO. Additionally, integration

between TM and nJIT enables the communication of the ASN status so that when TM creates a CO, it is reflected in nJIT.

Under Component Group Material, the status changes from JIT/JIS Call Created to Advanced Shipping Notification

Received. If you delete the CO, the system sends an update, and nJIT reverts the status of the component group material.

By selecting the status, you can navigate to a detailed view of the component group material where you can also find a

detailed view of the internal processing statuses.

From here on, the process resembles the standard Advanced Shipping and Receiving process.

For more information, see Advanced Shipping and Receiving.

## Related Information

Integration of Next Generation Just-In-Time

nJIT: Prerequisites

nJIT: Inbound Process

nJIT: Creating Deliveries

nJIT: Web Services

nJIT: Creating Deliveries

nJIT integration enables you to create inbound deliveries from Transportation Management (TM) with a JIT call as predecessor

document. Inbound deliveries contain package slot number and Incoterms. It also enables you to create outbound deliveries out of

S2C calls, which leads to the automatic creation of freight units (FU) in TM.

## Prerequisites

For information about prerequisites in Delivery Management (LE-SHP), see Integration of Next Generation Just-In-Time.

This is custom documentation. For more information, please visit SAP Help Portal.

53


1/14/26, 2:17 PM
## Features

## Inbound Deliveries

You create inbound deliveries from your freight or consignment orders with component groups. Deliveries with component groups

as delivery items have JIT calls as predecessor documents, while deliveries with components as delivery items must have

scheduling agreements as predecessor document. When customized, your system creates inbound deliveries automatically after

TM has created a consignment order based on the supplier’s advanced shipping notification (ASN).

Since the deliveries reference the corresponding JIT call, LE notifies nJIT when deliveries are created for component groups and

sends goods receipt notification for component groups to nJIT. LE also replicates inbound deliveries into Extended Warehouse

Management (EWM).

You have the option to make changes to the consignment orders before the status is set to Ready for Warehouse Execution. The

system automatically updates the deliveries. Once the status is set to Ready for Warehouse Execution, this information is

communicated to both LE and EWM. The change in status also prompts the transfer of component materials as delivery items to

the inbound delivery.

Finally, when you post goods receipt in EWM, EWM sends an update to LE. For partial deliveries, LE identifies the respective

components and registers the delivered items.

You must process the movement of goods in either Inventory Management for components or EWM for component groups.

This feature is part of the Advanced Shipping and Receiving (Advanced SR) process. For more information about related features,

see Advanced Shipping and Receiving.

## Outbound Deliveries

In the supply-to-customer (S2C) process, you create your outbound deliveries out of S2C calls, and the system automatically

creates FUs based on component group materials. The FUs are updated automatically when you make changes to the deliveries.

FUs contain the S2C call reference number, slot number, unloading point, and delivery address from the ship-to-party business

partner.

## More Information

For more information about integration with Delivery Management (LE-SHP), see Integration of Next Generation Just-In-Time.

For more information about integration with Extended Warehouse Management (EWM), see Inbound Process for Supply-to-

Production.

## Related Information

Integration of Next Generation Just-In-Time

nJIT: Prerequisites

nJIT: Inbound Process

nJIT: Outbound Process

nJIT: Forwarded Inbound Process

nJIT: Web Services

nJIT: Web Services

This is custom documentation. For more information, please visit SAP Help Portal.

54


1/14/26, 2:17 PM

You can send or receive advanced shipping notifications (ASN) as a supplier or customer.

Using an ASN, a supplier notifies the customer regarding the pending arrival of goods that have been shipped or that are about to

be shipped.

In an nJIT scenario, the ASN is based on the supplier's consignment order (CO) and uses the

BusinessTransactionDocumentReference (BTDRef) node with business transaction document ID, type code, and item ID. The

standard type code for communication is 3018, which represents the internal, or customer reference, JIT call ID.

<BusinessTransactionDocumentReference>

<BusinessTransactionDocumentReference>

<ID>JITCALL</ID>
<TypeCode>3018</TypeCode>
<ItemID>10</ItemID>

</BusinessTransactionDocumentReference>

</BusinessTransactionDocumentReference>

The inbound message enables the customer system to create a CO based on the business transaction document reference and to

locate and assign the corresponding freight units (FU). To locate the FUs, the system relies on the internal JIT reference number

and JIT reference item number.

<Item>

  <ID>10</ID>

  <CategoryCode>PKG</CategoryCode>

  <Description>T11_CFTO_1</Description>

The service also includes nJIT data such as the call type (S2C or S2P) and the delivered quantity with quantity unit.

 <PiecesTransportationQuantity unitCode="EA">1000</PiecesTransportationQuantity>

Furthermore, it contains packaging information such as packaging material and slot number.

<Package>

  <TypeCode>PT00</TypeCode>

  <TrayID>SLOTNUMBER</TrayID>

    <RecipientPackagingMaterialInternalID>PACKAGINGMATERIALID</RecipientPackagingMaterialInternalID

</Package>

## Extensibility

In addition to the standard implementation, which uses BTD type code 3018, BTD type code 3020 for external JIT call numbers

can be implemented by the supplier in the ASN outbound message.

In such a case, the external JIT call number is used in the ASN inbound message when the internal number is missing. Type code

3020 doesn't require an item ID. Instead, it can resort to the external JIT reference item number, the supplier number, component

group material, and unloading point.

<Product>
  <InternalID>PRODUCTID</InternalID>
    <ProductRecipientID>CUSTOMERID</ProductRecipientID>
</Product>

<UnloadingPointLocation>
  <InternalID>UNLOADINGPOINTID</InternalID>

This is custom documentation. For more information, please visit SAP Help Portal.

55


1/14/26, 2:17 PM

</UnloadingPointLocation>

## Process

The following graphic gives you an overview of the communication and data exchanged between a manufacturer’s Transportation

Management (TM) system and a supplier's TM system. The data are exchanged by using web services based on the SOA protocol.

## Phase

Process Step

## Details

## Web Service

Description of Web Services

Transportation Planning

Step 1: Send ASN based

The CO contains the JIT

TransportationOrderGenericRequest-

on CO to customer

data. That includes the

Out

component call type,

internal number, delivery

quantity and unit,

packaging information,

package slot number, and

group materials.

Transportation Planning

Step 2: Receive CO from

## Based on the BTDRef

TransportationOrderGenericRequest-

supplier

node, TM creates or

In

updates the CO, and the

system finds the

corresponding FUs and

assigns them to the CO.

Sample XML Payload

  Sample Code

<n0:TransportationOrderGenericRequest xmlns:n0="http://sap.com/xi/SAPGlobal20/Global">
  <MessageHeader>
    <CreationDateTime>2020-05-15T18:12:13.383Z</CreationDateTime>
    <SenderBusinessSystemID>ABC_123</SenderBusinessSystemID>
    <BusinessScope>
      <TypeCode>3</TypeCode>
      <ID>ASN</ID>
    </BusinessScope>
    <TestDataIndicator>false</TestDataIndicator>
   </MessageHeader>
   <TransportationOrder actionCode="04" replicateIndicator="false" completeTransmissionIndicator
    <ID>CONSIGNMENTORDERID</ID>
    <TypeCode>42CO</TypeCode>
    <CategoryCode>TU</CategoryCode>
    <ShipperParty>
      <InternalID>T42_SP42_1</InternalID>
    </ShipperParty>
    <AdditionalParty>
      <Party>
        <InternalID>T42_SP42_1</InternalID>
      </Party>

This is custom documentation. For more information, please visit SAP Help Portal.

56


1/14/26, 2:17 PM

      <RoleCode>TM033</RoleCode>
    </AdditionalParty>
    <TransportationTerms>
      <TransportModeCode>01</TransportModeCode>
    </TransportationTerms>
    <BaseBusinessTransactionDocumentReference>
      <ID>CONSIGNMENTORDERID</ID>
      <TypeCode>3002</TypeCode>
      <VersionID>2</VersionID>
    </BaseBusinessTransactionDocumentReference>
    <Item>
      <ID>1000000</ID>
      <CategoryCode>SHP</CategoryCode>
    </Item>
    <Item>
      <ID>10</ID>
      <CategoryCode>PKG</CategoryCode>
      <Description>T42_CSTO_1</Description>
      <GrossWeightTransportationQuantity unitCode="KGM">80</GrossWeightTransportationQuantity>
      <GrossVolumeTransportationQuantity unitCode="DMQ">0.010</GrossVolumeTransportationQuantity
      <NetWeightTransportationQuantity unitCode="KGM">0.010</NetWeightTransportationQuantity>
      <PiecesTransportationQuantity unitCode="EA">1</PiecesTransportationQuantity>
      <HierarchyRelationship>
        <ParentItemID>1000000</ParentItemID>
      </HierarchyRelationship>
      <Package>
        <TypeCode>PT01</TypeCode>
        <TrayID>AB01</TrayID>
         <RecipientPackagingMaterialInternalID>T42_CSTO_1</RecipientPackagingMaterialInternalID>
      </Package>
     </Item>
     <Item>
       <ID>20</ID>
       <CategoryCode>PRD</CategoryCode>
       <Description>T42_JIT_GROUP_A</Description>
       <GrossWeightTransportationQuantity unitCode="KGM">80</GrossWeightTransportationQuantity>
       <GrossVolumeTransportationQuantity unitCode="DMQ">0.010</GrossVolumeTransportationQuantit
      <NetWeightTransportationQuantity unitCode="KGM">0.010</NetWeightTransportationQuantity>
      <PiecesTransportationQuantity unitCode="EA">1</PiecesTransportationQuantity>
      <DeliveryQuantity unitCode="EA">1</DeliveryQuantity>
      <HierarchyRelationship>
        <UnloadingPointLocation>
          <InternalID>T42_LP_ROT_L43</InternalID>
        </UnloadingPointLocation>
        <ParentItemID>10</ParentItemID>
      </HierarchyRelationship>
      <Product>
        <InternalID>T42_JIT_GROUP_A</InternalID>
        <ProductRecipientID>T42_JIT_GROUP_A</ProductRecipientID>
      </Product>
      <DeliveryTerms>
        <DeliveryPriorityCode>1</DeliveryPriorityCode>
      </DeliveryTerms>
      <Incoterms>
        <ClassificationCode>ddp</ClassificationCode>
        <TransferLocationName>berlin</TransferLocationName>
      </Incoterms>
      <TransportationTerms>
        <TransportServiceLevelCode>01</TransportServiceLevelCode>
      </TransportationTerms>
      <BusinessTransactionDocumentReference>
        <BusinessTransactionDocumentReference>
          <ID>DELIVERYID</ID>
          <TypeCode>1137</TypeCode>
          <ItemID>100002</ItemID>
        </BusinessTransactionDocumentReference>
      </BusinessTransactionDocumentReference>
      <BusinessTransactionDocumentReference>
        <BusinessTransactionDocumentReference>
          <ID>JITCALL</ID>
          <TypeCode>3018</TypeCode>
          <ItemID>10</ItemID>
        </BusinessTransactionDocumentReference>
      </BusinessTransactionDocumentReference>

This is custom documentation. For more information, please visit SAP Help Portal.

57


1/14/26, 2:17 PM

    </Item>
  </TransportationOrder>
</n0:TransportationOrderGenericRequest>

## Related Information

Integration of Next Generation Just-In-Time

nJIT: Prerequisites

nJIT: Inbound Process

nJIT: Forwarded Inbound Process

## External TM System Integration

You can integrate orders and deliveries from external source systems such as SAP ERP or an external SAP S/4HANA system. The
information that follows on external system integration functionality refers to SAP ERP but applies also to integration with an
external SAP S/4HANA system.

## Use

You use integration of SAP ERP orders and deliveries to facilitate transportation planning and execution in Transportation

Management (TM) based on orders and deliveries that are created in an SAP ERP system. The orders and deliveries are

represented by transportation requirements in TM. The integration allows you to continuously react to changes to orders and

deliveries that occur in the SAP ERP system. In particular, integration with SAP ERP enables you to:

Collectively plan transportation for all orders, across order types.

Perform transportation planning in TM based on SAP ERP orders, prior to delivery creation, thus enabling you to get an

earlier forecast of future transportation and resource demands.

Perform tendering, subcontracting, and execution in TM based on SAP ERP orders prior to delivery creation.

Propose and create deliveries based on dates and quantities according to transportation planning results, taking into

account transportation constraints such as resource availability and transportation durations.

## Integration

The TM component ERP Logistics Integration is integrated with the following TM components:

Component

Planning

Master Data

## Features

Order Integration

## Type of Integration

Transportation requirements can form the basis for transportation

planning and execution.

As a prerequisite for creating transportation requirements, the

necessary master data must have been created.

Orders that are created in SAP ERP can be transferred to TM, where they are stored as order-based transportation requirements.

The following types of order in SAP ERP are supported by integration with TM:

This is custom documentation. For more information, please visit SAP Help Portal.

58


1/14/26, 2:17 PM

Sales order

Customer returns

Purchase order

Stock transport order

Returns purchase order

Returns stock transport order

MM Scheduling agreements

## Delivery Proposals

TM can generate a proposal for a delivery to be created in SAP ERP based on the order-based transportation requirement. For

more information, see External TM System Integration.

## Delivery Integration

Outbound deliveries and inbound deliveries that are created in SAP ERP can be transferred to TM, where they are stored as

delivery-based transportation requirements. Deliveries can be transferred to TM regardless of whether the delivery creation was

triggered by TM or not. Deliveries can also be transferred to SAP TM even if an order that relates to the delivery has not been sent

to TM.

## Dangerous Goods

If a product contained in an order or delivery is classified as dangerous goods, TM considers this information to ensure a safe and

compliant transportation of the product. For more information, see Dangerous Goods Checks.

## ERP-TM Communication

Order and delivery data can be transferred between TM and SAP ERP using enterprise services.

Configuring Integration of Orders and Deliveries

## Use

This section describes the additional settings that you need to make in Transportation Management (TM) and in SAP ERP to

integrate orders and deliveries.

## Prerequisites

You have set up connections between SAP ERP and TM and configured SAP ERP for order creation and delivery creation.

You have created master data in SAP ERP and TM.

For more information about master data in TM, see

## Master Data

Master Data Replication

## Activities

This is custom documentation. For more information, please visit SAP Help Portal.

59


1/14/26, 2:17 PM

Integration of ERP Orders and Deliveries

## Settings in TM

To set up integration of orders and deliveries in TM, you must complete the following activities:

In Customizing for Transportation Management, choose

## Integration

 Logistics Integration

 External TM System

## Integration

 Order-Based Transportation Requirement

 Define Order-Based Transportation Requirement Types

In this activity the following fields are of particular relevance:

## Plan on Req/Cnf Qty

Automatic Freight Unit Building

Freight Unit Building Rule

## FU Building Rule Condition

In Customizing for Transportation Management, choose

## Integration

 Logistics Integration

 External TM System

## Integration

 Delivery-Based Transportation Requirement

## Define Delivery-Based Transportation Requirement Types

If you have specified a freight unit building rule in Customizing for an order-based transportation requirement type, you

must have defined this freight unit building rule in the Freight Unit Building Rule app which you open from the launchpad..

Define conditions for determining the corresponding order-based transportation requirement type to be used for orders.

You do this by creating a condition of type/SCMTMS/OTR_TYPE in the Create Condition app which you open from the

launchpad.

Define conditions for determining the corresponding delivery-based transportation requirement type to be used for

deliveries. You do this by creating a condition of type /SCMTMS/DTR_TYPE in the Create Condition app which you open

from the launchpad.

For more information about conditions, see Condition.

Define a delivery profile for creating deliveries in SAP ERP. You do this in the Create Delivery Profile app which you open

from the launchpad.

For more information, see Delivery Profile.

## Settings in SAP ERP

In SAP ERP, you can display available control keys for document transfer, which you need to use for the following Customizing

activities in SAP ERP. For more information about the control keys delivered by SAP, see Customizing for Integration with Other

SAP Components, under  Transportation Management

## Logistics Integration

 Define Control Keys for Document Transfer

.

You must complete the activities in Customizing for Integration with Other SAP Components under  Transportation

## Management

 Logistics Integration  as follows:

1. To integrate sales orders, customer returns, and their corresponding deliveries, in the Activate Transfer of Sales

Documents activity, assign a control key to your sales order document types. The control key that you assign should have

the SO to TM checkbox and the Outbd Del. checkbox selected.

2. To integrate purchase orders, stock transport orders, return purchase orders, return stock transport orders, and their

corresponding deliveries, in the Activate Transfer of Purchasing Documents activity, assign a control key to your

purchasing document types. The control key that you assign should have the PO to TM checkbox and the Inbd Del.

checkbox selected.

This is custom documentation. For more information, please visit SAP Help Portal.

60


1/14/26, 2:17 PM

For more information about the necessary message control settings in SAP ERP, see SAP Help Portal at http://help.sap.com/erp

 under SAP Central Component. Select an SAP enhancement package for SAP ERP 6.0. In SAP Library, choose  SAP ERP

Central Component

## Logistics

 Logistics - General (LO)

 Integration of SAP ERP with SAP Transportation Management

 Integration: Order and Delivery Processing - SAP TM

 Prerequisites for Order and Delivery Integration .

## Integration of ERP Orders Without Sending Deliveries to TM

To configure this variant of integration, in your SAP ERP system, you make settings for orders such that corresponding deliveries

are not sent to TM. You make these settings as follows in the SAP ERP system:

In Customizing for Integration with Other SAP Components, under  Transportation Management

## Logistics Integration

 Activate Transfer of Sales Documents  andActivate Transfer of Purchase Orders, assign a control key to the sales document

type and the purchasing document type respectively. The control keys that you assign should not have the delivery checkboxes

selected and should have integration mode External TM System.

## Integration of ERP Deliveries Without Sending Orders to TM

To configure this variant of integration, in your SAP ERP system, you make settings for deliveries such that the preceding order

documents are not sent toTM. You make these settings as follows in the SAP ERP system:

In Customizing for Integration with Other SAP Components, under  Transportation Management

## Logistics Integration

 Activate Transfer of Delivery Documents , assign your control key to the delivery types. The control keys that you assign should

not have the SO to TM checkbox or the PO to TM checkbox selected.

Delivery Profile

## Definition

A group of user-specific settings that the system takes into account during delivery creation.

## Structure

A delivery profile enables you to make the following settings:

You can define that during delivery creation the system fixes the planning results for freight units, freight orders, or freight

bookings that have already been planned.

You can define how the system creates deliveries when a user triggers delivery creation in ERP for freight units that have

not been planned (for example, one delivery per item in an order-based transportation requirement).

You can specify incompatibility settings. In the incompatibility settings, you can define attributes that prevent freight units

from being combined into one delivery, for example. For more information about incompatibilities, see Incompatibilities.

You can configure the delivery proposal to aggregate order items in a delivery. The system compares items in a freight unit

to see if they have the same sales order or purchase order numbers and the same item type ID.

You can exclude freight units that have been blocked for planning.

You can exclude freight units that have been blocked for execution.

For more information about these settings, see the corresponding field help.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

61


1/14/26, 2:17 PM

You define delivery profiles in the Create Delivery Profile app, which you can open from the launchpad.

Integration of ERP Orders and Deliveries in Transp. Planning

## Use

You can integrate orders and deliveries from SAP ERP with Transportation Management (TM).

## Process

The following graphic shows the standard process for integrating orders and deliveries from SAP ERP with transportation planning

in TM, and is followed by a description of the process. Variants of this process are possible, and are described in subsequent

sections.

This is custom documentation. For more information, please visit SAP Help Portal.

62


1/14/26, 2:17 PM

Integration of ERP Orders and Deliveries with SAP TM

The following abbreviations are used for message types in the above figure:

## TRSR: TransportationRequestSUITERequest

This is custom documentation. For more information, please visit SAP Help Portal.

63


1/14/26, 2:17 PM

ODBCR: Outbound Delivery Bulk Create Request

IDCR: InboundDeliveryCreateRequest

ODBC: Outbound Delivery Bulk Confirmation

IDC: InboundDeliveryConfirmation_V1

The process runs as follows:

1. Create order (SAP ERP)

An order is created in SAP ERP containing items and schedule lines. When the order has been created, SAP ERP sends the

order to TM. For more information, see Integration of ERP Orders.

2. Create order-based transportation requirement (TM)

When TM receives an order from SAP ERP, TM creates an order-based transportation requirement. For more information

about order-based transportation requirements, see Order-Based Transportation Requirement.

3. Create freight units (TM)

Before transportation planning can take place, TM builds freight units (FUs) based on the order-based transportation

requirement. TM considers items and schedule line items when creating freight units. For more information about creating

freight units, see Creation and Editing of Freight Units.

4. Perform transportation planning (TM)

TM performs transportation planning based on the freight units. The planning results include pickup dates and delivery

dates, resource assignments, and routes. For more information about transportation planning, see Planning.

5. Create delivery proposal (TM)

TM creates delivery proposals based on the transportation planning results. TM sends these proposals to SAP ERP to

create a delivery. It is also possible to create delivery proposals based on freight units, if transportation planning has not

been performed. For more information, see Creation of Delivery Proposals.

6. Create deliveries (SAP ERP)

When SAP ERP receives the request to create a delivery, SAP ERP creates the delivery. This can be an inbound delivery or

an outbound delivery. For more information about the process of creating deliveries in SAP ERP based on delivery

proposals from TM, see Creation of ERP Deliveries from TM. It is also possible to create deliveries in SAP ERP without

having sent a proposal from TM. For more information, see Integration of ERP Deliveries.

7. Log delivery confirmation (TM)

When TM receives a confirmation of the deliveries that have been created in SAP ERP, TM writes this information to the

application log. If errors occurred during delivery creation an alert is generated in TM.

8. Create delivery-based transportation requirement (TM)

When TM receives a delivery from SAP ERP, TM creates a delivery-based transportation requirement. For more information

about delivery-based transportation requirements, see Delivery-Based Transportation Requirement.

9. Consume order-based transportation requirement

When TM creates the delivery-based transportation requirement, the delivery-based transportation requirement consumes

the transportation demand of the corresponding order-based transportation requirement or requirements. That is, TM

determines the corresponding order-based transportation requirement items and reassigns the freight units to the

delivery-based transportation requirement.

For more information, see Consumption of Order-Based Transportation Requirements.

This is custom documentation. For more information, please visit SAP Help Portal.

64


1/14/26, 2:17 PM

10. Adapt transportation planning

If necessary, TM can re-plan the transportation demands of the delivery-based transportation requirement and its freight

units.

11. Execute transportation

Transportation is executed based on the planning results.

  Note

The TM document flow for a specific ERP order or delivery can be displayed in the SAP ERP system (available as of SAP

enhancement package 6 for SAP ERP 6.0 support package 4). TM provides SAP ERP with information about the documents

created for an order or delivery (for example, freight units, freight orders, and freight settlement documents) and the status of

the documents (for example, life cycle status and execution status). This gives the user an overview of the entire ERP-TM

process for an individual ERP document and enables the user to track the status of document processing in TM from the SAP

ERP system.

Integration of ERP Orders

## Use

In this process, a customer bases their transportation processes on an order created in SAP ERP.

## Prerequisites

For information about setting up SAP ERP and TM for order integration, see Configuring Integration of Orders and Deliveries.

## Process

The following figure shows the process for transportation planning based on an SAP ERP order, and is followed by a description of

the process:

This is custom documentation. For more information, please visit SAP Help Portal.

65


1/14/26, 2:17 PM

## Transportation Planning Based on SAP ERP Order

In the above figure, the abbreviation TRSR means TransportationRequestSUITERequest.

The process runs as follows:

1. Create order (SAP ERP)

An order is created in SAP ERP containing items and schedule lines. The item contains information regarding the material

and the requested quantity, for example. The quantity of an item can be subdivided into multiple schedule lines, which, for

example, can have different delivery dates. When the order has been created, SAP ERP sends the order to TM.

2. Create order-based transportation requirement (TM)

The order number and order item numbers from SAP ERP are stored as references in the order-based transportation

requirement (on header level or item level respectively). In TM, the schedule lines from the SAP ERP order are stored as

items of the type Schedule Line in the order-based transportation requirement

3. Create freight units (TM)

TM creates freight units containing items that correspond to the schedule line items of order-based transportation

requirements. Depending on your settings in Customizing for the order-based transportation requirement type, TM can

build freight units automatically when the order-based transportation requirement is created, or the user can trigger the

creation manually. TM can use either the requested quantities or the confirmed quantities in an order-based transportation

requirement when creating freight units. Which quantity is used, depends on your settings in Customizing for the order-

based transportation requirement type.

This is custom documentation. For more information, please visit SAP Help Portal.

66


1/14/26, 2:17 PM

TM only creates freight units for transportation-relevant items. For example, if an order-based transportation requirement

contains an item for a bill of material, TM creates a freight unit (or units) for either the header item only or for the

component items only. This is dependent on the Customizing settings for the material in SAP ERP that determine which

items are relevant for goods movement.

TM can consolidate the transportation demand of an order-based transportation requirement with the demand of another

order-based transportation requirement into the same freight unit. However, particular attributes can prevent TM from

consolidating order-based transportation requirements into the same freight unit, for example if order combination is not

allowed for an order-based transportation requirement. If complete delivery is specified for an order, or items belong to the

same delivery group, TM consolidates the demand into a freight unit. For more information about consolidation and

incompatibilities that are considered when creating freight units, see Freight Unit Building Rule and Incompatibilities.

4. Perform transportation planning (TM)

TM can consolidate FUs from multiple order-based transportation requirements, even if the base documents in SAP ERP

have different order types. For example, the transportation demands of purchase orders and sales orders can be

consolidated during transportation planning. Furthermore, planning can be carried out either using own resources or by

tendering and subcontracting.

## Result

After transportation planning, TM can either execute transportation or trigger the creation of deliveries in SAP ERP. For more

information, see Creation of ERP Deliveries from TM.

You can display individual overviews of order-based freight orders, order-based air freight bookings, and order-based ocean freight

bookings in the Transportation Cockpit app, which you open from the launchpad.

Order-Based Transportation Requirement

## Definition

Represents a transportation demand based on an order that was created in an SAP ERP system. The order-based transportation

requirement can be used as a basis for transportation planning.

The order-based transportation requirement corresponds to a single order in SAP ERP and cannot be edited in Transportation

Management (TM).

## Structure

The transportation requirement has the following structure:

Tabs for general data, terms and conditions, business partners, location and dates/times, notes, and administrative data.

Contains information that is relevant for all items of an order-based transportation requirement.

## Document flow

Shows a list of preceding and subsequent documents that are related to the order-based transportation requirement.

## Items

This table provides a hierarchical view of the product items, schedule lines, service items, and text items. In the order-based

transportation requirement, the product items correspond to items in the ERP order. For each item, you can display more

detailed information on a number of tab pages.

This is custom documentation. For more information, please visit SAP Help Portal.

67


1/14/26, 2:17 PM

## Statuses in the Order-Based Transportation Requirement

The following statuses are available in the order-based transportation requirement:

Lifecycle Status

Status

## New

In Planning

## Planned

In Execution

## Description

The order-based transportation requirement has been created.

No freight units have been created for the order-based

transportation requirement yet.

The order-based transportation requirement is in the planning

process and at least one freight unit has been created for the

transportation requirement.

All the freight units that are assigned to the order-based

transportation requirement have been planned.

The order-based transportation requirement is in the execution

process. At least one follow-on document (not necessarily a

freight unit) is in execution. For more information about the

execution of a transportation requirement, see the execution

status of the transportation requirement or of the follow-on

documents.

## Completed

Processing of the order-based transportation requirement has

been completed. Execution has finished.

This status is also set when the freight units that were assigned

to the order-based transportation requirement have been

consumed by a delivery-based transportation requirement.

## Canceled

The order-based transportation requirement has been

canceled.

Execution Status

## Status

## Description

## Execution Not Started

The execution of the order-based transportation requirement

In Execution

## Executed

Consumption Status

has not yet started.

The order-based transportation requirement is currently being

executed. At least one of the planning documents assigned to

the order-based transportation requirement is in the execution

process.

The execution of the order-based transportation requirement

has been completed. The execution of all planning documents

assigned to the order-based transportation requirement has

been completed.

This is custom documentation. For more information, please visit SAP Help Portal.

68


1/14/26, 2:17 PM

## Status

Not Consumed

## Description

No freight units have been consumed by a delivery-based

transportation requirement.

## Consumed Partially

Some of the freight units that were assigned to the order-based

Consumed Completely

## Blocks

transportation requirement have been consumed or partially

consumed by a delivery-based transportation requirement.

All of the freight units that were assigned to the order-based

transportation requirement have been consumed by a delivery-

based transportation requirement.

An order-based transportation requirement can contain the following blocks:

Planning block

Execution block

## Delivery block

You can configure the way in which TM responds to delivery block reasons from SAP ERP. You can specify whether the TM system

should create a planning block or an execution block or both, according to the defined SAP ERP block reason.

For more information on this see Customizing for Transportation management under

## Integration

 Logistics Integration

## External TM System Integration

 Define Blocking of Transportation Requirements

 Define Blocks Based on Delivery Block

## Credit Check

You can set up credit control for sales orders in ERP. A sales order has a credit status that reflects the outcome of the credit limit

check on that document. If the credit status of the document is not “approved”  TM receives a delivery block with blocking reason

01 (“Credit Limit”) for the document.

## Integration

The order-based transportation requirement is integrated with the following objects in TM:

## Freight unit

You can create freight units based on an order-based transportation requirement.

## Delivery-based transportation requirement

One or more delivery-based transportation requirements can consume the transportation demand of one or more order-

based transportation requirements.

Creation of ERP Deliveries from TM

## Use

You use this process if you want to create a delivery proposal in Transportation Management (TM) and send the proposal to SAP

ERP where the delivery is created. The delivery proposal is based on the results of transportation planning such as consolidation

This is custom documentation. For more information, please visit SAP Help Portal.

69


1/14/26, 2:17 PM

and dates, taking into account transportation-planning-relevant information such as resource availability and transportation

durations. TM can also trigger the creation of deliveries prior to transportation planning.

## Process

The following figure shows the process for creating delivery proposals in TM and the subsequent creation of deliveries in SAP ERP

and is followed by a description of the process:

## Creation of ERP Deliveries from SAP TM

The following abbreviations are used for message types in the above figure:

ODBCR: Outbound Delivery Bulk Create Request

## IDCR: InboundDeliveryCreateRequest

This is custom documentation. For more information, please visit SAP Help Portal.

70


1/14/26, 2:17 PM

ODBC: Outbound Delivery Bulk Confirmation

IDC: InboundDeliveryConfirmation_V1

TRSR: TransportationRequestSUITERequest

The process runs as follows:

1. Select input (TM)

The user can start delivery creation by using a background report or interactively. For more information, see Creation of

Delivery Proposals.

TM considers data for delivery creation from the order-based transportation requirements and from the assigned freight

units, freight orders, and freight bookings.

2. Generate delivery proposals (TM)

Based on the chosen input, TM creates delivery proposals. A proposal consists of groups of freight units that can be

delivered together. Depending on the input method used, TM either sends the proposals automatically to SAP ERP to

create deliveries, or the user can check the proposals and then send them to SAP ERP.

If the user specified a delivery profile that requires the planning results to be fixed for planned freight units, freight orders,

or freight bookings, the system fixes the planning results during delivery proposal creation. Otherwise, the system does not

fix the planning results.

After the delivery proposals have been created and sent to SAP ERP, the system creates an entry in the application log. The

application log entry includes the delivery proposals that were sent to SAP ERP. Furthermore, the freight units for which a

delivery proposal is sent to SAP ERP are marked with a send timestamp.

3. Create deliveries (SAP ERP)

When SAP ERP receives the request to create deliveries, SAP ERP creates the deliveries. These can be inbound or outbound

deliveries. SAP ERP might split the proposed deliveries further, for example, based on additional split criteria. However, SAP

ERP will not change the dates that were proposed by TM nor consolidate proposed deliveries. When SAP ERP creates the

deliveries, SAP ERP sends a confirmation of delivery creation to TM, and a request to create a delivery-based transportation

requirement in TM.

4. Log delivery confirmations (TM)

TM creates an entry in the application log. The application log entry includes the system messages that were created in

SAP ERP during delivery creation as well as the number and document IDs of deliveries created in SAP ERP. If an error

occurred during delivery creation in SAP ERP, then TM generates an alert.

When a confirmation is received, TM sets a confirmation timestamp in the relevant freight units. The timestamp is used to

monitor whether SAP ERP has responded.

5. Create delivery-based transportation requirements (TM)

For more information, see Integration of ERP Deliveries.

6. Consume order-based transportation requirements (TM)

For more information, see Consumption of Order-Based Transportation Requirements.

Creation of Delivery Proposals

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

71


1/14/26, 2:17 PM

Transportation Management (TM) can propose inbound deliveries and outbound deliveries and send these proposals to SAP ERP

to trigger the creation of deliveries.

## Prerequisites

An order-based transportation requirement exists.

Freight units exist for the order-based transportation requirement.

The order-based transportation requirement is not blocked for delivery.

A delivery is expected for the order in the ERP system. This can be determined, for example, by the order type or shipping

conditions.

If you want to use a selection profile to select the relevant input for the delivery proposal, you have defined a selection

profile (see Selection Profile).

If you want to use a delivery profile during delivery creation, you have defined a delivery profile (see Delivery Profile).

If you want to send delivery proposals to SAP ERP from the freight order UI, you have assigned a delivery profile to the

relevant freight order types. You do this in Customizing for Transportation Management under  Freight Order

Management

## Freight Order

 Define Freight Order Types .

If you want to handle actual amounts that differ from the planned amount, you have to activate this functionality for the

relevant OTR type in Customizing for Transportation Management under

## Integration

 Logistics Integration

## External

## TM System Integration

 Order-Based Transportation Requirement

 Define Order-Based Transportation Requirement

## Types

When using the background report, a delivery proposal must not have already been made for the freight units. This includes freight

units for which a delivery failed to be created.

## Features

## Background Report

The user can create delivery proposals for order-based transportation requirements by using a background function (using

transaction SE38 to run program /SCMTMS/DLV_BATCH). The user can enter selection criteria or use selection profiles. In both

cases, the user can also enter a delivery profile. The system selects the documents, creates the delivery proposals, and sends

them automatically to SAP ERP.

If a freight unit has previously been used for a delivery proposal, but no delivery-based transportation requirement was ultimately

created, the user cannot use the function to create a new delivery proposal for that freight unit. Instead, the user has to create the

delivery proposal interactively.

For more information about the background function, see Creation of Deliveries in SAP ERP.

## Interactive Delivery Creation

The user can create deliveries interactively as follows:

From the launchpad, using the Delivery Proposal Builder app.

The user specifies one or more profiles according to which the system selects and displays a list of business documents.

The user then selects the relevant documents in the list and triggers delivery proposal creation. The user can review the

delivery proposals before sending them to SAP ERP

From the following overviews:

This is custom documentation. For more information, please visit SAP Help Portal.

72


1/14/26, 2:17 PM

Overview of freight orders or freight bookings in the Freight Orders app, which you open from the launchpad.

Overview of order-based transportation requirements or order-based freight units in the Order-Based

Transportation Requirements app, which you open from the launchpad.

Overview of order-based freight orders or order-based freight bookings in the Transportation Cockpit app, which

you open from the launchpad.

The user selects the relevant business documents in the overview and chooses the Create Deliveries in ERP pushbutton.

The system displays a list of freight units related to the selected business documents. The user selects the relevant freight

units and triggers delivery proposal creation. The user can review the delivery proposals before sending them to SAP ERP

## From the Transportation Cockpit

The user triggers delivery proposal creation for specific business documents after carrying out planning in the

Transportation Cockpit. The user selects the business documents in the Transportation Cockpit, specifies a delivery

profile, and chooses the Create Delivery Proposals pushbutton. The system automatically creates and displays the delivery

proposals. The user can review the delivery proposals before sending them to SAP ERP.

The user can also trigger the creation and sending of delivery proposals for a specific freight order by choosing  Follow Up

## Send

Delivery Proposals to ERP  in the freight order UI. The system automatically creates the delivery proposals and sends them to

SAP ERP. In this case, the user cannot review the delivery proposals before they are sent to SAP ERP. Note that if the user

generates the delivery proposal from a freight order UI, the system creates the delivery proposals according to the delivery profile

assigned to the freight order type.

## Source of Data

TM collects data from the relevant documents as follows:

## Dates

TM uses dates from the freight order or freight booking. If the order-based transportation requirement is not planned, that

is no freight order or freight booking exists, then TM uses dates from the freight units.

## Quantities

TM uses quantities from the freight units.

## ERP document references

TM retrieves document references (such as order document number) from the order-based transportation requirement.

## Consolidation

If order-based transportation requirements have been planned, and freight orders or freight bookings exist for the transportation

requirements, TM uses only one freight order or one freight booking for each delivery proposal. That is, only freight units that

belong to the same freight order or freight booking can be consolidated into a single delivery proposal. In this way, freight units

from various order-based transportation requirements can be consolidated into a single delivery proposal if they belong to the

same freight order or freight booking. If, however, freight units from a single order-based transportation requirement were

distributed across multiple freight orders or freight bookings, then multiple deliveries are proposed for the freight units of this one

order-based transportation requirement.

If order combination is not allowed for an order-based transportation requirement, TM does not group freight units from this

transportation requirement together with freight units from other order-based transportation requirements. If freight units for

such order-based transportation requirements have been consolidated into the same freight order or freight booking during

planning, TM does not include them in the same delivery proposal, but instead creates multiple delivery proposals.

In addition, freight units can only be consolidated into the same delivery proposal if the following data is the same:

This is custom documentation. For more information, please visit SAP Help Portal.

73


1/14/26, 2:17 PM

SAP ERP system from which the order was received

Source location

Destination location

## Incoterms

## Shipping conditions

SAP ERP document type, such as purchase order or sales order

Start stop (if planning has already been done)

Destination stop (if planning has already been done)

If an order-based transportation requirement has not been planned in TM, and no freight order or freight booking exists, TM can

also create delivery proposals for the corresponding freight units. In this case, TM creates delivery proposals according to the

settings in the delivery profile. For more information about the delivery profile, see Delivery Profile.

Bill of Materials (BOMs)

Either a BOM header or BOM items can be goods-movement-relevant. If a BOM header is goods-movement relevant, TM can, if

necessary, distribute the quantity across multiple delivery proposals. If BOM items are delivery relevant, TM expects a common

delivery group for all items and does not distribute the items or their quantities across multiple delivery proposals.

## Consumption of Schedule Lines in SAP ERP

The delivery proposal in TM takes into account that SAP ERP consumes order schedule lines in chronological order. Therefore, TM

does not propose a delivery for a schedule line before another schedule line of the same order item that has an earlier delivery

date has been used for a delivery proposal. If freight unit selection results in this situation, TM excludes the affected freight units

from the selection.

If an error occurs in SAP ERP when creating a delivery, then SAP ERP does not create deliveries that correspond to later schedule

lines of the same order item, or the delivery is created but excludes the later schedule lines of that item.

## Execution and Planning Blocks in SAP ERP

You can use the delivery profile to determine how, during delivery creation, the TM system deals with objects that are blocked for

planning or execution. You can choose either or both of the following options:

Exclude freight units or freight orders that are blocked for planning

Exclude freight units or freight orders that are blocked for execution

  Note
Previously the system excluded all objects with the status “Blocked for Execution”, from delivery creation. The option to exclude

objects with the status “Blocked for Planning” was not previously available.

The system considers freight units and freight orders to check whether they are blocked for planning or blocked for execution. If a

freight order or its assigned freight units are blocked, the system – depending on the settings you have chosen in the delivery

profile and depending on how you start delivery creation – prevents the user from creating a delivery. The system runs the check

based only on the object (freight orders, bookings, transportation units, freight units) that you have selected as the starting point

for creation of delivery proposals.

  Example

This is custom documentation. For more information, please visit SAP Help Portal.

74


1/14/26, 2:17 PM

A freight unit is assigned to a pre-carriage and a main-carriage freight order. The main-carriage freight order is blocked for

execution, but the freight unit has no blocks. The delivery profile has been configured to exclude freight units or freight orders

that are blocked for execution.

If you start creation of delivery proposals with the pre-carriage freight order, the system allows creation of deliveries.

If you start creation of delivery proposals with the main-carriage freight order, which is blocked for execution, the system

prevents you from creating a delivery.

The system checks for blocks in freight orders only when you start delivery creation in a freight order context, for example, from

the freight order POWL or the freight order UI or by using a freight order selection profile in the report “Create Deliveries in ERP”.

Otherwise only the blocks in freight units are considered.

## Delivery Proposals with Freight Document Hierarchies

With transportation units, TM provides a new three-tier hierarchy of freight documents. This can comprise a freight order on the

highest level, transportation units on the middle level, and freight units on the lowest level. For two-tier hierarchies, the highest

level can include freight orders, freight bookings and transportation units. On the lowest level, you can have freight units and

automatically generated transportation units. In addition, automatically generated transportation units and automatically

generated freight orders can represent a one level hierarchy.

You can create delivery proposals for each of these hierarchy types. If not explicitly stated, the term freight unit can also mean

automatically generated freight order or automatically generated transportation unit, in order to represent objects on the

lowest hierarchy level. In the same way the term freight order can also mean freight booking or transportation unit in order to

represent objects on the highest hierarchy level.

## Delivery Proposals for Bulk Material

Bulk materials are fluids and materials like sand or coal, that are given in base units of measure of volume or weight. You can use

TM to deal with the differences in actual and planned quantity that occur naturally during the loading of liquid or dry bulk material.

In the Freight Order UI you can enter the volume and/or the weight of the actual quantities that were measured during or after

loading. If these quantities differ from the planned quantities that were received from the OTR, the system creates a delivery

proposal with the actual quantities. Subsequently, the ERP system creates a delivery accordingly. Differing quantities do not lead

to split Freight Units.

Integration of ERP Deliveries

## Use

You use this process if a customer creates a delivery in SAP ERP and sends it to Transportation Management (TM). In this process,

a delivery-based transportation requirement is created in TM based on the delivery from SAP ERP. If the corresponding order was

also sent to TM, the transportation demand of the order-based transportation requirements is consumed.

## Process

## Integration of ERP Deliveries Without Sending ERP Order to TM

The following figure shows the process flow for a delivery that is created in the SAP ERP system and sent to TM, where a

corresponding order-based transportation requirement has not been created in TM:

This is custom documentation. For more information, please visit SAP Help Portal.

75


1/14/26, 2:17 PM

Integration of ERP Deliveries Without Sending ERP Order to SAP TM

In the above figure, the abbreviation TRSR means TransportationRequestSUITERequest.

The process runs as follows:

1. Create order (SAP ERP)

An order is created in SAP ERP, but is not sent to TM.

2. Create deliveries (SAP ERP)

Deliveries for the order are created in SAP ERP. SAP ERP sends the deliveries to TM.

3. Create delivery-based transportation requirements (TM)

When TM receives the deliveries, TM creates delivery-based transportation requirements for these deliveries.

4. Create freight units (TM)

Since no corresponding order-based transportation requirements exist for the delivery-based transportation requirement,

TM creates new freight units for the delivery-based transportation requirement, according to the freight unit building rule

specified.

5. Perform transportation planning (TM)

6. Execute transportation (TM)

This is custom documentation. For more information, please visit SAP Help Portal.

76


1/14/26, 2:17 PM

## Integration of ERP Deliveries With Order Integration

The following figure shows the process flow for a delivery that is created in the SAP ERP system and sent to TM where a

corresponding order-based transportation requirement exists in TM. There are two alternative processes that can precede this

process:

An order has been sent to TM and TM has sent a delivery proposal to SAP ERP (see Creation of ERP Deliveries from TM .

An order has been sent to TM, but TM has not sent a delivery proposal to SAP ERP.

## Integration of ERP Deliveries With Order Integration

In the above figure, the abbreviation TRSR means TransportationRequestSUITERequest.

The process runs as follows:

1. Create deliveries (SAP ERP)

Deliveries are created in SAP ERP. SAP ERP sends the deliveries to TM.

This is custom documentation. For more information, please visit SAP Help Portal.

77


1/14/26, 2:17 PM

2. Create delivery-based transportation requirements (TM)

When TM receives the deliveries, TM creates delivery-based transportation requirements for these deliveries.

3. Consume order-based transportation requirements (TM)

Since one or more corresponding order-based transportation requirements exist in TM, the delivery-based transportation

requirements consume the transportation demand of the order-based transportation requirement.

For more information, see Consumption of Order-Based Transportation Requirements.

4. Adapt transportation planning (TM)

Depending on change controller setting, TM can adjust the transportation planning that had previously been performed for

the order-based transportation requirement. For more information about the change controller, see Change Controller.

5. Execute transportation planning (TM)

  Note

You can display individual overviews of delivery-based freight orders, delivery-based air freight bookings, and delivery-

based ocean freight bookings in the Transportation Cockpit app, which you open from the launchpad.

Delivery-Based Transportation Requirement

## Definition

Represents a transportation demand based on a delivery that was created in SAP ERP. The delivery-based transportation

requirement (DTR) in Transportation Management (TM) corresponds to a single delivery in SAP ERP.

## Structure

The delivery-based transportation requirement has the following structure:

Tabs for general data, terms and conditions, business partners, location and dates/times, notes, and administrative data.

Contains information that is relevant for all items of a delivery-based transportation requirement.

## Document flow

Shows a list of preceding and subsequent documents that are related to the delivery-based transportation requirement.

## Items

This table shows the product items, service items, text items, and handling units. In the delivery-based transportation

requirement, handling units can contain product items and other handling units. For each item, you can display more

detailed information on a number of tab pages.

## Statuses in the Delivery-Based Transportation Requirement

The following statuses are available in the delivery-based transportation requirement:

## Lifecycle Status

This is custom documentation. For more information, please visit SAP Help Portal.

78


1/14/26, 2:17 PM

Status

## New

In Planning

## Planned

In Execution

Completed

## Canceled

Execution Status

## Description

The delivery-based transportation requirement has been

created. No freight units have been assigned to the delivery-

based transportation requirement yet.

The delivery-based transportation requirement is in the

planning process and at least one freight unit has been created

for the transportation requirement.

All the freight units that are assigned to the delivery-based

transportation requirement have been planned.

The delivery-based transportation requirement is in the

execution process. At least one follow-on document (not

necessarily a freight unit) is in execution. For more information

about the execution of a transportation requirement, see the

execution status of the transportation requirement or of the

follow-on documents.

Processing of the delivery-based transportation requirement

has been completed. Execution has finished.

The delivery-based transportation requirement has been

canceled.

## Status

## Description

## Execution Not Started

The execution of the delivery-based transportation

In Execution

## Executed

requirement has not yet started.

The delivery-based transportation requirement is currently

being executed. At least one of the planning documents

assigned to the order-based transportation requirement is in

the execution process.

The execution of the delivery-based transportation

requirement has been completed. The execution of all planning

documents assigned to the delivery-based transportation

requirement has been completed.

## Blocks

A delivery-based transportation requirement can contain the following blocks:

Planning block

## Execution block

You can configure the way in which TM responds to delivery block or shipment planning block reasons from SAP ERP. You can

specify whether the TM system should create a planning block or an execution block or both, according to the defined SAP ERP

block reason.

For more information on this see Customizing for Transportation management under:

This is custom documentation. For more information, please visit SAP Help Portal.

79


1/14/26, 2:17 PM

·

## Integration

 Logistics Integration

 External TM System Integration

 Define Blocking of Transportation

## Requirements

 Define Blocks Based on Delivery Block

·

## Integration

 Logistics Integration

 External TM System Integration

 Define Blocking of Transportation

## Requirements

 Define Blocks  Based on ERP Shipment Planning Block

## Credit Check

You can set up credit control for deliveries in SAP ERP. An order or delivery has a credit status that reflects the outcome of the

credit limit check on that document. If the credit status of the document is not “approved”  TM receives a delivery block with

blocking reason 01 (“Credit Limit”) for the document.

## Packaging Information

During the packing process in SAP ERP, handling units can be created to reflect items such as containers, rail cars, or pallets. In TM

you can now configure the system to use the appropriate item category to create the packaging information in TM.

For more information on this see Customizing for Transportation management under

## Integration

 Logistics Integration

 External TM System Integration

 Delivery-Based Transportation Requirement

 Define Usage of ERP Packaging Information

## Integration

The delivery-based transportation requirement is integrated with the following objects in TM:

## Freight units

TM can create freight units based on a delivery-based transportation requirement, or consume existing freight units.

## Order-based transportation requirement

One or more delivery-based transportation requirements consume the transportation demand of one or more order-based

transportation requirements.

Consumption of Order-Based Transportation Requirements

## Use

When a delivery-based transportation requirement (DTR) is created in Transportation Management (TM) based on a delivery that

was created in SAP ERP, the DTR consumes the freight units assigned to the relevant order-based transportation requirements

(OTR) if the corresponding orders were sent to TM.

## Features

## Determination of Freight Units

TM uses the ERP order (base document) item number that is referenced in the DTR item to find the corresponding OTR items (the

base document number and item number is also referenced in the OTR items). In this way, the system can determine the relevant

freight units, which are assigned to these OTR items.

## Reassigning Freight Units to the Delivery-Based Transportation Requirement

TM reassigns the freight units from the OTRs to the DTRs. If multiple freight unit items are determined, TM assigns the freight unit

items to the items of the DTR in chronological order (according the dates of the schedule lines that the freight unit items

This is custom documentation. For more information, please visit SAP Help Portal.

80


1/14/26, 2:17 PM

reference). Once a freight unit is assigned to a DTR, the freight unit cannot be assigned to another DTR.

If TM does not determine any freight units, TM can build new freight units for the DTR, if automatic freight unit building is allowed

for the DTR type. This situation might occur for example, if deliveries are created in the ERP system without a preceding delivery

proposal being sent from TM.

## Splitting Freight Units

If a freight unit is to be reassigned, but not all freight unit items or quantities are relevant for the DTR, TM splits the freight unit.

One of the resulting freight units contains only the relevant freight unit items and is assigned to the DTR. The other resulting

freight unit contains the non-relevant freight unit items and is assigned to the OTR.

Furthermore, if the quantity in the DTR item is less than the quantity in the freight unit, TM also splits the relevant freight unit.

If there are other differences between the freight unit or item and the DTR, TM adapts the freight units accordingly so that the

information in the freight unit corresponds to the transportation requirement.

## Updating the Open Quantity of the Order-Based Transportation Requirement

The open quantity in an OTR represents the quantity that has not been assigned to a DTR. When freight units are reassigned to a

DTR, the open quantity of the OTR is reduced accordingly.

## Updating the Status of the Order-Based Transportation Requirement

Initially the OTR has the consumption status Not Consumed. If at least one OTR item or a part of an item has been consumed by a

DTR item, the consumption status of the OTR will change to Consumed Partially. If all items in an OTR have been consumed, the

system changes the consumption status to Consumed Completely. Once the consumption status is Consumed Completely, the

system changes the lifecycle status to Completed.

## Handling Units

The item structure of the DTR may differ from the structure in the OTR due to the handling unit information in the delivery received

from SAP ERP. If a handling unit has been created, a handling unit is added to the DTR. This handling unit item is transportation

relevant and includes the complete quantity of both the packaging and goods that are to be transported. The handling unit item

can contain one or more product items or packaging items. The freight units (or parts thereof) that are determined for the items of

this handling unit item are consolidated into one single freight unit item, which is assigned to the handling unit item.

  Note

ERP-TM integration for deliveries does not support cross-delivery handling units.

## Example

The following figure shows a simple example of how an OTR might be consumed by a DTR and is followed by an explanation:

This is custom documentation. For more information, please visit SAP Help Portal.

81


1/14/26, 2:17 PM

OTR Consumed by DTR

1. Determine freight units

The relevant freight units are determined based on the order item references that are contained in the DTR items and the

OTR items.

2. Reassign freight unit (FU 1)

The first DTR item fully consumes the freight unit (FU 1) assigned to OTR item 1.

The open quantity of OTR item 1 is reduced to 0

3. Split freight unit (FU 2)

The quantity in FU 2 is greater than the quantity in item 2 of the DTR. The DTR item consumes the necessary quantity of

the FU. Therefore, the freight unit (FU 2) is split.

4. Assign freight unit to DTR

The freight unit containing only one item with the correct quantity, is assigned to the DTR item

5. Assign freight unit to OTR

The freight unit containing the remaining quantity is assigned to OTR item 2. The open quantity of OTR item 2 is reduced to

25.

## Posting Goods Issue from TM

This is custom documentation. For more information, please visit SAP Help Portal.

82


1/14/26, 2:17 PM
## Use

With this feature you can post goods issue for SAP ERP outbound deliveries from TM.

The TM system can post a goods issue to the ERP system if all of the following conditions are met:

a transport is started

all delivery items in ERP that are relevant for picking have been picked

a plant and storage location have been assigned

the goods issue has not already been posted

  Note

You cannot cancel the goods issue from TM. If it is necessary to cancel the goods issue this has to be done manually in ERP.

## Integration

For more information about the integration of this function into overall background processing, see Background Processing

## Prerequisites

An outbound delivery has been sent from SAP ERP to TM and a delivery-based transportation requirement (DTR) has been created

in TM.

## Features

In SAP ERP, the ERP inbound service OutboundDeliveryERPChangeRequestConfirmation_In_V1 is used to post a goods

issue for an outbound delivery in ERP. In TM this service is replicated as an outbound service:

OutboundDeliveryERPChangeRequestConfirmation_Out_V1. This TM outbound service does not support the complete

functionality of the ERP inbound service but only the subset needed for goods issue posting.

## Activities

You can use transaction SE38 to run the program /SCMTMS/POST_GI_BATCH to post goods issue to SAP ERP.

The system checks the goods movement status of the delivery in the ERP system and selects only deliveries for which no goods

issue has been posted. For all such deliveries the system checks the execution status for the related DTR in the TM system. The

system triggers goods issue for all DTRs for which execution has started or completed.

Synchronization of Transportation Planning Status

## Use

This feature synchronizes the transportation planning status of a delivery in SAP ERP with the planning status of a delivery-based

transportation requirement (DTR) in TM. For every change to the planning status in TM an update is sent to SAP ERP.

## Prerequisites

This is custom documentation. For more information, please visit SAP Help Portal.

83


1/14/26, 2:17 PM

You have enabled the sending of delivery updates from TM to SAP ERP delivery for the relevant delivery split/update type of the

DTR in Customizing for Transportation Management under

## Integration

 Logistics Integration

 External TM System

## Integration

 Delivery-Based Transportation Requirement

 Define Delivery Split/Updates Types .

An outbound delivery has been sent from SAP ERP to TM and a DTR has been created in TM.

## Features

In SAP ERP, a delivery contains a transportation planning status at header level. There are four possible transportation planning

statuses:

## Not Relevant

The delivery is not relevant to shipment.

## Not Processed

The delivery is not currently assigned to a shipment.

## Partially Processed

The delivery has been assigned to at least one stage of a shipment.

## Completely Processed

The delivery has been assigned to all required stages. All stages required for the delivery have been planned.

  Note
Prior to the release of enhancement package 1 (SP01) of TM9 this status could only be set automatically from SAP ERP

shipment processing.

In TM a corresponding planning status exists on DTR header level. The four possible planning statuses are:

## Planning Not Started

No freight units (FU) have been created.

## In Planning

All FUs have been created; no freight order assignment has been made.

## Partially Planned

At least one FU has been assigned to a freight order.

## Planned

All stages of all FUs have been planned.

The correspondence of statuses is as follows:

## TM Planning Status

SAP ERP Transportation Planning Status

Planning Not Started

Not Processed

In Planning

Not Processed

Partially Planned

## Partially Processed

This is custom documentation. For more information, please visit SAP Help Portal.

84


1/14/26, 2:17 PM

## TM Planning Status

SAP ERP Transportation Planning Status

## Planned

## Completely Processed

Integration of Changed and Deleted ERP Orders and Deliveries

## Use

Logistics integration with SAP ERP supports changes to and deletion of orders in SAP ERP, and changes to, deletion, and splitting

of deliveries in SAP ERP. If Transportation Management (TM) receives an updated order or delivery, the change controller

propagates the changes to the freight units of the corresponding transportation requirement. Once freight units have been

adapted, the change controller can process subsequent documents further depending on strategies. For more information, see

Change Controller.

  Note

A user cannot change the data in an order-based transportation requirement or delivery-based transportation requirement nor

cancel or delete these documents in Transportation Management (TM). Changes can only be made in the SAP ERP system and

sent to TM.

## Features

For more information about how the change controller handles freight units assigned to changed or deleted transportation

requirements, see the following sections:

Processing Changed or Deleted Orders from ERP

Processing Changed, Deleted, or Split Deliveries from ERP

## Deleting and Canceling Freight Units

If, based on a changed or deleted transportation requirement, a freight unit becomes empty, the system either deletes or cancels

the freight unit. Whether the freight unit is deleted or canceled, depends on your settings for the freight unit type.

Processing Changed or Deleted Orders from ERP

## Use

If a user changes the data in an order in SAP ERP (for example, quantities, dates and locations can be changed), SAP ERP sends

these changes to Transportation Management (TM) and the corresponding order-based transportation requirement is updated.

If an order is deleted in SAP ERP, the corresponding order-based transportation requirement is canceled in TM.

## Process

## Update of an Order

The following figure shows the process flow when an order is changed in SAP ERP, and is followed by a description:

This is custom documentation. For more information, please visit SAP Help Portal.

85


1/14/26, 2:17 PM

## Update of Order in SAP ERP

In the above figure, the abbreviation TRSR means TransportationRequestSUITERequest.

The process runs as follows:

1. Change order (SAP ERP)

If changes are made to an order in SAP ERP, an update is sent to TM

2. Update order–based transportation requirement (TM)

In TM, the corresponding order-based transportation requirement is updated. If the quantity has changed, the open

quantity (and, if affected by this, the consumption status) is adjusted accordingly.

3. Adapt freight units (TM)

TM updates the freight units according to the assigned freight unit building rule. If a delivery has already been created (and

thus, the freight units have already been reassigned to the delivery-based transportation requirement), TM creates new

freight units in case of a quantity increase to cover the resulting open quantity of the order-based transportation

requirement. Note that the delivery-based transportation requirement and its freight units are not affected by the updated

order.

4. Determine and apply strategies (TM)

The change controller uses strategies to adapt subsequent documents.

## Deletion of an Order

The following figure shows the process flow when an order is deleted in SAP ERP, and is followed by a description:

This is custom documentation. For more information, please visit SAP Help Portal.

86


1/14/26, 2:17 PM

## Deletion of Order in SAP ERP

In the above figure, the abbreviation TRSCR means TransportationRequestSUITECancellationRequest.

The process runs as follows:

1. Delete order (SAP ERP)

SAP ERP sends a request to cancel the order-based transportation requirement in TM. Note that if a delivery has already

been created in SAP ERP, the order cannot be deleted in SAP ERP

2. Cancel order-based transportation requirement (TM)

In TM, the corresponding order-based transportation requirement is canceled.

3. Adapt freight units

If the freight unit was only relevant for the canceled order-based transportation requirement, the freight unit becomes

empty. If the freight unit was assigned to multiple order-based transportation requirements, the quantity in the freight unit

is reduced according to the canceled order-based transportation requirement.

4. Delete or cancel freight units (TM)

If the freight unit is empty, TM either deletes or cancels the freight unit according to your settings for the freight unit type.

5. Determine and apply strategies (TM)

Processing Changed, Deleted, or Split Deliveries from ERP

## Use

If a delivery is changed, split, or deleted in SAP ERP, this information is sent to Transportation Management (TM). TM adjusts the

corresponding delivery-based transportation requirement based on this information.

Note that changes or splits can originate in SAP ERP or in the SAP Extended Warehouse Management (SAP EWM) application.

Changes or splits in SAP EWM are always transferred to TM via SAP ERP.

This is custom documentation. For more information, please visit SAP Help Portal.

87


1/14/26, 2:17 PM

The following sections describe how TM handles these changes.

## Process

## Update of a Delivery

The following figure shows the process for updating a delivery in SAP ERP after delivery creation and is followed by a description.

## Update of Delivery in SAP ERP

In the above figure, the abbreviation TRSR means TransportationRequestSUITERequest.

The process runs as follows:

1. Update delivery (SAP ERP)

ERP sends a changed delivery to TM.

2. Update delivery-based transportation requirement (TM)

In TM, the corresponding delivery-based transportation requirement is updated.

3. Adapt freight units (TM)

The change controller adjusts the freight units according to the changes in the delivery-based transportation requirement.

If the quantity of the delivery-based transportation requirement has changed and the delivery-based transportation

requirement is assigned to freight units that were consumed from an order-based transportation requirement, the change

controller processes the freight units as follows:

If the quantity of the delivery-based transportation requirement has decreased, the open quantity of the

corresponding order-based transportation requirements is increased accordingly; and the freight units of the

delivery-based transportation requirement are split. Freight units are retained by the delivery-based transportation

requirement to cover the reduced quantity of the delivery-based transportation requirement, and the remaining

freight units are assigned to the corresponding order-based transportation requirement.

This is custom documentation. For more information, please visit SAP Help Portal.

88


1/14/26, 2:17 PM

If the quantity of the delivery-based transportation requirement has increased, and there are still open quantities in

the corresponding order-based transportation requirement, the system reassigns the freight units from the order-

based transportation requirement to cover this increased delivery quantity. The system then reduces the open

quantity of the order-based transportation requirements.

4. Determine and apply strategies (TM)

## Deletion of a Delivery

The following figure shows the process for deleting a delivery in SAP ERP after delivery creation and is followed by a description:

## Deletion of Delivery in SAP ERP

In the above figure, the abbreviation TRSCR means TransportationRequestSUITECancellationRequest.

The process runs as follows:

1. Delete delivery (SAP ERP)

ERP sends a request to cancel the delivery-based transportation requirement.

2. Cancel delivery-based transportation requirement (TM)

In TM, the corresponding delivery-based transportation requirement is canceled.

3. Reassign freight units to order-based transportation requirement (TM)

If a corresponding order-based transportation requirement exists, the freight units are reassigned to this order-based

transportation requirement.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

89


1/14/26, 2:17 PM

If the process runs without order integration (that is, no order-based transportation requirement exists), the freight

units are adapted and, if necessary, are canceled or deleted depending on your settings for the freight unit type.

4. Determine and apply strategies (TM)

## Split of a Delivery

For more information, see the following:

Delivery Splits Triggered by SAP ERP

Delivery Splits and Updates Triggered by TM

Delivery Splits Triggered by SAP ERP

## Use

You can split an outbound delivery or inbound delivery in SAP ERP or in the SAP Extended Warehouse Management (SAP EWM)

application and trigger the required changes in TM. If SAP EWM triggers the split, the delivery split is processed in SAP ERP first

and then transferred to TM.

## Prerequisites

You have created a delivery-based transportation requirement (DTR) in TM based on an SAP ERP delivery.

If required, you have defined a delivery split/update type in Customizing for Transportation Management under

## Integration

  Logistics Integration

 External TM System Integration

 Delivery-Based Transportation Requirement

 Define Delivery Split/Update Types .

In the delivery/split update type, you define how the system updates freight unit planning after the delivery split has been

performed in TM. Note, however, that the system checks this setting only if the planning changes cannot be determined

based on other criteria (for example, the application that triggered the split). For more information about the criteria and

the sequence in which they are checked, see the field help for the Handle Planning Results field in the Customizing activity

Define Delivery Split/Update Types.

You have assigned the delivery split/update type to the delivery-based transportation requirement type in Customizing for

Transportation Management under

## Integration

 Logistics Integration

 External TM System Integration

## Delivery-

## Based Transportation Requirement

 Define Delivery-Based Transportation Requirement Types .

## Process

1. Split delivery (SAP ERP)

SAP ERP splits a delivery that has already been sent to TM. SAP ERP sends the following information in separate messages:

The new delivery that has been created for the items split from the original delivery. The data sent includes a

reference to the original delivery and the triggering application SAP ERP or SAP EWM.

The changed original delivery. The data sent includes a reference to the new delivery.

2. Create new DTR and update original DTR (TM)

TM creates the new DTR first by reassigning the freight units from the original DTR to the new DTR. It then updates the

original DTR.

This is custom documentation. For more information, please visit SAP Help Portal.

90


1/14/26, 2:17 PM

TM receives a new or updated delivery using the Maintain Transportation Request

(IntracompanyTransportationRequestRequest_In) enterprise service in the Transportation Request

Processing process component.

3. Update freight unit planning (TM)

The system determines the required changes to freight unit planning for the freight units assigned to the new DTR and the

original DTR. For example, the system discards the planning of the freight units assigned to the new DTR and keeps the

planning of the freight units assigned to the original DTR.

Delivery Splits and Updates Triggered by TM

## Use

You can split an outbound delivery in SAP ERP based on planning changes in TM. You can also update the goods issue date, loading

date, transportation start date, and delivery date in the outbound delivery based on changed dates in TM.

When SAP ERP receives a request for a split or update, it makes the necessary changes in outbound delivery processing and sends

the delivery data back to TM. TM can then make the required changes to the delivery-based transportation requirements (DTRs).

Note that TM can trigger the split or update of outbound deliveries only. It cannot trigger the split or update of inbound deliveries.

## Prerequisites

You have created a delivery-based transportation requirement (DTR) in TM based on an SAP ERP outbound delivery.

The outbound delivery in SAP ERP does not have one of the following statuses:

## Distribution status: Distributed

## Goods movement status: Partially Completed or Completed

If the delivery has one of the above statuses, TM does not request the split or update.

You have have assigned a split profile to the DTR type in Customizing for Transportation Management under

## Integration

 Logistics Integration

 External TM System Integration

 Delivery-Based Transportation Requirement

## Define

Delivery-Based Transportation Requirement Types .

## Process

## Outbound Delivery Split

1. Perform transportation planning (TM)

You perform planning or change the existing planning of freight units that belong to a DTR that is based on an outbound

delivery. When you save the planning results, the system determines that a delivery split is required. For example, freight

units that belong to the DTR have been assigned to different freight orders, or only some of the FUs that belong to a DTR

have been assigned to freight orders and the other FUs have not been assigned. Note that the split is required only if the

first stage or the last stage of the transportation chain is affected.

TM determines whether the SAP ERP delivery can still be changed by checking the delivery status. If the delivery can be

changed, TM sends the required delivery split to SAP ERP. TM sends the details of the items that are to be split from the

original delivery (that is, IDs of the items in the original delivery, split quantity, unit of measure, and the required dates for

the new delivery).

This is custom documentation. For more information, please visit SAP Help Portal.

91


1/14/26, 2:17 PM

TM sends the split request using the Request Outbound Delivery Split V1

(OutboundDeliveryERPSplitRequest_Out_V1) enterprise service in the Transportation Request Processing

process component. Note that if a delivery is to be split into several deliveries, each delivery is sent to SAP ERP in a

separate message.

2. Split outbound delivery (SAP ERP)

Based on a split request received from TM, SAP ERP creates a new outbound delivery and changes the original outbound

delivery (that is, it removes the relevant items from the original delivery and creates a new delivery for these items). If you

specified a split reason in the delivery split/update type, SAP ERP splits the delivery according to the settings in the

corresponding split profile.

SAP ERP informs TM about whether the delivery split was successful. The confirmation is received in TM by the Change

Transportation Request Based on Outbound Delivery Split Confirmation V1

(OutboundDeliveryERPSplitConfirmation_In_V1) enterprise service in the Transportation Request Processing

process component.

SAP ERP sends the following information in separate messages:

The new delivery that has been created for the items split from the original delivery. The data sent includes a

reference to the original delivery and the triggering application TM.

The changed original delivery. The data sent includes a reference to the new delivery.

3. Create new DTR and update original DTR (TM)

TM creates the new DTR first by reassigning the freight units from the original DTR to the new DTR. It then updates the

original DTR.

TM receives a new or updated delivery using the Maintain Transportation Request

(IntracompanyTransportationRequestRequest_In) enterprise service in the Transportation Request

Processing process component.

## Outbound Delivery Update

1. Perform transportation planning (TM)

You perform planning or change the existing planning of freight units that belong to a DTR that is based on an outbound

delivery. Dates are changed during planning. Alternatively, you change the dates of the relevant freight order. When you

save the planning results or the changed freight order, TM determines that the dates in the freight order no longer match

the dates in the DTR and the original SAP ERP delivery.

TM determines whether the SAP ERP delivery can still be changed by checking the delivery status. If the delivery can be

changed, TM sends the changed dates to SAP ERP and requests the update of the outbound delivery.

TM sends the update request using the Request Outbound Delivery Update

(OutboundDeliveryUpdateRequest_Out) enterprise service in the Transportation Request Processing process

component.

2. Update outbound delivery (SAP ERP)

Based on the request received from TM, SAP ERP updates the relevant dates.

SAP ERP informs TM about whether the delivery update was successful. The confirmation is received in TM by the Change

## Transportation Request Based on Outbound Delivery Update Confirmation

(OutboundDeliveryConfirmation_In_V1) enterprise service in the Transportation Request Processing process

component.

SAP ERP sends the updated outbound delivery to TM. In TM, the delivery is received by the Maintain Transportation

Request (IntracompanyTransportationRequestRequest_In) enterprise service in the Transportation Request

This is custom documentation. For more information, please visit SAP Help Portal.

92


1/14/26, 2:17 PM

Processing process component.

3. Update DTR (TM)

## Result

The planning data in TM and the SAP ERP delivery data is aligned.

Note the following:

The triggering application is included in the message sent by SAP ERP. This enables TM to distinguish between a split that

is triggered by TM (planning is correct) and a split triggered by SAP ERP or SAP EWM (planning is no longer correct and

must be updated).

If TM triggers a delivery split and a delivery update for the same delivery at the same time, the split and update is sent in

the same message using the Request Outbound Delivery Split V1 (OutboundDeliveryERPSplitRequest_Out_V1)

enterprise service.

You can use a worklist to monitor DTRs for which a delivery split or update has not been completed yet using the Display Delivery-

Based Transportation Requirement app, which you open from the launchpad.

Delivery Creation and Split for Package Units with Multiple
## Assignments

You can configure the system to allow a freight unit to be assigned to several package units when you create package units from a

freight order.

This means that the items of a freight unit may be spread across multiple package units and multiple freight orders. If load

planning is not finalized, this can lead to:

unnecessary delivery splits

unnecessary freight unit splits

creation of unnecessary deliveries

To avoid unnecessary splits, or creation of unnecessary deliveries, the system does not consider a freight order for delivery

creation until load planning for the freight units of that freight order is finalized. The system treats such freight units as unplanned

freight units. When load planning is finalized for all freight units of a freight order, the system considers that freight order and can

create, split, or update deliveries.

## Prerequisites

You have specified that a freight unit can be assigned to multiple packages. For more information see Customizing for

Transportation Management under  Freight Order Management

## Transportation Unit

## Define Transportation Unit Types

(Assgnmt of Pred.Docs (Assignment of Predecessor Documents) field)

## Features

When load planning for a freight order is finalized, the system identifies all required delivery splits, and then splits and updates

deliveries accordingly.

This is custom documentation. For more information, please visit SAP Help Portal.

93


1/14/26, 2:17 PM
Related Information

## Package Unit

Creating a Package Unit

## Load Planning

Integration of SAP ERP Scheduling Agreements with TM

## Use

A scheduling agreement is an outline agreement containing delivery quantities and dates within a specified time period. These are

then entered as schedule lines in a delivery schedule.

You can integrate purchase scheduling agreements and Sales scheduling agreements from SAP ERP with TM. The integration is

based on delivery schedules. You can control the communication between the two systems by using specific time horizons and by

specifying which delivery schedule types (Forecast or JIT) should be transferred.

Communication is based on eSOA services, supporting both process integration (PI) based communication and web services

reliable messaging (WS-RM).

The integration can be triggered by the creation or a change of delivery schedules. You can use a batch process to manage the

future transfer of delivery schedules

## Prerequisites

## Integration of Purchase Scheduling Agreements

You have completed Customizing for integration of purchase scheduling agreements. For more information see Customizing for

## SAP ERP under

Integration with other SAP Components

 Transportation Management

 Logistics Integration

## Define

Settings for Integration of MM Scheduling Agreements .

## Integration of Sales Scheduling Agreements

You have completed Customizing for integration of sales scheduling agreements. For more information see Customizing for SAP

## ERP under

Integration with other SAP Components

 Transportation Management

 Logistics Integration

## Define Settings

for Integration of Sales Scheduling Agreements

## Transfer of Purchasing Documents

You have completed Customizing for transfer of purchasing documents. For more information see Customizing for SAP ERP under

Integration with other SAP Components

 Transportation Management

 Logistics Integration

 Activate Transfer of

## Purchasing Documents

## Controlling the Sales Document Transfer

You have customized the processing of sales scheduling agreements to determine the relevant TM control key, specifying which

documents in a document chain are to be transferred to TM. For more information see Customizing for SAP ERP under

Integration with other SAP Components

 Transportation Management

## Order Integration

 Activate Transfer of Sales

Documents .

## Features

This is custom documentation. For more information, please visit SAP Help Portal.

94


1/14/26, 2:17 PM

You can work with the following types of scheduling agreements:

## Sales scheduling agreements

Create sales scheduling agreements (and corresponding delivery schedules) in SAP ERP and transfer them initially

to TM. You can then create transportation requirements in TM.

Change sales scheduling agreements(and corresponding delivery schedules) in SAP ERP and transfer the changes

to TM. You can then change the corresponding transportation requirements in TM.

Create delivery proposals in TM for freight units (FU), on the basis of sales delivery schedules. You can then process

the delivery proposal and create outbound deliveries in SAP ERP.

## Materials Management (MM) scheduling agreements

Create MM delivery schedules in SAP ERP and transfer them to TM. You can then create transportation

requirements in TM.

Change MM delivery schedules in SAP ERP and transfer the changes to TM. You can then change the corresponding

transportation requirements in TM.

Create delivery proposals in TM for FUs which are based on MM delivery schedules. Process the delivery proposal

and create inbound deliveries in SAP ERP.

## Restrictions

Sales scheduling agreements:

It is out of scope to send sales scheduling agreements via batch report RSNAST00. The messages for sales scheduling

agreements need to be created during the save process of the document.

Sales order scheduling (SOS) is not supported for sales scheduling agreements.

Packing instructions are not reflected in the interface for scheduling agreements.

Scheduling agreements with delivery orders (Standard document type LZM, VBAK-VBKLT = ʻC’) are out of scope.

Replenishment deliveries based on inbound sequenced JIT calls (Standard document type LZJ) are out of scope.

Scheduling agreements with external service agents are out of scope.

The use of bills of material is out of scope.

In the integration scenario, SAP ERP transfers either forecast (FRC) delivery schedules or just-in-time (JIT) delivery

schedules to TM. The simultaneous transfer of both FRC and JIT delivery schedules is not supported. Material

requirements planning (MRP) for delivery schedule types that require both FRC delivery schedules and JIT delivery

schedules to be delivery-relevant is not supported. This means that for delivery schedule types A and B, in which the

schedule lines of the forecast delivery schedule become relevant for delivery after the JIT delivery schedule horizon,

integration is not possible.

Purchase scheduling agreements:

Usage of pickup sheets: the customer can send a message to the vendor which represents a pickup sheet. A pickup sheet is

sent to the vendor and is the basis for transportation planning as the pickup is arranged according to this document. At the

vendor a delivery order is created out of the pickup sheet information. The pickup is planned in the TM system of the

customer. With respect to TM-integration this process is out of scope.

Acknowledgements of internet SA releases have no influence on which data is transferred to the TM system.

Replenishment with summarized JIT calls is out of scope.

This is custom documentation. For more information, please visit SAP Help Portal.

95


1/14/26, 2:17 PM

Replenishment based on outbound sequenced JIT calls is out of scope.

Purchase and Sales scheduling agreements :

If delivery creation is triggered by the ECC system the delivery creation must be consistent to the schedule line information

which has been transferred to TM. This means that a delivery creation process in ECC must not include schedule lines

which have not yet been transferred to the TM system or will never be transferred. Especially the ECC system must prevent

delivery of FRC schedule lines if these are not configured to be transferred to TM. The same applies to JIT schedule lines.

Supplier Returns Processing Based on QM Notifications

This example describes a process for handling supplier returns.

## Prerequisites

If you use this process within Advanced Shipping and Receiving, see Prerequisites for Advanced Shipping and Receiving

Customer Side: Inbound Process

1. Creating a purchase order

Create a purchase order in Materials Management (MM). The system automatically creates freight units (FU).

2. Creating a freight order

Create a freight order in Transportation Management (TM) and insert the FU.

3. Creating an inbound delivery

Create an inbound delivery in TM. You can create the delivery in the Create Freight Order app by selecting  Follow Up

 Create Delivery .

When goods are delivered, you post goods receipt.

4. Executing quality management

After putaway, you subject the goods to quality inspection. When any given number of goods fail inspection, you create a

QM notification and a returns handling process is initiated.

## Customer Side: Returns Handling

1. Creating a quality management (QM) notification

Start with a QM notification.

You can run transaction QM01 to call up the Create Notification window. To create a complaint, use notification type Q2.

Enter the purchasing document ID and item number.

Under tab Subject, you can enter the quantity of goods complained.

2. Creating a returns delivery

Next, go to Change Notification.

To create a returns delivery, first you must transfer the goods to a blocked stock. You can do that under Enter Transfer

Posting. Enter the complaint quantity and storage location. Save the changes.

This is custom documentation. For more information, please visit SAP Help Portal.

96


1/14/26, 2:17 PM

You can then create a returns delivery. Select the reason for the movement, for example, damaged.

You can find the returns delivery under Change Outbound Delivery.

3. Posting goods issue

To proceed, post goods issue under Outbound Delivery.

A new FU with the indicated quantity of goods is automatically assigned to the original purchase document.

Supplier Side: Outbound Process

1. Delivering goods based on open quantity

The supplier can now execute a new delivery based on the quantity indicated in the returns delivery.

## Related Information

## Advanced Shipping and Receiving

## Integration with Advanced Shipping and Receiving

This is custom documentation. For more information, please visit SAP Help Portal.

97
