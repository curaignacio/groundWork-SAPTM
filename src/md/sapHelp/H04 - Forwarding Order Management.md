1/14/26, 2:17 PM

Transportation Management (TM)

Generated on: 2026-01-14 14:17:02 GMT+0000

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

Forwarding Order Management

## Use

You can use the Forwarding Order Management component in Transportation Management (TM) to create, edit, and confirm

forwarding orders from your ordering parties. You can also already specify the route and have the transportation charges

calculated here. The orders then form the basis for transportation planning.

In addition to creating the forwarding order, you can also enter the data as a forwarding quotation and send it to the ordering party.

You can then create a forwarding order based on the forwarding quotation.

Note that the following function is not currently released:

Integration of the forwarding order and the FWSD in TM with Credit Management in SAP S/4HANA

## Integration

The TM component Forwarding Order Management is integrated with the following other TM components:

## Component

Integration Type

## Freight Order Management

You can create freight orders and freight bookings from forwarding

orders.

## Planning

Forwarding orders form the basis for planning and executing the

transportation.

## Forwarding Settlement

Based on the forwarding order, you can create a forwarding

settlement to trigger the invoice creation process.

## Master Data

As a prerequisite for creating forwarding orders, the necessary

master data must have been created.

Forwarding Order Management is also integrated with the dangerous goods management and global trade processes. For more

information, see Considering Dangerous Goods and Global Trade.

## Features

You can use the business documents from Forwarding Order Management to enter all the information required for planning and

executing the transportation of goods, such as pick-up and delivery addresses, dates/times, and goods to be transported. You can

enter the data manually or transfer it automatically via PI interfaces.

After you have edited the data, you can send a confirmation to your ordering party. Moreover, you can trigger transportation

planning from the forwarding orders and generate the following objects, for example, to further plan and execute the

transportation:

Freight Units

Freight Orders

## More Information

This is custom documentation. For more information, please visit SAP Help Portal.

2


1/14/26, 2:17 PM

## Creation of a Forwarding Order

Creation and Editing of a Forwarding Quotation

Forwarding Order

## Definition

An order from an ordering party to a carrier or logistics service provider with respect to the transportation of goods from a shipper

to a consignee according to the agreed-upon conditions.

## Use

You can use the forwarding order business document in Transportation Management (TM) to enter data for the transportation of

goods that you have agreed upon with an ordering party. You can enter the data manually (for example, after a telephone call) or

you can transfer it automatically (via PI interfaces, EDI). The forwarding order is the basis for further transportation planning. It

contains the most important data for planning and executing the transportation, such as the pick-up and delivery address,

dates/times, and the goods that are to be transported. From the forwarding order, you can determine and define the

transportation route, and create freight units and a transportation plan. You can also have the system calculate the transportation

charges and start the invoicing.

## Structure

The design of the user interface for the forwarding order is determined by the following factors:

Transportation mode (air, sea, or land)

Forwarding order type that you define in Customizing (see Settings for the Forwarding Order)

## Individual screen settings in the apps for forwarding orders from the launchpad

On the initial screen of the forwarding order, you can specify the forwarding order type and the transportation mode (if you have

not already predefined this in the forwarding order type). The user interface for the forwarding order is automatically adjusted to

the requirements of the transportation-mode-specific business processes. The forwarding order type also predefines which

additional information or special tab pages are displayed for each business process (such as displaying dangerous goods

information for the order items).

You can also configure your settings in the apps to define whether a tab page, assignment block, or specific fields in the forwarding

order are displayed or hidden. The forwarding order generally has the following basic structure:

## Areas for general data, business partners, locations, and dates/times

In these areas of the forwarding order, you enter data (or the system displays data) that is valid for all items in the order.

This data includes, for example, the sales organization, Incoterms, and service level. In addition, the totaled quantity data

and weight data for the order items is displayed.

Furthermore, you can specify attributes for process control, such as the transportation mode and shipping type.

For more information, see Creation of a Forwarding Order and Attributes for Process Control.

## Ordered route and actual route

In these assignment blocks or on the tab pages, you can enter the route requested by the ordering party and the actual

route with the individual transportation stages. For more information, see Determination of the Route.

This is custom documentation. For more information, please visit SAP Help Portal.

3


1/14/26, 2:17 PM

## List of order items

In this table, you enter the item-specific data in the form of an item hierarchy. For more information, see Creation of

Forwarding Order Items or Forwarding Quotation Items.

## Document flow

The system displays here which business documents have been entered into the forwarding order and which business

documents were created based on it. You can also display the follow-on documents from here, and call a freight unit, for

example.

## Output management

Here the system displays which documents were already printed or sent (by e-mail or fax, for example) for this forwarding

order. Moreover, you can print documents such as bills of lading from here. For more information, see Output Management.

## Status

Here the system displays the different statuses of the document, such as the life cycle status and the blocking status. For

more information, see Status of a Forwarding Order.

## HBL or HAWB

You can display data for house bills of lading (HBLs) or house air waybills (HAWBs) in this assignment block or on the tab. In

addition, you can make individual allocations of waybill numbers to freight units or remove the allocations again. For more

information, see Building and Printing of House Bills of Lading and House Air Waybills.

## Profitability

You can display a profitability analysis in this assignment block or on the tab page. From here, you can also navigate to the

individual business documents. For more information, see Profitability Analysis.

## Specialist, process-dependent tab pages

In addition to those described above, the system also displays additional tab pages or assignment blocks if you have

activated the corresponding business process in the document type, such as:

## Charge calculation and internal charge calculation

The system displays the data from an (internal) transportation charge calculation that you have made for the

forwarding order. Moreover, you can enter the transportation charges manually as well. For more information, see

Charge Calculation.

## Air cargo security

You can enter the data required if you want to perform an air cargo security check. For more information, see Air

Cargo Security.

## Instructions

If you have defined instructions for executing services in Customizing (such as an instruction for cleaning a

container), the system displays these here. You can also change or delete instructions or create new instructions on

this tab page. For more information, see Management of Instructions.

## Change documents

If you have activated change tracking in Customizing, the system displays any changes to your documents here. For

more information, see Change Tracking.

When you create air forwarding orders, you can enter the nature of goods on the Nature of Goods tab page. You can enter

the nature and quantity of goods, which is printed on air waybills, and the nature of goods for manifest, which is printed on

the security manifest and cargo manifests. For more information, see Nature of Goods.

This is custom documentation. For more information, please visit SAP Help Portal.

4


1/14/26, 2:17 PM

In addition to the comprehensive view of the forwarding order user interface, you can also use the Page function to access a view

for fast order entry. This view contains all input fields that are required to complete a forwarding order on a single screen (without

tab pages). You can also enter values more quickly by using the keyboard (with the exception of the list of order items).

## Integration

The business document for the forwarding order is integrated with further business documents in TM, such as the following:

## Forwarding Quotation

If you have sent a forwarding quotation to an ordering party and it was accepted by the ordering party, you can create a

forwarding order based on this forwarding quotation.

## Freight Unit

You can create freight units for this forwarding order from the order.

## Forwarding Settlement Document

You can create a forwarding settlement document for this forwarding order from the order.

## More Information

Creation of a Forwarding Order

Editing of a Forwarding Order

## Status of a Forwarding Order

The following document describes important statuses of a forwarding order, which are mainly displayed on the Status tab page.

Life Cycle Status

Status

## New

## Description

A new forwarding order was created, and no freight units or transportation units have been created for this

order yet.

## In Planning

The forwarding order is in the planning process, and at least one freight unit or transportation unit has been

created for the order.

## Planned

The forwarding order is in the planning process. All freight units and transportation units assigned to it have

been planned.

## In Execution

The forwarding order is in the execution process. At least one follow-on document (not necessarily a freight

unit or a transportation unit) is in execution. For more information about the execution of a forwarding order,

see the execution status of the forwarding order or of the follow-on documents.

## Executed

Execution of the forwarding order has been completed. Execution of all planning documents assigned to the

forwarding order has been completed.

## Partially Invoiced

The forwarding order is in the invoicing process. One or more forwarding settlement documents were created,

but the invoicing has not been carried out completely yet.

## Completed

Processing of the forwarding order has been completed. Execution has finished, the invoicing has taken place,

and existing instructions have been completed (if this was specified in the Customizing settings for the

forwarding order type). The status is also set by the system if the forwarding order was created only for

This is custom documentation. For more information, please visit SAP Help Portal.

5


1/14/26, 2:17 PM

## Status

## Description

settlement purposes (for example, as a service order) and the settlement documents were created in their

entirety.

## Determination Pending

This status is set temporarily by the system if the forwarding order was reopened after it had been assigned

the status Complete. If you make changes to the forwarding order and save it again, the status also changes

again (for example, back to In Execution, Partially Invoiced, or Completed depending on the type of change).

## Canceled

The forwarding order was canceled.

## Draft

The system sets this status if an import forwarding order is created or updated. You can change the sales

organization but the forwarding order is locked for all other changes.

Planning Status

## Status

## Description

## Planning Not Started

The planning process has not yet been started for the forwarding order.

## In Planning

The forwarding order is in the planning process. At least one freight unit or transportation unit has been

created for the forwarding order; however, a freight document has not yet been assigned.

## Partially Planned

The forwarding order is in the planning process. At least one freight unit (FU) or transportation unit (TU) has

been created for the forwarding order. Moreover, at least one freight document has been assigned to the

forwarding order; however, not all FU or TU stages have been planned yet.

## Planned

The forwarding order is in the planning process. All freight units and transportation units assigned to it have

been planned.

Execution Status

## Status

## Description

## Execution Not Started

Execution of the forwarding order has not yet been started.

## In Execution

The forwarding order is currently being executed. At least one of the planning documents linked to the

forwarding order is in the execution process.

## Executed

Execution of the forwarding order has been completed. Execution of all planning documents assigned to the

forwarding order has been completed.

Confirmation Status

## Status

Description

## Not Confirmed

No forwarding order confirmation has been created yet, or an existing confirmation was reset because data in

the forwarding order has changed.

## Confirmed

A forwarding order confirmation has been created.

## Approval Status

This status is only displayed if you have activated the approval workflow.

This is custom documentation. For more information, please visit SAP Help Portal.

6


1/14/26, 2:17 PM

## Status

Description

## Not Checked

The approval limits were not yet checked for this forwarding order.

## No Approval Required

The approval check was conducted for this forwarding order. The defined limits were not exceeded.

## Approval Required

The approval check was conducted for this forwarding order, and the defined limits were exceeded. The

forwarding order was blocked for further processing.

## Approved

The approval workflow was executed, and the forwarding order was approved by the person responsible. The

block of the forwarding order for further processing was removed.

## Not Approved

The approval workflow was executed, and the forwarding order was not approved by the person responsible.

The forwarding order remains blocked for further processing.

## Delivery Status

The status shows at header level of the forwarding order whether the freight units and transportation units assigned to the

forwarding order were actually delivered. This data originates from the associated freight document. In addition to this status at

header level, there is an additional status at order item level that specifies whether the freight units and transportation units for

the order item were delivered (cargo receipt status).

## Status

Description

## Delivered

All freight units and transportation units that are assigned to the forwarding order have been delivered.

## Partially Delivered

At least one but not all freight units and transportation units in the forwarding order requests were delivered.

## Not Delivered

None of the freight units or transportation units in the forwarding order requests were delivered.

## FWQ Assignment Status

This status indicates whether the forwarding order was created on the basis of a forwarding quotation or whether a forwarding

quotation was assigned to it subsequently. For more information, see Subsequent Assignment of Forwarding Quotations.

## Organization Interaction Status

This shows the status of the interaction between organizational units, for example, between a sales organization and a planning

and execution organization. It is available for a stage of the route and also as an aggregated status.

For more information, see Interaction Between Organizational Units.

## HBL or HAWB Status

This status is displayed on the General Data and HBL or HAWB tabs of a forwarding order. It supports, for example,

communication between a customer service agent and a capacity manager at the gateway. The status shows you whether the

house bills of lading (HBLs) or house air waybills (HAWBs) assigned to the forwarding order have been completed by the customer

service agent (Finalized) and are available for subsequent processes.

You can set the status manually for the forwarding order using a menu option and reset it to Not Finalized. If the HBL or HAWB

number has not been assigned, this is done automatically by setting the status.

If you set the status for a forwarding order with the forwarding order type Direct Shipment, it is set for both the HAWB and the

master air waybill (MAWB).

This is custom documentation. For more information, please visit SAP Help Portal.

7


1/14/26, 2:17 PM

## Status

Description

## Finalized

All house air waybills in the forwarding order have been completed.

## Partially Finalized

At least one but not all house air waybills in the forwarding order requests were completed.

## Not Finalized

No house air waybill in the forwarding order has been completed.

## Status for Air Cargo Security and Compliance with Foreign Trade Regulations

This status is displayed on the Status tab if you have activated the corresponding processes in Customizing for the forwarding

order type. For more information, see Settings for the Forwarding Order, Air Cargo Security, and Trade Compliance Check.

## Blocking the Forwarding Order

In addition to the forwarding order statuses described above, the system also displays the block status for this order on the Status

tab page. You can also set blocks manually. For more information, see Blocking Information of a Forwarding Order.

Blocking Information of a Forwarding Order

## Use

You can set blocks manually or have the system set blocks automatically for the following functions and processes in the

forwarding order:

Planning of the forwarding order, in other words, creation of freight units and transportation units, and creation of freight

orders

Execution of the forwarding order and associated planning documents

Confirmation of the forwarding order

## Creation of the forwarding settlement document

In Customizing you can specify the successor documents to which the blocks are copied. For more information, see Blocking

Information of Freight Units and Capacity Documents.

## Prerequisites

You have defined block reasons in Customizing. For more information, see Customizing for Transportation Management under

Basic FunctionsGeneral SettingsDefine Block Reason Codes.

## Features

You can display planning, execution, confirmation, and settlement blocks on the Status tab page in a forwarding order.

Furthermore, you can set or remove blocks manually:

## Manual setting of blocks

When you set a block manually, you can select a block reason from the values defined in Customizing. You can also set, for

example, multiple planning or execution blocks and choose different block reasons. All the block reasons are displayed both

in the aggregated view of the blocks next to the block status and in the successor documents.

This is custom documentation. For more information, please visit SAP Help Portal.

8


1/14/26, 2:17 PM

## Automatic setting of blocks

Blocks are set by the system, for example, if the forwarding order does not yet contain all the required information and is

therefore incomplete for planning. In the block details you can get information about which fields have still to be filled.

When you choose Check to check the completeness of the forwarding order, the system also checks the block status and

displays the same detailed messages.

You can use a Business Add-In (BAdI) to change the standard logic for checking the completeness of a forwarding order.

This means that you can, for example, specify that certain fields do not have to be filled in contrast to the standard system

(such as the movement type). Moreover, you can include additional fields in the check. For more information, see

Customizing for Transportation Management under  Business Add-Ins (BAdIs) for Transportation Management

 Forwarding Order Management

## Forwarding Order Management

 BAdI: Enhancements of FWO Completeness Checks

.

The system sets further automatic blocks when it executes the approval workflow or during the dangerous goods check, for

example.

## Removal of blocks

When you remove a block, you can enter a comment. The system also logs and displays who removed the block and when.

Note that you require the authorization to remove blocks. For more information, see Authorizations.

You cannot create a forwarding settlement document if the settlement block is set.

  Note
Note that changes to a business partner block are not always immediately visible in the forwarding order. If you have opened a

forwarding order and have in the meantime made changes to the business partner's master data, you do not see these changes

immediately. You first have to close the forwarding order and open it again. It is not sufficient to update the screen data.

## Settings for the Forwarding Order

The following describes the general settings that you can or must make for a forwarding order. Specific settings for individual

functions or processes can be found in the individual chapters.

## Profiles

You have created the following profiles in Customizing. Creating these profiles is optional, but you do need them for important

follow-up actions such as planning or printing:

## Planning profile

You use the planning profile to determine how transportation planning proceeds further, which you can trigger from the

forwarding order, or on what basis the system determines the routes. For more information, see Planning Profile.

## Output profile

You can use the output profile to determine which outputs are possible for the forwarding order (print documents and EDI

messages). Standard profiles are available, but you can also define your own profile.

For more information, see Customizing for Cross-Application Components under  Processes and Tools for Enterprise

## Applications

 Reusable Objects and Functions for BOPF Environment

 PPF Adapter for Output Management

 as well

as Output Management.

## Dangerous goods profile

This is custom documentation. For more information, please visit SAP Help Portal.

9


1/14/26, 2:17 PM

If you transport dangerous goods with the forwarding order, you can use the dangerous goods profile to make settings for

the processing of the dangerous goods items, such as for the output of error messages.

For more information, see Customizing for Transportation Management under  Basic Functions

## Dangerous Goods

 Define Dangerous Goods Profile  as well as under Considering Dangerous Goods.

## Partner Determination Profile

You can use this profile to indicate that the system is to assign business partners to your forwarding order automatically.

For more information, see Customizing for Transportation Management under  Master Data

 Business Partner

## Define

Partner Determination Profiles  and under Business Partner Determination.

## Other Customizing Activities

You have defined the forwarding order type. You use this document type to determine a series of characteristics for the

forwarding order. In this way, you can assign the profiles described above and the freight unit building rule or condition to

the forwarding order type, and make certain default settings, such as the following:

Transportation mode (air, sea, land)

Define default shipping type, traffic direction and sales organization

Automatic confirmation of the forwarding order

## Automatic freight unit building

Activate an approval workflow and a credit limit check

Activation and deactivation of charge calculation and internal charge calculation

Activation and deactivation of forwarding settlement and internal settlement

## Automatic charge calculation and internal charge calculation

Define and activate process-specific parameters and functions, such as the air waybill type (AWB type) and air

cargo security check

## Activate change tracking

In addition, you use the forwarding order type to determine the appearance of the user interface. This means for instance

that the input fields and menu options are tailored to the transportation mode. The system only displays dangerous goods

information for the order items, for example, if you have assigned a dangerous goods profile to the forwarding order type.

For more information, see Customizing for Transportation Management under  Forwarding Order Management

## Forwarding Order

 Define Forwarding Order Types .

If required, you have extended the standard checks that the system executes to decide whether a freight unit or

transportation unit must be rebuilt during business document maintenance. For more information, see Customizing for

Transportation Management under  Business Add-Ins (BAdIs) for Transportation Management

 Forwarding Order

## Management

## Freight Unit Building

 BAdI: Extension of Checks for Triggering FU Building from TRQ .

You have defined a number range interval, within which the system creates the identifiers (IDs) of the forwarding orders of

a previously defined type. For more information, see Customizing for Transportation Management under  Forwarding

## Order Management

 Define Number Range Intervals for Forwarding Order Management

.

You have defined the transportation mode, such as sea, air, and road. For more information, see Customizing for

Transportation Management under  Master Data

 Transportation Network

 Transportation Lane

## Define

Transportation Mode .

This is custom documentation. For more information, please visit SAP Help Portal.

10


1/14/26, 2:17 PM

If you want to use Forwarding Order Management to support an air or sea freight-specific process, you have defined

transportation mode-specific codes, such as airline codes or standard carrier alpha codes (SCAC) in Customizing and

assigned them to your business partners as required. For more information, see Transportation-Mode-Specific Codes and

Business Partner.

You can specify that the transportation service levels available in a forwarding order are assigned to the same

transportation mode as that for the forwarding order, or are not assigned to any specific transportation mode. If you do not

make any setting here, the selection of service levels in the forwarding order is not restricted. For more information, see

Customizing for Transportation Management under  Forwarding Order Management

## Define Transportation Service

Level Codes  as well as Transportation Service Levels .

If you want to use your own shipping types, you have defined shipping types in Customizing and assigned them

transportation modes if required. You can then select these shipping types in Customizing for forwarding order types and

forwarding quotation types using the input help on the user interface for the forwarding order and forwarding quotation. For

more information, see Customizing for Transportation Management under  Forwarding Order Management

## Define

Shipping Types .

If you want to define reasons for blocking a forwarding order, you have defined block reasons in Customizing. For more

information, see Customizing for Transportation Management under  Basic Functions

 General Settings

 Define Block

Reason Codes .

## Master Data

You have defined the business partners and locations as well as data such as Incoterms or service level. For more

information, see Master Data.

If you want to have an approval workflow for your forwarding order, you have activated this workflow in Customizing for the

document type (see above) and have made the required settings for the workflow. For more information, see Approval

Check.

If you want to support a process for which a house bill of lading (HBL) or house air waybill (HAWB) is required, you have

assigned number ranges for house bills of lading or house air waybills to sales organizations and ordering parties in the

master data for Transportation Management. On the user interface of the forwarding order, you can then assign these HBL

or HAWB numbers to a forwarding order or assign a number from the corresponding number range.

If for particular scenarios you want to exclude being able to assign an HBL or HAWB number from a number range in the

forwarding order document, you can deactivate this function in Customizing for the forwarding order type.

For more information, see Waybill Stock Definition.

## Other Settings

You have optionally defined a freight unit building rule (FUB rule) and determined a condition for determining the FUB rule.

For more information, see Freight Unit Building Rule.

You have made the settings for defining stages of a route. For more information, see Determination of the Route.

You have made the settings for creating order items. For more information, see Creation of Forwarding Order Items or

Forwarding Quotation Items.

Creation of a Forwarding Order

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

11


1/14/26, 2:17 PM

In Transportation Management (TM), you can create forwarding orders (see Forwarding Order) both manually and automatically.

You can create a forwarding order in the following ways:

## On the basis of a quotation

You first create a forwarding quotation and use the data entered there to create a forwarding order.

You can also subsequently assign a forwarding quotation to a forwarding order. However, this is subject to certain

prerequisites such as corresponding data between the documents.

## On the basis of a template

A template can contain the most important default data, such as sales organization or Incoterms, and thus facilitates the

creation of new orders.

You can create a new template or create a template based on an existing forwarding order (from the forwarding order or on

the order management overview). The system copies the data in the forwarding order, such as document type and order

data, into the template (with the exception of dates/times and planning and execution data).

## As a copy of an existing forwarding order

If you select Copy in the forwarding order, the new order already contains a lot of the data that has been copied, including

data about the route. However, it does not contain any dates/times and no follow-on documents, such as freight units or

freight orders, are assigned to it. You can also copy the forwarding order without transferring the data about the actual

route. The life cycle status is New.

## From the order management overview

You create a new forwarding order without reference to another object.

Instead of creating the forwarding order fully, you can also first enter the order in a fast entry screen and save it there. This

screen provides an overview of the most important data. You can call up the screen again later on and add further data.

## From a forwarding agreement

You can create a forwarding order from a forwarding agreement or with reference to a forwarding agreement. A forwarding

agreement always consists of an ID and a version. If you create a forwarding order from a forwarding agreement item or

with reference to a forwarding agreement item, service items in the forwarding agreement can be transferred to the

forwarding order. In addition, further information from the forwarding agreement is automatically transferred to the

forwarding order, such as transportation mode, shipping type, and sales organization.

## Using PI interfaces

You receive the data directly from the ordering party by means of an SAP NetWeaver Process Integration (SAP NetWeaver

PI) interface.

Note that the enterprise services of forwarding order management are only released with restrictions. For more

information, see Released with Restrictions.

The following describes how you create a new forwarding order manually. For more information about creating forwarding

quotations and their conversion to forwarding orders, see Creation and Editing of a Forwarding Quotation.

## Prerequisites

You have made the settings required for the forwarding order. For more information, see Settings for the Forwarding Order.

## Process

1. Entering the Data on the Initial Screen

This is custom documentation. For more information, please visit SAP Help Portal.

12


1/14/26, 2:17 PM

On the initial screen of the forwarding order, you specify important data for the forwarding order, such as the forwarding

order type and the transportation mode. You can also specify whether you want to create the forwarding order with

reference to other documents, as a copy of other documents, or as a template. Note the following:

If you do not enter a forwarding order type, the system uses the default type defined in Customizing for forwarding

order types.

You cannot change the forwarding order type subsequently in the document itself. However, you can still change

some of the other parameters in the document, such as the sales organization. This depends on whether you have

predefined a value in Customizing that can still be changed.

If you have already defined the transportation mode in the forwarding order type, this is displayed and can no longer

be changed. If you specify a transportation mode first, the input help for the forwarding order type only allows you to

select order types that are valid for this transportation mode. If you have not defined the transportation mode in the

forwarding type, you can enter it manually, or you can leave it empty and enter it later.

If you copy an existing forwarding order, you can enter a new forwarding order type for the new forwarding order you

are creating. This can, however, lead to inconsistencies with copied data, if, for example, the copied data has been

determined from the Customizing settings for the forwarding order type (such as the transportation mode and the

shipping type). If the data for the new forwarding order type is unique, the system updates the data automatically.

Otherwise you have to change the inconsistent data manually.

You can enter a reference to a specific version of a forwarding agreement. If you also specify the forwarding

agreement item, the system automatically transfers service items that are flagged as flow services from the

forwarding agreement item to the forwarding order. For more information, see Creation of Forwarding Order Items or

Forwarding Quotation Items.

You can also specify an additional forwarding agreement, version, and item that are to be used for the corresponding

import or export business document. For example, if you create an export forwarding order, you can enter the

additional forwarding agreement that is to be referenced by the corresponding import forwarding order.

You can enter a default route on the initial screen. The system takes this route into account when it creates the

requested route. In addition, the system checks whether the data for the default route matches the other data that

you have entered on the initial screen, for example, the transportation mode or shipping type.

If you create a forwarding order based on an item from a forwarding agreement (FWA), you can select a default route

that has been defined for the FWA item.

The default route that you enter or select here is displayed in the general data area of the forwarding order. You can

still change it here. In this case, the system again checks whether the new default route corresponds to the data in

the forwarding order or to an assigned FWA item.

The forwarding order that has the life cycle status New then appears.

2. Entering the General Forwarding Order Data

You first create the general data for the forwarding order such as data for the sales organization, process control attributes

and Incoterm data. Note the following:

If you have defined this data in Customizing for the forwarding order type, the system has already automatically

determined the sales organization data.

If a transportation mode has not already been specified, you can enter it here. If you leave the transportation mode

empty, any fields that are dependent on the transportation mode (for example, shipping type, default route, and

service level) are then also empty, but can be entered manually. However, this may restrict the available

transportation modes. For example, if you enter the shipping type, you can then specify only the transportation

mode that is assigned to the shipping type in Customizing.

If you enter the transportation mode manually, you may be able to change it at a later stage of document

processing. However, this depends on several factors. For example, you cannot change the transportation mode if

This is custom documentation. For more information, please visit SAP Help Portal.

13


1/14/26, 2:17 PM

follow-on business documents exist for the freight units (FUs) or transportation units (TUs), and the execution of at

least one main carriage stage of one of these FUs or TUs has already started.

If you change a manually entered transportation mode from one category to another (for example, from sea to air),

the system clears the values in all fields that are not relevant for the new transportation mode and saves the

document automatically. It then loads the UI that corresponds to the new transportation mode. If, however, you have

defined a Web Dynpro application configuration in the FWO type, the system does not make any changes to the UI

when the mode is changed. The ordered route, actual route and any dependent freight documents are not changed

automatically. You must update them manually, if required.

In addition to the transportation mode, you can specify a series of attributes for process control, such as the

shipping type, movement type, and air waybill type. Depending on the Customizing settings, these attributes are

already automatically pre-defined. For more information, see Attributes for Process Control.

The payment terms are considered during planning and invoicing. Depending on your Customizing settings for the

forwarding order type, you can enter Incoterms or freight terms. If you do not enter any payment terms here, the

system determines the corresponding forwarding agreement based on the ordering party and it creates only one

forwarding settlement document for the ordering party.

Note that if you define party roles for payers in a forwarding order, the system then takes the payment terms of

these payers into account when it calculates charges instead of the payment terms of the agreement parties. The

system transfers the payment terms that were defined in forwarding orders to the subsequent processes. When it

calculates charges, the system does not take into account any changes to payment terms that were made in

settlement documents.

For more information, see Incoterms in Forwarding Orders and Freight Terms in Forwarding Orders.

If the carrier to whom the main carriage of the forwarding order is assigned performs invoicing directly with the

ordering party based on a special freight agreement, you must specify this in the forwarding order. For more

information, see Uncontrolled Transportation.

If you want to consolidate goods from different suppliers that are intended for one consignee before the main

carriage and load them in one container, you can specify that this is to be Buyer's Consolidation. You can also

consolidate goods that originate from a supplier and that are intended for several consignees (Shipper’s

Consolidation). For more information, see Buyer's Consolidation (BCO) in Export/Import and Shipper's

Consolidation (SCO) in Export/Import.

You can enter or change a reference to a forwarding agreement or additional forwarding agreement on the General

Data tab page in the Forwarding Agreement References screen area. Here, a link is provided to the relevant version

of the referenced forwarding agreement.

3. Entering the Business Partner, Locations and Dates/Times

Enter data for your business partner, such as the shipper, consignee and ordering party and define the location and dates

for the entire forwarding order. Note the following:

If you have defined this data in Customizing, the system determines the business partner automatically using the

partner determination profile specified in the forwarding order type. For more information, see Business Partner

Determination.

If you specify a location and have activated this in movement type Customizing, the system automatically

determines the associated shipper or consignee from the master data. If you specify a business partner, the system

determines the associated location data, as long as this data is unique (in other words, only one location exists for

which the business partner has been specified in the master data).

You can manually overwrite the address of the business partner that was automatically determined. It is marked as a

deviating address and copied to the follow-up documents. You can also already define a business partner in the

master data as a one-time business partner without address data. The address entered is then also a one-time

address. For more information, see Deviating Business Partner Addresses.

This is custom documentation. For more information, please visit SAP Help Portal.

14


1/14/26, 2:17 PM

You can enter additional print-specific (such as L/C-compliant) address information for business partners. The

system uses this address information automatically in print forms.

If you have specified this in Customizing for the forwarding order type, you can make a credit limit check for a

business partner (that is, for the ordering party or other paying business partners). For more information, see Credit

Limit Check.

You can also define alternative business partners, locations and dates for individual items in your forwarding order

(see process step 6).

For more information about business partner master data, see Business Partner.

4. Entering and Changing the Business Process-Dependent Data

If you want to use the forwarding order in specialist business processes and have activated these in the Customizing

settings for the forwarding order type, you can enter and change additional data, such as:

## Air cargo security

You can enter data for the air cargo security check. For more information, see Air Cargo Security.

## Instructions

You can display instructions that have been defined in Customizing. You can also create, change and delete them.

For more information, see Management of Instructions.

## Export/Import processing

For export/import processing, you can predefine the traffic direction in Customizing of the forwarding order type or

you can specify it in the forwarding order itself. You must also observe certain specifications when defining business

partners and sales organizations in your forwarding order. For more information, see Export/Import Processing.

## Handling codes

Handling codes allow you to specify certain properties of your transportations and goods to be transported (such as

dangerous goods) that may also be relevant for planning. For more information, see Handling Codes.

5. Determining the Route

If you have already received information about the ordered route from the ordering party, you can create the stages of the

route. For more information, see Determination of the Route.

6. Creating the Order Items

You create the items of a forwarding order in an item hierarchy consisting of container, packaging, and product, for

example. Only the top level of this hierarchy is relevant to planning. The quantities and weights of these levels are totaled

and copied to the header data.

For more information, see Creation of Forwarding Order Items or Forwarding Quotation Items.

7. Saving the Forwarding Order

You save the forwarding order. The system now assigns the document an ID from the number range for this document type.

In addition, the system checks the entered data for completeness and consistency. The system displays the results of these

checks in the form of error messages and as a completeness status.

If you have defined this in Customizing, the system performs a series of automatic functions, such as the following:

## Automatic creation of freight units

Automatic confirmation of the forwarding order, with sending of the confirmation to ordering party

## Automatic calculation of transportation charges

This is custom documentation. For more information, please visit SAP Help Portal.

15


1/14/26, 2:17 PM

Check whether the limits for triggering an approval workflow have been exceeded and, if necessary, trigger the

workflow.

## Check of the credit limit of the business partners

Check whether the foreign trade regulations have been followed in the forwarding order (see Trade Compliance

Check).

## More Information

## Editing of a Forwarding Order

Confirmation and Completion of a Forwarding Order

Creation of a Forwarding Order for Rail Transportation

Attributes for Process Control

## Use

In Transportation Management (TM), you can already specify several attributes when entering order data in the forwarding order

or forwarding quotation. These attributes then control the further process of order creation and execution. They are entered in the

header data of the business document in the General Data area and are valid for the whole business document.

The following section briefly describes these attributes. For more information, see the individual chapters in which the process is

described.

## Prerequisites

You have defined transportation modes and movement types in Customizing. For more information, see Customizing for

Transportation Management under the following Customizing activities:

## Master Data

 Transportation Network

 Transportation Lane

 Define Transportation Mode

## Forwarding Order Management

 General Settings for Forwarding Order Management

## Define Movement Types

If required, you have already defined the transportation mode, the traffic direction and the shipping type in Customizing for the

forwarding order or forwarding quotation type. If you use this option, the attributes are automatically entered in the business

document and cannot be changed there. For more information, see Customizing for Transportation Management under the

following Customizing activities:

Forwarding Order Management

## Forwarding Order

 Define Forwarding Order Types

Forwarding Order Management

## Forwarding Quotation

## Define Forwarding Quotation Types

If you want to use your own shipping types, you have defined shipping types in Customizing and assigned them transportation

modes if required. You can then select these shipping types in Customizing for forwarding order types and forwarding quotation

types using the input help on the user interface for the forwarding order and forwarding quotation. For more information, see

Customizing for Transportation Management under  Forwarding Order Management

 Define Shipping Types .

  Note

If you want to create a forwarding order based on a forwarding quotation and predefine the shipping type and the

transportation mode in Customizing for the forwarding quotation type, these settings must be the same as those in the

This is custom documentation. For more information, please visit SAP Help Portal.

16


1/14/26, 2:17 PM

forwarding order type.

## Features

## Transportation Mode

This attribute determines how the freight is transported, that is, via sea, air, or road transportation, or by train. It is valid for all

items and main carriage stages of the business document and is taken into account during manual planning as well as during the

creation of freight bookings and freight orders.

## Traffic Direction

This attribute determines whether the transport is an import or export from the point of view of the sales organization entered in

the header data of the forwarding order or forwarding quotation. This information then determines, for example, the stage for

which the sales organization and the processor of the business document is responsible (for example, up to the main carriage that

starts in a different country or region).

## Shipping Type

This attribute determines how the planning and execution of the transportation of the freight is performed for a transportation

mode. For example, you can define the following information for the individual transportation modes:

Sea: Transport of cargo as a full container load into which no other package or product may be loaded (Full Container Load,

FCL), or as individual packages and products (Less Than Container Load, LCL).

Air: Transport of cargo in unit load devices (ULDs) or as loose cargo (Loose)

Rail: Transport of cargo as a full carload (Carload), individual cargo items (Intermodal Rail), or as a complete train (Unit

Train)

Road: Transport of cargo as a full truck load (Full Truck Load, FTL) or as individual packages and products (Less Than

Truck Load, LTL)

The shipping type allows you to specify, for example, that when you enter items, only the container (or ULD) may be entered as a

planning-relevant item (top level of the item hierarchy) or that no container items may be created at all.

## Movement Type

This attribute allows you to specify for which stages the logistics service provider is responsible as well as which stage types are

allowed for a forwarding order or a forwarding quotation. You can, for example, define the following movement types:

Door to Door: The logistics service provider is responsible for picking up the goods at the shipper (source location) and

delivering to the ship-to party (destination location).

Port to Port: The logistics service provider is only responsible for the sea transportation of the freight. The transportation

of the freight from the shipper (source location) to the port of loading and from the port of discharge to the ship-to party is

arranged by the sold-to party.

Depending on your Customizing settings for the movement type, certain stages of the actual route are displayed automatically.

Additionally, the stage types that you can enter may be restricted. For more information, see Determination of the Route.

If you change the movement type, the system automatically adjusts the actual route to the new movement type. To transfer the

existing route to the new route, the system applies standard logic. It determines which stages can remain in the new route, which

have to be deleted, and which have to be created. You can use a Business Add-In (BAdI) to change this logic. For more information,

see Customizing for Transportation Management under  Business Add-Ins (BAdIs) for Transportation Management

This is custom documentation. For more information, please visit SAP Help Portal.

17


1/14/26, 2:17 PM

 Forwarding Order Management

## Changes to Movement Type

 BAdI: Adapt Locations and Dates When Movement Type Is

Changed ..

## Air Waybill Type

You use this attribute to control the air freight-specific consolidation processes. You can also restrict the consolidation options and

define how many forwarding orders you can assign to a freight booking or to a master air waybill. You cannot assign any additional

forwarding orders to a freight booking or a master air waybill if a forwarding order is marked as Back-to-Back.

You can predefine the attribute in Customizing for the forwarding order type or forwarding quotation type; or you can define it

directly in an air forwarding order or quotation. For more information, see Air Freight-Specific Consolidation Processes.

## Effects on the Follow-On Processes

The attributes mentioned are obligatory for follow-on processes such as transportation planning or the creation of freight orders

and freight bookings. If you change the transportation mode, shipping type, or movement type, the assigned freight units (FUs) or

transportation units (TUs) will be created again and the freight costs will be calculated again. The transportation mode and

shipping type cannot be changed if follow-on business documents exist for the FUs or TUs and the execution of at least one main

carriage stage of one of these FUs or TUs has already started.

The attributes (except for air waybill types) are not copied directly to the freight orders and freight bookings, but rather the system

determines them again based on the business documents.

Uncontrolled Transportation

## Use

You use this function to specify that the carrier assigned to the main carriage stage of a forwarding order bills the sold-to party

directly based on a special freight agreement between the carrier and the sold-to party. In this case, you are still responsible for

organizing the transportation of the goods and for planning all stages including the main carriage stage; however, you can calculate

charges and create settlement documents only for the pre-carriage and on-carriage stages.

## Activities

To specify that transportation is uncontrolled, deselect the Controlled checkbox on the General Data tab page of the forwarding

order UI. You can then enter the ID of the external freight agreement that exists between the sold-to party and the carrier.

Deselecting the checkbox and entering the freight agreement ID has the following effect on further processing:

When you assign freight units that belong to the forwarding order to a freight booking, the system displays the Controlled

checkbox and the External Freight Agreement field on the Terms and Conditions tab page of the freight booking. Both

fields are read-only. They are visible in a freight booking only if the Controlled checkbox has been deselected in the

corresponding forwarding order.

Note the following:

You can assign freight units from other forwarding orders to this freight booking only if the forwarding orders

contain the same external freight agreement ID.

You cannot consolidate forwarding orders in the case of a less than container load (LCL) freight booking.

The system determines a suitable forwarding agreement or forwarding agreement item where you deselected the

Controlled checkbox. For the system to be able to calculate the charges for an uncontrolled transportation, you must

specify a carrier for the stage or an external freight agreement in the forwarding order or freight agreement. Note that the

system can determine the forwarding agreement or forwarding agreement item even if you have not specified the external

This is custom documentation. For more information, please visit SAP Help Portal.

18


1/14/26, 2:17 PM

freight agreement for the forwarding agreement or forwarding agreement item. The system cannot calculate the charges

for an uncontrolled transportation if the system cannot determine a suitable forwarding agreement or forwarding

agreement item.

When you calculate charges and carry out forwarding settlement or freight settlement, the system ignores the main

carriage stage. You can calculate charges and create settlement documents only for the pre-carriage and on-carriage

stages.

Incoterms in Forwarding Orders

## Use

This function enables you to specify who pays for the individual stages of a transport.

In Transportation Management (TM), you create a forwarding settlement document (FWSD) when you need to send an invoice to a

customer. The settlement is based on an associated forwarding order. To create a settlement, you must have a forwarding

agreement between the business partner and sales organization in a forwarding order. This means you can have a forwarding order

on the export side with a settlement to the shipper, and another forwarding order on the import side with a settlement to the ship-

to party.

The Incoterms function addresses the following business requirements:

## Settlement with shipper or ship-to party

The settlement is independent of the organizational unit that organizes the parts of the transport.

  Example
In a full container load (FCL) transport with an Incoterm of FOB (Free On Board), the shipper pays for the pre-carriage to

the export organization. The ship-to party pays the main carriage and on-carriage to the import organization. This

applies even if the export organization organizes the main carriage.

## Settlement between the export and import organizations

The settlement depends on the organizational unit that organizes the parts of the transport.

  Example

In an FCL transport with FOB, the export organization that organized the main carriage actually pays for the main

carriage. It then invoices the import organization to recover the main carriage costs from the ship-to party.

In this way, the Incoterm you specify in the forwarding order drives the overall settlement process.

## Prerequisites

You have specified the agreement party role for a stage type and Incoterm combination. When you specify an Incoterm in a

forwarding order, the system uses the agreement party role to identify the default agreement party for a stage.

For more information, see Customizing for Transportation Management under  Forwarding Order Management

## Define Default

Agreement Party Roles for Stages .

Features

## Incoterms

This is custom documentation. For more information, please visit SAP Help Portal.

19


1/14/26, 2:17 PM

You can use Incoterms to determine who pays for the stages of a transport. The following are the main party roles for Incoterms:

Prepaid agreement party

Collect agreement party

Prepaid bill-to party

Collect bill-to party

Prepaid payer

## Collect payer

The prepaid party sends the goods; the collect party receives the goods. The party roles are not necessarily the shipper or ship-to

party, and can be internal organizational units.

  Example

An internal organization can be the collect agreement party in a settlement between internal organizational units.

For an export forwarding order, the collect bill-to party and collect payer party can be the import organization.

You can specify the party roles and business partners for Incoterms on the Business Partners tab page. The system uses the

parties you specify on this tab page to determine who pays for a stage when you create a settlement.

You can only specify agreement party roles in the Stages tab page. The system uses the information you specify on the Stages tab

page to determine the agreement and therefore to calculate charges.

The following table explains how you assign party roles to business partners in the Business Partners tab page:

Business Partner

Party Role

BP1

BP2

Prepaid agreement party

## Collect agreement party

The following table explains how the system determines the agreement party when you specify the agreement party role in the

Stages tab page:

Stage Description

## Stage Type

Agreement Party Role

Agreement Party

Stage 1

Stage 2

Stage Status

## Pre-carriage

Prepaid agreement party BP1

## Main carriage

Collect agreement party

BP2

The system uses the following logic to determine the stage status:

The planning and execution organization for a stage belongs to a company organization. A company organization is

specified in the sales organization of the forwarding order. If these company organizations match, the stage status is

relevant for planning and execution.

The system displays the appropriate status in the Stage Status field.

If the company organizations do not match, the stage status is not relevant for planning and execution.

This is custom documentation. For more information, please visit SAP Help Portal.

20


1/14/26, 2:17 PM

The system displays a status of Not Relevant in the Stage Status field.

When you manually create an FWSD, the system displays a dialog box in which you select the relevant business partner. You can

create the FWSD for one of the new party roles. The party role that you select depends on the Incoterm specified in the forwarding

order.

  Example

You have a forwarding order with an Incoterm of EXW (Ex Works) to which you have assigned a collect agreement party. You can

create a collect FWSD for the collect agreement party.

You have a forwarding order with an Incoterm of DDP (Delivery Duty Paid) to which you have assigned a prepaid agreement

party. You can create a collect FWSD for the prepaid agreement party.

You can create more than one settlement document for these forwarding orders.

## More Information

For more information about forwarding orders, see Forwarding Order Management.

For more information about forwarding settlement documents, see Forwarding Settlement Document.

Freight Terms in Forwarding Orders

## Use

In a transportation scenario, you can have the following business requirements:

## Agree transportation charges in advance

You agree the transportation charges in advance with your customer. The charges provide the basis for settling the overall

transportation costs.

You can also agree on settlement terms for the individual parts of the freight cost in advance. You know in advance the

individual parts of the transportation that are paid for by the prepaid payer or the collect payer.

## Capture the entire transportation in a single forwarding order

In the standard scenarios for logistics service providers (LSPs), you use two business documents, an export forwarding

order and an import forwarding order, to deliver a forwarding order. For more information, see Export/Import Processing.

When you use a freight term, you work with just one forwarding order.

## Create forwarding settlement documents from the same forwarding order

You need a forwarding settlement document for the prepaid charges and another forwarding settlement document for the

collect charges in the same forwarding order. For more information on the differences between a freight term process and

an Incoterm process, see Process Differences Between Freight Terms and Incoterms.

## Settle the prepaid charges with the prepaid payer

The prepaid payer is usually the organization of the sold-to party that is closest to the location of origin.

## Settle the collect charges with the collect payer

The collect payer is usually the organization of the ship-to party that is closest to the destination location.

This is custom documentation. For more information, please visit SAP Help Portal.

21


1/14/26, 2:17 PM
## Example

The following figure illustrates a simple carrier scenario with freight terms and is followed by an explanation:

An LSP, LSP_DE, orders a transportation service from you, a carrier. Your agency in Germany, CARRIER_DE, organizes and delivers

the transportation service from Nuremberg to Houston. Your agency in the United States, CARRIER_US, organizes and delivers the

transportation service from Houston to Dallas.

## Forwarding Agreement Settings

You have one forwarding agreement, Forwarding_Agreement_1. The forwarding agreement contains the following details:

Sales organization: CARRIER_DE

sold-to party: LSP_DE

You have the following charge components in the agreement:

## Ocean freight charges

Export handling charge at Rotterdam

Import handling charge at Houston

You settle the charges as follows:

Prepaid charges settled between the prepaid payer (LSP_DE) and the prepaid invoicing party (CARRIER_DE)

Collect charges settled between the collect payer (LSP_US) and the collect invoicing party (CARRIER_US)

## Calculation Sheet Settings

You have a calculation sheet item of EUR 1,500 for the charge type Ocean Freight Charges. The table explains the freight terms

that you specify on the Freight Terms tab page of the calculation sheet item:

Freight Term

## Payer

Prepaid/Prepaid (PP) Prepaid payer

Collect/Collect (CC)

## Collect payer

The table explains the freight terms for the charge type Export Handling Charge (EUR 150):

This is custom documentation. For more information, please visit SAP Help Portal.

22


1/14/26, 2:17 PM

Freight Term

## Payer

Prepaid/Prepaid (PP) Prepaid payer

Collect/Collect (CC)

## Collect payer

The table explains the freight terms for the charge type Import Handling Charge (USD 200):

Freight Term

## Payer

Prepaid/Prepaid (PP) Collect payer

Collect/Collect (CC)

## Collect payer

You assign the calculation sheet to your forwarding agreement, Forwarding_Agreement_1.

## Forwarding Order Settings

The table explains the settings you enter in the forwarding order:

Setting Name

## Setting

## Freight term

Prepaid/Prepaid (PP)

Sales organization

CARRIER_DE

sold-to party

## LSP_DE

Prepaid bill-to party

## LSP_DE

Prepaid payer

## LSP_DE

Collect bill-to party

## LSP_US

Collect payer

## LSP_US

Prepaid invoicing party CARRIER_DE

Collect invoicing party

## CARRIER_US

## Charge Calculation

The table explains how the system calculates the prepaid charges in the forwarding order (CARRIER_DE bills LSP_DE for these

charges):

Charge Type

## Amount

Ocean freight charges

EUR 1,500

Export handling charge

EUR 150

CARRIER_US bills LSP_US for USD 200, for the collect charge Import handling charge.

## Forwarding Settlement Document

The system creates a settlement document for the prepaid charge types. The system includes the following details in the

settlement:

This is custom documentation. For more information, please visit SAP Help Portal.

23


1/14/26, 2:17 PM

Invoicing party: CARRIER_DE

Bill-to Party: LSP_DE

## Payer: LSP_DE

Charge item: CARRIER_DE, Forwarding_Agreement_1, item_0001, against LSP_DE

Ocean freight charges: EUR 1,500

Export handling charge: EUR 150

The system also creates a forwarding settlement document for the collect charge types. The system includes the following details

in the settlement:

Invoicing party: CARRIER_US

Bill-to party: LSP_US

## Payer: LSP_US

Charge item: CARRIER_US, Forwarding_Agreement_1, item_0001, against LSP_US

Import handling charge: USD 200

  Note

You can have different currencies in the prepaid and collect forwarding settlement documents. For more information, see

Freight Term Features in Forwarding Orders.

## More Information

Freight Term Prerequisites

Creation of a Forwarding Order

Freight Term Prerequisites

## Use

## Standard Settings

You have specified the standard settings for charge calculation. For more information, see Standard Charge Calculation.

## Freight Term for Transportation Modes Settings

You have specified the appropriate freight term settings in Customizing for Transportation Management under  Basic Functions

 Charge Calculation

## Basic Settings

 Freight Term Settings for Transportation Modes

  Define Freight Terms for

Transportation Modes .

For example, the following table contains the freight term settings you can specify for a transportation mode category of Sea:

Freight Term

Description

CC

## Collect/Collect

This is custom documentation. For more information, please visit SAP Help Portal.

24


1/14/26, 2:17 PM

Freight Term

Description

CP

PC

PP

Collect/Prepaid

Prepaid/Collect

## Prepaid/Prepaid

You can enter the freight terms you specify in this Customizing activity in the following business documents:

On the Freight Terms tab page of a calculation sheet item (see Calculation Sheet)

In the Freight Term field on the  General Data

 Settlement Terms  tab page of a forwarding order (see Forwarding

Order)

## Charge Calculation

You have specified the following charge calculation settings in Customizing for Transportation Management under  Basic

## Functions

 Charge Calculation

 Basic Settings :

## Define Charge Profiles

You have specified a charge profile for sales. You have assigned the charge profile for sales to a sales organization in your

company in Customizing for Transportation Management under  Master Data

 Organizational Management

 Organizational Model

 Change Organizational Model

 (transaction PPOME).

The system uses the charge profile when you calculate charges in a forwarding order, where the forwarding order contains

the sales organization.

## Define Charge Types

You have specified the relevant settings for the charge types that you assign to calculation sheets and rate tables, including

the freight term and payer for a charge type.

  Note

For a forwarding order that contains a freight term, the system automatically sets the calculation level to Header Level

Calculation. You cannot change this setting. For more information, see Calculation Profiles.

## Party Roles

You have specified the appropriate business partners for the following party roles on the Business Partner tab page of a

forwarding order:

Prepaid payer

## Collect payer

Prepaid invoicing party

Collect invoicing party

## Order and Quotation Types

You have specified the settlement terms for the forwarding order type used when creating the forwarding order.

You specify the settlement terms in Customizing for Transportation Management under  Forwarding Order Management

## Forwarding Order

 Define Forwarding Order Types .

This is custom documentation. For more information, please visit SAP Help Portal.

25


1/14/26, 2:17 PM

You have specified the settlement terms for the forwarding quotation type used when creating the forwarding quotation.

You specify the settlement terms in Customizing for Transportation Management under  Forwarding Order Management

## Forwarding Quotation

 Define Forwarding Quotation Types .

## More Information

Freight Terms in Forwarding Orders

Freight Term Features in Forwarding Orders

## Use

## Examples of Freight Terms in a Forwarding Order

The following table contains an example of the freight terms you can assign in your calculation sheet. You assign the freight terms

on the Freight Terms tab page of the calculation item.

Charge Type

## Freight Term

Prepaid/Prepaid (PP)

Prepaid/Collect (PC)

Collect/Prepaid (CP)

Collect/Collect (CC)

Pick-up charges

## Prepaid

Export clearance

## Prepaid

Export handling charge

## Prepaid

at port of loading

Basic freight

## Prepaid

Bunker adjustment

## Prepaid

Currency adjustment

## Prepaid

Import handling charge

## Collect

at port of unloading

Customs handling

## Collect

Delivery charge

Collect

Prepaid

Prepaid

Prepaid

Prepaid

Collect

Collect

Collect

Collect

Collect

Collect

Collect

Collect

Collect

Prepaid

Prepaid

Prepaid

Prepaid

Prepaid

Prepaid

Prepaid

Prepaid

Collect

Collect

Collect

Collect

Collect

## Collect

The following table explains the settings you enter in the forwarding order:

Setting Name

## Setting

## Freight term

Prepaid/Prepaid (PP)

Sales organization

CARRIER_DE

sold-to party

## LSP_DE

Prepaid bill-to party

## LSP_DE

Prepaid payer

## LSP_DE

This is custom documentation. For more information, please visit SAP Help Portal.

26


1/14/26, 2:17 PM

Setting Name

## Setting

Collect bill-to party

## LSP_US

Collect payer

## LSP_US

Prepaid invoicing party CARRIER_DE

Collect invoicing party

## CARRIER_US

The following table contains an example of how the system determines who pays when you use the Prepaid/Prepaid (PP) freight

term in a forwarding order:

## Charge Type

Location of Charge

## Payer

Invoicing Party

Pick-up charges

## Nuremberg

Export clearance

## Hamburg

Export handling charge at port

Hamburg

of loading

Basic freight

## Main stage

Bunker adjustment

## Main stage

Currency adjustment

## Main stage

Import handling charge at port

## Houston

of unloading

Customs handling

## Houston

Delivery charge

## Dallas

Forwarding Agreement

LSP_DE

LSP_DE

LSP_DE

LSP_DE

LSP_DE

LSP_DE

LSP_US

LSP_US

## LSP_US

CARRIER_DE

CARRIER_DE

CARRIER_DE

CARRIER_DE

CARRIER_DE

CARRIER_DE

CARRIER_US

CARRIER_US

## CARRIER_US

The system uses the sold-to party and the sales organization in the forwarding order to determine which forwarding agreement to

use.

For a freight term, the calculation level is always header level. This means that the system uses just one forwarding agreement to

calculate charges.

For more information on how the system determines which forwarding agreement to use, see Agreement and Calculation Sheet

Determination.

  Note

The document currency and term of payment in the agreement is copied into the settlement document. If you want to use

different currencies and terms of payment in your scenarios for prepaid and collect business partners, do not enter the

document currency and term of payment in the agreement.

## Currency Determination

In a forwarding order that contains freight terms, the system uses the following approach to assign a currency to a collect charge

item and a prepaid charge item:

1. The document currency specified in the agreement

This is custom documentation. For more information, please visit SAP Help Portal.

27


1/14/26, 2:17 PM

2. The currency specified in the master data for the business partner under  Logistics

 Transportation Management

## Master Data

## Maintain Business Partner

For the business partner in focus (either prepaid or collect payer), the currency is maintained for the business partner on

the  BP

 Customer Org Data

## Payment

 Currency  tab page for the organization in focus (either prepaid or collect

invoicing party).

  Example

You specify the following party role and business partner settings on the Business Partner tab page of a forwarding

order:

## Party Role

Business Partner

Sales Organization

CARRIER_DE

sold-to party

## LSP_DE

Prepaid Bill-to Party

## LSP_DE

Collect Bill-to Party

## LSP_US

Prepaid Payer

## LSP_DE

Collect Payer

## LSP_US

Prepaid Invoicing Party CARRIER_DE

Collect Invoicing Party

## CARRIER_US

The following table contains the settings you enter in the  Maintain Business Partner

 (BP) transaction:

## Setting

Business Partner

Display in BP Role

Entry

## LSP_DE

Sold-to Party

Customer Org. Data

 Sales Org. Settings

## Sales

CARRIER_DE

Organization

Customer Org. Data

 Payment

 Currency

EUR

The system uses the currency that you have assigned to CARRIER_DE in the forwarding order.

3. The local currency that you specify in the charges profile that you assign to the sales organization in the forwarding order

For example, you specify a charges profile for sales organization CARRIER_DE (which is the prepaid invoicing party).

Therefore the system uses the currency you specify for sales organization CARRIER_DE.

4. The currency that you specify for a company to which the sales organization in a forwarding order belongs

You can specify the currency in transaction PPOME under  Org. Data

 Currency . For example, you do not specify a

currency for sales organization CARRIER_DE (which is the prepaid invoicing party). Also, you do not assign a charges profile

to CARRIER_DE. CARRIER_DE is a part of company COMPANY_DE. Therefore the system uses the currency you specify for

company COMPANY_DE.

## Credit Limit Check

This is custom documentation. For more information, please visit SAP Help Portal.

28


1/14/26, 2:17 PM

The system performs a credit limit check on the business partners you specify in the party roles in a forwarding order. The system

uses the following pairs:

Sales organization or forwarding house represented by the prepaid invoicing party and the prepaid payer party

Sales organization or forwarding house represented by the collect invoicing party and the collect payer party

For more information, see Credit Limit Check.

## Terms of Payment

In a forwarding order that contains freight terms, the system uses the following approach to assign terms of payment to a collect

charge item and a prepaid charge item:

1. The terms of payment specified in the agreement

2. The terms of payment specified in the business partner master data of a sales organization

You specify the terms of payment in the business partner master data of a sales organization as follows:

a. On the SAP menu, choose  Logistics

 Transportation Management

## Master Data

 Maintain Business Partner

.

b. In the Display in BP Role field, enter Sold-to Party.

c. Choose the Customer Org. Data tab page.

d. Choose Show Detail Data to display the details of the sales organization.

e. In the Payment screen area, enter the terms of payment.

The sales organization is either the prepaid invoicing party or the collect invoicing party.

Note that you can also enter or edit a term of payment on the Business Partner tab page of a forwarding order for the party roles

Prepaid Payer and Collect Payer to override the terms of payment determined by the system.

You define terms of payment in the Define Terms of Payment Customizing activity.

## Forwarding Settlement Documents

In a forwarding order that contains freight terms, the system creates a forwarding settlement document for the prepaid payer and

another forwarding settlement document for the collect payer. If you manually create a forwarding settlement document from the

forwarding order, the system displays a dialog box with the following options:

Prepaid party

## Collect party

Both prepaid party and collect party

## Other party

When you create a forwarding settlement document against another party for unplanned charges, you can select either the

prepaid invoicing party or the collect invoicing party as the sales organization that issues the forwarding settlement document.

## More Information

## Freight Terms in Forwarding Orders

This is custom documentation. For more information, please visit SAP Help Portal.

29


1/14/26, 2:17 PM

Process Differences Between Freight Terms and Incoterms

Forwarding Settlement

## Creation of a Forwarding Order

Process Differences Between Freight Terms and Incoterms

## Use

You can only enter either a freight term or an Incoterm in a forwarding order. You cannot enter both.

The following table describes the differences between entering a freight term or an Incoterm in a forwarding order:

Freight Term

## Incoterm

You cannot use the export/import process.

You can use the export/import process (for more information, see

Export/Import Processing).

The calculation level is always header level.

The calculation level is always stage level.

The forwarding settlement document for the prepaid party and the

The forwarding settlement document for the prepaid party and the

collect party are created from the same forwarding order.

collect party are created from the same forwarding order.

The forwarding order has a different prepaid sales organization and

The sales organization in the forwarding settlement document is

collect sales organization, which are derived from the prepaid

the same as the sales organization in the forwarding order.

invoicing party and collect invoicing party in the forwarding order.

If the export/import process is activated with a forwarding order

with the traffic direction Export, on the import side the system

creates a forwarding order with the traffic direction Import and the

sales organization as the importing organization.

The system uses the sales organization and order party to

The system uses the sales organization and the prepaid agreement

determine the agreement used for the freight costs for both the

party to determine the agreement for the freight costs for the

prepaid payer and collect payer.

prepaid payer.

The system uses the sales organization and the collect agreement

party to determine the agreement for the freight costs for the

collect payer.

The system uses the freight term settings that you define in the

The system uses the Incoterm settings that you define in the

calculation sheet item to determine the payer of the charge.

calculation sheet item to determine the payer of the charge.

If you do not specify either a freight term or an Incoterm in a forwarding order, the system uses the sold-to party to determine the

appropriate forwarding agreement, and creates just one forwarding settlement document against the sold-to party.

## More Information

Freight Terms in Forwarding Orders

Freight Term Prerequisites

## Freight Term Features

This is custom documentation. For more information, please visit SAP Help Portal.

30


1/14/26, 2:17 PM

Credit Limit Check

## Use

You can use this function to determine the risk of losses on receivables from business partners and to make timely and efficient

credit decisions.

## Integration

Transportation Management (TM) integrates with the SAP Credit Management application to provide the credit limit check

feature.

## Features

## Business Partner Party Role Checks

The system checks the business partners you specify in the party roles in a forwarding order during a credit limit check.

It checks in the following order of priority if you have specified an Incoterm.

1. Prepaid side

a. Prepaid payer

b. Prepaid agreement party

2. Collect side

a. Collect payer

b. Collect agreement party

The system checks in the following order of priority if you have not specified an Incoterm:

1. Payer

2. sold-to party

We deliver this party role checks as standard. You cannot change the settings for these checks in Customizing.

## Credit Segment

When you perform a credit limit check on a forwarding order, the system checks the following conditions to identify the relevant

credit segment:

Has the BAdI: Credit Segment Determination for Forwarding Orders Business Add-In (BAdI) been defined?

Has the sales organization in the forwarding order been assigned to a credit segment?

Has the company organization to which the sales organization in the forwarding order belongs, been assigned to a credit

segment? If one of these conditions is met, the system uses the relevant credit segment.

Check Enabling.

In Customizing, you can specify that the credit limit check feature can be enabled by forwarding order type. If you make this

specification, the system automatically performs a credit limit check when you save a forwarding order. You can review the credit

This is custom documentation. For more information, please visit SAP Help Portal.

31


1/14/26, 2:17 PM

limit check status for orders in the Forwarding Orders worklist, and perform a manual check in an individual forwarding order.

For more information about enabling the credit limit check for a forwarding order type, see Customizing for Transportation

Management under.  Forwarding Order Management

## Forwarding Order

 Define Forwarding Order Types .

For more information about defining the credit segment IDs that the TM system uses to access the credit management

functionality in the SAP Credit Management application, see Customizing for Transportation Management under.  Basic

## Functions

 Credit Management Integration

 Integration with Credit Management

.

## SAP Credit Management Integration

TM updates SAP Credit Management at the following points in the business transaction flow:

When you create, change, or cancel a forwarding order with a credit limit check status of successful, or when you manually

approve a credit limit check failure

When you post a forwarding settlement document to Sales and Distribution (SD)

When you post an SD billing document to Financial Accounting (FI)

When you cancel a forwarding settlement document and the corresponding FI and SD documents are canceled

When you save, change, or cancel a forwarding order, the credit limit amount is updated to reflect the credit exposure

corresponding to the forwarding order. The application updates the amount in the Open Orders exposure category from the

forwarding order.

The TM system automatically checks the credit limit when you change the amounts or organizational entities in the forwarding

order. For example, the system automatically checks the credit limit when you change the following settings:

## Sales organization

Calculated amount or credit limit check amount

## Business partner

Logistics data that can influence the calculated amount, such as stages, weights, and volumes

When you successfully create and post a forwarding settlement document to SD, the credit limit check amount is updated in SAP

Credit Management. The application reduces the exposure value of the open order for the forwarding order by the amount of the

forwarding settlement document. The value from the SD billing document corresponding to the forwarding settlement document

is updated to the Billing Document Value exposure category. The system also performs these updates when you change and

cancel a forwarding settlement document.

TM integrates directly with SAP Credit Management when you configure TM and SAP Credit Management on a single client. If you

configure SAP Credit Management on a separate system or client, TM uses Web Services to interact with SAP Credit Management.

If you configure SAP Credit Management on a separate system or client, TM informs SAP Credit Management about the credit limit

check amount approved for a customer in a specific forwarding order using the Notify of Credit Commitment

(CreditCommitmentNotification_Out) service operation in the Transportation Request Processing process component.

If you configure SAP Credit Management on a separate system or client, TM informs SAP Credit Management about the credit limit

check amount in billing documents that are related to an approved forwarding order using the Notify of Credit Commitment

(CreditCommitmentNotification_Out) service operation in the Customer Freight Invoice Request Processing process

component.

Check Failures.

This is custom documentation. For more information, please visit SAP Help Portal.

32


1/14/26, 2:17 PM

If the credit limit check fails, the system uses the setting you specified in the Act. If CLC Failed (Action if Credit Limit Check Failed)

field of the Customizing for Define Forwarding Order Types. You can choose to block the order or take no action.

You can review the results of a credit limit check failure, including details on the credit limit for the business partner, and the

exposure amount. You can approve or reject an order that has failed. You must enter a reason for the approval or rejection.

When you approve the order, the system automatically removes the block, and you can process the order as normal. When you

reject the order, the system cancels the order.

If you configure SAP Credit Management on a separate system or client, TM does the credit worthiness check using the

CreditWorthinessQuery_Out service operations in the Transportation Requet Processing process component.

## More Information

For more information about SAP Credit Management, see SAP Library for SAP S/4HANA under.  Enterprise Business

Applications

## Finance

 Financial Operations

## Receivables Management

 SAP Credit Management (FIN-FSCM-CR)

.

For more information about updatong the credit exposure for a business partner in SAP Credit Management from TM, see

Updating of Credit Exposure.

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

This is custom documentation. For more information, please visit SAP Help Portal.

33


1/14/26, 2:17 PM

  Note

If you are a logistics service provider and can commit all the carriers who work for you to the same transportation service level,

we recommend you make the following settings:

Define transportation service level codes in Customizing. For more information, see Customizing for Transportation

Management under  Forwarding Order Management

 Define Transportation Service Level Codes .

Enter one of these values as the standard service level when you define your freight order type. For more information,

see Customizing for Transportation Management under  Freight Order Management

 Freight Order

## Define Freight

Order Types . The system then uses this value when you create a freight order.

Editing of a Forwarding Order

## Use

After you have created and saved a forwarding order, you can use this business document to perform further actions, such as the

following:

Create freight units

## Determine route

Start transportation planning

Create freight documents

Calculate transportation charges

Create forwarding settlement document

## Prerequisites

See Creation of a Forwarding Order.

## Process

The following describes an example of a process for editing the forwarding order and starting the transportation planning:

1. Creation of Freight Units

If the freight units are not created automatically after you save the forwarding order, you trigger the creation manually on

the user interface for the forwarding order (Follow-Up Actions menu). In this case, the system considers either the freight

unit building rule (FUB rule) or the condition for determining an FUB rule that you have specified in Customizing. A

prerequisite for the creation of freight units (automatically or manually) is that all required data has been entered in the

forwarding order.

You can have the system create the freight units per order item, for example, or define that the system merges as many

order items as possible into one freight unit. For more information, see Creation and Editing of Freight Units.

After the system has created the freight units, the life cycle status changes from New to In Planning.

2. Manual Transportation Planning

This is custom documentation. For more information, please visit SAP Help Portal.

34


1/14/26, 2:17 PM

You call the transportation cockpit. You enter your planning profile and selection profile and start the planning. The freight

units created by the system are displayed in the transportation cockpit.

You can now execute manual transportation planning by pulling the freight units to the resources via drag and drop. The

system then creates a freight order, which is displayed in the document flow for the forwarding order.

For more information about transportation planning, see Planning.

As an alternative to manual transportation planning, you can proceed as follows:

## Determination of a route

You can have the system determine a route. In doing so, the system generates several alternative routes for each

freight unit, one of which you can then accept. In Customizing for the forwarding order type, you can determine

whether only the freight units (that is, only the route) are to be saved when you accept the route or whether the

freight orders (that is, the planning) are to be saved as well. The system adjusts existing freight units.

If the freight orders are also saved, the life cycle status changes to Planned after you accept the proposed route. The

route is displayed in the forwarding order in the form of stages. For more information, see Determination of the

Route and Generation of Transportation Proposals.

## Automatic planning

You can use the VSR optimizer to perform automatic planning from the transportation cockpit. For more

information, see VSR Optimization.

## Direct creation of freight documents

Directly from the forwarding order, you can already create freight documents, such as freight orders or freight

bookings for the transportation stages defined in the document. You can also select available freight bookings. For

more information, see Direct Creation of Freight Documents and Selection of Schedules.

When all freight units of the forwarding order have been planned, the life cycle status changes to planned.

3. Calculating Transportation Charges

If you have activated transportation charge calculation in Customizing for the forwarding order type, and if the

transportation charges are not calculated automatically when you save the forwarding order, you can allow the forwarding

order to calculate these charges (internal and external charges). Moreover, you can enter the charges manually in the

forwarding order. The system recalculates the transportation charges each time the forwarding order is saved again.

However, transportation charges that you entered manually are fixed by the system and are kept during recalculation. For

more information, see Charge Calculation.

If you quickly want to estimate the transportation charges based on a minimum of data, you can use the Estimate

Forwarding Charges function to do so. For more information, see Charge Estimation.

You can also display a profitability analysis in the forwarding order (separate tab page). In the analysis, the system takes

into account all costs and revenues associated with the execution of a forwarding order. For more information, see

Profitability Analysis.

4. Creating a Forwarding Settlement Document

If you have activated this function in Customizing for the forwarding order type, you can create a forwarding settlement

document from the forwarding order based on the transportation charge calculation (Costs/Settlement menu). For more

information, see Forwarding Settlement and Internal Settlement Management.

5. Printing Documents

You can print the forwarding order directly or after previewing it. The default printout contains information such as item

descriptions and weights. If you have entered your order items in an item hierarchy, information about the lower hierarchy

levels are also displayed.

This is custom documentation. For more information, please visit SAP Help Portal.

35


1/14/26, 2:17 PM

The print history is displayed in the forwarding order under Output Management. This history also contains information

about all the documents you have faxed or sent by e-mail or EDI.

For more information, see Output Management.

6. Editing or Canceling the Forwarding Order

You can still change most of the data in a forwarding order or quotation during the transportation process, such as dates,

quantities, and locations, as well as add or delete items. This is also the case if freight units have already been built and

planning has been completed or execution has started. The system updates the freight units when saving the data. Follow-

on documents such as freight orders and freight bookings are also adjusted.

However, if data has already been transferred to the freight unit from the execution process and the status of the freight

unit has been changed to On Hand, for example, the system no longer adjusts the follow-on documents automatically. In

this case, the system prompts you to change the data manually.

If a forwarding settlement document or an internal settlement document already exists and you have activated the

forwarding settlement change process, you can enter the changes directly in the forwarding order (for example, changes to

quantities, to the shipper, or to the consignee). The change process triggers the necessary changes in the forwarding

settlement process. If a forwarding settlement document or an internal settlement document already exists and you have

not activated the forwarding settlement change process, you have to cancel the forwarding settlement document. You then

enter the changes directly in the forwarding order and create a new forwarding settlement document that contains the

changes. You can activate the forwarding settlement change process in the corresponding settlement profile by selecting

Reverse and Repost or Delta Only. The system uses the organization or a combination of organization and business

partner to assign the profile to the forwarding order. For more information, see Automatic Change Management for

Forwarding Settlements.

You can also cancel a forwarding order. Depending on your Customizing settings, you can enter a reason code that is then

displayed in the General Data area of the forwarding order. For more information, see Customizing for Transportation

Management under  Forwarding Order Management

 Define Cancellation Reason Codes .

After the cancellation, the planning is invalid and the system deletes the freight units. The life cycle status changes to

Canceled.

  Note

The cancellation of a forwarding order cannot be changed. A forwarding order cannot be canceled if it has been assigned

a freight document.

For more information, see Processing of Changes and Deletion of Forwarding Orders.

7. Executing a Forwarding Order

You can use SAP Event Management to monitor the further execution of the forwarding order. To do this, you need to have

set the corresponding indicator in Customizing for the document type. The forwarding order receives a tracking number

(tracking ID) upon creation. You can provide this number to your ordering party, who can then use it to track the execution

of the order on a special Web user interface. The system later creates event handlers for the follow-up documents freight

unit and freight order. For more information, see Integration with SAP Event Management.

Irrespective of SAP Event Management, the system displays the execution status in the forwarding order. It reflects the

execution status of the freight order (or rather, the cumulated execution status if several freight orders exist for the

forwarding order).

## More Information

Confirmation and Completion of a Forwarding Order

## Forwarding Order Management Preparation

This is custom documentation. For more information, please visit SAP Help Portal.

36


1/14/26, 2:17 PM

Profitability Analysis

## Use

You can view a profitability analysis in the forwarding order. The system takes into account all the costs and revenues associated

with the execution of a forwarding order in the analysis. You cannot edit the analysis.

The system displays the revenues, costs, and profits for the planned profitability and estimated profitability. You can navigate to

business document level in the analysis hierarchy, and you can open the individual business documents.

## Sources of Costs and Revenue

The sources of costs are freight orders, freight bookings, and freight settlement documents. The sources of revenue are forwarding

orders and the corresponding forwarding settlement documents. Internal settlement documents are costs for the company

receiving the settlement and revenue for the company sending the settlement.

## Calculation of Profitability

The system performs the following analysis:

## Planned profitability

The system calculates the revenue and cost charges from forwarding orders. It takes the planned revenue from the charge

calculation done in the forwarding order.

It takes the planned cost from the internal charge calculation done in the forwarding order. This is the planned internal cost

for the forwarding order. Note the system does not include the internal charges in the freight order or freight booking when

it calculates profitability.

If you enable intercompany settlement, the system uses the cost from the cost distribution in the freight order for an

intracompany stage and the cost from the internal charges for an intercompany stage. If you enable intracompany

settlement, the system uses the cost from the internal charges for both an intracompany and an intercompany stage.

You can enable a sales organization for intracompany settlement in transaction  PPOME

 Org. Data (Organization Data)

 Detailed Settings

 Intracompany Settlement

.

## Expected profitability

The system calculates the revenue and cost charges from settlement documents. It takes the expected revenue

calculations from the charge calculation done in the forwarding settlement documents that are associated with the relevant

forwarding order.

The system takes the expected cost from the cost distribution done on the relevant freight settlement documents. It also

takes the expected cost from the relevant internal settlement documents.

## Comparison of Profitability Charges

The system displays the results of the profitability analysis on the Profitability Details screen area of the Profitability tab page of a

forwarding order. It groups the results in a hierarchy, by charge category. You can compare the profitability down to the level of

charge types.

The following table contains an example of how the system displays the results:

Charge Category

Planned Cost (USD)

Planned Revenue (USD)

Planned Profit Amount (USD)

General Charges

100

150

50

This is custom documentation. For more information, please visit SAP Help Portal.

37


1/14/26, 2:17 PM

Charge Category

Planned Cost (USD)

Planned Revenue (USD)

Planned Profit Amount (USD)

120

350

100

150

225

75

30

-75

-25

Sea Freight Charges

CSI-BAF Bunker

Adjustment Factor

CSI-BASE Basic Freight

Charge

## CSI-LOAD

Loading/Unloading

## Charge

Other Transportation Charges

1350

1500

150

In the forwarding order above, you incur a loss of USD 70 in sea freight charges. However, you make a profit of USD 50 in general

charges and USD 150 in other transportation charges. This results in an overall profit of USD 130 ((50 + 150) -70).

## Profitability Status

The system displays the profitability status on the Profitability tab page of a forwarding order. The following table explains what

each profitability status means:

## Status

Not Yet Calculated

## Calculated

Recalculation Required

## Meaning

You have not yet calculated the profitability of the forwarding order.

You have calculated the profitability and the calculation is up to

date.

You have calculated the profitability, but there has been a change to

one or more of the following elements since you performed the

calculation:

Internal or external charges in the forwarding order or

associated freight orders

Freight orders or freight bookings that contain the

forwarding order

Freight settlement documents for the freight orders or

freight bookings that contain the forwarding order

Forwarding settlement document for the forwarding order

Internal settlement documents for the forwarding orders

You must calculate the profitability again.

You can calculate or recalculate the profitability by choosing  Charges/Settlement

 Calculate Profitability  in a forwarding

order. Alternatively, you can use the Calculation of Profitability (/SCMTMS/CALC_PROFITABILITY) background processing

function to schedule a background function to calculate or recalculate the profitability. For more information, see Calculation of

Profitability.

## Prerequisites

You have made the following settings in Customizing to enable a profitability analysis in a forwarding order:

This is custom documentation. For more information, please visit SAP Help Portal.

38


1/14/26, 2:17 PM

Enabled the relevant freight order or freight booking type for cost distribution. This is the freight order or freight booking

that you use as a basis for determining the freight cost source for the expected profitability. For more information, see

Customizing for Transportation Management under  Freight Order Management

## Freight Order

## Define Freight Order

Types and Freight Order Management

## Freight Booking

 Define Freight Booking Types .

If you use an internal agreement to calculate the planned costs, you have enabled the relevant forwarding order type for

internal charge calculation. For more information, see Customizing for Transportation Management under  Forwarding

Order Management

## Forwarding Order

 Define Forwarding Order Types .

Specified a cost distribution profile with distribution level of Forwarding Order for the purchasing organization. To specify a

distribution profile, see Customizing for Transportation Management under  Basic Functions

## Cost Distribution

 Define Cost Distribution Profiles . You assign the cost distribution profile to the purchasing organization by assigning the

distribution profile to the charges profile. For more information, see Customizing for Transportation Management under

Basic Functions

 Charge Calculation

## Basic Settings

 Define Charges Profiles .

Enabled the freight settlement document for cost distribution so the expected costs are available for the profitability

analysis in the forwarding order. For more information, see Customizing for Transportation Management under

## Settlement

## Freight Settlement

 Define Freight Settlement Document Types .

  Note

The system only calculates the complete planned profitability after you have performed charge calculation in the

following business documents:

## Forwarding order

Freight order or freight booking in which you have enabled cost distribution at the level of Forwarding Order

If you need to use an internal agreement to make the planned costs available to the profitability analysis, you must

perform an internal charge calculation in the forwarding order.

The system only calculates the complete expected profitability after you have completed the following tasks:

Generated all the necessary freight settlement documents for the freight order or freight booking that execute

the relevant forwarding order

Enabled the freight settlement documents for cost distribution at forwarding order level or created internal

settlement documents

In an export-import situation, you create two forwarding orders; one for each of the export and import sides. The system

restricts the profitability analysis to each of the forwarding orders individually. For example, it does not include the

revenue and costs from the forwarding order on the import side in the profitability analysis of the forwarding order on

the export side.

## Example

You are sales organization Nuremberg. You receive a forwarding order, with an Incoterm of FOB (Free On Board), from a customer

in Germany. The following table describes the planning, execution, and payment responsibilities.

Sales

Stage

## From/To

Planning and

Settlement

Billed By

Billed To

## Reason

Organization

(Company

Code) (FWO

Export/Import)

Execution

## Type

Organization

(Company

Code)

Nuremberg

Pre-carriage

Nuremberg to

Nuremberg

Forwarding

Nuremberg

## Shipper

(0001) (Export

Hamburg

(0001)

settlement

Nuremberg

recovers the

This is custom documentation. For more information, please visit SAP Help Portal.

39


1/14/26, 2:17 PM

Sales

Stage

## From/To

Planning and

Settlement

Billed By

Billed To

## Reason

Organization

(Company

Code) (FWO

Export/Import)

FWO)

Execution

## Type

Organization

(Company

Code)

cost of the

pre-carriage

from the

shipper.

Nuremberg

Main carriage

Hamburg to

Hamburg

Internal

Hamburg

Nuremberg

## Hamburg

(0001) (Export

FWO)

New York

(0002)

settlement

(0001)

0002 pays for

the main

carriage and

recovers this

cost from

Nuremberg

0001.

Nuremberg

Main carriage

Hamburg to

Nuremberg

Forwarding

Nuremberg

New York

## Nuremberg

(0001) (Export

FWO)

New York

(0001)

settlement

(0001)

(0003)

0001 sends a

forwarding

settlement to

New York

0003 to

recover its

costs.

New York

Main and On-

Hamburg to

New York

Forwarding

## New York

ship-to party

## New York

(0003) (Import

carriage

New York

(0003)

settlement

FWO)

New York to

ship-to party

0003 bills the

ship-to party

for the main

carriage and

on-carriage.

In the export forwarding order, the planned revenue for the Nuremberg sales organization is as follows:

Charge in the forwarding order for the shipper for the execution of the pre-carriage. This is driven by the FOB Incoterms

that the Nuremberg sales organization has for the shipper.

Charge in the forwarding order for the destination organization, to recover the cost of the main carriage and any other

charges at the origin or destination due back to the origin organization. The import organization recovers these charges

from the ship-to party (customer) because of the FOB Incoterms.

The planned costs for the Nuremberg sales organization are as follows:

Cost of pre-carriage

## Cost of main carriage

The system retrieves the planned cost as follows:

1. From the internal charge calculation for the pre-carriage and main carriage.

2. From the cost distribution of the charge calculation in the freight orders and freight bookings that are in place to execute

the pre-carriage and main carriage.

This is custom documentation. For more information, please visit SAP Help Portal.

40


1/14/26, 2:17 PM

For example, the system gets the cost of the main carriage from the purchasing organization in the freight booking. The

purchasing organization in the freight booking belongs to the same company code as the sales organization in the

forwarding order. This is an intracompany scenario, where the cost and the revenue are in the same organization in your

company. For example, your company is located in Germany. Your sales organization is in Nuremberg and you also have a

forwarding house in Hamburg. The forwarding house acts as a purchasing organization, and buys ocean carrier services.

The system determines the costs as follows:

If you do not enable intracompany settlement in Germany, the system uses the distributed cost in the freight

booking at forwarding order level as the cost for the forwarding order.

If you enable intracompany settlement in Germany, the system uses the internal charges in the forwarding order

that is in place between the purchasing organization in the freight booking (Hamburg) and the sales organization in

the forwarding order (Nuremberg) as the cost for the main carriage.

Alternatively, the purchasing organization in the freight booking belongs to a different company code than the sales

organization in the forwarding order. This is an intercompany scenario, where the cost and revenue are in different

organizations in your company. For example, your company in Germany has a sales organization in Nuremberg. You have a

forwarding house in Rotterdam, The Netherlands. The forwarding house acts as a purchasing organization, and buys ocean

carrier services from the port of Rotterdam. The forwarding house in Rotterdam services shipments routed from Germany

to Rotterdam. The forwarding house uses the internal settlement process to settle internally with the sales organization in

Nuremberg. The system gets the cost of the main carriage from the internal charge calculation for the main carriage, in the

internal settlement document.

The following table describes the profitability calculation.

## Source

Planned Revenue (EUR)

Planned Cost (EUR)

Planned Profitability (EUR)

None

None

400

1200

None

None

None

## None

Charge for shipper in forwarding

500

order

Charge for import organization

1500

in forwarding order

Cost of pre-carriage (charge in

## None

freight order for pre-carriage)

Cost of main carriage (charge in

## None

freight booking for main

carriage)

This includes the distributed

cost from the freight booking

when you have not enabled

intracompany settlement, as in

this example. For more

information about

intracompany settlements, see

Internal Settlement.

Total

2000

1600

400

Some additional costs are incurred during execution, and these are included in the respective settlements. For example, a

demurrage cost of EUR 50 is incurred at the pick-up location and is billed to the shipper.

The system retrieves the expected profitability from the settlement documents. The following table describes the expected

profitability for the forwarding order.

This is custom documentation. For more information, please visit SAP Help Portal.

41


1/14/26, 2:17 PM

## Source

Expected Revenue (EUR)

Expected Cost (EUR)

Expected Profitability (EUR)

Settlement for shipper

500 + 50 = 550

Invoice for the main carriage for

1500

the import organization

None

## None

Freight settlement document

## None

400 + 50 = 450

for freight order

Freight settlement document

## None

for freight booking

Total

2050

1200

1650

None

None

None

None

400

Confirmation and Completion of a Forwarding Order

## Use

After you have created and edited a forwarding order in Transportation Management (TM), you can confirm the data to the

ordering party. You can execute the confirmation based on the following data:

Data communicated by the ordering party

Data entered manually or edited

Data planned by the system

## Prerequisites

See Creation of a Forwarding Order.

In particular, you have defined the default confirmation type in Customizing for the document type, in other words, you have

defined which data the confirmation to the customer is to be based upon. You have also defined whether the confirmation is to

occur automatically upon saving. For more information, see Customizing for Transportation Management under  Forwarding

Order Management

## Forwarding Order

 Define Forwarding Order Types .

## Process

The following section contains a description of an example process for forwarding order confirmation:

1. Manual Confirmation

If the confirmation was not already sent to the ordering party automatically upon saving the forwarding order as according

to the Customizing settings, you confirm the order manually. You have the following options:

If you have specified in Customizing that the confirmation is to occur based on the ordering party data or the

planning data, choose Confirm and have the system enter the dates/times and quantities in the confirmation fields

of the forwarding order according to the Customizing settings. You can also enter the dates manually and overwrite

the Customizing settings.

If you have specified in Customizing that the confirmation is to take place based on the manually entered data, enter

the dates/times and quantities in the fields for confirmation of the forwarding order and choose Confirm.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

42


1/14/26, 2:17 PM

If you have configured Customizing so that the confirmation occurs based on the planning data, a confirmation is only

possible if complete planning data is available for the forwarding order. This means that the planning status of the

forwarding order must be Planned.

2. Sending and Printing the Confirmation

The system automatically sends the confirmation to the ordering party. The sending type (for example, fax, e-mail) depends

on your Customizing settings. You can also print out the forwarding order confirmation as a document. In the output

history, you can display which confirmation documents were already printed or sent.

3. Changes After the Confirmation

You can still make changes to the forwarding order even if you have already sent a confirmation to the ordering party. The

status of the order changes back to Not Confirmed, and you have to repeat the confirmation.

For more information about the effects of changes to the forwarding order on subsequent planning processes, see

Processing of Changes and Deletion of Forwarding Orders.

4. Completing the Forwarding Order

The system only assigns the status Completed to the forwarding order if the associated freight orders have been executed.

If you have allowed the invoicing of the forwarding order in the Customizing settings for the forwarding order type, the

invoicing must also have been completed. In this Customizing activity, you can also specify whether the instructions for the

forwarding order must also have been completed before the entire order can be completed.

Once a forwarding order has been assigned the status Completed, you can reopen it if you have the appropriate

authorization. This may be necessary if, for example, you want to add subsequent costs or attach documents. The life cycle

status changes temporarily to Determination Pending. Depending on the changes you have made, once the order has been

saved the status changes back to In Execution, Partially Invoiced, or Completed.

5. Archiving the Forwarding Order

Once the forwarding order has been closed or canceled, you can archive this business document. For more information, see

Archiving Business Documents for Forwarding Order Management (TM-FWM).

## More Information

## Confirmation of Forwarding Orders

Creation of a Forwarding Order for Rail Transportation

## Use

Transportation Management (TM) supports processes in which goods are transported by rail from a shipper to a consignee. The

goods can be shipped from a source rail station, through intermediate rail stations, to a destination rail station (and can also be

combined with pre-carriage and on-carriage stages by road). Different carriers can be responsible for execution and settlement on

the different stages of the transportation process. The system therefore supports the transportation of full carloads and unit

trains, as well as individual cargo items.

As a rail company or rail carrier transporting goods for your customers by rail, you can use forwarding order management in TM to

create a forwarding order for rail transportation. In the process description below, which shows how to create and edit a rail

forwarding order, rail companies and rail carriers are both referred to as carriers.

## Prerequisites

This is custom documentation. For more information, please visit SAP Help Portal.

43


1/14/26, 2:17 PM

You have configured the general settings for a forwarding order. For more information, see Settings for the Forwarding Order.

You have also configured the following settings that are particular to the rail transportation process:

You have defined the shipping type in Customizing. The following shipping types are available for rail transportation:

Carload: The shipper transfers an entire railcar to the carrier.

Intermodal Rail: The shipper transfers individual cargo items to the carrier, for example, containers, products, and

trailers.

Unit Train: The shipper transfers an entire train to the carrier.

You assign the shipping type to the transportation mode Rail. You can also specify that a cargo item in the item hierarchy is

always to be assigned to a railcar.

For more information, see Customizing for Transportation Management under  Forwarding Order Management

## Define

Shipping Types .

You have defined an item type in Customizing. You assign the item category Passive Vehicle Resource and the resource

class Railcar or Trailer to this item type.

For more information, see Customizing for Transportation Management under  Forwarding Order Management

## Define

Item Types for Forwarding Order Management

.

If you want to use vehicle groups and vehicle types, you have defined them in Customizing and assigned them to your item

type. You can define your vehicle resources such as railcars and trailers in the master data as resources with the necessary

details. Alternatively, you can also define a vehicle group and type for railcars and trailers that contains only general

information about these vehicles.

For more information, see Customizing for Transportation Management under  Master Data

 Resources

## Define

Equipment Groups and Equipment Types .

If you want to use a default route, you have defined it in the Create Default Route app on the launchpad under Master Data.

For more information, see Default Route.

If you want the system to create railcar units automatically, you have defined a transportation unit type in Customizing and

assigned it to your freight unit building rule. For more information, see Customizing for Transportation Management under

## Planning

## Transportation Unit

 Define Transportation Unit Types  and under Freight Unit Building Rule.

## Process

The following section describes the special aspects of creating and editing a rail forwarding order. For more information about the

standard process, see Creation of a Forwarding Order and Editing of a Forwarding Order.

1. Entering the Data on the Initial Screen

On the initial screen of the forwarding order, you enter the basic data for the forwarding order. You enter Rail as the

transportation mode and define a rail-specific means shipping type such as Carload. The user interface for the forwarding

order dynamically adjusts to meet the requirements of a rail forwarding order based on the transportation mode.

You can also enter a default route at this stage that you have defined in the master data. If you want to create the

forwarding order with a reference to the item of a forwarding agreement (FWA), you can select a default route that was

defined for the FWA item. The system then takes into account the default route when it creates the transportation stages

for the required route. The carrier data is also copied to the required route.

If you enter an FWA item as a reference, the system uses it to determine the agreed services and charges.

2. Entering General Forwarding Order Data, Locations, and Dates

This is custom documentation. For more information, please visit SAP Help Portal.

44


1/14/26, 2:17 PM

You enter the data that you have received from the ordering party using the standard process. As the locations, you enter

the source and destination rail stations.

3. Creating the Order Items

Depending on your Customizing settings, you can create a hierarchy consisting of railcar items and cargo items in the item

table of the forwarding order. By combining the shipping type and the item types of the individual items in the forwarding

order, you can specify that the railcar must be at the top level of the item hierarchy (shipping type Carload) or that the

cargo items have to be on the top level (Intermodal Transport).

Your Customizing settings also determine the options that you have for entering information about your vehicles such as

railcars:

If you have defined a vehicle resource in the master data, the detail data for the resource is displayed in the item

details of the forwarding order.

If you have defined a vehicle group and type in Customizing and assigned them to the item type, this data is

displayed in the details for the items created with the corresponding item type.

You can enter the vehicle group and type directly in the item details of the forwarding order.

4. Determination of the Route

If you have entered a default route, the route is displayed on the Ordered Route tab page. Otherwise, you can enter the

stages of the route with the source and destination rail stations. If the stages are to be executed or settled by different

carriers, you can enter the executing carrier and the invoicing carrier in each case. You can also enter the external

forwarding agreement for the invoicing carrier.

You can manually enter the train number for the relevant stages in the actual route. If you assign a schedule that contains a

train number to a stage, the system automatically transfers the train number to the stage. In this case, the train number is

read-only in the forwarding order. The train number is propagated to the freight unit, but not to the freight order. However, if

you specify a train number when you create the freight order, the system displays the train number from the freight order in

the forwarding order.

5. Creation of Railcar Units

If you have defined a transportation unit type in your freight unit building rule, the system creates railcar units instead of

freight units. For more information, see Creation and Editing of Freight Units and Railcar Unit.

6. Manual Transportation Planning

You plan the transportation as described in the standard process.

7. Exchange of Information Regarding Processing Progress

If other carriers are involved in the transportation process, you inform them of the transportation services that you are to

provide. You can also inform each other about the processing progress.

8. Creating a Forwarding Settlement Document

According to the process that you have agreed with the ordering party and any other carriers involved, you have the

following settlement options:

All of the carriers involved in the transportation process invoice their transportation stages separately to the

ordering party (for example, the rule 11 scenario in North America).

You carry out the settlement process with the ordering party for the entire route. If necessary, the other carriers

settle their stages with you. The system creates a forwarding settlement document for the entire forwarding order.

Some stages of the route are invoiced to the ordering party by the executing carrier, while other stages are invoiced

to the ordering party by one of the carriers on behalf of several executing carriers. This is a mixed settlement

scenario.

This is custom documentation. For more information, please visit SAP Help Portal.

45


1/14/26, 2:17 PM

For more information see Forwarding Settlement.

## More Information

For more information about a typical rail transportation process from the perspective of the shipper, see Rail Transportation.

Direct Creation of Capacity Documents and Selection of
Schedules

## Use

When you create a forwarding order in Transportation Management (TM), you can already create capacity documents, such as

freight orders, freight bookings, or transportation units, for the transportation stages defined in this document. You can also select

existing capacity documents and schedules (departures).

You can only use these functions for stages of the actual route, that is, not for stages of the ordered route.

You can also create and select capacity documents directly from freight units and transportation units.

## Prerequisites

You have defined default capacity document types for stages in Customizing. This means that you have specified which

type of capacity documents are to be created when you create capacity documents directly from the stage view of a

forwarding order, a freight unit, or a transportation unit.

In this Customizing activity, you can also restrict which activities are to be possible from the user interface of the

forwarding order (for example, selection of schedules).

For more information, see Customizing for Transportation Management under  Forwarding Order Management

## Forwarding Order

 Define Default Capacity Document Types for Stages .

If you want default routes and schedules to be considered during the creation of capacity documents, you have specified

this in advance. For more information, see Schedule.

## Features

## Creation and Selection of Capacity Documents

On the Actual Route tab page of a forwarding order, you can create freight orders or freight bookings for the stages defined for the

route, depending on the transportation mode. You can also select and assign a freight booking or freight order that already exists.

Furthermore, you can create and select transportation units such as container units or package units.

If you create a capacity document from a forwarding order and have not defined a standard capacity document type in

Customizing, a dialog box appears in which you can enter the required capacity document type. The system takes into account the

planning profile that you specified in Customizing for the transportation unit type and freight unit type of the transportation units

and freight units that are assigned to your forwarding order. If there is no planning profile or if the planning profile does not contain

a standard capacity document type, the system takes the standard profile into account.

If a default route already exists for a stage, a capacity document cannot be created directly. In this case, you can select schedules

for the stages of the default route. You can then create capacity documents for the stages of the actual route that were created

based on the default route.

This is custom documentation. For more information, please visit SAP Help Portal.

46


1/14/26, 2:17 PM

Once you have created the capacity document, the document ID is displayed as a link. You can then navigate to the document.

## Creation of a Capacity Document for Several Stages

You can also create a capacity document for several consecutive stages or for stages of different freight or transportation units.

This means that you can group several main carriage stages in a freight booking, for example.

The system first determines the capacity document type from your Customizing settings. The system then creates a freight order,

a freight booking, or a transportation unit with this document type, depending on the transportation mode. The following

prerequisites apply:

A capacity document type must be defined for each stage selected.

If you are creating freight orders, all selected stages must have the same freight order type.

If you are creating freight bookings, all selected main carriages must have the same freight booking type and the same

transportation mode.

The following relevant data for the stage must be the same (or may not be defined):

Carrier

## Voyage

## Name of vessel

The status of the stages must be Unplanned.

If you create a freight booking for several stages, you can change the freight document type that has been determined and, for

example, choose document types with corresponding service levels at the port of loading and port of discharge.

## Selection of a Schedule

You can select schedules that already exist for the stages of a forwarding order. If a default route exists, only the schedules that are

available for the stages of this route are displayed. If fixed schedules are assigned to the default route, only the options for these

schedules are displayed.

Once you have selected a schedule option, the data of the schedule is copied to your actual route. If the default route contains

additional stages, they are also copied to the actual route.

If you have entered locations for transportation zones in the master data and use these zones in the default route instead of

locations, the system takes them into account when it calculates the default route for the forwarding order.

## Remove Assignment of a Capacity Document

You can also remove a capacity document that you have created for one or several stages or assigned to the stage. In this case you

unassign it. The link to the capacity document is removed from the stage view.

If so defined in Customizing for the freight order type, the freight booking type, or the transportation unit type, the capacity

document is canceled or deleted from the system once it has been unassigned.

## Activities

If you want to create or select capacity documents for a forwarding order, open the Forwarding Orders - Worklist or Edit

Forwarding Order app on the launchpad. Open your forwarding order and select the Actual Route tab page.

If you want to create or select capacity documents for a transportation unit, open the Container Units - Worklist or Edit

Container Unit app on the launchpad. Open your transportation unit and select the Stages tab page.

This is custom documentation. For more information, please visit SAP Help Portal.

47


1/14/26, 2:17 PM

Depending on the function you require, you select one or several stages and choose  Capacity Document

 Create One for

Consecutive Stages  or  Capacity Document

## Select

, for example.

The system creates a capacity document of the type that you specified in Customizing. For example, if you have defined

that a freight booking is created for a transportation stage of the type main carriage with the transportation mode sea, the

system takes this into account.

If you want to select a schedule or remove the assignment, select the stage and choose the corresponding pushbutton. You

can also remove the assignment of several stages to a capacity document by selecting one or more of the assigned stages

and choosing  Capacity Document

 Remove  or Remove for This Stage and Following Stages. If you have only selected

one of the stages, the system will ask if you want to remove the assignment of all stages. Only this variant is possible.

## More Information

Direct Creation of Freight Orders (detailed information specific to freight orders)

## Determination of the Route

For more information about the interaction of the default route and the determination of transportation distance and

transportation duration, see Determination of Transportation Distance and Transportation Duration.

Forwarding Quotation

## Definition

Quotation from a carrier or logistics service provider to an ordering party with respect to the transportation of goods, which

contains information about the price and further conditions regarding the transportation services.

## Use

In Transportation Management (TM), the business document of the forwarding quotation serves to help the ordering party send

the data of a potential forwarding order with the quotation price. When the ordering party places the order, you can then create a

forwarding order in relation to the quotation.

Based on the forwarding quotation, you can have the system determine and define the route and calculate the transportation

charges.

## Structure

The forwarding quotation has a similar structure as the forwarding order, since it is the basis for the eventual forwarding order (see

Forwarding Order). In addition, you can enter the following data:

## Validity Scope for the Quotation

When creating the forwarding order based on this quotation, the system checks whether the quotation is still valid.

## Quotation Price

Here you can enter a total price for the quotation, without specifying the transportation charges in detail. If you specify

transportation charges, the system displays the total here in addition. You should note that the display of the quotation

price is determined according to the calculation level that you have defined in the calculation profile. The quotation price is

not displayed if you have defined a calculation at stage level in the calculation profile.

This is custom documentation. For more information, please visit SAP Help Portal.

48


1/14/26, 2:17 PM

## Status of the Forwarding Quotation

The statuses of the forwarding quotation represent for the most part those of the forwarding order (see Status of a Forwarding

Order). Only the values of the life cycle status that are described below differ from those of the forwarding order. Some statuses for

the forwarding quotation, which refer to planning and execution, have been removed.

Life Cycle Status

Status

## New

## Description

The forwarding quotation was newly created and not yet sent.

## Not Transferred

The forwarding quotation that was already sent to the ordering party was changed. The changes were not yet

sent.

## Transferred

The forwarding quotation was sent to the ordering party.

## Canceled

The forwarding quotation was canceled.

## Locking the Forwarding Quotation

In addition to the forwarding order statuses described above, the system displays the locking status for this quotation. You can set

the lock manually or have the system set it automatically. The system sets automatic locks when executing the approval workflow

or during the dangerous goods check, for example. The reason for the lock is also displayed for the lock status. If you set the lock

manually, you can use the value help to select the reason for the lock.

## Integration

The business document for the forwarding quotation is integrated with the following business document in TM:

## Forwarding Order

You can convert a forwarding quotation that you had sent to an ordering party and which was accepted by this ordering

party into a forwarding order, in other words, you create a forwarding order with reference to this quotation.

## More Information

Creation and Editing of a Forwarding Quotation

Creation and Editing of a Forwarding Quotation

## Use

You can use a forwarding quotation (see Forwarding Quotation) in Transportation Management (TM) to send an offer to your

ordering party. You can have the system determine possible routes and calculate the transportation charges based on the selected

route. You can send the quotation containing the transportation charge information to your ordering party via e-mail or fax, for

example.

After the ordering party has accepted the quotation, you can create a forwarding order based on it. You can also subsequently

assign a forwarding quotation to a forwarding order. However, this is subject to certain prerequisites such as corresponding data.

For more information, see Subsequent Assignment of Forwarding Quotations.

This is custom documentation. For more information, please visit SAP Help Portal.

49


1/14/26, 2:17 PM

You can create the forwarding quotation manually. If you receive a forwarding request for quotation electronically (for example,

within the tendering process), you can have the system create the forwarding quotation automatically based on the request for

quotation. For more information about the tendering process, see Freight Tendering.

## Prerequisites

The same prerequisites apply for creating a forwarding quotation as for creating a forwarding order, especially if you later want to

create a forwarding order based on the forwarding quotation. For more information, see Settings for the Forwarding Order.

Alternatively or in addition to the forwarding order type, you must also define the forwarding quotation type in Customizing. You

use this document type to determine a series of characteristics for the forwarding quotation and can make certain default settings.

For example, you can predefine the sales organization or determine how many forwarding orders are allowed to be created based

on a forwarding quotation of this type. Moreover, you can specify whether the forwarding quotation of this type is based on a

forwarding request for quotation (quotation mode)

For more information, see Customizing for Transportation Management under  Forwarding Order Management

 Forwarding

## Quotation

 Define Forwarding Quotation Types .

  Note

If you later want to create a forwarding order based on a forwarding quotation and predefine the shipping type and the

transportation mode in Customizing for the forwarding quotation type, these settings must be the same as those in the

forwarding order type.

If you want to specify reasons for the rejection or cancellation of a forwarding quotation, you have defined them in Customizing.

For more information, see Customizing for Transportation Management under the following Customizing activities:

Basic Functions

## General Settings

## Define Rejection Reason Codes

Forwarding Order ManagementDefine Cancellation Reason Codes

## Process

1. Entering the Data on the Initial Screen, the General Data, and the Quotation Items

Since the forwarding quotation can be the basis for a forwarding order, the data structure and user interface for creating

the quotation data is similar to that of the forwarding order. In addition, you can determine the validity scope of the

quotation.

For more information, see Creation of a Forwarding Order and Creation of Forwarding Order Items or Forwarding Quotation

Items.

If you have received a forwarding request for quotation from your ordering party, the forwarding quotation is automatically

created based on this request and the data it contains. It is displayed in your personal object worklist (POWL), from where

you can access and edit it.

2. Saving the Forwarding Quotation

If the forwarding quotation was not created automatically, save it. The system now assigns the document an ID from the

number range for this document type. In addition, the system checks the entered data for completeness and consistency.

The system displays the results of these checks in the form of error messages and as a completeness status.

If so defined in Customizing for the forwarding quotation type, the system automatically determines the transportation

charges after saving.

3. Determining the Route

This is custom documentation. For more information, please visit SAP Help Portal.

50


1/14/26, 2:17 PM

If you have already received information about the ordered route from the ordering party, you can create the stages of the

route. For more information, see Determination of the Route.

4. Calculating Transportation Charges

If this has not occurred automatically after saving, you can have the system calculate the transportation charges or you can

enter them manually. The sum of transportation charges is displayed as quotation price. Instead of entering the

transportation charges, you can also specify only the sum of the charges as the quotation price. For more information, see

Charge Calculation.

If you quickly want to estimate the transportation charges based on a minimum of data, you can use the Estimate

Forwarding Charges function to do so. For more information, see Charge Estimation.

5. Sending the Quotation to the Ordering Party and Printing the Document

You can send the forwarding quotation to your ordering party and print out the document immediately or after previewing

it. The sending type (for example, fax, e-mail) depends on your Customizing settings. If you have created the quotation

based on a request from your ordering party, you can dispense with this step.

The history of sending and printing quotation documents is displayed in the forwarding quotation on the Output

Management tab. For more information, see Output Management.

6. Accepting or Rejecting a Quotation

If your ordering party has already informed you whether he agrees with the quotation, or if the quotation is based on a

forwarding request for quotation from your ordering party, you can can accept or reject the forwarding quotation. If you

reject it, you can also specify a rejection reason code. The quotation is then automatically cancelled.

The corresponding response code and if necessary reason rejection code is displayed in the General Data area of the

forwarding quotation.

7. Creating the Forwarding Order Based on the Quotation, or Canceling the Quotation

Depending on whether your ordering party has accepted or rejected the quotation, or whether you accept the conditions of

your ordering party contained in the forwarding request for quotation, you can proceed as follows:

You create a forwarding order based on the forwarding quotation, in other words, you create a forwarding order

based on the data in the quotation. When you do so, the system also copies the route data and the price calculation

from the quotation. The system also checks whether the quotation is still valid. For more information, see Creation

of a Forwarding Order.

You can also receive a forwarding order based on a forwarding quotation electronically (EDI).

You cancel the quotation. The life cycle status changes to Canceled. Depending on your Customizing settings, you

can enter a cancellation reason that is displayed in the General Data area of the forwarding quotation.

Note that the cancellation is irreversible.

If you have specified in Customizing for the document type how many forwarding orders are allowed to be created from this

forwarding quotation, the system checks this when you create a forwarding order.

8. Archiving the Forwarding Quotation

After the forwarding order has been canceled or if it is no longer valid, you can archive the business document. For more

information, see Archiving Business Documents for Forwarding Order Management (TM-FWM).

Subsequent Assignment of Forwarding Quotations

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

51


1/14/26, 2:17 PM

If you follow the standard process in Transportation Management (TM), you create a forwarding order with reference to an existing

forwarding quotation (FWQ). However, you can also assign forwarding quotations to a forwarding order later. For example, you can

create a forwarding order even if the corresponding forwarding quotation does not exist at that time.

The transportation charges entered in the forwarding quotation can be copied automatically to the forwarding order.

Transportation charges that already exist in the forwarding order can be overwritten by the system.

## Prerequisites

If you want to assign a forwarding quotation to a forwarding order subsequently, certain prerequisites must be fulfilled, which are

checked by the system. When doing this, the system differentiates between hard and soft constraints. If these constrains are not

fulfilled, the system proceeds as follows:

## Hard Constraints

The forwarding quotation cannot be assigned. These constraints are implemented as standard in TM. They cannot be

changed.

## Soft Constraints

The forwarding quotation can be assigned, but the system does not copy the transportation charges to the forwarding

order.

You can use a Business Add-In (BAdI) to enhance these constraints. You can also replace the soft constraints with other

constraints. For more information, see Customizing for Transportation Management under  Business Add-Ins (BAdIs) for

Transportation Management

## Forwarding Order Management

 Assignment of Forwarding Quotation to Forwarding Order

.

## Features

## Hard Constraints

The system checks the following constraints:

Forwarding order:

No forwarding settlement document has been assigned to the forwarding order as yet.

Forwarding quotation:

The forwarding quotation is valid and has been submitted (in other words it has the status Submitted).

The forwarding quotation is not subject to a quotation block.

The forwarding quotation can be assigned to another forwarding order.

This constraint relates to a Customizing setting with which you can restrict the number of forwarding orders that

can be created based on one forwarding quotation. For more information, see Customizing for Transportation

Management under  Forwarding Order Management

 Forwarding Quotation

 Define Forwarding Quotation

Types .

Matching data:

The following data in the forwarding quotation and the forwarding order must match:

Forwarding agreement

## Traffic direction

Air waybill type (AWB type)

This is custom documentation. For more information, please visit SAP Help Portal.

52


1/14/26, 2:17 PM

## Shipper and consignee

Source location and destination location

## Soft Constraints

The system checks whether the following data matches in the forwarding quotation and the forwarding order:

## Sales organization and ordering party

Additional forwarding agreement (import or export forwarding agreement)

Incoterm data (Incoterm and free text for Incoterm location)

Service level, transportation mode, shipping type, and movement type

Amounts and quantities in the header data, for example high-value cargo

Pick-up and delivery date in the header data

## Dangerous goods indicator

In addition, certain items or stages in the forwarding quotation for which transportation charges have already been calculated

must exist in the forwarding order. Otherwise the system cannot copy the transportation charges from the forwarding quotation to

the forwarding order.

## Messages, Status Updates, and Options

The system displays the check results as system messages. In addition, it displays the status of the assignment on the Status tab

of the forwarding order as follows:

## Status

## No FWQ Assigned

FWQ Subsequently Assigned

## Description

No forwarding quotations have been assigned to the forwarding

order; this is the initial status.

A forwarding quotation was assigned to the forwarding order

subsequently, in other words after the forwarding order was

created; the hard checks were successful; existing transportation

charges from the forwarding quotation have been copied to the

forwarding order.

FWQ Subsequently Assigned; Soft Check Failed

A forwarding quotation was assigned to the forwarding order

subsequently; the soft checks were unsuccessful; any existing

transportation charges were not copied to the forwarding order.

## FWO Created from FWQ

The forwarding order was created based on a forwarding quotation,

either manually or using EDI.

If the soft check fails, you have the following options:

You can change the data of the forwarding quotation or forwarding order in such a way that the prerequisites are fulfilled.

Then you can run another check. This does not change the status.

You can copy the transportation charges from the forwarding quotation to the forwarding order. The status then changes to

FWQ Subsequently Assigned.

## Activities

This is custom documentation. For more information, please visit SAP Help Portal.

53


1/14/26, 2:17 PM

You can subsequently assign a forwarding quotation to a forwarding order as follows:

From the user interface of the forwarding order, by choosing  Forwarding Quotation

## Assign FWQ

From your personal worklist (POWL) (same navigation path)

In the POWL you can also find forwarding orders with assigned forwarding quotation based on their status.

If you want to recheck the prerequisites or subsequently copy the transportation charges, choose  Forwarding Quotation

 Recheck Constraints , or  Forwarding Quotation

 Copy Transportation Charges .

If you want to replace an assigned forwarding quotation by another one, you can assign the new forwarding quotation as described

above, by choosing  Forwarding Quotation

 Assign FWQ .

  Note

If transportation charges already exist in the forwarding order, the system asks if you want to overwrite them. The

forwarding quotation is only assigned to the forwarding order if you agree to this.

The transportation charges copied to the forwarding order are fixed.

## More Information

Creation and Editing of a Forwarding Quotation

## Creation of a Forwarding Order

Creation of Forwarding Order Items or Forwarding Quotation
Items

## Use

When you create a forwarding order or a forwarding quotation in Transportation Management (TM), you can enter the items of this

business document in an item hierarchy. The hierarchy can contain the following levels:

Railcar

Trailer

Container

Package

Product

## Service

The planning always occurs on the highest level, for example, on the level of the container or package. Information about the

packages in a container or the products contained in a package is additional information for the planner, and does not play an

essential role in the planning by the system. This information does, however, have an impact on a potential transportation charge

calculation. This is also valid for service items.

## Prerequisites

This is custom documentation. For more information, please visit SAP Help Portal.

54


1/14/26, 2:17 PM

If you want to provide information about railcars, trailers, or containers when creating the order items, you have defined

equipment groups and types as well as ventilation settings in Customizing. You can define transportation mode-specific

equipment groups and equipment types, for example, for sea freight containers and unit load devices (ULDs). You can also

enter information about packages by defining package types.

This data serves as additional information for the planner and is not relevant for the planning by the system. For more

information, see Customizing for Transportation Management under the following Customizing activities:

Master Data

## Resources

 Define Equipment Groups and Equipment Types

Forwarding Order Management

 Define Package Type Codes

General Settings for Order Management

## Define Ventilation Settings

In Customizing, you have specified item types and assigned them to document types. You can use the item type to

predefine various parameters for an item, such as the item category, equipment group and equipment type, as well as

default units of measure. Additionally, you can already assign a dangerous goods UI profile, with which you can make

settings for the display of dangerous goods information for items.

Assigning item types to document types allows you to specify which item types are allowed for a document type. You can

also specify a default item type for items with a certain item category that are created for a document with a certain

document type.

The default item type is used when forwarding orders and forwarding quotations are received electronically. If you create

items manually and have only defined one default item type for a combination of the item category and document type, the

system enters the item type automatically.

You can also define that the system automatically creates initial items using specified item types when you manually create

a forwarding order or forwarding quotation.

For more information, see Customizing for Transportation Management under the following Customizing activities:

Forwarding Order Management

## Define Item Types

Forwarding Order Management

## Forwarding Order

 Assign Item Types to Forwarding Order Types

Forwarding Order Management

## Forwarding Quotation

## Assign Item Types to Forwarding Quotation Types

If you want to use railcars or trailers in your item hierarchy, you have assigned the item category Passive Vehicle Resource

to your item type along with resource class Railcar or Trailer.

If you have defined the item type for the Service item category, and you want to assign service types to the service items,

you have defined service types in Customizing. For more information, see Customizing for Transportation Management

under  Basic Functions

 General Settings

 Define Service Types .

You have defined shipping types in Customizing. For the shipping type, you have specified whether cargo items such as

containers, packages, and products can or must be assigned to equipment items such as railcars. For more information,

see Customizing for Transportation Management under  Forwarding Order Management

 Define Shipping Types .

If you want to use commodity codes to classify goods, you have made settings in Customizing for Transportation

Management under  Master Data

 Classification of Goods . For more information, see Classification of Goods.

If you want to define that you can specify locations and business partners for an item that differ from the header data in

the forwarding order, you have defined this accordingly in Customizing for the forwarding order type or the forwarding

quotation type. The default setting is that you cannot specify locations and business partners that differ from the header

data. For more information, see the Customizing activities mentioned above.

## Features

You can create items in the forwarding order and forwarding quotation business documents as follows:

This is custom documentation. For more information, please visit SAP Help Portal.

55


1/14/26, 2:17 PM

## Item Hierarchy

You can create the items individually or as a hierarchy consisting of the levels railcar, trailer, container, package, product,

and service. The sequence of the levels is predefined, in other words, you cannot define a product as highest level with a

lower-level package.

Depending on the Customizing settings for your shipping type that you enter in the forwarding order or forwarding

quotation, you can or must assign cargo items such as containers, packages, and products to equipment items such as

railcars. In this way you can define, for example, that if the shipping type is Carload, the railcar must be at the highest level

in the item hierarchy.

## Item Type

You must enter an item type for each item. If you leave this field empty, a unique default item type for the combination of

the item type (for example, product) and the document type must be defined in Customizing (see above under

Prerequisites). In this case, the system determines the default value from the Customizing settings.

Once you have specified an item type for an item, it cannot be changed.

## Service Items

You can define the services in a service product catalog and include the service products in the forwarding agreements. You

can also include services that are not part of a service product catalog. The services are always assigned to a forwarding

agreement item.

When you specify a reference to a forwarding agreement item in your business document (that is, forwarding quotation or

forwarding order), the system automatically transfers the service items from the forwarding agreement item to the

business document. In the Items screen area on the Service Details tab page, the system sets the corresponding reference

type, that is, Reference to FWA Item or Reference to Additional FWA Item. If required, you can change this to No

Reference. If you delete the reference to the forwarding agreement item, the system sets No Reference for all service

items.

Note the following:

The system transfers services only if they have been flagged as flow services in the forwarding agreement. If a

service is also flagged as mandatory in the forwarding agreement, you cannot subsequently delete this service item

in the business document.

Before the system transfers the services, it checks if the business document already contains non-referenced

service items. If a non-referenced service item in the business document has the same service type as a service item

in the forwarding agreement item, the system reuses the non-referenced service item by setting the relevant

reference type in the service details (for example, Reference to FWA Item). It does not create a new service item in

this case.

If you have defined an item type for the Service item category in Customizing, you can create service items in your

forwarding order or forwarding quotation. You can specify the following features:

Service type, for example, cleaning and fumigating a container. For example, the service type can be assigned to an

instruction set that contains the step-by-step instructions for fumigating a container.

Reference (for example, Reference to FWA Item). You can specify a reference only if there is a service item with the

same service type in the forwarding agreement item.

Service items are used mainly for charge calculation and settlement. However, they are not carried over to follow-up

documents or included in scheduling. On the Charges tab page, you can enter the quantity for a service item below the

main item. The system uses the logistics data of the service item to calculate the charges. If you do not enter the quantity

for the service item, the system calculates the charges based on the quantity that you entered for the higher-level logistics

item.

This is custom documentation. For more information, please visit SAP Help Portal.

56


1/14/26, 2:17 PM

You can also create a forwarding order that contains only service items (for settlement purposes, for example). This means

that the forwarding order does not contain cargo items at the same time.

For more information, see Service Product Catalogs and Management of Instructions.

## Equipment Type

If you have made the corresponding settings in Customizing, you can assign equipment types (for example, freezer

containers and 20-foot containers) as well as package types (for example, pallets) to the items. The following also applies:

If you have assigned an equipment group to the item type in Customizing, it is entered automatically for an item with

this item type and equipment types of this group are displayed for selection. You can, however, overwrite the

equipment group.

If you have specified a default package type and a default equipment type in Customizing for the item type, this is

displayed automatically.

For containers, you can enter data in the detail data, for example, about temperature control. If you have defined

temperature data for this container type in Customizing for the equipment type, the system checks your entries based on

the Customizing data. You can also select ventilation settings that you have predefined in Customizing. This data is

information for the planner.

Furthermore, you can already enter data about seals for the container. This data is then automatically copied to the

successor freight booking or the freight order. For more information, see Use of Seals.

## Commodity Codes

If you have defined these in Customizing, you can assign commodity codes to the items of an air forwarding order or

forwarding quotation. You use these codes to classify and evaluate your goods to be transported (commodities) according

to characteristics of your choice. When classifying goods, you can take into account transportation-relevant product

characteristics, such as weight, density, loading properties, and handling (of dangerous goods, for example). You can use

this information, which is also transferred to follow-on documents such as freight orders or freight bookings, as an

additional description or a basis for decisions about packaging and so on.

For more information, see Classification of Goods.

## Quantities, Weights, and Volumes

You can enter quantity, weight and volume data for the items you entered (except for service items for which you can enter

only quantity data). These are partly aggregated across the different levels of an item hierarchy automatically. In addition,

any discrepancies between the required quantities and actual quantities are displayed. For more information, see Creation

of Quantity, Weight and Volume Data of an Item.

## Automatic Checks

In Customizing you can specify that you want the system to automatically check whether a specific product exists and that

you want the system to automatically calculate the weight and volume of the item based on the quantity and unit of

measure entered in the product master data. You can also specify that the system is to check whether a package exceeds

certain dimensions. If necessary, you can check the dimensions of a package manually. Additionally, a container number

that has been entered is check to see if it meets international standards.

## Copy and Move

You can copy existing items and move items via drag and drop to another position in the item hierarchy.

If you create a forwarding order based on a forwarding quotation, the item types that have been defined are copied to the

forwarding order.

## Splitting Items

This is custom documentation. For more information, please visit SAP Help Portal.

57


1/14/26, 2:17 PM

You can also split items into several items. The number of the split items depends on the number of pieces contained in the

item. A new item is created for each piece. The quantities are also split.

An item can only be split if it meets the following prerequisites:

It has not yet been planned.

It contains more than one piece.

It does not have any subitems.

It is not a service item.

## Locations and Business Partners

If you have not specified otherwise in Customizing, you can define your own source and target locations, pick-up and

delivery dates as well as business partners in the detail data of items or subitems in a forwarding order or forwarding

quotation. The following business scenarios can provide a reason for doing so:

You want to pick up the goods for a forwarding order from different locations or different shippers and transport

them together in a main carriage.

You want to deliver the goods from one forwarding order that you have transport in a main carriage to different

locations or consignees.

A combination of these two scenarios is also possible. Moreover, for business partners, you can enter one-time locations

and one-time addresses that differ from those in the header data in a forwarding order or quotation.

  Note

If you have specified different shippers or consignees for multiple forwarding order items, an automatic

settlement is performed only for those shippers or consignees that you have specified in the header data of the

forwarding order (or for the corresponding prepaid agreement parties and collect agreement parties from the

header data).

You can perform the settlement for the different business partners by creating forwarding settlement documents

manually.

## More Information

## Example for the Creation of Items

Creation of Quantity, Weight and Volume Data of an Item

## Use

When you create a forwarding order or forwarding quotation in Transportation Management (TM), you can create quantity, weight

and volume data for the order items, and have the system calculate the data automatically. The following is a description of the

special features that apply to this.

For more information, see Creation of Forwarding Order Items or Forwarding Quotation Items.

## Prerequisites

This is custom documentation. For more information, please visit SAP Help Portal.

58


1/14/26, 2:17 PM

If required, you have assigned a default unit of measure for weight, volume, and quantity as well as for length, width, and

height in Customizing for the business document type that you created for the forwarding order or forwarding quotation.

The system uses this unit of measure if the following applies:

You have not entered a unit of measure for the item on the user interface

You have not defined a unit of measure in the item type

The system calculates the total quantity of the planning-relevant order items

For more information, see Customizing for Transportation Management under the following Customizing activities:

Forwarding Order Management

## Forwarding Order

 Define Forwarding Order Types

Forwarding Order Management

## Forwarding Quotation

## Define Forwarding Quotation Types

If you want the system to automatically total the gross volume of an item from lower item levels, you can define this in

Customizing. For more information, see Customizing for Transportation Management under  Forwarding Order

## Management

 Define Item Types for Forwarding Order Management

.

If an item has the category Product and this product exists in the product master data, you can specify that you want the

system to automatically calculate the weight and volume of the item based on the quantity and unit of measure entered in

the product master data. To do this, set the Product Check checkbox in Customizing for Transportation Management

under  Forwarding Order Management

 Define Item Types for Forwarding Order Management

.

## Features

## Aggregation of the Data and Automatic Calculations

The quantities, weights and volumes of the planning-relevant items (in other words, the items on the highest level of an item

hierarchy) are totaled by the system and displayed in the base unit of measure in the header data of the document.

However, the totaling is only possible if the units of the items can be converted to the required unit. If this is not the case,

the total stays empty. All other items are additional information and can be included for instance on the print documents as

well.

The quantities and weights of the lower-level items in an item hierarchy are aggregated by the system to the next-higher

level of the hierarchy. In a three-level hierarchy consisting of container, package, and product levels, the system aggregates

the data as follows:

1. If you specify the gross weight on the product level, the system aggregates the data to the net weight of the next-

higher levels, for example of the package level. The net weight is no longer changeable.

2. If you specify on package level the weight of the packaging (tare weight) in addition to the net weight, the system

adds the data to the gross weight of the package.

3. The gross weight of the package is aggregated by the system to the net weight (loading capacity) of the container

and is then no longer changeable. If you additionally specify the tare weight of the container, the system totals the

net weight (loading capacity) and the tare weight to the gross weight (total weight) of the container. The total weight

is likewise no longer changeable. It is also displayed in the document header.

If you have activated this in Customizing of the forwarding order type (see below), the gross volume data of the lower-level

items in an item hierarchy is aggregated by the system to the next-higher level of the hierarchy. Once the value of an item

from lower item levels has been totaled, it can no longer be changed. You can only process the value at higher items levels if

the item does not have any subitems with volume data.

The value in the gross volume field of an item represents either the external volume or the volume of the contents,

depending on the item type. It can be interpreted as follows:

Container or ULD: Gross volume of the contents of a container or ULD

This is custom documentation. For more information, please visit SAP Help Portal.

59


1/14/26, 2:17 PM

Package: Gross volume of the package that, for example, is defined by the external dimensions of the package

(length, width and height)

## Product: Gross volume of the product

After you have entered the equipment group, the equipment type and the number of containers, the system calculates the

tare weight and the capacity of the container in TEU based on the Customizing settings.

If you do not specify a unit of measure, the system determines the default unit of measure from the item type or, if not

available, from the document type (if defined in Customizing).

If you enter the length, height, and width of a package item, the system calculates the gross volume automatically. However,

this is only possible if no volume data from lower item levels has been totaled. In addition, the gross volume field must

either be empty before the calculation, or the value entered in the field must correspond to the product regarding length,

height and width (meaning it has probably already been calculated).

If you enter only the gross weight, the system calculates the net weight and the empty weight. It does so as follows:

Containers and railcars: The system assumes that the gross weight is the same as the empty weight and that the

net weight is 0.

Packages and products: The system assumes that the gross weight is the same as the net weight and that the

empty weight is 0.

## Actual Quantities and Discrepancies

If the actual received quantities for an item have already been entered in the freight document, the cargo receipt status of

the freight document (for example, Delivered) is displayed in the item table. The detailed data for the item then displays the

quantities requested by the ordering party as well as the confirmed actual quantities of the freight document.

If there are discrepancies between the requested and actual quantities, or other discrepancies, this is displayed with a

status in the item table as well as on a separate tab in detail. You can then clarify the discrepancies and set them to solved

for subsequent planning. For more information, see Handling Discrepancies.

Example for the Creation of Items

## Use

The following describes an example of how you can create a hierarchy of items of a forwarding order or forwarding quotation in

Transportation Management (TM). For more information, see Creation of Forwarding Order Items or Forwarding Quotation Items.

Example

Item

Item

Item

Item

## Item

Level 1

Level 2

Level 3

Description

## Type

Package

## Type

Container

Gross

Weight

UoM Net

UoM Tare

Weight

Weight

Container

CN

HJCU4572305

5,900.00 KG

3,900.00 KG

2,000.00

Package

PKG

Europallet

3,900.00 KG

3,650.00

KG

250.00

Product Spare Part

PRD

3,650.00

KG

Container

CN

MWCU6059784

9,800.00 KG

7,800.00

KG

2,000.00

This is custom documentation. For more information, please visit SAP Help Portal.

60


1/14/26, 2:17 PM

Item

Item

Item

Item

## Item

Level 1

Level 2

Level 3

Description

## Type

Package

## Type

Container

Gross

Weight

UoM Net

UoM Tare

Weight

Weight

Package

PKG

Europallet

3,900.00 KG

3,650.00

KG

250.00

Product Spare Part

PRD

3,650.00

KG

Package

PKG

Europallet

3,900.00 KG

3,650.00

KG

250.00

Product Spare Part

PRD

3,650.00

KG

As the table shows, you create two items for containers on the highest hierarchy level. The first container HJCU4572305 has a

subitem on the second hierarchy level with a package of package type Europallet and a subitem on the third hierarchy level with a

product of the description Spare Parts. The second container MWCU6059784 has two subitems on the second level, each with a

package of package type Europallet. Each package has one additional subitem with a product of the description Spare Parts.

For the container MWCU6059784, the system aggregates the weight data as follows:

The container has a gross weight of 9,800 KG. Each package has a gross weight of 3,900 KG. The products each have a

gross weight of 3,650 KG.

The gross weight of the package of 3,900 KG is the sum of the net weight of 3,650 KG aggregated from the product and the

weight of the packaging (tare weight), which is 250 KG. The gross weight of the container of 9,800 KG is the sum of the net

weight of 7,800 KG that was aggregated from the packages and the tare weight of 2,000 KG of the container.

Only the two container items that were defined on the first hierarchy level are relevant for planning. Therefore, 15,700 KG is

displayed in the header data of the forwarding order as the total gross weight of the order (sum of the gross weight of 9,800 KG

and 5,900 KG of both containers). The subitems only serve as additional information, however, they can have an effect on the

calculation of transportation charges.

Handling Discrepancies

## Use

In a forwarding order, you enter the quantities and attributes requested by the ordering party for the items to be transported. When

the actual quantities are reported, there can be discrepancies between them and the requested quantities. You can enter these

quantity discrepancies in the freight document, just as you enter other discrepancies, such as packaging damage or missing

documents. These discrepancies are then also displayed in the forwarding order.

Using the displayed data, you can check discrepancies and, for example, clarify after discussion with the ordering party whether

the discrepancies are acceptable. Then, for further planning, you can set discrepancies to resolved, or block stages of the

forwarding order that were not yet executed.

In addition, you can search for forwarding orders that contain discrepancies. You can also display discrepancies in your personal

object worklist for discrepancies.

## Process

The following example illustrates the process for handling quantity discrepancies and other discrepancies.

1. The employee, who receives the goods, discovers a quantity discrepancy or other discrepancy for an item. This person

enters the discrepancy in the freight order or in the freight booking. For more information see Discrepancies and Events.

This is custom documentation. For more information, please visit SAP Help Portal.

61


1/14/26, 2:17 PM

2. In the forwarding order, the discrepancy is shown by a status in the table of order items (Discrepancy Exists).

3. You display the detail data for the item. Here you can check the actual quantities against the ordered quantities. The system

also displays here whether certain transportation-relevant attributes, such as Overdimensional Cargo or Dangerous

Goods, deviate from the requested data and whether a specific discrepancy needs to be resolved.

4. On the Discrepancies tab page of the detail data, you check the details of the various discrepancies. It is possible that the

discrepancy type, the discrepancy subcategory, and other additional information was entered in the freight document.

5. If your ordering party accepts the discrepancies in quantities and attributes, you can choose  Copy Actual Data

## Copy

Actual Quantities  to copy the actual quantities to the ordered quantities in the item table. You can also copy the actual

attributes in the same way.

If you want to copy to the order data only single items that deviate from the actual data, you can also change the order data

manually.

6. You can set the discrepancy to "Resolved" on the Discrepancies tab page. You can also define an execution block for stages

of the forwarding order that have not been executed yet. If you set the discrepancy to resolved, you indicate to the

subsequent planning stages that no further action is required (for example, if the discrepancy was accepted by the ordering

party). This does not mean that the discrepancy was corrected. For more information, see Resolution of Discrepancies.

  Note

If you want to resolve the discrepancy Missing Cargo and copy the actual data to your order data, you have to set the

discrepancy to "Resolved" first; you can then copy the actual quantities and attributes to your order data. There are

other restrictions that apply to the copying and manual changing of attributes. For more information, see Handling

Discrepancies in Transit Warehousing Process.

After you have set the status Discrepancy Resolved, you can also enter a note for it.

7. The status Discrepancy Resolved that is set in the forwarding order and any additional information you may enter are

displayed in the freight document. The reverse is also true - the forwarding order shows when a discrepancy was already set

to resolved in the freight document.

  Note
You can still change data in the forwarding order after the cargo receipt status has been set to On Hand. However, these

changes are not copied to follow-on documents. If a settlement document has already been created, first you have to cancel

this document, then you can make the changes, and finally you create a new settlement document.

## Search for Forwarding Orders with Discrepancies

If you want to directly process discrepancies in forwarding orders, you can search for forwarding orders with discrepancies in your

personal worklist as an additional process step. That is, you define a query for forwarding orders that have the status Discrepancy

Exists. A forwarding order receives the overall status Discrepancy Exists, if there is a discrepancy for at least one item of the order.

A forwarding order does not receive the status Discrepancy Resolved until all discrepancies that existed are resolved.

You can display the discrepancies together with all the relevant data in your personal object worklist for discrepancies.

Furthermore, you can solve discrepancies directly and access the related documents such as forwarding orders and freight orders.

## More Information

Discrepancies and Events (freight order)

Quantity Discrepancies (freight order)

Other Discrepancies (freight order)

This is custom documentation. For more information, please visit SAP Help Portal.

62


1/14/26, 2:17 PM

## Resolution of Discrepancies

Handling Discrepancies in Transit Warehousing Process (integration with SAP Extended Warehouse Management)

Determination of the Route

## Use

When you create a forwarding order or a forwarding quotation in Transportation Management (TM), you can already specify the

route requested by the ordering party. You can also define the route in more detail manually, as well as edit the requested route.

To do this, you can enter the individual stages of the route in the forwarding order or the forwarding quotation. The system then

considers the route during further transportation planning and settlement. If necessary, you can also have the system determine

the route and then copy the result to your order or quotation. The result of transportation planning done at a later time is also

displayed in the forwarding order.

## Prerequisites

Along with the general settings for a forwarding order or a forwarding quotation, you have made the following settings in

Customizing:

You have defined stage types. In doing so, you define whether a stage is a pre-carriage, main carriage, or on-carriage. This

categorization is required for the processes that follow, such as charge calculation, settlement, and the creation of freight

documents.

You can also define an instruction set in the stage type that contains work instructions for a stage (see Management of

Instructions).

You may have additionally specified which transportation modes are permitted for certain stage types. You can also

define a default transportation mode for a stage type.

You have defined movement types. In doing so, you specify the stages for which the logistics service provider is responsible

as well as which stage types are permitted for a forwarding order or a forwarding quotation.

If required, you have defined how the system determines stages in forwarding orders or forwarding quotations. You have

the following options:

## Determination of stages based on a stage profile

In a stage profile, you define which stage types are permitted and which are required in a forwarding order or a

forwarding quotation, which sequence is to apply to which stage types, and the properties of the stages. This allows

you to define a rule to determine the stages that are relevant for planning, for example.

You can assign the stage profile directly to the forwarding order or forwarding quotation type in Customizing.

Alternatively, you can first create a condition and then assign the stage profile to the condition (condition type

Determine Stage Profile, /SCMTMS/TRQ_STG_PRF). With the condition, you can configure the settings for

determining the stages to allow a flexible combination of movement type, transportation mode, and traffic direction.

## Determination of stages based on the movement type

You define which stage types are permitted and which are required for a specific movement type. As in the stage

profile, you also define the sequence for the stage types and specific properties of the stages. However, in contrast

to the stage profile, the settings only apply to a specific movement type.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

63


1/14/26, 2:17 PM

These Customizing settings are not relevant for stages for empty provisioning items and empty return items. In this

case, there are no restrictions as regards the stage type and stage sequence and the system does not automatically

enter any stages.

For more information, see Customizing for Transportation Management under Forwarding Order Management and the following

Customizing activities:

## Define Stage Types

Define Allowed Transportation Mode for Stage Types

## Define Movement Types

Define Stage Type Sequence for Movement Types

## Define Stage Profiles

In Customizing you have also defined default agreement party types for a combination of the stage type and Incoterm. The

system uses this information to automatically determine agreement parties for stages. For more information, see Customizing for

Transportation Management under  Forwarding Order Management

 Define Default Agreement Party Types for Stages .

If you want to work with Standard Carrier Alpha Codes (SCACs) or Airline Codes for carriers and airlines, you have defined this in

the business partner master data (see Definition of Business Partners). You can also specify SCACs and airline codes in

Customizing for the display in the input help. For more information, see Customizing for Transportation Management under

## Master Data

## Business Partners

 Define Standard Carrier Alpha Codes  and Define IATA Airline Codes.

If required, you have defined a default route in the master data. For more information, see Default Route.

## Features

## Ordered Route

In the forwarding order or forwarding quotation, you can enter the stages of the route requested by the ordering party on the tab

page or in the assignment block entitled Ordered Route. If you have already entered the source and destination locations on the

Locations and Dates/Times tab, this is displayed as a Complete Carriage. If you enter a default route on the initial screen of the

forwarding order or forwarding quotation, or if you select a default route based on a forwarding agreement item, the system

displays the stages from this route.

Otherwise you enter the source and destination locations on the Complete Carriage line of your route. The system then

automatically transfers this data to the general data on the Locations and Dates/Times tab. To create additional transportation

stages for the ordered route, you have the following options:

## As intermediate stages of the complete carriage

If the route only consists up to now of a source location and a destination location and you would like to add an

intermediate location, select the Complete Carriage line and choose Split. The system inserts two additional lines with

stages in the table. The system copies the data for the source location and the dates of the complete carriage for the first

transportation stage, and it leaves the destination location data empty. For the second transportation stage, the system

copies the data of the destination location and leaves the source location data empty.

You can enter the new source location data and the destination location data in the empty fields. If the complete carriage

previously went from location A to location C, you now have, for example, one transportation stage from A to B and another

from B to C.

## As additional stages for existing stages

This is custom documentation. For more information, please visit SAP Help Portal.

64


1/14/26, 2:17 PM

You select the line of an existing stage and choose Split. The system divides this line into two lines and proceeds as

described above.

## Actual Route

## Manual Entry of the Actual Route

You can also enter the actual route separately from or in addition to the route requested by the ordering party on the tab page or in

the assignment block entitled Actual Route. You can also have the system determine the actual route using  Route

## Transportation Proposal

 or select a default route using  Route

 Apply Default Route  and copy it to the table of the stages. If

you copy only the route proposed by the system, you can still make changes later. For you to create the actual route, it is not

necessary for the items and freight units to already exist in your forwarding order or forwarding quotation.

Depending on your Customizing settings as well as the entries made in the header data of the forwarding order or forwarding

quotation, specific data for your stages is already displayed as follows:

## Movement type, traffic direction, and stage profile

You enter the movement type and traffic direction in the header data for the whole business document. You may also have

defined a stage profile with the document type. Depending on your settings for the movement type or in the stage profile,

certain stages of the actual route are determined automatically. Additionally, the stage types that you can enter may be

restricted. Along with the traffic direction (export or import), the movement type also determines the transportation stages

for which you, as the logistics service provider or document processor, are responsible. This is displayed with the Stage

Status.

## Transportation mode

You enter the transportation mode in the header data for the whole business document. However, it only refers to the main

carriage (or the main carriage stages) of the route. If you enter the transportation mode manually for a stage or if you have

defined it for the stage type in Customizing, the system considers the entries in the following sequence:

1. Manual entry for the stage

2. Customizing settings for the stage type

3. Transportation mode in the header data

## Agreement party and agreement type

The system uses the stage type and the Incoterms entered in the header data to automatically determine the agreement

party and the agreement party type, determining who is responsible for settlement.

## SCAC or airline code

If you enter an SCAC and no carrier, the carrier is determined in the subsequent planning processes. If you enter a carrier

directly, the system automatically determines the related SCAC and enters the value in the corresponding field of the stage.

For more information, see Carrier Categorization.

In Customizing and in the master data, you can define airline codes for air cargo carriers, and you can specify whether the

carrier is a member of the International Air Transport Association (IATA). When you create an air forwarding order or

quotation, you can enter these codes. The system then automatically determines the related prefix for the master air

waybill (MAWB).

If the transportation stage is checked by the planning and execution organization, the system determines the organization

interaction status (for example, from the default route). For more information, see Interaction Between Organizational Units.

You can use the Determine Distance and Duration pushbutton to have the system determine the transportation distance and

duration of a stage. You can also enter the distance and duration manually or change the data determined by the system. For more

information, see Determination of Transportation Distance and Transportation Duration.

This is custom documentation. For more information, please visit SAP Help Portal.

65


1/14/26, 2:17 PM

You can also determine the detailed route data by selecting a schedule and copying it to your actual route data. For more

information, see Direct Creation of Freight Documents and Selection of Schedules.

## Actual Route Resulting from Transportation Planning

If you have performed transportation planning based on the forwarding order (see Editing of a Forwarding Order), the actual route

is displayed and can no longer be changed.

As an alternative to transportation planning, you can create freight orders and freight bookings directly from the forwarding order

for the stages of the route. The freight document ID as well as other related data, such as information about ship connections, are

displayed for each stage. For more information, see Direct Creation of Freight Documents and Selection of Schedules.

## Copying the Actual Route to the Ordered Route

The ordered route is not updated automatically by the data of the actual route. If you would like this to happen because you want

print up-to-date documents, you can choose Copy from Actual Route on the Ordered Route tab page to copy the data to the route

ordered by the ordering party. However, note that the ordered route is no longer visible.

## Detail Data

You can enter and display detail data, such as delivery dates and address data, for a specific transportation stage. If the system

has already determined the address data from the master data of the location, you can overwrite this data for the complete

carriage of the ordered route.

The system displays the detail data of the actual route on three different tab pages:

Ordered Data: Data that is provided by the customer and that was entered in the freight unit

Planning/Execution Data: Data that originates from successor documents, such as freight orders, and cannot be changed

## Additional TU Dates/Times: Dates for transportation units

The Planning/Execution Data and Additional TU Dates/Times tab pages are displayed only if the corresponding data is available

(for example, if freight documents have already been created).

The following dates for the transportation stages, among other things, are displayed in the detail data or can be entered there:

## Requested pick-up date and delivery date

The pick-up date and delivery date requested by the ordering party and specified in the ordered route.

## Planned departure and arrival date

The departure and arrival date entered manually in the actual route or by the system after transportation planning. If

planning has not yet been performed, the planned departure and arrival date corresponds to the requested date.

If a freight document has not been created and transportation planning has not been performed, you can still change the

dates.

## Actual departure and arrival date

The actual departure and arrival date (including the time) entered manually in the freight document or reported by SAP

Event Management.

Confirmed pick-up date and delivery date (valid for complete carriage of the ordered route)

The pick-up date and delivery date confirmed to the ordering party.

## Cut-off dates

This is custom documentation. For more information, please visit SAP Help Portal.

66


1/14/26, 2:17 PM

Cut-off dates are read from the freight document and indicate the latest time by which goods or specific documents must

be available. The document cut-off date, for example, indicates the date by which all freight-relevant documents must be

made available to ensure that transportation can be prepared and goods can be loaded on time.

If you have entered a default route that is used to determine the route, the system calculates the departure and arrival dates based

on the specified transportation duration. The transportation duration is the total length of time needed to complete a

transportation run by a single transportation resource, such as a truck. It includes the length of stay at each location in the run. For

more information about the interaction of the default route and the determination of transportation distance and transportation

duration, see Determination of Transportation Distance and Transportation Duration.

## Stage View and Item View

For the stage table display, you can switch between the stage view and the item view. These views have the following

characteristics and advantages:

## Stage view

In this view, the stages are displayed at the top level of a hierarchy and the items belonging to a stage are displayed below.

This has the advantage that you can, for example, easily perform the following for a stage:

Create a new stage for several items

## Edit the data of a stage for several items

## Create or select freight documents for a stage, as well as select schedules

If not all of the freight units contain the same data, the sequence of the stages is determined based on the following criteria:

1. The sequence specified for the movement type in Customizing

2. Item number

3. ID of the freight unit

## Item view

In this view, the items are displayed at the top level of the hierarchy and the related stages are displayed below. If your

forwarding order or forwarding quotation contains several freight units, you can see a list of the items with the

corresponding freight units. The list contains an entry for each item that is assigned to a freight unit. You can also make

changes to an item that apply for all related stages.

Both stage table views are divided into the following areas (only displayed if the corresponding stages exist):

Route: Contains the general stages of the route.

BCO: Contains the stages of the route that relate to the buyer's consolidation process.

SCO: Contains the stages of the route that relate to the shipper's consolidation process.

Empty Provisioning and Empty Return: Contains the stages of the route that relate to the corresponding process.

## Determination of Locations and Business Partners at Item Level

For individual items, you can also define source and destination locations as well as business partners that differ from the

locations in the header data and the complete carriage. For example, you can define that the items that are transported together in

the main carriage are picked up from or delivered to different locations.

In certain cases, you can also define different source and destination locations as well as business partners for subitems. This is

valid for the buyer’s consolidation (BCO) and shipper’s consolidation (SCO) processes. The following options are available:

This is custom documentation. For more information, please visit SAP Help Portal.

67


1/14/26, 2:17 PM

If you enter the value SCO in the Buyer’s or Shipper’s Consolidation field for a forwarding order and have defined Export

as the traffic direction, you can define an alternate destination location for a subitem in a container. The system

automatically creates the corresponding stage for the subitem in the ordered route. You can then still change the stage

manually in the stage table.

When you create freight units for a forwarding order, the system copies the stages for the subitems to the actual route. If

you then change the stages in the ordered route, the changes are not copied to the actual route. However, you can change

the stages separately in the actual route.

In the BCO process, an import forwarding order is created automatically from an export forwarding order. For this import

forwarding order, the system defines the value BCO in the Buyer’s or Shipper’s Consolidation field and Import as the

traffic direction. If the source location of the subitem in the forwarding order differs from the higher-level container item,

then the stage for the subitem is automatically created in the ordered route and the actual route. You can no longer change

the stage manually in the stage table.

As described above under Prerequisites, the system determines the stage types of the automatically created pre-carriage and on-

carriage stages from the movement type or stage profile that was assigned to the forwarding order type.

For more information, see Buyer's Consolidation (BCO) in Export/Import and Shipper's Consolidation (SCO) in Export/Import.

## Copying the Route Data

If you copy a forwarding order or use a forwarding quotation as a template for creating a forwarding order, the route data (both the

requested route and the actual route) is also copied. The following data is also copied:

Source location and destination location

## Stage types

## Transportation mode

All other route data, for example, dates and information about ship connections, are not copied, otherwise they would mean a

restriction for later transportation planning. Therefore, you are still able to replan.

Air Freight-Specific Consolidation Processes

## Use

You can use Forwarding Order Management in Transportation Management (TM) to consolidate goods from several forwarding

orders or house air waybills (HAWBs) in a single air freight booking or a master air waybill (MAWB). A capacity manager at the

gateway can for example combine several forwarding orders for an air freight booking (gateway consolidation). You can also create

multiple air freight booking for a forwarding order.

However, it can also be necessary to restrict the consolidation options, because for example consolidation is not admissible in a

country. Therefore, TM also supports the following air freight-specific processes in which goods cannot be consolidated in the main

carriage:

Back-to-Back Process

Direct Shipment

Internal Co-Load

## Prerequisites

This is custom documentation. For more information, please visit SAP Help Portal.

68


1/14/26, 2:17 PM

In Customizing for the forwarding order type or forwarding quotation type, you have optionally defined the air waybill type (AWB

type). For more information, see Customizing for Transportation Management under the following Customizing activities:

Forwarding Order Management

## Forwarding Order

 Define Forwarding Order Type

Forwarding Order Management

## Forwarding Quotation

## Define Forwarding Quotation Type

If you want to define which AWB types are allowed for particular countries, you have assigned AWB types to individual countries in

Customizing. For more information, see Customizing for Transportation Management under  Forwarding Order Management

 Define Allowed AWB Types for Country .

## Features

You control air freight-specific consolidation processes by assigning the AWB type attribute to the forwarding order or forwarding

quotation. You can predefine this attribute in Customizing for the forwarding order type or forwarding quotation type; or you can

define it directly in the forwarding order or quotation.

This attribute for example controls how many forwarding orders or house bills of lading can be assigned to an air freight booking or

master air waybill. This means you can only assign a forwarding order that is defined as Back-to-Back or a house bill of lading to an

air freight booking or a master air waybill.

The attribute also has the following features:

You define the air waybill type in a forwarding order or a forwarding quotation. The system transfers this to the air freight

booking where it is read-only. This means you cannot modify the AWB type in a booking.

If you have predefined a value in Customizing, the system displays this value in the business document but you cannot

change it there. Otherwise, the field in the business document is empty and you can enter a value.

If the AWB type for a forwarding order or forwarding quotation is not predefined in Customizing, you can also change this

subsequently yourself, directly in the document. This changes the consolidation options accordingly. If for example you

change a forwarding order that is defined as Back-to-Back to a forwarding order with Standard Consolidation, you can

assign any number of additional forwarding orders to the air freight booking associated with this forwarding order.

If you define or change an AWB type in a forwarding order, or enter or change the destination location of a main carriage,

the system checks whether the AWB type is allowed for the country in which the destination location is found.

You can search for (air) forwarding orders, forwarding quotations and air freight bookings with this attribute in your

personal worklist (POWL).

More Information

Back-to-Back Process

Direct Shipment

Internal Co-Load

Back-to-Back Process

## Use

You use a back-to-back process to negotiate with the ordering party that consolidation cannot be performed for the main carriage

of the route. This can have the following reasons:

This is custom documentation. For more information, please visit SAP Help Portal.

69


1/14/26, 2:17 PM

Legal reasons (consolidation is not admissible in some countries)

Special features of the goods involved (such as for dangerous goods)

Customer request

## Customs declaration

In this case, you can only assign a back-to-back house air waybill (HAWB) to a master air waybill (MAWB). In Transportation

Management (TM), you can specify accordingly that an air freight booking can only be assigned to a forwarding order that is

defined as a back-to-back order.

## Prerequisites

You have assigned number ranges for house air waybills to your sales organization and ordering party involved in the TM master

data. For more information, see Waybill Stock Definition.

## Process

To define and execute a back-to-back process, proceed as follows: This process description only covers the special features of the

back-to-back process. For more information about creating forwarding orders and quotations, see Creation of a Forwarding Order

and Creation and Editing of a Forwarding Quotation.

1. You create an (air) forwarding order and define the Back-to-Back air waybill type (AWB type). If you have predefined the air

waybill type in Customizing for the forwarding order type, the system displays this as the default value.

If you first want to create a quotation for your ordering party, you can also create a forwarding quotation with the AWB type

Back-to-Back.

2. You assign a house air waybill number to the forwarding order or assign a number from the corresponding number range.

3. Define the stages of the route and create an air freight booking for the main carriage of your route. Alternatively, you can

assign an existing air freight booking to the main carriage.

4. The system transfers the data in the forwarding order to the booking. This includes the AWB type Back-to-Back. The

system also determines business partners in the booking automatically on the basis of the business partner in the

forwarding order.

5. You can then add to and change the data in the booking. However, the AWB type is read-only in the booking and can no

longer be changed. If you want to subsequently change the AWB type, you should change this in the forwarding order.

## Result

You cannot assign an additional forwarding order to a booking to which a back-to-back forwarding order has already been

assigned.

You can print the house air waybill from the Output Management tab. The transportation charges are also included. For

more information, see Printing.

Direct Shipment

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

70


1/14/26, 2:17 PM

In a direct shipment process, the transportation process is performed by the shipper and the carrier. Goods can for example be

transported to the airport directly by the shipper. This means that a house air waybill (HAWB) is not required and transportation

activities are performed on the basis of the master air waybill (MAWB) for the airline. Goods are not consolidated in the main

carriage.

In Transportation Management (TM), you can mark a forwarding order for the direct shipment process using the air waybill type.

When you create an air freight booking for this forwarding order, the data in the order is transferred automatically to the booking

and you cannot assign any other forwarding orders to the booking. The system does not create a house air waybill, but instead

creates an air waybill (AWB) that is based on the master air waybill.

There is also a special user interface for the direct shipment process. When you create a forwarding order with the AWB type Direct

Shipment, a corresponding air freight booking is created automatically for the forwarding order. You can enter the data on a

consolidated screen for the forwarding order and freight booking, and start follow-on processes such as calculation of costs for

both documents. The following process description applies when you create a forwarding order with the AWB type Direct

Shipment for the direct shipment process.

## Prerequisites

In Customizing, you have defined a forwarding order type with the following settings:

Same Locations and BPs checkbox is selected

## Automatic Freight Unit Building checkbox is selected

Freight unit building rule (FUB rule) that does not permit freight units to be split

The system supports just one freight unit per direct shipment.

Transportation mode Air (optional)

AWB type Direct Shipment (optional)

For more information, see Customizing for Transportation Management under  Forwarding Order Management

## Forwarding Order

 Define Forwarding Order Types .

You have specified in the stage profile or for the movement type that the forwarding order must contain a main carriage

stage. For more information, see Customizing for Transportation Management under  Forwarding Order Management

 Define Stage Profiles  or under  Forwarding Order Management

 Define Stage Type Sequence for Movement Types .

You have then specified in the Customizing settings for the forwarding order type how the stages are to be determined, that

is, using the stage profile or the movement type.

You have defined a freight booking type in Customizing and indicated in the Service Definition area that consolidation is

not to take place for the source and destination location of the main carriage. For more information, see Customizing for

Transportation Management under  Freight Order Management

## Freight Booking

 Define Freight Booking Types .

In Customizing, you have defined the freight booking type that you created as the default freight document type. You have

defined this default freight document type for the forwarding order type that you defined for the direct shipment. You have

also selected Main Carriage at the stage type. For more information, see Customizing for Transportation Management

under  Forwarding Order Management

## Forwarding Order

 Define Default Capacity Document Types for Stages .

## Process

To define and execute a direct shipment process, proceed as follows: This process description only covers the special features of

the direct shipment process. For more information about creating forwarding orders and quotations, see Creation of a Forwarding

Order:

This is custom documentation. For more information, please visit SAP Help Portal.

71


1/14/26, 2:17 PM

1. On the initial screen for the forwarding order, use the input help to select a forwarding order type that is suitable for the

direct shipment process. If this has not already been predefined in Customizing, choose the transportation mode Air and

the AWB type Direct Shipment.

2. When you have specified in the Customizing settings for the forwarding order type that the stages are to be determined

based on the movement type, you select the relevant movement type using the input help.

3. The system creates an air forwarding order and the corresponding air freight booking. The system determines the freight

booking type based on your Customizing settings for the default freight document type.

The forwarding order and freight booking data that you predefined in Customizing are displayed on the user interface for

the forwarding order with the AWB type Direct Shipment. The freight booking is also displayed in the stage view of the

forwarding order for the main carriage stage.

4. You enter the airport data for the freight booking. You can then save the forwarding order.

5. You specify additional data for the forwarding order and freight booking depending on your requirements. Note the

following:

The general data as well as the business partner, stage, and item data relate to the forwarding order.

The location data for the transportation stages in the section view are determined by the system based on the

booking data. You can change this data only on the tab page or in the assignment block Booking Data.

The handling codes also relate to the forwarding order and are not copied to the booking.

If you copy an existing forwarding order with AWB type Direct Shipment, only the forwarding order data is copied.

You can also copy a forwarding order with the AWB type Direct Shipment to a forwarding order with AWB type

Normal Consolidation or vice versa. However, freight bookings assigned are not also copied.

6. You can draw an MAWB number from the waybill stock for the creation of an air waybill. If there is a carrier change, you can

return the number to stock and specify a new carrier.

7. You can calculate the costs for the forwarding order and freight booking separately or together for both documents. Both

the forwarding charges and the freight costs are displayed.

8. If you want to use additional input and editing options, you can open the forwarding order or the air freight booking

separately from the user interface for the forwarding order with the AWB type Direct Shipment.

## Result

You cannot assign any other forwarding orders to the air freight booking that is indicated as Direct Shipment.

If you cancel a forwarding order that is indicated as a Direct Shipment, the system also automatically cancels the

associated booking. The MAWB number is returned to the waybill stock automatically.

You can search for forwarding orders with the AWB type Direct Shipment in your personal object worklist.

Internal Co-Load

## Use

In this process, you can make cargo capacity that you have already booked available to another organizational unit in your

company. This business unit can also be a legally independent unit.

As a consolidating business unit (consolidator), you are responsible for the freight booking and the master air waybill (MAWB). You

can calculate the internal freight costs and perform an internal settlement with the other business unit (coloader). As a coloader,

This is custom documentation. For more information, please visit SAP Help Portal.

72


1/14/26, 2:17 PM

you conduct the negotiations with the customer and are responsible for executing the forwarding order to the customer and for

the house air waybill (HAWB). You also perform the settlement with the customer.

## Prerequisites

You have created a suitable organizational structure in Customizing. You must assign your organizational unit to a company

organization so that the system can, for example, determine whether your sales and purchasing organizations belong to the

same company code.

For more information, see Customizing for Transportation Management under  Master Data

 Organizational

## Management

 Organizational Model

 Create Organizational Model

.

You have configured the necessary settings for the external and internal charge calculation and settlement. In particular,

you have activated the internal charge calculation in Customizing for the forwarding order type and the charge calculation

in Customizing for the freight booking type. For more information, see Customizing for Transportation Management under

Forwarding Order Management

## Forwarding Order

 Define Forwarding Order Types  and under  Freight Order

Management

## Freight Booking

 Define Freight Booking Types . For further information, see also Charge Management

and Service Product Catalogs.

There is an internal agreement between the two organizational units between which you want to perform the co-load

process. There is also an external agreement with the customer of the coloader. For more information, see Agreement.

## Process

1. As a consolidator, you create an air freight booking and therefore reserve capacity for a particular flight. You define the

consolidating business unit as a purchasing organization. For more information, see Freight Booking.

2. As a coloader, you create a forwarding order. You define the co-loading business unit as a sales organization.

3. You define the stages of the route in the forwarding order. For the main carriage, you specify the source and destination

locations as well as the pick-up dates/times and delivery dates/times according to the freight booking already created

whose capacity you want to use. You also define the consolidating business unit as a planning and execution organization.

4. You assign the freight booking whose capacity you want to use to the main carriage of the forwarding order.

5. From the forwarding order, you calculate the charges that the customer must pay to the co-loading business unit based on

the agreement reached between the two parties. For more information, see Charge Calculation.

6. You calculate the internal charges that the co-loading business unit must pay to the consolidating business unit.

7. You create a settlement document for the settlement between the coloader and their customer from the forwarding order.

For more information see Forwarding Settlement.

8. As a consolidator, you create an internal settlement document for the settlement with the coloader from the overview of

the settlement documents. For more information, see Internal Settlement Management.

Interaction Between Organizational Units

## Use

You can use this function to model how organizational units interact with each other, for example, how a sales organization

interacts with a planning and execution organization. This interaction is especially important if you have to transport certain goods

in a specific transportation stage, for example, dangerous goods.

## Features

This is custom documentation. For more information, please visit SAP Help Portal.

73


1/14/26, 2:17 PM

The sales organization is responsible for entering the order, for example, but is not allowed to create freight bookings for specific

transportation stages or send them to a carrier. It can therefore propose how to transport the goods (by specifying a route and a

schedule, and assigning a freight order or a freight booking) and sets the organization interaction status to transfer the affected

stages to the planning and execution organization to be checked. The planning and execution organization checks the proposal and

the transportation stage details in the transportation cockpit. It can then confirm the data exactly as proposed in the forwarding

order, change data such as the departure and then confirm the proposal, or reject the proposal outright. The status for the stage in

the forwarding order then changes to Confirmed, Confirmed with Deviations, or Rejected respectively.

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

This is custom documentation. For more information, please visit SAP Help Portal.

74


1/14/26, 2:17 PM

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

3

4

5

6

7

8

Cancellation Approved

Cancellation Partially Approved

Cancellation Requested

Cancellation Partially Requested

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

Auto-Confirmation Profile

## Definition

A user-specific grouping of parameters that are taken into account in the interaction between organizational units (in particular,

between customer service agents and gateway). The profile is only relevant for freight units for which interaction between

organizational units is mandatory. You define whether interaction between organizational units is mandatory in the default route or

in Customizing under  Transportation Management

 Freight Order Management

 Define Freight Booking Types .

This is custom documentation. For more information, please visit SAP Help Portal.

75


1/14/26, 2:17 PM

The settings that you configure in the auto-confirmation profile are checked by the system when the freight booking is assigned to

the freight unit stage. If all criteria are fulfilled, the assignment of the freight booking is confirmed automatically.

To define auto-confirmation profiles, open the Create Auto-Confirmation Profile app on the launchpad under Profiles and

Settings.

## Structure

In the auto-confirmation profile, you define the following, for example:

## General data

Here, you specify a technical name and description for the profile that you want to create. In addition, you can configure

whether automatic confirmation for this profile is to be activated and can choose a transportation mode. If automatic

confirmation is activated, the criteria for capacity and utilization limits and excluded security statuses must be met so that

the freight unit stages are confirmed automatically.

## Capacity limits

Here you define hard capacity limits that the system takes into account for automatic confirmation. You can define a

maximum gross weight and a maximum gross volume for the freight unit. You can also define a maximum weight capacity

and a maximum volume capacity for the freight booking as percentage values. The utilization of the freight booking after

the freight units have been assigned must not exceed the limits defined in the profile.

## Excluded security statuses

Freight units for which at least one of the excluded security statuses is specified are not confirmed automatically. The

security status is only relevant for the Air transportation mode.

If all parameters are observed, the assignment of the freight unit stage to the freight booking is confirmed automatically.

Administrative data is also displayed.

Coordination Between Customer Service and Gateway Agent

## Use

If you are a customer service agent and receive a forwarding order, you can assign it to a freight booking. A gateway agent can then

check this assignment (in other words, confirm or reject it).

## Prerequisites

In the Create Auto-Confirmation Profile app from the launchpad, you have defined auto-confirmation profiles.

You have defined rejection reason codes. For more information, see Customizing for Transportation Management under

Basic Functions

## General Settings

 Define Rejection Reason Codes .

You have defined freight booking types. For more information, see Customizing for Transportation Management under

Freight Order Management

## Freight Booking

 Define Freight Booking Types .

## Process

1. Creating the forwarding order

This is custom documentation. For more information, please visit SAP Help Portal.

76


1/14/26, 2:17 PM

As a customer service agent, you create a forwarding order and enter information about the business partners and

locations involved and the items to be transported.

2. Creating the transportation stages (optional)

You create the transportation stages and select a predefined schedule.

3. Defining the planning and execution organization

You define the planning and execution organizations that are responsible for the transportation stages on the actual route.

You also have the option of assigning a transportation stage to a freight booking.

4. Starting the organization interaction process automatically

If you have executed step 2, you proceed as follows: If the organization interaction is activated for some stages on

the actual route and you have finished working on the stages, you change the organization interaction status from

Not Yet Requested to To Be Checked.

If you have not executed step 2, you proceed as follows: If you have assigned a stage to a booking for which the

organization interaction is activated, the system automatically sets the status to To Be Checked.

5. Starting the organization interaction process manually

You can also start the organization interaction by manually setting the status to To Be Checked.

6. Changing the organization interaction status to Confirmed

If a booking is assigned to a stage for which an auto-confirmation profile exists, the system checks the rules that are

defined in this profile. If the rules defined in the profile have been fulfilled, the system automatically sets the organization

interaction status to Confirmed.

7. Gateway Agent Check

If the freight unit stages are not confirmed automatically, the gateway agent of the planning and execution organization

must do this. As a gateway agent, if you accept the proposals provided by the customer service agent without changes, the

system sets the status to Confirmed. If you change the data, for example, dates/times or quantities, the system sets the

status to Confirmed with Deviations.

If the customer service agent has not made an assignment to a freight booking, you, as the gateway agent, must do this.

If you reject the proposals provided by the customer service agent, the system sets the status to Rejected. You can enter a

reason for the rejection.

8. Monitoring of the organization interaction status by the customer service agent

As a customer service agent, you can check whether the gateway agent has accepted or rejected your proposals and can

clarify any necessary changes with your customer.

## More Information

## Auto-Confirmation Profile

Interaction Between Organizational Units

Building and Printing of House Bills of Lading and House Air
Waybills

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

77


1/14/26, 2:17 PM

You can use this function to create and print house bills of lading (HBLs) and house air waybills HAWBs) for the following business

documents:

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

Which strategy is used depends on the business document from which you build the house bill of lading or house air

waybill. If you do not define a strategy in Customizing, the system uses the relevant standard strategy for forwarding orders

or freight documents (see below).

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

This is custom documentation. For more information, please visit SAP Help Portal.

78


1/14/26, 2:17 PM

charges must contain the two digit code for IATA other charges and also entries for the charge due (carrier or

agent).

For more information, see Customizing for Transportation Management under  Basic Functions

## Charge

Calculation

## Basic Settings

 Define Charge Types , and also under Charge Calculation.

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

This is custom documentation. For more information, please visit SAP Help Portal.

79


1/14/26, 2:17 PM

Build House Bill of Lading or House Air Waybill by Freight Documents (HBL_FDOC)

With this strategy, the system groups together all items that have the same freight documents in the main carriage.

Build House Bill of Lading or House Air Waybill by Shipper/Consignee with Address (HBL_SHPCNA)

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

This is custom documentation. For more information, please visit SAP Help Portal.

80


1/14/26, 2:17 PM

You create house bills of lading or house air waybills by choosing  Follow-up Actions

 Build HBL or HAWB . The

information for the house bill of lading or house air waybill is displayed at header level. A house bill of lading or house air

waybill can have one or more freight units.

For more information about hierarchy types, see Use of Hierarchical Views in FOM.

## More Information

Process Controller Configuration

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

This information can be entered in air forwarding orders, freight units, air bookings, and freight orders that cover pre-

carriage or on-carriage for the air booking. You can enter 9 lines with a maximum of 65 characters per line. In the air

forwarding order, you enter this information on header level on the Nature of Goods tab page. In the air booking, you enter

it on item level on the Capacity and Cargo tab page, and in the freight order, on item level on the Items tab page (Generic

Item View hierarchy type).

The nature of goods for manifest is printed in the security manifest and cargo manifests, which you print from the air

booking.

This is custom documentation. For more information, please visit SAP Help Portal.

81


1/14/26, 2:17 PM

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

This information is copied automatically to the air booking and freight order from the freight unit. It is displayed in

the details area of a freight unit that you have selected on the Capacity and Cargo tab page in the air booking or on

the Items tab page in the freight order (Generic Item View hierarchy type).

For both types of nature of goods, you can change the copied text. For example, you can replace the text with something

that is specific to a certain stage, country or region, or you can write the text in another language. You can also insert a

standard text that you have defined beforehand.

This is custom documentation. For more information, please visit SAP Help Portal.

82


1/14/26, 2:17 PM

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

Empty Provisioning and Empty Return

## Use

As a logistics service provider, you may be requested by your ordering party to provide the requisite empty containers or railcars

(empties) in addition to transporting goods. This means that you may be requested to provide more or fewer empties than you

actually needed to transport the goods. The ordering party can also request that you provide empties independent of a

transportation.

Transportation Management (TM) supports these different requests. The system also supports the return of empties as well as

different variants of these business processes. For example, you can specify that the ordering party organizes the pick-up and

delivery of the empties themselves.

The following describes how you can map your requests for the provisioning and return of empties in forwarding order

management.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

83


1/14/26, 2:17 PM

Empty provisioning and return is supported only for container units and railcar units. It is not supported for trailer units and

package units.

## Process

## Provisioning and Return of Empties with Reference to a Goods Transportation

If your ordering party has requested that you also provide the required number of empties in addition to transporting goods, you

can map this as follows in forwarding order management from TM:

1. Create a forwarding order with the corresponding container items or railcar items for the transportation of goods. For more

information about creating forwarding orders, see Creation of a Forwarding Order.

You can also request empty provisioning and return in forwarding quotations. If you create a forwarding order with

reference to a quotation, the system copies the entries for empty provisioning and return to the forwarding order. For more

information about creating forwarding quotations, see Creation of a Forwarding Quotation.

2. In the Empty Provisioning field, select the option Requested (X) for your cargo item. This indicates that your ordering party

requests the provisioning of the same number of empties as you have defined as the item quantity.

3. If your ordering party also requests the return of the provided empties, select Requested (X) in the Empty Return field.

Otherwise, select the default value Not Requested (empty).

4. The system displays information about the provisioning and return of empties in the item details on the Details of Empty

Provisioning and Details of Empty Return tab pages.

The system enters automatically the source location of the item as the destination location of the provisioning information

and the destination location of the item as the source location of the return information. You can also enter a source

location for the provisioning of empties and a destination location for their return. You can even leave this information open

in the forwarding order and add it at a later date. Furthermore, you can change the pick-up and delivery dates for the

provisioning and return of empties to meet your individual requirements.

Information about empty provisioning and empty return is also displayed in the stage tables of the ordered route and the

actual route.

5. The system creates separate freight units and transportation units (container units and railcar units) for the transportation

of goods and the provisioning or return of empties.

Note that you can search for forwarding orders and forwarding quotations in your personal object worklist (POWL) using empty

provisioning and empty return information.

## Provisioning and Return of Empties Without Reference to a Goods Transportation

If your ordering party has requested that you provide or return empties only without transporting goods, you can map this as

follows. You can also use this to map scenarios in which your ordering party requests that you provide or return more or fewer

empties than are actually needed for the transportation of goods:

1. Create a main item for the provisioning or return of empties. Create a container item or railcar item for this main item and

enter the required quantity.

2. Select the option Provisioning Only or Return Only in the Empty Provisioning or Empty Return field of this item.

3. The system displays information about the provisioning and return of empties in the item details on the Details of Empty

Provisioning and Details of Empty Return tab pages. Here you can enter the source and destination locations for the

provisioning or return of empties as well as the corresponding pick-up and delivery dates.

Information is also displayed in the stage tables of the ordered route and the actual route.

This is custom documentation. For more information, please visit SAP Help Portal.

84


1/14/26, 2:17 PM

4. The system creates transportation units for the provisioning and return of empties.

## Pick-Up and Delivery of Empties by Ordering Party

Your ordering party may want to organize the pick-up and delivery of empties themselves. This means that as the logistics service

provider you are only responsible for providing the empties. You are not responsible for their pick-up or delivery. You specify this as

follows:

1. Specify the provisioning or return of empties for cargo items or separately as described above.

2. In the detailed data about the provisioning or return of empties select the Organized by Ordering Party checkbox.

3. The system marks the corresponding stages of the pick-up and delivery route for empties as not relevant for planning

(planning block).

## More Information

Empty Provisioning and Return in Export/Import Processing

## Triangulation

Calculation of Charges for Empty Provisioning and Empty Return

Empty Provisioning and Return in Export/Import Processing

## Use

Empty provisioning and return can be planned and executed as part of export/import processing. In this case, the following

applies:

The export organization is responsible for planning and executing empty provisioning (because the empty containers or

railcars are required before transportation starts), but the import organization may be responsible for the transportation

charges.

The import organization is responsible for planning and executing empty returns (because the empty containers or railcars

are returned after transportation has taken place), but the export organization may be responsible for the transportation

charges.

Empty provisioning and return can be requested in export forwarding orders and quotations, and import forwarding orders and

quotations. The following are example processes for export/import processing with empty provisioning and return.

## Process

Empty provisioning and return with reference to the transportation of goods can be handled as follows in export/import

processing:

1. The export organization creates the export forwarding order and requests empty provisioning and empty returns for the

cargo items.

2. The system does the following:

Creates container units or railcar units for the empty provisioning items so that the export organization can plan and

execute empty provisioning

This is custom documentation. For more information, please visit SAP Help Portal.

85


1/14/26, 2:17 PM

Copies information about the requested empty returns to the item details of the main cargo item

If required, the export organization can then calculate the charges for the empty return items.

3. The system creates the import forwarding order. It does the following for empty provisioning and empty returns:

Copies information about the requested empty provisioning to the item details of the main cargo item

If required, the import organization can then calculate the charges for the empty provisioning items.

Creates container units or railcar units for the empty return items so that the import organization can plan and

execute empty returns

For empty provisioning and return without reference to the transportation of goods, the following applies:

Since the export organization is responsible for planning and executing empty provisioning, you can request empty

provisioning without reference to a main cargo item only in the export forwarding order.

Since the import organization is responsible for planning and executing empty returns, you can request empty returns

without reference to a main cargo item only in the import forwarding order.

More Information

Export/Import Processing

Triangulation

## Use

As a carrier, you can combine a request for empty provisioning and a request for empty return to save transportation charges.

  Example

You have to organize the pickup of an empty container that is no longer required from a consignee and the subsequent

transportation of this empty container to the container yard. At the same time, you have to organize the pickup of a second

empty container of the same type from the container yard and the provisioning of this empty container to the customer.

Instead of having the system execute these two orders separately, you can combine them into one order. This means that you

have the first empty container directly transported to the customer.

  Note

Triangulation is supported for container units and railcar units only. For the sake of simplicity, the term transportation units is

used below even though this term includes trailer units. Triangulation is not supported for trailer units.

## Prerequisites

You have created at least two forwarding orders. For one of these forwarding orders you have selected the option

Requested in the Empty Provisioning field for the corresponding cargo item. For the other forwarding order you have

selected the option Requested in the Empty Return field for the corresponding cargo item.

There are at least two transportation units: one for the empty provisioning and one for the empty return (movement

category Empty Return and Empty Provisioning). The two transportation units must have the same equipment type. The

transportation unit for the empty provisioning must be unplanned.

This is custom documentation. For more information, please visit SAP Help Portal.

86


1/14/26, 2:17 PM

The requested return of the empty transportation unit must be before the provisioning of the empty transportation unit.

## Features

You can combine a transportation unit for the empty provisioning (empty provisioning TU) and a transportation unit for the empty

return (empty return TU) in a single transportation unit (triangulation transportation unit). From a technical point of view, the

system keeps the empty return TU and deletes the empty provisioning TU. The new triangulation transportation unit (triangulation

TU) now refers to two forwarding orders and is assigned the movement category Triangulation. As with any other transportation

unit you can plan this transportation unit on a freight order. When you revoke triangulation, the system dissolves the triangulation

TU into the two original transportation units.

Triangulation is supported for unplanned transportation units only. If the empty return TU was already planned before

triangulation, the triangulation TU is also planned. The system updates the locations only.

If you change one of the assigned forwarding orders, the system tries to keep the triangulation TU. However, if you make critical

changes (by changing the equipment type or canceling the provisioning, for example) the system may have to dissolve the

triangulation TU into the two original transportation units.

To enable you to recognize whether an empty provisioning or empty return item belongs to a triangulated transportation unit, the

text (Triangulation) is added to the item text that is displayed in the actual route on the Stages tab page of the forwarding order.

## Activities

To perform triangulation, select a container unit or a railcar unit in the personal object worklist for container units or railcar units.

To do this, open the Railcar Units or Container Units app on the launchpad under Planning.

Then choose  Triangulation

 Create Triangulation . If you have selected the option for a container unit or railcar unit for the

provisioning, the system automatically proposes only container units or railcar units for the return, and vice versa.

Alternatively, you can directly select two container units or railcar units (one for the provisioning and one for the return) and then

choose  Triangulation

 Create Triangulation .

To revoke triangulation, choose Revoke Triangulation.

The options to create and revoke a triangulation are available on the user interfaces where you create and change container units

and railcar units as well as in the transportation cockpit.

You can search for triangulation TUs in your personal object worklist using the movement category. In the selection criteria to start

the transportation cockpit, you can also search for triangulation TUs using the movement category. Note that TUs are blocked for

planning if you have not entered a source location or destination location. In this case, you must select the value Include in

Selection in the selection criteria under Documents Blocked for Planning to ensure that these triangulation TUs are found.

## More Information

## Empty Provisioning and Empty Return

Processing of Changes and Deletion of Forwarding Orders

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

87


1/14/26, 2:17 PM

The forwarding order data received from your ordering party can change during the process. The change controller in

Transportation Management (TM) checks whether forwarding orders or forwarding quotations have changed and propagates the

changes to the freight unit. You can specify how the change controller is to carry out the changes. The following options are

available:

Synchronous

## Asynchronous

Synchronous with fallback to asynchronous

## Prerequisites

You have defined the way the system propagates the changes to successor documents in Customizing for Transportation

Management under:

Forwarding Order Management

## Forwarding Order

 Define Forwarding Order Types

Forwarding Order Management

## Forwarding Quotation

## Define Forwarding Quotation Types

You have implemented the batch report Background Job to Process Triggers Periodically

(/SCMTMS/PROCESS_TRIGGER_BGD), in case you process the changes asynchronous.

You have created the necessary change controller strategies and change controller conditions in Customizing for

Transportation Management under  Basic Functions

 Process Controller

 Define Strategy .

You have specified whether freight units can be deleted or canceled in Customizing for Transportation Management under

Planning

## Freight Unit

 Define Freight Unit Types .

## Features

## Changed Forwarding Order or Forwarding Quotation Data

You can still change most of the data in a forwarding order or quotation during the transportation process, such as dates,

quantities, and locations, as well as add or delete items. This is also the case if freight units have already been built and planning

has been completed or execution has started. The system updates the freight units when saving the data. Follow-on documents

such as freight orders and freight bookings are also adjusted.

However, if data has already been transferred to the freight unit from the execution process and the status of the freight unit has

been changed to On Hand, for example, the system no longer adjusts the follow-on documents automatically. In this case, the

system prompts you to change the data manually.

If a forwarding settlement document or an internal settlement document already exists and you have activated the forwarding

settlement change process, you can enter the changes directly in the forwarding order (for example, changes to quantities, to the

shipper, or to the consignee). The change process triggers the necessary changes in the forwarding settlement process. If a

forwarding settlement document or an internal settlement document already exists and you have not activated the forwarding

settlement change process, you have to cancel the forwarding settlement document. You then enter the changes directly in the

forwarding order and create a new forwarding settlement document that contains the changes. You can activate the forwarding

settlement change process in the corresponding settlement profile by selecting Reverse and Repost or Delta Only. The system

uses the organization or a combination of organization and business partner to assign the profile to the forwarding order. For more

information, see Automatic Change Management for Forwarding Settlements.

The system implements the changes synchronously or asynchronously as follows depending on your Customizing settings:

## Asynchronous changes

This is custom documentation. For more information, please visit SAP Help Portal.

88


1/14/26, 2:17 PM

The system can change the freight unit even if it is blocked by another process. It updates the freight unit as soon as the

freight unit is unlocked.

The system processes the changes in the background using the report Background Job to Process Triggers Periodically

(/SCMTMS/PROCESS_TRIGGER_BGD). You can check in the application log if the system correctly propagated

asynchronous processed changes. To do so from the SAP Easy Access menu, choose  Logistics

 Transportation

Management

## Administration

 Display Application Log Entries .

## Synchronous changes

The system informs you immediately if a freight unit is blocked. You cannot propagate the changes.

In case the forwarding order or forwarding quotation has the approval status Approval Needed and with your change the approval

becomes redundant, the system deletes the workitem from the workflow.

## Special Features When Changing Data

The following special features apply to the changing of forwarding order data and forwarding quotation data:

## Deleting items

When you delete items the system deletes the corresponding freight units provided they are still in planning. The system

does not delete freight units that are already in execution.

## Changing an item hierarchy

When you change an item hierarchy the system does not delete freight units that are in planning or are already in execution.

Changing the shipping type, movement type, and transportation mode

You cannot change these parameters if the following applies:

Shipping type: The main carriage stage of the route is already in execution or there is a valid forwarding settlement

document (in other words, this has not been canceled).

Movement type: A follow-on document has already been assigned to a stage of the route or there is a valid

forwarding settlement document.

Transportation mode: The main carriage stage of the route is already in execution, there is a valid forwarding

settlement document, or invoicing has already been completed.

## Canceled Forwarding Orders or Forwarding Quotations

You can cancel forwarding orders and forwarding quotations. The system either deletes or cancels the freight unit. If you have

specified, that the system can only cancel freight units, the freight unit remains with the status Canceled. Otherwise, the system

deletes the freight unit. If the execution has already started for an assigned freight order or freight booking, you cannot cancel the

forwarding order.

If the forwarding order or the forwarding quotation has the approval status Approval Needed, the system deletes the work item

from the workflow.

## More Information

For more information about changes to freight document data, see Change Controller.

For more information about changes within the integrated ERP process, see Integration of Changed and Deleted Orders and

Deliveries.

This is custom documentation. For more information, please visit SAP Help Portal.

89
