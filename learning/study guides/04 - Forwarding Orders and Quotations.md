# Session 04 — Forwarding Orders and Quotations

## Overview
This session covers Forwarding Order Management, the TM component a logistics service provider (LSP) uses to take a transportation job from an ordering party and turn it into something TM can plan, execute and invoice. You learn how a forwarding order is created, how its screen and route are organized, which statuses and blocks it carries, how a forwarding quotation relates to it, and how it connects to freight units, freight orders and the forwarding settlement document. In an LSP project the forwarding order is the starting document of the whole chain, so reading its Status tab and document flow is a daily skill.

## Purpose of Forwarding Order Management: create, edit and confirm forwarding orders from ordering parties, already specify the route and have transportation charges calculated; the orders form the basis for transportation planning. Data can also be entered as a forwarding quotation and sent to the ordering party
You use the Forwarding Order Management component to create, edit and confirm forwarding orders from your ordering parties. Already at this stage you can specify the route and have the transportation charges calculated. The orders then form the basis for transportation planning (H04).

Alongside the order, the same data can be entered as a **forwarding quotation** and sent to the ordering party. A forwarding order can then be created based on that quotation (H04).

The documents in this component hold everything needed to plan and execute the transport: pick-up and delivery addresses, dates/times and the goods. Data is entered manually or transferred automatically via PI interfaces. After editing, you can send a confirmation to the ordering party, and you can trigger transportation planning from the order, generating freight units and freight orders (H04).

*What the material does not establish:* H04 notes that integration of the forwarding order and the forwarding settlement document (FWSD) with Credit Management in SAP S/4HANA is currently not released. It gives no further detail on why.

## Integration of the component: freight orders and freight bookings can be created from forwarding orders (Freight Order Management); forwarding orders are the basis for planning and execution; a forwarding settlement can be created from the order to trigger invoicing; master data is a prerequisite; integration with dangerous goods management and global trade
H04 lists the integration points of Forwarding Order Management with other TM components:

| Component | What the integration means (H04) |
|---|---|
| Freight Order Management | Freight orders and freight bookings can be created from forwarding orders |
| Planning | Forwarding orders form the basis for planning and executing the transportation |
| Forwarding Settlement | A forwarding settlement can be created from the order to trigger the invoice creation process |
| Master Data | The necessary master data must exist before forwarding orders can be created |

The component is also integrated with dangerous goods management and the global trade processes (H04). In practice this shows up as the dangerous goods profile on the forwarding order type (dangerous goods information appears on order items only if such a profile is assigned) and as the trade compliance check that can run when the order is saved (H04).

The business document itself links to three TM documents: the forwarding quotation (an accepted quotation can be converted into an order), the freight unit (created from the order) and the forwarding settlement document (created from the order) (H04).

## Definition of a forwarding order: an order from an ordering party to a carrier or logistics service provider for the transportation of goods from a shipper to a consignee under agreed conditions; entered manually (for example after a telephone call) or transferred automatically via PI interfaces or EDI; holds pick-up and delivery address, dates/times and the goods
H04 defines the forwarding order as an order from an ordering party to a carrier or logistics service provider for the transportation of goods from a shipper to a consignee according to the agreed-upon conditions. Note the three business partner roles: ordering party (who places the order), shipper and consignee (the ends of the transport).

You enter the data manually, for example after a telephone call, or it is transferred automatically via PI interfaces or EDI. The order contains the most important data for planning and execution: pick-up and delivery address, dates/times and the goods to be transported. From it you can determine the transportation route, create freight units and a transportation plan, have charges calculated and start the invoicing (H04).

H04 adds that the enterprise services of forwarding order management are released only with restrictions.

## Forwarding orders and quotations as transportation requirements in the logistics service provider (LSP/3PL) deployment: they are created manually in the SAP TM UI or by EDI with an external system, and count as the transportation requirements of an LSP process
S48600 describes three ways transportation requirements arise, depending on deployment. For logistics service providers (LSPs or 3PLs), requirements arrive as forwarding orders, typically created manually in the SAP TM user interface or by EDI with an external system. Forwarding orders and forwarding quotations are considered transportation requirements within an LSP process (S48600).

The other two cases are side-by-side deployment (replicated order-based or delivery-based requirements) and embedded deployment (the freight unit is created directly from the original sales or purchasing object) (S48600). Session 05 covers these.

The contrast answers a common question: for a shipper, the demand comes from sales orders, purchase orders, stock transport orders or deliveries; for an LSP, the customer's request itself is the forwarding order, so no separate ERP document drives the demand (S48600).

## Design of the forwarding order screen: determined by the transportation mode (air, sea or land) and by the forwarding order type defined in Customizing; the initial screen takes the type and the mode, and the type decides which additional tab pages are shown for each business process
The design of the user interface is determined by two factors: the transportation mode (air, sea or land) and the forwarding order type defined in Customizing (H04).

On the initial screen you specify the forwarding order type and the transportation mode, unless the type already predefines the mode. The UI then adjusts automatically to the mode-specific business processes. The type also predefines which additional information or tab pages appear for each business process, for example dangerous goods information for order items (H04).

You can also configure, in the apps, whether a tab page, assignment block or specific fields are displayed or hidden (H04). If a Web Dynpro application configuration is defined in the order type, the system does not change the UI when the mode changes (H04).

## Basic structure of the forwarding order: general data, business partner, location and dates/times areas (valid for all items, including sales organization, Incoterms, service level, totals of quantity and weight); ordered route and actual route; list of order items; document flow; output management; status; HBL or HAWB; profitability; and process-dependent tab pages such as charge calculation, air cargo security, instructions and change documents
H04 gives the generic structure, in tab pages or assignment blocks:

- **General data, business partners, locations and dates/times.** Data valid for all items: sales organization, Incoterms, service level, and the totaled quantity and weight of the items. Process control attributes such as transportation mode and shipping type are also here.
- **Ordered route and actual route.** The route requested by the ordering party and the actual route, each with individual stages.
- **List of order items.** Item-specific data as an item hierarchy.
- **Document flow.** Documents entered into the order and documents created from it.
- **Output management.** Which documents were printed or sent (e-mail, fax), and printing of documents such as bills of lading.
- **Status.** Life cycle status, blocking status and the other statuses.
- **HBL or HAWB.** House bill of lading or house air waybill data.
- **Profitability.** A profitability analysis with navigation to the individual business documents.
- **Process-dependent tab pages**, shown if the process is activated in the document type: charge calculation and internal charge calculation, air cargo security, instructions (for example cleaning a container) and change documents (only if change tracking is activated). Air forwarding orders also have a Nature of Goods tab page.

## Fast order entry: besides the full view, the Page function opens a single-screen view without tab pages with all fields needed to complete an order
Besides the comprehensive view, the Page function gives access to a view for fast order entry. It contains all input fields needed to complete a forwarding order on one screen, without tab pages, and keyboard entry is faster (except in the list of order items) (H04).

H04 also describes a related creation route: from the order management overview you can first enter the order in a fast entry screen, save it, and call it up later to add further data.

## Ways to create a forwarding order: on the basis of a quotation, on the basis of a template, as a copy of an existing order, from the order management overview, from a forwarding agreement (ID and version, service items and data such as transportation mode, shipping type and sales organization are transferred), or via PI interfaces
H04 lists six ways to create a forwarding order:

| Way | What happens (H04) |
|---|---|
| On the basis of a quotation | Create the quotation first and use its data; a quotation can also be assigned to an order subsequently, subject to prerequisites such as matching data |
| On the basis of a template | A template holds default data such as sales organization or Incoterms |
| As a copy of an existing order | Much of the data is copied, including route data |
| From the order management overview | A new order without reference to another object |
| From a forwarding agreement | Reference to an agreement ID and version; service items and data such as transportation mode, shipping type and sales organization are transferred |
| Using PI interfaces | Data comes directly from the ordering party via SAP NetWeaver PI |

For the forwarding agreement route, a reference to a specific agreement version is entered; if you also specify the agreement item, service items flagged as flow services are transferred. You can also enter a second agreement for the corresponding import or export document (H04).

## Template and copy behaviour: a template copies the order data such as document type, except dates/times and planning and execution data; a copy keeps much of the data including route data but has no dates/times and no follow-on documents, and its life cycle status is New
- **Template.** You can create a template from scratch or from an existing order (from the order or from the order management overview). The system copies the data, such as document type and order data, except dates/times and planning and execution data (H04).
- **Copy.** Choosing Copy in the order gives a new order with much of the data, including route data. It has no dates/times and no follow-on documents such as freight units or freight orders. You can also copy without the actual route data. Its life cycle status is New (H04).

When you copy, you may enter a new forwarding order type for the new order. H04 warns this can cause inconsistencies with copied data that came from the old type's Customizing (such as transportation mode and shipping type). If the data for the new type is unique the system updates it automatically; otherwise you correct it manually (H04).

## Steps of manual creation: initial screen (forwarding order type, transportation mode, references, default route), general data (sales organization, process control attributes, Incoterms or freight terms), business partners, locations and dates/times, business process-dependent data, route, order items, then save
H04 describes manual creation in seven steps:

1. **Initial screen.** Forwarding order type and transportation mode; references to other documents, copy or template; a reference to a forwarding agreement version and item; and optionally a default route. The system checks that the default route fits the other entries. The order appears with life cycle status New.
2. **General data.** Sales organization (determined automatically if defined in Customizing), process control attributes (transportation mode, shipping type, movement type, air waybill type) and payment terms. Depending on Customizing you enter Incoterms or freight terms. If no payment terms are entered, the system determines the forwarding agreement from the ordering party and creates only one forwarding settlement document for the ordering party. Further options here include Uncontrolled Transportation, Buyer's Consolidation and Shipper's Consolidation.
3. **Business partners, locations and dates/times.** Partners such as shipper, consignee and ordering party can be determined automatically via the partner determination profile in the order type. A location can determine the shipper or consignee, and a business partner can determine the location if unique. A manually overwritten address is marked as deviating and copied to follow-up documents. A credit limit check can be activated.
4. **Business process-dependent data.** For example air cargo security, instructions, export/import processing, handling codes.
5. **Route.** Create the stages if the ordering party already gave route information (see the route items below).
6. **Order items.** Entered as a hierarchy.
7. **Save.** See the item on saving.

## Rules on type and mode: without an entry the default type from Customizing is used; the forwarding order type cannot be changed afterwards in the document; a mode defined in the type cannot be changed; a manually entered mode can be changed later only if no follow-on documents exist for FUs or TUs whose main carriage stage has started
These rules (H04, step 1 and 2 of creation):

- Without an entry, the default type from Customizing is used.
- The type cannot be changed afterwards in the document itself. Some other parameters, such as the sales organization, may still be changed if Customizing predefined a changeable value.
- If the mode is defined in the type, it is displayed and cannot be changed. If you enter the mode first, the input help for the type offers only types valid for that mode. If the type does not define a mode, you can enter it manually or leave it empty and enter it later.
- A manually entered mode may be changed later, but not if follow-on business documents exist for the freight units (FUs) or transportation units (TUs) and execution of at least one main carriage stage of one of them has already started.
- Changing a manually entered mode from one category to another (for example sea to air) clears the fields not relevant for the new mode, saves the document automatically and loads the UI for the new mode. The ordered route, actual route and dependent freight documents are not changed automatically and must be updated manually if required (H04).

Why it matters: the type fixes the profiles, defaults and UI (see the Customizing item), so choosing it wrongly means creating a new order rather than correcting the old one.

## Order item hierarchy: items are entered as a hierarchy such as container, packaging and product; only the top level is relevant to planning, and quantities and weights are totaled and copied to the header
Items are entered as a hierarchy, for example container, packaging and product. Only the top level of this hierarchy is relevant to planning. The quantities and weights of the levels are totaled and copied to the header data (H04). The default printout also shows information about the lower hierarchy levels if items were entered in a hierarchy (H04).

*What the material does not establish:* the item-creation detail (item types, service items, equipment types, splitting) sits in a separate H04 chapter this session does not expand.

## Saving the order: the system assigns an ID from the number range of the document type, checks completeness and consistency, and if customized automatically creates freight units, confirms the order, calculates charges, triggers an approval workflow, checks credit limits and runs the trade compliance check
On save the system assigns an ID from the number range of the document type and checks the data for completeness and consistency. Results appear as error messages and as a completeness status (H04).

If defined in Customizing, the system then performs automatic functions (H04):

- creation of freight units
- confirmation of the order, with the confirmation sent to the ordering party
- calculation of transportation charges
- a check of whether approval limits are exceeded, triggering the approval workflow if needed
- a credit limit check of the business partners
- a check of foreign trade regulations (trade compliance check)

If the order is incomplete for planning, the system sets an automatic block (see the blocking item). A BAdI can change which fields the completeness check requires (H04).

## Customizing behind the order: the forwarding order type assigns the profiles (planning, output, dangerous goods, partner determination) and the freight unit building rule or condition, and sets defaults such as transportation mode, shipping type, traffic direction, sales organization, automatic confirmation, automatic FU building, approval workflow, credit limit check, charge calculation, settlement and change tracking
The forwarding order type is the central Customizing object (H04). It lets you:

- assign the **profiles**: planning profile (how planning proceeds from the order, or on what basis routes are determined), output profile (possible print documents and EDI messages), dangerous goods profile and partner determination profile
- assign the **freight unit building rule or a condition** that determines it
- set **defaults**: transportation mode, shipping type, traffic direction, sales organization
- switch on or off: automatic confirmation, automatic freight unit building, approval workflow and credit limit check, charge calculation and internal charge calculation, forwarding settlement and internal settlement, process-specific parameters (air waybill type, air cargo security check) and change tracking
- determine the appearance of the UI

Other prerequisites named in H04: a number range interval for the order IDs, transportation modes, optional mode-specific codes (airline codes, SCAC), service levels, shipping types, block reasons, and optionally HBL/HAWB number ranges assigned to sales organizations and ordering parties. Profiles are optional but needed for follow-up actions such as planning or printing.

## Ordered route: the stages of the route requested by the ordering party; source and destination on the Locations and Dates/Times tab appear as one Complete Carriage line, which can be split into stages; a default route from the initial screen or a forwarding agreement item fills it
The ordered route holds the stages requested by the ordering party. If source and destination are already entered on the Locations and Dates/Times tab, they appear as one **Complete Carriage** line. A default route entered on the initial screen, or selected from a forwarding agreement item, fills the route with its stages (H04).

To add stages you select the Complete Carriage line (or an existing stage) and choose **Split**. The system inserts two lines: the first keeps the source location and dates and leaves the destination empty; the second keeps the destination and leaves the source empty. A route A to C becomes, for example, A to B and B to C (H04).

## Actual route: entered manually, determined by Route - Transportation Proposal, or taken from a default route; the transportation mode of the header refers only to the main carriage, and stage mode is taken from manual entry, then stage type Customizing, then header; after transportation planning the actual route is displayed and can no longer be changed
You can enter the actual route manually, have the system determine it with Route - Transportation Proposal, or apply a default route and copy it into the stage table. Items and freight units do not have to exist yet. A route copied from a proposal can still be changed (H04).

Stage data is pre-filled from Customizing and the header (H04):

- The **movement type and traffic direction** (and an optional stage profile) can determine stages automatically and restrict stage types. With the traffic direction they also decide which stages you are responsible for, shown in the Stage Status.
- The **transportation mode** in the header refers only to the main carriage. For a stage the mode is taken in this order: manual entry for the stage, then Customizing for the stage type, then the header.
- The **agreement party and type** are determined from the stage type and the Incoterms in the header, defining who is responsible for settlement.
- If you enter an **SCAC** without a carrier, the carrier is determined in later planning; entering a carrier fills the SCAC. For air, airline codes give the MAWB prefix.

If planning was performed from the forwarding order, the actual route is displayed and can no longer be changed. As an alternative to planning, you can create freight orders and freight bookings directly for the stages of the route (H04).

## Ordered route is not updated by the actual route; Copy from Actual Route overwrites it, after which the ordered route is no longer visible. Stage detail data distinguishes requested, planned, actual and confirmed dates
The ordered route is not updated automatically by the actual route. To print up-to-date documents you can choose **Copy from Actual Route** on the Ordered Route tab, which copies the data into the ordered route; the ordered route is then no longer visible (H04).

Stage detail data is shown on three tab pages: Ordered Data (provided by the customer), Planning/Execution Data (from successor documents such as freight orders, cannot be changed) and Additional TU Dates/Times (H04). The dates distinguish:

| Date | Meaning (H04) |
|---|---|
| Requested pick-up and delivery date | Requested by the ordering party, in the ordered route |
| Planned departure and arrival date | Entered manually or set by planning; before planning it equals the requested date |
| Actual departure and arrival date | Entered in the freight document or reported by SAP Event Management |
| Confirmed pick-up and delivery date | Confirmed to the ordering party, for the complete carriage |
| Cut-off dates | Read from the freight document: latest time goods or documents must be available |

## Document flow: shows which business documents were entered into the order and which were created from it, with navigation to follow-on documents such as a freight unit
The document flow shows which business documents were entered into the forwarding order and which were created based on it. From here you can display the follow-on documents and open, for example, a freight unit (H04). When manual planning in the transportation cockpit creates a freight order, it appears in the order's document flow (H04). This is the tool for tracing an order to its freight units, freight orders and forwarding settlement document.

## Life cycle status values of a forwarding order: New, In Planning, Planned, In Execution, Executed, Partially Invoiced, Completed, Determination Pending, Canceled, Draft
H04 defines the life cycle status values:

| Status | Meaning (H04) |
|---|---|
| New | Order created; no freight units or transportation units yet |
| In Planning | At least one FU or TU has been created |
| Planned | All FUs and TUs assigned to it have been planned |
| In Execution | At least one follow-on document (not necessarily an FU or TU) is in execution |
| Executed | Execution of all planning documents assigned to the order is completed |
| Partially Invoiced | One or more forwarding settlement documents were created, invoicing not yet complete |
| Completed | Execution finished, invoicing done, existing instructions completed (if so customized); also set for orders created only for settlement (for example service orders) once settlement documents are complete |
| Determination Pending | Set temporarily when an order is reopened after Completed; changes again after the next save |
| Canceled | The order was canceled |
| Draft | Set when an import forwarding order is created or updated; only the sales organization can be changed |

Reading this top to bottom gives the life of an order: planning, execution, invoicing, completion.

## Further status types: planning status, execution status, confirmation status, approval status (only with approval workflow), delivery status, FWQ assignment status, organization interaction status, HBL or HAWB status, and statuses for air cargo security and foreign trade compliance
Besides the life cycle status, the Status tab shows (H04):

- **Planning status:** Planning Not Started; In Planning (at least one FU or TU created, but no freight document assigned yet); Partially Planned (a freight document assigned, but not all FU or TU stages planned); Planned.
- **Execution status:** Execution Not Started; In Execution (at least one linked planning document in execution); Executed.
- **Confirmation status:** Not Confirmed (no confirmation yet, or it was reset because data changed); Confirmed.
- **Approval status** (only with approval workflow): Not Checked; No Approval Required; Approval Required (limits exceeded, order blocked); Approved; Not Approved (stays blocked).
- **Delivery status:** Delivered, Partially Delivered, Not Delivered, taken from the freight documents. An item-level cargo receipt status also exists.
- **FWQ assignment status:** whether the order was created from a forwarding quotation or one was assigned later.
- **Organization interaction status:** the interaction between organizational units, for example a sales organization and a planning and execution organization, per stage and aggregated.
- **HBL or HAWB status**, and statuses for air cargo security and compliance with foreign trade regulations (shown if activated in the order type).

Planning and execution statuses are finer-grained views of what the life cycle status summarizes. Note that the "In Planning" wording appears in both the life cycle and the planning status, with slightly different definitions: the planning status version stresses that no freight document is assigned yet (H04).

## HBL or HAWB: the assignment block shows house bill of lading or house air waybill data and allows waybill numbers to be allocated to freight units; its status (Finalized, Partially Finalized, Not Finalized) shows whether the customer service agent has completed the HBLs or HAWBs
The HBL or HAWB block shows house bill of lading or house air waybill data, and lets you assign waybill numbers to freight units individually or remove the assignments (H04). Number ranges can be assigned to sales organizations and ordering parties in the master data; you can assign a number from the range in the order, and deactivate that function per order type (H04).

The HBL or HAWB status supports communication, for example between a customer service agent and a capacity manager at the gateway. It shows whether the HBLs or HAWBs have been completed by the customer service agent and are available for subsequent processes (H04):

- **Finalized:** all house air waybills in the order are completed.
- **Partially Finalized:** at least one but not all are completed.
- **Not Finalized:** none is completed.

You can set the status manually via a menu option and reset it to Not Finalized. For the order type Direct Shipment the status is set for both the HAWB and the master air waybill (MAWB) (H04).

## Blocking: planning, execution, confirmation and settlement blocks can be set manually with block reasons from Customizing or automatically (incomplete order, approval workflow, dangerous goods check); removal needs authorization and a comment can be logged; a forwarding settlement document cannot be created while the settlement block is set
Blocks can be set manually or automatically for four functions (H04):

| Block | What it stops (H04) |
|---|---|
| Planning | Planning of the order: creation of FUs and TUs, and of freight orders |
| Execution | Execution of the order and associated planning documents |
| Confirmation | Confirmation of the order |
| Settlement | Creation of the forwarding settlement document |

**Manual blocks.** You pick a block reason defined in Customizing (Define Block Reason Codes). Several planning or execution blocks with different reasons can coexist, and all reasons show in the aggregated view and in successor documents.

**Automatic blocks.** The system blocks, for example, an order that lacks required information; block details list the fields still to fill, and the Check function shows the same messages. Further automatic blocks come from the approval workflow and the dangerous goods check.

**Removal.** You need the authorization to remove blocks. You can enter a comment, and the system logs who removed the block and when. You cannot create a forwarding settlement document while the settlement block is set. In Customizing you can specify the successor documents to which the blocks are copied (H04).

H04 also notes that changes to a business partner block are not always visible immediately in an open order; close and reopen it.

## Editing the order: freight units can be created automatically or from the Follow-Up Actions menu, planning is manual in the transportation cockpit or via route determination, automatic planning with the VSR optimizer, or direct creation of freight documents; changes are passed on to freight units and follow-on documents until execution data has moved the FU to On Hand; an order with an assigned freight document cannot be canceled
After saving, you can (H04):

1. **Create freight units**, automatically after save or manually from the Follow-Up Actions menu, using the FUB rule or its condition from Customizing. All required data must be entered first. After creation the life cycle status changes from New to In Planning.
2. **Plan transportation**, in one of four ways: manual planning in the transportation cockpit (drag freight units onto resources, creating a freight order shown in the document flow); **determination of a route** (the system proposes alternative routes per freight unit, and Customizing for the order type decides whether accepting saves only the freight units or also the freight orders; if freight orders are saved, status becomes Planned); **automatic planning** with the VSR optimizer from the cockpit; or **direct creation of freight documents** (freight orders or bookings for the stages, or selecting available freight bookings). When all freight units are planned, the status changes to Planned.
3. **Calculate charges**, if activated for the order type. The system recalculates on every save, but manually entered charges are fixed and kept. An Estimate Forwarding Charges function gives a quick estimate; a profitability analysis is available on its own tab.
4. **Create a forwarding settlement document** (see below).
5. **Print documents**; the print history appears under Output Management.
6. **Edit or cancel.** Most data (dates, quantities, locations, items) can still change, even after planning or execution start; freight units and follow-on documents such as freight orders and bookings are adjusted when saving. Once execution data has moved the freight unit to On Hand, the system no longer adjusts follow-on documents and asks you to change them manually. Canceling deletes the freight units, sets the status Canceled and cannot be undone; an order with an assigned freight document cannot be canceled (H04).
7. **Execute and track.** With the Customizing indicator set, SAP Event Management monitors the order, and the order receives a tracking ID the ordering party can use on a web UI. The execution status reflects the freight order's status (cumulated if several freight orders exist) (H04).

## Forwarding quotation: a quotation from a carrier or LSP to an ordering party with price and conditions; structured like the order plus a validity scope and a quotation price; its life cycle status values are New, Not Transferred, Transferred and Canceled; it is set up with a forwarding quotation type and can be converted into a forwarding order
A forwarding quotation is a quotation from a carrier or LSP to an ordering party about transporting goods, with price and further conditions. It helps send the data of a potential order together with the quotation price, and the order is created when the ordering party places it (H04).

**Structure.** Like the forwarding order, plus a **validity scope** (checked when an order is created from the quotation) and a **quotation price** (a total price without detailed charges; if charges are specified, their total is shown; the quotation price is not displayed if the calculation profile calculates at stage level) (H04).

**Life cycle status** (H04; planning and execution statuses are removed):

| Status | Meaning |
|---|---|
| New | Newly created, not yet sent |
| Not Transferred | An already sent quotation was changed; the changes were not yet sent |
| Transferred | Sent to the ordering party |
| Canceled | Canceled (irreversible) |

**Process** (H04): enter data on the initial screen (set up with a **forwarding quotation type** defined in Customizing; its shipping type and mode must match the order type if orders will be created from it), save, determine the route, calculate charges (or enter just a quotation price), send and print (history on the Output Management tab), accept or reject (rejection sets a reason code and cancels it), then create the forwarding order or cancel. A quotation can also be created automatically from an electronic request for quotation, for example in tendering, and then appears in the POWL. When the order is created from the quotation the system copies the route data and the price calculation and checks validity; the quotation type can limit how many orders may be created from one quotation. A quotation can also be locked, manually or automatically (for example by approval workflow or dangerous goods check) (H04).

## Forwarding settlement document: created from the forwarding order (Costs/Settlement menu) when activated for the forwarding order type, based on the charge calculation; if one exists, changes either flow through the forwarding settlement change process (Reverse and Repost or Delta Only in the settlement profile) or require canceling the document
When activated in Customizing for the forwarding order type, you create a forwarding settlement document from the order, based on the transportation charge calculation, via the Costs/Settlement menu (H04). It triggers the invoice creation process (H04).

If a forwarding settlement document or internal settlement document already exists and a change is needed (for example quantities, shipper or consignee), there are two cases (H04):

- the **forwarding settlement change process** is activated: you enter the changes in the order and the change process triggers the needed changes in settlement. You activate it in the settlement profile by selecting **Reverse and Repost** or **Delta Only**; the profile is assigned via the organization or organization plus business partner.
- it is **not activated**: you must cancel the settlement document, change the order, and create a new document.

A set settlement block prevents creating the document, and the life cycle status Partially Invoiced shows an order mid-invoicing (H04). *Detailed settlement mechanics belong to the settlement session; this material only covers the link from the order.*

## Practice
Write a one-page walkthrough of a forwarding order from quotation to forwarding settlement document. Cover the creation options, the screen areas, the ordered and actual route, the main status values and the blocks that can stop it. Write it so that a colleague can follow the document flow.

## Self-check
Can I explain how a forwarding order is created, which statuses it passes through and how it connects to the quotation, the freight units and the forwarding settlement document to a project stakeholder without notes?
