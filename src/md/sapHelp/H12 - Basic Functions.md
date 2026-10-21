1/14/26, 2:46 PM

Transportation Management (TM)

Generated on: 2026-01-14 14:46:32 GMT+0000

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


1/14/26, 2:46 PM

## Basic Functions

This section provides information about basic functions in Transportation Management (TM).

Considering Dangerous Goods

## Use

The dangerous goods functions in Transportation Management (TM) enable you to transport dangerous goods (DG) in compliance

with international regulations.

## Features

In Transportation Management you can work with dangerous goods in the following ways:

Dangerous Goods Processing Based on PS&S

Dangerous Goods Processing Based on Product Compliance

Dangerous Goods Processing Based on PS&S

## Use

The dangerous goods functions in Transportation Management (TM) enable you to transport dangerous goods (DG) in compliance

with international regulations.

## Features

When you perform dangerous goods checks for your business documents, the system bases the checks on the relevant dangerous

goods data. This data is created as follows:

Dangerous goods master data (created by shippers)

When a shipper enters a product in the product master data in TM and the product is classified as dangerous goods, the

shipper also creates a dangerous goods master data for the product.

Document-based dangerous goods records (created by logistics service providers)

When a logistics service provider (LSP) receives dangerous goods data from a shipper, the LSP enters the dangerous goods

data in the relevant business document by creating a document-based dangerous goods record at item level.

You can perform dangerous goods checks for business documents created in TM. These checks are performed in TM. The system

bases the checks on the available dangerous goods data, that is, dangerous goods master data, or document-based dangerous

goods records created for forwarding orders, freight orders, or freight bookings. For more information, see Dangerous Goods

## Checks

Note that when you print your business documents, the system also prints the required dangerous goods information if you have

made the required settings.

This is custom documentation. For more information, please visit SAP Help Portal.

2


1/14/26, 2:46 PM

Configuration of Dangerous Goods Processing

## Use

The following settings enable you to use the dangerous goods functions for your business documents.

## Activities

## Dangerous Goods Records

For dangerous goods master data, you have made the following settings:

In master data, you have assigned an indicator profile to the material. You define indicator profiles in Customizing

for Transportation Management under  Basic Functions

## Dangerous Goods

 Dangerous Goods Processing

Based on PS&S

## PS&S Services

 Dangerous Goods Management

 Dangerous Goods Checks and Dangerous

Goods Documents

## Common Settings

 Specify Indicator Profiles for the Material Master

.

You have created a dangerous goods master data record for the product, using the Display Dangerous Goods Data

app on the launchpad.

For information about the required settings for document-based dangerous goods records, see Document-Based

Dangerous Goods Records.

Note that you can load SAP EHS Regulatory Content into TM and use the content as the basis for document-based

dangerous goods records. For more information, see Loading Dangerous Goods Content.

## General Settings

The following settings apply to dangerous goods master data and document-based dangerous goods records:

You have specified environment parameters that control the processes in PS&S Services. You do this in Customizing for

Transportation Management under  Basic Functions

## Dangerous Goods

 Dangerous Goods Processing Based on

## PS&S

 PS&S Services

## Basic Services

 Specify Environment Parameters .

TM uses the PS&S framework to extract DG information in the form of phrases for printing. To enable the PS&S framework,

you have set up phrase management in PS&S Services and assigned a text pattern in the DG master. You have also defined

phrases in phrase management.

You have created a DG profile to activate DG checks. The profile defines general conditions for processing DG, such as

conditions for displaying error messages. For more information, see Customizing for Transportation Management under

Basic Functions

## Dangerous Goods

 Dangerous Goods Processing Based on PS&S

 Define Dangerous Goods Profile

.

You have assigned the DG profile to the business document types that you use in your business processes.

You do this in Customizing for Transportation Management under the following:

Freight Order Management

## Freight Order

 Define Freight Order Types

Freight Order Management

## Freight Booking

 Define Freight Booking Types

Planning

## Freight Unit

 Define Freight Unit Types

Forwarding Order Management

## Forwarding Order

 Define Forwarding Order Types

Forwarding Order Management

## Forwarding Quotation

## Define Forwarding Quotation Types

This is custom documentation. For more information, please visit SAP Help Portal.

3


1/14/26, 2:46 PM

Note that if you want to enter dangerous goods data in your business documents without performing any DG checks, you

still have to assign a DG profile to the business document type.

You have activated general settings for DG processing in Customizing for Transportation Management under  Basic

## Functions

## Dangerous Goods

 Dangerous Goods Processing Based on PS&S

 Define Common Settings for

Dangerous Goods Processing .

Note that this includes the required settings for printing dangerous goods data.

You have defined the mode of transport in Customizing for Transportation Management under  Master Data

 Transportation Network

 Transportation Lane

 Define Transportation Mode .

To use the DG checks during freight unit (FU) building and vehicle scheduling and routing (VSR) optimization, you have

assigned the methods FUB_DG and VSR_DG to the relevant process controller strategy . For more information, see

Customizing for Transportation Management under  Basic Functions

 Process Controller

 Assign Methods to a

Strategy .

You have defined whether processes are blocked if errors occur during a dangerous goods check. You define which

processes are blocked for block reason Error During Dangerous Goods Check. For more information, see Customizing for

Transportation Management under  Basic Functions

## General Settings

 Define Block Reason Codes .

## Adapting DG Processing

You can adapt dangerous goods processing to your requirements as follows:

You can create a DG check according to your needs by creating a function module, assigning it, and specifying a dangerous

goods check method. For more information, see Customizing for Transportation Management under  Basic Functions

## Dangerous Goods

 Dangerous Goods Processing Based on PS&S

## PS&S Services

## Dangerous Goods Management

 Dangerous Goods Checks and Dangerous Goods Documents

 Dangerous Goods Checks

 Specify Dangerous Goods

Check Methods .

You then assign the DG check method to the check schema in Customizing for Transportation Management under  Basic

## Functions

## Dangerous Goods

 Dangerous Goods Processing Based on PS&S

 PS&S Services

 Dangerous Goods

## Management

 Dangerous Goods Checks and Dangerous Goods Documents

 Dangerous Goods Checks

## Specify

Dangerous Goods Check Schemas .

You can change, delete, or extend the input data for the dangerous goods check and for printing data. For more information,

see Customizing for Transportation Management under  Business Add-Ins (BAdIs) for Transportation Management

 Basic Functions

 Dangerous Goods

## Integration with PS&S

 BAdI: Definition of Data for Printing and Checking for

Dangerous Goods .

You can read template data from an external database instead of the PS&S Services database. For more information, see

Customizing for Transportation Management under  Business Add-Ins (BAdIs) for Transportation Management

## Basic

## Functions

 Dangerous Goods

## Template Data

 BAdI: Dangerous Goods Processing .

Dangerous Goods Checks

## Use

You use this process to perform dangerous goods (DG) checks for forwarding orders, forwarding quotations, freight orders, and

freight bookings. The system can perform checks automatically when you save your business documents, and you can trigger the

checks manually. Due to different risks involved in transporting DG, the system carries out checks in different ways and at different

process steps to ensure safety precautions are observed during transportation. For example, the system can perform checks

during freight unit (FU) building and vehicle scheduling and routing (VSR) optimization. This ensures the compliance of the

resulting successor documents such as FUs and freight orders (FOs).

This is custom documentation. For more information, please visit SAP Help Portal.

4


1/14/26, 2:46 PM
## Prerequisites

You have created dangerous goods master data for your products, or you have created document-based dangerous goods records.

In addition, you have made the required settings for dangerous goods processing.

For more information, see Configuration of Dangerous Goods Processing.

Note that during planning, document-based dangerous good records created at item level in forwarding orders are automatically

transferred to the relevant freight orders or freight bookings (that is, freight documents). The document-based dangerous goods

records derived from forwarding orders are read-only in the freight documents. You can also create document-based dangerous

goods records at item level in freight documents.

## Process

1. You execute the DG check for the forwarding order.

If the system identifies DG, it selects the Dangerous Goods checkbox. If there are DG errors, the system blocks the

forwarding order.

To perform the check manually, choose the Check pushbutton or select Check from the menu.

2. TM creates freight units.

The system can check DG during freight unit building, for example, by using the mixed loading check. The system analyzes

the items with respect to their possible combination during transportation. The system considers incompatibilities for the

affected items. If the DG check returns errors, the system prevents these items from being transported in the same freight

unit.

You can check the blocking status on the Statuses tab page in the Blocking Information group box. If errors occur during a

DG check, the system displays block reason Error During Dangerous Goods Check and blocks the relevant processes

according to the settings in Customizing for the block reason. In the details, you can find further information about all

performed checks, including the DG check.

3. The TM system checks the freight units after they are created.

This check is also carried out each time the FU is changed.

The system selects the Dangerous Goods checkbox when it identifies DG. The system blocks the FU if there are DG errors.

4. The TM system can perform checks during VSR planning and checks the resulting freight document.

## Checking the transportation proposal during VSR planning

During VSR optimization the system assigns FUs to vehicle resources and creates freight documents. When creating

the transportation proposals, the system carries out the DG check and offers an alternative transportation proposal.

In batch processing, the system selects the first solution that does not contain DG errors.

With the mixed-loading check, you can check incompatible FUs that should not be transported together. By setting

up a freight unit vehicle check, you avoid planned freight documents that contain freight units with DG that are

incompatible with certain resources. The system incorporates incompatibilities into the VSR optimization run. For

more information about planning, see Planning.

## Checking the freight document

The system checks the resulting freight documents after the VSR optimization run. The system also performs this

check each time the freight document is changed.

During manual planning, the system checks the freight document each time it is saved or if the check is triggered

manually.

This is custom documentation. For more information, please visit SAP Help Portal.

5


1/14/26, 2:46 PM

Note that at this point, you can create document-based dangerous goods records in the freight document, if

required. The system includes the document-based dangerous goods records in the DG checks.

## Result

You can display information about DG processing on the following user interfaces:

Forwarding Order

Forwarding Quotation

Freight Unit

Freight Order

## Freight Booking

## Transportation Proposal

The business document contains the DG check result. You find further DG information for the related product on item level on the

Dangerous Goods tab page. You can print forwarding orders, forwarding quotations, freight orders, and freight bookings with DG

information.

In the forwarding order overview, you can define a query that selects forwarding orders according to dangerous goods data. For

example, all forwarding orders with dangerous goods records that contain a specific dangerous goods number and regulation.

In the application log (object /SCMTMS/TMS and subobject DG), you can display messages that occur during DG checks that are

carried out during freight FU building and VSR optimization. You can open the Application Log app from the Launchpad.

More Information

## Phrase Management

Dangerous Goods Master Data

Error and Conflict Handler (CA-FS-ECH)

Forwarding Order Management

Creation and Editing of Freight Units

Incompatibilities

## Freight Order

ADR 1.1.3.6 Points Check Calculation

## Use

The European Agreement concerning the international carriage of Dangerous Goods by Road (ADR) is an international standard

governing the transport of dangerous goods by road. Section 1.1.3.6 of the agreement describes an exemption based on the

calculation of points for dangerous goods. If the points total calculated according to the method described does not exceed 1000

points, the exemption can be applied.

This is custom documentation. For more information, please visit SAP Help Portal.

6


1/14/26, 2:46 PM

A new check method has been created (/SCMTMS/DG_ADR_1000_POINTS). For more information on how to assign this check

method to the check schema and business context, see Configuration of Dangerous Goods Processing.

You enable the points check in Customizing for Transportation Management. For more information see Customizing under  Basic

## Functions

## Dangerous Goods

 Dangerous Goods Processing Based on PS&S

 PS&S Services

 Dangerous Goods

## Management

 Dangerous Goods Checks and Dangerous Goods Documents

 Dangerous Goods Checks

 Specify Dangerous

## Goods Check Methods

The following business documents are involved in the calculation of points:

Forwarding Order (FWO)

Points are the sum of the points of all assigned items.

Forwarding Quotation (FWQ)

Points are the sum of the points of all assigned items.

Order-Based Transportation Requirement (OTR)

Points are the sum of the points of all assigned items.

Freight Unit (FU)

Points are the sum of the points of each assigned item.

Road Freight Order (FO)

Points are the maximum of the points of each stage.

You activate the ADR points check in the freight unit building rule for the relevant document type. The system considers the ADR

points limit when building freight units. For example, if you have set a limit of 1000 points per freight unit and you want to transport

three items each with 500 points, the system generates two freight units. For more information, see Freight Unit Building Rule.

The formula for calculating points is:

Points = Relevant Quantity x Multiplication Factor

The application of the formula varies according to the following:

Dangerous Goods Master Data

## Created by Shippers

Document-based Dangerous Goods Records

Created by Logistics Service Providers

## Determination of Relevant Quantity

Points are calculated on the basis of the relevant quantity.  You can measure quantities according to one of the following:

Dangerous Goods Master Data

Uses quantity from item level:

Gross Weight

Net Weight

## Gross Volume

This is custom documentation. For more information, please visit SAP Help Portal.

7


1/14/26, 2:46 PM

Document-based Dangerous Goods Records

Uses quantity from DG record level:

Gross Weight

## Net Weight

Nominal Volume of Receptacle

## Quantity Measurement

The quantity measurement to be used is determined by the aggregate state specified for transport of the material or product:

## Dangerous Goods Master Data

For each aggregate state specified in the DG master, you must assign a relevant quantity for dangerous goods master data.

## Document-based Dangerous Goods Records

For each aggregate state specified in the DG record, you must assign a relevant quantity for document-based dangerous

goods records. For more information see Definition of UI Profiles for Document-Based DG Data.

For more information see Customizing for Transportation Management under  Basic Functions

## Dangerous Goods

## Dangerous Goods Processing Based on PS&S

 Define Points-Relevant Quantities for ADR 1.1.3.6 DG Exemption

## Multiplication Factor

For dangerous goods master data, you specify the multiplication factor in the DG Master.

For document-based dangerous goods records, you specify the multiplication factor in the DG Record. For more information, see

Definition of UI Profiles for Document-Based DG Data.

## Transport Restrictions

For dangerous goods you can specify that a product or material is:

## Prohibited

Not eligible for consideration under ADR 1.1.3.6.

## Unlimited

Not considered in points calculation under ADR 1.1.3.6

If either of these flags is set, no points for this product or material will be calculated.

For dangerous goods master data, you specify these flags in the DG Master.

For document-based dangerous goods records, you specify these flags in the DG record. For more information, see Definition of UI

Profiles for Document-Based DG Data.

## Calculating Total Points

The system calculates points on the following levels:

## Document Item

## The sum of points for an item in a document

This is custom documentation. For more information, please visit SAP Help Portal.

8


1/14/26, 2:46 PM

## Document Header

The sum of points for all items in a document

## Document Stage Detail

The sum of points for all items assigned to a stage

## VSR Optimization

To activate the ADR points check in the optimizer you should create vehicle resources, maintaining dimensions and indicating that

the resource is relevant for ADR points check.

You can deactivate the points check in the optimizer settings of the planning profile or during the manual planning in the

## Transportation Cockpit. For more information, see VSR Optimization

If these resources are maintained in the Capacity Selection Settings of the planning profile, the VSR optimizer takes the DG ADR

1.1.3.6 points limit into account as a planning-relevant capacity for this resource. For more information see Planning Profile.

## Prerequisites

You have assigned a check schema to the relevant business documents and assigned the new check method to the check schema.

For more on information on this see Customizing for Transportation Management under:

Basic Functions

## Dangerous Goods

 Dangerous Goods Processing Based on PS&S

 PS&S Services

## Dangerous

## Goods Management

 Dangerous Goods Checks and Dangerous Goods Management

 Common Settings

## Specify

Business Context

Basic Functions

## Dangerous Goods

 Dangerous Goods Processing Based on PS&S

 PS&S Services

## Dangerous

## Goods Management

 Dangerous Goods Checks and Dangerous Goods Management

## Dangerous Goods Checks

 Specify Dangerous Goods Check Schema

Document-Based Dangerous Goods Records

## Use

If you transport dangerous goods on behalf of customers, you may not always have the required dangerous goods master data in

your SAP TM system. Document-based dangerous goods records enable you to do the following:

Enter dangerous goods data manually in a forwarding order, freight order, or freight booking. You create a document-based

dangerous goods record at item level for the relevant items.

Enter dangerous goods data automatically when TM creates a forwarding order based on data received from a business

partner (for example, a shipper). The relevant enterprise service creates the required document-based dangerous goods

records.

## Prerequisites

You have made the required general settings for dangerous goods. For more information, see Configuration of Dangerous

Goods Processing.

You have defined a user interface (UI) profile for document-based dangerous goods records.

This is custom documentation. For more information, please visit SAP Help Portal.

9


1/14/26, 2:46 PM

The UI profile controls which fields and regulations are available for entering document-based dangerous goods data. For

example, logistics service providers can create UI profiles based on dangerous goods that they regularly transport for their

customers.

For more information, see Definition of UI Profiles for Document-Based DG Data.

To have the system check an individual field in a document-based dangerous goods record during a consistency check of

the entire business document, you have enhanced the check methods accordingly.

You enhance the check methods in Customizing for Transportation Management under  Basic Functions

 Dangerous

## Goods

 Dangerous Goods Processing Based on PS&S

## PS&S Services

 Dangerous Goods Management

## Dangerous

Goods Checks and Dangerous Goods Documents

 Dangerous Goods Checks

 Specify Dangerous Goods Check

Methods .

You must use existing function module /SCMTMS/DG_CHECK_WITH_CONTENT as the item check method.

  Note

The system checks the data in the document-based dangerous goods record against the available dangerous goods

records in TM. These records are created when you save a document-based dangerous goods record as a template. If

you have not saved any template data, the system cannot perform any checks.

To enable you to perform consistency checks on document-based dangerous goods data, you can load SAP EHS

Regulatory Content into TM. You can use the generated dangerous goods master data records as templates for

document-based dangerous goods records. For more information, see Loading Dangerous Goods Content.

## Activities

You create document-based dangerous goods records on the Dangerous Goods tab page at item level in the forwarding

order, freight order, or freight booking.

For more information, see Creation and Editing of Document-Based Dangerous Goods Records.

You can save a document-based dangerous goods record as a template and you can use a template to create a dangerous

goods record.

For more information, see Creation and Use of Dangerous Goods Templates.

Definition of UI Profiles for Document-Based DG Data

## Use

To enter dangerous goods data manually in a business document, you must define a dangerous goods UI profile. A UI profile

controls which fields and regulations are available on the Dangerous Good tab page at item level in the business document. A UI

profile also defines the layout of the information on the tab page.

A UI profile consists of a set of dangerous goods fields that are organized in UI groups and that are assigned to the relevant

regulations. You can create UI profiles that contain the fields and regulations that you need on a regular basis.

## Features

## Creating and editing UI profiles

When you create a UI profile or change an existing UI profile, you select the required fields from the PS&S Services master

data. You can also select fields that you have previously defined according to your requirements.

This is custom documentation. For more information, please visit SAP Help Portal.

10


1/14/26, 2:46 PM

  Note

You cannot change a UI profile if it is in use (for example, if it is assigned to a forwarding order (FWO) item type and an

FWO with this FWO item type has been created with dangerous goods data). However, you can create a new profile by

copying an existing UI profile.

## Defining UI groups

You can organize the fields in a UI profile by defining UI groups. Before you insert a UI group into a profile, you must define

the UI-group title (for example, “Substance Rating”). You define the position of the UI group on the user interface by

specifying a column number and row number.

In addition, you can specify that all fields in a UI group are displayed as a table on the UI. Note that if you assign a phrase set

to a field in the UI group, the system automatically provides a link in the table that allows you to create or change a phrase

in phrase management.

After you have inserted a UI group into a profile, you assign the required fields.

## Assigning regulations

Each field in a UI profile is assigned to at least one regulation. When a user calls the Dangerous Goods tab page in a

business document, each regulation has a separate tab page.

You assign regulations at profile level, UI-group level, or field level. For example, when you create a UI profile or UI group, you

can select the required regulations. All fields that are added to the UI profile or UI group are then automatically assigned to

the same regulations and are available on the relevant tab pages within the Dangerous Goods tab page. If required, you can

change the assigned regulations at field level. If you have not assigned regulations at profile or group level, you must assign

at least one regulation at field level.

## Defining field properties

You can specify the following for individual fields:

You can specify for each regulation whether you need to edit a field separately. If you do not specify that a field is

edited separately, the value entered on the first regulation tab page is automatically transferred to the other

regulation tab pages.

You can specify whether the value displayed on the user interface is an initial value.

You can specify whether a field is displayed as a checkbox.

You can specify whether a field appears in the table view in addition to the detail view.

You can enter a corresponding field for a specific field. For example, you create a field for gross weight with a

corresponding field for the unit of measure.

You can enter a custom field label that is displayed on the UI instead of the default field label from the data element.

You can specify whether a consistency check is to be performed on a specific field if the user triggers a consistency

check for the entire business document or an individual dangerous goods record. Note that if you do not specify

this, the system does not check the field.

Previewing the final user interface layout

You can check the user interface layout before saving it.

## Assigning a phrase set to a field

If PS&S master data is already assigned to a phrase set, the system displays and stores this phrase set automatically. You

cannot change this assignment. If there is no such assignment, you can manually select phrase sets for fields that have the

same data type as fields with assigned phrase sets.

This is custom documentation. For more information, please visit SAP Help Portal.

11


1/14/26, 2:46 PM

## Downloading and uploading UI profiles

This enables you to transfer UI profiles from one system client to another, for example.

## Activities

You define UI profiles for document-based dangerous goods data in the Edit UI-Profile for Dangerous Goods app.

Note that you can generate a UI profile automatically by choosing the Generate Inbound Profile pushbutton. This profile

can be used to create document-based dangerous goods records automatically when the system creates a forwarding

order based on data received from a business partner. For more information, see Creation and Editing of Document-Based

Dangerous Goods Records.

For forwarding orders, you must assign the UI profile to the relevant forwarding order item types in Customizing for

Transportation Management under  Forwarding Order Management

 Define Item Types for Forwarding Order

Management

.

For freight orders or freight bookings, you must assign the UI profile to the dangerous goods profile in Customizing for

Transportation Management under  Basic Functions

## Dangerous Goods

 Dangerous Goods Processing Based on

## PS&S

 Define Dangerous Goods Profile . You must then assign the DG profile to the relevant freight order types or

freight booking types in Customizing for Transportation Management under  Freight Order Management

## Freight Order

 Define Freight Order Types  or  Freight Order Management

## Freight Booking

 Define Freight Booking Types .

You access the phrase management functions by opening the Manage Phrases app from the launchpad.

Creation and Editing of Document-Based Dangerous Goods
Records

## Use

You can use this function to manually edit, create, or delete dangerous goods (DG) records at item level in forwarding orders,

freight orders, or freight bookings. The system uses the dangerous goods user interface (UI) profile that is assigned to the

forwarding order item types or the freight document types in Customizing for Transportation Management (see Definition of UI

Profiles for Document-Based DG Data).

## Prerequisites

You have made the required settings for document-based dangerous goods records. For more information, see Document-

Based Dangerous Goods Records and Definition of UI Profiles for Document-Based DG Data.

You use the authorization object EHS: Phrase Item (C_EHSP_TPP) to control the authorizations for the phrase items. You

can define whether users are permitted to carry out the following functions:

02 Change

03 Display

You use the authorization object EHS: Phrase Library and Phrase Group (C_SHEP_TPG) to control the authorizations for

the phrase library and the phrase group. You can define whether users are permitted to carry out the following functions:

01 Add or create

02 Change

03 Display

This is custom documentation. For more information, please visit SAP Help Portal.

12


1/14/26, 2:46 PM
## Features

## Creating a dangerous goods record

When you create a dangerous goods record manually, you can use a dangerous goods template. You can also create the

record without a template. The system displays the relevant UI profile at the top of the Dangerous Goods tab page.

## Checking a dangerous goods record

You can run a consistency check on an individual dangerous goods record. The system only checks fields that are relevant

for the dangerous goods check, as specified in the corresponding UI profile.

The system checks the data in the document-based dangerous goods record against the available dangerous goods

records in TM. These records are created when you save a document-based dangerous goods record as a template. If you

have not saved any template data, the system cannot perform any checks.

To enable you to perform consistency checks on document-based dangerous goods data, you can load SAP EHS Regulatory

Content into TM. You can use the generated dangerous goods master data records as templates for document-based

dangerous goods records. For more information, see Loading Dangerous Goods Content.

## Saving a dangerous goods record

You save a dangerous goods record when you save the business document. If you are authorized, you can also save the

dangerous goods record as a reusable dangerous goods template.

## Finding dangerous goods templates

You can search for a dangerous goods template and copy the data into a new record.

## Creating and changing phrases

You can create, change, or display a phrase text by choosing the link next to the corresponding phrase field. A dialog box

appears where you either create phrases or change existing phrases in several languages.

## Selecting phrases

You can search for existing phrases and select them.

## Activities

You access the dangerous goods activities in the business document at item level on the Dangerous Goods tab page.

Note that during planning, document-based dangerous good records created at item level in forwarding orders are automatically

transferred to the relevant freight orders or freight bookings (that is, freight documents). The document-based dangerous goods

records derived from forwarding orders are read-only in the freight documents. You can then create additional document-based

dangerous goods records at item level in the freight documents.

  Note

Document-based dangerous goods records can be created automatically when TM creates a forwarding order based on data

received from a business partner (for example, a shipper). To generate the records, the system uses the UI profile that is

assigned to the forwarding order item type.

You can use UI profile DG_INBOUND_PROFILE to create the dangerous goods records automatically. This profile contains the

full set of fields that can be received from the business partner in the inbound message and that can be added to a UI profile.

This is useful if you do not know which dangerous goods data will be sent, for example.

This is custom documentation. For more information, please visit SAP Help Portal.

13


1/14/26, 2:46 PM

Creation and Use of Dangerous Goods Templates

## Use

You can use dangerous goods templates to create document-based dangerous goods records.

## Prerequisites

You use the authorization object DG Material Master: Master Data (M_MATE_DGM) to control the authorizations for master data.

You can define whether users are permitted to carry out the following functions:

01 Add or create dangerous goods master data

02 Change dangerous goods master data

03 Display dangerous goods master data

## Activities

When you create a document-based dangerous goods record in a business document, you can save the record as a released or

unreleased template. You can use released templates to create new dangerous goods records.

When you search for a released template, you can use the following dangerous goods key fields as filter criteria:

DG Number Type

DG Number

Packing Group

## Variant ID

You can check the processing status of templates in the dangerous goods master data using the Dislay Dangerous Goods Data

app which you can launch from the launchpad.

## More Information

Creation and Editing of Document-Based Dangerous Goods Records

Loading Dangerous Goods Content

## Prerequisites

You have purchased the dangerous goods content from a content provider and downloaded the zip file. The zip file contains

the following files:

CSV (comma-separated values) file for each regulation

## CSV files for phrases

CSV file that maps the regulation prefix (3 characters) to the regulation name (12 characters)

You have specified the regulations that are to be loaded into TM. You do this in Customizing for Transportation

Management under  Basic Functions

## Dangerous Goods

 Dangerous Goods Processing Based on PS&S

## PS&S

This is custom documentation. For more information, please visit SAP Help Portal.

14


1/14/26, 2:46 PM

## Services

 Dangerous Goods Management

## Dangerous Goods Master

## Specify Dangerous Goods Regulations . You

have to enter the 12-character regulation name from the CSV file.

You have opened the Dangerous Goods Content Loader app.

## Context

You can use the dangerous goods content loader to load the dangerous goods content from a content provider into Transportation

Management (TM). You downloaded the content from your content provider and then load it intoTM using the content loader. The

content comprises dangerous goods (DG) regulations, regulation texts (for example, substance names), phrases, and the required

Customizing data. Based on the content, the content loader generates DG master data records in TM.

The content loader is particularly useful if you do not have the required master data for dangerous goods in your TM system. For

example, if you are a logistics service provider (LSP) who receives dangerous goods data from shippers. You can use the generated

DG master data records as templates for document-based dangerous goods records and as the basis for consistency checks (for

example, to check whether a shipper has provided the correct temperature data for the corresponding UN number).

## Procedure

1. Upload Zip File

The system uploads the file to a staging area and informs you when the upload has been completed.

2. Load Phrase Data

We recommend that you load the phrases before you load the regulations.

To check the status of the loading process, go to step 4 Monitor Import Processes. To check if any system messages have

been generated, go to step 5 Check Generated Messages.

3. Load Regulation Data

The system displays a list of regulations that are specified in the CSV files. You select the regulations that you want to load.

If you cannot select a regulation, make sure that the regulation has been specified in the Customizing activity Specify

Dangerous Goods Regulations. If errors occur during the loading process, you can repeat the process for the data with

errors by selecting the corresponding load mode.

To check the status of the import, go to step 4 Monitor Import Processes. To check if any system messages have been

generated, go to step 5 Check Generated Messages.

4. Monitor Import Processes

This contains an overview of the processes for loading phrases and regulations. You can use it to check the loading status.

5. Check Generated Messages

This contains an overview of system messages that have been generated while loading phrases or regulations (for example,

information, warning, or error messages). You can filter the overview, for example, according to the regulation type and the

required message type. You can also filter the overview according to the context in which the message was generated (for

example, PHRASES_LOAD or REGULATIONS_LOAD).

6. Summary

This contains an overview of the processes that have been performed during the current session.

## Results

For each content record, the system creates a corresponding record in the dangerous goods master data in TM. Each dangerous

goods master data record contains a product with a product number generated by the system. This number always contains the

This is custom documentation. For more information, please visit SAP Help Portal.

15


1/14/26, 2:46 PM

respective UN number (for example, UN-1993-III-0101). The UN number can therefore be used to search for the imported

content in the dangerous goods master data.

You display dangerous goods master data using the Display Dangerous Goods Master app, which you launch from the launchpad.

Shipper's Declaration

## Use

The system can create a shipper's declaration for dangerous goods in a freight booking. The International Air Transport

Association (IATA) requires that all shipments tendered to air carriers and air freight forwarders classified by regulation as

dangerous goods are accompanied by the IATA shipper's declaration for dangerous goods. The shipper is responsible for correctly

and accurately completing the form in accordance with current IATA requirements and for ensuring that all requirements have

been met including packaging, labelling, and product information.

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

This is custom documentation. For more information, please visit SAP Help Portal.

16


1/14/26, 2:46 PM

As a shipper, you create a forwarding order and assign freight units that contain dangerous goods items. You assign the forwarding

order to an air freight booking. The system assesses the contents of the freight units, determines that the freight booking contains

dangerous goods and generates a shipper's declaration document that includes information on the dangerous goods from the

dangerous goods master. The shipper's declaration is available to the shipper.

## Dangerous Goods Processing Based on Product Compliance

The dangerous goods functions in Transportation Management (TM) enable you to transport dangerous goods (DG) by road, rail,

air, and ocean freight in compliance with international regulations.

## Features

You can view dangerous goods statuses for freight orders, freight units, and freight bookings. For more information see Product
Compliance Data in Transportation Processes.

## Configuration of Dangerous Goods Processing

The following settings enable you to use the functions of dangerous goods (DG) based on Product Compliance for your business

documents for road, rail, air, and ocean freight.

## Activities

You have enabled the use of Product Compliance processes. For more information, see Customizing for Transportation

Management under  Basic Functions

## Dangerous Goods

 Dangerous Goods Processing Based on PC

## Activate

Product Compliance .

You have specified the business features from product compliance that you want to use to support your product

compliance business processes. For more information, see Customizing for Transportation Management under  Basic

## Functions

## Dangerous Goods

 Dangerous Goods Processing Based on PC

 Activate Business Features for Product

Compliance .

To use the DG checks during freight unit building (FUB) and vehicle scheduling and routing (VSR) optimization, you have

assigned the methods FUB_DG and VSR_DG to the relevant process controller strategy. For more information, see

Customizing for Transportation Management under  Basic Functions

 Process Controller

 Assign Methods to a

Strategy .

Optionally, you have used BAdI: Definition of Data for Product Compliance Integration to change the parameters of the

API calls for DG checks, document description, and EDI structure. For more information, see Customizing for

Transportation Management under  Business Add-Ins (BAdIs) for Transportation Management

 Basic Functions

## Dangerous Goods

## Integration with Product Compliance

 BAdI: Definition of Data for Product Compliance Integration

.

## Sustainability

## Transportation and Greenhouse Gas Emissions

Greenhouse gas (GHG) emissions in the transportation sector increased steadily from 1990 to 2021. Road, aviation, shipping, and

rail comprise an approximate 16% of world-wide greenhouse gas emissions. Road freight alone is responsible for 40% of vehicle

emissions.

This is custom documentation. For more information, please visit SAP Help Portal.

17


1/14/26, 2:46 PM

Policy efforts aim to set the transportation sector on course to net-zero by 2030. Given the figures, significant transformation

efforts will be needed to reduce emissions and achieve sustainability goals. The efforts strive to ensure a robust and resilient

supply chain that promises sustainable growth while also achieving carbon footprint reduction goals.

## SAP Global Environmental Policy

SAP is committed to enabling sustainable business processes and supporting carbon footprint reduction aims.

Transportation Management (TM) is engaged in creating more efficient business processes that reduce greenhouse gas emissions,

and increase both transparency and efficient use of resources.

Below, you will find a summary of TM functions that directly or indirectly contribute to achieving SAP's sustainability goals.

## Transportation Management and Carbon Dioxide Emissions

TM allows you to organize your transports in both a cost-efficient and a sustainable way. Freight unit building, unified package

building, and load planning are just a few examples. By building both freight units and packages and loading your trucks in the

most efficient way possible, you can avoid wasting loading space and reduce the number of trucks needed. Also, by combining the

provisioning and return of empty containers, you can reduce GHG emissions.

More specifically, TM allows you to specify carbon dioxide (CO ) emissions per weight and distance unit for your trucks. These CO

2

2

emissions are taken into account during manual and automatic planning and displayed in your road freight oders.

## Related Information

Customizing for CO2 Emissions Calculation

Greenhouse Gas Emissions

Empty Provisioning and Empty Return

Global Trade

## Definition

The global trade functions in Transportation Management (TM) help you to meet the requirements for transporting customs-

relevant goods. They enable you to trigger the creation of customs declarations and handle various customs procedures.

## Use

Using the global trade features in TM, you can perform the following tasks:

Create and track customs export declarations. For this process, you integrate TM with SAP Global Trade Services (GTS) or a

similar customs management application.

For more information, see Export Declarations.

Make the required entries and settings to open and close the transit procedure, if you need to transport bonded goods

within a customs union

For more information, see Transit Procedure.

Perform security filing.

For more information, see Security Filing.

This is custom documentation. For more information, please visit SAP Help Portal.

18


1/14/26, 2:46 PM

Create import declarations as a logistics service provider on behalf of shippers for customs-relevant items in forwarding

orders. You can enter the customs data and set the customs statuses manually in the forwarding order (FWO) or, to

communicate with the customs authorities, you can use an integrated customs management application. With the

integrated solution, the customs management application automatically creates the import declaration and handles the

customs processes.

For more information, see Import Declarations by LSPs.

Perform a trade compliance check for new or changed business documents.

For more information, see Trade Compliance Check.

Secure approval from GTS to unload a freight order.

For more information, see Customs Transit Discharge.

## More Information

In some cases, separate organizational units are responsible for the export and import processes. For information about creating

export business documents and the corresponding import business documents, for example, export freight bookings and import

freight bookings, see Export/Import Processing.

Configuration of Customs Processing

## Use

You configure customs processing in Transportation Management (TM) in the Customizing. You define when and how customs

activities are triggered and tracked. The configuration controls how the system determines customs relevance, assigns processing

steps, and manages customs statuses based on business document types. Relationships between configuration elements

determine the overall customs processing behavior.

Customs processing is driven by the assignment of customs activities to business documents through customs profiles. These

activities define how customs processes, such as export or transit, are executed in the system. The configuration also includes

customs relevance checks, grouping logic, and the use of customs statuses.

## Features

A customs activity includes the following features:

Customs relevance check: Defines how the system determines whether a business document is subject to customs

processing.

Customs statuses for relevance: Specifies which customs status is shown when a document is either customs-relevant or

not.

Grouping strategy: Controls how the system creates customs groups from document items.

Trigger status for customs declaration: Sets the execution status a document must reach to trigger a customs

declaration.

  Note

The trigger status does not apply to customs processing based on freight units, such as export declarations by LSPs or

transit procedures for freight units.

This is custom documentation. For more information, please visit SAP Help Portal.

19


1/14/26, 2:46 PM

Customs statuses for declarations: Defines statuses used during the declaration process, such as Customs Declaration

Requested or Customs Declaration Approved.

## Output Management Adapter Settings

For exporting goods, two different sets of SOA interfaces are available to communicate with external systems:

Export declaration-based SOA services

ExportDeclarationSUITERequest_Out

ExportDeclarationSUITEConfirmation_In

ExportDeclarationSUITECancellationRequest_Out

Transportation customs declaration-based SOA services

TransportationCustomsDeclarationRequest_Out

TransportationCustomsDeclarationCancellationRequest_Out

TransportationCustomsDeclarationConfirmation_In

## Transportation Customs Declaration-Based Service Configuration

In addition to providing export services, transportation customs declaration-based SOA services support the following processes:

## Import

Transit Open

Transit Close

## Security Filing

To activate export declaration-based SOA services, enable action profile /SCMTMS/TOR_GTS.

To activate transportation customs declaration-based SOA services, enable action profile /SCMTMS/TOR_CST.

You make the required settings in Customizing for Cross-Application Components under  Processes and Tools for Enterprise

## Applications

 Reusable Objects and Functions for BOPF Environment

 PPF Adapter for Output Management

## Maintain

Output Management Adapter Settings .

In this Customizing activity, make the following settings:

Business Object: /SCMTMS/TOR

Node: CUSTOMS_GROUP

Customs Relevance Check

## Use

To determine whether a business document is relevant for a customs process (for example, export or transit), the system runs the

customs relevance check that is assigned to the customs activity. The customs relevance check determines, for example, whether

This is custom documentation. For more information, please visit SAP Help Portal.

20


1/14/26, 2:46 PM

goods are to be transported into a country or region that is in a different customs union and an export declaration is therefore

required.

## Features

The following are examples of the available standard customs relevance checks:

## EXP_EU

This check is used for export processes in freight documents (see Export Declarations by Shippers).

It checks whether the source and destination countries or regions belong to the European Union. The goods are customs-

relevant if the destination country or region is different from the source country or region, that is, one of the countries or

regions is not in the European Union. The relevance check identifies whether a country or region belongs to the European

Union by checking the relevant setting in Customizing for SAP NetWeaver under  General Settings

## Set Countries

 Specify Countries in mySAP Systems (CRM, SRM, SCM,…)

.

Note that if you are transporting goods between two countries or regions outside the European Union, the EXP_EU check

cannot identify whether the countries or regions belong to different customs unions. If you want to check customs

relevance in this case, you can implement the Business Add-In (BAdI) BAdI: Change Result of Customs Relevance Check.

For more information, see Customizing for Transportation Management under  Business Add-Ins (BAdIs) for

Transportation Management

 Basic Functions

 Global Trade

## Customs Activities

 BAdI: Change Result of Customs

Relevance Check .

TRA_T1

This check is used for opening the transit procedure in a freight document (see Transit Procedure for Freight Documents).

It checks the following:

Automatic customs handling has been specified for the corresponding forwarding order in Customizing for the

forwarding order type.

The transit procedure has been selected as the inbound customs activity for at least one of the items.

The transit procedure has been specified for at least one stage in the actual route.

There is at least one item without a movement reference number.

If these requirements are met, the freight document is relevant for the transit procedure.

Security Filing Relevance Checks

There are special checks for security filing:

SFE-US-CAR - Relevance Check Security Filing Export US Carrier

SFI-CA-CAR - Relevance Check Security Filing Import Canada Carrier

SFI-EU-CAR - Relevance Check Security Filing Import Europe Carrier

SFI-US-CAR - Relevance Check Security Filing Import US Carrier

SFI-US-IMP - Relevance Check Security Filing Import US Importer

The system checks one or more of the following:

does the route contain a security filing-relevant country or region?

what is the mode of transport?

if there is security filing-relevant country or region, is it an intermediate stop?

This is custom documentation. For more information, please visit SAP Help Portal.

21


1/14/26, 2:46 PM

For information about all standard customs relevance checks, see the documentation of the Customizing activity Define Customs

Relevance Check.

## Activities

You make the following settings in Customizing for Transportation Management under  Basic Functions

 Global Trade :

You define customs relevance checks in the Customizing activity Define Customs Relevance Check.

You assign customs relevance checks to customs activities in the Customizing activity Define Customs Activities and

Profiles.

Customs Groups

## Use

A customs group is a group of freight unit (FU) items for which a customs declaration is required. At least one customs group must

be created in order to perform a customs process.

The system creates customs groups according to the grouping strategy that is assigned to the customs activity. The strategy

groups the items according to specific criteria, such as the ship-to party or the goods seller. Depending on the criteria, more than

one customs group (and therefore more than one customs declaration) may be created for a load that is to be transported

together.

## Features

You can use the following standard grouping strategies:

## EXP_CONS

Groups FU items according to the ship-to party, goods buyer, goods seller, Incoterm, and Incoterm location

It is used for export processes in freight documents (for example, export declarations by shippers). It is assigned to

standard customs activity EXP_EU.

## EXP_LSP

## Groups FU items according to the movement reference number

It is used for export processes in freight units (for example, export declarations by logistics service providers). It is assigned

to standard customs activity EXP_EU_FU.

## TRA_OPEN

Groups FU items according to the transit end location, previous document, and previous document type

It is used for opening the transit procedure in freight documents. It is assigned to standard customs activity TRA_T1.

## TRA_CLOSE

Groups FU items according to the ship-to party, goods buyer, goods seller, Incoterm, Incoterm location, previous document,

and previous document type

It is used for closing the transit procedure in freight documents. It is assigned to standard customs activity TRA_T1_CL.

## TRA_OPENFU

This is custom documentation. For more information, please visit SAP Help Portal.

22


1/14/26, 2:46 PM

Groups FU items according to the transit end location and movement reference number

It is used for opening the transit procedure in freight units. It is assigned to standard customs activity TRA_T1_FU.

## SEC_FIL_FU

Groups all FU items of a FU in one group. For integration with a customs management system, security filing needs to be

triggered only once per HAWB/HBL. As several FUs can have the same HAWB/HBL, the systems aggregates several groups

into one SOA message.

## Activities

You can define your own grouping strategy by making the required settings in Customizing for Transportation Management under

Basic Functions

## Process Controller

 in the following Customizing activities:

Define Service

Define Strategy

## Define Methods

## Assign Methods to Strategy

You assign the grouping strategy to the customs activity in Customizing for Transportation Management under  Basic Functions

## Global Trade

 Define Customs Activities and Profiles .

Note that you can define and change grouping criteria. For more information, see Customizing for Transportation Management

under  Business Add-Ins (BAdIs) for Transportation Management

 Basic Functions

 Global Trade

 Grouping

 BAdI:

Grouping of Freight Unit Items .

Customs Statuses and Cumulated Customs Statuses

## Use

The system sets a customs status at different steps of customs processing. In Customizing for Transportation Management, you

define which customs status the system displays for each predefined step. You also define cumulated customs statuses that are

displayed at header and item level in a business document.

## Features

## Customs Statuses

If a customs relevance check is performed for a business document, the system displays a customs status that reflects the result

of the check (that is, relevant or not relevant). If a customs activity is relevant for a business document and you perform the

required customs process (for example, export or transit), the system displays a customs status that reflects the current status of

the customs process (for example, “Export Declaration Requested” or “Export Declaration Approved”).

## Cumulated Customs Statuses

As soon as customs groups have been created in a business document, the system displays a cumulated customs status at header

and item level. This is because a business document can contain more than one customs group, each with a different customs

status; and each item in a business document can belong to more than one customs group.

This is custom documentation. For more information, please visit SAP Help Portal.

23


1/14/26, 2:46 PM

You can assign a block reason to a cumulated customs status. As soon as the cumulated customs status is set, the system sets an

execution block in the business document and displays the corresponding block reason on the Statuses tab page. You can use

standard block reason 04 (Cust. Decl. Check Required) or you can define your own block reason.

## Activities

You make the following settings in Customizing for Transportation Management under  Basic Functions

 Global Trade :

You define customs statuses and cumulated customs statuses in the Customizing activity Define Cumulation of Customs

Statuses. You also assign a customs status to each cumulated customs status, and you assign a level to each cumulated

status. The level allows the system to determine which cumulated status is to be displayed if more than one cumulated

status is relevant.

Note that you can check if the customs statuses have been configured correctly by using the report provided in the

Customizing activity Check Customs Statuses. The report checks if each customs status has a unique description and

each customs status is assigned to a cumulated customs status.

You assign customs statuses to the customs activity in the Customizing activity Define Customs Activities and Profiles.

You define block reasons in Customizing for Transportation Management under  Basic Functions

 General Settings

## Define

Block Reason Codes .

For more information, see the documentation of the Customizing activities.

Customs Activities and Profiles

## Prerequisites

You have configured customs groups. For more information, see Customs Groups.

You have configured customs statuses and cumulated statuses. For more information, see Customs Statuses and Cumulated

Customs Statuses.

You have configured customs relevance checks. For more information, see Customs Relevance Check.

## Context

You define customs activities and profiles in the Customizing.

## Procedure

Go to  Basic Functions

 Global Trade  and perform activity Define Customs Activities and Profiles.

## Next Steps

Assign your profiles to document types in the Customizing.

Customizing for Document Types

Customizing Path

Freight Order Types

Freight Order Management

 Freight Order

 Define Freight

## Order Types

This is custom documentation. For more information, please visit SAP Help Portal.

24


1/14/26, 2:46 PM

Customizing Path

Freight Booking Types

Freight Order Management

 Freight Booking

 Define Freight

## Booking Types

## Customs Update for Export Declarations

Configure customs profiles to allow users to edit an existing export declaration instead of canceling and creating a new one.

## Context

You enable the update mode for a specific customs profile in the Customizing. Users can enter update mode in any export

declarations that are relevant to that profile.

  Note

You cannot add additional freight units to an existing export declaration in update mode.

Update mode is not available in all jurisdictions. For example, in Germany, it is not possible to update an export declaration, and

you must replace an erroneous one with a corrected one. However, in regions where it is allowed it reduces the effort required to

make small changes to an export declaration.

  Caution

SAP does not provide any guidance on which regions update mode is allowed in and it does not provide any configuration for

customs update.

## Procedure

1. Go to  Basic Functions

 Global Trade  and perform activity Define Customs Activities and Profiles.

2. Find the customs profiles for which you want to activate customs update or create new ones.

3. Select the Export Declaration Update Allowed option.

## Results

Customs update is now active for that customs profile and you can update any export declarations that you create, which are

relevant to the custom profile. For more information see Change Using Customs Update.

Security Filing

## Use

In response to security concerns, security authorities in several countries or regions have implemented a series of rules for

monitoring import cargos from all areas in the world. Organizations doing import/export business with companies of any of these

countries or regions, must comply with security authority regulations. For example, ocean freight destined for import to the United

States, needs to be approved by USCBP (US Customs and Border Protection), before loading can begin at the origin port. The

requirements vary according to country or region and mode of transport. Currently the following types of filing are supported:

This is custom documentation. For more information, please visit SAP Help Portal.

25


1/14/26, 2:46 PM

## Filing

## Country or Region

Import Control System (ICS)

## Europe

Automated Manifest System (AMS) / Automated Commercial

USA

Environment (ACE)

Importer Security Filing (ISF)

USA

Advance Commercial Information (ACI)

Since 2008 USCBP has required importers and carriers of record to make an ISF submission in addition to completing an AMS.

The ISF comprises additional information relating to any cargo to be brought into the United States by vessel. Normally the Ocean

AMS is triggered after the confirmation of the ISF is received.

## Europe, Canada, and USA

It is mandatory to submit all cargo-related data. Examples of this include

real exporter

real importer

number and type of packages (broken down to the smallest measurable item or unit)

cargo weight

hazmat information (if applicable)

container number/seal number (on containerized shipments)

Authorities must receive the submission no later than Authorities must receive the submission for ocean no later than 24

hours prior to the cargo being loaded on the vessel destined to the United States, and for aircraft, normally no later than the

time of the departure for the United States. Submissions must also include all freight remaining on board (FROB).

Exceptions are not permitted and omissions or late filings can result in a financial penalty, or off-loading from the vessel.

Importer Security Filing (ISF)

ISF comprises 10 data elements which are required to be sent to US Customs on all import shipments and FROB arriving

via sea-freight into the United States.

Manufacturer (or supplier) name and address

Seller (or owner) name and address

Buyer (or owner) name and address

Ship-to name and address

## Container stuffing location

## Consolidator (stuffer) name and address

Importer of record number/foreign trade zone applicant identification number

Ship-to Party number(s)

## Country or region of origin

Commodity Harmonized Tariff Schedule number to six (6) digits

Two additional elements are required from the carrier,:

This is custom documentation. For more information, please visit SAP Help Portal.

26


1/14/26, 2:46 PM

## Vessel stow plan

## Container status messages

Failure to provide the required information may result in monetary penalties, increased inspections and delay of cargo.

## Process

You can trigger the security filing process from either of the following documents:

Forwarding order

## Freight booking

Security filing is implemented on freight unit level. However a security filing is required if the freight unit or the corresponding

freight bookings include a target stop in any country or region requiring the additional security filings. For example, if a freight unit

is shipping from Germany to Canada with a stop in the US, it is necessary to complete a US filing for this freight unit also. The

system runs a relevance check to ensure compliance with such conditions.

Export Declarations

## Use

Transportation Management (TM) allows you to track the customs status of your exports. You can integrate TM with SAP Global

Trade Services (GTS) or a similar customs management application to have SAP S/4HANA create and issue the documents.

## Features

TM allows you to do the following:

Shippers can create export declarations from freight documents that are based on deliveries received from SAP S/4HANA.

For this process, you integrate SAP TM with SAP GTS or a similar customs management application.

Logistics service providers you can create export declarations from forwarding orders on behalf of a shipper. For this

process, you integrate SAP TM with SAP GTS or a similar customs management application.

Logistics service providers can enter export declaration statuses manually, for example, if the shipper has provided the

data.

Both can change and cancel issued export declarations.

Export Declarations by Shippers

## Prerequisites

You've integrated TM with SAP Global Trade Services (GTS) or a similar customs management application.

  Note

The following process describes the integration of TM with SAP GTS.

For more information, see Integration with SAP GTS.

This is custom documentation. For more information, please visit SAP Help Portal.

27


1/14/26, 2:46 PM

You've configured customs processing. For more information, see Configuration of Customs Processing.

TM has created freight units based on a delivery received from Delivery Management (LE-SHP).

For more information about delivery integration, see Integration of Orders and Deliveries in Transportation Planning.

## Context

In this process, you create export declarations for customs-relevant freight documents that contain freight units. You then submit
them to customs authorities automatically using SAP GTS or a similar customs management application.

  Note

Export declarations are created at the pre-carriage stage of a freight document.

## Procedure

1. Do transportation planning for freight units.

When you save the resulting freight document, the system does the following:

a. Checks whether a customs profile is assigned to the freight document type, for example, standard customs profile

for export GT_OUTBOUND

b. Determines which customs activities are assigned to the customs profile, for example, standard customs activity for

export EXP_EU)

c. Runs the customs relevance check that is assigned to the customs activity, for example, standard customs

relevance check EXP_EU

In the freight document, the system displays the customs activity in the Customs Activity group box on the Customs tab

page. If the freight document is customs-relevant, the system selects the Customs Relevance checkbox for the customs

activity. The system displays the corresponding customs status for the check result at header level (that is, on the Customs

tab page and Statuses tab page) and at item level (on the Customs tab page in the item details).

  Note

Note the following:

If you've assigned a block reason to the relevant cumulated customs status, the system sets an execution block

in the freight document.

If the freight document isn't customs-relevant, you can select the Customs Relevance checkbox manually and

then proceed with the next steps.

For more information about the standard customs relevance checks, see Customs Relevance Check.

2. Create an export declaration.

For more information, see Creating Export Declarations.

3. Wait for SAP GTS to create the export declarations and submit them to the customs authorities.

When SAP GTS receives an export confirmation from the customs authorities, it sends a confirmation to TM that contains

the following information:

## Customs management document number

This is the document ID provided by the customs management application that you use to communicate with the

customs authorities.

This is custom documentation. For more information, please visit SAP Help Portal.

28


1/14/26, 2:46 PM

## Customs reference number

In the European Union, for example, this is the movement reference number (MRN).

Indicator that shows the status of customs processing

The following values are possible:

Released: Customs clearance has been obtained for a customs group.

Canceled: An export declaration has been successfully canceled.

Fallback: A fallback procedure is in use (for example, if the customs authorities' IT systems or processes have

failed and communication has to be carried out using printouts instead of electronic messages). The status

of the customs groups and freight document doesn't change.

4. Wait for TM to receive confirmation from SAP GTS.

If customs have approved an export declaration for a particular customs group, the system sets the corresponding

customs status, for example, Customs Clearance Approved. The system displays the relevant cumulated customs status

at header and item level. If you haven't assigned a block reason to the new cumulated customs status, the system resets

any existing blocks.

## Results

When you request an export declaration for a freight document, the customs management application automatically creates the

export declaration and handles the customs processes.

As soon as customs clearance has been obtained for all customs groups and all execution blocks have been reset, the system

unfixes the freight document and the goods can be transported. The cumulated customs status, customs management document

number (that is, export declaration ID), and the customs reference number are displayed on the Customs tab page in the freight

document.

Export declaration documents are stored in the SAP GTS system. SAP GTS can send an export declaration document by e-mail to

an TM user.

Export Declarations by Logistics Services Providers

## Use

Transportation Management (TM) allows logistics services providers (LSPs) to manage export declarations on behalf of their

customers.

## Features

As an LSP, you can automate the export declarations submission and updates by integrating with SAP Global trade Management

(GTS) or a similar customs management application.

If you don't have an SAP GTS integration or if your customers want to track the status of their own export declarations to report

them to you, you can also update the status of the documents manually.

Manual Customs Handling for Logistics Services Providers
(LSPs)

This is custom documentation. For more information, please visit SAP Help Portal.

29


1/14/26, 2:46 PM
## Context

You use this process to enter customs data for customs-relevant items in forwarding orders. You enter the customs data and set

the customs statuses manually in the forwarding order (FWO).

## Procedure

1. Create an FWO with the required items.

You specify that the LSP is responsible for the export declaration by selecting the Export Declaration by LSP checkbox on

the General Data tab page in the FWO. Note that the system selects this checkbox automatically if you've selected the LSP

Export Declaration checkbox in the master data of the shipper.

2. Set the customs status of the items in the forwarding order to indicate that they're relevant for customs processes, for

example, Customs-Relevant.

You set the customs status on the Customs tab page in the item details. The system displays the relevant cumulated

customs status at header level on the Statuses tab page.

3. Save the FWO.

The system automatically creates freight units.

If you've assigned a block reason to the cumulated customs status, the system sets an execution block in the forwarding

order.

4. Enter the following data on the Customs tab page at item level in the forwarding order:

## Customs management document number

The export declaration ID provided by the shipper or obtained using a non-integrated customs management

application.

## Customs reference number and expiration date

In the European Union, for example, this is the movement reference number (MRN). The goods export has to take

place by the expiration date.

## Customs commodity code

Classifies the goods to be transported according to a customs tariff number. The system verifies the value that you

enter against the commodity codes you've defined. You can define commodity codes by opening the Manage

Commodity Codes app from the launchpad or using transaction /SAPSLL/CLSNR_01 Manage Commodity Codes.

For more information, see Classification of Goods.

5. Set the customs status of the items in the forwarding order, for example, “Export Declaration Approved” and save the

forwarding order.

The system displays the relevant cumulated status at header level. If you haven't assigned a block reason to the cumulated

customs status, the system resets any existing blocks.

## Results

When you create a freight document for the forwarding order, the freight document inherits the customs status from the

forwarding order. You can view the customs status on the Customs tab page in the freight document. It also inherits the customs

information at item level.

To cancel customs declarations manually in a forwarding order, choose the respective customs status at item level on the Customs

tab page. If you've assigned a block to the relevant cumulated customs status, the system sets an execution block in the

forwarding order.

This is custom documentation. For more information, please visit SAP Help Portal.

30


1/14/26, 2:46 PM

Configuring Manual Customs Handling for LSPs

## Procedure

Specify that customs handling is manual for the relevant FWO types. You define FWO types in Customizing for
Transportation Management under  Forwarding Order Management
Types .

 Forwarding Order

## Define Forwarding Order

Define a customs activity that controls customs handling for export declarations and assign the customs activity to a
customs profile. You've assigned the customs profile to the relevant freight unit types.

You make these settings in Customizing for Transportation Management as follows:

1. You define activities and profiles under  Basic Functions

## Global Trade

 Define Customs Activities and Profiles

.

For this process, you can use standard customs activity EXP_EU_FU, which is assigned to standard customs profile

GT_OUTBOUND_FU.

  Remember

You also have to define customs statuses and cumulated customs statuses. You assign the customs statuses to

the customs activity. You can also assign block reasons to cumulated customs statuses.

For more information, see Configuration of Customs Processing.

2. You define freight unit types under  Planning

## Freight Unit

 Define Freight Unit Types .

  Note

Some of the settings in the custom activity do not apply to manual customs handling (for example, customs

relevance check and grouping strategy). The most important settings are the trigger status and the assignment

of the customs statuses to the customs process.

Obtain the required customs data, for example, from the shipper or by using a non-integrated customs management
application.

  Tip

To create an export declaration, the forwarding order must contain one or more freight units (FUs). In the following

process, it is assumed that automatic FU creation has been set up in Customizing for Transportation Management.

Automatic Customs Handling an Export Declaration for Logistics
Services Providers (LSPs)

## Context

Use this procedure to create export declarations on behalf of shippers for customs-relevant items in forwarding orders.

To communicate with the customs authorities, you can use an integrated customs management application, such as SAP Global

Trade Services. When you request an export declaration from the forwarding order, the customs management application

automatically creates the export declaration and handles the customs processes.

## Procedure

1. Create a forwarding order (FWO) with the required items.

This is custom documentation. For more information, please visit SAP Help Portal.

31


1/14/26, 2:46 PM

Select the Export Declaration by LSP checkbox on the General Data tab page in the FWO. This checkbox is selected
automatically if the LSP Export Declaration checkbox is selected in the shipper's master data.

2. Save the FWO.

The system automatically creates freight units.

3. Trigger the creation of an export declaration from the forwarding order.

a. Choose  Customs

 Create Export Declaration .

b. Save the FWO.

The system performs the following actions:

Checks whether a customs profile is assigned to the freight unit type, for example, standard customs profile

GT_OUTBOUND_FU.

Determines assigned customs activities, for example, standard customs activity EXP_EU_FU.

Runs the customs relevance check, for example, standard customs relevance check EXP_EU_FU.

Creates customs groups based on the grouping strategy, for example, standard grouping strategy EXP_LS.

Requests an export declaration for each customs group.

4. Wait for SAP Global Trade Services to process the export declaration.

The system updates the customs status accordingly.

5. Monitor export declaration confirmations.

When SAP Global Trade Services receives confirmation from customs authorities, it sends a confirmation containing:

## Customs management document number

This is the document ID provided by the customs management application that you use to communicate with the

customs authorities.

## Customs reference number

In the European Union, for example, this is the movement reference number (MRN).

Indicator that shows the status of customs processing:

Released: Customs clearance has been obtained.

Canceled: An export declaration has been successfully canceled.

Fallback: A fallback procedure is in use.

6. Check the updated customs status in the system.

The system updates the customs status at header and item levels based on the confirmation.

## Results

When you create a freight document for the forwarding order, the freight document inherits the customs status from the

forwarding order. You can view the customs status on the Customs tab page in the freight document. The freight document also

inherits the customs information at item level. You can display this information on the Customs tab page in the item details.

To cancel an export declaration in the forwarding order, choose  Customs

 Cancel Customs Declaration . TM sends a

cancellation request to SAP Global Trade Services using the Request Export Declaration Cancellation

(ExportDeclarationSUITECancellationRequest_Out) enterprise service. Alternatively, the system can trigger the

## Request Transportation Customs Declaration Cancellation

(TransportationCustomsDeclarationCancellationRequest_Out) enterprise service. TM sets the corresponding

customs status (for example, “Export Declaration Cancellation Requested”). If you've assigned a block reason to the relevant

This is custom documentation. For more information, please visit SAP Help Portal.

32


1/14/26, 2:46 PM

cumulated customs status, the system sets an execution block in the forwarding order and the freight units. As soon as SAP Global

Trade Services, or a similar customs management application, has confirmed the cancellation, TM updates the customs statuses

accordingly.

Note that export declaration documents are stored in the external system (SAP Global Trade Services system or similar customs

management application), not in the TM system. The customs management application may make the export declaration available

to the TM system through, for example, a portal or cloud solution or by sending an export declaration document to the e-mail

address of the TM user.

Configuring Automatic Customs Handling for Logistics Services
providers (LSPs)

## Procedure

You've integrated TM with SAP Global Trade Services or a similar customs management application. For more information,
see Integration Scenarios for SAP Global Trade Services.

  Note

To use your own enterprise service to request an export declaration, you must implement the Business Add-In

(BAdI)BAdI: Creation of Export Declarations on Freight Unit. For more information, see Customizing for

Transportation Management under  Business Add-Ins (BAdIs) for Transportation Management

 Basic Functions

 Global Trade

## Declarations

 BAdI: Creation of Export Declarations on Freight Unit

.

You've defined a customs activity that controls customs handling for export declarations and assigned the customs activity
to a customs profile. You've assigned the customs profile to the relevant freight unit types.

You make these settings in Customizing for Transportation Management as follows:

1. You define activities and profiles under  Basic Functions

## Global Trade

 Define Customs Activities and Profiles

.

For this process, you can use standard customs activity EXP_EU_FU, which is assigned to a standard customs

profile GT_OUTBOUND_FU.

  Note

You also have to define customs statuses and cumulated customs statuses. You assign the customs statuses to

the customs activity. You can also assign block reasons to cumulated customs statuses.

For more information, see Configuration of Customs Processing.

2. You define freight unit types under  Planning

## Freight Unit

 Define Freight Unit Types .

You've specified that customs handling is automatic for the relevant FWO types. For more information, see Customizing
forTransportation Management under  Forwarding Order Management
Types .

 Define Forwarding Order

 Forwarding Order

  Note

To create an export declaration, the FWO must contain one or more freight units (FUs). In the following process, it's

assumed that automatic FU creation has been set up in Customizing for TM.

Creating Export Declarations

## Prerequisites

This is custom documentation. For more information, please visit SAP Help Portal.

33


1/14/26, 2:46 PM

SAP Transportation Management (TM) is integrated with SAP Global Trade Services (GTS) or a similar customs management

application.

  Note

The following description assumes you're using SAP Global Trade Services.

## Context

You create export declarations in a freight document based on customs groups, which are built according to your organization’s
settings. TM asks SAP Global Trade Services to create the export declaration and submit it to the relevant authorities.

## Procedure

1. Open the freight document that you want to create an export declaration for.

2. On the Customs tab, in the Customs Activity group, select the customs activity and choose Build Customs Groups.

The system groups the items in the freight document according to the grouping strategy assigned to the customs activity,
for example, the standard grouping strategy that is assigned to customs activity.

For more information about the standard grouping strategies, see Customs Groups.

3. Display the customs groups by selecting the customs activity in the Customs Activity group box.

The system displays the customs groups in the Item Groups table.

a. Optional: Check the item groups.

To display the items assigned to each customs group, select the customs group and choose Show Assigned Items.

The customs status of each customs group is displayed in the Item Groups table, in the Status field. The system
displays the relevant cumulated customs status at header and item level in the freight document. If you've assigned
a block reason to the cumulated customs status, the system sets an execution block in the freight document.

4. In the Item Groups table, select the customs groups.

5. Choose Request Customs.

6. Save the document.

## Results

Before the system sends the request, it checks if the freight document has the required trigger status, that is, the execution status

specified in the customs activity. If necessary, you must set the corresponding execution status and save the freight document

again.

The system sets the customs status of the customs groups, for example, Customs Clearance Requested. The system displays the

relevant cumulated customs status at header and item level in the freight document.

If you've assigned a block reason to the cumulated customs status, the system sets an execution block in the freight document.

TM fixes the freight document. Changes to the freight document aren't recommended at this point, but you can still update the

export declaration. For more information, see Changing Export Declarations.

SAP Global Trade Services creates the export declarations and submits them to the customs authorities.

## Changing Export Declarations

This is custom documentation. For more information, please visit SAP Help Portal.

34


1/14/26, 2:46 PM

After submitting a customs declaration, you sometimes need to change the document. Depending on your setup, you do this by

issuing a new declaration or by using customs update for the declaration.

## Change by Canceling and Resubmitting

Depending on the jurisdiction that you're exporting to, there are different ways to change issued export declarations. In certain

regions, you must first cancel the existing document, make the changes and re-create a new document.

## Prerequisites

Transportation Management (TM) is integrated with SAP Global Trade Services (GTS) or a similar customs management

application.

## Context

The standard process for changing existing export declarations is to cancel and reissue the document. This method is applicable in

most cases.

In addition, in some cases, you can update the documents in SAP GTS directly. For more information, see

https://help.sap.com/docs/SAP_GLOBAL_TRADE_SERVICES under  Application Help

 Customs Management

## Document

## Entry and Maintenance

 Creating Supplementary Customs Declarations .

## Procedure

1. In the freight document where you created the export declaration, cancel the declaration as described in Canceling Export

Declarations.

2. Change your customs groups as required.

3. Create a new export declaration from the customs group as described in Creating Export Declarations

## Results

The old declaration is canceled, and the new one is requested.

## Change Using Customs Update

Depending on the jurisdiction that you're exporting to, there are different ways to change issued export declarations. In certain

regions, you can update the declaration directly.

## Prerequisites

You've enabled customs update for the customs profile that your export declaration is relevant for. For more information,

see Customs Update for Export Declarations.

Transportation Management (TM) is integrated with SAP Global Trade Services (GTS) or a similar customs management

application.

## Context

This is custom documentation. For more information, please visit SAP Help Portal.

35


1/14/26, 2:46 PM

If the region you're exporting to allows it, you can activate customs update in the freight document to change it. When you save the

changes, the relevant export declaration is also updated.

  Restriction
You can't add additional freight units to an existing export declaration using customs update. For this you must first cancel the

document and resubmit it. For more information, see Change by Canceling and Resubmitting.

  Note

By default, updating a declaration isn't active. You can activate it for the jurisdictions that allow it. For more information, see

Customs Update for Export Declarations.

If the update button isn't visible, the mode isn't available for the export declaration.

## Procedure

1. In the freight document, select the customs group that the export declaration is valid for.

2. Choose Customs Update.

3. Make and save your changes.

## Results

The update request is sent to SAP Global Trade Services, which makes the changes and updates the document.

## Canceling Export Declarations

After issuing a customs declaration, you can cancel it if you need to make changes or no longer need to export the goods.

## Context

You've issued a customs export declaration and want to cancel it. You can do this in the freight document that you created the

customs declaration from.

In addition, you can cancel the document using SAP GTS. For more information, see

https://help.sap.com/docs/SAP_GLOBAL_TRADE_SERVICES under  Application Help

 Customs Management

## Document

## Entry and Maintenance

 Creating Supplementary Customs Declarations .

## Procedure

1. In the freight document, on the Customs tab, select the relevant customs group.

2. Choose Cancel Customs Declaration.

## Results

TM sends a cancellation request to SAP GTS.

TM sets the corresponding customs status, for example, Export Declaration Cancellation Requested. If you've assigned a block

reason to the relevant cumulated customs status, the system sets an execution block in the freight document. As soon as GTS has

confirmed the cancellation, TM updates the customs statuses accordingly.

This is custom documentation. For more information, please visit SAP Help Portal.

36


1/14/26, 2:46 PM

Import Declarations by LSPs

## Use

You use this process to create import declarations on behalf of shippers for customs-relevant items in forwarding orders. You can

enter the customs data and set the customs statuses manually in the forwarding order (FWO) or, to communicate with the

customs authorities, you can use an integrated customs management application. With the integrated solution, the customs

management application automatically creates the import declaration and handles the customs processes.

## Prerequisites

You have defined a customs activity that controls customs handling for import declarations and assigned the customs

activity to a customs profile. You have assigned the customs profile to the relevant freight unit types. You make these

settings in Customizing for Transportation Management as follows:

You define activities and profiles under  Basic Functions

## Global Trade

 Define Customs Activities and Profiles

.

For this process, you can use standard customs activity IMP_FU, which is assigned to standard customs profile

GT_IMPORT.

Note that you also have to define customs statuses and cumulated customs statuses. You assign the customs

statuses to the customs activity. You can also assign block reasons to cumulated customs statuses.

For more information, see Configuration of Customs Processing.

You define freight unit types in Customizing for Transportation Management under  Transportation Management

 Planning

## Freight Unit

 Define Freight Unit Types .

You have specified that customs handling is automatic for the relevant FWO types and that setting the Traffic Direction to

“Import” leads to and import order. For more information, see Customizing for Transportation Management under

Transportation Management

 Forwarding Order Management

## Forwarding Order

 Define Forwarding Order Types .

For automatic handling only: You have integrated TM with a customs management application.

  Note

Note that to create an import declaration, the FWO must contain one or more freight units (FUs). In the following process, it is

assumed that automatic FU creation has been set up in Customizing for Transportation Management.

## Process

1. You create an FWO with the required items.

You specify in the Traffic Direction attribute of the forwarding order type that the FWO is an import order.

You specify that the LSP is responsible for the import declaration by selecting the Import Decl. by LSP checkbox on the

General Data tab page in the FWO. Note that the system selects this checkbox automatically if you have selected the LSP

Import Declaration checkbox in the master data of the shipper.

2. You save the FWO and the system automatically creates freight units.

You trigger the creation of an import declaration from the forwarding order by choosing  Customs

## Create Import

Declaration  and then saving the FWO. When you save the forwarding order, the system does the following:

a. Checks whether a customs profile is assigned to the freight unit type (for example, standard customs profile

GT_IMPORT)

This is custom documentation. For more information, please visit SAP Help Portal.

37


1/14/26, 2:46 PM

b. Determines which customs activities are assigned to the customs profile (for example, standard customs activity

IMP_FU)

c. Runs the customs relevance check that is assigned to the customs activity (for example, standard customs

relevance check IMP_FU)

d. Creates custom groups

The system groups the items in the forwarding order according to the grouping strategy assigned to the customs

activity (for example, standard grouping strategy IMP_FU).

For more information about the standard grouping strategies, see Customs Groups.

On the Customstab page in the freight unit, you display the customs groups by selecting the customs activity in the

Customs Activity group box. The system displays the customs groups in the Item Groups table. You display the

items assigned to each customs group by selecting the customs group and choosing the Show Assigned Items

button.

e. Requests an import declaration for each customs group and sets the customs status of the customs groups (for

example, “Import Declaration Requested”)

The system sets the relevant cumulated customs status at header level and item level in the forwarding order, and at

header level in the freight unit. If you have assigned a block reason to the cumulated status, the system sets an

execution block in the forwarding order and the freight units.

For automatic handling only: In addition, the system triggers the Request Transportation Customs Declaration

(TransportationCustomsDeclarationRequest_Out) enterprise service. TM sends the request to the

customs management application.

3.

For manual handling only: you enter the following data (supplied by the customs authority) on the Customs tab

page at item level in the forwarding order:

## Customs management document number

This is the import declaration ID provided by the shipper or obtained using a non-integrated customs

management application.

## Customs reference number and expiration date

In the European Union, for example, this is the movement reference number (MRN). The goods import has to

take place by the expiration date.

If customs has approved an import declaration for a particular customs group, you set the corresponding customs

status (for example, “Import Declaration Approved”). The system displays the relevant cumulated customs status at

header and item level. If you have not assigned a block reason to the new cumulated customs status, the system

resets any existing blocks.

For automatic handling only: The customs management application creates the import declarations and submits

them to the customs authorities. When the customs management application receives an import confirmation from

the customs authorities, it sends a confirmation to TM that contains the following information

## Customs management document number

This is the import declaration ID provided by the customs management application.

## Customs reference number and expiration date

In the European Union, for example, this is the movement reference number (MRN). The goods import has to

take place by the expiration date.

This is custom documentation. For more information, please visit SAP Help Portal.

38


1/14/26, 2:46 PM

Indicator that shows the status of customs processing

The following values are possible:

Released: Customs clearance has been obtained for a customs group.

Canceled: An import declaration has been successfully canceled.

4.

## Result

For manual handling only: if customs has approved an import declaration for a particular customs group, you set the

corresponding customs status, for example, Import Declaration Approved. The system displays the relevant

cumulated customs status at header and item level. If you have not assigned a block reason to the new cumulated

customs status, the system resets any existing blocks.

For automatic handling only: TM receives the confirmation from the customs management application. The Change

Transportation Order Based on Transportation Custmos Declaration Confirmation

(TransportationCustomsDeclarationConfirmation_In) enterprise service receives the confirmation

from the customs management application. If customs has approved an export declaration for a particular customs

group, the system sets the corresponding customs status, for example, Import Declaration Approved. The system

displays the relevant cumulated customs status at header and item level. If you have not assigned a block reason to

the new cumulated customs status, the system resets any existing blocks.

When you create a freight document for the forwarding order, the freight document inherits the customs status from the

forwarding order. You can view the customs status on the Customs tab page in the freight document. The freight document also

inherits the customs information at item level. You can display this information on the Customs tab page in the item details.

For automatic handling only: To cancel an import declaration in the forwarding order, choose

## Customs

## Cancel Customs

Declaration . TM sends a cancellation request to the customs management application using the Request Transportation

Customs Declaration Cancellation (TransportationCustomsDeclarationCancellationRequest_Out) enterprise

service. TM sets the corresponding customs status, for example, Import Declaration Cancellation Requested. If you have

assigned a block reason to the relevant cumulated customs status, the system sets an execution block in the forwarding order and

the freight units. As soon as the customs management application has confirmed the cancellation, TM updates the customs

statuses accordingly. Note that import declaration documents are stored in the customs management application. The customs

management application sends an import declaration document to the email address of the TM user.

Transit Procedure

## Use

The transit procedure enables you to transport duty-unpaid goods within a customs union. To transport duty-unpaid goods, you

have to open the transit procedure so that the customs authorities can grant permission to transport the goods. You close the

transit procedure so that the customs authorities can grant permission to unload the goods.

Transportation Management (TM) enables you to make the required entries and settings that relate to the opening and closing of

the transit procedure.

You can connect the SAP-TM system to an external customs management applications., The customs process is triggered in TM

and sent to the connected customs management application. The TM system sets a customs status at each of the different steps

of customs processing.

## More Information

This is custom documentation. For more information, please visit SAP Help Portal.

39


1/14/26, 2:46 PM

Transit Procedure for Freight Documents

Transit Procedure for Freight Units

Transit Procedure for Freight Documents

## Use

You use this process to make the required entries and settings in a freight document that are related to the opening and closing of

the transit procedure.

  Note

For the transit procedure, TM does not provide functions for integrating a customs management application. You can make the

required entries and settings that relate to the transit procedure in the relevant business documents, but you cannot trigger

any follow-on processes in a connected customs management application. If required, however, you can implement a Business

Add-In (BAdI) in order to call an outbound service for a transit declaration. For more information, see Customizing for

Transportation Management under  Business Add-Ins (BAdIs) for Transportation Management

 Basic Functions

 Global

## Trade

## Declarations

 BAdI: Creation of Transit Declarations on Freight Document

.

The following is an example of the transit procedure for freight documents. Variants of this process are possible.

## Prerequisites

You have defined customs activities for opening the transit procedure and for closing the transit procedure. You have

assigned the customs activities to a customs profile. You have assigned the customs profile to the relevant freight

document types.

You make these settings in Customizing for Transportation Management as follows:

You define activities and profiles under  Basic Functions

## Global Trade

 Define Customs Activities and Profiles

.

You can use standard customs activity TRA_T1 for opening the transit procedure and TRA_T1_CL for closing the

transit procedure. These activities are assigned to standard customs profile GT_INBOUND.

Note that you also have to define customs statuses and cumulated customs statuses. You assign the customs

statuses to the customs activity. You can also assign block reasons to cumulated customs statuses.

For more information, see Configuration of Customs Processing.

You assign a customs profile to a freight order type under  Freight Order Management

 Freight Order

## Define

Freight Order Types .

You assign a customs profile to a freight booking type under  Freight Order Management

## Freight Booking

 Define Freight Booking Types .

You have defined that customs handling is automatic in the relevant forwarding order types. You define forwarding order

types in Customizing for Transportation Management under  Forwarding Order Management

## Forwarding Order

 Define Forwarding Order Types .

You have created a forwarding order with the required items, and you have made the following settings in the forwarding

order:

On the Actual Route tab page at item level, you have entered the required customs data (for example, commodity

code and previous documents) and you have set the inbound customs activity to Transit Procedure.

This is custom documentation. For more information, please visit SAP Help Portal.

40


1/14/26, 2:46 PM

On the Stages tab page, you have set the inbound customs activity to Transit Procedure for the relevant stages in

the actual route.

You have saved the forwarding order and the system has created freight units. Note that the system automatically sets the

inbound customs activity to Transit Procedure in the freight units.

To open the transit procedure, the goods have arrived at the point of entry into the customs union or the goods have been

stored in a bonded warehouse.

To close the transit procedure, the following requirements have been met:

The goods have arrived at the transit end location.

The transit procedure has been opened and approved.

## Process

1. You make the required entries and settings for opening the transit procedure (see Transit Procedure: Open Transit in Freight

Documents).

2. You make the required entries and settings for closing the transit procedure (see Transit Procedure: Close Transit in Freight

Documents).

3. You make the required entries and settings for canceling the transit procedure (optional).

You cancel a transit procedure by selecting the customs activity on the Customs tab page in the freight document and

choosing the Cancel Customs Declaration pushbutton.

In the freight document, the system sets the customs status of the customs groups as specified in the customs activity (for

example, “Open Transit Canceled” or “Close Transit Canceled”). In the freight document and the corresponding forwarding

order, the system sets the relevant cumulated customs status at header and item level. If you have assigned a block reason

to the cumulated customs status, the system sets an execution block in the freight document.

Transit Procedure: Open Transit in Freight Documents

## Use

You use this process to make the required entries and settings related to opening the transit procedure in a freight document.

Note that the following is an example of the transit procedure for freight documents. Variants of this process are possible.

## Prerequisites

You have made the required settings in Customizing for Transportation Management, and you have created a forwarding order

with the required freight units.

For more information, see Transit Procedure for Freight Documents.

## Process

1. You perform transportation planning for freight units in which the inbound customs activity Transit Procedure has been

specified.

When you save the resulting freight document, the system does the following:

This is custom documentation. For more information, please visit SAP Help Portal.

41


1/14/26, 2:46 PM

a. Checks whether a customs profile is assigned to the freight document type (for example, standard customs profile

for transit GT_INBOUND)

b. Determines which customs activities are assigned to the customs profile (for example, standard customs activity

TRA_T1)

c. Runs the customs relevance check that is assigned to each customs activity (for example, standard customs

relevance check TRA_T1)

In the freight document, the system displays the customs activities in the Customs Activity group box on the Customs tab

page and selects the Customs Relevance checkbox for the customs activities. The system displays the customs status for

the check result (for example, “Customs-Relevant”) at header level in the freight document (that is, on the Customs tab

page and Statuses tab page) and at item level (on the Customs tab page for the item).

Note the following:

If you have assigned a block reason to the relevant cumulated customs status, the system sets an execution block in

the freight document.

If a freight document is not customs-relevant, you can select the Customs Relevance checkbox manually and then

proceed with the next steps.

For information about the standard customs relevance checks, see Customs Relevance Check.

2. You open the transit procedure in the freight document by choosing  Customs

 Open Transit

.

The system automatically groups the items in the freight document according to the grouping strategy assigned to the

customs activity (for example, standard grouping strategy TRA_OPEN that is assigned to customs activity TRA_T1).

For information about the standard grouping strategies, see Customs Groups.

Before the system continues, it checks if the freight document has the required trigger status, that is, the execution status

specified in the customs activity. If required, you must set the corresponding execution status and save the freight

document again.

You display the customs groups by selecting the customs activity in the Customs Activity group box. The system displays

the customs groups in the Item Groups table. You can display the items assigned to each customs group by selecting the

customs group and choosing the Show Assigned Items pushbutton.

The customs status of each customs group is displayed in the Status field in the Item Groups table. At this point, each

customs group has the customs status for requesting the opening of the transit procedure, as defined in the customs

activity (for example, “Open Transit Requested”). At header level in the freight document (on the Customs tab page and on

the Statuses tab page) and at item level (on the Customs tab page for the item), the system displays the relevant

cumulated customs status. If you have assigned a block reason to the cumulated customs status, the system sets an

execution block in the freight document.

3. If a customs management application is connected, TM triggers the Request Transportation Customs Declaration

(TransportationCustomsDeclarationRequest_Out) enterprise service and sets the relevant cumulated customs

status at header level and item level.

If no customs management application is connected, you inform the customs authorities that you want to open the transit

procedure for the customs groups (for example, by using a non-integrated customs management application).

You cannot transport the goods to the transit end location until the customs authorities have approved the transit

procedure.

4. If no customs management application is connected, you manually change the customs status of the customs groups to

the relevant status (for example, “Open Transit Approved”).

You also enter the information provided by the customs authorities for each customs group:

This is custom documentation. For more information, please visit SAP Help Portal.

42


1/14/26, 2:46 PM

## Customs management document number

This is the unique document number that the customs management system assigns to a customs procedure that

you have triggered.

## Customs reference number

In the European Union, for example, this is the movement reference number (MRN).

## Expiration date

This is the date by which the transit procedure must be completed.

If a customs management application is connected, TM receives the Change Transportation Order Based on Transportation

Customs Declaration Confirmation (TransportationCustomsDeclarationConfirmation_In) enterprise service,

sets the above mentioned values, and sets the status “Released” or “Canceled” based on an indicator that shows the status

of the customs processing.

Based on the customs status of each customs group, the system sets the relevant cumulated customs status at header

level and item level in the freight document and the corresponding forwarding order. In addition, the system transfers the

customs reference number, customs management document number, and expiration date to the items in the forwarding

order (displayed on the Customs tab page at item level). If you have not assigned a block reason to the new cumulated

status, the system resets any existing execution blocks.

## Result

You can now transport the goods to the transit end location. When they arrive, you close the transit procedure by requesting

permission to unload the goods.

## More Information

Transit Procedure: Close Transit in Freight Documents

Transit Procedure: Close Transit in Freight Documents

## Use

You use this process to make the required entries and settings related to closing the transit procedure in a freight document.

Note that the following is an example of the transit procedure for freight documents. Variants of this process are possible.

## Prerequisites

You have made the required settings in Customizing for Transportation Management (see Transit Procedure for Freight

Documents).

You have opened the transit procedure in the freight document (see Transit Procedure: Open Transit in Freight Documents)

or the freight unit (see Transit Procedure for Freight Units).

## Process

1. You request permission to unload the goods by choosing  Customs

 Request Unload  for the corresponding unloading

location in the freight document.

This is custom documentation. For more information, please visit SAP Help Portal.

43


1/14/26, 2:46 PM

The system automatically groups the items in the freight document according to the grouping strategy assigned to the

customs activity for the unloading procedure (for example, standard grouping strategy TRA_CLOSE).

For information about the standard grouping strategies, see Customs Groups.

Before the system continues, it checks if the freight document has the required trigger status, that is, the execution status

specified in the customs activity. If required, you must set the corresponding execution status and save the freight

document again.

At this point, each customs group has the customs status for requesting permission to unload, as defined in the customs

activity (for example, “Transit Unload Requested”). At header level in the freight document (on the Customs tab page and

on the Statuses tab page) and at item level (on the Customs tab page for the item), the system displays the relevant

cumulated customs status. If you have assigned a block reason to the cumulated customs status, the system sets an

execution block in the freight document.

2. If a customs management application is connected, TM triggers the Request Transportation Customs Declaration

(TransportationCustomsDeclarationRequest_Out) enterprise service and sets the relevant cumulated customs

status at header level and item level.

If no customs management application is connected, you inform the customs authorities that you want to unload the goods

at the transit end location.

You cannot unload the goods until the customs authorities have granted permission to unload.

3. If a customs management application is connected, TM receives the Change Transportation Order Based on Transportation

Customs Declaration Confirmation. (TransportationCustomsDeclarationConfirmation_In) enterprise service

and sets the above mentioned status and values on its own.

If no customs management application is connected, you manually change the customs status of the customs groups to

the relevant status (for example, “Transit Unload Approved”).

Based on the customs status of each customs group, the system sets the relevant cumulated customs status at header

level and item level in the freight document and the corresponding forwarding order. If you have not assigned a block reason

to the new cumulated status, the system resets any existing execution blocks.

4. You unload the goods.

Transit Procedure for Freight Units

## Use

You use this process to make the required entries and settings related to opening the transit procedure for a freight unit in a

forwarding order. This process can be used, for example, if you need to add a package to a truck at the last minute. In this case, you

open the transit procedure in the freight unit before you assign the freight unit to the relevant freight document. However, you still

close the transit procedure from the freight document (see Transit Procedure: Close Transit in Freight Documents).

Note that the following is an example of the transit procedure for freight units. Variants of this process are possible.

## Prerequisites

You have defined a customs activity for opening the transit procedure and you have assigned the customs activity to a

customs profile. You have assigned the customs profile to the relevant freight unit types.

You make these settings in Customizing for Transportation Management as follows:

This is custom documentation. For more information, please visit SAP Help Portal.

44


1/14/26, 2:46 PM

You define activities and profiles under  Basic Functions

## Global Trade

 Define Customs Activities and Profiles

.

You can use standard customs activity TRA_T1_FU for opening the transit procedure in freight units. This activity is

assigned to standard customs profile GT_INBOUND_FU.

Note that you also have to define customs statuses and cumulated customs statuses. You assign the customs

statuses to the customs activity. You can also assign block reasons to cumulated customs statuses.

For more information, see Configuration of Customs Processing.

You assign the customs profile to the freight unit types under  Planning

## Freight Unit

 Define Freight Unit Types

.

You have defined that customs handling is automatic in the relevant forwarding order types. You define forwarding order

types in Customizing for Transportation Management under  Forwarding Order Management

## Forwarding Order

 Define Forwarding Order Types .

The goods have arrived at the point of entry into the customs union.

## Process

1. You create a forwarding order with the required items.

When you save the forwarding order, the system generates freight units.

2. On the Customs tab page at item level in the forwarding order, you enter the required customs data (for example,

commodity code and previous documents) and you set the inbound customs activity to Transit Procedure.

3. On the Stages tab page in the forwarding order, you set the inbound customs activity to Transit Procedure for the first

stage of the actual route.

4. You save the forwarding order.

On the Actual Route tab page at item level, the inbound customs activity is automatically set to Transit Procedure.

5. At item level in the forwarding order, you select the items that have been flagged as relevant for the transit procedure and

you choose the Open Transit pushbutton.

The system does the following:

a. Checks whether a customs profile is assigned to the freight unit type (for example, standard customs profile

GT_INBOUND_FU)

b. Determines which customs activities are assigned to the customs profile (for example, standard customs activity

TRA_T1_FU)

c. Runs the customs relevance check that is assigned to the customs activity (for example, standard customs

relevance check TRA_T1_FU)

d. Creates customs groups according to the grouping strategy assigned to the customs activity (for example, standard

grouping strategy TRA_OPENFU).

For more information about the standard grouping strategies, see Customs Groups.

6. You save the forwarding order.

7. You open the freight unit.

In the freight unit, the system displays the customs activity in the Customs Activity group box on the Customs tab page.

The system selects the Customs Relevance checkbox for the customs activity.

This is custom documentation. For more information, please visit SAP Help Portal.

45


1/14/26, 2:46 PM

You display the customs groups by selecting the customs activity in the Customs Activity group box. The system displays

the customs groups in the Item Groups table. You can display the items assigned to each customs group by selecting the

customs group and choosing the Show Assigned Items pushbutton.

The customs status of each customs groups is displayed in the Status field in the Item Groups table. At this point, the

customs groups have the customs status for requesting the opening of the transit procedure, as defined in the customs

activity (for example, “Open Transit Requested”).

At header level in the freight unit (that is, on the Statuses tab page and at the top of the Customs tab page), the system

displays the relevant cumulated customs status. The system also displays the cumulated customs status at header level in

the forwarding order (on the Statuses tab page) and at item level (on the Customs tab page for the item).

If you have assigned a block reason to the cumulated customs status, the system sets an execution block in the freight unit

and the forwarding order.

8. You inform the customs authorities that you want to open the transit procedure for the customs groups (for example, by

using a non-integrated customs management application).

You cannot transport the goods to the transit end location until the customs authorities have approved the transit

procedure.

9. In the freight unit, you manually change the customs status of the customs group to the relevant status (for example,

“Open Transit Approved”).

You enter the information provided by the customs authorities for the customs group:

## Customs management document number

This is the unique document number that the customs management system assigns to a customs procedure that

you have triggered.

## Customs reference number

In the European Union, for example, this is the movement reference number (MRN).

## Expiration date

This is the date by which the transit procedure must be completed.

The system transfers the customs reference number, customs management document number, and expiration date to the

items in the forwarding order (displayed on the Customs tab page at item level).

Based on the customs status of each customs group, the system sets the relevant cumulated customs status at header

level in the freight unit (that is, at the top of the Customs tab page). It also sets the cumulated customs status in the

forwarding order at header level (Status tab page) and item level (Customs tab page for the item). If you have not assigned

a block reason to the cumulated status, the system resets any existing execution blocks.

## Result

After opening the transit procedure, you must assign the freight unit to the relevant freight document. This enables you to close

the transit procedure in the freight document.

## More Information

Transit Procedure for Freight Documents

## Trade Compliance Check

This is custom documentation. For more information, please visit SAP Help Portal.

46


1/14/26, 2:46 PM
## Use

You can use this process to perform a trade compliance check for new or changed business documents in Transportation

Management (TM). The check is performed in the SAP Global Trade Services application.

## Prerequisites

You have set up the integration scenario TM_GTSTradeComplianceCheckIntegration in SAP NetWeaver Process Integration,

and you have implemented the required enterprise services.

For more information, see Integration with SAP Global Trade Services.

Note that the integration with SAP Global Trade Services is designed for a system landscape in which there is only one

global trade services (GTS) system connected to each TM system.

You have enabled the compliance check for the relevant business document types in TM by selecting the Enable

Compliance Check checkbox in Customizing for the document types. You can enable the compliance check for the

following document types in Customizing for Transportation Management:

Forwarding Order Management

## Forwarding Order

 Define Forwarding Order Types .

Forwarding Order Management

## Forwarding Quotation

 Define Forwarding Quotation Types .

Freight Order Management

## Freight Order

 Define Freight Order Types .

Freight Order Management

## Freight Booking

 Define Freight Booking Types .

You have set up In-Application-Sequencing to ensure that incoming messages are processed in the correct sequence at

application level. Whenever a missing message is detected for a new message, the new message is put into a waiting queue

until the missing message arrives. For more information, see Customizing under  Cross-Application Components

 Processes and Tools for Enterprise Applications

## Enterprise Services

 Point-to-Point Enablement for Asynchronous

## Enterprise Services

 Activate Support for Point2Point Communication .

You have defined whether processes are blocked if TM sets the following block reasons:

Compliance Check Required: A compliance check is required for a business document, but the result has not been

received from the global trade services (GTS) system.

Compliance Check Failed: The business document is not compliant according to the check performed by the GTS

system.

You define which processes are blocked in Customizing for Transportation Management under  Basic Functions

## General Settings

 Define Block Reason Codes .

  Note

The trade compliance check in SAP Global Trade Services consists of sanctioned party list screening and an embargo

check. During sanctioned party list screening, the GTS system compares business partner addresses with the addresses

on the relevant sanctioned party list. During the embargo check, the GTS system determines whether a business partner

involved in a business transaction is subject to an embargo situation due to the location of the business partner’s

company.

For more information, see SAP Library for SAP Global Trade Services on SAP Help Portal at http://help.sap.com/grc

under  SAP Global Trade Services

 Compliance Management

.

For sanctioned party list screening, the GTS system checks address data that is derived only from business partner

master data. It does not check address data derived from locations. In addition, it does not check addresses that a user

enters in the Printing Address field on the Business Partner tab page in the forwarding order.

This is custom documentation. For more information, please visit SAP Help Portal.

47


1/14/26, 2:46 PM

For the embargo check, the GTS system checks the countries or regions in the transportation route.

## Process

1. You save a new or changed business document in TM, and the system automatically determines if the compliance check

has been enabled for the corresponding document type.

If the compliance check has been enabled, TM proceeds as follows:

It sets the compliance check status of the business document to Not Checked and displays the status on the

Statuses tab page. Note that the compliance check status is displayed only if the compliance check has been

enabled for the document type.

If you have activated blocking for the block reason Compliance Check Required, it blocks the relevant processes

(for example, planning or execution).

It makes sure that only compliance-relevant data entered in a new document or changed in an existing document is

checked; that is, business partner data for sanctioned party list screening, or the countries or regions in the

transportation route for the embargo check.

It requests a trade compliance check for the business document in the GTS system.

TM sends the request using the enterprise service Request Trade Compliance Check

(TradeComplianceCheckSUITERequest_Out) in the Transportation Order Processing process component.

2. The GTS system performs the trade compliance check on the data received from TM.

If the check fails, the business document is blocked in the GTS system. Note that a compliance manager can manually

override the result of a failed check in the GTS system and unblock the business document.

3. The GTS system returns the result of the trade compliance check to TM, which proceeds as follows:

If the business document is not compliant, TM sets the compliance check status to Not Compliantand sets the

blocks that you have assigned to block reason Compliance Check Failed.

If the business document is compliant, it sets the compliance check status to Compliantand cancels any blocks that

were set for block reason Compliance Check Required.

In TM, the result of the check is received by the enterprise service Change Transportation Document Based on Trade

Compliance Check Confirmation (ChangeTradeComplianceCheckSUITEConfirmation_In).

4. TM requests the cancellation of the trade compliance check for the business document.

Regardless of the result of the trade compliance check, the GTS system continues to check the business document

periodically until it receives a cancellation request. TM sends a cancellation if the transportation activities have been

completed (life cycle status Executed) or if the business document has been canceled (life cycle status Canceled). The

business document that was created in the GTS system is canceled accordingly.

TM requests the cancellation using the enterprise service Request Trade Compliance Check

(TradeComplianceCheckSUITECancellationRequest_Out).

## Customs Transit Discharge

You can use this process to secure approval from SAP Global Trade Service (SAP GTS) to unload a freight order.

The process is based on the Customs Reference Number (CRN) – you can enter this manually for the consignments of the freight

order or the system can include it in the consignment information automatically if the freight order comes by EDI. Once a freight

This is custom documentation. For more information, please visit SAP Help Portal.

48


1/14/26, 2:46 PM

order has been checked in, the transit discharge is requested automatically – a manual request is also possible.

## Prerequisites

You've activated the compliance check in the logistics integration profile. For more information, see Customizing for

Transportation Management under

## Integration

## Logistics Integration

  Internal TM Component Integration

## Define

Logistics Integration Profile for SD, MM, and LE .

You've defined customs activities and a customs profile, and assigned one or more customs activities to the respective customs

profile. You've assigned the customs profile to a freight order type configured for an import process.

For more information, see Customizing for Transportation Management under  Basic Functions

 Global Trade

## Define

Customs Activities and Profiles .

## Process

1. You accept an order, setting the Execution Status of the freight order to Ready for Transportation Execution.

2. You check in the freight order, if compliant, by setting the Handling Execution Status to Checked In.

3. The system creates customs groups, taking into account the CRN maintained for each consignment item on the freight

order, and creates a request for unloading permission that it sends to SAP GTS. Pending the outcome of this request, the

system places a block on the stop.

4. SAP GTS sends an approval for the unloading permission. You can now update the Warehouse Processing Status to Ready

for Warehouse Processing.

## Related Information

Integration with SAP Global Trade Services

SAP GTS Integration for the Outbound Process

SAP GTS Integration for the Inbound Process

Execution Tracking

## Use

In Transportation Management (TM), you use this function to determine whether the end user can manually report the execution

of transportation processes managed by TM, or not. For example, the end user reports that an event has happened such as a

freight order has arrived at a destination.

Execution Tracking reports the tracking of the following TM business documents:

## Freight Units

Freight Orders and Freight Bookings

Transportation Units

  Note

Execution tracking is a basic TM function that does not require an external event management system, such as SAP Event

Management.

This is custom documentation. For more information, please visit SAP Help Portal.

49


1/14/26, 2:46 PM
## Features

You have the following options for execution tracking:

## No Execution Tracking

With this option selected, there is no tracking of executions. This is the default option.

## Execution Tracking

With this option you allow execution tracking without an external event management system. That is, the system

automatically starts the tracking of executions reported manually from transportation processes managed by TM. The data

this creates is stored in the TM database.

## Execution Tracking with External Event Management

With this option you allow execution tracking with an external event management system. The system stores the data from

the tracking of executions in the TM database, but it can also send it to an external event management system. This option

requires the connection of an external event management system, such as SAP Event Management. For more information

about integration with SAP Event Management, see Integration with SAP Event Management.

The use of SAP Event Management means that an end user can use its simple in-built interfaces to report actual events,

such as a freight order has arrived. Further, the time that those actual events occurred can be compared with the time they

were expected to occur. In addition, SAP Event Management allows events that are related but unexpected to be reported.

Together this means that for any tracked item a database record is always available including its last known event. From

that you can know whether that item is on track, late or whether an unexpected has happened to it. You can also use rule-

based processing in-built into SAP Event Management to trigger automatic follow up activities. For example, when a freight

order is received at its final destination, to update documents in TM and SAP ERP and send e-mail notification to all

involved parties.

  Note

In TM what is called an “execution” is called an “event” in event management systems.

If you allow execution tracking, we recommend you enter a last expected event. If you do not enter one, the

system uses UNLOAD_END as the last expected event by default.

Allowing execution tracking also has an effect on the propagation of events on document level. The system

checks if a business document and its predecessor document are relevant for execution tracking. If they are,

then the system propagates the event to the predecessor document. In the same way, if both a business

document and its successor document are relevant for execution tracking, the system propagates the event to

the successor document.

If, for example, a freight order and the related freight unit are relevant for execution tracking, the event is

propagated from the freight order to the related freight unit.

## Activities

You can see and change the current settings for execution tracking in Customizing. The path in Customizing depends on the type

of TM business document as follows:

For freight orders, make the settings in Customizing for Transportation Management under  Freight Order Management

## Freight Order

 Define Freight Orders Types . Then you select the Details button and under Execution Settings, select

an option from the field Execution Tracking Relevance.

For freight bookings, make the settings in Customizing for Transportation Management under  Freight Order

Management

## Freight Booking

 Define Freight Booking Types . Then you select the Details button and under

This is custom documentation. For more information, please visit SAP Help Portal.

50


1/14/26, 2:46 PM

Execution Settings, select an option from the field Execution Tracking Relevance.

For transportation units, make the settings in Customizing for Transportation Management under  Freight Order

## Management

## Transportation Unit

 Define Transportation Unit Types . Then you select the Details button and under

Execution Settings, select an option from the field Execution Tracking Relevance.

For freight units, make the settings in Customizing for Transportation Management under  Freight Order Management

 Planning

## Freight Unit

 Define Freight Unit Types . Then you select the Details button and under Execution Settings,

select an option from the field Execution Tracking Relevance.

Management of Instructions

## Use

An instruction is an individual step in a procedure that a user must carry out in the execution process. You can gather together

instructions in instruction sets and display them in a list of tasks on the user interface (UI).

For example, you can create an instruction set for a fumigation service. The set can include the following individual instructions:

Clean the container

Fumigate the container

## Seal the container

The system displays the list of instructions on the Instructions tab page of the business document. You can edit and delete the

instructions that the system adds automatically. You can insert instructions that suit your own business requirements. You can also

specify the priority of a set of instructions by editing the sequence field.

You can specify the following settings for an individual instruction:

Task or for information purposes

## Due date and alert date

Status of pending, in progress, or completed

## Responsible role and responsible user

If you set the status of an instruction to completed, the system automatically enters the current date as the completion date. You

can also manually enter the completion date after you have set the status to completed.

## Integration

If Transportation Management (TM) is integrated with SAP Event Management, the SAP Event Management system automatically

enters the following statuses for an instruction task:

Alert when the alert date has passed

## Overdue when the due date has passed

Completed After Due Date if you set the status of the instruction to Completed after the due date has passed

## Prerequisites

This is custom documentation. For more information, please visit SAP Help Portal.

51


1/14/26, 2:46 PM

You have defined instructions and assigned them to an instruction set in Customizing for Transportation Management under

Basic Functions

## Instructions

 Define Instructions and Instruction Sets .

You have assigned instruction sets to one or more object types in Customizing for Transportation Management under  Basic

Functions

## Instructions

 Assign Instruction Sets .

## Features

Instructions enable you to use the following features:

Specify general instructions in Customizing that you can reuse in multiple business documents for multiple customers.

This decreases duplication and work effort. You do not need to recreate instructions for each business document.

Include specific instructions for a customer in a particular business document

Reduce the need for the user to make unplanned decisions during execution

Ensure uniformity and compliance when you execute similar tasks

Each instruction contains the following information:

What must be done

Who performs the task

## When must the task be completed

You can assign instructions sets to particular object types in Customizing. The enables the system to automatically include the

relevant instructions when you use an object type to create a business document. For example, you assign an instruction set to a

stage type in Customizing. When you create a forwarding order that includes the relevant stage type, the system automatically

includes the relevant instruction set for the stage.

You can assign instruction sets to the following object types in Customizing:

Services

## Stages

Forwarding order items, such as container, product, and package

## Forwarding order types

In Customizing, you can also specify that the instructions flow to the forwarding order and freight unit business documents. In the

application, the system only displays the relevant instructions in the relevant business document. In this way, the user can only

work on instructions that are relevant for a particular part of the execution process.

For example, when you create a forwarding agreement, the system displays all the relevant instructions. When you create a follow-

on forwarding order from the agreement, the system only makes the instructions that are relevant for the forwarding order

available to the user. Similarly, when you create a follow-on freight unit from the forwarding order, the system only makes the

instructions that are relevant for the freight unit available to the user.

More Information

Service Product Catalogs

## Determination of the Route

This is custom documentation. For more information, please visit SAP Help Portal.

52


1/14/26, 2:46 PM

Creation of Forwarding Order Items or Forwarding Quotation Items

Creation of a Forwarding Order

Freight Unit

Change Tracking

## Use

You can use this function to display which data was changed, how it was changed, when it was changed, and by whom it was

changed for the following business documents:

Forwarding order

Forwarding quotation

Freight unit

Freight order

Freight booking

Transportation unit

Service order

## Prerequisites

In Customizing, you have activated change tracking for each of the business document types. For more information, see

Customizing for Transportation Management under:

Forwarding Order Management

## Forwarding Order

 Define Forwarding Order Types .

Forwarding Order Management

## Forwarding Quotation

 Define Forwarding Quotation Types .

Planning

## Freight Unit

 Define Freight Unit Types .

Freight Order Management

## Freight Order

 Define Freight Order Types .

Freight Order Management

## Freight Booking

 Define Freight Booking Types .

Freight Order Management

## Transportation Unit

 Define Transportation Unit Types .

Freight Order Management

## Service Order

 Define Service Order Types .

## Features

The changes are displayed on the Change Documents tab page on the user interfaces of the business documents.

You can display the changes in different views:

The flat view shows all changes made to your business document and the relevant information in a flat list.

In the hierarchical view, you can see who changed the business document and when it was changed. If you select a line,

more details are shown in the lower part of the screen, for example, what exactly was changed.

This is custom documentation. For more information, please visit SAP Help Portal.

53


1/14/26, 2:46 PM

To display the changes, you need to select Apply. You can restrict the data to be displayed by entering search criteria. There are

different search criteria for the two views:

## Flat view

You can search by user, from date, and to date. Also, you can search by the fields of a business object node (technical name

or data access definition).

## Hierarchical view

You can search by user, from date, and to date.

Further, you can switch between the preferred time zone and the individual time zone depending on what you selected in the

display settings. For more information, see Display Settings.

  Note

The Change Documents tab page is not shown by default. However, you can display it with the pushbutton for

personalizing your user interface.

If you want to display more technical information, you can personalize the views.

Text Collection

## Definition

An object that is used to store texts that are related to a business document.

## Use

You use this object in Transportation Management (TM) to create and store texts that are related to a business document, for

example a freight order or a forwarding order.

## Structure

The text collection stores text that is categorized according to its text type, the language it is written in, and the type of use

(internal or external). For example, the text may be of the type Special Note, it may have been written in English and it may be for

internal use only.

You define text types in Customizing.

Text types can be assigned to text schemas. When assigning the text type to text schemas, you can specify attributes that are

automatically inherited by all texts created using this text type. You assign text types to text schemas in Customizing.

You define a text schema and you assign it to a business document in Customizing.

For more information, see Customizing for Transportation Management under  Basic Functions

 Text Collection

## Define

Settings for Text Collection .

On the user interface, you can identify the text collection by the name Notes.

## Integration

This is custom documentation. For more information, please visit SAP Help Portal.

54


1/14/26, 2:46 PM

In the standard system, you assign a standard text schema to certain business documents in Customizing.

You can enhance this assignment by defining your own text types and text schemas and by assigning the text schemas to business

documents.

You assign a text schema to a business document by specifying it in the business document type in Customizing. For example, you

can assign a text schema to your freight order type in Customizing for Transportation Management under  Freight Order

Management

## Freight Order

 Define Freight Order Types .

## Assign Text Schemas to an Item Type

You can assign a text schema to each item type, for example, a product or package, in a business document type. This allows you to

define a different, relevant text schema for each item type. You can also assign a different text schema to the same item type in

different business document types. If no text schemas are assigned to an item type, then no texts are determined.

For more information, see Customizing for Transportation Management under:

Freight Order Management

## Freight Order

 Define Freight Order Types

Freight Order Management

## Freight Booking

 Define Freight Booking Types

Freight Order Management

## Transportation Unit

 Define Transportation Unit Types

Freight Order Management

## Service Order

 Define Service Order Types

Freight Order Management

## Consignment Order

 Define Consignment Order Types

Planning

## Freight Unit

 Define Freight Unit Types

## Working with Attachments

In your daily work, you deal with attachments that are related to a business document, for example a freight order or a forwarding

order. You can store, display, download, and print attachment files.

## Prerequisites

You've assigned an attachment schema to the relevant business document type.

The following attachment schemas are available:

DEFAULT: This is the default attachment schema and it’s configured to use an attachment folder. This schema

allows you to create a hierarchy of folders where you can upload files and create attachment URLs. You can also

adapt the visibility type of an attachment.

DEFLT_ATS: This attachment schema is configured to use the Attachment Service and it allows you to attach files

and attachment URLs in a flat structure. This schema doesn’t support the creation of folders, and it only supports

externally visible attachments.

If you want to define your own attachment schemas, see Defining Custom Attachment Schemas.

  Note
If you switch between attachment schemas for a business object type, the files and URLs that were previously

uploaded won’t be visible. The attachments will be visible again if you switch back to the attachment schema

that was used when uploading the attachments.

This is custom documentation. For more information, please visit SAP Help Portal.

55


1/14/26, 2:46 PM

If you want to print attachments, you must define an output device by choosing  System

 User Profile

 Own Data

## Defaults

 Spool Control

.

## Features

You can store attachments that are related to a business document on the Attachments tab of the business document.

If you’re using an attachment schema that is configured to use the attachment folder, you can structure the attachments

by creating folders.

You can store links using uniform resource locators (URLs) to navigate to external content. For example, links to content on

the Internet or links to files stored on a server.

Related Information

## Attachment Service

## Defining Custom Attachment Schemas

You can define your own attachment schemas to allow you to work with attachments that are related to business documents.

## Procedure

1. Define a content repository in Customizing for SAP NetWeaver under  Application Server

 Basis Services

 Knowledge

## Provider

 Content Management Service

 Define Content Repositories .

2. Link the content repository to the attachment folder document area by defining a content category in Customizing for SAP

NetWeaver under  Application Server
Content Categories .

 Basis Services

 Knowledge Provider

 Content Management Service

 Define

  Note

To use the Attachment Service, you must use the content category BS_ATF_ATS.

3. Define attachment types and an attachment schema in Customizing for Cross-Application Components under

Processes and Tools for Enterprise Applications
Object Attachment Folder

 Maintain Attachment Type Schema .

 Reusable Objects and Functions for BOPF Environment

## Dependent

Ensure that the MIME type of the documents you want to attach is assigned to your business object node.

4. Configure the attachment schema to use the Attachment Service by linking document types with object types in

Customizing for Cross-Application Components under  Classification System

## Classes

 Maintain Object Keys .

The following object types are available:

Object Type

TMFAGROOT

## TMFAGITEM

Business Object

## Node

/SCMTMS/FREIGHTAGREEMENT

## ROOT

/SCMTMS/FREIGHTAGREEMENT

## ITEMS

You can use document type TAT in TM. However, if you have existing document types or want to create your own document

types, you must perform the following steps:

a. Link your document types to the object types in Customizing for Cross-Application Components under

Document Management

## Control Data

 Define Document Types .

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

56


1/14/26, 2:46 PM

If you currently use an attachment schema for the attachment folder and intend to use Attachment Service

going forward, we recommend that you create new document types instead of using the existing ones.

b. In the same Customizing activity, link the document type with the object type under  Define Document Types

 Define Object Links .

c. In the same Customizing activity, maintain an object link description under Maintain Object Link Descriptions.

## Results

You've defined your own attachment schema, and you can now assign the attachment schema to the relevant business document

type. For more information, see Working with Attachments.

Display Settings

## Use

You can use this function to make the following settings in Transportation Management (TM):

Time Zone for the Display of Date and Time

## Unit of Measure for Distances

List Header (Disable Text Wrapping in Column Headers)

Charges (Default View)

Features

## Time Zone

The following options are available to you for configuring the time zone:

## User Time Zone

This is your local time zone, in other words, the time zone of the location in which your computer is situated. If you choose

this option, the date and time you entered for the local time zone in your user profile are valid.

## Individual Time Zone

This is any time zone that you can define yourself. If you choose this option, the date and time you entered for this time

zone are valid.

## Location-Dependent Time Zone

If you choose this option, the system automatically determines the time zone for the location entered (for example, from

the location master data). If no time zone is available for a location, the system uses either the user time zone or the

individual time zone, depending on the option selected. Therefore, this option takes priority over the other two options.

The system takes the location-dependent time zone by default. If no time zone is available for a location, the system uses

the user time zone.

  Note

If you change the settings of the time zones, the system converts a date and a time that have already been entered to the date

and time of the new time zone. However, if you have selected the option Location-Dependent Time Zone and you change a

This is custom documentation. For more information, please visit SAP Help Portal.

57


1/14/26, 2:46 PM

previously entered location to a location with a different time zone, the system keeps the date and time. The system does not

convert it to the date and time of the new time zone.

## Unit of Measure

To define the unit of measure for the display of distances (for example, kilometers or miles), you have the following options:

## Standard Unit of Measure

The standard unit of measure is Kilometer.

## Individual Unit of Measure

This is any unit of measure that you can define yourself.

## Location-Dependent Unit of Measure

If you choose this option, the system automatically determines the unit of measure for the geographical region of the

location entered (for example, from the location master data). If no unit of measure is available for a location, the system

uses either the standard unit of measure or the individual unit of measure, depending on the option selected.

## Times and Durations

You can indicate whether you want to use the short time format (hh:mm) to display times. Further, you can indicate in which

format durations are to be displayed. You have the following options:

## Full Days, Hours, Minutes

If you select this option, the duration is displayed as dddd hh:mm. For example, a duration of 36 hours would be displayed

as 1 12:00.

## Full Days and Fraction of Days

If you select this option, the duration is displayed as a fraction. For example, a duration of 36 hours would be displayed as

1.5.

## Hours, Minutes

If you select this option, the duration is displayed as hhhh:mm. For example, a duration of 36 hours would be displayed as

36:00.

List Header (Disable Text Wrapping in Column Headers)

The system tries to wrap longer column headers in up to three lines if the column header text is longer than the possible content of

the corresponding cells. You can deactivate this function.

## Charges

You can choose whether you want the system to display an expanded view or a collapsed view of the charge items as the default

view.

## Activities

On the user interface, you choose Display Settings. A dialog box appears in which you can make the settings. Changes to settings

have an immediate effect.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

58


1/14/26, 2:46 PM

The changes only have an effect on Web Dynpro-based screens.

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

## Definition of a Condition for Time Windows

This is custom documentation. For more information, please visit SAP Help Portal.

59


1/14/26, 2:46 PM

Definition of Conditions

## Use

You can use this function to define conditions.

## Prerequisites

SAP delivers the following in the standard system:

## Condition types

Customer condition types

## Data access definitions

Assignments of data access definitions to condition types (including specification of which data access definitions are used

by default for a condition type)

If you need additional fields for the condition types delivered as standard or you want to use customer condition types, you have to

create new data access definitions and extend the assignments in Customizing, as required. You can also change or add to the data

access definitions used by default.

For more information about creating data access definitions, see Customizing for Transportation Management under  Basic

Functions

## Conditions

 Data Access Definition .

For more information about assigning data access definitions to condition types, see Customizing for Transportation

Management under  Basic Functions

## Conditions

 Assign Condition Type to Data Access Definition .

You can define your own condition types in Customizing. For more information, see Customizing for Transportation Management

under  Basic Functions

## Conditions

 Define Condition Types .

## Features

## Definition of General Data and Decision Table

First, you define the condition type and specify the origin of the condition:

The system adopts these values (direct business object access).

The system uses the values as input values for a BRFplus decision table (BRFplus = Business Rule Framework plus).

The system creates a condition based on BRFplus expressions.

If you have specified that the condition is based on a BRFplus decision table, the system automatically creates a decision table on

the basis of the standard data access definitions assigned in Customizing. You can now process this decision table by entering

specific values. For more information about BRFplus, see Business Rule Framework plus (BRFplus).

Use Data Access Definition to change the data access definition. In the data access definition, you define which values the system

adopts directly or uses as input values for a decision table, and where it determines this data.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

60


1/14/26, 2:46 PM

However, you can also define the data source independently of the data access definition, for example, if you have particularly

special values. Note that, for such assignments, the system can only use data that is available when the condition is evaluated.

When the system checks the condition, it processes the decision table starting from the top. As soon as the system finds a row

that contains the required value for each column, it uses the values defined in the output.

Since the sequence of the rows in the decision table is important, make sure that you decide before inserting new rows whether

you want to append the new rows or whether you want to insert them between two existing rows. You can change the sequence of

the rows.

If you have specified that you want to create a condition based on BRFplus expressions, the system automatically creates a

function and signature in BRFplus when you create the condition. In BRFplus, you then use corresponding expressions to define

how the values are determined. For more information, see Business Rule Framework plus (BRFplus).

## Definition of Data Access Definitions

In the standard system, SAP delivers data access definitions as well as assignments of data access definitions to condition types.

In Customizing, you can create additional data access definitions, for example, to take into account fields that you have added to a

node. Moreover, you can make additional assignments or delete existing assignments in Customizing. Once you have added an

assignment, you can choose the corresponding data access definitions for the input values. Define only those values that you want

to be available when you call the condition. When doing so, you can use the data access definitions delivered with the standard

system for orientation purposes. Other fields from data access definitions that are assigned by default to the condition type are

available. This is also true of other nodes in the hierarchy if they are above or below the nodes that are predefined in the data

access definition assigned by default. You can check the hierarchical relationship of the nodes in transaction /BOBF/CONF_UI.

## Definition of Customer Condition Types

To determine conditions in a flexible way, you can use the customer condition types delivered with the standard system. You assign

data access definitions to these customer condition types in Customizing. You can also define your own customer condition types

in Customizing. We recommend that you only use your own customer condition types if these are called from your enhancement

coding.

## Example

You want to define a condition with which you can specify the determination of freight unit building rules (FUB rules) when using

dangerous goods.

In this case, you define a condition with the condition type /SCMTMS/FUBR based on a decision table.

Input value: Specifies whether the business document item of the business document of forwarding order management

(forwarding order, forwarding quotation, order-based or delivery-based transportation requirement) contains dangerous goods.

## Output value: FUB rule that the system uses

You enter a data access definition that identifies the dangerous goods. In the decision table, you specify that FUB rule 1 is used

when dangerous goods are involved, and FUB rule 2 is used when no dangerous goods are involved.

Depending on whether dangerous goods are involved or not, the system determines the relevant FUB rule based on the condition.

## More Information

## Definition of a Condition for Time Windows

This is custom documentation. For more information, please visit SAP Help Portal.

61


1/14/26, 2:46 PM

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

This is custom documentation. For more information, please visit SAP Help Portal.

62


1/14/26, 2:46 PM

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
constraint)

2 (hard constraint)

0

## False

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

Use of Data Crawler Input Values

## Use

When you are defining conditions, you can use data crawler input values. Using data crawler input values is advantageous in the

following cases:

The data that you want to use as input values is in a different business object. For example, you might want to use fields

from a forwarding order for a determination in a freight unit or a freight order.

You want to use specific associations within a business object, for instance, in order to use data of the first stop for a freight

order.

## Prerequisites

You have defined a data crawler profile in Customizing. For more information, see Customizing for Transportation

Management under  Basic Functions

## Conditions

 Define Data-Crawler Profile .

In Customizing in the data access definition, you have assigned the following in the Data Crawler area:

## Data Crawler Profile

Step (defines the node that you want to use as an input value)

## Field

This is custom documentation. For more information, please visit SAP Help Portal.

63


1/14/26, 2:46 PM

In addition, you have also specified a data element for F4 helps.

For more information, see Customizing for Transportation Management under  Basic Functions

 Conditions

## Data

Access Definition .

You have assigned your condition type for the data access definition in Customizing. For more information, see Customizing

for Transportation Management under  Basic Functions

## Conditions

 Assign Condition Type to Data Access Definition

.

## Features

In accordance with your settings in Customizing, the system uses the input values that you have defined with the data crawler

profile for the determination of values with your condition.

## Example

You want to determine the ERP order type for a freight unit from the TRQ root (TRQ_ROOT). To do this, you have defined a data

crawler value profile DC_FU_TO_TRQ_ROOT with the following values:

Attribute

Step

Value

10

## BO Name

/SCMTMS/TOR

Association

BO_TRQ_ROOT_ALL

Target Node

## TRQ_ROOT

In addition, you have defined data access defintion DAD_FU_TO_TRQ_ROOT with the following values:

## Attribute

Data Crawler Profile

## Step

Field Name

## Value

DC_FU_TO_TRQ_ROOT

10

## BASE_BTD_TCO

## Data Element for F4 Helps

/SCMTMS/BASE_BTD_TCO (Basis document type for business

transaction)

Change Controller

## Use

You can use this function to check whether the following business documents have changed and how the system is to process

these changes:

Freight order (see Freight Order)

Freight unit (see Freight Unit)

Freight booking (see Freight Booking)

This is custom documentation. For more information, please visit SAP Help Portal.

64


1/14/26, 2:46 PM

Transportation unit (see Transportation Unit

Service order (see Service Order)

## Prerequisites

You have made the settings for the change controller. For more information, see Settings for the Change Controller.

## Features

The change controller can react to the following planning-relevant changes:

## Quantity changes

You can use a quantity tolerance determination condition to determine the tolerances for a quantity change in a business

document. This means that in case of a quantity change, the change controller evaluates this condition to dynamically

determine if this quantity change can be classified as relevant or if it can be ignored. You assign this quantity tolerance

determination condition to your business document type (for example, freight unit type). For more information, see the

corresponding field help in the Customizing activity for defining the business document type, for example freight unit type.

## Changes to dates/times

You can use a date tolerance determination condition to determine the tolerances for a date change in a business

document. This means that in case of a date change, the change controller evaluates this condition to dynamically

determine if this date change can be classified as critical or uncritical or if it can be ignored. You assign this date tolerance

determination condition to your business document type (for example, freight unit type). For more information, see the

corresponding field help in the Customizing activity for defining the business document type, for example freight unit type.

Changes to source locations, intermediate stops, and destination locations

Changes to the transportation service level

## Reported execution information

Additional or deleted freight unit or location in the context of one of the following associated business documents:

Forwarding order

## Forwarding quotation

Order-based transportation requirement

## Delivery-based transportation requirement

The change controller can react to changes by performing the following actions for example:

Remove corresponding freight units from the transportation plan

Invalidate successor business documents such as freight orders

Stop the current associated tendering processes

Stop and restart the current associated tendering processes

## Issue alerts

You can also define your own actions.

You can use the process controller (see Process Controller Configuration) and conditions (see Condition) to define the parameters

for regulating the change controller. SAP delivers process-controller-relevant and condition-relevant objects for the change

This is custom documentation. For more information, please visit SAP Help Portal.

65


1/14/26, 2:46 PM

controller. For more information, see Objects Delivered by SAP for the Change Controller.

  Note

This chapter mainly describes how the change controller is to react to changes. But you can also define strategies that

are executed by the change controller each time a business document is saved or when a business document is created

or deleted.

The strategies delivered by SAP are templates that you can enhance or change. For example, in the strategies delivered

by SAP, the system always unfixes the business documents for which the strategies are executed to allow the strategies

to perform changes on these business documents. If you do not want the business documents to be unfixed during

execution of the strategy, you have to create your own strategy without using the following methods:

UNFIX_TORC

UNFIX_TORS

UNFIX_TORU

## Activities

The change controller is executed automatically whenever the situation that you have defined in Customizing occurs. If, for

example, you have assigned a certain change strategy to a certain freight unit type, the change controller executes that strategy

whenever a freight unit of that type is changed.

## Objects Delivered by SAP for the Change Controller

SAP delivers the objects for the change controller that are described in this document.

Process-Controller-Relevant Objects

## Service Types

TOR_CHACO (asynchronous processing)

Service type that you can use for change strategies.

TOR_CHACOS (synchronous processing)

Service type that you can use for change strategies.

TOR_CREATE (asynchronous processing)

Service type that you can use for creation strategies.

TOR_CREA_S (synchronous processing)

Service type that you can use for creation strategies.

TOR_SAVE (asynchronous processing)

Service type that you can use for save strategies.

TOR_SAVE_S (synchronous processing)

Service type that you can use for save strategies.

This is custom documentation. For more information, please visit SAP Help Portal.

66


1/14/26, 2:46 PM

## TOR_DELETE

Service type that you have to use for deletion strategies.

  Note
Strategies of service types TOR_CHACO, TOR_CREATE, and TOR_SAVE are processed asynchronously in a separate

task, whereas strategies of service types TOR_CHACOS, TOR_CREA_S, and TOR_SAVE_S are processed synchronously.

If strategy processing is to trigger the execution of determinations and validations, use asynchronous strategies;

otherwise use synchronous strategies to optimize the overall performance.

The change strategies, create strategies, and save strategies mentioned below are only delivered for the service types

for asynchronous processing. For more information about synchronous and asynchronous processing, see SAP Note

1674629

.

Change Strategies

## CANCEL_FOR

Current tendering processes are stopped and the associated freight orders are canceled.

## DEF_CHACO

Default reaction to changes in location, date, or quantity:

## Location changes

Involved business documents are removed from the transportation plan.

## Date changes

A rescheduling is performed. In case of time conflicts, the freight orders are blocked for execution.

## Quantity changes

A capacity check is performed. In case of an overload, the freight orders are blocked for execution.

## NO_ACTION

No follow-up action is processed.

## REM_CANC

The business document is deleted from the transportation plan and the former follow-up documents are canceled

or deleted if no other predecessor documents exist for it.

## RESET_TORS

Current tendering processes are stopped and the business document is deleted from the transportation plan.

## START_TEND

Current tendering processes are stopped and automatically restarted.

## STOP_TEND

Current tendering processes are stopped.

Creation Strategies

## CARR_SEL

Carrier selection is performed for this business document based on the default carrier selection settings that you

indicated in the business document type in Customizing.

This is custom documentation. For more information, please visit SAP Help Portal.

67


1/14/26, 2:46 PM

## CHARG_TEND

Charge calculation is performed for this business document and an automatic tendering process is started.

## PUBL_CREA

The Published status is set for the air freight booking after you created it.

## TEND_START

An automatic tendering process is started.

Deletion Strategies

## CANCEL_CAP

Current tendering processes are stopped and the associated freight orders are canceled.

Save Strategies

## CALC_CHARG

Calculates charges at every save.

## SRO_DELETE

Deletes empty service orders when you save your freight order or freight booking.

## TOR_CANCEL

Cancels freight orders without requirements assigned to them.

Change Strategy Methods

## CANCELCAPA

Associated freight orders and freight bookings are canceled if no freight unit is assigned to them anymore.

## CANCEL_FOR

Associated freight orders and freight bookings are canceled.

## CHACOALERT

Alert is issued.

## CHECK_CAPA

Capacity check is done for all involved business documents.

## DEF_REACT

Default reaction to changes in location, date, or quantity:

## Location changes

Involved business documents are removed from the transportation plan.

## Date changes

A rescheduling is performed. In case of time conflicts, the freight orders are blocked for execution.

## Quantity changes

A capacity check is performed. In case of an overload, the freight orders are blocked for execution.

This is custom documentation. For more information, please visit SAP Help Portal.

68


1/14/26, 2:46 PM

## REBUILD_FU

Freight unit building is retriggered for the related transportation requests. This method is only relevant for

unplanned and unfixed freight units.

## REBUILDFUH

Freight unit building is retriggered for the related transportation requests.

## START_TEND

Current tendering processes are stopped and automatically restarted.

## STOP_TEND

Current tendering processes are stopped.

## TOR_DELAY

Involved business documents are determined if a delay has been reported.

## TOR_REM_PL

Involved business documents are removed from the transportation plan.

## UNFIX_TORU

Unfixes the business document to enable a change strategy to perform changes.

## REFIX_TORU

Refixes business documents for the change strategy.

## REDET_PO

Redetermines the purchasing organization.

Creation Strategy Methods

## CALC_CHARG

Calculates charges after creation of a business document.

## STARTATEND

Automatic start of tendering process.

## UNFIX_TORC

Unfixes the business document to enable a strategy for creation to perform changes

## CARR_SEL

Carrier selection is performed for this business document based on the default carrier selection settings that you

indicated in the business document type in Customizing.

## PUBL_CREA

The Published status is set for the air freight booking after you created it.

## REFIX_TORC

Refixes business documents for the creation strategy.

## Deletion Strategy Methods

This is custom documentation. For more information, please visit SAP Help Portal.

69


1/14/26, 2:46 PM

## CANCTORDEL

Associated freight orders and freight bookings are canceled.

Save Strategy Methods

## CALCCHARG

Calculates charges when saving a business document.

## UNFIX_TORS

Unfixes the business document to enable a save strategy to perform changes.

## TOR_CANCEL

Cancels freight orders without requirements assigned to them.

## REFIX_TORS

Refixes business documents for the save strategy.

## SRO_DELETE

Deletes empty service orders when you save your freight order or freight booking.

Condition-Relevant Objects

## Condition type /SCMTMS/CC_QUAN_TOL

Condition to dynamically determine quantity tolerances.

Condition type /SCMTMS/CC_DATE_TOL

Condition to dynamically determine date tolerances.

## Condition type /SCMTMS/CC_TOR_STRAT

Condition to dynamically determine the change controller strategy for reacting to a change.

## Condition type /SCMTMS/CC_TOR_STR_M

Condition to dynamically determine multiple change controller strategies for reacting to a change. Note that the strategies

returned by the system must be independent. The system does not take into account the sequence of the strategies.

Settings for the Change Controller

## Use

To use the change controller, you must make the Customizing settings described in this document.

## Features

## Process Controller Settings

If you do not want to use the strategies delivered by SAP, you must define your own strategies for the change controller, and assign

them the change controller service TOR_CHACO. You can then assign to the strategies either change controller methods delivered

This is custom documentation. For more information, please visit SAP Help Portal.

70


1/14/26, 2:46 PM

by SAP, or methods created by you. For more information, see Process Controller Configuration and Objects Delivered by SAP for

the Change Controller.

## Condition Settings

Define a data access and assign to it one of the condition types delivered by SAP for the change controller. For more information,

see Condition and Objects Delivered by SAP for the Change Controller.

## Business Document Settings

Specify the following change controller settings for the business document types in Customizing for Transportation Management:

Default change strategy

Strategy determination condition

Quantity tolerance determination condition

## Date tolerance determination condition

If you indicate a strategy determination condition, the system uses the change strategy found via the condition. If you do not

indicate a condition or if the condition does not return a strategy, the system automatically uses the default change strategy.

There are three other types of strategies:

Strategy for saving (service type TOR_SAVE)

This strategy is executed each time you save a business document.

Strategy for creation (service type TOR_CREATE)

This strategy is executed each time a business document is created (by you or the system).

Strategy for deletion (service type TOR_DELETE)

This strategy is executed each time a business document is deleted (by you or the system).

SAP delivers strategies that you can select. You can also define your own strategies.

For more information, see Customizing for Transportation Management under the following nodes:

Freight Order Management

## Freight Order

 Define Freight Order Types

Freight Order Management

## Freight Booking

 Define Freight Booking Types

Freight Order Management

## Transportation Unit

 Define Transportation Unit Types

Freight Order Management

## Service Order

 Define Service Order Types

Planning

## Freight Unit

 Define Freight Unit Types

Business Add-In (BAdI)

If you want to enhance the standard logic of the change controller for determining changes to business documents, you must

make the settings for the BAdI BAdI: Determination of Changes for Change Controller. For more information, see Customizing for

Transportation Management under  Business Add-Ins (BAdIs) for Transportation Management

 Basic Functions

## Change

Controller

.

This is custom documentation. For more information, please visit SAP Help Portal.

71


1/14/26, 2:46 PM

Process Controller Configuration

## Use

You use this process to configure the process controller. The process controller is a framework with which you can define your own

strategies and methods, and in doing so, the way in which your planning process is executed, for example:

## Strategies

You use strategies to define complete processes. By assigning a service, you define the area in which the process is to be

used, for example, transportation charge management, freight unit building, or VSR optimization.

We provide a number of standard strategies.

## Methods

Methods define the individual process steps of a strategy. You assign a service to each method.

Transportation Management uses the process controller to define the following strategies:

Planning strategies (see Planning Strategies)

External strategies (see External Strategies)

You use strategies in Transportation Management in the following areas, for example:

Freight unit building (see Creation and Editing of Freight Units)

Carrier selection (see Carrier Selection)

VSR optimization (see VSR Optimization)

Load optimization (see Load Planning)

Manual planning (see Manual Planning)

Change controller (see Change Controller)

Definition of customer-specific functions (see Customer-Specific Functions)

## Process

1. You define a service for the required area.

2. You define a strategy.

3. You define one or more methods.

4. You assign these methods to your strategy. The sequence in which you assign the methods to the strategy determines the

sequence in which the system processes the methods. Strategies and methods must have the same service. You can also

assign one method to multiple strategies.

  Note

You define strategies and methods in Customizing for Transportation Management under  Basic Functions

 Process

## Controller

. Choose the following Customizing activities:

Define Service

## Define Strategy

This is custom documentation. For more information, please visit SAP Help Portal.

72


1/14/26, 2:46 PM

## Define Methods

## Assign Methods to a Strategy

You can use the other Customizing activities under the Process Controller Customizing node to define parameters to

further adjust your strategy.

More Information

Process Controller

Planning Strategies

## Use

You use planning strategies to define the planning steps that the system is to perform and the sequence in which it is to perform

them. Each planning strategy comprises one or more methods that represent the individual planning steps.

## Features

We deliver multiple standard planning strategies with methods. You can change these by adding or replacing methods.

You define planning strategies and methods in Customizing. For more information about the process controller configuration, see

Process Controller Configuration.

## Activities

To use standard planning strategies, you have to specify them in the corresponding profiles and settings for the relevant area. For

manual planning, specify the standard planning strategies in the planning profile, for example (see Manual Planning). For carrier

selection, specify them in the carrier selection settings (see Carrier Selection). For load optimization, specify them in the load

planning settings (see Automatic Load Planning).

External Strategies

## Use

You can use external strategies to change the standard behavior of certain areas of your system in accordance with your

requirements.

In the external strategy, you define the steps that the system is to perform and the sequence in which it is to perform them. Each

external strategy comprises one or more methods that represent the individual steps.

## Features

You use external strategies, for example, for incompatibilities (see Incompatibilities) and in transportation charge management

(see Agreement).

You define external strategies in Customizing. For more information, see Process Controller Configuration.

This is custom documentation. For more information, please visit SAP Help Portal.

73


1/14/26, 2:46 PM

Process Controller

## Use

The process controller is a framework with which you can define your own strategies and methods and the way in which the

system executes specific processes. It allows you to define adaptive processes that make it possible for a user to exclude delivered

functionality or include new functionality.

In the process controller, you model a process as a strategy. A strategy defines how the system executes a specific service, for

example the determination of geocoordinates, to suit your business need.

  Example

You want to determine geocoordinates using a specific geocoding provider. You use the strategy GC_GIS1.

In the standard system, SAP delivers a number of different strategies that you can use for your various services. The strategy itself

is made up of a sequence of methods. The methods define the individual process steps of the strategy. You must assign a service

to the strategy as well as to the methods. Different strategies can employ the same method. To change the behavior of the

methods that the strategies use, you can define parameters for a method and then assign them to it. For example, you can use a

parameter to define the number of expected results for a request. You must implement the logic within the method using the

parameter.

  Caution

If you include a customer-specific method in a strategy, the method must comply with the standard interfaces of the process

controller methods.

You can use the process controller to define the following strategies, for example:

Geocoordinate determination strategies

Distance and duration determination strategies

Route determination strategies

## Prerequisites

In Customizing, you have made the following settings:

You have defined a service under Define Service.

You have defined a strategy under Define Strategy.

You have defined one or more methods under Define Methods.

You have assigned the methods to a strategy under Assign Methods to a Strategy.

  Note

The sequence in which you assign the methods to the strategy determines the sequence in which the system processes

the methods. Strategies and methods must have the same service. You can also assign one method to multiple

strategies.

To further adjust your strategy, you can define parameters under:

This is custom documentation. For more information, please visit SAP Help Portal.

74


1/14/26, 2:46 PM

## Define Parameters

Assign Parameters to a Method

Assign Method Parameters to a Strategy

  Note

The definition and usage of parameters is optional. If you change a standard strategy we recommend you set the value of a

delivered standard parameter in Assign Method Parameters to a Strategy. If you define a new parameter, you must implement

the usage logic within the using method.

## Activities

You can set up the process controller in Customizing for Transportation Management under  Basic Functions

 Process

Controller

, for example.

If you have set up a new strategy, you must define for which process you use the strategy.

Map Display

## Use

You can use this function to display business documents and resources, such as freight orders or trucks, on a geographical map.

## Prerequisites

In Customizing for Transportation Management under  Basic Functions

 Geographical Map

 Define Settings for

Geographical Map , you have activated the map display.

Optional: In Customizing for Transportation Management under  Basic Functions

 Geographical Map

## Define Layouts

for Geographical Map , you have defined the layout of the geographical map.

## Features

You can display the map in three different areas in the system:

In the transportation network cockpit, you can select master data that is then displayed graphically on the geographical

map.

In the document overviews for freight orders or forwarding orders, for example, you can display the details for a document

on the map. The transportation stop sequence for this business document is displayed on the map, and the transportation

stops are connected by arrows showing the direction. If you have not selected a business document, only the map is

displayed. Note that although you can select multiple documents at the same time the system displays only the details of

the first hit it finds.

In the transportation cockpit, you can use this function to display planning-relevant business documents and resources. For

more information about the various ways of displaying documents and resources on the map, see Interactive Planning on

the Map (link is available below).

In addition to the standard navigation functions on the map, such as move, zoom in, and zoom out, you have the following

navigation functions:

This is custom documentation. For more information, please visit SAP Help Portal.

75


1/14/26, 2:46 PM

Function

and

and

## Description

## Expand and collapse navigation bar

Navigate forward and backwards to next/previous map view

This is the selection mode for business documents and resources.

You can select objects either as single objects, with a rectangle, or

with a lasso.

Rectangular zoom: You use this function to draw a rectangle around

the area that you want to zoom into.

This function moves the focus of the map to the displayed planning

objects. For example, if your objects are all in North America but

Europe is shown on the map you can choose this pushbutton to

move the map view to North America.

You have the following options for the planning objects:

To display a tooltip, move the mouse over an object

To display an object-specific context menu, right-click the object

To select the object for further processing, left-click the object

## To display more information about the object, double-click it

In the Customizing activity Define Layouts for Geographical Map you can configure which information is to be displayed.

More Information

## Map Functions

Interactive Planning on the Map

Map Functions

## Use

You can perform various actions on the map.

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

This is custom documentation. For more information, please visit SAP Help Portal.

76


1/14/26, 2:46 PM

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

## Address Search

Available in: transportation network cockpit, document overview, transportation cockpit

You can use the context menu of the map to start the address search and display the search results on the map. The address

search is based on the geocoding of the location. For more information, see Geocoding.

This allows you to perform several address searches and display the search results simultaneously on the map. You can use the

context menu of the map to hide the search results individually or completely.

## Route Display

Available in: transportation network cockpit, document overview, transportation cockpit

You can use the context menu of a connection line to determine a route display along real street routes (georoutes). This function

is dependent on the geographical information system available in the system.

Alternatively, you can use the context menu of a resource to display the connection lines of all freight orders assigned to this

resource.

## Dynamic Adjustment

Available in: transportation network cockpit, document overview, transportation cockpit

You can adjust the map display to meet your individual needs by selecting the option Show Display Profile from the context menu

for the map. For example, you can specify whether map objects are to be shown or hidden, whether you want to display the

descriptions, and whether you want to allow clustering for overlapping nodes.

Create Location and Transportation Zone

## Available in: transportation network cockpit

You can use the context menu for the map to create locations and transportation zones directly on the map. The locations or

transportation zones are created where you open the context menu. However, you cannot use the context menu to change the

This is custom documentation. For more information, please visit SAP Help Portal.

77


1/14/26, 2:46 PM

positioning of an object on the map.

## Proximity Search

## Available in: transportation network cockpit, transportation cockpit

You can use the context menu of the map to find resources as well as unplanned freight units or transportation units that are close

to a particular point on the map.

## Resource Item

## Available in: transportation cockpit

You can use the context menu of the map to specify the exact location of a resource at any time.

Differentiate Between Business Documents Using Colors

## Available in: transportation cockpit

You can use the context menu of the map to display different colors for multiple business documents selected simultaneously. This

enables you to better differentiate between the documents. The color of each respective document is displayed in the Color

column in the document list.

  Note

The Color column is hidden in the standard system.

More Information

## Map Display

Interactive Planning on the Map

## Scenario Builder

The scenario builder lets you quickly create data for testing, demos and training. Note, that creating scenarios is only enabled for

non-productive systems. The function cannot be used for master data setup in a productive system.

This is custom documentation. For more information, please visit SAP Help Portal.

78


1/14/26, 2:46 PM

## This video is in English. Open this video in a new window

With the scenario builder, administrators can create scenario templates that include all the scenario data (system objects and

Customizing data) required for running a scenario in Transportation Management. Testers, for example, can then browse the

scenario templates and use them to quickly create their own copy of the scenario data in the system.

## More Information

For more information about administrator-related tasks, see the following:

Creating a Scenario Template

## User Authorizations

Download and Upload Functions

## Depersonalization of Data

For more information about using the scenario builder to create scenario data in the system, see Using a Scenario Template and

Create Entities.

For more information about the use of personal prefixes with the scenario builder, see Personal Prefixes.

## Creating a Scenario Template

Creating a scenario template involves preparing the scenario data, adding a new scenario template to the scenario builder, and

then adding the scenario data to the scenario template.

## Prerequisites

You have authorization to create scenario templates in the scenario builder. For more information, see User Authorizations.

## Procedure

You have several possibilities to create a scenario template. You can copy an existing scenario template, create a scenario template

based on system data or create one from scratch by using the download and upload function. You then create a scenario templates

outside TM using a spreadsheet.

## Creating a Scenario Template Based on System Data

If you want to use data that already exists in the system for your new scenario template, you can proceed as follows:

1. In Transportation Management (TM), create and prepare the scenario data (system objects and Customizing data) that you

want to add to a scenario template. Proceed as follows:

If you want to work with personal prefixes, mark Use Personal Prefixes. For each system object that you want to add,

include your three-character personal prefix in its name. For more information, see Personal Prefixes.

If you want to add Customizing data to a scenario template, add the Customizing data to a Business Configuration

(BC) set. For more information, see Business Configuration Sets (BC-CUS).

This is custom documentation. For more information, please visit SAP Help Portal.

79


1/14/26, 2:46 PM

2. On the launchpad, open the Scenario Builder app and add a new scenario template.

3. Add the prepared scenario data to the scenario template. You have the following options:

If you add a BC set or forwarding order, for example, then in the displayed dialog box, enter the personal prefix used

in the BC set or forwarding order. For more information, see Personal Prefixes.

If users of the scenario template must select system objects or specifiy settings in the system because they are not

included in the scenario template, enter a comment on the Info tab.

The scenario template can now be used by testers, for example, to create their own copy of the scenario data in TM.

## Creating a Scenario Template from Scratch

If you don't want to use existing system data as a basis for your scenario template, but want to create the scenario template from

scratch using a spreadsheet, you can proceed as follows:

1. 1. Create a scenario template: On the launchpad, open the Scenario Builder app and add a new scenario template.

2. In the New Scenario Template dialog box, enter a name and description for your template and, if required, select the

Sample Data checkbox. You have the following options:

If you select this checkbox, the system creates sample data for your scenario template. When you download the

template in the next step, the system enters this sample data in the spreadsheet files that have been created

automatically. The sample data shows the data format that is used in the scenario builder.

If you don't select the checkbox, the system doesn't create any sample data for your scenario template. It creates

empty spreadsheet files that you can fill with your own data.

3. Download your scenario template.

The downloaded contains spreadsheet files for all supported objects. For more information, see Download and Upload

Functions.

4. Add or change the data in the spreadsheet files that the system has created automatically. The column titles already

contain information about the number of characters that you are allowed to enter (for example, 20 characters for the

location ID).

5. Upload the modified scenario template into the scenario builder.

You can now use the scenario template to create your scenario data in TM.

Related Information

Using a Scenario Template

Create Entities

## User Authorizations

Use the authorization object T_SB to specify which actions a user can perform with the scenario builder.

You can allow or prevent users from completing the following actions:

Creating and uploading a scenario template.

Displaying a scenario template.

This is custom documentation. For more information, please visit SAP Help Portal.

80


1/14/26, 2:46 PM

Editing a scenario template.

Deleting a scenario template.

Creating scenario data in the system using a scenario template.

For more information about authorizations, see Authorizations.

## Depersonalization of Data

The scenario builder might process data (personal data) that is subject to the data protection laws applicable in specific countries

or regions. This is especially true if you are using data in the scenario builder from your productive system. Therefore, you can use

the following BAdI to depersonalize data before using it in the scenario builder.

BAdI:/SCMTMS/SB_ADD_TEMPLATE_DATA.

Method contained in BAdI:CHECK_AND_ADJUST_DATA.

The method enables you to process the data that you have selected to use in the scenario builder. In this method, you must

anonymize any personal data.

To see an example implementation of how you can access the data in the BAdI, see /SCMTMS/SB_ADD_TEMPL_DATA_SMPL.

For more information, see Blocking and Deletion of Personal Data in TM.

## Download and Upload Functions

The download and upload functions in the scenario builder enable you to download and upload scenario templates as .zip files.

## Downloading a Scenario Template

If a system object that you want to include in the scenario template is unavailable to select in the system or if you want to create a

scenario template from scratch without using existing system data, you can download the template and manually enter the

object's details in the relevant spreadsheet file in the .zip file.

If you select the Sample Data checkbox in the New Scenario Template dialog box when creating a scenario template, the

downloaded spreadsheet file already contains sample data that shows the data format that is used in the scenario builder. The

column titles contain information about the number of characters that you are allowed to enter (for example, 20 characters for the

location ID).

You can also use the download function to share a scenario template with colleagues.

## Uploading a Scenario Template

After editing the spreadsheet files of the scenario template or after receiving a scenario template, you can use the upload function

to add the template available to the scenario builder.

## Using a Scenario Template

This is custom documentation. For more information, please visit SAP Help Portal.

81


1/14/26, 2:46 PM

Scenario Templates are used to create test data in Transportation Management (TM). You can create data based on a complete

scenario or based on single objects from a scenario template. When testing, for example, you can use the relevant scenario

template to quickly create your own copy of the scenario data (system objects and Customizing data) in TM.

## Prerequisites

You have authorization to browse and use scenario templates. For more information, see User Authorizations.

The data of your scenario template is consistent. For more information, see Consistency Check for Scenario Template.

## Procedure

You can create test data for all objects in a scenario template, or create data based on selected objects. For more information

about creating test data for selected objects, see Create Entities.

To create test data for all objects in a scenario template, proceed as follows:

1. On the launchpad, open the Scenario Builder app.

2. Choose the scenario template that contains the scenario data that you require.

3. Create the scenario. In the Create Scenario popup, you have the following options:

You can update time-dependent data while creating the scenario. For more information, see Update Dates While

Creating Scenarios or Entities.

If the use of personal prefixes is set for the scenario template, enter a personal three-character prefix. For more

information, see Personal Prefixes.

When the scenario builder creates the scenario data in the system, it includes your personal prefix in the system object

names and Customizing data.

4. After the scenario data is created in TM, you can select the objects and Customizing data on the relevant selection screens.

## Create Entities

Instead of creating test data for Transportation Management (TM) based on all objects in a scenario template, you can also create

test data based on particular objects.

Creating test data based on selected objects is especially useful if you want to create transactional data, such as purchase orders,

scheduling agreements, or forwarding orders. In addition, you can create entities if you only need certain data from a scenario

template, for example you only need locations.

You have, for example, a scenario template that contains locations, purchase orders and scheduling agreements. With Create

Entities you can, for example, create only purchase orders or only locations, based on the selected objects in the scenario

template.

## Prerequisites

You have authorization to create scenario templates in the scenario builder. For more information, see User Authorizations.

The data of the objects you want to copy are consistent. For more information, see Consistency Check for Scenario Template.

## Procedure

This is custom documentation. For more information, please visit SAP Help Portal.

82


1/14/26, 2:46 PM

To create entities for selected objects of a scenario template, proceed as follows:

1. In the Scenario Builder app, open a scenario template, and on the Materials Management tabe page choose an object type,

for example, purchase orders or scheduling agreements.

2. To create test data, mark one or more objects, and choose Create Entities.

In the displayed popup, you have the following options:

If the use of personal prefixes is set for the scenario template, you can enter a personal three-character prefix. For

more information, see Personal Prefixes.

You can define how many copies you want to create.

You can update time-dependent data while creating the test data. For more information, see Update Dates While

Creating Scenarios or Entities.

The system creates test data based on the selected objects, for example purchase orders or scheduling agreements. If the

documents are TM-relevant, the system also creates freight units for these documents.

3. Finding the test data: After the data is created in TM, you can select the objects on the relevant selection screens in the

system.

For more information about creating test data for all objects in the scenario template (entire scenario), see Using a Scenario
Template.

## Consistency Check for Scenario Template

Check to verify if the test data of your scenario template is consistent.

## Use

With the consistency check you can verify if the test data of your scenario template is consistent.

The system checks if all objects that are referenced by other objects in the scenario template exist in the template. Typical

examples for dependencies to other objects: A transportation zone that is defined as a group of locations, or a forwarding order

that references a product.

To be able to create a scenario for a scenario template, the test data must be consistent. The systems runs the consistency check

when you upload a scenario template, or on demand in the Scenario Builder app.

After the check is performed, a success message or a list of warnings for missing objects is displayed. In some cases, the system

creates a scenario for the scenario template despite warnings for referenced objects that could not be found in the template.

## Example

There are referenced objects in your scenario template, for example, a transportation zone contains references to locations. Some

referenced objects (here locations) are not part of the template, but they exist in the system. In this case, the system creates the

transportation zone though the consistency check for the scenario template reports warning messages for the missing objects.

## Personal Prefixes

Personal prefixes enable the users of a scenario template to create the scenario data in Transportation Management with their

initials or ID. And because each user of the template has their own copy of the scenario data, multiple users can simultaneously

This is custom documentation. For more information, please visit SAP Help Portal.

83


1/14/26, 2:46 PM

use the same data. When the scenario builder creates the scenario data in the system, it includes your personal prefix in the

system object names and Customizing data.

The usage of personal prefixes is optional. For more information, see Creating a Scenario Template.

The diagram below explains the role of personal prefixes in more detail.

## Update Dates While Creating Scenarios or Entities

Time-dependent data can be updated while creating scenarios or entities in the scenario builder.

These updates are relevant for scenario templates containing time-dependent data like dates in forwarding orders, validity of

default routes, or validity of transportation lanes. Even if the dates of a scenario template do not fit your purpose, you can create a

scenario on the basis of that scenario template, and, for certain objects, you can let the system update the dates of the test data

with your preferred dates.

You can have updated dates, without any manual effort for adjusting the dates in the scenario template, no matter if they occur in

the future or the past.

## Example

The validity dates of the transportation lane and the forwarding order in your scenario template are expired and you want to create

up-to-date test data.

You select Update Dates when creating a new scenario and enter a reference date. The reference date is used to calculate the days

for the date shift. The system takes the earliest date used in the template and calculates the difference to the reference date.

This is custom documentation. For more information, please visit SAP Help Portal.

84


1/14/26, 2:46 PM

For more information about creating a new scenario, see Using a Scenario Template. For more information about creating data

from selected objects, see Create Entities.

## Example

Your scenario template uses the following data:

Transportation lane: valid from 1.1. – 30.06.

Forwarding order: pick-up date: 20.1., delivery date: 21.1.

Entered reference date: 10.1.

The system takes the earliest date used in the template (in this example 1.1.) and calculates the difference to the reference date. In

this example the dates need to be shifted shift by 9 days.

The updated dates are:

Transportation lane valid from 10.1. – 09.7.

Forwarding order: pick-up date: 29.1., delivery date: 30.1.

Background Processing

## Use

Background processing enables you to use functions to perform mass processing tasks and background jobs. A mass processing

function enables you to work flexibly with a large number of business documents, with immediate results. A background job

function enables you to run a program in the background at a specific time or at the occurrence of a specific regular event.

The table explains how background processing functions are used:

Function

## Use

## Program

Forwarding Order Management Preparation

This function automates steps to

/SCMTMS/TRQ_PREP_PLNG_BATCH

create freight units and define the

route based on forwarding orders.

Creation of Package Units Based on Unified Package

This function starts creation of

/SCMTMS/PLN_PB_FU_BGD

Building for Freight Units

package units based on unified

package building for freight units.

Unified Package Building

This function starts unified package

/SCMTMS/PLN_PKG_BUILDING_BGD

building.

Creation or Cancellation of Package Units for Road

This function starts creation of

/SCMTMS/PLN_CRT_PB_PU_BGD

Freight Orders

## Planning Run

package units for road freight orders.

This function starts a planning run.

/SCMTMS/PLN_OPT

Determination of Distances and Durations Based on

This function starts distance and

/SCMTMS/PLN_DDD

## Selected Documents

duration determination based on

selected documents.

This is custom documentation. For more information, please visit SAP Help Portal.

85


1/14/26, 2:46 PM

Function

## Use

## Program

Creation of Capacity Documents Based on

This function starts creation of

/SCMTMS/PLN_REQ_STAGE_GROUP

Requirement Groups

capacity documents based on

requirement groups.

## Load Planning Run

This function starts a load planning

/SCMTMS/PLN_LOAD_PLANNING_BGD

run.

Load Consolidation Run

This function starts a load

/SCMTMS/PLN_LOADCONS

consolidation run.

## Selection of Carriers

This function automates the carrier,

/SCMTMS/TSPS_OPT_BGD

which can also include the trigger of

the tendering process.

## Tendering

This function triggers the tendering

/SCMTMS/TOR_TENDERING_BATCH

process independent of carrier

selection.

Creation of Schedule-Based Freight Documents

This function creates freight

/SCMTMS/SCH_CRT_DOC

documents based on the departures

of one or more schedules.

Offline Workflow for Sending and Approving Work

These functions send work items for

/SCMTMS/WI_NOTIFICATION_OFFAPP

## Items

freight agreement RFQ masters,

agreements, and validity periods in

rate tables by e-mail to users for

offline approval, and process inbound

work item e-mails.

/SCMTMS/WI_OFFLINE_EVAL_REPORT

Processing of FQs and Overdue RFQs

This function evaluates freight

/SCMTMS/TEND_CONT_PROCESS

quotations and detects that the

maximum response time for a

request for quotation (RFQ) is over.

Confirmation of Forwarding Orders

This function automates steps to

/SCMTMS/TRQ_CONF_BATCH

confirm forwarding orders.

Creation of Deliveries in SAP ERP

This function creates delivery

/SCMTMS/DLV_BATCH

proposals for order-based

transportation requirements.

Processing of FUs for Direct Shipment

This function converts freight units

/SCMTMS/DIRECT_SHIPMENT_BATCH

for which the system has determined

direct shipment options into freight

orders for direct shipment or assigns

them to freight orders.

Posting Goods Issue from TM

This function posts goods issue for

/SCMTMS/POST_GI_BATCH

SAP ERP outbound deliveries from

SAP TM.

Uploading of Allocations

This function enables you to upload

/SCMTMS/TAL_IMPORT

allocations from an external data

source to your TM system.

Processing of Freight Bookings

This function automates actions for

/SCMTMS/TOR_BO_PROC_BATCH

freight bookings.

This is custom documentation. For more information, please visit SAP Help Portal.

86


1/14/26, 2:46 PM

Function

## Use

## Program

Processing of Freight Orders

This function automates actions for

/SCMTMS/TOR_FO_PROC_BATCH

freight orders.

Calculation of Profitability

This function automates the

/SCMTMS/CALC_PROFITABILITY

calculation of profitability in

forwarding orders.

Communication of Settlements with SAP ERP

This function processes actions for

## RSPPFPROCESS

communication with SAP ERP.

Creation and Transfer of Forwarding Settlement

This function automates the creation

/SCMTMS/CFIR_CREATE_BATCH

## Documents

and transfer of forwarding

settlement documents.

/SCMTMS/CFIR_TRANSFER_BATCH

Publication of Freight Settlement Dispute Cases

This function enables you to publish

/SCMTMS/SET_CARRIER_RELEVANCE

freight settlement dispute cases in

batches in the background.

Posting of Carrier Invoices

This function enables you to post the

/SCMTMS/CAR_INV_POST_BATCH

carrier invoices that are ready for

posting in TM to materials

management (MM) as an incoming

invoice in the background.

Confirming the Resolution of Freight Settlement

This function enables you to confirm

/SCMTMS/SET_CARRIER_RELEVANCE

## Dispute Cases

the resolution status of freight

settlement dispute cases in batches

in the background.

Updating of Credit Exposure

This function enables you to update

/SCMTMS/CLC_EXPOSURE_UPDATE

the credit exposure for a business

partner in SAP Credit Management

from TM.

Creation and Transfer of Freight Settlement

This function automates the creation

/SCMTMS/SFIR_CREATE_BATCH

Documents using Integration with MM External

and transfer of freight settlement

## Services Management

documents using integration with

MM external services management.

/SCMTMS/SFIR_TRANSFER_BATCH

Creation and Transfer of Freight Settlement

This function automates the creation

/SCMTMS/SFIR_CREATE_BATCH

Documents using Integration with Lean Services

and transfer of freight settlement

documents using integration with

lean services.

/SCMTMS/SFIR_TRANSFER_BATCH

Display Agreements with Issues in Charge Types

This function enables you to

/SCMTMS/GET_EXTCHK_AGR_BO_DOC

automate the display of agreements

that have the issues in its charge

types.

You can also schedule several background jobs in a row. For more information, see Scheduling of Background Jobs.

  Note

By using a parallel processing profile, you can improve the performance of background processing. To define parallel processing

profiles, on the SAP Easy Access screen chooses  Logistics

 Transportation Management

 Current Settings

## Define

Parallel Processing Profile .

This is custom documentation. For more information, please visit SAP Help Portal.

87


1/14/26, 2:46 PM

For more information, see Definition of Parallel Processing Profiles.

## Activities

You can use a program in the following ways:

## To run a mass processing function

For example, you can process a large number of inbound tendering e-mails at the same time with an immediate result.

You can use different criteria to process objects. For example, you can process freight orders by document ID, shipper, or

consignee. You can also specify variants, to make it easier to enter the selection criteria that you use regularly.

To use these functions, on the SAP Easy Access screen, choose  Logistics

 Transportation Management

## Administration

 Background Processing .

## To create a background job using the Define Background Job (SM36) transaction

For example, you can specify that the system creates forwarding settlement documents at certain times during the working

day.

To run the transaction, enter the program name and the appropriate variant on the Create Step screen. Enter the start

criteria on the Job Selection screen.

## Scheduling of Background Jobs

You can schedule several background jobs in a row.

## Use

You indicate the individual background jobs that the system is to run and the sequence in which they are to run.

## Activities

1. On the SAP Easy Access screen, choose  Logistics

 Transportation Management

 Administration

 Background

## Processing

 Schedule Background Jobs .

2. Define a job name prefix for the overall job. Indicate the individual background jobs and specify the sequence in which you

want the system to run them. By selecting an individual background job, you include it in the run.

You can also indicate that the system is to cancel the run after one of the background jobs fails.

3. Execute the program.

If you execute the program directly, a second screen is displayed with an overview of the scheduled background jobs. You

can refresh the status to see, which jobs have been processed.

If you execute the program in the background, you can find details in transaction SM37.

Forwarding Order Management Preparation

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

88


1/14/26, 2:46 PM

This function automates steps to create freight units and to determine the route on the basis of forwarding orders. You can use this

function instead of executing the steps manually in the apps for your personal object worklist (POWL) from the launchpad. You can

use background processing if you want to process many forwarding orders simultaneously.

## Integration

For more information about the integration of this function into the overall background processing, see Background Processing.

## Prerequisites

You have created forwarding orders in the system.

You have optionally defined a selection profile. For more information see Selection Profile.

You have optionally defined a planning profile. For more information, see Planning Profile.

You have defined a freight unit building rule. For more information, see Freight Unit Building Rule.

We recommend that you define automatic freight unit building in Customizing for Transportation Management. For more

information, see  Forwarding Order Management

## Forwarding Order

 Define Forwarding Order Types .

## Features

This function executes the following activities:

## Creating freight units

For more information, see Creation and Editing of Freight Units.

## Determining the route

For more information, see Generation of Transportation Proposals.

## Activities

To use this function, you must run program /SCMTMS/TRQ_PREP_PLNG_BATCH.

Proceed as follows:

Select a selection profile or manually enter the selection criteria

Choose one of the following options:

Create Freight Units Only

## Define Route

You also have the following options:

Select a freight unit building rule

## Fix freight units

Define whether the forwarding order is processed in parallel (transaction /SCMTMS/PPRF)

Select a planning profile (only required for the option Define Route)

The system considers only those forwarding orders that have not yet been completed or canceled.

This is custom documentation. For more information, please visit SAP Help Portal.

89


1/14/26, 2:46 PM

The system selects the forwarding order items on the basis of the selection profile. The system performs the selected option for

the corresponding forwarding orders and saves the results. The system logs all messages that it creates when executing the

function in the application log under object /SCMTMS/TMS and subobject BP.

You can call the application log from the SAP Easy Access screen by choosing  Logistics

 Transportation Management

## Administration

 Display Application Log Entries .

Creation of Package Units Based on Unified Package Building for
Freight Units

## Use

You can use this function to start creation of package units based on unified package building for freight units in the background

instead of starting it in the transportation cockpit. You can start the function in simultaneous parallel sessions only if you have

indicated a parallel processing profile in your planning profile.

## Integration

For more information about the integration of this function into overall background processing, see Background Processing.

## Prerequisites

You have created a selection profile for freight units, which determines the input for unified package building.

You have created a planning profile. In your planning profile, you have indicated the following:

A default package unit type (in which you have defined Sequence Type of Stages as Linear with Distribution) and

optionally defined a default package unit creation rule.

Additionally, you can indicate a package unit type for package units with one destination location (in which you have

defined Sequence Type of Stages as Defined and Linear and Assignment of Predecessor Documents as

Completely) and optionally defined a corresponding package unit creation rule.

You have defined a unified package building profile and assigned it to your planning profile.

If you want to start this function in simultaneous parallel sessions, you have indicated a parallel processing profile in your

planning profile (under  Parallel Processing Profiles

 Unified Package Building ).

  Note

Since each parallel process calls the unified package building function separately, make sure that the maximum number

of parallel processes in your parallel processing profile is smaller than the number of slots that are available for unified

package building (load space optimization).

## Features

This function first builds packages for freight units according to the settings that you have made in your unified package building

profile. After that, the system creates package units for these packages. Note that the system only creates package units for

freight units for which you have selected Exclusive Package for Customer. That means, these package units contain products for

one specific customer only.

## Activities

This is custom documentation. For more information, please visit SAP Help Portal.

90


1/14/26, 2:46 PM

To use this function, you must run program /SCMTMS/PLN_PB_FU_BGD. You must specify the following:

## A planning profile

## A freight unit selection profile

Based on the chosen profiles, the system selects freight units. The system calls the unified package building function and builds

packages according to the unified package building profile. After that, it creates package units for these packages. The system logs

all messages that it issues when executing the function in the application log under object /SCMTMS/TMS and subobject PLN.

## Related Information

Use of Package Units in Planning

Unified Package Building

## Use

You can use this function to start unified package building in the background instead of starting it in the transportation cockpit. You

can start the function in simultaneous parallel sessions only if you have indicated a parallel processing profile in your planning

profile.

## Integration

For more information about the integration of this function into overall background processing, see Background Processing.

## Prerequisites

You have created selection profiles for road freight orders and transportation units, which determine the input for unified

package building.

You have defined a unified package building profile and assigned it to your planning profile.

If you want to start this function in simultaneous parallel sessions, you have indicated a parallel processing profile in your

planning profile.

  Note

Since each parallel process calls the unified package building function separately, make sure that the maximum number

of parallel processes in your parallel processing profile is smaller than the number of slots that are available for unified

package building (load space optimization).

## Features

This function starts unified package building and builds packages according to the settings that you have made in your unified

package building profile.

## Activities

To use this function, you must run program /SCMTMS/PLN_PKG_BUILDING_BGD. You must specify the following:

## Planning profile

This is custom documentation. For more information, please visit SAP Help Portal.

91


1/14/26, 2:46 PM

## Selection profiles

Based on the chosen profiles, the system selects road freight orders and transportation units. The system calls the unified package

building function and builds packages according to the unified package building profile. The system logs all messages that it issues

when executing the function in the application log under object /SCMTMS/TMS and subobject PLN.

  Note

This function is only available for unified package building based on capacity documents. Capacity-document-based unified

package building is only supported for road freight orders, trailer units, container units, and package units.

Creation or Cancellation of Package Units for Road Freight
Orders

## Use

You can use this function to start creation or cancellation of package units for road freight orders in the background instead of

starting it in the transportation cockpit.

## Integration

For more information about the integration of this function into overall background processing, see Background Processing.

## Prerequisites

You have created a selection profile for road freight orders.

For more information about further prerequisites, see Use of Package Units in Planning.

## Features

This function creates package units for road freight orders.

## Activities

To use this function, you must run program /SCMTMS/PLN_CRT_PB_PU_BGD. You must specify the following:

## A freight order selection profile

## Whether the system is to create package units or cancel package units and merge

Based on your selection, the system selects road freight orders and creates package units for the corresponding local package

items or it cancels the package units and re-creates the local package items. The system logs all messages that it issues when

executing the function in the application log under object /SCMTMS/TMS and subobject PLN.

## Related Information

## Use of Package Units in Planning

This is custom documentation. For more information, please visit SAP Help Portal.

92


1/14/26, 2:46 PM

Planning Run

## Use

This function starts a planning run. You can use this function instead of starting the Vehicle Scheduling and Routing optimizer (VSR

optimizer) from the transportation cockpit. You can start this function in simultaneous parallel sessions only if you have indicated a

parallel processing profile in your planning profile. We recommend that you use background processing if you want to process

business documents simultaneously.

## Integration

For more information about the integration of this function into overall background processing, see Background Processing.

## Prerequisites

You have created selection profiles and planning profiles, which determine the input for the VSR optimizer. For more information,

see Selection Profile and Planning Profile.

## Features

This function starts the planning process according to the planning strategy for the VSR optimizer that you maintained in the

optimizer settings. For more information, see Planning Profile.

## Activities

To use this function, you must run program /SCMTMS/PLN_OPT. You must specify the following settings:

Selection profiles

## Planning profile

Checkbox to indicate whether the run is a simulation run. This selection prevents the result of the planning run from being

saved.

Checkbox to indicate whether context determination for resources and documents is to be used.

Checkbox to indicate whether context determination for default drivers and truck drivers is to be used.

Based on the chosen profiles, the system selects freight units and resources. The system calls the VSR optimizer according to the

planning strategy. The system logs all messages that it issues when executing the function in the application log under object

/SCMTMS/TMS. If you run the function in the background, the system uses the subobject BP for logging. If you run the function

manually, the system logs the messages under subobjects according to the business object that created the message.

Related Information

## Context Determination

Context Determination in VSR Optimization

Creation of Capacity Documents Based on Requirement Groups

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

93


1/14/26, 2:46 PM

You can use this function to create capacity documents based on requirement groups. You can use this function instead of creating

capacity documents manually in the transportation cockpit.

You can start this function in simultaneous parallel sessions only if you have indicated a parallel processing profile.

## Integration

For more information about the integration of this function into overall background processing, see Background Processing.

## Prerequisites

You have created selection profiles for your freight units and transportation units, which determine the input for the

creation of capacity documents.

You have created a requirement grouping profile per capacity document category.

You have assigned your requirement grouping profiles to your planning profile in the capacity document creation settings.

Optionally, you have created a parallel processing profile.

For more information about further prerequisites, see Creation of Capacity Documents Based on Requirement Groups.

## Features

This function starts the creation of capacity documents based on your settings.

## Activities

To use this function, you must run program /SCMTMS/PLN_REQ_STAGE_GROUP. You must specify the following:

## Selection profiles

If you select several selection profiles, the system creates groups for each of them separately. Freight units and package

units are grouped together.

## Planning profile

Capacity document category, such as road freight order.

## Parallel processing profile

## Whether the system is to save the results

Based on the chosen profiles, the system selects requirement documents and groups them based on a requirement grouping

profile. For each of these groups, it creates a capacity document.

## Related Information

Creation of Capacity Documents Based on Requirement Groups

Load Planning Run

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

94


1/14/26, 2:46 PM

You can use this function to start an automatic load planning run instead of starting the optimizer for load planning and load

consolidation from the transportation cockpit. You can start the function in simultaneous parallel sessions only if you have

indicated a parallel processing profile in your planning profile.

## Integration

For more information about the integration of this function into overall background processing, see Background Processing.

## Prerequisites

You have created selection profiles, which determine the input for the optimizer for load planning and load consolidation

(for the selection of road freight orders, trailer units, and container units).

You have defined load planning settings, which determine specific rules for your optimizer run.

If you want to start this function in simultaneous parallel sessions, you have indicated a parallel processing profile in your

load planning settings.

  Note

Since each parallel process calls the optimizer for load planning and load consolidation separately, make sure that the

maximum number of parallel processes in your parallelization profiles is smaller than the number of slots that are

available for your optimizer for load planning and load consolidation in general.

## Features

This function starts the planning process according to the load planning strategy for the optimizer for load planning and load

consolidation that you defined in the load planning settings.

## Activities

To use this function, you must run program /SCMTMS/PLN_LOAD_PLANNING_BGD. You must specify the following settings:

Selection profiles

## Load planning settings

Based on the chosen profiles and settings, the system selects road freight orders, trailer units, and container units. The system

calls the optimizer for load planning and load consolidation according to the load planning strategy. The system logs all messages

that it issues when executing the function in the application log under object /SCMTMS/TMS and subobject PLN.

## Load Consolidation Run

You can use this function to start an automatic load consolidation run in the background instead of starting it from the

transportation cockpit.

## Integration

For more information about the integration of this function into overall background processing, see Background Processing.

## Prerequisites

This is custom documentation. For more information, please visit SAP Help Portal.

95


1/14/26, 2:46 PM

You have created a selection profile for the selection of freight units.

You have created a planning profile that includes capacity selection settings for the selection of resources, that is, trucks,

trailers, and containers.

## Features

This function starts load consolidation and plans the resources, for example containers, trying to keep their number at a minimum.

## Activities

To use this function, you must run program /SCMTMS/PLN_LOAD_CONS_BGD. You must specify the following settings:

Freight unit selection profile

## Planning profile

Based on the chosen profiles, the system selects freight units and resources. The system performs load consolidation. The system

logs all messages that it issues when executing the function in the application log under object /SCMTMS/TMS and subobject PLN.

Determine NLQs Based on Documents

## Use

You can use this function to determine a value for the normalized load consumption quantity (normalized quantity, NLQ) per

product and unit of measure (UoM) based on historical consolidation data. This value indicates how much space (footprint) a

single product consumes in a top-level package (that is, the outer packaging).

## Integration

For more information about the integration of this function into overall background processing, see Background Processing.

## Prerequisites

Road freight orders with NLQs exist in the system.

You have created a selection profile.

## Features

You need to specify the following:

## A selection profile

A weighting factor for real data

A maximum tolerance for outliers

## A threshold for saving the newly calculated NLQs

Further, you can indicate whether you want to run the function in test mode. In this case, the system calculates NLQs but doesn't

save data.

This is custom documentation. For more information, please visit SAP Help Portal.

96


1/14/26, 2:46 PM

The system calculates the NLQs for the products of the selected road freight orders. Afterwards, it saves the new NLQs in the

Normalized Quantity field of the Define Normalized Quantity app. If this app already contains entries for combinations of product

number and UoM for the normalized quantity, these entries are overwritten.

## Activities

To use this function, you must run program /SCMTMS/PLN_CALCNLQ.

## Related Information

NLQ Determination Based on Documents

Check NLQs and Cancel Documents

## Use

You can use this function to check whether the normalized load consumption quantities (normalized quantities, NLQs) in your

business documents are up to date and, if not, cancel these business documents. For example, you can schedule it to run

automatically after a new NLQ determination based on randomized data.

## Integration

For more information about the integration of this function into overall background processing, see Background Processing.

## Prerequisites

Business documents must exist.

## Features

This function first checks whether the normalized quantities in your business documents are up to date and, if not, cancels these

business documents.

## Activities

To use this function, you must run program /SCMTMS/PLN_CHECKNLQ. You must specify the following:

A document category (that is, road freight orders, container units, trailer units, package units, consignment orders, or

freight units)

One or several business documents using a selection profile and additional selection criteria, such as the document ID or

the document type

Further, you can indicate a threshold for canceling business documents. By doing so, you can prevent cancellation of business

documents in case of insignificant NLQ changes. You can also indicate whether you want to run the function in test mode. In this

case, the system doesn't cancel business documents and doesn't save data. In test mode, you can indicate that documents with

empty NLQs are to be determined and displayed.

## Related Information

This is custom documentation. For more information, please visit SAP Help Portal.

97


1/14/26, 2:46 PM

Check Normalized Quantities in Business Documents

Selection of Carriers

## Use

This function automates carrier selection, which can include the trigger of the tendering process. You can use this function instead

of manually starting automatic carrier selection in an app such as Carrier Selection, which is available on the launchpad. For more

information, see Carrier Selection.

## Integration

For more information about the integration of this function into overall background processing, see Background Processing.

## Prerequisites

You have a set of freight orders stored in the system.

You have defined selection profiles (optional). For more information, see Selection Profile.

## Features

This function automatically does the following:

Finds the available carriers for each business document based on the specified carrier selection settings and creates the

ranking list

## Assigns the best carrier if you requested it

Triggers the tendering process if you requested it and no carrier is assigned

## Activities

To use this function, you must run program /SCMTMS/TSPS_OPT_BGD. You must perform the following tasks:

Select the carrier settings.

Select a selection profile or define a set of freight order IDs.

Based on the chosen selection profile or the defined set of freight order IDs (or both), the system selects freight orders. The

explicitly listed freight order IDs will be included. The system executes the process controller strategy defined by the carrier

selection settings, which corresponds to manually executing the steps of automatic carrier selection in an app such as Carrier

Selection, which is available on the launchpad. If you have selected the corresponding checkbox in the function, the system logs all

messages that it creates during execution of the function in the application log under object /SCMTMS/TMS, subobject SCT.

Tendering

## Use

You can use this function to perform tendering separately in the background, in other words, independently of carrier selection.

This can be advantageous for reasons of performance and memory consumption. Moreover, you can use this function to control

This is custom documentation. For more information, please visit SAP Help Portal.

98


1/14/26, 2:46 PM

whether you want to only start tendering in the background and then publish it manually, or whether you want to start and publish

the tendering in the background.

If you want to execute tendering together with carrier selection in the background, you can use the relevant function for carrier

selection. For more information, see Selection of Carriers.

## Integration

For more information about the integration of this function into the overall background processing, see Background Processing.

## Prerequisites

You have a set of freight orders stored in the system.

The prerequisites for automatic tendering have been fulfilled. For more information, see Freight Tendering.

You have optionally defined a selection profile. For more information see Selection Profile.

## Features

You have the following options:

## Start Tendering

When you start tendering, all released freight orders are given the status In Tendering. You can also define that the

tendering plan is created and started automatically. When you start tendering manually, you have to manually set up and

start the tendering plan after executing this function.

## Stop Active Tenderings

You can define that freight orders that are already in the tendering process are canceled.

## Activities

To use this function, you must run the program /SCMTMS/TOR_TENDERING_BATCH.

The system processes the selected steps for the selected freight requests and saves the results.

Creation of Schedule-Based Freight Documents

## Use

This function creates freight documents based on the departures of one or more schedules.

## Integration

For more information about the integration of this function into overall background processing, see Background Processing.

## Prerequisites

You have created schedules and departures. For more information, see Creating Schedules.

This is custom documentation. For more information, please visit SAP Help Portal.

99


1/14/26, 2:46 PM
## Activities

To use this function, you must run program /SCMTMS/MP_SCHED_CREATE_TOR.

On the entry screen, you can choose to create the following freight documents:

Air bookings

Ocean bookings

Road freight orders

## Rail freight orders

For the different freight document types, you can select the respective departures by entering one or more of the following

selection criteria:

Selection Criteria Air Bookings

Ocean Bookings

Freight Orders

Schedules

Gateways

Airports

## Ports

Locations

Airline codes

Flight numbers

Carriers

Vessels

## Voyages

Start date/time

End date/time

Time zone

x

x

x

-

-

x

x

x

-

-

x

x

x

x

x

-

x

-

-

-

x

x

x

x

x

x

x

-

-

-

x

-

-

x

-

-

x

x

x

In addition, you can generate the master air waybill number for your air bookings.

  Note

By default, if a freight document already exists for a specific date, an additional freight document is not created.

## Logging

All departures that match the selection criteria and all freight documents that have been created are written to the log. If you

select the Display Selected Departures checkbox on the Technical Settings screen, you can display the selected departures

before you create the freight documents. All log entries are stored in the application log (object: /SCMTMS/TMS, subobject: PLN).

We recommend that you delete obsolete log entries at regular intervals. For more information, see system documentation for the

Application Log: Delete Expired Logs transaction (SLG2).

This is custom documentation. For more information, please visit SAP Help Portal.

100


1/14/26, 2:46 PM

## Error Handling

There are two different types of errors or messages:

## Errors or messages during departure selection

In the first step, the system selects departures based on the selection criteria. It displays these departures, for example, if

you have selected the Display Selected Departures checkbox on the Technical Settings screen. On this screen, you can

also select the Cancel if Selection Error Occurs checkbox to specify that the system does not create any freight bookings

and cancels processing if errors occur during selection.

## Errors during freight booking creation

In the second step the system creates the freight bookings based on the selected departures in a master flight schedule. If

you have selected the Cancel if Creation Error Occurs checkbox on the Technical Settings screen, the system cancels

processing if errors occur.

Processing of FQs and Overdue RFQs

## Use

You can use this function to evaluate freight quotations (FQs) and to detect that the maximum response time for a request for

quotation (RFQ) is over. If you do not use the function, the tendering process does not continue. The status of the RFQ remains

open and the system does not send RFQs to the next carrier in the tendering plan.

To use this function, you must run the program /SCMTMS/TEND_CONT_PROCESS.

## Integration

For more information about the integration of this function into the overall background processing, see Background Processing.

More Information

## Freight Tendering

Confirmation of Forwarding Orders

## Use

This function automates steps to confirm forwarding orders. You can use this function instead of executing the steps manually in

the apps for your personal object worklist (POWL) from the launchpad. We recommend that you use background processing if you

want to process and confirm multiple forwarding orders simultaneously.

## Integration

For more information about the integration of this function into the overall background processing, see Background Processing.

## Prerequisites

You have created forwarding orders in the system.

This is custom documentation. For more information, please visit SAP Help Portal.

101


1/14/26, 2:46 PM

You have optionally defined a selection profile. For more information see Selection Profile.

## Activities

To use this function, you must run program /SCMTMS/TRQ_CONF_BATCH.

You can select a selection profile or enter the selection criteria manually. Additionally, you can specify whether the forwarding

orders are to be processed in parallel. The system considers only those forwarding orders that have not yet been completed or

canceled.

The system selects forwarding order items from the planning data on the basis of the selection profile or the selection criteria that

you entered. The system processes the forwarding order and saves the results. The system logs all messages that it creates while

executing this function in the application log under object /SCMTMS/TMS and subobject BP.

You can call the application log from the SAP Easy Access screen by choosing  Logistics

 Transportation Management

## Administration

 Display Application Log Entries .

More Information

## Freight Unit

Posting Goods Issue from TM

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

This is custom documentation. For more information, please visit SAP Help Portal.

102


1/14/26, 2:46 PM

In SAP ERP, the synchronous ERP inbound service OutboundDeliveryERPChangeRequestConfirmation_In_V1 is used to

post a goods issue for an outbound delivery in ERP. In TM this service is replicated as an outbound service:

OutboundDeliveryERPChangeRequestConfirmation_Out_V1. This TM outbound service does not support the complete

functionality of the ERP inbound service but only the subset needed for goods issue posting.

## Activities

You can use transaction SE38 to run the program /SCMTMS/POST_GI_BATCH to post goods issue to SAP ERP.

The system checks the goods movement status of the delivery in the ERP system and selects only deliveries for which no goods

issue has been posted. For all such deliveries the system checks the execution status for the related DTR in the TM system. The

system triggers goods issue for all DTRs for which execution has started or completed.

Creation of Deliveries in Logistics Execution

## Use

This function creates deliveries for orders.

You can select by:

Selection Profiles

## Selection Parameters

Note that if the user specified a delivery profile that requires the planning results to be fixed for planned freight units, directly

created freight orders, freight orders, or freight bookings, the system fixes the planning results during delivery proposal creation.

Otherwise, the system does not fix the planning results.

## Integration

For more information about the integration of this function into overall background processing, see Background Processing.

## Prerequisites

You have made settings for order integration. For more information, see Configuring Integration of Orders and Deliveries.

If you want to use a selection profile when using this function, you have defined a selection profile. For more information,

see Profiles and Settings.

If you want to use a delivery profile when using this function, you have defined a delivery profile. For more information, see

Delivery Profile.

## Features

When you run the program /SCMTMS/DLV_BATCH, you can either specify selection profiles that are used to select the documents

for which deliveries are to be proposed, or you can manually enter selection criteria. You can also specify a delivery profile.

You can specify that freight units or transportation units need to be planned ahead of delivery creation.

The report allows parallel processing.

This is custom documentation. For more information, please visit SAP Help Portal.

103


1/14/26, 2:46 PM

Further options are available for how the function handles selected data; for example, how freight units are handled if a freight unit

that is determined is not completely assigned to a selected document. For more information, see the field help in the function.

## Activities

To access this report you open the Program to Create Delivery Proposals app from the launchpad..

Creation of Locations

## Use

The report /SAPAPO/CREATE_LOCATION creates locations for business partners, plants, and shipping points depending on the

given selection criteria. All selected entities which have no location are considered for the location creation.

Details about the location creation are written into the application log.

Related Information

Creating Locations

Updating Locations

## Filling of Location UUIDs

For all newly created locations, the location UUID field is filled with appropriate values. However, for existing locations from

previous releases, this field is empty after upgrading. You can use the report /SAPAPO/FILL_LOCATION_GUIDS to fill these

empty fields.

## Updating Address Numbers of Locations

It may happen that users create multiple instances of the same location in the system, for example, for business partners, plants or

shipping points, and that the system assigns different address numbers to these instances. You can use the report

/SAPAPO/UPDATE_LOC_ADDRNR to overwrite the address numbers of such locations. For locations of business partners, this is

only possible if the business partner has just one standard address.

The report assigns the location the same address number as the original entity. Furthermore, location details like geocodes or

transportation zone assignments are updated according to the new address. Details are written into the application log.

## Update Location for Shipping Points and Plants

If there are changes to the address data (including the transportation zone) of shipping points and plants you can use the report

/SAPAPO/UPD_LOC_SP_PL to update the corresponding location data.

## Related Information

## Updating Locations Using a Report

This is custom documentation. For more information, please visit SAP Help Portal.

104


1/14/26, 2:46 PM

Processing of FUs for Direct Shipment

## Use

The system converts freight units for which it has determined direct shipment options into freight orders for direct shipment. It

also assigns these freight units to freight orders that meet the requirements in terms of the source location, carrier, and pick-up

date.

We recommend that you schedule this function to run periodically in the background and that you use the pick-up date as

selection criterion.

## Integration

For more information about the integration of this function into the overall background processing, see Background Processing.

## Prerequisites

In case you do not want to use the default freight order type, you have assigned a freight order type either directly or via condition

to the freight unit type in Customizing. For more information, see Customizing for Transportation Management under  Planning

## Freight Unit

 Define Freight Unit Types .

## Activities

To use this function, you must run the program /SCMTMS/DIRECT_SHIPMENT_BATCH. You must specify one of the following

settings:

Define a pick-up date for selection.

Select a selection profile.

Define a set of freight units.

Combine the different selection criteria.

If you want the system to assign freight units to freight orders, you can restrict the selection to those freight units for which you

have defined a corresponding DSO result rule in Customizing for freight unit types.

Depending on either the selection criteria specified in this function or the selection profile, the system selects those freight units

for conversion or assignment that have previously identified direct shipment options and for which one of the options has been

selected. The conversion of a freight unit into a freight order encompasses the following:

Change of the document category from FU to TO

Determination of a new document ID

## Assignment of the selected carrier

Adaptation of the transportation stops according to the scheduled pick-up and delivery times of the selected direct

shipment option

If the system selects freight units to be assigned to freight orders, it identifies suitable freight orders that match the requirements

of the source location, carrier, and pick-up date. If the system cannot find a suitable freight order, it creates a new one. In this case,

it transfers the data from the freight unit and the direct shipment option to the new freight order.

This is custom documentation. For more information, please visit SAP Help Portal.

105


1/14/26, 2:46 PM

If you have activated tracking of execution with SAP Event Management for the freight unit type and freight order type, the system

deletes the event handler for the freight unit and creates a new event handler for the freight order.

The system logs all messages that it creates while executing the function in the application log under object /SCMTMS/TMS,

subobject DSO.

## More Information

Determination of Direct Shipment Options

Processing of Freight Bookings

## Use

This function automates the different actions for freight bookings.

## Integration

For more information about the integration of this function into the overall background processing, see Background Processing.

## Prerequisites

Freight bookings exist that are ready to be sent to the business partner using EDI (Electronic Data Interchange) or print

document (for example, a carrier was assigned).

You have specified the following output options in the freight booking type in Customizing:

Output Profile /SCMTMS/TOR_PRINT_SEA

## Additional Output Profile /SCMTMS/TOR

You have optionally defined a selection profile. For more information see Selection Profile.

## Activities

To use this function, you must run program /SCMTMS/TOR_BO_PROC_BATCH.

You can select a selection profile or enter the selection criteria manually. Additionally, you can specify whether the freight bookings

are to be processed in parallel (see Definition of Parallel Processing Profiles ).

Based on the selection profile or the selection criteria you entered, the system chooses freight bookings and executes the action

you choose:

The system sends the freight bookings to the shipping company, for example, and updates the confirmation status.

The system sends shipping instructions and updates the confirmation status.

The system sends the freight bookings to the ERP system and updates the status of the transfer to ERP. Shipments are

created or changed automatically in the ERP system.

The system sets the execution status to Ready for Transportation Execution or MAWB Closed (air freight scenario). This

ensures that all prerequisites are fulfilled with the result that the relevant print documents can be printed. For more

information about print documents, see Printing.

This is custom documentation. For more information, please visit SAP Help Portal.

106


1/14/26, 2:46 PM

The system fixes the freight bookings.

The system sets the life cycle status of the freight bookings to Completed.

The system saves the results.

By selecting the corresponding checkbox, you can ensure that the system executes the requested action only for the unprocessed

business documents. This means that the system only executes the action for the selected freight bookings if it has not already

executed the action once (for example, as a result of a user action on the user interface).

If you have selected the corresponding checkbox, all messages that the system creates while executing this function are saved in

the log display under object /SCMTMS/TMS and subobject BP.

You can call the application log from the SAP Easy Access screen by choosing  Cross-Application Components

 Processes and

Tools for Enterprise Applications

 Remote Control and Communication Framework

 Log Display .

More Information

## Freight Booking

Uploading of Allocations

## Use

You use this function to upload allocations from an external source to the Transportation Management (TM) system. Additionally,

with this function, you can change specific buckets of existing allocations.

  Note

If you want to change existing allocations, enter the allocation ID in your external source.

## Prerequisites

You have configured the relevant settings in Customizing for Transportation Management. For example, you have defined locations,

carriers, and allocation types that are used in the allocations you want to upload to your TM system.

## Features

This function only supports the XML-based Microsoft Excel worksheet file format.

If you select the Overwrite existing buckets checkbox, the system creates all buckets from your external source. At the same time,

the system searches for conflicts in existing buckets for a particular carrier on a specific trade lane that have a start date or an end

date that is in the time period of a bucket for the same carrier and trade lane in the external source. For every conflict found, the

system deletes the affected buckets.

If you do not select the Overwrite existing buckets checkbox, the system checks any buckets that already exist for a particular

carrier on a specific trade lane. It only creates buckets before or after the time periods of existing buckets.

The system cannot save the following information when uploading allocations from an external source to the TM system:

## Freight agreement

This is custom documentation. For more information, please visit SAP Help Portal.

107


1/14/26, 2:46 PM

## Item

Schedule

## Attribute

Additionally, the system determines the following information when uploading allocations from an external source to the TM

system irrespective of the data you entered in the external source:

Trade lane

## Allocation ID

Details such as current volume and current weight

## Activities

Besides executing this function, you can also upload allocations from an external source to the TM system by doing one of the

following:

Choose the Upload Allocations pushbutton in the allocations worklist

Choose the Upload Allocations pushbutton in the allocation UI

Processing of Freight Orders

## Use

This function automates the different actions for freight orders.

## Integration

For more information about the integration of this function into the overall background processing, see Background Processing.

## Prerequisites

Freight orders exist that are ready to be sent to the business partner using EDI (Electronic Data Interchange) or print

document (for example, a carrier was assigned).

You have specified the following output options in the freight order type in Customizing:

Output Profile /SCMTMS/TOR_PRINT_ROAD

## Additional Output Profile /SCMTMS/TOR

You have optionally defined a selection profile. For more information see Selection Profile.

## Activities

To use this function, you must run program /SCMTMS/TOR_FO_PROC_BATCH.

You can select a selection profile or enter the selection criteria manually. Additionally, you can specify whether the freight orders

are to be processed in parallel (see Definition of Parallel Processing Profiles).

This is custom documentation. For more information, please visit SAP Help Portal.

108


1/14/26, 2:46 PM

Based on the selection profile or the selection criteria you entered, the system chooses freight orders and executes the action you

choose:

The system checks whether the selected freight orders have to be updated. The system sends the freight orders to the

carrier and updates the subcontracting status.

The system sends the freight orders to the ERP system and updates the status of the transfer to ERP. Shipments are

created or changed automatically in the ERP system.

The system sets the execution status to Ready for Transportation Execution. This ensures that all prerequisites are fulfilled

with the result that the relevant print documents can be printed. For more information about print documents, see Printing.

The system fixes the freight orders.

The system sets the life cycle status of the freight orders to Completed.

The system saves the results.

By selecting the corresponding checkbox, you can ensure that the system executes the requested action only for the unprocessed

business documents. This means that the system only executes the action for the selected freight orders if it has not already

executed the action once (for example, as a result of a user action on the user interface).

If you have selected the corresponding checkbox, all messages that the system creates while executing this function are saved in

the application log under object /SCMTMS/TMS and subobject BP.

You can call the application log from the SAP Easy Access screen by choosing  Cross-Application Components

 Processes and

Tools for Enterprise Applications

 Remote Control and Communication Framework

 Log Display .

To prevent freight orders that have already been sent to the SAP ERP system from being sent again, you can use the report to

check whether the freight order is relevant for transfer. New freight orders are relevant for transfer. The system transfers freight

orders with this status, creates a transport in the SAP ERP system, and the processed freight order is no longer relevant for

transfer. If the freight order is changed in Transportation Management (TM), it is relevant again for transfer. If the corresponding

freight order is not changed in the SAP TM system, it remains not relevant for transfer. Services that are triggered by the SAP ERP

system do not change this status.

More Information

## Freight Order

Offline Workflow for Sending and Approving Work Items

## Use

Transportation Management (TM) can send work items for the following objects by e-mail to a user:

Freight agreement RFQ masters

## Agreements

## Validity periods in rate tables

The user can accept or reject the work item and update the system by e-mail. This capability gives a user the flexibility to process

work items for the objects without logging on to TM.

This is custom documentation. For more information, please visit SAP Help Portal.

109


1/14/26, 2:46 PM

  Note

For freight agreement RFQ masters, the system only e-mails work items that are in a ready status in your Business

Workplace inbox. For example, it does not e-mail work items that are in process.

Work items sent for offline approval remain in the approver’s Business Workplace inbox until TM receives and processes

the reply e-mails that contain the decisions.

If the user processes the work items online before the system receives and processes the reply e-mails, the system

ignores the reply e-mails.

## Integration

For more information about the integration of this function into the overall background processing, see Background Processing.

Prerequisites

## General

You have specified the prerequisites required to enable the approval workflow. For more information, see Approval Check.

You have specified the following information for the user in the appropriate position (for example, Customer Agent) in your

organization:

## User name of WF-BATCH

E-mail address on the Address tab page

User type of Dialog on the Logon Data tab page

You can specify the information under transaction SU01.

You have specified the necessary settings for sending and receiving e-mails for TM. For more information, see SAP Library

for SAP NetWeaver on SAP Help Portal at http://help.sap.com/nw. In SAP Library, choose  Function-Oriented View

 Application Server

 Application Server ABAP

## Other Services

 Services for Business Users

 Business Workplace

(BC-SRV-GBT)

 Administration of the Business Workplace

  Administration of the Send, Folder, and Office Functions

## Sending

 External Sending in the SAP System .

## Individual Objects

For work items for freight agreement RFQ masters, you have specified the prerequisites for freight agreement RFQ masters.

For more information, see Requesting of Quotations for Transportation Services.

For working with work items for agreements, you have specified the prerequisites for agreements. For more information,

see Agreement Maintenance.

For working with work items for validity periods in rate tables, you have specified the prerequisites for rate tables. For more

information, see Rate Definition and Maintenance.

## Features

## Sending Work Items by E-mail

You use program /SCMTMS/WI_NOTIFICATION_OFFAPP to send work items by e-mail to users for offline approval.

This is custom documentation. For more information, please visit SAP Help Portal.

110


1/14/26, 2:46 PM

You create a variant of the program in which you specify the selection parameters you want to use to send the work items. You

specify the following settings in the variant:

The time from which the work items are created

WF-BATCH, the user to whom you want to send the e-mails

## The language of the e-mail

## The job suffix to specify a unique run of the function

In transaction Define Background Job (SM36) you use the variant to create a background job. You enter the name of the program

and the variant in the ABAP Program screen area of the Create Step 1 screen. You can schedule the program under the start

conditions.

You execute the background job in transaction Simple Job Selection (SM37).

The system sends an e-mail with a short standard text that contains the main details from the work item. The e-mail also contains

an accept hyperlink and a reject hyperlink. When the user chooses one of the hyperlinks, the function automatically creates a reply

e-mail.

  Caution

We do not recommend that users forward the reply e-mail to third parties. For security reasons, TM only accepts reply e-mails

from the e-mail address of the original recipient.

## Inbound Processing

In the Create Step 1 screen of SM36, you enter the following information:

## User WF-BATCH

Program /SCMTMS/WI_OFFLINE_EVAL_REPORT in the ABAP Program screen area

You schedule the program under the start conditions.

You execute the program in SM37. In the Job Overview screen, you can check the work items that the user has processed from the

inbox.

The system only processes an e-mail if the sender is user WF-BATCH. If the object is locked by another user when the system

receives the reply e-mail, or if immediate processing fails for any other reason, the system displays a failure message in the Job

Overview screen.

You can check the received status of inbound e-mails in transaction SAP Connect: Inbound Send Requests (SMTP) (SOIN). To

display e-mails received, ensure that you specify Always Save in the Incoming E-mails screen area under  Utilities

## MIME

Settings .

Calculation of Profitability

## Use

This function enables you to automate the calculation of profitability in forwarding orders. Run the program

/SCMTMS/CALC_PROFITABILITY.

This is custom documentation. For more information, please visit SAP Help Portal.

111


1/14/26, 2:46 PM
## Prerequisites

For information about the prerequisites you must specify for calculating profitability, see Profitability Analysis.

## Integration

For more information about the integration of this function into the overall background processing, see Background Processing.

## Features

## Recalculation of Profitability and Charges

You can recalculate the profitability of a forwarding order that has a profitability status of Recalculation Required. You can also

recalculate the charges and internal charges of a forwarding order.

## Parallel Processing Profile

You can specify the technical processing conditions the system uses to process the function, such as application server usage and

queue time. You can create and edit profiles by choosing from the SAP Easy Access menu  Logistics

 Transportation

## Management

## Current Settings

 Define Parallel Processing Profile .

Communication of Settlements with SAP ERP

## Use

You can use this function to process actions for the background communication with SAP ERP of the following objects:

Freight, forwarding, and internal settlements, and credit memos

Credit management updates from Transportation Management (TM) to SAP Credit Management

The system uses the Post Processing Framework (PPF) to communicate with SAP ERP. For example, the system uses the PPF

action profile /SCMTMS/CFIR to communicate forwarding settlements to SAP ERP. The profile /SCMTMS/CFIR uses the following

action definitions:

/SCMTMS/SEND_CFIR_CANCELLATION

/SCMTMS/SEND_CFIR_REQUEST

/SCMTMS/SEND_CREDIT_UPDATE

## Integration

For more information about the integration of this function into the overall background processing, see Background Processing.

## Prerequisites

You have specified the action profiles /SCMTMS/TOR_INV_PREP and /SCMTMS/CFIR in the customizing activities

Maintain PPF Settings and Maintain Output Management Adapter Settings. For more information, see Cross-Application

Components under  Processes and Tools for Enterprise Applications

 Reusable Objects and Functions for BOPF

## Environment

 PPF Adapter for Output Management

.

This is custom documentation. For more information, please visit SAP Help Portal.

112


1/14/26, 2:46 PM

You have entered Processing when saving document in the field Processed At for all action definitions contained in the

/SCMTMS/TOR_INV_PREP and /SCMTMS/CFIR action profiles.

  Note
For the business object Supplier Freight Invoice Request (SFIR), Customizing contains the action profile

/SCMTMS/TOR_INV_PREP. For the business object Customer Freight Invoice Request (CFIR), Customizing contains

the action profile /SCMTMS/CFIR.

You assign these profiles in the Output Profile field of the Define Forwarding Settlement Document Types and Define

Freight Settlement Document Types Customizing activities. For more information, see Customizing for Transportation

Management under  Settlement

. Choose Freight Settlement or Forwarding Settlement, as appropriate.

The settlement documents that are processed in the background using this function have the status Transferred for

Accruals.

## Features

This function automatically executes the following actions:

For action profile /SCMTMS/TOR_INV_PREP, it does the following:

Requests the preparation of a freight settlement document (FSD)

## Requests the cancellation of an FSD

For action profile /SCMTMS/CFIR, it does the following:

Requests a forwarding settlement document (FWSD)

Requests the cancellation of an FWSD

## Request an update to SAP Credit Management

For more information, see the system documentation for program RSPPFPROCESS.

## Activities

To use this function, you must run the program RSPPFPROCESS. You must specify the following settings:

Select application /SCMTMS/TRANSPORTATION.

Choose the corresponding action profile and action definition.

Select Processing When Saving Document in the Time of Processing field.

Based on the selection criteria, the system selects the actions and executes them automatically in the background. If you run the

function in a dialog, the system selects the actions according to the selection criteria and displays them in the SAP List Viewer

(ALV). In the ALV, you can select individual actions or all actions and process them.

Creation and Transfer of Forwarding Settlement Documents

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

113


1/14/26, 2:46 PM

This function enables you to automate the creation of forwarding settlement documents (FWSDs). Run the program

/SCMTMS/CFIR_CREATE_BATCH. If you want the system to transfer the settlement documents to SAP ERP after creation

automatically, select the Immediate Transfer to ERP checkbox. If you do not automatically transfer settlement documents after

creation, you must run the program /SCMTMS/CFIR_TRANSFER_BATCH to transfer the settlement documents. For example, you

create settlement documents but then you want to transfer the settlement documents to SAP ERP in a structured way, twice a day.

You schedule the program /SCMTMS/CFIR_TRANSFER_BATCH to run in the background. This makes sure that the system

transfers all settlements that are not blocked to SAP ERP.

The Creation and Transfer of Forwarding Settlement Documents function does not create forwarding settlement documents with

a zero value. For example, the function does not create a settlement where you have not entered calculation details in an

agreement because you have agreed with a customer that you enter charges manually in the settlement for each individual

forwarding order. Also, the function automatically excludes forwarding orders that are already completely invoiced.

## Integration

For more information about the integration of this function into the overall background processing, see Background Processing.

## Prerequisites

## Forwarding Settlement Document

You have specified the appropriate settings for forwarding settlements (see Forwarding Settlement).

## Forwarding Settlement Document Types

You have assigned the FWSD type to an appropriate forwarding order (FWO) type in Customizing for Transportation Management

under  Forwarding Order Management

## Forwarding Order

 Define Forwarding Order Types .

## Settlement Profiles and Calculation Profiles

You have specified the relevant forwarding settlement profiles and calculation profiles (see Forwarding Settlement).

## Internal Settlement

You have specified the appropriate settings for internal settlements (see Internal Settlement Management).

## Credit Memos

To transfer credit memos to SAP ERP in the background, you have specified the appropriate settings for credit memos (see Credit

Memos for Forwarding Orders).

## Features

## Forwarding Settlements

To create forwarding settlements, you enter a document category of Forwarding Settlement Document. You enter either a

selection profile or the appropriate forwarding order document settings to specify the forwarding orders that the system uses to

create the settlements.

## Internal Settlements

To create internal settlements, you enter a settlement document category of Internal Settlement Document. You enter the

appropriate freight order or freight booking settings. The system uses the forwarding orders that are linked to these freight orders

This is custom documentation. For more information, please visit SAP Help Portal.

114


1/14/26, 2:46 PM

or freight bookings to create the settlements.

## Change Process for Forwarding Settlements

The system can take the following conditions into account when it creates a forwarding settlement document:

## Automatic change processing settings for the forwarding settlement

You can enable the automatic forwarding settlement change process in the relevant settlement profile, by specifying a

change process of either Reverse and Repost or Delta Only. The system uses the organization, or a combination of

organization and business partner, to assign the settlement profile to the forwarding order.

## Attribute changes in the forwarding order

The system flags the forwarding order as changed if you make the following changes after you have created a settlement

document:

Change the logistical data or charge information, and your change results in an update to the charges in a

forwarding order

The system indicates the change in the Late Changes setting on the Charges and Internal Charges tab pages of a

forwarding order.

Change the sales organization or business partner of a forwarding settlement

This includes a change to the ordering party, prepaid agreement party, or collect agreement party. The system

changes the invoicing status of the forwarding order to Not Up-to-Date.

Change the agreement determination attributes of the forwarding order, for example, service level, movement type,

shipping type, and changes in the stages

The change results in a new agreement or a new calculation sheet. The system changes the invoicing status of the

forwarding order to Not Up-to-Date.

You can specify the following forwarding settlement document creation settings in this background processing function:

## Include changed forwarding orders

The system creates forwarding settlement documents for all forwarding orders that have met one of the following criteria:

## Invoicing status is Not Up-to-Date, Not Invoiced, or Partially Invoiced

Late Changes setting is specified on the Charges and Internal Charges tab pages of a forwarding order, to indicate

the forwarding orders that you have changed

## Exclude changed forwarding orders

The system does not create forwarding settlement documents for forwarding orders that you have changed, and instead

creates forwarding settlement documents for all forwarding orders that are in an invoicing status of Not Invoiced or

Partially Invoiced.

## Only changed forwarding orders

The system only creates forwarding settlement documents for the forwarding orders that you have changed, where in the

forwarding order has met one of the following criteria:

## Invoicing status is Not Up-to-Date

Late Changes setting is specified on the Charges and Internal Charges tab pages

For more information, see Automatic Change Management for FWSDs and ISDs.

This is custom documentation. For more information, please visit SAP Help Portal.

115


1/14/26, 2:46 PM

## Header-Level Charges

You can include charges in an internal settlement document as follows:

Include both header-level charges and stage-level charges

This is the default setting of the function.

Include only stage-level charges and leave out header-level charges

You must deselect the Settle Header Charges checkbox.

You cannot create an internal settlement document only for header-level charges and leave out stage-level charges.

If you select the Header Charges in Separate Settlement Documents checkbox, the system creates a separate internal

settlement document for the header-level charges. If you don’t select the checkbox, the system includes the header-level charges

and the stage-level charges in the same internal settlement document.

To create an internal settlement for all the charge items that are ready for invoicing in a forwarding order, you can specify

parameters for the relevant forwarding order.

For example, you enter a forwarding order number in the selection parameters. You select Header-Level Charges. The system

selects the header-level charges of the forwarding order for inclusion in the background processing function.

If you enable the Stage Split setting in the relevant settlement profile, then the system creates separate settlement documents for

each stage-level charge item, and separate settlement documents for each header-level charge item. It does this regardless of the

setting you specify in the Header Charges in Separate Settlement Document checkbox. For example, the following table

describes the stages and charges you have in a forwarding order:

Purchase Organization of Freight

## Stage

Charge Item

Document

FWH_1

FWH_1

FWH_2

FWH_2

FWH_3

FWH_3

Header-level charge item

Header charge

Pre-carriage

## Stage charge

Header-level charge item

Header charge

Main carriage

## Stage charge

Header-level charge item

Header charge

On-carriage

## Stage charge

An example of a header-level charge item is an export documentation charge that you can incur during the pre-carriage stage of a

transportation. This charge applies to the entire transportation, and you may want to settle this charge separately from the other

pre-carriage charges.

Regardless of the setting you specify in the Header Charges in Separate Settlement Document checkbox, the system creates a

total of 6 internal settlement documents, one for each header-level and stage-level charge of each stage.

If you don’t enable the Stage Split setting in the relevant settlement profile, the system creates 3 settlement documents. It creates

a settlement document for each of the 3 different purchase organizations in the freight order or freight booking.

## Credit Memos

This is custom documentation. For more information, please visit SAP Help Portal.

116


1/14/26, 2:46 PM

You cannot use the /SCMTMS/CFIR_CREATE_BATCH program to create credit memos in the background. Instead, you must

create credit memos manually. However, you can use the /SCMTMS/CFIR_TRANSFER_BATCH program to transfer credit memos

to SAP ERP in the background.

## Invoice Date

You can create forwarding settlement documents for just the forwarding orders that have a particular invoice date, or that have an

invoice date in a range of invoice dates. For example, you specify an invoice date range of December 10, 2014 to December 15, 2014.

When you run the background function, the system only creates forwarding settlement documents for forwarding orders that have

an invoice date in the range of December 10, 2014 to December to 15, 2014.

## Zero Amounts and Calculation Errors

The following table illustrates how the system treats a charge item with a zero amount when you run the background

processing function:

## Order

Final Amount (USD)

Settlement Document

Invoicing Status of Charge

Charge item 1

Charge item 2

10

Zero

## Item

Settlement document 1

Completely Invoiced

No settlement document

Cannot Invoice Automatically

created

When you calculate charges in the order, you get a zero amount for charge item 2. When you use the background

processing function to create a settlement document for the order, with a settlement profile that contains a Calculation

Option setting of Copy all Charges, you also get a zero amount for charge item 2.

The system does not create settlement documents for these charge items and sets the invoicing status of the charge items

to Cannot Invoice Automatically. This prevents the system from processing the same order and charge item with a zero

amount every time it runs the background processing function. This reduces the amount of time the system needs to

create settlement documents in the background by ignoring these charge items.

If the system again determines the invoicing status of the charge item in the order when you calculate charges in the order,

the system determines the invoicing status for the charge item as follows:

## Not Invoiced if the system doesn’t create a settlement document

Over Invoiced if the charge amount in the order is less than the charge amount in the settlement document

Partially Invoiced if the charge amount in the order is more than the charge amount in the settlement document

The system does not change the invoicing status to Cannot Invoice Automatically in the following situations:

## Execution-based charge items

An execution-based charge item always has a zero amount in an order as the charges are calculated in the

settlement document, for example, in a buyer's consolidation. For execution-based charges, the system doesn't set

the invoicing status to Cannot Invoice Automatically to prevent the system from excluding such charges from the

settlement run.

## Invoice date in a calculation profile

There may not be any charge, and therefore a zero invoice amount, for a charge item if you specify a Calculation

Date Type of Invoice Date in Customizing for the relevant calculation profile.

For example, you have a rate that is valid from a certain date in the future. When you calculate charges and create a

settlement document, the system uses an order date of today’s date to calculate charges. The system does not use

This is custom documentation. For more information, please visit SAP Help Portal.

117


1/14/26, 2:46 PM

the rate that will be effective in the future to calculate charges. In this case, there will be a zero invoice amount.

If you create a settlement document at the date in the future, the system uses the future date as the invoice date on

which to calculate charges. In this case, there will be an invoice amount.

The system doesn’t specify an invoicing status of Cannot Invoice Automatically for these charge items.

For more information, see Customizing for Transportation Management under  Basic Functions

## Charge

Calculation

## Basic Settings

 Define Calculation Profiles .

Settlement charge items where the Calculation Option in the relevant settlement profile is Copy Fixed Charges and

Redetermine Others.

When you calculate charges, there may not be a charge amount. If you then specify a calculation option of Copy

Fixed Charges and Redetermine Others, the system may determine a charge when it creates a settlement. Because

of this, you cannot set the invoicing status to Cannot Invoice Automatically.

The system creates settlement documents with calculation errors only when you select the Create with Calc. Errors

(Create with Calculation Errors) setting and run the background processing function. If you don’t select the Create with

Calc. Errors setting, the system deletes the settlement documents that contain calculation errors. The system doesn’t set

the invoicing status to Cannot Invoice Automatically for these charge items.

## Selection Profile

You can define a selection profile to work with a subset of the settlements that need to be created and transferred. You can create

and edit profiles in on the launchpad under  Application Administration

## Planning

 Selection Profiles .

Message Display

## Detailed Messages

The system displays the following information after you create and transfer settlement documents:

List of orders for which it did not create settlement documents, and the reasons why it did not create the

settlements

Number of settlement documents created

## List of settlement documents created

If you select the Detailed Messages checkbox, the system displays additional details on-screen. For example, it displays the

input parameters you entered, the service date for each settlement, and the orders included in the settlements. The system

includes the additional details in the Analyze Application Log transaction (SLG1) regardless of whether you select the

Detailed Messages checkbox. The system creates the application log when you create and transfer settlement documents

in production mode (when you do not select the Run in Simulation Mode checkbox).

## Log Messages About Calculation Sheets

If you select the Log Calc. Sheet Messages (Log Calculation Sheet Messages) checkbox, the system displays the relevant

messages for each charge item in the Charge Analysis Log tab page of the settlement document. The system only displays

these messages if charges have been calculated for the settlement document.

## Parallel Processing Profile

You can specify the technical processing conditions the system uses to process the function, such as application server usage and

queue time. You can create and edit profiles on the launchpad under  Application Administration

 General Settings

## Define

Parallel Processing Profile (/SCMTMS/PPRF)

.

## Package Size

This is custom documentation. For more information, please visit SAP Help Portal.

118


1/14/26, 2:46 PM

You can define the maximum number of orders that the system processes for settlement creation in a processing step. This

enables you to optimize the system runtime and resource utilization when the system executes the background processing

function. For example, you specify 100 as your package size. You have 250 orders ready for settlement document creation. The

system creates the settlements in steps, processing a maximum of 100 orders in each step. In this case, the settlement process

runs in 3 iteration steps to complete the processing of the 250 orders.

## Prevent Split Due to Package Size in Collective Settlements

When the system uses a package size to create settlements in the background, it groups the forwarding orders that are due for

settlement by certain split criteria before it creates the forwarding settlement documents. For more information about the

standard split criteria, see Split Criteria in Settlement Document Creation.

You can use the Prevent Split Due to Package Size in Collective Settlements setting to prevent the system from creating

additional settlements because of the package size split, when it creates collective settlements. This ensures that the system only

splits a settlement creation run for a relevant business reason and not for the hard restriction of the number of forwarding orders

you specify in the package size, when it creates collective settlements. The following table contains an example of the forwarding

orders that are ready for settlement creation.

Business Partner

Forwarding Order

1

1

1

1

2

2

2

3

3

4

1

3

5

8

2

4

6

7

9

10

If you don’t enable Prevent Split Due to Package Size in Collective Settlements, and you have a package size of 3, the system

creates your collective forwarding settlement documents as follows:

Creation Run by

Forwarding Orders by

Business Partner

Forwarding Order in the

Forwarding Settlement

## Package

## Package Size

Forwarding Settlement

Document

1

1

2

2

3

3

1 to 3

1 to 3

4 to 6

4 to 6

7 to 9

7 to 9

1

2

1

2

1

3

Document

1, 3

2

5

4, 6

8

7, 9

FWSD 1

FWSD 2

FWSD 3

FWSD 4

FWSD 5

FWSD 6

This is custom documentation. For more information, please visit SAP Help Portal.

119


1/14/26, 2:46 PM

Creation Run by

Forwarding Orders by

Business Partner

Forwarding Order in the

Forwarding Settlement

## Package

## Package Size

Forwarding Settlement

Document

Document

4

10

4

10

FWSD 7

However, in your business, you may not want the system to create 7 forwarding settlement documents during the creation run.

Instead, you may want the system to create a single collective forwarding settlement document for each business partner. To

enable this, you select Prevent Split Due to Package Size in Collective Settlements. With a package size of 3, the system creates

forwarding settlement documents as follows:

Creation Run

Forwarding Orders

## Comment

Business Partner

Forwarding Order

Forwarding

by Package Size

by Business

Partner

Settlement

Document

1

2

3

3

1, 3, 5, 8

System processes

1

1, 3, 5, 8

FWSD 1

more than 3

forwarding orders

because of this

setting

2, 4, 6

7, 9, 10

7, 9, 10

None

None

None

2

3

4

2, 4, 6

7, 9

10

FWSD 2

FWSD 3

FWSD 4

Updating of Credit Exposure

## Use

This function enables you to update the credit exposure for a business partner in SAP Credit Management from Transportation

Management (TM). Run the program /SCMTMS/CLC_EXPOSURE_UPDATE.

For example, you are a logistics service provider (LSP). You use a forwarding order to transport goods on behalf of a shipper. You

use Sales and Distribution (SD) to bill your customer and Financial Accounting (FI) to receive payment from your customer. You

integrate credit management functionality with your forwarding orders. This ensures that you manage your credit exposure to your

shippers.

You notice that there is an error in your credit management information. For example, the system does not update your credit

management information properly and you have a mismatch between your forwarding orders and your credit exposure in credit

management.

To correct the information, you must take the following actions:

1. Delete the credit exposure information in credit management

In credit management, you run the program UKM_COMMTS_DELETE for a particular customer. This deletes all the credit

exposure information for the customer from credit management.

2. Create correct information in credit management using the information from your forwarding orders

In TM, you run program /SCMTMS/CLC_EXPOSURE_UPDATE. In the background, the system takes the following steps:

a. Finds all the forwarding orders in TM that have a particular business partner

This is custom documentation. For more information, please visit SAP Help Portal.

120


1/14/26, 2:46 PM

b. For each forwarding order, determines the credit exposure amount from the credit limit check amount and amount

that is already invoiced for each business partner in the forwarding order.

For example, you have a forwarding order for business partner CUST_01. The charge calculated is USD 1000 and this

is also the credit limit check amount. The following table explains the amount the system sends to SAP Credit

Management to update the credit exposure amount:

Charge for

Credit Limit

Invoicing Status

Credit Limit

Credit Exposure

Business Partner

Check Amount

Check Status

FWO 1

USD 1000

USD 1000

Not Invoiced

Successful or

USD 1000

CUST_01

Manually

Approved

FWO 1

USD 1000

USD 1000

Not Invoiced

## Failed

No update sent

CUST_01

FWO 1

USD 1000

USD 1000

Completely

Successful or

No update sent

CUST_01

Invoiced or Over

Manually

Invoiced

Approved

FWO 1

USD 1000

USD 1000

Partially Invoiced

Successful or

USD 50

CUST_01

(say only USD

## Manually

950 is invoiced)

## Approved

c. For each forwarding order, creates an XML message to be sent to SAP Credit Management

TM integrates directly with SAP Credit Management when you configure TM and SAP Credit Management on a

single client. If you configure SAP Credit Management on a separate system or client, TM uses Web Services to

interact with SAP Credit Management.

The XML message contains the credit exposure amount to be updated in SAP Credit Management.

d. Updates the open billing items in SD billing and FI accounts receivable

In SAP Credit Management, you run the program UKM_TRANSFER_ITEMS.

## Prerequisites

For more information about defining the credit segment IDs that TM uses to access the credit management functionality in SAP

Credit Management, see Customizing for Transportation Management under Basic Functions

 Credit Management

## Integration

 Integration with Credit Management

.

You have enabled the relevant forwarding order type for a credit limit check, and you have specified an action for when the credit

limit check fails. For more information, see Customizing for Transportation Management under  Forwarding Order Management

## Forwarding Order

 Define Forwarding Order Types .

You have enabled your business partner for credit management, under transaction BP. You have specified a Display in BP Role of

SAP Credit Management. You specify a credit segment, a check rule, and a credit limit.

Features

## Statuses

The system only includes forwarding orders that have an Invoicing status of Not Invoiced or Partially Invoiced. These forwarding

orders have a credit limit check status of Successful or Manually Approved. The system excludes forwarding orders with all other

This is custom documentation. For more information, please visit SAP Help Portal.

121


1/14/26, 2:46 PM

credit limit check statuses.

Also, the system doesn't include forwarding orders that have an invoicing status of Completely Invoiced or Over-invoiced.

## Forwarding Order

You usually don't enter a forwarding order ID. Usually you run the function to rebuild the credit exposure information in credit

management for a certain business partner or sales organization. If you enter forwarding orders, you must ensure that you enter

the full list of forwarding orders. Therefore, you use this field for exceptions, for example, to rebuild the credit exposure for a

particular forwarding order.

## Sales Organization

The sales organization of the forwarding order.

## Production Run

In a production run, the system uses the amounts in the forwarding order at that moment in time to update the credit exposure

amount in credit management. Based on the Test Run setting, the system displays the information in the following table as an

output:

System

## Displays

Credit Control

Business

Sales

Amount

## Currency

FWO Number Message ID

## Area

Partner ID

Organization

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

No

## Yes

Test Run

No

Production

Yes

## Run

## More Information

For more information about using a credit limit check with forwarding orders, see Credit Limit Check.

Creation and Transfer of Freight Settlement Documents using
Integration with MM External Services Management

## Use

You can automate the creation of freight settlement documents (FSDs). You can use this function instead of manually creating

FSDs in the launchpad.

Run the program /SCMTMS/SFIR_CREATE_BATCH. If you want the system to automatically transfer the settlement documents

to SAP ERP after creation, select the Post Immediately checkbox. If you do not automatically transfer settlement documents after

creation, you must run the program /SCMTMS/SFIR_TRANSFER_BATCH to transfer the settlement documents. For example, you

create settlement documents but then you want to transfer the settlement documents to SAP ERP in a structured way, twice a day.

You schedule the program /SCMTMS/SFIR_TRANSFER_BATCH to run in the background. This makes sure the system transfers

all settlements that are not blocked to SAP ERP.

## Integration

For more information about the integration of this function into the overall background processing, see Background Processing.

This is custom documentation. For more information, please visit SAP Help Portal.

122


1/14/26, 2:46 PM
## Prerequisites

## Freight Settlement Document

You have specified the appropriate settings for freight settlement (see Freight Settlement).

## Freight Settlement Document Types

You have assigned the FSD type to an appropriate freight order (FO) type in Customizing for Transportation Management under

Freight Order Management

## Freight Order

 Define Freight Order Types .

## Settlement Profiles and Calculation Profiles

You have specified the relevant freight settlement profiles and calculation profiles (see Freight Settlement).

## Internal Settlements

You have specified the appropriate settings for using resources with internal settlements (see Internal Settlement for Resources).

## Features

## Freight Settlement Documents

To create freight settlements, you specify Freight Settlement Document as the settlement document category. To specify the

freight orders that the system uses to create the settlements, you can enter either a selection profile or the document settings.

## Internal Settlement Documents

To create internal settlements, you specify Internal Settlement Document as the settlement document category. You can enter

either a selection profile or the document settings.

Change Process for Freight Settlements and SAP ERP Updates After Dispute Case Resolution

The system can take the following conditions into account when it creates a freight settlement document:

## Automatic change processing settings for a freight settlement

You can enable the automatic change process in the relevant settlement profile by specifying a freight settlement

document change process of either Create New FSD for Delta Amount or Reverse and Repost with New FSD.

The system uses the organization, or a combination of organization and business partner, to assign the settlement profile

to a freight document.

## Attribute changes in a freight document

The system flags a freight document as changed if you make the following changes after you have created a settlement

document:

Change the logistics information or charge information, and your change results in an update to the charges in the

freight document.

The system indicates the change on the Late Changes setting on the Charges and Internal Charges tab pages of

the freight document.

Change the agreement determination attributes of a freight document, for example, service level or changes in the

stages

This is custom documentation. For more information, please visit SAP Help Portal.

123


1/14/26, 2:46 PM

The change results in a new agreement or a new calculation sheet. The system changes the invoicing status of the

freight document to Not Up-to-Date.

You can specify the following freight settlement document creation settings in this background processing function:

## Include changed freight documents

The system creates freight settlement documents for all freight documents that have met one or more of the following

criteria:

## Invoicing status is Not Up-to-Date, Not Invoiced, or Partially Invoiced

Late Changes setting is specified on the Charges and Internal Charges tab pages of the freight documents, to

indicate the freight documents that you have changed

Dispute case status of the freight document is Resolved

## Exclude changed freight documents

The system does not create a freight settlement document for a freight document that you have changed, and instead

creates a freight settlement document for a freight document that has an invoicing status of Not Invoiced or Partially

Invoiced.

If the dispute case status of a freight document is Resolved, the system does not create a freight settlement document.

## Only changed freight documents

The system only creates a freight settlement document for a freight document that you have changed, where the freight

document has met one of the following criteria:

## Invoicing status is Not Up-to-Date

Late Changes setting is specified on the Charges and Internal Charges tab pages

Dispute case status of the freight document is Resolved

## Different Invoicing Carrier for Each Stage

This feature gives you the flexibility to create separate freight settlement documents for each of the invoicing carriers in a rail

freight document, where you have a different invoicing carrier for each stage in the document. For example, this enables you to

work with rule 11 business situations in North America.

If you enter a carrier in the Carrier/Service Provider field, the system selects the freight documents where the specified carrier is

the header carrier in the freight document. The header carrier is the carrier you specify in the  General Data

## Transportation

screen area of the freight document. In rule 11 situations, the header carrier receives the order from the customer and can execute

one or more of the stages.

If you enter a carrier in the Invoicing Carrier for Stage field, the system selects freight documents for the stages that have been

executed by the specified carrier.

If you enter a carrier in both the Carrier/Service Provider and the Invoicing Carrier for Stage fields, the system first chooses the

freight documents in which the carrier you specify in the Carrier/Service Provider field matches the header carrier in the freight

document. The system then creates freight settlement documents for the stages in the freight documents where the carrier you

enter in the Invoicing Carrier for Stage field matches the invoicing carrier. In rule 11 situations, the invoicing carrier is the carrier

who bills the customer for the shipment. This is the carrier you specify at stage level in the rail freight document. For more

information about rail freight documents, see Rail Transportation.

## Excluded Freight Documents

This is custom documentation. For more information, please visit SAP Help Portal.

124


1/14/26, 2:46 PM

The system does not automatically create settlement documents in the following circumstances:

If more than one settlement already exists for a freight document and you need to process a change in the freight

document

You create and transfer more than one freight settlement document for a freight document. Your carrier creates a dispute

case against some charge types or logistics quantities in the freight order that results in a change to the charge information

in the freight document.

The system does not know which of the existing settlement documents it should update in the automatic background

process. It displays an error. You must manually choose the appropriate settlement on the user interface (UI) and calculate

charges again. You can then create the settlement.

If an existing freight settlement document has a lifecycle status of Transferred for Accruals or Cancellation Requested.

When a settlement document has one of these statuses, Transportation Management (TM) is awaiting a response from

SAP ERP. TM does not know whether the transfer or cancellation have been successful, and cannot create a settlement

document.

## Settlement Date

You can specify the date the system uses as the settlement date for freight settlement documents. If you do not enter a settlement

date, the system uses today’s date as the default. You can use BAdI: Determination of the Settlement Date for Freight Orders to

propose a date as the settlement date. For more information, see Customizing for Transportation Management under  Business

Add-Ins (BAdIs) for Transportation Management

## Settlement

 Freight Settlement

.

## Zero or Negative Amounts and Calculation Errors

The system deletes all the settlements that have a zero or negative invoiced amount when it runs the background processing

function.

## Selection Profile

You can define a selection profile to work with a subset of the settlements that need to be created and transferred. You can create

and edit profiles in on the launchpad under  Application Administration

## Planning

 Selection Profiles .

Message Display

## Detailed Messages

The system displays the following information after you create and transfer settlement documents:

List of orders for which it did not create settlement documents, and the reasons why it did not create the

settlements

Number of settlement documents created

## List of settlement documents created

If you select the Detailed Messages checkbox, the system displays additional details on-screen. For example, it displays the

input parameters you entered, the service date for each settlement, and the orders included in the settlements. The system

includes the additional details in the Analyze Application Log transaction (SLG1) regardless of whether you select the

Detailed Messages checkbox. The system creates the application log when you create and transfer settlement documents

in production mode (when you do not select the Run in Simulation Mode checkbox).

## Log Messages About Calculation Sheets

If you select the Log Calc. Sheet Messages (Log Calculation Sheet Messages) checkbox, the system displays the relevant

messages for each charge item in the Charge Analysis Log tab page of the settlement document. The system only displays

This is custom documentation. For more information, please visit SAP Help Portal.

125


1/14/26, 2:46 PM

these messages if charges have been calculated for the settlement document.

## Parallel Processing Profile

You can specify the technical processing conditions the system uses to process the function, such as application server usage and

queue time. You can create and edit profiles on the launchpad under  Application Administration

 General Settings

## Define

Parallel Processing Profile (/SCMTMS/PPRF)

.

## Package Size

You can define the maximum number of orders that the system processes for settlement creation in a processing step. This

enables you to optimize the system runtime and resource utilization when the system executes the background processing

function. For example, you specify 100 as your package size. You have 250 orders ready for settlement document creation. The

system creates the settlements in steps, processing a maximum of 100 orders in each step. In this case, the settlement process

runs in 3 iteration steps to complete the processing of the 250 orders.

Creation and Transfer of Freight Settlement Documents using
## Integration with Lean Services

Instead of manually creating freight settlement documents (FSDs) from the launchpad, you can automate them using the program

/SCMTMS/SFIR_CREATE_BATCH.

## Prerequisites

## Freight Settlement Document

You've specified the appropriate settings for freight settlement (see Freight Settlement Integration using Lean Services).

You've also confirmed the freight cost and freight documents must be in the Ready for Posting status.

## Freight Settlement Document Types

You've assigned the FSD type to an appropriate freight order (FO) type in Customizing for Transportation Management under

Freight Order Management

## Freight Order

 Define Freight Order Types .

## Settlement Profiles and Calculation Profiles

You've specified the relevant freight settlement profiles and calculation profiles (see Freight Settlement Integration using Lean

Services).

## Internal Settlements

You've specified the appropriate settings for using resources with internal settlements (see Internal Settlement for Resources).

## Use

When you run the program /SCMTMS/SFIR_CREATE_BATCH, the system creates and posts the FSDs to SAP ERP automatically.

And as the system creates and posts the FSDs automatically, so selecting the checkbox Post Immediately doesn't have any

impact on the process.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

126


1/14/26, 2:46 PM

The system doesn't consider the value Collective for the setting  Processing Setting

  Invoice Creation Method  as by

default, the system creates and posts individual FSDs.

You run the program /SCMTMS/SFIR_TRANSFER_BATCH if there are some FSDs that aren't posted when you ran the

/SCMTMS/SFIR_CREATE_BATCH program as they're blocked.

## Integration

For more information about the integration of this function into the overall background processing, see Background Processing.

## Features

## Freight Settlement Documents

To create freight settlements, you specify Freight Settlement Document as the settlement document category. To specify the

freight orders that the system uses to create the settlements, you can enter either a selection profile or the document settings.

## Internal Settlement Documents

To create internal settlements, you specify Internal Settlement Document as the settlement document category. You can enter

either a selection profile or the document settings.

Managing Changes for Freight Settlements and SAP ERP Updates

The system considers the following when it creates a freight settlement document:

## Handling changes for freight settlement

The change process strategy for that you've defined in the Customizing activity for Transportation Management under

## Settlement

  Define Settlement Profile  isn't considered for freight settlement integration using lean services.

For freight settlement integration using lean services, the system identifies the change process based on the nature of

change to the charge line. For more information, see Flexibility in Freight Charge Changes.

The system doesn't consider the settings that you've specified in the section Creation Approach for Changed Freight

Documents in this program.

## Attribute changes in a freight document

The system flags a freight document as changed if you make the following changes after you've created a settlement

document:

Change the logistics information or charge information, and that change results in an update to the charges in the

freight document.

Change the agreement determination attributes of a freight document, for example, service level or changes in the

stages

## Different Invoicing Carrier for Each Stage

This feature gives you the flexibility to create separate freight settlement documents for each of the invoicing carriers in a freight

document, where you have a different invoicing carrier for each stage in the document. For example, this enables you to work with

rule 11 business situations in North America and manage multimodal transportation scenarios.

If you enter a carrier in the Carrier/Service Provider field, the system selects the freight documents where the specified carrier is

the header carrier in the freight document. The header carrier is the carrier that you specify in the  General Data

This is custom documentation. For more information, please visit SAP Help Portal.

127


1/14/26, 2:46 PM

 Transportation  screen area of the freight document. In rule 11 situations, the header carrier receives the order from the

customer and can execute one or more of the stages.

If you enter a carrier in the Invoicing Carrier for Stage field, the system selects freight documents for the stages that have been

executed by the specified carrier.

If you enter a carrier in both the Carrier/Service Provider and the Invoicing Carrier for Stage fields, the system first chooses the

freight documents in which the carrier you specify in the Carrier/Service Provider field matches the header carrier in the freight

document. The system then creates freight settlement documents for the stages in the freight documents where the carrier that

you enter in the Invoicing Carrier for Stage field matches the invoicing carrier. In rule 11 situations, the invoicing carrier is the

carrier who bills the customer for the shipment. This is the carrier that you specify at stage level in the rail freight document or a

freight booking with multimodal transportation. For more information about rail freight documents, see Rail Transportation and for

multimodal see Ocean Freight Bookings for Shippers (Outbound) and Air Freight Bookings for Shippers (Outbound).

## Settlement Date

When you create and post a freight settlement document, by default the system uses the date from the relevant Event for Freight

Cost Confirmation as the settlement date and doesn't consider the date that you've specified as the Invoice Date under

Document Settings.

You can override the system default date by implementing BAdI: Determination of Settlement Date for Freight Settlement

Documents. The system uses the settings that you specify in this BAdI to determine the settlement creation date. For more

information, see Customizing for Transportation Management under  Business Add-Ins (BAdIs) for Transportation

Management

## Settlement

 Freight Settlement

.

## Selection Profile

You can define a selection profile to work with a subset of the settlements that need to be created and transferred. You can create

and edit profiles in on the launchpad under  Application Administration

## Planning

 Selection Profiles .

Message Display

## Detailed Messages

The system displays the following information after you create and transfer settlement documents:

List of orders for which it didn't create settlement documents, and the reasons why it didn't create the settlements

Number of settlement documents created

## List of settlement documents created

If you select the Detailed Messages checkbox, the system displays additional details on-screen. For example, it displays the

input parameters you entered, the service date for each settlement, and the orders included in the settlements. The system

includes the additional details in the Analyze Application Log transaction (SLG1) regardless of whether you select the

Detailed Messages checkbox. The system creates the application log when you create and transfer settlement documents

in production mode (when you don't select the Run in Simulation Mode checkbox).

## Log Messages About Calculation Sheets

If you select the Log Calc. Sheet Messages (Log Calculation Sheet Messages) checkbox, the system displays the relevant

messages for each charge item in the Charge Analysis Log tab page of the settlement document. The system only displays

these messages if charges have been calculated for the settlement document.

## Parallel Processing Profile

This is custom documentation. For more information, please visit SAP Help Portal.

128


1/14/26, 2:46 PM

You can specify the technical processing conditions the system uses to process the function, such as application server usage and

queue time. You can create and edit profiles on the launchpad under  Application Administration

 General Settings

## Define

Parallel Processing Profile (/SCMTMS/PPRF)

.

## Package Size

You can define the maximum number of orders that the system processes for settlement creation in a processing step. This

enables you to optimize the system runtime and resource utilization when the system executes the background processing

function. For example, you specify 100 as your package size. You have 250 orders ready for settlement document creation. The

system creates the settlements in steps, processing a maximum of 100 orders in each step. In this case, the settlement process

runs in 3 iteration steps to complete the processing of the 250 orders.

Confirming the Resolution of Freight Settlement Dispute Cases

## Use

This function enables you to confirm the resolution status of freight settlement dispute cases in batches in the background. Run

the program /SCMTMS/SET_CARRIER_RELEVANCE.

You are a shipper and you allow your carriers to submit invoices using enterprise services. Your carrier creates an invoice

document in their external system and uses enterprise services to send you the invoice. The enterprise service creates a carrier

invoice in the TM module of your SAP S/4 HANA system.

Your carrier may have included additional unplanned freight costs or may have different charges to what you expect to pay in your

freight order. Your TM system automatically evaluates the external invoice. It automatically creates a dispute case when your

service provider submits an invoice that contains different values to what you expect. The system captures these differences in a

dispute case. The system captures the individual differences in charges as dispute items. To reduce your administration

commitments, you have specified tolerance settings so that the system automatically accepts some dispute cases,

On the execution of the tolerance rules, the system resolves the respective dispute items. However, you may want to review the

dispute cases so that you can monitor the tolerances by individually reviewing each dispute case. You can use this function to

finalize the resolution status of the dispute case in a separate step in the background.

You can enable this function when you set up your freight settlement dispute management process. You can then confirm the

resolution status of each dispute case that was automatically approved by the tolerance rules.

## Integration

For more information about the integration of this function into the overall background processing, see Background Processing.

## Prerequisites

You have enabled a tolerance group for a freight settlement profile in Customizing for Transportation Management under

## Settlement

 Define Settlement Profile

 Dispute Management Settings .

You have used this freight settlement profile to create the relevant freight orders for your carrier.

You have specified the following dispute case settings in Customizing for Transportation Management under  Settlement

## Freight Settlement

 Freight Settlement Dispute Management

:

## Dispute case reason codes and types

This is custom documentation. For more information, please visit SAP Help Portal.

129


1/14/26, 2:46 PM

Tolerance rules

## Features

You can enter a range of freight dispute cases or freight orders, or both freight dispute cases and freight orders.

Posting of Carrier Invoices

## Use

This function enables you to post the carrier invoices that are ready for posting in Transportation Management (TM) to materials

management (MM) as an incoming invoice. Run the program /SCMTMS/CAR_INV_POST_BATCH.

## Integration

For more information about the integration of this function into the overall background processing, see Background Processing.

## Prerequisites

## For Freight Settlement Integration with MM using External Services

You've specified the charge types for tax by enabling the Tax setting in the Define Charge Types Customizing activity under

Transportation Management

 Basic Functions

 Charge Calculation

 Basic Settings .

You've assigned the tax code to the TM charge type in the Assign Tax Code to Charge Types Customizing activity under

Transportation Management

## Integration

## Enterprise Services

 Carrier Invoice Integration . The system uses this

setting when it posts the carrier invoice to an internal MM system.

To post the carrier invoice to an external MM system running on SAP S/4HANA or SAP ERP, you have specified the mapping

settings in the Map SAP TM Tax Settings Customizing activity under

Integration with Other SAP Components

 Transportation Management

 Invoice Integration

 Tax .

You've met the following conditions for the carrier invoice document:

No dispute case exists, or the dispute case has a life cycle status of Resolved

## Has a life cycle status of other than Rejected

All associated freight orders have the invoicing status Completely Invoiced

All associated freight settlement documents have the life cycle status Accruals Posted

Has a block status of Not Blocked

## Has a consistency status of Consistent

For Freight Settlement Integration with MM using Lean Services

You've met the following conditions for the carrier invoice document:

No dispute case exists, or the dispute case has a life cycle status of Resolved

Has a life cycle status of other than Rejected

All associated freight orders have the invoicing status Posted

This is custom documentation. For more information, please visit SAP Help Portal.

130


1/14/26, 2:46 PM

All associated freight settlement documents have the life cycle status Accruals Posted

Has a block status of Not Blocked

Has a consistency status of Consistent

Features

## Invoice Date

You can specify the invoice date, or the invoice date range, that the system uses to select carrier invoices for posting to MM. For

example, you can post all carrier invoices that contain a particular invoice date.

## Detailed Messages

The system displays the following information after you post carrier invoices:

List of carrier invoices that the system didn't post to MM, and the reasons why it didn't post the invoices

## List of invoices posted to MM

If you select the Detailed Messages checkbox, the system displays additional details on-screen. For example, it displays the input

parameters you entered. The system includes the additional details in the Analyze Application Log transaction (SLG1) regardless

of whether you select the Detailed Messages checkbox. The system creates the application log when you post invoices in

production mode (when you don't select the Run in Simulation Mode checkbox).

## Parallel Processing Profile

You can specify the technical processing conditions the system uses to process the function, such as application server usage and

queue time. To define parallel processing profiles, on the SAP Easy Access screen, choose  Logistics

 Transportation

## Management

## Current Settings

 Define Parallel Processing Profile .

## Package Size

You can group invoices in defined package sizes for parallel processing. For example, if you can have 500 carrier invoices in a run

and you enter a package size of 100, the system posts your carrier invoices in 5 parallel sessions that each contain 100 carrier

invoices.

Display Agreements with Issues in Charge Types

## Use

This function enables you to automate the display of agreements that have the following issues with respect to its charge types.

Run the program /SCMTMS/GET_EXTCHK_AGR_BO_DOC to identify the following issues in charge types with various agreement

types:

Calculation sheet items with same charge types and same resolution base

## Negative or Positive/Negative indicator for independent charge types

This report validates the issues in the agreements only when you've not selected the Disable Extended Check for Charge Types in

Agrmt. Management checkbox.

This is custom documentation. For more information, please visit SAP Help Portal.

131


1/14/26, 2:46 PM

You can do that from the Customizing for Transportation Management under  Basic Functions

 General Settings

## Define

General Settings for TM .

## Integration

For more information about the integration of this function into the overall background processing, see Background Processing.

Features

## Category

You can select from the following types of agreements to see if they have the above-mentioned issues with their setup:

Freight agreements

Internal agreements

## Forwarding agreements

Forwarding Agreement Quotation and Assignment

Freight Agreement RFQ Master

Service Product Catalogue

## Parallel Processing Profile

You can specify the technical processing conditions the system uses to process the function, such as application server usage and

queue time. To define parallel processing profiles, on the SAP Easy Access screen, choose  Logistics

 Transportation

## Management

## Current Settings

 Define Parallel Processing Profile .

## Package Size

You can group agreements in defined package sizes for parallel processing. For example, if you can have 500 agreements in a run

and you enter a package size of 100, the system posts your agreements in 5 parallel sessions that each contain 100 agreements.

## Related Information

Validation of Charge Types in Agreement Management

Definition of Parallel Processing Profiles

## Use

You can use this function to define parallel processing profiles. You can specify these profiles for background processing, for

example, and by doing so improve performance. To do this, the system groups the data in packages. The system can assign each

package to a separate parallel work process. You can perform background processing using a parallel processing profile both in the

background and interactively.

## Features

In the parallel processing profile, you define the following, for example:

This is custom documentation. For more information, please visit SAP Help Portal.

132


1/14/26, 2:46 PM

## Server group

Resource on which you perform background processing

## Maximum number of work processes

Maximum number of work processes that the system is allowed to use for background processing

## Package size

Maximum number of objects in a package that is processed by a work process

## Wait time

Time (in seconds) that the system waits until resources are available for further processing

## Activities

To define parallel processing profiles, on the SAP Easy Access screen, choose  Logistics

 Transportation Management

## Current Settings

 Define Parallel Processing Profile .

Output Management

## Use

You can use output management to print, fax, and email documents such as order, delivery, and billing information. You can also

execute application-to-application or business-to-business actions. You can use output management features in the following

business documents:

Forwarding orders

Forwarding quotations

Freight orders

Freight bookings

Freight units

Container units

Forwarding agreements

Forwarding agreement quotations

## Freight agreements

Freight agreement RFQ masters

Freight settlements

## Forwarding settlements

Internal settlements you have created using forwarding settlement types

## Freight settlement dispute case

The following are the main output management features:

## Display an action such as a settlement document

This is custom documentation. For more information, please visit SAP Help Portal.

133


1/14/26, 2:46 PM

Choose the output method such as print, fax, and email

Preview a document

Enter an attachment

Enter a note

## Enter a recipient

## Execute the action, such as printing and faxing a settlement document

You can also regenerate and execute an action that you have already executed. For example, you can reprint a business document

that you have already printed. When you regenerate an action, you can change the attributes, for example, the recipients.

The system also displays the status of an action after execution. If a particular action was not processed successfully, the system

displays the cause of the error.

In the Output Management tab page of the Maintain Business Partner transaction (transaction BP), you can disable the features

such as external communication, method calls, alerts and workflows of an action definition for a business partner.

You can use delegated actions to reuse standard PPF output actions in a PPF output profile, without having to write additional

coding. Delegated actions are standard actions, such as outbound agent classes, that allow reuse. You can create multiple PPF

profiles customized to your needs and specify standard output actions as delegated actions. For more information see

Customizing for Cross-Application Components under  Processes and Tools for Enterprise Applications

## Reusable Objects

and Functions for BOPF Environment

 PPF Adapter for Output Management

 Maintain Output Management Adapter Settings

.

## Prerequisites

In Customizing for Cross-Application Components under  Processes and Tools for Enterprise Applications

## Reusable Objects

and Functions for BOPF Environment

 PPF Adapter for Output Management

, you have specified the following settings:

1. Defined actions and assigned them to action profiles in the Customizing activity Maintain PPF Settings

2. Assigned action profiles to business objects, such as forwarding orders and forwarding quotations, in the Customizing

activity Maintain Output Management Adapter Settings. These action profiles are available to the user in the output

management tab page of a business document.

In addition to the action profile you have assigned to a business object, you can also assign action profiles to a document type of a

business document. You enter the action profiles in the Output Profile and Additional Output Profile fields for the following

business document types in Customizing for Transportation Management:

Forwarding orders under  Forwarding Order Management

## Forwarding Order

## Define Forwarding Order Types

Forwarding quotations under  Forwarding Order Management

 Forwarding Quotation

 Define Forwarding Quotation

## Types

Freight orders under  Freight Order Management

## Freight Order

## Define Freight Order Types

Freight bookings under  Freight Order Management

## Freight Booking

 Define Freight Booking Types

Freight units under  Planning

## Define Freight Unit Types

Container units under  Freight Order Management

## Transportation Unit

 Define Transportation Unit Types

Forwarding settlements under  Settlement

## Forwarding Settlement

 Define Forwarding Settlement Document Types

Freight settlements under  Settlement

## Freight Settlement

## Define Freight Settlement Document Types

This is custom documentation. For more information, please visit SAP Help Portal.

134


1/14/26, 2:46 PM

Dispute case type under  Settlement

## Freight Settlement

 Freight Settlement Dispute Management

## Define Dispute

Case Reason Codes and Types

## Example

1. In the Customizing activity Maintain PPF Settings you have performed the following steps:

Created action A and B, and assigned it to action profile X

## Created action C and D, and assigned it to action profile Y

2. In the Customizing activity Maintain Output Management Adapter Settings, you have assigned action profile X to the

business object of forwarding order.

3. In the Customizing activity Define Forwarding Order Types, you have entered action profile Y in the Output Profile field for

the forwarding order type M.

When you create a forwarding order with forwarding order type M, the action profile X with actions A and B, and the action profile Y

with actions C and D are available in the output management tab page.

More Information

## Printing

SAP Library for SAP Supply Chain Management on SAP Help Portal at http://help.sap.com/scm . Under SAP SCM Server

application help, open SAP Library and choose  Processes and Tools for Enterprise Applications

 Reusable Objects and

Functions for the BOPF Environment (CA-EPT-BRC)

Printing

## Use

In Transportation Management (TM), you can print the following documents:

Business Document

Print Document

Freight booking

## Freight order

Cargo manifest (with addresses)

Cargo manifest (without addresses)

Security manifest

Master air waybill label

House sea bill of lading

## Master air waybill

Combined label (for air freight bookings only)

(Un)Loading instruction

Road waybill (with your own trucks, Europe)

Road waybill (with your own trucks, USA)

This is custom documentation. For more information, please visit SAP Help Portal.

135


1/14/26, 2:46 PM

Business Document

Print Document

Forwarding order

Forwarding quotation

Freight settlement document

Transportation labels

FIATA forwarding instructions

## Shipping manifest

(Un)Loading instruction (Load Plan)

House air waybill label

## Forwarding order

Forwarding order confirmation

House air waybill

Forwarding quotation

Freight settlement document

Freight settlement dispute case

## Dispute case

Forwarding settlement document

Forwarding settlement document

Freight agreement

Forwarding agreement

Internal agreement

Credit memo

## Features

Automated Output

Freight agreement

Forwarding agreement

Internal agreement

## Credit memo

Automated output of print documents is scheduled and executed according to the business scenarios and life cycle status of the

corresponding business documents. When a business document has the required status and the user saves the document, the

system automatically creates an entry on the Output Management tab and prints the relevant print document. Note that if the

user changes the business document and it still has the relevant status, the system prints the required document again. You can

change the status that triggers the automated output of a print document by changing the Post Processing Framework (PPF)

profile.

In the standard system, you can use automated output for print documents that are based on freight orders, freight bookings,

forwarding orders, and forwarding quotations. The relevant statuses are as follows:

Forwarding orders:

This is custom documentation. For more information, please visit SAP Help Portal.

136


1/14/26, 2:46 PM

## Forwarding order: Life cycle status New

Forwarding order confirmation: Confirmation status Confirmed

Forwarding quotations: Life cycle status Submitted.

## Immediate Printing

Immediate printing enables you to print a document manually from the Output Management tab. You can manually print the

following documents regardless of their status:

Forwarding agreements, freight agreements, and internal agreements

Forwarding settlement documents and freight settlement documents

## Credit memos

You can manually print documents based on freight orders, freight bookings, forwarding orders, and forwarding quotations only if

the relevant business document has the required status. The status required for immediate printing is the same as the status

required for automated output.

## Custom Print Forms

The system generates a print document using a print form. If required, you can change the standard print forms to suit your

requirements or create your own print forms.

For more information, see Creating Custom Print Forms.

## Print Forms for Air Waybills

You can use the following print forms for house air waybills and master air waybills:

## Print form for printing one original at a time on blank paper

The system prints the form layout and the values. If you need more than one document, you must trigger printing as many

times as required.

## Print form for printing multiple originals and copies on blank paper

The system prints the form layout and the values. The system prints three originals and five copies. The documents are

numbered. The number and the document use are printed at the bottom of the page, for example, Original 3 (for Shipper).

The system also prints the carrier’s limitation of liability on the even pages.

## Print form for printing one original at a time on a blank form

The system prints the values on the blank form. If you need more than one original, you must trigger printing as many times

as required.

The first option is already set up in the standard system. To use the second or third option, you must replace the existing form with

the form for the required option. For more information, see SAP Notes 1930333

 and 2017074

.

Configuration of Printing

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

137


1/14/26, 2:46 PM

The printing of documents in Transportation Management (TM) is controlled by settings in the Post Processing Framework (PPF)

and by Customizing settings in the TM system. These settings are provided for the standard print documents. In addition, the

following action profiles are provided, including the assignment of the action profiles to the relevant print documents:

Action Profile

Print Document

/SCMTMS/TOR_PRINT_AIR

/SCMTMS/TOR_PRINT_ROAD

## Cargo manifest

Cargo manifest with addresses

Security manifest

Master air waybill

## Master air waybill label

Road waybill (with your own trucks, Europe) *

Road waybill (with your own trucks, USA)

Transportation labels

FIATA forwarding instructions

Shipping manifest

## Load plan

ADR dangerous goods note *

US bill of lading *

Canadian bill of lading *

/SCMTMS/TOR_PRINT_RAIL

RID dangerous goods note *

/SCMTMS/TOR_PRINT_SEA

House sea bill of lading

Master bill of lading *

IMO dangerous goods declaration *

/SCMTMS/TRQ_FWO_PRINT

Forwarding order and forwarding order confirmation

/SCMTMS/TRQ_FWQ_PRINT

Forwarding quotation

/SCMTMS/SFIR_PRINT

Pro-forma supplier freight invoice request

Dispute case

/SCMTMS/CFIR_PRINT

Pro-forma customer freight invoice request

/SCMTMS/FAG_PRINT

/SCMTMS/CM_PRINT

/SCMTMS/TOR_PRINT _AIR_FU

Forwarding agreement, freight agreement, and internal agreement

## Credit memo

House air waybill

House air waybill label

/SCMTMS/TRQ_PRINT _AIR

## None

This is custom documentation. For more information, please visit SAP Help Portal.

138


1/14/26, 2:46 PM

*= Containing dangerous goods information based on Product Compliance only

## Activities

To ensure that the configuration is correct, check the following:

The required output management settings have been made in Customizing for Cross-Application Components under

Processes and Tools for Enterprise Applications

 Reusable Objects and Functions for BOPF Environment

## PPF Adapter

for Output Management

 Maintain PPF Settings  and Maintain Output Management Adapter Settings.

The relevant action profiles have been assigned to the document types in Customizing for Transportation Management:

Forwarding order:  Forwarding Order Management

## Forwarding Order

## Define Forwarding Order Types

Forwarding quotation:  Forwarding Order Management

 Forwarding Quotation

 Define Forwarding Quotation

## Types

Freight order:  Freight Order Management

## Freight Order

## Define Freight Order Types

Freight booking:  Freight Order Management

## Freight Booking

 Define Freight Booking Types

Container unit:  Freight Order Management

## Transportation Unit

 Define Transportation Unit Types

Freight settlement document:  Settlement

## Freight Settlement

 Define Freight Settlement Document Types

Forwarding settlement document:  Settlement

 Forwarding Settlement

 Define Forwarding Settlement

## Document Types

Credit memos for forwarding orders:  Settlement

 Forwarding Settlement

 Define Credit Memo Reason Codes

and Types for Forwarding SDs

Credit memos for freight orders:  Settlement

## Freight Settlement

 Define Credit Memo Reason Codes and

Types for Freight SDs

## More Information

For information about adapting the standard print forms to your requirements, see Creating Custom Print Forms.

## Standard Print Forms

The delivered print forms for SAP Output Management in Transportation Management are standardized templates provided to

support the production of transportation-specific documents. These templates are intended to streamline the generation and

handling of documents that are required in transportation processes.

The delivered print forms are configured to display the relevant data maintained in your S/4HANA system in the appropriate fields.

While SAP provides these predefined print forms to address common regulatory and operational requirements, you can create and

implement your own custom document templates, allowing them to adapt to specific business processes or regional regulations

as needed. For more information, see Creating Custom Print Forms.

## Example Documents

SAP provides standard templates for all documents that you can create using SAP Output Management. The following list is not

exhaustive but provides examples of the delivered documents:

This is custom documentation. For more information, please visit SAP Help Portal.

139


1/14/26, 2:46 PM

## ADR Dangerous Goods Note

This note is relevant in jurisdictions subject to the UNECE Agreement of 30 September 1957 concerning the International
Carriage of Dangerous Goods by Road. SAP provides a default template that you can use to print this document.

## RID Dangerous Goods Note

This note is relevant in jurisdictions subject to the UNECE Regulation concerning the International Carriage of Dangerous
Goods by Rail (RID). SAP provides a default template that you can use to print this document.

## IMO Dangerous Goods Declaration

This note is relevant in jurisdictions subject to the International Maritime Dangerous Goods (IMDG) Code issued by the
International Maritime Organization (IMO). SAP provides a default template that you can use to print this document.

Bill of Lading (USA)

This note is relevant in jurisdictions subject to U.S. transportation regulations. SAP provides a default template that you can
use to print this document.

Bill of Lading (Canada)

This note is relevant in jurisdictions subject to Canadian transportation regulations. SAP provides a default template that
you can use to print this document.

## ADR Dangerous Goods Note

This note is relevant in jurisdictions subject to the UNECE Agreement of 30 September 1957 concerning the International Carriage

of Dangerous Goods by Road. SAP provides a default template that you can use to print this document.

## Prerequisites

You can print this document from a freight order.

The document is only produced when products in the freight order are classified as dangerous goods. Whether goods are

classified as dangerous goods is determined by Product Compliance. For more information, see Dangerous Goods

Processing Based on Product Compliance.

## Default Template

The default template for this document looks like this:

This is custom documentation. For more information, please visit SAP Help Portal.

140


1/14/26, 2:46 PM

This is custom documentation. For more information, please visit SAP Help Portal.

141


1/14/26, 2:46 PM

  Note

The exact format and content of an ADR dangerous goods note can vary depending on your implementation. This image is of

the default template delivered by SAP.

## System Data

When generating the form for printing, the system copies data from the freight order to the output document. To enable this

transfer, you must maintain values in specific fields of the freight order. When you generate the print form, the system adds the

following information to the form:

  Note

Any fields which aren't listed in this table aren't filled by the system by default. A system administrator can configure the

system to add additional data by creating custom print forms. For more information, see Creating Custom Print Forms.

## Print Form Field

1. Shipper/Consignor/Vendor

2. Transport Document Number

4. Shipper's Reference

6. Consignee

7. Carrier

9. Additional Handling Information

## System Data

This field contains the data maintained in

the Shipper field in the freight order.

You can see and edit the shipper in the

freight order, on the Business Partner tab.

This field contains the freight order number

of the freight order that the document was

created from.

You can't edit this field. The data shown is

the same as in field 4.

This field contains the freight order number

of the freight order that the document was

created from.

You can't edit this field. The data shown is

the same as in field 2.

This field contains the data maintained in

the Ship-to Party field in the freight order.

You can see and edit the ship-to party in the

freight order, on the Business Partner tab.

  Note

If you have multiple consignees in the

freight order, the system generates one

document for each consignee.

This field contains the data maintained in

the Carrier field in the freight order.

You can see and edit the carrier in the

freight order, on the Business Partner tab.

This field contains the text of the Sender's

Instruction (CMR Freight Doc.) note.

This is custom documentation. For more information, please visit SAP Help Portal.

142


1/14/26, 2:46 PM

## Print Form Field

11. Port/Place of Loading

12. Port/Place of Discharge

14. Shipping Marks

22. Company Name of the Shipper Preparing this Note

Place and Date

## System Data

You can see and edit the Sender's

Instruction (CMR Freight Doc.) note in the

freight order, on the Notes tab.

You can add a note, in the freight order, on

the Notes tab, by inserting a new note and

selecting Sender's Instruction (CMR

Freight Doc.) as the text type.

This field contains the city and country of

the shipping/receiving point address where

the goods in the ADR note were loaded.

This information is determined

automatically. You can't edit this field. You

can see the data maintained for the place of

loading in the freight order, on the Overview

tab, in the row above the loading activity.

You can double-click the table row to view

details of the address.

This field contains the city and country of

the shipping/receiving point address where

the goods in the ADR note were unloaded.

This information is determined

automatically. You can't edit this field. You

can see the data maintained for the place of

discharge in the freight order, on the

Overview tab, in the row above the

unloading activity. You can double-click the

table row to view details of the address.

This field contains the products in the

freight order that are classified as

dangerous goods.

To add or remove products to or from the

list, make sure they're correctly configured.

For more information, see Dangerous

Goods Processing Based on Product

Compliance.

This field contains the data maintained in

the Name field of the shipper in the freight

order.

You can't edit this field. You can see the

shipper in the freight order, on the Business

Partner tab.

This field contains the data maintained in

the Departure Date field of the freight

order.

You cannot edit this field. You can see the

departure date in the freight order, on the

General tab.

This is custom documentation. For more information, please visit SAP Help Portal.

143


1/14/26, 2:46 PM

## RID Dangerous Goods Note

This note is relevant in jurisdictions subject to the UNECE Regulation concerning the International Carriage of Dangerous Goods by

Rail (RID). SAP provides a default template that you can use to print this document.

## Prerequisites

You can print this document from a freight order.

The document is only produced when products in the freight order are classified as dangerous goods. Whether goods are

classified as dangerous goods is determined by Product Compliance. For more information, see Dangerous Goods

Processing Based on Product Compliance.

## Default Template

This is custom documentation. For more information, please visit SAP Help Portal.

144


1/14/26, 2:46 PM

The default template for this document looks like this:

This is custom documentation. For more information, please visit SAP Help Portal.

145


1/14/26, 2:46 PM

  Note

The exact format and content of an RID dangerous goods note can vary depending on your implementation. This image is of the

default template delivered by SAP.

## System Data

When generating the form for printing, the system copies data from the freight order to the output document. To enable this

transfer, you must maintain values in specific fields of the freight order. When you generate the print form, the system adds the

following information to the form:

  Note

Any fields which aren't listed in this table aren't filled by the system by default. A system administrator can configure the

system to add additional data by creating custom print forms. For more information, see Creating Custom Print Forms.

## Print Form Field

1. Shipper/Consignor/Vendor

2. Transport Document Number

4. Shipper's Reference

6. Consignee

7. Carrier

9. Additional Handling Information

## System Data

This field contains the data maintained in

the Shipper field in the freight order.

You can see and edit the shipper in the

freight order, on the Business Partner tab.

This field contains the freight order number

of the freight order that the document was

created from.

You can't edit this field. The data shown is

the same as in field 4.

This field contains the freight order number

of the freight order that the document was

created from.

You can't edit this field. The data shown is

the same as in field 2.

This field contains the data maintained in

the Ship-to Party field in the freight order.

You can see and edit the ship-to party in the

freight order, on the Business Partner tab.

  Note

If you have multiple consignees in the

freight order, the system generates one

document for each consignee.

This field contains the data maintained in

the Carrier field in the freight order.

You can see and edit the carrier in the

freight order, on the Business Partner tab.

This field contains the text of the Sender's

Instruction (CMR Freight Doc.) note.

This is custom documentation. For more information, please visit SAP Help Portal.

146


1/14/26, 2:46 PM

## Print Form Field

11. Port/Place of Loading

12. Port/Place of Discharge

14. Shipping Marks

22. Company Name of the Shipper Preparing this Note

Place and Date

## System Data

You can see and edit the Sender's

Instruction (CMR Freight Doc.) note in the

freight order, on the Notes tab.

You can add a note, in the freight order, on

the Notes tab, by inserting a new note and

selecting Sender's Instruction (CMR

Freight Doc.) as the text type.

This field contains the city and country of

the shipping/receiving point address where

the goods in the RID note were loaded.

This information is determined

automatically. You can't edit this field. You

can see the data maintained for the place of

loading in the freight order, on the Overview

tab, in the row above the loading activity.

You can double-click the table row to view

details of the address.

This field contains the city and country of

the shipping/receiving point address where

the goods in the RID note were unloaded.

This information is determined

automatically. You can't edit this field. You

can see the data maintained for the place of

discharge in the freight order, on the

Overview tab, in the row above the

unloading activity. You can double-click the

table row to view details of the address.

This field contains the products in the

freight order that are classified as

dangerous goods.

To add or remove products to or from the

list, make sure they're correctly configured.

For more information, see Dangerous

Goods Processing Based on Product

Compliance.

This field contains the data maintained in

the Name field of the shipper in the freight

order.

You can't edit this field. You can see the

shipper in the freight order, on the Business

Partner tab.

This field contains the data maintained in

the Departure Date field of the freight

order.

You cannot edit this field. You can see the

departure date in the freight order, on the

General tab.

This is custom documentation. For more information, please visit SAP Help Portal.

147


1/14/26, 2:46 PM

## IMO Dangerous Goods Declaration

This note is relevant in jurisdictions subject to the International Maritime Dangerous Goods (IMDG) Code issued by the

International Maritime Organization (IMO). SAP provides a default template that you can use to print this document.

## Prerequisites

You can print this document from the pickup freight order of an ocean freight booking.

The document is only produced when products in the freight booking are classified as dangerous goods. Whether goods are

classified as dangerous goods is determined by Product Compliance. For more information, see Dangerous Goods

Processing Based on Product Compliance.

## Default Template

This is custom documentation. For more information, please visit SAP Help Portal.

148


1/14/26, 2:46 PM

The default template for this document looks like this:

This is custom documentation. For more information, please visit SAP Help Portal.

149


1/14/26, 2:46 PM

  Note

The exact format and content of an IMO dangerous goods declaration can vary depending on your implementation. This image

is of the default template delivered by SAP.

## System Data

When generating the form for printing, the system copies data from the freight order to the output document. To enable this

transfer, you must maintain values in specific fields of the freight order. When you generate the print form, the system adds the

following information to the form:

  Note

Any fields which aren't listed in this table aren't filled by the system by default. A system administrator can configure the

system to add additional data by creating custom print forms. For more information, see Creating Custom Print Forms.

Print Form Field

## System Data

1. Shipper/Consignor/Vendor

This field contains the data maintained in the Shipper field in the

freight order.

You can see and edit the shipper in the freight order, on the

Business Partner tab.

2. Transport Document Number

This field contains the freight order number of the freight order

that the document was created from.

You can't edit this field.

5. Freight Forwarder's Reference

This field contains the freight booking number of the freight

6. Consignee

booking associated with the freight order used to create the form.

You can't edit this field. You can navigate to the freight booking

using the document flow of the freight order.

This field contains the data maintained in the Ship-to Party field in

the freight booking that the pick-up freight order is based on.

You can see and edit the ship-to party in the freight booking, on the

Business Partner tab.

  Note

If you have multiple consignees in the freight order, the system

generates one document for each consignee.

7. Carrier

This field contains the data maintained in the Carrier field in the

freight order.

You can see and edit the carrier in the freight order, on the

Business Partner tab.

9. Additional Handling Information

This field contains the text of the Sender's Instruction (CMR

Freight Doc.) note.

You can see and edit the Sender's Instruction (CMR Freight Doc.)

note in the freight order, on the Notes tab.

You can add a note in the freight order, on the Notes tab, by

inserting a new note and selecting Sender's Instruction (CMR

This is custom documentation. For more information, please visit SAP Help Portal.

150


1/14/26, 2:46 PM

Print Form Field

## System Data

Freight Doc.) as the text type.

10. Vessel/Flight and Date

This field contains the ID maintained in the Vessel field and the

date maintained in the Departure Date field for the main carriage in

the freight order.

You can see and edit the Vessel ID field in the freight booking

associated with the freight order used to create the form. The field

is located in the freight booking, on the General Data tab, in the

Voyage screen area.

You can see and edit the date in the freight order, on the Stages

tab.

11. Port/Place of Handling

This field contains the city and country/region of the port of

departure.

This information is determined automatically. You can't edit this

field. You can see the data maintained for the place of loading in the

freight order, on the Overview tab, in the row above the unloading

activity. You can double-click the table row to view details of the

address.

14. Shipping Marks

This field contains the products in the freight order that are

15. CTU ID Number

16. Seal Number

17. CTU Size and Type

classified as dangerous goods.

To add or remove products to or from the list, make sure they're

correctly configured as dangerous goods. For more information,

see Dangerous Goods Processing Based on Product Compliance.

This field contains the data maintained in the Container /

registration Number field in the freight booking that the pick-up

freight order is based on.

You can view and edit this field in the freight booking, on the Items

tab, in row of the relevant container.

This contains the data maintained in the Seals table of the

container in the freight booking that the pick-up freight order is

based on.

You can view and edit this table in the freight booking, on the Items

tab. Select the row corresponding to the container that you want to

see seals for. Open the seals tab that appears underneath the table.

This field contains the data maintained in the Equipment Type field

in the freight booking that the pick-up freight order is based on.

This field is determined by the container type selected in the freight

booking. You can change the container type in the freight order, on

the Items tab.

18. Tare Mass (kg)

This field contains the tare mass of the products in the note.

This is calculated based on the products in the field 14.

19. Total Gross Mass

This field contains the total gross mass of the products in the note.

This is calculated based on the products in the field 14.

22. Name of Company Preparing Note

This field contains the data maintained in the Name field of the

shipper in the freight order.

This is custom documentation. For more information, please visit SAP Help Portal.

151


1/14/26, 2:46 PM

Print Form Field

Bill of Lading (USA)

## System Data

You can't edit this field. You can see the shipper in the freight order,

on the Business Partner tab.

This note is relevant in jurisdictions subject to U.S. transportation regulations. SAP provides a default template that you can use to

print this document.

## Prerequisites

You can print this document from a freight order.

The document is only produced when products in the freight order are classified as dangerous goods. Whether goods are

classified as dangerous goods is determined by Product Compliance. For more information, see Dangerous Goods

Processing Based on Product Compliance.

The system only produces this document if the products in the freight order pass through a territory within the United

States of America.

## Default Template

The default template for this document looks like this:

This is custom documentation. For more information, please visit SAP Help Portal.

152


1/14/26, 2:46 PM

The default template for this document looks like this:

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

153


1/14/26, 2:46 PM

The exact format and content of a bill of lading can vary depending on your implementation. This image is of the default

template delivered by SAP.

## System Data

When generating the form for printing, the system copies data from the freight order to the output document. To enable this

transfer, you must maintain values in specific fields of the freight order. When you generate the print form, the system adds the

following information to the form:

  Note
Any fields which aren't listed in this table aren't filled by the system by default. A system administrator can configure the

system to add additional data by creating custom print forms. For more information, see Creating Custom Print Forms.

Print Form Field

AT

## System Data

This field contains the data maintained in the Shipper field in the

freight order.

You can see and edit the shipper in the freight order, on the

Business Partner tab.

## Carrier

This field contains the data maintained in the Carrier field in the

freight order.

You can see and edit the carrier in the freight order, on the

Business Partner tab.

Consigned To

This field contains the data maintained in the Ship-to Party field in

the freight order.

You can see and edit the ship-to party in the freight order, on the

Business Partner tab.

  Note

If you have multiple consignees in the freight order, the system

generates one document for each consignee.

## Consignment Number

This field contains the freight order number of the freight order

that the document was created from.

You can't edit this field. The data shown is also used in other fields

of the freight document.

## Customer Order Number

This field contains the customer reference number from the sales

order.

## Date Shipped

This field contains the data maintained in the Departure Date field

of the freight order.

You can't edit this field. You can see the departure date in the

freight order, on the General tab.

## Del. Carrier SCAC

This field contains the SCAC code maintained for the delivering

carrier in the freight order.

## Delivery Date

This field contains the delivery date maintained in the freight order.

This is custom documentation. For more information, please visit SAP Help Portal.

154


1/14/26, 2:46 PM

Print Form Field

Freight Terms

## System Data

This field contains the text of the Sender's Instruction (CMR

Freight Doc.) note.

You can see and edit the Sender's Instruction (CMR Freight Doc.)

note in the freight order, on the Notes tab.

You can add a note in the freight order, on the Notes tab, by

inserting a new note and selecting Sender's Instruction (CMR

Freight Doc.) as the text type.

## Item Table

This field contains the products in the freight order that are

classified as dangerous goods.

To add or remove products to or from the list, make sure they're

correctly configured as dangerous goods. For more information,

see Dangerous Goods Processing Based on Product Compliance.

## Sales Order Number

This field contains the sales order number linked to the freight

## SCAC

SID Number

order.

This field contains the SCAC code maintained for the carrier in the

freight order.

This field contains the freight order number of the freight order

that the document was created from.

You can't edit this field. The data shown is also used in other fields

of the freight document.

## Total Weight

This field shows the total gross weight for all items in the item

table.

Bill of Lading (Canada)

This note is relevant in jurisdictions subject to Canadian transportation regulations. SAP provides a default template that you can

use to print this document.

## Prerequisites

You can print this document from a freight order.

The document is only produced when products in the freight order are classified as dangerous goods. Whether goods are

classified as dangerous goods is determined by Product Compliance. For more information, see Dangerous Goods

Processing Based on Product Compliance.

The system only produces this document if the products in the freight order pass through a territory within Canada.

## Default Template

The default template for this document looks like this:

This is custom documentation. For more information, please visit SAP Help Portal.

155


1/14/26, 2:46 PM

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

156


1/14/26, 2:46 PM

The exact format and content of a bill of lading can vary depending on your implementation. This image is of the default

template delivered by SAP.

## System Data

When generating the form for printing, the system copies data from the freight order to the output document. To enable this

transfer, you must maintain values in specific fields of the freight order. When you generate the print form, the system adds the

following information to the form:

  Note
Any fields which aren't listed in this table aren't filled by the system by default. A system administrator can configure the

system to add additional data by creating custom print forms. For more information, see Creating Custom Print Forms.

Print Form Field

System Data

Carrier

## SCAC

This field contains the data maintained in the Carrier field in the

freight order. You can see and edit the carrier in the freight order, on

the Business Partner tab.

This field contains the SCAC code maintained for the carrier in the

freight order.

## Date Shipped

This field contains the data maintained in the Departure Date field

Delivery Date

## Consignment Number

of the freight order. You can't edit this field. You can see the

departure date in the freight order, on the General tab.

This field contains the delivery date maintained in the freight order.

This field contains the freight order number of the freight order

that the document was created from. You can't edit this field. The

data shown is also used in other fields of the freight document.

## Sales Order Number

This field contains the sales order number linked to the freight

order.

## Customer Order Number

This field contains the customer reference number from the sales

Freight Terms

SID Number

AT

Consigned To

order.

This field contains the text of the Sender's Instruction (CMR

Freight Doc.) note. You can see and edit the Sender's Instruction

(CMR Freight Doc.) note in the freight order, on the Notes tab. You

can add a note in the freight order, on the Notes tab, by inserting a

new note and selecting Sender's Instruction (CMR Freight Doc.) as

the text type.

This field contains the freight order number of the freight order

that the document was created from. You can't edit this field. The

data shown is also used in other fields of the freight document.

This field contains the data maintained in the Shipper field in the

freight order. You can see and edit the shipper in the freight order,

on the Business Partner tab.

This field contains the data maintained in the Ship-to Party field in

the freight order. You can see and edit the ship-to party in the

freight order, on the Business Partner tab.

This is custom documentation. For more information, please visit SAP Help Portal.

157


1/14/26, 2:46 PM

Print Form Field

System Data

  Note

If you have multiple consignees in the freight order, the system

generates one document for each consignee.

## Del. Carrier SCAC

This field contains the SCAC code maintained for the delivering

## Item Table

carrier in the freight order.

This field contains the products in the freight order that are

classified as dangerous goods. Products classified as dangerous

goods are determined by Dangerous Goods Management. To add or

remove products, ensure they're correctly configured. For more

information, see Considering Dangerous Goods.

## Total Weight

This field shows the total gross weight for all items in the item

table.

Creating Custom Print Forms

## Prerequisites

If you are creating a new print form, you have created and activated a form using the Form Builder (transaction SFP).

## Context

You can adapt a standard print form to your requirements, or create a new print form.

## Procedure

1. Create a custom ABAP class for the print form (see Creation of an ABAP Class for a Print Form).

2. Create a custom ABAP class for the Post Processing Framework (PPF) service (see Creation of an ABAP Class for the PPF

Service).

3. Define an action profile and an action in the Post Processing Framework (PPF).

An action controls the point at which a document is to be printed (for example, when a user saves a document). When you

define an action, you have to specify the name of the print document. You also specify that the document is a PDF

document, and you enter a standard BAdI. Alternatively, you can use an existing action profile and action.

4. Create the required schedule conditions in Customizing for Cross-Application Components under  Processes and Tools
 Reusable Objects and Functions for BOPF Environment

 PPF Adapter for Output

for Enterprise Applications
## Management

 Maintain PPF Settings .

5. Assign the ABAP class for the PPF service created in step 2 to the relevant business object (BO) nodes.

The new PPF service class must be assigned to the relevant business object node as an output agent. You do this in

Customizing for Cross-Application Components under  Processes and Tools for Enterprise Applications

## Reusable

Objects and Functions for BOPF Environment

 PPF Adapter for Output Management

 Maintain Output Management

Adapter Settings .

## Next Steps

For more information about output management and the Post Processing Framework (PPF), see SAP help portal at

http://help.sap.com   SAP Business Suite

 SAP Supply Chain Management

 SAP SCM Server

. Select an SAP

This is custom documentation. For more information, please visit SAP Help Portal.

158


1/14/26, 2:46 PM

enhancement package for SAP SCM 7.0. In SAP Library choose  Processes and Tools for Enterprise Applications

## Reusable

Objects and Functions for the BOPF Environment (CA-EPT-BRC)

.

Creation of an ABAP Class for a Print Form

## Use

Each print form is processed by a separate ABAP class (that is, a printout class). To adapt a print form to your requirements, you

have to create a custom printout class based on the original printout class that is provided for a print form. The original printout

class is then the superclass of the custom printout class.

The printout class contains methods that fill the required content into the printout structure. Each method fills a specific part of

the printout structure. This content is later printed on the print document.

Note that the technical name of a printout structure is always as follows: CS_PRINTOUT_<abbreviation of the print form name>.

For example, the technical name of the printout structure for the road waybill (USA) is CS_PRINTOUT_VICS.

  Example

The /SCMTMS/CL_PRINTOUT_VICS printout class contains the FILL_PARTY method for printout structure

CS_PRINTOUT_VICS. This method fills those parts of the road waybill (USA) document that are related to the different parties

involved in the transportation of the goods (for example, ship-to party and ship-from party).

## Activities

To change the content that is filled into the printout structure, you have to create a custom printout class based on the original

printout class. The appropriate method in the custom class has to re-implement the corresponding method in the superclass. The

original coding of the superclass can still be used by calling the method of the superclass first (for example, CALL METHOD

super->FILL_PARTY). The custom coding for filling the printout structure can be placed after the call (or instead of the call) of

the method in the superclass.

Note that the custom class must only re-implement the methods that fill those parts of the printout structure that are to be

changed.

  Example

The FILL_PARTY method in the /SCMTMS/CL_PRINTOUT_VICS printout class is re-implemented by the custom printout

class. If the original coding is to be used, the custom method has to be designed as follows:

METHOD fill_party.
   CALL METHOD super->fill_party
## EXPORTING
          is_tor_root      = is_tor_root
          it_party         = is_party
## CHANGING
          cs_printout_vics = cs_printout_vics.
* customer specific coding
    cs_printout_vics-carrier_type_code = lv_type_code.
ENDMETHOD.

## Creation of an ABAP Class for the PPF Service

This is custom documentation. For more information, please visit SAP Help Portal.

159


1/14/26, 2:46 PM
## Use

The connection between a print request in the dialog and the corresponding printout class is carried out by agent classes for

business object nodes. These are called using the Post Processing Framework (PPF).

When a document is printed, the following occurs:

1. The Post Processing Framework (PPF) calls the relevant agent class for the business object node.

2. The agent class calls the relevant printout class (see Creation of an ABAP Class for a Print Form).

3. The printout class fills the content into the print form.

  Example

A road waybill (USA) can be printed for a Transportation Order business object at root level. When a printout is requested, the

corresponding agent class /SCMTMS/CL_PPF_SERV_FOR_TOR calls printout class /SCMTMS/CL_PRINTOUT_VICS.

## Activities

To print a custom print form, you have to derive a new custom agent class from the existing agent class for the relevant print form.

Within the custom agent class, you have to re-implement the PERSONALIZE_DOC_BY_ABAP method. This method calls the

printout functions. In the newly implemented PERSONALIZE_DOC_BY_ABAP method, you have to replace the original printout

class with the custom printout class. All other coding in the new method must be the same as the coding in the original method.

  Example

The /SCMTMS/CL_PRINTOUT_VICS printout class occurs once in the PERSONALIZE_DOC_BY_ABAP method in the

/SCMTMS/CL_PPF_SERV_FOR_TOR agent class.

You create a custom agent class based on the /SCMTMS/CL_PPF_SERV_FOR_TOR agent class. When you re-implement the

PERSONALIZE_DOC_BY_ABAP method in the custom agent class, you have to replace the name of the original printout class

with the name of your custom printout class.

The following shows the original coding of the PERSONALIZE_DOC_BY_ABAP method:

CASE is_ppf_act-ppf_action.
    WHEN mc_ad_print_vics.
*     Create instance of class for document to be printed.
      CREATE OBJECT lo_printout TYPE /scmtms/cl_printout_vics.

The following shows the re-implementation of the PERSONALIZE_DOC_BY_ABAP method:

CASE is_ppf_act-ppf_action.
    WHEN mc_ad_print_vics.
*      Create instance of class for document to be printed.
       CREATE OBJECT lo_printout TYPE zz_customer_specific_vics.

Authorizations

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

160


1/14/26, 2:46 PM

You can control whether users can access applications and can create and edit objects. (With a few exceptions, users have read

access for all Transportation Management profiles).

## Features

In Transportation Management (TM), user authorization is controlled by authorization objects. These objects are based on either

business documents or an authority context.

## Authorization Objects based on Business Documents

These objects contain authorization fields that you can map one-to-one to business document fields. In general, the business

document fields are located on the root nodes of the underlying BOPF business object.

In TM, you can define and activate authorization checks that the system executes at business-object level with transaction

Maintain Authorization Objects (SU21). You can find authorization objects that are delivered by SAP for TM under the object class

SCTS.

## Authorization Objects based on Authority Context

These objects contain the authorization field TM_CONTEXT and include an area where you can define the authority context.

For example, you can use the Maintain Authority Context function with planning and selection profiles to control by functional role

or location which users can create and edit individual profiles.

  Note

You can use authorization object T_ADMIN to deactivate TM-specific authorization checks: This improves performance and

reduces memory allocation. You are recommended to assign it to only system users or communication users who perform

batch or message processing. Do not assign it to dialog users.

## Checking Authorizations

The system checks if a user has the authorization to perform an activity using one of the following strategies:

## Full match

This is the most commonly used strategy and requires that the user passes all authorization checks that are defined in the

business document. If all checks are passed, the user can complete the requested activity, such as displaying, editing,

creating and deleting.

## Single match

This strategy is used for agreements, rate tables, waybill stocks, and TM profiles with authority context. Authorization

objects that are checked with this strategy have one or two authorization fields that are mapped to business document

fields that belong to sub-nodes of the underlying BOPF business object. Even though there can be multiple values for one

authorization field, only one check must be passed to allow the user to complete the requested activity.

## Activities

Complete the following steps to define user authorization using authority context:

1. On a profile screen, click Maintain Authority Context.

2. In the dialog, enter a value, such as "Germany", and click Save.

Note: You can enter multiple values and you can use the same value for multiple profiles.

This is custom documentation. For more information, please visit SAP Help Portal.

161


1/14/26, 2:46 PM

Now, after specifying the value, only users with a user profile that contains authorization objects with the value "Germany"

can edit the profile.

## More Information

For more information about how TM uses the ABAP authorization concept, see ABAP Authorization Concept).

For more information about the authorization function, see Central User Administration.

Transportation Management Monitoring with CCMS

## Use

You can use the monitoring architecture of the Computing Center Management System (CCMS) to monitor a system landscape.

The CCMS monitoring architecture is an SAP NetWeaver framework into which monitoring and administration functions can be

added.

SAP delivers the predefined monitor set SAP TM Monitor Templates for Transportation Management (TM), with which you can

monitor your TM system landscape. The SAP TM Monitor Templates include the following monitors:

## Event Manager Monitor

This monitor allows you to monitor events created in SAP Event Management. For more information about the Event

Manager Monitor, see SAP Library for SAP Event Management on SAP Help Portal at http://help.sap.com/scm . In SAP

Library, choose  SAP Event Management

 SAP Event Management Infrastructure

 Monitoring and Evaluating

## Processes

 Connection to the Computing Center Management System .

## SCM Optimizer Monitor

This monitor allows you to monitor your optimizers within SAP TM using the Remote Control and Communication

Framework (RCCF). For more information, see Remote Control and Communication Framework.

  Note
You cannot change the monitors delivered by SAP. To use a monitor as a template for your own monitor, copy the required

monitor and adapt it to meet your needs. For more information, see Editing Monitors and Monitor Sets.

## Prerequisites

If you run CCMS from a central system to monitor your system landscape, you have set up system connections to your

systems. For more information about setting up CCMS, see Configuring the Monitoring Architecture.

You can only make use of the Event Manager Monitor if SAP Event Management is installed on the same server as TM.

## Features

You can use the SCM Optimizer Monitor to monitor the following:

## Optimizer runs

The SCM Optimizer Monitor displays the percentage of optimizer runs that have been completed without error per

optimizer, such as VSR optimizer or carrier selection optimizer, and per client.

This is custom documentation. For more information, please visit SAP Help Portal.

162


1/14/26, 2:46 PM

## Destinations

The SCM Optimizer Monitor displays whether a destination is available or not as well as its current status.

## Hosts

The SCM Optimizer Monitor displays the hosts, that is, optimizer servers, on which your optimizers run.

You can change the default values for the severity and the frequency of the check. To do this, in the CCMS Monitor Sets

transaction, select the node in the alert monitoring tree for which you want to change the settings, and then choose the Properties

pushbutton.

## Activities

To call the SAP TM Monitor Templates in CCMS, on the SAP Easy Access screen, choose  Tools

## CCMS

 Control/Monitoring

 CCMS Monitor Sets .

More Information

## Alert Monitor

Remote Control and Communication Framework

## Use

The Remote Control and Communication Framework (RCCF) supports the calling, controlling, and logging of engines at external

destinations. It also supports communication with these engines.

The RCCF is used to control the optimizers in Transportation Management (TM).

## Prerequisites

If you want to define your engine servers, you have maintained the destinations in Customizing. While doing so, you have

also checked whether the RFC destinations are correct.

For more information, see Customizing for Cross-Application Components under  Processes and Tools for Enterprise

## Applications

 Remote Control and Communication Framework

  Edit Destinations .

You have entered any special parameters that you have been given by SAP Support or SAP Consulting into the system.

For more information, see Customizing for Cross-Application Components under  Processes and Tools for Enterprise

## Applications

 Remote Control and Communication Framework

  Make Settings for Experts .

## Features

The RCCF offers the following display transactions:

## Log Display

Logs for individual engine runs are displayed in this transaction along with the following data:

Start time

## Processor

This is custom documentation. For more information, please visit SAP Help Portal.

163


1/14/26, 2:46 PM

Application information

## Destination information

Profile information (only if the relevant application supports this)

Most applications offer the additional option to navigate from the log entry to the application and explanation log.

You can also download compressed data files for the engines to your computer in the log display.

## Display Active Sessions

The current engine runs are displayed in this transaction along with information about the engine process, the processor,

and the start time.

The current operating status of the engine run provides information about whether the entry is orphaned or whether it is

still running.

You can delete orphaned engine runs. Examples of orphaned engine runs include engine runs that still exist in the

application following a short dump.

You can exit engine runs in either a soft or hard way.

## Soft

You exit the engine run. This can take a while since the system does not exchange this state until the next time it

communicates with the engine. Most engines that are exited in this way return the data that was changed.

## Hard

You exit the engine run process using the relevant operating system command.

## Version Display

An overview of the engine versions that you have defined at the relevant destinations is displayed in this transaction. The

creation date and the target platform (Operating System field) are also displayed here, for example.

## Activities

To call the RCCF transactions, on the SAP Easy Access screen, choose  Cross-Application Components

 Processes and Tools

for Enterprise Applications

 Remote Control and Communication Framework .

## Data Management

Transportation Management provides a range of functions for managing your data.

For more information see Data Management in Transportation Management

Message Settings

## Use

You use this function to specify filters for messages displayed on the user interface (UI) or stored in the application log for a user

or a role.

## Integration

This is custom documentation. For more information, please visit SAP Help Portal.

164


1/14/26, 2:46 PM

Once the maximum number of messages that you have specified for the application log has been reached, the system saves all

subsequent messages in the message store (see Message Store).

## Prerequisites

For user-specific message settings, the user must exist in the system.

For role-specific message settings, the role must exist in the system.

## Features

You can specify the following settings for a message type (UI or application log message) and either a user or a role:

## Severity

The severity of a message specifies if the message is a warning or an error message, for example.

## Detail level

The detail level can range between 1 (least detailed level) and 9 (most detailed level).

## Problem class

The problem class can range between 1 (Very Important) and 4 (Additional Information).

## Maximum number of messages for application log

This is the maximum number of messages that the system stores in the application log.

For more information about these settings, see the corresponding field help.

## Activities

To make the message settings, in Customizing for Transportation Management, choose  Basic Functions

## User Interface

 Define Message Settings .

Message Store

## Use

You use this report to list the messages contained in the message store.

## Integration

The system saves messages to the message store if the maximum number of messages that can be stored in the application log

has been reached. You specify the maximum number of messages in the message settings (see Message Settings).

## Features

The message store contains all messages issued on the user interface or saved in the application log.

You use this report to do the following:

This is custom documentation. For more information, please visit SAP Help Portal.

165


1/14/26, 2:46 PM

## Display messages

The system displays all messages from the message store that correspond to your selection criteria (user, or date on which

the messages were issued, for example).

The message header information is displayed in an SAP List Viewer (ALV); the content of individual messages is displayed

as an XML file.

## Delete messages

The system deletes all messages from the message store that exceed the retention period that you have specified.

  Note
We recommend that you schedule a recurring batch job to delete messages periodically.

## Export messages

You can export the displayed messages to an XML file using the standard ALV function for exporting data.

## Activities

To access this report, on the SAP Easy Access screen, choose  Transportation Management

 Administration

 Display Message

Store .

This is custom documentation. For more information, please visit SAP Help Portal.

166
