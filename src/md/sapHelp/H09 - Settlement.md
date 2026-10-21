1/14/26, 2:42 PM

Transportation Management (TM)

Generated on: 2026-01-14 14:42:14 GMT+0000

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


1/14/26, 2:42 PM

Settlement

## Use

You can use settlements to meet the following business requirements:

Create a freight settlement document in Transportation Management (TM) for the transportation services provided to you

by a carrier. TM transfers the freight settlement document to Materials Management (MM). You can verify the invoices you

receive from your carrier against the information contained in the freight settlement document (see Freight Settlement).

Create a forwarding settlement document in TM to bill a customer for the transportation services you provide to the

customer. TM transfers the forwarding settlement document to Sales and Distribution (SD) and SD sends the invoice to the

customer (see Forwarding Settlement).

Create an internal settlement document for a transportation service provided to you by an internal organization in your

company. The internal organization bills you to recover the cost of the transportation services it provided to you when you

fulfilled a forwarding order to a customer (see Internal Settlement Management).

Create an internal settlement document for the resources you use in providing a transportation service in a freight order to

another internal organization in your company (see Internal Settlement for Resources).

The following functions that are described below are currently not released:

Group logistics scenario in system internal integration

## Internal settlement for resources

The figure below illustrates a typical customer order process for you as a provider of logistics services. The figure is followed by an

explanation:

To execute your forwarding orders you have the following organizations in place:

This is custom documentation. For more information, please visit SAP Help Portal.

2


1/14/26, 2:42 PM

Sales (SALES_1)

A sales organization that is customer facing.

Resource (RESOURCE_1)

An internal sales organization that owns the resource.

You can create, change, or display resources as follows:

On the SAP Easy Access screen, choose  Transportation Management

 Master Data Resource

 Resource .

In the SAP launchpad, open the Define Resource app

Purchasing (PUR_1)

A purchase organization that is responsible for the procurement of the transportation service.

You have a carrier (CARRIER_1), who provides you with transportation services.

You have the following customers:

Customer 1 (CUST_1)

Customer 2 (CUST_2)

You create a forwarding order for each of customers 1 and 2, to transport goods on their behalf from a source location to a

destination location. To move the goods, you need a trailer. Your internal resource organization owns a trailer, and agrees to provide

you with a trailer. You need a truck to pull the trailer. Your purchasing organization buys the services of a truck from your carrier.

You create a freight order (Freight_Order_1) to fulfill the demand, and you subcontract the freight order to a carrier.

In the freight order, you provision a trailer unit that contains the trailer resource (Trailer_1). An internal organization in your

company owns the trailer. The internal organization recovers the cost of providing the trailer from you.

The carrier uses his or her own truck and your trailer (Trailer_1) to move the goods from the source location to the destination

location.

The figure below illustrates the settlement process for the above customer order process and is followed by an explanation:

This is custom documentation. For more information, please visit SAP Help Portal.

3


1/14/26, 2:42 PM

To settle your forwarding orders, you have the following agreements in place:

A forwarding agreement between your sales organization SALES_1 and your first customer, CUST_1 so that your sales

organization gets paid for providing the transportation service. Also a forwarding agreement between your sales

organization SALES_1 and your second customer, CUST_2, again so that your sales organization gets paid for providing the

transportation service.

An internal agreement between your purchasing organization (PUR_1) and your sales organization (SALES_1), so that your

purchasing organization recovers the following costs:

## Payment to the carrier for providing the truck

## Payment to the resource organization (RESOURCE_1) for providing the trailer

An internal agreement between your resource organization (RESOURCE_1) and your purchasing organization (PUR_1), so

that your resource organization gets paid for providing the trailer.

An external agreement between your purchasing organization (PUR_1) and your carrier, so that your carrier (CARRIER_1)

provides the truck and hauls the trailer and gets paid for supplying the transportation service.

You have the following settlement documents:

Your sales organization creates a forwarding settlement document for each of the forwarding orders it has in place with

customer 1 and customer 2. This combined amount is what you get paid for the transportation service you provide to your

customers. You post the forwarding settlement documents to SD. SD sends the invoices to your customers and receives

payment from your customers.

Your purchasing organization creates an internal settlement against your sales organization for each of the forwarding

orders for which it provided a truck and trailer. This enables your purchasing organization to recover the cost of providing

the transportation service.

If the purchase organization belongs to a different company code in your company, you have an intercompany settlement.

You post the internal settlement document to SD.

This is custom documentation. For more information, please visit SAP Help Portal.

4


1/14/26, 2:42 PM

If the purchase organization belongs to the same company code as that of your sales organization, you have an

intracompany posting. You post the internal settlement document directly into financial accounting.

Your resource organization creates an internal settlement document against your purchasing organization, to recover the

cost of providing the trailer. You post the internal settlement document to SD to post to financials if the purchase

organization belongs to a different company code in your company. If the purchase organization belongs to the same

company code as that of your sales organization, the internal settlement document posts directly into financial accounting

to do an intra-company posting.

Your purchasing organization creates a freight settlement document against your carrier. This simulates the cost of

providing the truck in TM. You post the freight settlement document to MM. Later, when your carrier sends you the invoice

for providing the truck and hauling the trailer, you verify the amount in the invoice against the amount you transferred in the

freight settlement document to MM. If the amounts match, you pay the carrier.

## Settlement for Shippers

For shippers, your carrier or logistics service provider (LSP) provides you with a freight transportation service. You follow the

freight settlement process to settle the freight costs with your carrier or LSP. You can also use cost distribution to distribute the

freight costs to the level of each individual order/delivery item in your freight order to allocate the freight cost to financial

accounting and controlling. The system performs the cost distribution when it creates the associated freight settlement

document. You post the freight settlement document with the distributed costs to MM and settlement management.

When your carrier sends you the invoice for providing the truck and hauling the trailer, you verify the amount in the invoice against

the amount you transferred in the freight settlement document to MM. If the amounts match, you pay the carrier.

## More Information

The following table gives more information on the settlement process for LSPs:

## Subject

## More Information

Overview of how the different settlement types work together in a

Settlement for LSPs in an Ocean Freight Scenario

business context for a logistics service provider

Agreements, including forwarding and internal agreements

## Agreement Management

Overview of forwarding order management

## Forwarding Order Management

Overview of internal settlement management

Internal Settlement Management

Overview of freight order management

## Freight Order Management

Overview of how the forwarding settlement process works

## Forwarding Settlement

The following table gives more information on the settlement process for shippers:

## Subject

## More Information

Overview of how you can create and edit agreements with

## Agreement

transportation service providers

Overview of how the freight settlement process works

## Freight Settlement

Overview of cost distribution management

## Cost Distribution Management

Overview of how the system distributes freight costs

## Cost Distribution for Shippers

This is custom documentation. For more information, please visit SAP Help Portal.

5


1/14/26, 2:42 PM

Settlement for LSPs in an Ocean Freight Scenario

## Example

You are a logistics service provider (LSP) and you have a sales organization that takes forwarding orders from your customers. You

have an internal gateway organization that manages your container freight station, consolidates shipments from different sales

organizations, and creates consolidated bookings with your ocean carrier. Your gateway organization creates an intercompany

internal settlement document against your sales organization to recover the cost of providing the ocean booking, and any

additional costs incurred at the container freight station, for example consolidation costs. Only the sales organization is in contact

with your customer.

The figure below illustrates an example of a business scenario in which you use forwarding settlement documents, freight

settlement documents, and internal settlement documents. It is followed by an explanation:

## Term Explanation

Some of the key terms in the graphic are explained as follows:

STA

A station, which is usually the sales organization of an LSP.

## Gateway

A gateway consolidation operation that includes a container freight station. The gateway is both a sales organization for

internal sales and a purchasing organization for the procurement of freight services from carriers. The purchasing

This is custom documentation. For more information, please visit SAP Help Portal.

6


1/14/26, 2:42 PM

organization usually procures for the main carriage.

CU

A customer.

## STA-NUE

The export station at Nuremberg, and also the export sales organization.

## STA-DLS

The import station at Dallas, and also the import sales organization.

## Incoterms

The customer in Dallas (not shown on the graphic) uses an Incoterm of FOB (Free On Board) to Rotterdam. The shipper CU-NUE

Nuremberg pays for the pre-carriage. The ship-to party CU-DLS Dallas pays for the main carriage and the on-carriage.

In your forwarding order, you specify the shipper CU-NUE Nuremberg as the prepaid agreement party and Dallas import station

STA-DLS as the collect agreement party. You specify Dallas import station STA-DLS as the collect agreement party because you

use the business unit that is closest to the external customer to settle with the external customer (ship-to party CU-DLS Dallas). In

this example, the customer in Dallas, who is the ship-to party CU-DLS_Dallas, pays the sales organization in Dallas (STA-DLS,

Dallas import station).

Nuremberg export station STA-NUE pays the carrier for the pre-carriage. The Rotterdam gateway CFS-RTM pays the carrier for the

main carriage and settles internally with Nuremberg export station STA-NUE to recover the cost of the main carriage. The

Nuremberg export station STA-NUE recovers the cost of the main carriage from Dallas import station STA-DLS. Also the Dallas

import station STA-DLS settles with the ship-to party in Dallas (CU-DLS Dallas) for the main carriage and the on carriage.

## Cargo Movement

Nuremberg export station STA-NUE picks up the cargo from the shipper CU-NUE at Nuremberg. STA-NUE moves the cargo in the

pre-carriage stage to Rotterdam export container freight station CFS-RTM. The export gateway at Rotterdam is now responsible

for planning and moving the cargo. It moves the cargo in the main stage to Newark import container freight station CFS-NWK. The

import gateway at Newark collects the container at the port and brings it to the container freight station in Newark. Dallas import

station STA-DLA then moves the cargo in the on-carriage stage to the ship-to party CU-DLS in Dallas. You can use export/import

processing to ensure that the export organization and the import organization have the required information and business

documents to transport freight across customs borders. For more information, see Export/Import Processing.

## Agreements

The following table explains the agreements that are in place:

Agreement Type

Agreement Parties

Reason for Agreement

## Forwarding agreement

Nuremberg export station STA-NUE as the

Provide main carriage services

organization and Dallas import station STA-

DLA Dallas as the business partner

## Forwarding agreement

Nuremberg export station STA-NUE as the

Move the cargo from Nuremberg to

organization and shipper CU-NUE

Rotterdam as agreed in the Incoterm FOB

Nuremberg as the business partner

## Forwarding agreement

Dallas import station STA-DLS as the

Provide freight services from Rotterdam to

organization and ship-to party CU-DLS

the ship-to party location in Dallas

## Dallas as the business partner

This is custom documentation. For more information, please visit SAP Help Portal.

7


1/14/26, 2:42 PM

Agreement Type

Agreement Parties

Reason for Agreement

## Freight agreement

Nuremberg export station STA-NUE as the

Provide pre-carriage services

organization and Carrier 1 as the business

partner

## Freight agreement

Rotterdam export gateway CFS-RTM as the

Provide ocean freight services

organization and the ocean carrier Carrier 2

as the business partner

## Freight agreement

Dallas import station STA-DLS as the

Provide on-carriage services

organization and Carrier 3 as the business

partner

## Internal agreement

The Rotterdam gateway CFS-RTM as the

Provide main carriage and other

organization and Nuremberg export station

consolidation services

STA-NUE as the business partner

## Forwarding Settlements

The forwarding settlement document is a business document that contains the freight costs, and is a request to settle those costs

with the customers. The customers can be external customers or internal customers who are the other organizations participating

in the overall transportation. Transportation Management (TM) sends the forwarding settlement document to Sales and

Distribution (SD) to create a billing document to be sent to the customer.

Nuremberg export station STA-NEU sends a billing document to the shipper CU-NEU Nuremberg for USD 500. The shipper pays

for the pre-carriage cost.

Dallas import station STA-DLS sends a billing document to the ship-to party CU-DLS Dallas for USD 2800. The ship-to party pays

for the main carriage and on-carriage costs.

Nuremberg export station STA-NEU also sends a billing document to the internal organization Dallas import station STA-DLS for

USD 2200. The Dallas import station pays for the main-carriage cost.

## Freight Settlements

The freight settlement document is a business document that contains the freight costs. You can use the freight settlement

document to record the expected costs that you want to settle with your logistics service providers or carriers. Carrier 1 invoices

Nuremberg export station STA-NEU for USD 400, the cost of providing the pre-carriage transportation service. In TM, STA-NEU

creates a freight settlement document for the pre-carriage and posts these costs in materials management (MM). Nuremberg

export station then uses this information in MM as a basis to verify the invoice it receives from Carrier 1. If the details match, it

pays Carrier 1 from MM.

Rotterdam export gateway CFS-RTM and Dallas import station STA-DLS Dallas follow the same process. They pay carriers 2 and 3

USD 2000 and USD 400 respectively.

## Internal Settlements

Rotterdam export gateway CFS-RTM creates an internal settlement on Nuremberg export station STA-NEU to recover the costs it

incurred in providing the transportation services for the main carriage. CFS-RTM receives an invoice from its carrier for USD 2000,

but it can also charge STA-NEU USD 2200 based on the internal rates between the organizations. As a result CFS-RTM can make

USD 200 profit from the transportation.

Your company can also base the internal settlement document on the actual costs from the carrier. In this case CFS-RTM does not

make a profit and bills STA-NEU for USD 2000.

This is custom documentation. For more information, please visit SAP Help Portal.

8


1/14/26, 2:42 PM

## Consolidated Shipment

The graphic illustrates a single shipment scenario. You can also manage a consolidated shipment scenario where Rotterdam export

gateway CFS-RTM consolidates multiple forwarding orders (movements of cargo for an external customer) from different

organizations in your company. CFS-RTM moves the cargo for the forwarding orders to Newark import container freight station

CFS-NWK. CFS-NWK deconsolidates the cargo. The individual import freight stations then deliver the cargo to the different ship-to

parties.

Rotterdam export gateway CFS-RTM sends an internal settlement document for the main-carriage cost to each of the internal

export organizations for the forwarding orders. It can base the settlements on the internal rates agreed between the organizations

or the cost of executing the transportation services.

## Settlement Based on Agreed Rates

Rotterdam export gateway CFS-RTM can use a standard agreed rate as a basis for its freight costs. It can use the agreed rate to

settle the cost it incurs in servicing each forwarding order that it consolidates and ships. For more information, see Standard

Charge Calculation.

## Settlement Based on Freight Costs

If CFS-RTM bases the settlements on the costs, it must determine the share of the overall execution cost for which each

organization is liable. CFS-RTM uses cost distribution to share the costs to the organizations. Using cost distribution, CFS-RTM can

determine the share of the overall freight booking cost that applies to each of the forwarding orders, by distributing the freight

booking cost at the forwarding order level. It can then use the distributed costs for each of the forwarding orders to create the

settlement.

For more information about distributing freight costs, see Cost Distribution Management. For more information about transferring

distributed costs from the freight side to the forwarding side, and using the costs as a basis for settling with a customer or an

internal organization, see Cost Pull.

More Information

## Subject

## More Information

Overview of how the forwarding settlement process works

## Forwarding Settlement

Overview of how the freight settlement process works

## Freight Settlement

Overview of internal settlement management

Internal Settlement Management

Forwarding Settlement

## Use

You can trigger the creation of an invoice to give to a customer for transportation service charges. You can also trigger the creation

of a credit memo to give a credit to a customer. The Sales and Distribution (SD) system creates an invoice and a credit memo.

## Integration

Forwarding Settlement is a component of Transportation Management (TM) and is integrated with the following TM components:

This is custom documentation. For more information, please visit SAP Help Portal.

9


1/14/26, 2:42 PM

## Component

## Integration Type

## Forwarding Order Management

A forwarding order provides the basis for a forwarding settlement

document.

A forwarding settlement document provides the basis for credit

memos for forwarding orders.

Charge Management and Service Product Catalogs

As a prerequisite for creating a forwarding settlement document,

you must create the relevant charge management master data.

Forwarding Settlement is also integrated with SD, as the creation of the invoice and credit that are relevant for accounting takes

place in SD.

## Constraints

This component triggers the invoice and credit creation and the actual invoices and credit memos are created in the SD.

Forwarding Settlement Document

## Definition

A document that is posted to Sales and Distribution (SD) to request the creation of an invoice to be sent to a customer.

## Use

You can use the forwarding settlement document (FWSD) to enter the data for transportation invoicing for your business partners

on the sold-to party side, and forward it to SD for invoicing. Transportation Management (TM) calculates the transportation

charges on the basis of a forwarding order (FWO). When you post the FWSD, the system creates an invoice in SD.

You can create an individual FWSD for one FWO or a collective FWSD for multiple FWOs.

## Structure

The FWSD data is taken from the FWOs.

The FWSD consists of the following tab pages:

## General Data

The system displays general data such as the following:

Invoice date

Sales organization

Payment terms

Total amount

Document currency

## Business Partner

This is custom documentation. For more information, please visit SAP Help Portal.

10


1/14/26, 2:42 PM

The system displays the sold-to party, bill-to party and payer by default. You can use business partner determination to

specify how the system assigns business partners to forwarding settlement documents if they are not defined in the

forwarding orders.

## Charges

The system displays the transportation charges for each FWSD item. The FWSD item could be either an FWO or individual

items of the FWO, depending on the calculation level settings in the calculation profile. For more information about the

calculation profile, see Customizing for Transportation Management under  Basic Functions

 Charge Calculation

## Basic Settings

 Define Calculation Profiles . In the case of collective FWSDs, the system shows the total amount for all

the FWOs assigned to the FWSD.

For execution-based settlement scenarios such as buyer’s consolidation, trailer-unit-based settlement or route-based

settlements, the settlement items are the container item of the booking, the trailer unit and the freight order respectively.

## Orders

The system displays the list of FWOs or FWO items that are being settled with this FWSD, depending on the calculation level

settings in the calculation profile. The FWSD item could be either an FWO or individual items of the FWO.

For FWSDs that you create for FWOs that are part of a buyer’s consolidation, the system displays the freight booking

document that has the container item of the buyer’s consolidation. In the Details area of the screen, the system displays

the container item details and the FWOs that are part of the container.

For FWSDs that you create for FWOs that have a trailer-unit-based settlement basis, the system displays the relevant trailer

unit. In the Details area of the screen, the system displays the FWOs in the trailer unit for a bill-to party. For more

information, see Trailer-Unit-Based Settlement.

For FWSDs that you create for FWOs that have a route-based settlement basis, the system displays the relevant freight

order document. In the Details area of the screen, the system displays the forwarding orders associated with the freight

order. For more information, see Route-Based Settlement.

## Document Flow

The system displays the predecessor and successor business documents as a document flow, including the corresponding

follow-on billing documents created in SD on posting the FWSD. You can access the business documents from the

Document Flow tab of the document.

## Application Log

The system displays any error or warning messages that were encountered when the FWSD was posted to system Internal

SD. This information can help you to correct the errors and post the FWSD successfully.

The life cycle status indicates the current status of the FWSD in the business process. Important life cycle statuses are listed in the

following table:

Life Cycle Status

## In Process

Ready for Posting

## Posted

Posting Started

## Description

The FWSD has some incomplete or missing information.

The FWSD is ready for you to post to SD.

SD successfully created the billing document.

You posted the FWSD to SD to create a billing document and the

posting process is not yet finished.

## Cancellation Requested

You requested the cancellation of the FWSD from SD and the

cancellation is not yet finished.

This is custom documentation. For more information, please visit SAP Help Portal.

11


1/14/26, 2:42 PM

Life Cycle Status

Canceled

## Description

You canceled the FWSD. You also canceled the billing document in

SD.

## Canceled by Credit Memo

You created and posted a credit memo for the full amount of the

FWSD.

The confirmation status is used primarily to track the integration of FWSD with SD, and indicates the result of the last integration

interaction between TM and SD. Important confirmation statuses are listed in the following table:

Confirmation Status

Description

Not Yet Posted

Posting Successful

## Posting Failed

The FWSD is not yet posted to SD to create the billing document.

SD successfully created the billing document.

SD failed to create the billing document. You must manually check

why the billing document was not created.

## Cancellation Successful

SD successfully canceled the billing document.

Cancellation Failed

Posting Started

## Integration

SD failed to cancel the billing document.

You transferred the FWSD to SD and the status in SD is not yet

known.

The FWSD is integrated with a number of other components in TM, for example:

## Forwarding Order Management

You can start the generation of an FWSD from an FWO.

## Charge Management and Service Product Catalogs

The system calculates the transportation charges based on the setup of master data objects in the Charge Management

and Service Product Catalogs component, for example calculation sheets, rate tables, and scales.

## Agreement Management

The system can use the forwarding agreement to include master data objects for transportation charges in the order

process, such as calculation sheets or rate tables.

FWSD also integrates with SD to create the invoice that you send to the customer and also to post to financial accounting.

More Information

Forwarding Settlement

## Charge Calculation

Business Partner Determination

## Creation and Editing of Transportation Units

This is custom documentation. For more information, please visit SAP Help Portal.

12


1/14/26, 2:42 PM

Execution-Based Settlement

## Features

As a logistics service provider (LSP) or carrier, you need flexibility in how you settle for the transportation activities you carry out

on behalf of your customer. Transportation Management (TM) enables you to settle on the basis of individual forwarding orders as

standard. You can also settle on the basis of an execution criteria, such as buyer’s consolidation, route, or trailer unit.

## Buyer’s Consolidation

In a buyer’s consolidation scenario, you are an LSP and to keep the transportation costs low for your customer, you consolidate

and load the goods from different suppliers with whom your customer has an established business relationship, into one container

before the main carriage. This means you pass the full container load (FCL) rate for the main carriage and on-carriage to the

customer.

For more information, see Buyer's Consolidation Settlement.

## Execution-Based Criteria

In road transportation scenarios, you may also need to settle with your customer based on an execution unit such as a trailer unit,

or on execution attributes such as the type of vehicle used to provide the service, or on the distance a truck traveled to fulfill the

service.

For example, in a route-based settlement business scenario, your customer needs you to pickup goods from multiple locations

such as warehouses and distribution centers and deliver the goods to a series of customer locations or retail outlets. Your

customer wants to settle with you on the basis of an agreed rate for the full journey your truck makes as it performs the pickup and

delivery activities, and not on the basis of the individual forwarding orders that you execute during the journey. You need to use an

execution-based settlement criteria to enable this type of settlement.

## Settlement Basis in TM

You can specify a settlement basis for route-based and trailer-unit-based scenarios in the Settlement Basis field of an agreement

item.

By default, TM uses the information in an individual forwarding order to create forwarding settlement documents. For example, you

create a particular forwarding settlement document for a particular forwarding order. Using the settlement basis gives you the

flexibility to use different execution criteria to settle with your customers. You can settle based on how you executed the order and

not by individual forwarding orders.

The table explains some of the main differences between execution-based settlement and settlement based on individual

forwarding orders:

Execution-Based Settlement

Forwarding-Order-Based Settlement

## Settlement item

Execution document such as trailer unit or

Forwarding order

container

Resolution base grouping rule

In forwarding order

In execution document

Across forwarding orders in

execution document for execution

stages

This is custom documentation. For more information, please visit SAP Help Portal.

13


1/14/26, 2:42 PM

Execution-Based Settlement

Forwarding-Order-Based Settlement

Data source (stage and logistics quantities)

Execution document such as freight

As specified in settlement profile

booking item or trailer unit

In execution-based settlement, the system uses the stages from the freight order or trailer unit and not the constituent forwarding

orders to calculate the settlement amount. You can settle on the basis of route-based or trailer-unit-based settlement criteria. For

more information, see Route-Based Settlement and Trailer-Unit-Based Settlement.

When you specify a resolution base grouping rule in the basic data of a calculation sheet, the grouping rule applies to items in a

forwarding order. However, in the execution-based settlement scenario the item is a forwarding order. Therefore, the grouping logic

applies across forwarding orders that are part of the execution document. For more information on the resolution base grouping

rule, see Calculation Sheet.

## Constraints

You have specified the settings required for forwarding settlements. For more information, see Forwarding Settlement.

You have specified the appropriate settlement basis in the forwarding agreement item.

If FWO is settled on any of the execution-based settlements, the charges for the FWO for the execution-based stages are not

calculated in the individual FWO. The charges are only calculated in the forwarding settlement document. In the charge items for

the execution-based stages, the execution-based charge item is enabled in the charges tab.

## Example

You have 7 different forwarding orders that you deliver to a customer location on one trailer unit.

If you do not specify Trailer Unit in the Settlement Basis field, by default the system rates and settles each of the 7 forwarding

orders individually. If you create a collective settlement for the 7 forwarding orders, the system still bases the settlement on each

individual forwarding order. It performs the following tasks:

## Rates each of the forwarding orders individually

Creates one forwarding settlement document with each of the 7 forwarding orders specified as a line item in the settlement

In contrast, if you specify Trailer Unit in the Settlement Basis field of the relevant forwarding agreement, you execute the 7

forwarding orders in one trailer unit and you settle with your customer based on a rate for the trailer unit. This rate covers all 7

forwarding orders in the trailer unit.

Buyer's Consolidation Settlement

## Use

In a buyer’s consolidation scenario, you are a logistics service provider (LSP) or carrier and your customer regularly buys goods

from a number of suppliers in a particular country or region, and needs to transport them to a single location. Your customer needs

to keep transportation costs as low as possible and therefore requests you to do a buyer’s consolidation. To enable this, you can

consolidate and load the goods from the different suppliers into one container before the main carriage and deliver the

consolidated container to the customer’s location. This means you do not charge a less than container load (LCL) rate, and you

pass the full container load (FCL) rate for the main carriage and on-carriage to the customer.

This is custom documentation. For more information, please visit SAP Help Portal.

14


1/14/26, 2:42 PM
## Prerequisites

You specify the following settings to enable the system to settle for the charges in a buyer’s consolidation:

BCO (buyer’s consolidation) in the Buyer's or Shipper's Consolidation field of the forwarding order on the export side.

An agreement item for buyer’s consolidated transportation for main carriage and on-carriage. The agreement item includes

the following settings:

A separate calculation sheet for the buyer’s consolidation

BCO (buyer’s consolidation) in the Buyer's or Shipper's Consolidation field

## Features

## Settlement as a Variant of an Execution-Based Settlement

On the export side, the system bases the settlement charges for main carriage on the information from the freight booking

container item. The freight booking is the execution document and therefore the system settles for a buyer’s consolidation as a

variant of an execution-based settlement.

## Settlement Fallback

The system tries to find an agreement line item with a BCO (buyer’s consolidation) setting. If it does not find one, it tries to find an

agreement line with a shipping type of FCL (full container load). For more information, see Buyer's Consolidation.

## Settlement for Container Items

The system determines if the Buyer's or Shipper's Consolidation field in the freight booking for the container items has the BCO

(buyer’s consolidation) setting. If the setting exists, the system then creates one consolidated settlement for all the forwarding

orders in the container item for the main carriage.

## Example

In a buyer’s consolidation with an Incoterm of ExWorks (EXW), the ship-to party pays for all the transportation costs, including pre-

carriage, main carriage, and on-carriage.

The concept is illustrated in the following figure, and is followed by an explanation:

This is custom documentation. For more information, please visit SAP Help Portal.

15


1/14/26, 2:42 PM

For an Incoterm of EXW, on the export side there are multiple forwarding orders with one for each pickup location. The export

business unit creates a settlement document that bills the import business unit, for each of the following activities:

Pickup for forwarding order 1

Pickup for forwarding order 2

Pickup for forwarding order 3

## Main carriage

The system determines that the container item in the export freight booking has a buyer’s or shipper’s consolidation specification

of BCO for all three forwarding orders. The system uses the container information from the export freight booking to create a

single forwarding settlement document for the main carriage.

On the import side, the system automatically creates a copy of the forwarding order. This forwarding order contains a reference to

the container item for the buyer’s consolidation. The container item contains all the cargo information for the three forwarding

orders, including the pickup locations. The import business unit creates a settlement document on the ship-to party, for each of

the following activities:

Pickup for forwarding orders, using the cargo items in the container

Main carriage, using the cargo information for the container item

Delivery to the ship-to party, using the cargo information for the container item

## More Information

This is custom documentation. For more information, please visit SAP Help Portal.

16


1/14/26, 2:42 PM

Buyer's Consolidation (BCO) in Import/Export

Buyer's Consolidation

Execution-Based Settlement

Trailer-Unit-Based Settlement

## Features

You load a trailer with cargo items such as pallets and packages. The pallets and packages are from different forwarding orders

from your customer. According to the agreement, you want to settle for delivering the trailer unit and not for delivering individual

forwarding orders. You agree a set of rates that pass on to the customer the benefit of consolidating orders that have a common

destination into a single trailer unit.

For example, you agree a rate of USD 4,000 to deliver a trailer unit to a location. You use a single trailer unit to deliver 2 forwarding

orders (FWO1 and FWO2). FWO1 weighs 14,000 kg and FWO2 weighs 10,000 kg. You settle with the customer at the level of trailer

unit. The following table describes how the system calculates the settlement amount:

## Charge Type

Calculation (USD)

Charge (USD)

Trailer-unit charge

1 x 4,000

4,000

Settlement amount Not applicable

4,000

In contrast, for example, you agree with your customer that you do not settle on the basis of an execution criteria such as trailer

unit, and instead settle on the basis of each individual forwarding order (the default setting in the Settlement Basis field). The

following table describes how the system calculates the settlement amount:

## Charge Type

Calculation (USD)

Charge (USD)

Haulage FWO1

14,000 Kg X 0.2 cents / kg

Haulage FWO2

10,000 Kg X 0.2 cents / kg

Settlement amount for FWO1 and FWO2 Not applicable

2,800

2,000

4,800

More Information

Route-Based Settlement

Execution-Based Settlement

Route-Based Settlement

## Features

You can settle forwarding orders in a route-based settlement if you have a transportation journey with one or more pickups and

deliveries. A route-based settlement can accommodate the following business situations:

## Multiple pickup and single delivery

This is custom documentation. For more information, please visit SAP Help Portal.

17


1/14/26, 2:42 PM

Multiple pickups from plants or warehouses with a single delivery to an end location, such as a warehouse.

## Single pickup and multiple delivery

Pickup from a single location such as a distribution center and multiple deliveries to a series of locations such as retail

outlets or customer delivery locations.

## Multiple pickup and multiple delivery

Multiple pickups from locations such as warehouses and distribution centers followed by deliveries to customer locations

or retail outlets.

## Predefined start and end

Start from a specified location, pick up or delivery at scheduled locations, and return to the start location, or finish at a

specified end location.

The figure below illustrates a multiple pickup and multiple delivery scenario and is followed by an explanation:

The following table describes the transportation requirements for the 3 forwarding orders:

Forwarding Order Pickup Location

Delivery Location

FWO1

FWO2

FWO3

A

A

B

C

D

D

This is custom documentation. For more information, please visit SAP Help Portal.

18


1/14/26, 2:42 PM

The following table describes the planning output. In planning, you consolidate the forwarding orders into freight order FO1. You

use a 20-tonne truck.

From Location

To Location

Activity

Depot

A

B

C

A

B

C

D

Pickup FWO1 and FWO2 at location A

Pickup FWO3 at location B

Deliver FWO1 at location C

## Deliver FWO2 and FWO3 at location D

You agree to a settlement basis of route-based with your customer. The system charges for the 3 forwarding orders as follows:

Charge Type

Calculation

Charge (USD)

Base charge (as distance traveled times the

250 km X USD 1.20

rate per km)

Flat charge per truck (based on type of

USD 150 for a 20-tonne truck

truck)

Stop charge (number of stops times the

2 stops X USD 50 per stop

charge per stop)

Total freight cost

Not applicable

300

150

100

550

The system uses the information contained in freight order FO1, which executes the 3 forwarding orders, to create the forwarding

settlement. On the user interface, the system displays the amount of USD 550 in line 1 of the settlement document for freight

order FO1. It displays FWO1, FWO2, and FWO3 in the details screen with the full details for the journey.

## More Information

Trailer-Unit-Based Settlement

Execution-Based Settlement

Mixed Execution-Based Settlement

## Use

## Business Requirement

The business requirement is illustrated in the following figure, and is followed by an explanation:

This is custom documentation. For more information, please visit SAP Help Portal.

19


1/14/26, 2:42 PM

You are a carrier and your customer needs you to perform the following transportation tasks:

1. Pick up different cargo (different forwarding orders) from multiple locations

For example, you pick up cargo from customer suppliers who are based in different parts of your region.

2. Consolidate the cargo on a trailer to move it to a location as instructed by your customer

For example, you put the cargo on a trailer in a distribution center that your customer owns in a different region.

3. Deliver the cargo from the distribution center to other locations as instructed by your customer

For example, you deliver the cargo to different plants or retail outlets in the region.

4. Settle with the customer using a route-based settlement for the pick-up (pre-carriage) and delivery (on-carriage) stages.

Use a trailer-unit-based settlement to settle for the main carriage.

The following table describes the transportation requirements for the forwarding orders:

Forwarding Order

Source Location

Destination Location

FWO1

FWO2

A

B

D

E

You plan the following business documents in your system for FWO1 and FWO2:

Freight order 1 to pick up FWO1 and bring it to location C

This is custom documentation. For more information, please visit SAP Help Portal.

20


1/14/26, 2:42 PM

## Freight order 2 to pick up FWO2 and bring it to location C

Freight order 3 to pick up FWO1 and FWO2, now consolidated on a single trailer, and bring it from C to H

Freight order 4 to deliver FWO1 to location D

Freight order 5 to deliver FWO2 to location E

You use a small truck to pick up and deliver the forwarding orders.

You plan to include the following charge types in the settlement:

## Base freight

Calculated as distance traveled times the rate per km

## Flat charge per truck

Calculated based on the type of truck you use to execute the forwarding orders. This charge is not applicable for the main

carriage where the goods travel on a trailer.

## Base charge for trailer

Calculated as distance traveled times the rate per km for the type of trailer you use to execute the main carriage

## System Settings

You must specify the settings in the following table in the relevant forwarding agreement for your customer:

## Line Item

Stage Category

Settlement Basis

1

2

3

Pre-carriage

## Route

Main carriage

Trailer Unit

On-carriage

## Route

## Trailer Document for Main Carriage

You plan to move FWO1 and FWO2 on a single trailer between locations C and H in the main carriage. For more information on how

to plan a trailer, see Use of Trailers.

## Pre-Carriage and On-Carriage

You create the freight orders and plan for the pre-carriage and on-carriage stages of FWO1 and FWO2. For example, in the Actual

Route screen area of the forwarding order, you can select the relevant stage and choose  Freight Document

 Create . The

system adds the forwarding order to a freight order.

## Settlement Documents

When you create a forwarding settlement document for FWO1 the system creates 3 settlement documents for each of the

following documents:

Trailer document, for the main carriage of both FWO1 and FWO2

Pre-carriage of FWO1

On-carriage of FWO1

This is custom documentation. For more information, please visit SAP Help Portal.

21


1/14/26, 2:42 PM

When you create a settlement document for FWO2, the system creates 2 settlement documents as follows (it has already created

a settlement document for the main carriage, as the main carriage is part of the trailer-unit based settlement contained in FWO1):

Pre-carriage of FWO2

On-carriage of FWO2

To create a single settlement document for your customer for all the transportation activities, you can use the Collective option

under Create Forwarding Settlement Document when you select 2 or more forwarding orders on the forwarding order overview

screen.

## Charges

The system charges for the 2 forwarding orders as follows:

Distance and type of truck for A to C and for B to C, pre-carriage

Distance traveled by trailer for C to H, main carriage

Distance and type of truck for H to D and for H to E, on-carriage

The following table explains how the system applies the charges:

Forwarding Order Stage

## Charges

Calculation

Amount (USD)

Main carriage

Base freight

400 km X USD 1.20

480

Base charge for trailer

400 km X USD 0.20

Pre-carriage for FWO1

Base freight

50 km X USD 1.40

Flat charge for type of truck

USD 200

Pre-carriage for FWO2

Base freight

80 km X USD 1.40

Flat charge for type of truck

USD 200

On-carriage for FWO1

Base freight

30 km X USD 1.40

Flat charge for type of truck

USD 200

On-carriage for FWO2

Base freight

20 km X USD 1.40

Flat charge for type of truck

USD 200

80

70

200

112

200

42

200

28

200

## More Information

Execution-Based Settlement

Forwarding Settlement

## Use

In Transportation Management (TM), you can perform forwarding settlement with your ordering parties by creating a forwarding

settlement document (FWSD) and sending it to Sales and Distribution (SD) for creating the billing document (invoice) and posting

to financials.

This is custom documentation. For more information, please visit SAP Help Portal.

22


1/14/26, 2:42 PM
Prerequisites

## Agreements

You have the option of specifying the settlement basis at the agreement item level, where the system uses execution data

as the basis to perform invoicing. By default, the system uses the settlement basis at forwarding order level.

## Types of FWSD and number range intervals

In Customizing, you have defined types of FWSD as well as default types and number range intervals. For more information,

see Customizing for Transportation Management under  Settlement

 Forwarding Settlement

.

## Forwarding settlement profile

You have created a forwarding settlement profile in Customizing for Transportation Management under  Settlement

 Define Settlement Profile .

You have assigned the forwarding settlement profile to the charges profile that you assign to the sales organization that you

use in your forwarding order.

You can assign a forwarding settlement profile to a charge profile in Customizing for Transportation Management under

Basic Functions

 Charge Calculation

## Basic Settings

 Define Charges Profiles

 Set. Prof. (Forwarding Settlement

Profile)

. You can assign a charge profile to a sales organization in Customizing for Transportation Management under

## Master Data

 Organizational Management

## Organizational Model

 Change Organizational Model (transaction

PPOME)

. Select the relevant sales organization  Org. Data

 Detail Settings

 Charges Profile ID .

When the system creates a forwarding order, it checks for a forwarding settlement profile in the charges profile of the sales

organization.

If you do not specify a forwarding settlement in the charges profile, the system displays an error message when you create

a forwarding order.

## Calculation profile

You have specified a calculation profile in Customizing for Transportation Management under  Basic Functions

## Charge

Calculation

## Basic Settings

 Define Calculation Profiles . For more information about specifying calculation profiles,

see Calculation Profiles.

You can assign a calculation profile to a charge profile in Customizing for Transportation Management under  Basic

## Functions

 Charge Calculation

## Basic Settings

 Define Charges Profiles

 Calculation Profile .

You can assign a charge profile to a sales organization in Customizing for Transportation Management under  Master

## Data

 Organizational Management

## Organizational Model

 Change Organizational Model (transaction PPOME).

.

Select the relevant sales organization  Org. Data

 Detail Settings

 Charges Profile ID .

When the system creates a forwarding order, it checks for a calculation profile in the charges profile of the sales

organization.

If you do not specify a calculation profile in the charges profile, the system displays an error message when you create a

forwarding order.

## Process controller

In Customizing, you can set up the process controller for settlement documents. For example, if you want to use a strategy

to create or preprocess FWSDs differently than the standard way, you can define your own strategy using the process

controller and assign it to a specific service. For more information, see Customizing for Transportation Management under

## Settlement

 Configure Process Controller for Settlement

.

## Define default agreement partner functions for stages

This is custom documentation. For more information, please visit SAP Help Portal.

23


1/14/26, 2:42 PM

You have specified the agreement partner function for a stage type and Incoterm combination. When you specify an

Incoterm in a forwarding order (FWO), the system uses the agreement partner function to identify the default agreement

party for a stage. For more information, see Customizing for Transportation Management under  Forwarding Order

## Management

 Define Default Agreement Partner Functions for Stages .

## Master data for Charge Management

You have set up the master data in the Charge Management component. The system automatically calculates the

transportation charges based on this master data. For more information, see Charge Calculation.

## Business partner determination

You have the option of specifying a business partner determination profile, to enable the system to automatically assign

business partners to the settlement document. For more information, see Customizing for Transportation Management

under  Master Data

## Business Partners

 Define Partner Determination Profiles .

  Note

The system includes the bill-to party, sold-to party, and payer in the settlement document by default. The system does

not transfer business partners other than the sold-to party, the bill-to party and the payer to SD billing documents.

## Forwarding order

The system contains one or more forwarding orders (FWOs).

The system determines the logical system behind the business system group linked to the sales organization data of the

forwarding settlement document. The business system group indicates the ERP system from which the sales organization

is replicated in the organization model.

If this logical system is different to the current client logical system, the settlement document is posted to the external SD

using enterprise services. If the logical system is the same as the current client logical system, the settlement document is

posted to internal SD.

For more information on the organizational model see Customizing for Transportation Management under  Master Data

 Organizational Management

## Organizational Model

 Create and Merge Organizational Hierarchy .

## Integration settings for posting to SD

For integration to SD on an internal system, you have specified the relevant settings in Customizing for Transportation

Management under  Settlement

## Forwarding Settlement

 Settings for Posting Forwarding Settlements .

For integration to SD on an external SAP S/4 HANA or SAP ERP system, you have specified the relevant settings in

## Customizing under

Integration with Other SAP Components

 Transportation Management

  Invoice Integration

 Billing .

## Required execution status for settlement creation

As standard, you can create a forwarding settlement document at the following execution statuses in a forwarding order:

Execution Not Started

In Execution

## Executed

You can specify the execution status as follows:

In the relevant forwarding order type in Customizing for Transportation Management under  Forwarding Order

## Management

## Forwarding Order

 Define Forwarding Order Types

## Settlement Creation Status

In the relevant settlement profile type in Customizing for Transportation Management under  Settlement

## Define

## Settlement Profile

## Status for Settlement Creation

This is custom documentation. For more information, please visit SAP Help Portal.

24


1/14/26, 2:42 PM

If you don’t specify an execution status, the system does not take the execution status into account when it creates a

settlement document.

For example, you can use the Executed execution status setting of the forwarding order to settle the forwarding order.

You can also use the execution status as specified in a settlement rule as a basis for creating a forwarding settlement

document.

By default, the system includes the header-level charges with the stage-level charges in the first settlement document it

creates for a forwarding order.

## Process

1. You create the FWSD.

You can create an individual FWSD for one FWO or a collective FWSD for multiple FWOs. You can review the FWOs from your

personal worklist or in the Forwarding Order Management Overview or Forwarding Settlement Overview. The system

creates the FWSD based on the data in the FWOs and calculates the transportation charges.

You can also create settlement documents for the following FWOs:

FWO with Incoterms (see Incoterms in Forwarding Orders)

FWO with freight terms (see Freight Terms in Forwarding Orders)

The system uses certain criteria to divide settlements when you choose to create a collective settlement document. This

can result in the system creating more than one settlement. For more information, see Split Criteria in Settlement

Document Creation.

You can also create settlements for groups of charge types, charge categories, and charge subcategories from a forwarding

order. You can apply different settlement creation criteria to the different groups. You can define the factory calendar for the

billing schedule you want the system to use for a group of charges in a settlement group. This gives you control over when

you create settlements for different charges. For more information, see Flexible Creation of Forwarding Settlements.

  Note

You can create multiple forwarding settlement documents using the Creation of Forwarding Settlement Documents

function. For more information, see Creation and Transfer of Forwarding Settlement Documents.

2. You review the FWSD details.

You can preview the invoice as it would appear in SD. The preview contains information from the FWSD and tax information

determined from SD.

You can use the preview for FWSDs that are at all life cycle statuses except the following:

Posting Started

## Posted

Cancellation Requested

## Canceled

The consistency status of the document must also be Consistent. When you preview an invoice, the system does not

permanently store any data.

  Note

You can overwrite the address of the business partner that the system has automatically determined. For example, if you

need to send an invoice to a bill-to party at another address instead of the regular address, you can change the address

This is custom documentation. For more information, please visit SAP Help Portal.

25


1/14/26, 2:42 PM

of the bill-to party on the Business Partner tab page of the FWO or FWSD. When you post the settlement, the SD billing

document has the deviating address of the bill-to party in the SD billing document. For more information, see Creation of

a Forwarding Order.

3. You transfer the data to SD.

You choose Save and Post to send the FWSD to create the billing document in SD. If you have SD on an external SAP S/4

HANA or SAP ERP system, the system uses enterprise services to post between the systems.

4. SD confirms the billing document creation.

If SD created the billing document, you receive a confirmation from SD. The confirmation is displayed with the appropriate

status of the FWSD. The life cycle status changes to Posted.

If SD did not create the billing document, the confirmation status shows that posting failed. If posting is done to an internal

SD system, you must manually check in the Application Log tab of the settlement document for detailed messages about

why the invoice was not created. If you have SD on external SAP S/4 HANA or SAP ERP system, you must check the error

logs for the enterprise service message, in transaction SXI_MONITOR.

  Note
You can request that the FWSD is canceled at any time, even if its life cycle status is Posted. After you request cancellation of

the FWSD, SD cancels the billing document. If the billing document is canceled, the FWSD has the life cycle status Canceled. If

the billing document cannot be canceled, the FWSD has the confirmation status Cancellation Failed.

You can create an FWSD for a canceled FWO to recover any costs you incurred in processing the order before cancellation. You

must manually add the charges to the FWSD that is associated with the cancellation.

If you trigger the creation of an FWSD for an FWO that is a part of a buyer’s consolidation, the system takes the following steps:

Determines all the FWOs that are in the container item of the buyer’s consolidation

Creates one FWSD for the all the FWOs in the container item instead of individual FWSDs for each of the FWOs

If you trigger the creation of an FWSD for an FWO that has an execution-based settlement basis, the system creates one FWSD

for all the FWOs that are part of the relevant execution document for one customer. It bases the settlement on the execution

document instead of the individual FWOs.

For a settlement basis of trailer unit, the execution document is the trailer unit. For a settlement basis of route-based, the

execution document is a freight order.

## Tracking Manual Changes

If you make a manual change to an individual forwarding settlement document or internal settlement document, the system flags

the settlement document as manually changed.

The system regards changes to the following attributes in the forwarding settlement document as manual changes:

## Payment terms

Notes and attachments

## Charges

Invoice date

## Service date

This is custom documentation. For more information, please visit SAP Help Portal.

26


1/14/26, 2:42 PM

## Payer

## Deviating address for a bill-to business partner

You can view the manual change status on the personal object worklist for forwarding settlement documents.

## Creation Method

The system displays the approach you take when you create a forwarding settlement document or an internal settlement

document. The system displays the creation method on the POWL screen of the settlement document.

The system can display the following information:

## Manual

You have not previously created a settlement document for the forwarding order. You can manually create a forwarding

settlement document as follows:

Choose  Charges/Settlement

## Create Forwarding Settlement Document

Select one or more forwarding orders on the forwarding orders POWL screen, and choose the appropriate option

under Create Forwarding Settlement Document

## Background Processing

You use the Creation and Transfer of Forwarding Settlement Documents background processing function to create a

settlement document. You have not previously created a settlement document for the forwarding order and you have not

changed the forwarding order after previously creating a settlement document.

## Change and Background Processing

You have changed the associated forwarding order, enabled the relevant automatic change processing features, and run the

background processing function to create the forwarding settlement document.

## Follow-Up Forwarding Settlement Documents

You can create a second or subsequent forwarding settlement document after you have already created a settlement document.

When you create a follow-up forwarding settlement document, the system uses the following approach to propose the invoiced

amount:

1. Copy the charges from the forwarding order

Depending on the calculation option you specify in the relevant settlement profile, you can copy all the charge lines from

the order to the settlement as they are, or you can copy the fixed charges and recalculate the other charges.

For more information, see Customizing for Transportation Management under  Settlement

 Define Settlement Profile

.

2. Calculate the invoiced amount

The system takes the following steps:

For each charge line, subtract the invoiced amounts that are already included in the previously created but not

canceled forwarding settlement documents

Propose the result of the subtraction as the Invoiced Amount in the follow-up forwarding settlement document.

This can result in the following invoiced amounts in the follow-up settlement document:

An overall negative amount for the settlement document, where you have over-invoiced your customer

This is custom documentation. For more information, please visit SAP Help Portal.

27


1/14/26, 2:42 PM

## A zero amount where you have completely invoiced your customer

To prevent you from transferring the follow-up settlement document to Sales and Distribution until the zero or negative amount

has been removed, the system assigns a consistency status of Inconsistent to the follow-up settlement document.

You can perform the following tasks:

Run the background processing function to create and post settlement documents (program

/SCMTMS/CFIR_CREATE_BATCH) if you have enabled the change management process to correct the settlement

documents automatically.

Manually cancel the existing settlement document and replace it with a new settlement document that contains the

changed amount. The relevant forwarding order must not have a life cycle status of Completed.

Manually create a credit memo for the over-invoiced amount

More Information

Subject

## See

Create a buyer’s consolidation

Buyer's Consolidation

Create execution-based FWSDs

## Execution-Based Settlement

Determine business partners automatically

Business Partner Determination

Create, edit, and display a trailer unit

Creation and Editing of Transportation Units

Change management process for settlement documents

Automatic Change Management Process for Settlements

Determine a rate for a collective settlement document

Collective Rate Determination

Shipper's Consolidation Settlement

## Use

In a shipper’s consolidation scenario, you are a logistics service provider (LSP) or carrier and you have a single customer who

needs you to ship goods from a single location and deliver them to a number of different locations in a particular country or region.

Your customer needs to consolidate the goods over the pre-carriage and main carriage to optimize the freight cost. As an LSP, you

need to settle for the freight cost, including the main carriage cost, with your customer. You transport the goods in one container

for the pre-carriage and main carriage, and only separate the goods from the container for on-carriage delivery to the customer’s

location. You charge your customer a full container load (FCL) charge for the pre-carriage and main carriage.

## Prerequisites

You must specify the following settings to enable the system to settle for charges in a shipper’s consolidation:

SCO (shipper’s consolidation) in the Buyer's or Shipper's Consolidation field of the forwarding order on the export side

An agreement item for shipper’s consolidated transportation for pre-carriage and main carriage. The agreement item

includes the following settings:

## A calculation sheet for the shipper’s consolidation

This is custom documentation. For more information, please visit SAP Help Portal.

28


1/14/26, 2:42 PM

SCO (shipper’s consolidation) in the Buyer's or Shipper's Consolidation field

## Example

In a shipper’s consolidation with an Incoterm of Delivered Duty Paid (DDP), the seller (the shipper, your customer) pays for all the

transportation costs, including pre-carriage, main carriage, and on-carriage. To enable this, the system makes the shipper, ship-to

party, source location, and destination location information available for each item in the forwarding order.

The concept is illustrated in the following figure and is followed by an explanation:

For an Incoterm of DDP, on the export side, you create one forwarding order with one container item. In the container item, you

enter the cargo you collected from the single location that you deliver to different ship-to parties. The system uses the container as

the basis for creating the forwarding settlement. The export business unit creates a settlement document on the shipper, for each

of the following activities:

Pre-carriage

## Main carriage

On-carriage 1 in forwarding order 1 for item 1 in the container

On-carriage 2 in forwarding order 1 for item 2 in the container

On-carriage 3 in forwarding order 1 for item 3 in the container

This is custom documentation. For more information, please visit SAP Help Portal.

29


1/14/26, 2:42 PM

In the settlement document, the system includes each of the on-carriage stages for the individual cargo items from the forwarding

order.

On the import side, the system automatically creates a copy of the forwarding order for each of the on-carriages to the delivery

locations. The import business unit creates a forwarding settlement document on the export business unit, for each of the on-

carriages as follows:

On-carriage 1 in forwarding order 2

On-carriage 2 in forwarding order 3

On-carriage 3 in forwarding order 4

The system includes each of the individual on-carriage forwarding orders in the settlement document.

## More Information

Shipper's Consolidation (SCO) in Import/Export

Flexible Creation of Forwarding Settlements

## Use

You can create a forwarding settlement document for a group of charges in a forwarding order. This means that you can create

more than one forwarding settlement document for a forwarding order, where each settlement document is for a different group of

charges in the order. This enables you to create a settlement document for a group of charges that you want to settle at the same

time in your transportation process.

To enable this, you specify settlement groups and settlement rules in Customizing for Transportation Management under

## Settlement

 Define Settlement Groups and Settlement Rules .

You assign charge types, charge categories, and charge subcategories to a settlement group. You assign a settlement group to a

settlement rule. You can also specify the following additional criteria in a settlement rule:

## Minimum execution status

You can specify the minimum execution status required for a forwarding order before the system creates a forwarding

settlement document.

## Service date rule

You can specify the service date rule that the system uses to determine the service date of the forwarding settlement

document.

## Billing schedule

You can specify a factory calendar for the billing schedule that determines the settlement date for a settlement group.

When you create a forwarding settlement document, the system checks if a charge is contained in one of the charge types, charge

subcategories, or charge categories that you have assigned to a group. If it finds a charge, it creates the forwarding settlement

document according to the following criteria:

## Settlement group

The system creates a separate settlement for each settlement group.

This is custom documentation. For more information, please visit SAP Help Portal.

30


1/14/26, 2:42 PM

## Settlement rule

The system creates a separate settlement for a group of charges when a forwarding order is in a particular execution status

or when you reach a particular date.

Specifying settlement groups and settlement rules is optional. If you do not specify settlement groups, the system includes all the

charge types from a forwarding order in one forwarding settlement document.

For more information, see Customizing for Transportation Management under  Settlement

 Define Settlement Groups and

Settlement Rules .

## Prerequisites

## General Prerequisites

You have specified settlement groups, settlement rules, and assigned the necessary settlement groups to settlement rules

in Customizing for Transportation Management under  Settlement

 Define Settlement Groups and Settlement Rules .

You have assigned a settlement rule to a settlement profile. For more information, see Customizing for Transportation

Management under  Settlement

 Define Settlement Profile .

## Settlement Group Prerequisites

If you want to assign charge types to settlement groups, you have specified charge types in Customizing for Transportation

Management under  Basic Functions

 Charge Calculation

 Basic Settings

 Define Charge Types .

If you want to assign charge subcategories to settlement groups, you have specified charge subcategories in Customizing

for Transportation Management under  Basic Functions

 Charge Calculation

 Basic Settings

 Define Charge

Subcategories .

If you want to assign charge categories to settlement groups, you have specified charge categories in Customizing for

Transportation Management under  Basic Functions

 Charge Calculation

## Basic Settings

 Define Charge Categories

.

## Settlement Rule Prerequisites

If you want to use a service date rule, you have specified the necessary settings in Customizing for Transportation

Management under  Settlement

 Define Service Date Rules and Rule Prioritization .

If you want to specify a billing schedule, you have specified a factory calendar for a billing schedule in Customizing for

Transportation Management under  Master Data

## Calendar

 Maintain Factory Calendar

.

## Activities

Determine the following information:

## The set of charges you include in forwarding settlement documents

The set of charges you create settlements for after a forwarding order reaches a particular execution status

The set of charges you create settlements for at regular periods of time

## Example

## Business Requirements

This is custom documentation. For more information, please visit SAP Help Portal.

31


1/14/26, 2:42 PM

You need to settle the following charges:

Base freight

Fuel surcharge

## Demurrage

Other value added services (VAS)

You need to settle base freight and fuel surcharges together. You want to settle demurrage charges in a separate settlement so that

payment for base freight and fuel surcharge is not held up by disputes on the demurrage charges. You need to settle for the base

freight and other VAS charges every week, and for the demurrage charges every month.

You have the following business rules to determine the service date:

## Service date for demurrage charges is the system date

Service date for base freight, fuel surcharges, and other VAS is the pick-up date at the first location

You need to create settlement documents for basic freight charges (including base freight and fuel surcharges) and other VAS

charges when the forwarding order is in execution. You need to create settlement documents for demurrage charges when the

forwarding order has completed execution.

## Customizing Settings

You specify the following settlement groups in Customizing for Transportation Management under  Settlement

## Define

Settlement Groups and Settlement Rules :

## Basic freight charges

You assign the base freight and fuel surcharge charges to this group.

## Demurrage

You assign the demurrage charge to this group.

## Other VAS

You assign the charge types for VAS to this group.

You specify the settlement rule Standard Process Customer 1 that contains the following settings:

Line item 1 of the Assign Settlement Groups table:

Settlement group: Basic Freight Charges

## Execution status: In Execution

Service date rule: a rule that contains a date type of Actual Start Date of Complete Carriage at priority 1

Billing schedule: a weekly factory calendar

Line item 2 of the Assign Settlement Groups table:

Settlement group: Demurrage

Execution status: Executed

## Service date rule: leave empty

This is custom documentation. For more information, please visit SAP Help Portal.

32


1/14/26, 2:42 PM

The system uses the service date rule from the settlement profile. You must use a profile that contains an empty

service date rule (if the Service Date Rule field is empty, the system uses the system date).

Billing schedule: a monthly factory calendar

Line item 3 of the Assign Settlement Groups table:

Settlement group: Other VAS

## Execution status: In Execution

Service date rule: a rule that contains a date type of Actual Start Date of Complete Carriage at priority 1

Billing schedule: a weekly factory calendar

Freight Settlement

## Use

You use this component to trigger the accrual of the freight costs and to prepare for the verification of an invoice, received from a

service provider or carrier for transportation charges, against a freight document, such as freight orders, freight bookings, or

service orders.

In Transportation Management (TM), you can perform freight settlement with your service providers or carriers by creating a

freight settlement document and posting it to Materials Management (MM). The transportation charges are calculated in TM on

the basis of a freight order, freight booking, service order, or consignment order. TM relies on the integration to MM for the follow-

on processes in financials. The freight settlement document forms the basis of representing the freight document cost from TM to

MM. The information in the settlement document is used to create a purchase order and a service entry sheet (SES). The posting

of the SES confirmation forms the basis for invoice verification or the evaluated receipt settlement (ERS) process in MM.

  Note

Settlement and posting of freight costs for service orders are available only when you use Freight Settlement Integration using

MM External Services Management.

## Prerequisites

## Types of settlement document and number range intervals

In Customizing, you've defined freight settlement document types as well as default types and number range intervals. For

more information, see Customizing for Transportation Management under  Settlement

 Freight Settlement

.

## Freight settlement profile

You've created a freight settlement profile in Customizing for Transportation Management under  Settlement

## Define

Settlement Profile .

You've assigned the freight settlement profile as follows:

To the business partner and purchasing organization that you use in your freight order

You use the app Manage Business Partner Master Data to work with the business partner. Select the relevant

business partner

## Display in BP Role: Carrier

 Vendor Org. Data . Choose the relevant purchasing organization

Additional Settings

 FSD Profile ID .

For more information, see Business Partner.

This is custom documentation. For more information, please visit SAP Help Portal.

33


1/14/26, 2:42 PM

To the charges profile that you assign to the purchasing organization that you use in your freight order

You can assign a freight settlement profile to a charge profile in Customizing for Transportation Management under

Basic Functions

 Charge Calculation

## Basic Settings

 Define Charges Profiles

 Fre. Set. Prof. (Freight

Settlement Profile)

.

You can assign a charge profile to a purchasing organization in Customizing for Transportation Management under

## Master Data

 Organizational Management

 Organizational Model

## Change Organizational Model

(transaction PPOME). Select the relevant purchasing organization  Org. Data

 Detail Settings

 Charges Profile ID

.

When the system creates a freight order, it checks for a freight settlement profile as follows:

1. Business partner of the purchasing organization

2. Charges profile of the purchasing organization

If you don't specify a freight settlement profile in the business partner or in the charges profile, the system displays an error

message when you create a freight order.

## Calculation profile

You've specified a calculation profile in Customizing for Transportation Management under  Basic Functions

## Charge

Calculation

## Basic Settings

 Define Calculation Profiles . For more information about specifying a calculation profile,

see Calculation Profiles.

You've assigned the calculation profile as follows:

To the business partner of the purchasing organization that you use in your freight order

See  SAP Menu

## Logistics

 Transportation Management

## Master Data

## BP - Maintain Business Partner

(transaction BP). Select the relevant business partner  Display in BP Role: Carrier

## Vendor Org. Data . Choose

the relevant purchasing organization  Additional Settings

 Calculation Profile ID .

You can use the Manage Business Partner Master Data app to maintain the business partner. For more information,

see Business Partner.

To the charges profile that you assign to the purchasing organization that you use in your freight orders

You can assign a calculation profile to a charges profile in Customizing for Transportation Management under

Basic Functions

 Charge Calculation

## Basic Settings

 Define Charges Profiles

## Purch. Calc. Profile

(Purchasing Calculation Profile)

.

You can assign a charge profile to a purchasing organization in Customizing for Transportation Management under

## Master Data

 Organizational Management

 Organizational Model

## Change Organizational Model

(transaction PPOME). Select the relevant purchasing organization

## Org. Data

 Detail Settings

 Charges Profile

ID .

When the system creates a freight order, it checks for a calculation profile in the following objects:

1. Business partner of the purchasing organization

2. Charges profile of the purchasing organization

If you don't specify a calculation profile in the business partner or in the charges profile, the system displays an error

message when you create a freight order.

## Process controller

In Customizing, you can set up the process controller for use with settlement documents. For example, if you want to use a

strategy to create or preprocess settlement documents differently than the standard way, you can define your own strategy

This is custom documentation. For more information, please visit SAP Help Portal.

34


1/14/26, 2:42 PM

using the process controller and assign it to a specific service. For more information, see Customizing for Transportation

Management under  Settlement

 Configure Process Controller for Settlement

.

## Master data for charge management

You've set up the master data in the Charge Management component. The system automatically calculates the

transportation charges based on this master data. For more information, see Charge Calculation.

## Business partner determination

You have the option of specifying a business partner determination profile, to enable the system to automatically assign

business partners to a settlement document. For more information, see Business Partner Determination.

  Note

The system includes the invoicing party, carrier, and payee in the settlement document by default. The system doesn’t

transfer business partners other than the carrier, invoicing party, and payee to MM.

## Business document

The system contains one or more freight orders, service orders, or freight bookings.

## Integration

Freight Settlement is a subcomponent of Transportation Management (TM) and is integrated with the following TM

subcomponents:

Subcomponent

Integration Type

## Freight Order Management

Freight orders, freight bookings, and service orders provide the basis for the following

business documents:

Freight settlement documents

Credit memos for freight orders

## Charge Management and Service Product

As a prerequisite for creating a freight settlement document, you must create the relevant

## Catalogs

charge management master data.

This component prepares the freight settlement document for invoice verification and relies on the integration with Materials

Management (MM) using External Services Management or Lean Services for posting accruals and verifying invoices. For more

information, see:

Freight Settlement Integration using MM External Services Management.

Freight Settlement Integration using Lean Services.

Freight Settlement Integration using MM External Services
## Management

In Transportation Management (TM), you can perform freight settlement with your service providers or carriers by creating a

freight settlement document and posting it to Materials Management (MM) using external services management.

## Prerequisites

This is custom documentation. For more information, please visit SAP Help Portal.

35


1/14/26, 2:42 PM

You've enabled the checkbox TM Settlement Integration based on MM External Services Mgmt in the Customizing of

Transportation Mangement under  Basic Functions

## General Settings

## Define General Settings for TM . This setting

ensures that you've enabled external service-based integration to Materials Management (MM).

To integrate to an internal MM system, you've configured the following Customizing settings:

Assign Purchasing Information for Posting

Assign Service Master Record and Account Assignment Category

## Tax determination settings under Tax

Mapping for cost distribution in a shipper scenario, when you've enabled cost distribution in the freight settlement

document

For more information, see Customizing for Transportation Management under  Settlement

## Freight Settlement

 Integration for Settlement Posting

  External Services Management

.

To integrate to an external MM system on SAP S/4HANA or SAP ERP, you've made the relevant settings in the Customizing

activities under

Integration with Other SAP Components

 Transportation Management

## Invoice Integration

 Invoicing  in the external SAP ERP or SAP S/4HANA system.

The system determines the logical system behind the business system group that you've linked to your purchase

organization data for the freight settlement document. The business system group represents the SAP ERP or another SAP

S/4HANA system from which you replicate the purchasing organization in the organization model.

If the logical system is different to the current client logical system, the system uses enterprise services to post the

settlement document to an external MM system. If the logical system is the same as the current client logical system, the

system posts the settlement document directly to an internal MM system. For more information about organizational

models, see Organizational Management.

## Company code and Plant

For more information, see Company Code and Plant in Posting Freight Settlements.

## Process

1. You create the freight settlement document.

Note the following system features:

You can create an individual settlement document for a freight order, service order, or freight booking, or a collective

settlement document for multiple freight orders, service orders, or freight bookings. You can access freight orders,

service orders, or freight bookings from your personal worklist, in the relevant document overview, or in the Freight

Settlement Overview. The system automatically creates the settlement document on the basis of the data in the

freight orders, service orders, or freight bookings and calculates the transportation charges.

You can create multiple freight settlement documents using the Mass Creation of Freight Settlement Documents

function. You can run transaction /SCMTMS/SFIR_CREATE (report /SCMTMS/SFIR_CREATE_BATCH). For more

information, see Creation and Transfer of Freight Settlement Documents.

You can create settlement documents for individual stages in freight orders that contain non-linear stages. This

means you can create a settlement document for each pairing of a source location and destination location. For

more information, see Freight Orders with Non-Linear Stages.

You can create separate freight settlement documents for each of the invoicing carriers in a rail freight order, where

you have a different invoicing carrier for each stage in the order. This feature gives you the flexibility to work with rule

11 business situations in North America.

This is custom documentation. For more information, please visit SAP Help Portal.

36


1/14/26, 2:42 PM

In rule 11 situations, the header carrier receives the order from the customer and can execute one or more of the

stages. The header carrier is the carrier that you specify in the  General Data

 Transportation  screen area of the

freight order. The invoicing carrier is the carrier who bills the customer for the shipment. This is the carrier that you

specify at stage level in the rail freight order.

For more information about rail freight orders, see Rail Transportation.

You can create a settlement document for each additional agreement party if you have an existing freight order or

freight booking that contains one or more additional agreement parties. For more information, see Additional

Agreement Parties.

The system uses certain criteria to split settlements when you choose to create a collective settlement document.

This can result in the system creating more than one settlement. For more information, see Split Criteria in

Settlement Document Creation.

The system settles a parcel freight order in the same way as it settles a standard freight order. For more information

about parcel freight orders, see Parcel Shipment.

When you create a freight settlement document, by default the system uses today's date as the settlement date. You

have the following options to manually override the system default:

Implement BAdI: Determination of Settlement Date for Freight Settlement Documents. The system uses

the settings that you specify in this BAdI to determine the settlement creation date. For more information,

see Customizing for Transportation Management under  Business Add-Ins (BAdIs) for Transportation

Management

## Settlement

 Freight Settlement

.

Enter a settlement date in the Mass Creation of Freight Settlement Documents background processing

function. The system uses the date that you specify in this background function as the settlement date if you

haven't specified a rule in the BAdI.

2. You review the settlement document details for consistency.

You can review the settlement document details to check their accuracy and you can update some of the data as needed.

After you save any changes you make, you can check the consistency of the settlement document. If the automatic

consistency check is successful, the system changes the consistency status of the settlement document to Consistent and

the lifecycle status of the settlement document to Ready for Accruals.

3. You post the settlement document to MM to post accruals.

Note the following system features:

TM sends the settlement document data to MM when you choose Post. TM transfers the settlement information,

including the source location and destination location information for each stage in the settlement, to MM. The

location information enables MM to determine different tax rates for different locations, countries/regions in the

purchase order item or, if enabled, in the service item.

When the SES is accepted and posted, accruals are booked to accounting. The SES serves as the basis for invoice

verification in MM.

The settlement date from the freight settlement document is used as the Doc. Date (Document Date) in the header

of the purchase order.

The SES dates on the header of the Accept. Data (Acceptance Data) tab page are taken from the following places:

Posting date from the settlement date in the freight settlement document

Document date as the system date

## Posting Periods

This is custom documentation. For more information, please visit SAP Help Portal.

37


1/14/26, 2:42 PM

You can post the freight settlement document only if the posting periods in MM and Financial Accounting (FI) are

both open for the posting date of the SES. If the posting period is closed, you have the following options:

## Open the closed posting period

You must open the posting period for both MM and FI.

In FI, open the posting period in Customizing under  Financial Accounting

 Financial Accounting Global

Settings

## Ledgers

 Fiscal Year and Posting Periods

## Posting Periods

 Open and Close Posting Periods

.

In MM, open the posting period in the SAP Menu under  Logistics

 Materials Management

 Material

Master

## Other

 MMPV – Close Period  or MMRV - Allow Posting to Previous Period.

Change the settlement date of the freight settlement document to match the open posting period and post

the settlement document again.

In TM, you can have multiple charge types in a charge item. As standard, MM creates a purchase order item for a

charge item, and applies tax to the purchase order item. If you need the flexibility to apply tax to individual charge

types in a charge item, you must specify the settings in the following Customizing activities in Customizing for

Transportation Management under  Settlement

## Freight Settlement

 Integration for Settlement Posting

 Tax

:

## Define Tax at Charge Type Level for Countries/Regions

You can define the countries/regions in which you apply tax at charge type level.

## Assign Tax Indicators for Charges

You can define tax indicators for the charge categories, charge subcategories, and charge types that you use

in a country/region. You can use charge categories and charge subcategories to specify tax settings for a

group of charge types in one step. This avoids the need to specify tax settings for a large number of individual

charge types.

For more information, see Customizing for Transportation Management under  Settlement

 Freight

## Settlement

 Integration for Settlement Posting

  External Services Management

 Tax . Also see SAP

Note 2622403

.

4. When the settlement document is posted successfully, its lifecycle status is set to Posted. If issues are encountered during

posting, the lifecycle status is set either to In Process or Posting Started, and the confirmation status has the status of the

corresponding step in which the issue was encountered. For example, the confirmation status Accruals Failed means that

the entire FSD posting encountered an issue, or the status SES Posting Failed indicates that the purchase order was

created successfully but the SES creation and posting failed.

If you encounter issues when you post to internal MM, the system logs the issues. You can review the issues on the

Application Log tab of the settlement document.

5. Invoice verification and Evaluated Receipt Settlement (ERS)

MM bases the expected invoice on the SES confirmation. When the invoice is posted against the freight document,

the invoice values are updated to the freight settlement document and the lifecycle status of the settlement

document is set to Invoice Verified.

The automatically generated invoice is based on the data from the settlement document, if you perform ERS.

  Note

You can edit the settlement document until the point at which it's posted to MM.

You can't cancel the settlement document when the invoice is posted against the settlement document in MM and the

settlement document has a lifecycle status of Invoice Verified.

This is custom documentation. For more information, please visit SAP Help Portal.

38


1/14/26, 2:42 PM

When you successfully cancel the settlement document, the posting date of the canceled SES is determined as follows:

a. Original posting date of the SES, if both the MM posting period and FI posting period are open on the original

posting date.

b. Cancellation date of the freight settlement document if both the MM posting period and FI posting period are

open on the cancellation date.

More Information

## Subject

## More Information

Enable the system to determine the business partners that you use

Business Partner Determination

in different business document types.

Change management process for freight settlements

Automatic Change Management for Freight Settlements

## Verify Invoices for TM documents

Integration: Invoice Processing (MM-IV/SD-BIL) with TM

Perform self-billing for suppliers for TM documents

Evaluated Receipt Settlement (ERS) (LO-INT-TM)

Make certain changes to your freight costs in the freight order,

## Changes After Posting

freight booking, or service order after you post accruals

Allow for unplanned changes in your freight settlement process

## Reversing a Freight Settlement Document

Work with collective freight settlement documents, to combine the

Split Criteria in Settlement Document Creation

settlements for freight documents into a single freight settlement

document

Determine a rate for a collective settlement document

Collective Rate Determination

## Freight Settlement Document

A freight settlement document is a document that is used for posting the freight cost accruals, and that forms the basis of invoice

verification in Materials Management (MM) for freight documents such as freight orders, freight bookings, and service orders.

## Use

The transportation charges are calculated in Transportation Management (TM) on the basis of a freight order, service order, or

freight booking. TM relies on the integration to MM for the follow-on processes in financials. The freight settlement document

forms the basis of representing the freight document cost from TM to MM. On posting the freight settlement document, a

purchase order for services and a service entry sheet (SES) is created with the values from TM charge lines copied to these

business documents. The SES confirmation also is done simultaneously, which creates the necessary financial entries for the value

of the freight cost.

When the invoice is received, logistics invoice verification in MM checks it against the data replicated in MM from the freight

settlement document. If you perform evaluated receipt settlement, the automatically generated invoice is also based on the data

replicated in MM from the freight settlement document.

You can create an individual freight settlement document for one freight order, service order, or freight booking. You can create a

collective freight settlement document for multiple freight orders or freight bookings. You can also create multiple freight

settlement documents at the same time.

This is custom documentation. For more information, please visit SAP Help Portal.

39


1/14/26, 2:42 PM
## Structure

The freight settlement document data is taken from the business documents (for example, freight orders). However, you can still

change some of the data.

The freight settlement document contains the following tab pages:

## General Data

The system displays general data, such as the following:

Settlement document type

Settlement date

## Procuring company code

Purchasing organization and purchasing group

Payment terms

## Net amount

Document currency

## Verified invoice amount

You can change some of the data, such as the settlement date and payment terms.

## Business Partner

The system displays the carrier, invoicing party, and payee by default. You can use business partner determination to

specify how the system assigns business partners to freight settlement documents.

## Charges

The system displays the transportation charges for each freight settlement document item. The freight settlement

document item could be either referring to a business document (that is, freight order, service order, or freight booking), or

to individual items of the business document, depending on the calculation level settings in the calculation profile. For more

information about the calculation profile, see Customizing for Transportation Management under  Basic Functions

 Charge Calculation

## Basic Settings

## Define Calculation Profiles . In the case of collective freight settlement

documents, the system shows the total amount for all the freight orders, service orders, or freight bookings assigned to the

freight settlement document.

## Orders

The system displays the list of business documents or business document items that are being settled with this freight

settlement document, depending on the calculation level settings in the calculation profile. The list of all the freight orders,

service orders, or freight bookings assigned to the freight settlement document is shown.

## Document Flow

The system displays the predecessor and successor business documents as a document flow, including the corresponding

MM documents, such as the purchase order, SES, and invoice. You can access the business documents from the Document

Flow tab of the document.

## Application Log

The system displays any error or warning messages that were encountered when the freight settlement document was

posted to an internal MM system. This information can help you to correct the errors and post the freight settlement

document successfully.

This is custom documentation. For more information, please visit SAP Help Portal.

40


1/14/26, 2:42 PM

The life cycle status indicates the current status of the freight settlement document in the business process. Important life cycle

statuses are listed in the following table:

Life Cycle Status

Description

## In Process

The freight settlement document is not yet ready to be posted to MM.

## Ready for Accruals

The freight settlement document is ready for you to post accruals in MM.

## Posting Started

You have initiated posting of the freight settlement document and the freight settlement

document posting process is not yet complete.

## Posted

The freight settlement document has been posted successfully and the purchase order

(PO) and service entry sheet (SES) have been created in MM.

## Invoice Verified

At least one invoice has been posted against the freight settlement document in MM.

## Cancellation Requested

You requested the cancellation of the freight settlement document but the cancellation

process is not yet complete.

## Canceled

You canceled the freight settlement document.

## Reversal Requested

You have requested the reversal of the freight settlement document but the process of

posting the reversal is not yet complete.

## Reversed

The freight settlement document document has been successfully reversed in MM.

## Credit Memo Created

A credit memo has been posted against a reversed freight settlement document in MM.

The confirmation status is used primarily to track the posting status of the freight settlement document to MM, and indicates the

result of the last posting status. Important confirmation statuses are listed in the following table:

Confirmation Status

Description

## Not Posted

The freight sdettlement document is not yet posted to MM.

## Not Confirmed

The freight settlement document posting has been initiated but is not yet complete.

## Confirmed

## Posting Failed

The freight settlement document has been posted successfully to MM.

The posting of freight settlement document is not successful in MM.

## Cancellation Posting Failed

The cancellation posting of freight settlement document is not successful in MM.

## No Confirmation

You posted the freight settlement document to MM but and the status in MM is not yet

known.

## Reversal Failed

The reversal posting of the freight settlement document failed.

## Purchase Order Creation Failed

The creation of the purchase order failed when the freight settlement document was

posted. For information about the error, see the Application Log tab in the freight

settlement document.

## SES Creation Failed

The creation of the SES failed when the freight settlement document was posted. For

information about the error, see the Application Log tab in the freight settlement

document.

## SES Cancellation Failed

The cancellation of the SES failed when the freight settlement document was canceled. For

information about the error, see the Application Log tab in the freight settlement

document.

This is custom documentation. For more information, please visit SAP Help Portal.

41


1/14/26, 2:42 PM

Confirmation Status

## Description

## Purchase Order Cancellation Failed

The cancellation of the purchase order failed when the freight settlement document was

canceled. For information about the error, see the Application Log tab in the freight

settlement document.

## Cost distribution document creation failed

The creation of the settlement management documents with the cost distribution data

failed when the freight settlement document was posted. For information about the error,

see the Application Log tab in the freight settlement document.

## Cost distribution document cancellation

During the cancellation of the freight settlement document, the cancellation posting of

failed

settlement management documents with the cost distribution data failed. For information

about the error, see the Application Log tab in the freight settlement document.

## SES Reversal failed

During the reversal posting of the freight settlement document, the creation of the SES

failed. For information about the error, see the Application Log tab in the freight

settlement document.

## Cost distribution document reversal failed

During the reversal of freight settlement document, the reversal posting of settlement

management documents with the cost distribution data failed. For information about the

error, see the Application Log tab in the freight settlement document.

## Integration

The freight settlement document is integrated with a number of other components in TM, for example:

## Freight Order Management

You can start the generation of a freight settlement document from a freight order, service order, or freight booking.

## Charge Management and Service Product Catalogs

The system calculates the transportation charges based on the setup of master data objects in the Charge Management

and Service Product Catalogs component, for example calculation sheets.

## Agreement Management

The system can use the freight agreement to include master data objects for transportation charges in the order process,

such as calculation sheets or rate tables.

The freight settlement document also integrates with MM to create the purchase order (PO) and service entry sheet (SES)

to post accruals, and to be the basis for invoice verification.

More Information

Freight Settlement

## Charge Calculation

Business Partner Determination

## Reversing a Freight Settlement Document

In your business you are a requester of transportation services, such as a shipper, and you have a close working relationship with a

provider of transportation services, such as a carrier. You have enabled a self-billing (evaluated receipts settlement) process with a

This is custom documentation. For more information, please visit SAP Help Portal.

42


1/14/26, 2:42 PM

particular service provider. You automatically pay the service provider according to the charge details in your freight order, freight

booking, or service order.

Occasionally you can have the following business scenario:

1. Your carrier started to execute your transportation request.

2. You accrued the freight cost in Materials Management (MM).

3. You created a self-billing invoice to update the open item in your accounts payable.

Then your carrier encounters some unplanned issues. For example, the carrier does not deliver a particular transportation service

due to execution issues such as a vehicle breakdown. Also, you may encounter incorrect pricing information in Transportation

Management (TM)..

To resolve the issues, you need to reverse the freight settlement document in TM. When you transfer the reversal to MM, you need

to reverse the associated purchase order, service entry sheet (SES), and accruals posting in MM. You need MM to then run the

evaluated receipts settlement for the particular freight order. This posts a credit memo that reverses the self-billing invoice that

was created earlier. You can only reverse the freight settlement document when it has the life-cycle status Invoice Verified.

The following table describes the steps you must take to reverse the freight settlement document:

Module

TM

MM

MM

Action

## Result

Life-Cycle Status of FSD

Choose Reverse Document in

TM initiates the reversal

Reversal Requested

the freight settlement

process. The system creates an

document.

SES with a returns flag, for the

complete value of the freight

settlement document.

System creates an SES in which

System creates the reversal

## Reversed

it automatically enables the

posting for the accruals in MM.

returns indicator.

You run transaction MRRL

This creates a credit memo to

## Credit Memo Created

(Evaluated Receipt Settlement

reverse the previously posted

(ERS) with Logistics Invoice

invoice.

Verification). Under the

Transportation Management

screen area, you enter the

relevant TM freight order

number.

TM updates the invoicing status of the relevant freight order to Not Invoiced, and you can create a new freight settlement

document for the freight order.

## Related Information

Evaluated Receipt Settlement (ERS)

## Company Code and Plant in Posting Freight Settlements

The company code in the freight settlement process is used to book the freight accruals to financial accounting (FI) under the

company code. The plant is required in the posting process during the creation of the service purchase order as part of the posting

step for a freight settlement document.

This is custom documentation. For more information, please visit SAP Help Portal.

43


1/14/26, 2:42 PM

## Procuring Company Code

The procuring company code is responsible for the procurement of a transportation service from the carrier or transportation

service provider of a freight document. The procuring company code is available in the freight document under  General Data

 Organizational Data .

If a unique company code has been assigned to a purchasing organization, the system uses this company code automatically as

the procuring company code of the freight document. If the system cannot determine a unique company code, the field remains

empty. Procuring company code determination is enabled only when you have specified in Customizing for the freight order type,

freight booking type, or consignment order type that the freight document is relevant for subcontracting and have specified in

Customizing for the freight order type, freight booking type, or service order type in the Subcontract. Checks field that the system

is to perform basic additional checks.

If the procuring company code is defined in the freight document, it is transferred to the freight settlement document.

When the freight settlement document is posted, the system determines the company code and plant as follows during the

creation of the service purchase order and the service entry sheet (SES):

## Company Code

The system determines the company code as follows:

Procuring company code available in the freight settlement document header

Procuring company code of the plant that is specified in Customizing for Transportation Management under

## Settlement

## Freight Settlement

 Integration for Settlement Posting

 Assign Purchasing Information for

Posting  to integrate to an internal Materials Management (MM) system.

To integrate to an external MM system on SAP S/4 HANA or SAP ERP, see the Customizing activities under

Integration with Other SAP Components

 Transportation Management

 Invoice Integration

## Invoicing

 Mapping of Organizational Units .

## Plant

The system determines the plant to be populated in the purchasing order item as follows:

The plant specified at freight settlement document type Customization to determine the plant and procuring

company code. For more information see, Customizing for Transportation Management under  Settlement

## Freight Settlement

 Integration for Settlement Posting

  Assign Purchasing Information for Posting

## Assign

Purchasing Information for Posting  to integrate to an internal MM system.

To integrate to an external MM system on SAP S/4 HANA or SAP ERP, see the Customizing activities under

Integration with Other SAP Components

 Transportation Management

 Invoice Integration

## Invoicing

 Mapping of Organizational Units .

The plant from the underlying transactions (orders and deliveries) if they are all unique from the linked freight units

in the freight document.

Use the plant defined as the default plant for the company code in Customizing for Transportation Management

under  Settlement

## Freight Settlement

 Integration for Settlement Posting

 Assign Default Plant for

Company Code  to integrate to an internal MM system.

To integrate to an external MM system on SAP S/4 HANA or SAP ERP, see the Customizing activities under

Integration with Other SAP Components

 Transportation Management

 Invoice Integration

## Invoicing

 Mapping of Organizational Units .

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

44


1/14/26, 2:42 PM

If you have enabled in Customizing for the freight order type, freight booking type, or consignment order type that the freight

document is relevant for subcontracting and in the Subcontract. Checks field that the system is to perform Basic Additional

Checks, the company code is mandatory in the freight document and the same is taken over into the freight settlement

document. In this case, SAP recommends that you don't specify the plant in the Customizing activity Assign Purchasing

Information for Posting. This allows the plant to be determined (as described above) during the freight settlement document

posting. This allows the company code and plant to be determined more flexibly and not to be tied to the freight settlement

document type.

Related Information

## Company Codes

Changes After Posting

## Changes After You Post Accruals

You can include certain changes in the freight costs of a freight order, freight booking, or service order after you post accruals.

You can add or change charge amounts directly in the existing freight order, freight booking, or service order. You can transfer

these changes in the freight costs to Materials Management (MM).

If automatic change management is enabled, you can use the background function Creation and Transfer of Freight Settlement

Documents (program /SCMTMS/SFIR_CREATE_BATCH) to create, change, and post freight settlement documents to MM (see

Creation and Transfer of Freight Settlement Documents using Integration with MM External Services Management). The freight

settlement document contains the changes from the freight order. For more information, see Automatic Change Management for

Freight Settlements.

  Note

If automatic change management isn't enabled, the following conditions apply:

If the new or changed amount results in the invoicing status of the freight order changing to Partially Invoiced, you can

create a new freight settlement document to post the changed amounts to MM.

If the new or changed amount results in the invoicing status of the freight order changing to Over Invoiced, you can

create a credit memo in TM to send the changed amounts to MM.

If you don't want to create a new settlement document or credit memo, you can cancel the existing settlement

document provided the life-cycle status of the settlement document isn't Invoice Verified. You can then create a new

settlement document that contains the complete amount including the changes.

When you post the credit memo or the new settlement document to MM, a new purchase order and service entry sheet (SES)

are created.

## Follow-Up Freight Settlement Document

If automatic change management is not enabled, you can create a second or subsequent freight settlement document after you

have already created a settlement document. You can transfer these changes in the freight costs to Materials Management (MM)

as follows::

1. Copy the charges from the freight order

Depending on the calculation option you specify in the relevant settlement profile, you can copy all the charge lines from

the order to the settlement as they are, or you can copy the fixed charges and recalculate the other charges. For more

This is custom documentation. For more information, please visit SAP Help Portal.

45


1/14/26, 2:42 PM

information, see Customizing for Transportation Management under  Settlement

 Define Settlement Profile .

2. Calculate the invoiced amount

The system takes the following steps:

For each charge line, subtract the invoiced amounts that are already included in the previously created but not

canceled freight settlement documents

Propose the result of the subtraction as the Invoiced Amount in the follow-up freight settlement document

This can result in the following invoiced amounts in the follow-up settlement document:

An overall negative amount for the settlement document, where you have over-accrued costs for your carrier or

logistics service provider (LSP)

A zero amount where you have completely accrued the costs for your carrier or LSP.

To prevent you from posting the settlement document to MM until the zero or negative amount has been removed, the

system assigns a consistency status of Inconsistent to the settlement document.

You can run the background processing function to create and transfer settlement documents (program

/SCMTMS/SFIR_CREATE_BATCH) if you have enabled the change management process to correct the settlement

documents automatically

If you have not enabled the automatic change management process, you can perform the following tasks:

Manually cancel the existing settlement document and replace it with a new settlement document that contains the

changed amount. The relevant freight order must not have a life cycle status of Completed.

Manually create a credit memo for the over-accrued amount.

## Related Information

Automatic Change Management for Freight Settlements

Posting of Allocated Freight Costs in an Advanced Intercompany
## Business Process

You can use a freight order or freight booking to transport cargo in a business process for advanced intercompany sales or

advanced intercompany stock transfer.

The responsibility for the freight cost depends on the Incoterms that are in place between the relevant companies. In an advanced

intercompany sales process, the responsibility is with the delivering and selling company. In an advanced intercompany stock

transfer process, the responsibility is with the delivering and receiving company.

The system uses the responsibility for the logistics stage of the freight unit to determine the paying company code, based on the

incoterms of the stock transfer order or the intercompany sales order. The procuring company code of the freight order or freight

booking can be that of the delivering, selling, or receiving company.

The system posts the allocated freight costs to expenses or material valuation in financial accounting based on the answers to the

following questions:

Which company code is responsible for the freight cost?

Is the freight cost part of an advanced intercompany sales or advanced intercompany stock transfer process?

Is this company the delivering, receiving, or selling company code?

This is custom documentation. For more information, please visit SAP Help Portal.

46


1/14/26, 2:42 PM

The system posts the freight cost allocation to expenses or to a material account if the material is relevant for valuation in financial

accounting.

The following graphic outlines an example of an advanced intercompany stock transfer order, and is followed by an explanation:

In an advanced intercompany stock transfer process, you can transfer stock between different legal entities in a corporate group.

You can transfer stock from one plant to another if the plants belong to different company codes.

For example, a receiving company, 1010, located in Germany, needs a product that is manufactured by another legal entity in the

United States (U.S.). A purchasing organization in the receiving company creates an intercompany purchase order in the receiving

company, where the supplier represents a plant that is part of a different company code, in this case, in the U.S.

The contractual agreement with the internal supplier for the internal business is stored in the intercompany purchase order in the

receiving company. This includes the Incoterms that define the terms of sale and the passing of risk for the importation and

exportation of the goods.

In our example, the Incoterm in the intercompany purchase order is Free on Board (FOB). This means the delivering company is

responsible for organizing and paying the transportation of the goods from its plant to the port of departure, and for loading the

goods on the ship. The receiving company is responsible for organizing the transport and paying from the port of departure to the

final destination at its receiving location.

For an example of an advanced intercompany sales process, see Transportation Management in Advanced Intercompany Business

## Processes

## Advanced Intercompany Sales

For more information about this process, see Advanced Intercompany Sales.

The system uses the Incoterms agreed between the delivering company and selling company to determine the responsibility for

the freight costs. It posts the distributed costs as follows:

In the delivering company, as an expense for the intercompany sales order item (see step 4 in Advanced Intercompany

Sales) and the outbound delivery item (see step 5).

This is custom documentation. For more information, please visit SAP Help Portal.

47


1/14/26, 2:42 PM

In the selling company as an expense for the standard sales order item (see step 2) and the outbound delivery item (see

step 5).

## Advanced Intercompany Stock Transfer

For more information about this process, see Advanced Intercompany Stock Transfer.

The system uses the Incoterms agreed between the delivering company and receiving company to determine the posting of the

freight cost. It determines the posting of the freight cost in the delivering company as an expense because the freight movement is

outbound for the intercompany sales order item (see step 4 in Advanced Intercompany Stock Transfer) and the outbound delivery

item (see step 5).

If the material being transported is relevant for valuation in the delivering company, and you have enabled group valuation in

universal parallel accounting, the system also posts the freight cost in the group valuation ledger of the delivering company code

that is considered for group valuation. For more information about a group valuation ledger, see 3191636

.

## Prerequisites

To enable freight cost posting with freight cost allocation for an advanced intercompany sales and an advanced intercompany

stock transfer process, you must specify the following settings:

Freight cost allocation creation criteria of always by settlement documents in Customizing for Logistics – General under

Settlement Management

## Basic Settings

 Specify Extended Scope of Settlement Management

.

Criteria for creating settlement management documents in Customizing for Transportation Management under

## Settlement

## Freight Settlement

 Integration for Settlement Posting

 Mapping for Cost Distribution

## Posting Using

## Settlement Management

 Basic Settings for Creation of Settlement Management Documents . You must specify the

following settings:

## Document Category: always specify 1 Settlement

For the settlement process type, choose the delivered standard process type 2TME – Freight Cost Allocation

(Expense) and a use case type of 31 Freight Cost Distribution on G/L Account. Also choose a settlement process

type of 2TMM – Freight Cost Allocation (ML-Account) and a use case type of 30 Freight Cost Distribution on

Material Account.

  Note

If you already use freight cost allocation features and you decide to also use these intercompany features, you must change the

settings you have already made to the settings we recommend here.

## Viewing Freight Cost Allocation Documents

You can use the following apps to view freight cost allocation documents:

## Manage Freight Cost Allocation Documents

With this app, you can easily manage freight cost allocation documents. You can search for and navigate to specific freight

cost allocation documents. The app provides a detailed view of a freight cost allocation document including information

about the amounts, administrative data, and document items.

## Monitor Freight Cost Allocation Document Items

With this app, you can get an overview of items in a freight cost allocation document. You can quickly search for and analyze

specific freight cost allocation document items. In particular, you can search these allocation documents by freight order or

This is custom documentation. For more information, please visit SAP Help Portal.

48


1/14/26, 2:42 PM

freight booking.

## Schedule Document Release - Freight Cost Allocation

With this app, you can manually schedule a job to release freight cost allocation documents to Finance. Normally, when you

create a freight cost allocation document, the system automatically releases the document to Finance. However, if the

system cannot automatically release the document, you must manually schedule a job to release it. The system then

releases the document at the appointed time.

Alternatively, you can use transaction code WAB_RELEASE or program RWLF2056 to schedule the periodic release of

freight cost allocation documents in a background processing program.

For more information, see Freight Cost Allocation.

## Related Information

Transportation Management in Advanced Intercompany Business Processes

Advanced Intercompany Sales

Advanced Intercompany Stock Transfer

Dispute Management for Freight Settlements

## Use

As a requester of transportation services, such as a shipper, you can have one of the following freight settlement processes in

place with a provider of transportation services, such as a carrier:

## Self-billing

Your service provider does not submit an invoice. Instead, you settle automatically based on the information in your freight

order. Self-billing is also named evaluated receipt settlement (ERS).

Submission of an invoice by the service provider

You pay the service provider the amount contained in the invoice.

In both processes, you can have differences and potential disputes between what you expect to pay against what the service

provider expects to be paid. To keep good business relationships, you need to work closely with your service provider to resolve

these differences in a collaborative way. You need to get clarification on what the differences are, and converge on an agreement

with the service provider on how to resolve the differences.

In Transportation Management (TM), you can use the invoice submission settlement process with enterprise services. You are a

shipper who requests transportation services from your service provider. You can enable your service provider to use enterprise

services to submit invoices for the freight orders that the service provider executes. The service provider creates an invoice

document in their external system and uses enterprise services to send you the invoice. You use the external invoice to create a

carrier invoice in the TM module of your S/4 HANA system.

Your service provider may have included additional unplanned freight costs or may have different charges to what you expect to

pay in your freight order. Your TM system automatically evaluates the external invoice. It automatically creates a dispute case when

your service provider submits an invoice that contains different values to what you expect. The system captures these differences

in a dispute case. The system captures the individual differences in charges as dispute items.

On the dispute case screens, you as a shipper can approve or reject a dispute case. Open the Dispute Cases Worklist app from the

launchpad. Choose  Freight Settlement

## Dispute Case

 Overview Freight Settlement Dispute Cases .

This is custom documentation. For more information, please visit SAP Help Portal.

49


1/14/26, 2:42 PM

If you approve a dispute case, the system updates the freight order with information for the charge type, such as rate and quantity

information. However, the system does not update logistics information, such as gross weight, gross volume, and total distance of

the freight order.

When you resolve disputes early, you have the following business advantages:

Inclusion of changes and unplanned costs in one invoice

Accuracy in payment to the service provider

More Information

## Subject

## More Information

Structure of an individual dispute case, including working with a

Freight Settlement Dispute Case

dispute case

Structure of an individual carrier invoice, including working with a

Carrier Invoice

carrier invoice

Necessary Customizing settings required before you can use

Prerequisites for Dispute Management

dispute management

Individual aspects of dispute management

## Features of Dispute Management

Details of how freight cost accruals are updated in Materials

Automatic Change Management for Freight Settlements

Management (MM)

Evaluated Receipt Settlement process

Evaluated Receipt Settlement (ERS) (LO-INT-TM)

Supplier invoice web services (B2B)

Supplier Invoice - Create (B2B, Inbound, Asynchronous).

## Dispute Management for Invoice Submission

Your logistics service provider may have included additional unplanned freight costs or have differences in the charges to what you

expect in your freight order. Your system automatically evaluates the external invoice. It creates a dispute case when your service

provider submits an invoice that contains different values to what you expect. Your system captures these differences in a dispute

case. It captures the individual charge element differences as dispute items.

Your service provider creates an invoice document in their external system and uses enterprise services to send this invoice to you.

You create a carrier invoice in the TM module of your S/4 HANA system.

The following are the typical steps that can happen in an invoice submission process:

Transportation Management (TM) creates a freight settlement document for a freight order and posts the freight

settlement document to Materials Management (MM). For example, you have specified an event in your organization where

the system triggers the creation and transfer of a freight order when a freight order gets into execution.

You can use the background processing function Creation and Transfer of Freight Settlement Documents to create and

transfer freight settlement documents. For more information, see Creation and Transfer of Freight Settlement Documents.

On posting, purchase order and service entry sheet (SES) entries are created for the freight settlement document.

Your service provider uses enterprise services to submit an invoice in line with the terms you have agreed with your service

provider.

This is custom documentation. For more information, please visit SAP Help Portal.

50


1/14/26, 2:42 PM

Transportation Management creates a carrier invoice in the shipper's system. The carrier invoice captures the invoice

details submitted by your service provider. TM creates a dispute case if your service provider submits an invoice in which

there are charges that are different from the charges in the original freight order. The system links the dispute case to the

carrier invoice.

The system does not create a dispute case if your service provider does not submit any changes against the charge

amounts or logistics data in the carrier invoice.

You work closely with your service provider and either accept or reject the dispute case for the carrier invoice. When the

carrier invoice is successfully posted to Materials Management (MM), the life cycle status of the carrier invoice is set to

Accepted.

You reject the carrier invoice when you do not agree with the service provider on the carrier invoice. If the carrier

invoice has an associated open dispute case, the system closes the dispute case when you reject the carrier invoice.

You can add a note to the carrier invoice to record the reason for your rejection.

The life cycle status of the carrier invoice is set to Rejected.

You accept the dispute case for the carrier invoice.

TM updates the freight order with the new or changed charges that are contained in the carrier invoice. You can use

the background processing function Creation and Transfer of Freight Settlement Documents to update the new or

changed charges for the freight orders to MM.

You use the background processing function Posting of Carrier Invoices to transfer the carrier invoices that are ready for

posting to Materials Management (MM). For more information, see Posting of Carrier Invoices. The system creates an

incoming invoice in MM. The system posts the carrier invoices to MM for posting only when the following conditions are

satisfied:

No dispute case exists or the dispute case has a life cycle status of Resolved.

The carrier invoice has a life cycle status of other than Rejected.

All the freight orders associated with the carrier invoice have the invoicing status Completely Invoiced.

All the freight settlement documents associated with the freight orders have the life cycle status Accruals Posted.

The carrier invoice has a block status of Not Blocked.

The carrier invoice has a consistency status of Consistent.

More Information

## Subject

## More Information

Structure of an individual carrier invoice, including working with a

Carrier Invoice

carrier invoice

Necessary Customizing settings required before you can use

Prerequisites for Dispute Management

dispute management

Individual aspects of dispute management

## Features of Dispute Management

Details of how freight cost accruals are updated in Materials

Automatic Change Management for Freight Settlements

Management (MM)

## Freight Settlement Dispute Case

This is custom documentation. For more information, please visit SAP Help Portal.

51


1/14/26, 2:42 PM
## Use

A freight settlement dispute case is an individual business document that captures differences in logistics item quantities or

charge amounts for a freight order or a carrier invoice. As a requester of transportation services, such as a shipper, you own the

information in the freight order.

In the invoice submission process, the process of settlement between you and your service provider is based on an invoice that

your service provider submits to you for a freight order. For example, your service provider can submit an invoice that contains

changes to logistics details such as gross weight or gross volume, or changes to charge details such as rate or an additional charge

line for an unplanned charge. In these situations, the system captures the differences in a dispute case and links the dispute case

to the invoice your service provider submits.

If the dispute case fails the tolerance limits you specify in Customizing, you must manually review the dispute case on the Freight

Settlement Dispute Cases user interface (UI).

Structure

## General Data

The General Data tab page contains high-level information about the dispute case and associated freight order or carrier invoice,

for example:

Carrier name, carrier invoice reference, and freight order reference

## Source location and destination location

Logistics information, such as gross weight, gross volume, and total distance at freight order level

## Status information

Amount information, at freight order level

## Logistics Details

On the Logistics Details screen area, the system displays logistics dispute information for a dispute item submitted by the service

provider. For example, your carrier claims the total distance is 510 km, and not 500 km as you expect. The system displays 500 km

in the Order Quantity field, and 510 km in the Dispute Quantity field.

The system also displays the dispute resolution status of each logistics item in a dispute case.

  Note

For an invoice submitted through an enterprise service, these details are not captured because the logistical details for the

order are not part of the enterprise service.

## Charge Details

On the Charge Details screen area, the system displays the charge dispute information for a dispute item submitted by the service

provider. For example, your carrier adds an unplanned cost for 4 hours detention at the rate of USD 50 per hour, totaling USD 200.

The system displays the following information on the Charge Details screen area:

Dispute Item Description: New Charge Line

Charge Description: Detention

## Currency: USD

This is custom documentation. For more information, please visit SAP Help Portal.

52


1/14/26, 2:42 PM

Order Amount: 0

Dispute Amount: 200

The system also displays the dispute resolution status of each charge item in a dispute case.

## Dispute Charge Amounts

The system displays the proposed charge amount from the service provider for the total freight order or carrier invoice on the

Dispute Charge Amounts screen area. This is what your service provider expects to be paid in total and is how the freight order or

carrier invoice would look if you accept the proposal from your service provider.

In an invoice submission process, your service provider adds the unplanned cost for detention of USD 200 to the carrier invoice.

The system displays USD 5,200 in the Dispute Charge Amounts screen area of the carrier invoice.

## Proposed Charge Amounts

You accept or reject the dispute. The system displays the effect your decision has on the total charges in the freight order.

For example, the total order amount is USD 5,000. This is what you expect to pay your carrier. Your carrier submits a dispute case

for an unplanned cost for detention of USD 200. You reject the dispute item. The system displays USD 5,000 in the Dispute Charge

Amounts screen area.

## Taking Action on a Dispute Case

For dispute cases linked to the carrier invoice created using an enterprise service, you as a requester of the transportation service

can perform the following tasks:

Choose Approve All to accept all the dispute items. This means that you accept the carrier invoice sent by the carrier.

Choose Reject Invoice to reject the invoice from the carrier. This also closes the dispute case. The dispute case has the life-

cycle status Rejected.

In both the Logistics Details and Charge Details screen areas, you as a requester of transportation services can perform the

following tasks:

Choose the Approve button to accept a dispute item.

Choose the Reject button to reject a dispute item.

For information about dispute case statuses, see Statuses in Dispute Management. You can also save your work. This enables you

to save a draft while you finalize your decisions. When you save and confirm a dispute case, you finalize your action on the dispute

case.

You can also use the Publish Freight Settlement Dispute Cases background processing function (program

/SCMTMS/SET_CARRIER_RELEVANCE) to automatically save and confirm the dispute cases that pass the tolerance check

criteria. With this function, the system uses the charge details from a dispute case that is resolved to update the changed charge

information in the freight order. For more information, see Publication of Freight Settlement Dispute Cases. The system publishes

your decision for your service provider.

## Notes

On this tab page, you can add any relevant notes, enabling you to share information all though the process of dispute resolution.

You can use notes to collaborate with your colleagues internally.

## Attachments

This is custom documentation. For more information, please visit SAP Help Portal.

53


1/14/26, 2:42 PM

On this tab page, you can upload relevant files, enabling you to share files all through the process of dispute resolution. You can use

attachments to share information with your colleagues internally.

## Tolerance Check Log

On this tab page, the system displays the following information:

Success messages for the charge type dispute items that are inside your tolerance limits and that the system passed

automatically

Failure messages for the dispute items that are outside your tolerance limits and that the system failed automatically

The system displays the dispute cases that failed the automatic tolerance check on the Freight Settlement Dispute Cases - All

Freight Settlement Dispute Cases personal object worklist (POWL) screen. You must manually review these dispute cases.

You can specify tolerance limits in Customizing for Transportation Management under  Settlement

## Freight Settlement

 Freight Settlement Dispute Management

 Define Dispute Tolerance Rules .

## Work Items

The system displays information on the work items created for the dispute case, including the approval level, the status of the work

item, the approver, and the time key events in the lifecycle of the work item take place. For more information, see Workflow for

Dispute Management.

## Integration

Freight settlement dispute cases are integrated with freight orders. When you accept a change in a dispute case, the system

uses the dispute resolution details from a dispute case to update the changed charge information in the freight order. For

more information, see Freight Order Management.

For the freight orders for which you have resolved disputes, you use the background processing function Creation and

Transfer of Freight Settlement Documents to update the changed charges to materials management (MM).

The system posts the freight settlement documents, which are created from freight orders, to Materials Management. It

does not create a freight settlement document from a dispute case. For more information about integration, see

Integration: Invoice Processing (MM-IV/SD-BIL) with TM.

You can use an enterprise service to create a freight settlement dispute case from outside Transportation Management

(TM) in a self-billing scenario. You can send the details of the dispute case outside TM as an enterprise service message. For

more information, see <Provide link to the enterprise services documentation of the dispute case>.

More Information

## Subject

## More Information

Introduction to dispute management

Dispute Management for Freight Settlements

Necessary Customizing settings required before you can use

Prerequisites for Dispute Management

dispute management

Individual aspects of dispute management

## Features of Dispute Management

Details of how freight cost accruals are updated in MM

Automatic Change Management for Freight Settlements

Exchange the charge information that's under dispute between a

Transportation Dispute Case Notification

carrier and a shipper

This is custom documentation. For more information, please visit SAP Help Portal.

54


1/14/26, 2:42 PM

Carrier Invoice

## Use

In an invoice submission process, the process of settlement between you and your service provider is based on a carrier invoice

that your service provider submits to you against one or more freight orders. Your service provider has executed the transportation

requirements in your freight order before sending the invoice.. You have a trusted relationship with your service provider, and your

service provider sends you a carrier invoice.

## Prerequisites

You must specify a carrier invoice type in Customizing for Transportation Management under  Settlement

## Freight Settlement

 Define Carrier Invoice Types .

You must specify a carrier invoice type as the default type.

You must specify the charge types for tax by enabling the Tax setting in the Define Charge Types Customizing activity under

Transportation Management

 Basic Functions

 Charge Calculation

 Basic Settings .

You have specified the following settings in Customizing for Transportation Management under

Integration

 Enterprise

## Services

 Carrier Invoice Integration :

Map the condition type received in the interface to the TM charge type, in the Customizing activity Assign Carrier

Condition Type to TM Charge.

Assign the TM charge type for an invoice that TM processes, under the Customizing activity Assign Carrier Tax Types to TM

Tax Charge Type.

To post a carrier invoice, you must assign the tax code to the TM charge type in the Assign Tax Code to Charge Types Customizing

activity under  Transportation Management

## Integration

## Enterprise Services

## Carrier Invoice Integration . The system

uses this setting when it posts the carrier invoice to an internal materials management (MM) system.

To post the carrier invoice to an external MM system running on SAP S/4 HANA or SAP ERP, you must specify the mapping

settings in Customizing under

Integration with Other SAP Components

 Transportation Management

 Invoice Integration

## Tax

 Map SAP TM Tax Setting .

## Integration

The carrier invoice is integrated with the following objects and systems:

## Freight settlement dispute case

Your service provider can submit an invoice for one or more freight orders.

Transportation Management (TM) captures the invoice details submitted by your service provider. If there are differences

between the submitted invoice and the expected values for the freight order, TM creates a dispute case and links it to the

carrier invoice. If your service provider submits an invoice that matches the expected value for the freight order, TM does

not create a dispute case.

## Posting of the carrier invoice to MM

You can use the Posting of Carrier Invoices background function to post the carrier invoices that are ready for posting to

MM. MM creates incoming invoices. For more information, see Posting of Carrier Invoices.

You can also post one or more carrier invoice directly as follows:

This is custom documentation. For more information, please visit SAP Help Portal.

55


1/14/26, 2:42 PM

Under Freight Settlement, choose  Worklist

 Overview Freight Settlement Documents

 Carrier Invoices .

Under Freight Settlement, choose  Carrier Invoice

 Display Carrier Invoice .

You can also automate the carrier invoice posting directly by enabling Post Invoice Immediately for the carrier invoice type in

Customizing for Transportation Management under  Settlement

## Freight Settlement

 Define Carrier Invoice Types .

The system determines the logical system behind the business system group that you have linked to your purchase organization

data for the freight order, freight booking, or service order that is a part of the carrier invoice. The business system group

represents the SAP ERP system or SAP S/4 HANA system from which you replicate the purchasing organization in the organization

model.

If the logical system is different to the current client logical system, the system uses enterprise services to post the carrier invoice

to an external MM system. If the logical system is the same as the current client logical system, the system posts the carrier

invoice to an internal MM system.

For more information on organizational model see Create and Merge Organizational Hierarchy under  Transportation

Management

## Master Data

 Organizational Management

 Organizational Model

.

You use the InvoiceRequest_In interface to create a carrier invoice in TM. For more information see Carrier Invoice - Create (B2B).

## Features

## Possible Actions for Carrier Invoice

The following table explains possible actions that are available to you:

## Action

Action Description

## Reject Invoice

You can reject a carrier invoice at any time, provided the carrier invoice is not yet posted to MM.

When rejecting a carrier invoice, you can capture notes giving your reasons for rejection. Your service

provider must create a new carrier invoice for the freight order.

When you reject a carrier invoice that has an open dispute case, the system automatically closes the

dispute case. This saves you from taking extra steps to cancel the dispute case manually.

## Post

You can post the carrier invoice to MM provided the carrier invoice satisfies all of the following

conditions:

No dispute case exists or the dispute case has a life cycle status of Resolved

## Has a life cycle status of other than Rejected

All associated freight orders have the invoicing status Completely Invoiced

All associated freight settlement documents have the status Accruals Posted

Has a block status of Not Blocked

## Release

Releases the carrier invoice in the life cycle status Draft. When there are carrier invoices with charges

linked to the resolution base of the freight order, the carrier invoice is created in life cycle status Draft.

When the resolution base information is assigned to the repeating charges in the carrier invoice, this

action can be used to release the invoice for further processing.

## Set to Draft

Recall a released invoice in case you want to change the resolution base information for the charge

lines. This action cancels the relevant dispute case for the associated carrier invoice.

This is custom documentation. For more information, please visit SAP Help Portal.

56


1/14/26, 2:42 PM

## Life Cycle Status

The life cycle status indicates the resolution status of the overall carrier invoice. The following table explains what the key life cycle

statuses mean:

Status

## New

## Draft

## Status Description

Your service provider has not yet submitted the carrier invoice.

When there are carrier invoices with charges linked to the resolution base of the freight order, the

carrier invoice is created in life cycle status Draft.

## In Process

The carrier invoice satisfies one or more of the following conditions:

All the charge lines where you expect resolution base information have been resolved.

Submitted by your service provider but not yet accepted and posted to MM

Has disputes that are not yet resolved

## Not yet posted to MM

Transferred, but failed to post to MM

## Ready for posting

The carrier invoice satisfies all of the following conditions:

No dispute case exists or the dispute case has a life cycle status of Resolved.

## Has a life cycle status of other than Rejected

All associated freight orders have the invoicing status Completely Invoiced.

All associated freight settlement documents have the status Accruals Posted.

Has a block status of Not Blocked

Has a consistency status of Consistent

## Posting started

You have transferred the carrier invoice for posting to MM.

## Carrier invoice posted

The carrier invoice has been successfully posted as an invoice document in MM.

## Rejected

You rejected the carrier invoice for business reasons. For example, the tax amounts in the invoice were

incorrect

## Dispute Case Status in a Carrier Invoice

In an invoice submission process, your service provider submits a carrier invoice against one or more freight orders. You service

provider can also submit an invoice that has a different charge amount to what you expect as a shipper. TM subsequently creates a

dispute case so that you can come to a consensus on the disputed items with your service provider. The dispute case status

reflects the processing status of the dispute on the carrier invoice. The following table explains what the individual dispute case

statuses mean:

## Status

Status Description

## No Dispute

The default status of a carrier invoice, where there are no dispute cases on the charges or logistics

information in the freight orders covered by the carrier invoice.

## Awaiting Your Approval

You as the service requester must act to approve, make a proposal, or reject the dispute created by

your service provider.

This is custom documentation. For more information, please visit SAP Help Portal.

57


1/14/26, 2:42 PM

Status

## Resolved

## Status Description

Both you as the service requester and your service provider have agreed on common ground in the

dispute and you both have agreed on a decision. You have accepted the dispute case.

## Rejected by You by Carrier

You as a service requester reject a carrier invoice from your service provider. This closes the associated

## Invoice

dispute case.

## Block Status

The block status prevents the carrier invoice from being posted to MM. For example, your service provider can use an invoice

number reference from their own transportation system, such as a forwarding order number, a waybill number, or an invoice

number. When your service provider submits a carrier invoice, TM checks to ensure that your service provider has not used the

same invoice number reference ID to submit an invoice previously in the same day. If your service provider has used the same

invoice number reference previously in the same day, as standard TM blocks the carrier invoice and displays the reason Invoice

number reference already used on the carrier invoice screen. This protects you from creating duplicate invoices when you submit

invoices electronically, for example, when you use machine-to-machine (M2M) messages or B-to-B (B2B) messages.

You can specify your own additional blocking checks. For example, you can block a carrier invoice if the freight orders in the carrier

invoice have a delivery date that is later than the current date. As the shipper, this enables you to pay for a transportation only

when all of the parts of the transportation are completed. For more information, see Customizing for Transportation Management

under  Business Add-ins (BAdIs) for Transportation Management

## Settlement

 Freight Settlement

 Freight Settlement

## Dispute Management

 BAdI: Additional Checks for Blocking Carrier Invoices .

You cannot further process a carrier invoice when it is blocked. To unblock the carrier invoice, choose Unblock on the carrier

invoice screen. For more information on block statuses, see Customizing for Transportation Management under  Basic

## Functions

## General Settings

 Define Block Reason Codes .

## Confirmation Status

You can use the confirmation status to track the posting of a carrier invoice to MM. The status indicates the result of the last

integration interaction between TM and MM. The following table explains what the main confirmation statuses mean:

## Status

Status Description

## Not Posted

TM has not posted the carrier invoice to MM.

## Not Confirmed

TM has initiated the posting of the carrier invoice to MM, but the posting process is not yet complete.

## Confirmed

Carrier invoice was posted successfully and an invoice was created in MM.

## Invoice Posting Failed

Posting of carrier invoice could not be completed due to errors.

## Tax Handling

You must specify the charge types that represent tax by selecting the Tax checkbox in Customizing under  Transportation

Management

 Basic Functions

 Charge Calculation

 Basic Settings

 Define Charge Types .

When you post the carrier invoice to an internal MM system, you must assign a tax code to a TM charge type in the Assign Tax

Code to Charge Types Customizing activity under  Transportation Management

## Integration

 Enterprise Services

## Carrier

Invoice Integration .

When you post the carrier invoice to an external MM system running on SAP S/4 HANA or SAP ERP, you must specify the mapping

settings in the Map SAP TM Tax Settings Customizing activity under

Integration with Other SAP Components

 Transportation

## Management

  Invoice Integration

 Tax .

This is custom documentation. For more information, please visit SAP Help Portal.

58


1/14/26, 2:42 PM

TM does not verify the tax amounts in the carrier invoice. Instead, MM verifies the tax amounts when you post the invoice in MM.

If there is a discrepancy between what your carrier has submitted and what MM expects to pay, MM does not post the carrier

invoice. You must manually reject these carrier invoices in TM. You can find the carrier invoices that contain a discrepancy by

filtering the following statuses:

Life cycle status In Process

Confirmation status Invoice Posting Failed

More Information

## Subject

More Information

Background processing

Posting of Carrier Invoices

function for posting carrier

invoices to MM

Individual aspects of dispute

Features of Dispute Management

management

Process a carrier invoice using

Carrier Invoice - Create (B2B)

## Web Services

Processing of a Carrier Invoice Using a B2B Interface

## Use

You have a trusted relationship with your service provider, and your service provider sends a carrier invoice to you electronically

using the B2B message interface for one or more freight orders. Transportation Management (TM) captures the invoice details

submitted by your service provider. If there are differences between the submitted invoice and the expected values for the freight

order, TM creates a dispute case and links it to the carrier invoice. If your service provider submits an invoice that matches the

expected value for the freight order, TM doesn’t create a dispute case.

The InvoiceRequest_In interface is used to process a carrier invoice that refers to a document such as a freight order, a service

order, or a freight booking in TM. For more information on the B2B interface, see Carrier Invoice - Create (B2B).

## Process Flow

1. You as a shipper use a freight order, freight booking, or service order to request a transportation service from your carrier.

2. Your carrier provides the transportation services.

3. The carrier creates the invoice document in their external system and sends you the invoice through Web Services.

4. Your system creates a carrier invoice in the TM module.

5. Your carrier may include an additional unplanned freight cost. The carrier may send an invoice that differs in a charge

amount to what you expect in your freight order.

If your carrier submits an invoice that contains differences in values to what you expect, your system automatically

evaluates the incoming invoice and creates a dispute case. The system captures the individual charge element differences

as dispute items.

You resolve the dispute. For more information, see Dispute Management for Invoice Submission.

This is custom documentation. For more information, please visit SAP Help Portal.

59


1/14/26, 2:42 PM

6. If the values in the invoice your carrier sends match the values you expect in your freight order, the system doesn’t create a

dispute case.

You resolve the disputes by accepting the carrier values if they are acceptable to you and are for the correct reasons. For example,

the carrier invoice contains waiting as an additional charge. The system creates a dispute for this invoice. As part of the dispute

resolution you find that there was a waiting time for the carrier and hence the carrier's claim for the waiting charge is correct. You

accept this carrier invoice including the waiting charges.

Alternatively, the carrier invoice doesn’t contain any disputes. You post the carrier invoice to material management (MM). For more

information see Carrier Invoice.

## Restrictions

You as a shipper have the following restrictions in processing the carrier invoice and credit memo in TM. In all cases, the system

doesn’t process the carrier invoice or credit memo and creates an error against the B2B message. You must work with your carrier

to resolve these errors. Your carrier must then resend a new error-free B2B message.

## Complete Cancellation

TM only supports a credit memo that cancels the complete invoice that the carrier previously sent.

A credit memo that contains partial amounts from the previously sent invoice, or with different charge types than in the previously

sent invoice, causes an error. The system doesn't process the credit memo.

For example, your carrier sends you an invoice with the reference INV984500 for USD 1000. This comprises of a base freight

amount of USD 975 and a loading charge of USD 25. You accept the invoice. Later, the carrier realizes that the invoice is incorrect.

The loading charge isn't applicable for the freight order that is part of the invoice INV984500.

If your carrier uses the B2B message to send you the credit memo for the credit on the loading charge of USD 25, the system

doesn't process the credit memo and creates an error. Instead, your carrier must send a complete credit memo for all the

previously sent invoice. Your carrier must then send you a corrected invoice. In this example, your carrier must send a credit memo

with a canceled invoice ID of INV984500 for the whole amount of USD 1000. The carrier must then send second corrected invoice

for USD 975 for the base freight charge of USD 975.

## Repeating of Condition Types

The system doesn't process invoices for a freight order, freight booking, or service order in which the TM charge calculation

contains a repeating charge line that is not due to the calculation resolution base. Instead, the system creates an error. The

interface doesn't support an invoice with a repeating condition type for an item in an invoice.

For example, you have a freight order for a less-than-truck-load (LTL) shipment that consists of two packages. You agree with your

carrier that the carrier charges you a freight charge for each package and a handling charge for loading and unloading services. You

have an agreement with the carrier in which the system calculates charges for the freight order with header-level calculation and

has freight charges for each package and a handling charge for the loading and unloading. You expect the carrier to send you an

invoice as follows:

Charge Type

Amount (USD)

Explanation

Handling charge

Handling charge

5

5

Due to loading

Due to unloading

Freight change

25

For package 1

Freight charge

40

For package 2

This is custom documentation. For more information, please visit SAP Help Portal.

60


1/14/26, 2:42 PM

Charge Type

Amount (USD)

Explanation

Total

75

The freight charge is repeated for this freight order, and the invoice does not cause an error due to this charge as the system

handles such invoices for charges which repeat due to the resolution base. However, the system cannot process the handling

charges in the invoice above that are repeating and are not with a resolution base. Instead, the system creates an error in inbound

processing.

## Through-Rate Calculation

The system creates an error and doesn't process an invoice for a TM freight order or freight booking in which the TM charge

calculation is Though Rate. For more information, see Through Rates.

For example, you agree stage-level calculation with your carrier. You have a freight order with following transportation stages:

Stage ID

Stage

10

20

Stage A to stage B

## Stage B to stage C

Your carrier gives you a through rate for a freight order from stage A to stage C. The system doesn't process the carrier invoice and

creates an error if your carrier submits the freight order through the B2B interface.

## Partial Charge Line Resulting in a Dispute Case

The system creates a dispute case when your carrier submits an invoice that contains a partial charge line.

For example, your carrier sends you an invoice with a loading charge of USD 25. You expect the loading charge to be USD 50. The

system captures this deviation as a dispute case. It displays the information on the Dispute Charge Amounts screen area of the

dispute case.

## Different Currencies

The system processes an invoice sent by your carrier in the same currency as that which you expect for the freight document. If

the carrier sends you an invoice with a different currency than you expect, the system creates an error and doesn’t process the

invoice.

For example, you expect your carrier to send you an invoice in the currency USD. If the carrier sends the invoice through the B2B

interface in the currency EUR, the system doesn’t process the invoice document and creates an error.

Related Information

## Carrier Invoice

Carrier Invoice - Create (B2B)

Working with Resolution-Based Charges

## Working with Resolution-Based Charges

You have a freight order for a less-than-truck-load (LTL) shipment that consists of two packages. You agree with your carrier that

the carrier charges you a freight charge for each package and a loading and handling charge for the transport. You have an

agreement with your carrier in which the system calculates charges for the freight order with header-level calculation and has

This is custom documentation. For more information, please visit SAP Help Portal.

61


1/14/26, 2:42 PM

freight charges for each package and handling charge for the loading and unloading. You expect the carrier to send you an invoice

as follows:

Charge Type

Amount (USD)

Explanation

Handling charge

Freight charge

Freight charge

Total

5

25

40

70

Due to loading and unloading

For package 1

For package 2

The InvoiceRequest_In interface is used to process a carrier invoice, and a carrier credit memo that refers to such a freight order

cannot carry the reference of the packages for each charge. When these carrier invoices or credit memos are processed, the

system handles these invoices in the following way:

Creates a carrier invoice that contains charge lines with a resolution base in the life cycle status Draft.

The carrier invoice or carrier credit memo can only be processed when the logistical references for the charge lines for the

resolution base are assigned. The assignment can be done by the system automatically or by the user manually.

To enable the automatic determination of the logistical references, the Auto Prop Res Base Charge Line is enabled in the

settlement profile.

To manually assign the logistical reference, you can navigate to the carrier invoice or carrier credit memo by using the

worklist  Freight Settlement Worklist

 All Carrier Invoices in Draft Status or All Carrier Credit Memos in Draft Status .

In the carrier invoice or carrier credit memo, you can assign the logistical reference by going to the screen area Charges

with Logistical Refs. Alternatively, you can trigger the automatic determination of the logistical references by using the

action Propose Logistical References.

When the logistical references are assigned to the charge lines, the carrier invoice can be released for further processing.

Once the carrier invoice is released, the logistical reference assigned to the charge lines in the carrier invoice can be

changed by setting the carrier invoice life cycle status to Draft using the action Set to Draft. Any associated open dispute

case with the carrier invoices are cancelled on executing this action.

The processing of a carrier credit memo with charge lines that contain a resolution base is done in a similar way.

  Note

The following criteria are fulfilled for a carrier invoice that is set to Draft status by the user.

Only a carrier invoice and a carrier credit memo with charge lines expecting logistical references due to the resolution

base.

Only a carrier invoice and carrier credit memo that are not posted.

Only a carrier invoice with a dispute case, where the life cycle status of the dispute case is not in status Resolved.

A carrier credit memo cannot be set to Draft after it has been released.

## Related Information

## Determine Logistical References Automatically

This is custom documentation. For more information, please visit SAP Help Portal.

62


1/14/26, 2:42 PM

## Determine Logistical References Automatically

The automatic match algorithm is used to automatically propose the logistical references for charge lines with missing logistical

references in the carrier invoice and carrier credit memo. The charges in the freight document that are modelled using a resolution

base expect the logistical reference to which the charges are referenced. The logistical reference determination in the carrier

invoice and carrier credit memo can be enabled as follows:

Enable Auto Prop Res Base Charge Line in the settlement profile.

In the carrier invoice or carrier credit memo, you can trigger the automatic determination of the logistical references by

using the action Propose Logistical References.

The following steps show how the feature works:

1. In the carrier invoice, each charge line that expects a logistical reference is compared with respective charges in the freight

document based on matching a charge line with the same charge type with a rate amount, rate currency, price per unit,

UoM, final amount, final amount currency, and quantity. If a match is found, then the logistical reference is assigned from

the charge line of the freight document to the charge line in the carrier invoice.

For the carrier credit memo, the charge lines in the carrier credit memo are compared with the charge lines in the

corresponding carrier invoice referenced by the credit memo in the field Cancelled Supplier Invoice ID.

2. In the carrier invoice, if there is no complete match found, then in the carrier invoice, each charge line that expects a

logistical reference is compared with respective charges in the freight document based on matching with the same charge

type with a final amount, final amount currency, and quantity.

3. If the above exact matches are not feasible due to invoices with a variance or missing information from the carrier such as

quantity, the system tries to do a near match. In the carrier invoice, each charge line that expects a logistical reference is

compared with respective charges in the freight document based on the matching with the same charge type. If there are

more than one charge lines with the same charge type in the freight document, the invoiced amount and currency of the

charge line in the carrier invoice is compared with the final amount and currency of the charge line in the freight document

and the logistical reference of the freight document charge line which has the least difference with the carrier invoice

charge line is assigned to the charge line of the carrier invoice.

The following tables contain an example that explains how the feature works:

You have freight order 810002, that contains the following cargo items:

## Cargo Item

Cargo Item Details Quantity

## UoM

Gross Weight

## UoM

Package

Pallet 1

Product 1

Product 2

Product 3

50

50

5

10

PC

PC

PC

PC

10

10

20

25

KG

KG

KG

KG

Master data (calculation sheet):

Charge Type

## Resolution Base

Rate Table/Rate Value Currency

Base charge

Product

RT_BASE_WT

Loading charge

10

USD

USD

Packaging charge

## Package

RT_PACK_PTYPE

USD

This is custom documentation. For more information, please visit SAP Help Portal.

63


1/14/26, 2:42 PM

Freight order 810002 has the following charges:

Line Number

Charge Type

Rate (USD)

Price per Unit

Quantity

10

20

30

40

50

Base charge

Base charge

Base charge

Loading charge

Packaging

charge

10

10

10

10

50

Logistical

Reference

Product 1

Product 2

/1 KG

/1 KG

/1 KG

10 KG

20 KG

25 KG`

Product 3

/1 KG

1 KG

Pallet 1

Final Amount

(USD)

100

200

250

10

50

The carrier invoice for freight order 810002 is received with the following charges through the enterprise service. As the

InvoiceRequest_In interface does not carry the logistical references for the charge lines, the logistical references will be empty in

the carrier invoice:

Carrier Invoice # CAR10209

## Line

Charge Type

Rate (USD)

Price per Unit

Quantity

Logistical

## Reference

Invoice Amount

(USD)

1

2

3

4

5

Base charge

Base charge

Base charge

Loading charge

Packaging

charge

10

10

10

10

50

100

210

255

10

60

On executing the automatic logistical reference proposal, the system identifies the three charge lines for the base charge and one

charge line for the packaging charge that require the logistical references to be populated in the carrier invoice. The system runs as

follows on the charge line to propose the logistical reference:

1. For the first base charge line in the carrier invoice for 100 USD, the system tries to find the matching charge line in the

freight order 810002, based on the charge type, rate, price per unit, quantity, and invoice amount. As in this case there is no

such match, the charge line is processed for a near match in the next steps.

For the second and third base charge lines, as there is no exact match based on the charge type, rate, price per unit,

quantity, and invoice amount, the charge lines are processed for a near match in the next steps.

2. For the packaging charge, the same matching logic is run and also the system doesn't find a matching value. The charge is

processed for a near match in the next steps.

3. The system tries to find a match by comparing the three base charge lines based on the charge type individually from the

carrier invoice to the charge lines in the freight order. In this case for the first base charge line in the carrier invoice, the

system finds the match to the charge type and invoice amount to the charge type and final amount in the freight order

referring to the product one, the system proposes the product one as the logistical reference for the carrier invoice base

charge line in the carrier invoice. For the second and third base charge lines, the amounts do not match with the freight

order charges. For the packaging charge also, there is no match to the packaging charge line in the freight order based on

the charge type and amount comparison. These charge lines will be processed further in the nearest match step.

This is custom documentation. For more information, please visit SAP Help Portal.

64


1/14/26, 2:42 PM

4. The second base freight charge line of USD 210 in the carrier invoice is compared with the base charges in the freight order,

base charge 200 (line 20) and base charge 250 (line 30). For the carrier invoice for the second base charge line, the system

determines the nearest match to find the charge line with the least deviation. In this case, the system finds that the charge

line in the freight order for product two is with the least amount of deviation of 10 USD when compared to the base charge

for product three in the freight order, which has a deviation of 40 USD.

The third base freight charge line of USD 255 is compared with the only remaining base freight line and the logistical

reference of product three is assigned to the charge line in the carrier invoice. For the packaging charge, as there is only one

packaging charge in the freight order, the logistical reference of the charge line is assigned to the charge line in the carrier

invoice, in this case pallet one.

5. The system does not run the automatic logistical reference process on the loading charge as the loading charge does not

have a logistical reference in the freight order.

After the system runs the process, it updates the carrier invoice as follows:

Carrier invoice CAR10209

## Line

Charge Type

Rate (USD)

Logistical Reference

Invoice Amount (USD)

1

2

3

4

5

Base charge

Base charge

Base charge

Loading charge

10

10

10

10

Product 1

Product 2

Product 3

Packaging charge

50

Pallet 1

100

210

225

10

60

For the carrier credit memo, the cancelled supplier invoice ID is used as a reference to trace the credit memo to the supplier

invoice it is cancelling. The missing logistical references are established by the matching logic of the charge line information

between the carrier credit memo and the carrier invoice, based on exact charge line attributes such as charge type, rate, quantity,

and credit amount, or based on the charge type and credit amount.

For example, you have carrier credit memo CMCAR9002 with cancelled supplier invoice ID CAR10209:

## Line

Charge Type`

Rate (USD)

Credit Amount (USD)

1

2

3

4

5

Base charge

Base charge

Base charge

Loading charge

10

10

10

10

Packaging charge

50

100

210

255

10

60

On executing the automatic logistical reference proposal process on the carrier credit memo, the system identifies the three

charge lines for the base charge and one charge line for the packaging charge. These require the logistical references to be

populated in the carrier credit memo does the following:

The system runs the following steps on the charge line to propose the logistical reference:

1. For the first base charge line in the carrier credit memo, the base charge for USD 100, the system tries to find the matching

charge line in carrier invoice CAR10209, based on the charge type, rate, price per unit, quantity, and invoice amount. As the

This is custom documentation. For more information, please visit SAP Help Portal.

65


1/14/26, 2:42 PM

exact matches are found for the first base charge line, the logistical reference to product one from the carrier invoice is

copied over. The system does the same matching for the other two base charge lines and packaging charge, resulting in

product two, product three, and pallet one being assigned as the logistical references.

2. The system does not run this process on the loading charge as the loading charge does not have any logistical reference in

the carrier invoice.

After running the automatic logistical reference proposal, the system makes the following updates, for carrier credit memo

CMCAR9002 and cancelled supplier invoice CAR10209:

## Line

Charge Type

Rate (USD)

Logistical Reference

Credit Amount (USD)

Base charge

Base charge

Base charge

Loading charge

10

10

10

10

Product 1

Product 2

Product 3

Packaging charge

50

Pallet 1

100

210

225

10

60

1

2

3

4

5

  Note

1. You cannot add a logistical reference to a carrier invoice that does not exist in the freight document charge.

2. If there are additional charge lines that cannot be assigned a logistical reference in the carrier invoice, the carrier invoice

remains in the draft status and cannot be processed.

Prerequisites for Dispute Management

## Settlement Profile Settings

In Customizing for Transportation Management under  Settlement

## Define Settlement Profile , you can specify the freight

settlement profile settings. You have the option of specifying the following settlement profile settings:

Approval workflow to enable you to use an approval workflow for all freight settlement dispute cases that fall outside the

specified tolerances

Tolerance groups to enable you to specify lower and upper limits on disputed charge type amounts and total freight order

amounts within which the system automatically approves dispute cases

Dispute item profile to specify the individual logistics item or charge type against which a service provider can create a

dispute case

## Dispute Management Settings

In Customizing for Transportation Management under  Settlement

 Freight Settlement

 Freight Settlement Dispute

## Management

 you must specify the following settings:

## Dispute item types

In the Define Dispute Item Types Customizing activity, you must specify the dispute item types that a service provider can

use to create dispute items. The service provider can only enter dispute amounts and create dispute cases for the enabled

This is custom documentation. For more information, please visit SAP Help Portal.

66


1/14/26, 2:42 PM

fields.

You add a dispute item type to a dispute item profile, so that the system can subsequently use the item type when the

service provider creates a dispute case for the freight order.

## Dispute item profiles

In the Define Dispute Item Profiles Customizing activity, you must group the dispute item types against which you want to

allow a service provider to create dispute items.

  Note

For a carrier invoice created from an enterprise service, it is not mandatory to define the dispute item profile.

We deliver the item profile DEFAULT. The following table contains the item types we deliver as standard in the DEFAULT

item profile:

Item Type

Function

## Use Example

## CHARGELINE.DISPUTE

Propose a rate change on an existing

Create a dispute case against the base

charge line.

freight rate.

## MANUAL.CHARGE.DISPUTE

Propose a rate change for charge lines

## Loading charges

you have manually added from an

agreement.

NEW.CHARGE.LINE.DISPUTE

Add a new charge type.

Detention or demurrage

## ROOT.DISTANCE

Propose a change for the total distance

Not applicable

of a freight order.

## ROOT.GROSS.VOLUME

Propose a change on total gross volume

Not applicable

of a freight order.

## ROOT.GROSS.WEIGHT

Propose a change on total gross weight

Not applicable

of a freight order.

For example, you do not want your carrier to propose a new charge line in a dispute case. You use the DEFAULT item profile

and exclude the item type NEW.CHARGE.LINE.DISPUTE. Also, in a full truck load scenario, you do not want your carrier to

create a dispute case for the total distance. You use the DEFAULT item profile and exclude the item type ROOT.DISTANCE.

## Tolerance rules

In the Define Dispute Tolerance Rules Customizing activity, you must specify tolerance limits for charge types that enable

you to reduce administration overhead and automatically approve dispute cases. You can specify more than one tolerance

in a tolerance group.

You can use the tolerance settings to enable automatic approval for changes to the following charge amounts:

Charge line rate amount

Charge line final amount

## Overall amount in a freight order

For example, you can specify a tolerance for the total amount in a freight order for a dispute case in a self-billing

process, or a tolerance for the net amount in a carrier invoice submission process.

When the system creates a dispute case, it performs a tolerance check. It checks each charge type amount and the overall

amount in a dispute case against the tolerance deviations contained in the relevant dispute case. If the charge type amount

This is custom documentation. For more information, please visit SAP Help Portal.

67


1/14/26, 2:42 PM

or overall amount falls within the tolerance limits, the system automatically passes the dispute case. If the amount falls

outside the limits, the system adds the dispute case to the work list on the Freight Settlement Dispute Case screen for

manual attention.

If you do not specify tolerance rules, you must manually review each dispute case on the Freight Settlement Dispute Case

screen.

## Dispute case reason codes and types

In the Define Dispute Case Reason Codes and Types Customizing activity, you must specify the reason code that you

assign to a freight settlement dispute case or a freight settlement dispute case line item to specify the reason why you

created the dispute case or to record the reason why you approved, accepted with a proposal, or rejected the dispute case

or line item.

You must also specify the freight settlement dispute case types that the system uses when it creates a freight settlement

dispute case.

## Printouts, email, and enterprise service

If you want to exchange dispute case information with your carrier in a printout, email, or enterprise service, you must

assign the action profiles in the Output Profile and Additional Output Profile fields in Customizing for Transportation

Management under  Settlement

## Freight Settlement

 Freight Settlement Dispute Case

 Define Dispute Case Reason

Codes and Types .

For more information, see Output Management.

To send an email to your carrier, you must enter an email address in the Address Independent Communication section of

the business partner master data for the carrier.

## Approval levels and workflow

If you want to specify an approval workflow, you must specify the appropriate settings in the settlement profile in

Customizing for Transportation Management under  Settlement

 Define Settlement Profile . The system uses an

approval workflow for dispute cases created against freight orders for a service provider.

If you want to specify the approval levels a dispute case must pass through, and the roles that the system applies to each

approval level, you must specify the appropriate settings in the Define Approval Levels and Roles for Workflow

Customizing activity.

You can specify approval levels for level-1 users and level-2 users. Level-1 users and level-2 users can approve, accept and

propose, or reject a change from a service provider. For more information, see Workflow for Dispute Management.

If you want to add or remove workflow approvers based on one or more of the details in a dispute case, you must specify

BAdI: User Determination for Dispute Case Workflow in Customizing for Transportation Management under  Business

Add-Ins (BAdIs) for Transportation Management

## Settlement

. The approver you specify in this BAdI overrides the

approver you specify in Customizing.

You can use the Business Configuration Set (BC Set) Customizing Workflow Agents Approval Levels and Roles for

Workflow (/SCMTMS/INV_DISP_WFL_AGENTS_C) for the Define Approval Levels and Roles for Workflow Customizing

activity.

More Information

## Subject

## More Information

Structure of an individual dispute case, including working with a

Freight Settlement Dispute Case

dispute case

Individual aspects of dispute management

## Features of Dispute Management

This is custom documentation. For more information, please visit SAP Help Portal.

68


1/14/26, 2:42 PM

## Subject

## More Information

Details of how freight cost accruals are updated in Materials

Automatic Change Management for Freight Settlements

Management (MM)

Working with the master data for the vendor

Manage Supplier Master Data

## Features of Dispute Management

Your service provider, such as your carrier or additional agreement party for providing other services, submits invoices for the

freight orders. The carrier invoice may be different from what you expected to pay the carrier. This results in the system creating a

dispute case.

## Tolerance Check

When the service provider submits invoices with disputes, Transportation Management (TM) applies the tolerance settings you

specified in the Define Dispute Tolerance Rules Customizing activity. If the dispute items are within the tolerance limits, the

system automatically accepts the dispute case. If the dispute case is outside the limits, it fails the tolerance check and the dispute

case must be reviewed by a user on the  Freight Settlement

## Dispute Case

 Overview Freight Settlement Dispute Cases

screen.

The system stores the results of the tolerance checks in the Tolerance Check Log tab page of the individual dispute case. You have

a record of the automatic acceptance and automatic failure results.

## Dispute Resolution Cycle

A dispute is resolved when both you and your service provider arrive at a common agreement on the charge or logistics item under

dispute. To arrive at common ground, you either reject or accept the dispute.

You can have only one dispute case for one service provider at a time for a freight order. However, in freight orders with a carrier

and an additional agreement party, you can have two open disputes, one for the carrier and one for the additional agreement party.

Note that the system does not allow more than one dispute case for a freight order for the same service provider to be open at the

same time.

## Workflow and Work Items

You can use a workflow process to structure the approval process for your dispute cases. You can ensure that one or more users in

your organization approve a dispute case before you accept or reject a proposed change to a freight order from a service provider.

If you enable a workflow process to approve dispute cases, the system creates work items for your level-1 and level-2 users. You can

review all the work items that are open on the Freight Settlement Dispute Case Work Items screen. You can review the status of

the work items for an individual dispute case on the  Dispute Case

 Work Items  screen. You can navigate to the dispute case

screen from the work item. For more information, see Workflow for Dispute Management.

## Dispute Cases Statuses

The following table contains the statuses that can apply to a dispute case:

## Status

Answers the Question

## Life cycle status

Is the overall dispute case open or resolved?

## Action status

Who needs to act on the overall dispute case?

This is custom documentation. For more information, please visit SAP Help Portal.

69


1/14/26, 2:42 PM

## Status

Answers the Question

## Workflow status

What is the status of an individual work item?

Dispute item status in the Logistics Details

What is the approval status of an individual dispute item?

tab page and the Charge Details tab page

## Dispute status for total amount

What is the overall approval status for the total amount of the freight order?

For more information, see Statuses in Dispute Management.

## Dispute Case Status in Freight Order

You can review the dispute case status in a freight order on the  Statuses

 Subcontracting  screen. The status indicates the

resolution status of a dispute case in a freight order, and is explained in detail in the following table:

## Status

## No Dispute

## Status Description

The default status of the freight order when there are no disputes created against the

freight order.

## Awaiting Your Approval

You as the service requester must act to approve, make a proposal, or reject the dispute

created by your service provider.

Note that if the freight order is with a carrier and an additional agreement party, this status

applies to the open dispute cases from your service providers. If there are any open dispute

cases, you must act to approve, make a proposal, or reject the dispute.

## Awaiting Carrier Approval

Your service provider must act on a dispute case. If the freight order is with a carrier and an

additional agreement party, your service providers must act on their respective dispute

case. This means you as the service requester have taken one of the following actions:

Rejected the claim from your service provider. If your service provider agrees with

your decision, they must accept the dispute.

Proposed a solution that is acceptable to you against the claim from the service

provider. If your service provider agrees with your decision, they must accept the

dispute.

## Resolved

Both you as the service requester and your service provider have agreed on common

ground in the dispute and you both have agreed on a decision.

If the freight order is with a carrier and an additional agreement party, all the open dispute

cases have been agreed on common grounds by the service requester and the respective

service provider.

## In Dispute

This status only applies to the Dispute Case Status on the Status tab of a freight

document such as a freight order or a freight booking.

In a freight order with a carrier and an additional agreement party, there are unresolved

dispute cases from both the carrier and additional agreement party. The dispute cases for

each of the service providers may have different dispute case statuses. For example, one

dispute case may have the status Awaiting Your Approval and the other dispute case may

have the status Awaiting Carrier Approval. In such scenarios, you must navigate to the

dispute case document for the freight order to know the actual status of the dispute case.

Dispute Management with Carriers and Additional Agreement Parties

This is custom documentation. For more information, please visit SAP Help Portal.

70


1/14/26, 2:42 PM

If you specify one or more carriers or additional agreement parties in your freight order, you can have multiple disputes in a single

freight order. However you can have just one dispute for each party.

The service provider such as, a carrier or an additional agreement party, can submit an invoice to the shipper.

In the freight carrier invoice scenario, the service provider can submit a freight carrier invoice with the disputed items. The TM

system creates a dispute on a carrier invoice if there is a mismatch of values between the expected invoice value and the values

submitted by the carrier. The dispute gets resolved when you as the shipper approve the proposal submitted by the carrier. When

the dispute is resolved the system copies the charges approved in the dispute based on the freight carrier invoice and updates the

freight order.

For more information, see Additional Agreement Parties.

## Dispute Resolution Statuses

In dispute management scenario with multiple service providers such as, carriers or additional agreement parties, you have

multiple service providers who may create multiple dispute cases. The status of one dispute case may differ from the other. Hence,

the system displays the dispute resolution status for every charge item in a freight order. Based on the dispute statuses of the

charge items, the system displays a freight order dispute resolution status in the Dispute Case Status field on the Statuses tab.

The following table explains how the system computes the freight order dispute resolution status:

Dispute Resolution Status of Carrier 1

Dispute Resolution Status of Carrier 2

Dispute Resolution Status of Freight Order

No Dispute

No Dispute

No Dispute

No Dispute

## No Dispute

Awaiting Your approval

Awaiting Your Approval

Dispute Resolved

Dispute Resolved

Awaiting Your approval

## No Dispute

Awaiting Your Approval

Awaiting Your approval

Awaiting Your approval

Awaiting Your Approval

Awaiting Your approval

Dispute Resolved

Awaiting Your Approval

Dispute Resolved

## No Dispute

Dispute Resolved

Dispute Resolved

Awaiting Your approval

Awaiting Your Approval

Dispute Resolved

Dispute Resolved

## Dispute Resolved

For more information on the dispute statuses, see Carrier Invoice.

## Edit Dispute Case on Behalf of Carrier

As a shipper, you can act on behalf of a carrier to capture inputs on dispute items from the carrier. You can capture offline inputs

such as an email or phone conversation from your carrier and add the inputs to a dispute case on behalf of the carrier. To add this

information, the dispute case must be in the dispute resolution status of Awaiting Carrier Approval.

More Information

## Subject

## More Information

Structure of an individual dispute case, including working with a

Freight Settlement Dispute Case

dispute case

This is custom documentation. For more information, please visit SAP Help Portal.

71


1/14/26, 2:42 PM

## Subject

## More Information

Necessary Customizing settings required before you can use

Prerequisites for Dispute Management

dispute management

Introduction to dispute management

Dispute Management for Freight Settlements

Statuses in Dispute Management

## Life Cycle Status

The life cycle status indicates the resolution status of the overall dispute case. The following table explains what the individual

status values mean:

## Status

## In Dispute

## Status Description

Indicates that the transportation service requester and the transportation service provider

have not yet agreed a resolution to the dispute case. Both parties disagree on the logistics

information or charge information in the freight order.

## Cancelled

Your service provider has submitted a carrier invoice that has an associated dispute case.

You have rejected the carrier invoice. In the background, the system cancels the dispute

case and changes the dispute case status of the carrier invoice to Resolved. This saves you

from taking extra steps to cancel the open dispute case manually.

Your service provider has submitted a credit memo to cancel an existing carrier invoice. The

carrier invoice had an associated open dispute case that is cancelled by the system.

## Dispute Resolved

Indicates that the transportation service requester and the transportation service provider

have agreed a resolution to the dispute case.

This means that you as a service requester have taken one of the following actions:

## Accepted the claim from the service provider

Rejected the claim of the service provider and the service provider accepted this

decision

Proposed a solution that is acceptable to you against the claim from the service

provider, and the service provider accepts your proposal

## Dispute Rejected

Indicates that your transportation service provider has agreed to withdraw a dispute case.

## Action Status

The action status indicates the party that owns the next action in the dispute resolution process. The following table explains what

the individual status values mean:

## Status

Status Description

## Awaiting Your Approval

You as the service requester must act to approve, make a proposal,

or reject the dispute created by your service provider.

## Completed

Both you as the service requester and your service provider have

agreed on a decision for the dispute case.

This is custom documentation. For more information, please visit SAP Help Portal.

72


1/14/26, 2:42 PM
## Workflow Status

The workflow status indicates the status of the workflow for a dispute case. The following table explains what the individual status

values mean:

## Status

Workflow Not Enabled

Automatically Approved

Awaiting Approval

## Status Description

You have not enabled a workflow to resolve disputes with your

service provider in the Customizing settings for the relevant

settlement profile (see Prerequisites for Dispute Management). The

dispute case does not go through an automatic and structured

approval process.

The system has used the tolerance settings you specified in

Customizing to approve the dispute case automatically in the

background (see Prerequisites for Dispute Management). You do

not need to take any action.

You are waiting for one or more of the approvers in the workflow to

take action on the dispute. The approvers in the workflow must

accept, accept with a proposal, or reject the dispute case (see

Workflow for Dispute Management).

## Completed

The workflow has no more work items and the dispute case has an

action status of Completed.

## Dispute Item Status

The dispute item status indicates the resolution status of a dispute item for an individual logistics item or an individual charge

type. The following table explains what the individual status values mean:

Status

## New

## Status Description

You as the service requester must act on the dispute item. You

must accept, accept with a proposal, or reject the dispute item.

## Approved by You

You as the service requester have approved the dispute item.

## Accepted by You with Proposal

You as the service requester make a proposal against the dispute

submitted by your service provider, and send the proposal to your

service provider for action.

## Rejected by You

You as the service requester reject the dispute submitted by your

service provider.

## Approved by Tolerance Check

The system has used the tolerance settings you specified in

Customizing to approve the dispute item automatically in the

background (see Prerequisites for Dispute Management). You do

not need to take any action.

## Workflow for Dispute Management

As standard, we deliver a 2-level approval process for your dispute case approval workflow. In this process, when your service

provider submits a carrier invoice that has a dispute, the system sends the dispute case to a level-1 approver for approval. When

the level-1 approver takes action, the system sends the dispute case to a level-2 approver for approval.

This is custom documentation. For more information, please visit SAP Help Portal.

73


1/14/26, 2:42 PM

Both the level-1 approver and level-2 approver accept or reject the dispute case. When the level-2 approver takes action, the system

updates the life-cycle status of the dispute case. If the level-2 approver rejects the dispute case, the carrier invoice is rejected. If

the level-2 approver accepts the dispute case, the carrier invoice is accepted.

You must enable the relevant settlement profile for the approval workflow. For more information, see Prerequisites for Dispute

Management.

## Features

## Workflow Configuration

We have implemented the 2-level approval workflow WS61200016 as standard. You can review the configuration of the standard

workflow in transaction SWDD (Workflow Builder).

We have added an action to the standard Post Processing Framework (PPF) profile for dispute cases in freight settlement. We have

used the settings in the following table to specify the standard workflow in the PPF profile:

Object Type

Application

Action profile

Action definition

Processing type

Workflow template

## Object Name

/SCMTMS/TRANSPORTATION

/SCMTMS/TOR_INV_PREP (Post Freight Settlement Document

to MM)

/SCMTMS/FDI_WFL (Workflow for Dispute Invoice)

Workflow (Default)

WS61200016

You can review these settings in Customizing for Cross Application Components under  Processes and Tools for Enterprise

## Applications

 Reusable Objects and Functions for BOPF Environment

 PPF Adapter for Output Management

 Maintain PPF

Settings .

If you enable the approval workflow in a settlement profile, the system triggers the workflow when a dispute case is created in

either the self-billing or invoice submission processes. For more information, see Customizing for Transportation Management

under  Settlement

 Define Settlement Profile .

You can implement your own approval workflow. To do this you must create a workflow configuration to suit your business needs in

transaction SWDD, and specify the workflow in the Workflow processing type, under the /SCMTMS/FDI_WFL action definition.

## User and Role Specification

The system uses the role and the user assigned to the role to determine the approver for a work item. You specify the user in the

purchasing organization of the freight order. For more information, see Assigning Employees to Organizational Units. You specify

the role in Customizing for Transportation Management under  Settlement

 Define Settlement Profile

## Define Approval

Levels and Roles for Workflow . For more information, see Prerequisites for Dispute Management under  Dispute Management

## Settings

 Approval levels and workflow .

The system uses the approval level of the work item and the role assigned to the user to assign a work item to an approver.

For example, you assign employees John Brown and Josephine Green to a purchasing organization in your company. You assign a

role of settlement specialist for John Brown and a role of transportation manager for Josephine Green in transaction PFCG (Role

Maintenance). In the Define Approval Levels and Roles for Workflow activity, you specify approval level 1 for the settlement

specialist role and approval level 2 for the transportation manager role. You enable the settlement profile for the approval workflow.

This is custom documentation. For more information, please visit SAP Help Portal.

74


1/14/26, 2:42 PM

When the system creates a dispute case for freight orders in the purchasing organization, it first sends a work item for the dispute

case to John Brown. When he finishes with the work item, the system then sends the work item to Josephine Green. If you assign

more than one user to the same role, the system sends the work item to all the users assigned to the role. However, the system

moves the workflow on to the next stage if just one of the users takes action on the work item.

More Information

## Subject

## More Information

Resolution of errors in workflow

Workflow Error Resolution for Dispute Management

Necessary Customizing settings required before you can use

Prerequisites for Dispute Management

dispute management

Individual aspects of dispute management

Features of Dispute Management

Information on statuses in dispute management

Statuses in Dispute Management

## Information on specifying roles

SAP Help Portal at http://help.sap.com/netweaver

. Choose the

appropriate release and in the application help, choose  SAP

NetWeaver Library: Function-Oriented View

 Application Server

 Application Server ABAP

 Other Services

 Services for

Application Developers

 SAP Business Workflow

## Role

Documentation .

## Workflow Error Resolution for Dispute Management

You can use transaction SWI2_DIAG to check if the system does not process a work item due to an error in your system settings

or a technical error. You must run the transaction to check for errors. The system provides information such as the cause of the

error, the workflow step at which the error happened, and the ID of the work item. When you resolve an error, you must choose the

Restart Workflow button on the Diagnosis of Workflow with Errors screen to process the work item again. The system continues

with the workflow from the point where the error occurs.

## Resolution of Specific Errors

The following list contains details on the errors you may encounter, and the steps you must take to resolve the errors:

## Users not assigned to your purchasing organization

You have not assigned users to the purchasing organization to which the freight order belongs. The service provider has

created the dispute case against the freight order. The system cannot choose a user and therefore cannot create a work

item. In transaction PPOME (Organization and Staffing Change) -> Staff Assignments, you must ensure your level-1

approver and level-2 approver are assigned to the purchase organization that you use in the freight order.

## Incorrect roles assigned to approval levels

You have assigned a level-1 approver and a level-2 approver to the correct purchasing organization. You have specified the

role that the system uses for level-1 approval and level-2 approval in Customizing for Transportation Management under

## Settlement

## Freight Settlement

 Freight Settlement Dispute Management

 Define Approval Levels and Roles for

Workflow . However, although you have specified the level-1 approver and level-2 approver in the purchasing organization,

you have not assigned the users to a role that you have used in the Customizing activity.

For example, the following table contains the settings you specify in transaction PPOME for the users in your purchasing

organization:

This is custom documentation. For more information, please visit SAP Help Portal.

75


1/14/26, 2:42 PM

User

## Role

Role Description

## Josephine Green

/SCMTMS/TRANSPORTATION_MANAGER

Transportation manager

## John Brown

/SCMTMS/SETTLEMENT_SPECIALIST

## Settlement specialist

The following table contains the settings you specify in the Define Approval Levels and Roles for Workflow Customizing

activity:

Approval Level

## Role

Role Description

1

2

/SCMTMS/TRANSPORTATION_PLANNER

Transportation planner

/SCMTMS/PURCHASING_CLERK

## Purchasing clerk

You have not specified a role for a transportation manager and settlement specialist in the Define Approval Levels and

Roles for Workflow Customizing activity. The system does not create a work item.

Approval level number or role not specified in the Define Approval Levels and Roles for Workflow Customizing activity

You must specify an approval level for level 1 and level 2 of the workflow in Customizing for Transportation Management

under  Settlement

## Freight Settlement

 Freight Settlement Dispute Management

## Define Approval Levels and Roles

for Workflow . You must also specify a role for each approval level in the Define Approval Levels and Roles for Workflow

Customizing activity. This ensures that the system selects a role for an approval level. The system automatically sets the

approval level when you use the Business Configuration Set (BC Set) Customizing Workflow Agents Approval Levels and

Roles for Workflow for the Define Approval Levels and Roles for Workflow Customizing activity.

## Incorrect logic in BAdI: User Determination for Dispute Case Workflow

You may have implemented incorrect logic in the BAdI: User Determination for Dispute Case Workflow in Customizing for

Transportation Management under  Business Add-Ins (BAdIs) for Transportation Management

 Settlement

 Freight

## Settlement

## Freight Settlement Dispute Management

. The system uses your standard settings to determine the

approvers for your workflow. However, you can use this BAdI to overwrite the standard settings, to add or remove workflow

approvers according to your own logic. For example, the system determines John Brown as the level-1 user. You implement

this BADI to override this standard determination. However, due to an error in the BAdI logic, the system does not identify

an approver.

  Note

If you specify levels and roles in the Define Approval Levels and Roles for Workflow Customizing activity but do not enable the

approval workflow in the relevant settlement profile, the system takes the following action:

## Displays a workflow status of Workflow Not Enabled

Does not use the level and roles settings as you have not enabled the workflow

More Information

## Subject

## More Information

Workflow process for dispute management

Workflow for Dispute Management

Prerequisites you need for dispute management

## Prerequisites for Dispute Management

This is custom documentation. For more information, please visit SAP Help Portal.

76


1/14/26, 2:42 PM

## Subject

## More Information

Key aspects of dispute management

Features of Dispute Management

Explanation of dispute management statuses

Statuses in Dispute Management

## Standard SAP workflow process

SAP Help Portal at http://help.sap.com/netweaver

. Choose the

appropriate release and in the application help, choose  SAP

NetWeaver Library: Function-Oriented View

 Application Server

 Application Server ABAP

 Other Services

 Services for

Application Developers

 SAP Business Workflow

## SAP Business

Workflow: Reference Documentation .

Resolution of errors in standard SAP workflow process

SAP Help Portal at http://help.sap.com/netweaver

. Choose the

appropriate release and in the application help, choose  SAP

NetWeaver Library: Function-Oriented View

 Application Server

 Application Server ABAP

 Other Services

 Services for

Application Developers

 SAP Business Workflow

## Role

Documentation

 Roles in Workflow

## System Administrator

 Business Workflow Administration

 Workflow System

## Administration

 Workflow Runtime Administration

## Diagnosing

Workflows with Errors .

## Dispute Case Resolution and Accruals Update

A dispute is resolved when both you and your service provider arrive at a common agreement on the charge or logistics item under

dispute. The system updates the freight order with the changed charge information.

You use the background function Creation of Freight Settlement Documents to create, change, and post the freight settlement

documents to Materials Management (MM) (see Creation and Transfer of Freight Settlement Documents). The freight settlement

document contains the changes from the freight order.

## Change Process for Freight Settlement Documents

The system uses the change process for freight settlement documents that you specify in the relevant settlement profile in

Customizing to update MM. For more information, see Customizing for Transportation Management under  Settlement

## Define

Settlement Profile .

For example, you have a freight order with a transportation charge of USD 2000. Your carrier creates a dispute case for the

transportation rate, and you resolve the dispute by changing the transportation charge to USD 2300.

Transportation Management (TM) uses the change process for freight settlement documents and the life cycle status of the

freight settlement document to post the freight settlements to MM. Depending on the update strategy you select, TM updates the

accruals to MM as follows:

Create New FSD for Delta Amount

Life Cycle Status of

System Action

Example

FSD

## New/In

Include the new charges in the new FSD when the

A new FSD for the value of USD 300 is created if

Process/Ready for

invoicing status of the freight document is

the invoicing status of the freight document is

## Accruals

Partially Invoiced. If the invoicing status of the

Partially Invoiced. If the invoicing status of the

freight document is Over Invoiced, the system

freight document is Over Invoiced, the system

This is custom documentation. For more information, please visit SAP Help Portal.

77


1/14/26, 2:42 PM

Life Cycle Status of

System Action

Example

FSD

## Accruals

Posted/Invoice

## Verified

cancels the existing FSD and recreates the new

cancels the existing FSD for USD 2000 and

FSD for the new values.

recreates the new FSD for a new value of, for

example, USD 1800.

Create a new freight settlement document

TM creates a new freight settlement

for a positive delta amount if the invoicing

document for the delta amount of USD

status of the freight order is Partially

300. On posting this FSD in MM, a new

Invoiced. A positive amount is where you

purchase order and SES entry for USD

owe your carrier an extra amount as a

300 is created.

result of the dispute resolution.

If the transportation charge were updated

If the invoicing status of the freight

to USD 1800 after you resolved the

document is Over Invoiced, the system

dispute case, TM would create a credit

executes the change process for FSD as

memo for the entire previous invoice

Reverse and Repost with New FSD.

amount for USD 2000. It would then

create a new FSD for the revised amount

of USD 1800.

## Canceled

Create a new freight settlement document with

TM creates a new freight settlement document for

the updated amount.

USD 2300.

Reverse and Repost with New FSD

Life Cycle Status of

System Action

Example

FSD

## New/In

Cancels the existing FSD and recreates the new

TM changes the charges in the freight settlement

Process/Ready for

FSD for the new values.

document from USD 2000 to USD 2300. All FSDs

## Accruals

that were created earlier are canceled and a new

FSD for the revised value USD 2300 created.

## Accruals

Creates a credit memo for the FSD and reverses

A credit memo for USD 2000 is created and linked

## Posted/Invoice

the FSD amount. A new FSD is created for the

to the FSD, and a new FSD for the revised value of

## Verified

revised value of the freight document charges.

USD 2300 is created.

## Canceled

Create a new freight settlement document with

TM creates a new freight settlement document for

the updated amount.

USD 2300.

  Note

You can run the Creation of Freight Settlement Documents background function to post the freight settlement

documents to Materials Management (MM) (see Creation and Transfer of Freight Settlement Documents).

Regardless of the settings for the Change Process for FSD in the settlement profile, if a freight settlement

document has the life cycle status Posting Started, Cancellation Requested , or Reversal Requested when you

run the background function, the system reports an error. You must wait until the life cycle status of the

settlement document is Accruals Posted or In Process before you take further action.

Background Function to Publish Freight Settlement Dispute Cases

This is custom documentation. For more information, please visit SAP Help Portal.

78


1/14/26, 2:42 PM

You can use a background function to publish freight settlement dispute cases in batches in the background. When you run the

background function, you as a requester of transportation services confirm the decisions you make to accept the relevant dispute

cases. The system updates the resolution status of the dispute case to Dispute Resolved. Also the system uses the charge details

from a dispute case that is resolved to update the changed charge information in the freight order. For more information, see

Publication of Freight Settlement Dispute Cases.

## Background Function to Create and Transfer Freight Settlement Documents

You can include, exclude, or include only the freight orders for which all dispute cases are resolved when you create and transfer

freight settlement documents in the background. For more information, see Creation and Transfer of Freight Settlement

Documents.

More Information

## Subject

## More Information

Structure of an individual dispute case, including working with a

Freight Settlement Dispute Case

dispute case

Necessary Customizing settings required before you can use

Prerequisites for Dispute Management

dispute management

Individual aspects of dispute management

Features of Dispute Management

## Integration with MM

Integration: Invoice Processing (MM-IV/SD-BIL) with TM

Charge Correction Advice Management

## Use

The charge correction advice process enables you as a logistics service provider (LSP) to create a charge correction advice

document (CCAD) to correct errors in invoices that you have received from a carrier for delivering air freight transportation

services.

The process enables you to simulate in the Transportation Management (TM) system the invoicing process that takes place

externally between you and a carrier. The CCAD enables you to post corrections to the freight settlements that you receive from

your airline carrier.

You can settle an invoice that contains charges for shipments, and corrections for errors from a previous invoice. For example, you

receive invoices from your carrier at the end of each month. After you settle an invoice for the month of July, the carrier contacts

you saying there was an error on a particular invoice. You paid for the transportation of a particular item that weighed 50 kg. The

actual weight of the item was found to be 75 kg. You agree with the carrier to pay the extra amount due, for the extra weight. At the

end of August, the carrier sends you a revised invoice that contains the corrected amount due for the extra 25 kg from the invoice

in July.

## Process

1. The carrier provides the air freight service for an air freight booking. You create a freight settlement document (FSD). This is

the planned invoice from the carrier, and simulates the invoice that the carrier creates in an external system for the service.

2. You post the settlement document to Materials Management (MM).

This is custom documentation. For more information, please visit SAP Help Portal.

79


1/14/26, 2:42 PM

The life cycle status of the FSD changes to Posted. In MM, the system creates a purchase order (PO) and a service entry

sheet (SES) for the settlement document. The amount of the PO and the total amount in document currency in the

settlement document match.

3. In Logistics Invoice Verification, you verify the invoice from the carrier and pay the settlement amount.

4. After a short period of time, the carrier contacts you with a correction. The correction could be due to different reasons,

such as an error in the weights, or incorrect rates.

5. You navigate to the relevant air freight booking and make the correction. For example, you change the weight of the item

from 100 kg to 120 kg. You create a CCAD for this from the air freight booking.

The CCAD contains the amount that has already been settled, the new delta amount to be corrected, and the final correct

settlement amount for the freight booking.

  Note

The CCAD is a new category of freight settlement document type. You can only create a CCAD for an air freight booking

that has an associated FSD that is at a life cycle status of Posted.

6. You post the CCAD to MM. In MM, a new PO is created with the following details:

PO lines for the amounts that were previously invoiced, and SES lines with the amounts that were previously

invoiced. Both documents have the Returns Indicator enabled.

PO lines for the new amounts after correction and SES lines for the new amounts after correction that are newly

determined in the CCAD

Posting the SES with the returns indicator set reverses the previously invoiced amount. MM also posts a new SES entry for

the fully adjusted correct amount. The life cycle status of the CCAD after successful posting in TM changes to Posted.

## Example

The following table illustrates how the CCAD process works for an air freight booking:

Steps in TM

Amount in

Steps in MM

## Comment

FSD/CCAD (USD)

Total freight cost in air freight booking in TM 2400

None

## None

Generate the FSD

2400

PO created, for example, PO1 with line 10.

## Regular FSD

Update the booking to reflect the

3000

## None

correction, for example, weight correction.

New total freight cost in air freight booking

Generate a new CCAD

600

SES created, for example, SES 1, linked to

PO1/10 with amount USD 2400

process

## None

No change to PO1, created in step 1

PO2 has the following items:

Item 10 for USD 3000

reflecting the new changed

amount

MM posts a return

for the old

settlement

document amount

of USD 2400.

It also posts the new

amount of USD

Item 20 for USD 2400 with

3000.

returns indicator selected

This is custom documentation. For more information, please visit SAP Help Portal.

80


1/14/26, 2:42 PM

Steps in TM

Amount in

Steps in MM

## Comment

FSD/CCAD (USD)

SES 2 created for PO2/10, for USD

3000

SES 3 returned for PO2/20, for USD

2400

The following table illustrates how the CCAD process works for an air freight booking, where the process results in negative

amounts:

Steps in TM

Amount in FSD /

Steps in MM

Comment

CCAD (USD)

Total freight cost in air freight booking

2400

None

## None

Generate the FSD

2400

PO created, for example, PO1 with line 10.

## Regular FSD

SES created, for example, SES 1, linked to

PO1/10 with amount USD 2400.

Update the booking to reflect the

2000

## None

correction, for example, weight correction.

New total freight cost in air freight booking

Generate a new CCAD

-400

No change to PO1, created in step 1

PO2 has the following items:

Item 10 for USD 2000

reflecting the new changed

amount

Item 20 for USD 2400 with

returns indicator selected

SES 2 created for PO2/10 for USD

2000

SES 3 returned for PO2/20, for USD

2400

process

## None

MM posts a return

for the old

settlement

document amount

of USD 2400.

It also posts the new

amount of 2000.

## Related Information

Freight Settlement Integration using MM External Services Management

Management of Air Freight Bookings for Airlines

## Freight Settlement Integration using Lean Services

In Transportation Management (TM), you can perform freight settlement with your service providers or carriers by creating a

freight settlement document (FSD) and posting it to Materials Management (MM) using Lean Services.

## Prerequisites

This is custom documentation. For more information, please visit SAP Help Portal.

81


1/14/26, 2:42 PM

You've disabled the checkbox TM Settlement Integration based on MM External Services Mgmt in the Customizing of

Transportation Management under  Basic Functions

## General Settings

 Define General Settings for TM . This

ensures that you've enabled lean service-based integration with Materials Management (MM).

You can also enable lean service-based integration only for selected freight documents, when the rest of the system is using

external service-based integration. To do so, you've to specify combinations of company codes and carriers in the

Customizing activity Enable Lean Services based Settlement Integration. You can do that from the Customizing of

Transportation Management under  Settlement

## Freight Settlement

  Integration for Settlement Posting

## Service

Procurement - Lean Services . The system enables lean service-based integration only for those freight documents where

it finds the combination of these company codes and carriers.

You've integrated TM that enables you to post supplier invoices that refer to freight orders. These freight orders are based

on purchase orders with lean service items. You can do that from the customizing activity Activate Integration of

Transportation Management (TM) in Customizing of Materials Management under  Logistics Invoice Verification

 Incoming Invoice .

To integrate to an internal MM system, you've configured the following Customizing settings:

Assign Purchasing Info for Posting Lean Service Integration

Assign Val. Class, Acc. Assignment Category, and Conditions to Charge Types

Mapping for Cost Distribution when you've enabled cost distribution in the freight settlement document

For more information, see Customizing for Transportation Management under  Settlement

## Freight Settlement

 Integration for Settlement Posting

 Service Procurement - Lean Services .

The system determines the logical system from the freight units that are assigned to the freight document. The freight

documents are created from the requirement documents, such as sales orders, purchase orders, and so on. For more

information about organizational models, see Organizational Management.

## Company Code and Plant

For more information, see Company Code and Plant in Posting Freight Settlements using Lean Services

Freight cost confirmation and execution status

For more information, see Freight Cost Confirmation and Posting.

## Process

In lean service, the freight settlement document is created and posted as a part of the posting step from the related freight

documents. For more information, see Monitor Freight Documents for Accrual.

1. You create and post the freight settlement document.

The system creates and posts the individual settlement document for a freight order, freight booking, or

consignment order. You can see the freight documents from the Monitor Freight Documents for Accrual app. The

system automatically creates and posts the settlement document based on the data in the freight orders or freight

bookings.

You can create and post multiple FSDs using the Mass Creation of Freight Settlement Documents function. You can

run transaction /SCMTMS/SFIR_CREATE (report /SCMTMS/SFIR_CREATE_BATCH). For more information, see

Creation and Transfer of Freight Settlement Documents using Integration with Lean Services.

You can create separate freight settlement documents for each of the invoicing carriers in a rail freight order, where

you have a different invoicing carrier for each stage in the order. This feature gives you the flexibility to work with rule

11 business situations in North America.

This is custom documentation. For more information, please visit SAP Help Portal.

82


1/14/26, 2:42 PM

In rule 11 situations, the header carrier receives the order from the customer and can execute one or more of the

stages. The header carrier is the carrier that you specify in the  General Data

 Transportation  screen area of the

freight order. The invoicing carrier is the carrier who bills the customer for the shipment and you specify this carrier

at stage level in the rail freight order.

For more information about rail freight orders, see Rail Transportation.

You can create a settlement document for each additional agreement party if you have an existing freight order or

freight booking that contains one or more additional agreement parties. For more information, see Additional

Agreement Parties.

The system settles a parcel freight order in the same way as it settles a standard freight order. For more information

about parcel freight orders, see Parcel Shipment.

When you create and post a freight settlement document, by default the system uses the date from the relevant

Event for Freight Cost Confirmation as the settlement date. For more information, see Freight Cost Confirmation

and Posting

You can have multiple charge types in a charge item. As standard in lean services, MM creates a purchase order item

for every independent charge type and applies tax to the purchase order(PO) item. Dependent charge types are

represented as condition types for its parent service in the PO item.

TM transfers the settlement information, including the source location and destination location information for

every independent charge types to MM. The location information enables MM to determine different tax codes/rates

for different locations in the purchase order item.

For more information, see Setting Up Tax Rates for Purchasing Transportation Services.

When the SES is accepted and posted, accruals are booked to accounting. The SES serves as the basis for invoice

verification in MM.

The settlement date from the freight settlement document is used as the Doc. Date (Document Date) in the header

of the purchase order.

The SES dates on the header of the Accept. Data (Acceptance Data) tab page are taken from the following places:

Posting date from the settlement date in the freight settlement document

Document date as the system date

## Posting Periods

You can post the freight settlement document only if the posting periods in MM and Financial Accounting (FI) are

both open for the posting date of the SES. If the posting period is closed, you have the following options:

## Open the closed posting period

You must open the posting period for both MM and FI.

In FI, open the posting period in Customizing under  Financial Accounting

 Financial Accounting Global

Settings

## Ledgers

 Fiscal Year and Posting Periods

## Posting Periods

 Open and Close Posting Periods

.

In MM, open the posting period in the SAP Menu under  Logistics

 Materials Management

 Material

Master

## Other

 MMPV – Close Period  or MMRV - Allow Posting to Previous Period.

Change the Posting Date in the relevant freight document for a Business Partner under  Charges

Posting Date  tab to match the open posting period and post the freight document again.

2. When the settlement document is posted successfully, its lifecycle status is set to Posted. If issues are encountered during

posting, the lifecycle status is set to Posting Failed and the confirmation status has the status of the corresponding step in

This is custom documentation. For more information, please visit SAP Help Portal.

83


1/14/26, 2:42 PM

which the issue was encountered. For example, the confirmation status Purchase Order Creation Failed indicates that the

purchase order creation failed.

If you encounter issues when you post to internal MM, the system logs the issues. You can review the issues on the

Application Log tab of the freight settlement document.

3. Invoice verification and Evaluated Receipt Settlement (ERS)

MM bases the expected invoice on the SES confirmation. When the invoice is posted against the freight document,

the lifecycle status of the settlement document is set to Invoice Verified.

The automatically generated invoice is based on the data from the settlement document, if you perform ERS.

  Note

You can't cancel the settlement document when the invoice is posted against the settlement document in MM and the

settlement document has a lifecycle status of Invoice Verified.

When you successfully cancel the settlement document, the posting date of the canceled SES is determined based on

the event for freight cost confirmation. Once the posting date is determined based on the event for freight cost

confirmation, the same date is also copied over to the cancellation posting date. This ensures that while canceling the

accruals, the cancellation of posting is done in the same financial period where the posting was done earlier.

More Information

## Subject

## More Information

Enable the system to determine the business partners that you use

Business Partner Determination

in different business document types.

Make certain changes to your freight costs in the freight order or

Flexibility in Freight Charge Changes

freight booking after you post accruals

Allow for unplanned changes in your freight settlement process

Reversing a Freight Settlement Document

Combination of life cycle and confirmation status

Life Cycle Status of Freight Settlement Documents

Invoicing of freight documents

## Invoicing Freight Documents

## Life Cycle Status of Freight Settlement Documents

The life cycle status shows the current status of the freight settlement document in the business process. The confirmation status

indicates the result of the last posting step of the freight settlement document to Materials Management (MM).

The following table lists the combination of important life cycle and confirmation statuses:

Life Cycle Status

Confirmation Status

## Description

Ready for Accruals

Not Posted

## Posted

## Not Confirmed

Freight settlement document created in

blocked status but posting isn't yet initiated

Freight settlement document initiated for

posting but MM documents aren't yet

created

This is custom documentation. For more information, please visit SAP Help Portal.

84


1/14/26, 2:42 PM

Life Cycle Status

Confirmation Status

Description

Posted

Canceled

## Confirmed

Freight settlement document posted

Not Confirmed

successfully

Freight settlement document initiated for

cancellation but MM documents aren't yet

canceled

Canceled

## Confirmed

Freight settlement document canceled

successfully

## Posting failed

Purchase order creation failed

The creation of the purchase order failed

Posting failed

## SES Creation Failed

when the freight settlement document was

posted. For information about the error, see

the Application Log tab in the freight

settlement document.

The creation of the service entry sheet

failed when the freight settlement

document was posted. For information

about the error, see the Application Log tab

in the freight settlement document.

## Posting Failed

Cost distribution document creation failed

The creation of the settlement

management documents with the cost

distribution data failed when the freight

settlement document was posted. For

information about the error, see the

Application Log tab in the freight

settlement document.

Cancellation posting failed

Purchase Order Cancellation Failed

The cancellation of the purchase order

failed when the freight settlement

document was canceled. For information

about the error, see the Application Log tab

in the freight settlement document.

Cancellation posting failed

## SES Cancellation Failed

The cancellation of the SES failed when the

freight settlement document was canceled.

For information about the error, see the

Application Log tab in the freight

settlement document.

Cancellation posting failed

Cost distribution document cancellation

During the cancellation of the freight

failed

settlement document, the cancellation

posting of settlement management

documents with the cost distribution data

failed. For information about the error, see

the Application Log tab in the freight

settlement document.

Company Code and Plant in Posting Freight Settlements using
## Lean Services

The company code in the freight settlement process is used to book the freight accruals to financial accounting (FI) under the

company code. The plant is required in the posting process during the creation of the service purchase order as part of the posting

This is custom documentation. For more information, please visit SAP Help Portal.

85


1/14/26, 2:42 PM

step for a freight settlement document.

## Prerequisites

Procuring company code determination is enabled only when you've specified the following in Customizing for the freight

document type:

The document type is Relevant for Subcontracting.

Subcontract. Checks field has the value Basic Additional Checks.

For more information, see the Basic Settings section in the following Customizing:

Freight Order Management

## Freight Order

 Define Freight Order Types

Freight Order Management

## Freight Booking

 Define Freight Booking Types

Freight Order Management

## Consignment Order

 Define Consignment Order Types

## Procuring Company Code

The procuring company code is responsible for the procurement of a transportation service from the carrier or transportation

service provider of a freight document. The procuring company code is available in the freight document under  General Data

 Organizational Data .

The procuring company code is mandatory in the freight document and as is taken over in the freight settlement document. If the

procuring company code is defined in the freight document, it's transferred to the freight settlement document.

## Plant

The system determines the plant to be populated in the purchasing order item as follows:

The plant from the underlying transactions (orders and deliveries) if they're all unique from the linked freight units in the

freight document.

Use the plant defined as the default plant for the company code in Customizing for Transportation Management under

## Settlement

## Freight Settlement

 Integration for Settlement Posting

 Assign Default Plant for Company Code  to

integrate to an internal MM system.

## Freight Cost Confirmation and Posting

Freight cost confirmation is a prerequisite step to trigger the posting of the freight cost to financial for a freight document. Freight

costs can be confirmed based on the execution status of the freight document or automatically using business rules.

## Prerequisites

The freight document has reached the following state:

Freight orders: Checkout of last or only stop belonging to your organization.

In cases where the source and destination stop don't belong to your organization, then the Departure at the source stop is

used.

Ocean freight bookings: Shipped on Board

## Air freight bookings: Uplift Confirmed

This is custom documentation. For more information, please visit SAP Help Portal.

86


1/14/26, 2:42 PM
## Freight Cost Confirmation Based on Execution Status

To confirm the freight costs, the system considers the execution events for the freight documents. Execution status is used as one

of the prerequisites to create freight settlement document. You can configure the event relevant for the freight cost confirmation in

the Execution Settings section in the Customizing for Transportation Management under:

Freight Order Management

## Freight Order

 Define Freight Order Types

Freight Order Management

## Freight Booking

 Define Freight Booking Types

Freight Order Management

## Consignment Order

## Define Consignment Order Types

Following are the relevant events and their effects on freight cost confirmation:

Not Relevant: If you select this value in the associated freight order, freight booking, or consignment order type, the system

doesn't change the invoicing status to Ready for Confirmation. The system can't confirm the freight costs and perform the

follow-on processes unless the invoicing status is Ready for Confirmation.

  Note

For freight documents using lean service-based integration, you can't use Not Relevant as the value for the Customizing

setting Event for Freight Cost Confirm. because the invoicing status Ready for Confirmation is a mandatory

requirement for the follow-on processes.

Checkout, Departure: On the execution of these events, the system sets the status of the freight document as Ready for

Confirmation and you can start the follow-on processes.

Freight Booking: Start of Main Carriage: This is relevant only for freight bookings and on execution of this event the system

sets the status of the freight booking as Ready for Confirmation and you can start the follow-on processes.

## Automatic Freight Cost Confirmation

You can automate the confirmation and posting of freight costs during freight document processing by creating a condition with

the condition type /SCMTMS/TOR_FRC_CONF (Automatic Freight Cost Confirmation).

When creating the condition, ensure you specify the following details:

Carrier/service provider

Procuring company code

Purchasing organization

## Enable automatic confirmation

When a freight document matches the condition and has reached the relevant state, the system automatically confirms and posts

the freight costs. For more information, see Condition.

## Related Information

Invoicing Status of Freight Documents using Lean Services

## Invoicing Freight Documents

This is custom documentation. For more information, please visit SAP Help Portal.

87


1/14/26, 2:42 PM

You can post an invoice for a freight document and carrier or logistics service provider combination at the level of a charge

element. You can review the amounts and quantities associated with a freight charge element during invoice processing.

## Prerequisite

You've integrated TM that enables you to post supplier invoices that refer to freight orders. These freight orders are based on

purchase orders with lean service items. You can do that from the customizing activity Activate Integration of Transportation

Management (TM) in Customizing of Materials Management under  Logistics Invoice Verification

 Incoming Invoice .

## Key Features

You can create an invoice receipt item for an independent charge. Wherever applicable, the system merges or includes a

dependent charge in an invoice receipt item.

When you post an invoice for any charge, the system changes the posting status of the freight charge to Invoice Verified.

The system includes the freight document in the document flow.

## Variances in Freight Invoices

For a price variance, the system automatically distributes the price difference at the level of logistics document and delivery

item in the freight document. The system creates a freight cost allocation document for a price variance in a freight invoice.

It then automatically posts the price difference to an expense or material account depending on the business scenario. You

also get a price variance when you enter an unplanned freight cost for an invoice. For more information see, Manage

Variance Posting Errors.

## Unplanned Freight Cost

In the Create Supplier Invoice - Advanced app (App ID: MIRO) you use the fields Freight Order and Charge Type within the

G/L Account section to support the posting of supplier invoices with unplanned freight costs.

If you want to create an invoice that refers to a freight order with unplanned freight costs against a charge type which isn't

part of your freight order, the unplanned freight cost is posted as an unplanned G/L account item for which the

transportation management fields Charge Type and Freight Order are filled accordingly.

In addition, with the Supplier Invoice - Create (B2B, Inbound, Asynchronous) service, also known as InvoiceRequest_In,

you can now post supplier invoices with unplanned freight costs. For more information, see InvoiceRequest_In - Item.

The system doesn’t update the freight document with the unplanned freight cost.

## Invoice Processing

You can process an invoice for a freight document as follows:

## Create Supplier Invoice - Advanced

You can use this app to create and verify an invoice from your carrier or service provider.

Supplier Invoice - Create (B2B, Inbound, Asynchronous)

Your carrier or service provider can use an electronic business-to-business (B2B) message to submit an invoice to you, the

shipper.

For all transactions related to invoicing, see Invoicing Freight Orders.

## Related Information

Invoicing Status of Freight Documents using Lean Services

This is custom documentation. For more information, please visit SAP Help Portal.

88


1/14/26, 2:42 PM

## Submission of Carrier Invoice

In an invoice submission process, the process of settlement between you and your service provider is based on a carrier invoice

that your service provider submits to you against one or more freight orders. Your service provider has executed the transportation

requirements in your freight order before sending the invoice. You have a trusted relationship with your service provider, and your

service provider sends you a carrier invoice.

## Prerequisite

You must specify a carrier invoice type in Customizing for Transportation Management under  Settlement

## Freight Settlement

 Define Carrier Invoice Types .

You must specify a carrier invoice type as the default type.

## Integration

The carrier invoice is integrated with the following objects and systems:

## Freight settlement dispute case

Your service provider can submit an invoice for one or more freight orders.

Transportation Management (TM) captures the invoice details submitted by your service provider. If there are differences

between the submitted invoice and the expected values for the freight order, TM creates a dispute case and links it to the

carrier invoice. If your service provider submits an invoice that matches the expected value for the freight order, TM doesn't

create a dispute case.

For more information on dispute, see Dispute Management for Freight Settlements

## Posting of the carrier invoice to MM

You can use the Posting of Carrier Invoices background function to post the carrier invoices that are ready for posting to

MM. MM creates incoming invoices. For more information, see Posting of Carrier Invoices.

You can also post one or more carrier invoices directly as follows:

Under Freight Settlement, choose  Worklist

 Overview Freight Settlement Documents

 Carrier Invoices .

Under Freight Settlement, choose  Carrier Invoice

 Display Carrier Invoice .

You can also automate the carrier invoice posting directly by enabling Post Invoice Immediately for the carrier invoice type in

Customizing for Transportation Management under  Settlement

## Freight Settlement

 Define Carrier Invoice Types .

The system determines the logical system behind the business system group that you’ve linked to your purchase organization data

for the freight order, freight booking, or service order that is a part of the carrier invoice. The business system group represents the

SAP ERP system or SAP S/4HANA system from which you replicate the purchasing organization in the organization model.

For more information on organizational model, see Create and Merge Organizational Hierarchy under  Transportation

Management

## Master Data

 Organizational Management

 Organizational Model

.

You use the InvoiceRequest_In interface to create a carrier invoice in TM. For more information, see Carrier Invoice - Create

(B2B) for Lean Service Procurement.

## Features

## Possible Actions for Carrier Invoice

This is custom documentation. For more information, please visit SAP Help Portal.

89


1/14/26, 2:42 PM

The following table explains the possible actions that are available to you:

## Action

Action Description

## Reject Invoice

You can reject a carrier invoice at any time, provided the carrier invoice isn't yet posted to MM.

When rejecting a carrier invoice, you can capture notes giving your reasons for rejection. Your service

provider must create a new carrier invoice for the freight order.

When you reject a carrier invoice that has an open dispute case, the system automatically closes the

dispute case. This saves you from taking extra steps to cancel the dispute case manually.

## Post

You can post the carrier invoice to MM provided the carrier invoice satisfies all of the following

conditions:

No dispute case exists or the dispute case has a life cycle status of Resolved

Has a life cycle status of other than Rejected

All associated freight orders have the invoicing status Posted

All associated freight settlement documents have the status Accruals Posted

Has a block status of Not Blocked

## Release

Releases the carrier invoice in the life cycle status Draft. When there are carrier invoices with charges

linked to the resolution base of the freight order, the carrier invoice is created in life cycle status Draft.

When the resolution base information is assigned to the repeating charges in the carrier invoice, this

action can be used to release the invoice for further processing.

## Set to Draft

Recall a released invoice in case that you want to change the resolution base information for the

charge lines. This action cancels the relevant dispute case for the associated carrier invoice.

## Life Cycle Status

The life cycle status indicates the resolution status of the overall carrier invoice. The following table explains what the key life cycle

statuses mean:

Status

## Draft

## Status Description

When there are carrier invoices with charges linked to the resolution base of the freight order, the

carrier invoice is created in life cycle status Draft.

## In Process

The carrier invoice satisfies one or more of the following conditions:

All the charge lines where you expect resolution base information have been resolved.

Submitted by your service provider but not yet accepted and posted to MM

Has disputes that aren't yet resolved

## Not yet posted to MM

Transferred, but failed to post to MM

## Ready for Posting

The carrier invoice satisfies all of the following conditions:

No dispute case exists or the dispute case has a life cycle status of Resolved.

## Has a life cycle status of other than Rejected

All associated freight orders have the invoicing status Completely Invoiced.

This is custom documentation. For more information, please visit SAP Help Portal.

90


1/14/26, 2:42 PM

## Status

## Status Description

All associated freight settlement documents have the status Accruals Posted.

Has a block status of Not Blocked

Has a consistency status of Consistent

## Carrier invoice Posted

The carrier invoice has been successfully posted as an invoice document in MM.

## Rejected

You rejected the carrier invoice for business reasons. For example, the tax amounts in the invoice were

incorrect

## Dispute Case Status in a Carrier Invoice

In an invoice submission process, your service provider submits a carrier invoice against one or more freight orders. You service

provider can also submit an invoice that has a different charge amount to what you expect as a shipper. TM subsequently creates a

dispute case so that you can come to a consensus on the disputed items with your service provider. The dispute case status

reflects the processing status of the dispute on the carrier invoice. The following table explains what the individual dispute case

statuses mean:

## Status

Status Description

## No Dispute

The default status of a carrier invoice, where there are no dispute cases on the charges or logistics

information in the freight orders covered by the carrier invoice.

## Awaiting Your Approval

You as the service requester must act to approve, make a proposal, or reject the dispute created by

your service provider.

## Resolved

Both you as the service requester and your service provider have agreed on common ground in the

dispute and you both have agreed on a decision. You've accepted the dispute case.

## Rejected by You by Carrier

You as a service requester reject a carrier invoice from your service provider. This closes the associated

## Invoice

dispute case.

## Block Status

The block status prevents the carrier invoice from being posted to MM. For example, your service provider can use an invoice

number reference from their own transportation system, such as a forwarding order number, a waybill number, or an invoice

number. When your service provider submits a carrier invoice, TM checks to ensure that your service provider hasn't used the

same invoice number reference ID to submit an invoice previously in the same day. If your service provider has used the same

invoice number reference previously in the same day, as standard TM blocks the carrier invoice and displays the reason Invoice

number reference already used on the carrier invoice screen. This protects you from creating duplicate invoices when you submit

invoices electronically, for example, when you use machine-to-machine (M2M) messages or business-to-business (B2B)

messages.

You can specify your own additional blocking checks. For example, you can block a carrier invoice if the freight orders in the carrier

invoice have a delivery date that is later than the current date. As the shipper, this enables you to pay for the transportation service

only when all of the parts of the transportation are completed. For more information, see Customizing for Transportation

Management under  Business Add-ins (BAdIs) for Transportation Management

## Settlement

 Freight Settlement

## Freight

## Settlement Dispute Management

 BAdI: Additional Checks for Blocking Carrier Invoices .

You can't further process a carrier invoice when it's blocked. To unblock the carrier invoice, choose Unblock on the carrier invoice

screen. For more information on block statuses, see Customizing for Transportation Management under  Basic Functions

## General Settings

 Define Block Reason Codes .

## Confirmation Status

This is custom documentation. For more information, please visit SAP Help Portal.

91


1/14/26, 2:42 PM

You can use the confirmation status to track the posting of a carrier invoice to MM. The status indicates the result of the last

integration interaction between TM and MM. The following table explains what the main confirmation statuses mean:

## Status

Not Posted

Not Confirmed

Confirmed

## Description

TM hasn't posted the carrier invoice to MM.

TM has initiated the posting of the carrier invoice to MM, but the

posting process isn't yet complete.

Carrier invoice was posted successfully and an invoice was created

in MM.

## Invoice Posting Failed

Posting of carrier invoice couldn't be completed due to errors.

More Information

## Subject

More Information

Background processing

Posting of Carrier Invoices

function for posting carrier

invoices to MM

Individual aspects of dispute

Features of Dispute Management

management

## Process a carrier invoice using

Carrier Invoice - Create (B2B) for Lean Service Procurement

## Web Services

Details of dispute management

Dispute Management for Freight Settlements

in Settlement integrated with

MM using External Service

Management or Lean Services

## Resolution Based Charges

Working with Resolution-Based Charges

Automatic Determination of

Determine Logistical References Automatically

Logistical References

Manage Variance Posting Errors

App ID: F7090

With this app, you can monitor the errors that arise when you post a price variance for a carrier invoice. You can review the reason

for why a variance posting failed and you can also repost the variance after you correct the errors. The app displays the variance

posting errors that the system detects when it posts a carrier invoice for which it couldn't create a freight cost allocation

document.

After you correct the errors and successfully repost the variance, the system removes the relevant carrier invoice from the app.

## Key Features

You can use this app to do the following:

Monitor carrier invoices for errors when you post a variance

This is custom documentation. For more information, please visit SAP Help Portal.

92


1/14/26, 2:42 PM

View the reason for why a variance posting failed

## Repost the failed variance posting for the carrier invoice

Update the posting date when you repost the carrier invoice for failed variance postings

## Additional Details

You can update the posting date when you repost the variance from the app. When you repost the variance, the system creates a

freight cost allocation document. It distributes the variance amounts to the relevant delivery item or predecessor order item

associated with the freight document. It then posts the variance amount to material valuation or to an expense account (general

ledger) based on the business scenario.

Supported Device Types

Desktop

## Tablet

## Reversing a Freight Settlement Document

In your business, you are a requester of transportation services, such as a shipper, and you have a close working relationship with a

provider of transportation services, such as a carrier. You've enabled a self-billing (evaluated receipts settlement) process with a

particular service provider. You automatically pay the service provider according to the charge details in your freight order, freight

booking, or service order.

Occasionally you can have the following business scenario:

1. Your carrier started to execute your transportation request.

2. You accrued the freight cost in Materials Management (MM).

3. You created a self-billing invoice to update the open item in your accounts payable.

Then your carrier encounters some unplanned issues. For example, the carrier doesn't deliver a particular transportation service

due to execution issues such as a vehicle breakdown. Also, you can encounter incorrect pricing information in Transportation

Management (TM).

To resolve the issues, you need to reverse the freight settlement document in TM. When you transfer the reversal to MM, you need

to reverse the associated purchase order, service entry sheet (SES), and accruals posting in MM. You need MM to then run the

evaluated receipts settlement for the particular freight order. This posts a credit memo that reverses the self-billing invoice that

was created earlier. You can only reverse the freight settlement document when it has the life-cycle status Invoice Verified.

The following table describes the steps that you must take to reverse the freight settlement document:

Module

TM

Action

## Result

Life Cycle Status of FSD

Choose Reverse Document in

TM initiates the reversal

## Reversed

the freight settlement

process.

document.

This is custom documentation. For more information, please visit SAP Help Portal.

93


1/14/26, 2:42 PM

Module

MM

Action

## Result

Life Cycle Status of FSD

The approval of a service entry

System revokes the SES.

## Reversed

sheet is revoked and the status

of the service entry sheet is

reset to In Process.

MM

You run transaction MRRL

This creates a credit memo to

## Credit Memo Created

(Evaluated Receipt Settlement

reverse the previously posted

(ERS) with Logistics Invoice

invoice.

Verification). Under the

Transportation Management

screen area, you enter the

relevant TM freight order

number by selecting this from

the search help. For more

information, see Invoicing

Freight Documents.

TM updates the invoicing status of the relevant freight order to Ready for Posting, and you can create a new freight settlement

document for the freight order.

## Related Information

Evaluated Receipt Settlement (ERS)

## Invoicing Freight Orders

## Setting Up Tax Rates for Purchasing Transportation Services

You use Transportation Management (TM) in SAP S/4HANA, private cloud edition, and you post freight cost accruals to Financials.

When you post freight cost accruals, the system needs extra information to determine the tax code. You must specify extra

conditions to meet your business requirements. The system determines tax in the service purchase order item when it creates the

item during the posting step of freight cost accruals.

If you use the evaluated receipt settlement (ERS) process with your carriers and suppliers, to perform any follow-on steps you

must determine taxes when you post freight cost accruals.

To enable tax determination in the posting step of freight cost accruals, the system determines the value of the field KOMP-TAXIL

(Tax Indicator: Import) as described in the following table:

TAXIL (Tax Indicator: Import)

Description

3

4

5

6

7

## Transportation service for export of goods

Transportation service for export of goods in EU (European Union)

Transportation service for domestic movement of goods

Transportation service for import of goods

## Transportation service for import of goods in EU

The system uses the following criteria to specify the value of the TAXIL field:

Country/region of departure and country/region of arrival of the freight document or stage

This is custom documentation. For more information, please visit SAP Help Portal.

94


1/14/26, 2:42 PM

## Country/region of the freight procuring company

The following table gives you an example of the settings that can apply:

Country/region Code of

Source Location

Destination Location

TAXIL Indicator

TAXIL Indicator

Freight Procuring

Country/Region of

Country/Region of

Description

Company

Freight

## Freight

Document/Stage

Document/Stage

DE (Germany)

DE (Germany)

U.S. (United States)

DE (Germany)

DE (Germany)

FR (France)

DE (Germany)

DE (Germany)

DE (Germany)

DE (Germany)

U.S. (United States)

DE (Germany)

DE (Germany)

FR (France)

DE (Germany)

3

4

5

6

7

Transportation service

for export of goods

Transportation service

for export of goods in EU

Transportation service

for domestic movement

of goods

Transportation service

for import of goods

Transportation service

for import of goods in EU

The system also takes the tax indicator KOMP-TAXIR (Tax Indicator: Region) into account when it determines the tax code. The

system determines the TAXIR (Tax Indicator: Region) as described in the following table:

TAXIR (Tax Indicator: Import) Description

0

1

Same region

## Different region

The system compares the regions of the source and destination locations and determines the TAXIR (Tax Indicator: Region) as

described in the following table:

Source Location Region

Destination Location Region

TAXIR (Tax Indicator: Region)

TAXIR Description

HH (Hamburg)

HH (Hamburg)

HH (Hamburg)

BW (Baden-Wuerttemberg)

HH (Hamburg)

CA (California)

IN (Indiana)

HH (Hamburg)

0

1

1

1

Same region

Different region

Different region

## Different region

You can also configure tax determination for source and destination country/region and postal code by following the configuration

steps in Pricing and Conditions.

The fields that can be used to determine the country/region and postal code are described in the following table:

Field Name

KOMK-SLAND1_A

## Description

## Tax country/region departure

This is custom documentation. For more information, please visit SAP Help Portal.

95


1/14/26, 2:42 PM

Field Name

Description

## KOMK- SLAND1_Z

Tax country/region destination

KOMK- REGIOA

KOMK- REGIOZ

KOMK- PSTLZA

## KOMK- PSTLZZ

Departure region (federal state, county, province, duchy)

Destination region (federal state, county, province, duchy)

Departure postal code

## Target postal code

For more information about specifying the tax determination settings, see Set Tax Rates - Purchasing .

Monitor Freight Documents for Accrual

App ID: F4329

With this app, you can monitor your freight documents to post accruals. You can confirm a freight document to post the freight

cost to Financial Accounting for accruals. You can monitor your freight documents in case there are errors during the posting

process. To post the freight costs to Financial Accounting, you must confirm that the charges for a freight document are a correct

reflection of the planned costs to be paid to the carrier. When you confirm a freight document for posting, the system posts the

freight costs to Financial Accounting. You can also identify freight documents for which you have successfully posted the freight

costs.

## Key Features

You can use this app to perform the following tasks:

Confirm freight costs for posting to Financial Accounting for accruals

View freight documents that are successfully posted to Financial Accounting

Cancel postings for freight documents that are successfully posted to Financial Accounting

Monitor freight documents that have errors when you post them to Financial Accounting

Display the errors that the system encountered when it posted your freight documents

Post or cancel posting for freight documents for which the system encountered errors during posting

## Additional Details

You can check out road and rail freight orders from the Create Road Freight Order or Create Rail Freight Order app. When you

check out the last or only stop of the freight order and the stop belongs to your organization, the system gives the freight order a

posting status of Ready for Confirmation. In cases where the source and destination stop don't belong to your organization, the

posting status of the freight order is set to Ready for Confirmation after departure at the source stop. For more information, see

Freight Cost Confirmation and Posting.

You can set an ocean freight booking to Shipped on Board. The system gives the freight booking a posting status of Ready for

Confirmation. For more information, see Freight Booking. You can set an air freight booking to Uplift Confirmed. The system gives

the air freight booking a posting status of Ready for Confirmation. For more information, see Management of Air Freight Bookings

for Airlines.

You can view these freight documents in this Monitor Freight Documents for Accrual app, in the For Confirmation view.

This is custom documentation. For more information, please visit SAP Help Portal.

96


1/14/26, 2:42 PM

When your freight documents are in the invoicing status Ready for Confirmation and you've verified that the planned costs are

correct, you can confirm the freight cost for posting to Financial Accounting.

The system sets the invoicing status to Posted when the posting is successful or to Posting Failed if it encounters errors during

posting. In the Errors view, you can show the list of freight documents that have an invoicing status of Posting Failed. In the Posted

view, you can see the list of freight documents that have an invoicing status of Posted.

Supported Device Types

Desktop

## Tablet

Monitor Freight Settlements for Accrual

App ID: F8720

With this app, you can monitor the freight settlement postings for your freight documents.

## Key Features

This app provides the following key features:

## Unblock or cancel blocked freight settlement documents

You can see a list of freight documents under the tab Ready for Accruals that are blocked. You can navigate to these

documents and see the reason for their block and act upon it. You can then either Unblock the freight document and then

Post the freight settlement to Materials Management (MM) for further processing or Cancel the blocked freight settlement

document.

## View posting failed freight settlement documents

You can see a list of freight documents for which posting of accruals has failed under the Posting Failed tab and navigate to

these documents to see the specific errors that occurred during the accrual process. Posting typically fails when the

creation of a follow-on document encounters an error.

Once you resolve the errors, you can Reprocess the document.

## View posted freight settlement documents

You can see a list of freight documents that are successfully posted to MM, under the Posted tab. You navigate to these

documents and then to the Document Flow tab to see any follow-on documents that were created. If necessary, you can

also Cancel the accruals.

## View cancellation failed freight settlement documents

You can see a list of freight documents for which cancellation failed, under the Cancellation Failed tab. You can view the

reason for the failure under Application Log. Once you've resolved the error, you can Reprocess the freight settlement

document. Cancellation typically fails when an error prevents the cancellation of a related follow-on document.

Supported Device Types

Desktop

## Tablet

This is custom documentation. For more information, please visit SAP Help Portal.

97


1/14/26, 2:42 PM

## Smartphone

## Posting of Allocated Freight Costs

You can allocate freight costs at the level of document and delivery item in a freight document. The system posts the costs to a

material valuation in an inbound process, and to an expense account (general ledger) in an outbound process.

The following graphic gives a high-level overview of the settlement process for shippers, and is followed by an explanation:

In step 1, you create an order in the Sales and Sourcing and Procurement components.

In 2, you create a freight unit (FU) out of the order.

In 3, you plan the FUs in a freight document.

In 4, you post the freight document.

In 5a, the system creates a service purchase order (PO) and service entry sheet (SES) in Sourcing and Procurement.

In 5b, the system also posts the freight cost to material valuation for an inbound process or expense for an outbound

process.

In 6a, you receive the invoice from the carrier.

In 6b, you post the invoice against the accrued freight cost, from step 5a.

7 applies if you have a price difference in an invoice variance. The system posts the variance amount to a material valuation

for an inbound process or to an expense for an outbound process.

For example, you have a net amount in document currency of USD 1845 for a freight document consisting of two deliveries, with a

cost distribution of USD 800 for product 1 for delivery 1, and USD 1045 for product 2 for delivery 2. When you post the freight

document, the system takes the following steps:

Creates a service purchase order for USD 1845 and creates an SES for USD 1845.

Creates a freight cost distribution document with each product as an item.

Each item has the amount of the distributed cost, USD 800 for product 1, and USD 1045 for product 2.

You can post the distributed cost to material valuation or general ledger. Depending on whether the process is inbound or

outbound, the freight cost allocation document posts the freight cost to the respective cost objects.

This is custom documentation. For more information, please visit SAP Help Portal.

98


1/14/26, 2:42 PM

For example, in an outbound process you have a freight document with cargo items that are linked to the deliveries in a sales order.

The system posts the freight cost to the general ledger. When you post the freight document with a freight cost distribution, the

system passes on the distributed costs to the freight cost allocation document. The system takes the following steps:

Copies the references from the freight document cost distribution and gets the linked underlying delivery items.

Copies the product and quantities in the delivery item to the items in the freight cost distribution document for product 1

and product 2.

Copies the account assignments for the respective item in the freight cost distribution document from the underlying sales

order item to which the delivery item is linked.

Copies the allocated amounts to the items in the freight cost allocation document (USD 800 for product 1 and USD 1045

for product 2).

Examples of an account assignment can be cost objects including a cost center, profit center, Controlling – Profitability Analysis

(CO-PA) segment, or an internal order.

## Additional Details

You can review the relevant freight cost allocation document in the Manage Freight Cost Allocation Documents app. You can view

the freight cost allocation documents by entering the freight order or freight booking in the Monitor Freight Cost Allocation

Document Items app. The app provides list reporting at the level of freight cost allocation document item. The system

automatically releases the freight cost allocation document to accounting.

In special cases, you can release the freight cost allocation document in the Manage Freight Cost Allocation Documents app or

the Schedule Document Release app.

The following graphic displays a posting pattern for a freight document and is followed by an explanation:

In step 5a, the system uses the SES to post the total freight cost to an intermediate freight clearing account. In step 5b, the system

uses the freight cost distribution document to allocate the freight cost to Sourcing and Procurement for an inbound process, or to

a general ledger expense account for an outbound process. The system uses the material information and the account

assignments from the underlying sales orders or purchase orders.

In step 5a, you post freight costs in an inbound and outbound process. The system uses the account posting key GBB as the offset

entry for inventory posting. This points to a freight clearing account or a similar clearing account.

This is custom documentation. For more information, please visit SAP Help Portal.

99


1/14/26, 2:42 PM

In step 5b, you post freight costs in an inbound process. You post the freight cost to a material valuation. The freight clearing

account key comes from the pricing procedure (also known as a calculation schema) in the freight cost allocation document. The

material and its attributes determine the inventory posting account. The system posts the costs to BSX inventory posting or PRD

cost price differences. The system bases the postings on the typical material posting that you set up, depending on the price

control of the material and the material stock position.

Also in step 5b, you post the freight costs in an outbound process. You post the freight cost to an expense account. The system

uses the pricing procedure from the freight cost allocation document to determine the account keys for freight clearing and freight

expense.

## Prerequisites

## Distribution profile

The system uses criteria such as gross weight, net weight, gross volume, and distance times weight to perform freight cost

distribution. To configure a distribution profile, see the Customizing Activity Define Charges Profiles under Customizing for

Transportation Management

 Basic Functions

 Charge Calculation

 Basic Settings .

## G/L account settings

You must change the Manage G/L Account Master Data accounting settings.

For more information, see the setup instruction guide for any of the Transportation Management (TM) scope items under

the best practices for the solution scenario at https://me.sap.com/processnavigator/SolS/EARL_SolS-055

 . Navigate to

## Supply Chain

  Delivery and Transportation

 Freight Settlement (6W4)

.

## Example of Freight Cost Distribution with a Business Use Case

The following graphic contains an example of a freight document with a distribution level of Order/Delivery Item. It's followed by

an explanation.

The above table contains the item hierarchy of a freight order or freight booking. In the document, you have two products. You

packed each product in a separate package with appropriate labels for each package. You placed both packages in the same

container.

This is custom documentation. For more information, please visit SAP Help Portal.

100


1/14/26, 2:42 PM

The above table contains the charges for the freight document. The system bases some charges on the packaging or product. It

also bases other charges on the root or the container, as you can see in the Logistical Reference column. The system distributes

some charges by distribution rule. It distributes other charges directly. You can see this distribution in the following graphic:

The system assigns the costs for packaging and labeling directly. The distribution rule has no influence when the costs are

allocated directly.

## Flexibility in Freight Charge Changes

After you've posted accruals for a freight document, you can do the following changes to the freight costs:

Add or update charge amounts directly in the existing freight documents and also transfer these changes in the freight

costs to Materials Management (MM).

Add an independent freight charge for a freight document and carrier or service provider combination, after you've verified

the existing charges in an invoice. You can subsequently confirm the newly added freight charge for posting accruals.

This is custom documentation. For more information, please visit SAP Help Portal.

101


1/14/26, 2:42 PM

  Note

You can't change or delete an existing charge line with the invoicing status Invoice Verified.

You can't add a dependent charge that refers to an independent charge line which has the invoicing status Invoice

Verified.

For a freight document and carrier or service provider combination where some charges are invoice verified, you have the following

conditions:

Where some charges are invoice verified and other charges are posted, you can't change an invoice verified charge line.

Also, you can't include dependent charges that reference charges that are already invoice verified.

Where some charges are invoice verified and you have a dependent charge that references a charge range, you cannot

include an independent charge in the range of dependent charges.

For freight settlement integration using lean services, the system identifies the change process strategy based on the nature of

change to the charge line.

  Note

The change process strategy for that you've defined in the Customizing activity for Transportation Management under

## Settlement

 Define Settlement Profile  isn't considered for the freight settlements using integration with lean services.

The system uses change management where the previous freight settlement document (FSD) along with the purchase order (PO)

and service entry sheet (SES) is canceled and a new freight settlement document with the updated amount is created and posted.

You can use the background function Creation and Transfer of Freight Settlement Documents (program

/SCMTMS/SFIR_CREATE_BATCH) to create and post freight settlement documents to MM. For more information see, Creation

and Transfer of Freight Settlement Documents using Integration with Lean Services. The freight settlement document contains the

changes from the freight document.

## Changes to Invoice Verified Freight Documents

When there are changes to the charges for the business partners in the freight document which is already invoice verified, then the

system handles the changes in the following ways:

When you add a new charge line, a new FSD and follow-on documents (Purchase Order (PO) and Service Entry Sheet

(SES)) are created only for the new delta charge line without any changes to the existing follow-on documents.

Any change to the already invoiced charge lines isn't allowed.

The following table has some scenarios where there can be changes to Invoice Verified freight documents:

Scenario

## Description

## Agreement Redetermination

Once the invoice is verified for the business partners in the freight

document, you as a shipper along with your carrier notice that

there's a Toll Charge in the route and you decide to include it in the

freight agreement. This additional charge in the freight document is

posted and invoiced in separate follow-on PO and SES documents.

In case there are changes in the already invoiced charge line due to

agreement re-determination, then charge line isn't updated in the

freight document charges.

This is custom documentation. For more information, please visit SAP Help Portal.

102


1/14/26, 2:42 PM

Scenario

## Description

## Change in Logistical Data

There can also be instances where there are changes to the

## Unplanned Charges

logistical data. Example, the weight of the cargo during the planning

to the actual weight can differ due to the packaging activities which

occurs during the warehouse activity. In such cases the information

can be updated later in the process after the charges in the freight

document are already posted. The change in logistical data doesn't

have any impact on the Invoice Verified charge lines.

Unplanned charges are additional services that are provided or

received as part of the execution step.  Example, there could be

additional toll charges since the route used can be tolled roads or

can have fumigation charges incurred during execution. In such

cases the information can be updated later in the process after the

charges in the freight document are already posted or the invoice

verified.

## Changes to Posted Freight Documents

You can modify a charge line which has the invoicing status Posted. For posted charge lines in a freight document if the system has

already created the follow-on documents (like FSD, PO, or SES) the system cancels the existing follow-on documents and creates

new follow-on documents with updated amounts.

When you modify a Posted charge line, the system updates the status of the modified charge line to Ready for Confirmation and

the same is rolled-up to charge item and charge header level. Once you've confirmed freight documents with the status Ready for

Confirmation, the status changes set to Ready for Posting.

The following table shows the scenarios where the invoicing status is set to Ready for Confirmation after the FSD is posted and

the level at which the status change happens:

Charge Level

Scenario

## Impact

## Charge Element

Any manual or automatic change that

Rolled-up to charge item level and then

changes the amount of a charge element

charge header level, based on the following

A new charge line is added under the charge

1. Ready for Confirmation

priority:

item manually or comes in from an

agreement

2. Posting Failed

3. Ready for Posting

Logistical data change resulting in rate

4. Posted

change

5. Invoice Verified

Change in resolution base of a charge line

6. Not Ready for Posting

## Examples

The following examples show various scenarios and the follow-on documents that are created:

  Example

## Change to charge amount in Posted charge line

This is custom documentation. For more information, please visit SAP Help Portal.

103


1/14/26, 2:42 PM

The table shows the setup of the charge lines in a freight order:

Line No.

Charge Type

Rate (in USD)

Final Amount(in

Invoicing Status

Follow-on

Charge Header

BP Charge Item

10

20

Base Freight

200

Loading Charge

20

USD)

220

Posted

Posted

Posted

Posted

## Documents

FSD1, PO1, SES1

FSD1, PO1, SES1

Due to unforeseen circumstances, the loading charge is changed to 25 USD. As part of accrual posting, the system cancels the

FSD1, PO1, SES1 is canceled and creates FSD2, PO2, SES2. Also, for the freight cost allocation posting, the system creates the

reversal freight cost allocation document to reverse the amount 220 USD in the already posted freight cost allocation

document and creates a new freight cost allocation posting document for the updated amount 225USD.

Line No.

Charge Type

Rate (in USD)

Final Amount(in

Invoicing Status

Follow-on

Documents

USD)

225

Ready for

Confirmation

Ready for

Confirmation

Base Freight

200

## Posted

FSD2, PO2, SES2

Loading Charge

25

Ready for

Confirmation

FSD2, PO2, SES2

Charge Header

BP Charge Item

10

20

  Example

Addition of a new charge line to Posted freight documents:

For new charge line additions, the system creates FSD and subsequent follow-on documents only for the delta amount (newly

added amount) in the freight document without canceling the existing postings/ follow-on documents (FSD, PO, and SES). The

system determines if a delta settlement needs to be created based on the nature of the change:

For accrual postings, the system creates new FSD, PO, and SES documents for the newly added (delta) charge in the

freight document without canceling the existing FSD, PO, and SES.

For freight cost allocation postings, the system creates new freight cost allocation document for the newly added (delta)

charge in the freight document. The system doesn't change the already created freight cost allocation document and

also doesn't create any reversal freight cost allocation document.

The table shows the setup of the charge lines in a freight order:

Line No.

Charge Type

Rate (in USD)

Final Amount(in

Invoicing Status

Follow-on

Charge Header

BP Charge Item

10

Base Freight

200

USD)

220

Posted

Posted

Posted

## Documents

FSD1, PO1, SES1

This is custom documentation. For more information, please visit SAP Help Portal.

104


1/14/26, 2:42 PM

Line No.

Charge Type

Rate (in USD)

Final Amount(in

Invoicing Status

Follow-on

USD)

Documents

20

Loading Charge

20

## Posted

FSD1, PO1, SES1

Due to changes in the route, there's Toll Charge incurred and you update it in the freight document. As part of accrual posting,

FSD2, PO2, SES2 is created only for the delta charge Toll Charge without canceling the existing documents.

Line No.

Charge Type

Rate (in USD)

Final Amount(in

Invoicing Status

Follow-on

Charge Header

BP Charge Item

10

20

30

Base Freight

200

Loading Charge

Toll Charges

20

10

USD)

230

## Documents

FSD1, PO1, SES1

FSD1, PO1, SES1

FSD2, PO2, SES2

Ready for

Confirmation

Ready for

Confirmation

Posted

Posted

Ready for

## Confirmation

Also, for the freight cost allocation posting, the system creates a new freight cost allocation posting document for the delta

amount of 10 USD.

## Related Information

Invoicing Status of Freight Documents using Lean Services

## Blocking and Unblocking of Freight Documents

Generally, the freight settlement document (FSD) is created and posted when you confirm and post the freight document. But

there can be scenarios where charges are different for the freight document and the FSD. This difference can be due to

redetermination of a different freight agreement or redetermination of the rates in the same freight agreement during the creation

of FSD. The redetermination of freight agreements or rates can result in charges mismatch between the freight document and the

FSD.

The system can redetermine a freight agreement while FSD creation, if you've selected Copy Fixed Charges and Redetermine

Others as Calculation Option in the Customizing for Transportation Management under  Settlement

 Define Settlement

## Profile

 Settlement Profile Settings .

Whenever the system creates and posts an FSD from a freight document it checks the following:

If there are no charges mismatches during FSD creation, the FSD is created and posted. The invoicing status of the freight

document is set to Posted or Posting Failed based on whether the FSD was posted successfully or not.

When there are mismatched charges between the freight document and FSD during FSD creation, the system checks

whether those mismatched charges can be overruled or not.

## Blocking during Mismatched Charges

This is custom documentation. For more information, please visit SAP Help Portal.

105


1/14/26, 2:42 PM

Charges mismatch can be categorized into two types:

## Mismatches which are acceptable and can be overridden

In this case, you can review the mismatch that occurred in the freight document and FSD charges. If these mismatches are

acceptable, for example if you and your carrier have mutually agreed to a rate change in master data, you can override the

block manually in FSD and continue the accrual process.

Alternately, you can recalculate the charges in the freight document, create the FSD, and continue the accrual process.

## Mismatches which are inconsistent and can't be overridden

In these cases, mismatches occur when master data is deleted, for example charge lines or agreements. When you start the

accrual posting from the freight document, then the system detects these changes and does the following:

Stops the FSD creation.

Sets an invoicing block on the freight document to stop any further settlement process until the freight document

charges are corrected.

The invoicing status of the freight document is set to Posting Failed.

## Examples

## Scenario: No mismatch in charges

If there's no mismatch in charges, then the freight document and the FSD aren't blocked.

Scenario: Mismatch in charges due to definition in agreement (order relevant charges)

The following tables show the setup of a freight order FO1 and the corresponding freight settlement document FSD1:

Freight Order

Charge Type

Rate (in USD)

Final Amount (in USD)

FO1

FB00

100

150

LOAD (Order Relevant)

50

Freight Settlement Document Charge Type

Rate (in USD)

Final Amount (in USD)

FSD1

FB00

100

100

In this case, both the FO1 and FSD1 aren't blocked as the mismatch is only for order relevant charges.

Scenario: Mismatch in charges due to definition in agreement (invoice relevant charges)

The following tables show the setup of a freight order FO1 and the corresponding freight settlement document FSD1:

Freight Order

Charge Type

Rate (in USD)

Final Amount (in USD)

FO1

FB00

100

100

Freight Settlement Document Charge Type

Rate (in USD)

Final Amount (in USD)

FSD1

FB00

100

150

This is custom documentation. For more information, please visit SAP Help Portal.

106


1/14/26, 2:42 PM

Freight Settlement Document Charge Type

Rate (in USD)

Final Amount (in USD)

LOAD (Invoice Relevant)

50

In this case, both the FO1 and FSD1 aren't blocked as the mismatch is only for invoice relevant charges.

## Scenario: Amount Mismatch

The following tables show the setup of a freight order FO1 and the corresponding freight settlement document FSD1:

Freight Order

Charge Type

Rate (in USD)

Final Amount (in USD)

FO1

FB00

LOAD

100

50

150

Freight Settlement Document Charge Type

Rate (in USD)

Final Amount (in USD)

FSD1

FB00

LOAD

120

50

170

In this case, both the freight order and FSD have the status Blocked as there's an amount mismatch. To override, you can:

Manually override the block in FSD and then post to accruals. You can use the Monitor Freight Settlements for Accrual app

to unblock the FSD. For more information, see Monitor Freight Settlements for Accrual.

Recalculate the charges in the freight order which updates the charges in the freight order and removes the invoicing block.

The system then creates and posts the new FSD.

## Scenario: Missing charges due to change in master data

The following tables show the setup of a freight order FO1 and the corresponding freight settlement document FSD1:

Freight Order

Charge Type

Rate (in USD)

Final Amount (in USD)

FO1

FB00

LOAD

100

50

150

Freight Settlement Document Charge Type

Rate (in USD)

Final Amount (in USD)

FSD1

FB00

100

100

In this case, there are changes in the master data and the charges aren't updated in the freight order. To override the block, you've

to recalculate the charges in FO1 which updates the charges in FO1 and the system removes the invoicing block and creates a new

FSD and posts it.

## Scenario: Charges mismatch due to agreement redetermination

The following tables show the setup of a freight order FO1 with the agreement AGR1 and the corresponding freight settlement

document FSD1 with the agreement AGR2.

This is custom documentation. For more information, please visit SAP Help Portal.

107


1/14/26, 2:42 PM

## Freight Order

Charge Type (in charge items

Rate (in USD)

Final Amount (in USD)

FO1

of AGR1)

FB00

LOAD

100

50

150

Freight Settlement Document

Charge Type (in charge items

Rate (in USD)

Final Amount (in USD)

FSD1

of AGR2)

## BASE

DOCUMENTATION

100

50

100

In this case, due to redetermination of a new freight agreement during FSD creation, charges aren't updated in the freight order. To

override the block, you've to recalculate the charges in FO1 which updates charges in FO1 and the system removes the invoicing

block and creates a new FSD and posts it.

  Note

If you've selected Copy Fixed Charges and Redetermine Others as Calculation Option in the Customizing, then for charge

calculation in the follow-on documents, the system picks only that freight agreement and calculation sheet that has been

determined and used for the charge calculation in the freight document, and the freight agreement and calculation sheet is still

valid.

Dispute Case Resolution and Accruals Update in Lean Service
## Procurement

A dispute is resolved when both you and your service provider arrive at a common agreement on the charge or logistics item under

dispute. If there are any disputes or discrepancies due to changes in the planned charges or the addition of unplanned charges, the

system updates the charges for the Freight Order once the dispute is accepted

You use the background function Creation of Freight Settlement Documents to create, change, and post the freight settlement

documents to Materials Management (MM) (see Creation and Transfer of Freight Settlement Documents using Integration with

Lean Services). The freight settlement document contains the changes from the freight order.

## Freight Charge Changes in Freight Settlement Documents

The system uses a simple change management for managing the changed charge information where it cancels the existing freight

settlement document, purchase order, and service entry sheet document and creates a new freight settlement document and

posts it with the changed charges.

For example, you have a freight order with a transportation charge of 500 USD. Your carrier creates a dispute case for the base

freight charge, and you resolve the dispute by accepting the change to the base freight charge from 200 USD to 250 USD .

Before Dispute Resolution

Charge Type (Description)

Amount (in USD)

BASE_CHARGE (Base Freight)

200

HANDLING_CHG (Handling Charge)

300

This is custom documentation. For more information, please visit SAP Help Portal.

108


1/14/26, 2:42 PM

Charge Type (Description)

Amount (in USD)

Total

500

After Dispute Resolution

Charge Type (Description)

Amount (in USD)

BASE_CHARGE (Base Freight)

250

HANDLING_CHG (Handling Charge)

300

Total

550

Once the charges are confirmed after the dispute resolution, the system updates the accruals to MM by canceling the existing FSD

and the related postings and creates a new FSD and posts it.

## Background Function to Publish Freight Settlement Dispute Cases

You can use a background function to publish freight settlement dispute cases in batches in the background. When you run the

background function, you, as a requester of transportation services, confirm the decisions that you make to accept the relevant

dispute cases. The system updates the resolution status of the dispute case to Dispute Resolved. Also the system uses the charge

details from a dispute case that is resolved to update the changed charge information in the freight order. For more information,

see Publication of Freight Settlement Dispute Cases.

## Background Function to Create and Transfer Freight Settlement Documents

You can include, exclude, or include only the freight documents for which all dispute cases are resolved when you create and

transfer freight settlement documents in the background. For more information, see Creation and Transfer of Freight Settlement

Documents using Integration with Lean Services.

More Information

## Subject

## More Information

Structure of an individual dispute case, including working with a

Freight Settlement Dispute Case

dispute case

Necessary Customizing settings required before you can use

Prerequisites for Dispute Management

dispute management

Individual aspects of dispute management

Features of Dispute Management

## Handling Calculated Charges in Lean Services

In charge calculation, the final amount for a freight document is derived from the calculation parameter which is (Rate Amount

* Quantity)/Price Unit. For accrual postings using lean services, the calculation parameters from the charge element are

mapped to the corresponding purchase order (PO) items.

There can be scenarios where after you've calculated the charges for a freight document and the final amount of a charge element

can be different from the calculation parameters. If these calculation parameters are mapped to the PO, then the final amount in

PO is different from the final amount that is calculated in the freight document resulting in inconsistency.

This is custom documentation. For more information, please visit SAP Help Portal.

109


1/14/26, 2:42 PM

The scenarios where there can be inconsistency are:

Charge Calculation Methods

Clipping/Clipping_V2

External calculation methods, such as SMC3

Air freight: standard rating

Air freight: break-weight rating

Multiple calculation rules in rate tables

## Amount based calculation bases, such as GOODS_VALUE

For more information on calculation methods, see Calculation Methods and on calculation rules, see Rate Table and Local Rate

Table.

## Deficit Weight Rate (DWR) Calculation Method

When you use the calculation method DWR for a charge line, an additional charge line for the deficit amount with the same charge

type and same rate amount is created after charge calculation. The deficit weight charge line is a generated charge line which isn't

part of any agreement or is planned between the involved parties. Hence, the deficit weight charge line isn't sent to the PO for

further processing. Rather, the quantities of the deficit weight charge line are merged with the quantity of the parent charge line(s)

and then sent to PO for further processing.

The resolution base of the deficit charge line and the parent charge line can be ROOT or different resolution base, such as

PRODUCT or PACKAGE.

When both the deficit weight charge line and the parent charge line have the resolution base as ROOT, the system adds two charge

lines (deficit weight charge line and parent charge line) with the same charge type and same resolution base. But when the freight

document is posted then only the parent charge line is sent to the PO and the quantity of the deficit weight charge line is merged

with the parent charge line.

When the deficit weight charge line and parent charge line have a resolution base apart from ROOT, the deficit weight charge line

isn't sent to the PO but the quantity of the deficit charge line is merged with the quantity of the parent charge line, and the parent

charge line is sent to PO. The weighted average of the quantity of the deficit weight charge line (with respect to the quantity of each

parent charge line) is calculated and added to the quantity of the corresponding parent charge line. The other parameters like rate

amount, calculation rule, and price unit isn't changed for any of the charge lines.

  Example

The following table shows a freight order, FO1 with two charge lines with the same resolution base as ROOT. One is a parent line

with charge type SD02and the other is deficit weight charge line SD02(DWR). When the freight document is posted, the SD02

(DWR line) isn't sent to PO. The main SD02 line is sent where the quantities are combined (1800 KG + 200 KG = 2000 KG).

## Charge Line

Rate Amount (in EUR)

Quantity (in KG)

Merged Quantity in KG

Amount in EUR (to be

SD02

SD02 (DWR)

25

25

1800

200

  Example

(to be sent to PO)

calculated in the PO

item)

1800+200=2000

2000*25=50000

## Not sent to PO

This is custom documentation. For more information, please visit SAP Help Portal.

110


1/14/26, 2:42 PM

The following table shows a freight order FO2 with three charge lines, two with the same charge types SF02 and the one deficit

weight charge line SF02 (DWR). All three have the same resolution base as PRODUCT.

Charge Line

Rate Amount (in

Quantity (in KG)

Weighted Quantity

Merged Quantity

Amount in EUR (to

EUR)

from DWR (in KG)

(in KG, to be sent

be calculated in

SF02 (Product 10)

2

SF02 (Product 20)

2

SF02 (DWR)

2

Total Amount

30

50

10

to PO)

the PO item)

10 * (30 / (30 +

30 + 3.75 = 33.75

33.75 * 2 = 67.5

50)) = 3.75

10 * (50/ (30 +

50 + 6.25 = 56.25

56.25*2=112.5

50)) = 6.25

Not sent to PO

Not Sent to PO

(67.5+112.5) = 180

Here the weighted average for the deficit weight charge line is derived from the other two charge lines and the total amount is

calculated based on the weighted average.

The weighted average values are added to the quantities of the corresponding parent charge line and that parent charge line is

sent to PO.

Adjusted Charge Type (ADJ)

In freight tendering, you as a shipper can tender a road freight order or ocean freight booking to one or more carriers. Tendering

can be based on freight Request for Quotation (RFQ) ( only for road freight orders) or direct tendering. In some cases there can be

a difference between the amounts calculated by the shipper and proposed by the carrier. In those cases, ADJ charge type is used

as the adjusted amount. The following steps explain the tendering process and the usage of ADJ charge type:

You as a shipper, request for a quotation from the carriers for the transportation services. You can also set a price limit for

the carrier to consider your request.

The carrier responds to your quotation based on the price limits.

You can reject or accept the quotation or have further negotiation with the carrier.

When you accept (award) the quotation from the carrier, the system adjusts the charges in the freight order or freight

booking with the amount based on the response received from the carrier.

Assuming there's already an agreement between you and the carrier, and the amounts are calculated based on that

agreement, the system adjusts the difference in the charges grid in the form of a new charge line with charge type

Adjusted/Quoted Amount (ADJ). ADJ is a delta amount between charges from the shipper and amount the proposed by

the carrier.

Based on the difference in the amount provided by the carrier and the one calculated from the agreement, the amount for

ADJ line can be negative or positive. ADJ charge line is created automatically to handle the adjustment in charges so it

doesn't depict any transportation charges and isn't passed on to PO. Instead, the ADJ charge amount is distributed to the

other charge lines under the same charge item based on weighted average.

  Note

You can't edit the amount of an ADJ charge type manually.

As the ADJ lines aren't part of accruals posting process, its posting status is always blank.

This is custom documentation. For more information, please visit SAP Help Portal.

111


1/14/26, 2:42 PM

Example

  Example

The following example shows the distribution of ADJ charge amount based on weighted average when the adjusted charge

(ADJ) is positive:

The following are the amounts for various charge lines in freight order FO3 calculated from a freight agreement.

## Charge Type

Rate Amount (in USD) Amount (in USD)

FB00

BASE_3PL

Total Amount

200

20

200

570

770

The total amount is 770 USD. There's a carrier who has proposed 1100 USD, and the shipper has agreed to award the carrier. In

this case, the adjusted (ADJ) charge amount is (1100-770) USD = 330 USD, which is automatically calculated by the system.

Now, the charges in FO3 look like :

## Charge Type

Rate Amount (in USD) Amount (in USD)

200

20

FB00

BASE_3PL

ADJ

Total Amount

200

570

330

1100

To fit this adjusted amount (ADJ) charge line), the system calculates the weighted average and then calculates the charges

based on the weighted average and sends to PO as shown in the following table:

## Charge Type

Rate Amount (in USD)

Amount(in USD)

## Weighted

Amount to be sent to

200

20

200

570

FB00

BASE_3PL

Total amount

Average/Adjusted

PO (Amount+Adjusted

## Value

Value) (in USD)

(200 / (200 + 570 ) ) *

285.71

330 = 85.71

(570 / (200 + 570 ) )

814.29

*330 = 244.29

1100

The adjusted charge line (ADJ) isn't sent to the PO, but after the adjusted amount is calculated, the charge lines with charge

type FB00 and BASE_3PL are sent to the PO.

Example

  Example

The following example shows the distribution of ADJ charge amount based on weighted average, when the adjusted charge

(ADJ) amount is negative:

This is custom documentation. For more information, please visit SAP Help Portal.

112


1/14/26, 2:42 PM

The following are the amounts for various charge lines in freight order FO4 calculated from a freight agreement.

## Charge Type

Rate Amount (in USD) Amount (in USD)

FB00

BASE_3PL

Total Amount

450

550

450

550

1000

The total amount is 1000 USD. There's a carrier who has proposed 900 USD, and the shipper has agreed to award the carrier. In

this case, the adjusted (ADJ) charge amount is (900-1000) USD = -100 USD, which is automatically calculated by the system.

Now, the charges in FO4 look like :

## Charge Type

Rate Amount (in USD) Amount (in USD)

450

500

FB00

BASE_3PL

ADJ

Total Amount

450

550

-100

900

To fit this adjusted amount (ADJ) charge line), the system calculates the weighted average and then calculates the charges

based on the weighted average and sends to PO as shown in the following table:

## Charge Type

Rate Amount (in USD)

Amount(in USD)

## Weighted

Amount to be sent to

Average/Adjusted

PO (Amount+Adjusted

## Value

Value) (in USD)

450

550

450

550

FB00

BASE_3PL

## Total amount

(450 / (450 + 550 ) ) *(-

405

100) = -45

(550 / (450 + 550 ) ) *

495

(-100) = -55

900

The adjusted charge line (ADJ) isn't sent to the PO, but after the adjusted amount is calculated, the charge lines with charge

type FB00 and BASE_3PL are sent to the PO.

Related Information

Calculation Methods

Charges Overview

Credit Memos

## Use

You can create a credit memo for the following business reasons:

This is custom documentation. For more information, please visit SAP Help Portal.

113


1/14/26, 2:42 PM

## Damaged goods

## Delays in transports

Service level agreements not met

## Overcharges for transportation service

The type of credit memo you create depends on your role in the transportation process. You can create the following credit memo

types:

A credit memo for a forwarding order to reflect the credit you provide as a logistics service provider (LSP) to your customer.

Here you create a credit memo with reference to a forwarding settlement document. For more information, see Credit

Memos for Forwarding Orders.

A credit memo for a freight order to reflect the credit your carrier provides to you. Here you can create a credit memo with

reference to a freight settlement document. For more information, see Credit Memos for Freight Orders.

You can post a credit memo to financial accounting for further processing. You can create more than one credit memo for a

particular forwarding settlement document or freight settlement document. However, at any given time, there can be only one

credit memo for a particular forwarding settlement document or freight settlement document that hasn't yet been posted

successfully.

  Note

You can't use credit memos for freight settlements using lean-service based integration.

## Prerequisites

In Customizing, you have to set up the process controller for use with settlement documents. For example, if you want to use a

strategy to create or preprocess forwarding settlement documents differently than the standard way, you can define your own

strategy using the process controller and assign it to a specific service. For more information, see Customizing for Transportation

Management under  Settlement

 Configure Process Controller for Settlement

.

Features

## Charges

The system displays the transportation charges that have been invoiced in the Already Invoiced Amount field. The system displays

the difference between the amount that has been invoiced and the amounts credited in all credit memos entered against the

settlement in the Credit Remaining Amount field.

You can enter a credit amount against each of the charge types up to the amount in the Credit Remaining Amount field. The

system controls the credit amount that you can provide because you can't exceed the invoiced amount.

## Related Information

Forwarding Settlement Document

Freight Settlement Document

Credit Memos for Forwarding Orders

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

114


1/14/26, 2:42 PM

You can use a credit memo to give a credit to a customer in a forwarding settlement where you have over-invoiced for

transportation services. You use a forwarding settlement document as a reference when you create a forwarding credit memo.

## Prerequisites

## Types of credit memo and credit memo reason codes

In Customizing, you have defined a credit memo type that the system uses to automatically enter certain settings when you

create a credit memo. You have also defined the reasons for why the credit memo is necessary. For more information, see

Customizing for Transportation Management under  Settlement

 Forwarding Settlement

 Define Credit Memo Reason

Codes and Types for Forwarding SDs .

## Influence invoicing status

You can specify the Influence Invoicing Status setting in the relevant default credit memo type. When you create a credit

memo, either manually or using the background processing function, the credit memo has a role in determining the

invoicing status of the forwarding order.

## Automatically enter credit amount

When you specify that the system automatically enters the credit amount, the system automatically copies the credit

remaining amount to the credit amount in a credit memo. This means that you do not have to manually enter the credit

amount in a credit memo. For more information, see Customizing for Transportation Management under  Forwarding

## Settlement

 Define Credit Memo Reason Codes and Types for Forwarding SDs

 Automatically Propose Credit Amount

.

Integration settings for posting to Sales and Distribution (SD)

You have made the relevant settings in Customizing for Transportation Management under  Settings for Posting

Forwarding Settlements

## Settlement

 Forwarding Settlement

.

The system determines the logical system behind the business system group that you have linked to your sales

organization data for the credit memo. The business system group represents the SAP ERP system from which you

replicate the sales organization in the organization model.

If the logical system is different to the current client logical system, the system uses enterprise services to post the credit

memo to an external SD system. If the logical system is same as the current client logical system, the system posts the

credit memo to an internal SD system.

For integration to SD on an external system (SAP S/4HANA or SAP ERP), you have made the relevant settings in

## Customizing under

Integration with Other SAP Components

 Transportation Management

## Invoice Integration

 Billing  in the external system.

## Forwarding settlement documents

The system contains a forwarding settlement document that is associated with one or more forwarding orders and has the

life cycle status Posted.

## Features

## Credit Memo Preview

You can preview a credit memo as it would appear in Sales and Distribution (SD). The preview contains information from the credit

memo and tax information from SD.

You can use the preview for credit memo documents that are at all life cycle statuses except the following:

## Credit Memo Posting Started

This is custom documentation. For more information, please visit SAP Help Portal.

115


1/14/26, 2:42 PM

Credit Memo Posted

Cancellation Requested

## Canceled

The credit memo must also be consistent. In a preview, the system does not permanently store any data.

## Activities

You can create a credit memo from a forwarding settlement document. You can access the credit memos from the forwarding

settlement documents overview screen. The system creates the credit memo on the basis of the data in the associated forwarding

settlement documents and displays the amount that has already been invoiced.

The forwarding settlement document you reference can be one of the following types:

Individual forwarding settlement document that references just one forwarding order

Collective forwarding settlement document that references more than one forwarding order

Related Information

## Credit Memos

Automatic Change Management Process for Settlements

Credit Memos for Freight Orders

## Use

You can use a credit memo to get a credit from a carrier in a freight settlement process where you have overpaid or over accrued in

financials for a transportation service. You use a freight settlement document as a reference when you create a freight credit

memo.

  Note
For air freight bookings, you use a charge correction advice document (CCAD) to process changes in charges, including issuing

a credit. Alternatively, you could use the credit memo for handling credit from your carrier.

## Prerequisites

## Types of credit memo and credit memo reason codes

In Customizing, you have defined a credit memo type that the system uses to automatically enter certain settings when you

create a credit memo. You have also defined the reasons for why the credit memo is necessary. For more information, see

Customizing for Transportation Management under  Settlement

 Freight Settlement

 Define Credit Memo Reason

Codes and Types for Freight SDs .

## Influence invoicing status

You can specify the Influence Invoicing Status setting in the relevant default credit memo type. When you create a credit

memo, either manually or by using the background processing function, the credit memo has a role in determining the

invoicing status of the freight orders, freight bookings, or service orders. For more information, see Customizing for

This is custom documentation. For more information, please visit SAP Help Portal.

116


1/14/26, 2:42 PM

Transportation Management under  Freight Settlement

 Define Credit Memo Reason Codes and Types for Freight SDs

 Define Credit Memo Types

 Influence Invoicing Status .

## Automatically enter credit amount

When you specify that the system automatically enters the credit amount, the system automatically copies the remaining

credit amount to the credit amount in a credit memo. This means that you do not have to manually enter the credit amount

in a credit memo For more information, see Customizing for Transportation Management under  Freight Settlement

 Define Credit Memo Reason Codes and Types for Freight SDs

 Define Credit Memo Types

 Automatically Propose

Credit Amount

.

  Note

The system includes the invoicing party, carrier, and payee in the credit memo by default. The system does not transfer

business partners other than the invoicing party and the payee to materials management (MM).

## Business document

The system contains one or more freight orders, service orders, or freight bookings.

The system determines the logical system behind the business system group that you have linked to your purchase

organization data for the credit memo. The business system group represents the SAP ERP system from which you

replicate the purchasing organization in the organization model.

If the logical system is different to the current client logical system, the system uses enterprise services to post the credit

memo to an external MM system. If the logical system is same as the current client logical system, the system posts the

credit memo to an internal MM system.

For more information on organizational model see Create and Merge Organizational Hierarchy under  Transportation

Management

## Master Data

 Organizational Management

 Organizational Model

.

## Integration settings for posting freight settlement documents

For integration to an internal MM system, you have configured the following settings in Customizing:

Assign Purchasing Information for Posting

Assign Service Master Record and Account Assignment Category

## Tax determination setting under Tax

Mapping for cost distribution in a shipper scenario when you have enabled cost distribution in the freight settlement

document

For more information, see Customizing for Transportation Management under Settlement > Freight Settlement >

Integration for Settlement Posting.

For integration to MM on an external SAP S/4 HANA or SAP ERP system, you have made the relevant settings in

## Customizing under

Integration with Other SAP Components

 Transportation Management

## Invoice Integration

 Invoicing  in external the SAP S/4 HANA or SAP ERP system.

## Activities

You can create a credit memo from a freight settlement document on the overview screen for the freight settlement documents.

When you create a credit memo from a freight settlement document, the system includes the information from the freight

settlement document in the credit memo. The system takes the amount that is already invoiced from the freight settlement

document.

This is custom documentation. For more information, please visit SAP Help Portal.

117


1/14/26, 2:42 PM

When you use the automatic change process, the system uses the existing freight settlement document to create a credit memo.

This enables the system process a large-scale change to the freight document charges, for example, a change in the agreement or

in the calculation sheet, or the addition or deletion of a charge line. For more information, see Automatic Change Management for

Freight Settlements.

## Example

The following table illustrates how the freight credit memo process works for an ocean freight booking:

Steps in TM

Amount in FSD /

Steps in MM

## Comments

Freight Credit

Memo (USD)

Total freight cost in ocean freight booking

2400

None

## None

Create the freight settlement document

2400

Purchase order (PO) created, for example,

Regular freight

and post it to MM.

PO1 with line 10.

Service entry sheet (SES) created, for

example, SES 1. Linked to PO1/10 with

amount USD 2400.

Update the booking to reflect the

2000

## None

correction, for example, weight correction.

New total freight cost in freight booking.

settlement

document process

and posting of the

FSD

## None

Create the freight credit memo and post it

## Credit of 2400 using

When the credit memo is posted, a

## PO based on returns

to MM to reverse the old FSD amount.

the Credit Memo

purchase order (PO) created, for example,

item created on

Create a new FSD for the updated freight

cost..

FSD for 2000 for

PO2 with line 10.

the new, updated

A service entry sheet (SES) is created, for

posting of the credit

memo.

freight cost

example, SES 2. This is linked to PO1/10

## Regular freight

with the amount of USD 2400. However, in

settlement

this case the PO item and the SES are both

document process

marked as returns items, which reverses

and posting of the

the previous amounts posted by the FSD.

new FSD created for

the revised freight

cost.

When the new FSD is posted, a new

purchase order is created, for example, PO3

with line 10.

A service entry sheet (SES) created, for

example, SES 3. This is linked to PO1/10

with the amount of USD 2000.

Related Information

## Credit Memos

Automatic Change Management for Freight Settlements

Internal Settlement

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

118


1/14/26, 2:42 PM

You can send an internal settlement document from an internal organization in your company to another internal organization to

recover costs incurred in delivering transportation services for a forwarding order (see Internal Settlement Management).

You can also create internal settlement documents to settle the cost of providing internal resources for freight orders (see Internal

Settlement for Resources).

In the standard internal settlement process, the internal settlement is between the purchasing organization of the freight order

and the sales organization of the forwarding order. In the internal settlement process for resources, the settlement is between the

organizations that own the resources that are used to execute the order and the purchasing organization of the freight order.

## Prerequisites

You have specified the purchasing organization of the freight order or freight booking that is executing the stage as a

forwarding house. The forwarding house acts as an organization in the internal agreement. To work with internal

settlements, you must model the purchasing organization as a forwarding house.

You assign a business partner that represents your forwarding house or sales organization to the organization in

organization management. For the internal settlement process, the business partner assigned to the forwarding house or

the sales organization of the forwarding order is treated as a business partner of the purchasing organization. The

purchasing organization is modeled as a forwarding house in the freight order or freight booking for the internal charge

calculation in the forwarding order and internal settlement.

You have specified a forwarding settlement document type for internal settlement documents in Customizing for

Transportation Management under  Settlement

## Forwarding Settlement

 Define Forwarding Settlement Document

Types .

You have specified the general prerequisites for calculating charges. For more information, see Charge Calculation.

You have specified the relevant settlement profiles and calculation profiles. The process for specifying a settlement profile

and a calculation profile for an internal settlement document is similar to the process for specifying a forwarding

settlement profile and a calculation profile for a forwarding settlement document. For more information, see the

prerequisites for settlement profiles and calculation profiles in Forwarding Settlement.

By default, TM creates an intercompany settlement document when the sales organization of the forwarding order and the

purchase organization (which is modeled as a forwarding house in organization management) of the freight order or freight

booking belong to different company codes. These internal settlement documents for intercompany settlement are posted

to SD to create an invoice and for posting to financial accounting.

The system determines the logical system behind the business system group that you have linked to your sales

organization data for the internal settlement document. You model the sales organization as a forwarding house. The

business system group represents the SAP ERP system from which you replicate the sales organization in the organization

model.

If the logical system is different to the current client logical system, the system uses enterprise services to post the

settlement document to an external SD system or to financial accounting in your SAP S/4 HANA or SAP ERP system. If the

logical system is same as the current client logical system, the system posts the settlement document to an internal SD or

financial accounting system.

For more information on the organizational model, see Customizing for Transportation Management under  Master Data

 Organizational Management

## Organizational Mode

 Create and Merge Organizational Hierarchy

.

To integrate to an internal SD system, you have specified the relevant settings in Customizing for Transportation

Management under

## Settlement

## Forwarding Settlement

  Settings for Posting Forwarding Settlements

.

To integrate to an external SD on an external SAP S/4 HANA or SAP ERP system, you have specified the relevant settings in

## Customizing under

Integration with Other SAP Components

 Transportation Management

## Invoice Integration

 Billing  in the external SAP S/4 HANA or SAP ERP system. To post the SD billing document to your internal company as

an incoming vendor invoice in financial accounting, please see the SAP note 2157070

.

This is custom documentation. For more information, please visit SAP Help Portal.

119


1/14/26, 2:42 PM

To use an intracompany settlement when the sales organization of the forwarding order and the purchase organization

(which is modeled as a forwarding house in organization management) of the freight order or freight booking belong to the

same company organization, you have selected the Intracompany Settlement checkbox in the Org. Data tab page of the

company organization. You can access the structure using transaction PPOCE.

These internal settlement documents for intracompany settlement are posted to financial accounting to create the

financial accounting documents.

To integrate to an internal financial accounting module, you have specified the relevant settings in Customizing under

Integration with Other SAP Components

 Transportation Management

## Settlement

## Forwarding Settlement

 Settings for Posting Intracompany Settlements .

To integrate to financial accounting on an external SAP S/4 HANA, you have specified the relevant settings in Customizing

under

Integration with Other SAP Components

 Transportation Management

 Invoice Integration

 Billing

## Settings

for Posting Intracompany Settlements  in the external SAP S/4 HANA.

To integrate to financial accounting on an external SAP ERP, you have specified the relevant settings in Customizing for

Transportation Management under

Invoice Integration

## Billing

 Intracompany Settlement

 in the external SAP ERP.

You have assigned a sales organization unit (cost receiver organization) in Transportation Management (TM) to an internal

order or cost center in Controlling (CO) for cost distribution. The sales organization is the receiver of the cost for an internal

settlement.

You have assigned a purchasing organization unit (cost sender organization) in CO to an internal order or cost center

account for cost distribution. The purchasing organization is the sender of the cost for an internal settlement.

## Features

## Intercompany Settlements

When you post the internal settlement document to Sales and Distribution (SD), the system creates an SD billing document.

## Intracompany Settlements

When you post the internal settlement document, the system reposts the primary costs to an internal order or cost center in

financial accounting to create the financial accounting documents. The TM system performs the following tasks:

Displays the accounting document in the document flow of the internal settlement document

Uses an internal settlement document to move the cost from the purchasing organization of the execution document such

as freight order or freight booking, to the sales organization of the forwarding order that is part of the execution documents.

## Related Information

Integration: Invoice Processing (MM-IV/SD-BIL) with TM

Internal Settlement Management

## Use

You can send an internal settlement document from an internal organization in your company to another internal organization to

recover costs incurred in delivering transportation services for a forwarding order.

This is custom documentation. For more information, please visit SAP Help Portal.

120


1/14/26, 2:42 PM

If the organizations involved belong to the same company code, the settlement is an intracompany settlement. If the organizations

belong to different company codes, the settlement is an intercompany settlement.

## Prerequisites

You have specified an internal settlement rule in Customizing for Transportation Management under  Forwarding Order

## Management

 Define Stage Type Sequence for Movement Types . A stage in a forwarding order must reach the

execution status you specify here before you can create and edit internal settlements.

For internal settlements (both intracompany and intercompany settlements), you must have an internal agreement in place

between the purchasing organization (forwarding house) of the freight order or freight booking that is executing the stage,

and the sales organization in the forwarding order.

You have specified all the relevant internal settlement prerequisites (see Internal Settlement).

You have the option of specifying your own logic to set or unset the Ready for Invoicing checkbox for a header-level internal

charge item, with the BAdI: Readiness for Invoicing of Header-Level Charges.

For example, you can specify that the header-level charges for a purchasing organization in the freight order or freight

booking should be set to Ready for Invoicing only when the stage with the executing organization has a handling execution

status of Loaded.

For more information, see Customizing for Transportation Management under  Business Add-Ins (BAdIs) for

Transportation Management

## Settlement

## Forwarding Settlement

 BadI: Readiness for Invoicing of Header-Level

Charges .

## Activities

## Determining the Appropriate Agreement

You perform planning on a forwarding order to finalize its execution. The forwarding order contains a breakdown of the stages you

require to fulfill the order. Based on this breakdown, the system calculates the charges for the order. When it calculates charges it

determines the appropriate internal agreement to use to perform the calculation.

## Manually Creating an Internal Settlement Document

You can manually create an internal settlement document in the Forwarding Orders for Internal Settlement screen by selecting

the appropriate freight order or freight booking.

The system checks the following information in the forwarding order:

Purchasing organization of the freight order or freight booking executing the stage

## Sales organization of the overall forwarding order

Depending on the internal organizations that are involved, the system creates internal settlements that are either intercompany or

intracompany settlements.

## Creating Multiple Internal Settlement Documents

You can also create multiple internal settlement documents using the Creation of Forwarding Settlement Documents report, and

selecting a category of Internal Settlement Document.

Creating an Internal Settlement Document for Header-Level Charges

This is custom documentation. For more information, please visit SAP Help Portal.

121


1/14/26, 2:42 PM

You can have charges in a forwarding order that apply to an entire transportation, even though you incur the charges during a stage

of the transportation. For example, you can incur a charge for export documentation during the pre-carriage stage of a

transportation. This charge applies to the entire transportation, and you may want to settle this charge separately from the other

pre-carriage charges.

For internal settlements, you can settle header-level charges separately from your stage-level charges. You can also create internal

settlement documents for the header-level charges only.

The internal charges in the forwarding order represent the cost on the sales organization of the forwarding order, from the

purchasing organizations that execute the stages of the forwarding order. You can identify the purchasing organization in the

forwarding order as follows:

1. Choose the Actual Route tab page

2. In the Document column, choose the executing document

3. Under  General Data

## Organizational Data , see the Purchasing Organization

To enable you to create separate internal settlements for header-level charges, you have the following features:

## Ready for Settlement checkbox in the forwarding order

For each header-level internal charge item, the system automatically specifies the Ready for Settlement checkbox when

the forwarding order goes into an execution status of In Execution.

The system only includes a header-level charge item in an internal settlement when the Ready for Settlement checkbox is

selected.

## BAdI: Readiness for Invoicing of Header-Level Charges

You can specify your own logic to set or unset the Ready for Invoicing checkbox for a header-level internal charge item. For

more information, see the prerequisites section.

Creation and Transfer of Forwarding Settlement Documents background processing function (program

/SCMTMS/CFIR_CREATE_BATCH)

You can create internal settlement documents for header-level charges separately from stage-level charges. You can also

create internal settlements only for header-level charges. For more information, see Creation and Transfer of Forwarding

Settlement Documents.

## Working with Forwarding Orders for Internal Settlement

You can display all the forwarding orders, and the freight orders or freight bookings that contain forwarding orders, that must be

settled internally on the Forwarding Orders for Internal Settlement personal object worklist screen.

The individual line items can contain the following information:

Charge item in a forwarding order that covers the stage that the freight order or freight booking executed

Charge item that applies to the entire forwarding order, from the purchasing organization that is linked to the freight order

or freight booking.

The system does not display a link to the execution document for these charge items.

## Specifying a Forwarding House

You must specify the purchasing organization of the freight order or freight booking that is executing the stage as a forwarding

house. The forwarding house acts as the organization in the internal agreement. The business partner of the sales organization in

This is custom documentation. For more information, please visit SAP Help Portal.

122


1/14/26, 2:42 PM

the forwarding order acts as the business partner in the agreement, and is treated as a customer of the forwarding house.

## Example

A sales organization receives a forwarding order from a customer. The sales organization delegates the execution of the main

carriage to an internal organization. This internal execution organization uses an internal settlement document to bill the sales

organization that received the forwarding order, to recover the costs of executing the main carriage.

In Customizing, you have specified an internal settlement rule of In Execution in the Define Stage Type Sequence for Movement

Types Customizing activity. When the execution status of the freight booking that executes the main carriage goes to In Execution,

the main carriage of the forwarding order is ready for internal settlement. You can create the internal settlement document in the

following ways:

## Manually from the Forwarding Orders for Internal Settlement screen

Automatically in the background, using the Creation and Transfer of Forwarding Settlement Document background

processing program

If the internal organization that executed the main carriage belongs to the same company code as the sales organization that

received the forwarding order, the system creates an intracompany settlement. If the organizations belong to different company

codes, the system creates intercompany settlements.

More Information

Subject

## See

Using internal settlement documents to settle the costs of

Internal Settlement for Resources

providing internal resources

Role and structure of an agreement

## Agreement

Using forwarding settlements

## Forwarding Settlement

Using cost distribution for logistics service providers (LSPs)

## Cost Distribution for LSPs

Creating internal settlement documents in the background

Creation and Transfer of Forwarding Settlement Documents

Internal Settlement for Resources

## Use

You can create internal settlement documents to recover costs for the internal resources you use in executing orders, for example,

trailers and trucks.

  Note

The features described in this document are not yet released.

## Prerequisites

You have enabled a freight order type for internal settlements if you use your own resources to execute freight orders. You

have also assigned the internal settlement document type that you use to create internal settlements for your own

This is custom documentation. For more information, please visit SAP Help Portal.

123


1/14/26, 2:42 PM

resources to the relevant freight order type. For more information, see Customizing for Transportation Management under

Freight Order Management

## Freight Order

 Define Freight Order Types .

You have defined a resource in which the organizational unit to which the resource belongs is defined as a sales

organization, sales group, sales office, or a forwarding house. You do this in the /SCMTMS/RES01 – Resource transaction

under  SAP Menu

## Logistics

 Transportation Management

## Master Data

 Resource  or in the Define Resources app.

For freight orders in which you have used your own resources, you must have an internal agreement in place between the

organizational unit assigned to the resource (forwarding house, sales organization, sales group, or sales office) and the

business partner assigned to the purchasing organization or purchasing group of the freight order that is using the

resource.

You have specified Resource in the Resource field on the General Data tab page of the relevant internal agreement.

You have put in place all the relevant prerequisites for managing internal settlement documents (see Internal Settlement

Management).

TM creates an intercompany settlement document when the sales organization of the resource and the purchase

organization of the freight order belong to different company codes. You post these internal settlement documents for

intercompany settlement to Sales and Distribution (SD) to create the invoice and for financial accounting.

TM creates an intracompany settlement when the sales organization of the resource and the purchase organization of the

freight order belong to the same company code. You must select the Intracompany Settlement checkbox on the Org. Data

tab page of the company organization. You can access the structure using transaction PPOCE. You post these internal

settlement documents for intracompany settlement to financial accounting to create the financial accounting documents.

The system determines the logical system behind the business system group that you have linked to your sales

organization data for the internal settlement document. You model the sales organization as a forwarding house. The

business system group represents the SAP ERP system from which you replicate the sales organization in the organization

model.

If the logical system is different to the current client logical system, the system uses enterprise services to post the

settlement document to SD or financial accounting in an external SAP S/4 HANA or SAP ERP system. If the logical system

is same as the current client logical system, the system posts the settlement document to an internal SD of financial

accounting system.

For more information on organizational models, see Customizing for Transportation Management under  Master Data

 Organizational Management

## Organizational Model

 Create and Merge Organizational Hierarchy

.

To integrate to an internal SD module, you have specified the relevant settings in Customizing for Transportation

Management under  Settlement

## Forwarding Settlement

 Settings for Posting Forwarding Settlements .

To integrate to SD on an external SAP S/4 HANA or SAP ERP system, you have specified the relevant settings in

## Customizing under

Integration with Other SAP Components

 Transportation Management

## Invoice Integration

 Billing in the external SAP S/4 HANA or SAP ERP system.

To integrate to an internal financial accounting model, you have made the relevant settings in Customizing for

Transportation Management under  Settlement

 Forwarding Settlement

.

To integrate to financial accounting on an external SAP S/4 HANA system, you have specified the relevant settings in

## Customizing under

Integration with Other SAP Components

 Transportation Management

 Invoice Integration

## Billing

 Settings for Posting Intracompany Settlements

 in the external SAP S/4 HANA system.

To integrate to financial accounting on an external SAP ERP system, you have made the relevant settings in Customizing

under

Integration with Other SAP Components

 Transportation Management

 Invoice Integration

## Billing

 Intracompany Settlement

 in the external SAP ERP system.

You have assigned a sales organization unit (cost sender organization) in TM to an internal order or cost center in

Controlling (CO) for cost distribution. The sales organization of the resource is the sender of the cost for an internal

settlement.

This is custom documentation. For more information, please visit SAP Help Portal.

124


1/14/26, 2:42 PM

You have assigned a purchasing organization unit (cost receiver organization) in CO to an internal order or cost center

account for cost distribution. The purchasing organization is the receiver of the cost for an internal settlement.

## Features

You can use an internal settlement for a resource when you are a logistics service provider and you do not subcontract the

movement of goods to a carrier. Instead, you move the goods using your own resources, such as trucks and trailers.

Different organizations in your company can provide the resources. The organizations that provide the resources need to get paid.

You can use the internal settlement for resources feature to enable this payment.

For example, you have a trailer that organization 1 provides, and a truck and driver that organization 2 provides. Organization 3 is

the purchasing organization that manages the freight order. Organizations 1 and 2 create internal settlements on organization 3 to

recover the cost of providing their resources. Usually, you base an internal settlement document on a forwarding order. However,

for the freight orders that you execute using your own resources, you base the internal settlement on a freight order.

## Activities

You perform planning on a forwarding order to finalize its execution. You create freight orders to execute the forwarding orders

using your own resources, such as trailers or trucks. You create internal settlement documents to settle the costs of using your

own resources.

You can manually create an internal settlement document for a resource in a freight order by choosing  Follow Up

## Create

## Internal Settlement Document

. You can also create multiple internal settlement documents using the Mass Creation of Freight

Settlement Documents report, and selecting a create option of Internal Settlement Document.

The system checks the following information in the freight order:

Organizational unit that is assigned to the resource

## Purchasing organization of the overall freight order

Depending on the internal organizations that are involved, the system creates an internal settlement that is either an intercompany

settlement or an intracompany settlement. If the organizational unit of the resource and the purchase organization of the freight

order belong to the same company code, the system creates an intracompany settlement. If the organizations belong to different

company codes, the system creates an intercompany settlement.

The system displays a list of the resources that you include in the particular internal settlement document.

  Example

A sales organization receives a forwarding order from a customer. The sales organization delegates the execution of the main

carriage to an internal purchasing organization. The purchasing organization uses internal resources, such as trailers and

trucks, that are assigned to other internal organizations to plan and execute the order. The forwarding order is executed using

the internal resources. The organizations that own the trucks and trailers bill the purchasing organization of the freight order to

recover the costs of providing the trucks and trailers.

More Information

Topic

## Link

Overview of internal settlement document management

## Internal Settlement Management

This is custom documentation. For more information, please visit SAP Help Portal.

125


1/14/26, 2:42 PM

## Topic

Role and structure of agreements

Role and structure of trailer units

## Link

Agreement

## Trailer Unit

Creating, editing, and displaying trailer units

Creation and Editing of Transportation Units

Cost Distribution Management

## Use

Freight costs are an important part of financial reporting in your businesses. You need the ability to allocate freight costs at charge

element level across a number of charge sources to manage the following business processes:

Freight costs

## Material valuations

Profitability of customers, products, and lines of business

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

This is custom documentation. For more information, please visit SAP Help Portal.

126


1/14/26, 2:42 PM

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

This is custom documentation. For more information, please visit SAP Help Portal.

127


1/14/26, 2:42 PM

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

Use cost distribution for shippers, including individual prerequisites Cost Distribution for Shippers

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

This is custom documentation. For more information, please visit SAP Help Portal.

128


1/14/26, 2:42 PM

Cost Distribution for Shippers

## Use

As a shipper, you create documents such as purchase orders, sales orders, and deliveries. Transportation Management (TM)

creates a freight unit (see Integration of Orders and Deliveries in Transportation Planning). You use these freight units to plan the

execution by freight orders or freight bookings. You create a freight settlement document for the freight order to post the

transportation costs to Materials Management (MM). This enables you to post accruals and to match invoices from the

transportation service provider.

You must perform cost distribution at the level of order/delivery item in the freight settlement document.

For example, you have a net amount in document currency of USD 1000 for a freight order consisting of two deliveries, with a cost

distribution of USD 700 for product 1 for delivery 1, and USD 300 for product 2 for delivery 2. When you post the settlement

document, the system takes the following steps:

Creates a purchase order for USD 1000 and creates a service entry sheet for USD 1000

Creates a settlement management document with each product as an item. Each item has the amount of the distributed

cost, USD 700 for product 1 and USD 300 for product 2.

You specify the type of posting that you want to do with the distributed cost. For example, you can post the distributed cost to

material valuation or general ledger. Depending on the settings you've specified, the settlement management document posts to

these or other cost objects. Settlement management uses the underlying sales order and delivery information from the freight

settlement document cost distribution information to determine from the source order or delivery document the particular cost

object against which it posts the distributed costs.

For example, you have a freight order with cargo items that are linked to the deliveries in a sales order. You specify that you want to

post the freight cost to the general ledger if the underlying freight cost distribution item has a reference to a delivery item. When

you post the freight settlement document with cost distribution for this freight order, the distributed cost is passed on to

settlement management. Settlement management takes the following steps:

Creates a settlement management document with a type of Settlement Process and a document category of Settlement

Copies the references from the freight settlement document cost distribution information and gets the linked underlying

delivery items

Copies the product and quantities in the delivery item to the settlement process document item (product 1 and product 2)

Copies the account assignments for the respective settlement process document item from the underlying sales order

item to which the delivery item is linked

Copies the freight cost distribution amounts for the settlement process document item (USD 700 for product 1 and USD

300 for product 2)

Examples of account assignments can be cost objects including a cost center, profit center, CO-PA segment, or an internal order.

## Integration

The system uses the freight settlement document to enable you to integrate the freight cost back to the underlying order/delivery

items.

## Prerequisites

This is custom documentation. For more information, please visit SAP Help Portal.

129


1/14/26, 2:42 PM

To integrate to an internal settlement management system to post the freight cost distribution, you've configured the settings in

the following Customizing activities:

Enable cost distribution for the freight settlement document type in Customizing for Transportation Management under

## Settlement

## Freight Settlement

  Define Freight Settlement Document Types  and Define Credit Memo Reason Codes

and Types for Freight SDs

For freight settlement integration using Materials Management (MM) External Services Management, you've specified the settings

in the following Customizing activities under  Transportation Management

## Settlement

 Freight Settlement

  Integration for

## Settlement Posting

  External Services Management

:

Assign Purchasing Information for Posting

Assign Service Master Record and Account Assignment Category

Tax determination settings under Tax

## Mapping for Cost Distribution

For freight settlement integration using Lean Services, you've specified the settings in the following Customizing activities under

Transportation Management

## Settlement

## Freight Settlement

  Integration for Settlement Posting

  Service Procurement -

Lean Services :

Assign Purchasing Information for Posting Lean service Integration

Assign Val. Class, Acc. Assignment Category, and Conditions to Charge Types

Mapping for Cost Distribution when you've enabled cost distribution in the freight settlement document

To integrate to settlement management on an external SAP S/4HANA or SAP ERP system, you've specified the relevant settings in

the Customizing activities under

 Integration with Other SAP Components

 Transportation Management

## Invoice

## Integration

 Mapping for Cost Distribution .

## Example

The following figure illustrates the process in which deliveries of two sales orders are planned in the freight order in Transportation

Management. The freight costs are then posted for freight orders with freight cost distribution.

This is custom documentation. For more information, please visit SAP Help Portal.

130


1/14/26, 2:42 PM

## Processing Distributed Costs

You include two freight units for outbound deliveries in a freight order. The total amount in document currency of the freight order

is USD 1000. In the associated freight settlement document, the system distributes the freight cost to the underlying delivery

items by gross weight.

When you post the freight settlement document, the system takes the following steps:

1. Creates a service purchase order and includes the items that correspond to the total amount in document currency for the

freight settlement document.

2. Posts a service entry sheet (SES) to confirm the services in the service purchase order

3. Creates a settlement management document with two line items. Each line item corresponds to the individual line items in

the freight order.

The system copies the account assignment details from the relevant sales order line item into the settlement management

document. In this example, the system copies the account assignments from item 10 of sales order 1 to item 10 of the

settlement management document and item 10 of sales order 2 to the item 20 of the settlement management document.

## More Information

This is custom documentation. For more information, please visit SAP Help Portal.

131


1/14/26, 2:42 PM

## Subject

## More Information

Work with invoices for transportation management

## SAP S/4HANA

 Enterprise Business Applications

 Supply

## Chain

 Logistics - General (LO)

 Integration with SAP

Transportation Management

 Integration: Invoice Processing

(MM-IV/SD-BIL) with TM

Work with freight cost allocation documents

## Freight Cost Allocation

Use SAP best practices for Transportation Management in SAP

SAP Note 2535942

S/4HANA 1709 on premise, to configure settlement management

documents

## Billing the Freight Cost in TM to a Customer in SD

When you sell your products to a customer you may also take the responsibility of delivering these products to that customer. For

this you incur costs for transportation, for example, through a carrier. You can pass on these costs to your customer.

You use integration of sales orders and deliveries to facilitate transportation planning and execution in Transportation

Management (TM). The TM component creates or updates freight units directly for sales orders or deliveries. You plan

transportation for these freight units by creating freight orders that you then subcontract to the carrier. The freight order

determines the freight costs to be paid to the carrier. You configure TM to distribute the freight costs in the freight order according

to delivery items. You can then add the distributed costs for each delivery item to the final amount in the billing document that you

send to your customer.

This involves integration of the following processes:

Freight orders in TM

Pricing in SD

Billing in SD

## Example

As the seller of a product, you have a freight order that combines two deliveries for your customer. The freight order contains the

following information:

Item Hierarchy

## Item

Gross Weight (KG)

Tare Weight (KG)

Delivery Reference

Product 1

Product 2

20

50

2,250

2,750

0

0

Outbound delivery

81000100/10

Outbound delivery

81000900/10

You have the following charges in your freight order:

## Charge

Resolution Base

Amount (USD)

Base freight

Fuel surcharge

Root

Root

1,000

250

This is custom documentation. For more information, please visit SAP Help Portal.

132


1/14/26, 2:42 PM

## Charge

Resolution Base

Amount (USD)

## Packaging

Product (for product 1)

50

## Packaging

Product (for product 2)

100

Total Charges

1,400

You can distribute costs in the freight order to the level of each delivery item, based on the gross weight of each delivery item, as

follows:

Distribution Item/Charge Type

Amount (USD)

## Details

Outbound delivery 81000100/10 (2,250

612.50

KG)

Base freight

Fuel surcharge

Packaging

450

112.50

50

Outbound Delivery 81000900/10 (2,750

787.50

KG)

Base freight

Fuel surcharge

Packaging

550

137.50

100

1000*2,250/(2,250+2750)

250*2,250/(2,250+2750)

Assigned directly for product 1

1000*2,750/(2,250+2750)

250*2,750/(2,250+2750)

Assigned directly for product 2

If you enable the SD billing process for your delivery items, the system takes the distributed cost from TM into account when it

creates the billing document for the delivery items in SD. You create a billing document for the outbound deliveries 81000100/10

and 81000900/10 in SD. The system uses the freight cost of 612.50 USD and 787.50 USD for each of the delivery items

respectively in the SD billing document.

  Note

You must integrate SD with an internal TM component to be able to include the freight cost in the billing document for

all deliveries of products.

You can only include the freight cost in a billing document when you have one freight order document for the delivery

and the freight order has only one currency in which you calculate the cost.

## Related Information

Billing of Freight Costs - Integration with Transportation Management

Cost Distribution for Shippers

Cost Distribution for LSPs

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

133


1/14/26, 2:42 PM

As a logistics service provider (LSP), the customer contacts you for a transportation and you create a forwarding order in

Transportation Management (TM). An organization in your company works with customers to handle order placement and a

different organization works with carriers to handle order execution. You use a freight order to execute the transportation service.

You use the standard charge calculation and freight settlement processes to settle costs.

You can use cost distribution for external or internal costs in the following settlements:

Forwarding settlements to settle with your external customers

## Internal settlements to settle with your internal organizations

When the system calculates internal and external charges in a forwarding order, and the internal and external charge calculation is

based on cost pull, it automatically pulls the distributed costs from the associated freight documents, such as freight orders,

freight bookings, or service orders. It also uses the distributed cost to calculate the planned revenue in a profitability analysis.

## Integration

## Financial Accounting

The system uses the internal agreement and internal settlement document to integrate with financial accounting. For more

information, see Internal Settlement.

## Analysis of Profitability in Forwarding Order

You can use cost distribution as a prerequisite for analyzing profitability in a forwarding order. For more information, see

Profitability Analysis.

## Charge Management

You can use the distributed freight cost to settle with your external customers and to settle with your internal organizations. To

enable the system to use the distributed freight cost in a freight order or freight booking, you must select a calculation method

type of Internal Charge Calculation and the appropriate cost pull strategy in the relevant calculation sheet. You use the calculation

sheet in the agreement between your sales organization and your customer for a forwarding settlement, or between your sales

organization and purchase organization for an internal settlement.

When you calculate charges in the relevant forwarding order, the system checks the freight order that executed the forwarding

order. It uses the result of the cost distribution you performed on the forwarding order that was executed in the freight order as a

basis for the forwarding settlement document or internal settlement document. For more information, see Cost Pull.

## Prerequisites

You have performed the following tasks:

Enabled the freight order or freight booking for cost distribution in Customizing for Transportation Management under

Freight Order Management

## Freight Order

 Define Freight Order Types and Freight Order Management

 Freight

## Booking

 Define Freight Booking Types .

This enables you to use the cost distribution information with a cost-pull strategy when you calculate charges.

## Calculated charges in the freight document

Specified an internal agreement between the purchase organization of the freight document and the business partner of

the sales organizations in the forwarding orders. For more information, see Internal Settlement Management.

Specified a forwarding agreement between the sales organization in a forwarding order and the agreement party in the

same forwarding order. For more information, see Forwarding Settlement.

This is custom documentation. For more information, please visit SAP Help Portal.

134


1/14/26, 2:42 PM

Created a forwarding agreement or an internal agreement that contains a calculation sheet in which you have assigned a

calculation method type of Internal Charge Calculation to a charge type.

This enables you use cost distribution information when you calculate charges.

The system uses the cost distribution for external and internal costs as a basis for the calculation. For example, you can use this

calculation method to calculate the following costs and settlements:

Between the purchase organization in the freight document and the sales organization in the forwarding order

## Between the sales organization and the agreement party in the forwarding order

Alternatively, you can use calculation sheets with charge types that are linked to rate tables. You can use the rate tables as the

basis for creating settlements. In this case, you do not need cost distribution in the freight order, freight booking, or service order

to calculate internal settlements.

  Note

When you use a calculation sheet in which you have assigned a calculation method type of Internal Charge Calculation to a

charge type, the system uses the cost distribution amounts from both your external costs and internal costs. For more

information on the internal charge calculation methods see Cost Pull.

You have specified all the prerequisites for internal settlement (see Internal Settlement Management).

You have specified all the prerequisites for forwarding settlement (see Forwarding Settlement).

## Example

You are an LSP and you have 2 customers who need to transport cargo.

## Organizations

The following table explains the role of the relevant organizations in your company:

Organization

SalesOrg_1

## Role

Sells services to the customer and the customer places forwarding

orders with this organization

PurchaseOrg_1

Buys transportation services from carriers to execute freight

orders

## Agreements

The following tables give you an explanation of the external and internal agreements that you create to transport the cargo:

External agreements

## Agreement

Agreement Type

Organization

Business Partner

## Reason

Cust_Agmt_1

Forwarding agreement

SalesOrg_1

Customer_1

Pay for transportation

services in FWO_1

Cust_Agmt_2

Forwarding agreement

SalesOrg_1

Customer_2

Pay for transportation

services in FWO_2

This is custom documentation. For more information, please visit SAP Help Portal.

135


1/14/26, 2:42 PM

## Agreement

Agreement Type

Organization

Business Partner

## Reason

Int_Agmt_1

Internal agreement

PurchaseOrg_1

BP_of_SalesOrg_1

Pay haulage cost

(carrier)

Internal agreement

## Agreement

Agreement Type

Organization

Business Partner

## Reason

Int_Agmt_2

Internal agreement

PurchaseOrg_1

SalesOrg_1

Pay haulage cost

Int_Agmt_Res_3

Internal agreement for

ResOrg_1 (forwarding

BP_of_PurchaseOrg_1

Pay for usage of the

resource

house)

trailer resource

## Orders

You create two forwarding orders in TM, with one forwarding order for each customer. The carrier transports the cargo (the carrier

is the business partner of SalesOrg_1). In the freight order you have external costs from the carrier.

## Cost Distribution

You distribute costs by gross weight. You perform cost distribution at the level of Forwarding Order in the freight order. You also

have internal costs against the purchase organization of the freight order for using a trailer resource from another internal

organization. The following tables describe how the system distributes costs in the freight order or freight booking:

External cost for the carrier, viewed as a distributed cost for the two forwarding orders that are part of the freight order.

Base Freight (USD)

Haulage (USD)

Total (USD)

Net amount in document

700

currency for the freight order

Distributed cost for forwarding

500

order FWO_1

Distributed cost for forwarding

200

order FWO_2

Internal cost for the trailer

300

200

100

1000

700

300

Cost of Trailer (USD)

Use of Trailer over Distance

Total (USD)

Internal cost for provision of

200

## Trailer

Distributed cost for forwarding

140

order FWO_1

Distributed cost for forwarding

60

order FWO_2

(USD)

100

70

30

300

210

90

## Internal Settlement with Distributed Costs

FWO_1 and FWO_2 belong to SalesOrg_1. PurchaseOrg_1 performs the following tasks:

This is custom documentation. For more information, please visit SAP Help Portal.

136


1/14/26, 2:42 PM

Executes the freight order

## Pays the execution costs

Incurs the cost of using the trailer from the internal organization to which the trailer belongs

PurchaseOrg_1 uses the external costs it incurred for both forwarding orders to settle internally with SalesOrg_1. The following

table describes how PurchaseOrg_1 settles with SalesOrg_1:

External Cost (USD)

Internal Cost (USD)

Markup Charge (USD)

Total (USD)

FWO_1

FWO_2

700

300

210

90

100

50

1010

440

More Information

## Subject

Create and change agreements

## See

## Agreement

## Create and change calculation sheets

Calculation Sheet and Local Calculation Sheet Maintenance

Calculate transportation charges according to a specific logic

Calculation Methods

Manage internal settlements

Internal Settlement Management

Manage cost distribution

Cost Distribution Management

## Analyze profit

## Profitability Analysis

Transfer distributed costs from the freight side to the forwarding

## Cost Pull

side, and use the costs as a basis for settling with a customer or an

internal organization

## Create an invoice for TM

Integration: Invoice Processing (MM-IV/SD-BIL) with TM

Cost Distribution in Service Orders for Shippers and LSPs

## Use

A service order is linked to a freight document or a freight document item. The system distributes the service order cost to the

eventual consumer of the service. The system uses the underlying freight document or freight document item to establish the

consumer of the service. This can be a forwarding order or a delivery or a delivery item that is contained in the freight document.

The system uses the distribution level and the distribution rule that you specify to determine the distribution items.

## Prerequisites

You have specified the following settings in Customizing for Transportation Management:

1. Distribution item and distribution rule in the relevant distribution profile under  SAP Menu

 Basic Functions

## Cost

## Distribution

 Define Cost Distribution Profiles

2. Distribution profile under  Basic Functions

 Charge Calculation

## Basic Settings

## Define Charges Profile

This is custom documentation. For more information, please visit SAP Help Portal.

137


1/14/26, 2:42 PM

3. Charges profile in the relevant purchasing organization under  Master Data

 Organizational Management

 Organizational Model

 Change Organizational Model

 (transaction PPOME)

You include the purchasing organization in a freight document. You link a service order to the freight document.

You have enabled the relevant service order type for cost distribution in Customizing for Transportation Management under

Freight Order Management

## Service Order

 Define Service Order Types . For more information, see Creation and Editing of

Service Orders.

## Features

## Changing a Logistics Item

If you make a change to a logistics item in a freight document or freight document line item, and you have linked a service order or

service order item to the logistics item, the system automatically triggers cost distribution in the linked service order.

You can change a logistics item as follows:

Change the quantity of a logistics item where the logistics item is specified in the distribution rule

For example, you as an LSP create a service order for an item in a freight document so that a third party can deliver a

service. You specify a distribution rule of Gross Weight for the cost distribution.

You then change the gross weight of the item in the freight document. When you save the change, the system automatically

distributes the costs again in the service order.

## Add, delete, or reposition a logistics item

For example, you as an LSP remove a product from a package in a freight document. You have created a service order for

the freight document. When you save the change to the freight document, the system automatically adjusts the cost

distribution in the service order.

## Changing a Freight Document

You have a freight document with an associated service order. You change the freight document, but the change does not directly

impact the associated service order. However, because of the change, the system distributes the costs again in the freight

document. In this case, the system also automatically distributes costs again in the service order.

More Information

Topic

## Link

## Example 1 for a shipper

Shipper Example: One Service Order for an Entire Freight Booking

## Example 2 for a shipper

Shipper Example: One SO for a Service Item in a Freight Booking

Example 1 for an LSP

## Example 2 for an LSP

LSP Example: One Service Order for an Entire Freight Booking

LSP Example: One SO for a Service Item in a Freight Booking

Shipper Example: One Service Order for an Entire Freight
## Booking

The following table gives an example of a freight booking:

This is custom documentation. For more information, please visit SAP Help Portal.

138


1/14/26, 2:42 PM

Item Hierarchy

Sub-Level 2

Sub-Level 3

Item Type

Original

Quantity

Gross Weight

Level 1

Ocean freight

booking

FB71000

20 ft dry cont.

20x8

Description

Order/Delivery

Reference

## Container

Freight Unit 70

Freight Unit 71

Product 10

Product

## Delivery

950250/item 10

Product 20

Product

## Delivery

950250/item 20

Product 30

Product

## Delivery

950290/item 10

Product 40

Product

## Delivery

950290/item 20

1

1

1

(KG)

7000

7000

3000

800

2200

4000

2400

1600

You create one service order to cover the provision of a service for the entire booking (for example, the provision of fumigation and

cleaning).

The following table gives an example of the information on the Service Orders tab page of your freight booking:

Service Provider

## Service Order

SERVICE_PROVIDER_1 SO71000

The following table gives an example of the information on the  General Data

 Services  screen of the service order SO71000:

Item Hierarchy

Sub-Level 2

Original

## Item

Item Type

Service Type

Service Type

Document

71000

(Description)

Service

Service

9090

9091

Service

Service

FUM

CLN

Fumigation

Cleaning

Level 1

Booking

  Note

The system does not display any other information about the ocean freight booking on the service order screens.

The following table gives the freight cost in service order SO71000:

Freight Cost in Service Order SO71000 Charge Type

Amount (USD)

Fumigation charge

SRV_FUM

200

This is custom documentation. For more information, please visit SAP Help Portal.

139


1/14/26, 2:42 PM

Freight Cost in Service Order SO71000 Charge Type

Amount (USD)

Cleaning charge

SRV_CLN

Total

50

250

When the system distributes costs, it applies the service order costs to the order/delivery items in the ocean freight booking that

used the service. In this example, it applies the service order costs to delivery 950250, items 10 and 20, and delivery 950290, items

10 and 20.

The following table gives an example of the cost distribution information for the service order SO71000, where the distribution rule

is Gross Weight:

Distribution

Sub-Level 2

Charge Type

Distribution

Distribution

Quantity (KG)

Logistical

Percentage

Amount (USD)

Reference

11.0

28.57

## Delivery

950250/item 10

Fumigation

SRV_FUM

11.0

22.86

3000

charge

Cleaning charge

SRV_CLN

11.0

31.0

5.71

78.57

3000

## Delivery

950250/item 20

Fumigation

SRV_FUM

31.0

62.86

3000

charge

Cleaning charge

SRV_CLN

31.0

34.0

15.71

85.71

3000

## Delivery

950290/item 10

Fumigation

charge

SRV_FUM

34.0

68.57

4000

Cleaning charge

SRV_CLN

34.0

23.0

17.14

57.14

4000

## Delivery

950290/item 20

Hierarchy Level

1

Freight

document

SO71000 –

delivery

950250/item 10

Freight

document

SO71000 –

delivery

950250/item 20

Freight

document

SO71000 –

delivery

950290/item 10

Freight

document

SO71000 –

delivery

950290/item 20

Fumigation

SRV_FUM

23.0

45.71

3000

charge

This is custom documentation. For more information, please visit SAP Help Portal.

140


1/14/26, 2:42 PM

Distribution

Sub-Level 2

Charge Type

Distribution

Distribution

Quantity (KG)

Logistical

Hierarchy Level

1

Percentage

Amount (USD)

## Reference

Cleaning charge

SRV_CLN

23.0

11.43

3000

Shipper Example: One SO for a Service Item in a Freight Booking

The following table gives an example of a freight booking:

Item Hierarchy

Sub-Level 2

Sub-Level 3

Item Type

Original

Quantity

Gross Weight

Level 1

Ocean freight

booking

FB77000

20 ft dry cont.

20x8

Description

Order/Delivery

Reference

## Container

Freight unit 70

Freight unit 71

Product 10

Product

## Delivery

950250/item 10

Product 20

Product

## Delivery

950250/item 20

Product 30

Product

## Delivery

950290/item 10

Product 40

Product

## Delivery

950290/item 20

1

1

1

(KG)

7000

7000

3000

800

2200

4000

2400

1600

You purchase a packaging and labeling service for delivery 950250, item 10. You create a service order for delivery 950250 item 10.

Delivery 950250 item 10 is in the container.

You can review the service order information on the Items tab page of the ocean freight booking FB77000. You select the relevant

item and choose the Service Orders tab page.

The following table gives an example of the information on the Service Orders tab page of your freight booking:

Service Provider

Service Type

## Service Order

SERVICE_PROVIDER_1 Packaging and labeling

SO77000

The following table gives an example of the freight cost in service order SO77000:

Freight Cost in Service Order SO77000 Charge Type

Amount (USD)

Packaging and labeling charges

SRV_PAKLBL

70

This is custom documentation. For more information, please visit SAP Help Portal.

141


1/14/26, 2:42 PM

Freight Cost in Service Order SO77000 Charge Type

Amount (USD)

Total

70

The following table gives an example of the information on the  General Data

 Services  screen of the service order SO77000:

Item Hierarchy

Sub-Level 2

Original

## Item

Item Type

Service Type

Service Type

Level 1

Booking

Document

77000

90010

Service

9090

Service

PKL

(Description)

Packaging and

labeling

When the system distributes costs, it applies the service order costs to delivery 950250 item 10, as this is the only delivery item

that is associated with the service order.

The following table gives an example of the cost distribution information for service order SO77000, where the distribution rule is

Gross Weight:

Distribution

Sub-Level 2

Charge Type

Distribution

Distribution

Quantity (KG)

Logistical

Hierarchy Level

1

Freight

document

FB77000 -

delivery

950250/item 10

Percentage

Amount (USD)

Reference

100

900

## Delivery

950250/item 10

Packaging and

PACK

100

70

800

labeling

LSP Example: One Service Order for an Entire Freight Booking

The following table gives an example of a freight booking:

## Item

Hierarchy

Level 1

Ocean freight

booking

FB71000

20 ft dry cont.

20x8

Sub-Level 2

Sub-Level 3

## Item Type

Original Order

Quantity

Gross Weight

Description

Reference

## Container

Freight unit 70

Product 10

Product

Forwarding

order 250

1

1

1

(KG)

7000

7000

3000

3000

800

This is custom documentation. For more information, please visit SAP Help Portal.

142


1/14/26, 2:42 PM

## Item

Hierarchy

Level 1

Sub-Level 2

Sub-Level 3

## Item Type

Original Order

Quantity

Gross Weight

Description

Reference

Product 20

Product

Forwarding

order 350

1

1

Freight unit 71

Product 30

Product

Product 40

Product

(KG)

2200

4000

4000

2400

1600

You create one service order to cover the provision of a service for the entire booking (for example, the provision of fumigation and

cleaning).

The following table gives an example of the information on the Service Orders tab page of your freight booking:

Service Provider

## Service Order

SERVICE_PROVIDER_1 SO71000

The following table gives an example of the information on the  General Data

 Services  screen of the service order SO71000:

Item Hierarchy

Sub-Level 2

Original

## Item

Item Type

Service Type

Service Type

Document

71000

(Description)

Service

Service

9090

9091

Service

Service

FUM

CLN

Fumigation

Cleaning

Level 1

Booking

  Note

The system does not display any other information about the ocean freight booking on the service order screens.

The following table gives the freight cost in service order SO71000:

Freight Cost in Service Order SO71000 Charge Type

Amount (USD)

Fumigation charge

Cleaning charge

Total

SRV_FUM

SRV_CLN

200

50

250

When the system distributes costs, it applies the service order costs to the forwarding orders in the ocean freight booking that

used the service. In this example, it applies the service order costs to forwarding orders 250 and 350.

The following table gives an example of the cost distribution information for the service order SO71000, where the distribution rule

is Gross Weight:

This is custom documentation. For more information, please visit SAP Help Portal.

143


1/14/26, 2:42 PM

Distribution

Sub-Level 2

Charge Type

Distribution

Distribution

Quantity (KG)

Logistical

Percentage

Amount (USD)

Reference

43.0

107.14

250

Fumigation

SRV_FUM

43.0

85.71

3000

charge

Cleaning charge

SRV_CLN

43.0

57.0

21.43

142.86

3000

4000

350

Hierarchy Level

1

Freight

document

## SO71000 –

forwarding order

250

Freight

document

## SO71000 –

forwarding order

350

Fumigation

SRV_FUM

57.0

114.29

4000

charge

Cleaning charge

SRV_CLN

57.0

28.57

4000

LSP Example: One SO for a Service Item in a Freight Booking

The following table gives an example of a freight booking:

Item Hierarchy

Sub-Level 2

Sub-Level 3

Item Type

Description

Original Order

Reference

Quantity

Gross Weight

(KG)

7000

Level 1

Ocean freight

booking

FB77000

20 ft dry cont.

20x8

Container

1

7000

Forwarding order

1

3000

750

Freight unit 90

1

Product 10

Product

Product 20

## Product

Forwarding order

1

850

1

Freight unit 91

Product 30

Product

Product 40

Product

3000

800

2200

4000

4000

2400

1600

This is custom documentation. For more information, please visit SAP Help Portal.

144


1/14/26, 2:42 PM

You purchase a packaging and labeling service for product 10. Product 10 belongs to forwarding order 750. You create a service

order for product 10.

You can review the service order information on the Items tab page of the ocean freight booking FB77000. You select the relevant

item and choose the Service Orders tab page.

The following table gives an example of the information on the Service Orders tab page:

Service Provider

Service Type

## Service Order

SERVICE_PROVIDER_1 Packaging and labeling

SO77000

The following table gives an example of the freight cost in service order SO77000:

Freight Cost in Service Order SO77000 Charge Type

Amount (USD)

Packaging and labeling charges

SRV_PAKLBL

Total

70

70

The following table gives an example of the information on the  General Data

 Services  screen of the service order SO77000:

Item Hierarchy

Sub-Level 2

Original

## Item

Item Type

Service Type

Service Type

Level 1

Booking

Document

77000

9010

9090

Service

Service

PKL

(Description)

Packaging and

labeling

When the system distributes costs, it applies the service order costs to the forwarding order. In this example, this is forwarding

order 750 to which product 10 belongs.

The following table gives an example of the cost distribution information for service order SO77000, where the distribution rule is

Gross Weight:

Distribution

Sub-Level 2

Charge Type

Distribution

Distribution

Quantity (KG)

Logistical

Hierarchy Level

1

Freight

document

## FB77000 –

forwarding order

750

Percentage

Amount (USD)

Reference

100

900

750

Packaging and

PACK

100

70

800

labeling

Group Logistics Scenario

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

145


1/14/26, 2:42 PM

You can use a group logistics company process to consolidate all the transportation requirements from all the companies in your

enterprise into one central logistics company. Your core business activity can be something other than providing transportation

services. For example, you have a group of companies that manufactures products. You need to transport the products to your

customers. You can have one of the following business scenarios:

One company in your group of companies manufactures products and also plans and organizes transportation services for

your other internal manufacturing companies.

One company in your group of companies does not manufacture product but instead is a dedicated group logistics

company. All your manufacturing companies use the group logistics company for transportation services.

You can have a dedicated group logistics company for the following business reasons:

## Lower transportation costs

A single dedicated logistics company can get cheaper transportation rates from a logistics service provider (LSP). For

example, each individual company approaches an LSP separately. Each company gets a less than container load (LCL) rate

from the LSP. However, if you approach an LSP as one company with one transportation requirement, you can get a full

container load (FCL) rate.

## Standardized logistics process

You have a standard shipment and tracking process across all companies. Resources are not duplicated across companies.

For example, your manufacturing companies can concentrate fully on manufacturing.

## Visibility

You can have full visibility to your transportation demands and execution from a centralized operation.

The figure below illustrates a business example of a group logistics scenario, where your companies share a single warehouse, and

where an internal company manufactures product and also provides a transportation service to the other manufacturing

companies in your group of companies. The graphic is followed by an explanation:

This is custom documentation. For more information, please visit SAP Help Portal.

146


1/14/26, 2:42 PM

Company_1000, Company_2000, and Company_3000 belong to the same enterprise. Company_1000 manufactures product, but

also provides a transportation service for Company_2000 and Company_3000.

Company_2000 and Company_3000 act as internal shipper companies, buying transportation services from Company_1000.

Company_1000 acts as a forwarding house. It buys transportation services from Logistics_Service_Provider_1, and sells

transportation services to Company_2000 and Company_3000.

Transportation Management (TM) creates an order-based transportation requirement (OTR) or delivery-based transportation

requirement (DTR) for each of the sales orders or deliveries that each company has in place with their respective customers in

Sales and Distribution on an external S/4 HANA or SAP ERP system. Company_1000 then creates a freight order for the OTRs or

DTRs, with itself as the purchasing organization in TM. It sends the freight order to Logistics_Service_Provider_1.

Logistics_Service_Provider_1 collects the cargo at the warehouse and delivers the cargo to multiple destinations. The destination

locations are geographically close together. Logistics_Service_Provider_1 sends an invoice to Company_1000 for the freight order.

Company_1000 pays Logistics_Service_Provider_1. Company_1000 uses the internal settlement process to recover the cost of

providing the transportation service from Company_2000 and Company_3000.

In a group logistics scenario, Company_1000 can create and post internal settlement documents when the life cycle status of the

freight order is In Execution.

To run a group logistics process, you must integrate orders based on orders created in Sales and Distribution (SD) or Materials

Management (MM), and deliveries created in Logistics Execution (LE) from an external S/4 HANA or SAP ERP system with a TM

component.

## More Information

This is custom documentation. For more information, please visit SAP Help Portal.

147


1/14/26, 2:42 PM

Subject

## See

Detailed process flow for a group logistics company, including cost

Group Logistics Company Process

distribution

Comparison between the standard settlement process for shippers

Comparison: Standard Shipper Process and Group Log. Co.

with the process for a group logistics company

## Process

Group Logistics Company Process

## Use

The figure below illustrates an example of a process flow for a group logistics company scenario. The graphic is followed by an

explanation:

Example of Process Flow for Group Logistics Company Scenario

## Agreements

The table gives an example of the agreements that you can put in place:

Agreement Type

Organization

Business Partner

## Internal Agreement

Sales organization of Company_1000, the group

CO_2000, the company behind sales order 2 and

logistics company. Company_1000 is a forwarding

CO_3000, the company behind sales order 3

This is custom documentation. For more information, please visit SAP Help Portal.

148


1/14/26, 2:42 PM

Agreement Type

Organization

## Business Partner

house with both a purchasing role and a sales role.

## External Agreement

Purchasing organization of Company_1000, the

External logistics service provider (LSP)

group logistics company. Company_1000 is a

forwarding house with both a purchasing role and a

sales role.

The group logistics company (Company_1000) puts an internal agreement in place that covers one of the following charge

calculation situations:

Charge for the actual freight cost for each of the companies, based on the distributed costs in the freight order

Charge a mark-up in addition to the actual freight cost based on the distributed costs in the freight order

Use a rate table for a pricing structure that is different to the freight costs

## Cost Distribution

As the group logistics company, you have the option of distributing costs in the following business documents:

## Freight order

You can distribute costs in the freight order at order/delivery item level for each of the transportation requirements in the

freight order for the following business reasons:

You want to use the distributed cost as the basis for creating internal settlement documents.

You want a breakdown of your own transportation costs and the transportation costs of the internal shipper

companies. For example, Company_1000 distributes costs in the freight order, and uses the distributed costs to

create internal settlement documents for Company_2000 and Company_3000.

## Freight settlement document

As a group logistics company, you can distribute costs in the freight settlement document for the following business

reasons:

Transport your own cargo along with the cargo from the other internal companies

## Pay the external LSP for all the transportation costs

Post the freight cost to the underlying transportation requirement (that is, the order or delivery item), for example,

the sales order item, the delivery item, or the purchase order item

## Internal settlement document

You can distribute costs in an internal settlement document if the shipper companies in your group of companies need to

post the freight cost to the underlying transportation requirement, that is, the order or delivery item. The underlying

transportation can be a sales order item, a delivery item, or a purchase order item.

For example, Company_2000 and Company_3000 distribute costs in their respective internal settlement documents to

post the freight cost to sales order 2 item 20 and sales order 3 item 30 respectively.

Example of Settlement with an External Logistics Service Provider

Company_1000 uses the following process to pay the external LSP for the transportation services:

This is custom documentation. For more information, please visit SAP Help Portal.

149


1/14/26, 2:42 PM

1. Company_1000 receives the transportation requests from the internal shipper companies as order-based transportation

requirements (OTRs) or delivery-based transportation requirements (DTRs) in Transportation Management (TM).

2. Company_1000 uses the OTR or DTR to create a freight order or freight booking. It uses the freight order or freight booking

to purchase transportation services from the LSP. Company_1000 can distribute costs in the freight order or freight

booking. This enables it to use the distributed cost as the basis for creating internal settlements and to establish what its

own share of the freight costs are.

3. Company_1000 creates a freight settlement document. It can distribute costs in the freight settlement document to

establish what its own share of the freight costs are. It can also account for its own share of the costs in financial

accounting.

a. Company_1000 creates a service purchase order and a service entry sheet (SES) in Materials Management (MM)

for the entire freight order cost.

b. Company_1000 creates a settlement management document to transfer its own share of the costs to its account

either as an expense or for material valuation.

4. The LSP (not shown in the graphic) invoices Company_1000. Company_1000 pays the LSP the total amount for the full

transportation costs.

## Example of Recovering the Cost of Providing Transportation Services

Company_1000 uses the following process to recover the costs of providing the transportation services from Company_2000 and

Company_3000:

1. Company_1000 uses the freight order or freight booking to create an internal settlement document for each of

Company_2000 and Company_3000.

  Note
The life cycle status of the freight order must be In Execution before you can create internal settlement documents for

the items in the OTR or DTR. By default, the system uses the billing schedule you specify for the business partner as the

invoice date. You can specify the billing schedule under  SAP Menu

## Logistics

 Transportation Management

## Master Data

 BP - Maintain Business Partner

 Display in BP Role: Customer (FLCU01)

 Sales and Distribution

## Billing

 Invoicing Dates .

The system uses the billing schedule for Company_2000 and Company_3000 to determine the invoice dates in the internal

settlement documents for Company_2000 and Company_3000. Company_2000 and Company_3000 are customers of

Company_1000. Company_1000 acts as a forwarding house and sells the transportation service.

2. Company_1000 uses an internal agreement to calculate costs.

You specify Company_1000 as a forwarding house. The agreement is between the purchasing organization of

Company_1000 and each of the business partners for Company_2000 and Company_3000.

The agreement can use standard rates, cost pull, or cost pull plus a mark-up as a basis for calculating charges. For more

information, see Charge Calculation.

3. Company_1000 uses Company_2000 and Company_3000 as the bill-to parties in the respective internal settlement

documents.

Company_1000 has the option of distributing costs at order/delivery item level in both internal settlement documents. This

enables Company_2000 and Company_3000 to post the freight cost to the underlying transportation requirement, for

example, to the sales order item, delivery item, or purchase order item.

4. Company_1000 posts the internal settlement documents to Sales and Distribution (DS). SD creates two intercompany

billing documents for the group logistics company CO_1000. CO_0002 and CO_0003 pay for the freight costs.

This is custom documentation. For more information, please visit SAP Help Portal.

150


1/14/26, 2:42 PM

5. SD billing uses the output type configuration of the intercompany billing document to create an IDoc. The IDoc posts an

incoming invoice for each of the companies CO_2000 and CO_3000, recording the accounts payable to Company_1000.

For more information about the settings that you need in place in TM, see TM Prerequisites for a Group Logistics Company

Process.

6. If you enable cost distribution in the internal settlement documents, a settlement management document is created when

you post the document for each of CO_2000 and CO_3000.

The settlement management document contains the following:

A line item for the underlying transportation requirement item. This is the order/delivery item on the TM side. For

example, this can be a sales order item, a delivery item, or a purchase order item.

An amount in the line item that matches the distributed amount of the order/delivery item in TM.

  Note

You must have a single SAP S/4HANA client environment to create an intercompany billing document and subsequently

to use an IDoc to trigger the corresponding incoming invoice.

## Change Process

You can start a change process from TM for an internal settlement document that you have already posted to SD. You can take one

of the following steps:

Cancel the internal settlement document that you have already created

## Change the charges and recalculate in the existing internal settlement document

When you post the new or changed internal settlement document to SD, SD cancels the already existing intercompany billing

document. For the new internal settlement document, SD creates a new intercompany billing document. For a changed internal

settlement document, SD creates a new intercompany billing document that contains the changes. The system also takes the

following actions:

Uses an IDoc to reverse the accounts payable document for the purchasing company from the SD billing document that

was created

Cancels the settlement management document that contains the distributed freight costs

Uses an IDoc to create a new Financial Accounting (FI) invoice document that updates accounts payable for the purchasing

company with the new or changed values

Creates a settlement management document that contains the new or changed distributed freight costs

## Updates to TM Settlement Documents

The following documents in TM are updated when the settlement documents are posted:

Freight settlement document with the purchase order ID and SES ID

Internal settlement document with the Sales and Distribution (SD) billing document ID

You can use the Freight Cost Distribution Report (transaction WLFLTM) and the Overview of Freight Cost Distribution

Documents function (transaction WLFLTM2) to determine the settlement management documents that are linked to the freight

settlement document and the internal settlement document.

## More Information

This is custom documentation. For more information, please visit SAP Help Portal.

151


1/14/26, 2:42 PM

Subject

## See

Overview of the business process for a group logistics company

## Group Logistics Scenario

Comparison between the standard settlement process for shippers

Comparison: Standard Shipper Process and Group Logistics

with the process for a group logistics company

## Company Process

Prerequisite settings you must specify in TM

TM Prerequisites for a Group Logistics Company Process

Prerequisite settings you must specify in Sales and Distribution

Sales and Distribution (SD) Prerequisites for a Group Logistics

## Company Process

Partner Function Codes in an OTR or DTR

## Use

In a group logistics process, you have the option of specifying an agreement partner function for a stage type and Incoterm

combination. You specify an Incoterm in the sales order or delivery. TM includes the Incoterm in the OTR or DTR. TM assigns a

party role code of Supplying Company or Receiving Company to identify the default agreement party for a stage. It assigns the

partner function code in the Business Partner tab page of the OTR or DTR.

The following table explains how TM assigns the partner function codes Supplying Company or Receiving Company:

Transportation

Sales Order or

Sales Return or

Purchase Order

## Purchase

Stock Transfer

Stock Transfer

Requirement

Delivery

Delivery

or Delivery

Return or

Delivery

## Order

Return or

Delivery

OTR header

Company of

Company of

None

## None

Company of

Company of

sales

sales

organization as

organization as

supplying

company

receiving

company

supplying plant

receiving plant as

as supplying

company

receiving

company

OTR item

None

## None

Company of

Company of

Company of

Company of

receiving plant

supplying plant

receiving plant as

supplying plant

as receiving

as supplying

company

company

receiving

company

as supplying

company

DTR header

Company of

Company of

Company of

Company of

sales

sales

receiving plant

supplying plant

organization as

organization as

as receiving

as supplying

supplying

company

receiving

company

company

company

Company

Company

of

supplying

plant as

supplying

company

of

receiving

plant as

receiving

company

Company

Company

of

receiving

plant as

receiving

company

of

supplying

plant as

supplying

company

DTR item

None

None

None

None

None

## None

This is custom documentation. For more information, please visit SAP Help Portal.

152


1/14/26, 2:42 PM

The following table explains how the system uses the Supplying Company and Receiving Company role codes in charge

calculation and in creating settlement documents:

## Order or Delivery

Supplying Company Role Code

Receiving Company Role Code

Role Code Used in Calculation

## Sales order

Company of the sales

## None

Sales returns

Purchase order

organization

None

## None

Company of the sales

Collect party is always the

organization

receiving company

Company of the receiving plant

Collect party is always the

and Settlement

Prepaid party is always the

supplying company

## Purchase return

Company of the supplying plant

## None

receiving company

Prepaid party is always the

supplying company

Stock transfer order

Company of the supplying plant

Company of the receiving plant

Role code based on Incoterm

(prepaid party as supplying

company and collect party as

receiving company)

Stock transfer return

Company of the supplying plant

Company of the receiving plant

Role code based on Incoterm

(prepaid party as supplying

company and collect party as

receiving company)

For special cases such as that of stock transfer orders you can allow separate settlements of the different parts of the freight costs

to the internal shipper company that acts as a supplying company and to the internal shipper company that acts as a receiving

company. To enable this, you can use an Incoterm in combination with the stage type to determine the prepaid and collect parties.

For more information, see Customizing for Transportation Management under  Forwarding Order Management

## Define Default

Agreement Partner Functions for Stages .

You can also define your own logic to specify the partner function that the system uses for a stage in Customizing for

Transportation Management under  Business Add-Ins (BAdIs) for Transportation Management

 Settlement

 Forwarding

## Settlement

 BAdI: Change of Bill-to Party Types for Stage Items .

  Example

You have a stock transfer order from a supplying company that belongs to Company_1000. You supply the material to a

company that belongs to Company_2000, the receiving company. You specify an Incoterm of FOB, with an FOB location of sea

port.

Company_1000 pays for all the freight costs from the supplying company to when the cargo is loaded on a ship.

Company_2000 pays for all the freight costs for the main carriage and on-carriage to the delivery location. If you do not specify

an Incoterm or stage type in the freight unit that is linked to the OTR or DTR, by default the system uses the collect party as the

receiving company in the internal settlement document for the stock transfer order or the stock transfer return.

Comparison: Standard Shipper Process and Group Logistics
Company Process

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

153


1/14/26, 2:42 PM

The table explains the differences between the standard shipper process and the process for a group logistics company in

Transportation Management (TM):

## Item

Standard Shipper Process

Group Logistics Company Process

## Business scenario

Supports the following business process:

Supports the following business process:

1. TM consolidates an order-based

1. The OTR or DTR belong to different

transportation requirement (OTR) or a

companies. TM can consolidate the OTR or

delivery-based transportation requirement

DTR in a single freight order or freight

(DTR) in a freight order or freight booking.

booking.

The associated freight settlement

documents belong to the same company.

2. Any of the companies can settle the freight

costs with the external LSP. This can be a

2. The same company settles with the external

company that has cargo in the freight

logistics service provider (LSP).

document or the company that is taking the

3. The system posts the distributed freight

exclusive role of the group logistics company.

costs to the company that settles with the

3. The company that pays for the

LSP.

transportation service distributes the freight

cost. The paying company also settles the

freight cost with the other internal companies

that share the transportation service.

## Purchasing organization

Option to specify the purchasing organization in the

Specify the purchasing organization in the freight

freight order or freight booking in TM as the

order or freight booking in TM as a forwarding house.

purchasing organization.

This enables you to use an internal settlement

process for the freight order or freight booking.

## Charge calculation

Calculate charges in the freight order or freight

In addition to the charge calculation in the freight

booking. Use the rates in the rate table, in line with

order or freight booking, calculate internal charges in

the freight agreement between the purchasing

the OTR or DTR. The internal charges in the OTR or

organization in the freight order or freight booking

DTR give you, as the group logistics company, the

and the LSP.

amounts you expect to receive from the internal

Internal settlement

Not required

document

Cost distribution in the

Not required

freight order

shipper companies.

You, as a group logistics company, use an internal

settlement document to recover the cost of providing

the transportation service from the other internal

shipper companies. You can create and post an

internal settlement document when the life cycle

status of the freight order is In Execution.

Distribute costs in the freight order if you want to use

the distributed cost as a basis for internal

settlement.

Cost distribution in the

Distribute costs in the freight settlement document

Distribute costs in the freight settlement document if

freight settlement

to enable you to post freight costs to the underlying

you, as a group logistics company, have the following

document

transportation requirement, for example, a sales

business requirements:

order item, a delivery item, or a purchase order item.

Transport your own cargo along with the

cargo from the other internal shipper

companies

Pay the external LSP for all transportation

costs

Post the freight cost to an underlying

transportation requirement, for example, a

This is custom documentation. For more information, please visit SAP Help Portal.

154


1/14/26, 2:42 PM

## Item

Standard Shipper Process

Group Logistics Company Process

sales order item, a delivery item, or a

purchase order item

Cost distribution in the

## Not required

Distribute costs in the internal settlement document

internal settlement

document

if an internal shipper company needs to post the

freight cost to an underlying transportation

requirement, for example, a sales order item, a

delivery item, or a purchase order item.

The table explains the differences in the setup and posting of freight settlement and internal settlement documents between the

standard shipper process and the process for a group logistics company:

## Item

Standard Shipper Process

Group Logistics Company

## Organizations

Standard organizational setup. Purchasing

In TM, if you want to base the internal settlement

organization is set up with organizational unit

process on the freight order or freight booking, the

function specified as Purchasing.

purchasing organization in the freight order or freight

booking is set up with organizational unit function

specified as a forwarding house.

## Posting of freight

TM posts the freight settlement document, with

TM posts the freight settlement document, with

settlement document to

distributed costs, to MM.

distributed costs, to MM.

Materials Management

(MM)

Purchase order and service entry sheet (SES):

Purchase order and service entry sheet (SES):

Creates a service purchase order and

Creates a service purchase order and

includes the items that correspond to the

includes the items that correspond to the

total amount in document currency for the

total amount in document currency for the

freight settlement document.

freight settlement document

Creates and posts an SES to confirm the

Creates and posts an SES to confirm the

services in the service purchase order

services in the service purchase order

Settlement management document:

Settlement management document:

Creates a settlement management document

Creates a settlement management document

with a line item for each line item in the

if you, as the group logistics company,

freight order or freight booking

transport cargo of your own sales order

The account assignment details for the line

item from the relevant document in the

order/delivery item are transferred to the

settlement management document items.

items, purchase order items, or delivery line

items in the freight order or freight booking.

You also include cargo from the other internal

shipper companies in your orders.

For example, the assignment details from the

Creates settlement management document

sales order item, the purchase order item, or

items. The freight order items that are linked

the stock transfer order item are copied to

to own sales order items, purchase order

the settlement management items.

items, or delivery line items for which the

Posting of internal

## Not required

settlement document to

Sales and Distribution

(SD)

group logistics company pays the freight

cost.

Creates an intercompany billing document in Sales

and Distribution (SD) billing. This creates the

accounts receivable for the group logistics company.

The accounts receivable indicates the amounts the

group logistics company needs to recover from the

other internal shipper companies.

SD Billing creates an IDoc as follows:

This is custom documentation. For more information, please visit SAP Help Portal.

155


1/14/26, 2:42 PM

## Item

Standard Shipper Process

## Group Logistics Company

The SD billing document uses the output

type configuration of the intercompany billing

document to create an IDoc.

The IDoc posts an incoming invoice for the

each of companies involved in the

transportation.

This records the accounts payable to you, as the

group logistics company. For example, the IDoc posts

an incoming invoice for Company_2000 and

Company_3000, recording the accounts payable to

Company_1000.

Creates a settlement management document with a

line item for each line item in the freight order or

freight booking. It copies the account assignment

details from the relevant order/delivery item, for

example, from the sales order item, purchase order

item, or stock transfer order item. The settlement

management document establishes links to the sales

order item, purchase order item, or delivery line item

of the orders that belong to the internal shipper

companies.

More Information

Subject

## See

Overview of the business process for a group logistics company

## Group Logistics Scenario

Detailed process flow for a group logistics company, including cost

Group Logistics Company Process

distribution

Prerequisite settings you must specify in TM

TM Prerequisites for a Group Logistics Company Process

Prerequisite settings you must specify for setting up the posting of

Sales and Distribution (SD) Prerequisites for a Group Logistics

documents in Sales and Distribution (SD)

## Company Process

Organizational Prerequisites in TM and Sales and Distribution
(SD) for Group Logistics Process

## Organizational Settings

You have specified your organizational structure in Transportation Management (TM) in line with the organizational structure in

Materials Management (MM) and Sales and Distribution (SD).

For example, the following table contains the organizational structure you can build in SD and MM, along with the corresponding

structure in TM:

This is custom documentation. For more information, please visit SAP Help Portal.

156


1/14/26, 2:42 PM

Enterprise Structure Entity

Enterprise Structure Entity ID

TM Organization Management

TM Organization Management

## Company

Sales organization

1000

S001

Entity

## Entity ID

Company organization

CO_1000

Sales organization

SO_S001

Customer

## Company

Sales organization

Customer

## Company

Sales organization

Purchasing organization

CO_1000

Business partner

CO_1000

2000

S002

Company organization

CO_2000

Sales organization

SO_S002

CO_2000

Business partner

CO_2000

3000

S301

S301

Company organization

CO_0003

Forwarding house

FH_FH301

Vendor

CO_3000

Business partner

CO_3000

You can specify the organizational master data settings in Customizing for Enterprise Structure under Definition. You can link the

master data objects under Assignment.

You can use the Create and Merge Organizational Hierarchy Customizing activity to upload your organizational hierarchy. This

helps you to copy your organizational settings. For more information, see Customizing for Transportation Management under

## Master Data

 Organizational Management

 Organizational Model

.

Alternatively, you can specify the organizational settings in Customizing for Transportation Management under  Master Data

 Organizational Management

 Organizational Model

 Create Organizational Model

.

You must specify the following settings under your corporate organizational model:

All company organizations (company codes) in your corporate organization

An organization for your group logistics company, with an organizational unit function of Forwarding House.

You specify the group logistics company as a forwarding house because it has both a purchasing role and a selling role. It

purchases transportation services from an outside carrier and sells transportation services to the other internal shipper

companies in your corporation.

Enable the group logistics company organization as a group logistics company under  Org. Data

 Detail Settings

## Group

Logistics Company .

## Organizational Settings for Internal Settlement

To create internal settlement documents in TM and to post the internal settlement documents to SD, you must specify the

following settings:

1. Forwarding house in organization management

Define the forwarding house so that the business systems group organizational unit ID of the organization's data in

organizational management ID is the same as that used in the ERP enterprise structure for the sales organization and the

purchasing organization. The ERP enterprise structure has an identical sales organization ID and purchasing organization

ID. For example, you have 0001 for the sales organization and 0001 for the purchasing organization.

2. Business partner with role of Customers

This is custom documentation. For more information, please visit SAP Help Portal.

157


1/14/26, 2:42 PM

You must create a business partner (BP) for each of the company organizations (company codes) that participate as

internal shipper companies in the group logistics process.

3. Assign business partners to company organizations in TM

You must assign the business partner to a company organization (company code) in TM. For more information, see

Customizing for Transportation Management under  Master Data

 Organizational Management

 Organizational

## Model

 Change Organizational Model (transaction PPOME)

. Enter the business partner under  Org. Data

 Business

## Settings

## Business Partner

 of the relevant company organization.

More Information

Subject

## See

How TM assigns a partner function code of Supplying Company or

## Partner Function Codes in an OTR or DTR

Receiving Company to identify the default agreement party for a

stage

Prerequisite settings in Sales and Distribution (SD)

Sales and Distribution (SD) Prerequisites for a Group Logistics

## Company Process

Explanation of where a group logistics process fits in a business

Group Logistics Scenario

process

Detailed explanation of the group logistics process

## Group Logistics Company Process

TM Prerequisites for a Group Logistics Company Process

## Document Type Settings

## Integration of orders and deliveries

You have specified an order-based transportation requirement (OTR) type and a delivery-based transportation (DTR) type

to transfer the transportation requirements.

For example, in this way TM uses the sales orders and deliveries of the internal shipper companies to create OTR and DTR

documents for the internal shipper companies in TM.

You must enable the following settings in the OTR or DTR type:

Internal charge calculation

## Internal settlement

Internal settlement document type as the default internal settlement document type

You have the option of specifying the following settings in the OTR or DTR type:

## Stage profile, to determine the stage type in a freight unit

For example, you can use the group logistics process in an internal settlement scenario for a stock transfer order.

You can settle the different parts of the freight costs to the internal shipper company that acts as a supplying

company and to the internal shipper company that acts as a receiving company.

To enable this, you can use an Incoterm in combination with the stage type to determine the prepaid and collect

parties. For example, based on an Incoterm of Free on Board (FOB), you can specify that the supplying company

pays for the pre-carriage and the receiving company pays for the main carriage and on-carriage.

This is custom documentation. For more information, please visit SAP Help Portal.

158


1/14/26, 2:42 PM

Automatic freight unit building

## Freight order type

You have enabled the freight order or freight booking for cost distribution. You use this freight order type when your group

logistics company has the following business requirements:

You want to use the distributed cost as the basis for creating internal settlement documents.

You want a breakdown of your own transportation costs and the transportation costs of the internal shipper

companies. For example, Company_1000 distributes costs in the freight order and uses the distributed costs to

create internal settlement documents for Company_2000 and Company_3000.

You can use the distributed costs in a freight order or freight booking to calculate charges for internal settlement. The

system uses the distributed costs in the freight order or freight booking as the basis for pulling the costs into the

calculation process. For more information, see Freight Order Management.

## Freight settlement document type

You have enabled a freight settlement document type for cost distribution in Customizing for Transportation Management

under  Settlement

## Freight Settlement

 Define Freight Settlement Document Types . You use this freight settlement

document type when your group logistics company has the following business requirements:

Transports its own cargo along with the cargo from the other internal shipper companies

Pays the external logistics service provider (LSP) for all transportation costs

Posts the freight cost to the underlying transportation requirement, for example, to the sales order item, delivery

item, or purchase order item

## Internal settlement document type

You have specified a forwarding settlement document type for internal settlement documents in Customizing for

Transportation Management under  Settlement

 Forwarding Settlement

 Define Forwarding Settlement

Document Types .

You have the option of enabling the internal settlement document type for cost distribution if an internal shipper

company needs to post the freight cost to the underlying transportation requirement, for example, to the sales order

item, delivery item, or purchase order item.

You use an intercompany settlement in the group logistics process. By default, TM creates an intercompany settlement

document for organizations that belong to different company codes.

Cost distribution settings

## Cost distribution methods

You have specified the relevant cost distribution methods under  Basic Functions

 Cost Distribution

## Define

Cost Distribution Methods

## Cost distribution profile

You have specified the relevant settings in a cost distribution profile under  Basic Functions

## Cost Distribution

 Define Cost Distribution Profiles .

## Cost distribution profile assignment

You have assigned the cost distribution profile to a charge profile. You have assigned the charge profile to the

forwarding house of the group logistics company.

For more information on cost distribution settings in a group logistics process, see Group Logistics Company Process.

This is custom documentation. For more information, please visit SAP Help Portal.

159


1/14/26, 2:42 PM
## Profile Settings

## Forwarding settlement profile and calculation profile on the sales side

You have created a forwarding settlement profile and calculation profile for sales. You have assigned the forwarding

settlement profile and the calculation profile to the relevant sales organization. For more information, see Forwarding

Settlement.

## Freight settlement profile and calculation profile on the purchasing side

You have created a freight settlement profile and calculation profile for purchasing. You have assigned the freight

settlement profile and calculation profile to the relevant forwarding house or purchasing organization. For more

information, see Freight Settlement.

## Default Agreement Partner Function for a Stage

You have the option of specifying an agreement partner function for a stage type and Incoterm combination. TM uses the

agreement partner function to identify the default agreement party for a stage. For more information, see Partner Function Codes

in an OTR or DTR.

## Calculation Level for a Purchasing Organization

You can plan more than one freight order to deliver the transportation requirements in an OTR or DTR. You can use freight orders

that contain different purchasing organizations. However, you must specify the same calculation level for each of the purchasing

organizations that you use in each of the freight orders.

More Information

Subject

## See

Overview of the business process for a group logistics company

## Group Logistics Scenario

Detailed process flow for a group logistics company, including cost

Group Logistics Company Process

distribution

Comparison between the standard settlement process for shippers

Comparison: Standard Shipper Process and Group Logistics

with the process for a group logistics company

## Company Process

How TM assigns a partner function code of Supplying Company or

## Partner Function Codes in an OTR or DTR

Receiving Company to identify the default agreement party for a

stage

Organizational settings you must specify for a group logistics

Organizational Prerequisites in TM and Sales and Distribution (SD)

process

for Group Logistics Process

Prerequisite settings you must specify in Sales and Distribution

Sales and Distribution (SD) Prerequisites for a Group Logistics

## Company Process

Sales and Distribution (SD) Prerequisites for a Group Logistics
Company Process

## Integration

This is custom documentation. For more information, please visit SAP Help Portal.

160


1/14/26, 2:42 PM

## Internal settlement integration

On the external S/4 HANA or SAP ERP, you have enabled integration with SD with customizing activities in Billing under

Integration with Other SAP Components

 Transportation Management

 Invoice Integration .

## Freight settlement document integration

You have specified the prerequisite settings for posting freight settlement. For more information, see Freight Settlement.

You must specify the relevant settings in Customizing if your group logistics company meets the following business criteria:

## Has its own cargo in a freight order

Distributes costs at order/delivery item level in the freight order

## Creates a freight settlement document for that freight order

In Customizing in the external S/4 HANA or SAP ERP, you have also specified the following settings:

Assign Purchasing Information for Posting

Assign Service Master Record and Account Assignment Category

## Tax determination setting under Tax

## Mapping for Cost Distribution, when cost distribution is enabled in FSD in TM

For more information about the standard process of distributing costs for shippers, see Cost Distribution for Shippers.

## Mapping Settings

## Map charge type to condition type

You have specified the charge type that you created in the steps above in a condition type under

Integration with Other

## SAP Components

 Transportation Management

 Invoice Integration

## Billing

 Assignment of Transportation Charge

## Types

 Assign Condition Types .

Map transportation charge to cost distribution

You have specified the relevant settings under

Integration with Other SAP Components

 Transportation Management

## Invoice Integration

## Mapping for Cost Distribution

 Assign Transportation Charge Types to Condition Types .

You must map these settings if you enable your internal settlement documents for cost distribution in TM.

## Settlement Management Document Settings

You have specified the relevant settings in Customizing under

Integration with Other SAP Components

 Transportation

## Management

 Invoice Integration

## Billing

 Mapping for Cost Distribution .

## Other Settings

For more information about how to enable sales and distribution to post automatically to a vendor account in financial accounting

for a group logistics process, see SAP Note 2157070

.

## More Information

This is custom documentation. For more information, please visit SAP Help Portal.

161


1/14/26, 2:42 PM

Subject

## See

Overview of the business process for a group logistics company

## Group Logistics Scenario

Detailed process flow for a group logistics company, including cost

Group Logistics Company Process

distribution

Comparison between the standard settlement process for shippers

Comparison: Standard Shipper Process and Group Logistics

with the process for a group logistics company

## Company Process

Organizational settings you must specify for a group logistics

Organizational Prerequisites in TM and Sales and Distribution (SD)

process

for Group Logistics Process

Prerequisite settings you must specify in TM

TM Prerequisites for a Group Logistics Company Process

Automatic Change Management Process for Settlements

## Use

As a logistics service provider (LSP), you may need to make changes in your forwarding order process after you have billed your

external customer in a forwarding settlement scenario, or your internal customer in an internal settlement scenario. In

Transportation Management (TM), you may need to change a forwarding order after you have created a forwarding settlement

document or an internal settlement document, and after you have posted the settlement document to Sales and Distribution (SD)

to create the billing document.

Alternatively, you are a requester of logistics services, such as a shipper. You have a freight order process in place with an LSP or

carrier, to provide transportation services. You may need to make changes in the freight order process after you have created a

freight settlement document. In TM, you may need to change a freight order after you have created a freight settlement document

and after you have posted the freight settlement document to Materials Management (MM).

Changes can come from the following sources:

## Missing cargo in the transit warehousing process

For example, you are an LSP and in your business process you have integrated TM with Extended Warehouse Management

(EWM). You use transit warehousing, where you receive, consolidate, or ship cargo as part of a longer transportation chain.

You receive cargo and store it until it is required for transportation to the next stop in the transportation chain.

As part of the transit warehousing process, EWM updates the freight order or freight booking in TM. If there is missing

cargo, TM creates a discrepancy. For more information, see Handling Discrepancies in Transit Warehousing Process.

## Direct change in your freight order from your carrier

For example, you are an LSP and you have a forwarding order in process with a requester of transportation services, such as

a shipper. You have a freight order in process with a carrier to provide the transportation services. Your carrier reports

directly to your office that an item of cargo was missing when the carrier picked up cargo at a source location. You update

the freight order that you have in process with the carrier. This in turn updates the forwarding order that you have in

process with the shipper.

## Direct change to the charges in your freight order

For example, you are a shipper and you have a freight order in place with a provider of transportation services, such as an

LSP or carrier. You realize that your service provider had some additional unplanned charges, for example, demurrage

charges because of a delay at a delivery location. You update the freight order with the unplanned charge for demurrage.

This is custom documentation. For more information, please visit SAP Help Portal.

162


1/14/26, 2:42 PM

Alternatively, you are a shipper and you have a freight agreement with your LSP or carrier and you realize that your rates are

revised. You update the rates and then update the freight orders to reflect the revision of the rates by recalculating the

charges in the freight order.

The following table describes the role you play in your business, and the documents you work with in TM:

## Your Role

Role of Business Partner

## Business Document

Provider of logistics services, such as an

Requester of transportation services

Forwarding order on an external customer

LSP

outside your company, such as a shipper

Provider of logistics services such as an

Requester of transportation services inside

Forwarding order on an internal customer

LSP

your company, such as another business

organization

Requester of transportation services, such

Provider of logistics services, such as an

Freight order on an LSP or carrier

as a shipper

## LSP or carrier

Subcontractor, requesting transportation

Provider of logistics services, such as a

Freight order on a carrier

services from another transportation

carrier

provider, such as an LSP

You can streamline and automate the process of making changes. In a streamlined process, you only need to make a change in one

business document, for example, the freight document such as the freight order, freight booking, or service order, and forwarding

order. You run the background processing functions Creation and Transfer of Freight Settlement Documents or Creation and

Transfer of Forwarding Settlement Documents. In the background, the system makes the required change in the relevant

downstream business documents. The following table describes the downstream documents that the system can update

automatically:

Document You Change

Downstream Document in TM

Downstream Document

## Forwarding order

Forwarding settlement document

Internal settlement document

## Credit memo

Sales and distribution (SD) billing

document

Freight order, freight booking, service order

Freight settlement document

## Purchase order

Charge correction advice document

Service entry sheet (SES)

## Credit memo

Using an automated process also means you have control points at key stages in the change process. These controls ensure you

have an efficient change process.

More Information

## Subject

## More Information

Change management process for forwarding settlement

Automatic Change Management for Forwarding Settlements

documents

Change management process for freight settlement documents

## Automatic Change Management for Freight Settlements

This is custom documentation. For more information, please visit SAP Help Portal.

163


1/14/26, 2:42 PM

## Subject

## More Information

Background processing function to automatically change a

Creation and Transfer of Forwarding Settlement Documents

forwarding settlement document and an invoice posting

Standard credit memo process for forwarding orders

Credit Memos for Forwarding Orders

Changing a forwarding order

Editing of a Forwarding Order

## How EWM handles discrepancies

Handling Discrepancies in Transit Warehousing Process

Automatic Change Management for Forwarding Settlements

## Use

## Forwarding and Internal Settlement Change Management Process

The following table describes the steps you, as a logistics service provider (LSP), can take to implement a change in the forwarding

order process:

Process Stage

## Action

Before you create a forwarding settlement document or an internal

Make the change directly in the forwarding order.

settlement document

After you create a forwarding settlement document or an internal

Cancel the forwarding settlement document or internal settlement

settlement document, but before you post the SD billing document.

document. Change the forwarding order, and create a new

settlement document.

This enables you to keep a one-to-one relationship between the

settlement document in TM and your subsequent billing document

in Sales and Distribution (SD).

Alternatively, if the forwarding order has an invoicing status of

Partially Invoiced, you can leave the existing settlement document

in place and create a new settlement document for the delta

amount.

After you post a settlement document to create an SD billing

Cancel an existing settlement document by creating a credit memo

document.

in TM. Post the credit memo to cancel the existing SD billing

document.

When you create a new settlement document in TM, the new

settlement document contains the updated amounts including the

changes. You post the settlement document to SD to create an SD

billing document for the new amount.

This enables you to keep a one-to-one relationship between the

forwarding order in TM and your billing document in SD.

Alternatively, if the forwarding order has an invoicing status of

Partially Invoiced, you can create a new settlement document for

the delta amount, and send this to SD to create a new SD billing

document for the delta amount.

## Change Management Process Settings

This is custom documentation. For more information, please visit SAP Help Portal.

164


1/14/26, 2:42 PM

You specify the change management strategy for your forwarding orders in the relevant settlement profile under Customizing for

Transportation Management under  Define Settlement Profile

 Settlement Profile Settings

## Change Process FWSD . You

can specify a strategy of Standard Settlement Process, Reverse and Repost, or Delta Only. The system determines the process

steps according to the strategy that you choose.

You can control the change process strategy for settled charge lines when there's an increase in the charge lines from the

Customizing activity for Transportation Management under  Basic Functions

## General Settings

 General Settings for TM .

For more information, see Controlled Change Process for Freight and Forwarding Settlements.

You can specify the approach the system takes when you change a forwarding order for which a settlement document already

exists:

## Reverse and repost a settlement document

When you change a forwarding order, in the background Transportation Management (TM) creates a credit memo that

automatically cancels the settlement document in TM and the associated billing document in SD. The system creates a new

forwarding settlement document or internal settlement document, and a new billing document for the entire forwarding

order.

You must choose this option if you want to ensure that the replacement forwarding settlement document or internal

settlement document and replacement billing document are the only documents for the forwarding order that contain the

full total amount charge.

For example, in a forwarding settlement scenario, you have the following business documents and charges:

Business Document

Amount (USD)

Forwarding order at first, ID 1234

Forwarding settlement document, ID 810909

1000

1000

Sales and Distribution (SD) billing document, ID 5600121

1000

You then change the charge amount in the forwarding order from USD 1000 to USD 1200. In the reverse and repost

strategy, the system creates the following business documents:

In TM, a credit memo 9560005 for USD 1000 that cancels the forwarding settlement document 810909

On posting the credit memo 9560005 to SD, an SD credit memo 9951007 for USD 1000

On the overall accounting side, this means that the customer doesn't have to pay any charge, as the amount for the credit

memo 9560005 (USD 1000) cancels the amount of the forwarding settlement 810909 (USD 1000).

The system then creates the following documents:

In TM, the forwarding settlement document 810945 for USD 1200

On posting the forwarding settlement document to SD, the SD billing document 5600181 for USD 1200

On the overall accounting level, following the original forwarding settlement document, the credit memo, and the second

forwarding settlement document, the customer eventually must pay USD 1200.

If you change a forwarding order that is included in a collective forwarding settlement document or internal settlement

document, the credit memo that the system creates only cancels the items belonging to the forwarding order from the

collective settlement document

For example, you have a collective forwarding settlement document with a lifecycle status of Invoiced that includes the

following forwarding orders:

This is custom documentation. For more information, please visit SAP Help Portal.

165


1/14/26, 2:42 PM

Settlement Line Item Forwarding Order

Amount (USD)

10

20

30

1

2

3

1000

2000

3000

You change to forwarding order 1 from USD 1000 to USD 1200.

The system creates the following documents:

In TM, a credit memo for USD 1000 for forwarding order 1 only. This is item 10 of the existing settlement document.

On posting the credit memo to SD, an SD credit memo for USD 1000 for forwarding order 1

On the overall accounting level, the customer doesn't have to pay any charge for this forwarding order at this point in time.

The credit memo amount of USD 1000 cancels the forwarding settlement amount of USD 1000 for forwarding order 1.

The system then creates the following documents:

In TM, a forwarding settlement document for USD 1200 for forwarding order 1

On posting the forwarding settlement document to SD, an SD billing document for USD 1200

On the overall accounting level, from the original forwarding settlement document, to the credit memo, and on to the

second forwarding settlement document, the customer eventually pays USD 1200 for forwarding order 1.

## Delta amount only

When you change a forwarding order, the system doesn't cancel the existing settlement document and the associated

billing document. Instead, it creates a new settlement document and a new billing document for the amount that isn't

already covered by the existing forwarding settlement document or internal settlement document and billing document.

For example, in a forwarding settlement scenario, you have the following documents and charges:

Business Document

Amount (USD)

Forwarding order 1234 at first

1000

Forwarding settlement document 810909

1000

SD billing document 5600121

1000

You then change the charge amount in the forwarding order from USD 1000 to USD 1200. In the delta only strategy, the

system creates the following business documents:

Forwarding settlement document 810945 for USD 200

SD billing document 5600181 for USD 200

At the overall accounting level, the customer must pay the amounts in both forwarding settlement documents, a total of

USD 1200.

The following table describes the action that the system takes using the different strategies when you change a forwarding order

and the forwarding order has an existing settlement document:

This is custom documentation. For more information, please visit SAP Help Portal.

166


1/14/26, 2:42 PM

## Settlement

Lifecycle Status

Reverse and Repost

Delta Only

## Delta Only

Follow up Action

Document Type

Forwarding

settlement

document or

internal settlement

document

Forwarding

settlement

document or

internal settlement

document

Invoicing Status of

Invoicing Status of

Invoicing Status of

Forwarding Order:

Forwarding Order:

Forwarding Order:

Partially invoiced,

Over Invoiced or

Partially invoiced

Over Invoiced, or

Not Up-to-Date

Not Up-to-Date

In Process/Ready

Cancel the existing

Cancel the existing

## None

for Posting

settlement

document or

settlement

settlement

document or

settlement

document item

document item

Invoice Posted

Create a credit

Create a credit

## None

memo to reverse

memo to reverse

the settlement

the settlement

document or

settlement

document or

settlement

document item

document item

Credit memo

In Process/Ready

Cancel the existing

Cancel the existing

## None

for Posting

credit memo

credit memo

Credit memo

In Process/Ready

Cancel the existing

Cancel the existing

## None

for Posting

credit memo

credit memo

Credit memo

Invoiced Posted

Create a credit

Create a credit

## None

memo for the credit

memo for the credit

remaining amount

remaining amount

in the forwarding

in the forwarding

order.

order.

Create a new

settlement

document

Create a new

settlement

document

Create a new credit

memo for the

existing settlement

document, reversing

the settlement

document or the

settlement

document item.

Create a new

settlement

document.

Create a new credit

memo for the

existing settlement

document, reversing

the settlement

document or the

settlement

document item.

Create a new

settlement

document.

Create a new

settlement

document

Forwarding

settlement

document, internal

settlement

document, or credit

memo

Posting Started

Skip the change

Skip the change

Skip the change

Reexecute the

process for these

process for these

process for these

change process

settlement

settlement

settlement

once the documents

documents and

documents and

documents and

move out of the

report as errors

report as errors

report as errors

lifecycle status

This is custom documentation. For more information, please visit SAP Help Portal.

167


1/14/26, 2:42 PM

  Note

If you specify a change strategy of Delta Only and the invoicing status of the forwarding order is Over Invoiced or Not Up-to-

Date, the system processes the change as if you had a strategy of Reverse and Repost.

The system sets the invoicing status for the order to Not Up-to-Date when the charge in the order has a significant change in

either a new agreement or calculation sheet being determined for the order, or due to the change of a charge that has already

been settled in the order.

When you've enabled the setting Settlement Change Process: Reverse and Repost in Customizing for Transportation

Management under  Basic Functions

## General Settings

 General Settings for TM  and the settled charge line increases,

the system sets the invoicing status of the forwarding order as Not Up-to-Date. If the setting is disabled, the invoicing status is

set to Partially Invoiced.

The invoicing status of the order is set to Over Invoiced if there's a net negative value change in the order charge to what was

already settled, due to the addition of new charges that are negative in nature. In these cases, the system reverses the

settlement documents that you posted earlier to update the follow-on documents.

In a collective settlement document, the system applies the change process only for the items that have changed in a forwarding

order.

  Note

You can't post a forwarding settlement document with a net negative value. The credit memo, which is created automatically for

the settlement documents to be reversed during the change process, is always created for the full value of the settlement

document for the order that has changed. For a collective settlement, the credit memo is created for the full amount for the

settlement document item corresponding to the order that has changed.

The new settlement documents can be collective settlement documents in the following situations:

You enable an Invoice Creation Method of Collective when you run the background processing function Creation and

Transfer of Forwarding Settlement Documents (program /SCMTMS/CFIR_CREATE_BATCH).

You select the Collective Settlement checkbox in the relevant settlement profile.

  Note

In execution-based settlement scenarios, such as a buyer’s consolidation, a route-based settlement, or a trailer-unit based

settlement, the forwarding order doesn't contain the charge calculation details as the charges are only calculated in the

forwarding settlement documents. Therefore, for these scenarios, you can't use change tracking and change management in

the forwarding settlement process. For more information, see Execution-Based Settlement.

## Forwarding Settlement Document and Credit Memo Settings

You've enabled all the relevant settings for working with forwarding settlement documents and credit memos. For more

information about credit memos, see Credit Memos for Forwarding Orders.

The system determines the settlement document type as follows:

1. From BAdI: Forwarding Settlement Document Type Determination

For more information, see Customizing for Transportation Management under  Business Add-Ins (BAdIs) for

Transportation Management

## Settlement

 Forwarding Settlement

.

2. From the forwarding settlement document type

This is custom documentation. For more information, please visit SAP Help Portal.

168


1/14/26, 2:42 PM

For more information, see Customizing for Transportation Management under  Settlement

## Forwarding Settlement

 Define Forwarding Settlement Document Types .

3. From the default credit memo type

For more information, see Customizing for Transportation Management under  Settlement

## Forwarding Settlement

 Define Credit Memo Reason Codes and Types for Forwarding SDs .

If the system uses the credit memo type for a change process, you must specify a credit memo type in which you've enabled the

following settings:

Influence Invoicing Status

Automatically Enter Credit Amount

More Information

## Subject

## More Information

Change management process for settlement documents

Automatic Change Management Process for Settlements

Example of an Automated Change Management Process in a

Example of Automated Change Management in an FWSD Scenario

## Forwarding Settlement Scenario

Background processing function to automatically change a

Creation and Transfer of Forwarding Settlement Documents

forwarding settlement document and an invoice posting

Controlled Change Process for Freight and Forwarding Settlements

Controlled Change Process for Freight and Forwarding Settlements

Example of Automated Change Management in an FWSD
Scenario

## Use

1. You are a logistics service provider (LSP) and you work with a carrier to deliver your transportation requirements. Your

carrier reports that they picked up the cargo at a customer location. When this is done, you create the forwarding

settlement document to bill the customer.

However, you subsequently find out that the quantity of the cargo you get from your customer for transportation does not

match the quantity requested by your customer originally. You subsequently update the forwarding order with the change

in quantity. This results in a change to the charges in the forwarding order.

2. You have enabled the required Customizing settings for an automated change management process. For more information,

see Automatic Change Management for Forwarding Settlements.

3. You have enabled the background processing function Creation of Forwarding Settlement Documents

(/SCMTMS/CFIR_CREATE_BATCH), with a Creation Type of Include Changed FWOs or Only Changed FWOs.

Alternatively, you go to the impacted forwarding order in the personal worklist or in the individual order and you create the

forwarding settlement document.

In your business process, you keep a one-to-one relationship between your forwarding order in TM and your billing

document in Sales and Distribution (SD). In the settlement profile that the system applies to the forwarding order and the

customer, you have defined the change process strategy for forwarding settlement documents as Reverse and Repost.

In the background, the system performs the following tasks:

This is custom documentation. For more information, please visit SAP Help Portal.

169


1/14/26, 2:42 PM

TM creates a credit memo with the amount equal to the amount in the existing forwarding settlement document.

The credit memo cancels the existing forwarding settlement document.

On posting the credit memo to SD, the system creates a credit memo in SD to cancel the existing billing document.

TM creates a new forwarding settlement document for the changed forwarding order. The forwarding settlement

document now has an amount that is equal to the amount in the forwarding order after the change.

On posting the forwarding settlement document to SD, SD creates a new billing document.

4. Alternatively, in your business process, you don’t keep a one-to-one relationship between your forwarding order in TM and

your billing document in SD. You define a change process strategy for forwarding settlement documents as Delta Only in

the relevant settlement profile. The system applies the settlement profile to the forwarding order and the customer.

You make a change to the forwarding order, and the invoicing status of the forwarding order changes to Partially Invoiced.

In the background, the system performs the following tasks:

TM creates a new forwarding settlement document only for the extra charge.

On posting the forwarding settlement document to SD, SD creates a new billing document only for the extra charge.

Alternatively, you make a change to the forwarding order, and the invoicing status changes to Over Invoiced or Not Up-to-

Date. The system automatically uses the Reverse and Repost change process strategy. In the background, the system

performs the following tasks:

TM creates a credit memo with the amount equal to the amount in the existing forwarding settlement document.

This cancels the existing forwarding settlement document.

On posting the credit memo to SD, SD uses the credit memo to cancel the existing billing document.

TM creates a new forwarding settlement document for the changed forwarding order. The amount in the new

settlement document is equal to the amount in the forwarding order after the change.

On posting the forwarding settlement document to SD, SD creates a new billing document.

More Information

## Subject

## More Information

Change management process for forwarding settlements and

Automatic Change Management for Forwarding Settlements

internal settlements

Automatic Change Management for Freight Settlements

## Use

You're a requester of transportation services, such as a shipper or a logistics service provider (LSP). You create a freight order,

freight booking, or service order in your Transportation Management (TM) system to request transportation services. An LSP can

provide transportation services if you're a shipper. Alternatively, a carrier can provide transportation services if you're an LSP.

Sometimes, there can be a difference between what you expect to pay against your service provider expects to be paid. To keep

good business relationships, you can work closely with your service provider to resolve these differences in a collaborative way. For

more information, see Dispute Management for Freight Settlements. When you resolve a dispute using the dispute management

process, the system updates the freight order with the changed charge information.

This is custom documentation. For more information, please visit SAP Help Portal.

170


1/14/26, 2:42 PM

Alternatively, you may not have a dispute management process in place with your service provider. Instead, your service provider

communicates a discrepancy directly to your shipping department. You agree with the change, and you update the freight order

directly with the changed information.

You use the background function Creation of Freight Settlement Documents (program /SCMTMS/SFIR_CREATE_BATCH) to

create, change, and transfer the freight settlement documents to Materials Management (MM) (see Creation and Transfer of

Freight Settlement Documents). The freight settlement document contains the changes from the freight order. Alternatively, you

go to the impacted freight order from the personal worklist or the individual document, and you create the freight settlement

document.

## Change Management Process Settings

The system uses the automatic change management process that you specify in the relevant settlement profile in Customizing.

For more information, see Customizing for Transportation Management under  Settlement

 Define Settlement Profile

 Change Process FSD .

You can control the change process strategy for settled charge lines when there's an increase in the charge lines from the

Customizing activity for Transportation Management under  Basic Functions

## General Settings

 General Settings for TM .

For more information, see Controlled Change Process for Freight and Forwarding Settlements.

TM uses the following elements to determine what approach to take with the change:

Change Process FSD setting in the settlement profile

## Default credit memo type

You must specify a default credit memo type in Customizing for Transportation Management under  Settlement

 Freight

## Settlement

 Define Credit Memo Reason Codes and Types for Freight SDs . You must also specify the following settings

for the default credit memo type:

Influence invoicing status

Automatically enter the credit amount

## Lifecycle status of the freight settlement document

You have a freight order for transporting your cargo that you agree with your carrier, for the freight cost of 2000 USD.

Consider the following business scenarios for change:

## Additional Detention Charge

Your carrier communicates to you that there are additional charges of USD 300 due to an unplanned delay at the unloading

point. You verify this request from the carrier and agree to pay for the unplanned detention charge. In the relevant freight

order, you change the transportation charge by adding the detention charge for USD 300. This takes the freight order

charge to USD 2300. The freight order has an invoicing status of Partially Invoiced.

## Additional Discount due to Better Volume

Your purchasing department communicates that the carrier has agreed to an additional discount due to a better volume of

transactions. Because of this, there's a downward revision of the overall freight charges of USD 200. You add the discount

charge line in the freight order to make this change. The freight order charges are reduced to USD 1800. In this case, the

freight order has an invoicing status of Partially Invoiced.

## Decrease in Rate for the Base Freight

Your purchasing department communicates that the carrier has agreed to a reduced rate for freight due to a better volume

of transactions. Because of this, there's a downward revision of the overall freight charges for the freight order of USD 100.

You change the basic freight charge to reflect this reduction. The freight order changes to USD 1900. In this case the freight

order has an invoicing status of Not Up-to-Date.

This is custom documentation. For more information, please visit SAP Help Portal.

171


1/14/26, 2:42 PM

## Increase in Rate for the Base Freight

Your purchasing department communicates that the carrier has increased rate for freight. Because of this, there's an

upward revision of the overall freight charges for the freight order of USD 50. You change the basic freight charge to reflect

this increment. The freight order changes to USD 2050. In this case, if the setting Settlement Change Process: Reverse

and Repost in Customizing activity for Transportation Management under  Basic Functions

 General Settings

## General

Settings for TM  is enabled the system sets the invoicing status of the freight order as Not Up-to-Date. If the setting is

disabled, the invoicing status is set to Partially Invoiced.

You can select the following change process strategies:

Create New FSD for Delta Amount

Lifecycle Status

System Action

## Example

New/In Process/Ready for Posting

If the invoicing status of the freight order

## Additional Detention Charge

is Partially Invoiced, create a new freight

settlement document for the remaining

amount.

The system creates a new freight

settlement document for the remaining

amount of USD 300.

Additional Discount due to Better

## Volume

The system cancels the freight

settlement document for USD 2000 for

the freight order. The system creates a

new freight settlement document for the

revised value of the freight order of USD

1800.

Change in Rate for the Base Freight

The system cancels the freight

settlement document for USD 2000 for

the freight order. The system creates a

new freight settlement document for the

revised value of the freight order of USD

1900.

Accruals Posted/Invoice Verified

If the invoicing status of the

Example for Partially Invoiced

freight order is Partially Invoiced,

## Scenario

create a new freight settlement

document for the remaining

amount.

If the invoicing status of the

freight order is Over Invoiced, to

reverse the amount, the system

creates a credit memo for the

freight order with reference to

the freight settlement document

or freight settlement document

item in the case of a collective

freight settlement document. You

then create a new freight

settlement document for the full

value of the freight order

charges.

Additional Detention Charge

The system creates a new freight

settlement document for the

remaining amount of USD 300.

On posting the freight settlement

document to Material

Management (MM), the system

creates a new purchase order

and a service entry sheet (SES)

amount for USD 300.

Example for Over-Invoiced

## Scenario

Additional Discount due to

## Better Volume

This is custom documentation. For more information, please visit SAP Help Portal.

172


1/14/26, 2:42 PM

Lifecycle Status

System Action

## Example

For an airfreight booking, if a

The system creates a credit

charge correction advice

memo for USD 2000 with

document (CCAD) already exists

reference to the freight

for the freight booking, the

settlement document. If the

system creates a CCAD.

settlement for this order is by a

collective settlement document,

the system refers to the freight

settlement document item.

This reverses the amount in the

existing freight settlement

document or freight settlement

document item. On posting this

credit memo to MM, the system

reverses the posting of USD

2000.

The system creates a new freight

settlement document for USD

1800. On posting the new freight

settlement document to MM, the

system creates a new posting for

USD 1800

Change in Rate for the Base

## Freight

The system creates a credit

memo for USD 2000 with

reference to the freight

settlement document. If the

settlement for this order is by a

collective settlement document,

the system refers to the freight

settlement document item.

This reverses the amount in the

existing freight settlement

document or freight settlement

document item. On posting this

credit memo to MM, the system

reverses the posting of USD

2000.

TM creates a new freight

settlement document for USD

1900. On posting the new freight

settlement document to MM, the

system creates a new posting for

USD 1900.

Air Freight Scenarios Where a

## CCAD Already Exists

Example for a Partially Invoiced

## Scenario

## Additional Detention Charge

This is custom documentation. For more information, please visit SAP Help Portal.

173


1/14/26, 2:42 PM

Lifecycle Status

System Action

## Example

The system creates a new CCAD

for the remaining amount of USD

300. On posting the CCAD, the

system reverses the posting of

USD 2000 and creates a new

posting for USD 2300.

Example for Over-Invoiced

## Scenario

Additional Discount due to

Better Volume.

The system creates a new CCAD

for the remaining amount of USD

-200. On posting the CCAD, the

system reverses the posting of

USD 2000 and creates a new

posting for USD 1800.

Change in Rate for the Base

## Freight

The system creates a new CCAD

for the remaining amount of USD

-100. On posting the CCAD, the

system reverses the posting of

USD 2000 and creates a new

posting for USD 1900.

## Canceled/Reversed

Create a new freight settlement

Additional Detention Charge

document with the updated amount.

The system creates a new freight

settlement document for the revised

value of the freight order of USD 2300.

Additional Discount due to Better

## Volume

The system creates a new freight

settlement document for the revised

value of the freight order of USD 1800.

Change in Rate for the Base Freight

The system creates a new freight

settlement document for the revised

value of the freight order of USD 1900.

Reverse and Repost with New FSD

Lifecycle Status

System Action

## Example

New/In Process/Ready for Accruals

Cancel the freight settlement document

Additional Detention Charge

or freight settlement document item and

create a new freight settlement

document.

The system cancels the freight

settlement document for USD 2000 for

the freight order. It creates a new freight

settlement document for the remaining

amount of USD 2,300.

This is custom documentation. For more information, please visit SAP Help Portal.

174


1/14/26, 2:42 PM

Lifecycle Status

System Action

## Example

Additional Discount due to Better

## Volume

The system cancels the freight

settlement document for USD 2000 for

the freight order. It creates a new freight

settlement document for the revised

value of the freight order of USD 1800.

Change in Rate for the Base Freight

The system cancels the freight

settlement document for USD 2000 for

the freight order. It creates a new freight

settlement document for the revised

value of the freight order of USD 1900.

Accruals Posted/Invoice Verified

Regardless of whether the invoicing

Additional Detention Charge

status of the freight order is Partially

Invoiced, Over Invoiced, or Not Up-to-

Date to reverse the amount the system

creates a credit memo for the freight

order with reference to the freight

settlement document or freight

settlement document item in case of a

collective freight settlement document. It

then creates a new freight settlement

document for the full value of the freight

order charges.

In the case of an air freight booking, if a

CCAD already exists for the freight

booking, the system creates a CCAD.

The system creates a credit memo for

USD 2000 with reference to the freight

settlement document. If the settlement

for this order is by a collective settlement

document, the system refers to the

freight settlement document item.

This reverses the amount in the existing

freight settlement document or freight

settlement document item. On posting

this credit memo to MM, the system

reverses the posting of USD 2000.

TM creates a new freight settlement

document for USD 2300. On posting the

new freight settlement document to MM,

the system creates a new posting for

USD 2300.

Additional Discount due to Better

## Volume

The system creates a credit memo for

USD 2000 with reference to the freight

settlement document. If the settlement

for this order is by a collective settlement

document, the system refers to the

freight settlement document item.

This reverses the amount in the existing

freight settlement document or freight

settlement document item. On posting

this credit memo to MM, the system

reverses the posting of USD 2000.

The system creates a new freight

settlement document for USD 1800. On

posting the new freight settlement

document to MM, the system creates a

new posting for USD 1800.

This is custom documentation. For more information, please visit SAP Help Portal.

175


1/14/26, 2:42 PM

Lifecycle Status

System Action

## Example

Change in Rate for the Base Freight

The system creates a credit memo for

USD 2000 with reference to the freight

settlement document. If the settlement

for this order is by a collective settlement

document, the system refers to the

freight settlement document item.

This reverses the amount in the existing

freight settlement document or freight

settlement document item. On posting

this credit memo to MM, the system

reverses the posting of USD 2000.

The system creates a new freight

settlement document for USD 1900. On

posting the new freight settlement

document to MM, the system creates a

new posting for USD 1900

Air Freight Scenario when a CCAD

## Exists

Additional Detention Charge

The system creates a new CCAD for the

remaining amount of USD 300. On

posting the CCAD, the system would

have reversed the posting of USD 2000

and created a new posting for USD 2300.

Additional Discount due to Better

## Volume

The system creates a new CCAD for the

remaining amount of USD -200. On

posting the CCAD, the system would

have reversed the posting of USD 2000

and created a new posting for USD 1800.

Change in Rate for the Base Freight

The system creates a new CCAD for the

remaining amount of USD -100. On

posting the CCAD, the system would

have reversed the posting of USD 2000

and created a new posting for USD 1900.

## Canceled/Reversed

Create a new freight settlement

Additional Detention Charge

document with the updated amount.

The system creates a new freight

settlement document for the revised

amount of USD 2,300.

Additional Discount due to Better

## Volume

The system creates a new freight

settlement document for the revised

value of the freight order of USD 1800.

This is custom documentation. For more information, please visit SAP Help Portal.

176


1/14/26, 2:42 PM

Lifecycle Status

System Action

## Example

Change in Rate for the Base Freight

The system creates a new freight

settlement document for the revised

value of the freight order of USD 1900.

  Note

You can run the Creation of Freight Settlement Documents background function to automatically make changes in

freight settlement documents. For more information, see Creation and Transfer of Freight Settlement Documents.

You can create a freight settlement document either in the personal worklist or in the individual freight order.

Regardless of the change process strategy, if the invoicing status of a freight order is Not Up-to-Date, the system

automatically tries to apply the change process strategy of Reverse and Repost with New FSD.

The system doesn't automatically execute the change process and reports an error when you change a freight order

after you begin the freight settlement process, and the freight order has an existing credit memo that isn't enabled to

influence the invoicing status.

You must make a manual change in the settlement process. You can change or cancel the relevant credit memo and

create the freight settlement document again.

Irrespective of the change process strategy, if a freight settlement document has a lifecycle status of Posting Started,

Cancellation Requested or Reversal Started and you run the function Create and Transfer Freight Settlement

Documents, the system reports an error.

You must wait until posting is complete and the system updates the lifecycle status in TM to either Accruals Posted or

In Process before you take further action. If the system updates the status to In Process, errors have occurred during

the posting of the settlement documents.

## Charge Correction Advice Document

In an air freight scenario, you can create a CCAD to recover an overpaid amount from your carrier or pay an underpaid amount to

your carrier.

You can only manually create a CCAD for air freight orders.

A CCAD contains the amount that has already been settled, the new negative amount to be corrected, and the final correct

settlement amount for the freight order.

When posting the CCAD to MM, the system takes the following steps:

Posts an SES return to reverse the amount you previously posted from TM

Posts an SES with the revised freight order charge

More Information

## Subject

## More Information

Change management process for forwarding settlements

Automatic Change Management for Forwarding Settlements

## Working with a dispute case

## Dispute Management for Freight Settlements

This is custom documentation. For more information, please visit SAP Help Portal.

177


1/14/26, 2:42 PM

## Subject

## More Information

Charge correction advice management process

## Charge Correction Advice Management

Controlled Change Process for Freight and Forwarding Settlements Controlled Change Process for Freight and Forwarding Settlements

Controlled Change Process for Freight and Forwarding
## Settlements

When you change any settled charge lines, the system updates the invoicing status of settled freight orders, freight bookings,

service orders, or forwarding orders to reflect the change. After the invoicing status is set, the system uses the change process

strategy that you've defined in the Customizing activity for Transportation Management under  Settlement

## Define Settlement

Profile  to process the change process for posting.

Depending on whether you've enabled or disabled the setting Settlement Change Process: Reverse and Repost in Customizing

for Transportation Management under  Basic Functions

## General Settings

 General Settings for TM  the invoicing status of a

freight order, freight booking, service order, or forwarding order is set as follows:

## Scenario

Invoicing Status with settings disabled

Invoicing Status with settings enabled

Reduction or deletion of a settled charge or

Not Up-To-Date

## Not Up-To-Date

deactivating a charge line

Increment of a settled charge line

Partially Invoiced

## Not Up-To-Date

Addition of new charge line or activating an

Partially Invoiced

Partially Invoiced

inactive charge line

Changes in business partner or agreement

Not Up-To-Date

Not Up-To-Date

## Related Information

Automatic Change Management for Freight Settlements

Tax Determination

## Use

Transportation Management (TM) enables information to be transferred to Materials Management (MM) and Sales and

Distribution (SD), where it can be used to determine tax when settlement documents are posted. Taxes for forwarding settlement

documents are calculated using the Sales and Distribution (SD) component, but taxes for freight settlement documents are

determined using the Materials Management (MM) component.

You can set up the pricing procedures in the respective modules to establish rules based on your business requirements. TM can

change the way in which tax is determined by transferring influencing factors or determinants to the SD and MM modules. For

example, you post a settlement document for a freight order or freight booking to MM, or a forwarding order to SD. When you do

so, the system also transfers the location country/region details from the order. The location country/region details are used to

populate the country/region fields in the pricing communication structures. The communication structures are used when taxes

are calculated during the pricing procedure in SD and MM.

This is custom documentation. For more information, please visit SAP Help Portal.

178


1/14/26, 2:42 PM

## Integration

The following tables contain a summary of the fields that are populated in the pricing communication structure, which can be used

to determine the tax code.

Communication Structure

Field in TM

## Comment

Forwarding Settlement Integration

KOMK-LAND1

Country/Region of the

Country/region of the customer being billed

Customer

## KOMK-ALAND

Country/Region of the Sales

Country/region of the sales organization

## Org

## KOMK-SLAND1_A

## Source Country/Region

FWO – Source country/region, stage source country/region, or item

source country/region

## KOMK-SLAND1_Z

## Destination Country/Region

FWO – Destination country/region, stage destination

country/region, or item destination country/region

KOMK-TAXK1 to TAXK9

## BP Tax Group

Mapping of the tax group to the classification in SD from the tax

data of the business partner

KOMP-TAXM1 to TAXM9

## Charge Type Tax Group

Mapping of the tax group to the classification in SD from the charge

type level that is set up in TM

Freight Settlement Integration

Communication Structure

Field in TM

Comment

KOMK-LAND1

## None

Country/region of plant in MM-PO or country/region of company

code when the plant is determined during the creation of the

purchase order

## KOMK-ALAND

Country/Region of the Carrier

Country/region of the carrier

## KOMK-SLAND1_A

## Source Country/Region

FO – Source country/region, stage source country/region, or item

source country/region

This is custom documentation. For more information, please visit SAP Help Portal.

179


1/14/26, 2:42 PM

Communication Structure

Field in TM

## Comment

## KOMK-SLAND1_Z

## Destination Country/Region

FO – Destination country/region, stage destination country/region,

or item destination country/region

## KOMP-TAXIM

## Material Tax Indicator

Assignment of the tax indicator to the charge type level

## Prerequisites

Transportation Management

For Freight Settlement:

You've specified whether the tax is calculated at charge type level for countries/regions.

For TM embedded in SAP S/4HANA, you specify this in the Customizing activity Define Tax at Charge Type Level in

Customizing for Transportation Management under  Settlement

 Freight Settlement

 Integration for

Settlement Posting

 Tax .

For integration with an external SAP S/4 HANA ERP system, you specify this in the Customizing under

## Integration

with other SAP Components

 Transportation Management

 Invoice Integration

## Invoicing

## Tax Setting for TM

in SAP S/4HANA  in the SAP S/4 HANA ERP system.

You've specified the tax indicators for the charge types for countries/regions.

For TM embedded in SAP S/4HANA, you specify this in the Customizing activity Assign Tax Indicators for Charges

in Customizing for Transportation Management under  Settlement

 Freight Settlement

 Integration for

Settlement Posting

 Tax .

For integration with an external SAP S/4 HANA ERP system, you specify this in the Customizing under

## Integration

with other SAP Components

 Transportation Management

 Invoice Integration

## Invoicing

## Tax Setting for TM

in SAP S/4HANA  in the SAP S/4 HANA ERP system.

  Note
During freight settlement posting, the system prioritizes the Customizing settings in the TM for SAP S/4HANA system even

though you've specified the Customizing settings in the SAP ERP system.

For Forwarding Settlement:

You've specified whether the tax is calculated at charge type level for countries/regions in the Customizing activity Define

Tax at Charge Type Level under  Transportation Management

## Settlement

 Forwarding Settlement

 Tax .

You've specified the tax indicators for the charge types for countries/regions in the Customizing activity Assign Tax

Indicators for Charges under  Transportation Management

## Settlement

 Forwarding Settlement

 Tax .

## Features

On a country/region-specific basis, you can specify the tax influencers, such as the tax indicator and tax classification for the

charge-type level, charge category level, or subcategory level. You can also specify whether tax is to be applied at charge level.

These settings are transferred to pricing procedures in SD and MM, and is used when the forwarding settlement document or

freight settlement document is posted.

## More Information

This is custom documentation. For more information, please visit SAP Help Portal.

180


1/14/26, 2:42 PM

Forwarding Settlement

Freight Settlement

## Credit Memos

Split Criteria in Settlement Document Creation

## Use

When you create a collective forwarding settlement document or freight settlement document, the system attempts to combine

the settlement for the forwarding orders or freight documents you have selected into a single forwarding settlement document or

freight settlement document.

However, the split criteria arise when particular conditions are different between the orders the system is trying to combine. As a

result, the system creates multiple settlement documents.

The system makes a split in no particular order of priority.

## Features

## Split Criteria for Forwarding Settlement Documents

The system uses the following split criteria when it attempts to create a collective forwarding settlement document:

Sales organization

Bill-to party

## Payer

Sold-to party

Payment term

Credit segment

Document currency

## Calculation level

Stage, if you specify the Stage Split setting in the Define Settlement Profile Customizing activity. For more information,

see Customizing for Transportation Management under  Settlement

.

Settlement group, where you group the charge types that you want to settle at the same time in your process. For more

information, see Flexible Creation of Forwarding Settlements.

## Split Criteria for Freight Settlement Documents

The system uses the following split criteria when it attempts to create a collective freight settlement document:

Procuring company code

## Purchasing organization

## Carrier or additional agreement party

This is custom documentation. For more information, please visit SAP Help Portal.

181


1/14/26, 2:42 PM

Invoicing party

## Payee

Payment term

Document currency

## Calculation level

Stage, if you specify the Stage Split setting in the Define Settlement Profile Customizing activity.

## Example

## Forwarding Settlement

You have two forwarding orders that you want to combine into one forwarding settlement document.

FWO

Sales Organization

Sold-to Party / Bill-to

Payment Terms

Freight Cost (USD)

9100021

9100291

0001

0001

## Party / Payer

Delicious chocolates

0001 – Due immediately

200

Delicious chocolates

0002 – Net due in 15

300

days

You select the orders and select the combine option to create the collective settlement documents on the worklists screen.

However, as the payment term in the order does not match, the system creates two forwarding settlement documents.

## FWSD

Forwarding Order

Sales Organization

Sold-to Party / Bill-

Terms of Payment

Freight Cost (USD)

to Party / Payer

9700021

9100021

0001

Delicious chocolates 0001 – Due

200

immediately

9700022

9100291

0001

Delicious chocolates 0002 – Net due in

300

15 days

## Freight Settlement

You have three freight orders that you want to combine into one freight settlement document.

Freight Order

Procuring Company

## Purchasing

Carrier / Invoicing

Payment Terms

Freight Cost (USD)

8100021

Code

0001

0001

Organization

Party / Payee

8100229

0001

0001

8100291

0002

0002

Fast Trucking

## Company

Fast Trucking

## Company

Fast Trucking

Company

0001 – Due

immediately

0001 – Due

immediately

0001 – Due

immediately

200

240

300

You select the orders and select the combine option to create the collective settlement documents on the worklists screen.

However, as the company code and purchasing organization in the order do not match, the system creates two freight settlement

documents.

This is custom documentation. For more information, please visit SAP Help Portal.

182


1/14/26, 2:42 PM

Freight

Settlement

## Document

Freight Order

Procuring

Purchasing

Carrier /

Terms of

Freight Cost

Company Code

Organization

Invoicing Party /

Payment

Payee

900021

8100021

0001

0001

Fast Trucking

0001 – Due

440

8100229

## Company

immediately

900022

8100291

0002

0002

Fast Trucking

0001 – Due

300

## Company

immediately

## Related Information

Freight Settlement Integration using MM External Services Management

## Forwarding Settlement

This is custom documentation. For more information, please visit SAP Help Portal.

183
