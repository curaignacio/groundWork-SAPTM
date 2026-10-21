# Session 06 — Planning: Freight Units, Cockpit and Carrier Selection

## Overview
This session follows a transportation demand from the moment it becomes a freight unit to the moment a carrier is ranked for the resulting freight order. You learn how freight unit building rules (FUB rules) decide how many freight units exist and what they look like, how profiles and the transportation cockpit control what is planned and how, how VSR optimization, scheduling and transportation proposals work, and how carrier selection picks and ranks carriers. This is the working core of TM planning. Almost every question a planner asks, such as why there are so many freight units, why an order was delivered late, or why a carrier was chosen, goes back to one of these settings. Where the sources disagree, the text says so.

## The Planning component creates freight documents and transportation units from business documents (for example forwarding orders from which freight units have been built) by assigning capacities, while taking constraints such as requested delivery dates into account; it is integrated with Forwarding Order Management (source of the freight units), Freight Order Management (result of planning), Charge Calculation and Master Data
In planning, freight documents and transportation units are created from business documents, for example forwarding orders from which freight units have been built, by assigning capacities. Constraints such as requested delivery dates are taken into account (H07).

H07 lists four integrations of the Planning component:

| Component | Integration |
|---|---|
| Forwarding Order Management | The system creates freight units from forwarding orders. These freight units form the basis for planning. |
| Freight Order Management | Freight documents and transportation units are the result of planning. |
| Charge Calculation | The system can calculate the transportation charges for freight orders and freight bookings. |
| Master Data | The required master data must be created as a prerequisite for planning. |

H07 names six feature areas of Planning: freight units, unified package building, profiles and settings, manual and automatic planning (sometimes called interactive planning), scheduling, and carrier selection. The rest of this session follows that order. Planning is always based on freight units. S4TM2 gives the business reason: companies can plan manually or automatically, group orders with the same ship-from and ship-to locations, schedule and route multiple orders, choose the carrier, and weigh real-world constraints, costs and penalties.

## A freight unit is a set of goods transported together across the whole transportation chain and the smallest unit that can be transported; it merges items of forwarding orders, order-based and delivery-based transportation requirements, and carries transportation constraints for planning
H07 defines the freight unit as a set of goods that are transported together across the entire transportation chain. It can include transportation constraints for transportation planning. It merges items from forwarding orders, order-based transportation requirements and delivery-based transportation requirements that are to be transported together, and it is the smallest unit that can be transported. The business document data and the FUB rules are the basis for building it.

Practical points from H07 on the freight unit document:
- Freight unit data is taken automatically from the business document, but some of it can be changed. Items can come from different business documents, but each freight unit item is assigned to exactly one business document item.
- The most important settings sit in the freight unit type (see the freight unit type item below).
- The document shows items, locations (one-time locations can be entered at stage level, but changes to existing locations belong in the master data), transportation stages (loading and unloading times, transshipment locations, means of transport), actual quantities and deviations, transportation constraints, document flow, dangerous goods information, status and blocking information, instructions, change documents and CO2 emissions.
- You can split or merge freight unit stages in the freight unit UI and in the transportation cockpit. Splitting a stage inserts a transshipment location manually, and merging stages deletes transshipment locations automatically.
- From a freight unit you can create a freight document, build a house bill of lading or house air waybill, track events with SAP Event Management, and use the change controller to check how the system reacts to changes.

S4TM2 describes the same object as a business object that represents the smallest possible transportation unit. In order consolidation one or more freight units are combined into one freight order.

## The system creates freight units automatically from forwarding orders, order-based and delivery-based transportation requirements (sales orders, purchase orders, deliveries, EWM outbound delivery orders) and JIT calls, and can split and merge quantities according to the freight unit building rule used
H07 (Creation and Editing of Freight Units) says the system automatically creates freight units from:
- forwarding orders;
- order-based transportation requirements, and other order-based business documents such as sales orders or purchase orders from SD or MM, or outbound delivery orders from EWM;
- delivery-based transportation requirements, and other delivery-based business documents such as inbound and outbound deliveries;
- JIT calls.

When it creates freight units, the system can split and merge the product quantities of the requirements according to the FUB rules in use. In practice the planner rarely builds freight units by hand. The standard behavior is that saving the business document triggers the build (see the FUB_AUTO item). H07 mentions that freight units can also be created in the background, but recommends automatic creation.

## Freight unit size affects planning: larger freight units make VSR optimization simpler, smaller ones raise the theoretical optimization potential but make planning harder, so the advice is to aim somewhere in the middle (for example not one 20-ton unit and not 20,000 units of 1 kg for a 20-ton truck)
The size of the freight units created affects planning (H07, Creation and Editing of Freight Units; VSR Optimization):
- The larger the freight units, the simpler the planning activities in VSR optimization.
- Smaller freight units may give a higher theoretical potential for optimization, but in practice VSR planning becomes harder because there are more freight units.
- For the best planning result, aim for a size somewhere in the middle.

H07 gives the example of a truck with a 20-ton capacity that must carry 20 tons of flour in 1 kg packages. Neither extreme is advisable: do not create one freight unit of 20 tons, and do not create 20,000 freight units of 1 kg each. The FUB rule parameters covered below (split quantity, rounding value, item split) are the tools for choosing the size.

## Prerequisites for automatic freight unit building: the automatic freight unit building checkbox in the forwarding order type or in the logistics integration profile, freight unit types defined in Customizing, and freight unit building rules (FUB rules) with assigned freight unit types; incompatibilities are optional
H07 lists the prerequisites for automatic building when business documents are saved:
1. Business documents exist.
2. For forwarding orders, the checkbox for automatic freight unit building is selected in the forwarding order type (Customizing: Define Forwarding Order Types).
3. For order-based documents such as sales orders and purchase orders, the checkbox for automatic freight unit building is selected in the logistics integration profile (Define Logistics Integration Profile for SD, MM, and LE).
4. Freight unit types are defined in Customizing (Planning, Freight Unit, Define Freight Unit Types).
5. FUB rules are defined and freight unit types are assigned to them.
6. Optionally, incompatibilities are defined.

H07 adds optional items. You can extend the standard checks that decide whether a freight unit or transportation unit must be rebuilt (BAdI: Extension of Checks for Triggering FU Building from TRQ). A discrepancy profile can split a freight unit into one with the actual quantity and one with cargo receipt status Missing Cargo. Normalized load consumption quantities (NLQ) and additional normalized quantities (ALQ) can be used as split criteria if they are set up (a condition with condition type /SCMTMS/NLQ_UOM, conversion between the NLQ and ALQ units of measure, and NLQ or ALQ chosen as planning quantity in the FUB rule).

## Automatic creation first groups business document items by hard constraints (source and destination location, carrier, pick-up and delivery dates), business document attributes such as delivery group, packaging information and incompatibilities, then creates one or more freight units from the groups; items with different compatibility groups (package/product/schedule line, container, railcar, trailer) are never put into the same freight unit or transportation unit
**Step 1, grouping.** The system groups all business document items considering (H07, Automatic Creation of Freight Units):
- hard constraints, such as source location and destination location, carrier, and pick-up and delivery dates;
- business document attributes, such as delivery group, and packaging information;
- incompatibilities;
- the FUB rules, taking into account freight units that already exist for these business documents.

**Step 2, creation.** The system then creates one or more freight units from these groups. If you defined a split quantity and selected the item split checkbox, these entries are used when it creates several freight units.

**Hard constraints** are attributes of the predecessor documents, at header or item level, that prevent consolidation and lead to separate freight units. H07 gives a table of the main ones using the sales order as an example, and carrier and Incoterms attributes appear in it. S4611 describes the same grouping for deliveries: items are grouped first by the same source and destination location, pick-up and delivery dates, and the same Incoterm.

**Delivery group.** The item attribute Delivery Group consolidates all items with the same delivery group into one freight unit. Items with different delivery groups can still be consolidated into the same freight unit if the other grouping parameters allow it.

**Compatibility groups.** Main cargo items can have different categories as defined by the shipping type. Items with different categories form a compatibility group and cannot be grouped into one freight unit or transportation unit. The groups are package/product/schedule line, container, railcar and trailer. H07 example: a forwarding order with a container, a package and a railcar as main cargo items has three different compatibility groups, so the system creates three freight units or transportation units.

## The standard process controller strategy for freight unit building is FUB_AUTO, and a forwarding order triggers freight unit creation when it is saved
You can use process controller strategies to create freight units according to your own requirements. SAP delivers the standard strategy FUB_AUTO for freight unit building (H07, S4611). H07 says the system creates freight units, for example, when you save your forwarding order. S4611 states the same for deliveries: freight units are created automatically if transportation relevance is determined for the delivery. The strategy is also named in the FUB rule (Process Controller Strategies).

## The FUB rule defines how freight units are consolidated through the FUB strategy: Consolidate as much as possible (items from different business documents are grouped), Consolidate per item (one freight unit per business document item) and Consolidate per request (compatible parts) (all items of a business document form a freight unit); hard constraints and incompatibilities apply to all three
The FUB rule defines how the system consolidates freight units. H07 (Freight Unit Building Rule) names three FUB strategies:

| FUB strategy | Result |
|---|---|
| Consolidate as much as possible | Items come from different business documents (forwarding orders, and also forwarding quotations, order-based and delivery-based transportation requirements) and the system groups them in freight units. |
| Consolidate per item | The system generates one freight unit per business document item. |
| Consolidate per request (compatible parts) | The system groups all items of a business document to form a freight unit. |

For all three, the system takes hard constraints and incompatibilities into account. The FUB strategy also applies to the creation of transportation units and freight orders. S4TM2 also contains sections on Consolidate Per Item and Consolidate as Much as Possible.

## In the FUB rule the planning quantities (for example gross weight and gross volume) with their units of measure are copied to the freight unit and are the basis for resource capacity checks; the split quantity defines the maximum capacity of a freight unit, a rounding value makes the quantity a multiple of it, and the item split checkbox controls whether items may be split when the split quantity is exceeded; the critical quantity is the primary unit of measure that allows splitting
- **Planning quantities** such as gross weight and gross volume, with units of measure, are entered in the FUB rule. The system copies the units of measure to the freight units it creates, and they are the basis for checking the capacity of resources (H07). S4611 adds that every planning quantity is considered in the capacity checks and is copied to the freight unit.
- **Critical quantity** is the primary unit of measure that allows a line item of a transport requirement to be split into several freight units (S4611).
- **Split quantity** defines the maximum capacity of a freight unit.
- **Rounding value** makes the system calculate the freight unit quantity as a multiple of that value.
- **Item split** is a checkbox that controls whether items may be split if the split quantity is exceeded.
- If the system cannot find the planning unit in the business document, it converts the unit with the values in the product master.

H07 worked examples:
- 5 tons of cement, shipped only in batches of 500 kg. A split quantity of 500 kg gives 10 freight units.
- 5 tons of cement, batches of 0.5 m3, with 0.8 m3 equal to 1 ton in the product master. The system converts 5 tons into 4 m3 and generates 8 freight units.
- Computers at 0.06 m3 each, split quantity 1 m3. 1 divided by 0.06 is 16.67, so at most 16 computers fit. With a rounding value of 3 pieces (three computers per box) the maximum becomes 15, the largest multiple of 3 below 16.67.
- Strategy Consolidate as much as possible, critical quantity Gross Weight, item split not allowed, split quantity 20 tons. Four items weigh 21 tons (5, 5, 5 and 6). The system creates two freight units: items 1 to 3 in freight unit 1 and item 4 in freight unit 2.

H07 also covers a UoM setting for the quantity and alternative quantity. You can allow only dimensionless units (EACH, Pieces, PAL), units of all dimensions, or no unit of measure. With no unit the system uses the units from the predecessor document items, and splitting of freight units is not supported. Quantities with a dimensional unit of measure are ignored by VSR optimization, transportation proposal and load consolidation in the requirement documents. If you create equipment-based freight units, the system fills the planning and split quantities from the Customizing of the equipment.

## The freight unit update strategy of the FUB rule decides whether items may move between freight units on update (Item Swap Allowed is the standard behavior, Item Swap Not Allowed keeps items in their freight unit)
In the FUB rule you define whether items may move from one freight unit to another when freight units are updated (H07). H07 example: a forwarding order has two cargo items, and the system creates one freight unit for each. FU1 (item 1) is planned and FU2 (item 2) is not. If item 1 is deleted from the forwarding order:
- With Item Swap Allowed (standard behavior), item 2 moves to FU1 and FU2 is canceled.
- With Item Swap Not Allowed, item 2 stays in FU2 and FU1 is canceled.

## The document type in the FUB rule controls whether the freight unit builder creates a freight unit, transportation unit or freight order; without a document type the system creates freight units or package, container, railcar and trailer units according to the item category, and equipment type and group in the rule produce equipment-based units
H07 says the FUB rule controls which document type the freight unit builder creates: a freight unit type, a transportation unit type or a freight order type. You enter the document type directly or enter a condition that determines it in the advanced settings. If the system determines a freight order type, it generates freight orders without generating freight units or transportation units.

**Default categories** when no document type is given (H07):

| Item category | Business document category |
|---|---|
| Product / package | Freight unit |
| Package | Package unit (transportation unit with TU category Package) |
| Container | Container unit (TU category Container) |
| Railcar | Railcar unit (TU category Railcar) |
| Trailer | Trailer unit (TU category Trailer) |

The default document types come from Customizing, so a default type must exist in Define Freight Unit Types and Define Transportation Unit Types. To get a freight unit instead of a container unit for container items, enter the freight unit document type in the FUB rule (H07 recommends entering it directly rather than through a condition).

**Equipment-based units.** If you enter an equipment type and group in the FUB rule, the builder creates equipment-based freight units or transportation units. Depending on the equipment type they are of category container, railcar or trailer. Planning quantities, units of measure and split quantities are derived from the Customizing of the equipment, and you can delete or change them in the FUB rule. This allows transportation units or freight orders (shortcut) with multiple items. S4611 adds that with an equipment type in the rule, the capacity of the equipment is considered during freight unit building and the consolidated items are loaded into the equipment.

## Automatic creation of freight orders (shortcut scenario): entering a freight order type, directly or through a condition, as the document type makes the system create freight orders instead of freight units, for example for small orders sent by express delivery or orders that always travel as a full load; in the shortcut the freight unit is skipped and carrier selection can start directly
To get freight orders instead of freight units, enter a freight order type as the document type, or a condition that determines it (shortcut scenario). H07 example of a condition: if the quantity exceeds 20 tons use freight order type 1, otherwise freight unit type 1. H07 gives two typical uses:
- small orders below a defined upper limit that you generally send with an express delivery company;
- orders that always have to be transported as a full load because of their size.

S4TM2 explains the purpose. The short-cut process skips planning activities that are not needed in certain scenarios. For example, if received sales orders already state the required truck size, the freight order can be created directly from the transportation demand. Freight units as separate business documents are omitted where the demand exactly matches the transportation document to be created.

E03 (Compare the Standard and Shortcut Process) shows the difference in the document flow:
- Standard process: freight order 20000102 has freight unit 5106 as predecessor, which was created from outbound delivery 80000163, which refers to sales order 372.
- Shortcut process: after saving sales order 380, the document flow contains only the sales order and freight order 200000106, and the freight unit is skipped.
- In the shortcut, subcontracting is triggered directly when the freight order is created. The Subcontracting tab already shows a carrier ranking and carrier TM-CAR-10 was selected automatically. Means of transport, transportation mode, distance, duration, organizational data and dates were also determined automatically.

## The FUB rule for a business document is determined in order: a condition of type /SCMTMS/FUBR in the business document type (one per type), then a standard FUB rule in the business document type, then default settings; for deliveries S4611 describes the same cascade starting from the logistics integration profile; FUB rules are created in the Create Freight Unit Building Rule app
H07 (Determination of Freight Unit Building Rules) gives the order the system uses to find the FUB rule for a business document item:
1. It checks whether a condition (condition type /SCMTMS/FUBR) is specified in the business document type, for example the forwarding order type. There can be only one condition per business document type.
2. If there is no condition, or the condition returns no result, it checks whether a standard FUB rule is specified in the business document type.
3. If there is none, it uses default settings.

You can see which FUB rule the system used in the freight unit. S4611 describes the same three-step cascade for deliveries, starting from the logistics integration profile: first a condition in the profile, then a FUB rule maintained in the profile, then standard settings. To create FUB rules, open the Create Freight Unit Building Rule app from the launchpad (H07).

## The freight unit type (four-character identifier, unique across freight order, freight booking, transportation unit and freight unit types) carries the freight unit settings: change controller settings, creation, save and deletion strategies, planning settings (distance/duration determination, rule or condition for pick-up and delivery windows), default units of measure, organizational unit determination, track changes and output options; it also defines whether a freight unit is deleted or canceled
S4611 (Creating Freight Units): the freight unit type has a four-character identifier. Freight order, freight booking, transportation unit and freight unit types must be unique across these four business document types. Within the freight unit type you define whether a freight unit can be deleted or must be canceled. The main Customizing settings in the basic scenario:
- **Change controller settings:** how TM responds to document changes, for example quantity changes.
- **Additional strategies:** creation strategy (tasks when creating a freight unit), save strategy (tasks when saving) and deletion strategy (tasks when deleting or canceling).
- **Planning settings:** distance/duration determination, and the rule or condition for pick-up and delivery window determination.
- **Default units of measure:** weight and volume.
- **Organizational unit determination:** a condition, the Consider Organizational Unit of User checkbox, and default organizational units (execution organization, purchasing organization, execution group, purchase group) used if none of the earlier criteria succeeded.
- **Basic settings:** the Track Changes checkbox.
- **Output options:** output profile, additional output profile, text type and text schema.

## Handling units and freight units: all product items packed in one handling unit stay in one freight unit, so parts of a handling unit are never assigned to different freight orders; one freight unit can hold several handling units
S4611: when a delivery includes handling unit items, freight units are adjusted accordingly. All product items packed into one handling unit are in one freight unit and are not split across several freight units. This ensures that parts of a handling unit are never assigned to different freight orders during planning. If separate freight units were first built per product and the products are then consolidated into one handling unit, the separate freight units are merged into one. The relationship is not necessarily one to one: one freight unit can contain several handling units, and building can be set up to create one freight unit per handling unit.

## Conditions make TM configuration flexible: they can determine FUB rules, freight unit types, organizational units, change controller strategies and pick-up/delivery time windows; their origin is Direct Business Object Access, a BRFplus decision table or a BRFplus expression, and a decision table is processed from top to bottom until the first matching row
S4611 (Defining Conditions): conditions are a configuration means to maintain project-specific requirements flexibly. They can determine FUB rules, freight unit types, organizational units, change controller strategies, and pick-up and delivery time windows.

A condition works as input, decision and output. The input comes from a data access definition (for example, whether the goods are dangerous). The decision is based on the input and the condition type. The output is a result that depends on the condition type, for example a specific FUB rule. Condition types seen in this session are /SCMTMS/FUBR (FUB rule), /SCMTMS/TOR_TIMEWIND (pick-up and delivery time windows) and /SCMTMS/FU_PNLT_COST (earliness and lateness costs) (H07, S4TM2).

Three origins exist:
- **Direct Business Object Access** returns the value found by the data access definition directly, without evaluating it.
- **BRFplus Decision Table** evaluates the input in a table that you maintain from the condition UI.
- **BRFplus Expression** is maintained as nested if/then statements.

The system generates a BRFplus decision table from input and output values and processes it from top to bottom. At the first row whose input values match the current input, it copies the output values and uses them in the calling area.

## Freight units can be split and merged manually (for example in the transportation cockpit or the freight unit table) with Split/Merge; source, destination, Incoterms and dates/times must match, partial quantities cannot be split off for package or container items, Adopt Stops copies stops and planning results, and Fix Source/Target Freight Unit protects the result from automatic rebuilding
H07 (Manual Splitting and Merging of Freight Units): you can split or merge freight units the system created, for example in the freight unit UI, the transportation cockpit or the freight unit table in the planning overview, by choosing Split/Merge.
- When splitting, the target freight unit takes over the split-off items (or partial quantities) and is created in the split. When merging, the target is the existing freight unit that takes over the items.
- **Adopt Stops** copies the stops from the existing freight unit, and also the planning results (routing and assignments to freight orders) if it was already planned.
- **Fix Source Freight Unit** or **Fix Target Freight Unit** prevents automatic freight unit creation from changing the freight units after a manual split or merge.
- For product items you can split off or merge partial quantities by entering the quantity. Package items and container items can be split or merged only if they have no subitems, and partial quantities of them cannot be split off.
- Empty freight units created in a split are not deleted at once, and are deleted on save if still empty. A freight unit can be split several times. For example, 100 tons with a split quantity of 10 tons and 5 item splits gives 5 freight units of 10 tons, and the original keeps 50 tons.
- Manual splitting remains possible after execution has started (cargo receipt status On Hand), but the forwarding order is no longer adjusted.

**Mandatory hard checks:** source location, destination location, Incoterms and dates/times must match between source and target freight unit, and incompatibilities flagged in the Manual Violation field as not to be violated during manual planning must hold.

## Unified package building during freight unit building can create freight units, freight orders or package units with a full package and product hierarchy, or only a rough estimate of the number of packages, and requires a unified package building profile
H07 (FUB rule, Unified Package Building): on the Advanced Settings tab you can specify whether, during freight unit building, the system creates freight units, freight orders or package units with a complete hierarchy of package and product items from the order documents. It also determines the exact position of each product in the package, shown in the load plan. Alternatively, the system calculates only a rough estimation of the number of packages, shown in the header data of the freight unit (General Data tab) and usable by the VSR optimizer.

- A unified package building profile is a prerequisite. For exact product positions, Detailed Mixed Package Building must be selected as the mixed package building mode in that profile.
- What is created depends on the document type in the FUB rule. For a full hierarchy you can choose a type of category FU, FO or TU. For a TU type the category must be Package, and H07 recommends a TU type with category Package instead of an FU type.
- You can set a maximum number of top-level packages per document, and request a separate document for unpackaged items.
- If the package builder is the engine, the checkbox Only Full Packages in PB Result must be selected in the profile. The system then builds full packages and the remaining quantities stay unpackaged.

*What the material does not establish:* this session does not cover the internal logic of the package builder or the product-master settings for packaging. H07 treats those in separate sections.

## The planning process turns freight units into freight orders by order consolidation (grouping orders with the same ship-from and ship-to locations), routing and scheduling, and carrier selection; planning can be done in three steps (transportation proposal, VSR to create a freight order, carrier selection), two steps, or one step (one-step optimization determines route, creates the freight order and selects the carrier); it can be manual or automatic, interactive or in the background, always based on planning strategies
S4TM2 (Transportation Planning) describes the process.
- **Order consolidation:** grouping orders with the same ship-from and ship-to locations to get more efficient shipment quantities. One or more freight units are combined into one freight order.
- **Routing and scheduling:** S4TM2 uses a figure with freight unit X. First it is routed (for example by a transportation proposal), and three stages result: a U.S. road pickup, an ocean voyage and an EU road delivery. Up to a point these stages are planned independently because different local planners may be responsible. A freight order is created per stage, and carriers are then selected by specific criteria.
- **Three steps:** (1) determine routing (transportation proposal), (2) vehicle scheduling and routing to create a freight order, (3) carrier selection.
- **Two steps:** (1) VSR to create a freight order, (2) carrier selection.
- **One step:** one-step optimization determines the route and plan, creates a freight order and selects a carrier.
- Planning can be manual or automatic, and interactive or in the background. For interactive planning the central UI is the transportation cockpit. Both manual and automatic planning follow planning strategies, for example one-step optimization.

## Profiles and settings group planning-relevant parameters and are Customizing that can be transported: the selection profile (time-related, geographical and additional selection attributes; defines which freight units or freight orders and bookings are considered, up to a maximum number) and the planning profile (planning horizon, subprofile assignments such as capacity selection, manual planning, scheduling, optimizer, constraints and costs, incompatibility, carrier selection, load planning, unified package building and transportation cockpit settings); a standard planning profile is used when none is found; they are created in the Create Selection Profile and Create Planning Profile apps
H07 (Profiles and Settings): profiles and settings group planning-relevant settings, such as capacities and planning costs. They make it easier to start manual and automatic planning and are a prerequisite for VSR optimization in the background. Each subprofile has its own ID, is defined once and can be assigned to several profiles. It is Customizing that you can transport with a transport request. H07 recommends activating automatic change recording (transaction SCC4) so that profile changes are always assigned to a transport request, and names authorization objects such as T_PRF_CR, T_PRFOPPID, T_PRFSELID, T_PRFINCID, T_FUBRID and T_COND.

**Selection profile** (H07, S4TM2). It is a user-specific grouping of business documents (forwarding orders, freight units, freight orders) considered in planning. It is used in manual planning, VSR optimization, planning in the background and carrier selection. It defines which documents are considered and the maximum number of documents. Its attributes:
- Time-related selection attributes: the demand horizon.
- Geographical selection attributes: source and destination locations. S4TM2 says the profile has four sections, source locations, source transportation zones, destination locations and destination transportation zones, each with an inclusive or exclusive set of values. It notes that planning responsibility is often allocated by geography, so this lets a team see only the freight units or freight orders it is responsible for.
- Additional selection attributes: additional filters for database queries on documents of forwarding order management or freight order management. The geographical and additional criteria affect performance (H07).

Which documents are selected depends on where the profile is used. As a selection profile for freight units, the system selects freight units. As a selection for freight orders and freight bookings, it selects the existing freight orders and bookings considered in planning. Apps: Create Selection Profile, Edit Selection Profile, Create Additional Selection Attributes.

**Planning profile** (H07, S4TM2). It is a user-specific grouping of parameters used in manual planning, load planning and VSR optimization (interactive and background). S4TM2 says a planning profile must be specified for a background optimizer run and for interactive planning in the cockpit. It holds:
- the planning horizon;
- subprofile assignments: capacity selection settings, capacity availability settings, capacity document creation settings, manual planning settings, scheduling settings, optimizer settings, constraints and costs settings, incompatibility settings, carrier selection settings, load planning settings, unified package building settings and transportation cockpit settings. For each assigned subprofile except selection profiles and carrier selection settings, you can specify whether the profile data may be changed during planning sessions;
- parallel processing profiles, planning strategies, and the handling of empty stages.

S4TM2 adds the default business document type (default type from Customizing, a type set directly in the profile, or a condition) and check settings. If the system finds no planning profile, it uses the standard profile (H07). Apps: Create Planning Profile and the apps for subprofiles. In E03 the planning profile PLAN_S48600 sets the planning horizon to 60 days into the future, and the Capacity Selection Settings define which vehicle resources, vehicle types, drivers, container resources and types, and schedules are available.

*What the material does not establish:* it does not give a complete field list for each subprofile in one place. H07 and S4TM2 describe them in separate sections, only partly read for this session.

## The demand horizon (the period of demands considered, for pick-up and for delivery) is absolute (start and end date and time) or relative (start = current date + offset, end = start + duration, optionally with a factory calendar), while the planning horizon is the period in which transportation activities can be scheduled
**Demand horizon** (H07): the period containing all demands considered in planning. It is defined in the time-related selection attributes of the selection profile, separately for pick-up and for delivery. The system selects all freight units and freight orders whose pick-up or delivery date/time lies within the relevant horizon.
- **Absolute:** start and end date and time are fixed.
- **Relative:** a duration from the current date. Start = current date + defined offset (days plus hours and minutes). End = start + defined duration (days plus hours and minutes). With a factory calendar, non-working days are considered when calculating the start, so the horizon starts on a working day. You can simulate it with a reference date. A relative horizon can also have a fixed start time or a fixed end time.

**Planning horizon** (H07): the period in which transportation activities (for example loading, unloading, transport) can be scheduled. It is defined in the planning profile, absolute or relative, with the same offset and duration logic, optional rounding to full days and a time zone. H07 recommends always defining it in the future, otherwise documents in the past are considered, which can cause performance problems. To correct past documents, define a separate planning profile with its own horizon. S4TM2 states the planning horizon defines the horizon in which new freight documents can be created by planning. In E03 the selection profile SEL-S4TM1 selects freight units with delivery dates up to 60 days ahead, while the pick-up date is not relevant.

## The transportation cockpit is the main user interface for planning: it starts with Profile and Layout Sets (a selection profile, a planning profile and a page layout, one set can be the default) or with the Selection Criteria screen (saved searches), shows requirement lists, capacity lists and order lists, and supports planning with lists and hierarchies, on a map and in a Gantt chart; PLS Management defines which users work with which sets
S4TM2: the cockpit is the main UI for planning, including freight order creation. It shows transportation requirement lists (freight units), capacity lists (vehicle resources and schedules), order lists and order details.

**Three start elements.** For planning in the cockpit you typically need (E03, S4TM2):
- a **selection profile**, which selects the freight unit (stages) relevant to planning, that is what is planned;
- a **planning profile**, which defines how planning is executed;
- a **page layout**, which defines how information is presented. It defines the buttons, functions, levels and hierarchies shown in the cockpit, carrier selection and delivery creation UIs.

S4TM2 also mentions a capacity selection profile that restricts planning to the transportation resources that can be used. A combination of selection profile, planning profile and page layout can be assigned to a **profile and layout set (PLS)**, so that a planning scenario is always shown in its layout. One PLS can be the default. Layouts can be switched on the fly, for example when a multistep process has different needs in each step. S4TM2 examples of sets: next-day planner, dispatcher for today, air and ocean planner, carrier selection, and an area planner per country or region.

**Two start screens** (H07, E03):
- **Profile and Layout Sets.** Users pick a PLS an administrator assigned to them. The PLS management apps (PLS Management for Transportation Cockpit, for Carrier Selection, for Delivery Creation) let an administrator create PLSs centrally and assign users, for example the usual planner and a stand-in. For the cockpit H07 recommends a selection profile for freight units plus a planning profile that already contains a selection profile for freight orders and freight bookings. Authorization object T_PL_SETS controls who may create, edit and assign PLSs. In the cockpit, Change Planning Settings temporarily changes planning and load planning settings, and the changes are discarded when you leave or change the profile selection.
- **Selection Criteria.** Select the planning data for freight unit stages, vehicle types, freight orders and so on, by criteria such as source location, destination location and vehicle type, without configuring selection profiles. You can save searches (E03 uses PLAN_00) privately or globally and load them via Saved Searches. A planning profile is recommended, because otherwise default values are used. Switch Start Screen toggles between the two.

**Display forms** (S4TM2, E03, H07): lists and hierarchies (hierarchical views for freight orders, freight bookings and transportation units help filtering and rescheduling), a map (drag and drop, context menu, route display, proximity search), and a Gantt chart that shows availability of vehicle resources, handling resources and drivers. The cockpit has up to 6 views in a layout, the standard layout has four quadrants, and it can run in multiple windows on up to three screens (S4TM2). E03 shows layouts TCLAYOUT_SIMPLE, TCLAYOUT_VISUAL (Gantt chart) and LAYOUT-00 (map).

## Cockpit tasks: manual planning, creation of transportation proposals, VSR optimization, load planning, carrier selection, triggering of tendering, delivery proposals and freight bookings; page layouts define buttons, functions, levels and hierarchies and can be switched on the fly; views can be saved, shared and given conditional formatting
S4TM2 lists the cockpit tasks: manual planning, creation of transportation proposals, VSR optimization, load planning, carrier selection, triggering of a tendering process, creation of delivery proposals, and creation of freight bookings.

Page layouts define which buttons, functions, levels and hierarchies appear, so elements can be hidden or shown depending on user needs. S4TM2 gives the example of a planner of liquids in tank trucks who needs the volume of product, while for liquids in barrels on pallets the planner needs the pallet count. E03 shows Switch Page Layout and how to customize each screen area with Settings: columns, sorting and grouping, filters, aggregation and conditional formatting. In the E03 example, freight units with gross weight above 1500 kg are red, planned freight units green and unplanned ones yellow. Several views can be saved, shared with all or a specific group of users, and one can be the default. The E03 map view can show objects as arrows or icons and supports planning by drag and drop.

## Manual planning assigns requirement documents (freight units) to capacities (vehicle resources, schedules, equipment types) so that the system creates capacity documents such as freight orders; planning strategies VSRI_DEF (manual planning) and VSRI_SCH (manual planning with subsequent scheduling) are set in the planning profile, and the tools only support the planner, who remains responsible for consistent results
H07 (Manual Planning): to create a transportation plan you assign requirement documents, for example freight units, to capacities, for example vehicle resources. The system creates capacity documents, for example freight orders, which you process further (assign drivers, do load planning). If you assign freight units to a container, a container unit is created that you can assign to a freight booking.

Planning strategies determine the steps and their order, and you specify them in the planning profile. H07 names VSRI_DEF for manual planning and VSRI_SCH for manual planning with subsequent scheduling. S4TM2 lists VSRI_DEF, VSS_EMBED (embedded, which does not consider scheduling constraints defined in Customizing), VSRI_SCH and VSRI_1STEP (manual planning with carrier selection). H07 (Planning Profile) names VSRI_SCH as the standard strategy for manual planning.

Options (H07, S4TM2): create capacity documents directly from freight units, assign freight units to existing capacity documents or remove them, create blank capacity documents from resources or schedules, create documents from requirement groups, plan on equipment types, and use drag and drop (dragging an unplanned freight unit stage to a resource, or a resource to a stage, creates a freight order). H07 states that the tools and checks are only support, and the planner remains responsible for consistent results.

E03 (Perform Interactive Planning): freight unit 5116 is assigned to truck type TM-LORRY with Assign Selected Items, which creates a freight order with temporary number $1. More freight units can be assigned to an existing temporary order. In the overview you check vehicle, location sequence, activities and planned dates.

## Planning constraints can be physical (vehicle capacity, handling capabilities) or process-related (for example a maximum of 25 drops per day), including pick-up and delivery time windows, loading and unloading durations, maximum distance, duration or stopovers; VSR optimization always adheres to hard constraints and models soft constraints with penalty costs, with window constraints none, hard (acceptable dates), soft (requested dates) or both
S4TM2 (Planning Constraints): constraints can have physical root causes, such as vehicle capacity or handling capabilities for loading and unloading, or process-related ones, for example a delivery tour with a maximum of 25 drops per day. Listed assets and facilities: vehicle capacity, vehicle combinations (truck and trailer), compartments, depot locations, handling resources and opening hours, schedules, and incompatibilities. Listed process and execution constraints: decreasing capacities, maximum number of transshipment locations, maximum limits on distance, duration or stopovers, pick-up and delivery time windows, minimum and maximum storage time at a hub, loading and unloading durations, and scheduling constraints.

**Hard and soft.** VSR optimization always adheres to hard constraints. Soft constraints are modeled with penalty costs, for example lateness costs that are part of the total costs (H07, S4TM2). By weighting the penalty costs you influence how strongly soft constraints are respected. H07 notes a higher weighting of lateness costs can lead to longer distances to meet requested dates. H07 example: vehicle loading capacity is a hard constraint, requested dates/times are soft, so a freight unit can be scheduled after the requested delivery date and delay costs arise.

**Windows.** Forwarding orders, SAP ERP orders and deliveries have a single day and time for pick-up and delivery. TM planning uses time windows for flexibility (S4TM2). Window constraints can be none, hard (acceptable dates), soft (requested dates), or hard and soft. You also define tolerances: maximum earliness, maximum delay, delay without penalty costs and earliness without penalty costs. The condition for the windows is specified in the freight unit type (condition type /SCMTMS/TOR_TIMEWIND), and earliness and lateness costs use condition type /SCMTMS/FU_PNLT_COST. S4TM2 penalty logic: premature pick-up costs apply between the earliest pick-up time (hard) and the allowed premature pick-up (soft). Delayed pick-up costs apply between the allowed late pick-up (soft) and the latest pick-up (hard). Delivery works the same way.

## VSR optimization assigns freight units to capacities cost-effectively while adhering to constraints and determines delivery sequence and transportation dates; it minimizes a weighted sum of non-delivery, earliness and lateness penalties, fixed, travel-dependent, load-dependent and sustainability costs; standard strategies are VSR_DEF and VSR_1STEP (which can run carrier selection right after optimization); it is started with Optimizer Planning or in the background with report /SCMTMS/PLN_OPT
**Purpose** (H07): assign freight units to capacities, such as vehicle resources, cost-effectively while adhering to constraints, and determine the sequence of deliveries and the transportation dates/times. S4TM2 lists the decisions: per freight unit, transport or not; per transported freight unit, the path through the network; per stage, the capacity; per capacity, the relative order of activities (routing) and the start time of each activity (scheduling).

**How it works** (H07, S4TM2): it inserts freight units step by step into the plan, then modifies these initial solutions, for example by loading a freight unit on another capacity or changing the delivery sequence, to minimize total costs within the constraints. At the end it returns the best solution found. S4TM2 names the method as evolutionary local search. If the cost for non-delivery of a freight unit is lower than the cost of transporting it, the freight unit is not delivered (H07). Existing freight orders from an earlier run or manual planning serve as an initial solution if they use transportation lanes, lie in selected capacities and do not violate incompatibilities.

**Total costs** (S4TM2) are a weighted sum of non-delivery/execution penalty per freight unit, earliness and lateness penalty per freight unit, fixed cost per vehicle or tour, travel-dependent cost (distance and duration), load-dependent cost, and sustainability costs such as CO2 emissions. H07 lists the same as freight unit-dependent costs (earliness, lateness, non-delivery) and capacity-related costs (fixed costs per freight order, fixed costs per vehicle resource or equipment type, load costs, variable costs per time, distance and intermediate stops, transported quantity per distance, CO2). These costs are defined in the constraints and costs settings. H07 and S4TM2 stress they are not real costs, but a way to steer the result. For example, higher lateness costs than earliness costs make early delivery the preferred solution.

**Data and context.** The optimization data is all selected freight units (planned and unplanned) in the planning horizon, the data from context determination, and all capacities matching the capacity selection settings, plus the transportation lanes between all relevant locations. H07 states a vehicle needs a direct transportation lane from A to B. Lanes A to C and C to B are not combined. Context determination automatically brings in indirectly linked freight orders, freight units and transportation units, which the optimizer treats as information only, and it cannot be switched off.

**Strategies.** SAP delivers VSR_DEF and VSR_1STEP. VSR_1STEP can control whether carrier selection runs immediately after optimization (H07, S4TM2). For one-step planning, carrier selection settings must also be assigned to the planning profile (H07).

**Starting it.** In the cockpit, choose Optimizer Planning, for all entries or selected entries. For the background (H07), call report /SCMTMS/PLN_OPT, choose a planning profile and a requirements selection profile (and a freight order selection profile if needed), and run it in the background. Prerequisites include RCCF destinations for the optimization server, a planning profile with optimizer settings, constraints and costs settings and capacity selection settings, and transportation lanes. The results are explained in the explanation tool (S4TM2: user parameter /SCMTMS/EXP set to X logs optimizer data for interactive runs).

## Transportation proposals show alternative routes, means of transport and times for a freight unit (entry points: the forwarding order actual route and the transportation cockpit); the result can save only the route (freight unit stages) or the route and freight documents
S4TM2: a transportation proposal defines how a freight unit can be transported through the network (locations, transshipment locations, zones, lanes, vehicle resources, schedules, bookings). For a freight unit the system determines a set of alternatives. They have two purposes:
- to make options transparent. Proposals can differ in routing, means of transport and time, and each affects cost;
- to create stages upfront, for example choosing ocean transport because the order was placed well in advance. No freight orders are created, only stage information is stored, so different planners can plan the stages at different times.

**Entry points:** Forwarding Order, Stages, Actual Route, Define Route; and Transportation Cockpit, select freight unit(s), Transportation Proposal.

**Saving:** Save Route Only saves only the freight unit stages. Save Route and Freight Documents saves stages and freight documents. Not Defined lets you decide case by case.

**Preferences** (S4TM2): route variation, carrier variation, departure date variation, time relevance and cost variance, each weighted none, low, medium or high. Features include implicit transshipment locations defined by schedules and freight bookings, and rough planning of pre-leg and subsequent leg.

E03 example: after checking transshipment location assignments (TMCD-HANNOVER for zone DE-NRW, TMCD-FRANKFURT for TMAT_ZONE00), proposals for freight unit 5116 give a direct connection from SP_1010 to TMAT00-01 and a two-stage route via TMCD-FRANKFURT. Carrier TM-CAR-10 was proposed with estimated charges of 231,80 EUR against 256,54 EUR for TM-CAR-11.

## Scheduling determines start and end times for activities such as departure and arrival of a freight order, pick-up and delivery of freight units and coupling of trailers; it runs forward (first activity scheduled first) or backward (last activity first), the default strategy is Scheduling (Embedded) VSS_EMBED, and it considers time windows, loading and unloading durations, appointments, location sequence, existing freight orders, driver and vehicle availability and calendars
H07 (Scheduling): scheduling determines start and end times for dates and times such as departure and arrival of a freight order, pick-up and delivery of assigned freight units, or coupling and uncoupling of trailers. It can be triggered for one or several freight orders and is based on the planning profile. For schedule-based freight orders and bookings, loading and unloading durations are not considered.

**Direction.**
- Forward: the system defines start and end time of the first activity first, then all succeeding ones. It is the default.
- Backward: the system defines the last activity first, then all preceding ones.
In both cases it tries to minimize idle time. H07 and S4TM2 give the same example: with a nearly full depot (95 m3 of 100 m3) you move goods out as soon as possible, so you use forward scheduling. With goods that take little depot space (5 m3) you stick to the delivery window as closely as possible, so you use backward scheduling. In the freight order UI you can choose scheduling based on the planning profile (forward if no profile), forward, or backward. Execution-based scheduling fixes activities already reported and ignores everything before the last executed activity.

**Constraints considered** (H07, S4TM2): time windows for loading and unloading, loading and unloading durations, appointments of the freight order, location sequence, existing freight orders on resources (not for multiresources), fixed departure time of a stage, coupling and uncoupling durations, absences and non-working times of drivers, downtimes of vehicle resources, calendars of handling resources, and goods wait times at transshipment locations. H07 recommends driving and working constraint profiles instead of scheduling constraints, because rests are scheduled without interruption and can be displayed.

**Prerequisites** in the planning profile (H07): a planning horizon, loading and unloading durations (0 if missing), coupling and uncoupling durations (0 if missing), whether requested or acceptable dates are used, scheduling direction (forward by default), and a scheduling strategy.

**Strategy, source difference.** H07 states that Scheduling (Embedded) VSS_EMBED is the default scheduling strategy (no RCCF call, does not take into account scheduling constraints defined in Customizing), and that VSS_DEF is Scheduling (Optimizer Server). H07 (Planning Profile) also lists VSS_EMBED as the standard scheduling strategy. S4TM2 says in one place that the standard strategy is VSS_DEF, and a few lines later that VSS_EMBED (since SAP S/4HANA 2020) is the default scheduling strategy. The sources differ, so check the system before relying on either.

**Starting scheduling:** the Scheduling button in the cockpit areas, in the Gantt chart (including drag and drop), or in the freight order UI. With user parameter /SCMTMS/SCH_FORCE active, entering a departure date and pressing Enter starts it. E03 shows a result: forward scheduling put a freight order from Friday afternoon to Monday morning. After Change Planning Settings, Scheduling Settings, Backward, and Scheduling again, the order ran within Monday. The Explain Scheduling Result app analyzes the outcome.

## Carrier selection assigns a carrier to subcontractable business documents manually or automatically, aiming at the lowest cost under constraints; it requires transportation lanes with carriers and means of transport and carrier selection settings (Create Carrier Selection Settings app) that define regular selection, tendering or direct shipment options; if no carrier is available none is assigned
H07 (Carrier Selection): carrier selection assigns a suitable carrier to subcontractable business documents (for example freight orders or bookings), manually or automatically, aiming at the lowest cost under constraints. S4TM2 adds that the carrier is the business partner the freight order is subcontracted to, which can differ from the executing carrier.

**Prerequisites** (H07): transportation lanes in the master data with means of transport and carriers (carrier profiles optional); one or more optimization options (strategies, continuous move, business share, check against transportation allocations); business document types set as relevant for subcontracting in Customizing; and the carrier selection settings, which define the process (regular carrier selection, tendering, determination of direct shipment options).

**Manual:** you assign the carrier yourself. With a configured check against transportation allocations, warnings appear when relevant allocations have no capacity or would be violated.
**Automatic:** a separate optimization finds the most cost-effective carrier for all selected documents using the chosen options. If no carriers are available, none is assigned. H07 notes automatic carrier selection does not support consignment orders.

**Carrier selection settings** (S4TM2, Create Carrier Selection Settings app) control the process. The most important fields: Check Incompatibilities and incompatibility settings, Type of Carrier Selection Settings (general, for tendering, for direct shipment), Allocation Usage, BS Usage, Strategy, Carrier Cost Origin, Planning Strategy, Optimizer Runtime, Consider Manual Assignments as Fixed, Action for Manual Rankings, Transportation Charge Interpretation, Action after Carrier Selection Run (assign the highest ranking carrier or do nothing), Consider Hierarchy and Continuous Move Type. Configuring the settings for automatic carrier selection is mandatory.

**Where to start it** (S4TM2, H07): the Carrier Selection app (first with PLS selection), the freight order UI or any freight order worklist, the cockpit, or as part of a planning strategy that includes carrier selection (method VSR_TSPS in strategy VSR_1STEP). In the background, S4TM2 names report /SCMTMS/PLN_OPT with a planning strategy including carrier selection, report /SCMTMS/TSPS_OPT_BGD, and strategy Carr_Sel as creation strategy in the freight order type. H07 names /SCMTMS/TSPS_OPT_BGD for background carrier selection. **Source difference:** S4TM2 names both /SCMTMS/PLN_OPT (with a strategy that includes carrier selection) and /SCMTMS/TSPS_OPT_BGD as ways to start it, while H07 names only /SCMTMS/TSPS_OPT_BGD for carrier selection and /SCMTMS/PLN_OPT for VSR optimization. They describe different routes, but note the difference when you decide which report to schedule.

For freight bookings, S4TM2 states carrier selection considers only transportation allocations, no business shares or continuous moves.

## Automatic carrier selection optimizes with strategies Priority and Costs (internal costs from the transportation lane or carrier profile are used only for weighting, or charges from charge management), Continuous Move (simple continuous move or round trip with discounts), Business Share (target shares with tolerances and penalty costs) and a check against transportation allocations, which also applies to manual selection; SAP delivers strategy TSPS_DEF, and the result is a carrier ranking list
Strategies are optimization options used in automatic selection. They are defined either in the transportation lane or in the carrier selection settings, and lane-level strategies allow different settings in one run (H07, S4TM2). The optimizer creates a carrier ranking list (S4TM2). Supported options: cost and priority, business share, transportation allocation, continuous move.

| Option | What it does | Where configured |
|---|---|---|
| Priority | Chooses the carrier with the highest priority from the transportation lane, within the restrictions. | Priorities per carrier in the transportation lane |
| Costs | Chooses the lowest total costs, using internal costs or charges calculated in charge management. | Strategy in the transportation lane or the carrier selection settings; internal costs in the transportation lane or carrier profile; charge management for charges |
| Continuous Move | Combines subcontractable documents into continuous moves to cut costs, as a simple continuous move or a round trip (exactly two documents with the first source equal to the second destination). | Continuous Move checkbox in the carrier profile, Contin. Move Type in the transportation lane or carrier selection settings, windows, maximum distance and discount per carrier |
| Business Share | Targets shares of business per carrier with tolerances and penalty costs. | Create Business Shares app, plus lane and carrier selection settings |
| Transportation allocation | Checks carrier capacity quantities for a trade lane. Applies to automatic and manual selection. | Allocation usage in the carrier selection settings (use, not use, or decide per lane) |

**Internal costs.** H07: internal costs are transportation costs (per business document, weight or volume) and carrier costs (per kilometer or mile), defined in the transportation lane, or in the carrier profile if the lane has none. They are not real costs, only used for weighting (S4TM2 repeats this). Costs can alternatively come from charge management (the carrier selection settings must say so). S4TM2 notes the strategy can be cost, priority, cost plus priority, or cost times priority, and in its example Cost+Priority ranks carrier 1 first while Cost*Priority ranks carrier 2 first.

**Continuous move** (H07): requires both documents to be available for the carrier, the arrival of the first in the departure window of the second and the reverse, and the distance between the first destination and second source within the smaller maximum distance of the carrier. Discounts are deducted from the costs per document. H07 example: FRT1 1000 less 10 percent gives 900, FRT2 2000 less 20 percent gives 1600, total 2500 for carrier A, against 2750 for carrier B at 950 and 1800, so carrier A wins.

**Business share** (H07): penalty costs apply when the share is above or below the target plus or minus tolerance. They are not real costs. H07 recommends defining penalty costs, and always tolerances. Example: carrier A gets 50 percent of all freight orders from source DC_FRANKFURT by road in June 2010. Business shares and transportation allocations are each valid for exactly one trade lane.

**Transportation allocations** (S4TM2): defined capacities per carrier and trade lane during a validity period, for dimensions such as volume, weight and 20-foot equivalent units, in time buckets. Matching freight documents consume the buckets, and consumption is determined asynchronously.

**Standard strategy.** SAP delivers TSPS_DEF for carrier selection, which you specify in the carrier selection settings (H07, S4TM2). E03 shows a carrier selection run with settings CSEL_S4TM1 that ranks carrier TM-CAR-10 first (estimated charges 1,598.38 EUR) ahead of TM-CAR-11 (1,773.08 EUR) and selects it automatically. The subcontracting status then reads Carrier Assigned.

## Strategy determination picks the most concrete transportation lane for the business document (location-to-location is more concrete than location-to-zone or a location lane), and for documents with several stops the overall carrier availability setting intersects the carriers of all stages
H07 (Strategy Determination): the system finds, among the relevant transportation lanes, the one that most closely matches the business document, and uses the strategy defined there. H07 example for a freight order from A to B with three lanes: A to B between locations (most concrete), A to a zone B' that contains B (less concrete, since a zone can contain several locations), and a location transportation lane at A (less concrete, since a lane between two locations is more concrete than a location lane). Only carriers in the lane are considered.

**Several stops** (H07, Determining Available Carriers): the system looks for a direct lane between source and destination as a starting point. With the checkbox for overall carrier availability, it finds the most concrete lane for each stage (A to B, B to C, C to D) and also for the main carriage (A to D), then intersects all the carrier lists. The result can be no carrier, one or several. In effect, stages and stops act as a filter. First it checks which carriers cover all stages, then it picks from those with a direct lane between A and D. Without the checkbox, only the main stage is used. If transportation allocations are not to be considered, even carriers without free capacity are shown.

## Practice
Produce a one-page planning flow sheet for a fictional shipper. Choose one example order and show, in order:
1. The freight unit building step: the FUB strategy, the planning quantity, the split quantity and the rounding value, with the resulting number of freight units.
2. The cockpit start: the selection profile, the planning profile and the page layout used.
3. The planning choice, either manual planning, VSR optimization or the shortcut, with its scheduling direction.
4. The carrier selection strategy and the resulting ranking logic.

Use only terms and settings from this session's material.

## Self-check
Can I explain to a transportation planner, without notes, how a forwarding order becomes freight units, how those freight units are planned in the transportation cockpit, and how a carrier is selected for the resulting freight order?
