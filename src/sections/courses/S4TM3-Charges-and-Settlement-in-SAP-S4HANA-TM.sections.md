# S4TM3-Charges-and-Settlement-in-SAP-S4HANA-TM.md — Sections
Source: src/md/courses/S4TM3-Charges-and-Settlement-in-SAP-S4HANA-TM.md · 7925 lines · structure: markdown · built 2026-10-21

| Line | Topic |
|---|---|
| 2 | SAP S/4HANA TM |
| 16 | Unit 6 - Procuring Strategic Freight |
| 35 | S/4HANA Enterprise Management |
| 37 | Lesson 1 - Evaluating Transportation Management |
| 66 | Executive Decisions |
| 99 | Evolution of Transportation Management at SAP |
| 130 | Deployment Options and Migration Paths |
| 242 | Transportation Management - Overview |
| 483 | Data |
| 487 | Charge Calculations |
| 506 | Examples of Possible Scenarios |
| 545 | Note |
| 549 | Charge Requests |
| 582 | Scale template |
| 586 | Scale |
| 590 | Rate table |
| 598 | Charge types |
| 615 | Freight agreement |
| 625 | Business Example: Road-Sea-Road |
| 644 | Stage |
| 648 | Precarriage |
| 654 | Main carriage |
| 662 | On-carriage |
| 692 | Scale Base |
| 732 | Path for Customizing Templates |
| 738 | Fields |
| 740 | Field Assignment |
| 748 | UoM Relevant |
| 754 | Dimension |
| 765 | Numeric |
| 769 | Crcy Scale base |
| 773 | Raw values |
| 777 | Date Scale Base |
| 781 | Example |
| 793 | Value |
| 797 | WEIGHT |
| 801 | Usage |
| 824 | Scale Base Enhancement |
| 865 | Calculation Base |
| 937 | Scale Base |
| 941 | Field Assignment |
| 945 | Currency Field |
| 949 | Unit Field |
| 955 | Helper Assignment |
| 959 | Use BAdI |
| 966 | Party Role |
| 972 | Calculation Type |
| 980 | Calculation Usage |
| 988 | TrM Category |
| 1032 | Note |
| 1091 | Scale Templates |
| 1122 | Scale Template Fields |
| 1126 | Scale template |
| 1133 | Scale type |
| 1147 | Scale base |
| 1180 | Scale Maintenance Function |
| 1207 | Scale Creation |
| 1217 | Field |
| 1221 | Value |
| 1223 | Scale Base |
| 1227 | Length, Partner, Weight |
| 1233 | Scale Type |
| 1266 | Rounding |
| 1272 | Profile |
| 1284 | Calculation |
| 1290 | Type |
| 1321 | Scale Examples |
| 1332 | Charge Categories |
| 1400 | Charge Type Settings |
| 1404 | Possible Charge Type Settings |
| 1477 | Rate Table Templates |
| 1486 | Rate Tables |
| 1515 | Rate Table Template Usage |
| 1587 | Rate Table Maintenance |
| 1616 | Rate Table Definition Versus Maintain Rate Table |
| 1622 | Rate Table Maintenance Transactions |
| 1647 | Rate Table Structure |
| 1653 | Description |
| 1663 | Charge |
| 1667 | Usage |
| 1675 | Charge |
| 1679 | Type |
| 1685 | The Scales Tab Page |
| 1694 | Field |
| 1698 | Dimension |
| 1708 | Scale |
| 1712 | Calculation |
| 1716 | Base |
| 1722 | Minimum Value |
| 1730 | Value |
| 1750 | Method |
| 1758 | Calculation |
| 1771 | Field |
| 1773 | Description |
| 1775 | Valid From and Valid |
| 1781 | Rounding Profile |
| 1787 | Calculation Rules Tab Page |
| 1799 | Rate Values |
| 1816 | Multiple Scales within a Rate Table |
| 1867 | Approval Workflow |
| 1888 | Microsoft Excel Integration |
| 1902 | Download Options |
| 1927 | Mass Creation of Rates Tables Using Microsoft Excel |
| 1939 | Template Options |
| 1974 | SMC3 Integration for Rate Tables |
| 2013 | Mass Maintenance of Rates |
| 2017 | Mass Maintenance: Updating Rates |
| 2037 | Management of Validity Periods |
| 2070 | Integration of Mass Maintenance |
| 2119 | Mass Update of Rates - Example |
| 2131 | Source Location |
| 2166 | Attribute |
| 2200 | Source Location |
| 2227 | Source Location |
| 2258 | Calculation Sheet Maintenance |
| 2278 | Calculation Sheet Data |
| 2282 | General data |
| 2288 | Hierarchy items |
| 2298 | Preconditions and general terms |
| 2320 | Instruction Type |
| 2352 | Charge types |
| 2373 | Charge Type Details |
| 2389 | Rate Tab |
| 2424 | Basic Data Tab |
| 2487 | Classification Tab |
| 2507 | Preconditions and Notes Tab |
| 2522 | Resolution Base |
| 2528 | Charge Aspect Definition for Resolution Base |
| 2565 | Agreements Overview |
| 2609 | Organizations and Business Documents |
| 2629 | Contractual Data in Agreements |
| 2739 | Calculation and Charges Profiles |
| 2786 | Charges Profile |
| 2803 | Calculation Profile Assignment |
| 2846 | Note |
| 2856 | Calculation Settings in Freight Order Types |
| 2895 | Rules |
| 2897 | Freight Order Charge Calculation |
| 2926 | Freight Rate Derivation Process |
| 2957 | Maintain Preconditions in Agreement Items |
| 3006 | Available Item Preconditions |
| 3019 | CONSL_TYPE |
| 3023 | CONT_BASIS |
| 3031 | Mode |
| 3033 | MOVEM_TYPE |
| 3037 | SERVICE_LV |
| 3041 | SHIPMENT |
| 3045 | STAGE_CAT |
| 3049 | BRFplus Preconditions in Agreement Items |
| 3066 | Maintain Preconditions in Calculation Sheets |
| 3090 | BRFplus Preconditions in Calculation Sheets |
| 3107 | Agreement Determination |
| 3115 | Agreement Determination Based on Priority |
| 3145 | Agreement Determination and Selection Types |
| 3172 | Manual Agreement Selection: Functions |
| 3186 | Multiple Agreements Pop-up |
| 3192 | Note |
| 3199 | Agreement Determination Type |
| 3201 | Manual Agreement Selection: Example Scenarios |
| 3236 | Charge Calculation Rules |
| 3273 | TCM_FAGDEX - Freight Agreement Exclusion |
| 3301 | Further Charge Calculation Rules |
| 3393 | Freight Order Charge Estimations |
| 3415 | Item |
| 3426 | Wildcard Search |
| 3459 | Rate Lookup by Transportation Zone |
| 3488 | Charge Item at Header and Stage Level |
| 3533 | Charge Calculation with Through Rates |
| 3559 | Note |
| 3566 | Fuel Surcharge Calculation Method |
| 3736 | Optional: Standard Rate Table |
| 3759 | Calculation Methods |
| 3801 | Clipping Example |
| 3849 | Calculation Method Type Example: Break Weight |
| 3867 | Events |
| 3886 | Event Types |
| 3929 | Event-Based Charges |
| 3933 | Calculation of Charges Based on Delay |
| 3941 | Grace Days |
| 3961 | Event-Based Charge Customization |
| 3978 | Step 1: Definition of Calculation Bases |
| 4012 | ACTUAL_DATE |
| 4016 | ESTD_DATE |
| 4018 | ESTIMATED_DATE |
| 4024 | EXP_END_DATE |
| 4028 | DELAY |
| 4055 | Step 2: Event Profile |
| 4065 | Event Profile Attributes |
| 4095 | Business Document Options |
| 4141 | Event-Based Charges in Calculation Sheets |
| 4170 | Definition of the Related Calculation Base |
| 4176 | Definition of the Related Calculation Base |
| 4188 | Charge Calculation |
| 4220 | Freight Settlement Processing |
| 4300 | Freight Settlement Document Creation |
| 4353 | Note |
| 4364 | Partial Freight Settlement Document |
| 4378 | Management |
| 4384 | Posting Freight Charges |
| 4431 | Note |
| 4443 | Purchase Order and Service Entry Sheet |
| 4567 | Immediately" |
| 4575 | Check Results of Posting Action |
| 4637 | Note |
| 4649 | Automatic Change Management for Freight Settlements |
| 4717 | Configure Freight Settlement Creation in TM |
| 4746 | Step 1: Define Settlement Profiles |
| 4813 | Step 3: Define Number Range Intervals for FSDs |
| 4829 | Step 4: Define Freight Settlement Document Types |
| 4876 | Step 5: Assign FSD Type to FO/FB Types |
| 4901 | Note |
| 4907 | Configure Freight Settlement Integration to MM |
| 4932 | Step 1: Map Purchasing Organization |
| 4956 | Note |
| 5042 | Note |
| 5078 | Note |
| 5091 | Step 5: Enable User for Invoice Verification |
| 5118 | Carrier Invoice Verification & ERS |
| 5155 | Ready for Settlement |
| 5229 | Note |
| 5254 | Submitting Carrier Invoices |
| 5377 | Freight Charge Correction |
| 5401 | Note |
| 5412 | Credit Memo for Freight Orders |
| 5420 | Carrier Overcharge |
| 5438 | Credit Memo |
| 5467 | Example Flow for Credit Memo Process |
| 5495 | Note |
| 5510 | In customizing, chooseTransportation |
| 5518 | Influence invoicing status |
| 5532 | In customizing, choose Transportation |
| 5550 | In customizing, choose Transportation |
| 5569 | Dispute Management |
| 5621 | Business Scenario Examples |
| 5633 | Automatic |
| 5700 | Reject a dispute |
| 5708 | Mixed Scenario |
| 5721 | Cost Distribution |
| 5738 | Cost Distribution Steps |
| 5817 | Document Types in Freight Cost Posting |
| 5835 | Customer Scenarios: Examples |
| 5839 | SAP S/4HANA Integration |
| 6063 | Cost Distribution Configuration |
| 6098 | Direct Distribution |
| 6152 | Hierarchical Distribution |
| 6220 | Step 2: Define Cost Distribution Profile |
| 6263 | Step 5: Enable Cost Distribution in Document Types |
| 6271 | Cost Distribution Enablement |
| 6298 | SAP Business Add-Ins (BAdIs) for Cost Distribution |
| 6369 | Cost Distribution S4 Mapping Configuration |
| 6402 | Settlement Document Types |
| 6443 | Settlement Process Types |
| 6468 | Basic Settings for Settlement Document Creation |
| 6488 | Configuration Fields |
| 6564 | Note |
| 6578 | Documents |
| 6584 | Analyze Cost Distribution Postings |
| 6590 | Integration for Freight Cost Processing |
| 6606 | Freight Order Distribution: Based Upon Weight |
| 6662 | Analyze Postings for FSD and Settlement Management |
| 6728 | Lesson 3 - Billing Freight Cost to SD |
| 6797 | Note |
| 6814 | Lesson 1 - Understanding Strategic Freight Procurement |
| 6824 | Process Steps |
| 6894 | Determination of Procurement Needs |
| 6934 | Master RFQ Creation |
| 6959 | Creating Freight Agreement Master RFQs |
| 6978 | Master RFQ Versioning |
| 6988 | Note |
| 6998 | RFQ Header Data |
| 7023 | Master RFQ Items |
| 7040 | Transportation Spend Specifications |
| 7081 | Process |
| 7083 | RFQ Carrier Definition |
| 7110 | Trade Lane |
| 7132 | Target Business Shares and Individual RFQs |
| 7149 | Individual RFQ |
| 7186 | Responses to RFQs and Agreement Creation |
| 7209 | Evaluation and Freight Agreement Creation |
| 7274 | Response Comparison and Ranking |
| 7293 | Agreement Generation |
| 7326 | FA RFQ Assignments |
| 7376 | Freight Agreement RFQ Master Assignment Creation |
| 7388 | Note |
| 7400 | Procurement |
| 7408 | Optimization and Estimated Spend Simulation |
| 7433 | Target Share Strategies |
| 7450 | Condition Parameters |
| 7489 | Target Share Determination and Estimated Spend Simulation |
| 7537 | Target Rates in Freight Procurement |
| 7552 | Target Rate Settings |
| 7560 | Target Rate Publishing |
| 7575 | Bonus-Malus Functionality |
| 7591 | Bonus-Malus Functionality |
| 7633 | Bonus-Malus Values in Freight RFQ Carrier Section |
| 7657 | Provider Process |
| 7661 | Embedded LSP Business Scenarios |
| 7687 | Embedded LSP Scenarios |
| 7712 | Models for Embedded LSP Scenarios |
| 7716 | Embedded LSP Scenarios: Models |
| 7819 | Embedded LSP Basic Settings in TM |
| 7827 | Prerequisites and Configuration |
| 7864 | Configuration Steps |
| 7917 | Note |
