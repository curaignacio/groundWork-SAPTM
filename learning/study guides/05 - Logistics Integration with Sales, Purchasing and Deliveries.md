# Session 05 — Logistics Integration with Sales, Purchasing and Deliveries

## Overview
This session covers how a shipper's ERP documents reach TM and come back. Orders and scheduling agreements from sales and purchasing, deliveries from Logistics Execution (LE) and JIT calls become freight units in TM, TM plans them, and TM can then propose the deliveries that LE creates. You learn which documents are integrated and why (control keys, the logistics integration profile), how freight units are built, how the delivery proposal step works, and how Incoterm locations shape stages and responsibilities. In a shipper project, integration setup decides what ever reaches the planners, so most "why is there no freight unit?" questions trace back to this session.

## Scope of logistics integration: TM can be integrated with components in the same system or an external system; orders from SD and MM, deliveries from LE and JIT calls from nJIT drive transportation planning and execution, and the TM component creates or updates freight units directly for documents defined in Customizing as TM-relevant when they are saved
You can integrate TM with components in the same system (internal TM component integration) or with an external system. A decentralized EWM and TM system can also be integrated with an external system (H05).

Orders created in Sales and Distribution (SD) and Materials Management (MM), deliveries created in Logistics Execution (LE) and JIT calls created in Next Generation Just-In-Time (nJIT) facilitate transportation planning and execution in TM (H05). The TM component creates or updates freight units directly for orders or deliveries defined in Customizing as relevant for TM integration. When such a document is created or changed, the freight units are created or updated once you save it. TM can therefore react continuously to changes in SD, MM and LE (H05).

## What integration enables: collective planning for all orders and scheduling agreements, planning on sales or purchase orders before delivery creation for an earlier forecast of transportation demand, tendering, subcontracting and execution based on orders, sales order scheduling, and planning and execution of JIT calls
H05 lists what integration allows you to do:

- plan transportation collectively for all orders and scheduling agreements
- plan on sales or purchase orders before delivery creation, giving an earlier forecast of future transportation and resource demand
- perform tendering, subcontracting and execution in TM based on sales and purchase orders
- perform sales order scheduling: propose and create deliveries from dates and quantities in the planning results, considering constraints such as resource availability and transportation durations
- plan and execute JIT calls

## Integratable documents: orders (sales order, customer returns, purchase order, stock transport order, returns purchase order, returns stock transport order), scheduling agreements (sales, purchase, stock transport), JIT calls (sequenced, forwarded) and inbound and outbound deliveries from LE, also when an order was not sent to TM
H05 (Features) names four groups:

| Group | Documents |
|---|---|
| Orders (SD or MM) | Sales order, customer returns, purchase order, stock transport order, returns purchase order, returns stock transport order |
| Scheduling agreements | Sales, purchase and stock transport scheduling agreements |
| JIT calls (nJIT) | Sequenced JIT call, forwarded JIT call |
| Deliveries (LE) | Outbound and inbound deliveries, whether or not TM triggered their creation, and even if the related order was not sent to TM |

You can also define the transportation relevance of sales, purchase and delivery documents (H05). If a product in an order or delivery is classified as dangerous goods, TM takes this into account (H05).

*Conflict in wording:* S48600 lists "sales scheduling agreements" and "materials management scheduling agreements" among the triggering documents, whereas H05 names sales, purchase and stock transport scheduling agreements. S48600's list also omits JIT calls. The two are consistent in substance; use H05's list as the detailed one.

## Transportation requirements as sources: OTR is the demand from sales, purchasing and stock transport (SO, PO, STO); DTR is the demand from an inbound or outbound delivery (IDL/ODL); the freight unit represents the demand that is planned
S48600 defines these objects:

| Object | Abbreviation | Source documents |
|---|---|---|
| Order-based transportation requirement | OTR | Demand from sales, purchasing and stock transport (SO, PO, STO) |
| Delivery-based transportation requirement | DTR | Demand from an inbound or outbound delivery (IDL/ODL) |
| Freight unit | FU | Set of goods transported together; the smallest unit of freight in planning |

The freight unit merges items (transportation requirements) from originating documents such as SO, PO and STO for planning. Freight unit granularity varies by scenario: larger units simplify planning in VSR optimization, while smaller units theoretically offer higher optimization potential but complicate planning (S48600).

## Triggering documents and deployment models: sales orders, customer returns, purchase orders, stock transport orders and their returns, scheduling agreements and deliveries trigger transportation requirements; in side-by-side deployment the information is replicated and becomes order-based or delivery-based requirements via XML messages (SAP PI or point-to-point); in embedded deployment no separate document is needed and the freight unit is created directly from the original object
A transportation requirement is the event that initiates a TM process, triggered by transportation-relevant items in an initiating document. S48600 lists sales orders, customer returns, purchase orders, stock transport orders, return stock transport orders, sales and MM scheduling agreements, and outbound and inbound deliveries.

How it arises depends on the deployment (S48600):

- **Side-by-side / external TM system.** The original document is not in TM, so the information is replicated and creates order-based or delivery-based requirements. Integration with SAP ERP or SAP S/4HANA uses XML messages via SAP Process Integration or point-to-point communication.
- **Embedded / internal TM component.** The original object already exists in SAP S/4HANA, so no separate document is needed; the freight unit acts as the initial object for TM, created directly from the original object. S48600 states that this embedded scenario is the main focus of its overview training.
- **LSP.** Forwarding orders and quotations (session 04).

## Decentralized scenarios: a decentralized EWM and TM system can be integrated with an external ERP system and transportation planning done on outbound delivery orders; settings sit under Decentralized EWM-TM Integration
H05 states that a decentralized EWM and TM system can be integrated with an external ERP system, and that transportation planning is then done based on outbound delivery orders. The logistics integration profile for decentralized EWM is defined in Customizing under Integration, Decentralized EWM-TM Integration. It has common settings (freight unit building rule, condition for FUB rule determination), stage building (Incoterm locations 1 and 2, planning-relevant stages only or static stages as well) and compliance checks for the Advanced Shipping and Receiving process (H05).

*What the material does not establish:* this session's sources give only the profile description; the full decentralized process is in the Advanced Shipping and Receiving material of a later session.

## Transportation relevance and control keys: control keys define which documents in a chain are integrated; sales document integration is activated by assigning a control key to sales document type, sales area and shipping condition; purchasing documents by document type, purchasing organization and purchasing group; delivery documents by shipping point, delivery type and shipping condition; the key is stored in parameter TM_CONTROL_KEY and passed to all relevant documents in the chain
**Control keys** determine which documents in a document chain are integrated into TM. You can define as many as you need with different combinations of relevant documents, and you specify the integration mode: the internal TM component or an external TM system (H05).

| Document type | Control key is assigned to this combination (H05) |
|---|---|
| Sales documents (sales orders, customer returns) | Sales document type, sales area (sales organization, distribution channel, division) and shipping condition |
| Purchasing documents (purchase orders, stock transport orders, returns, scheduling agreements) | Document type, purchasing organization and purchasing group |
| Delivery documents | Shipping point, delivery type and shipping condition |

The control key decides whether the document and its corresponding delivery are integrated. When a document with activated integration is created, the system assigns the key (parameter TM_CONTROL_KEY) to it and to all relevant documents in the chain, such as the outbound or inbound delivery (H05). Practical reading: to decide whether a given order is integrated, check whether its document type, sales area or purchasing organization and shipping condition match an assignment that carries a control key.

H05 also covers related settings: a transport-driven process for outbound deliveries (the delivery is blocked for warehouse execution during transportation planning), and the definition of whether a delivery block is a planning block, an execution block or both.

## Deliveries inherit the control key of the preceding document and ignore the delivery Customizing in that case; the delivery setting is needed only when a delivery is integrated but its order is not
A delivery can be integrated using the control key of the preceding document, such as a sales or purchase order. It then inherits that key, and the system ignores the settings of the delivery Customizing activity. That activity is needed only when a delivery is to be integrated into TM but the corresponding order is not (H05).

## Three settings named by S48600 for integrating sales orders, scheduling agreements and deliveries: activate integration via control key, create a logistics integration profile, assign the profile to the document type; prerequisite for configuration is the location creation report /SAPAPO/CREATE_LOCATION
S48600 names three settings to integrate sales orders, scheduling agreements and deliveries:

1. Activate integration of documents via control key
2. Create a logistics integration profile
3. Assign the logistics integration profile to the document type

H05 states the prerequisite for the configuration: you have run the location creation report /SAPAPO/CREATE_LOCATION. It also describes the profile as something you can create several of and assign to TM-relevant business document types (H05). For purchasing documents, H05 says assigning a profile is optional.

## Logistics integration profile for SD, MM and LE: common settings (freight unit building rule, condition for FUB rule determination, automatic freight unit building, stage building variant) and order-related settings (plan on requested or confirmed quantities, FU building for partly complete sales documents, rule group for the time range of purchase scheduling agreements, integration based on actual quantity, improved location determination, Advanced SR compliance check)
The profile (Customizing: Integration, Logistics Integration, Internal TM Component Integration) has two groups of settings (H05).

**Common settings** (order-related and delivery-related):
- Freight unit building rule used when freight units are created automatically.
- Condition for FUB rule determination, which derives the rule from business document details.
- Automatic freight unit building: whether FUs are built automatically after the document is saved or in a separate manual step.
- Stage building variant: Static or Advanced (see the stage building item).

**Order-related settings:**
- Plan on requested or confirmed quantities.
- Freight unit building for partly complete sales documents: creates FUs for complete items of a partly complete sales document.
- Rule group to determine the time range of purchase scheduling agreements, limiting FU creation for scheduling agreements.
- Integration based on actual quantity: allows delivery integration on actual quantities determined during execution.
- Improved location determination: destination location based on the shipping point.
- Advanced Shipping and Receiving: enables compliance checks in that process.

Separate profiles exist for nJIT (common settings and stage building) and for decentralized EWM (H05).

## FUB rule determination: the system first checks the condition in the logistics integration profile, then the freight unit building rule in the profile, then standard settings; freight unit building can run automatically on save or be triggered manually or by background report (/SCMTMS/SUBSEQENT_FUB_LOGINT in embedded deployment)
S48600 gives three options in order: (1) the condition defined in the logistics integration profile; if none is specified or it gives no result, (2) the FUB rule specified in the profile; if none is maintained, (3) standard settings.

Freight units are generated automatically when transportation relevance is identified for a demand such as a sales order, purchase order, delivery, OTR or DTR. The system considers existing freight units, and builds new ones using the split quantity and the item split setting. SAP delivers the default strategy FUB_AUTO (S48600).

Inside a FUB rule (S48600): the critical quantity is the primary unit of measure that lets a line item be split into several FUs; split quantities set the maximum capacity of an FU (for example, 5 tons of cement with a 500 kg split quantity gives 10 FUs); Item Split Allowed controls whether items are split; an equipment type makes capacity count during building; incompatibility settings keep products apart (ice cream and ketchup). Exercise E02 shows the strategies of the rule FUBR_S4TM1: consolidate as much as possible, per item, or per request (E02).

Besides automatic building on save, FU building can be triggered manually or by the report /SCMTMS/SUBSEQENT_FUB_LOGINT in an internal TM component integration setup (H05).

## Order integration process: order created in SD/MM with items and schedule lines, TM creates freight units only for transportation-relevant orders, planning can consolidate FUs from orders of different types (for example purchase and sales orders), then TM can execute transportation or trigger delivery creation in LE
H05 describes three steps:

1. **Create order (SD/MM).** Items carry material, requested or confirmed quantity and desired delivery date; an item's quantity can be split into schedule lines with different dates. On creation the order is integrated into TM.
2. **Create freight units (TM).** TM creates FUs whose items correspond to the schedule line items. Depending on the profile, FUs are built automatically on save, use requested or confirmed quantities, and can be built for complete items in partly complete sales documents. TM creates FUs only for transportation-relevant orders.
3. **Plan (TM).** TM can consolidate FUs from several orders even if the base documents have different order types, for example purchase and sales orders.

After planning, TM either executes transportation or triggers delivery creation in LE (H05).

## End-to-end process from order to execution: create order (SD/MM), perform transportation planning (TM), create delivery proposal (TM), create deliveries (LE), reassign freight units from order to delivery (TM), execute transportation; the TM document flow can be displayed in SD, MM or LE
H05 gives the full chain:

| Step | System | What happens |
|---|---|---|
| 1. Create order | SD/MM | Order with items and schedule lines; FUs are created in TM |
| 2. Transportation planning | TM | Results include pickup and delivery dates, resource assignments and routes |
| 3. Create delivery proposal | TM | Based on planning results, or on FUs if no planning was done |
| 4. Create deliveries | LE | Inbound or outbound deliveries; also possible without a TM proposal |
| 5. Reassign freight units | TM | TM finds the order matching the delivery and reassigns the FUs from the order to the delivery |
| 6. Execute transportation | TM | Based on the planning results |

The TM document flow for an order or delivery (freight units, freight orders, freight settlement documents, with statuses) can be displayed in SD, MM or LE, so a user there can follow TM processing. In the integrated worklists you also see consolidated status, planning and execution block information (H05).

## Delivery proposals: TM proposes inbound or outbound deliveries from planning results and LE creates them; creation runs by background report /SCMTMS/DLV_BATCH, interactively from the Delivery Proposal Builder app or Freight Orders - Worklist app, from the transportation cockpit or from the freight order UI; dates come from the freight order or booking, otherwise from FUs, quantities from the FUs
TM can propose inbound and outbound deliveries from planning results, considering constraints such as resource availability and transportation durations, and can also trigger creation before planning. LE creates the deliveries; it may split them further on additional criteria but does not change TM's proposed dates or consolidate proposals (H05, S48600).

**Ways to start** (H05):
- Background report /SCMTMS/DLV_BATCH, with selection criteria or selection profiles and optionally a delivery profile.
- Interactive, from the **Delivery Proposal Builder** app: select profiles, review the listed documents, trigger proposals, review them.
- Interactive, from the **Freight Orders - Worklist** app: select documents, choose Create Deliveries, select freight units, trigger and review.
- From the **transportation cockpit** after planning: choose Create Delivery Proposals and review.
- From the **freight order UI** (needs a delivery profile assigned to the freight order type).

S48600 adds the OTR, Freight Unit, Freight Order and Ocean/Air Freight Booking worklists as start points.

**Data sources** (H05): dates from the freight order or booking, otherwise from the freight units; quantities from the freight units. A proposal consists of groups of freight units that can be delivered together. Depending on the start method, TM sends proposals to LE automatically or lets the user review first. If the delivery profile says so, planning results are fixed during proposal creation. Prerequisites include existing FUs, an order not blocked for delivery, and a control key making deliveries TM-relevant; when using the report, no proposal may already exist for the FUs.

*Naming difference between sources:* the interactive app is called "Delivery Proposal Builder" in H05 and "Create Deliveries - Delivery Builder" in E04 and "Delivery Builder app" in S48600.

## Delivery proposal consolidation and control: FUs can share a proposal only with the same source and destination location, Incoterms, shipping conditions, document type and (if planned) start and destination stop; TM respects chronological consumption of schedule lines in LE; the delivery profile (Create Delivery Profile app) controls fixing of planning results, grouping by freight unit, order or order item, and exclusion of planning or execution blocked objects
**Consolidation rules** (H05, S48600): if freight orders or bookings exist, only FUs of the same freight order or freight booking can share one proposal, so FUs of different orders can be combined, but FUs of one order spread over several freight orders give several proposals. If order combination is not allowed for an order, its FUs are not grouped with other orders' FUs. In addition, the FUs must match on source location, destination location, Incoterms, shipping conditions, document type (such as purchase or sales order), and start stop and destination stop if planning has been done. S48600 adds, for side-by-side scenarios, the SAP ERP system the order came from.

**Schedule lines.** LE consumes schedule lines chronologically, so TM does not propose a delivery for a schedule line before an earlier schedule line of the same item has been used; affected FUs are excluded. If LE errors on delivery creation, later schedule lines of the item are not delivered (H05).

**Delivery profile** (created in the Create Delivery Profile app) (H05):
- fix planning results of already planned FUs, freight orders or bookings
- when creating for unplanned FUs, create deliveries per freight unit (default), order or order item
- incompatibility settings that keep FUs out of one delivery
- include or exclude objects blocked for planning or execution; the check applies only to the object you start from (for example a main-carriage freight order blocked for execution blocks delivery creation if you start from it, but not if you start from the pre-carriage order)
- amalgamate FU items of the same order item into one delivery item or keep them separate
- when packaging information is transferred from the freight order to the delivery (relevant for the Advanced Shipping and Receiving inbound process)

Bulk material: actual quantities entered in the freight order UI create a delivery proposal with those quantities, without splitting FUs (H05).

## Delivery integration without order integration: if the order is not TM-relevant, TM creates new FUs for the delivery according to the specified FUB rule; changes to orders and deliveries update the FUs, a deleted order deletes its FUs, a deleted delivery reassigns FUs to the order if it is TM-relevant, otherwise deletes them
**Delivery without order integration** (H05): the order is created in SD/MM but is not TM-relevant; deliveries are created in LE; TM creates new FUs for the delivery by the specified FUB rule; then planning and execution follow.

**Changes and deletions** (H05):
- Order changed: TM updates the FUs by the assigned FUB rule; if the quantity rose after a delivery exists, new FUs cover the open quantity.
- Order deleted: TM deletes the FUs (an order cannot be deleted in SD/MM once a delivery exists). If an FU served several orders, its quantity is reduced; an empty FU is deleted or canceled per the freight unit type setting.
- Delivery updated: TM adjusts the FUs. A decreased delivery quantity raises the open quantity of the order, so order FUs adapt too; an increased quantity reassigns FUs from the order to cover it.
- Delivery deleted: FUs are reassigned to the order if the order is TM-relevant, otherwise canceled or deleted per the FU type.
- Delivery split: TM adjusts the FUs; splits in EWM are always integrated through LE.

S48600 also describes TM-triggered updates of outbound delivery dates and TM-triggered splits (outbound deliveries only; TM cannot trigger updates of inbound deliveries).

## Stock transport orders: a two-step process with outbound and inbound deliveries and reassignment of FUs from outbound to inbound delivery; in the Advanced Shipping and Receiving scenario goods issue triggers the inbound delivery and the reassignment, and FUs in one delivery must belong to the same EWM- or LE-managed warehouse or storage location
An STO transfers goods from one plant to another with the same company code. In the two-step process, outbound and inbound deliveries are created and FUs are reassigned from the outbound to the inbound delivery, giving visibility once goods issue is posted and goods are in transit (H05).

An STO can be executed order-based or delivery-based, with warehouse- or transport-driven execution. In the **Advanced Shipping and Receiving** scenario, goods issue posting triggers creation of the inbound delivery and automatic reassignment of the FUs; the warehouse processing status becomes In Transit. The One Step checkbox must be deselected for this. At both ends you can use EWM- or LE-managed warehouses or storage locations, but FUs in one delivery must belong to the same one (EWM or LE managed). In other scenarios the inbound delivery is not shown in the TM document flow and FUs are not reassigned (H05). Prerequisites include activating Improved Location Determination, defining control keys, and running delivery management, EWM and TM on a single system (H05).

## Scheduling agreement integration: schedule lines of purchase scheduling agreements create, change or delete freight units; TM planning results can be synchronized back to MM schedule lines in batch only for FUs not yet assigned to a delivery and within the planning time fence; inbound deliveries from an ASN lead TM to reassign FUs from the agreement to the delivery
For purchase scheduling agreements (H05):

- **Create or update schedule lines.** An MRP run or manual planning creates, changes or deletes schedule lines; after saving, TM creates, changes or deletes FUs accordingly.
- **Process planning.** Plan FUs manually or with the optimizer. The result can optionally be synchronized to materials planning in a batch run (report /SCMTMS/TM_SAG_PLANNING_SYNC), where MM creates, updates or deletes schedule lines. The planning time fence restricts updates; they are allowed only within the horizon fixed by an MRP run, and only for FUs not assigned to a delivery.
- **Communication to suppliers.** MM creates releases from schedule lines, so suppliers receive information based on TM planning results rather than material planning results.
- **Create deliveries.** MM creates or updates inbound deliveries from an ASN; when a new delivery is saved, TM reassigns the FUs from the agreement to the inbound delivery.

If a purchase scheduling agreement has Kanban indicator Z and a control cycle with TM relevance, TM creates FUs from the S2P JIT call regardless of the agreement's TM relevance (H05). Restrictions include that summarized JIT calls and outbound sequenced JIT calls are out of scope (H05).

H05 also describes deactivating and reactivating integration (reports /SCMTMS/DEACTIVATE_MMSAG_W_DLV and /SCMTMS/REACTIVATE_MMSAG_W_DLV), advising a fixed end date first with /SCMTMS/FIX_INT_TIMERANGE to avoid duplicate FUs.

## Integration time range for purchase scheduling agreements: start and end dates limit the schedule lines taken into account and so the freight units created; the start date is set once from the earliest schedule line with open quantity and a safety margin and is never in the future; the end date follows the schedule line count, matching rule and offsets and is determined daily; report /SCMTMS/UPDATE_INT_TIMERANGE preponed end dates
The time range limits how many schedule lines, and so how many FUs, TM builds, reducing FUs with distant delivery dates that are not yet relevant to planning (H05). The rule group is set in the logistics integration profile.

**Start date.** Determined once, when the agreement is first integrated and processed. The system finds the earliest schedule line with open quantity and uses its date as the upper limit; with a safety margin set, it takes the earlier of the two dates. It is usually before the current date and never in the future (H05).

**End date.** Determined daily. The system counts schedule lines within the "time range for schedule line count", finds the matching rule (by minimum number of lines), and adds the rule's integration time range offset and the additional offset (Planning Time Fence or Planned Delivery Time in Days, or none) (H05).

**Worked example** (H05): current date 17 May, safety margin 7 days (10 May), earliest open schedule line 8 May gives start date 8 May. For the end date: 30-day count range holds ten lines, so rule 2 (minimum 6 lines, 20 days) applies; plus 5 days planned delivery time gives an end date 25 days ahead.

If Customizing errors put the end date too far ahead, adjust Customizing and then run /SCMTMS/UPDATE_INT_TIMERANGE to prepone it (H05).

## Order-only integration of purchase scheduling agreements: activation report /SCMTMS/ACTIVATE_MMSAG_WO_DLV sets a start date and a reduction quantity strategy, adjustable later with /SCMTMS/ADAPT_START_MM_WO_DLV
In order-only integration, FUs are created for purchase scheduling agreement items without inbound delivery integration. These FUs are never transferred to a delivery, so execution relies on the order-based FUs and the agreement (H05).

The activation report /SCMTMS/ACTIVATE_MMSAG_WO_DLV determines a start date automatically (usually the next date with order quantity for which goods receipt is not yet booked); no FUs are built for quantities before it. You also choose a **reduction quantity strategy** (H05):
- don't consider any deliveries;
- consider only goods receipt quantities at or after the start date;
- consider all delivered quantities (goods receipt and deliveries) at or after the start date.

The system subtracts the reduction quantity before building FUs for the remaining quantity at every integration. The end date logic is unchanged. /SCMTMS/ADAPT_START_MM_WO_DLV lets you freely adjust start date and reduction quantity afterwards, which the activation report does not allow (H05).

## JIT call integration: FUs are created from sequenced JIT calls based on the component group material, with JIT call reference number, receiving point and unloading point; the outbound (S2C) process is delivery-based only
Integration with nJIT creates FUs from sequenced JIT calls. FUs are built from the call's component group material, not the individual components, and contain the JIT call reference number, receiving point and unloading point. Updates and deletions follow changes to the call (H05).

- **Supply to Production (S2P), inbound.** No initial package building; packaging information and slot number come with the ASN, and the system updates the S2P FUs on receipt. Initial FU building from component group materials is possible.
- **Supply to Customer (S2C), outbound.** FUs are created from the outbound delivery in LE-SHP; the process is delivery-based only, so FU building cannot be based on the S2C call. Creating deliveries with the delivery report is not available in S2C.
- A **forwarded JIS call** outsources component manufacturing from one supplier to another, running like S2P between two suppliers.

All solutions must operate on a single system (H05).

## Source and destination location determination: business partners, plants, shipping points or storage locations from ERP documents are identified and locations updated or created; a new address in a document creates a one-time location; Improved Location Determination uses shipping points as destination
The determination identifies business partners, plants, shipping points or storage locations in ERP documents and transmits them to the freight units; it updates or creates locations where needed. A document-specific address is also considered (H05).

- A new address entered in a business document creates a **one-time location** used as source or destination of the FU.
- By default, for stock transport orders, returns and STO scheduling agreements, business partner addresses are the destination; for purchase orders and agreements, a one-time location with the storage location address is used when one exists.
- **Improved Location Determination** uses shipping points as the destination instead; the item's delivery address tab then shows the storage location address, while the FU shows the receiving point address, which can differ. In Advanced SR scenarios the improvements are active by default (H05).

## Advanced intercompany sales and stock transfer: one freight unit across the business documents, harmonized Incoterm handling, Incoterm locations build FU stages, and TM sets the planned and actual transfer of control dates and times in the LE delivery
For advanced intercompany sales and advanced intercompany stock transfer, H05 states that TM supports these processes as follows:

- one freight unit is created across the various business documents
- Incoterm handling is harmonized between Sales, Sourcing and Procurement, LE and TM
- Incoterm locations build FU stages in TM
- TM sets the transfer of control dates and times in the LE delivery, based on planning and actual events (visible on the Shipment tab of the LE delivery)
- freight cost allocation posting is enabled

In advanced intercompany sales, a selling company's sales order leads to an intercompany purchase order and intercompany sales order in the delivering company; the delivering company delivers to the customer, invoices the selling company, and the selling company invoices the customer. In stock transfer, an intercompany purchase order is followed by an intercompany billing document and an automatically posted supplier invoice (H05). Prerequisites include setting both processes up and the logistics integration profile (H05).

## Incoterms and responsibilities: planning and cost responsibility transfer at Incoterm location 1; risk transfers there for non-C-clauses and at Incoterm location 2 for C-clauses (CIF, CIP, CFR, CPT); transfer of control is the transfer of risk responsibility, internal within the group and external to the customer
H05 separates three duties: **planning** responsibility (who organizes the transport), **cost** responsibility (who pays) and **risk** responsibility. Incoterm locations are where these pass from shipper to consignee.

- Planning and cost responsibility transfer at **Incoterm location 1**.
- Risk transfers at location 1 for non-C-clauses, and at **Incoterm location 2** for C-clauses (CIF, CIP, CFR, CPT).

The transfer of risk responsibility is **transfer of control**: internal when goods go from the delivering company to the selling company within the group, external when they go from the group to the customer; each has a planned and an actual version (H05). S48600 adds that an Incoterm location is a master data location in TM, and that the Incoterms (Part 2) field can define it, mapped with the app Assign Location to Incoterm Location.

**H05 example.** The sales order carries DDP, so the group plans and pays to the customer in Walldorf (location 1). The intercompany order carries CIF: two stages result, Palo Alto to the port of discharge in Hamburg (delivering company) and Hamburg to Walldorf (selling company). Internal transfer of control occurs at Incoterm location 2, when the goods are loaded on the vessel in New York, so risk passes then; the delivering company keeps planning and cost responsibility until Hamburg. External transfer of control occurs at the customer's address. *The H05 text alternates between calling the CIF Incoterm that of the intercompany purchase order and of the intercompany sales order; the stage and transfer logic is the same either way.*

## Stage building from Incoterm locations: stages are built only if the Incoterm has the Incoterm Location flag, otherwise one stage from source to destination; the logistics integration profile offers the Static variant (stage profile) or the Advanced variant (Incoterm locations 1 and 2), and the Incoterm Location Stage Building field gives rules 01 to 05
S48600: the system uses the Incoterm location for stage building only if the Incoterm has the **Incoterm Location flag** (a location must be entered with it). With no Incoterm, or an Incoterm without the flag, only one stage from source to destination is created.

Stage building variants in the profile (H05): **Static** (a stage profile and stage profile condition determine the stages, and you define which stages are built when the Incoterm location is used) or **Advanced** (considers Incoterm locations 1 and 2, with a choice of planning-relevant stages only, or static stages too).

Rules of the Incoterm Location Stage Building field (S48600):

| Value | Result |
|---|---|
| Initial value | Default: two planning-relevant stages |
| 01 Source Location to Incoterm Location, Type 1 | One stage, source to Incoterm location |
| 02 Source Location to Incoterm Location, Type 2 | Active stage source to Incoterm location, plus a non-planning-relevant stage to the destination |
| 03 Incoterm Location to Destination, Type 1 | One stage, Incoterm location to destination (for example a consignee planning only that leg) |
| 04 Incoterm Location to Destination, Type 2 | Active stage Incoterm location to destination, plus a non-planning-relevant stage from the source |
| 05 Two Active Stages | Two planning-relevant stages |

## Reports for logistics integration: /SCMTMS/LI_ACTIVATE, /SCMTMS/DLV_BATCH, /SCMTMS/SUBSEQENT_FUB_LOGINT, /SCMTMS/TM_SAG_PLANNING_SYNC and the purchase scheduling agreement activation, deactivation, reactivation and time range reports
H05 lists these reports (SAP Easy Access: Logistics, Transportation Management, Administration, Logistics Integration):

| Report | Purpose (H05) |
|---|---|
| /SCMTMS/LI_ACTIVATE | Activate integration of business transaction documents into TM (internal setup) |
| /SCMTMS/DLV_BATCH | Create deliveries based on existing freight units |
| /SCMTMS/SUBSEQENT_FUB_LOGINT | Trigger creation of freight units in internal TM component integration |
| /SCMTMS/TM_SAG_PLANNING_SYNC | Synchronize the planning date of FU items with the schedule line delivery date in the purchase scheduling agreement |
| /SCMTMS/ACTIVATE_MMSAG_WO_DLV | Activate purchase scheduling agreements without delivery integration |
| /SCMTMS/ADAPT_START_MM_WO_DLV | Adjust start date and reduction quantity for such agreements |
| /SCMTMS/DEACTIVATE_MMSAG_W_DLV | Deactivate purchase scheduling agreements |
| /SCMTMS/REACTIVATE_MMSAG_W_DLV | Reactivate integration of purchase scheduling agreements |
| /SCMTMS/UPDATE_INT_TIMERANGE | Verify end dates and reschedule them earlier |
| /SCMTMS/FIX_INT_TIMERANGE | Set a fixed end date for the end of integration |

*A JIT note in H05 writes the delivery report as /SCMTM/DLV_BATCH; the report list gives /SCMTMS/DLV_BATCH, which is used here.*

## Exercise flow (E02): create a purchase order with Create Purchase Order - Advanced and the confirmation control value Inbound delivery, open the Order Integration Worklist app, review the freight unit built by FUBR_S4TM1 and its document flow; E04 shows Create Deliveries - Delivery Builder turning four freight units into three delivery proposals
**E02 flow.**
1. Search for the Create Purchase Order - Advanced app. Supplier, organizational data and item details (material, quantity, delivery date, plant) are prefilled.
2. Choose Inbound Delivery from the confirmation control value list. The exercise notes that the purchase order (4500000069) has a type that allows TM integration.
3. Open the Order Integration Worklist app and choose freight unit 5105, built from the order by freight unit building rule FUBR_S4TM1. The purchase order data fills the source and destination locations, destination dates, materials and quantities of the FU.
4. Open the Document Flow: when a subsequent document such as a freight unit is created from a preceding one such as a purchase order, the system generates a document flow showing the sequence of related documents and their statuses (E02).

E02 also shows package building: a sales order of 100 pieces becomes several packages under 500 kg in the FU item hierarchy, driven by the unified package building profile assigned to rule FUBR-PB-00 (E02).

**E04 flow.** In Create Deliveries - Delivery Builder you select profile and layout sets (like in the cockpit), select freight orders, and choose Create Delivery Proposals. Three delivery proposals result for four freight units, because two FUs with the same destination were combined into one. Choosing Create Deliveries creates three deliveries, and the freight order's document flow shows which FUs went into each (E04). A second E04 exercise, titled "Trigger a Planning-related Delivery Split", creates one delivery for two planned freight units and then removes one freight unit from its freight order (E04); the outcome of that split is not covered in the part of E04 used here.

## Practice
Draw a one-page integration map for one scenario, for example a sales order or a purchase order. Show the document chain, the control key and logistics integration profile settings that make it TM-relevant, the freight units TM builds, the delivery proposal step and the point where freight units are reassigned to the delivery.

## Self-check
Can I explain how orders, scheduling agreements and deliveries from sales and purchasing become freight units in TM, and how deliveries come back from TM, to a project stakeholder without notes?
