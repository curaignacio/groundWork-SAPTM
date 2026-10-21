# Session 11 — Warehouse and Trade Integration (EWM, Advanced Shipping and Receiving, GTS)

## Overview
Transportation does not start at the truck. Goods are picked and packed in a warehouse, trucks queue at a gate and use a door, customs clearance may be needed before the truck can leave, and the shipper wants to see where the cargo is. This session covers how TM connects to those worlds: Advanced Shipping and Receiving (Advanced SR) with Extended Warehouse Management (EWM) and the other warehouse components, SAP Event Management for tracking, and SAP Global Trade Services (GTS) for compliance and customs. The thread running through it is status: at each step one status changes, and the status tells you who is responsible for the cargo, TM or the warehouse (H11, E04).

## The integration landscape of TM: logistics integration of orders and deliveries, integration with settlement, Advanced Shipping and Receiving, Extended Warehouse Management (EWM), SAP Event Management (SAP EM) and SAP Global Trade Services (SAP GTS); Document Information Extraction extracts data from delivery documents attached to a consignment order
H11 (Integration) lists what TM can be integrated with:

| Application | Integration |
|---|---|
| Logistics Integration | Integration of orders and deliveries |
| Settlement | Forwarding settlement and freight settlement (see Session 10) |
| Advanced Shipping and Receiving | Integrated end-to-end process to send, receive and transport products |
| Extended Warehouse Management | Integration with EWM |
| SAP Event Management | Tracking of execution status |
| SAP Global Trade Services | Customs processing and trade compliance |

H01 (Integration) adds the descriptions: SAP EM is used for event tracking to monitor the execution status of transportation; for SAP GTS you can request export declarations for freight orders or freight bookings, with data transferred by enterprise services. It also lists **Document Information Extraction**, a service that extracts data from delivery documents attached to a consignment order (H01 points to AI-Assisted Goods Receipt Analysis for details). H01 further notes that PS&S Services support dangerous goods, and that TM can integrate with external systems through enterprise services, for example to create and confirm forwarding orders automatically from data received from ordering parties.

*What the material does not establish:* H01 and H11 only name Document Information Extraction in one line; the corpus does not describe how it works.

## Advanced Shipping and Receiving (Advanced SR) is an integrated end-to-end process to send, receive and transport products, covering mixed and multi-warehouse scenarios in one freight order and the steps from the truck's arrival at the gate to the final goods receipt; it is also supported for rail freight orders
H11 (Advanced Shipping and Receiving) describes Advanced SR as an integrated, end-to-end process that lets users send, receive and transport products. It supports **mixed and multi-warehouse scenarios within one freight order** and helps coordinate the steps from the arrival of the truck at the gate to the final goods receipt in the warehouse. A truck that has posted arrival at a checkpoint can do both loading and unloading at a location, or deliver goods at several warehouses at the same location. The process is also supported for rail freight orders.

In practice this means the freight order becomes the working document of the yard and the gate: check-in, door assignment, loading or unloading, goods movement, check-out, all reported on the freight order (see the end-to-end process below).

## Advanced SR connects TM, EWM, Stock Room Management (STRM), MM-IM and Logistics Execution (LE) through a harmonized data model, the EDIFACT standard for EDI messages and dedicated apps; MM and SD are needed to create transportation requirements
H11 states that Advanced SR simplifies communication between TM, EWM, Stock Room Management (STRM), Inventory Management and Physical Inventory (MM-IM) and Logistics Execution (LE). Three means are named:

1. a **harmonized data model**;
2. the **EDIFACT standard** applied to EDI messages;
3. **dedicated apps**, plus expanded existing apps and RF transactions for shipping and receiving.

Information moves between the components so users can see the status of the products during the process. **Materials Management (MM) and Sales and Distribution (SD) are needed to create transportation requirements.**

## The warehouse management applications that can be integrated in the same system: Lean Warehouse Management (inventory at storage location level, needs a placeholder warehouse), Stock Room Management (small or low-complexity warehouses) and EWM; a freight order can contain EWM-managed and IM-managed storage locations
H11 (Storage Location) says the freight order can contain both EWM-managed and IM-managed storage locations, for example at a production location, and the two storage locations can share a loading point. In Advanced SR you can integrate TM with three warehouse applications in the same system:

| Application | Described in H11 as |
|---|---|
| Lean Warehouse Management | A very simple warehouse where inventory management takes place solely at storage location level. You must create a **placeholder warehouse** that ensures the document flow in TM |
| Stock Room Management | For small warehouse operations and warehouse operations with low complexity |
| Extended Warehouse Management | Flexible, automated support for processing goods movements and managing stocks in a warehouse complex |

## Integration based on the freight order does not use the EWM transportation unit (TU) or the EWM vehicle; it can run in parallel with integration based on the EWM TU, and warehouse-driven outbound processes start in EWM
H11 (Integration Based on Freight Order): the Advanced SR process is based on the **freight order** and does **not** use the EWM transportation unit (TU) or the EWM vehicle. The two integration approaches, based on the freight order and based on the EWM TU, **can run in parallel**. For warehouse-driven outbound processes, you start in EWM. The EWM-TU-based integration rests on two objects, the TU on the EWM side and the freight order on the TM side. H11 refers to SAP Note 3289977 for restrictions.

*What the material does not establish:* the reason why Advanced SR chose the freight order over the EWM TU is not stated in the sources read, only the fact. The EWM-TU-based integration has its own sections in H11 that this session does not cover.

## Consignment orders group transportation requirements by criteria such as source and destination location, delivery date and time and business partner; they can be created from inbound messages or manually, serve as the basis of communication between partners, support subcontracting, charge calculation, settlement and tracking but not tendering, and can be assigned to only one freight order at a time
H11 (Consignment Orders; Consignment Order):

- **What it groups.** Transportation requirements (freight units or package units based on sales orders, scheduling agreements or deliveries) with the same source and destination location, the same delivery date and time, and the same business partners (shipper, consignee, carrier). It contains only one linear transportation stage and one shipper and one consignee.
- **Role.** The consignment order gets an ID that serves as a reference between partners, for example a supplier telling the ordering party what will be delivered where and when.
- **What you can do with it.** Subcontracting, charge calculation, settlement with the carrier and shipment tracking. **Tendering is not possible** based on a consignment order. You choose in Customizing (order types) whether such functions run on the freight order or the consignment order.
- **Assignment.** It can be assigned to only one freight order at a time and must be completely assigned. A freight order can contain several consignment orders. It can also be assigned to a transportation unit that contains a matching stage.
- **Creation.** Manually (Create Consignment Order app), from an inbound message such as an advanced shipping notification via EDI, or by automatic consignment building through the consignment building profile. Creation based on top-level packages gives one consignment order per handling unit, with grouping rule TOP_CARGO.

## Decentralized EWM and TM: transportation logistics based solely on an outbound delivery from a sales order, embedded in S/4HANA, with the outbound delivery process either transport-driven or warehouse-driven; only the outbound process is supported, inbound features and Dangerous Goods integration are not, and SAP GTS can be integrated
H11 (Advanced SR for Decentralized EWM and TM): this deployment option is outbound-delivery-based. It lets you conduct transportation logistics solely on the basis of an outbound delivery stemming from a sales order, and it is embedded in SAP S/4HANA. It requires integration between TM and EWM, and EWM integration with an ERP system. The outbound delivery process can be **transport-driven or warehouse-driven**. To manage foreign-trade activities and compliance, you can integrate with SAP GTS.

**Restriction (H11):** only the outbound process is enabled. Inbound features in Advanced SR are not supported, and integration of Dangerous Goods is not supported. Supported ERP systems: SAP ERP 6.0 (EhP7 or higher) and SAP S/4HANA. A setup guide is in SAP note 3225241.

## Prerequisites and master data: the source or destination location (location type 1003, shipping point) must be flagged relevant for Advanced SR, a location of type 1200 (loading point) must be defined, STRM or Lean WM doors must be assigned to EWM doors or loading points when doors are shared (not needed for EWM-only scenarios), and Customizing is done under Integration
H11 (Prerequisites for Advanced Shipping and Receiving) lists the master data you must have before a location can be used:

1. In the location master data, **activate Advanced SR** by flagging the source or destination location (**location type 1003, shipping point**) as relevant for Advanced SR. Mandatory.
2. **Define a location of type 1200 (loading point).** Mandatory.
3. **Assign STRM or Lean WM doors to EWM doors or loading points.** Mandatory for all scenarios with shared doors and multiple warehousing components. Not needed when only EWM is used. For EWM-only scenarios, doors are assigned in the EWM app Assign Storage Bin to Door.
4. Customizing under Integration (for decentralized EWM and TM, under Integration, Logistics Integration, Decentralized EWM-TM Integration; related BAdIs are under Integration, Advanced Shipping and Receiving).

## Detailed organization of loading and unloading: a loading point or unloading point is a location in the master data that represents a group of doors; the app Assign STRM Doors to EWM Doors or Loading Points replaces an STRM or Lean WM door with the assigned EWM door, with the stated restrictions
A loading point or unloading point is defined in the master data as a location and represents a group of doors where goods are delivered or picked up. This gives more control over where trucks load or unload when a large warehouse has several points and doors and uses more than one warehousing component (H11).

The app **Assign STRM Doors to EWM Doors or Loading Points** (H11, Assignment of STRM Doors to EWM Doors or Loading Points):

- If an STRM or Lean WM warehouse and an EWM warehouse share a door in one building, assigning the STRM or Lean WM door to the EWM door makes the system use the EWM door as the main door and **replace** the STRM or Lean WM door with it in the warehouse loading or unloading stop details. If the EWM door already has a loading or unloading point, the EWM point overwrites any existing assignment.
- You can change the assigned door only if it is shared by the same pair of EWM and STRM or Lean WM warehouses.
- You can assign STRM or Lean WM doors to loading or unloading points if they are not already assigned to one.

**Restrictions (H11):** for Lean WM you need a placeholder warehouse with one loading or unloading point and one warehouse door; one STRM or Lean WM door can be assigned to only one EWM door, and one EWM door cannot be assigned to several STRM or Lean WM doors; one loading or unloading point can be assigned to only one STRM or Lean WM door.

## The end-to-end process between customer and supplier: scheduling agreement and schedule lines create freight units, a release sends a call off by IDoc, the supplier creates outbound deliveries and warehouse activities, plans a road freight order and consignment orders, checks the truck in, loads, posts goods movement and sends an advanced shipping notification (ASN); the customer's system creates a consignment order from the ASN and blocked inbound deliveries that are unblocked when the warehouse processing status is set to Ready for Warehouse Processing
H11 (End-to-End Process (E2E) for Advanced Shipping and Receiving) is an example where both customer and supplier use TM. If the systems are not integrated, the inbound or outbound process can be used separately.

**Customer side, inbound, start.**
1. Create a purchasing document in MM (purchase order or scheduling agreement). In the scheduling agreement item you can add a TM loading or unloading point.
2. Create schedule lines. For each schedule line the system creates one or more freight units in TM.
3. Create a scheduling agreement release. The system creates IDocs and sends a **call off** to the supplier's system.

**Supplier side, outbound.**
1. Create outbound deliveries in LE and EWM. The storage location in the delivery defines the kind of warehouse (for example EWM-managed). The TM Status tab of the delivery shows the assigned freight units.
2. Perform warehouse activities: picking and possibly packing, creating handling units or cross-delivery HUs (Load or Unload Freight Orders app). Then the TM process begins.
3. Create a road freight order (Create Road Freight Order or Transportation Cockpit app).
4. Create consignment orders, manually or automatically.
5. **Check-in at the gate** in the freight order. After check-in, assign doors (loading point and warehouse door), load cargo, set the execution status and **post goods movement**, which updates the warehouse system whatever kind it is. The freight order shows an overall status overview on the Advanced SR tab.
6. **ASN.** The system sends an advanced shipping notification, a web service based on the consignment order, from the supplier to the customer. The supplier can also inform the carrier.

**Customer side, inbound.**
1. When the ASN arrives, the customer's system creates a **consignment order** with a reference to the supplier's external order number. Freight units are assigned using criteria such as purchasing reference, supplier or material number.
2. The system can create **inbound deliveries** in LE and EWM; these are **blocked**.
3. Create a road freight order based on the consignment order stage (or automatically when the carrier sends the freight order as a load message). Set Set to Ready for Transportation Execution.
4. At the **gate**, compare the truck's transport documents with the freight order. Packages from EDI messages are fixed automatically (load plan status Finalized). Discrepancies can be corrected directly in the business document. Assign doors and unloading point.
5. After check-in is finished, set the **warehouse processing status to Ready for Warehouse Processing**. The EWM delivery is **unblocked** and warehouse activities such as unloading and goods movement can start.

## Transport-driven versus warehouse-driven outbound process in decentralized EWM and TM: in the transport-driven process the outbound delivery order is blocked until planning is complete and is released when the freight order status changes from In Process to Ready for Warehouse Processing; in the warehouse-driven process warehouse activities come first and the status is set to Ready for Shipping in the EWM outbound delivery order after planning
H11 (Decentralized EWM and TM Outbound Process and Integration; Transport-Driven Execution). Common start: the shipper creates an outbound delivery in LE from a sales order, the ERP system passes it to the decentralized system where EWM creates an **outbound delivery order**, and EWM replicates it to TM, which creates **freight units** from it. TM can then propose a plan. From there, one side leads.

| | Transport-driven | Warehouse-driven |
|---|---|---|
| First step | Transportation planning | Warehouse activities (picking, packing) |
| State of the outbound delivery order | Blocked for processing until planning is complete | Not blocked; the warehouse proceeds on creation |
| What releases / hands over | You change the freight order status from In Process to **Ready for Warehouse Processing**; this releases the delivery order and TM tells EWM | EWM reports the delivery status to TM on completion; after planning you set **Ready for Shipping** in the EWM outbound delivery order |
| Execution | Same for both: set arrival and check-in, load in EWM, set Goods Movement to Goods Issued to report departure | |

H11 (Transport-Driven Execution) adds that the transport-driven process is enabled automatically when a delivery meets the criteria defined in Customizing (warehouse number, shipping point, delivery type), and that the warehouse processing status must be set to Ready for Warehouse Processing manually. E04 states the principle: in the integration between warehousing and transportation one side must always lead the process.

## Warehouse loading stops and warehouse unloading stops: detailed stops with warehouse number, loading or unloading point and warehouse door, derived from predecessor documents or created manually, shown on the Overview tab and in the transportation cockpit, with items packed into different mixed packages when their warehouse number or point differs
H11 (Delivering Goods to Several Warehouses Within a Location). In Advanced SR one road freight order can serve several warehouses at the same location. The detail is carried by the **warehouse loading stop** (source location) or **warehouse unloading stop** (destination location): the exact warehouse number, loading or unloading point and warehouse door the truck must drive to. This is why they are needed: at the gate the driver learns where to deliver, from predecessor documents or on the spot.

- They can be added to road freight orders, consignment orders, freight units and transportation units. All items of a road freight order must be assigned to one.
- The system can **derive** them from predecessor documents (sales order, scheduling agreement), or you create or change them manually on the Loading Details or Unloading Details tab of the Overview. If the planned door is occupied you can enter a new one; the predecessor document is not updated.
- A stop may have substops. You can update derived stops with the door actually used. The Advanced SR tab shows planned and actual details.
- The transportation cockpit shows warehouse numbers, points and doors; with several substops it shows **Multiple**.
- **Package building:** items with different warehouse numbers or loading or unloading points, or none defined, go into different mixed packages.

## Status management in Advanced SR: Warehouse Door Status (Arrived at Door, Departed from Door) and Warehouse Processing Status (Not Determined, Not Started, Ready for Warehouse Processing, In Process, Completed), whose meaning differs between inbound and outbound
H11 (Explanation of Statuses).

**Warehouse Door Status** shows whether a door is physically occupied. It is set manually or automatically at the level of the warehouse loading or unloading stop, and can be reversed if set wrongly.
- **Arrived at Door:** the truck has reached the door, which is now occupied. It can be set only if the door is not occupied, for one stop at a time, and only if the **handling execution status of the stop is Checked In**. The event Arrival at Door is reported. With the Allow Multiple Door Assignments checkbox on a loading point, the occupancy check is skipped.
- **Departed from Door:** loading or unloading finished and the truck has left; the door is available again. It is set automatically if you set the handling execution status directly to Checked Out or Departed. The event Departure from Door is reported.

**Warehouse Processing Status** is from TM's perspective. In the inbound process it controls the **handover of responsibility for the cargo from TM to the warehouse**. In the outbound process it tracks whether cargo is ready to ship; once ready, TM can start loading or follow-on processes such as subcontracting and customs declarations.

| Value | Inbound | Outbound |
|---|---|---|
| Not Determined | Initial value | Initial value |
| Not Started | Truck documents not yet checked against system; warehouse inbound delivery is blocked | Optional, not relevant to TM; planning can start regardless, but waiting for Completed is recommended |
| Ready for Warehouse Processing | Documents match at the gate; set it to transfer responsibility from TM to the warehouse; the delivery is unblocked and changes to items in TM are limited | Optional; same recommendation |
| In Process | Optional; responsibility already handed over | The warehouse is working on the cargo; you can start cargo planning but cannot change items |
| Completed | Optional; warehouse activities such as repackaging are not relevant to transportation | The cargo is ready to ship; **responsibility transfers from the warehouse to TM** |

There are also aggregated values at header level (Partially Ready for Warehouse Processing, Partially in Process, Partially Completed) and **In Transit**, relevant only to stock transport orders. Goods movement can be triggered from TM only after Ready for Warehouse Processing for inbound, and after Completed for outbound (H11, Statuses in the Goods Movement Process).

## The integrated warehouse and transportation execution steps in the Fiori exercise: Set to Ready for Warehouse Processing, create and confirm warehouse tasks, Set to Ready for Shipping, assign a door in the Load or Unload Freight Orders app, Set to Arrived at Door, Set Items to Loaded, Set Stop to Loading Completed, post goods movement, Set to Departed from Door
E04 (Execute an Integrated Warehouse and Transportation Process) is a **transportation-driven** example. Freight order 20000109 has an EWM outbound delivery order (visible in the document flow). The steps and what each reports:

| Step | App / action | What it reports |
|---|---|---|
| 1 | Warehouse Monitor: outbound delivery order is **blocked** (red light) | Transport-driven: warehouse waits for TM |
| 2 | Freight order: **Set to Ready for Transportation Execution**, Save | Planning is complete |
| 3 | Items, Status Management, **Set to Ready for Warehouse Processing** | Responsibility for warehouse handling is released; the block is removed (green light) |
| 4 | Warehouse Monitor: **Create WT in Background**, then **Confirm WT in Background** | Warehouse tasks created and confirmed; packing optional |
| 5 | **Set to Ready for Shipping** | Warehouse process finished |
| 6 | Load or Unload Freight Orders app: select the warehouse loading stop, **Assign Door** (loading point ZLP_ZASR, door YD00) | Door assigned to the stop |
| 7 | **Set to Arrived at Door** (Warehouse Door Status) | Truck is at the door |
| 8 | **Set Items to Loaded** | Item load status turns green; stop status still red |
| 9 | **Set Stop to Loading Completed** (Execution Status) | Stop load status turns green |
| 10 | Goods Movement, **Post** | Goods issue requested; asynchronous, so the posting status is not immediately green |
| 11 | **Set to Departed from Door** | Truck has left the door |

Afterwards the freight order's Execution tab shows arrival, loading and departure events and the Statuses tab shows the freight order **In Execution**, departed from the loading point but not yet checked out, with warehouse processing only partially completed because a second loading stop at another warehouse is still to come.

## Delivery split: TM can split deliveries across Lean WM, STRM and EWM by creating a new delivery with the relevant freight units; it is not possible while warehouse activities run, and at loading, handling units not loaded get a new freight unit and delivery when the stop is set to Loading Completed
H11 (Delivery Split): TM can split deliveries across Lean WM, STRM and EWM in the same system. Splitting creates a new delivery and assigns the relevant freight units to it. If the delivery has only one freight unit, the freight unit is split as well.

1. **Planning.** If you reassign a freight unit from a delivery to a different freight order, a new delivery is needed for the new freight order.
2. **Warehouse activities.** They can start once the status is Ready for Warehouse Processing, and **a split is not possible while they run**. When picking starts the freight unit changes to In Process; when picking, packing and staging are complete the status is **Completed** and a split is possible again.
3. **Loading.** If the truck cannot take all handling units of a delivery, use Load or Unload Freight Orders to select the loaded handling units (Set Items to Loaded). When you **Set Stop to Loading Completed**, the system removes from the freight order every handling unit not loaded and creates **a new freight unit** to which it is assigned and **a new delivery**.

## Delivery deletion in TM: available for LE deliveries in an embedded setup when freight units are delivery-based and unplanned, with 2-step stock transport orders, side-by-side setups and EWM delivery orders excluded
H11 (Delivery Deletion): you can delete LE inbound and outbound deliveries in TM, for example unneeded deliveries in customer and supplier returns. Requirements: an **embedded** setup, deliveries originating in LE, and freight units that are **delivery-based and unplanned**. Excluded for technical and practical reasons: 2-step stock transport orders and side-by-side setups; scenarios with EWM delivery orders and EWM TU-based deliveries are not supported.

H11's scenario: inbound deliveries were created from an external delivery note number, the truck unloads, and a missing note is discovered that the supplier cannot supply. Procedure: in the Freight Units - Worklist app select all FUs of the delivery, choose Delete Delivery and confirm. If an FU is planned, first remove it from the freight order (edit, select the FU, Delete and Save).

## Late changes to capacity documents: items loaded or unloaded but not assigned can be added to the same warehouse stop even after departure; later additions create a document error, and unassignment after check-out requires the stop status Not Loaded and cancelled goods movement, export declaration and customs invoice
H11 (Late Changes to Capacity Documents): a capacity document such as a road freight order can be changed even after execution at the stop has started or finished, to reflect what really happened (for example, an extra pallet was loaded). You add the requirement document to the same warehouse stop, even after the truck departs, for example for charge calculation or settlement with the carrier.

- **Adding.** If the truck has arrived but processing has not started, the new items take the stop's statuses. If you add after loading or unloading, check-out or departure, the new item's statuses do not match the stop and the system creates a **document error** (Document Errors tab). You cannot revoke the stop's status but you can update the new items to match. Inbound example: set the item to Ready for Warehouse Processing (a delivery must be created first, Follow Up, Create Deliveries), set the handling execution status to Unloaded, and post goods movement. For a customs-relevant freight unit, enter the same external delivery note number as another item of the order.
- **Unassigning** after execution has started but before goods movement is posted is possible. After loading is completed and check-out reported, the **stop must have handling execution status Not Loaded**, goods movement postings must be **cancelled**, any export declaration requested or approved must be **cancelled**, and any customs invoice must be **cancelled**. The system then sets the items to Not Loaded and revokes their Loading and Unloading events.

## SAP Event Management integration: tracking of freight units, freight orders, freight bookings, transportation units, resources and instructions; expected events (Scheduled, Loading Begin, Loading End, Departure, Arrival at Destination, Unloading Begin, Unloading End) can be reported from either side, and unexpected events (Delay, Damage) raise alerts in TM
H11 (Integration with SAP Event Management; Tracking of Freight Units). Execution tracking can be done with or without SAP EM; connecting SAP EM adds visibility for shipper, dispatcher, ship-to party and carrier, and a proof of delivery reported by the ship-to party.

| Tracked object | Expected events named in H11 | Unexpected events |
|---|---|---|
| Freight units | Scheduled, Loading Begin, Loading End, Departure, Arrival at Destination, Unloading Begin, Unloading End | Delay, Damage (alert to TM) |
| Freight orders and freight bookings | Loading Begin, Loading End, Proof of Pick-up, Departure, Clear Customs, Arrival at Destination, Unloading Begin, Unloading End, Proof of Delivery | Reported for an item (Discrepancies and Events tab); SAP EM issues an alert on delays |
| Transportation units | Loading Begin, Loading End, Coupling, Departure, Arrival at Destination, Decoupling, Unloading Begin, Unloading End | Delay |
| Resources (trucks, locomotives, trailers, railcars, containers) | Coupling, Departure, Arrival at Destination, Decoupling | Sighting, Damage |
| Instructions | Instruction Execution | None supported |

**Two directions for reporting expected events:** the carrier sends an event message through SAP EM and TM updates the document, or you update the document in TM and TM sends an event message to SAP EM. For freight units the dispatcher receives an alert when an unexpected event such as damage is reported.

Instructions (H11, Tracking of Instructions) are templates from forwarding agreements, copied into forwarding orders and freight units. Each has an alert date and due date and statuses Pending, In progress, Completed, Completed after Due Date, Alert and Overdue; Alert and Overdue are set by SAP EM monitoring.

## SAP GTS integration: compliance checks (embargo, sanction party lists, legal control) and export declarations; the outbound customs activity is based on a consignment or freight order, the inbound one on the freight order; the legal split indicator groups items into freight units and deliveries, and a non-compliant freight unit blocks the delivery for warehouse execution
H11 (GTS Integration in Advanced Shipping and Receiving; SAP GTS Integration for the Outbound Process). SAP GTS performs compliance checks on freight units and freight orders, and export declarations on a consignment or freight order. In the outbound process customs activity is based on the consignment or freight order; in the inbound process, on the freight order.

**Outbound sequence (H11).**
1. Saving a sales order: SAP GTS creates customs documents and runs a trade compliance check, returning an overall status with embargo check, watch list screening and legal control statuses. Each sales document can carry a **legal split indicator**; freight units are grouped so that all items in a unit share it, and deliveries are split accordingly.
2. Delivery created: TM creates freight units; SAP GTS checks all freight unit items. If the check is incomplete or the **freight unit is not compliant, the delivery is blocked for warehouse execution**. The TM Status tab shows planning, execution, delivery and invoicing blocks. In the transport-driven process you must still set Ready for Warehouse Processing manually once compliance is met.
3. Freight order created (and optionally a consignment order): a compliance check runs if activated; blocks appear on the Blocking Information tab.
4. After the stop is **Checked In**, the export declaration process starts for customs groups (considering the legal split indicator), automatically after Set Stop to Loading Completed if so configured. At **Ready for Export Declaration** a request goes to SAP GTS, optionally with customs invoice data. A missing customs clearance can prevent Checked Out. With handling execution status **Cargo Ready for Loading** the requests can go out before the truck arrives.
5. After SAP GTS approves the declaration, TM receives a **customs reference number (CRN)**; then TM can post goods issue and the freight order can be checked out.

**Inbound sequence (H11).** Freight units are checked for compliance, with planning or execution blocks if not compliant. You can set Checked In only if the freight order is compliant. Each consignment order needs a CRN, and an **unloading permission** requested from SAP GTS, before the warehouse unloading stop can be set to Ready for Warehouse Processing. After unloading, customs groups can be set to Ready for Import Declaration once goods receipt is done for all items, then Checked Out.

H11 (SAP GTS Integration in Decentralized EWM and TM) states the decentralized variant supports only the outbound or export process, with compliance checks for freight unit and freight order and export declaration for consignment and freight orders. Integration uses enterprise services (for example Request Export Declaration, Request Trade Compliance Check), over SAP NetWeaver PI or point-to-point.

## Practice
Draw an annotated swimlane (as a table or a drawing) of one outbound delivery from sales order to truck departure. Show the TM, EWM and SAP GTS steps in order, the status that changes at each step, and whether the flow you show is transport-driven or warehouse-driven.

## Self-check
Can I explain to a warehouse manager, without notes, how a truck moves through Advanced Shipping and Receiving from gate check-in to goods movement, and how TM, the warehouse and SAP GTS hand over to each other?
