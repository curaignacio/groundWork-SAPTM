# Session 10 — Settlement

## Overview
Settlement is where the transportation plan turns into money documents. TM calculates the charges, but it does not invoice or pay anything itself: it creates settlement documents and hands them to other modules. A freight settlement document (FSD) goes to Materials Management (MM) so the carrier invoice can be verified. A forwarding settlement document (FWSD) goes to Sales and Distribution (SD) so a customer can be billed. Internal settlement documents move cost between organizations of the same company. This session covers the three document types, how a shipper differs from a logistics service provider (LSP), the statuses that tell you where a document stands, and how late changes, cost distribution, self-billing and disputes work (H09, S48600, S4TM3).

## The four business requirements settlement covers (H09, Use): a freight settlement document created in TM for transportation services provided by a carrier and transferred to Materials Management (MM), where received invoices are verified against it; a forwarding settlement document that bills a customer and is transferred to Sales and Distribution (SD), which sends the invoice; an internal settlement document for a transportation service provided by an internal organization of the company; and an internal settlement document for the resources used in a freight order and provided by another internal organization.
H09 (Use) lists four requirements that settlement meets:

1. **Towards the carrier.** TM creates a freight settlement document for the transportation services a carrier provides to you and transfers it to Materials Management (MM). You verify the invoices you receive from the carrier against the information in the freight settlement document.
2. **Towards the customer.** TM creates a forwarding settlement document to bill a customer for transportation services you provide. TM transfers it to Sales and Distribution (SD), and SD sends the invoice to the customer.
3. **Between internal organizations, for a service.** An internal settlement document for a transportation service provided to you by an internal organization of your company. That organization bills you to recover the cost of the service it provided when you fulfilled a forwarding order for a customer.
4. **Between internal organizations, for resources.** An internal settlement document for the resources you use in a freight order, billed to you by another internal organization of your company.

A compact way to remember the direction of each document:

| Direction | Document | Posted to |
|---|---|---|
| Towards a customer | Forwarding settlement document (FWSD) | SD |
| Towards a carrier | Freight settlement document (FSD) | MM |
| Between internal organizations | Internal settlement document | SD (intercompany) or financial accounting (intracompany) |

*What the material does not establish:* H09 notes that the group logistics scenario in system internal integration is not released, and the internal settlement for resources section states that its features are not yet released.

## Settlement for shippers versus settlement for logistics service providers (LSPs): a shipper follows the freight settlement process with its carrier or LSP and can add cost distribution to allocate freight cost to each order or delivery item for financial accounting and controlling (H09, Settlement for Shippers). An LSP combines forwarding, freight and internal settlement documents
**Shipper.** For a shipper, the carrier or LSP provides a freight transportation service. The shipper follows the freight settlement process with that carrier or LSP. It can also use cost distribution to spread the freight cost down to each individual order or delivery item in the freight order, so the cost reaches financial accounting and controlling. The system does the distribution when it creates the FSD, and the FSD with the distributed costs is posted to MM and to settlement management. When the carrier's invoice arrives, the shipper verifies its amount against what was transferred to MM, and pays if they match (H09, Settlement for Shippers).

**LSP.** An LSP sells transportation to customers and buys it from carriers, so it combines all three documents. H09 (Settlement for LSPs in an Ocean Freight Scenario) describes an LSP whose sales organizations take forwarding orders, and an internal gateway organization that runs a container freight station, consolidates shipments from different sales organizations and books with the ocean carrier. The gateway creates an intercompany internal settlement document against the sales organization to recover the ocean booking cost and extra costs such as consolidation. Only the sales organization is in contact with the customer.

In H09's terms, a gateway is both a sales organization for internal sales and a purchasing organization for buying freight services from carriers, usually the main carriage.

## The three agreement types and who the parties are in the ocean freight example: forwarding agreements (export station and shipper, import station and ship-to party, export station and import station), freight agreements (each station or gateway with its carrier) and an internal agreement (gateway and export station)
H09 (Agreements) sets out the agreements behind the ocean freight example. The key abbreviations: STA is a station (usually the sales organization of an LSP), STA-NUE the export station at Nuremberg, STA-DLS the import station at Dallas, CFS-RTM the Rotterdam export gateway.

| Agreement type | Parties | Reason |
|---|---|---|
| Forwarding agreement | Export station (organization) and import station (business partner) | Provide main carriage services |
| Forwarding agreement | Export station (organization) and the shipper CU-NUE (business partner) | Move the cargo from Nuremberg to Rotterdam as agreed in Incoterm FOB |
| Forwarding agreement | Import station (organization) and ship-to party CU-DLS (business partner) | Freight services from Rotterdam to the ship-to party location in Dallas |
| Freight agreement | Export station and Carrier 1 | Pre-carriage |
| Freight agreement | Rotterdam gateway CFS-RTM and ocean Carrier 2 | Ocean freight |
| Freight agreement | Import station and Carrier 3 | On-carriage |
| Internal agreement | Gateway CFS-RTM (organization) and export station (business partner) | Main carriage and other consolidation services |

The pattern: forwarding agreements run towards the sold-to side (customers, or internal stations acting as customers), freight agreements run towards carriers, and the internal agreement sits between the gateway and the export station.

*Source note:* the H09 text spells the stations inconsistently (STA-NUE and STA-NEU, STA-DLS and STA-DLA, Newark CFS-NWK); read them as the same stations.

## Prepaid and collect agreement parties and Incoterms in the example: with FOB to Rotterdam the shipper pays the pre-carriage, the ship-to party pays main carriage and on-carriage, and the business unit closest to the external customer settles with that customer
In the example the customer in Dallas uses Incoterm FOB to Rotterdam (H09, Incoterms). The shipper CU-NUE in Nuremberg pays the pre-carriage. The ship-to party CU-DLS in Dallas pays the main carriage and the on-carriage.

In the forwarding order the shipper CU-NUE is the **prepaid agreement party** and the Dallas import station STA-DLS is the **collect agreement party**. H09 gives the reason for the second choice: the business unit closest to the external customer settles with the external customer, so the ship-to party in Dallas pays the sales organization in Dallas.

The money then flows as follows (H09, Incoterms; Forwarding Settlements; Freight Settlements):

- The Nuremberg export station pays the carrier for the pre-carriage (Carrier 1 invoices USD 400) and bills the shipper USD 500 through a forwarding settlement document.
- The Rotterdam gateway pays the ocean carrier for the main carriage (USD 2000) and settles internally with the Nuremberg export station.
- The Nuremberg export station recovers the main-carriage cost from the Dallas import station (billing document USD 2200).
- The Dallas import station pays Carrier 3 for on-carriage (USD 400) and bills the ship-to party USD 2800 for main carriage and on-carriage.

## Internal settlement based on agreed internal rates or on actual carrier costs: the gateway pays its carrier USD 2000 and bills the export station USD 2200 on internal rates (USD 200 profit), or bills USD 2000 on actual costs (no profit)
The gateway CFS-RTM receives a carrier invoice of USD 2000 for the main carriage. Two ways to settle internally (H09, Internal Settlements):

- **Agreed internal rates.** The gateway bills the export station USD 2200 based on the rates agreed between the organizations. The gateway makes USD 200 profit.
- **Actual costs.** The internal settlement document is based on the carrier's actual cost. The gateway bills USD 2000 and makes no profit.

H09 states both options as possible and does not recommend one over the other. The profit versus pass-through difference is the practical distinction: rates give the gateway a margin, actual cost passes cost through unchanged.

## Consolidated shipment: the gateway sends an internal settlement document for the main-carriage cost to each internal export organization, based on agreed internal rates (standard agreed rate) or on the cost of execution; for cost-based settlement it uses cost distribution to determine each forwarding order's share of the freight booking cost
A consolidated scenario differs from the single shipment: the Rotterdam gateway consolidates several forwarding orders from different organizations in the company, moves them to the Newark import container freight station, which deconsolidates, and the import stations deliver to the ship-to parties. The gateway then sends an internal settlement document for the main-carriage cost to each internal export organization (H09, Consolidated Shipment). Two bases are possible:

- **Agreed rates.** The gateway uses a standard agreed rate to settle the cost of each forwarding order it consolidates and ships (see Standard Charge Calculation in the source).
- **Freight costs.** The gateway must work out each organization's share of the overall execution cost. It uses cost distribution to distribute the freight booking cost down to the forwarding order level, then uses those distributed costs to create the settlement. H09 refers to Cost Pull for transferring distributed costs from the freight side to the forwarding side.

## Internal settlement for resources: intercompany settlement (different company codes, posted to SD) versus intracompany settlement (same company code, posted to financial accounting, Intracompany Settlement checkbox on the Org. Data tab), and the prerequisites of an internal agreement with Resource specified and a freight order type enabled for internal settlements
This is the fourth business requirement: settling the cost of your own resources (trucks, trailers) used in a freight order. H09's example has a sales organization SALES_1, a resource organization RESOURCE_1 that owns a trailer, a purchasing organization PUR_1 and a carrier CARRIER_1 who provides the truck. The documents are:

- the sales organization's forwarding settlement document for each customer's forwarding order, posted to SD;
- an internal settlement by the purchasing organization against the sales organization, to recover the truck and trailer cost;
- an internal settlement by the resource organization against the purchasing organization, to recover the trailer cost;
- a freight settlement document by the purchasing organization against the carrier, posted to MM and later checked against the carrier's invoice.

**Intercompany versus intracompany.** If the organizations belong to different company codes, the internal settlement is intercompany and is posted to SD, which creates a billing document. If they belong to the same company code, it is intracompany and is posted to financial accounting, which reposts the primary costs to an internal order or cost center. For intracompany settlement you select the **Intracompany Settlement** checkbox on the Org. Data tab page of the company organization (transaction PPOCE) (H09, Internal Settlement).

**Prerequisites for resources (H09, Internal settlement for resources).** The freight order type is enabled for internal settlements, with the internal settlement document type assigned to it. The resource is defined (transaction /SCMTMS/RES01 or the Define Resources app) with its organizational unit set as a sales organization, sales group, sales office or forwarding house. There is an internal agreement between that organizational unit and the business partner of the purchasing organization or group of the freight order, with **Resource** specified in the Resource field on the General Data tab of the internal agreement. The general internal settlement prerequisites also apply. H09 marks these resource features as not yet released.

## The forwarding settlement document (FWSD): posted to SD to request an invoice, created individually for one forwarding order (FWO) or collectively for several, with tabs General Data, Business Partner, Charges, Orders, Document Flow and Application Log
H09 (Forwarding Settlement Document) defines the FWSD as a document posted to SD to request the creation of an invoice for a customer. TM calculates the charges based on a forwarding order (FWO), and posting the FWSD makes SD create the invoice. You can create an individual FWSD for one FWO or a collective FWSD for several FWOs. Credit memos are also triggered from TM and created in SD.

The FWSD data comes from the FWOs and is organized in tab pages:

| Tab | What it shows |
|---|---|
| General Data | Invoice date, sales organization, payment terms, total amount, document currency |
| Business Partner | Sold-to party, bill-to party and payer by default; business partner determination fills gaps |
| Charges | Charges per FWSD item, which is an FWO or an FWO item depending on the calculation level in the calculation profile |
| Orders | The FWOs or FWO items being settled |
| Document Flow | Predecessor and successor documents, including the SD billing documents created on posting |
| Application Log | Error and warning messages from posting to internal SD |

Prerequisites include FWSD types and number range intervals, and a forwarding settlement profile assigned to the charges profile of the sales organization used in the forwarding order (H09, Forwarding Settlement).

## FWSD life cycle statuses (In Process, Ready for Posting, Posted, Posting Started, Cancellation Requested, Canceled, Canceled by Credit Memo) and confirmation statuses (Not Yet Posted, Posting Successful, Posting Failed, Cancellation Successful, Cancellation Failed, Posting Started)
The life cycle status shows where the FWSD is in the business process. The confirmation status mainly tracks the integration with SD and shows the result of the last interaction between TM and SD (H09, Forwarding Settlement Document).

| Life cycle status | Meaning |
|---|---|
| In Process | Information is incomplete or missing |
| Ready for Posting | Ready to post to SD |
| Posting Started | Posted to SD, posting not yet finished |
| Posted | SD successfully created the billing document |
| Cancellation Requested | Cancellation requested from SD, not yet finished |
| Canceled | FWSD and its SD billing document canceled |
| Canceled by Credit Memo | A credit memo for the full FWSD amount was created and posted |

| Confirmation status | Meaning |
|---|---|
| Not Yet Posted | Not yet posted to SD |
| Posting Started | Transferred to SD, SD status not yet known |
| Posting Successful | SD created the billing document |
| Posting Failed | SD failed to create it; you must check why manually |
| Cancellation Successful | SD canceled the billing document |
| Cancellation Failed | SD failed to cancel the billing document |

Reading them together: a life cycle status of Ready for Posting with confirmation Not Yet Posted is a document waiting for you. Posted with Posting Successful is finished. A document stuck in Posting Started with a confirmation of Posting Failed needs investigation.

## The forwarding settlement process: create the FWSD, review it (invoice preview, deviating bill-to address), transfer with Save and Post, SD confirms billing document creation; cancellation can be requested at any time; failed posting is checked in the Application Log tab or, for external SD, in transaction SXI_MONITOR
H09 (Forwarding Settlement, Process) gives four steps:

1. **Create the FWSD.** Individually or collectively, from the personal worklist, the Forwarding Order Management Overview or the Forwarding Settlement Overview. The system creates it from the FWO data and calculates the charges. FWOs with Incoterms or freight terms are covered. In a collective creation, split criteria can lead to more than one FWSD. Batch creation is available with the Creation and Transfer of Forwarding Settlement Documents function.
2. **Review.** You can preview the invoice as it would appear in SD, including tax information determined from SD. The preview works at any life cycle status except Posting Started, Posted, Cancellation Requested and Canceled, and the document must be Consistent. You can overwrite the automatically determined address of the bill-to party on the Business Partner tab of the FWO or FWSD, and the SD billing document then carries that deviating address.
3. **Transfer to SD.** Choose **Save and Post**. With SD on an external SAP S/4HANA or SAP ERP system, the system posts through enterprise services.
4. **SD confirms billing document creation.** The life cycle status changes to Posted. If it failed, the confirmation status shows posting failed. For an internal SD, check the **Application Log** tab. For an external SD, check the enterprise service message log in transaction **SXI_MONITOR**.

Cancellation can be requested at any time, even when the status is Posted. If SD cancels the billing document the FWSD becomes Canceled, otherwise it shows the confirmation status Cancellation Failed. You can also create an FWSD for a canceled FWO to recover costs already incurred, by adding charges manually.

## Manual changes and follow-up FWSDs: changes to payment terms, notes and attachments, charges, invoice date, service date, payer or a deviating bill-to address flag the document as manually changed; a follow-up FWSD proposes the charge amount minus amounts already invoiced and is Inconsistent if the result is zero or negative
**Manual changes.** If you change an individual FWSD or internal settlement document by hand, the system flags it as manually changed. H09 counts changes to payment terms, notes and attachments, charges, invoice date, service date, payer, and a deviating address for a bill-to business partner. The flag is visible in the personal object worklist for FWSDs. The worklist also shows the **creation method**: Manual, Background Processing, or Change and Background Processing (H09, Forwarding Settlement).

**Follow-up FWSDs.** You can create a second or later FWSD after one already exists. The system:

1. copies the charges from the forwarding order (all charge lines as they are, or fixed charges with the rest recalculated, depending on the calculation option in the settlement profile);
2. for each charge line, subtracts the amounts already invoiced in earlier, non-canceled FWSDs, and proposes the result as the invoiced amount.

If the result is negative (customer over-invoiced) or zero (completely invoiced), the follow-up document gets consistency status **Inconsistent**, which blocks transfer to SD until the zero or negative amount is removed. Ways forward: run the background function (program /SCMTMS/CFIR_CREATE_BATCH) if automatic change management is enabled, cancel the existing document and replace it (the FWO must not be Completed), or create a credit memo manually for the over-invoiced amount.

## Execution-based settlement and the Settlement Basis field of an agreement item: by default TM settles per individual forwarding order; with a settlement basis (route-based, trailer-unit-based, or buyer's consolidation as a variant) the settlement item is the execution document, and its charges are calculated only in the forwarding settlement document
By default TM settles per individual forwarding order. An LSP may instead need to settle on how the order was executed. H09 (Execution-Based Settlement) names three criteria: buyer's consolidation, route, and trailer unit. You choose them in the **Settlement Basis** field of the agreement item (route-based and trailer-unit-based) and, for buyer's consolidation, through the BCO setting described in the next item.

| | Execution-based settlement | Forwarding-order-based settlement |
|---|---|---|
| Settlement item | Execution document, such as trailer unit or container | Forwarding order |
| Resolution base grouping rule | Across forwarding orders in the execution document, for execution stages | In the forwarding order |
| Data source (stages, quantities) | Execution document, such as freight booking item or trailer unit | As specified in the settlement profile |

In the FWSD the settlement items become the container item of the booking (buyer's consolidation), the trailer unit, or the freight order (route-based). Creating an FWSD for an FWO with an execution-based basis produces one FWSD for all FWOs in the execution document for one customer. Constraints: the forwarding settlement settings are in place, the right basis is on the forwarding agreement item, and the charges for the execution-based stages are calculated only in the FWSD, not in the individual FWO.

**Worked example (H09).** Seven forwarding orders are delivered on one trailer unit. With Trailer Unit empty in Settlement Basis, TM rates and settles each of the seven individually and creates one FWSD with seven line items, even for a collective settlement. With Trailer Unit in the field, you settle on one rate for the trailer unit covering all seven.

Route-based use case: a customer who wants one agreed rate for the full journey of a truck picking up at several places and delivering to several, not a price per forwarding order.

## Buyer's consolidation settlement: the BCO setting in the Buyer's or Shipper's Consolidation field, a separate calculation sheet in the agreement item, one consolidated settlement for all forwarding orders in the container item, and a fallback to an agreement line with shipping type FCL
In a buyer's consolidation the LSP loads goods from several suppliers of one customer into one container before the main carriage, so it does not charge an LCL rate and passes on the FCL rate for main carriage and on-carriage (H09, Buyer's Consolidation Settlement).

Prerequisites:
- BCO in the **Buyer's or Shipper's Consolidation** field of the forwarding order on the export side;
- an agreement item for the buyer's consolidated main carriage and on-carriage with a **separate calculation sheet** and BCO in the same field.

Behavior:
- It is a variant of execution-based settlement: on the export side the main-carriage charges come from the freight booking container item.
- If the container items in the freight booking carry BCO, the system creates **one consolidated settlement for all forwarding orders in the container item** for the main carriage.
- **Fallback:** the system looks for an agreement line item with BCO; if none, it looks for an agreement line with shipping type **FCL**.

Example in H09 (Incoterm EXW): with three pickup locations there are three forwarding orders on the export side. The export business unit bills the import business unit for each pickup and one single FWSD for the main carriage. On the import side, the system copies the forwarding order with a reference to the container item, and the import unit bills the ship-to party for pickups, main carriage and delivery.

## The freight settlement document (FSD): created for freight orders, freight bookings and service orders (or consignment orders); posting it to MM creates a purchase order for services and a service entry sheet (SES), books accruals, and is the basis for invoice verification or evaluated receipt settlement (ERS, self-billing)
H09 (Freight Settlement Document) defines the FSD as the document used for posting freight cost accruals and the basis of invoice verification in MM for freight documents. It can be created for freight orders, freight bookings and service orders (H09 and S4TM3 also mention consignment orders for settlement). Settlement of service orders needs Freight Settlement Integration using MM External Services Management (H09).

**What posting does in MM.** Posting the FSD creates a **purchase order for services** and a **service entry sheet (SES)** with the values of the TM charge lines. The SES confirmation is done at the same time, which creates the financial entries for the freight cost, that is, the accruals. When the carrier invoice arrives, logistics invoice verification in MM (transaction MIRO) checks it against this data. In evaluated receipt settlement (ERS, self-billing) the automatically generated invoice is built from the same data (H09; S4TM3).

S48600 and S4TM3 add that the purchase order and SES are used for technical purposes, to post accruals, and form the working list for invoice verification. In stage-level charge calculation the PO has as many items as the freight order has stages, and one SES per PO item (S4TM3). The PO and SES can be opened through ME23N or the TM document flow (S4TM3).

The FSD tabs mirror the FWSD: General Data (document type, settlement date, **procuring company code**, purchasing organization and group, payment terms, **net amount**, currency, **verified invoice amount**), Business Partner (carrier, invoicing party, payee), Charges, Orders, Document Flow (including the PO, SES and invoice in MM), Application Log.

## The freight settlement process steps: create the FSD (individual, collective, or mass creation with /SCMTMS/SFIR_CREATE_BATCH), review it until it is Consistent and Ready for Accruals, then post it to MM; the settlement date defaults to today's date and the posting runs asynchronously
H09 (Freight Settlement, Process) with the exercise E05:

1. **Create the FSD.** Individually, collectively (several freight orders, service orders or freight bookings), or with **mass creation**: transaction /SCMTMS/SFIR_CREATE (report /SCMTMS/SFIR_CREATE_BATCH). S4TM3 lists /SCMTMS/SFIR_TRANSFER_BATCH as the report for posting FSDs to MM. Separate FSDs can be created per stage of freight orders with non-linear stages, per invoicing carrier in a rail freight order, and per additional agreement party. The **settlement date defaults to today's date**; you can override it through a BAdI or by entering a date in the mass creation function.
2. **Review.** Check and edit details. After saving, an automatic consistency check runs. If it succeeds, the consistency status becomes **Consistent** and the life cycle status becomes **Ready for Accruals**.
3. **Post to MM.** Choosing Post sends the data to MM, including source and destination location for each stage so MM can determine tax rates. The posting runs **asynchronously**. The settlement date becomes the document date of the purchase order and the posting date of the SES.

**What you see in the exercise (E05, Create and Post a Freight Settlement Document and Verify the Invoice).** The FSD for freight order 200000109 shows Ready for Accruals and confirmation Not Posted. After Post, the life cycle status goes to Posting Started with confirmation Not Confirmed, and after Refresh to Posted and Confirmed. The Document Flow shows freight order, freight unit, outbound deliveries and sales orders before the FSD, and the purchase order and SES after it. The carrier invoice is then posted in transaction MIRO (company code 1010, invoice date, freight order number, tax code V1, amount 1961,62 EUR, with a remaining balance of 0,05 EUR). After posting, the FSD shows **Invoice Verified**.

## FSD life cycle and confirmation statuses (In Process, Ready for Accruals, Posting Started, Posted, Invoice Verified, Cancellation Requested, Canceled, Reversal Requested, Reversed, Credit Memo Created; Not Posted, Not Confirmed, Confirmed, Posting Failed and the specific failure statuses)
From H09 (Freight Settlement Document):

| Life cycle status | Meaning |
|---|---|
| In Process | Not yet ready to post to MM |
| Ready for Accruals | Ready for you to post accruals in MM |
| Posting Started | Posting initiated, not yet complete |
| Posted | Posted successfully; PO and SES created in MM |
| Invoice Verified | At least one invoice has been posted against the FSD in MM |
| Cancellation Requested | Cancellation requested, not yet complete |
| Canceled | You canceled the FSD |
| Reversal Requested | Reversal requested, posting of the reversal not complete |
| Reversed | Reversed in MM |
| Credit Memo Created | A credit memo posted against a reversed FSD in MM |

| Confirmation status | Meaning |
|---|---|
| Not Posted | Not yet posted to MM |
| Not Confirmed | Posting initiated, not complete |
| Confirmed | Posted successfully to MM |
| Posting Failed | Posting to MM not successful |
| No Confirmation | Posted but MM status not yet known |
| Cancellation Posting Failed, Reversal Failed | Cancellation or reversal posting failed |
| Purchase Order Creation Failed, SES Creation Failed | The failed step when posting; see the Application Log tab |
| SES Cancellation Failed, Purchase Order Cancellation Failed, SES Reversal failed | The failed step when canceling or reversing |
| Cost distribution document creation failed, cancellation failed, reversal failed | The settlement management documents with cost distribution data could not be created, canceled or reversed |

Note that S48600 and the carrier-invoice conditions text refer to the FSD status as **Accruals Posted**, while H09 names the status **Posted**; read them as the same state.

## Prerequisites for freight settlement: FSD types and number range intervals, and a freight settlement profile assigned to the business partner (carrier role) and purchasing organization; the procuring company code books the accruals and the plant is needed for the service purchase order
H09 (Freight Settlement, Prerequisites) and S48600 (Freight Settlement Document Creation - Configuration):

- **FSD types and number range intervals** are defined in Customizing. When FSD creation is triggered for a freight order or freight booking, its document type determines the FSD type (S48600).
- **A freight settlement profile**, assigned to the business partner (BP role Carrier, Vendor Org. Data for the relevant purchasing organization, Additional Settings, FSD Profile ID) and to the charges profile of the purchasing organization. When a freight order is created the system checks first the business partner of the purchasing organization, then the charges profile. If no profile is found in either, an error is shown when you create the freight order. The purchasing organization in the freight document determines the settlement profile (S48600).

**Company code and plant (H09, Company Code and Plant in Posting Freight Settlements).** The company code books the freight accruals to financial accounting. The plant is required to create the service purchase order during posting.
- The **procuring company code** is responsible for procuring the transportation service. It is taken from the freight document (General Data, Organizational Data), and is determined automatically if a unique company code is assigned to the purchasing organization. It is determined only when the order type is relevant for subcontracting and subcontracting checks are set. It then carries over to the FSD.
- For the **plant**, the system uses (in order) the plant from the FSD type Customizing (Assign Purchasing Information for Posting), the unique plant of the underlying orders and deliveries from the linked freight units, or the default plant for the company code. When the procuring company code is mandatory for subcontracting, SAP recommends not specifying the plant in Assign Purchasing Information for Posting, so company code and plant can be determined more flexibly.

## Reversing an FSD and changes after posting: reversal is only possible in life cycle status Invoice Verified and ends with a credit memo through transaction MRRL; added or changed charges lead to Partially Invoiced (new FSD) or Over Invoiced (credit memo or reverse and repost)
**Reversal (H09, Reversing a Freight Settlement Document).** The typical case: you use self-billing (ERS) with a close carrier, accrued the cost and created a self-billing invoice, and then the carrier does not deliver (for example a vehicle breakdown) or TM holds incorrect prices. You can only reverse the FSD when its life cycle status is **Invoice Verified**.

| Step | Module | Result | FSD status |
|---|---|---|---|
| Choose Reverse Document in the FSD | TM | Reversal initiated; an SES with a returns flag for the full FSD value is created | Reversal Requested |
| MM creates the reversal posting | MM | Reversal posting of the accruals with a returns indicator on the SES | Reversed |
| Run transaction MRRL (ERS with Logistics Invoice Verification), entering the TM freight order number | MM | Credit memo reverses the previously posted invoice | Credit Memo Created |

TM then sets the invoicing status of the freight order to **Not Invoiced**, and you can create a new FSD for it.

**Changes after posting accruals (H09, Changes After You Post Accruals; S48600, Freight Settlement - Updates).** You can add or change charge amounts directly in the existing freight order, freight booking or service order after accruals are posted, and transfer them to MM. S48600 gives the business reason: accruals are posted when liability is known, but diversions, lost cargo, detention, demurrage, tolls and similar may only become known later or at invoicing.

- With **automatic change management** enabled, the background function Creation and Transfer of Freight Settlement Documents (/SCMTMS/SFIR_CREATE_BATCH) creates, changes and posts FSDs that contain the changes.
- Without it: if the amount makes the invoicing status **Partially Invoiced**, create a new FSD for the delta. If it becomes **Over Invoiced**, create a credit memo in TM to send the changed amounts to MM, or cancel the existing FSD (possible only when its status is not Invoice Verified, and the freight order is not Completed) and create a new one with the full amount. Posting the new FSD or credit memo creates a new PO and SES.
- A follow-up FSD works like the follow-up FWSD: charges are copied, previously accrued amounts subtracted, and a zero or negative result gives consistency status **Inconsistent**, blocking posting.

**Source difference.** S48600 says the FSD change process is configured in the settlement profile and that, when an order changes and the invoicing status becomes Over Invoiced, the system automatically applies a **reverse and repost** strategy. H09 describes the credit memo or cancel-and-replace options when automatic change management is off. Both can be true under different settings, but the material does not reconcile them in one place.

Further H09 rules: you cannot change or delete a charge line with invoicing status Invoice Verified, and for Invoice Verified documents a new charge line produces a new FSD, PO and SES only for the delta. Under the lean services integration the previous FSD, PO and SES are canceled and a new FSD with the updated amount is posted.

## Cost distribution for shippers: freight cost is distributed to the order or delivery item level when the FSD is created and posted; MM gets one purchase order and SES for the net amount while a settlement management document carries the distributed amounts
H09 (Cost Distribution for Shippers): the shipper's orders and deliveries create freight units, planned in freight orders, and an FSD posts the transportation cost to MM for accruals and invoice matching. The distribution must be at the level of order/delivery item in the FSD, and the system does it when the FSD is created and posted.

**Worked example (H09).** A freight order with two deliveries has a net amount of USD 1000, distributed USD 700 to product 1 (delivery 1) and USD 300 to product 2 (delivery 2). On posting the system:

1. creates one purchase order for **USD 1000** and one SES for USD 1000;
2. creates a **settlement management document** with each product as an item carrying its distributed amount, USD 700 and USD 300.

Settlement management uses the underlying sales order and delivery information to find the cost object to post against. For an outbound delivery linked to a sales order, it copies references and the linked delivery items, copies product and quantity, copies the account assignments (cost center, profit center, CO-PA segment or internal order) from the sales order item, and copies the distributed amounts.

H09 also describes the same pattern in the Posting of Allocated Freight Costs section with USD 1845 split into 800 and 1045. There, the SES posts the total to an intermediate freight clearing account (offset key GBB), while the freight cost allocation document allocates to material valuation (inbound) or a general ledger expense account (outbound). The apps Manage Freight Cost Allocation Documents and Monitor Freight Cost Allocation Document Items let you review them, and the system normally releases the documents to accounting automatically.

S4TM3 and S48600 summarize the flow as: deliveries create freight units, freight orders are planned, charges are distributed to delivery items, the FSD is created, and posting creates PO and SES for invoice verification plus a settlement document for CO-PA, CO or material valuation.

## Cost distribution configuration: enabled in the document type, distribution profiles assigned through the charges profile, methods Direct and Hierarchical, rule basis Gross Weight, Gross Volume, Net Weight or Distance times Weight, and viewing of posted data with WLFLTM2
S48600 (Cost Distribution) gives the configuration summary:

- Cost distribution is **enabled in the document type** Customizing.
- A **distribution profile** (method, rule, level) is assigned to the organizational unit through the **charges profile** (H09 adds: and the charges profile is assigned to the purchasing organization on the Org. Data tab in the organizational model).
- **Methods:** *Direct* distributes charges to the line items by the chosen rule regardless of packaging hierarchy, normally when all charges can be distributed to delivery line items by gross weight or volume. *Hierarchical* works step by step through each packaging level, used when the resolution base includes containers or rail cars, so other charges go to the container level first and then to the line item level.
- **Rule basis:** Gross Weight, Gross Volume, Net Weight, Distance times Weight.
- **Distribution level:** the target level, forwarding order or order/delivery item.
- **Viewing posted data:** transaction **WLFLTM2** or Display Cost Distribution Documents, searchable by FSD number.

H09 adds limits: internal cost distribution cannot be enabled for a freight booking, and a document mixing forwarding order items and order/delivery items can only be distributed to one level. Charges can also be assigned directly (for example packaging and labeling of a specific product), in which case the rule has no influence (H09).

## Billing freight costs to customers: distributed costs per delivery item can be added to the SD billing document, which needs SD integrated with TM, one freight order for the delivery and one currency
A seller who takes responsibility for delivery can pass transport costs on. TM is set up to distribute freight cost to delivery items, and the distributed cost per delivery item is added to the amount in the SD billing document (H09, Billing the Freight Cost in TM to a Customer in SD; S48600, Billing Freight Costs). It involves freight orders in TM and pricing and billing in SD.

**Conditions:** SD must be integrated with an internal TM component, there is one freight order document for the delivery, and the freight order has only one currency for the cost.

**Worked example (H09).** Freight order with two deliveries, gross weights 2,250 kg and 2,750 kg. Charges: base freight 1,000 and fuel surcharge 250 (both at Root), packaging 50 for product 1 and 100 for product 2. Distribution by gross weight gives delivery 1: 450 base freight + 112.50 fuel + 50 packaging = 612.50; delivery 2: 550 + 137.50 + 100 = 787.50. The SD billing document uses 612.50 and 787.50 USD for the two delivery items.

**In the exercise (E05):** the Cost Distribution tab shows delivery 80000175 covers 390.15 EUR, the handling charge assigned fully to it and others allocated by gross weight. Creating the billing document with the Create Billing Document app shows pricing element FB00 representing freight charges of 390,15 EUR taken over from the freight order or FSD.

## Self-billing (ERS) versus invoice submission by the carrier, the automatic dispute case created for a carrier invoice that differs from the freight order, and the conditions for posting carrier invoices to MM
H09 (Dispute Management for Freight Settlements) and S48600 describe two freight settlement processes between a shipper and a service provider:

- **Self-billing (ERS):** the service provider does not submit an invoice; you settle automatically on the information in your freight order.
- **Invoice submission:** the provider submits an invoice and you pay the amount in it. In TM this uses enterprise services: the provider creates an invoice in its external system and sends it, and you use it to create a **carrier invoice** in TM.

In both there can be differences between what you expect to pay and what the provider expects. In invoice submission TM evaluates the external invoice automatically. If values differ (unplanned costs, different charges, changed logistics data), TM **creates a dispute case** automatically, linked to the carrier invoice, and captures each charge difference as a dispute item. If nothing differs, no dispute case is created. As shipper you approve or reject the dispute case (Dispute Cases Worklist app). Approving updates the freight order's charge information such as rate and quantity, but **not** logistics information such as gross weight, gross volume or total distance. Benefits named: changes and unplanned costs go into one invoice, and payment is accurate.

**Typical steps (H09):**
1. TM creates an FSD for a freight order and posts it to MM, creating the PO and SES.
2. The provider submits an invoice by enterprise services; TM creates the carrier invoice and, if needed, the dispute case.
3. You accept or reject. Rejecting the carrier invoice closes any open dispute case and sets the carrier invoice to Rejected; you can add a note with the reason.
4. Accepting the dispute case updates the freight order with the new charges, and the background function Creation and Transfer of Freight Settlement Documents moves the changes to MM.
5. The background function **Posting of Carrier Invoices** transfers ready carrier invoices to MM, creating an incoming invoice.

**Conditions for posting a carrier invoice to MM:**
- no dispute case exists, or it has life cycle status **Resolved**;
- the carrier invoice is not **Rejected**;
- all associated freight orders have invoicing status **Completely Invoiced**;
- all associated FSDs have reached the accrual-posted status (named Accruals Posted in the source);
- the carrier invoice is **Not Blocked**;
- the carrier invoice is **Consistent**.

H09 also notes that dispute management applies a tolerance check configured in Customizing; a dispute case that fails the tolerance limits must be reviewed manually.

## Practice
Create a one-page settlement map for a shipper and an LSP in your own words. For each settlement document (forwarding, freight, internal) list who creates it, what it is based on, which module it is posted to, and the statuses that show it is finished. Add one worked example of a freight order with cost distribution, such as the USD 1000 split into USD 700 and USD 300.

## Self-check
Can I explain to a finance controller, without notes, how a freight order becomes a freight settlement document, accruals and a verified carrier invoice, and when a forwarding or internal settlement document is used instead?
