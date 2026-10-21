S4TM2 - Planning and Execution in
## SAP S/4HANA TM

Unit 1 - End-to-End Transportation Process

Unit 2 - Transportation Management Master Data

Unit 3 - Creation of Transportation Requirements

Unit 4 - Transportation Planning Preparation

Unit 5 - Interactive Transportation Planning

Unit 6 - Automatic Transportation Planning

Unit 7 - Subcontracting, Load Planning, and Short-Cut-Process

Unit 8 - Transportation Execution

2-5

6-40

41-88

89-114

115-131

132-148

149-173

174-210

1


Unit 1 - Transportation Management Overview

Lesson 1 - End-to-End Transportation Process

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

Integrated  Sales  Order  and  Delivery  Process:  Sales  order  and  delivery

processes as well as transportation management are handled inside the same

instance/system.  Logistics  business  documents  derived  from  Sales  and

2


Distribution (SD), Materials Management (MM), or those generated in Logistics

Execution  (LE)  serve  as  the  source  for  transportation  requirements  and

planning.

●  Decentralized  Sales  Order  and  Delivery  Process:  Sales  orders and delivery are

handled  in  one  instance/system  and  transportation management is done in a

separate

instance/system.

Order-based

transportation

requests

(OTR)/delivery-based  transportation (DTR) request represents a transportation

demand based on an order/delivery that was created in an SAP S/4HANA ERP

system.  In  this  scenario,  the  order-based  transportation  requirement  or

delivery-based

transportation

requirement  serve  as

the  source

for

transportation requirements and planning.

For  LSPs,  forwarding  order/forwarding  quotations  serve  as  the  source  for

transportation requirements and planning.

All  the  above-mentioned  documents  serve  as  the  source  for  transportation

requirements  and  planning.  The  data  from  these  source  documents  is  used  to

generate  the  Freight  unit.  The  business  document  data, with the freight unit building

rules, form the basis for building a freight unit. A freight unit represents a collection of

goods that can be transported throughout the complete transportation process chain.

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

transportation  cockpit  can  tailor  its  interface  to  suit  the  specific  planning  scenario

being  undertaken.  This  includes  options  like  map-based  planning,  Gantt  chart

3


planning, drag-and-drop functionality, load planning, and command-based planning, all

of which can be executed seamlessly within the transportation cockpit.

Carrier  selection  can  be  undertaken  either  during  the  planning process or afterward.

Carrier  selection  can  be  executed  through  multiple  methods.  It  can  be  carried  out

manually,  using  optimization algorithms, or via a tendering process. The primary aim

of  carrier  selection  is  to  establish  a  ranked  list  of  carriers  eligible  to  fulfill a planned

freight  order.  This  selection  process  considers  various  constraints  such  as  costs,

priorities,  incompatibilities,  and  business  allocations.  The  tendering  process  can

function  as  an  integral  part  of  carrier  selection or operate as a distinct and separate

process.  Within  the  tendering  process, freight orders are proffered to eligible carriers

through a tendering or auction procedure.

Transportation execution encompasses a comprehensive range of activities related to

the  management  and  documentation  of  shipments  during  their  transit.  The  freight

order serves as the foundation of the execution process, providing precise details and

actual  quantities  of  the  cargo  being  transported.  Any  discrepancies  arising  between

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

these  charge  elements  within  the  calculation  sheet  and  calculates  correct  fees  for

customers or suppliers. The outcomes of these calculations are recorded in either the

forwarding order for customer invoices or the freight order for supplier invoices.

4


From  the  forwarding  order  and  freight  order,  draft  invoices  can  be  created  for

settlement  integration  to  the  SAP  S/4HANA  ERP.  To  create  customer  invoices,

forwarding settlement documents are created from the forwarding order and then are

sent  to  ERP  to  create  a  billing  document.  For  supplier  invoice  settlement,  freight

settlement  documents  are  created  from  the freight order and are then transferred to

ERP  to  create  accruals  and  later  to  create  a  purchase  order  and service entry sheet

(SES) for invoice verification or self-billing.

Within  the  SAP  S/4HANA  TM  system,  a  range  of  overview  pages,  reports,  and  KPI

dashboards  have  been  created  that  are  relevant  for  shippers  and  logistic  service

providers.  These  overview  pages  provide  a  consolidated  view  of  all  data  from

day-to-day  activities  and  help  in  real  time  decision-making.  These  pages  can  be

tailored to business roles, users who supervise transportation execution can start their

day by navigating to the freight order execution overview.

5


Unit 2 - Transportation Management Master Data

## Lesson 1 - Business Partners

The  master  data  of  customers  and  vendors  is  managed  in  SAP  S/4HANA  by  using

business  partner  master  data.  By  using  this  approach,  it  is  possible  to  centrally

maintain  the  master  data  for  customers  and  vendors  (in  SAP  ERP  they  have  been

handled separately).

Business partner master data can be maintained with the transaction BP or by using a

corresponding app from the SAP Fiori launchpad. Business partners can be assigned

multiple company codes. Business partners can be categorized as a person, group, or

organization. An organization represents units such as a company, a department of a

company,  or  an  association.  Organization  is  an  umbrella  term  to  map  every  kind  of

situation  in  the  day-to-day  business  activities.  A  group  represents  a  shared  living

arrangement, a married couple, or an executive board.

6


The  link  between  a  business  partner  and  other  components  is  achieved  by  a  role

concept.  A  business  partner  role  corresponds  to  a  business  context  in  which  a

business  partner  can  appear.  Relevant  business  partner  roles  related  to  shipping

process are:

●  Business Partner general (000000)

●  Customer (FLCU01)

●  FI customer (FLCU00)

●  Vendor (FLVN01)

●  FI vendor (FLVN00)

●

Invoicing Party (BBP006)

●  Carrier (CRM010)

This ensures that the relevant master data for the various processes can be recorded

correspondingly  and that the business partner can be used for the relevant functions

(such as sold-to party).

You define the general business partner data once and assign business partner roles

(BP  roles)  to  the  business  partner.  Specific  data  is  stored  for  each business partner

role.  In  this  way,  you  do  not  store  redundant  data,  since  the  general  data  is

independent of a business partner’s function or application-specific extensions. When

7


you first create a business partner in the system, the BP role General Business Partner

is automatically assigned to the business partner.

Assigning partner functions in the SAP system determines the functions of particular

partners in the process. A partner function is a particular role that a business partner

can  take  during  the  process.  For  example,  one  customer  orders  some  products

(partner  function:  sold-to-party  and  another  customer  receives  the  material  (partner

function: Ship-to-party). One partner can have several functions. For example, when all

the  partner  functions  within  the customer partner type are assigned to one business

partner, the same customer is the sold-to-party, ship-to-party, payer, and bill-to-party.

The following is a list of partner functions commonly used in the shipping process:

●  Consignee

●  Bill-to-party

●  Carrier

●  Shipper

●  Ordering party

●  Driver

●  Payer

●  Freight forwarder

8


Additional  text  can  be defined for the business partner master data and you can use

them as the printing address. The same business partner number can be maintained

across multiple company codes.

Drivers:  Drivers  operate  vehicles.  They  are  defined  as  business  partner  with  the  role

driver.  Attributes  like  driver  qualifications,  shift  sequence,  validity  period,  home

location, and absences can be maintained.

## Business Partner Determination

The  system  can  be  enabled  to  determine  business  partners  for  various  document

types. This allows users to easily and efficiently enter business partners in a business

document.  It  cuts  down  on  the  chance  of  manual  errors,  and  reduces  the  need  to

enter a business partner for each partner function.

In  Customizing  for  Transportation  Management  under  Master  Data→Business

Partners→Define  Partner  Determination  Profiles,  you  can  create  a  partner

determination  profile  that  the  system  uses  to  automatically  determine  the  following

features:

●  The partner functions available in a business document

You  specify  the  list  of  partner  functions  that  the  system makes available in a

business document.

●  The level of control the user has in entering the partner function

Depending  on  the  settings  you  define  in  Customizing,  you  change  or delete a

partner  function,  or  add  a  partner  function  from  a  list  of  available  partner

functions.  You  can  also  specify  settings  so  that  you  cannot  change or delete

specific partner functions.

●  How the system determines business partners for the partner functions

9


The system uses one of the following relationships that you specify in Customizing, to

determine a business partner:

●  Partner function and source partner function

In  Customizing,  you  can  specify  a  source  partner  function  for  a  particular

partner  function.  In  the  application,  when  you  enter  a  business  partner  in the

field  that  you  have  specified  as  the  source  partner  function,  the  system

automatically copies the business partner to the associated partner function.

For  example,  in  Customizing,  you  specify  the  partner  function  as  Invoicing

Party,  the  source type as Partner Function, and the source function as Sold-to

Party.  In  the  application,  you  specify  the  sold-to  party  as  Customer01.  The

system assigns Customer01 as the business partner for the invoicing party.

●  Partner  function  and  the  source  partner  function  in  business  partner  master

data

The system uses the settings that you specify on the Partner Function tab page

in  the  BP–Maintain  Business  Partner  transaction  to  determine  a  business

partner in a business document.

For  example,  you  are  a  logistics  service  provider  (LSP),  and  you  have  a

business partner APP_1. In the BP–Maintain Business Partner transaction, you

specify APP_1 with the BP role of FLCU01 (Customer). On the Partner Function

tab  page  of  the  BP  transaction  for  APP_1,  you  specify  an  organizational  unit

and  a  partner  function  for  the  business  partner  APP_INV.  APP_INV fulfills the

10


role  of  invoicing  party  for  APP_1.  In  Customizing,  you  specify  the  partner

function as Invoicing Party, the source type as BP Relationship, and the source

role as Sold-to Party.

In  a  forwarding  order,  you  specify  the  organization  as  561234  on the General

Data  tab  page  and  the  sold-to  party  as  APP_1  on  the  Business  Partner  tab

page.  The system checks the business partner master data for APP_1. On the

Partner  Function  tab  page,  it  finds  that  APP_1  uses  APP_INV as the invoicing

party  for  organization 561234. It assigns APP_INV as the business partner for

the invoicing party.

●  Partner function and business partner

In Customizing, you directly assign a business partner to a partner function. In

the  application,  the  system  automatically assigns this business partner to the

partner function.

For  example,  in  Customizing,  you  specify  the  partner  function  as  Invoicing

Party,  the  source  type  as  Business  Partner,  and  the  business  partner  as

CSI_CARR1.  The  system  automatically  assigns  CSI_CARR1  as  the  business

partner for the invoicing party in the application.

Note  that  you  can  enter  a  business  partner  that  does  not  exist  in the current

system. This enables you to assign a business partner to a partner function in

one  system  and  transport  it  to  another  system  where  the  business  partner

exists.  For  example,  in  a  Customizing  system,  you  have  not  defined  any

business  partner  master  data.  You  have  assigned  business  partner  LUF  to  a

partner  function  of  carrier.  You  transport  this  data  to  a  production  system

where  LUF  is  defined.  In  a  business  document  of  the  production  system,  the

system determines that the business partner for the carrier is LUF.

●  Relationship category

The  system  can  determine  the  business  partner  for  a  partner  function based

on  the  partner  relationship  you  specify  in  the  Maintain  Business  Partner

transaction (transaction BP).

You  can  assign  the  business  partner  determination  profile  to  the following business

document types:

11


●  Forwarding orders

●  Forwarding quotations

●  Forwarding settlement documents

●  Freight orders

●  Freight bookings

●  Freight settlement documents

●  Freight agreement RFQs

●  Forwarding agreement quotations

●  Freight agreements

●  Forwarding agreements

●

Internal agreements

●  Mutual agreements

12


Lesson 2 - Transportation Network

## Location Master

A location is a logical or physical place in which resources are managed on a quantity

basis.  This  business  object  is  used  as  the  basis  for  the  transportation  processes  in

which  you  name  a  source  location,  a  destination  location,  and  any  transshipment

locations necessary to complete it.

Different  customizing  entries  and  master  data  elements  from  SAP  S/4HANA  are

displayed  in SAP TM as locations with different location types. SAP S/4HANA plants,

customers, vendors, and shipping points are integrated with SAP TM and become the

following  types  of  location:  Plants-1001  (production  plant)  or  1002  (distribution

center),  Business  Partners-  1021  (business  partners),  and  Shipping  Points-1003

(shipping point). The following location types exist:

ID

Location Type

1001

Production Plant

1002

Distribution Center

1003

Shipping Point

1021

Business Partner

1030

Terminal

1040

Store

13


1100

Port

1110

Airport

1120

Railway Station

1130

Container Freight Station

1140

Hub

1150

Gateway

1160

Container yard

1170

Warehouse

1180

Carrier Warehouse

1190

Rail Junction

1191

## Border Crossing Point

If you are using SAP TM in SAP S/4HANA, no integration is required–material master

and business partners are already available. Location master data is created on the fly

or via a report when needed. In traditional SAP TM 9.6 deployment, the location type is

automatically  determined  based on the object being transferred from SAP S/4HANA.

In the SAP S/4HANA system, each inventory-relevant location can be assigned to one

or  more  shipping  points.  A  shipping  point  is  an  independent  organizational  unit at a

fixed  location  that  processes  and  monitors  inbound  and  outbound  deliveries.  The

physical address of a shipping point is represented as a location in the master data.

14


Transshipment  locations  are  used  for  unloading  goods  from  one  freight  order  and

loading  them  onto  another  freight  order  during  the  transportation  process.  This

function  is  necessary  when  different  means  of  transport  or  different  transportation

service  providers  (carriers)  have  to  be  used  to  execute  a  transportation  process, for

example, truck-ocean-truck; truck-rail-truck. Transshipment locations can also be used

when consolidating or deconsolidating goods to be transported.

## Geocoding Locations

Locations  are  critical  elements  of  your  transportation network, because they identify

source and destination points. Based on where these two points are located, SAP TM

can use distance and duration to calculate the best means of transporting a product.

## Geographical

information  plays  an  important  role  in  TM.  Almost  all  business

processes  relate  to  it.  High-quality  geodata  improves  these  processes.  The  SAP TM

Transportation Network is the foundation of a transportation planning process.

To see geographic information related to location master data, log into SAP Fiori, then

choose Master Data folder→Define Location.

A location is a specific point on the earth's surface that is defined by the geographical

coordinates  of  longitude,  latitude,  and  altitude.  These  coordinates  are  determined

from the address data of a location. An address can contain a country, region, postal

code,  city,  district, street, and house number, as well as additional fields. Determining

15


geographical  coordinates  from  address  data  is  called  geo-coding.  A  geographical

information system can be used to get precise geographical coordinates.

In  SAP  TM,  the  location  master  data  object  describes  the  geographical setup of the

transportation network underlying business processes. Location can store an address

and  the  geographical  coordinates  that  define  its  position.  The  accuracy  of  the

geo-coordinates  depends  on  the  address data provided and which service is used to

determine them.

Standard  SAP  applications  automatically  determine  a  geo-coordinate  at  region  level

when  creating  or changing the location address data. This is sufficient for processes

not working with static information or depending on distances, times, or map display.

Because  geo-coordinates  are  the  basis  for  distance  and  duration  determination  and

map display, they must be high quality in case those functions are required.

Geo-coordinates  are  displayed  in  degrees,  minutes,  and  seconds in the Geographical

Data area of the Location user interface and can be overwritten manually by the user.

The Precision field indicates the granularity of the geo-coding result.

A  geocoder  determines  the  geographical  coordinates  (longitude and latitude) from a

given address. The following two levels of geocoding are possible in SAP TM:

1.  Standard (included in the SAP TM software license)

2.  Full addresses (depending on capabilities of geocoding software)

The geocoding program supplied by SAP determines the longitude and latitude based

on the country and region code. There are several companies who provide geocoding

products,  including  the  following:  Google,  Here,  Rand-McNally,  PC-Miler,  and  PTV

(Karlsruhe, Germany).

## Transportation Zone

Transportation  zones  are  used  to  group individual locations. All the properties of the

zones  are  transferred  to  its  locations.  Transportation zones are typically used as the

origin and destination points for transportation lanes. Transportation zones reduce the

effort  needed  to  model  the  geographic  network  in  planning.  Grouping  locations  into

transportation  zones  reduces  the  volume  of  master  data  in  the  TM  system.

16


Transportation  zones  can  group  locations  and  can  include  one-time  locations.

Transportation  zones  can  include  zones  within  their  locations  and  subzones.  For

example,  all  locations  that  are  supplied  by the same warehouse (individual locations

and transportation zones) are grouped into a transportation zone.

If  SAP  S/4HANA  integration  through  the  DRF  is  used,  transportation  zones  are

automatically  created  from  the address of the location. The location is automatically

assigned to the transportation zone.

Transportation zones are not physical locations and therefore do not have an address.

Transportation  zones can also be assigned geographical coordinates. SAP TM offers

two options for calculating these coordinates. After defining the locations, regions, or

postal  codes,  the  system  can  calculate  the  coordinates.  This  estimates  the  center

point  of  the  zone  based  on  the  coordinates  of  all  locations  included  in  the  zone.

Alternatively,  identify  the  geographical  coordinates  and  manually  enter  them  in  SAP

TM.

## Transportation Zone Types

●  Region:  In  a  regional  zone,  locations  are  specified  by  a  country  or region. For

example,  the  state  of  Illinois  can be defined as its own zone. In the figure, the

zone US-Illinois is created and only Illinois is assigned to it.

17


●  Postal Codes: Transportation zones can be defined by the use of postal codes.

Companies can use zip/postal codes or zip/postal code ranges to define these

geographical  areas.  Most  major  U.S.  truck-load  and  less-than-truck-load

carriers publish their rate structures and transit time tables based on origin and

destination  three-digit  zip  code  lanes  rather  than  city  or  state  level  lanes.  In

these documents, carriers use ranges of three-digit zip codes, such as 170-173.

●  Direct:  In  a  direct  assignment,  locations  are  assigned  directly  to  a  zone.  For

example,  a  particular  customer  might  be  in  a  zone  that  has  low  volumes.  By

including  them  in  a  zone  with  a  larger  geography,  you  might  improve  the

optimization results.

●  Mixed:  You  can  use  any  combination  of  these  types  of  transportation  zones

when defining a zone. This is a called a mixed zone.

## Transportation Zone Hierarchy

Organizing  transportation  zones  into  transportation  zone  hierarchies  allows  you  to

transfer the properties of the higher-level transportation zone to the locations on lower

levels  of  the  hierarchy. You cannot assign a transportation zone to itself or to a zone

already assigned to the same zone.

Transportation  zone  hierarchies  reduce  the  amount of master data to be maintained

in SAP TM:

18


●  A zone can be assigned to any number of higher-level zones

●  Locations can be assigned to any number of zones

●  A zone cannot be assigned to a location

## Transportation Zone Hierarchy Definition

Transportation  zone  hierarchies  can  include  locations  and  transportation  zones.  To

see  the  zone  hierarchy,  log  into  SAP  Fiori,  then  choose  Master  Data  folder→Define

Zone Hierarchy.

19


Transportation and Trade Lane

## Transportation

lanes  represent  the  relationship  between  two

locations,  two

transportation  zones,  or  a  combination  of  locations  and  transportation  zones  that

expresses  the  direct  approachability  of  the  locations,  or  of  all  locations,  within  the

transportation zones for a specific means of transport (MTr).

Using  transportation  zones  as  the  source,  destination,  or both, considerably reduces

the number of transportation lanes to maintain.

A transportation lane points only in one direction. To model the reverse direction, you

must create another transportation lane.

## Trade Lane

A  trade  lane  can  have  a  mode  of  transport  and  means  of  transport.  The  trade  lane

defines a direction for transportation, which is characterized by the orientation, source,

and  destination.  Possible  orientations  are:  Inbound,  Outbound,  From,  To,  Within  and

Along.

A  trade  lane  is  an  abstract  representation  of  transport  classification.  A  trade  lane

instance does not represent a connection between any transportation network nodes

(zone/location,  and  so  on),

it

is  a  context-independent  classification  of  any

transportation-related activities.

Trade  lanes  can  build  up  a  hierarchy,  that  is,  more  generic  trade  lanes  imply  more

specific  trade  lanes  (for  example:  "Within  Germany  using  means  of  transport  Truck"

20


implies "Along from Frankfurt to Hamburg using means of transport Chilled Truck" and

"Within Bavaria using means of transport Truck for liquids").

Trade lanes can overlap each other (for example, "From Germany using Airplane" and

"Within  Europe  using  Airplane").  Trade  lane  hierarchies  include  transportation  zone

hierarchy  (for  example:  "From  Germany"  implies "From Bavaria", which implies "From

Plant_Munich"), means of transport hierarchy (for example: "Within Germany with Mtr

Truck"

implies

"Within  Germany  with  Mtr  Chilled_Truck")  and  means  of

transport–mode  of  transport  relations  (for  example:  "Within  Germany  with  Mode  of

Transport Road" implies "Within Germany with Mtr Chilled_truck").

There is no direct link between trade lane and transportation lane.

Methods of Transportation

## Transportation Mode

When  all  shipping  and  receiving  locations  are  defined,  frame  how you intend to ship

products  between  these  locations.  The  complexity  of  your  shipping  scenarios

influences how much detail you must maintain.

For example, consider whether products are shipped over road, rail, or waterways.

21


The  first  configuration  step

in  the  transportation  process

is  to

identify  the

transportation  modes  that  can  be  used  to  move  products.  The transportation mode

describes the highest-level transport grouping, for example, road, rail, inland waterway,

sea, or air. Each method of transport is assigned a single transportation mode.

## Transportation Mode Categories

SAP  transportation  mode  categories  are  road,  rail,  sea, air, postal service, and inland

waterways.

In  addition  to  the  transportation  mode  category, companies can assign a dangerous

goods  transport  category.  This  signals  that  you  may  have  to  ship  certain chemicals

under  pressure and only certain ways of transporting the product are suitable. These

categories define the type of transport to be used. Category 99 (all modes) is used in

the  U.S.  according  to  dangerous  goods  regulation  49  CFR.  Customers  can  use

categories 30–89 for their own definition.

## The Main Carriage

The  transportation  mode  can  be set as the Main Carriage. The reference to the main

carriage  indicates  that  this  segment  of transportation is the primary segment. When

22


dealing  with  export  scenarios,  you  can  have  the  precarriage,  main  carriage,  and

on-carriage. In a multimodal or multistage shipment, the main carriage stage contains

all of the shipment documents. It also allows pre- and on-carriage stages to be linked

to it.

These transportation modes can be used at a high level to determine incompatibilities.

When  you  define  the various transportation modes, your company can further define

the  transportation  process  by  creating  and  assigning  different  means  of  transport.

The  means  of  transport  describes  the  characteristics  of  specific  vehicle  types  or

classifications  that  transport  goods,  such  as  a  nonrefrigerated  truck,  a  refrigerated

truck, a 60-foot rail boxcar, or a bulk container.

## Assigning Vehicle Resources to a Means of Transport

The  network can be expanded by defining vehicle resources and assigning them to a

means of transport. Vehicle resources in a means of transport have a common set of

physical  characteristics  that  are  taken  into  account  during  the  planning  process.

These physical characteristics include the mode of transportation (air, rail, surface, or

sea),  vehicle  capacity,  speed,  cost  structure,  geographic  availability, and temperature

23


control. Whether a company-owned fleet can be used to group vehicles in a means of

transport is also a consideration.

Means  of  transport  also  allow  a  company  to  describe  the  cost  structure  and

geographical availability of a class of vehicle.

## Means of Transport Settings

There are various means of transport settings:

●  Transportation mode

●  Multi-resource

●  Scheduled means of transport

●  Own means of transport

●  GIS quality

## Means of Transport Definition

You can define the means of transport in Customizing for SAP TM.

Choose  Transportation  Management→Master  data→Resources→Define  Means  of

Transport and Compartment→Define Means of Transport.

## Transportation Mode Assignment

Within  the  means  of  transport,  you can assign a transportation mode. This specifies

how a product is transported, for example, by road, rail, sea, or air. You use the means

of transport to select the vehicle resources that are to execute the transportation.

The  standard  code  assigned  to  the  means  of  transport  represents  the  official

representation of the type of transport. The UN/EDIFACT standard uses the following

codes:

●  006 - Aircraft

●  011 - Ship

●  031 - Truck

●  038 - Car

The relevant settings are:

24


●  Scheduled means of transport: This defines if a resource is traveling based on

a fixed schedule such as a sailing or rail schedule.

●  Own means of transport: This determines if a resource is part of your own fleet

or that of an external provider.

## Multi-Resource

Instead  of  creating  individual  resources  for  a means of transport, you can select the

Multi-Resource  checkbox  for  the  means  of  transport.  During  planning,  the  system

assumes the availability of the number of resources you define. If you do not specify a

number  in  this  field,  the  system assumes that an unlimited number of resources are

available. During vehicle scheduling and preprocessing, the number of resources that

you  define  in  this  field  indicates  the  maximum  number  of parallel freight orders that

the system is allowed to create for each resource.

Duration

25


Duration is one of the key elements to consider when dealing with different means of

transport. This can be influenced by the type of transport as well as the quality or type

of  transportation  infrastructure  used. Selecting the GIS Quality checkbox means your

organization  is  integrating  with  a  third  party  geographical  information  system.  This

integration  is  specific  about  which  routes  (interstate  highways  or  county  roads)  are

used.  Anticipated  speeds  for  the  different  types  of  highways  or  roads  that  are  used

can be defined.

Distance and Speed

26


If  you  choose  not  to integrate with a GIS, you still differentiate durations for different

means  of  transport.  Within  each  means  of  transport,  you  can  specify  an  average

speed.  The  speed  is  then used, along with the distance from the transportation lane,

to calculate the transit duration.

The  distance  factor  establishes  the  difference  between  the  linear  distance  between

the  two locations and the actual distance covered by the vehicle. Based on the linear

distance,  you  can  use  this  factor  to  estimate  the  actual  travel  distance  for a vehicle

between  two  locations.  Together  with  the  average  speed,  you  can  estimate  the

transportation time.

## How to Use the Path Finder

Scenario  building  can  be  time-consuming.  Scenario  validation,  especially  for

transportation  optimization,

is  even  more  time  consuming.  The  planner  must

establish  if  all  elements  of  the  transportation  network  are  maintained  correctly  to

enable the optimizer to find a valid solution.

You can use the path finder function to search for legs in your transportation network

and take the following considerations into account during the process:

●  Locations

●  Transshipment locations

27


●  Transportation lanes

●  Schedules

●  Transportation zones

The path finder enables you to easily determine whether a connection exists between

two locations and, therefore, whether you have correctly configured your master data.

However, the path finder does not take incompatibilities into consideration.

## Path Finder Execution

You  can  execute  the  path  finder  and  check  the  result  in  either  the  transportation

network cockpit or on the transportation proposals user interface.

●  Transportation Network Cockpit:

When  you  open  the  context  menu for a location in the transportation network

cockpit,  you  can  choose  Find  Path  To  Location  and  enter  a  destination  in  the

displayed  dialog  box.  The  system  then  calculates  all  of  the  available

connections  in the transportation network and displays them on the map. The

color  of  the  connections  indicates  whether  a  valid  transportation  lane  or

schedule exists.

●  Transportation Proposals:

When  you call the user interface for transportation proposals, you can choose

the  appropriate  button  to  show  or  hide the available connections on the map.

As in the transportation network cockpit, the color of the connections indicates

whether a valid transportation lane or schedule exists.

●  Explanation Tool:

When you select one or more freight units, you can choose Show Network Path

to  analyze  the  underlying  transportation  network  that  is  taken  into  account

when planning the selected freight units.

●  Requests

○  Source location

○  Destination location

●  Options

○  Determine path

○  Determine connections

28


●  Restrictions

○  Outbound, inbound, or implicit hub

○  Transportation mode

○  Means of transport

## Path Finder Report: /SCMTMS/FIND_TN_PATH
The  required  input  for  the  tool  is  a  start  and  a  destination  location.  Using  assigned

transshipment  locations  and  existing  connections  (transportation  lanes,  schedules,

and  booking),  the  path  finder  tries  to  find  all  paths.  The  result  indicates  if  there  is a

valid connection or not (all existing are listed) for each stage of a path. It is thus easy

to  find  out  if you have assigned a transshipment location, but if it cannot be reached

from your start location.

The  report  has  some  limitations.  For  example,  it  is  not  possible  to  search  within  a

certain  timeframe  and  respect  the  validity  of  the  connections.  Also,  transportation

mode  and  means-of-transport  filters  are  not  available  and  incompatibilities  are  not

considered.

29


Lesson 3 - Transportation Resources

## Resources Overview

Resources  play  a  central  role  in  planning  and  execution  within  SAP  Transportation

Management.  Resource  data  is  relevant  to  the  planning  of  order  dates,  taking  into

account  working  times  and  the  available  capacities  of  the  resources.  Resources,  in

conjunction  with  booking,  offer  the  capacity  needed  to  perform  transportation

activities on freight units, such as transportation, loading, and unloading activities.

The following resource types exist:

●  Vehicle Resource

●  Handling Resource

●  Calendar Resource

●  Transportation Unit Resource

Goods are loaded onto and unloaded from vehicles and transportation units resource

and  transported  around  the  transportation  network.  Calendar  resources  specify

operating  hours  for  a  location,  during  which  goods  maybe  dropped  off  or  picked up

from  this  location.  Handling  resources  offers  a  handling  capacity  that  allows  the

goods to be loaded or unloaded from vehicle resources.

Vehicle Resource

30


Vehicles  are  moving  resources  that  transport goods between locations, for example,

trucks,  rail-cars,  planes,  and  ships.  Each  vehicle  resource  represents  a  unit  load,  for

example,  one  trailer  of  a  certain  capacity,  one container of a certain capacity, or one

rail car of a certain capacity. Eight dimensions and unit of measurements can be used

to define vehicle capacity, for example, mass, volume–that is, the capacity of a trailer

can be specified as 40,000 lb, or 2200 cu ft/s, or 24 pallets. Planning can only take the

vehicle  capacity

into  account

if  these  dimensions  and  unit  of  measurement

correspond to the dimensions and unit of measurements that are defined in a freight

unit building rule.

Vehicle group and vehicle types specify attributes such as the physical properties of a

certain kind of vehicle.

All  vehicles  are  assigned  to a means of transport (transportation method). Means of

transport are groups of vehicle resources. The transportation mode is assigned to the

means  of  transport.  The  transportation  mode  specifies  how  the  goods  are

transported, for example, as a sea shipment.

There are two types of vehicle resources: passive and active. Active vehicle resources

can  travel  by  themselves.  Passive  vehicle  resources  cannot  travel  by  themselves.  A

truck  that  has  a  motor  and can travel by itself is an active resource. An empty trailer

with no tractor is a passive resource.

31


The  means  of  transport  and  factory  calendar  should  be  defined  before  creating  a

vehicle  resource.  When  creating  a  vehicle  resource,  it  is  recommended  that  the

following information is input:

●  A resource name

●  A calendar and time zone

●  A capacity

The  following  fields  combined  together  define  capacity  and  volume  and  are

mandatory for creating a resource:

●  Factory Calendar

●  Continuous Dimension

●  Capacity

●  Unit of Measure

MTr  combinations  can  be  used  to  model  truck  and  trailer  combinations.

Multiresources can be used to model an external fleet in one step.

32


## Compartments

Compartments  can  be  used  to  indicate a division of the vehicle resource (truck) and

also  the  trailer

into  smaller  units.  Capacity  constraints  can  be  specified  for

compartments. Furthermore, they offer the following benefits:

●  Flexible and fixed compartments

●

Incompatibilities  can  be  used  to  restrict  certain  freight  units  from  being

transported  in  certain  compartments,  for  example,  because  of  temperature

restrictions

The  use  of  compartments allows you to assign dangerous goods to certain areas of

the  truck.  In  addition, the use of compartments improves transportation planning for

oil and gas, chemical, retail, and consumer products.

## Means of Transport Combinations

A means of transport combination is an instance of a particular means of transport, or

a  group  of  identical  instances  of  means  of transport that can provide transportation

services. You use this business object to map the capacity and availability of vehicles

that you want to use for transportation.

MTr combinations have the following attributes:

●  They can be used to model a truck and trailer combination.

●  You specify the number of the objects of each MTr within the combination, for

example, one truck and two trailers.

●  You specify capacities (several UoM): Maximum capacities of the combination.

●  Additional  (freely  definable)  attributes  can  be  used  for  compatibilities  and

incompatibilities; based on a customizable attribute definition (code + text).

●  Coupling/un-coupling durations are defined per passive MTr.

## Handling Resource

Handling  resources  are  used  for  handling  transportation  orders  at  a  location.  The

handling  resource  offers  handling  capacity  that  allows  the  goods  to  be  loaded  onto

and  unloaded  from  a  vehicle  resource,  for  example,  door,  loading  ramp,  or  forklift.

33


Handling  resources  maintain  downtimes,  restrictions  on  simultaneous  activities,

resource availability, qualification, and equipment requirements.

Availability times can be maintained by defining capacity variants and shift sequences.

Consumed capacity per loading and unloading operation is maintained in the location

master  data  with  the  assignment  of  the  (means  of  transport-specific)  handling

resource. The available capacity is maintained in the resource master data record.

## Calendar Resource

Calendar  resources  determine  the  operating  hours  of

locations.  Loading  and

unloading  activities  can  only  take  place  during  operating  hours.  Calendar  resources

are defined as resources and can be assigned to multiple locations as:

●

Inbound operating hours

●  Outbound operating hours

●  Means-of-transport specific operating hours (inbound)

●  Means-of-transport specific operating hours (outbound)

Availability times can be maintained by defining capacity variants and shift sequences.

## Transportation Unit Resource

For  an  instance  of  a  particular  transportation  unit,  such  as  a  container, you can use

the  transportation unit resource to map the capacity and availability that you want to

use for transportation.

You  can  choose  up  to  eight  dimensions  and  units  of  measurement  to  describe  the

capacity. Note that the mass and volume are predefined by default. Planning can only

take the transportation unit resource capacity into account if these correspond to the

dimensions and units of measurement that you define in a freight unit building rule.

The  equipment,  and  equipment  group  types,  specify  attributes  such  as  the  physical

properties  of  a  certain  kind  of  transportation  unit  resource.  By  creating  a

transportation unit resource, you can do the following:

●  Use the type as a template to create transportation unit resources, copying the

attributes of the type to a new resource.

34


●  Request a special type of transportation unit resource in a forwarding order or

in a booking order.

## Transportation Unit Resource

●  Master data object to represent individual containers

●  Can be created with reference to equipment group type

●  Parameters for transportation unit resources include the following:

○  Capacity

○  Minimum number of seals

○  Physical properties

○  Downtimes

○  Grouping attributes

○  Alternative names

35


Lesson 4 - Default Routes and Schedules

## Default Route

A default route defines the sequence of stops for a given source/destination location

combination.  Default routes can be used in place of transshipment chains with sales

orders  and  deliveries,  forwarding  orders,  and  forwarding  quotations.  Default  routes

can be modified manually where the desired route is different to that proposed by the

system.

To  see  information  related  to  default  routes,  log  into  SAP  Fiori,  then  choose  Master

Data folder→Define Default Routes.

Carrier Schedules

36


When  shipping  products  via  air  or  ocean,  consider  that  your  partners  are  typically

renting space at a port facility. This facility is used by many parties, and so options for

moving the product can be limited.

While  the  road-based  scenario  can  make  use  of  various  transportation  lanes  due to

the  flexibility  of  the  carriers,  ocean  and  air  carriers  often face more competition and

more  regulation.  This  limits  the  flexibility  for  departures  and  arrivals.  From  a

transportation  planning  perspective,  the  implication  is  that  you  may  need  a  more

structured  and  predictable  plan  for  scheduling  purposes.  With  SAP  Transportation

Management  (SAP  TM),  your  organization  can  take  advantage  of  different  types  of

schedules  to  model  specific  departure  and  arrival  rules  suited  to  air  and  ocean

shipping.

## Carrier Schedules for Actual Transportation

Carrier  schedules  represent  the  actual  transportation  executed  by  the  schedule

vehicle. Be it by plane, vessel, train, or truck. Usually, these schedules involve stopping

at locations such as ports and airports that are used commonly and shared by many

37


different  carriers.  Flights  for  air  transportation  and  vessel  voyages for the ocean are

examples of carrier schedules. Carrier schedules can also be truck schedules.

Location  and  time  information  are  relevant  to  a  schedule.  For  example,  the  planner

asks the following questions:

●  When and from where does the plane depart?

●  When do you have to be there to board it?

●  When will it arrive?

●  Which carrier is responsible for the transportation?

●  What can be transported?

Carrier schedules do not just have a start and end destination; they can have multiple

stops,  which  is common for air transportation. Carrier schedules can be executed by

different carriers on different stages using a connection schedule. It is possible to use

a  multistop  carrier  schedule  in  any  sequential  location  combination,  so  it  is  not

required to start at the first and leave at the last location.

Schedules can be created manually in SAP TM and uploaded from an external source.

You  can  also  upload  schedules  from  an  external  data  source  to  SAP  TM  by  calling

function  module  /SCMTMS/BAPI_SCHEDULE_SAVEMULT.  This  function  is  available

for  the  sea,  air,  and  road  transportation  modes.  Alternatively,  you  can  upload

schedules for the air transportation mode in a spreadsheet or CSV format to SAP TM

by  executing  report  /SCMTMS/SCH_UPLOAD.  For  more  information,  see  the  system

documentation.

You  can  delete schedules created manually and uploaded by calling function module

/SCMTMS/BAPI_SCHEDULE_DELMULTI

or

by

executing

report

/SCMTMS/SCH_DELETION.

There  are  four  ways  to  generate a schedule departure. A user can manually create a

schedule  departure  for  a  specific  date  or  generate  schedule  departures  based  on

departure  rules  according  to  a  specific pattern (for example, every Monday at noon).

Furthermore,  you  can  upload  schedule  departures  either  using  the  schedule  upload

report

/SCMTMS/SCH_UPLOAD

or

by

calling

function  module

/SCMTMS/BAPI_SCHEDULE_SAVEMULT.

38


## Schedule Types

SAP  TM  allows  businesses  to  create  different  schedule  types  to handle the multiple

shipping  scenarios  they  may  encounter.  Schedules  can  be  maintained  for  each

business  partner  or  carrier,  and  can  identify  different  loading  and  unloading  points,

such as ports and airports.

If you have reappearing transportation traffic in your transportation network scenario,

you  can  use  the  schedules  functionality.  A  combination  of  transportation  mode,

gateway  customer  fact  sheets  (CFS),  direct,  and  reference  fields  define  the  type  of

schedule.

A gateway schedule includes two gateway locations. In ocean scenarios, the locations

could be the CFS-locations. In air scenarios, they can be the gateway locations.

## Gateway Schedules: Subcategories

The following are the subcategories in the gateway schedules:

●  Direct

The  schedule  goes  from  A  to  B  without  changing  the  mode  of  transport.  For

example, GW Nurnberg to GW Hamburg via truck.

39


●

## Indirect

The  schedule  goes  from  A  to  B  but  the  mode  of  transport  changes.  For

example, GW Hamburg to GW Cape Town via truck and ocean.

## Air and Ocean Scenarios: Subcategories

The following are the subcategories in ocean and air scenarios:

●  Sailing schedules with vessel information

●  Master flight schedules with aircraft information

Carrier  schedules  describe  a  sequence  of  transportation  stops  where  the  start

location  and  the  target  stop  are  not  gateways.  A  gateway  is  a  transportation  hub

where freight is consolidated and deconsolidated.

Carrier Schedules

●  Ocean Carrier Schedule

Use the ocean carrier schedule to define a standard sequence of transportation

stops that are served by a ship. By specifying departure rules, you can generate

voyages automatically.

●  Carrier Flight Schedule

Use the carrier flight schedule to define a standard sequence of transportation

stops  that  are  served  by  a  plane.  By  specifying  departure  rules,  you  can

generate flights automatically.

●  Road Schedule

Use  the  road  schedule  to  define  a  standard sequence of transportation stops

that are served by a truck.

## Schedule Capacities

In the schedule type, you can define if the schedule has the following items assigned

to it:

●  Limited capacities

●  Transportation costs

40


Unit 3 - Creation of Transportation Requirements

Lesson  1  -  Defining  Transportation  Relevance  for  Orders  and
## Deliveries

Transportation Requirements

The

initial  event  that  triggers  the  transportation  management  process

is  a

transportation  requirement.  Based  on  the  deployment  option  used  for  SAP  TM,  the

following are the transportation requirement starting points:

●  Logistics Service Providers (LSPs or 3PLs)

●  The side-by-side deployment / external TM system integration

●  The embedded deployment / internal TM component integration

Logistics Service Providers (LSPs or 3PLs)

Logistics  service  providers  (LSPs  or  3PLs)  can  also  receive  transportation

requirements.  For  LSPs,  the  forwarding  orders  are  created

in  one  of  two

41


ways–manually,  using the SAP TM UI, or through integration with an external system

via electronic data interchange (EDI).

In an LSP process, the following documents act as transportation requirements:

●  Forwarding orders

●  Forwarding quotation

## The Side-by-Side Deployment/External TM System Integration

In  side-by-side  deployment  scenarios,  SAP  TM  is installed as a separate system and

the  original  document  causing  the  transportation  demand  is not present in SAP TM.

Therefore,  a  replication  of  this  information  to  the  SAP  TM  system  must  take  place.

This  replication  can  either  create  order-based  transportation  requirements  or

delivery-based  transportation requirements. Order-based transportation requirements

may be created from a sales order, a purchase order, a stock transport order (STO), or

a  scheduling  agreement.  Delivery-based transportation requirements may be created

from  an  outbound  or  inbound  delivery.  Integration  between  SAP  TM  and  the  source

system  (SAP  ERP  or  SAP  S/4HANA)  is  accomplished  using  XML messages via SAP

Process Integration, or a point-to-point communication.

## The Embedded Deployment/Internal TM Component

In  the  embedded  deployment  scenario,  a  separate  document  representing  a

transportation  requirement  is  not  required,  since  the  original  object  causing  the

transportation demand is already present in the SAP S/4HANA system itself. This can

be  order  documents  like  sales  orders,  purchase  orders,  stock  transport  orders,

scheduling agreements, or delivery documents like inbound or outbound deliveries. In

this  deployment  scenario,  the  freight  unit  is  the  starting  object  for  SAP  TM  and  the

freight  unit  is  created  directly  from  the  original  object  causing  the  transportation

demand. The embedded scenario is the primary focus of this overview training.

## Logistics Integration

The following documents can trigger an SAP TM process, either through internal SAP

TM component integration or via external SAP TM system integration:

●  Sales orders

42


●  Customer returns

●  Purchase orders

●  Stock transport order

●  Returns stock transport order

●  Sales scheduling agreement

●  MM Scheduling agreement

●  Outbound deliveries

●

## Inbound deliveries

The  following  configuration  steps  enable  freight  order  creation  from  SD/MM

documents:

●  Activate Integration of documents via control key

●  Create logistics integration profile

●  Assign logistics integration profile to document type

43


Lesson 2 - Creating Freight Units

## Freight Unit

The  freight  unit  is  the  smallest  unit  that  can  be  transported.  The  predecessor

document  data  and  the  freight  unit  building  rules  form  the  basis for building freight

units.  You  define  the  most  important  settings  for  the  freight  unit  in  the  freight  unit

type.

Predecessor documents can be forwarding orders, sales order, delivery, order-based

transportation  requirements,  or  delivery-based  transportation  requirements.  For

embedded  TM  deployment,  the  sales  order  or  forwarding  order  is  the predecessor

document.  For  side-by-side  deployment,  OTR/DTR  and  forwarding  orders  are  the

predecessor documents.

An  N:N  relationship  is  possible  between  the  freight  unit  and  its  predecessor

documents.  The  following  figure  is  applicable  for  the  embedded  environment.  The

same applies for the side-by-side scenario. Freight units can be further deleted, split,

merged based on settings defined in the freight unit type customization.

44


The following are the configuration settings for freight unit type:

Change  Controller  Settings:  You  can  assign  several different settings related to the

change controller. These settings impact how TM responds to changes made to the

freight unit and freight order.

Additional Strategies: There are various extra strategies:

●  Creation  Strategy:  Specifies  tasks  that  the  change  controller  is  to  perform

when creating a freight order, freight booking, and freight unit.

45


●  Save  Strategy:  Specifies  tasks  that  the change controller is to perform when

saving a freight order, freight booking, and freight unit.

●  Delete Strategy: Specifies tasks that the change controller is to perform when

a freight order, freight booking, or freight unit is deleted or canceled.

Execution Settings: There are various execution settings:

●  Execution  Track  Relevance:

## Indicator

for  controlling

the

tracking  of

documents.  To  track  certain  types  of  documents,  choose  2  (Execution

Tracking)  or  3  (Execution  Tracking  with  External  Event  Management).  The

system sets the initial document execution status to Not Started. If you do not

want  to  track certain types of documents, choose 1 (No Execution Tracking).

The system then sets the initial document execution status to Not Relevant.

●

Immediate Processing checkbox.

Planning Settings:

●  Planning  profile:  Planning  profile  can  be  assigned  to  a  freight  unit  type  for

freight order planning.

●  Rule  for  pick up/delivery windows: Time windows can be specified for pickup

and delivery of goods. If the condition is not defined, then rule is considered.

●  Condition

for  pickup  and  window  determination  window:  Condition

/SCMTMS/TOR_TIMEWIND can be assigned to the freight unit type based on

this  condition.  The  following four dates and times for pickup and delivery are

calculated  for  source  and  destination  based  on  information  derived  from the

sales order, forwarding quotation, OTR, DTR:

○  Acceptable start date and time

○  Requested start date and time

○  Requested end date and time

○  Acceptable end date and time

46


Event Management Settings:

●  Application  Object  Type:  Type  of  application  object  to  be  tracked  on  the

application  system  necessary  for  determining  event  management  relevance

for an application object. The event manager only processes event messages

for these objects.

●  Last  Expected  Event  for  Execution  of  a  Document:  The  last  expected event

for a document, for example, the unexpected event Unload End.

Default MTr Definition Settings:

●  Default MTr for Type: Indicate the default means of transport type

●  Condition for Default MTr

Default Units of Measure:

●  Weight

●  Volume

Direct Shipment Options:

●  Direct Shipment Option Type: There are three standard options, which include

no determination of direct shipment options, automatic determination of direct

shipment options, and manual determination of direct shipment options.

47


●  Carrier Selection Settings: Indicates carrier selection settings that are used for

the determination of direct shipment options.

●  Carrier  Selection  Conditions:  Specifies  the  condition  that the system uses to

determine carrier selection settings for direct shipment processes at runtime.

●  Direct  Shipment  Strategy:  Specifies  the  process  controller  strategy  that  can

be used to determine the direct shipment options for a freight unit.

Freight Order Determination:

●  Freight Order Type: Default freight order type for direct shipment.

●  Freight  Order  Type  Condition:  Condition  can  be  created  to  decide  which

freight order type is used for direct shipment.

Organizational Unit Determination:

●  Default Org Unit: Execution Organization, Purchasing Organization, Execution

Group, Purchase Group. These are the organization numbers that are created

in Organizational Structures.

●  Consider

the  Organization  Unit  of  User  checkbox:  Considers

the

organizational  unit  assigned  to  the  user  that  creates  the  freight  unit  in  the

determination of the organizational unit responsible for the freight unit.

●  Condition  of  Determination  Rules:  Conditions  can  be  created  to  affect  the

organizational unit determination.

Additional Settings:

Track Changes checkbox: Select this box if changes are to be tracked.

## Freight Unit Building Rule

Freight  unit  building  rules  define  how freight units are built. The system determines

which  freight  unit  building  rule  (FUBR)  is  taken  into  account  for  the  business

document during planning. The following are the three FUBR determination options:

1.  The  system  checks  the condition defined in the logistics integration profile. If

there  is  no  condition  or  the  condition  cannot  determine  a  result,  the  system

moves to the second option.

2.  The system checks if a FUBR has been maintained in the logistics integration

profile. If no FUBR is maintained, the system moves to the third option.

48


3.  The system applies to standard settings.

When  creating  freight  units,  the  system  first  groups  all  delivery  items  within  the

following parameters:

●  Hard constraints for source / destination location and pickup / delivery dates

●  Business document attributes and packaging information

●

## Incompatibilities

Freight  units  are  created  automatically  if  transportation-relevance  is  determined for

the  transportation  demand  (sales  order,  purchase  order,  delivery,  forwarding  order,

OTR, DTR).

The system considers freight units that already exist for the transportation demand. It

creates  freight  units  depending  on  the  split  quantity  and  the  checkbox  for  the  item

split  allowed.  The  system  considers  these  entries  when  creating  multiple  freight

units.  You  can  use  strategies  to  create  freight  units  in  accordance  with  your  own

requirements.  SAP  delivers  the  standard  strategy  FUB_AUTO  for  freight  unit

building.

49


Within  the  FUBR,  you  must  specify  the  critical quantity. This parameter defines the

primary unit of measure that allows a line item on a transport requirement to be split

into  multiple  freight  units.  Besides  that,  several  planning  quantities  can be defined,

for  example,  weight  and  volume. Every planning quantity is considered for capacity

checks  of  resources  during  transportation  planning,  and  every  planning  quantity  is

copied to the freight unit.

The  split  quantities  define  the  maximum  capacity  of  a  freight  unit.  The  system

calculates the freight unit as a multiple of the rounding quantity. If Item Split Allowed

is  selected,  the  freight  unit  splits  the  item  while it is being built, if it is over the split

quantity.  The  process  controller  strategy  allows  you  to  use  strategies  to  define  the

way  in  which freight units are created, in accordance with your requirements. If you

maintain  an  equipment  type  in  the  FUBR,  the  capacity  of  the  equipment  is

considered during freight unit building and the items consolidated into one freight unit

are loaded into the equipment.

If  necessary,  companies  can  define  that  the  freight  units  are  split  if  certain

constraints  are  present. For example, you define the maximum capacity of a freight

unit using the split quantity. Let's say, you have to transport five tons of cement, but

you can only transport it in batches of 500 kg. In this case, you define a split quantity

of 500 kg and the system generates 10 freight units.

Based  on  the  definition  of  freight  units,  all  items  included  in  a  freight  order  are

transported  together  from  their  source  to  their  final  destination.  However,  in

50


multimodal  scenarios,  different  planners  are  involved  in  scheduling  the  different

stages of the transport. For this reason, stage information can be added to the freight

unit. This allows a degree of independence when scheduling the stages.

## Using

the  process  controller,

freight  unit  building  can  be  adjusted

to

customer-specific requirements using ABAP coding.

Freight Unit Building Rule

## Consolidate Per Item

One FUBR strategy is to consolidate per item. This strategy creates separate freight

units for each item in the transportation requirement.

Consolidate per Request (Compatible Parts)

Another  FUBR  strategy  is  to  consolidate  per  request  for  compatible  parts.  The

system  groups  all  the  items  of  a  business  to  form  a  freight  unit. It is assumed that

compatibility rules are used to group similar items.

## Consolidate as Much as Possible

Another FUBR strategy is to consolidate as much as possible. This strategy can only

be  used  with  interactive  FU  creation  via  a  batch  report.  It  consolidates  several

51


transportation  requirements  into  one  freight  unit,  if there are no other reasons for a

split.

52


Lesson 3 - Conditions and Incompatibilities

## Conditions

BRFplus  (Business  Rules  Framework  plus)  is  a  powerful  rules-based  engine,  and  is

used  by TM conditions. TM Conditions empower users to process complex business

rules  and  it  reduces  the  need  to  develop,  customize,  and  configure.  Conditions  are

used as filters for automatic decision-making. A condition maps input values to output

values.  For  example,  determination  of  product  type,  determination  of  resource  type,

determination of execution organization.

There are different types of conditions for different areas. For example, document type

determination,  order

type  determination,

loading  and  unloading  durations,

incompatibilities, printing, approvals, tolerances, and any customer-specific rule(s).

53


Condition type (CT): First, you define the CT and specify the origin. Specify the CT, the

fields against which you are testing, and how you want to store the test results when

creating  a  condition.  This  is  referred  to  as  the  origin  of  the  condition.  The  system

provides the following three options for the origin of the condition:

●  Direct  business  object  access:  The  Direct  Business  Object  Access  condition

returns directly the value determined by the data access definition. There is no

evaluation of the data.

●  BRF+  Decision  Table: The BRFplus Decision Table condition takes the input of

the  data  access  definition  and  evaluates  it in a table. This condition table can

be  maintained  from  the  condition  user  interface.  This  origin  of  condition  is

most commonly used by TM users.

●  BRF+ Expression: The BRFplus Expression is a logical expression.

54


●

Input  values:  Input  values  originate  in  the  fields  of  business  objects  (direct

business  object  access)  or  user-specific  fields  (data  crawler),  or  values

determined  in  external  determination  classes.  The  available  input  values

depend  on  the  condition  type  chosen.  The  condition  type  defines  the  area  in

which the system is to take the condition into account. There are various input

values and they are determined by the following factors:

○  Direct Business Object Access

○  Data Crawler

○  Determination Class

●  Output values: The output of a condition is comprised of several output values,

all derived from the input values based on decision-making. The output values

are  determined  by  the  condition  type.  For  example,  the FUB rule is a result of

FUB rule determination.

●  BRFplus  decision  table:  The  system  creates  a  condition  based  on  BRFplus

expressions.  The  system  then  processes this table from top to bottom during

determination.  When  the  system  finds  a  row  in  the  BRFplus  decision  table

whose input values match the current input values, it copies the corresponding

output values and processes them in the area that made the call.

55


Conditions  are  tests  performed  against  various  objects,  such  as  transportation

requirements  or  freight  units,  to  determine  whether  a  situation  is  true  or  false.  For

example, to decide if products on a single transportation requirement can be shipped

together,  each  item  on  the  OTR  is  checked  for  certain  parameters.  If  a  certain

parameter is found, rules are built to determine where consolidation can take place. If

an incompatibility exists, more than one shipment is necessary.

If  you  need  extra  fields  for  the  condition  types  to  be  delivered  as standard, or if you

want to use customer condition types, create new data access definitions and extend

the  assignments  in  Customizing.  You  can  also  change  or  add  to  the  data  access

definitions  used  by  default.  The  condition  type  must  be  identified  when  defining  a

condition  in  SAP  TM.  A  condition  type  is  a  configurable object that is based on field

contents stored in various business object nodes. Each condition type is assigned to a

business object (structure) and the node name (at the header or item level).

When defining a condition type, you can identify when a result is found, if it is stored in

a structure, and if one or more conditions exist for this condition type. Condition types

are then assigned to data access definitions. These objects specify what fields and in

what sequence users can define specific condition records.

## Incompatibility

During  transportation  planning,  companies  prepare  a  set  of  guidelines  regarding

shipping.  For  example,  if  a  shipper  has  products  that  must  be  transported  via  a

56


refrigerated container, they cannot ship those products with frozen freight units. While

planning  transportation  shipments,  companies  define  rules  regarding  how  they

consolidate  loads  into  a  single  freight  order.  There  are  many  factors  other  than

capacity  that  impact  how  freight  orders  are  built.  In  SAP  TM,  these  rules  are  called

incompatibilities. This data defines the relevant parameters controlling when it is and

is not appropriate to consolidate loads.

In the figure, a company has various products to ship. The temperature at which items

must be stored during transit is the attribute that signals if items can be consolidated.

A test is executed to decide the temperature in which each product is shipped. A rule

states  that  items  classified  as  chilled  cannot  be  shipped  with  items  classified  as

frozen.  This  could  lead  to  damage  or  spoilage  if  a  product  is  shipped  at  the  wrong

temperature.

Incompatibilities  are  used  with  conditions  to  influence  the  results  in  SAP  TM  during

freight  unit  building,  transportation  planning,  transportation  proposals,  and  carrier

selection.  Incompatibilities  are

important  when  defining  requirements  for  load

building.  For  example,  freight  units  with  different incoterms must not be transported

together.  Refrigerated  goods  must  be  transported  in  an  appropriate  means  of

transport. Certain means of transport cannot be loaded at a specific location because

the location does not have a suitable loading ramp.

57


When  creating  an  incompatibility  definition,  you  must  specify  a  validity area. Validity

areas are composed of an incompatibility area and an incompatibility type.

Incompatibility areas define where an incompatibility can be used. Four incompatibility

areas  exist  in  TM:  Automatic  Planning  and  Manual  Planning  (previously  know  as

Vehicle  scheduling  and  routing  (VSR),  Freight  unit building, Carrier selection, Delivery

proposals.

Incompatibility  Types:  Incompatibility  types  are  delivered  by  SAP  and  define  the

objects  that  are  the  focus  of  the  rule  being  enforced.  The  following  list  contains

examples  of  incompatibility  types:  Freight  unit  -  Freight  unit,  Freight  unit  -  Vehicle,

Freight unit - Transshipment location, Carrier - Transportation Order.

In  addition  to  the  validity  area,  the  incompatibility  definition  can  determine  how  the

rule  is  enforced  in  both  manual  and  automatic  planning  by  defining the reaction, for

example, incompatibility is ignored, warning if ignored, must not be violated.

Incompatibilities can be defined between two attributes of two business objects. This

requires  that  two  conditions  are  defined  and  relevant  results  are  specified.  Two

58


business  objects  are  then  incompatible  if  the  result  of  the  conditions  matches  the

relevant results.

Setting  the  Identical  Values  Only  checkbox  in the incompatibility definition allows for

an  incompatibility  to be defined between two instances of the same business object,

for  example,  two  freight  units.  In  this  case,  a  single  condition  is  defined  in  the

incompatibility  definition.  The  two  business  object

instances  are  then  only

incompatible if their values differ.

59


Incompatibility  Settings:  Incompatibility  settings  can  be  maintained  in  planning

profiles,  carrier  selection  settings,  delivery  profiles,  and  the  freight  unit  building  rule.

Transportation  planning  profiles  specify  when  the  system  allows incompatibilities to

be violated during manual planning, in VSR optimization, or in background processing.

Incompatibility settings are assigned within these profiles. The incompatibility settings

group  together  several  incompatibility  definitions  that  can  apply  to  a  planning  run.

Only incompatibilities for the same incompatibility area can be combined.

60


61


Lesson 4 - Trigger, Create, and Manage Deliveries

## Delivery Overview

The  decision  about  whether  to  start  the  process  in  TM  with  either  the  order  or  the

delivery  depends  on  the  customer  requirements  and  guidelines  concerning

transportation  planning and execution. If shipping activities other than transportation

planning  are  involved  before  the  transportation  process,  the  process  based  on  the

delivery  is  more  likely  to  be  used.  If  the  goods  are  sold  with  all  shipping  activities

considered, the order is the basis for transportation planning.

There  is  no  difference  in  the  continuation  of  the  process  between  transportation

requirements based on an order and those based on deliveries. As shown in the figure,

both documents are capable of triggering the entire process.

The following integration scenarios can be set up:

●  Order Integration with delivery proposals

●  Delivery Integration without delivery proposals

62


## Order Integration with Delivery Proposal

If the TM component is leading the transportation process, you set up the integration

scenario Order Integration with Delivery Proposal. The order is created in SD/MM and

then integrated into the TM component. Freight units are created in TM automatically.

After  freight  units on freight orders, the delivery date can be known. This information

is relayed back to SD/MM, where delivery documents are created.

Delivery  proposals  are  used  to  propagate  planning  information  from  TM  to  SD/MM.

Deliveries are created in SD/MM. This process is called Delivery Proposal because TM

is proposing the creation of deliveries. SD/MM decides how the delivery is created.

63


SAP  TM  considers  data  for  delivery  creation  from  the  order  and  from  the  assigned

freight units, freight orders, and freight bookings. Based on the chosen input, SAP TM

creates  delivery proposals. A proposal consists of groups of freight units that can be

delivered together.

●  Dates:  TM  uses  dates  from  the  freight  order  or  freight  booking.  If  the  freight

unit  is  not  planned, that is, no freight order or freight booking exists, then SAP

TM uses the dates from the freight units.

●  Quantities: TM uses quantities from freight units.

●  SD/MM  Document  References:  TM  retrieves  document  references  (such  as

order  document  number)

from

the  order/order-based

transportation

requirement.

Delivery  profiles  define  how  delivery  proposals  are  created.  Although  the  delivery

profile is optional, it makes sense to create a profile to reuse the same settings every

time you want to create delivery proposals. The settings, you can define here, concern

how  and  if  freight  units  can  be  consolidated  into  one  delivery  proposal  and  which

freight units cannot be consolidated.

To see information related to delivery profiles, log into SAP Fiori, then choose Profiles

and Settings→Create delivery profile.

64


You  can  define  how  the  delivery  proposals  are  to  be  created  (for  example,  one

proposal per item, one proposal per freight unit, and so on). One option of the delivery

profile  is  to  "fix"  the  planning  result  for  freight  units  and  freight  orders.  Fixing  the

planning  means  that  after  the  planning  results  are  transferred  via  the  delivery

proposals,  they  can  no  longer  be  changed  in  SAP  TM.  Incompatibilities  in  delivery

profiles can be used to prevent certain freight units or items from being consolidated

into one delivery proposal.

After  the  delivery  proposals  have  been  sent,  deliveries  are created. SAP TM receives

information about the status of the delivery creation.

## Delivery Integration Without Delivery Proposals

If  the  SD/MM  component  is  the  leading  system  for  delivery  creation  and item order

consolidation, you set up the integration scenario Delivery Integration without Delivery

Proposal.  In  this  case,  the  order  does  not  trigger  the  transportation  management

process  and  thus  the  freight  unit  creation.  Only  after  the  delivery  is  created  for  the

order  are the freight units created. These freight units now better represent the splits

and  consolidations  that  have  been  done  previously  in  SD  or  MM.  Planning  can  now

start,  although  the  planning  results  do  not  affect  the  date  of  the  delivery  anymore.

Dates in the freight unit are considered as hard constraints during planning.

65


Lesson 5 - Creating Handling Units

## Handling Units

A  handling  unit  (HU)  is  a  logistic  unit  consisting  of  packaging  materials  and  goods

(materials).  Typically,  a  company  does  not  move  individual  pieces  of  different

materials, rather, it moves quantities of materials grouped together as packages. You

can depict this situation in the SAP System using Handling Unit Management.

When you use Handling Unit Management, the system tracks the entire HU rather than

individual  materials.  The  HU is the common unit for material and information flow. A

business  transaction  for  a  HU  implies  corresponding  business  transactions  in  the

background  for  the  materials  and  packaging  materials  it  contains.  In  this  way,  one

business  transaction  entry  takes  the  place  of  several  individual  material-movement

entries.

You  can  use  handling  units  and  can  pass  them  to  partners  throughout  the  supply

chain.  Handling  units  have  a  single  identification  number  that  uniquely  identifies the

handling  unit  across  the  various  processes  through  which  it  moves.  Using  handling

units in a cross-system logistics chain usually requires an identification number that is

unique  worldwide.  You  therefore  have  the  option  of  assigning  a  Serial  Shipping

Container Code (SSCC) number to each handling unit.

Packaging Materials

66


Packaging materials are intended to enclose or hold together the materials that are to

be  transported.  The  packaging  materials  and  the  goods  material  together  comprise

the handling unit, as we have seen.

The  material that is to be packed can be packed into or onto the packaging material.

The  packaging  material  can  also  be  a  load  carrier,  such  as  a  pallet.  The  most

important  packaging  materials  include  crates,  boxes,  containers,  wire  baskets,  and

pallets.

You must maintain the material master data for each packaging material you want to

use.  When  creating  material  master  records  for  packaging  materials,  enter  either

material  type,  VERP  (packaging),  or  a  customer-specific  material  type  that  you  have

already defined in Customizing.

Handling Units and Freight Units

When  a  delivery

includes  handling  unit

items,  the  freight  units  are  adjusted

accordingly.  All  product  items  that  have  been  packaged  into  one  handling  unit  are

67


included in one freight unit; they are not split across several freight units. In this way, it

is  ensured  that  parts  of  a  handling  unit  are  not  assigned  to  different  freight  orders

during transportation planning.

If,  for  example,  separate  freight  units  were  built  per  product  initially,  and  these

products are consolidated into one handling unit, the separate freight units are merged

into one freight unit.

There  is  not  necessarily a one-to-one relationship between handling units and freight

units.  One  freight  unit  can  contain  several  handling  units.  If  desired,  freight  unit

building can be set up to create one freight unit per handling unit.

68


Lesson 6 - Unified Package Building

Unified Package Building Overview

## Unified Package Building

Historically,  SAP-based  logistics  applications  have  implemented  separate  packing

solutions as part of their processes:

1 - LO has introduced Packing Instruction based logic

2 - EWM has introduced Packaging Specification based logic

3 - TM has introduced the Package Builder

69


While  packing  instructions  and  packaging  specifications  are  rule-based  and  share

many  similarities,  package  building  offers  a  different  approach,  which isn’t based on

rules  but  considers  constraints  and  offers  an  optimization  algorithm  to  build

optimized  mixed  pallets.  If  a  product  is  always  handled  and  shipped  in  a  certain

packaging  structure,  this  could  be  modeled  very  well  by  a  packing  instruction  or

packaging  specification.  If  the  business  at  hand  involves  transporting  mixed  pallets,

which contain multiple products for one or even multiple customers, package building

can be more appropriate as it minimizes the number of mixed pallets required.

As  the

integration  of  these  components

is  being  driven  as  part  of  recent

developments,  it  has  become  a  priority  to  consolidate/unify  the  use  of  the  three

packing solutions. As a consequence, Unified Package Building (UPB) allows different

business  applications,  like  EWM,  TM,  or  LO  processes,  to  leverage  the  usage  of

different packing solutions.

UPB  is  meant  to unify the packaging approaches that existed before its introduction.

More  specifically,  in  the  past  several  applications  in  TM,  EWM,  and  LO  have  used

differing  packing  engines that are based on different packing rules. In addition, these

different  packing  engines  handle  different  persistence  approaches  for  the  resulting

packaging  hierarchies.  As  the  underlying  requirements  to  package  materials  are

70


similar, SAP intends to align and unify its long-term strategy in this area. The following

diagram illustrates the approach:

The  UPB component is a reusable component that allows the packaging of products

by  using one of the available packing engines (defined as UPB engines) and applying

configurable  rules  (defined  as  UPB  rules).  Currently,  the  supported  UPB  engines  are

based on:

●  Packing Instructions (PI)

●  Package Builder (PB)

●  Packaging Specifications (PS)

The  UPB  is  currently  supported  by  processes  in  the  following  applications  (that  is,

components of SAP S/4HANA):

●  Transportation Management (TM)

●  Extended Warehouse Management (EWM)

●  Logistics General (LO)

In a nutshell, the UPB component receives input items, which correspond to materials.

It applies UPB rules (for example, PIs) and it returns a packaging hierarchy as a result.

71


UPB  primarily  establishes the structure of packaging but does not retain it. The onus

of  preserving  the  packaging  hierarchy  lies  with  the  end-user  applications  like  EWM,

TM,  and  LO  is  responsible  to  persist  the  packaging  hierarchy  in  its  business

documents.

UPB  is  compatible  with  a  distributed  system  environment;  however,  the  essential

master data and the UPB profile need to be present in the system in use. Therefore, if

a  standalone  SAP  S/4HANA  instance is to use it, the necessary master data and the

UPB profile must exist within that particular instance.

Unified Package Building Profile

72


## Unified Package Building Profile

In  the  unified  package  building  profile,  you  can  define  generic  settings  for  unified

package building (UPB):

●  You  can  control  UPB  in  a  way  that  items  belonging  to  different  locations  or

containing different products, for example, must not be packaged together.

●  You  can indicate that auxiliary packaging materials such as filling materials or

slip sheets are treated as separate items in the result of UPB.

●  You can activate the application log and indicate the logging severity.

●  You can choose, which UPB engine the system is to use. The following engines

are available:

○  Package building with the package builder

○  Packing instruction

○  Packaging specification

Package Building New

UPB TM Planning Integration

●  When freight units (FUs) are created

Early  in  the  process,  unified  package  building  can  be  used  during  freight  unit

building.  This  is  the  right  approach  if  packages  are  built  per  freight  unit  (FU).

This  type  of  unified  package  building  takes  place  early  in  the  process  if  the

system  creates  FUs  based  on  order  documents  (for  example,  forwarding

orders or sales orders).

73


When  FUs  are  created,  you  can  have  freight  orders  or  package  units  created

instead  of  FUs.  You  make  this  setting  in  the  freight  unit  building  rule  (FUBR)

(see "Prerequisites").

●  Based on capacity documents

Late  in  the  process,  unified  package  building  can  be  triggered  for  capacity

documents  such  as  road  freight  orders.  This  approach

is  needed

if

customer-mixed packages are to be built. This type of unified package building

takes  place  late  in  the  process  if  capacity  documents  exist  already.  You  can

start  from  the  user  interface  of  an  individual  capacity  document  or  from  the

transportation  cockpit.  It  is  offered  for  road  freight  orders,  trailer  units,

container units (Road transportation mode only), and package units.

●  During the automatic creation of package units

After  freight  unit  building,  package  units  can  be  created  by  applying  unified

package  building  to  a  set  of  FUs:  This  is  useful  if  multiple  FUs  are  packaged

and  transported  together.  You  can  create  package  units  based  on  unified

package building for FUs.

Orders are placed on products, which, during the real process, are packaged to create

packages  and  pallets  (HUs,  TUs,  main  cargo  items,  and  so  on).  Packaging  is  a

warehouse  process.  Warehouse-specific  information  can  influence  the  result  (for

example,  pick  sequence).  For  the  end-to-end  process,  the  package  information  is

required long before the warehouse is reached.

74


Package  Building  is  inserted  into  the  overall  planning  process  at  the  freight  unit

building  step.  It  allows  products  to  be  combined  into  packages.  These  packages

(within  FUs)  are  later  used  in  subsequent  planning  steps  (manual  and  optimizer

planning/VSR) to create freight orders and subsequent load planning).

Package Building Parameters:

75


Package  building  is  defined  by  the  package  building  profile.  This  enables  certain

process  steps  to  be  switched  on  or  off,  specific  behavior  to  be  defined  (especially

when  building  mixed  packages),  and  also  offers  default  attributes  that  can  be

overwritten by product-specific settings.

The following are examples of parameters:

●  Process  Products  by  Layer:  This  parameter  can  turn  off  the  creation  of  full

product  packages.  By  default,  this  is  seldom  required,  but  gives  a  mixed

package building logic more freedom. For example, a certain customer always

requires  a  specific  product  combination  (even  when ordering a high quantity),

this  can  then  be  implemented  in  an  enhancement  receiving  a  full  set  of

products.

●  Keep  Layers  Together: When building mixed packages, the parameter controls

of a product can be split over multiple mixed packages. In some situations, this

results  in a better and more efficient plan. However, in more warehouse-driven

scenarios,  it  might  not  be  efficient  to  process  a  product  twice  for  two

packages. Therefore, it can be turned off.

●

Ignore Product Height: When consolidating leftover products that are not filling

a  complete  package,  or  a  complete  product  layer,  the  system  tries  to  build

mixed  layers  combining  products  with  the  same  height.  This  step  can  be

skipped  if  the  product  height  is  not  important.  As a result, all leftover product

quantities can be combined directly resulting in standard nonstackable layers.

The  package  building  profile  is  assigned  to  the  FUBR.  In  addition,  for  freight  unit

building you can define the maximum number of package items that can be put into a

single FU.

The relevant package building profile can be set depending on the process in:

●  FUBR:  define  package  building  profile  ,  store  package  estimate  vs  packaging

hierarchy.

●  Planning  profile:  define  package  building  profile,  enabling  consolidation

package building.

Product and Package Type Assignment:

76


The  product  and  package  type  assignment  is  a  new  master  data  transaction  that

defines, for each product in the package builder, which package it goes into or onto.

To  reduce  the  effort  when  maintaining  those  definitions,  it  is  possible  to  work  with

generic patterns.

The  definition  can  depend  on  the  material/product,  business  partner,  and  shipping

location.  For  example,  product  A  is  delivered  with  an  EU  pallet  stacked  up  to  1.5

meters  (first  entry).  However,  when  delivering  this  product  to  customer  X  from  your

warehouse  Y,  you  use  a  different  pallet  type  containing  product  A  stacked  up  to 1.3

meters, because the customer can only handle pallets up to this height (second entry

as exception).

The  package  builder  will  always  prefer the most specific entry. It starts to search for

an entry matching all three key fields exactly. If nothing is found, it will score all other

keys in the following manner:

●  How many keys match exactly?

●  How many keys match by pattern?

●  How many keys are initial?

It then selects the key with the highest score.

77


Package  Building  Selected  Features:  During  package  building,  the  system  bundles

products  into  packages  based  on  specific  constraints,  while  also  keeping  the  total

number  of  packages  to  a  minimum.  The  system  can  also specify the exact position

and  orientation  of  each  product  item.  You  can  define  these  constraints  for  different

combinations  of  product,  business  partner,  equipment,  and  location.  If  several

constraints apply, the system always uses the most specific constraint.

The  system  creates  mixed  packages  based  on  one  of  the  following  consolidation

types:

●  Volume

●  Layer Definitions

78


●

Incompatibilities,  stacking  rules,  and  product  orientations  (based  on  these

values,  the system determines the exact positions of each product item in the

package (detailed mixed package building))

Furthermore,  the  definition  allows  specific  limits  to  be  set  regarding  the  weight  and

height  that  the  package builder considers when packing the product. It is possible to

set  valid  limits  on  the  package  material  (that  is,  product  master  data). For example,

you  can only stack an EU pallet up to 1.8 meters and put 900 kg on it. In the product

and  package  type  assignment,  you  can  lower  the  specific  product,  customer,  and

location limits.

When  creating  packages,  the  system  can  split  the  quantity  of  a  product  using  the

following criteria:

●  Quantity per package

●  Maximum height of the package

●  Maximum weight of the package

If  different  products  are  to  be  packaged, the system considers the lowest maximum

height  and  the  lowest  maximum  weight  for  a  product  or  a  packaging  material.  For

example, if each product has a different maximum height, the system uses the lowest

maximum height.

The result of package building is different types of packages, as follows:

79


●  Packages that contain only a single type of product.

●  Mixed packages that contain several different products.

●  Packages  that  consist  of  several  layers:  The layers within a package can also

contain different products, which results in mixed layers.

●  Nested packages, that is, a package in another package: For example, you can

plan 24 cans in one box and 100 boxes in ten layers on one pallet.

●  Full packages or incomplete packages: Incomplete packages provide room for

further consolidation.

●  Flat or uneven packages: Flat packages are a prerequisite for stackability.

"Late"  Package Building: The "late" or "consolidation" package building process defers

the  package  building  process  until  the  vehicle  scheduling  and  routing  process  has

created  freight  orders  for  the

individual  tours.  This  allows  to  add  additional

information  into  the  package  building  process,  that  is,  which  products  are  to  be

delivered with the same truck/tour/freight order. Consequently, this information can be

utilized to build packages/pallets across FUs/deliveries.

Package  Units:  The  Package  Unit  (PU)  is  an  additional  business  document.  It

represents  one  or  multiple  packages  to  be  transported  together  across  multiple

stages  (capacity  documents).  The  PU  is  not needed if there is only one stage. It can

have  a  deep  packaging  hierarchy,  for  example,  pallet–carton–product.

It

is

(technically) a transportation unit (like container units, trailer units, and railcar units). It

can  represent  both  a  capacity  document  and  a  demand  document.  That  means,

package units can be assigned to freight orders/bookings and container/trailer/railcar

80


units, but at the same time FUs can be assigned to a package unit. Typical examples

for package units are pallet, pallet cage, box, and carton.

The package unit provides additional functionality to enable an integrated delivery and

line-haul planning process:

The PU type allows defining the flexibility of assigning predecessor documents to the

PU:

●  Completely:  A  FU  is  completely  assigned  to  the  PU.  This  is  the  standard

approach of assigning FU.

●  Partially:  A  FU  can  be  distributed among multiple PUs (multi-assignment), but

the PUs are assigned to one single capacity document. This is a new approach,

which  helps  to  avoid  FU  splits  and  an  increasing  number  of  documents  in

scenarios  with  freight  units'  items  distributed  across  multiple  package  units

(for example, pallets).

If  PUs  containing  the  same FU get assigned to different capacity documents, the FU

gets split to ensure the fundamental FU consistency principle (it represents the goods

transported together across the whole transportation chain).

81


82


Lesson 7 - Understanding Change Controller

## Process Controller

The process controller is a framework with which you can define your own strategies,

methods, and how your planning process is executed.

You  can  use  strategies  to  define  complete  processes.  By  assigning  a  service,  you

define the area in which the process is to be used, for example, transportation charge

management, freight unit building, or VSR optimization. SAP delivers various standard

strategies.

Methods define the individual process steps of a strategy.

You use strategies in SAP Transportation Management in the following areas:

●  Freight unit building

●  Carrier selection

●  VSR optimization

●  Manual planning

●  Change controller

●  Definition of customer-specific functions

In  this  lesson,  we  are  going to focus on the change controller. The other areas listed

will be explained in other units.

83


## Change Controller

Whenever  there  are  changes  to  transportation  requirements,  for  which  follow-up

documents  already  exist,  SAP  TM  provides  support  to  react  to  these  changes.  For

example,  if  the  quantity  of  a  sales  order  changes,  and  that  sales  order  is  already

planned  in  SAP  TM,  you  might  have  to  adjust  your  transportation  plan.  SAP  TM

provides  a  configurable,  flexible  framework  to  support  change  processes.  In  the

example  of  a  quantity  change,  the  system  can  check  the  resource  capacity  and

remove  freight  units  from  planning  if  the  resource  is  overloaded.  In  addition,  a  user

could be informed of changes via an alert.

The  change  controller  checks  whether  one  of

the

following  business

documents/objects has changed and how the system is to process these changes:

●  Freight unit

●  Transportation unit

●  Freight order

●  Freight booking

●  Service order

●  Schedule type

The change controller can react to the following planning-relevant changes:

84


●  Changes to quantity

●  Changes to dates/times

●  Changes to source locations, intermediate stops, and destination locations

●  Reported execution information

●  Additional or deleted freight units or locations

The  change  controller  checks  whether  one  of

the

following  business

documents/objects has changed and how the system is to process these changes:

●  Freight unit

●  Transportation unit

●  Freight order

●  Freight booking

●  Service order

●  Schedule type

The change controller can react to the following planning-relevant changes:

●  Changes to quantity

●  Changes to dates/times

●  Changes to source locations, intermediate stops, and destination locations

●  Reported execution information

●  Additional or deleted freight units or locations

Note that this is not an exhaustive list.

The following is an example of change controller actions in response to changes:

●  Remove corresponding freight units from the transportation plan

●

Invalidate successor business documents such as freight orders

●  Stop the current associated tendering processes

●  Stop and restart the current associated tendering processes

●

## Issue alerts

You can also define your own actions. You can also react to other changes, and even

to  custom  fields.  If  you  want  to  enhance  the  standard logic of the change controller

85


for  determining  changes  to  business  documents,  you  must  make  the  necessary

settings for the following BAdI:

## Determination of Changes for Change Controller

SAP  TM  provides  a  set of predefined change strategies. You use strategies to define

complete  processes.  Methods  define  the  individual  process  steps  of  a strategy. You

can  also  define  your  own  strategies  and methods, and in doing so, the way in which

your process is executed.

If the system is unable to process a change controller strategy due to a locking issue,

you  can  use  the  background  program  /SCMTMS/PROCESS_TRIGGER_BGD  to

reprocess the strategy.

The  configuration  settings  relating to how changes should be processed on a freight

unit,  freight  order,  or  freight  bookings  are  located  in  the  type  customizing  of  these

documents. You can specify the change controller settings for the business document

types in SAP TM Customizing:

86


●  Default  Change  Strategy:  You  can  assign  a  default  change controller strategy

(default strategy) to each business document type. If you have defined several

change  controller  strategies,  you  can  use  a  condition  for  determining  the

adequate change controller strategy.

●  Strategy  Determination  Condition:  If  you  indicate  a  strategy  determination

condition,  the  system  uses  the  change  strategy  found  via  the  condition.  The

system  determines  the  change  controller  strategy  at  runtime  based  on  the

strategy  determination  condition.  If  you  do  not  indicate  a  condition  or  if  the

condition does not return a strategy, the system automatically uses the default

change strategy.

●  Quantity  Tolerance  Determination  Condition:  You  can  use  a  tolerance

determination  condition  to  determine  tolerances  that  are  to  be  taken  into

account in the case of a quantity change in a business document (freight unit,

freight  booking,  or  freight order). This means that if a quantity is changed, the

change  controller  evaluates  this  condition  to  dynamically  check  if  a  quantity

change  can  be tolerated. If no condition of this type is assigned to a business

document,  only  the  standard  logic  to  classify  quantity  changes  is  processed.

The standard logic classifies all quantity changes as relevant quantity changes.

This  means  that in case of a quantity change, the change controller evaluates

this condition to dynamically determine if this quantity change can be classified

as  relevant  or  if  it  can  be  ignored.  You  assign  this  quantity  tolerance

determination  condition  to  your  business  document type (for example, freight

unit  type).  The  result  of a tolerance determination condition has an impact on

the  evaluation  of  the change controller condition that is assigned to the same

business  document  type.  The  indicator  for  a  quantity  change that is provided

as a data access definition to the change controller condition can change from

"Relevant  Quantity  Change  Determined"  to  "No  Relevant  Quantity  Change

Determined" if the quantity change is within the tolerances found.

●  Date  tolerance  determination  condition:  You  can  use  a  date  tolerance

determination  condition  to  determine  the  tolerances  for  a  date  change  in  a

business  document.  This  means  that  in  case  of  a  date  change,  the  change

controller evaluates this condition to dynamically determine if this date change

87


can  be  classified  as  critical  or  uncritical  or  if  it  can be ignored. If you want to

classify  date  changes  according  to your own logic, you can use this condition

to  enhance  the  standard  logic.  If  no  condition  of  this  type  is  assigned  to  a

business  document  (freight  unit,  freight  booking,  or  freight  order),  only  the

standard  logic  to  classify  date  changes  is  processed.  The  standard  logic

classifies  all  date  changes  as  critical  changes.  You assign this date tolerance

determination  condition  to  your  business  document type (for example, freight

unit type). The result of a date tolerance determination condition has an impact

on  the  evaluation  of  the  change  controller  condition  that  is  assigned  to  the

same business document type. The indicator for a date change that is provided

as a data access definition to the change controller condition can change from

"Critical  Change" to "Non-Critical Change" or "No Change" if the date change is

within the tolerances found.

88


Unit 4 - Transportation Planning Preparation

Lesson 1 - Transportation Planning

## Reasons for Transportation Planning

The  goal  of  SAP  TM  is  to  provide  customers  with  the  ability  to  either  manually  or

automatically plan and optimize their transportation requests. This includes the ability

to  perform  order  consolidation,  where  a  company  can  group  orders  with  the  same

ship-from and ship-to locations for more efficient transportation quantities. If multiple

orders  are  being  shipped  within a predefined transportation zone, your company can

try  to  efficiently  schedule  and  route  the  multiple  orders,  and  choose  the appropriate

carrier.  The  planning  and  selection  can  be  determined  using  the  most cost-effective

and  timely  route  from  source  to destination while considering real-world constraints,

costs,  and  penalties.  The  optimizer  makes  multimodal  decisions  such  as  sea,  air,

truck,  train,  and  any  combination  thereof.  The  SAP  TM  planning  function  can  also

perform multipickup and stop options.

Transportation  planning  activities  in  SAP  TM  can  be  performed  manually  and

automatically  as  well as interactively and in the background. For interactive planning,

the  central  planning  UI  is  the  transportation  cockpit.  Both  manual  and  automatic

planning activities are performed based on planning strategies (for example, one-step

optimization).

## Order Consolidation

Order  consolidation  is  the  grouping  of  orders  with  the  same  ship-from  and  ship-to

locations to create more efficient shipment quantities.

The  result  of  order  consolidation  is  that  one or more freight units are combined into

one freight order. A freight unit is a business object representing the smallest possible

transportation unit. Business examples of order consolidation are multiple orders that

have  been  received  over  time  and  can  be shipped together. This can be at individual

line item level. Customers who make-to-order, and do not ship complete orders to their

89


customers, can consolidate line items from multiple orders as they are produced and

as their delivery-due lists are created.

## Routing and Scheduling

The  figure  outlines  the  process  of  routing  and  scheduling  in  the  following  way:  a

freight unit X is first routed using the transportation planning function, for example, a

transportation proposal. Based on this routing, three stages are created for freight unit

X, as follows:

●  A stage for U.S. road pickup transport

●  A stage for the ocean voyage

●  A stage for EU road delivery transport

Up  to  a  certain point, these stages are planned independently of each other because

different  (local)  planners  are  responsible  for  scheduling  each  of  the  three  stages.  A

freight order is created as a result of this stage. Finally, carriers are selected based on

specific  criteria.  This  is  described  as  a  three-step  process  but  a  planner  can  decide

whether  to  perform  planning  and  carrier  selection  in  two  steps  or  three.  It  is  also

possible  for  the  SAP TM optimization function to plan all three steps in one run–this

planning strategy is called one-step optimization.

90


## Process Steps

The steps involved in the process, whether one, two, or three steps, can be described

as follows:

●  Three step

1.  Determine routing (transportation proposal)

2.  Vehicle scheduling and routing to create a freight order

3.  Carrier selection

●  Two step

1.  Vehicle scheduling and routing to create a freight order

2.  Carrier selection

●  One step

One-step  optimization  determines  the  route  and  plan,  creates  a  freight  order

and selects a carrier

## Manual and Automatic Transportation Planning

Transportation  planning  activities  in  SAP  TM  can  be  performed  manually  and

automatically, as well as interactively and in the background. For interactive planning,

the  central  planning  UI  is  the  transportation  cockpit.  Both  manual  and  automatic

planning activities are performed based on planning strategies (for example, one-step

optimization).

91


## Planning Constraints

SAP TM can consider numerous constraints during planning. Which ones are relevant

and  can  be  used  in  a  specific  scenario  largely  depends  on  the  scenario  itself.

Constraints  can  have  physical  root  causes,  such  as  vehicle  capacity  or  handling

capabilities  for  loading  and  unloading  at  certain  facilities.  On  the  other  hand,

constraints  can  have  process-related  root  causes.  For  example,  a  delivery  tour  can

have  a  maximum  of  25  drops in a day. This is a maximum that fits in a driver’s daily

schedule, assuming they have to unload at the door and do some paperwork for each

customer drop.

Assets, Facilities, Resources, and Times
There are various assets, facilities, resources, and times:

●  Vehicle capacity

●  Vehicle combinations (truck and trailer)

●  Compartments

●  Depot locations

●  Handling resources, opening hours (calendars and shift patterns)

●  Schedules

●

Incompatibilities – constraints by design

## Process and Execution Constraints
There are various process and execution constraints:

●  Decreasing capacities

●  Max number of transshipment locations

●  Max limits on distance, duration, or stopovers

●  Pickup and deliver time windows

●  Min and max storage time at hub – cross-docking changeover

●  Loading and unloading durations

●  Scheduling constraints

## Freight Orders

The  freight  order's  execution  is  planned  by  a  carrier  or the shipper. The freight order

contains the following:

92


●  When and onto which vehicle freight units are to be loaded

●  Planned departure times for the vehicle

●  Execution data

Freight  orders  are used for land transportation and freight bookings are used for sea

and air transportation. Freight orders contain the following information:

●  Planning  information,  for  example,  planned  means  of  transport  and  stages,

routing, planned pickup and delivery dates, durations, and distances

●  Document dependencies, as well as predecessor and successor documents

●  Transportation charges and cost distribution

●  Cargo information: quantities and weights, goods information

●  Execution information

●  Business partner information

●  Output management

●  Status information and blocking information

●  Subcontracting information

Methods/Ways of Creating Freight Orders:

1.  Manually: Manual creation is used when you already know the most important

transportation data, such as source location, destination location, and business

partner,  because  you  regularly transport goods for a certain customer using a

certain carrier.

2.  Work-list:  Some  of  the  information,  like  source  and  destination  location,  are

automatically populated in the freight order if you create the freight order from

the freight unit work-list.

3.  Copying: You can create a freight order by copying an existing one (a reference

document).  The  system  copies  the  header  data  and  the  logistical  data.

However, it does not copy references to freight units and execution information.

4.  FUBR  rule:  You  can  create freight orders via the short-cut process based on a

freight  unit  building  rule,  which  will  be  explained  in  more  detail  later  in  this

lesson.

5.  The  more  advanced  features  of  creating  freight  orders  are  their  interactive

creation  in  the  transportation  cockpit,  VSR  optimization,  and  the  use  of

93


transportation  proposal  functionality.  These  topics  are  covered  once  we have

finished the relevant configuration.

A freight order type defines parameters that influence how the system processes the

freight  order.  When  manually  creating  a  freight  order, the user has to select a freight

order  type. If freight orders are created during planning and have associated settings

in  the  planning  profile,  the system determines the freight order type according to the

Customizing settings.

●  Number range intervals

●  Basic Settings:

○  Determining shipper and ship-to-party

○  Specifying if a freight order can be subcontracted

○  Defining whether a freight order is to be deleted or only canceled

○  Define subcontracting relevance

○  Define sequence types:

○  Defined  and  Linear:  The  sequence  of  stages  is  linear,  which

means that there is a single start stage and all other stages have

94


one  predecessor  stage.  There  is  also  a  single  end  stage  and all

other stages have one successor stage.

○  Non-Linear (Star-Shaped): All stages have the same start location

but  different  end

locations.  The  graphical  structure  of  the

transportation chain has a star shape.

○  Disconnected:  All  stages are separate from each other and each

stage has its own start and end location.

○  Star-Shaped Based on FU Stages: Based on the information from

the  freight  units,  the  stages  have  the  same  start  location  but

different  end  locations  (for  example,  for  parcel  freight  orders  or

freight orders for customer pick-up).

○  Star-Shaped  Based  on  FU  Stages  (Reversed):  Based  on  the

information from the freight units, the stages have the same end

location  but  different  start  locations  (for  example,  for  freight

orders for customer self-delivery).

○  Linear  with  (De-)  Consolidation  Stages:  This  sequence  type

contains three parts.

○

In the first part (precarriage), all stages have different start

locations  but

the  same  end

location  at  which

consolidation  takes  place.  The  graphical  structure  of  the

transportation chain has a star shape.

○

In the second part (main carriage), the sequence of stages

is linear.

○

In  the  third  part  (on-carriage),  all  stages  have  the  same

start  location  at  which  deconsolidation  takes  place  but

different  end  locations.  The  graphical  structure  of  the

transportation chain has a star shape.

○  Undefined:  There  is  no  sequence  of  stages  since  there  are  no

stages, only locations.

●  Charge Calculation and Settlement Document Settings:

○  Enabling charges and settlement

○  Enable cost distribution

95


●  Execution  Settings:  You  can  define,  for  example,  whether  the  system  is  to

perform  the  execution  steps  within  Transportation  Management.  You  can

define  more  conditions  that  must  be  fulfilled  so  that  the  status  Ready  for

Execution  can  be  set.  Moreover,  you  can  define  settings  for  integration  with

SAP Event Management.

●  Organizational Unit Determination: You can define how the system determines

the  purchasing  organization  and  the  execution  organization.  The  system  first

checks the Condition field. If you have not entered a condition or if the condition

does  not return a result, the system checks whether the Consider Organization

Unit  of  User  checkbox  is  selected  and  whether  the  user  is  assigned  to  a

purchasing  organization  and  an  execution  organization.  If  the  user  is  not

assigned  to  a  purchasing  organization  and  an  execution  organization,  the

system uses the data maintained in the Default Org Unit area.

●  Change  Controller  Settings:  You  can  define  settings  for  the change controller,

for  example,  a  default  change  strategy  and  a  condition  for  change  strategy

determination.

●  Output  Options:  You  can  define  an  output  profile  and  a  text  schema,  for

example.

## Freight Bookings

Freight  bookings  are  used  to  reserve  freight space on a vessel or in an airplane. The

corresponding mode-specific freight documents are called ocean freight bookings and

air freight bookings. They provide mode-specific information, such as the vessel name

or  flight  number.  The  space  reserved  by  freight  bookings  is  consumed  by assigning

freight units or container units to the bookings.

An ocean freight booking represents ocean transportation from a port of loading to a

port  of  discharge,  and  an  air  freight  booking  represents  air  transportation  from  an

airport  of  departure  to  an  airport  of  destination.  Freight  bookings  can  cover  a

consolidation  location  before  the  source  and  deconsolidation location after the port.

These  consolidation  and  deconsolidation  locations  are  called  container  freight

stations (CFSs) in the ocean case and gateways for the air case.

96


Methods/Ways of Creating Freight Bookings:

●  Manually

●  Work-list

●  Copying

A freight order type defines parameters that influence how the system processes the

freight bookings.

The following are a few differences between freight orders and freight bookings:

●  You  can  create  pickup  and  delivery  freight  orders  for  the  stages  from

consolidation  location  to  source  (air-)  port  and  from  destination  (air-)  port  to

deconsolidation  location,  respectively.  The  freight  booking type can define the

pickup freight order type and delivery freight order type.

●  You cannot assign drivers to bookings.

●  Whereas  freight  orders  allow  star-shaped,  unrelated,  and  other  stage

structures, freight bookings allow only sequential stages.

97


●  Freight  orders  cover  self-delivery  and  self-pickup  scenarios,  which  are  not

relevant for freight bookings.

All  booking  types  can  be  subcontracted, in contrast to freight order types, which can

forbid  subcontracting  to  cover  transportation  businesses  fully  relying  on  their  own

fleets.  Although  carrier  selection  and  tendering  are  offered  for  freight  orders,  only

carrier  selection  is  possible  for  freight  bookings.  In  most  scenarios,  the  carrier  is

already known at the time of booking creation.

98


Lesson 2 - Selection and Planning Profiles

## Selection Profile

Freight units (FUs) are selected based on the dates and times that they were originally

scheduled to be picked up (loading start) and delivered.

Within  each  section,  you  define  an  inclusive  or  exclusive  set  of  location  values  that

determine  which  FUs  are  relevant  for  planning.  Each  section  allows  users  to  define

specific values or ranges of values. Using these parameters of greater than, less than

or not equal to users are able to define precise criteria for planning.

Selection  profiles  are  used  to  select  documents/objects  (FUs,  freight  orders  (FOs),

freight  bookings,  and  transportation  units).  The  selection  profile  is  a  user-specific

grouping  of  business  documents  that  is  considered  during  transportation  planning.

The  system  takes  into  account  the  selection  profile  created  during  interactive

planning, VSR optimization, and carrier selection.

In  the  selection  profile  and  in  the  assigned  selection  attributes,  you  define  which

business  documents  the  system  is  to  take  into  account,  as  well  as  the  maximum

99


number of documents. You can assign the following selection attributes to a selection

profile:

●  Time-related selection attributes in which you define the demand Horizon.

●  Geographical  selection  attributes  in  which  you  define  source  and  destination

locations or zones.

●  Additional selection attributes in which you define more attributes for database

queries.

Geographical  Selection Attributes: In a company’s planning department, geography is

often  used  as  a  way  to  allocate planning responsibility. For example, an individual or

team can be responsible for a specific plant, distribution center, or group of customers

in  a  geographical  area.  The  geographical  selection  attributes  in  the  selection  profile

allow the team to limit their view in such a way that they only see FUs or FOs for which

they have responsibility.

The  geographical  profile  distinguishes  which  source  and  destination  locations  are

relevant for FU selection. The geographical profile is split into four sections:

●  Source Locations

●  Source Transportation Zones

●  Destination Locations

100


●  Destination Transportation Zones

Within  each  section,  you  define  an  inclusive  or  exclusive  set  of  location  values  that

determine  which  FUs  are  relevant  for  planning.  Each  section  allows  users  to  define

specific  values  or  ranges  of  values,  using  the  logical  greater  than,  less  than,  or  not

equal to, to provide precise planning.

Time-Related  Attributes:  You  can  define  the  demand  Horizon as absolute or relative.

With  absolute  time  periods,  you  define  the  demand  Horizon  precisely  by  defining  a

start and end date and a start and end time (calendar date). If using relative times, you

do not define the demand Horizon with precise dates and times, but specify instead a

duration  starting  from  the  current  date.  The  system  automatically  determines  the

start and end date and the start and end time. If the demand Horizon is not to start on

the current date, you can define an offset.

The relative demand Horizon is then defined as follows:

●  Start of demand Horizon = current date + defined offset. The offset is made up

of the offset in days and the additional offset in hours and minutes.

●  End  of  demand  Horizon  =  start  of  demand  Horizon  +  defined  duration  of

demand  Horizon.  The  duration  of  the  demand  Horizon  is  made  up  of  the

duration in days and the additional duration in hours and minutes.

101


If  you  specify  a  factory  calendar,  the  system  considers  nonworking  days  when

calculating  the  start  of  the  Horizon.  In  this  situation,  the  planning  Horizon  always

begins on a working day.

You  can  round  the  Horizon  to  full  days  and  define  the  time  zone  to be used for this

rounding.

Additional Selection Attributes: More selection criteria can be defined using additional

selection attributes. You can select objects and their fields and the criteria.

## Planning Profile

Planning  profiles  are  used  to  influence  and  control  the  outcome  of  the  planning

process.  A  planning  profile  must be specified for a background optimizer run as well

as  for  interactive  planning  (manual  planning)  in  the  transportation  cockpit.  During

planning,  the  system  considers  the  settings  that  you  make  in  the  various  planning

profiles.

A  user  defines  various  settings  on  the planing profile. These settings determine how

planning is to be performed. Settings belonging to a certain area are grouped together,

for  example,  all  the  settings  required  for  load  planning  are  grouped  under  load

planning settings. The following figures show the eight settings that are defined in the

102


planning  profile. All these settings can be maintained independently and can be used

for other planning profiles as well.

In  addition  to  these  settings,  the  following  functionality  is  defined  in  the  planning

profile as well:

●  Planning  Horizon:  The  planning  Horizon  defines  the  Horizon  in  which  new

freight documents can be created by planning. The planning Horizon is defined

in the planning profile in days, hours, and minutes. The planning Horizon starts

103


at  the  current  system  time  unless  an  offset  is  defined  in  the  planning profile.

The offset can be defined in both the past and the future.

●  Default  Business  Document  Type:  The  business  document determination rule

defines  which  document  types  are  used  when  freight  orders  and  freight

bookings  are  created  during  planning.  The  business  document  determination

rule  is  defined  for  each  planning  profile  and  applies  to  documents  created

either manually or by the VSR optimizer. Freight order type and freight booking

type can be determined in the following three ways:

○  The default type is defined in customizing

○  The type is defined in the planing profile directly

○  A condition can be used to determine the result

●  Check:  The  check  defines  the  check  strategy  and  for  handling  capacity

violation.

●  Package  building  profiles:  The  package  building  profile  is  a  collection  of

parameters  with  which  you  control  the  creation  of  packages.  When  you  are

doing package building based on the capacity documents, then you assign the

package  building  profile to the planning profile. The package building profile is

defined in customizing.

●  Parallel  processing  profiles:  By defining parallel processing the runtime for big

optimization  scenarios  can  be  reduced.  The  parallel  processing  profile  is

defined in customizing and assigned to the planning profile.

Strategies:  The  planning  profile  includes settings to control the different steps

of  the  optimization.  These  steps  are  controlled  by  strategies.  Strategies  are

made  up  of  various  programs.  If  you  wish  to  perform  manual  planning  or  a

scheduled  planning  run,  there  is  a  standard  strategy  for  each  function.

Standard  strategies  are  delivered  by  SAP.  However,  unique  strategies  can  be

created using a process controller.

●

1.  Capacity  selection  settings:  The  capacity  selection  settings  define  which

vehicle  resources,  containers,  drivers,  and  schedules  are  selected  for

transportation planning. This setting involves selecting the resource capacity in

the  transportation  cockpit.  Schedules  are  also  selected  based  on  the  criteria

104


defined  in  the  capacity  selection  settings.  The  mode  of transportation can be

maintained  explicitly.  Many  fields  in  the  resource  can be used for selection. A

few of them are listed below:

●  Location

●  Equipment types

●

ID

●  Planning Block

●  Resource owner

Note: If you use resources for which you have defined an ADR limit, VSR optimization

takes into account the number of ADR points for this resource during the optimization

run. Moreover, you can specify that resources for which you have set a planning block

are not displayed in the resource lists of the transportation cockpit.

Note:  The  Agreement  concerning  the  international  carriage  of  Dangerous  Goods  by

Road  (ADR)  is  an international standard governing the transport of dangerous goods

by road. The agreement describes an exemption based on the calculation of points for

dangerous  goods.  If  the  points  total  calculated  according  to  the  method  described

does not exceed 1000 points, the exemption can be applied.

2.  Optimizer  Settings:  Here,  you  can  define  the  optimizer runtime, the maximum

number  of  transshipment  locations  and  processes,  and  the  freight  order

building  rule,  for  example.  You  also  specify  whether  you  require  rough  or

detailed  information  for  your  planning  activities,  define  the  required  process

controller  strategy,  and  configure  the  settings  for  generating  transportation

proposals.

SAP  delivers  the  planning  strategies  VSR_DEF  and  VSR_1STEP  as  standards

for  the  optimization.  You  can use the planning strategy VSR_1STEP to control

whether  the  system  is  to  perform  carrier  selection  immediately  after  VSR

optimization.  The  results  of  the  VSR  optimization  run  are  explained  in  the

explanation tool.

In  the  advanced  settings,  you  can  also  specify  whether  the  main  aim  in  your

transportation  proposals  is to ensure the lowest transportation costs possible

or the shortest transportation duration possible, based on the planned delivery

105


date/time. You can also define preferences in relation to your relative weighting

of the variance of carriers, routes, and departure dates, or activate or deactivate

capacity constraints at transportation mode level. You can also specify whether

the  system  is to ignore certain settings such as the capacity or ADR limit of a

resource during VSR optimization.

VSR  optimization  generates  a  transportation  plan  from  the  optimization  data

consisting  of  planned  freight  orders.  It  processes  freight  orders  already

available  from  a  previous  VSR  optimization  run  or  manual  planning.  VSR

optimization  inserts  the freight units into the transportation plan and modifies

these  initial  solutions  by,  for  example,  loading  a  freight  unit  on  to  another

capacity or by changing the delivery sequence of a capacity.

The  optimizer  tries  to  minimize  the  total  costs  while  adhering  to  the

constraints.  At  the  end  of  the  planning  run, VSR optimization returns the best

solution  found.  You can generate multiple alternative transportation proposals

for each freight unit. You can then choose to use one of them.

3.  Load  optimization settings for: Here, you can define the optimizer runtime, the

planning  strategy,  and  various  rules  for  load  planning.  For  example,  you  can

define  the  maximum  height  difference  between  stacks  in  a  row,  stack  height

ascending  in  the  driving  direction.  The  standard  strategy  used  for  load

optimization is ALC_DEF.

4.  Constraints  and  costs  settings:  Here,  you  define  costs  related  to  freight units

and means of transport. Usually, these costs are not actual costs. They simply

offer  a  means  of  controlling  the  results  of  the  optimization  run  (for  example,

earliness costs and lateness costs).

5.  Incompatibility settings: Here, you define settings for your incompatibilities.

6.  Carrier  selection  settings:  Here,  you  specify  whether  the  system  is  to  use

transportation  allocations  or  business  shares.  The  planning  strategy  used for

carrier  selection

is  TSPS_DEF.  An  additional  strategy  for  cost,  priority,

cost+priory or cost* priority is defined.

With Cost +Priority, Carrier 1 is ranked highest.

With Cost*Priority, Carrier 2 is ranked highest.

106


Carrier(s)

## Cost

## Priority

Cost+Priority

Cost*Priority

Carrier 1

1000

20

1020

2000

Carrier 2

1100

10

1110

11000

Carrier 3

1200

30

1230

36000

7.  Settings  for  manual  planning:  Here,  you  specify  how  you  want  the  system  to

behave when it assigns documents and resources:

●  Assignment  of  documents:  You  use  these  settings  to  control  how  the

system  is  to  assign  one  or more requirement documents to a capacity

document.

●  Removal  of  the  assignment  of  documents:  You  use  this  setting  to

control  how  the  system  is  to  remove  the  assignment  of  requirement

documents to capacity documents.

●  Assignment  of  resources  and  creation  of  documents:  You  use  these

settings to control how the system is to assign resources to documents

and how it is to create and assign reference documents.

●  Driver  Assignment:  You  use  these  settings  to  control  how  the  system

assigns trucks to the drivers.

8.  Scheduling  Settings:  You  define

loading  and  unloading  durations  for

scheduling. The schedule strategy defines the actions that are performed when

scheduling

is

launched  for  a  freight  order  or  freight  booking

in  the

transportation  cockpit.  The  standard  strategy  used  for  scheduling  settings  is

VSS_DEF.  The  schedule  strategy  is  assigned  to  the  planning  profile.  Here,  we

define  if  the  system  considers  the  dates  in the freight unit as constraints and

whether a backward or forward scheduling direction is used.

107


## Lesson 3 - Transportation Cockpit

The  transportation  cockpit  is  the  main  UI  for  performing  planning.  Transportation

planning,  including  freight  order  (FO)  creation,  is  conducted  in  the  transportation

cockpit.  Transportation  requirements  lists  (freight  units  (FUs)), capacity lists (vehicle

resources  and  schedules),  order  lists,  and  order  details  can  be  all  seen  in  the

transportation cockpit. The following are transportation cockpit tasks:

●  Manual planning

●  Creation of transportation proposals

●  VSR optimization

●  Load planning

●  Carrier selection

●  Triggering of a tendering process

●  Creation of delivery proposals

●  Creation of freight bookings

The  cockpit  requires  users  to  enter  several  profiles  that  govern  the  content  of

generated  result  lists.  The  selection  profile determines what is to be planned, that is,

what  FUs  or  FOs  are  pertinent  for  a  particular  objective.  The  planning  profile

determines how the selected FUs are planned. The capacity selection profile restricts

the planning run in relation to the transportation resources that can be used. Once the

108


profiles have been determined, planners can use the cockpit to create freight bookings

or manage existing FOs.

The  transportation  cockpit

is  dynamic  and  can  be  configured  as  per  users

requirements. The transportation cockpit layout offers flexible settings to control what

information is presented and the processing options available. Depending on the user

requirements,  certain  elements  can  be  hidden  or  visible on a page. Page layouts are

used to define a view the user wants to see during planning. A page layout defines the

buttons,  functions,  levels,  and  hierarchies  that  are  displayed  in  the  transportation

cockpit, carrier selection, and delivery creation application UIs.

A  combination  of  selection  and  planning  profile  together  with  a  page  layout  can  be

assigned to a profile and layout set, such that this specific planning scenario is always

shown  in  this  layout,  while  another  planning scenario requires another layout. Profile

and layout sets are used to distinguish between different planning areas or functions.

One profile and layout set can be assigned as the default. Such a profile and layout set

is  based  on  the  specific  information  requirements  of  a  planner.  For  example,  in  one

scenario,  a  planner  has  to  plan  liquids  on  tank  trucks  and  must  be  able  to  see  the

volume  of  product,  while  in another scenario, the liquids are in barrels on pallets and

the  planner requires the pallet count to be displayed. It is possible to switch between

different  layouts  on-the-fly,  for  example,  if  a  multistep  planning  process  leads  to

different needs in each step. The following are a few examples of different layout sets:

109


●  A set for a planner who plans the next day

●  A set for a dispatcher who makes the planning changes for today

●  A set for an air and ocean planner

●  A set for carrier selection

●  A set for each area planner per country or region

In  the  standard layout, the main screen is broken up into four quadrants (views). The

maximum  number  of  views  in  any  layout  is  6.  If  a  user  works  with  several  screens,

they can choose a separate layout for each screen. The transportation cockpit can be

deployed  in  multiple  windows  on  up  to  three  screens.  Note  2551221  provides

additional information on this topic:2551221.

Hierarchical  view:  You  organize  the  view  in  the  transportation  cockpit  by  creating

hierarchical  views  for  FOs,  freight  bookings,  and  transportation  units  (trailer  units,

rail-car  units,  container  units,  and  package  units).  If  you  organize  these  business

documents into hierarchies, you can filter and sort various areas in the transportation

cockpit  according  to  specific  criteria,  such  as  the  vehicle  resource.  Defining

hierarchical  views  simplifies  your  rescheduling  activities  and  the  coupling  and

uncoupling of trailers. The following notes provide additional information on this topic:

●  2768608

●  2182927

Maps: The map can be displayed as one screen area in the transportation cockpit or in

full  screen.  However,  having  the  map  displayed  as  one  screen  area  enables  the

planner  to  directly  see  the  selected  FUs,  FOs  or  bookings,  transportation  units,  and

resources on the map. You can perform the following actions on the map:

●  Address Search: You can use the context menu of the map to start the address

search and display the search results on the map. The address search is based

on  the  geocoding  of  the  location.  This  allows  you  to perform several address

searches  and  display  the  search  results  simultaneously  on  the  map.  You can

use  the  context  menu  of  the  map  to  hide  the  search  results  individually  or

completely.

110


●  Route Display: You can use the context menu of a connection line to determine

a  route  display  along  real  street  routes.  This  function  depends  on  the

geographical information system available in the system. Alternatively, you can

use  the  context  menu  of  a  resource  to display the connection lines of all FOs

assigned to this resource.

●  Dynamic  Adjustment:  You  can  adjust  the  map  display  to meet your individual

needs  by  selecting  the  option  Show  Display  Profile  from the context menu for

the map. For example, you can specify whether map objects are to be shown or

hidden, whether you want to display the descriptions, and whether you want to

allow clustering for overlapping nodes.

●  Create  Location  and  Transportation  Zone:  You  can  use  the  context  menu  for

the map to create locations and transportation zones directly on the map. The

locations  or  transportation  zones  are  created  where  you  open  the  context

menu. However, you cannot use the context menu to change the positioning of

an object on the map.

●  Proximity  Search:  You can use the context menu of the map to find resources

as  well  as  unplanned FUs or transportation units that are close to a particular

point on the map.

●  Resource Item: You can use the context menu of the map to specify the exact

location of a resource at any time.

●  Differentiate  Between  Business  Documents  Using  Colors:  You  can  use  the

context  menu  of  the  map  to  display  different  colors  for  multiple  business

documents  selected  simultaneously.  This  enables  you  to  better  differentiate

between the documents. The color of each respective document is displayed in

the Color column in the document list.

Gantt  Chart:  The  Gantt  chart  is  fully  integrated  into  the  transportation  cockpit.  The

Gantt  chart  is  a  screen  area  in the transportation cockpit, which can be enabled in a

page  layout  of  the  transportation  cockpit.  You  can  also  update  maps,  generate

transportation  proposals,  and  run  optimizer  planning  for  the  selected  items  in  the

Gantt  chart  and  in  the  lists  and  hierarchies  of  the  transportation  cockpit.  The  Gantt

chart has the following features:

111


●  Transparent availability of resources and drivers: The chart panel presents you

with  an  overview  of  the  availability  of  vehicle  resources,  handling  resources,

and  drivers  over  time.  For  example,  different  colors  indicate  whether  a  truck

has  a  document  assigned  to  it,  or  whether  it  is  traveling,  in  downtime,  or  in

nonworking time. You can also check whether a handling resource is available

or  in  downtime  at  a  location  and  if  drivers  are  available  or  if  they are absent.

You  can  use  the  Operating  Time  Calendar  hierarchy to visualize the operating

time  configured  for  a  specific  location.  The Operating Time Calendar displays

the  nonworking times and activities occurring in that location. These activities

are:  loading,  unloading,  prepare,  and  finalize.  The  hierarchy  also  displays  the

overlaps between loading activities.

●  Visibility  of  utilization  of  resources:  You  can  display  the  level  of  consumed

capacity  of  a  vehicle  resource at a specific point in time. The system displays

the  utilization  curve  of  the  selected  vehicle  resource  in  the  chart  panel.  The

tool-tip  along  the  utilization  curve  displays  the  loading  utilization  of  a  vehicle

resource  in  terms  of  volume,  weight,  alternative  quantity,  or  normalized

quantity,  depending  on  your  settings  in  customizing.  The  tool-tip  along  the

utilization  line  of  a  handling  resource  presents  you  with  information  on  the

available capacity, required capacity, and overcapacity of this handling resource

at  a  specific  point  in  time. You can display loading or unloading activities that

are planned for a handling resource at different times.

●  Option  to  display  or  hide  document  separators  in  the  Gantt  chart:  The  Gantt

chart presents you with document separators indicating the precise document

start  and  document  end.  You  can  choose  to  display  or  hide  document

separators  in  the  Gantt  chart  by  selecting  the  corresponding  checkbox  in  the

legend  area.  Document  separators  apply  to  the resources (truck, trailer, driver,

locomotive, rail-car, and container).

●  Option  to  display  or  hide  time  windows  in  the  Gantt  chart:  The  Gantt  chart

presents you with time windows indicating when goods are to be picked up and

delivered. In the Gantt chart, time windows are shown as dotted lines and solid

lines. You can choose to display the time windows by using the corresponding

check-boxes in the legend area.

112


●  Option  to  display  and  solve  warnings  in  the  Gantt  chart:  The  Gantt  chart

presents you with warnings such as the Missing Stage warning or the Incorrect

Driver Assignment warning that are indicated by a warning icon. You can solve

a warning using the context menu. You can choose to display or hide this type

of  warning  in  the  Gantt  chart  by  selecting  the  respective  checkboxes  in  the

legend. The legend area also displays the number of warnings for each warning

type. Moreover, the number is dynamically updated once a warning of a certain

type  is  solved  or  generated.  Besides  of  the  legend  area,  the  Number  of

Warnings column in the table area shows you the total number of warnings on

each row in a real-time manner. You can also deselect a certain warning type in

the  legend  area  so  that  warnings  of  that  type  are  not  considered  when

calculating the total number.

●

Insights  into  planning  and  execution  status  of  documents  and  transportation

activities:  If  you  transfer  event-related  data  from  SAP  Event  Management  to

SAP  Transportation  Management,  you  can  gain  real-time  insights  into  the

planning  status  and  execution  status  of  the  documents  and  transportation

activities  in  the  chart  panel.  The  statuses  of  documents  and  activities  are

presented  in  predefined  colors  and  patterns,  as  described  in the legend. Note

that  the  Gantt chart automatically hides a legend item in the legend area if no

corresponding documents or activities are shown in the chart area.

●  Flexible and dynamic switch between different views: You can switch between

a  single  view  and  a  dual  view (with its horizontal and vertical versions). In the

chart  panel  of  each  view,  you  have  the  option  to switch between a document

view  and  an  activity  view.  The  dropdown  lists and the related push buttons in

the  toolbar  enable  you  to  switch  dynamically  between  views  and  hierarchies

that  are predefined in Customizing. For example, in a horizontal dual view, you

can  choose  to  display  FOs  in  the  upper  view  and  trucks  in  the lower view, so

that you can assign unplanned FOs to trucks using drag and drop.

●  Flexible  rendering  of  hierarchical  structures:  You  can  simplify  the  hierarchical

structure  of  document  flows  in  Customizing  so that stage documents can be

directly  shown  under  a  higher-level  parent,  instead  of  their  direct  parent.  This

provides you with more flexibility to render document flows in the Gantt chart.

113


●  View all objects with one click: Bird Eye provides you with the capability to have

a  panoramic  view of all objects with one click. With this feature turned on, the

system intelligently adjusts the zoom rate so that all items are displayed on the

chart  without  a  need  to  move  the  horizontal  scroll  bar.  This  feature  can  be

implemented on all rows or just on visible rows. This can be configured in Gantt

Chart customizing.

●  Personalize table area appearance: You can personalize the appearance of the

table area with the following options:

○  Display or hide a column

○  Modify the column sequence

○  Adjust the column width

●  Moreover,  you  can  save  all  personalization  settings  as  a  variant  so  that  the

table  area  is  presented  with  the  saved  settings  for the next time you load the

Gantt chart.

●  Configurable  visualization  of notifications: You can define the color and height

of a certain type of notifications in the Gantt chart. Moreover, you can configure

when  to  display  the  following  types  of  notifications  by  specifying  a utilization

range value of vehicle resources:

○  Empty run

○  Low utilization

○  Overcapacity

## Transportation Cockpit Customization Settings

The following changes can be made to the layout of the transportation cockpit:

●  The time zone in which to present time-related information

●  Unit for distance

●  The position and width of the tabs on the screen

●  The visibility of tabs

●  The sequence and number of rows and columns are visible

You  can  change  the  layout  to  suit  your  requirements  by  choosing  the  Page  Layout

button. For example, you can change to a layout that displays the command line and

so allows command line planning.

114


Unit 5 - Interactive Transportation Planning

Lesson 1 - Performing Interactive Planning

## Drag and Drop Freight Order Creation

Manual planning is done in the transportation cockpit. Manual planning allows you to

manually create or change a transportation plan. To create a transportation plan, you

assign  requirement  documents,  for  example  freight  units  (FUs),  to  capacities,  for

example  vehicle  resources.  The  system  creates  capacity  documents,  for  example

freight  orders  (FOs),  which  you  can  process  further.  For  example,  you  can  assign

drivers  to  your  FOs  or  perform  load  planning.  If  you  assign  FUs  to a container, for

example, a container unit is created that you can directly assign to a freight booking.

Planning  strategies  determine  the  steps  that  the  system  is  to  carry  out  during  the

planning  process  and  the  order in which it does so. In the planning profile, you can

specify  which  planning  strategy  you  want  to  use.  The  following  are  a  few  manual

planning strategies:

●  VSRI_DEF for manual planning

●  VSS_EMBED  for  embedded.  This  strategy  does  not  consider  scheduling

constrains defined in customizing

●  VSRI_SCH for manual planning with subsequent scheduling

●  VSRI_1STEP for manual planning with carrier selection

Drag and Drop FO Creation:

A  FO  can  be  created using the drag-and-drop functionality. Dragging an unplanned

FU stage to a resource or dragging a resource to an unplanned FU stage creates a

FO.  Changes  to  existing  documents  can  also  be  made  using  drag  and  drop.  It  is

possible  to  drag  extra  FU  stages  to  a  FO.  FUs  can  be  assigned  from  one  freight

document  to  another.  Blank  capacity  documents  can  be  created  (that  is,  capacity

documents that do not contain a FU), which you can then process later. It is possible

to drag and drop between various hierarchy levels.

The main drag and drop functionalities are as follows:

115


●  Change the relative stop sequence of a FO or transportation unit

●  Reassign the stop to a different vehicle, FO, or transportation unit

●  Reschedule a FO or transportation unit

●  Assign a FO or transportation unit to a resource (truck or trailer)

Manual planning can be done with multiple windows. The transportation cockpit can

be deployed in multiple windows on up to three screens.

●  Run  the  transportation cockpit on multiple windows. Select a separate layout

for each screen.

●  Drag  and  drop

from  any

list/hierarchy

in  one  window  to  any  other

list/hierarchy.

●  Actions  triggered  from  the  global  toolbar  (for  example,  undo,  redo,  assign

selected  items,  update  map,  or  optimization)  consider  selected  objects  from

all windows.

●  A change in one window automatically updates the other windows.

## Command Line Freight Order Creation

Command Line Freight Order (FO) Creation: The command line enables mouse-free

planning  and  is  an  alternative  to  drag-and-drop  planning.  Using the command line,

the  planner  instructs  the  system  to  assign  freight unit (FU) stages to vehicles via a

single character string.

To  enable  command  line  planning,  an  index  is  assigned  to  each  resource  and  FU

stage.  The  index  acts  as  a  unique  identifier  for  every  object  in  the  transportation

116


cockpit.  Note  that  vehicle  resources  are  assigned  low  numbers so that the planner

can easily remember them.

Planning  with  the  Command  Line:  When  planning  with  the  command  line,  the

planner  first  enters  index  numbers  that  represent  the FU unit stages, followed by a

dash  (-)  and  a  vehicle  resource  index.  Press  Enter,  and  a  FO  is  created  with  the

relevant stages and resources assigned. Multiple commands can be specified in one

string by using a plus (+) sign to separate them.

## Example: Simple Planning of FUs on a Vehicle Resource

The  FUs  that  you  want  to  plan  have  the  indexes 5, 6, and 7. The vehicle resource

that you want to use to transport the FUs has an index of 2. To assign the FUs to the

vehicle resource, you enter the following command in the command line: 5 6 7 — 2.

The following are prerequisites for using command line planning:

●  The display of the command line must be activated for the page layout for the

transportation cockpit.

●  The  index  field  should  be  displayed  for  the  FU  stages  and  vehicles  in  the

transportation cockpit.

The  help  field  of  the  command  line  provides  additional  information.  Choose  More

Field Help in the context menu for the field by clicking the right mouse button.

## Interactive Map Freight Order Creation

Interactive  Map  Freight  Order  (FO)  Creation:  FOs  can  be  created  using  the

interactive  map.  Freight  unit  (FU)  stages  and  vehicles  are  both  displayed  on  the

map.

117


You  can  carry  out  your  planning  activities  on  the  map.  If  you  select  Unplanned

Freight  Units  and  Start  Planning  from  the  context  menu,  for  example,  the  system

shows the possible assignments of the FUs to the resources. Select the assignments

that you require.

You can also assign unplanned FUs or multirelations that contain unplanned FUs to

resources by using drag and drop. When you do so, you can either assign the FUs to

the resource or the resource to the FU.

If  you  want  to  split  a  stage  that  is  displayed  on  the  map,  you  can  assign  an

unplanned  FU  or  multirelation  to  a  location  using  drag  and  drop.  Once  you  have

selected  the  required  planning  option,  the  system  adds the selected location to the

FU unit stage and updates the map accordingly. This process also applies to FOs.

You  can  also  display  transshipment  locations  that  are  not  part  of  your  planning

activities. You can display these locations by choosing Show Related Transshipment

Locations from the context menu.

If a FO does not have a vehicle assigned to it, you can also assign the vehicle using

drag  and  drop.  To  do  so,  you  assign  the  FO  to  a  single  vehicle  resource  or  a

multispot  that  contains  at  least  one  vehicle  resource  or  passive  vehicle  resource.

Then select the relevant planning option from the menu.

118


The  system  displays all of your transportation planning activities on the map. When

you  leave  the  full  display  of  the  map,  your  planning  activities  are  also displayed in

the table view of the transportation cockpit.

Interactive Planning on the Map: You can carry out your planning on the map.

●

If  you  select  Unplanned  Freight  Units  and  Start  Planning  from  the  context

menu, for example, the system shows the possible assignments of the FUs to

the resources. Select the assignments that you require.

●  You  can  also  assign  unplanned  FUs or multirelations that contain unplanned

FUs  to  resources  by  using  drag  and  drop.  When  you  do  so,  you  can  either

assign  the  FUs  to  the  resource  or  the resource to the FUs. You can use the

proximity  search

in

the  context  menu

to

find  unplanned  FUs  and

transportation units that are within a specific radius of a resource or a location.

●

If  you  want  to  split  a  stage  that  is  displayed  on  the map, you can assign an

unplanned  FU  or  multirelation  to  a  location  using  drag  and  drop.  Once  you

have  selected  the  required  planning  option,  the  system  adds  the  selected

location to the FU stage and updates the map accordingly. This process also

applies to FOs.

●  You  can  also  display  transshipment  locations  that  are  not  part  of  your

currently  selected  planning  activities.  You  can  display  these  locations  by

choosing Show Assigned Transshipment Locations from the context menu.

●

In the context menu for a FU, you can add locations.

●

If a FO does not have a vehicle assigned to it, you can also assign the vehicle

by  using  drag  and  drop.  To  do  so,  you  assign  the  FO  to  a  single  vehicle

resource or a multispot that contains at least one vehicle resource or passive

vehicle resource. Then select the relevant planning option from the menu. You

can  use  the  proximity search in the context menu to find available resources

that  are  within  a  specific  radius.  You can also specify the exact position of a

resource at any time in the context menu of the map.

●

In  the  case  of  resources  on  the  map,  you  can  find  the  assigned  business

documents  by  selecting  the  corresponding  option  from  the  context  menu for

the  resource.  The system searches for already planned FOs and adds these

to the map.

119


●  You  can  use  the  context  menu  of  the  map  to  display  different  colors  for

multiple  business  documents  selected  simultaneously.  This  enables  you  to

better  differentiate  between  the  documents.  The  color  of  each  respective

document is displayed in the Color column in the document list.

●  The  system displays all of your transportation planning activities on the map.

When  you  leave  the  display  of  the  map,  your  planning  activities  are  also

displayed in the table view of the transportation cockpit.

## Gantt Chart Freight Order Creation

Using a Gantt chart, which is often used in project planning as well, helps to visualize

the availability of resources and the sequential order of transports. The Gantt chart is

fully integrated into the transportation cockpit.

In the Gantt chart, freight orders (FOs) and vehicle resources are displayed as a time

bar  and  planners  can  manually  plan  transports  by  using  drag  and  drop. The Gantt

chart is a screen area in the transportation cockpit, which can be enabled in a page

layout  for  transportation  cockpits.  All  standard  functionalities,  like  positioning  the

Gantt chart anywhere on the transportation cockpit or maximizing the screen area to

full screen, are available for the Gantt chart too.

A  zoom  bar  on  top  of  the  screen  area can zoom in and out to see a more detailed

view of a day or week, or a more general view of the year.

120


An  important  factor  for  transportation  planning  is  the  utilization  of  a  vehicle.  The

utilization  of  the  vehicle  can  be  displayed  with  the  utilization  view,  which  can  be

enabled  when  needed.  The  utilization  view  shows the utilization of the vehicle over

time in a graph. The graph is displayed in a detailed line below the actual resource or

document. In this case, the single-view is chosen. This enables the user to see all of

the execution information within one screen. Multiple loading acts are only displayed

as one item in the Gantt chart. This keeps the chart clean and easy to understand.

Interactive  planning  can  be  performed  in  the  Gantt  chart  using  drag  and  drop.

Unplanned FOs can be assigned to resources. Likewise, resources can be assigned

to FOs. The FO is dropped on the time bar of the resource. If the FO is not dropped

at  the  same  date  it  was  originally  planned,  the  date  where it was dropped is taken

over into the FO. Scheduling is only performed when requested using the Scheduling

button  on  top  of  the  Gantt  chart.  The  dual-view  can  be  selected  to  have  the

unplanned  FOs  displayed  on  top  and  the  available  resources  below.  This  enables

the user to work with one window to plan FOs. The dual-view can be either displayed

horizontally or vertically. The size of each area can be changed by dragging with the

mouse.

The  Gantt  chart  enables  the  planning  of  unplanned  FOs  by  dragging  on  vehicle

resources,  as  well  as  the  creation  of  transportation  units.  When  dragging  and

dropping the loading activity of one FO into the time bar of another FO, both FOs are

combined.

121


Overlap  means  that  the  resource  was  planned  multiple  times  and  is  therefore  not

executable. For example, if the trailer is already planned and newly planned in a later

step, this can cause an overlap, which the user gets displayed as a red line.

Similar  to  the  utilization  view,  an  overlap  view  shows  if  several  documents  on  a

resource overlap. This overlap can be overcome by scheduling the resource.

122


Lesson 2 - Practice Freight Order Scheduling

## Scheduling

Scheduling  determines  start  and  end  times  for a set of dates and times such as the

departure  and  arrival  of  a  freight  order  (FO),  the  pickup  and delivery of the assigned

freight  units  (FUs),  or  the  coupling  and  uncoupling  of  trailers.  In  scheduling,  the

system  considers  multiple  constraints  like  a  predefined  relative  ordering  among  the

activities  of  the  FO  as  well  as  the  pickup  windows  and  the  delivery  windows  of  the

assigned FUs. Scheduling can be triggered for one or more selected FOs and is based

on your settings in the planning profile.

## Freight Order Scheduling
The scheduling of FOs can be initiated in the following ways:

●  From the transportation cockpit using the Scheduling button

●  From the FO user interface using the Scheduling button

●  Automatically,  by  entering  the  departure  date  of  a  FO  and  choosing  Enter  on

your keyboard (if the user parameter /SCMTMS/SCH_FORCE is active)

Scheduling considers the following constraints:

●  Time windows for loading and unloading activities for your FUs

●  Appointments for the FO to which your FUs are assigned

●  Loading and unloading durations of your FUs

●  Location sequence of your FO

●  Existing FOs on resources

●  Coupling and uncoupling durations

●  Calendar resources as well as the calendars and capacities for the loading and

unloading activities of handling resources

●  Calendars  of

the

involved  vehicle

resources

for

loading,  unloading,

transportation, coupling, and uncoupling activities

Scheduling Unplanned Requirement Documents

123


You  can  quickly  generate  the  approximate  transportation  time  for  requirement

documents  without  needing  to  plan  the  documents.  In  addition,  the  Gantt chart can

display the stage sequence to provide a useful visual aid.

There are multiple ways to schedule an unplanned requirement document, as follows:

●  Applying a default route to the document

●  Choosing Schedule

●  Starting the freight unit building process

You  can  view  the  scheduling  results  on  the  Gantt  chart  and  in  the  requirement

document.  After  scheduling,  the  requirement  document  contains  the  transportation

times for each stage (planned arrival and planned departure times) but the document

is still unplanned.

## Forward and Backward Scheduling

The following example illustrates the use of forward scheduling.

Customer A orders 50 pallets of product X and asks for a delivery date in three weeks.

Currently,  the  capacity  of  your  depot  is  100  m³.  Product  X  takes  up  95  m³  of  your

depot. Therefore, you decide to move the goods out of your depot as soon as possible

in order to minimize your inventory. That is why you decide to use forward scheduling.

124


Customer B orders 50 pallets of product Y and asks for a delivery date in three weeks.

Currently, the capacity of your depot is 100 m³. Product Y takes up 5 m³ of your depot.

Therefore, you decide to stick to the delivery time window as closely as possible. That

is why you decide to use backward scheduling.

## Scheduling Constraints and Settings

You  can  use  the  scheduling  constraints  function  to  consider  constraints  for

scheduling  during  VSR  optimization.  This  allows  VSR  optimization  to,  for  example,

extend  the  transportation  plans  for  long  trip  durations  so  that  a  driver  can  take  his

required  breaks.  This  function only applies to vehicle resources. For example, a truck

requires two days for a trip from the east coast to the west coast of the United States.

However, since the driver must take breaks along the way, a longer trip duration must

be scheduled.

125


## Resource Availability

Resource availability is considered for the following resources:

●  Vehicle resources

●  Calendar resources

●  Handling resources

Resource Availability Considerations

Resource availability considers the following:

●  Factory calendar

●  Capacity variants

●  Downtimes

●  Existing activities assigned to the resource

## Driving and Working Time Constraints

Driving time and working hours constraints are the rules that define when drivers must

take a rest, such as a lunch break or a night's rest. You define them in Customizing as

driving  and  working  constraint  profiles.  In  the  capacity  availability  settings  and  the

scheduling  settings  of  your  planning  profile,  you  enable  planning  to  take  these

constraints  into  account.  Scheduling  and  vehicle  scheduling  and  routing  (VSR)

optimization  can  then  schedule  rests

in  road  freight  orders  based  on  these

constraints.  You  can  see  the  scheduled  rests  in  the  corresponding  lists  and

hierarchies  of  the  transportation  cockpit.  They  are  also  graphically  visualized  in  the

Gantt  chart.  You  can  define  several  sets  of  constraints,  that  is,  driving  and  working

constraint profiles, to consider different regulations, such as EU and U.S. regulations.

126


## Scheduling Strategy

Scheduling  strategies  are  assigned  in  the  scheduling  settings in the planning profile.

The  standard  strategy  is  VSS_DEF.  In  the  scheduling  settings,  you  can  specify  the

forward/backward scheduling direction and maintain coupling/uncoupling durations.

## Embedded Scheduling

Since  the  SAP  S/4HANA  2020  release,  embedded  scheduling  is  represented  by  the

scheduling  strategy  VSS_EMBED.  Embedded  scheduling  is  using  the  new  ABAP

Engine and as its name suggest, the code of this engine is written in ABAP rather than

C++, which is the code used for the VSS scheduler.

This is the default scheduling strategy. It doesn't require a remote communication and

control  framework  (RCCF)  call.  You  can  indicate  in  the  scheduling  settings  that  the

system  is  to  take  into  account  cost-based  requested  dates/times.  However,  this

strategy doesn't take into account the scheduling constraints that you have defined in

Customizing.

127


## Explain Scheduling Results

The  Explain  Scheduling  Result  app  allows  you  to  analyze  the  result  of  a  scheduling

process.

## Driver Management

A  driver  is  any  person  who  can  operate  vehicles  and  perform  transportation-related

tasks  as  a  result  of  certain  qualifications.  Drivers  are  no  longer  maintained  as

resources  but  are  defined  as  business  partners. Drivers can get assigned to existing

freight  orders  (FOs)  and  vehicle  resources.  It  is also possible to create FOs to which

the  system  assigns  drivers  automatically  when  they  are  created.  This  function  is

available only for road FOs and trucks.

One  or  more  drivers  can  be  assigned  to  an  existing  FO  or  to  the  individual

transportation  stages  of  an  existing  FO.  In  a  driver  team,  the  individual  drivers  take

turns to drive. The person who is not driving sleeps.

A  prerequisite  of  this  process  is  that  drivers  are  created  as  business  partners  with

business  partner  role  TM  Labor  Resource.  The  following  are  the  properties  of  the

driver:

●  Home location

●  Org unit

●  Validity period

128


●  Absences (for example, sickness, vacation)

●  Nonworking times (for example, Monday–Friday)

●  Offered qualifications

●  Last planned location and availability time

In FO customizing, you can define the following settings related to drivers:

●  Settings can be changed in FO

●  Number of required drivers

●  Driver assignment type

In  the  manual  planning  settings,  you  can  define  default truck handling settings. This

defines how the default truck of a driver is considered when assigning a driver to a FO.

You  can ignore the default truck or use the default truck if no other truck is assigned

to the FO.

129


## Automatic Assignment of Drivers

Automatic assignment of drivers to FOs happens if the driver assignment is requested

via  the  FO  type  and  the driver is assigned to the resource master data of the vehicle

resource  as  the  default  driver.  Other  than  that,  manual  assignment  of  drivers  is

possible in the transportation cockpit as follows:

●  Drag and Drop: It is possible to drag and drop drivers from the list of drivers in

the  transportation  cockpit to the FO being planned in the road FO hierarchy or

in the road FO list. If it has been specified in the FO type that drivers have to be

assigned per transportation stage, it is possible to drag and drop drivers in the

road FO hierarchy to the individual transportation stages.

●  Manual creation and change: It is possible to enter or change drivers manually

in the Driver column in the road FO hierarchy or in the road FO list. If specified

in  the  FO  type  that  drivers  have  to  be  assigned  per  transportation  stage,  it is

possible  to  enter  or  change  drivers  for  individual  transportation  stages  in  the

Driver column in the road FO hierarchy. If driver assignment has been activated

in  the  order  details  area  in  the  layout  for  the  transportation  cockpit,  it  is

possible  to  select  a  FO  in  the  road  FO  hierarchy  or  in  the  road  FO  list  and

manually enter or change a driver in the details for this FO.

130


●  Dialog box: Finally, it is possible to select a FO in the road FO hierarchy or in the

road FO list and choose the Assign Driver push button. A dialog box appears in

which  drivers  can  be  entered.  Then,  the  user  can  decide  in  the  dialog  box

whether to replace the currently assigned drivers with new drivers or whether to

add drivers to the existing drivers.

131


Unit 6 - Automatic Transportation Planning

Lesson 1 - Plan with the VSR Optimizer

## Vehicle Scheduling and Routing Optimizer
The  vehicle  scheduling  and  routing  (VSR)  optimizer  considers  routing,  and  the

sequence  in  which  resources arrive at certain locations (as well as the scheduling of

tasks  running  in  parallel).  It evaluates potential changes to the routing and the effect

such  changes  can  have  on  scheduling,  helping  to  avoid  the  possibility  of  delayed

deliveries and follow-on costs.

The  goal  of  the  optimizer  is  to  assign  freight  units  to  vehicles/resources  and

determine  the  route  and  sequence  of  freight  units  per  vehicle/resource such that all

constraints are met and total costs are minimized. The optimizer achieves this goal by

evolutionary  local  search,  a  population-based  metaheuristic  that  borrows  selection

principles from evolutionary algorithms and relies heavily on local optimization.

The  transformation  displayed  in  the  figure  is  obviously  a  reduction  of  the  driven

distance.

Costs and Constraints

132


The total cost, which the optimizer is designed to minimize, is a weighted sum of the

following items:

●  Non-delivery/execution penalty (per freight unit (FU))

●  Earliness and lateness penalty (per FU)

●  Fixed cost (per vehicle or tour)

●  Travel-dependent costs (per vehicle), for example, distance and duration.

●  Load-dependent costs (per vehicle and tour)

●  Sustainability costs, such as CO2 emissions

## VSR Optimization Costs
Fixed  costs  are  calculated  once  by  the  system  for  each  capacity  used  in  the  VSR

optimization  run.  Capacities  include vehicle resources and schedules. For schedules,

the fixed costs are incurred per departure.

In  addition  to  fixed  costs,  other  variable  costs  can  be  applied.  The  following are the

variable transportation costs per unit for the following dimensions:

●  Duration

●  Distance

●  Transported quantity per distance

●

## Intermediate stop

These  costs  refer  to  the  use  of  the  dimensions  of  a  capacity,  including  empty  runs,

during the VSR optimization run.

## Duration and Distance Costs

You  can  define  the  costs  per  duration  for  each  VSR  optimization  run.  You  can  also

define  a  maximum  value  and  a  unit.  The  unit  refers  to  both  the  costs  and  the

maximum  value.  If  you  do  not  specify  a  unit,  the  system  measures  duration  in

seconds.

You  can  define  the  costs  per  distance  for  each  VSR  optimization  run.  You  can  also

define  a  maximum  value  and  a  unit.  The  unit  refers  to  both  the  costs  and  the

maximum  value.  If  you  do  not  specify  a  unit,  the  system  measures  distance  in

133


kilometers.  You  can  also  specify  the  cost  basis.  This  determines  if the system uses

the costs per distance from the costs per distance field in the planning profile or from

the  transportation  lane.  Alternatively,  you  can  specify  that  the  system  is  to  take  the

sum  of  both  values  into  account.  When  optimizing  for  destination-based  distance

costs, you have to define the distance cost in the transportation lane.

## Transported Quantity per Distance and Intermediate Stop Costs

You  can  define  the  costs  per  quantity  for  each  VSR  optimization  run.  You  can  also

define a unit. You cannot define a maximum value for the costs per quantity. However,

you can specify if the system is to use the costs per quantity from the transportation

lane or from the costs per quantity specified in the planning profile.

For costs per quantity from the transportation lane, you can specify if the system is to

calculate  the  costs  in  a  distance-independent  way  or  if  it  is  to  multiply  them  by  the

distance.

For  costs  per  quantity  from  the  planning  costs,  you  can  specify  if  the  system  is  to

calculate the costs in a distance-independent way per transportation lane or if it is to

multiply them by the distance. The system determines the costs per stage if costs are

calculated  in  a  distance-independent  way.  You  are  not  allowed  to  define  a  unit.  If

134


multiplying  by  the  distance,  the  system uses the fixed value that you have defined in

the costs per quantity field.

You  can  define  the  maximum  number  of  intermediate  stops  and  the  costs  per

additional stop.

## Route-Based Versus Destination-Based Cost

The figure illustrates the route-based and destination-based costs as follows:

●  Destination-based cost:

○  Freight order (A→B→C) = Distance (A→B→C) * Cost (A→C) = 300 * 1.5

= $450.

○  Freight order (A→C→B)

= Distance (A→C→B) * Cost (A→B) = 250 * 1.9 = $475.

●  Route-based cost:

○  Freight  order  (A→B→C)  =  Distance  (A→B)  *  Cost  (A→B)  +  Distance

(B→C) * Cost (B→C) = 200 * 1.9 + 100 * 1.8 = $560.

○  Freight  order  (A→C→B)  =  Distance  (A→C)  *  Cost  (A→C)  +  Distance

(C→B) * Cost (C→B) = 150 * 1.5 + 100 * 1.8 = $405.

Route-based and destination-based distance costs can yield different results. In North

America,  destination-based  distance  cost  calculation  is  used  frequently,  whereas  in

Europe, route-based distance costs are primarily used.

135


## Optimizer Considerations
The  goal  of  the  VSR  optimizer  is  freight  unit  consolidation  and  the  creation  of  a

cost-effective and timely route from source to destination.

## VSR Goals and Objectives

●  Goal:  Determine  a  transportation  plan that minimizes total costs and satisfies

all constraints.

●  Decisions:

○  Per freight unit: Transport or not?

○  Per  transported  freight  unit:  Select  a  path  through  the  transportation

network (stages).

○  Per selected stage: Select capacity or vehicle resource.

○  Per capacity or vehicle resource:

○  Select relative ordering of activities (= routing).

○  Assign a start time to each activity (= scheduling).

●  Total costs = sum of:

○  Penalty costs (nondelivery, earliness, or lateness).

○  Capacity or vehicle costs (fixed, duration, stops, quantity, and distance).

The  total  cost is the sum of penalty costs for nondelivery, early and late delivery, and

vehicle costs for duration, distance, stops, and quantity.

Optimizer Constraints

136


The  optimizer  operates  within  the  constraints  defined  in  the  preceding  figure.  The

optimizer  evaluates  any  changes  in  routing  caused  by  constraints for their Effect on

the scheduling and timing. It communicates any change of time or date to all tasks on

that  resource  or  to  any  dependent  tasks  on  any  other  resource.  Considering  both

aspects in parallel ensures effective planning.

The  optimizer  tries  to  assign  freight  units  to  vehicles  and  determine  an  effective

delivery  order  for  each  vehicle  so  that  total  transportation  costs  are  minimized.  It

considers several constraints and takes penalty costs into account as part of the total

transportation cost.

The  following  penalty  costs  are  defined  in  the  planning  profile  and  can  be  used  to

control the decisions made by VSR optimization:

●  Premature pickup

●  Delayed pickup

●  Premature delivery

●  Delayed delivery

The  optimizer  calculates  extra  costs  if  the  transportation  plan  deviates  from  the

requested  pickup  and  delivery  dates.  This is done when using soft constraints in the

pickup and delivery time window and defining penalty costs in the planning profile.

137


There  is  a balance in the optimizer process between selecting the cheapest mode of

transport  and  adhering  to  promised  delivery  dates  and  defined  pickup  dates.  For

example, the optimizer could decide to ship via an intermodal means of transport even

if  this  means  delivering  a  day  late.  This  is  on  the  condition  that  savings  made  by

selecting a slower means of transport outweigh the penalty costs for delayed delivery.

## Penalty Costs

The  penalty  cost  for  premature  pickup  is  incurred  when  the  scheduled  pickup  time

falls  between  the  earliest  pickup  time  (hard  constraint)  and  the  allowed  premature

pickup (soft constraint).

The  penalty  cost for delayed pickup is incurred when the scheduled pickup time falls

between the allowed late pickup time (soft constraint) and the latest pickup time (hard

constraint).

The  penalty  cost  for premature delivery is incurred when the scheduled delivery time

falls  between  the  earliest  delivery  time  (hard  constraint)  and  the  allowed  premature

delivery time (soft constraint).

138


The penalty cost for delayed delivery is incurred when the scheduled delivery time falls

between  the  allowed  late  delivery  time  (soft  constraint)  and  the  latest  delivery  time

(hard constraint).

Pickup and Delivery Window Definition

## Defining Pickup and Delivery Windows

●  Forwarding  orders,  SAP ERP-orders, and deliveries work only with a single day

and time for pickup and delivery.

●  To  allow more flexibility for freight consolidation and routing optimization SAP

TM Planning uses Time Windows.

●  The  combination  of  pickup  and  delivery  definition  and  penalty  costs  controls

how the optimizer schedules within the time window.

Windows  control  when  goods  are  to  be  picked  up  and  delivered.  VSR  optimization

schedules  the  pickup  or  delivery  exactly  in  the  window  defined.  If  there  were  no

windows, VSR optimization can schedule these dates to minimize the total costs.

You  can  also  control  the optimization when windows are not taken into account and

goods are picked up or delivered too early or too late.

## Defining Tolerances

You  can  create  windows  by  defining  the  tolerances  within  which  a  premature  or

delayed  pickup  or  delivery  is  to  be  allowed.  You  specify  for  each  tolerance  if  VSR

optimization  is  to  consider  it  a  hard,  soft,  or  hard  and  soft  constraint.  Specifying

constraints controls if VSR optimization calculates penalty costs when the constraints

are not adhered to.

The following tolerances can be defined:

●  Maximum earliness

●  Maximum delay

●  Delay without penalty costs

●  Earliness without penalty costs

139


The dates and times defined for the pickup and delivery in the freight unit are the basis

for calculating the tolerances. The exact time for the pickup date or delivery date can

be considered.

## Hard and Soft Constraints

Conditions are used to set up pickup and delivery windows. The condition is specified

in the freight unit type.

Window Constraints

●  None

●  Hard (acceptable dates)

●  Soft (requested dates)

●  Hard and soft (both)

VSR  optimization  takes  constraints  into  account  when  it  assigns  freight  units  to

capacities. You can differentiate between hard and soft constraints:

●  VSR optimization always adheres to hard constraints.

●  You  model  soft  constraints  using  penalty  costs,  for  example,  lateness  costs

that are part of the total costs.

The following are the relevant condition types:

●  For pickup and delivery time window definition: /SCMTMS/TOR_TIMEWIND

●  For earliness and lateness cost definition: /SCMTMS/FU_PNLT_COST

## Means of Transport Cost Evaluation

Using  the  planning  cost  settings,  the  optimizer  can  determine  the  best  means  of

transport to use. For example, a break-even analysis between a large truck and a small

truck can be modeled with this setting.

There  is  a  relation  between  pickup  and  delivery  penalty  time  and  cost  per  duration.

Depending on business rules, it could be better to delay pickup or deliver early.

The  maximum  distance  and  durations  are  useful  for  deciding  on rail or air transport

instead of road. The maximum number of stops and costs are useful for reducing the

number of visits during a week at customers or suppliers.

140


## Stop Off Costs

The figure shows two stop-offs between locations A and D. Stopover costs are applied

to  influence  the  outcome  of  VSR  optimization.  The  source  and  target  location  in  a

route  are not taken into account when calculating the number of stopovers. Maintain

the number of stopovers plus one.

## Explanation Tool
You  set  user  parameter /SCMTMS/EXP to X to allow for the logging of the optimizer

data for optimization runs that you start interactively.

The explanation tool for VSR optimization displays the following information:

●

Input for the VSR optimization run

●  Results of the VSR optimization run

●  Solution overview

Content of the Optimizer Planning Log / Explanation Protocol Input

●  Freight units

●  Transportation documents

●  Freight bookings

●  Resources

141


●  Transportation network

●

Incompatibilities

●  Conditions

●  Dimensions

●  Parameters

## Results

●  Freight units

●  Transportation documents

●  Freight bookings

●  Solution details

●  Resources

142


Lesson 2 - Plan via Hubs

## Pooled Distribution

In the pooled distribution process, the SAP TM system determines whether it is more

cost-effective  to  deliver  freight  directly  to  the  customer via truckload or using a pool

location to consolidate freight.

In the pool distribution process, a shipper wants to send goods from a shipping point

to customers using pool or hub locations for consolidation.

The  following  figure  lists  master  data  objects  that  are  required.  All  the  master  data

concepts  are  covered  in  Unit  2.  We  revise  transshipment  locations  here  as  they  are

important for this concept.

143


Definition  of  a  Transshipment  Location:  A  transshipment  location  is  defined  by

assigning  a  location  to either another location or to a transportation zone. When you

assign  a  transshipment  location  to  a  transportation  zone,  it  can  be  used  as  a

transshipment location by all locations that are part of that transportation zone.

A  transshipment location is used for unloading goods from one vehicle resource and

loading

it  onto  another  vehicle  resource  during  the  transportation  process.

Transshipment  locations  are  used  when  different  means  of  transport  or  different

carriers  have  to  be  used

in  the  transportation  process.  You  can  also  use

144


transshipment

locations  when  consolidating  or  deconsolidating  goods  to  be

transported.

If  you  define  a  transshipment  location  and  want  to  use  it  in  your  transportation

processes, you must define transportation lanes that take the transshipment location

into consideration.

## Multi-Stage Transportation

The  VSR  optimizer  evaluates  the  various  possibilities  for  transporting  the  selected

freight units. It then opts for pooled distribution whenever it is cost-effective to do so.

In a standard pooled distribution process, the VSR optimizer creates one freight order

to  transport  the cargo to the transshipment location. It then creates a second freight

order to transport the cargo out of the transshipment location.

Other scenarios are also possible. Multiple freight orders allow splitting up of resource

assignment,  carrier  assignment,  and  other  downstream  planning  and  execution

activities.

## Transportation Proposals

A  transportation  proposal  defines  how  a  freight  unit  can  be  transported  through  a

transportation  network  (which  is  defined  by  locations,  transshipment  locations,

transportation  zones,  transportation

lanes,  vehicle  resources,  schedules,  and

bookings).  For  a given transportation demand (freight unit), the system determines a

set  of  alternative  transportation  proposals.  The  transportation  proposal functionality

serves the following purposes:

●  To help the user identify the different transportation options for a freight unit. In

a complex network, in which end-to-end transportation requires several stages,

transportation  proposals  are  an  easy  way  to  make  the  different  options

transparent. Transportation proposals can differ in relation to routing, means of

transport,  and  time  required.  Each  of  these  variables  can  increase  or  reduce

costs,  and  the  proposals  thus  provide  the  planner  responsible  with  the

necessary information to make an appropriate choice.

145


●  To  create  the  stages  upfront,  for  example,  to  choose  the  option  of  ocean

transport, because the customer has placed their order well in advance and this

is the cheapest choice. In this use case, no freight orders are created based on

the  proposal  result,  but  only  the  stage  information  is  stored.  This  allows  the

task of planning the different stages to be assigned to different planners and to

be completed at different times.

Entry Points for Transportation Proposal Determination
The entry points for transportation proposal determination are as follows:

●  Forwarding Order→Stages→Actual Route→Define Route

●  Transportation Cockpit→Select Freight Unit(s)→Transportation Proposal

## Layout of the Transportation Proposal Result

The  layout  of  the  transportation  proposal  result  screen  can  be  flexibly  configured,

similar  to  the  transportation  cockpit  layout.  The  results  can  be  displayed  in  a  table

format or visualized on a map. If the transportation proposal has been carried out for

several freight units (because these compete for the same capacity, for example), the

solution  is  always  for  a  valid  combination  of assignments. In the table-based layout,

each stage is shown in a separate line. In complex networks, there could be millions of

routing  options  for  a  given  transport,  with  only  minor  differences  between  them.

Depending  on  the  objective  of  the  planner,  results  can  be  presented  according  to

defined criteria.

Transportation Proposal: User-Defined Preferences

146


●  Route variation

●  Carrier variation

●  Departure date variation

●  Time relevance

●  Cost variance

Preferences  can  be  weighed  against  each  other  based  on  relevance:  none,  low,

medium, or high.

When  you  use  the  optimizer  to  generate  a  transportation  proposal,  you  can  specify

whether  the  system  is  to  accept  only  the  proposed  route  or the proposed route and

associated freight documents. In this field, you have the following options:

●  Save  Route  Only:  Only  the  freight  unit  stages  are  saved  when  the  system

accepts the route that you have chosen.

●  Save Route and Freight Documents: Freight unit stages and freight documents

are saved by the system.

●  Not Defined: You can specify on a case-by-case basis whether the system is to

save only freight unit stages or also the associated freight documents.

## Features of the Transportation Proposal

The features of the transportation proposal are as follows:

●

Implicit  definition  of  transshipment

locations  by  schedules  and  freight

bookings (simplified definition of transportation network)

●  Mode of transport constraints on freight unit and freight unit stage level

●  Fast  determination  of  transportation  proposals,  yielding  more  alternatives

according  to  predefined  variation  criteria  (for  example,  route,  carrier,  and

departure  date),  and  trade-off  between  time  and  cost  (controlled  variation

according to predefined criteria)

●  Consideration  of  preferences  for  locations,  carrier,  mode  of  transport,  dates,

and times

●  Display of multiple solutions on the result map

●  Rough  planning  (detailed  planning  on the main leg and rough planning for pre

leg and subsequent leg, based on rough definition of transportation durations)

147


148


Unit  7  -  Subcontracting,  Load  Planning,  and

## Short-Cut-Process

## Lesson 1 - Carrier Selection

Once  a  freight  order  has  been  built,  a shipper must choose (and communicate with)

the  business  partner  responsible  for  moving  the  product.  We  refer  to  this  as  carrier

selection.

The  carrier  is  the  business  partner  that  you  subcontract  the  freight  order  to.  The

carrier  can  be  different  from  the executing carrier, which is another business partner

role  that  you  can  assign  to  your  freight  order,  if  the  carrier  itself  subcontracts  the

execution  of  the  freight  order  to  a  third  party.  That  way,  you  have  the  option  to

differentiate  between  the  party  you  contracted  with  and  the  party actually executing

the freight move.

149


## Carrier Selection

Carrier selection is used to assign a suitable carrier to your subcontractable business

documents  (for  example,  freight  orders),  either  manually  or  automatically.  Carrier

selection  can  be  done  for  freight  bookings  and  also  via  report  /SCMTMS/PLN_OPT.

The  aim  is  to  find  a  carrier  with  the  lowest costs under consideration of the defined

constraints.

In manual carrier selection, you manually assign the required carrier to your business

documents.  If  you  have  configured  a  check  against  transportation  allocations,  the

system

takes

this

into  account  and  checks

the

transportation  capacities

(transportation  allocations)  that you have defined for the individual carriers. If, during

the allocation, the system finds relevant transportation allocations without capacity or

that certain rules are violated by the allocation, warning messages appear. When you

want to take business shares into account for carrier selection that you have to define

this in the transportation lane and carrier selection settings.

A  separate  optimization  is  available  for  automatic  carrier  selection. It takes selected

optimization options into account when determining the most cost-effective carrier for

all  business  documents  that  you  have  selected.  If  none  of  the  carriers are available,

the system does not assign any carrier to the relevant business documents.

150


## Status Management in Subcontracting

The figure shows which statuses change during the subcontracting process.

## Strategy Options

During  planning  in SAP TM, strategies are defined which are optimization options for

carrier selection. The system takes these strategies into account during the automatic

carrier selection process.

You  define  strategies  either  in  the  transportation lane or in carrier selection settings.

Initially,  the  system  considers  the  appropriate  transportation  lane  for  each  freight

order.  This  allows  it  to  consider  different  settings  in  one  run.  Taking  strategies  and

settings into consideration, the optimizer then creates a carrier ranking list containing

the different carrier options.  The strategy options supported are as follows:

●  Cost and Priority

●  Business Share

●  Transportation Allocation

●  Continuous Move

## Costs and Priorities in Carrier Selection

In carrying out carrier selection, the system can put more weight on priorities or costs.

Penalty costs can influence business shares and continuous moves.

151


In terms of priority, the system can determine the most favorable carrier based on the

priorities  you  have  defined.  In  effect, this means that the system chooses the carrier

with the highest priority, while taking into account the various restrictions that can be

in place.

Alternatively,  the  system  can  determine  the  carrier  based  on  the  lowest  total  cost.

Costs  in  this  case  can  refer  to  internal  costs  or  to  charges  calculated  in  charge

management.  Carrier  reliability  can  be  taken  into  account,  for  example,  by using the

BCV  to  review  the  reliability  manually  in  a  manual  process  or  by  using  the

"cost+priority" selection and model as a bonus in an automatic process.

## Note
When  we  speak  of  internal  costs  here,  we  are  not  speaking  of  real-world  costs.

Internal costs are used for weighting only, as part of the carrier selection process.

## Transportation Allocations

Transportation allocations allow companies to assign defined quantities of capacity to

certain  business  partners.  This

includes  set  minimum  or  maximum  capacity

restrictions  that  regulate  how  much  business  is  allowed  with  a  certain  carrier  in  a

certain region for a certain means of transport. A separate business object is used to

model these allocations.

Often,  firm  relationships  exist  with  carriers in the form of contracts. These contracts

can  guarantee  that  an  amount  of  business is allocated to a carrier, which if not met,

results in penalties. SAP TM has the tools to track these relationships or, alternatively,

divide up business between different carriers.

An allocation represents the planned capacities for a carrier and a trade lane during a

validity period. The capacities can be defined for multiple dimensions, such as volume,

weight,  and  20-foot  equivalent  units,  as  well  as  a  sequence  of  time  periods  of  the

same granularity, which are frequently called (time) buckets. For each dimension and

time  period,  the  allocation  captures  the  already-consumed portion of the maintained

capacity.  All  freight  documents  matching  the  carrier,  trade  lane,  and  validity  period

consume  the  corresponding  buckets  of  the  allocation.  When  a  freight  document  is

created,  the  matching  allocations  are  determined  asynchronously  and  updated

152


according  to  the  freight  document’s  capacity. The consumed quantities are visible in

the allocations and allow tracking of the capacities and their utilizations.

The following are examples of transport allocations:

●  A  carrier  commits  to  at  least 25 shipments or truckloads from Nashville each

day. However, for business reasons, the availability changes each day.

●  A carrier normally provides two trucks per day from Dayton, Ohio. For business

reasons,  the  carrier  is  able  to  offer,  on  Tuesday  and Friday only, five trucks to

the shipper.

●  A  carrier  can  include  extra  capacity  to  the  existing  number  of  shipments  by

truck.  For  example,  a  carrier  could  add  five  more  trucks  during  the  week

between Tuesday and Thursday.

Carrier  capacity  can  be  defined  for  any  geographical  level  in  an  arbitrary

dimension.  When  defining  the  allocation,  the  trade  lane  can  be  specified  as

follows:

○  Along:  Both  source  location/zone and destination location/zone can be

specified

○  From: Source location/zone only

○  Within: Using zone hierarchy

○  To: Destination location/zone only

○

Inbound: Destination zone is specified

○  Outbound: Source zone is specified

●  Extended carrier selection optimizer interface

○  During  carrier  selection  either  using  optimizer  or  manual  planning,  the

allocation can be checked

○  During tendering, the allocation can be checked

153


Creation of Transportation Allocations:

When you create a transportation allocation, you define the following:

Creation  options: You can specify, for example, whether a transportation allocation is

to refer to a transportation lane and whether time buckets can be overwritten.

Scope  of  transportation  allocation:  Here  you  enter,  for  example,  the  planning  period

(yearly, weekly, and so on). You are free to choose the start of the planning period. For

example, you can define a bucket from Monday 14:00 until Tuesday 14:00.

Buckets:  Here  you  can  define,  for  example,  a  subbucket  distribution.  If  a  carrier  can

only deliver, for example, in the morning, you can define two subbuckets (Morning and

Afternoon)  for  the  bucket  Daily.  As  the  percentage  of  the  assigned  business

documents  (for  example,  freight  orders),  you  define  100%  for  Morning  and  0%  for

Afternoon. In addition, you can specify the minimum and maximum product allocation

quantity.

SAP  Transportation  Management  distinguishes  between  the  following  three

transportation allocation types:

●  Air freight agreement allocation

Stores  information  about  transportation  allocations  of  carriers  that  act  as

constraints  for  air  freight  agreements.  You  can  create  air  freight  agreement

allocations directly from an air freight agreement.

154


●  Carrier selection allocation

Stores  information  about  transportation  allocations  of  carriers  in  a  specific

trade  lane.  The  system  uses  carrier  selection allocations when optimizing the

carrier selection.

●  Flight schedule-based allocation

Stores  information  about  transportation  allocations  of  carriers  at  schedule

departure

level

in  a  master  flight  schedule.  You  can  create  flight

schedule-based allocations directly from a master flight schedule.

In

Customizing,

you

can

follow

the  menu

path

## Transportation

Management→Planning→General  Settings→Define  Transportation  Allocation  Types

and define allocation types by specifying the following parameters:

●  Default  Type:  If  you  created an allocation from scratch and did not choose an

allocation type, the default allocation type is chosen; it’s set by this parameter.

●  Mode of Transport: You can define the mode of transport or omit this field.

●  Planning Period: You can choose among daily, weekly, monthly, quarterly, yearly,

and  schedule  departure.  Whereas  the  first  considers  all  freight  documents  in

the  specified  time  period,  the last option refers to departures of an underlying

schedule. This means that all freight documents created for that departure are

covered by the bucket.

155


●  Schedule-Based  Allocation:  This  specifies  that  the  allocation  depends  on  a

schedule–that is, you can create the allocation only out of a schedule.

●  Full  Calendar  Units: You can define whether the bucket fully covers a calendar

unit  or  if  it  can  start  at  any  time but has a duration according to the planning

period. If you use a daily planning period and do not use full calendar units, you

can  have  a  planning  period  from  Monday  at  8:00 until Tuesday at 8:00. If you

use a monthly planning period and full calendar units, the bucket starts at 0:00

on  the  first  day  of  the  month  and  lasts  until  0:00  on  the  first  day  of  the  next

month.

●  Use  Attributes:  This allows you to create multiple buckets for the same period

of  time.  The  buckets  consider  different  attribute  combinations  based  on

shipping  type,  contract  basis,  or  handling  code.  Using  handling  codes  for  the

upper  deck  and  lower  deck  of  an  airplane,  you  can  define  two  buckets  with

individual capacities, one for the upper deck and one for the lower deck.

●  Use  Carrier  Selection:  This  defines  whether  allocations  of  this  type  are

considered by carrier selection.

●  Carrier  Selection  Unit  of  Measure:  If  carrier  selection  is  activated,  you  can

specify the allocation’s unit of measure that is considered for carrier selection.

You can define allocations with volume, weight, and TEU quantities and choose

carrier selection considering the TEU capacities.

●  Update Quantity Automatically: This defines whether a newly created allocation

or bucket gets an automatic update of its consumed quantities.

●  Bucket  Overlapping:  A  freight  document  can  cover  multiple  buckets  of  the

allocation.  Using  this  parameter,  you  can  define  whether  all  covered  buckets

get  consumed  by  the  freight  document  or  only  the  first  covered  bucket  gets

consumed.  This  parameter  cannot  be  changed  if  allocations  already  exist  in

your  productive  system  because  the  buckets  contain  data  according  to  both

consumption modes, which makes the quantities hard to interpret.

●  BW  Relevance:  This  specifies  whether  the  allocation  type  is  relevant  for

analytics based on SAP Business Warehouse (SAP BW).

Business Shares

156


Selecting Carriers Based on Business Shares

The objectives of business shares are as follows:

●  Assign defined percentages to certain business partners

●  Support negotiation of freight agreements

●  Avoid dependency on a single vendor

●  Consider the capacity of a carrier for a certain relation/route/geography

Like  transportation  allocations,  business  shares  use  trade  lanes.  With  SAP  TM,  you

can  define  such  target  shares  per  carrier  as  a  business  share  for  a  trade  lane  and

means  of  transport  or  mode  of  transport  on  a  daily,  weekly,  monthly,  quarterly,  or

yearly basis.

Business Share (Example)

157


When defining the business share context, you create the business share buckets. The

percentage  of  business  share  a  carrier  can  have  for  these  individual  buckets,  is  the

actual business share a carrier is allowed to have. There are different types of bucket

available  during  business  share  creation.  They  are  yearly,  quarterly,  monthly,  weekly,

and daily.

## Example One

Carrier A can have a weekly bucket of 75% of the business share on the lane between

Hamburg and Frankfurt between the validity periods 01 March 2015 to 31 May 2015.

In the same context, Carrier B can have a weekly bucket of 25% defined.

158


Tolerances and penalty costs can be defined for business shares. As long as business

shares  are  within  the tolerance limits, the cost calculations during carrier ranking are

not  affected.  Tolerances  are  always  defined  in  percentages  (%). If the total business

share  of  the  carrier  exceeds  the  defined tolerances, either shortfall or over, a penalty

applies.

The shortage penalty costs are added to all carriers, other than the one selected. The

excess  penalty  costs  are  added  to  the  carrier  under  consideration.  Penalties  are

maintained as numeric values in the business share. This number is multiplied by the

deviation percentage to arrive at the penalty cost.

It  only  makes  sense  to  use  business  shares  if  you  have  defined  penalty  costs.  It  is

recommended to also always define tolerances to give the optimizer a certain amount

of leeway.

## Example Two

There is a penalty of 1000 defined in the business share. An excess tolerance of 10%

is  also  defined.  During  business  share  calculation,  if  the  excess  is  12%,  the  excess

159


liable for penalty is 2%. This 2 is multiplied by 1000 to arrive at the total excess penalty

costs of 2000.

## Note
When calculating the total costs for a carrier, if you are working with TCM costs, there

will  be  a  currency  assigned  to  the  costs.  To  assign  a  currency  to  business  share

penalty  costs,  go  to  Carrier  Selection  Settings→Advanced  Settings→Common

Currency.

For  example, if you are working with carriers from multiple geographic locations with

multiple  currencies  to  arrive  at  the  correct  ranking,  the  system  uses  the  common

currency  (maintained  in  the  Carrier  Selection  Settings)  for  all  its  calculations.  The

currency displayed in the carrier ranking list is always the local currency of the carrier

(maintained in the freight agreement).

All  FORs  in  the  business  share  context  are  selected  for  the  business  share  penalty

calculations, though these FORs are not selected during the planning run.

For  example,  assume  in  a  business  share  context  there  are  two  carriers,  A  and  B.

There  are  no  tolerances  defined.  Carrier  A  is  awarded  a  60%  business  share  and

Carrier B a 40% business share. There are already 10 freight orders awarded, of which

Carrier A is assigned six and Carrier B is assigned four.

Now, let us perform carrier selection for the eleventh FOR. If Carrier B is assigned this

FOR, Carrier A has a shortfall of business share, and the penalty cost for the shortfall

is charged to Carrier B, on top of the usual costs determined during carrier selection.

 If Carrier A is assigned the eleventh FOR, Carrier B has a shortfall of business share,

and the penalty cost will be charged to carrier A, on top of the usual costs determined

during  carrier  selection.  Both  options  are evaluated by the system and the ranking is

done accordingly.

## Carrier Selection Settings

The  objective  of  carrier  selection  is  to  provide  a  ranking  list  of  carriers  that  are

available  to  execute  a  planned  freight  order.  You  can  perform  carrier  selection

manually, by using an optimization algorithm, or by using an auctioning mechanism as

part of the tendering process.

160


The  primary  objective  of  carrier  selection  is  to  assign  a  reliable  and  cost-efficient

carrier  to  a  freight  order.  This  can  be  done  in  the  background,  interactively  using

manual steps, or by using an automated optimization procedure.

Carrier  selection  can  be  started  directly  from  the  freight  order  user  interface  (UI)  or

from any work list that displays freight orders. It can also be started for freight orders

inside the transportation cockpit.

Carrier  selection  can  be  executed  as  part  of  a  planning  strategy  (for  example,  by

including method VSR_TSPS as in planning strategy VSR_1STEP, which is delivered as

a  standard  planning  strategy  that  combines  vehicle  scheduling  and  routing  (VSR)

optimization and carrier selection.

In the background, the carrier selection process can be initiated in the following ways:

●  As  part  of  the  transportation  planning  process  with  background  report

/SCMTMS/PLN_OPT  and  using  a  planning  strategy  that  includes  carrier

selection (for example, VSR_1STEP)

●  By scheduling report /SCMTMS/TSPS_OPT_BGD

●  By  assigning  strategy  Carr_Sel  as  a  creation  strategy  in  the freight order type

## Customizing

The  carrier  selection  process  is  predominantly  used in land transportation. However,

the  carrier  selection  process  can  also  be  triggered  for  freight  bookings  using  the

background  report  or  from  the  freight  booking  UI.  In  contrast  to carrier selection for

freight  orders,  carrier  selection  for  freight  bookings  will  only  consider  transportation

allocations–no business shares or continuous moves.

The input data for carrier selection is one or more freight orders (selected interactively

in a work-list) or a selection profile by which the freight orders that must have a carrier

assigned are determined. In addition, carrier selection settings are required to specify

exactly  how  carrier  selection  can  be  carried  out.  These  settings  control  the  carrier

selection  process  and  determine  which  constraints  are  used  and  how.  Therefore,

configuring carrier selection settings for automatic carrier selection is mandatory.

161


The following fields are the most important to influence the carrier selection process:

●  Check Incompatibilities: Incompatibilities are checked only if this checkbox has

been selected.

●

Incompatibility  Settings:  If  the  Check  Incompatibilities  checkbox  is  selected,

incompatibility  settings  define  which

incompatibility  definitions  must  be

adhered to.

●  Type  of  Carrier  Selection  Settings:  This  parameter  defines  the  purpose  of

carrier  selection.  Available  options  are  General  Carrier  Selection,  Carrier

Selection for Tendering, and Carrier Selection for Direct Shipment.

●  Allocation  Usage:  This  parameter  determines

the  consideration  of

transportation  allocations.  Available  options  are  to  use  transportation

allocations, not to use them, or to decide on the transportation lane level.

●  BS Usage: This business share usage parameter determines the consideration

of  business  shares.  Available  options  are  to  use  business  shares,  not  to  use

them, or to decide on the transportation lane level.

●  Strategy:  The  strategy  determines  how  the  objective  of  carrier  selection  is

calculated in optimization. The objective can be based on cost, priority, the sum

of  cost  plus  priority,  or  the  product  of  cost  times  priority.  In  addition, the Use

Transportation Lane Settings option can delegate this decision by geography to

the  individual  transportation  lanes,  so  that  in  different  geographical  areas,

162


different  objectives can be pursued (for example, priority in one transportation

lane and costs in another transportation lane).

●  Carrier  Cost  Origin:  Carrier  cost  origin  defines  how  costs  are  calculated.

Transportation  charges  from  Transportation  Charge  Management  or  internal

costs  can  be  used.  The No Cost Determination strategy can be used if carrier

selection  for  tendering  searches  for  the  available  carriers  in  a  broadcast

tendering  process.  Like  the  settings  for  strategy  with  the  Use  Transportation

Lane  Settings,  you  can  delegate  this  decision  by  geography  to  the  individual

transportation lanes.

●  Planning  Strategy:  The  default  planning  strategy  for  carrier  selection  is

TSPS_DEF.

●  Optimizer  Runtime:  This  parameter  specifies  the  maximum  runtime  for  the

optimizer (in seconds).

●  Consider  Manual  Assignments  as  Fixed:  Dealing  with  manual  assignments in

automatic  carrier  selection  is  an  important  topic  because  there  is  likely  a

reason  for  manual  assignments,  and  they  cannot  simply  be  overridden.

Therefore, manual assignments can be considered as fixed when this checkbox

is selected.

●  Action  for  Manual  Rankings:  A  similar  question  is  how  to  deal  with  manual

rankings. Available options for manual rankings are to keep them, remove them,

or keep the carrier only when it is considered available.

●  Transportation  Charge  Interpretation:  If  for  any  reason,  the  transportation

charges  for  a  carrier  for  a  freight  order  are  evaluated  as  zero,  this parameter

determines how to deal with it. Available options are to either ignore the carrier

availability  for  this  freight  order  or  accept  the  carrier  for  this  freight  order  as

either the cheapest available carrier or the most expensive one.

●  Action  after  Carrier  Selection  Run:  Available  actions  after  the carrier selection

run  are  the  automatic  assignment  of  the  highest  ranking carrier to the freight

order or doing nothing (that is, leaving this decision to a manual process/user,

based on the created carrier ranking).

●  Consider  Hierarchy:  This  parameter  chooses  the  available  carriers.  Options

include  considering  only  those  carriers  defined  on  the  most  specific

163


transportation  lane  or  considering  all  transportation lanes to retrieve available

carriers.

●  Continuous  Move  Type:  With  this  parameter,  you  decide  whether  only  simple

continuous moves are allowed, only round-trips are allowed, continuous moves

are  not  considered  at  all,  or  this  decision  is  made  on  the  transportation  lane

level.

164


## Lesson 2 - Load Planning

During truck planning, rules are applied to fulfill legal restrictions. For example, certain

axle loads cannot be exceeded. In addition, a certain loading sequence of the goods to

be transported optimizes the transportation plan. Load planning concerns the loading

of goods to be transported in an optimized manner into a transportation unit, be it be

a truck, trailer, or container resource.

You  can  plan  the  loading  space of box trucks, trailers, semitrailers, and containers in

the transportation cockpit or directly in one of the following business documents:

●  Road freight order

●  Trailer unit

●  Container unit

Planning is carried out at the level of business document items. Load planning returns

an approximate calculation of how the available loading space can be optimally used,

taking  into  account  the  maximum  axle  loads  and  the  maximum  weight  of  a  vehicle

resource. The calculation is based on the master data that you enter for the resource.

In  automatic  load  planning,  also  known  as  load  optimization,  the  load  optimizer

creates  a  load  plan  for  your  business document. It considers capacity restrictions in

terms  of  the  height,  width,  weight,  and  length  of  the  loading  space.  For  vehicle

resources with two axle groups, it also considers the maximum axle load.

Vehicle Capacity Attributes

●  VSR:

One-dimensional, for example, volume or mass: Up to eight dimensions.

●  VSO:

Three-dimensional, for example, pallet or box size: Visual representation.

●  Vehicle capacity is maintained in vehicle resource master data.

In  vehicle  scheduling  and  routing  (VSR)  planning,  SAP  TM  considers  the  resource

capacities  of  weight  and  volume.  However,  the  new  load  planning  function  requires

more information on the master data level. Not only are weight and volume limitations

considered more precisely, but the weight distribution of axles is also planned. This is

required to fulfill legal restrictions when creating a load plan.

165


Within  the  resource  master  data,  on  the  Physical  Properties  tab,  there  are  more

capacity  and  resource  configuration  fields  to  maintain.  You  can  specify  attributes

regarding  dimension,  weight,  and  type  of  resource.  One  specific  attribute  is  the

definition of axle groups.

The table, Box Truck, provides a detailed explanation of the elements of the preceding

figure.

## Box Truck

Measurement in Figure  Name  in the Master

Description

Data

a1

## Axle Group Distance

Distance  between  axle  group  1 and

1

the front of the box truck

166


c

a2

d

s2

h

l

Cargo

body

Distance  between  the  start  of  the

distance

loading  space  and  the  front  of  the

box truck

## Axle Group Distance

Distance  between  axle  group  2 and

2

the front of the box truck

Connector Distance  Distance

between

the

trailer

coupling  of  the  box  truck  and  the

front of the vehicle

Distance  Between

Distance within axle group 2

## Axles

## Interior Height

Height of the loading space

## Interior Length

Length of the loading space

167


## Vehicle Types Example 2: Semi-Trailer

The  table,  Semi-Trailer,  provides  a  detailed  explanation  of  the  elements  of  the

preceding figure.

## Semi-Trailer

Measurement in Figure  Name  in  the  Master

Description

Data

a1

s1

k

Axle  Group  Distance

Distance  between  axle  group  1

1

and the front of the trailer

Distance

## Between

Distance within axle group 1

## Axles

## King Pin Distance

Distance between the king pin and

the front of the trailer

168


h

l

p

## Interior Height

Height of the loading space

## Interior Length

Length of the loading space

## Split Deck Position

Position  in the trailer at which you

have added the split deck

## Freight Unit Dimensions

Dimensions  of  individual  packages  are  determined  from  the  business  document

items; that is, freight unit items are the basis for load planning and load optimization in

the transportation cockpit. The following are relevant dimensions:

●  Length

●  Height

●  Width

●  Gross Weight

## Load Plan Settings

Load  planning  settings  define  a  process  controller  strategy.  This  strategy  defines  a

sequence  of  methods  to  be  executed  for  the  load  planning  and  enables  a  flexible

combination of standard and custom logic. With the strategy, it is possible to define a

set  of  rules  to  be applied when optimizing the load. The rules can be given a priority,

deactivated  to  test  the  planning  with  a  different  rule  set,  and  adjusted  with  certain

attributes.

169


Load Planning Settings Definition

●  Load planning strategy

●  Load optimization runtime

●  Load planning rules (including their priorities and parameters)

Load  planning  settings  are  assigned  in  the  planning  profile.  By  assigning  a planning

profile  in  the  freight  order  type,  different  load  planning  settings  can  be  used  for

different freight order types.

## Load Planning Rules

In  automatic  load  planning,  you  can  define  the rules to be considered by the system

during a load optimization run. You can choose between the following types of rules:

●  Rules that apply to automatic planning for all resource types

●  Rules that apply only to the automatic load planning of box trucks

●  Rules that apply only to the automatic planning of trailers and semitrailers

●  Rules  that  apply  only  to  the  automatic  load  planning  of  the  upper  decks  of

double-deck trailers

You can define different rules for the lower and upper deck of double-deck trailers.

The  combination  of stack, row, and line indicates the exact position of each package

loaded  onto  the  resource.  Packages  loaded  on  top  of  each  other  form  a  stack.

Packages  loaded  next  to  each  other  from  left  to  right  form  a  row. The first row of a

170


deck  is  always  placed  towards  the  start  of  the  loading  space.  Packages loaded one

behind the other from front to back form a line. The first line of a deck is always on the

left side of the deck in the direction of travel.

## Rules for Load Planning

●  Stack height ascending in driving direction

●  Stack height descending in driving direction

●  Maximum height difference of adjacent stacks

●  Maximum height difference of stacks within a row

●  Maximum height difference of stacks within a line

●  Penalty for packages that cannot be loaded based on weight

●  Penalty  for  packages  that  cannot  be  loaded  based  on  weight  multiplied  by

volume

●  Packages with high density must be at the bottom of the stack

●  Packages  can  be  positioned  anywhere  in  the  stack  regardless  of  weight  and

density

## Load Planning

The  load  plan  is  the  result  of  load  planning. It provides you with an overview of how

the loading space available for transporting a business document is used currently.

In both the transportation cockpit and in the business document, you can display the

complete load plan as a 3D load plan or a table load plan of business document items.

171


In  the  3D  load  plan,  you  can  show  or  hide  individual  objects  as  well  as  entire  rows,

columns, or stacks and fill them with different colors. Furthermore, you can show and

hide gridlines in your decks in the 3D load plan.

If items cannot be loaded, the load plan includes information on the loading sequence

and the exact position on the vehicle. In addition to the load plan, a load distribution is

available for each axle and the complete vehicle. This document proves that the load

plan  fulfills  the  legal  requirements.  An additional tab holds statistical indicators such

as the used volume and area.

## The Load Plan

The load plan contains the following information about the business document item:

●  Resource

●

Item in the resource

●  Loading sequence

●  Row, stack, and level in the loading space

●  Gross weight

●  Height, width, and length

●  Stackability

## Load Plan Analysis

The  following  is  the  load  distribution  and  statistical  data  based  on  the  current  load

plan:

●  Number of loaded business document items

●  Used area on the lower deck of your double-deck trailer

●  Utilization of the loading volume in percent

●  Used area on the upper deck of your double-deck trailer

●  Maximum weight for each axle group compared to the current weight for each

axle group

●  Maximum trailing load compared to the current trailing load

172


## Lesson 3 - Short-Cut Process

Creating a freight order directly from the FUBR is called the short-cut planning process

because,  in this case, freight units as separate business documents are omitted, and

more planning steps are not required because the freight order is created right away.

The purpose of the short-cut process is to skip any planning activities, because these

cannot  be  required  in  certain  scenarios.  For  example,  if  the  sales  orders  that  are

received by a company already state the required truck size, the freight order could be

created  directly  from  the  transportation  demand  (in  this  example,  a  sale  order).

Technically,  this  is  done  during  freight  unit  building  by  selecting  a  freight  order  type

instead of a freight unit type. Thus, freight units are omitted in the scenarios where the

transportation demand/requirement exactly matches the to-be-created transportation

document.

173


## Unit 8 - Transportation Execution

Lesson 1 - Transportation Units and Service Orders

## Transportation Units

Transportation Units (TUs) can represent both demand and capacity. They share

some similarities with freight units (FUs) and others with freight orders (FOs), but they

also differ from both FUs and FOs.

Scenarios involving trailers, railcars, containers, and packages can be modeled by TUs,

abstracting from the specific documents called trailer units, railcar units, container

units, and package units. For these scenarios you have to configure freight order types

and transportation unit types.

Like freight documents, TUs have stages defining their paths through the network.

While trailer, railcar, and container resources can be assigned to the corresponding

TUs, package units represent one or multiple packages, each having an assigned

packaging material. On the one hand, TUs cannot move themselves; instead, they

require being moved by a truck, locomotive, vessel, or airplane and thus must be

174


assigned to a freight document. Therefore, they represent a demand for

transportation, like FUs.

The assignment of a TU to a freight document can be done directly–for example,

trailer unit to road freight order–or indirectly, such as container unit to trailer unit,

which is then assigned to a road freight order.

While a freight document cannot be assigned to another freight document, TUs allow

nested assignments within this document category. For example, consider the

following assignment chain: freight unit → package unit → container unit → trailer unit

→ road freight order. In this case, the TUs represent three consolidation levels

between freight unit and road freight order. It is not possible to consolidate a trailer

unit into another trailer unit, and this holds true analogously for railcar units, container

units, and package units.

On the other hand, TUs can consolidate other demands. Therefore, they also represent

a capacity for transportation, like freight documents. While a FU represents a single

transportation demand, the TU can represent a set of transportation demands that

can even have different source and destination locations. For example, a trailer is

moved from location A to B to C, delivering three FUs: the first from A to B, the second

from A to C, and the third from B to C. In general, TUs provide a lot of modeling

capabilities but that requires more planning decisions and adds planning complexity.

Therefore, we recommend avoiding using TUs if your business can be modeled

without them. For many transportation scenarios, using TUs is mandatory because it

is the only feasible way to model your business.

## Ways to Create TUs

There are many ways to create TUs:

●  Manual planning can be done in the transportation cockpit, as described in

Section.

●  The VSR optimizer can create trailer units and railcar units based on freight

units, container units, and package units.

●  Load consolidation can create trailer units and container units based on freight

units and package units.

175


●  Package units of linear distribution type can be extracted out of road freight

orders.

●  FUB can create trailer units, railcar units, container units, and package units, but

these TUs represent pure demand documents and do not allow consolidation.

## Configuring TUs

Each TU has a specific type, which you can maintain in Customizing by following the

menu path Transportation Management→Planning→Transportation Unit→Define

Transportation Unit.

Within the TU type, you configure the most important settings for the TU. For example,

you use the TU category to indicate whether you want to create the TU type for a

trailer, a railcar, a container, or a package. When you then create the related business

document (for example, a trailer unit), the system offers you only the relevant TUs.

Document Structure with Transportation Units

Document Structure with Transportation Units: An Explanation
The following table provides explanatory information about the preceding figure.

Transportation Order

Structure

176


Trailer TU 1

●

Contains FU 1 and FU 2

●  Defines own stages

Mover FO 1

Covers 1 TU stage

Mover FO 2

## Covers 2 TU stages

For truck and trailer scenarios, you have to configure freight order types and TU types.

## Service Order

Cleaning containers, fumigating, and performing security services or documentation

are typical examples of services that can occur for items of a freight order (FO) or

freight booking. The service order is used to account for and track services, calculate

charges, and enable settlement of the charges for services that have been provided

for individual items in a FO/booking or for the entire FO/booking.

You can create service orders in the following two ways:

●  Create service orders from freight bookings, FOs, freight booking items, or FO

items. With such a service order, you can:

○  Enter service items related to the freight booking, FO, freight booking

item, or FO item.

○  Add service items that are not related to the freight booking, FO, freight

booking item, or FO item. You can do this using the Add Service action

without marking another item.

●  Create standalone service orders without reference to any freight booking, FO,

freight booking item, or FO item. You can use the Create Service Order function

to create a service order by entering the service order type.

## Structure of Service Order

A service order contains the following information:

177


●  General data including the service provider, service order type, and status of the

service order

●  An item overview that contains the following information:

○  Link to the freight booking or FO for which the service order was

created. (Applies only for service orders created from freight bookings,

FOs, freight booking items, or FO items).

○

IDs of the original freight booking items or FO items for which services

are to be carried out, for example, containers or products. (Applies only

for service orders created from freight bookings, FOs, freight booking

items, or FO items).

○  Services to be carried out.

○  The location at which the services are to be executed and the time

period in which they are to be executed.

●  Transportation charges

●  Document dependencies as well as predecessor and successor documents

(document flow)

●  Other information such as the following:

○  Notes

○  Attachments

○  Change documents

○  Administrative data

○  Output management information

## Customizing Service Order

You make the required settings for service orders in Customizing for Transportation

Management under:

●  Freight Order Management→Define Item Types for Freight Order Management

●  Freight Order Management→Service Order→Define Service Order Types

●  Basic Functions→General Settings→Define Service Types.

You can use the change controller to define how the system reacts to changes.

Service Order Types, Service Item Types, and Service Types:

178


In Customizing, when defining service order types, you can specify the allowed service

item types (these must be item types of the category Service). You make the required

settings for service order types in Customizing for Transportation Management under

Freight Order Management→Service Order→Define Service Order Types.

For each service item type, you can specify the allowed service types. For more

information, see Customizing for Transportation Management under Freight Order

Management→Define Item Types for Freight Order Management.

Then, you can use the service order type you defined to create a service order. You can

specify one of the allowed item types for the order and the system proposes the

default service type for that item type. You can specify a different service type. If you

change this service type to a type that you have not specified in Customizing as

allowed for this item type, the system returns a warning message.

179


Lesson 2 - Warehouse Integration

## Direct SAP TM and SAP EWM Integration

Since the days of SAP TM 9.0, the integration of SAP TM with SAP EWM ran via SAP

ERP using SAP ERP shipments as an intermediate step. Data was not sent directly

between SAP TM and SAP EWM. Since release 9.1, SAP TM supports direct

integration between SAP TM and SAP EWM without creating shipments in SAP ERP.

The next step in the evolution is the current scenario, where both SAP EWM and SAP

TM run as part of the SAP S/4HANA system since release 1709. The SAP EWM for

SAP S/4HANA design was adapted to reflect the principle of one design idea, which

was the basic guideline for the development of the new system. For SAP EWM for

SAP S/4HANA, this meant both direct access to master data without the need for

replication and also structural changes in its architecture.

As part of its first release in SAP S/4HANA 1610, the inbound delivery notification and

the ODR were removed. The purpose of these objects was to reflect the information of

the delivery and form the basis for further warehouse execution. With the introduction

of SAP EWM for SAP S/4HANA, this intermediate step was no longer necessary to be

part of the overall design and thus was removed.

In this unit, we explain the current, direct integration in SAP S/4HANA within an SAP

EWM for SAP S/4HANA. The integration scenarios are still based on orders and

deliveries.

## Standard Integration Scenarios

To optimize transportation costs and efforts in a flexible and optimized way, SAP TM

supports transportation planning based on either SO requirements or outbound

deliveries. As part of transportation planning, the results influence warehouse-internal

processes such as staging. The integration of the SAP TM transportation planning

results into SAP EWM warehouse management processes is beneficial because it

enables smooth outbound processing with an optimized warehouse-internal process

according to the transportation planning result.

180


●  Order-based integration

●  Delivery-based integration

Integration type

Outbound

## Inbound

Order based

Sales orders

Purchase Orders

Delivery based

Outbound deliveries

## Inbound Deliveries

SAP Note 1984252 describes the known supported functional scope and limitations

of the direct integration.

Delivery-Based Transportation and Warehouse Integration

The delivery-based integration scenario is an integrated warehousing and

transportation process that sends ordered goods via an external carrier to external

customers from a warehouse managed with SAP EWM. Transportation is planned in

SAP TM, while warehouse activities are planned and executed in SAP EWM. This

process is based on SAP S/4HANA sales orders and transportation requirements are

based on SAP S/4HANA outbound deliveries.

181


Delivery processing in SAP S/4HANA involves grouping deliveries to pick, pack, and

ship and then performing all the functions associated with the delivery process. Based

on split criteria or combination indicators, you can group together entire orders or

individual items or split orders into partial deliveries. Outbound deliveries are created

and scheduled in SAP S/4HANA and are the basis for transportation planning in SAP

TM.

Because of the transportation planning in SAP TM, a freight order is created in SAP

TM, which, as soon as the freight order is ready for loading, results in the creation of a

transportation unit in SAP EWM.

One or more delivery positions can create one or more freight units. Always, the

documents created in SAP TM can be seen in the delivery via the document flow in the

TM Status tab of the delivery.

The deliveries are visible both in SAP TM for transportation planning and execution

and in SAP EWM for warehouse planning and execution. In SAP EWM, the delivery

182


creates an outbound delivery order, which acts as the actual warehouse request and

initiates the GI process in SAP EWM.

The outbound delivery contains data assumed from the preceding document and all

necessary information to trigger the GI process and monitor it accordingly. From the

perspective of warehouse management, the outbound delivery order represents a

worklist that is completed only when the picked materials have been loaded and

shipped.

The outbound delivery order in SAP EWM is still blocked for processing. It is released

as soon as the transportation planning process in SAP TM is completed, and SAP

EWM is updated with the final planning results. Sending the loading instructions to

SAP EWM creates a TU and automatically assigns the outbound delivery orders. With

this assignment, the outbound delivery orders are unlocked and updated with the

related carrier information from SAP TM.

Unlocked outbound delivery orders with transportation units are now the basis for

warehouse execution in SAP EWM. The SAP TM freight order now exists as a

transportation unit in SAP EWM. To easily identify the same object across all three

systems, they all share the same document number.

When the materials have been picked, staged, and loaded, GI can be posted. During

the outbound process execution, SAP TM is updated with all execution-relevant

information and events.

Order-Based Transportation and Warehouse Integration

In addition to delivery-based integration, SAP EWM and SAP TM can also work

together in an order-based process. In contrast to the previous scenario, the outbound

delivery is now created because of freight unit–based delivery proposals and

transportation planning in SAP TM. In the delivery-based scenario, inventory planning

and logistics execution had priority over the transportation planning process in SAP

TM, and deliveries were already created.

In the order-based scenario, SAP TM plans transportation based on SAP S/4HANA

sales orders and as a result proposes and creates deliveries based on the determined

183


dates and quantities. Transportation planning results in the creation of freight orders,

which are the basis for the delivery creation in SAP S/4HANA. In this context, SAP TM

considers transportation constraints, such as resource availability and transportation

durations. The created deliveries are usable by SAP EWM. In SAP TM, the freight order

can be the basis for tendering and carrier selection.

The process starts with a sales order and a planned delivery date. This automatically

creates freight units. These are then the basis for transportation planning and

optimization in SAP TM.

The transportation planning in SAP TM is completed when the transportation capacity

of the freight orders has been fully planned and all relevant transportation

requirements have been assigned. After the carrier has been assigned, SAP TM can

trigger the creation of a SAP S/4HANA outbound delivery and communicate the

freight order number to the selected carrier. These deliveries are based on the

transportation planning results and therefore consider planning constraints, such as

resource availability, distances, durations, and consolidation and dates. This step can

be executed manually or automatically as a background job. When the delivery has

184


been created, the document flow in SAP TM is updated to show all related documents

to a freight unit and freight order.

When the deliveries have been created, they are visible in the SAP EWM environment

for further processing as outbound delivery orders. The SAP S/4HANA delivery is

created with the proposed delivery date from SAP TM. If the SAP EWM outbound

delivery orders haven’t been assigned to a TU, these orders are locked for execution.

When the transportation planning activities are finished, and the freight order status

has been set to Cargo Ready for Loading, SAP TM sends a loading instruction to SAP

EWM. This triggers the creation of a TU in SAP EWM. In SAP EWM, the transportation

units are automatically assigned to the (locked) outbound delivery orders . With this

assignment, the outbound delivery orders are unlocked and updated with the related

carrier information from SAP TM. Unlocked outbound delivery orders, assigned to a

Transportation unit, are now the basis for warehouse execution in SAP EWM.

Goods are picked, staged, and loaded on a truck. Posting GI in SAP EWM immediately

adjusts the inventory in SAP S/4HANA, updating the outbound deliveries and the

freight order in SAP TM for a later freight cost settlement.

185


Lesson 3 - Advanced Shipping and Receiving

## Advanced Shipping and Receiving Overview

The Advance Shipping and Receiving is a new method to connect warehousing and

transportation. Advanced Shipping and Receiving is an integrated, end-to-end process

that allows users to send, receive, and transport products. The Advanced Shipping and

Receiving process is based on the freight order and does not use the EWM

transportation unit (TU) or the EWM vehicle. ASR supports mixed and multiwarehouse

scenarios within one freight order. Both integration processes, integration based on

the freight order or integration based on the EWM transportation unit, can run in

parallel.

## Advance Shipping and Receiving: Benefits

●  Cross-warehousing loading/ unloading: In Advanced Shipping and Receiving

you can integrate TM in S/4HANA with the following warehouse management

applications located in the same SAP S/4HANA system.

○  Lean Warehouse Management in SAP S/4HANA: You can use a very

simple warehouse where inventory management takes place solely at

186


storage location level. You need to create a place holder warehouse that

ensures the document flow in TM.

○  Stock Room Management in SAP S/4HANA: You can use Stock Room

Management for small warehouse operations and for warehouse

operations with low complexity. Stock Room Management contains SAP

S/4HANA functionality from the former Warehouse Management in

Logistics Execution (LE-WM).

○  Extended Warehouse Management in SAP S/4HANA: You can use EWM

for a flexible, automated support for processing various goods

movements and for managing stocks in your warehouse complex.

●  Easier Integration with business partners: Communication is simplified by

using a harmonized data model, by applying the EDIFACT standard to EDI

messages, and by providing dedicated apps and expanding existing apps and

RF transactions for shipping and receiving processes. Information moves freely

between the components and allows users to gain insights into the status of

the products during the process.

●  Multi-pick /mufti-drop: The freight order can contain both EWM managed and

IM managed storage locations, for example at a production location, and the

two storage locations can share a loading point. Same truck able to unload and

load at the same location during a multi-stop route with only one business

object freight order.

●  Simplified communication between components embedded in the SAP

S/4HANA: Advanced Shipping and Receiving simplifies communication

between components embedded in the SAP S/4HANA.

○  Transportation Management (TM)

○  Extended Warehouse Management (EWM)

○  Stock Room Management (STRM)

○

Inventory Management and Physical Inventory (MM-IM)

○  Logistics Execution (LE)

https://youtu.be/jLZM5S84AWM

187


Advanced Shipping and Receiving New Objects

Consignment Order:

A consignment order plays a significant role in facilitating communication within

business dealings involving multiple partners. For instance, if you are a supplier, a

consignment order allows you to convey to your ordering party the specific products

you deliver, the destination, and the delivery date. Each consignment order is given an

identification number, which acts as a mutual reference point for all involved business

partners. Each consignment order can be linked to a particular freight order.

188


A consignment order also forms the foundation for conducting various other tasks,

such as subcontracting, calculating charges, settling accounts with the carrier, and

even tracking shipments. However, tendering activities cannot be performed utilizing a

consignment order. This can be rectified in the customization settings for the

consignment order or freight order type, by enabling charge calculation and

settlement options or marking the documents of this particular type as suitable for

subcontracting.

Also, a consignment order can be assigned to a specific road freight order, allowing for

the determination of the exact vehicle that transports the product payload. While each

consignment order can only be connected to one freight order at a time, a singular

freight order can encapsulate multiple consignment orders. The planning and

execution of transport logistics arise from the freight order.

Furthermore, a consignment order can be linked to a transportation unit, such as a

container or trailer unit, which, in turn, can be attached to the freight order.

Nonetheless, the container or trailer unit must implement a transportation stage

mirroring that of the consignment order.

Detailed Organization of Loading and Unloading Activities

It is possible to deliver goods to or pick up goods from several warehouses at the

same location.

189


If you have a large warehouse with multiple loading or unloading points and several

doors, and you use more than one application component for warehousing, you can

organize your loading and unloading activities in detail, and decide which door, loading

or unloading point can be used by which application component. A loading point or

unloading point is defined in the master data as a location and represents a group of

doors where goods are delivered or picked up. This allows greater control over where

trucks load or unload cargo.

If you operate a sizable warehouse equipped with multiple loading or unloading

locations and an array of doors, along with the use of numerous application

components for warehousing, you have the ability to organize your loading and

unloading processes with precision. You can specify which door or which loading or

unloading location can be used with a particular application component. A loading or

unloading location is classified in the master data as a site and denotes a group of

doors that facilitate the delivery or collection of goods. This results in improved

command over the specific locations where trucks load or unload merchandise.

## Advanced Shipping and Receiving: Important Settings

Master Data: You have made the following settings in the location master data on the

SAP Easy Access screen under Logistics Transportation Management Master Data

Transportation Network Location:

190


●  You have activated Advanced Shipping and Receiving: You do this, by indicating

in the master data for your source or destination location. Location type 1003,

shipping point & location type 1200, loading points, is relevant for Advanced

## Shipping and Receiving. This setting is mandatory

●  You have defined a location with location type 1200 (loading point). The setting

is mandatory.

Assignment of Doors: Assign Stock Room Management (STRM) doors or Lean

Warehouse Management (Lean WM) doors to Extended Warehouse Management

(EWM) doors or loading points. This setting is mandatory for all scenarios using

shared doors and multiple warehousing components. The setting is not required for a

scenario that only uses EWM.

191


## Scenarios for Advanced Shipping and Receiving

As you can see on this slide, these scenarios offer distinct approaches to our

operations. Let's start with the first scenario, known as the warehouse-driven scenario.

In this case, the outbound delivery process is initiated, followed by picking and

packing. Once the picking process is completed, and the status of ready for shipping

is set, transportation planning can start. This scenario emphasizes the workflow

within the warehouse, ensuring that all necessary steps are completed, before moving

forward with transportation planning.

On the other hand, we have the transport-driven scenario, which can be based on

either sales orders or deliveries. The key difference between the two lies in the timing

of the delivery creation. In a transportation-driven scenario, based on sales orders, the

delivery is created after the transportation planning phase. However, in the other

scenario, the delivery is created immediately. After transportation planning, the

subsequent steps align with the warehouse-driven scenario, ensuring consistency in

the overall process.

To summarize, the transportation-driven scenario, regardless of whether it's based on

sales orders or deliveries, places emphasis on transportation planning, before

initiating the remaining steps in the process. In contrast, the warehouse-driven

192


scenario follows a sequential order within the warehouse, allowing for efficient

execution.

In conclusion, by considering these various scenarios and understanding the

implications, we can now optimize our operations and ensure a smooth flow

throughout the entire process. It's important to evaluate the specific needs of your

project and choose the most appropriate scenario that aligns with your objectives and

operational requirements.

In summary, future logistics and advanced shipping and receiving bring a multitude of

benefits to the transportation and logistics landscape. By harmonizing outbound and

inbound processes and integrating TM and EWM into S4/HANA, we have unlocked

new levels of efficiency and optimization. Our support for multipick, multidrop

scenarios, improved integration with business partners, and the introduction of new

objects like consignment and loading points, have all contributed to a seamless

logistics execution.

For those interested in exploring the subject in more detail, I recommend checking out

some related blogs and SAP Notes.

●  3225241 Advanced Shipping & Receiving Setup Guide Basic version

●  3271412 Advanced Shipping & Receiving Setup Guide GTS version

193


## Lesson 4 - Output Management

You can use output management to print, fax, and e-mail documents such as order,

delivery, and billing information. You can also execute application-to-application or

business-to-business actions. The Post Processing Framework (PPF) is a tool in

SAP TM used to execute program logic that is considered a follow-up action to a

certain business process step. The PPF is used for the following tasks or actions (to

name a few):

●  Document printing

●  Ending messages, such as e-mail, fax, or electronic data interchange (EDI)

●  Workflow triggers

All actions are defined in the PPF with a schedule condition that defines whether the

action must be executed and a processing time that defines when to execute the

action.

An action profile bundles all actions concerning a specific business process area (for

example, the action profile /SCMTMS/TOR bundles all actions important for the

freight order). You can see in the Action Settings area where we can define the

194


processing time of the action and whether the action can be scheduled automatically

or by a batch job.

The processing type of the action can be one of the following:

●  Trigger alert

●  Method call

●  Workflow

●  Smart Forms actions

●  External communication

To trigger PPF actions, start and schedule conditions must be configured according

to business needs or rules, as follows:

●  Schedule condition:

The schedule condition decides whether an action can be scheduled for

processing. An action is therefore only generated if the schedule condition is

met.

The filter value is specified in the Schedule condition field. The standard value

/BOFU/EVAL_SCHEDULE_CONDITION ensures that the method in the agent

class is invoked.

●  Start condition:

The start condition is checked before the action is executed. The action is

only executed when the start condition has been fulfilled.

The filter value is specified in the Start condition field. The standard value

/BOFU/EVAL_START_CONDITION ensures that the method in the agent

class is invoked.

## Adapter Settings

Output management automates the output of business documents such as printouts,

in response to certain business events. This output management adapter helps you

to integrate output management functionality with application business objects (BOs)

that are implemented in a business object processing framework (BOPF).

195


196


Lesson 5 - Track & Trace

## Execution Tracking

You use this function to determine whether the end user can manually report the

execution of transportation processes managed by TM, or not. For example, the end

user reports that an event has happened such as a freight order has arrived at a

destination.

Execution Tracking reports the tracking of the following TM business documents:

●  Freight Units

●  Freight Orders and Freight Bookings

●  Transportation Units

Features:

●  No Execution Tracking: With this option selected, there is no tracking of

executions. This is the default option.

●  Execution Tracking: With this option you allow execution tracking without an

external event management system. That is, the system automatically starts

the tracking of executions reported manually from transportation processes

managed by TM. The data this creates is stored in the TM database.

●  Execution Tracking with External Event Management; With this option you allow

execution tracking with an external event management system. The system

stores the data from the tracking of executions in the TM database, but it can

also send it to an external event management system. This option requires the

connection of an external event management system, such as SAP Event

Management. The use of SAP Event Management means that an end user can

use its simple in-built interfaces to report actual events, such as a freight order

has arrived. Further, the time that those actual events occurred can be

compared with the time they were expected to occur. In addition, SAP Event

Management allows events that are related but unexpected to be reported.

Together this means that for any tracked item a database record is always

available including its last known event. From that you can know whether that

item is on track, late or whether an unexpected has happened to it. You can

197


also use rule-based processing in-built into SAP Event Management to trigger

automatic follow up activities.

You can see and change the current settings for execution tracking in Customizing.

The path in Customizing depends on the type of TM business document as follows:

●  For freight orders, make the settings in Customizing for Transportation

Management under Freight Order Management Freight Order Define Freight

Orders Types. Then you select the Details button and under Execution Settings,

select an option from the field Execution Tracking Relevance.

●  For freight bookings, make the settings in Customizing for Transportation

Management under Freight Order Management Freight Booking Define Freight

Booking Types. Then you select the Details button and under Execution

Settings, select an option from the field Execution Tracking Relevance.

●  For transportation units, make the settings in Customizing for Transportation

Management under Freight Order Management Transportation Unit Define

Transportation Unit Types. Then you select the Details button and under

Execution Settings, select an option from the field Execution Tracking

Relevance.

●  For freight units, make the settings in Customizing for Transportation

Management under Freight Order Management Planning Freight Unit Define

Freight Unit Types. Then you select the Details button and under Execution

Settings, select an option from the field Execution Tracking Relevance.

198


## Event Management

Nowadays, supply chains are global and complex. End-to-end supply chain visibility is

one of the key factors in efficient supply chain operation and control. SAP Event

Management is the only application needed to provide this visibility, since it is

available to all partners, including customers. SAP Event Management can also work

with multiple SAP and non-SAP applications.

As companies expand their suite of IT products to handle more complex scenarios,

they often have to add systems to their ERP environment. This makes it difficult for

business users and management to gain a complete view of end-to-end processes

and monitor potential service issues. Therefore, it is imperative to have a tool that can

incorporate information from several systems and provide insight into how order

fulfillment is progressing.

SAP Event Management makes processes, assets, and performance visible across

the entire supply chain. Extensive tracking and tracing functions allow process

monitoring, automated exception resolution, proactive alerting, as well as extensive

reporting in a single solution.

The event management system is designed to work with several SAP ERP & S4 HANA

instances, if necessary. It can communicate with SAP CRM, where sales orders can be

received, and this communication is processed back to the customer to support order

199


fulfillment. SAP IBP can be responsible for creating the replenishment plan. SAP ERP

or SAP Manufacturing Execution can be responsible for communication and tracking

progress on the shop floor. SAP EWM (Extended Warehouse Management) can be

responsible for the picking and packing as part of the logistics execution.

## Event Management in SAP TM

SAP Event Management offers visibility processes to monitor transportation execution

in connection with SAP TM. The transportation execution visibility processes enable

users in roles such as transportation dispatcher, shipper, or ordering party, to track

and monitor planned events or to report an actual event.

Tracking and tracing is provided for the following business document types in SAP

TM:

●  Freight unit

●  Freight order

●  Freight booking

●  Transportation unit

●  Resource

●

Instruction execution for standard operating procedures

In each case, the goal is to manage by exception, reduce time to action, and spend

less time fire-fighting.

200


## Event Management Process

Monitor, notify, analyze, and adjust - these are the four cornerstones of SAP Event

Management, and they contribute in providing an adaptive solution. The monitoring

process collects data from the various source systems. Notifications can be set up to

be triggered, with alerts sent to the parties responsible if a process deviates from its

anticipated course. Based on the alerts, the appropriate parties can then simulate

adjustments and make any necessary changes. Finally, in relation to analytics, SAP

Event Management can be tied into the SAP BW environment to support

transportation management reviews.

201


In the integration between SAP TM and SAP EM, two different interfaces and functions

are used, as follows:

1.  Creation and update of the Event Handler with all expected events and other

critical fields such as parameter and tracking IDs.

2.  Sending or reporting of events from the SAP TM system, for example, loading

or unloading events from freight unit or freight order.

To be able to create event handlers in SAP TM, you must configure the application

object types (AOTs). From the AOTs, the extractors are created. These extractors send

the data to SAP EM and create SAP EM event handlers.

Content of Application Object Types
Application Object Types contain the following:

●  Expected events, with planned dates and times

●  Tracking IDs that uniquely identify the trackable object or business document,

for example, a freight order

●

Information and system parameters that contain information about the object

202


## Content of Extractors
The extractors contain the following:

●  A freight order

●  A freight booking

●  A freight unit

●  A transportation unit

●  Other objects

An event handler represents a business document (for example, freight order, freight

unit, or transportation unit) or a business process (for example, within a

Transportation Execution) that is relevant to tracking or monitoring functions. SAP EM

creates an event handler for each object. The event handler contains all of the

information necessary to track this application object. It contains this information in a

form that is independent of its origin, so that SAP EM can map and track business

processes in a uniform way.

The event handler information makes it possible to enable the monitoring of events

that are reported to SAP EM for an application object, and to check if the actual events

203


occur in line with the expected events. In SAP TM, event types are used to send or

report events to SAP EM.

GTT

The aim of SAP Logistics Business Network, global track and trace option is to

capture, process, and store tracking information about tracked processes and objects.

Then, it allows business users to get real-time transparency of the execution of those

processes. They can query any tracked process and display its retrieved data from

end to end.

Further, SAP Logistics Business Network, global track and trace option can use

rule-based triggering to automatically detect when certain predefined conditions occur

such as delay or damage to goods. The rules can also be used to trigger follow-up

activities such as sending e-mails to users or updating back-end systems.

SAP Logistics Business Network, global track and trace option is a cloud service. The

service is an optional package that you can select as part of the SAP Logistics

Business Network solution.

Features:

1. A cloud-based track and trace service to capture, process, and store messages with

tracking information about business processes.

2. A cloud-based service that allows connected cloud apps to trace those business

processes by retrieving tracking information.

3. Tools for an administrator to define and model the business processes to be

tracked and their related events and properties. He or she can also configure business

rules used by the event-to-action engine to process and evaluate received event

messages and to trigger automated follow up actions.

4. Tools for an administrator to replicate master data (business partner, location, and

product) from connected back-end systems.

5. Tools for an administrator to manage onboarding, configuration, and setup.

204


6. Apps for a business user, for example, to query any tracked process or object and

display it from end-to\u0002end, including to:

●  display its milestones with planned and actual date/times

●  display details of its processes

●  report planned and unplanned events

●  visualize related locations on a geographical map

205


## Lesson 6 - Discrepancy Management

The actual quantity cannot be estimated precisely beforehand, for example, when

transporting bulk freight. When the transportation execution starts, the actual quantity

must be recorded as well. This process in the SAP TM functionality is called

discrepancy handling. Discrepancies are a hassle for transportation execution

because they might affect the choice of vehicle resource being used for the

transportation or lead to a different charge calculation. Therefore, discrepancies must

be discussed with the shipper before transportation can continue. The transportation

process starts as usual, requested quantities are entered into a forwarding order, and

freight units are created out of this document. After the freight units are planned, the

execution of the transportation can begin. The carrier now physically receives the

cargo and checks the actual quantities against the requested quantities. This

checking and reporting is performed by the carrier and communicated to us as the

freight forwarder. We will then enter the actual quantities in the freight order’s items.

If the carrier does not receive the cargo as planned, you must report the discrepancy.

In general, you can differentiate between two types of discrepancies as follows:

●  Quantity discrepancies: The actual quantities are different from the requested

quantities because of a change in the quantity, gross weight, or volume.

206


○  The actual quantity, the actual weight, or the actual volume is lower than

expected.

○  The actual quantity, the actual weight, or the actual volume is larger than

expected.

○  You have received an unexpected cargo.

●  Other discrepancies: Discrepancies that are not caused by a change in

quantities are called other discrepancies. If the cargo is damaged, or

documents are missing for the cargo, these events can be recorded as other

discrepancies.

○  There is a dangerous goods item that you have not designated as such.

○  The packaging of an item is damaged.

○  You have received over dimensional or high-value cargo.

○  A different equipment type or package type has been used.

## Customizing Discrepancy

Before you can handle any discrepancies in SAP TM, you define the discrepancy types

in Customizing.

You can define different types of discrepancies in Customizing by following the IMG

menu path Transportation Management→Freight Order Management→Define

Discrepancy Profile.

In this Customizing activity, you can define discrepancy types and associate them with

predefined events and discrepancy subcategories. Further, among the discrepancy

types associated with the same event, you must select one discrepancy type as the

default discrepancy type. You can also define lower or upper discrepancy tolerances.

You can define discrepancy profiles. If you do so, you can assign discrepancy types

with different stop categories to them. You can assign discrepancy profiles to freight

order types, freight booking types, and transportation unit types.

## Methods of Entering Discrepancies

The following options are available when reporting discrepancies:

207


●  Report quantity discrepancies in the Items tab of FO, FB, or TU and actual

values in the Quantities tab of the item details.

●  Report other discrepancies in the Items tab of FO, FB, or TU and enter detailed

information in the Discrepancies tab of the item details.

●  Add any necessary attachments to a reported discrepancy within the

Attachments column on the Discrepancies tab of the item details.

●  Add any necessary notes to a reported discrepancy within either the Note or

the Notes column on the Discrepancies tab of the item details.

●

It is possible to unassigned FUs for which discrepancies have been reported.

FUs can be unassigned from a FO, FB, or TU in the FO/FB/TU screen or in the

transportation cockpit. While the discrepancy and the block or blocks still exist

on the freight unit level, they are removed in the FB, FO, or TU. This means that

the cargo (without the goods of the unassigned FU) can proceed with further

processing.

## Features

When a discrepancy is reported in an FO, FB, or TU document, the system

automatically blocks the subsequent stages of the transport when reported

discrepancies are not yet resolved.

208


For freight units, further planning and execution are blocked.

For freight orders, freight bookings, and transportation units, execution and invoicing

blocks are set.

In SAP TM, you can select a checkbox in the freight order, freight booking document,

or transportation unit that prevents the system from setting a block.

If there are unresolved discrepancies in a document, it is not possible to set the freight

execution status to Freight Ready for (Un-) Loading. Moreover, a block on an

unresolved discrepancy implies that no goods receipt can take place; therefore, you

cannot set the cargo receipt status.

## Resolving Discrepancies

During execution, discrepancies can be determined between the actual quantities and

the quantities that have been ordered by the customer. Furthermore, exceptions can

occur, such as missing or damaged cargo. This data can be sent from SAP EWM to

SAP TM, and either copied into the freight order or freight booking automatically, or

entered into the freight order or freight booking manually.

The customer service agent or transportation planner must decide with the ordering

party how to proceed with the discrepancies. Depending on this decision, the

customer service agent can adjust the ordered data to the actual data, or can plan the

subsequent delivery of missing cargo.

To support the exception handling process, the following functions of SAP TM have

been added or enhanced:

●  Discrepancy profile with the option to define discrepancy subcategories

●  Personal object worklist (POWL) for discrepancies

●  Copy of actual data from freight document to ordered data of forwarding order

●  Change of forwarding order data after execution has started

●  Assignment of local freight document items to forwarding orders and freight

units

●  Manual freight unit split after execution has started

●  Manual corrections of items, for example, after transfer of data from SAP EWM

209


Conditions for Using the Resolve and Undo Resolve Buttons

You can use the actions associated with the Resolve button for specific discrepancy

types only. The following conditions apply:

●  Resolve discrepancy:

This action is permitted for all discrepancy types, except for discrepancies with

the subcategory Missing Cargo. You cannot execute the Resolve action for this

subcategory if the Quantity Update column in the Customizing activity Define

Discrepancy Profile has the value Split Predecessor Document.

●  Resolve missing cargo (retain FU item):

You can execute this action for discrepancies with the subcategory Missing

Cargo only if the Quantity Update column in the Customizing activity Define

Discrepancy Profile has the value Split Predecessor Document.

●  Resolve missing cargo (delete FU item):

You can execute this action for discrepancies with the subcategory Missing

Cargo only if the Quantity Update column in the Customizing activity Define

Discrepancy Profile has the value Split Predecessor Document.

●  Resolve unexpected cargo (assign FWO item):

You can execute this action only for discrepancies with the subcategory

Unexpected Cargo.

You can use the action associated with the Undo Resolve button for specific

discrepancy types only. The following conditions apply:

●  The discrepancy must have the status Resolved.

●  The discrepancy must not have the subcategory Missing Cargo. If the

discrepancy does have the subcategory Missing Cargo, the action Undo Resolve

can be executed only if the Quantity Update column in the Customizing activity

Define Discrepancy Profile does not have the value Split Predecessor Document.

210
