# S4611-Basic-Transportation-Management-in-SAP-S4HANA.md — Sections
Source: src/md/courses/S4611-Basic-Transportation-Management-in-SAP-S4HANA.md · 8779 lines · structure: markdown · built 2026-10-21

| Line | Topic |
|---|---|
| 22 | Disclaimers |
| 65 | Typographic Conventions |
| 75 | Procedure |
| 79 | Hint |
| 153 | Management |
| 157 | Motivation and Overview |
| 169 | Lesson: Using Worklists in TM |
| 185 | Lanes |
| 195 | Lesson: Creating Freight Units |
| 199 | Building Rules |
| 201 | Lesson: Defining Conditions |
| 207 | Transportation Planning |
| 213 | Lesson: Subcontracting to Carriers |
| 256 | Transportation Execution |
| 288 | Outlook – Advanced Transportation |
| 299 | TARGET AUDIENCE |
| 342 | UNIT OBJECTIVES |
| 372 | LESSON OBJECTIVES |
| 379 | Motivation Behind SAP S/4HANA |
| 419 | Figure 1: SAP Strategy - Deliver the Intelligent Enterprise |
| 451 | Figure 2: The Next Generation Business Suite |
| 472 | Animation: The Next Generation Business Suite |
| 487 | Figure 4: The Next Generation Intelligent ERP |
| 498 | Animation: The Next Generation Intelligent ERP |
| 513 | Figure 6: The Evolution of the SAP S/4HANA Architecture |
| 566 | Figure 9: SAP S/4HANA Deployment Options |
| 600 | LESSON SUMMARY |
| 625 | LESSON OBJECTIVES |
| 634 | Transportation Management |
| 639 | Figure 10: Shipments in Logistics Execution |
| 663 | Animation: Shipments in Logistics Execution |
| 684 | Figure 12: Basic Shipping - LE-TRA and TM |
| 764 | Figure 14: Transportation Management - Overview |
| 789 | Animation: Transportation Management - Overview |
| 795 | Best Practice Scenarios |
| 812 | LESSON SUMMARY |
| 835 | Learning Assessment |
| 847 | X D Embedded SAP APO |
| 859 | X D Automatic carrier selection using the optimizer |
| 873 | X D Freight Order |
| 897 | Using Worklists in TM |
| 907 | UNIT OBJECTIVES |
| 934 | LESSON OBJECTIVES |
| 941 | SAP Fiori UX |
| 960 | Intuitive User Experience and a Responsive Design |
| 987 | Unit 2: New User Experience – Working with TM |
| 995 | Figure 16: Role Based User Experience |
| 1008 | Animation: Role Based User Experience |
| 1024 | Animation: Elements of Personalization |
| 1054 | Unit 2: New User Experience – Working with TM |
| 1079 | LESSON SUMMARY |
| 1096 | LESSON OBJECTIVES |
| 1103 | Worklists in TM |
| 1107 | Figure 22: Personal Object Worklists |
| 1144 | Management |
| 1146 | Business Example |
| 1176 | Management |
| 1178 | Business Example |
| 1282 | LESSON SUMMARY |
| 1296 | Learning Assessment |
| 1344 | Creating the Transportation Network |
| 1360 | UNIT OBJECTIVES |
| 1393 | LESSON OBJECTIVES |
| 1400 | Business Partners |
| 1418 | Figure 24: Business Partner Approach in SAP S/4HANA |
| 1428 | Unit 3: Master Data for Logistical Processes |
| 1458 | Relevant Business Partner Roles |
| 1496 | Simulation: How to Maintain Business Partners |
| 1501 | LESSON SUMMARY |
| 1518 | LESSON OBJECTIVES |
| 1527 | The Transportation Network and its Creation |
| 1534 | Figure 27: Transportation Network Overview |
| 1564 | Animation: Locations in the Transportation Network |
| 1596 | Vendor |
| 1645 | Port |
| 1647 | Airport |
| 1649 | Railway Station |
| 1653 | Hub |
| 1655 | Gateway |
| 1659 | Warehouse |
| 1663 | Rail Junction |
| 1667 | Loading Point |
| 1678 | Creation of Locations |
| 1689 | Lesson: Creating the Transportation Network |
| 1703 | Creating Locations Out of Business Documents |
| 1727 | Inbound Deliveries |
| 1729 | Creating Locations out of Business Partner Master |
| 1737 | Updating Locations Using a Report |
| 1763 | Unit 3: Master Data for Logistical Processes |
| 1768 | Transportation Zones |
| 1770 | Figure 31: Transportation Zones |
| 1802 | Transportation Lanes |
| 1806 | Animation: Transportation Lanes |
| 1827 | Default Route |
| 1829 | Figure 34: Default Route |
| 1836 | Animation: Default Route |
| 1848 | Means of Transport |
| 1852 | Animation: Means of Transport |
| 1904 | Business Example |
| 1937 | Unit 3: Master Data for Logistical Processes |
| 1956 | Business Example |
| 2003 | Unit 3: Master Data for Logistical Processes |
| 2068 | Lesson: Creating the Transportation Network |
| 2132 | LESSON SUMMARY |
| 2151 | LESSON OBJECTIVES |
| 2158 | Organizational Units |
| 2206 | Unit 3: Master Data for Logistical Processes |
| 2230 | Animation: Organizational Classification |
| 2247 | Figure 42: Organizational Structures |
| 2264 | Animation: TM and MM Purchasing Organization |
| 2273 | LESSON SUMMARY |
| 2287 | Learning Assessment |
| 2311 | X D Business Partner |
| 2321 | X C Transportation Lane |
| 2333 | X D Using a Report |
| 2340 | Unit 3: Learning Assessment |
| 2348 | X B Production |
| 2369 | Creating Freight Units |
| 2375 | Defining Conditions |
| 2389 | UNIT OBJECTIVES |
| 2424 | LESSON OBJECTIVES |
| 2435 | The Transportation Management Process |
| 2452 | Animation: Process Flow |
| 2475 | Delivery Integration |
| 2477 | Figure 47: Delivery Integration |
| 2487 | Control Keys |
| 2498 | Unit 4: Creation of Transportation Requirements |
| 2505 | Animation: Control Keys |
| 2516 | Defining Transportation Relevance by Assigning Control Keys |
| 2523 | Animation: Defining Transportation Relevance |
| 2538 | Lesson: Defining Transportation Relevance |
| 2552 | Logistics Integration Profile |
| 2565 | Incoterm Location Stage Building |
| 2570 | Incoterms |
| 2586 | Figure 52: Incoterms |
| 2622 | Ex Works |
| 2628 | Cost and Freight |
| 2644 | Free Carrier |
| 2658 | Lesson: Defining Transportation Relevance |
| 2666 | Figure 53: Stage Building Based on Incoterms |
| 2727 | Integration of Text Types |
| 2744 | Delivery Updates |
| 2755 | Figure 54: Delivery Updates |
| 2777 | Delivery Splits |
| 2788 | Figure 55: Delivery Splits |
| 2830 | Figure 56: Transportation Planning Changes |
| 2835 | Block Handling |
| 2846 | Handling Units |
| 2861 | Animation: Handling Units |
| 2882 | Packaging Materials |
| 2911 | LESSON SUMMARY |
| 2932 | LESSON OBJECTIVES |
| 2939 | Freight Unit Types |
| 2945 | Animation: Process Flow - Freight Units |
| 2955 | Lesson: Creating Freight Units |
| 2962 | Freight Units |
| 2966 | Animation: Freight Units |
| 2988 | Figure 64: Freight Unit Type Customizing |
| 3033 | Lesson: Creating Freight Units |
| 3052 | Freight Unit Building Rules |
| 3070 | Figure 65: Reasons for Freight Unit Splits |
| 3082 | Unit 4: Creation of Transportation Requirements |
| 3094 | Animation: Freight Unit Building Rule |
| 3119 | Freight Units |
| 3123 | Figure 68: Handling Units and Freight Units |
| 3172 | Business Example |
| 3188 | BS |
| 3203 | DEF_CHACO |
| 3244 | Business Example |
| 3260 | BS |
| 3275 | DEF_CHACO |
| 3352 | LESSON SUMMARY |
| 3369 | LESSON OBJECTIVES |
| 3376 | Defining Conditions |
| 3421 | Lesson: Defining Conditions |
| 3495 | Create Sales Orders and Deliveries |
| 3502 | Simulation: Create Sales Orders and Deliveries |
| 3517 | Business Example |
| 3577 | Unit 4: Creation of Transportation Requirements |
| 3627 | Business Example |
| 3808 | Ship-to-party: TMBS##* |
| 3843 | Unit 4: Creation of Transportation Requirements |
| 3911 | Not Planned |
| 3922 | LESSON SUMMARY |
| 3936 | Learning Assessment |
| 3944 | X B Changing the dates on a freight order |
| 3956 | X C Invoicing block |
| 3964 | X False |
| 3972 | X False |
| 3979 | Unit 4: Learning Assessment |
| 4018 | Subcontracting to Carriers |
| 4030 | UNIT OBJECTIVES |
| 4052 | LESSON OBJECTIVES |
| 4061 | Freight Orders and Freight Bookings |
| 4089 | Freight Order Types |
| 4102 | Animation: Freight Order Type Customizing |
| 4153 | Figure 75: Organizational Unit Determination |
| 4179 | Figure 76: Sequence Type of Stages |
| 4217 | Freight Order Creation |
| 4219 | Figure 78: Creating Freight Unit Stages |
| 4252 | Freight Orders |
| 4256 | Animation: Freight Orders |
| 4292 | Figure 81: Creating Freight Orders |
| 4358 | Business Example |
| 4372 | TM |
| 4374 | Description |
| 4392 | Defined And Linear |
| 4424 | Selected |
| 4432 | DEF_CHACO |
| 4443 | Unit 5: Transportation Planning |
| 4481 | Business Example |
| 4495 | TM |
| 4497 | Description |
| 4515 | Defined And Linear |
| 4547 | Selected |
| 4555 | DEF_CHACO |
| 4566 | Unit 5: Transportation Planning |
| 4696 | LESSON SUMMARY |
| 4715 | LESSON OBJECTIVES |
| 4722 | Subcontracting to Carriers |
| 4729 | Figure 83: Assigning Carriers |
| 4743 | Animation: Assigning Carriers |
| 4774 | Figure 85: Status Management in Subcontracting |
| 4811 | Business Example |
| 4826 | Lifecycle Status |
| 4830 | Subcontracting Status |
| 4834 | Execution Status |
| 4842 | Lifecycle Status |
| 4846 | Subcontracting Status |
| 4850 | Confirmation Status |
| 4854 | Execution Status |
| 4864 | Lifecycle Status |
| 4868 | Subcontracting Status |
| 4872 | Confirmation Status |
| 4876 | Execution Status |
| 4890 | Business Example |
| 4921 | Lifecycle Status |
| 4925 | Subcontracting Status |
| 4929 | Execution Status |
| 4937 | In Process |
| 4945 | Not Started |
| 4958 | Lifecycle Status |
| 4962 | Subcontracting Status |
| 4966 | Confirmation Status |
| 4970 | Execution Status |
| 4986 | Sent |
| 4994 | Not Started |
| 5002 | Lifecycle Status |
| 5006 | Subcontracting Status |
| 5010 | Confirmation Status |
| 5014 | Execution Status |
| 5034 | Sent |
| 5038 | Not Started |
| 5047 | LESSON SUMMARY |
| 5061 | Learning Assessment |
| 5069 | X A Manual Creation |
| 5075 | X D Creation by Copying |
| 5101 | X D Sea |
| 5109 | X False |
| 5151 | UNIT OBJECTIVES |
| 5186 | LESSON OBJECTIVES |
| 5195 | Transportation Execution |
| 5212 | Figure 87: Transportation Execution Process |
| 5222 | Unit 6: Transportation Execution |
| 5241 | LESSON SUMMARY |
| 5260 | LESSON OBJECTIVES |
| 5269 | Creation of (Print) Freight Documents |
| 5281 | Output Management in TM Documents |
| 5319 | Output Management Adapter |
| 5344 | Animation: Output Management Adapter |
| 5379 | Animation: Output Management Conditions |
| 5418 | Why |
| 5428 | Next batch job |
| 5442 | Process” |
| 5448 | Figure 93: Output Management Logic |
| 5456 | Output Management Capabilities |
| 5475 | Unit 6: Transportation Execution |
| 5488 | Simulation: Create Freight Documents |
| 5503 | Business Example |
| 5516 | Lifecycle Status |
| 5520 | Execution Status |
| 5536 | Business Example |
| 5549 | Lifecycle Status |
| 5553 | Execution Status |
| 5571 | Lifecycle Status |
| 5577 | Not Loaded |
| 5579 | Execution Status |
| 5594 | Lesson: Creating (Print) Freight Documents |
| 5622 | LESSON SUMMARY |
| 5641 | LESSON OBJECTIVES |
| 5648 | Warehouse Integration |
| 5660 | Inventory Management |
| 5680 | Inventory Management |
| 5684 | Animation: Inventory Management |
| 5697 | Extended Warehouse Management |
| 5715 | Figure 97: Extended Warehouse Management |
| 5726 | Advanced TM - EWM Integration |
| 5737 | Unit 6: Transportation Execution |
| 5752 | Stockroom Management |
| 5780 | Stock Room Management Exclusion List |
| 5803 | Warehouse Integration |
| 5818 | Unit 6: Transportation Execution |
| 5832 | Simulation: Pick, Load, and Post Goods Issue |
| 5847 | Business Example |
| 5883 | Overall Status |
| 5920 | Goods movement status |
| 5928 | Execution Status |
| 5930 | Logistical Execution Status |
| 5938 | Execution Status |
| 5952 | Business Example |
| 5988 | Overall Status |
| 6045 | Open |
| 6051 | In Process |
| 6057 | Open |
| 6115 | Goods movement status |
| 6147 | Packing not required |
| 6158 | Completed |
| 6172 | Completed |
| 6186 | Completed |
| 6194 | Execution Status |
| 6196 | Logistical Execution Status |
| 6216 | In Process |
| 6222 | SP_1010 Loaded with timestamp |
| 6239 | Logistical Execution Status |
| 6261 | In execution |
| 6274 | LESSON SUMMARY |
| 6288 | Learning Assessment |
| 6299 | X False |
| 6307 | X False |
| 6319 | X D Update Condition |
| 6333 | X D Outbound Delivery |
| 6340 | Unit 6: Learning Assessment |
| 6354 | X D Forwarding Orders |
| 6395 | Distributing Transportation Costs |
| 6415 | UNIT OBJECTIVES |
| 6452 | LESSON OBJECTIVES |
| 6463 | Charge Calculation Master Data |
| 6478 | Animation: Integration Of Charge Management |
| 6493 | Figure 105: Transportation Charge Management Master Data |
| 6498 | Freight Agreements Contractual Data |
| 6512 | Freight Agreement |
| 6522 | Lesson: Describing Charge Calculation Master Data |
| 6527 | Figure 106: Freight Agreement Overview |
| 6532 | Charge Calculation Sheet |
| 6553 | Figure 107: Calculation Sheet Overview |
| 6560 | Calculation Sheet Items |
| 6593 | Lesson: Describing Charge Calculation Master Data |
| 6629 | Charge Type |
| 6638 | Animation: Charge Types |
| 6650 | Figure 109: Charge Types |
| 6709 | Rate Table |
| 6716 | Rate Table Elements |
| 6750 | Unit 7: Settle Transportation Charges and Distribute Costs |
| 6798 | Scales |
| 6813 | Figure 111: Scale Overview |
| 6863 | Calculation Base |
| 6868 | Figure 112: Calculation Base |
| 6882 | Animation: Calculation Base |
| 6896 | Lesson: Describing Charge Calculation Master Data |
| 6905 | LESSON SUMMARY |
| 6926 | LESSON OBJECTIVES |
| 6931 | Agreement Determination |
| 6948 | Charge Calculation Customizing and Assignment |
| 6972 | Charges Profile |
| 6982 | Lesson: Calculating Transportation Charges |
| 6987 | Figure 114: Charge Calculation Customizing |
| 7014 | Animation: Charge Calculation |
| 7046 | Example Calculation |
| 7050 | Animation: Example Calculation |
| 7060 | Simulation: Calculate Transportation Charges |
| 7083 | Business Example |
| 7174 | Business Example |
| 7235 | Rate Table |
| 7237 | HANDLING_RATE_ |
| 7252 | Value Type |
| 7258 | HNDL |
| 7260 | Absolute Value |
| 7272 | Same Scale |
| 7288 | Currency |
| 7328 | Price Unit UoM |
| 7427 | Rate Table |
| 7441 | Rate Table |
| 7452 | LESSON SUMMARY |
| 7474 | LESSON OBJECTIVES |
| 7483 | Freight Settlement Processing |
| 7530 | Freight Settlement Document |
| 7551 | Animation: Freight Settlement Document Overview |
| 7579 | Animation: Freight Settlement Document Creation |
| 7610 | Animation: Freight Settlement Document Creation |
| 7683 | Animation: Purchase Order and Service Entry Sheet |
| 7703 | Lesson: Settling Transportation Charges with Carriers |
| 7721 | Freight Settlement Document Changes |
| 7742 | LESSON SUMMARY |
| 7761 | LESSON OBJECTIVES |
| 7766 | Freight Costs |
| 7781 | Animation: Cost Distribution Concept |
| 7791 | Lesson: Distributing Transportation Costs |
| 7804 | Figure 133: Cost Distribution Configuration |
| 7811 | Cost Distribution Profiles, Methods, and Rules |
| 7884 | Bill freight costs to customers in SD |
| 7905 | Figure 135: Billing Freight Costs in SD |
| 7945 | Business Example |
| 7969 | Type |
| 7981 | HNDL |
| 7989 | HNDL |
| 7997 | HNDL |
| 8006 | Unit 7: Settle Transportation Charges and Distribute Costs |
| 8030 | Business Example |
| 8068 | Type |
| 8080 | HNDL |
| 8088 | HNDL |
| 8092 | BASE |
| 8108 | HNDL |
| 8121 | Type |
| 8133 | FUEL |
| 8137 | HNDL |
| 8139 | Assigned |
| 8145 | FUEL |
| 8149 | HNDL |
| 8151 | Assigned |
| 8157 | FUEL |
| 8161 | HNDL |
| 8205 | Service Entry Sheet |
| 8222 | Number varies |
| 8233 | Simulation: Verify a Freight Invoice |
| 8248 | Business Example |
| 8271 | Business Example |
| 8321 | LESSON SUMMARY |
| 8340 | Learning Assessment |
| 8376 | X False |
| 8383 | Unit 7: Learning Assessment |
| 8395 | X C Carrier |
| 8420 | X False |
| 8453 | X D Sequential distribution |
| 8461 | X B Freight booking |
| 8465 | X D Delivery |
| 8489 | UNIT OBJECTIVES |
| 8509 | Management |
| 8511 | LESSON OBJECTIVES |
| 8516 | Advanced Transportation Management |
| 8522 | Animation: Functions of Advanced Transportation |
| 8552 | Figure 140: Order-Based Transportation Management |
| 8579 | Animation: VSR Optimizer Constraints |
| 8601 | Mixed Package Building |
| 8605 | Animation: Mixed Package Building |
| 8628 | Warehouse Integration |
| 8630 | Figure 145: Warehouse Integration |
| 8657 | Animation: Charge Calculation and Settlement |
| 8689 | Embedded Analytics |
| 8691 | Figure 148: Embedded Analytics |
| 8718 | LESSON SUMMARY |
| 8737 | Learning Assessment |
| 8745 | X A Sales Order |
| 8749 | X C Forwarding Order |
| 8753 | X E Delivery |
| 8763 | X C CS – Carrier Selection |
| 8767 | X E SEQ – Sequencing Optimizer |
| 8775 | X False |
