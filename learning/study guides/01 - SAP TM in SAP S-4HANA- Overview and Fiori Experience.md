# Session 01 — SAP TM in SAP S/4HANA: Overview and Fiori Experience

## Overview
This session places SAP Transportation Management (TM) inside SAP S/4HANA. It covers how TM relates to the older basic shipping (LE-TRA), what TM does across its five stages, the six objects you will meet in every later session, and how users reach TM through SAP Fiori. Nearly every later session builds on these objects, so learn the abbreviations here.

## Basic shipping (LE-TRA) versus Transportation Management: LE-TRA is part of the compatibility scope and its code line is kept within SAP S/4HANA Enterprise Management until end of 2030; TM has been part of SAP S/4HANA since 1709, and its advanced functions require an additional license
Logistics Execution in SAP ERP covered warehouse management, shipping and transportation. Inbound shipments follow procurement: purchase order, vendor confirmation, inbound delivery, inbound shipment, goods receipt, invoice verification. Outbound shipments follow sales: sales order, outbound delivery, outbound shipment, goods issue, invoice (S4611).

The software component LE-TRA carried this transportation content in SAP ECC. It is part of the compatibility scope, and its code line stays in SAP S/4HANA Enterprise Management until end of 2030. Its functionality is called **basic shipping**.

From SAP S/4HANA 1709, **Transportation Management** is part of SAP S/4HANA Enterprise Management. It offers much more comprehensive functionality, and its advanced functions need an additional license. It can also be used with limited scope, offering the same capabilities as LE-TRA, and that use needs no specific license. Before release 2020 the name "Basic Shipping" was also used for the base variant of SAP S/4HANA TM. From 2020 that capability is called Transportation Management.

Basic shipping and TM are independent. They can run in parallel on the same SAP S/4HANA database instance, but they have no data exchange and no integration within the shipping process. The course material points to SAP note 3065464 for which objects and functions belong to the basic scope and which need the additional license, and to SAP note 3097186 for a tool that analyzes LE-TRA usage and how to migrate it to TM. Best practices for implementing TM scenarios are in SAP notes 2535942 (1709), 2849554 (1809) and 2970208 (1909).

## Advanced TM plans from orders (sales orders, purchase orders, MM scheduling agreements) as well as from deliveries, and can combine inbound and outbound deliveries in one freight order; its differentiators are vehicle scheduling and routing, carrier selection, load consolidation and load planning; long term the LE-TRA shipment is replaced by the TM freight order
Advanced TM addresses shipping industries and also freight forwarders. In basic shipping, planning is based on deliveries only (outbound and inbound). Advanced TM adds early planning from orders: sales orders, purchase orders and MM scheduling agreements. It also allows inbound and outbound deliveries to be planned together in one freight order.

The key differentiators over basic shipping are sophisticated planning and optimization options: vehicle scheduling and routing, carrier selection, load consolidation and load planning.

The direction is clear in the material: long term, the collection of transportation processes is realized only with selected TM functions, and the LE-TRA shipment is replaced by the TM **freight order**. Because the freight processes were developed further in TM, some functions may be realized differently than in LE-TRA (S4611).

## The five main stages of TM: Requirements and Order Management, Transportation Planning, Transportation Execution, Freight Costing and Settlement, Analytics and Collaboration; and the scenario, shipping, movement and stage types TM supports
TM supports many scenarios for shippers and logistics service providers. S48600 lists, for example:
- scenario types: inbound, outbound, domestic, international
- shipping types: LTL, FTL, LCL, FCL and CEP
- movement types: direct shipment, uni-modal, multimodal, port-to-port, door-to-door, export shipment
- stage types: pickup, precarriage, main carriage, on-carriage, delivery, drayage, haulage
- parties and roles, such as ordering party, shipper, consignee, invoicing party, payment party, forwarder or carrier
- legal documents, such as HBL, HAWB, manifests and delivery notes

H01 adds that TM supports activities such as creating forwarding orders, freight units, delivery proposals, freight orders and freight bookings, performing carrier selection, creating agreements, tendering, dispatching and monitoring, charge calculation, and considering foreign trade and dangerous goods regulations.

The processes fall into five stages (S48600):
1. **Requirements and Order Management.** Transportation requirements are created from orders. For shippers this happens either embedded (sales order and delivery in the same system as TM, using SD, MM and LE documents) or decentralized (orders and deliveries in a separate system, represented by order-based or delivery-based transportation requests). The requirements' data, together with freight unit building rules, forms freight units.
2. **Transportation Planning.** Freight units are assigned to means of transport to create freight orders, manually, with optimization, or semi-automatically (for example transportation proposals, unified package building, load optimization). Planning happens in the transportation cockpit. Carrier selection can be manual, optimized or done by tendering, and produces a ranked list of eligible carriers.
3. **Transportation Execution.** The freight order is the basis. Cargo movement updates order and cargo status, through manual entries or automatic updates via SAP Event Management and Global Track and Trace.
4. **Freight Costing and Settlement.** Freight agreements reference calculation sheets that list charge elements. The calculation engine computes the charges, and the result is stored in the freight order. Freight settlement documents are created from freight orders and passed to ERP (accruals, later purchase order and service entry sheet for invoice verification or self-billing).
5. **Analytics and Collaboration.** Overview pages, reports and KPI dashboards, tailored to business roles.

## The core TM objects: OTR, DTR, freight unit (FU), freight order (FO), freight agreement (FA) and freight settlement document (FSD)
S48600 defines them as follows:

| Object | Abbreviation | What it is |
|---|---|---|
| Order-based transportation requirement | OTR | Demand from a sales order, purchase order or stock transport order |
| Delivery-based transportation requirement | DTR | Demand from an inbound or outbound delivery |
| Freight unit | FU | A set of goods that are transported together across the entire supply chain; the smallest planning unit |
| Freight order | FO | The object whose execution is planned by a carrier or a shipper |
| Freight agreement | FA | A contract with the carrier |
| Freight settlement document | FSD | Used to verify the carrier invoice |

The flow runs from requirement to freight unit (built from the business document data and freight unit building rules), to freight order (planning assigns freight units to means of transport), to freight settlement document (the carrier's charges, based on the freight agreement and calculation sheet, are verified).

## The SAP Fiori user experience and access to TM: role-based apps and the launchpad, catalogs, groups, spaces and pages; business catalogs and role templates; the three Fiori app types; the SAP Fiori Apps Reference Library; the Personal Object Worklist (POWL)
**Fiori principles.** SAP Fiori is based on SAPUI5 (HTML5) and is role-based: the large classic transactions are decomposed into discrete apps that fit user roles, all connected, with the launchpad as the central entry point. Users can personalize their launchpad.

**Launchpad structure (S48600).** A tile represents an app. A **catalog** is a set of tiles made available for one role, and catalogs are assigned to business roles. **Groups** define grouping, sort order and appearance of the apps on the home page. The layout can alternatively use **spaces and pages**: a space is the entry point for a business role, consists of one or more pages (self-contained work contexts), and a page consists of sections that structure the tiles. Technical catalogs define apps per solution area; business catalogs reference those apps per user duty; business roles tie business catalogs, groups and spaces to users.

**TM access (H02).** The launchpad is the access point for TM web apps. The tiles a user sees depend on the business catalogs assigned to their business roles. SAP delivers role templates SAP_BR_TRANSPORTATION_MANAGER, SAP_BR_TRANSPORTATION_PLANNER, SAP_BR_FRGHT_CTRC_SPECIALIST and SAP_BR_FRGHT_SETTLEMENT_CLERK. For the Transportation Manager role, the business catalogs include Transportation – Order Management (SAP_TM_BC_OM), Planning (SAP_TM_BC_PLN), Settlement (SAP_TM_BC_STLM), Contract Management (SAP_TM_BC_CTRM) and Charge Management.

**App types (S4611).** Transactional apps use ABAP, the classic approach. Analytical apps use the analytical capabilities of SAP HANA. Fact sheet apps use SAP HANA Enterprise Search.

**SAP Fiori Apps Reference Library (S48600).** It lists all relevant content for the launchpad. You can filter by application type and product version and find the technical data for installation and configuration. Always set the product suite and then the release first, because implementation can differ between releases.

**POWL (S48600).** The Personal Object Worklist gives central, personalized access to document lists. Users define and optionally store queries, similar to ERP selection screen variants. Tables can be filtered and personalized, queries can be refreshed, and refreshes run asynchronously.

*What the material does not establish:* it gives no complete list of TM role templates beyond the four above, and the Fiori app list file in the corpus is a lookup table, not explained here.

## Practice
Create a one-page "TM map". Include a table of the five stages, each with its main object and one activity, and a short comparison of basic shipping and advanced TM with two differences taken from this material.

## Self-check
Can I explain to a business stakeholder, without notes, how a sales order becomes a freight order and a settled carrier invoice in TM?
