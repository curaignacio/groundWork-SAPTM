# {Subject} — Knowledge Index
Last updated: 2026-10-21

<!--
FORMAT REFERENCE ONLY — the examples below are not entries. Keep this comment in place.

Written and updated by analyzeCorpus. Read first by every question, and by every skill
that works from the corpus. One entry per file in src/md/ and src/csv/, ordered by the
sequence in which files were processed. Updated incrementally on re-run: new or changed
files are added or updated; an entry is removed only when its source file is deleted.

A file of more than 500 lines has a topic map in src/sections/ listing its topics and the
line where each starts. Read the map, then only the lines of the topic you need.

Entry format — a large file:

## {file name}
- source: {original file name and format before conversion}
- location: src/md/{subfolder/}
- lines: {N}
- summary: {one-line description of what the document covers}
- key topics: {comma-separated list of main topics covered}
- sections: src/sections/{subfolder/}{file name without .md}.sections.md ({N} topics)

A file of 500 lines or fewer ends with:  - sections: none — read it whole
A large file with no structure ends with:  - sections: none — no structure found; search it
A CSV has  - rows: {N}  and  - columns: {A | B | C}  instead of lines, and ends with:
- sections: none — search its rows
-->

## FioriAppList.csv
- source: FioriAppList.csv
- location: src/csv/
- rows: 5702
- columns: App Name | App ID | App Launcher Title - Subtitle (Information) | UI Technology | Application Component | App Description
- summary: List of SAP Fiori apps with ID, launcher title, UI technology, application component and description.
- key topics: Fiori app names and IDs, launcher titles, UI technology (e.g. SAP Fiori elements), application components, app descriptions
- sections: none — search its rows

## MCC100-Managing-Clean-Core-for-SAP-S4HANA-Cloud.md
- source: MCC100-Managing-Clean-Core-for-SAP-S4HANA-Cloud.md
- location: src/md/courses/
- lines: 2737
- summary: SAP course material on why a clean core is needed for SAP Cloud ERP: changing business models and supply chains, what a clean core is and its components, its benefits and its dimensions.
- key topics: clean core, ERP challenges, business model adjustment, supply chain disruptions, customer preferences, technological advancements, SAP Cloud ERP, SAP BTP, system landscape flexibility, components of a clean core, implementing a clean core, misconceptions, benefits for users (performance, data, business processes), business process and requirement balance
- sections: src/sections/courses/MCC100-Managing-Clean-Core-for-SAP-S4HANA-Cloud.sections.md (114 topics)

## S4611-Basic-Transportation-Management-in-SAP-S4HANA.md
- source: S4611-Basic-Transportation-Management-in-SAP-S4HANA.md
- location: src/md/courses/
- lines: 8779
- summary: SAP course on basic Transportation Management in SAP S/4HANA: motivation and overview, Fiori user experience and worklists, master data and the transportation network, freight units, planning, carrier subcontracting and execution.
- key topics: SAP S/4HANA motivation and deployment options, TM overview, best practice scenarios, SAP Fiori UX, worklists, business partners, locations, transportation network, lanes, freight unit building rules, conditions, transportation planning, subcontracting to carriers, transportation execution, freight order, advanced transportation outlook
- sections: src/sections/courses/S4611-Basic-Transportation-Management-in-SAP-S4HANA.sections.md (458 topics)

## S48600-Business-Processes-in-SAP-S4HANA.md
- source: S48600-Business-Processes-in-SAP-S4HANA.md
- location: src/md/courses/
- lines: 7618
- summary: SAP course on business processes in SAP S/4HANA with a Transportation Management focus: TM overview, planning, execution, freight costing and settlement, analytics, Fiori launchpad and master data.
- key topics: SAP TM overview, transportation planning, transportation execution, freight costing and settlement, analytics and collaboration, common TM terms (SO, PO, STO, inbound, IDL/ODL), SAP Fiori launchpad and library, worklists, master data overview, organizational structure, material master, transportation networks
- sections: src/sections/courses/S48600-Business-Processes-in-SAP-S4HANA.sections.md (279 topics)

## S4TM2-Planning-and-Execution-in-SAP-S4HANA-TM.md
- source: S4TM2-Planning-and-Execution-in-SAP-S4HANA-TM.md
- location: src/md/courses/
- lines: 8962
- summary: SAP course on planning and execution in SAP S/4HANA TM: business partners and master data (locations, zones, trade lanes, modes, resources), network path finding, and the planning and execution of transportation.
- key topics: business partners, business partner determination, location master, border crossing point, geocoding, transportation zones and hierarchy, trade lane, transportation mode, means of transport, multi-resource, path finder, resources, compartments, handling resource, calendar resource, transportation unit resource
- sections: src/sections/courses/S4TM2-Planning-and-Execution-in-SAP-S4HANA-TM.sections.md (180 topics)

## S4TM3-Charges-and-Settlement-in-SAP-S4HANA-TM.md
- source: S4TM3-Charges-and-Settlement-in-SAP-S4HANA-TM.md
- location: src/md/courses/
- lines: 7925
- summary: SAP course on charges and settlement in SAP S/4HANA TM: evaluating TM and deployment options, charge calculation, rate tables, scales, charge types, freight agreements and settlement, strategic freight procurement.
- key topics: evaluating TM, evolution of TM at SAP, deployment options and migration paths, charge calculation, charge requests, scale template, rate table, charge types, freight agreement, road-sea-road example, stages, scale base, calculation sheet fields, UoM relevant, dimension, procuring strategic freight
- sections: src/sections/courses/S4TM3-Charges-and-Settlement-in-SAP-S4HANA-TM.sections.md (304 topics)

## SL_RISE419-Introducing-RISE-with-SAP-Methodology-for-SAP-Partners-and-Customers.md
- source: SL_RISE419-Introducing-RISE-with-SAP-Methodology-for-SAP-Partners-and-Customers.md
- location: src/md/courses/
- lines: 2069
- summary: SAP course introducing the RISE with SAP methodology for partners and customers: its standardized framework, key components, clean core fundamentals and the handover deliverables between phases.
- key topics: SAP Business Suite, RISE with SAP methodology, SAP Signavio Governance, clean core fundamentals, standardized framework, key components, business phase value and architecture artifacts handover, handover deliverables (required and recommended)
- sections: src/sections/courses/SL_RISE419-Introducing-RISE-with-SAP-Methodology-for-SAP-Partners-and-Customers.sections.md (44 topics)

## E01 - Master Data and Configuration.md
- source: E01 - Master Data and Configuration.md
- location: src/md/exercises/
- lines: 589
- summary: Step-by-step Fiori exercise on TM master data and configuration: reviewing carrier business partners, rate tables, vehicle resources and freight unit building rules.
- key topics: carrier business partner review, carrier role, TCM rate, rate table, vehicle resource, freight unit building rule INC_S4TM1_FU
- sections: src/sections/exercises/E01 - Master Data and Configuration.sections.md (12 topics)

## E02 - Transportation Requirements.md
- source: E02 - Transportation Requirements.md
- location: src/md/exercises/
- lines: 399
- summary: Step-by-step Fiori exercise: create a purchase order with Create Purchase Order - Advanced and review the resulting freight unit.
- key topics: create purchase order, supplier and organizational data, item overview, freight unit review, transportation requirement
- sections: none — read it whole

## E03 - Transportation Planning.md
- source: E03 - Transportation Planning.md
- location: src/md/exercises/
- lines: 3200
- summary: Step-by-step Fiori exercise on transportation planning: freight order worklists and documents, the transportation cockpit, selection and planning, and carrier selection.
- key topics: freight order worklist, transportation documents, freight order details, transportation cockpit, selection attributes, manual planning, planning map, saved profiles
- sections: src/sections/exercises/E03 - Transportation Planning.sections.md (81 topics)

## E04 - Transportation Execution.md
- source: E04 - Transportation Execution.md
- location: src/md/exercises/
- lines: 1017
- summary: Step-by-step Fiori exercise on transportation execution: create deliveries with the Delivery Builder and carry out warehouse loading and unloading steps.
- key topics: create deliveries, Delivery Builder, profile and layout sets, warehouse loading, warehouse unloading, execution steps
- sections: src/sections/exercises/E04 - Transportation Execution.sections.md (32 topics)

## E05 - Freight Costs and Settlements.md
- source: E05 - Freight Costs and Settlements.md
- location: src/md/exercises/
- lines: 1449
- summary: Step-by-step Fiori exercise on freight costs and settlement: freight agreements, rate tables, charge calculation and settlement.
- key topics: freight agreements worklist, agreement parties and validity, rate table, definition of charges, S4LG1_COUNTRY, S4LG1_WEIGHT, freight settlement
- sections: src/sections/exercises/E05 - Freight Costs and Settlements.sections.md (42 topics)

## H01 - Transportation Management (TM).md
- source: H01 - Transportation Management (TM).md
- location: src/md/sapHelp/
- lines: 168
- summary: SAP Help overview of Transportation Management: what TM does (delivery proposals, agreements, dispatching and monitoring, analytics) and its integration with other SAP components.
- key topics: TM overview, delivery proposals, agreements, dispatching and monitoring, analytics and KPIs, integration, Advanced Shipping and Receiving, SAP Global Trade Services, Document Information Extraction
- sections: none — read it whole

## H02 - Introductory Information.md
- source: H02 - Introductory Information.md
- location: src/md/sapHelp/
- lines: 251
- summary: SAP Help introductory information for TM: working with web applications, business catalogs and roles, and how to display application and field help.
- key topics: web applications, business catalogs (SAP_TM_BC_STLM, SAP_TM_BC_CTRM, SAP_TM_BC_CHGM, SAP_TM_BC_MD, SAP_TM_BC_PRFS), documents, document items, release scheduling, delivery customizing, application help, field help, feature scope
- sections: none — read it whole

## H03 - Master Data.md
- source: H03 - Master Data.md
- location: src/md/sapHelp/
- lines: 22317
- summary: SAP Help documentation of TM master data: business partners and partner determination, carrier and freight code sets, resources, transportation lanes, organizational model and agreements.
- key topics: Enterprise Asset Management integration, business partners (carrier, driver, forwarding agent), carrier service codes, partner functions and determination, freight code sets, transportation groups, carrier profile, resources, transportation lanes, equipment, fixed and dimension transportation costs, organizational model, organizational units, forwarding and freight settlements, forwarding quotation
- sections: src/sections/sapHelp/H03 - Master Data.sections.md (1718 topics)

## H04 - Forwarding Order Management.md
- source: H04 - Forwarding Order Management.md
- location: src/md/sapHelp/
- lines: 8255
- summary: SAP Help documentation of forwarding order management: creating and processing forwarding orders and quotations, their screens, statuses, blocking and forwarding settlement.
- key topics: forwarding order creation, ordered and actual route, order items, document flow, output management, status, HBL or HAWB, profitability, charge calculation, air cargo security, change documents, forwarding quotation, freight unit, forwarding settlement document, order statuses, blocking
- sections: src/sections/sapHelp/H04 - Forwarding Order Management.sections.md (603 topics)

## H05 - Logistics Integration.md
- source: H05 - Logistics Integration.md
- location: src/md/sapHelp/
- lines: 7158
- summary: SAP Help documentation of TM logistics integration with SD, MM and delivery processing: order, scheduling agreement, JIT call and delivery integration, advanced intercompany processes and related Customizing and reports.
- key topics: order integration, scheduling agreement integration, JIT call integration, delivery proposals, delivery integration, transportation relevance, integration time range, advanced intercompany sales and stock transfer, Incoterms, stage building, transfer of control, logistics integration profile, location determination, freight unit building rule, reports for logistics integration
- sections: src/sections/sapHelp/H05 - Logistics Integration.sections.md (553 topics)

## H06 - Freight Order Management.md
- source: H06 - Freight Order Management.md
- location: src/md/sapHelp/
- lines: 21798
- summary: SAP Help documentation of freight order management: freight order structure and creation, editing, transportation cockpit, resources, schedules, drivers, rail freight orders and carrier assignment.
- key topics: freight order, items, communication history, output management, transportation dependencies, seals, scheduling, manual creation, creation from planning, from freight unit, from schedule, freight order table, transportation cockpit, resources, drivers, forwarding orders from freight orders, rail freight order, stages, invoicing carrier, default routes, dangerous goods, global trade
- sections: src/sections/sapHelp/H06 - Freight Order Management.sections.md (1679 topics)

## H07 - Planning.md
- source: H07 - Planning.md
- location: src/md/sapHelp/
- lines: 24797
- summary: SAP Help documentation of TM planning: freight unit building, manual and automatic planning, transportation cockpit, constraints, carrier selection, scheduling and automatic freight order creation.
- key topics: freight units, freight unit building rules and strategies, unified package building, planning profiles and settings, manual and automatic planning, transportation cockpit, time windows, hard constraints, split and merge, scheduling, carrier selection, freight order types, transportation unit, process controller strategies, delivery-based requirements, JIT calls
- sections: src/sections/sapHelp/H07 - Planning.sections.md (1770 topics)

## H08 - Agreement Management.md
- source: H08 - Agreement Management.md
- location: src/md/sapHelp/
- lines: 8969
- summary: SAP Help documentation of agreement management: strategic freight procurement, freight agreement RFQs, quotations and awards, rate tables and freight agreements.
- key topics: strategic freight procurement, rate quotation, agreements, rating structure, quotations, freight agreement RFQ master, RFQ type, negotiation rounds, calculation sheet, carriers, trade lanes, capacities, Excel integration, versions, award summary, award confirmation, optimizer strategy, rate table
- sections: src/sections/sapHelp/H08 - Agreement Management.sections.md (645 topics)

## H09 - Settlement.md
- source: H09 - Settlement.md
- location: src/md/sapHelp/
- lines: 19298
- summary: SAP Help documentation of TM settlement: forwarding, freight and internal settlement, agreements, cost distribution, settlement documents and statuses, and charge management.
- key topics: internal settlement for resources, settlement for shippers, forwarding settlement, freight settlement, cost distribution, Incoterms, forwarding, freight and internal agreements, consolidated shipment, settlement based on agreed rates or freight costs, settlement statuses and posting, credit memos, charge management, service product catalogs, charge calculation, buyer's consolidation, settlement for container items
- sections: src/sections/sapHelp/H09 - Settlement.sections.md (1308 topics)

## H10 - Carrier Collaboration.md
- source: H10 - Carrier Collaboration.md
- location: src/md/sapHelp/
- lines: 859
- summary: SAP Help documentation of carrier collaboration: how carriers respond to freight agreement RFQs, handle freight tendering, confirm and execute freight orders and review settlement.
- key topics: carrier collaboration, strategic freight procurement, responding to freight agreement RFQs, freight tendering, freight request for quotation, freight quotation, freight order confirmation, freight order execution, credit memos, charges for freight orders
- sections: src/sections/sapHelp/H10 - Carrier Collaboration.sections.md (63 topics)

## H11 - Integration.md
- source: H11 - Integration.md
- location: src/md/sapHelp/
- lines: 12133
- summary: SAP Help documentation of TM integration with other components: logistics integration, Extended Warehouse Management, Advanced Shipping and Receiving, Event Management and Global Trade Services.
- key topics: logistics integration, freight settlement, Extended Warehouse Management, SAP Event Management, SAP Global Trade Services, Advanced Shipping and Receiving, storage location, Lean Warehouse Management, consignment orders, decentralized EWM and TM, doors, end-to-end process, transport-driven and warehouse-driven processes, delivery split, warehouse loading and unloading stops, package building, capacity documents
- sections: src/sections/sapHelp/H11 - Integration.sections.md (800 topics)

## H12 - Basic Functions.md
- source: H12 - Basic Functions.md
- location: src/md/sapHelp/
- lines: 13622
- summary: SAP Help documentation of TM basic functions, centred on dangerous goods management: checks, records, PS&S integration, settings, UI profiles and phrase management.
- key topics: checks, dangerous goods records, dangerous goods checks, PS&S services, common settings, forwarding quotation types, adapting DG processing, phrase management, goods check methods, transport restrictions, total points calculation, VSR optimization, UI profiles and groups, regulations, field properties
- sections: src/sections/sapHelp/H12 - Basic Functions.sections.md (1170 topics)

## H13 - Analytics.md
- source: H13 - Analytics.md
- location: src/md/sapHelp/
- lines: 7109
- summary: SAP Help documentation of TM analytics: overview pages, detailed views and CDS views for transportation allocation, business share, cost analysis, freight order execution and tendering.
- key topics: analytics overview pages, detailed views, CDS views, transportation allocation, business share, cost analysis, freight order execution, tendering, allocation analysis, trade lane weight, volume and container load analysis, utilization distribution, carrier selection, input parameters, measures and attributes, fulfillment ratios
- sections: src/sections/sapHelp/H13 - Analytics.sections.md (681 topics)

## H14 - Enterprise Services and ESR Content.md
- source: H14 - Enterprise Services and ESR Content.md
- location: src/md/sapHelp/
- lines: 18023
- summary: SAP Help documentation (Release 9.4 SP00) of TM enterprise services and ESR content: process components, business objects, service interfaces and operations for integration.
- key topics: enterprise services, ESR content, process components, TransportationOrderProcessing, TransportationRequestProcessing, master data for B2B communication, service interfaces, inbound and outbound, idempotency, released status, message types, enhancements, error handling, freight order, freight booking, freight request and tendering, trade compliance check, ERP logistics integration, use cases
- sections: src/sections/sapHelp/H14 - Enterprise Services and ESR Content.sections.md (1755 topics)

## H15 - Business Rule Framework plus (BRFplus).md
- source: H15 - Business Rule Framework plus (BRFplus).md
- location: src/md/sapHelp/
- lines: 19141
- summary: SAP Help documentation of Business Rule Framework plus (BRFplus), ABAP platform 2025 FPS02, a large document with no recoverable structure.
- key topics: BRFplus, business rules, functions, expressions, actions, data objects (element, structure, table), context and result, catalog, application
- sections: none — no structure found; search it
