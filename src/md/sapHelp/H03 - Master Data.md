1/14/26, 2:16 PM

Transportation Management (TM)

Generated on: 2026-01-14 14:16:22 GMT+0000

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


1/14/26, 2:16 PM

## Master Data

You use this component to manage master data that is used in a variety of business transactions in Transportation Management

(TM). The following master data objects are part of this component:

Business partner (see Business Partner)

Organizational management (see Organizational Management)

Transportation network (see Transportation Network)

Transportation mode (see Transportation Mode)

Product (see Product)

Carrier profile (see Carrier Profile)

Equipment (see Equipment Groups and Equipment Types)

Resources (see Definition of Resources)

Transportation charges (see Setup of MD for Charge Management and SP Catalogs)

  Note

Before you define any master data objects, you must create an active model in Customizing. For more information, see

Customizing for Transportation Management under  Master Data

 Create Active Version and Model

.

The following functions that are described below are currently not released:

## Enterprise Asset Management Integration

Equipment and Functional Location data are not integrated with the TM vehicle resource.

Business Partner

## Definition

A person, organization, group of persons, or group of organizations in which a company has a business interest.

## Use

You use this business object for a variety of business transactions.

You create and manage your business partners centrally along with the roles they assume for your company. To do so, you define

the general data of the business partner once and you assign business partner roles to the business partner. Specific data is

stored for each business partner role. In this way, you don't store redundant data since the general data is independent of a

business partner’s function or of application-specific extensions.

When you first create a business partner in the system, the business partner role General Business Partner is automatically

assigned to the business partner.

## Structure

This is custom documentation. For more information, please visit SAP Help Portal.

2


1/14/26, 2:16 PM

You identify each business partner with a unique business partner number.

You create and manage the specific data for a business partner role once you've assigned a specific role to the business partner.

You create and manage the following general elements of a business partner:

## General Data

Here, you enter data (or the system displays data) that is valid for all business partner roles. This data includes, for example, the

name, address, communication data, identification numbers, and business partner status.

## TM-Specific Data

The following business partner roles are most commonly used in TM:

000000 Business Partner (General)

FLCU01 Customer

FLCU00 FI Customer

FLVN01 Vendor

FLVN00 FI Vendor

## CRM010 Carrier

SLLCOF Global Trade Services: Customs Office

## TM0001 Driver

BUP004 Organizational Unit

BUP001 Contact Person

BUP002 Prospect

BUP003 Employee

## BUP005 Internet User

The role CRM010 (Carrier) contains the data of role FLVN01 (Vendor) plus additional TM specific data such as:

Regulated Agent Code

IATA Agent Code

CASS Account

SCAC Codes

Airline Codes

Service Level Codes

## Carrier Service Codes

The role FLVN01 (Vendor) and the role CRM010 (Carrier) allow maintenance of data on the level of a purchasing organization.

The roles FLCU001 (FI Customer) and FLVN00 (FI Vendor) allow maintenance of data on the level of a company code.

This is custom documentation. For more information, please visit SAP Help Portal.

3


1/14/26, 2:16 PM

  Note

FLCU01 contains data that can be maintained on sales area level (a sales area is a combination of sales organization,

distribution channel, and division.)

As TM documents such as forwarding orders and forwarding quotations don't contain distribution channel and division, you

need to maintain a default value for distribution channel and division in Customizing for Transportation Management under

Master Data

 Basic Functions

## General Settings

 Define General Settings for TM . These default values are used to

access business partner master data that are stored on sales area level by adding these as defaults for the sales organization

defined for TM.

  Note

In TM you need to create organizational units to represent sales organizations, purchasing organizations and company codes in

TM.

For more information, see Organizational Management.

## Integration

In an integrated system landscape (side-by-side scenario), you can replicate master data from a source system, such as an ECC

system or an SAP S/4HANA system, to the Transportation Management (TM) component of an SAP S/4HANA system (target

system). To replicate business partner master data, you set up a replication model in your source system using the DRF

customizing transaction DRFIMG and define the target system as part of the replication model.

In business transaction documents, such as a forwarding order, the business partner master data object appears as a party that

takes part in transportation processes. The party assumes partner functions, such as ship-to party, shipper, or sold-to party.

  Note
You don't need to define special business partner roles in Customizing for the partner functions (see Definition of Business

Partners). You can assign any business partner to the different partner functions.

You can configure the system to assign business partner roles to allowed business document partner functions.

For all business documents that you work with in TM:

The system checks whether a business partner is compatible with a business document partner function. If you enter a

business partner with a particular partner function in a business document, the system verifies whether that role is allowed

for that business partner.

You can activate the checking of the organizational data of a business partner’s company or the sales or purchasing

organizational data. These checks ensure that all business partners with the carrier role or customer role involved in certain

business documents are assigned to one or both of the following:

To a sales organization or purchasing organization in the business partner’s company

To the sales organization or purchasing organization in the header of the business document

These checks are relevant for the following business documents:

Forwarding orders, forwarding agreements, and forwarding settlement documents

Freight orders, freight bookings, freight agreements, and freight settlement documents

This is custom documentation. For more information, please visit SAP Help Portal.

4


1/14/26, 2:16 PM

You activate these checks in Customizing for Transportation Management under  Basic Functions

## General Settings

 Define General Settings for TM .

The search help for business partners reflects this configuration of business partners for the allowed business document

partner functions by only returning business partners in the result list that can be used for a specific business document

partner function.

## More Information

For more information about SAP Business Partner, see SAP Business Partner.

Definition of Business Partners

## Use

You use this process to define business partners (BPs) in Transportation Management (TM).

## Process

1. You define a BP in the the following apps, which you open from the launchpad:

Create Customer (Sales)

Create Vendor (Purchasing)

## Create Forwarding Agent

2. You assign additional BP roles to the BP.

TM delivers the following BP roles for BPs of the type Person:

3. You can create relationships between BPs.

  Note
The relationship category Has Contact Person is used in the tendering process.

The relationship category Has Subsidiary / Agent is used to describe subsidiaries and agents of a carrier organization.

Additional Texts

## Use

You can define additional texts for the business partner master and use them as printing addresses or signatures on different

documents.

## Prerequisites

You have defined additional text types in Customizing for Transportation Management under  Master Data

## Business Partners

 Define Text Types for Business Partner Master

.

## Features

This is custom documentation. For more information, please visit SAP Help Portal.

5


1/14/26, 2:16 PM

You can enter additional texts for the business partner role Business Partner (Gen.) on the Maintain Business Partner user

interface (transaction BP) on the Additional Texts tab page. Texts from this tab page (for example, addresses or signatures) are

used by Transportation Management (TM) as printing addresses or signatures on several printing documents such as air waybills.

To ensure that the texts have the correct dimensions for the designated areas, you specify text types with maximum numbers of

characters and lines. To support printing in several languages, you can define the language of the texts and enter additional texts

for one text type in different languages for one business partner instance.

  Note

You can also use additional texts to define formatted printing addresses or paragraphs for the related business partner and edit

them so that they are letter of credit-compliant. To use this function, you must define the default text type for printing

addresses in Customizing for Transportation Management under  Master Data

 Business Partners

 Assign BP Text Types

to Partner Functions .

Business Partner Blocking

## Use

With this function, you can block the assignment of a business partner to a forwarding quotation or to a forwarding order.

Additionally, you can block the business partner, so that within a forwarding order the system prevents forwarding settlement

documents from being created.

The blocking options are structured hierarchically in the business partner master record. You can set the blocks at the following

levels:

Complete business partner

## Company code

Purchasing organization

Sales organization

## Features

You can block the business partner manually.

You can set the blocks in TM by opening one of the following apps from the launchpad:

Create Customer (Sales)

Create Vendor (Purchasing)

Create Forwarding Agent

Block

## Role

Description

Document

## Tab Page

Posting Block

FLCU00

Blocks the

Forwarding Order

Choose the Company

assignment of

System checks the

business

partners to a

forwarding order

following:

## Sold-to Party

Code button then see

the Customer: Status

tab.

This is custom documentation. For more information, please visit SAP Help Portal.

6


1/14/26, 2:16 PM

Block

## Role

Description

Document

## Tab Page

document or a

## Prepaid

Posting Block

FLVN00

Sales Order Block

FLCU01

Agreement Party

## Collect

Agreement Party

Forwarding Order

Choose the Company

Code button then see

the Vendor: Status tab.

assignment of

System checks all

partner functions.

business

partners to a

forwarding order

document or a

forwarding

quotation

document

Blocks the

creation of

forwarding

settlement

documents

Blocks the

creation of

freight orders

Blocks the

forwarding

quotation

document

Blocks the

creation of

forwarding

settlement

documents

Blocks the

Forwarding Order

Choose the Sales and

Distribution button then

see the Customer:

Status tab.

assignment of

System checks the

following:

Sold-to Party

## Prepaid

Agreement Party

## Collect

Agreement Party

business

partners to

forwarding order

documents or

forwarding

quotation

documents

Blocks the

creation of

forwarding

settlement

documents of

the specific sales

organization

Billing Block

FLCU01

Blocks the creation of

Forwarding Settlement

Choose the Sales and

forwarding settlement

## Document

Distribution button then

documents of the

specific sales

organization

see the Customer:

Status tab.

This is custom documentation. For more information, please visit SAP Help Portal.

7


1/14/26, 2:16 PM

Block

## Role

Description

Document

## Tab Page

Purchasing Block

FLVN01

Blocks the creation of

Freight order, Freight

Choose the Purchasing

freight orders

## Booking

System checks all

partner functions.

button then see the

Purchasing Data tab.

## Activities

On the corresponding tab page, select the check box with the block you want to set or, in case of specific sales organizations, enter

block reason codes.

## Example

You would like to block the business partner Kulinarisch Weltweit, located in Cologne. To do so, on the Customer Company Org

Data tab page, you select the Central Posting Block check box. From now on, the system blocks all sales organizations of the

respective business partner and you cannot assign the business partner to a forwarding order.

If a forwarding order document already exists in the system when you set the block, you cannot create forwarding settlement

documents. This applies to the following blocks:

Central billing block

Central order block

Central posting block

Business Partner Determination

## Use

You can enable the system to determine the business partners that you use in different business document types. You can also

enable the system to automatically determine business partners for forwarding orders with specific Incoterms. This allows you

easily and efficiently enter business partners in a business document. It cuts down the chance of manual errors and reduces the

need to enter a business partner for each partner function.

In the Define Partner Determination Profiles Customizing activity, you can create a partner determination profile that the system

uses to automatically determine the following features:

## The partner functions available in a business document

You specify the list of partner functions that the system makes available in a business document.

## The level of control the user has in entering the partner function

Depending on the settings you define in Customizing, you change or delete a partner function, or add a partner function

from a list of available partner functions. You can also specify settings so that you cannot change or delete specific partner

functions.

## How the system determines business partners for the partner functions

The system uses one of the following relationships that you specify in Customizing, to determine a business partner:

This is custom documentation. For more information, please visit SAP Help Portal.

8


1/14/26, 2:16 PM

## Partner function and source partner function

In Customizing, you can specify a source partner function for a particular partner function. In the application, when you

enter a business partner in the field that you have specified as the source partner function, the system automatically copies

the business partner to the associated partner function.

For example, in Customizing, you specify the partner function as Invoicing Party, the source type as Partner

Function, and the source function as Sold-to Party. In the application, you specify the sold-to party as

Customer01. The system assigns Customer01 as the business partner for the invoicing party.

Partner function and the source partner function in business partner master data

The system uses the settings that you specify on the Partner Function tab page in the BP – Maintain Business Partner

transaction to determine a business partner in a business document.

For example, you are a logistics service provider (LSP), and you have a business partner APP_1. In the BP – Maintain

Business Partner transaction, you specify APP_1 with the BP role of FLCU01 (Customer). On the Partner Function tab

page of the BP transaction for APP_1, you specify an organizational unit and a partner function for the business partner

APP_INV. APP_INV fulfills the role of invoicing party for APP_1. In Customizing, you specify the partner function as

Invoicing Party, the source type as BP Relationship, and the source role as Sold-to Party.

In a forwarding order, you specify the organization as 561234 on the General Data tab page and the sold-to party as

APP_1 on the Business Partner tab page. The system checks the business partner master data for APP_1. On the Partner

Function tab page, it finds that APP_1 uses APP_INV as the invoicing party for organization 561234. It assigns APP_INV as

the business partner for the invoicing party.

## Partner function and business partner

In Customizing, you directly assign a business partner to a partner function. In the application, the system automatically

assigns this business partner to the partner function.

For example, in Customizing, you specify the partner function as Invoicing Party, the source type as Business

Partner, and the business partner as CSI_CARR1. The system automatically assigns CSI_CARR1 as the business partner

for the invoicing party in the application.

Note that you can enter a business partner that does not exist in the current system. This enables you to assign a business

partner to a partner function in one system and transport it to another system where the business partner exists. For

example, in a Customizing system, you have not defined any business partner master data. You have assigned business

partner LUF to a partner function of carrier. You transport this data to a production system where LUF is defined. In a

business document of the production system, the system determines that the business partner for the carrier is LUF.

## Relationship category

The system can determine the business partner for a partner function based on the partner relationship you specify in the

Maintain Business Partner transaction (transaction BP).

To do so, you must specify the Source Type as Relationship Category in the Customizing for Transportation Management

under  Master Data

## Business Partners

 Define Partner Determination Profiles . The system determines the

corresponding business partner based on the partner relationship you specify in the Maintain Business Partner

transaction (transaction BP) (such as Has Invoicing Party, Has Contact Person, and so on).

You can also choose to have a reverse relationship between the partner functions by selecting the Rev. Rel. checkbox in the

Customizing.

For example, in the Maintain Business Partner transaction (transaction BP), you have performed the following:

Created two business partners INV and SHP.

Defined a relationship that SHP has the invoicing party INV

This is custom documentation. For more information, please visit SAP Help Portal.

9


1/14/26, 2:16 PM

You have performed the following in Customizing:

Specified the partner function as RS (Invoicing Party)

Specified the source type as Relationship Category

Specified the source function as U6 (Shipper)

Specified the relationship category as BBP002 (Has Invoicing Party)

## Selected the Rev. Rel. checkbox

The system considers the following during business partner determination in a business document such as a forwarding order or a

freight order:

Direct relationship - Shipper SHP has invoicing party INV.

Reverse relationship - Invoicing party INV is invoicing party of shipper SHP.

In Customizing, you can assign different profiles to different types of business documents. For example, you can specify a profile

that controls how the system determines business partners in forwarding orders, and another profile for business partner

determination in forwarding settlement documents.

In Customizing, you can assign a profile to the following business document types:

Forwarding orders

Forwarding quotations

Forwarding settlement documents

Freight orders

## Freight bookings

Freight settlement documents

Freight agreement RFQs

Forwarding agreement quotations

Freight agreements

Forwarding agreements

Internal agreements

## Mutual agreements

When you use a particular forwarding order type to create a forwarding order and enter an Incoterm, the system uses the

information you specify in the Assign Partner Determination Profiles Based on Incoterms Customizing activity to determine the

business partner. It overwrites the partner determination profile you have assigned to the forwarding order type in the Define

Forwarding Order Types Customizing activity.

## Prerequisites

You have made the settings in Customizing to create a partner determination profile that the system uses to automatically

determine business partners. For more information, see Customizing for Transportation Management under  Master Data

## Business Partners

 Define Partner Determination Profiles .

This is custom documentation. For more information, please visit SAP Help Portal.

10


1/14/26, 2:16 PM

If you want to automatically determine business partners in a forwarding order with a specific Incoterm, you have assigned the

partner determination profile to forwarding order type and Incoterm combination in Customizing. For more information, see

Customizing for Transportation Management under  Master Data

## Business Partners

 Assign Partner Determination Profiles

Based on Incoterms .

You have created relationships between organizations and business partners in the transaction BP – Maintain Business Partner

under  SAP Menu

 Transportation Management

 Master Data .

If you want to assign a particular business partner to a particular partner function in a business document, you have performed

the following actions:

Entered Business Add-In in the Srce Type (Source Type) field in the Define Partner Determination Profiles

## Customizing activity

Implemented the Business Add-In BAdI: Specific Partner Assignment in Customizing for Transportation Management

under  Business Add-Ins for Transportation Management

## Master Data

 Business Partners

## More Information

Settings for the Forwarding Order

Creation and Editing of a Forwarding Quotation

## Forwarding Settlement

Creation and Editing of Freight Orders

Creation and Editing of Freight Bookings

## Freight Settlement

Definition of Carrier Service Codes

## Use

A carrier can offer services to shippers or logistics service providers (LSP). The shippers or LSPs contact the carrier and obtain the

list of services. Subsequently, the shippers or LSPs manually enter these services in the master data of the system to use it in a

freight document with the carrier.

You can enter the services that a carrier offers to a shipper or LSP in the Maintain Business Partner transaction (transaction BP).

When you enter the carrier in a freight agreement, the system makes these services available in the document.

## Activities

In the Maintain Business Partner transaction, perform the following steps to enter the services:

1. Enter the business partner.

2. Change BP role to Carrier.

3. In the Carrier Service Codes screen area of the Transportation Data tab page, enter the carrier service code and the

service type.

This is custom documentation. For more information, please visit SAP Help Portal.

11


1/14/26, 2:16 PM

You can define service types in Customizing for Transportation Management under  Basic Functions

 General Settings

 Define Service Types

## Example

In the Maintain Business Partner transaction, you enter carrier service codes and service types for services Fumigation,

Loading, and Unloading for a business partner LUF_1 with a BP role of Carrier. In a freight agreement, you enter the carrier

LUF_1. The system automatically makes the carrier service codes for Fumigation, Loading, and Unloading available in the input

help of the field Carrier Service Code in the agreement.

Carrier Profile

## Definition

A profile with which you characterize transportation capabilities of a carrier.

## Use

You use this object to store information that is used in a similar constellation for multiple carriers. Carriers are business partners

(BPs) to which you have assigned the business partner role Carrier. You can only create one profile for each carrier.

## Structure

You can store the following objects in a carrier profile:

## Freight code sets

Transportation lane and carrier-specific parameters

Product freight groups

## Transportation groups

Equipment groups and equipment types

Fixed transportation costs

Dimension costs

## Integration

You make use of the carrier profile when creating transportation proposals (see Generation of Transportation Proposals) and when

selecting a carrier.

Definition of Carrier Profiles

## Use

You use this process to define a profile for a carrier.

This is custom documentation. For more information, please visit SAP Help Portal.

12


1/14/26, 2:16 PM
## Prerequisites

You have assigned the business partner role Carrier to the business partner for which you want to create a carrier profile

(see Definition of Business Partners).

You have defined transportation lanes in Customizing (see Definition of Transportation Lanes).

You have defined freight code sets in Customizing. For more information, see Customizing for Transportation Management

under  Master Data

 Transportation Lane

## Carrier Profile

 Define Freight Code Sets, Freight Codes, and

Determination .

You have defined product freight groups in Customizing. For more information, see Customizing for Transportation

Management under  Master Data

 Transportation Lane

## Carrier Profile

 Define Product Freight Groups .

You have defined transportation groups in Customizing. For more information, see Customizing for Transportation

Management under  Master Data

## Product

 Maintain Transportation Group .

You have defined equipment groups and equipment types in Customizing. For more information, see Customizing for

Transportation Management under  Master Data

## General Settings

 Define Equipment Groups and Equipment Types

.

You have defined means of transport in Customizing. For more information, see Customizing for Transportation

Management under  Master Data

## Resources

 Define Means of Transport

.

## Process

1. On the SAP Easy Access screen, choose  Master Data

## General

 Define Carrier Profile  or, from the launchpad, open

the Define Carrier Profile app.

2. You choose the carrier for which you want to define a profile and save your entry.

You can set the following attributes:

## Performance

Cont. Move (Continuous Move) checkbox

3. You make settings on the following tab pages:

## Transportation Lane

You can enter any attributes that are relevant for the carrier, such as the business share or the priority.

## Freight Code Set

You must specify the country or region and the means of transport to which the freight code set relates.

Product Freight Group

Transportation Group

## Equipment

You can enter information about the location of the equipment or the means of transport to which this equipment is

restricted.

## Fixed Transportation Costs

You can define fixed transportation costs for the means of transport of the carrier.

## Dimension Costs

This is custom documentation. For more information, please visit SAP Help Portal.

13


1/14/26, 2:16 PM

You can define dimension costs for the means of transport of the carrier.

4. Save your entry.

## Result

You have defined a profile for a carrier. You can search for settings that you have made in the carrier profile and identify all carriers

that have those settings.

Organizational Management

## Definition

A means for creating and managing the organizational and staffing structures in your company that uses an organizational model

as its basis.

In Transportation Management (TM), the organizational structure can be based on the structure of the ERP components or a

connected system (SAP ERP). To enable this, you can create the following organizational units:

## Corporate organization

This organization unit is optional and serves as a single entry point into the organizations structure in TM.

## Company organization

This organization unit corresponds to the ERP company code containing the local currency.

  Note
The company organization unit is used by transportation charge management (TCM) for invoicing and charging.

## Sales organization, office, and group

A sales organization in TM is represented as an organizational unit maintained within the organizational management

application.

A sales organization is an organization unit that has function “4” (Sales) and role “1” (Organization).

For each sales organization that you maintain in organizational management, you need to assign a BSG Org. Unit. This is

the ID of a sales organization that is used to retrieve sales organization-dependent business partner data and is maintained

in Customizing.

## Purchase organization and group

A purchasing organization in TM is represented as an organizational unit maintained within the organizational management

application.

A purchasing organization is an organizational unit that has function “2” (Purchasing) and role “1” (Organization).

For each purchasing organization that you maintain in organizational management, you need to assign a BSG Org. Unit.

This is the ID of a purchasing organization that is used to retrieve purchasing organization-dependent business partner

data and is maintained in Customizing.

## Forwarding house

A forwarding house in TM is represented as an organizational unit maintained within the organizational management

application.

This is custom documentation. For more information, please visit SAP Help Portal.

14


1/14/26, 2:16 PM

A forwarding house is an organizational unit that has function “89” (Forwarding House) and role “1” (Organization).

In TM, you can use a forwarding house as a sales organization and as a purchasing organization.

For each forwarding house that you maintain in organizational management, you need to assign a BSG Org. Unit.

This organizational unit is the ID of both a purchasing organization and a sales organization. Both are maintained in

Customizing. This means that the ID of the sales organization and the purchasing organization are identical.

If the forwarding house is used as a sales organization, the BSG Org. Unit ID that is assigned to it is used to retrieve sales

organization-dependent business partner data.

If the forwarding house is used as a purchasing organization, the BSG Org. Unit ID that is assigned to it is used to retrieve

purchasing organization-dependent business partner data.

Planning and execution organization and group

  Note

You can activate the checking of the organizational data of a business partner’s company or the sales or purchasing

organizational data. These checks ensure that all business partners with the carrier role or customer role involved in certain

business documents are assigned to one or both of the following:

To a sales organization or purchasing organization in the business partner’s company

To the sales organization or purchasing organization in the header of the business document

These checks are relevant for the following business documents:

Forwarding orders, forwarding agreements, and forwarding settlement documents

Freight orders, freight bookings, freight agreements, and freight settlement documents

You activate these checks in Customizing for Transportation Management under  Basic Functions

## General Settings

 Define General Settings for TM .

## More Information

For more information, go to http://help.sap.com/s4hana, choose the relevant release, and navigate to  Product Assistance

 Enterprise Business Applications

## Human Resources

 Personnel Management (PA)

.

Creation of Organizational Models

## Use

In Transportation Management (TM), you use this process to create organizational models for the organizations that take part in

transportation processes. You can create the organizational models according to a predefined hierarchical structure. You can

assign employees who take part in workflow processes to the organizational units.

## Process

1. You define an organizational model. To do so, on the SAP Easy Access screen, choose Customer Service

 Service

Processing

 Environment

## Organization

 Organizational Plan

 Organization and Staffing

 PPOCE - Create .

This is custom documentation. For more information, please visit SAP Help Portal.

15


1/14/26, 2:16 PM

2. You define organizational units (see Organizational Unit) and assign an appropriate organizational unit function and

organizational unit role to them.

  Recommendation
You can use transaction /SCMTMS/ORG_INT to transfer organizational units from core components of SAP S/4HANA

to TM.

3. You relate organizational units to other organizational units according to their organizational unit role and depending on the

organizational unit function.

  Note

The hierarchical relationship of organizational units is fixed.

For organizational units with a Sales unit function, you can define the unit roles Organization, Office, and Group.

Organizational units with unit role Group can be assigned to organizational units with a unit role Office or Organization,

and organizational units with a unit role Office to organizational units with a unit role Organization.

For organizational units with a Purchasing or Planning and Execution unit function, you can only assign organizational

units with a unit role Group to organizational units with a unit role Organization.

4. You assign employees to organizational units, see Assigning Employees to Organizational Units.

You can also create an TM organization structure. For more information, see Customizing for Transportation Management

under  Master Data

 Organizational Management

## Organizational Model

 Create and Merge Organizational

Hierarchy .

## Example

You want to re-create the structure of a purchasing organization or a planning and execution organization. You proceed as follows:

1. You create an organizational unit with a Purchasing or Planning and Execution unit function and an Organization unit role.

2. You create an organizational unit with a Purchasing or Planning and Execution unit function and a Group unit role.

3. You assign the organizational unit with the Group unit role to the organizational unit with the Organization unit role.

Organizational Unit

## Definition

An object that is used for mapping the organizational structure of a company in an organizational model. Each organizational unit

is defined in more detail by its unit function and unit role.

## Use

You can use this object as the basis for an organizational model by arranging organizational units hierarchically and therefore

mirroring the structure of your company.

  Note

You may only use the Organization or Group organizational unit roles for organizational units with the Purchasing or Planning

and Execution organizational unit functions.

This is custom documentation. For more information, please visit SAP Help Portal.

16


1/14/26, 2:16 PM
## Integration

You use organizational units with a Sales organizational unit function to create the following:

Forwarding orders

Forwarding quotations

## Forwarding settlements

You use organizational units with a Purchasing organizational unit function to create the following:

Freight orders

Freight bookings

## Freight settlements

You use organizational units with an Execution organizational unit function to create the following:

Resources (see Definition of Resources)

## Freight orders

For settlement integration, the system uses the business system group (BSG) assigned to an organization to determine whether

the settlement document should be posted to an external system, or to the internal Sales and Distribution (SD) or Materials

Management (MM) component of the SAP S/4 HANA system. For example, for posting the forwarding settlement document, the

system uses the sales organization specified in the forwarding settlement document to determine the BSG. The BSG indicates the

logical system from which the sales organization is replicated in the organization model. If this logical system is different to the

current client logical system, the settlement document is posted to the external SD using enterprise services. If the logical system

is the same as the current client logical system, the settlement document is posted to the internal SD component.

Assigning Employees to Organizational Units

## Prerequisites

You have defined a business partner (BP) of the type Person (see Definition of Business Partners).

You have assigned the business partner role (BP role) Employee to the BP and maintained any data relevant for this BP

role.

  Note

As a minimum, you need to enter the country or region in which this business partner resides.

## Context

You use this procedure to assign employees to organizational units in Transportation Management (TM).

## Procedure

1. Access the organizational model on the SAP Easy Access screen by entering PPOME (Change Organization and Staffing) in

the command field.

2. Select an organizational unit and choose the Create button.

This is custom documentation. For more information, please visit SAP Help Portal.

17


1/14/26, 2:16 PM

3. Choose Incorporates Position and enter a name and a description in the Position input field.

4. In the context menu of the employee symbol, choose Assign.

The Choose Relationship screen appears.

5. Choose Holder Central Person and enter the name of the business partner that you want to assign to the position in the

search dialog.

## Results

You have assigned an employee to an organizational unit by assigning a business partner with the role Employee to the

organizational unit.

The system establishes a correlation between the master data objects Organizational Unit and Business Partner.

Changing of Organizational Models

## Use

You can use this process to change an organizational model in Transportation Management (TM).

## Process

1. You change an organizational model. To do so, on the SAP Easy Access menu, choose Customer Service

 Service

Processing

 Environment

## Organization

 Organizational Plan

 Organization and Staffing

 PPOME - Change .

2. You search for an existing organizational unit.

3. You change attributes of the organizational unit, such as:

Organizational unit ID

Reference organizational unit ID

Organizational unit function

## Organizational unit role

Local currency (company organizations only)

Relationship with other organizational units

4. You save your entry.

The system automatically adds a technical business partner and sets the business system group.

Workflow in Transportation Management

## Definition

Sequence of steps processed either by people or by an SAP system.

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

18


1/14/26, 2:16 PM

Transportation Management (TM) uses SAP Business Workflow, which is a cross-application tool that enables the integration of

business tasks across whole application areas.

For more information, go to http://help.sap.com/s4hana, choose the relevant release, and navigate to  Product Assistance

 Enterprise Technology

 SAP Business Workflow .

An example of the use of the workflow capability in TM is the approval check that you can define. For more information, see

Approval Check.

  Note

You have to assign employees to organizational units to be able to use the workflow capabilities. For more information, see

Assigning Employees to Organizational Units.

Approval Check

## Use

You use this function to do the following:

Check whether a forwarding order or a forwarding quotation meets the value ranges defined in a condition for specific

attributes of the business document.

Trigger the workflow to get approval for the processing of a business document, freight agreement RFQ, agreement, or

validity period in a rate table.

When you save a business document, freight agreement RFQ, agreement, or validity period in a rate table, the system triggers the

approval workflow.

## Integration

You can use this workflow with forwarding orders, forwarding quotations, freight agreement RFQs, agreements, and rate tables.

## Prerequisites

You have customized the workflow engine. For more information, on the SAP Easy Access screen, choose  Tools

 Business Workflow

 Development

## Utilities

 Automatic Workflow Customizing .

You have enabled the approval workflow functionality as relevant in the following activities in Customizing for

Transportation Management:

## Master Data

 Agreement RFQs and Quotations

 Define Freight Agreement RFQ Types

Forwarding Order Management

## Forwarding Order

 Define Forwarding Order Types

Forwarding Order Management

## Forwarding Quotation

 Define Forwarding Quotation Types

## Master Data

 Agreements and Service Products

 Define Freight Agreement Types

## Master Data

 Agreements and Service Products

 Define FWA and Service Product Catalog Types

## Master Data

 Agreements and Service Products

 Define Internal Agreement Types

Master Data

## Rate Tables

## Define Rate Table Types

This is custom documentation. For more information, please visit SAP Help Portal.

19


1/14/26, 2:16 PM

If you want to be able to override the approval check for forwarding orders and forwarding quotations, you must implement

the Specific Checks for Approval Workflow in FWO Management (TRQ_APPR_CHECK_BO) BAdI. For more information,

see Customizing for Transportation Management under  Business Add-Ins (BAdIs) for Transportation Management

## Forwarding Order Management

 BAdI: Specific Checks for Approval Workflow in FWO Management

.

If you want to check mandatory fields in freight agreement RFQs before proceeding with the approval workflow, you must

implement the Specific Checks for Approval Workflow in Freight Agreement RFQs (/SCMTMS/RFQ_APPR_CHECK_BO)

BAdI. For more information, see Customizing for Transportation Management under  Business Add-Ins (BAdIs) for

Transportation Management

 Master Data

## Agreement RFQs

 BAdI: Specific Checks for Approval Workflow in Freight

Agreement RFQs .

If you want to check mandatory fields in agreements before proceeding with the approval workflow, you must implement

the Specific Checks for Approval Workflow in Agreements (/SCMTMS/FAG_APPR_CHECK_BO) BAdI. For more

information, see Customizing for Transportation Management under  Business Add-Ins (BAdIs) for Transportation

Management

 Master Data

## Agreements

 BAdI: Specific Checks for Approval Workflow in Agreements .

If you want to check mandatory fields in rate tables before proceeding with the approval workflow, you must implement the

Specific Checks for Approval Workflow in Rate Tables (/SCMTMS/RATES_APPR_CHECK) BAdI. For more information, see

Customizing for Transportation Management under  Business Add-Ins (BAdIs) for Transportation Management

 Master Data

## Rate Tables

 BAdI: Specific Checks for Approval Workflow in Rate Tables .

You have created an organizational unit, assigned a position to it, for example, Customer Agent, and assigned an employee

to this position. For more information, see Creation of Organizational Models. When creating the organizational unit, you

must have specified the following settings:

Marked the appropriate position as Head of own organizational unit.

Assigned the Sales organizational unit function to the organizational unit for forwarding orders and forwarding

quotations.

You have defined agents for the workflow in the Workflow Builder and you have defined the standard task as a general task

in the workflow. For more information, on the SAP Easy Access screen choose  Tools

 Business Workflow

 Development

 Definition tools

 Workflow Builder

 Workflow Builder

.

For business documents (not freight agreement RFQs, agreements, or validity periods in rate tables), you have assigned

conditions to the /SCMTMS/APPROV_TRQ condition type:

A condition assigned to this type specifies certain fields and the exact limits the system must consider for starting the

approval workflow. For example, a condition says that the gross weight must be bigger than 5.000 kg. At 5.001 kg the

approval workflow starts.

For more information about defining conditions, see Definition of Conditions.

## Features

When you create a freight agreement RFQ, agreement, validity period in a rate table, or a business document, the system sets the

status as follows:

## RFQ status in a freight agreement RFQ to In Process

Approval status in an agreement, or validity period in the rate table, to In Process

Approval status in a business document to Not Checked

## Freight Agreement RFQs

If you have enabled the approval workflow for RFQ publication, when you create individual freight agreement RFQs, the system

changes the status to Freight Agreement RFQs Created. In the freight agreement RFQ master under Follow Up, you can request

This is custom documentation. For more information, please visit SAP Help Portal.

20


1/14/26, 2:16 PM

publishing approval. The system changes the status to Awaiting Approval.

The customer agent or approver can approve or reject the publishing request. The system updates the status as follows:

If the agent or approver approves, the status changes to Published. The system publishes an individual freight agreement

RFQ to each of the relevant carriers.

If the agent or approver rejects, the status changes to Freight Agreement RFQs Created. You can change the details of the

RFQ master and publish the RFQ master again.

If you have enabled the approval workflow for agreement creation, in the freight agreement RFQ master under Follow Up, you can

request agreement creation approval. The system changes the status from Published to Awaiting Approval.

The customer agent or approver can approve or reject the agreement creation request. The system updates the status as follows:

If the agent or approver approves, the status changes to Ready for Agreement Creation.

If the agent or approver rejects, the status changes to Published.

You must create a new negotiation round or change the business share allocation.

## Agreements, Validity Periods in Rate Tables, and Business Documents

If you have enabled the approval workflow for agreements, validity periods in rate tables, and business documents, the system

changes the status as follows:

For an agreement, or a validity period in a rate table, when you request approval, the system changes the status of the

agreement or validity period in the rate table to Awaiting Approval. When you then save the agreement, or validity period in

the rate table, the system triggers the workflow process.

For business documents, when you first save the business document, the system checks the document against the value

ranges defined in the conditions and takes one of the following actions:

If the business document meets the value ranges defined in the conditions, the system changes the approval status

from Not Checked to No Approval Needed. You can then process the business documents further.

If the business document does not meet the value ranges defined in the conditions, the system changes the status

of the business document from Not Checked to Approval Needed. The system then triggers the workflow and

sends a message to the customer agent or approver.

  Note

An action in the Post Processing Framework (PPF) triggers the workflow. For more information about the PPF,

see Post Processing Framework (BC-SRV-GBT).

The customer agent or approver can approve or reject the agreement, validity period, or business document as follows:

If the agent or approver approves the business document, the approval status changes to Approved.

You can then process the business document further.

If the agent or approver approves the agreement or validity period, the approval status changes to Released.

You can then process the agreement or validity period further.

If the agent or approver rejects the business document, the approval status changes to Not Approved.

The system blocks the business document for further processing and triggers the workflow.

If the agent or approver rejects the agreement or validity period, the approval status changes to In Process.

This is custom documentation. For more information, please visit SAP Help Portal.

21


1/14/26, 2:16 PM

  Note

The customer agent or approver can cancel the processing of the workflow item. The workflow item then stays in the

personal inbox of the customer agent or approver and the system cannot process the agreement RFQ, business

document, agreement, or validity period further.

More Information

## Definition of Conditions

Post Processing Framework (BC-SRV-GBT)

Workflow in Transportation Management

## Transportation Network

You use this component in Transportation Management (TM) to define the following master data objects:

## Location

Transportation Zone

Transportation Lane

## Schedule

In conjunction with the means of transport, the transportation network (TN) defines the direct reachability of transportation zones

and locations for a particular vehicle resource.

Transportation Network Cockpit

## Use

You can use this function to display the following master data of the transportation network on a map:

## Locations

Transportation zones

Transportation lanes

Trade lanes

## Schedules

Default routes

## Connections

Business partner networks

## Features

## General Map Functions

This is custom documentation. For more information, please visit SAP Help Portal.

22


1/14/26, 2:16 PM

For more information, see Map Functions.

## Object Relationships

For the individual master data objects, you can determine other master data objects that have a relationship to them. Select a

master data object and then one of the search functions available in the context menu. The system adds the master data objects

determined to the map view.

## Display Options

You can use the display profile to select all the objects that are to be displayed on the map. The display profile is available in the

toolbar

You can set the display status for the individual master data objects. Select a master data object and then one of the functions

available for hiding objects in the context menu. The system then removes the master data objects determined from the map view.

You can hide the master data object itself, all the other master data objects, and the master data objects that do not have a

relationship.

## Activities

To call the transportation network cockpit, open the Transportation Network Cockpit app on the launchpad.

Path Finder

## Use

You can use this function to search for legs in your transportation network and take the following into account in the process:

## Locations

Transshipment locations

Transportation lanes

## Schedules

## Transportation zones

This enables you to easily determine whether a connection exists between two locations and, therefore, whether you have

correctly configured your master data.

  Note

The path finder does not take incompatibilities into account. For more information about incompatibilities, see

Incompatibilities.

## Integration

This function is available both in the transportation network cockpit and on the user interface for transportation proposals. In both

cases, the result of the path finder is displayed on the geographical map.

## Prerequisites

This is custom documentation. For more information, please visit SAP Help Portal.

23


1/14/26, 2:16 PM

You have defined the following objects:

Locations [mandatory] (see Definition of Locations)

Transshipment locations that are assigned to locations [optional] (see Transshipment Location)

Connecting transportation lanes [optional] (see Definition of Transportation Lanes)

Schedules [optional] (see Schedule Creation)

## Features

You can execute this function and check the result in either the transportation network cockpit or on the transportation proposals

user interface:

## Transportation Network Cockpit

When you open the context menu for a location in the transportation network cockpit, you can choose:  Find

 Connection

To Location...

 and enter a destination in the dialog box displayed. The system then calculates all of the available

connections in the transportation network and displays them on the map. The color of the connections indicates whether a

valid transportation lane or schedule exists.

## Transportation Proposals

When you call the user interface for transportation proposals, you can choose the appropriate pushbutton to show or hide

the available connections on the map. As in the transportation network cockpit, the color of the connections indicates

whether a valid transportation lane or schedule exists.

## Explanation Tool

When you select one or more freight units, you can choose the Show Network Path pushbutton to analyze the underlying

transportation network that is taken into account when planning the selected freight units.

## More Information

Transportation Network Cockpit

Generation of Transportation Proposals

Location

## Definition

A logical or physical place in which products or resources are managed on a quantity basis.

## Use

You use this business object as the basis for transportation processes. In transportation processes, you name a source location, a

destination location, and any transshipment locations necessary to complete the transportation process. For this purpose, you

define locations.

## Structure

This is custom documentation. For more information, please visit SAP Help Portal.

24


1/14/26, 2:16 PM

A location is identified by a name. To define a location, you have to specify its name and type. Transportation Management (TM)

provides standard location types such as the following:

Production plant (1001)

Distribution center (1002)

Shipping point (1003)

Transportation zone (1005)

Business Partner (1021)

Terminal (1030)

Store (1040)

Port (1100)

Airport (1110)

Railway station (1120)

Container freight station (1130)

Hub (1140)

Gateway (1150)

Container yard (1160)

Warehouse (1170)

Carrier warehouse (1180)

Loading point (1200)

In TM, you use the location type as a means for categorizing locations. Location types are not used for controlling business

processes, they are only used as a means of reference.

## Integration

This business object is used throughout TM in almost every business process, including the following:

Definition of more complex master data objects that are part of the transportation network, such as transportation zones,

transportation lanes, or schedules.

Definition of other master data objects, such as resources.

Definition of loading requirements. You can specify for vehicle resources and locations whether they can be loaded or

unloaded from the left, right, back, or top. Further, you can specify the equipment that is attached to a vehicle resource and

the equipment that is required for loading and unloading at a location, for example, a forklift. A vehicle resource can only be

loaded or unloaded at a location if it fulfills at least one of the loading direction requirements and all of the attached

equipment requirements of this location. For more information see Loading Requirements for Locations.

Definition of incompatibilities. For example, a location may be marked as having a restriction in regards to the delivery of

goods by means of a specific vehicle resource.

Creation of forwarding orders, freight units, planned transportation activities, executed transportation activities, and so on.

## Locations of Business Partners

This is custom documentation. For more information, please visit SAP Help Portal.

25


1/14/26, 2:16 PM

A business partner can have multiple standard addresses and multiple delivery addresses. One standard address is valid at any

one time. In TM, one business partner can have multiple locations. For every relevant address of a business partner, you can create

a respective location. The address number of the location is the same as the address number of the business partner. When TM

receives a sales document or outbound delivery, it receives address data which it uses to determine the correct location, taking

into account the validity dates of the address.

More Information

Definition of Locations

Transshipment Location

One-Time Location

## Definition

A location that is stored as a transient master data object in the system.

## Use

You use one-time locations in business processes that require the input of locations that have not been defined as master data

objects, such as the creation of forwarding orders. The system creates one-time locations based on one-time address details that

you can specify on the user interface.

## Structure

A one-time location is specified by the name of the organization, its address data, its communication data, or a combination of

these.

You can create a note for each one-time location. When you create a note, you can only define one note per location and language.

## Integration

To find addresses for one-time locations using the input help (F4), complete the Customizing activities for SAP NetWeaver

under  Application Server

 Basis Services

## Address Management

 Regional Structure/City File .

In Customizing, you can activate an address search that determines whether one-time locations match locations that

already exist. For more information, see Customizing for Transportation Management under  Basic Functions

 General

## Settings

 Define General Settings for TM .

In the standard system, all user roles have been configured so that users can read the details of one-time locations. If you

reconfigure the roles to suite your business needs, we recommend that you do the following:

Configure all roles available in Transportation Management (TM) so that users assigned to them can read the details

of one-time locations.

Configure the roles that are used for creating or changing forwarding orders (see Forwarding Order), such as the

transportation booking agent, so that they can create one-time locations.

## More Information

You can activate the following BAdI implementations for one-time locations:

This is custom documentation. For more information, please visit SAP Help Portal.

26


1/14/26, 2:16 PM

A customer-specific address search for one-time locations. For a possible implementation, see Customizing for

Transportation Management under  Business Add-Ins (BAdIs) for Transportation Management

 Master Data

 General

## Settings

## One-Time Locations

 BAdI: Customer-Specific Search Logic for Locations Based on Address Data .

The adjustment of location data created for one-time locations. For a possible implementation, see Customizing for

Transportation Management under  Business Add-Ins (BAdIs) for Transportation Management

 Master Data

 General

## Settings

## One-Time Locations

 BAdI: Adjustment of Location Data Created for One-Time Locations .

Transshipment Location

## Definition

A location that is used for unloading goods from one vehicle resource and loading it onto another vehicle resource during the

transportation process.

## Use

You use transshipment locations when different means of transport or different carriers have to be used in the transportation

process. You can also use transshipment locations when consolidating or de-consolidating goods to be transported.

## Structure

A transshipment location is defined by assigning a location to either another location or to a transportation zone (see

Transportation Zone).

When you assign a transshipment location to a transportation zone, it can be used as a transshipment location by all locations that

are part of that transportation zone.

  Note
You cannot define a transshipment location by assigning a location to itself.

  Recommendation
For a better system performance, we recommend that you define only transshipment locations that you use.

## Integration

If you define a transshipment location and want to use it in your transportation processes, you must define transportation lanes

(see Transportation Lane) that take the transshipment location into account.

  Example
You want to transport goods from location A to location C. You have to unload some goods in location B and change your means

of transport. Location B is therefore a transshipment location.

For this transportation process to take place, you have to define the following:

1. A transshipment location B

2. A transportation lane from A to B and a transportation lane from B to C

This is custom documentation. For more information, please visit SAP Help Portal.

27


1/14/26, 2:16 PM

For more information, see Examples for the Transshipment Location.

Define Transshipment Location Assignments

## Use

You, as a system administrator, can use this report to display, create, and delete transshipment location assignments as follows:

You can display transshipment location assignments for selected locations, transportation zones, and transshipment

locations. You can display all transshipment location assignments in the system, by selecting the Display All Assignments

checkbox.

You can assign locations and/or transportation zones to one or more transshipment locations.

You can delete transshipment location assignments for selected locations, transportation zones, and transshipment

locations. To simulate the deletion of transshipment location assignments before deleting the assignments from the

system, you select the Simulate Deletion checkbox.

## Activities

To define transshipment location assignments, on the SAP Easy Access screen choose  Logistics

## Master Data

 Transportation Network

## Location

 Define Transshipment Location Assignments .

Examples for the Transshipment Location

Example 1

You want to transport goods from location A to location C. You have defined the transshipment location B for the location A. This

situation is depicted in the following figure (the transshipment location is displayed with a blue background):

## Examples for the Transshipment Location

This is custom documentation. For more information, please visit SAP Help Portal.

28


1/14/26, 2:16 PM

You have the following options for transporting goods from location A to location C (provided you have defined the respective

transportation lanes):

## A to C

You can transport the goods directly from location A to location C.

## A to B to C

You can transport the goods to location B first, and from location B to location C.

Example 2

You want to transport goods from location A to location D. You have defined the transshipment location B for the location A, and

the transshipment location C for the location D. This situation is depicted in the following figure (the transshipment locations are

displayed with a blue background):

## Examples for the Transshipment Location

You have the following options for transporting goods from location A to location D (provided you have defined the respective

transportation lanes):

## A to D

A to B to D

A to C to D

A to B to C to D

Example 3

You want to transport goods from location A to location D. You have defined the transshipment location B for the location A, and

the transshipment location C for the location B. This situation is depicted in the following figure (the transshipment locations are

displayed with a blue background):

This is custom documentation. For more information, please visit SAP Help Portal.

29


1/14/26, 2:16 PM

## Examples for the Transshipment Location

You have the following options for transporting goods from location A to location D (provided you have defined the respective

transportation lanes):

## A to D

A to B to D

A to B to C to D

  Note

In this example, you cannot transport goods from A to C to D, since C is not a transshipment location for the location A.

Example 4

You want to transport goods from location A to location D. You have defined the transshipment location B for the location A and the

location C. This situation is depicted in the following figure (the transshipment location is displayed with a blue background):

This is custom documentation. For more information, please visit SAP Help Portal.

30


1/14/26, 2:16 PM

## Examples for the Transshipment Location

You have the following options for transporting goods from location A to location D (provided you have defined the respective

transportation lanes):

## A to D

A to B to D

  Note
In this example, you cannot transport goods from A to B to C to D, since C is not a transshipment location for the location B.

Example 5

You want to transport goods from location A to location E. You have defined the transshipment locations B, C, and D for the

location A, and specified that B and C are mutual transshipment locations. This situation is depicted in the following figure (the

transshipment locations are displayed with a blue background):

This is custom documentation. For more information, please visit SAP Help Portal.

31


1/14/26, 2:16 PM

## Examples for the Transshipment Location

You have the following options for transporting goods from location A to location E (provided you have defined the respective

transportation lanes):

## A to E

A to B to E

A to C to E

A to D to E

A to B to C to E

A to C to B to E

Definition of Locations

## Use

You use this process to define locations in Transportation Management (TM).

  Note

If you create locations for a referring entity like business partners, shipping points, and plants, you should use the report

/SAPAPO/CREATE_LOCATION, to ensure that the addresses of locations and the referring entity are consistent. For more

information, see Creating Locations.

## Process

1. From the launchpad, you open the Define Location app (/SCMTMS/LOC3).

2. You specify your location, choose the location type, and choose Create.

3. You describe your location and enter location-specific data on the following tab pages:

## General

This tab page contains information about standard identification numbers for the location and the reference object

of the location, for example, the business partner. It also contains geographical data of the location, the business

partner that owns the location, and the priority of the location for business processes.

## Address

This tab page contains information about the contact details for the location, such as street address, PO box

address, and communication data.

  Note

If you enter data on the Address tab page, the system calculates the geographical data for the location and

enters the values in the corresponding fields on the General tab page. For this process to take place, as a

minimum you must specify the country or region code of the location.

The system can use a third-party geocoding program to calculate the geographical data. For more information,

see Geocoding.

This is custom documentation. For more information, please visit SAP Help Portal.

32


1/14/26, 2:16 PM

Note that with TM, we do not deliver a third-party geocoding program.

## Alt. Identifiers

This tab page contains information about the alternative location identifiers defined for the location. For more

information, see Definition of Alternative Location Identifiers

TM

This tab page contains information about the goods wait time of products for the location. You can also enter

information related to air cargo security (for example, the shipper security status for the location). For more

information, see Configuration of Air Cargo Security.

## Resources

This tab page contains information about restrictions that apply for this location in regards to resources and

operating times of resources for the inbound and outbound processes.

Addit. (Additional)

This tab page can contain distinctive information that you want to store with locations.

4. You save the location.

## Result

You have created locations. You can change or display locations that you have defined using the Define Location app, which you

can open from the launchpad.

  Note

If you search for an existing location by entering a business partner, and the business partner has multiple addresses, a popup

appears where you can choose the address for which you want to display the location.

You can use the locations in transportation processes, such as the creation of forwarding orders or the definition of resources.

Operating Times

## Definition

Time stream that describes the availability of a location.

## Use

You use this business object to specify at which times loading and unloading activities can take place at a specific location, and at

which times transportation activities can start or end at this location.

You can consider a multiple-shift operation when specifying operating times for a location.

## Integration

You specify operating times for a location by using a calendar resource (see Calendar Resource). On the Resources tab page of the

Change Location screen, you can assign calendar resources for the inbound and outbound delivery to the location.

This is custom documentation. For more information, please visit SAP Help Portal.

33


1/14/26, 2:16 PM

  Note

Several locations can refer to a single calendar resource.

VSR optimization (VSR = vehicle scheduling and routing) considers operating times only if you have specified values

greater than zero for loading and unloading durations (see Loading and Unloading Durations).

## Creating Locations

## Creating Locations Using a Report

You can use report /SAPAPO/CREATE_LOCATION to create new locations for plants, shipping points and business partners. This

is useful if you have a lot of entities for which you require locations.

To run the report you select from plants, shipping points and business partners. You can choose whether the report creates

locations only for the standard addresses of the entity, or for both the standard addresses and delivery addresses. The report

identifies all selected entities which have no location, and the system:

Creates a location using the existing address of the entity

## Calculates geocodes

Creates a transportation zone location if needed

Updates the location to zone assignment

## Creating Locations out of Business Documents

If you create or update a document that is relevant for Transportation Management (TM), the system checks that all necessary

locations needed to represent plants, shipping points and business partners in TM are present in the system. If a location has not

already been created, the system creates it. You can create locations, on demand, from the following TM-relevant business

document categories:

SD Documents

Sales Order (SO)

MM Documents:

Purchase Order (PO)

Stock Transfer Order (STO)

## Deliveries

Outbound Deliveries

## Inbound Deliveries

## Creating Locations out of Business Partner Master

For business partners, the system can be configured to immediately create locations when you create and save a business partner.

To do so you need to implement business add-in (BAdI) /SAPAPO/LOC_CREATE which allows you to specify the conditions for

creating or updating a location when a business partner is saved. Once you create a location, the system triggers any updates as

This is custom documentation. For more information, please visit SAP Help Portal.

34


1/14/26, 2:16 PM

you make a change to the business partner address.

Related Information

## Creation of Locations

Loading Requirements for Locations

You can define loading requirements for locations.

These requirements can be taken into account in VSR optimization, load consolidation, and for the generation of transportation

proposals. The system considers the requirements specified for locations and resources and can identify incompatibilities that

would, for example, make a resource unsuitable for use at a specific location. For manual planning, you can specify how the system

should handle, for example, a plan that includes a resource that is not compatible with the specified location.

## Features

## Loading Direction Profiles

You can use loading direction profiles to specify:

the direction from which loading or unloading is possible

a preference for loading direction, if required (not yet supported)

For more information see Customizing for Transportation Management under  Master Data

 Transportation Network

## Location

 Define Loading Direction Profile .

You can also specify loading direction profiles for resources. For more information see Loading Requirements for Vehicle

Resources.

## Attached Equipment Profiles

You can define attached equipment profiles that describe the equipment provided by the location for loading/unloading. For more

information see Customizing for Transportation Management under  Master Data

 Transportation Network

## Location

 Define Attached Equipment Profile .

You can also define attached equipment profiles to describe the equipment provided by a resource for loading/unloading. For more

information see Loading Requirements for Vehicle Resources.

In assessing compatibility, the system compares the location’s attached equipment profile with the resource’s attached

equipment profile. Other equipment that is assigned to the resource, for example, loading equipment in a vehicle loading profile, is

not relevant in this context.

## Location Loading Profiles

You can use location loading profiles to define specific loading constraints for a location as follows:

## Loading Direction Profile

Loading Equipment Required (not yet supported)

Defines for which loads a resource must provide a loading equipment at this location:

This is custom documentation. For more information, please visit SAP Help Portal.

35


1/14/26, 2:16 PM

For no loads

## For all loads

## For loads in double-deck resources

For more information see Customizing for Transportation Management under  Master Data

 Transportation Network

## Location

 Define Location Loading Profile .

## Planning Profile

In the incompatibility settings of your planning profile, you can define constraints for loading direction and attached equipment.

Note that once you define these constraints, we recommend that you check and adapt your master data. That means, add the

loading direction profile and the attached equipment profile to the locations and vehicle resources that should consider these

constraints.

Example: If a location has no loading direction profile defined, no restrictions with regards to this constraint are applied. That

would mean, vehicle resources can be loaded or unloaded from all sides at this location.

For more information, see Planning Profile.

## Related Information

Loading Requirements for Vehicle Resources

## Planning Profile

## Updating Locations Using a Report

The following reports are available for you to use to update your locations.

You can use the report /SAPAPO/UPD_LOC_SP_PL to update locations for plants and shipping points. You can trigger this

report in the following situations:

After making changes in the address data that are relevant for the geocodes of plants and shipping points

## On a scheduled basis, to capture any changes made during a specific period

It may happen that users create multiple instances of the same location in the system, for example, for business partners,

plants or shipping points, and that the system assigns different address numbers to these instances. You can use the report

/SAPAPO/UPDATE_LOC_ADDRNR to overwrite the address numbers of such locations. For locations of business partners,

this is only possible if the business partner has just one standard address.

The report assigns the location the same address number as the original entity. Furthermore, location details like geocodes

or transportation zone assignments are updated according to the new address. Details are written into the application log.

  Note

You can also use the report /SAPAPO/UPDATE_LOC_ADDRNR after executing the report /SAPAPO/FILL_LOCASGMT,

to correct any errors in cases where the address number of the original entity is not equal to the address number of the

corresponding location.

Related Information

## Updating Locations

This is custom documentation. For more information, please visit SAP Help Portal.

36


1/14/26, 2:16 PM

Deleting Locations

## Use

You can use this procedure to delete locations that have become obsolete in Transportation Management (TM).

## Prerequisites

1. You have checked if dependencies exist by generating a Where-Used List. For example, forwarding orders or resources may

depend on locations.

To generate a Where-Used List, do the following:

a. On the SAP Easy Access screen, choose  Logistics

 Transportation Management

 Master Data

 WUF – Where-

Used List

.

b. On the Where-Used List screen, enter the object type you want to check. In the Selection Criteria screen area, enter

the object value you want to check. For example, enter a location ID in a location check..

c. Under Object Name on the left hand side of the screen, select the object you want to check. On the right hand side

of the screen, choose the appropriate hosting object. For example, choose Transportation Document or Model for a

location.

The system displays the where-used information for the object you select.

2. You have eliminated any dependencies involving the locations.

  Note

Do not remove the technical dependency on the default model.

## Procedure

1. In the launchpad, open the Define Locations app and enter or choose the location you want to delete.

2. Select the Deletion Flag checkbox for the location by choosing  More

## Location

 Deletion Flag .

  Note

If you have selected the Deletion Flag checkbox for a location and you no longer want to delete the location, you can

deselect it at any time before deletion by choosing  More

## Location

 Deletion Flag.

3. If necessary, repeat steps number 1 and 2 to select the Deletion Flag checkbox for other locations.

4. Delete all locations that have been flagged for deletion by choosing  More

## Extras

 Delete Locations.

  Note

The system administrator may have scheduled a background job that deletes locations that have been flagged for deletion

periodically. In this case, you do not have to delete the locations manually as described in step number 4.

## More Information

## Deleting One-Time Locations

The procedure described above is not valid for deleting one-time locations (see One-Time Location).

This is custom documentation. For more information, please visit SAP Help Portal.

37


1/14/26, 2:16 PM

The system can delete one-time locations as soon as all dependencies of the individual one-time location to business processes

have been eliminated.

The system starts the deletion process for one-time locations when you carry out step number 4 as described above or when the

system starts a scheduled background job.

  Example

The system deletes one-time locations of a forwarding order if you do not save the forwarding order or if you delete the

forwarding order.

Application Logs for Locations

## Use

You use this function to collect messages, exceptions, and errors that have been stored in the system for a specific object, such as

a location. Logs can be displayed and deleted from the database.

## Features

The application log shows you messages issued by specific programs, such as the following:

## The deletion program for locations

The application log for this program provides you with an overview of where references to the deleted location still exist. You

can then remove these.

All programs capable of running in the background

## Activities

You can display logs for locations using the Application Logs app, which you open from the launchpad.

Use of Change Documents for Locations

## Use

You use this process to trace changes that are made to locations in Transportation Management (TM).

The changes are logged in change documents, which allow you to find out at any time, what was changed, when the changes

occurred, and how the changes were made. Change documents facilitate the analysis of errors. To use change documents for

locations, you have to define the business object as a change object in the system.

## Process

1. You activate change documents in Customizing. For more information, see Customizing for Transportation Management

under  Master Data

 Transportation Network

## Location

 Activate Change Documents .

2. You display the change documents for locations by opening the Display Change Documents app from the launchpad.

This is custom documentation. For more information, please visit SAP Help Portal.

38


1/14/26, 2:16 PM

Definition of Alternative Location Identifiers

## Use

You use this function to define alternative location identifiers (ALI) in Transportation Management (TM).

Once defined, you can use an ALI in transportation processes such as the creation of forwarding orders or the definition of

resources.

## Prerequisites

You have defined at least one ALI type in Customizing for Transportation Management under  Master Data

 Transportation Network

## Location

 Configuration for Alternative Location Identifiers .

If you want to use an ALI type with a strict code list, you must have defined a code list and type in Customizing for

Transportation Management under  Master Data

 Transportation Network

## Location

 Configuration of Alternative

Location Identifiers .

If you want to add an ALI to an existing location, this location must have been previously defined.

For more information, see Definition of Locations.

## Activities

1. You open the Define Locations app from the launchpad, then you either navigate to an existing location where you want to

add an ALI, or you select the Alt. Identifiers tab while you are defining a new location.

2. You specify the ALI Type and Alternate ID in the ALI table.

  Note

If you are using an ALI type with a defined code list, the value of the Alternate ID table entry must be a member of the

list.

3. You now repeat step 2 to add as many additional alternative location identifiers as you require.

4. You save the location.

## Geocoding

You can determine geographical coordinates (geocoordinates) based on address data.

## Use

The term geocoding comes from the area of geographical data processing. It describes the process for determining the

geocoordinates (longitude, latitude, and altitude) from the address data given. There are various commercial geocoding programs

that determine the required data using the address attributes (country, region, postal code, city, street, and so on).

You can use geocoordinates to do the following:

Display of business objects on a map, for example a location (localization of a business object on a map using address

data)

This is custom documentation. For more information, please visit SAP Help Portal.

39


1/14/26, 2:16 PM

Determination of the distance (distances can be calculated on the earth's surface from the geocoordinates determined; for

example, as a first approximation as the crow flies or with the relevant map material on a street basis)

Routing (for example, determination of a route on a street basis during transportation planning)

## Prerequisites

If you want to calculate simple geocoordinates based on country and region, you need to make the respective settings in

Customizing for ABAP Platform under  General Settings

 Set Geocoding .

If you want to calculate more precise geocoordinates, you need to set up the integration with SAP HANA spatial services.

For more information, see Standard Integration with SAP HANA spatial services.

If you have set up the integration with SAP HANA spatial services, you need to use the process controller framework to

ensure a more flexible approach to the determination of geocoordinates. The process controller framework is a flexible

framework that enables you to create different geocoding strategies so you can connect to external geographical

information systems (GIS) different from the standard geocoding program. This flexibility allows you to use third-party GIS

providers if required. You configure the process controller for geocoding in Customizing. For more information, see

Customizing for Transportation Management under  Master Data

 Transportation Network

 Location

## Geocoding

 Configure Process Controller for Geocoding .

## Features

## Geocoding Levels

You use geocoding levels to store geocoordinates for the address of a location on different levels of detail, for example by house

number, postal code, or region. Having different levels of detail for the geocoordinates of a location allows you to improve the

performance of the distance and duration determination between two locations. This is important if, for example, you have a large

number of locations geocoded on a high level of detail thereby making the distance and duration determination a performance

critical process. The lower the accuracy level the more locations share the same geocoordinates.

You can define the geocoding strategy that a geocoding level uses as well as which geocoding program to use and which address

fields to pass. Moreover, you can specify a GIS zone. You define geocoding levels in Customizing (see Customizing activity Define

Geocoding Levels).

  Example

You have two transportation lanes. Transportation lane A contains the start location WALLDORF and the destination location

MUNICH. Transportation lane B contains the start location WALLDORF and the destination location REGENSBURG. In the

location master, MUNICH and REGENSBURG are part of the same region and geocoded to be part of the same region.

When determining the distances and durations, the system first determines the distance and duration for transportation lane A

and saves the data in the buffering table. As transportation lane B ends in the same region, the system can reuse the data in the

buffering table instead of running a second determination of distance and duration thereby increasing the performance of the

system. The system only needs to call the distance and duration determination program once. You can define the required

accuracy level in Customizing (see Customizing activity Define Strategy for Distance and Duration Determination and

Georouting).

  Note
If you delete geocoding levels in the system, you can delete geocoordinates that have become obsolete as a consequence of

this. To delete obsolete geocoordinates, you can use the Delete Obsolete Geocoordinates report. For more information, see

Deletion of Obsolete Geocoordinates.

This is custom documentation. For more information, please visit SAP Help Portal.

40


1/14/26, 2:16 PM

## Mass Geocoding

If you want to maintain geocoding for multiple locations, you can use the Mass Geocoding report. For more information, see Mass

Geocoding.

## Validity of Geocoordinates

In the Customizing activity Define GIS Providers, you can indicate the validity of geocoordinates based on the GIS strategies for a

given GIS provider. The validity specifies the number of days or hours that geocoordinates from a GIS provider are stored in the

system before they are automatically deleted and redetermined. You can also indicate whether and how GIS data is to be stored. It

can be stored based on the validity of the GIS provider (in days) or the validity of the GIS strategy (in hours).

For more information, see Customizing for Transportation Management under  Master Data

 Transportation Network

 Geographical Services

 Define GIS Providers .

## Related Information

Distance and Duration Determination (DDD)

## Calculation of Transportation Zone Coordinates

You can calculate geographical coordinates (geocoordinates) for transportation zones, allowing you to determine distances

between business partners, for example.

## Use

You can use this program to calculate geocoordinates that represent the geolocation of a transportation zone. A geolocation is

defined by the following data:

Latitude

Longitude

## Time zone

Precision of the geolocation (for example, continent, country, region, postal code)

The system calculates the transportation zone coordinates by means of a geocoding program. The program determines the

geographical latitude and longitude of the transportation zone. You can use this data to calculate the distance between two

business partners, for example.

The geocoding is carried out according to the required precision, which may be defined at the level of country, region, postal code,

place, street, or house number.

## Prerequisites

You have entered the necessary address data. The system calculates the transportation zone coordinates on the basis of this

address data.

## Activities

On the SAP Easy Access screen, choose  Logistics

 Transportation Management

## Master Data

 Transportation Network

## Transportation Zone

 Calculate Transportation Zone Coordinates .

This is custom documentation. For more information, please visit SAP Help Portal.

41


1/14/26, 2:16 PM

Choose the transportation zones for which you wish to calculate the coordinates from the list of results and then choose Calculate

Coordinates. The system calculates the coordinates of the selected transportation zones. You will find the geographical data of the

transportation zones on the General tab page of the location master record.

## Mass Geocoding

You can calculate geographical coordinates (geocoordinates) for multiple locations.

## Use

You use this report to calculate geooordinates for longitude and latitude for your locations. Geocoordinates are essential for the

distance and duration calculation between two or more locations. The system defines the geocoordinates for a location using the

following data:

Longitude

## Latitude

Precision of the location (for example country, region, postal code, street, house number)

Match (percentage to which the geocoordinates match with the address defined in the location)

The report allows you to display existing geocoordinates from the database, to simulate geocoordinates that the geocoding

program provides, or to directly overwrite existing geocoordinates for locations. You determine geocoordinates by defining a

selection from the following:

## Location

Location type

## Transportation zone

## Validity end of geographical data

You can indicate the validity of geocoordinates in the Customizing activity Define GIS Providers. For more information, see

Geocoding.

Once you have a selection, you define if you want to calculate geocoordinates for all selected locations or only for locations that do

not yet have geocoordinates as follows:

If you want the system to calculate geocoordinates for all of your selected locations, select the All Selected Locations radio

button.

  Note

If you have defined geocoding levels in Customizing, the system calculates the geocoordinates on the basis of the

geocoding levels.

If you want the system to only calculate geocoordinates for those locations that have initial geocoordinates, select the Only

Locations Without Existing Geocoordinates radio button. You select the radio button for locations where no

geocoordinates were calculated upon the initial maintenance, or for locations that were transmitted from a back-end

system by means of the Core Interface. If you want the system to only calculate geocoordinates for those locations that

have initial geocoordinates on that geocoding level, additionally select a specific geocoding level.

If you want to calculate geocoordinates based on a specific geocoding level, select the Only Specific Geocoding Level radio

button.

This is custom documentation. For more information, please visit SAP Help Portal.

42


1/14/26, 2:16 PM

Furthermore, you can execute geocoding as follows:

If you want the system to display existing geocoordinates from the database for selected locations, select the Show

Existing Geocoordinates radio button.

If you want the system to simulate the geocoordinate determination, select the Simulate Geocoordinates radio button.

If you want the system to overwrite any existing geocoordinates with the geocoordinates that result from this calculation,

select the Overwrite Geocoordinates radio button.

## Prerequisites

The system calculates initial geocoordinates for a location on the basis of existing address data. You must therefore ensure

that you enter all relevant information (at least country or region) in the address data fields for your locations in the

location master.

You have defined geocoding levels in Customizing. For more information, see Customizing for Transportation Management

under  Master Data

 Transportation Network

 Location

## Geocoding

 Define Geocoding Levels .

## Activities

To access the Mass Geocoding report, on the SAP Easy Access, screen choose  Logistics

 Transportation Management

## Master Data

 Transportation Network

## Geocoding

 Mass Geocoding .

To access the Mass Geocoding in Batch report, on the SAP Easy Access, screen choose  Logistics

 Transportation

Management

## Master Data

 Transportation Network

## Geocoding

 Mass Geocoding in Batch .

## Deletion of Obsolete Geocoordinates

You can delete geographical coordinates (geocoordinates) after deleting geocoding levels.

## Use

You use this report to delete obsolete geocoordinates after one or more geocoding levels have been deleted.

## Prerequisites

You have defined geocoding levels in Customizing. For more information, see Customizing for Transportation Management under

## Master Data

 Transportation Network

 Location

## Geocoding

 Define Geocoding Levels .

## Features

You can simulate the deletion of obsolete geocoordinates by deselecting the Delete Obsolete Geocoordinates checkbox. You can

use the Delete Geocoordinates in Batch report to schedule background processing for the deletion of obsolete geocoordinates

after one or more geocoding levels have been deleted.

## Activities

To access the Delete Geocoordinates report, on the SAP Easy Access, screen choose  Logistics

 Transportation Management

## Master Data

 Transportation Network

## Geocoding

 Delete Geocoordinates .

This is custom documentation. For more information, please visit SAP Help Portal.

43


1/14/26, 2:16 PM

To access the Delete Geocoordinates in Batch report, on the SAP Easy Access, screen choose  Logistics

 Transportation

Management

## Master Data

 Transportation Network

## Geocoding

 Delete Geocoordinates in Batch .

Transportation Zone

## Definition

An object that groups a number of locations.

## Use

You use this business object to group locations into transportation zones. The system can partly transfer the properties that you

assign to a transportation zone to all its locations. This function reduces the volume of master data stored in the system.

  Example

A number of locations are supplied by the same warehouse. You group these in a transportation zone.

## Structure

A transportation zone is identified by a name. To define a transportation zone, you specify its name and type. In Transportation

Management (TM), the following types of transportation zones exist:

Direct zone

Postal code zone

Region zone

Mixed zone

  Note

A mixed zone is a combination of any of the other zone types.

## Integration

This business object is used in the definition of more complex master data objects that are part of the transportation network such

as transportation lanes (see Transportation Lane).

Definition of Transportation Zones

## Use

You use this process to define transportation zones in Transportation Management (TM).

## Prerequisites

You have defined locations (see Definition of Locations).

This is custom documentation. For more information, please visit SAP Help Portal.

44


1/14/26, 2:16 PM
## Process

1. You define a transportation zone in the Transportation Network Cockpit app, which you open from the launchpad.

2. You create a transportation zone by entering its name and a description for the zone.

  Note

The system automatically sets the zone type to M (mixed). If you require a different zone type, you can change the zone

type using the input help ( F4 ).

3. Depending on the type of transportation zone, you assign or exclude locations by creating entries on one of the following

tab pages:

## Zone – Location

To define a direct zone, you create entries on this tab page. You assign locations to the transportation zone directly

by entering the name of each location. You exclude locations by selecting the Exclude checkbox.

## Zone – Postal Code

To define a postal code zone, you create entries on this tab page. You assign locations to the transportation zone by

specifying a postal code range that is valid for a particular country or region.

## Zone – Region

To define a region zone, you create entries on this tab page. You assign locations to the transportation zone by

specifying a country/region and a region. If you only enter a country/region, the system automatically chooses all

regions of this country/region.

  Note

If you want to define a mixed zone, you can create entries on more than one tab page.

4. You save your entries.

  Caution

If you have defined a direct zone, a postal code zone, or a region zone, and you enter information on any other tab page, the

system automatically changes the type of transportation zone to a mixed zone. This change is irreversible.

Transportation Zone Hierarchy

## Definition

A hierarchy that can be defined for transportation zones.

## Use

You use this object to structure transportation zones hierarchically by assigning one transportation zone to another. All locations

included in a zone that is assigned to another zone, are automatically also part of that other zone.

Transportation zones that are included in a transportation zone hierarchy inherit properties of the superordinate zone.

The following conditions apply when you define a transportation zone hierarchy:

This is custom documentation. For more information, please visit SAP Help Portal.

45


1/14/26, 2:16 PM

You cannot assign a transportation zone to itself.

You cannot assign a transportation zone to another zone if the former already contains the other zone.

## Structure

A transportation zone hierarchy is defined by its name and its hierarchy structure.

## Integration

The VSR optimizer takes the transportation zone hierarchy into account during the optimization run.

The lane determination function takes the transportation zone hierarchy into account when determining a specific

transportation lane (see Lane, Distance, and Duration Determination (LDDD)).

The transshipment location determination function takes the transportation zone hierarchy into account when determining

all valid transshipment locations for a location.

Defining a Transportation Zone Hierarchy

## Prerequisites

You have defined transportation zones (see Definition of Transportation Zones).

## Context

You use this procedure to define a transportation zone hierarchy in Transportation Management (TM).

## Procedure

1. You define a transportation zone hierarchy in the Transportation Network Cockpit app, which you open from the

launchpad.

2. Enter RELH_ZONE as the name of the transportation zone hierarchy.

3. Enter RELHS_ZONE as the name of the hierarchy structure.

  Note

TM delivers the hierarchy structure as standard.

4. Choose Create.

5. Assign transportation zones to the transportation zone hierarchy by using the Hierarchy Fast Entry screen area or by

assigning them directly in the tree structure.

6. Save your entries.

Calculation of Geographical Data for a Transportation Zone

## Use

You use this process to calculate the geographical data of the geographical center of a transportation zone. The calculation is

based on the geographical data of all locations that are part of the transportation zone. The system calculates the following

This is custom documentation. For more information, please visit SAP Help Portal.

46


1/14/26, 2:16 PM

geographical data:

Latitude

Longitude

## Time zone

Precision (continent, country, region, and postal code)

  Note

In Transportation Management the precision is calculated based on the country and region of the locations.

The system uses the calculated data, for example, to increase the precision of a transportation lane when calculating the distance

between locations or zones.

## Prerequisites

You have entered the address data of all locations (see Definition of Locations). The system calculates the geographical data for

the location on the basis of the address data.

## Process

1. From the launchpad, you open the Transportation Network Cockpit app.

2. You select the transportation zone for which you want to calculate the coordinates and choose Calculate Coordinates.

  Note
The system does not consider locations for which you have set the Deletion Flag (see Deleting Locations) or locations

that have initial coordinates.

3. The system calculates the geographical data for the geographical center of the selected transportation zone and stores the

data in the background.

More Information

Transportation Lane

## Transportation Zone

Determination of Locations Within a Transportation Zone

## Use

You can use this report to determine all locations contained within a transportation zone.

## Prerequisites

Both locations (see Location) and transportation zones (see Transportation Zone) exist.

This is custom documentation. For more information, please visit SAP Help Portal.

47


1/14/26, 2:16 PM
## Features

The report offers the following options:

Determination of all locations that are directly contained in the transportation zone

In this case, the system determines all locations that are contained in this transportation zone.

Determination of all locations (that is, locations that are indirectly contained in the transportation zone)

In this case, the system determines all locations that are contained in both this transportation zone and in the

transportation zones of the corresponding transportation zone hierarchy.

The following applies when defining locations:

A location is directly contained within a transportation zone if one of the following criteria is met:

It is assigned directly to the transportation zone (zone type D or M).

It matches the transportation zone definition (zone type R or M) with regard to the region and country from the

location address.

It matches the transportation zone definition (zone type P or M) with regard to the postal code and country from the

location address.

A location is indirectly contained within a transportation zone if it is directly assigned to at least one transportation zone

that meets the following condition: It is a lower-level transportation zone within the transportation zone hierarchy of the

transportation zone that you entered in this report.

  Example

You have defined three transportation zones:

Transportation zone EU (Europe)

Transportation zone DE (Germany)

Transportation zone FR (France)

The transportation zones DE and FR are subordinate to the transportation zone EU.

If you run the report for transportation zone DE and specify that the system is to determine all locations that are directly

contained within this zone, the system displays all locations of transportation zone DE only. This result is irrespective of

whether you have manually assigned the locations to the transportation zone or whether the system has assigned them using

the address field.

If you specify that the system is to determine all locations, it displays the locations from the transportation zones EU and FR as

well.

## Activities

To execute the report, on the SAP Easy Access screen, choose  Transportation Management

 Master Data

 Transportation

## Network

 Determine Locations Within a Transportation Zone .

## Transportation Lane

This is custom documentation. For more information, please visit SAP Help Portal.

48


1/14/26, 2:16 PM
## Definition

A relationship between two locations, two transportation zones, or a combination of locations and zones that expresses the direct

reachability of the locations or of all locations within the zones for a specific means of transport.

## Use

You use this business object when planning distribution and procurement between different locations.

## Structure

A transportation lane is defined by a source location or zone, a destination location or zone, and a means of transport (MTr). You

have the option of assigning carriers to the transportation lane.

## Integration

This business object is used by several processes in Transportation Management (TM). For more information, see:

## Planning

Creation of Business Shares and Transportation Allocations

## Carrier Selection

Definition of Transportation Lanes

## Use

You use this process to define transportation lanes in Transportation Management (TM).

## Prerequisites

You have defined means of transport (MTr) in Customizing for Transportation Management under  Master Data

## Resources

 Define Means of Transport

.

You have defined at least two locations or transportation zones. For more information, see Definition of Locations or

Definition of Transportation Zones.

If you want to assign a carrier to a means of transport, you have assigned the business partner role Carrier to the business

partner that functions as the carrier. For more information, see Definition of Business Partners.

## Process

1. You define a transportation lane on the launchpad by opening the Define Transportation Lane app.

2. You create a transportation lane by entering information on either of the following tab page pages:

## Tr.Lane

You create the transportation lane by entering or choosing the source location or zone and the destination location

or zone.

## Intra-Zone Lane/Loc. Transp. Lane

This is custom documentation. For more information, please visit SAP Help Portal.

49


1/14/26, 2:16 PM

You use this tab page to define an intrazone lane or a location transportation lane.

You create an intrazone lane by entering or choosing a transportation zone.

You create a location transportation lane by entering or choosing a location.

  Note

Defining a location transportation lane has no impact on the reachability of locations. It can, however, be

useful in specific contexts such as the initialization of transportation allocations (see Transportation

Allocation).

For example, you might create a location transportation lane for a location A, define a planning period for

one or more means of transport, assign one or more carriers to the transportation lane, and define a

maximum freight order quantity for each carrier. This information can be evaluated during the creation of

transportation allocations, thereby limiting the number of transportation activities from or to location A

that are assigned to a specific carrier within the planning period.

Mass Maint. (Create)

You create multiple transportation lanes by copying an existing transportation lane.

  Note
On all tab pages, when you choose a transportation zone via the input help you can identify the transportation zones by

the location type 1005. This location type is used as a marker for transportation zones in the system. It cannot be used

to define transportation zones in the Define Location transaction (see Definition of Locations). To define transportation

zones, see Definition of Transportation Zones.

3. You assign a means of transport to the transportation lane.

Means of transport are used to move goods between the locations or zones of a transportation lane. You specify attributes

for the means of transport that apply to transportation activities between the source and destination of the goods to be

transported, such as the transportation duration, the transportation distance, and the transportation costs.

  Note

You can only create a transportation lane if you assign at least one means of transport to it.

4. You have the option of assigning carriers to the transportation lane.

A carrier offers services along a transportation lane for a specific means of transport. You, therefore, assign carriers to the

transportation lane by assigning them to the means of transport. Once you have assigned a carrier to the means of

transport, you can specify the attributes that are specific to this combination of carrier and MTr. For example, the

transportation costs, the priority, the share of business, or the capacity for the transportation allocation.

  Note

If you want to use automatic carrier selection, you have to assign carriers to means of transport.

## Result

You have created transportation lanes. You can change or display transportation lanes that you have defined on the launchpad by

opening the Define Transportation Lane app.

You can change or display multiple transportation lanes on the Mass Maint. (Display/Change) tab page.

You can use transportation lanes in transportation processes such as dispatching or subcontracting.

This is custom documentation. For more information, please visit SAP Help Portal.

50


1/14/26, 2:16 PM

Use of Change Documents for Transportation Lanes

## Use

You use this process to trace changes that are made to transportation lanes in Transportation Management.

The changes are logged in change documents, which allow you to find out at any time, what was changed, when the changes

occurred, and how the changes were made. Change documents facilitate the analysis of errors. To use change documents for

transportation lanes, you have to define the business object as a change object in the system.

## Process

1. You activate change documents in Customizing. For more information, see Customizing for Transportation Management

under  Master Data

 Transportation Network

 Transportation Lane

 Activate Change Documents .

2. You display the change documents for transportation lanes in the Display Change Documents app, which you open from

the launchpad.

Distance and Duration Determination (DDD)

## Use

You can use this function in Transportation Management (TM) to determine the distance of a transportation lane and the duration

it takes the means of transport to travel that distance. The system uses the distance and duration of the transportation lane in

planning processes. The VSR optimizer, for example, determines the most suitable means of transport for the transportation

processes on the basis of the distance and duration.

Further, you can use this function to determine the distance and duration between two locations in a business document of the

freight order management area and in planning. For more information, see Transportation Distance and Transportation Duration

and Determination of Transportation Distance and Transportation Duration.

Distance and duration determination is also used in the charge management area.

## Prerequisites

To ensure a more flexible approach to the determination of distances and durations, you can use the process controller as a

flexible framework to create different distance and duration determination strategies so you can connect to external geographical

information systems (GIS) that offer different calculations than the straight line distance and the calculation offered by the

standard geocoding program. You configure the process controller for the distance and duration determination in Customizing for

Transportation Management. For more information, see Customizing for Transportation Management under  Master Data

 Transportation Network

## Transportation Lane

 Distance and Duration DeterminationGeocoding

## Configure Process

Controller for Distance and Duration Determination .

For more information about further prerequisites, see .Settings for Distance and Duration Determination.

## Activities

In TM, you can implement a business add-in (BAdI) for distance and duration determination that can manipulate the calculated

values for the distance and duration. For more information, see Customizing for Transportation Management under  Business

Add-Ins (BAdIs) for Transportation Management

## Master Data

 Transportation Network

 Reuse Component

## Enhancement

of Basic Distance and Duration Determination

 BAdI: RC DDD - Basic Distance and Duration Determination .

This is custom documentation. For more information, please visit SAP Help Portal.

51


1/14/26, 2:16 PM
## More Information

Distance and Duration Determination.

Lane, Distance, and Duration Determination (LDDD)

## Use

The system uses this function to determine the most specific transportation lane for your transportation process. The lane,

distance, and duration determination (LDDD) considers the hierarchy of the means of transport and the hierarchy of the

transportation zone at the source and destination location. In addition to determining the transportation lane, the system

determines the distance of the lane and the duration it takes the means of transport to travel that distance.

LDDD is used in planning processes in Transportation Management (TM). The VSR optimizer, for example, determines the most

specific transportation lane for transportation processes on the basis of the lane, distance, and duration determination.

## Prerequisites

In Customizing, you have defined means of transport to which you have assigned superordinate means of transport. For

more information, see Customizing for Transportation Management under  Master Data

## Resources

 Define Means of

Transport

.

You have defined hierarchies for the source location or zone and the destination location or zone (see Defining a

Transportation Zone Hierarchy).

You have defined transportation lanes (see Definition of Transportation Lanes).

You have defined the hierarchy priorities for lane determination in Customizing. For more information, see Customizing for

Transportation Management under  Master Data

## Transportation Network

 General Settings for Transportation

Network Determination .

  Note

In the standard system, the hierarchy of the means of transport is considered first during determination.

## Activities

In TM, you can implement a business add-in (BAdI) for lane, distance, and duration determination that enables you to manipulate

the values for the distance and duration and the transportation lane calculated by the system. For more information, see

Customizing for Transportation Management under  Business Add-Ins (BAdIs) for Transportation Management

## Master Data

 Transportation Network

## Reuse Component

 Enhancement of Lane, Distance and Duration Determination

## BAdI: RC LDDD

- Lane, Distance and Duration Determination .

## More Information

Distance and Duration Determination

Distance and Duration Determination

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

52


1/14/26, 2:16 PM

You can use this function to determine the distance of a transportation lane and the duration it takes the means of transport to

travel that distance. The system determines the distance and duration in the following ways:

The system calculates the shortest distance (line of flight) between locations.

The system calculates the precise distance between locations based on the means of transport by using a third-party

geographic information system (GIS).

The distance and duration determination (DDD) uses geocoordinates that are stored in the system for each location. For a more

precise determination of distances and durations, you can use geocoding levels and DDD strategies to define on which level of

detail you want to determine the distance and duration. For example you can determine the distance and duration based on the

house number, the postal code or the region of the location's address. If the distance between a start and a destination location is

very large, you may not need to use the most detailed geocoordinates to determine the distances and durations as it does not

affect the business process significantly.

To use this function, you must have activated the business function Enhanced Services for Transportation Network

(SCM_SCMB_TR_NETWORK).

## Prerequisites

For information, see Settings for Distance and Duration Determination.

## Features

## Determining Distances and Durations for the DDD Buffer

The retrieval of data from a GIS can be time consuming and it can affect the performance of the system. For this reason, you can

store retrieved data in the DDD buffering table. You can use the Determine Distances and Durations for DDD Buffer (Selected

Geography) report to precalculate the distance and duration for a set of start and destination locations and save the result in the

distance and duration determination (DDD) buffer. For large volumes of data you can also run background jobs for this function.

For more information, see Determination of Distances and Durations Based on Selected Geography.

Whereas determination with this report is based on the selected geography, the Determine Distances and Durations for DDD

Buffer (Selected Documents) report determines distances and durations based on selected business documents. For more

information, see Determination of Distances and Durations Based on Selected Documents.

## Adjusting Distances and Durations for the DDD Buffer

You can use the Adjust Distances and Durations for the DDD Buffer report to manually adjust distances and durations for the

distance and duration determination (DDD) buffer. For more information, see Adjustment of Distances and Durations for the DDD

Buffer.

## Deleting Buffered Distances and Durations

You can use the Deletion of Buffered Distances and Durations report to delete obsolete entries from the distance and duration

determination (DDD) buffer. For more information, see Deletion of Buffered Distances and Durations.

## Determining the Distance and Duration for a Single Transportation Lane

You can determine distances and durations for a single transportation lane. For more information, see Determining the Distance

and Duration for a Single Transportation Lane.

Determining the Distance and Duration for Multiple Transportation Lanes

This is custom documentation. For more information, please visit SAP Help Portal.

53


1/14/26, 2:16 PM

You can determine distances and durations for multiple transportation lanes. For more information, see Determining the Distance

and Duration for Multiple Transportation Lanes.

Settings for Distance and Duration Determination

## Use

## Determining Distance and Duration Based on the Shortest Distance

If you want the system to determine the distance and duration for the shortest distance (line of flight) between two locations, you

have done the following:

In the Customizing activity Define Means of Transport, you have made the following settings:

You have defined means of transport and specified the average speed and the distance factor for them.

You have deactivated the GIS Qlty (GIS Quality) checkbox.

You have defined locations in the location master. If you have entered address data for the location, the system calculates

the geographical data for the location as well as any additional geocoordinates based on geocoordinate determination

strategies you have maintained. The system uses the geographical data of a location as a basis for the DDD.

## Determining Distance and Duration as well as Routes by Means of a GIS

If you want the system to determine the distance and the duration as well as routes by means of a geographic information system

(GIS), you have done the following:

You have set up the standard integration with SAP HANA spatial services (see Standard Integration with SAP HANA spatial

services) or you have used the process controller to create your own DDD or georouting strategy and method.

In the Customizing activity Set Usage of GIS Tool, you have set the usage of the GIS tool.

You have maintained means of transport for which you have specified the low, medium, and high speeds, and you have

activated the GIS Qlty (GIS Quality) checkbox in the Customizing activity Define Means of Transport.

  Note

If you do not make any entries for the speeds, the system can determine the distance but not the duration. In this case,

the system uses a standard value for the duration.

If you want to determine distances and durations on the basis of specified geocoordinates, you have done the following in

Customizing:

You have defined geocoding levels in the Customizing activity Define Geocoding Levels.

You have defined GIS zones for use in the DDD or georouting strategies in the Customizing activity Define GIS Zone.

You have assigned countries or regions to the GIS zones for use in the DDD or georouting strategies in the

Customizing activity Assign Country/Region to GIS Zone.

You have defined DDD or georouting strategies in the Customizing activity Define Strategy for Distance and

Duration Determination and Georouting.

You have defined global settings for the distance and duration determination in the Customizing activity Define

Global Settings for Distance and Duration Determination.

This is custom documentation. For more information, please visit SAP Help Portal.

54


1/14/26, 2:16 PM

You have defined number range intervals for speed profiles in the Customizing activity Define Number Range

Intervals for Speed Profiles.

Optionally, you have defined GIS providers in the Customizing activity Define GIS Providers and indicated the

validity of geographical data based on the GIS strategies for a given GIS provider. The validity specifies the number

of days or hours that geographical data from a GIS provider is stored in the system before it is automatically deleted

and redetermined. You can also indicate whether and how GIS data is to be stored. It can be stored based on the

validity of the GIS provider (in days) or the validity of the GIS strategy (in hours).

Determining the Distance and Duration for a Single
Transportation Lane

## Procedure

1. Define a transportation lane.

2. Display the detail screen for the means of transport and switch to change mode.

3. On the detail screen, in the Parameters frame, choose Generate Proposal.

## Results

The system determines the distance and duration on the basis of either a geographic information system or the shortest distance

(depending on the assigned means of transport) and enters values in the Transptn Distance (Transportation Distance) and Trsp.

Duration (Transportation Duration) input fields.

  Note
You can enter values for the distance and duration manually when defining a transportation lane.

## Next Steps

For more information about distance and duration determination, see Distance and Duration Determination.

For more information about creating transportation lanes, see Create Transportation Lanes.

Determining the Distance and Duration for Multiple
Transportation Lanes

## Procedure

1. Define multiple transportation lanes in the Mass Creation of Transportation Lanes report.

2. In the Transport Duration and Distances frame, choose either of the following:

## Calculate transport durations and distances

The system redetermines the distances and duration for the transportation lanes created. It determines the values

on the basis of either a GIS or the shortest distance and enters values in the Transptn Distance and Trsp. Duration

input fields of the means of transport.

## Adopt Transport. Duration and Distances from Template

This is custom documentation. For more information, please visit SAP Help Portal.

55


1/14/26, 2:16 PM

The system reuses the distances and duration of the transportation lane that is used as a template and enters

values in the Transptn Distance and Trsp. Duration input fields of the means of transport.

When you run mass maintenance, you need to run the Determine Distances and Durations for DDD Buffer (Selected Geography)

report. The system determines the distances and durations for all the transportation lanes created.

To run the report, on the Easy Access screen, search for Determine Distances and Durations for DDD Buffer (Selected

Geography) (/SCMB/DDD_PRECALC).

## More Information

For more information about distance and duration determination, see Distance and Duration Determination.

For more information about creating transportation lanes, see Create Transportation Lanes.

For more information about the precalculation of distances and durations, see Determination of Distances and Durations Based on

Selected Geography.

Determination of Distances and Durations Based on Selected
Geography

## Use

You can use this function to precalculate the distance and duration for a set of start and destination locations and save the result

in the distance and duration determination (DDD) buffer. For large volumes of data you can also run background jobs for this

function.

The precalculation of distances and durations speeds up the distance and duration determination by storing already calculated

results for later reuse. You can either add new entries only to the buffer or you can overwrite already existing buffer entries. You can

also simulate the selection. By simulating, the report displays the selected entries that the system potentially adds to the buffer.

The system does not make any changes to the buffer. You set up your selection based on the following data:

## DDD strategy

You select a DDD strategy and a geocoding level that you want to use for the distance and duration determination. If you

enter a DDD strategy and leave the Geocoding Level field empty, the system precalculates the distance and duration for all

geocoding levels of the locations. If you want the system to set the DDD strategy and the geocoding level dependent on the

settings in the DDD strategy Customizing, you can also select the Strategy Determination checkbox.

## Means of transport

You can select one or several means of transport. The system uses the means of transport for the distance and duration

calculation. If you leave the Means of Transport field empty, the system uses all means of transports maintained in the

system. The system calculates the distance and duration for all selected start and destination location pairs in combination

with all selected means of transport.

## Precision of DDD

You can select the precision of the determined durations and distances. By selecting Undefined, for example, you can

select all distances and durations that could not be determined.

## Validity end of buffer entry

This is custom documentation. For more information, please visit SAP Help Portal.

56


1/14/26, 2:16 PM

You can select a range of validity end dates. You can indicate the validity of distances and durations in the Customizing

activity Define GIS Providers. For more information, see Settings for Distance and Duration Determination.

## Start and destination location

You can select a set of start and destination locations for the distance and duration calculation.

By selecting the Use Only Existing Transportation Lanes checkbox, the system only selects combinations that have start and

destination locations with a corresponding transportation lane maintained. If you do not select the Use Only Existing

Transportation Lanes checkbox, the system considers all combinations between the start and destination locations.

Combinations with identical start and destination are ignored.

To use this report, you must have activated the business function Enhanced Services for Transportation Network

(SCM_SCMB_TR_NETWORK).

## Prerequisites

You have defined strategies for distance and duration determination in the process controller. The strategies provide the

connection to your GIS provider. You can define your own strategy or use the standard strategy DDD_STD.

You define strategies in the Customizing Define Strategy. For more information, see Process Controller.

  Note

The system updates the DDD buffer by means of the DDD strategies, so the strategies you use must contain the

standard method for the update of the buffer.

You have determined geocoordinates for all start and destination locations. You maintain geocoordinates with the Mass

Geocoding report. To run the Mass Geocoding report, on the SAP Easy Access screen search for Mass Geocoding

(/SAPAPO/MASSGEOCODE).

You have indicated in the Customizing activity Define Global Settings for Distance and Duration Determination whether a

failed distance and duration determination is to be buffered with a precision value of Undefined.

## Activities

To precalculate the distances and durations, on the SAP Easy Access screen search for Precalculate Distances and Durations for

the DDD Buffer (/SCMB/DDD_PRECALC).

To precalculate the distances and durations as a background job, on the SAP Easy Access screen search for Precalculate

Distances and Durations for the DDD Buffer in Batch ( /SCMB/DDD_B_PRECALC).

Determination of Distances and Durations Based on Selected
## Documents

You can use this function to determine distances and durations for start and destination locations based on selected business

documents.

## Use

This function determines distances and durations for a set of start and destination locations based on a number of selected

business documents and saves the result in the distance and duration determination (DDD) buffer.

This is custom documentation. For more information, please visit SAP Help Portal.

57


1/14/26, 2:16 PM

You can start this function in simultaneous parallel sessions only if you have indicated a parallel processing profile in your planning

profile. We recommend that you use background processing if you want to process business documents simultaneously.

## Integration

For more information about the integration of this function into overall background processing, see Background Processing.

## Prerequisites

You have created selection profiles and a planning profile. For more information, see Selection Profile and Planning Profile.

You have set up distance and duration determination with the DDD buffer. For more information, see Settings for Distance

and Duration Determination.

## Features

This function determines distances and durations for all pairs of locations that are relevant for a given combination of selection

profiles and planning profiles.

You can run this report as a preparation task so that distances and durations are already available when you start vehicle and

scheduling (VSR) routing. This will reduce runtime in the VSR optimizer preprocessing.

## Activities

To use this function, you must run program /SCMTMS/PLN_DDD. You must specify the following settings:

Selection profiles

## Planning profile

## Capacity selection settings

Checkbox to indicate whether all messages are to be displayed

Checkbox to indicate whether messages should be logged in the application log

As a result, the DDD buffer is filled.

The system logs all messages that it issues when executing the function in the application log under object /SCMTMS/TMS. If you

run the function in the background, the system uses the subobject BP for logging. If you run the function manually, the system logs

the messages under subobjects according to the business object that created the message.

Related Information

## Planning Run

## Adjustment of Distances and Durations for the DDD Buffer

You can use this report to manually adjust distances and durations for the distance and duration determination (DDD) buffer.

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

58


1/14/26, 2:16 PM

If distances and durations could not be determined for some locations, for example, you can use this report to filter for these

distances and durations using the Precision of DDD field and then enter distances and durations manually.

You set up your selection based on the following data:

## Strategy selection

You can set up the strategy selection as follows:

If you want to delete buffer entries with a specific strategy and a specific geocoding level only, you select a DDD

strategy and a geocoding level.

If you want to delete all entries with a certain strategy regardless of the geocoding level, you select a DDD strategy

and leave the Geocoding Level field empty.

To delete all entries with a specific geocoding level, regardless of the strategy, you can leave the Strategy field

empty and select a specific geocoding level.

If you leave both fields empty, the system deletes all combinations of strategy and geocoding level in the selection.

## Means of transport

You can select one or several means of transport if you want to delete buffer entries with specific means of transport only. If

you leave the Means of Transport field empty, the report uses all means of transports maintained in the system.

## Precision of DDD

You can select the precision of the determined durations and distances. If you select Undefined, for example, the system

displays all distances and durations that could not be determined. You can then enter distances and durations manually.

## Validity end of buffer entry

You can select a range of validity end dates. You can indicate the validity of distances and durations in the Customizing

activity Define GIS Providers. For more information, see Settings for Distance and Duration Determination.

## Time-dependent selection

You can select buffer entries for the deletion dependent on the date they were last changed or accessed.

## Start and destination location selection

You can select a set of start and destination locations to delete only buffer entries with selected locations.

## Prerequisites

You specify the interval in which the system updates the last access date for the time-dependent selection in the

Customizing activity Define Global Settings for Distance and Duration Determination. In this Customizing activity, you

also indicate whether a failed distance and duration determination is to be buffered with a precision value of Undefined.

## Activities

To adjust distances and durations, on the SAP Easy Access screen search for Adjust Distances and Durations for the DDD Buffer

(/SCMB/DDD_MAINTAIN).

Deletion of Buffered Distances and Durations

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

59


1/14/26, 2:16 PM

You can use this function to delete obsolete entries from the distance and duration determination (DDD) buffer. For large volumes

of data you can also run background jobs for this function.

You delete entries that are no longer needed or entries that are invalid because of a change in the system setup, for example a new

GIS Provider has been defined with a new strategy or a geocoding level has been removed. It is also possible to delete old entries

dependent on their last change or access date.

You set up your selection based on the following data:

## Strategy selection

You can set up the strategy selection as follows:

If you want to delete buffer entries with a specific strategy and a specific geocoding level only, you select a DDD

strategy and a geocoding level.

If you want to delete all entries with a certain strategy regardless of the geocoding level, you select a DDD strategy

and leave the Geocoding Level field empty.

To delete all entries with a specific geocoding level, regardless of the strategy, you can leave the Strategy field

empty and select a specific geocoding level.

If you leave both fields empty, the system deletes all combinations of strategy and geocoding level in the selection.

## Means of transport

You can select one or several means of transport if you want to delete buffer entries with specific means of transport only. If

you leave the Means of Transport field empty, the report uses all means of transports maintained in the system.

## Precision of DDD

You can select the precision of the determined durations and distances. By selecting Undefined, for example, you can

select all distances and durations that could not be determined and then delete them.

## Validity period selection

You can specify that only invalid entries are to be considered. Further, you can select a range of validity end dates for your

buffer entries. You can indicate the validity of distances and durations in the Customizing activity Define GIS Providers. For

more information, see Settings for Distance and Duration Determination.

## Time-dependent selection

You can select buffer entries for the deletion dependent on the date they were last changed or accessed.

## Start and destination location selection

You can select a set of start and destination locations to delete only buffer entries with selected locations.

To use this report, you must have activated the business function Enhanced Services for Transportation Network

(SCM_SCMB_TR_NETWORK).

## Prerequisites

You specify the interval in which the system updates the last access date for the time-dependent selection in the

Customizing activity Define Global Settings for Distance and Duration Determination. In this Customizing activity, you

also indicate whether a failed distance and duration determination is to be buffered with a precision value of Undefined.

## Activities

This is custom documentation. For more information, please visit SAP Help Portal.

60


1/14/26, 2:16 PM

To delete distances and durations, on the SAP Easy Access screen search for Delete Buffered Distances and Durations

(/SCMB/DDD_DELETION).

To delete distances and durations as a background job, on the SAP Easy Access screen search for Delete Buffered Distances and

Durations in Batch (/SCMB/DDD_B_DELETION).

Checking and Repairing the DDD Buffer Table

## Use

You use the Check and Repair Buffering Table report to check and repair any inconsistencies that might occur in the distance and

duration determination (DDD) buffering table. You can do the following with the report:

Delete all entries in the buffering table

Check the following for consistency:

Means of transport

DDD strategies

## Locations

To use this report, you must have activated the business function Enhanced Services for Transportation Network

(SCM_SCMB_TR_NETWORK).

## Activities

To access this report, on the SAP Easy Access screen, search for Check and Repair Buffering Table (/SCMB/DDD_CLEANUP).

## More Information

For more information about DDD, see Distance and Duration Determination.

Checking Buffered Distances and Durations for Inconsistencies

## Use

You use the Check Buffered Distances and Durations for Inconsistencies report to check the distance and duration

determination (DDD) buffer for inconsistencies which may arise from a triangle inequality. This check considers entries to be

inconsistent if the direct connection between two geocoordinates is longer or slower than the connection via intermediate

geocoordinates. The check returns information on the type of inconsistency, the involved locations for the geocoordinates and the

alternative paths that are shorter or faster to connect the geocoordinates from a DDD entry.

You can filter the displayed entries using the selection fields. Further, you can specify that the system is to skip consistent entries.

For more information, see the system documentation.

  Note

Currently, the report can handle up to 16 million DDD buffer entries.

This is custom documentation. For more information, please visit SAP Help Portal.

61


1/14/26, 2:16 PM
## Activities

To access this report, on the SAP Easy Access screen, search for Check Buffered Distances and Durations for Inconsistencies

(/SCMB/DDD_CHECK_TRIA).

## More Information

For more information about DDD, see Distance and Duration Determination.

Schedule

## Use

You use this function to define a sequence of stops such as ports, airports, or gateways that is valid for a specific period of time.

Ships, trucks, or airplanes can move goods at recurring times along the whole sequence or any part of it. The movement of goods

depends on the transit duration between each of the stops as well as the cut-off times and the length of stay at each stop.

As part of the new schedule concept, you can use different carrier schedules and gateway schedules to define information about

your stop sequence and departure rules. For more information about departure rules, see Use of Departure Rules.

## Features

There are up to three categories of schedules for each mode of transport available to you in Transportation Management (TM).

Direct and indirect gateway schedules

Gateway schedules with reference

Carrier schedules

## Gateway Schedules

Gateway schedules are schedules whose start stops and destination stops are transportation hubs (gateways) such as container

freight stations (CFS) where freight is consolidated and deconsolidated. When you create a gateway schedule, you can enter a

reference to a carrier schedule for each transportation stage and so transfer departure rules and voyages from the carrier

schedule to the gateway schedule. This function is based on the transportation mode and is available for the sea and air modes

only.

For more information, see Direct Creation of Freight Documents and Selection of Schedules.

  Note

You can enter only one source gateway and one target gateway for each gateway schedule.

The following gateway schedules are supplied in the standard SAP delivery:

## Road Gateway Schedule

As a logistics service provider, you use a road gateway schedule to define a direct connection between two gateways.

Consequently this involves a direct gateway schedule. Freight is transported between the two gateways in the road gateway

schedule by road.

## Sailing Schedule

This is custom documentation. For more information, please visit SAP Help Portal.

62


1/14/26, 2:16 PM

You use sailing schedules to define a schedule for the customer in an ocean freight scenario. Sailing schedules denote a

connection between two gateways that are designated as container freight stations in the sea transportation mode, and

include information about the port of loading and port of discharge. Unlike the road gateway schedule, this involves an

indirect gateway schedule for the sailing schedule. However, they do not include information about any of the other stops in

the sequence.

## Master Flight Schedule

As a logistics service provider, you use the master flight schedule to define a connection between the gateways at two

airports. As the master flight schedule contains further information about the airport of departure and the airport of

destination, this involves an indirect gateway schedule, similar to the sailing schedule.

You can reference from one master flight schedule to several carrier flight schedules, and therefore map connecting flights

in your schedule. You can define the individual references for each transportation stage of the main carriage.

If you define a restriction to certain organizational units for a master flight schedule, this restriction also applies to any air

freight bookings that you generate from this master flight schedule. This means that only transportation planners from the

specified organizational unit can plan the air freight bookings in question. For more information, see Publication and

Locking of Air Freight Bookings.

## Gateway Schedules with Reference

In the sea and air transportation modes, you can also reference one or more carrier schedules from a gateway schedule and as a

result map for instance connecting flights in your schedule in air transportation mode. You can define the individual references for

each transportation stage of the main carriage.

  Note

If there are changes in one of the referenced carrier schedules, and you have already entered these in the carrier schedule

yourself, then the status of referenced data in your gateway schedule is changed from Data Is Up-to-date to Data Is Not Up-to-

date . For each transportation stage, the system shows you whether the data in the relevant referenced carrier schedule has

changed.

  Example
You open your master flight schedule from Frankfurt to Los Angeles via New York. You note that the status of the referenced

data is Data Is Not Up-to-date. You now check in the departure rules of your schedule which transportation stage is affected by

this change. The status of the referenced data for the transportation stage from Frankfurt to New York is still Data Is Up-to-

date. However, the status of the referenced data for the transportation stage from New York to Los Angeles is Data Is Not Up-

to-date.

You assign the updated carrier flight schedule to the no longer up-to-date transportation stage of the master flight schedule

again. The system then changes the status of the referenced data for both the transportation stage from New York to Los

Angeles and for the entire master flight schedule to Data Is Up-to-date.

If these changes involve a postponement of the departure dates and one of the two flight schedules is assigned to an air freight

booking, the system changes the status of the referenced data in the air freight booking to Data Is Not Up-to-date. For

additional information about using schedules in freight documents, see Use of Schedules.

  Caution
Once you have assigned a new or updated carrier schedule to the gateway schedule, you have to regenerate the departures in

the gateway schedule.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

63


1/14/26, 2:16 PM

You can change the transit duration of a gateway schedule even after departure rules and voyages have been created.

Example: For a sailing schedule with a source container freight station (CFS) and a destination CFS, you can change the

pick-up transit duration (that is, the duration from the source CFS to the first port of loading) and the delivery transit

duration (that is, the duration from the last port of discharge to the destination CFS). The system considers these

transit durations for new departure rules or voyages in the corresponding schedule. Changing the transit durations does

not have an impact on existing departure rules and voyages.

Further, you can change the transit duration from the last port of discharge to the destination gateway after you have

created a voyage. The arrival time is derived from the transit duration. If you then copy time changes from the

underlying carrier schedule's voyage into the gateway schedule voyage, the system keeps the manually changed transit

duration and uses it to recalculate the arrival time.

## Gateway Schedules Without Consolidation

As in the freight booking, you can also specify whether a consolidation takes place for a gateway schedule. For example, you can

define a gateway schedule with a source gateway but not a destination gateway if you want a consolidation to take place only at

the source gateway. You define this in Customizing in the schedule type.

## Carrier Schedules

Carrier schedules define a sequence of stops for which the start stop and target stop are not gateways. By specifying departure

rules, you can generate departures automatically. The system calculates the arrival and departure dates and times at each stop in

the sequence, taking into account the transit duration, cut-off times, and availability of the goods for each stop. You can then

modify each voyage individually.

In the sea and air transportation modes, you can also reference carrier schedules from a gateway schedule. For more information,

see Direct Creation of Freight Documents and Selection of Schedules.

The following carrier schedules are supplied in the standard SAP delivery:

## Ocean Carrier Schedule

You use the ocean carrier schedule to define a standard sequence of stops that are served by a ship. By specifying

departure rules, you can generate voyages automatically.

## Carrier Flight Schedule

You use the carrier flight schedule to define a standard sequence of stops that are typically served by one plane.

Alternatively, you can also define carrier flight schedules for connection flights with multiple transportation stages, for

which various carriers with different aircraft types and flight numbers execute each of the transportation stages. If loading

and unloading activities do not take place at one of these stops but other activities such as refueling do take place, you can

classify this as a service stop.

Finally, by specifying departure rules, you can generate flights automatically.

Moreover, you can specify that the carrier entered in the carrier flight schedule is the operating (executing) carrier of the

schedule. Consequently, you can map codeshare flights in your schedule.

  Example

Airline XX offers a flight under their own flight number XX123. A different airline, ZZ, by arrangement with airline XX sells

the flight under flight number ZZ456, even though the other airline does not operate the flight itself. Airline XX is

therefore the operating carrier, and airline ZZ is the marketing carrier.

## Road Schedule

This is custom documentation. For more information, please visit SAP Help Portal.

64


1/14/26, 2:16 PM

You use the road schedule to define a standard sequence of stops that are served by a truck.

## Additional Functions

You can also create schedule-based freight documents by executing the report /SCMTMS/MP_SCHED_CREATE_TOR. For more

information, see the system documentation.

You can also use transaction WUF to display the documents that refer to a specific schedule. This function is available for the

following document types:

## Schedules

Freight bookings

## Freight orders

Schedule-based allocations

More Information

Creating Schedules

Use of Schedules

Creating Schedules

## Use

You can create various carrier schedules and gateway schedules that you want to use as part of your transportation planning

activities. You can create individual schedules manually or upload one or more schedules from an external data source to

Transportation Management (TM). For more information, see Manual Creation of Schedules and Uploading of Schedules.

## Creation of schedules in TM

This is custom documentation. For more information, please visit SAP Help Portal.

65


1/14/26, 2:16 PM
## Prerequisites

You have defined locations (see Location).

You have defined business partners and assigned them to the business partner role Carrier. For more information, see

Definition of Business Partners.

You have defined the modes of transportation in Customizing for Transportation Management under  Transportation

Management

## Master Data

 Transportation Network

 Transportation Lane

 Define Transportation Mode .

You have defined number range intervals for schedules and departures in Customizing for Transportation Management

under  Transportation Management

## Master Data

 Transportation Network

 Schedule .

You have defined a schedule type in Customizing for Transportation Management under  Transportation Management

## Master Data

 Transportation Network

## Schedule

 Define Schedule Types .

## More Information

Interaction Between Organizational Units

## Schedule

## Default Route

Manual Creation of Schedules

## Use

You use this process to create various carrier schedules and gateway schedules that you want to use as part of your transportation

planning activities. To create schedules, open the Create Schedule app on the launchpad.

## Process

1. Entering the Schedule Type

To specify the type of schedule you want to create, you enter the schedule type that you defined before in Customizing. TM

provides the following standard schedule types:

Ocean carrier schedule: 1000

Carrier flight schedule: 1100

Road schedule: 1200

Sailing schedule: 2000

Sailing schedule with reference to ocean carrier schedules: 2100

Road gateway schedule: 2200

Master flight schedule: 2500

Master flight schedule with reference to carrier flight schedules: 2600

Depending on the schedule type you entered, the system dynamically generates a user interface for creating schedules.

2. Entering the General Schedule Data

This is custom documentation. For more information, please visit SAP Help Portal.

66


1/14/26, 2:16 PM

First you enter the general data, such as the carrier, transportation mode, and the transportation group for your schedule.

You can also specify a shipping type. If you specify a shipping type, the system only takes the schedule into account for

forwarding orders with the same shipping type during automatic planning. For more information, see Customizing for

Transportation Management under  Basic Functions

 Type Codes and Role Codes

 General Type Codes and Role

## Codes

 Define Shipping Type .

If you create a sailing schedule with reference, you can reference to existing ocean carrier schedules. If you create a master

flight schedule with reference, you can reference to carrier flight schedules.

If you create a master flight schedule, you can define an air cargo security status for this schedule. For more information,

see Air Cargo Security in Business Document Processing and Air Freight-Specific Consolidation Processes.

3. Entering Location Data

You enter the standard sequence of stops along with the transit duration, the cutoff times, the length of stay, and so on. You

can also enter a start location and end location.

4. Creating Departure Rules

You enter departure rules to specify the frequency of voyages, departures, or flights from a stop. You also define a time

period during which the departure rule is valid. For example, you can specify that a ship sails from the port of Newark every

Thursday at 3:00 pm between January 1 and June 30. For more information about creating departure rules, see Example of

the Use of Departure Rules.

If you are working with a gateway schedule with reference and have referenced carrier schedules, you can copy the

departure rules from the relevant carrier schedules at transportation stage level.

5. Creating Voyages, Departures, and Flights

After you have created your departure rules, generate voyages, departures, or flights to calculate the actual departure

dates/times automatically. The system displays the actual departure dates/times on the appropriate tab.

6. Changing Departure Dates/Times

You select a departure date/time that the system created automatically, and adjust the relevant data as needed. You can

also add a departure date/time that is not based on a departure rule.

  Example

You created an ocean carrier schedule, in which your ship sails from port A via port B to port C and puts to sea every

Thursday at 3:00 pm. You receive a notification that port B will be closed next Thursday; therefore, for the trip next

week, you enter that your ship should sail directly from port A to port C.

If you have referenced one or more carrier schedules from a gateway schedule, you cannot change the data copied from the

carrier schedules. If you want to change this data, you have to change it directly in the relevant carrier schedule. As an

alternative, you can assign a different carrier schedule to the gateway schedule, and create new departures.

7. Deleting Schedules

You can delete entire schedules or departures, if they lie in the past, using report /SCMTMS/SCH_DELETION. For more

information, see the system documentation.

Uploading of Schedules

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

67


1/14/26, 2:16 PM

You can upload schedules from an external data source to Transportation Management (TM) by calling function module

/SCMTMS/BAPI_SCHEDULE_SAVEMULT. This function is available for the sea, air, and road transportation modes. For more

information, see the system documentation.

Alternatively, you can upload schedules in a format used by a spreadsheet program or in CSV format to TM by executing report

/SCMTMS/SCH_UPLOAD. This function is available for the sea and air transportation modes. For more information, see the system

documentation.

  Note

You can delete schedules created manually and uploaded by calling function module /SCMTMS/BAPI_SCHEDULE_DELMULTI

or by executing report /SCMTMS/SCH_DELETION.

Uploading of Schedules

More Information

SAP Note 1743069

 for uploading schedules for the air transportation mode

SAP Note 2136548

 for uploading schedules for the sea transportation mode

Transportation Costs

## Use

You can define transportation costs in your schedules based on the quantity of goods that are to be transported. These costs are

then used by the optimizer to calculate the most cost-effective route; they do not represent actual costs.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

68


1/14/26, 2:16 PM

You can also define transportation costs based on other criteria such as distance or duration in the planning profile. For more

information, see Constraints and Costs Settings.

## Prerequisites

In Customizing for Transportation Management, you have completed the activities under  Master Data

 Transportation

## Network

 Schedules .

## Features

You can calculate transportation costs in gateway schedules and carrier schedules based on the costs per quantity.

## Gateway Schedules

When you enter quantity costs in a gateway schedule such as a sailing schedule or an LCL overland schedule, the optimizer

calculates the transportation costs by multiplying the costs per quantity by the actual quantity to be transported. The system only

considers the stage between the port of loading and the port of discharge.

  Example

If you enter a quantity cost of 200 per ton and want to calculate the cost of transporting 1.5 tons, the system multiplies 200 x

1.5 and returns a transportation cost of 300.

## Carrier Schedules

When you enter quantity costs in a carrier schedule such as an ocean carrier schedule, the optimizer calculates the transportation

costs based on the number of stages. It therefore multiplies the costs per quantity by the actual quantity to be transported, and

then multiplies the result by the number of stages over which goods are transported.

  Example

If you enter a quantity cost of 200 per ton and want to calculate the cost of transporting 1.5 tons over 5 stages, the system

multiplies 200 x 1.5 x 5 and returns a transportation cost of 1500.

## Activities

To define quantity costs in schedules, open the Create Schedule app from the launchpad.

Example: Schedules for Sea Traffic

## Use

As a logistics service provider (LSP), you receive an order to transport freight from your container freight station (CFS) in

Nuremberg, Germany (CFS_NUR) to a CFS in Chicago, United States (CFS_CHI). You want to specify that all freight transported

between Nuremberg and Chicago is to be routed by default via the ports in Hamburg (PORT_HAM) and New York (PORT_NYK) and

their respective CFSs (CFS_HAM and CFS_NYK).

## Process

This is custom documentation. For more information, please visit SAP Help Portal.

69


1/14/26, 2:16 PM

1. You create a sailing schedule from the CFS in Hamburg (CFS_HAM) to the CFS in New York (CFS_NYK), and specify the

corresponding ports as Hamburg (PORT_HAM) and New York (PORT_NYK).

You specify LCL (less than container load) as the shipping type.

2. You create a road gateway schedule with which goods are transported from the CFS in Nuremberg (CFS_NUR) to the CFS in

Hamburg (CFS_HAM), and a second road gateway schedule with which goods are transported from the CFS in New York

(CFS_NYK) to the CFS in Chicago (CFS_CHI).

3. You create a default route with the following sequence of locations:

a. CFS in Nuremberg (CFS_NUR)

b. CFS in Hamburg (CFS_HAM)

c. CFS in New York (CFS_NYK)

d. CFS in Chicago (CFS_CHI)

4. On the Stages tab page of the forwarding order user interface under Actual Route, you select the stage from Nuremberg to

Chicago and choose  Schedule

 Select

.

The system lists a number of proposals.

  Note

Note that the system only takes into account schedules with shipping type LCL or schedules that do not have a defined

shipping type.

5. You select the transportation proposal that you require and choose Done.

The system automatically adds the pre-carriage and on-carriage stages along with additional data such as the port of

loading and port of discharge, voyage number, and the name of the vessel.

This process is shown in the following graphic:

This is custom documentation. For more information, please visit SAP Help Portal.

70


1/14/26, 2:16 PM

Example: Using sailing schedules, road gateway schedules, and default routes

## Result

When you select the appropriate sailing schedule from the forwarding order, the system automatically enhances the data on the

Stages tab page by adding the ports of loading and discharge, as well as the pre-carriage and on-carriage stages.

Use of Departure Rules

## Use

By specifying departure rules, you can generate departures automatically. The system calculates the arrival and departure dates

and times at each stop in a stop sequence, taking into account the following durations and times for each stop:

Transit duration

Length of stay

Cargo cut-off time

## Availability time

You can generate concrete departures from your departure rules and adjust them individually for each departure if required.

You can define departure rules at schedule or transportation stage level for carrier schedules and gateway schedules.

This is custom documentation. For more information, please visit SAP Help Portal.

71


1/14/26, 2:16 PM

You can also apply departure rules from a referenced carrier schedule to a gateway schedule.

## Prerequisites

You have created the required locations in the master data (see Location).

## Features

## Creation of Departure Rules at Schedule Level

If your standard stop sequence has just one source location and one destination location, your departure rule encompasses just

one transportation stage. The departure rule that you define therefore applies at schedule level.

## Creation of Departure Rules at Transportation Stage Level

To be able to define departure rules at transportation stage level, your standard stop sequence must contain more than two

locations.

When you create departure rules at transportation stage level, you can define multiple departure rules with diverging departure

times and arrival times for the various days of the week for which your schedule applies. This allows you to define different transit

durations, lengths of stay, cargo cut-off times, and availability times for each day of the week.

## Referencing Schedules with Departure Rules

In the gateway schedule with reference, you can reference a departure rule for a transportation stage from a carrier schedule for

each transportation stage of the main carriage. The referenced departure rules can come from different carrier schedules.

Alternatively, you can copy the departures for the entire main-carriage stage directly from a referenced carrier schedule.

If times are changed in the referenced carrier schedule, the system changes the status of the referenced data in the referencing

gateway schedule from Data Is Up-to-date to Data Is Not Up-to-date. In the departure rule of the gateway schedule with

reference, the system enters the status of the referenced data at transportation stage level. From here you can navigate via a link

to the relevant referenced carrier schedule, and there check exactly which times have changed. If you transfer these changes to

your gateway schedule with reference either by assigning the same carrier schedule with the up-to-date data for the

transportation stage concerned again, or by assigning a different carrier schedule for the first time, the system changes the status

of the referenced data from Data Is Not Up-to-date back to Data Is Up-to-date.

## Automatic Calculation of Times

If, in the Departure Rules screen area of your schedule, you select the Auto Fill Times checkbox and specify particular times for

various transportation stages, the system calculates the missing times for the various transportation stages of the departure rule

automatically, taking the different times zones of each of the locations into account. You can choose between the following modes

for the automatic calculation of times:

## Duration-based mode

You use the duration-based mode to calculate the arrival time of a transportation stage and the departure times and arrival

times of later transportation stages based on the transit duration and the length of stay of a transportation stage.

## Time-based mode

You use the time-based mode to calculate the transit duration and the length of stay of transportation stages based on the

departure times and arrival times of these transportation stages.

In carrier schedules, for example, in time-based mode the system uses the arrival time at the destination location of the first

transportation stage and the length of stay at the destination location of the first destination stage to calculate the departure time

This is custom documentation. For more information, please visit SAP Help Portal.

72


1/14/26, 2:16 PM

at the source location of the second transportation stage.

In the gateway schedule, you can also define the following durations and times for the pre-carriage and on-carriage as separate

transportation stages in the departure rule:

Transit duration

Length of stay

Cargo cut-off time

## Availability time

You can change the cargo cut-off times in the transportation stage for the pre-carriage only and the availability time in the

transportation stage for the on-carriage.

If you create a gateway schedule with reference in the transportation modes sea and air, you can change the departure time from

the source location of the first transportation stage and the arrival time at the destination location of the last transportation stage

in the gateway schedule. If you want to change any other times in the departure rule from the carrier schedule, you can only do so

in the actual carrier schedule.

## Activities

You first define in your schedule the locations of the standard stops for your schedule in the Standard Stop Sequence screen area

and specify the cut-off time and length of stay for each location. Based on this standard stop sequence, you create the departure

rules for the different departure times on the various days of the week.

After you have created your departure rules, choose Create Trips to calculate the actual departure times automatically. If you want

to change the dates of the departures generated automatically from the departure rule, select the trip in question and enter the

deviating dates. You can also add a trip that is not based on a departure rule. If you have assigned a new or updated carrier

schedule to a transportation stage of your departure rule, you have to regenerate the departures with the changed data.

## Example

Example of the Use of Departure Rules

## Example of the Use of Departure Rules

You want to define several departure rules for your carrier flight schedule from Frankfurt airport to John F. Kennedy airport in New

York via London Heathrow with differing departure times and transit durations on the various days of the week. One of these

departure rules applies every Monday.

In this departure rule, you specify the departure time from Frankfurt airport as 05:00 CET and the transit duration for the flight to

London Heathrow, which is one hour. The system calculates the arrival time in London Heathrow as 05:00 GMT UK.

Based on your cut-off times and the length of stay, which you specified as three hours, the system calculates the departure time

for the flight to John F. Kennedy airport in New York. The time determined is 08:00 GMT UK. Since you specified eight hours as the

transit duration, the system calculates the arrival time at John F. Kennedy airport in New York as 11:00 EST.

If the departure time from Frankfurt airport is moved back by two hours to 07:00 CET, the system adjusts the departure times and

arrival times in London and New York accordingly. The new arrival time in New York is therefore 13:00 EST.

You can use this departure rule as a transportation stage in the departure rule for a master flight schedule by first entering your

airport of departure and your airport of destination in the standard airport sequence of your master flight schedule, and assigning

This is custom documentation. For more information, please visit SAP Help Portal.

73


1/14/26, 2:16 PM

a corresponding carrier flight schedule to it. If you then create departure rules for your master flight schedule, you can select a

suitable departure rule from the referenced carrier flight schedule. The departure rule from the carrier flight schedule appears as

the only transportation stage in the departure rule for the master flight schedule.

The pre-carriage for this master flight schedule is from a gateway at Frankfurt airport to the airport. In the on-carriage, the goods

are transported from the John F. Kennedy airport in New York to a gateway at the airport. The source location of the main carriage

is Frankfurt airport and the destination location is John F. Kennedy airport in New York. The departure time from Frankfurt airport

is 07:00 CET and the arrival time in New York is 13:00 EST.

In the gateway schedule, you can now define the transportation stages of the pre-carriage and on-carriage as parts of the

departure rule. The departure time from your gateway at Frankfurt airport is 05:00:00 AM CET. The transit duration from the

gateway to the airport amounts to two hours. This means the goods arrive at Frankfurt airport on time for the departure at 07:00.

You specify the length of stay at John F. Kennedy airport in New York as two hours. The availability time at the gateway is therefore

15:00 EST. The customer can pick the goods up here at 15:00 EST.

If, in the referenced carrier flight schedule, the departure time at Frankfurt airport is moved from 5:00 EST to 7:00 CET so that the

arrival time at John F. Kennedy airport in New York is no longer 13:00 EST but 15:00 EST, the system changes the status of the

referenced data in the master flight schedule from Data Is Up-to-date to Data Is Not Up-to-date. In the departure rule of the

master flight schedule, you can navigate via a link to the referenced carrier flight schedule, and there check exactly which times

have changed. If you transfer the changed departure time at Frankfurter airport and the changed arrival time at John F. Kennedy

airport in New York to your master flight schedule, the system changes the status of the referenced data from Data Is Not Up-to-

date back to Data Is Up-to-date.

Trade Lane

## Definition

A trade lane is a classification of any transport-related activities representing a combination of zones or locations combined with a

transportation mode or means of transport and providing an orientation between the source and destination.

Examples of trade lanes include:

All transports from Hamburg to New York

All transports within Germany

## All transports that leave Bavaria

Trade lanes are not a substitute for transportation lanes. For planning purposes transportation lanes must be maintained even if a

suitable trade lane exists.

Trade lanes can form a hierarchy. This means that more generic trade lanes can contain more specific trade lanes. For example,

“Within Germany Using Means of Transport Truck” contains “Along the Way from Frankfurt to Hamburg with Means of Transport

Refrigerated Truck” and “Within Bavaria with Means of Transport Truck for Liquids”.

Trade lanes may overlap, for example, “From Germany Using Airplane” and “Within Europe Using Airplane”.

Trade lane hierarchies contain the following:

Transportation zone hierarchies, for example, “From Germany” contains “From Bavaria”, and this contains “From

## Plant_MÜNCHEN”

This is custom documentation. For more information, please visit SAP Help Portal.

74


1/14/26, 2:16 PM

Hierarchical relationships between means of transport, for example, “Within Germany Using Means of Transport Truck”

contains “Within Germany Using Means of Transport Refrigerated Truck”

Means of transport/transportation mode relationship, for example, “Within Germany Using Transportation Mode Street”

contains “Within Germany Using Means of Transport Refrigerated Truck”

In previous releases, trade lanes were created from, and associated with other business objects such as Business Shares,

Allocations, and Freight Agreements. You can now use trade lanes as full master data objects, creating, copying, and reusing them

according to the needs of your business. You can view all available trade lanes in a worklist and, view information such as a where-

used list.

You can configure the types of trade lanes that can be used to create trade lanes. For more information see Customizing for

Transportation Management under  Transportation Management

## Master Data

 Transportation Network

 Trade Lane

## Structure

You define the following settings for a trade lane:

## Description

Transportation Mode

Means of Transport

## Orientation

Possible settings:

Inbound

Outbound

From

To

Along

Within

## Source

Source Type

Destination

Destination Type

## Integration

This business object is used by several processes in Transportation Management (TM). For more information, see:

Creation of Business Shares and Transportation Allocations

Carrier Selection

## Agreement Maintenance

This is custom documentation. For more information, please visit SAP Help Portal.

75


1/14/26, 2:16 PM

Trade Lane Upload

## Use

You use this function to automatically create and delete trade lanes in TM by uploading a list of trade lanes.

## Integration

For more information about the integration of Trade Lanes into TM, see Trade Lane.

## Prerequisites

You have defined number range intervals for trade lanes Customizing for Transportation Management. For more information see

Customizing for Transportation Management under  Transportation Management

## Master Data

 Transportation Network

## Trade Lane

 Define Number Range Intervals for Trade Lanes .

  Note

In order to use a specific Trade Lane ID, you have to define an external number range. If you do not define an external number

range, the report assigns automatically a number from the internal number range to the trade lane.

You have defined types of trade lanes in Customizing for Transportation Management. For more information see Customizing for

Transportation Management under  Transportation Management

## Master Data

 Transportation Network

## Trade Lane

 Define Trade Lane Types .

You have created an XLS or XLSX file containing a list of trade lanes that you want to create or delete in TM.

The list contains the following columns:

## Excel ID

Trade Lane ID

Trade Lane Type

Transportation Mode

Means of Transport

Orientation

Source Type

## Source

Destination Type

Destination

## Language

## Trade Lane Description

You enter the details for each trade lane in a separate line.

You can enter multiple descriptions of a single trade lane in different languages. In order to add a description in an

additional language, enter a line with the same Excel ID. Leave all fields blank, except Excel ID, Language and Trade Lane

Description. When you use the same Excel ID repeatedly, the system adds multiple descriptions for the same trade lane.

This is custom documentation. For more information, please visit SAP Help Portal.

76


1/14/26, 2:16 PM

The following restrictions apply:

You cannot enter identical trade lanes with different Trade Lane IDs.

You must assign a unique Excel ID to each trade lane.

  Note

You cannot enter both a Transportation Mode and Means of Transport at the same time.

## Activities

After you have selected a file that contains the list of trade lanes that you want to upload, you can choose whether you want to

create or to delete these trade lanes in TM.

Furthermore, you can specify which lines of the XLS or XLSX file shall be uploaded, in order to exclude explanatory header lines or

similar irrelevant lines.

## Output

After the list of trade lanes has been uploaded to TM, the system runs several checks on the entered data, for example, whether

the data corresponds to predefined requirements or whether entered data is a duplicate of already existing trade lanes.

After checking the data the system displays a log message and writes the data to TM. If you choose to run the upload in test mode,

the system runs the background checks and creates a log message, but does not write the data to TM.

Default Route

## Use

You use this function to define a sequence of transshipment locations. For each default route you can specify the transportation

mode, carrier, schedule, and so on, for each transportation stage. The system considers default routes as possible routes for a

shipment between two locations.

In the transportation cockpit, you can manually assign or unassign freight unit stages and transportation unit stages to default

routes. This is also possible on the user interfaces of these business documents.

You can also use default routes in VSR optimization (see Use of Default Routes in VSR Optimization).

## Prerequisites

You have defined locations.

You have configured the settings in the Customizing activity Define Default Route Types under  Transportation

Management

## Master Data

 Transportation Network .

## Activities

To create a default route, open the Create Default Route app on the launchpad.

Transportation Management is shipped with default route type 3000.

This is custom documentation. For more information, please visit SAP Help Portal.

77


1/14/26, 2:16 PM
## More Information

For more information about how default routes are used in conjunction with forwarding orders, see Direct Creation of Freight

Documents and Selection of Schedules.

For an example of how default routes can be used together with schedules, see Example: Schedules for Sea Traffic.

For more information about the interaction of the default route and the determination of transportation distance and

transportation duration, see Determination of Transportation Distance and Transportation Duration.

Use of Default Routes in VSR Optimization

## Use

You use this function to consider default routes when you generate routes for the transport of freight units and transportation

units in VSR optimization. In your optimizer settings, you can specify how default routes are to be used when you process freight

units and transportation units in VSR optimization.

  Note

This function is not supported for trailer units.

## Prerequisites

You have defined default routes (see Default Route).

You have selected the required checkboxes in Customizing for Transportation Management under  Transportation Management

## Master Data

## Transportation Network

 Define Default Route Types  under Optimizer Settings.

In the optimizer settings of your planning profile, you have selected an option to consider default routes in VSR optimization. To do

this, open the Edit Optimizer Settings app on the launchpad.

## Features

When you use default routes in VSR optimization, you have the following options:

## Only consider default routes

The VSR optimizer searches only for default routes as possible routes for the transport of your freight units and

transportation units.

## Prefer default routes

The VSR optimizer searches for default routes but also generates alternative routes as possible routes for the transport of

your freight units and transportation units. If the VSR optimizer identifies a default route as a possible route, it

automatically selects the default route without considering the planning costs of the alternative routes.

## Also consider default routes

The VSR optimizer searches for default routes but also generates alternative routes as possible routes for the transport of

your freight units and transportation units. The VSR optimizer then selects the route with the lowest planning costs.

## Do not consider default routes

This is custom documentation. For more information, please visit SAP Help Portal.

78


1/14/26, 2:16 PM

The VSR optimizer does not search for default routes as possible routes for the transport of your freight units and

transportation units. If the VSR optimizer generates only routes based on transshipment locations, these routes may by

chance correspond to one of your default routes.

## Standard Integration with SAP HANA spatial services

Transportation Management is capable of using information determined by external geographical information system (GIS)

applications for geocoding, distances and durations, and georouting.

Using external GIS services requires custom code since the used Supply Chain Execution (SCE) GIS integration framework is a

generic framework and does not provide any vendor-specific connectors. With the introduction of SAP HANA spatial services, SAP

now offers a corresponding integration for this framework. The use of this integration enables the consumption of SAP HANA

spatial services without writing custom coding.

For more information about setting up this standard integration, see SAP Note 2751622

 (Setup Guide for SAP HANA Spatial

Services in SCE Applications).

For more information about SAP HANA spatial services, see SAP HANA spatial services.

Related Information

Using GIS Metrics

Using GIS Metrics

## Use

You can use GIS (Geographical Information System) metrics for monitoring and reporting purposes. GIS metrics are created in the

GIS Integration Framework when GIS requests are processed. In Transportation Management, you can display GIS metrics and

delete them.

## Prerequisites

For more information about the prerequisites for using the GIS Integration Framework, see SAP Note 2751622

 (Setup Guide for

SAP HANA Spatial Services in SCE Applications).

## Activities

To display GIS metrics, on the SAP Easy Access menu choose  Logistics

 Transportation Management

## Master Data

 Transportation Network

 Display GIS Metrics .

To delete GIS metrics, on the SAP Easy Access menu choose  Logistics

 Transportation Management

## Master Data

 Transportation Network

 Delete GIS Metrics .

Related Information

Display of GIS Metrics

Deletion of GIS Metrics

## Process Controller Configuration

This is custom documentation. For more information, please visit SAP Help Portal.

79


1/14/26, 2:16 PM

Display of GIS Metrics

## Use

You can use this report to display GIS (Geographical Information System) metrics. GIS metrics are created in the GIS Integration

Framework when GIS requests are processed. They can be used for monitoring and reporting purposes.

Features

## Selection

You need to indicate the following:

A process controller strategy that is relevant for the GIS Integration Framework

A horizon or a time window to select the relevant entries

## Outputs

On the GIS Metrics Display Summary screen, you can see the following information, for example:

The GIS service that was used (gecoding, georouting, or distance and duration determination)

The GIS provider who processed the GIS requests

The number of successful and failed calls to SAP HANA spatial services

The number of successful GIS requests, such as the number of routes for georouting

## The number of failed GIS requests

The number of transaction objects, such as the number of source locations for distance and duration determination

## Activities

To start the report, enter transaction code /SCMB/GIS_METR_DISPL in the command field.

Related Information

Process Controller

Deletion of GIS Metrics

## Use

You can use this report to delete GIS (Geographical Information System) metrics to clean up your database. GIS metrics are

created in the GIS Integration Framework when GIS requests are processed.

Features

## Selection

This is custom documentation. For more information, please visit SAP Help Portal.

80


1/14/26, 2:16 PM

You need to indicate the following:

A process controller strategy that is relevant for the GIS Integration Framework

A horizon or a time window to select the relevant entries

## Outputs

On the GIS Metrics Deletion Summary screen, you can see the following information, for example:

The GIS service that was used (gecoding, georouting, or distance and duration determination)

The GIS provider who processed the GIS requests

The number of successful and failed calls to SAP HANA spatial services

The number of successful GIS requests, such as the number of routes for georouting

## The number of failed GIS requests

The number of transaction objects, such as the number of source locations for distance and duration determination

## Activities

To start the report, enter transaction code /SCMB/GIS_METR_DEL in the command field.

Related Information

Process Controller

Transportation Mode

## Definition

You can use these features to define master data that is specific to a particular transportation mode, for example, air freight or

ocean freight. You can specify the following settings:

Air freight and ocean freight codes (see Transportation-Mode-Specific Codes)

Air waybill stock numbers (see Waybill Stock Definition)

## More Information

For more information about transportation modes, see Customizing for Transportation Management under  Master Data

 Transportation Network

 Transportation Lane

 Define Transportation Mode .

Transportation-Mode-Specific Codes

## Definition

Transportation Management allows you to define codes that are specific to various transportation modes. These codes are

explained in detail below.

This is custom documentation. For more information, please visit SAP Help Portal.

81


1/14/26, 2:16 PM

Air-Freight-Specific Codes

## Location codes

You can define air-freight-specific locations such as airports or cities in the vicinity of airports. When you create an air-

freight-specific document such as an air forwarding order or air freight booking, you can enter the airport of departure and

the airport of destination on the user interface. The system then automatically determines the correct location code from

the master data and displays it in read-only mode.

If you enter a one-time location (see One-Time Location) in your document, you can specify the location code directly in the

document.

The system also takes location codes into account when calculating charges.

You define locations codes in Customizing for Transportation Management under  Master Data

 Transportation

Network

## Location

 Define IATA Location Codes .

## Aircraft type codes

You can define aircraft type codes and assign a category to them to specify, for example, whether the aircraft is a freighter

or passenger aircraft.

You define aircraft type codes in Customizing for Transportation Management under  Master Data

 Resouces

## Define

IATA Aircraft Type Codes .

## Airline codes

You can define airline codes for each of your air-freight carriers and assign an air waybill prefix to them. You can also specify

whether the carrier is a member of the International Air Transport Association (IATA).

When you then create an air-freight document such as an air forwarding order, you can enter your airline code on the user

interface. The system then automatically identifies the associated air waybill prefix. If there is a one-to-one relationship

between the airline code and the associated carrier, the system can also determine the relevant carrier when you enter the

airline code.

You define airline codes in Customizing for Transportation Management under  Master Data

## Business Partners

 Define IATA Airline Codes .

## Handling codes

You can define handling codes to specify how certain types of freight are to be transported. For example, you can specify

that goods are perishable and must, therefore, be transported in a refrigeration unit.

You define handling codes in Customizing for Transportation Management under  Basic Functions

 General Settings

## Define Handling Codes

## Traffic conference areas and region codes

You can define traffic conference areas, which designate a part of the world, and assign them to regions. You can also assign

a country or region to the different regions.

You define traffic conference areas and region codes in Customizing for Transportation Management under  Master Data

## Transportation Network

 Define IATA Traffic Conference Areas  and  Master Data

## Transportation Network

 Define IATA Region Codes  respectively. You can also assign countries or regions to region codes by choosing  Master

## Data

## Transportation Network

 Assign Countries/Regions to IATA Regions .

## Other charge codes and notes

You can define charge codes that are defined by the International Air Transport Association (IATA) as Other Charges. You

can also enter IATA notes, which the system takes into account when calculating charges.

This is custom documentation. For more information, please visit SAP Help Portal.

82


1/14/26, 2:16 PM

You define other charge codes and notes in Customizing for Transportation Management under  Basic Functions

 Charge Calculation

## Basic Settings

 Maintain IATA Other Charge Codes  and  Basic Functions

 Charge Calculation

 Air Freight Settings

 Maintain IATA Notes .

Ocean-Freight-Specific Codes

Standard carrier alpha code (SCAC)

You define SCACs in Customizing and specify the period for which they are to be valid. When you assign SCACs to carriers,

the values that you have defined are proposed in the SCAC input help. You can, therefore, enter a SCAC to find the

associated carrier and vice versa.

You define SCACs in Customizing for Transportation Management under  Master Data

 Business Partners

## Define

Standard Carrier Alpha Codes .

United Nations Code for Trade and Transport Locations (UN/LOCODE)

You define UN/LOCODEs in the location master data and assign them to a container freight station (CFS) or a port, for

example. When you enter a location in your ocean forwarding order or ocean booking, the system automatically determines

the correct UN/LOCODE from the master data and displays it in the document in read-only mode.

If you enter a one-time location in your document, you can specify the UN/LOCODE directly in your document.

You define UN/LOCODEs in the Define Location app which you can open from the launchpad.

## More Information

For more information about defining business partners (airlines), see Definition of Business Partners.

For more information about locations, see Location.

For more information about SCACs and airline codes in Freight Order Management, see Carrier Categorization.

Product

## Definition

A tangible or intangible good that is part of the business activities of a company. It can be traded and it contributes directly or

indirectly to the value chain.

## Use

You use this object to manage global product master data.

  Note

Transportation Management (TM) does not use location-dependent products. TM uses product information which is

maintained under

Basic Data 1

Basic Data 2

## Additional Data

## Material description in different languages

This is custom documentation. For more information, please visit SAP Help Portal.

83


1/14/26, 2:16 PM

Units of Measure

## Structure

The product master data is maintained on a number of tab pages.

  Note

Some of the tab pages contain data that is not relevant for TM.

You identify each product with a unique product number, and an appropriate description.

You define whether the product is a packaging material by choosing the material group for packaging materials.

More Information

## Product Master

Definition of Products

## Use

You use this process to define products that are transportable goods.

## Prerequisites

In Customizing for Transportation Management, you have defined the following:

You have defined transportation groups under  Transportation Management

 Master Data

 Product

## Maintain

Transportation Group .

You have defined the packaging material types under  Transportation Management

 Master Data

 Product

## Define

Packaging Material Types .

## Process

You define a product in the Create Material app, which you can open from the launchpad.

Use of Change Documents for Products

## Use

You use this process to trace changes that are made to products in Transportation Management (TM).

The changes are logged in change documents, which allow you to find out at any time, what was changed, when the changes

occurred, and how the changes were made.

## Process

This is custom documentation. For more information, please visit SAP Help Portal.

84


1/14/26, 2:16 PM

You display the change documents for products in the Display Change Documents app, which you open from the launchpad.

## Classification of Goods

Commodity codes are a set of classification codes used in the global marketplace to identify goods and services. Commodity

codes group together goods and services and can differ for each country.

## Use

You can classify and evaluate your goods to be transported (commodities) according to characteristics of your choice. Each

commodity has its own commodity code. You can group commodity codes using a commodity code type. The classification

schemas (commodity code types) used for this purpose may depend on the transportation mode or country, for example.

When classifying goods, you can take into account transportation-relevant product characteristics, such as weight, density,

loading properties, and handling (of dangerous goods, for example).

You can use this function in Transportation Management (TM) for the following purposes:

Charge calculation for incoming invoices

## Printing

Commodity codes can be used when printing business documents. For more information, see Printing.

You have the following two options for determining commodity codes in TM:

Using commodity codes assigned to the material master

Using commodity codes assigned to items locally

## Related Information

Commodity Codes Assigned to Material Master

Commodity Codes Assigned to Items Locally

## Commodity Codes Assigned to Material Master

You can use a source based on SAP Governance, Risk and Compliance (GRC), that is, a source in the masterial master, to create

commodity codes in Transportation Management.

## Prerequisites

In Customizing for Transportation Management, under  Freight Order Management

## Freight Order

## Define Freight Order

Types , you have chosen Use Commodity Codes Assigned to Material Master.

You have made settings in the following activities in Customizing for Transportation Management, under  Master Data

 Classification of Goods :

Define Numbering Scheme for Commodity Codes

Define Numbering Scheme Content for Commodity Codes

## Activate Numbering Scheme Content for Commodity Codes

This is custom documentation. For more information, please visit SAP Help Portal.

85


1/14/26, 2:16 PM

Assign Numbering Scheme Content for Commodity Codes to Country/Region

## Use

You can use numbering schemes to create entries for commodity codes. You can maintain all the different types of numbering

schemes, their respective content, the link between the numbering scheme and the content, and also the country assignment by

making settings in Customizing.

You then assign the commodity code to a product and classify your products. To do so, you use the following apps on the

launchpad:

## Manage Commodity Codes for Transportation

You use this app to create entries for commodity codes for your chosen numbering scheme content.

You select the numbering scheme content, enter the commodity code for that numbering scheme content, and enter the

validity period. You can enter a validity period within the validity period you chose in the Customizing activity Activate

Numbering Scheme Content for Commodity Codes. You can also enter a description for the commodity code in a

language that you choose.

## Classify Products - Commodity Codes for Transportation

The new entry for the commodity code is then visible in this app. You can search for the new entry using the numbering

scheme and assign the commodity code to a product and enter the validity period.

You can display the commodity codes assigned to products by navigating to the detailed view of a freight order, freight booking,

freight unit, or consignment order. In the Items tab, select a product, and then Commodity Codes.

## Commodity Codes Assigned to Items Locally

You can use a local source in Transportation Management to create commodity codes.

## Prerequisites

In Customizing for Transportation Management, under  Freight Order Management

## Freight Order

## Define Freight Order

Types , you have chosen Use Commodity Codes Assigned to Items Locally.

You have defined commodity codes and commodity code types in Customizing for Transportation Management under  Master

## Data

 Classification of Goods

 Define Commodity Codes .

## Features

Commodity codes classify goods (commodities) based on various classification schemas (commodity code types). You can enter

commodity codes that belong to various classification schemas as value lists in Customizing.

You can make a selection on the following UIs:

## Forwarding Order

You can assign the commodity codes to cargo items when you create a forwarding order.

## Freight Booking

This is custom documentation. For more information, please visit SAP Help Portal.

86


1/14/26, 2:16 PM

The system copies the commodity codes from the forwarding order. You can adjust the commodity codes in the freight

booking as required. For more information, see Freight Booking and Management of Air Freight Bookings for Airlines.

## Freight Order

The system copies the commodity codes from the forwarding order. You can adjust the commodity codes in the freight

order as required. For more information, see Freight Order.

## Example

The commodity code type Cereal has the abbreviation CR and the following commodity codes:

Commodity Code Description

100

101

200

201

300

301

## Wheat

Organic wheat

## Barley

Organic barley

## Rye

## Organic rye

Example: Classification of Goods for Commodity Codes Assigned
to Items Locally

## Use

You use this process to classify and evaluate your goods to be transported according to characteristics of your choice.

## Prerequisites

In Customizing for Transportation Management, under  Freight Order Management

## Freight Order

## Define Freight Order

Types , you have chosen Use Commodity Codes Assigned to Items Locally.

You have defined commodity codes and commodity code types in Customizing for Transportation Management under  Master

## Data

 Classification of Goods

 Define Commodity Codes .

## Process

The following example outlines how to classify a cargo:

1. Changing the forwarding order

Open the Change Forwarding Order app on the launchpad. You display the detail data for a main cargo item and open the

Commodity Codes tab page.

You define the cargo as commodity code type Cereal with commodity code 300 (rye) and save your entries. When you save

the data, the system copies the classification to the corresponding freight order or freight booking.

2. Displaying or checking the freight order or freight booking for the forwarding order

This is custom documentation. For more information, please visit SAP Help Portal.

87


1/14/26, 2:16 PM

Open the Change Air Freight Booking or Change Ocean Freight Booking app on the launchpad. You display the detail data

for a main cargo item and open the Commodity Codes tab page. You now check whether the system has copied the

commodity code type and commodity code correctly from the forwarding order.

  Recommendation

From the forwarding order, you can also navigate to the follow-on documents Freight Order or Freight Booking using the

Document Flow tab page, and to the Commodity Codes tab page using the Cargo Management tab page.

3. Changing the freight order or freight booking for the forwarding order

In the freight order or freight booking, you display the detail data for a main cargo item and open the Commodity Codes

tab page. You select the Deviating Commodity Codes checkbox, change the commodity code to 301 (organic rye), and save

your entries. When you save your data, the commodity codes in the freight order or freight booking are adjusted. The

commodity codes in the forwarding order remain unchanged. Once the data is saved, no further data is copied from the

forwarding order to the freight order or freight booking.

## Result

Goods have been classified in the forwarding order.

Goods in the freight order or freight booking are classified either from the forwarding order or locally in the freight order or freight

booking using the Deviating Commodity Codes checkbox.

Equipment Groups and Equipment Types

## Use

You can use equipment types to group resources that have the same attributes. You can use equipment groups to group

equipment types into categories. If you work with containers, you need to assign the container groups to the relevant

transportation modes.

You can perform planning based on equipment groups and types.

## Features

## Grouping of Resources

When you define a resource in the resource master data transaction, you can assign an equipment group and type. By doing so,

this resource belongs to this equipment type and shares its attributes. You can also copy equipment group and type data into your

resource and use it as a template.

You can use an equipment type in various profiles, such as the capacity availability settings, to control the behavior of all resources

assigned to this equipment type.

## Planning Based on Equipment Types

For scenarios, in which you regularly subcontract your transportation demands to a carrier and prefer to work with vehicle or

container types, we recommend that you define equipment types. An equipment type can be assigned to an unlimited number of

capacity documents at the same point in time. Note that if you want to use planning based on equipment types, the name of the

equipment type needs to be unique across all equipment groups.

For more information, see Planning Based on Equipment Types.

This is custom documentation. For more information, please visit SAP Help Portal.

88


1/14/26, 2:16 PM

## Freight Unit Building

When you create freight units, you can take into account equipment types and their dimensions instead of the planning-relevant

quantities.

For more information, see Consideration of Equipment Data During FU Creation.

## Container

You can use equipment groups and types, for example, when creating forwarding order or forwarding quotation items of the

category Container. The physical property data of the container is then available in the forwarding order and subsequent business

documents as information for the planner. In addition, after you have entered the equipment group, the equipment type, and the

number of containers in the forwarding order, the system calculates the tare weight and the capacity of the container in twenty-

foot equivalents units (TEUs) based on the Customizing settings. If you have assigned an equipment group to the item type in

Customizing, the equipment group is entered automatically for an item with this item type, and equipment types of this group are

displayed for selection.

For more information, see Creation of Forwarding Order Items or Forwarding Quotation Items.

## Carrier profiles

When you define carrier profiles, you can use equipment types to describe the kind of equipment that is owned by the carrier.

For more information, see Definition of Carrier Profiles.

  Note

Equipment group and equipment type are generic terms. In Transportation Management (TM), the most specific term is

used on the user interface where possible. If this is not possible, the generic term equipment type or vehicle type is

used.

The following equipment types are supported:

Vehicle type

Truck type

Trailer type

Locomotive type

Railcar type

## Container type

Handling resource type

## Activities

You define equipment groups and types in Customizing.

1. To define a new equipment group, for example, a vehicle group, select the Vehicle Groups view and enter a name and a

description and select a resource class.

2. To define a vehicle type for your new vehicle group, select your vehicle group and then the Vehicle Types view and enter a

name and a description. By double-clicking on the vehicle type, the details screen that lets you enter the attributes of the

vehicle type is displayed.

This is custom documentation. For more information, please visit SAP Help Portal.

89


1/14/26, 2:16 PM

For example, you can define capacity and weight for your container types. For your truck types, you can define parameters,

such as payload weight or CO  emissions. For more information, see Customizing for CO2 Emissions Calculation.

2

For more information, see Customizing for Transportation Management under  Master Data

## Resources

 Define Equipment

Groups and Types .

If required, you can implement a consistency check. For a possible implementation, see Customizing for Transportation

Management, under  Business Add-Ins (BAdIs) for Transportation Management

 Master Data

## General Settings

## Equipment Types and Equipment Groups

 BAdI: Consistency Check for Equipment Types . This implementation checks

whether an equipment type has been assigned to exactly one equipment group.

Customizing for CO  Emissions Calculation

2

You can set the parameters by which carbon dioxide (CO ) emissions for a vehicle type are calculated. You must specify emissions

2

for a laden and unladen vehicle.

## Greenhouse Gas Emissions

Transportation Management (TM) measure CO  emissions for a road freight order based on the parameters you set for a vehicle

2

type. You indicate the value in the standardized CO  equivalents (CO e). In addition to the parameters you indicate below, you must

2

2

specify the payload weight and its unit of measure to enable the calculation of CO  emissions.

2

CO  Emissions (Empty)

2

You indicate an unladen vehicle's average CO  emissions.

2

CO  Emissions (Full)

2

You indicate a laden vehicle's average CO  emissions. A laden vehicle refers to a vehicle's gross combination weight, that is the

2

weight of the vehicle and the maximum permissible load weight.

## Units of Measurement

You must also indicate the unit of weight, for example, kilograms, and unit of distance, for example, kilometers.

## Road Freight Order

CO  emissions are reflected in the Edit Road Freight Order app and the Transportation Cockpit app. For more information, see

2

Greenhouse Gas Emissions.

## Activities

You set greenhouse gas emissions parameters in Customizing.

1. Select the Vehicle Groups.

2. Double-click on Vehicle Types.

3. For groups with multiple vehicle types, double-click on the type you wish to configure.

4. Set the parameters under the section Greenhouse Gas Emissions.

This is custom documentation. For more information, please visit SAP Help Portal.

90


1/14/26, 2:16 PM

For more information, see Customizing for Transportation Management under  Master Data

## Resources

 Define Equipment

Groups and Types .

Definition of Resources

## Use

Resources play a central role in planning and execution within Transportation Management. Resource data is relevant to the

planning of order dates taking into account working times and the available capacities of the resources. Resources, in conjunction

with booking, offer the capacity needed to perform transportation activities on freight units, such as transportation, loading, and

unloading activities.

## Features

The following resource types exist:

Calendar resource (see Calendar Resource)

Vehicle resource (see Vehicle Resource)

Handling resource (see Handling Resource)

Drivers (see Driver)

Transportation unit resource (see Transportation Unit Resource)

  Note
Drivers are defined in Transportation Management as business partners. However, they are often handled in the same way as

resources and are, therefore, described here.

## Activities

To create, change, or display resources, you have the following options:

On the SAP Easy Access screen, choose  Transportation Management

 Master Data

 Resource

 Resource .

In SAP launchpad, open the Define Resource app.

For more information, see the following sections:

Creating handling, vehicle, and calendar resources (see Creating Handling, Vehicle, and Calendar Resources)

Creating drivers (see Creating Drivers)

Copying resources (see Copying Resources)

Copying resources from template (see Copying Resources from Templates)

Deleting resources (see Deleting Resources)

## Classification of Resources

This is custom documentation. For more information, please visit SAP Help Portal.

91


1/14/26, 2:16 PM
## Use

You can use resource classes to group resources that have the same characteristics or types (for example, vehicle resources or

handling resources). This enables you to see at a glance exactly what kinds of resources are available for transportation planning.

You assign the resource class to a means of transport or an equipment group. The system then automatically assigns the correct

resource class to the resource when you specify the means of transport or equipment group.

## Prerequisites

You have defined resource classes in Customizing for Transportation Management under  Master Data

## Resources

 Define Resource Class .

You have defined means of transport in Customizing for Transportation Management under  Master Data

## Resources

 Define Means of Transport

.

You have defined equipment groups in Customizing for Transportation Management under  Master Data

## Resources

 Define Equipment Groups and Equipment Types .

## Features

## Vehicle Resources

You can use resource classes to specify the kind of vehicle that is to be used for your transportation activities. When you enter the

means of transport in the resource master data, the system automatically determines the resource class based on the means of

transport.

For example, if you have assigned the resource class Trailer to means of transport MTR_1 and subsequently create a resource with

means of transport MTR_1, the system automatically determines that your resource is a trailer.

If you do not assign a resource class to the means of transport, the system determines the resource class based on the

transportation mode and whether the vehicle resource is passive. The default values in this case are shown in the following table:

Transportation Mode

## Passive

Default Resource Class

Road

Road

Rail

Rail

Sea

## Air

Handling Resources

No

Yes

No

## Yes

Truck

Trailer

Locomotive

## Rail Car

Not applicable

## Vessel

Not applicable

## Airplane

You can use resource classes to specify the kind of equipment that is used to handle goods at a specific location (for example,

whether the piece of equipment is a dolly or a forklift truck). When you enter the equipment group in the handling resource master

data, the system automatically determines the resource class based on the equipment group.

For example, if you have assigned the resource class Forklift Truck to the handling resource group (that is, the equipment group)

EQ1, the system automatically determines that the resource class is to be Forklift Truck when you enter EQ1 in the resource

master data.

This is custom documentation. For more information, please visit SAP Help Portal.

92


1/14/26, 2:16 PM

If you do not assign a resource class to the handling resource group, the resource class defaults to Doors.

## Transportation Unit Resources

You can use resource classes to specify the kind of transportation unit resource that is to be used for your transportation activities.

When you enter the equipment group in the transportation unit resource master data, the system automatically determines the

resource class based on the equipment group.

For example, if you have assigned the resource class Container to the transportation unit group (that is, the equipment group) CN,

the system automatically determines that the resource class is to be Container when you enter CN in the resource master data. If

you do not assign a resource class to the transportation unit group, the resource class defaults to Container.

## More Information

Definition of Means of Transport

## Related Information

Equipment Groups and Equipment Types

## Resource Types

In the following sections, you can find information about the resource types:

Calendar resource (see Calendar Resource)

Vehicle resource (see Vehicle Resource)

Handling resource (see Handling Resource)

Driver (see Driver)

Transportation Unit resource (see Transportation Unit Resource)

Calendar Resource

## Definition

Resource that you can assign to a calendar and optionally to a shift. It is used particularly for scheduling the goods receipt and

goods issue processing time.

## Use

You use calendar resources to specify operating times for locations. For more information, see Operating Times.

  Note

You cannot define a capacity profile for calendar resources. For more information, see Definition of Capacity Profiles.

## Structure

This is custom documentation. For more information, please visit SAP Help Portal.

93


1/14/26, 2:16 PM

You can define, among others, the following parameters for calendar resources:

## Shifts

For more information about shifts, see Definition of Capacity Variants.

Downtimes (see Definition of Downtimes)

Vehicle Resource

## Definition

An instance of a particular means of transport, or a group of identical instances of means of transport that can provide

transportation services.

## Use

You use this business object to map the capacity and availability of vehicles that you want to use for transportation.

You can choose up to eight dimensions and units of measurement to describe the capacity. Note that the mass and volume are

predefined by default. Planning can only take the vehicle capacity into account if these correspond to the dimensions and units of

measurement that you have defined in a freight unit building rule.

  Note

You cannot define the available capacity for this resource type dependent on time. However, you can define a time-dependent

availability using shift sequences. For more information about defining shift sequences, see Specification of Definitions and

Creating Definitions.

In the planning profile, you can specify whether the system can consider a manual overload of the resource capacity.

## Vehicle Group and Vehicle Type

The vehicle and vehicle group types specify attributes such as the physical properties of a certain kind of vehicle. When you have

created a vehicle type you can:

use the type as a template to create vehicle resources, copying the attributes of the type to new resource

request a special type of vehicle resource in a forwarding order or in booking order. (This is similar to the function already

available for container groups and types).

For more information see Customizing for Transport Management under  Transportation Management

 Master Data

## Resources

 Define Equipment Groups and Equipment Types .

## Structure

You can define, among others, the following parameters for vehicle resources:

## Passive means of transport

In Customizing, you can define vehicle resources that cannot move by themselves, by selecting the Passive Means of

Transport checkbox for the means of transport assigned to the vehicle resource.

For more information, see Definition of Means of Transport.

This is custom documentation. For more information, please visit SAP Help Portal.

94


1/14/26, 2:16 PM

## Combination vehicle

You can combine vehicle resources as follows:

## Vehicle-resource combination

If you have your own fleet and want to dynamically couple or uncouple a tractor and trailer, we recommend that you

work with vehicle-resource combinations. VSR optimization can dynamically combine the individual components for

vehicle-resource combinations. This is based on the prerequisite that you have defined means-of-transport

combinations in Customizing under  Master Data

## Resources

 Means of Transport and Compartment

## Define

Means-of-Transport Combination . For more information, see Definition of Means-of-Transport Combinations.

## Combination resource

If you do not have your own fleet you can perform VSR optimization on the level of the combination resource. This

means that VSR optimization does not have to deal with the coupling and uncoupling of the individual components

of the combination resource. For more information, see Definition of Combination Resources.

Loading requirements.

You can specify for vehicle resources and locations whether they can be loaded or unloaded from the left, right, back, or

top. Further, you can specify the equipment that is attached to a vehicle resource and the equipment that is required for

loading and unloading at a location, for example, a forklift. A vehicle resource can only be loaded or unloaded at a location if

it fulfills at least one of the loading direction requirements and all of the attached equipment requirements of this location.

For more information see Loading Requirements for Vehicle Resources.

## Compartment

You can divide the loading space of a vehicle resource into compartments.

For more information, see Definition of Compartments.

Capacity (see Definition of Capacity)

Availability (see Definition of Availability)

## Minimum number of seals

You can specify the minimum number of seals of the vehicle resource. You can use this information for the definition of

incompatibilities.

Resource template (see Copying Resources from Templates)

Physical properties (see Definition of Physical Properties)

Downtimes (see Definition of Downtimes)

Qualifications (see Definition of Qualifications)

Attached equipment (see Definition of Attached Equipment)

Grouping attributes (see Definition of Grouping Attributes)

Alternative names (see Definition of Alternative Names)

## Integration

To define vehicle resources, you must have defined means of transport. For more information, see Definition of Means of Transport.

## More Information

This is custom documentation. For more information, please visit SAP Help Portal.

95


1/14/26, 2:16 PM

## Freight Unit Building Rule

Definition of Dimensions and Units of Measurement

Planning Profile

## Incompatibilities

Loading Requirements for Vehicle Resources

You can define loading requirements for vehicle resources.

These requirements can be taken into account in VSR optimization, load consolidation, and for the generation of transportation

proposals. The system considers the requirements specified for locations and resources and can identify incompatibilities that

would, for example, make a resource unsuitable for use at a specific location. For manual planning, you can specify how the system

should handle, for example, a plan that includes a resource that is not compatible with the specified location.

## Features

## Loading Direction Profiles

You can use loading direction profiles to specify:

the direction from which loading or unloading is possible

a preference for loading direction, if required (not yet supported)

For more information see Customizing for Transportation Management under  Master Data

## Resources

## General Settings

 Define Loading Direction Profile .

You can also specify loading direction profiles for locations. For more information see Loading Requirements for Locations.

## Attached Equipment Profiles

You can define attached equipment profiles that describe the equipment provided by the resource for loading/unloading. For more

information see Customizing for Transportation Management under  Master Data

## Resources

 General Settings

## Define

Attached Equipment Profile .

You can also define attached equipment profiles to describe the equipment provided by a location for loading/unloading. For more

information see Loading Requirements for Locations.

In assessing compatibility, the system compares the location’s attached equipment profile with the resource’s attached

equipment profile. Other equipment that is assigned to the resource, for example, loading equipment in a vehicle loading profile, is

not relevant in this context.

## Vehicle Loading Profiles

You can use vehicle loading profiles to define specific loading constraints of a vehicle as follows:

## Loading Direction Profile

Loading Equipment Group/Type (not yet supported)

This is custom documentation. For more information, please visit SAP Help Portal.

96


1/14/26, 2:16 PM

Models a loading equipment, for example, a forklift, the dimensions and weight of which can then be considered during

planning

Loading Equipment Fixed (not yet supported)

Defines whether the loading equipment is attached to the vehicle for every transport.

If it is fixed, planning can rely on the availability of the loading equipment without further checks.

If the loading equipment is not fixed, it could be removed in order to gain additional loading space and/or loading

weight capacity.

Loading Equipment Outside Cargo Space (not yet supported)

Defines whether the vehicle’s loading equipment is placed outside the cargo space.

For more information see Customizing for Transportation Management under  Master Data

## Resources

## General Settings

 Define Vehicle Loading Profile .

## Planning Profile

In the incompatibility settings of your planning profile, you can define constraints for loading direction and attached equipment.

Note that once you define these constraints, we recommend that you check and adapt your master data. That means, add the

loading direction profile and the attached equipment profile to the locations and vehicle resources that should consider these

constraints.

Example: If a location has no loading direction profile defined, no restrictions with regards to this constraint are applied. That

would mean, vehicle resources can be loaded or unloaded from all sides at this location.

For more information, see Planning Profile.

## Related Information

Loading Requirements for Locations

## Planning Profile

Definition of Means of Transport

## Use

You use means of transport to define groups of vehicle resources.

## Features

Means of transport are groups of vehicle resources, for example, container ships or cargo ships. You assign a means of transport to

each vehicle resource.

You can define the following attributes, for example:

## Your Own Means of Transport

You can specify that the means of transport is part of your own fleet.

Passive Means of Transport (Trailers)

This is custom documentation. For more information, please visit SAP Help Portal.

97


1/14/26, 2:16 PM

You can specify that a means of transport cannot move by itself and that it therefore needs to be coupled to a vehicle that

can move by itself. The incompatibilities (see Incompatibilities) as well as the means-of-transport combinations that you

have defined determine whether or not a trailer can be coupled to a vehicle.

You can define a coupling duration and an uncoupling duration for a trailer.

The system schedules the uncoupling activity for a trailer when a different vehicle has to move it in the next stage. If the

system has assigned an empty trailer to a stage, it schedules the coupling activity directly before the transportation activity

and the uncoupling activity directly after the transportation activity.

  Note

You cannot couple trailers to schedules (see Schedule).

Trailers must have capacity.

You cannot define schedules for trailers.

## Transportation Mode

The transportation mode specifies how the goods are transported, for example, as a sea shipment.

The following figure represents the relationship between vehicle resources, means of transport, and transportation modes:

Relationship Between Vehicle Resources, Means of Transport, and Transportation Modes

The vehicle resource is a particular means of transport, for example, the ship “Santa Maria”.

## Superordinate Means of Transport

You can specify a means of transport that is superordinate to a means of transport.

A means of transport A that is superordinate to another superordinate means of transport B is also superordinate to any

subordinate means of transport of the means of transport B.

This is custom documentation. For more information, please visit SAP Help Portal.

98


1/14/26, 2:16 PM

## Multiresource

You can specify that the resource assigned to this means of transport is a multiresource. You can use this attribute if an

unlimited number of resources are available for a means of transport but you want to define the settings for these

resources only once. For more information, see Use of Multiresources.

## No Transportation Lanes Required

You can activate planning with an unlimited transportation network. That means, a vehicle resource with this means of

transport can travel between all locations. Note that this setting is relevant for vehicle scheduling and routing (VSR)

optimization and for scheduling.

## Activities

You create means of transport in Customizing for Transportation Management under  Master Data

 Resources

 Define Means

of Transport

.

You define coupling and uncoupling durations for passive means of transport in Customizing for Transportation Management

under  Master Data

## Resources

 Define Coupling/Uncoupling Duration .

Definition of Means-of-Transport Combinations

## Use

You use a means-of-transport combination (MTr combination) to model vehicle combinations. An MTr combination consists of one

means of transport that can move independently and can move at least one passive means of transport (passive MTr).

## Prerequisites

You have selected the Passive checkbox for the corresponding means of transport for each passive MTr. For more information, see

Customizing for Transportation Management under  Master Data

## Resources

 Define Means of Transport

.

## Features

You can define a total capacity for MTr combinations. The total capacity is the maximum loading capacity without the tare weight

of the vehicle and passive MTr.

You can define incompatibilities for MTr combinations by using attributes (see Incompatibilities).

## Activities

You create MTr combinations in Customizing for Transportation Management under  Master Data

 Resources

## Define Means-

of-Transport Combination .

You define attributes for MTr combinations in Customizing for Transportation Management under  Master Data

## Resources

 Define Attributes of MTr Combination/Compartment

.

## Example

The following table shows the vehicle resources and means of transport you have defined, and the assignments you have made:

This is custom documentation. For more information, please visit SAP Help Portal.

99


1/14/26, 2:16 PM

Vehicle Resources

Means of Transport

TRUCK1

MTRTRUCK1

TRUCK2

MTRTRUCK2

PASSIVEVEH1

MTRPASSIVE1

PASSIVEVEH2

MTRPASSIVE2

According to your business needs, you model the following MTr combinations:

MTRTRUCK1 + MTRPASSIVE1

MTRTRUCK1 + MTRPASSIVE2

MTRTRUCK2 + MTRPASSIVE1

## Definition of Combination Resources

You use combination resources to define groups of vehicle resources.

## Features

A combination resource is the fixed amalgamation of one vehicle resource and one or more passive vehicle resources, for example,

one tractor and two trailers. These component resources are coupled in a fixed sequence and are always used together.

Unlike means of transport combinations, once you define a combination resource, the components are fixed and cannot be

changed, for example, as part of VSR optimization. For more information see about the difference between combination resources

and vehicle-resource combinations, see Vehicle Resource.

Combination resources simplify the handling of fixed truck-trailer combinations in Transportation Management (TM), by using a

single road freight order that includes the assigned trailers as local items instead of separate trailer unit documents.

You can perform VSR optimization on the level of the combination resource. This means that VSR optimization does not have to

deal with the coupling and uncoupling of the individual components of the combination resource but can still do load planning on

the truck-trailer level. For more information about using combination resources in planning, see Use of Combination Resources.

## Activities

## Configuring Combination Resources

You configure a combination resource in Customizing for Transportation Management under  Master Data

## Resources

## General Settings

 Define Equipment Groups and Equipment Types .

When you configure a vehicle group as a combination resource you must:

Specify one truck vehicle resource.

Define a number sequence and assign the lowest sequence number to that truck.

## Creating Combination Resources

In master data for resources, you create a resource with the following settings:

This is custom documentation. For more information, please visit SAP Help Portal.

100


1/14/26, 2:16 PM

Setting

## Value

Description

Resource Type

09

Vehicle Resource

Resource Class

01

## Truck

You specify a vehicle group and vehicle type that have been configured for a combination resource in Customizing. This vehicle

group and vehicle type combination identifies the resource as a combination resource.

You can work with the combination resource on the Combination Resource tab and, for example, add an additional passive

resource such as a trailer.

## Restrictions

The following restrictions apply:

You must specify one truck resource.

You must define a number sequence, the lowest number of which you assign to the truck resource.

If you have previously defined a vehicle type as part of a means-of-transport combination, you cannot use that resource as

part of a combination resource. For more information see Definition of Means-of-Transport Combinations.

If you have defined a compartment profile for a vehicle resource, you cannot use that vehicle resource in a combination

resource. For more information see Definition of Compartments.

If a vehicle resource is defined as a combination resource, it cannot be used as a component in another combination

resource.

If a vehicle resource is used as a component of a combination resource, it cannot be used standalone during planning. If

you need the same vehicle to be planned both as part of a combination resource and standalone, you need to create two

separate vehicle resources.

Definition of Compartments

## Use

You use compartments to map the loading space of a vehicle.

## Features

You define compartments by using compartment types. For example, you use the compartment type to define the capacity of the

compartment, possible steps, and a compartment profile. In the compartment profile, you specify the number and type of

compartments that a means of transport can have. You then assign this compartment profile to the means of transport.

You can define a fixed number of compartments for each resource.

For each compartment, you can define a capacity for each dimension. The capacity consumption within a compartment is linear.

By defining steps, you can model a capacity consumption on the basis of the step. This is recommended if the compartment has a

door or if you want to work with movable partitions.

The relationship between the total capacity of the vehicle resource and the total capacity of all assigned compartments

determines whether the individual compartments are fixed or flexible. This is not an attribute of the compartment. A resource with

fixed compartments means that the total capacity of all assigned compartments is the same as the total capacity of the resource.

This is custom documentation. For more information, please visit SAP Help Portal.

101


1/14/26, 2:16 PM

A resource with flexible compartments means that the total capacity of all assigned compartments is greater than the total

capacity of the resource. For more information, see Examples of Compartments.

You can define incompatibilities for compartments based on attributes.

## Activities

You define compartment types in Customizing for Transportation Management under  Master Data

 Resources

## Define

Compartment Type .

## Example

You use compartments for the following:

You have to separate two freight units on a truck because they contain refrigerated goods and fruit.

You want to transport different types of gasoline in one tanker.

## More Information

Definition of Dimensions and Units of Measurement

Incompatibilities

Compartment

## Definition

Part of the loading space of a vehicle resource (vehicle or trailer).

## Use

You use compartments for the following, for example:

You have to separate two freight units on a truck because they contain refrigerated goods and fruit.

You want to transport diesel and super fuel in one tanker.

## Structure

You define compartments by using compartment types. You can define a fixed number of compartments per vehicle resource

(vehicle or trailer).

For each compartment, you can define a capacity per dimension. The capacity consumption within a compartment is linear. By

defining steps, you can model a capacity consumption on the basis of the step. This is recommended if the compartment has a

door, or if you want to work with movable partitions, for example.

The relationship between the total capacity of the vehicle resource and the total capacity of all assigned compartments

determines whether the individual compartments are fixed or flexible. This is not an attribute of the compartment. A vehicle

resource with fixed compartments means that the total capacity of all assigned compartments is the same as the total capacity of

This is custom documentation. For more information, please visit SAP Help Portal.

102


1/14/26, 2:16 PM

the vehicle resource. A vehicle resource with flexible compartments means that the total capacity of all assigned compartments is

greater than the total capacity of the vehicle resource. For more information, see Examples of Compartments .

The system takes into account compartments in VSR optimization and in manual planning in the Transportation Planning/Vehicle

Scheduling(TP/VS) component, as well as in SAP Transportation Management (SAP TM).

## Integration

You define compartment types in Customizing for SCM Basis. You use the compartment type to define the capacity of the

compartment, possible steps, and a compartment profile, for example. In the compartment profile, you specify the number

and type of compartments that a means of transport is to have. You then assign this compartment profile to the means of

transport.

For more information, see the Implementation Guide (IMG) for SCM Basis under  Master Data

 Trailers and

## Compartments

 Define Compartment Type.

To be able to work with compartments in TP/VS, you must set the Activate Comps indicator in Customizing for

Transportation Planning/Vehicle Scheduling (TP/VS).

For more information, see the IMG for TP/VS under  Trailers and Compartments

 Activate Trailers and Compartments

.

You have defined a number range for the handling unit Compartment Type in TP/VS.

For more information, see the IMG for TP/VS under  Basic Settings

 Define Number Range for HU Compartment Type

.

You have assigned packaging materials to means of transport and compartment types in TP/VS.

For more information, see the IMG for TP/VS under

## Interfaces

 Maintain Mapping Table for Vehicles/Compartment

Type  .

You can define compatibilities and incompatibilities for compartments.

Dynamic route determination in TP/VS does not support compartments. For more information, see SAP Library on SAP

Help Portal at  http://help.sap.com

 SAP Supply Chain Management (SAP SCM)

 SAP Advanced Planning and

Optimization (SAP APO)

## Transportation Management

 Transportation Planning/Vehicle Scheduling (TP/VS)

 Dynamic Route Determination  .

Examples of Compartments

## Fixed Compartments

This is custom documentation. For more information, please visit SAP Help Portal.

103


1/14/26, 2:16 PM

In this example, the vehicle resource comprises three compartments with the compartment type X. Each compartment has a

maximum capacity of 5 m   . The total capacity of the vehicle resource is 15m   .

3

3

Flexible Compartments (Without Steps)

In this example, the vehicle resource comprises two compartments with the compartment type X. Each compartment has a

maximum capacity of 10m   . The total capacity of the vehicle resource is 15m   , in other words, you are not allowed to load more

3

3

than 15m   onto the vehicle resource.

3

Flexible Compartments (with Steps)

This is custom documentation. For more information, please visit SAP Help Portal.

104


1/14/26, 2:16 PM

In this example, the vehicle resource comprises one compartment with the compartment type X. The compartment has a
3

maximum capacity of 15 m   . The total capacity of the vehicle resource is 15m   . The compartment has three steps (5 m   , 10 m   ,

3

3

3

and 15m   ).

3

This means the following for the compartment:

Zero consumption is not possible for the compartment. That means if you do not load this compartment, it still consumes a

capacity of 5m   .

3

Each load that is greater than or equal to 0 m   but less than or equal to 5m   results in a capacity consumption of 5m   .

3

3

3

3
That means if you load this compartment with 3m   , for example, it still consumes a capacity of 5m   .

3

Each load that is greater than 5 m   but less than or equal to 10m   results in a capacity consumption of 10m   .

3

3

3

3

3

3

Each load that is greater than 10 m   but less than or equal to 15m   results in a capacity consumption of 15m   .

  Note

In a realistic scenario, you would define a second compartment, for example, a flexible compartment without steps.

Flexible Compartments (Zero Consumption Is Not Possible)

This is custom documentation. For more information, please visit SAP Help Portal.

105


1/14/26, 2:16 PM

In this example, the vehicle resource comprises two compartments. Compartment 1 has compartment type X, compartment 2 has

compartment type Y. Each compartment has a maximum capacity of 10m   . The total capacity of the vehicle resource is 15m   .

3

3
Compartment 1 has a door and a step (5m   ). Compartment 2 does not have any steps.

This means the following for the two compartments:

Compartment 1:

Zero consumption is not possible for the compartment. That means if you do not load this compartment, it still consumes a

capacity of 5m   .

3

Each load that is greater than or equal to 0 m   but less than or equal to 5m   results in a capacity consumption of 5m   .

3

3

3

Each load x that is greater than 5 m   but less than or equal to 10m   results in a capacity consumption of x m   .

3

3

3

3

Compartment 2:

Each load xm   results in a capacity consumption of xm   (linear capacity consumption).

3

3

Flexible Compartments (Zero Consumption Is Possible)

Example 1

This is custom documentation. For more information, please visit SAP Help Portal.

106


1/14/26, 2:16 PM

In this example, the vehicle resource comprises two compartments. Compartment 1 has compartment type X and a maximum

capacity of 10m   . Compartment 2 has compartment type Y and a maximum capacity of 15m   . The total capacity of the vehicle
3

3
resource is 15m   . Compartment 1 has two steps (0m   and 5m   ). Compartment 2 does not have any steps.

3

3

3

This means the following for the two compartments:

Compartment 1:

Zero consumption is possible for the compartment. That means if you leave this compartment empty, it does not consume

any capacity.

Each load that is greater than 0 m   but less than or equal to 5m   results in a capacity consumption of 5m   . This

3

3

compartment might be a refrigerated part with a door, for example. As soon as you load one frozen pizza, you have to turn

on the refrigerated part. The second compartment has to start behind the door.

3

3

Each load x that is greater than 5 m   but less than or equal to 10m   results in a capacity consumption of x m   (due to the

3

3

maximum capacity).

Compartment 2:

Each load xm   results in a capacity consumption of xm   (linear capacity consumption).

3

3

Example 2

This is custom documentation. For more information, please visit SAP Help Portal.

107


1/14/26, 2:16 PM

In this example, the vehicle resource comprises two compartments. Compartment 1 has compartment type X and a maximum

capacity of 10m   . Compartment 2 has compartment type Y and a maximum capacity of 15m   . The total capacity of the vehicle
3

resource is 15m   . Compartment1 has four steps (0m   , 5m   , 8m   , and 10m   ). Compartment2 also has four steps (5m   , 7m   ,

3

3

3

3

3

3

3

3

3

10m   , and 15m   ). There are two doors.

3

This means the following for the two compartments:

Compartment 1:

Zero consumption is possible for the compartment.

Each load that is greater than 0 m   but less than or equal to 5m   results in a capacity consumption of 5m   .

Each load x that is greater than 5 m   but less than or equal to 8 m   results in a capacity consumption ofxm   (linear

capacity consumption since you have set the Linear indicator for this step).

Each load that is greater than 8 m   but less than or equal to 10m   results in a capacity consumption of 10m   .

3

3

3

Compartment 2:

3

3

3

3

3

3

3

3

Each load x that is greater than 0 m   but less than or equal to 5 m   results in a capacity consumption ofxm   (linear

3

capacity consumption since you have set the Linear indicator for this step).

This is custom documentation. For more information, please visit SAP Help Portal.

108


1/14/26, 2:16 PM

Each load that is greater than 5 m   but less than or equal to 7m   results in a capacity consumption of 7m   .

3

3

Each load x that is greater than 7 m   but less than or equal to 10 m   results in a capacity consumption ofxm   (linear

capacity consumption since you have set the Linear indicator for this step).

3

3

3

3

Each load that is greater than 10 m   but less than or equal to 15m   results in a capacity consumption of 15m   .

3

3

3

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

## Example

## Examples for Dimensions and Units of Measurement

The following table provides you with examples of dimensions and of some units of measurement you can assign to them.

## Dimension

Units of Measurement

Mass

## Volume

## Kilogram; milligram

## Cubic centimeter; cubic decimeter

## Example for the Conversion of Units of Measurement

This is custom documentation. For more information, please visit SAP Help Portal.

109


1/14/26, 2:16 PM

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

Handling Resource

## Definition

An installation or device that is used to handle the goods at one specific location. The handling resource offers handling capacity

that allows the goods to be loaded onto or unloaded from vehicle resources.

## Use

You use this business object to handle goods.

You can specify the capacity of handling resources based on shifts using the capacity profile.

  Example

You have 50 doors for loading and unloading freight units. In the morning and in the evening the full capacity is needed, in other

words, all doors are open. During the day, only 20 doors are needed, in other words, the capacity is reduced.

## Structure

You can define, among others, the following parameters for handling resources:

Resource template (see Copying Resources from Templates)

This is custom documentation. For more information, please visit SAP Help Portal.

110


1/14/26, 2:16 PM

Capacity profile (see Definition of Capacity Profiles)

Availability (see Definition of Availability)

Downtimes (see Definition of Downtimes)

Qualifications (see Definition of Qualifications)

Attached equipments (see Definition of Attached Equipment)

Grouping attributes (see Definition of Grouping Attributes)

Alternative names (see Definition of Alternative Names)

Example

Forklift

## Door

More Information

Vehicle Resource

## Driver

## Definition

A driver is any person who can operate vehicles and perform transportation-related tasks as a result of certain qualifications.

You specify a driver in TM business documents.

You can assign a default driver for a truck. If you have defined required qualifications for a vehicle resource, the system checks the

qualifications of the driver to ensure that the driver meets the required qualifications of the vehicle.

When you assign a vehicle to a freight order, the system checks the driver assignment. If no driver has previously been assigned to

the freight order the system assigns the vehicle’s default driver to the freight order.

## Structure

You can define the following parameters for drivers:

Availability (see Definition of Availability)

Absences (see Definition of Downtimes)

Qualifications (see Definition of Qualifications)

## Supply Chain Unit

Represents the driver's home location.

## Driver Type

You can define driver types to categorize drivers depending on the duties they perform and based on certain parameters

such as their qualification. You can define this parameter in the Customizing for Transportation Management under

This is custom documentation. For more information, please visit SAP Help Portal.

111


1/14/26, 2:16 PM

## Master Data

 Business Partners

 Define Driver Types .

Transportation Unit Resource

## Definition

An instance of a particular transportation unit like a container that you can use to map the capacity and availability that you want

to use for transportation.

You can choose up to eight dimensions and units of measurement to describe the capacity. Note that the mass and volume are

predefined by default. Planning can only take the transportation unit resource capacity into account if these correspond to the

dimensions and units of measurement that you have defined in a freight unit building rule.

  Note

You cannot define the available capacity for this resource type according to time. However, you can define a time-dependent

availability using shift sequences. For more information about defining shift sequences, see Specification of Definitions and

Creating Definitions.

In the planning profile, you can specify whether the system can consider a manual overload of the resource capacity.

## Equipment Group and Equipment Type

The equipment and equipment group types specify attributes such as the physical properties of a certain kind of transportation

unit resource. When you have created a transportation unit resource type you can:

Use the type as a template to create transportation unit resources, copying the attributes of the type to a new resource

Request a special type of transportation unit resource in a forwarding order or in a booking order

For more information see Customizing for Transport Management under  Transport Management

 Master Data

## Resources

 Define Equipment Groups and Equipment Types

## Structure

You can define, among others, the following parameters for transportation unit resource resources:

Capacity (see Definition of Capacity)

Availability (see Definition of Availability)

## Multiresource

For container resources, you can specify whether the resource is a single resource or a multiresource (see Use of

Multiresources).

## Minimum number of seals

You can specify the minimum number of seals of the transportation unit resource. You can use this information for the

definition of incompatibilities.

Resource template (see Copying Resources from Templates)

Physical properties (see Definition of Physical Properties)

Downtimes (see Definition of Downtimes)

This is custom documentation. For more information, please visit SAP Help Portal.

112


1/14/26, 2:16 PM

Qualifications (see Definition of Qualifications)

Attached equipment (see Definition of Attached Equipment)

Grouping attributes (see Definition of Grouping Attributes)

Alternative names (see Definition of Alternative Names)

## More Information

## Freight Unit Building Rule

Definition of Dimensions and Units of Measurement

Planning Profile

## Incompatibilities

Creating, Copying, and Deleting Resources

In the following sections you can find information about:

Creating handling, vehicle, calendar, and transportation unit resources (see Creating Handling, Vehicle, and Calendar

Resources)

Creating drivers (see Creating Drivers)

Copying resources (see Copying Resources)

Creating resources based on resource templates (see Copying Resources from Templates)

Deleting resources (see Deleting Resources)

Creating Handling, Vehicle, Calendar, and Transp. Unit Resources

## Prerequisites

You have specified a factory calendar in Customizing for Transportation Management under  Master Data

## Calendar

 Maintain Factory Calendar

.

If you want to create a vehicle resource, you have to have specified a means of transport in Customizing for TM under

Transportation Management

 Master Data

## Resources

 Define Means of Transport

.

## Context

This procedure describes how to create the following resource types:

Handling resource (see Handling Resource)

Vehicle resource (see Vehicle Resource)

Calendar resource (see Calendar Resource)

Transportation Unit resource (see Transportation Unit Resource)

This is custom documentation. For more information, please visit SAP Help Portal.

113


1/14/26, 2:16 PM
## Procedure

1. You have the following options:

On the SAP Easy Access screen, choose  Transportation Management

 Master Data

 Resources

## Define

Resource .

In the SAP launchpad, open the Define Resources app.

2. Choose the Create Resources pushbutton.

3. Select the tab page for the resource type for which you want to create a new resource.

  Note
You cannot change the resource type later.

4. For handling resources, specify the resource class, the time zone or location, and the factory calendar.

For calendar resources, specify the time zone or location, and the factory calendar.

For vehicle resources, specify the resource class, the time zone or depot location, the factory calendar, the means of

transport, the dimension, and the capacity.

For transportation unit resources, specify the resource class, the time zone or depot location, the factory calendar, the

dimension, and the capacity.

  Note
You can specify the depot location in the Location column.

For more information about resource classes, see Classification of Resources.

5. In addition, you can define other resource-specific information, such as downtimes, attached equipment, time-continuous

capacity, or qualifications.

## Next Steps

## Definition of Means of Transport

Definition of Dimensions and Units of Measurement

Definition of Capacity

Definition of Downtimes

Definition of Attached Equipment

Definition of Qualifications

Creating Drivers

## Prerequisites

You have defined a factory calendar in Customizing for Transportation Management under  Master Data

## Calendar

 Maintain Factory Calendar

.

This is custom documentation. For more information, please visit SAP Help Portal.

114


1/14/26, 2:16 PM

You have defined qualifications in Customizing for Transportation Management under  Master Data

## Resources

 Maintain Settings for Qualifications .

## Context

You use this procedure to create the driver business partner.

## Procedure

1. In transaction BP, you create a new business partner of the type Person and specify the BP role as Driver. The entry screen

changes and a new Driver tab page is displayed.

2. On the Driver tab page, you enter the attributes of the driver such as the labor factor and the supply chain unit (the home

location of the driver).

3. In the Qualifications screen area, you enter the qualifications that are held by the driver. This enables you to specify, for

example, the type of license that the driver has or whether the driver has any experience of transporting dangerous goods.
For more information, see Definition of Qualifications.

4. In the Availability screen area, you enter the availability of the driver by specifying the valid from and valid to dates and

times. You must also enter a factory calendar.

You can define a number of capacity variants and specify which of these variants is to be used as the active variant. Note

that TM does not evaluate the type of capacity (minimum, mean, or maximum capacity). For more information, see

Definition of Capacity Variants.

You can also enter planned absences such as vacation periods and unplanned absences such as sick leave in this area. For

more information, see Definition of Downtimes.

## Next Steps

For more information about business partners, see Definition of Business Partners.

Copying Resources

## Use

You use this procedure to create a copy of one or more resources of the following type:

Handling resource (see Handling Resource)

Calendar resource (see Calendar Resource)

Transportation Unit resource (see Transportation Unit Resource)

## Prerequisites

You have created a resource. For more information, see Creating Handling, Vehicle, and Calendar Resources.

## Procedure

1. In the SAP Easy Access screen, choose  Master Data

## Resources

 Define Resource , or from the launchpad open the

Define Resource app. Enter the resource you want to copy and choose the Change pushbutton. Select the resource you

want to copy, and choose the Copy Resources pushbutton.

This is custom documentation. For more information, please visit SAP Help Portal.

115


1/14/26, 2:16 PM

2. Choose the Copy Resources pushbutton.

3. In the Copy Resources dialog box, you can create one or more copies of a resource.

## Single copy

Choose the copy mode Copy Resources and in the To field group maintain the name of the copy, its location, and a

short description.

## Multiple copies

Choose the copy mode Make Multiple Copies of Resources. Enter the number with which you want the copied

resources to begin and the number of resources that you want to create. This number is added to the end of the

resource name as a value for counting.

  Example

Assume that the name of the resource that you want to copy is Res_00. If you choose 1 as the start number and

10 as the number of resources, the system creates the resource copies Res_001 to Res_0010.

If you have selected more than one resource in the Change Resources: Header Data screen, the system calls up the selected

resources consecutively in the Copy Resources screen.

## Result

You have created a copy of one or more resources. Each copy has its own name.

Copying Resources from Templates

## Prerequisites

You have created a resource for which you have selected the Resource Template checkbox on the Transportation tab page.

For more information about creating resources, see Creating Handling, Vehicle, and Calendar Resources.

For handling resources that you want to mark as resource templates, you have specified template types in Customizing for

Transportation Management under  Master Data

## Resources

 Specify Resource Template Types .

  Note

For vehicle resources, the template type is automatically Means of Transport.

## Context

This procedure describes how to create a copy of one or more resources of the following type from resource templates:

Handling resource (see Handling Resource)

Vehicle resource (see Vehicle Resource)

## Procedure

1. You have the following options:

This is custom documentation. For more information, please visit SAP Help Portal.

116


1/14/26, 2:16 PM

On the SAP Easy Access screen, choose  Logistics

 Transportation Management

 Master Data

## Resources

 Define Resource  and choose the Resources (Copy Resources from Template) pushbutton.

On the SAP Easy Access screen, choose  Logistics

 Transportation Management

 Master Data

## Resources

 Copy Resource from Template .

Open the Copy Resource from Template app from the launchpad.

2. In the Name of New Resource group box, you specify the data for the new resource that you want to create from the

resource template.

3. In the Choose Resource Template group box, you specify whether the resource template is one of the following:

## Vehicle Resource

By specifying a means of transport, the system displays a list with all vehicle resources marked as resource

templates that you have assigned this means of transport to.

## Handling Resource

By specifying a template type, the system displays a list with all handling resources marked as resource templates

that you have assigned this template type to.

If you want to specify the name of the resource to be copied directly, select the From other Resource checkbox, and specify

the name in the Resource Name field.

  Note

By selecting this checkbox, you can copy resources that have not been marked as templates or resources that cannot

be marked as templates (for example, calendar resources).

4. To copy the data from the existing resource to the new resource, choose the Resource (Copy Resource) pushbutton.

Deleting Resources

## Prerequisites

You can only delete resources that are not planned or used in other master data. For this reason, check for existing dependencies

on the SAP Easy Access screen by choosing  Logistics

 Transportation Management

 Master Data

 Where-used List

.

## Context

This procedure describes how to delete the following resource types:

Vehicle resources (see Vehicle Resources)

Handling resources (see Handling Resources)

Calendar resources (see Calendar Resources)

Transportation Unit resources (see Transportation Unit Resource)

## Procedure

1. In the SAP Easy Access screen or in the Define Resource app, which you open from the launchpad, choose  Master Data
 Define Resource . Enter the resource you want to delete and choose the Change pushbutton.

## Resources

2. Select the resource you want to delete and choose Delete Resource.

This is custom documentation. For more information, please visit SAP Help Portal.

117


1/14/26, 2:16 PM

If there are no dependencies, the system deletes the resource.

If the resource has dependencies, the system displays an error message. You must remove all of these dependencies before

you can delete the resource.

3. Choose Save to confirm deletion.

Definition of Capacity

## Use

You use this function to specify the capacity that is available at specific points in time for a resource.

## Features

You can define the following capacity categories:

## Standard available capacity

You specify this capacity in the header data when creating a new resource. This capacity does not take a multiple-shift

operation into account, in other words, this capacity is always the same.

The standard available capacity is limited only by the resource availability (see Definition of Availability).

## Time-continuous capacity

The time-continuous capacity takes a multiple-shift operation into account. A capacity variant is used to define this

capacity based on different shift programs. For more information, see Definition of Capacity Variants.

You can define data for the time-continuous capacity for vehicle resources, drivers, and calendar resources. For handling

resources, you define a capacity profile.

## Capacity profile

The capacity profile corresponds to the time-continuous capacity, but is only available for handling resources. For more

information, see Definition of Capacity Profiles.

Moreover, the capacity profile provides you with an overview of the available capacity based on the standard available

capacity, and the capacity derived from capacity variants.

  Note

In downtimes, only reduced capacity is available for handling resources, and no capacity is available for all other resources. For

more information, see Definition of Downtimes.

Definition of Capacity Variants

## Use

If you work in a multiple-shift operation and want to plan using shifts, you can use capacity variants to define different capacities

for one or more resources.

## Prerequisites

This is custom documentation. For more information, please visit SAP Help Portal.

118


1/14/26, 2:16 PM

You have specified capacity variants in Customizing for Transportation Management under  Master Data

 Resources

## Specify

Capacity Variants . You can also specify these capacity variants on the Transportation Resource Master screen by choosing

Current Settings

 Capacity Variants .

## Features

You can define shift sequences with shifts, breaks, and shift factors in a capacity variant. You define these data based on

definitions (see Specification of Definitions).

If you define a capacity variant as the active variant on the General Data tab page of a resource, the system uses the capacity

information from the capacity variant instead of the standard available capacity.

  Note

The system considers the data of a capacity variant only if you have defined it as an active variant.

You can use the capacity profile to gain an overview of the available capacity that is determined from the active capacity variant for

the validity period of the resource. For more information, see Definition of Capacity Profiles.

Specification of Definitions

## Use

You use this function to specify resource-independent and date-independent templates for defining the available capacities of the

capacity variants.

## Features

The definitions, their use, and their data are summarized in the following table.

Definition

Use

## Data

## Shift sequence

In the shift sequence, you define the daily shifts for any number of

consecutive days, for example, for a week. For each shift, you define

working and break times, the utilization rate, and the capacity (in the

case of handling resources).

You assign shift sequences to the time intervals of a capacity variant.

In each interval, the shift sequence is repeated periodically (for

example, every seven days). You also specify on which day of a shift

sequence an interval starts.

## Shift

You define shift data in a shift definition.

## Breaks

In a break pattern, you define the breaks for a shift.

## Day numbers

Zero to nine shifts per

day

Processing of shifts

that start or end on

non-workdays

## Shift

Start and end of the

shift

Break pattern

Shift factors

## Break pattern

This is custom documentation. For more information, please visit SAP Help Portal.

119


1/14/26, 2:16 PM

Definition

Use

## Data

## Shift factors

You define a shift factor to define the rate of resource utilization and

the capacity of a shift.

## Break number

Start and end of the

breaks

Relative start of the

break, in relation to the

start of the shift, and

the total break duration

Shift factor definition

## Validity

Rate of resource

utilization

Capacity for handling

resources

## Activities

For more information about creating definitions, see Creating Definitions.

To check whether a definition is used in resources, on the Display Definitions screen, choose

.

## Example

The following figure is an example of how you can use definitions to define the capacity of capacity variants for a resource.

This is custom documentation. For more information, please visit SAP Help Portal.

120


1/14/26, 2:16 PM

Capacity Variants for a Resource

## Creating Definitions

This is custom documentation. For more information, please visit SAP Help Portal.

121


1/14/26, 2:16 PM
## Prerequisites

You have created a resource. For more information, see Creating Handling, Vehicle, and Calendar Resources.

## Procedure

1. On the SAP Easy Access screen, choose  Transportation Management

 Master Data

## Resources

## Define Resource

or in the launchpad, open the Define Resource app.

2. You have the following options:

On the Resources screen, choose the Definitions pushbutton.

Choose the Change pushbutton. On the Change Resources: Header Data screen, choose the Definitions

pushbutton.

3. Choose the Breaks tab page.

4. Create the new break pattern, for example, lunch, and assign a break number (dependent on how many breaks you want to

define for the day).

There are two ways to define breaks:

You specify the start and end of the break.

You specify the number of hours after which you want the break to take place and enter the duration of the break.

The reference point is always the beginning of the shift.

If you want to define a recurrent break, for example, a break for every 2 hours, you must define a break for 2 hours, 4

hours, 6 hours, and so on after the shift begins (taking into account the duration of any previous breaks).

5. Choose the Shifts tab page.

6. Enter a description for the shift, a validity end, and a start and end for the shift. Assign your break pattern to this shift.

  Note

The system takes into account shift factors only for handling resources.

7. Choose the Shift Sequences tab page.

8. Enter a description, the day number, and the validity end. In the Non-Workdays field, you can choose from the following

options to define the start and end of the shift:

Can Finish on a Non-Workday

Can Start on a Non-Workday

Can Only Start or Finish on a Workday

Can Start or Finish on a Non-Workday

Creating Capacity Variants

## Prerequisites

You have created definitions (see Creating Definitions).

You have specified capacity variants in Customizing for Transportation Management under  Master Data

## Resources

 Specify Capacity Variants .

This is custom documentation. For more information, please visit SAP Help Portal.

122


1/14/26, 2:16 PM
## Context

You can use this procedure to combine capacity-relevant data such as different shifts and breaks in a capacity variant.

## Procedure

1. On the SAP Easy Access screen or on the launchpad, open the resource for which you have created definitions.

2. On the Change Resources: Header Data screen, choose the Capacity Variants pushbutton. To create a new variant, choose

Interval.

3. Enter a capacity variant and a validity period. Assign the shift sequence to the capacity variant. Select the first day so that

the first day of the time interval is the first day of the shift sequence.

  Example

You have defined a four-day shift sequence. If you enter2 as the first day, the first day of the time interval has the shifts

from the second day of the shift sequence.

The following ways exist for defining workdays:

Workdays according to the factory calendar

No workdays (overwrites the factory calendar)

Workdays (overwrites the factory calendar)

4. Save the interval and go back to the resource master data.

5. On the General Data tab page, assign the capacity variant to the resource by specifying its name in the Act Var. (Active

Variant) field.

Definition of Capacity Profiles

## Use

The capacity profile provides you with an overview of the available capacity of a handling resource per day from the current date to

the end of the resource’s validity period for the following capacities:

Standard available capacity

Capacity variants

## Prerequisites

If you want the capacities from capacity variants to be displayed in the capacity profile, you have to specify capacity variants for

handling resources. For more information, see Creating Capacity Variants.

## Features

You can manually change the standard available capacity for selected resources without having to define a new shift or a new

interval in the capacity variant if, for example, the working time or the rate of resource utilization varies for individual days. The

system saves these changes to the database in a capacity profile for the standard available capacity or for the selected capacity

variant.

If, for example, you change the standard available capacity by changing the shift the system adjusts all unchanged data in the

capacity profile. All variants entered manually are retained.

This is custom documentation. For more information, please visit SAP Help Portal.

123


1/14/26, 2:16 PM

As soon as a capacity profile for the standard capacity or for the capacity variant exists in the database, the system takes the

variants defined there into consideration - instead of the corresponding capacity – when determining the valid capacity.

  Note
Depending on the validity period defined for the resource and the number of shifts, the overview may contain a large number of

entries.

## Activities

## Displaying the Capacity Profile

By choosing Capacity Profile on the Display Resources: Header Data screen, you can call an overview of the standard available

capacity, and the available capacity generated from the capacity variants.

## Changing the Available Capacity of a Shift

If you want to change the available capacity of a shift, proceed as follows:

1. In the capacity profile, choose the  Shifts (Change Shifts) pushbutton.

A dialog box appears in which you can specify the period and shift for which you want to change the available capacity.

  Note

You can also mark the period on the calendar. The system then automatically marks the corresponding shifts in the

overview. The marked period is also shown in the dialog box.

2. Enter the changed capacity in the Available Capacity group box.

Determination of the Valid Available Capacity

## Use

This process describes how the system determines the valid available capacity of a resource.

For planning purposes, the system takes the following capacity categories into consideration in a hierarchical sequence to

determine the capacity that is available at a specific point in time at a resource:

1. Standard available capacity (taking the factory calendar into account)

2. Capacity profile (for handling resources) or time-continuous capacity (for all other resources)

## Process

The system checks the resource at the current point in time in the following sequence. If the result of the check is negative, the

system moves on to the next step:

1. If you have defined a downtime for the resource for the current point in time, only reduced capacity is available for handling

resources and no capacity is available for all other resources.

2. If you have specified an active capacity variant in the resource and different data is defined in a capacity profile for the

current date, the system uses the capacity defined in the capacity profile.

This is custom documentation. For more information, please visit SAP Help Portal.

124


1/14/26, 2:16 PM

3. If you have specified an active capacity variant for the resource, for which a capacity profile does not exist, and an interval

with a capacity that is valid at the current time is defined in this variant, the system uses this capacity.

4. If you have also created a capacity profile for the standard available capacity, the system uses the capacity defined in the

capacity profile.

5. The system only uses the standard available capacity if it could not determine a valid resource capacity for the current

point in time during one of the previous checks.

6. If you have not defined any standard available capacity for the resource, the resource does not have any capacity.

The following figure shows the process flow:

This is custom documentation. For more information, please visit SAP Help Portal.

125


1/14/26, 2:16 PM

## Determination of the Valid Available Capacity

This is custom documentation. For more information, please visit SAP Help Portal.

126


1/14/26, 2:16 PM

Definition of Availability

## Use

You use this function to specify general availability for the following resource types:

Vehicle resources (see Vehicle Resources)

Handling resources (see Handling Resources)

## Features

The actual availability of a resource within the general availability depends on the factory calendar, downtimes, and shift and break

definitions.

  Note

Planning takes into account only available resources.

## Activities

You can specify the general availability for vehicle resources or handling resources. On the launchpad open the Define Resources

app, or on the SAP Easy Access screen, choose  Master Data

## Resources

 Define Resource . Enter the resource you want to

edit and choose Change. Choose the Transportation tab page.

Definition of Downtimes

## Use

You use this function to specify downtimes, that is time segments in which resources are not available.

You can define downtimes for all resource types and for the Driver business partner.

## Prerequisites

You have created a resource. For more information, see Creating Handling, Vehicle, and Calendar Resources.

## Features

Downtimes override the availability of a resource. They exclude vehicle resources from planning. In the case of handling resources,

downtimes can reduce the available capacity (but a remaining available capacity of 0 also excludes a handling resource from

planning).

A differentiation is made between scheduled downtime (for example, for maintenance) and non-scheduled, unexpected downtime

(for example, due to a machine breakdown).

Downtimes differ from a regular, scheduled non-working time based on the factory calendar or the shift sequence (for example,

break or holiday).

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

127


1/14/26, 2:16 PM

Downtimes outside the validity period are not taken into consideration during planning. It is not useful to define downtimes that

are outside the validity period of the resource, since a capacity has not been defined for the resource for these times.

For a driver, you can specify absences and non-working times. Absences can represent sickness or vacation. Non-working times,

for example weekends or public holidays, are defined in the calendar. Scheduling considers both absences and non-working times.

Vehicle scheduling and routing (VSR) optimization interprets a downtime for a single resource in the following way:

The resource is not available for planning during the downtime.

The VSR optimizer needs to empty the resource, that is, the resource must be unloaded before a downtime.

The VSR optimizer needs to bring the resource to the location for which the downtime has been defined.

  Note

VSR optimization does not consider downtimes for multiresources.

VSR optimization and scheduling do not consider downtimes and availabilities (factory calendars and shift sequences)

for drivers, trailer resources, container resources, and railcar resources.

## Activities

You define a downtime for the resource that you have created on the Change Resources: Header Data screen by specifying on the

Downtimes tab page a start date/time and end date/time as well as the downtime type (scheduled or non-scheduled downtime).

In addition, you can enter a language-dependent short text that describes the downtime in more detail.

For Driver business partners, you define downtimes in the Absence screen area of the business partner master data.

## Example

A handling resource has a capacity of 5. Due to a reduced load, you specify a downtime to reduce the handling resource’s capacity

for a specific period of time to 2.

Definition of Qualifications

## Use

You use this function to specify qualifications, such as skills, capabilities, and permissions needed to operate vehicle resources and

handling resources.

## Prerequisites

You have created a resource. For more information, see Creating Handling, Vehicle, and Calendar Resources.

You have defined qualification types and qualifications in Customizing for Transportation Management under  Master

## Data

## Resources

 Maintain Settings for Qualifications .

## Features

This is custom documentation. For more information, please visit SAP Help Portal.

128


1/14/26, 2:16 PM

You can specify a validity period for a qualification, defining a start and end date within which the qualification is valid.

## Activities

You assign qualification types and qualifications in the resource master on the SAP Easy Access screen, or in the Resources app,

which you can open from the launchpad.

## Example

You have maintained the qualification type Driving License with qualification A (Heavy Vehicle).

If you assign qualification A (Heavy Vehicle) of type Driving License to a vehicle resource, it means that this resource can only be

operated with such a driving license.

Definition of Attached Equipment

## Use

You use this function to specify equipment that is attached (attached equipment) to the following resource types:

Vehicle resource (see Vehicle Resource)

Handling resource (see Handling Resource)

Transportation Unit resource (see Transportation Unit Resource)

## Prerequisites

You have created a resource. For more information, see Creating Handling, Vehicle, and Calendar Resources.

You have specified categories of attached equipment in Customizing for Transportation Management under  Master

## Data

## Resources

 Maintain Settings for Attached Equipment

.

## Activities

On the SAP Easy Access screen or in the Resources app, which you can open from the launchapad, you assign attached

equipment to the categories you have specified in Customizing on the Change Resources: Header Data screen by choosing the

Attached Equip. (Attached Equipment) tab page.

## Example

You have specified the following categories of attached equipment in Customizing:

FIREEXTINGUISHER

ON_BOARD_UNIT

## NAVIGATIONSYSTEM

A truck has the following attached equipment:

On-board unit (serial number 001-001-001)

This is custom documentation. For more information, please visit SAP Help Portal.

129


1/14/26, 2:16 PM

Fire extinguisher (serial number 001-001-0815)

Portable navigation system (serial number 010-101-010)

In the resource master, you assign the attached equipment to the categories of attached equipment:

Attached equipment 001-001-001 to category FIREEXTINGUISHER

Attached equipment 001-001-0815 to category ON_BOARD_UNIT

Attached equipment 010-101-010 to category NAVIGATIONSYSTEM

Definition of Physical Properties

## Use

You use this function to specify the capacity requirement of a vehicle resource or transportation unit resource during

transportation.

## Prerequisites

You have created a resource. For more information, see Creating Handling, Vehicle, and Calendar Resources.

If you want to use packaging materials as a template for the dimensions Volume and Weight, and for a dimensionless

capacity, you have to have defined packaging materials in the product master (see Product).

## Features

You can specify the capacity requirement with a unit of measure for multiple dimensions. For dimensionless capacities, you can

specify multiple values.

You can use a packaging material as template for the dimensions Volume and Weight, and for dimensionless capacity. If the

packaging material specifies values for volume, weight, or capacity the system automatically transfers these values into the

physical properties of the resource. Here, you can overwrite the values that have been transferred automatically.

## Activities

You specify or change the physical properties on the SAP Easy Access screen or or in the Define Resource app, which you open

from the launchpad. You choose on the Change Resources: Header Data screen the Phys. Properties (Physical Properties) tab

page.

## Example

To define how much volume a container needs on a ship, you specify physical properties for the dimension Volume.

Definition of Grouping Attributes

## Use

You use this function to group the following resource types into categories of grouping attributes:

This is custom documentation. For more information, please visit SAP Help Portal.

130


1/14/26, 2:16 PM

Vehicle resource (see Vehicle Resource)

Handling resource (see Handling Resource)

Transportation Unit resource (see Transportation Unit Resource)

## Prerequisites

You have created a resource. For more information, see Creating Handling, Vehicle, and Calendar Resources.

You have specified categories of grouping attributes and grouping attributes in Customizing for Transportation

Management under  Master Data

## Resources

 Maintain Settings for Grouping Attributes .

## Activities

On the SAP Easy Access screen or on the launchpad you assign resources to a grouping attribute category and one of its grouping

attributes on the Change Resources: Header Data screen by choosing the Grouping tab page.

## Example

You have specified the following:

Grouping attribute category Truck with the grouping attributes A, B, and C

Grouping attribute category Container with the grouping attributes C, CC, and CCC

Grouping attribute category Emissions Standard with the grouping attributes S1, S2, S3, S4, and S5

Now you can group resources into trucks, containers, or resources with a specific emissions standard.

Definition of Alternative Names

## Use

You use this function to specify alternative names for the following resource types:

Vehicle resource (see Vehicle Resource)

Handling resource (see Handling Resource)

Transportation Unit resource (see Transportation Unit Resource)

Alternative names only play a role for selecting and displaying resources.

## Prerequisites

You have created a resource. For more information, see Creating Handling, Vehicle, and Calendar Resources.

You have specified categories of alternative names in Customizing for Transportation Management under  Master Data

## Resources

 Specify Categories of Alternative Names .

## Activities

This is custom documentation. For more information, please visit SAP Help Portal.

131


1/14/26, 2:16 PM

On the SAP Easy Access screen or in the Resources app, which you open from the launchpad, you assign categories of alternative

names to resources and specify alternative names on the Change Resources: Header Data screen by choosing the Alternative

Names tab page. Note that an alternative name has to be unique within an alternative name category.

  Example

Resource 001000815 is a vehicle resource. For this resource, you have specified the alternative name TRUCK_007 for the

category OURCUSTOMERS_RES_1. No other resource can have this alternative name within this category.

Charge Management and Service Product Catalogs

## Use

You use Charge Management and Service Product Catalogs to set up the master data that the system uses to calculate

transportation charges, such as revenues, costs, and profits. Once the system calculates the charges, you can trigger invoice

creation and verification.

You can also include service products in forwarding agreements or service product catalogs. This enables you to specify services,

such as fumigation of a container and cargo insurance in a forwarding order.

## Integration

Charge Management and Service Product Catalogs is a component of Transportation Management (TM). The following TM

components are integrated with Charge Management and Service Product Catalogs because you can automatically calculate

transportation charges in these components on the basis of the data stored in Charge Management and Service Product Catalogs:

Forwarding Order Management

Freight Order Management

Forwarding Settlement

## Freight Settlement

Charge Management and Service Product Catalogs is integrated with the Agreement Management component because TM also

calculates transportation charges on the basis of the data stored in agreements. For more information, see Agreement

Management.

## Features

The system calculates transportation charges based on agreements (see Agreement) and the following master data in

Charge Management and Service Product Catalogs:

Calculation Sheet

Rate Table

## Scale

Note that your TM system can calculate transportation charges based on an agreement maintained in an external system.

For more information, see External Agreements.

You can use the master data cockpit to access an overview of the charge management master data per organizational unit,

business partner, and charge type. The system also shows the relationship between the different types of charge

This is custom documentation. For more information, please visit SAP Help Portal.

132


1/14/26, 2:16 PM

management master data. For more information, see Master Data Cockpit.

When resolving the calculation sheet or the local calculation sheet, the system also takes into account the following:

Relevant rates

Additional charges

## Other surcharges

Discounts for the selling (debit) as well as the buying (credit) side for all transportation modes such as trucking

(land transport), rail, sea, air, and inland vessel cargo (barge)

## More Information

Setup of MD for Charge Management and SP Catalogs

## Service Product Catalogs

Setup of MD for Charge Management and SP Catalogs

## Use

Charge Management and Service Product Catalogs uses agreements and master data to calculate transportation charges for a

forwarding order or freight order, and for transportation planning (see Planning).

You can also include service products in forwarding agreements or service product catalogs. This enables you to specify services,

such as fumigation of a container and cargo insurance in a forwarding order.

## Prerequisites

You have configured the prerequisites for the individual charge management master data objects as mentioned in the

prerequisites of the respective master data object.

You have configured the prerequisites for agreements (see Agreement Maintenance).

You have configured the prerequisites for service products (see Service Product Catalogs).

If you use Transportation Management (TM) for air freight transportation, you must make certain air-freight-specific

settings (see Charge Management Settings for Air Freight).

## Process

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

1. Optionally, you define the following charge calculation rules on the Maintain Charge Calculation Rules screen:

Agreement Determination Rules - Standalone

Agreement Determination Rules - Exclusion

Calc. Sheet Determination Rules - Standalone

## Calc. Sheet and Calc. Sheet Item Precondition Rule

This is custom documentation. For more information, please visit SAP Help Portal.

133


1/14/26, 2:16 PM

Grouping Rules for Resolution Base

## Rules for Rate Table Determination

Standalone means that the standard determination is switched off and the condition associated with the organizational

unit is used for the charge calculation. If you select the Std Determ. checkbox, the system uses the standard determination

if the standalone determination rule fails. Exclusion means that the standard determination is active and that constraint

and filter options are available. For more information, see Rules and Conditions for Charge Management and SP Catalogs.

2. Optionally, you define a condition with a condition type name starting with Charge Calculation (see Condition).

3. You create an agreement (see Agreement).

You can include service products in forwarding agreements or service product catalogs.

4. You create a calculation sheet (see Calculation Sheet).

5. You create a rate table definition and maintain rate values for defined validity periods (see Rate Table).

You then release the validity periods.

We recommend that you use calculation sheet templates and rate table templates to quickly define and maintain rates. We

recommend that you do not create one central rate table with rates for all your business partners.

6. You create a scale (see Scale).

  Note

You can create an agreement, calculation sheet, rate table, and scale from one consolidated user interface, starting with

creating the agreement. Once you create the agreement, you can create the following from within the agreement:

## A calculation sheet for each agreement item

A rate table from the Calculation Sheet tab page for each charge line in the calculation sheet

## A scale from the Rate tab page of the Calculation Sheet tab page

If you copy an agreement, the system copies the calculation sheets, rate tables, and scales that you created from within the

agreement or that you referenced in the agreement.

If you delete an agreement, the system deletes the calculation sheets, rate tables, and scales that you created from within the

agreement. However, the system does not delete the calculation sheets, rate tables, and scales that you referenced in the

agreement.

## More Information

Charge Management and Service Product Catalogs

## Charge Calculation

Charge Management Settings for Air Freight

## Use

The following is an overview of the charge management master data settings you should make if using Transportation

Management (TM) for air freight transportation.

This is custom documentation. For more information, please visit SAP Help Portal.

134


1/14/26, 2:16 PM
## Prerequisites

You have configured the prerequisites for the individual charge management master data objects as mentioned in the

prerequisites of the respective master data object.

## Customizing Settings

You can maintain charges grouped as other charges by the International Air Transport Association (IATA) in Customizing for

Transportation Management under  Basic Functions

 Charge Calculation

 Basic Settings

 Maintain IATA Other

Charge Codes .

You can define IATA locations and assigned them to IATA city codes in Customizing for Transportation Management under

## Master Data

 Transportation Network

## Location

 Define IATA Location Codes .

You can define IATA airline codes in Customizing for Transportation Management under  Master Data

 Business

## Partner

 Define IATA Airline Codes .

You can maintain IATA notes in Customizing for Transportation Management under  Basic Functions

## Charge

## Calculation

 Air Freight Settings

 Maintain IATA Notes .

You can define unit load device (ULD) rate types in Customizing for Transportation Management under  Basic Functions

 Charge Calculation

 Air Freight Settings

 Define ULD Rate Types .

You can map ULD types to ULD rate types in Customizing for Transportation Management under  Basic Functions

 Charge Calculation

## Air Freight Settings

 Map ULD Types to ULD Rate Types .

You can define IATA commodity codes in Customizing for Transportation Management under  Master Data

 Classification of Goods . For more information about commodity codes, see Classification of Goods.

You can define air-freight-specific charge types with the following attributes in Customizing for Transportation

Management under  Basic Functions

 Charge Calculation

 Basic Settings

 Define Charge Types :

## Charge type classification

In air freight, the transportation charges are broadly classified as follows:

Weight charges

Other charges

## Commission

Additional charges

## Valuation charges

You can classify charge types to represent this classification in the system. You can specify charge type

classifications for air freight in Customizing for Transportation Management under  Basic Functions

## Charge

Calculation

## Basic Settings

 Freight Term Settings for Transportation Modes

 Define Classifications for

Transportation Modes .

## IATA other charge code

Transportation mode category of Air

## IATA charge due of Due Agent or Due Carrier

If you classify the charge type as a Weight or Valuation charge, you specify the IATA charge due as being Due

Carrier. If you classify the charge type as an Other charge, you can specify the IATA charge due as being Due Agent

or Due Carrier, as appropriate. For example, although the printing of the air waybill is the responsibility of the

carrier, it can be carried out by the logistics service provider. To allow the system to charge the correct business

This is custom documentation. For more information, please visit SAP Help Portal.

135


1/14/26, 2:16 PM

partner for the printing, you define a printing charge type, classify it as Other, and then specify the IATA charge due

as being Due Agent.

You can specify air-freight-specific freight terms in Customizing for Transportation Management under  Basic Functions

 Charge Calculation

## Basic Settings

 Freight Term Settings for Transportation Modes

 Define Freight Terms for

Transportation Modes .

You can specify air-freight-specific pay definitions in Customizing for Transportation Management under  Basic

## Functions

 Charge Calculation

## Basic Settings

 Freight Term Settings for Transportation Modes

## Define Pay

Definitions for Transportation Modes .

## TACT Rate Upload

If you want to calculate air freight transportation charges based on TACT rates, you should upload TACT rates to TM (see TACT

Rate Upload). Note that you can calculate an air freight transportation charge based on TACT rates or contract rates, as

appropriate.

## Calculation Sheet Settings

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

For each calculation sheet line item, you can specify whether the system should use contract rates, which are available in standard

rate tables, or TACT rates to calculate air freight charges. If using a contract rate, you must specify a rate table, a rate table

determination rule, or an amount. If using a TACT rate, the system automatically determines the relevant TACT rate based on

mandatory parameters (see TACT Rates).

You must specify an air-freight-specific charge type for each relevant calculation sheet line item. The system automatically enters

the charge type classification, charge due, and IATA other charge code, depending on the charge type's Customizing settings. If

these settings are not specified in the charge type's Customizing settings, you can specify them directly in the calculation sheet.

For more information about calculation sheets, see Calculation Sheet.

## Rate Table Settings

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

If you specify an air-freight-specific charge type for a rate table, you must specify the rate category. Once you specify the rate

category, you can define the rate table as follows:

ULD

If you define a rate table as a ULD rate category, you must define a scale with a weight-based calculation base. With ULD

rate tables, you can maintain rates specific to ULD rate types or across ULD rate types for a particular airport pair.

If you define a scale with the ULD Rate Type calculation base, the system applies default values for the weight-based scale

items based on the ULD rate type. For example, the default rate values can be the minimum pivot weight (ULD charge code

/A or /B, indicating rate class U (ULD rate)) and the over-pivot weight (ULD charge code /C, indicating rate class E

(extension rate)) for each ULD rate type and airport pair combination. The scale item type for the minimum pivot weight

can be a To Scale and for the over-pivot weight can be a Base Scale. You define the minimum pivot weights (chargeable

weights) for ULD rate types in Customizing for Transportation Management under  Basic Functions

## Charge

## Calculation

## Air Freight Settings

 Define ULD Rate Types . You then map ULD types to ULD rate types in Customizing

for Transportation Management under  Basic Functions

 Charge Calculation

 Air Freight Settings

 Map ULD Types to

ULD Rate Types .

This is custom documentation. For more information, please visit SAP Help Portal.

136


1/14/26, 2:16 PM

If you do not define a scale with the ULD Rate Type calculation base, you can enter the minimum pivot weight as a scale

item. You specify the rate values for an airport pair.

When creating the scale items for weight-based scales in a ULD rate table, you can create multiple pivot weights for the

ULD rate types. You can then use different pivot weights when required, for example, for different origin and destination

location pairs, days of the week, or flight codes. When creating multiple pivot weights for ULD rate types, the system

creates two weight scale items with ULD charge code /A or /B and one with charge code /C. These scale items represent

the pivot and the over-pivot rates respectively. The scale value of the first pair of weight scale items defaults to the pivot

weight defined for the ULD rate type in Customizing for Transportation Management under  Basic Functions

## Charge

## Calculation

## Air Freight Settings

 Define ULD Rate Types . You must manually enter the scale value of subsequent

scale items.

  Note

If there is no scale in the rate table with the ULD Rate Type calculation base, you create multiple pivot weights using

asterisk (*) for the ULD rate type.

Specific commodity rate (SCR)

If you define a rate table as an SCR rate category, you must define a scale with the COMMODITY_CODE calculation base and

a commodity code type, and also a scale with a weight-based calculation base. The rate class S is associated with the scale

items of an SCR rate table.

## General cargo rate (GCR) – M, N, & Q

If you define a rate table as a GCR – M, N, & Q rate category, you must define a scale with a weight-based calculation base

and ensure that it is mandatory to maintain a minimum value for the calculated rate.

For more information about rate tables, see Rate.

## Scale Settings

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

A scale created from within a rate table automatically has the same transportation mode category as that of the charge type of the

rate table. If the transportation mode category is Air, then you can specify attributes for the scale items of a scale with the Weight

scale base (for example, ULD rate type, ULD charge code, and rate class).

In master data scale templates, the Items tab page displays the scale item attributes that are relevant for air freight.

For more information about scales, see Scale.

## More Information

Setup of MD for Charge Management and SP Catalogs

Service Product Catalogs

## Use

You can use a service product catalog to capture the services that you make available to your customer. A catalog acts as a

template from which your customer can pick and choose, according to their business needs.

This is custom documentation. For more information, please visit SAP Help Portal.

137


1/14/26, 2:16 PM

You can specify one or more of each of the following features:

## Services in a service product

## Service products in a service product catalog

Forwarding agreements created from one or more service products in a service product catalog

Forwarding orders or forwarding quotations created from forwarding agreements, or from the items and service products in

a forwarding agreement

In this way, individual services flow from the catalog to the agreement, and on to the order, to fulfill your customer’s needs.

For example, you can create services in the system for each of cleaning, fumigation, refrigeration, and cargo insurance. You can

create one service product for cleaning and fumigation, another for refrigeration, and another for cargo insurance.

You can then create a service product catalog for transporting perishable food that contains the three service products. You can

create an agreement directly from the service products in the catalog, and in turn create a forwarding order from the agreement.

## Prerequisites

If you want the system to automatically add services and service products when you create a catalog, you make the following

settings in Customizing:

1. Define service types in Customizing for Transportation Management under  Basic Functions

 General Settings

## Define

Service Types .

2. Specify preconditions and assign service types to item types in Customizing for Transportation Management under

## Master Data

 Agreements and Service Products

 Define FWA and Service Product Item Types .

3. Specify preconditions and assign item types to catalog types in Customizing for Transportation Management under

## Master Data

 Agreements and Service Products

 Define FWA and Service Product Catalog Types .

You can also assign a calculation sheet template to a service product catalog type. When you create a service product

catalog, the system uses the template to create a calculation sheet or a local calculation sheet. For more information, see

Agreement Maintenance.

If you do not make these settings, the system uses the default catalog type that you specify in the Define FWA and Service

Product Catalog Types Customizing activity to create a catalog.

You have assigned charge types to service types in Customizing for Transportation Management under  Basic Functions

 Charge Calculation

## Basic Settings

 Assign Charge Types to Service Types . The system uses these settings to assign

calculation sheets or local calculation sheets to service products or catalogs.

## Features

You can edit and delete the service product information in the following business documents:

Service product catalog

Forwarding agreement

## Forwarding order

You can create an agreement from one or more service products in a catalog. You can add service products to a standard

agreement that you have not created from a catalog. You can add service products from a particular catalog to a different catalog.

This is custom documentation. For more information, please visit SAP Help Portal.

138


1/14/26, 2:16 PM

  Note

In a service product catalog, you can add services to a service product. In forwarding documents you can add services to an

item. If you create a forwarding agreement from a service product, the system inserts the service product as an item in the

agreement.

If you deselect the Add Services checkbox in the Define FWA and Service Product Item Types Customizing activity, the system

creates a standard agreement line item. You cannot add services to these service products in the application. However, you can

add a service type. In this case, the system treats the service product as a single-service product. For example, you can use this

feature to provide insurance for an order.

The system adds the instructions that are assigned to the service product type in the Customizing activity Define Service Types. It

displays instructions in the Instructions tab page, on the forwarding agreement and forwarding order screens. You can create, edit,

and delete the instructions to suit your business needs.

For the service product catalog, the following features are available:

Output management (See Output Management)

## Notes

## Attachments

Notes and attachments features are also available for the individual service products in a service product catalog.

## More Information

## Management of Instructions

Creation of Forwarding Order Items or Forwarding Quotation Items

Condition

## Use

You use conditions to determine dependent values, for example, in the following areas:

## Filtering freight units

Determining freight unit building rules (FUB rules) (see Determination of Freight Unit Building Rules)

Incompatibilities (see Incompatibilities)

## Determining the sales organization

Determining rate tables and agreements with charge calculation rules (see Rules and Conditions for Charge Management

and SP Catalogs)

Change controller (see Change Controller)

## Features

You define input values for each condition. You can use the following to do so:

This is custom documentation. For more information, please visit SAP Help Portal.

139


1/14/26, 2:16 PM

Business object fields including user-specific fields

## Values determined in external determination classes

Input values that you have defined in the data crawler (see Use of Data Crawler Input Values)

The input values that are available each time depend on the condition type that was chosen. The condition type defines the area in

which the system is to take the condition into account. SAP delivers a number of condition types in the standard system.

The output values are determined by the condition type. For example, the FUB rule results from FUB rule determination.

The system generates a BRFplus decision table (BRFplus = Business Rule Framework plus) from input and output values. The

system then processes this table from top to bottom during determination. As soon as the system finds a row in the BRFplus

decision table whose input values match the current input values, it copies the corresponding output values and processes them in

the area that made the call. For more information about BRFplus, see Business Rule Framework plus (BRFplus).

## Activities

Open the Create Condition app on the launchpad to define conditions.

You can use the Transport pushbutton to transport your conditions.

You can use the Reset BRFplus pushbutton to reset data objects that you have changed in BRFplus.

More Information

## Definition of Conditions

Definition of a Condition for Time Windows

Rules and Conditions for Charge Management and SP Catalogs

## Use

You can use this function to define rules and conditions for the Charge Management and Service Product Catalogs component,

including agreement determination, with a single point of entry. You do this on theSAP Easy Access screen by choosing

## Logistics

 Transportation Management

## Master Data

 Maintain Charge Calculation Conditions .

You use these rules to distinguish between the following:

Whether the system calls a related Business Add-In (BAdI) to obtain the decision from enhanced coding

Whether the system calls BRFplus (Business Rule Framework plus) with the configured BRFplus function

## Integration

Each of the available rules has either a corresponding BAdI method in which you can hard code or delegate a decision or the link to

BRFplus in which the business decision can be executed.

## Prerequisites

This is custom documentation. For more information, please visit SAP Help Portal.

140


1/14/26, 2:16 PM

You have set up the BRFplus function in the system by setting up a condition. For information about setting up conditions, see

Definition of Conditions.

## Features

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

You can define rules for agreement determination. You have the following options:

Exclusion (standard determination): The system can check both the condition and the BAdI option to see if an

automatically determined agreement has to be considered for the given business context. The system checks the

list of automatically determined agreements one by one to determine if they are still applicable. If more than one

agreement remains after the system has applied the exclusion rule, the system considers the agreement priority.

Standalone: You have switched off standard determination, and instead, the system executes a condition that

determines the agreement. If you select the Std Determ. checkbox, the system uses the standard determination

logic if the condition execution fails or returns no result.

You can define rules for calculation sheet determination.

Standalone: You have switched off standard determination, and instead, the system executes a condition that determines

the calculation sheet. If you select the Std Determ. checkbox, the system uses the standard determination logic if the

condition execution fails or returns no result.

You can define a precondition rule for the calculation sheet and calculation sheet item.

You define a BRFplus condition or a BAdI to check if a certain calculation sheet or calculation sheet item is to be processed

in a certain business context. The result of this rule is a true/false decision, that is, if the response from BRFplus or the BAdI

is true, the calculation sheet or calculation sheet item is considered for charge calculation. For more information, see the

Precondition tab page in the Items screen area of the agreement or calculation sheet.

You can define grouping rules for resolution bases. You have the following options:

## Condition

The system can dynamically determine the attribute or field by which the data source is to be grouped. Both

options, the direct grouping and the dynamic BRFplus-based attribute determination, work in the same way – the

data source currently being processed (for example, all shipment items) is sorted by this specific attribute. The

system then groups all items with the same attribute value and later handles them as one item.

Group By

If you know the calculation base by which the data source is to be grouped and this value is static, you can enter the

calculation base directly. The system then groups all items with the same attribute value and later handles them as

one item when looking up the rate table. For more information about grouping and collective rates, see Calculation

Logic.

  Note

The target structures, into which the data to be grouped is cumulated, are limited in comparison to the original data

source as only certain attributes can be logically cumulated. Data that cannot be grouped is handled as a separate

record.

You can define rate table determination rules.

You use this rule to flexibly determine which rate table is to be used for the current charge item. This rule provides the

following options:

This is custom documentation. For more information, please visit SAP Help Portal.

141


1/14/26, 2:16 PM

## Condition

The flexible, rule-based determination of a specific rate table. To configure this determination, the complete

logistical data source is available. Only a valid rate table is expected as the return parameter.

Determin. By BAdI (Rate Table Determination Using BAdI)

The rate table determination is coded inside the BAdI.

You can define rules for charge calculation by a formula.

The system calculates the charge item without the normal rate table access. That is, either the BAdI or BRFplus directly

returns the calculated amount for this charge item.

  Note

If you decide to calculate the charge item through BRFplus, you can use a mathematical formula or any other BRFplus

option. In this case, no information is available in the Calculation Base area.

BRFplus for Charge Management and SP Catalogs

## Use

You can use this function in Charge Management and Service Product Catalogs to do the following:

Define specific business rules for various decisions within an automatic charge calculation process

Determine agreements as follows:

## Automatically by exclusion

## Independently of built-in next level principle

Influence if a certain calculation sheet, local calculation sheet, or a calculation sheet line item is calculated in a certain

business context or if the calculation is only applied for certain logistical data

Flexibly determine a rate during charge calculation

Use a formula to calculate transportation charges

## Features

## Linking of Charge Management and Service Product Catalogs and BRFplus

Charge Management and Service Product Catalogs and BRFplus (Business Rule Framework plus) are linked using rules. For

information, see Rules and Conditions for Charge Management and SP Catalogs.

Any use of BRFplus in the Charge Management and Service Product Catalogs component is encapsulated by rules. If you can

choose to use BRFplus, you can also use a Business Add-In (BAdI). With a BAdI, you can code a better-performing and simplified

decision logic.

## Data Source Supply for BRFplus

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

This is custom documentation. For more information, please visit SAP Help Portal.

142


1/14/26, 2:16 PM

In Transportation Management (TM), the conditions maintenance manages the data source binding by naming certain fields within

a certain business object. In Charge Management and Service Product Catalogs, you can either use the standard calculation bases

or any data element in the forwarding order (FWO) or freight order (FO) as the basis for BRFplus conditions. You can use all

available calculation bases for conditions. All available calculation bases are also available as data access definitions for

conditions. The name is the same, with the suffix _TCMC. Charge management conditions can only use these data access

definitions; other data access definitions will fail. For example, to define a condition based on source location you must use data

access definition SOURCELOC_TCMC, which is mapped to calculation base SOURCELOC.

The calculation bases are in the context of the current resolution base if available, or the document header. The freight agreement

and forwarding agreement determination rule and the calculation sheet precondition rule are executed on the header level. All

other rules are executed on a specific resolution base, as specified in the calculation sheet. In contrast, the system evaluates

calculation sheet line item precondition rules against the resolution base of the charge line. For example, a container type code

would depend on the resolution base container.

You can also use any data element in the FWO or FO as the data access definition if the data element is mapped to a field in the

communication structure. To do this, you create a BRFplus condition with a new criterion, for example, executing carrier, and then

assign the BRFplus condition to a determination rule. You then assign the determination rule to a calculation profile of the business

partner or the sales organization. During charge calculation, the system uses the determination rule in the calculation profile to

determine the appropriate charge management master data.

For BRFplus data supply, you have to name all attributes that are necessary for the specific business rule decision within the

conditions maintenance.

## More Information

Business Rule Framework plus (BRFplus)

Calculation Sheet and Local Calculation Sheet

## Definition

A calculation sheet or a local calculation sheet is a hierarchical table used to calculate transportation charges.

A calculation sheet or a local calculation sheet combines the charge types permitted for a document and the sequence in which

the system takes these charge types into account during the calculation.

## Use

The system uses calculation sheets or local calculation sheets to specify which transportation charges to calculate and how to

calculate them. This helps to bill customers for transportation services and to pay suppliers or carriers for subcontracted

transportation services. Calculation sheets (both kinds, including local) contain line items and each line item can result in a

calculated amount.

You can create calculation sheet templates on which to base calculation sheets or local calculation sheets. For more information

about master data templates, see Calculation Sheet Maintenance. For more information about Customizing templates, see

Customizing for Transportation Management under  Basic Functions

 Charge Calculation

 Basic Settings

## Templates

 Define Calculation Sheet Templates .

## Structure

This is custom documentation. For more information, please visit SAP Help Portal.

143


1/14/26, 2:16 PM

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

A calculation sheet can contain the following main tab pages and screen areas:

## General Data

The General Data tab page contains general information about the calculation sheet. For example, the archiving status and

whether you can use the calculation sheet to calculate charges billable to your customer, charges to be billed to you by your

carrier, or both.

## Items

The Items screen area contains the details of the calculation sheet line items and you can create rate tables for each line

item. You can insert blank line items one at a time or insert one or more line items with the charge type already specified.

You can also control the charge type that you enter, based on your Customizing. For more information see, Calculation

Sheet and Local Calculation Sheet Maintenance. The system also displays certain attributes that you do not need for

charge calculation, for your information.

The following columns are mandatory in the Items screen area:

## Instruction Type

If the instruction type is Line Item Selection, the Operation (Charge Item Operation) column is mandatory.

If the instruction type is Standard, the following columns are mandatory:

## Currency

If the currency is % and the calculation base is not amount–based, the Reference-From Line Number

column is mandatory.

If the currency is % and the calculation base is Customs Value, Goods Value, or Insurable Value, you can

specify a rate table for the line item. You do not need to specify a reference line item.

Rate Amount, Rate Table Det. Rule (Rate Table Determination Rule) or Rate Table

Charge Type

  Note

Each calculation sheet has an initial mandatory sum line, which you cannot delete. You can only maintain the rounding

rule for this line because you cannot define a charge type.

Depending on the type of calculation sheet item you select, the Items screen area contains some of the following main tab

pages:

## Basic Data

The Basic Data tab page contains information on each line item (charge item), including information that

determines how the system processes and calculates the transportation charges for each line item. On the Basic

Data tab page, the following important information is available for each line item:

## Dimensional weight profile

The dimensional weight profile the system uses to calculate the transportation charges for the line item. The

system uses the dimensional weight factor in the dimensional weight profile to convert a product's gross

volume into dimensional weight. The system then uses the dimensional weight to apply the correct rate.

Note that a dimensional weight profile at the line item level of a calculation sheet has priority over a

dimensional weight profile in an agreement. You define dimensional weight profiles in Customizing for

This is custom documentation. For more information, please visit SAP Help Portal.

144


1/14/26, 2:16 PM

Transportation Management under  Basic Functions

 Charge Calculation

## Data Source Binding

 Define Dimensional Weight Profiles .

## Calculation resolution base

During charge calculation, the system determines the calculation resolution base by the origin of the data

upon which the charge aspect is based. You can define the charge aspect in the resolution base objects, for

example, container, product, and stage.

## Resolution base grouping rule

The rule the system uses to group selected input data, for example, destination location, weight, and volume.

You use the grouping rule together with the resolution base to group charge lines by the calculation base

specified in the Group By field of the grouping rule.

  Example

A calculation sheet line item contains Package as the resolution base and has a grouping rule assigned to

it. The grouping rule is grouped by the Destination Location calculation base. There is a freight order with

2 packages with the same destination location. The system groups the gross weight of the 2 packages

and determines a rate for the cumulative weight. This rate is lower than the rate that the system would

have determined for each package.

## Calculation method

When accessing rates during charge calculation, the system applies the specified calculation method to

calculate the charges for the charge type. You define customer-specific calculation methods in Customizing

for Transportation Management under  Basic Functions

 Charge Calculation

 Enhancements to Charge

## Calculation Engine

 Define Calculation Methods .

## Rate

The Rate tab page contains details of the rate table for each standard charge item. You can also create scales for

each rate table. For more information about the Rate tab page, see Rate Table.

## Classification

The Classification tab page contains details on each charge item, such as whether the charge item is mandatory for

charge calculation and its charge category.

## Precondition

The Precondition tab page contains the precondition rule or BRFplus condition for each charge item. The

precondition rule determines if the system processes the charge item before charge calculation. This tab page also

displays the text from the Documentation tab page of the condition. For information about conditions, see

Condition.

This tab page also contains Trade Lanes, Services, and Partners tab pages.

## Cost Pull

You can use the Cost Pull tab page to specify the charge types for each charge item that you want to transfer from

the freight side to the forwarding side. The charge types contain the distributed costs from the freight side. If you do

not enter a charge type, the system transfers the distributed costs for all charge types in the relevant freight orders.

For more information, see Cost Pull.

You define charge types in Customizing for Transportation Management under  Basic Functions

## Charge

Calculation

 Basic Settings

 Define Charge Types .

## Incoterms

This is custom documentation. For more information, please visit SAP Help Portal.

145


1/14/26, 2:16 PM

The Incoterms tab page contains the Incoterms for each charge item. If the Incoterm that is specified for a charge

item matches the Incoterm that is specified in a forwarding order, the system adds the line item to the order. You

define the Incoterms in Customizing for Transportation Management under  Basic Functions

## Charge

Calculation

## Basic Settings

 Define Charge Types . You can change the Incoterms that you specify in

Customizing, on the Incoterms tab page.

## Related Calculation Bases

In a calculation sheet, if you enter a calculation rule based on a calculation base that has related calculation bases,

you can directly enter values for the related calculation bases on the Related Calculation Bases tab page. You

specify related calculation bases in Customizing for Transportation Management under  Basic Functions

 Charge Calculation

 Data Source Binding

 Define Calculation Bases .

## Freight Terms

The Freight Terms tab page contains the freight terms for each charge type, indicating that you want to capture

prepaid export charges and collect import charges in a single forwarding settlement document. For more

information, see Freight Terms in Forwarding Orders. Note that the Freight Terms tab page is only visible when the

calculation sheet can be used to calculate charges billable to your customer, that is, if the charge usage of the

calculation sheet is Customer, Customer and Service Provider, or All.

You define freight terms in Customizing for Transportation Management under  Basic Functions

## Charge

Calculation

## Basic Settings

 Freight Term Settings for Transportation Modes

 Define Freight Terms for

Transportation Modes .

## Change Documents

You can view all changes made to a calculation sheet on the Change Documents tab page or screen area. The changes are

listed by date and time. You view the details of the changes at header level by selecting the relevant row in the Transactions

screen area and at field level by selecting the relevant row in the Record Level Changes screen area. You must refresh the

calculation sheet to view recently-saved changes.

## Integration

A calculation sheet or a local calculation sheet is integrated with agreements, rate tables, local rate tables, scales, and local scales.

For more information, see Agreement, Rate Table, and Scale.

## More Information

## Calculation Sheet Maintenance

Rules and Conditions for Charge Management and SP Catalogs

## Charge Calculation

Setup of MD for Charge Management and SP Catalogs

Calculation Sheet and Local Calculation Sheet Maintenance

## Use

You create and maintain calculation sheets (both kinds, including local) as a step in the process to set up master data for charge

calculation.

This is custom documentation. For more information, please visit SAP Help Portal.

146


1/14/26, 2:16 PM
## Integration

Calculation sheet maintenance is a step in the process to set up master data in the Charge Management and Service Product

Catalogs component and is integrated with agreements, rate tables, local rate tables, scales, and local scales. For more

information, see Setup of MD for Charge Management and SP Catalogs.

You can use the master data cockpit to access an overview of the charge management master data per organizational unit,

business partner, and charge type. The system also shows the relationship between the different types of charge management

master data. For more information, see Master Data Cockpit.

## Prerequisites

You have defined number ranges in Customizing for Transportation Management under  Basic Functions

 Charge Calculation

## Basic Settings

## Number Range Intervals

 Assign No. Ranges to Calc. Sheets, Rate Tables, & Scales .

## Features

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

## Templates

You can use templates to create calculation sheets, calculation sheet line items, and preconditions.

You can define Customizing templates in Customizing for Transportation Management under  Basic Functions

## Charge

Calculation

 Basic Settings

## Templates

 Define Calculation Sheet Templates . You can transfer Customizing

templates across different TM systems.

You can define master data templates directly in Transportation Management (TM). To define a master data template for a

calculation sheet, open the Create Calculation Sheet Template app from the launchpad. If required, you can define a

master data template based on a Customizing template.

You can view and update all calculation sheet templates in the Calculation Sheet Templates personal object worklist.

You can also influence the creation of a calculation sheet from a master data calculation sheet template or a Customizing

calculation sheet template. For more information, see Customizing for Transportation Management under  Business

Add-Ins (BAdIs) for Transportation Management

## Master Data

## Calculation Sheets

## BAdI: Calculation Sheet Creation

from Templates  or BAdI: Mass Calculation Sheet Creation from Templates

## Rate tables and scales

You can create rate tables and scales from within a calculation sheet in the following ways:

Create a rate table for each calculation sheet line item in the Items screen area.

You can assign a rate table to multiple line items if you allow multiple charge types in the rate table. Note that you

can assign a calculation rule to each calculation sheet line item and so do not need to use a rate table. The

calculation rule is applicable for the amount and not for the rate table.

Create a scale for a rate by going to the rate table details in the Items screen area.

You can also copy and delete the rate tables and scales from within a calculation sheet. For more information, see Rate

Table and Scale.

  Note
If you copy a calculation sheet, the system copies the rate tables and scales that you created from within the calculation

sheet or that you referenced in the calculation sheet. If you delete a calculation sheet, the system deletes the rate tables

This is custom documentation. For more information, please visit SAP Help Portal.

147


1/14/26, 2:16 PM

and scales that you created from within the calculation sheet. However, the system does not delete the rate tables and

scales that you referenced in the calculation sheet.

You can edit local rate tables and scales independently of the calculation sheet they were created within. To enable this,

you select the Edit Loc. MD Objects (Edit Local Charge Management Master Data Objects) checkbox in Customizing for

Transportation Management under  Basic Functions

## General Settings

 Define General Settings for TM .

## Index rate tables for fuel surcharges

You can enter an index rate table when fuel surcharges change frequently, and where you have different fuel surcharges in

different zones in your country or region. You can use one of the following approaches to calculate your fuel surcharges:

Use an actual fuel surcharge rate from an index rate table that is valid on a particular date.

To enable this approach, in the line item of the calculation sheet, specify a standard rate table with a calculation

base of FSC, and an index rate table.

Determine an index for the fuel surcharge and apply the index to the amount or percent you specify in a line item of

a calculation sheet.

To enable this approach using amounts, specify a standard rate table or amount, the index rate table, and the index

base date.

To enable this approach using percentages, specify two line items in the calculation sheet. In the first line item, enter

the standard rate table. In the second line item, enter the percent you want to apply, the index rate table, the index

base date, and the reference-from line number for the first line item.

For both amounts and percentages, you must use the calculation method type Fuel Surcharge Calculation and the

calculation method FUEL_SURCHARGE.

## Air freight charges

You can specify attributes in a calculation sheet to facilitate the calculation of air freight charges, for example:

Rate type of Contract Rate or TACT Rate

Rate category of ULD, SCR, or GCR - M, N, & Q

## Charge type classification

IATA charge due of Due Agent or Due Carrier

## IATA other charge code

The system displays certain attributes that you do not need for charge calculation, for your information.

For more information, see Charge Management Settings for Air Freight.

## Calculation rules

You can assign a calculation rule to a calculation sheet line item using the Amount field, instead of assigning a rate table.

You can only assign one calculation rule to each calculation sheet line item and cannot assign both a calculation rule and a

rate table to a calculation sheet line item.

If the calculation base has an amount-based scale base, the line currency must be % and you do not need a reference-from

or reference-to line. During charge calculation, the system applies the percentage amount to the amount values, such as

goods value and insurable value.

## Flat rates, relative rates, or percentages

You can specify a flat rate (amount) for a calculation sheet line item by entering an amount and a valid currency. You can

specify that a calculation sheet line item is a percentage of another calculation sheet line item by entering a percentage

This is custom documentation. For more information, please visit SAP Help Portal.

148


1/14/26, 2:16 PM

value, % in the Currency field, and a reference line number. You can also have a relative rate for a calculation sheet line item

by specifying a calculation rule in the calculation sheet line item. However, you can specify only one calculation rule at the

line-item level.

## Minimum and maximum rate values

You can specify a minimum rate value and a maximum rate value for each calculation sheet line item with the Standard

instruction type. Note that in order to specify minimum and maximum rate values, you must maintain the calculation rule

for the calculation sheet line item. If the system calculates the charges to be lower than the minimum rate value or higher

than the maximum rate value, the system enters the minimum rate value or maximum rate value as the charge. Note that

the minimum rate value must be higher than zero and you cannot specify a minimum rate value or maximum rate value if

there is a rate table or rate determination rule attached to the calculation sheet line item.

## Zero rates

You can indicate that there is no charge for a calculation sheet line item by selecting the Zero Rate checkbox on the Rate

tab page for the line item.

## Charge types

You can assign a charge type to calculation sheets and rate tables and specify one or more leading charge types in a

calculation sheet. A charge type classifies a charge line, which plays an important role in how the system calculates the

transportation charges for the charge line. For more information, see Charge Types.

## Prepaid and collect charges in one settlement document

You can capture prepaid export charges and collect import charges in a single forwarding settlement document by inserting

a charge type with freight terms. For more information, see Freight Terms in Forwarding Orders.

## Determination preconditions

The system uses preconditions during calculation sheet determination, for example, shipping type, stage category,

transportation mode, and service level.

## Cost pull

You can transfer distributed costs from the freight side to the forwarding side, and use the costs as a basis for settling with

a customer or an internal organization. To transfer the result of a cost distribution from the freight side to the forwarding

side, in a calculation sheet you must specify Customer or Internal in the Charge Usage field. You use an instruction type of

Cost at the item level. The system automatically includes an internal charge calculation method type, and the cost pull

calculation method COST_PULL. You must specify a cost pull strategy, and in the Cost Pull tab page, you can specify the

charge types the system transfers to the forwarding side. For more information, see Cost Pull.

## Calculation date type

You can specify the calculation date type for each calculation sheet item. Based on the calculation date type you specify,

the system uses a date, such as system date, invoice date, or order date, to determine a rate from the rate table and

calculates the charges for each calculation sheet item.

## Charge relevance

You can specify whether a charge line must be included for charge calculation in the invoice, order, or both.

## Validity period

You can set a validity period for each calculation sheet line item so that the charge line is relevant only during that period.

## Mass update of calculation sheet amounts

You can use the Update Calculation Sheet Amounts function to change the charge item amount in one or more calculation

sheets at the same time. You can navigate to the function in one of the following ways:

This is custom documentation. For more information, please visit SAP Help Portal.

149


1/14/26, 2:16 PM

Open the Charge Management app from the launchpad. Choose the master data cockpit for the relevant agreement

type and enter your search criteria. In the personal object worklist result, select the line items that contain the

calculation sheets you want to update, and choose the Update Rates/Calculation Sheet Amounts button.

In transaction SE38, enter /SCMTMS/TCCS_MASS_UPDATE.

For more information, see Update Calculation Sheet Amounts.

## Calculation sheets in forwarding agreement quotation items

You can enable the system to calculate the contribution and the target contribution in the flat view profile of forwarding

agreement quotations by selecting the Cost checkbox for calculation sheet items. For more information, see Flat View.

## Activities

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

To create a calculation sheet for an agreement item in an agreement, on the launchpad choose the Edit Freight Agreement app,

the Edit Forwarding Agreement app, or the Edit Internal Agreement app.

To change a calculation sheet for an agreement item in an agreement, on the launchpad choose the Edit Freight Agreement app,

the Edit Forwarding Agreement app, or the Edit Internal Agreement app. Edit the calculation sheet on the Calculation Sheet tab

page of the Items screen area in the agreement.

To display or edit a calculation sheet separately from the agreement it was created within, on the launchpad choose the Edit

Calculation Sheet app.

To create or change a calculation sheet, on the launchpad choose the Create Calculation Sheet app or the Edit Calculation Sheet

app. A calculation sheet can be used in multiple agreements.

  Recommendation
Adhere to the following guidelines when creating a calculation sheet:

Line numbers must be greater than 10 because the system generates the first sum line as 10.

The sum line must have reference lines greater than itself.

A subtotal line must have reference lines less than itself.

A subtotal line inherits the resolution base from the sum parent line.

If you require a nested sum line, decide on the reference line numbers accordingly.

## Related Information

Calculation Sheet and Local Calculation Sheet

Update Calculation Sheet Amounts

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

150


1/14/26, 2:16 PM

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

You can use the /SCMTMS/TCCS_MASS_UPDATE program to change the charge item amount in one or more calculation sheets at

the same time.

You can increase or decrease the amount by a percentage or an amount. You can apply the change to all charge items contained in

the calculation sheets in your selection. You can also apply the change to absolute and relative charge items. A charge item is

relative if you have specified a calculation rule for the charge item in the relevant calculation sheet.

You can further refine your selection by specifying the following settings; the function updates only the calculation sheets that fit

the criteria you enter:

## Validity period

You must select an existing validity period. The system displays the valid-from date in the function.

## Charge type

You must enter a charge type that is used in the relevant calculation sheets.

You can update charge item amounts for forwarding, freight, and internal agreements from the master data cockpit.

To work with the master data cockpit, open the Charge Management app from the launchpad. Choose the master data cockpit for

the relevant agreement type and enter your search criteria. In the personal object worklist result, if you select a line item that

contains a calculation sheet only and choose the Update Rates/Calculation Sheet Amounts button, the system opens the Update

Calculation Sheet Amounts function. The system automatically includes the calculation sheet in the update criteria when you

open the function.

If you select a line item that contains both a rate table and a calculation sheet, the system opens the Update Rates function. If you

select a line item that contains a rate table and a different line item that contains only a calculation sheet, the system opens both

the Update Rates and Update Calculation Sheet Amounts functions on the same screen. The system automatically includes the

calculation sheet and rate table in the update criteria when you open the function. For more information, see Update Rates.

You can only update charge items that have an instruction type of Standard.

## Integration

The update of calculation sheet amounts is a function in calculation sheet maintenance. For more information, see Calculation

Sheet Maintenance.

## Prerequisites

You have specified the settings required for calculation sheet maintenance. For more information, see Calculation Sheet

Maintenance.

## Example

You want to update charge item amounts in a calculation sheet or a local calculation sheet. The following table describes the

charge item settings in the calculations sheet or the local calculation sheet:

Item Hierarchy

Instruction Type

Validity

Amount (USD)

Absolute/Relative

Basic rate

## Standard

01.01.2013 to 02.01.2013

100

## Absolute

This is custom documentation. For more information, please visit SAP Help Portal.

151


1/14/26, 2:16 PM

Item Hierarchy

Instruction Type

Validity

Amount (USD)

Absolute/Relative

Air freight charges

## Standard

02.01.2013 to 03.01.2013

150

Insurance fees

## Standard

03.01.2013 to 04.01.2013

250

Relative

## Relative

The following table describes your inputs to the function:

## Setting

Validity period

Attribute

## None

Percentage for absolute charge items

+10%

The system updates the basic rate charge item from USD 100 to USD 110. The system does not include the charge items for air

freight charges and insurance fees because these are relative charge items and you specified absolute charge items in the

function.

More Information

Master Data Cockpit

Charge Types

## Use

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

When setting up charge management master data, you use charge types in calculation sheets and rate tables to classify charge

lines. This classification plays an important role in how the system calculates the transportation charges for a charge line.

You can assign charge types to calculation sheet line items and to rate tables at header level or item level. Note that the system

assigns rate tables to a line item in a calculation sheet only if the charge types match.

You define charge types in Customizing for Transportation Management under  Basic Functions

 Charge Calculation

## Basic

## Settings

 Define Charge Types . The system validates the following when you define a charge type:

You can define an independent charge type only with Positive Value for Positive/Negative.

When you edit an independent charge type, you can't update the value of the field Positive/Negative to Negative Value or

Positive/Negative Value.

  Note

The system doesn't validate the charge type when you update any other attributes of a charge type, for example calculation

base or charge usage.

  Recommendation

This is custom documentation. For more information, please visit SAP Help Portal.

152


1/14/26, 2:16 PM

Group and categorize charge types by charge subcategory and charge category to help structure transportation charges. You

define charge categories and charge subcategories in Customizing for Transportation Management under  Basic Functions

 Charge Calculation

## Basic Settings

 Define Category Codes  and  Define Subcategory Codes .

## Charge Type Attributes

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

A charge type’s attributes define how the charge type affects the calculation of transportation charges for a charge line in a

calculation sheet. There are standard attributes, which apply for transportation charges for all transportation mode categories,

and also air-freight-specific attributes. For more information about charge type attributes, see the Customizing activity Define

Charge Types.

## Standard Attributes

You can specify standard attributes for a charge type, for example:

## Whether the charge line can have a positive or a negative value

Whether the charge line can be an absolute value (an actual amount) or a percentage value of another charge line

Note that if a charge line represents a percentage, then to calculate a chargeable amount, this charge line must refer to

another charge line or to a subtotal that produces an absolute value.

Whether the charge type is a leading charge type and so must have a value for the system to be able to calculate the

charges

The transportation mode category (road, rail, sea, or air) of the charge type

You can then use the charge type only in a calculation sheet that is associated with an agreement with the same

transportation mode category or with no transportation mode category.

The classification of the charge type for transportation mode categories

## The charge usage of the charge type

You can then use the charge type only in calculation sheets or rate tables with a compatible charge usage. If you don't

specify the charge usage, you can use the charge type in any calculation sheet or rate table. Note that you can use the

program Mass Update of Charge Types with Charge Usage (/SCMTMS/MASS_UPD_CHRG_TYP_USAG) in transaction

SE38 to update the charge usage of multiple charge types at once.

The charge type description in multiple languages

## The Incoterm for the charge type

If a forwarding order has the same Incoterm, the system includes a line item from a calculation sheet in the forwarding

order.

## The freight terms for the charge type

The freight terms indicate that you want to calculate prepaid export charges and collect import charges for a single

forwarding order. If a calculation sheet has a charge type with freight terms, the system adds a Freight Terms tab page to

the calculation sheet. For more information about freight terms, see Freight Terms in Forwarding Orders.

## Air Freight Attributes

This is custom documentation. For more information, please visit SAP Help Portal.

153


1/14/26, 2:16 PM

If you want to use the charge type for calculating air freight charges, you can also specify air-freight-specific attributes, for

example:

The classification of the charge type for the transportation mode category of Air as one of the following:

Weight

## Other

## Commission

Additional Charge

## Valuation

The charge code of the charge type for charges classified as Other Charges by the International Air Transport Association

(IATA).

The transportation mode category as Air.

Whether the charges are due to the agent or to the carrier.

For more information about air freight settings, see Charge Management Settings for Air Freight.

## Leading Charge Types

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

You can have one or more leading charge types in a calculation sheet. A leading charge type must have a value for the system to

consider the calculation sheet for charge calculation. If there are multiple calculation sheets available when calculating charges,

the system skips the calculation sheets without a leading charge type. The system also skips the calculation sheets if the leading

charge type doesn't have a rate. If there are no calculation sheets with a leading charge type with a rate, the system chooses a

calculation sheet randomly. Note that if there are multiple leading charge types in a calculation sheet, all the leading charge types

must have a rate defined for the system to consider the calculation sheet for charge calculation. For more information about

leading charge types and calculation sheet determination, see Agreement and Calculation Sheet Determination.

  Note

For the system to take the leading charge type into account when calculating charges, you must select the Evaluate All

Agreements checkbox in Customizing for Transportation Management under  Basic Functions

 Charge Calculation

## Basic

## Settings

 Define Charges Profiles . The system then skips the agreements that use calculation sheets without a leading

charge type or with a leading charge type that doesn't have a rate.

You can specify a charge type as a leading charge type in the Customizing activity Define Charge Types.

## Multiple Charge Types

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

You can allow multiple charge types in a rate table for the following reasons:

You want to avoid defining numerous similar rate tables.

You want to use the rate table for multiple calculation sheet line items.

This is custom documentation. For more information, please visit SAP Help Portal.

154


1/14/26, 2:16 PM

In this case, the charge type of the dimension in the rate table and calculation sheet line item must match.

  Note

If you allow multiple charge types, you must adhere to the following guidelines when defining the rate table:

One dimension must have the Multiple Charge Type (MULT_CHRG_TYP) calculation base.

All charge types must have the same value type (absolute, percentage, or decided when assigning the charge type).

## Related Information

Calculation Sheet and Local Calculation Sheet

Calculation Sheet and Local Calculation Sheet Maintenance

Rate Table and Local Rate Table

## Charge Calculation

## Validation of Charge Types in Agreement Management

When you add a new charge line to any calculation sheet or edit a charge line, the system validates the charge type of that charge

line.

The validation for the charge lines is applicable for the following agreement types:

Freight agreements

Internal agreements

## Forwarding agreements

Forwarding Agreement Quotation and Assignment

Freight Agreement RFQ Master

## Service Product Catalogue

The system validates the charge types in the charge lines of calculation sheets in the following scenarios:

Creating new agreements, agreement templates, and calculation sheet templates.

Copying agreements, agreement templates, and calculation sheet templates from the existing ones.

Adding a new charge type in calculation sheet items of existing agreements, agreement templates, and calculation sheet

templates.

  Note

You can't manually add the charge type Adjusted/Quoted Amount (ADJ) to a calculation sheet or agreement.

Modifying the existing charge type in calculation sheet items of agreements, agreement templates, and calculation sheet

templates.

The validation depends on the Disable Extended Check for Charge Types in Agrmt. Management checkbox. You can do that from

the Customizing for Transportation Management under  Basic Functions

## General Settings

 Define General Settings for TM

.

This is custom documentation. For more information, please visit SAP Help Portal.

155


1/14/26, 2:16 PM

When you've not selected the Disable Extended Check for Charge Types in Agrmt. Management checkbox, the system

validates the following when you insert a charge line item in a calculation sheet item:

For new calculation sheets, you can't insert charge line items that have the same charge type with the same

resolution base.

You also can't add a charge line item with independent charge type having Negative or Positive/Negative indicator.

For an existing calculation sheet, the system doesn't validate the charge line items until you modify them. However,

if you edit the charge types of the existing charge line items the system validates them for charge types and

corresponding resolution base as mentioned earlier.

  Note

If you edit any other attribute of existing charge line items, for example Currency or Amount, the system

doesn't validate the charge line item.

Sign indicator validation for independent charge types isn't applicable for charge lines with

Adjusted/Quoted Amount (ADJ) charge type.

Adjusted/Quoted Amount (ADJ) is a charge type which is proposed by the system during charge

calculation. This charge type is based on the proposal from the carrier and it represents the delta amount.

You can't manually add it to a calculation sheet or agreement.

When you've selected the Disable Extended Check for Charge Types in Agrmt. Management checkbox, the system

validates the calculation sheet items based on the company code and carrier of the freight agreement where the

calculation sheet is used. This validation is based on the combination of company codes and carriers in the Customizing

activity Enable Lean Services based Settlement Integration. You can do that from the Customizing of Transportation

Management under  Settlement

## Freight Settlement

  Integration for Settlement Posting

  Service Procurement -

Lean Services .

You use the Customizing activity Enable Lean Services based Settlement Integration to enable lean service-based

integration. In this case, the system only validates the calculation sheet items of those freight agreements where it finds

the combination. For more information, see Freight Settlement Integration using Lean Services.

  Note

If a calculation sheet isn't used in any freight agreement, the system doesn't validate the calculation sheet line item

even when you add a new charge line item or edit the charge types of the existing charge lines items.

The following table shows the scenarios and their impact of using the Disable Extended Check for Charge Types in Agrmt.

Management and company code and carrier combination in the Customizing activity Enable Lean Services based Settlement

Integration.

## Scenario

Status of Agreement

## Impact

When you don't select Disable Extended

## New

Check for Charge Types in Agrmt.

Management checkbox.

## Existing

The system validates all charge types when

you add them to the calculation sheet.

The system validates only the new charge

types that you add to the calculation sheet.

This is custom documentation. For more information, please visit SAP Help Portal.

156


1/14/26, 2:16 PM

## Scenario

Status of Agreement

## Impact

When you select Disable Extended Check

## New or Existing

The system doesn't validate any charge

for Charge Types in Agrmt. Management

checkbox but haven't added any carrier and

company code combination in the

Customizing activity Enable Lean Services

based Settlement Integration.

When you select Disable Extended Check

## New

for Charge Types in Agrmt. Management

checkbox and have also added carrier and

company code combinations in the

Customizing activity Enable Lean Services

based Settlement Integration.

Existing

type.

System validates all the charge types in the

agreement for the carrier and purchase

company code combinations that are there

in the Customizing activity Enable Lean

Services based Settlement Integration.

System validates only the newly added

charge types in an agreement for the carrier

and purchase company code combinations

that are there in the Customizing activity

Enable Lean Services based Settlement

Integration

## Examples

The following examples show the process of validation of calculation sheet items that are used in freight agreements, when you've

selected the Disable Extended Check for Charge Types in Agrmt. Management checkbox:

  Example

You've defined the following are the settings for the two charge types SF04 and FB00 in the Customizing activity Define

Charge Types:

## Charge Type

Independent Charge Type Positive/Negative

SF04

FB00

Yes

## Yes

## Positive

## Positive/Negative

You've created a freight agreement AGR1 with the carrier CARR1, purchasing organization PUR1, and the following local

calculation sheet:

Calculation Sheet Item No. Charge Type

Resolution Base

Amount

10

20

SF04

FB00

ROOT

ROOT

15

25

You've also defined the following combination of carrier and company code in the Customizing activity Enable Lean Services

based Settlement Integration:

## Carrier

Company Code

CARR1

*

Now, you add a new calculation sheet item 30 to the local calculation sheet for the freight agreement AGR1:

This is custom documentation. For more information, please visit SAP Help Portal.

157


1/14/26, 2:16 PM

Calculation Sheet Item No. Charge Type

Resolution Base

Amount

10

20

30

SF04

FB00

FB00

ROOT

ROOT

ROOT

15

25

20

As you've checked the Disable Extended Check for Charge Types in Agrmt. Management checkbox in Customizing, and also

specified the combination of carrier and company code in the Customizing activity Enable Lean Services based Settlement

Integration, the system doesn't validate the existing calculation sheet item numbers 10 and 20, but validates only the newly

added calculation sheet item number 30. As the charge type FB00 is an independent charge with a Positive/Negative

indicator, the system doesn't save the freight agreement.

  Example

You've defined the following the two charge types SF04 and FB00 in the Customizing activity Define Charge Types:

## Charge Type

Independent Charge Type Positive/Negative

SF04

FB00

Yes

## Yes

## Positive

## Positive/Negative

You've also defined the following calculation sheet GS1:

Calculation Sheet Item No. Charge Type

Resolution Base

Amount

10

20

SF04

FB00

ROOT

ROOT

15

25

The calculation sheet GS1 is used in the following two freight agreements:

Agreement Carrier

AGR1

CARR1

AGR2

CARR2

You've also defined the following combination of carrier and company code in the Customizing activity Enable Lean Services

based Settlement Integration:

## Carrier

Company Code

CARR1

*

You add a new calculation sheet item to the calculation sheet GS1:

Calculation Sheet Item No. Charge Type

Resolution Base

Amount

10

20

SF04

FB00

ROOT

ROOT

15

25

This is custom documentation. For more information, please visit SAP Help Portal.

158


1/14/26, 2:16 PM

Calculation Sheet Item No. Charge Type

Resolution Base

Amount

30

FB00

ROOT

20

As you've selected the Disable Extended Check for Charge Types in Agrmt. Management checkbox in Customizing, the

system searches for all the freight agreements where GS1 is used. In this case, it's AGR1 and AGR2. The system then checks the

entries in the Customizing activity Enable Lean Services based Settlement Integration for any combination of company code

and carrier (CARR1). It also checks the agreements where CARR1 is used, which is AGR1. Then the system finally validates the

charge type in GS1 for the newly added calculation sheet item, line number 30. As the charge type FB00 is an Independent

charge with a Positive/Negative indicator, the system doesn't save the calculation sheet.

## Related Information

Handling Calculated Charges in Lean Services

Basic Settings for Tendering

Rate Table and Local Rate Table

## Definition

A rate table or a local rate table is a grouping of prices for transportation services. The prices (or rates) are listed by validity period

in the rate table. You can maintain up to 14 dimensions in a rate table or a local rate table.

## Use

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

You can define the scales and validities of the rate table. Once you define the rate table, you can maintain the rate values in the rate

table. For more information, see Rate Definition and Maintenance.

You can define a rate table manually or automatically by using a rate table template with predefined scales and validity dates. For

more information about master data templates, see Rate Definition and Maintenance. For more information about Customizing

templates, see Customizing for Transportation Management under  Basic Functions

 Charge Calculation

 Basic Settings

## Templates

 Define Rate Table Templates .

You can use the standard, break-weight, or clipping calculation method for a rate. The break-weight calculation method compares

and selects the lower rate from either the actual rate range or the lower end of the next rate range. It assumes that one of the

scales in the rate is the weight. The clipping calculation method considers all scales, even if the value lies outside of a scale. With

clipping, the system works through the pricing scale level-by-level. The calculation results from each scale level are then added up

to produce the overall result.

## Structure

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

A rate table can contain the following main tab pages and screen areas:

## General Data

This is custom documentation. For more information, please visit SAP Help Portal.

159


1/14/26, 2:16 PM

The General Data tab page contains general information about the rate table, for example, whether you can use the rate

table to calculate charges billable to your customer, charges to be billed to you by your carrier, or both. On this tab page,

you can also indicate how the system uses the rate table to calculate transportation charges, and whether you can use an

absolute value or a percentage value.

This tab page also displays scales. You can copy a scale into the rate table to create dimensions local to the rate table.

However, you cannot directly reuse a scale in the rate table. You can also create new scales for the rate table, with or

without a scale template. The following columns can be mandatory:

Calculation Base (always mandatory)

If the calculation base is amount-based, then the Scale Currency column is mandatory.

If the calculation base is not amount-based, then the Scale Unit of Measure column is mandatory.

Calculation Type (always mandatory)

Scale Type (conditionally mandatory)

If the calculation type of the calculation base is Relative, then the Scale Type column is mandatory.

Scale Type and Scale Unit of Measure (conditionally mandatory)

If the scale base is numeric, then the Scale Type and Scale Unit of Measure columns are mandatory.

For more information, see Scale.

The Details tab page contains the scale details.

## Dates and Values

The Dates and Values tab page contains general information about each rate, such as its validity period, the status of the

validity period, and the currency. The Valid From, Valid To, and Currency columns are mandatory on this tab page.

On the Dates and Values tab page, you can display the information in different ways and perform certain actions,

depending on the details already in the rate table, for example:

You can generate incremental scale items if the rate table contains a numeric scale that does not contain any scale

items.

You can choose which rates to display, that is, all rate combinations or only rates that were maintained, if the rate

table contains a scale item.

You can select which scale to use as the dimension column if the rate table contains a numeric scale and more than

one scale.

You can display the description of a rate, delete a rate, copy a rate, and freeze the columns in the Rate table if the

rate table contains a scale item.

If you open the rate table in display mode, you can choose to show archived validity periods. Note that you cannot change

to edit mode when showing archived validity periods. For more information about archived rate tables, see Archiving Rate

Tables (TM-MD-CM-RA).

You can also filter the rates that you want the system to display.

This tab page contains Rates, Calculation Rules, and Scale Items tab pages. On the Scale Items tab page, you can add and

maintain scale items and specify the actual base or factor with which the system calculates the charges for the scale. On

the Calculation Rules tab page, you determine the values with which the single rate is to be multiplied. If there is more than

one calculation rule, the system multiplies the determined rate with each of the given entries and totals the final amount

during charge calculation. If the scale items are relative, then the system applies the calculation rules. On this tab page, you

can also specify the level at which the system applies the calculation rule in the rate table, for example, at rate-table or

scale-item level.

This is custom documentation. For more information, please visit SAP Help Portal.

160


1/14/26, 2:16 PM

  Note

If you specify that the system applies the calculation rule at the Rate Table level, the Price Unit column on the

Calculation Rules tab page is mandatory. You must specify the level as Scale Item if the price unit of one of the scale

items is not the same as the others. In this case, you must specify the price unit on the Scale Items tab page for the

corresponding scale. The system applies the calculation rule only when the calculation type of the scale item for the

selected rate is relative.

Calculation rules and scale items are validity-dependent, meaning you can have different calculation rules and scale

items for each validity period listed in the rate table.

## Excel Integration

On the Excel Integration tab page, you can upload and download Microsoft Excel sheets to speed up the maintenance of

large rate tables. For more information, see Creation and Maintenance of Rate Tables Using Microsoft Excel.

## Change Documents

You can view all changes made to a rate table on the Change Documents tab page or screen area. The changes are listed by

date and time. You view the details of the changes at header level by selecting the relevant row in the Transactions screen

area and at field level by selecting the relevant row in the Record Level Changes screen area. You must refresh the rate

table to view recently-saved changes.

  Note

You can activate the Change Documents tab page or screen area in Customizing for Transportation Management

under  Master Data

## Rate Tables

 Define Rate Table Types .

## Integration

A rate table or a local rate table is integrated with agreements, calculation sheets, local calculation sheets, scales, and local scales.

For more information, see Agreement, Calculation Sheet, and Scale.

More Information

## Charge Calculation

Setup of MD for Charge Management and SP Catalogs

## TACT Rates

## Rate Definition and Maintenance

You define rate tables (both kinds, including local) and maintain rates as a prerequisite for charge calculation. If the rates for each

charge item aren't fixed or are calculated using a Business Add-In (BAdI) or BRFplus (Business Rule Framework plus), charge

calculation requires rates for every object in Transportation Management (TM), such as a forwarding order or freight order.

## Use

You can define and maintain rates directly in TM or upload and download them from Microsoft Excel or a similar XML-enabled

Application Programming Interface (API). Once you define the rate table or the local rate table, you can then maintain the rate

values in the rate table or the local rate table respectively. For more information, see Rate Table.

This is custom documentation. For more information, please visit SAP Help Portal.

161


1/14/26, 2:16 PM

  Recommendation

Use rate table templates to quickly define and maintain rates in rate tables or local rate tables. We recommend that you don't

create one central rate table with rates for all your business partners.

  Note

You can use TACT rates for calculating air freight charges (see TACT Rates).

## Integration

Rate maintenance is a step in the process to set up master data in the Charge Management and Service Product Catalogs

component and is integrated with agreements, calculation sheets, local calculation sheets, scales, and local scales. For more

information, see Setup of MD for Charge Management and SP Catalogs.

The system determines the most appropriate rate when calculating transportation charges, based on certain criteria and

attributes. For more information, see Rate Determination.

You can use the master data cockpit to access an overview of the charge management master data per organizational unit,

business partner, and charge type. The system also shows the relationship between the different types of charge management

master data. For more information, see Master Data Cockpit.

## Prerequisites

You've made the following settings in Customizing for Transportation Management under  Basic Functions

## Charge

Calculation :

Data Source Binding

 Define Calculation Bases

Data Source Binding

 Define Resolution Bases

## Basic Settings

## Number Range Intervals

## Assign No. Ranges to Calc. Sheets, Rate Tables, & Scales

You've defined rate tables types for rate tables and local rate tables in Customizing for Transportation Managements

under  Master Data

## Rate Tables

 Define Rate Table Types .

## Features

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

## Templates

You can use templates to create rate tables with predefined scales, organizational data, calculation rules, and validity

periods.

You can define Customizing templates in Customizing for Transportation Management under  Basic Functions

## Charge

Calculation

 Basic Settings

## Templates

 Define Rate Table Templates . You can transfer Customizing templates

across different TM systems.

You can define master data templates directly in TM. To define a master data template for a rate table, open the Create

Rate Table Template app from the launchpad. If needed, you can define a master data template based on a Customizing

template.

You can view and update all rate table templates in the Rate Table Templates personal object worklist.

This is custom documentation. For more information, please visit SAP Help Portal.

162


1/14/26, 2:16 PM

## Creation and maintenance of rate tables using Microsoft Excel

You can create multiple rate tables in Microsoft Excel using rate table templates and upload them to TM.

You can maintain a large rate table, with or without scale items, using Microsoft Excel. You can enter the rates and scales

into a Microsoft Excel file and upload the file to TM. Alternatively, you can define an empty rate table with validity periods in

TM and download it to Microsoft Excel. You can then maintain the rate table in the Microsoft Excel file and upload it to TM.

You can also choose to download rate tables in the background and be notified by e-mail when the download to the

application server path is complete (see Background Download of Rate Tables).

For more information, see Creation and Maintenance of Rate Tables Using Microsoft Excel.

## Update of rates

You can use the Update Rates function to change the rate values in a single rate table or in multiple rate tables at the same

time. You can navigate to the function in one of the following ways:

Open the Charge Management app from the launchpad. Choose the master data cockpit for the relevant agreement

type and enter your search criteria. In the personal object worklist result, select a line item that contains the rate

tables you want to update, and choose the Update Rates/Calculation Sheet Amounts button.

In the Maintain Rate Table app, open the rate table and choose the Update Rates button.

In transaction SE38, enter /SCMTMS/RATE_MASS_UPDATE.

For more information, see Update Rates.

## Approval workflow

You can enable an approval workflow when you create or change validity periods in rate tables.

You can specify that you want the system to notify the approver when you request approval for a new or changed validity

period. You can also specify whether you can edit rate tables that contain the validity periods during the approval workflow.

Note that the approver is the person assigned to the position that is the head of the organizational unit. Therefore, at least

one organizational unit must have a position that is the head of the organizational unit. For more information, see Approval

Check.

The approver uses Business Workplace to approve or reject the new or changed validity period. For more information, see

SAP Library for SAP Business Workflow on SAP Help Portal at http://help.sap.com/netweaver

. In SAP Library, choose

SAP NetWeaver 7.3

 Application Help

 Function-Oriented View

 Application Server

 Application Server ABAP

## Other

## Services

 Services for Application Developers

 SAP Business Workflow

 Reference Documentation .

  Note

You enable the approval workflow and allow the rate tables that contain the validity periods to be edited during the

approval workflow when you define rate table types in Customizing for Transportation Management under  Master

## Data

 Rate Tables .

## Offline approval workflow

TM can send work items for validity periods in rate tables by e-mail to the Microsoft Outlook inbox of a user, such as a

customer agent. The user can accept or reject a work item and update the system from their inbox.

For more information, see Offline Workflow for Sending and Approving Work Items.

## Rate table filter

On the Date and Values tab page, you can filter the rates that you want the system to display. In each rate table, you can

also create filter variants and select a default filter variant.

This is custom documentation. For more information, please visit SAP Help Portal.

163


1/14/26, 2:16 PM

When opening a rate table, the system can recommend that you use the rate table filter based on the number of rate table

entries in the rate table. For larger rate tables, the use of the rate table filter can improve system performance.

You can activate the rate table filter and specify the maximum number of rate table entries that you want the system to

display before recommending the use of the rate table filter. You can make these settings in Customizing for Transportation

Management under  Basic Functions

## General Settings

 Define General Settings for TM .

## Validity periods

When adding a new validity period to a rate table, you can choose whether you want the system to copy the scale items

from the existing validity period for the latest time period. The system doesn't copy the rates, just the scale items. If you

choose not to copy the scale items, scale items aren't copied into the validity period.

  Example

You have the following validity periods in a rate table:

Valid From Valid To

01.01.12

01.06.12

01.01.12

31.12.12

02.06.12

01.10.12

You decide to add a new validity period with scale items included. The system inserts the new validity period with the

same scale items as the validity period 01.01.12 to 31.12.12.

You release validity periods so that the rate values can be used for charge calculation.

## Rate-level validity periods

You can specify validity periods at rate level within the validity period of the parent validity period. You can also change rates

on a short-term basis without needing to update all the rates of the parent validity period. For more information, see Rate-

Level Validity Periods.

## Multiple charge types

You can allow multiple charge types in a rate table if you want to avoid defining numerous similar rate tables or if you want

to use the rate table for multiple calculation sheet line items. For more information, see Charge Types.

## Rate categories

You can specify the rate category of a rate table to facilitate the calculation of air freight charges. The rate categories

available are:

Unit load device (ULD)

Specific commodity rate (SCR)

## General cargo rate (GCR) – M, N, & Q

For more information, see Rate Categories and Charge Management Settings for Air Freight.

## Zero rates

You can enter a zero rate in a rate table to indicate that there's no charge. The system confirms that you entered a rate and

that the rate is zero by selecting the Zero Rate checkbox.

## Scales

This is custom documentation. For more information, please visit SAP Help Portal.

164


1/14/26, 2:16 PM

You can create scales on the Scales tab page of a rate table, for example:

You can enter a calculation base, scale type, and unit of measure.

You can enter a scale template.

You can specify different currencies at the level of individual rate values by selecting the Scale Rel. for Crcy Maint.

(Scale Relevant for Currency Maintenance) checkbox. Selecting the checkbox adds a currency column in the rate

table and you can maintain the currency against the respective scales for the rate values. The combination of scales,

currencies, and rates that you select is unique.

  Note
You can see only one currency column even if you select the Scale Rel. for Crcy Maint. checkbox for all the

scales, whether the scales are relative or absolute.

The system creates the scale when you choose the Create Scale button. You can also select existing scales (see Scale).

  Note

If you copy a rate table, the system copies the scales that you created from within the rate table or that you referenced

in the rate table. If you delete a rate table, the system deletes the scales that you created from within the rate table.

However, the system doesn't delete the scales that you referenced in the rate table.

You can edit local scales independently of the rate table they were created within. To enable this editing, you select the

Edit Loc. MD Objects (Edit Local Charge Management Master Data Objects) checkbox in Customizing for

Transportation Management under  Basic Functions

## General Settings

 Define General Settings for TM .

You can also allow a scale item with no value to a scale. When calculating the charges, the system uses the scale item with

no value in the following scenarios:

No scale items match the value of the scale item connected to the calculation base in the freight order or forwarding

order.

The calculation base has no value.

## Conditions

You can specify conditions as scales in a rate table by using the calculation base CONDITION. This enables you to

determine the most appropriate rate when you specify more than one rate for the same kind of scale base. You create

conditions using BRFplus conditions and use these conditions in rate tables. In the rate table, you specify the value for a

condition as true or false. If the system finds this condition in a forwarding order or freight order, it determines a rate from

the rate table where the condition is met.

## Scale items

You can maintain scale items directly in a rate table, for example:

In the Rates table, you can insert a scale item.

In the Rates table, you can generate incremental scale items for a numeric scale if it doesn't already contain any

scale items.

On the Scale Items tab page, you can add a scale item.

Scale items are validity-dependent, meaning you can have different scale items for each validity period listed in the rate

table. When you create a new validity period, the system copies the scale items from the most recently created validity

period into the newly created validity period.

## Index rate tables for fuel surcharges

This is custom documentation. For more information, please visit SAP Help Portal.

165


1/14/26, 2:16 PM

When you have fuel surcharges that change weekly and where you have different fuel surcharges in different zones in your

country or region, you can use a standard index rate table that is valid on a particular date to minimize administration. You

change the fuel surcharge rates in the index rate table just once each week or according to the time gaps in your validity

periods. The system calculates fuel surcharges according to the rate in the zone on the validity date. You can use the

following options to calculate fuel surcharges:

Use the actual rate amounts that you specify in the standard index rate table.

To enable this approach, in the line item of the calculation sheet, specify a standard rate table with a calculation

base of FSC, and an index rate table.

Determine an index for the fuel surcharge and apply the index to the amount or percent you specify in a line item of

a calculation sheet.

In this approach the index rate table specification stays the same, but you don't use the actual rate amounts in the

index rate table. The system uses the fuel surcharge rate for the scale item that is valid on the date you specify in

the Index Base Date field. It determines an index and uses the index along with the amount or percent you specify in

the relevant line item in the calculation sheet to determine the fuel surcharge amount.

To enable this approach using amounts, specify a standard rate table or amount, the index rate table, and the index

base date.

To enable this approach, specify two line items in the calculation sheet. In the first line item, enter the standard rate

table. In the second line item, enter the amount or percent you want to apply, the index rate table, the index base

date, and the reference-from line number for the first line item.

## Calculation rules

You can define a calculation rule and apply it to a rate or scale item. When defining the calculation rule, you must specify

the calculation base, unit of measure, and price unit. If you want the system to apply the calculation rule at rate-table level,

specify the price unit on the Calculation Rules tab page. If you indicate that you want the system to apply the calculation

rule at scale-item level, specify the price unit on the Scale Items tab page. Note that if the price unit of one of the scale

items isn't the same as the others, you must specify the level as Scale Item. The system applies the calculation rule only

when the calculation type of the scale item for the selected rate value is relative.

You can define calculation bases in Customizing for Transportation Management under  Basic Functions

## Charge

## Calculation

 Data Source Binding

 Define Calculation Bases .

  Note

If you specify the validity period for a relative scale that has at least one scale item that is also relative, the system

creates a default calculation rule for the scale items. The system applies the default calculation rule at the rate-table

level.

## Calculation types

You must specify a calculation type before creating a scale item for a scale, which affects how the system calculates

charges with the scale. The available calculation types are absolute and relative. Note that you can specify a relative

calculation type for numeric scale bases only. If the calculation type is relative, apply the calculation rule at scale-item level

and specify a price unit for each scale item.

You can also specify a default calculation type for a scale type based on the calculation base of the scale. The system then

enters the default calculation type when you enter the calculation base for the scale. You can overwrite the default

calculation type. You can specify the default calculation type in Customizing for Transportation Management under

Basic Functions

 Charge Calculation

 Data Source Binding

 Define Calculation Bases .

## Currencies

You can have different currencies for each rate in the rate table. You can also indicate the scales that are relevant for the

currency of the rate. The currency of the rate is then the same as the scale currency.

This is custom documentation. For more information, please visit SAP Help Portal.

166


1/14/26, 2:16 PM

## Through rates

When you trigger charge calculation, the system finds a rate from the source location of the first stage to the destination

location of the last stage. The system calculates the charges based on this rate. To use a through rate, maintain a rate for

the location pair (source location and destination location). You can enable though rates in Customizing for Transportation

Management under  Basic Functions

 Charge Calculation

## Basic Settings

 Define Calculation Profiles .

Rate tables in freight agreement RFQ masters

## Capacity

You can assign capacity driver scales on the Scales tab page and specify the capacity dimension at the rate-table

level. The capacity driver scales determine the scales that constitute the requested capacity in the rate value table.

Freight and forwarding agreement management use capacity scales and capacity dimensions at rate level to specify

confirmed capacity. For more information, see Capacities in Rate Tables for Freight Agreement RFQ Masters.

## Target rates

You can define a target rate or a target amount to specify the maximum price you're willing to pay for a carrier’s

service. You also specify a tolerance as a percentage. If the rate is beyond the target amount or target rate after

applying the tolerance percentage, the system doesn’t take a carrier’s rate into consideration.

## Request rates

You can select the Request Rate checkbox to indicate the rate records that the system downloads when

downloading an individual freight agreement RFQ as a Microsoft Excel file. When you send this file to a carrier, the

carrier responds with rates only for these rate records.

For more information, see Strategic Freight Procurement.

## Activities

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

To define or maintain a rate table for an agreement or calculation sheet, on the launchpad choose one of the following:

Edit Freight Agreement

Edit Forwarding Agreement

Edit Internal Agreement

## Edit Calculation Sheet

To display or edit a rate table separately from the calculation sheet it was created within, open the Edit Rate Table

Definition app or Maintain Rate Table app from the launchpad.

To define a rate table, open the Create Rate Table Definition app from the launchpad. A rate table can be used in multiple

agreements and calculation sheets.

To maintain a rate table, open the Maintain Rate Table app from the launchpad.

To generate incremental scale items, select the relevant row on the Dates and Values tab page. If there's a numeric scale in

the rate table that doesn't already contain any scale items, you can choose the Generate Scale Items button. Select the

scale and the system generates the incremental scale items for that scale. You must enter the values you want the scale

items to start and end at, and the step value you want each scale item to increment by.

To release a validity period so that the rate values can be used for charge calculation, select the validity period on the Dates

and Values tab page and select  Set Status

 Released .

This is custom documentation. For more information, please visit SAP Help Portal.

167


1/14/26, 2:16 PM

Creation and Maintenance of Rate Tables and Local Rate Tables
Using Microsoft Excel

## Use

You can use Microsoft Excel to speed up the process of creating and maintaining large rate tables and local rate tables.

## Features

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

## Rate and Scale Maintenance

You can maintain a large rate table, with or without scale items, using Microsoft Excel. You can enter the rates and scales into a

Microsoft Excel file and upload the file to your TM system. Alternatively, you can define an empty rate table with validity periods in

TM and download it to Microsoft Excel. You can then maintain the rate table in the Microsoft Excel file and upload it to your TM

system.

You can choose to download a rate table to Microsoft Excel in one of the following ways:

Rates for all validity periods in the rate table (scale ranges not included)

Rates for one validity period and selected scale ranges

Rates for multiple validity periods (scale ranges not included)

You can also choose to download the rate table in the background and be notified by e-mail when the download to the application

server path is complete (see Background Download of Rate Tables).

You can view non-numeric scale items in the downloaded excel.

You can choose to upload all the rates and scale items of a rate table from Microsoft Excel to TM.

## Mass Creation of Rates Tables

You can create multiple rate tables in Microsoft Excel using rate table templates and upload them to TM. You use the Mass

Creation of Rate Tables (/SCMTMS/TCC_RATE_MASS_CREATE) program to download the Microsoft Excel template in which you

enter the new rate table details and to upload the new rate table details to TM. In the Microsoft Excel template, you can specify the

following for each row in the Microsoft Excel:

The way you want the name of the rate tables to be generated, that is, by the system, by using the rate table template

name, or by using a rate table name that you provide

The system adds a number to the end of the name of each rate table to avoid any duplication. Note that if you specify that

you want to provide a rate table name, you must enter the rate table name in the Rate Table column.

## The rate table template on which to base the rate tables

You must specify the rate table template for the system to be able to create the rate tables.

## The quantity of rate tables

The system creates 1 rate table if you do not enter a quantity.

The system provides you with a list of the created rate tables and also of those that were not created successfully.

This is custom documentation. For more information, please visit SAP Help Portal.

168


1/14/26, 2:16 PM

## Background Download of Rate Tables

When maintaining a large rate table using Microsoft Excel, you can download the rate table in the background. Transportation

Management (TM) can notify you by e-mail when the download to the application server path is complete. For more information,

see Background Download of Rate Tables.

Background Download of Rate Tables and Local Rate Tables

## Use

When maintaining a large rate table or a local rate table using a spreadsheet application, you can download the rate table or the

local rate table in the background. Transportation Management (TM) can notify you by e-mail when the download to the

application server path is complete.

## Process

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

1. You define a logical path for the logical file Rate Table Background Download (/SCMTMS/RATE_DOWNLOAD_BKGRND)

using transaction FILE and then assign a physical file to the logical file.

2. You download the rate table to the application server path provided in the logical path using the Rate Excel Integration

(/SCMTMS/TCC_RATES_EXCEL_NEW) program.

3. You enter the rate table that you want to download in the background and specify the download details.

4. You specify that you want to download the rate table in the background.

5. You specify whether you want TM to notify you by e-mail when the download to the application server path is complete.

Alternatively, you can use transaction SM37 to view the status of the download.

6. Once the download to the application server path is complete, you download the rate table from the application server path

to your local desktop.

You download the rate table to your local desktop using the program Rate Table Download from Application Server

(/SCMTMS/TCC_DOWNLOAD_FROM_AS) in transaction SE38.

## More Information

Rate Definition and Maintenance

Update Rates

## Use

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

You can use the Update Rates (/SCMTMS/RATE_MASS_UPDATE) program to change the values in a single rate table or in multiple

rate tables at the same time. Note that if you want to change the values in a single rate table, you can also access the Update

This is custom documentation. For more information, please visit SAP Help Portal.

169


1/14/26, 2:16 PM

Rates program directly within the rate table by choosing the Update Rates button.

You can change the values for one period, multiple periods, or all periods in an existing validity period. You can also increase or

decrease a rate by a percentage or an amount.

If the validity period you need to update is not already specified in the existing validity periods, you can create a new validity period

in which the rate change applies. You can specify a new validity period within the date ranges already specified in the existing

validity periods. You can also specify a new validity period that is outside the existing validity periods in the rate table. By default,

the system uses the rate, calculation rule, and scale item settings in the latest validity period when it creates the new validity

period. For new validity periods, you can also automatically set the status to Released during the rate table update.

## Integration

The update of rates is a function in rate maintenance. For more information, see Rate Definition and Maintenance.

## Prerequisites

You have specified the settings required for rate maintenance. For more information, see Rate Definition and Maintenance.

## Features

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

## Master Data Cockpit

You can update rate tables for forwarding, freight, and internal agreements from the master data cockpit. To work with the master

data cockpit, open the Charge Management app from the launchpad, choose the master data cockpit for the relevant agreement

type, and enter your search criteria.

In the personal object worklist result, if you select a line item that contains both a rate table and a calculation sheet, the system

opens the Update Rates function when you choose the Update Rates/Calculation Sheet Amounts button. The system

automatically includes the rate table from the selected line item in the update criteria when you open the function.

If you select a line item that contains a rate table and a different line item that contains a calculation sheet only, the system opens

both the Update Rates and Update Calculation Sheet Amounts functions on the same screen when you choose the Update

Rates/Calculation Sheet Amounts button. The system automatically includes that rate table and calculation sheet from the

selected line items in the update criteria when you open the function.

For more information, see Update Calculation Sheet Amounts.

## Scale Ranges

When you specify a new validity period or when you update a rate in an existing validity period, you can also specify a scale range,

for example, source location. This enables the system to change only the rates in a particular scale range. However, you can only

specify a scale range that is already specified in an existing validity period of an existing rate.

## Scale Items

You can update rates based on the calculation type of the scale items (for example absolute or relative, or both absolute and

relative). For example, you can update the rates for relative scale items with one rate change and the rates for absolute scale items

with a different rate change. For relative value scale items, you can also update the price unit. For more information, see Rate

Definition and Maintenance.

This is custom documentation. For more information, please visit SAP Help Portal.

170


1/14/26, 2:16 PM

## Display Currency

You can display the currency of a rate table so that you are fully informed before you make any updates.

## Example

You want to create a new validity period that contains new rates where two validity periods already exist. The following table

describes the settings in the first existing validity period of January 1, 2010 to December 31, 2010:

## Source Location

Destination Location Value (USD)

NYC

NYC

NYC

PHI

CHI

SFO

100

120

340

The following table describes the settings in the second existing validity period January 1, 2011 to December 31, 2011:

## Source Location

Destination Location Value (USD)

NYC

NYC

NYC

PHI

CHI

SFO

110

130

350

You need to create a new validity period with new rates to cover the period December 1, 2010 to December 31, 2010. The following

table describes your inputs to the Update Rates function:

Setting

## Attribute

New validity period setting from 12-01-2010

New validity period setting to

12-31-2010

Source location

NYC

Destination location

PHI, CHI

Percentage

+10%

The system creates a new validity period for December 1, 2010 to December 31, 2010 with new rates. It keeps the old validity

period for 2010, but changes the validity dates to January 1, 2010 to November 1, 2010. The following tables describe the new

validity periods:

Validity 1: January 1, 2010 to November 1, 2010

## Source Location

Destination Location Value (USD)

NYC

NYC

NYC

PHI

CHI

SFO

100

120

340

This is custom documentation. For more information, please visit SAP Help Portal.

171


1/14/26, 2:16 PM

Validity 2: December 1, 2010 to December 31, 2010

## Source Location

Destination Location Value (USD)

NYC

NYC

NYC

PHI

CHI

SFO

110

132

340

## More Information

Rate Definition and Maintenance

Master Data Cockpit

Rate-Level Validity Periods

## Use

You can change rates on a short-term basis without needing to update all the rates of the parent validity period in the rate table or

the local rate table. This allows you to, for example, offer lower rates for a specific time period.

To specify a rate on a short-term basis, you split the validity period of the rate into a shorter validity period than that of the parent

validity period in the rate table or the local rate table. You can split a validity period multiple times. You then enter a rate for each of

the shorter validity periods.

  Note
If you enable rate validity split, you can only view rates on the Rates tab page in a list view. You cannot view rates with a column

scale in a grid view.

## Prerequisites

You have enabled rate validity split in Customizing for Transportation Management under  Master Data

 Rate Tables

## Define

Rate Table Types .

## Activities

To be able to specify rates on a short-term basis, you select the Rate Validity Split checkbox on the General Data tab page of the

rate table or the local rate table. Note that once you select the Rate Validity Split checkbox and save your changes, you cannot

deselect the checkbox.

On the  Dates and Values

 Rates  tab page, you can then split the rate validity of a rate by choosing the Split Rate Validity

button and specifying the date on which you want to split the rate validity. The system enters that date as the end date of the rate

that you selected to split. The system also creates a new row with a rate whose validity period starts on the rate validity split date

and ends on the end date of the parent validity period.

Note that you can also simply copy the rate into another row and split the validity period manually.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

172


1/14/26, 2:16 PM

If you change the start date or end date of a parent validity period, by default the system adjusts all its rate-level validity periods

that have the same start date or end date.

If you select the Update Rate Validity Periods checkbox, the system adjusts any rate-level validity periods that are inconsistent

with the parent validity period. This adjustment may include deleting rates that have invalid validity periods or validity periods

outside of the parent validity period. If you deselect this checkbox, the system informs you about any inconsistent rate-level

validity periods. You can then adjust each inconsistent rate-level validity period manually or by choosing the Update Rate

Validity Periods button.

Rate Categories

## Use

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

You can specify the rate category of a rate table to facilitate the calculation of air freight charges. Once you specify the charge type

for a rate table, you can specify the rate category. The rate category affects the scale items you should have in the rate table or the

local rate table. The rate categories available are as follows:

Unit Load Device (ULD)

If you define a rate table as a ULD rate category, you must define a scale with a weight-based calculation base. Once you define a

weight-based scale item, you can choose the Maintain Scale Items button to automatically create /A or /B scale items of rate

class U (ULD rate) and /C scale items of rate class E (extension rate).

For weight-based scale items, you can choose a ULD charge code type of /A or /B. For ULD charge code types of /A and /B, the

system automatically applies rate class U (ULD rate) for pivot weights. For ULD charge code types of /C, the system automatically

applies rate class E (extension rate) for over-pivot weights.

If you choose ULD charge code type /A, the system applies charge codes /A and /C for pivot and over-pivot scale items

respectively. If you choose charge code type /B, the system applies charge codes /B and /C for pivot and over-pivot scale items

respectively. If you choose a rate table view type of Column, you use the Maintain Scale Items button to create scale items. If you

choose the list view, the system uses the ULD charge code types you specify in  General Data

 Charge Type Settings  for all

scale items.

When creating the scale items for weight-based scales in a ULD rate table, you can create multiple pivot weights for the ULD rate

types. You can then use different pivot weights when required, for example, for different origin and destination location pairs, days

of the week, or flight codes. The system displays the additional pivot weights in the over-pivot charge column of the rate table and

in spreadsheet file downloads.

  Note

Scale items with ULD charge code /A are rates per kg based on the minimum pivot weight per the International Air Transport

Association (IATA) ULD rating type. ULD charge code /A represents a relative rate against the scale item combination.

Scale items with ULD charge code /B are minimum flat charges per the IATA ULD rating type with a chargeable weight up to the

first defined weight break. ULD charge code /B represents an absolute amount against the scale item combination.

Specific Commodity Rate (SCR)

This is custom documentation. For more information, please visit SAP Help Portal.

173


1/14/26, 2:16 PM

If you define a rate table as an SCR rate category, you must define a scale with the COMMODITY_CODE calculation base and a

commodity code type, and a scale with a weight-based calculation base. The rate class S is associated with the scale items of an

SCR rate table.

## General Cargo Rate (GCR) – M, N, & Q

If you define a rate table as a GCR – M, N, & Q rate category, you must define a scale with a weight-based calculation base and

ensure it’s mandatory to maintain a minimum value for the calculated rate. Once you define a weight-based scale item, you can

choose the Maintain Scale Items button to automatically create one scale item of rate class N (normal rate) and one or multiple

scale items of rate class Q (quantity rate).

## More Information

Rate Definition and Maintenance

Charge Management Settings for Air Freight

TACT Rates

## Use

You can calculate air freight transportation charges based on TACT rates, as well as using the contract rates available in standard

rate tables (both kinds, inclusing local) in Transportation Management (TM). The International Air Transport Association (IATA)

publishes TACT rates three times a year, and most of the world's major carriers use TACT rates for air freight. IATA represents more

than 100 airlines comprising more than 70% of scheduled international air traffic. TACT rates are published between city pairs and

can be specific to carrier and to unit load device (ULD) rate type.

The system automatically determines the relevant TACT rate based on the following mandatory parameters:

City of departure and destination

## Chargeable weight

You can specify more parameters before the system determines the relevant TACT rate.

## Prerequisites

You have uploaded TACT rates to TM (see TACT Rate Upload).

You have defined unit load device (ULD) rate types in Customizing for Transportation Management under  Basic

## Functions

 Charge Calculation

 Air Freight Settings

 Define ULD Rate Types .

You have mapped ULD types to ULD rate types in Customizing for Transportation Management under  Basic Functions

 Charge Calculation

## Air Freight Settings

 Map ULD Types to ULD Rate Types .

You have defined IATA airport codes and mapped them to IATA city codes in Customizing for Transportation Management

under  Basic Functions

 Type Codes and Role Codes

 General Type Codes and Role Codes

 IATA Codes

 Define IATA

Location Codes .

## Features

## TACT Rates personal object worklist

This is custom documentation. For more information, please visit SAP Help Portal.

174


1/14/26, 2:16 PM

You can view and search for specific TACT rates in the TACT Rates personal object worklist.

## Contract rates

Generally, contract rates are lower than TACT rates for a specific city pair and weight range. As a logistics service provider,

you can agree a contract rate with a carrier but charge a TACT rate to the customer. To enable this, you can specify a TACT

rate for printing the settlement document and a contract rate for pricing. You specify which rate type to use for printing and

which for settlement.

  Note

If you charge a TACT rate to the customer, the default calculation method is air freight: standard rating. However, you

can choose to use a different calculation method.

If you have a TACT rate in the air waybill (AWB) but charge a contract rate to the customer, you should not use a break-

weight calculation method. However, if you use a break-weight calculation method, the system takes the chargeable

weight in the AWB into account for the settlement document. Note that the system then may use a higher weight break

than the one determined by the break-weight calculation method. For more information, see Calculation Methods.

## TACT rate types

The following TACT rate types are available:

## ULD rate

Specific commodity rate

General cargo rate

More Information

## Rate Table

## Rate Definition and Maintenance

Setup of MD for Charge Management and SP Catalogs

Charge Calculation

TACT Rate Upload

## Use

Uploading TACT rates to database tables in Transportation Management (TM) allows TM to use TACT rates when calculating air

freight transportation charges. You upload TACT rates each time the International Air Transport Association (IATA) publishes them.

## Process

1. You define a logical path for the /SCMTMS/TACT_UPLOAD logical file using the Logical File Path Definition transaction

(transaction FILE) and then assign a physical file to the logical file.

2. You upload the TACT rate file to the application server and trigger the system to process the TACT rates in database tables

using the TACT Rate Upload transaction (transaction /SCMTMS/TACT_UPLOAD).

This is custom documentation. For more information, please visit SAP Help Portal.

175


1/14/26, 2:16 PM

You can specify selection parameters to restrict the TACT rates you want the system to process. The system processes the

TACT rates in the background. You can view the status using the Simple Job Selection transaction (transaction SM37).

  Note
You can use the TACT Rate Process transaction (transaction /SCMTMS/TACT_PROCESS) at a later point in time to

process TACT rates that you previously uploaded to the application server.

You can use the TACT Rate Upload (/SCMTMS/TACT_RATE_UPLOAD) report and the TACT Rate Processing

(/SCMTMS/TACT_RATE_PROCESS) report instead of the transactions.

3. The system automatically maps IATA codes to SAP codes using the Mapping of IATA Codes to SAP Codes

(/SCMTMS/TACT_MAP_IATA_TO_SAP) report.

You can also run this report at a later point in time if, for example, more country or region codes are added.

More Information

## TACT Rates

Scale and Local Scale

## Definition

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

A scale is a dimension of a rate. A scale is used to define a parameter that then defines a rate. For example, if a rate depends upon

distance and weight, you must define a separate scale for distance and for weight. The distance and weight scales are then used to

define the rate.

## Use

You can create a scale (both kinds, including local) manually or automatically by using a scale template with predefined scale

bases and calculation type. For more information about master data templates, see Scale Maintenance. For more information

about Customizing templates, see Customizing for Transportation Management under  Basic Functions

 Charge Calculation

 Basic Settings

## Templates

 Define Scale Templates .

## Structure

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

A scale can contain the following main tab pages and screen areas:

## General Data

The General Data tab page contains general information about the scale, for example, the scale unit measure and the scale

base, which defines how the system interprets the scale values during calculation. Note that you can assign a default

calculation type to the calculation base in Customizing for Transportation Management under  Basic Functions

## Charge

## Calculation

 Data Source Binding

 Define Calculation Bases .

## Items

This is custom documentation. For more information, please visit SAP Help Portal.

176


1/14/26, 2:16 PM

The Items tab page contains the details of the scale items such as the calculation type, which indicates how the system

calculates charges with the scale item.

  Note
If you use a scale in a rate table and use the Maintain Scale Items button on the Scales Items tab page of the Dates and

Values tab page, the system automatically enters the default calculation type for the calculation base of the scale item.

If you enter a calculation type for a scale item, the system overwrites the default calculation type with the one you

entered. You can also manually change the calculation type for a scale item.

## Change Documents

You can view all changes made to a scale on the Change Documents tab page or screen area. The changes are listed by

date and time. You view the details of the changes at header level by selecting the relevant row in the Transactions screen

area and at field level by selecting the relevant row in the Record Level Changes screen area. You must refresh the scale to

view recently-saved changes.

## Integration

A scale is integrated with agreements, calculation sheets, local calculation sheets, rate tables, and local rate tables. A scale or a

local scale is used by a rate table or a local rate table to define the rates. For more information, see Agreement, Calculation Sheet,

and Rate Table.

More Information

## Charge Calculation

Setup of MD for Charge Management and SP Catalogs

Scale Maintenance

## Use

You create and maintain scales (both kinds, including local) as a step in the process to set up master data for charge calculation.

For example, you can configure the items of a scale according to one of the following:

Quantities

Volumes

Weights

Distances

Points

  Note

You can generate incremental scale items for a scale (both kinds, including local) when you are defining a rate table (both kinds,

including local). For more information, see Rate Definition and Maintenance.

## Integration

This is custom documentation. For more information, please visit SAP Help Portal.

177


1/14/26, 2:16 PM

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

Scale maintenance is a step in the process to set up master data in the Charge Management and Service Product Catalogs

component and is integrated with agreements, calculation sheets, and rate tables. For more information, see Setup of MD for

Charge Management and SP Catalogs.

You can use the master data cockpit to access an overview of the charge management master data per organizational unit,

business partner, and charge type. The system also shows the relationship between the different types of charge management

master data. For more information, see Master Data Cockpit.

## Prerequisites

You have defined a valid scale base with a relevant unit of measure in Customizing for Transportation Management under

Basic Functions

 Charge Calculation

 Data Source Binding

 Define Scale Bases .

You have defined number ranges in Customizing for Transportation Management under  Basic Functions

## Charge

Calculation

## Basic Settings

## Number Range Intervals

 Assign No. Ranges to Calc. Sheets, Rate Tables, & Scales .

## Features

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

## Templates

You can use templates to create scales and scale items with predefined scale bases, calculation types, and rate categories.

You can define Customizing templates in Customizing for Transportation Management under  Basic Functions

## Charge

Calculation

 Basic Settings

## Templates

 Define Scale Templates . You can transfer Customizing templates across

different TM systems.

You can define master data templates directly in Transportation Management (TM). If required, you can define a master

data template based on a Customizing template.

You can view and update all scale templates in the Scale Templates personal object worklist.

## Calculation types

You can specify a calculation type for a scale base, which affects how the system calculates charges with the scale. The

available calculation types are absolute and relative. Note that you can specify a relative calculation type for numeric scale

bases only.

You can also specify a default calculation type for a scale type based on the calculation base of the scale base. You can

specify the default calculation type in Customizing for Transportation Management under  Basic Functions

## Charge

## Calculation

 Data Source Binding

 Define Calculation Bases .

## Activities

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

To define a master data template for a scale, open the Create Scale Template app from the launchpad.

To create or update a scale for an agreement, calculation sheet, or rate table, on the launchpad choose one of the following:

This is custom documentation. For more information, please visit SAP Help Portal.

178


1/14/26, 2:16 PM

Edit Freight Agreement, Edit Forwarding Agreement, or Edit Internal Agreement

Edit Calculation Sheet

## Maintain Rate Table

To display or edit a scale separately from the agreement, calculation sheet, or rate table it was created within, open the Edit Scale

app from the launchpad. Note that to be able to edit local scales independently of the charge management master data object

they were created within, you select the Edit Loc. MD Objects (Edit Local Charge Management Master Data Objects) checkbox in

Customizing for Transportation Management under  Basic Functions

## General Settings

 Define General Settings for TM .

To create or update scales, open the Create Scale app or the Edit Scale app from the launchpad. A scale can be used in multiple

agreements, calculation sheets, and rate tables.

More Information

## Scale

Master Data Cockpit

## Use

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

The master data cockpit provides an overview of the agreements and charge management master data per organizational unit,

business partner, and charge type. It also provides links directly to the main master data and shows the relationship between the

different types of charge management master data.

The master data cockpit lists the master data by freight agreement, forwarding agreement, or internal agreement and by default,

displays the agreements and rate tables that are valid on the current date. You can expand the list to see the rates, calculation

sheets, and related information, such as currencies, scale bases, and scale items. You can use the master data cockpit to get

specific information, for example:

The rates for a transport between your sales organization and a specific customer or between your purchasing organization

and a specific carrier

All charges maintained for one item in an agreement that has many rate tables

## The agreements valid for a specific period

Note that the system always includes the agreements and rate tables that are valid on the current date, as well as the

agreements and rate tables that are valid for the specific period.

## Integration

The master data cockpit is integrated with agreements and with the charge management master data: calculation sheets, local

calculation sheets, rate tables, local rate tables, scales, and local scales. For more information, see Agreement, Calculation Sheet,

Rate Table, and Scale.

## Features

This is custom documentation. For more information, please visit SAP Help Portal.

179


1/14/26, 2:16 PM

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

## Selection Criteria

You enter selection criteria, such as status, transportation mode, and source zone, to filter the agreements and master data

objects you want to list in the master data cockpit. For freight agreements, you must enter the purchasing organization and carrier

as selection criteria. For forwarding agreements, you must enter the sales organization and ordering party as selection criteria. For

internal agreements, you must enter the organizational unit name and business partner as selection criteria.

  Note
If an agreement item of an agreement or a calculation sheet item matches the selection criteria but the agreement header does

not, the agreement still appears in the master data cockpit. It is sufficient for the selection criteria to match the agreement

item or calculation sheet item. The agreement header does not need to match the selection criteria. However, the business

partner details specified in the agreement header must be a subset of the business partner details specified by the

preconditions at the agreement item level.

You can also enter attributes in the selection criteria for the system to use when determining which calculation sheets to list in the

master data cockpit. The attributes for calculation sheet and calculation sheet items are shipment type, stage type, and service

level.

You can also enter preconditions in the selection criteria for the system to use when determining which agreements to list in the

master data cockpit. The preconditions for agreement and agreement items can be, for example:

Transportation mode

Shipment type

Traffic direction

Stage type

Service level

Air waybill type

  Note
If an agreement item of an agreement or a calculation sheet item matches the preconditions or attributes but the agreement

header does not, the agreement still appears in the master data cockpit. It is sufficient for the preconditions or attributes to

match the agreement item or calculation sheet item. The agreement header does not need to match the preconditions or

attributes.

The system also considers the trade lane preconditions specified for an agreement item. However, the system displays the

calculation sheet item irrespective of the trade lane preconditions specified for a calculation sheet item.

## Mass Update

You can change the charge item amount in one or more calculation sheets at the same time. For more information, see Update

Calculation Sheet Amounts.

You can change the rate values in a single rate table or in multiple rate tables at the same time. For more information, see Update

Rates.

## Currency Conversion

This is custom documentation. For more information, please visit SAP Help Portal.

180


1/14/26, 2:16 PM

You can convert the currency of the rate amount using the Convert Currency button.

## Layout

You can add and remove columns to the master data cockpit, and save the changes as a personalized view. In the Master Data

Cockpit for Forwarding Agreements, you can choose to use a layout with the Agreement, Calculation Sheet, and Rate Table

columns always visible.

## Activities

To access the master data cockpit, open the Charge Management app from the launchpad. Choose the master data cockpit for

the relevant agreement type and enter your selection criteria, including the mandatory criteria.

Charge Calculation

## Use

You can calculate the charges for transporting goods between locations based on the rates you maintain in a rate table (both

kinds, including local). The system uses master data, such as, agreements, calculation sheets, local calculation sheets, rate tables,

and local rate tables, when calculating transportation charges. For more information, see Charge Management and Service

Product Catalogs.

You can trigger charge calculation from the following Transportation Management (TM) components:

Forwarding Order Management

Freight Order Management

## Planning

Forwarding Settlement

## Freight Settlement

Note that you can manually edit the transportation charges after charge calculation.

## Types of Charge Calculation

The system uses a standard charge calculation process to calculate transportation charges for the following:

Forwarding orders

## Freight orders

Forwarding settlements

Freight settlements

Forwarding quotations

Service orders

## Tendering

## Carrier selection

For more information, see Standard Charge Calculation.

This is custom documentation. For more information, please visit SAP Help Portal.

181


1/14/26, 2:16 PM

The charge calculation process can also vary depending on multiple factors, for example:

## Transportation mode category

The system uses a slightly different charge calculation process to calculate the charges for air freight. For more

information, see Air Freight Charge Calculation.

For rail transportation, you can calculate charges based on the number of railcar units. You can also calculate the

transportation charges in rule 11 scenario in a rail freight order when the carrier that pays for the stage is the same

or different from the carrier that executes the stage. For more information, see Rail Freight Order.

## Services

You can charge your customers for the additional charges incurred due to varying fuel costs. For more information,

see Fuel Surcharge Calculation.

When you create a service order for a freight booking or a freight booking item, you can calculate the charges for the

services. For more information, see Service Order.

  Note
We improved how TM determines the rates during charge calculation for agreement items and calculation sheet line items that

have preconditions. We improved system performance during charge calculation by ignoring empty instances of precondition-

dependent objects. If you upgraded to TM 9.4 or lower, you can use program Precondition Refactoring for Agreement and

Calculation Sheet Items (/SCMTMS/MIGR_140_PRECOND_UPD) to implement the performance improvements.

## Features

Calculating transportation charges enables you to analyze the profitability of a forwarding order. The system takes into

account all the costs and revenues associated with the processing of a forwarding order and determines the associated

profit.

For more information, see Profitability Analysis.

You can distribute costs in freight orders or freight settlement documents at an ERP-item level or forwarding-order level.

For more information, see Cost Distribution Management.

During carrier selection, calculating the transportation charges helps you to determine the lowest total costs.

For more information, see Strategies.

During tendering, calculating the transportation charges helps you to calculate the absolute price limit.

For more information, see Tendering.

You can consolidate freight units from multiple forwarding orders into a trailer freight unit and charge the customer based

on specific criteria, for example, a standard rate or the weight of the trailer.

For more information, see Use of Trailers.

The system automatically triggers charge calculation when you create the following:

Forwarding settlement document

Freight settlement document

Internal settlement document

## Credit memo

You can calculate charges for multiple forwarding orders and freight orders.

This is custom documentation. For more information, please visit SAP Help Portal.

182


1/14/26, 2:16 PM

You can calculate the charges for multiple forwarding orders using the Mass Charge Calculation for Forwarding Orders

report. To access the report, on the SAP Easy Access screen, choose  Logistics

 Transportation Management

 Administration

## Background Processing

 Calculate Charges for Forwarding Orders .

You can calculate the charges for multiple freight orders using the Mass Charge Calculation for Freight Orders report. To

access the report, on the SAP Easy Access screen, choose  Logistics

 Transportation Management

 Administration

## Background Processing

 Calculate Charges for Freight Orders .

When you create a credit memo, the system recalculates the transportation charges for the relevant forwarding order.

For more information, see Credit Memos.

You can calculate transportation charges between organizations of the same company code and between organizations of

different company codes. If the involved business units and gateway belong to different organizations of the same company

code, you perform intracompany settlement. If the involved business units and gateway belong to the organizations of

different company codes, you perform intercompany settlement. You can also calculate the internal charges in a freight

order when a purchasing organization of the freight order subcontracts resources from another organization.

Note that the system calculates the internal charges in a freight order based on the resources. You use internal agreements

to maintain the contract between the different organizations that belong to the same company code or different company

code.

For more information, see Internal Settlement Management.

If you’re using an agreement stored in an external system, you can establish a connection from TM to the external system.

The system displays the external agreement and the freight agreement item number on the Details tab page of the

Charges tab page.

For more information, see External Agreements.

The system calculates the charges based on the settlement basis you specify in the forwarding agreement.

If you specify the settlement basis as trailer-based, the system sets the calculation level as stage level in the forwarding

order. During settlement, the system creates a single forwarding settlement document for all the forwarding orders that

meet the specified execution criterion and bills the business partners based on certain execution criteria, such as the

number of trailers used to fulfill the order. The system also changes the invoicing status of the technical charge item in the

Charges tab of the forwarding order accordingly. If you don’t specify the settlement basis, the system sets the settlement

basis as forwarding order-based. The system uses the calculation level specified in the calculation profile and settles each

of the forwarding orders individually.

For more information, see Forwarding Settlement.

You can create invoices for partial amounts by manually entering the amounts in forwarding settlement documents.

You can specify the calculation date type that the system uses as the basis for the rate, exchange rate, and agreement

validity, and ultimately the charge calculation.

If the calculation date type for a subcontracting-relevant freight order is order date, the system calculates the charges

based on the date that the freight order is subcontracted to the carrier. The system displays the order date on the

Subcontracting tab page of the freight order.

You specify the calculation date type in Customizing for Transportation Management under  Basic Functions

## Charge

Calculation

## Basic Settings

 Define Calculation Profiles .

The charge lines created from the calculation sheet item with the SERVICE resolution base inherit the logistical data from

the main item in the hierarchy.

When you assign a charge type to a service type, the system defaults the resolution base to SERVICE. You assign charge

types to service types in Customizing for Transportation Management under  Basic Functions

 Charge Calculation

## Basic Settings

 Assign Charge Types to Service Types .

This is custom documentation. For more information, please visit SAP Help Portal.

183


1/14/26, 2:16 PM

For more information, see Service Product Catalogs.

You can selectively apply charges for certain charge types (for example, fuel), for active vehicle resources only (for example,

truck) and not the passive vehicle resources (for example, trailer). You use the resolution bases ACTIVE_RESOURCE and

PASSIVE_RESOURCE to differentiate between active vehicle resources and passive vehicle resources.

You can access the details and messages generated during charge calculation on the Charges or Internal Charges tab page

of the relevant business documents, such as a forwarding quotation, forwarding order, and freight order.

For more information, see Charges Overview.

When you create a follow-on settlement document from a freight order or forwarding order, you can manually change the

charge amount for a charge line in the forwarding order or freight order. When you recalculate charges in the settlement

document, the system can update the charge amounts in the settlement document based on the manually-changed charge

amounts in the forwarding order or freight order.

You enable the system to update charge amounts in the settlement document based on manually-changed charge

amounts in the forwarding order or freight order by selecting the Update Settl. Chrgs from Order checkbox in Customizing

for Transportation Management under  Settlement

 Define Settlement Profiles .

If you have freight order or a freight booking with items that have different source and destination locations, the system can

determine a rate based on the locations in the item. Note that rate determination using locations in the item works only

when calculating charges at item level and header level.

You can use freight terms as the basis of settling forwarding orders and forwarding quotations. You can agree the

transportation charges in advance with your sold-to party. In the calculation sheet (both kinds, including local), on the

Freight Terms tab, you can specify the payer (prepaid or collect) for a charge type for a freight term. That is, the same

freight term can have a different payer for different charge types. The system calculates charges based on this information

you specify and serves as the basis for settling the overall transportation costs.

You can use a single forwarding quotation or a forwarding order with freight terms to calculate the prepaid and collect

charges. The system creates two charge items one each for the prepaid payer and the collect payer. You can create

forwarding settlement documents to settle charges between the following parties:

Prepaid invoicing party and prepaid payer for prepaid charges

Collect invoicing party and collect payer for the collect charges

For more information, see Freight Terms in Forwarding Orders.

You can determine the rates you want to provide to shippers or logistics service provider for forwarding agreement

quotation items based on the existing service products. In this case, the system doesn’t perform charge calculation but

provides logistical information of the customer by analyzing the existing and past service products. For more information,

see Rate Determination of Forwarding Agreement Quotation Items.

## More Information

Setup of MD for Charge Management and SP Catalogs

Standard Charge Calculation

## Use

This process describes how the system calculates transportation charges when you trigger charge calculation from one of the

following Transportation Management components:

This is custom documentation. For more information, please visit SAP Help Portal.

184


1/14/26, 2:16 PM

Forwarding Order Management

Freight Order Management

Forwarding Settlement

Freight Settlement

## Prerequisites

In Customizing, you have carried out the activities for Transportation Management under  Basic Functions

## Charge

Calculation .

You have set up the master data for the Charge Management and Service Product Catalogs component.

For more information, see Setup of Service Product Catalogs and Charge Management MD.

## Process

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

1. You trigger charge calculation.

You can also calculate transportation charges between organizations of the same company code and between

organizations of different company codes. For more information, see Internal Settlement Management.

The system can calculate charges at header, item, or stage level, depending on your Customizing settings in the calculation

profile.

2. The system determines the agreement within organizational hierarchies (such as company organization or corporate

organization) and calculation sheets.

You can specify a leading charge type that must have a value for the system to consider the calculation sheet for charge

calculation. You specify leading charge types in Customizing for Transportation Management under  Basic Functions

 Charge Calculation

## Basic Settings

 Define Charge Types . For more information, see Calculation Sheet Maintenance.

You can also enter a zero rate for a mandatory charge line by selecting the Zero Rate checkbox in the rate table. The system

still considers the calculation sheet for charge calculation.

Note that if you trigger charge calculation from a personal object worklist (POWL) or if you perform batch charge

calculation with the agreement determination type as Display All Agreements, the system does not calculate charges. Also,

the system sets the calculation status as Automatic Charge Calculation Failed.

For more information, see Agreement and Calculation Sheet Determination.

3. The system determines rate tables and scales.

The system determines the most appropriate rate when calculating transportation charges, based on certain criteria and

attributes. For more information, see Rate Determination.

4. During calculation, the calculation sheet combines charge items while taking into account the sequence in which the

system takes these charge items.

5. The system rounds the charges for each charge line before calculating the total charges or rounds the charges once it has

calculated the total charge, depending on your settings.

You specify the level you want to round the charges at in Customizing for Transportation Management under  Basic

## Functions

 Charge Calculation

## Rounding

 Assign Rounding Profiles to Document Currencies .

This is custom documentation. For more information, please visit SAP Help Portal.

185


1/14/26, 2:16 PM

  Note

You can access the details and messages generated during charge calculation on the Charges or Internal Charges tab

page of the relevant business documents, such as a forwarding quotation, forwarding order, and freight order. For more

information, see Charges Overview.

The system displays the notes, which you have entered in the calculation sheet item, in the corresponding charge line

during charge calculation.

6. You can manually change the calculation bases, quantity, and unit of measure for a charge item and recalculate the

charges.

When you manually change the quantity, the system determines the appropriate rate from the rate table for the changed

quantity. If you have maintained only one calculation base in your rate table, the system displays it in the Calculation Base

field on the Charges tab page by default. If you have maintained more than one calculation base in the rate table, you must

choose one from the input help that displays all the calculation bases maintained in the rate table. Note that the system

can recalculate the charges only if the charge item has a rate table and the calculation base is numeric.

  Note

If you manually change, insert, or delete a charge line, the system flags the charge line as being manually changed. The

system retains manual changes during charge recalculation, provided that the system determines the same agreement

and agreement item. However, the system overwrites manual changes during charge recalculation in the following

situations:

You change the business partner, organizational unit, or logistical data and the system determines a different

agreement or calculation sheet during recalculation.

You change the calculation level.

You split or merge stages in the business document for through rates.

You change charge items due to through rates.

If you reset the charges in a business document, the system also resets manual changes.

More Information

## Charge Calculation

Air Freight Charge Calculation

Fuel Surcharge Calculation

Calculation Profiles

Calculation Logic

Calculation Logic

## Use

This function enables the system to use the following objects when calculating transportation charges:

## Resolution base

This is custom documentation. For more information, please visit SAP Help Portal.

186


1/14/26, 2:16 PM

Calculation base

Collective rate

## Integration

This function is used in the charge calculation process, which is used in the following Transportation Management (TM)

components:

Forwarding Order Management

Freight Order Management

Forwarding Settlement

## Freight Settlement

For more information, see Charge Calculation.

## Features

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

## Resolution Base

With the resolution base, you assign the charge type to a certain data source level. The charge type, for example, FB00, which is a

single building block of the calculation sheet, is calculated with regard to the resolution base. During charge calculation, the

system resolves the calculation sheet according to the given input data. At runtime, the calculation logic works as follows:

1. As a result of the initial resolution step, the system creates a calculation table based on the logistical data source. The

system has not yet performed any calculations or determined any rates.

2. The system processes the calculation table and determines a value for each row given in the calculation sheet. If the

system cannot determine any value for a certain charge type, the system issues a warning or error and does not apply a

charge for that row in the calculation sheet. However, the process is not interrupted.

  Note

The resolution base is defaulted to SERVICE in the calculation sheet, when you maintain a charge type in the calculation sheet

that is assigned to a service type in Customizing for Transportation Management under  Basic Functions

## Charge

Calculation

## Basic Settings

 Assign Charge Types to Service Types .

You can retain the default resolution base of SERVICE, if you maintain the service as a main item in the forwarding order and

you want the system to apply the charges for the service only once in the charge item. The system applies the service charges

based on the availability of the service type in the forwarding order and the corresponding charge type in the calculation sheet.

You can change the default resolution base of SERVICE, if the charge type entered in the calculation sheet is for charging a

service for a container or package or product. For the system to apply these charges, the item of corresponding service type

should be specified as the main item. The system applies the service to the appropriate logistical items based on the resolution

base of the corresponding charge type in the calculation sheet.

  Example

In the forwarding order, you have three containers for which you have to apply the charges for fumigation service.

This is custom documentation. For more information, please visit SAP Help Portal.

187


1/14/26, 2:16 PM

You have a charge type CT_FUMIG assigned to a service type SERV_FUMIG. In the calculation sheet, when you insert a charge

line with the charge type CT_FUMIG, the system defaults the resolution base as SERVICE. You change the resolution base to

CONTAINER in the calculation sheet. In the forwarding order, you insert an item with the service SERV_FUMIG as the main

item. During charge calculation, the system creates three charge lines for three containers each and calculates the charges.

You can also charge a service to different logistical items. You must maintain a service type as a sub item under the

corresponding container or package or product. You must maintain a charge type with the resolution base as SERVICE. During

charge calculation, a service charge line is created for each logistical item that has service as a sub item.

## Calculation Base

With the calculation base, you define the instruction to determine the data source. The calculation base represents the

configurable link to the data source with which a rate is determined. The system uses the calculation base to automatically

execute charge calculation.

  Example

You have a two-dimensional rate table with the first dimension (scale) based on the destination harbor and the second

dimension (scale) based on the weight of the cargo to be shipped. The rate that the system identifies after the two dimensions

of the price matrix have been evaluated, for example USD 39.60, is multiplied by the volume to be shipped. In this example, the

logistical data source has to provide at least three different pieces of information to calculate the correct charge. There is a

calculation base for each of these three entities, describing the path to the certain data source.

  Example

You are shipping a container from Europe to various destinations in the United States, such as New York and Los Angeles. You

want to charge for the transportation based on the source location (Europe), the destination location (New York and Los

Angeles), and the gross weight of the container. To enable this, you define a rate table with three scales (dimension) – source

location, destination location, and gross weight. Each of these scales uses the corresponding calculation bases, which are

SOURCELOC, DESTLOC, and GROSS_WEIGHT.

The calculation base and the resolution base are coupled in a way that the same calculation base leads to a different data source

dependent on the currently processed resolution base.

  Example

You have the following master data maintained in a calculation sheet:

Calculation Base

Resolution Base

## Calculation Rule

Gross Weight (maintained in rate table A

Container (for charge type FB00)

USD 10 per 100 kg

for charge type FB00)

Gross Weight (maintained in rate table B

Package (for charge type BASE)

USD 25 per 100 kg

for charge type BASE)

You have an FWO with 2 containers and 1 package with the following gross weights:

Container 1–1000 kg

Container 2–2000 kg

## Package 1–200 kg

This is custom documentation. For more information, please visit SAP Help Portal.

188


1/14/26, 2:16 PM

In this situation, the system applies charge type FB00 for each container (resolution base = container) and calculates the

transportation charges as follows:

Container 1: (1000/100)*10 = USD 100

Container 2: (2000/100)*10 = USD 200

The system also applies charge type BASE for each package (resolution base = package) and calculates the transportation

charges as follows:

Package 1: (200/100)*25 = USD 50

## Collective Rate

With a collective rate, you apply group discounts to charge types using a grouping rule. You base the grouping rule on a calculation

base, such as resource type or destination location. The grouping calculation base is determined by a grouping rule either directly

or dynamically using a condition. When you group charge types, the combined quantity of the charge items is used to calculate the

rate.

  Example

You use a weight scale to charge for transporting containers, and you create a grouping rule to group containers by destination

location. The system uses the combined weight of all containers going to the same location to calculate the collective rate, but

each individual weight is applied to the grouping rule.

The standard rate for a container is USD 1 per kg. The collective rate is USD 0.7 per kg if the combined weight is over 600 kg.

Each container going to one warehouse weighs 150 kg. However, the combined weight for five containers is 750 kg, so the

system charges the collective rate of USD 0.7 per kg instead of USD 1 per kg.

## Example

## Resolution Base

You have an FWO with 3 stages and want to calculate the transportation charges for the entire FWO, not for each stage. Therefore,

you specify the header as the calculation level. You want the system to calculate charge type BAF once in this FWO. Therefore, you

specify the resolution base as Root. This ensures that there is only one resulting row for the calculated calculation sheet in the

Charges tab page of the FWO. For more information about the Charges tab page, see Charges Overview.

You want the system to calculate charge type THC for each container in the FWO. Therefore, you specify the resolution base as

Container. If you ship three different containers, there are three resulting rows for the calculated calculation sheet – one for each

container.

The final sum adds the transportation charges in the four rows:

Row 1 for the BAF with amount a.

Sum of rows 2, 3, and 4 of THC with the following amounts:

b: Charge for container 1

b: Charge for container 2 (amount is the same as for container 1, because it has the same attributes)

c: Charge for container 3 (different than amount b because container 3 is bigger)

This is custom documentation. For more information, please visit SAP Help Portal.

189


1/14/26, 2:16 PM

Charges Overview

## Use

This function displays the results of the charge calculation on a Charges or an Internal Charges tab page for the following

business documents:

Forwarding Quotation

## Forwarding Order

Forwarding Settlement Document

Credit Memos

Freight Order

Freight Booking

## Service Order

## Freight Settlement Document

You can manually edit the charges on the Charges or the Internal Charges tab page.

## Prerequisites

In Customizing, you’ve carried out the activities for Transportation Management under  Basic Functions

## Charge

Calculation .

You have set up the master data for the Charge Management and Service Product Catalogs component. For more

information, see Setup of MD for Charge Management and SP Catalogs.

You have triggered charge calculation for the respective business document.

## Features

You can see the calculation date with a timestamp that specifies the date, time, and zone. You can use the timestamp for

agreement validity, agreement item validity, calculation sheet line item validity, and rate table validity. Note that only in newly

created business documents, you can see the timestamps.

The system displays the charge calculation results in a hierarchical table consisting of charge items and charge lines. The charge

items and charge lines correspond to the level at which the system determined the agreement and calculation sheets (both kinds,

including local). For more information, see Overview of Charges Grid.

## Charge Calculation Logs

You can see the details of how the system calculated the charges on the Charge Analysis Log tab page. The system re-creates

these details each time you trigger charge calculation for the business document. You can access all messages generated by the

system during charge calculation on the Charge Calculation Log tab page.

You can turn off or turn on the charge calculation logs for your user profile. You control this setting using the transaction SU3. On

the Parameters tab page, if you specify X as the value for the parameter /SCMTMS/CLOG, the system turns on the charge

calculation logs. If you don’t specify any value for this parameter, the system turns off the charge calculation logs.

## Charges Default View

This is custom documentation. For more information, please visit SAP Help Portal.

190


1/14/26, 2:16 PM

You can choose whether you want the system to display an expanded view or a collapsed view of the charge items as the default

view.

In order to make this setting, in the business document, you choose

. A dialog box appears in which you can select or deselect

the Expand Charge Items checkbox. Changes to settings have an immediate effect.

## Grouped View

You can view charge lines with the Container resolution base, grouped into aggregated rows, if the charge lines have the following

attributes in common:

Charge type

Equipment type

Rate amount

## Rate currency

Similarly, you can view charge lines with the Package resolution base, grouped into aggregated rows, if the charge lines have the

following attributes in common:

Charge type

Package type

Rate amount

## Rate currency

The system totals the final amount, calculated amount, and group count for all of the grouped charge lines. You can expand the

aggregated row to display the individual charge lines.

Note that if you change the rate amount or rate currency at the aggregated level, the system changes the rate amount for all the

charge lines in the group. For example, if you change the rate amount and rate currency from USD 20 to EUR 25 at the aggregated

level, the system passes the change down to all the charge lines in this group.

You can specify that you want the system to group the charge lines by default in the Customizing activity for the respective

business document. If you don’t specify this in the Customizing activity for the respective business document, the system checks

if there’s a default view specified in Customizing for Transportation Management under  Basic Functions

 Charge Calculation

## Basic Settings

 Define Charges Profiles .

If you specify a default view in both the general settings and in the settings for a specific business document type, the business

document settings take precedence. However, if you don’t specify a default view, the system doesn’t group the charge lines by

default.

## Charge Line Insertion

You can insert blank charge lines one at a time or insert one or more charge lines with the charge type already specified. When

inserting charge lines with specific charge types, you can filter by the following attributes:

## Charge type

Charge subcategory

Charge category

## Positive/Negative

This is custom documentation. For more information, please visit SAP Help Portal.

191


1/14/26, 2:16 PM

Value type

## Description

Inserted charge lines inherit the calculation resolution base and group type of the charge line you inserted them from. If you insert

charge lines from the charge item or the aggregated row of a group, the inserted charge lines inherit the ROOT calculation

resolution base and the group type is blank. You can change the group type of inserted charge lines.

  Note

If you change the group type of an inserted charge line, the system doesn’t group this charge line into the same aggregated row

as the charge line you inserted it from. This is because the inserted charge line and the charge line you inserted it from no

longer have the same equipment-type attribute.

## Show/Hide Access Sequence

If the instruction type is Line Item Selection, the system evaluates the line to be considered for the calculation among a set of two

or more lines. This evaluation is based on the highest or the lowest value of the affected lines, and on the access sequence.

If you set the operation to High, for example, the most expensive charge item remains and the cheaper charge items are

deactivated.

In general, the system displays only the charge lines used for charge calculation in case of access sequence. However, you can use

this button to view the access sequence of all the evaluated charge items.

## Reset Charges

You can revert the manual changes you made to the charge calculation results. When you reset charges, the system follows the

usual agreement determination process and performs charge calculation.

Note that when you reset charges, all the manual changes you made to the charge calculation results will be lost.

## Local Currency

During internal charge calculation, the system determines the local currency from the currency of the sales organization.

## Selective Copy of Charges

You can choose to exclude specific logistics items from the copy process such as, service items or packages when you copy a

forwarding order. When you exclude some of the logistics items and copy a forwarding order, the system recalculates the charges

and updates the charges accordingly in the new forwarding order. For more information on charge calculation, see Standard

Charge Calculation.

More Information

Charge Calculation

Overview of Charges Grid

## Use

In the following business documents, the result of a charge calculation is stored in a hierarchical table on the Charges tab page and

the Internal Charges tab page:

This is custom documentation. For more information, please visit SAP Help Portal.

192


1/14/26, 2:16 PM

Forwarding Quotation

## Forwarding Order

Forwarding Settlement Document

Credit Memos

Freight Order

Freight Booking

## Service Order

## Freight Settlement Document

The charge items and charge lines in the hierarchical table correspond to the level at which the system determines the agreement

and calculation sheets (both kinds, including local). The system specifies various attributes corresponding to the charge lines and

charge items in this table.

## Features

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

The following table lists the important attributes of charge lines and charge items and the corresponding descriptions:

Attribute

Description

## Charge hierarchy

The charges grid has a sum line, charge items, and charge lines.

Sum line is an initial mandatory line, which you can’t delete. All the charge lines and charge items are

part of this sum line. A charge item is a line item of a sum line. There can be more than one charge line

depending on the calculation level (header, item, or stage).

The charge line is a line item of a charge item. There can be more than one charge line for a charge

item depending on various criteria such as, charge type and resolution base.

## Execution-based charge item

In trailer-based and truck-based settlement scenarios, the system selects this checkbox in forwarding

orders. Selection of this checkbox indicates that the system doesn’t calculate charges in the

forwarding order. The system creates the charge items and displays them for reference purposes.

## Actions

The system displays an icon in the Actions field when you insert a charge line.

You can use this icon to manually insert consecutive charge lines after this charge line.

Note that in rate split scenario, you can use this button to split the charge lines in the freight booking.

For more information, see Rate Split.

## Calculation status

The system indicates the status of charge calculation for a charge item or a charge line. The system

displays the following statuses:

No calculation error

Calculation warning

Calculation error

## Charge type and charge

Charge type is a classification of a charge line that helps determine how the system calculates the

description

transportation charges for the charge line. A few charge types available are as follows:

This is custom documentation. For more information, please visit SAP Help Portal.

193

Basic handling charges


1/14/26, 2:16 PM

Attribute

Description

Delivery charges

## Documentation charges

The system displays the description of the charge type in the Charge Description field.

Commodity code and

commodity code type

These fields display the commodity code item number and the commodity code type used for charge

calculation.

Commodity codes enable you to define the categories of products that the parties in the agreements

have agreed to transport between them. You can group commodity codes using a commodity code

type.

For more information on commodity codes, see Classification of Goods.

## Logistical reference

Logistical reference displays the item or stage information for a charge line (with the resolution base

of container, package, product, or stage) from which the system obtains the logistical data.

## Rate amount

Rate amount is the amount that is used as the basis for calculating the calculated amount for a

charge line. The system derives the rate amount from the master data. You can manually add or

change the rate amount directly on the charges screen area.

## Manually-changed rate amount

This field indicates whether a rate amount is changed manually.

When you manually change the rate amount, the system selects this checkbox.

Price unit, unit of measure, and

Price unit is the factor with which the system derives the calculated amount. The system derives the

quantity

price unit from the calculation rule you specify in the corresponding calculation sheet.

Unit of measure specifies the unit of measure of the price unit.

Quantity specifies the quantity used for calculating the charge amount.

  Note

When you don’t specify any calculation rule, the rate amount and the calculated amounts are the

same.

  Example

You have a forwarding order with the following data:

Rate amount – USD 10

## Quantity – 1000 kg

If you specify a calculation rule in the calculation sheet with the price unit as per 100 kg, the

calculated amount is USD 100 (rate amount * quantity / price unit).

## Calculation base

Calculation base is the actual base or factor with which the system calculates the charges for the

scale.

There can be various scenarios in which the system must calculate a charge for different forms of

weights, for example, gross weight and net weight. In this case, both gross weight and net weight

correspond to the scale base Weight (W), whose dimension is mass. However, by definition, gross

weight and net weight are two entirely different charge aspects. Therefore, they have two different

calculation bases, such as W1 for gross weight and W2 for net weight.

To follow the scenario given here, you define a calculation base for every scale base. This calculation

base is the final element in the charge determination. This means that the calculation base is used to

determine the charges.

This is custom documentation. For more information, please visit SAP Help Portal.

194


1/14/26, 2:16 PM

Attribute

## Description

You can define calculation bases in Customizing for Transportation Management under  Basic

## Functions

 Charge Calculation

 Data Source Binding

 Define Calculation Bases .

## Calculated amount

Calculated amount is the amount that is used as the basis for calculating charges for a charge line.

The calculated amount is derived from the rate amount. Note that when you don’t specify any

calculation rule, the rate amount and the calculated amounts are the same.

## Ignore calculation rule

If you select this checkbox, the system ignores the calculation rule for the charge line you specified in

the relevant calculation sheet or rate table, and it doesn’t calculate the calculated amount. Instead, it

uses the rate amount as the calculated amount.

Note that the system deselects this checkbox by default. This checkbox is enabled only for charge

lines with a rate table.

For more information on calculation rules, see Rate Definition and Maintenance.

## Reference-from and reference-to

These fields specify the first and the last line numbers respectively of a reference range.

line numbers

  Note

If you enter a reference-from line number without entering a reference-to line number, the

system interprets this as a single reference percentage value. This means that the

percentage value only applies to the single charge item in the reference-from line.

If you enter a reference-to line number without entering a reference-from line number, the

system interprets this as a range starting from the first charge item to the charge item in

the reference-to line.

Items with the Sum and Subtotal instruction types aren’t considered in a reference range.

## Final amount

The amount that the system calculates based on the following:

Calculation rule

Calculation base

Calculated amount

Document currency

## Document currency

You can specify the document currency at agreement level. If you don’t specify a document currency

at agreement level, the system determines the document currency using the following hierarchy:

1. The currency specified for the business partner

2. The currency specified for the organizational unit function on the Org. Data tab page of the

organizational unit

3. The local currency specified in the general settings of the sales or purchasing organization

Note that for a single order freight term scenario, you must refer to the corresponding document.

You can specify the local currency for the business partner in the Define Business Partner app on the

fiori launchpad.

You can specify the local currency for the organizational unit in Customizing for Transportation

Management under  Master Data

 Organizational Model

 Change Organizational Model

.

You can specify the local currency in the general settings in Customizing for Transportation

Management under  Basic Functions

 Charge Calculation

 Basic Settings

 Define Charges

Profiles .

This is custom documentation. For more information, please visit SAP Help Portal.

195


1/14/26, 2:16 PM

Attribute

Description

## Exchange rate

Exchange rates are available at charge line level. You can get an overview of exchange rates on the

Exchange Rates or Calculated Amounts and Exchange Rates tab page. For example, you can see the

currencies, the type of currency conversion, and the exchange rate. If you enter different exchange

rates, the system recalculates the currency conversions. If you change the exchange rates at the sum

level, the system propagates the changes to all the charge items and charge lines under the sum level.

  Note

If you change the exchange rate at the charge item level, the system automatically updates all

relevant charge lines. If you change the exchange rate at the charge line level, the change only

affects that charge line.

If you manually change an exchange rate for a charge item, the system no longer automatically

updates the exchange rate at the charge item level. If you manually change an exchange rate for a

charge line, the system no longer automatically updates the charge line with changes made at the

charge item level.

## Statistical charge

This field indicates whether a charge line is for information only and isn’t a part of the total amount.

If you select this checkbox, on charge calculation, the system selects the Deactivated checkbox

automatically for the charge line. As a result, charge line amount isn’t included in the total amount.

## Deactivated

This field indicates whether a charge line is active or inactive.

## Charge item operation

If you select this checkbox, the charge line amount isn’t included in the total amount.

The system automatically deactivates a charge line when you select the Statistical Charge checkbox

for a charge line.

## Payer

The system displays whether a charge line is relevant for a prepaid party or collect party.

## Charge item operation

This field indicates how the system determines which charge item to include during charge

calculation.

You use this value in combination with the Line Item Selection instruction type.

If you set the charge type to Line Item Selection and the operation to Highest Value. The system

selects the most expensive charge line under it.

Access sequence selects the first charge line that has been calculated successfully.

Charge calculation base,

These fields specify the details of quantitative calculation bases (measurable calculation bases such

chargeable quantity, and unit of

as volume and weight) used for rate determination. You can manually change the chargeable quantity

measure

used for rate determination.

Note that the charge line must have a rate table with scales of different dimensions for the system to

calculate charges.

More Information

## Charges Overview

## Invoicing Status of Freight Documents using Lean Services

The invoicing status in a freight document tells you the status of the posting of accruals and invoice verification for a

transportation charge. You can see the invoicing status of a freight document in the charges grid at the charge element level.

This is custom documentation. For more information, please visit SAP Help Portal.

196


1/14/26, 2:16 PM

When you create a freight document, the invoicing status is Not Ready for Posting. If the system calculates the charges

successfully, the status is set to Ready for Confirmation based on the event reported in the freight order, freight booking, or

consignment order. For more information on events, see Freight Cost Confirmation and Posting.

You can use the Monitor Freight Documents for Accrual app to monitor your freight documents to post accruals. When your

freight documents are at the invoicing status Ready for Confirmation and you've verified that the planned costs are correct, you

can confirm the transportation charges for posting to Financial Accounting.

The following invoicing statuses are available:

Invoicing Status

Not Ready for Posting

Ready for Confirmation

Ready for Posting

## Posted

Invoice Verified

Posting Failed

## Description

The charge element is newly created, and the checkout event or an

equivalent event isn’t reported. This indicates posting of freight

cost isn't initiated.

After the relevant checkout event or an equivalent event is reported

charges are successfully calculated, then the charges are ready to

be confirmed. After you confirm the charges, the system initiates

the posting for accruals.

The charges are confirmed and are ready for posting of accruals.

Charges are posted for accruals.

Charges are posted and invoice is received and verified.

The charge element was posted for accruals but failed due to some

reason.

## Transition of Invoicing Status

The following table shows the various scenarios for charge elements explaining the status transition of the freight documents :

  Note

You can't change any freight document, charge item, or charge element with the status Invoice Verified.

## Scenario

Current Status

## Next Status

Initial charge calculation isn't done and

Not Ready for Posting

## Not Ready for Posting

Checkout/Departure event not reported

Initial charge calculation is done and

Not Ready for Posting

## Ready for Confirmation

Checkout/Departure event is reported

Checkout / Shipped on Board / Uplift

Not Ready for Posting

## Ready for Confirmation

Confirmed event reported in the execution

tab

The event Checkout is already reported in

Ready for Confirmation

## Not Ready for Posting

the freight document and then Not

## Checkout event is reported

Posting is triggered using Confirm Posting

Ready for Confirmation

## Ready for Posting

This is custom documentation. For more information, please visit SAP Help Portal.

197


1/14/26, 2:16 PM

## Scenario

## Current Status

When the freight cost posting to Material

## Ready for Posting

Management (MM) is successful

Next Status

## Posted

When the freight cost posting to MM failed

Ready for Posting

## Posting Failed

When freight document in Ready for

Ready for Posting

## Ready for Confirmation

Posting status undergoes changes in

charges

A freight document with the status Ready

Ready for Posting

## Not Ready for Posting

for Posting undergoes changes in charges

and Not Checkout event is reported

When you resolve the errors that led to

Posting Failed

## Posted

Posting Failed and post the freight

document again

You do Cancel Posting on the Posting

Posting Failed

## Not Ready for Posting

Failed document and Not Checkout event

is reported

When the invoice is processed for the

## Posted

Invoice Verified

## Posted freight document

When freight document is Posted and FSD

## Posted

## Posting Failed

is created, but Purchase Order (PO) and

Service Entry Sheet (SES) creation failed

When you do Cancel Posting on the Posted

## Posted

## Not Ready for Posting

freight document for which Not Checkout

event is reported

When you do Cancel Posting on the Posted

## Posted

## Ready for Posting

freight document for which accrual is

confirmed

When invoice is reversed by MM

Invoice Verified

## Posted

When freight document status is Posting

Posting Failed

## Ready for Posting

Failed, FSD is created, but PO and SES

creation failed and FSD is canceled.

The following table explains the transition, if there are changes to any charges in the charge element:

## Scenario

Current Status

## Next Status/Impact

Changes to any charge element

Not Ready for Posting

## No impact

This is custom documentation. For more information, please visit SAP Help Portal.

198


1/14/26, 2:16 PM

## Scenario

Current Status

## Next Status/Impact

Any change in the amount or charge

Status can be either of the following:

## Ready for Confirmation

element is activated/deactivated. Note that

the updated amount isn't zero.

When you update the charge amount to

zero

Ready for Confirmation

Posting Failed

Ready for Posting

## Posted

Not Ready for Posting

## Not Ready for Posting

Add a new charge element with non-zero

## Not Ready for Posting

If Checkout/Departure event is reported,

amount.

Add a new charge element with zero

amount

then status is Ready for Confirmation.

If Checkout/ Departure isn't reported, then

status is Not Ready for Posting.

## Not Ready for Posting

Calculation status of the charge element

## Not Ready for Posting

If Checkout/Departure event is reported,

has errors, but you resolve the errors

then status is Ready for Confirmation.

If Checkout/ Departure isn't reported, then

status is Not Ready for Posting.

  Note
You can't delete a charge element when it has the following status:

Posting Failed

## Posted

Invoice Verified

## Invoicing Status Roll-up

The invoicing status at the charge element level is rolled up to charge item level and then to the charges header level. This provides

an overall invoicing status at the charges header and item level.Roll-up is essential so that freight documents are picked based on

the status Ready for Confirmation to perform initial posting or to execute the changes.

There can be various scenarios where multiple charge items are created like stage level calculation, additional agreement party,

service based charges and so on. In all the cases, the invoicing status is rolled-up from the charge elements to the corresponding

charge items and then to the charges header level. For roll-up, the priority of invoicing status is as follows:

1. Ready for Confirmation

2. Posting Failed

3. Ready for Posting

4. Posted

5. Invoice Verified

6. Not Ready for Posting

This is custom documentation. For more information, please visit SAP Help Portal.

199


1/14/26, 2:16 PM

Calculation Methods

## Use

This function enables the system to calculate transportation charges according to a specific logic, for example, by considering the

break-weight or the deficit weight. You specify a calculation method for each charge type when defining a calculation sheet or a

local calculation sheet. The system applies the calculation method when calculating the charges for the charge type.

## Integration

You specify a calculation method for each charge type when defining a calculation sheet or a local calculation sheet.

This function is used in the charge calculation process (see Charge Calculation).

## Prerequisites

You have defined calculation methods in Customizing for Transportation Management under  Basic Functions

## Charge

## Calculation

 Enhancements to Charge Calculation Engine

 Define Calculation Methods .

## Features

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

## Calculation Method Types

You can choose the type of calculation method to use for each charge type. If you don’t choose the type of calculation method, the

system uses the standard calculation method.

The following calculation method types are available in Transportation Management (TM):

## Standard

The system calculates the transportation charges based on the specified rate, calculation rule, and actual weight. For

example, the rate is USD 10 and the calculation rule specifies that the rate is for every 100 kg. The weight is 1800 kg, so the

system calculates the transportation charges as USD 180 (1800 kg/100 kg * USD 10).

## Break-Weight

The system calculates the transportation charges by comparing and selecting the lower rate from either the actual rate

range or the lower end of the next rate range. Break-weight is the weight from which it’s cheaper to calculate the rate as

opposed to the actual weight of the goods to be transported. One of the scales in the rate must be weight.

  Example

You’re shipping 490 kg and are using the following break-weights and rates:

Weight Scale

## Rate

>= 100 kg

USD 10 per kg

>= 500 kg

USD 8 per kg

>= 1000 kg

## USD 6 per kg

This is custom documentation. For more information, please visit SAP Help Portal.

200


1/14/26, 2:16 PM

Using the standard calculation method, the system calculates the transportation charges as USD 4900 (490 kg * USD

10).

Using the break-weight calculation method, the system checks if it’s cheaper to use the rate for the original rate range

(USD 10 per kg for >=100 kg) or the next rate range (USD 8 per kg for >=500 kg). Since the next rate range is cheaper,

the system considers the 490 kg as being >= 500 kg and calculates the transportation charges as USD 4000 (500 kg *

USD 8).

## Clipping

The system calculates the transportation charges by working through all scales level-by-level, even if the value lies outside

the scale. The system then totals up the calculation results from each scale level to produce the overall result. For clipping,

one scale item must have a relative calculation type.

  Example

The scale levels are defined with the following values:

Up to 5 tons: USD 50 absolute

Up to 7 tons: USD 14 per ton

Up to 10 tons: USD 13 per ton

## Up to 15 tons: USD 12 per ton

Using the clipping calculation method for a load weighing 12 tons, the system calculates the transportation charges as

follows:

5 tons at USD 50 = USD 50 (first scale level)

2 tons at USD 14 per ton = USD 28 (up to the second scale level)

3 tons at USD 13 per ton = USD 39 (up to the third scale level)

2 tons at USD 12 per ton = USD 24 (remainder in the fourth scale level)

This results in a charge of USD 141. If you don’t use the clipping calculation method, the 12 tons fall into the "up to 15

tons" scale level and the transportation charge is USD 12 per ton, resulting in a charge of USD 144.

## Deficit weight rating

The system calculates the transportation charges for a weight greater than the actual weight of the goods to be

transported, if it results in a lower transportation charge. The system calculates the difference between the actual weight

and the next scale level and adds this difference to the goods to be transported as a deficit weight. The system then

calculates the costs for the deficit weight using the cheaper rate. Deficit weight rating (DWR) is primarily used in U.S. land

transportation.

  Example
You’re shipping two freight classes with different rates. For 500 kg of freight class A, the rates are as follows:

Weight Scale

## Rate

< 1000 kg

USD 1.50 per kg

>= 1000 kg

## USD 1 per kg

For 400 kg of freight class B, the rates are as follows:

This is custom documentation. For more information, please visit SAP Help Portal.

201


1/14/26, 2:16 PM

Weight Scale

## Rate

< 1000 kg

USD 2.50 per kg

>= 1000 kg

## USD 2 per kg

Using the standard calculation method, the system calculates the transportation charges as USD 750 for freight class A

(500 kg * USD 1.50) and USD 1000 for freight class B (400 kg * USD 2.50). The total charge is USD 1750.

Using the DWR calculation method, the system adds 100 kg to the actual weight to bring it to 1000 kg for both freight

classes. The system then calculates the transportation charges as USD 500 for freight class A (500 kg * USD 1) and

USD 800 for freight class B (400 kg * USD 2). The system calculates the deficit weight using the lowest rate, resulting in

a charge of USD 100 (100 kg * USD 1). The total charge is USD 1400.

## External system

The system connects to an external system to determine the rates.

## Internal charge calculation

The system can calculate transportation charges between organizations of the same company code and between

organizations of different company codes. You can use internal agreements for internal charge calculation between two

different business units and between business units and gateways. Using internal agreements between business units and

gateways, you can maintain the contract between the different organizations that belong to the same company code or

different company. You can calculate the external freight charges for each stage or combination of stages in freight orders

or freight bookings. During internal charge calculation of a forwarding order, the external freight charges for each stage or

combination of stages that belong to the same freight order and freight booking appear in the corresponding forwarding

orders. The system can’t consolidate charges for two or more stages of the same forwarding order if these stages belong to

different freight orders or freight bookings. Note that you can create an internal settlement document only between a

business unit and a gateway.

If the involved business units and gateway belong to different organizations of the same company code, you perform

intracompany settlement. If the involved business units and gateway belong to the organizations of different company

codes, you perform intercompany settlement.

For more information, see Internal Settlement Management.

## Air freight: standard rating

Depending on the rate type, the system calculates the air freight transportation charges based on TACT rates or contract

rates. The system uses a combination of the clipping and break-weight calculation methods to calculate the charges using

unit load device (ULD) rates. The system uses the standard rate determination process for general cargo rates (GCRs) and

specific commodity rates (SCRs).

## Air freight: break-weight rating

Depending on the rate type, the system calculates the air freight transportation charges based on TACT rates or contract

rates. The system uses a combination of the clipping and break-weight calculation methods to calculate the charges using

ULD rates. The system uses the break-weight determination process for GCRs and SCRs. The break-weight calculation

method for air freight compares the higher weight break charges with the sum of lower weight break charges and the over-

pivot charges and chooses the minimum rate. The system compares the weight breaks for ULD rates, GCRs, and SCRs

using a greater-than scale.

## Fuel surcharge calculation

You can calculate the fuel surcharge using the calculation method FUEL_SURCHARGE. For more information, see Fuel

Surcharge Calculation.

This is custom documentation. For more information, please visit SAP Help Portal.

202


1/14/26, 2:16 PM

## Cost pull

You can transfer distributed external costs from the freight side to the forwarding side, and use the costs as a basis for

settling with a customer or an internal organization. To transfer the result of a cost distribution from the freight side to the

forwarding side, you use an instruction type of Cost at the item level. The system automatically includes an internal charge

calculation method type, and the cost pull calculation method COST_PULL. For more information, see Cost Pull.

## Calculation Method Modeling

You can model your own calculation method types instead of choosing a calculation method type supplied by TM. Each calculation

method type is realized as an implementation of the interface Calculation Methods Interface

(/SCMTMS/IF_TC_CALC_METHODS). You can override the implementations of the calculation method types with customer-

specific implementations.

Calculation Profiles

## Use

This function provides a central location to define the settings that you want the system to use when calculating transportation

charges.

## Integration

This function is used in the charge calculation process. For more information, see Charge Calculation.

## Features

The following are examples of settings you can define in a calculation profile:

Specify the calculation date type that is used as the basis for the rate and agreement validity during charge calculation.

For example, the order date, the invoice date, or the expected end date of the main carriage.

Specify the exchange rate date type that is used as the basis for exchange rates during charge calculation.

Specify the level at which the system calculates the charges, for example, at header level, item level, or stage level.

The system can calculate charges for an agreement item at header level even when calculating the rest of the charges at

stage level. To enable header-level charges when calculating charges at stage level, the calculation level must be stage level.

Specify the determination rule that the system uses to determine the agreement and the calculation sheet (both kinds,

including local).

Specify a single rate, known as a through rate, for multiple stages of a transportation route.

Specify the default dimensional weight profile for the organizational unit and the condition that the system uses to

determine the dimensional weight profile.

Specify the exchange rate type the system uses for currency conversion during the charge calculation process.

Specify the source of the data that the system uses for charge calculation and invoicing, for example, actual route, ordered

route, or actual and ordered route.

If you use the actual route, the system uses actual route information. If you use the ordered route, the system uses ordered

route information from forwarding orders.

This is custom documentation. For more information, please visit SAP Help Portal.

203


1/14/26, 2:16 PM

Once you’ve defined the settings, you can assign the calculation profile to an organizational unit or a business partner role.

  Note

If you assign a calculation profile to an organizational unit and to a business partner role, the system applies the calculation

profile for the business partner role.

## Activities

You can define calculation profiles in Customizing for Transportation Management under  Basic Functions

 Charge Calculation

## Basic Settings

 Define Calculation Profiles .

You can assign a calculation profile to an organizational unit in Customizing for Transportation Management under  Basic

## Functions

 Charge Calculation

## Basic Settings

 Define Charges Profiles . You can specify both a sales calculation profile and

a purchasing calculation profile if the organizational unit is a forwarding house. You can also assign a calculation profile to a

business partner with one of the following roles:

Sold-to party

Ship-to party

Carrier

## Vendor

You can assign a calculation profile to business partner roles in the Define Business Partner app on the fiori launchpad. You can

assign a calculation profile on the Customer Org. Data tab page of the business partner role. Here you can define individual

profiles for each organizational unit of the business partner.

## Charges Templates

You use charges templates when a valid freight agreement between the business parties, for example the purchasing organization

and carrier, is missing. Charges templates are freight agreements without carriers that contain the possible charge types for the

respective business processes of the freight documents (freight orders and freight bookings).

## Use

You can use a charges template in the following scenarios:

## Agreement is under negotiation

When the parties are yet to finalize the charges and the rates for a transportation order, they can use a charges template to

understand the possible charge types that are required and relevant for the transportation order.

## Spot tendering

In spot tendering, the carrier assignment is done on the spot and there's no possibility to have an agreement with the

carrier. In this case, the shipper uses a charges template to propose the valid charge types for the business and the charge

amount can be manually entered in the freight document.

## Mass creation of freight agreements

For ocean freight bookings, a shipper can create multiple agreements based on charges templates.

Validation of charge types based on the business process of the carrier

This is custom documentation. For more information, please visit SAP Help Portal.

204


1/14/26, 2:16 PM

You can use a charges template where you want to restrict the charge types based on the transportation mode or shipping

type of the carrier. For example, if a carrier transports road freights, then they can see the charge types relevant only for the

transportation mode Road and not for Rail or Sea.

## Prerequisites

You've selected the Carrier Optional checkbox in Customizing for Transportation Management under  Master Data

## Agreements and Service Products

Define Freight Agreement Types , to use a freight agreement as charges

template.

You've assigned transportation mode and shipping type in Customizing for Transportation Management under  Master

## Data

Basic Functions

Charge Calculations

Basic Settings

Define Charge Types .

## Features

The following details are mandatory:

Validity period

## Description

Purchasing organization

Transportation mode

## Shipping type

Manual charges are always allowed, so the Manual Charge Item checkbox is always selected.

When you manually add charges in the charges grid of the freight document, the system validates the transportation mode

and shipping type of the charge type with that of the freight document.

For example, when you add unplanned charges to a charges template, the system validates whether the unplanned charges

are relevant for the transportation mode and shipping type of the freight document.

If the charge type has no transportation mode or shipping type assigned to it, then the charge type is valid for all

transportation modes and shipping types.

When you add a calculation sheet or local calculation sheet to a charges template, the system validates the transportation

mode and shipping type of the charge type in the calculation sheet or local calculation sheet with that of the freight

agreement header or items.

Rates (rate table or flat rate) are optional.

During charge calculation, the system first tries to determine a freight agreement between the business parties. If there

isn't a freight agreement, the system determines a charges template based on the business organization, for example, the

purchasing organization.

## Related Information

Agreement and Calculation Sheet Determination

Rate Determination

External Agreements

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

205


1/14/26, 2:16 PM

This function allows Transportation Management (TM) to use agreements stored in an external system when calculating

transportation charges. When processing the calculation sheet (both kinds, including local) and checking the relevant rates, the

TM system connects to the external system to determine the rates. TM can obtain accurate rates or estimated rates from the

external system, depending on whether you specify the reference number of the external system's agreement.

## Integration

This function is used in the charge calculation process, which is used in the following TM components:

Forwarding Order Management

Freight Order Management

Forwarding Settlement

## Freight Settlement

For more information about the standard charge calculation process, see Standard Charge Calculation.

## Prerequisites

To use this function, you’ve established a connection from TM to the external system by configuring the following settings:

You have integrated Web services into your TM system.

You’ve defined the bindings or logical ports for the Web service by using transaction SOAMANAGER.

You’ve defined your user access by using transaction SE38 and executing the report Secure Store Logon for SMC3

(/SCMTMS/TCC_SEC_STORE_LOGON).

You’ve created a material freight group in Customizing for Transportation Management under  Master Data

 Transportation Network

 Transportation Lane

## Carrier Profile

 Define Material Freight Groups .

You’ve created a freight code set with freight codes and assigned the freight codes to the material freight group in

Customizing for Transportation Management under  Master Data

 Transportation Network

 Transportation Lane

## Carrier Profile

 Define Freight Code Sets, Freight Codes, and Determination .

You’ve defined the connection parameters and charge types and mapped the external system's parameters to the

calculation bases in TM by using transaction SM34 and accessing the /SCMTMS/VC_SMC3 view cluster.

## Activities

To use an agreement stored in an external system, enter External System in the Calculation Method Type field of the agreement's

calculation sheet (both kinds, including local).

To obtain accurate rates from the external system, in the agreement specify the reference number of the external system's

agreement.

To obtain estimated rates from the external system, don’t specify the reference number of the external system's agreement.

More Information

## Agreement

## Calculation Sheet

This is custom documentation. For more information, please visit SAP Help Portal.

206


1/14/26, 2:16 PM

Agreement and Calculation Sheet Determination

## Use

Transportation Management (TM) enables you to create agreements between business partners and sales groups or sales

organizations. Agreements are integrated with calculation sheets and rate tables (both kinds, including local) to enable the system

to calculate charges. During charge calculation, the system determines the most appropriate agreement, and thereby the

calculation sheet (both kinds, including local), in order to determine a rate.

The system determines the agreement within organizational hierarchies (such as company organization or corporate

organization) based on the following:

## Business partner

Organizational unit (sales organization for forwarding agreements and purchasing organization for freight agreements)

## Organizational unit hierarchy

If the system doesn’t find an agreement between the business partner and sales group, it determines an agreement between the

business partner and sales organization.

If the system finds multiple agreements between a business partner and a sales organization, the system does one among the

following based on the agreement determination type:

The system finds the final amounts for all the agreement items and chooses the agreement item with the minimum final

amount for charge calculation.

The system finds the final amounts for all the agreement items and chooses the agreement item with the maximum final

amount for charge calculation.

The system displays all the agreements from which you can select an agreement for charge calculation.

  Note

In the following scenarios, the system may not display all agreements even when you specify the agreement

determination type as Display All Agreements:

If you select the Eval. All Agreements checkbox in Customizing for Transportation Management under  Basic

## Functions

 Charge Calculation

## Basic Settings

## Define Charges Profiles , the system displays agreements

or agreement items based on the leading charge type. If the charge item has one or more agreement or

agreement items with a leading charge type, the system displays only the agreements or agreement items with a

leading charge type. If the charge item has agreement or agreement items without a leading charge type, the

system displays all the relevant agreements and agreement items.

If you enable automatic charge calculation for forwarding orders and freight orders, the system doesn’t

determine multiple agreements. Instead, the system sets the calculation status as Automatic Charge

Calculation Failed.

If you trigger charge calculation from a personal object worklist (POWL) or if you perform batch charge

calculation with the agreement determination type as Display All Agreements, the system doesn’t calculate

charges. Also, the system sets the calculation status as Automatic Charge Calculation Failed.

You specify an agreement determination type in Customizing for Transportation Management under  Basic Functions

## Charge

Calculation

## Basic Settings

 Define Calculation Profiles . If you don’t specify an agreement determination type, the system

doesn’t consider the agreement determination type for charge calculation and follows the standard agreement determination

process.

This is custom documentation. For more information, please visit SAP Help Portal.

207


1/14/26, 2:16 PM

Once the system determines an agreement, it determines a calculation sheet (both kinds, including local) based on various

attributes specified in the forwarding order or freight order such as, shipping type and stage category. If you haven’t specified any

attribute in the forwarding order, the system arbitrarily determines a calculation sheet (both kinds, including local) for charge

calculation.

## Integration

The system determines agreements and calculation sheets (both kinds, including local) during charge calculation. For more

information, see Charge Calculation.

## Prerequisites

You have set up the master data for the Charge Management and Service Product Catalogs component. For more information, see

Setup of MD for Charge Management and SP Catalogs.

## Features

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

The agreement and calculation sheet determination process can slightly differ from the usual way when you specify additional

attributes in the agreement, forwarding order, freight order, or calculation profile. The system then determines the most

appropriate agreement and calculation sheet based on the following:

## Leading charge type

The system takes the leading charge type into account by skipping agreements that use calculation sheets without a

leading charge type. The system then skips agreements if the leading charge type doesn’t have a rate. If there are multiple

leading charge types in a calculation sheet, all the leading charge types must have a rate defined for the system to consider

the agreement and calculation sheet for charge calculation. We recommend that you maintain a single leading charge type

in a calculation sheet.

To allow the system to take leading charge type into account, select the Eval. All Agreements checkbox in Customizing for

Transportation Management under  Basic Functions

 Charge Calculation

## Basic Settings

 Define Charges Profiles .

## Incoterms

In forwarding orders with Incoterms, the system determines the charges from the calculation sheet item based on the

Incoterm and the payer role. For the system to be able to determine a calculation sheet item for charge calculation, the

Incoterm and the payer role specified in the forwarding order must match the Incoterm and payer role specified in the

calculation sheet item. The system then adds a charge line to the forwarding order. For more information, see Incoterms in

Forwarding Orders.

## Manually-specified agreement

You can specify a freight agreement or freight agreement item for a freight order stage. The system calculates the charges

based on the specified freight agreement or freight agreement item and doesn’t determine any other agreement.

## Default route

You can specify a default route in a forwarding order and a list of default routes at the agreement-item level. If the default

route specified in a forwarding order or freight order matches one of the default routes specified in an agreement item, the

system uses the calculation sheet associated with the agreement item during charge calculation.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

208


1/14/26, 2:16 PM

You can also specify a blank default route in the agreement item. For a forwarding order with or without default route,

the system may select this agreement item for charge calculation.

## Stage type

You can specify a stage type for a stage in a forwarding order or freight order and also in an agreement item. If the stage

type specified in a forwarding order or freight order stage matches the stage type specified in an agreement item, the

system uses the calculation sheet associated with the agreement item during charge calculation.

## Resource ownership type

You can specify a resource ownership type for a resource item in a forwarding order or freight order and also in an

agreement. If the ownership type specified in a forwarding order or freight order matches the ownership type specified in

an agreement item, the system uses the calculation sheet associated with the agreement item during charge calculation.

## Forwarding agreement quotation

In scenarios such as forwarding agreement quotation, you may want the system to determine agreements of all validity

periods including expired agreements and service products.

To enable this, you must set the parameter SEL_SP as X in the back-end and deselect the Eval. All Agreements checkbox

in the Define Charges Profiles Customizing activity.

For more information this scenario, see Rate Determination of Forwarding Agreement Quotation Items.

  Note

If you’re using an agreement stored in an external system, you can establish a connection from TM to the external system. The

system displays the external agreement and the freight agreement item number on the  Charges

 Details  tab page. For

more information, see External Agreements.

You use internal agreements to maintain the contract between the different organizations that belong to the same company

code or different company code. For more information, see Internal Settlement Management.

More Information

Agreement Maintenance

Calculation Sheet Maintenance

## Rate Definition and Maintenance

Freight Agreement Determination of Freight Bookings for Stage
## Invoicing Carriers

For freight bookings, when you've enabled invoicing carrier and stage invoicing carrier at stage level, the system determines the

freight agreement for each stage level invoicing carrier and the subsequent charge calculation and payment are settled for the

individual invoicing carriers. Along with the stage-level invoicing carrier, freight agreement determination is based on the

transportation mode, shipping type, and other mandatory attributes, such as validity period and involved parties.

In a freight booking, if you specify Stage Invoicing Carrier Level as Header Carrier, the system determines the valid agreement

based on the carrier, transportation mode, and shipping type at the header level and settles the final charges with the respective

header carrier.

This is custom documentation. For more information, please visit SAP Help Portal.

209


1/14/26, 2:16 PM

If you've specified Stage Invoicing Carrier Level as Stage Carrier, then the system determines the valid agreement based on the

invoicing carrier, and the transportation mode and shipping type for that stage (pre-carriage, main carriage, and on-carriage). The

system settles the final charges with the respective stage invoicing carrier.

For more information, see Freight Settlement.

You can see the freight charges for the stage invoicing carrier and the header carrier on the Charges tab of the freight booking. For

more information on freight agreements, see Agreement.

  Note

Transportation mode and shipping type are mandatory attributes of a freight agreement. The system determines a freight

agreement for a freight booking based on the appropriate transportation mode and shipping along with other mandatory

attributes, for example lifecycle status as Released.

## Prerequisites

You've assigned the appropriate Application Configuration Settings in the Customizing for Transportation Management

under  Freight Order Management

## Freight Booking

## Define Freight Booking Types . Assign

/SCMTMS/FRE_BOOK_OCEAN_ES for ocean freight bookings and /SCMTMS/FRE_BOOK_AIR_ES for air freight

bookings.

You've defined a freight agreement with transportation mode and shipping type that matches with the transportation mode

and shipping type of the stage that you assign to the invoicing carrier in the freight booking.

For a freight booking, you’ve made the following settings:

Assigned a transportation mode and shipping type for the header and each stage of the freight booking.

Entered the Stage Invoicing Carrier Level as Stage or Header on the Stages tab of the freight booking.

Assigned an invoicing carrier to each stage of the freight booking.

## Features

Freight agreement determination without shipping type in the stage of a freight booking

When you don’t assign shipping type for a particular stage, the system determines the freight agreement with the

transportation mode for the stage invoicing carrier. If there’s no such freight agreement, the system determines the freight

agreement based on the header-level transportation mode and shipping type.

Agreement determination without transportation mode and shipping type in the stage of a freight booking

If you don’t assign transportation mode and shipping type to a stage, the system determines the freight agreement based

on the header-level transportation mode and shipping type for the invoicing carrier. If there's no such freight agreement,

the system can't determine a freight agreement for the stage.

Same freight agreement determination for freight order or freight booking based on carrier, transportation mode, and

shipping type

While determining a freight agreement whether for a freight order or freight booking (stage-level), the system checks the

combination of the carrier, transportation mode, and shipping type and picks the same agreement for a freight order or

freight booking (stage-level) that matches that combination. This ensures that you don't create multiple freight

agreements with the same carrier, transportation mode, and shipping type.

## Example

This is custom documentation. For more information, please visit SAP Help Portal.

210


1/14/26, 2:16 PM

You've created an ocean freight booking with multiple stages and the following values for transportation mode, shipping type, and

carrier:

## Freight Booking

Transportation Mode Shipping Type

Header Carrier

Freight_Booking

Sea

FCL

## Main_Carrier

You've also created a freight order with the following transportation mode and shipping type:

## Freight Order

Transportation Mode Shipping Type

Freight_Order

Road

FTL

The freight booking Freight_Booking has multiple stages and the following values for transportation mode, shipping type, and

carrier:

## Stages

Transportation Mode

Shipping Type

Invoicing Carrier

Stage Invoicing Carrier

Stage1

Stage2

Stage3

Stage4

Road

Sea

Road

N/A

FTL

FCL

N/A

N/A

Carrier1

Carrier2

Carrier3

Carrier3

Level

Stage

Stage

Stage

## Stage

You've created and released the freight agreements with the following values for transportation mode, shipping type, and carrier:

Freight Agreement

## Carrier

Transportation Mode Shipping Type

Agr1

Agr2

Agr3

Agr4

Agr5

Carrier1

Carrier2

Main_Carrier

Carrier3

Carrier3

Road

Sea

Sea

Road

Sea

FTL

FCL

FCL

FTL

FCL

During charge calculation for the freight booking, the system determines the following freight agreements for the header and

stage level:

## Header level and header carrier Main_Carrier

The system determines agreement AGR3 because the transportation mode and shipping type of AGR3 match with the

transportation mode and shipping type at the header-level of the freight booking.

Stage1 and invoicing carrier Carrier1

The system determines freight agreement AGR1 because the transportation mode and shipping type of AGR1 match with

the transportation mode and shipping type for Stage1 of the freight booking.

Stage2 and invoicing carrier Carrier2

This is custom documentation. For more information, please visit SAP Help Portal.

211


1/14/26, 2:16 PM

The system determines freight agreement AGR2 because the transportation mode and shipping type of AGR2 match with

the transportation mode and shipping type for Stage2 of the freight booking.

Stage3 and invoicing carrier Carrier3

The system determines freight agreement AGR4 because the transportation mode of AGR4 matches with the

transportation mode of Stage3 of the freight booking.

Stage4 and invoicing carrier Carrier3

The system determines the freight agreement AGR5 because, in the absence of a stage-level transportation mode and

shipping type, the system considers the transportation mode and shipping type of the header level.

During charge calculation for the freight order, Freight_Order, the system determines the freight agreement AGR1 as it has the

same carrier, transportation mode, and shipping type as that of the freight order.

Related Information

Freight Booking

## Agreement

## Rate Determination

Transportation Management determines the most appropriate rate when calculating transportation charges, based on certain

criteria and attributes. The system determines a rate from the rate table (both kinds, including local) automatically during charge

calculation based on the attributes specified in the business document and the agreement.

With rate determination, you can also determine appropriate rates for various scenarios, for example:

You need to charge customers additional charges for providing a value added service, such as overnight service, first

priority service, and service provided on a holiday.

You need to charge customers for a single transportation rate instead of multiple rates.

## Rate Determination Techniques

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

## Through Rates

The system can determine a through rate from the source location of the first stage to the destination location of the last

stage in a forwarding order or freight order. You can also determine a through rate for two or more stages.

## Rate Determination with Partial Information

The system can determine the correct rate even when relevant information is missing from the forwarding order, freight

order, or rate table.

## Rate Determination with Scales of Different Dimensions

The system can determine the correct rate even when you maintain a rate table with scales that contain different

dimensions.

## Rate Determination Based on Holiday Calendar

This is custom documentation. For more information, please visit SAP Help Portal.

212


1/14/26, 2:16 PM

You can charge customers additional charges incurred for providing services on non-working days in a particular country or

a region, such as weekend days and public holidays.

## Rate Determination for Direct Shipment of Parcels

During the direct shipment of parcels, you can charge customers additional charges incurred for providing an overnight

service or a first priority service.

## Rate Determination Based on Zone Hierarchy and Postal Codes

Based on zone hierarchy, the system can determine the correct rate even when you don’t maintain rates for a specific zone.

Also, you can maintain a single rate in the rate table for multiple postal codes within a specific range by using the wildcard

character (*) in place of numerals for the postal code.

## Collective Rate Determination

When you create a collective settlement document from multiple forwarding orders or freight orders, you can choose to

sum up the values of the calculation bases with scales of different dimensions (as specified in the grouping rule) in multiple

forwarding orders and determine a rate for the collective value.

## Rate Determination Based on Transportation Duration

As a logistics service provider or shipper, you can charge your customers or pay your carriers based on how long it takes to

transport the order.

## Rate Determination Based on Planned Distance

As a logistics service provider or shipper, you can charge your customers or pay your carriers based on the planned

distance of each stage or of the entire freight order or freight booking.

## Rate Determination Based on Transportation Stops

As a logistics service provider or shipper, you can charge your customers or pay your carriers based on all stops and

intermediate stops also including substops of a transportation order.

## Rate Determination Based on Normalized and Additional Normalized Quantities

Normalized and additional normalized quantities are units that are used to determine the number of pallets and cargo

space occupied by transported cargo items.

## Rate Determination based on Commodity Codes Assigned to Material Master

You use commodity codes based on SAP Governance, Risk and Compliance (GRC), that is, a source in the material master,

to calculate the transportation charges.

Rate Determination based on Units of Measures (UoMs)

You use non-dimesnionless units of measure (UoM) in your scale base to calculate the transportation charges.

Through Rates

## Use

This function allows the system to use stage categories to calculate through rates in a forwarding order or freight order. You can

have a through rate for each stage category (for example, pre-carriage, main carriage, or on-carriage), a combination of successive

stage categories (for example, pre-carriage and main carriage), or an overall through rate. An overall through rate is a single rate

that can be used from the source location of the first stage category to the destination location of the last stage category.

This is custom documentation. For more information, please visit SAP Help Portal.

213


1/14/26, 2:16 PM

You can also enable through rates for internal transfer pricing (ITP) while calculating internal charges in a forwarding order.

Depending on the agreement settings, you can calculate the internal charges for each stage or combination of stages of a

forwarding order in a freight order or a freight booking.

## Integration

This function is used in the charge calculation process. For more information, see Charge Calculation.

## Prerequisites

You’ve enabled the calculation of through rates in Customizing for Transportation Management under  Basic Functions

 Charge Calculation

## Basic Settings

 Define Calculation Profiles .

You’ve entered a rate in the rate table (both kinds, including local) for the location pair (source location and destination

location).

Alternatively, if the leading charge type has a rate specified and you assign a rate directly to a calculation sheet line item

without using a rate table (both kinds, including local), you must enter a trade lane precondition for the calculation sheet

line item.

To enable internal charge calculation between the business unit and the gateway, you’ve performed the following:

You’ve maintained an internal agreement between the business unit and the gateway.

You’ve maintained a calculation sheet line item with the calculation method type Internal Charge Calculation.

To enable through rates for ITP, you’ve selected the Through Rate checkbox and you’ve maintained the calculation level as

Calculation at Stage Level in the calculation profile for the gateway. You define calculation profiles in Customizing for

Transportation Management under  Basic Functions

 Charge Calculation

 Basic Settings

 Define Calculation

Profiles .

## Features

While calculating through rates, the system evaluates through rates for a single stage category or a combination of stage

categories. The system also evaluates partial through rates when a through rate is available for the main carriage but not for the

pre-carriage and on-carriage. The system doesn’t consider through rates that split a stage category.

The use of stage categories simplifies and speeds up the calculation of through rates as the system checks for rates for every

location pair (source location and destination location).

You can see in the application log how the system evaluated and determined the through rates. You can use transaction SLG1 to

access the log object /SCMTMS/TMS with sub-object TCM. For the external ID, search with a wildcard and the user name.

## Example

You want to calculate the charge of a carriage on a route with the following stage categories:

Pre-carriage stage category with two stages: pick-up and pre-carriage 1

Main carriage stage category with two stages: main carriage 1 and main carriage 2

## On-carriage stage category with two stages: on-carriage 1 and delivery

While calculating the through rates, the system evaluates the through rates for a single stage category or a combination of stage

categories, as follows:

This is custom documentation. For more information, please visit SAP Help Portal.

214


1/14/26, 2:16 PM

Pre-carriage, main carriage, and on-carriage together

Pre-carriage and main carriage together

Main carriage and on-carriage together

## Main carriage only

## Pre-carriage, main carriage, and on-carriage separately

The system doesn’t consider through rates that split a stage category. For example, the system doesn’t consider a through rate for

pre-carriage and main carriage 1. The system doesn’t split the main carriage stage category even if you maintain the rates in a split

manner. But you can have a partial through rate where the through rate is maintained for the main carriage only but no through

rate is available for the pre-carriage and on-carriage.

In the application log, you can see the through rates that the system used to calculate the charges and how the system determined

those through rates.

More Information

Rate Determination

## Charge Calculation

Rate Determination with Partial Information

## Use

The system can determine the correct rate even when relevant information is missing from the forwarding order, freight order, rate

table, or local rate table. When one or two attributes are missing from the forwarding order or freight order but the rates are

present, the system determines multiple rates. Then you can select the applicable rate manually or the system can select it

automatically based on the multiple rate default specified for the calculation sheet line item. Note that the system can determine

multiple rates only if the calculation base that is missing in the forwarding order or freight order isn’t numeric. When a carrier is

assigned to a stage in the forwarding order or freight order, but there’s no rate for the carrier in the rate table or the local rate

table, the system determines a generic rate.

Note that the system can also determine multiple rates for mandatory charge lines.

## Integration

The system determines the rate during the charge calculation process. For more information, see Charge Calculation.

## Prerequisites

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

For the system to determine multiple rates, you’ve assigned a rate table with two or more attributes to the calculation sheet.

Depending on the attributes, you’ve also specified the resolution base for the charge type.

For the system to determine a generic rate, you have a rate table containing a scale item with no value. To allow a rate table to

contain a scale item with no value, choose the calculation base of the carrier on the Scales tab of the rate table and select the Item

with No Value Allowed checkbox. The system adds a scale item with no value to the scale.

This is custom documentation. For more information, please visit SAP Help Portal.

215


1/14/26, 2:16 PM
## Features

When the IATA note or general note information isn’t available in the business document and when you maintain the

calculation base as IATA note or general note in the calculation sheet (both kinds, including local), the system determines

multiple rates. If the multiple rate determination results in a single rate, the system performs an automatic rate lookup and

calculates charges.

For each calculation sheet line item, you can specify on the Rates tab what you want the system to do when the system

finds multiple rates.

For example, the system can automatically select one of the following:

The lowest rate

## The highest rate

The only rate (if only one rate is found)

If you enter All or don’t specify what you want the system to do when the system finds multiple rates, the system doesn’t

automatically select the applicable rate. Instead, you must select the applicable rate manually. Specifying the multiple rate

default allows the system to select the rate automatically without you needing to intervene manually.

If you specify commodity codes in a forwarding order or the associated master data, the system determines multiple rates

in the following cases:

When you have a forwarding order with no commodity codes and the associated rate table (both kinds, including

local) has rates for multiple commodity codes. On triggering charge calculation, the system displays multiple rates

for the charge line.

When you have a forwarding order with multiple commodity codes and the associated rate table (both kinds,

including local) has the calculation base as COMM_CODE_MUL. On triggering charge calculation, the system displays

multiple rates for the charge line.

For more information on commodity codes, see Classification of Goods.

## Activities

The system determines multiple rates when you choose Multiple Rates and you can choose the applicable rate. Note that you can

choose to show or hide scale value descriptions and rate table notes in the Multiple Rates dialog box.

  Note

The system determines a generic rate instead of displaying multiple rates when the charge type under the instruction type Line

Item Selection and the corresponding rate table (both kinds, including local) have more than one scale base with a generic

value.

For the system to determine a generic rate when calculating the charges, the system uses the scale item with no value if no scale

items match the value of the calculation base in the forwarding order or freight order or if the calculation base has no value.

## Example

The following example is applicable to both kinds of rate table and calculation sheets, including local rate tables and calculation

sheets.

You assign the following rate table to the calculation sheet:

This is custom documentation. For more information, please visit SAP Help Portal.

216


1/14/26, 2:16 PM

Source Location

Destination Location

Transshipment Location Rate

HAM

HAM

HOU

HOU

CY_NUE

## CY_NUE

USD 100 per 10 kg

## USD 200 per 10 kg

The transshipment location is missing in the forwarding order or freight order. The system determines multiple rates. As you

specified All as the multiple rate default for the calculation sheet line item, you must select the applicable rate manually in the

charges grid on the Charges tab of the business document.

When entering the data for another rate table, you enter the following data:

## Source Location

Destination Location Carrier

Rate

HAM

HAM

HOU

HOU

A

*

USD 100 per 10 kg

## USD 200 per 10 kg

The system determines a generic rate as follows:

If the carrier is A in the forwarding order or freight order, the system applies USD 100.

If the carrier is anything other than A in the forwarding order or freight order, the system picks up the scale item with no

value and applies USD 200.

If no carrier is assigned to a stage in the forwarding order or freight order, the system determines both rates and you select the

applicable one.

More Information

## Rate Determination

Rate Definition and Maintenance

## Scale Maintenance

Rate Determination with Scales of Different Dimensions

## Use

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

When you maintain a rate table with scales of different dimensions, the system can determine the correct rate based on the

information in the forwarding order (FWO) or freight order (FO). The system performs the following tasks to determine the correct

rate:

1. Selects the rate table item in which different attributes of the same scale match the attributes in the FWO or FO.

2. Uses this rate table item to determine the correct rate that matches the other attributes in the FWO or FO.

## Integration

This is custom documentation. For more information, please visit SAP Help Portal.

217


1/14/26, 2:16 PM

The system determines the rate during the charge calculation process. For more information, see Charge Calculation.

## Activities

To define or change a rate table or a local rate table for an agreement, a calculation sheet, or a local calculation sheet, choose one

of the following apps on the fiori launchpad:

Freight Agreements or Forwarding Agreements

Create Calculation Sheet or Edit Calculation Sheet

## Example

You specify the following attributes in a rate table or a local rate table:

Source Location

Destination Location

<=200 kg

<=400 kg

<=600 kg

A

A

B

C

USD 50

USD 90

USD 75

USD 130

USD 100

In the FWO, you specify the source location as A and the destination location as C for a freight unit of 150 kg.

During charge calculation, the system determines the rate table item for source location A and destination location C. The system

then determines the less than 400 kg rate of USD 75 as the correct rate from the rate table or the local rate table because you

haven’t entered a rate for the less than 200 kg.

More Information

## Rate Determination

Rate Definition and Maintenance

Rate Determination Based on Holiday Calendar

## Use

As a logistics service provider or carrier, you can charge your customers additional charges incurred for providing services on

nonworking days, such as weekends and public holidays, in a particular country or region.

## Prerequisites

You've defined factory calendars in Customizing for Transportation Management under  Master Data

 Calendar

## Maintain

Factory Calendar

.

You've defined a location calendar for a specific country and a region using a factory calendar in Customizing for Transportation

Management under  Basic Functions

 Charge Calculation

## Basic Settings

 Define Location Calendar

.

## Integration

The system determines the rate during the charge calculation process. For more information, see Charge Calculation.

This is custom documentation. For more information, please visit SAP Help Portal.

218


1/14/26, 2:16 PM
## Features

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

In a rate table, you can maintain the calculation base as either PICKUP_HOLIDAY or DELIVER_HOLIDAY. If you specify the

calculation base as PICKUP_HOLIDAY, the system uses the source location specified in the forwarding order or freight order for

rate determination. If you specify the calculation as DELIVER_HOLIDAY, the system uses the destination location specified in the

forwarding order or freight order for rate determination.

Based on the calculation date type specified at the charge type level in the calculation sheet, the system chooses the calculation

date as order date, system date, or invoice date. If you haven't maintained any calculation date type for a calculation sheet item,

the system uses the calculation date specified in the calculation profile to determine rates for charge calculation. Using the

location and date information, the system determines from the factory calendar whether the date used for charge calculation is a

nonworking day or a working day in a specific region.

More Information

## Rate Determination

## Rate Definition and Maintenance

Rate Determination for Direct Shipment of Parcels

## Use

As a logistic service provider or carrier, you may need to transport parcels to the customer as soon as possible and hence you

forward them directly without consolidation. In such cases, you can charge the customer for the additional charge incurred for

providing an overnight service or a first priority service.

Transportation Management enables you to determine rates for direct shipments from either the Web services provided by an

external parcel service provider or from a standard rate table (both kinds, including local).

## Integration

This function is a part of the charge calculation process. From more information, see Charge Calculation.

## Prerequisites

You have defined a calculation profile with the calculation level as Calculation at Item Level in Customizing for

Transportation Management under  Basic Functions

 Charge Calculation

 Basic Settings

 Define Calculation

Profiles .

You have assigned the calculation profile to a charges profile and maintained a local currency in Customizing for

Transportation Management under  Basic Functions

 Charge Calculation

## Basic Settings

 Define Charges Profiles .

You have assigned the charges profile to an organizational unit in the transaction PPOME.

You have defined a manifest or express freight order type in Customizing for Transportation Management under  Freight

Order Management

## Freight Order

 Define Freight Order Types .

This is custom documentation. For more information, please visit SAP Help Portal.

219


1/14/26, 2:16 PM

You have maintained the direct shipment option settings in Customizing for Transportation Management under

## Planning

## Freight Units

 Define Freight Unit Types .

You have maintained a master waybill stock between the purchase organization and the carrier in the Waybill Number

Stocks app on the fiori launchpad.

## Features

You can determine rates from a standard rate table (both kinds, including local). You can create an agreement with a carrier and

assign each agreement item to one carrier product. You can specify the attributes, such as length, width, height, and girth, on the

Parcel tab page of the agreement. When you perform direct shipment option determination, the system compares the attributes of

the parcel specified in the freight unit with that specified in the agreement. For the system to consider an agreement for charge

calculation, all the attribute values specified in the freight unit must be less than or equal to the attribute values specified in the

agreement. If there are multiple agreements that meet this condition, the system displays a list from which you can choose one.

## Activities

You can create a parcel freight order in the Create Road Freight Order app on the fiori launchpad. Note that a parcel freight order

is created as a road freight order that has a corresponding freight order type and the shipping type Parcel. For more information

see Parcel Shipment.

More Information

## Rate Determination

Rate Definition and Maintenance

## Agreement Maintenance

Rate Determination Based on Zone Hierarchy and Postal Codes

## Use

The system determines the correct rate in the following scenarios:

If you don’t maintain the rates for a specific zone, the system determines the appropriate rate based on zone hierarchy.

If you don’t maintain the rates for a specific postal code, the system determines the rate based on wildcard search.

## Integration

The system determines the rate during the charge calculation process. For more information, see Charge Calculation.

## Features

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

## Zone Hierarchy

This is custom documentation. For more information, please visit SAP Help Portal.

220


1/14/26, 2:16 PM

The system calculates the charges based on the transportation zone hierarchy you maintain. For example, you’ve maintained the

following zones in the following hierarchy:

1. Zone A

2. Zone B

3. Zone C

4. Zone D

During charge calculation, for a forwarding order with zone D, the system determines a rate for zone D from the rate table. If you

haven’t maintained any rates for zone D, the system determines the next appropriate rate from the rates maintained for the

superordinate zones in the hierarchy as follows:

1. Zone C

2. Zone B

3. Zone A

## Postal Codes

You can maintain a single rate for multiple postal codes within a specific range by using the wildcard character (*) in place of

numerals in the postal code and maintain rates in the rate table. For example, you maintain a rate table as follows:

Postal Code/ Weight

>100 kg

>200 kg

90210

9021*

902*

10 USD

12 USD

15 USD

-

-

25 USD

You have a forwarding order with a postal code of 90210 and gross weight of 250 kg. During charge calculation, the system

determines 25 USD as the rate from the rate table and calculates charges. The system looks for the most specific rate (for postal

code 90210) and when not found, it determines the next appropriate rate with a wildcard-based search. Here, the rate

determination is based on the following sequence:

1. 90210

2. 9021*

3. 902*

More Information

## Rate Determination

Rate Definition and Maintenance

## Collective Rate Determination

When you create a collective settlement document from multiple forwarding orders or freight orders, you can choose to sum up

the values of the calculation bases with scales of different dimensions in multiple orders and determine a rate for the collective

value.

This is custom documentation. For more information, please visit SAP Help Portal.

221


1/14/26, 2:16 PM

The system groups the rates based on a grouping rule and also on the resolution base you specify in the calculation sheet. The

resolution base determines the level (for example, item level or container level) at which the system must determine the rates.

The collective rate can often be less than the rate for the individual values.

Note that you can specify that the system performs standard charge calculation when you don't maintain a rate for a collective

quantity.

## Prerequisites

You've defined grouping rules in the view Define Grouping Rules for Charge Calculation Resolution

(/SCMTMS/V_RUL113) using transaction SM30.

The system groups the calculation base values if you specify Yes in the Group Across Orders field and specify the

calculation base that the system must use for grouping in the Group By field. You must deselect the By Calculation Level

checkbox for the system to determine a rate for the collective value.

You've created a collective forwarding settlement document or a collective freight settlement document using the

Forwarding Settlements app or the Freight Settlements app on the launchpad.

## Example

A customer asks you to transport products from the same pick-up location in two separate forwarding orders. According to the

forwarding agreement you have with the customer, you must charge a collective rate based on the source location across multiple

forwarding orders. A collective rate helps ensure you charge the better rate for the customer.

You make the following settings:

voucher

1. Using transaction SM30, you define the rule for grouping the rates in the view Define Grouping Rules for Charge

Calculation Resolution (/SCMTMS/V_RUL113).

You specify the following settings:

Group by the Source Location calculation base

## Group across orders

2. In the agreement you have with the customer, you create a consolidation charge line and specify this grouping rule under

General Details

## Items

 Calculation Sheet Overview .

3. In the agreement, you use a rate table that specifies the following rates per KG:

$10 for < 10 KG

$8 for between 10 KG and < 25 KG

$6 for between 15 KG and < 45 KG

In the two forwarding orders, the gross weight of the transported products is 8 KG and 13 KG. The system determines the

collective rate based on the consolidated gross weight as follows:

8 KG + 13 KG = 21 KG x $8 = $168

If the system determined the rate separately for each forwarding order, the rate would be as follows:

8 KG x $10 = $80

This is custom documentation. For more information, please visit SAP Help Portal.

222


1/14/26, 2:16 PM

13 KG x $8 = $104

$80 + $104 = $184

The collective rate is the better rate for the customer.

## More Information

Freight Settlement Integration using MM External Services Management

Forwarding Settlement

## Charge Calculation

## Rate Determination Based on Transportation Duration

As a logistics service provider or shipper, you can charge your customers or pay your carriers based on how long it takes to

transport the order. For the system to determine the rate based on the transportation duration, you specify the calculation base as

Gross Duration (DURATION_GROSS) or Net Duration (DURATION_NET) in a rate table or a local rate table. When you specify the

calculation base as DURATION_GROSS, the system uses the total time taken to transport the order. The total time includes the

actual transportation duration and the time taken for other tasks needed to transport the order, such as the time taken to load and

unload. When you specify the calculation base as DURATION_NET, the system uses only the actual transportation duration. Note

that when you maintain the scales or define the scale values, the default unit of measure for the calculation bases is HH: MMMM.

You can change the unit of measure to any time-based unit of measure when you define the calculation rules in rate tables. You can

change the unit of measure in rate tables under  Rate Table

 Dates and Values

## Validity

 Calculation Rules .

## Integration

The system determines the rate during the charge calculation process. For more information, see Charge Calculation.

## Example

You have the following rates for the base freight charge type:

## Source Location

Destination Location Duration >=

## Rate

Currency

Nürnberg

Hamburg

Nürnberg

Hamburg

16:00

20:00

100

120

EUR

EUR

The calculation rule is as follows:

Calculation Base Price Unit

DURATION_NET

50

UoM

## Min

The net duration for the freight order is 18 hours. The system calculates the price per minute: 18 hours = 1,080 minutes.

The system calculates the charge for the freight order as follows:

This is custom documentation. For more information, please visit SAP Help Portal.

223


1/14/26, 2:16 PM

Charge Type

## Rate

Currency

Price Unit

UoM

## Qty

Calc. Base

Chargeable

Final

## Qty

## Amount

BASE_FREIGHT

100

EUR

50

Min

1080

DURATION_NET

18:00

2160

Related Information

## Rate Determination

Rate Definition and Maintenance

## Rate Determination Based on Planned Distance

As a logistic service provider or shipper, you can charge your customers or pay your carriers based on the planned distance of

each stage or of the entire freight order or freight booking.

To calculate the planned distance-based charges, add the relevant charge type and the calculation base PLAND_DIST in the

calculation sheets or scales of the rate table.

## Integration

The system determines the rate during the charge calculation process. For more information, see Charge Calculation.

## Example

You’ve a freight order that you’re shipping from Munich to Berlin. The planned distance between Munich (source location) and

Nürnberg (destination location) is based on the number of stages, if any. Your freight order has two stages, which are the following:

## Source Location

Destination Location Distance

Munich

Nürnberg

169.2 KM

The planned distance from Munich to Nürnberg is 169.2 KM.

You’ve defined the following calculation bases in the rate table:

Calculation Base

Calculation Base

Calculation Type

Scale Type

Scale UoM

Description

## SOURCELOC

Source Location

## Absolute

Same Scale (=)

## DESTLOC

Destination Location

## Absolute

Same Scale (=)

PLAND_DIST

Distance

## Relative

Base Scale (>=)

KM

You've defined the following rate lines:

Source Location (=)

Destination Location (=)

Rate (Distance >=100KM) Currency

Munich

Nürnberg

Nürnberg

Berlin

3

5

EUR

EUR

This is custom documentation. For more information, please visit SAP Help Portal.

224


1/14/26, 2:16 PM

Source Location (=)

Destination Location (=)

Rate (Distance >=100KM) Currency

Munich

Berlin

7

EUR

The system calculates the charge ( Base FTL - Minimum) for the entire freight order based on the formula:

((Rate amount * Quantity)/Price per unit)

In this case, the rate amount is 3 EUR per KM and the quantity (total distance) for the freight order is 169.2 KM. Therefore, the final

amount is ((3*169.2)/1) = 507.60 EUR.

Charge Item

Charge Type

Rate Amount

## Currency

Price per Unit

## UoM

Quantity

Final Amount

Base FTL -

BASE_FTL_MIN 3

EUR

1

KM

169.2 KM

507.60 EUR

## Minimum

Related Information

## Rate Determination

## Rate Definition and Maintenance

## Rate Determination Based on Transportation Stops

As a logistic service provider or shipper, you can charge your customers or pay your carriers based on all stops and intermediate

stops also including substops of a transportation order.

For the system to determine the rate based on the number of stops, you can specify the following calculation bases in the

calculation sheets or scales of the rate table:

NUMBER_OF_STOPS (Number of Stops)

NO_OF_INT_STOPS (Number of Intermediate Stops)

STOPS_SUBSTOPS (Number of Stops Including Sub-Stops)

INTSTOP_SUBSTOP (Number of Intermediate Stops Including Sub-Stops)

You can see the stops in the Stages tab of freight documents or the Route tab of forwarding documents.

You can see the sub-stops (for example the loading or unloading stops, for both inbound and outbound deliveries) for Advanced

Shipping and Receiving (ASR) enabled shipping or receiving points in the Overview tab of freight orders. For more information and

prerequisites, see Advanced Shipping and Receiving

  Note

You can use the calculation bases NUMBER_OF_STOPS(Number of Stops) and NO_OF_INT_STOPS (Number of

Intermediate Stops) for both freight and forwarding documents.

You can use the calculation bases STOPS_SUBSTOPS (Number of Stops Including Sub-Stops) and INTSTOP_SUBSTOP

(Number of Intermediate Stops Including Sub-Stops) only for freight orders.

## Integration

This is custom documentation. For more information, please visit SAP Help Portal.

225


1/14/26, 2:16 PM

The system determines the rate during the charge calculation process. For more information, see Charge Calculation.

## Example

You’ve a transportation order whose source location is Nürnberg and destination location is Hamburg. There's a shipping/receiving

point (industry park) in Hamburg with two warehouses. There're two substops Warehouse1 – Unloading Point1 (UL001) and

Warehouse2 – Unloading Point2 (UL002).

You've the following stages and locations:

Stages

Stage 1

Stage 2

Source Location

Destination Location

Sub Stops

Nürnberg

Frankfurt

Frankfurt

Hamburg

## None

Warehouse1 – Unloading Point1

(UL001)

Warehouse2 – Unloading Point2

(UL002)

Following are the values for header-level charge calculation:

NUMBER_OF_STOPS is 3 (Nürnberg, Frankfurt, and Hamburg)

NO_OF_INT_STOPS is:

(NUMBER_OF_STOPS – 2) = (3-2) = 1

STOPS_SUBSTOPS is 4 (Nürnberg, Frankfurt, UL001, and UL002)

INTSTOP_SUBSTOP is:

(STOPS_SUBSTOPS – 2) = (4-2) = 2

For item-level charge calculation, STOPS_SUBSTOPS is always 2 and INTSTOP_SUBSTOP is 0.

  Note

The system doesn't support stage-level charge calculation based on the number of sub-stops.

Related Information

## Rate Determination

## Rate Definition and Maintenance

Rate Determination Based on Normalized and Additional
## Normalized Quantities

Normalized and additional normalized quantities are units that are used to determine the number of pallets and cargo space

occupied by transported cargo items.

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

226


1/14/26, 2:16 PM

Additional normalized quantities allow shippers and trucking companies to determine the size of the trailer for transporting cargo

items. You can calculate transportation charges based on the normalized quantity and additional normalized quantity.

The normalized quantities and additional normalized quantities are available in the General Data tab of the freight order or freight

booking.

Based on the agreed rates and freight agreement, the system determines the freight charges based on the normalized quantities

and additional normalized quantities. You use calculation bases NLQ for normalized quantities and ALQ for additional normalized

quantities in a rate table to add the rates. These rates are then used to determine the charges for the freight order or freight

booking.

For more information, see Use of Normalized Quantities and Capacities.

Rate Determination based on Commodity Codes Assigned to
## Material Master

You use commodity codes based on SAP Governance, Risk and Compliance (GRC), that is, a source in the material master, to

calculate the transportation charges.

You can base transportation charges on commodity codes for a particular numbering scheme.

For example, for rail freight orders in North America, the rates and handling of freight depend on the type of commodity that is

shipped by the rail carrier. As carriers aren’t aware of the type of freight that is subcontracted by the shipper, standard commodity

codes are used to classify the freight for transportation.

There are sets of commodity codes for a particular numbering scheme that you assign to the products of a freight order. You can

see the numbering scheme and commodity code for a product on the

## Items

  Commodity Codes tab of the freight order.

Based on agreed rate and freight agreement between the business parties, the system determines the transportation charges

based on the numbering scheme and commodity code. You use calculation base COM_CODE_SCHM in the rate table for charges

based on commodity codes. For more information see, Commodity Codes Assigned to Material Master.

Rate Determination based on Units of Measures (UoMs)

As a logistics service provider or shipper, you can calculate transportation charges based on units of measures (UoMs) for the

product quantities. For the system to determine the rate based on the UoMs, you specify the scale base as QTYALL and calculation

base as QTY_ALL_VAL in a rate table or local rate table.

UoMs can be of the following types:

Dimensionless where the quantity of the item/product in freight documents have no specific dimensions, for example, Each

Piece, Carton, and so on.

Non-Dimensionless where the quantity of the item/product in freight documents have specific dimensions, for example,

Meter, Millimeter, and so on.

UoMs are defined in the sales order or purchase order (in the material master of the product items). During charge calculation, you

can use the same UoM to calculate the charges. For example:

If the sales order has the non-dimesnionless UoM Meter (M), then the same UoM is used in the subsequent freight units

and freight orders. Charge calculation considers Meter (M) as the UoM at the product level.

This is custom documentation. For more information, please visit SAP Help Portal.

227


1/14/26, 2:16 PM

If the sales order has the dimensionless UoM Each (EA), then the same UoM is used in the subsequent freight units and

freight orders. Charge calculation considers Each (EA) as the UoM at the product level.

## Scale and Calculation Bases

For UoM relevant charge calculation, the scale base is QTYALL. In the Customizing for the scale base, the UoM Relevant checkbox

is checked. You can see that in the Customizing for Transportation Mangement under  Basic Functions

 Charge Calculation

 Data Source Binding

 Define Scale Bases .

The system considers all types of UoMs, including dimensionless and non-dimensionless UoMs, for calculating the transportation

charges when there's no value in the Dimension field.

If you enter any valid dimension in the Dimension field for the scale base QTYALL, then the sytsem considers that dimension for

change calculation. You can do that in the Customizing for Transportation Mangement under  Basic Functions

## Charge

## Calculation

 Data Source Binding

 Define Scale Bases .

The calculation base for using all kind of UoMs, including dimensionless and non-dimensionless, is QTY_ALL_VAL.

  Note

There're no changes to the settlement processes when you use dimensionless or non-dimensionless UoMs for charge

calculation.

Charge Estimation

## Use

This function allows you to estimate freight charges, forwarding charges, and internal charges for a single route based on

minimum input. You can estimate charges for the entire route (header-level calculation) or for individual stages of the route (stage-

level calculation). Note that the more data you enter, the more accurate the charge estimation.

Using this function, the system allows you to provide an immediate response to a query. This is useful, for example, to allow a sales

person to respond promptly to a query from a business partner about the charge for a transport over a particular route.

  Note

The system does not save the data that you enter, or the charge estimation.

## Integration

This function is available as part of the charge calculation process. For more information, see Charge Calculation.

## Prerequisites

In Customizing, you have carried out the activities for Transportation Management under  Basic Functions

## Charge

Calculation .

You have set up the master data for the Charge Management and Service Product Catalogs component (see Setup of MD

for Charge Management and SP Catalogs).

If you want to estimate freight and forwarding charges for air transportation, you must make the charge management

settings that are relevant for air freight (see Charge Management Settings for Air Freight).

This is custom documentation. For more information, please visit SAP Help Portal.

228


1/14/26, 2:16 PM
## Features

You can estimate charges for existing or new business partners. You must enter the following information:

Sales organization

Source location

## Destination location

For existing business partners, you must also enter the sold-to party.

  Note

During the charge estimation of freight and forwarding charges for air transportation, the system determines the air waybill

type, printing, and settlement based on TACT rates or contract rates as specified in the calculation profile settings. If the

system does not determine the air waybill type, printing, and settlement, you can also manually enter these values.

During charge estimation of ocean freight charges, you can calculate the transportation charges either from port-to-port or

door-to-door. You specify the consolidation settings to estimate charges for a freight booking in Customizing for

Transportation Management under  Freight Order Management

## Freight Booking

 Define Freight Booking Types .

During strategic freight procurement, the system can estimate the cost of using a carrier to provide transportation services in a

trade lane. For more information, see Strategic Freight Procurement and Post-Bid Analysis.

When estimating the charges for existing business partners, the system uses the specific agreement between the business

partner and the sales organization. When estimating the charges for new business partners, the system uses a generic agreement

that is not specific to any business partner.

Note that if you do not enter the pick-up date, the system uses the system date as the pick-up date.

## Activities

You can estimate freight charges in the Estimate Freight Charges app on the fiori launchpad.

You can estimate forwarding charges in the Estimate Forwarding Charges app on the fiori launchpad.

Service Charges

## Use

You can charge customers for additional services, such as fumigation, packing and labelling, and insurance, even when you do not

specify these additional service items in the freight agreement attached to a freight order. You can include the charges for the

charge types associated with the service items in the freight order and perform charge calculation.

## Integration

You use additional service charges during charge calculation process (see Charge Calculation).

## Prerequisites

This is custom documentation. For more information, please visit SAP Help Portal.

229


1/14/26, 2:16 PM

In Customizing, you have carried out the activities for Transportation Management under  Basic Functions

## Charge

Calculation .

You have set up the master data for the Charge Management and Service Product Catalogs component (see Setup of MD

for Charge Management and SP Catalogs).

You have assigned charge types to a service type in Customizing for Transportation Management under  Basic Functions

 Charge Calculation

## Basic Settings

 Assign Charge Types to Service Types .

## Features

When you select the Additional Service Charges checkbox in a freight agreement item, the system automatically inserts a blank

charge line on the Charges tab page in the freight order corresponding to each additional service item specified in the freight

order. The system inserts these charge lines using the charge types assigned to the service items. The system specifies the

instruction type as Standard in these newly-added charge lines. You can manually enter information, such as rates and calculation

rules, for charge calculation. The system defaults the resolution base to SERVICE for these newly-created charge lines.

  Note

If you have assigned multiple charge types to a service type in Customizing for Transportation Management under  Basic

## Functions

 Charge Calculation

## Basic Settings

 Assign Charge Types to Service Types , the system selects only one of

these charge types corresponding to the service to create a blank charge line on the Charges tab page.

If you deselect the Additional Service Charges checkbox, the system does not automatically insert charge lines for additional

services and the system does not consider the additional service items in the freight order for charge calculation.

More Information

Calculation Logic

## Cost Pull

You can use execution costs as a basis for settling with your customers or internal organization by transferring distributed costs

from the freight side to the forwarding side. You can charge the customer for the total or partial execution charges and the

additional charges using the cost pull calculation method.

Note that cost pull only works with header-level and stage-level charge calculation; it doesn’t work with item-level charge

calculation.

## Integration

Cost pull calculation method is used in the cost distribution process and charge calculation process. For more information, see

Cost Distribution Management and Charge Calculation.

## Prerequisites

You’ve specified the cost distribution settings in Customizing for Transportation Management under  Basic Functions

 Cost Distribution .

You’ve assigned the distribution profiles to the relevant organization in the Customizing for Transportation Management

under  Basic Functions

 Charge Calculation

## Basic Settings

 Define Charges Profiles .

This is custom documentation. For more information, please visit SAP Help Portal.

230


1/14/26, 2:16 PM

For logistics service providers that want to use the freight cost in a freight order or freight booking for internal settlement,

you must enable freight orders or freight bookings for cost distribution. For more information, see the following

Customizing activities:

For freight orders, see Customizing for Transportation Management under  Freight Order Management

 Freight

## Order

 Define Freight Order Types .

For freight bookings, see Customizing for Transportation Management under  Freight Order Management

## Freight Bookings

 Define Freight Booking Types .

To transfer the result of cost distribution from the freight side to the forwarding side, in the calculation sheet or the local

calculation sheet, you must specify Customer and Service Provider in the Charge Usage field. For internal charge

calculation, you must specify Internal as the charge usage. You must specify the instruction type as Cost when defining a

calculation sheet or a local calculation sheet. For more information, see Calculation Sheet.

You’ve specified the data source as Actual Route. You specify the data source in Customizing for Transportation

Management under  Basic Functions

 Charge Calculation

## Basic Settings

 Define Calculation Profiles .

## Features

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

## Cost Instruction Type

You use an instruction type of Cost at item level. When you use a cost instruction type, the system automatically includes an

internal charge calculation method type, and the cost pull calculation method COST_PULL. You can insert a markup charge line for

a percentage value with reference to the cost charge line. For a cost charge line, you can specify a cost pull strategy based on

which the system transfers the results of cost distribution to the forwarding side.

## Cost Pull Strategy

You specify the cost pull strategy in the calculation sheet. Based on the cost pull strategy you specify, the cost charge line appears

in the forwarding order with or without standard charge lines. Based on the cost pull strategy, the system can either add the costs

and aggregate it in a standard charge line or just copy the costs under the cost charge line or the standard charge line.

You can specify one of the following settings:

## Aggregation

The system adds the charges in all the distributed charge lines in the freight order and displays the totals in a standard

charge line in the forwarding order. Note that a standard charge line is mandatory when you specify the cost pull strategy

as Aggregate. For more information, see Internal Settlement Management.

## Active Copy

The system copies the individual distributed charge lines in the freight order to the forwarding order under a cost charge

line as active charge lines.

## Inactive Copy

The system copies the individual charge lines from the air waybill charge item to the forwarding order under a cost charge

line as inactive charge lines. For more information, see Air Waybill Direct Cost Pull.

On the Cost Pull tab page in the calculation sheet, you can specify the charge types the system transfers to the forwarding side.

This is custom documentation. For more information, please visit SAP Help Portal.

231


1/14/26, 2:16 PM

Note that you can’t edit the Amount or Currency fields for the cost charge line and the standard charge lines under the cost

charge line.

## Source Charge

You can specify the source of the charges in the calculation sheet. Based on the source charge you specify, the system pulls the

charge lines from one of the following areas to the forwarding order:

From the settlement charge item of the freight order or freight booking

## From the air waybill charge item

From the Internal Charges tab page of the freight order

From the Charges tab page and the Internal Charges tab page of the freight order

From the Internal Charges tab page of the forwarding order to the Charges tab page of the forwarding order

  Note

The system defaults the source charge as External. The system enables the Source Charge field in the calculation sheet

only when you specify the cost pull strategy as Active Copy. If you don’t enter a value in the Source Charge field, the

system pulls the distributed costs in the freight order to the forwarding order. The system copies all the charge lines as

active charge lines in the forwarding order.

When you specify the cost pull strategy as Active Copy and the source charge as Air Waybill, the system copies the

calculation base, the calculation rule, and the rate details, for each charge line from the freight booking to the forwarding

order.

## Automatic Recalculation of Cost Pull Charges

If charges are changed in a freight order or freight booking in a cost pull scenario, the system recalculates the cost pull charges

automatically in the relevant forwarding orders. For more information, see Automatic Recalculation of Cost Pull Charges in

Forwarding Orders.

Related Information

Examples: Cost Pull

## Cost Distribution for LSPs

Calculation Sheet and Local Calculation Sheet Maintenance

## Calculation Methods

Automatic Recalculation of Cost Pull Charges in Forwarding
## Orders

If charges are changed in a freight order or freight booking in a cost pull scenario, the system recalculates the cost pull charges

automatically in the relevant forwarding orders.

If the forwarding order in process, the system recalculates the cost pull charges automatically and updates the invoicing status

accordingly.

If the forwarding order is complete, the system reopens the forwarding order before recalculating the cost pull charges and

updating the invoicing status. The system then updates the status of the forwarding order in alignment with the invoicing status.

This is custom documentation. For more information, please visit SAP Help Portal.

232


1/14/26, 2:16 PM

That is, if the forwarding order is completely invoiced, the status is set to complete. However, if the forwarding order isn’t

completely invoiced, the status is set to in process.

Note that you can check existing forwarding orders for cost pull charges using the program Check for Cost Pull Charges in

Existing Business Documents (/SCMTMS/SET_COST_CHARGE_EXIST). If the system finds existing forwarding orders with cost

pull charges and charges were changed in the relevant freight order or freight booking, the system recalculates the charges.

  Note

The system doesn’t redetermine the agreement, calculation sheet, or local calculation sheet.

When automatically recalculating the cost pull charges in forwarding orders, the system also recalculates all other

charge lines.

Therefore, any changes to rate tables or local rate tables are reflected in all relevant charge lines.

If the settlement document already exists, the system can create a new settlement document to settle the updated

charges in the business document.

The system creates this new settlement document automatically using the program Creation of Forwarding

Settlement Documents (/SCMTMS/CFIR_CREATE_BATCH). For more information, see Creation and Transfer of

Forwarding Settlement Documents.

## Prerequisites

You have made the prerequisite settings for cost pull (see Cost Pull).

Examples: Cost Pull

## Use

The following examples describe the various possibilities of the cost distribution function in Transportation Management (TM). For

more information, see Cost Pull.

## Prerequisites

You plan two forwarding orders in a freight order. The gross weights of forwarding order 1 and 2 are 560 kg and 450 kg respectively.

You have the following values in the freight order and you perform charge calculation:

Charge Type

## Rate Amount

Calculation Rules

Total Gross Weight in kg

Calculated Amount in

Loading charges

10

On gross weight per 10

1010

Basic charges

200

External cost distribution scenario:

kg

NA

NA

USD

1010

200

After calculating charges, you distribute the costs in the associated forwarding orders. The externally-distributed costs are as

follows:

This is custom documentation. For more information, please visit SAP Help Portal.

233


1/14/26, 2:16 PM

Forwarding Order

Loading Charges

Basic Charges

Total Charges in

Gross Weight

Forwarding order 1

560

Forwarding order 2

450

110.89

89.11

Internal cost distribution scenario:

USD

670.89

539.11

560

450

Distribution

Percentage

55.40

44.60

You have a vehicle resource DI_TRUCK for shipping the cargo. You maintain an agreement between the organization of the vehicle

resource and the business partner of the purchasing organization.

You have the following values in the freight order and you perform internal charge calculation:

Charge Type

## Rate Amount

Calculation Rules

Total Gross Weight in kg

Calculated Amount in

Loading charges

Haulage charges

10

3

On gross weight per 10

1010

kg

On gross weight per 1 kg

1010

USD

1010

3030

After calculating internal charges, you distribute the costs in the associated forwarding orders. The internally-distributed costs are

as follows:

Forwarding Order

Haulage Charges

Loading Charges

Total Charges in

Gross Weight

Forwarding order 1

1680

Forwarding order 2

1350

560

450

Example

USD

2240

1800

560

450

Distribution

Percentage

55.40

44.60

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

Example 1:

You specify the cost pull strategy as Active Copy and the source charge as External in the calculation sheet.

When you calculate charges in the forwarding order 1, the following happens:

The system calculates the charges and displays them on the Charges tab. The system displays the costs pulled from the

freight order under the cost charge line.

The system creates two charge lines; one for the loading charges and one for the basic charges. From the freight order, the

system pulls and displays the calculated amount and final amount as USD 560 and USD 110.89 for the loading charges and

basic charges respectively.

As you’ve specified the source charge as External, the system pulls the costs from the external cost distribution of the

freight order. The pulled execution cost has all the charge lines from freight order 1.

As you’ve specified the cost pull strategy as Active Copy, you can edit the rate amount and currency.

This is custom documentation. For more information, please visit SAP Help Portal.

234


1/14/26, 2:16 PM

Example 2:

You specify the cost pull strategy as Inactive Copy and the source charge as Internal in the calculation sheet.

When you calculate charges in the forwarding order 1, the following happens:

The system calculates the charges and displays them on the Charges tab. The system displays the costs pulled from the

freight order under the cost charge line.

The system creates two charge lines; one for the loading charges and one for the haulage charges. From the freight order,

the system pulls and displays the calculated amount and final amount as USD 560 and USD 1680 for the loading charges

and haulage charges respectively.

As you’ve specified the source charge as Internal, the system pulls the costs from the internal cost distribution of the

freight order. The pulled execution cost has all the charge lines from freight order 1.

As you’ve specified the cost pull strategy as Inactive Copy, you can’t edit the charge lines.

Example 3:

You specify the cost pull strategy as Inactive Copy and the source charge as External & Internal in the calculation sheet.

When you calculate charges in the forwarding order 1, the following happens:

The system calculates the charges and displays them on the Charges tab. The system displays the costs pulled from the

freight order under the cost charge line.

The system creates four charge lines for the following charges:

Haulage charges – USD 1680

Loading charges – USD 560

Loading charges – USD 560

Basic charges – USD 110.89

From the freight order, the system also pulls and displays the above values for the calculated amount and final amount.

As you’ve specified the source charge as External & Internal, the system pulls the costs from both the internal and external

cost distribution of the freight order. The pulled execution cost has all the charge lines from freight order 1.

As you’ve specified the cost pull strategy as Inactive Copy, you can’t edit the charge lines.

Example 4:

You specify the cost pull strategy as Active Copy and the source charge as Own Internal in the calculation sheet.

When you calculate charges in the forwarding order 1, the following happens:

The system calculates the charges and displays them on the Charges tab. The system displays the costs pulled from the

freight order under the cost charge line.

The system creates two charge lines; one for the loading charges and one for the haulage charges. From the freight order,

the system pulls and displays the calculated amount and final amount as USD 560 and USD 1680 for the loading charges

and haulage charges respectively.

As you’ve specified the source charge as Own Internal, the system pulls the costs from the Internal Charges tab page to

the Charges tab page within the same forwarding order. The pulled execution cost has all the charge lines from internal

charges of the forwarding order.

This is custom documentation. For more information, please visit SAP Help Portal.

235


1/14/26, 2:16 PM

As you’ve specified the cost pull strategy as Active Copy, you can edit the rate amount and currency.

  Note

You can you use the own internal source charge only for external charge calculation in a forwarding order.

The own internal source charge works irrespective of the source of internal charges in a forwarding order.

That is, you can use own internal source charge even when the internal charges aren’t based on the cost pull scenario.

Example 5:

You specify the cost pull strategy as Aggregate and the source charge as External in the calculation sheet.

When you calculate charges in the forwarding order 1, the following happens:

The system calculates the charges and displays them on the Charges tab. The system displays the costs pulled from the

freight order in a standard line under the cost charge line.

The standard line has the calculated amount and final amount as USD 670.89, which is the sum of loading charges and

basic charges (USD 560 + USD 110.89).

As you’ve specified the source charge as External, the system pulls the costs from the external cost distribution of the

freight order.

As you’ve specified the cost pull strategy as Aggregate, the pulled execution cost has the total distributed cost from the

freight order.

Example 6:

You specify the cost pull strategy as Aggregate and the source charge as Internal in the calculation sheet.

When you calculate charges in the forwarding order 1, the following happens:

The system calculates the charges and displays them on the Charges tab. The system displays the costs pulled from the

freight order in a standard line under the cost charge line.

The standard line has the calculated amount and final amount as USD 2240, which is the sum of haulage charges and

loading charges (USD 1680 + USD 560).

As you’ve specified the source charge as Internal, the system pulls the costs from the internal cost distribution of the

freight order.

As you’ve specified the cost pull strategy as Aggregate, the pulled execution cost has the total distributed cost from the

freight order.

Example 7:

You specify the cost pull strategy as Aggregate and the source charge as Internal & External in the calculation sheet.

When you calculate charges in the forwarding order 1, the following happens:

The system calculates the charges and displays them on the Charges tab. The system displays the costs pulled from the

freight order in a standard line under the cost charge line.

The standard line has the calculated amount and final amount as USD 2910.89, which is the sum of loading charge, basic

charge, haulage charge, and loading charge (USD 560 + USD 110.89 + USD 1680 + USD 560).

This is custom documentation. For more information, please visit SAP Help Portal.

236


1/14/26, 2:16 PM

As you’ve specified the source charge as Internal & External, the system pulls the costs from the internal and external cost

distribution of the freight order.

As you’ve specified the cost pull strategy as Aggregate, the pulled execution cost has the total distributed cost from the

freight order.

Example 8:

You specify the cost pull strategy as Aggregate and the source charge as Own Internal in the calculation sheet.

When you calculate charges in the forwarding order 1, the following happens:

The system calculates the charges and displays them on the Charges tab. The system displays the costs pulled from the

freight order in a standard line under the cost charge line.

The standard line has the calculated amount and final amount as USD 2910.89, which is the sum of loading charge, basic

charge, haulage charge, and loading charge (USD 560 + USD 110.89 + USD 1680 + USD 560).

As you’ve specified the source charge as Own Internal, the system pulls the costs from the Internal Charges tab page to

the Charges tab page within the same forwarding order.

As you’ve specified the cost pull strategy as Aggregate, the pulled execution cost has the total distributed cost from the

freight order.

  Note

You can you use the own internal source charge only for external charge calculation in a forwarding order.

The own internal source charge works irrespective of the source of internal charges in a forwarding order.

That is, you can use own internal source charge even when the internal charges aren’t based on the cost pull scenario.

Rate Split

## Use

After calculating transportation charges, you can split the charge lines in the freight booking for air waybill printing purposes.

## Integration

This function is used in the air freight charge calculation process. For more information, see Air Freight Charge Calculation.

## Features

The Air Waybill View displays only the weight-based charge lines under the air waybill charge item. You can split weight-based

charge lines under the air waybill charge item.

When you insert a split line, the system copies certain parameters from the main charge line. For the inserted charge line, you can

enter values for the following attributes:

Rate category

## Chargeable weight

This is custom documentation. For more information, please visit SAP Help Portal.

237


1/14/26, 2:16 PM

Gross weight

Number of pieces

## Commodity code

Reference percentage of class rate

  Note

You can only edit the chargeable weight and not the number of pieces and gross weight information in the main charge line.

Also, you can only insert a maximum of eleven split charge lines.

The system subtracts the logistical data values of the inserted charge lines from the corresponding logistical values of the main

charge line.

A summary line displays the total values of quantity, gross weight, and chargeable weight of all the charge lines under the air

waybill charge item. A header line displays the initial values of quantity, gross weight, and chargeable weight from the logistical

data and charges data.

In the Air Waybill View, you can choose to switch from ULD rate category to general cargo rate category or specific commodity

rate category. When you do so, the system refers to the logistical data of loose cargo. Note that you cannot revert back to the ULD

rate category after you switch to the general cargo rate category or specific commodity rate category. However, if you use the

Reset button in the Air Waybill View, the system reverts back to the original copy and resets all the changes you have made in the

Air Waybill View.

## Activities

You can navigate to the Air Waybill View from the View button on the Charges tab page to split charge lines.

More Information

## Charge Calculation

Air Freight Charge Calculation

## Use

You can use Transportation Management (TM) to calculate air freight charges based on the following:

TACT rates published by the International Air Transport Association (IATA)

Air freight transportation charges are calculated based on TACT rules and regulations. For more information, see TACT

Rates.

Contract rates available in standard rate tables in TM

For more information, see Rate Table.

## Prerequisites

You’ve defined a calculation profile with the calculation level at header level in Customizing for Transportation

Management under  Basic Functions

 Charge Calculation

## Basic Settings

 Define Calculation Profiles .

This is custom documentation. For more information, please visit SAP Help Portal.

238


1/14/26, 2:16 PM

You’ve defined a settlement profile with the calculation option as Copy All ChargesTransportation Management under

## Settlement

 Define Settlement Profiles .

You’ve assigned the calculation profile and settlement profile defined above to an organizational unit in Customizing for

Transportation Management in Customizing for under  Basic Functions

 Charge Calculation

 Basic Settings

## Define

Charges Profiles .

You’ve defined the transportation mode category as Air for the charge types you want to use for air freight.

You define charge types in Customizing for Transportation Management under

 in Customizing forBasic Functions

 Charge Calculation

 Basic Settings

 Define Charge Types .

You have made the master data settings for the Charge Management and Service Product Catalogs component (see

Charge Management Settings for Air Freight).

## Process

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

1. You trigger charge calculation for the air freight booking from the Freight Order Management component of Transportation

Management (TM).

For more information, see Management of Air Freight Bookings for Airlines.

The system determines the air waybill (AWB) printing and settlement based on TACT rates or contract rates, depending on

the calculation profile settings. If the system doesn’t determine the AWB printing and settlement, you can also manually

enter the values on the Charges tab page of the air freight booking. The system creates two charge items, one for AWB

printing and the other for the settlement with the carrier. The system prints the charge calculation details, based on the

settings that you maintain on the Charges tab page of the air freight booking for printing freight charges and other charges.

  Note

Based on the calculation sheet settings, the system displays the IATA charge code and the charge due for other charges.

The system displays the additional charges and commission only under the settlement charge item. Since these

charges aren’t printed on the AWB, these charges don’t appear in the AWB charge item.

You can enter a description for the nature of goods, which is printed in the AWB.

The system determines whether the payment is on the import side or export side based on the charge type classification

and the freight term.

2. The system either activates or deactivates the charges based on the traffic direction, charge due, and payer, for example:

Due agent charges are activated on the export freight booking irrespective of the payer.

Due carrier prepaid charges are active on the export freight booking and inactive on the import freight booking.

Due carrier collect charges are deactivated on the export freight booking and activated on the import freight

booking.

3. Depending on whether you’re using TACT rates or contract rates, the process continues as follows:

Rate Type

Next Steps

## TACT

a. The system chooses the unit load device (ULD) rate table, specific commodity rate

(SCR) table, or general cargo rate (GCR) table based on the rate category you specify on

This is custom documentation. For more information, please visit SAP Help Portal.

239


1/14/26, 2:16 PM

Rate Type

## Next Steps

the Charges tab page of the freight order. The system determines the rate class based

on the rate category and chargeable weight. Note that the system determines the TACT

rates based on chargeable weights only.

If you specify the rate category as a class rate, you can specify either a percentage

reduction or a percentage surcharge to a reference rate class depending on the type of

goods.

If you use no rate lookup, rates are not determined or calculated for the charge line and

you can maintain blank or zero value for the chargeable weight.

b. If you don’t specify a rate category, the system follows the access sequence to

determine the charges. Depending on the logistical item type, the system determines

the economical rate. For ULDs, the access sequence is as follows:

i. ULD

ii. SCR

iii. GCR

For packages and loose cargo, the access sequence is as follows:

i. SCR

ii. GCR

Note that the system follows the access sequence only if you maintain the resolution

base as Main_Item.

If the system chooses a GCR, the system compares the calculated charge with the

minimum charge. If the calculated charge is less than the minimum charge, the system

chooses the minimum charge.

Note that for the system to choose an SCR rate table, you must have maintained the

commodity item code on the Capacity and Cargo tab page of the air freight booking.

a. You manually define the access sequence in the calculation sheet using the Line Item

Selection instruction type. For more information, see Calculation Sheet.

b. You can’t specify the rate category since the system determines the rate category based

on the charge calculation. As a result, rate class is also an output of charge calculation.

c. If there are special handling requirements for the shipment, you can specify a handling

code in the air freight booking. For example, handling code DGR specifies dangerous

goods. You can calculate the charges for charge types based on specific handling codes.

If there are multiple handling codes and corresponding rates in the same air freight

booking, the system displays all the available rates. You can manually choose a handling

code with which you want to charge the customer.

Contract

  Note

You can manually insert a charge line. For a manually-inserted charge line, you can enter the rate category, rate class,

rates, calculation rule, and chargeable weight. If you’ve specified the rate class as B rate or M rate, the calculated

amount is the same as the rate you’ve specified. The system doesn’t calculate the charges based on the chargeable

weight.

4. You specify the calculation method as either Air Freight: Standard Rating or Air Freight: Break-Weight Rating.

This is custom documentation. For more information, please visit SAP Help Portal.

240


1/14/26, 2:16 PM

Based on the calculation method you specify, the system uses the break-weight or standard rate determination process as

appropriate. Note that for ULD rates, the standard rate determination process supports break-weight calculation methods.

For more information, see Calculation Methods.

  Note

If you selected to group the charge types, the system consolidates multiple packages and ULDs, based on the following

criteria.

The system consolidates multiple packages if the packages have the following attributes in common:

Commodity code (valid for SCR)

Rate category (valid for TACT rates)

Rate table (valid for contract rates)

The system consolidates multiple ULDs if the ULDs have the following attributes in common:

Commodity code (valid for SCR and ULD rates)

Rate category (valid for TACT rates)

Rate table (valid for contract rates)

## ULD rate type

If the ULDs and packages have the rate category as GCR, the system consolidates multiple packages and ULDs. Note

that the system uses the GCR rates for ULDs only when you don’t maintain ULD rates. Also, for the system to

consolidate packages and ULDs, they must have the following attributes in common:

Rate category

## ULD rate type

Commodity code (valid for SCR and ULD rates)

You can group charge types in Customizing for Transportation Management under  Basic Functions

## Charge

Calculation

## Basic Settings

 Define Charge Types . If you didn’t select this option, the system determines the rates

for individual packages and ULDs.

The system determines multiple rates when one or more attributes are missing in the air freight booking. For example, if

the note information isn’t maintained in the air freight booking and you’re maintaining rates for carrier-specific notes, the

system determines multiple carrier-specific rates from which you can select the appropriate rate. Note that you can’t

determine multiple rates for a B rate, a K rate, or a ULD rate. For more information, see Rate Determination with Partial

Information.

During contract-based charge calculation, the system can determine the correct rate even when you maintain a rate for a

specific weight break that belongs to a combination of same scale. Note that for a combination of same scale values, if you

maintain rates for more than one weight break, the system doesn’t calculate the correct charges.

  Example

You specify the following attributes in a rate table:

## Source

Destination

ULD Rate

<=200 kg

>201 kg

<=300 kg

>301 Kg

<=400 kg

>401 Kg

Location

Location

Type

A

D

08

USD 250

USD 1 per

kg

This is custom documentation. For more information, please visit SAP Help Portal.

241


1/14/26, 2:16 PM

## Source

Destination

ULD Rate

<=200 kg

>201 kg

<=300 kg

>301 Kg

<=400 kg

>401 Kg

Location

Location

Type

B

C

D

D

08

08

USD 650

USD 2 per

kg

USD 1250

USD 3 per

kg

In the FWO, you specify the ULD rate type as 08, source location as B, and the destination location as D for a freight unit

of 350 kg.

During charge calculation, the system determines the rate table item for ULD rate type 08, source location B, and

destination location D and calculates the transportation charges as USD 700 (350 kg * USD 2). Note that the system

displays the charges for the pivot weight and the over-pivot weight in two separate lines. You can view the air freight

messages on the Charge Analysis tab page.

5. If the main item in the cargo is a ULD, the system calculates the chargeable weight by comparing the net weight with the

dimensional weight. If the main item in the cargo isn’t a ULD, the system calculates the chargeable weight by comparing the

gross weight with the dimensional weight.

The system chooses the highest weight as the chargeable weight.

You maintain the gross weight and gross volume on the Capacity and Cargo tab page of the air freight booking. The system

calculates the dimensional weight using the gross volume and the dimensional weight factor maintained in the dimensional

weight profile. You maintain a dimensional weight profile either in the calculation sheet, agreement, or calculation profile.

You can also modify the chargeable weight manually. If the chargeable quantity is less than the first weight break of 1 kg,

the system applies the rate for 1 kg and calculates the charges. Note that if you modify the chargeable weight, the system

recalculates the charges.

You define dimensional weight profiles in Customizing for Transportation Management under  Basic Functions

## Charge

## Calculation

## Data Source Binding

 Define Dimensional Weight Profiles .

6. The system rounds the chargeable weight based on the rounding profile you maintained in the rate table.

The system rounds the dimensional weight in each charge line before calculating the total charges. Dimensional weight

rounding is based on the rounding rule you specify in the dimensional weight profile.

  Note
The air freight charge calculation works in a different manner in the following scenarios:

## Direct Shipments

For direct shipments that aren’t consolidated and have to be forwarded as soon as possible, you can charge the

customer based on the AWB printing charges in the air freight booking.

Using the air_cost calculation method, the system can copy the AWB printing charges in the air freight booking as

the settlement amount for the main carriage in the forwarding order. The system deactivates the sub-charge lines in the

forwarding order and uses only the total charge for settlement. Note that you can determine the AWB printing charges

irrespective of whether the printing calculation is TACT-based or contract-based. For more information, see Air Waybill

Direct Cost Pull.

Air freight bookings with general sales agents (GSAs)

If the airline (issuing carrier) has a GSA operating at the source location, you can calculate the charges based on the

agreement with the GSA. You can maintain a freight agreement with the general sales agent (GSA) specifying the GSA

as the business partner in the freight agreement. In the Items screen area, you can specify the airline code that the GSA

This is custom documentation. For more information, please visit SAP Help Portal.

242


1/14/26, 2:16 PM

represents. In the freight booking, on the Booking tab page, you can specify the airline code that the GSA represents,

and you can specify the local carrier as GSA in the Issuing Carrier Airline Code/Local Carrier field.

During charge calculation, the system determines a rate based on the agreement with the GSA. Note that if you haven’t

maintained an agreement with GSA, the system determines the agreement with the airline.

## Charge calculation based on volumetric weight factor

Sometimes, lightweight packages and unit load devices (ULDs) occupy large volumes of space in an aircraft. Therefore,

the space in the aircraft becomes fully occupied even before reaching its maximum weight capacity. In such cases, the

system calculates the charges based on volumetric weight factor. The volumetric weight factor is calculated using the

following formula:

## Volumetric weight factor = Volume/Weight

You can maintain rates for the volumetric weight factor in cubic centimeter per kilogram (ccm/kg) in the rate table.

  Note

Before calculating the volumetric weight factor, the system converts the unit of measure (UoM) for volume into

ccm and the UoM for weight into kg if the volume and weight are specified in any other UoM.

To enable the system to calculate the volumetric weight factor, you must specify the volume of the package or

ULD in the order.

For ULDs, the system uses the net weight to calculate the volumetric weight factor. For packages, the system

uses the gross weight to calculate the volumetric weight factor.

## More Information

Standard Charge Calculation

Forwarding Order Management

Air Waybill Direct Cost Pull

## Use

Transportation Management enables you to use execution costs as a basis for settling with your customers or internal

organization. In this scenario, you can transfer the charge lines from the air waybill charge item to the forwarding side. You can

charge customers for total or partial execution charges and additional charges using the cost pull calculation method.

## Integration

The system pulls the costs from the air waybill to the forwarding order during the air freight charge calculation process. For more

information, see Air Freight Charge Calculation.

For more information on standard cost pull feature, see Cost Pull.

## Prerequisites

You have made the master data settings for the Charge Management and Service Product Catalogs component (see Charge

Management Settings for Air Freight).

This is custom documentation. For more information, please visit SAP Help Portal.

243


1/14/26, 2:16 PM
## Features

You can copy charge lines from the air waybill charge item to the forwarding order as either active or inactive charge lines. Copying

charge lines as active enables you to edit charge lines in the forwarding order. You specify the cost pull strategy as Active Copy or

Inactive Copy in the calculation sheet or the local calculation sheet.

  Note
When you specify the cost pull strategy as Active Copy, the system enables the Source Charge field. For the system to copy

individual charge lines from the air waybill charge item to the forwarding order, you must use air waybill as the source charge.

Also, when you use air waybill as the source charge, the system considers the following freight order attributes to calculate the

final amount in the forwarding order:

Calculation rule

Calculation base

## Calculated amount

If you don’t specify a value in the source charge field, the system copies the distributed charge lines in the freight order to the

forwarding order.

Based on the freight term and the Incoterm you specify in the forwarding order, the system settles the charges to the shipper,

ship-to party, import business unit, or export business unit as appropriate.

Based on the freight term, you determine whether the payment is on the import side or export side. Based on the Incoterm, you

identify who pays for the individual stages of a transport.

## Example

You have a forwarding order with the Incoterm EXW (Ex Works). According to EXW, the ship-to party pays for all the stages in the

forwarding order. However, the precarriage and the main carriage stages are executed by the export business unit on behalf of the

import business unit. So, there’s an internal settlement between the export business unit and the import business unit.

Based on the freight term you specify in the forwarding order, one of the following happens:

## Freight term PP

If you specify the freight term as PP, all the charges are prepaid in both the export freight booking and the import freight

booking. Prepaid charges are active in the export freight booking and collect charges are active in the import freight

booking.

Export Freight Booking

Charge Type Amount

Freight Term Status

FB00

100

Prepaid

Active

SCC1

DOCF

20

30

Prepaid

Active

Prepaid

## Active

## Import Freight Booking

This is custom documentation. For more information, please visit SAP Help Portal.

244


1/14/26, 2:16 PM

Charge Type Amount

Freight Term Status

FB00

100

Prepaid

Inactive

SCC1

DOCF

20

30

Prepaid

Inactive

Prepaid

## Inactive

During charge calculation, the following happens:

1. The charge types in the export freight booking are pulled into the export forwarding order and the export business

unit internally charges the import business unit 150 USD for the prepaid charges.

2. The charges in the import freight booking are pulled into the import forwarding order and the import business unit

charges the ship-to party 150 USD.

## Freight term CC

If you specify the freight term as CC, all the charges are collect in both the export freight booking and the import freight

booking. Collect charges are active in the import freight booking.

Export Freight Booking

Charge Type Amount

Freight Term Status

FB00

100

Collect

Inactive

SCC1

DOCF

20

30

Collect

Inactive

Collect

## Inactive

Import Freight Booking

Charge Type Amount

Freight Term Status

FB00

100

Collect

Active

SCC1

DOCF

20

30

Collect

Active

Collect

## Active

The system doesn’t calculate the charges in the export forwarding order since all the charges are collect in the export

freight booking.

During charge calculation in the import forwarding order, the charges in the import freight booking are pulled into the

import forwarding order and the import business unit charges the ship-to party 150 USD.

## Freight term PC

If you specify the freight term as PC, the weight charges are prepaid and the other charges are collect in both the export

freight booking and the import freight booking. Prepaid charges are active in the export freight booking and collect charges

are active in the import freight booking.

## Export Freight Booking

This is custom documentation. For more information, please visit SAP Help Portal.

245


1/14/26, 2:16 PM

Charge Type Amount

Freight Term Status

FB00

100

Prepaid

Active

SCC1

DOCF

20

30

Collect

Inactive

Collect

## Inactive

Import Freight Booking

Charge Type Amount

Freight Term Status

FB00

100

Prepaid

Inactive

SCC1

DOCF

20

30

Collect

Active

Collect

## Active

During charge calculation, the following happens:

1. The charge types in the export freight booking are pulled into the export forwarding order and the export business

unit internally charges the import business unit 100 USD for the prepaid charges.

2. The charges in the import freight booking are pulled into the import forwarding order and the import business unit

charges the ship-to party 150 USD.

## Fuel Surcharge Calculation

Due to uncertainties in fuel prices, it is significant to charge the customer appropriately based on the fuel surcharge index

published by the government. As a logistics service provider or carrier, you need to recover, the additional charges incurred due to

varying fuel costs. Transportation Management simplifies the fuel surcharge calculation by providing an easy-to-maintain fuel

surcharge calculation method.

You can determine fuel surcharge based on two different models. For more information, see Fuel Surcharge Calculation: Model 1

and Fuel Surcharge Calculation: Model 2.

Fuel Surcharge Calculation: Model 1

## Use

You can calculate the fuel surcharge based on a fuel surcharge model widely used in North America. In this model, you calculate

the fuel surcharge based on the fuel surcharge index published by the government. The fuel surcharge index is based on the origin

location or zones.

## Prerequisites

You’ve defined a calculation profile in Customizing for Transportation Management under  Basic Functions

## Charge

Calculation

## Basic Settings

 Define Calculation Profiles .

You’ve assigned the calculation profile to a charges profile in Customizing for Transportation Management under  Basic

## Functions

 Charge Calculation

## Basic Settings

 Define Charges Profiles .

This is custom documentation. For more information, please visit SAP Help Portal.

246


1/14/26, 2:16 PM

You’ve assigned the charges profile to an organizational unit in the transaction PPOME.

## Process

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

To calculate the fuel surcharge, you must maintain two rate tables; a standard rate table with the fuel surcharge rates for

corresponding fuel surcharge values, and an index rate table with the location, dates or validity, and the respective fuel surcharge

values. You proceed as follows:

1. Define an index base rate table.

Define an index rate table with the fuel surcharge values based on scale items such as location and calculation date. You

can define a calculation rule on the Calculation Rules tab page.

2. Define a standard rate table.

Define a standard rate table with the calculation base as FSC and scale type as either Base Scale or To Scale. Define the

rates for fuel surcharge values.

  Note

You define rate tables in the Create Rate Table Definition app on the launchpad. For more information, see Rate Table.

3. Define a calculation sheet with a charge item for fuel surcharge and define the following attributes:

Enter the charge type as Fuel.

Enter the standard rate table in the Rate Table field and the index rate table in the Index Rate Table field.

Enter the calculation method type as C and calculation method as FUEL_SURCHARGE in the Basic Data tab page.

  Note

You define calculation sheets in the Create Calculation Sheet app on the launchpad. For more information, see

Calculation Sheet.

4. Trigger charge calculation.

You can trigger charge calculation from a forwarding order or freight order.

5. The system determines the fuel surcharge and calculates the transportation charges along with the fuel surcharge.

Based on the location and date specified in the forwarding order or freight order, the system determines a fuel surcharge

value from the index rate table. The system then uses this fuel surcharge value to determine a rate from the standard rate

table.

## Example

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

You maintain an index rate table with the following fuel surcharge values:

## Calculation Date

Source Location: A Source Location: B Source Location: C

09-05-2013

3.12

3.99

3.45

This is custom documentation. For more information, please visit SAP Help Portal.

247


1/14/26, 2:16 PM

## Calculation Date

Source Location: A Source Location: B Source Location: C

09-12-2013

09-19-2013

3.24

3.15

3.78

4.12

3.65

3.55

You maintain the scale type as To Scale.

You maintain a standard rate table with the following rates for fuel surcharge values:

Fuel Surcharge Value Rate (USD)

3.12

3.15

3.24

3.42

3.55

3.62

3.75

3.97

4.10

0.33

0.35

0.41

0.43

0.47

0.49

0.53

0.62

0.68

You have a calculation profile with the calculation date type as Order Date. You have a forwarding order with the Order Date as

09.10.2013 and the Source Location as B.

As you’ve specified the calculation date as To Scale (less than or equal to), the system determines a fuel surcharge value of 3.78,

which you’ve maintained for the date 09.12.2013 for location B.

Now, the system determines a rate for the fuel surcharge value 3.78 from the standard rate table. If you maintain the scale type as

Base Value (greater than or equal to) in the standard rate table, the system picks the rate of 0.53, which is maintained for 3.75 (as

3.78 is >=3.75) to calculate fuel surcharge. If you’ve maintained the scale type as To Value (less than or equal to) in the standard

rate table, the system picks the rate of 0.62, which is maintained for 3.97 (as 3.78 is <=3.97) to calculate fuel surcharge.

## More Information

Fuel Surcharge Calculation: Model 2

Rate Definition and Maintenance

## Agreement Maintenance

Fuel Surcharge Calculation: Model 2

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

248


1/14/26, 2:16 PM

You can calculate the fuel surcharge based on a base fuel surcharge value. The logistic service provider or carrier agrees with the

customer on an index base date based on which the system determines the base fuel surcharge value. The actual fuel surcharge is

calculated based on the current fuel surcharge value and base fuel surcharge value.

## Prerequisites

You’ve defined a calculation profile in Customizing for Transportation Management under  Basic Functions

## Charge

Calculation

## Basic Settings

 Define Calculation Profiles .

You’ve assigned the calculation profile to a charges profile in Customizing for Transportation Management under  Basic

## Functions

 Charge Calculation

## Basic Settings

 Define Charges Profiles .

You’ve assigned the charges profile to an organizational unit in the transaction PPOME.

## Process

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

To calculate the fuel surcharge, you define an index base rate table with the fuel surcharge values for specific calculation dates or

validities. Optionally, you can define a standard rate table with the fuel surcharge values for scale items such as location and

calculation dates or validity periods. You proceed as follows:

1. Define an index base rate table.

Define an index rate table with the calculation base as Calculation Date, scale type as To Scale or Base Scale, and the

value type as Absolute or Percentage. Note that you must not maintain a calculation rule in this rate table.

  Note
You define rate tables in the Create Rate Table Definition app on the launchpad. For more information, see Rate Table.

2. Optionally, you can define a standard rate table.

Define a standard rate table with a calculation base and scale type as either Base Scale or To Scale. Define the fuel

surcharge values for scale items such as source location and destination location.

  Note

If you don’t define a standard rate table, the system determines the fuel surcharge using the base rate specified in the

calculation sheet.

3. Define a calculation sheet with a charge item for fuel surcharge and define the following attributes:

Enter the charge type as Fuel.

Enter the index rate table in the Index Rate Table field.

Enter an index base date in the Index Base Date field.

If you’ve defined a standard rate table, enter it in the Rate Table field. Otherwise, you must enter a rate in the Base

Rate field as a percentage or absolute value.

Enter the calculation method type as C and calculation method as FUEL_SURCHARGE on the Basic Data tab page.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

249


1/14/26, 2:16 PM

You define calculation sheets in the Create Calculation Sheet app on the launchpad. For more information, see

Calculation Sheet.

4. You trigger charge calculation.

You can trigger charge calculation from a forwarding order or freight order.

5. The system determines the current fuel surcharge value.

Based on the calculation date specified in the forwarding order or freight order, the system finds the current fuel surcharge

value from the index rate table.

6. The system determines the base fuel surcharge value.

The system finds the fuel surcharge value for the index base date specified in the calculation sheet from the index rate

table.

Note that for the system to determine the base fuel surcharge value, you must specify an index base date in the Index Base

Date field and specify a fuel surcharge value for the index base date in the index base rate table.

7. The system determines the fuel surcharge and calculates the transportation charges along with the fuel surcharge.

If you don’t define a standard rate table, the system calculates the fuel surcharge using the following formula:

Fuel surcharge in percentage = (Current fuel surcharge value/Base fuel surcharge value)* Base rate in calculation sheet

If you define a standard rate table, the system determines a fuel surcharge value for the scale items in the forwarding order

or freight order and calculates the fuel surcharge using the following formula:

Fuel surcharge in percentage = (Current fuel surcharge value/Base fuel surcharge value)* Fuel surcharge value from the

standard rate table

## Example

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

You maintain an index rate table with the following fuel surcharge values:

Calculation Date

Fuel Surcharge Value

09-05-2013

09-12-2013

09-19-2013

09-25-2013

09-30-2013

3.45

3.65

3.55

3.82

3.91

You maintain the scale type as To Scale.

You maintain a base rate of 1.19% in the calculation sheet.

You have a calculation profile with the calculation date type as Order Date and in the forwarding order, the order date is

09.18.2013 and the Index Base Date maintained in the calculation sheet is 09.28.2013.

This is custom documentation. For more information, please visit SAP Help Portal.

250


1/14/26, 2:16 PM

The system determines the current fuel surcharge using the order date. The order date 09.18.2013 occurs earlier than 09.19.2013

in the index rate table. Hence, the value 3.55 is determined as the current fuel surcharge value.

The system determines the base fuel surcharge using the index base date of 09.28.2013. The index base date 09.28.2013 occurs

earlier than 09.30.2013 in the index rate table. Hence, the value 3.91 is determined as the base fuel surcharge value.

The fuel surcharge is calculated as follows:

Fuel surcharge in percentage = (Current fuel surcharge value/Base fuel surcharge value)* Base rate in calculation sheet

Fuel surcharge in percentage = (3.55/3.91)*1.19 = 1.08

Alternatively, you can also use standard rate tables to calculate the fuel surcharge. You maintain a standard rate table as follows:

Source Location

Destination Location

Fuel Surcharge Value

A

B

C

D

B

C

D

E

3.12

3.15

3.24

3.42

Once the system determines the current fuel surcharge value and the index fuel surcharge value as mentioned above, the system

determines the fuel surcharge value for the source location and destination location specified in the forwarding order. In the

forwarding order, if you’ve maintained the source location as B and the destination location as C, the system determines the fuel

surcharge value of 3.15 from the standard rate table.

The fuel surcharge is calculated as follows:

Fuel surcharge in percentage = (Current fuel surcharge value/Base fuel surcharge value)* Fuel surcharge value from standard rate

table

Fuel surcharge in percentage = (3.55/3.91)*3.15 = 2.86

## More Information

Fuel Surcharge Calculation: Model 1

Rate Definition and Maintenance

Agreement Maintenance

Event-Based Charge Calculation

## Use

Transportation Management (TM) enables you to coordinate between your transportation planning and the actual execution by

exchanging information with SAP Event Management. You can track various events that occur during transportation execution,

such as delays, arrivals, and departures, and enables you to charge the customer appropriately.

This is custom documentation. For more information, please visit SAP Help Portal.

251


1/14/26, 2:16 PM

With the help of SAP Event Management, you can also charge the customer for additional services, such as fumigation and

container cleaning by maintaining events for these services. The system also notifies the progress of the additional services.

## Integration

TM is integrated with SAP Event Management to coordinate between the transportation planning and the actual execution. For

more information, see Help Portal at http://help.sap.com/em .

## Prerequisites

You've specified the data source as Actual Route. You specify the data source in Customizing for Transportation Management

under  Basic Functions

 Charge Calculation

## Basic Settings

 Define Calculation Profiles .

## Features

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

## Event Profile for Charge Calculation

You can control the event handler through the event profile. An event handler represents business processes or business objects

(for example, purchase order, shipment, production order, or handling unit) that are to be tracked within the supply chain by SAP

Event Management. An event handler contains expected, reported, or unexpected events and attributes to identify and track the

related business processes. With the event profile, you can configure events for charge calculation. You can also define the

following rules based on which the system performs the charge calculation in the forwarding order or freight order:

Event code

Event reason

## Event status

Reference event code

Reference event reason

## Reference event status

## Business documents in which the event needs to be charged

For example, forwarding orders, freight orders, internal forwarding orders, and internal freight orders in which the event

needs to be charged.

You can also link service types to the events, which enable you to bill the customer based on services. If you assign a specific

service type to an event code, the system charges the customer for the service when the assigned event code occurs in the

forwarding order or freight order.

You can also maintain different event profiles for the customer and carrier by assigning different event profiles to the forwarding

order type, freight order type, or freight booking type.

  Note
You can also report events at the item level in a freight order. For example, during buyer’s consolidation (consolidation of

multiple forwarding orders), you can report an event for one of the containers and the system calculates the charges for the

event only on related forwarding order that has the container.

This is custom documentation. For more information, please visit SAP Help Portal.

252


1/14/26, 2:16 PM

## Related Calculation Bases

In a calculation sheet, if you enter a calculation rule based on a calculation base that has related calculation bases, you can directly

enter values for the related calculation bases on the Related Calculation Bases tab page.

For example, to calculate charges in the event of demurrage, for the calculation base delay_days, you maintain a related

calculation base grace_days in Customizing for Transportation Management under  Basic Functions

 Charge Calculation

## Data Source Binding

 Define Calculation Bases . In the calculation sheet, you can specify the number of grace days allowed to

the customer.

You can also specify your own calculation rule and charge type using the BRFplus (Business Rule Framework plus) condition. You

can assign the BRF plus rules to the calculation base. The system processes the condition for all the data access definitions based

on the condition you specify. For more information, see BRFplus for Charge Management and SP Catalogs.

## Activities

You define event profiles for charge calculation in Customizing for Transportation Management under  Basic Functions

## Charge

Calculation

## Basic Settings

 Define Charges Profiles . You maintain the event type, event reason, and charge type on the

Define Event Assignment to Charge Type tab page of the Define Event Profiles for Charge Calculation Customizing.

You assign event profiles for charge calculation to forwarding order type in Customizing for Transportation Management under

Forwarding Order Management

## Forwarding Order

 Define Forwarding Order Types .

You assign event profiles for charge calculation to freight order type in Customizing for Transportation Management under

Freight Order Management

## Freight Order

 Define Freight Order Types .

You assign event profiles for charge calculation to freight booking type in Customizing for Transportation Management under

Freight Order Management

## Freight Booking

 Define Freight Booking Types .

You define calculation bases and the related calculation bases in Customizing for Transportation Management under  Basic

## Functions

 Charge Calculation

 Data Source Binding

 Define Calculation Bases .

## Example

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

To calculate demurrage charges, you perform the following:

1. You define the calculation base (for example, delay_days) and the related calculation base (for example, grace_days)

in the Customizing activity Define Calculation Bases.

2. You maintain a calculation sheet with a calculation rule (for example, delay_days) and a charge type (for example,

delay) on the fiori launchpad. Delay_days is calculated by the following formula:

## Delay days = Actual data — Planned data — Grace days

In the calculation sheet, you can define the number of grace days provided to the customer on the Related Calculation

Bases tab page.

3. You define event profiles with a charge type (for example, delay/demurrage) in the Customizing activity Define Event

Profiles for Charge Calculation.

4. The system calculates the demurrage charges based on the calculation rule and the rates you specify in the calculation

sheet.

This is custom documentation. For more information, please visit SAP Help Portal.

253


1/14/26, 2:16 PM

Calculation of Charges for Empty Provisioning and Empty Return

## Use

In Transportation Management, you can request provisioning of empty containers or railcars for providing transportation service in

the future. You can also request for return of the empty containers or railcars. You can then calculate the charges for empty

provisioning, empty return, or empty provisioning with a transportation service.

## Prerequisites

In Customizing, you have carried out the activities for Transportation Management under  Basic Functions

## Charge

Calculation .

You have set up the master data for the Charge Management and Service Product Catalogs component.

For more information, see Setup of MD for Charge Management and SP Catalogs.

You have specified the resolution base as CONTAINER for container items so the system can calculate charges at header

level.

## Features

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

You request empty provisioning or empty return for a container in the forwarding order and specify the charge types for empty

provisioning and empty return in the calculation sheet.

The system compares the empty provisioning and empty return values specified in the forwarding order and calculation sheet,

based on which the system calculates the charges.

Empty provisioning can have one of the following values in the forwarding order and calculation sheet:

Requested (X)

## Not Requested

Provisioning Only (P)

Similarly, empty return can have one of the following values in the forwarding order and calculation sheet:

Requested (X)

Not Requested

Return Only (R)

When you create a request for empty provisioning or empty return with the value as Requested (X), the system creates a technical

item for either empty provisioning (P) or empty return (R) as appropriate in the back end. The system creates a technical item to

include empty provisioning charges or empty return charges along with the freight charges.

You can agree with the shipper on whether you will arrange for the return of containers or you require the shipper to return the

empty containers. Charge calculation varies based on the agreement.

## Example

This is custom documentation. For more information, please visit SAP Help Portal.

254


1/14/26, 2:16 PM

You have an empty provisioning request. In the forwarding order, you specify the following values for provisioning:

## Charge Item

Empty Provisioning

10

80

30

40

Requested (X)

Provisioning Only (P, technical)

## Not Requested

Provisioning Only (P)

Note that the system creates a technical item (P) in the back end for provisioning requested (X).

In the calculation sheet or the local calculation sheet, you specify the following values for the following charge types:

Charge Type

## Description

Empty Provisioning

C1

C2

C3

Basic freight charges

## Not Requested

Freight charges and provisioning charges Requested (X)

Provisioning only charges

Provisioning Only (P)

When you calculate the charges at header level with the resolution base as CONTAINER, the system applies the following charges:

Charge Element Charges

Charge Item

CH1

C1

C1

C2

C3

C3

10

30

10

80

40

The system applies basic freight charges (C1) to the containers when the empty provisioning is Requested (X) and Not

Requested.

The system applies basic freight charges and the provisioning charges (C2) to the containers when the empty provisioning is

Requested (X).

The system applies provisioning charges (C3) to the containers when the empty provisioning is Provisioning Only (R) and the

technical item (P) that is created in the back end for provisioning requested.

## More Information

Empty Provisioning and Empty Return

## Additional Agreement Parties

This is custom documentation. For more information, please visit SAP Help Portal.

255


1/14/26, 2:16 PM

You can calculate transportation charges for each of the additional agreement parties in a freight order or freight booking.

## Use

In a freight order or freight booking, along with the main carrier, you use additional agreement parties for other logistics services

such as export clearance and fumigation of containers.

When you calculate charges for a freight order or freight booking with additional agreement parties, the system calculates the

charges based on the valid agreement between the organization and the main carrier and between the organization and the

additional agreement parties.

You can calculate charges at header, item, or stage level, depending on your Customizing settings in the charges or calculation

profile assigned to the organization, main carrier, or additional agreement parties.

However, if you want to calculate the charges for the main carrier as well as any additional agreement party only at the header level

you've to do the following settings in the Customizing for Transportation Management. Under  Basic Functions

## Define

General Settings for TM , select the checkbox Header Level Charge Calc. in Freight document with Add. Agreement Party.

  Note

In the Business Partner tab of the freight order or freight booking, under Partner Function you add your additional

agreement parties as Addtnl. Agrmt. Party.

You add the main carrier in the General Data tab of the freight order or freight booking.

The system doesn't support quotations, carrier selection, and tendering for additional agreement parties.

## Example

In the following example, you want to transport food items in a container from Rotterdam to New York. The main carrier is CARR01

and the additional agreement party for import/export clearance is AAP01. You pay CARR01 for the transportation service and

AAP01 for the import/export clearance.

The setup for the cargo and service items is:

Item Hierarchy

Active Vehicle 10

Item Type

Quantity

Quantity UoM

Service Type

Container 1000

TRUC

## CONT

Packages

PKG

1

1

10

EA

EA

EA

Service Item

Custom

## Clearance

## Custom Service

Following are the charges in the calculation sheet of the valid freight agreement between the main carrier CAR001 and the

business organization.

Item Hierarchy

Line No.

Charge Type

Amount

Currency

Rate Table

Base Freight

Fuel Surcharge

10

20

BASE_FRT

FSC

100

10

EUR

RT_01

% of Base Freight

This is custom documentation. For more information, please visit SAP Help Portal.

256


1/14/26, 2:16 PM

Following are the charges in the calculation sheet of the valid freight agreement between the additional agreement party AAP01

and the business organization.

Item Hierarchy

Line No.

Charge Type

Amount

Currency

Rate Table

Calculation

Resolution Base

Custom Fee

30

CUSTOM_FEE

EUR

RT_01

## Service

## Header level charge calculation

When you calculate charges at the header level, then the charges for the entire shipment for both the main carrier and additional

agreement party are calculated at header.

Charge Hierarchy Charge Type

Rate Amount

Rate Currency

Final Amount

Doc Currency

CARR01

AAP01

BASE_FRT

FSC

100

10

EUR

EUR

CUSTOM_FEE

50

EUR

110

100

10

50

50

EUR

EUR

EUR

EUR

EUR

Related Information

Charge Calculation

## Freight Settlement

## Features of Dispute Management

Freight Settlement for Additional Agreement Parties

Dispute Management with Additional Agreement Parties

## Freight Settlement for Additional Agreement Parties

You can create a freight settlement document (FSD) for each of the additional agreement parties that are contained in a freight

order or freight booking.

## Use

When you create a freight settlement document from the freight order or freight booking, the system displays a dialog box if

additional agreement parties exist in the freight order or freight booking. You can select one or more parties and continue with the

settlement process.

  Note

You can't enter the details of the services provided by an additional agreement party in a freight order or freight booking.

Instead, you can use the charge type in the freight agreement to record the service.

If you've overlapping services between the carrier and an additional agreement party, the system issues an FSD for the

overlapping services to both parties. For example, you've a freight agreement with a carrier in which the carrier provides both

transportation and fumigation services. You also have an additional agreement party that provides a fumigation service. You've

a freight order in which the carrier provides transportation services and the additional agreement party provides a fumigation

This is custom documentation. For more information, please visit SAP Help Portal.

257


1/14/26, 2:16 PM

service. The system creates an FSD that includes a charge for the fumigation service for both parties. You must manage this

situation outside of the system.

If you've more than one calculation sheet to cover different services from the same additional agreement party or carrier, the

system can't differentiate between the different calculation sheets. It uses just one calculation sheet when it creates an FSD.

For example, you've a carrier that provides both carrier and fumigation services. In your system, you've one calculation sheet

for transportation charges and a second calculation sheet for fumigation charges. You've a freight order in which the same

carrier provides transportation and fumigation services. The system uses just one calculation sheet to create the FSD, and you

can't create an FSD that includes both charges. Again, you must manage this situation outside of the system.

The system doesn't support quotations, carrier selection, and tendering for additional agreement parties.

Related Information

Charge Calculation

## Freight Settlement

## Features of Dispute Management

Dispute Management with Additional Agreement Parties

## Dispute Management with Additional Agreement Parties

You can maintain multiple disputes in a dispute management scenario, if you specify one or more additional agreement parties in

your freight document. In some of the transportation scenarios, you as a requester of transportation services, can have multiple

service providers execute a single freight document.

For example, you've a transportation requirement to transport goods from one location to another. You also require additional

services such as export clearance and fumigation from a service provider. In Transportation Management (TM), you can capture

these requests in a single freight document. You can specify the details of the executing carrier and the additional agreement party

who performs the additional services in the freight document.

In such scenarios, you've to maintain multiple disputes with multiple service providers. TM enables you to create and maintain

multiple disputes in a single freight document. You can maintain multiple disputes in a freight document that has one or both of

the following:

One or more additional agreement parties

## Multiple invoicing carriers

For more information on freight documents and non-linear stages, see Freight Orders with Non-Linear Stages.

Related Information

Charge Calculation

## Freight Settlement

## Features of Dispute Management

Freight Settlement for Additional Agreement Parties

## Freight Charges for Service Providers

In freight transportation, the main carrier is responsible to provide the transportation service. Apart from the main carrier, there

can be other service providers who are responsible for additional services, such as fumigation, custom clearance, insurance, and

This is custom documentation. For more information, please visit SAP Help Portal.

258


1/14/26, 2:16 PM

so on. These additional services are service items in a freight order or freight booking. For a freight order or freight booking, you

can calculate transportation charges for the transportation service by the main carrier and the additional services by the service

providers.

## Use

For each service item, you can assign a service provider and also can add details about the service location and duration, which are

used with other logistical information to determine the rates for specific service charges. The system calculates the charges based

on the valid freight agreements between the main carrier and the business organization and the service provider and business

organization.

For service providers, the system can calculate charges at service item or header level. But for main carrier, the system calculates

the charges depending on the Customizing settings in the charges profile or calculation profile assigned to the organization or

business partner.

For calculating service charges based on the service location and duration, you use calculation bases SRV_LOCATION and

SRV_DURATION in the rate table along with resolution base SERVICE in the calculation sheet.

For a freight order or freight booking, you add service provider under the Items tab in a freight order or freight booking. Select

Charge Hierarchy as Service Items Only. If you require a service that is provided by a service provider that isn't the carrier, select

the Item Specific Service Provider checkbox, enter the name of the business partner under Business Partner, and select the

service type.

For more information, see Service Items.

  Note

The system doesn't support quotations, carrier selection, and tendering for service providers.

For service items with no service providers, the service charges are included with main carrier.

## Example

You've a freight order with main carrier CAR001 with the following cargo and service items and service provider SRV_PR01

assigned to the service items:

## Item

Hierarchy

## Active

Vehicle 10

Item Type

Quantity

Quantity

Service

Business

Item

UoM

## Type

Partner

Specific

Service

Provider

Container

1000

TRUC

## CONT

Product 10

PRD

Service 10

SRV

Service 20

SRV

1

1

10

3

1

EA

EA

EA

EA

EA

Inspection

SRV_PR01

X

## Fumigation

This is custom documentation. For more information, please visit SAP Help Portal.

259


1/14/26, 2:16 PM

Following are the charges in the calculation sheet of the freight agreement between the main carrier CAR001 and the business

organization.

Item Hierarchy

Line No.

Charge Type

Amount

Currency

Rate Table

Calculation

Base Freight

Fumigation

Charges

10

20

BASE_FRT

100

FUMI_CHRG

75

EUR

EUR

Resolution Base

## Service

Following are the charges in the calculation sheet of the freight agreement between the service provider SRV_PR01 and the

business organization.

Item Hierarchy

Line No.

Charge Type

Amount

Currency

Rate Table

Calculation

Resolution Base

Inspection

Charges

30

INSP_CHRG

50

EUR

RT_01

## Service

Following are the charge calculation scenarios based on the level of charge calculation:

## Header level charge calculation

When you calculate charges at the header level, then the charges for the entire shipment for both the main carrier and service

provider are calculated at header level, which is (175 + (50*3)) = 325 EUR.

Fumigation charge is calculated for main carrier CAR001 as there's no specific service provider for this additional service. The

inspection charges are calculated for the service provider SRV_PR01.

Charge

Charge

Rate

## Rate

Hierarchy

Type

Amount

Currency

Price

Unit

## UoM

Quantity

Calculation

Final

Doc

Base

Amount

Currency

CAR001

SRV_PR01

## Base

Freight

100

EUR

Fumigation

75

EUR

Charges

175

100

EUR

EUR

75

EUR

150

Inspection

50

EUR

1

EA

3

QUANTITY_VAL

150

EUR

## Charges

## Item level charge calculation

When you calculate charges at the item level, then the charges for the entire shipment are broken down for individual charge items.

There are three items for the main carrier and one service item for the service provider. For the main carrier, the total amount is

(100+75+100) = 275 EUR and for the service provider the amount is (50*3) = 150 EUR. Thus, the final amount is (275+150) = 425

EUR.

This is custom documentation. For more information, please visit SAP Help Portal.

260


Charge

Rate

Rate

Price

## UoM

Quantity

Calculation

Final

Doc

Type

Amount

Currency

Unit

Base

Amount

## Currency

1/14/26, 2:16 PM

Charge

Hierarchy

CAR001

Container

1000

Service

20

## Base

Freight

100

EUR

Fumigation

75

EUR

Charges

## Base

Freight

100

EUR

SRV_PR01

EUR

275

175

100

EUR

75

EUR

100

100

EUR

150

Inspection

50

EUR

1

EA

3

QUANTITY_VAL

150

EUR

## Charges

## Stage level charge calculation

When you calculate charges at the stage level, then the charges for the entire shipment are broken down based on the stages of

the main carrier and the service provider. There's one stage for the main carrier, so the total amount is (100+75) = 175 EUR and for

the service provider charge is always calculated at the header level, so the amount is (50*3) = 150 EUR. The final amount is

(175+150) = 325 EUR.

Charge

Hierarchy

CAR001

Loc A

to Loc

B

SRV_PR01

Charge

Rate

Rate

Price

## UoM

Quantity

Calculation

Final

Doc

Type

Amount

Currency

Unit

Base

Amount

Currency

## Base

Freight

100

EUR

Fumigation

75

EUR

Charges

175

100

EUR

75

EUR

150

Inspection

50

EUR

1

EA

3

QUANTITY_VAL

150

EUR

## Charges

## Additional Information

You can also settle freight charges for service providers.

## Related Information

This is custom documentation. For more information, please visit SAP Help Portal.

261


1/14/26, 2:16 PM

Service Items

Freight Settlement

Waybill Stock Definition

## Use

You can define number stocks for business documents to uniquely identify and track transports. The system enables you to use

these stocks to allocate waybill numbers to business documents, such as forwarding orders, freight orders, freight bookings, and

freight units.

You can create, edit, and delete waybill stock number ranges for business documents of all modes of transport in using the Waybill

Number Stocks app, which you can open from the launchpad. Furthermore, you can create waybill stock number ranges without

assigning a mode of transport yet.

## Prerequisites

You have created number stock types in Customizing for Transportation Management under  Master Data

## Waybill Stock

 Define Waybill Number Stock Types .

If you want to define master air waybill stocks, you have defined airline codes for IATA carriers or non-IATA carriers in Customizing

for Transportation Management under  Master Data

## Business Partners

 Define IATA Airline Codes . You can also enter a

prefix for the carrier.

To specify a local carrier for a master waybill stock, you have performed the following steps:

1. Go to the Maintain Business Partner transaction (transaction BP).

2. Enter the business partner for the local carrier.

3. Enter Carrier in the Display in BP role field.

4. On the Vendor Data tab page, enter the airline code in the Airline Codes screen area.

5. Save your entries.

## Features

For business documents with a transportation mode of Parcel, you can specify tracking number stocks for multiple purchasing

organization and carrier combinations. You can draw a number from this stock if the combination of purchasing organization and

carrier in the business document matches a purchasing organization and carrier combination in the tracking number stocks.

For house waybills, you can specify a waybill number range stock for multiple sales organizations and ordering parties. You can

draw a number from this stock in a house waybill. When you draw a number in the waybill, the system matches the attributes in the

business document with the attributes of the waybill stock until it recognizes a matching attribute. The system checks the

attributes of the stock in the following order:

1. Sales organization and ordering party combination

2. Ordering party

3. Sales organization

This is custom documentation. For more information, please visit SAP Help Portal.

262


1/14/26, 2:16 PM

Note that a forwarding order with a transportation mode of air must contain an air waybill type before you can draw a waybill

number.

  Example
You have created a waybill stock for sales organization 245006 and another waybill stock for ordering party FL_1. When you

draw a waybill number in a business document with sales organization 235006 and ordering party FL_1, the system first

searches to see whether there is any existing stock that possesses both these attributes. As it does not find a match, it

searches for a stock with the ordering party and draws the number from the stock with ordering party FL_1.

For master waybills, you can specify a stock for multiple purchasing organizations, and for local carriers or global carriers. You can

draw a number from this stock in a master waybill if the combination of purchasing organization and carrier in the business

document matches the combination of purchasing organization and carrier of the waybill stock.

You must specify the airline code for a master air waybill (MAWB). For master bills of lading with transportation mode of ocean or

land, you have the option to specify a SCAC.

  Example

You have created a waybill stock for an airline code LUF, a purchasing organization 560011, and a carrier SD_01. When you

draw a waybill number in a MAWB, the system compares the airline code, purchasing organization, and ordering party of the

business document with the airline code, purchasing organization and ordering party of the stock. If the entities match, it draws

a number.

In master waybill stocks, you can delegate a waybill number to a purchasing organization. When you draw a waybill number in a

business document with this purchasing organization, the system makes the waybill number that you have delegated available in

the document.

  Example

A business unit in Frankfurt with purchasing organization FRA001 needs a MAWB number for a MAWB document. A business

unit in Berlin can delegate a number to the purchasing organization FRA001. When the Frankfurt business unit draws a waybill

number in the MAWB, the system makes the delegated waybill number available in the document.

  Note

If the system does not find a waybill stock or tracking number stock from which you can draw a waybill number or tracking

number in a business document, it performs the following steps:

1. Checks the transaction PPOME for parent organizations of the organization you have entered in the business document

2. Traverses through the parent organizations until it finds a parent organization that has a waybill stock.

3. Makes a waybill number from this parent stock available in the business document.

## More Information

Management of Air Freight Bookings for Airlines

Building and Printing of House Bills of Lading and House Air Way

This is custom documentation. For more information, please visit SAP Help Portal.

263


1/14/26, 2:16 PM

Create and Update Service Products for Independent Charge
## Types

You use this report to schedule a background processing function to replicate charge types as service products. You use this report

when you first set up your system, when you use the settlement of transportation cost features. You can also use this report to

schedule a background processing function when you extend the posting of transportation cost settlements to other company

codes and plants. You can also use this report when you choose to use a new charge type in your business for which you may not

have created a corresponding service product.

## Key Features

This report provides the following key features:

Scheduling settings to schedule the background processing function

Parameters that the system uses as a default when it creates service products

## Additional Details

This is a prerequisite step for the posting of transportation cost settlement features. You must replicate all the charge types you

use in your settlement process as service products. During the posting process, the system creates a purchase order and a service

entry sheet in the background. For each of the independent charges in the freight order, the system creates a purchase order item

with the service product that is linked to the charge type. The system then posts a service entry sheet for each purchase order

item that has a linked service product.

When you schedule the background processing function, you can specify an immediate start or a later start date and time.

You must specify the following parameters:

Material group

## Purchasing group

## Material type of Service Product

The system uses the parameters as the default when it creates service products. You must specify the plant that the system uses

when it posts transportation costs. You also specify the plant to which you extend a service product.

You can specify independent charge types. If you don't specify a charge type, by default the system creates the service product for

all the independent charge types in the system.

  Note

If new calculation bases are made available in Transportation Management, there can be new units of measure (UoMs)

used for charge calculation quantities in freight documents. To be able to use the new UoMs, you must use this function

before starting a settlement process involving the new calculation bases. This ensures the system updates existing

service products to include the new UoMs.

Alternately you can also run the program /SCMTMS/MANAGE_SERV_MAT from the background to perform the same

activities that you can do using this report from the frontend.

## Supported Device Types

This is custom documentation. For more information, please visit SAP Help Portal.

264


1/14/26, 2:16 PM

Desktop

## Tablet

This is custom documentation. For more information, please visit SAP Help Portal.

265
