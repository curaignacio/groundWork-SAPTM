# Session 03 — Locations, Zones, Trade Lanes, Modes and Resources

## Overview
This session covers the transportation network: the master data that tells TM where goods can start, stop, transfer and finish, how they can move between those points, and which resources carry or handle them. Locations, zones, lanes, trade lanes, modes, means of transport and resources are all needed before planning or carrier selection can return a sensible result. Many planning errors in later sessions trace back to a missing lane, a missing resource or a mismatched capacity dimension. The session also introduces the path finder, which checks whether a connection exists.

## Transportation network building blocks: locations, transportation zones, transportation lanes, transshipment locations, default routes, schedules and trade lanes; the Transportation Network Cockpit displays locations, zones, lanes, trade lanes, schedules, default routes, connections and business partner networks on a map; planning algorithms use the network to find the most efficient path
The transportation network defines the direct reachability between locations and transshipment locations (S48600). Advanced planning algorithms use the network definition to determine the most efficient path and to assign suitable carriers. They also consider freight and forwarding agreements that contain rates based on trade lanes (S48600).

The key terms (S48600):
- **Locations:** the basic building blocks, marking start and end points of routes.
- **Transportation zones:** group multiple locations, which makes planning and optimization across larger areas easier.
- **Transportation lanes:** define the direct routes between locations and zones.
- **Transshipment locations:** let goods be transferred from one mode of transportation to another.
- **Default routes:** specific paths from source to destination through a sequence of stops. S4TM2 adds that a default route can be used in place of transshipment chains with sales orders and deliveries, forwarding orders and forwarding quotations. It can be modified manually, and is maintained in the Fiori app Define Default Routes.
- **Schedules:** recurring routes with fixed dates and times along a predefined sequence of locations.
- **Trade lanes:** an additional dimension that defines business relationships with customers and carriers.

The **Transportation Network Cockpit** displays locations, transportation zones, transportation lanes, trade lanes, schedules, default routes, connections and business partner networks on a map (S48600).

*What the material does not establish:* S4611 was not read for this guide, so the comparison with the basic scope is not covered here.

## Locations: a logical or physical place where products or resources are managed on a quantity basis; every freight unit has a source and destination location; location types (for example 1001 Production Plant, 1002 Distribution Center, 1003 Shipping Point, 1021 Business Partner, 1100 Port, 1110 Airport) are only a reference and do not control business processes; the address of a shipping point is represented as a location
A location is a logical or physical place where products or resources are managed on a quantity basis (S48600, S4TM2). Products or freight units go from a source to a destination location, may pass through locations on the way, and are loaded and unloaded at them (S48600). To define a location, you specify its name and type.

In TM the location type categorizes locations. Location types are not used to control business processes but serve as a reference (S48600). S48600 lists these standard types: 1001 Production plant, 1002 Distribution center, 1003 Shipping point, 1005 Transportation zone, 1021 Business Partner, 1030 Terminal, 1040 Store, 1100 Port, 1110 Airport, 1120 Railway station, 1130 Container freight station, 1140 Hub, 1150 Gateway, 1160 Container yard, 1170 Warehouse, 1180 Carrier warehouse and 1200 Loading point.

*Source difference:* S4TM2 lists 1190 Rail Junction and 1191 (Border Crossing Point), which S48600 does not, and does not list 1005, 1160 or 1200. Treat both lists as examples, not as complete.

**Integration with S/4HANA (S4TM2).** Plants become location types 1001 or 1002, business partners become 1021, and shipping points become 1003. In SAP S/4HANA each inventory-relevant location can be assigned to one or more shipping points. A shipping point is an independent organizational unit at a fixed location that processes and monitors inbound and outbound deliveries. Its physical address is represented as a location in the master data. With TM in S/4HANA, no integration is needed for material master and business partners, and location master data is created on the fly or by report.

In the Fiori launchpad, the Master Data folder holds Define Location (S4TM2).

*What the material does not establish:* it says location types do not control processes, but what in the master data does drive how a location is used in planning is not stated in the passages read.

## Creating locations: on the fly from sales orders, purchase orders, stock transfer orders and deliveries; with report /SAPAPO/CREATE_LOCATION for plants, shipping points and business partners; with BAdI /SAPAPO/LOC_CREATE when a business partner is saved; one-time locations are transient and used for example in forwarding orders; a business partner can have several locations, one per address
**On the fly.** When TM-relevant documents are created or updated, the system checks that the locations for plants, shipping points and business partners exist, and creates missing ones. The document categories are sales orders (SD), purchase orders and stock transfer orders (MM), and outbound and inbound deliveries (S48600).

**Report /SAPAPO/CREATE_LOCATION.** It creates locations for plants, shipping points and business partners, and suits large numbers of entities. You select from plants, shipping points and business partners, and choose standard addresses only or standard plus delivery addresses. For each selected entity that lacks a location, the system creates a location from the existing address, calculates geocodes, creates a transportation zone location if necessary, and updates the location-to-zone assignment (S48600).

**BAdI /SAPAPO/LOC_CREATE.** It creates locations as soon as a business partner is created and saved. Implementing it lets you specify the conditions for creating or updating a location. After a location exists, later address changes trigger updates (S48600).

**One-time locations.** Locations that need not be stored permanently are one-time locations, stored as a transient master data object. They are used in processes that need locations not defined as master data, such as creating forwarding orders. The system creates them from one-time address details. A one-time location is characterized by the organization's name, address data, communication data, or a combination, and has one note per location and language (S48600).

**Locations of business partners.** A business partner can have several standard and delivery addresses and needs one valid standard address at any time. Several locations can be assigned to one business partner, one per relevant address, and the location's address number matches that of the business partner. When TM receives a sales document or outbound delivery, it uses the address data and validity dates to find the right location (S48600).

If S/4HANA integration through the DRF is used, transportation zones are created automatically from the address of the location and the location is assigned to that zone (S4TM2).

## Geocoding: geo-coordinates (longitude, latitude, altitude) are derived from the address; standard SAP applications determine them at region level, which suffices unless distances, durations or map display are needed; the Precision field shows the granularity; two geocoding levels exist, standard (in the license) and full addresses (depends on the geocoding software)
A location is a point on the earth's surface defined by longitude, latitude and altitude. These coordinates are determined from the address data (country, region, postal code, city, district, street, house number and more). Determining coordinates from address data is geocoding (S4TM2).

- Standard SAP applications determine a geo-coordinate at region level when you create or change the location address. This is enough for processes that do not work with static information or depend on distances, times or map display.
- Because coordinates are the basis for distance and duration determination and map display, they must be high quality if those functions are needed.
- Coordinates appear in degrees, minutes and seconds in the Geographical Data area of the Location UI and can be overwritten manually. The Precision field indicates the granularity of the geocoding result.
- Two levels: standard (included in the SAP TM license) and full addresses (depending on the capabilities of the geocoding software). The program supplied by SAP determines longitude and latitude from country and region code. The material names Google, Here, Rand-McNally, PC-Miler and PTV (Karlsruhe, Germany) as companies providing geocoding products.

## Transshipment locations: used to unload goods from one freight order or vehicle resource and load them onto another, for different means of transport or carriers (for example truck-ocean-truck) or for consolidation and deconsolidation; defined by assigning them to a location or transportation zone
A transshipment location is used to unload goods from one vehicle resource (S48600) or freight order (S4TM2) and load them onto another during transportation. It applies when different means of transport or carriers are needed, for example truck-ocean-truck or truck-rail-truck, and for consolidation or deconsolidation (S4TM2, S48600).

It is defined by assigning it to another location or to a transportation zone. When assigned to a zone, it can serve as transshipment location for all locations in that zone (S48600). The assignment is made with Define Transshipment Location Assignments (H03). H03 gives two examples, both assuming the respective transportation lanes exist:
- Transshipment location B defined for location A, goods going A to C: either A to C directly, or A to B to C.
- B defined for A and C defined for D, goods going A to D: A to D, A to B to D, or A to C to D.

## Transportation zones: group locations (including one-time locations and subzones) so that zone properties pass to the locations and less master data is needed; they have no address but can have coordinates, either calculated as the center point of the included locations or entered manually; types are region, postal code, direct and mixed
A transportation zone is a business object that aggregates multiple locations. The system can propagate properties assigned to a zone to all its locations, which minimizes the master data (S48600, S4TM2). Zones can contain individual locations, one-time locations and subzones. An example is all locations supplied by the same warehouse (S48600). Zones are typically the origin and destination of transportation lanes (S4TM2).

Zones are not physical, so they have no address, but they can have geographical coordinates. The system can estimate the center point from the coordinates of all included locations, or you can enter them manually (S48600, S4TM2). Each zone is identified by its name and type together (S48600).

| Type | How locations are assigned | Remark from the material |
|---|---|---|
| Direct | By entering each location | A low-volume customer can be put in a larger zone to improve optimization results (S4TM2) |
| Postal code | By a valid postal code range for a country or region | Carriers often publish rates and transit times by three-digit zip code ranges, such as 170-173 (S4TM2) |
| Region | By country/region and region. If only a country/region is entered, all its regions are included | Example: US-Illinois (S4TM2) |
| Mixed | A combination of the other types | |

## Transportation zone hierarchy: properties of higher-level zones pass to lower levels; a zone cannot be assigned to itself or to a zone it already contains; a zone can be in any number of higher-level zones and a location in any number of zones; the VSR optimizer, lane determination and transshipment location determination consider the hierarchy
A hierarchy structures zones by assigning one zone to another, so all locations of a subordinate zone become part of the superordinate zone. Zones inherit the properties of their superior zone (S48600). This reduces master data (S4TM2).

Rules (S48600, S4TM2):
- A zone cannot be assigned to itself.
- A zone cannot be assigned to a zone that already contains it.
- A zone can be assigned to any number of higher-level zones.
- A location can be assigned to any number of zones.
- A zone cannot be assigned to a location.

The hierarchy is used (S48600) by the VSR optimizer during the optimization run, by lane determination when identifying a specific transportation lane, and by transshipment location determination to find all valid transshipment locations for a location. In the Fiori launchpad it is shown through Master Data, Define Zone Hierarchy (S4TM2).

## Transportation lanes: express direct reachability between two locations, two zones or a mix for a specific means of transport; a lane points in one direction only, so the reverse needs another lane; at least one means of transport must be assigned, carriers can be assigned per means of transport (with cost, priority, share of business or capacity), and carriers are needed for automatic carrier selection; created in the Define Transportation Lane app
A transportation lane is a relationship between two locations, two zones, or a location and a zone. It expresses the direct reachability of the locations (or of all locations in the zones) for a specific means of transport (S48600, S4TM2, H03). Using zones as source, destination or both reduces the number of lanes to maintain. A lane points in one direction only, so the reverse direction needs another lane (S48600, S4TM2).

A lane controls which location can forward goods to another, which means of transport can be used, and which carrier can supply a vehicle for that means of transport (S48600). It is defined by source, destination, direction, available means of transport (MTr) and optionally a carrier per MTr. It can be maintained individually or by mass maintenance (S48600).

**Creating a lane (H03, S48600).** In the Define Transportation Lane app, enter the source and destination on the Tr.Lane tab, or define an intrazone lane (by zone) or a location transportation lane (by location) on the Intra-Zone Lane/Loc. Transp. Lane tab. A location transportation lane has no impact on the reachability of locations. It can help for initializing transportation allocations, for example by limiting a carrier's freight orders from or to a location within a planning period (H03). Prerequisites: means of transport defined, at least two locations or zones, and the Carrier role on any carrier BP you want to assign.

**Means of transport and carriers.** The creation of a lane requires at least one means of transport. Attributes such as duration, distance and costs for the means of transport must be specified. A carrier provides service along the lane for a specific means of transport and is assigned by linking it to the MTr. You can then specify attributes such as transportation costs, priority, share of business or capacity for transportation allocation. To enable automatic carrier selection, carriers must be assigned to means of transport (S48600).

## Trade lanes: abstract, context-independent classification of transport with an orientation (Inbound, Outbound, From, To, Within, Along), source and destination, optionally a mode and means of transport; they form hierarchies and can overlap; they do not replace transportation lanes and have no direct link to them
A trade lane defines a transportation direction characterized by an orientation (Inbound, Outbound, From, To, Within, Along), a source and a destination, and can have a mode and means of transport. It is an abstract classification: an instance does not represent a connection between network nodes. Examples are all transports from Hamburg to New York, all transports within Germany, and all transports that leave Bavaria (S48600, S4TM2).

- **Hierarchy:** more generic trade lanes include more specific ones, for example "Within Germany using means of transport Truck" includes "Within Bavaria using means of transport Truck for liquids". Hierarchies can combine zone hierarchies ("From Germany" includes "From Bavaria", which includes "From Plant_Munich"), MTr hierarchies and mode-to-MTr relations (S4TM2, S48600).
- **Overlap:** for example "From Germany using Airplane" and "Within Europe using Airplane" (S48600).
- **No link to transportation lanes:** trade lanes do not replace them, and there is no direct link between the two (S48600, S4TM2).
- **Use as master data:** in previous releases trade lanes were created from and associated with other business objects (business shares, allocations, freight agreements). Now they can be master data objects that you create, copy and reuse, with a worklist that includes a where-used list (S48600). S48600 also says agreements contain rates based on trade lanes.

## Transportation mode and means of transport: the mode is the highest-level grouping (categories road, rail, sea, air, postal service, inland waterways); the main carriage mode holds the shipment documents in multistage shipments; a means of transport describes a vehicle type and carries mode, multi-resource, scheduled, own means of transport and GIS quality settings; UN/EDIFACT standard codes include 006 Aircraft, 011 Ship, 031 Truck, 038 Car; without a GIS, average speed and distance factor estimate transit time
**Mode.** The transportation mode is the highest-level transport grouping, such as road, rail, inland waterway, sea or air, and each means of transport is assigned a single mode. SAP categories: road, rail, sea, air, postal service and inland waterways. A dangerous goods transport category can be added. Category 99 (all modes) is used in the US under 49 CFR, and customers can use categories 30-89 for their own definitions (S4TM2).

**Main carriage.** A mode can be set as the Main Carriage. In export scenarios you can have precarriage, main carriage and on-carriage. In a multimodal or multistage shipment, the main carriage stage contains all the shipment documents and allows pre- and on-carriage stages to be linked to it. Modes can also be used at a high level to determine incompatibilities (S4TM2).

**Means of transport.** It describes the characteristics of a vehicle type or classification, for example a refrigerated truck, a 60-foot rail boxcar or a bulk container. It describes the cost structure and geographic availability of a class of vehicle. Vehicle resources assigned to it share physical characteristics such as mode, capacity, speed, cost structure, geographic availability and temperature control (S4TM2). It is defined in Customizing under Transportation Management, Master data, Resources, Define Means of Transport and Compartment, Define Means of Transport (S4TM2). Settings (S4TM2):
- Transportation mode
- Multi-resource
- Scheduled means of transport: whether the resource travels on a fixed schedule such as a sailing or rail schedule
- Own means of transport: whether the resource is part of your own fleet or an external provider's
- GIS quality: integration with a third-party geographical information system, which makes routes (interstate highways or county roads) and expected speeds specific

**Standard codes (UN/EDIFACT).** 006 Aircraft, 011 Ship, 031 Truck, 038 Car (S4TM2).

**Without a GIS.** You can specify an average speed per means of transport. Speed and the distance from the transportation lane give the transit duration. The distance factor accounts for the difference between the linear distance of two locations and the actual distance covered, so you can estimate the actual distance from the linear one (S4TM2). H03 also lists a setting No Transportation Lanes Required, which activates planning with an unlimited network so a vehicle resource of that means of transport can travel between all locations, relevant for VSR optimization and scheduling.

## Multi-resource: a means of transport can be flagged so that the system assumes a defined number of resources (unlimited if none given) instead of individual resources; the number is the maximum of parallel freight orders per resource and it can model an external fleet in one step
Instead of creating individual resources for a means of transport, you select the Multi-Resource checkbox. During planning the system assumes the number of resources you define, and unlimited if you give no number. During vehicle scheduling and preprocessing, the number is the maximum of parallel freight orders the system may create for each resource (S4TM2). Multiresources can model an external fleet in one step (S4TM2). H03 states the use case: an unlimited number of resources is available for a means of transport but you want to define the settings only once. For container resources you can also set single resource or multiresource (H03).

## Path finder: searches legs in the network over locations, transshipment locations, transportation lanes, schedules and zones to show whether a connection exists and master data is correct; it runs in the transportation network cockpit (Find Path To Location) or on the transportation proposals UI, and as report /SCMTMS/FIND_TN_PATH; it does not consider incompatibilities
The path finder searches for legs in the network, considering locations, transshipment locations, transportation lanes, schedules and transportation zones. It shows whether a connection exists between two locations and so whether master data is correctly configured. The planner must establish that all network elements are maintained correctly so the optimizer can find a valid solution (S4TM2, S48600).

**Where it runs (S4TM2, S48600).**
- **Transportation Network Cockpit:** from the context menu of a location, choose Find Path To Location and enter a destination. The system shows all available connections on the map, and the color indicates whether a valid transportation lane or schedule exists.
- **Transportation proposals UI:** a button shows or hides the available connections on the map, with the same color logic.
- **Explanation tool:** with freight units selected, Show Network Path analyzes the network considered when planning them. Its request is source and destination, options Determine path and Determine connections, and restrictions are outbound, inbound or implicit hub, transportation mode and means of transport.
- **Report /SCMTMS/FIND_TN_PATH:** input is a start and destination location. Using assigned transshipment locations and existing connections (lanes, schedules and booking), it tries to find all paths and states for each stage whether a valid connection exists. It shows, for example, a transshipment location that is assigned but cannot be reached from the start location.

**Limits.** The path finder does not take incompatibilities into consideration (S4TM2). The report cannot search within a time frame or respect the validity of connections, and its mode and means-of-transport filters are not available (S4TM2).

## Resource types: vehicle, handling, calendar and transportation unit resource (H03 also lists driver); a vehicle resource is a unit load with up to eight capacity dimensions that planning only uses if they match a freight unit building rule, and can be active or passive; Factory Calendar, Continuous Dimension, Capacity and Unit of Measure are mandatory
Resources are central to planning and execution. Their data is relevant to planning order dates, taking working times and available capacities into account. With bookings, resources provide the capacity for transportation, loading and unloading of freight units (S4TM2, S48600).

| Resource type | What it models |
|---|---|
| Vehicle resource | Moving resources such as trucks, rail cars, planes and ships. Each is a unit load: one trailer, container or rail car of a certain capacity |
| Handling resource | Handling capacity to load and unload vehicle resources (for example door, loading ramp, forklift) |
| Calendar resource | Operating hours of locations |
| Transportation unit resource | An individual container with its capacity and availability |

H03 also lists Driver in its resource types (see Session 02 for the driver data).

**Vehicle resource details (S4TM2, H03).**
- Up to eight dimensions and units of measurement define capacity, for example 40,000 lb, 2200 cu ft or 24 pallets. Mass and volume are predefined by default. Planning can only take the vehicle capacity into account if the dimensions and units correspond to those in a freight unit building rule.
- The available capacity cannot depend on time. A time-dependent availability can be defined using shift sequences (H03).
- A vehicle resource is assigned to a means of transport, which is assigned a mode. Vehicle group and vehicle type specify physical properties and can serve as a template for resources or be requested in a forwarding or booking order (H03).
- Active vehicle resources travel by themselves (a truck with a motor). Passive ones do not (an empty trailer with no tractor) (S4TM2). In Customizing this comes from the Passive Means of Transport checkbox (H03).
- Define the means of transport and factory calendar before creating the resource. Recommended input: resource name, calendar and time zone, capacity. Mandatory fields: Factory Calendar, Continuous Dimension, Capacity and Unit of Measure (S4TM2).
- In the planning profile you can specify whether manual overload of capacity is allowed (H03).

**Transportation unit resource (S4TM2, H03).** Up to eight dimensions, mass and volume predefined, same freight unit building rule condition as for vehicles. It can be created with reference to an equipment group and type, requested in a forwarding or booking order, and has parameters such as capacity, minimum number of seals, physical properties, downtimes, grouping attributes and alternative names.

## Other resource objects: compartments divide a vehicle resource and support incompatibilities (for example dangerous goods areas); means-of-transport combinations model truck and trailer; handling resources (door, loading ramp, forklift) give loading and unloading capacity; calendar resources set location operating hours; transportation unit resources represent containers; resource classes are determined from the means of transport or equipment group
**Compartments (S4TM2).** They divide a vehicle resource (truck or trailer) into smaller units, with capacity constraints, in flexible or fixed form. Incompatibilities can restrict freight units from certain compartments, for example for temperature reasons. Compartments let you assign dangerous goods to certain areas of the truck.

**Means-of-transport combinations (S4TM2, H03).** They model truck and trailer combinations. You specify the number of objects of each MTr, for example one truck and two trailers, the maximum capacities of the combination, free attributes for compatibilities and incompatibilities, and coupling/uncoupling durations per passive MTr. H03 states a combination consists of one means of transport that can move independently and can move at least one passive MTr. With your own fleet, vehicle-resource combinations let VSR optimization couple and uncouple dynamically. Without your own fleet, combination resources let VSR optimization work on the combination level.

**Handling resources.** They offer handling capacity for loading and unloading vehicle resources. They maintain downtimes, restrictions on simultaneous activities, availability, qualification and equipment requirements. Availability is maintained through capacity variants and shift sequences (S4TM2). The consumed capacity per loading and unloading operation is kept in the location master data, with the (MTr-specific) handling resource assignment, and the available capacity is kept in the resource master data (S4TM2). S48600 adds parameters such as resource template, capacity profile (for example a dock with 50 doors in the morning and evening and fewer during the day), availability, downtimes, qualifications, attached equipment and grouping attributes.

**Calendar resources.** They determine the operating hours of locations, and loading and unloading can only happen in operating hours. They can be assigned to several locations as inbound or outbound operating hours, plus means-of-transport specific inbound and outbound hours (S4TM2). A calendar resource is assigned to a calendar and optionally to a shift, mainly for scheduling goods receipt and goods issue processing time (S48600, H03). A capacity profile cannot be defined for it (H03).

**Resource classes (H03).** Classes group resources with the same characteristics. You assign a resource class to a means of transport or equipment group, and the system assigns it automatically to the resource. Without an assignment, the defaults for vehicle resources are by mode and passive flag (road: truck, or trailer if passive; rail: locomotive or rail car; sea: vessel; air: airplane). Handling resources default to Doors and transportation unit resources default to Container.

## Incompatibilities for resources in the exercise: incompatibilities define objects that must not be combined, for example ice cream and vehicles without a cooling unit; INC_S4TM1_VEH_FU links freight units to vehicle resources/types, and violations can be allowed or forbidden separately for manual planning and VSR optimization
In the Review Incompatibility simulation (E01), you open the Edit Incompatibility app from the Profiles and Settings group. Incompatibilities specify which objects should not be combined during transportation, for example ice cream and vehicles that lack a cooling unit.

- **Incompatibility INC_S4TM1_VEH_FU:** it is defined between freight units and vehicle resources or vehicle types (incompatibility type 04).
- **Area 01:** the incompatibility is checked in all automatic planning applications (VSR optimization, load planning, load consolidation, creation of transportation proposals) and in all manual planning activities. Other areas exist.
- **Violation settings:** you can specify separately whether the system may violate the incompatibility in manual planning or in VSR optimization. For example, violations can be forbidden in automatic planning while manual overrides are allowed with only a warning.
- **Conditions:** freight units for which condition INC_S4TM1_FU returns X (for example those containing ice cream) are incompatible with vehicle resources or types for which the second condition INC_S4TM2_RES returns T (for example those without a cooling unit).

Incompatibilities can be quite complex in real business environments (E01).

## Practice
Create a network design sheet for a small example flow: a plant, a port and a customer zone.
1. List the locations with their types and the geocoding approach you would use for each.
2. Describe the zone and its type.
3. List the transportation lanes in both directions, with means of transport and carrier for each.
4. Add one trade lane.
5. List the vehicle, handling and calendar resources needed.
6. Add a note on how the path finder would confirm the connection, and what it would not check.

## Self-check
Can I explain how locations, zones, lanes, trade lanes, modes and resources fit together in the transportation network to a project stakeholder without notes?
