# Session 14 — Enterprise Services, ESR Content and BRFplus

## Overview
This session covers two technical topics that sit behind the business processes of earlier sessions. The first is how SAP TM exchanges transportation orders, transportation requests, customs and trade-compliance requests, and other messages with partners and with SAP ERP through enterprise services, and which additional ESR content (integration scenarios and mappings) complements them (H14). The second is BRFplus, the rule framework in which business rules are modeled once and reused by calling applications (H15). In practice you read this material when you must find which operation carries a message, why a message failed, which BAdI can change its content, or how a rule is structured.

## Enterprise services for SAP TM are documented per process component, each with business process objects, service interfaces and service operations; additional ESR content (integration scenarios, mappings) complements them
H14 is organized in a fixed hierarchy. A **process component** (for example Transportation Order Processing) has one or more **business process objects** (for example Transportation Order); each object has **service interfaces** (for example Export Declaration Requesting Out); each interface groups **service operations** (for example Request Export Declaration). Every level has a Definition and a Technical Data table, and the operation level adds Business Context and Use, Related Operations, Features, Message Types, Prerequisites, Error Handling, Integration, Configuration and Enhancements (H14).

The enterprise services themselves are described in section 2 of H14. Section 3 covers Other Web Services, and section 4 covers Additional ESR Content, that is, integration scenarios and mappings stored in the Enterprise Services Repository (H14). The following items work through each part.

*What the material does not establish:* the ESR is not explained as a product here, only the content that SAP TM places in it.

## Process component TransportationOrderProcessing covers the ordering of transportation services from carriers: it lets shippers, logistics service providers and carriers exchange transportation-relevant data and create, change or cancel freight orders, freight requests for quotation or freight bookings, assign transportation demands to capacities, and let shippers create delivery proposals
The definition in H14 is short: "the ordering of transportation services from carriers". The process component gives shippers, logistics service providers and carriers functions to exchange transportation-relevant data and to create, change or cancel freight orders, freight requests for quotation and freight bookings. It also lets them assign transportation demands to transportation capacities, and lets shippers create delivery proposals for further processing in the corresponding logistics execution system (H14, Transportation Order Processing).

From a shipper's perspective a carrier may also be a logistics service provider (LSP), whose business typically consists of consolidating transportation demands from several shippers into containers or full truck loads (H14).

Do not confuse it with TransportationRequestProcessing: that component is defined as the processing of requests from an ordering party for the provision of transportation services (H14).

## In the TransportationOrderProcessing scenario a shipper sends a transportation order to a carrier, who receives it as a transportation request and is expected to confirm; the carrier may subcontract the order to other carriers, who reply with confirmations
The scenario in H14 runs in three steps.

1. During transportation planning, the shipper decides which freight units go on its own vehicle resources and which are subcontracted to carriers.
2. The shipper sends a transportation order to a carrier. The carrier receives it in the form of a transportation request and is expected to send a confirmation to the shipper.
3. The carrier can then do refined planning on the transportation request and decide whether its own resources or one or more subcontractors execute the service. If it subcontracts, it sends a transportation order to the subcontractors, who can reply with confirmations. These activities happen in the carrier's own business system (H14).

A concrete pair in H14 shows how this looks at operation level. The outbound operation Request Transportation Order (technical name TransportationOrderRequest_Out, category B2B, asynchronous, released) sends a new or updated freight order to a carrier. The corresponding inbound Maintain Transportation Request (TransportationRequestRequest_In, category B2B, asynchronous, Released with Restrictions) in TransportationRequestProcessing creates or changes a forwarding order from it. The inbound side answers with the outbound Confirm Transportation Request, which says whether the carrier accepted or rejected the freight order, and a Cancel Transportation Request inbound operation cancels the forwarding order when the freight order is cancelled (H14, Request Transportation Order; Maintain Transportation Request).

Request Transportation Order can also be sent as a notification for late changes, with no further subcontracting or tendering. That use needs an EDI communication profile assigned to the carrier in the business partner master data and a BAdI that determines the freight orders (H14).

## The business process object TransportationOrder supports requesting a quotation, requesting execution of a transportation service, booking freight space, cancellations, replies (accept, modify, decline), shipping instructions (waybill notification), loading appointments and notifications about loading or unloading
The Transportation Order business object is defined as an order from an ordering party to a carrier to transport goods from one or more shippers to one or more consignees under agreed terms; it can include the assignment of vehicle resources and stages, and can have the character of a freight request for quotation (H14, Transportation Order). It enables shippers, logistics service providers, and carriers who subcontract to:

- request a quotation by sending a freight request for quotation;
- request execution of a transportation service by sending a freight order;
- book freight space by sending a freight booking;
- send a cancellation of a freight request for quotation, freight order or freight booking;
- receive replies in which the carrier accepts, modifies or declines;
- send a shipping instruction (also called waybill notification) based on an already confirmed freight booking, or receive one, in which case a replicated freight booking document is created in the receiving system (typically an import organization informed by an export organization in a multinational company);
- request a loading appointment by sending planning information about loading or unloading to a business partner such as a warehouse or container freight station;
- receive notifications that loading or unloading has been executed.

It also lets a freight order or freight booking be updated from current execution information, for example customs processing information (H14).

## Process component TransportationRequestProcessing handles customer requests for transportation services: A2A scenarios (Order Integration with order-based transportation requirements OTR, Delivery Integration with delivery-based transportation requirements DTR) and B2B scenarios (Forwarding Quotations, Forwarding Orders, Forwarding Orders Based on Forwarding Quotations)
H14 defines this component as the processing of requests from an ordering party for transportation services. A request represents, in a B2B scenario, a forwarding quotation or a forwarding order, and in an intracompany (A2A) scenario an order-based transportation requirement (a preliminary request for a particular order) or a delivery-based transportation requirement (a finalized request for a particular delivery) (H14).

| Type | Scenario | What happens |
|---|---|---|
| A2A | Order Integration | Orders move from order processing to transportation request processing, where an order is an OTR. Used for sales orders, purchase orders (including stock transport orders) and returns orders |
| A2A | Delivery Integration | Deliveries move from delivery processing, where a delivery is a DTR. Used for inbound and outbound deliveries |
| B2B | Forwarding Quotations | The carrier receives a request for quotation, creates a forwarding quotation, then confirms it (sends a quotation) or sends a rejection reason; the customer can cancel the request for quotation |
| B2B | Forwarding Orders | The carrier receives a new or updated freight order and creates or updates a forwarding order, then confirms; the customer can cancel, if the forwarding order status allows it |
| B2B | Forwarding Orders Based on Forwarding Quotations | A forwarding order is created with reference to an existing forwarding quotation |

A customer can be a shipper, a logistics service provider, or a carrier who subcontracts to another carrier (H14).

In practice the A2A entry point is Maintain Transportation Request (IntracompanyTransportationRequestRequest_In, category SAP A2A, inbound, asynchronous, released) in the Intracompany Transportation Requesting In interface. It receives order or delivery data from sales order, purchase order, customer return, outbound delivery and inbound delivery processing and creates or changes OTRs or DTRs. It can also create or change DTRs after a delivery split triggered by SAP ERP, SAP EWM or SAP TM (H14).

## The business process object TransportationRequest lets a carrier receive requests for quotation and create forwarding orders, and lets a shipper plan and execute order-based and delivery-based transportation requirements
For a carrier, the Transportation Request object supports two activities (H14, Transportation Request):

- receive a request for quotation from a customer, submit a forwarding quotation, and, if the customer accepts, create a forwarding order based on it;
- create a forwarding order from an order received from a customer. The carrier uses it to plan and execute and for the customer settlement process.

For a shipper, the object enables planning and execution for OTRs and DTRs created from orders and deliveries received from a logistics execution system (H14).

H14 adds a naming link: in the SAP TM back end, a forwarding order, an OTR and a DTR each correspond to an instance of the Transportation Request business object (H14).

## A service interface groups operations and is described by category (for example SAP A2A, B2B) and direction (inbound or outbound); a service operation is described by release state, technical name, namespace, direction, mode, idempotency and P2P communication enabled
Every interface and operation page has a Technical Data table. How to read it (H14):

| Level | Fields in the table |
|---|---|
| Service interface | Entity type, Category (for example SAP A2A or B2B), Direction (Inbound or Outbound) |
| Service operation | Entity type, Release State, Technical Name, Namespace, Direction, Mode, Idempotency, P2P Communication Enabled. Some operations also show Application Component, Category, Change/Update Behavior or Business Context |

Examples of values in the source: mode Asynchronous or Synchronous; idempotency Yes, No or Not Applicable; namespace http://sap.com/xi/TMS/Global; application components such as TM-GT-GTS, TM-ERP-TR, TM-FWM-FWO and TM-FRM-FRO (H14).

For example, Request Export Declaration is Released, ExportDeclarationSUITERequest_Out, Outbound, Asynchronous, idempotency No, P2P communication enabled Yes (H14).

*What the material does not establish:* the tables give the values but do not define idempotency or P2P communication in prose in the parts read.

## Release state of an operation is shown as Released or Released with Restrictions; the technical name carries a direction suffix such as _Out or _In (for example ExportDeclarationSUITERequest_Out and TransportationRequestRequest_In)
Release State is a field in each operation's Technical Data. Both values appear throughout H14. Request Export Declaration and Change Transportation Order based on Export Declaration Confirmation are Released. Request Transportation Customs Declaration, Maintain Transportation Request in the forwarding-order interface, and Check Transportation Request Ordering Party Creditworthiness are Released with Restrictions (H14).

The suffix of the technical name matches the direction: ExportDeclarationSUITERequest_Out is outbound, and TransportationRequestRequest_In and ExportDeclarationSUITEConfirmation_In are inbound (H14). The suffix is a quick way to read direction before opening the table.

*What the material does not establish:* the sections read do not explain what the restrictions are. They are not defined in the text, so check the operation page itself (for example its Constraints and Prerequisites sections) before relying on an operation.

## Worked example of an outbound/inbound pair: Request Export Declaration (outbound, asynchronous) sends parties, items, means of transport, Incoterms and related document IDs to a customs management application, and Change Transportation Order based on Export Declaration Confirmation (inbound) receives the export declaration ID, the movement reference number (MRN) and an approval indicator and updates the order and its customs status
**Request.** A shipper needs an export declaration to transport customs-relevant goods. Request Export Declaration sends the request to a customs management application. It sends the parties (for example seller and consignee), the items with packaging and quantities, the means of transport, the Incoterms and the IDs of related documents such as a sales order or outbound delivery. The message type is ExportDeclarationSUITERequest (H14).

**Trigger.** The operation is triggered in the SAP TM back end when a customs declaration is requested for items in an order. For a freight order, the order must have the execution status defined in the customs profile and must be based on a delivery-based transportation requirement (H14).

**Customs side.** The customs management application creates the export declaration and sends it to the customs authority. If the authority approves it, it issues a movement reference number (MRN) (H14).

**Confirmation.** The customs application sends a confirmation (ExportDeclarationSUITEConfirmation) containing the export declaration ID, the MRN and an indicator showing whether the declaration is approved. Change Transportation Order based on Export Declaration Confirmation (ExportDeclarationSUITEConfirmation_In, inbound, asynchronous) adds the ID and MRN to the order and updates its customs status. It also handles a confirmed cancellation: it updates the status of the customs activity and a new export declaration can be requested later. Its prerequisite is that Request Export Declaration has sent the request (H14).

**Related operations.** Request Export Declaration Cancellation (ExportDeclarationSUITECancellationRequest_Out) is the outbound partner for cancelling. Both operations exchange data with Customs Processing operations in SAP Global Trade Services (components TM-GT-GTS and SLL-LEG-CUS-EXP) (H14). A newer, more general pair, Request Transportation Customs Declaration and Change Transportation Order Based on Transportation Customs Declaration Confirmation, covers export, import and transit declarations and security filing (H14).

## Inbound operations support Forward Error Handling (FEH) with error categories such as DCE (Determination and Conversion Error), PRE (Processing Error) and PRE.TEE.LRE (Lock Request Error); Maintain Transportation Request also writes missing-master-data errors to the business application log
Inbound operations in H14 have an Error Handling section stating that they support Forward Error Handling (FEH) and listing the categories used (H14):

| Category | Meaning in H14 |
|---|---|
| DCE | Determination and Conversion Error |
| PRE | Processing Error |
| PRE.TEE.LRE | Lock Request Error (in some operations written "Lock Error") |

H14 refers to the code list of the global data type LogItemCategoryCode for details of each category. Not every inbound operation lists all three: Change Transportation Order based on Export Declaration Confirmation lists only DCE and PRE, while Maintain Transportation Request lists all three (H14).

The forwarding-order variant of Maintain Transportation Request also checks, for example, whether the required master data exists, and displays errors in the business application log if it does not (H14). In the integration scenario TM_ERPInvoiceIntegration, a step that SAP TM or SAP ERP cannot process triggers an error in the system concerned (H14).

*What the material does not establish:* how FEH is operated (monitoring, reprocessing) is not described in the parts read, only that the operations support it.

## Implementation notes: carriers and customers must be defined as business partners in the SAP TM back-end system, with standard IDs recommended for business partners, locations and products; outbound communication needs a logical system with an Outbound Queues queue type assigned in Customizing for SCM Basis (Integration Basic Settings for Creating the System Landscape)
**Master data.** In Transportation Order Processing you define your carriers as business partners in the SAP TM back end; in Transportation Request Processing you define your customers. H14 gives the path in SAP NetWeaver Business Client as Master Data, General, Define Business Partner. SAP recommends standard IDs for each business partner and for each location and product involved (H14, Master Data for B2B Communication).

**Customizing for outbound.** For outbound communication such as the trade compliance check, you define a logical system for the client that sends the messages and assign a queue of type Outbound Queues to it in Customizing for SCM Basis under Integration, Basic Settings for Creating the System Landscape, Assign Logical System and Queue Type. The logical system must be marked as an SAP system, and you also check Name Logical Systems, Assign Logical Systems to a Client, Maintain Business System Group and Settings for qRFC Communication (H14, Trade Compliance Check Requesting Out).

**Other prerequisites.** Depending on the operation: a connection to SAP Global Trade Services for customs and trade compliance, a connection to SAP Credit Management plus credit segments for the creditworthiness check, a connection to SAP ERP for order and delivery integration, and an EDI communication profile for notification messages (H14).

## Enhancements: operations list a BAdI (for example /SCMTMS/EXP_SE_EXPDE_REQ for ExportDeclarationSUITERequest_Out) and some an enhancement spot (/SCMTMS/CDC_SE_SPOT_CDC)
Operations have an Enhancements section naming the Business Add-Ins that can adapt them. Examples (H14):

| Operation | Enhancement |
|---|---|
| Request Export Declaration (ExportDeclarationSUITERequest_Out) | BAdI /SCMTMS/EXP_SE_EXPDE_REQ |
| Change Transportation Order based on Export Declaration Confirmation | BAdI /SCMTMS/EIN_SE_EXPDE_ANS |
| Request Transportation Customs Declaration | Enhancement spot /SCMTMS/CDC_SE_SPOT_CDC and BAdI /SCMTMS/CDC_SE_CDC_REQ |
| Change Transportation Order Based on Transportation Customs Declaration Confirmation | Enhancement spot /SCMTMS/CDC_SE_SPOT_CDC and BAdI /SCMTMS/CDC_SE_CDC_CNF |
| Request Trade Compliance Check | BAdI /SCMTMS/CPC_SE_CPC_REQ |
| Maintain Transportation Request (A2A) | BAdI /SCMTMS/TRQ_SE_REQREQ |
| GetTransportationDocumentURI | BAdI /SCMTMS/TDO_IF_SE_GET_URI |

## Additional ESR content: integration scenarios such as TM_ERPInvoiceIntegration live in the SAPTM IC software component in namespace http://sap.com/xi/TMS/Global/IC; mappings are named <Message name in SAP TM>_to_<IDoc type in SAP ERP> or the reverse
**Integration scenarios.** H14 section 4.1 says the integration scenarios are in the ESR in the SAPTM IC software component in namespace http://sap.com/xi/TMS/Global/IC. Two are described: TM_ERPInvoiceIntegration and TM_ERPOrderIntegration.

TM_ERPInvoiceIntegration transfers settlement documents from SAP TM to SAP ERP to create billing documents or accruals. It uses asynchronous steps between an SAP TM and an SAP ERP system of the same company (H14):

- Forwarding Settlement: SAP TM requests a billing document in SAP ERP from a forwarding settlement document; SAP ERP creates, changes or cancels it and confirms; SAP TM updates the document. A credit memo can follow in the same way.
- Freight Settlement: SAP TM requests accruals (a service purchase order and one or more service entry sheets) from a freight settlement document; SAP ERP confirms; SAP TM updates the document.
- Invoice Notification: SAP ERP notifies SAP TM that a supplier invoice was received, and SAP TM updates the posted amounts.
- Invoice Simulation: SAP TM asks SAP ERP for data to preview a customer invoice or credit memo.

SAP TM can start communication at any time with Send Forwarding Settlement Request or Send Freight Settlement Request. SAP ERP can start with Send Invoice Notification only after it has processed a freight settlement request, and with Simulate Customer Invoice only if the customer invoice has not yet been created (H14).

TM_ERPOrderIntegration transfers orders and deliveries from SAP ERP to SAP TM as transportation requirements, and lets SAP TM propose deliveries to be created in SAP ERP (H14).

**Mappings.** Interface mappings and message mappings are in the same component and namespace. They follow one of two naming conventions, depending on direction: `<Message name in SAP TM>_to_<IDoc type in SAP ERP>` or `<IDoc name in SAP ERP>_to_<message name in SAP TM>` (H14, Mappings). For example, TransportationOrderSCMExecutionRequest_to_SHPMNTSHPMNT05 maps a TM message to the IDoc SHPMNT.SHPMNT05. The freight order ID is mapped to field TKNUM, so it becomes the ID of the ERP shipment, which requires external number ranges for the relevant shipment types. Shipment type and transportation planning point are set by value mapping in the Integration Directory of the PI system (H14).

## The Web service GetTransportationDocumentURI (namespace http://sap.com/xi/TMS/UX) is an inbound, synchronous operation that lets SAP ERP display SAP TM documents, for example from invoice verification (MIRO, MIR7, MIR4) and agency business (WLF3, WZR3)
GetTransportationDocumentURI is listed in section 3, Other Web Services, with namespace http://sap.com/xi/TMS/UX, available as of SAPTM 1.0, category Inbound, mode Synchronous (H14).

- **Invoice verification (MIRO, MIR7, MIR4).** From the ERP transaction you can display a specific freight settlement document in the browser, for example to check an incoming carrier invoice against it.
- **Agency business (WLF3, WZR3).** You can display a specific freight order or freight settlement document, for example when creating a payment or vendor billing document. This is relevant for shippers using the cost distribution function in SAP TM.

The SAP TM inbound operation is triggered by the outbound operation of the same name in SAP ERP, which requests the URL of a business document. SAP TM generates the URL from the document type and number and returns it, and the caller opens the browser (H14).

Prerequisites: the business function LOG_TM_IV_INT in SAP ERP for invoice verification (it adds the TM Doc. tab with a Details pushbutton), the business function LOG_TM_ORD_INT_II for agency business, and point-to-point communication set up between the two operations (see SAP Note 1451472) (H14).

A second synchronous inbound web service, BusinessDocumentFlowTMInformationbyBusinessObjectReferenceQueryResponse_In, returns TM document flow and statuses for an ERP order or delivery (H14).

## BRFplus provides an API and a UI to define and process business rules and reuse them in different applications; typical uses are validation, matching responsibilities or products, calculation of costs, overhead and risks, and technical configuration
BRFplus provides a comprehensive application programming interface (API) and user interface (UI) for defining and processing business rules, modeled in an intuitive way and reusable in different applications. Scenarios named in H15 are: validation of data and detection of invalid data and states; matching responsibilities, suitable products and locations; calculation of costs, overhead and risks; and BRFplus as a technical configuration engine. It supports simulation, trace, transport and XML export and import (H15, Use).

H15 also states that BRFplus is an ABAP-based framework, best suited for integration into an ABAP-based environment. For Java-based environments or SOA landscapes it names SAP Business Rules Management (SAP BRM) as an alternative; the two can call each other, and BRFplus web services can still make sense when most data sits in an ABAP back end (H15, BRFplus Overview).

*What the material does not establish:* this document does not say which SAP TM functions use BRFplus. Do not link them from memory.

## BRFplus major components are application, function, catalog, expression, action and data object; the function is the interface between the rule and the calling application and holds the business logic; rules are implemented as expressions assigned to a function
H15 lists the major components as application, function, catalog, expression, action and data object. The function is the interface between a business rule and the application that uses it. It serves as a container for the entire business logic, however complex. Rules are implemented as expressions that are assigned to a function (H15, Use).

The function acts as a link between application code and BRFplus code. It imports the context from the calling application, passes it to the assigned top expression or rulesets, and returns the result. The workbench can generate an ABAP code snippet, an RFC-enabled function module or a web service to call a function (H15, Function).

## A function has a context (rule input) and a result (rule output), both made of data objects of type element, structure or table; it can run in functional mode, event mode, or both
The rule input is the **context** and the rule output is the **result**. Both consist of data objects of type element, structure or table (H15, Use).

- The context is a container of data objects assigned as import parameters. You choose them to suit the calling application, and they also define which objects the expressions of the function can access.
- The result data object returns the value calculated by the function's expressions. In event mode the result is automatically the predefined Actions table, which records the actions triggered by the rulesets (H15, Function).

| Mode | How it runs |
|---|---|
| Functional mode | Needs a top expression. The function evaluates it, with any nested expressions, and the expression result is the function result. Typical for simpler cases with a clear output |
| Event mode | Uses rulesets instead of a top expression. Rules whose condition is met trigger actions. Typical for more complex cases and where no result is needed |
| Functional and Event mode | A top expression and a result data object are mandatory. The top expression is processed first, then the associated rulesets run, possibly changing the context |

(H15, Function; Modes of Operation)

## Data object types build on each other: an element is an elementary type, a structure combines elements and structures, and a table takes the fields of one structure (or of one element, giving a one-column list); data objects can be bound to DDIC elements or ESR global data types
H15 (Data Objects and Types) says a data object describes data and acts as a data carrier in the context or result of an expression or action.

- **Element.** A predefined elementary type that cannot be broken down or extended. Subtypes include text (up to 255 characters when persisted), number, boolean, amount, quantity and timepoint.
- **Structure.** A combination of any number of elements and structures, so structures can be nested. A practical limit applies: if the fully qualified name of a field in a deeply nested structure exceeds 255 characters, code generation is no longer possible.
- **Table.** Its fields come from exactly one element or one structure. A table does not build up its fields one by one. Assigning an element instead of a structure gives a one-column table, that is, a simple list.

**Data binding.** Instead of defining a type manually, a data object can be bound to a DDIC element, structure or table type, to a global data type (GDT) in the ESR, or to an existing BRFplus element. Binding imports the type, length and domain values, for instance ISO country codes from a DDIC data element, and keeps reused values consistent. A DDIC structure or table type is imported with all its fields, with the client field and raw fields filtered out. A DDIC NUMC field is always turned into a text data object. Binding to GDTs is currently supported only for a limited scope of SAP-internal development projects (H15, Data Binding).

## Expression types (for example Boolean, Case, Decision Table, Decision Tree, Formula, Value Range) define the computational power of BRFplus; a decision table compares input against condition rows from the top and returns the result of the first row where all cells match, so the most specific rows belong first
Expression types define the computational power of BRFplus. Each type is a self-contained computational unit with its own logic, and expressions can be nested and reused as building blocks, starting with the top expression of a function. The predefined types are Boolean, BRMS Connector, Case, Constant, DB Lookup, Decision Table, Decision Tree, Dynamic, Formula, Function Call, Loop, Procedure Call, Random Number, Search Tree, Table Operation and Value Range. Step Sequence and XSL Transformation are deprecated (H15, Expressions).

**Decision table.** It compares input against a list of predefined condition combinations, each with an assigned result (H15, Decision Table Expression).

1. Evaluation starts with the first row. Each cell gives a boolean result.
2. If all cells in a row are true, evaluation stops and the result of that row is returned.
3. Otherwise processing continues with the next row until a match or the end of the table.

Because of this top-to-bottom processing, define the most specific condition first and then increasingly general ones. H15's example has a payment target of 60 days for region Europe alone and 30 days for Europe and Germany. If the region-only row comes first, Germany wrongly gets 60. The check functions detect many such errors, and the Rearrange function moves cells with unspecified values to the bottom (H15).

Other settings: by default (single match mode) the first matching row wins; with Return all matches found (multiple match mode) all matching results are collected and the result data object must be a table. If nothing matches, an exception is raised unless Return initial value if no match is found is set (H15).

## Actions are the interactive part of BRFplus (Call Procedure, Log Message, Send Email, Start Workflow, Workflow Event); they have no output and can only be the final step of a processing branch
Actions are a special flavor of expression types for the interactive part of BRFplus. They can be triggered by a rule, by a matching condition in a decision table, decision tree, search tree or case expression, or as a follow-up action of another action. Actions have no output, so they can only be the last step of a branch; no calculation can follow an action as a response to what it changed. Action type names carry a trailing (Act) and a verb-object pattern, as in Call Procedure (Act) as opposed to the Procedure Call expression (H15, Actions).

| Action | What it does (H15) |
|---|---|
| Call Procedure | Runs function modules or methods of an ABAP OO class in the back end. Like all actions it returns no result, and follow-up actions can be defined |
| Log Message | Writes system messages to the application log during rule processing, for example for documentation or audit. Message types are Abort, Error, Exit, Information, Status and Warning, subject to restrictions set on the application |
| Send Email | Notifies a person about a situation in the system |
| Start Workflow | Starts a workflow |
| Workflow Event | Raises a workflow event |

*What the material does not establish:* the Start Workflow and Workflow Event actions are only named in the part of H15 read for this item, and are not described there.

## A rule (If condition with a True branch and an optional False branch) can only be triggered inside a ruleset; a ruleset is assigned to one function in event mode, with priority 0 to 99 controlling execution order
**Rule.** A rule object is the technical form of a simple business rule. It consists of an embracing If condition: the True branch is required and the False branch is optional. A rule can only be triggered in the context of a ruleset and never stand-alone. Its operations are triggering an action, processing an expression whose result can update the context, and initializing or updating context data objects (H15, Rule).

A rule has no context of its own. It uses the context of the ruleset it is in. Because one rule can be assigned to many rulesets, it can access only the context data objects that all referencing rulesets share, that is, their intersection (H15).

**Ruleset.** A ruleset is a collection of rules and an entry point for processing, an alternative to a top expression. It must be assigned to a function in event mode or in functional and event mode. A function can have any number of rulesets, but a ruleset has exactly one function, and the relationship is stored from the ruleset's side (H15, Ruleset; Function).

**Priority.** With several rulesets, execution follows the priority value, 0 to 99. The list is sorted ascending, so the lowest value runs first. The default 0 means no priority and is processed after all rulesets with a priority above 0. Rulesets run one after another, never in parallel, and no ruleset can stop the next one (H15, Function).

Several levels decide whether a rule runs: the function is called, the ruleset is enabled, the ruleset precondition holds, the rule precondition holds, the rule is enabled, the current date is in the validity period, and the precondition of the activity holds (H15, Ruleset).

## A catalog is a filter that hides the repository and shows business users only the objects needed to maintain rules; an application is the container for all objects and has a storage type (system, master data or customizing) that cannot be changed after creation
**Catalog.** It simplifies rule maintenance for business users by hiding the repository and showing only the objects needed in a business scenario. It serves as a filter on all repository objects. A typical business catalog offers, for example, decision tables, while functions, data objects, constants, formulas and actions stay invisible. A catalog can contain folder nodes, object nodes (references to BRFplus objects) and catalog nodes (references to nodes of another catalog) (H15, Catalog).

**Application.** It is a container of BRFplus objects, a reflection of a system functionality you want to enhance with rules. It sits at the top of the object hierarchy, and every object must be assigned to an application. You can define as many applications as you like (H15, Application).

**Storage type.** There are three: system application (default), master data application and customizing application. They behave differently in system transports, and master data applications are always local. The storage type and the locality setting are inherited by all objects in the application. The storage type is chosen when the application is created and cannot be changed afterwards (H15, Application).

## Typical BRFplus workflow: create an application, create a function with context, result and top expression, activate the objects, simulate the function, then integrate it with the calling application; the workbench is started with transaction BRFPLUS
The workflow in H15 (Typical Workflow):

1. Create an application, the BRFplus object that collects all objects of the business logic.
2. Create a function, assign context and result to it, and assign a top expression.
3. Activate the objects.
4. Simulate the function.
5. Integrate the BRFplus function with your application. Here "application" means your own solution, not the BRFplus object.

The workbench is started in the back end with transaction BRFPLUS or in a browser with the system-specific workbench URL. It is based on Web Dynpro ABAP and needs the role SAP_BC_FDT_ADMINISTRATOR or a custom role with a subset of its authorizations. It has a Navigation Panel and a Work Area, and two UI modes: Simple Mode (recommended for business users) and Expert Mode (for business experts and developers) (H15, Understanding the User Interface).

## Practice
Build a one-page reference table with five enterprise service operations taken from H14. For each, record the process component, the business object, the direction, the mode, the release state and the related operation. Good candidates from this session are Request Transportation Order, Maintain Transportation Request (forwarding order), Request Export Declaration, Change Transportation Order based on Export Declaration Confirmation, and Request Trade Compliance Check. Then add a short BRFplus sketch of one rule of your choice, showing the application, the function, the context data objects, the result data object and the top expression.

## Self-check
Can I explain how SAP TM exchanges transportation orders and requests through enterprise services, and how BRFplus rules are structured, to a technical colleague without notes?
