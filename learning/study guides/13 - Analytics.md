# Session 13 — Analytics

## Overview
This session covers TM analytics, the fifth stage of the TM process: Analytics and Collaboration. TM delivers Fiori apps called overview pages (OVPs). Each one shows the KPIs for one area, such as cost, allocation, business share, execution, quantity or tendering. Each page has cards, detailed views behind the cards, and CDS views and OData services underneath. In practice you meet this in two ways. A transportation manager asks "which page shows me X", and a consultant has to find out why a page is empty. The second needs the technical chain: CDS view, OData service in the Gateway system, authorizations and input parameters. Almost all content is from the Analytics chapter of the SAP Help (H13).

## TM analytics overview pages (OVP): apps on the Fiori launchpad that show KPIs for operational business; each page covers one area of TM (for example freight booking, freight ordering, tendering, business share); made of cards that are read-only, show data in real time, can be resized and reordered (H13, Analytics Overview Pages; S48600, Analytics and Collaboration)
TM analytics provide apps, called overview pages, that show the KPIs you need to manage your operational business, "at a glance" for daily decisions. Each page shows information from a different area of TM (H13). You open them from the Fiori launchpad.

S48600 places this in the fifth process stage, Analytics and Collaboration. Overview pages, reports and KPI dashboards have been created for shippers and logistics service providers. They give a consolidated view of day-to-day activity and help real-time decision-making. They can be tailored to business roles.

**Cards (H13):**

- Each page is made of cards, similar to tiles, based on one or more KPIs.
- Cards are read-only: you cannot enter information or run queries or searches on them.
- They present data as lists, tables or charts. Some show summary information you can drill down from, for example to individual transactions.
- They show data in real time, which helps you spot delays and bottlenecks and act quickly.
- You can resize them and change their order.

Each page is based on one or more Core Data Services (CDS) views (see the CDS views section below).

## Detailed views: reached by selecting a card header (unfiltered) or a chart data point (filtered); they combine donut, bar and line charts with a table, are read-only, and let you navigate to the document (for example freight order or freight booking) to change it; some overview pages have two detailed views (H13, Analytics Overview Pages; Detailed Views)
**How you get there (H13):**

- For cards with graphical charts, selecting the **header** takes you to a detailed view with all the unfiltered data.
- Selecting a **data point** in a chart takes you to a detailed view filtered to the information relevant to that data point.
- Selecting a card header or information line also leads to the detailed view for non-chart cards.

**What it contains.** A combination of donut, bar and line charts, and a table that lists the relevant TM documents. The page layout described for each detailed view has these areas:

- **Information filter** at the top. By default the graphics view is shown, and you can switch to a field view (compact filter) with fields such as units, currency or tolerances.
- **Chart** in the middle. It can be changed to a table or a combination, and a View By filter gives more specific cuts, for example by means of transport, carrier or block reason.
- **Table** at the bottom. You add or remove columns in Settings. Selecting a row, or a button such as Change Transportation Allocation or Change Tendering, opens the document in Transportation Management in edit mode.

**Read-only, but actionable.** Detailed views are read-only as well, with no entry and no queries or searches. You act by navigating from the table straight to the document, such as a freight order or freight booking, and changing it there (H13). That answers how a manager acts on what a card shows.

**One or two detailed views.** Some pages have two, each for specific cards. In the Cost Analysis page, the Invoicing Block Analysis card opens the Transportation Invoice Blocked Detailed View, and any other card opens the Transportation Costs Detailed View. Freight Order Execution Monitoring also has two (see its section below). Each detailed view has its own Fiori ID.

**Time basis.** Detailed views show a two-month rolling basis, the current and previous month (H13).

## CDS views: query views (SQL queries on the database) that feed each overview page; top-level consumption views containing other contributing CDS views, made of key figures and attributes; appropriate authorization objects are needed; the OData service of each Fiori ID must be activated in the Gateway system (H13, CDS Views; S4TM3, Determination of Procurement Needs)
H13: "A CDS view is a query view, that is, an SQL query on the database requesting certain data to be returned." One or more CDS views feed each OVP. They are top-level views, called **consumption views**, containing other contributing CDS views, and they consist of **key figures and attributes**. You need the appropriate authorization objects to access them.

S4TM3 gives the same picture and adds the activation requirement. You must activate the respective OData service for each Fiori ID of the analytics area in the Gateway system. SAP Help lists all analytics areas and technical IDs under the search topic "Analytics".

**What must be in place technically for a page to work (from the sources):**

1. The CDS view (delivered, named in each page's Technical Basis section).
2. The OData service for that Fiori ID activated in the Gateway system. For example, the Allocation Analysis page requires C_TRANSPALLOCCOMPLIANCEQ_CDS. A page with two data sources needs two services.
3. Authorization objects for the CDS view. The help lists them per view. For Allocation Analysis these include T_ADMIN (activity H1) or T_TAL (activity 03), plus B_BUP_PCPT for business partners and /SCMB/LOCB for locations. The execution and quantity views list objects such as T_TOR_PUR, T_TOR_EXE and TM_* objects.
4. The mandatory unit and currency input parameters (see the parameters section below).

*What the material does not establish:* the full authorization set for every view. I read the Allocation Analysis one only, so check the Prerequisites sections of the other views in H13.

## Mapping of overview pages to CDS views: Allocation Analysis and Business Share Analysis to C_TranspAllocComplianceQ and C_BusinessShareComplianceQ, Cost Analysis to C_FreightSettlementCostQ and C_TranspOrdInvcgBlockStsQ, Freight Booking and Freight Order monitoring and quantity pages to their Execution, Execution Status and Quantity queries, Tendering Analysis to C_TenderingQuery (H13, Summary table)
The H13 summary table, completed with the Fiori IDs from each page's Technical Basis section:

| Overview page | Fiori ID | Detailed views (Fiori ID) | CDS views |
|---|---|---|---|
| Allocation Analysis | F2673 | Transportation Allocation (F2745) | C_TranspAllocComplianceQ |
| Business Share Analysis | F2674 | Business Share (F2746) | C_BusinessShareComplianceQ |
| Cost Analysis | F2672 | Transportation Costs (F2754); Transportation Invoice Blocked (F2755) | C_FreightSettlementCostQ; C_TranspOrdInvcgBlockStsQ |
| Freight Booking Execution Monitoring | F2677 | Freight Booking Execution (F2747); Freight Booking Execution Status (F2748) | C_FrtBkgExecutionQuery (Event Query); C_FrtBkgExecutionStsQ (Status Query) |
| Freight Booking Quantity Analysis | F2678 | Freight Booking Quantity (F2749) | C_FrtBkgQuantityQuery |
| Freight Order Execution Monitoring | F2675 | Freight Order Execution (F2750); Freight Order Execution Status (F2751) | C_FrtOrdExecutionQuery (Event Query); C_FrtOrdExecutionStsQ (Status Query) |
| Freight Order Quantity Analysis | F2676 | Freight Order Quantity (F2752) | C_FrtOrdQuantityQuery |
| Tendering Analysis | F2679 | Tendering (F2753) | C_TenderingQuery |

Note that two pages are fed by two CDS views, called data sources 1 and 2, each producing different cards: Cost Analysis, and the Freight Booking and Freight Order Execution Monitoring pages. In each case a card resolves to a detailed view, the detailed view to its CDS view, and the CDS view to an OData service with the same name plus _CDS, for example C_TENDERINGQUERY_CDS.

In the Freight Order Execution Monitoring page, the blocking and non-blocking discrepancies, carrier, location and activity on time performance, and unexpected events cards open the Freight Order Execution Detailed View. The life cycle status analysis, execution and planning block analysis, and delayed-in-transit cards open the Freight Order Execution Status Detailed View (H13).

## Delivered time filters: all CDS views behind the OVPs and analytical list pages contain the current and previous month on a two-month rolling basis; they can be changed with metadata extensions (SAP Note 2779334) (H13, Metadata Extensions to Replace Delivered Time Filters)
SAP provides time filters with all the CDS views behind the OVPs and analytical list pages (ALPs) in TM. In all cases they contain the current and previous month, on a two-month rolling basis. You can change them with metadata extensions, per SAP Note 2779334 (H13). So every page and detailed view you read covers this window unless a customer has changed it, which matters when a user asks why last quarter's data is missing.

## Allocation Analysis (Fiori ID F2673; detailed view F2745): KPIs for weight, volume and amounts of the transportation allocation including net, gross, minimum and maximum values and total and average utilization; cards such as Trade Lane Weight, Volume and Container Load Analysis, Transportation Mode Category Analysis, Overall Weight and Container Utilization Distribution; Change Transportation Allocation opens the allocation in edit mode (H13, Allocation Analysis; Transportation Allocation Detailed View)
**Audience.** A transportation manager for a shipper who works with carriers (H13).

**KPIs.** Weight, volume and amounts of the transportation allocation, including net, gross, minimum and maximum values, plus total and average utilization for all units of measure. Data covers the current and previous month.

**Cards:**

- Trade Lane Weight Load Analysis: total current, minimum and maximum weights by orientation (for example along) for each carrier. It may help identify the most effective trade lane for goods of a given size and orientation.
- Trade Lane Volume Load Analysis: the same for aggregated volumes.
- Trade Lane Container Load Analysis: the same for container counts.
- Transportation Mode Category Analysis: weight, volume and quantities transported per mode category, for example air or sea.
- Overall Weight Utilization Distribution: the total weight per carrier per month, and any increase above the average minimum threshold or decrease from the average maximum threshold.
- Overall Container Utilization Distribution: the same for container counts.

**Detailed view (F2745).** It shows a donut chart of total gross weight for the current and previous month, a line chart of gross weight by mode category, and bar charts of gross volume per means of transport and number of containers by orientation. The table lists allocation, orientation, source and destination location, gross weight and volume. Selecting an allocation and choosing **Change Transportation Allocation** opens it in edit mode in TM. The field view accepts weight, volume and quantity unit, minimum and maximum tolerance (percentage), mode, means of transport and orientation.

**Use case in the help.** Find the destinations that took the highest gross weight by road last month and the number of containers used. One location has low weight but many containers, so you open the allocation and look at the carrier and details.

**Technical.** CDS view C_TranspAllocComplianceQ, OData service C_TRANSPALLOCCOMPLIANCEQ_CDS. The view is built on the Transportation Allocation business object.

## Business Share Analysis (F2674): current amount and target quantity per carrier, ratio and business share per month; Weight Fulfillment Ratio, Volume Fulfillment Ratio, Trade Lane Fulfillment, Road, Sea and Air Fulfillment Distribution compare actual booked carrier quantity with target quantity (H13, Business Share Analysis)
**KPIs.** The current amount and target quantity of each carrier's transports, the current value to target quantity ratio, and business share quantities per month, for the current and previous month (H13).

**Cards:**

- **Weight Fulfillment Ratio**: how much of their allocated share carriers achieved, also as a percentage. The help's example is 328,750 kg out of an allocation of 493,125 kg (66.67%).
- **Volume Fulfillment Ratio**: the same for volume, for example 5000 m3 out of 10000 m3 (50%).
- **Trade Lane Fulfillment**: how each trade lane performs against its allocated share for all units of measure, for example 987,500 kg out of 987,500 kg (100%).
- **Road Fulfillment Distribution (Weight), Sea Fulfillment Distribution, Air Fulfillment Distribution**: actual booked carrier quantity against the target quantity, shown as a graph.

**Detailed view (F2746).** The help example: you planned 70% of shipments to one carrier and 30% to another, but the first carrier took 90% and the second none. You already incurred penalties past the 70% threshold. You research why, and change the business share information in favor of the second carrier.

**Technical.** CDS view C_BusinessShareComplianceQ, OData service C_BUSINESSSHARECOMPLIANCEQ_CDS, built on the Business Share business object. The weight and volume unit parameters are mandatory.

## Cost Analysis (F2672): two data sources, C_FreightSettlementCostQ for cost cards (Cost Distribution, Carrier Cost Analysis, Charge Type Analysis, Purchasing Organization Cost Analysis and others) and C_TranspOrdInvcgBlockStsQ for Invoicing Block Analysis; the Invoicing Block Analysis card opens the Transportation Invoice Blocked Detailed View, any other card the Transportation Costs Detailed View (H13, Cost Analysis)
**Audience.** A transportation manager or person responsible for costs, who tracks costs and issues with freight orders or freight bookings blocked for invoicing (H13). KPIs cover cost amounts by invoicing week, mode category (with weights and volumes), carrier, charge type, purchasing organization, source and destination country or region, and the number of transportation orders blocked for invoicing, with reasons.

**Data source 1, C_FreightSettlementCostQ:**

- **Cost Distribution**: invoiced, credit and cost amounts for each invoicing week.
- **Cost and Quantity Analysis**: total cost per transportation mode category, with gross weight and volume. It is a bubble chart.
- **Logistic Network Analysis**: total cost per source and destination country or region, highest first.
- **Carrier Cost Analysis**: carriers with the highest costs first.
- **Charge Type Analysis**: charge types with the highest costs first, for example basic freight charges or pick up charges.
- **Purchasing Organization Cost Analysis**: purchasing organizations with the highest costs first.

**Data source 2, C_TranspOrdInvcgBlockStsQ:** the **Invoicing Block Analysis** card shows how many freight orders or freight bookings are blocked for invoicing, per blocking reason, such as time conflict, compliance or incomplete for planning.

**Where the cards lead.** Invoicing Block Analysis opens the Transportation Invoice Blocked Detailed View (F2755). Any other card opens the Transportation Costs Detailed View (F2754).

**Help examples.**

- *Blocked for invoicing.* Three sea freight orders are blocked with block category time conflict and block reason penalty charges. You open the orders, find that the carrier arrived late for its customs slot twice, and contact the carrier about the penalty dispute.
- *Costs.* High air freight cost in one invoicing week. You navigate to the freight settlement document and the air freight booking.

**Technical.** OData services C_FREIGHTSETTLEMENTCOSTQ_CDS and C_TRANSPORDINVCGBLOCKSTSQ_CDS. This page uses the most parameters: P_DisplayTimeUnit, P_DisplayWeightUnit, P_DisplayVolumeUnit, P_DisplayQuantityUnit, P_DisplayLengthUnit and P_DisplayCurrency, all mandatory.

## Freight Order Execution Monitoring (F2675) and Freight Booking Execution Monitoring: Life Cycle Status Analysis, Execution Block and Planning Block Analysis, Delayed Freight Orders in Transit, Blocking and Non-Blocking Discrepancies, Carrier, Location and Activity On Time Performance, Unexpected Events; a freight order is on time if all its events are classed as on time, and the on time cards use time-relevant events with expected and actual date and time and event status Reported (H13, Freight Order Execution Monitoring)
**Purpose.** KPIs on critical process statuses that lead to blocking situations, and a carrier's on time performance, which helps when allocating future business (H13). The Freight Booking page (F2677) is built the same way for freight bookings.

**Data source 1, C_FrtOrdExecutionStsQ (status):**

- **Life Cycle Status Analysis**: execution-relevant freight orders by life cycle status. Execution-relevant means execution status In Execution (03), with a departure event but no arrival event at the final destination. For freight bookings, the counts per status Draft (00), New (01) or In Process (02) are shown in descending order.
- **Execution Block Analysis** and **Planning Block Analysis**: freight orders with a block, grouped by reason, in descending order. The reasons are specified in the TM Freight Order transaction. If you have not done so, the system creates them from the blocking category.
- **Delayed Freight Orders in Transit**: freight orders whose latest time-relevant event is delayed. Both the expected and actual date and time fields must exist and the event status must be Reported. The delay is the difference between the actual and expected date.

**Data source 2, C_FrtOrdExecutionQuery (events):**

- **Blocking Discrepancies** and **Non-Blocking Discrepancies**: discrepant events that did or did not lead to a block, by event code and discrepancy type.
- **Carrier On Time Performance**: the percentage of freight orders each carrier delivered on time, also as numbers, for example 6 / 14. A freight order is on time if all its events are classed as on time. Otherwise it is classed as delayed.
- **Location On Time Performance**: the percentage of on time events per location, lowest first, for example 6 / 8.
- **Activity On Time Performance**: the percentage of on time events per event code, such as loading or unloading, lowest first, for example 12 / 27.
- **Unexpected Events**: events such as accident or delay, grouped by event code, highest count first.

**Definition of on time.** The calculation for all on time cards uses all time-relevant events that have both expected and actual date and time and the event status Reported (H13).

*Source wording to note:* in the freight order section, the help text says freight bookings in the Life Cycle Status Analysis description and in the "Freight bookings delayed in transit" card reference. That looks like carry-over from the booking page. The card is named Delayed Freight Orders in Transit in the key features list.

## Freight Order Quantity Analysis (F2676) and Freight Booking Quantity Analysis: gross weight, gross volume and quantity distribution by week for completed freight orders, carrier, shipper and ship-to party quantity analysis, Utilization Distribution, Distance Analysis (H13, Freight Order Quantity Analysis)
**KPIs.** Current weight, volume and numbers being transported weekly by each carrier, shipper and ship-to party, by transportation mode, and by source and destination country or region. Each carrier's utilization performance is also shown (H13). Cards cover **completed** freight orders, that is, life cycle status Completed.

**Cards:**

- Gross Weight, Gross Volume and Quantity Distribution: change by completion week over the current and previous month.
- Transportation Mode Category Analysis: gross weight and gross volume as axes, with the number of freight orders per mode category.
- Logistic Network Analysis: source and destination countries or regions with total gross weight, highest first.
- Carrier, Shipper and Ship-To Party Quantity Analysis: total gross weight, gross volume and container count per party.
- **Utilization Distribution**: the lowest average utilization per carrier as a percentage, lowest first.
- Quantity Analysis: gross volume and gross weight per mode category.
- **Distance Analysis**: total net duration and total distance per mode category.

**Technical.** F2676 uses C_FrtOrdQuantityQuery (OData service C_FRTORDQUANTITYQUERY_CDS). The detailed view is F2752. The booking equivalent is F2678, with C_FrtBkgQuantityQuery and detailed view F2749. I read the freight order page in full and the booking page only at the card-name level.

## Tendering Analysis (F2679): Open Requests, Overdue Requests, Acceptance Analysis, Tendering Peer-to-Peer Cycle Analysis, Tendering Cycle Time Analysis, Tendering Ratio, Original Carrier Changed (comparison of awarded business against the carrier the system proposed) (H13, Tendering Analysis)
**Audience.** A tendering manager or transportation manager. The page helps you identify the best carriers, assess them for peer-to-peer freight requests for quotation (RFQs) and across all tendering types, find the best tendering type per carrier, and investigate why a system-proposed carrier was manually replaced (H13).

**Cards:**

- **Open Requests**: your current worklist of freight RFQs sent out that have not yet reached their deadline. You drill down and open the request in TM.
- **Overdue Requests**: RFQs past their deadline. You can work with critical requests where there may still be time to answer.
- **Acceptance Analysis**: the proportion of RFQs an individual carrier responded to, and the number accepted out of the total, for example 2 / 4.
- **Tendering Peer-to-Peer Cycle Analysis**: the proportion of peer-to-peer requests a carrier answered with a quotation, and response times. It shows who responds immediately, who delays, and who delays and then submits a higher amount.
- **Tendering Cycle Time Analysis**: the average cycle time in hours and the number of cycles per carrier, across a mix of tendering types, for example peer-to-peer and broadcast.
- **Tendering Ratio**: the most successful tendering type per carrier, answering which type gets the most or the quickest responses.
- **Original Carrier Changed**: the percentage and number of times the carrier the system proposed was manually replaced by another carrier, with reasons. It compares the business you actually awarded against the business the system proposed.

**Detailed view (F2753).** A bar chart of cycle time by requested carrier. The view-by options include freight RFQ status, life cycle status and negative responses. The **Change Tendering** button opens the freight order in edit mode.

**Technical.** CDS view C_TenderingQuery, OData service C_TENDERINGQUERY_CDS.

## Main input parameters: P_Language, P_TodayDate (system date; data from the beginning of the previous month up to the system date), P_DisplayTimeUnit, P_DisplayWeightUnit, P_DisplayVolumeUnit, P_DisplayQuantityUnit, P_DisplayLengthUnit, P_DisplayCurrency; the unit and currency parameters are mandatory; Allocation Analysis adds P_TrAlcMinToleranceInPercent and P_TrAlcMaxToleranceInPercent (H13, Main Input Parameters of each view)
Each view's Structure section lists main input parameters (H13). The subset differs by view.

| Parameter | What it does |
|---|---|
| P_Language | Display language of texts. The system uses the system language automatically. |
| P_TodayDate | Timeframe of the data. The system uses the system date, usually your local date, and retrieves data from the beginning of the previous month up to the system date. |
| P_DisplayTimeUnit | Units of time, for example Event Delay in hours or minutes. |
| P_DisplayWeightUnit | Units of weight, for example Gross Weight in kilograms. |
| P_DisplayVolumeUnit | Units of volume, for example Item Volume in meters cubed. |
| P_DisplayQuantityUnit | Units of quantity, for example Number of Containers in pieces. |
| P_DisplayLengthUnit | Units of length, for example Package Length in meters. |
| P_DisplayCurrency | Currency, for example Invoice Amount in euros. |
| P_TrAlcMinToleranceInPercent, P_TrAlcMaxToleranceInPercent | Allocation Analysis only: another tolerance value for the minimum and maximum value. |

The unit and currency parameters are mandatory. In the views I read, the Allocation Analysis and Business Share Analysis views name the weight and volume unit parameters as the mandatory ones, and Cost Analysis names all six unit and currency parameters. The help does not list the same set in every view.

## Analytics in the wider TM processes: overview pages can be tailored to business roles and supervisors of execution can start at the freight order execution overview (S48600, Analytics and Collaboration); analytics can analyze historic transportation volumes to determine procurement needs, but their use is not mandatory for the strategic freight procurement process (S4TM3, Determination of Procurement Needs)
**In the process landscape (S48600).** Analytics and Collaboration is the fifth stage of TM. Pages can be tailored to business roles, and users who supervise transportation execution can begin their day at the freight order execution overview.

**In strategic freight procurement (S4TM3).** SAP analytic tools can analyze historic transportation volumes to determine procurement needs. That analysis is helpful when creating a forecast for the next period. S4TM3 also names the allocation and business share analysis as examples of the areas a page can cover. However, the analysis of historic data and the creation of a forecast "are not related to the freight agreement master RFQ" created from that information. So using the analysis tools is not mandatory for the SFP process.

S4TM3 adds, in a different lesson, that trade lanes do not influence optimizer planning, but they are important to analytics (and used in Trade and Commodity Management, and sometimes as restrictions for carrier selection in the case of allocations).

*What the material does not establish:* the other analytics, such as reports and KPI dashboards that S48600 mentions, beyond the overview pages and ALPs covered in H13. It also does not describe the collaboration half of the stage here.

## Practice
Build a one-page analytics map. List each TM overview page with its Fiori ID, the CDS views behind it, its detailed views, and one business question it answers. Start from the table in the mapping section and add the question per page, for example which carriers have the highest on time performance, or why freight orders are blocked for invoicing.

## Self-check
Can I explain which TM overview page and detailed view answers a given KPI question, and what feeds it technically, to a transportation manager without notes?
