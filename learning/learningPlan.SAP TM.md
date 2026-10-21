# {Subject} — Learning Plan

<!--
FORMAT REFERENCE ONLY — the example below is not a session. Keep this comment in place.

Written session by session by learningPlanner, one approved session at a time.
Read by sessionWrite, studyGuideCreator (via the session files), podcastPrompter,
questionnaire, and chatQuiz when sessions are referenced.

This file is the source of truth for all learning artifacts.

Session numbers use 01, 02, 03 format throughout. Sessions are separated by a
horizontal rule. Sections marked (tier: inferred) are inferred rather than extracted
from src/ — studyGuideCreator strips these markers from the learner-facing HTML.

Session block format:

## Session {NN} — {Title}

### Knowledge items
- {item}

### Skill items (tier: inferred)
- {item}

### Important questions
- {question}

### Deliverable (tier: inferred)
{deliverable description}

### Self-confidence question (tier: inferred)
{question}

### Quiz questions
```yaml
- q: {stem}
  o: [{option 0}, {option 1}, {option 2}, {option 3}]
  a: 0
  e: {explanation}
```

---
-->

## Session 01 — SAP TM in SAP S/4HANA: Overview and Fiori Experience

### Knowledge items
- Basic shipping (LE-TRA) versus Transportation Management: LE-TRA is part of the compatibility scope and its code line is kept within SAP S/4HANA Enterprise Management until end of 2030; TM has been part of SAP S/4HANA since 1709, and its advanced functions require an additional license
- Advanced TM plans from orders (sales orders, purchase orders, MM scheduling agreements) as well as from deliveries, and can combine inbound and outbound deliveries in one freight order; its differentiators are vehicle scheduling and routing, carrier selection, load consolidation and load planning; long term the LE-TRA shipment is replaced by the TM freight order
- The five main stages of TM: Requirements and Order Management, Transportation Planning, Transportation Execution, Freight Costing and Settlement, Analytics and Collaboration; and the scenario, shipping, movement and stage types TM supports
- The core TM objects: OTR, DTR, freight unit (FU), freight order (FO), freight agreement (FA) and freight settlement document (FSD)
- The SAP Fiori user experience and access to TM: role-based apps and the launchpad, catalogs, groups, spaces and pages; business catalogs and role templates; the three Fiori app types; the SAP Fiori Apps Reference Library; the Personal Object Worklist (POWL)

### Skill items (tier: inferred)
- Tell basic shipping from advanced TM when scoping a requirement
- Place a business activity in one of the five TM stages
- Use the TM object abbreviations correctly when reading a document
- Find a TM app through the launchpad and the SAP Fiori Apps Reference Library
- Set up and reuse a worklist query

### Important questions
- How do LE-TRA and TM relate, and what is the difference between basic shipping and advanced TM?
- What happens in each of the five stages of TM?
- What does each core TM object (OTR, DTR, FU, FO, FA, FSD) represent?
- How are tiles organized in the SAP Fiori launchpad, and how do they reach a user?
- How do the three SAP Fiori app types differ?
- What is the POWL for?

### Deliverable (tier: inferred)
A one-page "TM map": a table of the five stages, each with its main object and one activity, plus a short comparison of basic shipping and advanced TM with two differences taken from the course material.

### Self-confidence question (tier: inferred)
Can I explain to a business stakeholder, without notes, how a sales order becomes a freight order and a settled carrier invoice in TM?

### Quiz questions
```yaml
- q: Until when is the LE-TRA code line kept within SAP S/4HANA Enterprise Management?
  o: ["End of 2025", "End of 2030", "End of 2035", "The 2020 release"]
  a: 1
  e: "LE-TRA is part of the compatibility scope, and its code line is kept within SAP S/4HANA Enterprise Management until end of 2030 (S4611, Basic Shipping - LE-TRA and TM)."
- q: Which TM object replaces the LE-TRA shipment in the long term?
  o: ["The freight unit", "The delivery-based transportation requirement", "The freight agreement", "The freight order"]
  a: 3
  e: "S4611 states that long term the shipment from LE-TRA will be replaced by the freight order from TM."
- q: What does advanced transportation management allow that basic shipping does not?
  o: ["Early planning based on orders as well as on deliveries", "Posting goods issue for outbound deliveries directly in TM", "Creating outbound deliveries directly from sales orders", "Maintaining business partner master data for carriers"]
  a: 0
  e: "Advanced TM allows early planning based on orders (sales orders, purchase orders, MM scheduling agreements) in addition to planning based on deliveries, which is the only option in basic shipping (S4611)."
- q: What is the correct sequence of the five main stages of TM?
  o: ["Transportation Planning, Requirements and Order Management, Transportation Execution, Analytics and Collaboration, Freight Costing and Settlement", "Transportation Execution, Transportation Planning, Requirements and Order Management, Freight Costing and Settlement, Analytics and Collaboration", "Requirements and Order Management, Transportation Planning, Transportation Execution, Freight Costing and Settlement, Analytics and Collaboration", "Requirements and Order Management, Transportation Execution, Transportation Planning, Analytics and Collaboration, Freight Costing and Settlement"]
  a: 2
  e: "S48600 lists the five stages in this order: Requirements and Order Management, Transportation Planning, Transportation Execution, Freight Costing and Settlement, Analytics and Collaboration."
- q: What is the smallest planning unit used in transportation planning?
  o: ["The freight order", "The freight unit", "The order-based transportation requirement", "The freight settlement document"]
  a: 1
  e: "S48600 describes a freight unit as the smallest planning unit used in transportation planning, representing a collection of goods that can be transported together throughout the complete transportation process chain."
- q: What is the freight settlement document (FSD) used for?
  o: ["To verify the carrier invoice", "To represent a contract with the carrier", "To represent demand from a sales, purchase or stock transport order", "To represent a set of goods transported together"]
  a: 0
  e: "In the S48600 table of common terms, the freight settlement document is the object used to verify the carrier invoice; the contract with the carrier is the freight agreement."
- q: What is a catalog in the SAP Fiori launchpad?
  o: ["A collection of pages inside a space", "The semantic structure of the content of a page", "The entry point for a business role", "A set of tiles made available for one role"]
  a: 3
  e: "S48600 defines a catalog as a set of tiles that you want to make available for one role; catalogs are assigned to business roles. A space is the entry point for a business role."
- q: Which SAP Fiori app type uses the analytical capabilities of SAP HANA?
  o: ["Transactional apps", "Fact sheet apps", "Analytical apps", "SAP CoPilot apps"]
  a: 2
  e: "S4611 states that analytical apps use the analytical capabilities of SAP HANA to provide insights in business data; transactional apps use ABAP and fact sheet apps use Enterprise Search."
- q: Which business catalog covers Transportation – Planning for the Transportation Manager role?
  o: ["SAP_TM_BC_OM", "SAP_TM_BC_PLN", "SAP_TM_BC_STLM", "SAP_TM_BC_CTRM"]
  a: 1
  e: "H02 lists SAP_TM_BC_PLN as the technical name of Transportation – Planning; SAP_TM_BC_OM is Order Management, SAP_TM_BC_STLM Settlement and SAP_TM_BC_CTRM Contract Management."
- q: What does the Personal Object Worklist (POWL) let users do?
  o: ["Replace the business catalogs assigned to a role with personal tile groups", "Generate freight units directly from sales orders and purchase orders", "Define and store queries in a similar way to ERP selection screen variants", "Assign business roles to users and manage their launchpad catalogs"]
  a: 2
  e: "S48600 describes the POWL as giving central, personalized access to document lists, where users can define and optionally store queries similar to SAP ERP selection screen variants."
```

---

## Session 02 — Business Partners and the Organizational Model

### Knowledge items
- Business partner master data: in SAP S/4HANA the master data of customers and vendors is managed as business partners (previously handled separately in SAP ERP); it is maintained with transaction BP or a Fiori app, a business partner can be assigned to multiple company codes, and it is categorized as person, organization or group (S4TM2 Lesson 1; S48600 Business Partner)
- Business partner roles: general data is defined once and roles are assigned for each business context; the role General Business Partner (000000) is assigned automatically on creation; roles most used in TM include FLCU01 Customer, FLCU00 FI Customer, FLVN01 Vendor, FLVN00 FI Vendor, CRM010 Carrier, TM0001 Driver, BUP004 Organizational Unit, BUP001 Contact Person (S48600 Business Partner; S4TM2 Lesson 1; H03)
- Organizational levels of the roles: FLCU01 allows data on sales area level (TM defaults distribution channel and division in Define General Settings for TM), FLVN01 and CRM010 on purchasing organization level, FLCU00 and FLVN00 on company code level (S48600; H03; E01)
- Carrier and driver data: role CRM010 contains the data of role FLVN01 plus TM-specific data (Regulated Agent Code, IATA Agent Code, CASS Account, SCAC Codes, Airline Codes, Service Level Codes, Carrier Service Codes); the Transport Data tab appears for the Carrier role; role TM0001 holds home location, qualifications, shift sequences, validity periods and absences (H03; E01; S48600)
- Partner functions: a partner function is the role a business partner takes in a process (for example sold-to party, ship-to party, payer, bill-to party, consignee, shipper, carrier, driver, freight forwarder); one partner can have several functions; no special BP roles are needed in Customizing for partner functions, and the system can check that a BP is compatible with a document partner function (S4TM2 Lesson 1; H03)
- Business partner determination: a partner determination profile (Customizing, Master Data, Business Partners, Define Partner Determination Profiles) sets the partner functions available in a document, the level of control the user has, and how partners are determined; it is assigned to document types such as forwarding orders, freight orders, freight bookings, settlement documents, agreements and RFQs (S4TM2 Business Partner Determination; S48600)
- Ways to determine a partner: partner function with source partner function, source partner function in the BP master data (BP Relationship), a fixed business partner for a partner function (may not yet exist in the Customizing system), and relationship category (S4TM2 Business Partner Determination; H03)
- Business partner relationships, texts and blocking: relationship category Has Contact Person is used in tendering and Has Subsidiary / Agent describes subsidiaries and agents of a carrier; additional texts serve as printing addresses or signatures; a BP can be blocked for forwarding quotations and orders at complete BP, company code, purchasing organization or sales organization level (H03)
- Carrier profile: a profile characterizing a carrier's transportation capabilities, one per carrier with the Carrier role; it can hold freight code sets, transportation lane and carrier-specific parameters, product freight groups, transportation groups, equipment groups and types, fixed transportation costs and dimension costs; it is used for transportation proposals and carrier selection (H03)
- Organizational structure in TM: optional corporate organization, company organization (company code, local currency, legal entity), sales organization (forwarding orders, quotations, forwarding settlements), purchase organization and group (freight orders, bookings, freight settlements), planning and execution organization (resources, freight orders) and forwarding house (sales, purchasing and planning/execution in LSP scenarios); units map to S/4 units through the BSG Org. Unit field; plants and shipping points are created as locations (S48600 Organizational Structure; H03)
- Organizational model rules: organizational units have a unit function (sales 4, purchasing 2, forwarding house 89) and a unit role (Organization, Office, Group); the hierarchy is fixed (for example Group under Office or Organization, Office under Organization; for purchasing and planning/execution only Group under Organization); /SCMTMS/ORG_INT transfers units from S/4HANA core components; optional checks ensure carrier and customer BPs belong to a sales or purchasing organization of their company or of the document header (H03)
- Material master attributes relevant to TM: base unit of measure, alternative units of measure, gross weight, net weight, volume, transportation group (for example palletized or refrigerated goods) and material freight group, which is transferred from the sales order item to the product item of the freight unit (S48600 Material Master)

### Skill items (tier: inferred)
- Look up a carrier business partner in the Maintain Business Partner app and identify where its TM-specific data and purchasing organization data are held
- Choose which business partner role to assign for a given party (customer, vendor, carrier, driver) and explain which organizational level its data belongs to
- Trace how a partner determination profile would fill a partner function such as invoicing party from a given setup
- Sketch a simple TM organizational structure for a company and map each unit to the documents it is used in
- Read a material master record and name the fields that TM uses for transportation

### Important questions
- Why does S/4HANA manage customers and vendors as one business partner with roles instead of separate masters, and what does the role concept avoid?
- Which business partner role holds data at sales area, purchasing organization and company code level, and why does that matter for TM documents that have no distribution channel or division?
- What is the difference between a business partner role and a partner function?
- In which situations would each of the four ways to determine a business partner be the more suitable one?
- Why does TM need organizational units of its own, and how do they connect to the S/4HANA organizational units?
- Where would you maintain the transportation capabilities of a carrier, and which TM processes read them?

### Deliverable (tier: inferred)
A one-page business partner and organization map for a fictional logistics service provider: its carrier, customer and driver business partners with the roles assigned, one partner determination example for invoicing party, and a small organizational model showing corporate, company, sales, purchasing and forwarding house units with the documents each serves.

### Self-confidence question (tier: inferred)
Can I explain business partner roles, partner determination and the TM organizational structure to a project stakeholder without notes?

### Quiz questions
```yaml
- q: Which business partner role contains the data of role FLVN01 (Vendor) plus TM-specific data such as SCAC Codes and Airline Codes?
  o: ["TM0001 (Driver)", "FLCU01 (Customer)", "CRM010 (Carrier)", "BUP004 (Organizational Unit)"]
  a: 2
  e: "H03 states that the role CRM010 (Carrier) contains the data of role FLVN01 (Vendor) plus additional TM-specific data such as Regulated Agent Code, IATA Agent Code, CASS Account, SCAC Codes, Airline Codes and Service Level Codes. The same is shown in E01, Review Carrier Information."
- q: At which level do the roles FLVN01 (Vendor) and CRM010 (Carrier) allow data to be maintained?
  o: ["Purchasing organization", "Sales organization level", "Company code level", "Plant or storage location level"]
  a: 0
  e: "H03 and E01 state that FLVN01 and CRM010 permit data maintenance at the purchasing organization level, for example order currency and payment terms agreed with the carrier. FI Customer and FI Vendor work at company code level."
- q: Which role does the system assign automatically when a business partner is first created?
  o: ["Organizational Unit (BUP004)", "Vendor (FLVN01)", "Carrier (CRM010)", "General Business Partner"]
  a: 3
  e: "S4TM2, Lesson 1 - Business Partners, states that when you first create a business partner the BP role General Business Partner is automatically assigned; S48600 (Business Partner) says the same."
- q: In Customizing the partner function Invoicing Party has source type Partner Function and source function Sold-to Party. A user enters Customer01 as sold-to party. What does the system do?
  o: ["It leaves the invoicing party empty for manual entry", "It assigns Customer01 as the invoicing party", "It reads the invoicing party from the BP relationship", "It copies the carrier into the invoicing party"]
  a: 1
  e: "S4TM2, Business Partner Determination, gives exactly this example. The system copies the business partner entered in the source partner function, so Customer01 becomes the business partner for the invoicing party."
- q: Which BP relationship category is used in the tendering process?
  o: ["Has Subsidiary / Agent", "Has Employee", "Has Customer", "Has Contact Person"]
  a: 3
  e: "H03, Definition of Business Partners, notes that the relationship category Has Contact Person is used in the tendering process, while Has Subsidiary / Agent describes subsidiaries and agents of a carrier organization."
- q: How many carrier profiles can you create for one carrier?
  o: ["Only one profile per carrier", "One profile per means of transport", "One profile per purchasing organization", "One profile per transportation lane"]
  a: 0
  e: "H03, Carrier Profile, states that carriers are business partners with the role Carrier and that you can only create one profile for each carrier."
- q: Which TM organizational unit is optional and serves as a single entry point into the organization's structure?
  o: ["Company organization unit", "Forwarding house", "Corporate organization", "Planning organization unit"]
  a: 2
  e: "S48600 (Organizational Structure) and H03 (Organizational Management) describe the corporate organization as optional and a single entry point into the structure in TM; the company organization corresponds to the company code."
- q: How can a forwarding house be used in TM?
  o: ["As a sales organization or a corporate organization", "As both a sales and a purchasing organization", "As a purchasing organization or a planning group", "As a company organization or a planning group"]
  a: 1
  e: "H03, Organizational Management, states that in TM a forwarding house (function 89, role 1) can be used as a sales organization and as a purchasing organization. S48600 adds that it can handle sales, purchasing and planning/execution activities."
- q: The material freight group of a material is transferred from the sales order item to which TM object?
  o: ["The item of the forwarding quotation", "The stop of the freight order", "The leg of the transportation lane", "The freight unit product item"]
  a: 3
  e: "S48600, Material Master, states that in TM the material freight group is transferred from the sales order item to the product item of the freight unit; it is used to determine freight classification and freight code."
- q: What does the BSG Org. Unit field do in SAP S/4HANA TM?
  o: ["Maps TM units to S/4 org units", "Links business partners to company codes", "Assigns locations to transportation zones", "Connects carriers to purchasing groups"]
  a: 0
  e: "S48600, Organizational Structure, states that SAP S/4HANA TM maps its organizational units with S/4 organizational units through the BSG Org. Unit field. H03 adds that it holds the ID used to retrieve sales or purchasing organization-dependent business partner data."
```

---

## Session 03 — Locations, Zones, Trade Lanes, Modes and Resources

### Knowledge items
- Transportation network building blocks: locations, transportation zones, transportation lanes, transshipment locations, default routes, schedules and trade lanes; the Transportation Network Cockpit displays locations, zones, lanes, trade lanes, schedules, default routes, connections and business partner networks on a map; planning algorithms use the network to find the most efficient path (S48600 Transportation Network Overview; S4611)
- Locations: a logical or physical place where products or resources are managed on a quantity basis; every freight unit has a source and destination location; location types (for example 1001 Production Plant, 1002 Distribution Center, 1003 Shipping Point, 1021 Business Partner, 1100 Port, 1110 Airport) are only a reference and do not control business processes; the address of a shipping point is represented as a location (S48600 Locations; S4TM2 Location Master)
- Creating locations: on the fly from sales orders, purchase orders, stock transfer orders and deliveries; with report /SAPAPO/CREATE_LOCATION for plants, shipping points and business partners; with BAdI /SAPAPO/LOC_CREATE when a business partner is saved; one-time locations are transient and used for example in forwarding orders; a business partner can have several locations, one per address (S48600 Locations; S4611)
- Geocoding: geo-coordinates (longitude, latitude, altitude) are derived from the address; standard SAP applications determine them at region level, which suffices unless distances, durations or map display are needed; the Precision field shows the granularity; two geocoding levels exist, standard (in the license) and full addresses (depends on the geocoding software) (S4TM2 Geocoding Locations)
- Transshipment locations: used to unload goods from one freight order or vehicle resource and load them onto another, for different means of transport or carriers (for example truck-ocean-truck) or for consolidation and deconsolidation; defined by assigning them to a location or transportation zone (S4TM2 Border Crossing Point; S48600 Transshipment Location)
- Transportation zones: group locations (including one-time locations and subzones) so that zone properties pass to the locations and less master data is needed; they have no address but can have coordinates, either calculated as the center point of the included locations or entered manually; types are region, postal code, direct and mixed (S4TM2 Transportation Zone; S48600 Transportation Zones)
- Transportation zone hierarchy: properties of higher-level zones pass to lower levels; a zone cannot be assigned to itself or to a zone it already contains; a zone can be in any number of higher-level zones and a location in any number of zones; the VSR optimizer, lane determination and transshipment location determination consider the hierarchy (S4TM2 Transportation Zone Hierarchy; S48600)
- Transportation lanes: express direct reachability between two locations, two zones or a mix for a specific means of transport; a lane points in one direction only, so the reverse needs another lane; at least one means of transport must be assigned, carriers can be assigned per means of transport (with cost, priority, share of business or capacity), and carriers are needed for automatic carrier selection; created in the Define Transportation Lane app (S48600 Transportation Lanes; H03; S4TM2)
- Trade lanes: abstract, context-independent classification of transport with an orientation (Inbound, Outbound, From, To, Within, Along), source and destination, optionally a mode and means of transport; they form hierarchies and can overlap; they do not replace transportation lanes and have no direct link to them (S4TM2 Trade Lane; S48600 Trade Lane)
- Transportation mode and means of transport: the mode is the highest-level grouping (categories road, rail, sea, air, postal service, inland waterways); the main carriage mode holds the shipment documents in multistage shipments; a means of transport describes a vehicle type and carries mode, multi-resource, scheduled, own means of transport and GIS quality settings; UN/EDIFACT standard codes include 006 Aircraft, 011 Ship, 031 Truck, 038 Car; without a GIS, average speed and distance factor estimate transit time (S4TM2 Transportation Mode through Distance and Speed)
- Multi-resource: a means of transport can be flagged so that the system assumes a defined number of resources (unlimited if none given) instead of individual resources; the number is the maximum of parallel freight orders per resource and it can model an external fleet in one step (S4TM2 Multi-Resource)
- Path finder: searches legs in the network over locations, transshipment locations, transportation lanes, schedules and zones to show whether a connection exists and master data is correct; it runs in the transportation network cockpit (Find Path To Location) or on the transportation proposals UI, and as report /SCMTMS/FIND_TN_PATH; it does not consider incompatibilities (S4TM2 How to Use the Path Finder; S48600 Path Finder)
- Resource types: vehicle, handling, calendar and transportation unit resource (H03 also lists driver); a vehicle resource is a unit load with up to eight capacity dimensions that planning only uses if they match a freight unit building rule, and can be active or passive; Factory Calendar, Continuous Dimension, Capacity and Unit of Measure are mandatory (S4TM2 Resources Overview; H03 Classification of Resources)
- Other resource objects: compartments divide a vehicle resource and support incompatibilities (for example dangerous goods areas); means-of-transport combinations model truck and trailer; handling resources (door, loading ramp, forklift) give loading and unloading capacity; calendar resources set location operating hours; transportation unit resources represent containers; resource classes are determined from the means of transport or equipment group (S4TM2 Compartments to Transportation Unit Resource; H03)
- Incompatibilities for resources in the exercise: incompatibilities define objects that must not be combined, for example ice cream and vehicles without a cooling unit; INC_S4TM1_VEH_FU links freight units to vehicle resources/types, and violations can be allowed or forbidden separately for manual planning and VSR optimization (E01 Review Incompatibility)

### Skill items (tier: inferred)
- Choose the appropriate location type and creation route (on the fly, report or BAdI) for a plant, a shipping point and a business partner address
- Design a small network using a transportation zone, two transportation lanes (both directions) and a transshipment location, and decide the means of transport for each lane
- Run the path finder between two locations and interpret a missing connection
- Distinguish a transportation lane from a trade lane for a given business statement
- Pick the resource type (vehicle, handling, calendar, transportation unit) that models a given real-world asset

### Important questions
- Why are location types only a reference, and what does drive how a location is used in planning?
- When is region-level geocoding enough, and when must coordinates be of higher quality?
- How do transportation zones and zone hierarchies reduce master data, and what must be true for a hierarchy to be valid?
- Why does a transportation lane need a means of transport, and what changes when a carrier is assigned to it?
- If a trade lane has no link to a transportation lane, what is a trade lane used for in the network?
- If the path finder shows a connection, which checks has it still not done?
- What are the differences between a handling resource, a calendar resource and a vehicle resource at a location?

### Deliverable (tier: inferred)
A network design sheet for a small example flow (plant, port, customer zone): the locations with types and geocoding approach, the zone with its type, the transportation lanes in both directions with means of transport and carrier, one trade lane, and the vehicle, handling and calendar resources needed, with a note on how the path finder would confirm the connection.

### Self-confidence question (tier: inferred)
Can I explain how locations, zones, lanes, trade lanes, modes and resources fit together in the transportation network to a project stakeholder without notes?

### Quiz questions
```yaml
- q: What role does the location type play in SAP TM?
  o: ["It controls which business processes can run at the location", "It is only a reference and controls no business process", "It decides which carrier may serve a particular location", "It sets the transportation zone of the location"]
  a: 1
  e: "S48600, Locations, states that in TM the location type is used to categorize locations and that location types are not used to control business processes but serve as a reference."
- q: Which report can be used to create locations for plants, shipping points and business partners?
  o: ["/SCMTMS/FIND_TN_PATH", "/SCMTMS/ORG_INT", "/SAPAPO/CREATE_LOCATION", "/SAPAPO/LOC_CREATE_ALL"]
  a: 2
  e: "S48600, Creating Locations Using a Report, names /SAPAPO/CREATE_LOCATION for this purpose. /SAPAPO/LOC_CREATE is a BAdI used to create locations when a business partner is saved, and /SCMTMS/FIND_TN_PATH is the path finder report."
- q: A transportation lane exists from location A to location B. How is the reverse direction modeled?
  o: ["By creating another transportation lane", "By selecting a bidirectional indicator", "By creating a trade lane with orientation To", "By reversing the means of transport"]
  a: 0
  e: "S4TM2 (Transportation and Trade Lane) and S48600 (Transportation Lanes) state that a transportation lane points only in one direction and that you must create another lane to model the reverse direction."
- q: What is required to create a transportation lane?
  o: ["At least one carrier assigned", "A schedule with fixed departure times", "At least one means of transport assigned", "A default route with several stops defined"]
  a: 2
  e: "S48600, Transportation Lanes (Note), states that creating a transportation lane requires the assignment of at least one means of transport; carriers are needed in addition only to enable automatic carrier selection."
- q: How are trade lanes related to transportation lanes?
  o: ["Each trade lane generates a transportation lane automatically", "There is no direct link between them", "A trade lane replaces the transportation lane in planning", "Both are maintained on the same screen"]
  a: 1
  e: "S4TM2, Trade Lane, and S48600, Trade Lane (Note), state that trade lanes do not replace transportation lanes and that there is no direct link between a trade lane and a transportation lane."
- q: Which transportation zone type assigns locations through a range of codes for a country or region?
  o: ["Direct assignment zone", "Country or region zone", "Mixed combination zone", "Postal code zone"]
  a: 3
  e: "S48600, Transportation Zones, says that in a postal code zone locations are assigned by specifying a valid postal code range for a country or region. S4TM2 adds that carriers often publish rates for ranges of three-digit zip codes such as 170-173."
- q: Which rule applies when defining a transportation zone hierarchy?
  o: ["A zone cannot be assigned to itself", "A zone can be in only one higher-level zone", "A zone can be assigned to a location", "A location can belong to only one zone"]
  a: 0
  e: "S48600 states that a transportation zone cannot be assigned to itself or to a zone that already contains it. S4TM2, Transportation Zone Hierarchy, adds that a zone can be assigned to any number of higher-level zones, locations to any number of zones, and a zone cannot be assigned to a location."
- q: Which of the following does the path finder not take into consideration?
  o: ["Transshipment locations", "Schedules", "Incompatibilities", "Transportation zones"]
  a: 2
  e: "S4TM2, How to Use the Path Finder, states that the path finder does not take incompatibilities into consideration. It does consider locations, transshipment locations, transportation lanes, schedules and transportation zones."
- q: What must hold for planning to take the capacity of a vehicle resource into account?
  o: ["The vehicle must be flagged as an active resource", "Dimensions and units match a freight unit building rule", "The vehicle must be assigned to a calendar resource and shift", "A compartment must be defined for the vehicle"]
  a: 1
  e: "S4TM2, Resources Overview, and H03 (Vehicle Resource) state that planning can only take the vehicle capacity into account if the dimensions and units of measurement correspond to those defined in a freight unit building rule."
- q: What is the purpose of a calendar resource?
  o: ["It provides the capacity to load and unload vehicles", "It models the capacity of a single container", "It represents a trailer that cannot travel alone", "It sets the operating hours of locations"]
  a: 3
  e: "S4TM2, Calendar Resource, states that calendar resources determine the operating hours of locations and that loading and unloading can only take place during operating hours. Handling resources provide the loading and unloading capacity."
```

---

## Session 04 — Forwarding Orders and Quotations

### Knowledge items
- Purpose of Forwarding Order Management: create, edit and confirm forwarding orders from ordering parties, already specify the route and have transportation charges calculated; the orders form the basis for transportation planning. Data can also be entered as a forwarding quotation and sent to the ordering party (H04, Use)
- Integration of the component: freight orders and freight bookings can be created from forwarding orders (Freight Order Management); forwarding orders are the basis for planning and execution; a forwarding settlement can be created from the order to trigger invoicing; master data is a prerequisite; integration with dangerous goods management and global trade (H04, Integration)
- Definition of a forwarding order: an order from an ordering party to a carrier or logistics service provider for the transportation of goods from a shipper to a consignee under agreed conditions; entered manually (for example after a telephone call) or transferred automatically via PI interfaces or EDI; holds pick-up and delivery address, dates/times and the goods (H04, Forwarding Order)
- Forwarding orders and quotations as transportation requirements in the logistics service provider (LSP/3PL) deployment: they are created manually in the SAP TM UI or by EDI with an external system, and count as the transportation requirements of an LSP process (S48600, Transportation Requirements Overview)
- Design of the forwarding order screen: determined by the transportation mode (air, sea or land) and by the forwarding order type defined in Customizing; the initial screen takes the type and the mode, and the type decides which additional tab pages are shown for each business process (H04, Structure)
- Basic structure of the forwarding order: general data, business partner, location and dates/times areas (valid for all items, including sales organization, Incoterms, service level, totals of quantity and weight); ordered route and actual route; list of order items; document flow; output management; status; HBL or HAWB; profitability; and process-dependent tab pages such as charge calculation, air cargo security, instructions and change documents (H04, Structure)
- Fast order entry: besides the full view, the Page function opens a single-screen view without tab pages with all fields needed to complete an order (H04, Structure)
- Ways to create a forwarding order: on the basis of a quotation, on the basis of a template, as a copy of an existing order, from the order management overview, from a forwarding agreement (ID and version, service items and data such as transportation mode, shipping type and sales organization are transferred), or via PI interfaces (H04, Creation of a Forwarding Order)
- Template and copy behaviour: a template copies the order data such as document type, except dates/times and planning and execution data; a copy keeps much of the data including route data but has no dates/times and no follow-on documents, and its life cycle status is New (H04, Creation of a Forwarding Order)
- Steps of manual creation: initial screen (forwarding order type, transportation mode, references, default route), general data (sales organization, process control attributes, Incoterms or freight terms), business partners, locations and dates/times, business process-dependent data, route, order items, then save (H04, Process)
- Rules on type and mode: without an entry the default type from Customizing is used; the forwarding order type cannot be changed afterwards in the document; a mode defined in the type cannot be changed; a manually entered mode can be changed later only if no follow-on documents exist for FUs or TUs whose main carriage stage has started (H04, Process)
- Order item hierarchy: items are entered as a hierarchy such as container, packaging and product; only the top level is relevant to planning, and quantities and weights are totaled and copied to the header (H04, Process, step 6)
- Saving the order: the system assigns an ID from the number range of the document type, checks completeness and consistency, and if customized automatically creates freight units, confirms the order, calculates charges, triggers an approval workflow, checks credit limits and runs the trade compliance check (H04, Process, step 7)
- Customizing behind the order: the forwarding order type assigns the profiles (planning, output, dangerous goods, partner determination) and the freight unit building rule or condition, and sets defaults such as transportation mode, shipping type, traffic direction, sales organization, automatic confirmation, automatic FU building, approval workflow, credit limit check, charge calculation, settlement and change tracking (H04, Settings for the Forwarding Order)
- Ordered route: the stages of the route requested by the ordering party; source and destination on the Locations and Dates/Times tab appear as one Complete Carriage line, which can be split into stages; a default route from the initial screen or a forwarding agreement item fills it (H04, Ordered Route)
- Actual route: entered manually, determined by Route - Transportation Proposal, or taken from a default route; the transportation mode of the header refers only to the main carriage, and stage mode is taken from manual entry, then stage type Customizing, then header; after transportation planning the actual route is displayed and can no longer be changed (H04, Actual Route)
- Ordered route is not updated by the actual route; Copy from Actual Route overwrites it, after which the ordered route is no longer visible. Stage detail data distinguishes requested, planned, actual and confirmed dates (H04, Copying the Actual Route to the Ordered Route; Detail Data)
- Document flow: shows which business documents were entered into the order and which were created from it, with navigation to follow-on documents such as a freight unit (H04, Structure)
- Life cycle status values of a forwarding order: New, In Planning, Planned, In Execution, Executed, Partially Invoiced, Completed, Determination Pending, Canceled, Draft (H04, Status of a Forwarding Order)
- Further status types: planning status, execution status, confirmation status, approval status (only with approval workflow), delivery status, FWQ assignment status, organization interaction status, HBL or HAWB status, and statuses for air cargo security and foreign trade compliance (H04, Status of a Forwarding Order)
- HBL or HAWB: the assignment block shows house bill of lading or house air waybill data and allows waybill numbers to be allocated to freight units; its status (Finalized, Partially Finalized, Not Finalized) shows whether the customer service agent has completed the HBLs or HAWBs (H04, HBL or HAWB; HBL or HAWB Status)
- Blocking: planning, execution, confirmation and settlement blocks can be set manually with block reasons from Customizing or automatically (incomplete order, approval workflow, dangerous goods check); removal needs authorization and a comment can be logged; a forwarding settlement document cannot be created while the settlement block is set (H04, Blocking the Forwarding Order)
- Editing the order: freight units can be created automatically or from the Follow-Up Actions menu, planning is manual in the transportation cockpit or via route determination, automatic planning with the VSR optimizer, or direct creation of freight documents; changes are passed on to freight units and follow-on documents until execution data has moved the FU to On Hand; an order with an assigned freight document cannot be canceled (H04, Editing of a Forwarding Order)
- Forwarding quotation: a quotation from a carrier or LSP to an ordering party with price and conditions; structured like the order plus a validity scope and a quotation price; its life cycle status values are New, Not Transferred, Transferred and Canceled; it is set up with a forwarding quotation type and can be converted into a forwarding order (H04, Forwarding Quotation; Creation and Editing of a Forwarding Quotation)
- Forwarding settlement document: created from the forwarding order (Costs/Settlement menu) when activated for the forwarding order type, based on the charge calculation; if one exists, changes either flow through the forwarding settlement change process (Reverse and Repost or Delta Only in the settlement profile) or require canceling the document (H04, Forwarding Settlement Document; Editing of a Forwarding Order)

### Skill items (tier: inferred)
- Read a forwarding order's Status tab and say which stage of planning, execution and invoicing the order has reached
- Explain from a forwarding order which data belongs to the ordered route and which to the actual route
- Choose between creating an order from a quotation, a template, a copy or a forwarding agreement for a given situation
- Trace a forwarding order through its document flow to freight units, freight orders and a forwarding settlement document

### Important questions
- Why does the forwarding order type matter so much, and what can no longer be changed once it is chosen?
- What is the difference between the ordered route and the actual route, and when does the actual route stop being editable?
- How do the life cycle status and the planning, execution and confirmation statuses relate to each other?
- Which blocks can stop an order, who sets them, and what do they prevent downstream?
- How does a forwarding quotation relate to a forwarding order, and what happens to the data when the order is created from it?
- Why are forwarding orders treated as transportation requirements for a logistics service provider while sales and purchase orders play that role elsewhere?

### Deliverable (tier: inferred)
A one-page walkthrough of a forwarding order from quotation to forwarding settlement document: the creation options, the screen areas, the ordered and actual route, the main status values and the blocks that can stop it, written so a colleague can follow the document flow.

### Self-confidence question (tier: inferred)
Can I explain how a forwarding order is created, which statuses it passes through and how it connects to the quotation, the freight units and the forwarding settlement document to a project stakeholder without notes?

### Quiz questions
```yaml
- q: What determines the design of the user interface of a forwarding order?
  o: ["The ordering party and the sales organization entered in the order", "The carrier assigned to the main carriage and the freight agreement", "The transportation mode and the forwarding order type", "The number of order items and the total weight of the goods entered"]
  a: 2
  e: "The user interface is determined by the transportation mode (air, sea or land) and by the forwarding order type defined in Customizing (H04, Structure)."
- q: A forwarding order has just been saved and no freight units or transportation units exist for it yet. Which life cycle status does it have?
  o: ["New", "In Planning", "Planned", "In Execution"]
  a: 0
  e: "New means a forwarding order was created and no freight units or transportation units exist yet; In Planning needs at least one FU or TU (H04, Status of a Forwarding Order)."
- q: After transportation planning has been performed from a forwarding order, what is true of the actual route?
  o: ["It is deleted and must be entered again manually", "It is copied automatically into the ordered route", "It stays editable until the first freight order is saved", "It is displayed and can no longer be changed"]
  a: 3
  e: "If planning was performed based on the forwarding order, the actual route is displayed and can no longer be changed (H04, Actual Route Resulting from Transportation Planning)."
- q: How does the ordered route get the data of the actual route, for example to print up-to-date documents?
  o: ["Automatically whenever the order is saved again, without any user action", "By choosing Copy from Actual Route on the Ordered Route tab", "Automatically once all freight units of the order have been planned", "By splitting the Complete Carriage line into several stages at once"]
  a: 1
  e: "The ordered route is not updated automatically; Copy from Actual Route copies the data, but the ordered route is then no longer visible (H04, Copying the Actual Route to the Ordered Route)."
- q: Which statement about the forwarding order type is correct when creating an order?
  o: ["The type cannot be changed afterwards in the document itself", "The type can be changed freely as long as no items exist", "The type can be changed once the order has been confirmed", "The type is always taken from the ordering party's master data"]
  a: 0
  e: "You cannot change the forwarding order type subsequently in the document, although some other parameters such as the sales organization may still be changed (H04, Creation of a Forwarding Order, Process step 1)."
- q: In the item hierarchy of a forwarding order, which level is relevant to planning?
  o: ["The lowest level, for example the product", "The middle level, for example the packaging", "Every level, because each is planned separately", "Only the top level of the hierarchy"]
  a: 3
  e: "Items are entered as a hierarchy, but only the top level is relevant to planning; quantities and weights are totaled and copied to the header (H04, Creation of a Forwarding Order, step 6)."
- q: What effect does a set settlement block have on a forwarding order?
  o: ["The order can no longer be confirmed to the ordering party", "No forwarding settlement document can be created", "The freight units of the order are deleted", "The order is canceled with a reason code"]
  a: 1
  e: "You cannot create a forwarding settlement document if the settlement block is set (H04, Blocking Information of a Forwarding Order)."
- q: Which life cycle status describes a forwarding quotation that was already sent to the ordering party and then changed, with the changes not yet sent?
  o: ["Transferred", "Partially Transferred", "Not Transferred", "Awaiting Confirmation"]
  a: 2
  e: "Not Transferred means a quotation that was already sent was changed and the changes were not yet sent; Transferred means it was sent (H04, Status of the Forwarding Quotation)."
- q: What is left out when a template is created from an existing forwarding order?
  o: ["Dates/times and planning and execution data", "The document type and the general order data", "The sales organization and the Incoterms of the order", "The business partners and the locations of the order"]
  a: 0
  e: "The system copies the data of the order, such as document type and order data, into the template with the exception of dates/times and planning and execution data (H04, Creation of a Forwarding Order)."
- q: In a logistics service provider deployment, which documents count as the transportation requirements?
  o: ["Sales orders and outbound deliveries from the shipper", "Purchase orders and inbound deliveries from suppliers", "Forwarding orders and forwarding quotations", "Freight orders and freight bookings"]
  a: 2
  e: "Forwarding orders are typically created manually in the SAP TM UI or by EDI, and forwarding orders and quotations are considered transportation requirements within an LSP process (S48600, Transportation Requirements Overview)."
```

---

## Session 05 — Logistics Integration with Sales, Purchasing and Deliveries

### Knowledge items
- Scope of logistics integration: TM can be integrated with components in the same system or an external system; orders from SD and MM, deliveries from LE and JIT calls from nJIT drive transportation planning and execution, and the TM component creates or updates freight units directly for documents defined in Customizing as TM-relevant when they are saved (H05, Logistics Integration; Internal TM Component Integration, Use)
- What integration enables: collective planning for all orders and scheduling agreements, planning on sales or purchase orders before delivery creation for an earlier forecast of transportation demand, tendering, subcontracting and execution based on orders, sales order scheduling, and planning and execution of JIT calls (H05, Internal TM Component Integration, Use)
- Integratable documents: orders (sales order, customer returns, purchase order, stock transport order, returns purchase order, returns stock transport order), scheduling agreements (sales, purchase, stock transport), JIT calls (sequenced, forwarded) and inbound and outbound deliveries from LE, also when an order was not sent to TM (H05, Features)
- Transportation requirements as sources: OTR is the demand from sales, purchasing and stock transport (SO, PO, STO); DTR is the demand from an inbound or outbound delivery (IDL/ODL); the freight unit represents the demand that is planned (S48600, Common Terms Used in SAP Transportation Management)
- Triggering documents and deployment models: sales orders, customer returns, purchase orders, stock transport orders and their returns, scheduling agreements and deliveries trigger transportation requirements; in side-by-side deployment the information is replicated and becomes order-based or delivery-based requirements via XML messages (SAP PI or point-to-point); in embedded deployment no separate document is needed and the freight unit is created directly from the original object (S48600, Transportation Requirements Overview)
- Decentralized scenarios: a decentralized EWM and TM system can be integrated with an external ERP system and transportation planning done on outbound delivery orders; settings sit under Decentralized EWM-TM Integration (H05, Logistics Integration; Logistics Integration Profile for Decentralized EWM)
- Transportation relevance and control keys: control keys define which documents in a chain are integrated; sales document integration is activated by assigning a control key to sales document type, sales area and shipping condition; purchasing documents by document type, purchasing organization and purchasing group; delivery documents by shipping point, delivery type and shipping condition; the key is stored in parameter TM_CONTROL_KEY and passed to all relevant documents in the chain (H05, Configuring Integration of Orders and Deliveries)
- Deliveries inherit the control key of the preceding document and ignore the delivery Customizing in that case; the delivery setting is needed only when a delivery is integrated but its order is not (H05, Activate Integration of Delivery Documents)
- Three settings named by S48600 for integrating sales orders, scheduling agreements and deliveries: activate integration via control key, create a logistics integration profile, assign the profile to the document type; prerequisite for configuration is the location creation report /SAPAPO/CREATE_LOCATION (S48600, Integrating Transportation Relevant Documents with SAP TM; H05, Configuring Integration of Orders and Deliveries)
- Logistics integration profile for SD, MM and LE: common settings (freight unit building rule, condition for FUB rule determination, automatic freight unit building, stage building variant) and order-related settings (plan on requested or confirmed quantities, FU building for partly complete sales documents, rule group for the time range of purchase scheduling agreements, integration based on actual quantity, improved location determination, Advanced SR compliance check) (H05, Logistics Integration Profile for SD, MM, and LE)
- FUB rule determination: the system first checks the condition in the logistics integration profile, then the freight unit building rule in the profile, then standard settings; freight unit building can run automatically on save or be triggered manually or by background report (/SCMTMS/SUBSEQENT_FUB_LOGINT in embedded deployment) (S48600, Freight Unit Building Rules; H05, Reports for Logistics Integration)
- Order integration process: order created in SD/MM with items and schedule lines, TM creates freight units only for transportation-relevant orders, planning can consolidate FUs from orders of different types (for example purchase and sales orders), then TM can execute transportation or trigger delivery creation in LE (H05, Integration of Orders)
- End-to-end process from order to execution: create order (SD/MM), perform transportation planning (TM), create delivery proposal (TM), create deliveries (LE), reassign freight units from order to delivery (TM), execute transportation; the TM document flow can be displayed in SD, MM or LE (H05, Integration of Orders and Deliveries in Transportation Planning)
- Delivery proposals: TM proposes inbound or outbound deliveries from planning results and LE creates them; creation runs by background report /SCMTMS/DLV_BATCH, interactively from the Delivery Proposal Builder app or Freight Orders - Worklist app, from the transportation cockpit or from the freight order UI; dates come from the freight order or booking, otherwise from FUs, quantities from the FUs (H05, Creation of Deliveries from TM; Creation of Delivery Proposals)
- Delivery proposal consolidation and control: FUs can share a proposal only with the same source and destination location, Incoterms, shipping conditions, document type and (if planned) start and destination stop; TM respects chronological consumption of schedule lines in LE; the delivery profile (Create Delivery Profile app) controls fixing of planning results, grouping by freight unit, order or order item, and exclusion of planning or execution blocked objects (H05, Creation of Delivery Proposals; Delivery Profile)
- Delivery integration without order integration: if the order is not TM-relevant, TM creates new FUs for the delivery according to the specified FUB rule; changes to orders and deliveries update the FUs, a deleted order deletes its FUs, a deleted delivery reassigns FUs to the order if it is TM-relevant, otherwise deletes them (H05, Integration of Deliveries; Integration of Changed and Deleted Orders and Deliveries)
- Stock transport orders: a two-step process with outbound and inbound deliveries and reassignment of FUs from outbound to inbound delivery; in the Advanced Shipping and Receiving scenario goods issue triggers the inbound delivery and the reassignment, and FUs in one delivery must belong to the same EWM- or LE-managed warehouse or storage location (H05, Integration of Stock Transport Orders)
- Scheduling agreement integration: schedule lines of purchase scheduling agreements create, change or delete freight units; TM planning results can be synchronized back to MM schedule lines in batch only for FUs not yet assigned to a delivery and within the planning time fence; inbound deliveries from an ASN lead TM to reassign FUs from the agreement to the delivery (H05, Integration of Purchase Scheduling Agreements)
- Integration time range for purchase scheduling agreements: start and end dates limit the schedule lines taken into account and so the freight units created; the start date is set once from the earliest schedule line with open quantity and a safety margin and is never in the future; the end date follows the schedule line count, matching rule and offsets and is determined daily; report /SCMTMS/UPDATE_INT_TIMERANGE preponed end dates (H05, Integration Time Range for Purchase Scheduling Agreement)
- Order-only integration of purchase scheduling agreements: activation report /SCMTMS/ACTIVATE_MMSAG_WO_DLV sets a start date and a reduction quantity strategy, adjustable later with /SCMTMS/ADAPT_START_MM_WO_DLV (H05, Integration of Purchase Scheduling Agreements without Inbound Delivery)
- JIT call integration: FUs are created from sequenced JIT calls based on the component group material, with JIT call reference number, receiving point and unloading point; the outbound (S2C) process is delivery-based only (H05, Integration of Next Generation Just-In-Time)
- Source and destination location determination: business partners, plants, shipping points or storage locations from ERP documents are identified and locations updated or created; a new address in a document creates a one-time location; Improved Location Determination uses shipping points as destination (H05, Source and Destination Location Determination)
- Advanced intercompany sales and stock transfer: one freight unit across the business documents, harmonized Incoterm handling, Incoterm locations build FU stages, and TM sets the planned and actual transfer of control dates and times in the LE delivery (H05, Transportation Management in Advanced Intercompany Business Processes)
- Incoterms and responsibilities: planning and cost responsibility transfer at Incoterm location 1; risk transfers there for non-C-clauses and at Incoterm location 2 for C-clauses (CIF, CIP, CFR, CPT); transfer of control is the transfer of risk responsibility, internal within the group and external to the customer (H05, Incoterms and Incoterm Locations; Transfer of Control)
- Stage building from Incoterm locations: stages are built only if the Incoterm has the Incoterm Location flag, otherwise one stage from source to destination; the logistics integration profile offers the Static variant (stage profile) or the Advanced variant (Incoterm locations 1 and 2), and the Incoterm Location Stage Building field gives rules 01 to 05 (S48600, Stage Building Based on Incoterms; H05, Logistics Integration Profile)
- Reports for logistics integration: /SCMTMS/LI_ACTIVATE, /SCMTMS/DLV_BATCH, /SCMTMS/SUBSEQENT_FUB_LOGINT, /SCMTMS/TM_SAG_PLANNING_SYNC and the purchase scheduling agreement activation, deactivation, reactivation and time range reports (H05, Reports for Logistics Integration)
- Exercise flow (E02): create a purchase order with Create Purchase Order - Advanced and the confirmation control value Inbound delivery, open the Order Integration Worklist app, review the freight unit built by FUBR_S4TM1 and its document flow; E04 shows Create Deliveries - Delivery Builder turning four freight units into three delivery proposals (E02; E04, Create Deliveries)

### Skill items (tier: inferred)
- Decide from a document type, sales area or purchasing organization whether an order or delivery is integrated into TM, and name the control key and profile settings involved
- Describe which TM objects are created and reassigned at each step from order to delivery
- Choose among the delivery proposal start points (report, Delivery Proposal Builder, freight order worklist, cockpit) for a given planning situation
- Use the Incoterm locations of an order to say which stages TM builds and where responsibilities transfer

### Important questions
- Which documents are integrated, and what decides whether a given order or delivery is transportation-relevant?
- What does the logistics integration profile control, and where is it assigned?
- When are freight units built from the order and when from the delivery, and what happens to them when the delivery is created?
- Why does TM propose deliveries instead of letting LE create them freely, and which data must match for FUs to share a proposal?
- Why does a purchase scheduling agreement need an integration time range?
- How do Incoterm locations 1 and 2 change the stages and the transfer of control in an advanced intercompany process?

### Deliverable (tier: inferred)
A one-page integration map for one scenario (for example a sales order or a purchase order): the document chain, the control key and logistics integration profile settings that make it TM-relevant, the freight units TM builds, the delivery proposal step and the point where FUs are reassigned to the delivery.

### Self-confidence question (tier: inferred)
Can I explain how orders, scheduling agreements and deliveries from sales and purchasing become freight units in TM, and how deliveries come back from TM, to a project stakeholder without notes?

### Quiz questions
```yaml
- q: Which of the following can be integrated into TM as an order from SD or MM?
  o: ["Freight booking for a vessel", "Returns stock transport order", "Freight agreement with a carrier", "Capacity document for a trip"]
  a: 1
  e: "The order types listed for integration are sales order, customer returns, purchase order, stock transport order, returns purchase order and returns stock transport order (H05, Order Integration)."
- q: Which parameter does the system assign to a sales document with activated TM integration and to all relevant documents in its chain, such as the outbound delivery?
  o: ["TM_PROFILE_ID", "TM_RELEVANCE_FLAG", "TM_FUB_RULE", "TM_CONTROL_KEY"]
  a: 3
  e: "When a document with activated integration is created, the system assigns the control key to it (parameter TM_CONTROL_KEY) and to all relevant documents in the document chain (H05, Activate Integration of Sales Documents)."
- q: In an embedded TM deployment, which object acts as the initial object for SAP TM?
  o: ["The freight unit, created directly from the original object", "The forwarding order, entered by hand in the TM user interface", "The order-based requirement, replicated from the ERP system", "The freight order, created from the delivery proposal"]
  a: 0
  e: "In embedded deployment the original object already exists in SAP S/4HANA and the freight unit acts as the initial object for SAP TM, created directly from it; replication into requirements belongs to side-by-side deployment (S48600, Transportation Requirements Overview)."
- q: In which order does the system determine the freight unit building rule for a transportation demand?
  o: ["Rule in the profile, then condition in the profile, then standard settings", "Standard settings first, then condition in the profile, then rule in the profile", "Condition in the profile, then rule in the profile, then standard settings", "Condition in the profile, then standard settings, then rule in the profile"]
  a: 2
  e: "The system first reviews the condition in the logistics integration profile, then the freight unit building rule in the profile, and finally applies standard settings (S48600, Freight Unit Building Rules)."
- q: What does the Advanced stage building variant in the logistics integration profile consider when it builds stages for freight units?
  o: ["Only the stage profile and its condition", "Incoterm locations 1 and 2", "The planning profile of the freight order", "The shipping point and the delivery type"]
  a: 1
  e: "With the Advanced variant the system considers Incoterm locations 1 and 2; with the Static variant a stage profile and stage profile condition determine the stages (H05, Logistics Integration Profile for SD, MM, and LE)."
- q: Which of the following must be the same for freight units to be consolidated into one delivery proposal?
  o: ["The carrier of the freight order", "The net weight of the items", "The currency of the order", "The shipping conditions"]
  a: 3
  e: "Freight units can be consolidated into the same delivery proposal only if source location, destination location, Incoterms, shipping conditions and document type match, plus start and destination stop if planning is done (H05, Creation of Delivery Proposals)."
- q: Which report creates deliveries in ERP based on existing freight units?
  o: ["/SCMTMS/DLV_BATCH", "/SCMTMS/LI_ACTIVATE", "/SCMTMS/FIX_INT_TIMERANGE", "/SCMTMS/SUBSEQENT_FUB_LOGINT"]
  a: 0
  e: "/SCMTMS/DLV_BATCH is described as the report to create deliveries based on existing freight units; the others activate documents, fix time range end dates or trigger subsequent freight unit building (H05, Reports for Logistics Integration)."
- q: The current date is 17 May, the safety margin is seven days (10 May) and the earliest schedule line with open quantity is 8 May. Which integration start date does the system choose?
  o: ["17 May", "10 May", "8 May", "7 May"]
  a: 2
  e: "The earliest schedule line with open quantity precedes the safety margin, so the system chooses 8 May as the start date (H05, Integration Time Range for Purchase Scheduling Agreement, Example)."
- q: In the advanced intercompany sales example, the Incoterm on the intercompany sales order is CIF. Where does the internal transfer of control occur?
  o: ["At Incoterm location 1, the port of discharge in Hamburg, Germany", "At Incoterm location 2, when loaded on the vessel", "At the customer's address in Walldorf, on delivery", "At the plant of the delivering company in Palo Alto, California"]
  a: 1
  e: "With CIF the internal transfer of control occurs at Incoterm location 2, when the goods are loaded on the vessel, and risk passes from the delivering to the selling company (H05, Example of an Advanced Intercompany Sales Process; Incoterms and Incoterm Locations)."
- q: In exercise E02, what does the system generate when a freight unit is created based on a preceding document such as a purchase order?
  o: ["A delivery proposal listing the open quantities of the order", "A freight order with the next available vehicle assigned", "A transportation unit for the receiving warehouse or location", "A document flow with the related documents and statuses"]
  a: 3
  e: "When a subsequent document like a freight unit is created from a preceding document such as a purchase order, the system generates a document flow showing the sequence of related documents and their statuses (E02, Create Purchase Order and Review the Freight Unit)."
```

---

## Session 06 — Planning: Freight Units, Cockpit and Carrier Selection

### Knowledge items
- The Planning component creates freight documents and transportation units from business documents (for example forwarding orders from which freight units have been built) by assigning capacities, while taking constraints such as requested delivery dates into account; it is integrated with Forwarding Order Management (source of the freight units), Freight Order Management (result of planning), Charge Calculation and Master Data (H07, Planning)
- A freight unit is a set of goods transported together across the whole transportation chain and the smallest unit that can be transported; it merges items of forwarding orders, order-based and delivery-based transportation requirements, and carries transportation constraints for planning (H07, Freight Unit)
- The system creates freight units automatically from forwarding orders, order-based and delivery-based transportation requirements (sales orders, purchase orders, deliveries, EWM outbound delivery orders) and JIT calls, and can split and merge quantities according to the freight unit building rule used (H07, Creation and Editing of Freight Units)
- Freight unit size affects planning: larger freight units make VSR optimization simpler, smaller ones raise the theoretical optimization potential but make planning harder, so the advice is to aim somewhere in the middle (for example not one 20-ton unit and not 20,000 units of 1 kg for a 20-ton truck) (H07, Creation and Editing of Freight Units; VSR Optimization)
- Prerequisites for automatic freight unit building: the automatic freight unit building checkbox in the forwarding order type or in the logistics integration profile, freight unit types defined in Customizing, and freight unit building rules (FUB rules) with assigned freight unit types; incompatibilities are optional (H07, Creation and Editing of Freight Units)
- Automatic creation first groups business document items by hard constraints (source and destination location, carrier, pick-up and delivery dates), business document attributes such as delivery group, packaging information and incompatibilities, then creates one or more freight units from the groups; items with different compatibility groups (package/product/schedule line, container, railcar, trailer) are never put into the same freight unit or transportation unit (H07, Automatic Creation of Freight Units; Hard Constraints)
- The standard process controller strategy for freight unit building is FUB_AUTO, and a forwarding order triggers freight unit creation when it is saved (H07, Automatic Creation of Freight Units; S4611, Freight Unit Building Rules)
- The FUB rule defines how freight units are consolidated through the FUB strategy: Consolidate as much as possible (items from different business documents are grouped), Consolidate per item (one freight unit per business document item) and Consolidate per request (compatible parts) (all items of a business document form a freight unit); hard constraints and incompatibilities apply to all three (H07, Freight Unit Building Rule)
- In the FUB rule the planning quantities (for example gross weight and gross volume) with their units of measure are copied to the freight unit and are the basis for resource capacity checks; the split quantity defines the maximum capacity of a freight unit, a rounding value makes the quantity a multiple of it, and the item split checkbox controls whether items may be split when the split quantity is exceeded; the critical quantity is the primary unit of measure that allows splitting (H07, Planning and Split Quantities; S4611, Freight Unit Building Rules)
- The freight unit update strategy of the FUB rule decides whether items may move between freight units on update (Item Swap Allowed is the standard behavior, Item Swap Not Allowed keeps items in their freight unit) (H07, Freight Unit Update Strategy)
- The document type in the FUB rule controls whether the freight unit builder creates a freight unit, transportation unit or freight order; without a document type the system creates freight units or package, container, railcar and trailer units according to the item category, and equipment type and group in the rule produce equipment-based units (H07, Document Type; Default Business Document Categories; Equipment-Based Freight Units)
- Automatic creation of freight orders (shortcut scenario): entering a freight order type, directly or through a condition, as the document type makes the system create freight orders instead of freight units, for example for small orders sent by express delivery or orders that always travel as a full load; in the shortcut the freight unit is skipped and carrier selection can start directly (H07, Automatic Creation of Freight Orders; E03, Compare the Standard and Shortcut Process)
- The FUB rule for a business document is determined in order: a condition of type /SCMTMS/FUBR in the business document type (one per type), then a standard FUB rule in the business document type, then default settings; for deliveries S4611 describes the same cascade starting from the logistics integration profile; FUB rules are created in the Create Freight Unit Building Rule app (H07, Determination of Freight Unit Building Rules; S4611, Freight Unit Building Rules)
- The freight unit type (four-character identifier, unique across freight order, freight booking, transportation unit and freight unit types) carries the freight unit settings: change controller settings, creation, save and deletion strategies, planning settings (distance/duration determination, rule or condition for pick-up and delivery windows), default units of measure, organizational unit determination, track changes and output options; it also defines whether a freight unit is deleted or canceled (S4611, Creating Freight Units)
- Handling units and freight units: all product items packed in one handling unit stay in one freight unit, so parts of a handling unit are never assigned to different freight orders; one freight unit can hold several handling units (S4611, Creating Freight Units)
- Conditions make TM configuration flexible: they can determine FUB rules, freight unit types, organizational units, change controller strategies and pick-up/delivery time windows; their origin is Direct Business Object Access, a BRFplus decision table or a BRFplus expression, and a decision table is processed from top to bottom until the first matching row (S4611, Defining Conditions)
- Freight units can be split and merged manually (for example in the transportation cockpit or the freight unit table) with Split/Merge; source, destination, Incoterms and dates/times must match, partial quantities cannot be split off for package or container items, Adopt Stops copies stops and planning results, and Fix Source/Target Freight Unit protects the result from automatic rebuilding (H07, Manual Splitting and Merging of Freight Units)
- Unified package building during freight unit building can create freight units, freight orders or package units with a full package and product hierarchy, or only a rough estimate of the number of packages, and requires a unified package building profile (H07, Unified Package Building)
- The planning process turns freight units into freight orders by order consolidation (grouping orders with the same ship-from and ship-to locations), routing and scheduling, and carrier selection; planning can be done in three steps (transportation proposal, VSR to create a freight order, carrier selection), two steps, or one step (one-step optimization determines route, creates the freight order and selects the carrier); it can be manual or automatic, interactive or in the background, always based on planning strategies (S4TM2, Transportation Planning)
- Profiles and settings group planning-relevant parameters and are Customizing that can be transported: the selection profile (time-related, geographical and additional selection attributes; defines which freight units or freight orders and bookings are considered, up to a maximum number) and the planning profile (planning horizon, subprofile assignments such as capacity selection, manual planning, scheduling, optimizer, constraints and costs, incompatibility, carrier selection, load planning, unified package building and transportation cockpit settings); a standard planning profile is used when none is found; they are created in the Create Selection Profile and Create Planning Profile apps (H07, Profiles and Settings; S4TM2, Selection and Planning Profiles)
- The demand horizon (the period of demands considered, for pick-up and for delivery) is absolute (start and end date and time) or relative (start = current date + offset, end = start + duration, optionally with a factory calendar), while the planning horizon is the period in which transportation activities can be scheduled (H07, Demand Horizon; Planning Horizon)
- The transportation cockpit is the main user interface for planning: it starts with Profile and Layout Sets (a selection profile, a planning profile and a page layout, one set can be the default) or with the Selection Criteria screen (saved searches), shows requirement lists, capacity lists and order lists, and supports planning with lists and hierarchies, on a map and in a Gantt chart; PLS Management defines which users work with which sets (H07, Starting the Transportation Cockpit; S4TM2, Transportation Cockpit; E03, How to Select Data for Planning)
- Cockpit tasks: manual planning, creation of transportation proposals, VSR optimization, load planning, carrier selection, triggering of tendering, delivery proposals and freight bookings; page layouts define buttons, functions, levels and hierarchies and can be switched on the fly; views can be saved, shared and given conditional formatting (S4TM2, Transportation Cockpit; E03, Define Saved Searches and Views)
- Manual planning assigns requirement documents (freight units) to capacities (vehicle resources, schedules, equipment types) so that the system creates capacity documents such as freight orders; planning strategies VSRI_DEF (manual planning) and VSRI_SCH (manual planning with subsequent scheduling) are set in the planning profile, and the tools only support the planner, who remains responsible for consistent results (H07, Manual Planning; E03, Perform Interactive Planning)
- Planning constraints can be physical (vehicle capacity, handling capabilities) or process-related (for example a maximum of 25 drops per day), including pick-up and delivery time windows, loading and unloading durations, maximum distance, duration or stopovers; VSR optimization always adheres to hard constraints and models soft constraints with penalty costs, with window constraints none, hard (acceptable dates), soft (requested dates) or both (S4TM2, Planning Constraints; Hard and Soft Constraints)
- VSR optimization assigns freight units to capacities cost-effectively while adhering to constraints and determines delivery sequence and transportation dates; it minimizes a weighted sum of non-delivery, earliness and lateness penalties, fixed, travel-dependent, load-dependent and sustainability costs; standard strategies are VSR_DEF and VSR_1STEP (which can run carrier selection right after optimization); it is started with Optimizer Planning or in the background with report /SCMTMS/PLN_OPT (H07, VSR Optimization; S4TM2, VSR Optimizer)
- Transportation proposals show alternative routes, means of transport and times for a freight unit (entry points: the forwarding order actual route and the transportation cockpit); the result can save only the route (freight unit stages) or the route and freight documents (S4TM2, Transportation Proposals; E03, Assign Transshipment Locations and Generate Transportation Proposals)
- Scheduling determines start and end times for activities such as departure and arrival of a freight order, pick-up and delivery of freight units and coupling of trailers; it runs forward (first activity scheduled first) or backward (last activity first), the default strategy is Scheduling (Embedded) VSS_EMBED, and it considers time windows, loading and unloading durations, appointments, location sequence, existing freight orders, driver and vehicle availability and calendars (H07, Scheduling; S4TM2, Scheduling; E03, Perform Interactive Planning)
- Carrier selection assigns a carrier to subcontractable business documents manually or automatically, aiming at the lowest cost under constraints; it requires transportation lanes with carriers and means of transport and carrier selection settings (Create Carrier Selection Settings app) that define regular selection, tendering or direct shipment options; if no carrier is available none is assigned (H07, Carrier Selection; S4TM2, Carrier Selection)
- Automatic carrier selection optimizes with strategies Priority and Costs (internal costs from the transportation lane or carrier profile are used only for weighting, or charges from charge management), Continuous Move (simple continuous move or round trip with discounts), Business Share (target shares with tolerances and penalty costs) and a check against transportation allocations, which also applies to manual selection; SAP delivers strategy TSPS_DEF, and the result is a carrier ranking list (H07, Strategies; Continuous Move; Business Share; S4TM2, Carrier Selection; E03, Assign Carriers to Freight Orders)
- Strategy determination picks the most concrete transportation lane for the business document (location-to-location is more concrete than location-to-zone or a location lane), and for documents with several stops the overall carrier availability setting intersects the carriers of all stages (H07, Strategy Determination; Determining Available Carriers)

### Skill items (tier: inferred)
- Explain to a colleague, using the 5 tons of cement and 500 kg example, how split quantity, rounding value and item split determine the number of freight units a FUB rule creates
- Choose a FUB strategy and a document type (freight unit, transportation unit or freight order for the shortcut) for a described shipping situation and justify it from the grounded rules
- Trace which FUB rule the system determines for a business document by following the condition, standard rule and default cascade
- Set up and read the three cockpit start elements (selection profile, planning profile, page layout) and describe which one controls what is planned and which how
- Plan freight units onto a vehicle resource in the cockpit, check the scheduling result and switch between forward and backward scheduling
- Distinguish hard from soft constraints and say how a lateness cost influences a VSR optimization result
- Compare carrier selection strategies (Priority, Costs, Continuous Move, Business Share, transportation allocation) and say which setting each is configured in
- Recognize the one-step, two-step and three-step planning variants and the shortcut process in a described scenario

### Important questions
- Why does the size of a freight unit matter for planning, and what is the stated compromise between very large and very small freight units?
- Which parameters make the system put two business document items into separate freight units even when the FUB strategy says to consolidate as much as possible?
- What is the practical difference between creating a freight unit, a transportation unit and a freight order from the same business document, and when is the shortcut worthwhile?
- Which of the selection profile, planning profile and page layout would you change to restrict a planner to one region, to change the scheduling direction, or to hide a function in the cockpit?
- How does a soft constraint end up in the result of a VSR optimization run, and why will the optimizer sometimes accept a late delivery?
- When would you plan manually in the cockpit, when run VSR optimization, and when use one-step planning?
- Why are internal carrier costs called not real costs, and what do they actually do in carrier selection?
- What changes in carrier selection when transportation allocations or business shares are switched on?

### Deliverable (tier: inferred)
A one-page planning flow sheet for a fictional shipper: for one example order, show the freight unit building step (FUB strategy, planning quantity, split quantity and rounding value with the resulting number of freight units), the cockpit start (selection profile, planning profile, page layout), the planning choice (manual, VSR optimization or shortcut) with its scheduling direction, and the carrier selection strategy with the resulting ranking logic, using only terms and settings from the session material.

### Self-confidence question (tier: inferred)
Can I explain to a transportation planner, without notes, how a forwarding order becomes freight units, how those freight units are planned in the transportation cockpit, and how a carrier is selected for the resulting freight order?

### Quiz questions
```yaml
- q: A truck has a capacity of 20 tons and 20 tons of flour in 1 kg packages must be moved. How should freight unit building approach the freight unit size?
  o: ["Create a single freight unit weighing 20 tons", "Create 20,000 freight units of 1 kg each", "Create one freight unit per forwarding order item", "Aim for a size somewhere in the middle of both"]
  a: 3
  e: "H07 (Creation and Editing of Freight Units and VSR Optimization) states that neither extreme is advisable for this example: one freight unit of 20 tons or 20,000 units of 1 kg. Large units simplify VSR planning, small units make it harder, so the recommendation is to aim somewhere in the middle."
- q: Which result does the FUB strategy Consolidate per item produce?
  o: ["One freight unit for each business document item", "One freight unit for all items of a business document", "One freight unit for items from different documents", "One freight unit for each source and destination pair"]
  a: 0
  e: "H07 (Freight Unit Building Rule) explains that with Consolidate per item the system generates one freight unit per business document item, whereas Consolidate per request groups all items of a document and Consolidate as much as possible groups items from different documents."
- q: You want to transport 5 tons of cement but only in batches of 500 kg, so you define a split quantity of 500 kg in the FUB rule. How many freight units does the system generate?
  o: ["Five freight units", "Two freight units", "Ten freight units", "Fifty freight units"]
  a: 2
  e: "H07 (Planning and Split Quantities) gives exactly this example. The split quantity of 500 kg turns 5 tons into 10 freight units."
- q: For a business document the system finds no result from the condition entered in the business document type. What does it check next to determine the FUB rule?
  o: ["The planning profile assigned to the user", "A standard FUB rule in the business document type", "The carrier profile of the transportation lane", "The selection profile of the transportation cockpit"]
  a: 1
  e: "H07 (Determination of Freight Unit Building Rules) lists the order. First a condition in the business document type, then a standard FUB rule in the business document type, and finally the default settings."
- q: Which combination can be assigned to a profile and layout set in the transportation cockpit?
  o: ["A selection profile, a carrier profile and a resource calendar", "A planning profile, a freight order type and a rate table", "A page layout, a capacity profile and a scheduling strategy", "A selection profile, a planning profile and a page layout"]
  a: 3
  e: "S4TM2 (Transportation Cockpit) states that a combination of selection and planning profile together with a page layout can be assigned to a profile and layout set. E03 (How to Select Data for Planning) confirms the three elements."
- q: In manual planning you assign freight units to a vehicle resource. What does the system create as a result?
  o: ["A capacity document such as a freight order", "A new freight unit building rule for the vehicle", "A forwarding order for each assigned freight unit", "A transportation proposal for the vehicle resource"]
  a: 0
  e: "H07 (Manual Planning) explains that requirement documents such as freight units are assigned to capacities such as vehicle resources and the system creates capacity documents, for example freight orders, which can be processed further."
- q: How does VSR optimization treat a soft constraint such as a lateness cost?
  o: ["As a limit it must never violate", "As a warning shown after the run", "As a penalty cost within total costs", "As a filter set in the selection profile"]
  a: 2
  e: "S4TM2 (Hard and Soft Constraints) says VSR optimization always adheres to hard constraints, while soft constraints are modeled with penalty costs, for example lateness costs that are part of the total costs."
- q: In backward scheduling, which activity does the system schedule first?
  o: ["The first activity of the freight order", "The last activity to be scheduled", "The loading of the heaviest freight unit", "The coupling of the trailer to the truck"]
  a: 1
  e: "H07 (Scheduling) states that in backward scheduling the system first defines the start and end time of the last activity to be scheduled and then assigns times to all preceding activities, while forward scheduling starts with the first activity."
- q: In carrier selection, what are the internal costs that the Costs strategy can use?
  o: ["Costs used only for weighting, not real costs", "The final charges billed by the carrier", "The costs posted to the freight settlement document", "The penalty costs of the VSR optimizer run"]
  a: 0
  e: "H07 (Strategies) notes that the costs used are not real costs but internal costs used for weighting, defined in the transportation lane or in the carrier profile. S4TM2 (Carrier Selection) repeats this."
- q: What must be entered in the FUB rule so that the system creates freight orders directly instead of freight units?
  o: ["A transportation unit type with category Container", "A split quantity of zero for the planning quantity", "A planning profile with the strategy VSR_1STEP", "A freight order type as the document type"]
  a: 3
  e: "H07 (Automatic Creation of Freight Orders) states that for the shortcut scenario you enter a freight order type, or a condition that determines it, as the document type in the FUB rule. E03 (Compare the Standard and Shortcut Process) shows the freight unit being skipped."
```

---

## Session 07 — Freight Order Management and Execution

### Knowledge items
- Freight Order Management creates and edits freight orders (road and rail), freight bookings (air and sea) and trailer units, railcar units, container units and package units, which are used to plan with trailers, railcars and containers; in TM, freight bookings are created for the transportation modes air and sea, freight orders for all other modes (H06, Freight Order Management; S4611, Freight Orders and Freight Bookings)
- Freight order management is integrated with master data (a prerequisite), forwarding order management (values copied from forwarding orders or freight units), planning (freight orders are the result of planning and the basis for carrier selection), freight settlement (charge calculation), dangerous goods checks and global trade (H06, Integration)
- A freight order is an order whose execution is planned by a carrier or the shipper and contains the plan for the logistical processing (when and onto which vehicle freight units are loaded), planned departure times and execution data; it is the result of planning and the freight document for execution (H06, Freight Order; S4611, Freight Orders and Freight Bookings)
- A freight order holds planning information (means of transport, stages, routing, planned dates, durations, distances), document dependencies, charges and cost distribution, cargo information, execution information, business partner information (including drivers), output management, status and blocking information and subcontracting information; further: items, communication history, document flow, CO2 emissions, notes and attachments (S4611, Freight Orders; H06, Structure)
- Stages are created in the freight unit to split the transportation chain (for example pre-carriage to port of loading, main carriage, on-carriage), so separate freight orders or bookings can subcontract each stage to different carriers; one-time locations can be entered at stage level (S4611, Freight Order Creation; S48600, Freight Order Structure; H06, Structure)
- The freight order type holds the most important settings: basic settings (shipper and ship-to-party determination, whether subcontracting is allowed, delete or only cancel), charge calculation and settlement settings, execution settings, organizational unit determination, change controller settings, output options and driver settings; a user must select a type when creating a freight order manually (S4611, Freight Order Types; S4TM2, Freight Orders; H06, Use of Drivers)
- Organizational unit determination in a freight document: the system first checks a condition of type /SCMTMS/TOR_ORGUNIT, then the Consider Organizational Unit of User checkbox and the user assignment, and finally the default organization (S4611, Organizational Unit Determination; S4TM2, Freight Orders)
- The sequence type of stages of a freight order type is Defined and Linear, Non-Linear (Star-Shaped), Disconnected, Star-Shaped Based on FU Stages, Star-Shaped Based on FU Stages (Reversed), Linear with (De-)Consolidation Stages or Undefined; freight bookings allow only sequential stages (S4611, Sequence Type of Stages; S4TM2, Freight Orders and Freight Bookings)
- Freight orders can be created manually, from an inbound EDI message (service interface TransportationOrderGenericRequest_In), from transportation planning (manual planning, VSR optimization, background planning, or New in the cockpit), directly from a freight unit (one order per stage or for consecutive stages), by copying and from a schedule (report /SCMTMS/MP_SCHED_CREATE_TOR); S4611 describes manual creation, copying and creation through the Transportation Order Generic Request web service (H06, Creation and Editing of Freight Orders; S4611, Creating Freight Orders; S4TM2, Freight Orders)
- Creating a freight order by copying takes over header and logistical data but not references to freight units or execution information; a different freight order type may be chosen only if the sequence type of stages and the setting for customer self-delivery or pick-up match (H06, Creation by Copying; S4611, Creating Freight Orders)
- Manual creation process: enter general data (shipper, consignee, carrier, resources, locations, dates, driver, terms of payment), optional intermediate stops, items (insert freight units or enter items directly), optional charge calculation, check and save (consistency, capacity and dangerous goods checks), send to the carrier (Subcontracting, Send to Carrier), confirm or reject on behalf of the carrier, send loading and unloading instructions, print, fix the order against background processing and create the freight settlement document after execution (H06, Manually Creating Freight Orders)
- Direct creation of freight orders: on saving, a freight order is created directly from a forwarding order or transportation requirement if the document is subcontracted, not consolidated, deliverable in one freight order without pre- or on-carriage and has one source and one destination; the trigger is the document type, document attributes or quantity (via a FUB rule and conditions) and no further freight units can be added (H06, Direct Creation of Freight Orders)
- Freight orders can be created without a forwarding order and the forwarding order created later, which is recommended for customer self-delivery (items known after the truck is unloaded) and collective goods traffic (items known when the truck arrives) (H06, Creation of Forwarding Orders from Freight Orders)
- Editing and displaying: the Freight Orders (worklist) app with queries such as All Road Freight Orders, Create/Edit Road Freight Order and Create/Edit Rail Freight Order, and the transportation cockpit, which shows freight orders only if they match the selection profile for freight orders and freight bookings; tabs include General Data, Items, Overview, Subcontracting, Document Flow, Charges, Cost Distribution, Execution, Statuses, Output Management and Communication History (H06, Editing and Displaying Freight Orders; E03, Explain Transportation Documents)
- Freight bookings reserve freight space on a vessel or aircraft (ocean and air freight bookings with mode-specific data such as vessel name or flight number), are consumed by assigning freight units or container units and can be created manually, from a worklist or by copying; drivers cannot be assigned to bookings, all booking types can be subcontracted and only carrier selection (not tendering) is offered (S4TM2, Freight Bookings; H06, Freight Booking; E03, Create an Ocean Freight Booking)
- Rail freight orders model a train with locomotives (vehicle resources, only the main locomotive at header level is considered in planning) and railcars (passive vehicle resources, individual items or multi-items) to which cargo items are assigned; schedules can be assigned at header or stage level and non-linear stages are not supported (H06, Rail Freight Order)
- In rail scenarios the invoicing carrier invoices the shipper or bill-to party for its stages (rule 11 in North America); carriers can be assigned by stage, the Default Route function proposes routing options from default routes, freight agreement items and rate tables sorted by price, and one freight settlement document is created per invoicing carrier (H06, Rail Freight Order; Rail Transportation)
- Setting the cargo execution status of a railcar multi-item adjusts all subitems and cargo items, and loading single cargo items sets the multi-item to Cargo Partially Loaded and then Cargo Loaded (H06, Rail Freight Order, Status)
- Drivers (road freight orders and trucks only) are business partners with validity, non-working times and absences; a default driver can be linked to a vehicle resource; the freight order type defines one driver or a driver team, assignment per stage or per order and whether this can be changed; the system checks overlaps and availability and sets the Driver Assignment Status (Not Relevant, Underassigned, Fully Assigned, Overassigned); drivers not in master data can be entered with No Master Data Defined (H06, Use of Drivers in Freight Order Management; S4TM2, Driver Management)
- A driver team (two drivers who take turns driving and sleeping) is recommended for time-critical orders such as rush orders, while a driver assigned per transportation stage means only one driver is in the cabin at a time; in the cockpit drivers can be assigned by drag and drop, by manual entry or through the Assign Driver dialog (H06, Use of Drivers; S4TM2, Automatic Assignment of Drivers)
- Appointments for freight orders are defined on the Overview or Stages tab or in the cockpit; the acceptable start of loading and acceptable end of unloading of freight units must lie within the appointment, otherwise an error is raised; scheduling a freight order adjusts departure and arrival times and derives loading and unloading times of the freight units, and changes to dates propagate between forwarding order, freight units and freight order, with an execution block if the order is already in execution (H06, Appointments; Scheduling of Freight Orders)
- Carrier assignment: the carrier is the business partner the freight order is subcontracted to and can differ from the executing carrier; manually a carrier is entered in the freight order or assigned by Mass Change from the worklist; automatically through the default route, the partner function SP (Forwarding Agent) in the delivery, the partner determination profile of the freight order type (fixed partner or BAdI) or a process controller strategy (S4611, Subcontracting to Carriers; E03, Assign Carriers to Freight Orders)
- Sending to the carrier: Subcontracting then Send to Carrier sends TransportationOrderRequest_Out, the carrier confirms via TransportationRequestConfirmation_Out and the shipper receives it with TransportationOrderConfirmation_In; the Communication History tab lists all messages including the XML; on subcontracting the system recalculates charges and cancels subcontracting if they changed (H06, External Communication in Overland Transportation; Manually Creating Freight Orders; E03)
- Freight order statuses: life cycle (New, In Process, Complete, Canceled), driver assignment, planning (Not Planned, Partially Planned, Planned and more), subcontracting (No Subcontracting Result, In Tendering, Carrier Assigned, Sent, Changed After Sending), confirmation (No Confirmation Yet, Invalid Confirmation Received, Rejected, Confirmed, Confirmed with Changes and more), tendering and execution; in the exercise, assigning a carrier gives In Process, Carrier Assigned and Not Started, sending gives Sent and No Confirmation Yet, and Set to confirmed by carrier gives Confirmed (H06, Statuses; S4611, Exercise 6)
- Execution status values: Not Started, Capacity Planning Finished, Loading in Process, Ready for Transportation Execution, Not Ready for Transportation Execution, In Execution, Executed, Interrupted, Canceled, Not Relevant; it is set automatically for documents subject to tracking or manually, and a last expected event can set Executed automatically (H06, Execution Status)
- Handling execution status is set on item level (Not Determined, Not Unloaded, Unloaded, Not Loaded, Loaded, and for trailer or railcar units Coupled, Uncoupled and their negatives) and on stop level (for example Cargo Ready for Loading, Arrived, Checked In), and the cargo execution status of containers and railcars follows it (H06, Handling Execution Status)
- Transportation execution in (basic) TM: the freight order is the central document until the vehicle has left the loading location and for status tracking afterwards; actual quantities and discrepancies can be recorded, loading status maintained manually, local events monitored on the Execution tab, external events reported through the TOR_GENERIC web service, local container or package items and seal data maintained on the Items tab (S4611, Describing Freight and Transport Execution)
- Output management creates print and other outputs for freight units, freight orders, freight bookings, freight agreements and freight settlement documents; the output profile in the document type maps to a PPF action profile (for example /SCMTMS/TOR_PRINT_ROAD with CMR, waybill, packaging labels), and PPF answers what (action definition), why (scheduling condition) and when (starting condition); PPF actions only process data already saved to the database (S4611, Creation of (Print) Freight Documents; E04, Generate Outputs for Freight Orders)
- Tracking and event handling: SAP Event Management (on-premise capable) and SAP Business Network Global Track and Trace (cloud, separately licensed) monitor freight units, freight orders, freight bookings, transportation units and resources; event types are regular, overdue, unexpected and unreported (S48600, Freight Order Execution)
- Delivery creation can be triggered in TM: TM creates delivery proposals from freight units, freight orders and bookings (dates from the freight order or booking, quantities from the freight units), sends them to the ERP system, and the delivery builder, a background report /SCMTMS/DLV_BATCH, worklists or the cockpit after planning can trigger it; freight units are consolidated into one proposal only if, for example, source, destination, Incoterms and shipping conditions match (S48600, Delivery Creation; E04, Create Deliveries)
- Delivery changes and splits: changed planning dates can update the outbound delivery, and if freight units of one delivery are planned on different freight orders the delivery is split automatically (only when the first or last stage of the chain is affected, and only for outbound deliveries from TM); in the exercise the system created two deliveries after the second freight order was saved (S48600, Delivery Change and Split; E04, Trigger a Planning-related Delivery Split)
- Warehouse integration in execution: in basic TM all warehouse options (Inventory Management with optional Handling Unit Management, Stockroom Management, EWM) are integrated through the delivery; advanced shipping and receiving integrates shipping and receiving into the freight order (S4611, Exploring Warehouse Integrations; S48600, Warehouse Integration)
- Loading and unloading with the Load or Unload Freight Orders app: assign loading points, unloading points and doors, set arrived at or departed from door, set items to loaded or unloaded, set the stop to loading completed, and post goods issue or goods receipt; goods issue of an outbound delivery is tied to a freight order covering the first stage and goods receipt of an inbound delivery to one covering the last stage, controlled by events such as Loading Begin, Loading End or Departure (S48600, Loading and Unloading Freight Orders; E04, Execute an Integrated Warehouse and Transportation Process)
- In the integrated warehouse exercise (transportation-driven) the outbound delivery order stays blocked until the freight order is set to Ready for Transportation Execution and its items to Ready for Warehouse Processing; then warehouse tasks are created and confirmed, and the freight order shows In Execution after departure from the door with warehouse processing partially completed while further stops remain (E04, Execute an Integrated Warehouse and Transportation Process)
- In the basic shipping exercise the deliveries are picked (Pick Outbound Delivery), goods issue is posted in Manage Outbound Deliveries (status Ready to Post GI, then goods movement status Completed) and the freight order is set to Loaded and then Departed, giving In Execution (S4611, Exercise 8)

### Skill items (tier: inferred)
- Walk through the manual creation of a road freight order from the data entered to the freight settlement document, naming the app or menu entry for each step
- Compare the freight order creation methods and pick the one that fits a described case (regular customer and carrier, copy of an existing order, order created from a freight unit, customer self-delivery)
- Read the Statuses tab of a freight order and explain what each of life cycle, subcontracting, confirmation and execution status says about where the order stands
- Describe the subcontracting sequence from carrier assignment to Send to Carrier and Set to confirmed by carrier and the statuses after each action
- Explain how drivers are assigned to a freight order (single driver, driver team, per stage) and what the Driver Assignment Status means
- Describe the order of events in a transportation-driven warehouse and transport execution, from Ready for Transportation Execution to goods issue and departure
- Explain how PPF output management decides what, why and when a document output is created for a freight order

### Important questions
- What distinguishes a freight order from a freight booking, and which transportation modes and planning constraints belong to each?
- Why can a freight order type with the sequence type Defined and Linear not be replaced by one with a non-linear type when copying an order?
- Which creation method would you use for a daily collection route where the goods are known only after unloading, and why?
- How do the subcontracting status, the confirmation status and the execution status of a freight order change independently of each other?
- What does it mean for a warehouse process to be transportation-driven, and which status changes release the warehouse side?
- Why does the system split a delivery when its freight units land on different freight orders, and what must be true for the split to be needed?
- Where does the freight order stop being the leading document in basic transportation management, and which tracking options exist beyond that?
- How do the rail invoicing carrier and stage-level carrier assignment change settlement compared with a road freight order?

### Deliverable (tier: inferred)
A freight order lifecycle storyboard for one road shipment: a sequence of steps from creation (method and freight order type), carrier assignment and sending, confirmation, ready for transportation execution, warehouse loading with door assignment, goods issue and departure to completion, with the relevant status values (life cycle, subcontracting, confirmation, execution) shown after each step and the output documents that PPF would create, using only values named in the session material.

### Self-confidence question (tier: inferred)
Can I explain to a dispatcher, without notes, how a freight order is created, assigned to a carrier and driver, and followed through warehouse loading, goods issue and departure using its statuses?

### Quiz questions
```yaml
- q: For which transportation modes does TM create freight bookings instead of freight orders?
  o: ["Road and rail", "Road and sea", "Air and sea", "Rail and air"]
  a: 2
  e: "S4611 (Freight Orders and Freight Bookings) states that for the transportation modes Air and Sea freight bookings are created, and for all other modes freight orders. H06 (Freight Order Management) lists freight orders for road and rail and freight bookings for air and sea."
- q: When a freight order is created by copying an existing one, what does the system copy?
  o: ["Header data and logistical data", "References to the freight units", "Execution information such as actual times", "Freight unit assignments and charges"]
  a: 0
  e: "H06 (Creation by Copying) and S4611 (Creating Freight Orders) both state that the header data and the logistical data are copied, but references to freight units and execution information are not."
- q: When the system determines the purchasing and execution organization of a freight document, what does it check first?
  o: ["Whether the user is assigned to a purchasing organization", "Whether the Consider Organizational Unit of User box is set", "The default organization kept in the document type", "The condition of type /SCMTMS/TOR_ORGUNIT"]
  a: 3
  e: "S4611 (Organizational Unit Determination) says the system first checks the condition, then the Consider Organizational Unit of User checkbox and the user assignment, and only then uses the default organization. S4TM2 (Freight Orders) describes the same order."
- q: In a rail scenario with an invoicing carrier (rule 11 in North America), what does the invoicing carrier do?
  o: ["It executes every stage of the rail freight order itself", "It invoices the shipper or bill-to party for its stages", "It supplies the locomotive that is planned as main item", "It confirms the loading of the railcars at the source location"]
  a: 1
  e: "H06 (Rail Freight Order) defines the invoicing carrier as the carrier that invoices the shipper, or another designated bill-to party, for the charges calculated for the corresponding stages."
- q: For which kind of order does the SAP Help documentation recommend assigning a driver team?
  o: ["Time-critical orders such as rush orders", "Orders with several unloading points per day", "Orders executed by a subcontracted carrier", "Orders that contain dangerous goods only"]
  a: 0
  e: "H06 (Use of Drivers in Freight Order Management) recommends a driver team for time-critical orders, for example rush orders, because two drivers are in the cabin and take turns driving and sleeping."
- q: After you choose Send to Carrier on a freight order, which confirmation status does the order show?
  o: ["Confirmed with Changes", "Invalid Confirmation Received", "No Confirmation Yet", "Update Sent, No Confirmation Yet"]
  a: 2
  e: "S4611 (Exercise 6 solution) and E03 (Assign Carriers to Freight Orders) show subcontracting status Sent together with confirmation status No Confirmation Yet after sending. H06 (Statuses) defines that value as the carrier not having sent a confirmation yet."
- q: In the transportation-driven exercise, why is the outbound delivery order blocked at first?
  o: ["The warehouse tasks for the delivery have not yet been confirmed", "The transportation team has not signaled warehouse readiness yet", "No loading point and door have been assigned to the warehouse stop", "The freight order has not yet been scheduled by the VSR optimizer"]
  a: 1
  e: "E04 (Execute an Integrated Warehouse and Transportation Process) explains that one side must lead the integration and in a transportation-driven process the outbound delivery order stays blocked until the transportation team indicates readiness for warehouse processing. The block is lifted after the items are set to Ready for Warehouse Processing."
- q: In PPF output management, which condition decides the point in time at which an action is executed?
  o: ["The scheduling condition", "The spool condition", "The update condition", "The starting condition"]
  a: 3
  e: "S4611 (Output Management Conditions) explains that the scheduling condition answers why an action is executed, while the starting condition is checked just before execution and defines when, for example on save or one day before pick-up."
- q: A goods issue of an outbound delivery can only be associated with the execution of a freight order covering which part of the transport?
  o: ["The first stage of the transport", "The last stage of the transport", "Any stage that contains a warehouse stop", "The main carriage stage only"]
  a: 0
  e: "S48600 (Posting Goods Issue and Goods Receipt) states that goods issue for an outbound delivery can only be associated with a freight order covering the first stage, while goods receipt for an inbound delivery relates to the last stage."
- q: Two freight units of one outbound delivery are planned on different freight orders. What does the system do?
  o: ["It rejects the second freight order assignment", "It merges both freight orders into one document", "It splits the original delivery in two", "It keeps the delivery and sets an execution block"]
  a: 2
  e: "E04 (Trigger a Planning-related Delivery Split) shows the system automatically splitting the original delivery so each freight order and freight unit has its own delivery. S48600 (Delivery Change and Split) says the split is required when freight units of one delivery go to different freight orders."
```

---

## Session 08 — Agreement Management, Strategic Freight Procurement and Carrier Collaboration

### Knowledge items
- Purpose of Agreement Management: shippers and LSPs forecast and assess transportation requirements, request bids from carriers and negotiate contracts (agreements); carriers use it to respond with rates; agreements are the basis for charge calculation, and Agreement Management is integrated with Charge Management and Service Product Catalogs (H08, Agreement Management).
- Strategic freight procurement (SFP) is tailored mainly to shippers procuring long-term transportation services from carriers or LSPs; it runs in four steps: Prepare RFQ, Submit RFQ, Evaluate responses and optimize, Generate agreements (S4TM3, Unit 6; H08, Strategic Freight Procurement).
- Determining procurement needs: historic transportation is analyzed as a forecast and divided by trade lane, commodity code or transportation mode; legacy systems or TM analytics (overview pages, CDS views) can be used, but their use is not mandatory for SFP (S4TM3, Unit 6).
- Freight agreement RFQ master: the central business document with a shipper's or LSP's transportation requirements for a future period; it can be created with the Manage Freight Agreement RFQ Masters app or from a template, and per S4TM3 from an existing freight agreement, a template, anew, or by copying an RFQ (H08, Freight Agreement RFQ Master; S4TM3, Unit 6).
- Structure of the RFQ master: header data (organizational unit, validity period, carriers, RFQ type, RFQ negotiation round number, response deadline, calculation sheet template, Carrier KPI Profile, Incumbent indicator) and items with tabs for Calculation Sheet Overview, Carriers, Trade Lanes, Capacities, Commodity Codes, Default Route, Document Flow, Output Management, Excel Integration, Versions and Award Summary; only a purchasing organization, company or corporate can be assigned as organizational unit (H08; S4TM3).
- Carriers are maintained on the RFQ master header; they can be deleted per item but a carrier cannot be added on a single item; carriers of an existing freight agreement are flagged Incumbent (S4TM3, Unit 6).
- Rating structure of an RFQ item: calculation sheets define which charges are calculated and how, rate tables define rates directly in TM; the Request Rate checkbox marks the rate records downloaded in an individual RFQ spreadsheet; carriers submit rates and promised capacity but cannot change the structure of calculation sheets or rate tables (H08, Strategic Freight Procurement).
- Target rate or target amount: the maximum price the shipper is willing to pay, with a tolerance percentage (example 1000 USD with 10% means rates above 1100 USD need not be considered); it is shown to carriers only if Publish Target Rate is selected in the freight agreement RFQ type (H08; S4TM3).
- Publication: publishing the master automatically creates and sends individual freight agreement RFQs; creation and publication can be separated into two steps (otherwise the Create & Publish indicator does one step), individual RFQs cannot be sent selectively, an approval workflow can be enabled, and mass processing uses /SCMTMS/RFQ_PUBLISH; a master that cannot be published stays in Publication in Process, is checked in SLG1 and republished with /SCMTMS/RFQ_RE_PUBLISH (H08; S4TM3).
- System notifications to carriers: after publication, as the response deadline approaches, on the deadline, on cancellation, after creation of the agreement, and when the agreement is expiring, using business-to-business communication (H08, Requesting of Quotations for Transportation Services).
- Negotiation rounds versus versions: a new negotiation round (Follow Up, Create Negotiation Round) requires a published master, adds 1 to the round number and resets the version number to zero; a new version (Generate New Version) needs status In Process, adds 1 to the version number and keeps the round number (H08; S4TM3).
- Response evaluation in the comparison cockpit: manual comparison by carrier and charge type (flat amounts only, ranking by lowest quoted rate, manually entered target share) or optimizer-based comparison for complex cases with constraints (H08, Post-Bid Analysis; S4TM3, Unit 6).
- Target share strategies and strategy conditions (Define Target Share Strategies): minimum and maximum target share, minimum and maximum number of carriers, separate conditions for incumbent carriers, respect for carrier-promised capacity; the optimizer can be run in the back end with /SCMTMS/OPTIMIZER_RUN, can use historical spend simulation, and can add risk or bonus-malus logic via BAdI (H08; S4TM3).
- Strategy spend estimation and Award Summary: the system estimates cost, it does not calculate actual charges; the strategy spend comparison graph compares strategy versions; the Award Summary tab shows graphs by trade lane, carrier or RFQ item and last year's spend (H08).
- Awarding and agreement creation: selecting and accepting the preferred target share strategy calculates the confirmed capacity (changeable manually) and sets the RFQ status to Awarded; Create/Update Agreement generates or updates freight agreements per carrier, with agreement allocations; the optimizer's target share is copied into the business share used in carrier selection in planning (H08; S4TM3).
- Award confirmation (optional, enabled in the RFQ type): an award confirmation deadline, the Notify the Carrier for Award Confirmation button, consolidation of carrier confirmations, and statuses; it is only a soft confirmation, carriers are not rejected if they miss the deadline (H08, Award Confirmation).
- RFQ master assignments distribute single RFQ items to analysts or organizations whose results are merged back once approved; publication to carriers is possible only from the master (S4TM3, Unit 6; H08).
- Reverse auction: carriers can revise bids and see the current best rates; by default only lower bids are possible unless Allow Carriers to Increase their Bids is selected (H08, Reverse Auction).
- Carrier collaboration prerequisites: for each carrier, a business partner with the role Carrier and a collaboration user defined in the Maintain Collaboration Users app; carriers need not use TM (H10, Carrier Collaboration).
- Carrier response to freight agreement RFQs: in the Manage Freight Agreement RFQs app the carrier monitors RFQs by status, responds with rates or rejects participation, can download and upload a spreadsheet; the shipper then accepts or rejects rates, requests confirmation and creates or updates the freight agreement (H10, Management of Quotations for Transportation Services).
- Carrier apps for order management: Manage Freight RFQs (accept, accept with proposed changes if the shipper allows it, or reject; accepting creates a freight quotation that can be revised within the deadline), Display Freight Quotations (pending, rejected, awarded), Confirm Freight Orders (Confirm with Changes, driver and vehicle details) and Manage Execution of Freight Orders (report planned and unplanned events and actual quantities; no events for a blocked freight order) (H10).

### Skill items (tier: inferred)
- Walk through the SFP process from the RFQ master to the freight agreement and name the document, status or app involved at each step.
- Decide whether a given RFQ calls for manual comparison or the optimizer, and say which strategy conditions would apply.
- Choose between a new version and a new negotiation round for a given change request.
- Match each carrier action (respond to RFQ, quote, confirm, report events) to the carrier app that supports it.

### Important questions
- Why does TM keep both versions and negotiation rounds, and what does each protect?
- When is a manual response comparison enough, and when should the optimizer be used?
- How does the optimizer's target share end up influencing carrier selection in planning?
- What does a carrier need on the shipper's side to respond without using TM?
- What does it mean that the award confirmation is only a soft confirmation?

### Deliverable (tier: inferred)
A one-page process map of strategic freight procurement from RFQ master to freight agreement, showing for each step the shipper action, the carrier action, the document or status involved and the app or report used.

### Self-confidence question (tier: inferred)
Can I explain how a shipper moves from a freight agreement RFQ master to a freight agreement, and what the carrier does at each step, to a procurement manager without notes?

### Quiz questions
```yaml
- q: In S4TM3, the strategic freight procurement process is divided into four steps. Which sequence is correct?
  o: ["Prepare RFQ, evaluate responses and optimize, submit RFQ, generate agreements", "Submit RFQ, prepare RFQ, generate agreements, evaluate responses and optimize", "Prepare RFQ, submit RFQ, evaluate responses and optimize, generate agreements", "Prepare RFQ, submit RFQ, generate agreements, evaluate responses and optimize"]
  a: 2
  e: "S4TM3, Unit 6 Process Steps. The four steps are Prepare RFQ, Submit RFQ, Evaluate responses and optimize, and Generate agreements."
- q: A shipper sets a target amount of 1000 USD with a tolerance of 10% in a calculation sheet. For which carrier rate does the shipper not have to consider the carrier when awarding?
  o: ["Any rate higher than 1100 USD", "Any rate higher than 1010 USD", "Any rate lower than 900 USD", "Any rate higher than 1000 USD"]
  a: 0
  e: "H08, Strategic Freight Procurement, Rating structure. With a target of 1000 USD and a tolerance of 10%, a proposed rate higher than 1100 USD means the carrier need not be taken into consideration."
- q: What happens to the numbers on a published freight agreement RFQ master when you create a new negotiation round?
  o: ["The round number goes up by 1 and the version number is kept as it was", "The round number is kept as it was and the version number goes up by 1", "Both the round number and the version number are set back to zero again", "The round number goes up by 1 and the version resets to zero"]
  a: 3
  e: "H08, Requesting of Quotations for Transportation Services, Negotiation Rounds and RFQ Versions. A new negotiation round updates the number of negotiation rounds by 1 and resets the version number to zero, so the latest round always has a clean version."
- q: Where must the carriers taking part in strategic freight procurement be maintained in the freight agreement master RFQ?
  o: ["On each RFQ item, because a carrier can be added on a separate item", "On the header, from where carriers can be deleted on single items", "In the individual RFQs, once the master RFQ has been approved by the head of purchasing", "In the target share strategy, before the master RFQ is created in the system"]
  a: 1
  e: "S4TM3, Unit 6, RFQ Carrier Definition. All carriers must first be maintained on the header level, and a carrier cannot be added on a separate item; carriers can only be deleted from an item."
- q: How does the award confirmation deadline in a freight agreement RFQ master work?
  o: ["It is a hard confirmation, and carriers that miss it are rejected automatically by the system", "It is a binding confirmation that blocks the creation of the freight agreement until it arrives", "It is a soft confirmation, and carriers are not rejected if they miss it", "It is a confirmation that applies only to carriers that use TM themselves as their own system"]
  a: 2
  e: "H08, Award Confirmation, Features. The confirmation is only a soft confirmation; the system does not reject carriers that do not respond within the deadline, and the shipper can still confirm capacities with them offline."
- q: What does the system do automatically when you accept the preferred target share strategy in the comparison cockpit?
  o: ["It calculates the confirmed capacity in the RFQ master", "It creates the individual RFQs for all the carriers again", "It publishes a new negotiation round to all the carriers", "It posts the estimated spend as actual charges to orders"]
  a: 0
  e: "H08, Requesting of Quotations for Transportation Services, Preferred Target Share Strategy. Accepting the preferred strategy automatically calculates the confirmed capacity from the optimizer's target share; it can be changed manually before agreements are created. S4TM3 adds that the RFQ status is set to Awarded."
- q: For which responses can you compare directly in TM without the optimizer, and how are carriers ranked?
  o: ["Charge types with rate tables, ranked by the highest promised capacity", "All charge types, with the optimizer proposing the target shares for carriers", "Charge types with local rate tables only, shown in a response comparison graph", "Charge types with flat amounts, ranked by lowest quoted rate"]
  a: 3
  e: "H08, Post-Bid Analysis, Manual Response Comparison. Manual comparison directly in TM works only for charge types with flat amounts, and the system ranks carriers by the lowest quoted rate per charge type."
- q: Which organizational units can be assigned to a freight agreement RFQ master?
  o: ["Purchasing group, purchasing office or company", "Purchasing organization, company or corporate", "Purchasing organization, purchasing group or corporate", "Company, corporate or purchasing office"]
  a: 1
  e: "H08, Freight Agreement RFQ Master, General Data. Only a purchasing organization, company or corporate can be assigned; a purchasing group or purchasing office cannot."
- q: What must be set up for each carrier that is to collaborate with the shipper without using TM?
  o: ["A business partner with the role Carrier and a collaboration user for it", "A business partner with the role Carrier and a TM license on the carrier side", "A freight agreement with the carrier and a published tendering plan already in place", "A collaboration user that is not assigned to any business partner of the shipper"]
  a: 0
  e: "H10, Carrier Collaboration, Prerequisites. A business partner with the role Carrier is created, and a collaboration user is defined in the Maintain Collaboration Users app for that business partner."
- q: In the Manage Freight RFQs app, when can a carrier accept a freight RFQ by proposing changes to price, currency or dates?
  o: ["When the carrier already has a freight agreement with the shipper in place", "When the freight RFQ is still open after the response deadline has passed", "When the shipper has configured the tendering settings to allow proposed changes", "When the freight quotation has already been awarded to the carrier"]
  a: 2
  e: "H10, Freight Request for Quotation. Accepting with proposed changes is available only if the shipper has configured the tendering settings to allow it."
```

---

## Session 09 — Charge Calculation and Freight Agreements

### Knowledge items
- Scope of charge calculation in the course: master data for charge calculation, charge calculation and freight settlement processes on the buying side only; charge calculation for forwarding orders (selling side) is not covered (S4TM3, Charge Calculations).
- Charge calculation determines the freight charge for a transportation scenario from conditions in the business rules framework, charge calculation master data and configuration items; the result goes back to the requesting document together with charge type, charge category or subcategory so accounting can determine organizational unit, cost or revenue receivers and general ledger account (S4TM3, Charge Calculations).
- Charge requests can come from the freight order, freight booking, service order, dispute, freight agreement RFQ, forwarding quotation, forwarding order, forwarding settlement document and freight settlement document (S4TM3, Charge Requests).
- Charge Management master data: scale template, scale (a dimension of a rate table), rate table (rates by validity period), charge types (for example Haul, BAF, FSC), calculation sheet (hierarchical table combining permitted charge types and their sequence) and freight agreement (S4TM3, Charge Requests; Calculation Sheet Maintenance).
- Business example Road-Sea-Road: a sales order builds a freight unit, the planner creates stages (precarriage by truck Denver to Newark, main carriage by vessel Newark to Rotterdam, on-carriage by truck Rotterdam to Cologne); freight orders for the truck stages and a freight booking for the main carriage each get their own calculated amount used to pay the carrier (S4TM3, Business Example Road-Sea-Road).
- Scale base: defines how the system interprets a scale and is defined in Customizing under Define Scale Bases; its fields include Field Assignment, UoM Relevant, Dimension (link to T006), Rounding Rule, Numeric, Crcy Scale base, Raw values and Date Scale Base; example WEIGHT with dimension Mass; a rate that depends on distance and weight needs a separate scale for each, and scales can be reused in several rate tables (S4TM3, Scale Base).
- Scale types and scale creation: Base scale (from a value upward, >=), To Scale (up to a value, <=) and Same Scale (exactly one value, =); a scale also has a scale unit of measure, a rounding profile and a calculation type (absolute for non-numeric scales such as region, transportation zone or business partner, relative for numeric scales such as weight, distance, length); scales are created in the Create Scale app or during rate table maintenance (S4TM3, Scale Templates; Scale Creation).
- Scale templates: optional help to create scales and predefine scale items; Customizing templates are transportable but cannot have items for Same Scales, master data templates can and need no Customizing authorization but cannot be transported (S4TM3, Scale Templates).
- Calculation base: the actual base or factor on which a charge is calculated, defined for a scale base in Define Calculation Bases (for example W1 for gross weight and W2 for net weight under scale base Weight, or DESTLOC for the destination location); its fields include Field Assignment, Currency Field, Unit Field, Helper Assignment, Use BAdI, Party Role, Calculation Type, Calculation Usage and TrM Category (S4TM3, Calculation Base).
- Resolution base: determined by the origin of the data a charge aspect is based on, with Root (document header), Stage, Container and Product as examples; for instance the gross weight of the order uses the root, and per-package freight uses the package (S4TM3, Resolution Base; E05, Explain a Calculation Sheet).
- Charge types: classify a charge line (for example base rate, surcharge, discount); settings include positive or negative value, absolute or percentage, charge category and subcategory, tax indicator, rounding, default calculation base, leading charge type, inactive flag and transportation mode category; categories and subcategories map to SD pricing condition types for billing and MM service activities for carrier invoice processing (S4TM3, Charge Categories; Charge Type Settings).
- Rate tables: a price list grouped by validity period (business object /SCMTMS/TC_RATES), up to 14 dimensions though not recommended, with rate table determination rules to reduce dimensions; created manually, from rate table templates, or maintained in Microsoft Excel; Create Rate Table Definition defines the structure and Maintain Rate Table maintains rates; minimum and maximum values, calculation rules, the No Value Allowed flag for generic rates, and an optional approval workflow (S4TM3, Rate Tables; Rate Table Maintenance).
- Calculation sheet: charge usage in the general data; hierarchy items with instruction types Sum, Subtotal, Standard and Compare High/Low Value; each item has Rate, Basic Data (manual charge item, resolution base, rounding and adjustment profiles, dimensional weight profile, calculation method), Classification (mandatory, tax, statistical charge) and Preconditions tabs; a percentage item must refer to another item or subtotal (S4TM3, Calculation Sheet Maintenance).
- Agreements: forwarding agreements (FWA) for charges billable to the customer, freight agreements (FA) for charges billed by the carrier, internal agreements (IA) between organizations of a company, and service agreements as a type of freight agreement; contractual data covers organizational unit, parties, payment terms and validity; the agreement type Customizing sets allowed item types, default calculation sheet template, multiple parties and allocation type (S4TM3, Agreements Overview; Contractual Data in Agreements).
- Agreement determination: by organization, business partner, validity period and preconditions; with several matches a leading charge type or the agreement priority decides; preconditions on agreement items are built-in (trade lanes, partners, item precondition) or BRFplus/BAdI; calculation profile determination types Minimum Charges, Maximum Charges and Determine All Agreements enable manual selection; condition types TCM_FAGDET and TCM_FAGDEX determine or exclude agreements (S4TM3, Agreement Determination; S48600, Charge Calculation).
- Calculation profile and charges profile: the calculation profile sets the date type for rate and validity, the calculation level (header, item or stage), determination rules, through rates, dimensional weight profile and data source (actual or ordered route); a charges profile assigned to a purchasing organization groups it with the settlement and cost distribution profiles; a profile on a business partner role takes precedence over one on the organizational unit; the freight order type must enable charge calculation (S4TM3, Calculation and Charges Profiles; Calculation Settings in Freight Order Types).
- Calculation process: collect data from the transaction object, configuration, BRF+ conditions, master data and BAdIs, determine the freight agreement, then the calculation sheet, calculate each charge type, keep a log and show results in the freight order; rate derivation determines calculation base and rate table, reads logistical data, determines the date baseline, finds the matching rate table record and calculation rule, and calculates the amount; the transportation zone rate is found by going up the zone hierarchy (S4TM3, Freight Order Charge Calculation; Freight Rate Derivation Process; S48600).
- Special calculation features: through rates across several stages (carrier-dependent, enabled in the calculation profile), header-level charges alongside stage-level calculation, and calculation methods such as break-weight (cheaper next rate) and clipping (level-by-level totals, one scale item relative) (S4TM3, Charge Item at Header and Stage Level; Charge Calculation with Through Rates; Calculation Methods).
- Hands-on example in E05: freight agreement FRAGR_S4TM1_CAR10 with calculation sheet S4TM1_CALCSHET_CAR10; rate table BASE_RATE_00 with scales S4LG1_COUNTRY (countries) and S4LG1_WEIGHT (up to 100, 200, 500, 1.000, 5.000 and 999.999.999 kg); Update Rates with simulation mode and Excel download and upload; Calculate Charges in the freight order shows the agreement, calculation sheet, rate table, rate amount and calculation rules (E05).

### Skill items (tier: inferred)
- Trace a calculated freight order charge back through calculation sheet, charge type, rate table, scales and agreement.
- Choose a scale type and calculation type for a given rate dimension such as weight or destination country.
- Pick the resolution base that applies a charge once per header, stage, container or product.
- Explain why a given agreement was or was not determined, using priority, leading charge type and determination type.

### Important questions
- What is the difference between a scale base, a scale, a calculation base and a resolution base?
- Why can one freight order have charges from several agreement items, and what decides which one is used?
- When does Update Rates split a validity period, and how does simulation mode help?
- What does a through rate change compared with stage-by-stage calculation?
- Why must a custom calculation base always get a scale base?

### Deliverable (tier: inferred)
A diagram of the charge calculation master data chain (scale base, scale, rate table, charge type, calculation sheet, freight agreement) annotated with the E05 example objects and the steps the system takes to calculate one charge line in a freight order.

### Self-confidence question (tier: inferred)
Can I explain how TM turns a freight order into a calculated charge, from agreement determination to the rate table lookup, to a logistics manager without notes?

### Quiz questions
```yaml
- q: A BASE rate table has scale levels up to 5 tons at USD 50 absolute, up to 7 tons at USD 14 per ton, up to 10 tons at USD 13 per ton and up to 15 tons at USD 12 per ton. What does the Clipping calculation method charge for a 12-ton load?
  o: ["USD 144", "USD 139", "USD 141", "USD 156"]
  a: 2
  e: "S4TM3, Clipping Example. Clipping works through the scale levels (50 + 28 + 39 + 24) for USD 141, while without clipping the 12 tons fall into the up to 15 tons level at USD 12 per ton, which gives USD 144."
- q: In scale maintenance, what does a scale of type Base scale mean?
  o: ["The scale levels apply from a certain value upward (>=)", "The scale levels apply up to a certain value (<=)", "The scale levels apply for exactly one value (=)", "The scale levels apply only to non-numeric values such as regions"]
  a: 0
  e: "S4TM3, Scale Creation Data and Scale Template Fields. Base scale means from a certain value and upwards (>=), To Scale means up to a certain value (<=) and Same Scale means exactly one value (=)."
- q: How does TM distinguish gross weight from net weight when both belong to the scale base Weight?
  o: ["They use two different scale bases, one for each type of weight that is charged", "They share one calculation base and differ only by the rounding profile that is applied", "They use two scales that are defined with different units of measure in the system", "They share the scale base Weight but have calculation bases such as W1 and W2"]
  a: 3
  e: "S4TM3, Calculation Base. Gross and net weight both correspond to the scale base Weight, but they are different charge aspects and therefore get different calculation bases, for example W1 for gross weight and W2 for net weight."
- q: Which agreement is used to calculate the transportation charges billed to you by your carrier?
  o: ["Forwarding agreement", "Freight agreement", "Internal agreement", "Customer agreement"]
  a: 1
  e: "S4TM3, Agreements Overview. Forwarding agreements calculate charges billable to your customer, freight agreements calculate charges billable to you by your carrier, and internal agreements calculate charges between organizations of the same company."
- q: To which objects in SAP S/4HANA are charge types, charge categories and charge subcategories mapped?
  o: ["SD sales order types and MM purchasing groups and plants", "SD output conditions and MM material master records and plants", "SD pricing condition types and MM service activities", "SD partner functions and MM vendor account groups"]
  a: 2
  e: "S4TM3, Charge Types. They are mapped to pricing condition types in SAP Sales and Distribution used for customer billing and to service activities in SAP Materials Management for carrier invoice processing."
- q: A calculation profile has the agreement determination type Minimum Charges. How does the system pick the agreement item?
  o: ["It finds the final amounts of all agreement items and takes the lowest", "It takes the item with the highest agreement priority", "It lists all agreements and asks the user to select one per charge item", "It takes the first agreement where the leading charge type can be calculated"]
  a: 0
  e: "S4TM3, Manual Agreement Selection: Example Scenarios. With Minimum Charges the system finds the final amounts for all agreement items and chooses the item with the minimum final amount; Determine All Agreements is the option that lets the user select."
- q: How many dimensions can a rate table maintain, and what does S4TM3 say about using them?
  o: ["Up to 3 dimensions, with further scales modeled as separate calculation sheets", "Up to 7 dimensions, all of which should always be used", "Up to 14 dimensions, all of which should be used for accuracy", "Up to 14 dimensions, though this is not recommended"]
  a: 3
  e: "S4TM3, Rate Tables. You can maintain up to 14 dimensions in a rate table, but this is not recommended; options such as a rate table determination rule reduce the number of dimensions."
- q: In exercise E05 the rates of rate table BASE_RATE_00 are raised by 10% for calendar year 2025 with Update Rates. What happens to the initial validity period?
  o: ["It is replaced by one period for 2025 that holds the new rates", "It is split into three periods, and only 2025 has new rates", "It is split into two periods with all later years using the new rates", "It stays unchanged and a separate rate table is created for 2025"]
  a: 1
  e: "E05, Work with Rate Tables. The initial validity period was divided into three periods (2021 to 2024 and from 2026 with the old rates, 2025 with the new rates); rates for destination country AT rose from 120 EUR and 60 EUR to 132 EUR and 66 EUR."
- q: In E05 the Handling Charge has the calculation resolution base PRODUCT. What does this mean in the freight order?
  o: ["The charge is calculated once for the whole freight order header", "The charge is calculated once for each stage of the freight order", "The charge line is applied once for each product", "The charge is calculated once for each container that is used"]
  a: 2
  e: "E05, Explain a Calculation Sheet. With the resolution base PRODUCT the charge line is applied multiple times in the freight order, once for each transported product."
- q: A calculation profile is assigned both to the purchasing organization and to the carrier business partner role. Which profile does the system apply?
  o: ["Only the one on the business partner role", "Only the profile assigned to the organizational unit", "Both profiles, with the higher charge being used", "Neither profile, so the freight order cannot be saved"]
  a: 0
  e: "S4TM3, Calculation Profile Assignment. If a profile is assigned to an organizational unit and to a business partner role, only the one assigned to the business partner role is applied; a profile cannot be assigned to a business partner alone."
```

---

## Session 10 — Settlement

### Knowledge items
- The four business requirements settlement covers (H09, Use): a freight settlement document created in TM for transportation services provided by a carrier and transferred to Materials Management (MM), where received invoices are verified against it; a forwarding settlement document that bills a customer and is transferred to Sales and Distribution (SD), which sends the invoice; an internal settlement document for a transportation service provided by an internal organization of the company; and an internal settlement document for the resources used in a freight order and provided by another internal organization.
- Settlement for shippers versus settlement for logistics service providers (LSPs): a shipper follows the freight settlement process with its carrier or LSP and can add cost distribution to allocate freight cost to each order or delivery item for financial accounting and controlling (H09, Settlement for Shippers). An LSP combines forwarding, freight and internal settlement documents (H09, Settlement for LSPs in an Ocean Freight Scenario).
- The three agreement types and who the parties are in the ocean freight example: forwarding agreements (export station and shipper, import station and ship-to party, export station and import station), freight agreements (each station or gateway with its carrier) and an internal agreement (gateway and export station) (H09, Agreements).
- Prepaid and collect agreement parties and Incoterms in the example: with FOB to Rotterdam the shipper pays the pre-carriage, the ship-to party pays main carriage and on-carriage, and the business unit closest to the external customer settles with that customer (H09, Incoterms).
- Internal settlement based on agreed internal rates or on actual carrier costs: the gateway pays its carrier USD 2000 and bills the export station USD 2200 on internal rates (USD 200 profit), or bills USD 2000 on actual costs (no profit) (H09, Internal Settlements).
- Consolidated shipment: the gateway sends an internal settlement document for the main-carriage cost to each internal export organization, based on agreed internal rates (standard agreed rate) or on the cost of execution; for cost-based settlement it uses cost distribution to determine each forwarding order's share of the freight booking cost (H09, Consolidated Shipment, Settlement Based on Agreed Rates, Settlement Based on Freight Costs).
- Internal settlement for resources: intercompany settlement (different company codes, posted to SD) versus intracompany settlement (same company code, posted to financial accounting, Intracompany Settlement checkbox on the Org. Data tab), and the prerequisites of an internal agreement with Resource specified and a freight order type enabled for internal settlements (H09, Internal settlement for resources).
- The forwarding settlement document (FWSD): posted to SD to request an invoice, created individually for one forwarding order (FWO) or collectively for several, with tabs General Data, Business Partner, Charges, Orders, Document Flow and Application Log (H09, Forwarding Settlement Document).
- FWSD life cycle statuses (In Process, Ready for Posting, Posted, Posting Started, Cancellation Requested, Canceled, Canceled by Credit Memo) and confirmation statuses (Not Yet Posted, Posting Successful, Posting Failed, Cancellation Successful, Cancellation Failed, Posting Started) (H09, Forwarding Settlement Document).
- The forwarding settlement process: create the FWSD, review it (invoice preview, deviating bill-to address), transfer with Save and Post, SD confirms billing document creation; cancellation can be requested at any time; failed posting is checked in the Application Log tab or, for external SD, in transaction SXI_MONITOR (H09, Forwarding Settlement).
- Manual changes and follow-up FWSDs: changes to payment terms, notes and attachments, charges, invoice date, service date, payer or a deviating bill-to address flag the document as manually changed; a follow-up FWSD proposes the charge amount minus amounts already invoiced and is Inconsistent if the result is zero or negative (H09, Forwarding Settlement).
- Execution-based settlement and the Settlement Basis field of an agreement item: by default TM settles per individual forwarding order; with a settlement basis (route-based, trailer-unit-based, or buyer's consolidation as a variant) the settlement item is the execution document, and its charges are calculated only in the forwarding settlement document (H09, Execution-Based Settlement).
- Buyer's consolidation settlement: the BCO setting in the Buyer's or Shipper's Consolidation field, a separate calculation sheet in the agreement item, one consolidated settlement for all forwarding orders in the container item, and a fallback to an agreement line with shipping type FCL (H09, Buyer's Consolidation Settlement).
- The freight settlement document (FSD): created for freight orders, freight bookings and service orders (or consignment orders); posting it to MM creates a purchase order for services and a service entry sheet (SES), books accruals, and is the basis for invoice verification or evaluated receipt settlement (ERS, self-billing) (H09, Freight Settlement Document; S4TM3, Freight Settlement Processing).
- The freight settlement process steps: create the FSD (individual, collective, or mass creation with /SCMTMS/SFIR_CREATE_BATCH), review it until it is Consistent and Ready for Accruals, then post it to MM; the settlement date defaults to today's date and the posting runs asynchronously (H09, Freight Settlement; E05, Create and Post a Freight Settlement Document and Verify the Invoice).
- FSD life cycle and confirmation statuses (In Process, Ready for Accruals, Posting Started, Posted, Invoice Verified, Cancellation Requested, Canceled, Reversal Requested, Reversed, Credit Memo Created; Not Posted, Not Confirmed, Confirmed, Posting Failed and the specific failure statuses) (H09, Freight Settlement Document).
- Prerequisites for freight settlement: FSD types and number range intervals, and a freight settlement profile assigned to the business partner (carrier role) and purchasing organization; the procuring company code books the accruals and the plant is needed for the service purchase order (H09, Freight Settlement; Company Code and Plant in Posting Freight Settlements; S48600, Freight Settlement Document Creation - Configuration).
- Reversing an FSD and changes after posting: reversal is only possible in life cycle status Invoice Verified and ends with a credit memo through transaction MRRL; added or changed charges lead to Partially Invoiced (new FSD) or Over Invoiced (credit memo or reverse and repost) (H09, Reversing a Freight Settlement Document, Changes After You Post Accruals; S48600, Freight Settlement - Updates).
- Cost distribution for shippers: freight cost is distributed to the order or delivery item level when the FSD is created and posted; MM gets one purchase order and SES for the net amount while a settlement management document carries the distributed amounts (H09, Cost Distribution for Shippers; E05, Distribute Freight Costs and Bill Transportation Charges to Customers).
- Cost distribution configuration: enabled in the document type, distribution profiles assigned through the charges profile, methods Direct and Hierarchical, rule basis Gross Weight, Gross Volume, Net Weight or Distance times Weight, and viewing of posted data with WLFLTM2 (S48600, Cost Distribution).
- Billing freight costs to customers: distributed costs per delivery item can be added to the SD billing document, which needs SD integrated with TM, one freight order for the delivery and one currency (S48600, Billing Freight Costs; E05).
- Self-billing (ERS) versus invoice submission by the carrier, the automatic dispute case created for a carrier invoice that differs from the freight order, and the conditions for posting carrier invoices to MM (H09, Dispute Management for Freight Settlements; S48600, Dispute Management for Freight Settlement).

### Skill items (tier: inferred)
- Choose which settlement document (forwarding, freight or internal) a described business situation needs, and name the system it is posted to.
- Read the life cycle and confirmation status of a forwarding or freight settlement document and say what the next step or the likely problem is.
- Decide, for a given scenario, whether settlement should follow individual forwarding orders or an execution document through the Settlement Basis field.
- Trace the documents created in MM and SD from a settlement document using its Document Flow tab.
- Describe how a late change to freight charges after accruals reaches MM.

### Important questions
- Which settlement document is created in each direction of a transportation business (towards the customer, towards the carrier, between internal organizations), and into which module is each posted?
- Why does TM create a purchase order and a service entry sheet when a freight settlement document is posted, and what does that make possible for the carrier invoice?
- When is it better to settle an internal organization on agreed internal rates, and when on actual freight cost?
- What changes in the settlement document when the settlement basis is a trailer unit, a route or a buyer's consolidation instead of the individual forwarding order?
- What can still be changed after accruals are posted, and what must happen instead when the amount becomes too high?
- How does cost distribution link the freight order to the delivery items, and where do the distributed amounts end up?
- How do self-billing and invoice submission differ, and what does the dispute case do for the shipper?

### Deliverable (tier: inferred)
A one-page settlement map for a shipper and an LSP in the learner's own words: for each settlement document (forwarding, freight, internal) list who creates it, what it is based on, which module it is posted to, and the statuses that show it is finished, plus one worked example of a freight order with cost distribution (such as the USD 1000 split into USD 700 and USD 300).

### Self-confidence question (tier: inferred)
Can I explain to a finance controller, without notes, how a freight order becomes a freight settlement document, accruals and a verified carrier invoice, and when a forwarding or internal settlement document is used instead?

### Quiz questions
```yaml
- q: Which TM document is posted to SD so that an invoice is sent to a customer for transportation services?
  o: ["Freight settlement document", "Forwarding settlement document", "Settlement management document", "Service entry sheet document"]
  a: 1
  e: "H09, Forwarding Settlement Document, defines the FWSD as a document posted to SD to request the creation of an invoice for a customer. The freight settlement document goes to MM instead."
- q: What does the system create in MM when a freight settlement document is posted?
  o: ["A billing document and a customer invoice", "A carrier invoice and a dispute case item", "A sales order and an outbound delivery", "A purchase order and a service entry sheet"]
  a: 3
  e: "H09, Freight Settlement Document, states that on posting, a purchase order for services and a service entry sheet are created with the values of the TM charge lines. They are the basis for invoice verification."
- q: In which life cycle status can a freight settlement document be reversed?
  o: ["Invoice Verified", "Posted", "Ready for Accruals", "Posting Started"]
  a: 0
  e: "H09, Reversing a Freight Settlement Document, says you can only reverse the document when it has the life cycle status Invoice Verified."
- q: A freight order with two deliveries has a net amount of USD 1000 and a cost distribution of USD 700 and USD 300. What amount does the purchase order created on posting carry?
  o: ["USD 700", "USD 300", "USD 1000", "USD 1700"]
  a: 2
  e: "H09, Cost Distribution for Shippers, shows that posting creates a purchase order and a service entry sheet for USD 1000, while the settlement management document carries USD 700 and USD 300 as item amounts."
- q: Which cost distribution method suits a resolution base that includes containers or rail cars?
  o: ["Direct", "Hierarchical", "Proportional", "Cascading"]
  a: 1
  e: "S48600, Cost Distribution, says the Hierarchical method is used when the resolution base includes containers or rail cars, so charges are distributed to the container level first and then to the line item level."
- q: An LSP delivers 7 forwarding orders on one trailer unit and leaves the Settlement Basis field empty in the agreement item. How does TM settle them?
  o: ["With one rate for the whole journey of the truck", "With one rate for the container item of a booking", "With one rate for each execution stage", "With a rate for each forwarding order"]
  a: 3
  e: "H09, Execution-Based Settlement, says that without Trailer Unit in the Settlement Basis field the system rates and settles each of the 7 forwarding orders individually."
- q: For a buyer's consolidation, what does the system try if it finds no agreement line item with the BCO setting?
  o: ["A line with shipping type FCL", "A line with shipping type LCL", "A line with a trailer unit settlement basis", "A line with a route-based settlement basis"]
  a: 0
  e: "H09, Buyer's Consolidation Settlement, Settlement Fallback, says the system looks for an agreement line with a shipping type of FCL (full container load) when no BCO line exists."
- q: A gateway receives a carrier invoice of USD 2000 and bills the export station USD 2200 based on internal rates. What is the gateway's result?
  o: ["A loss of USD 200", "A loss of USD 2200", "A profit of USD 200", "A profit of USD 2200"]
  a: 2
  e: "H09, Internal Settlements, states that CFS-RTM receives an invoice for USD 2000 but charges STA-NEU USD 2200 on internal rates, so it makes USD 200 profit. Settlement on actual costs would give no profit."
- q: SD is on an external system and posting of an FWSD fails. Where do you check the error logs of the enterprise service message?
  o: ["Transaction MIRO", "Transaction /SCMTMS/SFIR_CREATE", "Transaction SXI_MONITOR", "Transaction WLFLTM2"]
  a: 2
  e: "H09, Forwarding Settlement, process step 4, says that with SD on an external S/4HANA or SAP ERP system you check the error logs for the enterprise service message in transaction SXI_MONITOR."
- q: Which condition must be met before the Posting of Carrier Invoices function sends a carrier invoice to MM?
  o: ["The carrier invoice has the lifecycle status Rejected", "The freight orders have the invoicing status Not Invoiced", "The carrier invoice has the consistency status Inconsistent", "Any existing dispute case has the lifecycle status Resolved"]
  a: 3
  e: "S48600, Dispute Management for Freight Settlement, lists the conditions: no dispute case exists or it is Resolved, the invoice is not Rejected, the freight orders are Completely Invoiced, the invoice is Not Blocked and Consistent."
```

---

## Session 11 — Warehouse and Trade Integration (EWM, Advanced Shipping and Receiving, GTS)

### Knowledge items
- The integration landscape of TM: logistics integration of orders and deliveries, integration with settlement, Advanced Shipping and Receiving, Extended Warehouse Management (EWM), SAP Event Management (SAP EM) and SAP Global Trade Services (SAP GTS); Document Information Extraction extracts data from delivery documents attached to a consignment order (H11, Integration; H01, Integration).
- Advanced Shipping and Receiving (Advanced SR) is an integrated end-to-end process to send, receive and transport products, covering mixed and multi-warehouse scenarios in one freight order and the steps from the truck's arrival at the gate to the final goods receipt; it is also supported for rail freight orders (H11, Advanced Shipping and Receiving).
- Advanced SR connects TM, EWM, Stock Room Management (STRM), MM-IM and Logistics Execution (LE) through a harmonized data model, the EDIFACT standard for EDI messages and dedicated apps; MM and SD are needed to create transportation requirements (H11, Advanced Shipping and Receiving).
- The warehouse management applications that can be integrated in the same system: Lean Warehouse Management (inventory at storage location level, needs a placeholder warehouse), Stock Room Management (small or low-complexity warehouses) and EWM; a freight order can contain EWM-managed and IM-managed storage locations (H11, Storage Location).
- Integration based on the freight order does not use the EWM transportation unit (TU) or the EWM vehicle; it can run in parallel with integration based on the EWM TU, and warehouse-driven outbound processes start in EWM (H11, Integration Based on Freight Order).
- Consignment orders group transportation requirements by criteria such as source and destination location, delivery date and time and business partner; they can be created from inbound messages or manually, serve as the basis of communication between partners, support subcontracting, charge calculation, settlement and tracking but not tendering, and can be assigned to only one freight order at a time (H11, Consignment Orders; Consignment Order).
- Decentralized EWM and TM: transportation logistics based solely on an outbound delivery from a sales order, embedded in S/4HANA, with the outbound delivery process either transport-driven or warehouse-driven; only the outbound process is supported, inbound features and Dangerous Goods integration are not, and SAP GTS can be integrated (H11, Advanced SR for Decentralized EWM and TM).
- Prerequisites and master data: the source or destination location (location type 1003, shipping point) must be flagged relevant for Advanced SR, a location of type 1200 (loading point) must be defined, STRM or Lean WM doors must be assigned to EWM doors or loading points when doors are shared (not needed for EWM-only scenarios), and Customizing is done under Integration (H11, Prerequisites for Advanced Shipping and Receiving).
- Detailed organization of loading and unloading: a loading point or unloading point is a location in the master data that represents a group of doors; the app Assign STRM Doors to EWM Doors or Loading Points replaces an STRM or Lean WM door with the assigned EWM door, with the stated restrictions (H11, Assignment of STRM Doors to EWM Doors or Loading Points).
- The end-to-end process between customer and supplier: scheduling agreement and schedule lines create freight units, a release sends a call off by IDoc, the supplier creates outbound deliveries and warehouse activities, plans a road freight order and consignment orders, checks the truck in, loads, posts goods movement and sends an advanced shipping notification (ASN); the customer's system creates a consignment order from the ASN and blocked inbound deliveries that are unblocked when the warehouse processing status is set to Ready for Warehouse Processing (H11, End-to-End Process (E2E) for Advanced Shipping and Receiving).
- Transport-driven versus warehouse-driven outbound process in decentralized EWM and TM: in the transport-driven process the outbound delivery order is blocked until planning is complete and is released when the freight order status changes from In Process to Ready for Warehouse Processing; in the warehouse-driven process warehouse activities come first and the status is set to Ready for Shipping in the EWM outbound delivery order after planning (H11, Decentralized EWM and TM Outbound Process and Integration).
- Warehouse loading stops and warehouse unloading stops: detailed stops with warehouse number, loading or unloading point and warehouse door, derived from predecessor documents or created manually, shown on the Overview tab and in the transportation cockpit, with items packed into different mixed packages when their warehouse number or point differs (H11, Delivering Goods to Several Warehouses Within a Location).
- Status management in Advanced SR: Warehouse Door Status (Arrived at Door, Departed from Door) and Warehouse Processing Status (Not Determined, Not Started, Ready for Warehouse Processing, In Process, Completed), whose meaning differs between inbound and outbound (H11, Explanation of Statuses).
- The integrated warehouse and transportation execution steps in the Fiori exercise: Set to Ready for Warehouse Processing, create and confirm warehouse tasks, Set to Ready for Shipping, assign a door in the Load or Unload Freight Orders app, Set to Arrived at Door, Set Items to Loaded, Set Stop to Loading Completed, post goods movement, Set to Departed from Door (E04, Execute an Integrated Warehouse and Transportation Process).
- Delivery split: TM can split deliveries across Lean WM, STRM and EWM by creating a new delivery with the relevant freight units; it is not possible while warehouse activities run, and at loading, handling units not loaded get a new freight unit and delivery when the stop is set to Loading Completed (H11, Delivery Split).
- Delivery deletion in TM: available for LE deliveries in an embedded setup when freight units are delivery-based and unplanned, with 2-step stock transport orders, side-by-side setups and EWM delivery orders excluded (H11, Delivery Deletion).
- Late changes to capacity documents: items loaded or unloaded but not assigned can be added to the same warehouse stop even after departure; later additions create a document error, and unassignment after check-out requires the stop status Not Loaded and cancelled goods movement, export declaration and customs invoice (H11, Late Changes to Capacity Documents).
- SAP Event Management integration: tracking of freight units, freight orders, freight bookings, transportation units, resources and instructions; expected events (Scheduled, Loading Begin, Loading End, Departure, Arrival at Destination, Unloading Begin, Unloading End) can be reported from either side, and unexpected events (Delay, Damage) raise alerts in TM (H11, Integration with SAP Event Management; Tracking of Freight Units).
- SAP GTS integration: compliance checks (embargo, sanction party lists, legal control) and export declarations; the outbound customs activity is based on a consignment or freight order, the inbound one on the freight order; the legal split indicator groups items into freight units and deliveries, and a non-compliant freight unit blocks the delivery for warehouse execution (H11, GTS Integration in Advanced Shipping and Receiving; SAP GTS Integration for the Outbound Process).

### Skill items (tier: inferred)
- Tell which of the integration options (EWM, Advanced SR, decentralized EWM and TM, Event Management, GTS) a described warehouse or customs requirement points to.
- Place the warehouse processing status values on a simple inbound or outbound timeline and say which side holds responsibility for the cargo at each point.
- Distinguish a transport-driven from a warehouse-driven outbound flow by naming its first step and what releases the delivery.
- Follow the Fiori steps of the integrated warehouse and transportation exercise and say what each status change reports.
- Name the master data needed before a location can be used in Advanced SR.

### Important questions
- Why does Advanced SR work on the freight order rather than on the EWM transportation unit, and when can both integrations run side by side?
- What changes between a transport-driven and a warehouse-driven outbound process, and who releases the delivery in each?
- Why are warehouse loading and unloading stops needed when one truck serves several warehouses at the same location?
- How does the warehouse processing status control the hand-over of cargo between TM and the warehouse in the inbound and outbound direction?
- What happens to the delivery and the freight unit when a truck cannot take all handling units of a delivery?
- Which documents does a customs check in SAP GTS block, and where in the process does it block them?
- What does the shipper gain by connecting SAP Event Management, and which events come back to TM as alerts?

### Deliverable (tier: inferred)
An annotated swimlane (as a table or a drawing) of one outbound delivery from sales order to truck departure, showing the TM, EWM and SAP GTS steps in order, the status that changes at each step, and whether the flow shown is transport-driven or warehouse-driven.

### Self-confidence question (tier: inferred)
Can I explain to a warehouse manager, without notes, how a truck moves through Advanced Shipping and Receiving from gate check-in to goods movement, and how TM, the warehouse and SAP GTS hand over to each other?

### Quiz questions
```yaml
- q: Integration based on the freight order in Advanced Shipping and Receiving does not use which EWM objects?
  o: ["The EWM warehouse task and handling unit", "The EWM door and loading point", "The EWM transportation unit and vehicle", "The EWM delivery order and wave"]
  a: 2
  e: "H11, Integration Based on Freight Order, states that the process is based on the freight order and does not use the EWM transportation unit (TU) or the EWM vehicle."
- q: What must you create when you use Lean Warehouse Management in Advanced Shipping and Receiving?
  o: ["A placeholder warehouse", "An EWM transportation unit", "A separate freight booking", "An additional shipping point"]
  a: 0
  e: "H11, Lean Warehouse Management, says you need to create a place holder warehouse that ensures the document flow in TM."
- q: Which function can not be performed based on a consignment order?
  o: ["Subcontracting", "Charge calculation", "Shipment tracking", "Tendering"]
  a: 3
  e: "H11, Consignment Order, Use, says you can perform subcontracting, charge calculation, settlement with the carrier and shipment tracking, but it is not possible to perform tendering based on a consignment order."
- q: Which Advanced Shipping and Receiving processes are enabled in a decentralized EWM and TM deployment?
  o: ["Only the inbound process", "Only the outbound process", "Both inbound and outbound", "Only returns processes"]
  a: 1
  e: "H11, Advanced SR for Decentralized EWM and TM, states that it enables the outbound process and that inbound features in Advanced Shipping and Receiving are not supported."
- q: Which location type represents a loading point in the master data prerequisites for Advanced Shipping and Receiving?
  o: ["Location type 1200", "Location type 1003", "Location type 1100", "Location type 1300"]
  a: 0
  e: "H11, Prerequisites for Advanced Shipping and Receiving, says you must define a location with location type 1200 (loading point). Location type 1003 is the shipping point flagged as relevant."
- q: In a transport-driven outbound process with decentralized EWM and TM, what releases the blocked outbound delivery order for warehouse activities?
  o: ["Posting the goods issue for the delivery in the warehouse", "Setting the EWM outbound delivery order to Ready for Shipping", "Setting the freight order to Ready for Warehouse Processing", "Reporting the truck's arrival and check-in at the gate door"]
  a: 2
  e: "H11, Transport-Driven Process, explains that the delivery order is blocked until planning is complete, and that the status change of the freight order from In Process to Ready for Warehouse Processing releases it."
- q: To set a warehouse door to Arrived at Door, which handling execution status must the warehouse stop have?
  o: ["Checked Out", "Checked In", "Loaded", "Departed"]
  a: 1
  e: "H11, Explanation of Statuses, Warehouse Door Status, says Arrived at Door can only be set if the door is not occupied and the handling execution status of the stop is Checked In."
- q: When is a delivery split possible again after warehouse activities have started?
  o: ["When picking has started in EWM", "When the Warehouse Processing Status is In Process", "When the truck has checked in at the gate", "When the Warehouse Processing Status is Completed"]
  a: 3
  e: "H11, Delivery Split, says that during warehouse activities a split is not possible, and that after all activities are completed and the Warehouse Processing Status is Completed a split is possible again."
- q: Which unexpected events can SAP Event Management track for freight units and report to TM as alerts?
  o: ["Loading begin and loading end", "Departure and arrival at destination", "Delay and damage", "Unloading begin and unloading end"]
  a: 2
  e: "H11, Tracking of Freight Units, lists Scheduled, Loading Begin, Loading End, Departure, Arrival at Destination, Unloading Begin and Unloading End as expected events, and Delay and Damage as unexpected events that send an alert to TM."
- q: In the Advanced Shipping and Receiving inbound process, on which document is the customs activity with SAP GTS based?
  o: ["The freight order", "The consignment order", "The forwarding order", "The scheduling agreement"]
  a: 0
  e: "H11, GTS Integration in Advanced Shipping and Receiving, says that in the outbound process customs activity is based on either the consignment or the freight order, and in the inbound process on the freight order."
```

---

## Session 12 — Dangerous Goods and Basic Functions

### Knowledge items
- Purpose of the dangerous goods (DG) functions in TM: to transport dangerous goods in compliance with international regulations (H12, Considering Dangerous Goods). Dangerous goods are solids, liquids or gases that pose risks to people, living organisms, property or the environment, and the chemical safety laws governing them vary between countries (S48600, Dangerous Goods).
- Two DG processing options, Dangerous Goods Processing Based on PS&S and Dangerous Goods Processing Based on Product Compliance; they are mutually exclusive, so only one can be activated at a time (H12, Considering Dangerous Goods; S48600, Dangerous Goods).
- DG data that the checks rely on: dangerous goods master data (created by shippers for products classified as DG, displayed with the Display Dangerous Goods Data app) and document-based dangerous goods records (created by logistics service providers at item level in the business document) (H12, Dangerous Goods Processing Based on PS&S).
- Dangerous Goods Indicator Profile: defined in SAP EHS Management, assigned to the material in the master data, selectable when the material is relevant for dangerous goods; the examples listed are Environmentally Relevant and Highly Viscous and In Bulk/Liquids. Indicator profiles are specified in Customizing under Specify Indicator Profiles for the Material Master (S48600, Dangerous Goods Indicator Profile; H12, Configuration of Dangerous Goods Processing).
- Configuration of DG processing (PS&S): environment parameters for PS&S Services, phrase management and a text pattern in the DG master, a DG profile that activates the DG checks (and is also required to enter DG data without checks), assignment of the DG profile to forwarding order, forwarding quotation, freight unit, freight order and freight booking types, the transportation mode, the block reason Error During Dangerous Goods Check, and the methods FUB_DG and VSR_DG assigned to the process controller strategy (H12, Configuration of Dangerous Goods Processing).
- Adapting DG processing: create a function module, specify it as a DG check method, assign the method to a check schema; BAdIs can change the input data for checks and printing or read template data from an external database (H12, Adapting DG Processing).
- Dangerous goods checks process: the check runs for forwarding orders, forwarding quotations, freight orders and freight bookings, on save or manually; it is repeated during freight unit building (for example the mixed loading check), on the freight units, during VSR planning (transportation proposal, freight unit vehicle check) and on the resulting freight document. Errors block the document or FU with the block reason Error During Dangerous Goods Check; messages are in the application log (object /SCMTMS/TMS, subobject DG) (H12, Dangerous Goods Checks).
- ADR 1.1.3.6 points check: exemption if the points total does not exceed 1000 points; check method /SCMTMS/DG_ADR_1000_POINTS; Points = Relevant Quantity x Multiplication Factor; the relevant quantity depends on the aggregate state (master data uses item-level gross weight, net weight or gross volume; DG records use gross weight, net weight or nominal volume of receptacle); points are summed per document item, header and stage, with FWO, FWQ, OTR and FU as the sum of items and the road freight order as the maximum of the stages (H12, ADR 1.1.3.6 Points Check Calculation).
- Transport restrictions Prohibited (not eligible under ADR 1.1.3.6) and Unlimited (not considered in the points calculation); if either flag is set, no points are calculated (H12, Transport Restrictions).
- Points check in planning: the ADR points check is activated in the freight unit building rule; the VSR optimizer uses vehicle resources with dimensions flagged as relevant for the ADR points check, and the check can be deactivated in the planning profile or in the transportation cockpit (H12, VSR Optimization).
- Document-based dangerous goods records: entered manually on the Dangerous Goods tab page at item level or created automatically from a business partner's data; records from forwarding orders are copied to the freight documents as read-only; item check method /SCMTMS/DG_CHECK_WITH_CONTENT; they can be saved as released or unreleased templates and searched by DG Number Type, DG Number, Packing Group and Variant ID (H12, Document-Based Dangerous Goods Records; Creation and Editing of Document-Based Dangerous Goods Records; Creation and Use of Dangerous Goods Templates).
- UI profiles for document-based DG data: fields organized in UI groups, assigned to regulations (one tab page per regulation), field properties (separate editing per regulation, checkbox, table view, corresponding field, custom label, consistency check), phrase sets; defined in the Edit UI-Profile for Dangerous Goods app; a profile in use cannot be changed but can be copied; DG_INBOUND_PROFILE and Generate Inbound Profile support automatic record creation (H12, Definition of UI Profiles for Document-Based DG Data).
- Phrase management and Loading Dangerous Goods Content: phrases are maintained with the Manage Phrases app; the Dangerous Goods Content Loader loads purchased content (regulations, phrases, Customizing data) in steps, phrases before regulations, and generates DG master data records whose product number contains the UN number (for example UN-1993-III-0101) (H12, Loading Dangerous Goods Content).
- Dangerous goods documents: the shipper's declaration (IATA, generated for a freight booking from the DG master, viewable in the Output Management tab) and the standard print forms ADR Dangerous Goods Note, RID Dangerous Goods Note and IMO Dangerous Goods Declaration (H12, Shipper's Declaration; Standard Print Forms).
- DG processing based on Product Compliance: covers road, rail, air and ocean freight; activated in Customizing under Activate Product Compliance and Activate Business Features for Product Compliance; the DG statuses of freight orders, freight units and freight bookings can be viewed; FUB_DG and VSR_DG are also assigned (H12, Dangerous Goods Processing Based on Product Compliance).

### Skill items (tier: inferred)
- Trace, for a forwarding order with a dangerous goods item, where in the process chain the DG check runs and what blocks if it fails.
- Work out the number of freight units the ADR 1.1.3.6 points limit produces for a given set of items and points.
- List the Customizing prerequisites needed before DG checks work for one business document type.
- Decide whether a shipper or a logistics service provider needs master data or document-based records, and name the supporting setup (UI profile, templates).

### Important questions
- Why can only one of the two DG processing options (PS&S or Product Compliance) be active at a time, and what does each option rest on?
- Where in the TM process chain is the DG check repeated, and what makes it behave differently during freight unit building and VSR planning?
- How does the points formula behave for a road freight order compared with a freight unit, and why?
- What must be configured so that a user can enter a document-based dangerous goods record, and what limits the consistency check?
- Which settings tie a DG profile and a UI profile to a document type?

### Deliverable (tier: inferred)
A one-page DG checklist for a given business document type that lists the Customizing prerequisites (DG profile, block reason, FUB_DG and VSR_DG methods, UI profile or master data), the checks the document goes through along the process chain, and the points-check settings if the ADR 1.1.3.6 exemption is used.

### Self-confidence question (tier: inferred)
Can I explain how TM checks dangerous goods along the process chain, from the forwarding order to the freight document, to a transportation planner without notes?

### Quiz questions
```yaml
- q: How do the two dangerous goods processing options in TM relate to each other
  o: ["They can run side by side in the same client", "They apply to different transportation modes", "They are mutually exclusive, only one is active", "They are chosen separately per business document"]
  a: 2
  e: "S48600, Dangerous Goods, states that DG processing based on PS&S and DG processing based on product compliance are mutually exclusive, so only one can be activated at a time."
- q: Who creates document-based dangerous goods records in the PS&S-based processing
  o: ["Logistics service providers, at item level", "Shippers, as part of the product master data", "The system itself, from regulatory content only", "Carriers, once they accept the freight order"]
  a: 0
  e: "H12, Dangerous Goods Processing Based on PS&S: when an LSP receives DG data from a shipper, it enters the data by creating a document-based dangerous goods record at item level. Shippers create the DG master data."
- q: What must you still do if you want to enter DG data in a business document without performing any DG checks
  o: ["Activate the points check in the FU building rule", "Assign the methods FUB_DG and VSR_DG to a strategy", "Load SAP EHS Regulatory Content into TM first", "Assign a DG profile to the business document type"]
  a: 3
  e: "H12, Configuration of Dangerous Goods Processing: even without DG checks, a DG profile still has to be assigned to the business document type."
- q: Which methods are assigned to the process controller strategy to use DG checks during FU building and VSR optimization
  o: ["DG_ADR and DG_VSR", "FUB_DG and VSR_DG", "FU_CHECK and VSR_CHECK", "FUB_PS and VSR_PS"]
  a: 1
  e: "H12, Configuration of Dangerous Goods Processing: to use the DG checks during FU building and VSR optimization you assign the methods FUB_DG and VSR_DG to the relevant process controller strategy."
- q: A limit of 1000 points per freight unit is set and three items with 500 points each are to be transported. How many freight units does the system generate
  o: ["One freight unit holding all three items", "Three freight units, one per item", "Two freight units", "No freight unit, the items are blocked"]
  a: 2
  e: "H12, ADR 1.1.3.6 Points Check Calculation: with a limit of 1000 points per freight unit and three items of 500 points each, the system generates two freight units."
- q: How are points calculated for a road freight order under the ADR 1.1.3.6 points check
  o: ["As the maximum of the points of each stage", "As the sum of the points of all assigned items", "As the average of the points of each stage", "As the points of the first stage only"]
  a: 0
  e: "H12, ADR 1.1.3.6 Points Check Calculation: for the road freight order the points are the maximum of the points of each stage, whereas FWO, FWQ, OTR and FU use the sum of the assigned items."
- q: What happens to a UI profile for document-based DG data that is already in use
  o: ["It can be changed after a new release", "It is deleted once the document is saved", "It switches over to the inbound profile", "It cannot be changed, but can be copied"]
  a: 3
  e: "H12, Definition of UI Profiles for Document-Based DG Data: a profile in use cannot be changed, but you can create a new profile by copying an existing one."
- q: In which order does the Dangerous Goods Content Loader recommend loading data
  o: ["Regulations first, then the phrases", "Phrases first, then the regulations", "Customizing data first, then the phrases", "Both together in a single step"]
  a: 1
  e: "H12, Loading Dangerous Goods Content: it is recommended to load the phrases before loading the regulations."
- q: What does the Prohibited or Unlimited transport restriction flag mean for the points calculation
  o: ["Points are doubled for the product", "Points are taken from the item gross weight", "No points are calculated for the product", "Points are calculated at header level only"]
  a: 2
  e: "H12, Transport Restrictions: Prohibited means not eligible under ADR 1.1.3.6 and Unlimited means not considered in the points calculation; if either flag is set, no points for the product are calculated."
- q: Where can a user view the IATA shipper's declaration for dangerous goods that the system generates from a freight booking
  o: ["In the Output Management tab of the freight order", "In the Statuses tab of the forwarding order item", "In the Dangerous Goods tab of the freight unit item", "In the application log with the subobject DG"]
  a: 0
  e: "H12, Shipper's Declaration: the system generates the declaration from the DG master based on the freight booking and you can view it in the Output Management tab of the freight order."
```

---

## Session 13 — Analytics

### Knowledge items
- TM analytics overview pages (OVP): apps on the Fiori launchpad that show KPIs for operational business; each page covers one area of TM (for example freight booking, freight ordering, tendering, business share); made of cards that are read-only, show data in real time, can be resized and reordered (H13, Analytics Overview Pages; S48600, Analytics and Collaboration).
- Detailed views: reached by selecting a card header (unfiltered) or a chart data point (filtered); they combine donut, bar and line charts with a table, are read-only, and let you navigate to the document (for example freight order or freight booking) to change it; some overview pages have two detailed views (H13, Analytics Overview Pages; Detailed Views).
- CDS views: query views (SQL queries on the database) that feed each overview page; top-level consumption views containing other contributing CDS views, made of key figures and attributes; appropriate authorization objects are needed; the OData service of each Fiori ID must be activated in the Gateway system (H13, CDS Views; S4TM3, Determination of Procurement Needs).
- Mapping of overview pages to CDS views: Allocation Analysis and Business Share Analysis to C_TranspAllocComplianceQ and C_BusinessShareComplianceQ, Cost Analysis to C_FreightSettlementCostQ and C_TranspOrdInvcgBlockStsQ, Freight Booking and Freight Order monitoring and quantity pages to their Execution, Execution Status and Quantity queries, Tendering Analysis to C_TenderingQuery (H13, Summary table).
- Delivered time filters: all CDS views behind the OVPs and analytical list pages contain the current and previous month on a two-month rolling basis; they can be changed with metadata extensions (SAP Note 2779334) (H13, Metadata Extensions to Replace Delivered Time Filters).
- Allocation Analysis (Fiori ID F2673; detailed view F2745): KPIs for weight, volume and amounts of the transportation allocation including net, gross, minimum and maximum values and total and average utilization; cards such as Trade Lane Weight, Volume and Container Load Analysis, Transportation Mode Category Analysis, Overall Weight and Container Utilization Distribution; Change Transportation Allocation opens the allocation in edit mode (H13, Allocation Analysis; Transportation Allocation Detailed View).
- Business Share Analysis (F2674): current amount and target quantity per carrier, ratio and business share per month; Weight Fulfillment Ratio, Volume Fulfillment Ratio, Trade Lane Fulfillment, Road, Sea and Air Fulfillment Distribution compare actual booked carrier quantity with target quantity (H13, Business Share Analysis).
- Cost Analysis (F2672): two data sources, C_FreightSettlementCostQ for cost cards (Cost Distribution, Carrier Cost Analysis, Charge Type Analysis, Purchasing Organization Cost Analysis and others) and C_TranspOrdInvcgBlockStsQ for Invoicing Block Analysis; the Invoicing Block Analysis card opens the Transportation Invoice Blocked Detailed View, any other card the Transportation Costs Detailed View (H13, Cost Analysis).
- Freight Order Execution Monitoring (F2675) and Freight Booking Execution Monitoring: Life Cycle Status Analysis, Execution Block and Planning Block Analysis, Delayed Freight Orders in Transit, Blocking and Non-Blocking Discrepancies, Carrier, Location and Activity On Time Performance, Unexpected Events; a freight order is on time if all its events are classed as on time, and the on time cards use time-relevant events with expected and actual date and time and event status Reported (H13, Freight Order Execution Monitoring).
- Freight Order Quantity Analysis (F2676) and Freight Booking Quantity Analysis: gross weight, gross volume and quantity distribution by week for completed freight orders, carrier, shipper and ship-to party quantity analysis, Utilization Distribution, Distance Analysis (H13, Freight Order Quantity Analysis).
- Tendering Analysis (F2679): Open Requests, Overdue Requests, Acceptance Analysis, Tendering Peer-to-Peer Cycle Analysis, Tendering Cycle Time Analysis, Tendering Ratio, Original Carrier Changed (comparison of awarded business against the carrier the system proposed) (H13, Tendering Analysis).
- Main input parameters: P_Language, P_TodayDate (system date; data from the beginning of the previous month up to the system date), P_DisplayTimeUnit, P_DisplayWeightUnit, P_DisplayVolumeUnit, P_DisplayQuantityUnit, P_DisplayLengthUnit, P_DisplayCurrency; the unit and currency parameters are mandatory; Allocation Analysis adds P_TrAlcMinToleranceInPercent and P_TrAlcMaxToleranceInPercent (H13, Main Input Parameters of each view).
- Analytics in the wider TM processes: overview pages can be tailored to business roles and supervisors of execution can start at the freight order execution overview (S48600, Analytics and Collaboration); analytics can analyze historic transportation volumes to determine procurement needs, but their use is not mandatory for the strategic freight procurement process (S4TM3, Determination of Procurement Needs).

### Skill items (tier: inferred)
- Pick the overview page that answers a given management question (cost, carrier performance, allocation fulfillment, tendering behavior).
- Trace an overview page card to its detailed view and to the CDS view and OData service that feed it.
- Read a fulfillment ratio or an on time performance figure and say what it measures and which period it covers.

### Important questions
- Which overview page would a transportation manager open to see why freight orders are blocked for invoicing, and where does the card lead?
- What is the difference between selecting a card header and selecting a chart data point?
- What must be in place technically (CDS view, OData service, authorization) before an overview page works?
- How is a carrier's on time performance defined, and which events does it use?
- Why are the cards read-only, and how does the user act on what a detailed view shows?

### Deliverable (tier: inferred)
A one-page analytics map that lists each TM overview page with its Fiori ID, the CDS views behind it, its detailed views, and one business question it answers.

### Self-confidence question (tier: inferred)
Can I explain which TM overview page and detailed view answers a given KPI question, and what feeds it technically, to a transportation manager without notes?

### Quiz questions
```yaml
- q: What can a user do on the cards of a TM analytics overview page
  o: ["Enter data directly into the cards", "Only view the data, the cards are read-only", "Run queries and searches on the card data", "Edit the underlying documents inside the card"]
  a: 1
  e: "H13, Analytics Overview Pages: the cards are read-only; you can't enter any information or perform queries or searches on them."
- q: What happens when you select a data point in a chart card of an overview page
  o: ["The overview page reloads with the previous month data", "The system opens the related document in edit mode now", "The card is removed from the overview page", "A detailed view opens, filtered to that data point"]
  a: 3
  e: "H13, Analytics Overview Pages: selecting the header takes you to a detailed view with all the unfiltered data, while selecting a data point takes you to a detailed view filtered to the information relevant to that data point."
- q: What kind of object is the CDS view that feeds an overview page
  o: ["A top-level consumption view over other CDS views", "A Customizing table that stores the card layout", "A BRFplus rule that selects the cards to display", "An enterprise service that sends events to the page"]
  a: 0
  e: "H13, CDS Views: the views feeding each overview page are top-level views called consumption views that contain other contributing CDS views and consist of key figures and attributes."
- q: How do the delivered time filters of the TM analytics CDS views work?
  o: ["They cover the current year on a rolling basis for all users", "They are fixed by SAP and cannot be changed by customers at all", "They cover two months and can be changed with metadata extensions", "They are set per user in the launchpad settings of each role"]
  a: 2
  e: "H13, Metadata Extensions to Replace Delivered Time Filters: the time filters contain the current and previous month on a two-month rolling basis and can be changed by using metadata extensions (SAP Note 2779334)."
- q: Which detailed view does the Invoicing Block Analysis card of the Cost Analysis overview page open
  o: ["Transportation Costs Detailed View", "Transportation Invoice Blocked Detailed View", "Freight Order Execution Status Detailed View", "Business Share Detailed View"]
  a: 1
  e: "H13, Cost Analysis: selecting the Invoicing Block Analysis card takes you to the Transportation Invoice Blocked Detailed View, while any other card takes you to the Transportation Costs Detailed View."
- q: What does the Weight Fulfillment Ratio card of Business Share Analysis show
  o: ["How much of its allocated weight share a carrier achieved", "How much of the vehicle capacity each freight order used", "How many freight orders each carrier delivered on time", "How much each carrier charged per kilogram of goods transported"]
  a: 0
  e: "H13, Business Share Analysis: the card shows how carriers performed in respect of total weight transported, that is, how much of their allocated share they achieved, for example 328,750kg out of 493,125kg (66.67%)."
- q: Which freight orders count as execution-relevant in the Life Cycle Status Analysis of Freight Order Execution Monitoring
  o: ["Those with status Completed and an arrival event", "Those with status New and no departure event", "Those with a planning block and a departure event", "Those In Execution (03) with no final arrival"]
  a: 3
  e: "H13, Freight Order Execution Monitoring: execution-relevant freight orders have the execution status In Execution (03) and have a departure event but no arrival event at the final destination."
- q: Which period of data does the input parameter P_TodayDate cause the system to retrieve
  o: ["The current day only", "The last twelve months from the system date", "The start of last month up to the system date", "The current calendar year up to the system date"]
  a: 2
  e: "H13, Main Input Parameters: the system uses the system date as P_TodayDate and retrieves information from the beginning of the previous month up to the system date."
- q: When does the Carrier On Time Performance card classify a freight order as on time
  o: ["When its first event is on time", "When all its events are classed as on time", "When at least half of its events are on time", "When its arrival event is on time"]
  a: 1
  e: "H13, Freight Order Execution Monitoring: a freight order is on time if all its events are classed as on time, otherwise it is classed as delayed."
- q: Is the use of TM analytics mandatory for the strategic freight procurement process
  o: ["No, it is not related to the master RFQ", "Yes, the master RFQ is built from the results", "Yes, but only for the carriers that are awarded", "No, because analytics cannot read the agreements"]
  a: 0
  e: "S4TM3, Determination of Procurement Needs: the analysis of historic data and the forecast are not related to the freight agreement master RFQ, so the use of SAP analysis tools is not mandatory for the SFP process."
```

---

## Session 14 — Enterprise Services, ESR Content and BRFplus

### Knowledge items
- Enterprise services for SAP TM are documented per process component, each with business process objects, service interfaces and service operations; additional ESR content (integration scenarios, mappings) complements them (H14).
- Process component TransportationOrderProcessing covers the ordering of transportation services from carriers: it lets shippers, logistics service providers and carriers exchange transportation-relevant data and create, change or cancel freight orders, freight requests for quotation or freight bookings, assign transportation demands to capacities, and let shippers create delivery proposals (H14, Transportation Order Processing).
- In the TransportationOrderProcessing scenario a shipper sends a transportation order to a carrier, who receives it as a transportation request and is expected to confirm; the carrier may subcontract the order to other carriers, who reply with confirmations (H14, Transportation Order Processing).
- The business process object TransportationOrder supports requesting a quotation, requesting execution of a transportation service, booking freight space, cancellations, replies (accept, modify, decline), shipping instructions (waybill notification), loading appointments and notifications about loading or unloading (H14, Transportation Order).
- Process component TransportationRequestProcessing handles customer requests for transportation services: A2A scenarios (Order Integration with order-based transportation requirements OTR, Delivery Integration with delivery-based transportation requirements DTR) and B2B scenarios (Forwarding Quotations, Forwarding Orders, Forwarding Orders Based on Forwarding Quotations) (H14, Transportation Request Processing).
- The business process object TransportationRequest lets a carrier receive requests for quotation and create forwarding orders, and lets a shipper plan and execute order-based and delivery-based transportation requirements (H14, Transportation Request).
- A service interface groups operations and is described by category (for example SAP A2A, B2B) and direction (inbound or outbound); a service operation is described by release state, technical name, namespace, direction, mode, idempotency and P2P communication enabled (H14, Export Declaration Requesting Out, Maintain Transportation Request).
- Release state of an operation is shown as Released or Released with Restrictions; the technical name carries a direction suffix such as _Out or _In (for example ExportDeclarationSUITERequest_Out and TransportationRequestRequest_In) (H14).
- Worked example of an outbound/inbound pair: Request Export Declaration (outbound, asynchronous) sends parties, items, means of transport, Incoterms and related document IDs to a customs management application, and Change Transportation Order based on Export Declaration Confirmation (inbound) receives the export declaration ID, the movement reference number (MRN) and an approval indicator and updates the order and its customs status (H14, Request Export Declaration, Change Transportation Order Based on Export Declaration Confirmation).
- Inbound operations support Forward Error Handling (FEH) with error categories such as DCE (Determination and Conversion Error), PRE (Processing Error) and PRE.TEE.LRE (Lock Request Error); Maintain Transportation Request also writes missing-master-data errors to the business application log (H14, Error Handling).
- Implementation notes: carriers and customers must be defined as business partners in the SAP TM back-end system, with standard IDs recommended for business partners, locations and products; outbound communication needs a logical system with an Outbound Queues queue type assigned in Customizing for SCM Basis (Integration Basic Settings for Creating the System Landscape) (H14, Master Data for B2B Communication, Request Trade Compliance Check Requesting Out).
- Enhancements: operations list a BAdI (for example /SCMTMS/EXP_SE_EXPDE_REQ for ExportDeclarationSUITERequest_Out) and some an enhancement spot (/SCMTMS/CDC_SE_SPOT_CDC) (H14, Enhancements).
- Additional ESR content: integration scenarios such as TM_ERPInvoiceIntegration live in the SAPTM IC software component in namespace http://sap.com/xi/TMS/Global/IC; mappings are named <Message name in SAP TM>_to_<IDoc type in SAP ERP> or the reverse (H14, Additional ESR Content, Mappings).
- The Web service GetTransportationDocumentURI (namespace http://sap.com/xi/TMS/UX) is an inbound, synchronous operation that lets SAP ERP display SAP TM documents, for example from invoice verification (MIRO, MIR7, MIR4) and agency business (WLF3, WZR3) (H14, Other Web Services).
- BRFplus provides an API and a UI to define and process business rules and reuse them in different applications; typical uses are validation, matching responsibilities or products, calculation of costs, overhead and risks, and technical configuration (H15, Use).
- BRFplus major components are application, function, catalog, expression, action and data object; the function is the interface between the rule and the calling application and holds the business logic; rules are implemented as expressions assigned to a function (H15, Use).
- A function has a context (rule input) and a result (rule output), both made of data objects of type element, structure or table; it can run in functional mode, event mode, or both (H15, Function, Data Objects and Types).
- Data object types build on each other: an element is an elementary type, a structure combines elements and structures, and a table takes the fields of one structure (or of one element, giving a one-column list); data objects can be bound to DDIC elements or ESR global data types (H15, Data Objects and Types, Data Binding).
- Expression types (for example Boolean, Case, Decision Table, Decision Tree, Formula, Value Range) define the computational power of BRFplus; a decision table compares input against condition rows from the top and returns the result of the first row where all cells match, so the most specific rows belong first (H15, Expressions, Decision Table Expression).
- Actions are the interactive part of BRFplus (Call Procedure, Log Message, Send Email, Start Workflow, Workflow Event); they have no output and can only be the final step of a processing branch (H15, Actions).
- A rule (If condition with a True branch and an optional False branch) can only be triggered inside a ruleset; a ruleset is assigned to one function in event mode, with priority 0 to 99 controlling execution order (H15, Rule, Ruleset, Function).
- A catalog is a filter that hides the repository and shows business users only the objects needed to maintain rules; an application is the container for all objects and has a storage type (system, master data or customizing) that cannot be changed after creation (H15, Catalog, Application).
- Typical BRFplus workflow: create an application, create a function with context, result and top expression, activate the objects, simulate the function, then integrate it with the calling application; the workbench is started with transaction BRFPLUS (H15, Typical Workflow, Understanding the User Interface).

### Skill items (tier: inferred)
- Read an operation's technical data table and state its direction, mode, release state and idempotency.
- Trace a B2B message pair (request out, confirmation in) between two process components or systems for one scenario.
- Map an error category (DCE, PRE, PRE.TEE.LRE) to the kind of failure it signals.
- Sketch a BRFplus function with its context data objects, result data object and top expression for a simple rule.
- Order the rows of a decision table from most specific to least specific.

### Important questions
- Which process component and which service operation would carry a freight order from a shipper to a carrier, and which one receives it as a forwarding order?
- What does it mean for an operation to be Released with Restrictions rather than Released, and where would you check this before relying on it?
- Why do inbound operations need error handling such as FEH when communication is asynchronous?
- Which master data and Customizing settings must exist before an outbound B2B message can be sent?
- How do BRFplus context and result relate to the calling application, and why must a decision table only use data objects that every function using it provides?

### Deliverable (tier: inferred)
A one-page reference table listing five enterprise service operations from H14 (process component, business object, direction, mode, release state, related operation), plus a short BRFplus sketch of one rule showing application, function, context, result and top expression.

### Self-confidence question (tier: inferred)
Can I explain how SAP TM exchanges transportation orders and requests through enterprise services, and how BRFplus rules are structured, to a technical colleague without notes?

### Quiz questions
```yaml
- q: According to H14, what is the process component TransportationOrderProcessing defined as
  o: ["The settlement of freight charges with the carriers involved", "The planning of freight units into freight orders for execution", "The ordering of transportation services from carriers", "The processing of requests from an ordering party for service"]
  a: 2
  e: "H14, Transportation Order Processing, Definition. The definition is the ordering of transportation services from carriers. The request-from-an-ordering-party definition belongs to TransportationRequestProcessing."
- q: When a shipper sends a transportation order to a carrier, in what form does the carrier receive it
  o: ["As a transportation request", "As a delivery proposal", "As a freight settlement document", "As a forwarding agreement"]
  a: 0
  e: "H14, Transportation Order Processing. The carrier receives the order in the form of a transportation request and is then expected to send a confirmation to the shipper."
- q: In the Delivery Integration scenario of TransportationRequestProcessing, how is a delivery represented in transportation request processing
  o: ["As an order-based transportation requirement for a sales order", "As a forwarding quotation for a customer request", "As a freight booking sent to a carrier", "As a delivery-based transportation requirement"]
  a: 3
  e: "H14, Transportation Request Processing. In Delivery Integration a delivery is represented by a delivery-based transportation requirement (DTR); orders are represented by order-based requirements (OTR)."
- q: In Forward Error Handling for inbound operations, which error category stands for Determination and Conversion Error
  o: ["PRE", "DCE", "LRE", "TEE"]
  a: 1
  e: "H14, Error Handling. The categories used are DCE (Determination and Conversion Error), PRE (Processing Error) and PRE.TEE.LRE (Lock Request Error)."
- q: What does the inbound operation Change Transportation Order based on Export Declaration Confirmation add to the order when creation is confirmed
  o: ["The export declaration ID and the MRN", "The customs tariff number and the carrier invoice number", "The loading appointment and the waybill number issued", "The trade compliance result and the credit limit status"]
  a: 0
  e: "H14, Change Transportation Order Based on Export Declaration Confirmation, Features. The operation adds the export declaration ID and the MRN to the order and updates its customs status."
- q: What is the mode of the inbound operation GetTransportationDocumentURI
  o: ["Asynchronous with idempotency", "Asynchronous without queues", "Synchronous", "Batch"]
  a: 2
  e: "H14, Other Web Services, GetTransportationDocumentURI. Category Inbound and mode Synchronous; it is triggered by the outbound operation of the same name in SAP ERP."
- q: In BRFplus, what is the input of a rule called
  o: ["Result", "Catalog", "Action", "Context"]
  a: 3
  e: "H15, Use. The rule input is known as context and the rule output is called result; both consist of data objects of type element, structure or table."
- q: What results in BRFplus when an element data object rather than a structure is assigned to a table data object
  o: ["A deeply nested structure of fields", "A one-column table, a simple list", "A table without any defined fields", "A table made of exactly two elements"]
  a: 1
  e: "H15, Data Objects and Types. If an element is assigned to a table instead of a structure, the result is a one-column table, that is a simple list."
- q: How does a BRFplus decision table expression evaluate its rows at runtime
  o: ["Row by row from the top, stopping at the first fully true row", "All rows in parallel, returning the result of the last matching row found", "Row by row from the bottom, stopping at the most general matching row", "Only the first row, falling back to a default result when it does not match"]
  a: 0
  e: "H15, Decision Table Expression. Rows are processed sequentially from the first row; when all cells in a row are true, evaluation stops and that row's result is returned. Hence the most specific conditions should come first."
- q: What is the purpose of a catalog in BRFplus
  o: ["To store the trace of every function execution", "To transport active objects between systems as XML", "To generate web services for the calling application", "To filter the repository for business users"]
  a: 3
  e: "H15, Catalog. A catalog simplifies rule maintenance by hiding the repository and displaying only the relevant objects; it serves as a filter for all objects in the repository."
```

---

## Session 15 — Clean Core and RISE with SAP Methodology

### Knowledge items
- Why a clean core is needed: a cloud ERP such as SAP Cloud ERP receives updates continuously, so extensions and integrations must be managed differently from on-premise SAP ERP; SAP developed the clean core concept for this (MCC100, Adjusting Business Models).
- The challenges behind clean core fall into three areas: business adaptability (supply chain disruptions, changing customer preferences, regulatory compliance), technological change, and landscape complexity (MCC100, Lessons 1 to 3 of Unit 1).
- Business model and supply chain pressure: supply chain disruptions (natural disasters, geopolitical tensions, COVID-19) expose single-source vulnerability, and businesses must pivot business models quickly without the technology landscape being an impediment (MCC100, The Impact of Disruptions in Global Supply Chains, Adapting Business Models).
- SAP Cloud ERP and SAP BTP are the response: SAP manages updates, security, compliance and scalability, SAP Cloud ERP is extensible and offers ready-to-go APIs, and SAP BTP is a cloud-native platform as a service that brings together AI, machine learning, data, analytics, database and DevOps (MCC100, SAP Cloud ERP, SAP BTP and Landscape Flexibility).
- Definition of clean core: core means five dimensions (processes, extensions, data, integrations, operations); clean means best practices, methodologies and tools exist for each; the clean core concept is a mindset and philosophy supported by governance and guiding principles; the goal is to get the core clean and then keep it clean (MCC100, Analyzing Clean Core Components).
- A newly provisioned SAP Cloud ERP system is clean by definition; the ideal state is an up-to-date release with cloud-compliant extensions and integration, excellent master data quality and perfect process design (MCC100, Clean Core Components; SL_RISE419, Clean Core Fundamentals).
- Components or distinguishing features of a clean core are minimalism, modularity, scalability, maintainability, and stability and reliability (MCC100, Components of a Clean Core; SL_RISE419, Clean Core Fundamentals).
- Implementation types: greenfield (new installation, clean by default), brownfield (system conversion to private edition or on-premise, retained complexity must be cleaned) and selective data transition or system landscape transformation (consolidating several ERP systems); the public edition cannot be chosen in a brownfield approach, and clean core can be accomplished with all approaches (MCC100, Describing Implementation Types and Clean Core).
- Misconceptions: SAP BTP is not the only means (key user and developer extensibility on stack are possible); clean core is not only about custom code and extensibility; it is not only about TCO; fit-to-standard is not the only way, since Tier 1 extensibility also keeps the core clean (MCC100, Some Misconceptions About Clean Core).
- Benefits for users (performance, reliable data, stability, flexible processes), for IT (no technical debt from legacy systems, software stack always at the latest release, extensions that do not break upgrades) and for the company (streamlined operations, cost savings, improved decision-making, enhanced collaboration) (MCC100, Unit 3).
- Clean business processes: mantra 'Keep competitiveness while reducing complexity'; establish organizational structure, technical foundation and transformation methodology, set up a prioritized business process hierarchy with end-to-end and functional views; tools named include SAP LeanIX, SAP Cloud ALM, SAP Signavio Process Manager and SAP Signavio Process Governance (MCC100, Clean Business Processes).
- Clean extensions: mantra 'Keep the extensions clean'; extensions are on-stack (Key User type 1, Developer type 2) or side-by-side on SAP BTP (type 3), may only use released APIs, BAdIs and extension points, and cloud-enabled technologies (ABAP Cloud); the Clean Core Level Concept evolves the 3-Tier model into Levels A, B, C and D (MCC100, Clean Extensions).
- Clean data: data is configuration, master and transactional; quality facets are accuracy, completeness, consistency, timeliness, validity and uniqueness; data volume must be controlled and personal master data stored only for justifiable purposes; tools named include SAP Master Data Governance and SAP Information Lifecycle Management (MCC100, Clean Data).
- Clean integrations (landscape): base integrations on standard OData and SOAP APIs, use SAP Integration Suite and SAP Event Mesh, use SAP Application Interface Framework for monitoring, and use RFC and IDoc only if absolutely necessary; SAP Integration Solution Advisory Methodology (ISA-M) supports strategy (MCC100, Clean Landscapes).
- Clean operations: mantra 'Keep the operations effective and efficient'; release management is the foundation, housekeeping tasks are established, and SAP Cloud ALM and the clean core dashboard (SAP S/4HANA Cloud Private Edition systems only) support monitoring (MCC100, Clean Operations).
- Best practices for implementation: assess business processes, establish a governance framework, streamline processes, rationalize data, simplify in both greenfield and brownfield, align with SAP's reference architecture, adopt SAP Activate and manage change and user adoption (MCC100, Clean Core Best Practices).
- RISE with SAP is SAP's transformation journey to the SAP Business Suite; the RISE with SAP Methodology is built on a clean core strategy and has three core components: a standardized framework, an integrated toolchain and expert guidance (SL_RISE419, The RISE with SAP Methodology, Key Components).
- Standardized framework: it augments the SAP Activate roadmap; the Discover phase uses the Digital Discovery Assessment, the Prepare phase has four onboarding calls with the Onboarding Advisor, and through Explore, Realize, Deploy and Run the Project Manager verifies tasks through Clean Core Quality Gates (questionnaires in SAP Cloud ALM); the Clean Core Success Plan holds over 150 recommended tasks (SL_RISE419, Standardized Framework, Prepare Phase, Explore to Run).
- Business phase Value and Architecture Artifacts Handover: presales and sales teams complete artifacts and hand them to the implementation team from Discover to Prepare; deliverables include the Business Capability Map, Application Architecture Overview, Solution Component Diagram, Technical Assessment, Architecture Roadmap, Value Roadmap, RISE Adoption Plan and Executive Proposal, each marked required or recommended (SL_RISE419, Handover Deliverables).
- Integrated toolchain: SAP LeanIX (landscape analysis), SAP Signavio (process evaluation and modeling), SAP BTP (extensions), Tricentis Test Automation, SAP Enable Now and SAP WalkMe, with SAP Cloud ALM as the digital backbone for project execution and the clean core success plan; SAP Signavio Governance is listed among the process analysis tools (SL_RISE419, The Integrated Toolchain, The RISE with SAP Methodology).
- Expert guidance and partners: individual sessions, expert meetings on Clean Core Quality Gate reports, the partner ecosystem and enhanced support; the RISE with SAP Competency has three levels (Essential, Advanced, Expert) and Expert-level partners can qualify as RISE with SAP Validated Partners (SL_RISE419, Expert Guidance, RISE with SAP Competency).
- The RISE with SAP Methodology Dashboard (Clean Core Dashboard, accessed through SAP Cloud ALM) has a System View (version insights, tool readiness, upgrade preparation) and an Operations View (daily System Health score and KPIs with up to 30 days of history) (SL_RISE419, Dashboard).

### Skill items (tier: inferred)
- Classify a given extension or integration approach against the five clean core dimensions and name the principle it follows or breaks.
- Place a described extension on the Clean Core Level Concept (A to D) and say why.
- Choose between greenfield, brownfield and selective data transition for a short customer description and justify the clean core consequence.
- Map a RISE with SAP phase (Discover, Prepare, Explore to Run) to its clean core activities and tools.

### Important questions
- Why does continuous updating in a cloud ERP change how extensions and integrations must be built?
- Which of the five dimensions is hardest to keep clean after go-live, and which tool or method named in the sources supports it?
- How do the four misconceptions about clean core differ from what the course actually states?
- What is the difference between the Clean Core Quality Gates and the RISE with SAP Methodology Dashboard?
- Which handover deliverables would an implementation team need first when a project moves from Discover to Prepare?

### Deliverable (tier: inferred)
A one-page clean core checklist with one section per dimension (processes, extensions, data, integrations, operations): the mantra, two principles and the SAP tool or method named for it, plus a short timeline of the RISE with SAP phases showing where the four onboarding calls and the Quality Gates occur.

### Self-confidence question (tier: inferred)
Can I explain what a clean core is, why it is needed, and how the RISE with SAP Methodology supports it to a project sponsor without notes?

### Quiz questions
```yaml
- q: Which set lists the five dimensions of core described in MCC100
  o: ["Processes, extensions, applications, integrations, users", "Processes, extensions, data, interfaces, hardware", "Processes, modifications, data, integrations, operations", "Processes, extensions, data, integrations, operations"]
  a: 3
  e: "MCC100, Analyzing Clean Core Components. By core the course means the dimensions Processes, Extensions, Data, Integrations and Operations; SL_RISE419 lists the same five."
- q: How does MCC100 describe a newly provisioned SAP Cloud ERP system with regard to clean core
  o: ["It is clean by definition, so the goal is to keep it clean", "It must first pass a dedicated cleansing project before it counts as clean", "It is clean only after all existing custom code has been migrated", "It is clean only if it is provisioned as the private edition"]
  a: 0
  e: "MCC100, Clean Core Components. A newly provisioned SAP Cloud ERP system is clean per definition, and the goal for the customer in that case is to keep the core clean."
- q: Which implementation approach is NOT possible for SAP S/4HANA Cloud Public Edition according to MCC100
  o: ["Greenfield implementation as a new installation", "Starting with a clean slate in a provisioned system", "Brownfield implementation as a system conversion", "Designing processes on current best practices"]
  a: 2
  e: "MCC100, Describing Implementation Types and Clean Core. A brownfield implementation upgrades an existing system to private edition or on-premise; the public edition cannot be chosen in the context of a brownfield approach."
- q: Which statement does MCC100 give as a misconception about clean core
  o: ["Clean core also affects data, integration and operations", "SAP BTP is the only way to keep the core clean", "Clean core contributes to a reduction of TCO", "Tier 1 extensibility also keeps the core clean"]
  a: 1
  e: "MCC100, Some Misconceptions About Clean Core. SAP BTP is needed for side-by-side extensions, but key user and developer extensibility on stack are also possible with SAP Cloud ERP."
- q: In MCC100, where are type 3 extensions created
  o: ["As key user extensions inside SAP S/4HANA Cloud", "As developer extensions inside SAP S/4HANA Cloud", "As classic ABAP modifications of delivered code", "As side-by-side extensions on SAP BTP"]
  a: 3
  e: "MCC100, Extensions Don't Break Upgrades. On-stack extensions are Key User (type 1) or Developer (type 2); side-by-side extensions are created within SAP BTP (type 3)."
- q: In the Clean Core Level Concept, which extensions belong to Level B
  o: ["Those using an unreleased API that SAP deems stable", "Those using only publicly released and stable interfaces", "Those using APIs with a changelog because they may change", "Those using explicitly non-recommended objects or techniques"]
  a: 0
  e: "MCC100, Clean Core Level Concept. Level B uses an unreleased API (like a BAPI) deemed by SAP to be stable and upgrade safe; Level A uses released interfaces, Level C relies on APIs with a changelog, Level D is not considered clean."
- q: According to MCC100, which SAP solution best addresses data privacy compliance through automated archiving and retention
  o: ["SAP Master Data Governance for central hubs", "SAP Datasphere for data warehousing", "SAP Information Lifecycle Management", "SAP Information Steward for data analysis"]
  a: 2
  e: "MCC100, Data Privacy Compliance. Data privacy compliance is best addressed through SAP Information Lifecycle Management, which automates data archiving and retention and decommissioning of legacy systems."
- q: How does MCC100 treat RFC and IDoc for integrations
  o: ["As the preferred technologies for all integrations", "As recommended only if absolutely necessary", "As required for event-based scenarios", "As replaced entirely by SAP Event Mesh"]
  a: 1
  e: "MCC100, Avoid Legacy APIs And Their Legacy Extension Options. RFC and IDoc are only recommended if absolutely necessary; OData and SOAP align better with clean core principles."
- q: What are the three core components of the RISE with SAP Methodology
  o: ["Discovery toolkit, quality gates and dashboards for each phase", "Roadmap viewer, success plan and runbook for every project team", "Onboarding calls, handover artifacts and partner workshops", "Standardized framework, integrated toolchain, expert guidance"]
  a: 3
  e: "SL_RISE419, The RISE with SAP Methodology. The core components are a standardized framework, an integrated toolchain and expert guidance through end-to-end engagement."
- q: How many personalized onboarding sessions does SAP's Onboarding Advisor host in the Prepare phase
  o: ["Four", "Two", "Three", "Six"]
  a: 0
  e: "SL_RISE419, Standardized Framework and Prepare Phase. SAP's Onboarding Advisor hosts four personalized sessions, from Get Started with SAP to reviewing the Clean Core Quality Gate assessment."
```

---
