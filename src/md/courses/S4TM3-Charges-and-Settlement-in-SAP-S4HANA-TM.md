S4TM3 - Charges and Settlement in
## SAP S/4HANA TM

Unit 1 - Managing Transportation as Part of SAP S/4HANA Enterprise Management

2-10

Unit 2 - Managing Transportation Charge Master Data

Unit 3 - Calculating Charges

Unit 4 - Managing Freight Settlement

Unit 5 - Distributing Transportation Costs

## Unit 6 - Procuring Strategic Freight

Unit 7 - Managing the Embedded Logistics Service Provider Process

11-72

73-109

110-147

148-175

176-204

205-211


Unit  1  -  Managing  Transportation  as  Part  of  SAP

## S/4HANA Enterprise Management

## Lesson 1 - Evaluating Transportation Management

Companies  have  been  shipping  products  across  countries  and  continents  for

centuries.  The  concept  of  managing  the  transportation  of  products  is  not  new.

However,  using  new  methodologies  and  technology  can  make  a  difference  in  an

industry.  Today,  most  economies  are  wholly  reliant  on  efficient  transportation

logistics.

With the shift in recent years towards a global economy, crossing borders has become

commonplace.  Reaching  customers  in  more  remote  locations  and  sourcing  the

procurement of product from multiple vendors or locations has increased the cost of

transporting  products.  As  the  world  becomes  smaller,  the  team  tasked  with

maintaining logistics must respond faster and more cost-effectively.

Global natural disasters and other dangers show the vulnerability of the global supply

chain.  Despite  these  challenges,  the  transportation  part  of  the  supply  chain,  in

particular,  has  to  solve  the  problems  that  arise  to  keep  factories  running  and
customers supplied.

## Executive Decisions

The following examples are issues that key executives face:

●  How can I manage my logistics network in a holistic fashion?

●  How can I minimize the risk factors throughout my supply chain?

●  How can I reduce my operational costs and better understand transportation

costs at the customer level?

●  How can I ensure the best possible usage of my assets? How do I ensure high

customer service levels and responsiveness to unexpected supply chain

events?

2


●  How do I ensure I am compliant with all of the varying regulations and

compliance policies?

Transportation  management  is  never  an  isolated  process.  Rather,  it  is  always

integrated  into  other  business  processes.  If  transportation  management  is  poorly

organized, it may have a negative impact on related business processes, for example,

manufacturing or distribution.

## Evolution of Transportation Management at SAP

SAP  Transportation  Management  (TM)  6.0  and  7.0  evolved  from  the  SAP

Transportation  Planning/Vehicle  Scheduling  (TPVS)  solution.  With  SAP  TM  8.0,  the

architecture was redesigned and the execution was improved.

As  time  went  on,  customer  feedback  and

lessons

learned  from  the  early

implementations  were  used  as  a  basis  for  improving  the solution further. As society

and  business  make  the  move  to  mobile,  SAP  TM  is  evolving  accordingly  and  now

includes  several  mobile-friendly  elements.  For  example,  drivers  can  input  updates

using  mobile  devices  and  this  information  can  be  used  to  update  customers  of

possible  delays.  While  previous  iterations  included  integration  with  Global  Trade

Services  (GTS)  and  facilitated  compliance,  the  focus  more  recently  has  been  on

improving the shipper and freight forwarder elements of SAP TM.

3


## Deployment Options and Migration Paths

SAP  Transportation  Management  as  part  of  SAP  S/4HANA  is  optimized  for  the

processing  of  system  internal  transportation  demand,  with  regards  to  data footprint

and TCO:

●  No replication of master data and customizing

●  No replication of transactional data (for example, the freight unit is directly

integrated in system internal predecessor documents without the need of the

TM business object TRQ in between, which stores replicated order data)

●  Direct integration of predecessor and successor documents without web

service messages and monitoring of corresponding queues

As of SAP S/4HANA 1709, SAP Transportation Management as part of SAP S/4HANA

also  supports  side-by-side  scenarios,  which  means  that  transportation  demand  can

also  be  received  from  other  SAP  ERP  or  SAP  S/4HANA  instances  to  process  the

necessary steps for planning and execution and send back the needed information to

the  source  system  of  the demand. In this case, replication of data is needed and the

mentioned advantages for system internal processing do not apply.

4


From  a  system  perspective,  an  SAP  S/4HANA  system  has  to  be  installed  and

Transportation  Management  capabilities  can  be  used  for  the  following  different

scenarios:

1.  System internal integration of SAP Transportation Management with SAP

S/4HANA Enterprise Management applications in the same system instance

("Embedded")

2.  System external integration of SAP Transportation Management with SAP

S/4HANA Enterprise Management or ERP applications in other system

instances ("Side-by-Side")

Benefits of SAP Transportation Management

The benefits derived from using SAP TM include the following:

●  Reduced costs and improved operational performance

●

Improved carrier collaboration and resource utilization

●  Efficient end-to-end order and process management

●  Efficient logistics and fulfillment processes

●

Improved execution visibility and responsiveness

5


In many cases, responsibility does not end by executing the shipment. Often, strategic

contracts  require  that  the  shipments  are  traced,  to  provide  visibility  so  that  you  can

recognize  and  react  to  potential  delays  that  could  jeopardize  customer service. This

information  is  not  often  made  available  to  ERP  systems,  whose  concern  is  more

finance-driven  than  service-driven.  Depending  on  the  type  of products that are being

transported  to  different  countries,  compliance  with  regional  regulations  regarding

dangerous goods must be reviewed and adhered to.

With  SAP  TM,  existing  SAP  ERP  customers  can  achieve  integrated order processing

and  management.  SAP  TM

is  delivered  with  out-of-the-box

integration,  with

order-to-cash  and  procure-to-pay  scenarios  to  support  timely  execution  updates.  In

addition,  integrated  freight  settlement  with  SAP  ERP  billing and invoicing is available

for  customers who want to increase the speed at which business process cycles are

executed.  More  planning  features  are  available  to  support  comprehensive  order

management. This includes forwarding, freight (land), and booking (sea and air) order,

and  intermodal  scenarios.  This  integrated  environment  provides  full  document  flow

and order lifecycle management, as well as a centralized order data management tool

for planning, tendering, and so on.

## Transportation Management - Overview

A typical transportation process starts with order management. Order management is

the  process  of  creating  a  transportation  requirement.  Transportation  requirements

can  be  sales  orders,  purchase  orders,  deliveries,  and  so  on.  In  a  second  step,  these

transportation  requirements  are  planned.  SAP  TM  offers  manual  planning functions,

optimizer planning, and semiautomated processes (transportation proposal creation).

Different  aspects of planning supported by SAP TM are means-of-transport selection

(for  example,  rail  versus  road),  carrier  selection  based  on  real  carrier  rates,  load

6


optimization (3D-planning of container/truck utilization). Once the planning process is

finished,  SAP  TM  also  supports  the  execution  of  transports.  Execution  includes

delivery  creation,  document  creation  (print  or  electronic,

like  waybills),  event

management

integration  (track  and  trace),  and  warehouse

integration  (EWM

integration). If you do not operate your own fleet, you must make sure that the external

carrier  is  paid  for  their  services.  SAP  TM  allows you to maintain freight agreements,

calculation sheets, and rate tables to accurately define real carrier costs, which can be

used for charge calculation (already in the planning phase, carrier selection), but also

for  settlement  processes  after  the  transport  has  been  executed.  Analytics  and

reporting functionalities complete the available functions of SAP TM.

End-to-End Transportation Processes

Transportation Management - Object Overview

7


Transportation Management Main Areas:

●  Requirements and Order Management

●  Transportation Planning

●  Transportation Execution

●  Freight Costing and Settlement

●  Analytics and Collaboration

Requirements  Management  &  Order  Management:  The  transportation  process

initiates with the management of transportation requirements and order processing.

For shippers, the creation of these requirements can occur in two distinct scenarios:

●

Integrated Sales Order and Delivery Process: Sales order and delivery

processes as well as transportation management are handled inside the same

instance/system. Logistics business documents derived from Sales and

Distribution (SD), Materials Management (MM), or those generated in Logistics

Execution (LE) serve as the source for transportation requirements and

planning.

●  Decentralized Sales Order and Delivery Process: Sales orders and delivery are

handled in one instance/system and transportation management is done in a

separate instance/system. Order-based transportation requests

(OTR)/delivery-based transportation (DTR) request represents a transportation

demand based on an order/delivery that was created in an SAP S/4HANA ERP

system. In this scenario, the order-based transportation requirements or

delivery-based transportation requirements serve as the source for

transportation requirements and planning.

For  LSPs,  forwarding  order/forwarding  quotations  serve  as  the  source  for

transportation requirements and planning.

All  the  above-mentioned  documents  serve  as  the  source  for  transportation

requirements  and  planning.  The  data  from  these  source  documents  is  used  to

generate  the  Freight  unit.  The  business  document  data, with the freight unit building

rules  from the basis for the building freight unit. A freight unit represents a collection

8


of  goods  that  can  be  transported  throughout  the  complete  transportation  process

chain.

During  planning,  freight  units  are  assigned  to  means  of  transport  to  create  freight

orders. SAP TM offers choices for manual planning, optimization-driven planning, and

semiautomated  procedures  such  as  generating  transportation  proposals,  creating

unified  packaging  hierarchies,  and  optimizing  loads.  Load  optimization  specifically

aims to maximize the utilization of container or truck space within a three-dimensional

framework.  In  the  planning  process,  various  attributes  (including  those  associated

with  time  and  geography),  capacities  (encompassing  vehicle  resources,  types,  and

schedules),  and  elements  related  to  the  transportation  network  (involving  locations,

zones,  and  lanes)  are  considered.  Also,  the  planning  process  addresses constraints,

such as capacity, time, routing, scheduling, and incompatibilities.

Planning  is  conducted  within  the  transportation  cockpit  user  interface  (UI).  The

transportation  cockpit  is  able  to  tailor  its  interface  to  suit  the  specific  planning

scenario being undertaken. This includes options like map-based planning, Gantt chart

planning, drag-and-drop functionality, load planning, and command-based planning, all

of which can be executed seamlessly within the transportation cockpit.

Carrier  selection  can  be  undertaken  either  during  the  planning process or afterward.

Carrier  selection  can  be  executed  through  multiple  methods.  It  can  be  carried  out

manually,  utilizing  optimization  algorithms,  or  via  a  tendering  process.  The  primary

aim  of  carrier  selection  is  to  establish  a  ranked  list  of  carriers  eligible  to  fulfill  a

planned  freight  order.  This  selection  process  considers  various  constraints  such  as

costs, priorities, incompatibilities, and business allocations. The tendering process can

function  as  an  integral  part  of  carrier  selection or operate as a distinct and separate

process.  Within  the  tendering  process, freight orders are proffered to eligible carriers

through a tendering or auction procedure.

Transportation execution encompasses a comprehensive range of activities related to

the  management  and  documentation  of  shipments  during  their  transit.  The  freight

order serves as the foundation of the execution process, providing precise details and

actual  quantities  of  the  cargo  being  transported.  Any  discrepancies  arising  between

9


the  initial  order  capture  and  planning  phases,  and  the  physical  verification  and

handling,  are  systematically  recorded.  Furthermore,  the  process  of  moving  cargo

triggers updates to both the order and cargo status. This includes actions like manual

entry  of  loading  status  into  the  transportation  management  system  or  automatic

updates  facilitated  through  SAP  Event  Management  &  Global  Track  and  Trace,

ensuring real-time visibility and traceability of the shipment's progress.

Charge  management  delivers  comprehensive  financial  insights  by  supplying  precise

details  concerning  costs,  revenue,  and  profitability  within  the  transportation domain.

Within  this  framework,  agreements  play  a  central  role,  serving  as  contractual

instruments  that  represent  both  customers  through  forwarding  agreements  and

suppliers  through  freight  agreements.  These  agreements  make  explicit  reference  to

calculation  sheets that encompass an exhaustive list of charge elements used in the

computation  of  fees  for  customers  or  suppliers.  The  calculation  engine  analyzes

these charge elements within the calculation sheet and calculates the correct fees for

customers or suppliers. The outcomes of these calculations are recorded in either the

forwarding order for customer invoices or the freight order, for supplier invoices.

From  the  forwarding  order  and  freight  order,  draft  invoices  can  be  created  for

settlement  integration  to  the  SAP  S/4HANA  ERP.  To  create  customer  invoices,

forwarding settlement documents are created from the forwarding order and then are

sent  to  ERP  to  create  a  billing  document.  For  supplier  invoice  settlement,  freight

settlement  documents  are  created  from  the  freight  order  and  transferred  to  ERP  to

create accruals and later to create a purchase order and service entry sheet (SES) for

invoice verification or self-billing.

Within  the  SAP  S/4HANA  TM  system,  a  range  of  overview  pages,  reports,  and  KPI

dashboards  have  been  created  that  are  relevant  for  shippers  and  logistic  service

providers.  These  overview  pages  provide  a  consolidate  view  of  all  data  from

day-to-day  activities  and  help  in  real  time  decision-making.  These  pages  can  be

tailored to business roles, users who supervise transportation execution can start their

day by navigating to the freight order execution overview.

10


Unit  2  -  Managing  Transportation  Charge  Master

## Data

Lesson 1 - Managing Charge Calculation Master Data

## Charge Calculations

This course focuses on the following:

●  Master data for charge calculation

●  Charge calculation

●  Freight settlement processes

The focus of this course is on the buying side only. Charge calculation and settlement

related to forwarding orders (the selling side) are not covered.

Transportation Charge Management Solution Overview

11


## Examples of Possible Scenarios

●  A shipper sends a request to a carrier for a quotation to send a product from a

distribution center to a customer.

●  An LSP receives a booking request to transport a container from one port to

another.

●  A shipper sends a request to a carrier to move a product from the

manufacturing plant to a distribution center.

●  A shipper sends a service request to a service provider to execute

transport-related service tasks (value-added services), such as container

cleaning and customs handling.

The charge is determined based on conditions in the business rules framework,

charge calculation master data, and configuration items.

The calculated charge is sent back to the requesting document.

12


Charge calculation also provides information on the charge type, charge category, or

subcategory so that the receiving accounting processes can determine the

organizational unit, cost, or revenue receivers and the general ledger account.

The transportation charge calculation process determines the freight charge for a

given transportation scenario.

## Note

Scenarios related to LSPs are not detailed in this course.

## Charge Requests

The calculated charge request can come from the following SAP TM documents:

●  Freight order

●  Freight booking

●  Service order

●  Dispute

●  Freight agreement RFQ

●  Forwarding quotation

●  Forwarding order

●  Forwarding settlement document

●  Freight settlement document

Master Data Structure

Charge Management Master Data

13


The system calculates transportation charges based on the following master data in

Charge Management:

## Scale template

A scale template can be used to create the scale easily.

## Scale

A scale is a dimension of a rate table.

## Rate table

A rate is a price for a certain transportation service that is only valid for the period as

defined by its validity. A rate is listed in a rate table. This is where the freight rates are

maintained based on the scale specifications.

## Charge types

The charge type describes a specific charge. For example, Haul (Haulage), BAF

(Bunker Adjustment Factor) or FSC (Fuel Surcharge).

Calculation sheet

14


The charge calculation sheet is a hierarchical table used to calculate transportation

charges. It combines the charge types permitted for a document and the sequence in

which the system takes these charge types into account during the calculation.

## Freight agreement

A freight agreement describes the contractual relationship between the freight service

provider (or customer) and the requesting organizational unit. It contains payment

terms, limits, validity period, and valid calculation sheets. Information such as

organizational unit, contracting parties, or conditions can be specified.

## Business Example: Road-Sea-Road

In this scenario, a full container load is being sent via road-sea freight. In SAP SD, a

sales order for the entire move is created. On save of the sales order the system

automatically builds a freight unit for this move. The freight unit is then shown in the

respective SAP TM planning area. The planner decides the routing for the container

move, hence creating stages in the freight unit. Each stage of the freight unit is then

planned separately:

Road-Sea Freight Example: Freight Unit Stages

15


## Stage

Description

## Precarriage

Truck move from shipper origin (Denver)

to port (Newark)

## Main carriage

Vessel move from POL (port of loading)

(Newark) to POD (Port of Destination)

(Rotterdam)

## On-carriage

Truck move from port (Rotterdam) to

customer unloading location (Cologne)

Two freight orders are created: one for the precarriage stage (Chicago to Newark) and

one for the on-carriage stage (Rotterdam to Cologne). The amount calculated for

these stages is used to pay the carrier.

A freight booking is also created for the main carriage stage (Newark to Rotterdam).

The amount calculated for this stage is used to pay the ocean carrier.

Example Calculation for the Freight Booking

16


This example demonstrates how the system calculates the charge for the transport of

the container from Newark to Rotterdam via ocean freight based on the master data.

17


Lesson 2 - Maintaining Scale and Calculation Bases

## Scale Base

The figure shows where the scale resides in the Transportation Charge Management

(TCM) master data structure.

The scale base defines how the system interprets the scale.

You can define scale bases in Customizing for Transportation Management under

Basic Functions→Charge Calculation→Data Source Binding→Define Scale Bases.

Rate Table with Three Scales

18


A scale is used to define a parameter that then defines a rate. For example, if a rate

depends upon distance and weight, you must define a separate scale for distance and

for weight. The distance and weight scales are then used to define the rate. A scale

can be reused in multiple rate tables.

In the example in the figure, the rate table has the following three dimensions:

●  Dest zone

●  Origin location

●  Weight in lbs

Therefore, three scales must be defined for each dimension.

Configuration - Scale Base

19


## Path for Customizing Templates

You can define scale bases in Customizing for Transportation Management under

Basic Functions→Charge Calculation→Data Source Binding→Define Scale Bases.

## Fields

## Field Assignment

Field assignment denotes the internal field from /SCMTMS/S_TCSCALE_ITEM_DB,

which is assigned to the corresponding scale base and stores the scale values for the

scale created with this scale base.

## UoM Relevant

Unit of Measure (UoM) relevance checks if a scale base is relevant for the unit of

measure.

## Dimension

Link to the T006 dimension.

Rounding Rule

20


The rounding rule indicates whether a rounding rule is applicable to the scale or not.

## Numeric

Numeric checks whether the input scale value is numeric or not.

## Crcy Scale base

Checks if the scale base is for currencies (example: amount).

## Raw values

Checks if the scale base is for raw values (examples: business partner, location).

## Date Scale Base

Checks if the scale base is for dates (example: date).

## Example

The cost of a shipment depends upon the weight of the goods and the distance

traveled. Therefore, the weight and distance form the scale base. To define a scale

base for weight, you maintain it in Customizing in the following way:

Scale Base Data

Field

## Value

Scale Base

## WEIGHT

Scale Base Desc.  SCAVAL_WT

## Usage

Base for Scales

UoM Relevant

X

Dimension

Mass

21


Rounding Rule

X

Numeric

X

## Scale Base Enhancement

The standard scale bases reflect the most common in the transportation industry.

There are situations in which you may have unique requirements and need an

enhancement.

You want to add customer-specific scale bases.

1. Extend scale item structure:

Use the extension and include /SCMTMS/INCL_EEW_TC_SCALE_ITEM. Append the

new field with the corresponding data element and search help to structure.

2. Add the scale base in Customizing:

In Customizing, choose Transportation Management → Basic Functions → Charge

Calculation → Data Source Binding for Charge Calculation → Define Scale Bases.

3. Enhance the scale UI:

22


a) Open the Dynpro component configuration /SCMTMS/WDCC_TCM_SCALE_ITM

(package /SCMTMS/UI).

b) Use the Web Dynpro enhancement concept to add a new column. The new field

from the scale item structure will is available here.

c) The column visibility is controlled by the TCM view exit class

/SCMTMS/CL_UI_VIEWEXIT_TCM, method SCALE_ITEM_PROP.

No changes should be necessary.

## Calculation Base

A calculation base identifies the actual base or factor with which the system

calculates the charges for the scale.

There can be various scenarios in which the system must calculate a charge for

different forms of weights, for example, gross weight and net weight.

23


In this case, both gross weight and net weight correspond to the scale base Weight

(W), whose dimension is mass. However, by definition, gross weight, and net weight

are two entirely different charge aspects. Therefore, they have two different

calculation bases, such as "W1" for gross weight and "W2" for net weight.

To follow the scenario given here, you define a calculation base for every scale base.

This calculation base is the final element in the charge determination. This means that

the calculation base is used to determine the charges.

In the figure, the charges depend on the weight and the destination location. The scale

has the scale base Location. This scale base defines that the scale uses locations

only. The scale base can be used for both the source and destination location. The

calculation base DESTLOC determines that the destination location of the freight

order is used. Technically, in the customizing of the calculation base, you define which

field is to be used and which program or class the system calls on to determine the

field value.

If the resolution base in the calculation sheet points to the freight order stage, the

system derives the values from the specific stage and use it in the calculation.

Configuring the Calculation Base

24


The calculation base is defined in Customizing. Choose Transportation

Management→Basic Functions→Charge Calculation→Data Source Binding→Define

Calculation Bases.

In the Customizing activity, you define a calculation base for a scale base.

The calculation base indicates on what base that the charge calculation is executed

for a corresponding scale. You can assign a default calculation type to the calculation

base, for example, absolute or relative. You can also specify the transportation mode

category. This restricts the calculation bases in a rate table to calculation bases that

have the same transportation mode category as the charge type in the rate table and

to those with no specified transportation mode category.

When configuring, the following fields can be specified:

## Scale Base

The Scale Base refers to the scale base, which will be utilized for this calculation.

## Field Assignment

The Field Assignment refers to the internal field assignment of the logistical data.

## Currency Field

The Currency Field is used for a currency-based calculation base.

## Unit Field

The Unit Field is used for quantity-based calculation bases such as weight, volume,

pieces, and so on.

## Helper Assignment

The Helper Assignment refers to the program logic, which links to the data source.

## Use BAdI

Select if a custom-specific logic is to be specified.

25


## Party Role

The Party Role is used when business partners are specified and such role

assignments are required, such as consignee, sold-to, or bill-to party, and so on.

## Calculation Type

You can assign a default calculation type to the calculation base. For "same-scale"

scale bases, the calculation type is absolute, whereas the quantity fields, which refers

from and to will be relative.

## Calculation Usage

The Calculation Usage specifies whether the calculation base is used for manual

charges or rate tables, or whether it can be used in both situations. Leave blank for no

restriction.

## TrM Category

The TrM Category restricts the calculation bases in a rate table to calculation bases

that have the same transportation mode category as the charge type in the rate table

and to calculation bases with no specified transportation mode category.

Calculation Base Enhancement

26


Calculation base enhancement involves extending the communication structure,

adding the calculation base in Customizing, and (optionally) implementing the BAdl or

helper class.

Addition of the Scale and Calculation Base

27


When adding the scale and calculation base, it is often necessary to add a new

resolution base.

To add a new resolution base, you do the following:

●  Adapt the resolution base configuration. Add a new resolution base to table

/SCMTMS/C_RES_BS. This was Customizing, but is now delivered as a control

table. Only the resolution base name must be maintained. All other fields are

currently not used.

●

Implement logic in BAdl. The data access object provides a BAdI:

/SCMTMS/TCC_BO_DATA_ACCESS for customer implementations.

## Note

When creating a custom calculation base, it is always necessary to define a scale

base for that calculation base.

How to Configure Enhancements to a Calculation Base

1. Extend the communication structure:

a) Use the extension included for the calculation base structure:

/SCMTMS/INCL_EEW_TCC_CB.

b) Append a new field with the corresponding data element.

The component name must be the same as on the underlying document.

The field is copied over to the internal communication structure and available in the

engine automatically.

2. Add a calculation base in Customizing:

a) In Customizing, choose Transportation Management → Basic Functions → Charge

Calculation → Data Source Binding → Define Calculation Bases.

b) Add a new entry and use the new field for the field assignment.

28


c) Set the scale base and other properties.

3. Implement the BAdl or helper class.

a) If the calculation base needs additional logic, use the BAdI method

GET_CALC_BASE_VALUES of BAdI /SCMTMS/TCC_BO_DATA_ACCESS. Refer to the

BAdI documentation for details.

b) Set the BAdI flag in the calculation base Customizing.

You can also use the helper class approach, which allows you to extend existing

helper classes. The interface /SCMTMS/IF_TCC_CALC_BASE is similar to the BAdI

interface.

c) Refer to existing helper classes /SCMTMS/CL_TCC_CB_* for sample

implementations.

The BAdI or helper class is called after the value has been retrieved from the

communication structure if a field assignment is provided as well.

## Scale Templates

This figure shows where the scale template resides in the TCM master data structure.

Scale Templates Defined

29


A scale template is used to create a scale automatically. The use of a scale template

is optional, as you can also create a scale manually.

One advantage of using scale templates is that you can predefine available scale

items, reducing the effort required for manual maintenance and avoiding errors due to

typos. A scale template is an efficient way to create scales during rate table

maintenance.

You can create scale templates either in Customizing or as Master Data. When using

Customizing, the templates can be transported between systems and used as

templates for creating scales.

In Customizing, choose Transportation Management→Basic Functions→Charge

Calculation→Basic Settings→Templates→Define Scale Templates.

## Scale Template Fields

The scale template includes the following information:

## Scale template

This is the name of the scale template that the system uses to create a scale.

30


## Scale type

Indicates whether the scale values depict the upper or lower boundaries for the scale

levels. The scale type defines how the system interprets the scale values during

calculation, as follows:

●  From a certain value and upwards (Base Scale)

●  Up to a certain value (To Scale)

●  Exactly one value (Same Scale)

## Scale base

Defines how the system interprets the scale. A parameter or a factor can influence

transportation charges.

You also have the option of creating scale template items.

When creating scale templates using Customizing, you cannot create items for Same

Scales, because they are dependent on Master Data. When creating Scale Templates

as Master Data (using the SAP Fiori Launchpad), you can also maintain scale items

for Same Scales.

Master data templates can be created and used by users who have no authorization

to change customizing. In contrast to templates created in customizing, master data

templates cannot be transported across different systems. In the SAP Fiori

Launchpad Charge Management Worklist, master data and customizing templates

are depicted in their own queries.

Scale Maintenance

31


This diagram shows where the scale resides in the TCM master data structure.

## Scale Maintenance Function

You can use the scale maintenance function to create and change scales. For

example, you can configure the items of a scale according to one of the following:

●  Quantities

32


●  Volumes

●  Weights

●  Distances

●  Points

Scale maintenance is a prerequisite for the maintenance of rates, as scales are the

dimensions of rate tables. You can create scales as own master data, or during rate

table maintenance. If you maintain scales as separate master data objects

independently from rate tables, you can reuse scales in multiple rate tables.

## Scale Creation

You create a new scale in the SAP Fiori Launchpad.

Choose Charge Management→Create Scale.

When creating a scale, enter the following information:

Scale Creation Data

## Field

Description

## Value

## Scale Base

Used to define the parameters that define

## Length, Partner, Weight

the rate and is considered as a dimension

of a rate table.

## Scale Type

Controls how the scale levels are defined.

Base scale: from a

Indicates where the scale values that

certain value (>=)

were specified depict the upper or lower

boundaries for the scale levels.

To Scale: up to a certain

value (<=)

Same scale: for exactly

one value (=)

33


Scale Unit of

Unit of measure for the scale levels.

KG, LB, Day, Mile, KM

Measure

## Rounding

Before the system accesses the scale to

Round Up/Down to 0.01,

## Profile

look up a rate in a rate table, the system

10.00

rounds the input value based on the

rounding profile to determine the right

scale level.

## Calculation

You can specify a calculation type for a

Absolute: This is used

## Type

scale base, which affects how the system

for non-numeric scales

calculates charges with the scale. The

such as Region,

available calculation types are absolute

Transportation Zone, and

and relative. Note that you can specify a

Business Partner.

relative calculation type for numeric scale

bases only.

Relative: This is used for

numeric scales such as

weight, distance, length.

34


## Scale Examples

The figure shows how scales can be created for destination zone, weight, and

location.

35


Lesson 3 - Configuring Charge Types

## Charge Categories

A charge type is the classification of a charge line that plays an important role in how

the system calculates the transportation charges for the charge line, for example, a

base rate, surcharge, or discount.

A charge type can result in a positive or negative value for a charge line. You can also

specify whether a charge type can be an amount or a percentage value.

This figure shows where the charge type resides in the TCM master data structure.

Charge Categories and Subcategories

36


Charge types can be grouped into charge categories. A useful code list is the

UN/EDIFACT codelist 5237. All three entities are freely definable in Customizing.

You can use the charge subcategories of charge types to group and categorize charge

types in a more granular way than charge categories. A suitable example is the code

list resulting from UN/EDIFACT Recommendation 23: "FREIGHT COST CODE # FCC

Harmonization of the Description of Freight Costs and Other Charges".

You define charge categories for charge types in the following Customizing activity: In

Customizing, choose Transportation Management→Basic Functions→Charge

Calculation→Basic Settings→Define Charge Categories.

You define charge subcategories for charge types in the following Customizing

activity: In Customizing, choose Transportation Management→Basic

Functions→Charge Calculation→Basic Settings→Define Charge Subcategories.

Charge categories and subcategories can be assigned in the charge type customizing

activity, and can be used to determine the SD condition type during billing or MM

service master record/ Activity number during settlement.

Charge Types

37


In the Define Charge Types Customizing activity, you define charge types that you can

assign to calculation sheets and rate tables. Once assigned to a calculation sheet line

item or a rate table, a charge type plays an important role in how the system

calculates the transportation charges for that line.

You can define the charge types in the following Customizing activity: In Customizing,

choose Transportation Management→Basic Functions→Charge Calculation→Basic

Settings→Define Charge Types.

## Charge Type Settings

When defining charge types, you can use the following settings:

## Possible Charge Type Settings

●  Specify whether a charge type can result in a positive or negative value.

●  Specify whether a charge type can be an absolute value or a percentage value.

●  Specify whether you want to set the charge type as an absolute value or a

percentage value each time you assign the charge type.

●  Assign a charge type to a charge category and charge subcategory.

38


●

Indicate if the charge is a tax.

●  Specify if and how the system rounds a value.

●  Assign a default calculation base to the charge type so you do not need to

assign a calculation base each time you create a calculation sheet line item.

●

Indicate whether a charge type is a leading charge type and so must have a

value for the system to be able to calculate the charges.

●  Mark a charge type as inactive, so the system cannot use the charge type to

create any new calculation sheets or rate tables.

●  Specify the transportation mode category, which restricts the charge types in a

calculation sheet to those with the same transportation mode category as the

associated agreement, and to those with no specified transportation mode

category.

●  Enter a charge type description in multiple languages.

●  Specify other values used for air freight calculations or forwarding charges

calculation.

This figure shows how the charge type, charge category, and charge subcategory

influence the integration between SAP TM and SAP S/4 Sales & Distribution as well as

Materials Management.

Object Mapping of Charge Types in SAP S/4

The charge types, charge categories, and charge subcategories are mapped in SAP

S/4 to the following objects:

●  Pricing condition types in SAP Sales and Distribution used for customer billing.

●  Service activities in SAP Materials Management for carrier invoice processing.

39


40


Lesson 4 - Maintaining Rate Tables

## Rate Table Templates

This diagram shows where rate tables and rate table templates reside in the TCM

master data structure.

41


## Rate Tables

A rate table is a grouping of prices for transportation services. It is like a price list. The

prices (or rates) are listed by validity period in the rate table.

The rate table is a separate business object (/SCMTMS/TC_RATES) and can be used

in various calculation sheets to provide flexible maintenance.

You can maintain up to 14 dimensions in a rate table, however, we do not recommend

that you model charge management in that way.

There are many options to reduce the number of dimensions in a table. For example, a

rate table determination rule can be created to determine which rate table is to be

used for the current charge item.

You can define a rate table manually or automatically by using a rate table template

with predefined scales and validity dates. You can also maintain a large rate table, with

or without scale items, using Microsoft Excel.

42


## Rate Table Template Usage

You can use a rate table template to create a rate table with predefined scales,

calculation rules, and validity dates.

In the Define Rate Table Templates Customizing activity, you define rate table

templates to transport across different systems and use as templates for creating

rate tables.

To define rate table templates, in Customizing, choose Transportation

Management→Basic Functions→Charge Calculation→Basic

Settings→Templates→Define Rate Table Templates.

Master data templates can be created and used by users who have no authorization

to change customizing. In contrast to templates created in customizing, master data

templates cannot be transported across different systems. In the SAP Fiori

Launchpad Charge Management Worklist, master data and customizing templates

are depicted in their own queries.

43


The following transactions are available in SAP TM.

In the Customizing activity, you can do the following:

1.  Create a rate table template with the following required information:

●  Rate table template

●  Charge type or allow multiple charge types

●  Charge usage

●  Currency

2.  Create a rate table template scales with the following required information:

●  Dimension number (indicates the order of the input scales)

●  Scale template

●  Calculation base code

3.  Create a calculation rule with the following required information (optional -

used in the Validity table):

●  Calculation base

●  Unit of measure

●  Quantity

Similar information can be specified when creating a master data template. The main

difference is that if you create a master data template, you can also maintain scale

items and values for non-numeric scales.

44


## Rate Table Maintenance

A rate table is a grouping of prices for transportation services. It is like a price list. The

prices (or rates) are listed by validity period in the rate table.

The rate table is a separate business object (/SCMTMS/TC_RATES) and can be used

in various calculation sheets to provide flexible maintenance.

You can maintain up to 14 dimensions in a rate table, however, we do not recommend

that you model charge management in that way.

There are many options to reduce the number of dimensions in a table. For example, a

rate table determination rule can be created to determine which rate table is to be

used for the current charge item.

You can define a rate table manually or automatically by using a rate table template

with predefined scales and validity dates. You can also maintain a large rate table, with

or without scale items, using Microsoft Excel.

45


## Rate Table Definition Versus Maintain Rate Table

The figure depicts the basic structure of the rate table and some important fields

within each screen area.

## Rate Table Maintenance Transactions

The following transactions are available in SAP TM for maintaining rate table

information:

1.  Create Rate table Definition: In SAP Fiori Launchpad, choose Charge

Management→Create Rate Table Definition.

2.  Maintain Rate Table: In SAP Fiori Launchpad, choose Charge

Management→Maintain Rate Table.

1.  Note

In the Maintain Rate Table transaction, scale definition is not available.

These transactions enable different users to define rate table definitions and to

maintain rate information.

46


## Rate Table Structure

A rate table contains the following tab pages and screen areas.

General Data Tab Page:

## Description

The rate table identifier must be unique to avoid inconsistent rates.

Field

Rate

Table

## Charge

You can define the rate table to calculate transportation charges billable

## Usage

to your customer or to be billed to you by your carrier. A forwarding

agreement, freight agreement, and calculation sheet have the same

attribute for this distinction.

## Charge

The system only assigns rate tables to a charge item in a calculation

## Type

sheet if the charge type matches. You can use this field to search for a

rate table.

## The Scales Tab Page

You select prepared scales to determine the dimensions of the rate table and to create

a rate table based on these dimensions.

47


## Field

Description

## Dimension

You add each dimension on which you want your rate to be

defined and looked up. For example, if you want the rate to be

defined based on destination location and weight, add a

dimension for destination location and for weight.

## Scale

A scale defines the dimension of your rate table.

## Calculation

You can define the calculation base for the scale. The calculation

## Base

base is the actual base or the factor on which the charge

calculation happens.

## Minimum Value

If you select these checkboxes, you can maintain a minimum or

or Maximum

maximum value for the calculated rate. The system determines a

## Value

certain rate in the rate table and multiplies this rate based on the

calculation rule. Usually, the value of this multiplication result is

the final amount for this specific charge, which is the actual

amount equals the charge. If you set a minimum or maximum

value, the system checks if the calculated value is lower than the

minimum or greater than the maximum. If so, the minimum or

maximum value is charged.

Rel. Calc.

If you select this checkbox, you are defining whether you want the

## Method

system to apply a special calculation method, such as

(Relevant for

break-weight or clipping, to the rate table on the level of a charge

## Calculation

item. This charge item then only considers those rate tables that

Method)

you designated for such a special calculation method.

48


Dates and Values Tab Page

## Field

## Description

## Valid From and Valid

These fields define the validity period of the rate table.

To

## Rounding Profile

You define if and how the calculated amount or charge is

rounded.

## Calculation Rules Tab Page

Here you determine the values with which the single rate is to be multiplied. If there is

more than one charge calculation rule, the system multiplies the determined rate with

each of the given entries. You must select the Relative Scale Items Only checkbox for

at least one charge calculation rule if a relative scale is involved in the rate table

dimensions.

## Rate Values

You can maintain single rate values or upload and download complete Microsoft Excel

sheets. We recommend the following process flow:

1.  Create an empty rate table in SAP TM.

2.  Download this rate table from SAP TM to an xlsx file (default file type).

3.  Open this xlsx file with Microsoft Excel and maintain all the rates there.

4.  Save this xlsx file and upload it to SAP TM.

49


## Multiple Scales within a Rate Table

Master data maintenance in many organizations is a layered process, taking place at

different levels of abstraction. For example, when a logistics service provider (LSP)

starts operating in a new trade lane, it may offer some carrier-specific rates, as well as

some carrier-agnostic rates. Sometimes, LSP may have only incomplete rate data.

In such cases, business users upload generic rates where the actual scale values are

not available. For example, users may upload carrier-specific and carrier-agnostic

rates in the same rate table. If no specific rate for the carrier exists, the normal

business use is to pick up the carrier-agnostic rate.

The rate determinations in the examples in the figure are as follows:

●  Example 1:

 The rate is not specified for the destination zone or the carrier, so the rate is

determined from the generic entry for Zone 1.

●  Example 2:

 The rate is not specified for the carrier, so the rate is determined from the rate

table entry for the origin and destination zones.

50


●  Example 3:

 The rates are specified for each of the three scales in the table.

There may be multiple instances when rate-relevant information is missing, which

must be considered during charge calculation.

The No Value Allowed flag allows for the uploading of rates that are generic across

multiple dimensions. The No Value Allowed flag is given priority from the last

dimension scale to the first dimension scale of the rate table. The No Value Allowed

feature is available only for same-scale.

## Approval Workflow

In certain situations, new or changed rates must be approved by a Senior Rate

Administrator to become effective. An approval workflow can be activated for each

rate table type. Instead of releasing the rate table for usage, the rate administrator can

request an approval. The status of the rate table validity interval then switches to

"Awaiting Approval". Using SAP Business Workflow, an approval task is triggered and a

notification is sent to a manager. The manager receives an approval request. Once

51


approved, the validity interval will then be released and can be used. To use the

approval process, the organizational model must be maintained.

## Microsoft Excel Integration

You can maintain a large rate table, with or without scale items, using Microsoft Excel.

You can enter the rates and scales into a Microsoft Excel file and upload the file to

your SAP TM system.

Alternatively, you can define an empty reference rate table with validity periods in SAP

TM and download it to Microsoft Excel. You can then maintain the rate table in the

Microsoft Excel file and upload it to your SAP TM system.

## Download Options

You can download a rate table to Microsoft Excel in one of the following ways:

●  Rates for all validity periods in the rate table (scale ranges not included)

●  Rates for one validity period and selected scale ranges

52


●  Rates for multiple validity periods (scale ranges not included)

●  Rates of the current validity period with scale ranges

You can view non-numeric scale items in the downloaded Excel file.

You can choose to upload all the rates and scale items of a rate table from Microsoft

Excel to SAP TM.

The system provides you with a list of the created rate tables and also of those that

were not created successfully.

## Mass Creation of Rates Tables Using Microsoft Excel

You can create multiple rate tables in Microsoft Excel using rate table templates and

upload them to SAP TM. You use the mass creation of rate tables

(/SCMTMS/TCC_RATE_MASS_CREATE) report to download the Microsoft Excel

template, in which you enter the new rate table details, and then you upload the new

rate table details to SAP TM.

## Template Options

In the Microsoft Excel template, you can specify the following for each row in

Microsoft Excel:

●  The way you want the name of the rate tables to be generated, that is, by the

system, by using the rate table template name, or by using a rate table name

that you provide.

●  Whether you want to provide a rate table name. If you do so, you must enter the

rate table name in the rate table column. The system adds a number to the end

of the name of each rate table to avoid any duplication.

●  The rate table template on which to base the rate tables.

●  The rate table template to enable the system to create the rate tables. This

must be specified.

●  The quantity of rate tables. The system creates one rate table if you do not

enter a quantity.

53


The system provides you with a list of rate tables created, and also of those that were

not created successfully.

## SMC3 Integration for Rate Tables

In some use-cases, the integration of an external rate management system is

required. In the U.S., RateWare by SMC3 is often used to manage LTL rates according

to industry standards. Instead of replicating all rate information to the SAP TM

database (which requires significant ongoing maintenance effort), integrating the data

is advantageous. It is possible to combine the rates provided by RateWare with

additional or manual charges calculated in SAP TM: for example, LTL base rates from

SMC3, minimum charges, surcharges, and carrier-specific discounts in SAP TM.

The technical integration is done using Web-Services. SAP Note 1636870 describes

the configuration steps for technical integration.

In the SAP TM calculation sheet, a specific calculation method must be assigned to a

charge item to call the external system during charge calculation. For SMC3

integration, you can use the calculation method CALL_SMC3, which is part of the TM

standard. View cluster /SCMTMS/VC_SMC3 can be used for basic configuration

54


(detailed instructions are also contained in the SAP Note). In the same view cluster,

you can map SMC3 parameters to SAP TM calculation bases.

The External Ref. Number maintained in the TM Freight Agreement Header must

contain the SMC3 contract ID, if rates from a specific contract are to be calculated.

## Mass Maintenance of Rates

In this section, we look at several aspects of the mass maintenance of rates.

## Mass Maintenance: Updating Rates

●  A rate can be increased or decreased by a percentage or an amount.

●  You must specify a scale range, for example, source location, to enable the

system to change only the rates in a particular scale range.

Only scale ranges that are already specified in an existing validity period of an

existing rate can be specified.

●  Rates can be updated based on the calculation type of the scale items (for

example, absolute or relative, or both absolute and relative).

For example, you can update the rates for relative scale items with one rate

change and the rates for absolute scale items with a different rate change.

## Management of Validity Periods

●  Values for one period, multiple periods, or all periods in an existing validity

period can be changed.

●

If the validity period to be updated is not already specified in the existing validity

periods, you can create a new validity period in which the rate change applies.

○  Specify a new validity period within the date ranges already specified in

the existing validity periods.

○  Specify a new validity period that is outside the existing validity periods

in the rate table.

○  By default, the system uses the rate, calculation rule, and scale item

settings in the latest validity period when it creates the new validity

period.

55


○  For new validity periods, you can also automatically set the status to

Released during the rate table update.

## Integration of Mass Maintenance

●  Mass Maintenance is integrated in rate table maintenance.

●

●

Integration occurs into the master data cockpit query.

Integration is done using a batch report.

You can use the /SCMTMS/RATE_MASS_UPDATE program to change the values in a

single rate table or in multiple rate tables at the same time.

Rate tables for forwarding, freight, and internal agreements are accessible from the

master data cockpit query.

To access the master data cockpit, in the SAP Fiori Launchpad, choose Charge

Management→Charge Management-Worklist→Master Data Cockpit.

Choose the relevant agreement type query and enter your search criteria (Purchasing

Org and Carrier).

In the personal object worklist result, when you select a line item that contains both a

rate table and a calculation sheet, the system opens the Update Rates function when

you choose Update Rates/Calculation Sheet Amounts. The system automatically

includes the rate table from the selected line item in the update criteria when you open

the function.

When you select a line item that contains a rate table and a different line item that

contains a calculation sheet only, and choose Update Rates/Calculation Sheet

Amounts, the system opens both the Update Rates and Update Calculation Sheet

Amounts functions on the same screen.

56


## Mass Update of Rates - Example

An example of the mass update of rates is described here.

You want to create a new validity period that contains new rates.

The following table describes the settings in the first existing validity period of January

1, 2021 to December 31, 2021:

Rates Table

## Source Location

Destination Location  Value (USD)

NYC

NYC

NYC

PHI

CHI

SFO

100

120

340

57


You must create a new validity period with new rates to cover the period December 1,

2021 to December 31, 2021. The following table describes your inputs to the Update

Rates function:

Selection Criteria

Setting

## Attribute

New validity period setting

01.12.2021

from

New validity period setting to

31.12.2021

Source location

NYC

Destination location

PHI, CHI

Percentage

+10%

The system creates a new validity period for December 1, 2021 to December 31, 2021

with new rates. It keeps the old validity period for 2021, but changes the validity dates

to January 1, 2021 to November 1, 2021. The following tables describe the new

validity periods:

Validity 1: January 1, 2021 to November 1, 2021

## Source Location

Destination Location  Value (USD)

NYC

NYC

NYC

PHI

CHI

SFO

100

120

340

58


Validity 2: December 1, 2021 to December 31, 2021

## Source Location

Destination Location  Value (USD)

NYC

NYC

NYC

PHI

CHI

SFO

110

132

340

The system did not update the rate from NYC to SFO, since it was not included in the

selection criteria.

59


Lesson 5 - Defining Calculation Sheets

## Calculation Sheet Maintenance

The calculation sheet is a hierarchical table to calculate transportation charges. It

combines the charge types permitted for a document and the sequence in which the

system takes these charge types into account during the calculation.

The system uses the calculation sheet to specify which transportation charges to

calculate and how to calculate them. This helps to bill customers for transportation

services and to pay suppliers or carriers for subcontracted transportation services.

It provides for a calculation schema showing the steps and the specifications for the

charges. Based on the calculation sheet, the resulting charges, subtotals, and totals

can then be displayed in the documents.

## Calculation Sheet Data

When setting up the calculation sheet, you can specify the following:

## General data

The general data contains charge usage. Charge usage determines if the calculation

sheet is valid for the customer and/or service provider.

## Hierarchy items

Under the hierarchy items, you can specify the instruction, charge type, and

instructions on how the charge type should be calculated. This calculation schema

shows the steps and the specifications that the system takes into account during

calculation.

## Preconditions and general terms

Preconditions can be specified in the assignment of the calculation sheet to the

freight agreement. Such conditions for applying the calculation sheet, and payment

terms or other general terms, can be specified.

60


Calculation Sheet Item Components

61


The Items screen area contains the details of the calculation sheet items and you can

create rate tables for each calculation sheet item.

The following columns are mandatory in the Items screen area:

## Instruction Type

Sum: This is used to evaluate the total sum of all the lines under the sum line. The

charge item with the sum instruction evaluates the sum of all the lines below. Each

calculation sheet has an initial mandatory sum line. You cannot delete this line. You

can only maintain the rounding rule for this line because you cannot define a charge

type.

Subtotal: This is used to evaluate the subtotal amount of all lines included in a range

defined by a reference-from line and a reference-to line.

Standard: This is a standard line, as this charge item results in a direct charge when

the item refers to a charge type.

Compare High/Low Value: This evaluates the line to be considered for the calculation

among a set of two or more lines. This evaluation is based on the highest or the

lowest value of the affected lines. You use this value in combination with the

Operation attribute. This charge item triggers a comparison of other charge items. If

you set the operation to High, for example, the most expensive charge item remains

and the cheaper charge items are deactivated.

## Charge types

This is an itemized list of valid transportation charges. Charge types can be grouped

into categories or subcategories. During calculation, it can result in a positive

(surcharge) or negative (discount) value. If the charge item represents a percentage, it

must refer to another charge item or subtotal that produces an absolute value to

result in a chargeable amount.

Rate table details

62


Charge type instructions are sometimes called rate table details, consisting of the

specifications for how the charge type will be processed.

## Charge Type Details

The Rate Table/Charge Type details area contains the following important

information:

●  Rate

●  Basic Data

●  Classification

●  Preconditions

●  Notes

## Rate Tab

The Rate tab page of the Items screen area has the following important fields:

●  Amount: If you maintain this field, the charge item is not derived or calculated

but is always equal to this amount.

63


●  Currency/Percentage: You can enter eight, the currency code, or %.

●  Reference-From and Reference-To line numbers: If the calculated amount falls

outside the minimum or maximum amounts specified here, these values are

substituted.

●  Rate Table Determination Rule: This rule determines the rate table from which

the single charge item is derived using a condition or a BAdI.

●  Rate Table: The rate table is fixed and predefined for each charge item. The rate

calculation works in the same way as the rate table determination.

●  Calculation Rule: The value with which the single rate is to be multiplied.

●

Index Table: The index table is used, for example, to calculate the fuel

surcharge.

## Basic Data Tab

The Basic Data tab page of the Items screen area has the following important fields:

●  Charge Type: The types of transportation charges such as haulage, ocean

freight, and fuel surcharge.

●  Manual Charge Item: If you select this checkbox, the system does not calculate

the charges for this charge item, but instead expects you to enter an amount

manually.

●  External Calculation Flag: This specifies whether the system uses an external

charge engine, such as SMC3.

●  Logistical Data Specification: You can specify logistical data, such as stage

category, shipping type, or dangerous goods for which the charge type is to be

applied.

●  Resolution Base: This defines which logistical data is used to determine the

rate. Logistical data can be booking, container, main item, package, root (or

Header of the document), or document stage. You can also determine if a

grouping rule is to be used to group selected input data together, such as

stages. The group stage is then the basis for a new charge item, that is, this

rule is used together with the resolution base.

64


●  Rounding Profile: You define if and how the calculated amount or charge is

rounded.

Adjustment Profile: This allows you to change all involved calculation bases.

You use this profile, for example, to adjust the logistical weight by any factor or

logic. That is, you adjust the gross weight in such a way that the system only

considers the chargeable weight for the rate table access

●  Dimensional Weight Profile: If the charge type is relevant for dimensional weight

calculation, a specification of dimensional factor, such as Imperial cubic pound

factor 166 or 194, is applicable. Metric factors can also be specified.

●  Calculation Method Type and Calculation Method: You can enable a special

calculation method for each charge item, for example, whether the system

calculates the charges by considering the break-weight or not.

## Classification Tab

The Classification tab page has the following important fields:

●  Mandatory: You use this field in preconditions and for checks based on

Business Add-Ins (BAdIs). If the system cannot calculate the charge item

properly, it creates a warning message. If the system cannot calculate a

mandatory charge item, it creates an error message during invoice creation

before transferring it to SAP S/4 MM.

●  Tax: Indicates that the charge is a tax.

●  Statistical Charge: The charge is informational or statistical only and not to be

charged to the customer.

## Preconditions and Notes Tab

The Preconditions tab page has the following important field:

●  The Preconditions tab contains the Precondition rule field. The precondition rule

checks if certain charge items are to be processed before charge calculation,

according to the given logistical data source.

●  On the Notes tab page, notes can be added, distinguished by text type.

65


## Resolution Base

During charge calculation, the system determines the calculation resolution base by

the origin of the data upon which the charge aspect is based.

## Charge Aspect Definition for Resolution Base

You can define the charge aspect in the following resolution base objects:

●  Root: This is the header of the document, such as freight order, booking order,

or forwarding order.

●  Stage: Refers to utilizing stage attributes, such as distance between the shipper

location and the port of loading.

●  Container: If an attribute is stored on container level (for example, the

Equipment Type: 22GP, 42G0.) is required for charge calculation, resolution

base CONTAINER should be used (otherwise, this information is not available

for charge calculation).

●  Product: When product attributes like product quantity, weight, or volume must

be used.

For example, you want to determine the freight rate based on the gross weight of the

order. To do this, you must use the calculation resolution base of the root. However, if

you want to calculate the freight on a prepackage basis, the calculation resolution

base should be package.

66


Lesson 6 - Creating Freight Agreements

## Agreements Overview

Agreements are the basis for calculating transportation charges and can involve one

or more parties.

You use forwarding agreements (FWAs) to calculate transportation charges billable to

your customer, and freight agreements (FAs) to calculate transportation charges

billable to you by your carrier.

You use internal agreements (IAs) to calculate transportation charges between

organizations of the same company code and between organizations of different

company codes in the same company.

A service agreement is a type of freight agreement, which contains only service types

or service products.

Agreement Overview

67


Organizational Units in SAP Transportation Management (TM)

Organizational units are used to determine responsibilities, for example, for approval

processes, and authorization of who is allowed to see data or perform certain actions.

68


In SAP Transportation Management (TM), organizational units can be divided into

sales and purchasing, and planning and execution.

Forwarding houses can be used to represent business units (LSP), and perform all

functions including sales, purchasing, planning, and execution.

## Organizations and Business Documents

The sales side is responsible for sales and services, such as organizing the necessary

activities for shipment transportation. For this reason, the sales organization is

indicated in the business documents forwarding documents, order-based

transportation requirements, delivery-based transport requirements, and forwarding

settlement documents.

The purchasing side is responsible for procuring the necessary services from vendors

(for example, carriers). For this reason, the purchasing organization is indicated in the

business documents freight orders, freight bookings, service orders, and freight

settlement documents (FSD).

## Contractual Data in Agreements

An agreement includes contractual data, such as the following:

●  Organizational unit (for example, the sales or purchasing organization)

●

Involved parties (for example, the ordering party or carrier)

69


●  Terms of payment

●  Validity dates

The system determines the agreement based on organization, business partner,

validity period, and preconditions. An agreement is most commonly determined by the

purchasing organization and business partner (carrier for freight agreements,

customer for forwarding agreements). In the Freight Agreement Type Customizing

activity, you can configure whether one or multiple partners can be entered in the

agreement; that is, if you have one freight agreement with a carrier valid for multiple

purchasing organizations.

Also, there is the possibility of selecting agreements manually:

Therefore, the agreement determination type of the calculation profile has to be set to

'Display All Agreements' (Unit 3, Lesson 2).

Forwarding and Freight Agreement Customizing Considerations

A forwarding agreement is a long-term contract that represents the contractual

relationship with a customer to whom you are selling transportation services.

70


A freight agreement is a long-term contract that represents the contractual

relationship with a carrier from whom you are buying transportation services.

When configuring agreements, it is necessary to examine the logistical model.

Purchasing organizations, business partners such as customers and carriers, as well

as business rules, such as plan or actual ship date, have a direct impact on how

agreements are maintained.

The standard determination rule for freight agreements uses purchasing organization

and carrier; for forwarding agreements, the standard determination rules use sales

organization and customer.

For complex determination rules, a BRF+ condition can be created. This allows

rule-based determination based on more fields.

Customizing Agreements–Agreement Types

The allowed item types are:

●  Preconditions that can be defined in the agreement, such as transportation

mode or service level

●  Text schema used to store freight agreement notes

●  Default calculation sheet template used when creating the calculation sheet

from within the agreement

●  Direct shipment order scheduling type

●  Display time determination type is used to specify if the time display can be

editable or display only

●  External delivery date determination rule if other system besides TM is used for

the delivery date determination

●  Multiple parties allowed

●  Departure, transit, and arrival calendar

●  Allocation type the system uses to create transportation allocation

●  Setting to enable Change Document tab page or screen area

71


72


Unit 3 - Calculating Charges

Lesson 1 - Configuring Charge Calculation

## Calculation and Charges Profiles

The calculation profile function provides a central location to define the settings that

you want the system to use when calculating transportation charges.

The following are examples of settings that you can define in a calculation profile:

●  Specify the date type that the system uses as the basis for the rate, exchange

rate, and agreement validity, and ultimately the charge calculation. (For

example, the order date, the invoice date, or the expected end date of the main

carriage.)

●  Specify the level at which the system calculates the charges, for example, at

header level, item level, or stage level.

●  Specify the determination rule that the system uses to determine the

agreement and the calculation sheet.

73


●  Specify a single rate, known as a through rate, for multiple stages of a

transportation route.

●  Specify the default dimensional weight profile for the organizational unit and

the condition that the system uses to determine the dimensional weight profile.

●  Specify the source of the data that the system uses for charge calculation and

invoicing, for example, actual route, ordered route, or actual and ordered route.

In the Define Calculation Profiles Customizing activity, you define the settings that you

want the system to use when calculating transportation charges.

In Customizing, choose Transportation Management→Basic Functions→Charge

Calculation→Basic Settings→Define Calculation Profiles.

## Charges Profile

You can enable charge calculation for a purchasing organization by assigning a

Charges Profile to the Purchasing Organization (see the PPOCE transaction). The

charges profile groups together the general settings for charge calculation, such as

the calculation profile you want the system to use when calculating transportation

charges, as well as the freight settlement profile for settling your charges, the cost

distribution profile, and the local currency of your business documents.

74


## Calculation Profile Assignment

You can create a charges profile in the Customizing activity Define Charges Profile.

Here you can assign your calculation profile, which then gets automatically assigned

to the organizational unit to which the charges profile gets assigned.

In Customizing, choose Transportation Management→Basic Functions→Charge

Calculation→Basic Settings→Define Charges Profiles.

A purchasing calculation profile for your purchasing organization has to be maintained

for charge calculation on the freight/buying side (freight order and freight booking).

If the organization is a forwarding house, both sales and purchase calculation profiles

have to be maintained. The same profile can be used for both sales and purchase,

depending on the scenario.

You can also assign a calculation profile to the following business partner roles:

●  Sold-to party

●  Ship-to party

●  Carrier

●  Vendor

75


To assign a calculation profile to business partner roles, in SAP Fiori Launchpad,

choose Master Data→Define Business Partner. You can assign a calculation profile on

the Vendor/ Transportation Purch. Org. Data tab page of the business partner role. You

can also use the BP transaction.

## Note

If you assign a calculation profile to an organizational unit and to a business partner

role, the system only applies the calculation profile you assigned to the business

partner role. You can also assign a calculation profile only to the organizational unit,

but you cannot assign a calculation profile only to a business partner.

## Calculation Settings in Freight Order Types

In the Customizing activity Define Freight Order Types, the following settings influence

charge calculation:

Enable Charge Calculation: This must be selected to enable the system to calculate the

charges. This setting does not influence manual freight charges, as they can be

entered even when this setting is not selected. Also, the system also allows the

quoted price of awarded freight quotations to be updated.

Calculate Charge After Each Save: When this save strategy is selected, the system

performs the charge calculation after each save. If a mandatory charge type cannot

be determined or is missing, the freight order cannot be saved.

76


In the freight order, additional settings, such as Track Changes and Default Charges

View (ungrouped/ grouped view), can be maintained.

To define freight order types, in Customizing, choose Transportation

Management→Freight Order Management→Freight Order→Define Freight Order Types.

Note: The described settings can also be applied in freight booking types and service

order types.

77


Lesson  2  -  Determining  Agreements  and  Charge  Calculation
## Rules

## Freight Order Charge Calculation

During freight charge calculation in the freight order, the following steps occur:

1.  The data is collected from the following SAP TM core objects:

●  Transaction business object: freight order, freight booking, service order,

stage, item, container

●  Configuration objects

●  BRF+ conditions

●  Master data

●  Any BAdI implementation

2.  The freight agreement is determined.

3.  The values of each charge type in the calculation sheet are calculated.

4.  The log file of the calculation run is held, and so on.

5.  The calculated results are shown in the freight order.

78


## Freight Rate Derivation Process

During the freight rating process, the following steps are performed:

1.  Based on the calculation sheet line item, the system determines the calculation

base and the rate table.

2.  Given the dimension of the rate table (scales), it then obtains the logistical data.

3.  Given the calculation profile, the system determines the baseline for the

calculation date determination.

4.  The system obtains the matching rate table record and then determines the

appropriate calculation rule.

5.  The system calculates the freight rate amount.

Transportation Zone Derivation Using Zone Hierarchy

79


The derivation of the transportation zone is flexible. It is not essential to maintain rates

for all values - they can be maintained at the appropriate level.

The system retrieves the rate by going up in the hierarchy level until it finds the rate.

## Maintain Preconditions in Agreement Items

In an agreement, there are two ways of using preconditions for the agreement items

(calculation sheets):

●  Built-in preconditions

●  BRFplus preconditions

It is possible to define a BRFplus condition or a BAdI to check if a certain calculation

sheet is to be processed in a certain business context. The result of this rule is a true

or false decision. If the response from BRFplus or the BAdI is true, the calculation

sheet is considered for charge calculation. Some built-in preconditions are available

on agreement item level.

80


Types of Built-in Preconditions in Agreement Items

Built-in preconditions in agreement items are as follows:

●  Trade Lanes:

 These are based on criteria such as source location, source zone, destination

location, destination zone, mode of transport, or means of transport. The

agreement item can be activated or deactivated.

●  Partners:

 Based on the business partner, an agreement item can be activated or

deactivated.

●

Item Precondition:

 Based on up to seven predefined conditions, it is possible to activate or

deactivate an agreement item.

## Available Item Preconditions

The table lists the available item preconditions and their descriptions.

Available Item Preconditions

Precondition

Description

81


## CONSL_TYPE

Allows selection of a certain Air Waybill Type

## CONT_BASIS

Allows selection of a certain Contract Basis

MOT

Allows selection of a certain Transportation

## Mode

## MOVEM_TYPE

Allows selection of a certain Movement Type

## SERVICE_LV

Allows selection of a certain Service Level

## SHIPMENT

Allows selection of a certain Shipping Type

## STAGE_CAT

Allows selection of a certain Stage Category

## BRFplus Preconditions in Agreement Items

●  Certain items (calculation sheets) in the agreement can be set to true or false

based on parameters that are flexibly defined in the condition or a BAdI.

●  The condition (condition type TCM_PRECON) is assigned to the agreement

item.

●  You maintain the condition in the Precondition Rule field of the Precondition

Tab in the Agreement Item details section.

82


## Maintain Preconditions in Calculation Sheets

There are two ways of using conditions in the calculation sheet. There are predefined

parameters in the built-in preconditions that can be used or a BRF+ precondition/BAdI

can be maintained as well.

Types of Built-in Preconditions in Calculation Sheets

●  Trade Lanes: Based on criteria such as source location, source zone,

destination location, destination zone, mode of transport, or means of

transport, the charge line can be activated or deactivated.

●  Service: Based on the service level, a charge item can be activated or

deactivated.

●  Business Partner: Based on the business partner, a charge item can be

activated or deactivated.

## BRFplus Preconditions in Calculation Sheets

A BRFplus condition, or a BAdI, can be defined to check if a certain calculation sheet

item is to be processed in a certain business context. The result of this rule is a

true/false decision. If the response from BRFplus or the BAdI is true, the calculation

sheet item is considered for charge calculation.

83


The precondition for the charge item can be maintained on charge item level in the

Precondition tab.

## Agreement Determination

Freight agreements (FAs) and forwarding agreements (FWAs) are the basis for

calculating transportation charges. In this section, we look at how agreements are

determined.

## Agreement Determination Based on Priority

●  The system determines the agreement based on organization, business

partner, validity period, and preconditions.

●

If there are several matching agreements, which can be determined on the data

from the freight order/booking or from the forwarding order, it is possible to

have a leading charge type (defined in charge type Customizing), and the first

agreement where the defined leading charge type can be calculated is picked.

Besides using leading charge types, it is possible to maintain priorities.

●

If the system finds multiple matching agreements during agreement

determination, the agreement priority defines the sequence in which the

subsequent determination is executed.

●  The agreement priority can be maintained on the General Data tab in the details

section.

## Agreement Determination and Selection Types

Often logistics service providers (LSPs) have multiple freight agreements (FAs) with

the same carriers and purchasing organizations. This is because a LSP can strike

deals with carriers at various levels, for example, on a country, regional, and global

basis.

Normally, the larger the contract, the better the rates. However, if a country Business

Partner (BP) is pushing a lane to increase market share, then the LSP could potentially

84


get better rates. Therefore, it makes sense to have a different contract with the

country BP, or even multiple contracts.

Similar scenarios can exist on the customer side. Therefore, the ability to choose a

particular context in a given scenario is a critical business requirement on both the

buying and selling side.

## Manual Agreement Selection: Functions

●  An enhancement to the standard agreement selection, which is an automated

process.

●  Provides the capability to select an agreement or agreement item for charge

calculation.

●  Offers extra capability for automatic selection of minimum or maximum

agreement items through calculation profile control setting.

## Multiple Agreements Pop-up

The figure shows the Multiple Agreements dialog box, which can be used to select an

agreement manually.

## Note

The Multiple Agreement pop-up is not supported for through rates.

85


## Agreement Determination Type

## Manual Agreement Selection: Example Scenarios

Customizing activity for Transportation Management occurs in Transportation

Management→Basic Functions→Charge Calculation→Basic Settings→Define

Calculation Profiles.

If you enter Minimum Charges, the system finds the final amounts for all the

agreement items and chooses the agreement item with the minimum final amount for

charge calculation.

86


If you enter Maximum Charges, the system finds the final amounts for all the

agreement items and chooses the agreement item with the maximum final amount

for charge calculation.

If you enter Determine All Agreements, the system displays all the relevant agreements

and agreement items for each charge item. You can then select an agreement or

agreement item for each charge item, for charge calculation.

If you do not enter any value, the system does not consider the agreement

determination type for charge calculation and follows the standard agreement

determination process.

## Charge Calculation Rules

It is possible to define charge calculation rules to determine the right agreement. The

standard determination logic based on purchasing organization, validity, and business

partner is ignored and the logic of the condition, based on a certain business context

maintained in the conditions, is used.

Condition Types for Agreement Determination

●  TCM_FAGDET - Freight Agreement Determination

●  TCM_FAGDEX - Freight Agreement Exclusion

87


TCM_FAGDET - Freight Agreement Determination Standalone

●  The determination condition is assigned to a charge calculation rule

(Agreement Determination Rules–Standalone) in the SAP Easy Access Screen.

●

In the SAP Easy Access Screen, choose Logistics→Transportation

Management→Master Data→Maintain Charge Calculation Conditions.

●

If you select the Std Determ. checkbox, the system uses the standard

determination logic when the condition execution fails or returns no result.

## TCM_FAGDEX - Freight Agreement Exclusion

●  The system can check both the condition and the BAdI option to see if an

automatically determined agreement has to be considered for the given

business context.

●  The system checks the list of automatically determined agreements one by

one to determine if they are still applicable. If more than one agreement

remains after the system has applied the exclusion rule, the system considers

the agreement priority.

●  This charge calculation rule can be embedded in the calculation profile for the

determination condition. The exclusion condition can be maintained directly in

the agreement in the General Data→Details section.

●  Once the exclusion condition is embedded in the agreement, the system can

check that condition to see if an automatically determined agreement has to be

considered for the given business context.

## Further Charge Calculation Rules

Besides the described Agreement Determination, Charge Calculation Rules can be

used also for the following activities:

88


●  You can define rules for calculation sheet determination

Standalone: You have switched off standard determination, and instead, the

system executes a condition that determines the calculation sheet. If you

select the Std Determ. checkbox, the system uses the standard determination

logic if the condition execution fails or returns no result.

●  You can define a precondition rule for the calculation sheet and calculation

sheet item

You define a BRFplus condition or a BAdI to check if a certain calculation sheet

or calculation sheet item is to be processed in a certain business context. The

result of this rule is a true/false decision, that is, if the response from BRFplus

or the BAdI is true, the calculation sheet or calculation sheet item is considered

for charge calculation. For more information, see the Precondition tab page in

the Items screen area of the agreement or calculation sheet.

●  You can define grouping rules for resolution bases. You have the following

options:

○  Condition: The system can dynamically determine the attribute or field

by which the data source is to be grouped. Both options, the direct

grouping and the dynamic BRFplus-based attribute determination, work

in the same way–the data source currently being processed (for

example, all shipment items) is sorted by this specific attribute. The

system then groups all items with the same attribute value and later

handles them as one item.

○  Group By: If you know the calculation base by which the data source is

to be grouped and this value is static, you can enter the calculation base

directly. The system then groups all items with the same attribute value

and later handles them as one item when looking up the rate table.

●  You can define rate table determination rules

○  Condition: The flexible, rule-based determination of a specific rate table.

To configure this determination, the complete logistical data source is

available. Only a valid rate table is expected as the return parameter.

○  Determin. By BAdI (Rate Table Determination Using BAdI): The rate table

determination is coded inside the BAdI.

89


●  You can define the rules for charge calculation by a formula

○  The system calculates the charge item without the normal rate table

access. That is, either the BAdI or BRFplus directly returns the calculated

amount for this charge item.

○

If you decide to calculate the charge item through BRFplus, you can use

a mathematical formula or any other BRFplus option. In this case, no

information is available in the Calculation Base area.

## Freight Order Charge Estimations

In SAP Fiori Launchpad, you can perform carrier selection and estimate the charges

for a freight order with only a minimal amount of logistical data.

You must provide the following data to estimate the charges:

●  Origin

●  Destination

●  Purchasing Organization

●  Carrier

●  From and To dates (Carrier Selection): the user receives a ranking of carriers

based on total cost

●

## Item

To estimate the charges, in SAP Fiori Launchpad, choose Freight Order

Management→Estimate Freight Charges.

90


Lesson 3 - Understanding Special Charges

## Wildcard Search

A shipper often has freight rate agreements with carriers based on ZIP codes, ZIP

code areas (often two or three-digit ZIP codes), or transportation zones.

Zone and ZIP Code (Wildcard Modeling) for Rate Search

●  To minimize maintenance, a shipper can use a partial character set and

wildcards in the rate table, instead of defining transportation zones. For

example, the rate for postal code 12345 can be maintained as the rate for code

123*.

●  During charge calculation, the system picks up the postal code that has the

greatest string match with the postal code coming from the document.

For example, for postal code 65192:

○  Rate 1: 65* = 20 USD

○  Rate 2: 651* = 25 USD

○

In this case, rate 2 is picked up because it has the greatest string match.

91


## Rate Lookup by Transportation Zone

In SAP TM, the same location is mapped to multiple transportation zones. For

example, Hamburg is mapped to two transportation zones: Germany zone (for

example, for sourcing) and Hamburg zone (for example, for marketing).

The rate agreement is set up so that rates are provided for a location-to-zone

transportation or even a zone-to-zone transportation (since it can be cumbersome to

maintain multiple location-to-location rates). The system picks up a rate from the rate

table and performs charge calculation in such scenarios.

The system carries out multiple comparisons until it finds a record in the rate table

that matches the scale item. The engine first compares the Germany zone with the

rate maintained. It finds none, so it searches with the Hamburg zone, finds a rate, and

returns that rate. The engine always sends the first rate that it encounters. It does not

set any priority to the rates.

92


## Charge Item at Header and Stage Level

There are business scenarios that use stage-level charge calculation where some of

the charges are not stage-specific. Stage-level calculation is commonly used in freight

forwarding scenarios where charges applicable to a stage are mapped to a respective

calculation sheet. However, some of the charges can be stage-independent and apply

for one of the business partners.

These stage-independent charges are applicable to a business partner only and

cannot be assigned to a particular stage. For example, unloading fees cannot be

assigned to one stage, so are applicable to a business partner.

To fulfill this requirement, a "mixed" calculation level can be used. The mixed

calculation level is not a new calculation level, rather a contextual new behavior.

The system can calculate charges for an agreement item at header level, even when

calculating the rest of the charges at stage level. During charge calculation, the

system calculates the header-level charges independently of the stage charges. The

system calculates the stage charges as usual. To enable header-level charges when

calculating charges at stage level, you must maintain a calculation profile with the

calculation level as stage level.

93


For example, in a Free On Board (FOB) incoterm scenario, the consignee is responsible

for the security charges across the main and on-carriage. Therefore, instead of

mapping such charges to one of the stage-relevant calculation sheets, these can be

defined as header-level charges in a separate calculation sheet.

## Charge Calculation with Through Rates

To maintain rates that cover multiple stages of a transportation route, "through" rates

can be maintained. If a through rate is available for the entire transportation route or

part of the transportation route in an order, this rate can be applied during charge

calculation, depending on the customizing setting.

In a freight order with multiple stages and different carriers per stage, the through rate

calculation is carrier-dependent. Through rates can be maintained across stage

categories without overlap.

In the figure, the shipper negotiates a Door-Port (A to B and B to C) rate, including the

carrier’s haulage costs with Carrier 1. The on-carriage stage (C to D) is contracted to

another carrier (Carrier 2) on the import side.

The system finds a through rate for stage A-C for Carrier 1 and a rate for stage C-D for

Carrier 2.

## Note

You must enable the through rate functionality in the calculation profile to use it.

94


## Fuel Surcharge Calculation Method

Due to uncertainties in fuel prices, it is significant to charge the customer

appropriately based on the fuel surcharge index, published by the government

(common in North America) and/or by logistics service providers, also called Diesel

floater. As a logistics service provider or carrier, you must recover the additional

charges incurred due to varying fuel costs. Transportation Management simplifies the

fuel surcharge calculation by providing an easy-to-maintain fuel surcharge calculation

method. Two different methods exist for this purpose: Model 1 and Model 2.

Fuel Surcharge Calculation: Model 1

You can calculate the fuel surcharge based on an index value (fuel surcharge value).

The index value (fuel surcharge value) is defined in an index rate table (for example,

based on the calculation date and/or source location). The fuel surcharge value is the

used to retrieve the rate from a standard rate table. Based on this rate, the final

amount gets calculated.

95


Configuration Steps:

1.  Define an index base rate table

Define an index rate table with the calculation base such as calculation date

and source location. You can also maintain a calculation rule in this index rate

table.

2.  Define a standard rate table

Define a standard rate table with a calculation base as FSC and scale type as

either Base Scale or To Scale. Define the rates for the fuel surcharge values

from the index rate table.

3.  Define a calculation sheet with a charge item for fuel surcharge and define the

following attributes:

a.  Enter the charge type as Fuel.

b.  Enter the index rate table in the Index Rate Table field.

c.  Enter the standard rate table in the Rate Table field.

d.  Enter the calculation method type as C and calculation method as

FUEL_SURCHARGE on the Basic Data tab page.

Fuel Surcharge Calculation: Model 2

You can calculate the fuel surcharge based on a base fuel surcharge value. The

logistic service provider or carrier agrees with the customer on an index base date

based on which the system determines the base fuel surcharge value. The actual fuel

surcharge is calculated based on the current fuel surcharge value and base fuel

surcharge value.

Configuration Steps:

To calculate the fuel surcharge, you define an index base rate table with the fuel

surcharge values for specific calculation dates or validities. Optionally, you can define

a standard rate table with the fuel surcharge values for scale items such as location

and calculation dates or validity periods:

1.  Define an index base rate table

Define an index rate table with the calculation base as Calculation Date, scale

96


type as To Scale or Base Scale, and the value type as Absolute or Percentage.

Note that you must not maintain a calculation rule in this rate table.

2.  Optionally, define a standard rate table

Define a standard rate table with a calculation base and scale type as either

Base Scale or To Scale. Define the fuel surcharge values for scale items such

as source location and destination location.

1.  Note

If you don’t define a standard rate table, the system determines the fuel

surcharge using the base rate specified in the calculation sheet.

2.  Define a calculation sheet with a charge item for fuel surcharge and define the

following attributes:

a.  Enter the charge type as Fuel.

b.  Enter the index rate table in the Index Rate Table field.

c.  Enter an index base date in the Index Base Date field.

d.  If you’ve defined a standard rate table, enter it in the Rate Table field.

Otherwise, you must enter a rate in the Base Rate field as a percentage

or absolute value.

e.  Enter the calculation method type as C and calculation method as

FUEL_SURCHARGE on the Basic Data tab page.

Calculation Example

97


98


As the figure shows:

You maintained an index rate table with scale type as From Scale.

The calculation sheet has a base rate of 1.19 % and the index base date set to

07.28.2021.

You have a calculation profile with the calculation date type as Order Date and in the

freight order, the order date is 08.25.2021.

The system determines the current fuel surcharge using the order date. The order

date 08.25.2021 occurs later than 08.20.2021 in the index rate table. Hence, the value

3.82 is determined as the current fuel surcharge value.

The system determines the base fuel surcharge using the index base date of

07.28.2021. The index base date 07.28.2021 occurs later than 07.22.2021 in the index

rate table. Hence, the value 3.65 is determined as the base fuel surcharge value.

The fuel surcharge is calculated as follows:

Fuel surcharge in percentage = (Current fuel surcharge value/ Base fuel surcharge

value)* Base rate in calculation sheet

Fuel surcharge in percentage = (3.82/ 3.65)*1.19 = 1.25 %

## Optional: Standard Rate Table

Once the system determines the current fuel surcharge value and the index fuel

surcharge value as previously mentioned, the system determines the fuel surcharge

value for the source location and destination location specified in the freight order. In

the freight order, the source location B and the destination location C are maintained.

The system determines the fuel surcharge value of 3.15 from the standard rate table.

The fuel surcharge is calculated as follows:

Fuel surcharge in percentage = (Current fuel surcharge value/Base fuel surcharge value)*

Fuel surcharge value from standard rate table

99


Fuel surcharge in percentage = (3.82/ 3.65)*3.15 = 3.30 %

## Calculation Methods

Calculation methods enable the system to calculate transportation charges according

to a specific logic, for example, by considering the break-weight or the deficit weight.

You specify a calculation method for each charge type when defining a calculation

sheet. The system applies the calculation method when calculating the charges for

the charge type.

Calculation method types can also help to use customer-specific logic or special

formula for freight charge calculation.

To define calculation methods in Customizing, go to Transportation

Management→Basic Functions→Charge Calculation→Enhancements to Charge

Calculation Engine→Define Calculation Methods.

Clipping is another calculation method offered inside the TM system. Calculation

methods enable the system to calculate transportation charges according to a

specific logic, for example, by considering the break-weight, fuel surcharge or clipping.

Calculation methods are specified for each charge type when defining a calculation

sheet. The system applies the calculation method when calculating the charges for

the charge type.

For creating or editing of a calculation sheet, in the SAP Fiori launchpad, go to Charge

Management→Create/Edit Calculation Sheet.

On the Basic Data tab of for example, the charge line for the charge type BASE, enter

Clipping as your calculation method type.

## Clipping Example

You define a rate table for your BASE charge line and assign it in the calculation sheet.

With the Clipping calculation method enabled, the system calculates the

transportation charges by working through all scales level-by-level, even if the value

100


lies outside the scale. The system then totals up the calculation results from each

scale level to produce the overall result. For clipping, one scale item must have a

relative calculation type.

The scale levels are defined with the following values:

●  Up to 5 tons: USD 50 absolute

●  Up to 7 tons: USD 14 per ton

●  Up to 10 tons: USD 13 per ton

●  Up to 15 tons: USD 12 per ton

Using the clipping calculation method for a load weighing 12 tons, the system

calculates the transportation charges as follows:

●  5 tons at USD 50 = USD 50 (first scale level)

●  2 tons at USD 14 per ton = USD 28 (up to the second scale level)

●  3 tons at USD 13 per ton = USD 39 (up to the third scale level)

●  2 tons at USD 12 per ton = USD 24 (remainder in the fourth scale level)

This results in a charge of USD 141. If you don’t use the clipping calculation method,

the 12 tons fall into the "up to 15 tons" scale level and the transportation charge is

USD 12 per ton, resulting in a charge of USD 144.

101


## Calculation Method Type Example: Break Weight

A calculation method, such as the break-weight calculation, uses special functions to

derive the rate. When a break-weight calculation is specified in the calculation sheet,

the system compares the next rate to the current rate and applies the cheaper rate.

Other calculation methods common in the transportation industry include clipping,

deficit weight rating, most expensive main carriage, internal charge calculation, and

external systems.

Calculation method types can also help to use customer-specific logic or special

formula for freight charge calculation.

## Events

SAP Event Management (SAP EM) and SAP Global Track and Trace (SAP GTT) in

combination with SAP Transportation Management (SAP TM), offers visibility

scenarios for tracking and tracing freight orders, freight bookings, and freight units.

For each of those documents, expected and unexpected events can be reported either

via TM directly or via Event Management. An expected event is a predefined process

milestone and an unexpected event describes an event that is not foreseen to happen

in the process.

102


## Event Types

The visibility scenario for EM-TM offers standard events that can be used. According

to rules based on, for example, the departure date and loading duration, a planned

date is assigned to Loading Begin, Loading End, and Departure events. This date

defines the time stamp at which this event or process milestone is expected to be

reported. The time stamp, at which the event is reported, defines the actual date. This

means that it is possible to have the following:

●  Regular events (reported in a predefined time frame)

●  Early events (reported before predefined time frame)

●  Late events (reported after predefined time frame)

●  Unreported events (not yet reported)

An unexpected delay or event is caused by a traffic jam or an accident. Unexpected

events do not have a planned date, as they are not foreseen to happen. These events

have an actual date that can be linked to a certain expected event. For example, a

traffic jam, with an estimated delay of two hours, influences the arrival date at the

customer and therefore is linked to the arrival date.

Events can be propagated back to other documents using the document flow. For

example, when reporting the unloading start of the freight order, the event can be

103


propagated back to the assigned freight unit so that the unloading start of the freight

order also creates the unloading start of the freight unit.

## Event-Based Charges

Events can influence how the carrier is paid (via the freight order and freight booking).

## Calculation of Charges Based on Delay

Charges based on the calculated delay for a specific event are calculated in the

following way:

Delay = Actual Date/Time–Planned Date/Time (or Estimated Date/Time) –

## Grace Days

●  The Actual Date/Time comes from SAP EM when a specific event is reported.

●  The Planned Date/Time comes from SAP EM and defines the expected

date/time.

●  The Estimated Date/Time is used when there is no integration with SAP EM. In

this case, an event is created in SAP TM directly with no planned date or time.

The estimated date/time entered when the event is created in SAP TM is used.

●  Grace Days, or Free Days, can be defined in charge management master data.

Charges can be calculated within the freight order and/or freight booking based on the

number of days of the delay.

## Event-Based Charge Customization

To use event-based charges, settings must be configured in Customizing.

Required Customizing Settings for Event-Based Charges

●  Definition of Calculation Bases: ACTUAL_DATE, DELAY, ESTD_DATE,

GRACE_DAYS, PLANNED_DATE

●  Event Profile

●  Assignment of Event Profile to Business Document

104


## Step 1: Definition of Calculation Bases

Five calculation bases are used during charge calculation to retrieve the dates and

times of events, and to calculate the delay that is relevant for the charge calculation.

The calculation bases are defined in the following Customizing location:

In Customizing, choose Transportation Management→Basic Functions→Charge

Calculation→Data Source Binding→Define Calculation Bases.

The ACTUAL_DATE, ESTD_DATE, and PLANNED_DATE are customized so that dates

and times can be pulled into a charge calculation. This data is derived from SAP Event

Management and predefined helper classes are assigned to the calculation bases.

DELAY and GRACE_DAYS data are not derived from Event Management into charge

calculation, but are necessary to calculate the exact delay. To determine the dates and

times, a predefined helper class is assigned.

Required Field Assignments and Helper Classes for Calculation Bases

Calculation Base

Field Assignment

Helper Class

ACTUAL_DATE

## ACTUAL_DATE

/SCMTMS/CL_TCC_CB_CONV_TS

## ESTD_DATE

## ESTIMATED_DATE

/SCMTMS/CL_TCC_CB_CONV_TS

PLANNED_DATE

## EXP_END_DATE

/SCMTMS/CL_TCC_CB_CONV_TS

## DELAY

GRACE_DAYS

—

—

/SCMTMS/CL_TCC_CB_DELAY

/SCMTMS/CL_TCC_CB_REL_CBASE

The number of days for the DELAY is influenced by the GRACE_DAYS. This means that

for the calculation base DELAY, the related calculation base GRACE_DAYS must be

maintained.

105


In the calculation base Customizing for DELAY, the related calculation base can be

maintained by choosing Related Calculation Base in the Dialog Structure. This setting

influences the calculation sheet in which the number of grace days is entered.

## Step 2: Event Profile

The event profile triggers the event-based charge calculation and can be maintained in

Customizing.

In Customizing, choose Transportation Management→Basic Functions→Charge

Calculation→Basic Settings→Define Event Profiles.

## Event Profile Attributes

Within the event profile, the following attributes can be set up:

●  Charge Type: used for event-based charging. This is the charge type used in the

calculation sheet.

●  Event, Event Reason, and Event Status: To calculate a delay, define the event on

which the charge is based. As there are several events, each one could

potentially have different delays. As a result, this delay calculation has to be

based on a specific event and, if needed, an event reason. The Event Status

defines the type of event.

●  Referenced Event, Reference Event Reason, and Referenced Event Status: An

unexpected event, such as a Delay, can be reported several times with a

different reference event each time. It is necessary to define which of those

Delays is taken, whether it is the event Delay with reference to the loading begin

or the event Delay regarding the unloading end.

●  Business Document where event-based charging is triggered.

## Business Document Options

The following options are available for business documents:

●  Forwarding Order Charge Calculation

●  Freight Order Charge Calculation

106


●  Forwarding Order Internal Charge Calculation

●  Freight Order Internal Charge Calculation

Step 3: Assignment of Event Profile to Business Document

The event profile is assigned to the document type where event-based charges are

activated.

The event profile can be maintained in the following document types:

●  Forwarding Order Type

In Customizing, choose Transportation Management→Forwarding Order

Management→Forwarding Order→Define Forwarding Order Types.

●  Freight Booking

In Customizing, choose Transportation Management→Freight Order

Management→Freight Booking→Define Freight Booking Types.

●  Freight Order

In Customizing, choose Transportation Management→Freight Order

Management→Freight Order→Define Freight Order Types.

107


Event-Based Charges in the Calculation Sheet

## Event-Based Charges in Calculation Sheets

To set up event-based charges in the calculation sheet, follow these steps:

1.  Maintain a new line in the calculation sheet with the charge type customized in

the event profile, which has been assigned to the appropriate document type.

2.  Define where the rate amount is coming from (for example, fix amount, rate

table, rate table determination condition, and so on).

3.  Choose the calculation base (for a fixed amount, in the calculation sheet; for

rate tables, in the rate table calculation rule section itself). This is the

calculation base for the delay with the helper class

/SCMTMS/CL_TCC_CB_DELAY assigned. Define the price unit and calculation

rule unit of measure. For example if a price unit of 1 and a unit of measure DAY

is defined, the rate amount is multiplied by the number of days of the delay.

4.  Define the related calculation base.

108


## Definition of the Related Calculation Base

For the calculation sheet item with the delay charge type, on the Related Calculation

Base tab, you define the number of grace days as outlined below.

## Definition of the Related Calculation Base

1.  Calculation Base: GRACE_DAYS. This calculation base is maintained with

helper class /SCMTMS/CL_TCC_CB_REL_CBASE.

2.  Quantity: Number of free days/hours/minutes that are subtracted from the

difference between planned and actual date/time to determine the delay.

3.  Unit of Measure: Defines the unit like days/hours/minutes.

## Charge Calculation

Reported events and calculation sheet settings influence charge calculation. The

actual date or time, and the planned date or time, are derived from event management

during the charge calculation for a specific event, which is maintained in the event

profile. The difference is the delay time without grace days.

Then the grace days are subtracted from the total delay, which ends up in the charge

calculation-relevant delay. This charge calculation-relevant delay is multiplied with the

rate amount.

With the event-based charging, it is possible to define a fixed amount per delay day or

an amount coming from a rate table for a charge type, which is then multiplied by the

number of days of delay.

109


110


Unit 4 - Managing Freight Settlement

Lesson 1 - Creating Freight Settlement Documents

## Freight Settlement Processing

A freight settlement document (FSD) is a business document that takes up the

transportation charges from TM and is posted to SAP MM (Materials Management)

creating a purchase order and a service entry sheet requesting the verification of an

invoice received from a supplier or carrier. When the invoice is received, SAP MM

checks it against the data from the freight settlement document (Transaction MIRO -

"Logistics Invoice Verification"). If performing an evaluated receipt settlement (ERS -

"Self-billing"), the automatically generated invoice is based on the data from the TM

freight settlement document.

FSDs can be used to enter the data for transportation invoicing and forwarded to SAP

MM for invoice verification. The transportation charges are calculated in SAP

Transportation Management based on a freight order, service order, or freight booking.

Freight charges are settled with the carrier (supplier).

The settlement includes the following:

111


●  Assigning and transferring transportation costs to Financial Accounting to

generate accruals, and assigning costs to a CO object.

●  Settlement of costs with the carrier: posting payables by canceling the

accruals.

You must have entered and accepted the services provided before you can transfer

costs to Financial Accounting. The system automatically creates the service entry

sheet based on a purchase order for external services. Before you can settle costs

with the carrier, you must create an invoice using manual invoice verification or create

a credit memo using the credit memo procedure.

You can create an individual FSD for one freight order, service order, or freight booking.

You can create a collective FSD for multiple freight orders or freight bookings. You can

also create multiple FSDs at the same time.

Freight Settlement Document Overview

An FSD contains the following information:

112


●  General data: Document type, the purchasing organization, payment terms,

document currency, and so on.

●  Business partner information: Invoicing party, payee, additional business

partners, which can be entered manually or automatically determined by the

system.

●  Orders: The business documents or the business document items that are

being settled using the FSD.

●  Charges: For each FSD item, the Charges tab page has the charges relevant for

settlement with the carrier.

## Freight Settlement Document Creation

Based on a transportation requirement, the planner carries out several planning steps

and create a freight order or a freight booking to subcontract the transportation

activity to a carrier.

Upon settlement, the system creates a Freight Settlement Document (FSD). This

document contains all relevant logistical data, as well as the charges and other

commercial data. The charges can be copied over from the freight order (most

common), or another charge calculation is triggered based on the freight agreement

between the purchasing organization and the ordering party. It is possible to manually

change charges in the FSD.

FSDs can be created online or in batch. It is possible to create a collective settlement

(several freight orders are settled with one FSD).

The FSD can then be posted to the SAP MM via a Background RFC or in the case of a

side-by-side S4 to TM landscape via the exchange infrastructure.

113


The FSD can be created in the following ways:

●  You can create an individual FSD for one freight order or freight booking or a

collective FSD for multiple freight orders or freight bookings. To do this, access

freight orders or freight bookings from the worklist, in the relevant document

overview, or in the freight settlement overview. The system automatically

creates the FSD based on the data in the freight orders, or freight bookings and

calculates the transportation charges.

●  You can create FSDs directly out of the freight booking or freight order apps.

●  You can create partial FSDs for previously invoiced freight documents.

●  You can create multiple freight settlement documents using the mass creation

FSD batch report.

## Note

Background reports are the following:

●  /SCMTMS/SFIR_CREATE_BATCH - Creation of FSDs

●  /SCMTMS/SFIR_TRANSFER_BATCH - Posting of FSDs to MM

114


## Partial Freight Settlement Document

It is possible to create a partial FSD for an already invoiced freight document. In this

case, the invoicing status of a freight order changes from Completely Invoiced to

Partially Invoiced before the additional FSD is created.

It is possible to add charges to an invoiced freight order, but not to remove them.

115


Lesson  2
## Management

-  Mapping  Freight  Settlement

to  Materials

## Posting Freight Charges

As shown in the figure, the typical freight settlement process flow is as follows:

Based on a delivery, the planner carries out several planning steps and creates a

freight order (FO) or a freight booking to calculate the charges and to subcontract to a

carrier.

On settlement, the system creates a FSD. This document contains all relevant

logistical data as well as the charges and other commercial data. The charges can be

copied over from the freight order or freight booking (most common) or another

charge calculation is triggered based on the freight agreement between the

purchasing organization and the carrier. It is possible to manually change charges in

the FSD. FSDs can be created online or in batch. It is possible to do a collective

settlement (several freight orders or bookings are settled with one FSD). The FSD can

then be posted to MM.

The FSD contains one or more charges sections that appear as PO items. In general,

in the case of a stage level-based charge calculation, the PO has as many items as

116


there are stages in the corresponding FO, and therefore more than one service entry

sheets, one per PO item.

After posting, the purchase order and service entry sheet are created in MM. This

constitutes the working list for invoice verification. You also have the option of

self-billing.

The PO and SES can be accessed via the transaction ME23N or via the TM Document

Flow.

## Note

The purchase order and service entry sheet are only used for technical purposes to

post accruals. The service entry sheet comprises a list of services performed by a

vendor based on a purchase order, containing service descriptions and details of

quantities and values. The descriptions of planned services deriving from the

purchase order are used as default descriptions in the service entry sheet.

## Purchase Order and Service Entry Sheet

Each service entry sheet is based on an external service order. Determining a valid

purchase order is required for transfers to Financial Accounting and for settlements.

117


You can also create the purchase order every month for the carrier. Important criteria

for the service order include carrier, purchasing organization, purchasing group, plant,

and item category.

When the system has automatically determined a valid purchase order, a service entry

sheet is created that refers to the purchase order. During posting, you accept services

and, in Financial Accounting, an accounting document for generating accruals is

created.

During account assignment, the system automatically determines the correct G/L

account in Financial Accounting for each cost item and the assignment for

Controlling. Account assignment can be carried out at different levels, depending on

the level of detail at which you want to track costs.

The transfer to Financial Accounting to establish accruals requires entering and

accepting the services rendered. The system automatically creates a service entry

sheet. Using the credit memo procedure, also referred to as the Evaluated Receipt

Settlement (ERS) procedure, you can settle the freight costs with the carrier without

having received invoices. You can choose from different settlement periods. You

transfer the calculated freight costs to Financial Accounting. The invoices are verified

by the carrier. If the carrier discovers variances, you can post these as subsequent

debits or credits.

If you receive invoices from the carrier, you can also verify the invoices manually and

create the invoices manually in logistics invoice verification.

Freight Settlement Posting Actions and Updates

118


In an embedded SAP S/4HANA system landscape, the posting of the Freight

Settlement Document is carried out via BgRFC (Background Remote Function Call).

There are various actions available that can be triggered directly on the FSD UI, the

worklists or via background jobs:

●  Save and Post: Create PO and SES, post accruals

●  Cancel Document: Cancel posted Accruals, Cancel SES + PO (Lifecycle acruals

posted)

●  Reverse Document: Create return SES for previously created PO (Carrier has to

be ERS enabled)

●  Cancel PO: Cancel PO when SES creation failed for any reason, Posting must

be started again after successful cancellation

●  Reprocess failed Document: Used when document creation failed, Used to

continue the posting process

Post FSD Directly

119


Asynchronous means here, that in the backend a BgRFC unit is created, but will be

executed later. At any point in time, the lifecycle status indicates the current stage of

the FSD in the business process. The asynchronous job leads immediately to the

following statuses:

1.  Lifecycle Status = posting started

2.  Confirmation Status = not confirmed

These statuses are updated when the BgRFC unit is executed. In addition, the user

gets messages about the triggered action.

In customizing, choose Transportation Management→Basic Functions→User

Interface→Define Message Settings.

After execution of the BgRFC unit, a Refresh leads to the updated statuses:

1.  Lifecycle Status = Accruals posted

2.  Confirmation Status = confirmed

Post FSD via batch job

120


To post a FSD via a batch job, in the backend transaction SE38, you can set up the

batch jobs:

●  /SCMTMS/SFIR_CREATE_BATCH to create an FSD with the option to "Post

## Immediately"

●  /SCMTMS/SFIR_TRANSFER_BATCH to post existing FSDs for accruals or to

reprocess failed postings

These reports process the posting and reprocessing of FSD in a synchronous mode.

## Check Results of Posting Action

After Posting, you can track and check the results if there are posting failures.

You can check in the FSD tab "Application Log" for errors or warnings.

121


In case that MM configuration is missing, this cannot be alerted upfront, but will be

shown in the Application log. Example: G/L account does not match (MM

configuration).

In the Application log, the Error messages are listed, and in the long text you get a

procedure how to solve the issue.

After completing the missing customizing, the actions "Cancel PO" (only via UI or

worklist) or "Reprocess failed documents" (only via Batch report) can be triggered.

After PO cancellation, the posting action must be triggered again.

To reprocess failed documents, you must use the

/SCMTMS/SFIR_TRANSFER_BATCH. This is done when, for example, the SES creation

or cancellation failed due to missing MM customizing. Even for a failed reversal

action, the batch report can be used.

You can also monitor the processing of the BGRFC units that will be created when an

asynchronous job is triggered. This can be done via backend transaction code

SBGRFCMON.

122


After posting, if FSD confirmation is not received for more than 2 min, go to the

BGRFC Monitor and enter the data as shown in the screenshot.

After Executing, you are able to see the background processes.

●

If the background process is still processing, then you will see the status as

"Unit Blocked/Locked"

●

If the background process failed due to some runtime error, then you will see

the status as "Unit has errors"

Select the respective entry and click on the details button to see more information.

## Note

If you are in a TM side-by-side scenario, TM and the SAP S/4HANA ERP system are

connected via SAP Process Integration or Web Services.

In this case you will have to use the backend transaction SXMB_MONI (XML Monitor)

to check the FSD integration for errors and to restart the respective service messages

for transferring the document after the customizing has been corrected.

## Automatic Change Management for Freight Settlements

There can be late changes in the freight order requiring changes to logistical data,

which may result in the change in the charges (increase or decrease). These changes

can occur at time when the old values are already transferred to settlement

documents and / or the settlement documents have also been transferred to

financials.

Accruals are posted when the financial liability is known (example: departure or

confirmed pickup of the freight by the carrier). However, there can be mid execution

changes (example: diversions (consignee changes), loss of cargo (in transit),

unavailability of cargo, unplanned costs due to detention, demurrages, loading and

unloading activities, tolls, and so on).

123


These changes may only be known after execution or during the invoicing process

(when the carrier sends the invoice).

The system uses the automatic change management process that you specify in the

relevant settlement profile. In customizing, go toTransportation

Management→Settlement→Define Settlement Profile→Change Process FSD.

TM uses the following elements to determine what approach to take with the change:

●  Change Process FSD setting in the settlement profile

●  Life cycle status of the freight settlement document

There are two different FSD Update Strategies/ Change Processes available:

When an order is changed and the invoicing status changes to Over Invoiced, the

system automatically applies the reverse and repost strategy.

For applying the automatic change process, you use the background function

"Creation of Freight Settlement Documents" (program:

/SCMTMS/SFIR_CREATE_BATCH) to create, change, and transfer the freight

124


settlement documents to Materials Management (MM). The freight settlement

document contains the changes from the freight order.

Alternatively, you go to the impacted freight document from the personal worklist or

the individual document, and you create the freight settlement document or apply

changes to the charges directly on the UI in a manual way. This would trigger the

relevant change process that is defined in the settlement profile, too.

## Configure Freight Settlement Creation in TM

When the FSD creation is triggered for a freight order/freight booking (FO/FB), the

corresponding document type is used to determine the FSD type used.

The purchasing organization specified in the FO/FB is used to determine the

settlement profile. The system takes care of the relevant charges for the FO/FB. All of

this information is then used to create FSDs for the selected FO/FB.

125


In SAP TM, there are some customizing steps that must be performed when

configuring freight settlement:

1.  Define Settlement Profiles

2.  Assign Settlement Profile to Charges Profile and Org Unit

3.  Define Number Range Intervals for FSDs

4.  Define FSD Types

5.  Assign FSD Type to FO/FB Type

## Step 1: Define Settlement Profiles

The first stage in our configuration is to define a settlement profile.

The settlement profile consists of a set of parameters with which you can control how

the system creates settlement documents.

In the Define Settlement Profile customizing activity, you can define the profile for

creating settlement documents.

You can specify the following activities:

●  Profile category to determine whether the system can use the profile to create

freight settlements, forwarding settlements, or both freight settlements and

forwarding settlements

●  Data source to determine the type of data that the system uses when creating

a settlement document. You can specify planned and confirmed data from

forwarding orders or planned data from freight orders

●  Split/consolidation strategy profile to split or consolidate settlement

documents

●  Collective invoice to create one invoice for several orders

●  Stage split to create invoices for individual stages in a freight order or

forwarding order

●  FSD Change Process for determining the FSD update strategy in the case of

late changes

126


To define settlement profiles, in customizing, choose Transportation

Management→Settlement→Define Settlement Profile.

Step 2: Assign Settlement Profile to Charges Profile and Org Unit

The second step in our configuration is to assign the settlement profile to the charges

profile.

In customizing, choose Transportation Management→Basic Functions→Charge

Calculation→Basic Settings→Define Charges Profiles.

The assignment makes it possible to control different settlement creation settings for

different organizations. It is also possible to determine the settlement profile at

runtime using the BRF+ condition of type /SCMTMS/TCM_FCP_DET. For the

assignment of a charges profile to the purchasing organization, see the PPOCE

transaction.

## Step 3: Define Number Range Intervals for FSDs

In the third step of our configuration, number range intervals are defined for the FSD.

When an FSD is created, a unique number is assigned to it, identifying the document.

The number comes from the number range, which is provided for the document type.

You define number range intervals in the Define Number Range Intervals for Freight SDs

customizing activity.

In customizing, choose Transportation Management→Settlement→Freight

Settlement→Define Number Range Intervals for Freight SDs.

## Step 4: Define Freight Settlement Document Types

You can use the freight settlement types to specify certain parameters for certain

types of FSDs.

127


To define freight settlement document types, in customizing, choose Transportation

Management→Settlement→Freight Settlement→Define Freight Settlement Document

Types.

You can specify the following parameters:

●  Business partner determination profile to assign business partners to the

freight settlement document.

●  Number range interval of FSDs.

●  FSD categories (to define either a freight settlement document or charge

correction advice).

●  Separate categories are available to define a freight settlement document and a

charge correction advice document.

●  Tracking of changes.

●  BW relevance.

●  Enable Cost Distribution.

●  Default UoMs.

●  Residence period for archiving.

●  Output profile for printing and transferring (by default, this is set to

/SCMTMS/TOR_INV_PREP).

●  Default view for the charges tab.

## Step 5: Assign FSD Type to FO/FB Types

The final step in our configuration is the assignment of the FSD type to freight order

and freight booking types.

You can assign the FSD type to one or several freight order types in the Define Freight

Order Types customizing activity.

In customizing, choose Transportation Management→Freight Order

Management→Freight Order→Define Freight Order Types.

You can assign the FSD type to one or several freight booking types in the Define

Freight Booking Types customizing activity.

128


In customizing, choose Transportation Management→Freight Order

Management→Freight Booking→Define Freight Booking Types.

## Note

Both the freight order and freight booking types have to be enabled for settlement by

checking the respective box during FSD Type assignment.

## Configure Freight Settlement Integration to MM

When the FSD is posted to MM, the accruals are posted and a PO and a service entry

sheet (SES) per PO line item are created. The SES serves as the basis for invoice

verification.

In SAP TM and SAP MM, there are several customizing steps that must be performed

when configuring freight settlement integration:

1.  Map Purchasing Organization

129


2.  Map FSD Type to PO Type and Plant

3.  Map Transportation Charge Types to MM Service Master

4.  Configure Automatic Determination of G/L Account

5.  Enable User for Invoice Verification

## Step 1: Map Purchasing Organization

TM documents contain different information than MM documents. The TM

organizational structure is different to the MM organizational structure. Therefore, the

organizational units must be mapped when a MM document (PO) is created out of a

TM document (FSD).

To find the Purchasing Organization in MM, in customizing, choose Enterprise

Structure→Definition→Materials Management→Maintain purchasing organization.

Maintain the MM Purchasing Organization/group in the corresponding TM Purchasing

Organizational Unit:

In the backend, go to transaction PPOME and choose your TM Purchasing

Organization.

In the tab Org. Data, field BSG Org. Unit, enter the MM Purchasing Organization.

## Note

In a SAP S/4HANA TM to SAP S/4HANA side-by-side deployment, the previous

settings have to be applied. In a SAP S/4HANA TM to SAP ERP side-by-side

deployment, the organizational unit mapping requires a slightly different set-up. Here

you have to assign the TM purchasing organization to the MM purchasing

organization directly in the ERP customizing:

In the customizing settings Mapping of Organizational Units, activity Assign

Organizational Units for Purchasing, you assign the TM purchase organization, TM

purchase group, and freight settlement document type to the MM organizational data.

130


In ERP, choose Integration with Other SAP Components → Transportation

Management → Invoice Integration → Invoicing → Mapping of Organizational Units →

Assign Organizational Units for Purchasing.

Step 2: Map FSD Type to PO Type and Plant

For each FSD type the following must be defined:

●  Purchase Order Type

●  Material Group

●  Plant

●  Purchasing Group

This mapping enables the system to find the right PO type, assigned to the

responsible plant and material group to take up the settled charges and create the

respective FI and material documents.

In customizing, choose Transportation Management→Settlement→Freight

Settlement→Integration for Settlement Posting→Assign Purchasing Information for

Posting.

Step 3: Map Transportation Charge Types to MM Service Master

It is crucial to assign the transportation charge item categories, transportation charge

item subcategories, and transportation charge types to MM service master records,

also called activity numbers, and account assignment categories.

The account assignment category, set to "K" for the cost center, specifies which

account assignment data is necessary for an item. The cost center serves as an

organizational unit within a controlling area that represents a defined location of cost

incurrence.

The MM Service Master Record/ Activity number represents the purchased service

based on the TM Charge Type. The services are depicted in the PO Item section. In

transaction AC01 the activity numbers can be set-up. Here, they are also linked to a

131


valuation class, which enables the system to find the respective G/L accounts that are

updated when services are entered.

In customizing, choose Transportation Management→Settlement→Freight

Settlement→Integration for Settlement Posting→Assign Service Master Record and

Account Assignment Category.

## Note

In a SAP S/4HANA TM to SAP ERP side-by-side deployment, at first you have to set-up

the TM Charge Types, Categories, and Subcategories in the ERP system. After you

have done that, you can map the Charge Types to MM Service Masters.

In SAP ERP, in customizing choose Integration with Other SAP Components →

Transportation Management → Invoice Integration → Invoicing → Definition of

Transportation Charges → Define Charge Type.

Step 4: Configure Automatic Determination of G/L Account

During settlement cost processing, the system can determine G/L accounts for the

transportation costs automatically. This process uses the settings that you configure

in the following Customizing activity to find the correct G/L accounts:

In customizing, choose Materials Management→Valuation and Account

Assignment→Account Determination→Account Determination without

wizard→Configure Automatic Postings.

Here, you define the determination of for example, the GR/IR clearing account, which

takes up the accruals for the transportation charges and is balanced when the carrier

invoice is received and verified. Furthermore, you set-up the determination of material

Inventory and consumption accounts as well as freight clearing accounts.

## Note

This activity is performed in close corporation with the financial department of

customers and demands close alignments. A further prerequisite is the complete

132


set-up of the respective MM and FI/CO basic settings (for example, PO types, posting

periods, valuation classes, movement types, and so on).

## Step 5: Enable User for Invoice Verification

To enable invoice verification, set up the user parameter TM_INVOICE_CLERK in the

user data. With the user parameter TM_INVOICE_CLERK, you control which tabs the

user sees when entering or changing incoming invoices in the transactions MIRO and

MIR7, in change mode in the transaction MIR4, and in GR/IR clearing account

maintenance in the transaction MR11.

In logistics invoice verification (MIRO), the user is now able to see the TM Ref. Tab.

Here, you can enter for example, the freight order ID or the carrier ID to bring up the

freight settlement transportation charges for comparing them with the carrier invoice.

In transaction SU01 or SU3, enter the respective user name and maintain the

parameter ID in the tab Parameters plus parameter value X.

133


Lesson 3 - Verifying Carrier Invoices and Self-Billing

## Carrier Invoice Verification & ERS

In SAP MM, the purchase order and service entry sheets are created using the worklist

for the invoice verification. There is also an option to do a self-billing (ERS).

The invoice verification is performed in SAP MM and can be done with reference to an

SAP TM freight order, carrier, bill of lading, air waybill, flight number, or voyage number.

If SAP MM successfully verifies the actual invoice against the expected invoice, SAP

TM is notified by updating the freight settlement document (FSD) with the invoice ID

and actual amounts. SAP TM updates the Life Cycle Status of the FSD to Invoice

Verified. Once the FSD has reached this status, it is not possible to cancel the invoice.

In MM, for logistics invoice verification, internal documents such as a purchase order

and a service entry sheet that the system requires for invoice creation are created

based on TM data. When incoming invoices are entered or canceled, external TM is

informed by enterprise service Supplier Invoice Notification (InvoiceNotification_Out).

134


When working with TM as an internal component, the updates to the freight

settlement document are done online.

When verifying invoices in MM, you can navigate to the TM freight order details by

clicking on the Details for the invoice item.

## Ready for Settlement

Once the settlement process is completed, the process for paying the carrier invoice

can begin. Using transaction MIRO, the vendor invoice can be entered. However, if the

evaluated receipt settlement (ERS) procedure is in place, this process occurs

automatically.

For SAP TM-related invoices, there is a TM Reference tab in the MIRO transaction. To

view this tab, you must set up the user parameter TM_INVOICE_CLERK in the user

data. With the user parameter TM_INVOICE_CLERK, you control which tabs the user

sees when entering or changing incoming invoices in the transaction. The user

parameter can be set to Blank (where the user sees both the TM Reference and PO

Reference tabs) or X (where the user sees the TM Reference tab only).

Financial Postings

135


 When a payment is made, financial postings are carried out. These are the same

postings that would be made for non-TM related invoices.

Evaluated Receipt Settlement (ERS)

Evaluated Receipt Settlement, also known as "self-billing" is the process of settling

goods receipts directly without receiving an invoice from the carrier. The system can

generate the corresponding invoices and post them. A carrier invoice is no longer

required. You can execute the evaluated receipt settlement with reference to

documents in Transportation Management.

If you have a long-term partnership with your carriers and the respective carrier

executes many orders for your company with an outstanding performance, this

process is a common practice to reduce the administrative effort regards financial

settlement.

In the same way as when incoming invoices are entered, in evaluated receipt

settlement TM is informed by an enterprise service (SupplierInvoiceNotification -

InvoiceNotification_Out) when you use an external SAP TM system. When you use an

136


internal TM system, the ERS process notifies the freight settlement document when

the system creates an invoice online.

For using the self-billing scenario, the carrier business partner has to be enabled for

ERS.

To check if the carrier is enabled, go to Transaction BP, choose your carrier and the

role FLVN01 MM Vendor. In the header bar, click on Purchasing. In the Purchasing

Data tab, check if the flag for ERS is set.

## Note

The ERS flag comes from the MM BP settings. It cannot be set in the TM.

In the same tab, section Additional Control Data, check that the flag "Auto GRSet. Ret."

is set. This "Automatic evaluated receipt settlement for return items" flag enables the

creation of the Credit Memo via the ERS process. If the carrier is ERS-enabled, a

posted and invoiced FSD (lifecycle status "invoice verified") can be reversed via the

137


"Reverse Document" action button directly in the FSD or in the worklist. A new SES

with the returns indicator set will be created.

The ERS process and a variance called carrier invoice submission, can also be

performed using the SAP Business Network for Logistics (SAP BN4L), which is a

cloud-based carrier portal solution available with a separate licence.

## Submitting Carrier Invoices

Freight Settlement and Dispute Management are the process of publishing the freight

charges in the SAP Business Network for Logistics and resolving differences in

charges in a freight order (FO) or freight booking (FB) between a carrier or logistics

service provider (LSP) and a requester of transportation services, such as a shipper or

an LSP. This functionality simplifies and accelerates the carrier invoicing and

correction processes. Also, there is no need to set up extra interfaces from third

parties to SAP MM for uploading incoming carrier invoices for invoice verification. The

carrier creates an invoice directly in the SAP Business Network for Logistics. This

invoice gets matched to the calculated freight order amount, and the freight

settlement process can be executed later.

Freight Settlement and Dispute Management via SAP Business Network for Logistics

are supported for modes of transports road, ocean, and air. Invoice submission is

supported via API or web UI, dispute management via backend integration for

shippers and via web UI for carriers.

138


The carrier can verify all relevant logistical and the respective charge amounts. If the

carrier wants to change or add data, the collaborative invoice dispute management

functionality can be triggered. The dispute can involve changes in logistics item

quantities (weight, volume, and distance) or item charges, and can lead to changes in

charge amounts in freight order.

The freight settlement in SAP Business Network Freight Collaboration addresses

invoice creation, including potential dispute management. It is currently available for

road and ocean shipments. It enables you to manage freight settlement with your

carriers in sync with your transportation management system as it is integrated into

SAP Transportation Management and SAP S/4HANA Transportation Management

out-of- the-box. You can define your settlement process centrally, which includes the

mapping of internal charge codes from your transport management system to the

charge codes visible to your carriers. In addition, you can configure tolerance levels,

for example, which discrepancies you are willing to accept (and maybe even auto

approve) and above which level you enter into a dispute process.

While large carriers create invoices themselves that they can share using the

standardized EDI 210 format, you as a shipper can also trigger the billing process. You

can initiate self-billing based on freight documents in your transportation

management system that the carrier receives through SAP Business Network for

Logistics (‘Review Freight Document’ Tile). In case there is a discrepancy between the

139


agreed and the actual amount charged in the carrier invoice, a dispute can be raised

(based on your tolerance settings). As a shipper, you receive a worklist of disputes.

You can navigate into each invoice and review the details to decide whether you will

accept, propose other values or decline. If the shipper has updated or resolved a

dispute, you are notified via e-mail.

In this process, we assume that the carrier creates the invoice based on the freight

documents shared via SAP Business Network Freight Collaboration. From their

worklist in the Web UI, the carrier can start creating the invoice, which contains the

items as of the freight documents. Extra charges can be added such as tax, road tolls,

and so on. Then the invoice is submitted for review to you as the shipper.

In case there are any discrepancies between the planned and the actual invoice, a

dispute can be raised. You can automatically identify invoices for dispute based on the

tolerance settings configured. These can be specific amounts or percentages.

Relevant approver(s) are notified automatically about new disputes (via e-mail) and

can process the dispute in the SAP Business Network Freight Collaboration Web UI.

As a shipper, approvers will be able to include internal notes (for example, for the next

level approver) or a note to the carrier. Once the dispute has been settled, the initial

invoice can be canceled with a credit memo (the entire invoice amount will be

canceled) and a new invoice can be resubmitted by the carrier. Once you receive this

new invoice, you can further process it, creating a service PO in your transport

management system and forwarding it to Finance.

140


Lesson 4 - Correcting Freight Charges

## Freight Charge Correction

After the posting of a freight settlement document (FSD), if the actual freight charges

are identified as different, then a charge correction document can be created to

correct the charges for the differential amounts.

The following charge correction documents are supported in SAP TM:

●  Credit memo (CM)

●  Charge correction advice (CCA)

Credit memos are used for charge correction on freight documents for all modes of

transportation except air. For air freight processes (freight booking), a charge

correction advice is used. Both of these two documents are freight settlement

documents of a specific category (CM & CCA). The category for a freight settlement

can be set in the respective FSD Type customizing activity.

## Note

As mentioned, both the Credit Memo and the CCA are FSD Types. That also means

they have to be mapped to MM and the integration customizing activities have to be

carried out as you learned in the Post FSD section of this course.

141


## Credit Memo for Freight Orders

You can use a credit memo to get a credit from a carrier in a freight settlement when

you have overpaid for transportation services. You use a freight order, freight booking,

or service order as a reference when you create a freight credit memo.

## Carrier Overcharge

A carrier could overcharge for transportation services in the following circumstances:

●  The carrier demands an amount, which is over the current planned amount

(and is above the tolerance).

●  You demand a lower amount to be billed than what the carrier has billed you or

is expecting.

●  You expect credit from the carrier for the excess billing or the excess amount

that you have paid the carrier.

●  Reversal of the billing item/amount due to incorrect billing.

## Credit Memo

You create a credit memo for an individual freight order, freight booking, or service

order with relationship to the respective freight settlement documents or FSD items, in

case of a collective settlement, for these orders. You can access the credit memos

from the freight settlement documents overview screen.

142


You can create a credit memo from a freight settlement document on the overview

screen for the freight settlement documents.

The system creates the credit memo based on the data in the associated freight

settlement documents and displays the amount that has already been invoiced.

When you use the automatic change process, the system uses the existing freight

settlement document to create a credit memo. This enables the system to process a

large-scale change to the freight document charges, for example, a change in the

agreement or in the calculation sheet, or the addition or deletion of a charge line.

## Example Flow for Credit Memo Process

The change process "Reverse and Repost with new FSD" is used:

●

In a freight order, the transportation charges are 2000 USD. The FO is

completely invoiced with a FSD along with a PO and a SES in MM.

●  Due to a granted discount from the carrier, the FO charges are reduced to 1800

USD. The FO is overinvoiced.

●  The system creates a credit memo to reverse the current FSD and posts the

CM to MM. Here, a new PO and a SES with returns indicator are created.

●

In the last step, a new FSD for the updated amount of 1800 USD is created and

posted to MM. A new PO and SES are created. The FO is in the status

completely invoiced again.

As a result, the FO is linked to two FSDs, one CM and three SES in MM.

## Note

A credit memo can only be created for a freight document that has been invoiced

completely and has the status Accruals Posted.

143


Prerequisites for Creating a Credit Memo

●  Types of credit memo and credit memo reason codes

○

## In customizing, chooseTransportation

Management→Settlement→Freight Settlement→Define Credit Memo

Reason Codes and Types for Freight SDs.

●

## Influence invoicing status

○  You can specify the Influence Invoicing Status setting in the relevant

default credit memo type. When you create a credit memo, either

manually or by using the background processing function, the credit

memo has a role in determining the invoicing status of the freight

orders, freight bookings, or service orders.

○

## In customizing, choose Transportation

Management→Settlement→Freight Settlement→Define Credit Memo

Reason Codes and Types for Freight SDs.→Define Credit Memo Types

Influence Invoicing Status.

●  Automatically enter credit amount

○  When you specify that the system automatically enters the credit

amount, the system automatically copies the remaining credit amount

to the credit amount in a credit memo

○

## In customizing, choose Transportation

Management→Settlement→Freight Settlement→Define Credit Memo

Reason Codes and Types for Freight SDs.→Define Credit Memo Types

Automatically Propose Credit Amount.

For invoice verification, in transaction MIRO, select Credit Memo. Then enter the freight

order for which the credit memo was created. Enter the amount of the freight order

and post the invoice. The credit memo is now verified. The status of the credit memo

is in SAP TM.

144


## Dispute Management

Freight dispute management is the process of resolving differences in logistics

quantities and charges in a freight order (FO) or freight booking (FB) between a carrier

or logistics service provider (LSP) and a requester of transportation services, such as

a shipper or an LSP.

The expected charges of an FO are exposed on a portal (SAP Business Network for

Logistics), which the carrier can access. The carrier can then verify relevant logistical

data and charges. If the carrier wants to change or add data, it is then possible to

create a dispute. The dispute can involve changes in logistics item quantities (such as

weight, volume, and distance) or item charges (USD or hour), and can lead to changes

in charge amounts in the FO.

Dispute management with self-billing can also be established between an LSP and a

carrier or a carrier and another subcontracted carrier.

For freight orders, the dispute management process can be managed in the SAP

Business Network for Logistics based on submitted invoices from the carrier. From

the shipper perspective, the disputes are either managed in TM or in SAP Business

Network for Logistics.

145


For freight orders and ocean freight bookings, the carrier can create its invoice either

in the Web UI or via an API. For ocean freight bookings, the dispute can be managed in

the SAP S/4HANA system of the shipper.

In the case of self-billing, the dispute from the shipper perspective can be managed

either in SAP Business Network for Logistics or in the SAP S/4HANA system of the

shipper.

146


## Business Scenario Examples

In this section, we look at examples of common disputes that arise between shipper

and carrier.

Business Scenario Examples

Scenario

Example

## Automatic

The carrier raises a dispute about the logistical data, for

tolerance

example, the gross weight is 5500 KG instead of 5000 KG, which

acceptance

results in the base freight value increasing from 500 USD to 550

USD. The dispute case is automatically approved by the

tolerance rules set by the shipper.

Dispute on

The carrier raises a dispute to charge the shipper for detention

unplanned costs

or demurrage. The tolerance defined by the shipper fails to

approve the dispute and triggers the workflow. The shipper

accepts that there was a detention or demurrage and manually

approves the dispute.

Dispute on

The carrier feels that the rate for base freight is incorrect and

revised rate

raises a dispute with the revised rates. The shipper then

amount

proposes a new rate with the carrier. The carrier can then either

accept the new rate or start a second round of negotiation.

Dispute on

The carrier raises a dispute on the manual charge coming from

manual charge

the agreement. In the agreement, loading charges of 100 USD

coming from an

per hour are defined. If according to the shipper, loading took 4

agreement

hours, the final amount is 400 USD in the FO. The carrier can

raise a dispute on QTY (hours), RATE (total rate), or both (but not

on Price per unit).

147


## Reject a dispute

If a shipper rejects a dispute case, the carrier can accept the

rejection or propose a new amount and resubmit it to the

shipper via the Logistics Business Network.

## Mixed Scenario

The shipper can accept, reject, and propose some or all of the

charge disputed items.

148


Unit 5 - Distributing Transportation Costs

Lesson 1 - Distributing Freight Costs

## Cost Distribution

Cost distribution takes place in a freight order (FO), a freight booking (FB), or a freight

settlement document (FSD). Posting of the distributed cost to SAP S/4HANA is done

with the freight settlement document (FSD).

In the shipper scenario, the distribution level is set to ERP item (Order/ Delivery item).

In the logistics service provider (LSP) scenario (for cost-based internal settlement), the

distribution level is set to forwarding order.

149


## Cost Distribution Steps

Cost distribution involves the following steps:

1.  Distribution of the freight costs at the level of delivery items based on some

rules, such as Weight of the Delivery items. This step is executed in TM.

2.  Processing of the distributed freight costs in the financials for either processing

the freight cost for material valuation or for expensing at the product level. This

step is executed in the respective SAP S/4HANA modules.

For example, the inbound delivery freight cost is typically posted for material

valuation. Outbound delivery costs are posted to cost objects or modules, such as

CO-PA segments from the sales order, to calculate the profitability during sales order

processing.

Freight Cost Posting via Settlement Management Integration

TM uses SAP S/4HANA's LO Settlement Management module for distributed freight

cost posting.

Settlement Management provides a flexible posting engine where you can define the

type of processing that is carried out from a financial processing perspective via

customizing. TM uses this posting engine to hand over the distributed freight cost to

SAP S/4HANA.

The Settlement Management document provides a documented way of posting

distributed freight costs in SAP S/4HANA.

The Settlement Management document item created for TM freight cost postings has

references to the following:

●  Order and order item–sales order, purchase order, or stock transfer order and

the corresponding item reference.

●  Delivery and delivery item–Inbound or outbound delivery and the corresponding

item references. During order and delivery integration processing, TM transfers

these references.

150


●  Service purchase order–The service purchase order (for freight cost), linked to

the FSD integration with SAP MM.

●  TM freight settlement document (FSD).

●  TM freight order (FO).

Settlement Management provides native integration to financial functions, such as

financial accounting, controlling, CO profitability analysis, material valuation, and

material ledger. For example, based on a given reference document, you can specify

that the freight cost processing will be posted to the material account.

Settlement documents do not create or update any accounts receivables or accounts

payables. The document is used only for material adjustment postings to either

expense general ledger (G/L) accounts or to material accounts.

## Document Types in Freight Cost Posting

For posting freight costs, SAP LO Settlement Management uses the following

document types:

1.  Settlement Document Generic: This document type enables you to post freight

costs to material valuation.

2.  Settlement Process Type: This document type enables you to post freight costs

to the G/L accounts.

Existing processes in Settlement Management and posting options are determined via

use case types and document categories during mapping for cost distribution.

## Customer Scenarios: Examples

The following are examples of customer scenarios:

## SAP S/4HANA Integration

●  Transfer transportation cost as a delivery cost for the inbound material

(material-level tracking).

The transportation cost flows to material valuation. The freight cost transfer as

151


delivery cost is not updated in the purchase order of the material. The delivery

cost posting is achieved via the posting carried out by the Settlement

Management document.

●  Post the cost back to CO objects linked from order/delivery/material.

The material-relevant costs are tracked directly down to the CO objects from

the transactions but more likely at an aggregated level, not necessarily at the

material level. That is, there is no material valuation update. For example, all

material-relevant costs, including indirect costs such as transportation, are

tracked at the profit center level. Costs are segregated based on material

movements (inbound, inter/intra, and customer deliveries).

●  Post cost back to the sales order /CO-PA responsible for the delivery (outbound

scenario).

This scenario occurs on the seller's side. Costs associated with the sales order

directly are tracked and have an impact on profitability analysis (CO-PA)

segments.

Customer Scenario: Goods Calculation

152


In the example in the figure, we see how the final cost of a finished good is calculated.

Before the finished good leaves the factory, the material cost consists of different cost

components, such as the cost of material and manufacturing overheads. In CO-PA,

some other costs can be displayed, such as fixed costs based on material costs or

depreciations, and so on.

In the case of a stock transfer order where finished goods are moved from the

manufacturing plant to an external warehouse, a transportation cost is incurred. Cost

distribution is required to assign this cost to the responsible material.

The material in the external warehouse is charged with the transportation costs based

on a certain distribution key, such as weight or volume.

The scenario illustrates how the freight cost distribution functionality allocates the

freight cost to the level of material and then processes the cost for material valuation.

This is one example where the TM freight cost distribution functionality plays a role in

allocating the freight cost to the level of material from the freight orders, before

processing this cost information for material valuation.

From the example, you can extrapolate that the material cost valuation increased from

$750 to $870, including the $120 actual transport cost from TM. This $120 represents

the distributed cost for a given material in a transport. If the material valuation type is

set to moving average, the cost increases upon receipt of the product. If the material

valuation type is set to standard pricing the cost does not change until the next

valuation run.

153


Freight Cost Distribution Process

1.  In LE, create a delivery.

2.  In TM, based on the delivery, freight units (FUs) are created in the background.

3.  The freight units are assigned to certain freight orders (FOs) or freight bookings

(FBs) for subcontracting to a carrier (air/ocean/land) and charge calculation.

4.  In TM, create a freight settlement document (FSD) to post to SAP S/4 for

invoicing and cost distribution.

5.  In TM, cost distribution occurs in the FSD based on certain distribution rules

such as weight, volume, distance-times-weight, or a customer-specific rule

such as the number of product pieces in an SD order item.

6.  Send the FSD containing all the freight costs and the distributed freight cost

details to SAP S/4HANA. Here the following two process subsets are executed:

●  The overall freight costs are posted to SAP Materials Management (MM)

(step 6a in the figure) where a purchase order and a service entry sheet

(SES) are created.

●  The distributed freight costs from the FSD are transferred to the

settlement management posting engine in SAP S/4HANA for posting to

the responsible cost collector (step 6b in the figure). Based on

information such as an SD order item, the settlement management

154


distributes the cost to the appropriate cost object in Controlling or to

CO-PA. In the case of inbound deliveries for purchase orders or stock

transfer orders, the freight cost may be posted to material valuation and

to different CO object-level cost centers, determined from the production

order or stock transport order. This step takes place in the background.

In SAP S/4HANA, you can monitor this event using transaction

WLFLTM2 or the Fiori Launchpad and view the list of such freight cost

documents.

7.  In MM, based on the purchase order with a service entry sheet (SES), an

incoming carrier invoice is verified and posted using transaction MIRO. Any

deviation in the verification creates a new Adjustment settlement management

document for the difference. The adjustment document uses the same

splitting logic as the original document for the planned costs coming from TM

(See step 7a and step 7b in the figure).

Distributed Freight Costs Posting

155


The figure shows an example of a typical posting pattern. The setup has to ensure the

following:

1.  From a financial posting perspective, at the material level, there are two steps

in the process of posting freight costs to either material valuation or G/L

account. In the first step (2a in the figure), the total freight costs are posted to

an intermediate account, such as a freight clearing account. In the second step

(2b in the figure), the amounts are moved from the freight clearing account to

the material or G/L (expense) account, based on material information from the

relevant sales, purchase, or stock transfer orders.

2.  The account posting key GBB, which is set up for the FSD, points to the freight

clearing account (transaction OBYC).

3.  The step 6b is derived from the Settlement Management postings setup.

a.  In the case of inbound freight cost posting, the VBD setup picks up the

freight clearing entry based on the account key maintained in the pricing

schema (see example WT0001). The inventory posting account is

determined by the material and its attributes, and determine whether it

is posted to BSX or PRD.

b.  For outbound freight cost posting, the settlement document picks up

both the accounts from the pricing schema. The freight clearing account

is picked up from the account key accrual field, and the freight expense

account from the accounting key. (For example, see pricing schema

WT0002.)

4.  For outbound freight cost posting, if the freight cost components are to be

posted to different G/L accounts, then map TM charge types to both the

condition types (which are SAP MM conditions) and the account posting keys

that were set up for the settlement document type. (For example, see pricing

schema WT0002.)

156


Cost Distribution Configuration TM

## Cost Distribution Configuration

The cost distribution configuration consists of the following:

●  Defining cost distribution methods

●  Assigning cost distribution methods to distribution profiles

●  Defining the organizational unit settings for charge calculation

●  Enabling the freight settlement and freight order/booking types for cost

distribution

Step 1: Define Cost Distribution Methods

157


In Customizing, choose Transportation Management→Basic Functions→Cost

Distribution→Define Cost Distribution Methods.

In the Define Cost Distribution Methods customizing activity, you assign a distribution

method to a distribution class, in which you have specified your own distribution logic.

This enables you to specify your own distribution method for cost distribution.

The standard settings deliver two default methods: direct distribution and hierarchical

distribution.

If necessary, you can add your own distribution methods in this customizing activity.

## Direct Distribution

In a direct distribution, the system distributes costs according to the attributes you

specify in the distribution rule and distribution level, without reference to where in the

item hierarchy you package a product. For example, if you specify a distribution rule of

Gross Weight and a distribution level of ERP Item, the system uses the gross weight of

158


the ERP item in the cost distribution, regardless of where the ERP item appears in the

item hierarchy of the freight order or freight booking.

In the example in the figure, the distribution method is set to Direct, the distribution

rule is Gross Weight, and the distribution level is ERP Item (that is, the product).

In a direct distribution for product 40, the system performs the following calculations:

 Product 30 = 1500 kg.

Product 40 = 2500 kg.

Product 70 = 500 kg.

The distribution for product 40 is 2500 kg/ (1500 kg+ 2500 kg + 500 kg) * USD 2000 =

USD 1111.11.

In general, whether it is hierarchical or direct distribution, costs are applied to those

products that are accruing costs. For example, there is a freight order with two stages,

and in the charge management master data, the calculation resolution base for basic

charges is defined as STAGE. This means for that freight order, each stage is

calculated separately. As this freight order has two stages, the basic charges are

calculated twice. Then during cost distribution, the basic charges of each stage are

allocated to only those products that are being transported on that specific stage.

Therefore, costs accruing on the first stage are allocated to the products that are

transported on the first stage. The same applies to the second stage.

159


## Hierarchical Distribution

In the hierarchical distribution method, the system uses a step-by-step approach to

take each level of the packaging hierarchy into account in the cost distribution. For

example, if you specify a distribution rule of Gross Weight and a distribution level of

ERP Item, the system uses the gross weight at each level of the item hierarchy to

distribute the higher-level costs to the ERP item level. The system takes into account

the tare weight of the packaging in the packaging hierarchy.

In the figure, you can see a table containing an example of data from a freight

settlement document. In this example, the cost distribution is done first to move all

Root (header) level charges of the freight order to the containers. Then the cost is

distributed from each of the container items to the packages in the container, and

finally to the product.

You perform a cost distribution for product 40. You specify a distribution level of ERP

Item and a distribution rule of Gross Weight. The charge type is applicable to the whole

160


document, with a calculation resolution base of root. The total freight cost is USD

2000.

In a hierarchical distribution for product 40, the system performs the following

calculations:

Step 1

 Container 10 = 7500 kg.

Container 60 = 2500 kg.

The distribution for container 10 is 7500 kg/(7500 kg+2500 kg) * USD 2000 = USD

1500.00.

Step 2

Package 20 = 1750 kg.

Package 50 = 2750 kg.

The distribution for package 50 is 2750 kg/(2750 kg+ 1750 kg) * USD 1500.00 =  USD

916.67.

Step 3

Product 40 = 2500 kg.

No distribution is required, because package 50 includes only product 40: USD 916.67.

161


## Step 2: Define Cost Distribution Profile

In Customizing, choose Transportation Management→Basic Functions→Cost

Distribution→Define Cost Distribution Profiles.

In this Customizing activity, you specify the settings you want the system to use to

perform cost distribution in a freight order, freight booking, or freight settlement

document. You can specify the following settings:

●  Distribution Method - Specifies the analysis approach the system takes in

performing a cost distribution.

●  Distribution Rule - Specifies the criteria that the system uses to perform a cost

distribution. Criteria can include gross weight, net weight, gross volume,

distance times weight, and a custom rule (based on a BAdI).

●  Distribution Level - Specifies the target level to which the system allocates

costs for a freight order or freight settlement document (FWO or ERP Item).

162


Step 3: Assign the Cost Distribution Profile to the Organizational Unit

In the Charge Calculation customizing activity, you can assign the distribution profile to

the organizational unit for charge calculation.

In Customizing, choose Transportation Management→Basic Functions→Charge

Calculation→Basic Settings→Define Charges Profiles.

Step 4: Assign Charges Profile to Organizational Unit

Assign the charges profile to the purchasing organization in transaction PPOME.

## Step 5: Enable Cost Distribution in Document Types

Cost distribution takes place in the freight order (FO), the freight booking (FB), and the

freight settlement document (FSD).

The posting of distributed costs to SAP S/4 is done with the FSD.

## Cost Distribution Enablement

To enable cost distribution, choose one of the following paths in Customizing:

●  FSD type:

 Transportation Management→Settlement→Freight Settlement→Define Freight

Settlement Document Types.

163


●  Freight order type:

 Transportation Management→Freight Order Management→Freight

Order→Define Freight Order Types.

●  Freight booking type:

 Transportation Management→Freight Order Management→Freight

Booking→Define Freight Booking Types.

Customer-specific Cost Distribution Settings

## SAP Business Add-Ins (BAdIs) for Cost Distribution

SAP Business Add-Ins (BAdIs) are used to adapt SAP TM to specific cost distribution

requirements:

●  Cost distribution rule (/SCMTMS/TCD_DISTRIB_RULE)

You can use this BAdI to perform the following tasks:

○  Overwrite the distribution rule for the individual charge types provided in

the Define Cost Distribution Profiles Customizing activity (the standard

distribution rule in the Customizing activity covers all charge types in a

business document). For example, you can specify a distribution rule for

gross volume instead of gross weight for an individual charge type.

○  Provide your own distribution rule for any quantity field.

●  Cost distribution rule at hierarchy level (/SCMTMS/TCD_DIST_RULE_HIE_LVLS)

You can use this BAdI to specify a different distribution rule at each level of a

hierarchical distribution. For example, in a freight order for a trailer, you can use

one rule for the trailer, another rule for the packages in the trailer, and another

rule for the products in the packages.

●  Exclusion of charge lines (/SCMTMS/TCD_UNALLOC_CE)

164


○  You can use this BAdI to prevent the system from distributing charge

lines during a cost distribution analysis. The system stores these items

as unallocated.

○  The system calls this BAdI before it runs the distribution logic on charge

lines.

●  Exclusion of Items from a Cost Distribution (/SCMTMS/TCD_UNASSIGN_DI)

○  You can use this BAdI to change the way the system distributes costs

for one or more distribution items in a freight document.

○  The system does not allocate a cost to one or more distribution items

that you exclude from a cost distribution in a freight document, such as

a freight order. Instead, the system allocates the cost to the remaining

distribution items in the freight document.

You can activate the BAdI implementations in Customizing.

In Customizing, choose Transportation Management→Business Add-Ins (BAdIs) for

Transportation Management→Basic Functions→Cost Distribution.

For information about implementing BAdIs as part of the enhancement concept, see

SAP Library under BAdIs - Embedding in the Enhancement Framework.

## Cost Distribution S4 Mapping Configuration

In the Assign Transportation Charge Types to Condition Types Customizing activity, you

can assign a transportation charge type to a MM condition type for cost distribution.

165


This setting is needed for shipper scenarios in TM, where the freight cost distribution

is activated with the TM freight settlement document (FSD) to the SAP order item. The

SAP S/4HANA system uses this assignment and mapping when processing the

settlement management document for processing the distributed freight cost posting

to Financials.

In Customizing, choose the following path: Transportation

Management→Settlement→Freight Settlement→Integration for Settlement

Posting→Mapping for Cost Distribution→Assign Transportation Charge Types to

Condition Types.

Cost Distribution Configuration: Settlement Management

For inbound & outbound freight costs, the system creates Settlement Management

Document and Process Types for TM integration.

## Settlement Document Types

Settlement document types control the processing of settlement documents, such as

invoices, credit, and debit memos, as well as cancellation documents.

In the Settlement Document Types customizing activity, you define the settlement

document types that model the different business transactions involved with cost

distribution activities.

Settlement document type 1600 Cost Distribution, is the generic document type for

posting freight costs.

For canceling/ reversal of the posting, the settlement management uses document

type 1601.

In the section Control of Account Determination, the settings for determining the

accounting procedure (MM Account Determination) and the clearing account

assignment is done.

You can adapt these document types during implementation.

166


In Customizing for Logistics - General, choose the following: Logistics -

General→Settlement Management→Settlement Documents→All Document Types.

To process outbound freight costs, the system creates and uses settlement process

types with settlement documents to determine the right settlement procedure for SAP

TM integration purposes.

## Settlement Process Types

In the Settlement Process Types customizing activity, you define process types that

determine and depict the different business transactions involved in processing

payments for vendors and customers.

Process type 1600 Cost Distribution on G/L accounts - TM, is the settlement process

type for posting freight costs on G/L accounts. It has a settlement document type

1600 assigned to be used for processing the freight costs and right accounts.

You can adapt this process type during implementation.

In Customizing for Logistics - General, choose the following: Logistics -

General→Settlement Management→Settlement Process→Define Settlement Process

Types.

167


## Basic Settings for Settlement Document Creation

In the Basic Settings for Creation of Settlement Management Documents Customizing

activity, you can specify the customizing used for the creation of the specific

settlement documents based on reference documents, such as orders and deliveries

as well as use cases. This configuration drives the freight cost posting via the

settlement management documents.

You must specify settlement document types and process types. If you input

calculation procedures, the settlement management procedure determination is

overruled. Some of the keys of this table are set in BAdI Determine Fields That Control

Settlement Management Document Creation.

## Configuration Fields

The following fields are filled out during the configuration:

●  Reference Document Category: Indicates the classification for the various

document categories that you can process in the system (for example

168


purchase orders, sales orders, or invoices). It corresponds to the direct

reference of SAP S/4HANA objects in the FO or FB in TM. For example, if the

FO is linked to a sales order, then while posting distributed freight costs to SAP

S/4HANA, this line is referenced to pick up the posting rule.

●  Posting Type: Blank is the default value. If there are other business scenarios

and the customer would like to extend the posting rules, this field allows

special posting.

●  Use Case Type: The use case characterizes existing business processes within

Settlement Management. For freight cost posting, the following two rules are

relevant:

○  30 - Freight Cost Posting on Material Account

○  31 - Freight Cost Posting on G/L Account

●  This use case drives the type of posting: Use case type 30 creates Settlement

Documents to post to material account and use case type 31 posts to expense

account.

●  Condition Application: Subdivides the usage of a condition (for example, pricing)

for use in different application areas (for example, sales and distribution or

purchasing). Purchase is the default use for the pricing procedure from the MM

module (Purchasing).

●  Document Category: This is directly related to the use case type. The value

Settlement is used to post to the G/L account (outbound), and Invoice for

posting to material valuation (inbound).

●  Settlement Process Type and Settlement Document Type fields: You assign the

document types here that is used to post to the G/L account via the process

type or the material valuation via the settlement document type.

For example, for inbound delivery, the use case type is 30 - Freight Cost Posting on

Material Account. You then assign the settlement document type 1600 for such a line.

In Customizing, choose the following: Transportation

Management→Settlement→Freight Settlement→Integration for Settlement

Posting→Mapping for Cost Distribution→Posting Using Settlement

Management→Basic Settings for Creation of Settlement Management Documents.

169


## Note

As a prerequisite, all basic settings in SAP S/4HANA LO, MM and FI/CO are required

and have to be set up properly. This activity is performed in close corporation with the

financial department of customers and demands close alignments. SAP also delivers

BAdis to alter the behavior of the integration and posting processes.

170


Lesson  2
## Documents

-  Understanding  Freight  Costs

in  Settlement

## Analyze Cost Distribution Postings

The SAP S/4 integration for freight cost distribution processing occurs in the following

stages:

## Integration for Freight Cost Processing

1.  Transfer the transportation costs as "delivery costs" for the material (inbound

scenario).

 Have the transportation costs flow to material valuation.

2.  Post the transportation costs back at the level of the sales order/CO-PA/CO

objects that are responsible for the shipment costs (outbound scenario).

 Post all the freight costs at the level of sales order or other controlling object,

or CO-PA to track the costs associated with the shipment.

## Freight Order Distribution: Based Upon Weight

In the example in the figure, there is a freight order with three charge codes: Basic

Freight (5000 USD), BAF (500 USD), and CAF (-125 USD).

Each delivery consists of only one item with the weight specified as 5000 KG for

Delivery 1, 10000 KG for Delivery 2, and 7000 KG for Delivery 3. The distribution is

performed based on the weight for each charge type. The total weight of the freight

order is 22000 KG.

To perform the calculation, you first calculate what percentage of the total weight that

each delivery represents. Then, you multiply the percentage by the costs.

171


The cost distribution is calculated as follows:

Delivery 1

% of Total Weight = 5000/22000 * 100 = 22.7%

Basic Freight = 5000 * 22.7/100 = 1135.00 USD

BAF = 500 *22.7/100 = 113.50 USD

CAF = -125 USD * 22.7/100 = -28.38 USD

Delivery 2

% of Total Weight = 10000/22000 * 100 = 45.5%

Basic Freight = 5000 * 45.5/100 = 2275.00 USD

BAF = 500 * 45.5/100 = 227.50 USD

CAF = -125 USD * 45.5/100 = -56.88 USD

Delivery 3

% of Total Weight = 7000/22000 * 100 = 31.8%

Basic Freight = 5000 * 31.8% = 1590.00 USD

BAF = 500 * 31.8% = 159.00 USD

CAF = -125 USD * 31.8% = -39.75 USD

172


## Analyze Postings for FSD and Settlement Management

The figure shows the posting for the outbound deliveries. The documents that are

created include financial accounting for the G/L, controlling document for the cost

center-related postings, and profitability analysis.

To check if all amounts and postings are correct, you can access the Service Entry

Sheet of the respective Purchase Order (Step 6a) for the freight costs postings and the

Settlement Management Document for the distributed amounts and postings (Step

6b).

To access the Settlement Doc overview and the accounting documents, in the SAP

Fiori launchpad, go to Settlement → Display Cost Distribution Documents or use the

backend transaction WLFLTM2.

Here you can enter the freight settlement document (FSD) ID and execute.

173


In the Overview of Freight Cost Allocation Documents screen, in the Freight Cost

Allocation Documents section, click the document number to open it.

Review the data in the Basic Data and Flexible Overview tabs.

In the case of cost distribution for an outbound scenario, you can look onto the CO-PA

profitability segment. Here you can monitor the assignment of the distributed costs to

the sales order item and the respective customer assigned to the order. This provides

an overview of the revenue to transportation costs relationship for the respective

order.

In the case of cost distribution for an inbound scenario, the distributed costs get

posted into material valuation and are assigned to the respective order material price

analysis. You can access the detailed distributed amount on material level:

To access the price analysis for the respective material, note the material number

from the Settlement Doc overview and go to transaction MM03. Enter the material

number, click Select View(s) → Accounting 1→enter the plant the material is assigned

to. In the Accounting 1 tab of the material, click the button "Mat. Price Analysis". The

"Prices details view" depicts the overview of the inventory and price development for

the material, which also shows the distributed freight costs of the settlement

document overview.

174


## Lesson 3 - Billing Freight Cost to SD

When you sell your products to a customer, you can also take the responsibility of

delivering these products to that customer. For this, you incur costs for transportation,

for example, through a carrier. You can pass on these costs to your customer.

You use the integration of sales orders and deliveries to facilitate transportation

planning and execution in Transportation Management (TM). The TM component

creates or updates freight units directly for sales orders or deliveries. You plan

transportation for these freight units by creating freight orders that you then

subcontract to the carrier. The freight order determines the freight costs to be paid to

the carrier. You can configure TM to distribute the freight costs in the freight order

according to delivery items. You can then add the distributed costs for each delivery

item to the final amount in the billing document that you send to your customer.

This involves the integration of the following processes:

●  Freight orders in TM

●  Pricing in SD

●  Billing in SD

Transportation costs are now part of the billing document and can be invoiced to the

customer. Details can be checked in the Pricing Elements section while creating the

billing document. Locate the condition type, which lists the freights costs. The amount

175


shown there is equal to the respective amount in the Freight Order under Cost

Distribution > Distribution Items.

The transfer of the freight costs to the SD billing document is achieved via copy

control from the delivery to the billing document using the TM freight order as a

source:

In customizing, chooseSales and Distribution→Billing→Billing Documents→Maintain

Copying Control for Billing Documents.

Furthermore, the pricing procedure has to include a condition type with condition

function FCTM:

In customizing, choose Sales and Distribution→Basic Functions→Pricing

Control→Define Condition Types.

The condition type has to be assigned to the pricing procedure.

In customizing, choose Sales and Distribution→Basic Functions→Pricing

Control→Define and Assign Pricing Procedures.

## Note

You must integrate SD with an internal TM component to be able to include the freight

cost in the billing document for all deliveries of products.

You can only include the freight cost in a billing document when you have one freight

order document for the delivery and the freight order has only one currency in which

you calculate the cost.

176


Unit 6 - Procuring Strategic Freight

## Lesson 1 - Understanding Strategic Freight Procurement

Strategic freight procurement (SFP) is tailored to support (mainly shippers) with the

procurement of long-term transportation services for logistics service providers

(LSPs) or carriers. However, LSPs can also use this scenario to procure transportation

services from carriers while offering transportation services to clients.

## Process Steps

The SFP process is divided into four steps that are depicted in the following figure:

1.  Prepare RFQ:

The shipper prepares the required procurement. There is no interaction with the

carrier. Historic transportation is analyzed and used as a forecast for the next

period. Once the need for procurement is determined, it is divided by the

shipper into different scenarios according to the trade lane, commodity code, or

transportation mode.

It is not necessary to use the SAP TM system for the first stage of the

preparation work. You can use the legacy systems to analyze historic data,

forecast transport volumes, and classify procurement needs.

The final task of the first step is the creation of a central document for the SFP

process, the freight agreement master RFQ. All of the procurement needs and

classifications are entered into the master RFQ.

2.  Submit RFQ:

 The interaction with the carrier is started. The carriers assigned to the SFP

process are added to the master RFQ. If necessary, the target business shares

are assigned among them. If the optional approval is selected within the

purchasing organization, the individual RFQs are created and sent for each

carrier.

3.  Evaluate responses and optimize:

 Once the carriers have responded to the RFQ, the responses are evaluated and

177


compared. SAP TM supports the comparison by creating ranking lists and

suggesting the optimal business shares. You can start negotiation rounds with

the carriers at this stage.

4.  Generate agreements:

The optimal business shares and carriers can be awarded once they are

selected for the next period. Freight agreements are generated by one-click

freight agreement creation when the carriers are awarded in the SFP process. A

freight agreement acts as the contract signed between the shipper and the

carrier.

178


Lesson 2 - Preparing Freight Agreement RFQ Master

## Determination of Procurement Needs

SAP Analytic tools can be used to analyze historic transportation volumes for

determination of procurement needs. The analysis of historic data is helpful when

creating a forecast for the next period.

Transportation Management analytics provide apps, called overview pages that show

the key performance indicators (KPIs) that you must manage your operational

business. At a glance, you can see all the vital data you need for your daily

decision-making. Each overview page displays information from a different area of

TM, for example, freight booking, freight ordering, tendering, business share analysis,

and allocation analysis.

Besides overview pages, analytics provide CDS views. These are query views that are

an SQL queries on the database requesting certain data to be returned. One (or more)

CDS view feeds this information into each overview page (OVP).

You must activate the respective OData service for each Fiori ID of the analytics area

in the Gateway system in order to use this functionality. SAP help provides lists of all

existing analytics areas and technical IDs under the search topic "Analytics".

However, the analysis of historic data and the creation of a forecast are not related to

the freight agreement master RFQ that is created based on this information.

Therefore, the use of SAP analysis tools is not mandatory for the strategic freight

procurement (SFP) process.

## Master RFQ Creation

The central document used in the SFP process is the freight agreement master RFQ. It

contains all of the procurement needs and classifications for the shipper and also

states which carriers are to be included in the process.

179


The freight agreement master RFQ can seem similar to a freight agreement. The

freight agreement master RFQ contains information about the validity period of the

prospective freight agreement.

After assigning carriers and RFQ item details to the document, the RFQ master has to

be approved by the head of the purchasing organization. Therefore, the approval

workflow functionality is integrated. Once the RFQ master document is approved, the

RFQ is submitted to each carrier, creating individual RFQs out of the master RFQ.

## Creating Freight Agreement Master RFQs

The creation of the master RFQ is shown in the following figure. Freight agreement

master RFQs can be created in the following ways:

●  Using an existing freight agreement. This method is used when the same trade

lanes are to be tendered periodically.

●  Creating templates on which new RFQ masters are based.

●  Creating a new RFQ.

●  Copying an existing RFQ.

180


## Master RFQ Versioning

The RFQ master allows versioning, therefore a new version can be created at any

time. The version is copied from the current master RFQ, a new version is created, and

the version counter is incrementally updated. An overview of all of the existing

versions of an RFQ master is located on the Versions tab.

## Note

The currently displayed or edited version is not shown in the version overview.

Several negotiation rounds can be started by choosing Follow up→Create Negotiation

Round. The RFQ can be resubmitted to the carriers for a new negotiation round. The

counter displayed in the RFQ general data is incrementally updated.

## RFQ Header Data

The following RFQ header data is also shown in the figure:

181


●  The RFQ has Valid-From and Valid-To dates, which can be maintained in the

RFQ header.

●  The RFQ Response Deadline date determines the date until which the invited

carriers can respond.

●  The Carrier KPI Profile controls which KPIs are shown on the carrier fact-sheet.

●  The Valid-From and Valid-To dates are related to the validity period of the

resulting freight agreement.

●  The RFQ master can be valid for several purchasing organizations, as well as

multiple carriers. For current carriers, the indicator Incumbent is maintained.

## Master RFQ Items

The carriers are copied from the RFQ header. If the RFQ item is not sent to the specific

carrier, the carrier can be deleted on the item level.

The valid trade lane for the item is specified on the Trade Lanes tab. The logic used for

defining trade lanes in freight agreements is used.

182


The requested capacity is specified in various dimensions on the Capacities tab. TEU

is typically used for ocean transportation.

## Transportation Spend Specifications

The periodicity and the dimension for calculating the transportation spend are

specified, as follows:

●  Capacity driver:

 Specifies the dimensions that you want the system to use to determine the

capacity requirements. If the capacity requirements are available at a granular

level, rather than just at trade lane level, then it is specified at the granular level.

This level is defined in the system using capacity drivers. If one or more scales

in the rate table are marked as capacity drivers, the capacity requirement is

specified for all of the relevant combinations of the scale items in the capacity

drivers.

●  Capacity dimension:

 Specifies the dimension that you use to enter the capacity requirements for an

item in a trade lane.

The valid item is specified for the commodity codes on the Commodity Code tab.

Uploaded notes and attachments are specified on the Notes and Attachments tabs.

The tabs outlined are shown in the following figure.

183


184


Lesson  3  -  Submitting  and  Evaluating  Quotations  and  Award
## Process

## RFQ Carrier Definition

Carriers are maintained on the header level of the freight agreement master RFQ.

However, the exact carriers for each item can be defined again on the item level by

deleting specific carriers from an item. All of the carriers taking part in the strategic

freight procurement (SFP) process must be first maintained on the header level. A

carrier cannot be added on a separate item. The defined carriers are depicted in the

following figure.

If a master RFQ is created from an existing freight agreement, the carriers assigned to

the agreement are flagged as Incumbent. It is preferable to use incumbent carriers in a

response evaluation by the optimizer at a later point.

In the Fiori Launchpad, go to Contract Management→Create Freight Agreement RFQ

Master.

185


## Trade Lane

In SAP TM, the available geographical locations and relations are called trade lanes.

There are several differences between transportation lanes and trade lanes. While

transportation lanes are crucial for optimizer planning and carrier selection, trade

lanes do not influence optimizer planning. Trade lanes are master data that are used

in Trade and Commodity Management (TCM), and sometimes as restrictions for

carrier selections (in the case of allocations). Trade lanes are also important to

analytics.

Trade lanes describe a geographical area or relation. Trade Lanes can include a

defined source and destination (along) or only one defined source or destination (from

or to). The source and destination are exact locations or zones.

## Target Business Shares and Individual RFQs

You can request capacities for each item required. The requested capacities must

represent the total capacities for the item. The capacities can be maintained in the

most common units. Therefore, the requested capacity of the item already resembles

the allocation information, as shown in the figure. At the end of the SFP process,

agreement allocations are created for the items.

186


Contract Management→Create/ Edit Freight Agreement RFQ Master.

## Individual RFQ

Once the freight agreement master RFQ is created and finalized, the agent responsible

for creating the RFQ sends the freight agreement master RFQ to the supervisor of the

purchasing organization for approval. The standard SAP approval workflow is

triggered and the approval task is shown in the supervisor’s SAP Inbox. Once approval

is given, the agent creates individual freight agreement RFQs, as shown in the figure.

Individual freight agreement RFQs contain information from the master RFQ, but only

the information designed for the individual carrier. Therefore, if a carrier is removed

from a response item, the item will not be shown in the individual RFQ.

The agent can review the individual RFQs, which are also visible in the document flow

of the master RFQ. Once the individual RFQs are reviewed, they are published or sent

to the carrier.

187


If no further review of the individual RFQs is required, they are created and published

in one step. This function is enabled by setting the indicator Create & Publish in the

configuration of the RFQ type.

In the Fiori Launchpad, go to Contract Management→Create/ Edit Freight Agreement

RFQ Master.

## Responses to RFQs and Agreement Creation

The carrier can access all the request for quotations (RFQs) submitted by the shipper

in the SAP LBN (Logistics Business Network) if they are provided with an individual

user. The RFQ shows all of the required information in the portal.

The most important part of the RFQ, an Excel sheet, can be shown in the portal. The

Excel workbook contains the following: RFQ header, item, capacity, commodity,

calculation sheet, and rate table information. For every rate table, there is a separate

worksheet for rate table details. The carrier can download the Excel sheet and fill it

with rates. Once this is completed, the Excel sheet can be uploaded to the LBN again,

where SAP TM interprets it and creates the relevant TCM master data.

188


## Evaluation and Freight Agreement Creation

Once the carriers have responded to the RFQ, the responses can be evaluated and

compared. The SAP TM system supports the comparison by creating ranking lists and

suggesting the optimal business shares. Negotiation rounds with carriers can also be

started from here.

Carrier responses are shown in the freight agreement master RFQ as response items

under the request items, as shown in the following figure.

In the Fiori Launchpad, go to Contract Management→Create/ Edit Freight Agreement

RFQ Master.

In the Comparison Cockpit, the response for an individual RFQ or several RFQ items

are compared. You can select the relevant items before navigating to the Comparison

Cockpit, or add more items once the comparison of the initially selected RFQ items is

completed.

There are two possible types of comparisons supported by two sections in the

Comparison Cockpit:

189


●  The transportation manager can use manual response comparison if the

following criteria are met:

○  The only objective is rate minimization without any other constraints.

○  The scenario is simple, for example, the number of carriers responding

to the requirement is much less.

●  The transportation manager uses the automated comparison for the objective

to minimize rates with constraints, such as the following:

○  Minimum or maximum number of carriers

○  Carrier-specific minimum or maximum target shares

○

Incumbents’ minimum or maximum target shares

○  Risk-related constraints

○  Bonus/Malus, historical carrier performance linked to carrier selection:

 The automated comparison uses the carrier selection optimizer, which

proposes the target business shares that are spread across carriers,

bearing in mind the given constraints.

## Response Comparison and Ranking

The rates defined by the carriers are compared and a ranking is shown in the

Comparison Cockpit, as shown in the following figure.

The Response Comparison section of the Comparison Cockpit offers the following

selection options:

●  Select all items: Every item in the column "Select for Comparison is selected.

●  Select matching items: Select a certain item type (for example, pick up

charges) and choose Select Matching Items all pick up charges are selected.

190


## Agreement Generation

Once the optimal business shares and carriers are selected for the next period, they

can be awarded. Awarding the carriers in the SFP process means that freight

agreements are generated for them. Freight agreements act as the contract between

shipper and carrier.

As previously mentioned, agreement allocations are created per carrier while freight

agreements are generated. The generation is based on the requested capacities in the

request item of the master RFQ and the target business share defined for the carrier.

1.  Upon completing the request for quotation (RFQ) and finalization of the

evaluation, choose Create/Update Agreement in the RFQ master.

2.  For each carrier, you can choose to have a new agreement or to update an

existing agreement. Also, you can decide if you want to convert each RFQ item

into a separate agreement.

3.  Upon saving, the freight agreement is shown as a successive Business

Document within the RFQ document flow.

191


## FA RFQ Assignments

A shipper gets a response to a request for quotation from a carrier, which includes the

request for rates in many different segments. Since the responsibilities for those

segments are spread among different purchase organizations or departments, the

freight agreement request for quotation (RFQ) must be distributed to different users,

who should be able to work on the request for quotation at the same time.

The shipper wants to distribute the work on an RFQ to the responsible persons or

departments. The responsible persons or departments want to work on the

preparation and comparisons of the freight agreement RFQ responses at the same

time.

192


The freight agreement RFQ serves as the master document, consolidating all

requested transportation services (that is, items) of the request. After approving and

publishing the master RFQ, the shipper can distribute the items to different users or

organizations by creating an RFQ assignment document for one item of the freight

agreement RFQ master.

To create an RFQ assignment document, you proceed as follows:

●  Within a freight agreement RFQ master, in the Items section, you choose

Create/Update RFQ Assignment.

●  For the chosen RFQ item, a separate freight agreement RFQ master

assignment is created with one transportation requirement item (based on

trade lanes) inside, including a copy of previous responses, as shown in the

figure.

193


## Freight Agreement RFQ Master Assignment Creation

When finishing the work in the RFQ master assignment, the user can transfer the

information to the freight agreement RFQ master document, with a follow-up action

on the RFQ assignment item. The prerequisite for merging an assignment item to the

freight agreement RFQ master is that the item is already approved in the RFQ master

assignment document.

## Note

RFQ assignment documents have the same capabilities as freight agreement RFQ

master documents. However, the publication to the carrier is only possible in the

freight agreement RFQ master document.

194


Lesson  4
## Procurement

-  Understanding  Special  Functions

in  Freight

Optimization and Target Share Strategies

## Optimization and Estimated Spend Simulation

The final result of the strategic freight procurement (SFP) process is the optimal

generation of freight agreements for carriers. It is referred to as optimal generation

because the best business shares are created for the request items. To do so, the

optimizer helps to define optimal business shares. The optimizer proposes target

shares, which are then used to calculate the estimated total spend for each carrier

and each request item.

Spend estimation can be done separately from target share determination. Target

shares can also be manually overwritten to simulate the estimated spend for

individual carriers and request items.

195


Go to Contract Management→Create/ Edit Freight Agreement RFQ Master.

## Target Share Strategies

When using the optimizer for target share calculation, you can define strategies that

restrict optimizer calculations. Strategies contain conditions that define the

restrictions for the optimization, as shown in the following figure.

Enter SPRO in the transaction window, and choose Transportation

Management→Master Data→Agreement RFQs and Quotations→Define Target Share

196


Strategies.

## Condition Parameters

Certain parameters are assigned to a strategy and can be maintained per condition.

Condition Parameters

●

Incumbent:

 This option is selected to indicate that the carrier is incumbent, but is

deselected if the carrier is nonincumbent.

●  Maximum business share:

 Enter the maximum business share given to the carrier.

●  Minimum business share:

 Enter the minimum business share given to the carrier.

●  Maximum number of carriers:

 Enter the number of carriers to get the same maximum business share.

●  Minimum number of carriers:

 Enter the number of carriers to get the same minimum business share.

197


In the RFQ type, you can define whether the optimizer processes one item, or all of the

available items. It specifies the mapping between the agreement type and the freight

agreement RFQ type.

## Target Share Determination and Estimated Spend Simulation

Target share optimization takes rate table values into account by creating a simulated

freight order and calculating its values.

This process can be repeated for many different scenarios, with different Tgt Share

Strategies or conditions.

You can add an additional Target Share Strategy by choosing Insert. The same strategy

is used multiple times, but with different strategy versions. You maintain the strategy

version in order to define different versions, as shown in the previous figure,

Comparison Cockpit: Optimization and Estimated Spend Simulation.

For each strategy, choose Insert→Conditions to add conditions.

As shown in the following figure, Target Shares are calculated for each carrier by

choosing Run Optimizer.

By choosing Simulate Estimate Spend, the system calculates the spend per carrier for

each strategy, as shown in the the figure.

198


Strategy Spend Comparison Graph and Selection of Preferred Strategy

The figure shows a graphical spend comparison graph, which compares the business

shares and total spend between different strategy versions.

The optimization, simulated estimated spend, and graphical strategy spend

comparison are created per RFQ item or for the entire RFQ.

Once the RFQ has been analyzed, you select Accept Preferred Strategy, and the RFQ

status is set to Awarded. The figure shows a selected strategy.

199


## Target Rates in Freight Procurement

A shipper only wants to receive carrier responses within an acceptable range of

values. Outside this range, rates are considered too expensive for a transportation

service. Therefore, the shipper can publish acceptable target rates in the rate tables

and calculation sheet to the carrier when publishing the request for quotation (RFQ).

The carrier can view these defined target rates.

200


## Target Rate Settings

The target rates are shown directly in the Agreement RFQ Calculation Sheet Items

section and in the rate table of the respective item. Here you can enter a target value,

including a tolerance range for every specified charge line item.

## Target Rate Publishing

The target rate specifies the maximum acceptable rate that you have determined for a

transportation service. If you select the Publish Target Rate checkbox, the carrier can

view the target rate when you publish an individual freight agreement RFQ.

In customizing, choose the following: Transportation Management→Master

Data→Agreement RFQs and Quotations→Define Freight Agreement RFQ Types.

201


## Bonus-Malus Functionality

Bonus-Malus is a concept that can influence and optimize the freight procurement

process with the carrier performance data. For example, if the carrier performed well

last year, in the current RFQ cycle, the shipper might like to give this carrier a bonus

and influence the optimizer to give a higher target share to this carrier.

In a case in which the carrier performed badly last year, in the current RFQ cycle, the

shipper might like to give this carrier a malus (or penalty), and influence the optimizer

to give a smaller target share to this carrier.

## Bonus-Malus Functionality

●  With SAP TM, it is possible to influence the target share proposed by the carrier

using carrier performance scores received from the SAP Business Information

Warehouse (SAP BW) system.

●  A flag is available in the Customizing activity target share strategy, which

enables the Bonus-Malus functionality.

202


In customizing, choose Transportation Management→Master Data→Agreement RFQs

and Quotations→Define Target Share Strategies.

Business Add-In (BAdI)

This Business Add-In (BAdI) is used in the freight agreement RFQ (TM-FRA-RFQ)

component. You can use this BAdI to define a logic to reward or penalize a carrier

because of their past performance in a trade lane in the optimizer. When you run the

optimizer, the system takes into account the strategy conditions and other

constraints, and then takes into account the reward or penalty for a carrier from this

BAdI. For example, if a carrier has a history of delays in delivery, you can add 10%

extra cost to the cost a carrier has proposed. This ensures that the carrier is penalized

when you run the optimizer.

This BAdI uses the GET_BONUS_MALUS_VALUE method.

203


## Bonus-Malus Values in Freight RFQ Carrier Section

The values for the Bonus-Malus functionality are taken into account in the optimizer

run for carrier ranking in the comparison cockpit. The Bonus-Malus values influence

the target share of the carriers, and therefore deliver a different position in the carrier

ranking.

Estimated Spend Simulation and Carrier Ranking

204


The figure shows an estimated spend simulation and carrier ranking in the

comparison cockpit.

205


Unit 7 - Managing the Embedded Logistics Service

## Provider Process

Lesson 1 - Understanding the Embedded LSP Process

## Embedded LSP Business Scenarios

Companies are adopting various models to consolidate the transportation (and

logistics) operations within a company to achieve various benefits.

Transportation and Logistics Consolidation Models

●  Strategic reasons

○  Better visibility of transport costs across business units

○  Complete transportation demand visibility

●  Consolidation

○  Higher volume of better rates

○  Centralized handling of goods and logistical operations

●  Standardization

○  Tracking and tracing across companies

○  Document handling and design across companies

## Embedded LSP Scenarios

In the embedded LSP business scenarios, some organizational units take care of the

logistical activities of the group company. These units can either be separate business

units, exclusively managing the transportation activity, or business units that take care

of transportation for their own needs and those of other business units.

This leads to a scenario in which such embedded organizational units must take care

of the settlement with carriers for outsourced transportation, as well as the settlement

with internal business units, billing them for the transportation service provided.

206


You need support for external and internal financial reporting of all such relevant

financial transactions to reflect on the financial statements, such as balance sheet

and profit and loss statements, and other management accounting statements.

## Models for Embedded LSP Scenarios

The main models for embedded LSP scenarios are outlined below:

## Embedded LSP Scenarios: Models

●  Model 1 Exclusive logistics and transportation with own company code

One organizational unit cares for the logistical activities of the group.

●  Model 2 Exclusive logistics and transportation with own company code and

external orders

One organizational unit cares for the logistical activities of the group and

serves for external companies.

●  Model 3 One organizational unit has transportation services, additionally

One organizational unit participates in the core business of the group and cares

for the logistical activities of the group.

207


For the Embedded LSP models shown in the figure, the relevant terminology is as

follows:

●  Group company: A financially and legally independent organizational center that

is not tied to a geographical location and that is registered under business law.

In this example, Super Animal Trading (SAT) is the group company.

●  Company Code: The smallest organizational unit for which a complete,

self-contained set of accounts can be drawn up for the purposes of external

reporting. In this example, SAT 1 (producing pigs), SAT 2 (producing cows), and

SAT 3 (internal LSP) are covered under the group company SAT.

●  ECL stands for "Efficient Cargo Lines", a carrier doing business with SAT3 & 1.

●  EXT is an external company using SAT3 as carrier/ service provider in model 2.

Process Example Group Logistics Model 3

208


Company_C1, Company_C2, and Company_C3 belong to the same enterprise.

Company_C1 manufactures products, but also provides transportation services for

Company_C2 and Company_C3.

Company_C2 and Company_C3 act as internal shipper companies, buying

transportation services from Company_C1. Company_C1 acts as a forwarding house.

It buys transportation services from Logistics_Service_Provider_LSP, and sells

transportation services to Company_C2 and Company_C3.

Transportation Management (TM) creates an order-based transportation requirement

(OTR) or delivery-based transportation requirement (DTR) for each of the sales orders

or deliveries that each company has in place with their respective customers in Sales

and Distribution on an external S/4 HANA or SAP ERP system. Company_C1 then

creates a freight order for the OTRs or DTRs, with itself as the purchasing organization

in TM. It sends the freight order to Logistics_Service_Provider_LSP.

Logistics_Service_Provider_LSP collects the cargo at the warehouse and delivers the

cargo to multiple destinations. The destination locations are geographically close

together. Logistics_Service_Provider_LSP sends an invoice to Company_C1 for the

freight order. Company_C1 pays Logistics_Service_Provider_LSP. Company_C1 uses

the internal settlement process to recover the cost of providing the transportation

service from Company_C2 and Company_C3.

In a group logistics scenario, Company_C1 can create and post internal settlement

documents when the life cycle status of the freight order is In Execution.

To run a group logistics process, you must integrate orders based on orders created in

Sales and Distribution (SD) or Materials Management (MM), and deliveries created in

Logistics Execution (LE) from an external S/4 HANA or SAP ERP system with a TM

component.

209


## Embedded LSP Basic Settings in TM

The Customizing and master data settings that have to be set up and enabled in SAP

TM have already been covered in previous lessons. The relevant internal settlement

settings are described here:

## Prerequisites and Configuration

●  Create the internal settlement document type.

●  Define the shipping type.

●  Define the transportation modes allowed for stage types.

●  Define the stage profile.

●  Define the order-based transportation requirement (OTR) type.

●  Define the freight settlement document type.

●  Define the freight order type.

●  Create settlement profiles for both forwarding and freight settlement.

●  Set up organizational data.

●  Assign the business partner to the organization.

●  Create the calculation profile.

210


●  Create cost distribution methods.

●  Create cost distribution profiles.

●  Assign the created settlement profiles, calculation profile, and distribution

profile to the charges profile assigned to the organizational unit.

Internal settlement document types can be defined.

## Configuration Steps

The steps for embedded LSP configuration are as follows:

●  Assign the settlement profile and calculation profile to the organization unit:

 In Customizing, choose Transportation Management→Basic

Functions→Charge Calculation→Basic Settings→Define Charges Profiles.

●  Create the internal settlement document type:

 In Customizing, choose Transportation Management→Settlement→Forwarding

Settlement→Define Forwarding Settlement Document Types.

●  Create an internal agreement:

 In the SAP Fiori launchpad, choose Contract Management→Create Internal

Agreement.

●  Enable the freight order (FO) or freight booking (FB) type for cost distribution:

 In Customizing, choose Transportation Management→Freight Order

Management→Define Freight Order Types.

●  Specify the purchasing organization of the freight order or freight booking that

is executing the stage as a forwarding house:

 In transaction PPOME, choose your Purchase Organization→tab Org.

Data→Field Org. Unit Function: Forwarding House.

These steps are common to setting up both intracompany and intercompany

settlements.

By default, the SAP TM system creates an intercompany settlement document for

organizations that belong to different company codes. If you want to use an

intracompany settlement for a company organization, you must select the

211


Intracompany Settlement checkbox in the Org. Data tab page of the relevant

organization structure. You can access the structure using transaction PPOME.

## Note

The further and detailed Forwarding Settlement integration settings to SAP SD, as well

as the intercompany settlement process and the LSP-based Cost Distribution, are

covered in the respective LSP-based TM courses.

212
