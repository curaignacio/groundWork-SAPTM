1/14/26, 2:41 PM

Transportation Management (TM)

Generated on: 2026-01-14 14:41:08 GMT+0000

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


1/14/26, 2:41 PM

Agreement Management

## Use

As a shipper or logistics service provider (LSP), you use Agreement Management to do the following:

Forecast and assess your transportation requirements.

Request bids from carriers for your transportation requirements.

Negotiate contracts (agreements) with carriers.

These features help keep your transportation costs down and efficiently manage contracts with carriers.

As a carrier, you use Agreement Management to respond to shippers or LSPs with your rates for transportation services.

Carriers, shippers, and LSPs can also use Agreement Management to set up and maintain agreements, the basis for calculating

transportation charges.

## Integration

Agreement Management is a component of Transportation Management (TM). Agreement Management is integrated with the

Charge Management and Service Product Catalogs component because TM calculates transportation charges based on the

master data stored in calculation sheets, rate tables, and scales that are created locally or that are created independently of the

agreement. For more information, see Charge Management and Service Product Catalogs.

## Features

## Strategic freight procurement

As a shipper or LSP, you can detail your transportation requirements, request bids from carriers, and compare the bids you

receive. You can then negotiate and award the transportation business to carriers and negotiate contracts with carriers (see

Strategic Freight Procurement). You can also collaborate with carriers even if the carrier doesn't use TM (see Carrier

Collaboration).

## Rate quotation

As a carrier, you can respond to shippers or LSPs with your rates for transportation services (see Forwarding Agreement

Quotation).

## Agreements

As a shipper, LSP, or carrier, you can create long-term contracts with your business partners as a starting point for enabling

charge calculation (see Agreement Maintenance).

Strategic Freight Procurement

## Use

As a shipper or logistics service provider (LSP), you need to keep your transportation costs low while still ensuring reliable

transportation services from carriers. Strategic freight procurement helps you to investigate the best rates from carriers to

This is custom documentation. For more information, please visit SAP Help Portal.

2


1/14/26, 2:41 PM

transport items between specific locations (trade lanes) and then to agree a contract (agreement) with the carriers.

Transportation Management (TM) supplies the tools you need to request rate quotations, evaluate responses, and award the

transportation business to carriers.

## Prerequisites

You have defined number ranges in Customizing for Transportation Management under  Master Data

 Agreement RFQs

and Quotations

 Define Number Range Intervals .

You have defined freight agreement RFQ types in Customizing for Transportation Management under  Master Data

 Agreement RFQs and Quotations

 Define Freight Agreement RFQ Types .

You have defined target share strategies and strategy conditions in Customizing for Transportation Management under

## Master Data

 Agreement RFQs and Quotations

 Define Target Share Strategies .

If you are a carrier responding to RFQs, you must define forwarding agreement quotation types in Customizing for

Transportation Management under  Master Data

 Agreement RFQs and Quotations

 Define Forwarding Agreement

Quotation Types .

You have configured the prerequisites for agreements (see Agreement Maintenance).

You have configured the prerequisites for output management and business-to-business communication (see Output

Management).

## Process

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

1. You create a freight agreement RFQ master to detail your transportation requirements.

In the freight agreement RFQ master, you specify the trade lanes, carriers, RFQ items, and logistical parameters, for

example:

Requested capacities

Commodity codes

Service levels

Movement types

Periodicities

## Rating structure

The rating structure of each RFQ item can consist of calculation sheets and rate tables. The system uses calculation sheets

to specify which transportation charges to calculate and how to calculate them, and uses rate tables to define and maintain

rates directly in TM. For more information, see Calculation Sheet and Rate Table.

  Note

In the rate table of the calculation sheet, you can select the Request Rate checkbox for rate records. This

indicates the rate records that the system downloads when you download an individual freight agreement RFQ

as a spreadsheet file. When you send this file to a carrier, the carrier responds with rates only for these rate

records.

In the calculation sheet or the rate table of a calculation sheet, you can define a target rate or target amount.

This specifies the maximum price you are willing to pay for a carrier’s service. You also specify a tolerance as a

This is custom documentation. For more information, please visit SAP Help Portal.

3


1/14/26, 2:41 PM

percentage. You can take informed decisions about the carrier if the rate is beyond the target amount or target

rate after applying the tolerance percentage. For example, you specify a target amount or target rate of 1000

USD. You also specify a tolerance of 10%. If the rate the carrier has proposed is higher than 1100 USD, you do not

have to take the carrier into consideration while awarding the transportation service.

You can choose to display the target rate to your carriers. To enable this feature, select the Publish Target Rate

checkbox in Customizing for Transportation Management under  Master Data

 Agreement RFQs and

## Quotations

 Define Freight Agreement RFQ Types .

2. You publish the freight agreement RFQ master.

As part of the publication process, the system automatically creates and sends individual freight agreement RFQs to the

carriers based on your output management settings and using business-to-business communication. For more

information, see Freight Agreement Quotation Processing. Note that you can create individual freight agreement RFQs for

multiple freight agreement RFQ masters and publish the freight agreement RFQ masters using the program Mass

Publication of Freight Agreement RFQ Masters (/SCMTMS/RFQ_PUBLISH) in transaction SE38.

You can separate the creation of the individual freight agreement RFQs and the publication of the freight agreement RFQ

master into 2 steps. This separation allows you to edit individual freight agreement RFQs before sending them to carriers.

You separate the creation and publication in the Customizing activity Define Freight Agreement RFQ Types. Note that you

cannot selectively send individual freight agreement RFQs to carriers – the system sends all the individual freight

agreement RFQs to the carriers when you publish the freight agreement RFQ master.

You can enable an approval workflow so you have to get approval from an approver before publishing the freight agreement

RFQ master. When an approver approves the publication of the freight agreement RFQ master, the system automatically

publishes the freight agreement RFQ master and creates and sends the individual freight agreement RFQs to the carriers. If

you separated the creation and the publication into 2 steps, and an approver approves the publication, you can then

separately trigger the creation of the individual freight agreement RFQs and the publication of the freight agreement RFQ

master.

  Note

If the system cannot publish the freight agreement RFQ master, the status of the freight agreement RFQ master

changes to Publication in Process and does not change to Published. You can check the freight agreement RFQ

masters that are not published in transaction SLG1. You can subsequently correct the errors in the unpublished freight

agreement RFQ masters and publish the freight agreement RFQ masters again using the report Publish Freight

Agreement RFQ Master (/SCMTMS/RFQ_RE_PUBLISH) in transaction SE38.

3. The system notifies each carrier about the individual RFQ.

The system also reminds each carrier if they have not responded and the response deadline is approaching. For more

information about system notifications, see Requesting of Quotations for Transportation Services.

4. The carriers respond to the individual RFQs.

The carriers evaluate and respond to their individual RFQ with their rates for the transportation services. Carriers submit

their rates and promised capacity for each charge type listed in the calculation sheet of each RFQ item. If a charge type has

a rate table associated with it, carriers are expected to provide rate values for each of the combinations listed in the rate

table. Carriers cannot change the structure of the calculation sheets or rate tables (see Calculation Sheet Maintenance and

Rate Definition and Maintenance).

For more information about responding to freight agreement RFQ masters, see Forwarding Agreement Quotation and

Forwarding Agreement Quotation Processing. Carriers can also respond to individual RFQs even if they don't use TM. For

more information, see Carrier Collaboration.

5. You evaluate the responses.

  Recommendation

This is custom documentation. For more information, please visit SAP Help Portal.

4


1/14/26, 2:41 PM

If you already know which carriers you want to award the transportation business to, skip the following 3 steps in the

process. Instead, directly create or update freight agreements for the carriers you are awarding the business to.

Therefore you do not need to do the following:

a. Evaluate the responses.

b. Review the results of the response comparison and strategy spend estimation.

c. Accept your preferred target share strategy.

After you receive the responses from carriers, you evaluate which carrier quoted the best rate by comparing the responses

by RFQ item in the comparison cockpit. You compare the responses by using the optimizer for carrier selection. The

optimizer is especially useful when the comparison is complex and multiple constraints must be taken into account. You

compare the responses in the following way:

a. You insert the target share strategy and the strategy conditions that you want the system to apply when proposing

target shares for carriers.

You define target share strategies and strategy conditions in the Customizing activity Define Target Share

Strategies.

b. You run the optimizer to propose target shares based on the target share strategy.

The optimizer proposes the most ideal target share distribution to produce the most cost effective solution. You can

run the optimizer repeatedly with different target share strategies and strategy versions.

  Note

You can run the optimizer for specific target share strategies or for all target share strategies in the freight

agreement RFQ master in the back end using program Mass Optimizer Run and Strategy Spend Estimation

(/SCMTMS/OPTIMIZER_RUN) in transaction SE38. If you do specify the target share strategies, the system

runs the optimizer for all the target share strategies in the freight agreement RFQ master. The system can also

estimate the strategy spend at the same time.

In the freight agreement RFQ master, when you enter a company or a corporate as an organizational unit, the

system sorts all the purchasing organizations under the company or corporate and picks up the first purchasing

organization for strategy spend calculation.

c. The system simulates the estimated strategy spend based on the responses you received from the carriers and the

target share strategies.

d. You select your preferred target share strategy.

When you select your preferred target share strategy, the system automatically calculates the confirmed capacity in

the freight agreement RFQ master.

  Note

If the comparison is fairly simple and the rates are the only constraints that must be taken into account, you can first

compare the responses manually, as follows:

a. You compare the responses by carrier and charge type.

You can compare the responses directly in TM. Alternatively, if the charge type has a rate table, you can compare

the rate tables in a spreadsheet application.

b. You choose whether you want to enable the confirmation of awarded capacities.

You can decide whether you want the carrier to send a response for the allocated confirmed capacities in order

to execute a transportation request. You can consolidate the responses from different carriers. You can analyze

This is custom documentation. For more information, please visit SAP Help Portal.

5


1/14/26, 2:41 PM

and assign transportation requests to different carriers. For more information, see Award Confirmation.

c. The system ranks the carriers based on the rates the carrier quoted per charge type.

d. The system displays the results in a response comparison graph.

If you compare the rate tables in a spreadsheet application only, the system does not display the results in a

graph.

For more information, see Post-Bid Analysis.

  Note

If you are not satisfied with the responses from the carriers, you can create a new negotiation round. You can then

change the details of the freight agreement RFQ master and publish it again. The carriers can then resubmit their rates.

  Note

You can create a freight agreement RFQ master assignment to delegate evaluation of responses to analysts. The

analysts have expertise in analyzing bids for a trade lane. The analysts determine the best bids from the carrier bids for

transportation services for a particular trade lane and merge the results back to the freight agreement RFQ master. For

more information, see Freight Agreement RFQ Master Assignment.

6. You review the results of the response comparison and strategy spend estimation.

You can use the Award Summary tab page to get an overview of the business you plan to award to the carriers.

7. You accept your preferred target share strategy.

8. You create or update freight agreements for the carriers you are awarding the business to.

The system notifies the carriers about the creation or update of the freight agreements. The notification includes a copy of

the freight agreement and the rate tables, if any. For more information about system notifications, see Requesting of

Quotations for Transportation Services.

You can enable an approval workflow so that you have to request approval to create the freight agreements. You enable this

workflow in the Customizing activity Define Freight Agreement RFQ Types.

  Note

If you update the status of the freight agreement RFQ master to completed, the system automatically sets the status of

the individual freight agreement RFQs to completed.

## More Information

Freight Agreement RFQ Master

## Agreement

Agreement Management

Analytics

## Advanced RFQs

## Freight Agreement RFQ Master

This is custom documentation. For more information, please visit SAP Help Portal.

6


1/14/26, 2:41 PM
## Definition

A freight agreement request for quotation (RFQ) master is a business document containing the transportation requirements of a

shipper or logistics service provider (LSP) for a specific future period. A shipper or LSP uses a freight agreement RFQ master to

select a set of carriers to fulfill the transportation requirements.

## Use

Strategic freight procurement helps you to investigate the best rates from carriers to transport items between specific locations

(trade lanes) and for a specific set of logistical parameters, such as shipping type, transportation mode, and movement type. You

then agree a contract (agreement) with the carriers. Freight agreement RFQ masters are a key element in strategic freight

procurement, as you use them to do the following:

1. Detail your transportation requirements.

2. Request capacity and rate quotations from carriers.

3. Evaluate and compare the bids you receive from carriers.

4. Distribute target share according to the carriers’ bids.

5. Simulate the estimated costs based on the carriers’ rates.

6. Negotiate and award the transportation business to carriers.

7. Agree the contracts with carriers.

In essence, you use freight agreement RFQ masters to request bids from carriers for transportation services and, based on those

bids, select carriers to fulfill your transportation requirements.

  Note

A carrier receives an individual freight agreement RFQ in the form of a forwarding agreement quotation. Forwarding agreement

quotations allow carriers to respond with their transportation rates. For more information, see Forwarding Agreement

Quotation. Carriers can also respond to individual RFQs even if they don't use Transportation Management (TM). For more

information, see Carrier Collaboration.

You can create a freight agreement RFQ master in the following ways:

Using the Manage Freight Agreement RFQ Masters app

  Note

This app displays all existing freight agreement RFQ masters regardless of their status in the strategic freight

procurement process. You can create, edit, and display freight agreement RFQ masters using this app.

Using a freight agreement RFQ master template

  Note

You can create, edit, or display freight agreement RFQ master templates using the freight agreement RFQ master

template apps.

You can define Customizing templates based on industry standards for freight agreement RFQ masters in

Customizing for Transportation Management under  Master Data

 Agreement RFQs and Quotations

## Define

Freight Agreement RFQ Master Templates . With the freight agreement RFQ master template apps on the

launchpad, you can use these Customizing templates to create master data templates for freight agreement

This is custom documentation. For more information, please visit SAP Help Portal.

7


RFQ masters. The freight agreement RFQ master templates that you create from the Customizing templates

enable you to make simple changes before creating a freight agreement RFQ master.

1/14/26, 2:41 PM

## Structure

A freight agreement RFQ master can contain the following main tabs and screen areas:

## General Data

The General Data tab page contains high-level information about the freight agreement RFQ master, for example:

## Organizational unit responsible

Note that you can only assign a purchasing organization, company, or corporate to an organizational unit. You can’t

assign purchasing group or a purchasing office to an organizational unit.

Validity period

Carrier details

  Note

You can specify multiple carriers in the carrier table. Carrier table contains details about the status of the

individual RFQs, if available.

## RFQ type

## RFQ negotiation round number

## Deadline for responding to the freight agreement RFQ

Calculation sheet template the system uses to create a calculation sheet or local calculation sheet in the freight

agreement RFQ master

## Items

The Items screen area contains information about the RFQ items. On this tab page, you can access the comparison cockpit

to compare the responses you receive from carriers (see Post-Bid Analysis). You can also accept your preferred strategy

before awarding the transportation business to carriers.

Note that you can specify a freight agreement type in a freight agreement RFQ type in Customizing for Transportation

Management under  Master Data

 Agreement RFQs and Quotations

 Define Freight Agreement RFQ Types . When

you create a freight agreement RFQ master with a freight agreement RFQ type, the item types assigned to the associated

freight agreement type are automatically available in the input help of the item type field in the freight agreement RFQ

master.

This screen area can contain the following tab pages, when relevant:

## Calculation Sheet Overview

This tab page displays the calculation sheet(both kinds, including local) details for each RFQ item.

## Carriers

This tab page displays the details of the carriers that responded to the RFQ item.

## Trade Lanes

On this tab page, you enter the details about the trade lanes for each RFQ item.

This is custom documentation. For more information, please visit SAP Help Portal.

8


1/14/26, 2:41 PM

## Capacities

This tab page contains the capacity required from carriers, the capacity carriers can commit to, and the capacity

awarded to carriers. For more information, see Capacities in Rate Tables for Freight Agreement RFQ Masters.

## Commodity Codes

On this tab page, you specify the commodity codes for each RFQ item.

## Default Route

On this tab page, you specify the route between a location pair for delivering the RFQ item.

## Notes

On this tab page, you can add any notes relevant to the RFQ item.

## Attachments

On this tab page, you can upload files relevant to the RFQ item.

## Document Flow

The Document Flow tab page displays the business documents that were created based on the freight agreement RFQ

master, with status information. For example, the individual freight agreement RFQs and the responses received from

carriers.

## Output Management

On the Output Management tab page, you can print RFQ details and generate emails and faxes and send them directly to

the intended recipient. You can also see a record of the documents that were already printed or sent (by e-mail or fax, for

example). For more information, see Output Management.

## Excel Integration

You can download the details of a freight agreement RFQ master. This helps you to review the details in the form of a

spreadsheet.

## Versions

The Versions tab page contains a list of the RFQ versions and negotiation rounds, including the status of each version.

## Award Summary

The Award Summary tab page displays graphs summarizing all the logistical information. This summary helps you to judge

how the negotiation process is going and make key decisions, such as whether to initiate a new negotiation round. You can

view the award summary by trade lane, carrier, or RFQ item.

You can also check what you spent last year for transportation services with the same logistical information, that is:

Trade lane

Shipping type

## Transportation mode

For more information, see Award Summary.

## Notes

On this tab page, you can add any notes relevant to the freight agreement RFQ master.

## Attachments

On this tab page, you can upload files relevant to the freight agreement RFQ master.

This is custom documentation. For more information, please visit SAP Help Portal.

9


1/14/26, 2:41 PM

## Capacities

This tab page contains the total capacity required from carriers, the total capacity carriers can commit to, and the total

capacity awarded to carriers.

  Note

You can activate the Capacities tab page or screen area in Customizing for Transportation Management under

## Master Data

 Agreement RFQs and Quotations

 Define Freight Agreement RFQ Types .

## Integration

Freight agreement RFQ masters are integrated with forwarding agreement quotations, as carriers use forwarding agreement

quotations to respond to individual freight agreement RFQs.

During strategic freight procurement, the system estimates the cost of using a carrier to provide transportation services in a trade

lane. To perform this estimation, freight agreement RFQ masters are integrated with calculation sheets, local calculation sheets,

rate tables, local rate tables, and ultimately charge calculation.

The system creates or updates freight agreements as part of the strategic freight procurement process.

## More Information

## Strategic Freight Procurement

Requesting of Quotations for Transportation Services

Forwarding Agreement Quotation

## Agreement

Calculation Sheet

## Rate Table

Optimization as Part of Carrier Selection

## Advanced RFQs

Freight Agreement RFQ Master Assignment

## Definition

A freight agreement RFQ master assignment is a business document that you as an analyst of a shipper or logistics service

provider (LSP) use to evaluate rates from carriers for transportation services.

A purchasing manager can create a freight agreement RFQ master assignment from a freight agreement RFQ master item. The

manager creates the freight agreement RFQ master assignment to delegate the task of bid analysis to analysts. The analysts have

expertise in analyzing bids for a trade lane. The analysts determine the best bids from the carrier bids for transportation services

for a particular trade lane and merge the results back to the freight agreement RFQ master item.

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

10


1/14/26, 2:41 PM

Strategic freight procurement helps you to investigate the best rates from carriers to transport items between specific locations

(trade lanes) and for a specific set of logistical parameters, such as shipping type, transportation mode, and movement type. You

then agree a contract (agreement) with the carriers. Freight agreement RFQ master assignments are a key element in strategic

freight procurement, as you use them to do the following:

1. Use the items that have received bids from carriers in the freight agreement RFQ assignment.

2. Evaluate and compare the bids you receive from carriers.

3. Distribute target share according to the carriers’ bids.

4. Simulate the estimated costs based on the carriers’ rates.

5. Determine the carries from which you want to purchase the transportation services.

6. Merge the items back to the freight agreement RFQ master.

## Structure

A freight agreement RFQ master assignment can contain the following main tab pages and screen areas:

## General Data

The General Data tab page contains high-level information about the freight agreement RFQ master assignment, for

example:

Organizational unit responsible

## Validity period

Carrier details, including whether you already have an agreement in place with the carrier in the trade lane

## RFQ type

## RFQ negotiation round number

## Deadline for responding to the freight agreement RFQ

Calculation sheet template the system uses to create a calculation sheet or a local calculation sheet in the freight

agreement RFQ master assignment

## Items

The Items screen area contains information about the RFQ assignment items. On this tab page, you can access the

comparison cockpit to compare the responses you receive from carriers (see Post-Bid Analysis). You can also accept your

preferred strategy before awarding the transportation business to carriers.

This screen area can contain the following tab pages, when relevant:

## Calculation Sheet Overview

This tab page displays the calculation sheet (both kinds, including local) details for each RFQ assignment item.

## Carriers

This tab page displays the details of the carriers that responded to the RFQ assignment item.

## Trade Lanes

On this tab page, you display the details about the trade lanes for each RFQ assignment item.

## Capacities

This is custom documentation. For more information, please visit SAP Help Portal.

11


1/14/26, 2:41 PM

This tab page contains the capacity required from carriers, the capacity carriers can commit to, and the capacity

awarded to carriers. For more information, see Capacities in Rate Tables for Freight Agreement RFQ Masters.

## Commodity Codes

On this tab page, you display the commodity codes for each RFQ assignment item.

## Default Route

On this tab page, you display the route between a location pair for delivering the RFQ assignment item.

## Notes

On this tab page, you can display any notes relevant to the RFQ assignment item.

## Attachments

On this tab page, you can display files relevant to the RFQ assignment item.

## Business Partner

The Business Partner tab page displays the business partners associated with the business document. For example, an

invoicing party and carrier.

  Note

You can display the business partner hierarchy in the business partner tab page.

In a freight agreement RFQ master assignment, it displays all the business partners associated with the carrier.

You can restrict the party roles available in the business partner tab page. For more information, see Business

Partner Determination.

You can display additional party roles, such as notify party and communication party, for information purposes in

addition to primary party roles, such as carrier.

## Document Flow

The Document Flow tab page displays the business documents that exist based on the freight agreement RFQ master

assignment, with status information. For example, the freight agreement master RFQ.

## Output Management

On the Output Management tab page, you can print RFQ assignment details and generate e-mails and faxes and send

them directly to the intended recipient. You can also see a record of the documents that were already printed or sent (by e-

mail or fax, for example). For more information, see Output Management.

## Excel Integration

You can download the details of a freight agreement RFQ master. This helps you to review the details in the form of a

spreadsheet.

## Versions

The Versions tab page contains a list of the RFQ assignment versions and negotiation rounds, including the status of each

version.

## Award Summary

The Award Summary tab page displays graphs summarizing all the logistical information. This summary helps you to judge

how the negotiation process is going and make key decisions, such as whether to initiate a new negotiation round. You can

view the award summary by trade lane, carrier, or RFQ assignment item.

This is custom documentation. For more information, please visit SAP Help Portal.

12


1/14/26, 2:41 PM

You can also check what you spent last year for transportation services with the same logistical information, that is:

Trade lane

Shipping type

## Transportation mode

For more information, see Award Summary.

## Notes

On this tab page, you can display any notes relevant to the freight agreement RFQ master assignment.

## Attachments

On this tab page, you can display files relevant to the freight agreement RFQ master assignment.

## Capacities

This tab page contains the total capacity required from carriers, the total capacity carriers can commit to, and the total

capacity awarded to carriers.

  Note
You can activate the Capacities tab page or screen area in Customizing for Transportation Management under

## Master Data

 Agreement RFQs and Quotations

 Define Freight Agreement RFQ Types .

## More Information

Freight Agreement RFQ Master

## Strategic Freight Procurement

Requesting of Quotations for Transportation Services

Forwarding Agreement Quotation

## Agreement

Calculation Sheet

## Rate Table

Optimization as Part of Carrier Selection

Award Confirmation

## Use

Strategic freight procurement helps you to investigate and negotiate the best rates and optimal capacities with carriers to

transport items between specific locations (trade lanes) and for specific logistical parameters, and then to create a contract

(agreement) with the selected carriers.

As a shipper or a logistics service provider, Transportation Management (TM) enables you to choose whether you want the carrier

to send a soft confirmation to the allocated confirmed capacities before awarding the capacities or business share through a

This is custom documentation. For more information, please visit SAP Help Portal.

13


1/14/26, 2:41 PM

freight agreement. You can consolidate the responses from different carriers. When you choose to enable confirmation of awarded

capacities, you can perform the following tasks:

Define an award confirmation deadline

## Notify the carrier of award confirmation

View the confirmation reason from each carrier for each response item in the freight agreement RFQ master

## Consolidate the confirmations from the carriers

Upload the confirmations from carriers into the respective individual freight agreement RFQs

View the statuses of award confirmations

## Prerequisites

You've enabled award confirmation in Customizing for Transportation Management under  Master Data

 Agreement RFQs and

## Quotations

 Define Freight Agreement RFQ Types .

You've configured the prerequisites for strategic freight procurement (see Strategic Freight Procurement).

## Features

## Award Confirmation Deadline

In a freight agreement RFQ master, you can define a confirmation deadline before to sending notification to carriers for award

confirmation. The carriers confirm the allocation of awarded capacities and forward the responses to the freight agreement RFQ

master within this deadline.

Note that this confirmation is only a soft confirmation. The system doesn't reject the carriers if they don't respond within the

deadline. The shipper can still communicate with the carriers offline in order to confirm the allocated capacities.

## Carrier Notification

When you choose the Notify the Carrier for Award Confirmation button in a freight agreement RFQ master, the system notifies

the carriers of the allotted confirmed capacities and the award confirmation deadline.

## Consolidation of Confirmations

A carrier can send a response for award confirmation to the shipper through an email. You can send a spreadsheet that contains all

the information, for example, items, rate tables, local rate tables, calculation sheets, local calculation sheets, transportation

modes, and service levels. The carrier enters a response and a confirmation reason in the spreadsheet and sends the file back to

you in an email attachment. If the carrier doesn't use TM, the carrier can also use the Manage Freight Agreement RFQs app to

send you a response for award confirmation. For more information, see Carrier Collaboration.

  Note
The system automatically updates the award confirmation status for master RFQ once the confirmation for an individual RFQ is

available.

Optionally, you can also run the report /SCMTMS/RESPONSE_AWARD_CONFIRM manually after the award confirmation

deadline. The system retrieves all the freight agreement RFQ masters with the status Pending Confirmation from Carrier.

Alternatively, you can also retrieve a specific freight agreement RFQ master by entering the RFQ ID.

## Display of Award Confirmation Statuses

This is custom documentation. For more information, please visit SAP Help Portal.

14


1/14/26, 2:41 PM

The system displays the status of award confirmation from the carrier in the following areas:

Freight agreement RFQ master

Freight agreement RFQ item

## Response

## Optimizer strategy

For more information on award confirmation statuses, see Statuses in Award Confirmation.

## Activities

To create or update freight agreement RFQ masters, in the Create Freight Agreement RFQ Master app on the fiori launchpad.

## More Information

Strategic Freight Procurement

Statuses in Award Confirmation

Optimizer Strategy Statuses

## Status

Appears When

Award Confirmation - Pending from One or More Carriers

Before the award confirmation deadline when one or more carriers

do not send any response to the shipper or logistics service

provider (LSP) for the allotted confirmed capacities for one or more

RFQ items.

## Rejected by One or More Carriers

One or more carriers reject the confirmed capacities allotted by the

shipper for a transportation requirement (RFQ item).

## No Response from One or More Carriers

After the award confirmation deadline when one or more carriers

do not send any response to the shipper or LSP for the allotted

confirmed capacities for one or more RFQ items.

## Awarded by Shipper

The shipper or the LSP awards one or more RFQ items to one or

more carriers.

## Rejected by All Carriers

All carriers reject the confirmed capacities allotted by the shipper

for a transportation requirement.

Freight Agreement RFQ Master Statuses or RFQ/Quotation Statuses

## Status

Appears When

## No Response from one or More Carriers

One or more carriers do not send a confirmation to the shipper or

LSP for the allotted confirmed capacities for one or more RFQ

items.

## Rejected by Carriers

All carriers reject all the confirmed capacities allotted by the

shipper or LSP for all RFQ items.

This is custom documentation. For more information, please visit SAP Help Portal.

15


1/14/26, 2:41 PM

## Status

Appears When

## One or More Items Rejected by Carriers

One or more carriers reject the confirmed capacities allotted by the

shipper or LSP for one or more RFQ items.

## Awarded by Shipper

The shipper or LSP awards all the transportation requirements to

one or more carriers.

Individual Freight Agreement RFQ Root Statuses

## Status

Appears When

## Award Confirmation - Pending from Carrier

The carrier does not send a confirmation to the shipper or LSP for

the allotted confirmed capacities for one or more RFQ items.

## Award Confirmation - Received by Shipper

The carrier sends a response to the shipper or LSP for the allotted

confirmed capacities for one or more RFQ items.

Award Confirmation - Uploaded by Carrier

The carrier has sent the spreadsheet file that contains the

response for award confirmation.

Award Confirmation - Submitted with Errors by Carrier

## The background processing function

/SCMTMS/RESPONSE_AWARD_CONFIRM chooses a file containing

errors.

After the award confirmation deadline, you run a recurring

background processing function
/SCMTMS/RESPONSE_AWARD_CONFIRM, to consolidate the

responses in spreadsheet files submitted by carriers.

For example, this status appears if the system chooses a file

without any responses for all the RFQ items.

## No Response from One or More Carriers

Before the award confirmation deadline when the carrier does not

send a response to the shipper or LSP for the allotted confirmed

capacities for one or more RFQ items.

## Rejected by Carriers

The carrier rejects the confirmed capacities allotted by the shipper

for all RFQ items.

## One or More Items Rejected by Carriers

The carrier rejects the confirmed capacities allotted by the shipper

for one or more RFQ items.

## Accepted by Carrier

The carrier accepts the confirmed capacities allotted by the

shipper for all RFQ items.

Freight Agreement RFQ Item Statuses

## Status

Appears When

Preferred Strategy – Accepted by Shipper

The shipper accepts the preferred strategy for a specific

transportation requirement by choosing the Accept Preferred

Strategy button in the award confirmation process.

## Award Confirmation – Pending from Carrier

After the shipper requests a confirmation from the carriers for a

specific RFQ item, the system sets this status before the award

confirmation deadline.

This is custom documentation. For more information, please visit SAP Help Portal.

16


1/14/26, 2:41 PM

## Status

Appears When

## Rejected by One or More Carriers

One or more carriers reject the confirmed capacities allotted by the

shipper or LSP.

## No Response from One or More Carriers

One or more carriers do not send a response to the shipper or LSP

for the allotted confirmed capacities.

## Rejected by All Carriers

All carriers reject the confirmed capacities allotted by the shipper

or LSP.

Response Statuses

## Status

Appears When

Preferred Strategy - Accepted by Shipper

The shipper accepts the preferred strategy for a specific

transportation requirement by choosing the Accept Preferred

Strategy button in the award confirmation process.

## Award Confirmation - Pending from Carrier

After the shipper requests a confirmation from the carrier for a

specific RFQ item, this status is set on the response item before the

award confirmation deadline.

## Accepted by Carrier

The carrier accepts the confirmed capacities allotted by the

shipper for a transportation requirement.

## Rejected by Carrier

The carrier rejects the confirmed capacities allotted by the shipper

for a transportation requirement.

## Optimization at Individual Capacity Lines

Transportation Management enables you as a shipper to optimize the business share allocation process to evaluate the carriers at

a granular level. You can specify business share conditions for a strategy at an individual capacity line-level in a freight agreement

RFQ. By providing different business share constraints for different individual capacity lines, you can influence the business share

output of the optimizer at a granular level. These capacity lines can be modeled as the rate table lines.

## Prerequisites

1. You have defined a flat view profile in Customizing for Transportation Management under  Master Data

## Agreement

## RFQs and Quotations

 Define Excel and Flat View Profiles .

2. You have defined a freight agreement RFQ type in Customizing for Transportation Management under  Master Data

## Agreement RFQs and Quotations

 Define Freight Agreement RFQ Types . You have assigned the flat view profile to the

freight agreement type in the same Customizing activity.

## Features

## Location Pair Description

You can choose the Show Descriptions or Hide Descriptions buttons to show or hide the descriptions of the source and

destination locations respectively.

This is custom documentation. For more information, please visit SAP Help Portal.

17


1/14/26, 2:41 PM
## Add or Remove Carriers

You can specify a set of carriers for a specific capacity line. You can add or delete more carriers during the process. You can also

specify whether a carrier is incumbent or non-incumbent.

You can select an individual capacity line and choose  Carrier Assignment

## Add Carrier

. The system displays all the carriers

associated with the capacity line in the Carriers tab. You can add a new carrier and choose Add Selected Carrier button.

You can select an individual capacity line and choose  Carrier Assignment

## Remove Carrier

. The system displays all the

carriers associated with the capacity line in the Carriers tab. You can remove a carrier and choose Remove Selected Carrier

button.

## Strategy Creation for Individual Capacity Lines

You can select individual capacity lines in the flat view and choose the Create Strategy button.

  Note

If you have assigned target share strategies in the Customizing for Transportation Management under  Master Data

## Agreement RFQs and Quotations

 Define Freight Agreement RFQ Types , the system displays the details of the strategy. If

you have not assigned target share strategies in Customizing, you can enter the strategy details and create the strategy

## Update Carrier Strategy Conditions

You can update strategy conditions for a specific carrier by selecting the corresponding response item and choosing Update

Carrier Strategy Conditions button. A dialog box appears in which you can enter the condition values for the following and choose

update:

Minimum business share

## Maximum business share

Note that in the dialog box, only when you select the Update checkbox, the optimizer considers the new value during optimizer

execution.

## Update Master Strategy Conditions

You can update the conditions specific to an entire RFQ item by selecting the corresponding RFQ item and choosing the Update

Master Strategy Conditions button. A dialog box appears in which you can enter the condition values for the following and choose

update:

Minimum number of carriers

Maximum number of carriers

Enable bonus-malus

## Enable transit time

Note that in the dialog box, only when you select the Update checkbox, the optimizer considers the new value during optimizer

execution.

## Strategy Conditions

This is custom documentation. For more information, please visit SAP Help Portal.

18


1/14/26, 2:41 PM
## Optimizer Constraints Based Solution Spend Calculation

Once the strategy is created, the system displays the strategies when you navigate to  Views

 Strategy View . When you select

a strategy, and choose

## Insert

 Conditions , a Strategy Conditions dialog box appears. Here you can specify optimizer strategy

conditions such as the following:

Minimum number of carriers

Maximum number of carriers

Bonus-malus

## Transit time

## Historical Data Based Solution Spend Calculation

You can also choose to perform historical data-based analysis. In the Strategy Conditions dialog box, you can specify the

historical spend constraints such as the following:

Prime charge type

Valid-from date

## Valid-to date

## Optimizer Run Execution

Once you update or enter the strategy conditions, you can choose the Run Optimizer button. On successful run of optimizer, the

system displays the target shares in the Target Share column. The system also displays the corresponding capacity share, which is

calculated based on the business share, in the Proposed Capacity Distribution column.

Note that the optimizer run may fail if the strategy conditions are invalid. You can also choose to select multiple strategy lines and

run the optimizer.

## Simulation of Solution Spend

To calculate estimated spend, choose Simulate Estimated Spend. On calculation of estimated spend, the system displays the

values in the strategy view. When you select the strategy, the system displays the item and item responses along with the

capacities and business shares in the flat view.

## Activities

1. To enable individual capacity level optimization, in the RFQ item, select the Individual Capacity Optimization checkbox.

When you select this checkbox, the system allows you to specify business share conditions for strategies at the individual

capacity line- level.

2. Select an RFQ item and choose Display Flat View.

The system displays the individual capacity lines associated with the flat view profile and charge type.

Note that you can filter the flat view contents based on the rate table dimensions.

3. Specify a set of carriers for the individual capacity lines.

4. Select individual capacity lines in the flat view, create strategies, and specify valid strategy conditions.

This is custom documentation. For more information, please visit SAP Help Portal.

19


1/14/26, 2:41 PM

5. Run the optimizer to get the appropriate business shares for each carrier and simulate the estimated spend to view the

approximate costs incurred.

  Note
If the maximum business share is zero at individual capacity lines, the system does not allocate any share to the specific

carrier. The business share becomes zero when you do not mention any condition at strategy level.

You cannot create strategy conditions for individual capacity lines in the assignment documents in the Document Flow tab in

the freight agreement RFQ master.

## More Information

Freight Agreement RFQ Master

## Strategic Freight Procurement

## Requesting of Quotations for Transportation Services

Strategic freight procurement helps you to investigate and negotiate the best rates from carriers to transport items between

specific locations (trade lanes) and for specific logistical parameters, and then to agree a contract (agreement) with the selected

carriers.

Requesting quotations for transportation services using freight agreement request for quotation (RFQ) masters is a key element in

strategic freight procurement. This is because you use freight agreement RFQ masters to request bids from carriers for

transportation services and, based on those bids, select carriers to fulfill your transportation requirements. When requesting

quotations for transportation services, you can do the following:

Detail your transportation requirements.

Request and compare the bids you receive from carriers.

Distribute target share according to the carriers’ bids.

Simulate the estimated costs based on the carriers’ rates.

Negotiate and award the transportation business to carriers.

Agree the contracts with carriers.

## Prerequisites

You've configured the prerequisites for strategic freight procurement (see Strategic Freight Procurement).

Features

## Templates

You can use templates to help simplify the process of creating freight agreement RFQ masters.

You can define Customizing templates in Customizing for Transportation Management under  Master Data

 Agreement RFQs

and Quotations

 Define Freight Agreement RFQ Master Template . You can transfer Customizing templates across different TM

systems.

This is custom documentation. For more information, please visit SAP Help Portal.

20


1/14/26, 2:41 PM

You can define master data templates directly from the launchpad. If necessary, you can define a master data template based on a

Customizing template. To define, view, and update master data templates for freight agreement RFQ masters, open the Create FA

RFQ Master Templates app.

## Transportation Requirement Details per RFQ Item

You specify your transportation requirements per RFQ item. For each RFQ item, you can specify the following, for example:

The carrier details that are specific to the RFQ item

## The trade lanes where you want the transportation services

The capacity that you need the carrier to be able to fulfill, the capacity the carrier can commit to, and the capacity you

award to the carrier (see Capacities in Rate Tables for Freight Agreement RFQ Masters)

## The commodity codes for the RFQ item

The calculation sheet and rate tables (both kinds, including local) for carriers to use when submitting their rates for the

transportation services (see Calculation Sheet and Rate Table)

## Logistical parameters such as shipping type, movement type, and transportation mode

Note that if you change the validity of the agreement in the freight agreement RFQ master, you can update the validity of all or

selected RFQ items and service products with the same validity period.

## Approval Workflow

You can enable approval workflows so that you have to get approval from an approver before publishing a freight agreement RFQ

master and before creating a freight agreement during strategic freight procurement. When an approver approves the publication

of the freight agreement RFQ master, the system automatically publishes the freight agreement RFQ master and creates and

sends the individual freight agreement RFQs to the carriers. You enable these approval workflows in the Customizing activity

Define Freight Agreement RFQ Types. You can also specify that you want the system to notify an approver when you request

approval. For more information, see Approval Check.

You can also use an offline approval workflow to send work items for freight agreement RFQ masters by e-mail to a user, such as a

customer agent. The user can accept or reject a work item and update the system from their inbox. For more information, see

Offline Workflow for Sending and Approving Work Items.

## Comparison Cockpit

After you receive responses from carriers during strategic freight procurement, you use the comparison cockpit to evaluate which

carrier quoted the best rate by comparing and analyzing some or all of the responses per RFQ item or across RFQ items. The

comparison cockpit supports you in the vital post-bid analysis step, which in turn supports your decision-making process. The

comparison cockpit helps you to decide which carriers to award the transportation business to.

In the comparison cockpit, you compare responses by using the optimizer for carrier selection. The optimizer is especially useful

when the comparison is complex and multiple constraints must be taken into account. You can also compare responses manually

directly in TM or using spreadsheets.

For more information, see Post-Bid Analysis.

## Periodicity

On the Capacities tab of a freight agreement RFQ item, you can specify the periodicity. This specification enables the shipper to

specify the frequency at which the carrier can expect a volume of goods to be shipped. Note that the freight agreement RFQ item

must have just one trade lane. For more information, see Check Against Transportation Allocations.

This is custom documentation. For more information, please visit SAP Help Portal.

21


1/14/26, 2:41 PM

The system can specify the periodicity of an item if you've performed the following activities:

Define a transportation allocation type with a specific periodicity in the Customizing activity Define Transportation

Allocation Types in Customizing for Transportation Management under  Planning

## General Settings

Assign this allocation type to a freight agreement type in the Customizing activity Define Freight Agreement Types in

Customizing for Transportation Management under  Master Data

## Agreements and Service Products

Assign this freight agreement type to the freight agreement RFQ type in the Customizing activity Define Freight

Agreement RFQ Types in Customizing for Transportation Management under  Master Data

 Agreement RFQs and

## Quotations

When you create a freight agreement from the freight agreement RFQ master, the system uses the allocation period you’ve

specified in Define Transportation Allocation Types Customizing activity, as the periodicity in the freight agreement RFQ item. You

can't change this periodicity. If you havn't specified allocation period, the system leaves the periodicity field blank.

## Negotiation Rounds and RFQ Versions

If you aren't satisfied with the responses from carriers, you can create a new negotiation round. You can then change the details of

the freight agreement RFQ master and publish it again. The carriers can then resubmit their rates. The system records the number

of the RFQ negotiation round, indicating how many times you published a freight agreement RFQ master to carriers. The freight

agreement RFQ master must be published before you can create a new negotiation round. When you create a new negotiation

round, the system updates the number of negotiation rounds by 1 and resets the version number to zero. This ensures that the

latest round you publish always has an associated clean version.

You can create a new version of the freight agreement RFQ master without creating a new negotiation round. A new version

enables you to make changes without publishing the freight agreement RFQ master to your carriers. You can use versions for

internal changes before you publish, and you can use negotiation rounds for the changes that you send to your carriers. The freight

agreement RFQ master must have the In Process status to create a new version. If you have created individual freight agreement

RFQs or published the freight agreement RFQ master, you cannot create a new version of the freight agreement RFQ master. When

you create a new version, the system updates the version number by 1 and the negotiation round number remains the same. When

you publish the freight agreement RFQ master, the negotiation round number is updated by 1.

To create a negotiation round, in the freight agreement RFQ master, select  Follow Up

 Create Negotiation Round .

To create a version, in the freight agreement RFQ masters choose the Generate New Version button.

## Award Summary

You can display a summary and graphs of all the logistical information in a freight agreement RFQ master. This summary helps you

to judge how the negotiation process is progressing and make key decisions, such as whether to create a new negotiation round.

You can also check what you spent last year for transportation services with the same logistical information, such as trade lane,

shipping type, and transportation mode. For more information, see Award Summary.

## Mass Individual RFQ Creation and Publication

You can perform the following activities using the program Mass Publication of Freight Agreement RFQ Masters

(/SCMTMS/RFQ_PUBLISH) in transaction SE38.

Create individual freight agreement RFQs for the carriers in multiple freight agreement RFQ masters

Create and publish individual freight agreement RFQs for the carriers in multiple freight agreement RFQ masters

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

22


1/14/26, 2:41 PM

The system doesn't automatically publish the freight agreement RFQ masters if you separated the creation of individual freight

agreement RFQs and the publication of the freight agreement RFQ master into 2 steps. You separate the creation and

publication in Customizing for Transportation Management under  Master Data

 Agreement RFQs and Quotations

## Define

Freight Agreement RFQ Types . If you separated the creation and publication, you can also use this program to publish

multiple freight agreement RFQ masters for existing individual freight agreement RFQs.

## System Notifications

TM integrates with output management (see Output Management) to allow you to automatically notify carriers at various stages

of the strategic freight procurement process as follows:

1. After publication of the freight agreement RFQ master

The system notifies carriers that you published a freight agreement RFQ, and includes the freight agreement RFQ as an

attachment. The system also attaches XLS files for rate tables and local rate tables used for any charge types.

2. When the response deadline is approaching

The system sends a reminder to carriers who haven't responded to the freight agreement RFQ. You define when to send this

reminder in the Customizing activity Define Freight Agreement RFQ Types.

3. On the response deadline

On the last day of the response, the system sends a reminder to carriers who have still not responded to the freight

agreement RFQ.

4. When the freight agreement RFQ is canceled

The system notifies carriers that the freight agreement RFQ has been withdrawn.

5. After creation of the agreement

The system notifies carriers that you created the agreement, and includes the freight agreement, rate tables, and local rate

tables, if any, as attachments.

6. When the agreement is expiring

The system notifies carriers that the freight agreement is expiring and includes the freight agreement both as an

attachment and as a link.

TM uses business-to-business communication to exchange this information electronically between business partners. For more

information, see Freight Agreement Quotation Processing and Forwarding Agreement Quotation Processing.

## Business Share Integration

When you create or update an agreement from an agreement RFQ, the system proposes a target share. The target share is the

output from the optimizer run that you perform in the comparison cockpit in the freight agreement RFQ master. The system

copies the share into the item details of the agreement. For more information, see Agreement Maintenance.

The business share is automatically included in the agreement from the agreement RFQ. The system includes the target share in

the business share, and uses the business share in the carrier selection settings in planning. For more information, see Business

Share.

## Maintenance of RFQ Masters Using Spreadsheets

You can download the RFQ master data into a spreadsheet for editing. The spreadsheet contains the following information:

## RFQ header details

This is custom documentation. For more information, please visit SAP Help Portal.

23


1/14/26, 2:41 PM

## RFQ items

Requested capacities

Offered capacities

## Confirmed capacities

Calculation sheets and local calculation sheets

## Calculation sheet items

The spreadsheet also contains a worksheet for each rate table or local rate table. You can't edit the details in the worksheet.

However, you can download the rate tables or local rate tables as an XLS file and then upload the edited XLS file back into the RFQ

master in your TM system. The system updates the RFQ master with your changes.

To download or upload a freight agreement RFQ master, choose Freight Agreements app from the launchpad. From the freight

agreement work list, choose Freight Agreement RFQ Masters. Open the freight agreement RFQ master and go to the Excel

Integration tab page. You can also download or upload a freight agreement RFQ master using program Excel Integration with

Freight Agreement RFQs (/SCMTMS/CARR_RFQ_EXCEL) in transaction SE38.

  Note

Your carriers can also download their individual freight agreement RFQs for editing when responding to you with their rates for

the transportation services. For more information, see Responses from Carriers Using Spreadsheets.

If one or more carriers have responded to the freight agreement RFQ, you can download a spreadsheet that enables you to

compare the responses of the carriers in the freight agreement RFQ master.

## Carrier Collaboration

If your carriers don't use TM, you can allow them to view and respond to the individual freight agreement RFQs that they receive

from you using a carrier worklist. Your carriers contact your purchasing organization for logon details to this personal object

worklist.

Carriers can use the Manage Freight Agreement RFQs app to view the individual freight agreement RFQs specific to the carrier

organization. For more information, see Carrier Collaboration.

## Activities

To create or update freight agreement RFQ masters, choose the Freight Agreements app from the launchpad.

To create a freight agreement RFQ master and to start the process of updating a freight agreement, choose the Freight

Agreements app from the launchpad. Open the freight agreement and choose the Create RFQ Master button.

## More Information

Strategic Freight Procurement

Archiving Agreements and RFQ Masters

## Responses from Carriers Using Spreadsheets

This is custom documentation. For more information, please visit SAP Help Portal.

24


1/14/26, 2:41 PM

When responding to you with their rates for transportation services, carriers can download an individual freight agreement RFQ

into a spreadsheet for editing. You can choose a structured format, a compatible format, or a flat view format for your carriers to

download.

## Prerequisites

You've specified the format of the spreadsheet that you want carriers to download in Customizing for Transportation

Management under  Master Data

 Agreement RFQs and Quotations

 Define Freight Agreement RFQ Types .

## Features

Spreadsheet Formats

## Structured format

The data shown in this format is structured so that you don't have to scroll too much to get to the most important

information. There's a separate sheet for the RFQ header details and for each RFQ item. We recommend using the

structured format when there's a low number of RFQ items.

The address of the location used in the trade lanes or rate tables (both kinds, including local) is also included.

## Compatible format

This format displays the following details in one row in one sheet:

RFQ header details

## RFQ items

Requested capacities

Offered capacities

Confirmed capacities

## Calculation sheet items

There are then separate sheets for each rate table (both kinds, including local). This format is available for compatibility

reasons only.

## Flat View Format

This format displays the capacity demand and rates as a consolidated view consisting of all the charges and rates that are

relevant for negotiating a freight agreement RFQ.

## Editing of the Spreadsheet by Carrier

Carriers can only edit certain pieces of information such as the following:

RFQ Items: Offered capacities, Responded column, and Confirmed column

## Calculation sheet items: Amounts for flat charges

Local rate table: Offered amounts, offered capacities, and offered transit times

You can also download or upload a freight agreement RFQ using program Excel Integration with Freight Agreement RFQs

(/SCMTMS/CARR_RFQ_EXCEL) in transaction SE38.

This is custom documentation. For more information, please visit SAP Help Portal.

25


1/14/26, 2:41 PM
## Related Information

Requesting of Quotations for Transportation Services

Capacities in Rate Tables and Local Rate Tables for Freight
Agreement RFQ Masters

## Use

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

You can specify capacities in the rate tables of freight agreement RFQ masters. Capacities enable you to publish the amount of

business you require from a carrier. Note that the business share feature also enables you to specify the amount of business you

want to allocate to a carrier. However, you use the business share for your own analysis and business decisions. You use capacities

to seek a response from carriers and as an output of business share decisions. For more information about business shares, see

Business Share.

In the rate table of a freight agreement RFQ master, the system displays the following fields for a scale dimension in the  Dates

and Validity

 Rates  screen area:

## Requested Capacity

The capacity you require from a carrier. You enter this information before publishing the freight agreement RFQ master.

## Offered Capacity

The capacity the carrier offers to you. The carrier enters this information when responding to the freight agreement RFQ

master.

## Confirmed Capacity

The actual capacity you award to a carrier. After you compare the responses from the carriers and select a carrier, the

system enters the confirmed capacity based on the target share proposed by the optimizer. You can manually change the

confirmed capacity.

## Average Load

The average capacity per shipment that you transport in a trade lane during the validity period of the freight agreement

RFQ master.

## Target Share

The capacity as a percent of the total business for an item in a trade lane that you award to a carrier.

  Note

You can create rate tables or local rate tables from within a freight agreement RFQ master. However, you can’t specify rate

tables. Also, rate tables only display the confirmed capacity.

## Features

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

This is custom documentation. For more information, please visit SAP Help Portal.

26


1/14/26, 2:41 PM

Capacity Drivers and Capacity Dimensions

## Capacity drivers

Capacity drivers are the dimensions in a rate table that determine your capacity requirements. For example, when you

specify source location A and destination location B as capacity drivers, you specify that you need the specified capacity

from location A to location B. When you specify the capacity drivers, the system doesn’t take any of the other dimensions

into account for capacity.

In most cases, the source location and destination location are the capacity drivers (given that you’re working in a trade

lane for a freight agreement RFQ master). However, you can also use other drivers, such as equipment type and commodity

code. You must specify at least one capacity driver in a rate table and you can have multiple capacity drivers.

Note that if you specify source location and destination location as the capacity drivers, you can’t select source location

and destination location as column scales in the  Dates and Validity

 Rates  screen area.

  Note

You must have the same requested capacity for all instances of a combination of capacity drivers in a rate table.

For example, you have 3 dimensions in a rate table: source location, destination location, and gross weight. The capacity

drivers are source location and destination location. The rate table appears as follows:

Source Location

## Destination Location

Gross Weight >= (TON) Requested Capacity

A

A

A

A

A

B

B

C

D

D

100

500

100

100

500

100

100

200

300

300

The requested capacity is the same for all the gross weight values for the location pairs. The system copies the

requested capacity of the first instance of the combination of capacity drivers throughout the rate table for all instances

of that combination of capacity drivers.

## Capacity dimension

You can specify the dimension that you use to enter your capacity requirements for an item in a trade lane. You can only use

a number-based dimension. Therefore, you must use a number-based calculation base as the capacity dimension. This in

turn means you must use a calculation base that is associated with one of the following scale bases:

Number

Quantity

Volume

## Weight

For example, you can’t specify a commodity code as a capacity dimension because it isn’t number-based. Note that the

system doesn’t use dimensional weight when estimating the strategy spend. Therefore, you can’t use the following

calculation bases:

Chargeable Weight (CHRG_WEIGHT)

Chargeable Weight Based on Net Weight (CHRG_WEIGHT_NET)

This is custom documentation. For more information, please visit SAP Help Portal.

27


1/14/26, 2:41 PM

Customs Value (CUSTOMS_VALUE)

You also can’t use an amount-based dimension, for example, you can’t use the following calculation bases:

Goods Value (GOODS_VALUE)

Insurable Value (INSURABLE_VALUE)

Customs Value (CUSTOMS_VALUE)

Note that you can specify only one capacity dimension in a rate table.

You can’t specify the same dimension as both a capacity driver and a capacity dimension.

  Note
If you don’t specify a capacity dimension, the system assumes that you’re working with full container loads (FCLs) or full truck

loads (FTLs). The capacity of the truck or container is then considered as full.

## Creating Freight Agreement RFQ Masters from Freight Agreements

You can create a freight agreement RFQ master from a freight agreement. If there’s a rate table in the freight agreement, the

system adds a copy of the table as a rate table for the RFQ master. The system keeps the dimensions in the rate table, but clears

the amounts for the rates and capacities.

## Full Container Loads or Full Truck Loads

When working with FCLs or FTLs, the capacity of the truck or container is considered as full and you don’t need to specify

capacities. In an FCL or FTL scenario, you also can’t edit the average load. You can’t edit the average load because you work with

full loads, and the average load is therefore not a factor in your capacity requirements. The system doesn’t validate the shipping

type against the capacity dimension.

## Deleting Rates

If you delete the rate for a selected line, the system deletes only the relevant rate in the  Dates and Validity

 Rates  screen area.

The system doesn’t delete the amounts of other related values for the same scale dimension combination. For example, you have 3

rates for a source location and destination location, with 3 different gross volumes. If you delete the rate in the first row, the system

doesn’t delete the rate in the 2 remaining rows. The following table illustrates this behavior:

## Source Location

Destination Location Gross Volume

>=1,000

Requested Capacity

CSI-APORT-AMS

CSI-APORT-HKG

1000

CSI-APORT-AMS

CSI-APORT-HKG

2000

CSI-APORT-AMS

CSI-APORT-HKG

3000

None

110

115

100

100

100

  Note
If you delete the capacity for a selected line, the system deletes the capacity for all other lines with the same combination of

capacity drivers. This occurs because you must have the same requested capacity for all instances of a combination of capacity

drivers.

## Activities

This is custom documentation. For more information, please visit SAP Help Portal.

28


1/14/26, 2:41 PM

To display the capacities, on the  Dates and Validity

 Rates  tab page of the rate table or local rate table choose the Show More

Info button. The system only displays capacities if you’ve selected at least one item as the capacity driver in the  General Data

 Scales  screen area.

You can only enter the requested capacity and the average load. The carrier can enter only the offered capacity, in a response.

The system displays the confirmed capacity in the rate table or the local rate table when you award transportation business to a

carrier and create an agreement.

To enable FCL or FTL, select FCL or FTL as the shipping type for the item in the Items screen area of the freight agreement RFQ

master.

More Information

## Agreement RFQ

Requesting of Quotations for Transportation Services

## Rate Table

Rate Definition and Maintenance

Post-Bid Analysis

## Use

After you receive responses from carriers for the quotations you requested, you use the comparison cockpit to evaluate which

carrier quoted the best rate for the specified periodicity. You compare and analyze some or all of the responses per RFQ item or

across RFQ items. The comparison cockpit supports you in the vital post-bid analysis step, which in turn supports your decision-

making process. The comparison cockpit helps you to decide which carriers to award the transportation business to and in what

proportion.

  Note
The system simulates an estimation of the cost; the system doesn't calculate the actual charges.

If you know which carriers you want to award the transportation business to, you can directly create or update the freight

agreements.

## Integration

You compare responses during strategic freight procurement (see Strategic Freight Procurement).

## Prerequisites

A freight agreement RFQ master has been published.

Carriers have responded to the individual freight agreement RFQs with their rates for the transportation services.

You have defined target share strategies in Customizing for Transportation Management under  Master Data

 Agreement RFQs and Quotations

 Define Target Share Strategies .

This is custom documentation. For more information, please visit SAP Help Portal.

29


1/14/26, 2:41 PM

You've defined a calculation profile for the organizational unit in Customizing for Transportation Management under

Basic Functions

 Charge Calculation

## Basic Settings

 Define Calculation Profiles .

You've defined a charges profile for the organizational unit, including specifying a local currency, and assigned the

calculation profile defined above.

You define the charges profile in Customizing for Transportation Management under  Basic Functions

## Charge

Calculation

## Basic Settings

 Define Charges Profiles .

You've assigned the charges profile defined above to the organizational unit using transaction PPOME.

## Features

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

## Optimization-Based Response Comparison

You compare responses by using the optimizer for carrier selection. The optimizer is especially useful when the comparison is

complex and multiple constraints must be taken into account. With the optimizer, you can simulate and analyze the potential

strategy spend depending on your strategy conditions. The system can then display the results by amount and strategy version in

a strategy spend comparison graph. The system displays results for the periodicity specified in the freight agreement RFQ master.

The optimizer uses target share strategies and strategy conditions to propose target shares for carriers. You define target share

strategies and strategy conditions in the Customizing activity Define Target Share Strategies. You can define strategy conditions

such as the minimum and maximum target share percentage that the optimizer should respect when proposing target shares for

carriers and the minimum and maximum number of carriers to include in the target share strategy. You can specify strategy

conditions for incumbent carriers and strategy conditions for all other carriers. Depending on your business process, you might

want to award a higher percentage of business to an incumbent carrier. Note that the optimizer also takes the capacity promised

by the carriers into account. This ensures that the optimizer proposes a target share for a carrier that is within the carrier’s

confirmed capacity.

In the comparison cockpit, you can use the Copy button to create a new strategy by copying an existing strategy. You can manually

change the attributes of the copied strategy. You can either copy all the attributes of a strategy or you can copy a strategy without

the target shares. When you copy a strategy without the target shares, the system copies only the strategy conditions and doesn't

copy all other attributes such as, business shares, target shares, and proposed capacities. You can manually allocate target shares

for the carriers and run the optimizer.

  Note

After specifying target share strategies and strategy conditions in a freight agreement RFQ master, you can run the

optimizer in the back end for specific target share strategies or for all target share strategies in the freight agreement

RFQ master. The system can also estimate the strategy spend at the same time.

You can run the optimizer in the back end using program Mass Optimizer Run and Strategy Spend Estimation

(/SCMTMS/OPTIMIZER_RUN) in transaction SE38. You can use this program for a single freight agreement RFQ

master or for multiple freight agreement RFQ masters.

If you don't specify the target share strategies when using this program for a single freight agreement RFQ master, the

system runs the optimizer for all the target share strategies in the freight agreement RFQ master. When using this

program for multiple freight agreement RFQ masters, you can run the optimizer only for all target share strategies in the

freight agreement RFQ masters.

You can add additional constraints to the optimizer (for example, in relation to risks or bonuses) when comparing

responses to freight agreement RFQs.

This is custom documentation. For more information, please visit SAP Help Portal.

30


1/14/26, 2:41 PM

For more information, see Customizing for Transportation Management under  Business Add-Ins (BAdIs) for

Transportation Management

 Master Data

## Agreement RFQs

 BAdI: Additional Optimizer Constraints .

You can add additional parameters and costs before or after estimating the strategy spend.

For more information, see Customizing for Transportation Management under  Business Add-Ins (BAdIs) for

Transportation Management

 Master Data

## Agreement RFQs

 BAdI: RFQ Strategy Spend Estimation .

You can replace the standard strategy spend estimation with your own customer-specific strategy spend estimation.

For more information, see Customizing for Transportation Management under  Business Add-Ins (BAdIs) for

Transportation Management

 Master Data

## Agreement RFQs

 BAdI: Customer-Specific Strategy Spend

Estimation .

You can reward or penalize a carrier because of the past performance of a carrier in a trade lane in the optimizer.

For more information, see Customizing for Transportation Management under  Business Add-Ins (BAdIs) for

Transportation Management

 Master Data

## Agreement RFQs

 BAdI: Specification of Historical Parameters for

Optimizer

.

You can reward or penalize a carrier based on the difference between the requested transit time and the offered transit

time in the optimizer. For example, if the difference is of less value, you can award a higher reward to the carrier.

For more information, see Customizing for Transportation Management under  Business Add-Ins (BAdIs) for

Transportation Management

 Master Data

## Agreement RFQs

 BAdI: Specification of Transit Time for Optimizer

.

The optimizer proposes the most ideal target share distribution to produce the most cost effective solution. The system can then

simulate the estimated strategy spend based on the responses you received from the carriers and the target share strategies

proposed by the optimizer. This simulation gives you an indication of how much you’ll potentially spend if you choose the target

share distribution proposed by the optimizer. Note that you can run the optimizer repeatedly with different target share strategies

and strategy versions. This allows you to simulate the impact of strategy changes and compare spend variations across different

strategy versions. For information about how to use the optimizer to compare responses, see Strategic Freight Procurement. For

information about how the system estimates the strategy spend, see Strategy Spend Estimation.

An optimization-based response comparison with two versions of the same strategy mentioned above is depicted in the following

figures:

  Note

The system can compare only one rate table at a time. The system can't compare charge types with different rate tables.

This is custom documentation. For more information, please visit SAP Help Portal.

31


1/14/26, 2:41 PM

Rate tables must not contain the calculation bases Transportation Zone of Source Location (SOURCELOC_ZONE) or

Transportation Zone of Destination Location (DESTLOC_ZONE).

The system takes into account the minimum and maximum rate values that you can specify in rate tables for the line

items of RFQ items.

For more information, see Calculation Sheet Maintenance.

A local rate table can have just one validity period.

The system takes into account the rates for all the capacity drivers.

For more information about capacity drivers, see Capacities in Rate Tables for Freight Agreement RFQ Masters.

If you manually change the target share for a carrier after the optimizer run, the system estimates the strategy spend

based on the carrier-level target share.

The system no longer bases the estimation on the rate-table target share.

If the optimizer proposes a target share at rate-table level for a location pair, the system applies the same target share

for all the charge types in the calculation sheets for the location pair.

If the optimizer doesn’t propose a target share at the rate-table level, the system bases the estimation for all the charge

types on the carrier-level target share.

If the optimizer can't fill the total requested capacity because of the minimum or maximum target share you specified

for the carriers, the optimizer will dismiss the minimum or maximum target share and accept the capacity offered by the

carriers.

  Example

You request a capacity of 100 kg. Carrier 1 offers 60 kg and carrier 2 offers 100 kg.

You specified a maximum target share of 70% for carrier 1 so accept the offered capacity of 60 kg from that carrier.

You specified a maximum target share of 30% for carrier 2. However, this doesn't fill the total requested capacity of 100

kg. Therefore, the optimizer dismisses the maximum target share of 30% for carrier 2 and instead accepts 40 kg of the

capacity offered by carrier 2. The total requested capacity is filled.

To insert a target share strategy into a freight agreement RFQ master, in the Response Comparison screen area of the comparison

cockpit you must first select the charge types that you want to compare using the optimizer.

This is custom documentation. For more information, please visit SAP Help Portal.

32


1/14/26, 2:41 PM

## Manual Response Comparison

If the comparison is fairly simple and the rates are the only constraints that must be taken into account, you can compare

responses manually by carrier and charge type directly in Transportation Management (TM). Note that you can only compare the

responses manually directly in TM for charge types with flat amounts. The system ranks the carriers according to the lowest

quoted rate per charge type. The system also displays the results in a response comparison graph.

Alternatively, if the charge type has a rate table or a local rate table associated with it, you can compare the rate tables in a

spreadsheet. If you compare the rate tables in a spreadsheet, the system doesn't display the results in a response comparison

graph.

Note that if you compare responses manually, you manually enter the target share for the carriers. As there's no optimizer

involvement, the system estimates the strategy spend based on the carrier-level target share. The system doesn’t base the

estimation on the rate-table target share.

## Historical Spend Simulation

In the optimizer conditions, you can specify a prime charge type and validity periods. The system uses the structure of the rate

table or the local rate table of the prime charge type to find previous orders with the same attributes within the validity periods.

The system then calculates the charges for these orders with the rates that the carriers have proposed in the individual freight

agreement RFQs. The system uses the total charge for all the previous orders to determine the target share when you run the

optimizer. Since the input to the optimizer are charges and not rates, the accuracy of the optimizer increases. Note that the system

uses the report Historical Spend Simulation (/SCMTMS/SOL_SPEND_SIMULATE) in transaction SE38 to find the pervious

orders.

## Currency Conversion

If you include multiple currencies when comparing responses, the system converts the currencies into a single currency as follows:

If the RFQ items contain multiple currencies, the system converts the currencies and displays the amounts in the currency

of the freight agreement RFQ master.

If the RFQ items contain a single currency that is different to the currency of the freight agreement RFQ master, the system

displays the amounts in the currency of the RFQ items.

If the RFQ items contain a single currency but the charge types contain a different currency, the system converts the

currencies and displays the amounts in the currency of the RFQ items.

You can specify the exchange rates in Customizing for SAP NetWeaver under  General Settings

 Currencies

 Enter Exchange

Rates .

## Graphs

You can use the response comparison graph and strategy spend comparison graph to display the comparisons visually. There's a

range of graph types available, for example, stacked and horizontal graphs, pie charts, line charts, and area charts. The default

graph type is a 100% stacked column graph.

You can use the comparison graph to view the system proposed capacities. You can also view the amount that is spent if you

accept the capacity proposal.

## Preferred Target Share Strategy

After comparing the responses using the optimizer for carrier selection, you select your preferred target share strategy. You must

then accept your preferred strategy before awarding the transportation business to carriers. When you accept your preferred

target share strategy, the system automatically calculates the confirmed capacity in the freight agreement RFQ master based on

This is custom documentation. For more information, please visit SAP Help Portal.

33


1/14/26, 2:41 PM

the target share proposed by the optimizer. You can manually change this confirmed capacity. You can then create or update

freight agreements for the carriers you’re awarding the business to.

More Information

## Award Summary

Requesting of Quotations for Transportation Services

Freight Agreement RFQ Master

Agreement Maintenance

Strategy Spend Estimation

## Use

As part of the post-bid analysis during the strategic freight procurement process, you can compare responses from carriers in the

comparison cockpit. Comparing responses helps you to evaluate which carrier quoted the best rate for the specified periodicity. In

Transportation Management, you can either compare the responses manually by carrier and charge type directly or by using the

optimizer for carrier selection. For more information about how to compare responses, see Post-Bid Analysis.

With optimization-based response comparison, the system proposes the most ideal target share distribution across carriers,

taking into account your strategy conditions and the capacity promised by the carriers. The system then estimates the total cost

of using a particular carrier or carriers to provide the transportation business for the selected RFQ items in a freight agreement

RFQ master for the specified periodicity. The system bases the estimated cost on the target share proposed by the optimizer. The

system estimates the strategy spend in different ways depending on the responses you select in the Response Comparison

screen area of the comparison cockpit.

  Note

The system estimates the cost; the system doesn’t calculate the actual charges.

If you compare responses manually, you enter the target share for the carriers. Since there’s no optimizer involvement,

the system estimates the strategy spend based on the carrier-level target share. The system doesn’t base the

estimation on the rate-table target share.

Rate tables (both kinds, including local) must not contain the calculation bases Transportation Zone of Source

Location (SOURCELOC_ZONE) or Transportation Zone of Destination Location (DESTLOC_ZONE).

## Prerequisites

You’ve configured the prerequisite settings for the post-bid analysis of the responses you receive from carriers (see Post-

Bid Analysis).

If a line item has a flat amount, you must not specify a calculation resolution base.

## Estimation Considerations

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

This is custom documentation. For more information, please visit SAP Help Portal.

34


1/14/26, 2:41 PM

The system estimates the strategy spend for the full validity period of each RFQ item.

If the periodicity of the RFQ item is different to the validity period, the system adjusts the calculation to take this into

account. For example, the validity period for an RFQ item is 12 months and the periodicity is monthly. Therefore, the system

estimates the strategy spend for the full 12 months by multiplying the estimated strategy spend by the periodicity value of

12.

The system takes into account the minimum and maximum rate values that you can specify in rate tables for the line items

of RFQ items.

For more information about minimum and maximum rate values, see Calculation Sheet Maintenance.

The system can estimate the strategy spend for a single rate table only.

The system can’t compare charge types with different rate tables at the same time.

A local rate table can have just one validity period.

The system takes into account the rates for all the capacity drivers.

For more information about capacity drivers, see Capacities in Rate Tables for Freight Agreement RFQ Masters.

If you manually change the target share for a carrier after the optimizer run, the system estimates the strategy spend

based on the carrier-level target share.

The system no longer bases the estimation on the rate-table target share.

If the optimizer proposes a target share at rate-table level for a location pair, the system applies the same target share for

all the charge types in the calculation sheets for the location pair.

If the optimizer doesn’t propose a target share at the rate-table level, the system bases the estimation for all the charge

types on the carrier-level target share.

You can specify only one of the following capacity dimensions when you run the optimizer:

Gross weight

Gross volume

## Container count

You can add additional parameters and costs before or after estimating the strategy spend.

For more information, see the following business add-ins in Customizing for Transportation Management under

Business Add-Ins (BAdIs) for Transportation Management

 Master Data

 Agreement RFQs :

BAdI: RFQ Strategy Spend Estimation

## BAdI: Additional Optimizer Constraints

## BAdI: Specification of Historical Parameters for Optimizer

You can replace the standard strategy spend estimation with a strategy spend estimation that suits your specific

requirements.

For more information, see Customizing for Transportation Management under  Business Add-Ins (BAdIs) for

Transportation Management

 Master Data

## Agreement RFQs

 BAdI: Customer-Specific Strategy Spend Estimation .

Estimation Examples

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

35


1/14/26, 2:41 PM

In the examples below, the validity period for RFQ items is 12 months and the periodicity is monthly. Therefore, the periodicity

value is 12.

## Example Data

You have a freight agreement RFQ master for the US East Zone to the US West Zone listing the following carriers:

SON_CAR001

SON_CAR002

SON_CAR003

SON_CAR004

You have the following RFQ items in the freight agreement RFQ master:

## RFQ Item

Transportation

Movement Type

Requested

Yearly Budget

Shipping Type

Validity Period

## Mode

Capacity

(USD)

Item 100: US

## Road

Door to port

5,200 kg per

200,000

Less than truck

01.02.2014-

East Zone to

Dallas

month

load (LTL)

31.01.2015

Item 200: Dallas

## Road

Port to port

30 containers

450,000

Full truck load

01.02.2014-

to Denver

per month

(FTL)

31.01.2015

Item 300:

## Road

Port to door

5,200 kg per

150,000

LTL

Denver to US

West Zone

month

Item 400: US

## Road

Door to door

30 containers

750,000

FTL

East Zone to US

West Zone

per month

01.02.2014-

31.01.2015

01.02.2014-

31.01.2015

The RFQ items have the following capacity details:

## Details

Requested Capacity

Offered Capacity

Confirmed Capacity

Gross Weight

5,200 kg

Not applicable at this stage Not applicable at this stage

Equipment Group

## Pallets

Equipment Type

IG2

Pallets

IG2

Pallets

IG2

Periodicity

## Monthly

Not applicable

Not applicable

Capacity Dimension

Gross Weight

Not applicable

## Not applicable

Based on the details above, you can estimate the strategy spend for the following scenarios:

1. For items that divide the end to end transportation into stages

For each stage with each carrier for RFQ items 100, 200, and 300

2. For an Individual Item that covers all stages of end to end transportation

For door-to-door FTL with each carrier for RFQ item 400

This is custom documentation. For more information, please visit SAP Help Portal.

36


1/14/26, 2:41 PM

Scenario 1: Estimate for Each Stage with Each Carrier for RFQ Items 100, 200, and 300

For this scenario, you can run the optimizer by specifying constraints across RFQ items 100, 200, and 300. Alternatively, you can

run the optimizer separately per item with the same constraints for RFQ items 100, 200, and 300 for the same result.

For scenario 1, the optimizer proposes the following target share strategy for the freight agreement RFQ master at the carrier level

across the RFQ items:

## Carrier

Target Share (%)

Estimated Spend (USD)

SON_CAR001

SON_CAR002

SON_CAR003

SON_CAR004

20

20

40

20

5,592.60

5,856

10,812

5,642

You indicate your preferred target share strategy, before you create or update agreements with the carriers you’re awarding the

business to.

If you run the optimizer per item, the optimizer proposes the following target share strategy per item:

RFQ item 100 (strategy spend estimated as USD 16,525.60):

## Carrier

Target Share (%)

Estimated Spend (USD)

SON_CAR001

SON_CAR002

SON_CAR003

SON_CAR004

20

20

40

20

3,286.40

3,452.80

6,406.40

3,380

RFQ item 200 (strategy spend estimated as USD 2,940):

## Carrier

Target Share (%)

Estimated Spend (USD)

SON_CAR001

SON_CAR002

SON_CAR003

SON_CAR004

20

20

40

20

585

630

1,140

585

RFQ item 300 (strategy spend estimated as USD 8,437):

## Carrier

Target Share (%)

Estimated Spend (USD)

SON_CAR001

SON_CAR002

20

20

1,721.20

1,773.20

This is custom documentation. For more information, please visit SAP Help Portal.

37


1/14/26, 2:41 PM

## Carrier

Target Share (%)

Estimated Spend (USD)

SON_CAR003

SON_CAR004

40

20

3,265.50

1,677

The system also proposes the target strategy share at each RFQ item level. If there’s a rate table (both kinds, including local)

included in the RFQ items you’re estimating, then the system stores the proposed target strategy share for the trade lane using the

rate table (both kinds, including local) in the Target Share column of the rate table (both kinds, including local).

Scenario 2: Estimate for Door-to-Door Full Truck Load with Each Carrier for RFQ Item 400

For this scenario, you can estimate the strategy spend by specifying constraints and running the optimizer for RFQ item 400. The

optimizer proposes the following target share strategy:

Version 1 (strategy spend estimated as USD 13,998) with the following target share distribution:

## Carrier

Target Share (%)

Estimated Spend (USD)

SON_CAR002

SON_CAR003

SON_CAR004

SON_CAR001

20

20

20

40

2,856

2,730

2,796

15,616

Version 2 (strategy spend estimated as USD 13,930.50) with the following target share distribution:

## Carrier

Target Share (%)

Estimated Spend (USD)

SON_CAR002

SON_CAR003

SON_CAR004

SON_CAR001

20

35

35

10

2,856

4,777.50

4,893

1,404

Version 2 would be your preferred target share strategy if the decision is based solely on the strategy that yields the lowest costs.

Based on these analyses, you can decide if you want to use scenario 1 or scenario 2 for your transportation needs.

## More Information

Strategic Freight Procurement

Award Summary

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

38


1/14/26, 2:41 PM

You can display a summary and graphs of all the logistical information in a freight agreement RFQ master. This summary helps you

to judge how the negotiation process is progressing and make key decisions, such as whether to create a new negotiation round.

To access the award summary, in the freight agreement RFQ master choose the Award Summary tab page.

## Integration

The Award Summary tab page is available in the freight agreement RFQ master (see Freight Agreement RFQ Master). You use the

award summary during strategic freight procurement (see Strategic Freight Procurement).

## Prerequisites

A freight agreement RFQ master has been published.

Carriers have responded to the individual freight agreement RFQs with their rates for the transportation services.

Features

## Views

You can view the award summary using the following views:

## Trade Lane

This view provides a summary of all RFQ items across the trade lanes of the freight agreement RFQ master. You can view important

logistical parameters associated with trade lanes, such as the following:

Equipment type

## Transportation mode

## Estimated strategy spend for the trade lane

Budget allocated for the trade lane for the specified periodicity

On the Items tab page, you can view further information, for example:

Number of carriers operating in the trade lane

Target share distribution across various carriers

## Agreement-related information

You can see how the negotiation process with carriers is progressing because you can see how the estimated spend for the trade

lane compares to the planned periodicity budget. For example, if you can easily see that the estimated spend is greater than the

planned periodicity budget, you can consider creating a new negotiation round.

The graphs indicate the comparison of planned periodicity budget, estimated spend, and historical spend. On the Items tab page,

the graph displays the information by estimated spend and by capacity.

## Carrier

This view provides an award summary of all the carriers, including the target share for each carries and the carriers that you

awarded the transportation business to. In this view, you find information related to important logistical parameters that the

carrier has agreed to provide or operate within, such as:

This is custom documentation. For more information, please visit SAP Help Portal.

39


1/14/26, 2:41 PM

Transportation mode

Equipment type

## Shipping type

Strategy spend version

## Amount

In the Estimated Spend view, the graph indicates the spend variation per RFQ item for all carriers. In the Capacity view, the graph

indicates the capacity per RFQ item for all carriers and the target strategy spend assigned to them.

## RFQ Item

This view provides an award summary by RFQ item. The graphs display a comparison of the periodicity budget versus the

estimated spend per item and the spend per carrier for the chosen item. On the Trade Lanes tab page, you can view further

information, for example, carrier and target share.

## Historic Spend

In the Trade Lane and RFQ Item view, the system can display what you spent historically for transportation services with the same

logistical information, that is, with the same trade lane, transportation mode, and shipping type. The system sends a query to SAP

NetWeaver Business Warehouse for the historical data and displays it in graph format with the periodicity budget and the

estimated strategy spend. Note that if the currency from SAP NetWeaver Business Warehouse differs to the currency in the RFQ

master, the system converts the currency to match the currency of the RFQ master.

To check what you spent historically for transportation services with the same logistical information, choose the Display Historic

Spend button in the Trade Lane or RFQ Item view on the Award Summary tab page.

## More Information

Requesting of Quotations for Transportation Services

## Advanced RFQs

Allows you to work with the improved usability and features of freight agreement requests for quotation (RFQs).

## Prerequisites

You've ensured that the checkbox to use advanced RFQs is selected for the freight agreement RFQ type. You define freight

agreement RFQ types in Customizing for Transportation Management under  Master Data

 Agreement RFQs and Quotations

 Define Freight Agreement RFQ Types .

  Note

This option is selected by default when you define new freight agreement RFQ types.

If you don't keep this option selected, note the following points:

Improved usability and features aren't available when working with freight agreement RFQ masters.

You continue to work with freight agreement RFQ masters as before.

This is custom documentation. For more information, please visit SAP Help Portal.

40


1/14/26, 2:41 PM

We recommend that you don’t select this checkbox for existing freight agreement RFQ types that are used in ongoing RFQ

negotiations. This is to ensure that there are no compatibility issues with your existing documents. However, when defining new

freight agreement RFQ types for new documents, we recommend that you keep this checkbox selected.

## Features

New Web Dynpro application configuration /SCMTMS/TCM_EFA_RFQ_ADV so you can work with advanced freight

agreement RFQ masters

The option to maintain only one purchasing organization in freight agreement RFQ masters (selected by default)

The option to create only one RFQ item in freight agreement RFQ masters (selected by default)

Maintaining trade lanes for freight agreement RFQ items is now optional when publishing freight agreement RFQ masters.

Capacity details can be specified using the quantity dimension

Option to edit certain details of a freight agreement RFQ master after it is published

You can edit the response deadline, update the planned agreement validity period, responsible person, freight agreement

RFQ master description, and add notes and attachments.

Work with a single user interface for capacity demand and rates when negotiating freight agreement RFQs with carriers

For more information, see Capacity Demand and Rates.

Option to reject participation in a freight agreement RFQ on behalf of a carrier

Option to reopen a freight agreement RFQ for negotiation with a carrier based on the following conditions:

The response deadline is not in the past.

The freight agreement RFQ has one of the following statuses: Submitted by Carrier, Submitted with Errors by

Carrier, Participation Rejected by Carrier.

The status of the freight agreement RFQ master is either Published or Updated After Publication.

Option to use capacity demand and rates when a freight agreement RFQ is created from a freight agreement

Option to implement a business add-in (BAdI) to perform business-specific validations when a carrier uploads a response

for a freight agreement RFQ

For more information, see Customizing for Transportation Management under  Business Add-Ins (BAdIs) for

Transportation Management

## Master Data

 Agreement RFQs and Quotations

 BAdI: Validate Carrier Response .

## Capacity Demand and Rates

Allows you as a shipper or logistics service provider to work with a single user interface (UI) for capacity demand and rates when

negotiating freight agreement requests for quotation (RFQs) with carriers.

## Prerequisites

You have defined a freight agreement RFQ type in Customizing for Transportation Management under  Master Data

 Agreement RFQs and Quotations

 Define Freight Agreement RFQ Types .

Ensure that you have selected the checkbox to use advanced RFQs in the freight agreement RFQ type.

Ensure that you have selected the checkbox to enable capacity demand and rates for the freight agreement RFQ type.

This is custom documentation. For more information, please visit SAP Help Portal.

41


1/14/26, 2:41 PM

You have defined a calculation sheet template in Customizing for Transportation Management under  Basic Functions

 Charge Calculation

 Basic Settings

## Templates

 Define Calculation Sheet Templates .

## Features

You can use the following features of capacity demand and rates to help simplify working with freight agreement RFQs:

## Capacity Demand and Rates Profile

Use a capacity demand and rates profile to create a calculation sheet, calculation sheet line items, and rate tables. You can

assign a capacity demand and rates profile to an RFQ item in an Advanced RFQ. (For more information, see Advanced

RFQs.)

You define a capacity demand and rates profile in Customizing for Transportation Management under  Master Data

 Agreement RFQs and Quotations

 Define Capacity Demand and Rates Profiles .

You can use a capacity demand and rates profile to do the following:

Specify a calculation sheet template in the profile.

Based on the calculation sheet template, the system proposes fields that you can select and assign to the profile.

These fields are displayed in the capacity demand and rates flat view (see Capacity Demand and Rates Flat View ).

Each field that you assign to the profile is displayed as a column in the capacity demand and rates flat view (flat

view). You can specify the relative position of a field, which is then used to display information in the flat view.

Allow fields to be displayed as search criteria for the flat view.

Allow additional related fields to be displayed in the flat view. The following is an example of additional related fields.

  Example

If you select Source Location as a field, and select the checkbox to show related fields, some of the related fields

that are displayed in the flat view are as follows: Source Location City, Source Location Country/Region,

Source Location Zip Code etc.

Pivot the flat view on a particular field by selecting a field to be a pivot column. This option transposes the existing

data of the selected field from several rows to one row by adding new columns to the flat view.

Capacity Demand and Rates Flat View (Flat View)

The flat view is a consolidated view of all the charge items and rate tables that are relevant for negotiating freight

agreement RFQs. The flat view displays information using the capacity demand and rates profile that you have assigned to

an RFQ item. The following example explains what information is displayed in the flat view:

  Example

The following table displays a calculation sheet in a freight agreement RFQ that is under negotiation:

## Item

Line No.

Instruction

Charge

Amount

Currency

Rate Table

Target

Target

Hierarchy

Type

Type

Amount

Currency

Basic rate

10

Standard

FB00

Loading

Charges

## Base

Charges

20

30

Standard

TM7-LOAD

Standard

TM7-BASE

18859

18860

EUR

EUR

EUR

EUR

EUR

EUR

This is custom documentation. For more information, please visit SAP Help Portal.

42


1/14/26, 2:41 PM

The following table displays the scales that are configured for the rate table 18859:

Scale Dimension

Calculation Base

Calculation Base

## Scale Type

Scale Unit of Measure

01

02

03

Description

## SOURCELOC

Source Location

Same Scale (=)

## DESTLOC

Destination Location

Same Scale (=)

QUANTITY_VAL

## Quantity

To Scale (<=)

PAL

The following table displays the scales that are configured for the rate table 18860:

Scale Dimension

Calculation Base

Calculation Base

## Scale Type

Scale Unit of Measure

Description

01

02

## SOURCELOC

Source Location

Same Scale (=)

EQUIP_TYPE

Equipment Type

Same Scale (=)

If you use capacity demand and rates, the flat view displays the following fields:

## Source

Destination

Equipment

Quantity

## Basic

Location

Location

Type (=)

(=)

(=)

(PAL)

(<=)

rate –

Target

Rate

(EUR

per 1

PAL)

Basic

rate –

Loading

Loading

Base

## Base

charges

charges

Charges

Charges

Tolerance

– Target

–

– Target

–

(%)

Rate

(EUR)

Tolerance

Amount

Tolerance

(%)

(EUR)

(%)

  Note

When using capacity demand and rates, the Calculation Sheet Overview tab is not visible.

## Search Criteria

Apply search criteria to the flat view to view only specific records. You can also limit the number of records to be retrieved

and displayed in the flat view. In the capacity demand and rates profile, you can select the fields to be displayed as search

criteria on the flat view.

## File Download and Upload

Download the capacity demand and rates records as a spreadsheet, which you can then use to update. You can choose to

download the records with or without applying the search criteria.

You can upload a spreadsheet to update the capacity demand and rates. For example, the spreadsheet can contain your

updated lanes, break-weights, target rates, and target amounts for flat charges.

  Note

For information about carrier spreadsheet formats, see Responses from Carriers Using Spreadsheets.

## Capacity Demand and Rates Flat View for Carriers

This is custom documentation. For more information, please visit SAP Help Portal.

43


1/14/26, 2:41 PM

Enable your carriers to use the flat view to submit their responses to freight agreement RFQs. Select the flat view format

under Carrier Settings in the freight agreement RFQ type that you have defined in Customizing for Transportation

Management under  Master Data

 Agreement RFQs and Quotations

 Define Freight Agreement RFQ Types .

Capacity Demand and Rates in Freight Agreement RFQs Created from Freight Agreements

Use capacity demand and rates in a freight agreement RFQ created from a freight agreement. The system determines the

capacity demand and rates profile based on the calculation sheet in the freight agreement items. If the system could not

determine a capacity demand and rates profile, you can manually add the profile in the freight agreement RFQ.

## Evaluations and Awarding

Allows you as a shipper to work with a single user interface (UI) for evaluating and awarding capacities to carriers or logistics

service providers.

## Prerequisites

You have defined a capacity demand and rates profile in Customizing for Transportation Management under  Master

## Data

 Agreement RFQs and Quotations

 Define Capacity Demand and Rates Profiles .

You have selected Dimensions or RFQ Item for the award level in the capacity demand and rates profile.

If you have selected Dimensions as the award level, in Assign Fields and Configure Properties, you have also selected the

capacity dimensions as the award level dimensions.

Carriers or logistics service providers have responded to your request for quotations.

## Features

## Capacity Demand and Rates Flat View for Evaluations

After you publish a freight agreement RFQ master, the flat view displays the individual responses from your carriers. You

can use this information to evaluate the responses by comparing offered rates, offered capacities, and offered transit times.

You can apply search criteria to evaluate specific records. You can also download and view the records as a spreadsheet.

## Evaluations

The evaluations UI is displayed after you publish the freight agreement RFQ master. You can use this UI to insert or edit

simulations to view and evaluate target share strategies based on the responses received from the carriers.

You can use simulations to evaluate using the optimizer or perform a manual evaluation.

In an optimizer-based evaluation, the simulation uses the optimizer to allocate the target shares based on the target

share strategy that you have defined in Customizing for Transport Management under  Master Data

## Agreement

## RFQs and Quotations

 Define Target Share Strategies .

In the simulation, you can specify an optimizer strategy and the conditions to use when comparing carrier

responses.

In a manual evaluation, you must manually allocate the target shares to carriers based on the award level

dimensions or at the RFQ Item level.

You can use a spreadsheet to award the carriers based on percentages or capacities on the award level dimensions.

## Simulation Estimated Spends and Awarding

This is custom documentation. For more information, please visit SAP Help Portal.

44


1/14/26, 2:41 PM

Simulate the estimated spend to view the estimated spends based on offered capacity, requested capacity, and

missing capacity.

Missing capacity represents the capacity that was not committed by a carrier.

Insert multiple simulations and compare the responses from carriers based on estimated spends.

Set one of the simulations to be your preferred simulation. This simulation represents your preferred target share

allocations to carriers.

Accept the preferred strategy for a freight agreement RFQ item for awarding.

  Note
When using capacity demand and rates, the comparison cockpit is not available. You can use the evaluations and

awarding feature of capacity demand and rates to compare carrier responses.

## Reverse Auction

Allows you as a shipper to enable carriers to revise their bids and view the current best rates for the lanes.

## Prerequisites

You've defined the following in the Customizing for Transportation Management, under  Master Data

 Agreement RFQs and

Quotations :

## You've selected Advanced RFQs

You've selected Enable Capacity Demand and Rates

## You've selected Enable Reverse Auction

(Optional) You've selected Allow Carriers to Increase their Bids if you want to enable your carrier to quote higher than the

previous bid. You can select this checkbox, only if you've selected Enable Reverse Auction for the RFQ

## Features

As a shipper, you can:

## Allow your logistic service providers to revise their bids

View the current best rates by your logistics service providers on the user interface as well as spreadsheets

Logistics service providers (LSPs) can:

View the current best rates available for any given lane

Revise their bids that could be higher or lower

  Note

LSPs can submit higher bids only if the shipper has enabled the following:

In the Customizing for Transportation Management, under  Master Data

 Agreement RFQs and

## Quotations

Allow Carriers to Increase their Bids

## By default, LSPs can submit only lower bids

This is custom documentation. For more information, please visit SAP Help Portal.

45


1/14/26, 2:41 PM

Submit bids multiple times until the response deadline is or the negotiation is completed or cancelled

Use spreadsheets to upload latest bids for resubmission

Related Information

Capacity Demand and Rates

Strategic Freight Sales

## Use

Strategic freight sales helps you as a carrier or logistics service provider (LSP) to determine the best rates you can provide to

transport items between specific locations (trade lanes) and then to agree a contract (agreement) with shippers or other LSPs.

Transportation Management (TM) supplies the tools you need to receive requests for rate quotations, evaluate your responses,

and also proactively send your rates to shippers or other LSPs.

This feature enables you to quickly and conveniently determine the prices you can provide for various services based on the prices

you have quoted previously. This gives you higher productivity and better decision making.

## Process

1. You create a forwarding agreement (FWA) quotation

A shipper or LSP can communicate requests for you to provide rates to transport specific items as follows:

Business-to-business (B2B)

In a freight agreement RFQ master, a shipper or LSP that uses TM can specify transportation items along with

attributes such as transportation mode and service type. Subsequently, the shipper or LSP sends the freight

agreement RFQ master to you using business-to-business communication. For more information, see Freight

Agreement Processing. The system displays the freight agreement RFQ as a forwarding agreement quotation in

your worklist. You can see the worklist in the Forwarding Agreements app on the fiori launchpad. For more

information, see Strategic Freight Procurement.

## E-mail

A shipper or LSP uses e-mail to send you all the details of a request. Details can include information such as, items,

rate tables, local rate tables, calculation sheets, local calculation sheets, transportation modes, and service levels.

You perform the following actions to use this information in a forwarding agreement quotation:

a. Download a new forwarding agreement quotation as a spreadsheet file. For more information, see

## Forwarding Agreement Quotation

b. Enter the information the shipper or LSP has sent in to the spreadsheet.

c. Upload the spreadsheet in the forwarding agreement quotation. For more information, see Forwarding

Agreement Quotation.

The system automatically fills all the fields in the forwarding agreement quotation according to the details specified

in the spreadsheet. Subsequently, you enter rates for the various transportation items and download the details of

the forwarding agreement quotation in another spreadsheet in the Excel Integration tab page of the forwarding

agreement quotation. You can then send this spreadsheet file to the shipper or LSP.

If a shipper or LSP sends you a spreadsheet file with the request details in the format of a downloaded Microsoft

Excel file, you can directly upload the file in the Excel Integration tab page of a new forwarding agreement quotation.

This is custom documentation. For more information, please visit SAP Help Portal.

46


1/14/26, 2:41 PM

  Note

You can also change an existing forwarding agreement quotation using a Microsoft Excel file. You upload the

Microsoft Excel file in the Excel Integration tab page of the forwarding agreement quotation. The system updates

the information in the forwarding agreement quotation.

## Microsoft Excel

For more information, see Creation of FWA Quotation from Non-TM Formatted Excel

A shipper or LSP can contact you with a request for rates for items by email, telephone, and so on. You can create a

forwarding agreement quotation and enter the items the shipper or LSP has specified. For more information, see

## Forwarding Agreement Quotation

To proactively send rates for items to shippers and LSPs, you can create a forwarding agreement quotation from any of the

following documents or the document items:

## Service product catalogs

You can open a service product catalog and select the service products from which you create a forwarding

agreement quotation. For more information on service product catalogs, see Service Product Catalogs.

## Forwarding agreements

You can open a forwarding agreement and select the agreement items you want to offer to shippers or LSP.

Subsequently, you can create a forwarding agreement quotation from these items. For more information on

forwarding agreements, see Forwarding Agreement Maintenance.

## Forwarding agreement quotation template

## Opportunity in an SAP Customer Relationship Management (CRM) system

You can use the service products you define from the TM system in an Opportunity business document in the SAP

CRM system. Subsequently, you can create a forwarding agreement quotation to send rates for these service

products.

  Note

After you have created the forwarding agreement quotation, you can create forwarding agreement quotation

assignments. You create forwarding agreement quotation assignments to delegate the task of rate specification for

transportation services for a particular trade to analysts who has expertise in providing rates for the trade lane. The

analysts perform step 2 and step 3 and proposes rates. Subsequently, the analysts merge the rates back to the

forwarding agreement quotation. For more information, see Forwarding Agreement Quotation Assignment.

2. You specify the rate for each forwarding agreement quotation item

For more information, see Rate Determination for Forwarding Agreement Quotation Items

3. You request for approval of rate from the approver

You can enter a rate proposal for an item in the item or in a response to the item. You send the item or response to your

approver for approval. The approver receives the request for approval in the workflow inbox. The approver can decide

whether to accept or reject your rate proposal in the response or item. If the approver accepts the proposal for a response,

the system automatically copies the rates you have proposed in the response to the calculation sheet (both kinds, including

local) in the quotation item and the status of the response and quotation item changes to Approved. Note that the system

does not copy all the rates but only the relevant rates for similar dimensions in the quotation item. If the approver accepts

the rate in the item, the system changes the status of the item to Approved. If the approver rejects the rate proposal in the

response or item, the status of the response or item changes to rejected. You can subsequently change the rate proposal

and send it to the approver again.

This is custom documentation. For more information, please visit SAP Help Portal.

47


1/14/26, 2:41 PM

  Note

You must select the checkbox Publication Workflow in Customizing for Transportation Management under  Master

## Data

## Agreement RFQs and Quotations

 Define Forwarding Agreement Quotation Types  to enable the approver to

receive the quotation items for approval. If you do not select this checkbox, you must manually set the status of the

forwarding agreement quotation item to Approved before you can send the rate proposal to the shipper or LSP.

4. You send the forwarding agreement quotation to a shipper or an LSP

After the status of a forwarding agreement quotation changes to Approved, you can send the quotation to the shipper or

LSP. The system includes the rates you have proposed in the quotation.

You choose the Submit button to send the forwarding agreement quotation to the shipper or LSP. You can send the

forwarding agreement quotation using business-to-business communication. For more information, see Forwarding

Agreement Processing. The forwarding agreement quotation is sent through the B2B (business to business)

communication. The status of the forwarding agreement quotation changes to Submitted. You can also download the

FWAQ as a Microsoft Excel file and send it as an email attachment.

If the shipper or LSP accepts your quotation item, you can create a forwarding agreement from the quotation item.

However, if the shipper or LSP wants to renegotiate the prices or wants additional services, the system increments the

customer negotiation cycle by one or creates a new version of the document with the changes the shipper or LSP has

requested. Subsequently, you repeat the process from step 2 and propose new rates.

  Note

If you want to create a new version of the forwarding agreement quotation when a shipper or LSP wants to renegotiate

the prices or wants additional services, you must select the select the checkbox Create New Version in Customizing for

Transportation Management under  Master Data

 Agreement RFQs and Quotations

## Define Forwarding Agreement

Quotation Types . The system creates the new version with the changes the shipper or LSP has requested. If you do

not select this checkbox, the system increments the customer negotiation cycle by one.

When you use B2B communication to send the forwarding agreement quotation, the system creates a freight agreement

RFQ in the TM system of the shipper or LSP.

5. You create a forwarding agreement

When the shipper or LSP awards you with a quotation item, you can create a new forwarding agreement or update an

existing forwarding agreement for the shipper or LSP.

Once one or more of the items have been awarded by the shipper or LSP, you can select the items and create or update a

forwarding agreement with the shipper or LSP.

  Note

The forwarding agreement can also be sent to the shipper through B2B. The system creates a freight agreement in the

TM system of the shipper.

Forwarding Agreement Quotation

## Definition

A forwarding agreement quotation is an individual business document that you as a carrier or logistics service provider (LSP)

proactively send to a shipper or another LSP to bid for the provision of future transportation services in a trade lane for a defined

period of time.

This is custom documentation. For more information, please visit SAP Help Portal.

48


1/14/26, 2:41 PM

You can also use a forwarding agreement quotation to respond to a request for a quotation from a shipper or an LSP with your

rates for transportation services. For more information, see Strategic Freight Sales.

You can create, edit, or display forwarding agreement quotations in the Create Forwarding Agreement Quotation or Edit

Forwarding Agreement Quotation app on the fiori launchpad.

  Note

You must define forwarding agreement quotation types before you create a forwarding agreement quotation. You can

create forwarding agreement quotation types in Customizing for Transportation Management under  Master Data

## Agreement RFQs and Quotations

 Define Forwarding Agreement Quotation Types .

You can use a forwarding agreement quotation template to create a forwarding agreement quotation. You can create,

edit, or display forwarding agreement quotation templates in the Forwarding Agreement Quotation Template app on

the fiori launchpad.

## Use

In a forwarding agreement quotation, you can perform the following actions on a forwarding agreement quotation item:

## Business context viewer

You can review the transportation history of shippers and logistics service providers (LSPs) to which you send rate

proposals for forwarding agreement quotation items. For more information, see Customer Analysis.

Build a rate proposal for an item and response, manually or automatically

For more information, see Rate Determination for Forwarding Agreement Quotation Items.

## Create a forwarding agreement quotation assignment

A sales manager can create an FWAQ assignment from a forwarding agreement quotation. The manager creates the FWAQ

assignment to delegate the task of rate specification for transportation services for a particular trade to an analyst who has

expertise in providing rates for the trade lane. For more information, see Forwarding Agreement Quotation Assignment

## Display as flat view

You can view the entire forwarding agreement quotation (FWAQ) or an FWAQ item in one screen. This enables you to make

quick and efficient decisions about rates based on logistical information. For more information, see Flat View.

## Send item for approval

After you’ve decided the rates for a particular item or response, you send the item for approval to your approver. For more

information, see Strategic Freight Sales

## Estimate forwarding charges

You can estimate forwarding charges for a forwarding agreement quotation item. The sales organization, sold-to party,

movement type, traffic direction, transportation mode, and shipping type are copied from the forwarding agreement

quotation to the estimate forwarding charges application. When you calculate charges, the system uses the forwarding

agreement quotation item as an agreement item. It also uses the calculation sheet (both kinds, including local) and the

rates of the forwarding agreement quotation item to calculate the charges.

## Display duplicate documents

The system checks and displays other business documents with matching attributes when you save or check the business

document.

This is custom documentation. For more information, please visit SAP Help Portal.

49


1/14/26, 2:41 PM
## Structure

A forwarding agreement quotation can contain the following main tab pages and screen areas:

## General Data

The General Data tab page contains high-level information about the transportation services the shipper or LSP wants you

to bid for, for example:

Organizational unit responsible

## Validity period

Your details, including whether the shipper or LSP already has an agreement in place with you for the trade lane

forwarding agreement quotation type

## Customer negotiation cycle

Deadline for responding to the shipper or LSP

## Items

The Items screen area contains information about the quotation items. This screen area can contain the following tab

pages, when relevant:

## Calculation Sheet Overview

This tab page displays the calculation sheet (both kinds, including local) details for each quotation item.

## Trade Lanes

This tab page displays the details about the trade lanes for each quotation item.

## Details

On this tab page, you can specify the details of the payment terms and general terms. Note that when you create an

agreement from the forwarding agreement quotation, the system copies the information you specify here to the

details tab page of the agreement.

## Capacities

This tab page contains the capacity required from you, the carrier or logistics service provider, the capacity you can

commit to, and the capacity awarded to you.

## Commodity Codes

This tab page displays the commodity codes for each quotation item.

## Notes

This tab page displays any notes relevant to the quotation item.

## Attachments

On this tab page, you can upload files relevant to the quotation item.

## Default Route

On this tab page, you can use default routes to specify the sequence of locations that the system uses if there’s no

direct connection between your locations. If there’s a direct connection between your locations, you can specify a

default route to predefine entries for the organization interaction status, transportation mode, and so on.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

50


1/14/26, 2:41 PM

In the forwarding agreement quotation item, you can also specify an Opportunity business document and the

corresponding item that exists in an SAP Customer Relationship Management system. This enables you to access the

CRM opportunity from the forwarding agreement quotation item. This increases your response time and reduces

workload.

## Business Partner

The Business Partner tab page displays the business partners associated with the business document. For example, a bill-

to party and sold-to party.

  Note

You can display the business partner hierarchy in the business partner tab page.

In a forwarding agreement quotation, it displays all the business partners associated with the sold-to party.

You can restrict the partner functions available in the business partner tab page. For more information, see

Business Partner Determination.

You can specify additional partner functions, such as notify party and communication party, for information

purposes in addition to primary partner functions, such as sold-to party.

The information on this tab page isn’t considered when you create an agreement from the forwarding agreement

quotation.

## Output Management

On the Output Management tab page, you can print forwarding agreement quotation details and generate e-mails and

faxes and send them directly to the intended recipient. You can also see a record of the documents that were already

printed or sent (by e-mail or fax, for example). For more information, see Output Management.

## Notes

On this tab page, you can add any relevant notes.

## Attachments

On this tab page, you can upload relevant files.

## Change Documents

You can view all changes made to a forwarding agreement quotation on the Change Documents tab page or screen area.

The changes are listed by date and time. You view the details of the changes at header level by selecting the relevant row in

the Transactions screen area and at field level by selecting the relevant row in the Record Level Changes screen area. You

must refresh the forwarding agreement quotation to view recently saved changes.

  Note

You can activate the Change Documents tab page or screen area in Customizing for Transportation Management

under  Master Data

## Agreement RFQs and Quotations

 Define Forwarding Agreement Quotation Types .

## Document Flow

You can view the business documents from which the forwarding agreement quotation was created and the business

documents created from the forwarding agreement quotation.

## Excel Integration

You can use a Microsoft Excel file to update details when you create a new forwarding agreement quotation or when you

edit an existing forwarding agreement quotation. You can perform the following actions:

This is custom documentation. For more information, please visit SAP Help Portal.

51


1/14/26, 2:41 PM

Download the forwarding agreement quotation as a Microsoft Excel file

Update the Microsoft Excel file that you download with the shipper's or LSP's requirements

## Upload the Microsoft Excel file in the Excel Integration tab page

The system uses the information in the uploaded Microsoft Excel file to automatically enter information in the

relevant fields in the quotation. You can then propose rates for various items in the forwarding agreement quotation.

You can also perform the following activities:

## Download the forwarding agreement quotation as a customer excel

If you’ve created the forwarding agreement quotation from a Microsoft Excel provided by a customer, you can

download the forwarding agreement quotation in the same format of the customer's Microsoft Excel file. For more

information on creating a forwarding agreement quotation from a customer's Microsoft Excel file, see Creation of

## FWA Quotation from Non-TM Formatted Excel

Download all items, all item responses, or all items and item responses in the forwarding agreement quotation as a

Microsoft Excel file

  Note

You specify the fields of forwarding agreement quotations that you want another LSP or a shipper to be able to edit in

Microsoft Excel in Customizing for Transportation Management under  Master Data

 Agreement RFQs and

## Quotations

## Define Editable Fields in Excel

. Note that this Customizing isn’t taken into account if you download the

forwarding agreement quotation as a customer excel.

## Versions

The Versions tab page contains a list of the FWAQ versions, including the status of each version.

## Capacities

This tab page contains the total capacity required from you, the carrier or logistics service provider, the total capacity you

can commit to, and the total capacity awarded to you.

  Note

You can activate the Capacities tab page or screen area in Customizing for Transportation Management under

## Master Data

## Agreement RFQs and Quotations

 Define Forwarding Agreement Quotation Types .

## More Information

Freight Agreement RFQ Master

## Agreement

## Strategic Freight Sales

For more information about SAP CRM opportunities, see SAP Library on SAP Help Portal at http://help.sap.com/crm . Choose a

release and under Application Help, choose  SAP Customer Relationship Management

## Sales

## Opportunity Management

 Integration with SAP Transportation Management

.

Forwarding Agreement Quotation Assignment

## Definition

This is custom documentation. For more information, please visit SAP Help Portal.

52


1/14/26, 2:41 PM

A forwarding agreement quotation (FWAQ) assignment is a business document that you as an analyst of a carrier or logistics

service provider (LSP) use to propose rates for transportation services.

A sales manager can create an FWAQ assignment from a forwarding agreement quotation item. The manager creates the FWAQ

assignment to delegate the task of rate specification for transportation services for a particular trade to an analyst who has

expertise in providing rates for the trade lane.

You, as an analyst, can also create an FWAQ assignment and use the items that are relevant to you from various FWAQs and

propose rates for the transportation services. For example, you have expertise in providing rates between Asia and Europe. You can

create a forwarding agreement quotation assignment and use items from various FWAQs that have routes between these locations

to provide rates for transportation services.

For every item in the FWAQ assignment, the system displays the FWAQ from which the item is used.

You can create, edit, and display FWAQ assignments in the Forwarding Agreement Quotation Assignment app in the fiori

launchpad.

## Use

In an FWAQ assignment, you can perform the following actions on an FWAQ assignment item:

## Business context viewer

You can review the transportation history of shippers and logistics service providers (LSPs) to which you send rate

proposals for forwarding agreement quotation items. For more information, see Customer Analysis.

Build a rate proposal for an item and response, manually or automatically

For more information, see Rate Determination for Forwarding Agreement Quotation Items.

## Display as a flat view

You can view the entire forwarding agreement quotation assignment (FWAQ) or an FWAQ assignment item in one screen.

This enables you to make quick and efficient decisions about rates based on logistical information. For more information,

see Flat View.

## Estimate forwarding charges

You can estimate forwarding charges for an FWAQ assignment item. The sales organization, sold-to party, movement type,

traffic direction, transportation mode, and shipping type are copied from the FWAQ assignment to the estimate forwarding

charges application. When you calculate charges, the system uses the forwarding agreement quotation assignment item as

an agreement item. It also uses the calculation sheet (both kinds, including local) and the rates of the forwarding

agreement quotation assignment item to calculate the charges.

## Send item for approval

After you’ve decided the rates for a particular item or response, you send the item for approval to your approver. For more

information, see Strategic Freight Sales.

## Merge items

After you’ve proposed the rates, you can merge the rates back into the FWAQ item. Note that the rates for the items must

be approved before you can merge the rates into the FWAQ item.

## Display duplicate documents

The system checks and displays other business documents with matching attributes when you save or check the business

document.

This is custom documentation. For more information, please visit SAP Help Portal.

53


1/14/26, 2:41 PM
## Structure

A forwarding agreement quotation assignment can contain the following main tab pages and screen areas:

## General Data

The General Data tab page contains high-level information about the transportation services the shipper or LSP wants you

to bid for, for example:

Organizational unit responsible

Validity period

## FWAQ type

## Customer negotiation cycle

Deadline for responding to the shipper or LSP

Business partner hierarchy

## Items

The Items screen area contains information about the FWAQ assignment items. This screen area can contain the following

tab pages, when relevant:

## Calculation Sheet Overview

This tab page displays the calculation sheet (both kinds, including local) details for each FWAQ assignment item.

## Trade Lanes

This tab page displays the details about the trade lanes for each FWAQ assignment item.

## Capacities

This tab page contains the capacity required from you, the carrier or logistics service provider, the capacity you can

commit to, and the capacity awarded to you.

## Commodity Codes

This tab page displays the commodity codes for each FWAQ assignment item.

## Notes

This tab page displays any notes relevant to the FWAQ assignment item.

## Attachments

On this tab page, you can upload files relevant to the FWAQ assignment item.

## Default Route

On this tab page, you can use default routes to specify the sequence of locations that the system uses if there’s no

direct connection between your locations. If there’s a direct connection between your locations, you can specify a

default route to predefine entries for the organization interaction status, transportation mode, and so on.

## Business Partner

The Business Partner tab page displays the business partners associated with the business document. For example, a bill-

to party and sold-to party.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

54


1/14/26, 2:41 PM

You can display the business partner hierarchy in the business partner tab page.

In an FWAQ assignment, it displays all the business partners associated with the sold-to party.

You can restrict the partner functions available in the business partner tab page. For more information, see

Business Partner Determination.

You can specify additional partner functions, such as notify party and communication party, for information

purposes in addition to primary partner functions, such as sold-to party.

## Output Management

On the Output Management tab page, you can print the FWAQ assignment details and generate e-mails and faxes and send

them directly to the intended recipient. You can also see a record of the documents that were already printed or sent (by e-

mail or fax, for example). For more information, see Output Management.

## Notes

On this tab page, you can add any relevant notes.

## Attachments

On this tab page, you can upload relevant files.

## Change Documents

You can view all changes made to an FWAQ assignment on the Change Documents tab page or screen area. The changes

are listed by date and time. You view the details of the changes at header level by selecting the relevant row in the

Transactions screen area and at field level by selecting the relevant row in the Record Level Changes screen area. You must

refresh the FWAQ assignment to view recently saved changes.

  Note

You can activate the Change Documents tab page or screen area in Customizing for Transportation Management

under  Master Data

## Agreement RFQs and Quotations

 Define Forwarding Agreement Quotation Types .

## Excel Integration

You can use a spreadsheet to update details when you create a new FWAQ assignment or when you edit an existing FWAQ

assignment. You can perform the following actions:

## Download the FWAQ assignment to a spreadsheet

Update the spreadsheet that you download with the shipper's or LSP's requirements

## Upload the spreadsheet in the Excel Integration tab page

The system uses the information in the uploaded spreadsheet to automatically enter information in the relevant

fields in the FWAQ assignment. You can then propose rates for various items in the FWAQ assignment.

You can also download all items, all item responses, or all items and item responses in the forwarding agreement quotation

to a spreadsheet

  Note

You specify the fields of an FWAQ assignment that you want another LSP or a shipper to be able to edit in a spreadsheet

in Customizing for Transportation Management under  Master Data

 Agreement RFQs and Quotations

## Define

Editable Fields in Excel

.

## Capacities

This is custom documentation. For more information, please visit SAP Help Portal.

55


1/14/26, 2:41 PM

This tab page contains the total capacity required from you, the carrier or logistics service provider, the total capacity you

can commit to, and the total capacity awarded to you.

  Note
You can activate the Capacities tab page or screen area in Customizing for Transportation Management under

## Master Data

## Agreement RFQs and Quotations

 Define Forwarding Agreement Quotation Types .

## More Information

Forwarding Agreement Quotation

Freight Agreement RFQ Master

## Agreement

Strategic Freight Sales

Customer Analysis

## Use

You can use this feature to review the transportation history of shippers and logistics service providers (LSPs) to which you send

rate proposals for forwarding agreement quotation items.

## Prerequisites

You have performed the following tasks:

Integrated Transportation Management (TM) with SAP NetWeaver Business Warehouse (SAP NetWeaver BW) BI CONTENT

747 – SP07. The system uses the analyzed data in SAP NetWeaver BW to display the carriers' performance in the BCV.

Implemented SAP note 1715521

.

Activated the business configuration set /SCMTMS/BCV_CUSTOMER_ANALYSIS.

## Features

The system displays the following customer analysis information:

## Revenue per year

Displays the total revenue earned from a shipper or an LSP over a period of time in a graph. This enables you to determine

the impact the customer has on your business profits.

You can also review the revenue per quarter. This enables you to check if the revenue you generated was uniform over a

particular year.

## Demand per year

Displays the total load that you carried for a customer over a period of time in a graph. This enables you to determine

whether a customer is inflating demand in the request.

This is custom documentation. For more information, please visit SAP Help Portal.

56


1/14/26, 2:41 PM

You can also review the demand per quarter. This enables you to check if the load you delivered was uniform over a

particular year or if the load increased or decreased during certain periods.

Note that you can also enter the sales organization so that the system displays analytics that is specific to the transportation

history of the agreements between the sold-to party and sales organizations. You can also analyze data for the shipper or LSP

based on trade lanes. This enables you to truncate your analysis over a trade lane.

## More Information

Forwarding Agreement Quotation

Strategic Freight Sales

Flat View

## Use

As a logistic service provider or carrier, you can view the entire forwarding agreement quotation (FWAQ) or an FWAQ item in one

screen. This enables you to see a broader view of the FWAQ to make quick and efficient decisions about rates based on logistical

information.

You can display the flat view of an FWAQ or an FWAQ item when you open an FWAQ in the Edit Forwarding Agreement Quotation

app on the SAP Fiori launchpad.

## Prerequisites

You’ve performed the following activities:

Defined a flat view profile in Customizing for Transportation Management under  Master Data

 Agreement RFQs and

## Quotations

 Define Excel and Flat View Profiles

## Define Flat View Profiles for FWAQs

Assigned the flat view profile to an FWAQ type in Customizing for Transportation Management under  Master Data

 Agreement RFQs and Quotations

## Define Forwarding Agreement Quotation Types

When you display the flat view from an FWAQ of this FWAQ type, the system uses the flat view profile to display a flat view of the

FWAQ or the FWAQ item.

## Features

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

You can perform the following activities:

## Change rates

For the same charge type across items, you can simultaneously update the rates for a particular scale or for all scales. For

example, you can increase the rates for basic freight with the charge type of FB00 by 20% with source location Bangalore

and destination location Hamburg.

Margin and target margin

The system displays the following:

This is custom documentation. For more information, please visit SAP Help Portal.

57


1/14/26, 2:41 PM

The rate obtained by the system by subtracting the rate in the cost charge types from the total rate in all the non-

cost charge types as the margin

The rate obtained by the system by subtracting the rate in the cost charge types from the total target rate in all the

non-cost charge types as the target margin

  Note

You can select the Cost checkbox only if you’ve selected the Statistical Charge checkbox. You can perform these

activities on the Classification tab page of a charge type when you edit a calculation sheet.

## Business context viewer

You can review the transportation history of shippers and logistics service providers (LSPs) to which you send rate

proposals for forwarding agreement quotation items. For more information, see Customer Analysis.

## Update repeated rates

A repeated rate is the rate for the same logistical combination that is displayed multiple times in flat view. The system

automatically updates all the rows of a charge type that have repeated rates when you update one of the rate rows.

  Example

A forwarding agreement quotation item contains two charge types with the following rate tables:

FB00 with the rate table values:

## Source Location

Destination Location Rate

Berlin

Chicago

10

BAF with the rate table values:

## Source Location

Destination Location Gross Weight

Rate

Berlin

Berlin

Chicago

Chicago

100

200

10

30

When you display the item as a flat view, the system displays the two charge types as follows:

## Source Location

Destination Location Gross Weight

FB00

Berlin

Berlin

Chicago

Chicago

100

200

10

10

BAF

20

30

If you change the rate of FB00 from 10 to 5 in one row, the system automatically updates all the rows of the charge type

with the same rate for the same logistical combination if you’ve enabled the repeated rates feature.

## Source Location

Destination Location Gross Weight

FB00

Berlin

Chicago

100

5

BAF

20

This is custom documentation. For more information, please visit SAP Help Portal.

58


1/14/26, 2:41 PM

## Source Location

Destination Location Gross Weight

FB00

Berlin

Chicago

200

5

BAF

30

## Copy or delete a row

You can use the Copy button to copy an existing row and the Delete button to delete an existing row.

## Mass update

You can use the Mass Update button to update all the rates displayed in the table.

## Download as a spreadsheet

You can download the visible columns and rows in the flat view of an FWAQ to a spreadsheet file.

## Filter data based on specific attributes

You can filter data based on criteria you specify. For example, simulation date enables you to view the rates for a particular

date. In the rate table, the system finds the validity period in which this date exists and displays the rate for the validity

period.

## Display trade lane, commodity code, and default route for a row

You select a row. The rates in the row are present in a particular item. The system displays the trade lane, commodity code,

and default route of the item.

## Change and save the view

You can edit the manner in which the system displays the flat view and can also save this view for later use.

## Filter based on values

You can filter the values in the flat view based on specific values of columns and hide the rest of the data. For example, you

can display the rates that have values for an equipment type of 20G.

  Note

The number of characters for the value of a field name can’t exceed 29 characters if the orientation is By Column.

Instead, you can specify an orientation of By Row to accommodate more than 29 characters.

The system doesn’t display the calculation rule in the flat view.

## Example

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

An FWAQ with an FWAQ type FLAT_QT contains an item with charge types with the following rate tables:

Charge type FB00 with the rate table values:

Source Location

Destination

## Commodity

Equipment Type

## Rate

Target Rate

Location

Berlin

Chicago

FAK1

20G

100

90

This is custom documentation. For more information, please visit SAP Help Portal.

59


1/14/26, 2:41 PM

Source Location

Destination

## Commodity

Equipment Type

## Rate

Target Rate

Berlin

Berlin

Berlin

Location

Chicago

Chicago

Chicago

FAK1

FAK2

FAK2

40G

20G

40G

110

200

210

100

190

200

Charge type BAF with the rate table values:

Source Location

Destination Location

Equipment Type

## Rate

Target Rate

Berlin

Berlin

Chicago

Chicago

20G

40G

50

40

40

30

Cost Charge type FB01 with the rate table values:

## Source Location

Destination Location Commodity

Equipment Type

Rate

Berlin

Berlin

Berlin

Berlin

Chicago

Chicago

Chicago

Chicago

FAK1

FAK1

FAK2

FAK2

20G

40G

20G

40G

20

20

20

20

In the Customizing activity Define Flat View Profiles for FWAQs, you’ve specified the following settings for a flat view profile

FLAT_DEM.

Document Hierarchy Level

Field Name

Orientation

Sequence Number

Calculation Sheet

TCET084

By Column

Scale

Scale

Scale

Scale

## Scale

SOURCELOC

DESTLOC

By Row

## By Row

COMMODITY_CODE

## By Row

EQUIP_TYPE

TARGET_RATE

By Row

By Row

1

2

3

4

You’ve also assigned the flat view profile to the forwarding agreement quotation type FLAT_QT

When you display the FWAQ item as a flat view in the FWAQ, the system displays the following view of the item:

## Source

Destination

Commodity

Equipment

FB00

Location

Location

Code

Type

Target

Rate

FB00

BAF

Target

FB01

Margin

Rate

BAF

Target

Margin

Berlin

Chicago

FAK1

20G

100

90

50

40

20

130

110

This is custom documentation. For more information, please visit SAP Help Portal.

60


1/14/26, 2:41 PM

## Source

Destination

Commodity

Equipment

FB00

Target

BAF

Target

FB01

Margin

Target

Location

Location

Code

Type

Berlin

Chicago

FAK1

Berlin

Chicago

FAK2

Berlin

Chicago

FAK2

40G

20G

40G

110

200

210

Rate

FB00

100

190

200

40

50

40

Rate

BAF

30

40

30

20

20

20

130

230

230

Margin

110

210

210

Note that the target margin is the sum of the target rates in all the non-cost charge types after subtracting the rate in the cost

charge type.

You can also change the values of the rates and save the FWAQ.

## More Information

## Forwarding Agreement Quotation

Rate Determination of Forwarding Agreement Quotation Items

## Use

The system enables you to easily and efficiently determine the rates you want to provide to shippers or logistics service provides

(LSPs) for forwarding agreement quotation (FWAQ) items based on the existing service products. Note that you can also use this

feature in a forwarding agreement quotation assignment for the forwarding agreement quotation assignment items.

## Prerequisites

In the forwarding agreement quotation, you’ve selected a leading charge type in the calculation sheet (both kinds, including

local) of an item. This enables the system to easily find service products based on the information, such as location pairs, in

the rate table (both kinds, including local) of the leading charge type. Subsequently, the system tries to find matching rate

records of the leading charge type in the rate records of the charge type in the service products.

  Recommendation
We recommend that you choose a charge type that contains the source locations and destination locations as the leading

charge type. This enables the system to find matching service products with the similar source locations and destination

locations in the rate records of the charge type in the service product. This enables the system to match the most optimum

rates.

We recommend that you select only one charge type as the leading charge type. This enables the system to find matching

service products quickly.

## Features

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

## Automatically Build Rate

This is custom documentation. For more information, please visit SAP Help Portal.

61


1/14/26, 2:41 PM

In the forwarding agreement quotation item, you can choose one or more items and automatically build rate. The system performs

the following activities for each item:

1. Tries to find service products with the attributes as the rate table in the leading charge type

2. If it finds matching service products, the system tries to find matching rate records of the leading charge type in the rate

records of the charge type in the service product

3. If it finds matching rate records, the system creates a forwarding agreement quotation item response in the item

The forwarding agreement quotation item response contains not only the matching charge type and matching rate record,

but all the charge types with a matching rate record.

The system creates separate forwarding agreement quotation item responses for every matching service product.

  Note

After the system finds a match for the leading charge type and a rate record combination in a service product, the

system doesn’t search for more service products for the rate record.

The system selects a rate from the rate table of the matching service product based on the middle date of the

agreement validity in the forwarding agreement quotation. For example, the rates in a rate table of a matching service

product are valid from April 1, 2015 to April 20, 2015 and another rate from April 21, 2015 to May 21, 2015. If the

agreement validity is from April 15, 2015 to May 15, 2015, the system selects the rate that is valid on April 30, 2015,

which is the middle date of the agreement validity. Therefore, the system selects the rate that is valid from April 21, 2015

to May 21, 2015.

  Example

Two service products exist in the system with charge type FB00 with the following rate tables:

FB00 rate table for service product 1

Source Location

Destination Location

Equipment Type

Rate (USD)

Hamburg

Moscow

20G

100

FB00 rate table for service product 2

## Source Location

Destination Location Rate (USD)

Hamburg

Moscow

110

The leading charge type FB00 of the item contains the following rate table:

Source Location

Destination Location

Equipment Type

Rate (USD)

Hamburg

Moscow

20G

Both the service products match the leading charge type. However, the system uses the one it finds first. It doesn’t continue to

search after it has found one of the two service products.

## Rate Builder Cockpit

This is custom documentation. For more information, please visit SAP Help Portal.

62


1/14/26, 2:41 PM

For one or more items, you can open the rate builder cockpit to manually build rate from matching service products. When you

open the rate builder cockpit for an item, the system automatically finds matching service products for the leading charge type

and the corresponding rate records in the item. Subsequently, you can perform the following activities:

## Copy the service product as your response

You choose one or more matching service products and copy the service product as a response. The system automatically

copies the service product along with the calculation sheet as a response to the forwarding agreement quotation item.

## Copy charge type

You choose the forwarding agreement quotation item or a forwarding agreement quotation item response. Subsequently,

you can choose a matching service product and copy the charge type in the service product to your forwarding agreement

quotation item or the forwarding agreement quotation item response.

  Note

You can copy a charge type with or without currency conversion. When you choose to copy a charge type with currency

conversion, the system uses the currency specified in the calculation sheet item for currency conversion. If you haven’t

maintained any currency in the calculation sheet item, the system chooses the document currency you’ve specified in

the forwarding agreement quotation for currency conversion. You specify the exchange rates in Customizing for SAP

NetWeaver under  General Settings

## Currencies

 Enter Exchange Rates .

## Build rate in the forwarding agreement quotation item

You select one or more service products and build rate within the item. The system performs the following steps:

1. Tries to find matching rate records of the leading charge type in the rate records of the charge type in the service

product

2. If it finds matching rate records, the system copies all the matching rate records for only the matching charge types.

  Note

You can build rate in the forwarding agreement quotation item with or without currency conversion. When you choose to

build rates with currency conversion, the system uses the currency specified in the calculation sheet item for currency

conversion. If you haven’t maintained any currency in the calculation sheet item, the system chooses the document

currency you’ve specified in the forwarding agreement quotation for currency conversion. You specify the exchange

rates in Customizing for SAP NetWeaver under  General Settings

## Currencies

 Enter Exchange Rates .

## Build rate with responses

You select one or more service products and build rate as responses. The system performs the following steps:

1. Tries to find matching rate records of the leading charge type in the rate records of the charge type in the service

product

2. If it finds matching rate records, the system creates a forwarding agreement quotation item response in the item

The forwarding agreement quotation item response contains not only the matching charge type and matching rate

record, but all the charge types with a matching rate record.

The system creates separate forwarding agreement quotation item responses for every matching service product.

  Note

The system selects a rate from the rate table of the matching service product based on the middle date of the

agreement validity in the forwarding agreement quotation. For example, the rates in a rate table of a matching

service product are valid from April 1, 2015 to April 20, 2015 and another rate from April 21, 2015 to May 21, 2015.

If the agreement validity is from April 15, 2015 to May 15, 2015, the system selects the rate that is valid on April

This is custom documentation. For more information, please visit SAP Help Portal.

63


1/14/26, 2:41 PM

30, 2015, which is the middle date of the agreement validity. Therefore, the system selects the rate that is valid

from April 21, 2015 to May 21, 2015.

## Search additional service products

You can choose to ignore the service products that the system has found and instead specify your criteria to search for

service products

## Porting of Rates

After you have finished building rates automatically or in the rate builder cockpit for an item, and you have approved the rates, you

can perform one of the following activities:

## Send rates only for the requested services of the customer

The system merges the forwarding agreement quotation item responses that are relevant to the item before you send it to

the customer. This ensures that the customer is sent the rates for only the requested transportation services.

To use this feature, you must specify a format type of Customer in Customizing for Transportation Management under

## Master Data

## Agreement RFQs and Quotations

 Define Forwarding Agreement Quotation Types .

Send rates not only for the requirements of the customer but also additional service rates

If you want to send additional service products to the customer, you can build additional responses and send the item and

the additional forwarding agreement quotation item responses to the customer.

To use this feature, you must specify a format type of Carrier in Customizing for Transportation Management under

## Master Data

## Agreement RFQs and Quotations

 Define Forwarding Agreement Quotation Types .

## Example

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

A forwarding agreement quotation item contains a calculation sheet with the FB00 charge type and the following rate table:

Source Location ( = )

Destination Location ( =

Equipment Type ( = )

Commodity Code ( = )

Value

BUSAN

BUSAN

BUSAN

BUSAN

NINGBO

NINGBO

NINGBO

NINGBO

NINGBO

NINGBO

)

ROTTERDAM

ROTTERDAM

ROTTERDAM

ROTTERDAM

HAMBURG

HAMBURG

HAMBURG

HAMBURG

ROTTERDAM

ROTTERDAM

20G0

20G0

42G0

42G0

20G0

20G0

42G0

42G0

20G0

20G0

4701

4701

4701

4701

4701

4701

4701

4701

4701

4701

0.00

0.00

0.00

0.00

0.00

0.00

0.00

0.00

0.00

0.00

This is custom documentation. For more information, please visit SAP Help Portal.

64


1/14/26, 2:41 PM

Source Location ( = )

Destination Location ( =

Equipment Type ( = )

Commodity Code ( = )

Value

NINGBO

NINGBO

)

ROTTERDAM

ROTTERDAM

SHANGHAI

HAMBURG

SHANGHAI

HAMBURG

SHANGHAI

HAMBURG

SHANGHAI

HAMBURG

MOSCOW

MOSCOW

DELHI

DELHI

42G0

42G0

20G0

20G0

20G0

20G0

20G0

42G0

4701

4701

4701

4701

4701

4701

4701

4701

0.00

0.00

0.00

0.00

0.00

0.00

0.00

0.00

The system finds one service product with the following charge type rate tables:

FB00

Source Location (

Destination

Equipment Type (

Commodity Code

No. of Containers

Value

= )

Location ( = )

= )

NINGBO

ROTTERDAM

20G0

NINGBO

ROTTERDAM

20G0

NINGBO

ROTTERDAM

20G0

NINGBO

ROTTERDAM

20G0

NINGBO

ROTTERDAM

20G0

NINGBO

ROTTERDAM

20G0

## NINGBO

SOUTHAMPTON

20G0

## NINGBO

SOUTHAMPTON

20G0

## NINGBO

SOUTHAMPTON

20G0

## NINGBO

SOUTHAMPTON

20G0

## NINGBO

SOUTHAMPTON

20G0

## NINGBO

SOUTHAMPTON

20G0

THC

( = )

4701

4701

4701

4711

4711

4711

4701

4701

4701

4711

4711

4711

in TEU

100

200

300

100

200

300

100

200

300

100

200

300

96

90

72

138

120

108

112

126

133

145

157

178

Transportation Zone of Destination

Equipment Type ( = )

## Value

Location ( = )

EUROPE

EUROPE

20G0

22B0

30

60

This is custom documentation. For more information, please visit SAP Help Portal.

65


1/14/26, 2:41 PM

Transportation Zone of Destination

Equipment Type ( = )

## Value

Location ( = )

EUROPE

EUROPE

MALAYSIA

MALAYSIA

MALAYSIA

MALAYSIA

BAF

42G0

42H0

20G0

22B0

42G0

42H0

45

80

25

45

60

75

Destination Location ( = )

Equipment Type ( = )

Value

HAMBURG

HAMBURG

ROTTERDAM

ROTTERDAM

SOUTHAMPTON

SOUTHAMPTON

20G0

42G0

20G0

42G0

20G0

42G0

50

80

60

90

40

70

When you build a forwarding agreement quotation response, the system creates a forwarding agreement quotation response with

the following charge types and rate tables:

FB00

Source Location (

Destination

Equipment Type (

Commodity Code

No. of Containers

Value

= )

Location ( = )

= )

NINGBO

ROTTERDAM

20G0

NINGBO

ROTTERDAM

20G0

NINGBO

ROTTERDAM

20G0

NINGBO

ROTTERDAM

20G0

NINGBO

ROTTERDAM

20G0

NINGBO

ROTTERDAM

20G0

THC

( = )

4701

4701

4701

4711

4711

4711

in TEU

100

200

300

100

200

300

96

90

72

138

120

108

This is custom documentation. For more information, please visit SAP Help Portal.

66


1/14/26, 2:41 PM

Transportation Zone of Destination

Equipment Type ( = )

## Value

Location ( = )

EUROPE

EUROPE

EUROPE

EUROPE

BAF

20G0

22B0

42G0

42H0

30

60

45

80

Destination Location ( = )

Equipment Type ( = )

Value

HAMBURG

HAMBURG

20G0

42G0

50

80

The system finds a second service product with the following charge type rate tables:

FB00

Source Location (

Destination

Equipment Type (

Commodity Code

No. of Containers

Value

= )

Location ( = )

= )

MOSCOW

DELHI

20G0

( = )

4701

THC

Transportation Zone of Destination

Equipment Type ( = )

Location ( = )

ASIA

20G0

in TEU

100

Value

30

96

When you build another forwarding agreement quotation response, the system creates a new forwarding agreement quotation

response with the following charge types and rate tables:

FB00

Source Location (

Destination

Equipment Type (

Commodity Code

No. of Containers

Value

= )

Location ( = )

= )

MOSCOW

DELHI

20G0

( = )

4701

in TEU

100

96

THC

This is custom documentation. For more information, please visit SAP Help Portal.

67


1/14/26, 2:41 PM

Transportation Zone of Destination

Equipment Type ( = )

Location ( = )

ASIA

20G0

Value

30

More Information

Strategic Freight Sales

Forwarding Agreement Quotation

Forwarding Agreement Quotation Assignment

Creation of FWA Quotation from Non-TM Formatted Excel

## Use

A shipper or logistics service provider can send you, the carrier or logistics service provider, the requirements for transportation

services in a Microsoft Excel file that isn’t in the format of a Microsoft Excel downloaded from a forwarding agreement quotation.

From the Microsoft Excel file, in SAP NetWeaver Business Client (NWBC) under  Forwarding Agreement Management

## Forwarding Agreement Quotations

 Create/Update Forwarding Agreement Quotation from Microsoft Excel

, you can perform

the following activities:

Create a new forwarding agreement quotation

Create a new version of a forwarding agreement quotation

Replace the items in a forwarding agreement quotation

## Add items to a forwarding agreement quotation

You can perform these activities using Microsoft Excel 2007 and higher releases.

  Note

After you’ve created the forwarding agreement quotation, you must manually specify values for fields that haven’t been

entered automatically from the Microsoft Excel file for determining the rates you can provide. To change the values that

have been entered from the Microsoft Excel file, you must manually change the values in the forwarding agreement

quotation.

You can map the rates in the Microsoft Excel file to the rate or target rate, or both in the forwarding agreement

quotation.

You can download the forwarding agreement quotation in the same format of the customer's Microsoft Excel file. You can then

send this file to the customer. Since the customer receives the Microsoft Excel file in a known format, it’s easy for the customer to

analyze the rates.

## Prerequisites

To ensure that the values in the Excel are mapped to the correct field in the forwarding agreement quotation, you’ve performed the

following activities in Customizing for Transportation Management under  Master Data

## Agreement RFQs and Quotations

This is custom documentation. For more information, please visit SAP Help Portal.

68


1/14/26, 2:41 PM

 Define Excel and Flat View Profiles

 Map Data in Non-TM Formatted Excel to TM Fields.

:

1. Defined an excel mapping profile

2. Assigned the method in which the values in the Microsoft Excel file are mapped to the fields in the forwarding agreement

quotation.

In SAP NetWeaver Business Client (NWBC) under  Forwarding Agreement Management

## Forwarding Agreement Quotations

 Create/Update Forwarding Agreement Quotation from Microsoft Excel

, you assign excel mapping profiles to the sheets of a

Microsoft Excel file to create the forwarding agreement quotation.

The values in the Microsoft Excel file must be valid Transportation Management master data values. Else, you can use the business

add-in BAdI: Master Data Mapping for FWAQ under  Business Add-Ins (BAdIs) for Transportation Management

## Master Data

 Agreement RFQs and Quotations  to map your master data to TM master data.

## Example

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

A shipper sends you a Microsoft Excel file in the following format:

A

B

C

D

E

F

G

H

I

1

2

3 Shipping

Source Region

Source

## Source

Destination

Destination

Destination

Transportation

## Type

Country/Region

Airport

## Region

Country/Region

Airport

Mode

4 10

PA_APORT_EUR DE

BER

PA_APORT_US US

5

6

7

10

10

10

PA_APORT_EUR DE

BER

PA_APORT_US US

PA_APORT_EUR DE

BER

PA_APORT_US US

PA_APORT_EUR DE

BER

PA_APORT_US US

ATL

AUS

BOS

BWI

05

05

05

05

Shi

Typ

10

10

10

10

In Customizing for Transportation Management under  Master Data

 Agreement RFQs and Quotations

 Define Excel and

## Flat View Profiles

 Map Data in Non-TM Formatted Excel to TM Fields.

, you define an Excel Mapping Profile of CUST_1 and

specify the following settings in the Assign Excel Fields to Document Fields screen:

Document

Field Name

Orientation

Starting Column

End Column

Row Number

Hierarchy Level

Charge

Header

Item

Item

## Item

By Column

SHIPPING_TYPE

By Row

DEST_ZONE

By Row

MOT

## By Row

MOVEM_TYPE

By Row

M

A

E

H

J

R

1

This is custom documentation. For more information, please visit SAP Help Portal.

69


1/14/26, 2:41 PM

Document

Field Name

Orientation

Starting Column

End Column

Row Number

Hierarchy Level

Item

Item

Scale

Scale

Scale

Scale

Scale

  Note

SHIPPING_TYPE

## By Row

SOURCE_ZONE

## By Row

CHRG_WEIGHT

By Column

DESTLOC_CNTRY

## By Row

DEST_AIR_IATA

## By Row

SOURCELOC_CNTRY By Row

SOURCE_AIR_IATA

By Row

I

B

M

F

G

C

D

R

2

4

You’ve specified a row number of 4 for field name DESTLOC_CNTRY to specify that the values for the all the field names for

which you haven’t specified a row number, and have an orientation of By Row start from the 4th row. Therefore, the system

considers the values for following fields from the 4th row:

SOURCE_AIR_IATA

SOURCELOC_CNTRY

DEST_AIR_IATA

DESTLOC_CNTRY

SOURCE_ZONE

SHIPPING_TYPE

MOVEM_TYPE

MOT

DEST_ZONE

## SHIPPING_TYPE

You don’t have to specify a row number of 4 only for field name DESTLOC_CNTRY. You can specify a row number of 4 for any of

the field names for which the value start from the 4th row, and has an orientation of By Row, for example MOVEM_TYPE. The

system automatically assumes that the values for the all the field names for which you haven’t specified a row number, and has

an orientation of By Row begins from the 4th row.

If you don’t specify a row number of 4 for any of these fields, the system assumes that the values start right after the last

specified row number that has an orientation or By Column. Therefore, the system would assume that the values start from

row 3. This would be incorrect for this example.

In SAP NetWeaver Business Client (NWBC) under  Forwarding Agreement Management

## Forwarding Agreement Quotations

 Create/Update Forwarding Agreement Quotation from Microsoft Excel

, you upload the Microsoft Excel file. Specify the Excel

Mapping Profile of CUST_1 for the sheet that contains the relevant values and create a forwarding agreement quotation. The

system automatically maps the values in the Excel to the fields in the forwarding agreement quotation in the following method:

Specifies a shipping type of 10 in the header

Creates an item with the following attributes:

This is custom documentation. For more information, please visit SAP Help Portal.

70


1/14/26, 2:41 PM

A shipping type of 10

A movement type of DIA

A transportation mode of 05

## A trade lane with a source of PA_APORT_EUR and destination of PA_APORT_US

The system also creates a calculation sheet with a charge type of FB00. The rate table of the charge type contains the

following scale calculation base values:

SOURCELOC_CNTRY

SOURCE_AIR_IATA

DESTLOC_CNTRY

DEST_AIR_IATA

## CHRG_WEIGHT

The system selects the minimum value checkbox for chargeable weight and creates the following rate table:

Source

## IATA

Destination

## IATA

Minimum

<= 1

<= 45

<= 100

<= 300

<= 500

Country/Region

## Source

Country/Region

Destination

Value

KG (R)

KG (R)

KG (R)

KG (R)

KG (R)

(=)

DE

DE

DE

DE

Location

(=)

Location

(=)

BER

BER

BER

BER

US

US

US

US

(=)

ATL

AUS

BOS

BWI

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

Agreement

## Definition

An agreement is a long-term contract between business partners that details their commitment to conduct business with each

other in an agreed manner.

An agreement can be legally binding. Available agreement types are, for example, freight agreement, forwarding agreement,

charges templates, and internal agreement. Agreement types can be mutual between the business partners.

## Use

Agreements are the basis for calculating transportation charges and can involve one or more parties. You use forwarding

agreements to calculate transportation charges billable to your customer and freight agreements to calculate transportation

charges billable to you by your carrier. You use internal agreements to calculate transportation charges between organizations of

the same company code and between organizations of different company codes in the same company. You use charges template

when a valid released agreement is missing between the purchasing organization and carrier.

An agreement includes contractual data, such as the following:

This is custom documentation. For more information, please visit SAP Help Portal.

71


1/14/26, 2:41 PM

Organizational unit, for example, the sales or purchasing organization

Involved parties, for example, the sold-to party or carrier (except charges templates)

Terms of payment

## Validity dates

The system determines the agreement based on organization, business partner, validity period, and preconditions. Agreement

determination is based mainly on the partner relationship.

## Structure

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

An agreement can contain the following main tabs and screen areas:

## General Data

The General Data tab contains general information about the agreement, for example, the organizational unit responsible

for the forwarding order or freight order, the validity period of the agreement, and business partner details. Note that in

agreements with multiple parties, you can specify business partners and business partner hierarchy trees. In agreements

with a single party, you can specify either a business partner or business partner hierarchy tree.

You can also specify the calculation sheet template the system can use when creating a calculation sheet from within the

agreement.

  Note

If you don’t specify either the sold-to party/carrier or the business partner hierarchy tree for an agreement, the system

considers the agreement to be a standard agreement. A standard agreement is valid only if an agreement isn’t identified

during agreement determination for the sold-to party specified in the forwarding order or for the carrier specified in the

freight order.

You can define a freight agreement or forwarding agreement type to apply to multiple organizational units and multiple

business partners in Customizing for Transportation Management under  Master Data

 Agreements and Service

## Products

 Define FWA and Service Product Catalog Types  or under  Master Data

 Agreements and Service

## Products

 Define Freight Agreement Types . You can also specify multiple organizational units and business partners

for mutual agreements. While defining the freight agreement types, if you don't specify a number range, the system

allows you to manually enter the agreement ID when you create an agreement using that freight agreement type.

On this tab, you can add an agreement determination exclusion rule or a BRFplus condition to exclude the agreement from

agreement determination. During agreement determination, if the system finds a condition that matches the condition in

the agreement determination exclusion rule, the system excludes the agreement. For more information, see Rules and

Conditions for Charge Management and SP Catalogs.

## Items

The Items screen area contains the details of the agreement items. You must define at least one item for the agreement to

be relevant for charge calculation. You can assign preconditions to agreement items and each agreement item can

represent any combination of them, for example:

Service level

Stage category

## Transportation mode

This is custom documentation. For more information, please visit SAP Help Portal.

72


1/14/26, 2:41 PM

## Shipping type

The system uses these preconditions and external strategies (see External Strategies) to determine the pick-up frequency

and transit duration. Service preconditions define whether a service is valid for certain freight units.

  Note

You can assign service level, stage category, transportation mode, and shipping type only to agreements with Editable

entered for the display control setting. You make this setting in Customizing for Transportation Management under

## Master Data

 Agreements and Service Products .

This screen area can contain the following main tabs:

Precondition

## Details

Dimensions (freight agreements only)

## Capacities

Calculation Sheet Overview

## Commodity Codes

Business Share (freight agreements only)

## Default Routes

Instructions (forwarding agreements only)

## Notes

## Attachments

You must attach a calculation sheet to each agreement item and you can also specify additional preconditions, payment

terms, and commodity codes for each agreement item. For more information about the Calculation Sheet Overview screen

area, see Calculation Sheet.

  Note

You can choose an existing calculation sheet or create a calculation sheet. If you enter the name of an existing

calculation sheet, the system attaches the calculation sheet to the agreement item. If the calculation sheet doesn’t

already exist, the system prompts you to create it. The calculation sheet that the system creates is based on the

calculation sheet template you specified on the General Data tab. If you didn’t specify a calculation sheet template, the

system creates the calculation sheet with one sum line at the top level. You can then add additional lines to the

calculation sheet. For more information, see Calculation Sheet Maintenance.

## Business Partner

The Business Partner tab displays the business partners associated with the business document. For example, a bill-to

party and sold-to party is specified in a forwarding agreement.

  Note

You can display the business partner hierarchy in the business partner tab.

In a freight agreement or freight agreement RFQ master, it displays all the business partners associated with the

carrier.

In a forwarding agreement, forwarding agreement quotation, or internal agreement, it displays all the business

partners associated with the sold-to party.

This is custom documentation. For more information, please visit SAP Help Portal.

73


1/14/26, 2:41 PM

You can restrict the partner functions available in the business partner tab. For more information, see Business

Partner Determination.

The information on this tab isn’t considered when the system determines the agreement to use in a forwarding

order or freight order.

You can specify additional partner functions, such as notify party and communication party, for information

purposes in addition to primary partner functions, such as sold-to party or carrier.

## Output Management

On the Output Management tab, you can print agreement details and generate emails and faxes and send them directly to

the intended recipient. You can also see a record of the documents that were already printed or sent (by email or fax, for

example). For more information, see Output Management.

## Versions

The Versions tab contains a list of the agreement versions, including the status of each version.

## Change Documents

You can view all changes made to an agreement on the Change Documents tab or screen area. The changes are listed by

date and time. You view the details of the changes at header level by selecting the relevant row in the Transactions screen

area and at field level by selecting the relevant row in the Record Level Changes screen area. You must refresh the

agreement to view recently saved changes.

  Note

You can activate the Change Documents tab or screen area in Customizing for Transportation Management under

## Master Data

## Agreements and Service Products

 Define FWA and Service Product Types  or under  Master Data

 Agreements and Service Products

 Define Freight Agreement Types .

## Integration

All agreement types are integrated with calculation sheets, local calculation sheets, rate tables, local rate tables, scales, and local

scales. For more information, see Calculation Sheet, Rate Table, and Scale.

More Information

Agreement Management

Agreement Maintenance

Charge Calculation

## Charges Templates

Setup of MD for Charge Management and SP Catalogs

Management of Instructions

Agreement Maintenance

## Use

This is custom documentation. For more information, please visit SAP Help Portal.

74


1/14/26, 2:41 PM

You create and maintain freight agreements, forwarding agreements, internal agreements, and mutual agreements as a starting

point for enabling charge calculation.

  Note
If an agreement is a mutual agreement, the agreement usage is Customer and Service Provider. The agreement usage of an

agreement is visible in the relevant agreement personal object worklist.

## Integration

Agreement maintenance is a step in the process to set up master data in the Charge Management and Service Product Catalogs

component and is integrated with calculation sheets, local calculation sheets, rate tables, local rate tables, scales, and local scales.

You can create all charge management master data from within an agreement. For more information, see Setup of MD for Charge

Management and SP Catalogs.

You can use the master data cockpit to access an overview of the agreements and the charge management master data per

organizational unit, business partner, and charge type. The system also shows the relationship between the different types of

charge management master data. For more information, see Master Data Cockpit.

## Prerequisites

You have defined number ranges in Customizing for Transportation Management under  Basic Functions

## Charge

Calculation

## Basic Settings

## Number Range Intervals

 Assign No. Ranges to Calc. Sheets, Rate Tables, & Scales .

For freight agreements, forwarding agreements, and internal agreements, you have defined agreement item types,

agreement types, and a default agreement type in Customizing for Transportation Management under  Master Data

 Agreements and Service Products .

If you enable approval workflow for the release of agreements, you must create conditions and configure workflow settings

(see Workflow in Transportation Management).

## Features

## Agreement Versions

You can generate different versions of agreements, with the same validity period or with mutually exclusive validity periods.

Agreement versions ensure that you do not need to create a new agreement when an agreement’s validity period expires or the

details of an agreement change depending on the time period. Note that you can have only one released agreement version with

the same validity period or an overlapping validity period but can have multiple released agreement versions with mutually

exclusive validity periods. You can revert to an earlier agreement version by deactivating the released version and releasing the

earlier version. You can also delete agreement versions. The Versions tab page contains a list of the agreement versions, including

the status of each version.

## Business Partners

The system displays the business partners associated with the business document. For example, a bill-to party and sold-to party.

  Note

You can display the business partner hierarchy in the business partner tab page.

For example, in a forwarding agreement, it displays all the business partners associated with the sold-to party.

You can restrict the partner functions available in the business partner tab page. For more information, see Business

Partner Determination.

This is custom documentation. For more information, please visit SAP Help Portal.

75


1/14/26, 2:41 PM

You can specify additional partner functions, such as notify party and communication party, for information purposes in

addition to primary partner functions, such as sold-to party.

## Approval Workflow

You can enable an approval workflow for the release of agreements. You can specify that you want the system to notify an approver

when you request approval for the release of an agreement. You can also specify whether you can edit agreements during the

approval workflow. In agreements with multiple parties, only one approver must approve the release of the agreement.

Note that the approver is the person assigned to the position that is the head of the organizational unit. Therefore, at least one

organizational unit must have a position that is the head of the organizational unit. For more information, see Approval Check.

The approver uses Business Workplace to approve or reject the release of agreements. For more information, see SAP Library for

SAP Business Workflow on SAP Help Portal at http://help.sap.com/netweaver

. In SAP Library, choose  SAP NetWeaver 7.5

## Application Help

 SAP NetWeaver Library: Function-Oriented View

 Application Server

 Application Server ABAP

## Other

## Services

 Services for Application Developers

## SAP Business Workflow

 SAP Business Workflow: Reference Documentation

.

  Note
You enable the approval workflow and allow the agreement to be edited during the approval workflow when you define

agreement types. You define freight agreement, forwarding agreement, and internal agreement types in Customizing for

Transportation Management under  Master Data

 Agreements and Service Products .

## Offline Approval Workflow

Transportation Management (TM) can send work items for agreements by e-mail to a user, such as a customer agent. The user can

accept or reject a work item and update the system by e-mail. For more information, see Offline Workflow for Sending and

Approving Work Items.

## Calculation Sheets, Rate Tables, and Scales

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

You can create calculation sheets, rate tables, and scales from within an agreement in the following ways:

Create a calculation sheet for each agreement item in the Items screen area

Create a rate table for each calculation sheet item on the Calculation Sheet tab page of the Items screen area

## Create a scale for a rate by going to the rate table details in the Items screen area

You can also copy and delete the calculation sheets, rate tables, and scales from within an agreement. For more information, see

Calculation Sheet, Rate Table, and Scale.

  Note
If you copy an agreement, the system copies the calculation sheets, rate tables, and scales that you created from within the

agreement or that you referenced in the agreement.

If you delete an agreement, the system deletes the calculation sheets, rate tables, and scales that you created from within the

agreement. However, the system does not delete the calculation sheets, rate tables, and scales that you referenced in the

agreement.

This is custom documentation. For more information, please visit SAP Help Portal.

76


1/14/26, 2:41 PM

You can edit local charge management master data objects independently of the agreement they were created within. To

enable this, you select the Edit Loc. MD Objects (Edit Local Charge Management Master Data Objects) checkbox in

Customizing for Transportation Management under  Basic Functions

## General Settings

 Define General Settings for TM

.

Charge-Calculation-Specific Features

Chargeable weight

Agreement determination

Uncontrolled transportation

Header-level charges

External reference number

## Resource-based internal agreements

For more information, see Agreements and Charge Calculation.

## Preconditions

Depending on your Customizing settings and the agreement type (freight agreement, forwarding agreement, or internal

agreement), you can add preconditions at agreement and agreement-item level, for example:

Transportation mode

Shipping type

Traffic direction

Stage category

Service level

Contract basis

## Consolidation type

In the Item Precondition tab page, you can add second and subsequent preconditions to an agreement item. You can also add

second and subsequent values to the same precondition. This enables you to use the same agreement item and calculation sheet

or local calculation sheet for more than one precondition, and more than one precondition value. For example, you can specify a

precondition of Transportation Mode in an agreement item that already contains a precondition of Service Level. You can also

specify precondition values of Sea and Road for the same agreement item.

If you use the search on a precondition field to search for a precondition and you have entered an item type for the agreement

item, the system displays all preconditions that are available in the system. However you can only edit the preconditions, including

any default values, that you specified for the item type in the Customizing activity Define Freight Agreement Item Types. If you

have not entered an item type for the agreement item, the system displays all the preconditions that are available in the system.

For more information, see Customizing for Transportation Management under  Master Data

 Agreements and Service

## Products

 Define Freight Agreement Item Types .

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

77


1/14/26, 2:41 PM

The availability of some preconditions is dependent on the transportation mode of the agreement or agreement item. For

example, you can enter the contract basis and air waybill type only if the transportation mode is Air. The transportation mode

in an agreement also restricts the calculation method types available in calculation sheets created from the agreement.

The system also uses preconditions during agreement determination. You can use preconditions to search for agreements in the

relevant agreement personal object worklist on the launchpad.

You can add or remove these preconditions for freight agreements, forwarding agreements, and internal agreements in

Customizing for Transportation Management under  Master Data

 Agreements and Service Products .

## Commodity Codes

You can define commodity codes for agreement items in forwarding, freight, and internal agreements. Commodity codes enable

you to define the categories of products that the parties in the agreements have agreed to transport between them.

You can also use a wildcard entry to represent a group of commodity codes in the agreement item. The system calculates the

charges when the commodity code in the forwarding order fully or partially matches the commodity code or wildcard entry in the

agreement item. On the Charges tab page, you can see the commodity code type and commodity item number used for charge

calculation. Note that you can use commodity code-based agreement determination only for item-level calculation.

You can define a rate table or a local rate table with the rates for commodity codes. You must specify the commodity code type for

the rate table or the local rate table and you can use the commodity codes belonging to the commodity code type to define rates.

For example, your customer needs a product with a set of rates to transport livestock and another product and set of rates to

transport food. To differentiate between the commodities, you use a commodity type of LF, with commodity codes of 01*to 05* for

livestock and 16*to 24* for food. When you create a forwarding agreement, you select the appropriate product, and the system

calculates charges based on the product you transport.

You must have made settings in Customizing for Transportation Management under  Master Data

 Classification of Goods .

For more information, see Classification of Goods.

## Default Routes

You can specify default routes for agreement items. This enables you to specify the route you take between a location pair in

delivering an order. You can assign existing default routes, create new default routes, and edit default route details in the  General

## Data

 Default Routes  tab page under the agreement item.

When you create a forwarding order from a forwarding agreement item with a default route, the system copies the default route

stages to the forwarding order. The system uses the default route you specify in the agreement as the ordered route in the order.

The system uses the default route stages in charge calculation if you specify the data source as Ordered Route in the calculation

profile. You can also specify or change the actual route later in the Stages tab page of the order or in planning (see Determination

of the Route).

You can create and edit default routes under  Master Data

## Transportation Network

## Default Route , and assign these default

routes to an agreement item. You must assign a default route type to a default route. For more information, see Customizing for

Transportation Management under  Master Data

 Transportation Network

 Define Default Route Types .

## Duplication Check

The system checks and displays other business documents with matching attributes when you save or check the business

document.

  Note

You can activate the feature for the following documents:

This is custom documentation. For more information, please visit SAP Help Portal.

78


1/14/26, 2:41 PM

Freight agreements in Customizing for Transportation Management under  Master Data

 Agreements and Service

## Products

## Define Freight Agreement Types

Forwarding agreements in Customizing for Transportation Management under  Master Data

 Agreements and

## Service Products

## Define FWA and Service Product Catalog Types

Internal agreements in Customizing for Transportation Management under  Master Data

 Agreements and Service

## Products

## Define Internal Agreement Types

Freight agreement RFQs in Customizing for Transportation Management under  Master Data

 Agreement RFQs and

## Quotations

## Define Freight Agreement RFQ Types

Forwarding agreement quotations in Customizing for Transportation Management under  Master Data

## Agreement

## RFQs and Quotations

 Define Forwarding Agreement Quotation Types

## Capacities

The system displays the total capacity required from carriers, the total capacity carriers can commit to, and the total capacity

awarded to carriers.

  Note

You can activate the Capacities tab page or screen area in Customizing for Transportation Management under  Master Data

## Agreements and Service Products

 Define Freight Agreement Types  for freight agreements.

You can activate the Capacities tab page or screen area in Customizing for Transportation Management under  Master Data

## Agreements and Service Products

 Define FWA and Service Product Catalog Types  for forwarding agreements.

## Release of Agreements with Rate Tables

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

In freight agreements, forwarding agreements, and internal agreements, you can simultaneously release the agreement and the

corresponding rate tables.

In the forwarding agreement management worklist and the freight agreement management worklist, you can select and release

multiple agreements with the corresponding rate table.

  Note

If you have enabled an approval workflow for the agreement and the corresponding rate tables, the system processes the

agreement release workflow and then the rate table release workflow before releasing the agreement with the corresponding

rate table.

Freight-Agreement-Specific Features

## Specify service levels

Create freight booking, freight orders, and service orders from items

Create freight agreement RFQ masters

## Integrate business share

## Create freight agreements for general sales agents

This is custom documentation. For more information, please visit SAP Help Portal.

79


1/14/26, 2:41 PM

Create transportation allocations

## Specify dimensions and units of measure for items

Use a spreadsheet file to update details when you create or edit a freight agreement

Restrict the editing of released freight agreements only to super users

For more information, see Freight Agreement Maintenance.

## Forwarding-Agreement-Specific Features

Specify service levels and create forwarding orders and forwarding quotations based on service levels

## Specify instructions for the processing of the forwarding agreement

Specify to settle for transportation services on the basis of execution criteria, such as buyer’s consolidation, route, or trailer

unit

Consolidate goods from different suppliers into one container

For more information, see Forwarding Agreement Maintenance.

## Consumed Capacity and Amount

At agreement-item level, you can calculate how much of the capacity specified in an agreement is consumed by orders and by

invoices, and the charge amount this corresponds to. This helps you to check how much of the possible capacity you plan to use

during a specified period, and how much is actually used. The system calculates what you plan to consume by checking freight

orders or forwarding orders. The system calculates what is actually consumed by checking invoices. You can see the consumed

capacity and amount for an agreement item on the Capacities tab page in the Items screen area of the agreement. The system

calculates the actual amount based on the calculated rate for the actual capacity from the freight orders or forwarding orders.

Note that you can recalculate the consumption if you want to ensure you have the most up-to-date consumption data visible in the

agreement.

You can calculate the consumed capacity and amount for each agreement item on the launchpad by opening the agreement. In the

Items screen area, select the item and choose  Follow-Up

 Calculate Consumption .

You can calculate the consumed capacity and amount for multiple or all agreement items in one or more agreements by using

program Calculate Consumed Capacity and Amount at Agreement-Item Level (/SCMTMS/FAG_CONSUMPTION) in transaction

SE38.

## Validity Period Update

If you change the validity of an agreement, you can update the validity of all the items and service products with the same validity

period. You can also update the validity of selected items and service products instead.

## General

## Agreement search

In the relevant agreement POWL, you can search for agreements within a zone. You do not need to specify an exact source

or destination location. If you search a zone and specify to include the location within the zone, the system also searches

agreements whose location is within the zone. You can also search for agreements involving a specific carrier by using the

carrier’s standard carrier alpha code (SCAC).

## Printing, e-mailing, and faxing

This is custom documentation. For more information, please visit SAP Help Portal.

80


1/14/26, 2:41 PM

You can print agreement details and generate e-mails and faxes and send them directly to the intended recipient. For more

information, see Customizing for Cross-Application Components under  Processes and Tools for Enterprise

## Applications

 Reusable Objects and Functions for BOPF Environment

 PPF Adapter for Output Management

, as well

as Printing.

## Creation of agreements from Customizing templates

You can create Customizing templates for freight, forwarding, and internal agreements and in turn use the Customizing

templates to create agreements. You can also create a mutual agreement from a Customizing forwarding or freight

agreement template.

You can reuse these Customizing templates across multiple TM systems so that you don't need to recreate a Customizing

template in each different system. This decreases duplication and work effort. In a Customizing template, you can predefine

various attributes of an agreement such as, organization, business partner, preconditions, and commodity code.

You define a Customizing forwarding agreement template in Customizing for Transportation Management under  Basic

## Functions

 Charge Calculation

 Basic Settings

## Templates

 Define Forwarding Agreement Templates .

You define a Customizing freight agreement template in Customizing for Transportation Management under  Basic

## Functions

 Charge Calculation

 Basic Settings

## Templates

 Define Freight Agreement Templates .

You define a Customizing internal agreement template in Customizing for Transportation Management under  Basic

## Functions

 Charge Calculation

 Basic Settings

## Templates

 Define Internal Agreement Templates .

## Creation of agreements from master data templates

You can create master data templates for freight, forwarding, and internal agreements on the launchpad and in turn use the

master data templates to create agreements. You can also create a mutual agreement from a master data forwarding or

freight agreement template. However, you cannot reuse these master data templates across multiple TM systems.

In a Customizing template, you can predefine the different attributes of an agreement such as, organization, business

partner, preconditions, and commodity code.

Note that you can also create a master data template from an existing Customizing template.

You define a master data forwarding agreement template in the Create Forwarding Agreement Template app on the

launchpad.

You define a master data freight agreement template in the Create Freight Agreement Template app on the launchpad.

You define a master data internal agreement template in the Create Internal Agreement Template app on the launchpad.

## Activities

Create or update freight agreements in the Freight Agreements app on the launchpad.

Create or update forwarding agreements in the Forwarding Agreements app on the launchpad.

Create or update internal agreements, in the Internal Agreements app on the launchpad.

Create a forwarding agreement from a Customizing or a master data template in the Create Forwarding Agreement app on the

launchpad. Enter the forwarding agreement template ID in the Forwarding Agreement Template field and choose Continue.

Create a freight agreement from a Customizing or a master data template in the Create Freight Agreement app on the launchpad.

Enter the freight agreement template ID in the Freight Agreement Template field and choose Continue.

Create an internal agreement from a Customizing or a master data template in the Create Internal Agreement app on the

launchpad. Enter the internal agreement template ID in the Internal Agreement Template field and choose Continue.

This is custom documentation. For more information, please visit SAP Help Portal.

81


1/14/26, 2:41 PM

Create a mutual agreement from a forwarding agreement Customizing or a master data template in the Create Forwarding

Agreement app on the launchpad. Enter the forwarding agreement template ID in the Forwarding Agreement Template field,

select the Mutual Agreements checkbox, and choose Continue.

More Information

## Agreement

## Agreement Management

Archiving Agreements and RFQ Masters

Agreements and Charge Calculation

## Use

Transportation Management (TM) calculates transportation charges on the basis of the data stored in agreements and charge

management master data. You can make specific charge calculation settings as part of the creation and maintenance of

agreements.

## Prerequisites

You have configured the prerequisites for agreements (see Agreement Maintenance).

## Features

## Chargeable Weight

You can assign a dimensional weight profile at agreement level and at agreement-item level to calculate the chargeable weight of a

product. By assigning a dimensional weight profile at agreement-item level, you can have a different dimensional weight profile for

each stage of a freight order or forwarding order. During charge calculation, you can change the dimensional weight profile at the

charge-item level in a forwarding order.

  Note

A dimensional weight profile at agreement-item level has priority over a dimensional weight profile at agreement level. If you do

not assign a dimensional weight profile at agreement-item level, the system uses the dimensional weight profile assigned at

agreement level.

You can also assign a dimensional weight profile for manually-changed charge lines.

You can also assign a dimensional weight profile to the calculation profile of the organizational unit. If you do not assign a

dimensional weight profile at the agreement-item and agreement header level, the system uses the dimensional weight profile

assigned to the calculation profile of the organizational unit. You can assign dimensional weight profiles to calculation profiles

in Customizing for Transportation Management under  Basic Functions

 Charge Calculation

 Basic Settings

## Define

Calculation Profiles .

You can define dimensional weight profiles in Customizing for Transportation Management under  Basic Functions

## Charge

## Calculation

## Data Source Binding

 Define Dimensional Weight Profiles .

## Agreement Determination

This is custom documentation. For more information, please visit SAP Help Portal.

82


1/14/26, 2:41 PM

Note that the following information is relevant whether the calculation sheets, rate tables, or scales are created locally within an

agreement, calculation sheet, or rate table or are created independently of an agreement, calculation sheet, or rate table.

The system determines the agreement based on business partner and organizational unit (sales organization for forwarding

agreements and purchasing organization for freight agreements). If there are multiple agreements for a carrier or customer when

the system tries to calculate transportation charges, the system determines which agreement to use within the organizational

hierarchy. As part of the agreement determination, if you select the Evaluate All Agreements checkbox in Customizing for

Transportation Management under  Basic Functions

 Charge Calculation

## Basic Settings

 Define Charges Profiles , the

system takes the leading charge type into account by skipping agreements that use calculation sheets without a leading charge

type. The system then skips agreements if the leading charge type does not have a rate. If there are multiple leading charge types

in a calculation sheet, all the leading charge types must have a rate defined for the system to consider the agreement and

calculation sheet for charge calculation. We recommend that you maintain a single leading charge type in a calculation sheet.

The system also uses preconditions during agreement determination. For more information, see Agreement and Calculation Sheet

Determination.

## Uncontrolled Transportation

You can specify whether an agreement is for controlled or uncontrolled transportation, which impacts on whether the system can

calculate the charges for the main stage of an uncontrolled transportation. For more information, see Uncontrolled Transportation.

## Header-Level Charges

The system can calculate charges for an agreement item at header level even when calculating the rest of the charges at stage

level. You can group the charges common to all stages in a separate agreement item. During charge calculation, the system

calculates the header-level charges independently of the stage charges. The system calculates the stage charges as usual.

Note that when you create an internal settlement document, you can choose to settle header-level charges along with one of

stage-level charges or you can also settle header-level charges independently. You must run the program

/SCMTMS/CFIR_CREATE_BATCH to manage this setting. When you select the Header Charges in Separate Settlement

Document checkbox, the system settles the head-level charges independently. Also, the system displays the Ready for Invoicing

status at the header charges along with the charge item status.

To enable header-level charges when calculating charges at stage level, you must maintain a calculation profile with the calculation

level as stage level. For more information, see Customizing for Transportation Management under  Basic Functions

## Charge

Calculation

## Basic Settings

 Define Calculation Profiles . For information about calculation profiles, see Calculation Profiles.

## External Reference Number

You can specify the reference number of a separate agreement in an external system or the reference number your business

partner uses in their internal system for your same agreement in TM.

## Resource-Based Internal Agreements

You can specify internal agreements as resource-based agreements to use when charging only for the use of resources. For more

information, see Internal Settlement for Resources.

  Example

A shipper wants carrier A to transport goods on its behalf. Carrier A outsources the transportation of the goods to carrier B.

Carrier B uses carrier A’s vehicles to transport the goods. Carrier A uses a resource-based internal agreement to charge carrier

B for the use of its vehicles.

## More Information

This is custom documentation. For more information, please visit SAP Help Portal.

83


1/14/26, 2:41 PM

Charge Calculation

## Agreement

Freight Agreement Maintenance

## Use

As part of the creation and maintenance of freight agreements, you can use the following features specific to freight agreements

only.

Note that you can use many other features that are not specific to freight agreements. For more information, see Agreement

Maintenance.

## Prerequisites

You have configured the prerequisites for agreements (see Agreement Maintenance).

## Features

## Service Levels

The service levels you can choose for freight agreement items are service levels that are defined for the carrier. For more

information, see Definition of Business Partners.

## Capacity Dashboard

For an item in a freight agreement, you choose  Follow Up

 Calculate Consumption  and open the dashboard. You can view the

quantity consumed and the amount calculated in order documents and settlement documents for the validity period of the

agreement item. You can subsequently compare this data to the quantity decided in the agreement. This enables you to analyze

the usage of the agreement.

You can view the quantity consumed and the amount calculated in order documents and settlement documents for specific

periods of time. You can also view these individual orders and the settlement documents.

## Freight Booking, Freight Orders, and Service Orders

When you create a freight document or service order from an agreement item, the system copies the services you have specified

in the item to the freight document or service order. For more information, see Definition of Carrier Service Codes.

Note that when you create a freight order from a multi-party freight agreement the carrier information is not copied to the freight

order.

## Freight Agreement RFQ Masters

You can create freight agreement RFQ masters from within freight agreements to start the process of updating the freight

agreements. To create a freight agreement RFQ master from within a freight agreement, in the Freight Agreements worklist app on

the launchpad. Open the freight agreement and choose the Create RFQ Master button.

You can also create freight agreements from within freight agreement RFQ masters. You can do this, in the Create Freight

Agreement RFQ Master app on the launchpad. Open the freight agreement RFQ master and choose the  Follow Up

 Create/Update Agreement

 button.

This is custom documentation. For more information, please visit SAP Help Portal.

84


1/14/26, 2:41 PM

For more information about freight agreement RFQ masters, see Freight Agreement RFQ Master.

## Business Share Integration

If you include a target share when you create or update a freight agreement from a freight agreement RFQ master, the system

includes the target share in the freight agreement items. If you create a freight agreement without reference to a freight

agreement RFQ master, you can manually add a target share to the freight agreement items.

If you want the system to take the target share into account in planning, you must choose the Create Business Share button. The

system includes the target share in the business share, and uses the business share in the carrier selection settings in planning.

You can specify mandatory settings by choosing the Edit Business Share button on the Business Shares tab page.

To create a business share for planning, you must have specified the following settings in the freight agreement:

Valid-from date and valid-to date

## Carrier

Trade lane on the Precondition tab page

## Periodicity on the Capacities tab page

When you create and edit a business share, the system displays a temporary identifier (ID) in the Business Shares tab page. It

assigns a permanent ID when you save the freight agreement.

For more information about how you can use a business share in planning, see Business Share.

## General Sales Agents

You can create a freight agreement for a general sales agent (GSA), and specify the airlines to which the freight agreement applies.

To enable you to create this freight agreement, you must specify the following settings in  BP – Maintain Business Partner

 Display in BP Role

 Vendor Data :

## Carrier Category of Agent

Airlines the GSA represents in the Airline Codes screen area

You can open the BP – Maintain Business Partner transaction in SAP Menu under  Logistics

 Transportation Management

 Master Data .

In the freight agreement, when you specify the GSA carrier, you cannot specify an airline at header level. Instead you can only

specify the airlines you specified in the BP master, at item level.

## Transportation Allocations

In freight agreements with a single party, you can create and edit transportation allocations for freight agreement items to allocate

a certain volume of business to a carrier on a specific trade lane. Note that the freight agreement item must have just one trade

lane. For more information, see Check Against Transportation Allocations.

## Dimensions and Units of Measure

You can enter the dimensions and units of measure for a freight agreement item. You can specify the attributes, such as length,

width, height, and girth, on the Dimensions tab page of the freight agreement. When you perform direct shipment option

determination, the system compares the attributes of the parcel specified in the freight unit with that specified in the freight

agreement. For the system to consider a freight agreement for charge calculation, all the attribute values specified in the freight

unit must be less than or equal to the attribute values specified in the freight agreement. If there are multiple freight agreements

This is custom documentation. For more information, please visit SAP Help Portal.

85


1/14/26, 2:41 PM

that meet this condition, the system displays a list from which you can choose one. For more information, see Rate Determination

for Direct Shipment of Parcels.

  Example
You define dimensions for the following freight agreement items:

Item 100 with a height of 200 cm and width of 100 cm

## Item 200 with a height of 250 cm

When you perform direct shipment option determination for a freight unit with a height of 210 cm, the system can use freight

agreement item 200 to determine the charges.

When you perform direct shipment option determination for a freight unit with height of 200 cm and width of 90 cm, the

system can use both freight agreement item 100 and freight agreement item 200 to determine the charges. In this case, the

system displays both from which you can choose one.

## Excel Integration

You can use a spreadsheet file to update details when you create a new freight agreement or when you edit an existing freight

agreement. You can perform the following actions:

Download the freight agreement as a spreadsheet file.

Update the file that you downloaded.

Upload the file on the Excel Integration tab page.

The system uses the information in the uploaded file to automatically enter information in the relevant fields in the freight

agreement.

  Note

You specify the fields that can be edited in the downloaded spreadsheet file in Customizing for Transportation Management

under  Master Data

 Agreements and Service Products

 Define Editable Fields in Excel

.

## Rate Change Requests

Your carriers can request rate changes for released freight agreements. Your carriers can therefore request changes to the rates

previously agreed between you, without the need for a new agreement. For more information, see Request of Rate Changes by

Carriers.

## Editing of Released Freight Agreements

You can restrict the editing of released freight agreements only to super users if you set up authorizations using authorization

object T_AGR_FRS. However, you can also allow all users to edit released freight agreements in Customizing for Transportation

Management under  Basic Functions

## General Settings

 Define General Settings for TM .

  Note

If you upgraded from a lower release of SAP S/4HANA toSAP S/4HANA 1909 or higher, you're using authorization object

T_AGR_FR instead of T_AGR_FRS. Then as a default, all users with edit authorization can edit released freight agreements.

## More Information

This is custom documentation. For more information, please visit SAP Help Portal.

86


1/14/26, 2:41 PM

## Agreement

## Request of Rate Changes by Carriers

Your carriers can request changes to the rates previously agreed between you, without the need for a new agreement.

## Use

Your carriers can request rate changes for released freight agreements with a current or future validity period. If you, the shipper,

accept the request from the carrier, the carrier then submits the new rates. If you accept the new rates, then the freight agreement

(rates) is adjusted according to the new rates and the new rates are used when calculating the transportation charges.

  Note
Your carriers can request rate changes only for rate tables and calculation sheets created within the freight agreement, that is,

local rate tables and calculation sheets.

## Prerequisites

The freight agreement is released.

The rates your carrier wants to change are in rate tables or local rate tables and not directly in calculation sheets or local

calculation sheets.

You’ve selected the Negotiable checkbox for the charge type of the calculation sheet line items.

## Process

1. Typically, the carrier contacts you, the shipper, to request a change of rates for the charge lines in a released freight

agreement.

2. In the freight agreement, you can specify from when the rate change is valid and also a deadline for you to decide about the

rate change.

Note that the start date of the rate validity of the calculation sheet line items should be the same as the start date of the

rate change validity.

3. You accept or reject the rate change request at the calculation sheet line item level.

If you reject the rate change request, the freight agreement then has the status Request Rejected and the process ends.

If you accept the rate change request, the freight agreement then has the status Request Accepted.

Note that if you accept or reject the rate change request at header level, this action overwrites any changes accepted or

rejected at rate level.

4. You download the Update_Rate_<Date_of_Shipper_Deadline>.xlsx file available on the Attachments tab page

of the freight agreement and rename it to Updated_Rate_<Date_of_Shipper_Deadline>.xlsx before sending it

to the carrier.

5. The carrier enters the rate changes into the file and sends the file back to you.

6. Once you receive the file from the carrier, you upload it to the Attachments tab page of the freight agreement and then

upload the rate changes to the system by choosing the  Rate Change Request

 Submit Rates  button.

The freight agreement now has the status Rates Uploaded.

This is custom documentation. For more information, please visit SAP Help Portal.

87


1/14/26, 2:41 PM

7. You submit the rate changes to the system using program Update Responses in SAP TM

(/SCMTMS/UPLOAD_RFQ_RESPONSE).

Once the system is updated, the freight agreement has the status Rates Submitted or Rates Submitted with Errors. The

program creates a new validity period in the rate tables (both kinds, including local) of the calculation sheet line items with

the rate changes proposed by the carrier.

8. You review each successfully submitted rate change and accept or reject the changes at rate table validity-period level.

If you accept the rate changes, the system truncates the existing validity period and releases the new validity period. The

calculation sheet line items have the status Rate Change Accepted.

Note that if you accept or reject the changes at header level, this decision overwrites any changes accepted or rejected at

rate level.

## Result

The new rates come into effect from the new valid-from date. The previous rates remain relevant up until the new valid-from date.

## More Information

Freight Agreement Maintenance

Forwarding Agreement Maintenance

## Use

As part of the creation and maintenance of forwarding agreements, you can use the following features specific to forwarding

agreements only.

Note that you can use many other features that are not specific to forwarding agreements. For more information, see Agreement

Maintenance.

## Prerequisites

You have configured the prerequisites for agreements (see Agreement Maintenance).

## Features

## Service Levels

The service levels you can choose for forwarding agreement items are the service levels that are defined for the forwarding

agreement item’s transportation mode, or service levels that are defined independently of the transportation mode. You define

service levels in Customizing for Transportation Management under  Forwarding Order Management

 Define Transportation

Service Level Codes .

## Capacity Dashboard

For an item in a forwarding agreement, you choose  Follow Up

 Calculate Consumption  and open the dashboard. You can view

the quantity consumed and the amount calculated in order documents and settlement documents for the validity period of the

agreement item. You can subsequently compare this data to the quantity decided in the agreement. This enables you to analyze

the usage of the agreement.

This is custom documentation. For more information, please visit SAP Help Portal.

88


1/14/26, 2:41 PM

You can view the quantity consumed and the amount calculated in order documents and settlement documents for specific

periods of time. You can also view these individual orders and the settlement documents.

## Instructions

If you have a forwarding agreement with service products that have services, the system automatically adds the instructions

specified for the service type to the Instructions tab page of the forwarding agreement. You can edit or delete these instructions,

and also add additional instructions. Note that if you create a forwarding order from a forwarding agreement with instructions, the

system includes the instructions in the forwarding order and subsequent business documents.

You define service types in Customizing for Transportation Management under  Basic Functions

 General Settings

## Define

Service Types . You define instructions and instruction sets in Customizing for Transportation Management under  Basic

Functions

## Instructions

 Define Instructions and Instruction Sets . You assign instruction sets to service types in Customizing

for Transportation Management under  Basic Functions

## Instructions

 Assign Instruction Sets . For more information, see

Management of Instructions.

## Forwarding Orders and Forwarding Quotations

You can create forwarding orders and forwarding quotations based on service products.

## Forwarding Agreement Quotations

You can create forwarding agreement quotations from within forwarding agreements to start the process of updating the

forwarding agreements. You can create a forwarding agreement quotation from within a forwarding agreement in the Create

Forwarding Agreement or Edit Forwarding Agreement app on the fiori launchpad. Open the forwarding agreement and choose the

Follow Up

 Create Forwarding Agreement Quotation  button.

You can also create forwarding agreements from within forwarding agreement quotations. You can do this in the Create

Forwarding Agreement Quotation or Edit Forwarding Agreement Quotation app on the fiori launchpad. Open the forwarding

agreement quotation and choose the Create Agreement button.

For more information about forwarding agreement quotations, see Forwarding Agreement Quotation.

## Buyer’s Consolidation

For forwarding agreement items, you can consolidate goods from different suppliers that are intended for one ship-to party. For

more information, see Buyer’s Consolidation.

## Settlement Basis

At the agreement item level in forwarding agreements, you can specify that you bill your business partners based on certain

execution criteria, such as by the trailers used to fulfill the order, or the route taken to execute the order. During settlement, the

system creates a single forwarding settlement document for all the forwarding orders that meet the specified execution criterion.

By default, the settlement basis is at forwarding order level. For more information, see Execution-Based Settlement.

More Information

## Agreement

This is custom documentation. For more information, please visit SAP Help Portal.

89
