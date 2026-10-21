APPLICATION HELP | PUBLIC

Release 9.4 SP00

Document Version: 2.0 – 2019-10-09

Enterprise Services and ESR Content

.

d
e
v
r
e
s
e
r
s
t
h
g
i
r

l
l

A

.
y
n
a
p
m
o
c
e
t
a

i
l

ffi
a
P
A
S
n
a
r
o
E
S
P
A
S
9
1
0
2
©

THE BEST RUN


Content

1

2

Enterprise Services and ESR Content. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .4

Enterprise Services. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5

2.1

Transportation Order Processing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5

Transportation Order. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6

Transportation Planning View. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109

2.2

Transportation Request Processing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122

Transportation Request. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .123

2.3

Freight Agreement Processing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176

Freight Agreement. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .177

2.4

Forwarding Agreement Processing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 190

Forwarding Agreement. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .191

2.5

Customer Freight Invoice Request Processing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 205

Customer Freight Invoice Request. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 206

2.6

Supplier Freight Invoice Request Processing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 219

Supplier Freight Invoice Request. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220

2.7

Supplier Invoice - Create (B2B). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 223

InvoiceRequest_In - Invoice. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .224

InvoiceRequest_In - Item. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .227

Examples of B2B Messages for a Carrier Invoice. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 231

3

3.1

3.2

4

4.1

Other Web Services. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245

GetTransportationDocumentURI. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245

BusinessDocumentFlowTMInformationbyBusinessObjectReferenceQueryResponse_In. . . . . . . . . 247

Additional ESR Content. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 249

Integration Scenarios. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 249

TM_ERPInvoiceIntegration. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 249

TM_ERPOrderIntegration. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 251

TM_ERPSalesOrderScheduling. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 254

TM_ERPShipmentIntegration_Out. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .255

TM_ERPShipmentIntegration_In. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 257

TM_GTSExportDeclarationIntegration. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 258

TM_GTSTradeComplianceCheckIntegration. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 259

TM_FINCreditManagementIntegration. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 260

4.2

Mappings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 261

Interface Mappings for Shipment Integration. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 261

2

## P U B L I C

Enterprise Services and ESR Content
## Content


Message Mappings for Shipment Integration. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 262

Enterprise Services and ESR Content
## Content

P U B L I C

3


1

## Enterprise Services and ESR Content

This section contains information about the enterprise services and additional Enterprise Services Repository
(ESR) content for SAP Transportation Management (SAP TM).

4

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services and ESR Content


2  Enterprise Services

This section contains information about the enterprise services for SAP Transportation Management (SAP
TM).

2.1  Transportation Order Processing

## Definition

The ordering of transportation services from carriers.

Technical Data

Entity Type

## Technical Name

Business Context and Use

## Process Component

## TransportationOrderProcessing

The Transportation Order Processing  process component provides shippers, logistics service providers, and
carriers with various functions for processing transportation orders. It enables them to exchange
transportation-relevant data and execute the functions that are required to create, change, or cancel freight
orders, freight requests for quotation, or freight bookings. In addition, it allows them to assign transportation
demands to transportation capacities, and it allows shippers to create delivery proposals for further processing
in the corresponding logistics execution system.

The functions provided by the Transportation Order Processing  process component can be used in different
scenarios. For example, they enable a shipper to send a transportation order to a carrier who can then
subcontract the order to other carriers. During transportation planning, the shipper decides which freight units
are to be transported by the shipper’s own vehicle resources and which are to be subcontracted to carriers.
When the shipper sends a transportation order to a carrier, the carrier receives the order in the form of a
transportation request. The carrier is then expected to send a confirmation to the shipper.

Following on from this scenario, the carrier can perform refined planning based on the transportation request,
and decide if the requested transportation service is to be executed by the carrier’s own resources or by one or
more subcontractors. If the carrier subcontracts the execution of the transportation service, the carrier sends
a transportation order to the relevant subcontractors, who can also reply to the carrier by sending
confirmations. Note that these activities are performed in the carrier's business system.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

5


From a shipper’s perspective, a carrier may also be a logistics service provider (LSP). The business of an LSP
typically consists of consolidating transportation demands from multiple shippers into containers or full truck
loads.

Notes on SAP Implementation

## Master Data for B2B Communication

You have to define your carriers as business partners in the SAP Transportation Management (SAP TM) back-

end system. You define business partners in SAP NetWeaver Business Client (NWBC) by choosing  Master

Data General Define Business Partner

.

We recommend that you assign standard IDs to each business partner and to each of the involved locations
and products.

## More Information

SAP Transportation Management (SAP TM)

2.1.1  Transportation Order

## Definition

An order from an ordering party to a carrier to transport goods from one or more shippers to one or more
consignees in accordance with agreed terms and conditions. The order can also include the assignment of
vehicle resources and transportation stages. The order can also have the character of a freight request for
quotation that is sent to a carrier.

Technical Data

Entity Type

Technical Name

Object Category

6

P U B L I C

Business Object

TransportationOrder

## Business Process Object

Enterprise Services and ESR Content
Enterprise Services


## Business Context and Use

The Transportation Order business object enables the following transportation activities to be carried out by
shippers and logistics service providers, and by carriers who subcontract transportation services to other
carriers:

● Request a quotation by sending a freight request for quotation to a carrier

● Request the execution of a transportation service by sending a freight order to a carrier

● Book freight space by sending a freight booking to a carrier

● Send a cancellation of a freight request for quotation, freight order, or freight booking to a carrier

● Receive replies from a carrier, who can accept, modify, or decline a freight request for quotation, freight

order, or freight booking

● Send a shipping instruction (also known as a waybill notification) to a carrier or to an additional

communication partner, based on a freight booking that has already been confirmed

● Receive a shipping instruction based on a freight booking that has already been confirmed by a carrier.
When an inbound shipping instruction is processed, this triggers the creation of a replicated freight
booking document in the receiving system. This occurs typically when an import organization receives
information about a freight booking that has been triggered by an export organization in a multinational
company.

● Request a loading appointment by sending planning information about loading or unloading to a business
partner (for example, a warehouse or container freight station). This business partner can be either an
organizational unit of the logistics service provider (LSP) that sends the loading appointment, or it can be
an independent service provider that is subcontracted to carry out loading or unloading operations.

● Receive notifications from a business partner about loading or unloading operations that have been

executed

In addition, the Transportation Order  business object enables a freight order or freight booking to be updated
based on current order execution information (for example, customs processing information).

For more information about the business context, see the documentation of the  Transportation Order
Processing [page 5]  process component.

2.1.1.1

Export Declaration Requesting Out

## Definition

An interface to request the creation or cancellation of business transaction documents that are prerequisites
for an export declaration.

Technical Data

## Entity Type

## Service Interface

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

7


Category

Direction

SAP A2A

## Outbound

## Business Context and Use

The Export Declaration Requesting Out outbound service interface groups operations that send data to
a customs management application in order to request the creation or cancellation of documents that are
required for the transportation of customs-relevant goods.

## Constraints

Note that this interface cannot currently be used to change business transaction documents that are
prerequisites for an export declaration.

Notes on SAP Implementation

## Integration

The operations in this interface can exchange data with the operations in the Export Declaration Requesting
In inbound service interface in the Customs Processing process component. This enables you to exchange
customs data between the GTS Integration (TM-GT-GTS) component in SAP Transportation Management (SAP
TM) and the GTS: Customs: Export Processing (SLL-LEG-CUS-EXP) component in SAP Global Trade Services.

## Configuration

To exchange data with SAP Global Trade Services, you have to connect the SAP TM system to the SAP Global
Trade Services system and make the required Customizing settings in both systems. For more information, see
the following:

● Integration with SAP Global Trade Services

● SAP Library for SAP Global Trade Services on SAP Help Portal at http://help.sap.com/grc

. In SAP

Library, choose  Global Trade Services Customs Management

Logistics Integration of Feeder System

and Customs Management

Logistics Integration: Freight Orders .

2.1.1.1.1

Request Export Declaration

## Definition

To request the creation of business transaction documents that are prerequisites for an export declaration.

8

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


Technical Data

Entity Type

Release State

Technical Name

Namespace

Direction

## Mode

## Idempotency

P2P Communication Enabled

Service Operation

## Released

ExportDeclarationSUITERequest_Out

http://sap.com/xi/TMS/Global

Outbound

Asynchronous

No

## Yes

## Business Context and Use

A shipper needs an export declaration to transport customs-relevant goods. The Request Export Declaration
outbound operation requests the creation of an export declaration for items in an order. The operation sends
the request to a customs management application, which creates the export declaration and handles the
customs procedure for the items.

## Related Operations

● The corresponding Maintain Export Declaration inbound operation in the Customs Processing process
component can create an export declaration based on a request received from the Request Export
Declaration  outbound operation.

● The Change Transportation Order based on Export Declaration Confirmation [page 13]  inbound

operation receives a confirmation of the creation or cancellation of an export declaration.

● The Request Export Declaration Cancellation [page 10]  outbound operation requests the cancellation of

an export declaration.

## Features

The Request Export Declaration outbound operation sends data such as the following to the customs
management application:

● Parties involved (for example, seller and consignee)

● List of items that represent the goods to be transported and additional information about the goods (for
example, containers, packages, or products, with the respective measurements and quantities, such
as gross weight, net weight, and number of pieces)

● Means of transport

● Incoterms

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

9


● IDs of related business documents, for example, sales order or outbound delivery

## Message Types

● ExportDeclarationSUITERequest

Notes on SAP Implementation

## Integration

The Request Export Declaration outbound operation is triggered in the SAP Transportation Management (SAP
TM) back-end system when a customs declaration is requested for items in an order. Note that the following
applies if a customs declaration is requested for items in a freight order:

● The freight order must have a specific execution status, which is defined in the customs profile. For more

information, see Customizing for Transportation Management under  Transportation Management

Global Trade Define Customs Activities and Profiles .

● The freight order must be based on a delivery-based transportation requirement.

## Configuration

For more information, see the documentation of the Export Declaration Requesting Out [page 7] outbound
interface.

## Enhancements

The BAdI for ExportDeclarationSUITERequest_Out (/SCMTMS/EXP_SE_EXPDE_REQ) Business Add-In (BAdI) is
available for this operation.

2.1.1.1.2

Request Export Declaration Cancellation

## Definition

To request the cancellation of business transaction documents that are prerequisites for an export declaration.

Technical Data

Entity Type

Release State

10

## P U B L I C

Service Operation

## Released

Enterprise Services and ESR Content
Enterprise Services


## Technical Name

ExportDeclarationSUITECancellationRequest_Out

Namespace

Direction

## Mode

## Idempotency

P2P Communication Enabled

http://sap.com/xi/TMS/Global

Outbound

Asynchronous

No

## Yes

## Business Context and Use

The Request Export Declaration Cancellation outbound operation requests the cancellation of an export
declaration in a customs management application.

## Related Operations

● The corresponding Cancel Export Declaration inbound operation in the Customs Processing process

component can receive a cancellation request from the Request Export Declaration Cancellation outbound
operation.

● If the export declaration is canceled, the Change Transportation Order Based on Export Declaration

Confirmation [page 13]  inbound operation receives a confirmation of the cancellation from the customs
management application.

## Features

The Request Export Declaration Cancellation outbound operation sends the ID of the relevant export
declaration and the business transaction document reference.

## Message Types

● ExportDeclarationSUITECancellationRequest

## Prerequisites

The Request Export Declaration [page 8] outbound operation has requested the creation of an export
declaration.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

11


Notes on SAP Implementation

## Integration

This operation is triggered when a customs declaration is canceled in the SAP Transportation Management
(SAP TM) back-end system.

## Configuration

For more information, see the documentation of the Export Declaration Requesting Out [page 7] outbound
interface.

## Enhancements

The BAdI for ExportDeclarationSUITECancellationRequest_Out (/SCMTMS/ECA_SE_EXPDE_CAN) Business
Add-In (BAdI) is available for this operation.

2.1.1.2

Export Declaration Requesting In

## Definition

An interface to receive confirmations of requests for an export declaration.

Technical Data

Entity Type

Category

## Direction

Business Context and Use

Service Interface

SAP A2A

## Inbound

The Export Declaration Requesting In inbound service interface contains an operation that receives a
confirmation of the creation or cancellation of an export declaration that is required for the transportation of
customs-relevant goods.

Notes on SAP Implementation

Integration

12

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


The operation in this interface can exchange data with the corresponding operation in the Export Declaration
Requesting Out outbound service interface in the Customs Processing process component. This enables you to
exchange customs data between the GTS Integration (TM-GT-GTS) component in SAP Transportation
Management (SAP TM) and the GTS: Customs: Export Processing (SLL-LEG-CUS-EXP) component in SAP
Global Trade Services.

## Configuration

For more information, see the documentation of the Export Declaration Requesting Out [page 7] outbound
service interface.

2.1.1.2.1

Change Transportation Order Based on Export
Declaration Confirmation

## Definition

To change a transportation order based on the confirmation of an export declaration.

Technical Data

Entity Type

Release State

Technical Name

Namespace

Direction

## Mode

## Idempotency

P2P Communication Enabled

Service Operation

## Released

ExportDeclarationSUITEConfirmation_In

http://sap.com/xi/TMS/Global

## Inbound

Asynchronous

No

## Yes

## Business Context and Use

A request for an export declaration has been sent to a customs management application. The customs
management application has created an export declaration and sent it to the customs authority. If the customs
authority approves the export declaration, it provides a movement reference number (MRN) for the goods. The
customs management application can then send a confirmation that contains, for example, the MRN, the
status of customs processing, and the export declaration ID.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

13


The Change Transportation Order based on Export Declaration Confirmation inbound operation receives
the confirmation and updates the relevant order. This operation can also receive a confirmation of a canceled
export declaration.

## Related Operations

The Change Transportation Order based on Export Declaration Confirmation inbound operation can receive a
confirmation from the corresponding Confirm Export Declaration outbound operation in the Customs
Processing process component.

## Features

If the customs management application confirms the creation of an export declaration, the Change
Transportation Order based on Export Declaration Confirmation inbound operation receives data that
includes the following:

● Export declaration ID

● Movement reference number (MRN) issued by the customs authority

● Indicator that shows whether the export declaration has been approved

The operation adds the export declaration ID and the MRN to the relevant order and updates the customs
status of the order.

If the customs management application confirms the cancellation of an export declaration, the Change
Transportation Order based on Export Declaration Confirmation inbound operation receives a cancellation
indicator that shows whether the export declaration has been canceled. The operation updates the status of
the customs activity in the order. A new export declaration can then be requested at a later stage, if required.

## Message Types

● ExportDeclarationSUITEConfirmation

## Prerequisites

The Request Export Declaration [page 8] outbound operation has requested the creation of an export
declaration.

## Error Handling

Forward Error Handling

14

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


The inbound operation Change Transportation Order based on Export Declaration Confirmation supports
Forward Error Handling (FEH). The following error categories are used:

● DCE: Determination and Conversion Error

● PRE: Processing Error

For more information about the individual error categories, see the code list for the global data type
LogItemCategoryCode.

Notes on SAP Implementation

## Configuration

For more information, see the documentation of the Export Declaration Requesting Out [page 7] outbound
interface.

## Enhancements

The BAdI for ExportDeclarationSUITEConfirmation_In (/SCMTMS/EIN_SE_EXPDE_ANS) Business Add-In (BAdI)
is available for this operation.

2.1.1.3

Transportation Customs Declaration Requesting
Out

## Definition

An interface to receive declarations requesting the creation or cancellation of documents that are required for
the transportation of customs-relevant or security filing-relevant goods.

Technical Data

Entity Type

Category

## Direction

Service Interface

B2B

## Outbound

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

15


## Business Context and Use

The Transportation Customs Declaration Requesting Out outbound service interface groups operations that
send data to a customs management application in order to request the creation or cancellation of documents
that are required for the transportation of customs-relevant or security filing-relevant goods.

Notes on SAP Implementation

## Integration

The operations in this interface can exchange data with a customs management application.

## Configuration

To exchange data with a customs management application, you have to connect the SAP TM system to a
customs management application and make the required Customizing settings in both systems.

You have made the following settings in the SAP TM system:

● You have defined one or more suitable output profiles, and schedule conditions that control whether a

message is sent. You do this in Customizing for Cross-Application Components under  Processes and

Tools for Enterprise Applications Reusable Objects and Functions for BOPF Environment PPF Adapter

for Output Management Maintain PPF Settings .
Note that output profile /SCMTMS/TOR is provided as part of the standard Customizing settings. This
profile is available in the configuration of PPF application /SCMTMS/TRANSPORTATION via the subactivity
Define Action Profile and Actions.

● You have assigned a suitable output profile to the relevant freight unit types. You define freight unit types in

Customizing for Transportation Management under  Planning

Freight Unit Define Freight Unit Types .

● You have defined a logical system that represents the client from which the outbound communication is to
take place, and you have assigned a queue of the type Outbound Queues to this logical system. You do this

in Customizing for SAP Transportation Management under  SCM Basis

Integration Basic Settings for

Creating the System Landscape Assign Logical System and Queue Type . Here, the logical system must
be marked as an SAP system. Also check the settings in the following Customizing activities: Name Logical
Systems, Assign Logical Systems to a Client, Maintain Business System Group , and Settings for qRFC
Communication.

2.1.1.3.1

Request Transportation Customs Declaration

## Definition

To request the creation of business transaction documents that are prerequisites for any of the following:

● export declaration

● import declaration

● transit declaration

16

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


● security filing

Technical Data

Entity Type

Release State

Technical Name

Namespace

Direction

## Mode

## Idempotency

## Service Operation

## Released with Restrictions

TransportationCustomsDeclarationRequest_Out

http://sap.com/xi/TMS/Global

Outbound

Asynchronous

## Not Applicable

P2P Communication Enabled

## Yes

## Business Context and Use

In a customs management application, the Request Transportation Customs Declaration outbound operation
requests one of the following:

● export declaration

● import declaration

● transit declaration

● security filing

## Related Operations

● Request Transportation Customs Declaration Cancellation

● Change Transportation Order Based on Transportation Customs Declaration Confirmation

## Message Types

● TransportationCustomsDeclarationConfirmation

Notes on SAP Implementation

## Enhancements

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

17


● Enhancement Spot: /SCMTMS/CDC_SE_SPOT_CDC

● BAdI: /SCMTMS/CDC_SE_CDC_REQ

2.1.1.3.2

Request Transportation Customs Declaration
Cancellation

## Definition

To request the cancellation of business transaction documents that are prerequisites for any of the following:

● export declaration

● import declaration

● transit declaration

● security filing

Technical Data

Entity Type

Release State

Technical Name

Namespace

Direction

## Mode

## Idempotency

## Service Operation

## Released with Restrictions

TransportationCustomsDeclarationCancellationR

equest_Out

http://sap.com/xi/TMS/Global

Outbound

Asynchronous

## Not Applicable

P2P Communication Enabled

## Yes

## Business Context and Use

In a customs management application, the Request Transportation Customs Declaration outbound operation
requests the cancellation of one of the following:

● export declaration

● import declaration

● transit declaration

18

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


● security filing

## Related Operations

● Request Transportation Customs Declaration

● Change Transportation Order Based on Transportation Customs Declaration Confirmation

## Message Types

● TransportationCustomsDeclarationCancellationRequest

## Prerequisites

The Request Transportation Customs Declaration operation has requested the creation of a transportation
customs declaration.

Notes on SAP Implementation

## Enhancements

● Enhancement Spot: /SCMTMS/CDC_SE_SPOT_CDC

● BAdI: /SCMTMS/CDC_SE_CDC_CRQ

2.1.1.4

Transportation Customs Declaration Requesting In

## Definition

An interface to receive confirmations of the creation or cancellation of documents that are required for the
transportation of customs-relevant or security filing-relevant goods.

Technical Data

Entity Type

Category

## Direction

Service Interface

B2B

## Inbound

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

19


## Business Context and Use

The Transportation Customs Declaration Requesting In inbound service interface contains an operation that
receives a confirmation of the creation or cancellation of documents that are required for the transportation of
customs-relevant or security filing-relevant goods.

Notes on SAP Implementation

## Integration

The operations in this interface can exchange data with a customs management application.

## Configuration

To exchange data with a customs management application, you have to connect the SAP TM system to a
customs management application and make the required Customizing settings in both systems.

2.1.1.4.1

Change Transp. Order Based on Transp. Custms.
Decl. Conf.

## Definition

To change a transportation order based on the confirmation of any of the following:

● export declaration

● import declaration

● transit declaration

● security filing

Technical Data

Entity Type

Release State

Technical Name

Namespace

Direction

20

## P U B L I C

## Service Operation

## Released with Restrictions

TransportationCustomsDeclarationConfirmation_

In

http://sap.com/xi/TMS/Global

## Inbound

Enterprise Services and ESR Content
Enterprise Services


Entity Type

## Mode

## Idempotency

Service Operation

Asynchronous

## Not Applicable

P2P Communication Enabled

## Yes

## Business Context and Use

The Change Transportation Order Based on Transportation Customs Declaration Confirmation inbound
operation receives a confirmation or a cancellation one of the following:

● export declaration

● import declaration

● transit declaration

● security filing

The operation then updates the relevant order.

## Related Operations

● Request Transportation Customs Declaration

● Request Transportation Customs Declaration Cancellation

## Error Handling

## Forward Error Handling

The inbound operation Change Transportation Order based on Export Declaration Confirmation supports
Forward Error Handling (FEH). The following error categories are used:

● DCE: Determination and Conversion Error

● PRE: Processing Error

● PRE.TEE.LRE: Lock Request Error

For more information about the individual error categories, see the code list for the global data type
LogItemCategoryCode.

## Message Types

● TransportationCustomsDeclarationRequest

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

21


## Prerequisites

The Request Transportation Customs Declaration operation has requested the creation of a transportation
customs declaration or the Request Transportation Customs Declaration Cancellation operation has requested
the cancellation of a transportation customs declaration.

Notes on SAP Implementation

## Enhancements

● Enhancement Spot: /SCMTMS/CDC_SE_SPOT_CDC

● BAdI: /SCMTMS/CDC_SE_CDC_CNF

2.1.1.5

Trade Compliance Check Requesting Out

## Definition

An interface to request the processing of a trade compliance check.

Technical Data

Entity Type

Category

## Direction

Business Context and Use

Service Interface

A2A

## Outbound

The Trade Compliance Check Requesting Out outbound service interface groups operations that send data to a
global trade services (GTS) application to request a trade compliance check for a freight document or to
request the cancellation of a trade compliance check for a freight document.

Notes on SAP Implementation

Integration

22

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


The operations in this interface and the corresponding inbound interface Trade Compliance Check Requesting
In [page 27] enable you to integrate SAP Transportation Management (SAP TM) with the SAP Global Trade
Services application. Data is exchanged between the GTS Integration (TM-GT-GTS) component in SAP TM and
the GTS: Compliance Management (SLL-LEG-CON) component in SAP Global Trade Services.

Note that a freight document (that is, freight order or freight booking) in the SAP TM back-end system
corresponds to an instance of a Transportation Order [page 6] business object.

## Configuration

To exchange data with SAP Global Trade Services, you must connect the SAP TM system to the global trade
services (GTS) system and make the required Customizing settings in both systems.

In the SAP TM system, you must enable the trade compliance check for the relevant freight document types in
Customizing for Transportation Management. For more information, see Trade Compliance Check.

For information about SAP Global Trade Services, see SAP Library for SAP Global Trade Services on SAP Help

## Portal at http://help.sap.com/grc

 under  SAP Global Trade Services Compliance Management

.

In addition, you have made the following message control settings in SAP TM:

● You have defined one or more suitable output profiles, as well as schedule conditions that control whether

a message is sent. You do this in Customizing for Cross-Application Components under  Processes and

Tools for Enterprise Applications Reusable Objects and Functions for BOPF Environment PPF Adapter

for Output Management Maintain PPF Settings .

● You have assigned a suitable output profile to the relevant freight order types in Customizing for

Transportation Management under

Freight Order Management

Freight Order Define Freight Order

Types .

● You have assigned a suitable output profile to the relevant freight booking types in Customizing for

Transportation Management under

Freight Order Management

Freight Booking Define Freight

Booking Types .

● You have defined a logical system that represents the client from which the outbound communication is to
take place, and you have assigned a queue of the type Outbound Queues to this logical system. You do this

in Customizing for SCM Basis under

## Integration Basic Settings for Creating the System Landscape

Assign Logical System and Queue Type . Here, the logical system must be marked as an SAP system. Also
check the settings in the following Customizing activities:

○ Name Logical Systems

○ Assign Logical Systems to a Client

○ Maintain Business System Group

○ Settings for qRFC Communication

2.1.1.5.1

Request Trade Compliance Check

## Definition

To request a trade compliance check for a transportation order.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

23


Technical Data

Entity Type

Release State

Technical Name

## Namespace

Application Component

Category

Direction

## Mode

## Idempotency

Change/Update Behavior

P2P Communication Enabled

Business Context

Service Operation

## Released

TradeComplianceCheckSUITERequest_Out

http://sap.com/xi/TMS/Global

TM-GT-GTS

A2A

Outbound

Asynchronous

Not Applicable

Type 1

## Yes

You perform a trade compliance check for your freight documents prior to commencing the required
transportation activities and also throughout the ongoing transportation process. The trade compliance check
helps you to ensure that your business transactions comply with international trade regulations.

The Request Trade Compliance Check outbound operation requests a trade compliance check for a freight
document. It sends the freight document data to a connected global trade services application.

## Related Operations

● The inbound operation Change Transportation Document Based on Trade Compliance Check Confirmation

[page 28] receives the result of a trade compliance check.

● The outbound operation Request Trade Compliance Check Cancellation [page 26] requests the

cancellation of a trade compliance check.

## Features

The Request Trade Compliance Check outbound operation sends the freight document data that is required to
perform the trade compliance check. This comprises the following mandatory data:

● Business partner (sales organization or purchasing organization)

24

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


If a forwarding order or forwarding quotation is assigned to the freight document, the operation sends the
business partner of the sales organization. Otherwise, the operation sends the business partner of the
purchasing organization.

● At least one item

● At least the source location country and destination location country

The operation also sends all business partner IDs and all countries from the transportation routes, if this data is
available. The countries are determined from the stages, source location, and destination location.

Notes on SAP Implementation

## Integration

The Request Trade Compliance Check outbound operation can send freight document data to the Maintain
Trade Compliance Check inbound service operation in the Trade Compliance Processing process component.
This enables you to perform a trade compliance check for an SAP Transportation Management (SAP TM)
freight document in the SAP Global Trade Services application.

SAP TM sends a freight document to the global trade services (GTS) system when a user creates a freight
document that is relevant for the trade compliance check (that is, the compliance check has been enabled in
the freight document type). If the freight document is subsequently changed, SAP TM triggers a trade
compliance check only if the changed fields are relevant for the compliance check (that is, the fields described
in the Features section above). The system blocks a freight document that is relevant for the trade compliance
check until the check has been performed and the result is that the document is compliant.

 Note

● The trade compliance check performed in SAP Global Trade Services for SAP TM consists of

sanctioned party list screening and an embargo check.

● For sanctioned party list screening, SAP Global Trade Services checks address data that is derived only
from business partner master data. It does not check address data derived from locations. In addition,
it does not check addresses that a user enters in the Printing Address field on the Business Partner tab
page in the forwarding order.

● For the embargo check, SAP Global Trade Services checks the countries in the transportation route.

## Configuration

For more information, see Trade Compliance Check Requesting Out [page 22].

## Enhancements

The Business Add-In (BAdI) BAdI for TradeComplianceCheckSUITERequest_Out (/SCMTMS/CPC_SE_CPC_REQ)
is available for this operation.

More Information

## Trade Compliance Check

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

25


2.1.1.5.2

Request Trade Compliance Check Cancellation

## Definition

To request the cancellation of a trade compliance check for a transportation order.

Technical Data

Entity Type

Release State

Technical Name

## Namespace

Application Component

Category

Direction

## Mode

## Idempotency

Change/Update Behavior

P2P Communication Enabled

Business Context

Service Operation

## Released

TradeComplianceCheckSUITECancellationRequest_

Out

http://sap.com/xi/TMS/Global

TM-GT-GTS

A2A

Outbound

Asynchronous

Not Applicable

Not Applicable

## Yes

You have sent a freight document to a connected global trade services (GTS) application to perform a trade
compliance check. The GTS application continues to check the freight document until you request the
cancellation of the check, for example, because the transportation activities have been completed or the
freight document has been canceled.

The Request Trade Compliance Check Cancellation outbound operation requests the cancellation of a trade
compliance check for a freight document.

26

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## Features

The Request Trade Compliance Check Cancellation outbound operation sends the ID of the freight document
for which the trade compliance check is to be canceled.

## Prerequisites

The Request Trade Compliance Check [page 23] outbound operation has requested a trade compliance check
for a freight document.

Notes on SAP Implementation

## Integration

The Request Trade Compliance Check Cancellation outbound operation can send freight document data to the
Cancel Trade Compliance Check inbound operation in the Trade Compliance Processing process component.
This enables you to cancel a trade compliance check for an SAP Transportation Management (SAP TM) freight
document in the SAP Global Trade Services application.

SAP TM sends a cancellation if the freight document has been canceled (life cycle status of the freight
document is Canceled). The document that was created in SAP Global Trade Services is canceled accordingly.

## Configuration

For more information, see Trade Compliance Check Requesting Out [page 22].

## Enhancements

The Business Add-In (BAdI) BAdI for TradeComplianceCheckSUITECancellationRequest_Out (/SCMTMS/
CPC_SE_CPC_CANCREQ) is available for this operation.

More Information

Trade Compliance Check

2.1.1.6

Trade Compliance Check Requesting In

## Definition

An interface to receive confirmations of requests for a trade compliance check.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

27


Technical Data

Entity Type

Category

## Direction

Service Interface

A2A

## Inbound

## Business Context and Use

The Trade Compliance Check Requesting In inbound service interface contains an operation that receives the
result of a trade compliance check from a global trade services (GTS) application.

## Notes on SAP Implementation

For more information, see Trade Compliance Check Requesting Out [page 22].

2.1.1.6.1

Change Transportation Order Based on Trade
Compliance Check Confirmation

## Definition

To change a transportation order of the category “freight order” or “freight booking” based on the confirmation
of a trade compliance check.

Technical Data

Entity Type

Release State

Technical Name

## Namespace

Service Operation

## Released

TradeComplianceCheckSUITEConfirmation_In

http://sap.com/xi/TMS/Global

Application Component

TM-GT-GTS

28

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


Category

Direction

## Mode

## Idempotency

Change/Update Behavior

P2P Communication Enabled

Business Context

A2A

## Inbound

Asynchronous

Not Applicable

Not Applicable

## Yes

You have sent a freight document to a connected global trade services (GTS) application to perform a trade
compliance check. The GTS application checks the document and returns the result of the check, that is,
whether or not the freight document complies with the relevant international trade regulations.

The inbound operation Change Transportation Order Based on Trade Compliance Check Confirmation receives
the result of the check and updates the status of the freight document accordingly.

## Features

The inbound operation Change Transportation Order Based on Trade Compliance Check Confirmation receives
an indicator that specifies whether the freight document is compliant. It sets the status of the freight
document based on this value.

## Prerequisites

The Request Trade Compliance Check [page 23] outbound operation has requested a trade compliance check
for a freight document.

## Error Handling

## Forward Error Handling

The inbound operation Change Transportation Order Based on Trade Compliance Check Confirmation supports
Forward Error Handling (FEH). The following error categories are used:

● DCE: Determination and Conversion Error

● PRE: Processing Error

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

29


● PRE.TEE.LRE: Lock Request Error

For more information about the individual error categories, see the code list for the global data type
LogItemCategoryCode.

Notes on SAP Implementation

## Integration

The inbound operation Change Transportation Order Based on Trade Compliance Check Confirmation can
receive the result of a trade compliance check from the Confirm Trade Compliance Check outbound operation
in the Trade Compliance Processing process component. This enables you to receive the result of a trade
compliance check that was performed in the SAP Global Trade Services application for an SAP Transportation
Management (SAP TM) freight document.

When SAP TM receives the result of the check, it sets the compliance status of the freight document to
Compliant or Not Compliant. The system blocks a freight document that is relevant for the compliance check
until a trade compliance check has been performed and until the check determines that the document is
compliant.

## Configuration

For more information, see Trade Compliance Check Requesting Out [page 22].

## Enhancements

The Business Add-In (BAdI) BAdI for TradeComplianceCheckSUITEConfirmation_In (/SCMTMS/
CPC_SE_CPC_CNF) is available for this operation.

More Information

Trade Compliance Check

2.1.1.7

Intracompany Transportation Ordering In

## Definition

An interface to create, change, or cancel in-house transportation orders.

30

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


Technical Data

Entity Type

Category

## Direction

Business Context and Use

Service Interface

SAP A2A

## Inbound

The Intracompany Transportation Ordering In inbound service interface groups operations that create, change,
or cancel freight orders based on shipment data received from a logistics execution system. The freight orders
can be used for tendering or carrier selection, for example.

## Notes on SAP Implementation

In the SAP TM system, you have defined which freight order types the system uses to create freight orders
based on ERP shipments. You have the following options:

● You can assign freight order types to ERP shipment types in Customizing for Transportation Management

under

## Integration

ERP Logistics Integration Shipment Integration Assign Freight Order Types to

ERP Shipment Types .

● You can specify a default freight order type that the system uses if it cannot find an entry for an ERP

shipment type in the Customizing activity Assign Freight Order Types to ERP Shipment Types. To specify
the default freight order type, select the Default Type for ERP Shipment Integration checkbox in the relevant

freight order type in Customizing for Transportation Management under

## Freight Order Management

Freight Order Define Freight Order Types .

In the Define Freight Order Types Customizing activity, you have also configured the following settings for the
freight order type:

● You have assigned a suitable output profile to the relevant freight order type.

● You have specified that the freight order type is relevant for subcontracting.

● If you want the freight order to have the same ID as the ERP shipment, you have assigned an external

number range interval to the freight order type.

You define number range intervals in Customizing for Transportation Management under

## Freight Order

Freight Order Define Number Range Intervals for Freight Order Management

## Management
that the ERP shipment ID has not already been used in SAP TM for a different freight order, the external
number range interval from SAP ERP must not fall within the internal number range interval in SAP TM.

. To ensure

● If you want to display texts from an ERP shipment in the corresponding freight order in SAP TM, you have
to assign the relevant ERP text types to TM text types in Customizing for Transportation Management

under

## Integration

ERP Logistics Integration Shipment Integration Assign ERP Text Types to TM Text

Types for Freight Orders .

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

31


## More Information

Shipment-Based Tendering.

2.1.1.7.1

Maintain Transportation Order

## Definition

To create or change a transportation order of the category “freight order”.

Technical Data

Entity Type

Release State

Technical Name

## Namespace

Service Operation

## Released

TransportationOrderSCMRequest_In

http://sap.com/xi/TMS

Application Component

TM-FRM-FRO

Category

Direction

## Mode

## Idempotency

P2P Communication Enabled

Business Context and Use

SAP A2A

## Inbound

Asynchronous

No

## Yes

A shipper uses a transportation management system to perform tendering for shipments created in a logistics
execution system. The Maintain Transportation Order inbound operation creates or changes a freight order
based on shipment data received from a logistics execution system. The shipper can then perform
tendering for the freight order.

## Related Operations

● The Notify of Transportation Order Tendering Result [page 37] outbound operation informs the logistics

execution system about the result of the tendering process.

32

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


● The Cancel Transportation Order [page 34] inbound operation receives a request to cancel a freight order
that was created in the transportation management system based on shipment data received from the
logistics execution system.

## Features

The  Maintain Transportation Order inbound operation creates or changes a freight order using data received
from the sending system. This includes the following data:

● Parties involved (for example, shipper and consignee)

● Transportation stages and relevant dates (for example, pick-up and delivery dates)

● Means of transport

● Goods to be delivered, including quantity, weight, and volume

● Related business documents (for example, shipment number, shipment type, delivery IDs, and delivery

item IDs)

● Texts entered in the shipment (for example, shipping instructions)

## Error Handling

The  Maintain Transportation Order inbound operation supports Forward Error Handling. The following error
categories are used:

● PRE.TEE.LRE: Lock Error

● DCE: Conversion Error

● PRE: Processing Error

For more information about the individual error categories, see the code list for the global data type
LogItemCategoryCode.

## Message Types

● Transportation Order SCM Request

Notes on SAP Implementation

## Integration

You can use this operation to create freight orders in SAP Transportation Management (SAP TM) based on
shipments created in SAP ERP. When you initiate tendering for a shipment in SAP ERP, the SHPMNT05 IDoc
sends the shipment data to SAP TM. This triggers the Maintain Transportation Order inbound operation in SAP
TM.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

33


## Configuration

For more information, see the documentation of the Intracompany Transportation Ordering In [page 30]  In
inbound service interface.

## Enhancements

The BAdI for TransportationOrderSCMRequest_In (/SCMTMS/TOR_SE_TORSCM_RQ) Business Add-In (BAdI) is
available for this operation.

2.1.1.7.2

Cancel Transportation Order

## Definition

To cancel a transportation order of the category “freight order”.

Technical Data

Entity Type

Release State

Technical Name

## Namespace

Service Operation

## Released

TransportationOrderSCMCancellationRequest_In

http://sap.com/xi/TMS

Application Component

TM-FRM-FRO

Category

Direction

## Mode

## Idempotency

P2P Communication Enabled

Business Context and Use

SAP A2A

## Inbound

Asynchronous

No

## Yes

A shipper has sent a shipment from a logistics execution system to a transportation management system to
perform tendering for the shipment. If the shipper then cancels the tendering process or deletes the shipment
in the logistics execution system, the Cancel Transportation Order inbound operation cancels the freight order
that was created for the shipment in the transportation management system.

34

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## Features

The Cancel Transportation Order inbound operation receives the shipment number, based on which it cancels
the corresponding freight order.

## Error Handling

The Cancel Transportation Order inbound operation supports Forward Error Handling . The following error
categories are used:

● PRE.TEE.LRE: Lock Error

● DCE: Conversion Error

● PRE: Processing Error

For more information about the individual error categories, see the code list for the global data type
LogItemCategoryCode.

## Message Types

● Transportation Order SCM Cancellation Request

## Prerequisites

The Maintain Transportation Order [page 32] inbound operation has created a freight order based on a
shipment.

Notes on SAP Implementation

## Integration

You can use this operation in SAP Transportation Management (SAP TM) to receive cancellation requests from
SAP ERP. For more information, see Shipment-Based Tendering.

## Configuration

For more information, see the documentation of the Intracompany Transportation Ordering In [page 30]
 inbound service interface.

## Enhancements

The BAdI for TransportationOrderSCMCancellationRequest_In (/SCMTMS/TOR_SE_TORSCM_CNC) Business
Add-In (BAdI) is available for this operation.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

35


2.1.1.8

Intracompany Transportation Ordering Out

## Definition

An interface to send notifications in response to a request to create or change an in-house transportation
order.

Technical Data

Entity Type

Category

## Direction

Business Context and Use

Service Interface

SAP A2A

## Outbound

The Intracompany Transportation Ordering Out outbound service interface contains an operation that sends a
notification about the result of tendering for a freight order that was created based on shipment data received
from a logistics execution system.

Notes on SAP Implementation

## Integration

The operations in this interface and the Intracompany Transportation Ordering In [page 30]  inbound interface
can exchange data with IDocs in SAP ERP. This enables you to exchange data between the Freight Order
Management (TM-FRM) component in SAP Transportation Management (SAP TM) and the Logistics Execution
– Transportation (LE-TRA) component in SAP ERP.

Note that a freight order in the SAP TM back-end system corresponds to an instance of a Transportation Order
[page 6]  business object.

## Configuration

You have made the following settings in the SAP TM system:

● You have enabled PPF output agent /SCMTMS/TOR_TENDERING, which is used to send the tendering result

to SAP ERP. You do this in Customizing for Cross-Application Components under  Processes and Tools for

Enterprise Applications Reusable Objects and Functions for BOPF Environment PPF Adapter for Output

Management Maintain Output Management Adapter Settings . You have to enable the following entry:

○ Output Agent : /SCMTMS/TOR_TENDERING

36

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


○ Business Object : /SCMTMS/TOR

○ Node : TENDERING

○ Agent Class for BO Node : /SCMTMS/CL_PPF_SERV_TOR_TEND

● You have defined a logical system that represents the client from which the outbound communication is to
take place, and you have assigned a queue of the type  Outbound Queues  to this logical system. You do this

in Customizing for SCM Basis under

## Integration Basic Settings for Creating the System Landscape

Assign Logical System and Queue Type . Here, the logical system must be marked as an SAP system. Also
check the settings in the following Customizing activities:

○ Name Logical Systems

○ Assign Logical Systems to a Client

○ Maintain Business System Group

○ Settings for qRFC Communication

More Information

Shipment-Based Tendering

2.1.1.8.1

Notify of Transportation Order Tendering Result

## Definition

To send a notification about the result of a tendering process for a transportation order of the category “freight
order”.

Technical Data

Entity Type

Release State

Technical Name

Namespace

Category

Direction

## Mode

Service Operation

## Released

TransportationOrderSCMTenderingResultNotification_Out

http://sap.com/xi/TMS

SAP A2A

Outbound

## Asynchronous

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

37


## Idempotency

P2P Communication Enabled

No

## Yes

## Business Context and Use

A shipper has sent a shipment from a logistics execution system to a transportation management system to
perform tendering for the shipment. When the tendering step has been completed in the transportation
management system, the Notify of Transportation Order Tendering Result outbound operation sends the
tendering result to the logistics execution system, which updates the shipment accordingly.

## Features

If the tendering step was successful, the Notify of Transportation Order Tendering Result outbound operation
sends the following information to the receiving system:

● Carrier

● Price

● Confirmed dates and times

● Tendering status

If the tendering step was unsuccessful, the operation sends the tendering status only.

## Message Types

● Transportation Order SCM Tendering Result Notification

## Prerequisites

The Maintain Transportation Order [page 32] inbound operation has created a freight order based on a
shipment.

Notes on SAP Implementation

## Integration

You can use this operation to send the tendering result for a shipment from SAP Transportation Management
(SAP TM) to SAP ERP. When you award a quotation to a carrier or when you reject all quotations in the SAP TM

38

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


system, the Notify of Transportation Order Tendering Result outbound operation in SAP TM sends the tendering
result to SAP ERP. The SHPMNT05 IDoc in SAP ERP receives the tendering result and updates the shipment.

## Configuration

For more information, see the documentation of the Intracompany Transportation Ordering Out [page 36]
 outbound service interface.

## Enhancements

The BAdI for TranspOrderSCMTenderingResultNotification_Out (/SCMTMS/TOR_SE_TORSCM_TRN) Business
Add-In (BAdI) is available for this operation.

2.1.1.9

Transportation Generic Ordering In

## Definition

An interface to create, change, or cancel transportation orders of the category “freight order”, “freight
booking”, or “transportation unit”.

Technical Data

Entity Type

Category

## Direction

Business Context and Use

Service Interface

B2B

## Inbound

The Transportation Generic Ordering In inbound service interface contains an operation that creates, changes,
or cancels a freight order, a freight booking, or a transportation unit, based on freight planning data received
from a business partner. The business partner could be another carrier or another organizational unit within
the same company.

Notes on SAP Implementation

## Integration

If a communication partner also uses SAP Transportation Management (SAP TM), the operations in this
service interface exchange data with the operations in the Transportation Ordering Out outbound service

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

39


interface in the Transportation Order Processing process component of the partner’s system landscape.
Otherwise, the operations can exchange data with an equivalent third-party application that is being used by
the communication partner. Note that each of the documents that can be created by means of this service
interface corresponds to an instance of the Transportation Order business object.

More Information

## Freight Order Management

2.1.1.9.1  Maintain Generic Transportation Order

## Definition

To create, change, or cancel a transportation order of the category “freight order”, “freight booking”, or
“transportation unit”.

Technical Data

Entity Type

Release State

Technical Name

## Namespace

Application Component

Category

Direction

## Mode

Change/Update Behavior

P2P Communication Enabled

## Service Operation

Released with Restrictions

TransportationOrderGenericRequest_In

http://sap.com/xi/TMS/Global

TM-FRM

B2B

## Inbound

Asynchronous

Type 1

Yes

40

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## Business Context and Use

The Maintain Generic Transportation Order inbound operation receives a request to create, change, or cancel a
transportation order. This operation can be consumed by a communication partner either in a B2B scenario or
in an A2A scenario. The following highlight examples of these two scenarios:

● In a B2B scenario, the exchange of rail carrier waybills between rail carriers, or between a central

coordination agency and a rail carrier

● In an A2A scenario, the process of receiving new or updated transportation orders from an external

planning system in the system landscape of a carrier

Unlike most of the other inbound operations in the Transportation Order Processing process component, the
Maintain Generic Transportation Order inbound operation is not restricted to operate on transportation orders
of a specific category (for example, the category “freight booking”). This means that upon creation of a
transportation order, the consumer can specify the category of the new transportation order, and optionally
also its type. On the other hand, after successful creation of a transportation order, a subsequent inbound
operation that refers to the same document and that specifies a value of 02 for the actionCode attribute is
allowed to change any attribute of that document except for the transportation order category and the
transportation order type. An attempt to change the category or the type results in a rejection of the inbound
operation and an error message.

## Features

The Maintain Generic Transportation Order inbound operation receives data such as the following from the
sending system:

● The category of the transportation order that is to be created or changed

● Parties involved (for example, shipper and consignee).

Note that if address information is not yet known or differs from existing master data, the operation
automatically creates a deviating address in the background.

● A list of items that represent the goods to be transported and additional information about the goods (for
example, containers, packages, or products, with the respective measurements and quantities, such as
gross volume, gross weight, net weight, and number of pieces)

● Means of transport and locations, for example, ship-from and ship-to location, including address

information. Note that if address information is not yet known or differs from existing master data, the
operation automatically creates a one-time location in the background.

● Transportation stages and relevant dates (for example, pick-up and delivery dates)

● Transportation terms and delivery terms

● A reference to a predecessor document in the sending system

● IDs of other business documents related to the transportation order, for example, a sales order, a purchase

order, or an outbound delivery

● IDs of resources involved in the requested transport, for example, IDs of containers or railcars

● IDs of seals that have been applied to these resources

Depending on the configuration of the receiving system, a creation of a transportation order triggered by this
operation may also imply the creation of other documents in the receiving system and/or in connected
systems. For example, a forwarding order may be created automatically, or the creation of an export
declaration may be requested from a connected Global Trade Services (GTS) application.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

41


Notes on SAP Implementation

## Configuration

You have defined freight order types, freight booking types, and transportation unit types in Customizing. For
more information, see Freight Order Management.

2.1.1.10  Transportation Booking Out

## Definition

An interface to send or cancel transportation orders of the category “freight booking” and to send related
notifications.

Technical Data

Entity Type

Category

## Direction

Business Context and Use

Service Interface

B2B

## Outbound

The Transportation Booking Out outbound service interface groups operations that send freight booking data
to a carrier (for example, an ocean carrier or an airline).

Notes on SAP Implementation

## Integration

A freight booking in the SAP Transportation Management (SAP TM) back-end system corresponds to an
instance of a Transportation Order [page 6] business object.

## Configuration

You have made the following settings in the SAP TM system:

● You have defined one or more suitable output profiles, and schedule conditions that control whether a

message is sent. You do this in Customizing for Cross-Application Components under  Processes and

42

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


Tools for Enterprise Applications Reusable Objects and Functions for BOPF Environment PPF Adapter

for Output Management Maintain PPF Settings .
Note that output profile /SCMTMS/TOR is provided as part of the standard Customizing settings. This
profile is available in the configuration of PPF application /SCMTMS/TRANSPORTATION via the
subactivity Define Action Profile and Actions.

● You have assigned a suitable output profile to the relevant freight booking types. You define freight booking

types in Customizing for Transportation Management under  Transportation Management

Freight Order

## Management

Freight Booking Define Freight Booking Types .

● You have defined a logical system that represents the client from which the outbound communication is to
take place, and you have assigned a queue of the type Outbound Queues to this logical system. You do this

in Customizing for Transportation Management under  SCM Basis

Integration Basic Settings for

Creating the System Landscape Assign Logical System and Queue Type . Here, the logical system must
be marked as an SAP system. Also check the settings in the following Customizing activities: Name Logical
Systems, Assign Logical Systems to a Client, Maintain Business System Group , and Settings for qRFC
Communication .

For more information, see SAP Note 1517523

.

More Information

## Freight Booking

2.1.1.10.1  Request Transportation Order Booking

## Definition

To request the processing of a new or updated transportation order of the category “freight booking”.

Technical Data

Entity Type

Release State

Technical Name

Namespace

## Category

## Service Operation

Released with Restrictions

TransportationOrderBookingRequest_Out

http://sap.com/xi/TMS/Global

B2B

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

43


Entity Type

Direction

## Mode

## Idempotency

P2P Communication Enabled

Service Operation

Outbound

Asynchronous

No

## Yes

## Business Context and Use

A customer wants to book freight space, for example, on a specific voyage of a cargo ship run by an ocean
carrier, or on a specific flight of a cargo aircraft run by an air cargo carrier. To book the freight space, the
customer sends a freight booking to the carrier that specifies the goods to be transported, the capacity
requirements, the locations, and the delivery dates, for example. The Request Transportation Order Booking
outbound operation sends a freight booking to a carrier.

## Related Operations

● The Request Transportation Order Booking Cancellation [page 49] outbound operation informs a carrier

about a canceled freight booking.

● The Change Order Based on Transportation Order Booking Confirmation [page 52] inbound operation

receives a confirmation from a carrier about a freight booking that was sent using the Request
Transportation Order Booking  operation.

● The Notify of Transportation Order Booking Waybill [page 46] outbound operation notifies a carrier about
a waybill that has been issued. The notification contains more detailed information than the initial freight
booking.

## Features

The Request Transportation Order Booking  outbound operation sends data such as the following to the
receiving system:

● Parties involved (for example, shipper, consignee, and carrier)

● Items that are to be transported and the transportation stages, as well as the assignment of the items to

the transportation stages

● ID of the actual journey to which the freight booking relates (that is, the voyage number or the flight

number)

● Capacity requirements

● ID of the involved master waybill document, that is, a MBL number (ocean) or MAWB number (air)

● Weighing information for verified gross mass (VGM) – relevant for ocean only

For more information, see the documentation of the TranspOrdBkgReqMsg  message data type in SAP Note
1512334

.

44

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## Message Types

● Transportation Order Booking Request

Notes on SAP Implementation

## Integration

The Request Transportation Order Booking  outbound operation is triggered when a customer opens a freight
booking in the SAP Transportation Management (SAP TM) back-end system and then selects

Subcontracting Send to Carrier

.

You can change the Transport Mode by using BAdI: Adapt Transport Mode Code for Outbound B2B Services. For

more information see Customizing for Transportation Management under  Business Add-Ins (BAdIs) for

Transportation Management

## Integration

Enterprise Services

Freight Order Management

## Freight Booking

BAdI: Adapt Transport Mode Code for Outbound B2B Services .

As a prerequisite, you have configured an EDI communication profile to use the transport mode code BAdI and
assigned that profile to the carrier. For more information, see Customizing for Transportation Management

under

## Integration

Enterprise Services Define EDI Communication Profile .

You can run a completeness check before transferring data by using BAdI: Check Completeness Before Sending

B2B Services. For more information see Customizing for Transportation Management under  Business Add-

Ins (BAdIs) for Transportation Management

## Integration

Enterprise Services

## Freight Order Management

Freight Booking BAdI: Check Completeness Before Sending B2B Services .

## Configuration

For more information, see the documentation of the Transportation Booking Out [page 42] outbound interface.

## Prerequisites

To use this operation, the following requirements must be met:

● The freight order fulfills all schedule conditions that are checked at runtime. You define schedule
conditions in Customizing for Cross-Application Components. For more information, see the
documentation of the Transportation Booking Out [page 42] outbound service interface.

● A carrier has been assigned to the freight booking.

## Enhancements

The BAdI for TransportationOrderBookingRequest_Out (/SCMTMS/TOR_SE_TORB_REQ) Business Add-In (BAdI)
is available for this operation.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

45


2.1.1.10.2  Notify of Transportation Order Booking Waybill

## Definition

To send a notification about a waybill that is to be issued by a carrier. The information in the notification
enables a carrier to issue a waybill with reference to a confirmation of a transportation order of the category
“freight booking”, or with reference to a master bill of lading ID or a master air waybill number..

Technical Data

Entity Type

Release State

Technical Name

Namespace

Category

Direction

## Mode

## Idempotency

P2P Communication Enabled

## Service Operation

## Released with Restrictions

TransportationOrderBookingWaybillNotification

_Out

http://sap.com/xi/TMS/Global

B2B

Outbound

Asynchronous

No

## Yes

## Business Context and Use

A customer has already booked freight space (for example, on a specific voyage of a cargo ship run by an ocean
carrier, or on a specific flight of a cargo aircraft run by an air cargo carrier). The customer has also received a
confirmation from the carrier. At a later point in time, the customer collects additional information about the
goods to be transported and their packaging, such as detailed product IDs, batch numbers, container IDs, and
package numbers. This information can be shared with the carrier by means of a waybill notification message
(also known as a shipping instruction). In exceptional cases, It is also allowed to send a shipping instruction
without a preceding Request Transportation Order Booking operation and without receiving an explicit
confirmation beforehand. You can control this by setting the Send Shipping Instruction Only value in the
Message Sequence field of the relevant EDI communication profile.

The Notify of Transportation Order Booking Waybill  outbound operation sends a waybill notification to a carrier,
based on which the carrier can then create and issue a waybill.

46

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


 Note

The Notify of Transportation Order Booking Waybill  outbound operation can also be used to send freight
bookings to business partners involved in a role other than the carrier (for example, from one
organizational unit to another within the same company). For more information, see the documentation of
the Maintain Transportation Order Based On Transportation Order Booking Waybill Notification [page 55]
 inbound operation.

## Related Operations

● The Request Transportation Order Booking [page 43]  outbound operation sends a freight booking to a

carrier.

● The Change Order Based on Transportation Order Booking Confirmation [page 52]  inbound operation
receives a confirmation that indicates whether a carrier has accepted or rejected a freight booking that
was sent using the Request Transportation Order Booking [page 43]  operation.

● The Request Transportation Order Booking Cancellation [page 49]  outbound operation informs a carrier

about a canceled freight booking.

## Features

The Notify of Transportation Order Booking Waybill  outbound operation sends data such as the following to the
receiving system:

● ID of the freight booking from which the waybill notification is derived

● Booking number that has been received from the carrier as part of the freight booking confirmation

● Container IDs and package numbers

● References to export declarations

● Batch numbers or equivalent information (optional)

● References to documents of the type "house bill of lading" or "house air waybill" being consolidated (if

relevant)

● Weighing information for verified gross mass (VGM) – relevant for ocean only

For more information, see the documentation of the TranspOrdBkgWbillNotifMsg message data type in
SAP Note 1512334

.

## Message Types

● Transportation Order Booking Waybill Notification

## Prerequisites

The Change Order Based on Transportation Order Booking Confirmation [page 52]  inbound operation has
received a confirmation of a freight booking from a carrier.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

47


Alternatively, the confirmation may have been transmitted using a different communication channel (for
example, a fax transmission). In this case, the confirmation and also the booking number may have been
entered manually.

Notes on SAP Implementation

## Integration

The Notify of Transportation Order Booking Waybill  outbound operation is triggered when a customer opens a
freight booking in the SAP Transportation Management (SAP TM) back-end system and sends a shipping
instruction to a carrier.

You can also use this operation for export/import processing in SAP TM. If the export organization uses SAP
TM and the import organization uses an external application, the operation can be used to send freight
bookings from SAP TM to the external application. For more information, see Export/Import Processing:
External Communication (Outbound).

You can change the Transport Mode by using BAdI: Adapt Transport Mode Code for Outbound B2B Services. For

more information see Customizing for Transportation Management under  Business Add-Ins (BAdIs) for

Transportation Management

## Integration

Enterprise Services

Freight Order Management

## Freight Booking

BAdI: Adapt Transport Mode Code for Outbound B2B Services . As a prerequisite, you have configured an
EDI communication profile to use the transport mode code BAdI and assigned that profile to the carrier. For

more information, see Customizing for Transportation Management under

## Integration

## Enterprise Services

Define EDI Communication Profile .

You can run a completeness check before transferring data by using BAdI: Check Completeness Before Sending

B2B Services. For more information see Customizing for Transportation Management under  Business Add-

Ins (BAdIs) for Transportation Management

## Integration

Enterprise Services

## Freight Order Management

Freight Booking BAdI: Check Completeness Before Sending B2B Services .

## Configuration

For more information, see the documentation of the Transportation Booking Out [page 42]  outbound
interface.

## Versioning

The Notify of Transportation Order Booking Waybill  outbound operation performs a similar function to the
Notify of Waybill  outbound operation in SAP Transportation Management 7.0 (SAP TM 7.0).

## Enhancements

The BAdI for TransportationOrderBookingWaybillNotification_Out  (/SCMTMS/TOR_SE_TORBWBNT) Business
Add-In (BAdI) is available for this operation.

48

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


2.1.1.10.3  Request Transportation Order Booking

Cancellation

## Definition

To request the processing of a canceled transportation order of the category “freight booking”.

Technical Data

Entity Type

Release State

Technical Name

Namespace

Category

Direction

## Mode

## Idempotency

P2P Communication Enabled

## Service Operation

## Released with Restrictions

TransportationOrderBookingCancellationRequest_Out

http://sap.com/xi/TMS/Global

B2B

Outbound

Asynchronous

No

## Yes

## Business Context and Use

If a customer cancels a freight booking that has already been sent to a carrier (for example, an ocean carrier),
the Request Transportation Order Booking Cancellation  outbound operation informs the carrier about
the canceled freight booking.

## Features

The Request Transportation Order Booking Cancellation  outbound operation sends the ID of the canceled
freight booking to the receiving system. For more information, see the documentation of the
TranspOrdBkgCanclnReqMsg message data type in SAP Note 1512334

.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

49


## Message Types

● Transportation Order Booking Cancellation Request

## Prerequisites

The Request Transportation Order Booking [page 43]  outbound operation has sent a freight booking to a
carrier.

Notes on SAP Implementation

## Integration

In the standard SAP Transportation Management (SAP TM) back-end system, the Request Transportation
Order Booking Cancellation outbound operation is triggered when a customer cancels a freight booking that
has already been sent to a carrier. The customer can cancel a freight booking by selecting Cancel Document on
the freight booking user interface. The operation is also triggered if the carrier assigned to the freight booking
is changed or removed.

As stated above, this operation sends only the ID of the canceled freight booking to the receiving system. It
does not send the full set of attributes that describe the freight booking. However, some carriers might run
legacy systems that expect the full set of attributes to be transmitted, comprising the same scope of
information as the Request Transportation Order Booking [page 43] outbound operation. If this applies to
some or all of your business partners, you can use the enhancement spot /SCMTMS/OUTB_SPOT_TOR_B2B to
control in which situations the Request Transportation Order Booking [page 43] outbound operation is
triggered with an action code that specifies a deletion (thus sending what is referred to as a “cancellation with
content”) instead of the Request Transportation Order Booking Cancellation outbound operation (“lean
cancellation”) that is triggered in the standard system.

For more information, see SAP Note 1711010

.

Note that in simple scenarios, you can avoid using Business Add-In (BAdI) BAdI: Sending of B2B Cancellation
Messages with Document Content (/SCMTMS/TOR_OUTB_SEND_CNC_W_CO) by selecting Send Cancellation
with Full Content in the Booking Cancellation field of the EDI communication profile. However, if an active
implementation of this BAdI exists, it will override the setting in this field. For more information, see

Customizing for Transportation Management under

## Integration

Enterprise Services Define EDI

Communication Profile .

## Configuration

For more information, see the documentation of the Transportation Booking Out [page 42] outbound
service interface.

## Versioning

The Request Transportation Order Booking Cancellation  outbound operation performs a similar function to the
Request Booking Cancellation operation in SAP Transportation Management 7.0 (SAP TM 7.0).

Enhancements

50

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


The Business Add-In (BAdI) BAdI for TransportationOrderBookingCancellationRequest_Out (/SCMTMS/
TOR_SE_TORBCNCREQ) is available for this operation.

In addition, the BAdI BAdI: Sending of B2B Cancellation Messages with Document Content (/SCMTMS/
TOR_OUTB_SEND_CNC_W_CO) can be used to control whether the Request Transportation Order Booking [page
43] outbound operation is to replace the Request Transportation Order Booking Cancellation outbound
operation that is used in the standard system. Alternatively, you can use the EDI communciation profile to
control this (see section Integration above).

2.1.1.11  Transportation Booking In

## Definition

An interface to receive confirmations in response to a request to process a new or updated transportation
order of the category “freight booking”.

Technical Data

Entity Type

Category

## Direction

Business Context and Use

Service Interface

B2B

## Inbound

The Transportation Booking In  inbound service interface contains an operation that receives a confirmation
indicating whether a carrier has accepted or rejected a freight booking.

Note that in most cases, a confirmation is an answer to a TransportationOrderBookingRequest message. But in
exceptional cases, it can also be an answer to a TransportationOrderBookingWaybillNotification message.

Notes on SAP Implementation

## Integration

A freight booking in the SAP Transportation Management (SAP TM) back-end system corresponds to an
instance of a Transportation Order business object.

## Configuration

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

51


For more information, see the documentation of the Transportation Booking Out [page 42] outbound interface.

More Information

## Freight Booking

2.1.1.11.1  Change Order Based on Transportation Order

Booking Confirmation

## Definition

To change a transportation order of the category “freight booking” based on the confirmation of this
transportation order. The confirmation is either a reservation of freight space in response to the initial freight
booking request, or the rejection of a freight booking, or a preliminary response.

Technical Data

Entity Type

Release State

Technical Name

Namespace

Category

Direction

## Mode

## Idempotency

P2P Communication Enabled

Business Context and Use

## Service Operation

## Released with Restrictions

TransportationOrderBookingConfirmation_In

http://sap.com/xi/TMS/Global

B2B

## Inbound

Asynchronous

No

## Yes

When a customer sends a freight booking to a carrier (for example, an ocean carrier), the carrier is expected to
confirm if the freight booking was successful. The Change Order Based on Transportation Order Booking
Confirmation  inbound operation receives a confirmation that indicates whether a carrier has accepted or

52

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


rejected a freight booking. In addition, it is also possible to receive a preliminary response, for example, an
information about the booking request being placed on a waiting list.

## Features

The Change Order Based on Transportation Order Booking Confirmation  inbound operation receives an
acceptance code that specifies whether a carrier has accepted or rejected a freight booking. The operation can
receive the following data, for example:

● The cut-off date for verified gross mass (VGM) – relevant for ocean only

● If a carrier rejects a freight booking, the operation receives the rejection reason (for example, insufficient
capacity on the required dates). The operation updates the confirmation status of the freight booking to
Rejected.

● If a carrier accepts a freight booking without changes, the operation updates the confirmation status of the

freight booking to Confirmed.
For an air freight booking, the operation can also receive and update a space allocation advice code per
stage. Note that if the value of the space allocation advice code is KK (Confirming (confirmed by the
Airline)) for each stage, there is no need for the operation to set the confirmation status to Confirmed with
Changes.

● If a carrier accepts a freight booking but sends back changed data, the operation updates the confirmation

status of the freight booking to Confirmed with Changes. In this case, the operation also receives the
changed data, which it updates in the freight booking. It can receive the following data, for example:

○ Additional parties that the carrier has added to the freight booking

○ Changed transportation stages (for example, intermediate transportation stages that have been added

to the freight booking)

○ Changed quantities and capacity requirements (for example, if the carrier can only transport a partial

quantity)

● Where address information of carrier or execution carrier is not yet known or differs from existing master

data, the operation automatically creates a deviating address in the background.

For more information, see the documentation of the TranspOrdBkgConfMsg message data type in SAP Note
1512334

.

## Message Types

● Transportation Order Booking Confirmation

## Prerequisites

The Request Transportation Order Booking [page 43] outbound operation has sent a freight booking to a
carrier.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

53


Notes on SAP Implementation

## Integration

The Change Order Based on Transportation Order Booking Confirmation  inbound operation is triggered when a
confirmation of a freight booking is received from a carrier in the SAP Transportation Management (SAP TM)
back-end system.

Note that the carrier may use a different communication channel to confirm a freight booking (for example, a
fax transmission). In this case, the customer can enter the confirmation manually by choosing Confirm on the
freight booking user interface for an ocean booking or air booking. The customer can also enter the booking
number manually.

## Configuration

For more information, see the documentation of the Transportation Booking Out [page 42] outbound
service interface.

## Versioning

The Change Order Based on Transportation Order Booking Confirmation  inbound operation performs a similar
function to the Maintain Booking Confirmation  inbound operation in SAP Transportation Management 7.0 (SAP
TM 7.0).

## Enhancements

The BAdI for TransportationOrderBookingConfirmation_In (/SCMTMS/TOR_SE_TORB_CONF) Business Add-In
(BAdI) is available for this operation.

2.1.1.12  Transportation Booking Waybill In

## Definition

An interface to create transportation orders of the category “freight booking”.

Technical Data

Entity Type

Category

Direction

54

## P U B L I C

Service Interface

B2B

## Inbound

Enterprise Services and ESR Content
Enterprise Services


## Business Context and Use

The Transportation Booking Waybill In inbound service interface contains an operation that creates freight
bookings based on freight booking data received from a business partner, for example, another organizational
unit within the same company.

2.1.1.12.1  Maintain Transportation Order Based On

Transportation Order Booking Waybill Notification

## Definition

To create a transportation order of the category “freight booking” based on a notification about a waybill that
has been issued or is to be issued.

Technical Data

Entity Type

Release State

Technical Name

Namespace

Category

Direction

## Mode

## Idempotency

P2P Communication Enabled

Business Context and Use

## Service Operation

## Released with Restrictions

TransportationOrderBookingWaybillNotification_In

http://sap.com/xi/TMS/Global

B2B

## Inbound

Asynchronous

No

## Yes

A logistics service provider (LSP) needs to send a freight booking to a business partner. For example, the LSP
has an organizational unit (org. unit) in Europe that handles the pre-carriage and main carriage stages for a
specific freight booking, and an org. unit in the United States that handles the on-carriage stage. In this case,
the LSP sends the freight booking to the org. unit in the United States in order to provide the org. unit with
relevant information about the transportation of the goods. The Maintain Transportation Order Based On

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

55


Transportation Order Booking Waybill Notification  inbound operation receives the freight booking data and
creates a freight booking.

## Related Operations

In export/import processing, this operation can receive freight booking data sent by the Notify of
Transportation Order Booking Waybill [page 46] outbound operation.

## Features

The Maintain Transportation Order Based On Transportation Order Booking Waybill Notification  inbound
operation creates a freight booking by using data received from the sending system, such as the following:

● Freight booking ID

● Responsibility code that indicates who is responsible for the pre-carriage and on-carriage stages, and who

is responsible for the main carriage stage

● Items that are to be transported

● Capacity requirements

## Message Types

● Transportation Order Booking Waybill Notification

## Notes on SAP Implementation

A freight booking in the SAP Transportation Management (SAP TM) back-end system corresponds to an
instance of a Transportation Order [page 6] business object.

You can use this operation for export/import processing in SAP TM. If the import organization uses SAP TM
and the export organization uses an external application, the operation can be used to create import freight
bookings in SAP TM based on data received from the external application. For more information, see Export/
Import Processing: External Communication (Inbound).

## Enhancements

The BAdI for TransportationOrderBookingWaybillNotification_In (/SCMTMS/TOR_SE_TORWBNTF) Business Add-
In (BAdI) is available for this operation.

2.1.1.13  Transportation Order Execution Out

## Definition

An interface to request the execution of transportation orders.

56

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


Technical Data

Entity Type

Category

## Direction

Service Interface

SAP A2A

## Outbound

## Business Context and Use

The Transportation Order Execution Out outbound service interface groups operations that send freight
document data to a logistics execution system for further processing.

Notes on SAP Implementation

## Integration

The operations in this interface and the corresponding inbound service interface Transportation Order
Execution In [page 63] can exchange data with IDocs in SAP ERP. This enables you to exchange data between
the Freight Order Management (TM-FRM) component in SAP Transportation Management (SAP TM) and the
Logistics Execution - Transportation (LE-TRA) component in SAP ERP.

Note the following:

● A delivery-based transportation requirement in the SAP TM back-end system corresponds to an instance

of a Transportation Request [page 123] business object.

● A freight document in the SAP TM back-end system corresponds to an instance of a Transportation Order

[page 6] business object.

## Configuration

You have made the following message control settings in the SAP TM system:

● You have defined schedule conditions and one or more suitable output profiles that control whether a

message is sent. You do this in Customizing for Cross-Application Components under  Processes and

Tools for Enterprise Applications Reusable Objects and Functions for BOPF Environment PPF Adapter

for Output Management Maintain PPF Settings .

● You have assigned a suitable output profile to the relevant freight document types.

You define freight order types in Customizing for Transportation Management under  Transportation

## Management

## Freight Order Management

Freight Order Define Freight Order Types .

You define freight booking types in Customizing for Transportation Management under

Freight Order

## Management

Freight Booking Define Freight Booking Types .

● You have defined a logical system that represents the client from which the outbound communication is to
take place, and you have assigned a queue of the type Outbound Queues to this logical system. You do this

in Customizing for SCM Basis under

Integration Basic Settings for Creating the System Landscape

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

57


Assign Logical System and Queue Type . The logical system must be marked as an SAP system. Also
check the settings in the following Customizing activities: Name Logical Systems, Assign Logical Systems to
a Client, Maintain Business System Group, and Settings for qRFC Communication.

For more information, see SAP Note 1517523

.

## More Information

Shipment Integration Based on Freight Orders

Shipment Integration Based on Freight Bookings

2.1.1.13.1  Request Transportation Order Execution

## Definition

To request the execution of a transportation order of the category “freight order” or “freight booking”.

Technical Data

Entity Type

Release State

Technical Name

Namespace

Category

Direction

## Mode

## Idempotency

P2P Communication Enabled

Service Operation

## Released

TransportationOrderSCMExecutionRequest_Out

http://sap.com/xi/TMS

SAP A2A

Outbound

Asynchronous

No

Yes

58

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## Business Context and Use

After carrying out transportation planning for delivery-based transportation requirements (DTRs), a shipper
sends the resulting freight documents to a logistics execution system for further processing, for example, for
invoicing or output management.

The Request Transportation Order Execution outbound operation sends a freight document to a logistics
execution system and requests the execution of the freight document. To execute the freight document, the
logistics execution system can create a shipment, for example.

## Related Operations

● The Request Transportation Order Execution Cancellation [page 61] outbound operation informs the

logistics execution system about a canceled freight document.

● The Change Transportation Order based on Transportation Order Execution Confirmation [page 64]

 inbound operation receives a confirmation of the execution of a freight document.

● The Change Transportation Order based on Transportation Order Execution Status Notification [page 66]

inbound operation receives an update of the execution status of a freight document.

● The Change Transportation Order Based on Transportation Order Execution Delivery Assignment Changed

Notification [page 68] inbound operation receives information about changed delivery assignments.

● The Change Transportation Order Based on Transportation Order Execution Packaging Assignment

Changed Notification [page 70] inbound operation receives a notification about updated packaging and
item assignments.

## Features

The  Request Transportation Order Execution outbound operation sends data such as the following to the
receiving system:

● Parties (for example, shipper and consignee)

● Locations (for example, ship-from and ship-to location)

● Relevant dates (for example, pick-up and delivery dates)

● Means of transport

● IDs of the business documents related to the freight document, for example, the IDs of the deliveries based

on which a delivery-based transportation requirement was created

● Packaging information for vehicle resources or containers at the highest level of the item hierarchy (or for

both of these)
The operation sends the material ID of each relevant vehicle or container. Note that you can send
information only for the top level of the item hierarchy, and you cannot send information about the
assignment of the delivery items to the containers or vehicles.

## Message Types

● Transportation Order SCM Execution Request

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

59


Notes on SAP Implementation

## Integration

You can use this operation to send freight document data from SAP Transportation Management (SAP TM) to

## Follow Up Create/Update ERP Shipment
## SAP ERP. The operation is triggered when you select the action
in a freight order or freight booking. The SHPMNT05 IDoc in SAP ERP creates a shipment based on the freight
document.

If the freight document data includes packaging information, SAP ERP creates handling units based on this
information, using container as the packaging material. Note that you must send packaging information to SAP
ERP if you want to send the shipments from SAP ERP to the SAP Extended Warehouse Management (SAP
EWM) application to carry out warehouse planning and execution.

You can change the Transport Mode by using BAdI: Adapt Transport Mode Code for Outbound B2B Services. For

more information see Customizing for Transportation Management under  Business Add-Ins (BAdIs) for

Transportation Management

## Integration

Enterprise Services

Freight Order Management

## Freight Order

BAdI: Adapt Transport Mode Code for Outbound B2B Services . As a prerequisite, you have configured an EDI
communication profile to use the transport mode code BAdI and assigned that profile to the carrier. For more

information, see Customizing for Transportation Management under

## Integration

## Enterprise Services

Define EDI Communication Profile .

## Configuration

You have defined that freight documents are to be sent to SAP ERP by setting the required value in the
Shipment Creation Relevance field in Customizing for the freight document type. This setting also defines
whether packaging information is sent to SAP ERP. For more information, see the field help for the Shipment
Creation Relevance field.

In addition, the following requirements have been met:

● The freight document is derived from a delivery-based transportation requirement.

● The freight document is in process and does not have one of the following statuses:

○ Blocked for execution

○ Blocked for planning

○ Marked for deletion

For information about the required settings, see Shipment Integration Based on Freight Orders or Shipment
Integration Based on Freight Bookings.

For information about the required message control settings for outbound communication, see the
documentation of the Transportation Order Execution Out [page 56] outbound interface.

## Versioning

The Request Transportation Order Execution outbound operation performs a similar function to the Request
Freight Order Execution outbound operation in SAP Transportation Management 7.0 (SAP TM 7.0).

## Enhancements

The BAdI for TransportationOrderSCMExecutionRequest_Out (/SCMTMS/TOR_SE_SHPMNT_REQ) Business Add-
In (BAdI) is available for this operation.

60

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## More Information

Shipment Integration Based on Freight Orders

Shipment Integration Based on Freight Bookings

2.1.1.13.2  Request Transportation Order Execution

Cancellation

## Definition

To request the cancellation of the execution of a transportation order of the category “freight order” or “freight
booking”.

Technical Data

Entity Type

Release State

Technical Name

Namespace

Category

Direction

## Mode

## Idempotency

P2P Communication Enabled

Business Context and Use

Service Operation

## Released

TransportationOrderSCMExecutionCancellationRe­

quest_Out

http://sap.com/xi/TMS

SAP A2A

Outbound

Asynchronous

No

## Yes

A shipper has carried out transportation planning for delivery-based transportation requirements (DTRs) and
sent the resulting freight documents to a logistics execution system for further processing (for example, for
invoicing or output management). If the shipper then cancels a freight document, the Request Transportation
Order Execution Cancellation outbound operation informs the logistics execution system about the cancellation
and requests the cancellation of the execution of the freight document.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

61


The operation is also triggered if the shipper decides to send the freight document to a different logistics
execution system. In this case, the Request Transportation Order Execution Cancellation outbound
operation informs the previous logistics execution system about the cancellation.

## Features

The Request Transportation Order Execution Cancellation outbound operation sends the ID of the canceled
freight document to the logistics execution system.

## Message Types

● Transportation Order SCM Execution Cancellation Request

## Prerequisites

The Request Transportation Order Execution [page 58] outbound operation has sent a freight document to the
logistics execution system.

Notes on SAP Implementation

## Integration

You can use this operation to send cancellation data from SAP Transportation Management (SAP TM) to SAP
ERP. The operation is triggered when you cancel a freight order or freight booking that has already been sent to
SAP ERP using the Request Transportation Order Execution [page 58] outbound operation. The TPSSHT01
IDoc in SAP ERP cancels the corresponding shipment based on the cancellation request.

## Configuration

For information about the required message control settings for outbound communication, see the
documentation of the Transportation Order Execution Out [page 56] outbound service interface.

## Versioning

The Request Transportation Order Execution Cancellation outbound operation performs a similar function to
the Request Freight Order Execution Cancellation outbound operation in SAP Transportation Management 7.0
(SAP TM 7.0).

## Enhancements

The BAdI for TransportationOrderSCMExecutionCancellationReq_Out (/SCMTMS/TOR_SE_SHPMNT_CNC)
Business Add-In (BAdI) is available for this operation.

62

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## More Information

Shipment Integration Based on Freight Orders

Shipment Integration Based on Freight Bookings

2.1.1.14  Transportation Order Execution In

## Definition

An interface to receive confirmations of requests to execute transportation orders.

Technical Data

Entity Type

Category

## Direction

Business Context and Use

Service Interface

SAP A2A

## Inbound

The Transportation Order Execution In inbound service interface groups operations that receive confirmations
or notifications for freight documents that have been sent to a logistics execution system for further
processing.

## Notes on SAP Implementation

For more information, see the documentation of the Transportation Order Execution Out [page 56] outbound
interface.

## More Information

Shipment Integration Based on Freight Orders

Shipment Integration Based on Freight Bookings

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

63


2.1.1.14.1  Change Transportation Order Based on

Transportation Order Execution Confirmation

## Definition

To change a transportation order of the category “freight order” or “freight booking” based on the confirmation
of a request to execute this transportation order.

Technical Data

Entity Type

Release State

Technical Name

Namespace

Category

Direction

## Mode

## Idempotency

P2P Communication Enabled

Service Operation

## Released

TransportationOrderSCMExecutionConfirmation_In

http://sap.com/xi/TMS

SAP A2A

## Inbound

Asynchronous

No

## Yes

## Business Context and Use

A shipper has carried out transportation planning for delivery-based transportation requirements (DTRs)
and sent the resulting freight documents to a logistics execution system for further processing. To execute a
freight document, the logistics execution system has created a shipment, for example.

The Change Transportation Order Based on Transportation Order Execution Confirmation inbound operation
receives a confirmation of the execution of a freight document in the logistics execution system.

## Related Operations

The Change Transportation Order based on Transportation Order Execution Status Notification [page 66]
 inbound operation receives an update of the execution status of a freight document.

64

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## Features

The Change Transportation Order Based on Transportation Order Execution Confirmation inbound operation
receives the following data:

● ID of the document created in the logistics execution system (for example, shipment ID)

● Time at which the document was created

The operation assigns the document ID to the freight document.

## Message Types

● Transportation Order SCM Execution Confirmation

## Prerequisites

The Request Transportation Order Execution [page 58] outbound operation has sent a freight document to the
logistics execution system.

Notes on SAP Implementation

## Integration

You can use this operation to receive a confirmation from SAP ERP. SAP ERP sends a confirmation message
when the SHPMNT05 IDOC creates a shipment based on a request sent by the Request Transportation Order
Execution [page 58] outbound operation. Note that SAP ERP only sends a confirmation message if it has
created a shipment.

## Versioning

The Change Transportation Order Based on Transportation Order Execution Confirmation inbound operation
performs a similar function to the Change Freight Order Execution Based on Freight Order Execution
Confirmation inbound operation in SAP Transportation Management 7.0 (SAP TM 7.0).

## Enhancements

The BAdI for TransportationOrderSCMExecutionConfirmation_In (/SCMTMS/TOR_SE_SHPMNT_CNF) Business
Add-In (BAdI)  is available for this operation.

## More Information

Shipment Integration Based on Freight Orders

Shipment Integration Based on Freight Bookings

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

65


2.1.1.14.2  Change Transportation Order Based on

Transportation Order Execution Status
Notification

## Definition

To change a transportation order of the category “freight order” or “freight booking” based on a notification
about the status of the execution of this transportation order.

Technical Data

Entity Type

Release State

Technical Name

Namespace

Category

Direction

## Mode

## Idempotency

P2P Communication Enabled

Business Context and Use

Service Operation

## Released

TransportationOrderSCMExecutionStatusNotification_In

http://sap.com/xi/TMS

SAP A2A

## Inbound

Asynchronous

No

## Yes

A shipper has carried out transportation planning for delivery-based transportation requirements (DTRs) and
sent the resulting freight documents to a logistics execution system for further processing. The logistics
execution system has created a shipment for the freight document, for example. Relevant changes to the
execution status in the logistics execution system are received by the Change Transportation Order Based on
Transportation Order Execution Status Notification inbound operation.

66

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## Features

The Change Transportation Order based on Transportation Order Execution Status Notification inbound
operation receives data such as the following:

● ID of the document that the logistics execution system has created to execute the freight document (for

example, shipment ID) and the freight document to which it relates

● Timestamp of the status change

● An indicator that shows which status has been set in SAP ERP (for example, Planned)

## Message Types

● Transportation Order SCM Execution Status Notification

## Prerequisites

The Change Transportation Order Based on Transportation Order Execution Confirmation [page 64] inbound
operation has received a confirmation of the execution of the freight document in the logistics execution
system.

Notes on SAP Implementation

## Integration

You can use this operation to receive a status notification from SAP ERP. When the SHPMNT05 IDoc creates a
shipment based on a request sent by the Request Transportation Order Execution [page 58] outbound
operation, the overall transportation status of the shipment is set to Planned. This status is based on the
execution status Not Started in the corresponding freight document. As soon as the Planned status is set, SAP
ERP sends a status notification to SAP TM. Based on the notification, SAP TM changes the execution status of
the freight document from Not Started to In Execution. As soon as this status is set, the freight document is
blocked for further processing in SAP TM.

## Versioning

The Change Transportation Order based on Transportation Order Execution Status Notification inbound
operation performs a similar function to the Change Execution Status Based on Freight Order Execution Status
Notification inbound operation in SAP Transportation Management 7.0 (SAP TM 7.0).

## Enhancements

The Business Add-In (BAdI) BAdI for TranspOrderSCMExecutionStatusNotification_In (/SCMTMS/
TOR_SE_TORSCM_ST) is available for this operation.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

67


## More Information

Shipment Integration Based on Freight Orders

Shipment Integration Based on Freight Bookings

2.1.1.14.3  Change Transportation Order Based on

Transportation Order Execution Delivery
Assignment Changed Notification

## Definition

To change a transportation order of the category “freight order” or “freight booking” based on a notification
about changed delivery assignments.

Technical Data

Release State

Technical Name

## Namespace

Application Component

Category

Direction

## Mode

## Idempotency

Change/Update Behavior

P2P Communication Enabled

Business Context

## Released

TransportationOrderSCMExecutionDeliveryAssign

mentChangedNotification_In

http://sap.com/xi/TMS

TM-ERP-SHP

A2A

## Inbound

Asynchronous

No

Type 1

## Yes

A shipper has carried out transportation planning for delivery-based transportation requirements (DTRs) and
sent the resulting freight documents to a logistics execution system for further processing. The DTRs are based

68

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


on deliveries that were originally received from the logistics execution system. The logistics execution system
has created a shipment for each freight document. The deliveries that formed the basis of the DTRs are
automatically assigned to the corresponding shipment in the logistics execution system.

If a delivery is subsequently removed from or assigned to a shipment in the logistics execution system, the
corresponding freight document must be updated. The inbound operation Change Transportation Order Based
on Transportation Order Execution Delivery Assignment Changed Notification receives information about
changed delivery assignments and updates the freight document accordingly.

## Related Operations

The outbound operation Request Transportation Order Execution [page 58] sends a freight document to a
logistics execution system.

## Features

The inbound operation Change Transportation Order Based on Transportation Order Execution Delivery
Assignment Changed Notification receives the ID of the freight document that needs to be changed (for
example, the freight order ID) and the ID of the relevant delivery-based transportation requirement (DTR). It
also receives the information as to whether the DTR has to be removed from or assigned to the freight
document.

## Prerequisites

The inbound operation Change Transportation Order based on Transportation Order Execution Confirmation has
received a confirmation of the execution of the freight document in a logistics execution system.

## Error Handling

The inbound operation Change Transportation Order Based on Transportation Order Execution Delivery
Assignment Changed Notification supports Forward Error Handling. The following error categories are used:

● PRE.TEE.LRE: Lock Error

● DCE: Conversion Error

● PRE: Processing Error

For more information about the individual error categories, see the code list for the global data type
LogItemCategoryCode.

Notes on SAP Implementation

## Integration

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

69


You can use this operation to update freight documents in SAP Transportation Management (SAP TM) based
on data received from SAP ERP. SAP ERP uses IDoc SHPMNT05 to send changed delivery assignments to SAP
TM.

## Enhancements

The Business Add-In (BAdI) BAdI for TranspOrderSCMExecDeliveryAssignmentChngdNotif_In (/SCMTMS/
TOR_SE_TORSCM_ASG) is available for this operation.

## More Information

Shipment Integration Based on Freight Orders

Shipment Integration Based on Freight Bookings

2.1.1.14.4  Change Transportation Order Based on

Transportation Order Execution Packaging
Assignment Changed Notification

## Definition

To change a transportation order of the category “freight booking” or “freight order” based on a notification
about changed packaging and item assignments.

Technical Data

Release State

Technical Name

## Namespace

Application Component

Category

Direction

## Mode

Idempotency

70

P U B L I C

## Released

TransportationOrderSCMExecutionItmPckgAssgnmt

ChangedNotification_In

http://sap.com/xi/TMS

TM-ERP-SHP

A2A

## Inbound

Asynchronous

No

Enterprise Services and ESR Content
Enterprise Services


Change/Update Behavior

P2P Communication Enabled

Type 1

## Yes

## Business Context

A shipper performs transportation planning for a delivery-based transportation requirement (DTR) and sends
the resulting freight document to a logistics execution system for further processing. The logistics execution
system creates a shipment based on the freight document (see Request Transportation Order Execution [page
58]). If the freight document contains packaging information, the logistics execution system creates handling
units based on the packaging information.

When container IDs and items are assigned to the handling units, the Change Transportation Order Based on
Transportation Order Execution Packaging Assignment Changed Notification inbound operation receives a
notification about the updated packaging and item assignments from the logistics execution system.

## Features

The Change Transportation Order Based on Transportation Order Execution Packaging Assignment Changed
Notification inbound operation receives the IDs of the relevant containers, items, and handling units. It also
receives the material IDs that were sent to the logistics execution system by the Request Transportation Order
Execution [page 58] outbound operation.

Note that packaging information can be received only for the top level of the item hierarchy. For more
information, see the documentation of the Request Transportation Order Execution [page 58] outbound
operation.

## Prerequisites

The Request Transportation Order Execution [page 58] outbound operation has sent a freight document with
the required packaging information to the logistics execution system.

## Error Handling

## Forward Error Handling

The Change Transportation Order Based on Transportation Order Execution Packaging Assignment Changed
Notification operation supports Forward Error Handling. The following error categories are used:

● DCE: Determination and Conversion Error

● PRE: Processing Error

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

71


● PRE.TEE.LRE: Lock Request Error

For more information about the individual error categories, see the code list for the global data type
LogItemCategoryCode.

Notes on SAP Implementation

## Integration

You can use this operation to receive packaging and item assignment updates from SAP ERP. SAP ERP sends
the updates using IDoc SHPMNT05.

For more information about sending packaging information to SAP ERP, see the documentation of the Request
Transportation Order Execution [page 58] outbound operation.

## Enhancements

The Business Add-In (BAdI) BAdI for TranspOrderSCMExecutionItmPckgAssgnmtChngdNotif_In (/SCMTMS/
TOR_SE_TOR_PKGASG) is available for this operation.

## More Information

Shipment Integration Based on Freight Orders

Shipment Integration Based on Freight Bookings

2.1.1.15  Transportation Order Invoicing Preparation Out

## Definition

An interface to request the creation, change, or cancellation of business transaction documents that are
prerequisites for settling freight orders and forwarding orders.

Technical Data

Entity Type

Category

Direction

72

## P U B L I C

Service Interface

SAP A2A

## Outbound

Enterprise Services and ESR Content
Enterprise Services


## Business Context and Use

The Transportation Order Invoicing Preparation Out outbound service interface groups operations that send
transportation data to purchase order processing to enable invoice verification to be carried out for
subcontracted transportation services. The data is used to create, change, or cancel the documents required
for invoice verification.

Notes on SAP Implementation

## Integration

The operations in this interface can exchange data with the operations in the Transportation Processing In
interface in the Purchase Order Processing process component. This enables you to exchange data between the
Freight Settlement (TM-FRS) component in SAP Transportation Management (SAP TM) and the Invoice
Verification (MM-IV) component in  SAP ERP.

Note the following:

● A freight settlement document in the SAP TM back-end system corresponds to an instance of a Supplier

Freight Invoice Request [page 220]  business object.

● A freight settlement document is created based on one or more freight orders. A freight order corresponds

to an instance of a Transportation Order [page 6]  business object.

## Configuration

To carry out invoice verification in SAP ERP, you have to connect your SAP Transportation Management (SAP
TM) system to an SAP ERP system and make the required Customizing settings in both systems. For more
information about the Customizing settings, see Freight Settlement.

2.1.1.15.1  Request Transportation Order Invoicing Preparation

## Definition

To request the creation or change of business transaction documents that are prerequisites for settling freight
orders and forwarding orders.

Technical Data

Entity Type

Release State

## Service Operation

Released with Restrictions

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

73


Technical Name

## Namespace

Application Component

Category

Direction

## Mode

## Idempotency

## Change/Update Behavior

TransportationOrderSUITEInvoicingPreparationRequest_Out

http://sap.com/xi/TMS/Global

TM-FRS

SAP A2A

Outbound

Asynchronous

Not Applicable

## Not Applicable

P2P Communication Enabled

## Yes

## Business Context and Use

A shipper subcontracts transportation services to a carrier, for example. To perform freight settlement for the
subcontracted transportation services, the shipper creates a freight settlement document, which contains
details of the transportation services and the calculated transportation charges. To perform invoice
verification, the shipper transfers the freight settlement document to purchase order processing, which posts
the accruals and creates the required documents, that is, a service purchase order and one or more service
entry sheets.

The freight settlement document transfers a location identifier for the source location and destination location
of each stage in the settlement, in a charge item. This enables purchase order processing to determine
different tax rates for the service charges in the settlement, for different locations or countries. When the
invoice arrives, an invoicing clerk can verify the invoice against the data provided in the freight settlement
document.

The Request Transportation Order Invoicing Preparation  outbound operation sends a freight settlement
document to purchase order processing and requests the creation of the relevant documents.

## Related Operations

● The Maintain Purchase Order based on Order Invoicing Preparation Request inbound operation in the

Purchase Order Processing process component can receive a request from the Request Transportation
Order Invoicing Preparation outbound operation.

● If a shipper cancels a freight settlement document, the Request Transportation Order Invoicing
Preparation Cancellation [page 76] outbound operation requests the cancellation of the invoice
verification documents in purchase order processing.

● The Change based on Transportation Order Invoicing Preparation Confirmation [page 79] inbound
operation receives a confirmation of the creation, change, or cancellation of the invoice verification
documents in purchase order processing.

74

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## Features

The Request Transportation Order Invoicing Preparation operation sends data such as the following to purchase
order processing:

● ID of the freight settlement document for which the invoice verification documents are to be created

● Business elements that enable the creation of the invoice verification document, including the following:

○ Transportation services and the corresponding charges (TransportationCharge)

○ Relevant purchasing organization (PurchasingArea)

○ Bill-from party (BillFromParty)

○ Payee party (PayeeParty)

● Location identifiers that can be used to determine the tax code, as follows:

○ The identifier of a location (InternalID)

○ The address of a location (Address)

○ The loading location (ChargeRelevantLoadingLocationInternalID)

○ The unloading location (ChargeRelevantUnloadingLocationInternalID)

For more information, see the documentation of the
TransportationOrderSUITEInvoicingPreparationRequestMessage message data type in SAP Note 1512334

.

## Message Types

● Transportation Order SUITE Invoicing Preparation Request

## Prerequisites

The freight settlement document has the status Ready for Accruals.

Notes on SAP Implementation

## Configuration

For more information, see the documentation of the Transportation Order Invoicing Preparation Out [page 72]
outbound service interface.

## Versioning

The Request Transportation Order Invoicing Preparation outbound operation performs a similar function to the
Request Freight Order Invoicing Preparation outbound operation in SAP Transportation Management (SAP TM
7.0).

## Enhancements

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

75


The BAdI for TranspOrderSUITEInvoicingPreparationRequest_Out (/SCMTMS/SFI_SE_TORINPRCRT) Business
Add-In (BAdI) is available for this operation.

2.1.1.15.2  Request Transportation Order Invoicing Preparation

Cancellation

## Definition

To request the cancellation of business transaction documents that are prerequisites for settling freight and
forwarding orders.

Technical Data

Entity Type

Release State

Technical Name

## Service Operation

## Released with Restrictions

TransportationOrderSUITEInvoicingPreparationCancella­

tionRequest_Out

## Namespace

http://sap.com/xi/TMS/Global

Application Component

Category

Direction

## Mode

## Idempotency

Change/Update Behavior

TM-FRS

SAP A2A

Outbound

Asynchronous

Not Applicable

## Not Applicable

P2P Communication Enabled

## Yes

## Business Context and Use

A shipper performs invoice verification in purchase order processing as part of the freight settlement process
for transportation services subcontracted to a carrier, for example. If the shipper cancels a freight settlement
document, the Request Transportation Order Invoicing Preparation Cancellation outbound operation requests
the cancellation of the documents created in purchase order processing for the invoice verification process.

76

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## Related Operations

● The Cancel Purchase Order Based on Order Invoicing Preparation Cancellation Request inbound operation
in the Purchase Order Processing process component can receive a cancellation request from the Request
Transportation Order Invoicing Preparation Cancellation outbound operation.

● The Change Based on Transportation Order Invoicing Preparation Confirmation [page 79] inbound
operation receives a confirmation of the creation, change, or cancellation of the invoice verification
documents in purchase order processing.

## Features

The Request Transportation Order Invoicing Preparation Cancellation  outbound operation sends data such as
the following to purchase order processing:

● ID of the freight settlement document for which the invoice verification documents were created

● Requested cancellation date (optional)

For more information, see the documentation of the
TransportationOrderSUITEInvoicingPreparationCancellationRequestMessage message data type in SAP Note
1512334

.

## Message Types

● Transportation Order SUITE Invoicing Preparation Cancellation Request

## Prerequisites

The Request Transportation Order Invoicing Preparation [page 73] outbound operation has requested the
creation of the invoice verification documents.

Notes on SAP Implementation

## Configuration

For more information, see the documentation of the Transportation Order Invoicing Preparation Out [page 72]
outbound service interface.

## Versioning

The Request Transportation Order Invoicing Preparation Cancellation  outbound operation performs a similar
function to the Request Freight Order Invoicing Preparation Cancellation outbound operation in SAP
Transportation Management (SAP TM 7.0).

## Enhancements

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

77


The BAdI for TranspOrderSUITEInvoicingPreparationCancellatn_Out (/SCMTMS/SFI_SE_TORINPRCNCL) is
available for this operation.

2.1.1.16  Transportation Order Invoicing Preparation In

## Definition

An interface to receive confirmations of requests to prepare the settlement of freight and forwarding orders.

Technical Data

Entity Type

Category

## Direction

Business Context and Use

Service Interface

SAP A2A

## Inbound

The Transportation Order Invoicing Preparation In inbound service interface contains an operation that receives
a confirmation of the creation, change, or cancellation of documents that are required to carry out invoice
verification for subcontracted transportation services.

Notes on SAP Implementation

## Integration

The operations in this interface can exchange data with the operations in the Transportation Processing Out
outbound service interface in the Purchase Order Processing process component. This enables you to
exchange data between the Freight Settlement (TM-FRS) component in SAP Transportation Management (SAP
TM) and the Invoice Verification (MM-IV) component in SAP ERP.

## Configuration

For more information, see the documentation of the Transportation Order Invoicing Preparation Out [page 72]
 outbound service interface.

78

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


2.1.1.16.1  Change Based on Transportation Order Invoicing

Preparation Confirmation

## Definition

To change a freight or forwarding order based on the confirmation of the preparation of a settlement for a
freight or forwarding order.

Technical Data

Entity Type

Release State

Technical Name

## Service Operation

## Released with Restrictions

TransportationOrderSUITEInvoicingPreparationConfirma-

tion_In

## Namespace

http://sap.com/xi/TMS/Global

Application Component

## TM-FRS

Web Service Definition (Back End)

/SCMTMS/TOR_INVPREPCNF

Category

Direction

## Mode

## Idempotency

Change/Update Behavior

P2P Communication Enabled

Business Context and Use

SAP A2A

## Inbound

Asynchronous

Not Applicable

Type2

## Yes

A shipper performs invoice verification in purchase order processing as part of the freight settlement process
for transportation services subcontracted to a carrier, for example. The Change Based on Transportation Order
Invoicing Preparation Confirmation inbound operation receives a confirmation of the creation, change, or
cancellation of the documents required for invoice verification (that is, a service purchase order and one or
more service entry sheets).

## Related Operations

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

79


The Confirm Transportation Order Invoicing Preparation outbound operation in the  Purchase Order Processing
process component can send a confirmation of the creation, change, or cancellation of the invoice verification
documents.

## Features

The Change Based on Transportation Order Invoicing Preparation Confirmation inbound operation receives an
acceptance code that specifies whether the documents have been created, changed, or canceled. It updates
the freight settlement document as follows:

● If the documents have been created or changed, the operation receives the purchase order number and
the service entry sheet numbers. It updates the document numbers in the relevant freight settlement
document and changes the life cycle status of the freight settlement document to Accruals Posted.

● If the documents have not been created or changed, the operation changes the life cycle status of the

freight settlement document to Accruals Failed.

● If the documents have been canceled, the operation changes the life cycle status of the freight settlement
document to Canceled in ERP. If cancellation was unsuccessful, it changes the status to Cancellation
Failed.

For more information, see the documentation of the
TransportationOrderSUITEInvoicingPreparationConfirmationMessagemessage data type in SAP Note 1512334

.

## Message Types

● Transportation Order SUITE Invoicing Preparation Confirmation

## Prerequisites

The Request Transportation Order Invoicing Preparation [page 73] outbound operation has requested the
creation or change of the invoice verification documents, or the Request Transportation Order Invoicing
Preparation Cancellation [page 76] outbound operation has requested the cancellation of the invoice
verification documents.

Notes on SAP Implementation

## Configuration

For more information, see the documentation of the Transportation Order Invoicing Preparation Out [page 72]
 outbound service interface.

Enhancements

80

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


The BAdI for TranspOrderSUITEInvoicingPreparationConfirmation_In (/SCMTMS/SFI_SE_TORINPRCNF)
Business Add-In (BAdI) is available for this operation.

2.1.1.17  Transportation Order Loading Out

## Definition

An interface to request the creation, change, or cancellation of loading appointments for transportation orders
of the category “freight order” or “freight booking”.

Technical Data

Entity

Category

## Direction

Service Interface

B2B

## Outbound

## Business Context and Use

The Transportation Order Loading Out outbound interface contains an operation that requests a loading
appointment for a freight order or freight booking from a warehousing system.

Notes on SAP Implementation

## Integration

● A freight order or freight booking in the SAP TM back-end system corresponds to an instance of a

Transportation Order [page 6] business object.

● A loading instruction in the SAP TM back-end system corresponds to a loading appointment in the

Enterprise Services Repository and in the receiving application (for example, a warehousing application). In
this context, the term “loading instruction” is used for an instruction that can refer either to a loading
activity or to an unloading activity. These activities can also comprise coupling or decoupling activities.
Similar considerations apply to the term “loading appointment”.

● A loading instruction can only be sent if the status of the related freight order or freight booking is In

Execution or Ready for Execution. It always refers to loading or unloading activities that are about to take
place at the current stop of that freight order or freight booking, from an execution perspective.

● The recipient of a loading instruction is the party that operates a warehouse represented by the current
stop. If this party represents an organizational unit inside the company, then the outbound service

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

81


interface triggers an A2A communication (for example, with an SAP EWM system within the system
landscape of the company). If that party is outside the company, then the outbound service interface
triggers a B2B communication. In that case, the receiving application could be either an SAP EWM system
run by that external partner, or an equivalent third party component used by that partner.

## More Information

Message-Based Communication with a Warehouse Management System

2.1.1.17.1  Request Transportation Order Loading Appointment

## Definition

To request the creation or change of a loading appointment for a transportation order of the category “freight
order” or “freight booking”.

Technical Data

Entity Type

Release State

Technical Name

## Namespace

Application Component

Category

Direction

## Mode

P2P Communication Enabled

## Service Operation

## Released with Restrictions

TransportationOrderLoadingAppointmentRequest_

Out

http://sap.com/xi/TMS/Global

TM-FRM

B2B

Outbound

Asynchronous

Yes

82

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## Business Context and Use

A customer has planned a freight order or freight booking and wants to request a loading appointment during
which goods are to be loaded onto or unloaded from a resource. To request the loading appointment, the
customer sends the planning data for the freight order or freight booking to a warehousing system.

The Request Transportation Order Loading Appointment outbound operation sends the planning data to the
warehousing system.

## Related Operations

The Change Transportation Order Based on Transportation Order Loading Appointment Notification [page
85] inbound operation receives information about the loading appointment that has been allocated by a
warehousing system, and about the progress of loading or unloading activities.

## Features

The Request Transportation Order Loading Appointment outbound operation is triggered when a customer
requests a planned time slot for loading or unloading the goods in a freight order or freight booking. The
outbound operation sends loading appointment data for a freight order or freight booking to a warehousing
system to create or change the loading appointment and keep track of operations when loading or unloading
activities are carried out.

Notes on SAP Implementation

## Integration

The Request Transportation Order Loading Appointment outbound operation is triggered when a user opens a
freight order or freight booking in the SAP Transportation Management (SAP TM) back-end system and
performs one of the following actions:

● The user chooses the Send Loading/Unloading Instruction option from the Follow Up Actions dropdown

menu.
This option is only available if the Document Creation Relevance attribute of the relevant freight order type
or freight booking type has any value other than “E” (Transportation Activity Creation in SAP EWM), or else
if the Sending of the EWM Integration Profile attribute assigned to the relevant freight order type or freight
booking type has one of the values Manual Sending or Automatic and Manual Sending.

● The user chooses the

Load Plan Status Set Load Plan to Finalized  option and then saves the

document.

● The user chooses the

Load Plan Status Set Unload Plan to Finalized  option and then saves the

document.

The latter two options trigger a Request Transportation Order Loading Appointment outbound operation only if
the status of the related freight order or freight booking is In Execution or Ready for Execution, and if the
Document Creation Relevance attribute of the relevant freight order type or freight booking type has the value
“E” (Transportation Activity Creation in SAP EWM).

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

83


The actions mentioned above always refer to the current stop. If any of these actions is executed at different
points in time, they may trigger communication with different partners and with different content.

## Prerequisites

You have created a freight order or freight booking and entered the relevant planning data (for example, the
forwarding order items that are to be loaded or unloaded have been assigned to freight units).

## Enhancements

The Business Add-In (BAdI) BAdI for TransportationOrderLoadingAppointmentRequest_Out (/SCMTMS/
LA_REQ_OUTBD) is available for this operation.

2.1.1.18  Transportation Order Loading In

## Definition

An interface to receive confirmations of requests to create or change loading appointments for transportation
orders of the category “freight order” or “freight booking”, and to receive related notifications.

Technical Data

Entity

Category

## Direction

Service Interface

B2B

## Inbound

## Business Context and Use

The Transportation Order Loading In inbound interface contains an operation that receives confirmations of
requests to create or change a loading appointment for a freight order or freight booking in a warehousing
system.

Notes on SAP Implementation

## Integration

● A freight order or freight booking in the SAP TM back-end system corresponds to an instance of a

Transportation Order [page 6] business object.

● A loading instruction in the SAP TM back-end system corresponds to a loading appointment in the

Enterprise Services Repository and in the receiving application (for example, a warehousing application).

84

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## More Information

Message-Based Communication with a Warehouse Management System

2.1.1.18.1  Change Transportation Order Based on

Transportation Order Loading Appointment
Notification

## Definition

To change a transportation order of the category “freight order” or “freight booking” based on a notification
about a change to a loading appointment.

Technical Data

Entity Type

Release State

Technical Name

## Namespace

Application Component

Category

Direction

## Mode

P2P Communication Enabled

## Service Operation

## Released with Restrictions

TransportationOrderLoadingAppointmentNotifica

tion_In

http://sap.com/xi/TMS/Global

TM-FRM

B2B

## Inbound

Asynchronous

## Yes

## Business Context and Use

A customer has sent planning data for a freight order or freight booking to a warehousing system to request a
time slot for loading or unloading goods. Once the goods have been allocated to a resource in the warehousing
system, the Change Transportation Order Based on Transportation Order Loading Appointment Notification
inbound operation receives notification of which goods have actually been allocated to which resource.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

85


## Features

The Change Transportation Order Based on Transportation Order Loading Appointment Notification inbound
operation receives a notification about loading operations from a warehousing system with reference to a
Request Transportation Order Loading Appointment message that has been sent previously to that
warehousing system.

Notes on SAP Implementation

## Prerequisites

Planning data has been submitted to the warehousing system using the Request Transportation Order Loading
Appointment [page 82] outbound operation.

## Enhancements

The Business Add-In (BAdI) BAdI for TransportationOrderLoadingAppointmentNotification_In (/SCMTMS/
TOR_SE_TORLD) is available for this operation.

2.1.1.19  Transportation Ordering Out

## Definition

An interface to send or cancel transportation orders of the category “freight order”.

Technical Data

Entity Type

Category

## Direction

Business Context and Use

Service Interface

B2B

## Outbound

The Transportation Ordering Out outbound service interface groups operations that send freight order data
from a customer (for example, a shipper) to a carrier, based on which the carrier can create, update, or cancel a
forwarding order.

86

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


Note that the operations in this service interface can be used for direct tendering. The operations in the
Transportation Quotation Requesting Out [page 97]  outbound service interface and the Transportation
Quotation Requesting In [page 106] inbound service interface are used for RFQ-based tendering.

Notes on SAP Implementation

## Integration

● If a carrier also uses SAP Transportation Management (SAP TM), the operations in this interface exchange
data with the operations in the Transportation Requesting In [page 157]  inbound service interface in the
Transportation Request Processing [page 122] process component. Otherwise, the operations can
exchange data with an equivalent third-party application that is being used by the carrier.

● A freight order in the SAP TM back-end system corresponds to an instance of a Transportation Order [page

6] business object.

● A forwarding order in the SAP TM back-end system corresponds to an instance of a Transportation

Request [page 123] business object.

## Configuration

You have made the following settings in the SAP TM system:

● You have defined one or more suitable output profiles, and schedule conditions that control whether a

message is sent. You do this in Customizing for Cross-Application Components under  Processes and

Tools for Enterprise Applications Reusable Objects and Functions for BOPF Environment PPF Adapter

for Output Management Maintain PPF Settings .
Note that output profile /SCMTMS/TOR is provided as part of the standard Customizing settings. This
profile is available in the configuration of PPF application /SCMTMS/TRANSPORTATION via the subactivity
Define Action Profile and Actions.

● You have assigned a suitable output profile to the relevant freight order types. You define freight order

types in Customizing for Transportation Management under

Freight Order Management

## Freight Order

Define Freight Order Types .

● You have defined a logical system that represents the client from which the outbound communication is to
take place, and you have assigned a queue of the type Outbound Queues to this logical system. You do this

in Customizing for SAP Transportation Management under  SCM Basis

Integration Basic Settings for

Creating the System Landscape Assign Logical System and Queue Type . Here, the logical system must
be marked as an SAP system. Also check the settings in the following Customizing activities: Name Logical
Systems, Assign Logical Systems to a Client, Maintain Business System Group , and Settings for qRFC
Communication.

For more information, see SAP Note 1517523

.

More Information

Freight Order Management

## Tendering

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

87


2.1.1.19.1  Request Transportation Order

## Definition

To request the processing of a new or updated transportation order of the category “freight order”. The carrier
that receives and processes the transportation order can use the information provided to create or change a
corresponding transportation request of the category “forwarding order”.

Technical Data

Entity Type

Release State

Technical Name

## Namespace

Service Operation

## Released

TransportationOrderRequest_Out

http://sap.com/xi/TMS/Global

Application Component

TM-FRM-FRO

Category

Direction

## Mode

## Idempotency

Change/Update Behavior

B2B

Outbound

Asynchronous

Not Applicable

## Not Applicable

P2P Communication Enabled

## Yes

## Business Context and Use

When a customer subcontracts transportation services to a carrier, the customer sends a freight order to the
carrier. A freight order is the result of planning and contains essential information such as the goods to be
transported and the delivery dates. Based on the freight order, the carrier can then create a forwarding order,
which the carrier uses to plan the execution of the transportation services. The Request Transportation Order
outbound operation sends a new or updated freight order to a carrier, based on which the carrier’s system can
create or update a forwarding order.

The operation Request Transportation Order can also be sent out as a notification message for late changes. In
this case, the only purpose is a notification without triggering further subcontracting or direct tendering. The
prerequisites for this use are as follows:

88

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


● You have configured an EDI communication profile to send notifications and assigned that profile to the
carrier in business partner master data. For more information, see Customizing for Transportation

Management under

## Integration

Enterprise Services Define EDI Communication Profile .

● Determine the relevant freight orders in the BAdI “Trigger TransportationOrderRequest_Out as Notification

Message”. For more information see Customizing for Transportation Management under  Business Add-

Ins (BAdIs) for Transportation Management

## Integration

Enterprise Services

Freight Order

## Management

Freight Order BAdI: Trigger TransportationOrderRequest_Out as Notification Message .

## Related Operations

● The corresponding Maintain Transportation Request [page 158]  inbound operation in the Transportation

Request Processing [page 122]  process component can create a forwarding order based on a freight order
sent by the Request Transportation Order  outbound operation.

● The Request Transportation Order Cancellation [page 91]  outbound operation informs a carrier about a

canceled freight order.

● The Change Transportation Order Based on Transportation Order Confirmation [page 94]  inbound

operation receives a confirmation from a carrier about a freight order that was sent using the Request
Transportation Order  outbound operation.

## Features

The Request Transportation Order  outbound operation sends data such as the following to the receiving
system:

● Freight order ID

● Parties involved (for example, shipper and consignee)

● List of items that represent the goods to be transported and additional information about the goods (for
example, containers, packages, or products, with the respective measurements and quantities, such as
gross volume, gross weight, net weight, and number of pieces)

● Means of transport and locations (for example, ship-from and ship-to location, including address

information)

● Transportation stages and relevant dates (for example, pick-up and delivery dates)

● Transportation terms and delivery terms

● IDs of the business documents related to the freight order, for example, a sales order or purchase order

● Optionally, the detailed charge hierarchy created during charge calculation. Note that this information is

only provided if the following precondition is met:

○ You have configured an EDI communication profile to include charges and assigned that profile to the

carrier. For more information, see Customizing for Transportation Management under

## Integration

Enterprise Services Define EDI Communication Profile .

For more information, see the documentation of the TransportationDocumentRequestMessage message
data type in SAP Note 1512334

.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

89


## Message Types

● Transportation Order Request

Notes on SAP Implementation

## Integration

The Request Transportation Order outbound operation is triggered when a customer (for example, a shipper or
a logistics service provider) opens a freight order and then sends it to a carrier.

Note that you can use the Request Transportation Order outbound operation to send a freight order directly to a
carrier without using any of the tendering functions in SAP TM, or you can use the operation for direct
tendering. In this context, the Request Transportation Order outbound operation is sent as a separate award or
rejection message. In addition, if you carry out RFQ-based tendering in SAP TM, the Request Transportation
Order outbound operation is used to send a freight order to the successful carrier after you have
collected confirmations from the carriers who took part in the tendering step. For information about the
enterprise services used for RFQ-based tendering, see the documentation of the Request Transportation Order
Quotation Creation [page 98] outbound operation.

You can change the Transport Mode by using BAdI: Adapt Transport Mode Code for Outbound B2B Services. For

more information see Customizing for Transportation Management under  Business Add-Ins (BAdIs) for

Transportation Management

## Integration

Enterprise Services

Freight Order Management

## Freight Order

BAdI: Adapt Transport Mode Code for Outbound B2B Services .

As a prerequisite, you have configured an EDI communication profile to use the transport mode code BAdI and
assigned that profile to the carrier. For more information, see Customizing for Transportation Management

under

## Integration

Enterprise Services Define EDI Communication Profile .

You can run a completeness check before transferring data by using BAdI: Check Completeness Before Sending

B2B Services. For more information see Customizing for Transportation Management under  Business Add-

Ins (BAdIs) for Transportation Management

## Integration

Enterprise Services

## Freight Order Management

Freight Order BAdI: Check Completeness Before Sending B2B Services .

## Configuration

For more information, see the documentation of the Transportation Ordering Out [page 86]  outbound service
interface.

## Prerequisites

To use this operation, the following requirements must be met:

● The freight order fulfills all schedule conditions that are checked at runtime. You define schedule
conditions in Customizing for Cross-Application Components . For more information, see the
documentation of the Transportation Ordering Out [page 86] outbound service interface.

● A carrier has been assigned to the freight order.

## Versioning

The Request Transportation Order outbound operation performs a similar function to the Request Freight Order
and Request Shipment outbound operations in SAP Transportation Management 7.0 (SAP TM 7.0).

90

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


Note that in SAP TM 1.0, the Request Transportation Order outbound operation and the Maintain
Transportation Request [page 158] inbound operation shared a common message data type:
TransportationDocumentRequestMessage. As of SAP TM 1.01, however, these services use different message
data types that are similar in structure, but not identical. The outbound operation continues to use message
data type TransportationDocumentRequestMessage, whereas the inbound operation now uses a separate
message data type  TransportationRequestRequestMessage. As a consequence, a mapping between these
message data types is required. This mapping is usually implemented in the system landscape of the receiving
party, that is, the carrier.

## Enhancements

The BAdI for TransportationOrderRequest_Out (/SCMTMS/TOR_SE_TPNOR_REQ) Business Add-In (BAdI) is
available for this operation.

2.1.1.19.2  Request Transportation Order Cancellation

## Definition

To request the processing of a canceled transportation order of the category “freight order”.

Technical Data

Entity Type

Release State

Technical Name

## Namespace

Service Operation

## Released

TransportationOrderCancellationRequest_Out

http://sap.com/xi/TMS/Global

Application Component

TM-FRM-FRO

Category

Direction

## Mode

## Idempotency

Change/Update Behavior

B2B

Outbound

Asynchronous

Not Applicable

## Not Applicable

P2P Communication Enabled

## Yes

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

91


## Business Context and Use

If a customer cancels a freight order that has already been sent to a carrier, the Request Transportation Order
Cancellation  outbound operation informs the carrier about the cancellation and requests the cancellation of
the corresponding forwarding order.

## Related Operations

The Cancel Transportation Request [page 162] inbound operation in the Transportation Request Processing
[page 122] process component can cancel a forwarding order based on a freight order cancellation sent by the
Request Transportation Order Cancellation  outbound operation.

## Features

The Request Transportation Order Cancellation  outbound operation sends the following data to the receiving
system:

● ID of the canceled freight order

● ID of the forwarding order in the receiving system that was created based on the freight order (optional)

For more information, see the documentation of the
TransportationDocumentCancellationRequestMessage message data type in SAP Note 1512334

.

## Message Types

● Transportation Order Cancellation Request

## Prerequisites

The Request Transportation Order [page 88]  outbound operation has sent a freight order to a carrier.

Notes on SAP Implementation

## Integration

In the standard SAP Transportation Management (SAP TM) back-end system, the Request Transportation
Order Cancellation outbound operation is triggered when a customer cancels a freight order that has already
been sent to a carrier. The customer can cancel a freight order by selecting Cancel Document on the freight
order user interface. The operation is also triggered if the carrier assigned to the freight order is changed or
removed.

As stated above, this operation sends only the ID of the canceled freight order to the receiving system. It does
not send the full set of attributes that describe the freight order. However, some carriers might run legacy

92

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


systems that expect the full set of attributes to be transmitted, comprising the same scope of information as
the Request Transportation Order [page 88] outbound operation. If this applies to some or all of your business
partners, you can use the enhancement spot /SCMTMS/OUTB_SPOT_TOR_B2B to control in which situations
the Request Transportation Order [page 88] outbound operation is triggered with an action code that specifies
a deletion (thus sending what is referred to as a “cancellation with content”) instead of the Request
Transportation Order Cancellation outbound operation (“lean cancellation”) that is triggered in the standard
system.

For more information, see SAP Note 1711010

.

## Configuration

For more information, see the documentation of the Transportation Ordering Out [page 86]  service interface.

## Versioning

The Request Transportation Order Cancellation  outbound operation performs a similar function to the Request
Freight Order Cancellation and Request Shipment Cancellation outbound operations in SAP Transportation
Management 7.0 (SAP TM 7.0).

## Enhancements

The BAdI for TransportationOrderCancellationRequest_Out (/SCMTMS/TOR_SE_TPNOR_CNC) Business Add-In
(BAdI) is available for this operation.

In addition, the BAdI BAdI: Sending of B2B Cancellation Messages with Document Content (/SCMTMS/
TOR_OUTB_SEND_CNC_W_CO) can be used to control whether the Request Transportation Order [page 88]
outbound operation is to replace the Request Transportation Order Cancellation outbound operation that is
used in the standard system.

2.1.1.20  Transportation Ordering In

## Definition

An interface to receive confirmations in response to a request to process a new or updated transportation
order of the category “freight order”.

Technical Data

Entity Type

Category

## Direction

Service Interface

B2B

## Inbound

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

93


## Business Context and Use

The Transportation Ordering In inbound service interface contains an operation that receives a confirmation
indicating whether a carrier has accepted or rejected a freight order sent by a customer (for example, a
shipper).

Notes on SAP Implementation

## Integration

If a carrier also uses SAP Transportation Management (SAP TM), the operation in this interface exchanges data
with the operation in the Transportation Requesting Out [page 164] outbound service interface in the
Transportation Request Processing [page 122] process component. Otherwise, the operation exchanges data
with an equivalent third-party application that is being used by the carrier.

For more information about integration and configuration, see the documentation of the Transportation
Ordering Out [page 86] outbound interface.

More Information

## Freight Order Management

2.1.1.20.1  Change Transportation Order Based on

Transportation Order Confirmation

## Definition

To change a transportation order of the category “freight order” based on the confirmation of this
transportation order.

Technical Data

Entity Type

Release State

Technical Name

94

## P U B L I C

Service Operation

## Released

TransportationOrderConfirmation_In

Enterprise Services and ESR Content
Enterprise Services


Entity Type

## Namespace

## Service Operation

http://sap.com/xi/TMS/Global

Application Component

TM-FRM-FRO

Category

Direction

## Mode

## Idempotency

Change/Update Behavior

B2B

## Inbound

Asynchronous

Not Applicable

## Not Applicable

P2P Communication Enabled

## Yes

## Business Context and Use

When a customer sends a freight order to a carrier, the carrier is expected to send back a confirmation that
indicates whether the freight order has been accepted or rejected. The Change Transportation Order Based on
Transportation Order Confirmation inbound operation receives the confirmation from the carrier and updates
the required data in the freight order.

## Related Operations

The  Confirm Transportation Request [page 165] outbound operation in the Transportation Request Processing
[page 122] process component can send the confirmation that is received by the Change Transportation Order
Based on Transportation Order Confirmation inbound operation.

## Features

The Change Transportation Order Based on Transportation Order Confirmation  inbound operation receives an
acceptance code that specifies whether a carrier has accepted or rejected a freight order. The operation can
receive the following data, for example:

● If a carrier rejects a freight order, the operation receives the rejection reason. The operation updates the

confirmation status of the freight order to Rejected.

● If a carrier accepts a freight order without changes, the operation receives the ID of the forwarding order

and the confirmed quantities and dates, for example. The operation updates the confirmation status of the
freight order to Confirmed.

● If a carrier accepts a freight order with changes, the operation receives the ID of the forwarding order and
the changed data, for example, changed quantities or dates. It updates the data in the freight order and
changes the confirmation status to Confirmed with Changes.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

95


● Optionally, in a direct tendering process, if a carrier accepts a freight order that specifies a detailed charge

hierarchy, the operation also receives the confirmed rates and related quantities within the charge
hierarchy.

● Where address information of carrier or execution carrier is not yet known or differs from existing master

data, the operation automatically creates a deviating address in the background.

For more information, see the documentation of the TransportationDocumentConfirmationMessagemessage
data type in SAP Note 1512334

.

## Message Types

● Transportation Order Confirmation

## Prerequisites

The Request Transportation Order [page 88] outbound operation has sent a freight order to a carrier.

Notes on SAP Implementation

## Integration

The Change Transportation Order Based on Transportation Order Confirmation inbound operation is triggered
when a confirmation of a freight order is received from a carrier.

## Configuration

For more information, see the documentation of the Transportation Ordering Out [page 86] service interface.

## Versioning

The Change Transportation Order Based on Transportation Order Confirmation inbound operation performs a
similar function to the Maintain Freight Order Confirmation  and Maintain Shipment Confirmation
inbound operations in SAP Transportation Management 7.0 (SAP TM 7.0).

Note that in SAP TM 1.0, the Confirm Transportation Request [page 165] outbound operation and the Change
Transportation Order Based on Transportation Order Confirmation inbound operation shared a common
message data type: TransportationDocumentConfirmationMessage. As of SAP TM 1.01,
however, these operations use different message data types that are similar in structure, but not identical. The
inbound operation continues to use message data type TransportationDocumentConfirmationMessage,
whereas the outbound operation now uses a separate message data
type TransportationRequestConfirmationMessage. As a consequence, a mapping between these message data
types is required. This mapping for a confirmation message is usually implemented in the system landscape of
the sending party, that is, the carrier.

Enhancements

96

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


The BAdI for TransportationOrderConfirmation_In (/SCMTMS/TOR_SE_TPNOR_CNF) Business Add-In (BAdI) is
available for this operation.

2.1.1.21  Transportation Quotation Requesting Out

## Definition

An interface to send or cancel transportation orders of the category “freight request for quotation”.

Technical Data

Entity Type

Category

## Direction

Business Context and Use

Service Interface

B2B

## Outbound

The Transportation Quotation Requesting Out outbound service interface groups operations that send freight
request for quotation (RFQ) data to a carrier during a tendering process started by a customer (for example, a
shipper).

Note that the operations in this service interface are only used for RFQ-based tendering. The operations in the
Transportation Ordering Out [page 86] outbound service interface and the Transportation Ordering In [page
93] inbound service interface are used for direct tendering.

Notes on SAP Implementation

## Integration

● If a carrier also uses SAP Transportation Management (SAP TM), the operations in this service interface
exchange data with the operations in the Transportation Quotation Requesting In [page 148] inbound
service interface in the Transportation Request Processing [page 122]  process component. Otherwise, the
operations can exchange data with an equivalent third-party application that is being used by the carrier.

● A freight request for quotation in the SAP TM back-end system corresponds to an instance of a

Transportation Order [page 6] business object.

● A forwarding quotation in the SAP TM back-end system corresponds to an instance of a Transportation

Request [page 123] business object.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

97


## Configuration

You have made the following settings in the SAP TM system:

● You have defined schedule conditions that control whether a message is sent. You do this in Customizing

for Cross-Application Components under  Processes and Tools for Enterprise Applications Reusable

Objects and Functions for BOPF Environment PPF Adapter for Output Management Maintain PPF

Settings .

● You have enabled the creation of outbound messages for tendering in Customizing for Transportation

Management under

## Freight Order Management

Tendering Define General Settings for Tendering .

● You have defined a logical system that represents the client from which the outbound communication is to
take place, and you have assigned a queue of the type Outbound Queues to this logical system. You do this

in Customizing for SAP Transportation Management under  SCM Basis

Integration Basic Settings for

Creating the System Landscape Assign Logical System and Queue Type . Here, the logical system must
be marked as an SAP system. Also check the settings in the following Customizing activities: Name Logical
Systems, Assign Logical Systems to a Client, Maintain Business System Group , and Settings for qRFC
Communication.

● You have verified the configuration settings under  Cross-Application Components Processes and Tools

for Enterprise Applications Reusable Objects and Functions for BOPF Environment PPF Adapter for

Output Management Maintain Output Management Adapter Settings .
Action profile /SCMTMS/TOR_TENDREQ is provided in the standard Customizing settings and assigned to
node TENDERINGREQUEST of business object /SCMTMS/TOR. If required, you can replace this assignment
by specifying another suitable action profile. Note that removing this assignment without replacing it with
another one would disable outbound communication via the Transportation Quotation Requesting Out
outbound service interface.

For more information, see SAP Note 1517523

.

More Information

## Tendering

2.1.1.21.1  Request Transportation Order Quotation Creation

## Definition

To request the processing of a new transportation order of the category “freight request for quotation”. The
carrier that receives and processes the transportation order can use the information provided to create a
corresponding transportation request of the category “forwarding quotation”.

98

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


Technical Data

Entity Type

Release State

Technical Name

## Namespace

Service Operation

## Released

TransportationOrderQuotationCreateRequest_Out

http://sap.com/xi/TMS/Global

Application Component

TM-FRM-FRT

Category

Direction

## Mode

Idempotency

B2B

Outbound

Asynchronous

## Not Applicable

P2P Communication Enabled

## Yes

## Business Context and Use

As a transportation planner or a dispatcher (that is, an employee of a company acting as a shipper or a logistics
service provider), you use RFQ-based tendering to determine which carrier is to execute a particular freight
order. You start the tendering process for a freight order by sending a freight request for quotation (RFQ) to one
or more carriers. The RFQ contains relevant data from the freight order, for example, quantities and delivery
dates. Based on this, the carrier can decide whether to submit a quotation or reject the RFQ. The Request
Transportation Order Quotation Creation outbound operation sends a new freight request for quotation to a
carrier, based on which the carrier’s system can create a forwarding request quotation. The carrier can then
review the forwarding request for quotation and either accept it (that is, submit a forwarding quotation) or
reject it.

## Related Operations

In the system of the requesting company (that is, shipper or logistics service provider), the following operations
can also be used:

● The Request Transportation Order Quotation Cancellation [page 101] outbound operation informs a

carrier about a canceled freight request for quotation.

● The Change Transportation Order Based on Transportation Order Quotation Confirmation [page 107]

inbound operation receives a confirmation from a carrier about a freight request for quotation that was
sent using the Request Transportation Order Quotation Creation   outbound operation.

In the carrier's system (if the carrier also uses SAP TM), the corresponding Create Transportation Request
Quotation [page 149] inbound operation in the Transportation Request Processing [page 122] process
component can create a forwarding request for quotation based on the freight request for quotation sent by
the Request Transportation Order Quotation Creation outbound operation.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

99


## Features

The Request Transportation Order Quotation Creation outbound operation sends data such as the following to
the receiving system:

● Price limit

● Parties involved (for example, shipper and consignee)

● List of items that represent the goods to be transported and additional information about the goods (for
example, containers, packages, or products, with the respective measurements and quantities, such as
gross volume, gross weight, net weight, and number of pieces)

● Means of transport and locations (for example, ship-from and ship-to location, including address

information)

● Transportation stages and relevant dates (for example, pick-up and delivery dates)

● Transportation terms and delivery terms

● Optionally, the detailed charge hierarchy created during charge calculation. Note that this information is

only provided if, for the tendering step, you assigned a tendering profile that specifies the required value for
the Price Details attribute.

For more information, see the documentation for the
TransportationDocumentQuotationCreateRequestMessage message data type in SAP Note 1512334

.

## Message Types

● Transportation Order Quotation Create Request

Notes on SAP Implementation

## Integration

The Request Transportation Order Quotation Creation outbound operation is triggered when the tendering
process is started manually or automatically for a freight order in the SAP Transportation Management (SAP
TM) back-end system.

You can change the Transport Mode by using BAdI: Adapt Transport Mode Code for Outbound B2B Services. For

more information see Customizing for Transportation Management under  Business Add-Ins (BAdIs) for

Transportation Management

## Integration

Enterprise Services

Freight Order Management

## Freight Request

for Quotation  BAdI: Adapt Transport Mode Code for Outbound B2B Services . As a prerequisite, you have
configured an EDI communication profile to use the transport mode code BAdI and assigned that profile to the

carrier. For more information, see Customizing for Transportation Management under

## Integration

Enterprise Services Define EDI Communication Profile .

You can run a completeness check before transferring data by using BAdI: Check Completeness Before Sending

B2B Services. For more information see Customizing for Transportation Management under  Business Add-

Ins (BAdIs) for Transportation Management

## Integration

Enterprise Services

## Freight Order Management

Freight Request for Quotation  BAdI: Check Completeness Before Sending B2B Services .

100

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## Configuration

For more information, see the documentation of the Transportation Quotation Requesting Out [page 97]
outbound interface.

## Prerequisites

To use this operation, the following requirements must be met in addition those mentioned in the Configuration
section of the Transportation Quotation Requesting Out [page 97] outbound service interface:

● The freight request for quotation must fulfill all schedule conditions that are checked at runtime. You define
schedule conditions in Customizing for Cross-Application Components . For more information, see the
documentation of the Transportation Quotation Requesting Out [page 97]  outbound service interface.

● The freight order for which tendering is to be carried out must have the status In Process.

## Versioning

The Request Transportation Order Quotation Creation outbound operation performs a similar function to the
Request Shipment Quote and Request Freight Quote outbound operations in SAP Transportation Management
7.0 (SAP TM 7.0).

Note that in SAP TM 1.0, the Request Transportation Order Quotation Creation  outbound operation and the
Create Transportation Request Quotation [page 149]  inbound operation shared a common message data type:
TransportationDocumentQuotationCreateRequestMessage. As of SAP TM 1.01, however, these operations use
different message data types that are similar in structure, but not identical. The outbound operation continues
to use message data type TransportationDocumentQuotationCreateRequestMessage, whereas the inbound
operation now uses a separate message data type TransportationRequestQuotationCreateRequestMessage. As
a consequence, a mapping between these message data types is required. This mapping is usually
implemented in the system landscape of the receiving party, that is, the carrier.

## Enhancements

The BAdI for TransportationOrderQuotationCreateRequest_Out (/SCMTMS/TOR_SE_TPNORQ_REQ) Business
Add-In (BAdI) is available for this operation.

2.1.1.21.2  Request Transportation Order Quotation

Cancellation

## Definition

To request the processing of a canceled transportation order of the category “freight request for quotation”.

Technical Data

Entity Type

Release State

Service Operation

## Released

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

101


Technical Name

## Namespace

TransportationOrderQuotationCancellationRequest_Out

http://sap.com/xi/TMS/Global

Application Component

TM-FRM-FRT

Category

Direction

## Mode

Idempotency

B2B

Outbound

Asynchronous

## Not Applicable

P2P Communication Enabled

## Yes

## Business Context and Use

A customer uses RFQ-based tendering to determine which carrier is to execute a particular freight order. If the
customer cancels a freight request for quotation that has already been sent to a carrier, the Request
Transportation Order Quotation Cancellation outbound operation informs the carrier about the cancellation and
requests the cancellation of the corresponding forwarding request for quotation or forwarding quotation.

## Related Operations

The Cancel Transportation Request Quotation [page 152] inbound operation in the Transportation Request
Processing [page 122] process component can cancel a forwarding quotation based on a canceled freight
request for quotation sent by the Request Transportation Order Quotation Cancellation  outbound operation.

## Features

The Request Transportation Order Quotation Cancellation  outbound operation sends data such as the
following to the receiving system:

● ID of the canceled freight request for quotation

● ID of the forwarding quotation in the receiving system that was created based on the freight request for

quotation (optional)

For more information, see the documentation of the
TransportationDocumentQuotationCancellationRequestMessage message data type in SAP Note 1512334

.

## Message Types

● Transportation Order Quotation Cancellation Request

102

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## Prerequisites

The Request Transportation Order Quotation Creation [page 98] outbound operation has sent a freight request
for quotation to one or more carriers.

Notes on SAP Implementation

## Integration

The Request Transportation Order Quotation Cancellation outbound operation is triggered in the SAP
Transportation Management (SAP TM) back-end system when a customer stops the tendering process. This
results in the cancellation of all freight requests for quotation that have been sent to carriers during this
tendering process.

## Configuration

For more information, see the documentation of the Transportation Quotation Requesting Out [page 97]
outbound interface.

## Versioning

The Request Transportation Order Quotation Cancellation outbound operation performs a similar function to
the Request Freight Quote Cancellation and Request Shipment Quote Cancellation outbound operations in SAP
Transportation Management 7.0 (SAP TM 7.0).

## Enhancements

The BAdI for TransportationOrderQuotationCancellationRequest_Out (/SCMTMS/TOR_SE_TPNORQ_CNC)
Business Add-In (BAdI) is available for this operation.

2.1.1.21.3  Notify of Transportation Order Quotation

## Definition

To send a notification about a transportation order of the category "freight quotation".

Technical Data

Entity Type

Release State

Technical Name

## Service Operation

## Released with Restrictions

TransportationOrderQuotationNotification_Out

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

103


Entity Type

## Namespace

## Service Operation

http://sap.com/xi/TMS/Global

Application Component

TM-FRM-FRT

Category

Direction

## Mode

Idempotency

B2B

Outbound

Asynchronous

## Not Applicable

P2P Communication Enabled

## Yes

## Business Context and Use

A customer uses RFQ-based tendering to determine which carrier is to execute a particular freight order. When
the customer sends a freight request for quotation to a carrier, the carrier can either accept it by submitting a
quotation, or reject it. In return the customer uses the Notify of Transportation Order Quotation outbound
operation to notify the carrier that the quotation has been awarded or rejected.

## Related Operations

In the system of the requesting company (that is, shipper or logistics service provider), the following operations
can also be used:

● The Request Transportation Order Quotation Creation [page 98] outbound operation sends a freight

request for quotation to one or more carriers.

● The Request Transportation Order Quotation Cancellation [page 101] outbound operation informs a carrier

about a canceled freight request for quotation.

● The Change Transportation Order Based on Transportation Order Quotation Confirmation [page 107]

inbound operation receives a confirmation from a carrier about a freight request for quotation that was
sent using the Request Transportation Order Quotation Creation   outbound operation.

In the carrier's system (if the carrier also uses TM), the corresponding Create Transportation Request
Quotation [page 149] inbound operation in the Transportation Request Processing [page 122] process
component can create a forwarding request for quotation based on the freight request for quotation sent by
the Request Transportation Order Quotation Creation outbound operation.

## Features

The Notify of Transportation Order Quotation outbound operation sends data such as the following to the
receiving system:

● ID of the freight quotation

104

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


● Award status of the quotation

● ID of the freight request for quotation

For more information, see the documentation of the TransportationOrderQuotationNotification_Out
message data type in SAP Note 2474555

.

## Message Types

Transportation Order Quotation Notification

## Prerequisites

The Request Transportation Order Quotation Creation outbound operation has sent a freight request for
quotation to one or more carriers.

You have configured communications settings or carrier-specific communication settings to send EDI

messages of type Notification Messages in Customizing under

 Transportation Management

## Freight Order

## Management Tendering

 Define General Settings for Tendering .

Notes on SAP Implementation

## Integration

The Notify of Transportation Order Quotation outbound operation is triggered in the Transportation
Management (TM) back-end system when the quotation is rewarded or rejected.

You can run a completeness check before transferring data by using BAdI: Check Completeness Before Sending

B2B Services. For more information see Customizing for Transportation Management under  Business Add-

Ins (BAdIs) for Transportation Management

## Integration

Enterprise Services

## Freight Order Management

Freight Request for Quotation BAdI: Check Completeness Before Sending B2B Services .

## Configuration

For more information, see the documentation of the Transportation Quotation Requesting Out [page 97]
outbound interface.

## Enhancements

The BAdI for TransportationOrderQuotationNotification_Out (/SCMTMS/TOR_SE_TPNORQ_NTF) Business Add-
In (BAdI) is available for this operation.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

105


2.1.1.22  Transportation Quotation Requesting In

## Definition

An interface to receive confirmations in response to a request to process a transportation order of the category
“freight request for quotation”.

Technical Data

Entity Type

Category

## Direction

Business Context and Use

Service Interface

B2B

## Inbound

The Transportation Quotation Requesting In inbound service interface contains an operation that receives a
confirmation indicating whether a carrier has accepted or rejected a freight request for quotation sent by a
customer (for example, a shipper) during a tendering process.

Notes on SAP Implementation

## Integration

If a carrier also uses SAP Transportation Management (SAP TM), the operation in this service interface
exchanges data with the operation in the Transportation Quotation Requesting Out [page 154]  outbound
service interface in the Transportation Request Processing [page 122] process component. Otherwise, the
operation can exchange data with an equivalent third-party application that is being used by the carrier.

For more information about integration and configuration, see the documentation of the Transportation
Quotation Requesting Out [page 97] outbound interface.

More Information

Tendering

106

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


2.1.1.22.1  Change Transportation Order Based on

Transportation Order Quotation Confirmation

## Definition

To change a transportation order of the category “freight request for quotation” based on the confirmation of
this transportation order. The confirmation is either a freight quotation in response to the initial freight request
for quotation, or it is a rejection of a freight request for quotation.

Technical Data

Entity Type

Release State

Technical Name

## Namespace

Service Operation

## Released

TransportationOrderQuotationConfirmation_In

http://sap.com/xi/TMS/Global

Application Component

TM-FRM-FRT

Category

Direction

## Mode

Idempotency

B2B

## Inbound

Asynchronous

## Not Applicable

P2P Communication Enabled

## Yes

## Business Context and Use

A customer uses RFQ-based tendering to determine which carrier is to execute a particular freight order. When
the customer sends a freight request for quotation to a carrier, the carrier can either accept it by submitting a
quotation, or reject it. The Change Transportation Order Based on Transportation Order Quotation Confirmation
inbound operation receives a confirmation that contains either a quotation or the reason for rejecting the
freight request for quotation. The operation updates the required data in the freight request for quotation.

## Related Operations

The Confirm Transportation Request Quotation [page 155] outbound operation in the Transportation Request
Processing [page 122] process component can send the confirmation that is received by the Change
Transportation Order Based on Transportation Order Quotation Confirmation  inbound operation.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

107


## Features

The Change Transportation Order Based on Transportation Order Quotation Confirmation  inbound operation
receives an acceptance code that specifies whether a carrier has accepted or rejected a freight request for
quotation. The operation can receive the following data, for example:

● If a carrier rejects a freight request for quotation, the operation receives the rejection reason.

● If a carrier accepts a freight request for quotation, the operation receives the ID of the forwarding quotation

and a quotation price, for example.

● Optionally, if a carrier accepts a freight request for quotation that specifies a detailed charge hierarchy, the

operation receives the rates and related quantities within the charge hierarchy.

● Optionally, the operation receives loading and unloading times for the transportation stages given in the

freight request for quotation.

For more information, see the documentation of the TransportationDocumentQuotationConfirmationMessage
message data type in SAP Note 1512334

.

## Message Types

● Transportation Order Quotation Confirmation

## Prerequisites

The Request Transportation Order Quotation Creation [page 98] outbound operation has sent a freight request
for quotation to one or more carriers.

Notes on SAP Implementation

## Integration

The Change Transportation Order Based on Transportation Order Quotation Confirmation  inbound operation is
triggered in the SAP Transportation Management (SAP TM) back-end system when a confirmation of a freight
request for quotation is received from a carrier.

## Configuration

For more information, see the documentation of the Transportation Quotation Requesting Out [page 97]
outbound interface.

## Versioning

The Change Transportation Order Based on Transportation Order Quotation Confirmation  inbound operation
performs a similar function to the Maintain Supplier Shipment Quote and Maintain Supplier Freight Quote
inbound operations in SAP Transportation Management 7.0 (SAP TM 7.0).

108

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


Note that in SAP TM 1.0, the Confirm Transportation Request Quotation [page 155]  outbound operation and
the  Change Transportation Order Based on Transportation Order Quotation Confirmation inbound
operation shared a common message data type: TransportationDocumentQuotationConfirmationMessage. As
of SAP TM 1.01, however, these operations use different message data types that are similar in structure, but
not identical. The inbound operation continues to use message data type
TransportationDocumentQuotationConfirmationMessage, whereas the outbound operation now uses a
separate message data type  TransportationRequestQuotationConfirmationMessage. As a consequence, a
mapping between these message data types is required. This mapping for a confirmation message is usually
implemented in the system landscape of the sending party, that is, the carrier.

## Enhancements

The BAdI for TransportationOrderQuotationConfirmation_In (/SCMTMS/TOR_SE_TPNORQ_CNF) Business Add-
In (BAdI) is available for this operation.

2.1.2  Transportation Planning View

## Definition

A view that selects and displays transportation orders and relevant resources, which are planned in a joint
planning step. This step can be carried out either manually or by using one or more planning engines.

Technical Data

Entity Type

Technical Name

## Object Category

Business Context and Use

## Business Object

TransportationPlanningView

## Transformed Object

The Transportation Planning View  business object enables you to carry out planning activities and create
delivery proposals for selected transportation orders. It is used to select and display transportation orders and
relevant resources for which planning is to be carried out. It is also used to select and display transportation
orders for which delivery proposals are to be created. It enables the relevant activity to be performed, and it
can also display the result of the activity, for example, the created delivery proposals.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

109


## Features

The Transportation Planning View  business object is used in manual processing and background processing. In
both cases, it uses specified selection parameters and profiles to select the relevant transportation orders and
resources.

## Use Case 1: Interactive Freight Unit Planning

The transportation planning view uses specified selection profiles and parameters to select and display freight
units (FUs) and relevant resources that are to be planned in a joint planning step. The user can then assign the
FUs to the resources and trigger the planning step. Note that the resources comprise handling resources and
vehicle resources (including passive resources). The planning step includes vehicle scheduling, with the option
of creating freight orders or freight bookings. The transportation planning view also displays the freight orders
or freight bookings if they are created during planning.

## Use Case 2: Interactive Delivery Creation

The transportation planning view uses specified selection profiles and parameters to select and display freight
units or freight orders for which delivery proposals are to be created. The user selects the required freight units
or freight orders from the overview and triggers the creation of the delivery proposals. The transportation
planning view displays the delivery proposals, which can then be sent to a connected logistics execution
system.

Notes on SAP Implementation

## Integration

This business object and its operations are used to exchange delivery data between SAP Transportation
Management (SAP TM) and SAP ERP, as follows:

● When a user or a background report in the SAP TM back-end system sends delivery proposals to SAP ERP,
the Transportation Planning View business object triggers the Create Outbound Delivery as Bulk outbound
operation or the Create Inbound Delivery outbound operation.

● When SAP ERP informs SAP TM whether delivery creation was successful, SAP TM receives the

confirmation data using the corresponding Change Transportation Planning View Based on Delivery Bulk
Confirmation [page 119]  inbound operation or the Change Transportation Planning View based on Delivery
Confirmation [page 114]  inbound operation. Note, however, that neither of these inbound
operations change an instance of a Transportation Planning View  business object. It is a transient business
object that is not persisted in the database. Instead, these operations add the log entries in the
confirmation messages to the business application log of the receiving SAP TM back-end system.

## Configuration

To exchange delivery data between SAP TM and SAP ERP, you have to connect your SAP TM system to an SAP
ERP system and make the required Customizing settings in both systems. For more information, see
Configuring Integration of Orders and Deliveries.

110

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


2.1.2.1

Inbound Delivery Out

## Definition

An interface to request the creation of inbound deliveries.

Technical Data

Entity Type

Category

## Direction

Service Interface

SAP A2A

## Outbound

## Business Context and Use

The Inbound Delivery Out outbound service interface contains an operation that requests the creation of
inbound deliveries in the Inbound Delivery Processing process component, based on delivery proposals
created in the Transportation Order Processing [page 5] process component.

## Notes on SAP Implementation

For more information, see the documentation of the Transportation Planning View [page 109] business object.

2.1.2.1.1

Request Inbound Delivery Creation

## Definition

To request the creation of an inbound delivery.

Technical Data

## Entity Type

## Service Operation

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

111


Release State

Technical Name

Namespace

## Released

InboundDeliveryCreateRequest_Out

http://sap.com/xi/TMS/Global

Application Component

TM-ERP-TR-DLV

Category

Direction

## Mode

## Idempotency

Change/Update Behavior

SAP A2A

Outbound

Asynchronous

Not Applicable

## Not Applicable

P2P Communication Enabled

## Yes

## Business Context and Use

A shipper uses a transportation management system to carry out transportation planning and execution for
orders created in a logistics execution system (for example, purchase orders and returns orders). During the
planning process, optimized delivery proposals are created for the orders. The Request Inbound Delivery
Creation outbound operation sends the delivery proposals to the logistics execution system and requests the
creation of the inbound deliveries.

## Related Operations

Delivery proposals for outbound deliveries can be sent to a logistics execution system using the Request
Outbound Delivery Creation As Bulk [page 117]  outbound operation.

## Features

The Request Inbound Delivery Creation  inbound operation requests the creation of a delivery for items from
one or more orders. The type of delivery created depends on the type of order to which the delivery relates (for
example, inbound deliveries are created for purchase orders, and returns deliveries are created for returns
orders). At header level, each inbound delivery creation request is identified by an ID and contains information
about dates. At item level, it provides the referenced order items, as well as information about the product,
quantities, and measurements (for example, gross weight and gross volume).

For more information, see the documentation of the Create Inbound Delivery inbound operation in the Inbound
Delivery Processing process component.

112

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## Message Types

● InboundDeliveryCreateRequest

## Notes on SAP Implementation

For more information, see the documentation of the Transportation Planning View [page 109] business object.

## Enhancements

The BAdI for InboundDeliveryCreateRequest_Out (/SCMTMS/DLVP_SE_IDLV) Business Add-In (BAdI) is
available for this operation.

2.1.2.2

Inbound Delivery In

## Definition

An interface to receive confirmations of requests to create inbound deliveries.

Technical Data

Entity Type

Category

## Direction

Service Interface

SAP A2A

## Inbound

## Business Context and Use

The Inbound Delivery In  inbound service interface contains an operation that receives a confirmation of the
creation of inbound deliveries in the Inbound Delivery Processing process component, based on delivery
proposals created in the Transportation Order Processing [page 5] process component.

## Notes on SAP Implementation

For more information, see the documentation of the Transportation Planning View [page 109] business object.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

113


2.1.2.2.1

Change Transportation Planning View Based on
Delivery Confirmation

## Definition

To react to the receipt of a confirmation of the creation of an inbound delivery.

Technical Data

Entity Type

Release State

Technical Name

## Namespace

Service Operation

## Released

InboundDeliveryConfirmation_In_V1

http://sap.com/xi/TMS/Global

Application Component

TM-ERP-TR-DLV

Category

Direction

## Mode

Idempotency

SAP A2A

## Inbound

Asynchronous

No

Change/Update Behavior

## Not Applicable

P2P Communication Enabled

## Yes

## Business Context and Use

A shipper uses a transportation management system to carry out transportation planning and execution for
orders created in a logistics execution system (for example, purchase orders and returns orders). When the
logistics execution system creates an inbound delivery based on a delivery proposal received from the
transportation management system, it sends a confirmation of delivery creation (for example, using the
Confirm Inbound Delivery outbound operation). The Change Transportation Planning View based on Delivery
Confirmation  inbound operation receives the confirmation and updates the required data in the transportation
management system.

## Related Operations

● The Change Transportation Planning View Based on Delivery Confirmation  inbound operation can be used
in a procure-to-pay process, for example. For more information, see the documentation of the  Request
Inbound Delivery Creation [page 111]  outbound operation.

114

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


● The Change Transportation Planning View Based on Delivery Bulk Confirmation [page 119]  inbound
operation receives confirmations of outbound deliveries created in a logistics execution system.

## Features

The Change Transportation Planning View Based on Delivery Confirmation  inbound operation receives the
following details:

● Information about the deliveries that were successfully created. The operation adds the total number of

deliveries and the IDs of the deliveries to the business application log.

● Log items with information about delivery creation (for example, an error message that explains why a

particular delivery could not be created). The operation adds the log items to the business application log.

● Processing result code (successful or unsuccessful) that relates to all log items sent in a message. The

operation updates the processing result code and sets a confirmation timestamp in the freight units that
are related to the delivery confirmation.

Note that the Change Transportation Planning View Based on Delivery Confirmation  inbound operation does
not change an instance of a Transportation Planning View [page 109]  business object (this is a transient
business object that is not persisted in the database).

## Error Handling

The Change Transportation Planning View Based on Delivery Confirmation  operation supports Forward Error
Handling. The following error categories are used:

● PRE.TEE.LRE: Lock Error

● DCE: Conversion Error

● PRE: Processing Error

For more information about the individual error categories, see the code list for the global data type
LogItemCategoryCode.

## Message Types

● InboundDeliveryConfirmation_V1

Notes on SAP Implementation

## Integration

You can use this operation and the related operations to integrate SAP ERP with SAP Transportation
Management (SAP TM). For more information, see the documentation of the Transportation Planning View
[page 109] business object.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

115


To determine whether a response has been received from SAP ERP for freight units that are related to an order-
based transportation requirement (OTR) and that contain a timestamp for sending a delivery proposal, the
monitoring process in SAP TM uses the confirmation timestamp that is set by this operation.  For more
information, see Monitoring of Delivery Creation.

Note that if the processing result code sent by SAP ERP  is Unsuccessful, the SAP TM system raises an alert of
category TMS_OI_DLV_CREATION_PROBLEM.

## Enhancements

The BAdI for InboundDeliveryConfirmation_In_V1 (/SCMTMS/CPX_SE_IDLV_CNF1) Business Add-In (BAdI) is
available for this operation.

2.1.2.3  Outbound Delivery Out

## Definition

An interface to request the creation of outbound deliveries.

Technical Data

Entity Type

Category

## Direction

Business Context and Use

Service Interface

SAP A2A

## Outbound

The Outbound Delivery Out  outbound service interface contains an operation that requests the creation of
outbound deliveries in the Outbound Delivery Processing process component, based on delivery proposals
created in the Transportation Order Processing [page 5] process component.

## Notes on SAP Implementation

For more information, see the documentation of the Transportation Planning View [page 109] business object.

116

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


2.1.2.3.1

Request Outbound Delivery Creation As Bulk

## Definition

To request the creation of multiple outbound deliveries.

Technical Data

Entity Type

Release State

Technical Name

## Namespace

Service Operation

## Released

OutboundDeliveryBulkCreateRequest_Out

http://sap.com/xi/TMS/Global

Application Component

TM-ERP-TR-DLV

Category

Direction

## Mode

## Idempotency

Change/Update Behavior

SAP A2A

Outbound

Asynchronous

Not Applicable

## Not Applicable

P2P Communication Enabled

## Yes

## Business Context and Use

A shipper uses a transportation management system to carry out transportation planning and execution for
orders created in a logistics execution system (for example, sales orders or returns orders). During the
planning process, optimized delivery proposals are created for the orders. The Request Outbound Delivery
Creation As Bulk  outbound operation sends the delivery proposals to the logistics execution system
and requests the creation of the outbound deliveries.

## Related Operations

Delivery proposals for inbound deliveries can be sent to a logistics execution system using the  Request
Inbound Delivery Creation [page 111] outbound operation.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

117


## Features

The Request Outbound Delivery Creation As Bulk  outbound operation requests the creation of the relevant
deliveries for the order items. The type of delivery created depends on the type of order to which the delivery
relates (for example, outbound deliveries are created for sales orders, and replenishment deliveries are created
for stock transport orders). At header level, each outbound delivery creation request is identified by an ID and
contains information about dates. At item level, it provides the referenced order items, as well as information
about the product, quantities, and measurements (for example, gross weight and gross volume). The delivery
creation requests are sent in a bulk service operation to ensure that they are processed in the correct sequence
(that is, first in first out).

For more information, see the documentation of the Create Outbound Delivery as Bulk inbound operation in the
Outbound Delivery Processing process component.

## Processing

For more information about bulk processing, see  Bulk, Bundle, Collection.

## Message Types

● Outbound Delivery Bulk Create Request

## Notes on SAP Implementation

For more information, see the documentation of the Transportation Planning View [page 109] business object.

## Enhancements

The BAdI for OutboundDeliveryBulkCreateRequest_Out (/SCMTMS/DLVP_SE_ODLV_B) Business Add-In (BAdI)
is available for this operation.

2.1.2.4  Outbound Delivery In

## Definition

An interface to receive confirmations of requests to create outbound deliveries.

118

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


Technical Data

Entity Type

Category

## Direction

Business Context and Use

Service Interface

SAP A2A

## Inbound

The Outbound Delivery In  inbound service interface contains an operation that receives a confirmation of the
creation of outbound deliveries in the Outbound Delivery Processing process component, based on delivery
proposals created in the Transportation Order Processing [page 5] process component.

## Notes on SAP Implementation

For more information, see the documentation of the Transportation Planning View [page 109] business object.

2.1.2.4.1

Change Transportation Planning View Based on
Delivery Bulk Confirmation

## Definition

To react to the receipt of a confirmation of the creation of multiple outbound deliveries.

Technical Data

Entity Type

Release State

Technical Name

## Namespace

Service Operation

## Released

OutboundDeliveryBulkConfirmation_In

http://sap.com/xi/TMS/Global

Application Component

## TM-ERP-TR-DLV

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

119


Web Service Definition (Back End)

/SCMTMS/OUTBDLVBULKCONF

Category

Direction

## Mode

## Idempotency

Change/Update Behavior

SAP A2A

## Inbound

Asynchronous

Not Applicable

## Not Applicable

P2P Communication Enabled

## Yes

## Business Context and Use

A shipper uses a transportation management system to carry out transportation planning and execution for
orders created in a logistics execution system (for example, sales orders and returns orders). When
the logistics execution system creates an outbound delivery based on a delivery proposal received from the
transportation management system, it sends a confirmation of delivery creation (for example, using the
Confirm Outbound Delivery as Bulk outbound operation). The Change Transportation Planning View Based on
Delivery Bulk Confirmation   inbound operation receives the confirmation and updates the required data in the
transportation management system.

## Related Operations

● This operation can be used in a sell-from-stock process, for example. For more information, see the
documentation of the Request Outbound Delivery Creation As Bulk [page 117] outbound operation.

● The Change Transportation Planning View based on Delivery Confirmation [page 114]  inbound operation

receives confirmations of inbound deliveries created in a logistics execution system.

## Features

The Change Transportation Planning View based on Delivery Confirmation [page 114]  inbound operation
receives the following details:

● Information about the deliveries that were successfully created. The operation adds the total number of

deliveries and the IDs of the deliveries to the business application log.

● Log items with information about delivery creation (for example, an error message that explains why a

particular delivery could not be created). The operation adds the log items to the business application log.

● Processing result code (successful or unsuccessful) that relates to all log items sent in a message. The

operation updates the processing result code and sets a confirmation timestamp in the freight units that
are related to the delivery confirmation.

Note that the Change Transportation Planning View Based on Delivery Bulk Confirmation  inbound operation
does not change an instance of a Transportation Planning View [page 109] business object (this is a transient
business object that is not persisted in the database).

120

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## Processing

For more information about bulk processing, see Bulk, Bundle, Collection.

## Error Handling

The Change Transportation Planning View Based on Delivery Bulk Confirmation  operation supports Forward
Error Handling. The following error categories are used:

● PRE.TEE.LRE: Lock Error

● DCE: Conversion Error

● PRE: Processing Error

For more information about the individual error categories, see the code list for the global data type
LogItemCategoryCode.

## Message Types

● Outbound Delivery Bulk Confirmation

Notes on SAP Implementation

## Integration

You can use this operation and the related operations to integrate SAP ERP with SAP Transportation
Management (SAP TM). For more information, see the documentation of the Transportation Planning View
[page 109]  business object.

To determine whether a response has been received from SAP ERP for freight units that are related to an order-
based transportation requirement (OTR) and that contain a timestamp for sending a delivery proposal, the
monitoring process in SAP TM uses the confirmation timestamp that is set by this operation.  For more
information, see Monitoring of Delivery Creation.

Note that if the processing result code sent by SAP ERP  is Unsuccessful, the SAP TM system raises an alert of
category TMS_OI_DLV_CREATION_PROBLEM.

## Enhancements

The BAdI for OutboundDeliveryBulkConfirmation_In (/SCMTMS/CPX_SE_ODLV_CNF) Business Add-In (BAdI) is
available for this operation.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

121


2.2  Transportation Request Processing

## Definition

The processing of requests from an ordering party for the provision of transportation services.

Technical Data

Entity Type

## Technical Name

Business Context and Use

## Process Component

## TransportationRequestProcessing

The Transportation Request Processing process component provides functions for handling requests received
from a customer for the provision of transportation services. A transportation service is represented by a
request to transport goods from one or more shippers to one or more consignees in accordance with agreed
terms and conditions. In a B2B scenario, the request can represent a forwarding quotation or a forwarding
order. In an intracompany scenario (that is, an A2A scenario), the request can represent either an order-based
transportation requirement (that is, a preliminary request to transport goods for a particular order) or a
delivery-based transportation requirement (that is, a finalized request to transport goods for a particular
delivery).

The Transportation Request Processing process component provides A2A enterprise services that enable order
processing and delivery processing to be integrated with transportation request processing. It provides
enterprise services for the following scenarios:

● Order Integration

In this scenario, orders are transferred from order processing to transportation request processing. In
transportation request processing, an order is represented by an order-based transportation requirement
(OTR). This scenario can be used for sales orders, purchase orders (including stock transport orders), and
returns orders.

● Delivery Integration

In this scenario, deliveries are transferred from delivery processing to transportation request processing. In
transportation request processing, a delivery is represented by a delivery-based transportation
requirement (DTR). This scenario can be used for inbound deliveries and outbound deliveries.

The Transportation Request Processing process component provides B2B enterprise services that enable a
carrier to communicate directly with a customer. It provides B2B services for the following scenarios:

● Forwarding Quotations

In this scenario, a carrier receives a request for quotation from a customer, based on which transportation
request processing creates a forwarding quotation. The carrier can then confirm the request for quotation,
that is, send a quotation to the customer or send the reason for rejecting the request for quotation. The

122

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


customer can also send a cancellation of a request for quotation that has already been sent to the carrier.
Based on this, transportation request processing cancels the corresponding forwarding quotation.

● Forwarding Orders

In this scenario, a carrier receives a new or updated freight order from a customer, based on which
transportation request processing creates or updates a forwarding order. The carrier can then send a
confirmation to the customer to confirm the creation of the forwarding order. The customer can also send
a cancellation of a freight order that has already been sent to the carrier. Based on this, transportation
request processing cancels the corresponding forwarding order. (Note that an update or cancellation can
only be carried out if the status of the forwarding order allows it.)

● Forwarding Orders Based on Forwarding Quotations

In this scenario, transportation request processing creates a forwarding order with reference to an existing
forwarding quotation.

Note that a customer could be either a shipper, a logistics service provider, or a carrier who subcontracts
transportation services to another carrier.

Notes on SAP Implementation

## Master Data for B2B Communication

You have to define your customers as business partners in the SAP Transportation Management (SAP TM)
back-end system. You define business partners in SAP NetWeaver Business Client (NWBC) by choosing

Master Data General Define Business Partner

.

We recommend that you assign standard IDs to each business partner and to each of the involved locations
and products.

## More Information

SAP Transportation Management (SAP TM)

2.2.1  Transportation Request

## Definition

A request to transport goods from one or more shippers to one or more consignees in accordance with agreed
terms and conditions. In an intracompany integration scenario, the request can represent either an order-
based transportation requirement (preliminary) or a delivery-based transportation requirement (final). In a
B2B scenario, it can represent a forwarding quotation or a forwarding order. A transportation request can also
include the assignment of transportation stages.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

123


Technical Data

Entity Type

Technical Name

## Object Category

Business Context and Use

Business Object

TransportationRequest

## Business Process Object

The Transportation Request business object enables a carrier to perform the following transportation activities:

● Receive requests for quotation from a customer and submit a forwarding quotation. If the quotation is
accepted by the customer, the carrier can then create a forwarding order based on the forwarding
quotation.

● Create a forwarding order based on an order received from a customer. The carrier uses the forwarding

order to plan and execute the transportation activities. It is also used for the customer settlement process.

Note that a customer could be either a shipper, a logistics service provider, or a carrier who subcontracts
transportation services to another carrier.

The Transportation Request business object enables a shipper to carry out transportation planning and
execution for order-based transportation requirements and delivery-based requirements that were created
based on orders and deliveries received from a logistics execution system.

For more information about the business context, see the documentation of the Transportation Request
Processing [page 122]  process component.

2.2.1.1

Credit Usage Out

## Definition

An interface to query the creditworthiness of business partners and to send information about their credit
commitments.

Technical Data

Entity Type

Category

124

## P U B L I C

Service Interface

## SAP A2A

Enterprise Services and ESR Content
Enterprise Services


Direction

## Outbound

## Business Context and Use

The Credit Usage Out outbound service interface contains operations that exchange credit information about
business partners with a connected credit management application.

2.2.1.1.1

Check Transportation Request Ordering Party
Creditworthiness

## Definition

To trigger the sending of information about the creditworthiness of a business partner involved in a
transportation request in the role of a payer party.

Technical Data

Entity Type

Release State

Technical Name

Namespace

Category

Direction

## Mode

## Idempotency

P2P Communication Enabled

Business Context and Use

## Service Operation

Released with Restrictions

CreditWorthinessQuery_Out

http://sap.com/xi/TMS/Global

SAP A2A

Outbound

Synchronous

No

## Yes

Before you approve a new or changed forwarding order, you check the creditworthiness of the relevant
business partner (that is, the payer) by performing a credit limit check. The Check Transportation Request

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

125


Ordering Party Creditworthiness outbound operation requests information about the business partner from a
connected credit management application. Based on the response from the credit management application,
you can decide whether or not to proceed with the order.

## Related Operations

● The Notify of Credit Commitment [page 127] outbound operation in the Transportation Request

Processing [page 122] process component informs the credit management application about the credit
limit amount approved for a business partner in a specific order.

● The Notify of Credit Commitment [page 207] outbound operation in the Customer Freight Invoice Request
Processing [page 205] process component provides the credit management application with updated
information about the business partner’s credit commitments during forwarding settlement.

## Features

The Check Transportation Request Ordering Party Creditworthiness outbound operation sends the following
data to the credit management application:

● Business partner ID (that is, payer ID)

● Amount to be checked

● Internal ID of the credit segment

The operation receives data about the creditworthiness of the business partner, including the following:

● Flag that indicates whether the business partner is creditworthy

● Credit limit that is valid for the business partner for a specific period

● Total credit exposure amount of the business partner

● Flag that indicates whether the business partner is blocked in the credit management application

● Credit rating

● Credit risk class that indicates the risk of non payment

## Message Types

● CreditWorthinessQuery

● CreditWorthinessResponse

## Notes on SAP Implementation

In SAP Transportation Management (SAP TM), you use this operation to request credit limit information for a
business partner from SAP Credit Management. If you have enabled credit limit checks for the relevant
forwarding order types, the SAP TM system triggers the operation when you save a new or changed forwarding
order or when you manually trigger a credit limit check for a forwarding order.

Note that a forwarding order in the SAP TM back-end system corresponds to an instance of a Transportation
Request [page 123] business object.

126

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## Configuration

You have connected your SAP TM system to the SAP Credit Management system.

In SAP Credit Management, you have carried out the following activities in Customizing for Financial Supply

Chain Management under  Credit Management

Integration with Accounts Receivable Accounting and Sales

and Distribution

Integration with Accounts Receivable Accounting :

● Define Credit Segment

● Assign Credit Control Area and Credit Segment

In SAP TM, you have made the following Customizing settings:

● You have enabled the credit limit check for the relevant forwarding order types. For more information, see

Customizing for Transportation Management under

Forwarding Order Management

## Forwarding Order

Define Forwarding Order Types .

● You have assigned the credit segment IDs that the SAP TM system uses to access the credit management

functions in the SAP Credit Management application. For more information, see Customizing for

Transportation Management under  Basic Functions Credit Management Integration Assign Credit

Segments to Sales Orgs and Company Orgs .

## Enhancements

The BAdI for CreditWorthinessQuery_Out (/SCMTMS/CLC_SE_CRCMT) Business Add-In (BAdI) is available for
this operation.

## More Information

Forwarding Order Management

2.2.1.1.2  Notify of Credit Commitment

## Definition

To send a notification about the credit commitments of business partners.

Technical Data

Entity Type

Release State

Technical Name

## Service Operation

Released with Restrictions

CreditCommitmentNotification_Out

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

127


Namespace

Category

Direction

## Mode

## Idempotency

P2P Communication Enabled

Business Context and Use

http://sap.com/xi/TMS/Global

SAP A2A

Outbound

Asynchronous

No

## Yes

You have approved a new or changed forwarding order after performing a credit limit check for the relevant
business partner (that is, the payer). You used a connected credit management application to perform the
check. Either the credit limit check was successful, or the credit limit check was unsuccessful and you have
decided to proceed with the order despite the result.

When you approve and save the order, the Notify of Credit Commitment outbound operation informs the credit
management application about the credit limit amount approved for the business partner. This allows the
credit management application to update the credit exposure information for the business partner. The
operation also sends an update to the credit management application if you cancel an approved forwarding
order.

## Related Operations

During forwarding settlement, the Notify of Credit Commitment [page 207] outbound operation in the
Customer Freight Invoice Request Processing [page 205] process component provides the credit management
application with updated information about the business partner’s credit commitments.

## Features

The Notify of Credit Commitment outbound operation sends credit commitment data to the credit
management application, including the following:

● Business partner ID (that is, payer ID)

● Amount committed (for example, total amount of the forwarding order)

● Forwarding order number

● Internal ID of the credit segment

● Validity date of the commitment

128

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## Message Types

● CreditCommitmentNotification

## Prerequisites

The Check Transportation Request Ordering Party Creditworthiness [page 125] outbound operation has
requested credit information about a business partner from a connected credit management application.

## Notes on SAP Implementation

In SAP Transportation Management (SAP TM), you use this operation to send credit commitment information
for a business partner to SAP Credit Management. The SAP TM system triggers the operation when you
approve and save a forwarding order after you have carried out a credit limit check for the business partner; or
when you cancel an approved forwarding order. SAP Credit Management updates the credit limit amount for
the business partner accordingly (credit exposure category Open Orders ). Note that a forwarding order in the
SAP TM back-end system corresponds to an instance of a Transportation Request [page 123] business object.

## Configuration

You have made the required settings for credit limit checks. For more information, see the Configuration section
in the documentation of the Check Transportation Request Ordering Party Creditworthiness [page 125]
outbound operation.

## Enhancements

The BAdI for CreditCommitmentNotification_Out Business Add-In (BAdI) is available for this operation.

## More Information

Forwarding Order Management

2.2.1.2

Intracompany Transportation Requesting In

## Definition

An interface to simulate, create, change, or cancel in-house transportation requests.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

129


Technical Data

Entity Type

Category

## Direction

Business Context and Use

Service Interface

SAP A2A

## Inbound

The Intracompany Transportation Requesting In inbound service interface groups operations that simulate,
create, change, or cancel transportation requirements, based on order or delivery data received from a logistics
execution system.

Notes on SAP Implementation

## Configuration

To integrate order and delivery processing in SAP ERP with transportation request processing in SAP
Transportation Management (SAP TM), you have to connect your SAP TM system to an SAP ERP
system and make the required Customizing settings in both systems. For more information, see Configuring
Integration of Orders and Deliveries.

Note that an order-based transportation requirement (OTR) or a delivery-based requirement (DTR) in the SAP
TM back-end system corresponds to an instance of a  Transportation Request [page 123]  business object.

2.2.1.2.1  Maintain Transportation Request

## Definition

To create or change a transportation request of the category “order-based transportation requirement” or
“delivery-based transportation requirement”.

Technical Data

## Entity Type

Service Operation

130

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


Release State

Technical Name

## Namespace

Application Component

Category

Direction

## Mode

## Idempotency

Change/Update Behavior

P2P Communication Enabled

## Released

IntracompanyTransportationRequestRequest_In

http://sap.com/xi/TMS/Global

TM-ERP-TR

SAP A2A

## Inbound

Asynchronous

## Yes

Type1

## Yes

## Business Context and Use

A shipper uses transportation request processing to carry out transportation planning and execution for orders
and deliveries created in a logistics execution system. The Maintain Transportation Request inbound operation
receives the order or delivery data and creates or changes the corresponding order-based transportation
requirements or delivery-based transportation requirements (DTRs). These are used as the basis for
transportation planning.

This operation can be used in a sell-from-stock process, for example. For more information, see the
documentation of the  Request Outbound Delivery Creation As Bulk [page 117] outbound operation.

## Related Operations

The following operations can send order data to the Maintain Transportation Request inbound operation:

● Request Transportation Request outbound operation in the Sales Order Processing process component

● Request Transportation Request outbound operation in the Purchase Order Processing process component.
Note that this operation is used for purchase orders, stock transport orders, and returns purchase orders.

● Request Transportation Request outbound operation in the Customer Return Processing process

component

The following operations can send delivery data to the Maintain Transportation Request inbound operation:

● Request Transportation Request outbound operation in the Outbound Delivery Processing process

component

● Request Transportation Request outbound operation in the Inbound Delivery Processing process

component

In addition, you can use the following operations:

● The Cancel Transportation Request [page 135] inbound operation cancels a transportation requirement

based on a canceled order or delivery.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

131


● The Simulate Transportation Request [page 133] inbound operation simulates an order-based

transportation requirement for a sales order.

## Features

The Maintain Transportation Request inbound operation receives data such as the following:

● Category of the transportation request that is to be created or changed, that is, an order-based

transportation requirement or a delivery-based transportation requirement

● ID of the document in the sending system for which a transportation requirement is to be created or

changed

● Information about the items in the order or delivery

● Relevant dates, locations (for example, ship-from and ship-to locations), and business partners (for

example, shipper and consignee)

## Error Handling

## Forwarding Error Handling

The Maintain Transportation Request inbound operation supports Forward Error Handling (FEH). The following
error categories are used:

● DCE: Determination and Conversion Error

● PRE: Processing Error

● PRE.TEE.LRE: Lock Request Error

For more information about the individual error categories, see the code list for the global data type
LogItemCategoryCode.

## Message Types

● TransportationRequestSUITERequest

## Notes on SAP Implementation

The Maintain Transportation Request inbound operation can create DTRs or change DTRs as a result of a
delivery split triggered by SAP ERP, the SAP Extended Warehouse Management (SAP EWM) application, or
SAP TM. If SAP EWM triggers the split, the delivery split is processed in SAP ERP first and then transferred to
SAP TM. The triggering application is included in the message sent by SAP ERP to enable SAP TM to
distinguish between a split that is triggered by SAP TM (planning is correct in SAP TM) and a split triggered by
SAP ERP or SAP EWM (planning is no longer correct and must be updated in SAP TM).

132

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


For information about delivery splits triggered by SAP TM, see the documentation of the Request Outbound
Delivery Split V1 [page 138] outbound operation.

## Configuration

For more information, see the documentation of the Intracompany Transportation Requesting In [page 129]
inbound service interface.

## Enhancements

The BAdI for IntracompanyTransportationRequestRequest_In (/SCMTMS/TRQ_SE_REQREQ) Business Add-In
(BAdI) is available for this operation.

2.2.1.2.2  Simulate Transportation Request

## Definition

To simulate a transportation request.

Technical Data

Entity Type

Release State

Technical Name

## Service Operation

## Released with Restrictions

IntracompanyTransportationRequestSimulateRequestCon­

firmation_In

## Namespace

http://sap.com/xi/TMS/Global

Application Component

Category

Direction

## Mode

## Idempotency

P2P Communication Enabled

TM-ERP-TR

SAP A2A

## Inbound

Synchronous

No

## Yes

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

133


## Business Context and Use

A shipper carries out transportation planning synchronously in transportation request processing during sales
order processing in a logistics execution system. This enables the transportation situation to be taken into
account when calculating feasible dates and quantities for sales order items.

While creating, changing, or rescheduling a sales order in sales order processing, a user triggers transportation
planning in transportation request processing. Sales order processing requests the simulation of an order-
based transportation requirement (OTR) and the related planning activities. The Simulate Transportation
Request inbound operation creates an order-based transportation requirement, triggers transportation
planning, and returns the planning results to sales order processing.

## Related Operations

The Simulate Transportation Request inbound operation can receive a simulation request from the Request
Transportation Request Simulation outbound operation in the Sales Order Processing process component.

## Features

The Simulate Transportation Request inbound operation receives data such as the following:

● ID of the sales order if the sales order has already been created in sales order processing

● Information about the items in the sales order

● Relevant dates, locations (for example, ship-from and ship-to locations), and business partners (for

example, shipper and consignee)

The Simulate Transportation Request outbound operation returns the transportation planning results to the
requesting system. For example, it sends the relevant dates and corresponding quantities for the schedule lines
in the order (for example, delivery and loading date).

## Message Types

● Transportation Request SUITE Simulate Confirmation

● Transportation Request SUITE Simulate Request

Notes on SAP Implementation

## Configuration

To use this operation in SAP Transportation Management (SAP TM) to receive a simulation request from SAP
ERP, you have to connect your SAP TM system to an SAP ERP system and make the required Customizing
settings in both systems. For more information, see Scheduling of SAP ERP Sales Orders in SAP TM.

Enhancements

134

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


The BAdI for IntracompanyTranspRequestSimulateReqConfirmation_In (/SCMTMS/
TRQ_SE_TPNREQ_SIM) Business Add-In (BAdI) is available for this operation.

2.2.1.2.3  Cancel Transportation Request

## Definition

To cancel a transportation request of the category “order-based transportation requirement” or “delivery-
based transportation requirement”.

Technical Data

Entity Type

Release State

Technical Name

Service Operation

## Released

IntracompanyTransportationRequestCancellationRe­

quest_In

## Namespace

http://sap.com/xi/TMS/Global

Application Component

Category

Direction

## Mode

Idempotency

TM-ERP-TR

SAP A2A

## Inbound

Asynchronous

## Yes

Change/Update Behavior

## Not Applicable

P2P Communication Enabled

## Yes

## Business Context and Use

A shipper cancels an order or delivery that has already been sent from order processing or delivery
processing to transportation request processing. In addition, transportation request processing has already
created the corresponding order-based transportation requirement (OTR) or delivery-based transportation
requirement (DTR).The Cancel Transportation Request inbound operation receives a request to cancel an OTR
or DTR for a canceled order or delivery. It cancels the OTR or DTR and any related business documents.

## Related Operations

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

135


The following operations can send order cancellation data to the Cancel Transportation Request inbound
operation:

● Request Transportation Request Cancellation outbound operation in the Sales Order Processing process

component

● Request Transportation Request Cancellation outbound operation in the Purchase Order Processing

process component

● Request Transportation Request Cancellation outbound operation in the Customer Return

## Processing process component

The following operations can send delivery cancellation data to the Cancel Transportation Request inbound
operation:

● Request Transportation Request Cancellation outbound operation in the Outbound Delivery Processing

process component

● Request Transportation Request Cancellation outbound operation in the Inbound Delivery

Processing process component

## Features

The Cancel Transportation Request inbound operation receives the ID of the canceled order or delivery, based
on which it cancels the corresponding transportation requirement and any related documents.

## Error Handling

## Forward Error Handling

The Cancel Transportation Request inbound operation supports Forward Error Handling (FEH). The following
error categories are used:

● DCE: Determination and Conversion Error

● PRE: Processing Error

● PRE.TEE.LRE: Lock Request Error

For more information about the individual error categories, see the code list for the global data type
LogItemCategoryCode .

## Message Types

● TransportationRequestSUITECancellationRequest

136

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## Prerequisites

The  Maintain Transportation Request [page 130]  inbound operation has created a transportation requirement
based on an order or delivery. Note that cancellation is not possible if the OTR or DTR has the status Canceled
or Completed .

Notes on SAP Implementation

## Configuration

For more information, see the documentation of the Intracompany Transportation Requesting In [page 129]
inbound service interface.

## Enhancements

The BAdI for IntracompanyTranspRequestCancellationRequest_In (/SCMTMS/TRQ_SE_CNCLRQ) Business Add-
In (BAdI) is available for this operation.

2.2.1.3  Outbound Delivery Out

## Definition

An interface to request the split of outbound deliveries.

Technical Data

Category

Direction

A2A

## Outbound

## Business Context and Use

The Outbound Delivery Out outbound service interface contains an operation that sends information about a
required outbound delivery split to a logistics execution system.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

137


## More Information

Request Outbound Delivery Split V1 [page 138]

2.2.1.3.1

Request Outbound Delivery Split V1

## Definition

To request the split of an outbound delivery.

Technical Data

Release State

Technical Name

## Namespace

Application Component

Category

Direction

## Mode

## Idempotency

Change/Update Behavior

P2P Communication Enabled

Business Context

## Released

OutboundDeliveryERPSplitRequest_Out_V1

http://sap.com/xi/TMS/Global

TM-ERP-TR

A2A

Outbound

Asynchronous

No

Type 1

## Yes

A shipper performs transportation planning or changes the existing planning of a delivery-based transportation
requirement (DTR). The DTR is based on an outbound delivery that was received from a logistics execution
system. When the shipper saves the planning results, the system determines that a delivery split is required
(for example, because freight units that belong to the DTR have been assigned to different freight orders).

To split the delivery-based transportation requirement, the outbound delivery must be split first in the logistics
execution system. The Request Outbound Delivery Split V1 outbound operation requests the delivery split in the
logistics execution system.

138

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## Related Operations

● Delivery split requests sent by the Request Outbound Delivery Split V1 outbound operation can be received

by the Maintain Outbound Delivery Based on Outbound Delivery Split Request V1
(OutboundDeliveryERPSplitRequest_In_V1) inbound operation in the Outbound Delivery Processing
process component.

● The Change Transportation Request Based on Outbound Delivery Split Confirmation V1 [page 141]
inbound operation receives a confirmation that specifies whether the outbound delivery split was
successful.

● If the dates in an outbound delivery have to be updated because dates are changed during transportation
planning or manually in a freight order, the Request Outbound Delivery Update [page 143] outbound
operation requests a delivery update in the logistics execution system. Note that if the system determines
that a delivery update and a delivery split are required for the same outbound delivery at the same time,
both the split and update are requested by the Request Outbound Delivery Split V1 outbound operation.

## Features

The Request Outbound Delivery Split V1 outbound operation sends information about the items that are to be
split from the original outbound delivery (that is, IDs of the items in the original delivery, split quantity, unit of
measure, and the required dates for the new delivery). If a delivery is to be split into several deliveries, each
delivery is sent in a separate message.

If the logistics execution system splits the outbound delivery, it sends the following data to transportation
request processing in separate messages:

● The new delivery that has been created for the items split from the original delivery. The data sent includes

a reference to the original delivery and the triggering application.

● The changed original delivery. The data sent includes a reference to the new delivery.

The Maintain Transportation Request [page 130] inbound operation creates the new delivery-based
transportation requirement and updates the existing delivery-based transportation requirement accordingly.

## Prerequisites

The Maintain Transportation Request [page 130] inbound operation has created a delivery-based
transportation requirement based on an outbound delivery received from a logistics execution system.

## Notes on SAP Implementation

You use this operation in SAP Transportation Management (SAP TM) to request a delivery split in SAP ERP.
Note the following:

● A delivery split is required only if the first stage or the last stage of the transportation chain is affected.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

139


● SAP TM requests a delivery split only if the ERP outbound delivery does not have one of the following

statuses:

○ Distribution status: Distributed

○ Goods movement status: Partially Completed or Completed

● SAP TM can request a delivery split only for an outbound delivery. It cannot request a delivery split for an

inbound delivery.

You can use a worklist to monitor DTRs for which a delivery split or update has not been completed yet. In SAP

NetWeaver Business Client choose  ERP Logistics Integration Worklist Overview Transportation

Requirements (Not Finalized) DTRs with Incomplete Delivery Splits/Updates .

## Configuration

● You have defined a delivery split/update type in Customizing for Transportation Management under

## Integration

ERP Logistics Integration Delivery-Based Transportation Requirement Define Delivery

Split/Update Types .

● You have assigned the delivery split/update type to the delivery-based transportation requirement type in

Customizing for Transportation Management under

## Integration

## ERP Logistics Integration Delivery-

Based Transportation Requirement Define Delivery-Based Transportation Requirement Types .

● You have assigned output profile /SCMTMS/TRQ_DTR to the delivery-based transportation requirement

type in the Customizing activity Define Delivery-Based Transportation Requirement Types.

## Enhancements

The Business Add-In (BAdI) BAdI for OutboundDeliveryERPSplitRequest_Out_V1 (/SCMTMS/
TRQ_SE_DLVSPLT_RQ) is available for this operation.

## More Information

Delivery Splits and Updates Triggered by SAP TM

2.2.1.4  Outbound Delivery In

## Definition

An interface to receive a confirmation in response to a request for an outbound delivery split.

Technical Data

Category

A2A

140

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


Direction

## Inbound

## Business Context and Use

The Outbound Delivery In inbound service interface contains an operation that receives a confirmation of an
outbound delivery split.

## More Information

Change Transportation Request Based on Outbound Delivery Split Confirmation V1 [page 141].

2.2.1.4.1

Change Transportation Request Based on
Outbound Delivery Split Confirmation V1

## Definition

To change a transportation request of the category “delivery-based transportation requirement” based on the
confirmation of an outbound delivery split.

Technical Data

Release State

Technical Name

## Namespace

Application Component

Category

Direction

## Mode

Idempotency

## Released

OutboundDeliveryERPSplitConfirmation_In_V1

http://sap.com/xi/TMS/Global

TM-ERP-TR

A2A

## Inbound

Asynchronous

No

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

141


Change/Update Behavior

P2P Communication Enabled

Type 1

## Yes

## Business Context

An outbound delivery split has been requested in a logistics execution system by the Request Outbound
Delivery Split V1 [page 138] outbound operation. When the logistics execution system confirms whether the
delivery split was successful, the Change Transportation Request Based on Outbound Delivery Split
Confirmation V1 inbound operation receives the confirmation and updates the corresponding delivery-based
transportation requirement.

## Related Operations

The Change Transportation Request Based on Outbound Delivery Split Confirmation V1 inbound operation can
receive a confirmation from the Confirm Outbound Delivery Split V1
(OutboundDeliveryERPSplitConfirmation_Out_V1) outbound operation in the Outbound Delivery
Processing process component.

## Features

The Change Transportation Request Based on Outbound Delivery Split Confirmation V1 inbound operation
receives the ID of the original delivery for which the delivery split was requested and a severity code that shows
whether the split was successful. If the split was successful, the operation also receives the ID of the new
outbound delivery. Note that it is not possible to trigger a new delivery split until the current delivery split has
been successfully completed.

## Prerequisites

The Request Outbound Delivery Split V1 [page 138] outbound operation has requested an outbound delivery
split.

## Notes on SAP Implementation

For more information, see the documentation of the Request Outbound Delivery Split V1 [page 138] outbound
operation.

## Enhancements

The Business Add-In (BAdI) BAdI for OutboundDeliveryERPSplitConfirmation_In_V1 (/SCMTMS/
TRQ_SE_ODLVSPLTCF) is available for this operation.

142

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## More Information

Delivery Splits and Updates Triggered by SAP TM

2.2.1.5  Outbound Delivery Processing Out

## Definition

An interface to request the update of outbound deliveries.

Technical Data

Category

Direction

A2A

## Outbound

## Business Context and Use

The Outbound Delivery Processing Out outbound service interface contains an operation that sends
information about a required outbound delivery update to a logistics execution system.

## More Information

Request Outbound Delivery Update [page 143]

2.2.1.5.1

Request Outbound Delivery Update

## Definition

To request the update of an outbound delivery.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

143


Technical Data

Release State

Technical Name

## Namespace

Application Component

Category

Direction

## Mode

## Idempotency

Change/Update Behavior

P2P Communication Enabled

Business Context

## Released

OutboundDeliveryUpdateRequest_Out

http://sap.com/xi/TMS/Global

TM-ERP-TR

A2A

## Oubound

Asynchronous

No

Type 1

## Yes

A shipper performs transportation planning or changes the existing planning of a delivery-based transportation
requirement (DTR). The DTR is based on an outbound delivery that was received from a logistics execution
system. Dates are changed during planning or the shipper changes the dates of the relevant freight order
manually. When the shipper saves the planning results or the changed freight order, the system determines
that the dates in the freight order no longer match the dates in the DTR and the original outbound delivery.

To update the delivery-based transportation requirement accordingly, the dates must be updated first in the
outbound delivery. The Request Outbound Delivery Update outbound operation requests the delivery update in
the logistics execution system.

## Related Operations

● A request sent by the Request Outbound Delivery Update outbound operation can be received by the

Update Outbound Delivery (OutboundDeliveryUpdateRequest_In) inbound operation in the Outbound
Delivery Processing process component.

● The Change Transportation Request Based on Outbound Delivery Update [page 147] inbound operation

receives a confirmation that specifies whether the outbound delivery update was successful.

● If an outbound delivery has to be split as the result of new or changed transportation planning, the Request

Outbound Delivery Split V1 [page 138] outbound operation requests a delivery split in the logistics
execution system. Note that if the system determines that a delivery update and a delivery split are
required for the same outbound delivery at the same time, both the split and update are requested by the
Request Outbound Delivery Split V1 [page 138] outbound operation. In this case, the update is not
requested by the Request Outbound Delivery Update outbound operation.

144

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## Features

The Request Outbound Delivery Update outbound operation sends the changed dates and the ID of the
outbound delivery in the logistics execution system.

If the delivery update is successful, the logistics execution system sends the updated original delivery back to
transportation request processing. The Maintain Transportation Request [page 130] inbound operation
receives the delivery data and updates the corresponding delivery-based transportation requirement.

## Prerequisites

The Maintain Transportation Request [page 130] inbound operation has created a delivery-based
transportation requirement based on an outbound delivery received from a logistics execution system.

## Notes on SAP Implementation

You use this operation in SAP Transportation Management (SAP TM) to request an outbound delivery update in
SAP ERP. You can update the goods issue date, loading date, transportation start date, and delivery date in the
outbound delivery based on changed dates in SAP TM.

Note the following:

● SAP TM requests a delivery update only if the SAP ERP outbound delivery does not have one of the

following statuses:

○ Distribution status: Distributed

○ Goods movement status: Partially Completed or Completed

● SAP TM can request a delivery update only for an outbound delivery. It cannot request a delivery update for

an inbound delivery.

You can use a worklist to monitor DTRs for which a delivery split or update has not been completed yet. In SAP

NetWeaver Business Client choose  ERP Logistics Integration Worklist Overview Transportation

Requirements (Not Finalized) DTRs with Incomplete Delivery Splits/Updates .

## Configuration

● You have defined a delivery split/update type in Customizing for Transportation Management under

## Integration

ERP Logistics Integration Delivery-Based Transportation Requirement Define Delivery

Split/Update Types .

● You have assigned the delivery split/update type to the delivery-based transportation requirement type in

Customizing for Transportation Management under

## Integration

## ERP Logistics Integration Delivery-

Based Transportation Requirement Define Delivery-Based Transportation Requirement Types .

● You have assigned output profile /SCMTMS/TRQ_DTR to the delivery-based transportation requirement

type in the Customizing activity Define Delivery-Based Transportation Requirement Types.

## Enhancements

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

145


The Business Add-In (BAdI) BAdI for OutboundDeliveryUpdateRequest_Out (/SCMTMS/TRQ_SE_DLVUPD_REQ)
is available for this operation.

## More Information

Delivery Splits and Updates Triggered by SAP TM

2.2.1.6  Outbound Delivery Processing In

## Definition

An interface to receive a confirmation in response to a request for an outbound delivery update.

Technical Data

Category

Direction

A2A

## Inbound

## Business Context and Use

The Outbound Delivery Processing In inbound service interface contains an operation that receives a
confirmation of an outbound delivery update.

## More Information

Change Transportation Request Based on Outbound Delivery Split Confirmation [page 141]

146

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


2.2.1.6.1

Change Transportation Request Based on
Outbound Delivery Update Confirmation

## Definition

To change a transportation request of the category “delivery-based transportation requirement” based on the
confirmation of an outbound delivery update.

Technical Data

Release State

Technical Name

## Namespace

Application Component

Category

Direction

## Mode

## Idempotency

Change/Update Behavior

P2P Communication Enabled

Business Context

## Released

OutboundDeliveryConfirmation_In_V1

http://sap.com/xi/TMS/Global

TM-ERP-TR

A2A

## Inbound

Asynchronous

No

Type 1

## Yes

An outbound delivery update has been requested in a logistics execution system by the Request Outbound
Delivery Update [page 143] outbound operation. When the logistics execution system confirms whether the
delivery update was successful, the Change Transportation Request Based on Outbound Delivery Update
Confirmation inbound operation receives the confirmation and updates the corresponding delivery-based
transportation requirement.

## Related Operations

The Change Transportation Request Based on Outbound Delivery Update Confirmation inbound operation can
receive a confirmation from the Confirm Outbound Delivery V1 (OutboundDeliveryConfirmation_Out_V1)
outbound operation in the Outbound Delivery Processing process component.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

147


## Features

The Change Transportation Request Based on Outbound Delivery Update Confirmation inbound operation
receives the ID of the original delivery for which the delivery update was requested and a severity code that
shows whether the update was successful. Note that it is not possible to trigger a new delivery update until the
current delivery update has been successfully completed.

## Prerequisites

The Request Outbound Delivery Update [page 143] outbound operation has requested an outbound delivery
update.

## Notes on SAP Implementation

For more information, see the documentation of the Request Outbound Delivery Update [page 143] outbound
operation.

## Enhancements

The Business Add-In (BAdI) BAdI for OutboundDeliveryConfirmation_In_V1(/SCMTMS/TRQ_SE_ODLVCNF1) is
available for this operation.

## More Information

Delivery Splits and Updates Triggered by SAP TM

2.2.1.7

Transportation Quotation Requesting In

## Definition

An interface to create or cancel transportation requests of the category “forwarding quotation”.

Technical Data

## Entity Type

Service Interface

148

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


Category

Direction

B2B

## Inbound

## Business Context and Use

The Transportation Quotation Requesting In inbound service interface groups operations that receive freight
request for quotation (RFQ) data from a customer (for example, a shipper) during a tendering process.

Note that the operations in this service interface are only used in RFQ-based tendering. The operations in the
Transportation Requesting In [page 157] inbound service interface and the Transportation Requesting Out
[page 164]  outbound service interface are used for direct tendering.

Notes on SAP Implementation

## Integration

If a customer also uses SAP Transportation Management (SAP TM), the operations in this service interface
exchange data with the operations in the Transportation Quotation Requesting Out [page 97] outbound service
interface in the Transportation Order Processing [page 5] process component. Otherwise, the operations can
exchange data with an equivalent third-party application that is being used by the customer.

For more information about integration and configuration, see the documentation of the Transportation
Quotation Requesting Out [page 154] outbound service interface.

More Information

Freight Tendering

2.2.1.7.1

Create Transportation Request Quotation

## Definition

To create a transportation request of the category “forwarding quotation”. Prior to confirmation, this
transportation request represents a “forwarding request for quotation”. After confirmation, and provided it has
not been rejected, it represents a “forwarding quotation”.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

149


Technical Data

Entity Type

Release State

Technical Name

## Namespace

## Service Operation

## Released with Restrictions

TransportationRequestQuotationCreateRequest_In

http://sap.com/xi/TMS/Global

Application Component

TM-FWM-FWQ

Category

Direction

## Mode

Idempotency

B2B

## Inbound

Asynchronous

## Not Applicable

P2P Communication Enabled

## Yes

## Business Context and Use

A customer uses RFQ-based tendering to determine which carrier is to execute a particular freight order. The
customer starts the tendering process for a freight order by sending a freight request for quotation (RFQ) to
one or more carriers. It contains relevant data from the freight order, for example, quantities and delivery dates.
Based on this, the carrier can decide whether to submit a forwarding quotation or reject the RFQ. The Create
Transportation Request Quotation inbound operation creates a forwarding request for quotation based on a
freight request for quotation received from a customer. The carrier can then review the forwarding request for
quotation and either accept it (that is, submit a forwarding quotation) or reject it.

## Related Operations

● The corresponding Request Transportation Order Quotation Creation [page 98] outbound operation in the
Transportation Order Processing [page 5]  process component can send a freight request for quotation,
based on which the Create Transportation Request Quotation inbound operation creates a forwarding
request for quotation.

● The Confirm Transportation Request Quotation [page 155]  outbound operation sends a confirmation

indicating whether a carrier has accepted or rejected a forwarding request for quotation received from a
customer.

● The Cancel Transportation Request Quotation [page 152]  inbound operation cancels a forwarding request
for quotation or a forwarding quotation, based on a canceled freight request for quotation received from a
customer.

150

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## Features

The Create Transportation Request Quotation inbound operation receives data such as the following from the
sending system:

● Price limit

● Parties involved (for example, shipper and consignee). Note that if address information is not yet known or

differs from existing master data, the operation automatically creates a deviating address in the
background.

● List of items that represent the goods to be transported and additional information about the goods (for
example, containers, packages, or products, with the respective measurements and quantities, such as
gross volume, gross weight, net weight, and number of pieces)

● Means of transport and locations (for example, ship-from and ship-to location, including address

information)

● Transportation stages and relevant dates (for example, pick-up and delivery dates)

● Transportation terms and delivery terms

## Message Types

● Transportation Request Quotation Create Request

## Prerequisites

A customer has sent a freight request for quotation (for example, using the Request Transportation Order
Quotation Creation [page 98]  outbound operation in the Transportation Order Processing [page 5]  process
component).

## Constraints

In the Item node in the TransportationRequestQuotationCreateRequestMessage message data
type, only StandardID and InternalID of a Product element are supported.

Items of the category “Active Vehicle Resource Item” and “Passive Vehicle Resource Item” are not supported.

Notes on SAP Implementation

## Integration

Note that the forwarding request for quotation is part of the forwarding quotation. Only the term “forwarding
quotation” is used on the user interface.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

151


## Configuration

For more information, see the documentation of the Transportation Quotation Requesting Out [page 154]
 outbound interface.

## Versioning

Note that in SAP TM 1.0, the Request Transportation Order Quotation Creation [page 98]  outbound operation
and the Create Transportation Request Quotation inbound operation shared a common message data type:
TransportationDocumentQuotationCreateRequestMessage. As of SAP TM 1.01, however, these operations use
different message data types that are similar in structure, but not identical. The outbound operation continues
to use message data type TransportationDocumentQuotationCreateRequestMessage, whereas the inbound
operation now uses a separate message data type TransportationRequestQuotationCreateRequestMessage.
As a consequence, a mapping between these message data types is required. In addition, you must implement
Business Add-In (BAdI) BAdI for TransportationRequestQuotationCreateRequest_In (/SCMTMS/
TRQ_SE_TPNRQQ_REQ) to filter out the vehicle resource items, because these items are not supported (see
Constraints).

## Enhancements

The BAdI for TransportationRequestQuotationCreateRequest_In (/SCMTMS/TRQ_SE_TPNRQQ_REQ) Business
Add-In (BAdI) is available for this operation.

2.2.1.7.2

Cancel Transportation Request Quotation

## Definition

To cancel a transportation request of the category “forwarding quotation”.

Technical Data

Entity Type

Release State

Technical Name

## Namespace

## Service Operation

## Released with Restrictions

TransportationRequestQuotationCancellationRequest_In

http://sap.com/xi/TMS/Global

Application Component

TM-FWM-FWQ

Category

Direction

Mode

152

P U B L I C

B2B

## Inbound

## Asynchronous

Enterprise Services and ESR Content
Enterprise Services


Idempotency

## Not Applicable

P2P Communication Enabled

## Yes

## Business Context and Use

A customer uses RFQ-based tendering to determine which carrier is to execute a particular freight order. If the
customer cancels a freight request for quotation that has already been sent to a carrier, the customer informs
the carrier about the cancellation and requests the cancellation of the corresponding forwarding request for
quotation or forwarding quotation. The Cancel Transportation Request Quotation inbound operation cancels a
forwarding request for quotation or forwarding quotation based on a freight request for quotation
cancellation received from a customer.

## Related Operations

The corresponding Request Transportation Order Quotation Cancellation [page 101] outbound operation in the
Transportation Order Processing [page 5] process component can inform a carrier about a canceled freight
request for quotation.

## Features

The Cancel Transportation Request Quotation inbound operation receives the following data from the sending
system:

● ID of the canceled freight request for quotation

● ID of the forwarding quotation that was created based on the freight request for quotation (optional)

## Message Types

● Transportation Request Quotation Cancellation Request

## Prerequisites

The Create Transportation Request Quotation [page 149]  inbound operation has been triggered by a freight
request for quotation received from a customer.

Notes on SAP Implementation

## Configuration

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

153


For more information, see the documentation of the Transportation Quotation Requesting Out [page 154]
 outbound interface.

## Enhancements

The BAdI for TransportationRequestQuotationCancellationReq_In (/SCMTMS/TRQ_SE_TPNRQQ_CNC) Business
Add-In (BAdI) is available for this operation.

2.2.1.8  Transportation Quotation Requesting Out

## Definition

An interface to send notifications or confirmations in response to a request to create a transportation request
of the category “forwarding quotation”.

Technical Data

Entity Type

Category

## Direction

Service Interface

B2B

## Outbound

## Business Context and Use

The Transportation Quotation Requesting Out outbound service interface contains an operation that sends a
confirmation indicating whether a carrier has accepted or rejected a freight request for quotation received
from a customer (for example, a shipper) during a tendering process.

Notes on SAP Implementation

## Integration

● If a customer also uses SAP Transportation Management (SAP TM), the operation in this service interface
exchanges data with the operation in the Transportation Quotation Requesting In [page 148]  inbound
service interface in the Transportation Order Processing [page 5]  process component. Otherwise, the
operation can exchange data with an equivalent third-party application that is being used by the customer.

● A freight request for quotation in the SAP TM back-end system corresponds to an instance of a

Transportation Order [page 6]  business object.

● A forwarding quotation in the SAP TM back-end system corresponds to an instance of a Transportation

Request [page 123] business object.

154

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


Note that the forwarding request for quotation is part of the forwarding quotation. Only the term “forwarding
quotation” is used on the user interface.

## Configuration

You have made the following settings in the SAP TM system:

● You have defined one or more suitable output profiles, and schedule conditions that control whether a

message is sent. You do this in Customizing for Cross-Application Components under  Processes and

Tools for Enterprise Applications Reusable Objects and Functions for BOPF Environment PPF Adapter

for Output Management Maintain PPF Settings .

● You have assigned a suitable output profile to the relevant forwarding quotation types in Customizing for

Transportation Management  under

Forwarding Order Management

Forwarding Quotation Define

Forwarding Quotation Types .

● You have defined a logical system that represents the client from which the outbound communication is to
take place, and you have assigned a queue of the type Outbound Queues to this logical system. You do this

in Customizing for SAP Transportation Management under  SCM Basis

Integration Basic Settings for

Creating the System Landscape Assign Logical System and Queue Type . Here, the logical system must
be marked as an SAP system. Also check the settings in the following Customizing activities: Name Logical
Systems, Assign Logical Systems to a Client, Maintain Business System Group , and Settings for qRFC
Communication.

For more information, see SAP Note 1517523

.

More Information

Freight Tendering

2.2.1.8.1

Confirm Transportation Request Quotation

## Definition

To confirm the receipt of a request to create a transportation request of the category “forwarding quotation”.
The confirmation is either a forwarding quotation or the rejection of a forwarding request for quotation.

Technical Data

Entity Type

Release State

## Service Operation

Released with Restrictions

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

155


Technical Name

## Namespace

TransportationRequestQuotationConfirmation_Out

http://sap.com/xi/TMS/Global

Application Component

TM-FWM-FWQ

Category

Direction

## Mode

Idempotency

B2B

Outbound

Asynchronous

## Not Applicable

P2P Communication Enabled

## Yes

## Business Context and Use

A customer uses RFQ-based tendering to determine which carrier is to execute a particular freight order. When
the customer sends a freight request for quotation to a carrier, the carrier either accepts it by submitting a
quotation, or rejects it.

The Confirm Transportation Request Quotation outbound operation sends a confirmation to a customer. The
confirmation either contains a forwarding quotation or the reason for rejecting the RFQ.

## Related Operations

The corresponding Change Transportation Order Based on Transportation Order Quotation Confirmation [page
107] outbound operation in the Transportation Order Processing [page 5]  process component can receive the
confirmation sent by the Confirm Transportation Request Quotation outbound operation.

## Features

The Confirm Transportation Request Quotation outbound operation can send the following data to the receiving
system, for example:

● If a carrier rejects a freight request for quotation, the operation sends the rejection reason.

● If a carrier accepts a freight request for quotation, the operation sends the ID of the forwarding quotation

and a quotation price, for example.

## Message Types

● Transportation Request Quotation Confirmation

156

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## Prerequisites

The Create Transportation Request Quotation [page 149]  inbound operation has created a forwarding request
for quotation based on a freight request for quotation received from a customer.

Notes on SAP Implementation

## Integration

The Confirm Transportation Request Quotation outbound operation is triggered in the SAP Transportation
Management (SAP TM) back-end system when a carrier either submits a forwarding quotation or rejects an
RFQ.

## Configuration

For more information, see the documentation of the Transportation Quotation Requesting Out [page 154]
 outbound interface.

## Prerequisites

The forwarding quotation must fulfill all schedule conditions that are checked at runtime. You define schedule
conditions in Customizing for Cross-Application Components . For more information, see the documentation of
the Transportation Quotation Requesting Out [page 154]  outbound service interface.

## Versioning

Note that in SAP TM 1.0, the Confirm Transportation Request Quotation outbound operation and the Change
Transportation Order Based on Transportation Order Quotation Confirmation [page 107] inbound
operation shared a common message data type: TransportationDocumentQuotationConfirmationMessage. As
of SAP TM 1.01, however, these operations use different message data types that are similar in structure, but
not identical. The inbound operation continues to use message data type
TransportationDocumentQuotationConfirmationMessage, whereas the outbound operation now uses a
separate message data type TransportationRequestQuotationConfirmationMessage. As a consequence, a
mapping between these message data types is required.

## Enhancements

The BAdI for TransportationRequestQuotationConfirmation_Out (/SCMTMS/TRQ_SE_TPNRQQ_CNF) Business
Add-In (BAdI) is available for this operation.

2.2.1.9  Transportation Requesting In

## Definition

An interface to create, change, or cancel transportation requests of the category “forwarding order”.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

157


Technical Data

Entity Type

Category

## Direction

Service Interface

B2B

## Inbound

## Business Context and Use

The Transportation Requesting In inbound service interface groups operations that create, change, or cancel
forwarding orders, based on freight order data received from a customer (for example, a shipper).

Note that the operations in this service interface can be used to receive orders in a direct tendering scenario.
The operations in the Transportation Quotation Requesting In [page 148] inbound service interface and the
Transportation Quotation Requesting Out [page 154] outbound service interface are used for RFQ-based
tendering.

Notes on SAP Implementation

## Integration

If a customer also uses SAP Transportation Management (SAP TM), the operations in this service interface
exchange data with the operations in the Transportation Ordering Out [page 86]  outbound service interface in
the Transportation Order Processing [page 5] process component. Otherwise, the operations can exchange
data with an equivalent third-party application that is being used by the customer.

For more information about integration and configuration, see the documentation of the Transportation
Requesting Out [page 164] outbound service interface.

## More Information

Forwarding Order Management

## Freight Tendering

2.2.1.9.1  Maintain Transportation Request

## Definition

To create, change, or cancel a transportation request of the category “forwarding order”.

158

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


Technical Data

Entity Type

Release State

Technical Name

## Namespace

## Service Operation

Released with Restrictions

TransportationRequestRequest_In

http://sap.com/xi/TMS/Global

Application Component

TM-FWM-FWO

Category

Direction

## Mode

## Idempotency

Change/Update Behavior

P2P Communication Enabled

Business Context and Use

B2B

## Inbound

Asynchronous

Not Applicable

Type1

## Yes

When a customer subcontracts transportation services to a carrier, the customer sends a freight order to the
carrier. A freight order is the result of planning and contains essential information such as the goods to be
transported and the delivery dates. Based on the freight order, the carrier can then create a forwarding order,
which the carrier uses to plan the execution of the transportation services. The Maintain Transportation
Request  inbound operation creates or changes a forwarding order based on a new or changed freight order
received from a customer.

## Related Operations

● The Maintain Transportation Request inbound operation can create a forwarding order based on a freight
order sent by the corresponding Request Transportation Order [page 88] outbound operation in the
Transportation Order Processing [page 5] process component.

● The Confirm Transportation Request [page 165] outbound operation sends a confirmation indicating

whether a carrier has accepted or rejected a freight order received from a customer.

● The Cancel Transportation Request [page 162] inbound operation cancels a forwarding order based on a

canceled freight order received from a customer.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

159


## Features

The Maintain Transportation Request inbound operation receives data such as the following from the
sending system:

● Freight order ID

● Parties involved (for example, shipper and consignee). Note that if address information is not yet known or

differs from existing master data, the operation automatically creates a deviating address in the
background.

● List of items that represent the goods to be transported and additional information about the goods (for

example, passive vehicle resources, containers, packages, or products, with the respective measurements
and quantities, such as gross volume, gross weight, net weight, and number of pieces)

● List of items that represent the services to be executed and additional information about the service (for

example, quantities and execution date)

● Means of transport and locations, for example, ship-from and ship-to location, including address

information. Note that if address information is not yet known or differs from existing master data, the
operation automatically creates a one-time location in the background.

● Transportation stages and relevant dates (for example, pick-up and delivery dates)

● Transportation terms and delivery terms

● IDs of the business documents related to the freight order, for example, a sales order or purchase order

● Weighing information for verified gross mass (VGM) - relevant for ocean only

## Error Handling

The Maintain Transportation Request  inbound operation checks, for example, whether the required master
data exists. If the master data is not available, the system displays error messages in the business application
log.

## Forwarding Error Handling

The Maintain Transportation Request inbound operation supports Forward Error Handling (FEH). The following
error categories are used:

● DCE: Determination and Conversion Error

● PRE: Processing Error

● PRE.TEE.LRE: Lock Request Error

For more information about the individual error categories, see the code list for the global data type
LogItemCategoryCode .

## Message Types

● Transportation Request Request

160

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## Prerequisites

A customer has sent a freight order (for example, using the Request Transportation Order [page 88] outbound
operation in the Transportation Order Processing [page 5] process component). Note that the Maintain
Transportation Request inbound operation cannot change a forwarding order that has the status  Completed or
Canceled.

## Constraints

In the Item node in the TransportationRequestRequestMessage message data type, only StandardID and
InternalID of a Product element are supported.

Items of the category “Active Vehicle Resource Item” and “Passive Vehicle Resource Item” are not supported.

Notes on SAP Implementation

## Integration

If all involved communication partners use a standard SAP Transportation Management (SAP TM) system, this
operation is used only to create or change a forwarding order. However, some of the communication partners
might have activated a feature called “cancellation with content” by means of enhancement techniques. To
cover this case without requiring complex SAP NetWeaver Process Integration mapping, this operation can
also be used to cancel a forwarding order.

For more information about cancellation with content, see SAP Note 1711010

.

## Configuration

For more information, see the documentation of the Transportation Requesting Out [page 164]  outbound
service interface.

## Versioning

The Maintain Transportation Request inbound operation performs a similar function to the Maintain Freight
Request and Maintain Shipment Request  inbound operations in SAP Transportation Management 7.0 (SAP TM
7.0).

Note that in SAP TM 1.0, the Request Transportation Order [page 88] outbound operation and the Maintain
Transportation Request  inbound operation shared a common message data type:
TransportationDocumentRequestMessage. As of SAP TM 1.01, however, these operations use different
message data types that are similar in structure, but not identical. The outbound operation continues to use
the message data type TransportationDocumentRequestMessage, whereas the inbound operation now uses a
separate message data type TransportationRequestRequestMessage. As a consequence, a mapping between
these message data types is required. In addition, you must implement Business Add-In (BAdI) BAdI for
TransportationRequestRequest_In (/SCMTMS/TRQ_SE_TPNRQ_REQ) to filter out the vehicle resource items,
because these items are not supported (see Constraints).

## Enhancements

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

161


The BAdI for TransportationRequestRequest_In (/SCMTMS/TRQ_SE_TPNRQ_REQ) Business Add-In (BAdI) is
available for this operation.

2.2.1.9.2  Cancel Transportation Request

## Definition

To cancel a transportation request of the category “forwarding order”.

Technical Data

Entity Type

Release State

Technical Name

## Namespace

## Service Operation

## Released with Restrictions

TransportationRequestCancellationRequest_In

http://sap.com/xi/TMS/Global

Application Component

SCM-TM-OM

Category

Direction

## Mode

## Idempotency

Change/Update Behavior

B2B

## Inbound

Asynchronous

Not Applicable

## Not Applicable

P2P Communication Enabled

## Yes

## Business Context and Use

A customer subcontracts transportation services to a carrier. If the customer cancels a freight order that has
already been sent to a carrier, the customer informs the carrier about the cancellation and requests the
cancellation of the corresponding forwarding order.

The Cancel Transportation Request inbound operation cancels a forwarding order based on a freight order
cancellation received from a customer.

Related Operations

162

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


The Cancel Transportation Request inbound operation can cancel a forwarding order based on a freight order
cancellation received from the Request Transportation Order Cancellation [page 91] outbound operation in the
Transportation Order Processing [page 5] process component.

## Features

The Cancel Transportation Request inbound operation receives the following data from the sending system:

● ID of the canceled freight order, or the freight request for quotation ID if the canceled freight order was

based on direct tendering

● ID of the forwarding order that was created based on the freight order (optional)

## Message Types

● Transportation Request Cancellation Request

## Prerequisites

The Maintain Transportation Request [page 158]  inbound operation has created a forwarding order based on a
freight order received from a customer.

Notes on SAP Implementation

## Integration

If all involved communication partners use a standard SAP Transportation Management (SAP TM) system, this
operation is used to cancel a forwarding order. However, some of the communication partners might have
activated a feature called “cancellation with content” by means of enhancement techniques. To cover this case
without requiring complex SAP NetWeaver Process Integration mapping, the Maintain Transportation Request
[page 158] operation can also be used to cancel a forwarding order.

For more information about cancellation with content, see SAP Note 1711010

.

## Configuration

For more information, see the documentation of the  Transportation Requesting Out [page 164]  outbound
service interface.

## Versioning

The Cancel Transportation Request inbound operation performs a similar function to the Cancel Freight
Request and Cancel Shipment Request inbound operations in SAP Transportation Management 7.0 (SAP TM
7.0).

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

163


## Enhancements

The BAdI for TransportationRequestCancellationRequest_In (/SCMTMS/TRQ_SE_TPNRQ_CNC) Business Add-In
(BAdI) is available for this operation.

2.2.1.10  Transportation Requesting Out

## Definition

An interface to send notifications or confirmations in response to a request to create or change a
transportation request of the category “forwarding order”.

Technical Data

Entity Type

Category

## Direction

Business Context and Use

Service Interface

B2B

## Outbound

The Transportation Requesting Out outbound service interface contains an operation that sends a confirmation
indicating whether a carrier has accepted or rejected a freight order received from a customer (for example, a
shipper).

Notes on SAP Implementation

## Integration

● If a customer also uses SAP Transportation Management (SAP TM), the operation in this service interface
exchanges data with the operation in the Transportation Ordering In [page 93]  inbound service interface in
the Transportation Order Processing [page 5] process component. Otherwise, the operation can exchange
data with an equivalent third-party application that is being used by the customer.

● A freight order in the SAP TM back-end system corresponds to an instance of a Transportation Order [page

6] business object.

● A forwarding order in the SAP TM back-end system corresponds to an instance of a Transportation

Request [page 123] business object.

Configuration

164

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


You have made the following settings in the SAP TM system:

● You have defined one or more suitable output profiles, and schedule conditions that control whether a

message is sent. You do this in Customizing for Cross-Application Components under  Processes and

Tools for Enterprise Applications Reusable Objects and Functions for BOPF Environment PPF Adapter

for Output Management Maintain PPF Settings .

● You have assigned a suitable output profile to the relevant forwarding order types. You define

forwarding order types in Customizing for Transportation Management under

Forwarding Order

## Management

Forwarding Order Define Forwarding Order Types .

● You have defined a logical system that represents the client from which the outbound communication is to
take place, and you have assigned a queue of the type Outbound Queues to this logical system. You do this

in Customizing for SAP Transportation Management under  SCM Basis

Integration Basic Settings for

Creating the System Landscape Assign Logical System and Queue Type . Here, the logical system must
be marked as an SAP system. Also check the settings in the following Customizing activities: Name Logical
Systems, Assign Logical Systems to a Client, Maintain Business System Group, and Settings for qRFC
Communication.

For more information, see SAP Note 1517523

.

## More Information

## Forwarding Order Management

2.2.1.10.1  Confirm Transportation Request

## Definition

To confirm the receipt of a request to create or change a transportation request of the category “forwarding
order”.

Technical Data

Entity Type

Release State

Technical Name

## Namespace

## Service Operation

Released with Restrictions

TransportationRequestConfirmation_Out

http://sap.com/xi/TMS/Global

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

165


Application Component

TM-FWM-FWO

Category

Direction

## Mode

## Idempotency

Change/Update Behavior

B2B

Outbound

Asynchronous

Not Applicable

## Not Applicable

P2P Communication Enabled

## Yes

## Business Context and Use

When a customer subcontracts a freight order to a carrier, the carrier is expected to send back a confirmation
that indicates whether the freight order has been accepted or rejected. The Confirm Transportation Request
outbound operation sends a confirmation indicating whether a carrier has accepted or rejected a freight order.

## Related Operations

The corresponding  Change Transportation Order Based on Transportation Order Confirmation [page 94]
inbound operation in the Transportation Order Processing [page 5] process component can receive a
confirmation sent by the Confirm Transportation Request outbound operation.

## Features

The Confirm Transportation Request outbound operation sends an acceptance code that specifies whether a
carrier has accepted or rejected the freight order. The operation can send the following data, for example:

● If a carrier rejects a freight order, the operation sends the rejection reason.

● If a carrier accepts a freight order without changes, the operation sends the ID of the forwarding order and

the confirmed quantities and dates, for example.

● If a carrier accepts a freight order with changes, the operation sends the ID of the forwarding order and the

changed data, for example, changed quantities and dates.

## Message Types

● Transportation Request Confirmation

166

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## Prerequisites

The Maintain Transportation Request [page 158] inbound operation has created a forwarding order based on a
freight order received from a customer.

Notes on SAP Implementation

## Integration

The Confirm Transportation Request outbound operation is triggered in the SAP Transportation Management
(SAP TM) back-end system when a carrier confirms and then saves a forwarding order that was created based
on a freight order received from a customer. It can also be triggered automatically by a background job.

## Configuration

For more information, see the documentation of the Transportation Requesting Out [page 164] outbound
service interface.

## Prerequisites

The forwarding order must fulfill all schedule conditions that are checked at runtime. You define schedule
conditions in Customizing for Cross-Application Components . For more information, see the documentation of
the Transportation Requesting Out [page 164] outbound service interface.

## Versioning

The Confirm Transportation Request outbound operation performs a similar function to the Confirm Freight
Request and Confirm Shipment Request outbound operations in SAP Transportation Management 7.0 (SAP TM
7.0).

Note that in SAP TM 1.0, the Confirm Transportation Request outbound operation and the Change
Transportation Order Based on Transportation Order Confirmation [page 94]  inbound operation shared a
common message data type: TransportationDocumentConfirmationMessage. As of SAP TM 1.01,
however, these operations use different message data types that are similar in structure, but not identical. The
inbound operation continues to use message data type TransportationDocumentConfirmationMessage,
whereas the outbound operation now uses a separate message data
type TransportationRequestConfirmationMessage. As a consequence, a mapping between these message data
types is required.

## Enhancements

The BAdI for TransportationRequestConfirmation_Out (/SCMTMS/TRQ_SE_TPNRQ_CNF) Business Add-In
(BAdI) is available for this operation.

2.2.1.11  Trade Compliance Check Requesting Out

## Definition

An interface to request the processing of a trade compliance check.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

167


Technical Data

Entity Type

Category

## Direction

Business Context and Use

Service Interface

A2A

## Outbound

The Trade Compliance Check Requesting Out outbound service interface groups operations that send data to a
global trade services (GTS) application to request a trade compliance check or to request the cancellation of a
trade compliance check for a forwarding order or forwarding quotation.

Notes on SAP Implementation

## Integration

The operations in this interface and the corresponding inbound interface Trade Compliance Check Requesting
In [page 173] enable you to integrate SAP Transportation Management (SAP TM) with the SAP Global Trade
Services application. Data is exchanged between the GTS Integration (TM-GT-GTS) component in SAP TM and
the GTS: Compliance Management (SLL-LEG-CON) component in SAP Global Trade Services.

Note that a forwarding order or a forwarding quotation in the SAP TM back-end system corresponds to an
instance of a Transportation Request [page 123] business object.

## Configuration

To exchange data with SAP Global Trade Services, you must connect the SAP TM system to the global trade
services (GTS) system and make the required Customizing settings in both systems.

In the SAP TM system, you must enable the trade compliance check for the relevant forwarding order or
forwarding quotation types in Customizing for Transportation Management. For more information, see Trade
Compliance Check.

For information about SAP Global Trade Services, see SAP Library for SAP Global Trade Services on SAP Help

## Portal at http://help.sap.com/grc

 under  SAP Global Trade Services Compliance Management

.

In addition, you have made the following message control settings in SAP TM:

● You have defined one or more suitable output profiles, as well as schedule conditions that control whether

a message is sent. You do this in Customizing for Cross-Application Components under  Processes and

Tools for Enterprise Applications Reusable Objects and Functions for BOPF Environment PPF Adapter

for Output Management Maintain PPF Settings .

● You have assigned a suitable output profile to the relevant forwarding order types and forwarding quotation

types in Customizing for Transportation Management under

Forwarding Order Management

168

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


Forwarding Order Define Forwarding Order Types  and

Forwarding Order Management

## Forwarding

Quotation Define Forwarding Quotation Types .

● You have defined a logical system that represents the client from which the outbound communication is to
take place, and you have assigned a queue of the type Outbound Queues to this logical system. You do this

in Customizing for SCM Basis under

## Integration Basic Settings for Creating the System Landscape

Assign Logical System and Queue Type . Here, the logical system must be marked as an SAP system. Also
check the settings in the following Customizing activities:

○ Name Logical Systems

○ Assign Logical Systems to a Client

○ Maintain Business System Group

○ Settings for qRFC Communication

2.2.1.11.1  Request Trade Compliance Check

## Definition

To request a trade compliance check for a transportation request.

Technical Data

Entity Type

Release State

Technical Name

## Namespace

Application Component

Category

Direction

## Mode

## Idempotency

Change/Update Behavior

P2P Communication Enabled

Service Operation

## Released

TradeComplianceCheckSUITERequest_Out

http://sap.com/xi/TMS/Global

TM-GT-GTS

A2A

Outbound

Asynchronous

Not Applicable

Type 1

## Yes

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

169


## Business Context

You perform a trade compliance check for forwarding orders or forwarding quotations prior to commencing the
required transportation activities and also throughout the ongoing transportation process. The trade
compliance check helps you to ensure that your business transactions comply with international trade
regulations.

The Request Trade Compliance Check outbound operation requests a trade compliance check for a forwarding
order or forwarding quotation. It sends the business document data to a connected global trade services
application.

## Related Operations

● The inbound operation Change Transportation Order Based on Trade Compliance Check Confirmation

[page 174] receives the result of a trade compliance check.

● The outbound operation Request Trade Compliance Check Cancellation [page 171] requests the

cancellation of a trade compliance check.

## Features

The Request Trade Compliance Check outbound operation sends the business document data that is required
to perform the trade compliance check. This comprises the following mandatory data:

● Business partner of the sales organization

● At least one item

● At least the source location country and destination location country (the UNLOCDE or IATA code is not

sufficient)

The operation also sends all business partner IDs (at header and item level), and the address data of a business
partner in case of a deviating address (also at header and item level).

Notes on SAP Implementation

## Integration

The Request Trade Compliance Check outbound operation can send business document data to the Maintain
Trade Compliance Check inbound service operation in the Trade Compliance Processing process component.
This enables you to perform a trade compliance check for an SAP Transportation Management (SAP TM)
forwarding order or forwarding quotation in the SAP Global Trade Services application.

SAP TM sends a business document to the global trade services (GTS) system when a user creates a business
document that is relevant for the trade compliance check (that is, the compliance check has been enabled in
the business document type). If the business document is subsequently changed, SAP TM triggers a trade
compliance check only if the changed fields are relevant for the compliance check (that is, the fields described
in the Features section above). The system blocks a business document that is relevant for the trade
compliance check until the check has been performed and the result is that the document is compliant.

170

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


 Note

● The trade compliance check performed in SAP Global Trade Services for SAP TM consists of

sanctioned party list screening and an embargo check.

● For sanctioned party list screening, SAP Global Trade Services checks address data that is derived only
from business partner master data. It does not check address data derived from locations. In addition,
it does not check addresses that a user enters in the Printing Address field on the Business Partner tab
page in the forwarding order.

● For the embargo check, SAP Global Trade Services checks the countries in the transportation route.

## Configuration

For more information, see Trade Compliance Check Requesting Out [page 167].

## Enhancements

The Business Add-In (BAdI) BAdI for TradeComplianceCheckSUITERequest_Out (/SCMTMS/CPC_SE_CPC_REQ)
is available for this operation.

More Information

## Trade Compliance Check

2.2.1.11.2  Request Trade Compliance Check Cancellation

## Definition

To request the cancellation of a trade compliance check for a transportation request.

Technical Data

Entity Type

Release State

Technical Name

## Namespace

Application Component

Service Operation

## Released

TradeComplianceCheckSUITECancellationRequest_

Out

http://sap.com/xi/TMS/Global

## TM-GT-GTS

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

171


Category

Direction

## Mode

## Idempotency

Change/Update Behavior

P2P Communication Enabled

Business Context

A2A

Outbound

Asynchronous

Not Applicable

Not Applicable

## Yes

You have sent a forwarding order or forwarding quotation to a connected global trade services (GTS)
application to perform a trade compliance check. The GTS application continues to check the business
document until you request the cancellation of the check, for example, because the transportation activities
have been completed or the business document has been canceled.

The Request Trade Compliance Check Cancellation outbound operation requests the cancellation of a trade
compliance check for a forwarding order or forwarding quotation.

## Features

The Request Trade Compliance Check Cancellation outbound operation sends the ID of the business document
for which the trade compliance check is to be canceled.

## Prerequisites

The Request Trade Compliance Check [page 169] outbound operation has requested a trade compliance
check.

Notes on SAP Implementation

## Integration

The Request Trade Compliance Check Cancellation outbound operation can send business document data to
the Cancel Trade Compliance Check inbound operation in the Trade Compliance Processing process
component. This enables you to cancel a trade compliance check for an SAP Transportation Management
(SAP TM) business document in the SAP Global Trade Services application.

172

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


SAP TM sends a cancellation if the transportation activities have been completed (life cycle status of the
business document is Executed) or if the business document has been canceled (life cycle status of the
business document is Canceled). The document that was created in SAP Global Trade Services is canceled
accordingly.

## Configuration

For more information, see Trade Compliance Check Requesting Out [page 167].

## Enhancements

The Business Add-In (BAdI) BAdI for TradeComplianceCheckSUITECancellationRequest_Out (/SCMTMS/
CPC_SE_CPC_CANCREQ) is available for this operation.

More Information

## Trade Compliance Check

2.2.1.12  Trade Compliance Check Requesting In

## Definition

An interface to receive confirmations of requests for a trade compliance check.

Technical Data

Entity Type

Category

## Direction

Business Context and Use

Service Interface

A2A

## Inbound

The Trade Compliance Check Requesting In inbound service interface contains an operation that receives the
result of a trade compliance check from a global trade services (GTS) application.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

173


## Notes on SAP Implementation

For more information, see Trade Compliance Check Requesting Out [page 167].

2.2.1.12.1  Change Transportation Request Based on Trade

Compliance Check Confirmation

## Definition

To change a transportation request of the category “forwarding order” or “forwarding quotation” based on the
confirmation of a trade compliance check.

Technical Data

Entity Type

Release State

Technical Name

## Namespace

Application Component

Category

Direction

## Mode

## Idempotency

Change/Update Behavior

P2P Communication Enabled

Business Context

Service Operation

## Released

TradeComplianceCheckSUITEConfirmation_In

http://sap.com/xi/TMS/Global

TM-GT-GTS

A2A

## Inbound

Asynchronous

Not Applicable

Not Applicable

## Yes

You have sent a forwarding order or forwarding quotation to a connected global trade services (GTS)
application to perform a trade compliance check. The GTS application checks the business document and
returns the result of the check, that is, whether or not the business document complies with the relevant
international trade regulations.

174

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


The inbound operation Change Transportation Request Based on Trade Compliance Check Confirmation
receives the result of the check and updates the status of the forwarding order or forwarding quotation
accordingly.

## Features

The inbound operation Change Transportation Request Based on Trade Compliance Check Confirmation
receives an indicator that specifies whether the business document is compliant. It sets the status of the
business document based on this value.

## Prerequisites

The Request Trade Compliance Check [page 169] outbound operation has requested a trade compliance
check.

## Error Handling

## Forward Error Handling

The inbound operation Change Transportation Request Based on Trade Compliance Check Confirmation
supports Forward Error Handling (FEH). The following error categories are used:

● DCE: Determination and Conversion Error

● PRE: Processing Error

● PRE.TEE.LRE: Lock Request Error

For more information about the individual error categories, see the code list for the global data type
LogItemCategoryCode.

Notes on SAP Implementation

## Integration

The inbound operation Change Transportation Request Based on Trade Compliance Check Confirmation can
receive the result of a trade compliance check from the Confirm Trade Compliance Check outbound operation
in the Trade Compliance Processing process component. This enables you to receive the result of a trade
compliance check that was performed in the SAP Global Trade Services application for an SAP Transportation
Management (SAP TM) business document.

When SAP TM receives the result of the check, it sets the compliance status of the business document to
Compliant or Not Compliant. The system blocks a business document that is relevant for the compliance check
until a trade compliance check has been performed and until the check determines that the business
document is compliant.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

175


## Configuration

For more information, see Trade Compliance Check Requesting Out [page 167].

## Enhancements

The Business Add-In (BAdI) BAdI for TradeComplianceCheckSUITEConfirmation_In (/SCMTMS/
CPC_SE_CPC_CNF) is available for this operation.

More Information

Trade Compliance Check

2.3  Freight Agreement Processing

## Definition

The requesting of agreement quotations or agreements from carriers.

Technical Data

Entity Type

## Technical Name

Business Context and Use

## Process Component

## FreightAgreementProcessing

The FreightAgreementProcessing  process component enables shippers or logistics service providers
(LSPs) to send freight agreement RFQs or freight agreements to multiple carriers for transporting goods. Each
carrier can respond to the freight agreement RFQ or freight agreements with the prices and services that it can
offer.

Since the shipper or LSP sends freight agreement RFQs or freight agreements to multiple carriers, the shipper
or LSP receives a competitive price from each carrier. Also, the shipper or LSP can spread the business share
among multiple carriers to ensure reliable transportation of goods.

176

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


Notes on SAP Implementation

## Integration

The operations in the service interfaces exchange data with equivalent third-party applications used by the
carriers.

A freight agreement RFQ or freight agreement in SAP Transportation Management (SAP TM) corresponds to
an instance of a Freight Agreement business object.

## More Information

SAP Transportation Management (SAP TM)

2.3.1  Freight Agreement

## Definition

An agreement between a shipper and a carrier that establishes a long-term contractual relationship and that
defines rates for transportation services. The agreement can also have the character of a freight agreement
request for quotation that is initiated by a shipper.

Technical Data

Entity Type

Technical Name

## Object Category

Business Context and Use

Business Object

FreightAgreement

## Business Process Object

The Freight Agreement business object enables the following transportation activities to be carried out by
shippers and LSPs:

● The shipper or LSP sends out a freight agreement RFQ or freight agreement to one or more carriers for

price, quantity, and transportation conditions to transport goods.

● Carriers respond with quotations or agreements based on the requirements in the freight agreement RFQ

or agreement.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

177


These activities enable the shipper or LSP to acquire the best price and service from various carriers. The
shipper or LSP can easily determine the business share that a carrier receives. This enables the shipper or LSP
to ensure the reliable transport of goods at the best price.

## More Information

Freight Agreement Processing [page 176]

2.3.1.1

Freight Agreement Requesting In

## Definition

An interface to receive responses from a carrier or logistics service provider for a freight agreement.

Technical Data

Entity Type

Category

## Direction

Business Context and Use

Service Interface

B2B

## Inbound

The Freight Agreement Requesting In inbound service interface contains an operation that receives responses
for freight agreements.

2.3.1.1.1  Maintain Freight Agreement

## Definition

To process a forwarding agreement received from a carrier.

178

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


Technical Data

Entity Type

Release State

Technical Name

## Namespace

Application Component

Category

Direction

## Mode

## Idempotency

P2P Communication Enabled

Service Operation

## Released

FreightAgreementRequest_In

http://sap.com/xi/TMS/Global

TM-FRA

B2B

## Inbound

Asynchronous

No

## Yes

## Business Context and Use

A shipper or logistics service provider (LSP) uses a transportation management system to carry out
transportation planning for the next fiscal year. As part of the planning, the shipper or LSP wants to start a
bidding process to create freight agreements with carriers. The shipper or LSP creates a freight agreement
RFQ master that contains agreement-relevant information such as:

● Commodities to be shipped

● Capacities

● Trade lanes

● Service levels

● Transportation modes

The shipper or LSP sends the freight agreement RFQs to carriers and the carriers respond to the freight
agreement RFQ with their quotes. The shipper or LSP can consolidate these quotes and decide which carriers
should be used for the transportation process.

If the shipper or LSP decides on a carrier, the carrier can create and release a forwarding agreement. The
shipper or LSP uses the service operation FreightAgreementRequest_In inbound to receive the forwarding
agreement and to create a freight agreement in the shipper's or LSP system.

## Message Types

● TransportationAgreementRequest

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

179


Notes on SAP Implementation

## Integration

If a carrier also uses SAP Transportation Management (SAP TM), the operation exchanges data with the
operation ForwardingAgreementRequest_Out. Otherwise, the operation can exchange data with an
equivalent third-party application that is being used by the carrier. For more information, see Maintain
Forwarding Agreement [page 200].

2.3.1.2

Freight Agreement Requesting Out

## Definition

An interface to send freight agreements to carriers.

Technical Data

Entity Type

Category

## Direction

Business Context and Use

Service Interface

B2B

## Outbound

The Freight Agreement Requesting Out outbound service interface contains an operation that sends agreement
data to carriers. When shippers or logistics service providers start transportation planning for the next fiscal
year, they can use the operation to send agreements to carriers.

2.3.1.2.1

Request Freight Agreement

## Definition

To send a freight agreement to a carrier.

180

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


Technical Data

Entity Type

Release State

Technical Name

## Namespace

Application Component

Category

Direction

## Mode

## Idempotency

P2P Communication Enabled

Service Operation

## Released

FreightAgreementRequest_Out

http://sap.com/xi/TMS/Global

TM-FRA

B2B

Outbound

Asynchronous

No

## Yes

## Business Context and Use

A shipper or logistics service provider (LSP) uses a transportation management system to carry out
transportation planning for the next fiscal year. As part of the planning, the shipper or LSP wants to start a
bidding process to create freight agreements with carriers. The shipper or LSP creates a freight agreement
RFQ master that contains agreement-relevant information such as:

● Commodities to be shipped

● Capacities

● Trade lanes

● Service levels

● Transportation modes

The shipper or LSP sends the freight agreement RFQs to carriers and the carriers respond to the freight
agreement RFQ with their quotes. The shipper or LSP can consolidate these quotes and decide which carriers
should be used for the transportation process.

After the shipper or LSP has decided to use the services of a particular carrier, the shipper or LSP creates and
releases a freight agreement. The shipper or LSP can use the service operation
FreightAgreementRequest_Out outbound to create a forwarding agreement in the carrier's system.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

181


## Features

The Request Freight Agreement outbound operation sends the following data to a carrier:

● Contract period

● List of items that represent the goods to be transported

● Information about the goods:

○ Items such as containers, packages, or products

○ Measurements such as gross volume, gross weight, net weight, and quantity

● Means of transport and locations

● Transportation terms such as the service levels and the transportation modes

## Message Types

● TransportationAgreementRequest

Notes on SAP Implementation

## Integration

If a carrier also uses SAP Transportation Management (SAP TM), the operation exchanges data with the
operation ForwardingAgreementRequest_In. Otherwise, the operation can exchange data with an
equivalent third-party application that is being used by the carrier. For more information, see Maintain
Forwarding Agreement [page 200].

2.3.1.3

Freight Agreement Quotation Notification In

## Definition

An interface to receive responses from a carrier or logistics service provider for all the items in a freight
agreement RFQ master.

Technical Data

Entity Type

Category

182

## P U B L I C

Service Interface

B2B

Enterprise Services and ESR Content
Enterprise Services


Direction

## Inbound

## Business Context and Use

The Freight Agreement Quotation Notification In inbound service interface contains an operation that receives
responses for all the items in a freight agreement RFQ.

2.3.1.3.1

Change Freight Agreement RFQ Based on
Notification

## Definition

To receive a response for all the items in a freight agreement RFQ from a logistics service provider (LSP) or
carrier.

Technical Data

Entity Type

Release State

Technical Name

## Namespace

Service Operation

## Released

FreightAgreementQuotationNotification_In

http://sap.com/xi/TMS/Global

Application Component

TM-FRA-RFQ

Category

Direction

## Mode

## Idempotency

P2P Communication Enabled

B2B

## Inbound

Asynchronous

No

## Yes

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

183


## Business Context and Use

You use SAP Transportation Management system to carry out transportation planning for the next fiscal year.
As part of the planning, you want to start a bidding process to create agreements with carriers or LSPs. You
create a freight agreement RFQ master that contains agreement-relevant information such as:

● Commodities to be shipped

● Capacities

● Trade lanes

● Service levels

● Transportation modes

You send the freight agreement RFQs to carriers or LSPs and they respond to the freight agreement RFQ with
their rates.

Note that a carrier or an LSP can proactively create and send rates for a set of items. You can use this operation
to receive this document as well.

The ForwardingAgreementQuotationNotificationIn inbound operation enables you to receive a carrier's
response to the freight agreement RFQ master for all the items specified.

## Message Types

● FreightAgreementQuotationNotification_In

Notes on SAP Implementation

## Integration

This operation exchanges data with the carrier’s or LSP’s Forwarding Agreement Quotation Notification Out
[page 197] outbound service interface in the Forwarding Agreement Processing [page 190] process
component. The operation can also exchange data with an equivalent third-party application that is being used
by the carrier or LSP.

For more information about integration and configuration, see Forwarding Agreement Quotation Notification
Out [page 197] outbound interface.

2.3.1.4

Freight Agreement Quotation Requesting In

## Definition

An interface to process responses from carriers to freight agreement RFQs.

184

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


Technical Data

Entity Type

Category

## Direction

Business Context and Use

Service Interface

B2B

## Inbound

The Freight Agreement Quotation Requesting In inbound service interface contains an operation that processes
responses from carriers to the freight agreement RFQs sent by the shipper or logistics service provider.

2.3.1.4.1

Change Freight Agreement RFQ Based on
Confirmation

## Definition

To process a response from a carrier to a freight agreement RFQ.

Technical Data

Entity Type

Release State

Technical Name

## Namespace

Service Operation

## Released

FreightAgreementQuotationConfirmation_In

http://sap.com/xi/TMS/Global

Application Component

TM-FRA-RFQ

Category

Direction

## Mode

Idempotency

B2B

## Inbound

Asynchronous

No

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

185


P2P Communication Enabled

## Yes

## Business Context and Use

A shipper or logistics service provider (LSP) uses a transportation management system to carry out
transportation planning for the next fiscal year. As part of the planning, the shipper or LSP wants to start a
bidding process to create freight agreements with carriers. The shipper or LSP creates a freight agreement
RFQ master that contains agreement-relevant information such as:

● Commodities to be shipped

● Capacities

● Trade lanes

● Service levels

● Transportation modes

The shipper or LSP sends the freight agreement RFQs to carriers and the carriers respond to the freight
agreement RFQ with their quotes. The shipper or LSP can consolidate these quotes and decide which carriers
should be used for the transportation process.

The FreightAgreementQuotationConfirmation_In inbound operation receives the quote sent by a
carrier and saves the data in the carrier’s individual freight agreement RFQ. The freight agreement RFQ
includes the following details:

● The capacity that the carrier can provide for a requested capacity

● The rates at which the carrier can provide the transportation service

## Message Types

● FreightAgreementQuotationConfirmation_In

Notes on SAP Implementation

## Integration

If a carrier also uses SAP Transportation Management (SAP TM), the operation in this service interface
exchanges data with the operation in the Forwarding Agreement Quotation Requesting Out [page 194]
outbound service interface in the Forwarding Agreement Processing [page 190] process component.
Otherwise, the operation can exchange data with an equivalent third-party application that is being used by the
carrier.

For more information about integration and configuration, see Forwarding Agreement Quotation Requesting
Out [page 194] outbound interface.

186

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


2.3.1.5

Freight Agreement Quotation Requesting Out

## Definition

An interface to send freight agreement RFQs to carriers.

Technical Data

Entity Type

Category

## Direction

Business Context and Use

Service Interface

B2B

## Outbound

The Freight Agreement Quotation Requesting Out outbound service interface contains an operation that sends
RFQ data to carriers. When shippers or logistics service providers start transportation planning for the next
fiscal year, they can use the operation to request quotations.

2.3.1.5.1

Request Freight Agreement Quotation

## Definition

To request the processing of a new freight agreement RFQ master.

Technical Data

Entity Type

Release State

Technical Name

## Namespace

Service Operation

## Released

FreightAgreementQuotationRequest_Out

http://sap.com/xi/TMS/Global

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

187


Application Component

Category

Direction

## Mode

## Idempotency

P2P Communication Enabled

Business Context and Use

TM-FRA-RFQ

B2B

Outbound

Asynchronous

No

## Yes

A shipper or logistics service provider (LSP) uses a transportation management system to carry out
transportation planning for the next fiscal year. As part of the planning, the shipper or LSP wants to start a
bidding process to create agreements with carriers. The shipper or LSP creates a freight agreement RFQ
master that contains agreement-relevant information such as:

● Commodities to be shipped

● Capacities

● Trade lanes

● Service levels

● Transportation modes

The shipper or LSP sends the freight agreement RFQs to carriers and the carriers respond to the freight
agreement RFQ with their quotes. The shipper or LSP can consolidate these quotes and decide which carriers
should be used for the transportation process.

The Freight Agreement Quotation Request outbound operation sends the freight agreement RFQ to the carriers.

## Features

The Freight Agreement Quotation Request outbound operation sends the following data to the carrier system:

● Contract period

● List of items that represent the goods to be transported

● Information about the goods:

○ Items such as containers, packages, or products

○ Measurements and quantities such as gross volume, gross weight, net weight, and quantity

● Means of transport and locations

● Transportation terms such as service levels and transportation modes

188

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## Message Types

● Freight Agreement Quotation Request

## Prerequisites

To use this operation, the freight agreement RFQ master must fulfill all the schedule conditions that are
checked at runtime. You define schedule conditions in Customizing for Cross-Application Components under

Processes and Tools for Enterprise Applications Reusable Objects and Functions for BOPF Environment

PPF Adapter for Output Management Maintain PPF Settings.

.

Notes on SAP Implementation

## Integration

The Freight Agreement Quotation Request outbound operation is triggered by the manual publication of a
freight agreement RFQ master in SAP Transportation Management (SAP TM).

## Configuration

You make the following settings in SAP TM:

● Define schedule conditions that control whether a message is sent

You make these settings in Customizing for Cross-Application Components under  Processes and Tools

for Enterprise Applications Reusable Objects and Functions for BOPF Environment PPF Adapter for

Output Management Maintain PPF Settings .

● Define a logical system that represents the client from which the outbound communication is to take place,

and you have assigned a queue of the type Outbound Queues to this logical system.

You make these settings in Customizing for SAP Transportation Management under   SCM Basis

Integration Basic Settings for Creating the System Landscape Assign Logical System and Queue Type .
You must mark the logical system as an SAP system. Also, check the settings in the following Customizing
activities:

○ Name Logical Systems

○ Assign Logical Systems to a Client

○ Maintain Business System Group

○ Settings for qRFC Communication

● Define output management adapter settings in Customizing for Cross-Application Components under

Processes and Tools for Enterprise Applications Reusable Objects and Functions for BOPF Environment

PPF Adapter for Output Management Maintain Output Management Adapter Settings   .

 Note

The /SCMTMS/FAG_RFQ_B2B action profile is provided in the standard Customizing settings and assigned
to the node  ROOT of the /SCMTMS/FREIGHTAGREEMENT business object. If required, you can replace this
assignment by specifying another suitable action profile. Note that removing this assignment without

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

189


replacing it with another one disables outbound communication through the Freight Agreement Quotation
Requesting Out [page 187] outbound service interface.

2.4  Forwarding Agreement Processing

## Definition

A process to send a carrier’s agreement and quotation details to a shipper or logistics service provider (LSP).

Technical Data

Entity Type

## Technical Name

Business Context and Use

## Process Component

## ForwardingAgreementProcessing

The ForwardingAgreementProcessing process component enables carriers to carry out the following activities

● To provide a quote or agreement based on the information in a freight agreement RFQ master or freight

agreement sent by a shipper or LSP

● To proactively send its rates to a shipper or LSP

● To automatically create a forwarding agreement if the shipper or LSP accepts the quotation

These activities enable the carrier to plan transportation activities for the future. It enables the carrier to
provide the best price and service for the transportation of goods to a shipper or LSP while maintaining a profit.

Notes on SAP Implementation

## Integration

You must use SAP Transportation Management to use this feature.

## More Information

SAP Transportation Management (SAP TM)

190

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


2.4.1  Forwarding Agreement

## Definition

A business object that a carrier uses to respond to the shipper or logistics service provider request for rates for
transportation services. The business object can also be used to establish a long-term contract that represents
the contractual relationship with a shipper or logistics service provider to whom you, as a carrier, are selling
transportation services.

Technical Data

Entity Type

Technical Name

## Object Category

Business Context and Use

## Business Object

ForwardingAgreementRequest

## Business To Business

The ForwardingAgreementRequest business object enables carriers to carry out the following activities:

● To provide a quote or agreement based on the information in a freight agreement RFQ master or freight

agreement sent by a shipper or LSP

● To proactively send a carrier's rates in a forwarding agreement quotation to a shipper or LSP

● To automatically create a forwarding agreement if the shipper or LSP accepts a quotation

These activities enable the carrier to plan transportation activities for the future. It enables the carrier to
provide the best price and service for the transportation of goods to a shipper or LSP while maintaining a profit.

## More Information

Forwarding Agreement Processing [page 190]

2.4.1.1

Forwarding Agreement Quotation Requesting In

## Definition

An interface to receive freight agreement RFQ masters from shippers or logistics service providers (LSPs).

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

191


Technical Data

Entity Type

Category

## Direction

Service Interface

B2B

## Inbound

## Business Context and Use

The Forwarding Agreement Quotation Requesting In  inbound service interface contains an operation that
receives freight agreement RFQ masters sent by shippers or LSPs.

2.4.1.1.1  Maintain Forwarding Agreement Quotation

## Definition

To process a freight agreement RFQ master received from a shipper or logistics service provider (LSP).

Technical Data

Entity Type

Release State

Technical Name

## Namespace

Service Operation

## Released

ForwardingAgreementQuotationRequest_In

http://sap.com/xi/TMS/Global

Application Component

TM-FWA-RFQ

Category

Direction

## Mode

## Idempotency

P2P Communication Enabled

SAP B2B

## Inbound

Asynchronous

No

Yes

192

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## Business Context and Use

A shipper or LSP uses a transportation management system to carry out transportation planning for the next
fiscal year. As part of the planning, the shipper or LSP wants to start a bidding process to create freight
agreements with carriers. The shipper or LSP creates a freight agreement RFQ master that contains
agreement-relevant information such as:

● Commodities to be shipped

● Capacities

● Trade lanes

● Service levels

● Transportation modes

The shipper or LSP sends the freight agreement RFQ masters to carriers and the carriers respond to the freight
agreement RFQ masters with its quotes. The shipper or LSP can consolidate these quotes and decide which
carriers should be used for the transportation process.

The Forwarding Agreement Quotation Request inbound can be used by a carrier to create a forwarding
agreement RFQ after receiving a freight agreement RFQ master from the shipper or LSP. The forwarding
agreement RFQ contains the transportation requirements specified by the shipper or LSP in the freight
agreement RFQ master.

## Features

The ForwardingAgreementQuotationRequest_In operation receives the following data from the shipper
or LSP:

● Contract period

● List of items that represent the goods to be transported

● Information about the goods:

○ Items such as containers, packages, or products

○ Measurements such as gross volume, gross weight, net weight, and quantity

● Means of transport and locations

● Transportation terms such as the service levels and the transportation modes

## Message Types

● FreightAgreementQuotation

Notes on SAP Implementation

## Integration

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

193


If a carrier also uses SAP Transportation Management (SAP TM), the operation in this service interface
exchanges data with the operation in the Freight Agreement Quotation Request Out outbound service interface
in the Freight Agreement Quotation Processing process component. Otherwise, the operation can exchange
data with an equivalent third-party application used by the carrier. For more information about integration and
configuration, see Freight Agreement Quotation Requesting Out [page 187].

## More Information

Forwarding Agreement Quotation Requesting In [page 191]

2.4.1.2

Forwarding Agreement Quotation Requesting Out

## Definition

An interface to send responses to freight agreement RFQ masters received from shippers or logistics service
providers (LSPs).

Technical Data

Entity Type

Category

## Direction

Business Context and Use

Service Interface

B2B

## Outbound

The Forwarding Agreement Quotation Requesting Out outbound service interface contains an operation that
sends responses to freight agreement RFQ masters received from a shipper or LSP.

## More Information

Forwarding Agreement Quotation [page 191]

194

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


2.4.1.2.1

Confirm Forwarding Agreement Quotation

## Definition

To send a response to a freight agreement RFQ master received from a shipper or logistics service provider
(LSP).

Technical Data

Entity Type

Release State

Technical Name

## Namespace

Service Operation

## Released

ForwardingAgreementQuotationConfirmation_Out

http://sap.com/xi/TMS/Global

Application Component

TM-FWA-RFQ

Category

Direction

## Mode

## Idempotency

P2P Communication Enabled

Business Context and Use

SAP B2B

Outbound

Asynchronous

No

## Yes

A shipper or LSP uses a transportation management system to carry out transportation planning for the next
fiscal year. As part of the planning, the shipper or LSP wants to start a bidding process to create freight
agreements with carriers. The shipper or LSP creates a freight agreement RFQ master that contains
agreement-relevant information, such as:

● Commodities to be shipped

● Capacities

● Trade lanes

● Service levels

● Transportation modes

The shipper or LSP sends the freight agreement RFQs to carriers and the carriers respond to the freight
agreement RFQ with their quotes. The shipper or LSP can consolidate these quotes and decide which carriers
should be used for the transportation process.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

195


The Forwarding Agreement Quotation Confirmation outbound operation sends a carrier's response to the
shipper’s or LSP's freight agreement RFQ master. The responses include the following:

● The total capacity that the carrier can provide

● The rate at which the carrier can offer the transportation services

## Message Types

● FreightAgreementQuotation

## Prerequisites

To use this operation, the freight agreement RFQ master must fulfill all the schedule conditions that are
checked during execution.You define schedule conditions in Customizing for Cross-Application Components

under  Processes and Tools for Enterprise Applications Reusable Objects and Functions for BOPF

Environment PPF Adapter for Output Management Maintain PPF Settings .

Notes on SAP Implementation

## Integration

The Forwarding Agreement Quotation Confirmation outbound operation is triggered when the carrier submits
the response to the shipper’s or LSP's freight agreement RFQ master.

## Configuration

You make the following settings in SAP Transportation Management system:

● Define schedule conditions that control whether a message is sent.

You make these settings in Customizing for  Cross-Application Components under  Processes and Tools

for Enterprise Applications Reusable Objects and Functions for BOPF Environment PPF Adapter for

Output Management Maintain PPF Settings .

● Define a logical system that represents the client from which the outbound communication is to take place,

and assign a queue of the type Outbound Queues to this logical system.

You make these settings in Customizing for SAP Transportation Management under  SCM Basis

Integration Basic Settings for Creating the System Landscape Assign Logical System and Queue Type .
You must mark the logical system as an SAP system. Also, check the settings in the following Customizing
activities:

○ Name Logical Systems

○ Assign Logical Systems to a Client

○ Maintain Business System Group

○ Settings for qRFC Communication

196

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


● Define output management adapter settings for Cross-Application Components under  Processes and

Tools for Enterprise Applications Reusable Objects and Functions for BOPF Environment PPF Adapter

for Output Management Maintain Output Management Adapter Settings  .

 Note

The /SCMTMS/FAG_RFQ_B2B  action profile is provided in the standard Customizing settings and assigned
to the ROOT node of the /SCMTMS/FREIGHTAGREEMENT business object. If required, you can replace this
assignment by specifying another suitable action profile. Note that removing this assignment without
replacing it with another one disables outbound communication through the Forwarding Agreement
Quotation Requesting Out [page 194] outbound service interface..

2.4.1.3

Forwarding Agreement Quotation Notification Out

## Definition

An interface for you as a carrier to send rates for all the items in a freight agreement RFQ masters received
from shippers or logistics service providers (LSPs).

Technical Data

Entity Type

Category

## Direction

Business Context and Use

Service Interface

B2B

## Outbound

The Forwarding Agreement Quotation Notification Out outbound service interface contains an operation that
sends responses for all the items in a forwarding agreement quotation to a logistics service provider or a
shipper.

## More Information

Forwarding Agreement Quotation [page 191]

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

197


2.4.1.3.1  Notify Forwarding Agreement Quotation

## Definition

This service operation enables you as a carrier to send rates for all items in a freight agreement RFQ master
received from a shipper or logistics service provider (LSP).

Technical Data

Entity Type

Release State

Technical Name

## Namespace

Service Operation

## Released

ForwardingAgreementQuotationNotification_Out

http://sap.com/xi/TMS/Global

Application Component

TM-FWA-RFQ

Category

Direction

## Mode

## Idempotency

P2P Communication Enabled

Business Context and Use

SAP B2B

Outbound

Asynchronous

No

## Yes

A shipper or LSP sends you a freight agreement RFQ master that contains items. Each of the items can specify
agreement-relevant information such as:

● Commodities to be shipped

● Capacities

● Trade lanes

● Service levels

● Transportation modes

The system displays the freight agreement RFQ master as a forwarding agreement quotation in your system.
Subsequently, you specify the rates you can provide for individual items in the forwarding agreement quotation
and send it back to the shipper or LSP.

Note that you can proactively create and send a forwarding agreement quotation with rates for a set of items to
a shipper or LSP.

198

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


The ForwardingAgreementQuotationNotificationOut outbound operation enables you to send a
response to the shipper or LSP for the items, all at once.

## Message Types

● ForwardingAgreementQuotation

## Prerequisites

To use this operation, the freight agreement RFQ master must fulfill all the schedule conditions that are
checked during execution.You define schedule conditions in Customizing for Cross-Application Components

under  Processes and Tools for Enterprise Applications Reusable Objects and Functions for BOPF

Environment PPF Adapter for Output Management Maintain PPF Settings .

Notes on SAP Implementation

## Integration

The Forwarding Agreement Quotation Notification outbound operation is triggered when you send a response to
all the items in a forwarding agreement quotation or when you proactively send rates for all the items in a
forwarding agreement quotation you have created.

## Configuration

You make the following settings in SAP Transportation Management system:

● Define schedule conditions that control whether a message is sent.

You make these settings in Customizing for  Cross-Application Components under  Processes and Tools

for Enterprise Applications Reusable Objects and Functions for BOPF Environment PPF Adapter for

Output Management Maintain PPF Settings .

● Define a logical system that represents the client from which the outbound communication is to take place,

and assign a queue of the type Outbound Queues to this logical system.

You make these settings in Customizing for SAP Transportation Management under  SCM Basis

Integration Basic Settings for Creating the System Landscape Assign Logical System and Queue Type .
You must mark the logical system as an SAP system. Also, check the settings in the following Customizing
activities:

○ Name Logical Systems

○ Assign Logical Systems to a Client

○ Maintain Business System Group

○ Settings for qRFC Communication

● Define output management adapter settings for Cross-Application Components under  Processes and

Tools for Enterprise Applications Reusable Objects and Functions for BOPF Environment PPF Adapter

for Output Management Maintain Output Management Adapter Settings  .

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

199


 Note

The /SCMTMS/FWAQ_B2B  action profile is provided in the standard Customizing settings and assigned to
the ROOT node of the /SCMTMS/FREIGHTAGREEMENT business object. If required, you can replace this
assignment by specifying another suitable action profile. Note that removing this assignment without
replacing it with another one disables outbound communication through the Forwarding Agreement
Quotation Notification Out [page 197] outbound service interface..

2.4.1.4

Forwarding Agreement Requesting In

## Definition

An interface to receive freight agreements from shippers or logistics service providers (LSPs).

Technical Data

Entity Type

Category

## Direction

Business Context and Use

Service Interface

B2B

## Inbound

The ForwardingAgreementRequestingIn inbound service interface contains an operation that receives freight
agreement sent by shippers or LSPs.

2.4.1.4.1  Maintain Forwarding Agreement

## Definition

To process a freight agreement received from a shipper or logistics service provider (LSP).

200

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


Technical Data

Entity Type

Release State

Technical Name

## Namespace

Application Component

Category

Direction

## Mode

## Idempotency

P2P Communication Enabled

Service Operation

## Released

ForwardingAgreementRequest_In

http://sap.com/xi/TMS/Global

TM-FWA

B2B

## Inbound

Asynchronous

No

## Yes

## Business Context and Use

A shipper or logistics service provider (LSP) uses a transportation management system to carry out
transportation planning for the next fiscal year. As part of the planning, the shipper or LSP wants to start a
bidding process to create freight agreements with carriers. The shipper or LSP creates a freight agreement
RFQ master that contains agreement-relevant information such as:

● Commodities to be shipped

● Capacities

● Trade lanes

● Service levels

● Transportation modes

The shipper or LSP sends the freight agreement RFQs to carriers and the carriers respond to the freight
agreement RFQ with their quotes. The shipper or LSP can consolidate these quotes and decide which carriers
should be used for the transportation process.

After the shipper or LSP has decided to use the services of a particular carrier, the shipper or LSP creates and
releases a freight agreement. The carrier uses the service operation ForwardingAgreementRequest_In
inbound to create a forwarding agreement in the carrier's system.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

201


## Features

The ForwardingAgreementRequest_In inbound operation receives the following data from the shipper or
LSP:

● Contract period

● List of items that represent the goods to be transported

● Information about the goods:

○ Items such as containers, packages, or products

○ Measurements such as gross volume, gross weight, net weight, and quantity

● Means of transport and locations

● Transportation terms such as the service levels and the transportation modes

## Message Types

● TransportationAgreementRequest

Notes on SAP Implementation

## Integration

If a shipper or LSP also uses SAP Transportation Management (SAP TM), the operation exchanges data with
the operation FreightAgreementRequest_Out. Otherwise, the operation can exchange data with an
equivalent third-party application used by the carrier. For more information, see Request Freight Agreement
[page 180].

2.4.1.5

Forwarding Agreement Requesting Out

## Definition

An interface to send responses to freight agreements received from shippers or logistics service providers
(LSPs).

Technical Data

## Entity Type

Service Interface

202

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


Category

Direction

B2B

## Outbound

## Business Context and Use

The ForwardingAgreementRequestingOut outbound service interface contains an operation that sends
responses to freight agreements received from a shipper or LSP.

## More Information

Forwarding Agreement Quotation [page 191]

2.4.1.5.1

Request Forwarding Agreement

## Definition

To send a forwarding agreement to a shipper or logistics service provider (LSP).

Technical Data

Entity Type

Release State

Technical Name

## Namespace

Application Component

Category

Direction

## Mode

## Idempotency

Service Operation

## Released

ForwardingAgreementRequest_Out

http://sap.com/xi/TMS/Global

TM-FWA

B2B

Outbound

Asynchronous

No

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

203


## Entity Type

Service Operation

P2P Communication Enabled

## Yes

## Business Context and Use

A shipper or logistics service provider (LSP) uses a transportation management system to carry out
transportation planning for the next fiscal year. As part of the planning, the shipper or LSP wants to start a
bidding process to create freight agreements with carriers. The shipper or LSP creates a freight agreement
RFQ master that contains agreement-relevant information such as:

● Commodities to be shipped

● Capacities

● Trade lanes

● Service levels

● Transportation modes

The shipper or LSP sends the freight agreement RFQs to carriers and the carriers respond to the freight
agreement RFQ with their quotes. The shipper or LSP can consolidate these quotes and decide which carriers
should be used for the transportation process.

After the shipper or LSP has decided to use the services of a particular carrier, the carrier can create and
release a forwarding agreement. The carrier can use the service operation ForwardingAgreementRequest_Out
to create a freight agreement in the shipper's or LSP's system.

## Features

The ForwardingAgreementRequest_Out outbound operation sends the following data to a carrier:

● Contract period

● List of items that represent the goods to be transported

● Information about the goods:

○ Items such as containers, packages, or products

○ Measurements such as gross volume, gross weight, net weight, and quantity

● Means of transport and locations

● Transportation terms such as the service levels and the transportation modes

## Message Types

● TransportationAgreementRequest

204

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


Notes on SAP Implementation

## Integration

If a shipper also uses SAP Transportation Management (SAP TM), the operation exchanges data with the
operation FreightAgreementRequest_In. Otherwise, the operation can exchange data with an equivalent
third-party application used by the shipper. For more information, see Maintain Freight Agreement [page 178].

2.5  Customer Freight Invoice Request Processing

## Definition

The requesting of invoicing for transportation services performed for a customer (for example, a shipper).

Technical Data

Entity Type

## Technical Name

Business Context and Use

## Process Component

## CustomerFreightInvoiceRequestProcessing

The Customer Freight Invoice Request Processing  process component enables a carrier to trigger customer
invoice processing for transportation services performed for a customer, for example, a shipper. It also enables
credit commitment information to be transferred to a connected credit management application during
forwarding settlement.

Notes on SAP Implementation

## Integration

This process component enables transportation invoicing data to be transferred between the Forwarding
Settlement (TM-FWS) component in SAP Transportation Management (SAP TM) and the Sales Billing (SD-BIL)
component in SAP ERP. In addition, it enables credit commitment information to be transferred between SAP
TM and SAP Credit Management.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

205


Note the following:

● A forwarding settlement document or a credit memo in the SAP TM back-end system corresponds to

an instance of a Customer Freight Invoice Request [page 206]  business object.

● A forwarding settlement document or a credit memo is created based on a forwarding order, which

corresponds to an instance of a Transportation Request [page 123] business object.

● An SD billing document in the SAP ERP back-end system corresponds to an instance of a Customer Invoice

 business object.

More Information

## Forwarding Settlement

2.5.1  Customer Freight Invoice Request

## Definition

A request sent to billing to create one or more customer invoices.

Technical Data

Entity Type

Technical Name

## Object Category

Business Context and Use

## Business Object

CustomerFreightInvoiceRequest

## Business Process Object

The Customer Freight Invoice Request business object enables a carrier to trigger customer invoicing for
transportation services performed for a customer, for example, a shipper. It enables the carrier to enter
the required data (for example, transportation charges) and send this data to a customer invoicing system,
which creates and processes the corresponding customer invoice.

206

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## Notes on SAP Implementation

For more information, see the documentation of the Customer Freight Invoice Request Processing [page 205]
process component.

2.5.1.1

Credit Usage Out

## Definition

An interface to send information about the credit commitments of business partners.

Technical Data

Entity Type

Category

## Direction

Service Interface

SAP A2A

## Outbound

## Business Context and Use

The Credit Usage Out  outbound service interface contains an operation that sends information about a
business partner’s credit commitments to a connected credit management application.

2.5.1.1.1

Notify of Credit Commitment

## Definition

To send a notification about the credit commitments of business partners.

Technical Data

## Entity Type

## Service Operation

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

207


Release State

Technical Name

Namespace

Category

Direction

## Mode

## Idempotency

P2P Communication Enabled

Business Context and Use

Released with Restrictions

CreditCommitmentNotification_Out

http://sap.com/xi/TMS/Global

SAP A2A

Outbound

Asynchronous

No

## Yes

Before you approve a new or changed forwarding order, you perform a credit limit check for the relevant
business partner (that is, the payer) by using a connected credit management application. During forwarding
settlement for an approved forwarding order, the Notify of Credit Commitment  outbound operation sends
updated information about the business partner’s credit commitments to the credit management application.
This allows the credit management application to update the credit exposure information for the business
partner.

## Features

The  Notify of Credit Commitment  outbound operation sends credit commitment data to the credit
management application, including the following:

● Business partner ID (that is, payer ID)

● Amount committed (for example, total amount of the forwarding settlement document)

● Forwarding order number

● Internal ID of the credit segment

● Validity date of the commitment

## Message Types

● CreditCommitmentNotification

208

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## Prerequisites

● The Check Transportation Request Ordering Party Creditworthiness [page 125]  outbound operation in the
Transportation Request Processing [page 122] process component has requested information about a
business partner from a connected credit management application.

● The Notify of Credit Commitment [page 127] outbound operation in the Transportation Request Processing
[page 122] process component has informed the credit management application about the credit limit
amount approved for a business partner in a specific order.

## Notes on SAP Implementation

In SAP Transportation Management (SAP TM), you use this operation to send updated credit information for a
business partner to SAP Credit Management during forwarding settlement. The operation sends credit
commitment data to SAP Credit Management when you create, change, or cancel a forwarding settlement
document and transfer it to SAP ERP, and SAP ERP subsequently confirms the creation, change, or
cancellation of the corresponding invoice. SAP Credit Management can then update the credit limit amount for
the business partner accordingly. For example, when SAP Credit Management receives information about
credit commitments derived from a new forwarding settlement document, it does the following:

● Reduces the exposure value of the open order for the forwarding order by the amount of the forwarding

settlement document

● Moves the new amount from the Open Orders exposure category to the Billing Document Value exposure

category

SAP TM triggers the operation only in the following cases:

● The forwarding settlement document is related to a forwarding order with a successful credit limit check

status.

● SAP ERP has sent a confirmation of invoice creation, change, or cancellation.

Note the following:

● A forwarding settlement document in the SAP TM back-end system corresponds to an instance of a

Customer Freight Invoice Request [page 206] business object.

● A forwarding order in the SAP TM back-end system corresponds to an instance of a Transportation

Request [page 123] business object.

## Configuration

You have made the required settings for credit limit checks. For more information, see the Configuration section
in the documentation of the Check Transportation Request Ordering Party Creditworthiness [page 125]
outbound operation.

## Enhancements

The BAdI for CreditCommitmentNotification_Out Business Add-In (BAdI) is available for this operation.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

209


## More Information

For more information about credit limit checks in SAP TM, see Forwarding Order Management.

2.5.1.2  Customer Freight Invoicing Out

## Definition

An interface to request the creation, change, or cancellation of customer invoices or credit memos.

Technical Data

Entity Type

Category

## Direction

Business Context and Use

Service Interface

SAP A2A

## Outbound

The Customer Freight Invoicing Out outbound service interface groups operations that send data to a customer
invoicing system to carry out invoicing or process credit memos for transportation services performed for a
customer, for example, a shipper.

## Notes on SAP Implementation

For more information, see the documentation of the Customer Freight Invoice Request Processing [page 205]
process component.

2.5.1.2.1

Simulate Customer Freight Invoice Request

## Definition

To request the data required to simulate a forwarding settlement document or credit memo with a category of
Forwarding Settlement Document or Credit Memo.

210

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


Technical Data

Entity Type

Release State

Technical Name

## Namespace

Application Component

Category

Direction

## Mode

## Idempotency

P2P Communication Enabled

## Service Operation

## Released with Restrictions

CustomerFreightInvoiceRequestSUITESimulate_Ou

t

http://sap.com/xi/TMS/Global

TM–FWS

A2A

Outbound

Synchronous

Not Applicable

## Yes

## Business Context and Use

A carrier performs transportation services for a customer such as a shipper and creates a forwarding
settlement document or credit memo. The carrier wants to preview the corresponding customer invoice or
credit memo before actually requesting the creation of the invoice or credit memo.

The Simulate Customer Freight Invoice Request outbound operation sends a new or changed forwarding
settlement document or credit memo to the customer invoicing system and requests the transfer of data to
preview the customer invoice or credit memo.

## Related Operations

The Maintain Customer Invoice based on Customer Freight Invoice Request Request_V1 inbound operation in
the Customer Invoice Processing process component returns data to simulate a customer invoice based on a
request sent by the Simulate Customer Freight Invoice Request outbound operation.

## Features

The Simulate Customer Freight Invoice Request outbound operation sends forwarding settlement document
data to the customer invoicing system. The customer invoicing system returns invoice data such as tax
information as a PDF stream, which the requesting system uses to generate a preview of the customer invoice.

You can change the tax parameters and other invoice-related data in the customer invoicing system by
transferring additional request data, which may be required to simulate the customer invoice for the forwarding

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

211


settlement document or credit memo. This data can include air waybill numbers, sources and destinations,
freight booking numbers, charges incurred during each stage, and any transactional data relating to freight
execution.

## Prerequisites

The Simulate Customer Freight Invoice Request outbound operation can only be used if a customer invoice has
not yet been created in the customer invoicing system. For more information, see the Request Customer
Freight Invoice Request_V1 [page 212] service operation.

## Notes on SAP Implementation

A forwarding settlement document or a credit memo in the SAP Transportation Management (SAP TM) back-
end system corresponds to an instance of a Customer Freight Invoice Request [page 206] business object.

## Enhancements

The Business Add-In (BAdI) BAdI for CustomerFreightInvoiceRequestSUITESimulate_Out (/SCMTMS/
CFI_SE_SIMRQ) is available for this operation.

2.5.1.2.2  Request Customer Freight Invoice Request_V1

## Definition

To request the creation or change of a customer invoice based on a forwarding settlement document with a
category of Forwarding Settlement Document or Credit Memo.

Technical Data

Entity Type

Release State

Technical Name

## Namespace

## Service Operation

## Released with Restrictions

CustomerFreightInvoiceRequestSUITERequest_Out_V1

http://sap.com/xi/TMS/Global

Application Component

TM-FWS

212

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


Category

Direction

## Mode

Idempotency

SAP A2A

Outbound

Asynchronous

## Not Applicable

P2P Communication Enabled

## Yes

## Business Context and Use

A carrier performs transportation services for a customer, for example, a shipper. To carry out forwarding
settlement for the transportation services, the carrier creates a forwarding settlement document, which
contains details of the transportation services and the calculated transportation charges. The carrier sends the
forwarding settlement document to a customer invoicing system. The Request Customer Freight Invoice
Request_V1 outbound operation sends a new or changed forwarding settlement document to a customer
invoicing system and requests the creation or change of the corresponding customer invoice. Note that this
operation can also request the creation or change of a credit memo.

## Related Operations

● The Maintain Customer Invoice based on Customer Freight Invoice Request Request_V1 inbound operation
in the Customer Invoice Processing process component can create a customer invoice based on a request
sent by the Request Customer Freight Invoice Request_V1 outbound operation.

● The Change Invoice Request based on Customer Freight Invoice Request Confirmation_V1 [page 217]
inbound operation receives a confirmation of the creation, change, or cancellation of the requested
customer invoice.

● The Request Customer Freight Invoice Request Cancellation_V1 [page 214]  requests the cancellation of a

customer invoice based on a canceled forwarding settlement document or credit memo.

## Features

The Request Customer Freight Invoice Request_V1 outbound operation sends data such as the following to
customer invoice processing:

● Forwarding settlement document or credit memo ID

● Information about the transportation services and the corresponding charges

● Ship-from location

## Versioning

The Request Customer Freight Invoice Request_V1 outbound operation is the successor of the Request
Customer Freight Invoice Request outbound operation in SAP Transportation Management 7.0 (SAP TM 7.0).
The new operation only contains those elements that are required to carry out customer invoice processing.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

213


## Message Types

● Customer Freight Invoice Request SUITE Request_V1

## Notes on SAP Implementation

A forwarding settlement document or credit memo in the SAP Transportation Management (SAP TM) back-
end system corresponds to an instance of a Customer Freight Invoice Request [page 206] business object.

For more information about requesting invoicing for transportation services performed for a customer, see the
documentation of the Customer Freight Invoice Request Processing [page 205] process component.

## Enhancements

The BAdI for CustomerFreightInvoiceRequestSUITERequest_Out_V1 (/SCMTMS/CFI_SE_CRTRQ) Business Add-
In (BAdI) is available for this operation.

2.5.1.2.3  Request Customer Freight Invoice Request

Cancellation_V1

## Definition

To request the cancellation of a customer invoice.

Technical Data

Entity Type

Release State

Technical Name

## Service Operation

## Released with Restrictions

CustomerFreightInvoiceRequestSUITECancellationRe­

quest_Out_V1

## Namespace

http://sap.com/xi/TMS/Global

Application Component

Category

Direction

Mode

214

P U B L I C

TM-FWS

SAP A2A

Outbound

## Asynchronous

Enterprise Services and ESR Content
Enterprise Services


Idempotency

## Not applicable

P2P Communication Enabled

## Yes

## Business Context and Use

A carrier cancels a forwarding settlement document that has already been sent to a customer invoicing
system. The Request Customer Freight Invoice Request Cancellation_V1  outbound operation sends information
about the canceled forwarding settlement document to the customer invoicing system and requests the
cancellation of the corresponding customer invoice.

Note that this operation can also request the cancellation of a credit memo.

## Related Operations

The Cancel Invoice based on Customer Freight Invoice Request Cancel Request_V1 inbound operation in the
Customer Invoice Processing process component cancels a customer invoice based on a cancellation
request sent by the Request Customer Freight Invoice Request Cancellation_V1  outbound operation.

## Features

The Request Customer Freight Invoice Request Cancellation_V1 outbound operation sends the ID of the
canceled forwarding settlement document or credit memo to customer invoice processing.

## Versioning

The Request Customer Freight Invoice Request Cancellation_V1 outbound operation is the successor of the
Request Customer Freight Invoice Request Cancellation outbound operation.

## Message Types

● Customer Freight Invoice Request SUITE Cancellation Request_V1

## Prerequisites

The Request Customer Freight Invoice Request_V1 [page 212] outbound operation has sent a new or changed
forwarding settlement document or credit memo to customer invoice processing.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

215


## Notes on SAP Implementation

A forwarding settlement document or credit memo in the SAP Transportation Management (SAP TM) back-
end system corresponds to an instance of a Customer Freight Invoice Request [page 206] business object.

For more information about requesting invoicing for transportation services performed for a customer, see the
documentation of the Customer Freight Invoice Request Processing [page 205] process component.

## Enhancements

The BAdI for CustFreightInvoiceReqSUITECancellationReq_Out_V1 (/SCMTMS/CFI_SE_CNCLNRQ) Business
Add-In (BAdI) is available for this operation.

2.5.1.3  Customer Freight Invoicing In

## Definition

An interface to receive customer invoice confirmations.

Technical Data

Entity Type

Category

## Direction

Business Context and Use

Service Interface

SAP A2A

## Inbound

The Customer Freight Invoicing In  inbound service interface contains an operation that receives a confirmation
of the creation, change, or cancellation of a customer invoice based on a new, changed, or canceled forwarding
settlement document or credit memo. The customer invoice is used to carry out customer invoicing for
transportation services performed for a customer, for example, a shipper.

## Notes on SAP Implementation

For more information, see the documentation of the Customer Freight Invoice Request Processing [page 205]
 process component.

216

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


2.5.1.3.1

Change Invoice Request Based on Customer
Freight Invoice Request Confirmation_V1

## Definition

To change a forwarding settlement document with the category Forwarding Settlement Document or Credit
Memo based on the confirmation of a request to create or change a customer invoice.

Technical Data

Entity Type

Release State

Technical Name

## Namespace

## Service Operation

## Released with Restrictions

CustomerFreightInvoiceRequestSUITEConfirmation_In_V1

http://sap.com/xi/TMS/Global

Application Component

## TM-FWS

Web Service Definition (Back End)

/SCMTMS/CFIRSUITE_CONF

Category

Direction

## Mode

## Idempotency

Change/Update Behavior

P2P Communication Enabled

Business Context and Use

SAP A2A

## Inbound

Asynchronous

Not Applicable

Type2

## Yes

To carry out customer invoicing for transportation services performed for an ordering party, a carrier sends a
forwarding settlement document to customer invoicing. The Change Invoice Request based on Customer
Freight Invoice Request Confirmation_V1 inbound operation receives a confirmation of the creation, change, or
cancellation of the corresponding customer invoice.

Note that this operation can also receive a confirmation of the creation, change, or cancellation of a credit
memo.

## Related Operations

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

217


The  Confirm Customer Freight Invoice Request_V1 outbound operation in the Customer Invoice Processing
process component sends a confirmation of the creation, change, or cancellation of a customer invoice.

## Features

The Change Invoice Request based on Customer Freight Invoice Request Confirmation_V1 inbound operation
receives an acceptance code that specifies whether a customer invoice has been created, changed, or
canceled for a forwarding settlement document or a credit memo. In the case of a confirmation of a created
customer invoice, the operation updates the forwarding settlement document as follows:

● If invoice creation was successful, the operation receives the ID of the customer invoice. It adds this ID to
the relevant forwarding settlement document and updates the invoicing status to Invoicing Confirmed.

● If invoice creation failed, it updates the status of the forwarding settlement document to Invoicing Failed.

## Versioning

The Change Invoice Request based on Customer Freight Invoice Request Confirmation_V1 inbound operation
is the successor of the Change Invoice Request based on Customer Freight Invoice Request
Confirmation inbound operation in SAP Transportation Management 7.0 (SAP TM 7.0).

## Message Types

● Customer Freight Invoice Request SUITE Confirmation_V1

## Prerequisites

The Request Customer Freight Invoice Request_V1 [page 212]  outbound operation has sent a new or changed
forwarding settlement document or credit memo to customer invoicing and requested the creation or change
of the corresponding customer invoice; or the Request Customer Freight Invoice Request Cancellation_V1
[page 214]  outbound operation has sent a canceled forwarding settlement document or credit memo to
customer invoicing and requested the cancellation of the corresponding customer invoice.

## Notes on SAP Implementation

A forwarding settlement document or credit memo in the SAP Transportation Management (SAP TM) back-
end system corresponds to an instance of a Customer Freight Invoice Request [page 206] business object.

For more information about requesting invoicing for transportation services performed for a customer, see the
documentation of the Customer Freight Invoice Request Processing [page 205] process component.

## Enhancements

The BAdI for CustFreightInvoiceRequestSUITEConfirmation_In_V1 (/SCMTMS/CFI_SE_CNFRQ) Business Add-In
(BAdI) is available for this operation.

218

## P U B L I C

Enterprise Services and ESR Content
## Enterprise Services


2.6  Supplier Freight Invoice Request Processing

## Definition

The requesting of invoice verification for invoices submitted by a supplier (for example, a carrier) for
transportation services ordered from that supplier.

Technical Data

Entity Type

Technical Name

## Process Component

SupplierFreightInvoiceRequestProcessing

## Notes on SAP Implementation

This process component can exchange data with the Supplier Invoice Processing process component. This
enables you to exchange data between the Invoice Verification (MM-IV) component in SAP ERP and the Freight
Settlement (TM-FRS) component in SAP Transportation Management (SAP TM). Note the following:

● A freight settlement document in the SAP TM back-end system corresponds to an instance of a Supplier

Freight Invoice Request [page 220] business object.

● A freight settlement document is created based on a freight order or freight booking, which corresponds to

an instance of a Transportation Order [page 6] business object.

● A freight invoice in the SAP ERP back-end system corresponds to an instance of a Supplier Invoice

business object.

## Business Context and Use

The  Supplier Freight Invoice Request Processing  process component receives information about invoices that
have been verified and posted in supplier invoice processing; for example, invoices submitted by a carrier for
transportation services performed for a shipper.

More Information

## Freight Settlement

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

219


2.6.1  Supplier Freight Invoice Request

## Definition

A request sent to invoice verification advising that a freight invoice for specified quantities and prices is
expected or is to be created through evaluated receipt settlement.

Technical Data

Entity Type

Technical Name

Object Category

## Business Object

SupplierFreightInvoiceRequest

Business Process Object

## Notes on SAP Implementation

For more information, see Supplier Freight Invoice Request Processing [page 219].

## Business Context and Use

The Supplier Freight Invoice Request business object enables a shipper to perform invoice verification for
transportation services subcontracted to a carrier, for example. It enables the shipper to enter the required
data (for example, the expected transportation charges) and send this data to purchase order processing,
which creates the documents required for invoice verification. The invoice sent by the carrier can later be
verified and posted in supplier invoice processing.

2.6.1.1

Supplier Freight Invoicing In

## Definition

An interface to receive supplier invoice confirmations.

220

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


Technical Data

Entity Type

Category

## Direction

Service Interface

SAP A2A

## Inbound

## Business Context and Use

The Supplier Freight Invoicing In inbound interface contains an operation that receives a notification about a
verified and posted invoice that relates to a specific freight settlement document.

## Notes on SAP Implementation

For more information, see Supplier Freight Invoice Request Processing [page 219].

2.6.1.1.1

Change Invoice Request Based on Invoice
Notification

## Definition

To change a freight settlement document with the category Freight Settlement Document based on an invoice
notification.

Technical Data

Entity Type

Release State

Technical Name

## Namespace

## Service Operation

Released with Restrictions

InvoiceNotification_In

http://sap.com/xi/TMS/Global

Application Component

## TM-FRS-IV

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

221


Web Service Definition (Back End)

/SCMTMS/INVOICENOTIFICATION_IN

Category

Direction

## Mode

Idempotency

SAP A2A

## Inbound

Asynchronous

## Not Applicable

P2P Communication Enabled

## Yes

## Business Context and Use

A shipper carries out invoice verification in supplier invoice processing for transportation services
subcontracted to a carrier, for example. When an invoice is received from the carrier, an invoicing clerk verifies
and posts the invoice. The Change Invoice Request Based on Invoice Notification  inbound operation receives a
notification about the posted invoice and updates the corresponding freight settlement document.

## Features

The Change Invoice Request Based on Invoice Notification  inbound operation receives data such as the
following:

● ID of the freight settlement document for which the invoice was posted

● Posted amounts

The operation updates the posted amounts in the relevant freight settlement document.

## Error Handling

The Change Invoice Request Based on Invoice Notification inbound operation supports Forward Error Handling
 (FEH). The following error categories are used:

● PRE: Processing Error

● DCE: Determination and Conversion Error

For more information about the individual error categories, see the code list for the global data type
LogItemCategoryCode .

222

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## Message Types

● InvoiceNotification

## Notes on SAP Implementation

For more information, see Supplier Freight Invoice Request Processing [page 219].

A freight settlement document in SAP Transportation Management (SAP TM) corresponds to an instance of a
Supplier Freight Invoice Request [page 220] business object.

2.7  Supplier Invoice - Create (B2B)

## Technical Name: InvoiceRequest_In

With this asynchronous inbound service, your system can electronically receive invoices from your
transportation service providers in SAP Transportation Management (SAP TM). Your transportation service
provider creates an invoice document in an external system. The external system sends a message through
this enterprise service and creates a carrier invoice document in the SAP TM system of the transportation
service buyer.

Namespace: http://sap.com/xi/TMS/Global

Service Request

## Service Message Header

The service message header contains information on the message header data, for example, the involved
sender and receiver, as well as the date and time. The following nodes and fields are the most important ones:

Node or Field

ID

CreationDateTime

SenderBusinessSystemID

## Description

## ID of the SOAP message

Date and time at which the message

was created

ID of the external system that sends the

message

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

223


Node or Field

SenderParty

InternalID

## Description

ID of the business partner that sends

the message to your SAP TM system.

The ID must be identical to the ID of the

business partner in your SAP TM sys­

tem.

## Service Nodes

The service nodes contain the business data of the service.

## Node

Invoice

## Item

Description

## Link to details

Header information for the invoice

InvoiceRequest_In - Invoice [page 224]

Item information for the invoice

InvoiceRequest_In - Item [page 227]

See also:Examples of B2B Messages for a Carrier Invoice [page 231]

2.7.1  InvoiceRequest_In - Invoice

## Use

Node that contains the invoice header data of the invoice document.

## Nodes and Fields

The following table provides an overview of the fields.

 Note

In the following table, field attributes are marked in blue.

Node or Field

SupplierInvoiceID

Description

## Cardinality

Supplier Invoice ID

1..1

Identifies the invoice in

the supplier’s system.

224

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


Node or Field

Description

## Cardinality

CancelledSupplierInvoiceID

SupplierInvoiceTypeCode

ID of Canceled Supplier

0..1

## Invoice

Identifies the invoice

(in the supplier’s sys­

tem) that is canceled

by the credit memo.

You must send this

field if the document

represents a credit

memo. In this case, the

field must contain the

ID of the invoice in the

supplier’s system.

Supplier Invoice Type

1..1

## Code

Indicates the type of

the document:

● Invoice: Type code

= 004

● Credit Memo: Type

code = 005

DocumentDate

Document Date

1..1

Specifies the date on

which the supplier in­

voice was issued.

GrossAmount

CurrencyCode

Gross Amount

1..1

## Currency Code

Specifies the gross in­

voice amount in the

document currency.

## Party

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

225


Node or Field

Description

Cardinality

PartyType

Party Type

1..1

You can use the follow­

ing values:

● BillFrom (Manda­

tory if

BuyerPartyID is

set.)

● BillTo (Mandatory

if

SupplierPartyI

D is set.)

GlobalLocationNumber

[Not in use]

BuyerPartyID

Buyer Party ID

0..1

When the attribute

Either the

PartyType = BillFrom

BuyerPartyID, or

(Supplier), then the

the

BuyerPartyID is the

SupplierPartyID

number that the buyer

must be available.

uses for the supplier.

SupplierPartyID

Supplier Party ID

When the attribute

PartyType = BillTo

(Buyer), then the

SupplierPartyID is

the number that the

supplier uses for the

buyer.

DueCalculationBaseDate

Due Calculation Base

0..1

## Date

CashDiscount1Percent

Cash Discount

0..1

Percentage 1

CashDiscount1Days

Days for Cash Discount

0..1

1

CashDiscount2Percent

Cash Discount

0..1

Percentage 2

PaymentTerms

0..1

226

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


Node or Field

Description

## Cardinality

CashDiscount2Days

Days for Cash Discount

0..1

2

NetPaymentDays

Net Payment Days

0..1

Defines the standard

settlement period (in

days).

HeaderTax

Header Tax

1..unbounded

## Amount

Tax Amount

1..1

SupplierTaxTypeCode

Specifies the tax

amount in document

currency.

Supplier Tax Type Code

1..1

The supplier tax type

code, for example, V1.

TaxPercentage

Tax Rate

1..1

In SAP Transportation

Management (SAP

TM), the tax rate and

tax type are used to as­

sign tax codes in the

buyer's system. You

must use the Custom­

izing activity Assign

Carrier Tax Types to

SAP TM Tax Charge

Type under

Transportation

Management

## Integration

Enterprise Services

Carrier Invoice

Integration .

[Not in use]

P U B L I C

227

## DocumentHeaderText

2.7.2  InvoiceRequest_In - Item

## Use

Enterprise Services and ESR Content
## Enterprise Services


Node that contains the item-level data of the invoice document.

Nodes and Fields

Node or Field

Description

## Cardinality

SupplierInvoiceItemID

Supplier Invoice Item ID

1..1

Identifies the item number

that the supplier uses to

identify the invoice item in

the supplier’s system.

SupplierInvoiceItemTypeCode

Supplier Invoice Item Type

1..1

## Code

Indicates the type of the in­

voice item:

● Invoice item: Type code

= 00

● Credit memo: Type code

= 00

NetAmount

Net Amount

0..1

Specifies the net amount in

the document currency.

InvoicedQuantity

Invoiced Quantity

0..1

Not in use.

PurchaseOrderID

Purchase Order ID

0..1

Not in use.

PurchaseOrderItemID

Purchase Order Item ID

0..1

Not in use

DeliveryNote

Delivery Note

0..1

Not in use

()

228

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


Node or Field

PricingElement

Description

Cardinality

Pricing Element

0..n

Mandatory to process a car­

rier invoice in SAP Transpor­

tation Management (SAP

TM).

SupplierConditionType

Supplier Condition Type

0..1

For invoices to be processed

in SAP TM, this is the condi­

tion type agreed with your

carrier. It is mapped to the

SAP TM charge type using

the Customizing activity

Assign Carrier Condition type

to SAP. TM Charge Type un­

der

Transportation

Management

## Integration

## Enterprise Services

Carrier Invoice Integration .

It contains the condition type

agreed with your carrier to

represent the SAP TM charge

type.

Mandatory.

ConditionRateValue

Condition Rate Value

0..1

Contains the rate and the

rate currency agreed with the

carrier.

ConditionQuantity

Condition Quantity

0..1

Contains the price unit on

which the rate is dependent.

ConditionAmount

Condition Amount

0..1

Contains the invoice amount

and document currency for

the component invoiced by

the carrier.

Mandatory.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

229


Node or Field

Description

## Cardinality

ConditionBaseValue

Condition Base Value

0..1

Product

Not in use

## ItemTax

Contains the quantity from

the SAP TM freight order,

freight booking, or service or­

der, on which the price is ap­

plied.

Item Tax

Not in use

1..1

DocumentItemText

Document Item Text

0..unbounded

## Not in use

TransportationOrderReference

Transportation Order

0..1

## Reference

TransportationOrderID

Transportation Order ID

0..1

Contains the freight order,

freight booking, or service or­

der number in the shipper’s

system.

Mandatory.

TransportationOrderIte

Transportation Order Item ID

0..1

mID

Contains the item ID of the

freight order item in the ship­

per’s system if the invoice

item is for a freight order

item.

Only required when the cal­

culation level in SAP TM for

the carrier is Item Level.

230

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


Node or Field

Description

## Cardinality

TransportationStageID

Transportation Stage ID

0..n

Contains the stage ID of the

freight order stage in the

shipper’s system if the in­

voice item is for a freight or­

der stage.

Only required when the cal­

culation level in SAP TM for

the carrier is Stage Level.

2.7.3  Examples of B2B Messages for a Carrier Invoice

You can specify the information that you need to include in your carrier invoice. This is useful when you send
information in B2B message format. This enables you to specify the following information:

● Relationship between the invoice item in the message and the calculation level and charge items

● Transportation order reference fields at an item level

● Pricing conditions

You have a freight order ID of 9540 for carrier CAR001 that contains 2 pallets, as follows:

Item Detail

Item ID

100010

100020

Stage Detail

Details

Pallet 1

Pallet 2

Total Weight

## Volume

Gross Weight (KG)

(M3)

100

200

300

1

1

## Stage

Internal Stage ID

## Source

Destination

Distance (KM)

1

2

00000010

00000020

A

B

B

C

50

80

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

231


If you specify a charge calculation base of Header Level, the freight order contains the following charges:

Header Charges

Charge Type (De­

Rate and Cur­

Calculation Quan­

Invoice Amount

scription)

rency

Price and Unit

tity

(USD)

Invoice Currency

BASE_CHARGE

50 USD

None

## None

(Base Freight)

HANDLING_CHG

20 USD

100 KG

300

(Handling Charge)

Total

USD

USD

50

60

110

You must map the B2B message for the carrier invoice as follows:

Nodes and Fields

Node or Field

SupplierInvoiceID

Value

INV1234

SupplierInvoiceTypeCode

004

DocumentDate

GrossAmount

Party

## Party

PartyType

BuyerPartyID

2018-09-21

USD 110

## Value

BillFrom

CAR001

## Explanation

The ID of the service provider in the

service provider’s system

## Invoice

Invoice date

Gross amount

## Explanation

Service provider ID

SupplierPartyID

Leave this field empty

Leave this field empty

Payment Terms

Term

## Value

## Explanation

DueCalculationBaseDate

2018-09-21

Baseline date for terms of payment

CashDiscount1Percent

CashDiscount1Days

NetPaymentDays

3

10

15

3% cash discount

If paid within 10 days

Due date for payments

232

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


Header Tax

## Tax

SupplierTaxTypeCode

## Amount

TaxPercentage

Items

## Item

SupplierInvoiceItemID

Value

VAT

0

0

Value

1

SupplierInvoiceItemTypeCode

002

Explanation

USD

## Explanation

Automatically created number, begin­

ning at 1

Invoice

NetAmount

USD 110

Item amount

InvoiceQuantity

Leave this field empty

PurchaseOrderID

Leave this field empty

PurchaseOrderItemID

Leave this field empty

## DeliveryNote

Leave this field empty

Pricing for Base Freight

PricingElement

SupplierConditionType

Value

FB00

ConditionRateValue

USD 50

ConditionQuantity

Leave this field empty

ConditionAmount

USD 50

ConditionBaseValue

Leave this field empty

Pricing for Handling Charge

PricingElement

SupplierConditionType

ConditionRateValue

ConditionQuantity

ConditionAmount

Value

HNDL

USD 20

100 KG

USD 60

Explanation

Base freight

Explanation

## Handling charge

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

233


PricingElement

ConditionBaseValue

Product

## Item Tax

SupplierTaxTypeCode

## TaxPercentage

Transportation Order

Value

300 KG

Value

VAT

## Zero

Explanation

## Explanation

TransportationOrderReference

## Value

## Explanation

TransportationOrderID

9540

Shipper’s freight order ID

TransportationOrderItemID

Leave this field empty

Transpiration Stage ID

## Leave this field empty

If you specify a charge calculation base of Stage Level, the freight order contains the following charges:

Header Charges

Charge Type (De­

Rate and Cur­

Calculation Quan­

scription)

rency

Price and Unit

tity

Invoice Amount

Invoice Currency

DOC_HANDLING

30 USD

None

None

30

USD

(Documentation

Charge)

Stage A to B Charges

Charge Type (De­

Rate and Cur­

Calculation Quan­

scription)

rency

Price and Unit

tity

Invoice Amount

Invoice Currency

BASE_CHARGE

1 USD

1 KM

50

(Base freight)

STOP_OFF

10 USD

None

None

50

10

USD

USD

(Stop charge)

Stage B to C Charges

Charge Type (De­

Rate and Cur­

Calculation Quan­

scription)

rency

Price and Unit

tity

Invoice Amount

Invoice Currency

BASE_CHARGE

1 USD

1 KM

80

80

USD

(Base freight)

234

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


Charge Type (De­

Rate and Cur­

Calculation Quan­

scription)

rency

Price and Unit

tity

Invoice Amount

Invoice Currency

UNLOADING

25 USD

None

None

25

USD

(Unloading

charge)

The invoice total is USD 195.

You must map the B2B message for the carrier invoice as follows:

Nodes and Fields

Node or Field

SupplierInvoiceID

SupplierInvoiceTypeCode

DocumentDate

GrossAmount

Party

## Party

PartyType

BuyerPartyID

Value

INV1234

004

2018-09-21

USD 195

## Value

BillFrom

CAR001

## Explanation

The ID of the service provider in the

service provider’s system

## Invoice

Invoice date

Gross amount

## Explanation

Service provider ID

SupplierPartyID

Leave this field empty

Payment Terms

Term

## Value

## Explanation

DueCalculationBaseDate

2018-09-21

Baseline date for terms of payment

CashDsicount1Percent

CashDiscount1Days

NetPaymentDays

Header Tax

## Tax

SupplierTaxTypeCode

Amount

3

10

15

Value

VAT

## Zero

3% cash discount

If paid within 10 days

Due date for payments

Explanation

USD

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

235


## Tax

TaxPercentage

Items

## Item

SupplierInvoiceItemID

Value

Zero

Value

1

SupplierInvoiceItemTypeCode

002

Explanation

## Explanation

Automatically created number, begin­

ning at 1

Invoice

NetAmount

USD 30

Item amount

InvoiceQuantity

Leave this field empty

PurchaseOrderID

Leave this field empty

PurchaseOrderItemID

Leave this field empty

## DeliveryNote

Leave this field empty

Pricing for Document Charges

PricingElement

SupplierConditionType

ConditionRateValue

Value

DOCC

USD 30

ConditionQuantity

Leave this field empty

ConditionAmount

USD 30

ConditionBaseValue

Leave this field empty

Product

## Item Tax

SupplierTaxTypeCode

## TaxPercentage

Transportation Order

Value

VAT

## Zero

## Explanation

Documentation charges

## Explanation

TransportationOrderReference

## Value

## Explanation

TransportationOrderID

9540

Shipper’s freight order ID

TransportationOrderItemID

Leave this field empty

236

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


TransportationOrderReference

## Value

## Explanation

Transportation Stage ID

Leave this field empty

Items

## Item

SupplierInvoiceItemID

Value

2

SupplierInvoiceItemTypeCode

002

## Explanation

Automatically created number, begin­

ning at 2

Invoice

NetAmount

USD 60

Item amount

InvoiceQuantity

Leave this field empty

PurchaseOrderID

Leave this field empty

PurchaseOrderItemID

Leave this field empty

## DeliveryNote

Leave this field empty

Pricing for Base Freight

PricingElement

SupplierConditionType

ConditionRateValue

ConditionQuantity

ConditionAmount

ConditionBaseValue

Pricing for Stop Charge

PricingElement

SupplierConditionType

ConditionRateValue

Value

FB00

USD 1

1 KM

USD 50

50 KM

Value

STOP

USD 10

ConditionQuantity

Leave this field empty

ConditionAmount

USD 10

ConditionBaseValue

Leave this field empty

Explanation

Base freight

Explanation

## Base freight

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

237


Item Tax

## Tax

SupplierTaxTypeCode

## TaxPercentage

Transportation Order

Value

VAT

## Zero

## Explanation

TransportationOrderReference

## Value

## Explanation

TransportationOrderID

9540

Shipper’s freight order ID

TransportationOrderItemID

Leave this field empty

Transportation Stage ID

00000010

Internal stage ID for stage A to B

Items

## Item

SupplierInvoiceItemID

Value

3

SupplierInvoiceItemTypeCode

002

## Explanation

Automatically created number, begin­

ning at 3

Invoice

NetAmount

USD 105

Item amount

InvoiceQuantity

Leave this field empty

PurchaseOrderID

Leave this field empty

PurchaseOrderItemID

Leave this field empty

## DeliveryNote

Leave this field empty

Pricing for Base Freight

PricingElement

SupplierConditionType

ConditionRateValue

ConditionQuantity

ConditionAmount

ConditionBaseValue

Value

FB00

USD 1

1 KM

USD 60

80 KM

Explanation

Base freight

238

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


Pricing for Unloading Charge

PricingElement

SupplierConditionType

ConditionRateValue

Value

UNLD

USD 25

ConditionQuantity

Leave this field empty

ConditionAmount

USD 25

ConditionBaseValue

Leave this field empty

Item Tax

## Tax

SupplierTaxTypeCode

## TaxPercentage

Transportation Order

Value

VAT

## Zero

Explanation

Unloading charge

## Explanation

TrtansportationOrderReference

## Value

## Explanation

TransportationOrderID

9540

Shipper’s freight order ID

TransportationOrderItemID

Leave this field empty

Transportation Stage ID

00000020

## Internal stage ID for stage B to C

If you specify a charge calculation base of Item Level, the freight order contains the following charges:

Item 100010 – Pallet 1 Charges

Charge Type (De­

Rate and Cur­

Calculation Quan­

scription)

rency

Price and Unit

tity

Invoice Amount

Invoice Currency

BASE_CHARGE

1 USD

5 KG

100

(Base freight)

PACK

10 USD

None

None

30

10

USD

USD

(Packaging

charge)

Item 100020 – Pallet 2 Charges

Charge Type (De­

Rate and Cur­

Calculation Quan­

scription)

rency

Price and Unit

tity

Invoice Amount

Invoice Currency

BASE_CHARGE

1 USD

5 KG

200

40

USD

(Base freight)

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

239


Charge Type (De­

Rate and Cur­

Calculation Quan­

scription)

rency

Price and Unit

tity

Invoice Amount

Invoice Currency

PACKAGING

25 USD

None

None

25

USD

(Packaging

charge)

The invoice total is USD 95.

You must map the B2B message for the carrier invoice as follows:

Nodes and Fields

Node or Field

SupplierInvoiceID

Value

INV1234

## Explanation

The ID of the service provider in the

service provider’s system.

SupplierInvoiceTypeCode

004

DocumentDate

2018-09-21

## Invoice

Invoice date

GrossAmount

USD 95

Gross amount

Party

## Party

PartyType

BuyerPartyID

## Value

BillFrom

CAR001

SupplierPartyID

Leave this field empty

Payment Terms

## Term

DueCalculationBaseDate

CashDiscount1Percent

CashDiscount1Days

NetPaymentDays

Header Tax

## Tax

SupplierTaxTypeCode

Amount

## Value

2018-09-21

3

10

15

Value

VAT

## Zero

Explanation

Carrier ID

## Explanation

Baseline date for terms of payment

3% cash discount

If paid within 10 days

Due date for payments

Explanation

USD

240

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


## Tax

TaxPercentage

Items

## Item

SupplierInvoiceItemID

Value

Zero

Value

1

SupplierInvoiceItemTypeCode

002

Explanation

## Explanation

Automatically created number, begin­

ning at 1

Invoice

NetAmount

USD 30

Item amount

InvoiceQuantity

Leave this field empty

PurchaseOrderID

Leave this field empty

PurchaseOrderItemID

Leave this field empty

## DeliveryNote

Leave this field empty

Pricing for Base Freight

PricingElement

SupplierConditionType

ConditionRateValue

ConditionQuantity

ConditionAmount

ConditionBaseValue

Pricing for Packaging

PricingElement

SupplierConditionType

ConditionRateValue

Value

FB00

USD 1

5 KG

USD 20

100 KG

Value

PACK

USD 10

ConditionQuantity

Leave this field empty

ConditionAmount

Leave this field empty

ConditionBaseValue

Leave this field empty

## Product

Leave this field empty

Explanation

Base freight

Explanation

## Base freight

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

241


Item Tax

## Tax

SupplierTaxTypeCode

## TaxPercentage

Transportation Order

Value

VAT

## Zero

## Explanation

TransportationOrderReference

## Value

## Explanation

TransportationOrderID

9540

Shipper’s freight order ID

TransportationOrderItemID

100010

Internal item ID of the item in the ship­

Transportation Stage ID

Leave this field empty

Items

## Item

SupplierInvoiceItemID

Value

2

SupplierInvoiceItemTypeCode

002

per’s system

## Explanation

Automatically created number, begin­

ning at 2

Invoice

NetAmount

USD 65

Item amount

InvoiceQuantity

Leave this field empty

PurchaseOrderID

Leave this field empty

PurchaseOrderItemID

Leave this field empty

## DeliveryNote

Leave this field empty

Pricing for Base Freight

PricingElement

SupplierConditionType

ConditionRateValue

ConditionQuantity

ConditionAmount

ConditionBaseValue

Value

FB00

USD 1

5 KG

USD 40

200 KG

Explanation

Base freight

242

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


Pricing for Packaging

PricingElement

SupplierConditionType

Value

PAK1

ConditionRateValue

USD 25

ConditionQuantity

Leave this field empty

ConditionAmount

USD 25

ConditionBaseValue

Leave this field empty

Product

Item Tax

## Tax

SupplierTaxTypeCode

## TaxPercentage

Transportation Order

Leave this field empty

Value

VAT

## Zero

Explanation

Packaging charge

## Explanation

TransportationOrderReference

## Value

## Explanation

TransportationOrderID

9540

Shipper’s freight order ID

TransportationOrderItemID

100020

Internal item ID of the item in the ship­

per’s system

Transportation Stage ID

Leave this field empty

 Note

To use this interface to send a credit memo, the SupplierInvoiceTypeCode field has the value 005 and
the CancelledSupplierInvoiceID field contains the ID of the invoice in the carrier’s system that the
carrier previously sent.

For example, the carrier sends an invoice with a SupplierInvoiceID of INV1234. Next, the carrier wants
to send a credit memo to cancel the invoice. The field CancelledSupplierInvoiceID will contain the
invoice reference INV1234. The rest of the field content in the message will be that same as that mentioned
in the examples above.

## Example of the Customizing Information in Your System

The system uses the Assign Carrier Condition Types to SAP TM Charge Types Customizing activity under

Transportation Management

## Integration

Enterprise Services Carrier Invoice Integration  to map the

condition types in the interface to the SAP TM charge types.

Enterprise Services and ESR Content
Enterprise Services

P U B L I C

243


The following table contains the mapping information:

Condition Type

FB00

HNDL

DOCC

STOP

UNLD

## PACK

Charge Type

BASE_CHARGE

HANDLING_CHG

DOC_HANDLING

STOP_OFF

UNLOADING

## PACKAGING

The system uses the Assign Carrier Tax Types to SAP TM Tax Charge Types Customizing activity under

Transportation Management

## Integration

Enterprise Services Carrier Invoice Integration  to map the

tax rate and tax type to the SAP TM charge types. The following table contains the mapping information:

Carrier Tax Type

Tax Percentage

SAP TM Charge Type

VAT

VAT

0.000000

19.000000

VAT_0

VAT_19

244

## P U B L I C

Enterprise Services and ESR Content
Enterprise Services


3  Other Web Services

This section contains information about other Web services for SAP Transportation Management (SAP TM).

3.1  GetTransportationDocumentURI

## Use

Technical Data

Field

## Value

Operation Name in Enterprise Services Repository (ES Repository) GetTransportationDocumentURI

Namespace in ES Repository

http://sap.com/xi/TMS/UX

Software Component Version in ES Repository

Available as of SAPTM 1.0

Category

## Mode

Business Context and Use

## Inbound

## Synchronous

The GetTransportationDocumentURI operation enables you to display SAP Transportation Management (SAP
TM) documents in SAP ERP while using the following SAP ERP functions:

● Invoice verification (transactions MIRO, MIR7, and MIR4): You can display a specific freight settlement

document in the Web browser from the SAP ERP system. For example, when you enter an invoice received
from a carrier into the SAP ERP system, you can call up the corresponding freight settlement document to
check if the invoice data is correct.

● Agency business (transactions WLF3 and WZR3): You can display a specific freight order or freight

settlement document in the Web browser from the SAP ERP system. For example, when you create a
payment document or vendor billing document in SAP ERP, you can display the corresponding SAP TM
document to verify the data. Note that this is relevant for shippers who use the cost distribution function in
SAP TM.

## Features

The GetTransportationDocumentURI inbound operation in SAP TM is triggered by the
GetTransportationDocumentURI outbound operation in SAP ERP. The GetTransportationDocumentURI

Enterprise Services and ESR Content
Other Web Services

P U B L I C

245


outbound operation in SAP ERP requests the URL of a specific business document. The
GetTransportationDocumentURI inbound operation in SAP TM generates the relevant URL and returns it to the
requesting operation, which calls the browser and displays the document. To generate the URL, the inbound
operation requires the type and number of the business document.

 Note

In the Enterprise Services Repository, the GetTransportationDocumentURI outbound operation in SAP ERP
is available in the SAP_APPL component (as of SAP_APPL 6.04) in the http://sap.com/xi/
APPL/PI/TM/UX namespace.

Notes on SAP Implementation

## Prerequisites

● For invoice verification, you have activated the TMS-ERP: Invoice Integration (LOG_TM_IV_INT) business
function in SAP ERP (available as of SAP enhancement package 4 for SAP ERP 6.0 support package 9). If
you activate this business function, the system displays the TM Doc. tab page in the relevant transactions
in SAP ERP. The tab page contains the Details pushbutton for displaying an SAP TM business document.
The GetTransportationDocumentURI outbound operation in SAP ERP is triggered when a user chooses the
Details pushbutton.

● For agency business integration, you have activated the ERP-TMS: Order and Invoice Integration

(LOG_TM_ORD_INT_II) business function in SAP ERP (available as of SAP enhancement package 5 for
SAP ERP 6.0 support package 9 and SAP enhancement package 6 for SAP ERP 6.0 support package 4). If
you activate this business function, the user can access the relevant SAP TM business documents from the
agency business document in the SAP ERP system.

● You have set up point-to-point communication between the inbound and outbound operation. To enable

the operations to exchange data, you must carry out the required settings in SAP TM and SAP ERP. For
more information, see SAP Note 1451472

.

## Enhancements

The BAdI for GetTransportationDocumentURI (/SCMTMS/TDO_IF_SE_GET_URI) Business Add-In (BAdI) is
available for this operation in SAP TM.

More Information

Freight Settlement

246

## P U B L I C

Enterprise Services and ESR Content
## Other Web Services


BusinessDocumentFlowTMInformationbyBusinessObje
ctReferenceQueryResponse_In

3.2

## Use

Technical Data

Field

## Value

Operation Name in Enterprise Services Repository (ES Repository) BusinessDocumentFlowTMInformationbyBusines­

sObjectReferenceQueryResponse_In

Namespace in ES Repository

http://sap.com/xi/TMS/UX

Software Component Version in ES Repository

Available as of SAPTM 1.10

Category

## Mode

Business Context and Use

## Inbound

## Synchronous

## The inbound operation
BusinessDocumentFlowTMInformationbyBusinessObjectReferenceQueryResponse_In provides a
logistics execution system with information about SAP Transportation Management (SAP TM) documents that
relate to a specific business document in the logistics execution system. For example, TM documents that were
created for an order or delivery that was sent to SAP TM to carry out transportation planning and execution.
The operation provides the logistics execution system with information about the document flow and statuses
of the TM documents.

## Features

A logistics execution system sends the ID and type of the business document for which the TM document flow
and status information is required. The inbound operation
BusinessDocumentFlowTMInformationbyBusinessObjectReferenceQueryResponse_In returns the
required information. This includes the following:

● IDs of the individual TM documents, as well as the references between the TM documents and the business

document in the logistics execution system

● Web URI (Uniform Resource Identifier) of each TM document

For example, Web URIs of the relevant order-based transportation requirement, delivery-based
transportation requirement, and dependent documents such as freight units, freight orders, and freight
settlement documents. This enables the user in the logistics execution system to directly display the TM
documents from the original TM system in the Web browser.

Enterprise Services and ESR Content
Other Web Services

P U B L I C

247


● Statuses of the individual TM business documents and cumulated statuses for the entire business

document in the logistics execution system
For each TM document, the operation sends the following statuses: life cycle status, execution status,
confirmation status, subcontracting status, tendering status, consumption status, and invoicing status.
The operation also sends cumulated statuses. These cumulated statuses apply to the entire business
document in the logistics execution system. For example, if some of the relevant TM business documents
have the life cycle status New and the rest have the status In Process, the life cycle status of the entire
business document in the logistics execution system is set to Partially In Process.

Note the following:

● For freight settlement documents, the operation provides only the life cycle status and invoicing status.
The operation does not provide information about charges (for example, prices or exchange rates).

● For freight orders, the operation provides only the document ID, category, description, and status.

Notes on SAP Implementation

## Integration

You can use this Web service to send document flow and status information to SAP ERP. This enables the user
in SAP ERP to access an overview of the entire ERP-TM process for an individual ERP document and to track
the status of document processing in SAP TM from the SAP ERP system. The document flow and status
information can be displayed for a specific ERP purchase order, stock transport order, sales order, outbound
delivery, or inbound delivery for return orders and purchase orders.

## Prerequisites

You have activated the ERP-TMS: Order and Invoice Integration 2 (LOG_TM_ORD_INT_II) business function in
SAP ERP (available as of SAP enhancement package 5 for SAP ERP 6.0 support package 9 and SAP
enhancement package 6 for SAP ERP 6.0 support package 4). If you activate the business function, the system
displays the TM tab page in the transactions for changing or displaying orders, and it displays the TM
pushbutton in the transactions for changing or displaying deliveries.

In addition, you have sent an ERP order or delivery to SAP TM. For more information about order and delivery
integration, see ERP Logistics Integration.

## Enhancements

The Business Add-In (BAdI) BAdI for
BusinessDocumentFlowTMInformationbyBusinessObjectReferenceQueryResponse_In (/SCMTMS/
BDF_SE_BFDINFO) is available for this operation.

248

## P U B L I C

Enterprise Services and ESR Content
Other Web Services


4  Additional ESR Content

This section contains information about additional Enterprise Services Repository (ESR) content for SAP
Transportation Management (SAP TM).

4.1

## Integration Scenarios

This section contains information about the integration scenarios for SAP TM, which are available in the
Enterprise Services Repository in the SAPTM IC software component in the http://sap.com/xi/TMS/Global/IC
namespace.

4.1.1  TM_ERPInvoiceIntegration

## Use

You can use this integration scenario to transfer settlement documents from SAP Transportation Management
(SAP TM) to SAP ERP to create billing documents or accruals. In a typical shipper scenario, carrier settlement
is achieved by performing accruals posting and invoice verification in SAP ERP based on data provided by SAP
TM.

## Prerequisites

In the Enterprise Services Repository, the TM_ERPInvoiceIntegration integration scenario is in the SAPTM IC
software component in the http://sap.com/xi/TMS/Global/IC namespace.

## Process

The integration scenario comprises the following asynchronous communication steps between an SAP TM
system and an SAP ERP system in the same company.

## Forwarding Settlement

1. Send Forwarding Settlement Request

SAP TM requests the creation, change, or cancellation of a billing document in SAP ERP. The billing
document is based on a forwarding settlement document in SAP TM.

Enterprise Services and ESR Content
Additional ESR Content

P U B L I C

249


For more information about the business context, see the documentation of the following enterprise
services in the Customer Freight Invoice Request Processing process component:

○ Request Customer Freight Invoice Request_V1 [page 212]

○ Request Customer Freight Invoice Request Cancellation_V1 [page 214]

2. Create Customer Invoice

SAP ERP creates, changes, or cancels the billing document based on the request received from SAP TM. It
then sends a confirmation to SAP TM. If SAP ERP cannot send a response for technical reasons, an error is
triggered in SAP ERP.

3. Receive Forwarding Settlement Confirmation

SAP TM receives the confirmation and updates the corresponding forwarding settlement document. If SAP
TM cannot process the confirmation, an error is triggered in SAP TM.
Note that SAP TM can now request the creation of a credit memo in SAP ERP, as follows:

1. SAP TM requests the creation, change, or cancellation of a credit memo in SAP ERP. The credit memo

is based on the billing document that was created in step 2 above.

2. SAP ERP creates, changes, or cancels a credit memo. It then sends a confirmation to SAP TM. If SAP

ERP cannot send a response for technical reasons, an error is triggered in SAP ERP.

3. SAP TM receives the confirmation and updates the corresponding credit memo. If SAP TM cannot

process the confirmation, an error is triggered in SAP TM.

## Freight Settlement

1. Send Freight Settlement Request

SAP TM requests the creation, change, or cancellation of accruals in SAP ERP (that is, the creation of a
service purchase order and one or more service entry sheets). The accruals are based on a freight
settlement document in SAP TM. SAP ERP also sends an update to SAP TM as soon as the corresponding
supplier invoice has been posted (that is, invoice verification has been carried out and the accruals have
been posted).
For more information about the business context, see the documentation of the following enterprise
services in the Transportation Order Processing process component:

○ Request Transportation Order Invoicing Preparation [page 73]

○ Request Transportation Order Invoicing Preparation Cancellation [page 76]

2. Create Supplier Invoice

SAP ERP creates, changes, or cancels the accruals (that is, the service purchase order and one or more
service entry sheets) based on the request received from SAP TM. It then sends a confirmation to SAP TM.
If SAP ERP cannot send a response for technical reasons, an error is triggered in SAP ERP.

3. Receive Freight Settlement Confirmation

SAP TM receives the confirmation from SAP ERP and updates the corresponding freight settlement
document. If SAP TM cannot process the confirmation, an error is triggered in SAP TM.

Invoice Notification

1. Send Invoice Notification

SAP ERP sends a notification about the receipt of a supplier invoice to SAP TM.

2. Receive Invoice Notification from ERP

SAP TM receives the invoice notification and updates the posted amounts in the corresponding freight
settlement document. If SAP TM cannot process the invoice notification, an error is triggered in SAP TM.

## Invoice Simulation

1. Simulate Customer Invoice

250

## P U B L I C

Enterprise Services and ESR Content
## Additional ESR Content


SAP TM sends a new or changed forwarding settlement document or credit memo to SAP ERP and
requests the transfer of data to preview the customer invoice or credit memo. SAP ERP returns the
required data to SAP TM.

2. Simulate Forwarding Settlement Request in ERP System

SAP TM uses the data provided by SAP ERP to generate a preview of the customer invoice or credit memo.

Note the following:

● SAP TM can initiate communication at any time starting with the action Send Forwarding Settlement

Request or Send Freight Settlement Request (that is, these actions can be executed independently of each
other).

● SAP ERP can initiate communication starting with the action Send Invoice Notification only if SAP ERP has

already received and processed a freight settlement request from SAP TM (that is, the action Create
Customer Invoice is a prerequisite).

● SAP ERP can initiate communication starting with the action Simulate Customer Invoice only if a customer
invoice has not yet been created in SAP ERP (that is, the action Create Customer Invoice has not been
performed).

More Information

Forwarding Settlement

## Freight Settlement

4.1.2  TM_ERPOrderIntegration

## Use

Orders and deliveries in SAP ERP can be transferred to SAP Transportation Management (SAP TM) and saved
there as transportation requirements. These transportation requirements can then be used as the basis for
further transportation activities (for example, planning). In addition, SAP TM can propose deliveries that can be
created in SAP ERP.

## Prerequisites

In the Enterprise Services Repository, the TM_ERPOrderIntegration integration scenario is in the SAPTM IC
software component in the http://sap.com/xi/TMS/Global/IC namespace.

For more information about configuration and prerequisites, see Configuring Integration of Orders and
Deliveries.

Enterprise Services and ESR Content
Additional ESR Content

P U B L I C

251


## Process

The integration scenario comprises the following asynchronous communication steps between an SAP ERP
system and an SAP TM system in the same company.

## Send SAP ERP Order to SAP TM

1. Send Sales Order to Transportation Management System / Send Customer Return to

Transportation Management System / Send Purchase Order to Transportation
## Management System
When a sales order, returns order, or purchase order is created, changed, or canceled in the SAP ERP
system, SAP ERP sends the order to SAP TM. The same applies to stock transport orders, returns
purchase orders, and returns stock transport orders.

 Note

The documents are only sent to SAP TM if the SAP ERP system has been configured accordingly (in
particular, with respect to the corresponding document types). For more information about the
required settings, see Configuring Integration of Orders and Deliveries.

2. Import Order from SAP ERP

SAP TM creates, changes, or cancels an order-based transportation requirement (OTR) based on the
request received from SAP ERP. Based on the OTRs, freight units can be created in SAP TM and
transportation planning can be carried out. The results of transportation planning can then also form the
basis of the creation of delivery proposals.
For more information, see Integration of ERP Orders and Deliveries in Transp. Planning.

Send Delivery Proposal to SAP ERP (Outbound Delivery)

1. Send Outbound Delivery Proposal (as Bulk)

SAP TM creates delivery proposals and sends them to SAP ERP to request the creation of the
corresponding deliveries. In this step, multiple delivery proposals may be grouped into a bulk message to
enable joint transmission, and to ensure that the delivery proposals are processed in the correct sequence
and with sufficient levels of performance.
For more information, see Creation of ERP Deliveries from SAP TM.

2. Create Outbound Delivery (as Bulk)

SAP ERP creates one or more outbound deliveries based on the delivery proposals received from SAP TM.
SAP ERP might split the proposed deliveries (for example, based on additional split criteria defined in SAP
ERP).
SAP ERP sends a bulk confirmation to SAP TM, which contains individual confirmations for each delivery
proposal in the bulk request that was received from SAP TM. If SAP ERP cannot process the complete
request, an error is triggered in SAP ERP.

3. Receive Outbound Delivery Bulk Confirmation

SAP TM receives the bulk confirmation from SAP ERP and creates an entry in the application log. The
application log entry includes the system messages that were created in SAP ERP during delivery creation,
as well as the total number of deliveries created in SAP ERP and the ID of each delivery. If an error occurred
during delivery creation in SAP ERP, SAP TM generates an alert.
When a confirmation is received, SAP TM sets a confirmation timestamp in the relevant freight units. The
timestamp is used to monitor whether SAP ERP has responded. For more information, see Monitoring of
Delivery Creation.

Send Delivery Proposal to SAP ERP (Inbound Delivery)

252

## P U B L I C

Enterprise Services and ESR Content
Additional ESR Content


1. Send Inbound Delivery Proposal

SAP TM creates delivery proposals and sends them to SAP ERP to request the creation of the
corresponding deliveries. Note that inbound delivery proposals are sent using single messages; unlike
outbound delivery proposals, which are sent using bulk messages.
For more information, see Creation of ERP Deliveries from SAP TM.

2. Create Inbound Delivery

SAP ERP creates one or more inbound deliveries based on the delivery proposals received from SAP TM.
SAP ERP might split a proposed delivery (for example, based on additional split criteria defined in SAP
ERP).
SAP ERP sends a confirmation to SAP TM. If SAP ERP cannot process the complete request, an error is
triggered in SAP ERP.

3. Receive Inbound Delivery Confirmation

SAP TM receives the confirmation from SAP ERP and creates an entry in the application log. The
application log entry includes the system messages that were created in SAP ERP during delivery creation,
as well as the total number of deliveries created in SAP ERP and the ID of each delivery. If an error occurred
during delivery creation in SAP ERP, SAP TM generates an alert.
When a confirmation is received, SAP TM sets a confirmation timestamp in the relevant freight units. The
timestamp is used to monitor whether SAP ERP has responded. For more information, see Monitoring of
Delivery Creation.

## Send SAP ERP Delivery to SAP TM

1. Send Outbound Delivery to Transportation Management System / Send Inbound Delivery

to Transportation Management System
When an outbound delivery or inbound delivery is created, changed, or canceled in the SAP ERP system,
SAP ERP sends the delivery to SAP TM.

 Note

The execution of this step does not depend on delivery creation having been triggered by a delivery
proposal received from SAP TM. For example, this step can also be carried out if the delivery was
created manually in SAP ERP. For more information, see Integration of ERP Deliveries.

Outbound deliveries and inbound deliveries are sent to SAP TM only if the SAP ERP system has been
configured accordingly (in particular, with respect to the corresponding delivery types). For more
information about the required settings, see Configuring Integration of Orders and Deliveries.

2. Import Delivery from SAP ERP

SAP TM creates, changes, or cancels a delivery-based transportation requirement (DTR) based on the
request received from SAP ERP. When SAP TM creates the DTR, the DTR consumes the transportation
demand of the corresponding order-based transportation requirement or requirements, if applicable. That
is, SAP TM determines the corresponding OTR items and reassigns the freight units to the DTR.
For more information, see Integration of ERP Orders and Deliveries in Transp. Planning.

Split Outbound Delivery

1. Send Outbound Delivery Split

Based on planning changes, SAP TM requests that an outbound delivery is split in SAP ERP.

2. Split Outbound Delivery

SAP ERP splits the outbound delivery and sends a confirmation to SAP TM.

3. Receive Outbound Delivery Split Confirmation
SAP TM receives confirmation of the split from SAP ERP.

Enterprise Services and ESR Content
Additional ESR Content

P U B L I C

253


 Note

SAP ERP sends the new delivery and the changed original delivery to SAP TM in separate messages
(see the steps under Send SAP ERP Delivery to SAP TM). SAP TM can then create the new DTR
and change the original DTR.

Update Outbound Delivery

1. Send Outbound Delivery Update

Based on planning changes related to changed dates, SAP TM requests that an outbound delivery is
updated in SAP ERP.

2. Update Outbound Delivery

SAP ERP updates the outbound delivery and sends a confirmation to SAP TM.

3. Receive Outbound Delivery Update Confirmation
SAP TM receives confirmation of the update from SAP ERP.

 Note

SAP ERP sends the updated outbound delivery to SAP TM in a separate message (see the steps under
Send SAP ERP Delivery to SAP TM). SAP TM can then update the corresponding DTR.

## More Information

ERP Logistics Integration

4.1.3  TM_ERPSalesOrderScheduling

## Use

A shipper can use this integration scenario to carry out transportation planning synchronously in SAP
Transportation Management (SAP TM) during sales order processing in SAP ERP. This enables the
transportation situation to be taken into account when calculating feasible dates and quantities for sales order
items.

## Prerequisites

In the Enterprise Services Repository, the TM_ERPSalesOrderScheduling integration scenario is in the SAPTM
IC software component in the http://sap.com/xi/TMS/Global/IC namespace.

For more information about configuration and prerequisites, see the documentation of the corresponding
service interfaces:

● Intracompany Transportation Requesting Out outbound service interface in the Sales Order Processing

process component

254

## P U B L I C

Enterprise Services and ESR Content
## Additional ESR Content


● Intracompany Transportation Requesting In inbound service interface in the Transportation Request

Processing process component (see Intracompany Transportation Requesting In [page 129])

## Process

The integration scenario comprises the following synchronous communication steps between an SAP ERP
system and an SAP TM system in the same company:

1. Simulate Sales Order in Transportation Management System

While creating, changing, or rescheduling a sales order in sales order processing in SAP ERP, a shipper
triggers sales order scheduling for the sales order items. SAP ERP sends the sales order data to SAP TM
and requests the simulation of an order-based transportation requirement (OTR) and the related planning
activities.

2. Simulate ERP Sales Order

When SAP TM receives the sales order data, it creates a temporary OTR, triggers transportation planning,
and returns the planning results to SAP ERP. When SAP ERP receives the results of the simulation, it
updates the schedule lines of the sales order accordingly.

## More Information

Simulate Transportation Request [page 133]

Scheduling of SAP ERP Sales Orders in SAP TM

4.1.4  TM_ERPShipmentIntegration_Out

## Use

A shipper can use this integration scenario to perform transportation execution in SAP ERP. After carrying out
transportation planning for delivery-based transportation requirements (DTRs), a shipper can carry out
transportation execution for the resulting freight orders or freight bookings either in SAP Transportation
Management (SAP TM) or in SAP ERP. If a shipper uses SAP ERP for transportation execution, the SAP TM
system sends relevant information about the freight orders or freight bookings to SAP ERP, based on which the
SAP ERP system creates shipments. The shipments can form the basis of further processing in SAP ERP, for
example, execution tracking, invoicing, or output management.

## Prerequisites

In the Enterprise Services Repository, the TM_ERPShipmentIntegration_Out integration scenario is in the
SAPTM IC software component in the http://sap.com/xi/TMS/Global/IC namespace.

Enterprise Services and ESR Content
Additional ESR Content

P U B L I C

255


For more information about configuration and prerequisites, see the documentation of the corresponding
Transportation Order Execution Out outbound service interface in the Transportation Order Processing process
component.

## Process

The integration scenario comprises the following asynchronous communication steps between an SAP TM
system and an SAP ERP system in the same company.

Create Shipment in SAP ERP

1. Send Freight Order

SAP TM requests the creation or change of a shipment in SAP ERP. The shipment is based on a freight
order or freight booking in SAP TM and on one or more deliveries that are referenced by the freight order or
freight booking.

2. Create Shipment

SAP ERP creates or changes a shipment based on the request received from SAP TM. SAP ERP then sends
a confirmation to SAP TM. If SAP ERP cannot send a response for technical reasons, an error is triggered in
SAP ERP.

3. Receive Shipment Confirmation

SAP TM receives the confirmation from SAP ERP and updates the corresponding freight order or freight
booking. If SAP TM cannot process the confirmation, an error is triggered in SAP TM.

## Notify of Status Change

1. Send Notification About Execution Status Change

When the execution status of the shipment changes, SAP ERP can send a notification to SAP TM. SAP ERP
sends a notification only if you have configured the SAP ERP system accordingly.

2. Receive Notification About Shipment Status Change

SAP TM receives the notification from SAP ERP and updates the corresponding freight order or freight
booking. If SAP TM cannot process the notification, an error is triggered in SAP TM.

Send Cancellation to SAP ERP

1. Send Freight Order Cancellation

If a freight order or freight booking that has already been sent to SAP ERP is canceled in SAP TM, SAP TM
sends a cancellation request to SAP ERP to trigger the cancellation of the corresponding shipment. SAP
TM sends a cancellation request only if you have configured the SAP TM system accordingly.

2. Delete Shipment

SAP ERP deletes the shipment based on the request received from SAP TM. If an error occurs during
deletion, this error is only visible in SAP ERP.

Notify of Changed Delivery Assignment

1. Send Notification About Changed Delivery Assignment

If a delivery is removed from or assigned to the shipment, SAP ERP sends a notification to SAP TM. SAP
ERP sends a notification only if you have configured the SAP ERP system accordingly.

2. Receive Notification About Changed Delivery Assignment

SAP TM receives the notification from SAP ERP and updates the corresponding freight order or freight
booking. If SAP TM cannot process the notification, an error is triggered in SAP TM.

Notify of Changed Packaging and Item Assignment

256

## P U B L I C

Enterprise Services and ESR Content
## Additional ESR Content


1. Send Notification About Changed Packaging and Item Assignment

SAP TM can send packaging information to SAP ERP with the freight order or freight booking data. Based
on this data, SAP ERP creates handling units, using container as the packaging material. When container
IDs and items have been assigned to the handling units in SAP ERP, SAP ERP sends a notification to SAP
TM.

2. Receive Notification About Changed Packaging and Item Assignment

SAP TM assigns the container IDs and package items to the containers in the freight order or freight
booking.

## More Information

Integration with SAP ERP Shipment Processing

4.1.5  TM_ERPShipmentIntegration_In

## Use

A shipper can use this integration scenario to carry out tendering in SAP TM for shipments created in SAP ERP.
SAP TM creates freight orders based on shipments received from SAP ERP. After the shipper has carried out
tendering for a shipment-based freight order, SAP TM returns the tendering result to SAP ERP, which updates
the original shipment.

## Prerequisites

In the Enterprise Services Repository, the TM_ERPShipmentIntegration_In integration scenario is in the SAPTM
IC software component in the http://sap.com/xi/TMS/Global/IC namespace.

## Process

The integration scenario comprises the following asynchronous communication steps between an SAP ERP
system and an SAP TM system in the same company.

Send Shipment

1. Send Shipment

When a shipper initiates tendering for a shipment in SAP ERP, SAP ERP sends the shipment to SAP TM and
requests the creation or change of a freight order. The freight order is based on the shipment and on the
SAP ERP deliveries referenced by the shipment. In addition, a shipper can request the cancellation of an
existing shipment-based freight order.

2. Receive Shipment

Enterprise Services and ESR Content
Additional ESR Content

P U B L I C

257


SAP TM creates, changes, or cancels a freight order based on the shipment data received from SAP ERP.
The shipper can use a shipment-based freight order to carry out tendering.

## Notify of Tendering Result

1. Send Notification About Tendering Result

When the tendering result is available, SAP TM sends the result to SAP ERP (for example, if a carrier has
been found, SAP TM sends the carrier, price, and tendering status).

2. Receive Notification About Tendering Result

SAP ERP updates the shipment according to the tendering result received from SAP TM.

More Information

## Shipment-Based Tendering

4.1.6  TM_GTSExportDeclarationIntegration

## Use

You can use this integration scenario to integrate SAP Transportation Management (SAP TM) with SAP Global
Trade Services. When you create an export declaration in SAP TM, SAP Global Trade Services automatically
handles the required customs processes. SAP TM receives a confirmation from SAP Global Trade Services and
can then set the relevant customs status.

## Prerequisites

In the Enterprise Services Repository, the TM_GTSExportDeclarationIntegration integration scenario is in the
SAPTM IC software component in the http://sap.com/xi/TMS/Global/IC namespace.

## Process

The integration scenario comprises the following asynchronous communication steps between SAP TM and
SAP Global Trade Services:

1. Send Export Declaration Request

On the basis of an order, SAP TM sends a request to create or cancel an export declaration.

2. Receive Export Declaration Request

SAP Global Trade Services receives the request, creates or cancels an export declaration, and sends back a
confirmation.

3. Receive Export Declaration Confirmation

SAP TM receives the confirmation and updates the corresponding order.

258

## P U B L I C

Enterprise Services and ESR Content
Additional ESR Content


## More Information

Integration with SAP Global Trade Services

4.1.7  TM_GTSTradeComplianceCheckIntegration

## Use

You can use this integration scenario to integrate SAP Transportation Management (SAP TM) with SAP Global
Trade Services. It enables you to perform a trade compliance check in SAP Global Trade Services for SAP TM
business documents.

## Prerequisites

In the Enterprise Services Repository, the TM_GTSTradeComplianceCheckIntegration integration scenario is in
the SAPTM IC software component in the http://sap.com/xi/TMS/Global/IC namespace.

## Process

The integration scenario comprises the following asynchronous communication steps between SAP TM and
SAP Global Trade Services:

1. Send Trade Compliance Check Request

SAP TM requests a trade compliance check for a business document (for example, forwarding order or
freight order). SAP TM sends the request to SAP Global Trade Services.

2. Receive Trade Compliance Check Request

SAP Global Trade Services receives the business document data, performs the trade compliance check,
and returns the result to SAP TM.

3. Receive Trade Compliance Check Confirmation

SAP TM receives the result of the check and updates the status of the business document accordingly.

More Information

## Trade Compliance Check

Enterprise Services and ESR Content
Additional ESR Content

P U B L I C

259


4.1.8  TM_FINCreditManagementIntegration

## Use

You can use this integration scenario to perform a credit limit check on a business partner in SAP
Transportation Management (SAP TM) based on credit information provided by SAP Credit Management. It
enables you to request information about a business partner and send updates to SAP Credit Management
about the business partner's credit commitments.

## Prerequisites

In the Enterprise Services Repository, the TM_FINCreditManagementIntegration integration scenario is in the
SAPTM IC software component in the http://sap.com/xi/TMS/Global/IC namespace.

## Process

The integration scenario comprises the following communication steps between an SAP TM system and an
SAP Credit Management system in the same company.

Creditworthiness Query (Synchronous Communication)

1. Send Creditworthiness Query

When you create or change a forwarding order, you perform a credit limit check on the business partner
specified in the forwarding order. SAP TM requests information about the business partner from SAP
Credit Management.

2. Receive Creditworthiness Query

SAP Credit Management receives the request and sends back the relevant credit information. Based on the
response, you can decide whether to approve the forwarding order.

Credit Commitment Notification (Asynchronous Communication)

1. Send Credit Commitment Notification

SAP TM informs SAP Credit Management about the business partner's credit commitments. Note that
SAP TM sends a notification when you approve a forwarding order and when you perform forwarding
settlement for an approved forwarding order.

2. Receive Credit Commitment Notification

SAP Credit Management receives the information and updates the credit exposure information for the
business partner.

More Information

Credit Limit Check

260

## P U B L I C

Enterprise Services and ESR Content
Additional ESR Content


4.2  Mappings

This section contains information about the interface mappings and message mappings for SAP
Transportation Management (SAP TM). They are available in the Enterprise Services Repository in the SAPTM
IC software component in the http://sap.com/xi/TMS/Global/IC namespace.

 Note

All interface mappings and message mappings use one of the following naming conventions, depending on
the direction of communication:

● <Message name in SAP TM>_to_<IDoc type in SAP ERP>

● <IDoc name in SAP ERP>_to_<message name in SAP TM>

For more information about using mappings, see the Description field for each mapping in the Enterprise
Services Repository.

4.2.1  Interface Mappings for Shipment Integration

## Use

In the integration scenarios TM_ERPShipmentIntegration_Out and TM_ERPShipmentIntegration_In, interface
mappings are used to map messages from an SAP Transportation Management (SAP TM) system to IDocs in
an SAP ERP system, and vice versa.

The following interface mappings are available for the TM_ERPShipmentIntegration_Out integration scenario:

● TransportationOrderSCMExecutionRequest_to_SHPMNTSHPMNT05

● SHPMNTSHPMNT05_to_TransportationOrderSCMExecutionConfirmation

● SHPMNTSHPMNT05_to_TransportationOrderSCMExecutionStatusNotification

● TransportationOrderSCMExecutionCancellationRequest_to_SHIPPLTPSSHT01

The following interface mappings are available for the TM_ERPShipmentIntegration_In integration scenario:

● SHPMNTSHPMNT05_to_TransportationOrderSCMRequest_In

● SHIPPLTPSSHT01_to_TransportationOrderSCMCancellationRequest_In

● TransportationOrderSCMTenderingResultNotification_to_SHPMNT_TNDRSHPMNT05

● SHPMNTSHPMNT05_to_TransportationOrderSCMCancellationRequest_In

## More Information

Message Mappings for Shipment Integration [page 262]

Enterprise Services and ESR Content
Additional ESR Content

P U B L I C

261


4.2.2  Message Mappings for Shipment Integration

The following message mappings are available for the TM_ERPShipmentIntegration_Out integration scenario:

● TransportationOrderSCMExecutionRequest_to_SHPMNTSHPMNT05

For more information, see TransportationOrderSCMExecutionRequest_to_SHPMNTSHPMNT05 [page
262]

● SHPMNTSHPMNT05_to_TransportationOrderSCMExecutionConfirmation

● SHPMNTSHPMNT05_to_TransportationOrderSCMExecutionStatusNotification

● TransportationOrderSCMExecutionCancellationRequest_to_SHIPPLTPSSHT01

For more information, see TransportationOrderSCMExecutionCancellationRequest_to_SHIPPLTPSS [page
263].

The following message mappings are available for the TM_ERPShipmentIntegration_In integration scenario:

● SHPMNTSHPMNT05_to_TransportationOrderSCMRequest

● SHIPPLTPSSHT01_to_TransportationOrderSCMCancellationRequest

● TransportationOrderSCMTenderingResultNotification_to_SHPMNT_TNDRSHPMNT05

● SHPMNTSHPMNT05_to_TransportationOrderSCMCancellationRequest

4.2.2.1

TransportationOrderSCMExecutionRequest_to_SHP
MNTSHPMNT05

## You can use this message mapping to map the message type
TransportationOrderSCMExecutionRequest in SAP TM to the IDoc SHPMNT.SHPMNT05 in SAP ERP.

Note the following:

● For each line in the root structure of the message that provides the input for the mapping, the system

creates a line in the root structure of the message that is created as a result of the mapping.

● The freight order ID (field ID of TransportatonOrderExecution) is mapped to field TKNUM in the

resulting root structure E1EDT20; that is, the freight order ID in SAP TM is used as the ID of the shipment
created in SAP ERP.
To enable the freight order ID to be used as the shipment ID, you have to configure the use of external
number ranges for the relevant shipment types.

● The content of the fields E1EDT20-SHTYP (header level, shipment type) and E1ADRM4[2]-E1ADRE4-
EXTEND_D (address, transportation planning point) are defined dynamically at runtime using value
mapping. This means that during system configuration, mapping tables that depend on the actual system
landscape are defined in the Integration Directory of the PI system.

The following user-defined functions are used in this message mapping:

● convXSDduration

This function converts the duration in XSD format into the duration format expected in the ERP shipment.
It contains the following parameters:

○ Inbound parameter: Duration in XSD format

○ Outbound parameter: Duration in the simple format expected by the ERP shipment

262

## P U B L I C

Enterprise Services and ESR Content
Additional ESR Content


● GetLastTen

This function reformats freight order IDs and delivery IDs to 10 digits, if necessary by padding the ID with
leading zeros (for example, ID 1489 is reformatted to 0000001489). It contains the following parameters:

○ Inbound parameter: String (that is, the ID of the freight order or delivery)

○ Outbound parameter: String consisting of 10 digits

● deriveStageDel

This function derives the ID of the delivery that is assigned to a transportation stage. It contains the
following parameters:

○ Inbound parameter: Item ID; ID of the delivery to which the item is assigned; ID of the assignment of a

transportation stage to the item

○ Outbound parameter: ID of the delivery that is assigned to the transportation stage

4.2.2.2

TransportationOrderSCMExecutionCancellationReq
uest_to_SHIPPLTPSSHT01

## You can use this message mapping to map the message type
TransportationOrderSCMExecutionCancellationRequest in SAP TM to the IDoc SHPMNT.SHIPPL in
SAP ERP.

Note the following:

● For each line in the root structure of the message that provides the input for the mapping, the system

creates a line in the root structure of the message that is created as a result of the mapping.

● The freight order ID (field ID of TransportatonOrderExecution) is mapped to field SHPID in the

resulting root structure E1TPSHH. That is, the freight order ID in SAP TM is the ID of the shipment in SAP
ERP that is to be deleted.

● The content of the E1TPSHH-SHPPPT field (header level, transportation planning point) is defined

dynamically at runtime using value mapping. This means that during system configuration, mapping tables
that depend on the actual system landscape are defined in the Integration Directory of the PI system.

Enterprise Services and ESR Content
Additional ESR Content

P U B L I C

263


Important Disclaimers and Legal Information

## Hyperlinks

Some links are classified by an icon and/or a mouseover text. These links provide additional information.

About the icons:

●

## Links with the icon

: You are entering a Web site that is not hosted by SAP. By using such links, you agree (unless expressly stated otherwise in your

agreements with SAP) to this:

●

●

The content of the linked-to site is not SAP documentation. You may not infer any product claims against SAP based on this information.

SAP does not agree or disagree with the content on the linked-to site, nor does SAP warrant the availability and correctness. SAP shall not be liable for any

damages caused by the use of such content unless damages have been caused by SAP's gross negligence or willful misconduct.

●

## Links with the icon

: You are leaving the documentation for that particular SAP product or service and are entering a SAP-hosted Web site. By using such

links, you agree that (unless expressly stated otherwise in your agreements with SAP) you may not infer any product claims against SAP based on this

information.

## Beta and Other Experimental Features

Experimental features are not part of the officially delivered scope that SAP guarantees for future releases. This means that experimental features may be changed by

SAP at any time for any reason without notice. Experimental features are not for productive use. You may not demonstrate, test, examine, evaluate or otherwise use

the experimental features in a live operating environment or with data that has not been sufficiently backed up.

The purpose of experimental features is to get feedback early on, allowing customers and partners to influence the future product accordingly. By providing your

feedback (e.g. in the SAP Community), you accept that intellectual property rights of the contributions or derivative works shall remain the exclusive property of SAP.

## Example Code

Any software coding and/or code snippets are examples. They are not for productive use. The example code is only intended to better explain and visualize the syntax
and phrasing rules. SAP does not warrant the correctness and completeness of the example code. SAP shall not be liable for errors or damages caused by the use of
example code unless damages have been caused by SAP's gross negligence or willful misconduct.

## Gender-Related Language

We try not to use gender-specific word forms and formulations. As appropriate for context and readability, SAP may use masculine word forms to refer to all genders.

264

## P U B L I C

Enterprise Services and ESR Content
Important Disclaimers and Legal Information


Enterprise Services and ESR Content
Important Disclaimers and Legal Information

P U B L I C

265


www.sap.com/contactsap

© 2019 SAP SE or an SAP affiliate company. All rights reserved.

No part of this publication may be reproduced or transmitted in any form
or for any purpose without the express permission of SAP SE or an SAP
affiliate company. The information contained herein may be changed
without prior notice.

Some software products marketed by SAP SE and its distributors
contain proprietary software components of other software vendors.
National product specifications may vary.

These materials are provided by SAP SE or an SAP affiliate company for
informational purposes only, without representation or warranty of any
kind, and SAP or its affiliated companies shall not be liable for errors or
omissions with respect to the materials. The only warranties for SAP or
SAP affiliate company products and services are those that are set forth
in the express warranty statements accompanying such products and
services, if any. Nothing herein should be construed as constituting an
additional warranty.

SAP and other SAP products and services mentioned herein as well as
their respective logos are trademarks or registered trademarks of SAP
SE (or an SAP affiliate company) in Germany and other countries. All
other product and service names mentioned are the trademarks of their
respective companies.

Please see https://www.sap.com/about/legal/trademark.html for
additional trademark information and notices.

Material Number: 50137586

*50137586*

## THE BEST RUN
