1/14/26, 2:43 PM

Transportation Management (TM)

Generated on: 2026-01-14 14:43:46 GMT+0000

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


1/14/26, 2:43 PM

## Carrier Collaboration

As a shipper, you can collaborate with carriers for various processes in Transportation Management (TM) in SAP S/4HANA, even if

the carrier doesn't use TM.

Once you give your carrier access to the relevant TM features, the carrier can, for example, respond to your freight agreement

requests for quotation (RFQs) with their proposed rates.

  Note

This documentation is aimed at shippers, and also at carriers or service provider representatives for carrier organizations who

work with shippers.

## Prerequisites

You've performed the following steps for each carrier that you want to collaborate with:

1. In the Maintain Business Partner (BP) transaction, you've created a business partner with the business partner role of

Carrier.

2. In the Maintain Collaboration Users app, you've defined a collaboration user and specified that this collaboration user is

for the business partner with the role of Carrier.

For more information, see Maintain Collaboration Users (F4911).

The following graphic describes the mapping of a carrier organization with an external user.

You've also performed the following steps for the relevant business document types:

You've assigned an attachment schema that is configured to use the Attachment Service. For more information, see

Working with Attachments.

## More Information

This is custom documentation. For more information, please visit SAP Help Portal.

2


1/14/26, 2:43 PM

Management of Quotations for Transportation Services

Strategic Freight Procurement

## Agreement Management

As a shipper, you can collaborate with carriers during your strategic freight procurement process in Transportation Management

(TM) in SAP S/4HANA, even if the carrier doesn't use TM.

For example, you can request quotations for transportation services and carriers can respond with their proposed rates. You can

then negotiate the best rates from your carriers.

## More Information

Management of Quotations for Transportation Services

## Strategic Freight Procurement

## Management of Quotations for Transportation Services

As a shipper, you can request quotations for transportation services and negotiate the best rates during your strategic freight

procurement process, even if the carrier doesn't use Transportation Management (TM) in SAP S/4HANA.

As the carrier or a service provider representative negotiating freight agreements with shippers, you can use the Manage Freight

Agreement RFQs app to monitor your freight agreement requests for quotation (RFQs). You can submit your responses to the

shipper with your proposed rates for the transportation services.

As a carrier or a service provider representative, you can use the Manage Freight Agreement RFQs app to do the following:

Monitor freight agreement RFQs by status, for example, freight agreement RFQs that are open for response and are waiting

for carrier confirmation

Use a spreadsheet to enter your rate details

Use attachments and notes

## Respond to freight agreement RFQs

Display freight agreement RFQs in a worklist sorted by response deadline

Display freight agreement RFQs in a list that you can filter by different criteria

Choose not to negotiate rates with the shipper by rejecting your participation in a freight agreement RFQ

  Note

If as a shipper, you decide that you don't want carriers to collaborate with you using the Manage Freight Agreement RFQs app,

you can exchange freight agreement RFQ details using a spreadsheet instead. For more information, see Responses from

Carriers Using Spreadsheets.

## Prerequisites

The shipper has configured the prerequisites for collaboration with carriers (see Carrier Collaboration).

This is custom documentation. For more information, please visit SAP Help Portal.

3


1/14/26, 2:43 PM

The shipper has configured the prerequisites for strategic freight procurement (see Strategic Freight Procurement).

The shipper has maintained carrier text types to enable carriers to add notes.

## Procedure

1. In the Create Freight Agreement RFQ Master app, the shipper creates a freight agreement RFQ master to detail their

transportation requirements (see Freight Agreement RFQ Master).

2. The shipper publishes the freight agreement RFQ master and the system automatically creates and sends individual freight

agreement RFQs to the carriers.

3. The system notifies each carrier about their individual RFQ, basically asking the carrier to bid for the provision of future

transportation services in a trade lane.

4. In the Manage Freight Agreement RFQs app, the carrier evaluates the freight agreement RFQ and responds to the shipper.

If the carrier does not want to bid for the transportation services, the carrier can choose to reject participating in the freight

agreement RFQ.

If the carrier wants to participate in the bid, they can respond to the shipper with their rates.

If needed, the carrier can download the freight agreement RFQ in a spreadsheet, enter their rate details, and then upload

the freight agreement RFQ spreadsheet back to the Manage Freight Agreement RFQs app.

  Note
The uploaded spreadsheet is also attached to the freight agreement RFQ as an attachment.

5. The shipper monitors and reviews the carrier responses for the freight agreement RFQ.

6. The shipper accepts or rejects the rates from the carrier.

7. The shipper requests a confirmation of the rates submitted by the carrier.

8. Once the rates are confirmed, the shipper creates or updates the freight agreement for the carrier.

## More Information

Requesting of Quotations for Transportation Services

## Order Management

As a carrier or a service provider representative, you can use the transportation order management apps to respond to freight

tendering requests in the freight subcontracting process.

You have the following features available in transportation order management:

## Freight tendering

Freight order confirmation

## Freight order execution

The following graphic gives you an overview of transportation order management:

This is custom documentation. For more information, please visit SAP Help Portal.

4


1/14/26, 2:43 PM

## Freight Tendering

As a carrier or a service provider representative, you can display the freight requests for quotation (RFQs) that you have received

from a shipper. You can also display the freight quotations that you submitted to a shipper for a specific freight RFQ.

For more information, see Freight Request for Quotation and Freight Quotation.

## Freight Order Confirmation

As a carrier or a service provider representative, you can view, confirm, or reject freight orders that have been sent to you by a

shipper. This helps you to plan your workload independently of the tendering process.

For more information, see Freight Order Confirmation.

## Freight Order Execution

As a carrier or a service provider representative, you can view and monitor the execution of freight orders that have been sent to

you by a shipper. You can report events and report actual quantities of the items for the freight orders that you are executing.

For more information, see Freight Order Execution.

## Freight Request for Quotation

As a shipper, when you use a freight request for quotation (RFQ) tendering process to send out one or more freight requests for

quotation (RFQs) to carriers, the carriers can use the transportation order management apps to respond to your freight tendering

requests. For more information as a shipper, see Freight Tendering and Tendering.

This is custom documentation. For more information, please visit SAP Help Portal.

5


1/14/26, 2:43 PM

As a carrier or a service provider representative, you can use the Manage Freight RFQs app to manage and respond to the freight

RFQs that you have received from the shipper.

You can use the following features in the Manage Freight RFQs app:

On the app tile, view the number of freight RFQs that are due for a response from you and when they are due. The app tile

also displays when the information was last retrieved from the system and allows you to refresh the information.

Use the app to view all freight RFQs, and to list those that are open, closed, and responded to.

Open freight RFQs require a response from you. The freight RFQs that you respond to are sent to the shipper for evaluation.

Closed freight RFQs are those that have been evaluated by the shipper and are either rejected or awaiting an award. Closed

freight RFQs are also those whose response time has been exceeded or that were canceled.

Perform a search on the freight RFQs by using the filter criteria.

Choose a freight RFQ from the list to view details of the freight RFQ such as source and destination details, transportation

details, cargo details, information about whether the cargo is considered dangerous goods, transportation stops, notes, and

attachments.

Choose a transportation stop in a freight RFQ to view the items that are to be loaded or unloaded at that stop. You can also

view details of the cargo items.

Perform the following actions in a freight RFQ:

Accept a freight RFQ without making any changes.

Accept a freight RFQ by proposing changes to the price, currency, or start and end dates.

  Note

This action is available to you if the shipper has configured the tendering settings to allow you to propose

changes.

Reject a freight RFQ and select a reason for rejection.

A freight quotation is created when you accept a freight RFQ. The freight quotation is listed in the freight RFQ details.

As a carrier, you can revise the quotation multiple times within the response deadline.

## Prerequisites

The shipper has configured the prerequisites for collaboration with carriers (see Carrier Collaboration).

## Freight Quotation

As a carrier or a service provider representative, when you accept freight RFQs, the system creates freight quotations and sends

them to the shipper.

You can use the Display Freight Quotations app to view all existing freight quotations.

You can use the following features in the Display Freight Quotations app:

On the app tile, view the number of freight quotations that have been awarded to you or rejected by the shipper. The app tile

also displays when this information was last retrieved from the system and allows you to refresh this information.

Use the app to view all freight quotations, and to list those that are pending, rejected, and awarded.

This is custom documentation. For more information, please visit SAP Help Portal.

6


1/14/26, 2:43 PM

The pending freight quotations are those that are being evaluated by the shipper. The awarded freight quotations are those

that have been evaluated by the shipper and have been awarded to you. The rejected freight quotations are those that have

been evaluated by the shipper and have been rejected.

Perform a search on the freight quotations by using the filter criteria.

Choose a freight quotation from the list to view details of the freight quotation such as source and destination details,

transportation details, cargo details, information about whether the cargo is considered dangerous goods, transportation

stops, notes, and attachments.

Choose a transportation stop in a freight quotation to view the cargo items that are to be loaded or unloaded at that stop.

You can also view details of the cargo items.

## Prerequisites

The shipper has configured the prerequisites for collaboration with carriers (see Carrier Collaboration).

## Freight Order Confirmation

As a carrier or a service provider representative, you can use the Confirm Freight Orders app to manage and respond to freight

orders sent to you by the shipper.

You can use the following features in the Confirm Freight Orders app:

On the app tile, view the number of freight orders that require your confirmation.

Use the app to view all the freight orders, and to list those that require your confirmation or have been confirmed or closed.

Closed freight orders are the freight orders that you have either canceled or completed.

Perform a search on the freight orders by using the filter criteria.

Choose a freight order from the list to view details of the freight order such as source and destination details,

transportation details, cargo details, information about whether the cargo is considered dangerous goods, driver details,

transportation stops, notes, and attachments.

Choose a transportation stop in a freight order to view details of the stop and the items to be loaded or unloaded at that

stop.

Update driver and vehicle registration details for a freight order.

Propose changes to the confirmed start date and time, confirmed end date and time, price limit, or currency by choosing

Confirm with Changes.

## Prerequisites

The shipper has configured the prerequisites for collaboration with carriers (see Carrier Collaboration).

## Freight Order Execution

As a carrier or a service provider representative, you can use the Manage Execution of Freight Orders app to monitor the

execution of freight orders sent to you by a shipper.

You can use the following features in the Manage Execution of Freight Orders app:

This is custom documentation. For more information, please visit SAP Help Portal.

7


1/14/26, 2:43 PM

On the app tile, view the number of freight orders that you are currently executing.

View all freight orders, and list those that are in execution or have been closed or blocked.

A closed freight order is a freight order that you have either canceled or completed.

A blocked freight order is a freight order that is currently blocked for execution by the shipper.

Perform a search on the freight orders by using the filter criteria.

From the list of freight orders, you report a planned event or an unplanned tour event to the shipper for a freight order in

execution.

For a planned event, you select the event listed for a location. The reporting date and time is defaulted to the current date

and time. Additionally, you can and add a comment. For an unplanned event, you select a reason for the event. An example

for a planned event could be Arrival or Loading Begin, and an example of an unplanned event could be Delay.

You cannot report events for a blocked freight order.

Choose a freight order from the list to view details about the freight order such as transportation details, source and

destination details, cargo details, information about whether the cargo is considered dangerous goods, transportation

stops, tour events, notes, and attachments.

Report a planned event for a freight order when viewing the details of a freight order.

Choose a transportation stop in a freight order to view details of the stop, stop events, and details of the items to be loaded

or unloaded at that stop.

Report a planned or unplanned event in a transportation stop. When you report an event, you enter the date and time and

add a comment. You also need to choose a reason if you report an unplanned event.

Report the actual quantities of each item in a transportation stop.

Under Tour Events, add a new, unplanned event that affects the entire transportation, and also report the event.

View documents or links attached by the shipper. As a carrier, you can upload documents or links.

## Prerequisites

The shipper has configured the prerequisites for collaboration with carriers (see Carrier Collaboration).

## Settlement Management

As a carrier or a representative of a service provider, you can use the settlement management apps to process freight orders for

settlement.

You have the following features available in the settlement management:

Manage Charges for Freight Orders

Manage Freight Orders for Invoicing

Manage Freight Invoices

## Display Credit Memos

## Manage Charges for Freight Orders

This is custom documentation. For more information, please visit SAP Help Portal.

8


1/14/26, 2:43 PM

As a carrier or a representative of a service provider, you can view, update, or add charges for a freight order. You can also view the

details of a freight order such as stages, cargo etc.

For more information, see Manage Charges for Freight Orders.

## Manage Freight Orders for Invoicing

As a carrier or a representative of a service provider, you can use this app to create invoices for freight orders that you've received

from shipper.

For more information, see Manage Freight Orders for Invoicing.

## Manage Freight Invoices

As a carrier or a representative of a service provider, you can use this app to manage invoices that you've submitted for a shipper.

For more information, see Manage Freight Invoices.

## Display Credit Memos

As a carrier or a representative of a service provider, you can use this app to display the credit memos that you've submitted to a

shipper.

For more information, see Display Credit Memos .

Manage Charges for Freight Orders

App ID: F7104

With this app, as a carrier or a logistics service provider, you can monitor the charges for the freight orders that you've received

from the shipper.

## Key Features

On an app tile, view the number of freight orders that require your approval, freight orders that have new disputes that you

haven't submitted to the shipper, and freight orders with disputes that you have submitted to the shipper.

View all freight orders that you're currently executing, and list them by the status of the dispute.

A new dispute is a freight order that you're editing to update the charges but haven't submitted to the shipper.

A submitted dispute is a freight order for which you've updated the charges and submitted to the shipper for review.

A freight order for approval is a freight order for which the shipper has proposed charges and has sent to you for approval.

A freight order with no dispute or a resolved dispute is listed under No Dispute.

Perform a search on the freight orders using the filter criteria.

Choose a freight order from the list to view details about the freight order such as transportation details, source and

destination details, cargo details, transportation stages, charges, notes, and attachments.

Edit a freight order to perform the following actions:

Add a charge or update an existing charge.

This is custom documentation. For more information, please visit SAP Help Portal.

9


1/14/26, 2:43 PM

Propose the rate amount for a new or an existing charge with or without a calculation base.

Propose the price per unit or quantity for a new or an existing charge with a calculation base.

  Note

For charges having amounts in percentages and values, you must propose charges using two different fields

Proposed Rate Amount in % and Proposed Rate Amount.

You can't add a new charge that is a percentage charge type.

You can only delete a charge line that you've added to the freight orders. You can add a charge line only for No

Dispute, For Approval, and New Dispute freight orders. The charge lines that you've added are known as

unplanned charges.

If you select multiple charge lines and try to delete them, the system deletes only the unplanned charges.

Tax handling isn't supported.

Submit a freight order with updated charges to the shipper for review.

Discard a new dispute.

Accept a freight order with proposed charges from the shipper.

View or add documents or links attached to a dispute.

  Note

You can attach documents to a freight order only if the freight order has a dispute.

View or add notes attached to a dispute.

You can add a note by entering the text and choosing  (Submit).

  Note

You can add notes to a freight order only if the freight order has a dispute.

Personalize the charges table and group, sort, or filter the charges by a particular field.

You can also manage and save your personalized views of the table using variants.

## Prerequisites

The shipper has configured the prerequisites for collaboration with carriers (see Carrier Collaboration).

Manage Freight Orders for Invoicing

App ID: F7732

With this app, as a carrier or a logistics service provider, you can create invoices for freight orders that you've received from a

shipper.

## Key Features

You can use this app to do the following:

This is custom documentation. For more information, please visit SAP Help Portal.

10


1/14/26, 2:43 PM

View all the freight orders based on their invoicing status.

For freight orders where you're added as an additional agreement party, you can't view those freight orders using this app.

## Status

Not Invoiced

Partially Invoiced

Completely Invoiced

## Description

Freight orders where invoices haven't been submitted

Freight order where invoices need your approval for posting

## Freight order where invoices have been created and submitted

Use various filter criteria, for example, Source Location, Destination Location, or Means of Transport to search freight

orders

View various details of a freight order, for example, Net Amount in Document Currency, Source Location, and Destination

## Location

Create freight invoices for Not Invoiced or Partially Invoiced freight orders

Supported Device Types

Desktop

## Tablet

Related Information

Manage Freight Invoices

Manage Freight Invoices

App ID: F7106

With this app, as a carrier or a logistics service provider, you can manage invoices that you've submitted to a shipper.

## Key Features

You can use this app to do the following:

On the app tile, view the number of invoices that you've created but not submitted and invoices that need your approval

View all the invoices that you're currently processing and list them by their status:

Status

Submitted

## Description

Invoices that are submitted by the shipper for further processing

## Not Submitted

Invoices that you've created but not submitted for further processing

## For Approval

Invoices that need your approval for changes to the charges proposed by the shipper

## Rejected or Canceled

Invoices that are canceled by you or rejected by the shipper

This is custom documentation. For more information, please visit SAP Help Portal.

11


1/14/26, 2:43 PM

Use various filter criteria, for example, Invoice Date, Document Currency, or Terms of Payment, to search invoices

On the list page, view various invoice details, for example, Invoice Date, Gross Amount, Proposed Gross Amount and

## Status

Select an invoice to view various details, for example, Invoice Date, Terms of Payment, and Invoice Items

View invoice items with relevant freight order details such as source and destination location, and the date and time of

departure and arrival

You can select the invoice item to view its transport details, cargo details, and the charges.

You can also see if a charge line has a dispute or not. Disputed charge lines are marked in red and non-disputed ones are

marked green.

Disputed charge lines are the ones which you've inserted or edited manually and the shipper needs to act upon them.

  Note

The charge lines that you've excluded from the invoice using the Exclude button doesn't have any color associated with

it.

View, upload, download, or delete an attachment

## View or add a note

Once you've added a note, you can submit it to the shipper.

## Not Submitted

You can do the following with Not Submitted invoices:

Edit the invoice reference and the invoice date

## Add a tax charge or a charge to an invoice item

Discard invoices that you don't need. Discarding an invoice deletes it permanently from the system

Delete the charge lines that you, as a carrier, have added to the invoice

Edit the rate amount, price per unit, or quantity of an existing charge of an invoice item

Exclude or include a charge line from the invoice item

## Submit the invoice to the shipper

After editing, you must save the invoice before submitting it to the shipper.

## Submitted

You can do the following with Submitted invoices:

## Create a credit memo for the invoice

You can create a credit memo to reverse an invoice that has been processed by a shipper and post the credit memo to

financial accounting for further processing. There can be only one credit memo for an invoice. When you create a credit

memo, you can also attach a note for the shipper in the credit memo.

You can also add a note when you create a credit memo.

## Recall an invoice

This is custom documentation. For more information, please visit SAP Help Portal.

12


1/14/26, 2:43 PM

You can recall an invoice only if the financial posting of an invoice isn't yet processed.

Successful recall of an invoice results in the following changes:

The invoice goes back to the Not Submitted status

You can resubmit the invoice with or without any changes

Any existing disputes corresponding to the invoice are canceled.

## For Approval

You can do the following with For Approval invoices:

View an invoice, invoice item details, and the charges proposed by the shipper

## Edit an invoice or its item

If the charges proposed by the shipper are acceptable, approve the shipper's proposal

If the charges proposed by the shipper aren't acceptable, edit the charges and propose new charges

Recall an invoice

## Rejected

You can view the details of invoices that have been canceled by you or rejected by the shipper.

Supported Device Types

Desktop

## Tablet

Related Information

## Display Credit Memos

Manage Freight Orders for Invoicing

Display Credit Memos

App ID: F7502

With this app, a carrier or a logistics service provider can display the credit memos that they've submitted to a shipper. They can

create a credit memo to reverse an invoice that has been processed by a shipper. Thay can post the credit memo to financial

accounting for further processing. There can be only one credit memo for an invoice.

## Key Features

You can use this app to do the following:

On the app tile, view the number of credit memos that you've submitted to the shipper

Use various filter criteria, for example, Credit Memo Date or Terms of Payment, to search credit memos

View the various credit memo details, for example, Credit Memo Reference, Gross Amount, and Status

This is custom documentation. For more information, please visit SAP Help Portal.

13


1/14/26, 2:43 PM

View credit memo items with the relevant freight order details such as source and destination location, and the date and

time of departure and arrival

You can select the freight order to view its details and the charges that are applicable to the credit memo.

## Manage notes and attachments that are relevant for the credit memo

Note that you can upload, download, or delete an attachment, but you can only add a note and can't delete or edit the note.

Supported Device Types

Desktop

## Tablet

Related Information

## Manage Freight Invoices

This is custom documentation. For more information, please visit SAP Help Portal.

14
