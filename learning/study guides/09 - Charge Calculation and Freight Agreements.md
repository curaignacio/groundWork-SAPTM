# Session 09 — Charge Calculation and Freight Agreements

## Overview
This session explains how TM turns a freight order into a calculated charge. The chain of master data is: scale base, scale, rate table, charge type, calculation sheet, and freight agreement. Around it sit the settings that decide which agreement and calculation sheet apply (profiles, preconditions, determination rules) and the calculation logic itself (resolution base, rate derivation, through rates, calculation methods). A consultant needs this chain because every cost shown on a freight order, and later settled with the carrier, traces back to it. The session closes with the hands-on example from exercise E05, which is the reference path for tracing one charge line.

## Scope of charge calculation in the course: master data for charge calculation, charge calculation and freight settlement processes on the buying side only; charge calculation for forwarding orders (selling side) is not covered
The course (S4TM3) covers three things: master data for charge calculation, charge calculation, and freight settlement processes. The focus is on the buying side only. Charge calculation and settlement related to forwarding orders (the selling side) are not covered, and scenarios related to LSPs are not detailed (S4TM3).

Where this session mentions forwarding agreements or sales-side profiles, it does so only to place the freight agreement in context.

## Charge calculation determines the freight charge for a transportation scenario from conditions in the business rules framework, charge calculation master data and configuration items; the result goes back to the requesting document together with charge type, charge category or subcategory so accounting can determine organizational unit, cost or revenue receivers and general ledger account
The transportation charge calculation process determines the freight charge for a given transportation scenario (S4TM3). S4TM3 gives example scenarios: a shipper asks a carrier to quote a move from a distribution center to a customer, an LSP receives a booking for a container between ports, a shipper moves product from plant to distribution center, or a shipper requests value-added services such as container cleaning and customs handling.

The charge is determined from conditions in the business rules framework, charge calculation master data and configuration items. The calculated charge goes back to the requesting document. Together with it the engine provides the charge type, charge category or subcategory, so that the receiving accounting processes can determine the organizational unit, the cost or revenue receivers and the general ledger account (S4TM3).

## Charge requests can come from the freight order, freight booking, service order, dispute, freight agreement RFQ, forwarding quotation, forwarding order, forwarding settlement document and freight settlement document
S4TM3 lists the TM documents that can issue a charge request:

- freight order
- freight booking
- service order
- dispute
- freight agreement RFQ
- forwarding quotation
- forwarding order
- forwarding settlement document
- freight settlement document

The freight agreement RFQ appears here because strategic freight procurement estimates spend with the same charge calculation machinery (see session 08, and H08 on the integration of RFQ masters with calculation sheets and rate tables).

## Charge Management master data: scale template, scale (a dimension of a rate table), rate table (rates by validity period), charge types (for example Haul, BAF, FSC), calculation sheet (hierarchical table combining permitted charge types and their sequence) and freight agreement
S4TM3 describes the master data the system uses to calculate charges:

| Object | What it is |
|---|---|
| Scale template | Helps create scales easily |
| Scale | A dimension of a rate table |
| Rate table | A price list; a rate is valid only for the period defined by its validity; freight rates are maintained here by the scale specifications |
| Charge type | Describes a specific charge, for example Haul (Haulage), BAF (Bunker Adjustment Factor) or FSC (Fuel Surcharge) |
| Calculation sheet | A hierarchical table that combines the charge types permitted for a document and the sequence in which they are considered |
| Freight agreement | The contractual relationship between the service provider (or customer) and the requesting organizational unit; holds payment terms, limits, validity period and valid calculation sheets, plus organizational unit, contracting parties and conditions |

S48600 gives the same picture from the process side: freight agreements reference calculation sheets, and the calculation engine computes the charges and stores the result in the freight order (see session 01).

The practical reading order for a charge line is therefore: agreement, then calculation sheet, then charge type line, then rate table, then scales. Scale bases and calculation bases sit underneath and define how scales and logistical data are interpreted.

## Business example Road-Sea-Road: a sales order builds a freight unit, the planner creates stages (precarriage by truck Denver to Newark, main carriage by vessel Newark to Rotterdam, on-carriage by truck Rotterdam to Cologne); freight orders for the truck stages and a freight booking for the main carriage each get their own calculated amount used to pay the carrier
S4TM3 uses a full container load sent by road and sea. A sales order is created in SD for the entire move, and on save the system builds a freight unit. The planner decides the routing and creates stages, each planned separately:

| Stage | Move |
|---|---|
| Precarriage | Truck from shipper origin (Denver) to port (Newark) |
| Main carriage | Vessel from port of loading (Newark) to port of destination (Rotterdam) |
| On-carriage | Truck from Rotterdam to the customer unloading location (Cologne) |

Two freight orders are created, one for precarriage and one for on-carriage. The amount calculated for these stages is used to pay the trucking carrier. A freight booking is created for the main carriage, and the amount calculated for it is used to pay the ocean carrier (S4TM3). The course then shows how the system calculates the Newark to Rotterdam booking charge from the master data.

*Difference inside S4TM3:* the stage table says precarriage runs Denver to Newark, while the sentence after it says the precarriage freight order runs "Chicago to Newark". The corpus does not resolve this.

## Scale base: defines how the system interprets a scale and is defined in Customizing under Define Scale Bases; its fields include Field Assignment, UoM Relevant, Dimension (link to T006), Rounding Rule, Numeric, Crcy Scale base, Raw values and Date Scale Base; example WEIGHT with dimension Mass; a rate that depends on distance and weight needs a separate scale for each, and scales can be reused in several rate tables
The scale base defines how the system interprets the scale. It is defined in Customizing for Transportation Management, Basic Functions, Charge Calculation, Data Source Binding, Define Scale Bases (S4TM3).

A scale defines a parameter that then defines a rate. If a rate depends on distance and weight, you define a separate scale for each. A scale can be reused in several rate tables. In the course figure the rate table has three dimensions (destination zone, origin location, weight in lbs), so three scales are defined (S4TM3).

Fields (S4TM3):

- **Field Assignment:** the internal field from /SCMTMS/S_TCSCALE_ITEM_DB that stores the scale values for scales created with this scale base.
- **UoM Relevant:** checks whether the scale base is relevant for unit of measure.
- **Dimension:** link to the T006 dimension.
- **Rounding Rule:** whether a rounding rule applies to the scale.
- **Numeric:** whether the input scale value is numeric.
- **Crcy Scale base:** the scale base is for currencies (example: amount).
- **Raw values:** the scale base is for raw values (examples: business partner, location).
- **Date Scale Base:** the scale base is for dates.

Example: scale base WEIGHT (description SCAVAL_WT), usage Base for Scales, UoM Relevant X, Dimension Mass, Rounding Rule X, Numeric X (S4TM3).

For unique requirements, a customer-specific scale base is added by extending the scale item structure (include /SCMTMS/INCL_EEW_TC_SCALE_ITEM), adding the scale base in Customizing, and enhancing the scale UI (S4TM3).

## Scale types and scale creation: Base scale (from a value upward, >=), To Scale (up to a value, <=) and Same Scale (exactly one value, =); a scale also has a scale unit of measure, a rounding profile and a calculation type (absolute for non-numeric scales such as region, transportation zone or business partner, relative for numeric scales such as weight, distance, length); scales are created in the Create Scale app or during rate table maintenance
Scale maintenance is a prerequisite for rate maintenance, because scales are the dimensions of rate tables. Scale items can be configured by quantities, volumes, weights, distances or points. You can create scales as separate master data, which lets you reuse them in several rate tables, or during rate table maintenance (S4TM3). In the launchpad: Charge Management, Create Scale (S4TM3).

Data entered when creating a scale (S4TM3):

| Field | Meaning |
|---|---|
| Scale Base | The parameter that defines the rate, considered a dimension of the rate table (for example Length, Partner, Weight) |
| Scale Type | Base scale: from a certain value (>=). To Scale: up to a certain value (<=). Same scale: exactly one value (=) |
| Scale Unit of Measure | Unit for the scale levels, for example KG, LB, Day, Mile, KM |
| Rounding Profile | Before the rate lookup, the system rounds the input value by this profile to find the right scale level |
| Calculation Type | Absolute: for non-numeric scales such as Region, Transportation Zone, Business Partner. Relative: for numeric scales such as weight, distance, length |

A relative calculation type can be specified for numeric scale bases only (S4TM3). In E05, the scale S4LG1_WEIGHT is a numeric scale for which you specify the scale type (From Scale or To Scale), unit of measure and rounding profile, while S4LG1_COUNTRY is linked to a scale base for countries and its items list the countries (E05).

## Scale templates: optional help to create scales and predefine scale items; Customizing templates are transportable but cannot have items for Same Scales, master data templates can and need no Customizing authorization but cannot be transported
A scale template creates a scale automatically, and its use is optional. Its advantages are predefined scale items, less manual work and fewer typos. It is an efficient way to create scales during rate table maintenance (S4TM3). A template holds a scale template name, the scale type and the scale base, and optionally scale template items.

| | Customizing template | Master data template |
|---|---|---|
| Where | Customizing: Transportation Management, Basic Functions, Charge Calculation, Basic Settings, Templates, Define Scale Templates | SAP Fiori Launchpad |
| Transportable between systems | Yes | No |
| Items for Same Scales | Not possible (they depend on master data) | Possible |
| Authorization | Needs Customizing access | Users without Customizing authorization can create and use them |

In the Charge Management Worklist, master data and Customizing templates appear in their own queries (S4TM3).

## Calculation base: the actual base or factor on which a charge is calculated, defined for a scale base in Define Calculation Bases (for example W1 for gross weight and W2 for net weight under scale base Weight, or DESTLOC for the destination location); its fields include Field Assignment, Currency Field, Unit Field, Helper Assignment, Use BAdI, Party Role, Calculation Type, Calculation Usage and TrM Category
A calculation base identifies the actual base or factor with which the system calculates charges for the scale (S4TM3). Gross weight and net weight both correspond to the scale base Weight (dimension mass) but are different charge aspects, so they get different calculation bases, for example W1 for gross weight and W2 for net weight. You define a calculation base for every scale base, and it is the final element in charge determination (S4TM3).

Location example (S4TM3): the scale has the scale base Location, which says the scale uses locations only and can serve for source and destination. The calculation base DESTLOC says the destination location of the freight order is used. If the resolution base in the calculation sheet points to the freight order stage, the system takes the value from that stage.

Customizing path: Transportation Management, Basic Functions, Charge Calculation, Data Source Binding, Define Calculation Bases. Fields (S4TM3):

- **Scale Base:** the scale base used.
- **Field Assignment:** the internal field assignment of the logistical data.
- **Currency Field:** for currency-based calculation bases.
- **Unit Field:** for quantity-based bases such as weight, volume, pieces.
- **Helper Assignment:** the program logic that links to the data source.
- **Use BAdI:** select if customer-specific logic is needed.
- **Party Role:** when business partners are involved, for example consignee, sold-to or bill-to.
- **Calculation Type:** a default (absolute or relative); for same-scale bases it is absolute, quantity fields from/to are relative.
- **Calculation Usage:** manual charges, rate tables, or both (blank means no restriction).
- **TrM Category:** restricts the calculation bases in a rate table to those with the same transportation mode category as the charge type, and those with none.

**Custom calculation bases.** Extend the communication structure (include /SCMTMS/INCL_EEW_TCC_CB), add the calculation base in Customizing with the new field as field assignment, and set the scale base. If extra logic is needed, use method GET_CALC_BASE_VALUES of BAdI /SCMTMS/TCC_BO_DATA_ACCESS and set the BAdI flag, or use a helper class (interface /SCMTMS/IF_TCC_CALC_BASE). The source states: when creating a custom calculation base, it is always necessary to define a scale base for it (S4TM3). Often a new resolution base is also needed: add its name to table /SCMTMS/C_RES_BS (only the name is maintained) and implement logic in the BAdI.

## Resolution base: determined by the origin of the data a charge aspect is based on, with Root (document header), Stage, Container and Product as examples; for instance the gross weight of the order uses the root, and per-package freight uses the package
During charge calculation the system determines the calculation resolution base by the origin of the data a charge aspect is based on (S4TM3). Examples:

- **Root:** the header of the document, such as freight order, booking order or forwarding order.
- **Stage:** use stage attributes, for example the distance between shipper location and port of loading.
- **Container:** needed when an attribute stored at container level (for example equipment type 22GP or 42G0) is required, otherwise that information is not available for calculation.
- **Product:** when product attributes such as quantity, weight or volume must be used.

To determine freight by the gross weight of the order, use the root. To calculate per package, use package (S4TM3). The resolution base is set on the Basic Data tab of a calculation sheet item, where logistical data can be booking, container, main item, package, root or document stage, optionally with a grouping rule (S4TM3).

In E05, the Handling Charge has the resolution base PRODUCT, which means the charge line is applied multiple times in the freight order, once for each product transported (E05).

How the four bases differ: the scale base says how a scale is interpreted, the scale is one dimension of a rate table, the calculation base says which value is used in the lookup, and the resolution base says from which part of the document that value is taken.

## Charge types: classify a charge line (for example base rate, surcharge, discount); settings include positive or negative value, absolute or percentage, charge category and subcategory, tax indicator, rounding, default calculation base, leading charge type, inactive flag and transportation mode category; categories and subcategories map to SD pricing condition types for billing and MM service activities for carrier invoice processing
A charge type classifies a charge line, for example base rate, surcharge or discount, and it matters for how the system calculates that line (S4TM3). Define charge types in Customizing: Transportation Management, Basic Functions, Charge Calculation, Basic Settings, Define Charge Types.

Settings (S4TM3):

- Positive or negative result.
- Absolute or percentage value, or decide each time the charge type is assigned.
- Charge category and charge subcategory.
- Tax indicator.
- If and how the system rounds the value.
- A default calculation base, so you need not assign one for each calculation sheet line.
- Leading charge type: it must have a value for the system to calculate the charges.
- Inactive: the type cannot be used for new calculation sheets or rate tables.
- Transportation mode category, which restricts the charge types in a calculation sheet to those with the same category as the agreement, and those with none.
- Descriptions in several languages, and extra values for air freight or forwarding charges.

**Categories and subcategories.** Charge types can be grouped into categories and subcategories (freely definable). S4TM3 names the UN/EDIFACT codelist 5237 as a useful code list for categories, and UN/EDIFACT Recommendation 23 (Freight Cost Code) for subcategories. They are defined under Basic Settings, Define Charge Categories and Define Charge Subcategories.

**Mapping into S/4HANA.** Charge types, categories and subcategories are mapped to pricing condition types in SD used for customer billing, and to service activities in MM used for carrier invoice processing (S4TM3).

## Rate tables: a price list grouped by validity period (business object /SCMTMS/TC_RATES), up to 14 dimensions though not recommended, with rate table determination rules to reduce dimensions; created manually, from rate table templates, or maintained in Microsoft Excel; Create Rate Table Definition defines the structure and Maintain Rate Table maintains rates; minimum and maximum values, calculation rules, the No Value Allowed flag for generic rates, and an optional approval workflow
**Concept.** A rate table is a grouping of prices, like a price list, with rates listed by validity period. It is a separate business object (/SCMTMS/TC_RATES) usable in several calculation sheets. You can maintain up to 14 dimensions but S4TM3 does not recommend modelling that way. A rate table determination rule can be used to decide which rate table applies to the current charge item and so reduce dimensions. Create manually, from a rate table template with predefined scales and validity dates, or maintain a large table in Microsoft Excel (S4TM3).

**Templates.** A Customizing template (Define Rate Table Templates) needs the template name, charge type or multiple charge types, charge usage and currency; template scales need dimension number, scale template and calculation base code; an optional calculation rule needs calculation base, unit of measure and quantity. Master data templates carry similar data and can also hold scale items and values for non-numeric scales (S4TM3).

**Two apps.** Create Rate Table Definition (Charge Management) defines the structure; Maintain Rate Table maintains rate information, and scale definition is not available there. This lets different users define structure and maintain rates (S4TM3).

**Structure (S4TM3).**

- General Data: the rate table identifier (unique), the charge usage (billable to your customer, or billed to you by your carrier, matching the agreement and calculation sheet) and the charge type. A rate table is assigned to a charge item only if the charge type matches.
- Scales tab: one dimension per scale, with the calculation base for each scale. Minimum and maximum value checkboxes make the system charge the minimum if the calculated value is below it and the maximum if above. A checkbox, Rel. Calc. Method (Relevant for Calculation Method), marks the table for special methods such as break-weight or clipping.
- Dates and Values tab: Valid From and Valid To and a rounding profile.
- Calculation Rules tab: the values the single rate is multiplied by. With several rules, the rate is multiplied by each. If a relative scale is involved, Relative Scale Items Only must be selected on at least one rule.
- Rate values: maintain single values, or the recommended Excel flow (create empty table, download to xlsx, maintain, upload).

**No Value Allowed.** Lets you upload rates that are generic across several dimensions, for example carrier-agnostic rates where no carrier-specific rate exists. The flag has priority from the last dimension scale to the first, and is available only for same-scale (S4TM3).

**Approval workflow.** Can be activated per rate table type. The rate administrator requests approval instead of releasing; the validity interval status becomes "Awaiting Approval", a SAP Business Workflow task notifies a manager, and once approved the interval is released. The organizational model must be maintained (S4TM3).

**Updating rates.** The Update Rates function (also the program /SCMTMS/RATE_MASS_UPDATE, and the Master Data Cockpit under Charge Management Worklist) can raise or lower rates by a percentage or amount, limited to a scale range already present in an existing validity period, and by calculation type (absolute, relative or both) (S4TM3). For validity periods you can change one, several or all, or create a new validity period inside or outside existing ones; by default the new period copies rate, calculation rule and scale item settings from the latest period, and it can be released automatically (S4TM3).

## Calculation sheet: charge usage in the general data; hierarchy items with instruction types Sum, Subtotal, Standard and Compare High/Low Value; each item has Rate, Basic Data (manual charge item, resolution base, rounding and adjustment profiles, dimensional weight profile, calculation method), Classification (mandatory, tax, statistical charge) and Preconditions tabs; a percentage item must refer to another item or subtotal
The calculation sheet is a hierarchical table that combines the charge types permitted for a document and the order in which they are considered. It serves both to bill customers and to pay carriers, and it lets documents show charges, subtotals and totals (S4TM3). Launchpad: Charge Management, Create/Edit Calculation Sheet.

**Data.** General data holds charge usage (valid for customer and/or service provider). Hierarchy items give the instruction, charge type and calculation instructions. Preconditions and general terms are set when the sheet is assigned to the freight agreement (S4TM3).

**Instruction types (S4TM3).**

- **Sum:** total of all lines below. Every sheet has an initial mandatory sum line that cannot be deleted; only its rounding rule can be maintained.
- **Subtotal:** amount of all lines between a reference-from and a reference-to line.
- **Standard:** a direct charge when it refers to a charge type.
- **Compare High/Low Value:** evaluates which of two or more lines counts, by highest or lowest value, with the Operation attribute. With High, the most expensive item stays and cheaper ones are deactivated.

A charge type can give a positive (surcharge) or negative (discount) value. If an item is a percentage, it must refer to another item or subtotal that produces an absolute value (S4TM3).

**Item tabs (S4TM3).**

- **Rate:** Amount (if filled, the item is not derived, it always equals this amount); currency or %; reference-from and reference-to lines for minimum or maximum substitution; Rate Table Determination Rule; fixed Rate Table; Calculation Rule; Index Table (for example for fuel surcharge).
- **Basic Data:** Charge Type; Manual Charge Item (no calculation, manual entry expected); External Calculation Flag (external engine such as SMC3); logistical data specification (stage category, shipping type, dangerous goods); Resolution Base; Rounding Profile; Adjustment Profile (for example so only chargeable weight is used); Dimensional Weight Profile (for example factor 166 or 194, or metric); Calculation Method Type and Method.
- **Classification:** Mandatory (a warning if it cannot be calculated; an error at invoice creation before transfer to MM if a mandatory item cannot be calculated), Tax, Statistical Charge (informational only).
- **Preconditions and Notes:** a precondition rule checks whether items are processed according to the logistical data source.

E05 shows this on calculation sheet S4TM1_CALCSHET_CAR10 (see the E05 item below).

## Agreements: forwarding agreements (FWA) for charges billable to the customer, freight agreements (FA) for charges billed by the carrier, internal agreements (IA) between organizations of a company, and service agreements as a type of freight agreement; contractual data covers organizational unit, parties, payment terms and validity; the agreement type Customizing sets allowed item types, default calculation sheet template, multiple parties and allocation type
Agreements are the basis for calculating transportation charges and can involve one or more parties (S4TM3).

| Agreement | Use |
|---|---|
| Forwarding agreement (FWA) | Charges billable to your customer |
| Freight agreement (FA) | Charges billable to you by your carrier |
| Internal agreement (IA) | Charges between organizations of the same company code and of different company codes in the same company |
| Service agreement | A type of freight agreement containing only service types or service products |

The sales organization appears on sales-side documents (forwarding documents, OTRs, DTRs, forwarding settlement documents); the purchasing organization appears on freight orders, freight bookings, service orders and freight settlement documents (S4TM3).

**Contractual data (S4TM3):** organizational unit, involved parties (for example ordering party or carrier), terms of payment, validity dates. The agreement type Customizing sets, among others: allowed item types, preconditions on the agreement (for example transportation mode or service level), a text schema for notes, the default calculation sheet template, multiple parties allowed (one freight agreement with a carrier valid for several purchasing organizations), calendars, the allocation type for transportation allocations, and enabling the Change Document tab.

E05's freight agreement FRAGR_S4TM1_CAR10 shows on the General Data tab the agreement version, parties (purchasing organization and carrier), validity period, agreement priority and document currency, with items below that can have a deviating validity, each with a calculation sheet (E05).

## Agreement determination: by organization, business partner, validity period and preconditions; with several matches a leading charge type or the agreement priority decides; preconditions on agreement items are built-in (trade lanes, partners, item precondition) or BRFplus/BAdI; calculation profile determination types Minimum Charges, Maximum Charges and Determine All Agreements enable manual selection; condition types TCM_FAGDET and TCM_FAGDEX determine or exclude agreements
**Standard determination.** The system determines the agreement from organization, business partner, validity period and preconditions. Most commonly this is purchasing organization plus carrier for freight agreements and sales organization plus customer for forwarding agreements. A BRF+ condition can be used for complex rules (S4TM3).

**Several matches.** A leading charge type (set in charge type Customizing) can be used: the first agreement where it can be calculated is picked. Agreement priority (General Data tab, details section) defines the sequence in which the subsequent determination runs (S4TM3; S48600 states the same). S4TM3 explains why several agreements exist: an LSP can strike deals with the same carrier at country, regional and global level, and a better rate can sit in a country-level contract.

**Preconditions on agreement items (S4TM3).** Either built-in or BRFplus/BAdI. A BRFplus condition or BAdI returns true or false, and if true the calculation sheet is considered. Built-in preconditions: Trade Lanes (source or destination location or zone, mode or means of transport; the item can be activated or deactivated), Partners (item activated or deactivated by business partner), and Item Precondition (up to seven predefined conditions).

**Manual selection (S4TM3).** An enhancement to the automated standard. It allows choosing an agreement or agreement item, plus automatic selection of the minimum or maximum item through the calculation profile (Define Calculation Profiles, agreement determination type):

- **Minimum Charges:** the system finds the final amounts of all agreement items and chooses the item with the minimum final amount.
- **Maximum Charges:** the same, choosing the maximum.
- **Determine All Agreements:** the system shows all relevant agreements and items for each charge item and you select.
- Blank: standard determination.

The Multiple Agreements pop-up is not supported for through rates.

*Difference inside S4TM3:* an earlier page calls the selection type that lets you pick manually "Display All Agreements", while the example scenarios page calls it "Determine All Agreements". The Customizing value names should be checked in the system.

**Charge calculation rules (S4TM3).** Condition types TCM_FAGDET (freight agreement determination, standalone) and TCM_FAGDEX (freight agreement exclusion). With TCM_FAGDET the standard logic (organization, validity, partner) is ignored and the condition is used; the Std Determ. checkbox falls back to standard determination if the condition fails or returns nothing. Maintained via Maintain Charge Calculation Conditions. TCM_FAGDEX checks the automatically determined agreements one by one for applicability (condition and BAdI option); if more than one remains, the agreement priority is used. It can be embedded in the calculation profile or kept in the agreement under General Data, Details. The same rule mechanism also supports calculation sheet determination, preconditions for sheets and items, grouping rules for resolution bases, rate table determination rules and charge-by-formula rules (BRFplus or BAdI returns the amount directly) (S4TM3).

## Calculation profile and charges profile: the calculation profile sets the date type for rate and validity, the calculation level (header, item or stage), determination rules, through rates, dimensional weight profile and data source (actual or ordered route); a charges profile assigned to a purchasing organization groups it with the settlement and cost distribution profiles; a profile on a business partner role takes precedence over one on the organizational unit; the freight order type must enable charge calculation
**Calculation profile** (Customizing: Basic Functions, Charge Calculation, Basic Settings, Define Calculation Profiles). It is the central place for the settings used in charge calculation (S4TM3):

- the date type used as basis for rate, exchange rate, agreement validity and charge calculation (for example order date, invoice date, expected end date of main carriage);
- the calculation level: header, item or stage;
- the determination rule for agreement and calculation sheet;
- through rates across several stages;
- the default dimensional weight profile and its determination condition;
- the data source for calculation and invoicing: actual route, ordered route, or actual and ordered route;
- the agreement determination type (see above).

**Charges profile.** Enables charge calculation for a purchasing organization. It groups the calculation profile, the freight settlement profile, the cost distribution profile and the local currency of the business documents. It is created in Define Charges Profiles, where the calculation profile is assigned and then flows to the organizational unit the charges profile is assigned to (S4TM3).

*Difference between sources on the assignment transaction:* S4TM3 names transaction PPOCE for assigning the charges profile to the purchasing organization, while S48600 and H08 name PPOME. The material does not say which is right for a given release.

**Assignment rules (S4TM3).**

- A purchasing calculation profile is needed on the buying side (freight order and freight booking). A forwarding house needs both sales and purchasing profiles, and one profile can serve both.
- Calculation profiles can also go on the business partner roles sold-to party, ship-to party, carrier and vendor (Define Business Partner, Vendor/Transportation Purch. Org. Data tab, or BP).
- If a profile is assigned to both the organizational unit and a business partner role, only the one on the business partner role applies. You can assign a profile to the organizational unit alone, but not to a business partner alone.

**Freight order type settings (S4TM3, Define Freight Order Types).** Enable Charge Calculation must be selected for the system to calculate (manual charges can still be entered, and the quoted price of awarded freight quotations can be updated). Calculate Charge After Each Save runs the calculation on every save, and if a mandatory charge type cannot be determined, the order cannot be saved. The same settings exist for freight booking and service order types. S48600 adds that charge calculation must be enabled in the corresponding freight document type Customizing to activate it.

## Calculation process: collect data from the transaction object, configuration, BRF+ conditions, master data and BAdIs, determine the freight agreement, then the calculation sheet, calculate each charge type, keep a log and show results in the freight order; rate derivation determines calculation base and rate table, reads logistical data, determines the date baseline, finds the matching rate table record and calculation rule, and calculates the amount; the transportation zone rate is found by going up the zone hierarchy
**Freight order charge calculation (S4TM3; S48600).**

1. Collect data from TM core objects: the transaction business object (freight order, freight booking, service order, stage, item, container), configuration objects, BRF+ conditions, master data and any BAdI implementation.
2. Determine the freight agreement.
3. Determine the calculation sheet within the agreement (listed as its own step in S48600; S4TM3's list moves straight to calculating the values).
4. Calculate the value of each charge type in the calculation sheet.
5. Keep the log file of the calculation run.
6. Show the results in the freight order.

**Freight rate derivation (S4TM3).**

1. From the calculation sheet line item, determine the calculation base and the rate table.
2. From the dimensions (scales) of the rate table, obtain the logistical data.
3. From the calculation profile, determine the baseline for date determination.
4. Obtain the matching rate table record and then the appropriate calculation rule.
5. Calculate the freight rate amount.

**Zones.** Rates need not be maintained for every value; they can sit at the appropriate level. The system goes up the zone hierarchy until it finds a rate (S4TM3). A location can belong to several transportation zones (example in S4TM3: Hamburg in a Germany zone and a Hamburg zone). The engine compares the zones one by one and returns the first rate it finds, with no priority among rates.

**Estimation.** In the Fiori Launchpad you can do carrier selection and charge estimation with minimal data: origin, destination and purchasing organization are named as required (S4TM3).

## Special calculation features: through rates across several stages (carrier-dependent, enabled in the calculation profile), header-level charges alongside stage-level calculation, and calculation methods such as break-weight (cheaper next rate) and clipping (level-by-level totals, one scale item relative)
**Through rates (S4TM3).** A through rate covers several stages, or the whole route, and is applied if available, depending on Customizing. With several stages and different carriers, the calculation is carrier-dependent, and through rates can be maintained across stage categories without overlap. Example: a Door-Port rate (A to B and B to C) negotiated with Carrier 1 including haulage, while the on-carriage C to D belongs to Carrier 2; the system finds a through rate for A to C for Carrier 1 and a rate for C to D for Carrier 2. The functionality must be enabled in the calculation profile. Compared with stage-by-stage calculation, one rate then covers several stages instead of one rate per stage.

**Header and stage level (S4TM3).** Some charges cannot be assigned to a stage and apply to a business partner, for example unloading fees. A "mixed" calculation level lets the system calculate header-level charges for an agreement item independently while the rest is calculated by stage. It needs a calculation profile with the calculation level set to stage. Example: in an FOB incoterm scenario the consignee bears security charges across main and on-carriage, defined as header-level charges in a separate calculation sheet.

**Calculation methods (S4TM3).** Specified per charge type in the calculation sheet (Basic Data tab, calculation method type), defined in Customizing under Basic Functions, Charge Calculation, Enhancements to Charge Calculation Engine, Define Calculation Methods. Examples named: break-weight, clipping, fuel surcharge, deficit weight rating, most expensive main carriage, internal charge calculation and external systems.

- **Break-weight:** the system compares the next rate with the current rate and applies the cheaper one.
- **Clipping:** the system works through all scale levels one by one and adds up the results. One scale item must have a relative calculation type. Worked example: levels up to 5 t at USD 50 absolute, up to 7 t at USD 14 per ton, up to 10 t at USD 13 per ton, up to 15 t at USD 12 per ton. A 12-ton load costs 50 + 28 + 39 + 24 = USD 141 with clipping, and USD 144 (12 t at USD 12) without it.

## Hands-on example in E05: freight agreement FRAGR_S4TM1_CAR10 with calculation sheet S4TM1_CALCSHET_CAR10; rate table BASE_RATE_00 with scales S4LG1_COUNTRY (countries) and S4LG1_WEIGHT (up to 100, 200, 500, 1.000, 5.000 and 999.999.999 kg); Update Rates with simulation mode and Excel download and upload; Calculate Charges in the freight order shows the agreement, calculation sheet, rate table, rate amount and calculation rules
The exercise (E05) walks through the chain from the contract down to one charge line:

1. **Agreement.** The Freight Agreements Worklist app lists agreements with parties, validity and release status. Open FRAGR_S4TM1_CAR10: General Data shows version, purchasing organization and carrier, validity, priority and currency. The single item points to a calculation sheet.
2. **Calculation sheet.** In the Charge Management Worklist, query All Calculation Sheets, open S4TM1_CALCSHET_CAR10. Items include the Basic Freight Charge and the Handling Charge. The Basic Data tab shows manual or calculated, and rounding and adjustment profiles. The Rate tab holds a rate amount, a rate table or a rate table determination rule. The Classification tab shows category, subcategory, mandatory, statistical and tax. The Handling Charge has the resolution base PRODUCT.
3. **Rate table.** In Edit Rate Table Definition, BASE_RATE_00 has two dimensions: destination country and gross weight. The Dates and Values tab holds validity periods (initially one, 01.07.2021 to 31.12.9999) and the rate table. The Calculation Rules tab specifies how the rates are applied (the exercise notes rates charged per distance for a distance of 100 km).
4. **Scales.** In Edit Scale: S4LG1_COUNTRY is linked to a scale base for countries, with the countries as items. S4LG1_WEIGHT is numeric, with scale type, unit and rounding profile, and items up to 100, 200, 500, 1.000, 5.000 and 999.999.999 kg.
5. **Update Rates.** Raise rates by 10% in a new validity period for calendar year 2025 (01.01.2025 to 31.12.2025). First run with simulation mode selected and check that all messages are green, then repeat with simulation off. Result: the initial validity period is divided into three: 01.07.2021 to 31.12.2024 (old rates), 01.01.2025 to 31.12.2025 (new rates) and from 01.01.2026 (old rates). For destination country AT the first two rates go from 120 EUR and 60 EUR to 132 EUR and 66 EUR.
6. **Excel.** On the Excel Integration tab, download the rate table for all validity periods (the workbook is protected, so change values but not the structure, with one sheet per validity period). Change a cell to 135, add rates for FR (country codes are checked with a value list), save, upload, save, and check the Dates and Values tab: AT minimum is now 135 EUR and the FR rates are added.
7. **Calculate Charges.** In freight order 200000109, choose Calculate Charges, expand all, and select a charge with Show/Hide Details. The Overview tab shows the agreement, calculation sheet, rate table, rate amount and calculated amount; the Calculation Rules tab shows the basis, for example the Basic Freight Charge based on a net weight of 5.180 KG with the rate determined per 10 KG, and the second Handling Charge based on 2 pieces at a rate per 1 PC. A 50 EUR waiting time surcharge is then added manually. In the worklist, selected freight orders move from Not Calculated to Calculated with a net amount in document currency.

## Practice
Draw a diagram of the charge calculation master data chain (scale base, scale, rate table, charge type, calculation sheet, freight agreement). Annotate it with the E05 example objects (FRAGR_S4TM1_CAR10, S4TM1_CALCSHET_CAR10, BASE_RATE_00, S4LG1_COUNTRY, S4LG1_WEIGHT) and list the steps the system takes to calculate one charge line in a freight order.

## Self-check
Can I explain how TM turns a freight order into a calculated charge, from agreement determination to the rate table lookup, to a logistics manager without notes?
