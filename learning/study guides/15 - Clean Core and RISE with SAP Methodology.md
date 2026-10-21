# Session 15 — Clean Core and RISE with SAP Methodology

## Overview
This session explains why SAP promotes a clean core for cloud ERP, what "clean core" means across five dimensions, how the implementation type affects it, and how the RISE with SAP Methodology helps customers get the core clean and keep it clean. It draws on two courses: MCC100, which defines and explains clean core, and SL_RISE419, which describes the RISE with SAP Methodology, its framework, toolchain, expert guidance and dashboard. In practice you meet this material in project governance, extension decisions and go-live quality checks. The two courses speak about SAP Cloud ERP in general, and this session does not add links to SAP TM.

## Why a clean core is needed: a cloud ERP such as SAP Cloud ERP receives updates continuously, so extensions and integrations must be managed differently from on-premise SAP ERP; SAP developed the clean core concept for this
SAP's ERP software traditionally ran in the customer's own data center. SAP Cloud ERP is a cloud-native solution that combines current industry best practices with continuous innovation. Because a cloud ERP such as SAP Cloud ERP receives updates on a continuous basis, customers need a slightly different approach to extensions and integrations than in an on-premise environment. SAP developed the "clean core" concept for customers to follow, so that the effectiveness of SAP Cloud ERP is maximized (MCC100, Adjusting Business Models).

The same point returns in the later units. As a cloud-based solution, SAP Cloud ERP means customers must take a modified approach to extensions, integrations and operations compared with on-premise SAP ERP (MCC100, Introduction to Unit 2). In practice this explains why custom code, modifications and old interfaces become a problem: they must survive updates that the customer does not schedule. The sources do not describe an update frequency.

## The challenges behind clean core fall into three areas: business adaptability (supply chain disruptions, changing customer preferences, regulatory compliance), technological change, and landscape complexity
MCC100 groups the challenges into three areas, one lesson each in Unit 1.

| Area | What the lesson covers |
|---|---|
| Business adaptability | Disruption of supply chains, changing customer preferences and regulatory compliance |
| Technological change | New technological advancements, accelerating innovation, optimizing and automating business processes, fostering agility |
| System landscapes | Business model adaptations, key application adjustments, responding to changing customer needs; the need for a simple, flexible infrastructure, helped by cloud computing and agile development |

(MCC100, Lessons 1 to 3 of Unit 1)

MCC100 closes each lesson with the same answer: SAP Cloud ERP is the solution for business change, for technological challenges and for landscape challenges, through its extensibility and integration capabilities (MCC100).

*Source note:* the plan calls the third area "landscape complexity"; MCC100 itself frames the third lesson as adapting system landscapes and the need for a simple and flexible infrastructure.

## Business model and supply chain pressure: supply chain disruptions (natural disasters, geopolitical tensions, COVID-19) expose single-source vulnerability, and businesses must pivot business models quickly without the technology landscape being an impediment
Global supply chains are the backbone of many industries, and disruptions affect production schedules, inventory levels and customer satisfaction. Natural disasters, geopolitical tensions and events like COVID-19 exposed their vulnerabilities. Businesses that rely on a single source of supply for critical components or materials are vulnerable, and any disruption can have a domino effect on production. Responses named include diversifying supply sources, strong supplier relationships, risk management strategies, and digital technologies such as advanced analytics and supply chain visibility platforms (MCC100, The Impact of Disruptions in Global Supply Chains).

On the business model side, entire new markets can appear without warning and the first mover often reaps most of the profits. Companies must be able to pivot their business models quickly and their technology landscape must not be an impediment (MCC100, Adapting Business Models).

MCC100 illustrates this with the Heidelberg Hotel chain during COVID-19. Napkins and masks were hard to procure, guests wanted contactless check-in and phone-based room access, and regulations changed quickly. The hotel adopted SAP Cloud ERP and, thanks to fast deployment and a modern approach to extensions, could move "on the fly" (MCC100, Case Study).

## SAP Cloud ERP and SAP BTP are the response: SAP manages updates, security, compliance and scalability, SAP Cloud ERP is extensible and offers ready-to-go APIs, and SAP BTP is a cloud-native platform as a service that brings together AI, machine learning, data, analytics, database and DevOps
For technological change, MCC100 says SAP manages all updates, so customers do not need extensive IT resources or face business disruption. Security, compliance and scalability are built into SAP S/4HANA Cloud, and backup and disaster recovery, system maintenance and data protection are handled automatically (MCC100, SAP ERP, Clean Core, and Technological Innovation).

For landscape flexibility, the cloud may seem to limit options, but SAP Cloud ERP is extensible and provides ready-to-go APIs with supporting tools and documentation, so customers can integrate with partners or build on top. Continuous innovation does not compromise that flexibility. Alongside it, SAP BTP is a modern cloud-native platform as a service that brings together artificial intelligence, machine learning, data, analytics, database, DevOps and more in a unified environment (MCC100, SAP Cloud ERP, SAP BTP and Landscape Flexibility).

## Definition of clean core: core means five dimensions (processes, extensions, data, integrations, operations); clean means best practices, methodologies and tools exist for each; the clean core concept is a mindset and philosophy supported by governance and guiding principles; the goal is to get the core clean and then keep it clean
**Core.** "Core" refers to five dimensions, or pillars, in no particular order: Processes, Extensions, Data, Integrations, Operations (MCC100, Analyzing Clean Core Components). SL_RISE419 lists the same five and describes them as: processes (sequences of actions in an end-to-end flow), extensions (extra functionality beyond standard), data (configuration, master and transactional data), integrations (communication and data exchange between solutions) and operations (ongoing governance and monitoring) (SL_RISE419, Clean Core Fundamentals).

**Clean.** For each dimension a set of best practices, methodologies and tools exists. If they are used, the dimension counts as clean (MCC100). SL_RISE419 adds that the SAP Activate roadmap provides tasks, deliverables and accelerators that keep each dimension clean (SL_RISE419).

**Clean core.** The video transcript in MCC100 calls it "a mindset and philosophy supported with governance and guiding principles" that lays the foundation for a flexible, future-ready ERP, with stable, upgrade-safe and transparent approaches to processes, extensions, integrations and data, plus a separate platform to innovate. It enables faster deployment, easier adoption of SAP innovations and regulatory changes, and avoids excess technical debt. The goal is to "get" the core clean and then "keep" it clean (MCC100).

MCC100 adds that SAP Cloud ERP with a clean core is so fundamental that "with a clean core" is implied whenever the course says SAP Cloud ERP (MCC100, SAP Cloud ERP and Clean Core).

## A newly provisioned SAP Cloud ERP system is clean by definition; the ideal state is an up-to-date release with cloud-compliant extensions and integration, excellent master data quality and perfect process design
The best case is an up-to-date system on the latest release, with cloud-compliant extensions and integration, excellent master data quality and perfect process design. A newly provisioned SAP Cloud ERP system is clean per definition, and the customer's goal is then to keep the core clean. For customers choosing a system conversion or system landscape transformation, the goal is to get and then keep the core clean (MCC100, Clean Core Components).

SL_RISE419 states it slightly more narrowly: by default a newly provisioned SAP S/4HANA Cloud system, Public or Private Edition, that uses standard processes from SAP Signavio Process Navigator is considered clean (SL_RISE419, Clean Core Fundamentals). MCC100 does not include the Signavio Process Navigator condition.

## Components or distinguishing features of a clean core are minimalism, modularity, scalability, maintainability, and stability and reliability
Both courses give the same five features (MCC100, Components of a Clean Core; SL_RISE419, Clean Core Fundamentals):

| Feature | Meaning |
|---|---|
| Minimalism | Simplicity: identify and remove redundant or obsolete functionality so only essential components remain |
| Modularity | The ERP system is divided into modular, loosely coupled components, for easier maintenance and adaptability |
| Scalability | The system can grow and change without losing performance or stability |
| Maintainability | A simpler code base that developers can understand, modify and enhance more easily |
| Stability and reliability | Fewer dependencies, so the system is less prone to bugs and inconsistencies |

MCC100 illustrates the contrast with ABC Manufacturing, a company with a bloated, heavily customized ERP, performance problems and high maintenance cost. It chose a system conversion to SAP Cloud ERP Private, removed customizations, add-ons and integrations that no longer fit, and planned a later new implementation, with a midterm horizon of about five years (MCC100).

## Implementation types: greenfield (new installation, clean by default), brownfield (system conversion to private edition or on-premise, retained complexity must be cleaned) and selective data transition or system landscape transformation (consolidating several ERP systems); the public edition cannot be chosen in a brownfield approach, and clean core can be accomplished with all approaches
MCC100 starts from three options for SAP S/4HANA: SAP S/4HANA Cloud Public Edition, Private Edition and on-premise (MCC100, Describing Implementation Types and Clean Core). Where the course says "private edition" it applies equally to on-premise unless stated.

| Approach | What it is | Clean core consequence |
|---|---|---|
| Greenfield | New installation or provisioning in public edition, private edition or on-premise | A new system starts clean by default. Full freedom to design processes on current and future needs. Viable if the company can adopt processes on current best practices with a fit-to-standard approach |
| Brownfield | System conversion of an existing system to private edition or on-premise. The public edition cannot be chosen | Retains historic complexity and possibly unwanted customizations, so the system does not start clean. The strategy is to identify which parts of the legacy system to retain, eliminate or transform, and do it. Viable when complex processes are necessary and costly to redesign |
| Selective data transition or system landscape transformation | Consolidates configuration and data of multiple ERP systems, often after mergers and acquisitions, into one private edition or on-premise target | Third option, not explicitly discussed further |

Clean core can be accomplished with all approaches; the choice only affects how to get there. Public edition is described as ready-to-run, private edition and on-premise as tailored-to-fit. Greenfield is the simplest route to a clean core but not always appropriate; the choice correlates with business context, resources and tolerance for change (MCC100).

## Misconceptions: SAP BTP is not the only means (key user and developer extensibility on stack are possible); clean core is not only about custom code and extensibility; it is not only about TCO; fit-to-standard is not the only way, since Tier 1 extensibility also keeps the core clean
MCC100 names four misconceptions (MCC100, Some Misconceptions About Clean Core):

1. "SAP BTP is the only means." BTP is necessary for side-by-side extensions, but key user and developer extensibility, both on stack, are possible with SAP Cloud ERP.
2. "Clean core is only about custom code and extensibility." It also affects business processes, data, integration and operations.
3. "Clean core is only about TCO." It contributes to lower TCO but also enables consumption of the latest innovations and a mindset shift away from on-premise and towards cloud.
4. "Fit-to-standard is the only means." A fit-to-standard system is probably clean, but Tier 1 extensibility options also make and keep the core clean.

*Source note:* SL_RISE419 says that maintaining cleanliness involves building extensions on SAP BTP, separating them from the core ERP software (SL_RISE419, Clean Core Fundamentals). That is narrower than misconception 1 in MCC100, which stresses that on-stack extensions are also clean core compliant. The two courses emphasize different options; they do not state a conflict explicitly.

## Benefits for users (performance, reliable data, stability, flexible processes), for IT (no technical debt from legacy systems, software stack always at the latest release, extensions that do not break upgrades) and for the company (streamlined operations, cost savings, improved decision-making, enhanced collaboration)
MCC100 Unit 3 follows a fictional production company, The Gritty Pixel, through a greenfield implementation of SAP S/4HANA Cloud with SAP BTP, from three viewpoints.

- **Users (Jane, a production clerk).** Performance: processes are harmonized with no interfaces between sales, production and inventory, so the former batch jobs run as real-time applications. Data: reliable and up to date. Stability: release management is integrated in daily operations, with few inconsistencies and little downtime. Processes: clear but flexible, based on SAP best practices.
- **IT (Klaus, developer and interface owner).** Technical debt disappears with the retirement of legacy systems. The core software stack is always at the latest release and updates arrive automatically with a notification. Business processes based on SAP Best Practices are clean core compliant from the start, so revalidation meetings after upgrades are no longer needed. With the ABAP Cloud Development Model and the SAP S/4HANA Cloud Extensibility Model, upgrades do not break extensions and extensions do not break upgrades.
- **Company (Fatima, Chief Customer Officer).** Streamlined operations, cost savings, improved decision-making and enhanced collaboration. A single platform replaced fragmented systems, and SAP BTP provided the platform for her machine-learning proposal.

(MCC100, Unit 3)

## Clean business processes: mantra 'Keep competitiveness while reducing complexity'; establish organizational structure, technical foundation and transformation methodology, set up a prioritized business process hierarchy with end-to-end and functional views; tools named include SAP LeanIX, SAP Cloud ALM, SAP Signavio Process Manager and SAP Signavio Process Governance
Mantra: "Keep competitiveness while reducing complexity." The aspects of this dimension (MCC100, Clean Business Processes):

1. **Establish organizational structure, technical foundation and transformation methodology.** Define roles and responsibilities, for example in a process transformation office; set up an end-to-end toolchain connecting Enterprise Architecture Management, Business Process Management and Application Lifecycle Management; establish guidelines for governing process enhancements.
2. **Set up a prioritized and segmented business process hierarchy,** with end-to-end views (how data flows through the organization) and functional views (activities within each function). Clustering examples are commodity, differentiating and innovating.
3. **Align to-be process design and technical realization.** Use best practices where possible, govern the to-be process, requirements and design approvals centrally, and link design, testing, realization and rollout to the to-be process.

Tools named:

| Tool | Role (MCC100) |
|---|---|
| SAP LeanIX | Visualize the IT application landscape, find obsolete applications, design a target state, plan architecture roadmaps |
| SAP Solution Manager and SAP Cloud ALM | Accelerate time to value and reduce TCO. SAP Cloud ALM is cloud-native, to implement SAP cloud solutions and operate cloud and hybrid landscapes |
| SAP Signavio Process Manager | Modeling platform for business process management |
| SAP Signavio Process Governance | Turns process models into standardized governance workflows |
| SAP Signavio Process Insights and Process Intelligence | Discover improvement and automation potential |
| SAP Activate, SAP Signavio Process Explorer, SAP Signavio Process Collaboration Hub | Methodology, preconfigured best practice processes, collaboration |

## Clean extensions: mantra 'Keep the extensions clean'; extensions are on-stack (Key User type 1, Developer type 2) or side-by-side on SAP BTP (type 3), may only use released APIs, BAdIs and extension points, and cloud-enabled technologies (ABAP Cloud); the Clean Core Level Concept evolves the 3-Tier model into Levels A, B, C and D
Mantra: "Keep the extensions clean." Guiding principles: avoid extensions when possible; create decoupled extensions under strong governance; custom extensions do not break an upgrade and upgrades do not break an extension; separate extensions by using released APIs; use on-stack and side-by-side extensibility; create technical debt only as an informed decision (MCC100, Clean Extensions).

The SAP S/4HANA Cloud extensibility model rests on three principles:

1. Extensions are implemented either internally as **on-stack** extensions (Key User type 1, Developer type 2) or externally as **side-by-side** extensions on SAP BTP (type 3). Types 1 and 2 are used when close coupling is needed, type 3 when looser coupling is acceptable.
2. Extensions may only use released local or remote public APIs, BAdIs and ABAP RESTful Application Programming Model business object extension points.
3. Extensions may only use cloud-enabled and released technologies. The ABAP Cloud Development Model enforces this: only approved object types, ABAP Cloud language and released API usage enforced by syntax check, and ABAP development tools for Eclipse.

**3-Tier model (first generation).** Tier 1: ABAP Cloud and the extensibility model, mandatory for public edition and recommended otherwise. Tier 2: private edition and on-premise, wrapping an unreleased object in a released one, until SAP releases the API (Customer Influence Tool). Tier 3: ABAP Classic, private edition and on-premise only, for when nothing else is feasible.

**Clean Core Level Concept (second generation).** Extensions are classed in four levels by architectural integrity and upgrade safety:

| Level | Meaning |
|---|---|
| A | Only publicly released, stable interfaces with formal stability contracts, based exclusively on ABAP Cloud. The evolution of Tier 1 and the preferred approach |
| B | Uses an unreleased API, such as a BAPI, that SAP deems stable and upgrade-safe, so no wrapper is needed. Also preferred |
| C | Relies on APIs not officially released but needed for legacy scenarios. SAP provides a changelog to spot upgrade risks. Not preferred, but possible if necessary |
| D | Not clean: uses explicitly non-recommended objects or techniques. Highest risk and most likely to create technical debt |

The SAP Application Extension Methodology helps assess extension use cases and define a target solution. Extensions must never duplicate standard functionality (MCC100).

## Clean data: data is configuration, master and transactional; quality facets are accuracy, completeness, consistency, timeliness, validity and uniqueness; data volume must be controlled and personal master data stored only for justifiable purposes; tools named include SAP Master Data Governance and SAP Information Lifecycle Management
Mantra: "Keep the data clean." MCC100 distinguishes three kinds of data (MCC100, Clean Data):

- **Configuration:** defines the organization's structure, for example company code, plants, purchase organizations.
- **Master:** consistent identifiers and attributes of core entities, for example customers, vendors, products, general ledger accounts.
- **Transactional:** derived from transactions, for example sales orders or purchase orders; it has a time dimension, a numerical value and refers to master data.

Quality facets are accuracy, completeness, consistency, timeliness, validity and uniqueness. Data volume has to be controlled to optimize memory and disk, so outdated, unused or redundant data should be purged, and personal master data must be stored only for justifiable purposes.

Tools and methods: SAP Master Data Governance (central hub, single source of truth, validated values, business rules), SAP Information Steward, SAP Datasphere, the SAP One Domain Model (ODM) and the SAP Data and Analytics Advisory Methodology. SAP Information Lifecycle Management addresses privacy by automating archiving and retention and decommissioning legacy systems. Benefits named are "Data To Value", process efficiency, lower TCO, easier data exchange and lower privacy risk (MCC100).

## Clean integrations (landscape): base integrations on standard OData and SOAP APIs, use SAP Integration Suite and SAP Event Mesh, use SAP Application Interface Framework for monitoring, and use RFC and IDoc only if absolutely necessary; SAP Integration Solution Advisory Methodology (ISA-M) supports strategy
The lesson is titled Clean Landscapes, and the mantra it states is "Keep the landscape reliable" (MCC100, Clean Landscapes). The lesson's video transcript repeats the text of the clean data dimension, which looks like a copy error in the course.

- **Standard APIs.** Base integrations on standardized OData and SOAP APIs. The SAP Business Accelerator Hub helps explore APIs and events, and for OData APIs you can try them in an SAP sandbox.
- **SAP Integration Suite.** SAP's integration platform as a service for middleware-based scenarios: routing, mapping and connectivity through adapters.
- **SAP Event Mesh.** A BTP service for asynchronous, event-driven communication, with an event provider, an event consumer and Event Mesh as the glue.
- **Avoid legacy APIs.** RFC and IDoc are common in SAP systems but recommended only if absolutely necessary, because they do not align with reliable and flexible integration.
- **SAP Application Interface Framework.** Lets business users monitor interfaces across technologies such as OData and SOAP, configure alerts and fix business errors such as bad data without IT. Sensitive data can be hidden from them.
- **ISA-M.** The SAP Integration Solution Advisory Methodology offers integration use case patterns, architecture blueprints and best practices, and covers organizational aspects such as an Integration Center of Excellence. SAP Integration Assessment applies it in a tool-based way.

Goals named: upgrade-stable interfaces, proper monitoring and error resolution, and only actively used, well-documented integrations (MCC100).

## Clean operations: mantra 'Keep the operations effective and efficient'; release management is the foundation, housekeeping tasks are established, and SAP Cloud ALM and the clean core dashboard (SAP S/4HANA Cloud Private Edition systems only) support monitoring
Mantra: "Keep the operations effective and efficient." The framework (MCC100, Clean Operations):

- Integrate keeping the core clean into the end-to-end concept for operations. The course suggests IT as owner of the end-to-end view, with integrated monitoring and alerting for data, extensions and other facets, and procedures for event management and escalation.
- **Release management is the foundation.** Public edition updates are pushed to all customers at once. Private edition and SAP S/4HANA (on-premise or hosted) customers are not forced to update, but must strive for the latest release, define a release adoption timeline in governance, and not let the system stay frozen.
- **Housekeeping.** Examples: design background jobs for efficient use of infrastructure, avoid file interfaces for data import and export, and review and adapt user authorizations regularly.
- **Distribution of roles and responsibilities** agreed with SAP, and maintenance within pre-approved contractual maintenance periods.
- **SAP Solution Manager and SAP Cloud ALM** help to detect incidents, analyze root causes, correct problems and automate recurring activities.

**Clean core dashboard (MCC100).** Available through SAP for Me, in Systems & Provisioning, Systems tab, Clean Core Compliance tab. It shows metrics such as software stack version, number of custom code objects, number of business modifications and Tier 1 extensions. It is only available for SAP S/4HANA Cloud Private Edition systems, covers productive systems only, can be shared with partners, needs the authorizations SC_CCCREAD plus INSTDISP (read) or INSTPROD (edit), and collects data mainly through Early Watch Alert, which SAP sets up (MCC100).

*Source note:* SL_RISE419 describes a clean core dashboard that is accessed through SAP Cloud ALM, not SAP for Me (see the dashboard item below). The two courses describe the access path differently, and the corpus does not say whether these are the same product at different times or different views. Check both before giving instructions.

## Best practices for implementation: assess business processes, establish a governance framework, streamline processes, rationalize data, simplify in both greenfield and brownfield, align with SAP's reference architecture, adopt SAP Activate and manage change and user adoption
MCC100's closing lesson gives a starting framework (MCC100, Clean Core Best Practices):

1. **Prepare.** Assess business processes: evaluate existing processes, systems and data structures, engage stakeholders, identify improvement areas. Establish governance: defined roles, top management commitment and funding, IT strategy aligned with company goals. In a greenfield, technical and business transformation happen together; in a brownfield, technical transformation tends to come first and the cleaning of custom code can be lengthy.
2. **Key principles.** Streamline business processes (remove unnecessary steps, fewer deviations, industry best practice). Rationalize data structures (assess quality, cleanse, reduce duplicates, data governance). Simplify in both greenfield and brownfield: minimize customizations and extensions, retire outdated applications, adopt technologies such as AI and RPA. Converting is not incompatible with innovation.
3. **Best practices.** Align with SAP's reference architecture (recommended landscape and modular architectures, industry best practices, SAP Integration Suite). Adopt SAP Activate (agile practices, collaborative workshops and prototyping, preconfigured industry accelerators). Apply tools such as SAP Data Migration Cockpit and the SAP Fiori Custom Code Migration App.
4. **Overcome challenges.** Early, comprehensive change management with users involved in the plan, end user training and support, and continuous improvement based on stakeholder feedback and SAP roadmaps.

## RISE with SAP is SAP's transformation journey to the SAP Business Suite; the RISE with SAP Methodology is built on a clean core strategy and has three core components: a standardized framework, an integrated toolchain and expert guidance
RISE with SAP was traditionally a specific sales package including SAP Cloud ERP Private (SAP S/4HANA Cloud Private Edition). In the context of the SAP Business Suite it focuses broadly on the customer's transformation journey and has become the standard path for existing on-premise SAP ERP customers to adopt the SAP Business Suite, which covers SAP's cloud portfolio including public and private cloud ERP and line-of-business solutions. The SAP Cloud ERP Private Package remains one of the suite's offerings (SL_RISE419, SAP Business Suite).

The RISE with SAP Methodology aids the transition with structured guidance across defined phases, supported by SAP experts and partners. It is "built on a clean core strategy", keeping data streamlined, processes flexible and operations efficient. Its core components are (SL_RISE419, The RISE with SAP Methodology; Key Components):

1. **Standardized framework:** augments the SAP Activate roadmap tasks and deliverables with activities that gather important information before implementation.
2. **Integrated toolchain:** a recommended set of tools to manage the project digitally and increase transparency and collaboration.
3. **Expert guidance:** support from SAP experts and certified partners from the very beginning to ongoing improvements.

Enhancements named: an improved discovery phase with the Digital Discovery Assessment toolkit, broader adoption roadmaps, transformation services for SAP Cloud ERP Private customers, improved onboarding with a clean core success plan, and an enhanced toolchain (SL_RISE419).

## Standardized framework: it augments the SAP Activate roadmap; the Discover phase uses the Digital Discovery Assessment, the Prepare phase has four onboarding calls with the Onboarding Advisor, and through Explore, Realize, Deploy and Run the Project Manager verifies tasks through Clean Core Quality Gates (questionnaires in SAP Cloud ALM); the Clean Core Success Plan holds over 150 recommended tasks
The framework adds activities to SAP Activate to gather key information, onboard the project team and familiarize them with clean core activities (SL_RISE419, Standardized Framework).

| Phase | What happens |
|---|---|
| Discover | The Digital Discovery Assessment captures information that guides the project and shows the customer's planned journey. The onboarding team and customer success managers take part |
| Prepare | SAP's Onboarding Advisor hosts four personalized sessions; initial system provisioning is triggered via SAP for Me |
| Explore, Realize, Deploy, Run | The Project Manager (partner or SAP) verifies task completion through Clean Core Quality Gates |

**The four Prepare calls (SL_RISE419, Prepare Phase):**

1. Call 1, Get Started with SAP: overview of solution capabilities and entitlements of the SAP Cloud ERP Private package, introduction of the customer IT contact ("super admin") and core project team, and system provisioning.
2. Call 2, RISE with SAP Methodology and Clean Core Project: clean core principles and structured support, and setting up the Clean Core Success Plan in SAP Cloud ALM, with tasks across Activate phases in the Clean Core Runbook.
3. Call 3, Complete your Clean Core Quality Gate: helps finish the Quality Gate 1 assessment before submission via SAP Cloud ALM.
4. Call 4, Review your Clean Core Quality Gate Assessment: reviews the Quality Gate report with findings and recommendations.

**Quality Gates.** They are questionnaires managed in SAP Cloud ALM. After submission, SAP's Enterprise Support team gives a feedback report with recommendations based on the answers and on system data analysis, reviewed with the RISE with SAP Enterprise Architect. The onboarding video says analysis typically takes around 10 days and that Quality Gates 2, 3 and 5 follow in later phases (SL_RISE419).

**Clean Core Success Plan.** It guides task completion and deliverables, uses SAP Cloud ALM to manage over 150 recommended clean core tasks, and tracks progress in a runbook. It is described as a living document; the Clean Core Runbook guides stakeholders (SL_RISE419, Explore to Run).

*Source note:* Quality Gate 1 is conducted during Prepare (calls 3 and 4), while the general statement is that Quality Gates are used from Explore through Run. The text does not reconcile the two, so treat gate 1 as the Prepare-phase gate and later gates as the later phases.

## Business phase Value and Architecture Artifacts Handover: presales and sales teams complete artifacts and hand them to the implementation team from Discover to Prepare; deliverables include the Business Capability Map, Application Architecture Overview, Solution Component Diagram, Technical Assessment, Architecture Roadmap, Value Roadmap, RISE Adoption Plan and Executive Proposal, each marked required or recommended
The enhanced SAP Activate roadmap starts with Discover, where the customer's IT architecture, business processes and operations are analyzed to refine the implementation scope and value proposition. Presales and sales teams complete artifacts that document requirements and technical architecture needs and hand them to the implementation team for a seamless transition from Discover to Prepare (SL_RISE419, Business Phase).

The handover deliverables, with the required or recommended marker as read in the course's table order (SL_RISE419, Handover Deliverables):

| Deliverable | Marker |
|---|---|
| RISE with SAP Methodology / Clean Core Strategy | Required |
| Business Strategy Map | Recommended |
| Architecture Principles Catalog | Recommended |
| Value Discovery Approach (Clean Core Maturity Assessment) | Recommended |
| Digital Discovery Assessment | Required |
| Business Capability Map | Required |
| Business Value Flow Diagram | Recommended |
| Application Architecture Overview Diagram | Required |
| Solution Component Diagram | Recommended |
| Software Distribution Diagram | Recommended |
| Product Map | Recommended |
| Bill of Materials (including Solution Sizing) | Required |
| Technical Assessment (Architecture, Cybersecurity, Infrastructure) | Required |
| Architecture Roadmap (Capability, Solution) | Required |
| Value Roadmap | Required |
| RISE Adoption Plan | Required |
| Executive Proposal | Required |

*Source caveat:* the text copy of this table is jumbled, with the markers detached from their rows, so the pairing above follows the order in which the markers appear and should be checked against the original course page before you rely on it.

## Integrated toolchain: SAP LeanIX (landscape analysis), SAP Signavio (process evaluation and modeling), SAP BTP (extensions), Tricentis Test Automation, SAP Enable Now and SAP WalkMe, with SAP Cloud ALM as the digital backbone for project execution and the clean core success plan; SAP Signavio Governance is listed among the process analysis tools
SL_RISE419 states that customers adopting a clean core approach report up to 75% incremental business value and a lower likelihood of incomplete or canceled IT modernization projects, largely thanks to the integrated toolchain. The tools follow the journey (SL_RISE419, The Integrated Toolchain):

| Stage | Tool | Role |
|---|---|---|
| Landscape analysis | SAP LeanIX | Analyzes existing landscape architecture, systems and integrations |
| Process evaluation | SAP Signavio | For SAP ECC or SAP S/4HANA systems, evaluates existing processes. A free one-time data load is offered through SAP Signavio Process Insights, discovery edition. SAP Signavio Process Manager documents custom processes in BPMN |
| Extensions | SAP BTP | Builds and hosts extensions so the core stays clean. Low/no-code (SAP Build Apps, Process Automation) and pro-code (Business Application Studio, ABAP environment, SAP Build Code), with Integration Suite and Connectivity Service |
| Testing | Tricentis Test Automation | Integrated in SAP Cloud ALM, supports manual and automated testing of business processes |
| End-user enablement | SAP Enable Now | Guided simulations of business processes |
| End-user support | SAP WalkMe | Insight into workflow difficulties, personalized guidance and process automation |
| Throughout | SAP Cloud ALM | The digital backbone for project execution, task management, reporting and the clean core success plan; after go-live, operations applications for monitoring |

The overview of transformation tools in the same course lists SAP Signavio Governance among the process analysis and optimization tools, next to Process Insights and Intelligence, Process Manager, the Process Collaboration Hub and others, and lists SAP LeanIX Application Portfolio Management, Architecture and Roadmap Planning, and Technology Risk and Compliance under enterprise architecture (SL_RISE419, The RISE with SAP Methodology).

## Expert guidance and partners: individual sessions, expert meetings on Clean Core Quality Gate reports, the partner ecosystem and enhanced support; the RISE with SAP Competency has three levels (Essential, Advanced, Expert) and Expert-level partners can qualify as RISE with SAP Validated Partners
Expert guidance means collaboration among the customer project team, implementation partners and SAP. Under the methodology customers receive (SL_RISE419, Expert Guidance):

1. **Individual sessions** between the SAP Onboarding Advisor and the core project team (including the partner's Project Manager) to set up project management tools and the roadmap and introduce clean core principles and success plans.
2. **Expert meetings** between an SAP expert and the partner's Project Manager to review Clean Core Quality Gate reports and give tailored recommendations.
3. **Partner ecosystem,** supported by the SAP Competency Framework and findable through the SAP Partner Finder.
4. **Enhanced support,** such as SAP Preferred Success and SAP MaxAttention.

**RISE with SAP Competency.** A mandatory certification path for partners to qualify as RISE with SAP partners, with three levels: Essential, Advanced and Expert. Essential is the baseline for a qualified implementation partner.

**RISE with SAP Validated Partners.** Partners at Expert level that frequently deliver significant transformation projects can qualify. Examples of the course's criteria: Expert status across RISE with SAP, SAP BTP and SAP Business Process Transformation; over five RISE projects with an ACV above EUR 550,000 in the past 24 months; at least 80% of projects completing Clean Core Quality Gates with status Accepted or Conditionally Accepted; and certification targets for project-level staff. A one-time 180-day safeguarding period applies for partners who miss new tier requirements at the effective date (SL_RISE419, RISE with SAP Validated Partners).

## The RISE with SAP Methodology Dashboard (Clean Core Dashboard, accessed through SAP Cloud ALM) has a System View (version insights, tool readiness, upgrade preparation) and an Operations View (daily System Health score and KPIs with up to 30 days of history)
The RISE with SAP Methodology Dashboard, also known as the Clean Core Dashboard, is where customers view and build on their system's adherence to clean core principles. It is accessed through SAP Cloud ALM (SL_RISE419, Dashboard).

- **System View.** Version insights (is the installed SAP S/4HANA product version up to date), tool readiness (are the tools for clean core data collection active, for example SAP EarlyWatch Alerts) and upgrade preparation (assess current extensions to anticipate upgrade risks). Insights cover all SAP S/4HANA systems (development, test, production), helping to identify non-compliant code and keep it from reaching production.
- **Operations View.** Available for RISE with SAP customers, with daily insights and up to 30 days of history on system health KPIs, aligned with the operations dimension. Metrics come from SAP Cloud ALM applications for configured and productive SAP S/4HANA systems, are evaluated daily against thresholds and are aggregated into KPIs and scores. It shows the System Health score for all productive SAP S/4HANA systems (Cloud Private Edition and on-premise), a system-specific view of metric deviations, and jump-ins to SAP Cloud ALM applications. Metrics, thresholds and algorithms are shared so calculation is consistent across all RISE with SAP customers.

The dashboard is a continuous monitoring tool. The Quality Gates, in contrast, are phase-based questionnaires with a feedback report reviewed in expert meetings (SL_RISE419).

## Practice
Build a one-page clean core checklist with one section per dimension (processes, extensions, data, integrations, operations). In each section record the mantra, two principles from the course and the SAP tool or method named for that dimension. Then add a short timeline of the RISE with SAP phases (Discover, Prepare, Explore to Run) that shows where the four onboarding calls and the Clean Core Quality Gates occur.

## Self-check
Can I explain what a clean core is, why it is needed, and how the RISE with SAP Methodology supports it to a project sponsor without notes?
