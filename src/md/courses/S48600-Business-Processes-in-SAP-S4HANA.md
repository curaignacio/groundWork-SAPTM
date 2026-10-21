S48600  -  Business  Processes  in  SAP
## S/4HANA TM

Unit 1 - Introducing Transportation Management

Unit 2 - Defining Transportation Management Master Data

## Unit 3 - Developing Transportation Networks

Unit 4 - Managing Transportation Capacities, Conditions and Incompatibilities

Unit 5 - Creating Transportation Requirements

Unit 6 - Planning Transportation

Unit 7 - Monitoring Transportation Execution

Unit 8 - Processing Transportation Cost and Charges

2-16

17-33

34-54

55-70

71-87

88-153

154-190

191-220


Unit 1 - Introducing Transportation Management

Lesson 1 - Explaining the Transportation Management Features
and Functions

## Objective

After  completing  this  lesson,  you  will  be  able  to  explain  standard  processes  in
transportation management.

Transcript for video:

“The concept of managing the transportation of products is not new. People have
been  shipping  products  across  local  regions,  kingdoms,  countries  and  even
continents  throughout  recorded  history.  However,  new  methodologies  and
technologies  have  made  a  significant  impact  in  the way we transport goods, as
well  as  the  considerations  involved  in  optimizing  this  process.  Today,  most
economies  are  wholly  reliant  on  efficient  transportation  logistics.  With  the  shift
towards  a  global  economy,  crossing  borders  has  become  commonplace  and
reaching  customers  in  more remote locations, as well as sourcing products and
materials  from  multiple  vendors  or  locations  has  increased  the  complexity  of
transportation  networks.  Meanwhile,  natural  disasters,  conflicts  and  other
dangers  highlight  the  vulnerability  of  the  global  supply  chain.  Despite  these
challenges,  the  transportation  portion  of  the  supply  chain,  in  particular,  has  to
solve  these  problems  as  they  arise  in  order  to  keep  factories  running  and
customers  supplied,  responding  faster  and  more  cost-effectively.  Business
executives  and  the  teams  they  oversee  must  ask  questions such as: How can I
manage  my  logistics  network  in  a  holistic  fashion? How can I minimize the risk
factors throughout my supply chain? How can I reduce my operational costs and
better  understand  transportation  costs  at  the customer level? How can I ensure
the  best  possible  usage  of  my  assets?  How  do  I  ensure  high  customer  service
levels  and  responsiveness  to  unexpected  supply  chain  events?  And,  how  do  I
ensure I am compliant with all of the varying regulations and compliance policies?
Tackling  transportation  issues  such  as these can impact business operations in
other  areas  as  well  because  transportation  management  is  never  an   isolated
process.  Rather,  it  is  always  integrated  into  other  business  processes.  If
transportation management is poorly organized, this may have a negative impact
on  related  business  processes,  for  example,  manufacturing  or  distribution.  SAP
TM  allows  SAP  ERP  customers  to  achieve  seamless  order  processing  and

2


management, with out-of-the-box integration for order-to-cash and procure-to-pay
scenarios. The platform offers planning features to support comprehensive order
management, encompassing forwarding, land freight via truck and rail, as well as
sea  and  air  freight  booking  scenarios.  This  integrated  environment  enables  full
document  flow,  order
lifecycle  management,  and  centralized  order  data
management  for  planning,  tendering  and  monitoring,  so  you  can  deal  with
transportation challenges as they arise.”

In  this  video,  we  explore  transportation  logistics  in  a  global  economy  and  the
challenges  of  managing  global  supply  chains.  In  particular,  some  of  the  business
challenges executives and their teams face are:

●  How can I holistically manage my logistics network?
●  How can I minimize the risk factors throughout my supply chain?
●  How  can  I  reduce  my  operational  costs  and  better  understand transportation

costs at the customer level?

●  How can I ensure the best possible usage of my assets? How do I ensure high
customer  service  levels  and  responsiveness  to  unexpected  supply  chain
events?

●  How  do  I  ensure  I  am  compliant  with  all  of  the  varying  regulations  and

compliance policies?

Transportation  management  is  never  an  isolated  process.  Instead,  it's  permanently
integrated into other business processes. SAP TM seeks to provide a full suite of tools
built for managing the various operational stages of transportation management and
integrations to ensure seamless function and transparency across your business.

3


## SAP Transportation Management Overview

SAP  Transportation  Management  (SAP  TM)  provides  comprehensive  support  for  a
wide  variety  of  complex  scenarios  relevant  to shippers and logistic service providers
around the world. Supported scenarios include the following examples:

●  Scenario Types: Inbound, outbound, domestic, and international.
●  Goods/Cargo: General, bulk, fluid, packaged, and loose.
●  Shipping  Types:  Less  than  Truck  Load  (LTL),  Full  Truck  Load (FTL), Less than
Container  Load  (LCL),  Full  Container  Load  (FCL),  and  Courier  Express  Parcel
(CEP).

●  Movement  Types:  Direct  shipment,  uni-modal,  multimodal,  port-to-port,

door-to-door, and export shipment

●  Stage  Types:  Pickup,  precarriage,  main carriage, on-carriage, delivery, drayage,

and haulage.

●  Parties  and  Roles:  Ordering  party,  shipper  or  sender,  consignee  or  recipient,
invoicing  party,  payment  party,  notifying  party,  agreement  party,  importer  or
exporter, and forwarder or carrier.

●  Legal  Documentation:  House  Bill  of Lading (HBL), House Air Waybills (HAWB),

manifests, and delivery notes.

Transportation Management's Five Main Stages

4


The processes covered by transportation management fall under these five stages:

1.  Requirements and Order Management
2.  Transportation Planning
3.  Transportation Execution
4.  Freight Costing and Settlement
5.  Analytics and Collaboration

The  following  video  briefly  summarizes  each  of  these  transportation  management
stages.

Transcript for video:

is

typical  transportation  process  starts  with  order  management.  Order
“A
the  process  of  creating  a  transportation  requirement.
management
Transportation  requirements  can  be  derived from sales orders, purchase orders,
deliveries,  and  so  on.  In  a  second  step,  these  transportation  requirements  are
planned.  SAP  TM  offers  manual  planning  functions,  optimizer  planning,  and
semi-automated  processes  such  as  transportation  proposal  creation.  Different
aspects  of  planning  supported  by  SAP  TM are means-of-transport selection, for
example,  rail  versus  road,  carrier  selection  based  on  real  carrier  rates,  and  load
optimization,  which  offers  3D-planning  of container or truck utilization. Once the
planning  process  is  finished,  SAP TM also supports the execution of transports.
Execution  includes  delivery  creation,  document  creation,  such as waybills which
can be delivered either in print or electronic form, event management integration
or  track  and  trace,  as  well as warehouse integration with solutions such as SAP
EWM.  If  you  do  not  operate  your  own  fleet,  you  need  to  make  sure  that  the
external  carrier  is  paid  for  their  services.  SAP TM allows you to maintain freight
agreements,  calculation  sheets,  and  rate  tables  to  accurately  define  real  carrier
costs,  which  can  be  used  for  charge  calculation,  but  also  for  settlement
processes  after  the  transport  has  been  executed.  Analytics  and  reporting
functionalities  complete  the  available  functions  of  SAP  TM.  Throughout  this
course  we  will  explore  each  of  these  areas  of  Transportation  Management  in
more detail. Enjoy learning with SAP!”

5


The Five Stages of SAP Transportation Management in More Detail

Requirements Management and Order Management

transportation  process  starts  with

The
transportation
requirements  derived  from  orders.  For  shippers,  the  creation  of  these  requirements
can occur in two distinct scenarios:

the  management  of

●

Integrated  Sales  Order  and  Delivery  Process:  Sales  order  and  delivery
processes  and  transportation  management  are  handled  inside  the  same
instance/system,  often  referred  to  as
"Embedded".  Logistics  business
documents  derived  from  Sales  and  Distribution  (SD),  Materials  Management
(MM),  or  those  generated  in  Logistics  Execution  (LE)  serve  as  the  source  for
transportation requirements and planning.

●  Decentralized Sales Order and Delivery Process: Sales orders and deliveries are
handled  in  one instance/system, and transportation management is done in a
separate
instance/system.  Order-based  transportation  requests  (OTR)  or
delivery-based  transportation  requests  (DTR)  represent  a  transportation
demand  based  on  an  order/delivery created in an SAP S/4HANA ERP system.
In  this  scenario,  order-  or  delivery-based  transportation  requirements  are  the
source of transportation requirements and planning.

All  the  documents  mentioned  here  are  sources  for  transportation  requirements  and
planning.  The  data  from  these  source  documents  is  used  to  create  one  or  multiple

6


freight units. The business document data, along with freight unit building rules, form
the basis for building a freight unit. A freight unit is the smallest planning unit used in
transportation  planning and represents a collection of goods that can be transported
together throughout the complete transportation process chain.

## Transportation Planning

During  planning,  freight  units  are  assigned  to  means  of  transport  to  create  freight
orders. SAP TM offers choices for manual planning, optimization-driven planning, and
semiautomated  procedures  such  as  generating  transportation  proposals,  creating
unified packaging hierarchies, and optimizing loads.

Load  optimization  aims  to  maximize  container  or  truck  space  utilization  within  a
three-dimensional  framework.  In  the  planning  process,  various  attributes  (including
those  associated  with  time  and  geography),  capacities  (encompassing  vehicle
resources,  types,  and schedules), and elements related to the transportation network
(involving  locations,  zones,  and  lanes)  are  considered.  Also,  the  planning  process
addresses  constraints,  such  as  capacity,
routing,  scheduling,  and
incompatibilities.

time,

Planning  is  conducted  within  the  Transportation  Cockpit  user  interface  (UI).  The
transportation  cockpit  can  tailor  its  interface  to  suit  the  specific  planning  scenario.
This  includes  options  like  map-based  planning,  Gantt  chart  planning,  drag-and-drop
functionality,  load  planning,  and  command-based  planning,  all  of  which  can  be
executed seamlessly within the transportation cockpit.

Carrier  selection  can  be  undertaken  either  during  the  planning process or afterward.
Carrier selection can be executed through multiple methods. It can be done manually,
utilizing optimization algorithms, or via a tendering process. The primary aim of carrier
selection is to establish a ranked list of carriers eligible to fulfill a planned freight order.
This  selection  process  considers  constraints  such  as  costs,  priorities,
incompatibilities, and business allocations. The tendering process can function as an
integral  part  of  carrier  selection  or  as  a  distinct  and  separate  process.  Within  the
tendering  process, freight orders are proffered to eligible carriers through a tendering
or auction procedure.

## Transportation Execution

Transportation execution encompasses a comprehensive range of activities related to
managing and documenting shipments during transit. The freight order serves as the
foundation of the execution process, providing precise details and actual quantities of
the  cargo  being  transported. Any discrepancies between the initial order capture and
planning  phases  and  the  physical  verification  and  handling  are  systematically

7


includes  actions

recorded.  Furthermore,  moving  cargo  triggers  updates  to  both  the  order  and  cargo
status.  This
into  the
transportation  management  system  or  automatic  updates  facilitated  through  SAP
Event  Management  and  Global  Track  and  Trace,  ensuring  real-time  visibility  and
traceability of the shipment's progress.

like  manual  entry  of

loading  status

## Freight Costing and Settlement

Charge  management  delivers  comprehensive  financial  insights  by  supplying  precise
details  concerning  costs,  revenue,  and  profitability  within  the  transportation domain.
Within  this  framework,  agreements  play  a  central  role,  serving  as  contractual
instruments  between  purchasing  organizations  and  suppliers  through  freight
that
agreements.  These  agreements  explicitly
encompass an exhaustive list of charge elements used in the computation of fees for
customers or suppliers. The calculation engine analyzes these charge elements within
the  calculation  sheet  and  calculates  the  correct fees for transportation charges. The
outcomes of these calculations are recorded in the freight order for supplier invoices.

reference  calculation  sheets

Draft  invoices  can  be  created  for  settlement  integration  to  the  SAP  S/4HANA  ERP
from freight orders. For supplier invoice settlement, freight settlement documents are
created  from  the  freight  order  and  transferred  to ERP to create accruals and later to
create  a  purchase  order  and  service  entry  sheet  (SES)  for  invoice  verification  or
self-billing.

## Analytics and Collaboration

Within  the  SAP  TM  system,  a  range  of  relevant  overview  pages,  reports,  and  KPI
dashboards  have  been  created  for  shippers  and  logistic  service  providers.  These
overview pages provide a consolidated view of all data from day-to-day activities and
help in real-time decision-making. These pages can be tailored to business roles, and
users who supervise transportation execution can start their day by navigating to the
freight order execution overview.

## Common Terms Used in SAP Transportation Management

The  following  table  provides  a  list  of  transportation  objects  and  their corresponding
definitions:

8


Transportation
## Object

Order-Based
Transportation
Requirement

## Sales
Purchase
Stock
Order

Order,
Order,
Transfer

Abbreviation

Description

OTR

An  object/document  representing the demand
from sales, purchasing, and stock transport.

## SO, PO, STO

An  object/document
procurement, or transfer of goods demand.

representing  sales,

Delivery-Based
Transportation
Requirement

DTR

## Inbound
Delivery/Outbound
Delivery

## IDL/ODL

Freight Unit

FU

object/document

An
the
transportation  demand  from  an  inbound  or
outbound delivery.

representing

object/document

the
An
transportation  demand  from  an  inbound  or
outbound delivery.

representing

An  object/document  that  represents  a  set  of
good  that  are  transported  together across the
entire supply chain.

Freight Order

FO

An  object/document  whose  execution
planned by a carrier or a shipper.

is

Freight Agreement  FA

An object/document that represents a contract
with the carrier.

Freight  Settlement
Document

FSD

An  object/document  that  is  used  to  verify
carrier invoice.

9


Lesson  2  -  Accessing  Transportation  Management  Using SAP
Fiori Apps

## Objective

After completing this lesson, you will be able to set up workspace preferences and create
queries and views to analyze transportation needs and transportation orders.

SAP Fiori Reference Library and SAP Fiori Launchpad Overview

## SAP Fiori Launchpad

The  SAP  Fiori  launchpad  is  a  shell  that  hosts  SAP  Fiori  apps  and  provides  services
such as navigation, personalization, embedded support, and application configuration.

The  launchpad  is  the  entry  point  to  SAP  Fiori  apps  on  mobile  and  desktop  devices.
The  SAP  Fiori  launchpad  home  page  is  the  first page users see after signing in. The
launchpad home page displays tiles and links, allowing users to launch apps. Tiles are
a visual representation of an app. Each tile represents a business application that the
user can launch.

The  tiles/apps  displayed  to  users  on  the  SAP  Fiori  launchpad  are  organized  using
catalogs and groups.

10


A catalog is a set of tiles that you want to make available for one role. These catalogs
are  assigned  to  business  roles.  Depending  on  the  role  and  the  catalogs assigned to
the role, users can browse through the catalogs and choose the tiles.

Groups  define  the  grouping,  sort  order,  and  general  appearance  (tile  or  link)  of apps
that are initially displayed on the SAP Fiori launchpad home page for a user. Users can
personalize  the  Entry  Fiori  Page  by  adding  or removing applications to predefined or
self-defined groups.

The SAP Fiori launchpad layout can be structured by groups or by spaces and pages.

A  space  serves  as  an  entry  point  for  a  business  role  and  shows  information  and
functions  that  are  assigned  to  that  business  role.  A  space  is  represented  as  a
navigation  item  in  the  top-level  navigation.  It  consists  of  one  or  multiple  pages  that
further structure the content of a space.

11


A  page  is  part  of  a  space  with  one  or  multiple  pages.  Multiple  pages allow users to
structure  the  space into numerous self-contained work contexts. Business roles with
fewer  apps  may  use  one  page  per  space,  whereas  those  with  more  apps  may  use
multiple  pages.  A  page  consists  of  sections  that  are  used  to  structure  the  content
further.

A  section  structures  the  content  of  a  page  semantically.  A  section  consists  of  tiles
that visualize the content of a space. A section title is optional.

Users can switch between both layouts with the user actions menu.

12


## SAP Fiori Library

The  SAP  Fiori  Apps  Reference  Library  is  a  comprehensive  library  of  all  relevant SAP
content for the SAP Fiori launchpad. All available apps can be explored using the SAP
Fiori Apps Reference Library. See https://www.sap.com/fiori-apps-library.

SAP  Fiori  apps  can  be  categorized  by  line  of  business,  industry,  user  role,  and
technical foundation.

Using the library, you can:

●  Find  filters  such  as  Application  Type  and  Product  Version  to  help  select  the

sets of apps needed.

●  Find  key  information  for  each app, including all the technical data required for

installation and configuration

13


In  the  details  for  an  SAP  Fiori  app,  you should first set the product suite followed by
the release at the top of the page. Although an app is available in several products and
releases,  their  implementation  may  differ.  The  header  information,  product  features,
implementation  information,  and  related  apps  change  depending  on  the  selected
product and release.

Catalogs  are the basis of the SAP Fiori content in the SAP Fiori launchpad. Technical
catalogs  define  apps  per  solution  area,  whereas  business  catalogs  reference  these
apps  per  user duty. Groups, spaces, and pages reference tiles and links per business
topic  from  business  catalogs.  Business  catalogs,  groups,  and  spaces  can  then  be
assigned to users via business roles.

## Worklist in SAP TM

Personal Object Worklist (POWL)

One  of  the  more  flexible  tools  available  to  users  in  SAP  TM  is  the  Personal  Object
Worklist  (POWL).  As  an  Enterprise  Portal  user,  the  Personal  Object  Worklist  (POWL)
provides  you  with  a  general  overview  of  your  work  environment  and  all  related
business objects you would be interested in working on.

14


The  Personal  Object  Worklist  (POWL)  provides  central,  personalized  access  to
document lists. It gives users a portal-based interface that they can use to define (and
optionally  store)  queries  in  a  similar  way  they  are  used  to  from  SAP  ERP  selection
screen  variants.  This  tool  allows  users  to  easily  access  queries  and  create,  change,
delete,  or  categorize  queries.  Application-related  buttons  provide  object-based
functions. The data table can be filtered, and other settings can be applied. Users can
personalize  the  data  table  and  refresh  a  single  or all queries. The user sees the very
latest  information  thanks  to  a high-performance refreshing and caching mechanism.
Updates  run  asynchronously,  and  worklists  remain  available  until  the  results  are
refreshed.

15


Transactional Screen View

16


Unit 2 - Defining Transportation Management
## Master Data

Lesson  1  -  Explaining  General  Master  Data  for  Transportation
Management

## Objective

After completing this lesson, you will be able to conceptualize general master data.

Introducing General Master Data in SAP TM

Transcript for video:

“Well  maintained  master  data  can  be  drawn  on  as  a  single  source  of  truth  for
multiple  business  processes,  ensuring  that  the  information  used  across  many
touch-points  is  correct  and  making  the creation of records much more efficient.
Master data in SAP Transportation Management forms the backbone of efficient
logistics  planning  and  execution.  Accurate  master  data  ensures  seamless
operations,  minimizes  errors,  reduces  costs,  and  ultimately,  enhances customer
satisfaction.  In  this lesson we will talk about some of the master data related to
transportation  types,  organizational structures, materials, and business partners,
relevant  to  Transportation  Management.  In  SAP  TM,  transportation  modes,
means  of  transport,  and  vehicle  resources  are  organized  hierarchically.
Transportation  modes  define  broad categories of transportation like sea, air, rail,
or  road.  Means  of  transport  categorize  vehicle  types  within  these  modes,  and
vehicle resources record specific vehicles or fleets depending on the needed level
of granularity. Organizational structures lay out how departments and units within
a  company  are  organized.  These  structures  are  vital  for  managing  data,
include  sales
transactions,  and  authorizations  effectively.  Key  elements
organizations,  distribution  channels,  and  shipping  points.  Material  master  data
categorizes  raw  materials,  semi-finished  and  finished  products,  packaging
materials,  and  more.  Centralized  data  reduces  inconsistencies  and  provides  all
departments  with  accurate  logistics  information.  Material  master  data  includes
attributes  relevant  to  transportation,  such  as  dimensions  and  transportation
groups.  These  attributes  are  crucial  for  planning  and  executing  transportation
efficiently. Business partners in SAP TM include customers, vendors, carriers, and
more.  A  single  business  partner  can  have  multiple  roles  such  as  being  both  a

17


customer  and  a  vendor.  Maintaining  a  single record about this business partner
and  then  applying  the  different  roles,  rather  than  maintaining  two  separate
records  on  the  sales  and  purchasing  sides  of  the  business  streamlines  the
process  of  doing  business  with  this  partner.  Master  data  is  fundamental  to
optimizing  business  processes  in  SAP  S/4HANA  and  SAP  TM.  I  hope  this
overview  helps  clarify  why  understanding  master  data  is  important  and  how  it
impacts transportation management. Enjoy learning with SAP!”

## Master Data Overview

## SAP Transportation Management Master Data: An Overview

SAP  Transportation  Management  (SAP  TM)  is  a  robust  and comprehensive solution
designed  to  manage  and  optimize  transportation  processes. The master data within
SAP  TM  forms  the  foundation  for  efficient  transportation  planning  and  execution.  It
serves  as  the  single  source  of  truth,  encompassing  critical  information  about
organizational  structures,  products,  business  partners,  transportation  routes,  and
logistical  parameters.  Accurate  and  well-maintained  master  data  ensures  seamless
interoperability  between  various  business  functions,  enabling  precise  planning,
execution,  and  monitoring of transportation activities. This minimizes errors, reduces
operational  costs,  and  enhances  customer  satisfaction  by  providing  consistent  and
reliable  data  across  the  entire  supply  chain.  Moreover,  master  data  facilitates
regulatory  compliance  and  enables  advanced  analytics,  driving
informed
decision-making and strategic planning.

18


Master  data  relevant  to  SAP  Transportation  Management (SAP TM) encompasses a
variety  of  key  elements  essential  for  the  smooth  and  efficient  functioning  of
transportation processes. These master data elements include, but are not limited to:

●  Organizational Structures: The hierarchical arrangements within an

organization that define the various departments, units, and their relationships.

●  Material Masters: The comprehensive database of materials that records all

pertinent details and attributes of the materials used within the transportation
process.

●  Business Partners: The records of all entities such as suppliers, customers,
carriers, and so on, that interact and engage in business transactions.

●  Transportation Mode: The different types of transportation methods, such as

road, rail, air, and sea, utilized in the logistics chain.

●  Means of Transport: Means of Transport: The specific vehicles or vessels used

to carry goods, such as trucks, ships, airplanes, and trains.

●  Transportation Networks: The connections that facilitate the movement of

goods from origin to destination.

●  Location: The geographical points, such as warehouses, ports, and distribution

centers, that play a crucial role in the supply chain.

●  Zones: The predefined geographical areas that help in planning and managing

transportation activities.

●  Lanes: The specific paths between two locations that are frequently used for

transportation.

●  Routes The predefined pathways that goods follow during transportation,
which may include multiple stops and various transportation modes.

●  Schedules: The planned timelines for transportation activities and movements,

including departure and arrival times.

●  Resources: The assets, such as equipment, and vehicles, that are deployed to

execute transportation tasks.

●  Conditions: The specific criteria or restrictions that must be met during the

●

transportation process.
Incompatibilities: The constraints and restrictions that prohibit certain
combinations of goods, modes, or resources.

In  Units  2,  3,  and  4,  we  will  delve  deeply  into  each  of  these  master  data  types,
providing  insights  and  practical  guidance  on  how  to  effectively  utilize  each  type  of
data within SAP Transportation Management.

19


Transportation Mode, Means of Transport, and Vehicle Resource.

## Definition, Role, and Examples

The  relationship  between  Mode  of  Transport,  Means  of  Transport,  and  Vehicle
Resource  is  hierarchically  structured  and interdependent, forming a cohesive system
for the conveyance of goods.

1.  Mode of Transport: The transportation mode delineates the method by which
goods are conveyed, such as via sea freight, air cargo, rail transport, or road
transport.

●  Definition: This defines the overarching method by which goods are
moved from one place to another, such as by sea, air, rail, or road.

●  Role: It sets the framework and parameters within which specific means

of transport operate.

●  Example: Sea freight, air cargo, rail transport, road transport.

2.  Means of Transport: This term denotes a categorization of vehicle resources

that are designated to a specific transportation method.

●  Definition: This is a classification encompassing different types of
vehicles that are used within a particular transportation mode.
●  Role: It forms the bridge between the transportation mode and the
specific vehicle resources. It provides a generalized grouping of
transport vehicles suited to a particular mode.

●  Example: Cargo ships (sea freight), aircraft (air cargo), trains (rail

transport), trucks (road transport).

20


3.  Vehicle Resource: An entity representing an individual instance or a collection

of identical instances of a particular means of transport, facilitating the
provision of transportation services.

●  Definition: This represents specific instances or sets of similar instances

of a particular means of transport.

●  Role: It's the actual asset that provides transportation services,
operating within the means of transport category for a given
transportation mode.

●  Example: A specific cargo ship like the MSC Oscar (within the means of

transport "cargo ships" under the sea freight mode), a Boeing 747
freighter (within the means of transport "aircraft" under air cargo), a set
of locomotives (within the means of transport "trains" under rail
transport), or a fleet of Volvo FH16 trucks (within the means of transport
"trucks" under road transport).

Relationship Flow:

●  Top-Level (Transportation Mode): Establishes the broad method of

transportation (for example, sea freight).

●  Middle-Level (Means of Transport): Categorizes types of vehicles suitable for

that method (for example, cargo ships for sea freight).

●  Bottom-Level (Vehicle Resource): Details actual vehicles or fleets operating
within the means of transport category (for example, MSC Oscar for cargo
ships).

In  summary,  the  transportation  mode  defines  the  method,  the  means  of  transport
categorizes  the  vehicle  types  under  this  method,  and  the  vehicle  resource  specifies
the actual vehicles that provide the transportation services. Each layer depends on the
other to effectively facilitate the movement of goods.

21


Lesson  2
## Transportation Management

-  Explaining  Organizational  Structures

for

## Objective

After completing this lesson, you will be able to conceptualize the organizational
structures relevant for transportation management.

## Organizational Structure

## Organizational Structure: Generic View

An organizational structure represents the framework of a company. Each department
within  the  company  has  designated  organizational  units,  which  serve  as  distinct
segments responsible for specific functions and operations.

This  structured  approach  ensures  that  data  and  transactions  are  efficiently
segregated  and  managed  within  the  appropriate  channels.  For  instance,  the  sales
department  may  have  its  own  set  of  sales  organizations,  distribution  channels,  and
sales groups. In contrast, the logistics department might have unique shipping points
and  transportation  planning  units.  Companies  can  streamline  operations,  maintain
accountability, and optimize resource allocation by assigning dedicated organizational
units to each department.

Organizational  structures  play  a  crucial role in restricting user access and are one of
the basic requirements for defining authorization and role setups. Before loading data
and  executing  transactions in SAP S/4HANA, it is necessary to define the company’s
entities within the system.

Organizational Structure: SAP Transportation Management Specific View

22


In Transportation Management (TM), the organizational structure can be based on the
structure  of  a  connected  SAP  system.  Still,  creating  organizational  units  that  do not
exist in SAP is also possible.

SAP S/4HANA TM maps its organizational units with S/4 organizational units through
the  "BSG  Org.  Unit"  field.  Plant  and  shipping  points  are  created  as  locations  in  SAP
S/4HANA TM.

●  Corporate Organization: This organizational unit is optional and serves as a

single entry point into the organization's structure in TM. It represents the group
organization.

●  Company Organization: This organizational unit corresponds to the company
code. It establishes the local currency and represents the company's legal
entity.

●  Sales Organization: The sales organization structures and manages the sale of
logistics services and their execution. Multiple sales organizations can be
assigned to a company organization. The sales organization is relevant in the
following documents:

○  Forwarding orders
○  Forwarding quotations
○  Forwarding settlements

●  Purchase Organization and Purchasing Group: The purchasing organization
procures materials and services. The following documents are generally
associated with the purchasing organization:

○  Freight orders
○  Freight bookings
○  Freight settlements

23


●  Planning and Execution Organization: The planning and execution organization
is responsible for planning and/or executing shipments. These organizational
units are used in the following documents and objects:

○  Resources
○  Freight orders

●  Forwarding House: In some Logistics Service Provider (LSP) scenarios, it is

essential for the same organizational unit to perform multiple tasks, such as
selling transportation services to customers and purchasing transportation
services from vendors. A generic organizational unit of the type "Forwarding
House" can be defined in these scenarios. A forwarding house can handle
sales, purchasing, and planning/execution activities, allowing it to be assigned
to various documents and objects related to these functions.

24


Lesson  3  -  Using  Materials  Master  Data  for  Transportation
Management

## Objective

After completing this lesson, you will be able to explain the role of material master data
in the context of transportation management.

Material Master

## Material Master

Material  master  data,  also  known  as  product  master  data,  classifies,  identifies,  and
characterizes materials and services. The material master serves as a comprehensive
repository  of  information  regarding  materials  transported,  manufactured,  sold,  or
purchased by an organization.

Each  material  is  assigned  a  unique  identifier  and  created  as  a  single  record  in  the
system.  This  centralized  data  is  accessible  to  all  relevant  departments,  including
purchasing,  inventory  management,  MRP,  transportation,  and  warehousing,  reducing
inconsistencies and eliminating redundancy.

## Material Types

When  creating  a  new  material  master  record,  selecting  a  material  type  to which the
material will be assigned is essential. Materials sharing similar properties are grouped
under  the  same  material  type.  Examples  of  material  types  include  raw  materials,

25


semifinished  products,  and  finished  products.  In  SAP  S/4HANA,  various  predefined
material  types  are  available,  and  additional  material  types  can  be  configured  in
Customizing  to  meet  specific  business  requirements.  Some  SAP-provided  material
types include the following:

●  Finished goods FERT: A finished good is a material manufactured by some
form of production from items, such as raw materials. A finished good isn’t
purchased and thus doesn’t contain any purchasing information. However, a
finished good is sold and thus does contain sales information.

●  Trading goods HAWA: Trading goods are generally materials purchased from
suppliers and sold. This material type only allows purchasing and sales
information because no internal operations are carried out on these materials.
An example of a trading good can be found at many computer manufacturers
that sell their own manufactured goods (computers) but also may sell printers
and routers. Trading goods are not manufactured by the company but bought
from other manufacturers and sold alongside their own computers instead.

●  Services (DIEN): Services are internally or externally supplied by a supplier.

Service material master records don’t have storage information.

●  Packaging material VERP: material Unlike material type LEER (empties), the
packaging material type is for materials that are packaged but are free of
charge to the customer in the delivery process. Although free, the packaging
material may still have value, and a physical inventory is recorded.

●  Returnable packaging LEIH: Reusable packaging material is used to pack
finished goods for the customer. When the finished good is unpacked, the
customer must return the returnable packaging material to the supplier.

The material type is a critical element within the material master record, as it performs
several  key  control  functions.  It  determines  how  the  material  number  is  assigned,
whether  internally  or  by  the  user,  and whether it's numeric, alphanumeric, or within a
specific  number  range.  Additionally,  it  controls  which  screens  are  displayed  and  in
what  order  during  the  material  master  maintenance  process.  It  influences  the  field
selection  control  by  dictating  which  fields  are  mandatory,  optional,  hidden,  or
display-only in the material master record.

## Material Views

The  material  master  data  is  categorized  into  multiple  views,  each  aligned  with  a
is  accessible  and
particular  user  department,  ensuring  relevant
manageable  by  the  respective  teams.  This  structure  allows  customized  access  to
data pertinent to various operations such as purchasing, inventory management, MRP,
work  scheduling,  and  warehousing.  Each  view  consolidates  data  specific  to  the
department's  activities,  simplifying
the  process  and  ensuring  efficient  data
management.

information

26


Transportation  Related  Attributes:  Within  the  material  master,  the  Sales  view  (Sales:
General/Plant) specifies the following transport-relevant attributes:

●  Base Unit of Measure (BUoM): The Base Unit of Measure field is the UoM that

represents the lowest level for the material.

●  Alternative units of measure (AUoMs): A base unit can have alternative units of

measure (AUoMs) that are multiples of the BUoM (that is, grams and
kilograms).

●  Dimensions: Gross Weight, Net Weight, and Volume Fields. The dimensions of
a material may be relevant to shipping companies when deciding how to pack
and ship material. The dimensions may determine how the material is to be
shipped.

●  Transportation Group: A categorization criterion that classifies materials based

on similar processing conditions, facilitating efficient logistics and
transportation planning. Examples include palletized goods, refrigerated goods,
and dairy products.

●  Material Freight Group: The Material Freight Group field is used to group

materials to determine their freight classification and, ultimately, their freight
code. In Transportation Management, the material freight group is transferred
from the sales order item to the product item of the freight unit.

27


## Dangerous Goods

Dangerous goods, also known as hazardous materials or hazmat, are solids, liquids, or
gases that pose risks to people, living organisms, property, or the environment. These
substances  are  subject  to  chemical  safety  laws  that  vary  between  countries.  They
radioactive,  flammable,  explosive,  corrosive,  oxidizing,  asphyxiating,
include
biohazardous,  toxic,  pathogenic,  or  allergenic  materials. Physical conditions, such as
compressed  gases,  liquids,  or  hot  materials,  are  also  included.  This category covers
goods  containing  such  materials  or  chemicals  or  those  exhibiting  hazardous
characteristics under specific circumstances.

The  dangerous  goods  functions  in  Transportation  Management  (TM)  enable  you  to
transport dangerous goods (DG) in compliance with international regulations.

●  Dangerous Goods Based on Product Compliance
●  Dangerous Good Processing based on PS&S

## Note

One can choose between DG processing based on PS&S and DG processing based on
product compliance. Since these two solutions are mutually exclusive, only one can be
activated at a time.

Dangerous  goods  experts  classify  products  according  to  the  applicable  dangerous
goods  regulations.  This  information  is  used  by  a  compliance check carried out in all
relevant business documents in the value chain, such as intracompany stock transfer

28


orders,  sales  orders,  outbound  deliveries,  and freight orders. The check verifies if the
transport of this product is allowed. If not, the check blocks the business document.

## Dangerous Goods Indicator Profile

The  DG  indicator  profile  field  is  defined  in  SAP  Environment,  Health,  and  Safety
Management  (SAP  EHS  Management).  A  dangerous  goods  indicator  profile  can  be
selected  if  the  material  being  added  is  relevant  for  dangerous  goods  and  any
documentation accompanying that type of material.

●  Environmentally Relevant
●  Highly Viscous and In Bulk/Liquids

29


Lesson  4
## Management

-  Using  Business  Partner  for  Transportation

## Objective

After completing this lesson, you will be able to explain the role of business partners in
the context of transportation management

## Business Partner

Introduction to Business Partners

Business Partner Definition:

A  business  partner  refers  to  any  entity  with  which  a  company  has  established  a
business  relationship.  Business  partners  can  be  classified
into  three  primary
categories:  person,  organization,  and  group.  An  organization  may  represent  a
company,  a  department  within  a  company,  or  an  association.  A  group  could include
entities such as a shared living arrangement, a married couple, or an executive board.

In  SAP  S/4HANA,  the  master  data  of  customers  and  vendors  is  handled  through
business  partner  master  data.  This  approach  allows  for  centralized  maintenance  of
customer and vendor master data, which were previously managed separately in SAP
ERP.  This  centralized  maintenance  enables  business  partners  to  be  assigned  to
multiple company codes.

30


When  a  new  business  partner  is  created  in  the  system, they are automatically given
the  role  of  General  Business  Partner.  The  general  data  for  a  business  partner  is
defined once, after which specific business partner roles (BP roles) are assigned. Each
business  partner  role  reflects  a  particular  business  context  in  which  the  business
partner can participate.

To  create  a  customer,  create  a  generic  business  partner,  and  assign  the  roles  of
"Customer" and "FI Customer" to the business partner. Assigning these roles activates
the  relevant  additional  fields:  the  "FI  Customer"  role  makes  sales  and  organizational
fields available, while the "Customer" role enables all sales-relevant fields.

Similarly,  to  create  a  vendor,  create  a  generic  business  partner,  and  then  assign  the
roles of "Vendor" and "FI Vendor" to the business partner.

The following business partner roles are most commonly used in TM:

31


●  Business Partner General (000000
●  Customer (FLCU01)
●  FI Customer (FLCU00)
●  Vendor (FLVN01 )
●  FI Vendor (FLVN00)
●  Carrier (CRM010)
●  Global Trade Services: Customs Office (SLLCOF )
●  Driver (TM0001)
●  Organizational Unit (BUP004)
●  Contact Person (BUP001)
●  Prospect (BUP002)
●  Employee (BUP003)
●

Internet User (BUP005)

The "Customer" (FLCU01) role enables the maintenance of data and fields at the sales
organization  level.  In  contrast,  the  "Vendor"  (FLVN01)  and  "Carrier"  (CRM010)  roles
permit  the  maintenance  of  data  and  fields  at  the  purchasing  organization  level.
Moreover,  the  "FI  Customer"  (FLCU001)  and  "FI Vendor" (FLVN00) roles support data
and field maintenance at the company code level.

The  "Carrier"  (CRM010)  role  encompasses  the  data  of  the  "Vendor"  (FLVN01) role. It
includes additional Transportation Management (TM)-specific information such as the
Regulated  Agent  Code,  IATA  Agent Code, CASS Account, SCAC Codes, Airline Codes,
Service Level Codes, and Carrier Service Codes.

The  "Driver"  (TM0001)  role  contains  driver-specific  data,  including  home  location,
qualifications, shift sequences, validity periods, and absences.

Assigning partner functions in the SAP system defines the specific roles that business
partners assume during various processes. A partner function represents a particular

32


responsibility a business partner can take on. For instance, one customer might order
products  (partner  function:  Sold-to  party),  while  another  might  receive  the  material
(partner  function:  Ship-to  party).  A  single  partner  can  have  multiple  functions.  For
example,  if  all  partner  functions  within  the  customer  category  are  assigned  to  one
business partner, that customer would serve as the sold-to party, ship-to party, payer,
and bill-to party.

## Business Partner Determination

Business  partner  determination  enables  the  system  to  automatically  identify  and
assign  business  partners  to  various  business  document  types.  This  feature
streamlines  entering  business  partners  into  business  documents,  reducing  manual
errors and enhancing efficiency.

A  partner  determination  profile
is  created  to  determine  business  partners
automatically.  This  profile  must  be  assigned  to  the  specific  business  document  for
which  it  will  be  used.  Different  profiles  can be assigned to various types of business
documents.  The  following  business  document  types  can  have  specific  profiles
assigned:

●  Freight orders
●  Freight bookings
●  Freight settlement documents
●  Freight agreement RFQs
●  Freight agreements
●
## Internal agreements

Watch the simulation Review Carrier Information to learn more about business partner
master data.

33


Unit 3 - Developing Transportation Networks

Lesson 1 - Understanding Transportation Networks

## Objective

After completing this lesson, you will be able to understand the use of transportation
networks in SAP TM.

Transcript for video:

“In  this  unit  we  will  cover  Transportation  Network  Master  Data  in  SAP
Transportation  Management.  You  will  gain an understanding of the master data
relevant  to  SAP  TM,  including  locations,  transportation  zones,  transportation
lanes,  and  default  routes.  These  elements  work  together  to  ensure  seamless
logistics  operations.  By  the  end  of  this  unit,  you  will  be  able  to:  Understand the
use  of  transportation  networks  in  SAP  TM.  Create and manage locations within
your  transportation  network.  Aggregate  multiple  locations  into  transportation
zones  to  streamline  data  management.  Establish  transportation  lanes  to  define
the  relationships and direct approachability between locations. Configure default
routes  to  optimize  freight  movement.  A  transportation  network  in  SAP  TM  is  a
pivotal component that defines how different locations and transshipment points
are  connected.  This  network  supports  end-to-end  logistics  scenarios,  ensuring
that  goods  can  move  efficiently  from  origin  to  destination.  The  fundamental
building  blocks  of  your  transportation  network  are  locations,  which  represent
physical  sites  such  as  warehouses,  distribution  centers,  and  customer  delivery
addresses.  Transportation  zones  help  in  grouping  multiple  locations,  making  it
easier  to  manage  and  propagate  certain  properties  across all locations within a
zone.  This  reduces  the  volume  of  master  data  you  need  to  maintain.
Transportation lanes represent the direct routes between locations or zones. They
control  how  goods  can  be  transported  from  one  point  to  another, ensuring that
you  have  a  clear  and  efficient  path  for  your  logistics  operations.  Finally,  we  will
cover  the  creation  of  default  routes.  These  routes  are  predefined  paths  that
optimize  the  movement of freight, ensuring timely and cost-effective delivery. By
the  end  of  this  unit,  you  will  be  equipped  with  the  foundational  knowledge  and
skills  to  begin  configuring and managing transportation networks effectively. So,
let's  get  started  and  dive  into  transportation  networks  in  SAP  Transportation
Management! Enjoy learning with SAP!”

34


Transportation Network

## Transportation Network Overview

In  this  lesson,  the  focus  is  on  understanding  the  master  data  relevant  to  SAP
Transportation  Management  (SAP  TM)  in  the  context  of  the  transportation network.
SAP TM uses various types of master data, including locations, transportation zones,
transportation
locations,  to  support  comprehensive
end-to-end logistics scenarios for manufacturers and distributors.

lanes,  and  transshipment

The  transportation  network  is  a  pivotal  component  in  Transportation  Management
(TM) that defines the direct reachability between various locations and transshipment
locations,  providing  a  comprehensive  framework for freight movement. This network
lays out clear connections between locations, allowing for the efficient transportation
of goods from one point to another.

Transshipment locations play a critical role in this network as well. They are designed
to facilitate the reloading of goods from one transportation option to another, ensuring
the  continuity  of  the  freight  movement  process.  These  locations  are  essential  for
intermodal  transport,  where  multiple  transportation  methods,  such  as  road,  rail,  and
sea, are employed to move goods efficiently.

Advanced planning algorithms use transportation network definition to determine the
most  efficient  path  through  the  network,  selecting  the best routes and assigning the
most suitable carriers for given transportation demands. This optimized path ensures
timely  delivery  and  minimizes  costs  by  considering  various  factors,  including  freight
and forwarding agreements that contain rates based on trade lanes.

Key Terms

35


To  fully  utilize  the  transportation  network,  several  critical  components  must  be
understood and defined:

●  Locations: Locations constitute the basic building blocks of the network,

marking the start and end points of transportation routes.

●  Transportation Zones: These zones group multiple locations. By aggregating
locations into zones, it becomes easier to plan and optimize transportation
across broader areas.

●  Transportation Lanes: These lanes define the direct routes between locations

and zones.

●  Transshipment Locations: Transshipment locations ensure that goods can be

seamlessly transferred from one mode of transportation to another.
●  Default Routes: These routes define specific paths from the source to the

destination through a sequence of stops.

●  Schedules Schedules outline recurring routes with fixed dates and times along

a predefined sequence of locations.

●  Trade Lanes: These lanes offer an additional dimension to the transportation
network by defining business relationships with customers and carriers.

Utilizing Transportation Network Master Data

## Transportation Network Cockpit

Transportation  Network  Cockpit  can  be  used  to display the following master data of
the transportation network on a map:

●  Locations

36


●  Transportation zones
●  Transportation lanes
●  Trade lanes
●  Schedules
●  Default routes
●  Connections
●  Business partner networks

## Path Finder

Path  finder  searches  for  legs  within  the  transportation  network,  considering  the
following elements:

●  Locations
●  Transshipment locations
●  Transportation lanes
●  Schedules
●  Transportation zones

37


By using this function, it becomes straightforward to determine whether a connection
exists  between  two  locations,  which  means  verifying  the  correct  configuration  of
master  data.  This  function is available in the Transportation Network Cockpit and on
the user interface for transportation proposals. The Path Finder result is displayed on
the geographical map in both cases.

38


Lesson 2 - Creating Locations

## Objective

After completing this lesson, you will be able to create locations.

## Locations

A location is a logical or physical place where products or resources are managed on
a quantity basis.

●  Products or freight units are transported between various locations.
●  Each product or freight unit has a source and destination location.
●  Products or freight units may transit through multiple locations along their

journey.

●  Products or freight units are loaded and unloaded at these locations.

transshipment

In  transportation  processes,  a  source  location,  a  destination  location,  and  any
necessary
the
transportation process. A name identifies each location. To define a location, its name
and type must be specified. In Transportation Management (TM), the location type is
used  to  categorize  locations.  Location  types  are  not  used  to  control  business
processes but serve as a reference. TM provides standard location types, such as:

locations  must  be  designated

to  complete

●  Production plant (1001)
●  Distribution center (1002)
●  Shipping point (1003)
●  Transportation zone (1005)

39


●  Business Partner (1021)
●  Terminal (1030)
●  Store (1040)
●  Port (1100)
●  Airport (1110)
●  Railway station (1120)
●  Container freight station (1130)
●  Hub (1140)
●  Gateway (1150)
●  Container yard (1160)
●  Warehouse (1170)
●  Carrier warehouse (1180)
●  Loading point (1200)

## One time Locations

Any locations that do not need to be stored permanently in the system as master data
can  be  stored  as  one-time  locations.  A  one-time  location  is  stored  as  a  transient
master  data object in the system. These are used in business processes that require
the  input  of  locations  not  defined  as  master  data  objects,  such  as  the  creation  of
forwarding orders. The system creates one-time locations based on one-time address
details.

A  one-time  location  is  characterized  by  the  organization’s  name,  address  data,
communication  data,  or  a  combination.  A  note  can  be  created  for  each  one-time
location, with only one note per location and language.

## Locations of Business Partners

A  business  partner  can  have  multiple  standard  and  delivery  addresses  and  requires
one valid standard address at any time. In TM, multiple locations can be assigned to a
single  business  partner.  A  corresponding  location  can  be  created  for  each  relevant
address.  The  address  number  of  the  location  matches  that  of  the  business partner.
When TM receives a sales document or outbound delivery, it uses the address data to
determine the correct location, taking into account the validity dates of the address.

Creating Locations

Creating Locations

40


## Creating Locations Using a Report

Report  /SAPAPO/CREATE_LOCATION  can  be  utilized  to  create  new  locations  for
plants,  shipping  points,  and  business  partners.  This  is  particularly  helpful  for
managing many entities requiring locations.

To execute the report, selections are made from plants, shipping points, and business
partners.  Options  are  available  to  create  locations  solely  for  the  entities'  standard
addresses or for the standard and delivery addresses. The report identifies all selected
entities that lack a location, and the system performs the following actions:

●  Creates a location using the entity's existing address.
●  Calculates geocodes.
●  Creates a transportation zone location if necessary.
●  Updates the location to zone assignment.

Creating Locations from Business Documents:

When  creating  or updating documents relevant to Transportation Management (TM),
the  system  verifies  the  presence  of  all  necessary  locations  representing  plants,
shipping points, and business partners. If a required location has not been created, the
system  will  automatically  generate  it. Locations can be created on demand from the
following TM-relevant business document categories:

●  SD Documents: Sales Order (SO)

41


●  MM Documents: Purchase Order (PO), Stock Transfer Order (STO)
●  Deliveries: Outbound Deliveries, Inbound Deliveries

## Creating Locations out of Business Partner Master

For  business partners, the system can be configured to create locations immediately
upon  the  creation  and  saving  of  a  business  partner.  This  configuration  requires  the
implementation  of  the  business  add-in  (BAdI)  /SAPAPO/LOC_CREATE,  allowing  the
specification of conditions for creating or updating a location when a business partner
is  saved. Once a location is created, the system automatically triggers updates when
changes are made to the business partner's address.

42


Lesson 3 - Creating Transportation Zones

## Objective

After completing this lesson, you will be able to create transportation zones.

Transportation Zones

## Definition

A  transportation  zone  is  a  business  object  that  aggregates  multiple  locations.  This
business object is used to group locations into transportation zones. The system can
propagate  certain  properties assigned to a transportation zone to all locations within
it, minimizing the volume of master data maintained.

Transportation  zones  can  encompass  individual  locations,  one-time  locations,  and
subzones  within  other  zones.  For  instance,  all  locations  supplied  by  the  same
warehouse  (whether  individual  locations  or  transportation zones) can be aggregated
into a single transportation zone.

As  transportation  zones  are  not  physical  entities,  they  do  not  possess  addresses.
Nevertheless,  geographical  coordinates  can  be  assigned  to  them.  SAP  TM  provides
two  options  for  calculating  these  coordinates.  The  system  can  either  estimate  the
center  point  of  the  zone  based  on  the  coordinates  of  all  included  locations  after
defining  the  locations,  regions,  or  postal  codes,  or  the  geographical coordinates can
be manually entered into SAP TM.

43


Each transportation zone is uniquely identified by a specific name. The combination of
the  name  and  type  distinctly  defines  and  specifies  every  transportation  zone.  In
Transportation Management (TM), the types of transportation zones include:

●  Direct zone: Locations are assigned to the transportation zone directly by

entering the name of each location.

●  Postal code zone: Locations are assigned to the transportation zone by
specifying a valid postal code range for a particular country or region.

●  Region zone: Locations are assigned to the transportation zone by specifying a
country/region and a specific region. If only a country/region is entered, the
system automatically includes all regions within that country/region.

●  Mixed zone: A mixed zone combines any other zone types.

Transportation Zone Hierarchy

44


A  hierarchy  that  can  be  defined  for  organizing  transportation  zones.  This  object
structures  transportation  zones  hierarchically  by  allowing  the  assignment  of  one
transportation  zone  to  another.  Therefore,  all  locations  in  a  subordinate  zone
automatically  become  part  of  the  superordinate  zone. Transportation zones within a
hierarchy  inherit  properties  from  their  superior  zone.  The  following  conditions  apply
when defining a transportation zone hierarchy:

●  A transportation zone cannot be assigned to itself.
●  A transportation zone cannot be assigned to another zone if it already contains

that zone.

The zone hierarchy can be leveraged in the following scenarios:

●  The VSR optimizer considers the transportation zone hierarchy during the

optimization run.

●  The lane determination function considers the transportation zone hierarchy

when identifying a specific transportation lane.

●  The transshipment location determination function uses the transportation

zone hierarchy to identify all valid transshipment locations for a given location.

Transshipment Location

## Definition

A  transshipment location is used for unloading goods from one vehicle resource and
loading them onto another during transportation.

45


Transshipment locations are applicable when different means of transport or carriers
are  required
in  the  transportation  process.  These  locations  are  also  used  to
consolidate or deconsolidate goods for transport.

A  transshipment  location  is  defined  by  assigning  it  to  another  location  or  a
transportation  zone.  When  assigned  to  a  transportation  zone,  it  can  serve  as  a
transshipment location for all locations within that zone.

46


Lesson 4 - Creating Transportation Lanes

## Objective

After completing this lesson, you will be able to create transportation lanes.

## Transportation Lanes

Definition: Transportation lanes represent the relationship between two locations, two
transportation  zones,  or  a  combination  of  locations  and  transportation  zones  that
expresses  the  direct  approachability  of  the  locations,  or  all  locations,  within  the
transportation zones for a specific means of transport (MTr). Carriers can be assigned
to the transportation lane as needed.

Using  transportation  zones  as  the  source,  destination,  or  both  considerably  reduces
the  number  of  transportation  lanes  to  maintain.  A  transportation  lane  points  only  in
one direction. To model the reverse direction, you must create another transportation
lane.

The  transportation  lane controls how goods can be transported from one location to
another.

Transportation lanes play a key role in SAP TM. They control:

●  Which location can forward goods to another location
●  Which means of transport can be used to do so
●  Which carrier can supply a vehicle for the means of transport

47


Creating Transportation Lanes

## Transportation
lanes  represent  a  direct  connection  between  two  locations  or
transportation zones to transport freight from one location to another. They're typically
maintained on transportation zone level and are defined by:

●  Source and Destination
●  Direction
●  Available MTr

 Optional: Carrier per MTr

Maintenance:

Individual

●
●  Mass maintenance

Transport Lane Creation:

●  Tr.Lane: Enter source and destination locations or zones to create a

transportation lane.
Intra-Zone Lane/Loc. Transp. Lane:

●

○  Define an intrazone lane by specifying a transportation zone.
○  Define a location transportation lane by specifying a particular location.

●  Mass Maint. (Create): Create multiple transportation lanes by copying an

existing one.

Means  of  Transport  Assignment:  Means  of  transport  facilitates  the  movement  of
goods  between  the  locations  or  zones  of  a  transportation  lane.  Attributes  for  the
means  of  transport,  which  apply  to  transportation  activities between the source and
destination of the goods, including transportation duration, distance, and costs, must
be specified.

48


Carrier  Assignment:  A  carrier  provides  services  along  a  transportation  lane  for  a
specific means of transport. Carriers are assigned to the transportation lane by linking
them to the means of transport. Once a carrier is assigned to the means of transport,
attributes specific to this combination, such as transportation costs, priority, share of
business, or capacity for transportation allocation, can be specified.

## Note

The creation of a transportation lane requires the assignment of at least one means of
transport.  Also,  to  enable  automatic  carrier  selection,  carriers  must  be  assigned  to
means of transport.

## Trade Lane

A  trade  lane  can  have  a  mode  of  transport  and  means  of  transport.  The  trade  lane
defines  a  transportation  direction  characterized  by  the  orientation,  source,  and
destination. Possible orientations are inbound, outbound, from, to, within, and along.

A  trade  lane  is  an  abstract  representation  of  transport  classification.  A  trade  lane
instance does not represent a connection between any transportation network nodes
(zone/location,  and  so  on).
It's  a  context-independent  classification  of  any
transportation-related activities.

Examples of trade lanes include:

●  All transports from Hamburg to New York
●  All transports within Germany
●  All transports that leave Bavaria

## Note

It's important to note that trade lanes do not replace transportation lanes.

There's no direct link between a trade lane and a transportation lane.

Trade Lane Hierarchy and Overlap:

Trade  lanes  can  form  hierarchical  structures,  where  more  generic  trade  lanes
encompass more specific trade lanes. For instance: "Within Germany Using Means of
Transport Truck" includes:

●

●

"Along the Way from Frankfurt to Hamburg with Means of Transport
## Refrigerated Truck"
"Within Bavaria with Means of Transport Truck for Liquids"

49


Trade lanes may also overlap. Examples include:

●
●

"From Germany Using Airplane"
"Within Europe Using Airplane"

Hierarchy Components:

Trade lane hierarchies can include:

●  Transportation Zone Hierarchies:

For example, "from Germany" includes "from Bavaria," which further includes
"from Plant_Munchen."

●  Hierarchical Relationships between Means of Transport:

 For instance, "Within Germany Using Means of Transport Truck" includes
"Within Germany Using Means of Transport Refrigerated Truck."

●  Means of Transport/Transportation Mode Relationships:

For example, "Within Germany Using Transportation Mode Street" includes
"Within Germany Using Means of Transport Refrigerated Truck."

## Note

In  previous  releases,  trade  lanes  were  created  from  and  associated  with  other
business objects such as Business Shares, Allocations, and Freight Agreements. Now,
trade  lanes  can  be  used  as  master  data  objects,  allowing  for  creation,  copying,  and
reuse  according  to  business  needs.  A  worklist  is  available  to  view  all  trade  lanes,
including information such as a where-used list.

Distance and Duration Determination (DDD)

A  location  is  a  distinct  point  on  the  Earth's  surface,  defined  by  the  geographical
coordinates of longitude, latitude, and altitude. These coordinates can be derived from
the  address  data,  which  provides  an  alternate  description  of  the  same  point.  An
address  may  include  elements  such  as  country,  region,  postal  code,  city,  district,
street, house number, and additional fields.

Geographical  coordinates  are  displayed  in  degrees,  minutes,  and seconds within the
Geographical  Data  section  of  the  Location  user  interface  (UI)  and  can  be  manually
overridden.  The  precision  field  specifies  the  granularity  of  the geo-coding result, and
the  accuracy  of  these  geo-coordinates  depends  on  the  quality  of  the  address  data
provided.

50


The Transportation Lane master data object links two locations and records distance
and  duration  information  for  each  assigned  means  of  transport.  By  default,  this
information  is  determined  through  calculating  the  straight-line  distance,  accounting
for  the  Earth's  curvature,  and  applying  a  deviation  factor  specific  to  the  means  of
transport.  If  this  abstraction  level  does  not  meet  the  accuracy  requirements  of
business  processes,  more  precise distances and durations can be obtained using an
external Geographic Information System (GIS).

The following two options are available for calculating DDD:

●  Shortest Distance Calculation: The system calculates the shortest possible

route (line of flight) between locations.

●  Precise Distance Calculation: By leveraging a third-party geographic

information system (GIS), the system calculates the exact distance based on
the means of transport.

51


Lesson 5 - Creating Default Routes and Schedules

## Objective

After completing this lesson, you will be able to create default routes and schedules.

Default Routes and Schedules

Default Routes

## Definition

A  default  route  outlines  a  sequence  of  locations  from  a  specified  origin  to  a
predetermined  destination,  encompassing  individual  locations  or  entire  zones.  The
default  route  acts  as  a  blueprint  for  transporting  goods  from  the  origin  to  the
destination, directing the flow through the transportation network.

Default  routes  can predefine the sequence of transshipment locations for intermodal
transports.  Truck  and  trailer  scenarios  involving  dynamic  recoupling  can  also
predefine the sequence of coupling and uncoupling locations for the trailer unit.

Transportation  mode,  carrier,  schedule,  and  other  relevant  details  for  each  default
route can be specified for each transportation stage.

Schedules

Definition

52


The  Schedule  function  defines  a  sequence  of  stops,  such  as  ports,  airports,  or
gateways, valid for a specific timeframe. Ships, trucks, or airplanes can move goods at
recurring intervals along the entire sequence or any part of it. The movement of goods
depends  on  transit  durations  between  stops,  cut-off  times,  and  the length of stay at
each stop.

Schedules  can  be  maintained  for  each  business  partner  or  carrier,  and  different
loading and unloading points, such as ports and airports, can be identified.

Gateway  Schedules:  Gateway  schedules  are  for  transportation  hubs,  such  as
container  freight  stations  (CFS),  where  freight is consolidated and deconsolidated. A
reference  to  a  carrier  schedule  can  be  entered  for  each  transportation  stage,
transferring departure rules and voyages.

●  Road Gateway Schedule: Defines a direct connection between two gateways

via road.

●  Sailing Schedule: Defines a connection between two ocean gateways, including

information about ports of loading and discharge.

●  Master Flight Schedule: Defines a connection between airport gateways and
can be used to map connecting flights by referencing several carrier flight
schedules.

Carrier  Schedules:  Carrier  schedules  define  sequences  of  stops  that  do  not
necessarily  involve  gateways.  By  specifying  departure  rules,  departures  can  be
generated automatically while considering transit durations and cut-off times.

●  Ocean Carrier Schedule: Defines a standard sequence of stops a ship serves.

53


●  Carrier Flight Schedule: Defines a standard sequence of stops for a plane or

connection flights with multiple stages and various carriers.

●  Road Schedule: Defines a standard sequence of stops a truck serves.

54


Unit 4 - Managing Transportation Capacities,
Conditions and Incompatibilities

Lesson 1 - Defining Transportation Capacities

## Objective

After completing this lesson, you will be able to create transportation capacities.

## Vehicle Resources

## Resources in Transportation Management

Resources are crucial for planning and execution within SAP Transportation
Management (TM). Resource data impacts order date planning by accounting for
working times and available resource capacities. With bookings, resources provide the
necessary capacity for executing transportation activities on freight units, including
transportation, loading, and unloading.

Types of Resources

## Vehicle Resource

Used for transporting goods around the
transportation network.

## Handling Resource

Provides the capacity needed to load and
unload goods.

## Calendar Resource

Specifies operating hours for a location,
determining when goods can be dropped off
or picked up.

Transportation Unit
## Resource

Represents containers in TM.

## Vehicle Resources

Vehicles serve as dynamic resources for transporting goods between locations,
including trucks, railcars, planes, and ships. Each vehicle resource represents a unit
load, such as a trailer, container, or railcar with a specific capacity. The capacity of a
vehicle can be defined using various dimensions and units of measurement, such as:

55


●  Mass: For example, a trailer capacity of 40,000 pounds.
●  Volume: For example, a container capacity of 2,200 cubic feet.
●  Quantity: For example, a capacity to hold 24 pallets.

Calendar and Handling Resource

## Handling Resources

Definition: A handling resource is an installation or device used to manage goods at a
specific location. It provides the capability to load goods onto or unload goods from
vehicle resources.

Handling resources are crucial for efficient transportation order processing at various
locations. Examples: Doors, Forklifts. Handling resources include several parameters
that help define their capabilities and limitations:

●  Resource Template: Used for copying predefined resource specifications.
●  Capacity Profile: This profile details the resource's capacity based on

time-dependent shifts. For example, a dock may have 50 doors available in the
morning and evening and reduced capacity during the day.

●  Availability: Specifies the periods when the handling resource is operational.
●  Downtimes: Denotes periods when the resource is unavailable.
●  Qualifications: Defines any specific skills or certifications required to operate

the handling resource.

●  Attached Equipment: Lists any additional equipment associated with the

resource.

●  Grouping Attributes: These are used for grouping similar handling resources.

## Calendar Resources

Definition: A calendar resource is assigned to a calendar and optionally to a shift
schedule. It's primarily used for scheduling the processing time for goods receipt and
goods issue at a location. Calendar resources are employed to define the operating
times for locations.

56


Calendar resources include several parameters to capture their operational schedule:

●  Shifts: Defines the working periods within the calendar, such as morning,

afternoon, and evening shifts.

●  Downtimes: Specifies periods when the calendar resource is unavailable for

operation, helping to manage maintenance and operational breaks.

57


Lesson 2 - Using Conditions and Incompatibilities

## Objective

After completing this lesson, you will be able to use conditions and incompatibilities to
model business requirements.

Introducing Conditions and Incompatibilities Using BRFplus

Transcript for video:

“In  this  lesson  we  will  focus  on  BRFplus  and  how  we  manage  incompatibilities  during
transportation planning. First, let's talk about BRFplus, or Business Rule Framework Plus.
This is a powerful tool used for defining, managing, and executing business rules within
Transportation  Management  for  SAPS/4HANA.  It's  user-friendly  and  supports  various
features  like  simulation,  tracing,  transport,  and  XML  export  and  import.  Essentially,
BRFplus helps streamline decision-making processes by allowing us to model and reuse
rules  efficiently.  Some  typical  use  cases  for  BRFplus  include  validating  data,  matching
responsibilities,  suitable  products  and  locations,  and  calculating  costs,  overhead  and
risks.  In  transportation  management,  we  might  use  BRFplus  to  determine  the
appropriate organizational unit based on the source location specified in a freight order.
One of the key methods in BRFplus is the Decision Table. This table maps input values to
output  values.  The  system  processes  this  table  sequentially  from  top  to  bottom,  and
when it finds a match, it uses the corresponding output values. This is particularly useful
in  scenarios  like  determining organizational units or calculating costs. Now, let's switch
gears and talk about incompatibilities in transportation planning. Incompatibilities define
the  compatibility  of  planning  data  that  must  be  considered.  For  instance,  freight  units
with different Incoterms shouldn't be transported together, and refrigerated goods must
only  be  transported  using  appropriate  means  of  transport like refrigerated trucks. Here
are  some  more examples: A container of a certain equipment type can't be transported
on a particular resource due to size constraints. A truck requiring side unloading can't be
unloaded at a location that doesn't offer the appropriate facilities. And, a driver must not
transport dangerous goods if they lack the necessary license. In SAP TM, conditions are
used  for  various  purposes  like  filtering  freight  units,  determining  freight  unit  building
rules,  managing  incompatibilities,  and  setting rate tables and agreements. In summary,
BRFplus  and  the  management  of  incompatibilities  are  crucial  components  in  SAP
Transportation  Management.  They  help  ensure  that  our  transportation  planning  is
efficient,  compliant, and optimized for various constraints and requirements. I hope you

58


found  this  summary  helpful  and  invite  you  to  explore  this  topic  in  more  detail  in  the
lesson below! Enjoy learning with SAP!”

## Conditions

Business Rules Framework plus (BRFplus)

The  Business  Rule  Framework  Plus  (BRFplus)  is  a  sophisticated  tool  for  defining,
managing,  and  executing  business  rules.  Its  user-friendly  interface  facilitates  the
modeling  and  reuse  of  rules,  thereby  streamlining  decision-making  processes.
BRFplus  supports  various  features,  including  simulation,  tracing,  transport,  and XML
export and import.

Typical Use Cases for BRFplus:

●  Validation of data and detection of invalid data and states
●  Matching responsibilities, suitable products, and locations
●  Calculation of costs, overhead, and risks

Conditions Using the Business Rules Framework Plus (BRFplus)

The  Business  Rules  Framework  plus  (BRFplus)  is  a  comprehensive,  rules-based
engine  widely  used  within  SAP  Transportation  Management  (TM)  for  managing
complex  business  rules.  This  framework  significantly reduces the need for extensive
development,  customization,  and  configuration  by  providing  a  streamlined  approach
to  handling  SAP  TM  conditions.  These  conditions  act  as  filters  for  automated
decision-making processes, mapping input values to corresponding output values.

59


In  SAP  TM,  conditions  are  logical  evaluations  applied  to  various  objects,  such  as
transportation  requirements  or  freight  units.  These  evaluations  assess  whether
specific  criteria  are  met,  guiding  whether  particular  actions  or  decisions  should  be
executed during transportation planning. By automating the validation of compatibility
between  different  elements  and  ensuring  adherence  to  business  rules,  conditions
enhance efficiency and minimize manual intervention.

## Note

The conditions in the transportation management system (TMS) are not based on the
condition  technique  used  in  SAP  ERP.  In  the  transportation  management  system
(TMS),  the  condition  is  a  proposition  on  which  another proposition depends or what
data  will  be  fetched  based  on  the  filters  and  selection.  Objects  like  tables,  access
sequences,  or  procedures  are  not  available.  Instead,  SAP  provided  predefined
conditions, and one can assign or set selection filters to fetch or determine a specific
value.

Key applications of conditions include:

●  Filtering freight units
●  Determining freight unit building rules (FUB Rules)
●  Managing incompatibilities
●  Establishing sales organizations
●  Setting rate tables and agreements with charge calculation rules

## Origin of Condition: Condition Area

There are various types of conditions used for different areas, such as document type
loading  and  unloading  durations,
determination,  order
incompatibilities, printing, approvals, tolerances, and custom rules.

type  determination,

## Origin of Condition: Condition Type

The  condition  type  defines  the  area  in  which  the  system  takes  the  condition  into
account. SAP delivers several condition types in the standard system. A condition type
defines possible input values as well as the output of conditions of that type. So-called
data access definitions define the input values.

The Origin of Condition slide explains how conditions in SAP TM are evaluated based
on  input  data,  processed through an origin source (Direct Business Object Access or
BRF+ Decision Table or Expression), and result in a specific output or action.

60


## Input Values

Input  Values:  The  input  values  available  each  time  depend  on  the  chosen  condition
type. The input values are defined by data access definitions, which specify what data
exists and where to get it when evaluating the Condition.

## Output Values

Output  Values:  The output values are determined by the condition type. For example,
the org unit results from the org unit determination.

Three Key Methods for Condition Origin Determination

## Direct Business Object Access

This  approach  retrieves  values  directly  from  predefined  data  definitions  without
additional evaluation. The system adopts the input values of a condition as its output
values.

61


## BRFplus Decision Table

This  method  evaluates  input  values  against  a  decision  table maintained through the
condition user interface. It's commonly used in Transportation Management (TM). The
system  translates  input  values  into  corresponding  output  values  based  on  the
mappings defined in the decision table.

## BRFplus Expression

This  method  evaluates  input  values  against  a  decision  table maintained through the
condition  user  interface.  It  is  commonly  used  in  Transportation  Management  (TM).
The  system  translates  input  values  into  corresponding  output  values  based  on  the
mappings defined in the decision table.

Watch the simulation Review Conditions to learn how to display a condition by filtering
for the appropriate condition type.

## BRFplus Decision Table

A  condition  maps  input  values  to  output  values.  This  condition  can  be  a  single
Boolean  value  used  to  select  a  business  object  or  can  consist  of  multiple  output
values derived from input values through a decision-making process.

The  system  creates  a  BRFplus  decision  table using these input and output values. It
then processes this table sequentially from top to bottom during determination. When
the system encounters a row where the input values match the current input values, it
copies the associated output values and processes them in the calling area.

slide

exemplifies

type
The
this
"/SCMTMS/TOR_ORGUNIT."  Utilizing  a  BRFplus  decision
the  system
automatically  generates  this  table  by  employing  standard  data  access  definitions
configured  in  Customizing.  Users  can  then  input  specific  values  into  the  table  to

demonstrating

condition

table,

the

by

62


determine  organizational  units  based  on  the  source  location  specified  in  the  freight
order.

Incompatibilities

## Incompatibilities

Incompatibilities  define  the  compatibility  of  planning  data  that  must  be  considered
during transportation planning. For instance:

●  Freight units with different Incoterms should not be transported together.
●  A container of a specific equipment type cannot be transported on a particular

resource due to size constraints.

●  Refrigerated goods must only be transported using appropriate means of

transport, such as refrigerated trucks.

●  A specific means of transport cannot be unloaded at a location lacking a

suitable loading ramp.

●  A truck requiring side unloading cannot be unloaded at a location that does not

offer the appropriate facilities for side unloading.

●  A driver must not transport dangerous goods or operate a truck without a

license.

During  transportation  planning,  companies  establish  guidelines  for  shipping.  For
example,  products  requiring  refrigerated  containers  cannot  be  shipped  with  frozen
freight  units.  When  planning  transportation  shipments,  companies  define  rules  for
consolidating  loads  into  a  single  freight  order.  Various  factors,  aside  from  capacity,
influence  how  freight  orders  are  constructed.  In  SAP  Transportation  Management
(TM),  these  rules  are  known  as  incompatibilities.  This  data  defines  the  parameters
controlling when to consolidate loads and when not.

As  illustrated,  a  company  may  have  diverse  products  to  ship,  each  with  specific
storage  temperature  requirements that dictate whether items can be consolidated. A
test  determines  the  optimal  shipping  temperature  for  each  product.  According  to  a
rule,  items  classified  as  chilled  cannot  be  shipped  with  items  classified  as frozen to
prevent damage or spoilage.

Incompatibilities  are  used  with  conditions  to  influence  outcomes  in  SAP  TM  during
freight  unit  building,  transportation  planning,  transportation proposal generation, and
carrier selection. They are crucial for defining load-building requirements. For instance,
freight  units  with  different  Incoterms  must  not  be  transported together. Refrigerated
goods  must  be  transported  using  appropriate  means.  Certain  means  of  transport
cannot be loaded at specific locations due to the absence of suitable loading ramps.

63


When creating an incompatibility definition, you must specify a validity area and type.
The  example  in  the  image  above  shows  Products  (FUs)  and  Vehicle  Resources.
Incompatibilities can be defined in the following way depending on the transportation
planning requirements:

Defining Incompatibilities Between Two Attributes:

You can establish incompatibilities between any two attributes of two business object
nodes. This involves setting up two conditions and specifying the relevant results. Two
business objects will be incompatible if the condition results match these criteria.

Defining Incompatibilities for Identical Values:

Alternatively,  you  can  define  incompatibilities  for  instances  of  the  same  business
object  by  entering  a  single  condition  and  selecting  the  "Ident. Values Only" (Identical
Values  Only)  checkbox.  This  approach
to  define
incompatibilities  between  two  freight  units.  The  two  instances  will  be  deemed
incompatible if their attribute values differ.

for  example,

is  utilized,

## Incompatibility Definition

When  creating  an  incompatibility  definition,  you  must  specify  a  validity  area,  which
consists of an incompatibility area and an incompatibility type.

Incompatibility Areas:

Incompatibility  areas  determine  where  an  incompatibility  can  be  applied.  There  are
four incompatibility areas within SAP Transportation Management (TM):

64


●  Automatic Planning (formerly known as Vehicle Scheduling and Routing (VSR))
●  Manual Planning
●  Freight Unit Building
●  Carrier Selection
●  Delivery Proposals

Incompatibility Area

01 - Automatic
Planning and
Manual Planning

04 – Freight Unit
Building

05 – Carrier
Selection

07 – Delivery
## Proposal

01  – Freight Unit –
## Unit
## Freight
(Vehicle Level)

52
Transportation
Request Item

–

Carrier

81
–
–Transportation
Order

–

51
Transportation
Request  Header  –
Transportation
Request Root

–

52
Transportation
## Request
Transportation
Request Item

Item  –

53  – Freight Unit –
## Freight Unit

02  – Freight Unit –
## Unit
## Freight
(Compartment
Level)

03  – Freight Unit –
Freight
## Unit
(Means  of  Transp.
Combination)

04  – Freight Unit –
Vehicle Resource

05  –  Freight  Unit
Transshipment
## Location

06  – Freight Unit –
## Vehicle
Compartment

–

07
## Vehicle
Resource – Vehicle
Resource

–

–

82
Transportation
## Order
Transportation
Order

65


–

08
Resource
Location
Level)

Vehicle
–
(Stay

–

Vehicle
–

09
Resource
## Location
(Loading/Unloadin
g Level)

10  –  Vehicle  MTR
–
Combination
## Location

11  – Freight Unit –
Freight Booking

(…)

Incompatibility Types:

SAP provides predefined incompatibility types that specify the objects to which a rule
applies. Examples include:

●  Freight Unit to Freight Unit
●  Freight Unit to Vehicle
●  Freight Unit to Transshipment Location
●  Carrier to Transportation Order

In  addition  to  defining  the validity area, the incompatibility definition can also specify
how the rule is enforced during manual and automatic planning. This includes setting
the reaction to the incompatibility, such as whether it's ignored, a warning is issued if
ignored, or it must not be violated.

Incompatibilities  can  be  defined  between  two  attributes  of  two  business  objects  by
setting up two conditions and specifying relevant results. Two business objects will be
incompatible if the condition results match the criteria.

66


Setting  the Identical Values Only check box in the incompatibility definition allows for
an  incompatibility  to be defined between two instances of the same business object,
for  example,  two  freight  units.  In  this  case,  a  single  condition  is  defined  as
incompatibility.  The  two  business object instances are then only incompatible if their
values differ.

## Incompatibility Settings

Incompatibility  settings  can  be  maintained  in  planning  profiles,  carrier  selection
settings,  delivery  profiles,  and  the  freight  unit  building  rule.  Transportation  planning
profiles specify when the system allows incompatibilities to be violated during manual
planning,  VSR  optimization,  or  background  processing.  Incompatibility  settings  are
assigned  within  these  profiles.  The
incompatibility  settings  combine  several
definitions  that  can  apply  to  a  planning  run.  Only  incompatibilities  for  the  same
incompatibility area can be combined.

Watch  the  simulation Review Incompatibility to learn how to display Incompatibilities
and review the essential settings needed.

67


Lesson 3 - Scenario Builder

## Objective

After completing this lesson, you will be able to use the Scenario Builder.

## Scenario Builder Overview

The  Scenario  Builder  is  a  powerful  tool  designed  to  facilitate  the  rapid  creation  of
master  and  transactional  data  for  testing,  demonstrations,  and  training  purposes.  It
enables  users  to  efficiently  develop  and  execute  scenarios  within  the  SAP
Transportation Management (TM) system.

Administrators can use Scenario Builder to create comprehensive scenario templates,
encompassing  all  necessary  data,  including  system  objects  and  customization
settings, required for running a scenario in TM.

Testers can easily browse available scenario templates and generate their own copies
of the scenario data within the system. This approach eliminates uncertainties related
to the required data and significantly reduces the time spent on test preparation.

68


## Key Features

●  Comprehensive Data Inclusion: Administrators can incorporate both

customization data and various system objects into a scenario template,
ensuring that all elements needed for scenario execution are included.
●  Reusable Templates: Once created, scenario templates can be reused
indefinitely by an unlimited number of users, offering efficiency and
consistency across multiple test cases.

●  Personalized Data Copies: Scenario Builder allows each user to generate
individual copies of the scenario data, enabling multiple users to work
concurrently with the same data without conflicts. This feature is particularly
beneficial for group testing, workshops, and collaborative exercises.
●  Template Portability: Scenario templates can be exported and shared for

collaboration or local editing, providing flexibility for teams working across
different environments.

Note:  The  Scenario  Builder  is  intended  specifically  for  demonstration,  testing,  and
proof of concept purposes. It's not designed for use in live operational environments.

## Personal Prefixes

Personal  prefixes allow users of a scenario template to generate scenario data using
unique  identifiers  such  as  their  initials  or  user ID. This ensures that each user works
with  their  own  version of the scenario data, allowing for simultaneous usage without
interference.

●  With Sample Data: The system generates sample data, and you will receive

Excel files containing this data format.

●  Without Sample Data: The system provides empty Excel files for you to

populate with your own data.

## Objects Supported by Scenario Builder

The  following  master  data  and  configuration  objects  are  supported  by  the  scenario
builder:

●  Master Data:

○  Locations
○  Transportation Zones
○  Transshipment Location Assignments
○  Schedules
○  Transportation Lanes
○  Vehicle Resources

69


○  Default Routes
○  Business Partners (TM-specific data only)
○  Materials (TM-specific data only)

●  Configuration Objects:

○  Freight Unit Building Rules
○  Selection Profiles
○  Scheduling Settings
○  Optimizer Settings
○  Planning Profiles
○  Capacity Selection Settings

●  Customizing (BC Sets)
●  Report Variants

70


Unit 5 - Creating Transportation Requirements

Lesson 1 - Defining Transportation Relevance

## Objective

After completing this lesson, you will be able to explain transportation relevance and how
sales and purchasing trigger transportation processes.

Introducing Transportation Requirements

Transcript for video:

“In  this  unit  we  will  look  at  how  SAP  Transportation  Management  uses  specialized
planning  units  such  as  'transportation  requirements'  and  'freight  units'  to  represent
physical  items,  such  as  the  line  items  in  a sales order, in a transportation context. The
transportation  management  process  is  initiated  by  the  presence  of  a  transportation
requirement.  Transportation  requirements  in  SAP  TM are triggered by documents such
as  sales  orders,  purchase  orders,  and deliveries. When these documents contain items
that  need  to  be  transported,  SAP  S/4HANA  automatically  creates  corresponding
transportation requirements which flow into TM for creating freight units and managing
the  transportation  effectively.  Once  an  order  with  transportation  relevant  items  has
triggered  the  creation  of  a  transportation  requirement, freight units need to be created.
Freight  units  are  the  backbone  of  effective  shipping.  They  represent  sets  of  goods
transported  together.  Creating  balanced  freight  units  is  key—neither  too  large  nor  too
small,  ensuring  optimal  transportation  planning.  Freight  unit  building  rules  dictate how
these  units  are  grouped,  ensuring  efficiency  and  adherence  to  business  rules.
Transportation  and  warehouse  management  are  tightly  related  business  processes.
Where  transportation  management  uses  freight  units,  warehouse  management  uses
handling  units.  A  handling  unit  is  a  logistic  unit  consisting  of  packaging  materials  and
goods.  These  handling  units  need  to  be  packed,  and  SAP  TM  supports  various
packaging  methodologies  to  optimize logistics operations. Unified Package Building (or
UPB)  integrates  different  packaging  methodologies  within  SAP.  Whether  during  freight
unit  building,  consolidation,  or  capacity  document  creation,  UPB  optimizes  your  entire
logistics process by considering specific constraints and minimizing the total number of
packages.  Different  industries  have  varied  logistics  needs.  For  example,  eCommerce
companies  need  to  blend  various  products  for  efficient  shipping.  Food  distribution
companies need to manage bulk quantities with varied temperature requirements, while
automotive  companies  need  to  handle  specialized  parts.  Effective  freight and package

71


unit  management  in  SAP  TM  ensures  that  your  logistics  operations  run  smoothly,
irrespective  of  the  industry.  Please  continue  this  unit  to  learn  how  transportation
relevance  is  defined,  how  freight  units  are  built,  and  how  packaging  information  is
managed. Enjoy learning with SAP!”

Transportation Requirements Overview

Transportation Requirements in SAP TM: An Overview

is  the  essential  event  that

Creating  a  transportation  requirement
initiates  a
transportation  management  process.  This  requirement  serves  as  the  starting  point
and  is  triggered  by  transportation-relevant items in an initiating document, such as a
sales order or a delivery. Creating a transportation requirement in SAP Transportation
Management (SAP TM) varies based on the deployment option. Below are the primary
starting points for transportation requirements depending on the selected deployment
model:

Documents Triggering the Creation of Transportation Requirement

The  following  documents  can  trigger  the  creation  of  a transportation requirement in
SAP  TM,  either  through  internal  integration  with  the  SAP  TM  component  or  via
external SAP TM system integration:

●  Sales orders
●  Customer returns
●  Purchase orders
●  Stock transport orders
●  Return stock transport orders
●  Sales scheduling agreements
●  Materials management scheduling agreements
●  Outbound deliveries
●
## Inbound deliveries

Transportation Requirement Creation in Different SAP TM Deployment Models

72


1.  Logistics Service Providers (LSPs or 3PLs): Transportation requirements can be
received in various ways by logistics service providers or third-party logistics
providers (3PLs). Forwarding orders are typically manually created using the
SAP TM User Interface (UI) or Electronic Data Interchange (EDI) with an
external system. The forwarding orders and forwarding quotations are
considered transportation requirements within an LSP process.

2.  Side-by-Side Deployment / External TM System Integration: SAP TM is installed

as a separate system in side-by-side deployment scenarios. The original
document driving the transportation demand does not reside in SAP TM itself,
necessitating the replication of this information. This replication process can
create either order-based or delivery-based transportation requirements.
Order-based requirements may originate from documents such as sales
orders, purchase orders, stock transport orders (STOs), or scheduling
agreements. On the other hand, delivery-based requirements stem from
outbound or inbound deliveries. Integration between SAP TM and the source
system, whether SAP ERP or SAP S/4HANA, is facilitated using XML messages
via SAP Process Integration or point-to-point communication.

3.  Embedded Deployment / Internal TM Component Integration: In an embedded

deployment scenario, the need for a separate document to represent a
transportation requirement is eliminated, as the original object causing the
transportation demand already exists in the SAP S/4HANA system. These
original objects may include sales orders, purchase orders, stock transport
orders, scheduling agreements, or delivery documents such as inbound and
outbound deliveries. Here, the freight unit acts as the initial object for SAP TM,
created directly from the original object instigating the transportation demand.
This embedded scenario is the primary focus of this overview training.

This  structured  approach  to  understanding  transportation  requirements  in  SAP  TM
ensures  clarity  in  transportation  management's  deployment  and  operational  facets,
facilitating efficient logistics and supply chain execution.

73


Integrating Transportation Relevant Documents with SAP TM

The documents that are created in sales and distribution (SD), materials management
(MM)  and  logistics  execution  (LE)  can  be  integrated  into  TM.  The  following settings
have to be configured to integrate sales orders, scheduling agreements and deliveries.

●  Activate Integration of Documents via Control Key
●  Create Logistics Integration Profile
●  Assign Logistics Integration Profile to Document Type

Route Determination with Incoterms

## Incoterm and Incoterm Locations

Definition:  Incoterms,  short  for  international  commercial  terms,  are  standardized
international  rules  that  define  the  commonly  used  terms  in  international  trade. They
outline  the  terms  of  sale  and  the  transfer  of  risks  associated  with  importing  and
exporting  merchandise.  The  International  Chamber  of  Commerce  (ICC)  publishes
incoterms and periodically releases new versions.

Incoterm

Description

EXW

Ex Works

FAS

Free Alongside Ship

FOB

Free On Board

CFR

Cost and Freight

CIF

Cost, Insurance, and Freight

CPT

Carriage Paid To

DES

Delivered Ex Ship

DEQ

Delivered Ex Quay

DAF

Delivered At Frontier

DDP

Delivered Duty Paid

74


DDU

Delivered Duty Unpaid

FCA

Free Carrier

CIP

Carriage  and  Insurance  Paid
To

Incoterms  are  intended  to  communicate  the  tasks,  costs,  and  risks  associated  with
transporting  and  delivering  goods. They define a contractual agreement between the
shipper  and  consignee  to  determine  who  is  responsible  for  which  stage  of  the
transport and where and when the responsibilities of each partner start and end.

Some  of  these  incoterms  require  a  location  where  tasks,  costs,  and  risks  are
transferred  from  the  shipper  to  the  consignee.  The  incoterm  location  is  where  the
goods are physically handed over and where the responsibilities for the goods change.
The  incoterm  location  is  a  master  data  location  in  SAP  TM  and  can  be  used  for
routing purposes.

Regarding  delivery  integration  with  SAP TM, the Incoterms (Part 2) field can be used
to define the incoterm location. You can map incoterms (Part 2) to an SAP TM master
data  location  with  the  app  Assign  Location  to  Incoterm  Location.  You  can  use  this
information for stage building.

## Stage Building Based on Incoterms

In  SAP  TM,  you  can  build  stages  based  on  the  incoterm  location.  The  Incoterm
Location  Stage  Building  field  in  the  logistics  integration  profile  customizing  defines

75


how  stages  are  built  based  on  source,  incoterm,  and  destination  locations.  The
system  uses  the  incoterm  location  for  stage  building  if  the  incoterm  has  set  the
Incoterm  Location  flag  (a  flag  that  indicates  that  you  must  enter  a location with this
incoterm).  If  no incoterm is specified, the system does not use the incoterm location
for  stage  building,  and  the  system  creates  only  one  stage  from  the  source  to  the
destination  location.  If  an  incoterm  is  specified  but  this  incoterm  has  not  set  the
Incoterm  Location  flag,  the  system  does  not  use  the  incoterm  location  for  stage
building.  Instead,  the  system  creates  only  one  stage  from  the  source  to  the
destination location. The following stage-building rules are possible:

1.  Initial Value – Two Active Stages: This setting is default. Two planning-relevant

stages are created.

2.  01 Source Location to Incoterm Location – Type 1: One stage from the source

to the incoterm location is created.

3.  02 Source Location to Incoterm Location – Type 2: Two stages are created. An
active stage from the source location to the incoterm location. An additional
stage from the incoterm location to the destination location which is not
relevant for planning

4.  03 Incoterm Location to Destination – Type 1: One stage from the incoterm

location to the destination. This is relevant, for example, for the consignee who
plans only the route from the incoterm location to the goods receipt location.

5.  04 Incoterm Location to Destination – Type 2: Two stages are created—an
active stage from the incoterm location to the destination location and an
additional stage that is not relevant for planning from the source location to the
incoterm location.

6.  05 Two Active Stages: Two planning-relevant stages are created.

76


Lesson 2 - Defining Freight Units

## Objective

After completing this lesson, you will be able to analyze freight units, their attributes and
their use.

## Freight Units

Freight Units Defined

A freight unit is:

●  A set of goods intended to be transported together from origin to destination
●  The smallest unit of freight used in transportation planning
●  A unit used to merge items (transportation requirements) derived from
originating documents (SO, PO, STO, and so on) for the planning of
transportation.

The granularity of freight units required for transportation planning varies significantly
depending on the business scenario. The system can split and merge product
quantities of the requirements when creating freight units, depending on the applied
freight unit building rules. The creation of freight units subsequently impacts planning.
Larger freight units simplify planning activities in VSR optimization, while smaller
freight units theoretically offer higher optimization potential but complicate planning

77


due to their increased number. To achieve optimal planning results, it's recommended
to strike a balance.

Examples:

1.  Food Distribution: Consider a truck with a capacity of 20 tons intended for

transporting 20 tons of flour in 1 kg packages. Creating a single freight unit of
20 tons or 20,000 freight units of 1 kg each is not advisable for the
aforementioned reasons. A balanced approach should be sought.

2.  E-commerce Shipments: An e-commerce company needs to transport a mix of
electronics, clothing, and home goods. Instead of creating separate freight
units for every single item (resulting in a very high number of freight units), or
combining everything into one large freight unit (making it cumbersome to
handle), it would be more efficient to create freight units grouped by product
category or delivery destination.

3.  Automotive Industry: A manufacturer needs to deliver a variety of auto parts to
different assembly plants. Splitting the freight units based on part types (for
example, engine components, body parts, electrical systems) rather than by
individual items or as a single freight unit for all parts combined can enhance
the efficiency of both transportation and handling at the destination.

4.  Pharmaceutical Logistics: A pharmaceutical company requires the

transportation of both temperature-sensitive and non-sensitive medications.
Creating separate freight units for temperature-sensitive items (such as
vaccines) and non-sensitive items (like vitamins) ensures proper handling and
compliance with regulations without overwhelming the planning system with
too many small units.

Freight units are fundamental to efficient and effective transportation planning and
execution. Understanding the importance of freight unit granularity and appropriately
configuring systems to manage freight units can significantly streamline logistics
operations, balance planning complexities, and optimize transportation resources. By
ensuring accuracy in defining and managing freight units, businesses can enhance
operational efficiency, minimize costs, and meet specific transportation requirements
effectively.

Initiating Freight Unit Building

78


Freight unit building can be either automatically triggered or manually executed.
Typically, if freight units should not consolidate items from different predecessor
documents, which is the most common scenario, automatic freight unit building can
be activated. Freight units are created immediately upon the creation or saving of their
predecessor documents. Additionally, the creation of freight units can be triggered by
background reports. Specifically, report /SCMTMS/TRQ_PREP_PLNG_BATCH can be
utilized to create freight units in a side-by-side deployment scenario. In such cases,
freight units are generated based on the /SCMTMS/TRQ object. For an embedded
deployment scenario, report /SCMTMS/SUBSEQUENT_FUB_LOGINT should be used.

Manual options are also available for initiating the creation of freight units. This can be
done via worklists for any of the possible predecessor documents (Order-based
Transportation Requirements (OTR), Delivery-based Transportation Requirements
(DTR)).

## Freight Unit Building Rules

Understanding Freight Unit Building Rules

79


Freight Unit Building Rules (FUB rules) are essential for determining how freight units
are created and managed within a transportation management system. These rules
ensure that goods are efficiently grouped for transport, optimizing load capacities and
meeting specific business requirements.

There are three options for determining freight unit building rules:

1.  Condition Check in Logistics Integration Profile: The system first reviews the
condition defined in the logistics integration profile. The system transitions to
the next option if no condition is specified or fails to produce a result.
2.  Freight Unit Building Rule in Logistics Integration Profile: Next, the system

verifies if a freight unit building rule is specified within the logistics integration
profile. The system proceeds to the final option if no such rule is maintained.

3.  Application of Standard Settings: The system defaults to applying standard

settings in the absence of a condition or a specified freight unit building rule.

Freight units are automatically generated when transportation relevance is identified
for a transportation demand, such as a sales order, purchase order, delivery, OTR, or
DTR.

The system considers any existing freight units associated with the transportation
demand. It creates freight units based on the defined split quantity and the status of
the item split checkbox. These parameters are considered when multiple freight units
need to be created. Custom strategies can be employed to create freight units to meet
specific requirements. SAP provides the default strategy, FUB_AUTO, for freight unit
building.

## Defining a Freight Unit Building Rule

Within the freight unit building rule, defining the critical quantity is essential. This
parameter specifies the primary unit of measure that enables a line item on a

80


transport requirement to be split into multiple freight units. Additionally, several
planning quantities, such as weight and volume, can be defined. Each planning
quantity is considered for capacity checks during transportation planning and is
copied to the freight unit.

The split quantities set the maximum capacity of a freight unit. The system calculates
freight units as multiples of the rounding quantity. If the Item Split Allowed option is
selected, the system will split the item during freight unit building if it exceeds the split
quantity. The process controller strategy allows customized strategies to define how
freight units are created according to specific requirements. When an equipment type
is maintained in the freight unit building rule, the capacity of the equipment is
considered during freight unit building, and the items consolidated into one freight unit
are loaded accordingly.

If necessary, companies can specify that freight units should be split under certain
constraints. For example, the maximum capacity of a freight unit is defined using the
split quantity. If transporting five tons of cement but limited to batches of 500 kg, the
split quantity is set to 500 kg, and the system generates 10 freight units.

Based on the definition of freight units, all items within a freight order are transported
together from their source to their final destination. However, in multimodal scenarios,
different planners may be involved in scheduling various transport stages. To
accommodate this, stage information can be added to the freight unit, providing a
degree of independence when scheduling each stage.

The freight unit building rule also considers incompatibilities. For example, certain
products cannot be transported together due to differing temperature requirements;
ice cream and ketchup must be shipped separately. Consequently, these items must
be kept apart during freight unit building, even though other items within the same
transportation requirement, such as chocolate ice cream and strawberry ice cream,
can be consolidated into a single freight unit. To address such planning constraints,
incompatibility settings can be defined and assigned within the freight unit building
rule.

81


Lesson 3 - Managing Packaging Information

## Objective

After completing this lesson, you will be able to recognize the role of package building
and normalized quantities.

## Understanding Packaging Materials

Packaging materials are essential for enclosing or securing the goods to be
transported. The packaging materials and the goods constitute the handling unit,
ensuring that items are safely transported.

Maintaining material master data for each packaging material is essential. When
creating material master records for packaging materials, selecting the correct
material type, such as VERP (specifically designated for packaging materials), is
essential.

## Types of Packaging Materials

The material destined for transport can be packaged into or onto various packaging
materials. These materials can also serve as load carriers, such as pallets. Some of
the most commonly used packaging materials include:

●  Crates: Used for sturdy and rigid protection of goods.
●  Boxes: Versatile and widely used for various items.
●  Containers: Ideal for large quantities and bulk transportation.
●  Wire Baskets: Suitable for smaller, loose items that need to be grouped.
●  Pallets: Fundamental load carriers facilitating stacking and handling.

82


## Handling Units: Managing Packaging and Goods Together

A handling unit (HU) is a logistic unit consisting of packaging materials and goods
(materials). With Handling Unit Management, the system tracks the entire HU rather
than individual materials. The HU serves as the fundamental unit for both material and
information flow. A business transaction involving an HU triggers corresponding
background transactions for the materials and packaging materials it contains,
consolidating several individual material movements into a single entry.

Handling units can be used and transferred to partners throughout the supply chain.
Each handling unit is assigned a single identification number that uniquely identifies it
across various processes. In cross-system logistics chains, this identification number
often must be unique worldwide. A Serial Shipping Container Code (SSCC) number
can be assigned to each handling unit to facilitate this.

## Packaging Solutions

In SAP S/4HANA, different application domains have developed distinct
methodologies for determining a packaging hierarchy, each tailored to specific

83


logistics and management needs. Understanding these approaches is crucial for
optimizing packaging and logistics operations within the system.

1.  Packing Instructions in Logistics General: Packing instructions are utilized

within the Logistics module to define how items should be packed. Packing
instructions serve as a template for the creation of a handling unit. The packing
instructions define the materials and packaging materials to be packed in a
handling unit. This enables you to reproduce specific customer packaging
requirements in the system. You can also automate the packing process by
proposing a handling unit based on packing instructions.

2.  Packaging Specifications in Extended Warehouse Management (SAP EWM):
Packaging specifications have evolved from packing instructions and are
employed within the Extended Warehouse Management module. Packaging
specifications are part of the master data. The packaging specification defines
all the necessary packing levels for a product in order, for example, to put away
or transport the product. For a product, a packaging specification mainly
describes in which quantities you can pack the product into which packaging
materials in which sequence.

3.  Package Building in SAP Transportation Management: Package building is a
feature offered in the SAP Transportation Management (TM) module and is
utilized within EWM during the cartonization process.

●  Given a set of product quantities, package building determines a

packaging hierarchy to minimize the number of top-level packages

●  Different Package Building modes:

○  Rule-based package building: layer-based and volume-based
○  Detailed mixed package building: optimizer (PBO) defines x/y/z

positions and orientations

●  Features: separator material, deep packaging hierarchy, incompatibilities
between products, orientation profile, loading sequence per package,
and so on. Considers material master, package building profile, and so
on

84


While packing instructions and packaging specifications are rule-based and share
many similarities, package building offers a very different approach, which isn’t based
on rules but considers constraints and offers an optimization algorithm to build
optimized mixed pallets. If a product is always handled and shipped in a certain
packaging structure, this could be modeled very well by packing instructions or
packaging specifications. Suppose the business involves transporting mixed pallets
containing multiple products for one or even multiple customers. Package building
may be more appropriate in that case as it minimizes the required mixed pallets.

As the integration of these components is driven by recent developments,
consolidating/unifying the use of the three packing solutions has become a priority.

## Unified Package Building

UPB aims to unify the previously diverse packaging methodologies across various
applications in TM, EWM, and LO. Historically, these applications utilized different
packing engines based on different packing rules and persistence approaches for

85


resulting packaging hierarchies. Given the similar underlying requirements for
packaging materials, SAP's long-term strategy is to align and unify these approaches.

The UPB component is a reusable component that allows the packaging of products
by using one of the available packing engines (defined as UPB engines) and applying
configurable rules (defined as UPB rules). Currently, the supported UPB engines are
based on:

●  Packing Instructions (PI)
●  Package Builder (PB)
●  Packaging Specifications (PS)

The UPB is currently supported by processes in the following applications:

●  Transportation Management (TM)
●  Extended Warehouse Management (EWM)
●  Logistics General (LO)

During package-building, the system groups products into packages based on specific
constraints while minimizing the total number of packages. The system can also
determine each product item's exact position and orientation within the package.
These constraints can be defined for various product combinations, business
partners, equipment, and locations. When multiple constraints apply, the system
always uses the most specific constraint.

In a nutshell, the UPB component receives input items corresponding to materials. It
applies UPB rules (and returns a packaging hierarchy as a result).

Unified Package Building (UPB) in SAP S/4HANA represents a strategic advancement
in packaging methodologies, integrating various approaches into a unified framework.
UPB enhances efficiency, consistency, and optimization in packaging operations by
aligning packaging processes across different applications.

## Unified Package Building in the Planning Process

In Transportation Management (TM), the system can create packages through several
methods, ensuring flexibility and efficiency in packaging operations. These methods
include:

●  Early in the Process: During Freight Unit Building. Unified package building can

be utilized during the creation of freight units. This method is ideal when
packages will be built on a per-freight-unit basis.

86


●  Late in the Process: Based on Capacity Documents. Unified package building
can be activated for capacity documents, such as road freight orders. This
approach is particularly effective when building customer-mixed packages.

87


Unit 6 - Planning Transportation

Lesson 1 - Defining Transportation Documents

## Objective

After completing this lesson, you will be able to recognize the purpose of various
documents related to the planning and execution of transportation processes.

Overview of Transportation Planning in SAP TM

Transcript for video:

“Transportation planning is at the heart of logistics management, and SAP TM provides
powerful tools to optimize this complex task. Over the next several lessons, we'll explore
how  to  effectively  use  these  tools  to  streamline  your  transportation  operations.  We'll
begin  by  examining  the  various  transportation  documents  used  in  SAP  TM,  including
freight  units,  freight  orders,  and  freight  bookings.  You'll  learn  how  these  documents
interact and flow through the system. In particular, this unit focuses on freight orders and
freight  bookings  which  are  central  to  SAP  Transportation  Management.  These
documents  consolidate  freight  units  and  drive  carrier  selection,  tendering,  and
settlement  processes.  They  contain  essential  information  for  transportation  execution,
including  planning  details,  cargo  data,  and  execution  status.  Next,  we'll  look  at  the
different  planning  processes  available,  from  manual  to  fully  automated  options.  We'll
cover  how to set up selection and planning profiles to tailor the system to your specific
needs.  A  key  focus  will  be  on  the  Transportation  Cockpit  -  the  central  workspace  for
planners.  You'll  see  how  to  use  this  powerful  interface  for  both  interactive  and
automated  planning  tasks.  We'll  also  explore  advanced  features  like  the  Vehicle
Scheduling  and  Routing  Optimizer,  which  can  dramatically  improve  efficiency  and  cut
costs. You'll learn how to generate optimized load plans and create freight bookings for
various  transportation  modes.  Finally,  we'll  cover  the  important  processes  of  carrier
selection and tendering, which allow you to choose the best transportation providers for
each  shipment.  By  the  end  of  this  unit,  you'll  have  a  comprehensive  understanding  of
how  to  leverage  SAP  TM  for  world-class  transportation planning. Let's get started with
our first lesson where we define some of the most essential transportation documents.
Enjoy learning with SAP!”

## Role of Transportation Documents

Various  business  documents  are  relevant  to  planning,  each  with  a  specific  purpose.
These  documents  can  be  interconnected  in  different ways. Demand documents and
their  stages  can  be  assigned  to  capacity  documents.  A  capacity  document  can
represent the transportation of one or multiple demand stages.

88


While  a  freight  unit  solely  represents  demand,  freight  orders  and  freight  bookings
represent pure capacities. Other documents can represent both demand and capacity
simultaneously.  Pure  capacity  documents  and  consignment  orders  can  be
subcontracted  and  serve  as  the  foundation  for  execution.  They  may  be  created  in
advance  to  reserve  a  carrier's  transportation  capacity,  which  is  then  utilized  by
assigning demands.

The documents serve the following business purposes:

Business Documents in Transportation Management

## Freight unit

A  freight  unit  represents  an  original  transportation
demand  abstracting  from  forwarding  orders,  sales
orders,  or  deliveries.  It  is  transported  through  the
complete  transportation  chain  without  splitting  it  on
any  transportation  stage.  As  a  pure  demand,  a  freight
unit consumes capacity.

Package unit  Package units represent demands transported together

in the same packages, such as a pallet or carton.

Consignment
order

Container
unit

A  consignment  order  represents  a  logical  grouping  of
one  or  multiple transportation demands with the same
source and destination but doesn’t represent a physical
capacity. A consignment order contains only one stage.
It’s  frequently  used  in communication, for example, for
advanced  shipping  notifications  between  shippers and
consignees,  and  can  also  be  used  for  subcontracting
represent  a
purposes.  Consignment  orders  can
demand but also consolidate demands.

A  container  unit  models  a  demand  transported  in  a
container.  You  can  consolidate  multiple  freight  units
into a container unit, which serves as capacity from the
freight  unit  viewpoint.  However,  the  container  also
represents  a  demand  that  must  be  transported.  In  an
intermodal  container  transportation  scenario  from
China  to  Europe,  the  container  may  have  three  stages
assigned  to  a  road  freight order for pre-carriage within

89


China,  an  ocean  freight  booking  for  the  main  carriage,
and  another  road  freight  order  for  the  subsequent
carriage in Europe.

## Trailer unit

A trailer unit represents trailer demands transported by
a road freight order.

## Railcar unit

Railcar  units  represent  railcar demands transported by
a rail freight order.

Road  freight
order

Road  freight  orders  represent  transportation  by  road,
which  can  be  subcontracted  or  executed  by  a
company’s  fleet.  This  document  represents  a  capacity
and  can  consolidate  multiple  demands  that  consume
the capacity.

freight

Rail
order

In  the  same  way as the road freight order, a rail freight
order represents transportation by rail.

Ocean freight
booking

Ocean freight bookings represent subcontracted ocean
transports.  Like
freight  orders,  a  booking  can
consolidate multiple demands.

freight

## Air
booking

Like  ocean  freight  bookings,  an  air  freight  booking
represents transportation by airplane.

Assigning Transportation Documents: (Descriptions refer to the figure above)

Box  1: Freight units and package units can be assigned to the documents in boxes 2
and 3.

Box  2:  Consignment  orders  and  container  units  can  be  assigned  to  all  capacity
documents  shown  in  box  3,  except  for  consignment  orders,  which  don’t  allow  the
assignment to ocean and air freight bookings.

90


Box  3:  While  trailer  and  railcar  units  are  specifically  dedicated  to  the  corresponding
road  or  rail  mode  of  transport,  container  units  frequently  involve  multiple  modes  of
transport  across  the  different  container  unit  stages.  Freight  orders  represent  the
movements of trucks and locomotives. Freight bookings represent the subcontracted
movement of vessels or airplanes. Without freight orders and freight bookings, neither
freight  nor  transportation  units  can  be  transported.  However,  freight  orders  can
represent transportation without transportation units and freight units; these represent
empty moves, which may make sense in certain circumstances, although you usually
attempt to avoid them.

## Freight Order Structure

Freight  orders  and  freight  bookings  result  from  planning  and  consolidating  freight
units onto a vehicle-booked capacity or scheduled means of transport. Once this has
been completed, transport order execution can be triggered, and follow-on settlement
processing can begin.

However,  before  creating freight orders or freight bookings, you must plan for stages
at the freight unit level. This is because the freight orders that will be created relate to
the individual stages of a split transportation chain.

Freight units can have one or more stages. Stages can be created in the freight unit to
split  the  overall  transportation  chain,  for  example,  based  on  the  mode  of
transportation.  A  freight  unit  with  a  source  in  Germany  and  a  destination  in  the  US
may be split into three stages to reflect the following:

●  Pre-carriage from source to port-of-loading (PoL)
●  Main-carriage from port of loading to port of discharge (PoD)
●  On-carriage from port of discharge to destination

91


In this way, the individual stages may be used to create separate freight orders/freight
bookings  for  each  stage  to  subcontract  these  different  stages  to  three  different
business partners/carriers.

## Freight Orders

Freight orders and freight bookings contain the following information:

●  Planning information, for example, planned means of transport and stages,

routing, planned pickup and delivery dates, durations, and distances

●  Document dependencies, as well as predecessor and successor documents
●  Transportation charges and cost distribution

92


●  Cargo information: quantities and weights, goods information
●  Execution information
●  Business partner information
●  Output management
●  Status information and blocking information
●  Subcontracting information

93


Lesson 2 - Defining Planning Processes

## Objectives

After completing this lesson, you will be able to:

●  Explain the different planning processes and options.
●  Explain the different selection options for planning processes.
●  Define the tasks involved in transportation planning and identify the relevant SAP

Fiori apps used to carry out these tasks.

## The Planning Processes

The goal of transportation management is to provide customers with the ability to
manually or automatically plan and optimize their transportation requests. This
includes performing order consolidation, where a company can group orders with the
same ship-from and ship-to locations for more efficient transportation quantities.

If multiple orders are being shipped within a predefined transportation zone, your
company can try to efficiently schedule and route the various orders, and choose the
appropriate carrier. The planning and selection can be determined using the most
cost-effective and timely route from source to destination while considering real-world
constraints, costs, and penalties. The optimizer can make multi-modal decisions such
as sea, air, truck, train, and any combination thereof. The planning function can also
perform multi-pickup and multi-drop options.

Within the optimization algorithm is the ability to use the appropriate resources
regarding availability and capacity. The optimizer can consider incompatibility rules to
restrict how freight orders are built, such as modeling material-specific transport
requirements (for example, cooled products). In addition, carrier selection allows your
company to determine the right combination of carrier assignments based on cost,
equipment availability, priority, and business share goals.

## Transportation Planning Scenarios

Transportation planning supports multiple variants. Several scenarios can be used,
depending upon shipping requirements, as follows:

●  Truckload shipments (FTL or LTL)
●
Intermodal (IM)
●  Direct shipments

94


●  Multi-stop shipments
●  Pooled distribution

Truckload Shipments (FTL or LTL)

Truckload shipments tend to be the simplest of the outbound planning scenarios. The
transportation order received by the shipper is in a full truck load quantity, typically >=
35,000 lb, or 3,660 cubic feet, or 28 - 32 pallets. The shipment is from one source to
one destination, so very little route planning is necessary, except for carrier selection.
The ideal situation would be one product, but multiple line items can be supported. In
TM, when orders are entered with a weight greater than 35,000 lb, the system can be
set up to automatically plan, tender, and cost the freight order without additional user
intervention. This is considered a one-step process.

Full Truck Load (FTL): In some industries, goods are ordered and delivered based on
full truck load because that is an inexpensive option. Typically, this is used for cheap
products where the transport costs are high compared to the value of the goods. This
FTL scenario is also used extensively in bulk transport. If the order is for multi-line
items, TM can perform truck load optimization planning for freight units. During
planning, companies can perform carrier restrictions (a carrier is not permitted).
Additionally, companies can perform carrier selection based on lowest costs if a
default carrier is not maintained. Once planning is done, the transportation order is
ready for tendering. Finally, bills of lading can be created with driver notes when the
shipment is picked up.

## Intermodal Shipment

Intermodal freight transport involves the transportation of freight in a container or
vehicle that can use multiple modes of transportation (rail, ship, and truck) without any
handling of the freight itself when changing modes. This method reduces cargo
handling, improving security, reducing damages and losses, and allowing freight to be
transported faster. This method reduces costs compared with road transport and is
the key advantage when deployed for intracontinental use. However, the cost savings
may be offset by reduced timing for road transport over shorter distances.

Intermodal transport is generally used for two purposes. One is to move goods
relatively cheaply over long distances using ocean and rail transport. The second is
moving goods over long distances quickly, for example, with air freight. Based on the
requested delivery date, the carrier selection process determines whether to use
intermodal or truck load as the means of transport. This is based on the transit time
for each means of transport: intermodal container on flat car (COFC) with a four-day
transit period or TL with a three-day transit period.

95


## Multi-Stop Shipments

Multi-stop or pool shipment consolidates two or more orders into one or more
shipments. Instead of making several (say 5) shipments and sending a separate
vehicle to each customer, your company plans to have only one vehicle visit each
customer. This is a truck load (TL) process, requiring some planning to ensure no
constraints are violated. Be aware that in-transit stops are limited, usually three or
fewer. As transportation volumes increase, optimized multi-stop planning improves
operational efficiencies. Routes can be determined by pick-up and delivery windows at
both shipping and receiving locations.

## Pooled Shipment

Pooled distribution is prevalent in delivery/distribution scenarios, from distribution
centers to customers. In the postal industry, it is also used to deliver mail to post
offices or large customers and institutions. In general, this scenario also includes the
collection of empty returnable packaging from customer sites.

## International Transportation

When companies begin to transport goods across borders, the complexity of the
logistics increases. Multiple modes of transportation may be needed depending on
how the product gets to its destination. In addition, you have to consider the legal
requirements necessary to import and export products to other countries.

Standard Process Flow

96


The standard planning process begins with creating freight units.

Planning relies on three distinct pillars, as follows:

●  Master Data

Master data objects such as the transportation network (locations,
transshipment hierarchies, transportation zones, transportation zone
hierarchies and transportation lanes) and resources are the basis for any
planning activities in SAP TM.

●  Selection Profiles

Selection profiles specify what should be planned in a particular scenario. For
example, selection settings specify the geography for which a transportation
plan shall be created. This could be, for example, all freight units to be
transported within California.

●  Planning Profiles

Planning profiles specify the "how" of the process. For example, a planner may
only be allowed to schedule standard trucks and not a helicopter for
emergency transports. This information dictates how the actual transportation
is to be carried out. Which resources can be used, and at what cost is specified
in the planning settings?

97


## Short-Cut Process, Purpose and Application

Once created, freight units are used by manual or automatic planning activities to
build freight orders, which can subsequently be used for carrier selection and/or
tendering processes. The purpose of the short-cut process is to skip any planning
activities because these may not be required in certain scenarios. For example, if the
sales orders that a company receives already state the required truck size, the freight
order could be created directly from the transportation demand (in this example, a
sale order). Technically, this is done during freight unit building by selecting a freight
order type instead of a freight unit type.

Watch the simulation Compare the Standard and Shortcut Process to learn more
about the standard and short cut process flow.

## Exercise
Start Exercise

98


## Selection Options

Selection profiles determine which items are brought up for planning in the
transportation cockpit.

## Selection Objects

Selections can be made on several objects, including those outlined in the following
list:

●  Freight Unit (Stages)
●  Transportation Units
●  Freight Orders
●  Freight Bookings

99


Selection attributes include geographical selection (using any location or zone
attribute) and time-related selection attributes, such as pickup and delivery windows.

Additional selection attributes such as statuses (for example, planned or unplanned
freight units) can be considered.  An example of an additional selection attribute might
be the product's nature, such as freight unit type or dangerous goods.

## Geographical Selection Attributes

In a company’s planning department, geography is often used to allocate planning
responsibility.  For example, an individual or team might be responsible for a specific
plant, distribution center, or group of customers in a geographical area.  The
geographical selection attributes in the selection profile allow the team to limit their
view so that they only see FUs or FOs for which they have responsibility.

## Time-Related Selection Attributes

You define the demand horizon in the time-related selection attributes that you assign
to your selection profile. You can define a demand horizon for pickup and a demand
horizon for delivery. The system chooses all freight units and freight orders whose
pick-up date/time or delivery date/time lies within the relevant demand horizon.

## Additional Selection Options

You do not have to use selection profiles, typically pre-defined, to select objects for
planning. Suppose you need to plan on the fly without a selection profile. In that case,
you can also choose freight units from a worklist or use the second entry screen of
the transportation cockpit to define selection criteria. These selection criteria do not
only include freight unit(s) (stages) but allow you to select other documents (like
container units and freight orders) as well as capacities (like vehicle resources or
schedules) and configuration (like the planning profile and page layout).

## Profile and Layout Sets

●  Profile and layout sets are used in several apps:

○  Transportation Cockpit
○  Carrier Selection
○  Delivery Builder
●  Profile and layout sets define

○  Data to read (for example, freight units)
○  Settings (for example, planning profiles)
○  Page layouts

100


The profile and layout set (PLS) management applications enable an administrator to
centrally create and manage PLSs for a team or organization and assign users to
them. This approach simplifies working with PLSs by removing the need for individual
users to create and maintain their own. When an administrator creates a PLS and
assigns a user, the PLS is available for the user to select on the relevant application
start screen.

When creating a PLS, the following recommendations should be considered:

●  Transportation cockpit:

You are recommended to enter a selection profile for freight units and a
planning profile to which you have already assigned a selection profile for
freight orders and freight bookings.
Optionally, you can also specify incompatibility settings and settings for
capacity selection. If you have already assigned incompatibility settings or
settings for capacity selection to the specified planning profile, the system
overwrites these settings with the settings you specified here.
The system considers the profiles you specify in your PLS for all planning
options available in the transportation cockpit.

## Note
In the transportation cockpit, the user can use the Change Planning Settings function
to temporarily change the planning and load planning settings in the selection profiles.
The system discards these changes when you leave the transportation cockpit or
change the profile selection.
Carrier selection:
You are recommended to enter a selection profile for freight orders, freight bookings,
and carrier selection settings.
Creating delivery proposals:
You are recommended to enter a selection profile for freight units, freight orders,
freight bookings, and a delivery profile.

## Planning Tasks

Routing, Planning, and Carrier Selection

101


The figure, Routing, Planning and Carrier Selection, outlines the complete planning
process: a freight unit X is first routed using, for example, a transportation proposal.
Based on this routing, three stages are created for freight unit X, as follows:

●  10 - A stage for US road pick-up transport
●  20 - A stage for the ocean voyage
●  30 - A stage for EU road delivery transport

Up to a certain point, these stages are planned independently because different (local)
planners may be responsible for scheduling each stage. A freight order is created as a
result of this stage. Finally, carriers are selected based on specific criteria. This is
described as a three-step process, but a planner can decide whether to perform
planning and carrier selection in two steps or three. It is also possible for the SAP TM
optimization function to plan all three steps in one run - this planning strategy is called
one-step optimization.

## Process Steps

The steps involved in the process, whether one, two, or three steps, can be described
as follows:

●  Three-step

1.  Determine routing (for example, via transportation proposal)
2.  Vehicle scheduling and routing to create (a) freight order(s)
3.  Carrier selection

●  Two-step

1.  Vehicle scheduling and routing to create a freight order

102


2.  Carrier selection

●  One-step

1. One-step optimization determines the route, creates a freight order, and
selects a carrier

## Creating Freight Orders

Manual creation is generally used when you know the most important transportation
data, such as source location, destination location, and business partner. You regularly
transport goods for a certain customer using a certain carrier.

To manually create a freight order, you require the following information: general data
for the freight order (shipper, consignee, carrier, resource, locations, dates and times,
and terms of payment), information about any additional intermediate stops, the items
involved (add freight units to the freight order or enter the items directly on the freight
order), and information about the charges involved (as calculated or configure the
system to calculate charges). Once the required information has been entered, you
can check the consistency and save the freight order. The freight order can then be
sent to the carrier and confirmed or rejected on behalf of the carrier. Necessary
documents can be printed, and a freight settlement document is created after the
execution. Some information, like source and destination location, is automatically

103


populated in the freight order if you create the freight order from the freight unit
worklist.

You can create a freight order by copying an existing one (a reference document). The
system copies the header data and the logistical data. However, it does not copy
references to freight units and execution information.

Finally, you can create freight orders via the short-cut process based on a freight unit
building rule, which will be explained in more detail later in this lesson.

The more advanced features of creating freight orders are their interactive creation in
the transportation cockpit, VSR optimization, and the use of transportation proposal
functionality.

## Manual and Automatic Transportation Planning

Transportation planning activities in TM can be performed manually, automatically,
interactively, and in the background. For interactive planning, the central planning user
interface is the transportation cockpit. Both manual and automatic planning activities
are performed there based on planning strategies (for example, one-step
optimization).

## Planning Profile

Planning profiles are used to influence and control the outcome of the planning
process.  A planning profile must be specified for a background optimizer run and
interactive planning in the transportation cockpit. A planning profile is relevant for

104


scheduling actions performed in the freight order. Several settings can/must be
created for use in the planning profile.

The planning profile includes settings to control the different steps of the optimization.
These steps are controlled by strategies set up in Customizing.  SAP delivers standard
strategies – but unique strategies can be created.  The strategies are made up of
various programs.  If you wish to perform manual planning or a scheduled planning
run, there is a standard strategy for each.  You also specify in the planning profile
which type of checks will take place concerning incompatibilities, dangerous goods,
and so on.

You can assign the following settings and profiles to a planning profile:

●  Capacity selection settings:

Here, you choose the required capacities, such as resources. If you use
resources for which you have defined an ADR limit, VSR optimization considers
the number of ADR points for this resource during the optimization run.
Moreover, you can specify that resources for which you have set a planning
block are not displayed in the resource lists of the transportation cockpit.

●  Capacity availability settings:

Here, you can restrict the availability of resources and equipment types. Using
the rules you define here, the system determines when specific resources or
equipment types are available based on shift sequences and factory calendars.

●  Capacity document creation settings:

The capacity document creation settings define which document types are
used with this planning profile and which requirement grouping profile should
be applied.

●  Optimizer settings:

Here, you can define the optimizer runtime, the maximum number of

105


transshipment locations and processes, and the freight order building rule, for
example. You also specify whether you require rough or detailed information
for your planning activities, define the necessary process controller strategy,
and configure the settings for generating transportation proposals.
In the advanced settings, you can also specify whether the main aim of your
transportation proposals is to ensure the lowest transportation costs or the
shortest transportation duration possible. You can also define preferences
about your relative weighting of the variance of carriers, routes, and departure
dates or activate or deactivate capacity constraints at the transportation mode
level. You can also specify whether the system is to ignore specific settings,
such as the capacity or ADR limit of a resource during VSR optimization.

●  Load planning settings:

Here, you can define the optimizer runtime, the planning strategy, and various
rules for load planning. For example, you can define the maximum height
difference between stacks in a row.

●  Constraints and costs settings:

Here, you define costs related to freight units and means of transport. In most
cases, these costs are not actual costs. They offer a means of controlling the
result of the optimization run (for example, earliness costs and lateness costs).
Incompatibility settings:
Here, you define settings for your incompatibilities.

●

●  Carrier selection settings:

Here, you specify whether the system uses transportation allocations or
business shares, for example.

●  Manual planning settings:

Here, you specify how you want the system to behave when it assigns
documents and resources:

○  Assignment of documents:

You use these settings to control how the system assigns one or more
requirement documents to a capacity document.

○  Removal of the assignment of documents:

You use this setting to control how the system removes the assignment
of requirement documents to capacity documents.
○  Assignment of resources and creation of documents:

You use these settings to control how the system assigns resources to
documents and how it creates and assigns reference documents.

●  Scheduling settings:

Here, you define loading and unloading durations for scheduling, for example.

●  Unified package building settings:

The unified package building profile relevant to the late package building
process is defined here, among others.

106


●  Transportation cockpit settings:

These settings define some of the behaviour of the transportation cockpit.

107


Lesson 3 - Planning Interactively

## Objectives

After completing this lesson, you will be able to:

●  Explain the relevant transportation activities and their scheduling logic
●  Access the transportation cockpit.
●  Perform interactive planning to create freight orders.

## Transportation Activities

Scheduling in SAP TM involves the following activities:

●  Drive / Travel
●  Load
●  Unload
●  Prepare
●  Finalize
●  Couple
●  Uncouple

The duration of the individual activities is defined in the transportation network (travel)
and in the scheduling settings of the planning profile (load, unload, prepare, finalize,
couple, uncouple).

108


Scheduling in the transportation cockpit or freight order considers the following
constraints:

●  Time windows for loading and unloading activities for your freight units
●  Loading and unloading durations of your freight units
●  Appointments for the freight order your freight units are assigned to
●  Location sequence of your freight order
●  Existing freight orders on resources
●  Coupling and uncoupling durations
●  Absences and non-working times of the involved drivers
●  Downtimes and non-working times of the involved vehicle resources
●  Calendar resources, as well as the calendars and capacities for the loading and

unloading activities of handling resources

●  Calendars of the involved vehicle resources and drivers for loading, unloading,

transportation, coupling, and uncoupling activities

●  Minimum and maximum goods wait times defined for transshipment locations

Transportation Cockpit

## Business Example

John is a logistics coordinator at a shipping company, and needs software that will
manage his company’s shipments. He needs the ability to view all of his customer’s
domestic and international export orders, and consolidate them to ship as efficiently
as possible. To accomplish this, he needs an easily managed dashboard to plan his
orders. For some shipments, John uses automatic planning, but he still needs to verify
the result of the optimizations. For other shipments, he needs to plan the transport
requirements manually. Therefore, Depending on the scenario, he requires different
information and functions to be available at different times. The specific and
differentiated presentation of information possible in TM allows him to plan efficiently.

Transportation Cockpit

109


Amongst others, the transportation cockpit includes the following elements:

●  Requirements list (freight units)
●  Capacity lists (vehicle resources and schedules)
●  Order list (freight orders, but may also contain freight bookings as transactional

or agreed capacities)

●  Order details

## Tasks in the Transportation Cockpit

The transportation cockpit is a central element in the transportation planning process
and facilitates numerous tasks.

The transportation cockpit can be used for the following tasks:

Transportation Cockpit Tasks

●  Manual planning
●  Creation of transportation proposals
●  VSR optimization
●  Load planning
●  Carrier selection
●  Triggering of a tendering process
●  Creation of delivery proposals
●  Creation of freight bookings

The cockpit requires users to enter multiple profiles that dictate the content of the
generated result lists. The selection profile specifies which freight units or freight

110


orders are relevant for a particular objective. The planning profile outlines how the
selected freight units will be planned. Additionally, the capacity selection profile limits
the planning run based on the transportation resources that are available for use.

Once the profiles are determined, planners can utilize the cockpit to create freight
bookings or manage existing freight orders. The layout of the transportation cockpit
offers flexible settings that control the information displayed and the available
processing options. A combination of selection and planning profiles and a layout can
be assigned to a specific profile and layout set. This ensures that each planning
scenario is consistently shown in the designated layout, while another can utilize a
different layout.

For instance, in one scenario, a planner might need to plan for liquids being
transported in tank trucks and would need to see the volume of the product. In
another scenario, the liquids might be in barrels on pallets, requiring the planner to see
the pallet count instead. Switching between different layouts on the fly is possible,
especially if a multi-step planning process leads to varying needs at each stage.

## Transportation Cockpit: Standard Layout

In the standard layout, the main screen is divided into four quadrants (views). The
maximum number of views in any layout is 6. The standard layout contains the
following views:

●  Freight units to be planned
●  Available capacities that can be used for planning
●  Freight order/booking list
●  Freight order/booking details

Each view has processing options using menus and buttons within the views.
Processing options include the following actions:

●  Merge / split freight units
●  Apply default routes to freight units
●  Remove resources from freight orders
●  Cancel freight orders
●  Schedule and check freight orders

Each menu or button can be personalized in the planning layout definition.

Freight Planning on Multiple Screens

111


If a user works with several screens, they can choose a separate layout for each
screen. The transportation cockpit can be deployed in multiple windows on up to three
screens.

Planning from the Cockpit

## Automatic Planning

Both manual and automatic planning are provided for in the cockpit. In relation to
automatic planning, transportation proposals can be generated automatically and the
optimizer allows planners to plan requirements onto resources and freight bookings or
orders. Optimizer planning also creates detailed log information that can be analyzed
using the explanation tool.

## Manual Planning

The following options exist for manual planning:

●  Drag a freight unit onto a resource, thereby creating a new freight order. Add

resources/MTrs.

●  Drag a freight unit onto a freight booking, thereby adding the freight unit to this

freight booking.

●  Drag a freight unit onto a freight order, thereby extending the freight order.
●  Command line planning and buttons provide additional options on top of the

drag and drop functionality.

Transcript for video:

“The  integration  of  Business  AI  in  cloud-based  ERP  solutions  is  an  important  area  of
focus  in  SAP's  strategy,  and  Transportation  Management  is  benefiting  from  new  use
cases  based  on  generative AI. One example of how such innovation is being integrated
into  Transportation  Management  is  conversational  planning.  In  the  transportation
cockpit,  planners  can  perform  various  planning  operations  using  natural  language
through  the  conversation  planning  feature. For instance, if a planner needs to schedule
stages  to  France  using  a  Volvo  van,  he  can  simply  enter  a  prompt  such  as  select  the
stages to France and the Volvo van. The generative AI function identifies and selects the
necessary  stages  and  resources,  displaying  the  results  instantly.  The  planner  then
assigns  the  selected  stages  to  the  selected  resource.  Next,  the  planner  wants  to  plan
shipments  for  a  specific  store  using  a  sustainable  truck  by  entering  his  request  and
natural  language.  The  system  seamlessly  executes  the  planning  with  a  sustainable
resource. Now the planner needs to select unplanned stages requiring 10-ton trucks with
a  prompt.  The  system  efficiently  filters  the  stages  based  on  the  criteria,  allowing  the
planner  to  use  an  optimizer  for  planning.  The  planner  updates  the  map  to  show  the

112


detailed routes for all of the freight orders that were just created. It's pretty cool right? As
AI  continues  to  revolutionize  how  we  work,  we  can  expect  to  see  more  and  more
innovation  in  the  area  of  Transportation  Management.  This  example  is  just  one  of the
use  cases  currently available using SAP S/4HANA Cloud with integrated Transportation
Management.  Keep  an  eye  on  future  developments  and  stay  up to date with the latest
features as they are released.”

This video introduces the integration of Business AI in cloud-based ERP solutions with
the example of conversational planning being integrated into SAP Transportation
Management.

## Conversational Planning with AI

Conversational Planning with AI* is embedded in the transportation cockpit (*some
contractual requirements apply for use of AI-based functionality). AI-powered
conversational planning can assist a planner in making manual planning decisions.
The transportation cockpit user interface is enhanced with a natural language
conversational interface that allows users to seamlessly perform UI actions, execute
multiple commands, and retrieve planning context information (that might not be
displayed in the cockpit).

Commands can be either typed or spoken, and contextual information available in TM
data can be automatically retrieved. Data that is not available in TM, but only in an
LLM, can also be used; an example of such commands is "Plan all products that need
to be refrigerated and transported to the city of Berlin on the smallest truck".

This new way of working enables a completely new way of interacting with TM in the
transportation cockpit, delivering flexibility, efficiency and broader accessibility.

## Interactive Planning

Interactive Planning on the Map

113


Interactive planning on the map allows you to:

●  Assign freight units/freight orders to resources
●  Add an intermediate location to a freight unit or a freight order
●  Search by proximity
●  Show related transshipment locations

## Options

●  Drag and drop
●  Context menu

The map can be displayed in a separate screen area in the transportation cockpit or in
full screen. However, having the map displayed in a separate screen area enables the
planner to see the selected freight units, freight orders/bookings, transportation units,
and resources on the map directly.

## Display Options

When you display the map, you can choose whether all of the planning objects or only
selected ones will be displayed. Furthermore, in a display profile, you can choose
which planning objects will be displayed on the map, such as freight orders or freight
units. You can call up the display profile with the toolbar.

## Planning Functions

You can carry out your planning on the map. If, for example, you select unplanned
freight units and start planning from the context menu, the system shows the possible

114


assignments of the freight units to the resources. Select the assignments that you
require.

You can also assign unplanned freight units or multi-relations containing unplanned
freight units to resources using drag and drop. When you do so, you can either assign
the freight units to the resource or the resource to the freight units. You can use the
proximity search in the context menu to find unplanned freight and transportation
units within a specific radius of a resource or location.

If you want to split a stage displayed on the map, you can assign an unplanned freight
unit or multi-relation to a location using drag and drop. Once you have selected the
required planning option, the system will add the chosen location to the freight unit
stage and update the map accordingly. This process also applies to freight orders.
You can also display transshipment locations that are not necessarily part of your
planning activities. You display these locations by choosing Show Related
Transshipment Locations from the context menu.

If a freight order does not have a vehicle assigned to it, you can assign it by using drag
and drop. To do so, you assign the freight order to a single vehicle resource or a
multi-spot containing at least one vehicle or passive vehicle resource and select the
relevant planning option from the menu. You can use the proximity search in the
context menu to find available resources within a specific radius. You can also specify
the exact position of a resource at any time in the context menu of the map. The
system displays all of your transportation planning activities on the map. When you
leave the display of the map, your planning activities are also displayed in the table
view of the transportation cockpit.

Context Menu Options

## Address Search

You can use the context menu of the map to start the address search and display the
search results on the map. The address search is based on the geocoding of the
location. This allows you to perform several address searches and display the search
results simultaneously on the map. You can use the context menu of the map to hide
the search results individually or entirely.

## Route Display

You can use the context menu of a connection line to determine a route display along
actual street routes (georoutes). This function is dependent on the geographical
information system available in the system. Alternatively, you can use a resource's
context menu to display the connection lines of all freight orders assigned to this
resource.

115


Gantt Chart: Display of Resources and Documents

Gantt Chart

Visibility:

●  Usage of trucks and trailers
●  Load utilization of trucks and trailers
●  Downtimes and nonworking times
●  Execution status and reported times for freight orders, trailer units, and their

activities

●  Notifications for overload, empty movements, and time conflicts

Usability & Flexibility:

●  Time zoom in and out
●  Aggregated and detailed view
●  Hierarchical views
●  Single and dual view (horizontal and vertical)

When performing transportation planning, a planner usually considers two main
aspects: availability of resources and utilization of the used resources. With the
conventional use of the transportation cockpit, the sequential order of freight orders
using a particular resource and resource availability for a specific timeframe is not
(graphically) shown. Using a Gantt chart, often used in project planning as well, helps
to visualize the availability of resources and the sequential order of transports. The
Gantt chart is fully integrated into the transportation cockpit.

116


Transportation planning can now also be done using a Gantt chart. In the Gantt chart,
freight orders and vehicle resources are displayed as a time bar, and planners can
manually plan transports using drag and drop.

The Gantt chart provides a visual platform for performing transportation planning.
With an intuitive and graphical user interface, the Gantt chart enables you to perform
transportation planning visually, interactively, and more efficiently.

The Gantt chart is a screen area in the transportation cockpit, which can be enabled in
a page layout. All standard functionalities, such as positioning the Gantt chart
anywhere on the transportation cockpit and maximizing the screen area to full screen,
are available in a Gantt chart.

The Gantt chart displays planned and unplanned freight orders and resources in a
time bar. It is configurable; additional sets of information should be displayed next to
the time bar. The time bar itself shows the activities planned for the document and
resource. Depending on the layout chosen, the planner can use a single view, which
only indicates planned and unplanned freight orders or resources exclusively, or a dual
view (as shown in the figure, Gantt Chart: Display of Resources and Documents) that
displays two entities next to each other. Similar to the dual view in the transportation
cockpit, the dual view can be configured vertically or horizontally. The scrollbars of
both screen areas can be synchronized.

A zoom bar on top of the screen area can zoom in and out to see a more detailed view
of a day or week or a more general view of a month.

An essential factor for transportation planning is the utilization of a vehicle. The
utilization of the vehicle can be displayed with the utilization view, which can be
enabled when needed. The utilization view shows the utilization of the vehicle over
time in a graph. The graph is displayed in a detail line below the actual resource or
document. In this case, the single-view option is chosen, which enables the user to
see all the execution information on one screen. Multiple loading acts are only
displayed as one item in the Gantt chart. This keeps the chart clean and easy to
understand.

## Gantt Chart: Interactivity and Planning Scenarios

The main benefit of this functionality is a good overview of the status of the trucks.
Re-planning can be done by drag and drop. Freight orders can be fixed or unfixed by
just clicking one button. Furthermore, navigating directly to the resources or trailer
units is possible.

117


The main focus is the planning of road transport. The truck and trailer planning can be
done easily. When execution events change the planning necessary, this can be
immediately done via this overview.

Interactive planning can be performed in the Gantt chart using drag and drop.
Unplanned freight orders can be assigned to resources. Likewise, resources can be
assigned to freight orders. The freight order is dropped on the resource time bar. If the
freight order is not dropped on the same date it was initially planned, the date where it
was dropped is taken over into the freight order. Scheduling is only performed when
requested using the Scheduling button on top of the Gantt chart. The dual-view can be
selected to display unplanned freight orders on top and the available resources below.
This enables the user to work with one window to plan freight orders. The dual view
can either be displayed horizontally or vertically. The size of each area can be changed
by dragging with the mouse.

The Gantt chart enables the planning of unplanned freight orders by dragging on
vehicle resources and creating transportation units. When dragging and dropping the
loading activity of one freight order into the time bar of another freight order, both
freight orders are combined.

Overlap means a resource has been planned multiple times and is therefore not
executable. For example, if a trailer is already scheduled and newly planned during the
next step, an overlap is caused, which is displayed as a red line to the user.

Similar to the utilization view, an overlap view shows if several documents on a
resource overlap. This overlap can be overcome by scheduling the resource.

Driver Management Overview

118


Drivers can get assigned to existing freight orders and vehicle resources. It is also
possible to create freight orders to which the system assigns drivers automatically as
soon as they are created. This function is available only for road freight orders and
trucks. One or more drivers can be assigned to an existing freight order or to the
individual transportation stages of an existing freight order. In a driver team, the
individual drivers take turns driving—the person not driving sleeps.

A prerequisite of this process is that drivers are created as business partners with
business partner role Driver. The properties of the driver are as follows:

●  Home location
●  Organizational Unit
●  Validity Period
●  Absences (for example, sickness, vacation)
●  Non-working times (for example, shift sequences from Monday to Friday)
●  Last planned location and availability time
●  Qualifications

## Automatic Assignment of Drivers

Automatic assignment of drivers to freight orders happens if the driver assignment is
requested via the freight order type and the driver is assigned to the resource master
data of the vehicle resource as the default driver. Other than that, manual assignment
of drivers is possible in the transportation cockpit as follows:

●  Drag and drop:

It is possible to drag and drop drivers from the list of drivers in the
transportation cockpit to the freight order being planned in the road freight
order hierarchy or in the road freight order list. Suppose it has been specified in
the freight order type that drivers have to be assigned per transportation stage.
In that case, it is possible to drag and drop drivers in the road freight order
hierarchy to the individual transportation stages.

●  Manual creation and change:

It is possible to enter or change drivers manually in the Driver column in the
road freight order hierarchy or in the road freight order list. If specified in the
freight order type that drivers have to be assigned per transportation stage, it is
possible to enter or change drivers for individual transportation stages in the
Driver column in the road freight order hierarchy. Suppose the driver
assignment has been activated in the order details area in the layout of the
transportation cockpit. In that case, it is possible to select a freight order in the
road freight order hierarchy or in the road freight order list and manually enter
or change a driver in the details for this freight order.

119


●  Dialog box:

Finally, it is possible to select a freight order in the road freight order hierarchy
or in the road freight order list and choose the Assign Driver button. A dialog
box appears in which drivers can be entered. Then, the user can decide in the
dialog box whether to replace the currently assigned drivers with new drivers or
add drivers to the existing ones.

120


Lesson  4  -  Planning  Automatically  Using  the  Optimizer  and
Proposal

## Objectives

After completing this lesson, you will be able to:

●  Generate a transportation proposal.
●  Understand the logic of VSR optimization.
●  Execute the VSR optimizer.

## Transportation Proposal

A transportation proposal defines how a freight unit can be transported through a
transportation network (which is defined by locations, transshipment locations,
transportation zones, transportation lanes, vehicle resources, schedules, and
bookings). The system determines a set of alternative transportation proposals for a
given transportation demand (freight unit). Transportation proposal functionality
serves two purposes.

The first and most obvious purpose is to help the user identify the different
transportation options for a freight unit. In a complex network where end-to-end
transportation requires several stages, transportation proposals are an easy way to
make the different options transparent. Transportation proposals can differ in routing,
means of transport, and time required. Each of these variables can increase or reduce
costs, and the proposals thus provide the planner responsible with the necessary
information to make an appropriate choice.

Secondly, transportation proposal functionality can be used from the freight unit to
create the stages upfront, for example, to choose the option of ocean transport
because this is the cheapest choice. In this use case, no freight orders are created
based on the result of the proposal, but only the stage information is stored. This
allows the task of planning the different stages to be assigned to different planners
and completed at different times.

121


Entry Points for Transportation Proposal Determination

Freight Unit→Stages→Route→Transportation Proposal

Transportation Cockpit→Select Freight Unit→Transportation Proposal

## Layout of the Transportation Proposal Result

The layout of the transportation proposal result screen can be configured in a way that
is similar to the transportation cockpit layout. The results can be displayed in a table
format or visualized on a map. In the table-based layout, each stage is shown in a
separate line. In complex networks, there could be millions of routing options for a
given transport, with only minor differences between them. Depending on the
objective of the planner, results can be presented according to defined criteria, as
follows:

●  Lowest cost
●  Shortest duration
●  Carriers assigned
●  Departure days
●  Routes

## Features of the Transportation Proposal

The features of the transportation proposal are as follows:

●

Implicit definition of transshipment locations by schedules and freight
bookings (simplified definition of transportation network)

●  Mode of transport constraints on freight unit and freight unit stage level
●  Fast determination of transportation proposals, yielding more alternatives

according to predefined variation criteria (for example, route, carrier, departure
date) and trade-off between time and cost (controlled variation according to
predefined criteria)

122


●  Consideration of preferences for locations, carrier, mode of transport, dates,

and times

●  Display of multiple solutions on the result map
●  Rough planning (detailed planning on the main leg and rough planning for
pre-leg and subsequent leg, based on rough definition of transportation
durations)

Vehicle Scheduling and Routing Optimizer

## Business Example

In his role as an SAP transportation consultant, John has been requested to explain
the benefits of freight orders and how they can be created using optimization criteria.
John must describe the principles of vehicle scheduling and routing (VSR)
optimization used in TM.

Freight orders represent a single shipment or load departing from one of your facilities
(outbound scenario) or arriving in one of your facilities (inbound scenario). For
example, the freight order can be created manually or automatically using the vehicle
scheduling and route optimizer. Freight orders are the basis for carrier selection,
tendering, and freight settlement processes. These topics are covered in separate
lessons.

## Note

A freight booking can also be created due to transportation planning, similar to a
freight order. For the sake of simplicity, only the term freight order is used
subsequently.

Freight Orders in Transportation Planning

123


In a freight order, freight units from different transportation demands
(SO/PO/DEL/OTR/DTR/FWO) can be consolidated. The VSR optimizer aims to find the
lowest cost solution based on the freight units planned, the transportation network (as
defined in master data), and, for example, the costs defined in the relevant planning
profile.

As the name suggests, the vehicle scheduling and routing (VSR) optimizer considers
routing and the sequence in which resources arrive at specific locations (as well as
the scheduling of tasks running in parallel). It evaluates potential changes to the
routing and the effect such changes would have on scheduling, helping to avoid the
possibility of delayed deliveries and follow-on costs.

Essentially, the optimizer's goal is to assign freight units to vehicles/resources and
determine the route and sequence of freight units per vehicle/resource so that all
constraints are met and total costs are minimized. The optimizer achieves this goal by
evolutionary local search, a population-based meta-heuristic that borrows selection
principles from evolutionary algorithms and relies heavily on local optimization.

A more evident example of how the optimizer works is its approach to potential date
changes. When a date change occurs, the optimizer applies this change to all freight
units on the affected vehicle or resource and dependent freight units on any other
resources. This method helps determine the best possible choice. The optimizer also
considers multiple factors simultaneously for other variables, such as transshipment
locations. This comprehensive analysis is essential for developing effective plans or
improving existing ones.

Costs and Constraints

124


The total cost, which the optimizer is designed to minimize, is a weighted sum of the
following items:

●  Non-delivery/execution penalty (per FU)
●  Earliness and lateness penalty (per FU)
●  Fixed cost (per vehicle or tour)
●  Travel-dependent costs (per capacity), for example, distance, duration, etc.
●  Load-dependent costs (per capacity and tour)
●  Sustainability costs such as CO2 emissions

## Optimizer Constraints

The optimizer can consider various additional constraints, as follows:

●  At some locations, a handling resource for loading or unloading may be

necessary, with attendant breaks or delays.

●  The transshipment time of an order at a specific location can be restricted by a

minimum and maximum duration.

●  There may be incompatibilities between orders, vehicles, (transshipment)

locations, and so on, which must be considered.

●  Driving times of vehicles may be restricted. For example, a planner can define
that after 8 hours of travel, a driver needs a 2-hour break and that 10 hours is
the maximum daily traveling time.

The VSR optimizer primarily operates based on freight units. When there are
unplanned freight units, the optimizer searches for available capacity to transport
them. As a result, it creates freight orders or freight bookings. If the VSR optimizer is
tasked with maintaining existing freight orders but can modify them, guidelines must

125


be provided on how these changes can be made. This process is known as
incremental planning for freight orders.

## Cost and Constraints Settings

The cost and constraint settings of the planning profile contain input for the
optimization cost. These are internal costs and are not related to a particular currency.
The following settings can be made:

●  Non-delivery cost: This is (business-wise, not technical) a mandatory entry. The
algorithm used in the optimization takes non-delivery into account. If there are
no costs for non-delivery, the system will deliver nothing since this is the
cheapest solution. Therefore, a cost setting for non-delivery must be
maintained.

●  Earliness and lateness cost: Sometimes, it is more cost-effective to deliver

early or late if this means the route/trip can be completed. This setting controls
the period for early or late pickup and delivery.

●  Means of transport or resource-specific cost: This setting controls the cost

●

concerning means of transport, and a break-even calculation can be made to
determine the means of transport used. For instance, rail is cheaper than road
for large volumes of weighty goods. These costs can be defined for individual
resources (based on vehicle resource master data) or groups of similar
resources (based on means-of-transport level).
In the Costs and Constraints Settings, it is allowed to define the minimum
target utilization of a means of transport to be considered when road freight
orders are created during VSR optimization. Furthermore, whether this
utilization is a hard or soft constraint can be specified. As a soft constraint, the
target utilization may not be reached, and a warning will be issued in this case.
This setting controls whether freight documents not meeting the desired target
utilization are kept or deleted after the optimization run. As a hard constraint,
the target utilization is always considered so that freight units may remain
unplanned. Note that maintaining a minimum utilization is not a constraint in
the optimization algorithm itself but rather a check performed on the result.

## Incremental Planning

In incremental planning, the following options are available:

●  The optimizer keeps the resource (truck or trailer).
●  The optimizer keeps all stops of an incremental freight order.
●  The optimizer keeps all freight units of such an incremental freight order.
●

It is possible to specify whether additional new stops to an incremental freight
order are allowed.

126


If more control over the incremental planning is required, there is a BAdI before the
optimization call. Here, each freight order can be flagged separately for incremental
planning. Additionally, there are the following options:

●  Define time frames for how much change is allowed in rescheduling.
●  Define if it is allowed to add stops as first or last stop or only between.
●  Define which locations are potentially allowed to be inserted and which are not.

How incremental planning can be controlled is described in note 1866364.

## Planning with CO2 Emissions as a Constraint

Given this focus on environmental topics, and transportation's key contribution to an
organization's carbon footprint, Transportation Management allows you not only to
report on greenhouse gas emissions but also to consider them as a constraint during
manual planning and vehicle scheduling as well as routing optimization for road
transport.

Transcript for video:

“Sustainable  business  practices,  including  environmental  sustainability, are becoming a
key  concern  for  many businesses around the world. Meeting Environmental, Social and
Governance,  or  ESG, targets is becoming a strategic focus for many organisations, and
reporting  results  connected  to  these  topics  is  becoming  a  requirement  in  some
jurisdictions.  Given  this  focus  on  environmental  topics  and  transportation's  key
contribution  to  an  organisation's  carbon  footprint,  I'd  like  to  show  you  how  SAP
Transportation  Management  enables  the  calculation  of  greenhouse  gas  emissions
during manual planning and vehicle scheduling, as well as routing optimization for road
transport.  CO2  emissions  can  be  considered  as  a  constraint  by  the  optimizer,  just  like
cost  or  time  constraints.  Planners  access  the  transportation  cockpit  via  the  SAP  Fiori
Launchpad.  In  the left panel of the cockpit, all queried planning requirements are listed.
In  the  requirements  panel,  key  sales  order  information  is  displayed,  including  location
information. Color-coded icons instantly highlight transportation requirements that need
attention.  In  the  road  freight  order  list  on  the  right,  CO2  emissions  are  displayed.
Color-coded icons in this panel highlight freight orders where the CO2 emissions exceed
a  shipper-to-find  threshold.  Now  we  select  unplanned  transportation  requirements  to
plan  using  the  optimizer.  Selecting  the  Details  button  populates  the  table  on  the lower
right  with  the  details  of  the proposed freight order. We can see the freight order on the
map  with  the  proposed  route.  Hovering  over  the  route  shows  the pop-up with planned
CO₂ emissions. Switching to the Gantt Chart view, the CO₂ data is also visual on the left
side  of  the Gantt Chart. Shrinking the Gantt chart view, we can see the Gantt chart and
map views. Switching back to the tabular view, we can save the proposed freight orders.
Drilling into the details of the newly saved freight order, the planned CO2 emission data is

127


visible  in  bar  chart  format.  Actual  CO2  emission  data  can  be  manually  entered  in  this
view  if  those  details  are  available.  Carriers  can  also  enter  data  about  the  actual  CO2
emissions via the Business Network for Logistics. Plan versus actual data is available in
bar  chart  format  within  the  freight  order  details.  As  you  can  see,  SAPTM  can  provide
invaluable  insight  into  the  CO2  emissions  generated  by  a potential transportation plan,
allowing  the  transportation planner to reduce the environmental impact of a company's
logistics  operations  as  well  as provide the transparent CO2 data needed by ESG teams
to drive strategic planning and company reporting.”

128


Lesson 5 - Planning Loads

## Objective

After completing this lesson, you will be able to generate a load plan

## Load Planning

Transcript for video:

“The  Transportation  Cockpit  offers  many  useful  features  to  a  transportation  planner.
Here I'd like to show you how you can use the 3D Load Plan to optimize how pallets are
loaded into a transportation resource such as a truck or a shipping container. This offers
a  good  visual  example  of  how  the  system  utilizes  data  such  as  the  Means  of
Transportation  and  Materials  master  data,  as  well  as  data  such  as  packaging
information,  and  so  on,  to enable efficient transportation planning. We start by opening
the  Transportation  Cockpit,  the  main  workspace  for  transportation  planners.  Here  we
navigate  to  the  upper  right-hand  quadrant  of  the  transportation  cockpit  where  we  can
identify all container units that have been planned and in our case, look for the container
unit  that  is  currently  being  planned  but  has  not been finalized, which is denoted by the
dollar  sign  followed  by  the  number  one. We navigate to the lower right quadrant of the
Transportation Cockpit where we can see the corresponding load plan for the container
unit  that  is  currently  being  planned.  Notice  the dollar sign followed by the number one,
further indicating this load plan matches the container unit selected. Clicking the Expand
icon in the lower right quadrant of the Transportation Planning Cockpit changes the GUI
to display and visualize the load plan in full screen mode. In full screen mode, we see the
load  plan  details  for  the  container  unit  that is currently being planned. On the left-hand
side  of  the  screen,  listed  in the item hierarchy, we see that there are 24 pallets that are
assigned  to  this container unit. On the right-hand side of the screen we see a graphical
visual  representation  of  the  20  foot  container  along  with all 24 pallets shown in red as
listed in the item hierarchy. By using the cursor, we can click on the pallets and can rotate
the  items,  offering  a  360°  view  of the items being considered by the load plan. We can
even  zoom  in  and  zoom  out  on  any  individual  palette.  When  we  click  the  Create  Load
Plan  button,  the  system  considers  all  the  rules  that  have  to  be  considered  like
stackability  and  dimensional  attributes  of  the  product  which  has  been  configured  and
suggests  an  optimal  load  plan  for  all  24  pallets  shown  in  blue.  As  indicated  by  the
messages for container "dollar sign 1", 24 of 24 items can be loaded. By using the cursor
we  can  click  on  the  20-foot container and can rotate the object offering a 360° view of
the  planned  pallets.  We  can  even  zoom  in  and  zoom  out  on  any  individual  palette.

129


Clicking  the  Clear  Load  Plan  button  will  remove  all  of  the plan pallets from the 20-foot
container.  The  pallets  change  from blue back to red along with the message Load plan
cleared.  Using  this  feature  allows  the  transportation  planner  to  make  any  necessary
changes.  Clicking  the  three dots at the top right of the screen will give a drop-down list
allowing  the  user  to  change  the  page  layout  along  with  various  settings.  Selecting
Change  Planning  Settings  will  offer  four  tabs  to  the  user,  these  are  Planning  Settings,
Manual  Planning  Settings,  Capacity  Document  Creation  Settings,  and  Load  Planning
Settings,  in  these  tabs  individual  settings  can  be  adjusted.  As  an  example,  we  can
change  the  loading  plan  rules  by  switching  the  setting  from  inactive  to  active,  or  vice
versa. Finalizing the changes can be done by pressing the OK button. Clicking the Create
Load  Plan  button,  the  system considers all the newly changed loading plan rules and a
new  load  plan  is  suggested.  By  using  the  cursor, we can click on the 20-foot container
and  can  rotate  the  object  offering  a  360-degree  view  of  the  planned  pallets.  We  can
zoom  in  and  zoom  out  on  any  individual  palette.  We  can  even  see  the  details  for  a
specific  palette  such  as  weight,  the  freight  unit  ID,  and  more.  By  using  the  right  click
mouse button, a list appears giving the user the ability to look at the proposed load plan
in a variety of ways. In this example, we can highlight items with the same product and
the system will highlight all pallets having the same product with the same color. Clicking
the  save  button  will  save  the  created  load  plan  indicated  by  the  message  data  saved
successfully. Features such as this simplify a planning process that would otherwise be
fairly  abstract  and  hard  to  perform  efficiently  without  all  the  required  data  at  your
fingertips. I hope you enjoyed this demo and found it helpful.”

You can plan the loading space of box trucks, trailers, semi-trailers, and containers in
the transportation cockpit or directly in one of the following business documents:

●  Road freight order
●  Trailer unit
●  Container unit

Planning is carried out at the level of business document items.

## Note

Load planning returns an approximate calculation of how the available loading space
can be optimally used, considering the maximum axle loads and the maximum weight
of  a  vehicle  resource.  The  calculation  is  based  on  the  master data you enter for the
resource. You must check the results calculated during load planning.

130


Take  the  following  business  scenario:  Katie  is  working  in  the  road  department  of  a
logistics  service  provider  (ABC  Company). She plans hundreds of road freight orders
on trucks every day. Previously, the system has supported her by comparing the total
weight  and  volume  of  the  cargo  and  the  truck.  However,  in  some  cases,  cargo  has
been left at the warehouse because carrying it would contravene the guidelines of the
truck  (for  example,  axle  weight  distribution).  Katie  requires  system  support  that
optimizes  the  load  plan  regarding  weight,  dimensions,  stackability,  axle  weight
distribution, and further rules. This support would enable her to create a detailed load
plan  that  could  then  be  used in the warehouse to guide the loading of the truck. The
load planning functionality of TM provides this support.

Load Planning as Part of the Planning Process

131


When  you  plan  a  road  freight  order  on  a  box  truck, trailer, or semi-trailer, the system
considers  capacity  restrictions  regarding  the  height,  width,  length,  and  weight of the
loading space. The same capacity restrictions also apply to planning a trailer unit on a
trailer  or  semi-trailer.  It  also  takes  into  account  the  maximum  axle  load  of  your  box
truck.  Furthermore,  in  the  system,  you  can  add  a  split  deck  to  your  trailer  or
semi-trailer  and  plan  two  decks.  When  you  plan  a  container  unit  on  a  container,  the
system also considers capacity restrictions in terms of the height, width, and length of
the loading space, as well as the total and empty weight of the container. In both the
transportation cockpit and the freight order, you can check the results of load planning
as a 3D load plan or a table load plan in the form of a list of business document items.
In the 3D load plan, you can show or hide individual objects and entire rows, columns,
or  stacks.  The  systems  also  provide  information  about  the  loading  space's  current
load distribution and utilization.

## Load Plan

The  load  plan  is  the  result  of  load  planning.  It  provides  an  overview  of  the  current
loading  space  available  for  transporting  a  business  document.
In  both  the
transportation cockpit and the business document, you can display the complete load
plan  as  a 3D or table load plan of business document items. You can show and hide
grid  lines  in  your  decks  in  the  3D  load  plan.  You  can  also  show  and  hide  individual
objects and entire rows, columns, or stacks and fill them with different colors.

The load plan contains the following information about the business document item:

132


Item in the resource

●  Resource
●
●  Loading sequence
●  Row, stack, and level in the loading space
●  Gross weight
●  Height, width, and length
●  Stackability

You  also  get  information  about  the  load  distribution  and  additional  statistical  data
about the current load on separate tab pages. This includes the following:

●  Number of loaded business document items
●  Used area on the lower deck of your double-deck trailer
●  Utilization of the loading volume as a percentage
●  Used area on the upper deck of your double-deck trailer
●  Maximum weight for each axle group compared to the current weight for each

axle group

●  Maximum trailing load compared to the current trailing load

3D Visualization

The  visualization  gives  the  planner  an  enhanced overview of the truck's loading. The
planner  can  rotate  the  view,  hover  the  mouse  over  particular  items  to  see  more
information  about  the  items,  and  they  can  hide  or  unhide  special  items  to  get  a
complete impression of the current loading.

In the 3D load plan, you can adjust a load plan manually using buttons in the toolbar or
keyboard shortcuts to move products and packages onto a truck. The status and the
axle  load  are adjusted accordingly. You must have selected the Activate Manual Load
Planning  checkbox  in  Customizing  for  Transportation  Management  under  Basic
Functions→Load  Planning→Define  Layouts  for  3D  Load  Plan.  You  can  also  define  in
this  Customizing  activity  which  combination  of  keys  execute  which  command  and
how far an object should be moved (length of the movement increment).

Load Optimization Functionality

133


## Load Planning Prerequisites concerning master data

You  have  specified  capacity  details  in  the  Resource  Master  Data  for  the  truck  on
which planning is to take place. The optimizer cannot perform the load planning if the
relevant  dimensions  are  not  maintained.  The  optimizer  and  the  3D-Visualization  for
the load planning use the dimensions maintained here.

Concerning the last point, the following data is critical:

●  Capacity

○  Mass: Gross vehicle weight
○
○
○

Internal length: length of loading space
Internal width: width of loading space
Internal height: height of loading space

●  Physical Properties

○  Tare weight: empty vehicle weight
○  Cargo body distance: from the front of the truck to the beginning of the

loading space

●  Axle Group

○  Axle type: single, tandem, triple, and so on
○  Axle group distance: distance from front of truck to axle
○  Dist. between axles: relevant in case of more than one axle
○  Max weight on group: maximum weight on axle group
○  Emp. weight on group: weight of empty vehicle on axle group
●  The load planning settings and rules. In the load planning settings, you can

maintain specific rules that the optimizer considers during the load planning
run, such as height difference within a row, maximum deviation, and so on. You
can set each rule as active or inactive and prioritize the list of rules.

Load Planning Settings

134


The  rules that the load optimization algorithm should observe are defined in the load
planning settings of the planning profile.

## Load Planning in the Transportation Cockpit

When  entering  the  transportation  cockpit,  select  the  appropriate  planning  and
selection  profile.  The  example  layout  in  the  figure  shows  a  list of all selected freight
orders in the top area. You can see the Load Plan tab in the lower area. Choosing this
tab  for  a  selected  freight  order  shows a list with all the main cargo items along with
the  3D  visualization  of  the  vehicle.  Only  the  main  cargo  items  of  a  freight  order  are
relevant  for  load  planning,  so  if  you  have  a  pallet  where  products  are  assigned  as
sub-items,  those  products  are  not  shown  in  the  list,  only  the  pallets.  In  the  case  of
multi-items (the item type can be defined in the freight order type), the level below the
multi-item is used for load planning.

Choosing the Load Planning button (above the freight order list) runs the load planning
optimization. The load optimizer fits the cargo items onto the vehicle, considering their
dimensions  and  ensuring  that  no  rules  are  broken.  Using the load planning function,
the planner can see immediately how much space for further items is left on the truck.

Information  about  the  planned  load  is  displayed  in  the  table  to  the  left  of  the
visualization image and includes information on the following points:

●  Position in which the item is loaded (loading sequence) on the truck
●  The stack, row, and level on which the item is loaded
●  Weight
●  Dimension

Load Consolidation

135


Load Consolidation is an extension of load planning. In load planning, the assignment
of a set of packages to one truck, trailer, or container has already been decided before,
and  the  decision  to  be  made  is  on  how  to  place  the  packages  within  the  one  truck,
trailer,  or  container.  The  planning  problem  for  load  planning  can  be  described  as
follows:

●  Given a set of packages and multiple trucks, trailers, and containers, how do
you assign the packages to the available trucks, trailers, and containers?

●  How do you place the packages in the assigned trucks, trailers, and containers?

Load Consolidation offers the following:

●  Optimizer-based, automated assignment of a given set of freight units to

resource types

●  Determination of the number of resources to be ordered / to be used
●  Focus on planning the main route where no routing decision has to be made

Load Consolidation supports the following:

●  Alternative resource types (for example, 20 ft, 40 ft, 40 ft High Cube Container)
●  Limitation of the maximal number of available instances possible
●  Minimization of total costs (based on defined fixed cost for usage of one

resource type instance)

136


●  Capacity Check based on given load dimensions (for example, weight and

●

●

volume)
Incompatibility between Freight Unit and Resource Type (for example,
temperature condition)
Incompatibility between Freight Unit and Freight Unit (for example, dangerous
goods)

●  Detailed Capacity Check (considering detailed pallet dimensions and loading

space and stackability of pallets)

●  Providing an exact load plan (as in load planning)

137


Lesson 6 - Creating Freight Bookings

## Objective

After completing this lesson, you will be able to create freight bookings and recognize
how they differ from freight orders.

## Ocean Freight Bookings

Ocean  transport  has  been  the  largest  freight  carrier  throughout  recorded  history.
Although the importance of sea travel for passengers has decreased due to the rise of
aviation (it is still popular for short trips and pleasure cruises), it remains important for
transporting goods. Freight transport by water is cheaper than transport by air. Sea or
ocean  transport  can  be  over  any  distance  -  by  boat,  ship,  sailboat,  or  barge,  over
oceans  and  lakes,  through  canals,  or  along  rivers.  Virtually  any  material  that  can  be
moved by water. Despite these benefits, ocean transport is less practical when speedy
delivery is paramount.

Regarding  ocean  transport, 'general cargo' refers to goods packaged in boxes, cases,
pallets, and barrels. In the 1960s, a "containerization" revolution altered how cargo was
moved  overseas.  When  a  cargo  is  carried  in  more  than  one  mode,  it  is  said  to  be
intermodal or co-modal.

Intermodal  freight  transport  involves  the  transportation  of  freight  in  an  intermodal
container  or  vehicle,  using  multiple  modes of transport (rail, ship, and truck), without
handling the freight itself when changing modes. The method reduces cargo handling,
improves security, reduces damages and losses, and allows freight to be transported
faster.

138


Planning  an  ocean  freight  movement  differs  from  planning  a  domestic  freight
movement  insofar  as  the  resources  are  often  more  scarce  and  tend  to  operate  on
fixed schedules. Schedules in TM can mimic the departure days, times, and frequency
of ocean-going vessels.

One  step  in  the  ocean-bound  process  that is different from the domestic scenario is
the  use  of  a booking. The freight booking is intended to reserve capacity on a vessel
(or  aircraft).  The  difference  between  a  (ocean)  freight  booking  and  a  freight order is
that  a  freight  booking  is  equivalent  to  buying  an  airplane  ticket;  that  is,  you  book
capacity; a freight order is equivalent to checking in baggage and having it put aboard
the plane.

## SOLAS – Convention for the Safety of Live at Sea

Starting  July  1,  2016,  the  International  Maritime  Organization  (IMO)  will  enforce  the
Safety  of  Life  at  Sea  Convention  (SOLAS)  requirements  to  verify  the  gross  mass  of
packed containers.

"A  packed  container  will  not  be  allowed  to  be  loaded  on  board  vessels  to  which the
SOLAS Convention applies unless the Verified Gross Mass (VGM) of the container has
been  provided  to  the  ship’s  master  or  his  representative  and  to  the  terminal  or  its
representative sufficiently in advance to allow for the edition of the loading plan."

VGM must be auditable.

Definitions and Explanations:

VGM  (Verified  Gross  Mass)  = The total weight of a container, including the weight of
goods, packing material, and container tare.

The following two methods are allowed to determine the VGM:

●  Weighing of the packed container
●  Sum of weighted packages and cargo items (including the mass of pallets,
dunnage, and other packing and securing material to be packed in the
container) plus tare mass of the container

The  VGM  must  be  included  in  the  shipping  instructions.  The  company  that  has  to
report  the  VGM  data  to  the  carrier/terminal  depends  on  the  scenario.  The  verified
gross mass of a packed container should be provided to the next party taking custody
of the container.

Several use cases/processes are supported in SAP TM.

139


## Air Freight Bookings

Like  ocean  freight  bookings,  air  freight  bookings  can  be  created  in  TM  as  capacity
reservations  with airline carriers. During transportation planning, they can be used as
capacities.  Before being shipped, air freight may be consolidated in one of two ways:
gateway consolidation and business unit consolidation.

## Gateway Consolidation

In the gateway consolidation scenario, the gateway (freight forwarder) receives freight
from several business units or stations. The gateway is responsible for flight planning,
capacity  management,  (de)consolidation,  MAWB  (Master  Air  Waybill)  creation,  and
communicating  directly  with  the  air  carrier.  The  gateway  is  also  responsible  for
transfers  to/from  the  airport.  The  business  units  consume  the  gateway's  booking
capacity. A business unit issues a HAWB (House Air Waybill) to the MAWB maintained
at the gateway. As the gateway receives cargo from different business units, multiple
HAWBs (forwarding orders) may be issued to one MAWB (air freight booking).

## Business Unit Consolidation

With  business  unit  consolidation,  the  business  units  have  direct  customer
relationships  and  are  consolidating  cargo  from  multiple  shippers.  This  might  also
include  cargo  from  other  business  units.  The  business  unit  is  responsible  for  flight
planning,  capacity  management,  consolidation,  MAWB  creation,  and  communicating

140


directly  with  the  air  carrier.  No  gateway  is  involved  (for  export  or  import)  in  this
scenario.  The  MAWB  is  the  airfreight  booking  in  TM,  and  the  HAWB  represents  a
forwarding order. In this scenario, the business unit issues both the HAWB and MAWB.
In an internal co-load scenario, a booking (air or ocean) arranged by a certain business
unit  (BU1)  is  used  by  a  separate,  independent  business  unit  (BU2)  to  ship  their
forwarding orders. The cargo (forwarding orders) of BU2 is co-loaded on the air freight
booking of BU1.

141


Lesson 7 - Selecting Carriers and Tendering

## Objectives

After completing this lesson, you will be able to:

●  Explain the carrier selection process.
●  Assign carriers to freight orders and freight bookings.
●  Tender freight orders.
●  Explain freight collaboration through SAP Business Network for Logistics.

## Carrier Selection Process

Once  a  freight  order  has  been  created,  a  shipper  must  choose  (and  communicate
with) the business partner responsible for moving the product. We will refer to this as
carrier selection.

The  carrier  is  the  business  partner  to  whom  you  subcontract  the  freight  order.  The
carrier  can  be  different  from  the executing carrier, which is another business partner
role  that  you  can  assign  to  your  freight  order  if  the  carrier  itself  subcontracts  the
execution of the freight order to a third party. That way, you can differentiate between
the party you contracted with and those executing the freight move.

142


## Carrier Selection

Carrier selection is used to assign a suitable carrier to your subcontractable business
documents  (for  example,  freight  or  consignment  orders)  manually  or  automatically.
The  aim  is  to  find  a  carrier  with  the  lowest costs under consideration of the defined
constraints.

In manual carrier selection, you manually assign the required carrier to your business
documents.  If  you  have  configured  a  check  against  transportation  allocations,  the
system  considers  this  and  checks  the  transportation  capacities  (transportation
allocations)  you  have  defined  for  the  individual  carriers.  If,  during  the  allocation,  the
system finds relevant transportation allocations without capacity or that specific rules
are violated by the allocation, warning messages appear.

A  separate  optimization  is  available  for  automatic  carrier  selection.  It  considers
selected optimization options when determining the most cost-effective carrier for all
business  documents  you  have  chosen.  If  no  carriers  are  available,  the  system  does
not assign any carrier to the relevant business documents.

## Strategy Options

The  system  takes  strategies  into  account  during  the  automatic  carrier  selection
process.  You  define  strategies  either  in  the transportation lane or in carrier selection
settings.  Initially,  the  system  considers  the  appropriate  transportation  lane  for  each
freight  order.  This  allows  it  to  consider  different  settings  in  one  run.  Considering
strategies and settings, the optimizer then creates a carrier ranking list containing the
different carrier options.  The strategy options supported are as follows:

143


●  Cost and Priority
●  Business Share
●  Transportation Allocation
●  Continuous Move

## Costs and Priorities in Carrier Selection

In carrying out carrier selection, the system can put more weight on priorities or costs.
In  terms  of  priority,  the  system  can  determine  the  most  favorable  carrier  based  on
your  defined  priorities.  In effect, this means that the system chooses the carrier with
the  highest  priority  while  considering  the  various  restrictions  that  may  be  in  place.
Alternatively,  the  system  can  determine  the carrier based on the lowest total cost. In
this  case,  costs  can  refer  to  internal  costs  or  charges  calculated  in  charge
management.

## Carrier Selection Settings

The  relevant  constraints  for  the  carrier  selection  process  are  defined  in  the  carrier
selection  settings  of  the  planning  profile.  Some  of  the  decisions  taken  in  the  carrier
selection  settings  can  be  delegated  to  the  relevant  transportation  lanes  if  decisions
should  not  be  taken  globally  but  are  different  for  some  geographical  regions.  The
options  selected  here  include  strategies  such  as  lowest  cost,  business  share,  and
priority.  Carrier  selection  can  consider  continuous  move  options  and  equipment
allocations and can tender automatically based on the tendering strategy.

## Business Share

Formalized firm relationships often exist with carriers in the form of contracts. These
contracts  can  guarantee  an  amount  of  business  to  be  allocated  to  a  carrier.  If  the
required  allocation  is  not  met,  penalties  may  result.  TM  has  the  tools  to track these
relationships  and  to  divide  business  appropriately  between  different  carriers.  This
avoids dependency on a single vendor. The idea is to use a fixed percentage to dictate
the assignment of jobs to specific carriers. When generating assignments, the system
can  also  consider  a  carrier's  capacity  concerning  specific  routes  or  geographical
areas.

When defining the business share context, you create business share buckets. These
define  the  actual  business  share  a  carrier  is  allowed  to  have.  Different  buckets  are
available for business share creation - yearly, quarterly, monthly, weekly, and daily.

You  can  define  tolerances  and  penalty  costs  concerning  business  share.  As long as
the business share for a specific carrier is within the tolerance limits, it does not affect
the cost calculations during carrier ranking. However, penalties start to apply once the

144


share  allocation  goes  beyond  a  defined  level.  Tolerances  are  always  defined  in
percentage  terms.  Penalties  are  maintained  as  numeric  values.  This  number  (the
penalty)  is  multiplied  by  the  deviation  percentage  (the  amount  outside  the  defined
tolerance range) to arrive at the penalty cost.

## Note

If  you  are  working  with  carriers  from  multiple  geographic  locations  with  multiple
currencies,  the  system  uses the internal common currency (maintained in the carrier
selection  settings)  for  its  calculations  to  arrive  at  the  correct  ranking.  The  currency
displayed in the carrier ranking list is always the local currency of the carrier (the one
maintained in the freight agreement).

All  freight  orders  in  a  business  share  context  are  selected  for  the  business  share
penalty calculations, although these freight orders are not selected during the planning
run.

## Business Examples

●  Carrier A has a weekly bucket equating to 75% of the business share on the

lane between Hamburg and Frankfurt between the validity period 03.01.2025 to
31.12.2025. In the same context, Carrier B can have a defined weekly bucket of
25%.

●  A penalty of 1,000 is defined. An excess tolerance of 10% is also specified.

During business share calculation, if the excess is 12%, the excess liable for
penalty is 2%. This 2 is multiplied by 1,000 to arrive at the total excess penalty
cost of 2,000.

●  Assume that we have two carriers in a business share context: A and B. No
tolerances have been defined. Carrier A is awarded 60%, and carrier B 40%.
There are already ten freight orders awarded, of which carrier A is assigned six
and carrier B is assigned 4. Now, let’s perform carrier selection for an 11th
freight order. If carrier B is assigned this FO, carrier A will have a shortfall of
business share. If the freight order is assigned to carrier A, carrier B will have a
shortfall of business shares. Both options are evaluated by the system and
ranked according to their suitability.

## Allocation

Transportation  allocations  allow  companies  to  assign  defined  capacity  quantities  to
certain  business  partners.  This
includes  set  minimum  or  maximum  capacity
restrictions  that  regulate  how  much business is permitted with a specific carrier in a
particular region for a certain means of transport. A separate business object is used
to model these allocations.

145


Carrier Selection

## Carrier Selection

When using automatic carrier selection, the system will create a carrier ranking list of
the  relevant  carriers  for  a  particular  freight  order/freight  booking.  Users  can  see
various  information  that  influenced  the  selection  process  for  each  relevant  carrier.
This  could  include  the  means  of  transport  cost,  delivery  performance  ratings,  and
others.  After  automatic  carrier  selection,  the  ranking  list  will  be  visible  in  the  freight
order.

## Status Management in Subcontracting

The figure shows which statuses change during the subcontracting process.

146


## Tendering

Once carrier selection has taken place, communication with the selected carrier must
be  initiated.  This  process  is  referred  to  as  order  tendering.  Different  tendering
processes  can  be  deployed  depending  upon  the  technology  used  by the carrier. You
use  this  process  to  tender  (offer)  a  freight  order  to  one  or  more  potential  carriers.
Tendering is a bidding process, in which you request one or multiple carriers to submit
a  quote  for  a  transportation  service  that  is  defined  in  a freight order. You can select
the  carrier  that  you  want  to  execute  the  transportation  service  by  evaluating  the
quotes.  The  main  characteristics  of  the  tendering  process  are  flexible  configuration
and  the  reduction  of  required  manual  interaction  to  support  ease-of-use  and  lower
total cost of ownership (TCO).

147


In  general,  there  are  two  types  of  tendering.  Long-term  tendering is where contracts
are  negotiated  for  a  longer  period,  for  example,  a  year.  Long-term  tendering  is  a
process that is covered in strategic freight management, which is also a functionality
of  TM,  but  not  covered  here.  Short-term  tendering  is  where  tendering  is  executed
based on specific orders. This is known as order tendering. TM supports the following
short-term tendering scenarios:

●  Peer-to-Peer Tendering
●  Broadcast Tendering

The strategies for each are determined in tendering profiles in TM.

## Parties and Roles in the Tendering Process

At  least  two parties are involved in the tendering process - a customer who wants to
subcontract a transportation service that is defined in a freight order, and a supplier or
carrier,  who  potentially  carries  out  the  transportation  service. There are two roles on
the  customer  side  of  the  tendering  process.  The  first  is  a  transportation  dispatcher,
who is responsible for the transportation service, that is, the freight order. The second
is  the  tendering  manager,  who  is  responsible  for  configuring  and  executing  the
tendering  process  and  acquiring  an  acceptable  quote  from  a  carrier  to  perform  the
transportation service.

## Manual and Automatic Tendering

When  a  transportation  dispatcher  initiates  the  tendering  process,  they  have  two
options:  manual  process  configuration or automatic tendering. If they want to tender
only a single freight order, the transportation dispatcher can choose between the two
options. If they initiate a tendering process using manual configuration, the tendering
manager  must  configure  and  start  the  tendering  process  manually.
If  the
transportation  dispatcher  wants  to  tender  more  than  one  freight  order,  they  must
initiate  automatic  tendering  and  use  the  automatic  tendering  configuration  in  the
system.

Peer-to-Peer and Broadcast Tendering

148


Peer-to-peer tendering is a process whereby freight orders are tendered sequentially or
"offered"  to  preselected  carriers.  Peer-to-peer  tendering  involves  the  sequential
sending of freight requests for quotation (freight RFQs) to each proposed carrier. The
system  waits  until  the  carrier  sends  a  freight  quotation  (FQ),  or  until  the  maximum
response  time  has  passed.  If  the carrier does not send a quote within the maximum
response time, the peer-to-peer tendering process continues, and the system sends a
request  for  quote  to  the  next  carrier.  If  peer-to-peer  tendering  ends  without  an
acceptable  quote,  the  tendering  process  continues  with  the  next  tendering  process
step  that  you  have  configured.  If  the  carrier  sends  a  quote  before  the  maximum
response  time  has  elapsed, the system evaluates the quote and can either accept or
reject it. In the case of rejection, a new RFQ is sent out. The process continues until at
least  one  acceptable  FQ  has  been  received.  The  system  awards  this  a  Quotation
Acceptable  evaluation  result  and  the process ends successfully. There are two types
of peer-to-peer tendering: response required and no response required.

## Broadcast Tendering

Broadcast  tendering  is  a  tender  process  whereby  freight  orders  are  simultaneously
tendered  (offered)  to  preselected  carriers.  All  carriers have to respond within a given
maximum  response time. There are two types of broadcast tendering: best offer and
first  acceptable  offer.  Depending  on which one of these is being used, either the first
acceptable quote wins or, after the maximum response time, the system evaluates all
the  acceptable  quotes  and  selects  the  carrier  that  has  submitted the quote with the
lowest  price.  If  broadcast  tendering  ends without an acceptable quote, the tendering
process continues with the next tendering process step that you have configured.

149


Freight Collaboration with SAP BN4L

## Tendering Profiles

The tendering profile contains basic tendering data and is a prerequisite for automatic
tendering. You can use a tendering profile when you manually create a tendering plan.
Within  the  profile, you can define multi-step tendering. This allows a company to mix
tendering  types.  For  example,  you  can  first  use  peer-to-peer  tendering,  and  if  this  is
unsuccessful  you  can  use  broadcast  tendering.  In  a  tendering  profile, you can make
settings in relation to the following options:

●  Choose from tendering types — peer-to-peer, broadcasting (best offer, first

acceptable offer)

●  Choose from tendering processes — direct or RFQ-based
●  Choose fully or semi-automatically rules-based tendering (response time and

price limits, automatic retendering)

●  Configure the tendering process and RFQ publishing
●  Set up web-based, e-mail, B2B tendering communication
●  Set up authorization-based RFQ processing and data visibility (carrier

authorization to change the price and delivery dates, view tender price limit,
stop date and rejection code reasons, support of free text and attachments)

●  Make settings in relation to currency

## Communication Methods

There are several communication methods that support the tendering scenarios. First,
SAP  S/4HANA  Transportation  Management  natively  supports  e-mail.  Requests  for
quotation (RFQs) can be received by e-mail and quotations can be submitted without
the  need  to  access  a  TM  system  at  all.  In  this  case,  an  RFQ  is  sent  to  a  carrier  by
e-mail  message.  The  carrier  responds to the e-mail using a regular e-mail client on a
PC or mobile device. The e-mail is then converted (using PI) into a quotation. Carriers
can  accept  RFQs  directly,  reject  them  with  a  specified  reason  or  accept  them  with
changes.

If  a  subcontractor  is  more  technically  advanced,  EDI  (electronic  data  interchange)
message  communication  can  be used. In this situation, a copy of the freight order is
created  for  the  carrier  (the  tendering  manager  or  system  administrator  can  control
what is included in the copy that is visible to the carrier). The copy is persisted in the
system  to  retain  what  was  communicated  to  the  carrier.  A  freight  request  for
quotation (tendering request) is sent via PI and received as a forwarding quotation in
the supplier’s TM system. The carrier can accept the order directly or, if the first carrier
rejects  the  order,  the  freight  order  will  be  sent  to the next carrier. Finally, a quotation
confirmation is sent back to the customer and is converted into a quotation (tendering

150


response) in the customer’s TM system. The change controller allows you to react to
changes in the FO, for example, by stopping tendering when there are major changes
in the FO.

In  addition,  SAP  offers  SAP  Business  Network,  a  cloud  service  with  global  coverage
built  to  connect  logistics  business  partners;  to  collaborate  across  companies  and
jointly manage transactions, exchange documents and data, and share insights.

SAP  Business  Network  Freight  Collaboration  supports  end-to-end  collaboration  in
logistics  processes  from  contracting to settlement. It also allows carriers to respond
to tendering requests for quotation (broadcast or direct tendering) and process freight
orders through web portal applications or integrate via API to process freight orders in
their frontend of choice. Each carrier in the network is provided with their own user IDs
and  passwords,  and  the  relevant  authorizations  to  restrict  visibility  to  the  loads  that
have been tendered to them.

While  the  standard  web  portal  applications  in  SAP  Business  Network  Freight
Collaboration  are  delivered  by  SAP  and  can  be  used  out  of  the  box,  the  use  of  API
requires custom integration.

With  regards  to  tendering,  the  process  works  as  follows.  The  request  for  quotation
(RFQ)  message  is  triggered  from  the  shipper’s  TM  system.  Post  receiving  the
message  and  persisting  the  request  for  quotation  in  SAP  Business  Network  Freight
Collaboration,  the  RFQ  is  sent  to  one  or  more  carriers.  The  carriers  respond  to  the
tendering  and  the  quotation  is  sent  back  to  the  shipper’s  TM  system.  Award
notifications are again distributed via SAP Business Network Freight Collaboration.

If  shippers  work with several carriers through SAP Business Network, they only must
integrate  once  to  collaborate  across  the  logistics  processes  and  share  their  freight
orders,  requests  for  quotation,  freight  bookings,  freight  documents  for  invoicing,  …

151


with  their  network.  This  simplifies  an  otherwise  tedious  process  of  integrating  with
each carrier individually.

152


Lesson 8 - Creating Service Orders

## Objective

After  completing  this  lesson,  you  will  be  able  to  create  service  orders  relevant  to  the
transportation of goods and materials.

## Service Items and Service Orders

Cleaning  containers,  fumigating,  and  performing  security  services  or  documentation
are  typical  examples  of  services that can occur for items of a freight order or freight
booking. Depending on whether the carrier selected in the freight document or a third
party is tasked with the execution of the service, the service is either added as an item
to the freight document or created as a separate service order.

In the first scenario, one or more service items are added in the item hierarchy of the
freight  order  or  freight  booking.  Service  items  can  be added on any level of the item
hierarchy  depending  on  the  item,  the  service  relates  to.  For  example,  a  fumigation
service  would  relate  to  a  container  and  therefore  added  underneath  the  container
position,  whereas  a  labeling  service  would  be  added  on  package  or  product  level
depending on what has to be labeled. In this case, the service is executed by the same
carrier, that the freight order of freight booking is subcontracted to.

The  service  order  is  used  to  account  for  and  track  services,  calculate  charges,  and
enable  settlement  of  the  charges  for  services  that  have  been  provided for individual
items  in  a  freight  document  or  for  the  entire  freight document, if a third party (other
than the carrier of the freight document) is tasked with the execution of the services.

You can create service orders in the following two ways:

153


●  Create service orders from freight documents or freight document items. With

such a service order, you can:

○  Enter service items related to the freight booking, freight order, freight

booking item, or freight order item.

○  Add service items that are not related to the freight booking, freight

order, freight booking item, or freight order item. You can do this using
the Add Service action without marking another item.

●  Create standalone service orders without reference to any freight document or
freight document item. You can use the Create Service Order function to create
a service order by entering the service order type.

## Structure of Service Order

A service order contains the following information:

●  General data including the service provider, service order type, and status of the

service order

●  An item overview that contains the following information:

○

○  Link to the freight booking or freight order for which the service order
was created. (Applies only for service orders created from freight
bookings, freight orders, freight booking items, or freight order items).
IDs of the original freight booking items or freight order items for which
services are to be carried out, for example, containers or products.
(Applies only for service orders created from freight bookings, freight
orders, freight booking items, or freight order items).

○  Services to be carried out.
○  The location at which the services are to be executed and the time

period in which they are to be executed.

●  Transportation charges
●  Document dependencies, predecessor, and successor documents (document

flow)

●  Other information such as the following:

○  Notes
○  Attachments
○  Change documents
○  Administrative data
○  Output management information

154


Unit 7 - Monitoring Transportation Execution

Lesson 1 - Creating Deliveries

## Objectives

After completing this lesson, you will be able to:

●  Create deliveries and integrate them into the transportation process.
●  Explain the options for delivery integration.

Overview of Monitoring Transportation Execution

Transcript for video:

“In  today's  complex  supply  chains,  effective  monitoring  of  transportation  processes  is
crucial  for  maintaining  efficiency,  reducing  costs,  and  ensuring  customer  satisfaction.
This  unit  focuses  on  the  critical  phase  where  planned  transportation  activities  are  put
into  action.  We'll  explore  how  to  seamlessly  transition  from  planning  to execution, and
how  to  maintain  visibility  and  control  throughout  the  process.  We'll  examine  delivery
management  as  the  bridge  between order fulfillment and transportation execution, and
how  it  integrates  with  warehouse  operations.  You'll  learn  about  managing  loading  and
unloading operations, critical touchpoints that impact overall supply chain visibility. Clear,
timely  documentation  is  essential  in  transportation,  so  we'll  cover  generating  and
managing  various  outputs  to  ensure  all  stakeholders  have  the  information  they  need.
into  real-time  monitoring  and  exception
Perhaps  most
management,  leveraging  event  management  systems  and  global  track  and  trace
capabilities  to  keep  your  operations  running  smoothly.  Throughout  this  unit,  you'll gain
practical  insights  into  creating  a  robust  transportation  execution  monitoring  system.
Whether you're dealing with local deliveries or global shipments, the principles and tools
we'll discuss will help you optimize your transportation processes, improve visibility, and
ultimately deliver better service to your customers. Enjoy learning with SAP!”

importantly,  we'll  delve

## Delivery Creation

The delivery document controls, supports, and monitors numerous sub-processes for
shipment processing, such as picking, packing, loading, and posting the goods issue.
In  addition,  the delivery document can be used as a reference document for creating
other shipment documents, such as a bill of lading.

155


Outbound  and  inbound  deliveries  are  created  in  SAP  S/4HANA  or  SAP  ERP.  In  a
side-by-side  scenario,  they  are  integrated  into  TM  and  stored  as  delivery-based
transportation requirements. They can act as a starting point for TM processes or be
created during transportation. A delivery document can be created in SAP ERP / SAP
S/4HANA or TM.

## Triggered in SAP ERP / SAP S/4HANA

When the delivery is created and considered relevant for transportation management,
it triggers the creation of a freight unit. In a side-by-side scenario, the delivery is sent to
TM as a Delivery-Based Transportation Requirement (DTR).

## Triggered in TM

The second scenario is one in which the creation of deliveries is triggered from TM, for
example,  based  on transportation planning performed in TM. This solution offers the
possibility  of  combining  and  planning  multiple  orders  in  TM  and  creating  a  single
delivery and transport.

156


## Delivery Creation Triggered in TM

TM can generate proposals for delivery creation in SAP ERP / SAP S/4HANA based on
dates  and  quantities  according  to  transportation  planning  results  and  considering
transportation  constraints  such  as  resource availability and transportation durations.
TM  can  also trigger the creation of deliveries before transportation planning. TM can
send these proposals to SAP ERP / SAP S/4HANA to trigger the creation of deliveries.

After the delivery proposals have been created and sent to SAP ERP / SAP S/4HANA,
the  system  creates  an  entry in the application log. The application log entry includes
the  delivery  proposals  sent  to  SAP  ERP  /  SAP  S/4HANA  (in  side-by-side  scenarios).
Furthermore,  the freight units for which a delivery proposal is sent to SAP ERP / SAP
S/4HANA are marked with a send timestamp.

SAP ERP / SAP S/4HANA creates the deliveries when it receives the request to do so.
SAP ERP / SAP S/4HANA may split the proposed deliveries further, for example, based
on  additional  split  criteria.  However,  SAP  ERP  /  SAP  S/4HANA  will  not  change  TM's
proposed  dates  nor  consolidate  proposed  deliveries.  Once  the  deliveries  have  been
created, SAP ERP / SAP S/4HANA sends a confirmation to TM and a request to create
a delivery-based transportation requirement in TM.

TM  creates  an  entry  in  the  application  log.  The  application  log  entry  includes  the
system  messages  created  in  SAP  ERP  /  SAP  S/4HANA  during  delivery  creation and

157


the numbers and document IDs of deliveries created in SAP ERP / SAP S/4HANA. TM
generates an alert if an error occurs during SAP ERP / SAP S/4HANA delivery creation.
When  a  confirmation  is  received,  TM  sets  a  confirmation  timestamp  in  the  relevant
freight  units.  The  timestamp  monitors  whether  SAP  ERP  /  SAP  S/4HANA  has
responded.

## Note

For  error-handling  purposes,  the  following  two  additional  worklists  are  available  (in
side-by-side scenarios):

●  One for all OTRs for which delivery creation has been triggered but no response

has arrived from SAP ERP / SAP S/4HANA

●  One for all OTRs for which delivery creation has been triggered and the

confirmation has arrived from SAP ERP / SAP S/4HANA, but for which an error
occurred during delivery creation (and for which the delivery creation must be
triggered again)

Methods for Delivery Creation

●  Background Report
●

Interactive Delivery Creation

Background Report

(report
Delivery  proposals  can  be  created  using  a  background
/SCMTMS/DLV_BATCH).  The  user  can  enter  selection  criteria  or  use  a  selection
profile. In both cases, the user can also enter a delivery profile. Delivery profiles include
settings for delivery creation. The system selects the documents, creates the delivery
proposals, and sends them to SAP ERP / SAP S/4HANA (in a side-by-side scenario).

report

Interactive Delivery Creation

●

Input Selection with Profiles Using the Delivery Builder App:
The user specifies one or more profiles according to which the system selects
and displays a list of documents. The user can then select the relevant
documents in the list and trigger the creation of a delivery proposal. The user
can review the delivery proposals before processing them.

●  For Specific Documents:

The user can trigger delivery creation for specific business documents from
worklists. The system automatically processes the proposals to create
deliveries. It also displays the proposals before sending them. The following are
worklists from which delivery creation can be triggered:

158


○  OTR Worklist
○  Freight Unit Worklist
○  Freight Order Worklist
○  Ocean/Air Freight Booking Worklist

●  The user can also trigger the creation and sending of delivery proposals for a

specific freight order in the freight order UI.

●  After Planning:

The user can trigger delivery creation for specific documents after planning in
the transportation cockpit. The system displays the delivery proposals, which
users can review before processing.

## Data Sources

TM  considers  data  for  delivery  creation  from  the  order  /  order-based  transportation
requirements  and  the  assigned  freight  units,  freight  orders,  and  freight  bookings.
Based  on  the  chosen  input,  TM  creates  delivery  proposals.  A  proposal  consists  of
groups of freight units that can be delivered together.

Data Collected by TM

●  Dates:

TM uses dates from the freight order or freight booking. If the freight unit is not
planned, no freight order or freight booking exists, and then TM uses dates
from the freight units.

●  Quantities:

TM uses quantities from the freight units.

●  SAP ERP Document References:

TM retrieves document references (such as order document number) from the
order / order-based transportation requirement.

## Consolidation

If  order-based  freight  units have been planned, and freight orders or freight bookings
exist  for  the  transportation  demands,  TM  uses  only  one  freight  order  or  one  freight
booking  for  each  delivery  proposal.  Only  freight  units  from the same freight order or
freight  booking  can  be  consolidated  into  a  single  delivery proposal. This way, freight
units  from  various  order-based  transportation  demands  can  be  consolidated  into  a
single  delivery  proposal  if  they  belong  to  the  same  freight  order  or  freight  booking.
Suppose freight units from a single order-based transportation demand are distributed
across  multiple freight orders or freight bookings. In that case, multiple deliveries are
proposed for the freight units of this one order-based transportation demand.

159


If  order  combination  is  not  allowed  for  an  order-based  transportation  demand,  TM
does  not  group  freight  units  from  this  transportation  demand  together  with  freight
units from other order-based transportation demands. Suppose freight units for such
order-based  transportation  demands  have  been  consolidated  into  the  same  freight
order or freight booking during planning. In that case, TM does not include them in the
same delivery proposal but creates multiple delivery proposals instead.

In  addition,  freight  units  can  only  be  consolidated  into  the  same  delivery  proposal if
the following data is the same:

●  SAP ERP system from which the order was received (only in side-by-side

Incoterms

scenarios)
●  Source location
●  Destination location
●
●  Shipping conditions
●  SAP ERP document type, such as purchase order or sales order
●  Start stop (if planning has already been done)
●  Destination stop (if planning has already been done)

## Order- or Delivery-Based Transportation Process

The  decision  about  whether  to  start  the  transportation  process  with  either  the  ERP
order  or  the  ERP  delivery  depends  on  the  customer  requirements  and  guidelines
concerning  transportation  planning  and  execution.  If  shipping  activities  other  than
transportation  planning  are  involved  before  the  transportation  process,  the  process
based  on  the  ERP  delivery  is  more  likely  to  be  used.  The  ERP  order  is  the  basis  for
transportation planning if goods are sold with all shipping activities considered.

There is no significant difference to subsequent process steps on whether an OTR or
DTR  (in  side-by-side  scenarios)  or  order-  or  delivery-based  freight  units  (in  an
embedded  scenario)  are  used  as  a  starting  point.  There  is  no  difference  in  the
continuation  of  the  process  between  transportation  requirements  based  on  an  ERP
order and those based on ERP deliveries.

## Delivery Change and Split

Delivery  updates  can  be  triggered  from  SAP  ERP  /  SAP  S/4HANA  and  TM.  Updates
from TM are based on planning changes.

160


If a delivery is changed or deleted, this information is sent to TM. The freight units are
adjusted  according  to  the  changes.  If  the  delivery  quantity  has  changed,  the  freight
units are adjusted.

You can also update the goods issue date, loading date, transportation start date, and
delivery  date  in  the  outbound  delivery  based  on  changed  planning  dates  in  TM. You
perform  planning  or  change  the  existing  freight  unit planning based on an outbound
delivery. Alternatively, you can change the dates of the relevant freight order. When you
save the planning results or the changed freight order, TM determines that the dates in
the freight order no longer match the dates in the original delivery.

TM  determines  whether  the  delivery  can  still  be  changed  by  checking  the  delivery
status.  If  the  delivery  can  be  changed,  TM  sends  the  changed dates and request an
update  on  the  outbound  delivery.  Note  that  TM  can  trigger  the  update  of  outbound
deliveries only. It cannot trigger the update of inbound deliveries.

Delivery  splits  can  be  triggered  from  SAP  ERP  /  SAP  S/4HANA  and  TM.  Splits
triggered from TM are based on planning changes.

161


A delivery that has already been sent to TM and created freight units can be split next.
Afterward,  there  are  two  deliveries:  the  changed  original  one  and  the  new  one.  The
changed original delivery updates its freight units. A new delivery has been created for
the  items  split  from  the  original  delivery.  New  freight  unit(s)  will  be  created  for  this
new delivery.

Technically,  TM  first  creates  the  new  freight  unit(s)  by  reassigning  the  freight  units
from the original delivery to the new delivery. It then updates the freight units from the
original delivery. The system determines the required changes to freight unit planning
for the freight units assigned to both deliveries. After reassigning the freight units, the
system  must  determine  whether  the  planning  of  the  freight  units  in  the  new  or  the
original delivery is to be discarded or kept.

You  can  split  an  outbound  delivery  based  on  planning  changes  in  TM.  You  perform
planning  or  change  the  existing  freight  unit  planning based on an outbound delivery.
When  you  save  the  planning  results,  the  system  determines  that  a  delivery  split  is
required.  For  example,  freight  units  that  belong  to  the  same  delivery  have  been
assigned  to  different freight orders, or only some of the freight units that belong to a
delivery  have  been  assigned  to  freight  orders.  The  other  freight  units  have  not  been
assigned.  Note  that  the  split  is  required  only  if  the  transportation chain's first or last
stage is affected.

TM  determines  whether  the  delivery  can  still  be  changed  by  checking  the  delivery
status.  If  the  delivery  can  be  changed,  a  new  outbound  delivery  is  created,  and  the

162


original  outbound  delivery  is  adapted  (that  is,  it removes the relevant items from the
original delivery and creates a new delivery for these items).

163


Lesson 2 - Integrating into Warehouse Processes

## Objectives

After completing this lesson, you will be able to:

●  Explain how the transportation process integrates with warehouse processes.
●  Understand the options to integrate into warehousing processes.
●  Understand the advanced shipping and receiving process.

## Warehouse Integration

With  SAP  S/4HANA,  there  are  various  ways  to  model  the  execution  process.  This
depends  on  the  complexity  of  your  warehouse  processes.  SAP  offers  solutions  for
warehouse  execution,  from  simple  (none)  warehouse  processes  to  full-scale
warehouse  setups.  All  of  them  are  integrated  via  the  delivery  to  SAP Transportation
Management.

Ways to Handle Stock

## Inventory Management
Inventory Management with Handling Unit Management

●
●
●  Stockroom Management (former LE-WM)
●  Extended Warehouse Management (SAP EWM)

## Warehouse Integration Options

The most straightforward way to model a process for transport execution is without a
dedicated  warehouse  setup.  Therefore,  the  transportation  demand  represents  the
delivery  in  logistics  execution.  This  leads  to  a  freight  unit  that  can  be  planned  on  a
freight order, and the transportation execution can be started.

164


## Inventory Management

Note  that  Handling  Unit  Management (HUM) is optional and could be used to create
deliveries with handling units or take care of the items themselves, for example, if you
want  to  model  a  lean process and do not have to take care of which item is shipped
on what load carrier system-wise.

## Stockroom Management

For small to medium warehouse setups, there is an option available called Stockroom
Management.  Stockroom  Management is integrated directly into the LE Delivery, and
the  warehouse  transportation  orders  are  triggered  as  a  subsequent  task  to  the  LE
predecessor documents.

Stockroom  Management  is  a  specific  offering  for  installed  base  customers  to
continue running their light warehouse management implementation in the context of
SAP  S/4HANA.  The  license  is included in the SAP S/4HANA Enterprise Management
component.

The main reason for creating the Stockroom Management offering is to allow existing
LE-WM  customers  to  keep  these  warehouses  untouched,  which  do  not  benefit
immediately  from  moving  to  embedded  EWM.  Stock  room  management  is  the  ECC
warehouse  management  component  (LE-WM)  without  capabilities  supporting  more

165


complex  warehouses.  It  is  relevant  for  small  warehouses  with  manual  operations
(storage bin management).

:  No  innovations  are  planned  in  stockroom  management,  and  extended  warehouse
management remains the strategic product.

## SAP Extended Warehouse Management

SAP Extended Warehouse Management (EWM) is designed to fulfill the requirements
of  complex  warehouse  setups,  including  requirements  such  as  automated  guided
vehicles (AGVs), complex conveyor techniques, and high turn-over.

There are two ways to integrate TM and EWM:

TM and EWM Integration Methods

Integration Method

Basic License

Advanced
## License

Based  on  Freight  Orders  -  Advanced  Shipping
and Receiving (ASR)

Based  on  Transportation  Units  -  Extended
Warehouse Management (EWM)

166


The  process  based on advanced shipping and receiving (integration based on freight
orders,  starts  with  the  creation  of  the  LE  delivery,  which  is  propagated  to  EWM  (to
create  an  outbound  delivery  order)  and  TM  (to  create  a  freight  unit).  Depending  on
whether  the  process
is  transportation-driven  or  warehouse-driven,  one  of  the
documents will be blocked until the other application has finished its process.

Extended Warehouse Management (Advanced)

There  is  also  an  advanced  integration  between  SAP  EWM  and  TM  that  requires  an
advanced  license.  In  this  scenario,  you  use  more  planning  capabilities  by  creating
deliveries  already  on  a  plan  made  based  on  sales  orders  in  TM  and  handing  over  a
load  plan  from  your  TMS  system  to  the  WMS  system  for  execution.  Therefore,  the
transportation  unit  is  needed in SAP EWM. The transportation unit in this scenario is
created based on the Freight Order in TM.

167


Classic TM-EWM Integration based on Transportation Units

In TM, you can plan your transportation activities based on an outbound delivery and
send  your  freight  orders  to  SAP  EWM.  In  SAP  EWM,  you  can  carry  out  the  steps
relating  to  the  warehouse,  such  as  loading.  Because  the  two  systems  are  directly
integrated,  TM  informs you that the truck in SAP EWM has been loaded and whether
there are any discrepancies, such as quantity deviations.

168


The  main  steps  of  an outbound process based on the classical TM-EWM integration
based on transportation units are described as follows. The description assumes that
there  is  only  one  transportation  stop.  If  your  freight  order  comprises  several
transportation  stops,  the  process  is  repeated  for  each  stop  if  the  stop  contains
loading  locations  relevant  to  SAP  EWM.  Note,  however,  that  multiple  pickup  and
multiple delivery scenarios are not supported:

1.  You create a sales order in SD.
2.  Freight units get created, transportation is planned, and freight orders are

created in TM.

3.  When transportation planning is based on sales orders, you trigger delivery

creation from TM.

4.  You create outbound deliveries in SAP S/4HANA and send them to TM and
EWM. In TM, a delivery-based transportation requirement is automatically
created along with the associated freight units. EWM creates an outbound
delivery request and an outbound delivery order automatically.

5.  You set the load plan status of the freight order to Load Plan Finalized. TM
automatically sends a loading instruction to EWM with the message
LoadingAppointmentRequest.

169


6.  When the LoadingAppointmentRequest message is received from TM, EWM
automatically creates a transportation unit, and the outbound delivery orders
are assigned to the TU activity.

7.  Perform the warehouse activities related to the outbound delivery orders, such
as picking, packing, staging, and loading the goods. The system can create
handling units automatically. All warehouse activities except loading can be
performed before the TU arrives at the door.

8.  The warehouse workers post the goods issue (optional).
9.  The warehouse workers post the departure of the truck. EWM sends the
LoadingAppointmentNotification message to TM. At the same time, the
outbound delivery is automatically updated in ERP.

10. When the data is updated in ERP, the delivery-based transportation requirement

is automatically updated in TM.

11. When the LoadingAppointmentNotification message is received, TM updates
the freight order and sets the execution status to In Execution. The cargo
receipt status at the item level is automatically set to Shipped. If the item is to
be unloaded at the next transportation stop, the handling execution status is
automatically set to Not Unloaded. The system also updates the associated
freight units.

12. You complete freight order execution.

## Advanced Shipping and Receiving

The  objective  of  Advanced  Shipping  and  Receiving  is  to  ensure  suppliers  and
customers  can  access  the  same  data  in  their  systems,  using  standardized  data
structures and facilitating communication through EDI messages. One of the essential
EDI  messages  is  the  advanced  shipping  notification  (ASN),  which  provides  detailed
information about upcoming shipments sent by the supplier. Another crucial message
is the bordero, which assists in managing transportation-related documentation and is
usually sent by the carrier. Using both information, the ASN from the supplier and the
bordero from the carrier, the customer has everything he needs to facilitate an efficient
goods receipt process.

Integrating TM and EWM into SAP S/4HANA has improved efficiency and streamlined
operations.  With  Advanced  Shipping  and  Receiving  (ASR),  it  is  possible  to  embed
warehouse  management  functionalities,  allowing  for  seamless  maintenance  of
warehouse  requests  and  handling  units  within  the  freight  order.  Importantly,  this
integration  eliminates  data  redundancies  between  the  old  EWM  transportation  unit
and the transportation management freight order.

A  freight  order  replication  service  achieves  synchronization  between  shipping  and
receiving  and  extended  warehouse  management  in  the  standalone  version.  This

170


service  ensures that the code line remains the same while providing a partial view of
the  freight  order  in  the  Extended  Warehouse Management instance, specific to each
warehouse.

One  significant  advantage  of  ASR  is  the  ability  to  load  and  unload  across  multiple
warehouses.  This  means  you  can  integrate  loading  and  unloading  processes  with
EWM,  stockroom  management  systems,  and  IM-managed warehouses on the same
truck. This consolidation of operations results in faster processing times and reduces
the need for multiple transactions across different warehouses.

Advanced  Shipping  and  Receiving  functionality  also  improves  integration  with
business  partners.  Full  EDI  support
for  consignment  and  bordero,  using
globally-recognized  standards, such as the global DESADV and IFTSTA, is supported.
This  ensures  a  smooth  flow  of  information  throughout  the  transportation  process,
covering every level of truck and shipment. As a result, error handling becomes more
efficient,  and  the  need  for  full  mapping  between  different  systems  is  minimized.
Another  noteworthy  feature  is  the  support  for  multi-pick,  multi-drop  scenarios.
Creating separate business objects for inbound and outbound processes is no longer
required.  Instead,  you  can  have  a  single  freight  order  with  multiple  stops,  allowing
loading  and  unloading  at  the  same  location.  This  optimization  improves  transport
capacity utilization, lowers costs, and enhances efficiency.

171


Two  new  objects  have  been  introduced  to  facilitate  these  advanced  shipping  and
receiving capabilities. The consignment represents a group of freight or deliveries with
the  same  source  and  destination  locations.  On  the  other  hand,  the  loading  point
serves  as  a  shared  master  data  object  for  both  EWM  and  non-EWM  warehouses.  It
enables grouping doors within a warehouse or across different warehouse types, such
as EWM warehouses and stockroom management or IM-based warehouses.

The  consignment,  in  particular,  serves  as  the  basis  for  the  communication  between
suppliers  and  customers,  allowing  for  better  alignment and collaboration throughout
the logistics process. Importantly, the freight order serves as the object to be sent by
the carrier to the customer, with the respective consignment references. With that, the
supplier, customer, and carrier systems have a full data structure.

What  does  the  transportation-driven  process  look  like  based  on  deliveries?  The
starting  point  of  the  process  is  a  sales  order,  or  SD  scheduling  agreement  creation,
and the outbound delivery creation.

The  outbound  delivery  order
is  initially  blocked  for  execution  until  the  entire
transportation  planning  is  done  on  the  TM  side.  This  can  be  done  with  the
transportation cockpit, as well as with the optimizer. With the transportation planning,
the consignment order is created. However, the consignment order is only created as
a  local  consignment  order  because  only  after  the  complete  transportation  planning
and warehouse execution is the consignment order extracted.

172


With  the  status  "Ready  for  Warehousing"  set,  the  outbound  delivery  order in EWM is
unblocked  for  execution.  With  that,  picking,  packing,  and  staging  can  start.  After
setting  the  "Ready  for Shipping" status, the actual package information is sent to the
TM freight unit and freight order.

From  this  point,  truck  check-in  can  be  done  at  the  shipping  point.  The  truck  can  be
docked  to  the  door  at  the  loading  point.  The  EWM  functionality  with  the  RF  loading
can start. After Loading Finished is set, an outbound delivery order could split. In that
case, or at the latest, the automatic consignment order creation must happen.

With the triggering of the goods issue, the warehouse stock goods issue is posted or
performed,  and  there  is  an  update  to  the  freight  unit,  freight  order,  and  the
consignment.

The ASN can be sent based on the consignment order, which is also the same in the
DESADV message. The next process step is that the bill of lading can be printed. The
truck  can  depart  from  the  door  at  the  loading  point,  report checkout at the shipping
point,  and  send  the  freight  order  information  to  the  carrier,  which  then  sends  the
freight order information with the consignment references to the customer so that the
customer has the complete information, the complete data structure.

173


Lesson 3 - Loading and Unloading Freight Orders

## Objective

After completing this lesson, you will be able to load and unload freight orders and post
goods issue.

Loading and Unloading Freight Orders

## Loading and Unloading Freight Orders

As  part  of  the  advanced  shipping  and  receiving  process,  the  Load or Unload Freight
Orders app allows you to process shipping and receiving activities. With this app, you
can:

●  Handle deliveries that are managed in Extended Warehouse Management

(EWM) and Inventory Management

●  Assign or unassign loading points, unloading points, and doors to inbound or

●
●
●
●
●

outbound deliveries
Indicate whether inbound deliveries are ready for warehouse processing
Indicate whether goods arrive at, or depart from, doors
## Indicate whether goods are loaded or unloaded
Indicate whether goods are loaded or entirely unloaded on stop level
Indicate the staging area, staging area group, and staging bay of the goods on
product level and stop level

●  Post a goods issue or a goods receipt
●  Process loading and unloading activities for a single warehouse visit

## Posting Goods Issue and Goods Receipt

The goods issue of an outbound delivery can be triggered as soon as the execution of
a freight order starts. You can use transportation-related events to control and trigger
the  execution  of  goods  movements  automatically.  Goods  issue  for  an  outbound
delivery can only be associated with the execution of a freight order covering the first
stage  of  the  transport.  You  can  control  the  goods  issue  of  a  freight  order  using
transportation-related  events  such  as  Loading  Begin,  Loading  End,  or  Departure.  An
additional  prerequisite  for  posting  goods  issue  is  that  all  delivery  items  that  are
relevant for picking have been picked.

For inbound deliveries, goods receipt can be triggered once the execution of a freight
order  ends.  It  can  be  associated  with  transportation-related  events  like  Arrival  at
Destination,  Unloading Start, or Unloading End. Goods receipt for an inbound delivery

174


can  only  be  related  to  the  execution  of  a  freight  order  covering  the last stage of the
transport.

## Intelligent Goods Receipt

In  Transportation  Management in SAP  S/4HANA  Cloud  Private  Edition,  you  can  use
Document  Information  Extraction  with  generative  AI  technology  to  analyze  delivery
documents attached to a consignment order, extract their header data, item data, and
item reference data, and insert it into a consignment order. This allows you to reduce
manual checks at the gate and improve operational efficiency at goods receipt.

In  TM,  you  upload  your  delivery  documents,  such  as  PDF  documents,  to  a
consignment  order.  If  you  created  a  consignment  order  based  on  an  advanced
shipping  notification  (ASN),  it  might  already  have  the  delivery  documents  attached.
You send your attachments to the extraction service. You can monitor the processing
status  directly  in  Document  Information  Extraction.  Since  Document  Information
Extraction  doesn't  send  success  messages,  you  retrieve  your  extraction  results  by
refreshing  the  consignment  order.  The  system  compares  the  extracted  data  to
existing  data  for  your  consignment  order.  The  data  is  filled  into  your  consignment
order based on the extraction and comparison results. During the process, you might
run into errors. You can view and resolve any document errors related to this process
on  the  Document  Errors  tab  of  the  consignment  order.  Depending  on  the  error
solution, you can continue with the consignment order data or the extracted data. You
have  to  resolve  all  document  errors  before  the  system  can  determine  the  correct
requirement documents to continue.

The  following  steps  describe  in  detail  an  example  process  of  how  to  automatically
process data from delivery documents that are attached to consignment orders:

175


1.  You scan a delivery document and attach it as a PDF document to a

consignment order.

2.  You submit your attachment to the extraction service using the Extract

Attachment Data function. Your consignment order is blocked for planning.
3.  Document Information Extraction receives the data from the attachment and

starts the extraction.

4.  While the extraction is running, you check the processing status in Document

Information Extraction.

5.  You refresh the consignment order and see that the extraction is done.
6.  The system retrieves the extracted data and enters it in your consignment

order.

7.  The extracted data is compared to the data in the system.

You are notified that an item mismatch creates a document error. You can view
the error message on the Document Error tab.
The data comparison results show that one of the items in the consignment
order is missing in the extracted data. You can check the information in the
attachment and find a typo in the corresponding item in the delivery document.
Because of the typo, the extraction service couldn't read the data correctly. On
the Document Error tab, you choose Delete to delete the error and continue
with the consignment data.

8.  The processing block for the consignment order is removed.
9.  The system determines the correct requirement documents based on the

extracted data.

176


Lesson  4  -  Generating  Document  Outputs  for Print and Digital
Delivery

## Objective

After  completing  this  lesson,  you  will  be able to generate outputs for your freight order
and preview the documents.

## Output Management

In this lesson, you learn how to configure settings to enable the printing of documents
in the freight order.

## Output Management Capabilities

In  general,  output  management  provides  the  following  capabilities  based  on  the
business document:

●  Automated (backend), rule-based dispatching of outbound communications in

response to business events, such as the creation of an order, saving a
document, and so on

●  Preview of output and manual (front end) outputs in the user interface (UI)
●  Archive output dispatched concerning business documents
●  Mass output from a worklist

177


## Output Management

Before,  during,  and  after  execution,  each  user  and  party  involved  must  be  notified
when a task is required to be executed or a report on a recent activity is made. Users
must  view  the  result  of  business  process  activities  and generate output in response
along  the  process.  Output  management  automates  the  output  of  business
documents, such as printouts, mail, or fax to specific events.

TM  has  several  standard  output  types,  such  as  external  communication  and  alert
notification.  Several  other  tools  and  methods  may  also  be  used.  Your  business  can
use  standard  printing,  fax,  and  e-mail  for  external  communication  with  a  document
preview  option.  For  internal communication, alert management options are available,
and  a  workflow  can  pass  requirements  from  one  business  process  step  to  another.
Communication  with  B2B  systems  is  also  available  in  situations  such  as  tendering
freight orders when a bidding or purchasing activity is present.

BI  data  uploads  can  be  executed  to  provide  management  reporting  on  various
documents like freight units, freight orders, and freight bookings. Various order events
can  trigger  communication  to  event  management  systems  to  make  cross-system

178


activities  transparent.  While  TM  has  its  own  internal  status,  when  integrating  with
systems  such  as  SAP  ERP  or  EWM,  cross-system  communication  is  necessary  to
gain visibility of the big picture.

## Output Types

The output management in TM is available for all documents.

To understand what happens when documents are printed, you must understand the
Post  Processing  Framework  (PPF).  It  is  configured  in  the  backend  system,  with  the
following  customizing  path:Cross-Application  Components→Process  and  Tools  for
Enterprise  Applications→Reusable  Objects  and  Functions for BOPF Environment→PPF
Adapter for Output Management→Maintain PPF Settings. Here, you manage the action
profiles.  An  action  profile  is  the  smallest  set  of  action  definitions  that  can  be
investigated during one call of the action determination of the PPF.

Post-Processing Framework (PPF)

As  a  framework,  you  can  imagine  the  PPF  as  a  way  to  answer  the  following  three
questions:

●  What (should be done in the activity)?
●  Why (is the activity done)?
●  When (is the activity done)?

179


Post-Processing Framework (PPF) Answers Three Questions

What

Why

When

Send the whole shipping list
via EDI

Shipping list has been created  Next batch job

Send whole shipping list via
mail

Shipping
changed

list

has

been

saving

When
document

the

Send  shipping  list  changes
via fax

Business object is in the state
In Process

saving

When
document

the

Generally, it is essential to note that PPF actions can only process information already
saved  to  the  database.  This  prevents  you  from  accidentally  sending  preliminary
transportation labels to a spool in the warehouse, for example.

## Output Management Adapter

You can connect the PPF at the level of the individual BO nodes. When you select the
application /SCMTMS/TRANSPORTATION in customizing, you can manage the action
profiles  assigned  to  this  application.  An  action  profile  is  the  smallest  set  of  action
definitions  that can be investigated during one call of the action determination of the
PPF.

180


Each  action  profile  contains  a  set  of  multiple  action  definitions  (1:n).  An  action
definition  defines  all  possible  realizations.  The  realizations  are  modeled  in  the
so-called processing type. The processing type represents the technical realization of
an  action  definition,  for  example,  the  start  of a workflow, sending out a PDF form by
fax or mail. The action definition determines whether business partner data is required
for  the  execution  and  the  business  partner  to  which  the  data  relates.  An  action
definition, therefore, has the character of a business task and defines "what" should be
done with this action (mail, fax, and so on).

: The conditions are checked if the system has identified the action definition from the
action
important  types  of  conditions  for  the  PPF/Output
Management:

list.  There  are  two

●  The first one is the scheduling condition. This condition is checked during the
PPF action determination. It decides whether an action should be executed or
not. The scheduling condition is identified from the assignment to the
configured action definition. The scheduling conditions define the "why"; for
example, the lifecycle of the predecessor document is X, or the document is
canceled.

●  The second important condition is the starting condition. This condition is

checked just before the execution of an action starts. These conditions should
only influence the point in time when an action will be executed. They define the
"when"; for example, they define that the message is sent "on save", or "one day
before pickup", and so on.

181


Lesson 5 - Monitoring the Execution of the Freight Documents

## Objective

After completing this lesson, you will be able to monitor the execution of freight
documents.

## Freight Order Execution

The logistics/transportation process involves activities and procedures spread across
different business partners and often across several distributed systems. From a
tracking perspective, this increases the challenges of successfully monitoring the
progress of individual process parts. In this lesson, you will learn how your company
can overcome these difficulties by using tracking solutions from SAP:

●  SAP Business Network Global Track and Trace
●  SAP Event Management

SAP Business Network Global Track and Trace and SAP Event Management allow you
to make processes, assets, and performance visible across the supply chain.
Extensive tracking and tracing functions allow process monitoring, automated
exception resolution, proactive alerting, and extensive reporting in a single solution.

The key difference between both solutions is that SAP Business Network Global Track
and Trace is a cloud solution that needs to be licensed separately. SAP Event
Management is also available on-premise and can be run on the same SAP S/4HANA
system with TM.

## Event Management in SAP TM

The event management system is designed to work with several SAP ERP instances, if
necessary. It can communicate with SAP CRM, where sales orders may be received,
and this communication is processed back to the customer to support order
fulfillment. SAP Advanced Planning and Optimization (APO) may create the
replenishment plan. SAP ERP or SAP Manufacturing Execution may be responsible for
communication and tracking progress on the shop floor. SAP EWM (Extended
Warehouse Management) may be responsible for the picking and packing as part of
the logistics execution.

182


SAP Event Management offers visibility processes to monitor transportation execution
in SAP TM. The transportation execution visibility processes enable users in roles
such as transportation dispatcher, shipper, or ordering party to track and monitor
planned events or to report an actual event.

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
less time firefighting.

Monitor, notify, analyze, and adjust are the four cornerstones of SAP Event
Management, which contribute to an adaptive solution. The monitoring process
collects data from the various source systems. Notifications can be set up to be
triggered, with alerts sent to the parties responsible if a process deviates from its
anticipated course. The appropriate parties can simulate adjustments and make
necessary changes based on the alerts. Finally, concerning analytics, SAP Event

183


Management can be tied into the SAP BW environment to support transportation
management reviews.

## Event Types

SAP Event Management is capable of processing several different types of events.
Within a given process, you have events that you expect to happen and events that
happen. Typically, you want to compare the actual event against what you expected,
as follows:

●  Regular Event

The first type of event is an event that you expect to happen within a particular
time frame, and it happens as expected. This is a regular event.

●  Overdue Event

This is an event that you expect to happen within a particular time frame, and it

184


occurs outside the scheduled time frame. An overdue event can cause a
subsequent event to be rescheduled or recorded as an overdue event.

●  Unexpected Event

The third type of event is unexpected. This could be a truck breaking down or a
malfunction in a piece of equipment, potentially affecting subsequent events,
causing something to be rescheduled, or taking another action.  An unexpected
event could trigger an alert or another type of notification.

●  Unreported Event

In this case, you expect an event to occur within a particular time frame, but it
is not reported for whatever reason. It is possible that something still needs to
happen following this event, so you could set a time limit that sends a message
or triggers something to happen when the event is unreported for a specific
period.

## Event Management Integration

Transportation operations is an area in which transparency is crucial, especially in
those cases where lengthy transportation times have to be considered, such as when
shipping overseas. To ensure customer satisfaction, keeping complete control of what
is happening is more important than ever, even if parts of the business process may
run outside your company’s sphere of influence.

Visibility processes for transportation management offer preconfigured,
out-of-the-box content for transportation operations, supporting you in tracking
relevant activities within and beyond the confines of your company. You can monitor
different processes and business documents, such as freight units, orders, and
bookings.

185


The Event Management Integration figure shows a typical scenario in which the SAP
EM and TM systems are updated to accurately reflect a freight order's real-world
progress.

During the loading process, SAP ERP or SAP EWM may send a signal (notification)
that there is a delay in the loading process. This can trigger an alert. The
transportation planner may have to adjust the schedule to ensure the container makes
it to the ship on time. Once the ship has left the departure port, GPS updates may
indicate it has not reached its midway point. This could be due to weather or
mechanical issues. The customer service agent can be notified and contact the
customer to inform them of anticipated delays.

Due to the alert system, the planning team does not have to watch over every order.
They can spend most of their time managing exceptions.

## Global Track and Trace

SAP Business Network is a cloud service with global coverage specifically built to
connect logistics business partners – to collaborate across companies and jointly
manage transactions, exchange documents and data, and share insights. You
onboard to the network once and are set to connect and collaborate with many!

186


SAP Business Network Global Track and Trace is integrated with SAP S/4HANA
Transportation Management to synchronize business objects and milestone updates.
It captures, processes, and stores tracking information about logistics business
processes with out-of-the-box visibility connectivity. In addition, it allows business
users to achieve real-time transparency in executing those processes, conduct impact
analysis, and manage exceptions.

Business benefits from SAP Business Network Global Track and Trace are derived
from the global logistics visibility that the solution provides. There are three:

1.  Enhanced risk mitigation through data-driven decision-making.

Analyzing routes, events, and statuses for individual in-progress shipments
alone can provide valuable insights into supply chain operations. By combining
detailed transportation insights with the higher-level business context of a
Sales Order, Purchase Order, or Stock Transport Order, natively integrated into a
company’s ERP, provides supply chain managers with critical inputs into
strategic decisions, such as supplier sourcing, route optimization, and inventory

187


allocation, leading to improved business performance and competitiveness
from a more resilient supply chain.

2.  Improved operational efficiency, including better inventory management.
Logistics visibility allows companies to optimize their transportation and
distribution processes by identifying inefficiencies, streamlining routes, and
consolidating shipments to minimize delays, improve resource utilization, and
drive cost savings. Detailed logistics visibility enables more precise inventory
management, enabling businesses to accurately monitor the movement of
goods in real-time and with sufficient granularity to forecast inventory levels to
avoid stockouts and unplanned long lead times or excess inventory and
spoilage.

3.  Better customer service through faster problem resolution.

With detailed visibility into shipment routes and events, businesses can provide
more accurate and timely updates to customers regarding the status and
location of their shipments. When, or even before, issues arise during transit,
such as delays, damages, or lost shipments, transportation planners can take
action. Transportation planners can act upon predictive or reported status to
pinpoint the location and situation of affected units and take immediate
corrective actions, such as rerouting shipments or initiating investigations. This
transparency then allows customer service personnel to enhance customer
satisfaction by reducing uncertainty, improving responsiveness, and enabling
better communication, which enhances customer loyalty.

SAP Business Network Global Track and Trace in SAP S/4HANA Transportation
## Management

SAP Business Network Global Track and Trace is integrated with SAP S/4HANA to
track order fulfillment progress and goods in transit. Objects such as sales or
purchase orders, freight units, tracking units, or shipments created in SAP S/4HANA
are synchronized via IDOC interface to SAP Business Network Global Track and Trace
along with planned and actual milestones such as arrival, departure, goods issue,
goods received, …

188


To provide shippers (solution owners) a holistic multi-modal view into order fulfillment
and goods in transit, SAP Business Network Global Track and Trace allows logistics
service providers to integrate via public API or EDI 213 and 214 to receive order
tracking requests for the respective tracked processes and share order events.

Optionally, additional licenses can be purchased to add visibility providers as an
additional layer and reduce the integration efforts of individual logistics service
providers. As visibility providers might have different expertise in different regions or
modes, SAP Business Network Global Track and Trace can help distribute tracking
requests to business partners.

As the tracked processes are populated with actual events, solution owners can
understand the impact of deviations from the plan as events on the shipment level are
correlated to deliveries or orders, and there is an impact analysis available for
shipments ‘running late’ or being ‘delayed.’

Further, stakeholders can be kept in the loop as logic is built in to determine recipients
and respective notification content through event-to-action scripts.

189


SAP Business Network Global Track and Trace Standard Application

There are standard applications tailored to different roles. For transportation planners,
there is the Track Shipment app; for shipping specialists the Monitor Outbound
Deliveries app and for internal sales representatives and purchasers there are the
Track Sales Order Fulfillment app and the Track Purchase Order Fulfillment app, which
includes stock transport orders. In addition, we support receiving specialists via the
Monitor Inbound ASN app.

User attribute authorization allows solution owners to define who can see which
shipment or tracked process.

However, SAP Business Network for Logistics is more than the above standard
applications. Solution owners can utilize the flexible and extensible setup, which
supports customer-defined fields, event types, and event-to-action scripts to extend
standard applications or build custom scenarios from scratch.

SAP Business Network Global Track and Trace Example Scenario

Let’s look at an example tracked process for sales order fulfillment that utilizes
standard and custom events and scripts (in the graphic below, black items need to be
custom configured, and grey items are part of the standard delivery).

For each sales order, the following predefined milestones (planned events) and
corresponding action are relevant:

●  Goods issue – triggering a notification
●  Proof of Delivery – triggering a notification
●  Quality Inspection – triggering notification in case of quality KPI NOT fulfilled
●  Goods Receipt – send customer survey

190


Additional actual events that might be received are:

●  Confirmation of execution of sales order – notify customer
●  Delay – update expected time of arrival in SAP S/4HANA Transportation

Management

191


Unit 8 - Processing Transportation Cost and
## Charges

Lesson 1 - Managing Charge Calculation Master Data

## Objective

After completing this lesson, you will be able to understand how freight agreements,
charge calculation sheets, rate tables, and scales are maintained.

Overview of Transportation Costs and Charges

Transcript of video:

“When  shipping  products  to  customers  via  a  third  party,  an  organization  needs  to
account  for  the  costs,  as agreed with the logistics service provider. SAP TM provides a
broad  and  flexible  calculation  process.  In  this  unit, we'll dive into the critical aspects of
managing  and  calculating  transportation  costs  within  the  SAP  system.  We'll  start  by
includes
exploring  the  management  of  charge  calculation  master  data.  This
understanding  Freight  Agreements,  which  are  essentially  contracts  between  shippers
and  carriers.  We'll  look  at  how  these  agreements  are  structured  and  the  components
that drive the calculations such as Calculation Sheets, Rate Tables and Scales. Next, we'll
examine  the  process  of  calculating  charges  in  freight  documents.  You'll  learn  how the
system  determines  which  agreement  to  use  and  how  it  applies  various  factors  to
calculate the final charges for a shipment. We'll then move on to the settlement of freight
charges.  This  involves  creating  Freight  Settlement  Documents,  which  are  crucial  for
verifying  invoices  and  posting  costs  to  the  appropriate  financial  accounts.  Finally, we'll
explore the distribution of freight costs. This is a key step in ensuring that transportation
costs  are  accurately  allocated  to  the  right  cost  centers or materials, which is essential
for proper profitability analysis. Throughout this unit, you'll gain insights into the intricate
processes  that  SAP  TM  uses  to  manage  transportation  costs  effectively.  By  the  end,
you'll have a solid understanding of how to set up, calculate, settle, and distribute freight
charges within the system. Enjoy learning with SAP!”

Freight Agreements

Freight Agreement Overview

192


A  Freight  Agreement  is  like  a  master  contract  between  a  company  that  must  ship
goods  (shipper)  and  a  company  that  provides  transportation  services  (carrier).  It
outlines  the  terms,  conditions,  and  pricing  for transportation services over a specific
period.

Components of a Freight Agreement (in hierarchical order):

1.  Freight Agreement (FA): This is the top-level document containing all the

contract details.

2.  Calculation Sheets: These are attached to the freight agreement and define

how transportation charges are calculated. Multiple calculation sheets can be
linked to a single freight agreement.

3.  Rate Tables: These are part of the calculation sheets and contain the actual
prices for transportation services. Rate tables use scales to define pricing
based on various factors.

4.  Scales: These are the building blocks of rate tables. Scales define the

dimensions or parameters that affect pricing, such as weight, distance, or
volume.

5.  Charge Types: These are used within calculation sheets to classify different

charges, such as base rates, surcharges, or discounts.

How they relate:

●  A freight agreement can have multiple calculation sheets to cover different

scenarios or service types.

●  Each calculation sheet contains multiple charge types and refers to one or

more rate tables.

●  Rate tables are built using scales to define how prices change based on

different factors.

●  Scales provide the foundation for creating flexible and detailed pricing

structures within rate tables.

193


Think  of  it  like  this:  The  freight  agreement  is  like  a  book  that  contains  the  terms  of
your shipping contract. Calculation sheets are the chapters in this book, each dealing
with  a  specific  type of shipment or service. Charge types are the different categories
of  fees  mentioned  throughout  the  book,  and  rate  tables  are  the  detailed  price  lists.
Scales are the rules that determine how prices in these lists change based on factors
like weight or distance. This structure allows for a flexible and detailed way to manage
complex  pricing  and  terms  for  transportation  services  while  keeping  everything
organized under a single agreement.

## Integration of Charge Management

When shipping products to customers via a third party, an organization must account
for and recognize the costs of moving goods.

TM  provides  a  broad  and  flexible  calculation  process.  With  the  integration  of  MM,
integration to the Financial Accounting (FI) and Controlling (CO) applications allows an
organization  to  perform  payment,  execute  billing  transactions,  and  trigger  the
settlement process to accrue the proper transportation charges to financial accounts.

194


## Transportation Charge Management Master Data

The  master  data  elements  required  for  charge  calculation  are  freight  agreements,
calculation sheets, rate tables, and scales. For all of them, you can create templates to
minimize the effort when new master data is required.

## Freight Agreements

Freight  agreements  (FAs)  represent  a  long-term  contract  between  a  shipper  or  LSP
and a carrier or supplier. Freight agreements can be determined based on purchasing

195


organization  and  carrier.  (Additional  preconditions  can  also  be defined if necessary).
Each  agreement  can  point  to  one  or  more  calculation  sheets  (CS).  The  freight
agreement is connected to a CS, and the costs (freight charges and advice fees) used
in the assigned CS are visible in the FA.

Freight agreements (FAs) are the basis for calculating transportation charges. You use
FAs to calculate transportation charges billable to you by your carrier.

## Freight Agreement Structure

The  system  determines  the  agreement  based  on  organization,  business  partner,
validity  period,  and  preconditions.  In  the  freight  agreement type customizing activity,
you  can  configure  whether  one  or  multiple  partners  can  be  entered  into  the
agreement.  That  is  if  you  have  one  freight  agreement  with  a  carrier  that  is  valid  for
numerous purchasing organizations,

Agreement Structure Overview:

## Charge Calculation Sheets

Depending  on  how  a  shipment  will  be  transported,  various  charges may be incurred
for different means of transport. In TM, companies can create calculation sheets that
reflect  all  possible  charge  elements  for  a  given  carrier.  These  charges  essentially
mimic the terms of the freight contract.

196


The calculation sheet is a hierarchical table used to calculate transportation charges.
The  calculation  sheet  combines  the  charge  types  permitted  for a document and the
sequence  in  which  the  system  considers  these  charge  types  during  the  calculation.
The  system  uses  the  calculation  sheet  to  specify  which  transportation  charges  to
calculate  and  how  to  calculate  them.  This  helps  to  pay  suppliers  or  carriers  for
subcontracted  transportation  services.  The  calculation  sheet  points to charge items,
and each charge item can result in a calculated amount.

## Calculation Sheet Maintenance

Calculation  sheet  maintenance  is  a  step  in  the  process  of  setting up master data in
the  Transportation  Charge  Management  (TCM)  component.  It  is  integrated  with
agreements,  rate  tables,  and  scales.  You  can  use  the master data cockpit to access
an overview of the charge management master data per organizational unit, business
partner,  and  charge  type.  The  system  also  shows  the  relationship  between  the
different types of charge management master data.

You can use a template to create a calculation sheet and calculation sheet line items.
The calculation sheet includes transportation charge elements, subtotals, and totals.

It  provides for a calculation schema showing the steps and the specifications for the
charges.  The  resulting  charges,  sub-totals,  and  totals  can  be  displayed  in  the
documents based on the calculation sheet.

197


## Calculation Sheet Items

The calculation sheet items have the following attributes:

●  Charge Type
●  Rate

Rates contain details of the rate table for each standard charge item. It is also
possible to enter fixed rates or percentages of other lines in the calculation
sheet.

●  Dimensional Weight Profile

The system uses the dimensional weight factor in the dimensional weight
profile to convert a product's gross volume into dimensional weight. The
system then uses the dimensional weight to apply the correct rate. Note that a
dimensional weight profile at the line item level of a calculation sheet has
priority over a dimensional weight profile in an agreement.

●  Calculation Resolution Base (for example, root, container, product, and stage)
During charge calculation, the system determines the calculation resolution
base by the origin of the data upon which the charge aspect is based. You can
define the charge aspect in the resolution base objects, such as container,
product, and stage.

○  Root: This is the document's header, which includes the freight order or

the freight booking.

○  Stage: To utilize stage attributes such as distance between the shipper

location and the port of loading.

○  Container: When the container's gross weight will be used for the

calculation.

○  Product: When product attributes like product quantity, weight, or

volume need to be used.

●  For example, you want to determine the freight rate based on the gross weight
of the order. To do this, you must use the calculation resolution base of root. If,
however, you want to calculate the freight per package, the calculation
resolution base should be package.

●  Resolution Base Grouping Rule (for example, destination location, weight,

volume)
The rule the system uses to group selected input data, for example, destination
location, weight, and volume. You use the grouping rule and the resolution base
to group charge lines using the calculation base specified in the Group By field
of the grouping rule.

●  Calculation Method (for example, standard or break-weight)

The calculation method defines how the rates determined from the rate table
will be interpreted. The break weight calculation method compares and selects
the lower rate from either the actual or lower end of the following rate range.

198


With clipping, the system works through the pricing scale level by level. The
calculation results from each scale level are then summarized to produce the
overall result.

## Charge Types

A charge type is the classification of a charge line that plays an important role in how
the  system  calculates  the  transportation  charges  for  the  charge  line,  for  example,  a
base  rate,  surcharge,  or  discount.  A  charge  type  can  result  in  a  positive  or  negative
value for a charge line. You can also specify whether a charge type can be an amount
or a percentage value.

Charge  types  can  be  grouped  into  charge  categories.  A  useful  code  list  is  the
UN/EDIFACT code list 5237. All three entities are freely definable in Customizing. You
can  use  the  charge  subcategories  of  charge  types  to  group  and  categorize  charge
types  more  granularly  than  charge  categories.  A  suitable  example  is  the  code  list
resulting  from  UN/EDIFACT  Recommendation  23:  "FREIGHT  COST  CODE  #  FCC
Harmonization of the Description of Freight Costs and Other Charges".

Charge categories and subcategories can be assigned in the charge type customizing
activity and used to determine the service material during settlement.

When defining charge types, you can use the following settings:

●  Specify whether a charge type can result in a positive or negative value.
●  Specify whether a charge type can be an absolute or a percentage value.
●  Specify whether you want to set the charge type as an absolute or a

percentage value each time you assign the charge type.

199


Indicate if the charge is a tax.

●  Assign a charge type to a charge category and charge subcategory.
●
●  Specify if and how the system rounds a value.
●  Assign a default calculation base to the charge type so you do not need to

assign a calculation base each time you create a calculation sheet line item.

## Rate Tables

A rate is a price for a certain transportation service that applies only during its validity
period. In TM, rates are listed in a rate table.

## Rate Table Elements

You can define the following elements in the rate table:

●  Charge Usage

You can define the charge usage as relevant to paying your carrier.

●  Charge Type

The system only assigns rate tables to a charge item in a calculation sheet if
the charge types match. You can use this field to search for a rate table.

●  Dimensions

You add each dimension on which you want your rate to be defined and looked
up. For example, if you wish the rate to be defined based on destination
location and weight, add a dimension for destination location and weight.

●  Calculation Base (for each scale)

You can define the calculation base for the scale. The calculation base is the
actual base or the factor on which the rate retrieval is performed.

200


●  Relevance for Calculation Method

If you select this checkbox, you define whether you want the system to apply a
special calculation method, such as break weight or clipping, to the rate table
on the level of a charge item.

Rate tables also contain the freight rates for transportation services and allow you to
maintain  rates  for  certain  validity  periods.  A  rate  table  can  contain  up  to  14
dimensions  for  rate  maintenance.  The  rates  are  reusable  and  can  be  referred  to  in
multiple  calculation  sheets.  The  rates  can  be  imported  or  exported  using  Microsoft
Excel.

Example of rates include the following:

●  Weight/volume rates
●  Volumetric rate calculation (bulkiness factors)
●  Distance rates
●  Freight of all kinds and commodity rates
●  Various origin and destination point classifications such as point-to-point,

point-to-zip, point-to-state, zip-to-zip, and state-to-state

●  Rates based on equipment (container type or size) or packaging class
●  Handling charges: Terminal handling, cross-docking costs, loading and

unloading, empty handling, document handling, AMS filing, canal due, security
surcharge, and so on

Rate Table Integration with Microsoft Excel

201


You can maintain a large rate table, with or without scale items, using Microsoft Excel.
You  can  enter  the  rates  and  scales  into  a  Microsoft  Excel  file  and  upload  the  file  to
your  TM  system.  Alternatively,  you  can  define  an  empty  reference  rate  table  with
validity  periods  in  TM and download it to Microsoft Excel. You can then maintain the
rate table in the Microsoft Excel file and upload it to your TM system.

## Scales

While  a  rate  is  a  price for a certain transportation service that applies only during its
validity  period,  a scale represents a dimension of the rate. In effect, a scale defines a
parameter that then defines a rate. For example, if a rate depends upon distance and
weight,  you  must  define  a  separate  scale  for  distance and weight. The distance and
weight scales are then used to define the rate.

Scale  maintenance
is  a  prerequisite  for  maintaining  rates,  as  scales  are  the
dimensions  of  rate  tables.  You  maintain  scales  independently  of  the agreement and
the  rates  and  can  reuse  them  in  multiple  rate  tables.  A  scale  has  a  scale  base,
essentially  a  database  field  tied  to  an  attribute  of  the  freight  order.  The  scale  base
defines  how  the  system  interprets  the  scale.  For  example,  a  rate  based  on distance
has to have the distance calculated.

Possible scale bases include the following:

●  Product quantity
●  Package type
●  Weight
●  Volume
●  Means of transport

202


●  Location
●  Distance
●  Business partner

Each scale is based on a scale type. The scale type controls how the scale levels are
defined.  It  indicates  whether  the  specified  scale  values  represent  the  scale  levels'
upper or lower boundaries.

Depending  upon  the  scale  base,  a  scale  unit  of  measure  can  be  defined.  This  is  a
mandatory  field  if  the  unit  of  measure  is  relevant  for  the  scale  base.  Weight,  for
example, requires a unit of measure.

Concerning  calculation  type,  you  can  choose  between  absolute  and  relative.  For
non-numeric  scales,  you  can  only  choose  absolute. The system uses the calculation
type on the scale level as the proposed value for rate table maintenance.

You  can  also  assign  rounding profiles. Before the system accesses the scale to look
up  a  rate  in  a  rate  table,  it  rounds  the  input  value  based  on  the  rounding  profile  to
determine the right scale level.

## Calculation Base

A  calculation  base  identifies  the  actual  base  or  factor  with  which  the  system
calculates the charges for the scale.

203


There  can  be  various  scenarios  in  which  the  system  must  calculate  a  charge  for
different weights, such as gross and net weights.

In  this  case,  gross  and  net  weights  correspond  to  the  scale  base  Weight,  whose
dimension  is  mass.  However,  by  definition,  gross  weight  and  net  weight  are  two
entirely different charge aspects. Therefore, they have two different calculation bases,
for example, "W1" for gross weight and "W2" for net weight.

To  follow the scenario given here, you define a calculation base for every scale base.
This calculation base is the final element in the charge determination. This means that
the calculation base is used to determine the charges.

In  the  figure,  Calculation  Base,  the  charges  depend  on  weight  and  the  destination
location. The scale has the scale base Location. This scale base defines the scale as
using locations only. The scale base can be used for both the source and destination
location.  The  calculation  base  DESTLOC  determines  the  destination  location  of  the
freight  order  used.  Technically,  in customizing the calculation base, you define which
field  to  use  and  which  program  or  class  the  system  will  call  to  determine  the  field
value.

If  the  resolution  base  in  the  calculation  sheet  points  to  the  freight  order  stage,  the
system will derive the values from the specific stage and use them in the calculation.

Lesson 2 - Calculating Charges in Freight Documents

## Objective

After completing this lesson, you will be able to calculate transportation charges.

## Charge Calculation

Freight Agreements (FAs) are the basis for calculating transportation charges. In this
section, we look at how agreements are determined.

The system determines the agreement based on organization, business partner,
validity period, and preconditions. Suppose that several matching agreements exist,
which can be determined from the freight order/booking data. In that case, it is

204


possible to have a leading charge type (defined in charge type Customizing), and the
first agreement where the defined leading charge type can be calculated is picked.
Besides using leading charge types, it is possible to maintain priorities. If the system
finds multiple matching agreements during agreement determination, the agreement
priority defines the sequence in which the subsequent determination is executed. The
agreement priority can be maintained on the General Data tab in the details section.

## Built-in Preconditions in Agreement Items

In an agreement, there are two ways of using preconditions for the agreement items
(calculation sheets):

●  Built-in preconditions
●  BRFplus preconditions

It is possible to define a BRFplus condition or a BAdI to check if a certain calculation
sheet is to be processed in a certain business context. The result of this rule is a true
or false decision. If the response from BRFplus or the BAdI is true, the calculation
sheet is considered for charge calculation. Some built-in preconditions are available
on the agreement item level.

## Manual Agreement Selection

Often, logistics service providers (LSPs) have multiple FAs with the same carriers and
purchasing organizations. This is because an LSP may strike deals with carriers at
various levels, for example, on a country, regional, and global basis.

Normally, the larger the contract, the better the rates. However, if a country business
partner (BP) pushes a lane to increase market share, the LSP could get better rates.

205


Therefore, having a different contract with the country BP, or even multiple contracts,
makes sense.

If there is no rule available to define in a unique way which agreement should be used
for the calculation, manual agreement selection is also possible. Manual agreement
selection offers additional capability for automatically selecting minimum or
maximum agreement items through calculation profile control settings.

Charge Calculation Customizing

## Calculation Profile

The calculation profile provides a central location to define the settings you want the
system to use when calculating transportation charges. The following are examples of
settings you can define in a calculation profile:

●  Specify the data type the system uses for the basis for the rate, exchange rate,
agreement validity, and ultimately the charge calculation. (For example, the
order date, the invoice date, or the expected end date of the main carriage.)
●  Specify the level at which the system calculates the charges, for example, at

the header, item, or stage level.

●  Specify the determination rule that the system uses to determine the

agreement and the calculation sheet.

●  Specify the default dimensional weight profile for the organizational unit and
the condition the system uses to determine the dimensional weight profile.

In the Define Calculation Profile Customizing activity, you define the settings you want
the system to use when calculating transportation charges. You find it in Customizing
at Transportation Management→Basic Functions→Charge Calculation→Basic Settings
for Charge Calculation→Define Calculation Profiles.

206


## Charges Profile

You can enable charge calculation for a purchasing organization by assigning a
charges profile to the purchasing organization (see the PPOMEtransaction). The
charges profile groups the general settings for charge calculation, such as the
calculation profile you want the system to use when calculating transportation
charges.

To activate charge calculation in any freight document, you must enable charge
calculation in the corresponding freight document type customizing activity.

## Freight Order Charge Calculation Process

During freight charge calculation in the freight order, the following steps occur:

1.  The data is collected from the following TM core objects:

●  Transaction business object: freight order, freight booking, service order,

stage, item, container
●  Configuration objects
●  BRF+ conditions
●  Master data
●  Any BAdI implementation
2.  The freight agreement is determined.

207


3.  The calculation sheet within the freight agreement is determined.
4.  The values of each charge type in the calculation sheet are calculated.
5.  The log file of the calculation run is held, and so on.
6.  The calculated results are shown in the freight order.

Lesson 3 - Settling Freight Charges

## Objectives

After completing this lesson, you will be able to:

●  Generate freight settlement documents.
●  Post freight charges to MM
●  Verify freight invoices.

## Freight Settlement Documents

A freight settlement document (FSD) is a business document that is posted to MM to
create a purchase order and service entry sheet in order to verify an invoice received
from a supplier or carrier. When the invoice is received, it should be checked against
the data from the freight settlement document. If performing an evaluated receipt
settlement, the automatically generated invoice is based on the data from the freight
settlement document.

The transportation charges are calculated in TM based on a freight order, or freight
booking. The actual invoice verification takes place in MM. You can create an

208


individual FSD for one freight order, or freight booking. You can create a collective FSD
for multiple freight orders or freight bookings. You can also create multiple FSDs at
the same time.

The settlement includes the following:

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

209


●  General data: Document type, the purchasing organization, payment terms,

document currency, and so on.

●  Business partner information: Invoicing party, payee, additional business

partners, which can be entered manually or automatically determined by the
system.

●  Orders: The business documents or the business document items that are

being settled using the FSD.

●  Charges: For each FSD item, the Charges tab page has the charges relevant for

settlement with the carrier.

Freight Settlement Document Creation

The FSD can be created in the following ways:

●  You can create an individual FSD for one freight order, or freight booking, or a

collective FSD for multiple freight orders, or freight bookings. To do this access
freight orders, or freight bookings from the worklist, in the relevant document
overview, or in the freight settlement overview. The system automatically
creates the FSD based on the data in the freight orders, or freight bookings and
calculates the transportation charges.

●  You can create FSDs directly out of the freight booking or freight order apps.
●  You can create multiple freight settlement documents using the mass creation

of FSD report.

Freight Settlement Document Creation - Configuration

210


When the FSD creation is triggered for a freight booking/freight order (FB/FO), the
corresponding document type is used to determine the FSD type used.

The purchasing organization specified in the FB/FO is used to determine the
settlement profile. All of this information is then used to create FSDs for the selected
FO/FB.

## Posting Freight Charges

Supplier Freight Processing - Process Flow

211


As you can see in the figure, Supplier Freight Processing - Process Flow, the typical
freight settlement process flow is as follows:

Based on a delivery, the planner carries out several planning steps and creates a
freight order or a freight booking to subcontract to a carrier.

On settlement, the system creates a Freight Settlement Document (FSD). This
document contains all relevant logistical data, charges, and other commercial data.
The charges can be copied from the freight order or booking (most commonly), or
another charge calculation can be triggered based on the freight agreement between
the purchasing organization and the carrier. It is possible to change charges in the
FSD manually. FSDs can be created online or in batch. It is possible to do a collective
settlement (several freight orders or bookings are settled with one FSD). The FSD can
then be posted to MM.

A purchase order and a service entry sheet are created in MM. This constitutes the
worklist for invoice verification. You also have the option of self-billing.

## Note

The purchase order and service entry sheet are only used for technical purposes to
post accruals. The service entry sheet comprises a list of services a vendor performs
based on a purchase order, containing service descriptions and details of quantities
and values. The descriptions of planned services deriving from the purchase order are
default descriptions in the service entry sheet.

You can add charges to an invoiced FO, but removing them is impossible. In the latter
case, a credit memo must be created based on the FSD.

212


## Invoice Verification

## Purchase Order and Service Entry Sheet

Each service entry sheet is based on an external service order. Determining a valid
purchase order is required for transfers to Financial Accounting and for settlements.
Important criteria for the service order include carrier, purchasing organization,
purchasing group, plant, and item category.

When the system has automatically determined a valid purchase order, a service entry
sheet is created that refers to the purchase order. During posting, you accept services
and, in Financial Accounting, an accounting document for generating accruals is
created.

During account assignment, the system determines the correct G/L account in
Financial Accounting for each cost item and the assignment for Controlling. Account
assignment can be carried out at different levels, depending on the level of detail at
which you want to track costs.

The transfer to Financial Accounting to establish accruals requires entering and
accepting the services rendered. The system automatically creates a service entry
sheet. Using the credit memo procedure, also referred to as the evaluated receipt
settlement (ERS) procedure, you can settle the freight costs with the carrier without
having received invoices. You can choose from different settlement periods. You
transfer the calculated freight costs to Financial Accounting. The carrier verifies the
invoices. In case the carrier discovers variances, you can post these variances as
subsequent debits or credits.

213


If you receive invoices from the carrier, you can verify them manually and create them
manually. Invoice verification can be done with reference to the freight order, carrier,
bill-of-lading, air waybill, flight number, and voyage number.

## Dispute Management

## Dispute Management for Freight Settlement

As a requester of transportation services, such as a shipper, you can have one of the
following freight settlement processes in place with a provider of transportation
services, such as a carrier:

●  Self-billing:

Your service provider does not submit an invoice. Instead, you settle
automatically based on the information in your freight order. Self-billing is also
called evaluated receipt settlement (ERS).

●  Submission of an invoice by the service provider:

You pay the service provider the amount contained in the invoice.

In both processes, there can be differences and potential disputes between what you
expect to pay and what the service provider expects to be paid. To keep good
business relationships, you must work closely with your service provider to resolve
these differences collaboratively. It would be best to clarify the differences and agree
with the service provider on resolving them.

214


In TM, you can use the invoice submission settlement process with enterprise
services. You are a shipper who requests transportation services from your service
provider. You can enable your service provider to use enterprise services to submit
invoices for the freight orders the service provider executes. The service provider
creates an invoice document in their external system and uses enterprise services to
send you the invoice. You use the external invoice to create a carrier invoice in TM.

Your service provider may have included additional unplanned freight costs or may
have charges different from what you expect to pay in your freight order. Your TM
system automatically evaluates the external invoice. It automatically creates a dispute
case when your service provider submits an invoice with values different from what
you expect. The system captures these differences in a dispute case. The system
captures the individual differences in charges as dispute items.

On the dispute case screens, you, as a shipper, can approve or reject a dispute case. If
you approve a dispute case, the system updates the freight order with information for
the charge type, such as rate and quantity information. However, the system does not
update logistics information, such as gross weight, gross volume, and total distance
of the freight order.

When you resolve disputes early, you have the following business advantages:

Inclusion of changes and unplanned costs in one invoice

●
●  Accuracy in payment to the service provider

The following are the typical steps that can happen in a dispute case:

●  Your service provider uses enterprise services to submit an invoice in line with
the terms you have agreed with your service provider. TM creates a carrier
invoice in the shipper's system. The carrier invoice captures the invoice details
submitted by your service provider. TM produces a dispute case if your service
provider submits an invoice with charges that differ from those in the original
freight order. The system links the dispute case to the carrier invoice.
●  You work closely with your service provider and either accept or reject the

dispute case for the carrier invoice. When the carrier invoice is successfully
posted to Materials Management (MM), the lifecycle status of the carrier
invoice is set to Accepted.

○  You reject the carrier invoice when you disagree with the service

provider on the carrier invoice. If the carrier invoice has an associated
open dispute case, the system closes the dispute case when you reject
the carrier invoice. You can add a note to the carrier invoice to record the
reason for your rejection.
The lifecycle status of the carrier invoice is set to Rejected.

215


○  You accept the dispute case for the carrier invoice.

TM updates the freight order with the new or changed charges in the
carrier invoice. You can use the background processing function
Creation and Transfer of Freight Settlement Documents to update the
new or altered charges for the freight orders to MM.

●  You use the background processing function Posting of Carrier Invoices to

transfer the carrier invoices ready for posting to Materials Management (MM).
The system creates an incoming invoice in MM. The system posts the carrier
invoices to MM for posting only when the following conditions are satisfied:
○  No dispute case exists, or the dispute case has a lifecycle status of

Resolved.

○  The carrier invoice has a lifecycle status other than Rejected.
○  All the freight orders associated with the carrier invoice have the

invoicing status Completely Invoiced.

○  All the freight settlement documents associated with the freight orders

have the lifecycle status Accruals Posted.

○  The carrier invoice has a block status of Not Blocked.
○  The carrier invoice has a consistency status of Consistent.

## Freight Settlement - Updates

There can be late changes in the freight order requiring changes to logistical data,
which may result in a change in the charges (an increase or decrease). These changes
can occur when the old values have already been transferred to settlement
documents and/or the settlement documents have also been transferred to financials.

Business example:

Accruals are posted when the financial liability is known (for example, departure or
confirmed freight pickup by the carrier). However, there can be mid-execution changes
(for example, diversions (consignee changes), loss of cargo (in transit), unavailability
of cargo, unplanned costs due to detention, demurrages, loading and unloading
activities, tolls, and so on).

These changes may only be known after execution or during the invoicing process
(when the carrier sends the invoice). The configuration of the FSD change process is
done in the Settlement Profile. When an order changes and the invoicing status
changes to Over Invoiced, the system automatically applies the reverse and repost
strategy.

216


Lesson 4 - Distributing Freight Costs

## Objectives

After completing this lesson, you will be able to:

●  Distribute freight costs to relevant sales order items and other transportation

relevant process items.
Include freight costs into the SD billing document.

●

## Cost Distribution

Freight costs incurred by the organization must be allocated to individual cost or profit
centers so that profitability can be properly assessed. In this lesson, you examine the
steps performed by the system in assisting the allocation of freight costs.

To compute true profitability for any manufacturing organization, all operational costs
must be computed correctly. Most organizations would like the freight costs for
material procurement to be included in the material cost. Similarly, for customer
deliveries, the freight cost for the delivery must be considered for margin and
profitability computation. TM can distribute each of the charges used in the freight
cost calculation to the item level of the delivery. The item level cost can then be
processed when the accrual is posted for the supplier freight invoices.

Various scenarios are supported, including the following:

●  Transfer freight costs for inbound deliveries and stock transfers into material

valuation.

●  Post distributed costs to CO so that material-relevant costs can be tracked at
the profit center level. (In such cases, material valuation is not impacted.)
●  Post freight costs back to CO-PA for the customer outbound delivery to be

accounted during profitability analysis.

Cost Distribution Concept

217


The figure, Cost Distribution Concept, shows the data flow. Deliveries are the starting
point for this process. These create freight units, which are later planned to create
freight orders or freight bookings. In addition to the charges in the freight
order/booking, the calculated charges are distributed to the delivery items contained
in the freight order/booking. Afterwards, freight settlement documents are created.
When the FSD and distributed costs are posted, a purchase order and service entry
sheet are created in MM for a subsequent invoice verification process. Also, a
settlement document is created to post the entries to CO-PA, CO, or material valuation.

Cost Distribution Configuration

218


Cost distribution must be enabled in the document type Customizing. Further settings
for cost distribution include distribution profiles, methods, rules, and levels. The
distribution profile is assigned to the organizational unit for charge calculation via the
charges profile.

Cost distribution profiles are used to identify the rules for distributing freight costs. A
profile consists of distribution methods, distribution rules (basis for distribution), and
distribution levels.

TM provides two methods for cost distribution, as follows:

●  Direct:

 This method is normally used when all charges incurred can be distributed to
individual line items of a delivery based on gross weight or volume. Normally,
the charge elements may be calculated at the header or individual item level.

●  Hierarchical:

 This method may be used when the resolution base may include other levels,
such as containers or rail cars. In such cases, there may be charges for the
individual container or rail car, in addition to other charges. So, other charges
must be distributed to the container level first and then the final distribution
should take place to allocate the cost to the line item level.

If necessary, you can add your own distribution methods.

TM supports the following rule basis to be used for cost distribution:

219


●  Gross Weight
●  Gross Volume
●  Net Weight
●  Distance times Weight

The distribution level specifies the target level to which the system allocates
transportation charges for a freight order or freight settlement document.

Posted data can be viewed using the transaction code WLFLTM2 or via Display Cost
Distribution Documents. Distribution data can be searched using the FSD number as
the reference document number.

## Billing Freight Costs

When you sell your products to a customer, you may also take responsibility for
delivering these products to that customer. You incur costs for transportation, for
example, through a carrier. You can pass on these costs to your customers.

You integrate sales orders and deliveries to facilitate transportation planning and
execution in TM. TM creates or updates freight units directly for sales orders or
deliveries. You plan transportation for these freight units by creating orders that you
subcontract to the carrier. The freight order determines the freight costs to be paid to
the carrier. You configure TM to distribute the freight costs in the freight order
according to delivery items. Next, you can add the distributed costs for each delivery
item to the final amount in the billing document to be sent to your customer.

This involves the integration of the following processes:

●  Freight orders in TM
●  Pricing in SD
●  Billing in SD

220


## Note

You must integrate SD with an internal TM component to include the freight cost in
the billing document for all product deliveries.

You can only include the freight cost in a billing document when you have one freight
order document for the delivery and the freight order has only one currency in which
you calculate the cost.

221
