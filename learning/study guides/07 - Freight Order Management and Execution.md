# Session 07 — Freight Order Management and Execution

## Overview
Planning ends with a freight order or freight booking, and this session follows that document through the rest of its life. You learn what a freight order contains and how it is configured through its type, the ways to create one, how drivers, appointments and carriers are assigned, how the document is sent to a carrier and confirmed, and how its statuses tell you where it stands. You then follow execution: output documents, tracking, delivery creation and splitting, and the warehouse steps from "ready" to goods issue and departure. A dispatcher reads the Statuses tab all day, so knowing exactly what each status value means is the practical goal.

## Freight Order Management creates and edits freight orders (road and rail), freight bookings (air and sea) and trailer units, railcar units, container units and package units, which are used to plan with trailers, railcars and containers; in TM, freight bookings are created for the transportation modes air and sea, freight orders for all other modes
H06 lists the business documents of Freight Order Management and their transportation modes:

| Business document | Transportation modes |
|---|---|
| Freight order | Road and rail |
| Freight booking | Air and sea |
| Trailer unit | Road |
| Railcar unit | Rail |
| Container unit | Independent |
| Package unit | Independent |

Trailer units, railcar units and container units are used to carry out planning with trailers, railcars and containers (H06). S4611 puts the mode rule plainly: for the transportation modes Air and Sea, freight bookings are created in TM, and for all other modes, freight orders. Freight orders represent a single shipment or load departing from one of your facilities (outbound) or arriving in one of them (inbound), and they are the result of planning and the freight document for execution (S4611). H06 notes that you can create freight orders directly or in planning, calculate charges, then perform carrier selection, subcontract directly to a carrier, or perform tendering.

## Freight order management is integrated with master data (a prerequisite), forwarding order management (values copied from forwarding orders or freight units), planning (freight orders are the result of planning and the basis for carrier selection), freight settlement (charge calculation), dangerous goods checks and global trade
H06 (Integration):
- **Master data:** a prerequisite for creating freight orders and freight bookings.
- **Forwarding order management:** the system copies values from the forwarding orders directly, or from the freight units into the freight orders.
- **Planning:** freight orders are the result of transportation planning and serve as the basis for carrier selection. Freight bookings serve as the basis for transportation planning.
- **Freight settlement:** the system can calculate the transportation charges of freight orders and freight bookings.
- **Dangerous goods:** a dangerous goods check can be run for freight orders and bookings.
- **Global trade:** freight orders and bookings form the basis for the integration with global trade.

H06 also states that freight order management integrates with EWM and is part of Advanced Shipping and Receiving, and that freight orders and bookings form the basis for tracking with SAP Event Management.

## A freight order is an order whose execution is planned by a carrier or the shipper and contains the plan for the logistical processing (when and onto which vehicle freight units are loaded), planned departure times and execution data; it is the result of planning and the freight document for execution
H06 defines the freight order as an order for which execution is planned by a carrier or the shipper. It contains the plan for the logistical processing (for example, when and onto which vehicle freight units are to be loaded), the planned departure times of the vehicle, and execution data. It is used primarily for land transportation (road freight order) and rail transportation. You can plan loads, select carriers, and then subcontract directly or first tender. S4611 describes it as the result of planning and consolidating freight units onto a vehicle-booked capacity or scheduled means of transport. Once that is done, transport order execution can be triggered and follow-on settlement processing can begin. S4TM2 repeats the definition.

## A freight order holds planning information (means of transport, stages, routing, planned dates, durations, distances), document dependencies, charges and cost distribution, cargo information, execution information, business partner information (including drivers), output management, status and blocking information and subcontracting information; further: items, communication history, document flow, CO2 emissions, notes and attachments
S4611 and S4TM2 list what freight orders and bookings contain:
- planning information (planned means of transport and stages, routing, planned pick-up and delivery dates, durations, distances);
- document dependencies, with predecessor and successor documents;
- transportation charges and cost distribution;
- cargo information (quantities, weights, goods information);
- execution information;
- business partner information;
- output management;
- status and blocking information;
- subcontracting information.

H06 adds detail on the structure:
- **Items tab** (it replaces the old Cargo tab, which can be restored by personalization): quantities and weights, goods information, corresponding pick-up and delivery freight orders, dangerous goods, seal information, foreign trade information and house bill of lading. Change Hierarchy shows all items or only service items or cargo items.
- **Locations and dates/times:** one-time locations and addresses can be entered at stage level, and the system adjusts stages and assigned freight units. H06 still recommends changing existing locations in the master data.
- **Subcontracting information:** carriers and prices, tendering information, and a freight agreement, version and item (the agreement and version are used for charge calculation, the item for service items).
- **Execution information:** for example actual departure times, and events can be reported directly.
- **Communication history:** inbound and outbound messages with carriers, the carrier's document number and the XML messages.
- **Other:** document flow, CO2 emissions per stage for road freight orders, document references, attachments, notes and change documents.
- **Output management:** requires the settings in the freight order type (for example the output profile).

## Stages are created in the freight unit to split the transportation chain (for example pre-carriage to port of loading, main carriage, on-carriage), so separate freight orders or bookings can subcontract each stage to different carriers; one-time locations can be entered at stage level
S4611 and S48600: freight units can have one or more stages, created to split the overall transportation chain, for example by mode. A freight unit from Germany to the US may be split into pre-carriage from source to port of loading (PoL), main carriage from PoL to port of discharge (PoD), and on-carriage from PoD to destination. Each stage can be used to create a separate freight order or freight booking, so the three stages can be subcontracted to three different business partners. S48600 stresses that stages must be planned at freight unit level before freight orders or bookings are created, because the freight orders relate to individual stages of the split chain. H06 adds that one-time locations can be entered at stage level and that a freight booking can have several pre-carriage and on-carriage stages (these model extra activities such as weighing, not multiple pick-ups).

## The freight order type holds the most important settings: basic settings (shipper and ship-to-party determination, whether subcontracting is allowed, delete or only cancel), charge calculation and settlement settings, execution settings, organizational unit determination, change controller settings, output options and driver settings; a user must select a type when creating a freight order manually
A freight order type defines parameters that influence how the system processes the freight order. When you create a freight order manually you must select a type. If orders are created during planning, the type comes from the Customizing settings and the planning profile (S4611, S4TM2). Settings named in the sources:
- **Basic settings:** determination of shipper and ship-to party, whether the order can be subcontracted, whether it is deleted or only canceled, subcontracting relevance, and the sequence type of stages (S4TM2).
- **Charge calculation and settlement document settings:** enabling charges and settlement, and cost distribution.
- **Execution settings:** for example whether the system performs the execution steps in TM, additional conditions that must be met before Ready for Execution can be set, and integration with SAP Event Management (S4TM2).
- **Organizational unit determination** (next item).
- **Change controller settings:** for example a default change strategy and a condition for change strategy determination.
- **Output options:** an output profile and a text schema.
- **Driver settings:** number of drivers (one or a team), assignment per stage or per order, and whether they can be changed in the order (H06).

S4611 adds that an advanced transportation management license is required if a freight order picks up at (outbound) or delivers to (inbound) multiple shipping or receiving points. It also notes that for scheduling in basic TM only embedded scheduling is allowed.

## Organizational unit determination in a freight document: the system first checks a condition of type /SCMTMS/TOR_ORGUNIT, then the Consider Organizational Unit of User checkbox and the user assignment, and finally the default organization
S4611 (Organizational Unit Determination): the purchasing and execution organizations in freight documents can be determined in the freight order or booking type by a default organization assignment, by user assignment, and by a condition of type /SCMTMS/TOR_ORGUNIT. The order of checks:
1. The system first checks the condition.
2. If there is no condition, or it returns no result, it checks whether the Consider Organizational Unit of User checkbox is selected and whether the user is assigned to a purchasing and/or execution organization.
3. If the checkbox is not selected, or the user has no such assignment, it uses the data maintained as the default organization.

S4TM2 describes the same order. The same determination pattern appears in the freight unit type (see session 06 material).

## The sequence type of stages of a freight order type is Defined and Linear, Non-Linear (Star-Shaped), Disconnected, Star-Shaped Based on FU Stages, Star-Shaped Based on FU Stages (Reversed), Linear with (De-)Consolidation Stages or Undefined; freight bookings allow only sequential stages
S4TM2 lists seven sequence types (S4611 lists the first five):

| Sequence type | Meaning |
|---|---|
| Defined and Linear | A single start stage and a single end stage. All other stages have one predecessor and one successor. |
| Non-Linear (Star-Shaped) | All stages share the start location but have different end locations. |
| Disconnected | All stages are separate, each with its own start and end location. |
| Star-Shaped Based on FU Stages | Based on freight unit information, same start location, different end locations (for example parcel orders or customer pick-up). |
| Star-Shaped Based on FU Stages (Reversed) | Same end location, different start locations (for example customer self-delivery). |
| Linear with (De-)Consolidation Stages | Three parts: a pre-carriage star with different starts and one consolidation location, a linear main carriage, and an on-carriage star from one deconsolidation location to different ends. |
| Undefined | No stages, only locations. |

S4TM2 states that freight orders allow star-shaped, unrelated and other stage structures, whereas freight bookings allow only sequential stages. H06 (Freight Orders with Non-Linear Stages) says such orders can only be created with customer-specific functions or ERP shipments, cannot be created from a forwarding order, cannot be planned, and allow freight settlement documents per stage. Rail freight orders do not support non-linear stages (H06).

## Freight orders can be created manually, from an inbound EDI message (service interface TransportationOrderGenericRequest_In), from transportation planning (manual planning, VSR optimization, background planning, or New in the cockpit), directly from a freight unit (one order per stage or for consecutive stages), by copying and from a schedule (report /SCMTMS/MP_SCHED_CREATE_TOR); S4611 describes manual creation, copying and creation through the Transportation Order Generic Request web service
H06 (Creation and Editing of Freight Orders) lists the options:
- **Manual creation** (Create Road Freight Order or Create Rail Freight Order app).
- **Inbound message:** a business partner sends the freight order by EDI via service interface TransportationOrderGenericRequest_In. If the inbound order contains errors, it is usually still saved and the errors appear on the Document Errors tab for correction. H06 also mentions external planning with a carrier (B2B), where freight units go to the carrier by EDI and freight orders come back.
- **Transportation planning:** manual planning, VSR optimization and planning in the background create freight orders. You can also choose New in the transportation cockpit, for example for a trailer.
- **Direct creation from a forwarding order business document** (see the direct creation item).
- **From the freight unit:** one freight order per transportation stage, or consecutive stages grouped in one order.
- **Copying** (next item).
- **From a schedule:** report /SCMTMS/MP_SCHED_CREATE_TOR.

S4TM2 names ways: manually, from the freight unit worklist (source and destination are populated), copying, the FUB rule (shortcut), and the advanced ways (cockpit, VSR optimization, transportation proposals). S4611 describes manual creation, copying, and the Transportation Order Generic Request web service (see SAP note 2474539) for inbound and outbound exchange of freight orders or bookings.

## Creating a freight order by copying takes over header and logistical data but not references to freight units or execution information; a different freight order type may be chosen only if the sequence type of stages and the setting for customer self-delivery or pick-up match
H06 (Creation by Copying), S4611: the system copies header data and logistical data, but not references to freight units and execution information. You can create several copies at once. You may enter a different freight order type for the copy, for example copy a road freight order of type Freight Order with Subcontracting into one of type Freight Order with Internal Processing executed by your own trucks. When the type differs, two settings must match: the sequence type of stages (a linear order cannot be copied into a non-linear type) and the setting for Freight Order for Customer Self-Delivery or Pick-Up.

## Manual creation process: enter general data (shipper, consignee, carrier, resources, locations, dates, driver, terms of payment), optional intermediate stops, items (insert freight units or enter items directly), optional charge calculation, check and save (consistency, capacity and dangerous goods checks), send to the carrier (Subcontracting, Send to Carrier), confirm or reject on behalf of the carrier, send loading and unloading instructions, print, fix the order against background processing and create the freight settlement document after execution
H06 (Manually Creating Freight Orders) gives an example for a regular customer and carrier. Open Create Road Freight Order (or Create Rail Freight Order) and proceed:
1. **General data:** shipper, consignee, carrier, used resources, locations and dates/times, schedules, driver, terms of payment, notes.
2. **Intermediate stops** (optional): Overview tab, Insert, Location.
3. **Items:** add freight units (Overview tab, Insert, Freight Unit), or enter items directly under Freight (for example empties). You can also build packages.
4. **Charges** (optional): calculate expected charges. The Mass Cost Calculation Report for Freight Orders handles several orders. Item level charge calculation is not supported for a freight order with consignment orders as items.
5. **Check and save:** consistency check, plus capacity and dangerous goods checks.
6. **Send to the carrier:** Subcontracting, Send to Carrier. On subcontracting the system recalculates charges. If they differ from the earlier ones, it cancels subcontracting, and you must check and adjust the charges, then resend.
7. **Confirm or reject** in the name of the carrier, or by message.
8. **Loading and unloading instructions** to the warehouse (message-based communication with a warehouse management system).
9. **Print** the print documents.
10. **Fix** the order to protect it against changes from background processing (planning runs or carrier selection).
11. **Freight settlement document** after execution, the basis for checking the invoice or issuing a voucher. For an Additional Agreement Party partner the system creates settlement documents automatically.

A variant: enter only the general data, open the transportation cockpit, assign freight units and do all further planning steps there (charges, carrier selection or tendering). S4611 describes the same process.

## Direct creation of freight orders: on saving, a freight order is created directly from a forwarding order or transportation requirement if the document is subcontracted, not consolidated, deliverable in one freight order without pre- or on-carriage and has one source and one destination; the trigger is the document type, document attributes or quantity (via a FUB rule and conditions) and no further freight units can be added
H06 (Direct Creation of Freight Orders): when an FWM business document (forwarding order, order-based or delivery-based transportation requirement) is saved, a freight order is created directly if:
- the document is subcontracted and not consolidated with other FWM documents;
- it can be delivered in one freight order, so there is no pre-carriage or on-carriage;
- it has only one source location and one destination location.

Three triggers:
- **Document type:** a FUB rule is found that assigns a freight order type, for example for a forwarding order type that is subcontracted directly.
- **Document attributes:** a condition determines the freight order type from attributes such as the ERP document type.
- **Quantity:** the total quantity exceeds the truck size, the split quantity splits it into several freight units, and a condition converts a freight unit of truck size into a freight order.

You cannot add further freight units to such directly created freight orders (H06). This is the shortcut scenario from session 06.

## Freight orders can be created without a forwarding order and the forwarding order created later, which is recommended for customer self-delivery (items known after the truck is unloaded) and collective goods traffic (items known when the truck arrives)
H06 (Creation of Forwarding Orders from Freight Orders) recommends creating the freight order first in two scenarios:
- **Customer self-delivery:** a customer truck enters the yard, and you cannot tell what it carries until it is unloaded. You create the freight order and enter the items after the truck has arrived.
- **Collective goods traffic:** your own truck travels a route daily and collects goods. You can create the freight order with the main data before arrival but cannot create the items until the truck arrives.

Prerequisites: a shipper and a consignee on the freight order item, and item types assigned to the forwarding order type. From the Items tab, choose Create Forwarding Order. The shipping type of the forwarding order type must correspond to the selected items (with LCL you cannot select container items). The movement type must match: for customer self-delivery the first stage type in the sequence must be Customer Self-Delivery, for collective goods traffic it must be Pre-Carriage. The system creates the forwarding order, freight units and stages, and connects the first stage of the freight unit to the freight order.

## Editing and displaying: the Freight Orders (worklist) app with queries such as All Road Freight Orders, Create/Edit Road Freight Order and Create/Edit Rail Freight Order, and the transportation cockpit, which shows freight orders only if they match the selection profile for freight orders and freight bookings; tabs include General Data, Items, Overview, Subcontracting, Document Flow, Charges, Cost Distribution, Execution, Statuses, Output Management and Communication History
H06 names the apps: Freight Orders (the freight order table or worklist), Edit Road Freight Order and Edit Rail Freight Order, and the Transportation Cockpit app. In the cockpit, freight orders appear only if they match the criteria of the selection profile for freight orders and freight bookings.

E03 (Explain Transportation Documents) shows the worklist with the query All Road Freight Orders. Opening an order shows the General Data tab (cargo, utilization, distances and durations, addresses and dates, CO2 emissions with calculated versus reported values) and other tabs. Tabs used elsewhere in the sources: Items, Overview, Subcontracting (carrier ranking), Document Flow, Charges, Cost Distribution, Execution, Statuses, Output Management and Communication History.

## Freight bookings reserve freight space on a vessel or aircraft (ocean and air freight bookings with mode-specific data such as vessel name or flight number), are consumed by assigning freight units or container units and can be created manually, from a worklist or by copying; drivers cannot be assigned to bookings, all booking types can be subcontracted and only carrier selection (not tendering) is offered
S4TM2 (Freight Bookings) and H06:
- A freight booking reserves freight space on a vessel or in an airplane, and is also the document for the actual execution (H06). Ocean and air freight bookings carry mode-specific data such as vessel name or flight number. The space is consumed by assigning freight units or container units.
- An ocean freight booking covers port of loading to port of discharge, an air freight booking airport of departure to airport of destination. Bookings can cover a consolidation location before the source and a deconsolidation location after the port (container freight stations for ocean, gateways for air).
- Creation: manually, from a worklist, or by copying (S4TM2). H06 adds creation from a forwarding order, the cockpit, the freight unit, and a schedule.
- Differences from freight orders (S4TM2): pick-up and delivery freight orders can be created for the stages to and from the consolidation locations. Drivers cannot be assigned. Bookings allow only sequential stages. Self-delivery and self-pickup are not relevant. All booking types can be subcontracted, while freight order types can forbid subcontracting. Only carrier selection is possible for bookings, not tendering, because in most scenarios the carrier is already known when the booking is created.
- Capacity requirements: for air and ocean you may need to reserve capacity before planning, for example by entering equipment type, equipment group and container count (H06).

E03 (Create an Ocean Freight Booking) shows a booking of document type BST1. You assign a schedule departure (here from PORT-DEHAM to PORT-CNSHA), insert a capacity requirement (three 20-ft containers of type 20G0 and two 40-ft containers of type 42G0), and save, which creates one container item per container. The Verified Gross Mass can be recorded on the Quantities tab. Booking confirmation status starts as Not Sent to Carrier, moves to Sent to Carrier with Subcontracting, Send Booking, and can be set to Confirmed by Carrier manually.

## Rail freight orders model a train with locomotives (vehicle resources, only the main locomotive at header level is considered in planning) and railcars (passive vehicle resources, individual items or multi-items) to which cargo items are assigned; schedules can be assigned at header or stage level and non-linear stages are not supported
H06 (Rail Freight Order): a rail freight order models the logistical processing of transports with trains, with one or more locomotives and railcars. You can execute it yourself or subcontract it.
- **Locomotives** are vehicle resources. Several locomotives can be modeled as multi-items, but planning considers only the main locomotive entered at header level. The others are ignored in scheduling and incompatibility checks.
- **Railcars** are passive vehicle resources. Railcar items come from assigned railcar units or are created directly in the order (simpler scenarios), singly or as multi-items. Cargo items are assigned to the railcars.
- Settings are in the freight order type. You can select a carrier and award the order as a subcontract. Schedules can be assigned at header or stage level, and after a schedule is assigned, default routes can no longer be applied.
- Non-linear transportation stages are not supported.
- Number of railcars: the actual number is shown. If scale prices are agreed with the carrier, you can enter the number for the scale as rating value once the carrier agrees. H06 example: nine available railcars but a tariff for ten.

## In rail scenarios the invoicing carrier invoices the shipper or bill-to party for its stages (rule 11 in North America); carriers can be assigned by stage, the Default Route function proposes routing options from default routes, freight agreement items and rate tables sorted by price, and one freight settlement document is created per invoicing carrier
H06 (Rail Freight Order, Rail Transportation):
- The **invoicing carrier** invoices the shipper, or another designated bill-to party, for the charges calculated for the corresponding stages. This is common in North America, known as "rule 11". In rule 11 scenarios the electronic bill of lading goes to just one carrier, usually the one for the first or last main stage, which sends routing instructions to all invoicing and executing carriers.
- **Assigning carriers by stage:** different carriers per stage and several invoices per rail freight order. One carrier accepts the actual order, but all involved carriers submit invoices for their stages. The invoicing carrier level states whether the carrier at header or stage level is used for settlement. Each stage is classified as pre-carriage, main carriage or on-carriage.
- **Default Route** (pushbutton): the system finds default routes whose first and last locations match the source and destination rail locations, then freight agreement items for each executing carrier (filtered by trade lanes and commodity codes), then rates in the rate tables. It proposes routing options sorted by price, with alternatives if several invoicing carriers apply. After you select one, it generates the stages with stage types, executing carriers, invoicing carriers and freight agreement items.
- **Settlement:** with a different invoicing carrier per stage, the system creates one freight settlement document for each carrier.

Compared with a road freight order, where one carrier is subcontracted and normally one settlement follows, the rail case can split invoicing across stages and carriers.

## Setting the cargo execution status of a railcar multi-item adjusts all subitems and cargo items, and loading single cargo items sets the multi-item to Cargo Partially Loaded and then Cargo Loaded
H06 (Rail Freight Order, Status): on the Items tab (hierarchy Cargo Management for All Locations, mode Rail) you can set handling execution status of cargo and cargo execution status of railcars.
- Setting Cargo Loaded for a **multi-item** sets the cargo execution status of all subitems (railcars) to Cargo Loaded and the handling execution status of all assigned cargo items to Loaded.
- Setting a cargo item to Loaded updates the railcar and the multi-item. With a multi-item of two railcars, each with a cargo item, setting the first to Loaded gives the railcar Cargo Loaded and the multi-item Cargo Partially Loaded. Setting the second gives the second railcar and the multi-item Cargo Loaded.
- For a **single item**, setting a cargo item to Loaded sets the railcar to Cargo Loaded, and vice versa.

## Drivers (road freight orders and trucks only) are business partners with validity, non-working times and absences; a default driver can be linked to a vehicle resource; the freight order type defines one driver or a driver team, assignment per stage or per order and whether this can be changed; the system checks overlaps and availability and sets the Driver Assignment Status (Not Relevant, Underassigned, Fully Assigned, Overassigned); drivers not in master data can be entered with No Master Data Defined
H06 (Use of Drivers in Freight Order Management) and S4TM2 (Driver Management):
- Supported for road freight orders and trucks only. Drivers are business partners (S4TM2: role TM Labor Resource), not resources. Their properties include validity, absences (sickness, vacation), non-working times, qualifications, home location, org unit and last planned location and availability (S4TM2).
- A **default driver** can be assigned to a default vehicle resource (Transportation tab of the resource master). If the resource is used in a freight order and no driver is assigned yet, the driver is copied.
- The **freight order type** says whether one driver or a driver team (two drivers per stage) is assigned, whether drivers are assigned per stage or per order, and whether this can be changed in the order. The number of required drivers must be set for the driver fields to show.
- **Checks on save:** a driver must not be assigned twice to a stage or to two overlapping freight orders, and validity and availability within the order time frame are checked. You can also run them via Check, Document or Resources.
- **Driver Assignment Status** (H06, set automatically at header level from required versus assigned drivers): Not Relevant, Underassigned (at least one stage has too few drivers), Fully Assigned (all stages have the required number), Overassigned (all stages have too many).
- **Drivers not in master data:** select the No Master Data Defined checkbox on the Drivers tab, then Edit Deviating Address in the Actions column. Useful when a driver is only entered at check-in or check-out, or is not employed by you. Qualifications are not shown for these drivers, and the Freight Orders (Worklist) app can search for orders with them.
- Drivers can be assigned on the General Data, Overview and Drivers tabs.

## A driver team (two drivers who take turns driving and sleeping) is recommended for time-critical orders such as rush orders, while a driver assigned per transportation stage means only one driver is in the cabin at a time; in the cockpit drivers can be assigned by drag and drop, by manual entry or through the Assign Driver dialog
H06: assigning a driver team is recommended for time-critical orders such as rush orders, with two drivers in the cabin taking turns driving and sleeping. Assigning a driver to the entire freight order means this driver covers source to destination. Assigning drivers to individual stages means a driver covers some stages and another takes over, so only one driver is in the cabin at a time.

S4TM2 (Automatic Assignment of Drivers): automatic assignment happens if the freight order type requests driver assignment and the driver is the default driver in the resource master of the vehicle. In the cockpit you can assign drivers manually by drag and drop (to the order, or to stages in the road freight order hierarchy if assignment is per stage), by entering them in the Driver column, or through the **Assign Driver** pushbutton, where you choose whether to replace or add to the current drivers. In the manual planning settings, default truck handling defines whether the default truck of a driver is ignored or used if no other truck is assigned.

## Appointments for freight orders are defined on the Overview or Stages tab or in the cockpit; the acceptable start of loading and acceptable end of unloading of freight units must lie within the appointment, otherwise an error is raised; scheduling a freight order adjusts departure and arrival times and derives loading and unloading times of the freight units, and changes to dates propagate between forwarding order, freight units and freight order, with an execution block if the order is already in execution
**Appointments** (H06): time windows you define in the freight order for when delivery or pick-up at the customer is to happen, with start and end times. A carrier's appointment from its tendering response is also shown. The appointment is a hard constraint for scheduling: the system compares acceptable and requested times of the freight units with it. The acceptable start of loading and the acceptable end of unloading must lie within the appointment, or an error message is generated. The acceptable end of loading and acceptable start of unloading may lie outside it. You define appointments on the Overview and Stages tabs by double-clicking a stop, or in the cockpit for road freight orders. H06 example: loading appointment 10:00 to 13:30 on day 1 and unloading 11:00 to 14:30 on day 2. FU1 breaks both, FU2 fits both.

**Scheduling of freight orders** (H06):
1. Enter requested and acceptable dates in the forwarding order (optional, the system can determine them during scheduling).
2. On save, freight units are created, and dates are copied per the freight unit type settings.
3. When a freight order is created, the dates are copied as planned departure and arrival.
4. You may add cut-off and availability dates, and appointments.
5. Scheduling adjusts departure and arrival and determines loading and unloading dates of the freight units under a set of constraints. Transportation duration comes from distance and duration determination. Loading and unloading durations come from the planning profile or a condition. Schedule-based orders ignore loading and unloading durations. The user parameter /SCMTMS/SCH_FORCE can force automatic forward scheduling after changes.

**Date propagation** (H06): the system takes dependencies between freight unit stages and freight orders into account even without scheduling, and sets the cross-document check status if dates conflict. Changed requested or acceptable dates in the forwarding order are copied to freight units, and also to the freight order if it is not yet in execution. If the order is already in execution, the system sets an execution block when dates conflict. Changed planned dates in the freight order update loading and unloading dates in the freight unit. The change controller defines how the system reacts to changes.

## Carrier assignment: the carrier is the business partner the freight order is subcontracted to and can differ from the executing carrier; manually a carrier is entered in the freight order or assigned by Mass Change from the worklist; automatically through the default route, the partner function SP (Forwarding Agent) in the delivery, the partner determination profile of the freight order type (fixed partner or BAdI) or a process controller strategy
S4611 (Subcontracting to Carriers): the carrier is the business partner you subcontract to. It can differ from the executing carrier (another partner role) if the carrier subcontracts execution to a third party.

**Manual:** enter the carrier in the freight order (General Data tab, Transportation, Carrier), or select freight orders in a worklist and use Mass Change (E03: Mass Actions, Mass Change, enter the carrier, refresh).

**Automatic options** (S4611):
1. Assign the carrier to the default route, so it is added to the freight unit during building by the FUB rule.
2. Pass the carrier from the delivery to the freight unit by maintaining it with partner function SP (Forwarding Agent) in the delivery.
3. Take the carrier from the partner determination profile assigned to the freight order type, with a fixed business partner for role Carrier.
4. Use a BAdI through the partner determination profile (custom code).
5. Use a process controller strategy, for example a creation strategy, assigned to the freight order type (custom code).

Carrier selection (session 06) is the other automatic route: it creates a ranking and can assign the highest-ranked carrier (E03).

## Sending to the carrier: Subcontracting then Send to Carrier sends TransportationOrderRequest_Out, the carrier confirms via TransportationRequestConfirmation_Out and the shipper receives it with TransportationOrderConfirmation_In; the Communication History tab lists all messages including the XML; on subcontracting the system recalculates charges and cancels subcontracting if they changed
H06 (External Communication in Overland Transportation) describes sending freight orders directly to a carrier without tendering. Prerequisites: your sending system and the carrier's receiving system are configured, as is the XI system.
1. Subcontracting, Send to Carrier: the sending system sends the order with service operation TransportationOrderRequest_Out.
2. The receiving system gets it as a forwarding order via TransportationRequestRequest_In.
3. The receiving system confirms via TransportationRequestConfirmation_Out, to accept (possibly with changes) or reject.
4. The sending system receives the confirmation via TransportationOrderConfirmation_In.
5. The sending system can cancel via TransportationOrderCancellationRequest_Out.

The same operations can be used in direct tendering. The Communication History tab lists all inbound and outbound messages. In E03 (Assign Carriers to Freight Orders) and E04 (Generate Outputs) you reach the XML message through the Request to Carrier entry on that tab. As noted in the manual creation process, subcontracting recalculates the charges and cancels subcontracting if they changed.

## Freight order statuses: life cycle (New, In Process, Complete, Canceled), driver assignment, planning (Not Planned, Partially Planned, Planned and more), subcontracting (No Subcontracting Result, In Tendering, Carrier Assigned, Sent, Changed After Sending), confirmation (No Confirmation Yet, Invalid Confirmation Received, Rejected, Confirmed, Confirmed with Changes and more), tendering and execution; in the exercise, assigning a carrier gives In Process, Carrier Assigned and Not Started, sending gives Sent and No Confirmation Yet, and Set to confirmed by carrier gives Confirmed
H06 (Explanation of Statuses) describes how they are set:

| Status | Values and meaning |
|---|---|
| Life cycle | **New**: created but not yet considered in planning and execution. **In Process**: planning, execution, subcontracting or invoicing started (Customizing can set it right after creation, required for documents resulting from planning). **Complete**: execution finished and invoicing status Completely Invoiced or no invoice expected (set automatically, or manually from In Process). **Canceled**: planning and execution canceled, can be set manually with Cancel Document. |
| Driver assignment | Not Relevant, Underassigned, Fully Assigned, Overassigned (see the drivers item). |
| Planning | From the stages: **Not Planned**, **Partially Planned**, **Planned**, Not Ready for Planning, Not Published. A single stage can be Unplanned, Planned, Planned with conflict between FU and freight order/booking times, or Not Ready for Planning (missing location, planning block set automatically). |
| Subcontracting | Set automatically, only for subcontractable documents. **No Subcontracting Result**: no carrier. **In Tendering**: tendering in process. **Carrier Assigned**. **Sent**: sent to the carrier (needs Carrier Assigned first). **Changed After Sending**: a relevant change after sending (quantities, dates/times, source, intermediate stops or destination locations, transportation service level). |
| Confirmation | Set automatically (only if subcontracting status is Sent) or manually. **No Confirmation Yet**, **Invalid Confirmation Received** (cannot be interpreted), **Rejected**, **Confirmed**, **Confirmed with Changes**, **Update Sent, No Confirmation Yet**, **Document Changed After Confirmation**, **Document Changed After Rejection**. |
| Tendering | For tendered documents (subcontracting status In Tendering): Not Published, Published, Review Required, Completed. |
| Execution | Next item. |

**Exercise path** (S4611 Exercise 6, E03):
- After assigning carrier CAR_TM3_##: life cycle In Process, subcontracting Carrier Assigned, execution Not Started.
- After Subcontracting, Send to Carrier and save: subcontracting Sent, confirmation No Confirmation Yet, life cycle In Process, execution Not Started.
- After Subcontracting, Set to confirmed by carrier and save: subcontracting stays Sent, confirmation Confirmed.

E03 shows the same path (Carrier Assigned, then Sent with No Confirmation Yet, then Confirmed). S4611 adds that in basic TM only manual award confirmation is supported as part of tendering.

Because the statuses are separate fields, they change independently. For example, a freight order can be Confirmed while its execution status is still Not Started.

## Execution status values: Not Started, Capacity Planning Finished, Loading in Process, Ready for Transportation Execution, Not Ready for Transportation Execution, In Execution, Executed, Interrupted, Canceled, Not Relevant; it is set automatically for documents subject to tracking or manually, and a last expected event can set Executed automatically
H06 (Execution Status): set automatically for documents subject to tracking (the tracking relevance is set in Customizing of the document type), and can be set manually. Values:
- **Not Started** (MAWB Open for air): execution has not started.
- **Capacity Planning Finished**.
- **Loading in Process**: loading started.
- **Ready for Transportation Execution** (MAWB Finalized for air): execution can start, that is loading finished or a carrier accepted the order. Customizing can enable automatic derivation when the first execution-relevant event is reported or the first stop's execution status is updated. A document with MAWB Finalized can no longer be planned.
- **Not Ready for Transportation Execution** (MAWB Not Finalized): the readiness check failed or you set it manually.
- **In Execution**: execution started. Customizing can set this right after creation.
- **Executed**: execution finished. If the type is relevant for execution tracking, H06 recommends specifying a last expected event, which sets Executed automatically when reported.
- **Interrupted**, **Canceled**.
- **Not Relevant**: the type is not relevant for execution tracking. Set automatically and never changes.

## Handling execution status is set on item level (Not Determined, Not Unloaded, Unloaded, Not Loaded, Loaded, and for trailer or railcar units Coupled, Uncoupled and their negatives) and on stop level (for example Cargo Ready for Loading, Arrived, Checked In), and the cargo execution status of containers and railcars follows it
H06 (Handling Execution Status), set automatically or manually:
- **Item level** (cargo items at the current stop: product, package or container): Not Determined (initial), Not Unloaded, Unloaded, Not Loaded, Loaded, and for passive vehicle resource items only Not Coupled, Coupled, Not Uncoupled, Uncoupled.
- **Stop level:** progress of execution activities at a stop, for example Not Determined, **Cargo Ready for Loading** (goods ready, warehouse processing status Completed; Cargo Not Ready for Loading reverts it), **Arrived**, **Checked In** (documents of arrived goods match, the truck may drive to the yard; setting it first sets Arrived automatically), Loaded, Partially Loaded, Unloaded, Partially Unloaded, Departed.
- In the inbound part of Advanced Shipping and Receiving, Set Items to Unloaded sets items to Unloaded. In the outbound part, Set Items to Loaded sets items at the warehouse loading stop to Loaded.
- **Links:** when all cargo items are loaded into a container, the container's cargo execution status becomes Cargo Loaded. Item Loaded sets the stop to Loaded (all) or Partially Loaded (some), and Unloaded works the same way. Setting the stop to Loaded or Unloaded sets all items. A stop set to Loaded or Partially Loaded sets the header execution status to Loading in Process, and Departed sets it to In Execution. The stop-level execution status is green only if the handling status is Unloaded.
- Departed on an outbound stop also sets the cargo receipt status of items to Picked Up, and earlier outbound stops to Departed (H06).

**Source difference.** S4611 Exercise 8 sets the freight order's Execution Status to Loaded and shows execution status Ready for transportation execution plus a logistical execution status "SP_1010 Loaded with timestamp". H06 describes the stop-level link as Loaded setting the header to Loading in Process. The two describe different actions, so check the system before relying on either sequence.

## Transportation execution in (basic) TM: the freight order is the central document until the vehicle has left the loading location and for status tracking afterwards; actual quantities and discrepancies can be recorded, loading status maintained manually, local events monitored on the Execution tab, external events reported through the TOR_GENERIC web service, local container or package items and seal data maintained on the Items tab
S4611 (Describing Freight and Transport Execution): in basic TM, the freight order is the central document with all execution-relevant information until the vehicle has left the loading location and for status tracking even after departure. Before and during execution you can create documents related to cargo movement and compliance, document actual quantities and details, record discrepancies between order and execution, and record the loading status manually. Execution is monitored on the Execution tab using local events. These are not integrated with SAP Event Management in the basic scope. External events can be reported via the TOR_GENERIC web service. The web service TransportationEventBulkNotification into Global Track and Trace can be used in basic TM only if LBN is licensed, and milestone tracking is supported via LBN. On the Items tab you can create local container or package items, create cross delivery handling units manually by assigning several freight units to one package item locally, and maintain seal data.

## Output management creates print and other outputs for freight units, freight orders, freight bookings, freight agreements and freight settlement documents; the output profile in the document type maps to a PPF action profile (for example /SCMTMS/TOR_PRINT_ROAD with CMR, waybill, packaging labels), and PPF answers what (action definition), why (scheduling condition) and when (starting condition); PPF actions only process data already saved to the database
S4611 (Creation of (Print) Freight Documents): output management automates printouts, mail or fax in response to events. It is available for freight units, freight orders, freight bookings, freight agreements and freight settlement documents.
- **Profiles:** output profiles in the document type Customizing map to **action profiles** of the Post Processing Framework (PPF), under application /SCMTMS/TRANSPORTATION. Example: output profile /SCMTMS/TOR_PRINT_ROAD, whose action definitions include documents such as CMR, waybill and packaging labels. For the parcel manifest and label, H06 requires output profile /SCMTMS/TOR_LBL_PRINT in the freight order type.
- **Action definition = what.** It defines what is done (mail, fax and so on) and the processing type (trigger alert, method call, workflow, Smart Form action, external communication, BI data upload).
- **Scheduling condition = why.** It is checked during PPF action determination and decides whether an action should be executed, for example life cycle of the predecessor is X or the document is canceled.
- **Starting condition = when.** It is checked just before execution and only affects the point in time, for example on save or one day before pick-up.
- **Capabilities:** rule-based automatic dispatch, preview and manual output in the UI, archiving of dispatched output, and mass output from a worklist.
- **Caution:** PPF actions can only process information already saved to the database, which prevents preliminary labels from being sent to a spool.

E04 (Generate Outputs for Freight Orders): on the Output Management tab of the road freight order, an output such as the Road Waybill (Europe) can be opened with Action Details and Document Preview as a PDF with order number, carrier, shipper, consignee and materials. On the Communication History tab you open the Request to Carrier with its XML message.

## Tracking and event handling: SAP Event Management (on-premise capable) and SAP Business Network Global Track and Trace (cloud, separately licensed) monitor freight units, freight orders, freight bookings, transportation units and resources; event types are regular, overdue, unexpected and unreported
S48600 (Freight Order Execution): two tracking solutions are named. **SAP Business Network Global Track and Trace** is a cloud solution that must be licensed separately. **SAP Event Management** is also available on-premise and can run on the same SAP S/4HANA system as TM. Tracking is provided for freight units, freight orders, freight bookings, transportation units, resources, and instruction execution for standard operating procedures. The aim is management by exception. Event Management is built around monitor, notify, analyze and adjust.

Event types, comparing what is expected with what happens:
- **Regular:** expected within a time frame and happens as expected.
- **Overdue:** expected within a time frame but occurs outside it, and can cause later events to be rescheduled or recorded as overdue.
- **Unexpected:** for example a truck breaking down, which can trigger an alert or other action.
- **Unreported:** expected but not reported, so you can set a time limit that triggers a message or action.

S48600 gives an example: a delay signal during loading triggers an alert and the planner adjusts the schedule. SAP Business Network Global Track and Trace is integrated with TM to synchronize business objects and milestone updates.

## Delivery creation can be triggered in TM: TM creates delivery proposals from freight units, freight orders and bookings (dates from the freight order or booking, quantities from the freight units), sends them to the ERP system, and the delivery builder, a background report /SCMTMS/DLV_BATCH, worklists or the cockpit after planning can trigger it; freight units are consolidated into one proposal only if, for example, source, destination, Incoterms and shipping conditions match
S48600 (Delivery Creation): deliveries are created in SAP S/4HANA or SAP ERP, or triggered from TM. Triggered in TM, the solution makes it possible to combine and plan multiple orders in TM and create a single delivery and transport.
- **Proposals:** TM generates proposals based on dates and quantities from planning results, considering resource availability and transportation durations. It can also trigger delivery creation before planning. After sending, the application log has an entry and freight units get a send timestamp. ERP creates the deliveries, may split them further, but does not change TM's dates or consolidate proposals. TM sets a confirmation timestamp on the freight units when the confirmation arrives and raises an alert on errors.
- **Triggers:** the background report /SCMTMS/DLV_BATCH (selection criteria or selection profile, plus an optional delivery profile), the Delivery Builder app (profiles, review proposals), worklists (OTR, freight unit, freight order, ocean/air freight booking), the freight order UI, or the cockpit after planning.
- **Data sources:** dates from the freight order or booking, or from the freight units if unplanned. Quantities from the freight units. Document references from the order or order-based transportation requirement.
- **Consolidation:** with planned freight units, each proposal uses only one freight order or booking. Freight units can be in the same proposal only if source, destination, Incoterms, shipping conditions, ERP document type, and (if planned) start and destination stops are the same, plus the ERP system in side-by-side scenarios. If order combination is not allowed for an order-based demand, its freight units are not grouped with others.

E04 (Create Deliveries): in the Delivery Builder, three delivery proposals were created for four freight units, because two freight units with the same destination were combined. Creating the deliveries produced three deliveries, and one outbound delivery order was created in EWM.

## Delivery changes and splits: changed planning dates can update the outbound delivery, and if freight units of one delivery are planned on different freight orders the delivery is split automatically (only when the first or last stage of the chain is affected, and only for outbound deliveries from TM); in the exercise the system created two deliveries after the second freight order was saved
S48600 (Delivery Change and Split):
- **Changes:** if a delivery is changed or deleted in ERP, TM adjusts the freight units. TM can update goods issue date, loading date, transportation start date and delivery date of the outbound delivery from changed planning dates, if the delivery status still allows it. TM can trigger updates of outbound deliveries only, not inbound.
- **Split:** a split is required when freight units of one delivery are assigned to different freight orders, or only some are assigned to freight orders, and only if the first or last stage of the transportation chain is affected. TM creates a new outbound delivery for the split-off items and adapts the original. It first reassigns the freight units to the new delivery, then decides whether planning of the new or original freight units is kept or discarded. The delivery must still be changeable by its status.

E04 (Trigger a Planning-related Delivery Split): freight units 5122 and 5123 were planned on one freight order, one delivery proposal and delivery 800000177 were created. After freight unit 5122 was removed and planned on a second freight order, the situation became inconsistent because one delivery cannot go on two freight orders. After Refresh, the system had split the original delivery so each freight order and freight unit had its own delivery.

## Warehouse integration in execution: in basic TM all warehouse options (Inventory Management with optional Handling Unit Management, Stockroom Management, EWM) are integrated through the delivery; advanced shipping and receiving integrates shipping and receiving into the freight order
S4611 (Exploring Warehouse Integrations): in basic TM, all options are integrated via the delivery.
- **Inventory Management** (Handling Unit Management is optional): the simplest model, with no dedicated warehouse setup. The transportation demand represents the delivery, which gives a freight unit that can be planned on a freight order.
- **Stockroom Management** (former LE-WM): for small to medium warehouse setups, integrated into the LE delivery. Aimed at installed-base customers, license included in SAP S/4HANA Enterprise Management, with no innovations planned. S4611 lists LE-WM functions not part of it (for example Task and Resource Management, Yard Management, Cross-Docking, Wave Management).
- **EWM:** for complex warehouses. In basic TM the integration is done through the delivery, replicated to EWM, and EWM updates the LE delivery and therefore the freight unit.
- **Advanced shipping and receiving (since SAP S/4HANA 2020):** integrates shipping and receiving directly into the freight order, supporting both EWM and IM integration, usable within basic TM scope as long as no advanced criteria are met (for example EWM and TM running side by side).
- **Advanced TM and EWM integration** needs the advanced license and is based on transportation units. A load plan from TM can go to the warehouse system (SAP Notes 1984252 and 2269324 are named).

S48600 shows the same two methods: freight order based (Advanced Shipping and Receiving, basic license) and transportation unit based (EWM integration, advanced license).

## Loading and unloading with the Load or Unload Freight Orders app: assign loading points, unloading points and doors, set arrived at or departed from door, set items to loaded or unloaded, set the stop to loading completed, and post goods issue or goods receipt; goods issue of an outbound delivery is tied to a freight order covering the first stage and goods receipt of an inbound delivery to one covering the last stage, controlled by events such as Loading Begin, Loading End or Departure
S48600: as part of Advanced Shipping and Receiving, the Load or Unload Freight Orders app handles deliveries managed in EWM and Inventory Management. It lets you assign or unassign loading points, unloading points and doors, mark inbound deliveries ready for warehouse processing, record arrival at and departure from doors, set items to loaded or unloaded, set the stop to loaded or entirely unloaded, record staging areas, and post goods issue or goods receipt.

**Goods issue** of an outbound delivery can be triggered as soon as execution of the freight order starts, and can only be associated with a freight order covering the **first stage**. Events such as Loading Begin, Loading End or Departure can control it. All delivery items relevant for picking must have been picked. **Goods receipt** for an inbound delivery can be triggered once execution ends, by events such as Arrival at Destination, Unloading Start or Unloading End, and relates only to the freight order covering the **last stage**.

## In the integrated warehouse exercise (transportation-driven) the outbound delivery order stays blocked until the freight order is set to Ready for Transportation Execution and its items to Ready for Warehouse Processing; then warehouse tasks are created and confirmed, and the freight order shows In Execution after departure from the door with warehouse processing partially completed while further stops remain
E04 (Execute an Integrated Warehouse and Transportation Process) in order:
1. The freight order document flow shows warehouse outbound delivery order 30003 in EWM for freight unit 5119.
2. In the Warehouse Monitor the outbound delivery order is blocked (red). In integration, one side must lead the process. Here it is transportation-driven, so the order stays blocked until the transportation team signals readiness.
3. In the freight order, choose **Set to Ready for Transportation Execution** and save.
4. On the Items tab, Status Management, select all items and choose **Set to Ready for Warehouse Processing** from the Warehouse Processing Status menu, and save.
5. After Refresh in the warehouse monitor, the block is removed (green).
6. Create warehouse tasks (Create WT in Background) and confirm them (Confirm WT in Background). Packing is optional and skipped. Choose **Set to Ready for Shipping**.
7. In the Load or Unload Freight Orders app, choose the warehouse loading stop and **Assign Door** (loading point ZLP_ZASR, door YD00).
8. **Set to Arrived at Door**, save. The load status is red.
9. **Set Items to Loaded**: item load status turns green, stop status is still red. Save.
10. **Set Stop to Loading Completed**: stop load status turns green. Save.
11. Post goods issue (Goods Movement, Post). The posting status is asynchronous and not green at once.
12. **Set to Departed from Door**, save.
13. The Execution tab records arrival, loading and departure events triggered by the app. On the Statuses tab the order is In Execution, has departed from the loading point ZLP_ZASR of shipping point SP_ZASR but not yet checked out of the shipping point, and warehouse processing is only partially completed because the second loading stop at another warehouse or shipping point is still open.

## In the basic shipping exercise the deliveries are picked (Pick Outbound Delivery), goods issue is posted in Manage Outbound Deliveries (status Ready to Post GI, then goods movement status Completed) and the freight order is set to Loaded and then Departed, giving In Execution
S4611 Exercise 8 (Pick, Load, and Post Goods Issue):
1. Check the picking, packing and overall status of the deliveries.
2. Pick the delivery quantity for all deliveries (storage location 0001) with Pick Outbound Delivery.
3. In Manage Outbound Deliveries, filter Overall Status Ready to Post GI, select the deliveries and choose Post GI. The result is picking status Fully Picked (C), packing status Packing not required or Completely Packed (C), and goods movement status Completed.
4. After the loading report arrives, on the freight order choose Execution Status, **Set to Loaded** and save. The Statuses tab shows life cycle In Process, execution status Ready for transportation execution, and logistical execution status SP_1010 Loaded with timestamp.
5. Choose **Set to Departed**. The execution status is In execution and the logistical execution status SP_1010 Departed with timestamp, with life cycle still In Process.

## Practice
Build a freight order lifecycle storyboard for one road shipment. Write a sequence of steps from creation (the method and the freight order type), through carrier assignment and sending, confirmation, ready for transportation execution, warehouse loading with door assignment, goods issue and departure, to completion. After each step show the relevant status values (life cycle, subcontracting, confirmation, execution), and list the output documents that PPF would create. Use only values named in this session's material.

## Self-check
Can I explain to a dispatcher, without notes, how a freight order is created, assigned to a carrier and driver, and followed through warehouse loading, goods issue and departure using its statuses?
