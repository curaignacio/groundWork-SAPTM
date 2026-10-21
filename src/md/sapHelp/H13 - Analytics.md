1/14/26, 2:47 PM

Transportation Management (TM)

Generated on: 2026-01-14 14:47:18 GMT+0000

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


1/14/26, 2:47 PM

## Analytics

Transportation Management analytics provide apps, called overview pages, that show the key performance indicators (KPIs) that

you need to manage your operational business. At a glance, you can see all the vital data you need for your daily decision-making.

Each overview page displays information from a different area of TM, for example, freight booking, freight ordering, tendering, and

business share.

## Analytics Overview Pages

Each overview page consists of a number of cards (similar to tiles) that display information based on one or more KPIs. The cards

are read-only; you can't enter any information or perform queries or searches on them. The cards present data in different ways;

some show lists, others display tables or charts. Some cards present summary information and you can drill down to see further

details, such as individual transactions.

For cards displaying graphical charts (line, bubble), selecting the header takes you to a detailed view showing all the unfiltered,

while selecting a data point in a chart takes you to a detailed view, filtered to show only the information relevant to that data point.

All the cards show information in real time, so that you always have the most up-to-date information. This can be invaluable in

identifying problems such as delays or bottlenecks, and enable you to take swift action to remedy the situation.

You can re-size the cards and change the order in which they're displayed to suit your own requirements.

Each overview page is based on one or more Core Data Services (CDS) views.

You access the TM overview pages from the Fiori launchpad.

## Detailed Views

You can use visual features to analyze the KPI information at a more detailed level. Selecting a card header or information line on

the overview page takes you to the detailed view, which presents summary information graphically in the form of a combination of

donut, bar, and line charts, and also in a table listing relevant Transportation Management documents. From the table you can

navigate directly to the relevant document, such as a freight order or a freight booking, in the Transportation Management system

and change it if necessary.

Detailed views are also read-only; you can't enter any information or perform queries or searches on them.

Some overview pages have two detailed views, each containing information relevant to specific cards, while others only have one.

For example, on the Cost Analysis overview page, selecting the Invoicing Block Analysis card takes you to the Transportation

Invoice Blocked Detailed View, while selecting any other card takes you to the Transportation Costs Detailed View.

## CDS Views

A CDS view is a query view, that is, an SQL query on the database requesting certain data to be returned. One (or more) CDS view

feeds this information into each overview page (OVP). These CDS views are top-level views, called consumption views, that contain

other contributing CDS views. They consist of key figures and attributes.

You need to have the appropriate authorization objects to access CDS views.

The following table lists the TM analytics overview pages, detailed views, and the CDS views that feed information to them:

This is custom documentation. For more information, please visit SAP Help Portal.

2


1/14/26, 2:47 PM
## Summary

Overview Page

## Detailed Views

Contributing CDS Views

Allocation Analysis

## Transportation Allocation

Transportation Allocation Compliance Query

Business Share Analysis

## Business Share

(C_TranspAllocComplianceQ)

Business Share Compliance Query

(C_BusinessShareComplianceQ)

## Cost Analysis

Transportation Costs

Freight Settlement Cost Query

Transportation Invoice Blocked

(C_FreightSettlementCostQ)

Transportation Order Invoicing Block Status Query

(C_TranspOrdInvcgBlockStsQ)

Freight Booking Execution Monitoring

Freight Booking Execution

Freight Booking Execution Event Query

Freight Booking Execution Status

Freight Booking Quantity Analysis

Freight Booking Quantity

(C_FrtBkgExecutionQuery)

Freight Booking Execution Status Query
(C_FrtBkgExecutionStsQ)

Freight Booking Quantity Query
(C_FrtBkgQuantityQuery)

Freight Order Execution Monitoring

## Freight Order Execution

Freight Order Execution Event Query

Freight Order Execution Status

Freight Order Quantity Analysis

Freight Order Quantity

(C_FrtOrdExecutionQuery)

Freight Order Execution Status Query
(C_FrtOrdExecutionStsQ)

Freight Order Quantity Query
(C_FrtOrdQuantityQuery)

Tendering Analysis

## Tendering

Tendering Query (C_TenderingQuery)

## Metadata Extensions to Replace Delivered Time Filters

SAP provides time filters with all the CDS views behind the OVPs and analytical list pages (ALPs) in Transportation Management.

The time filters in all cases contain the current and previous month, on a two-month rolling basis. You can change the standard

delivered time filters by using metadata extensions. For more information, see SAP Note 2779334

.

## Allocation Analysis

As a transportation manager for a shipper, you work with carriers to transport your products to your customers. You can use the

Allocation Analysis overview page to provide you with the key performance indicators (KPIs) that you need to manage your

execution business. At a glance, you can see all the vital data you need for your daily decision-making.

The KPIs show the weight, volume, and amounts of the transportation allocation, including net, gross, minimum, and maximum

values. You can also see the total and average utilization for all units of measure.

The overview page provides you with KPIs for the current and previous month.

## Key Features

## Trade Lane Weight Load Analysis

This is custom documentation. For more information, please visit SAP Help Portal.

3


1/14/26, 2:47 PM

You can view the total current, minimum, and maximum weights, listed by orientation (for example, along) for each carrier.

This may help you identify the most effective trade lane for goods of a particular size and orientation.

## Trade Lane Volume Load Analysis

You can see the aggregated current, minimum, and maximum volumes that each carrier is transporting, listed by

orientation. This may help you identify the most effective trade lane for goods of a particular volume and orientation.

## Trade Lane Container Load Analysis

You can review the total current, minimum, and maximum container counts, listed by orientation for each carrier. This may

help you identify the most effective trade lane for transporting containers.

## Transportation Mode Category Analysis

For each transportation mode category (for example, air, sea), you can view the weight, volume, and quantities that have

been transported.

## Overall Weight Utilization Distribution

You can see the total weight that each carrier is transporting per month (for the current and previous month). You can also

analyze any increase from the average minimum threshold for the transported weight, or any decrease from the average

maximum threshold.

## Overall Container Utilization Distribution

You can see the total container count for each carrier per month (for the current and previous month). You can also analyze

any increase from the average minimum container count threshold, or any decrease from the average maximum threshold.

## Detailed View

You can use visual features to analyze the KPI information at a more detailed level. Selecting a card header or information line

takes you to the detailed view, which presents summary information graphically and also in a table, from which you can navigate

directly to the transportation allocation in the Transportation Management system and change it if necessary.

Supported Device Types

Desktop

## Tablet

Smartphone

Technical Basis

Fiori ID: F2673

This overview page uses the C_TranspAllocComplianceQ CDS view.

You must activate the C_TRANSPALLOCCOMPLIANCEQ_CDS OData service in the Gateway system.

More Information

## Subject

## More Information

Carrier selection overview for a business person

## Carrier Selection

This is custom documentation. For more information, please visit SAP Help Portal.

4


1/14/26, 2:47 PM

## Subject

## More Information

Allocation analysis detailed view for a business person

Transportation Allocation Detailed View

Underlying technical object for a technical person

C_TranspAllocComplianceQ CDS view

Transportation Allocation Compliance Query

## Transportation Allocation Detailed View

You can get a detailed analysis of each key performance indicator (KPI).You can have instant and flexible access to the information

you need to analyze your transportation allocation and change it if necessary by navigating directly to the relevant document in

the Transportation Management (TM) system.

The system displays the information on a two-month rolling basis (current and previous month).

Screen Areas

## Information filter

You can use the information filter on the top of the screen to select the information that the system displays in the chart

and table underneath. This enables you to view your filtered transport allocation data in different ways.

You can quickly see the total gross weight of goods you transported in the current and previous month represented visually

by a donut chart. The total gross weight of goods you transported, filtered by transportation mode category, is depicted by

a line chart. Bar charts show the total gross volume per means of transport, and the number of containers by orientation.

The following views are available:

## Graphics view

By default, the system displays the graphics filter. For example, you can select KPIs for the total gross weight of

goods you transported by road and per orientation used.

## Field view

You can change to a field filter (compact filter), where you can enter the following filter criteria: weight, volume, and

quantity unit, minimum and maximum tolerance (percentage), transportation mode, means or transport, and

orientation.

## Bar chart

The chart in the middle of the screen gives you a comparison view of your KPIs by current value of gross weight, volume,

and number of containers in the current and previous month. You can change the chart to a table or a combined table and

chart. Use the View By filter to view more specific information such as means of transport, destination location, and trade

lane. For example, you can quickly see the number of containers being transported by road to a specific destination location

in the current month.

## Table

The table at the bottom of the screen gives you more information on your KPIs, such as allocation, orientation, source and

destination location, and gross weight and volume. You can add or remove columns in Settings to give you the information

you want to see, for example, the volume of goods transported from a source location in the previous month and the gross

volume utilization.

Selecting an allocation in the table and pressing Change Transportation Allocation takes you directly to the transportation

allocation in Transportation Management (it opens in edit mode), where you can change the information to get a more

This is custom documentation. For more information, please visit SAP Help Portal.

5


1/14/26, 2:47 PM

desirable outcome.

## Example

You want to find out the destination locations to which you transported the highest gross weight by road last month, and the

number of containers used. You see that one location transported a low weight but used a relatively high number of containers. You

navigate directly to the transportation allocation to find out which carrier transported the goods and view further details on that

location.

You can now investigate any issues with that destination location and whether the carrier could be more efficient.

## Technical Basis

Your system administrator or another technical user can use the following technical information to change the detailed view.

Fiori ID: F2745

This detailed view uses the C_TranspAllocComplianceQ CDS view.

You must activate the C_TRANSPALLOCCOMPLIANCEQ_CDS OData service in the Gateway system.

More Information

## Allocation Analysis

Transportation Allocation Compliance Query

Transportation Allocation Compliance Query

Technical Name

## View Type

C_TRANSPALLOCCOMPLIANCEQ Consumption view

## Purpose

This view contains key performance indicators (KPIs) based on the weight, volume, and amounts of the transportation allocation,

including net, gross, minimum, and maximum values. All the KPIs are available on the database level.

The view also calculates the total and average utilization from these KPIs for all units of measure.

## Prerequisites

Authorization is based on both standard Transportation Management and transportation allocation authorization objects, as well

as business partner and trade lane authorization objects.

You’ll need either the Transp. Management Administrative Settings authorization object (T_ADMIN) with activity H1 checked, or

the Transp. Management: Allocation authorization object (T_TAL) with activity 03 checked.

You’ll need the Business Partner: Purpose Completed authorization object (B_BUP_PCPT) for all the business partners you

access in this query.

This is custom documentation. For more information, please visit SAP Help Portal.

6


1/14/26, 2:47 PM

In addition, you’ll need the Location: Access Based on Authorization Group authorization object (/SCMB/LOCB) for all the

locations you access in this query.

The following table lists the authorization objects with required fields and values:

Authorization

Check Condition

Object

Field

Value

## T_ADMIN

Check if the user has either T_ADMIN or T_TAL authorization

object.

## T_TAL

Check if the user has either T_ADMIN or T_TAL authorization

object.

## ACTVT

H1 (Deactivate)

TM_TALTYPE

TranspAllocType

## ACTVT

03 (Display)

## ACTVT

03 (Display)

B_BUP_PCPT Only when the business purpose of the carrier is set to

Completed (value of view field

CarrierBusPurposeIsCompleted = X), check if
authorization object B_BUP_PCPT has set field ACTVT to 03.

The system uses B_BUP_PCPT in the data destruction process

for Information Lifecycle Management.

/SCMB/LOCB Only when the business purpose of the source location or

destination location is set to Completed
(_SourceLocation.IsBusinessPurposeCompleted = X

or

_DestinationLocation.IsBusinessPurposeCompleted

= X), check field BRGRU against the value of view field

_SourceLocation.AuthorizationGroup or

_DestinationLocation.AuthorizationGroup.

The system uses /SCMB/LOCB in the data destruction process
for Information Lifecycle Management

The field BRGRU enables display access to blocked locations

based on the settings you specify in the Define Authorization

Group Indicating Blocked Master Data Customizing activity.

## BRGRU

_SourceLocation.Authorizat

and

_DestinationLocation.Autho

## ACTVT

03 (Display)

This is custom documentation. For more information, please visit SAP Help Portal.

7


1/14/26, 2:47 PM
## Structure

## Business Objects

This view is built on the Transportation Allocation business object.

## Main Input Parameters

The main input parameters are as follows:

## P_Language

Specifies the display language of the texts. The system automatically uses the system language as the P_Language.

## P_TodayDate

Specifies the timeframe of the data that you want to display. The system automatically uses the system date as the

P_TodayDate. This date is usually your local date. The system retrieves information from the beginning of previous month

up to the system date.

## P_DisplayWeightUnit

Specifies the units of weight, for example, Gross Weight in kilograms.

## P_DisplayVolumeUnit

Specifies the units of volume, for example, Item Volume in meters cubed.

## P_DisplayQuantityUnit

Specifies the units of quantity, for example, Number of Containers in pieces.

## P_TrAlcMinToleranceInPercent

Sets another tolerance value for the minimum value.

## P_TrAlcMaxToleranceInPercent

Sets another tolerance value for the maximum value.

The weight and volume unit parameters are mandatory.

## Measures and Attributes

The most important measures and attributes are listed below.

Keys and Identifiers

TransportationAllocation

Transportation Allocation Attributes

## YearMonth

TranspAllocCategory

## TranspAllocType

TranspAllocValdtyStartDateTime

## TranspAllocValdtyEndDateTime

This is custom documentation. For more information, please visit SAP Help Portal.

8


1/14/26, 2:47 PM

TranspAllocBucketType

TrAlcBucketValdtyStrtDate

TrAlcBucketValdtyStrtDteTme

TrAlcBucketValdtyEndDteTime

TranspAllocValdtyEndDateTime

TrAlcBucketValdtyStrtDteYrMnth

TrAlcBucketValdtyEndDteYrMnth

TrAlcCtnUnitOfMeasureDimn

TrAlcGrossVolUnitOfMsrDimn

TrAlcGrossWgtUnitOfMsrDimn

## TradeLane

TradeLaneOrientation

SourceLocation

DestinationLocation

TransportationMode

## MeansOfTransport

TransportationModeCategory

Transportation Allocation Measures

NumberOfTranspAllocBuckets

TrAlcMinGrossWgtInDspUnit

TrAlcMaxGrossWgtInDspUnit

TrAlcCurGrossWeightInDspUnit

TrAlcMinGrossWgtTolInDspUnit

TrAlcMaxGrossWgtTolInDspUnit

TrAlcGrossWgtTolHigh

TrAlcGrossWgtDvtnHigh

TrAlcGrossWgtTolLow

TrAlcGrossWgtDvtnLow

TrAlcUtilznGrossWeightRatio

TrAlcRltvDeviationGrossWeight

TrAlcMinGrossVolInDspUnit

TrAlcMaxGrossVolInDspUnit

## TrAlcCurGrossVolumeInDspUnit

This is custom documentation. For more information, please visit SAP Help Portal.

9


1/14/26, 2:47 PM

TrAlcMinGrossVolTolInDspUnit

TrAlcMaxGrossVolTolInDspUnit

TrAlcGrossVolTolHigh

TrAlcGrossVolDvtnHigh

TrAlcGrossVolTolLow

TrAlcGrossVolDvtnLow

TrAlcUtilznGrossVolumeRatio

TrAlcRltvDeviationGrossVolume

TrAlcMinNmbrOfCtnsInDspUnit

TrAlcMaxNmbrOfCtnsInDspUnit

TrAlcCurNmbrOfCtnsInDspUnit

TrAlcMinNmbrOfCtnsTolInDspUnit

TrAlcMaxNmbrOfCtnsTolInDspUnit

TrAlcNmbrOfCtnsTolHigh

TrAlcNmbrOfCtnsDvtnHigh

TrAlcNmbrOfCtnsTolLow

TrAlcNmbrOfCtnsDvtnLow

TrAlcUtilznContainerRatio

TrAlcRltvDeviationContainer

## Units

DisplayQuantityUnit

DisplayWeightUnit

DisplayVolumeUnit

Constraints

None.

## Business Share Analysis

As a transportation manager for a shipper, you work with carriers to transport your products to your customers. You can use the

Business Share Analysis overview page to provide you with the key performance indicators (KPIs) that you need to manage your

execution business. The KPIs show the current amount and target quantity of each carrier’s transports, the current value to target

quantity ratio, and business share quantities per month. At a glance, you can see all the vital data you need for your daily decision-

making. The overview page provides you with KPIs for the current and previous month.

## Key Features

This is custom documentation. For more information, please visit SAP Help Portal.

10


1/14/26, 2:47 PM

## Weight Fulfillment Ratio

You can see how carriers have performed in respect of total weight transported, that is, how much of their allocated share

they have achieved. You can also see this as a percentage. For example, one carrier may have shipped 328,750kg out of

their allocation of 493,125kg (66.67%).

## Volume Fulfillment Ratio

You can see how carriers have performed in respect of total volumes transported, that is how much of their allocated share

they have achieved. You can also see this as a percentage. For example, one carrier may have shipped 5000m3 out of their

allocation of 10000m3 (50%) .

## Trade Lane Fulfillment

You can view how each trade lane is performing for all units of measure (such as weight and volume), that is, how much of

their allocated share they have actually transported. You can also see this as a percentage. For example, one trade lane may

have transported 987,500kg out of their allocation of 987,500kg (100%).

Road Fulfillment Distribution (Weight)

You can review the volume of goods transported by road by seeing the actual booked carrier quantity against the target

quantity. This is illustrated as a graph.

## Sea Fulfillment Distribution

You can see the volume of goods transported by sea by viewing the actual booked carrier quantity against the target

quantity. This is illustrated as a graph.

## Air Fulfillment Distribution

You can review the volume of goods transported by air by seeing the actual booked carrier quantity against the target

quantity. This is illustrated as a graph.

## Detailed View

You can use visual features to analyze the KPI information at a more detailed level. Selecting a card header or information line

takes you to the detailed view, which presents summary information graphically and also in a table, from which you can navigate

directly to the business share document in the Transportation Management system and change it if necessary.

Supported Device Types

Desktop

## Tablet

Smartphone

Technical Basis

Fiori ID: F2674

This overview page uses the C_BusinessShareComplianceQ CDS view.

You must activate the C_BUSINESSSHARECOMPLIANCEQ_CDS OData service in the Gateway system.

## More Information

This is custom documentation. For more information, please visit SAP Help Portal.

11


1/14/26, 2:47 PM

## Subject

## More Information

Business share overview for a business person

## Business Share

Business share detailed view for a business person Business Share Detailed View

Underlying technical object for a technical person

C_BusinessShareComplianceQ

Business Share Compliance Query

## Business Share Detailed View

You can get a detailed analysis of each key performance indicator (KPI). You can have instant and flexible access to the information

you need to analyze and change your business share quantities and change them if necessary by navigating directly to the relevant

document in the Transportation Management (TM) system.

The system displays the information on a two-month rolling basis (current and previous month).

Screen Areas

## Information filter

You can use the information filter on the top of the screen to select the information that the system displays in the chart

and table underneath. This enables you to view your filtered business share data in different ways.

You can quickly see how your bookings for the month to date compare with the bookings for the previous month

represented visually by a donut chart. A line chart shows fulfilled quantities per transportation mode category, such as

road, sea, and air, while fulfilled quantities per carrier are depicted by a bar chart.

The following views are available:

## Graphics view

By default, the system displays the graphics filter. For example, you can select KPIs for booked quantities in the

current and previous month and the fulfillment ratio per transportation mode category.

## Field view

You can change to a field filter (compact filter), where you can enter the following filter criteria: weight and volume

unit, dimensions (mass or volume), current or previous month, transportation mode, and carrier.

## Bar chart

The chart in the middle of the screen gives you a comparison view of your KPIs by target against booked quantities per

transportation mode category for the current and previous month. For example, you can quickly see whether booked

quantities aligned with target quantities last month. Use the View By filter to view more specific information such as carrier,

means of transport, and trade lane. For example, you can quickly see the quantity of goods being transported within

Germany by road in refrigerated trucks by a specific carrier in the current month.

## Table

The table at the bottom of the screen gives you more information on your KPIs, such as fulfillment ratio, booked quantities,

and target quantities in the current and previous month. You can add or remove columns in Settings to give you the

information you want to see. This enables you to see how a business share is performing against how you planned that it

would perform.

Selecting an allocation in the table and pressing Change Business Share takes you directly to the business share in

Transportation Management (it opens in edit mode), where you can change the information to get a more desirable

This is custom documentation. For more information, please visit SAP Help Portal.

12


1/14/26, 2:47 PM

outcome.

## Example

In a specific trade lane for the month to date, you planned that a carrier would transport 70% of your shipments and another

carrier would transport 30% of your shipments. However, in detailed analysis, you notice that the first carrier has actually

transported 90% of your shipments. The second carrier hasn’t transported any shipments.

You know that you have already incurred penalties because you have passed the 70% threshold for the first carrier, and you will not

reach the 30% threshold for the second carrier in the given time period.

You research why the first carrier got so much of your business, and you change the business share information to favor the

second carrier. You are more confident now that the month will come in closer to what you had originally planned.

## Technical Basis

Your system administrator or another technical user can use the following technical information to change the detailed view.

Fiori ID: F2746

This detailed view uses the C_BusinessShareComplianceQ CDS view.

You must activate the C_BUSINESSSHARECOMPLIANCEQ_CDS OData service in the Gateway system.

More Information

Business Share Analysis

Business Share Compliance Query

Business Share Compliance Query

Technical Name

## View Type

C_BUSINESSSHARECOMPLIANCEQ Consumption view

## Purpose

This view contains business share key performance indicators (KPIs) based on the current amount and target quantity of the

carrier’s transports. The KPIs show relative and absolute tolerance values, the current value to target quantity ratio, and business

share quantities per month.

## Prerequisites

Authorization is based on both standard Transportation Management and business share authorization objects, as well as

business partner and trade lane authorization objects.

You’ll need either the Transp. Management Administrative Settings authorization object (T_ADMIN) with activity H1 checked, or

the Transp. Management: Business Share authorization object (T_BUSSHARE) with activity 03 checked.

This is custom documentation. For more information, please visit SAP Help Portal.

13


1/14/26, 2:47 PM

You’ll need the Business Partner: Purpose Completed authorization object (B_BUP_PCPT) for all business partners accessed in

this query.

In addition, you’ll need the Location: Access Based on Authorization Group authorization object (/SCMB/LOCB) for all locations

accessed in this query.

The following table lists the authorization objects with required fields and values:

Authorization

Check Condition

Object

Field

Value

## T_ADMIN

Check if the user has either T_ADMIN or T_BUSSHARE

authorization object.

ACTVT H1 (Deactivate)

ACTVT 03 (Display)

ACTVT 03 (Display)

T_BUSSHARE Check if the user has either T_ADMIN or T_BUSSHARE

authorization object.

B_BUP_PCPT Only when the business purpose of the carrier is set to

Completed (value of view field

CarrierBusPurposeIsCompleted = X), check if

authorization object B_BUP_PCPT has set field ACTVT to 03.

The system uses B_BUP_PCPT in the data destruction process
for Information Lifecycle Management.

/SCMB/LOCB Only when the business purpose of the source location or

destination location is set to Completed

(_SourceLocation.IsBusinessPurposeCompleted = X
or

_DestinationLocation.IsBusinessPurposeCompleted

= X), check field BRGRU against the value of view field

_SourceLocation.AuthorizationGroup or

_DestinationLocation.AuthorizationGroup.

The system uses/SCMB/LOCB in the data destruction process for

Information Lifecycle Management.

The field BRGRU enables display access to blocked locations
based on the settings you specify in the Define Authorization

Group Indicating Blocked Master Data Customizing activity.

This is custom documentation. For more information, please visit SAP Help Portal.

14

## BRGRU

_SourceLocation.AuthorizationGro

and

_DestinationLocation.Authorizat


Field

## Value

ACTVT 03 (Display(

1/14/26, 2:47 PM

Authorization

Check Condition

Object

## Structure

## Business Objects

This view is built on the Business Share business object.

## Main Input Parameters

The main input parameters are as follows:

## P_Language

Specifies the display language of the texts. The system automatically uses the system language as the P_Language.

## P_TodayDate

Specifies the timeframe of the data that you want to display. The system automatically uses the system date as the

P_TodayDate. This date is usually your local date. The system retrieves information from the beginning of previous month

up to the system date.

## P_DisplayWeightUnit

Specifies the units of weight, for example, Gross Weight in kilograms.

## P_DisplayVolumeUnit

Specifies the units of volume, for example, Item Volume in meters cubed.

The weight and volume unit parameters are mandatory.

## Measures and Attributes

The most important measures and attributes are listed below.

Keys and Identifiers

## BusinessShare

Business Share Attributes

## Carrier

CalendarYear

## YearMonth

BusShrValidityStartDate

BusShrValidityEndDate

BusShrValidityStartDateTime

## BusShrValidityEndDateTime

This is custom documentation. For more information, please visit SAP Help Portal.

15


1/14/26, 2:47 PM

TradeLaneOrientation

## TradeLane

SourceLocationUUID

DestinationLocationUUID

TransportationMode

TransportationModeCategory

MeansOfTransport

UnitOfMeasureDimension

Business Share Measures

BookedBusinessShrQtyInDspUnit

BookedCarrBusShrQtyInDspUnit

BusShrTargetQuantityInDspUnit

BusShrPositiveToleranceValue

BusShrNegativeToleranceValue

BusShrPositiveToleranceInPct

BusShrNegativeToleranceInPct

BusinessShareRelativeDeviation

BusinessShareAbsoluteDeviation

BusinessShareRatio

## Units

RatioUnit

DisplayUnit

Constraints

None.

## Cost Analysis

As a transportation manager or person responsible for costs, you need to track your costs and be aware of any issues with freight

orders or freight bookings that are blocked for invoicing. You can use the Cost Analysis overview page to provide you with the key

performance indicators (KPIs) that you need to analyze costs and take the appropriate action if required.

The KPIs show cost amounts analyzed in different ways: by invoicing week, transportation mode category (with weights and

volumes), carrier, charge type, purchasing organization, source and destination country or region, and number of transportation

orders (freight orders and freight bookings) blocked for invoicing, with blocking reasons. At a glance, you can see all the vital data

you need for your daily decision-making.

This is custom documentation. For more information, please visit SAP Help Portal.

16


1/14/26, 2:47 PM

The overview page provides you with KPIs for the current and previous month.

This overview page is based on two CDS views (data sources), each generating different cards.

## Key Features

The following features are available with data source 1 (C_FreightSettlementCostQ CDS view):

## Cost Distribution

A chart displays the increase or decrease in invoiced amounts, credit amounts, and cost amounts in each invoicing week.

The total cost appears at the top, for example, 5.3M euros.

## Cost and Quantity Analysis

A bubble chart shows the total cost for each transportation mode category, together with the gross weight and volume

transported. The overall total cost appears at the top, for example, 1.6B euros.

## Logistic Network Analysis

You can see a table displaying the total cost for goods transported from source to destination countries or regions, with the

highest cost at the top. For example, Germany to USA has a total cost of 2.2M euros. This lets you see at a glance where you

are spending most on transportation costs.

## Carrier Cost Analysis

You can view a table showing carriers with the highest costs (highest at the top). The total cost per carrier is shown

alongside their name. This gives you a quick visual indication of the carriers with whom you are spending the most.

## Cost and Quantity Analysis

You can see the total cost per transportation mode category, together with the gross weight and volume transported in

each category.

## Charge Type Analysis

You can review charge types with the highest costs (highest at the top). The total cost, with gross weight and volume, is

displayed for each charge type (for example, basic freight charges, pick up charges), enabling you to see where you are

spending the most.

## Purchasing Organization Cost Analysis

You can see purchasing organizations with the highest costs (highest at the top). The total cost for each purchasing

organization is shown alongside their name, enabling you to see at a glance the purchasing organizations with which you

are doing the most business.

The following feature is available with data source 2 (C_TranspOrdInvcgBlockStsQ CDS view):

## Invoicing Block Analysis

You can see how many transportation orders (freight orders or freight bookings) are blocked for invoicing. The numbers are

shown per blocking reason, such as time conflict, compliance, incomplete for planning. This may prompt you to investigate

further, perhaps to find out why specific invoices are blocked, and to take immediate action if necessary.

## Detailed View

You can use visual features to analyze the KPI information at a more detailed level. Selecting a card header or information line

takes you to the detailed view, which presents summary information graphically and also in a table, from which you can navigate

directly to the freight booking or freight order in the Transportation Management system and change it if necessary.

This is custom documentation. For more information, please visit SAP Help Portal.

17


1/14/26, 2:47 PM

Selecting the Invoicing Block Analysis card takes you to the Transportation Invoice Blocked Detailed View. Selecting any other

card takes you to the Transportation Costs Detailed View.

Supported Device Types

Desktop

## Tablet

Smartphone

Technical Basis

Fiori ID: F2672

This overview page uses the the following CDS views:

C_FreightSettlementCostQ (data source 1)

•

C_TranspOrdInvcgBlockStsQ (data source 2)

You must activate the following OData services in the Gateway system:

C_FREIGHTSETTLEMENTCOSTQ_CDS (data source 1)

C_TRANSPORDINVCGBLOCKSTSQ_CDS (data source 2)

More Information

## Subject

## More Information

Cost analysis overview for a business person

## Settlement

Cost analysis detailed views for a business person

Transportation Costs Detailed View

Transportation Invoice Blocked Detailed View

Underlying technical objects for a technical person

Freight Settlement Cost Query

C_FreightSettlementCostQ

## Freight Settlement Cost Query

Transportation Order Invoicing Block Status Query

## C_TranspOrdInvcgBlockStsQ

Transportation Order Invoicing Block Status Query

## Transportation Costs Detailed View

You can get a detailed analysis of each key performance indicator (KPI). You can have instant and flexible access to the information

you need to analyse your costs and change them if necessary by navigating directly to the relevant document in the Transportation

Management (TM) system.

This is custom documentation. For more information, please visit SAP Help Portal.

18


1/14/26, 2:47 PM

The system displays the information on a two-month rolling basis (current and previous month).

Screen Areas

## Information filter

You can use the information filter on the top of the screen to select the information that the system displays in the chart

and table underneath. This enables you to view your costs filtered in different ways.

For example, you can quickly see the total cost for goods you transported by road and the proportion of your business this

represented, represented visually by donut and line charts as follows:

## Graphics view

By default, the system displays the graphics filter. For example, you can select KPIs for invoice year week and

transportation mode category.

## Field view

You can change to a field filter (compact filter), where you can enter filter criteria such as weight unit, volume unit,

and currency.

## Bar chart

The chart in the middle of the screen gives you a comparison view of your KPIs. You can change the chart to a table or a

combined table and chart. Use the View By filter to view more specific information such as carrier, charge type, and source

and destination countries or regions. For example, you can quickly see the cost of goods transported by road to the USA by

a carrier in a specific invoicing week.

## Table

The table at the bottom of the screen gives you more information on your KPIs, such as carrier, charge type, purchasing

organization, and gross weight and volume. It also lists the relevant freight settlement documents. You can add or remove

columns in Settings to give you the information you want to see, for example, the volume of goods transported to a country

or region and by which carrier in a specific invoicing week.

Selecting a a row in the table takes you directly to the freight settlement document in Transportation Management (it

opens in edit mode), where you can change the information to get a more desirable outcome.

## Example

You want to see how much you spent on transporting goods by air from the USA to Japan last month, with a view to making

savings. You see that you spent a high amount in one invoice week, while no costs were involved in other weeks. You navigate

directly to the freight settlement document to find out which carrier transported the goods and view the charges involved. You

notice that goods were transported by air five times during that week. You also navigate to the air freight booking to see more

details.

You now have the facts to further investigate the reasons for transporting the goods by air that week; perhaps it had become an

urgent shipment and if more notice had been given, you could have used a less expensive mode of transport.

## Technical Basis

Your system administrator or another technical user can use the following technical information to change the detailed view.

Fiori ID: F2754

This detailed view uses the C_FreightSettlementCostQ CDS view.

This is custom documentation. For more information, please visit SAP Help Portal.

19


1/14/26, 2:47 PM

You must activate the C_FREIGHTSETTLEMENTCOSTQ_CDS OData service in the Gateway system.

More Information

## Cost Analysis

## Transportation Invoice Blocked Detailed View

You can get a detailed analysis of each key performance indicator (KPI). You can have instant and flexible access to the information

you need to investigate transportation orders blocked for invoicing and take action if necessary by navigating directly to the

relevant document in the Transportation Management (TM) system.

The system displays the information on a two-month rolling basis (current and previous month).

Screen Areas

## Information filter

You can use the information filter on the top of the screen to select the information that the system displays in the chart

and table underneath. This enables you to view transportation orders (freight orders and freight bookings) that are blocked

for invoicing filtered in different ways.

You can quickly see the total cost of transportation orders blocked for invoicing per transportation order life cycle status

year week and per transportation mode category, represented visually by donut and line charts as follows:

## Graphics view

By default, the system displays the graphics filter. For example, you can select KPIs for cost amount by life cycle

status year week and transportation mode category.

## Field view

You can change to a field filter (compact filter), where you can enter filter criteria such as weight unit, volume unit,

and currency.

## Bar chart

The chart in the middle of the screen gives you a comparison view of your KPIs. You can change the chart to a table or a

combined table and chart. Use the View By filter to view more specific information such as carrier, block category, and

block reason. For example, you can quickly see the total cost of transportation orders blocked for invoicing involving goods

transported by sea for a specific carrier, and the reasons why they are blocked.

## Table

The table at the bottom of the screen gives you more information on your KPIs, such as block category, block reason,

carrier, source and destination country or region, and document category. It also lists the relevant Transportation

Management documents. You can add or remove columns in Settings to give you the information you want to see. This

enables you to see, for example, which carrier was used and the destination of the goods being transported in a specific

transportation order life cycle status year week.

Selecting a a row in the table takes you directly to the freight booking or freight order in Transportation Management (it

opens in edit mode), where you can change the information to get a more desirable outcome.

## Example

This is custom documentation. For more information, please visit SAP Help Portal.

20


1/14/26, 2:47 PM

You want to know how many freight orders are currently blocked for invoicing for goods being transported by sea and find out why,

so that you can take remedial action. You see that three orders are blocked with a block category of time conflict and a block

reason of penalty charges. You go directly to the freight orders to view the charges and gain more insight into what happened. You

find out that the carrier arrived late for their customs slot on two occasions and can see all the relevant details.

Armed with the facts, you can now contact the carrier to resolve any dispute over payment of the penalty charges and ensure that

they keep to their schedule in future.

## Technical Basis

Your system administrator or another technical user can use the following technical information to change the detailed view.

Fiori ID: F2755

This detailed view uses the C_TranspOrdInvcgBlockStsQ CDS view.

You must activate the C_TRANSPORDINVCGBLOCKSTSQ_CDS OData service in the Gateway system.

More Information

## Cost Analysis

Freight Settlement Cost Query

Technical Name

## View Type

C_FREIGHTSETTLEMENTCOSTQ Consumption view

## Purpose

This view contains key performance indicators (KPIs) to enable you to see if you’ve reached your business goals for individual

charge types and timeframe.

The view also contains calculations showing you how much you’ve spent on transportation for each carrier and how much you’ve

spent on each transportation mode.

## Prerequisites

Authorization is based on the standard Transportation Management authorization objects.

You’ll need either the Transp. Management Administrative Settingsauthorization object (T_ADMIN), or all of the following

authorization objects:

Transp. Management Order Management & Planning (Purchase) (T_TOR_PUR)

Transp. Management Order Management & Planning (Execution) authorization object (T_TOR_EXE)

Transp. Management Freight Settlement authorization object (T_SD_FSD)

.

In addition, you’ll need the Business Partner: Authorization Groups authorization object (B_BUPA_GRP) for all business partners

accessed in this query.

This is custom documentation. For more information, please visit SAP Help Portal.

21


1/14/26, 2:47 PM

The following table lists the authorization objects with required fields and values:

Authorization Object

Field

## Value

Description

T_ADMIN

T_TOR_PUR

T_TOR_EXE

T_SD_FSD

B_BUPA_GRP

## ACTVT

H1 (Deactivate)

## Activity

Transp. Management:

Administrative Settings

authorization object

TM_OC

## TM_OT

TM_XPORG

TM_XPGRP

TM_RP

TM_MOT

ACTVT

TM_OC

## TM_OT

TM_XEORG

TM_XEGRP

TM_RP

TM_MOT

## ACTVT

Transp. Management: Order

Management & Planning

(Purchase) authorization

object

TransportationOrderCategory

Field in query view

TransportationOrderType

Field in query view

PurchasingOrgExternalID

Field in query view

PurchasingGroupExternalID

Field in query view

TranspOrdResponsiblePerson

Field in query view

TransportationMode

Field in query view

09 (Display prices)

## Activity

Transp. Management: Order

Management & Planning

(Execution) authorization

object

TransportationOrderCategory

Field in query view

TransportationOrderType

Field in query view

PlngAndExecOrgExternalID

Field in query view

PlngAndExecGroupExternalID

Field in query view

TranspOrdResponsiblePerson

Field in query view

TransportationMode

Field in query view

09 (Display prices)

## Activity

Transp. Management: Freight

Settlement authorization

object

## TM_SF_CAT

SuplrFrtInvcReqCategory

Field in query view

## TM_SF_TYPE

SuplrFrtInvcReqType

Field in query view

## ACTVT

03 (Display)

## Activity

Business Partner:

Authorization Groups

authorization object

This is custom documentation. For more information, please visit SAP Help Portal.

22


1/14/26, 2:47 PM

Authorization Object

Field

## Value

Description

## BEGRU

CarrierAuthorizationGroup

Fields in query view

ShipperAuthorizationGroup

ConsigneeAuthorizationGroup

## ACTVT

03 (Display)

Activity

## Structure

## Business Objects

This view is built on the following business business objects:

Freight Settlement Documents

Transportation Order

Transportation Charges

## Main Input Parameters

The main input parameters are as follows:

## P_Language

Specifies the display language of the texts. The system automatically uses the system language as the P_Language.

## P_TodayDate

Specifies the timeframe of the data that you want to display. The system automatically uses the system date as the

P_TodayDate. This date is usually your local date. The system retrieves information from the beginning of previous month

up to the system date.

## P_DisplayTimeUnit

Specifies the units of time, for example, Event Delay in hours or minutes.

## P_DisplayWeightUnit

Specifies the units of weight, for example, Gross Weight in kilograms.

## P_DisplayVolumeUnit

Specifies the units of volume, for example, Item Volume in meters cubed.

## P_DisplayQuantityUnit

Specifies the units of quantity, for example, Number of Containers in pieces.

## P_DisplayLengthUnit

Specifies the units of length, for example, Package Length in meters.

## P_DisplayCurrency

Specifies the currency, for example, Invoice Amount in euros.

The unit parameters (time, weight, volume, quantity, length, and currency) are mandatory.

This is custom documentation. For more information, please visit SAP Help Portal.

23


1/14/26, 2:47 PM

## Measures and Attributes

The most important measures and attributes are listed below.

Keys and Identifiers

SupplierFreightInvoiceRequest

TransportationOrder

SuplrFrtInvcReqUUID

TransportationOrderUUID

TransportationChargesObjUUID

TranspChargeItemUUID

TranspChargeItemElementUUID

Freight Settlement Document Attributes

SuplrFrtInvcReqCategory

SuplrFrtInvcReqType

SuplrFrtInvcReqLifeCycSts

SuplrFrtInvcReqConfStatus

SuplrFrtInvcReqConstcySts

SuplrFrtInvcReqArchStatus

InvoicingStatus

PurchasingOrganization

PurchasingGroup

BillFromParty

## Carrier

## InvoiceDate

InvoiceDateYearWeek

InvoiceDateYearMonth

InvoiceDateYearQuarter

## InvoiceDateYear

Freight Order/Freight Booking Attributes

TransportationOrderCategory

TransportationOrderType

TranspOrdShippingType

## TransportationMode

This is custom documentation. For more information, please visit SAP Help Portal.

24


1/14/26, 2:47 PM

TransportationModeCategory

## MeansOfTransport

TranspOrdTrafficDirection

TranspOrdLifeCycleStatus

TranspOrdPlanningStatus

PlngAndExecOrganization

PlngAndExecGroup

Shipper

## Consignee

SourceLocation

SourceLocationType

SourceLocationCountry

SourceLocationRegion

DestinationLocation

DestinationLocationType

DestinationLocationCountry

DestinationLocationRegion

Transportation Charges Attributes

TranspChargeCategory

TranspChargeSubCategory

TranspChargeType

TranspChargeInstrnType

TranspChargeCalcStatus

CarrierInvoicingStatus

TranspChargeItmInvcgStatus

TranspChargeCalcLevel

TranspChargeCalcSheetLineNmbr

## TranspChargeCalcReslnBase

Freight Order/Freight Booking Measures

TranspOrdGrossWeightInDspUnit

TranspOrdGrossVolumeInDspUnit

TranspOrdQuantityInDisplayUnit

## TranspOrdNumberOfCtnsInDspUnit

This is custom documentation. For more information, please visit SAP Help Portal.

25


1/14/26, 2:47 PM

TranspOrdDistanceInDspUnit

TranspOrdNetDurationInDspUnit

Transportation Charges Measures

InvoicedAmountInDspCurrency

CreditAmountInDisplayCurrency

CostAmountInDisplayCurrency

## Units

DisplayTimeUnit

DisplayWeightUnit

DisplayVolumeUnit

DisplayQuantityUnit

DisplayLengthUnit

DisplayCurrency

Constraints

None.

Transportation Order Invoicing Block Status Query

Technical Name

## View Type

C_TRANSPORDINVCGBLOCKSTSQ Consumption view

## Purpose

This view contains key performance indicators (KPIs) to help you find out if any freight orders or booking orders are blocked for

invoicing (for a specific timeframe).

## Prerequisites

Authorization is based on the standard Transportation Management authorization objects.

You’ll need either the Transp. Management Administrative Settingsauthorization object (T_ADMIN), or all of the following

authorization objects:

Transp. Management Order Management & Planning (Purchase) (T_TOR_PUR)

Transp. Management Order Management & Planning (Execution) authorization object (T_TOR_EXE)

Transp. Management Freight Settlement authorization object (T_SD_FSD)

.

This is custom documentation. For more information, please visit SAP Help Portal.

26


1/14/26, 2:47 PM

In addition, you’ll need the Business Partner: Authorization Groups authorization object (B_BUPA_GRP) for all business partners

accessed in this query.

The following table lists the authorization objects with required fields and values:

Authorization Object

Field

## Value

Description

T_ADMIN

T_TOR_PUR

T_TOR_EXE

T_SD_FSD

## ACTVT

H1 (Deactivate)

## Activity

Transp. Management:

Administrative Settings

authorization object

TM_OC

## TM_OT

TM_XPORG

TM_XPGRP

TM_RP

TM_MOT

ACTVT

TM_OC

## TM_OT

TM_XEORG

TM_XEGRP

TM_RP

TM_MOT

## ACTVT

Transp. Management: Order

Management & Planning

(Purchase) authorization

object

TransportationOrderCategory

Field in query view

TransportationOrderType

Field in query view

PurchasingOrgExternalID

Field in query view

PurchasingGroupExternalID

Field in query view

TranspOrdResponsiblePerson

Field in query view

TransportationMode

Field in query view

09 (Display prices)

## Activity

Transp. Management: Order

Management & Planning

(Execution) authorization

object

TransportationOrderCategory

Field in query view

TransportationOrderType

Field in query view

PlngAndExecOrgExternalID

Field in query view

PlngAndExecGroupExternalID

Field in query view

TranspOrdResponsiblePerson

Field in query view

TransportationMode

Field in query view

09 (Display prices)

## Activity

Transp. Management:

Freight Settlement

authorization object

## TM_SF_CAT

SuplrFrtInvcReqCategory

Field in query view

## TM_SF_TYPE

SuplrFrtInvcReqType

Field in query view

## ACTVT

03 (Display)

## Activity

This is custom documentation. For more information, please visit SAP Help Portal.

27


1/14/26, 2:47 PM

Authorization Object

Field

## Value

Description

## B_BUPA_GRP

Business Partner:

Authorization Groups

authorization object

## BEGRU

BillFromPtyAuthorizationGroup

Fields in query view

CarrierAuthorizationGroup

ShipperAuthorizationGroup

ConsigneeAuthorizationGroup

## ACTVT

03 (Display)

Activity

## Structure

## Business Objects

This view is built on the following business business objects:

Transportation Order

Freight Settlement Documents

Transportation Charges

## Main Input Parameters

The main input parameters are as follows:

## P_Language

Specifies the display language of the texts. The system automatically uses the system language as the P_Language.

## P_TodayDate

Specifies the timeframe of the data that you want to display. The system automatically uses the system date as the

P_TodayDate. This date is usually your local date. The system retrieves information from the beginning of previous month

up to the system date.

## P_DisplayWeightUnit

Specifies the units of weight, for example, Gross Weight in kilograms.

## P_DisplayVolumeUnit

Specifies the units of volume, for example, Item Volume in meters cubed.

## P_DisplayQuantityUnit

Specifies the units of quantity, for example, Number of Containers in pieces.

## P_DisplayCurrency

Specifies the currency, for example, Invoice Amount in euros.

The unit and currency parameters (weight, volume, quantity, and currency) are mandatory.

## Measures and Attributes

This is custom documentation. For more information, please visit SAP Help Portal.

28


1/14/26, 2:47 PM

The most important measures and attributes are listed below.

Keys and Identifiers

SupplierFreightInvoiceRequest

## TransportationOrder

Freight Order/Freight Booking Attributes

TransportationOrderCategory

TransportationOrderType

TranspOrdShippingType

TransportationMode

TransportationModeCategory

## MeansOfTransport

TranspOrdTrafficDirection

TranspOrdLifeCycleStatus

TranspOrdPlanningStatus

TransportationOrderExecSts

PurchasingOrganization

## PurchasingGroup

PlngAndExecOrganization

PlngAndExecGroup

Shipper

Consignee

## Carrier

SourceLocation

SourceLocationType

SourceLocationCountry

SourceLocationRegion

DestinationLocation

DestinationLocationType

DestinationLocationCountry

DestinationLocationRegion

DangerousGoodsAreContained

TranspOrdPlanningBlock

## TranspOrdExecutionIsBlocked

This is custom documentation. For more information, please visit SAP Help Portal.

29


1/14/26, 2:47 PM

InvoicingIsBlocked

InvoicingBlockReason

CarrierOriginOfEntry

TranspOrdLfcycStsChgDteTime

TranspOrdLfcycStsChgDte

TranspOrdLfcycStsChgDteYrWeek

TranspOrdLfcycStsChgDteYrMnth

TranspOrdLfcycStsChgDteYearQtr

TranspOrdLfcycStsChgDteYear

Freight Settlement Document Attributes

SuplrFrtInvcReqCategory

SuplrFrtInvcReqType

SuplrFrtInvcReqLifeCycSts

SuplrFrtInvcReqBlockReason

SuplrFrtInvcReqBlockStatus

SuplrFrtInvcReqConfStatus

SuplrFrtInvcReqConstcySts

SuplrFrtInvcReqArchStatus

InvoicingStatus

BillFromParty

## InvoiceDate

InvoiceDateYearWeek

InvoiceDateYearMonth

InvoiceDateYearQuarter

## InvoiceDateYear

Transportation Charges Attributes

TranspChargeCalcStatus

CarrierInvoicingStatus

TranspChargeItmInvcgStatus

## TranspChargeCalcLevel

Freight Order/Freight Booking Measures

## TranspOrdGrossWeightInDspUnit

This is custom documentation. For more information, please visit SAP Help Portal.

30


1/14/26, 2:47 PM

TranspOrdGrossVolumeInDspUnit

TranspOrdQuantityInDisplayUnit

TranspOrdNumberOfCtnsInDspUnit

NumberOfTransportationOrders

NumberOfInvcgBlkdTranspOrds

Transportation Charges Measures

InvoicedAmountInDspCurrency

CreditAmountInDisplayCurrency

CostAmountInDisplayCurrency

## Units

DisplayWeightUnit

DisplayVolumeUnit

DisplayQuantityUnit

DisplayCurrency

Constraints

None.

## Freight Booking Execution Monitoring

As a transportation manager for a shipper, you work with carriers to transport your products to your customers. You need to

monitor your freight bookings with carriers to make sure they are being executed on time.

A freight booking contains the logistical plan for the transportation of goods, for example, fixed departure times of a ship. You use a

freight booking to reserve freight space on a ship or in an airplane, and it also contains information on how the plan is actually

carried out.

You can use the Freight Booking Execution Monitoring overview page to provide you with the key performance indicators (KPIs)

that you need to manage your execution business. At a glance, you can see all the vital data you need for your daily decision-

making.

The overview page provides you with KPIs for the current and previous month.

## Key Features

This overview page is based on two CDS views (data sources), each generating different cards.

The following features are available with data source 1 (C_FRTBKGEXECUTIONSTSQ_CDS CDS view):

## Life Cycle Status Analysis

You can view the number of execution-relevant freight bookings, grouped by freight booking life cycle status. Execution-

relevant freight bookings have the execution status In Execution (03) and have a departure event but no arrival event at the

This is custom documentation. For more information, please visit SAP Help Portal.

31


1/14/26, 2:47 PM

final destination.

You can see the number of freight bookings for each life cycle status (Draft (00), New (01), or In Process (02)), sorted in

descending order.

## Execution Block Analysis

You can review all freight bookings with an execution block, grouped by execution block reason. This helps you to determine

the most common causes of execution blocking and take the appropriate action. The list is sorted in descending order.

You specify execution block reasons in the TM Freight Booking transaction; if you haven’t done this, the system

automatically creates them, based on the blocking category.

## Planning Block Analysis

You can review all freight bookings with a planning block, grouped by planning block reason. This helps you to determine

the most common causes of planning blocking and take the appropriate action. The list is sorted in descending order.

You specify execution block reasons in the TM Freight Booking transaction; if you haven’t done this, the system

automatically creates them, based on the blocking category.

## Delayed Freight Bookings in Transit

You can view freight bookings that are delayed in transit, that is, if their latest, time-relevant event is delayed (both the

expected and actual date and time fields are available and the event status is Reported). The delay is the time difference

between the actual date and the expected date.

You can see the total number of freight bookings and then drill down to view details such asFreight Booking ID, Means of

Transport, Gross Weight, and Delay. You specify the units as parameters in the relevant CDS query view.

You can also navigate directly to the related freight booking transaction by selecting the first line or header line of the

details view.

The following features are available with data source 2 (C_FRTBKGEXECUTIONQUERY_CDS CDS view):

## Blocking Discrepancies

You can review the discrepant freight booking events that led to a block, sorted by event code and discrepancy type (such

as delivery of item, late, or delay). The discrepancy type with the most blocking events is at the top.

## Non-Blocking Discrepancies

You can see the discrepant freight booking events that didn’t result in a block, sorted by event code and discrepancy type

(such as arrival at destination, departure, or loading end). The discrepancy type with the most non-blocking events is at the

top.

## Carrier On Time Performance

You can view the percentage of freight bookings that each carrier delivered on time. You can also see this expressed in

numbers, for example, 6 / 14 were on time. A freight booking is on time if all its events are classed as on time, otherwise it is

classed as delayed. This helps you identify the most efficient carriers.

The calculation for all the on time performance cards takes into account all time-relevant events where both expected and

actual date and time fields are available, and where the event status is Reported.

## Location On Time Performance

This shows the percentage of on time freight booking events for each location, sorted by the transportation order events on

time ratio. The lowest percentage is at the top. You can also see this expressed in numbers, for example, 6 / 8 events were

on time. This helps you understand how individual locations are performing.

## Activity On Time Performance

This is custom documentation. For more information, please visit SAP Help Portal.

32


1/14/26, 2:47 PM

You can review the percentage of on time freight booking events for each event code (such as loading or unloading), with

the lowest number at the top. You can also see this expressed in numbers, for example, 12 / 27 events took place on time.

You can use this information to identify potential bottlenecks.

## Unexpected Events

You can monitor unexpected events that took place within the freight booking, grouped by event code (such as accident or

delay), with the highest number at the top. This information may prove vital in taking preventative measures to avoid such

events in the future.

## Detailed View

You can use visual features to analyze the KPI information at a more detailed level. Selecting a card header or information line

takes you to the detailed view, which presents summary information graphically and also in a table, from which you can navigate

directly to the freight booking worklist in the Transportation Management system and change it if necessary.

Selecting the blocking and non-blocking discrepancies, carrier, location, and activity on time performance, and unexpected events

cards takes you to the Freight Booking Execution Detailed View. Selecting the life cycle status analysis, execution and planning

block analysis, and freight bookings delayed in transit cards takes you to the Freight Booking Execution Status Detailed View

Supported Device Types

Desktop

## Tablet

Smartphone

Technical Basis

Fiori ID: F2677

This overview page uses the following CDS views:

C_FrtBkgExecutionStsQ (data source 1)

C_FrtBkgExecutionQuery (data source 2)

You must activate the following OData services in the Gateway system:

C_FRTBKGEXECUTIONSTSQ_CDS (data source 1)

C_FRTBKGEXECUTIONQUERY_CDS (data source 2)

More Information

## Subject

## More Information

Freight booking overview for a business person

## Freight Booking

Freight booking execution detailed views for a business person

Freight Booking Execution Detailed View

Freight Booking Execution Status Detailed View

Underlying technical objects for a technical person

## C_FrtBkgExecutionStsQ CDS view

This is custom documentation. For more information, please visit SAP Help Portal.

33


1/14/26, 2:47 PM

## Subject

## More Information

Freight Booking Execution Status Query

C_FrtBkgExecutionQuery CDS view

Freight Booking Execution Event Query

## Freight Booking Execution Detailed View

You can get a detailed analysis of each key performance indicator (KPI). You can have instant and flexible access to the information

you need to monitor and analyze your freight booking execution and change it if necessary by navigating directly to the relevant

document in the Transportation Management (TM) system.

This detailed view provides further information on the following cards on the Freight Booking Execution Monitoring overview

page:

Blocking and non-blocking discrepancies

Carrier, location, and activity on time performance

## Unexpected events

The system displays the information on a two-month rolling basis (current and previous month).

Screen Areas

## Information filter

You can use the information filter on the top of the screen to select the information that the system displays in the chart

and table underneath. This enables you to view your filtered freight booking data in different ways.

You can quickly see the event on time ratio by location and carrier, represented visually by a bar chart and a line chart

respectively. Donut charts display the ratio of on time events per event (such as arrival at destination, departure, or loading

end), expressed as a percentage, and the number of events broken down into discrepancy type leading to a block and

discrepancy type not leading to a block.

The following views are available:

## Graphics view

By default, the system displays the graphics filter. For example, you can select KPIs for the on time ratio of arrival

events, or for a specific location.

## Field view

You can change to a field filter (compact filter), where you can enter filter criteria such as event status and the

weight, volume, and time units in which you want to see the information.

## Bar chart

The chart in the middle of the screen gives you a comparison view of your KPIs by number of freight bookings per

transportation mode category and traffic direction. You can change the chart to a table or a combined table and chart. Use

the View By filter to view more specific information such as discrepancy, discrepancy type, and event. For example, you can

quickly see the number of freight bookings transported by road that arrived at their destination with no discrepant events.

## Table

This is custom documentation. For more information, please visit SAP Help Portal.

34


1/14/26, 2:47 PM

The table at the bottom of the screen gives you more information on your KPIs, such as destination country or region,

event, event status, and number of delayed freight bookings. You can add or remove columns in Settings to give you the

information you want to see, for example, ship-to party and expected end date.

Selecting a freight booking in the table and pressing Change Freight Booking takes you directly to the freight booking in

Transportation Management (it opens in edit mode), where you can change the information to get a more desirable

outcome.

## Example

You want to review the discrepant freight booking events that led to a block and see which discrepancy types are the most
common, for example, delivery of item, late, or delay. You see that late is the most frequently occurring discrepancy type. You find
out that several late events involved one location and the same means of transport. You navigate directly to the freight booking to
see further details. You now have the information to investigate the issue with that location with the carrier and prevent future
problems.

## Technical Basis

Your system administrator or another technical user can use the following technical information to change the detailed view.

Fiori ID: F2747

This detailed view uses the C_FrtBkgExecutionQuery CDS view.

You must activate the C_FRTBKGEXECUTIONQUERY_CDS OData service in the Gateway system.

## More Information

Freight Booking Execution Monitoring

Freight Booking Execution Event Query

## Freight Booking Execution Status Detailed View

You can get a detailed analysis of each key performance indicator (KPI). You can have instant and flexible access to the information

you need to analyse your freight booking execution status and change it if necessary by navigating directly to the relevant

document in the Transportation Management (TM) system.

This detailed view provides further information on the following cards on the Freight Booking Execution Monitoring overview

page:

Life cycle status analysis

Execution and planning block analysis

## Freight orders delayed in transit

The system displays the information on a two-month rolling basis (current and previous month).

Screen Areas

## Information filter

This is custom documentation. For more information, please visit SAP Help Portal.

35


1/14/26, 2:47 PM

You can use the information filter on the top of the screen to select the information that the system displays in the chart

and table underneath. This enables you to view your filtered freight booking status data in different ways.

You can quickly see the number of freight bookings per life cycle status represented visually by a donut chart, for example,

1055 in process and 27 completed. Bar charts display the planning blocked freight bookings by transportation mode

category and the number of execution blocked freight bookings by traffic direction. The number of execution blocked

freight bookings by carrier and the number of freight bookings for destination country or region are depicted by line charts.

The following views are available:

## Graphics view

By default, the system displays the graphics filter. For example, you can select KPIs for the number of execution

blocked freight bookings per carrier and per traffic direction and the number of new freight bookings.

## Field view

You can change to a field filter (compact filter), where you can enter filter criteria such as the execution block and

the weight, volume, and time units in which you want to see the information.

## Bar chart

The chart in the middle of the screen gives you a comparison view of your KPIs by number of freight bookings per

transportation mode category and traffic direction. You can change the chart to a table or a combined table and chart. Use

the View By filter to view more specific information such as as ship-to party, source country or region, and whether

dangerous goods were transported. For example, you can quickly see the number of freight bookings transported by air

with planning block, and the category for that block.

## Table

The table at the bottom of the screen gives you more information on your KPIs, such as carrier, ship-to party, and life cycle

status. You can add or remove columns in Settings to give you the information you want to see, for example, execution

status and life cycle change date.

Selecting a freight booking in the table and pressing Change Freight Booking takes you directly to the freight booking in

Transportation Management (it opens in edit mode), where you can change the information to get a more desirable

outcome.

## Example

You want to review how many freight bookings sent by air have an execution block, and the execution block reason. You want to
determine the most common causes of execution blocking for goods transported by air. You navigate directly to the freight
booking to find out more details and take the appropriate action.

## Technical Basis

Your system administrator or another technical user can use the following technical information to change the detailed view.

Fiori ID: F2748

This detailed view uses the C_FrtBkgExecutionStsQ CDS view.

You must activate the C_FRTBKGEXECUTIONSTSQ_CDS OData service in the Gateway system.

## More Information

## Freight Booking Execution Monitoring

This is custom documentation. For more information, please visit SAP Help Portal.

36


1/14/26, 2:47 PM

Freight Booking Execution Status Query

Freight Booking Execution Event Query

Technical Name

## View Type

C_FRTBKGEXECUTIONQUERY Consumption view

## Purpose

This view contains key performance indicators (KPIs) to help you monitor your freight bookings with carriers to make sure they are

being executed on time, for example, KPIs on critical process statuses that lead to blocking situations in your operational business

that you need to solve urgently. It also contains each carrier’s on-time performance to aid when allocating future business.

## Prerequisites

Authorization is based on the standard Transportation Management authorization objects.

You’ll need either the Transp. Management Administrative Settings authorization object (T_ADMIN), or both the Transp.

Management Order Management & Planning (Purchase) authorization object (T_TOR_PUR) and the Transp. Management Order

Management & Planning (Execution) authorization object (T_TOR_EXE).

You’ll need the Business Partner: Purpose Completed authorization object (B_BUP_PCPT) for all business partners accessed in

this query.

In addition, you’ll need the Location: Access Based on Authorization Group authorization object (/SCMB/LOCB) for all locations

accessed in this query.

The following table lists the authorization objects with required fields and values:

Authorization

Check Condition

Object

Field

Value

## T_ADMIN

Check if the user has either T_ADMIN or both T_TOR_PUR and

T_TOR_EXE authorization objects.

## T_TOR_PUR

Check if the user has either T_ADMIN or both T_TOR_PUR and

T_TOR_EXE authorization objects.

## ACTVT

H1 (Deactivate)

This is custom documentation. For more information, please visit SAP Help Portal.

37

## ACTVT

03 (Display)


1/14/26, 2:47 PM

Authorization

Check Condition

Object

## T_TOR_EXE

Check if the user has either T_ADMIN or both T_TOR_PUR and

T_TOR_EXE authorization objects.

Field

Value

## TM_OC

TransportationOrderCategory

BO (Freight Booking)

## TM_OT

TransportationOrderType

## TM_XPORG

PurchasingOrgExternalID

## TM_XPGRP

PurchasingGroupExternalID

## TM_RP

TranspOrdResponsiblePerson

## TM_MOT

TransportationMode

## ACTVT

03 (Display)

## TM_OC

TransportationOrderCategory

BO (Freight Booking)

## TM_OT

TransportationOrderType

## TM_XEORG

PlngAndExecOrgExternalID

## TM_XEGRP

PlngAndExecGroupExternalID

## TM_RP

TranspOrdResponsiblePerson

## TM_MOT

TransportationMode

## ACTVT

03 (Display)

B_BUP_PCPT Only when the business purpose of the carrier, shipper, or ship-to

party is set to Completed (value of view field

CarrierBusPurposeIsCompleted = X or

ShipperBusPurposeIsCompleted = X or

ConsigneeBusPurposeIsCompleted = X), check if

authorization object B_BUP_PCPT has set field ACTVT to 03.

This is custom documentation. For more information, please visit SAP Help Portal.

38


1/14/26, 2:47 PM

Authorization

Check Condition

## Object

The system uses B_BUP_PCPT in the data destruction process
for Information Lifecycle Management.

Field

Value

## ACTVT

03 (Display)

/SCMB/LOCB Only when the business purpose of the event, source location, or

destination location is set to Completed

(_Location.IsBusinessPurposeCompleted = X or
_SourceLocation.IsBusinessPurposeCompleted = X or

_DestinationLocation.IsBusinessPurposeCompleted

= X), check field BRGRU against the value of view field

_Location.AuthorizationGroup or

_SourceLocation.AuthorizationGroup or

_DestinationLocation.AuthorizationGroup.

The system uses /SCMB/LOCB in the data destruction process
for Information Lifecycle Management

The field BRGRU enables display access to blocked locations

based on the settings you specify in the Define Authorization

Group Indicating Blocked Master Data Customizing activity.

## BRGRU

_Location.AuthorizationGroup

and

_SourceLocation.Authorizatio

and

_DestinationLocation.Authori

## ACTVT

03 (Display)

## Structure

## Business Objects

This view is built on the Transportation Order (TOR) business object with TransportationOrderCategory = BO.

## Main Input Parameters

The main input parameters are as follows:

## P_Language

Specifies the display language of the texts. The system automatically uses the system language as the P_Language.

## P_TodayDate

Specifies the timeframe of the data that you want to display. The system automatically uses the system date as the

P_TodayDate. This date is usually your local date. The system retrieves information from the beginning of previous month

up to the system date.

## P_DisplayTimeUnit

Specifies the units of time, for example, Event Delay in hours or minutes.

This is custom documentation. For more information, please visit SAP Help Portal.

39


1/14/26, 2:47 PM

## P_DisplayWeightUnit

Specifies the units of weight, for example, Gross Weight in kilograms.

## P_DisplayVolumeUnit

Specifies the units of volume, for example, Item Volume in meters cubed.

## P_DisplayQuantityUnit

Specifies the units of quantity, for example, Number of Containers in pieces.

## P_DisplayLengthUnit

Specifies the units of length, for example, Package Length in meters.

The unit parameters (time, weight, volume, quantity, and length) are mandatory.

## Measures and Attributes

The most important measures and attributes are listed below.

Keys and Identifiers

FreightBooking

TranspOrdExecution

TransportationOrderUUID

TransportationOrderEventUUID

Freight Booking Attributes

TransportationOrderType

MeansOfTransport

TransportationMode

PlngAndExecOrganization

PurchasingOrganization

TranspOrdLifeCycleStatus

TransportationOrderExecSts

Carrier

Shipper

## Consignee

TranspOrdIsDiscrepant

## DiscrepancyType

TranspOrdHasQtyDiscrepancy

SourceLocationName

## SourceLocationType

This is custom documentation. For more information, please visit SAP Help Portal.

40


1/14/26, 2:47 PM

SourceLocationCountry

DestinationLocationName

DestinationLocationType

DestinationLocationCountry

Freight Booking Execution Attributes

TranspOrdEventCode

TranspOrdEventStatus

TranspOrdEventReasonCode

Location

LocationType

## Country

GeographicalLocationLatitude

GeographicalLocationLongitude

TranspOrdEvtActualDateTime

TranspOrdEvtExpdEndDateTime

TranspOrdEvtActualDateTimeZone

TranspOrdEvtEstimatedDateTime

TranspOrdEventIsOnTime

TranspOrdEventIsDelayed

TranspOrdEventIsTimeRelevant

Freight Booking Measures

NumberOfTransportationOrders

NumberOfTimeRlvtTranspOrds

NumberOfOnTimeTranspOrds

NumberOfDelayedTranspOrds

TransportationOrderOnTimeRatio

Freight Booking Execution Measures

TranspOrdEventDelayInDspUnit

AverageTranspOrdEventDelay

NumberOfTranspOrdEvents

NumberOfTimeRlvtTranspOrdEvts

## NumberOfOnTimeTranspOrdEvents

This is custom documentation. For more information, please visit SAP Help Portal.

41


1/14/26, 2:47 PM

NumberOfDelayedTranspOrdEvents

TranspOrdEventOnTimeRatio

## Units

DisplayLengthUnit

DisplayQuantityUnit

DisplayTimeUnit

DisplayWeightUnit

DisplayVolumeUnit

Constraints

None.

Freight Booking Execution Status Query

Technical Name

## View Type

C_ FRTBKGEXECUTIONSTSQ Consumption view

## Purpose

This view contains the key performance indicators (KPIs) for your daily operational business, such as transports that are critically

blocked either in planning or execution, grouped by block reason. This helps you to determine the most common causes of

blocking and take the appropriate action. It also contains transports that are currently in transit and delayed so that you can

investigate and remedy the situation.

The view also has a workload analysis showing the number of transports in draft, new, in process, and in execution.

## Prerequisites

Authorization is based on the standard Transportation Management authorization objects.

You’ll need either the Transp. Management Administrative Settings authorization object (T_ADMIN), or both the Transp.

Management Order Management & Planning (Purchase) authorization object (T_TOR_PUR) and the Transp. Management Order

Management & Planning (Execution) authorization object (T_TOR_EXE).

You’ll need the Business Partner: Purpose Completed authorization object (B_BUP_PCPT) for all business partners accessed in

this query.

In addition, you’ll need the Location: Access Based on Authorization Group authorization object (/SCMB/LOCB) for all locations

accessed in this query.

The following table lists the authorization objects with required fields and values:

This is custom documentation. For more information, please visit SAP Help Portal.

42


1/14/26, 2:47 PM

Authorization

Check Condition

Object

Field

Value

## T_ADMIN

Check if the user has either T_ADMIN or both T_TOR_PUR and

T_TOR_EXE authorization objects.

## T_TOR_PUR

Check if the user has either T_ADMIN or both T_TOR_PUR and

T_TOR_EXE authorization objects.

## ACTVT

H1 (Deactivate)

## ACTVT

03 (Display)

## TM_OC

TransportationOrderCategory

BO (Freight Booking)

## TM_OT

TransportationOrderType

## TM_XPORG

PurchasingOrgExternalID

## TM_XPGRP

PurchasingGroupExternalID

## TM_RP

TranspOrdResponsiblePerson

## TM_MOT

TransportationMode

## ACTVT

03 (Display)

## TM_OC

TransportationOrderCategory

BO (Freight Booking)

## TM_OT

TransportationOrderType

## T_TOR_EXE

Check if the user has either T_ADMIN or both T_TOR_PUR and

T_TOR_EXE authorization objects.

This is custom documentation. For more information, please visit SAP Help Portal.

43


Field

## Value

## TM_XEORG

PlngAndExecOrgExternalID

## TM_XEGRP

PlngAndExecGroupExternalID

## TM_RP

TranspOrdResponsiblePerson

## TM_MOT

TransportationMode

## ACTVT

03 (Display)

## ACTVT

03 (Display)

1/14/26, 2:47 PM

Authorization

Check Condition

## Object

B_BUP_PCPT Only when the business purpose of the carrier, shipper, or ship-to

party is set to Completed (value of view field

CarrierBusPurposeIsCompleted = X or

ShipperBusPurposeIsCompleted = X or

ConsigneeBusPurposeIsCompleted = X), check if
authorization object B_BUP_PCPT has set field ACTVT to 03.

The system uses B_BUP_PCPT in the data destruction process

for Information Lifecycle Management.

/SCMB/LOCB Only when the business purpose of the source location or

destination location is set to Completed
(_SourceLocation.IsBusinessPurposeCompleted = X

or

_DestinationLocation.IsBusinessPurposeCompleted

= X), check field BRGRU against the value of view field

_SourceLocation.AuthorizationGroup or

_DestinationLocation.AuthorizationGroup.

The system uses /SCMB/LOCB in the data destruction process
for Information Lifecycle Management

The field BRGRU enables display access to blocked locations

based on the settings you specify in the Define Authorization

Group Indicating Blocked Master Data Customizing activity.

## BRGRU

_SourceLocation.Authorizatio

and

_DestinationLocation.Authori

## ACTVT

03 (Display)

## Structure

## Business Objects

This view is built on the Transportation Order (TOR) business object with TransportationOrderCategory = BO.

## Main Input Parameters

This is custom documentation. For more information, please visit SAP Help Portal.

44


1/14/26, 2:47 PM

The main input parameters are as follows:

## P_Language

Specifies the display language of the texts. The system automatically uses the system language as the P_Language.

## P_TodayDate

Specifies the timeframe of the data that you want to display. The system automatically uses the system date as the

P_TodayDate. This date is usually your local date. The system retrieves information from the beginning of previous month

up to the system date.

## P_DisplayTimeUnit

Specifies the units of time, for example, Event Delay in hours or minutes.

## P_DisplayWeightUnit

Specifies the units of weight, for example, Gross Weight in kilograms.

## P_DisplayVolumeUnit

Specifies the units of volume, for example, Item Volume in meters cubed.

## P_DisplayQuantityUnit

Specifies the units of quantity, for example, Number of Containers in pieces.

## P_DisplayLengthUnit

Specifies the units of length, for example, Package Length in meters.

The unit parameters (time, weight, volume, quantity, and length) are mandatory.

## Measures and Attributes

The most important measures and attributes are listed below.

Keys and Identifiers

FreightBooking

TranspOrdExecution

TransportationOrderUUID

TransportationOrderEventUUID

Freight Booking Attributes

TransportationOrderType

MeansOfTransport

TransportationMode

PlngAndExecOrganization

PurchasingOrganization

TranspOrdLifeCycleStatus

## TransportationOrderExecSts

This is custom documentation. For more information, please visit SAP Help Portal.

45


1/14/26, 2:47 PM

Carrier

Shipper

## Consignee

TranspOrdIsInTransit

TranspOrdIsDlydInTransit

TranspOrdPlanningBlock

TranspOrdPlanningBlockRsn

TranspOrdExecutionIsBlocked

TranspOrdExecBlockReason

InvoicingIsBlocked

SourceLocationName

SourceLocationType

SourceLocationCountry

DestinationLocationName

DestinationLocationType

DestinationLocationCountry

Freight Booking Measures

NumberOfTransportationOrders

NumberOfTranspOrdsInTransit

NmbrOfDelayedTranspOrdsInTrnst

TranspOrdDelayInDspUnit

TranspOrdGrossWeightInDspUnit

TranspOrdGrossVolumeInDspUnit

TranspOrdQuantityInDisplayUnit

TranspOrdNumberOfCtnsInDspUnit

NumberOfPlngBlkdTranspOrds

NumberOfExecBlkdTranspOrds

## Units

DisplayLengthUnit

DisplayQuantityUnit

DisplayTimeUnit

DisplayWeightUnit

## DisplayVolumeUnit

This is custom documentation. For more information, please visit SAP Help Portal.

46


1/14/26, 2:47 PM

Constraints

None.

## Freight Booking Quantity Analysis

As a transportation manager for a shipper, you work with carriers to transport your products to your customers. You need to

monitor your freight bookings with carriers to make sure they are being executed on time. A freight booking contains the logistical

plan for the transportation of goods, for example, fixed departure times of a ship. You use a freight booking to reserve freight space

on a ship or in an airplane, and it also contains information on how the plan is actually carried out.

You can use the Freight Booking Quantity Analysis overview page to provide you with the key performance indicators (KPIs) that

you need to manage your execution business. At a glance, you can see all the vital data you need for your daily decision-making.

The overview page provides you with KPIs for the current and previous month.

## Key Features

## Gross Weight Distribution

You can view a chart showing how gross weight distribution for completed freight bookings (that is, with a freight booking

life cycle status of Completed) has increased or decreased in each completion week (current and previous month only).

The total gross weight distribution also appears at the top, for example, 190K.

## Gross Volume Distribution

You can view a chart showing how gross volume distribution for completed freight bookings has increased or decreased in

each completion week (current and previous month only). The total gross volume distribution also appears at the top, for

example, 200K.

## Quantity Distribution

You can view a chart showing how quantity distribution for completed freight bookings has increased or decreased in each

completion week (current and previous month only). The total gross quantity distribution also appears at the top, for

example, 175K.

## Transportation Mode Category Analysis

You can see a chart with gross weight and gross volume as axes, plus the total number of freight bookings, for each

transportation mode category for completed freight bookings. This can help you identify the most effective method of

transportation.

## Logistic Network Analysis

You can review a table showing source and destination countries or regions, and total gross weight for completed freight

bookings. This identifies where you have transported most goods in the current and previous months. The table is sorted in

descending order of gross weight.

## Carrier Quantity Analysis

You can view the total gross weight, gross volume, and container count per carrier for completed freight bookings. This

gives you information on which carriers you are using the most. The highest weight appears at the top.

## Shipper Quantity Analysis

You can view the total gross weight, gross volume, and container count per shipper for completed freight bookings. This

gives you information on which shippers you are using the most. The highest weight appears at the top.

## Ship-To Party Quantity Analysis

This is custom documentation. For more information, please visit SAP Help Portal.

47


1/14/26, 2:47 PM

You can view the total gross weight, gross volume, and container count per ship-to party for completed freight bookings.

This gives you information on which ship-to parties you are using the most. The highest weight appears at the top.

## Utilization Distribution

You can see the lowest average utilization per carrier (expressed as a percentage) for completed freight bookings. This

helps you assess carriers’ performance and capacity. The lowest utilization percentage appears at the top.

## Quantity Analysis

You can view a table showing the gross volume and gross weight transported for each transportation mode category (for

example, road and air) for completed freight bookings. You can use this information when deciding on the most efficient

method of transportation. The table is sorted in descending order of gross weight.

## Distance Analysis

You can see the total net duration and total distance for transported goods for each transportation mode category (for

example, sea and air) for completed freight bookings. You can use this information when deciding on the most efficient

method of transportation. The greatest distance appears at the top.

## Detailed View

You can use visual features to analyze the KPI information at a more detailed level. Selecting a card header or information line

takes you to the detailed view, which presents summary information graphically and also in a table, from which you can navigate

directly to the freight booking in the Transportation Management system and change it if necessary.

Supported Device Types

Desktop

## Tablet

Smartphone

Technical Basis

Fiori ID: F2678

This overview page uses the C_FrtBkgQuantityQuery CDS view.

You must activate the C_FRTBKGQUANTITYQUERY_CDS OData service in the Gateway system.

More Information

## Subject

## More Information

Freight booking overview for a business person

## Freight Booking

Freight booking quantity analysis detailed view for a business

Freight Booking Quantity Detailed View

person

Underlying technical object for a technical person

C_FrtBkgQuantityQuery CDS view

## Freight Booking Quantity Query

This is custom documentation. For more information, please visit SAP Help Portal.

48


1/14/26, 2:47 PM

## Freight Booking Quantity Detailed View

You can get a detailed analysis of each key performance indicator (KPI). You can have instant and flexible access to the information

you need to analyze the execution of your freight bookings and change it if necessary by navigating directly to the relevant

document in the Transportation Management (TM) system.

The system displays the information on a two-month rolling basis (current and previous month).

Screen Areas

## Information filter

You can use the information filter on the top of the screen to select the information that the system displays in the chart

and table underneath. This enables you to view your filtered freight booking data in different ways.

You can quickly see the total gross weight of goods transported per carrier in the current and previous month represented

visually by a line chart, and the number of freight bookings per transportation mode category depicted by a bar chart.

The following views are available:

## Graphics view

By default, the system displays the graphics filter. For example, you can select KPIs for gross weight per carrier in

the current and previous month and the number of freight bookings per transportation mode category.

## Field view

You can change to a field filter (compact filter), where you can enter filter criteria such as the weight, volume, and

time units in which you want to see the information.

## Bar chart

The chart in the middle of the screen gives you a comparison view of your KPIs by by gross weight per transportation mode

category for completion weeks in the current and previous month. You can change the chart to a table or a combined table

and chart. Use the View By filter to view more specific information such as carrier, destination country or region, and life

cycle status. For example, you can quickly see the total gross weight of goods transported by sea in each completion week

of the current and previous month, and by which carriers.

## Table

The table at the bottom of the screen gives you more information on your KPIs, such as carrier, number of containers, and

source and destination countries or regions. You can add or remove columns in Settings to give you the information you

want to see, for example, completion date, destination location, and ship-to party.

Selecting a freight booking in the table and pressing Change Freight Booking takes you directly to the freight booking in

Transportation Management. The document opens in edit mode.

## Example

You want to assess the most efficient mode of transport to a specific location in China. Looking at the current and previous
months, you can see the total gross weight of goods transported by air, road, and sea. You check the destination location and see
that most goods were transported by sea. Navigating directly to the freight booking, you confirm that sea was indeed the most
efficient mode of transport, with all bookings being completed on time.

## Technical Basis

Your system administrator or another technical user can use the following technical information to change the detailed view.

This is custom documentation. For more information, please visit SAP Help Portal.

49


1/14/26, 2:47 PM

Fiori ID: F2749

This detailed view uses the C_FrtBkgQuantityQuery CDS view.

You must activate the C_ FRTBKGQUANTITYQUERY_CDS OData service in the Gateway system.

## More Information

Freight Booking Quantity Analysis

Freight Booking Quantity Detailed View

Freight Booking Quantity Query

Technical Name

## View Type

C_FRTBKGQUANTITYQUERY Consumption view

## Purpose

This view contains key performance indicators (KPIs) to help you monitor your freight bookings with carriers. It contains the

current weights, volumes, and numbers being transported on a weekly basis by each carrier, shipper, and ship-to party, as well as

by transportation mode, and source and destination country or region. The view also calculates each carrier’s utilization.

## Prerequisites

Authorization is based on the standard Transportation Management authorization objects.

You’ll need either the Transp. Management Administrative Settings authorization object (T_ADMIN), or both the Transp.

Management Order Management & Planning (Purchase) authorization object (T_TOR_PUR) and the Transp. Management Order

Management & Planning (Execution) authorization object (T_TOR_EXE).

You’ll need the Business Partner: Purpose Completed authorization object (B_BUP_PCPT) for all business partners accessed in

this query.

In addition, you’ll need the Location: Access Based on Authorization Group authorization object (/SCMB/LOCB) for all locations

accessed in this query.

The following table lists the authorization objects with required fields and values:

Authorization

Check Condition

Object

Field

Value

## T_ADMIN

Check if the user has either T_ADMIN or both T_TOR_PUR and

T_TOR_EXE authorization objects.

This is custom documentation. For more information, please visit SAP Help Portal.

50

## ACTVT

H1 (Deactivate)


1/14/26, 2:47 PM

Authorization

Check Condition

Object

Field

## Value

## T_TOR_PUR

Check if the user has either T_ADMIN or both T_TOR_PUR and

T_TOR_EXE authorization objects.

## T_TOR_EXE

Check if the user has either T_ADMIN or both T_TOR_PUR and
T_TOR_EXE authorization objects.

## TM_OC

TransportationOrderCategory

BO (Freight Booking)

## TM_OT

TransportationOrderType

## TM_XPORG

PurchasingOrgExternalID

## TM_XPGRP

PurchasingGroupExternalID

## TM_RP

TranspOrdResponsiblePerson

## TM_MOT

TransportationMode

## ACTVT

03 (Display)

## TM_OC

TransportationOrderCategory

BO (Freight Booking)

## TM_OT

TransportationOrderType

## TM_XEORG

PlngAndExecOrgExternalID

## TM_XEGRP

PlngAndExecGroupExternalID

## TM_RP

TranspOrdResponsiblePerson

## TM_MOT

## TransportationMode

This is custom documentation. For more information, please visit SAP Help Portal.

51


1/14/26, 2:47 PM

Authorization

Check Condition

Object

Field

Value

## ACTVT

03 (Display)

B_BUP_PCPT Only when the business purpose of the carrier, shipper, or ship-to

party is set to Completed (value of view field

CarrierBusPurposeIsCompleted = X or

ShipperBusPurposeIsCompleted = X or
ConsigneeBusPurposeIsCompleted = X), check if

authorization object B_BUP_PCPT has set field ACTVT to 03.

The system uses B_BUP_PCPT in the data destruction process

for Information Lifecycle Management.

/SCMB/LOCB Only when the business purpose of the source location or

## ACTVT

03 (Display)

destination location is set to Completed

(_SourceLocation.IsBusinessPurposeCompleted = X

or

_DestinationLocation.IsBusinessPurposeCompleted

= X), check field BRGRU against the value of view field

_SourceLocation.AuthorizationGroup or
_DestinationLocation.AuthorizationGroup.

The system uses /SCMB/LOCB in the data destruction process

for Information Lifecycle Management

The field BRGRU enables display access to blocked locations

based on the settings you specify in the Define Authorization

Group Indicating Blocked Master Data Customizing activity.

## BRGRU

_SourceLocation.Authorizatio

and

_DestinationLocation.Authori

## ACTVT

03 (Display)

## Structure

## Business Objects

This view is built on the Transportation Order (TOR) business object with TransportationOrderCategory = BO.

## Main Input Parameters

The main input parameters are as follows:

## P_Language

Specifies the display language of the texts. The system automatically uses the system language as the P_Language.

## P_TodayDate

Specifies the timeframe of the data that you want to display. The system automatically uses the system date as the

P_TodayDate. This date is usually your local date. The system retrieves information from the beginning of previous month

up to the system date.

This is custom documentation. For more information, please visit SAP Help Portal.

52


1/14/26, 2:47 PM

## P_DisplayTimeUnit

Specifies the units of time, for example, Event Delay in hours or minutes.

## P_DisplayWeightUnit

Specifies the units of weight, for example, Gross Weight in kilograms.

## P_DisplayVolumeUnit

Specifies the units of volume, for example, Item Volume in meters cubed.

## P_DisplayQuantityUnit

Specifies the units of quantity, for example, Number of Containers in pieces.

## P_DisplayLengthUnit

Specifies the units of length, for example, Package Length in meters.

The unit parameters (time, weight, volume, quantity, and length) are mandatory.

## Measures and Attributes

The most important measures and attributes are listed below.

Keys and Identifiers

TransportationOrder

TransportationOrderStage

TransportationOrderUUID

SourceLocationUUID

DestinationLocationUUID

Freight Booking Attributes

TransportationOrderCategory

TransportationOrderType

DangerousGoodsAreContained

TranspOrdShippingType

TranspOrdTrafficDirection

MeansOfTransport

TransportationMode

TransportationModeCategory

TranspOrdLifeCycleStatus

PlngAndExecOrganization

PlngAndExecGroup

## PurchasingOrganization

This is custom documentation. For more information, please visit SAP Help Portal.

53


1/14/26, 2:47 PM

## PurchasingGroup

TranspOrdCompletionDateTime

TranspOrdCompletionDate

TranspOrdCompletionYearWeek

TranspOrdCompletionYearMonth

TranspOrdCompletionYearQuarter

TranspOrdCompletionYear

ChangedDateTime

## Carrier

CarrierOriginOfEntry

Shipper

## Consignee

SourceLocation

SourceLocationType

SourceLocationCountry

SourceLocationRegion

DestinationLocation

DestinationLocationType

DestinationLocationCountry

DestinationLocationRegion

Freight Booking Stage Attributes

TranspOrdStageSrceLocation

TranspOrdStageSrceLocationType

TranspOrdStageSrceLocCntry

TranspOrdStageSrceLocRgn

TranspOrdStageDestLocation

TranspOrdStageDestLocationType

TranspOrdStageDestLocCntry

TranspOrdStageDestLocRgn

Freight Booking Measures

NumberOfTransportationOrders

TranspOrdMaxUtilznRatio

## TranspOrdMaxUtilznMassRatio

This is custom documentation. For more information, please visit SAP Help Portal.

54


1/14/26, 2:47 PM

TranspOrdMaxUtilznVolumeRatio

TranspOrdNumberOfCtnsInDspUnit

TranspOrdGrossWeightInDspUnit

TranspOrdGrossVolumeInDspUnit

TranspOrdQuantityInDisplayUnit

Freight Booking Stage Measures

NumberOfTranspOrdStages

TranspOrdStageMaxUtilznRatio

TranspOrdStageUtilznVolRatio

TranspOrdStageUtilznMassRatio

TranspOrdStageDstncInDspUnit

TranspOrdStageNetDurnInDspUnit

## Units

DisplayLengthUnit

DisplayQuantityUnit

DisplayTimeUnit

DisplayWeightUnit

DisplayVolumeUnit

Constraints

None.

## Freight Order Execution Monitoring

As a transportation manager for a shipper, you work with carriers to transport your products to your customers. You can use the

Freight Order Execution Monitoring overview page to provide you with the key performance indicators (KPIs) that you need to

manage your execution business. At a glance, you can see all the vital data you need for your daily decision-making. For example,

you can see KPIs on critical process statuses that lead to blocking situations in your operational business that may need your

urgent attention. A carrier’s on-time performance KPI also helps you make decisions when allocating future business.

The overview page provides you with KPIs for the current and previous month.

## Key Features

This overview page is based on two CDS views (data sources), each generating different cards.

The following features are available with data source 1 (C_FrtOrdExecutionStsQ CDS view):

## Life Cycle Status Analysis

This is custom documentation. For more information, please visit SAP Help Portal.

55


1/14/26, 2:47 PM

You can view the number of execution-relevant freight orders, grouped by freight order life cycle status. Execution-relevant

freight orders have the execution status In Execution (03) and have a departure event but no arrival event at the final

destination.

You can see the number of freight bookings for each life cycle status (Draft (00), New (01), or In Process (02)), sorted in

descending order.

## Execution Block Analysis

You can review all freight orders with an execution block, grouped by execution block reason. This helps you to determine

the most common causes of execution blocking and take the appropriate action.

You specify execution block reasons in the TM Freight Order transaction; if you haven’t done this, the system automatically

creates them, based on the blocking category.

The list is sorted in descending order.

## Planning Block Analysis

You can review all freight orders with a planning block, grouped by planning block reason. This helps you to determine the

most common causes of planning blocking and take the appropriate action.

You specify execution block reasons in the TM Freight Order transaction ; if you haven’t done this, the system automatically

creates them, based on the blocking category.

The list is sorted in descending order.

## Delayed Freight Orders in Transit

You can view freight orders that are delayed in transit, that is, if their latest, time-relevant event is delayed (both the

expected and actual date and time fields are available and the event status is Reported). The delay is the time difference

between the actual date and the expected date.

You can see the total number of freight orders and then drill down to view details such asFreight Order ID, Means of

Transport, Gross Weight, and Delay. You specify the units as parameters in the relevant CDS query view.

You can also navigate directly to the related freight order transaction by selecting the first line or the header line on the

details view.

The following features are available with data source 2 (C_FrtOrdExecutionQuery CDS view):

## Blocking Discrepancies

You can review the discrepant freight order events that led to a block, sorted by event code and discrepancy type (such as

delivery of item, late, or delay). The discrepancy type with the most blocking events is at the top.

## Non-Blocking Discrepancies

You can see the discrepant freight order events that didn’t result in a block, sorted by event code and discrepancy type

(such as arrival at destination, departure, or loading end). The discrepancy type with the most non-blocking events is at the

top.

## Carrier On Time Performance

You can view the percentage of freight orders that each carrier delivered on time. You can also see this expressed in

numbers, for example, 6 / 14 were on time. A freight order is on time if all its events are classed as on time, otherwise it is

classed as delayed. This helps you identify the most efficient carriers.

The calculation for all the on time performance cards takes into account all time-relevant events where both expected and

actual date and time fields are available, and where the event status is Reported.

## Location On Time Performance

This is custom documentation. For more information, please visit SAP Help Portal.

56


1/14/26, 2:47 PM

This shows the percentage of on time freight order events for each location, sorted by the transportation order events on

time ratio. You can also see this expressed in numbers, for example, 6 / 8 events were on time. This helps you understand

how individual locations are performing. The lowest percentage is at the top.

## Activity On Time Performance

You can review the percentage of on time freight order events for each event code (such as loading or unloading), with the

lowest number at the top. You can also see this expressed in numbers, for example, 12 / 27 events took place on time. You

can use this information to identify potential bottlenecks.

## Unexpected Events

You can monitor unexpected events that took place within the freight order, grouped by event code (such as accident or

delay), with the highest number at the top. This information may prove vital in taking preventative measures to avoid such

events in the future.

## Detailed View

You can use visual features to analyze the KPI information at a more detailed level. Selecting a card header or information line

takes you to the detailed view, which presents summary information graphically and also in a table, from which you can navigate

directly to the freight order in the Transportation Management system and change it if necessary.

Selecting the blocking and non-blocking discrepancies, carrier, location, and activity on time performance, and unexpected events

cards takes you to the Freight Order Execution Detailed View. Selecting the life cycle status analysis, execution and planning

block analysis, and freight bookings delayed in transit cards takes you to the Freight Order Execution Status Detailed View

Supported Device Types

Desktop

## Tablet

Smartphone

Technical Basis

Fiori ID: F2675

This overview page uses the following CDS views:

C_FrtOrdExecutionStsQ (data source 1)

C_FrtOrdExecutionQuery (data source 2)

You must activate the following OData services in the Gateway system:

C_FRTORDEXECUTIONSTSQ_CDS (data source 1)

C_FRTORDEXECUTIONQUERY_CDS (data source 2)

More Information

## Subject

## More Information

Freight order management overview for a business person

## Freight Order Management

This is custom documentation. For more information, please visit SAP Help Portal.

57


1/14/26, 2:47 PM

## Subject

## More Information

Freight order execution monitoring detailed views for a business

Freight Order Execution Detailed View

person

Freight Order Execution Status Detailed View

Underlying technical objects for a technical person

C_FrtOrdExecutionStsQ CDS view

Freight Order Execution Status Query

C_FrtOrdExecutionQuery CDS view

Freight Order Execution Event Query

## Freight Order Execution Detailed View

You can get a detailed analysis of each key performance indicator (KPI). You can have instant and flexible access to the information

you need to analyze your freight order execution and change it if necessary by navigating directly to the relevant document in the

Transportation Management (TM) system.

This detailed view provides further information on the following cards on the Freight Order Execution Monitoring overview page:

Blocking and non-blocking discrepancies

Carrier, location, and activity on time performance

## Unexpected events

The system displays the information on a two-month rolling basis (current and previous month).

Screen Areas

## Information filter

You can use the information filter on the top of the screen to select the information that the system displays in the chart

and table underneath. This enables you to view your filtered freight order data in different ways.

You can quickly see the event on time ratio by location and carrier, represented visually by a bar chart and a line chart

respectively. Donut charts display the ratio of on time events per event (such as arrival at destination, departure, or loading

end), expressed as a percentage, and the number of events broken down into discrepancy type leading to a block and

discrepancy type not leading to a block.

The following views are available:

## Graphics view

By default, the system displays the graphics filter. For example, you can select KPIs for the on time ratio of arrival

events, or for a specific location.

## Field view

You can change to a field filter (compact filter), where you can enter filter criteria such as event status and the

weight, volume, and time units in which you want to see the information.

## Bar chart

The chart in the middle of the screen gives you a comparison view of your KPIs by number of freight orders per

transportation mode category and traffic direction. You can change the chart to a table or a combined table and chart. Use

This is custom documentation. For more information, please visit SAP Help Portal.

58


1/14/26, 2:47 PM

the View By filter to view more specific information such as discrepancy, discrepancy type, and event. For example, you can

quickly see the number of freight orders transported by road that arrived at their destination with no discrepant events.

## Table

The table at the bottom of the screen gives you more information on your KPIs, such as destination country or region,

event, event status, and number of delayed freight orders. You can add or remove columns in Settings to give you the

information you want to see, for example, ship-to party and expected end date.

Selecting a freight order in the table and pressing Change Freight Order takes you directly to the freight order in

Transportation Management (it opens in edit mode), where you can change the information to get a more desirable

outcome.

## Example

You want to review the performance of carriers and see whether they delivered goods on time. This helps you identify the most
efficient carriers. You see that two carriers had a much lower ratio that the others. You look at the events, event statuses, and any
discrepant events. You then navigate directly to the freight order to see if there were any extenuating circumstances. This
information helps you make decisions when allocating future business.

## Technical Basis

Your system administrator or another technical user can use the following technical information to change the detailed view.

Fiori ID: F2750

This detailed view uses the C_FrtOrdExecutionQuery CDS view.

You must activate the C_FRTORDEXECUTIONQUERY_CDS OData service in the Gateway system.

## More Information

Freight Order Execution Monitoring

Freight Order Execution Event Query

## Freight Order Execution Status Detailed View

You can get a detailed analysis of each key performance indicator (KPI). You can have instant and flexible access to the information

you need to analyze your freight order execution status and change it if necessary by navigating directly to the relevant document

in the Transportation Management (TM) system.

This detailed view provides further information on the following cards on the Freight Order Execution Monitoring overview page:

Life cycle status analysis

Execution and planning block analysis

## Freight orders delayed in transit

The system displays the information on a two-month rolling basis (current and previous month).

## Screen Areas

This is custom documentation. For more information, please visit SAP Help Portal.

59


1/14/26, 2:47 PM

## Information filter

You can use the information filter on the top of the screen to select the information that the system displays in the chart

and table underneath. This enables you to view your filtered freight order status data in different ways.

You can quickly see the number of freight orders per life cycle status represented visually by a donut chart, for example,

1055 in process and 27 completed. Bar charts display the number of planning blocked freight orders by transportation

mode category and the number of execution blocked freight orders by traffic direction. The number of execution blocked

freight orders by carrier and the number of freight orders per destination country or region are depicted by line charts.

The following views are available:

## Graphics view

By default, the system displays the graphics filter. For example, you can select KPIs for the number of execution

blocked freight orders per carrier and per traffic direction and the number of new freight orders.

## Field view

You can change to a field filter (compact filter), where you can enter filter criteria such as the execution block and

the weight, volume, and time units in which you want to see the information.

## Bar chart

The chart in the middle of the screen gives you a comparison view of your KPIs by number of freight orders per

transportation mode category and traffic direction. You can change the chart to a table or a combined table and chart. Use

the View By filter to view more specific information such as as ship-to party, source country or region, and whether

dangerous goods were transported. For example, you can quickly see the number of freight orders transported by air with

planning block, and the category for that block.

## Table

The table at the bottom of the screen gives you more information on your KPIs, such as carrier, ship-to party, and life cycle

status. You can add or remove columns in Settings to give you the information you want to see, for example, execution

status and life cycle change date.

Selecting a freight order in the table and pressing Change Freight Order takes you directly to the freight order in

Transportation Management (it opens in edit mode), where you can change the information to get a more desirable

outcome.

## Example

You want to review how many freight orders sent by air have an execution block, and the execution block reason. You want to
determine the most common causes of execution blocking for goods transported by air. You navigate directly to the freight order
to find out more details and take the appropriate action.

## Technical Basis

Your system administrator or another technical user can use the following technical information to change the detailed view.

Fiori ID: F2751

This detailed view uses the C_FrtOrdExecutionStsQ CDS view.

You must activate the C_FRTORDEXECUTIONSTSQ_CDS OData service in the Gateway system.

## More Information

This is custom documentation. For more information, please visit SAP Help Portal.

60


1/14/26, 2:47 PM

Freight Order Execution Monitoring

Freight Order Execution Status Query

Freight Order Execution Event Query

Technical Name

## View Type

C_ FRTORDEXECUTIONQUERY Consumption view

## Purpose

This view contains key performance indicators (KPIs) to help you monitor your freight orders with carriers to make sure they are

being executed on time, for example, KPIs on critical process statuses that lead to blocking situations in your operational business

that you need to solve urgently. It also contains each carrier’s on-time performance to aid when allocating future business.

## Prerequisites

Authorization is based on the standard Transportation Management authorization objects.

You’ll need either the Transp. Management Administrative Settings authorization object (T_ADMIN), or both the Transp.

Management Order Management & Planning (Purchase) authorization object (T_TOR_PUR) and the Transp. Management Order

Management & Planning (Execution) authorization object (T_TOR_EXE).

You’ll need the Business Partner: Purpose Completed authorization object (B_BUP_PCPT) for all business partners accessed in

this query.

In addition, you’ll need the Location: Access Based on Authorization Group authorization object (/SCMB/LOCB) for all locations

accessed in this query.

The following table lists the authorization objects with required fields and values:

Authorization

Check Condition

Object

Field

Value

## T_ADMIN

Check if the user has either T_ADMIN or both T_TOR_PUR and

T_TOR_EXE authorization objects.

## T_TOR_PUR

Check if the user has either T_ADMIN or both T_TOR_PUR and

T_TOR_EXE authorization objects.

## ACTVT

H1 (Deactivate)

This is custom documentation. For more information, please visit SAP Help Portal.

61


1/14/26, 2:47 PM

Authorization

Check Condition

Object

## T_TOR_EXE

Check if the user has either T_ADMIN or both T_TOR_PUR and

T_TOR_EXE authorization objects.

Field

Value

## ACTVT

03 (Display)

## TM_OC

TransportationOrderCategory

TO (Freight Order)

## TM_OT

TransportationOrderType

## TM_XPORG

PurchasingOrgExternalID

## TM_XPGRP

PurchasingGroupExternalID

## TM_RP

TranspOrdResponsiblePerson

## TM_MOT

TransportationMode

## ACTVT

03 (Display)

## TM_OC

TransportationOrderCategory

TO (Freight Order)

## TM_OT

TransportationOrderType

## TM_XEORG

PlngAndExecOrgExternalID

## TM_XEGRP

PlngAndExecGroupExternalID

## TM_RP

TranspOrdResponsiblePerson

## TM_MOT

TransportationMode

## ACTVT

03 (Display)

B_BUP_PCPT Only when the business purpose of the carrier, shipper. or ship-to

party is set to Completed (value of view field

CarrierBusPurposeIsCompleted = X or

ShipperBusPurposeIsCompleted = X or

ConsigneeBusPurposeIsCompleted = X), check if

authorization object B_BUP_PCPT has set field ACTVT to 03.

This is custom documentation. For more information, please visit SAP Help Portal.

62


1/14/26, 2:47 PM

Authorization

Check Condition

## Object

The system uses B_BUP_PCPT in the data destruction process
for Information Lifecycle Management.

Field

Value

## ACTVT

03 (Display)

/SCMB/LOCB Only when the business purpose of the event, source location, or

destination location is set to Completed

(_Location.IsBusinessPurposeCompleted = X or

_SourceLocation.IsBusinessPurposeCompleted = X or

_DestinationLocation.IsBusinessPurposeCompleted

= X), check field BRGRU against the value of view field

_Location.AuthorizationGroup or

_SourceLocation.AuthorizationGroup or
_DestinationLocation.AuthorizationGroup.

The system uses /SCMB/LOCB in the data destruction process

for Information Lifecycle Management

The field BRGRU enables display access to blocked locations

based on the settings you specify in the Define Authorization

Group Indicating Blocked Master Data Customizing activity.

## BRGRU

_Location.AuthorizationGroup

and

_SourceLocation.Authorizatio

and

_DestinationLocation.Authori

## ACTVT

03 (Display)

## Structure

## Business Objects

This view is built on the Transportation Order (TOR) business object with TransportationOrderCategory = TO.

## Main Input Parameters

The main input parameters are as follows:

## P_Language

Specifies the display language of the texts. The system automatically uses the system language as the P_Language.

## P_TodayDate

Specifies the timeframe of the data that you want to display. The system automatically uses the system date as the

P_TodayDate. This date is usually your local date. The system retrieves information from the beginning of previous month

up to the system date.

## P_DisplayTimeUnit

Specifies the units of time, for example, Event Delay in hours or minutes.

This is custom documentation. For more information, please visit SAP Help Portal.

63


1/14/26, 2:47 PM

## P_DisplayWeightUnit

Specifies the units of weight, for example, Gross Weight in kilograms.

## P_DisplayVolumeUnit

Specifies the units of volume, for example, Item Volume in meters cubed.

## P_DisplayQuantityUnit

Specifies the units of quantity, for example, Number of Containers in pieces.

## P_DisplayLengthUnit

Specifies the units of length, for example, Package Length in meters.

The unit parameters (time, weight, volume, quantity, and length) are mandatory.

## Measures and Attributes

The most important measures and attributes are listed below.

Keys and Identifiers

FreightOrder

TranspOrdExecution

TransportationOrderUUID

TransportationOrderEventUUID

Freight Order Attributes

TransportationOrderType

MeansOfTransport

TransportationMode

PlngAndExecOrganization

PurchasingOrganization

TranspOrdLifeCycleStatus

TransportationOrderExecSts

Carrier

Shipper

## Consignee

TranspOrdIsDiscrepant

## DiscrepancyType

TranspOrdHasQtyDiscrepancy

SourceLocationName

## SourceLocationType

This is custom documentation. For more information, please visit SAP Help Portal.

64


1/14/26, 2:47 PM

SourceLocationCountry

DestinationLocationName

DestinationLocationType

DestinationLocationCountry

Freight Order Execution Attributes

TranspOrdEventCode

TranspOrdEventStatus

TranspOrdEventReasonCode

Location

LocationType

## Country

GeographicalLocationLatitude

GeographicalLocationLongitude

TranspOrdEvtActualDateTime

TranspOrdEvtExpdEndDateTime

TranspOrdEvtActualDateTimeZone

TranspOrdEvtEstimatedDateTime

TranspOrdEventIsOnTime

TranspOrdEventIsDelayed

TranspOrdEventIsTimeRelevant

Freight Order Measures

NumberOfTransportationOrders

NumberOfTimeRlvtTranspOrds

NumberOfOnTimeTranspOrds

NumberOfDelayedTranspOrds

TransportationOrderOnTimeRatio

Freight Order Execution Measures

TranspOrdEventDelayInDspUnit

AverageTranspOrdEventDelay

NumberOfTranspOrdEvents

NumberOfTimeRlvtTranspOrdEvts

## NumberOfOnTimeTranspOrdEvents

This is custom documentation. For more information, please visit SAP Help Portal.

65


1/14/26, 2:47 PM

NumberOfDelayedTranspOrdEvents

TranspOrdEventOnTimeRatio

## Units

DisplayLengthUnit

DisplayQuantityUnit

DisplayTimeUnit

DisplayWeightUnit

DisplayVolumeUnit

Constraints

None.

Freight Order Execution Status Query

Technical Name

## View Type

C_ FRTORDEXECUTIONSTSQ Consumption view

## Purpose

This view contains the key performance indicators (KPIs) for your daily operational business, such as transports that are critically

blocked either in planning or execution, grouped by block reason. This helps you to determine the most common causes of

blocking and take the appropriate action. It also contains transports that are currently in transit and delayed so that you can

investigate and sort out the situation.

The view also has a workload analysis showing the number of transports in draft, new, in process, and in execution.

## Prerequisites

Authorization is based on the standard Transportation Management authorization objects.

You’ll need either the Transp. Management Administrative Settings authorization object (T_ADMIN), or both the Transp.

Management Order Management & Planning (Purchase) authorization object (T_TOR_PUR) and the Transp. Management Order

Management & Planning (Execution) authorization object (T_TOR_EXE).

You’ll need the Business Partner: Purpose Completed authorization object (B_BUP_PCPT) for all business partners accessed in

this query.

In addition, you’ll need the Location: Access Based on Authorization Group authorization object (/SCMB/LOCB) for all locations

accessed in this query.

The following table lists the authorization objects with required fields and values:

This is custom documentation. For more information, please visit SAP Help Portal.

66


1/14/26, 2:47 PM

Authorization

Check Condition

Object

Field

Value

## T_ADMIN

Check if the user has either T_ADMIN or both T_TOR_PUR and

T_TOR_EXE authorization objects.

## T_TOR_PUR

Check if the user has either T_ADMIN or both T_TOR_PUR and

T_TOR_EXE authorization objects.

## ACTVT

H1 (Deactivate)

## ACTVT

03 (Display)

## TM_OC

TransportationOrderCategory

TO (Freight Order)

## TM_OT

TransportationOrderType

## TM_XPORG

PurchasingOrgExternalID

## TM_XPGRP

PurchasingGroupExternalID

## TM_RP

TranspOrdResponsiblePerson

## TM_MOT

TransportationMode

## ACTVT

03 (Display)

## TM_OC

TransportationOrderCategory

TO (Freight Order)

## TM_OT

TransportationOrderType

## T_TOR_EXE

Check if the user has either T_ADMIN or both T_TOR_PUR and

T_TOR_EXE authorization objects.

This is custom documentation. For more information, please visit SAP Help Portal.

67


Field

## Value

## TM_XEORG

PlngAndExecOrgExternalID

## TM_XEGRP

PlngAndExecGroupExternalID

## TM_RP

TranspOrdResponsiblePerson

## TM_MOT

TransportationMode

## ACTVT

03 (Display)

## ACTVT

03 (Display)

1/14/26, 2:47 PM

Authorization

Check Condition

## Object

B_BUP_PCPT Only when the business purpose of the carrier, shipper, or ship-to

party is set to Completed (value of view field

CarrierBusPurposeIsCompleted = X or

ShipperBusPurposeIsCompleted = X or

ConsigneeBusPurposeIsCompleted = X), check if
authorization object B_BUP_PCPT has set field ACTVT to 03.

The system uses B_BUP_PCPT in the data destruction process

for Information Lifecycle Management.

/SCMB/LOCB Only when the business purpose of the source location or

destination location is set to Completed
(_SourceLocation.IsBusinessPurposeCompleted = X

or

_DestinationLocation.IsBusinessPurposeCompleted

= X), check field BRGRU against the value of view field

_SourceLocation.AuthorizationGroup or

_DestinationLocation.AuthorizationGroup.

The system uses /SCMB/LOCB in the data destruction process
for Information Lifecycle Management

The field BRGRU enables display access to blocked locations

based on the settings you specify in the Define Authorization

Group Indicating Blocked Master Data Customizing activity.

## BRGRU

_SourceLocation.Authorizatio

and

_DestinationLocation.Authori

## ACTVT

03 (Display)

## Structure

## Business Objects

This view is built on the Transportation Order (TOR) business object with TransportationOrderCategory = TO.

## Main Input Parameters

This is custom documentation. For more information, please visit SAP Help Portal.

68


1/14/26, 2:47 PM

The main input parameters are as follows:

## P_Language

Specifies the display language of the texts. The system automatically uses the system language as the P_Language.

## P_TodayDate

Specifies the timeframe of the data that you want to display. The system automatically uses the system date as the

P_TodayDate. This date is usually your local date. The system retrieves information from the beginning of previous month

up to the system date.

## P_DisplayTimeUnit

Specifies the units of time, for example, Event Delay in hours or minutes.

## P_DisplayWeightUnit

Specifies the units of weight, for example, Gross Weight in kilograms.

## P_DisplayVolumeUnit

Specifies the units of volume, for example, Item Volume in meters cubed.

## P_DisplayQuantityUnit

Specifies the units of quantity, for example, Number of Containers in pieces.

## P_DisplayLengthUnit

Specifies the units of length, for example, Package Length in meters.

The unit parameters (time, weight, volume, quantity, and length) are mandatory.

## Measures and Attributes

The most important measures and attributes are listed below.

Keys and Identifiers

FreightOrder

TranspOrdExecution

TransportationOrderUUID

TransportationOrderEventUUID

Freight Order Attributes

TransportationOrderType

MeansOfTransport

TransportationMode

PlngAndExecOrganization

PurchasingOrganization

TranspOrdLifeCycleStatus

## TransportationOrderExecSts

This is custom documentation. For more information, please visit SAP Help Portal.

69


1/14/26, 2:47 PM

Carrier

Shipper

## Consignee

TranspOrdIsInTransit

TranspOrdIsDlydInTransit

TranspOrdPlanningBlock

TranspOrdPlanningBlockRsn

TranspOrdExecutionIsBlocked

TranspOrdExecBlockReason

InvoicingIsBlocked

SourceLocationName

SourceLocationType

SourceLocationCountry

DestinationLocationName

DestinationLocationType

DestinationLocationCountry

Freight Order Measures

NumberOfTransportationOrders

NumberOfTranspOrdsInTransit

NmbrOfDelayedTranspOrdsInTrnst

TranspOrdDelayInDspUnit

TranspOrdGrossWeightInDspUnit

TranspOrdGrossVolumeInDspUnit

TranspOrdQuantityInDisplayUnit

TranspOrdNumberOfCtnsInDspUnit

NumberOfPlngBlkdTranspOrds

NumberOfExecBlkdTranspOrds

## Units

DisplayLengthUnit

DisplayQuantityUnit

DisplayTimeUnit

DisplayWeightUnit

## DisplayVolumeUnit

This is custom documentation. For more information, please visit SAP Help Portal.

70


1/14/26, 2:47 PM

Constraints

None.

## Freight Order Quantity Analysis

As a transportation manager for a shipper, you work with carriers to transport your products to your customers. You can use the

Freight Order Quantity Analysis overview page to provide you with the key performance indicators (KPIs) that you need to

manage your execution business. At a glance, you can see all the vital data you need for your daily decision-making.

You can see KPIs for the current weight, volume, and numbers being transported on a weekly basis by each carrier, shipper, and

ship-to party, as well as by transportation mode, and source and destination country or region. You can also view each carrier’s

utilization performance.

The overview page provides you with KPIs for the current and previous month.

## Key Features

## Gross Weight Distribution

You can view a chart showing how gross weight distribution for completed freight orders (that is, with a freight order life

cycle status of Completed) has increased or decreased in each completion week (current and previous month). The total

gross weight distribution also appears at the top, for example, 5K.

## Gross Volume Distribution

You can view a chart showing how gross volume distribution for completed freight orders has increased or decreased in

each completion week (current and previous month). The total gross volume distribution also appears at the top, for

example, 194K.

## Quantity Distribution

You can view a chart showing how quantity distribution for completed freight orders has increased or decreased in each

completion week (current and previous month). The total gross quantity distribution also appears at the top, for example,

55K.

## Transportation Mode Category Analysis

You can see a chart with gross weight and gross volume as axes, plus the total number of freight orders, for each

transportation mode category for completed freight orders. This can help you identify the most effective method of

transportation.

## Logistic Network Analysis

You can review a table showing source and destination countries or regions, and total gross weight for completed freight

orders. This identifies where you have transported most goods in the current and previous months. The table is sorted in

descending order of gross weight.

## Carrier Quantity Analysis

You can view the total gross weight, gross volume, and container count per carrier for completed freight orders. This gives

you information on which carriers you are using the most. The highest weight appears at the top.

## Shipper Quantity Analysis

You can view the total gross weight, gross volume, and container count per shipper for completed freight orders. This gives

you information on which shippers you are using the most. The highest gross weight appears at the top.

This is custom documentation. For more information, please visit SAP Help Portal.

71


1/14/26, 2:47 PM

## Ship-To Party Quantity Analysis

You can view the total gross weight, gross volume, and container count per ship-to parties for completed freight orders. The

highest gross weight appears at the top

## Utilization Distribution

You can see the lowest average utilization per carrier (expressed as a percentage) for completed freight orders. The lowest

utilization percentage appears at the top. This helps you assess carriers’ performance and capacity.

## Quantity Analysis

You can view a table showing the gross volume and gross weight transported for each transportation mode category (for

example, road and air) for completed freight orders. You can use this information when deciding on the most efficient

method of transportation. The table is sorted in descending order of gross weight.

## Distance Analysis

You can see the total net duration and total distance for transported goods for each transportation mode category (for

example, sea and air) for completed freight orders. You can use this information when deciding on the most efficient

method of transportation. The greatest distance appears at the top.

## Detailed View

You can use visual features to analyze the KPI information at a more detailed level. Selecting a card header or information line

takes you to the detailed view, which presents summary information graphically and also in a table, from which you can navigate

directly to the freight order in the Transportation Management system and change it if necessary.

Supported Device Types

Desktop

## Tablet

Smartphone

Technical Basis

Fiori ID: F2676

This overview page uses the C_FrtOrdQuantityQuery CDS view.

You must activate the C_FRTORDQUANTITYQUERY_CDS OData service in the Gateway system.

More Information

## Subject

## More Information

Freight order management for a business person

## Freight Order Management

Freight order quantity analysis detailed view for a business person

Freight Order Quantity Detailed View

Underlying technical object for a technical person

C_FrtOrdQuantityQuery CDS view

## Freight Order Quantity Query

This is custom documentation. For more information, please visit SAP Help Portal.

72


1/14/26, 2:47 PM

## Freight Order Quantity Detailed View

You can get a detailed analysis of each key performance indicator (KPI). You can have instant and flexible access to the information

you need to analyse your freight order execution and change it if necessary by navigating directly to the relevant document in the

Transportation Management (TM) system.

The system displays the information on a two-month rolling basis (current and previous month).

Screen Areas

## Information filter

You can use the information filter on the top of the screen to select the information that the system displays in the chart

and table underneath. This enables you to view your filtered freight order data in different ways.

You can quickly see the total gross weight of goods transported per carrier in the current and previous month represented

visually by a line chart, and the total gross weight of freight orders per transportation mode category depicted by a bar

chart.

The following views are available:

## Graphics view

By default, the system displays the graphics filter. For example, you can select KPIs for gross weight per carrier in

the current and previous month and the number of freight orders per transportation mode category.

## Field view

You can change to a field filter (compact filter), where you can enter filter criteria such as the weight, volume, and

time units in which you want to see the information.

## Bar chart

The chart in the middle of the screen gives you a comparison view of your KPIs by by gross weight per transportation mode

category for completion weeks in the current and previous month. You can change the chart to a table or a combined table

and chart. Use the View By filter to view more specific information such as carrier, destination country or region, and life

cycle status. For example, you can quickly see the total gross weight of goods being transported by road in a specific

completion week.

## Table

The table at the bottom of the screen gives you more information on your KPIs, such as carrier, number of containers, and

source and destination countries or regions. You can add or remove columns in Settings to give you the information you

want to see, for example, completion date and whether dangerous goods are being transported.

Selecting a freight order in the table and pressing Change Freight Order takes you directly to the freight order in

Transportation Management. The document opens in edit mode.

## Example

You want to see which carriers transported goods by road to the USA in the previous month, and the total gross weight transported

by each. You see that you used three carriers, but one transported much more than the others. You navigate directly to the freight

order to find out more details.

You see that the carrier that transported the most is performing in line with expectations, but the other carriers are not. You can

now investigate the reasons why, and take action if necessary.

This is custom documentation. For more information, please visit SAP Help Portal.

73


1/14/26, 2:47 PM
## Technical Basis

Your system administrator or another technical user can use the following technical information to change the detailed view.

Fiori ID: F2752

This detailed view uses the C_FrtOrdQuantityQuery CDS view.

You must activate the C_FRTORDQUANTITYQUERY_CDS OData service in the Gateway system.

## More Information

Freight Order Quantity Analysis

Freight Order Quantity Query

Freight Order Quantity Query

Technical Name

## View Type

C_FRTORDQUANTITYQUERY Consumption view

## Purpose

This view contains key performance indicators (KPIs) to enable you to monitor your freight orders with carriers. It contains the

current weights, volumes, and numbers being transported on a weekly basis by each carrier, shipper, and ship-to party, as well as

by transportation mode, and source and destination country or region. The view also calculates each carrier’s utilization.

## Prerequisites

Authorization is based on the standard Transportation Management authorization objects.

You’ll need either the Transp. Management Administrative Settings authorization object (T_ADMIN), or both the Transp.

Management Order Management & Planning (Purchase) authorization object (T_TOR_PUR) and the Transp. Management Order

Management & Planning (Execution) authorization object (T_TOR_EXE).

You’ll need the Business Partner: Purpose Completed authorization object (B_BUP_PCPT) for all business partners accessed in

this query.

In addition, you’ll need the Location: Access Based on Authorization Group authorization object (/SCMB/LOCB) for all locations

accessed in this query.

The following table lists the authorization objects with required fields and values:

Authorization

Check Condition

Object

Field

Value

## T_ADMIN

Check if the user has either T_ADMIN or both T_TOR_PUR and

T_TOR_EXE authorization objects.

This is custom documentation. For more information, please visit SAP Help Portal.

74


1/14/26, 2:47 PM

Authorization

Check Condition

Object

Field

Value

## ACTVT

H1 (Deactivate)

## T_TOR_PUR

Check if the user has either T_ADMIN or both T_TOR_PUR and

T_TOR_EXE authorization objects.

## T_TOR_EXE

Check if the user has either T_ADMIN or both T_TOR_PUR and

T_TOR_EXE authorization objects.

## TM_OC

TransportationOrderCategory

TO (Freight Order)

## TM_OT

TransportationOrderType

## TM_XPORG

PurchasingOrgExternalID

## TM_XPGRP

PurchasingGroupExternalID

## TM_RP

TranspOrdResponsiblePerson

## TM_MOT

TransportationMode

## ACTVT

03 (Display)

## TM_OC

TransportationOrderCategory

TO (Freight Order)

## TM_OT

TransportationOrderType

## TM_XEORG

PlngAndExecOrgExternalID

## TM_XEGRP

PlngAndExecGroupExternalID

## TM_RP

## TranspOrdResponsiblePerson

This is custom documentation. For more information, please visit SAP Help Portal.

75


Field

Value

## TM_MOT

TransportationMode

## ACTVT

03 (Display)

## ACTVT

03 (Display)

1/14/26, 2:47 PM

Authorization

Check Condition

## Object

B_BUP_PCPT Only when the business purpose of the carrier, shipper, or ship-to

party is set to Completed (value of view field

CarrierBusPurposeIsCompleted = X or

ShipperBusPurposeIsCompleted = X or
ConsigneeBusPurposeIsCompleted = X), check if

authorization object B_BUP_PCPT has set field ACTVT to 03.

The system uses B_BUP_PCPT in the data destruction process

for Information Lifecycle Management.

/SCMB/LOCB Only when the business purpose of the source location or
destination location is set to Completed

(_SourceLocation.IsBusinessPurposeCompleted = X

or

_DestinationLocation.IsBusinessPurposeCompleted

= X), check field BRGRU against the value of view field

_SourceLocation.AuthorizationGroup or
_DestinationLocation.AuthorizationGroup.

The system uses /SCMB/LOCB in the data destruction process

for Information Lifecycle Management

The field BRGRU enables display access to blocked locations

based on the settings you specify in the Define Authorization

Group Indicating Blocked Master Data Customizing activity.

## BRGRU

_SourceLocation.Authorizatio

and

_DestinationLocation.Authori

## ACTVT

03 (Display)

## Structure

## Business Objects

This view is built on the Transportation Order (TOR) business object with TransportationOrderCategory = TO.

## Main Input Parameters

The main input parameters are as follows:

## P_Language

Specifies the display language of the texts. The system automatically uses the system language as the P_Language.

## P_TodayDate

This is custom documentation. For more information, please visit SAP Help Portal.

76


1/14/26, 2:47 PM

Specifies the timeframe of the data that you want to display. The system automatically uses the system date as the

P_TodayDate. This date is usually your local date. The system retrieves information from the beginning of previous month

up to the system date.

## P_DisplayTimeUnit

Specifies the units of time, for example, Event Delay in hours or minutes.

## P_DisplayWeightUnit

Specifies the units of weight, for example, Gross Weight in kilograms.

## P_DisplayVolumeUnit

Specifies the units of volume, for example, Item Volume in meters cubed.

## P_DisplayQuantityUnit

Specifies the units of quantity, for example, Number of Containers in pieces.

## P_DisplayLengthUnit

Specifies the units of length, for example, Package Length in meters.

The unit parameters (time, weight, volume, quantity, and length) are mandatory.

## Measures and Attributes

The most important measures and attributes are listed below.

Keys and Identifiers

TransportationOrder

TransportationOrderStage

TransportationOrderUUID

SourceLocationUUID

DestinationLocationUUID

Freight Order Attributes

TransportationOrderCategory

TransportationOrderType

DangerousGoodsAreContained

TranspOrdShippingType

TranspOrdTrafficDirection

MeansOfTransport

TransportationMode

TransportationModeCategory

TranspOrdLifeCycleStatus

## PlngAndExecOrganization

This is custom documentation. For more information, please visit SAP Help Portal.

77


1/14/26, 2:47 PM

PlngAndExecGroup

PurchasingOrganization

## PurchasingGroup

TranspOrdCompletionDateTime

TranspOrdCompletionDate

TranspOrdCompletionYearWeek

TranspOrdCompletionYearMonth

TranspOrdCompletionYearQuarter

TranspOrdCompletionYear

ChangedDateTime

## Carrier

CarrierOriginOfEntry

Shipper

## Consignee

SourceLocation

SourceLocationType

SourceLocationCountry

SourceLocationRegion

DestinationLocation

DestinationLocationType

DestinationLocationCountry

DestinationLocationRegion

Freight Order Stage Attributes

TranspOrdStageSrceLocation

TranspOrdStageSrceLocationType

TranspOrdStageSrceLocCntry

TranspOrdStageSrceLocRgn

TranspOrdStageDestLocation

TranspOrdStageDestLocationType

TranspOrdStageDestLocCntry

TranspOrdStageDestLocRgn

Freight Order Measures

## NumberOfTransportationOrders

This is custom documentation. For more information, please visit SAP Help Portal.

78


1/14/26, 2:47 PM

TranspOrdMaxUtilznRatio

TranspOrdMaxUtilznMassRatio

TranspOrdMaxUtilznVolumeRatio

TranspOrdNumberOfCtnsInDspUnit

TranspOrdGrossWeightInDspUnit

TranspOrdGrossVolumeInDspUnit

TranspOrdQuantityInDisplayUnit

Freight Order Stage Measures

NumberOfTranspOrdStages

TranspOrdStageMaxUtilznRatio

TranspOrdStageUtilznVolRatio

TranspOrdStageUtilznMassRatio

TranspOrdStageDstncInDspUnit

TranspOrdStageNetDurnInDspUnit

## Units

DisplayLengthUnit

DisplayQuantityUnit

DisplayTimeUnit

DisplayWeightUnit

DisplayVolumeUnit

Constraints

None.

## Tendering Analysis

As a tendering manager or transportation manager for a shipper, you work with carriers to transport your products to your

customers. You can use the Tendering Analysis overview page to provide you with the key performance indicators (KPIs) that you

need to manage your tendering business. At a glance, you can see all the vital data you need for your daily decision-making. The

overview page provides you with KPIs for the current and previous month.

You can identify and work with the carriers who perform the best. You can assess the performance of carriers with peer-to-peer

requests for quotation (freight RFQs). You can also assess the performance of carriers with all your tendering types.

You can investigate the best tendering type for an individual carrier. You can investigate why a carrier that the system proposed

was manually replaced with another carrier.

## Key Features

This is custom documentation. For more information, please visit SAP Help Portal.

79


1/14/26, 2:47 PM

## Open Requests

You have sent freight RFQs to your carriers. You want your carriers to give you freight quotations for providing you with

transportation services. This is essentially your current worklist, where you can review all the freight RFQs you have sent

out that are still open, and that haven’t yet reached their deadlines. You can drill down to see summaries of the open

requests and, from each summary, you can open the request in the Transportation Management system.

## Overdue Requests

You can review all the freight RFQs that you have sent out to your carriers that have exceeded their deadlines.

You can work with your critical requests where you may still have time to answer a request.

## Acceptance Analysis

You can review the proportion of freight RFQs to which an individual carrier has responded. This enables you to determine

which carriers perform well, and which will most likely support you with an urgent request. You can also see the number of

requests accepted out of total requests made, for example, two out of four requests accepted (2 / 4).

## Tendering Peer-to-Peer Cycle Analysis

You can review the proportion of peer-to-peer requests to which an individual carrier has responded with a quotation. This

enables you to determine which carriers perform well on your peer-to-peer freight RFQs, and which will most likely support

you with an urgent peer-to-peer freight RFQ.

You can also review the response times from your carriers. This enables you to see who responds to your freight RFQs

immediately, who delays a response, and also who delays a response and submits an increased amount in a quotation.

## Tendering Cycle Time Analysis

You use a combination of tendering types with your carriers, for example, peer-to-peer and broadcast tendering types. You

can review the average cycle time in hours and the number of cycles taken by a carrier to respond to freight RFQs. This

enables you to determine which carriers perform well on your overall tendering business, and which will most likely support

you with urgent requests.

## Tendering Ratio

You can review the most successful tendering type for individual carriers. For example, you want to see which broadcast

tendering type got the best response from a particular carrier. You can answer the questions: which tendering type gets the

most responses and which tendering type gets the quickest response?

## Original Carrier Changed

You can review the percentage and number of times the carrier that the system proposed was manually replaced with

another carrier who fulfilled the transportation service. You can review the reasons why a carrier was manually replaced.

You can use the information on this card to compare the business you actually awarded against the business the system

proposed.

## Detailed View

You can use visual features to analyze the KPI information at a more detailed level. Selecting a card header or information line

takes you to the detailed view, which presents summary information graphically and also in a table, from which you can navigate

directly to the freight order in the Transportation Management system and change the tendering if necessary.

Supported Device Types

Desktop

## Tablet

This is custom documentation. For more information, please visit SAP Help Portal.

80


1/14/26, 2:47 PM

Smartphone

Technical Basis

Fiori ID: F2679

This overview page uses the C_TenderingQuery CDS view.

You must activate the C_TENDERINGQUERY_CDS OData service in the Gateway system.

More Information

## Subject

## More Information

Freight tendering overview for a business person

## Freight Tendering

Tendering detailed view for a business person

## Tendering Detailed View

Underlying technical object for a technical person

C_TenderingQuery CDS view

## Tendering Query

## Tendering Detailed View

You can get a detailed analysis of each key performance indicator (KPI). You can have instant and flexible access to the information

you need to analyze and manage your tendering business and change it if necessary by navigating directly to the relevant

document in the Transportation Management (TM) system.

The system displays the information on a two-month rolling basis (current and previous month).

Screen Areas

## Information filter

You can use the information filter on the top of the screen to select the information that the system displays in the chart

and table underneath. This enables you to view your filtered tendering data in different ways.

You can quickly see the cycle time by requested carrier, represented visually by a bar chart.

The following views are available:

## Graphics view

By default, the system displays the graphics filter. For example, you can select KPIs for the cycle time in which an

individual carrier has responded to freight requests for quotation (RFQs).

## Field view

You can change to a field filter (compact filter), where you can enter filter criteria such as freight order tendering

completed, and the weight, volume, and time units in which you want to see the information.

## Bar chart

The chart in the middle of the screen gives you a comparison view of your KPIs for tendering time by requested carrier. You

can change the chart to a table or a combined table and chart. Use the View By filter to view more specific information such

This is custom documentation. For more information, please visit SAP Help Portal.

81


1/14/26, 2:47 PM

as freight RFQ status, life cycle status, and negative responses. For example, you can quickly see the number of negative

responses from the requested carrier.

## Table

The table at the bottom of the screen gives you more information on your KPIs, such as response submission date, number

of completed tendering cycles, and positive responses. You can add or remove columns in Settings to give you the

information you want to see, for example, request time left and number of successful tenderings.

Selecting a tendering in the table and pressing Change Tendering takes you directly to the freight order in Transportation

Management (it opens in edit mode), where you can change the tendering if necessary.

## Example

You want to identify and work with the carriers who perform the best. You look at the completed tendering cycles for each carrier,

their positive and negative responses to RFQs, and any rejection reasons.

You identify two carriers who have performed the best, so you investigate which carrier will most likely support you with an urgent

request. You then navigate directly to the freight order and look at the tendering to find out further details about the carriers. You

then have all the information you need to proceed.

## Technical Basis

Your system administrator or another technical user can use the following technical information to change the detailed view.

Fiori ID: F2753

This detailed view uses the C_TenderingQuery CDS view.

You must activate the C_TENDERINGQUERY_CDS OData service in the Gateway system.

More Information

Tendering Analysis

Tendering Query

Tendering Query

Technical Name

## View Type

C_ TENDERINGQUERY Consumption view

## Purpose

This view contains tendering key performance indicators (KPIs) such as open, overdue, and accepted tendering requests. It also

contains calculations for different cycle time definitions and carrier-based tendering ratios.

This information helps you identify which carriers perform the best by assessing their performance with peer-to-peer requests for

quotation (freight RFQs) and all the different tendering types.

This is custom documentation. For more information, please visit SAP Help Portal.

82


1/14/26, 2:47 PM
## Prerequisites

Authorization is based on the standard Transportation Management authorization objects.

You’ll need either the Transp. Management Administrative Settings authorization object (T_ADMIN), or both the Transp.

Management Order Management & Planning (Purchase) authorization object (T_TOR_PUR) and the Transp. Management Order

Management & Planning (Execution) authorization object (T_TOR_EXE).

You’ll need the Business Partner: Purpose Completed authorization object (B_BUP_PCPT) for all business partners accessed in

this query.

In addition, you’ll need the Location: Access Based on Authorization Group authorization object (/SCMB/LOCB) for all locations

accessed in this query.

The following table lists the authorization objects with required fields and values:

Authorization

Check Condition

Object

Field

Value

## T_ADMIN

Check if the user has either T_ADMIN or both T_TOR_PUR and

T_TOR_EXE authorization objects.

## T_TOR_PUR

Check if the user has either T_ADMIN or both T_TOR_PUR and

T_TOR_EXE authorization objects.

## ACTVT

H1 (Deactivate)

## TM_OC

TransportationOrderCategory

TO (Freight Order)

## TM_OT

TransportationOrderType

## TM_XPORG

PurchasingOrgExternalID

## TM_XPGRP

PurchasingGroupExternalID

## TM_RP

TranspOrdResponsiblePerson

## TM_MOT

TransportationMode

## ACTVT

03 (Display)

This is custom documentation. For more information, please visit SAP Help Portal.

83


1/14/26, 2:47 PM

Authorization

Check Condition

Object

Field

## Value

## T_TOR_EXE

Check if the user has either T_ADMIN or both T_TOR_PUR and

T_TOR_EXE authorization objects.

## TM_OC

TransportationOrderCategory

TO (Freight Order)

## TM_OT

TransportationOrderType

## TM_XEORG

PlngAndExecOrgExternalID

## TM_XEGRP

PlngAndExecGroupExternalID

## TM_RP

TranspOrdResponsiblePerson

## TM_MOT

TransportationMode

## ACTVT

03 (Display)

B_BUP_PCPT Only when the business purpose of the Carrier, Requested

Carrier, or Selected Carrier is set to Completed (value of view

field CarrierBusPurposeIsCompleted = X or

TndrgReqdCarrBusPrpsIsCmpltd = X or

TndrgSeldCarrBusPrpsIsCmpltd = X), check if

authorization object B_BUP_PCPT has set field ACTVT to 03.

The system uses B_BUP_PCPT in the data destruction process

for Information Lifecycle Management.

/SCMB/LOCB Only when the business purpose of the source location or

## ACTVT

03 (Display)

destination location is set to Completed

(_SourceLocation.IsBusinessPurposeCompleted = X

or
_DestinationLocation.IsBusinessPurposeCompleted

= X), check field BRGRU against the value of view field

_SourceLocation.AuthorizationGroup or

_DestinationLocation.AuthorizationGroup.

The system uses /SCMB/LOCB in the data destruction process

for Information Lifecycle Management

The field BRGRU enables display access to blocked locations

based on the settings you specify in the Define Authorization

Group Indicating Blocked Master Data Customizing activity.

This is custom documentation. For more information, please visit SAP Help Portal.

84


1/14/26, 2:47 PM

Authorization

Check Condition

Object

## Structure

Business Objects

Field

Value

## BRGRU

_SourceLocation.Authorizatio

and

_DestinationLocation.Authori

## ACTVT

03 (Display)

This view is built on the Transportation Order (TOR) business object with TransportationOrderCategory = TO.

## Main Input Parameters

The main input parameters are as follows:

## P_Language

Specifies the display language of the texts. The system automatically uses the system language as the P_Language.

## P_TodayDate

Specifies the timeframe of the data that you want to display. The system automatically uses the system date as the

P_TodayDate. This date is usually your local date. The system retrieves information from the beginning of previous month

up to the system date.

## P_DisplayTimeUnit

Specifies the units of time, for example, Event Delay in hours or minutes.

## P_DisplayWeightUnit

Specifies the units of weight, for example, Gross Weight in kilograms.

## P_DisplayVolumeUnit

Specifies the units of volume, for example, Item Volume in meters cubed.

## P_DisplayQuantityUnit

Specifies the units of quantity, for example, Number of Containers in pieces.

## P_DisplayCurrency

Specifies the currency, for example, Tendering Response Submitted Amount in euros.

The unit parameters (time, weight, volume, quantity, and currency) are mandatory.

## Measures and Attributes

The most important measures and attributes are listed below.

Keys and Identifiers

## TransportationOrder

This is custom documentation. For more information, please visit SAP Help Portal.

85


1/14/26, 2:47 PM

TenderingSequenceNumber

TenderingStepSequenceNumber

TenderingRequestSequenceNumber

TenderingResponseSqncNumber

TransportationOrderUUID

SourceLocationUUID

DestinationLocationUUID

TenderingUUID

TenderingStepUUID

TenderingRequestUUID

TenderingResponseUUID

Freight Order Attributes

TransportationOrderCategory

TransportationOrderType

TransportationMode

TransportationModeCategory

MeansOfTransport

## ChangedDateTime

TranspOrdLifeCycleStatus

TransportationOrderExecSts

PlngAndExecOrganization

PlngAndExecGroup

PurchasingOrganization

PurchasingGroup

## Carrier

CarrierOriginOfEntry

SourceLocation

DestinationLocation

Tendering Attributes

## TenderingType

TenderingProcessResult

TenderingIsSuccessful

## TenderingHasCompletedCycle

This is custom documentation. For more information, please visit SAP Help Portal.

86


1/14/26, 2:47 PM

PeerToPeerTndrgIsSuccssfl

CarrierIsFromTendering

FrtOrdHasCompletedTndrg

TenderingLifeCycleStatus

TenderingStartDateTime

TenderingStartDate

TenderingStartDateYear

TenderingStartDateYearWeek

TenderingStartDateYearMonth

TenderingStartDateYearQuarter

TenderingResponseDate

TenderingCreationUser

TenderingChangeUser

Tendering Step Attributes

TenderingProcessMode

CarrierAssignmentMethod

TrAlcAndBusShrIsUpdtdByRFQ

TndrgStepLifeCycleStatus

Tendering Request Attributes

TenderingRequestIsOpen

TenderingRequestIsOverdue

TenderingRequestIsCompleted

TndrgReqLifeCycleStatus

TenderingRequestedCarrier

FreightQuotationDueDateTime

Tendering Response Attributes

TenderingResponseCode

TndrgResponseIsPositive

TndrgResponseIsNegative

TenderingRejectionReason

TndrgQuotationEvalResult

## IsProposedFreightQuotation

This is custom documentation. For more information, please visit SAP Help Portal.

87


1/14/26, 2:47 PM

QuotationReviewIsRequired

TenderingAwardStatus

FreightQuotationStatus

TenderingSelectedCarrier

TndrgCarrierIsDiscrepant

Freight Order Measures

NumberOfTransportationOrders

TranspOrdGrossWeightInDspUnit

TranspOrdGrossVolumeInDspUnit

TranspOrdQuantityInDisplayUnit

TranspOrdNumberOfCtnsInDspUnit

Tendering Measures

## NumberOfTenderings

NumberOfSuccessfulTenderings

NumberOfCarriersFromTendering

NumberOfFrtOrdsWithCmpltdTndrg

NumberOfCmpltdTenderingCycles

NumberOfPeerToPeerTndrgCycles

NmbrOfSuccssflPeerToPeerTndrgs

AvgNumberOfPeerToPeerCycles

TenderingCycleTimeInDspUnit

TenderingAvgCycleTimeInDspUnit

TenderingSuccessRatio

FrtOrdsWithTenderingRatio

CarrierFromTenderingRatio

Tendering Step Measures

NumberOfTenderingSteps

TndrgStepAbsltPrcLmtInDspCrcy

AvgRelativePriceLimitInPercent

MaxResponseDurationInDspUnit

Tendering Request Measures

## NumberOfTenderingRequests

This is custom documentation. For more information, please visit SAP Help Portal.

88


1/14/26, 2:47 PM

NumberOfOpenTndrgRequests

NumberOfOverdueTndrgRequests

NumberOfCompletedTndrgRequests

RmngOpenTndrgReqTimeInDspUnit

TndrgRspSubmdAmtInDspCrcy

Tendering Response Measures

NumberOfTenderingResponses

NumberOfPositiveTndrgResponses

NumberOfNegativeTndrgResponses

NumberOfDiscrepantCarrierSel

PositiveTenderingResponseRatio

NegativeTenderingResponseRatio

TndrgReqAbsltPrcLmtInDspCrcy

## Units

DisplayQuantityUnit

DisplayTimeUnit

DisplayWeightUnit

DisplayVolumeUnit

DisplayCurrency

Constraints

None.

This is custom documentation. For more information, please visit SAP Help Portal.

89
