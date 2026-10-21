# Session 12 — Dangerous Goods and Basic Functions

## Overview
This session covers how TM handles dangerous goods (DG): where the DG data comes from, how the checks are configured, and where in the process chain they run, from the forwarding order to the freight document. It also covers the ADR 1.1.3.6 points exemption, the user interface for document-based DG records, content loading, and the DG print documents. Nearly all of it comes from the "Considering Dangerous Goods" part of the Basic Functions help (H12). In a project, a DG scenario fails mostly because one Customizing prerequisite is missing, such as the DG profile on the document type, the block reason, or the FUB_DG and VSR_DG methods. Knowing the whole chain lets you find the gap.

## Purpose of the dangerous goods (DG) functions in TM: to transport dangerous goods in compliance with international regulations (H12, Considering Dangerous Goods). Dangerous goods are solids, liquids or gases that pose risks to people, living organisms, property or the environment, and the chemical safety laws governing them vary between countries (S48600, Dangerous Goods)
The DG functions in TM "enable you to transport dangerous goods (DG) in compliance with international regulations" (H12).

S48600 defines the subject. Dangerous goods, also called hazardous materials or hazmat, are solids, liquids or gases that pose risks to people, living organisms, property or the environment. They are subject to chemical safety laws that vary between countries. The list in S48600 includes radioactive, flammable, explosive, corrosive, oxidizing, asphyxiating, biohazardous, toxic, pathogenic and allergenic materials. Physical conditions such as compressed gases, liquids or hot materials are also included. The category covers goods that contain such materials or chemicals, or that show hazardous characteristics under specific circumstances.

S48600 also describes the idea behind the checks. DG experts classify products according to the applicable regulations. A compliance check then runs in all relevant business documents in the value chain, for example intracompany stock transfer orders, sales orders, outbound deliveries and freight orders. It verifies whether transporting the product is allowed. If it is not, the check blocks the business document.

H12 adds that when business documents are printed, the system also prints the required DG information, if the required settings have been made.

## Two DG processing options, Dangerous Goods Processing Based on PS&S and Dangerous Goods Processing Based on Product Compliance; they are mutually exclusive, so only one can be activated at a time (H12, Considering Dangerous Goods; S48600, Dangerous Goods)
H12 lists the two ways of working with DG in TM:

- **Dangerous Goods Processing Based on PS&S**
- **Dangerous Goods Processing Based on Product Compliance**

S48600 states it as a note: "One can choose between DG processing based on PS&S and DG processing based on product compliance. Since these two solutions are mutually exclusive, only one can be activated at a time."

What each option rests on, according to the sources:

| | PS&S | Product Compliance |
|---|---|---|
| Data the checks use | DG master data and document-based DG records held in TM, plus PS&S phrase management (H12) | Product Compliance data; DG statuses of freight orders, freight units and freight bookings can be viewed (H12) |
| Modes named | The PS&S section names the ADR points check (road) and the IATA shipper's declaration (air) (H12) | Road, rail, air and ocean freight (H12) |
| Where it is switched on | Customizing under Dangerous Goods Processing Based on PS&S (H12) | Customizing under Dangerous Goods Processing Based on PC (H12) |

*What the material does not establish:* why the two are mutually exclusive, beyond the statement that only one can be active. It also does not say how to switch from one option to the other.

## DG data that the checks rely on: dangerous goods master data (created by shippers for products classified as DG, displayed with the Display Dangerous Goods Data app) and document-based dangerous goods records (created by logistics service providers at item level in the business document) (H12, Dangerous Goods Processing Based on PS&S)
In the PS&S-based processing, the DG checks are based on the available DG data, which is created in two ways (H12):

- **Dangerous goods master data (created by shippers).** When a shipper enters a product in the product master data in TM and the product is classified as dangerous goods, the shipper also creates a DG master data record for it. You display it with the Display Dangerous Goods Data app on the launchpad.
- **Document-based dangerous goods records (created by logistics service providers).** When an LSP receives DG data from a shipper, it enters that data in the business document by creating a document-based DG record at item level.

The checks run in TM. They use DG master data or the document-based records created for forwarding orders, freight orders or freight bookings (H12).

The reason for the second kind: an LSP transporting DG for customers "may not always have the required dangerous goods master data in your SAP TM system" (H12, Document-Based Dangerous Goods Records). So the practical rule is that a shipper maintains master data, and an LSP works with records in the documents. The records can be typed in manually or created automatically when TM creates a forwarding order from a business partner's data, through the relevant enterprise service (H12). The two options are covered in more detail below.

## Dangerous Goods Indicator Profile: defined in SAP EHS Management, assigned to the material in the master data, selectable when the material is relevant for dangerous goods; the examples listed are Environmentally Relevant and Highly Viscous and In Bulk/Liquids. Indicator profiles are specified in Customizing under Specify Indicator Profiles for the Material Master (S48600, Dangerous Goods Indicator Profile; H12, Configuration of Dangerous Goods Processing)
S48600 says the DG indicator profile field is defined in SAP Environment, Health, and Safety Management (SAP EHS Management). A profile can be selected if the material being added is relevant for dangerous goods and for any documentation that accompanies that kind of material. The examples listed are:

- Environmentally Relevant
- Highly Viscous and In Bulk/Liquids

In H12 (Configuration of Dangerous Goods Processing), the indicator profile is one of the settings for DG master data. In the master data you assign an indicator profile to the material. You define the profiles in Customizing for Transportation Management under Basic Functions > Dangerous Goods > Dangerous Goods Processing Based on PS&S > PS&S Services > Dangerous Goods Management > Dangerous Goods Checks and Dangerous Goods Documents > Common Settings > Specify Indicator Profiles for the Material Master. The other master data step is to create the DG master data record for the product with the Display Dangerous Goods Data app.

*What the material does not establish:* what the profiles do technically beyond "selectable when the material is DG-relevant", and which other profiles exist besides the two examples.

## Configuration of DG processing (PS&S): environment parameters for PS&S Services, phrase management and a text pattern in the DG master, a DG profile that activates the DG checks (and is also required to enter DG data without checks), assignment of the DG profile to forwarding order, forwarding quotation, freight unit, freight order and freight booking types, the transportation mode, the block reason Error During Dangerous Goods Check, and the methods FUB_DG and VSR_DG assigned to the process controller strategy (H12, Configuration of Dangerous Goods Processing)
H12 lists the settings that apply to both DG master data and document-based records. Use it as a checklist:

1. **Environment parameters** for the processes in PS&S Services: Customizing under Dangerous Goods Processing Based on PS&S > PS&S Services > Basic Services > Specify Environment Parameters.
2. **Phrase management and a text pattern.** TM uses the PS&S framework to extract DG information, as phrases, for printing. To enable it you set up phrase management in PS&S Services, assign a text pattern in the DG master, and define phrases in phrase management.
3. **A DG profile** (Define Dangerous Goods Profile) that activates the DG checks. It defines general conditions for processing DG, such as conditions for displaying error messages.
4. **Assignment of the DG profile to the document types you use:**
   - Freight Order Management > Freight Order > Define Freight Order Types
   - Freight Order Management > Freight Booking > Define Freight Booking Types
   - Planning > Freight Unit > Define Freight Unit Types
   - Forwarding Order Management > Forwarding Order > Define Forwarding Order Types
   - Forwarding Order Management > Forwarding Quotation > Define Forwarding Quotation Types

   If you want to enter DG data in a document without performing any DG checks, you still have to assign a DG profile to the document type.
5. **General settings** for DG processing (Define Common Settings for Dangerous Goods Processing). These include the settings needed for printing DG data.
6. **The transportation mode**, defined in Master Data > Transportation Network > Transportation Lane > Define Transportation Mode.
7. **The methods FUB_DG and VSR_DG** assigned to the relevant process controller strategy (Basic Functions > Process Controller > Assign Methods to a Strategy). This is what enables the DG checks during freight unit (FU) building and vehicle scheduling and routing (VSR) optimization.
8. **The block reason.** You define which processes are blocked when an error occurs in a DG check, for the block reason Error During Dangerous Goods Check (Basic Functions > General Settings > Define Block Reason Codes).

For document-based records there are two further prerequisites, covered below: a UI profile, and the check method set-up. Loaded SAP EHS Regulatory Content can be used as the basis for the records (H12).

## Adapting DG processing: create a function module, specify it as a DG check method, assign the method to a check schema; BAdIs can change the input data for checks and printing or read template data from an external database (H12, Adapting DG Processing)
H12 describes four ways to adapt DG processing:

- **Your own check.** Create a function module, specify it as a DG check method (Customizing: PS&S Services > Dangerous Goods Management > Dangerous Goods Checks and Dangerous Goods Documents > Dangerous Goods Checks > Specify Dangerous Goods Check Methods), then assign the method to a check schema (Specify Dangerous Goods Check Schemas).
- **Input data.** You can change, delete or extend the input data for the DG check and for printing data with the BAdI: Definition of Data for Printing and Checking for Dangerous Goods (under Integration with PS&S).
- **Template data.** You can read template data from an external database instead of the PS&S Services database with the BAdI: Dangerous Goods Processing (under Template Data).

The same method, schema and business context mechanism is used for delivered methods. The ADR points check has the prerequisite that you assign a check schema to the relevant business documents and then assign the new check method to that schema. The business context is specified under Common Settings > Specify Business Context (H12).

## Dangerous goods checks process: the check runs for forwarding orders, forwarding quotations, freight orders and freight bookings, on save or manually; it is repeated during freight unit building (for example the mixed loading check), on the freight units, during VSR planning (transportation proposal, freight unit vehicle check) and on the resulting freight document. Errors block the document or FU with the block reason Error During Dangerous Goods Check; messages are in the application log (object /SCMTMS/TMS, subobject DG) (H12, Dangerous Goods Checks)
**Why several checks.** H12 says that "due to different risks involved in transporting DG, the system carries out checks in different ways and at different process steps". The aim is to ensure compliance of the successor documents, the FUs and freight orders (FOs).

**Prerequisite.** DG master data or document-based records exist, and the configuration above is done. During planning, document-based records created at item level in forwarding orders are transferred automatically to the freight orders or freight bookings. They are read-only there. You can also create records at item level in the freight documents.

**The chain (H12):**

| Step | What happens |
|---|---|
| 1. Forwarding order | The check runs on save, or manually with the Check pushbutton or menu entry. If the system identifies DG, it selects the Dangerous Goods checkbox. If there are DG errors, the forwarding order is blocked. |
| 2. Freight unit building | The system can check DG during FU building, for example with the **mixed loading check**. It analyzes how items can be combined and considers incompatibilities. If the check returns errors, items are prevented from being transported in the same FU. |
| 3. Freight units | The FUs are checked after creation and each time the FU changes. The Dangerous Goods checkbox is selected when DG is identified, and the FU is blocked if there are DG errors. |
| 4. VSR planning, transportation proposal | VSR optimization assigns FUs to vehicle resources and creates freight documents. When creating transportation proposals the system runs the DG check and offers an alternative proposal. In batch processing it selects the first solution without DG errors. The mixed-loading check covers incompatible FUs. A **freight unit vehicle check** avoids planned documents that contain DG FUs incompatible with certain resources. These incompatibilities go into the optimization run. |
| 5. Freight document | The resulting freight document is checked after the VSR run and each time it changes. In manual planning it is checked on every save or when triggered manually. At this point you can create document-based DG records in the freight document, and they are included in the checks. |

**What blocks.** If a DG check has errors, the Statuses tab page shows the block reason Error During Dangerous Goods Check in the Blocking Information group box. The system blocks the relevant processes according to the Customizing for that block reason. The details show every check performed, including the DG check.

**Where to look afterwards.** DG information is shown on the forwarding order, forwarding quotation, freight unit, freight order, freight booking and transportation proposal user interfaces, with the check result in the document. Further item-level DG information is on the Dangerous Goods tab page. In the forwarding order overview you can define a query that selects forwarding orders by DG data, for example by a specific DG number and regulation. Messages from the checks during FU building and VSR optimization are in the application log, object /SCMTMS/TMS and subobject DG, which you open from the Application Log app on the launchpad.

## ADR 1.1.3.6 points check: exemption if the points total does not exceed 1000 points; check method /SCMTMS/DG_ADR_1000_POINTS; Points = Relevant Quantity x Multiplication Factor; the relevant quantity depends on the aggregate state (master data uses item-level gross weight, net weight or gross volume; DG records use gross weight, net weight or nominal volume of receptacle); points are summed per document item, header and stage, with FWO, FWQ, OTR and FU as the sum of items and the road freight order as the maximum of the stages (H12, ADR 1.1.3.6 Points Check Calculation)
**Background.** ADR is the European agreement on the international carriage of dangerous goods by road. Its section 1.1.3.6 describes an exemption based on a points calculation. If the total does not exceed 1000 points, the exemption can be applied (H12).

**Set-up.** The check method is /SCMTMS/DG_ADR_1000_POINTS. You enable the points check in Customizing (Specify Dangerous Goods Check Methods) and assign the method to the check schema and business context, as in the configuration section above.

**Formula.** Points = Relevant Quantity x Multiplication Factor.

**Relevant quantity.** It depends on the aggregate state specified for transport:

| Data source | Quantity taken from | Options |
|---|---|---|
| DG master data (shippers) | Item level | Gross Weight, Net Weight, Gross Volume |
| Document-based DG records (LSPs) | DG record level | Gross Weight, Net Weight, Nominal Volume of Receptacle |

For each aggregate state in the DG master or DG record you assign a relevant quantity, in Customizing under Define Points-Relevant Quantities for ADR 1.1.3.6 DG Exemption. The multiplication factor is entered in the DG master (master data) or in the DG record (document-based records).

**Totals** are calculated at three levels (H12):

- Document item: the sum of points for an item in a document.
- Document header: the sum of points for all items in the document.
- Document stage detail: the sum of points for all items assigned to a stage.

**Document-level rule:**

| Document | Points are |
|---|---|
| Forwarding order (FWO), forwarding quotation (FWQ), order-based transportation requirement (OTR), freight unit (FU) | the sum of the points of the assigned items |
| Road freight order (FO) | the maximum of the points of each stage |

*What the material does not establish:* why the road freight order uses the maximum of the stages. The help gives the rule only. Reading it as "a stage is one leg of the vehicle's load" would be an inference and is not stated.

## Transport restrictions Prohibited (not eligible under ADR 1.1.3.6) and Unlimited (not considered in the points calculation); if either flag is set, no points are calculated (H12, Transport Restrictions)
For DG you can specify that a product or material is (H12):

- **Prohibited**: not eligible for consideration under ADR 1.1.3.6.
- **Unlimited**: not considered in the points calculation under ADR 1.1.3.6.

If either flag is set, no points are calculated for that product or material. For master data you set the flags in the DG master. For document-based records you set them in the DG record, using the UI profile (see the UI profile section below).

## Points check in planning: the ADR points check is activated in the freight unit building rule; the VSR optimizer uses vehicle resources with dimensions flagged as relevant for the ADR points check, and the check can be deactivated in the planning profile or in the transportation cockpit (H12, VSR Optimization)
**In FU building.** You activate the ADR points check in the freight unit building rule for the relevant document type, and the system considers the points limit when building FUs. The H12 example: with a limit of 1000 points per FU and three items of 500 points each, the system generates two freight units. The reasoning is that one FU can hold at most two of the items, because three would reach 1500.

**In VSR optimization.** To activate the points check in the optimizer, you create vehicle resources, maintain their dimensions and flag them as relevant for the ADR points check. If these resources are maintained in the Capacity Selection Settings of the planning profile, the VSR optimizer takes the ADR 1.1.3.6 points limit into account as a planning-relevant capacity for the resource.

**Switching off.** You can deactivate the points check in the optimizer settings of the planning profile, or during manual planning in the transportation cockpit.

## Document-based dangerous goods records: entered manually on the Dangerous Goods tab page at item level or created automatically from a business partner's data; records from forwarding orders are copied to the freight documents as read-only; item check method /SCMTMS/DG_CHECK_WITH_CONTENT; they can be saved as released or unreleased templates and searched by DG Number Type, DG Number, Packing Group and Variant ID (H12, Document-Based Dangerous Goods Records; Creation and Editing of Document-Based Dangerous Goods Records; Creation and Use of Dangerous Goods Templates)
**Entering records.** You create, edit or delete a record at item level on the Dangerous Goods tab page of a forwarding order, freight order or freight booking. The system uses the UI profile assigned to the forwarding order item type or to the freight document type. You can create a record from a template or without one, and the UI profile is shown at the top of the tab page. Alternatively, records are created automatically when TM creates a forwarding order from data received from a business partner, using the UI profile of the forwarding order item type. The profile DG_INBOUND_PROFILE contains the full set of fields that can be received in the inbound message. It is useful when you do not know which DG data will be sent. During planning, records from forwarding orders are copied to freight orders or freight bookings as read-only, and you can add further records at item level there.

**Prerequisites for a user to enter a record (H12):**

1. The general DG settings from the configuration section.
2. A UI profile for document-based DG records.
3. For field checks, enhanced check methods. To have an individual field checked during a consistency check of the whole document, you enhance the check methods in Specify Dangerous Goods Check Methods, and you must use the existing function module /SCMTMS/DG_CHECK_WITH_CONTENT as the item check method.
4. Authorizations. The help names the authorization objects C_EHSP_TPP (phrase items) and C_SHEP_TPG (phrase library and phrase group) for phrases, and M_MATE_DGM for DG master data.

**What limits the consistency check.** The system checks a record against the available DG records in TM. These exist when you save a record as a template. If no template data has been saved, the system cannot perform any checks. Loading SAP EHS Regulatory Content provides master data records that serve as templates. Only fields marked in the UI profile as relevant for the check are checked. A field not flagged for the check is not checked.

**Templates.** You save a record together with the business document. If you are authorized, you can also save it as a reusable template, either released or unreleased. Only released templates can be used to create new records. To find a released template, filter by DG Number Type, DG Number, Packing Group and Variant ID. You can check the processing status of templates in the DG master data with the Display Dangerous Goods Data app.

## UI profiles for document-based DG data: fields organized in UI groups, assigned to regulations (one tab page per regulation), field properties (separate editing per regulation, checkbox, table view, corresponding field, custom label, consistency check), phrase sets; defined in the Edit UI-Profile for Dangerous Goods app; a profile in use cannot be changed but can be copied; DG_INBOUND_PROFILE and Generate Inbound Profile support automatic record creation (H12, Definition of UI Profiles for Document-Based DG Data)
A UI profile controls which fields and regulations are available on the Dangerous Goods tab page at item level and how the information is laid out (H12). LSPs can build profiles around the DG they regularly carry for customers. You define profiles in the **Edit UI-Profile for Dangerous Goods** app.

**Building blocks:**

- **Fields.** You select them from the PS&S Services master data, or use fields you defined yourself.
- **UI groups.** They organize the fields. You define a group title (for example "Substance Rating") and its position by column and row number. A group can be shown as a table. If a phrase set is assigned to a field in such a group, the table gets a link for creating or changing the phrase.
- **Regulations.** Every field belongs to at least one regulation, and each regulation gets its own tab page within the Dangerous Goods tab page. You assign regulations at profile level, group level or field level. Fields inherit them from the profile or group and you can change them per field. If none is set at profile or group level, assign at least one at field level.
- **Field properties.** Whether a field is edited separately per regulation (otherwise the value from the first regulation tab page carries over to the others). Whether the shown value is an initial value. Whether it is a checkbox. Whether it also appears in the table view. A corresponding field, such as a unit of measure for a gross weight field. A custom label. Whether a consistency check applies to it (if not specified, the field is not checked).
- **Phrase sets.** If PS&S master data already has a phrase set assigned, the system shows it and you cannot change it. Otherwise you can select phrase sets for fields of the same data type as fields with assigned phrase sets.
- **Preview** of the layout before saving, and **download and upload** of profiles to move them between clients.

**Rules and links to document types.**

- A profile in use (for example assigned to a forwarding order item type that has an order with DG data) cannot be changed. You can copy it to create a new one.
- For forwarding orders, assign the UI profile to the forwarding order item types (Define Item Types for Forwarding Order Management).
- For freight orders and freight bookings, assign the UI profile to the DG profile (Define Dangerous Goods Profile), then assign the DG profile to the freight order types or freight booking types.
- The Generate Inbound Profile pushbutton creates a profile that supports automatic record creation from business partner data.
- The multiplication factor, the relevant quantity per aggregate state and the Prohibited and Unlimited flags for document-based records are defined through the UI profile.

## Phrase management and Loading Dangerous Goods Content: phrases are maintained with the Manage Phrases app; the Dangerous Goods Content Loader loads purchased content (regulations, phrases, Customizing data) in steps, phrases before regulations, and generates DG master data records whose product number contains the UN number (for example UN-1993-III-0101) (H12, Loading Dangerous Goods Content)
**Phrase management.** You open phrase management from the Manage Phrases app on the launchpad. In a DG record, a link next to a phrase field opens a dialog where you create, change or display phrase texts in several languages. You can also search for existing phrases and select them.

**Content loading.** The Dangerous Goods Content Loader app loads content you have bought from a content provider (H12).

- **Prerequisites.** You have downloaded the zip file. It contains a CSV file per regulation, CSV files for phrases, and a CSV file mapping the 3-character regulation prefix to the 12-character regulation name. You have specified the regulations to load in Customizing (Specify Dangerous Goods Regulations), entering the 12-character name from the CSV file.
- **Steps in the app:** 1 Upload Zip File (to a staging area). 2 Load Phrase Data (load the phrases before the regulations). 3 Load Regulation Data (select regulations from the list; if one cannot be selected, check it is specified in Customizing; load mode lets you repeat for data with errors). 4 Monitor Import Processes. 5 Check Generated Messages (filter by regulation type, message type, or context such as PHRASES_LOAD or REGULATIONS_LOAD). 6 Summary.
- **Why it matters.** The content comprises DG regulations, regulation texts such as substance names, phrases and the required Customizing data. It is useful if you do not have DG master data, for example as an LSP. The generated DG master data records serve as templates for document-based records and as the basis for consistency checks, for example to check whether a shipper gave the correct temperature data for a UN number.
- **Result.** For each content record the system creates a DG master data record. Its product has a generated product number that contains the UN number, for example UN-1993-III-0101, so you can search for imported content by UN number. You display the records with the Display Dangerous Goods Master app.

## Dangerous goods documents: the shipper's declaration (IATA, generated for a freight booking from the DG master, viewable in the Output Management tab) and the standard print forms ADR Dangerous Goods Note, RID Dangerous Goods Note and IMO Dangerous Goods Declaration (H12, Shipper's Declaration; Standard Print Forms)
**Shipper's declaration (H12).** IATA requires that shipments classified as DG tendered to air carriers and air freight forwarders are accompanied by the IATA shipper's declaration for dangerous goods. The shipper is responsible for completing it correctly. Based on the freight booking, the system finds the relevant DG master and generates a declaration stating the nature and quantity of the DG and the type of packing material. You view it in the Output Management tab of the freight order. SAP provides a template that the shipper must implement and review, adapting it to its processes, in particular the packing function and country-specific or region-specific deviations. Integration is with SD and MM based on the sales order business object.

Prerequisites: Output Management is configured, the output profile is specified for the freight booking type (Define Freight Booking Types), and the PPF action settings and the action definition /SCMTMS/PRINT_SHPRS_DCL are specified for the output agents of the relevant business objects.

Example in the help: as a shipper you create a forwarding order, assign FUs with DG items, and assign the order to an air freight booking. The system finds DG in the booking and generates the declaration with information from the DG master.

**Standard print forms (H12).** SAP delivers default templates for:

- **ADR Dangerous Goods Note**: jurisdictions under the UNECE Agreement of 30 September 1957 on the international carriage of dangerous goods by road.
- **RID Dangerous Goods Note**: jurisdictions under the UNECE regulation on the international carriage of dangerous goods by rail.
- **IMO Dangerous Goods Declaration**: jurisdictions under the IMDG Code of the International Maritime Organization.

You can build custom forms instead. For the ADR Dangerous Goods Note, you print it from a freight order, and it is only produced when products in the freight order are classified as dangerous goods. The help says that classification is determined by Product Compliance (see the next section).

*What the sources show side by side:* the shipper's declaration is generated from the DG master (the PS&S side), while the ADR note prerequisite refers to classification by Product Compliance. The help does not explain how the two fit together. Treat this as a point to verify. I only read the ADR note's prerequisites in detail, and did not check the RID and IMO prerequisite texts.

## DG processing based on Product Compliance: covers road, rail, air and ocean freight; activated in Customizing under Activate Product Compliance and Activate Business Features for Product Compliance; the DG statuses of freight orders, freight units and freight bookings can be viewed; FUB_DG and VSR_DG are also assigned (H12, Dangerous Goods Processing Based on Product Compliance)
H12 says this option lets you transport DG by road, rail, air and ocean freight in compliance with international regulations. You can view DG statuses for freight orders, freight units and freight bookings.

**Configuration (H12):**

1. Enable the Product Compliance processes: Customizing under Basic Functions > Dangerous Goods > Dangerous Goods Processing Based on PC > Activate Product Compliance.
2. Specify which business features from Product Compliance you want to use (Activate Business Features for Product Compliance).
3. Assign the methods FUB_DG and VSR_DG to the relevant process controller strategy, to use DG checks during FU building and VSR optimization.
4. Optionally, use the BAdI: Definition of Data for Product Compliance Integration to change the parameters of the API calls for DG checks, document description and EDI structure.

S48600 gives the surrounding picture. Compliance checks run across the value chain (stock transfer orders, sales orders, outbound deliveries, freight orders) and block a document when transport is not allowed.

*What the material does not establish:* how a Product Compliance check proceeds step by step inside TM, or how the check chain above (forwarding order, FU building, VSR, freight document) behaves in this option. The chain is documented for the PS&S option only. The statuses and process details are in the Product Compliance topic that H12 refers to, which is not part of the corpus.

## Practice
Write a one-page DG checklist for one business document type of your choice, for example a forwarding order type or a freight order type. List:

1. The Customizing prerequisites: the DG profile and its assignment to the document type, the block reason Error During Dangerous Goods Check, the methods FUB_DG and VSR_DG on the process controller strategy, and the UI profile (document-based records) or DG master data (shipper case).
2. The checks the document goes through along the process chain, from the forwarding order through FU building and VSR planning to the freight document, with what is blocked at each step.
3. If you use the ADR 1.1.3.6 exemption: the check method, the check schema and business context, the points-relevant quantities, the activation in the freight unit building rule, and the vehicle resource and planning profile settings.

## Self-check
Can I explain how TM checks dangerous goods along the process chain, from the forwarding order to the freight document, to a transportation planner without notes?
