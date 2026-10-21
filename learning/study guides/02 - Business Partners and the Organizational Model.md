# Session 02 — Business Partners and the Organizational Model

## Overview
This session covers the master data that says who takes part in a transportation process (business partners) and which organizational units own the documents (the TM organizational model). It also covers the few material master fields that TM uses. Partner and organization data are read by almost every TM document, from forwarding orders to freight settlement documents. Many questions later come down to which role, partner function or organizational unit applies, so this session sets the vocabulary.

## Business partner master data: in SAP S/4HANA the master data of customers and vendors is managed as business partners (previously handled separately in SAP ERP); it is maintained with transaction BP or a Fiori app, a business partner can be assigned to multiple company codes, and it is categorized as person, organization or group
In SAP ERP, customers and vendors were handled separately. In SAP S/4HANA their master data is managed centrally as business partner master data (S4TM2, S48600). A business partner is any entity with which the company has a business relationship (S48600). Each one is identified by a unique business partner number (H03).

- **Maintenance:** with transaction BP or a corresponding app from the SAP Fiori launchpad (S4TM2). In TM, H03 names the launchpad apps Create Customer (Sales), Create Vendor (Purchasing) and Create Forwarding Agent for defining a business partner. The Maintain Business Partner app is used in the carrier review exercise (E01).
- **Company codes:** a business partner can be assigned to multiple company codes, and the same business partner number can be maintained across company codes (S4TM2, S48600).
- **Categories:** person, organization or group. An organization is an umbrella term for a company, a department of a company or an association. A group is, for example, a shared living arrangement, a married couple or an executive board (S4TM2, S48600).

## Business partner roles: general data is defined once and roles are assigned for each business context; the role General Business Partner (000000) is assigned automatically on creation; roles most used in TM include FLCU01 Customer, FLCU00 FI Customer, FLVN01 Vendor, FLVN00 FI Vendor, CRM010 Carrier, TM0001 Driver, BUP004 Organizational Unit, BUP001 Contact Person
The link between a business partner and other components is a role concept. A BP role corresponds to a business context in which the partner can appear (S4TM2). General data is defined once, such as name, address, communication data, identification numbers and business partner status (H03). Specific data is stored per role. This avoids redundant data, because the general data does not depend on the partner's function or on application-specific extensions (S4TM2). When a business partner is first created, the BP role General Business Partner is assigned automatically (S4TM2, S48600).

The roles most commonly used in TM (H03, S48600):

| Role | Code |
|---|---|
| Business Partner (General) | 000000 |
| Customer | FLCU01 |
| FI Customer | FLCU00 |
| Vendor | FLVN01 |
| FI Vendor | FLVN00 |
| Carrier | CRM010 |
| Global Trade Services: Customs Office | SLLCOF |
| Driver | TM0001 |
| Organizational Unit | BUP004 |
| Contact Person | BUP001 |
| Prospect | BUP002 |
| Employee | BUP003 |
| Internet User | BUP005 |

S4TM2 also lists Invoicing Party (BBP006) among the roles relevant to shipping. To create a customer, create a generic business partner and assign the roles Customer and FI Customer. For a vendor, assign Vendor and FI Vendor (S48600). Assigning a role activates the additional fields for that context (S48600).

*Source difference:* H03 and S48600 write the FI Customer role code once as FLCU001 in running text, while their role lists and S4TM2 give FLCU00. This guide uses FLCU00.

## Organizational levels of the roles: FLCU01 allows data on sales area level (TM defaults distribution channel and division in Define General Settings for TM), FLVN01 and CRM010 on purchasing organization level, FLCU00 and FLVN00 on company code level
The level at which a role holds data decides which organizational unit is needed to read it.

- **FLCU01 Customer:** data on sales area level. A sales area is a combination of sales organization, distribution channel and division (H03).
- **FLVN01 Vendor and CRM010 Carrier:** data on purchasing organization level (H03, S48600). In the carrier simulation, order currency and payment terms agreed with the carrier are maintained on the Purchasing tab (E01).
- **FLCU00 FI Customer and FLVN00 FI Vendor:** data on company code level (H03, S48600).

TM documents such as forwarding orders and forwarding quotations contain no distribution channel and no division. You therefore maintain default values for both in Customizing for Transportation Management, under Master Data, Basic Functions, General Settings, Define General Settings for TM. These defaults are added to the sales organization defined for TM, so that business partner master data stored at sales area level can still be accessed (H03).

## Carrier and driver data: role CRM010 contains the data of role FLVN01 plus TM-specific data (Regulated Agent Code, IATA Agent Code, CASS Account, SCAC Codes, Airline Codes, Service Level Codes, Carrier Service Codes); the Transport Data tab appears for the Carrier role; role TM0001 holds home location, qualifications, shift sequences, validity periods and absences
**Carrier (CRM010).** The role contains the data of FLVN01 plus these TM-specific fields (H03, S48600):
- Regulated Agent Code
- IATA Agent Code
- CASS Account
- SCAC Codes
- Airline Codes
- Service Level Codes
- Carrier Service Codes

In the Review Carrier Information simulation (E01), you open the Maintain Business Partner app and search for the business partner with the string TM*CAR*, then choose TM-CAR-10. When you change the BP role to Carrier, the Transport Data tab appears, and it holds the TM-specific data. The Purchasing tab holds the purchasing organization level data.

**Driver (TM0001).** Drivers operate vehicles and are defined as business partners with the role driver (S4TM2). The role holds home location, qualifications, shift sequences, validity periods and absences (S4TM2, S48600). H03 describes a driver as any person who can operate vehicles and perform transportation-related tasks as a result of certain qualifications. H03 lists availability, absences, qualifications and a Supply Chain Unit as the driver's home location. When you assign a vehicle to a freight order, the system checks the driver assignment. If no driver was assigned, it assigns the vehicle's default driver. If a vehicle resource requires qualifications, the system checks the driver's qualifications against them (H03). Driver types, which categorize drivers by duties and qualification, are defined in Customizing under Master Data, Business Partners, Define Driver Types (H03).

## Partner functions: a partner function is the role a business partner takes in a process (for example sold-to party, ship-to party, payer, bill-to party, consignee, shipper, carrier, driver, freight forwarder); one partner can have several functions; no special BP roles are needed in Customizing for partner functions, and the system can check that a BP is compatible with a document partner function
A partner function is a particular role that a business partner can take during the process. In the S4TM2 example, one customer orders the products (sold-to party) and another receives them (ship-to party). One partner can have several functions. If all partner functions of the customer partner type are assigned to one partner, the same customer is sold-to party, ship-to party, payer and bill-to party (S4TM2).

Partner functions commonly used in the shipping process (S4TM2): consignee, bill-to party, carrier, shipper, ordering party, driver, payer and freight forwarder. In TM documents such as a forwarding order, the business partner appears as a party that takes part in the process and assumes partner functions such as ship-to party, shipper or sold-to party (H03).

**Roles versus functions.** A BP role is a business context of the master data (what data is held). A partner function is the part played in one document. H03 says you do not need to define special business partner roles in Customizing for the partner functions: you can assign any business partner to the different partner functions. You can still configure the system to assign BP roles to allowed document partner functions. The system then checks whether a business partner is compatible with the document's partner function, and the business partner search help returns only partners that can be used for that function (H03).

## Business partner determination: a partner determination profile (Customizing, Master Data, Business Partners, Define Partner Determination Profiles) sets the partner functions available in a document, the level of control the user has, and how partners are determined; it is assigned to document types such as forwarding orders, freight orders, freight bookings, settlement documents, agreements and RFQs
Business partner determination lets the system determine the partners in a business document. This cuts down manual errors and the need to enter a partner for each partner function (S4TM2, H03, S48600). You create a partner determination profile in Customizing for Transportation Management under Master Data, Business Partners, Define Partner Determination Profiles. The profile determines three things (H03, S4TM2):

1. **The partner functions available in a business document:** you specify the list of partner functions the system makes available.
2. **The level of control the user has:** depending on the settings, the user can change or delete a partner function, or add one from the list of available functions. A partner function can also be set so that it cannot be changed or deleted.
3. **How the system determines the partners** for the partner functions (see the next item).

You assign the profile to document types, and different profiles can go to different types. For example, one profile controls forwarding orders and another controls forwarding settlement documents (H03). The types are forwarding orders, forwarding quotations, forwarding settlement documents, freight orders, freight bookings, freight settlement documents, freight agreement RFQs, forwarding agreement quotations, freight agreements, forwarding agreements, internal agreements and mutual agreements (H03, S4TM2).

*Source difference:* S48600 lists only six document types (freight orders, freight bookings, freight settlement documents, freight agreement RFQs, freight agreements, internal agreements). H03 and S4TM2 give the longer list above.

**Incoterms.** When you create a forwarding order of a given type and enter an Incoterm, the system uses the Assign Partner Determination Profiles Based on Incoterms Customizing activity. That profile overwrites the one assigned to the forwarding order type in Define Forwarding Order Types (H03).

## Ways to determine a partner: partner function with source partner function, source partner function in the BP master data (BP Relationship), a fixed business partner for a partner function (may not yet exist in the Customizing system), and relationship category
All four use the invoicing party as the example (S4TM2, H03).

| Way | Customizing setting | What the system does |
|---|---|---|
| Partner function with source partner function | Partner function Invoicing Party, source type Partner Function, source function Sold-to Party | When the user enters Customer01 as sold-to party, Customer01 becomes the invoicing party. |
| Source partner function in the BP master data | Source type BP Relationship, source role Sold-to Party | The system reads the Partner Function tab of the BP in transaction BP. For logistics service provider (LSP) customer APP_1 with the role FLCU01, that tab names APP_INV as invoicing party for an organizational unit. For a forwarding order with organization 561234 and sold-to party APP_1, APP_INV is assigned as invoicing party. |
| Fixed business partner for a partner function | Source type Business Partner, business partner CSI_CARR1 | CSI_CARR1 is always assigned as invoicing party. The partner may not exist in the Customizing system, so you can assign a partner in one system and transport the setting to a system where it exists (H03 uses carrier LUF). |
| Relationship category | Source type Relationship Category (for example BBP002 Has Invoicing Party), optionally with Rev. Rel. | The system uses the relationship maintained in transaction BP. With Rev. Rel. selected, both directions are considered: shipper SHP has invoicing party INV, and invoicing party INV is invoicing party of shipper SHP. |

H03 adds a further option, which is not one of the four above: a Business Add-In. You enter Business Add-In in the Srce Type field and implement BAdI: Specific Partner Assignment.

*What the material does not establish:* it gives no guidance on when each way is the better choice. Any choice between them must be inferred from the mechanics in the table.

## Business partner relationships, texts and blocking: relationship category Has Contact Person is used in tendering and Has Subsidiary / Agent describes subsidiaries and agents of a carrier; additional texts serve as printing addresses or signatures; a BP can be blocked for forwarding quotations and orders at complete BP, company code, purchasing organization or sales organization level
**Relationships.** After defining a BP and assigning roles, you can create relationships between BPs. The category Has Contact Person is used in the tendering process. The category Has Subsidiary / Agent describes subsidiaries and agents of a carrier organization (H03). H03 says TM delivers BP roles for business partners of the type Person, but its extract does not list which ones.

**Additional texts.** On the Additional Texts tab page (transaction BP), role Business Partner (Gen.), you can enter texts such as addresses or signatures. TM uses them as printing addresses or signatures on printing documents such as air waybills. Text types with a maximum number of characters and lines make the texts fit the print areas. Texts can be entered in several languages. The default text type for printing addresses is set in Assign BP Text Types to Partner Functions (H03).

**Blocking.** The block stops a business partner being assigned to a forwarding quotation or a forwarding order. You can also block it so that, within a forwarding order, the system prevents forwarding settlement documents from being created. Blocks are hierarchical in the BP master record and can be set at these levels: complete business partner, company code, purchasing organization, sales organization. They are set manually, from the launchpad apps Create Customer (Sales), Create Vendor (Purchasing) or Create Forwarding Agent (H03). For example, the FLCU00 company code block on a sold-to party makes the system check the forwarding order. H03 also lists the central billing, order and posting blocks.

## Carrier profile: a profile characterizing a carrier's transportation capabilities, one per carrier with the Carrier role; it can hold freight code sets, transportation lane and carrier-specific parameters, product freight groups, transportation groups, equipment groups and types, fixed transportation costs and dimension costs; it is used for transportation proposals and carrier selection
A carrier profile characterizes the transportation capabilities of a carrier. It stores information used in a similar constellation for multiple carriers. Carriers are business partners with the role Carrier, and you can create only one profile per carrier (H03).

What it can hold (H03): freight code sets, transportation lane and carrier-specific parameters, product freight groups, transportation groups, equipment groups and equipment types, fixed transportation costs and dimension costs.

**Process (H03).** Prerequisites are the Carrier role on the BP and, in Customizing, defined transportation lanes, freight code sets, product freight groups, transportation groups, equipment groups and types, and means of transport.
1. Open Define Carrier Profile (SAP Easy Access Master Data, General, or the launchpad app).
2. Choose the carrier and save. A performance attribute is the Cont. Move (Continuous Move) checkbox.
3. Make settings on the tab pages Transportation Lane (for example business share or priority), Freight Code Set (country or region and means of transport are required), Product Freight Group, Transportation Group, Equipment, Fixed Transportation Costs and Dimension Costs.
4. Save. You can then search the settings and find all carriers that have them.

**Where it is read.** H03 states the carrier profile is used when creating transportation proposals and when selecting a carrier.

## Organizational structure in TM: optional corporate organization, company organization (company code, local currency, legal entity), sales organization (forwarding orders, quotations, forwarding settlements), purchase organization and group (freight orders, bookings, freight settlements), planning and execution organization (resources, freight orders) and forwarding house (sales, purchasing and planning/execution in LSP scenarios); units map to S/4 units through the BSG Org. Unit field; plants and shipping points are created as locations
S48600 gives the generic idea first: organizational structures frame the company, segregate data and transactions, restrict user access, and are a basic requirement for authorization and role setups. In TM the structure can be based on a connected SAP system, but you can also create organizational units that do not exist there. TM maps its organizational units to S/4 organizational units through the BSG Org. Unit field. Plants and shipping points are created as locations (S48600). The units, with the documents they serve (S48600, H03):

| Unit | What it is | Documents and objects |
|---|---|---|
| Corporate organization | Optional, a single entry point into the structure in TM, represents the group organization | None named |
| Company organization | Corresponds to the company code, holds the local currency, legal entity; used by transportation charge management (TCM) for invoicing and charging | None named |
| Sales organization (with office and group) | Structures and manages the sale of logistics services and their execution; several can sit under one company organization | Forwarding orders, forwarding quotations, forwarding settlements |
| Purchase organization and group | Procures materials and services | Freight orders, freight bookings, freight settlements |
| Planning and execution organization and group | Plans and/or executes shipments | Resources, freight orders |
| Forwarding house | One unit that sells, purchases and plans/executes in LSP scenarios | Documents of all three functions |

**Settlement link.** For settlement integration, the system uses the business system group (BSG) assigned to an organization to decide whether the settlement document is posted to an external system or to internal SD or MM. For a forwarding settlement document it uses the sales organization in the document. If the BSG's logical system differs from the client's logical system, the document goes to external SD through enterprise services. If it is the same, it goes to internal SD (H03).

## Organizational model rules: organizational units have a unit function (sales 4, purchasing 2, forwarding house 89) and a unit role (Organization, Office, Group); the hierarchy is fixed (for example Group under Office or Organization, Office under Organization; for purchasing and planning/execution only Group under Organization); /SCMTMS/ORG_INT transfers units from S/4HANA core components; optional checks ensure carrier and customer BPs belong to a sales or purchasing organization of their company or of the document header
**Unit function and role (H03).** Each organizational unit is defined by its unit function and unit role.
- Sales organization: function 4 (Sales), role 1 (Organization).
- Purchasing organization: function 2 (Purchasing), role 1 (Organization).
- Forwarding house: function 89 (Forwarding House), role 1 (Organization). It is used both as a sales and as a purchasing organization. The BSG Org. Unit assigned to it is the ID of both, so the sales and purchasing organization IDs are identical.
- For each sales organization, purchasing organization and forwarding house you assign a BSG Org. Unit. It is the ID used to retrieve organization-dependent business partner data, and it is maintained in Customizing.

**Hierarchy rules (H03).** The hierarchical relationship is fixed.
- Sales unit function: roles Organization, Office and Group. A Group can go under an Office or an Organization, and an Office under an Organization.
- Purchasing or Planning and Execution unit function: only the roles Organization and Group, and a Group can only go under an Organization.

For example, to rebuild a purchasing or planning and execution structure, you create one unit with the Organization role and one with the Group role, then assign the Group to the Organization (H03).

**Creating and changing the model (H03).** Create the model with PPOCE and change it with PPOME. The recommendation is to use /SCMTMS/ORG_INT to transfer organizational units from the core components of SAP S/4HANA to TM. Employees are assigned through positions in PPOME by assigning a BP with the role Employee. When you save a change, the system adds a technical business partner and sets the business system group.

**Optional checks (H03).** You can activate checks that every business partner with the carrier or customer role in the document is assigned to a sales or purchasing organization in the partner's own company, to the sales or purchasing organization in the document header, or to both. They apply to forwarding orders, forwarding agreements, forwarding settlement documents, freight orders, freight bookings, freight agreements and freight settlement documents. You activate them under Basic Functions, General Settings, Define General Settings for TM.

*What the material does not establish:* it does not explain why TM needs its own units beyond the mapping and access purposes stated above.

## Material master attributes relevant to TM: base unit of measure, alternative units of measure, gross weight, net weight, volume, transportation group (for example palletized or refrigerated goods) and material freight group, which is transferred from the sales order item to the product item of the freight unit
The material master (also called product master data) is the central record of materials transported, manufactured, sold or purchased, accessible to purchasing, inventory management, MRP, transportation and warehousing (S48600). The material type, for example FERT finished goods, HAWA trading goods, DIEN services, VERP packaging material or LEIH returnable packaging, controls how the number is assigned, which screens appear and which fields are mandatory, optional, hidden or display-only (S48600).

The transport-relevant attributes sit in the Sales view (Sales: General/Plant) (S48600):
- **Base Unit of Measure (BUoM):** the lowest-level unit of the material.
- **Alternative units of measure (AUoMs):** multiples of the BUoM.
- **Dimensions:** Gross Weight, Net Weight and Volume. They can matter to shipping companies when deciding how to pack and ship.
- **Transportation Group:** classifies materials with similar processing conditions, for example palletized goods, refrigerated goods and dairy products.
- **Material Freight Group:** groups materials to determine their freight classification and ultimately the freight code. In TM it is transferred from the sales order item to the product item of the freight unit.

## Practice
Draw a one-page business partner and organization map for a fictional logistics service provider.
1. List its carrier, customer and driver business partners and the roles assigned to each (for example CRM010, FLCU01, FLCU00, TM0001).
2. Write one partner determination example for the invoicing party. Name the source type, the source function and the result the system would produce.
3. Sketch a small organizational model with corporate, company, sales, purchasing and forwarding house units. Show for each the documents it serves.

## Self-check
Can I explain business partner roles, partner determination and the TM organizational structure to a project stakeholder without notes?
