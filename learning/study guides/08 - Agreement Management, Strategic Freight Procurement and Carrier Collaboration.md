# Session 08 — Agreement Management, Strategic Freight Procurement and Carrier Collaboration

## Overview
This session covers how a shipper buys long-term transportation capacity in TM and how carriers take part. Agreement Management is the component that holds the contracts (agreements) on which charge calculation rests. Strategic freight procurement (SFP) is the process that produces those contracts: the shipper details its transport needs in a freight agreement RFQ master, carriers bid, the shipper compares the bids and distributes target shares, and freight agreements are generated. Carrier collaboration lets carriers answer without running TM themselves, and the carrier apps for order management cover the operational side once agreements exist. In practice this is where rates, shares and carrier relationships are decided, and what is decided here later drives carrier selection in planning and charge calculation (session 09).

## Purpose of Agreement Management: shippers and LSPs forecast and assess transportation requirements, request bids from carriers and negotiate contracts (agreements); carriers use it to respond with rates; agreements are the basis for charge calculation, and Agreement Management is integrated with Charge Management and Service Product Catalogs
As a shipper or logistics service provider (LSP), you use Agreement Management to forecast and assess your transportation requirements, request bids from carriers for them, and negotiate contracts (agreements) with carriers. The stated aim is to keep transportation costs down and to manage carrier contracts efficiently. As a carrier, you use it to respond to shippers or LSPs with your rates for transportation services (H08).

Agreement Management also lets carriers, shippers and LSPs set up and maintain agreements, which are the basis for calculating transportation charges (H08). H08 groups the features into three blocks:

- **Strategic freight procurement:** the shipper or LSP details requirements, requests bids, compares them, awards business and negotiates contracts.
- **Rate quotation:** the carrier responds with rates (through the forwarding agreement quotation).
- **Agreements:** long-term contracts as the starting point for charge calculation.

Agreement Management is a component of TM. It is integrated with Charge Management and Service Product Catalogs, because TM calculates charges from the master data in calculation sheets, rate tables and scales, whether these are created locally in an agreement or independently of it (H08).

## Strategic freight procurement (SFP) is tailored mainly to shippers procuring long-term transportation services from carriers or LSPs; it runs in four steps: Prepare RFQ, Submit RFQ, Evaluate responses and optimize, Generate agreements
SFP supports mainly shippers in procuring long-term transportation services from LSPs or carriers. LSPs can use the same scenario to buy from carriers while they sell services to their own clients (S4TM3). H08 states the business reason: the shipper needs low cost but also reliable service, and SFP helps find the best rates for moving items between specific locations (trade lanes) and then agree a contract with the carriers.

The four steps (S4TM3, Unit 6):

1. **Prepare RFQ.** The shipper prepares the procurement with no carrier interaction. Historic transportation is analyzed and used as a forecast for the next period. The need is split by trade lane, commodity code or transportation mode. The last task is to create the central document, the freight agreement master RFQ.
2. **Submit RFQ.** Interaction with carriers starts. The carriers are added to the master RFQ and, if necessary, target business shares are assigned among them. The individual RFQs are created and sent per carrier (with the optional approval where it is selected for the purchasing organization).
3. **Evaluate responses and optimize.** Responses are evaluated and compared. TM creates ranking lists and suggests optimal business shares. Negotiation rounds can be started here.
4. **Generate agreements.** Optimal shares and carriers are awarded for the next period. Freight agreements are generated in one click and act as the contract between shipper and carrier.

H08 gives the same flow in eight numbered actions: create the master, publish, system notifies carriers, carriers respond, evaluate, review comparison and spend estimation, accept preferred strategy, create or update agreements. H08 adds a shortcut: if you already know which carriers get the business, skip evaluation, review and acceptance of the preferred strategy and go straight to creating or updating the agreements.

Prerequisites in Customizing (H08): number ranges for agreement RFQs and quotations, freight agreement RFQ types, target share strategies and strategy conditions (Define Target Share Strategies), output management and business-to-business communication, and the agreement prerequisites. A carrier responding in TM also needs forwarding agreement quotation types.

## Determining procurement needs: historic transportation is analyzed as a forecast and divided by trade lane, commodity code or transportation mode; legacy systems or TM analytics (overview pages, CDS views) can be used, but their use is not mandatory for SFP
Analysis of historic volumes helps create the forecast for the next period (S4TM3). TM analytics offer overview pages (OVPs) that show KPIs for areas such as freight booking, freight ordering, tendering, business share analysis and allocation analysis. CDS views, which are query views on the database, feed information into each overview page. To use an analytics app, the OData service for its Fiori ID must be activated in the Gateway system. SAP Help lists the analytics areas and technical IDs under the search topic "Analytics" (S4TM3).

The course is explicit that this analysis and the forecast are not linked to the freight agreement master RFQ that is created from them. Therefore using the TM analytics is not mandatory, and the first stage can be done in legacy systems (S4TM3).

## Freight agreement RFQ master: the central business document with a shipper's or LSP's transportation requirements for a future period; it can be created with the Manage Freight Agreement RFQ Masters app or from a template, and per S4TM3 from an existing freight agreement, a template, anew, or by copying an RFQ
**Definition (H08).** A freight agreement RFQ master is a business document with the transportation requirements of a shipper or LSP for a specific future period. It is used to select a set of carriers. H08 lists what the master is used for: detail requirements, request capacity and rate quotations, evaluate and compare bids, distribute target share, simulate estimated costs, negotiate and award, and agree contracts. A carrier receives an individual freight agreement RFQ in the form of a forwarding agreement quotation.

**Ways to create it.**

- H08: with the Manage Freight Agreement RFQ Masters app (which shows all masters regardless of status, and lets you create, edit and display), or from a freight agreement RFQ master template. Customizing templates (Define Freight Agreement RFQ Master Templates) are based on industry standards and can be transferred across TM systems. Master data templates are created and maintained with the freight agreement RFQ master template apps (Create FA RFQ Master Templates) and allow simple changes before the master is created.
- S4TM3: from an existing freight agreement (used when the same trade lanes are tendered periodically), from a template, as a new RFQ, or by copying an existing RFQ. In the launchpad: Contract Management, Create Freight Agreement RFQ Master.

**Approval.** *The two sources differ in tone.* S4TM3 first says the master "has to be approved by the head of the purchasing organization" before individual RFQs are created, and later describes the approval as optional where selected for the purchasing organization. H08 describes the approval workflow as something you can enable in the Customizing activity Define Freight Agreement RFQ Types. Treat it as configurable and check the RFQ type.

**Document flow.** The Document Flow tab shows the documents created from the master with status, for example the individual RFQs and the carrier responses. A freight agreement created at the end appears as a successor document in the document flow (H08; S4TM3).

## Structure of the RFQ master: header data (organizational unit, validity period, carriers, RFQ type, RFQ negotiation round number, response deadline, calculation sheet template, Carrier KPI Profile, Incumbent indicator) and items with tabs for Calculation Sheet Overview, Carriers, Trade Lanes, Capacities, Commodity Codes, Default Route, Document Flow, Output Management, Excel Integration, Versions and Award Summary; only a purchasing organization, company or corporate can be assigned as organizational unit
**Header (General Data).** H08 lists the organizational unit responsible, validity period, carrier details (a carrier table, with the status of the individual RFQs where available), RFQ type, RFQ negotiation round number, response deadline, and the calculation sheet template used to create a calculation sheet or local calculation sheet in the master. S4TM3 adds that the Valid-From and Valid-To dates relate to the validity of the resulting freight agreement, the response deadline is the date until which invited carriers can respond, the Carrier KPI Profile controls which KPIs show on the carrier fact sheet, and the master can be valid for several purchasing organizations and multiple carriers, with the Incumbent indicator maintained for current carriers.

**Organizational unit rule.** Only a purchasing organization, company or corporate can be assigned. A purchasing group or purchasing office cannot (H08). For strategy spend calculation, when a company or corporate is entered, the system sorts the purchasing organizations under it and picks the first one (H08).

**Items.** On the Items area you reach the comparison cockpit and can accept the preferred strategy before awarding. The item types available come from the freight agreement type assigned to the RFQ type in Customizing. The tabs (H08):

| Tab | Content |
|---|---|
| Calculation Sheet Overview | Calculation sheet details per item, including local ones |
| Carriers | The carriers that responded to the RFQ item |
| Trade Lanes | Trade lane details per item |
| Capacities | Capacity required from carriers, capacity carriers can commit to, capacity awarded |
| Commodity Codes | Commodity codes per item |
| Default Route | Route between a location pair |
| Notes, Attachments | Notes and files per item |
| Document Flow | Documents created from the master, with status |
| Output Management | Print, e-mail, fax and a record of what was sent |
| Excel Integration | Download master details to a spreadsheet |
| Versions | RFQ versions and negotiation rounds with status |
| Award Summary | Graphs of the logistical information |

On the master, the Capacities tab or area can be activated in the Customizing activity Define Freight Agreement RFQ Types (H08). S4TM3 adds that requested capacity is entered in various dimensions (TEU is typical for ocean), that periodicity and capacity driver/dimension are set as spend specifications (if scales in the rate table are marked as capacity drivers, capacity is specified per combination of those scale items), and that the trade lane on the Trade Lanes tab uses the same logic as in freight agreements.

H08 also notes that carriers can be given a periodicity on the Capacities tab; the item must then have just one trade lane, and the period comes from the transportation allocation type assigned through the freight agreement type and RFQ type.

## Carriers are maintained on the RFQ master header; they can be deleted per item but a carrier cannot be added on a single item; carriers of an existing freight agreement are flagged Incumbent
All carriers taking part in SFP must first be maintained at header level. Each item copies the carriers from the header. If an item should not go to a certain carrier, delete that carrier at item level. A carrier cannot be added on a separate item (S4TM3).

Consequence for individual RFQs: an individual RFQ holds only the information designed for that carrier. If a carrier is removed from an item, that item does not appear in that carrier's individual RFQ (S4TM3).

If a master is created from an existing freight agreement, the carriers on that agreement are flagged Incumbent. S4TM3 says it is preferable to use incumbent carriers in the later optimizer evaluation, and the strategy conditions have a separate incumbent setting (see the target share item below).

## Rating structure of an RFQ item: calculation sheets define which charges are calculated and how, rate tables define rates directly in TM; the Request Rate checkbox marks the rate records downloaded in an individual RFQ spreadsheet; carriers submit rates and promised capacity but cannot change the structure of calculation sheets or rate tables
The rating structure of an RFQ item can consist of calculation sheets and rate tables (both also in a local form inside the RFQ). Calculation sheets specify which charges are calculated and how. Rate tables define and maintain the rates directly in TM (H08).

- **Request Rate checkbox:** in the rate table of the calculation sheet you can select Request Rate on rate records. These are the records downloaded when you download an individual RFQ as a spreadsheet, and the carrier responds with rates only for them (H08).
- **What the carrier fills in:** carriers submit rates and promised capacity for each charge type in the calculation sheet of each RFQ item. If a charge type has a rate table, the carrier gives rate values for each combination in the rate table. The carrier cannot change the structure of calculation sheets or rate tables (H08).

The detailed structure of calculation sheets and rate tables is the subject of session 09.

## Target rate or target amount: the maximum price the shipper is willing to pay, with a tolerance percentage (example 1000 USD with 10% means rates above 1100 USD need not be considered); it is shown to carriers only if Publish Target Rate is selected in the freight agreement RFQ type
In the calculation sheet or the rate table of a calculation sheet you can define a target rate or target amount: the maximum price you are willing to pay for a carrier's service, plus a tolerance in percent. You can then decide on a carrier whose rate exceeds the target after tolerance. Example (H08): target 1000 USD, tolerance 10%; if a carrier proposes more than 1100 USD, you do not have to consider that carrier when awarding.

Target rates are entered for every charge line item in the Agreement RFQ Calculation Sheet Items section and in the rate table of the item (S4TM3). They are visible to carriers only when Publish Target Rate is selected in Customizing, Define Freight Agreement RFQ Types, and the individual freight agreement RFQ is published (H08; S4TM3). S4TM3's reason: the shipper only wants responses within an acceptable range.

## Publication: publishing the master automatically creates and sends individual freight agreement RFQs; creation and publication can be separated into two steps (otherwise the Create & Publish indicator does one step), individual RFQs cannot be sent selectively, an approval workflow can be enabled, and mass processing uses /SCMTMS/RFQ_PUBLISH; a master that cannot be published stays in Publication in Process, is checked in SLG1 and republished with /SCMTMS/RFQ_RE_PUBLISH
- **What happens:** on publication the system creates and sends individual freight agreement RFQs to carriers, using output management settings and business-to-business communication (H08).
- **One step or two:** the Create & Publish indicator in the RFQ type configuration creates and publishes in one step (S4TM3). Separating creation and publication (set in Define Freight Agreement RFQ Types) lets you edit or review the individual RFQs before sending. You cannot send individual RFQs selectively: publishing the master sends all of them (H08).
- **Approval:** an approval workflow can require an approver before publication. When approved, the system publishes the master automatically and creates and sends the individual RFQs. If creation and publication are separated, you then trigger each step separately. An offline approval workflow can send work items by e-mail (H08).
- **Mass processing:** program Mass Publication of Freight Agreement RFQ Masters (/SCMTMS/RFQ_PUBLISH) in SE38 creates, or creates and publishes, individual RFQs for several masters. With the two-step setting it does not publish automatically, but can publish masters that already have individual RFQs (H08).
- **Failure:** if the system cannot publish, the status becomes Publication in Process, not Published. Check in SLG1, correct the errors, and republish with Publish Freight Agreement RFQ Master (/SCMTMS/RFQ_RE_PUBLISH) in SE38 (H08).

## System notifications to carriers: after publication, as the response deadline approaches, on the deadline, on cancellation, after creation of the agreement, and when the agreement is expiring, using business-to-business communication
H08 (Requesting of Quotations for Transportation Services) lists six notifications, integrated with output management and sent by business-to-business communication:

1. After publication: the RFQ is attached, plus XLS files for rate tables and local rate tables.
2. When the response deadline is approaching: a reminder to carriers who have not responded (timing set in Define Freight Agreement RFQ Types).
3. On the response deadline: a reminder on the last day to carriers still not responded.
4. When the RFQ is canceled: carriers are told it is withdrawn.
5. After creation of the agreement: carriers get the freight agreement and rate tables as attachments.
6. When the agreement is expiring: carriers get the agreement as an attachment and a link.

## Negotiation rounds versus versions: a new negotiation round (Follow Up, Create Negotiation Round) requires a published master, adds 1 to the round number and resets the version number to zero; a new version (Generate New Version) needs status In Process, adds 1 to the version number and keeps the round number
**Negotiation round (H08).** Use it when the responses are not satisfactory. You change the master and publish again, and carriers resubmit rates. The round number records how often you published the master to carriers. The master must be published before you can create a round. Creating a round adds 1 to the round number and resets the version number to zero, so the latest published round always has a clean version. Menu path: Follow Up, Create Negotiation Round (also in S4TM3).

**Version (H08).** A version lets you make changes without publishing to carriers. The master must have status In Process; once individual RFQs exist or the master is published, you cannot create a new version. Creating a version adds 1 to the version number and keeps the round number. Use the Generate New Version button. When you publish, the round number goes up by 1.

H08 sums it up: use versions for internal changes before you publish, and negotiation rounds for changes you send to carriers. The Versions tab lists versions and rounds with status. S4TM3 notes that the version currently displayed or edited is not shown in the version overview.

| | New negotiation round | New version |
|---|---|---|
| Precondition | Master published | Status In Process, nothing published or created yet |
| Round number | +1 | unchanged |
| Version number | reset to 0 | +1 |
| Goes to carriers | Yes, on publication | No |

## Response evaluation in the comparison cockpit: manual comparison by carrier and charge type (flat amounts only, ranking by lowest quoted rate, manually entered target share) or optimizer-based comparison for complex cases with constraints
The comparison cockpit is where responses are compared per RFQ item or across items. This post-bid analysis supports the decision which carriers get the business and in what proportion (H08). Prerequisites (H08): the master is published, carriers have responded, target share strategies are defined, and a calculation profile and a charges profile (with local currency) are defined and assigned to the organizational unit in transaction PPOME. The system simulates an estimate of cost; it does not calculate actual charges.

**Manual response comparison.**

- Suitable when the comparison is simple and rates are the only constraint (H08). S4TM3 adds: the only objective is rate minimization and the number of responding carriers is small.
- Works directly in TM only for charge types with flat amounts. The system ranks carriers by the lowest quoted rate per charge type and shows a response comparison graph (H08).
- If the charge type has a rate table or local rate table, you can compare the tables in a spreadsheet instead, with no graph (H08).
- You enter the target share per carrier manually. With no optimizer involved, spend is estimated from the carrier-level target share, not the rate-table target share (H08).
- In the Response Comparison area you can Select all items or Select matching items for a given item type (S4TM3).

**Optimizer-based comparison.**

- Especially useful when the comparison is complex and several constraints apply (H08). S4TM3 lists the constraints: minimum or maximum number of carriers, carrier-specific and incumbent-specific minimum or maximum target shares, risk-related constraints, and Bonus/Malus linked to historical carrier performance.
- The optimizer proposes target shares across carriers bearing these constraints in mind, and you can run it repeatedly with different strategies and versions (H08; S4TM3).
- Before inserting a target share strategy, select in the Response Comparison area the charge types you want to compare with the optimizer (H08).

**Other points (H08).** Historical spend simulation lets you specify a prime charge type and validity periods in the optimizer conditions. The system finds previous orders with the same attributes (report /SCMTMS/SOL_SPEND_SIMULATE in SE38), calculates their charges with the carriers' proposed rates and uses the total to determine target share. The optimizer therefore works on charges rather than rates. Currency conversion is applied when several currencies are compared. Graphs include the response comparison graph and the strategy spend comparison graph; the default type is a 100% stacked column graph.

## Target share strategies and strategy conditions (Define Target Share Strategies): minimum and maximum target share, minimum and maximum number of carriers, separate conditions for incumbent carriers, respect for carrier-promised capacity; the optimizer can be run in the back end with /SCMTMS/OPTIMIZER_RUN, can use historical spend simulation, and can add risk or bonus-malus logic via BAdI
**Where defined.** Customizing, Transportation Management, Master Data, Agreement RFQs and Quotations, Define Target Share Strategies (S4TM3; H08). A strategy contains conditions that restrict the optimizer.

**Condition parameters (S4TM3).** Incumbent (selected if the carrier is incumbent), maximum business share, minimum business share, maximum number of carriers and minimum number of carriers. H08 words it as minimum and maximum target share percentage and minimum and maximum number of carriers to include, with separate conditions for incumbent carriers and all other carriers. H08's reason: you may want to give an incumbent a higher percentage. The optimizer also respects the capacity promised by carriers, so a proposed share stays within the carrier's confirmed capacity (H08).

**In the cockpit.** The same strategy can be used several times as different strategy versions. Choose Insert to add a strategy and Insert, Conditions for conditions. Run Optimizer calculates target shares per carrier. Simulate Estimate Spend calculates spend per carrier and strategy (S4TM3). The Copy button creates a new strategy from an existing one, with or without the target shares; copying without target shares keeps only the strategy conditions (H08). The RFQ type can define whether the optimizer processes one item or all items (S4TM3).

**Back end.** Program Mass Optimizer Run and Strategy Spend Estimation (/SCMTMS/OPTIMIZER_RUN) in SE38 runs the optimizer for specific strategies or for all strategies in a master, and can estimate spend at the same time. For several masters at once, only "all strategies" is possible (H08).

**Bonus-Malus and BAdIs.** A flag in the target share strategy Customizing enables Bonus-Malus, which uses carrier performance scores from SAP BW to push the optimizer toward or away from a carrier. The BAdI method GET_BONUS_MALUS_VALUE defines the reward or penalty; the course example adds 10% to a carrier's proposed cost for a history of delays (S4TM3). H08 lists further BAdIs: Additional Optimizer Constraints (for example risks or bonuses), Specification of Historical Parameters for Optimizer, and a customer-specific strategy spend estimation.

## Strategy spend estimation and Award Summary: the system estimates cost, it does not calculate actual charges; the strategy spend comparison graph compares strategy versions; the Award Summary tab shows graphs by trade lane, carrier or RFQ item and last year's spend
**Estimation (H08).** The system estimates strategy spend for the full validity period of each RFQ item and adjusts if the periodicity differs (for example validity 12 months and periodicity monthly: the estimate is multiplied by 12). It respects minimum and maximum rate values from rate tables. Constraints named in H08 include: spend can be estimated for a single rate table only; charge types with different rate tables cannot be compared at the same time; a local rate table can have only one validity period; rate tables must not contain the calculation bases SOURCELOC_ZONE or DESTLOC_ZONE; a flat-amount line item must not have a calculation resolution base; only one capacity dimension (gross weight, gross volume or container count) can be used when running the optimizer. If you change a carrier's target share after the optimizer run, estimation uses the carrier-level share.

The strategy spend comparison graph compares amounts and shares across strategy versions (H08; S4TM3).

**Award Summary (H08).** Available on the published master once carriers have responded. It helps judge how negotiation is going, for example whether to create a new round. Views:

- **Trade Lane:** equipment type, transportation mode, estimated strategy spend, budget for the periodicity, number of carriers and target share distribution. Comparing estimated spend with the planned periodicity budget can indicate a need for a new negotiation round.
- **Carrier:** target share per carrier and who was awarded, plus transportation mode, equipment type, shipping type, strategy spend version and amount.
- **RFQ Item:** periodicity budget versus estimated spend per item and spend per carrier.
- **Historic spend:** in Trade Lane and RFQ Item views, Display Historic Spend queries SAP NetWeaver Business Warehouse for what was spent on the same trade lane, transportation mode and shipping type, converted to the master's currency if needed.

## Awarding and agreement creation: selecting and accepting the preferred target share strategy calculates the confirmed capacity (changeable manually) and sets the RFQ status to Awarded; Create/Update Agreement generates or updates freight agreements per carrier, with agreement allocations; the optimizer's target share is copied into the business share used in carrier selection in planning
1. **Accept the preferred strategy.** Choose Accept Preferred Strategy. The system calculates the confirmed capacity in the master from the optimizer's target share (you can change it manually) (H08), and the RFQ status becomes Awarded (S4TM3).
2. **Create/Update Agreement.** In the master, choose Create/Update Agreement. For each carrier you can create a new agreement or update an existing one, and you can turn each RFQ item into a separate agreement. Agreement allocations are created per carrier, based on the requested capacities of the request item and the target business share defined for the carrier (S4TM3). An approval workflow can be required before agreements are created (H08).
3. **Notification.** The system notifies carriers about the creation or update, with a copy of the agreement and rate tables (H08).
4. **Completion.** Setting the master to completed sets the individual RFQs to completed (H08).

**From target share to planning (H08).** When you create or update an agreement from an RFQ, the system proposes a target share, which is the output of the optimizer run in the comparison cockpit. It is copied into the item details of the agreement. The target share is included in the business share, and the business share is used in the carrier selection settings in planning.

## Award confirmation (optional, enabled in the RFQ type): an award confirmation deadline, the Notify the Carrier for Award Confirmation button, consolidation of carrier confirmations, and statuses; it is only a soft confirmation, carriers are not rejected if they miss the deadline
Award confirmation lets the shipper ask carriers to confirm the allocated capacities before capacity or business share is awarded through a freight agreement. It is enabled in Define Freight Agreement RFQ Types (H08).

- **Deadline:** defined in the master. Carriers confirm within it. This is only a soft confirmation: the system does not reject carriers that miss the deadline, and the shipper can still confirm capacities offline (H08).
- **Notification:** the button Notify the Carrier for Award Confirmation tells carriers their confirmed capacities and the deadline.
- **Consolidation:** a carrier can answer by e-mail with a spreadsheet (items, rate tables, calculation sheets, transportation modes, service levels) containing a response and a confirmation reason. A carrier not using TM can use the Manage Freight Agreement RFQs app. The master's award confirmation status updates automatically when an individual RFQ confirmation is available. After the deadline you can run /SCMTMS/RESPONSE_AWARD_CONFIRM, which retrieves masters with status Pending Confirmation from Carrier (or a specific RFQ ID).
- **Statuses:** shown on the master, the RFQ item, the response and the optimizer strategy.

*The material read does not explain the individual award confirmation status values in detail; only the places where they are shown were read.*

## RFQ master assignments distribute single RFQ items to analysts or organizations whose results are merged back once approved; publication to carriers is possible only from the master
Responsibilities for different segments of an RFQ may sit with different purchasing organizations or departments that need to work on comparisons at the same time (S4TM3). After the master is approved and published, the shipper picks an item in the Items area and chooses Create/Update RFQ Assignment. A separate freight agreement RFQ master assignment is created with one transportation requirement item (based on trade lanes) and a copy of previous responses. H08 describes the analysts as having expertise in a trade lane, who determine the best bids and merge results back to the master.

When work is finished, the user transfers the item back with a follow-up action on the assignment item, and this works only if the item is already approved in the assignment document (S4TM3). Assignment documents have the same capabilities as master documents, but publication to the carrier is only possible from the master (S4TM3).

## Reverse auction: carriers can revise bids and see the current best rates; by default only lower bids are possible unless Allow Carriers to Increase their Bids is selected
Reverse auction belongs to the Advanced RFQs feature (H08). Prerequisites in Customizing (Master Data, Agreement RFQs and Quotations): Advanced RFQs, Enable Capacity Demand and Rates, Enable Reverse Auction, and optionally Allow Carriers to Increase their Bids (only if Enable Reverse Auction is selected).

The shipper can let carriers revise bids and see the current best rates on the user interface and in spreadsheets. Carriers see the current best rates for a lane and can revise their bids. By default they can submit only lower bids, and higher bids need Allow Carriers to Increase their Bids. They can bid multiple times until the response deadline, or until the negotiation is completed or canceled, and can upload their latest bids by spreadsheet (H08).

## Carrier collaboration prerequisites: for each carrier, a business partner with the role Carrier and a collaboration user defined in the Maintain Collaboration Users app; carriers need not use TM
A shipper can collaborate with carriers for various TM processes even if the carrier does not use TM. Once carriers have access to the relevant features they can, for example, answer freight agreement RFQs with proposed rates (H10).

For each carrier (H10):

1. In the Maintain Business Partner (BP) transaction, create a business partner with the role Carrier.
2. In the Maintain Collaboration Users app, define a collaboration user and specify that it is for that business partner with the role Carrier (app F4911).

For the relevant business document types, an attachment schema configured to use the Attachment Service must also be assigned (H10). The shipper must also have configured SFP prerequisites, and maintained carrier text types so carriers can add notes (H10).

## Carrier response to freight agreement RFQs: in the Manage Freight Agreement RFQs app the carrier monitors RFQs by status, responds with rates or rejects participation, can download and upload a spreadsheet; the shipper then accepts or rejects rates, requests confirmation and creates or updates the freight agreement
**Carrier side (H10, app Manage Freight Agreement RFQs).** Monitor RFQs by status (for example open for response, waiting for carrier confirmation), view a worklist sorted by response deadline or a filterable list, respond with rates or reject participation, use a spreadsheet for rate details, and use attachments and notes. The uploaded spreadsheet is also attached to the RFQ.

**Process (H10):**

1. The shipper creates the master (Create Freight Agreement RFQ Master app).
2. The shipper publishes it; the system creates and sends individual RFQs.
3. The system notifies each carrier.
4. The carrier evaluates and responds, or rejects participation; optionally downloads the spreadsheet, enters rates and uploads it.
5. The shipper monitors and reviews responses.
6. The shipper accepts or rejects the rates.
7. The shipper requests confirmation of the rates.
8. Once confirmed, the shipper creates or updates the freight agreement for the carrier.

If the shipper does not want carriers to use the app, RFQ details can be exchanged by spreadsheet instead (H10; H08 describes the spreadsheet format).

*Difference between sources:* S4TM3 describes carrier access through the SAP LBN (Logistics Business Network) with an individual user, where the Excel sheet is shown in the portal, downloaded, filled and uploaded. H10 describes the Manage Freight Agreement RFQs app with a collaboration user. The corpus does not say how the two relate, so check which channel applies in a given landscape.

## Carrier apps for order management: Manage Freight RFQs (accept, accept with proposed changes if the shipper allows it, or reject; accepting creates a freight quotation that can be revised within the deadline), Display Freight Quotations (pending, rejected, awarded), Confirm Freight Orders (Confirm with Changes, driver and vehicle details) and Manage Execution of Freight Orders (report planned and unplanned events and actual quantities; no events for a blocked freight order)
These apps cover freight tendering, freight order confirmation and freight order execution in the subcontracting process (H10). Each requires the carrier collaboration prerequisites to be configured by the shipper.

| App | What the carrier does |
|---|---|
| Manage Freight RFQs | Sees open, closed and responded RFQs and the number due on the tile. Can accept without changes, accept with proposed changes to price, currency or start and end dates, or reject with a reason. Accepting with changes is available only if the shipper configured tendering settings to allow it. Accepting creates a freight quotation, which can be revised multiple times within the response deadline. |
| Display Freight Quotations | Lists quotations as pending (being evaluated), rejected or awarded, with details such as stops and cargo. |
| Confirm Freight Orders | Lists orders needing confirmation, confirmed or closed (canceled or completed). Updates driver and vehicle registration details. Can propose changes to confirmed start and end date and time, price limit or currency with Confirm with Changes. |
| Manage Execution of Freight Orders | Lists orders in execution, closed or blocked. Reports a planned event (for example Arrival or Loading Begin) or an unplanned event with a reason (for example Delay), at order, stop or tour-event level. Reports actual quantities of each item in a stop. Cannot report events for a blocked freight order. |

Order confirmation lets the carrier plan its workload independently of the tendering process (H10). H10 also lists settlement apps for carriers (Manage Charges for Freight Orders F7104, Manage Freight Orders for Invoicing F7732, Manage Freight Invoices F7106, Display Credit Memos F7502). These are outside this session's items and belong to the settlement session.

## Practice
Draw a one-page process map of strategic freight procurement from RFQ master to freight agreement. For each step show the shipper action, the carrier action, the document or status involved, and the app or report used. Use the four SFP steps as the frame and include publication, response, comparison, preferred strategy, Awarded status, and Create/Update Agreement.

## Self-check
Can I explain how a shipper moves from a freight agreement RFQ master to a freight agreement, and what the carrier does at each step, to a procurement manager without notes?
