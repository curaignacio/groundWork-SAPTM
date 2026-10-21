# H05 - Logistics Integration.md — Sections
Source: src/md/sapHelp/H05 - Logistics Integration.md · 7158 lines · structure: markdown · built 2026-10-21

| Line | Topic |
|---|---|
| 9 | Public |
| 15 | Warning |
| 32 | Logistics Integration |
| 50 | Use |
| 86 | Collectively plan transportation for all orders and scheduling agreements |
| 94 | Perform sales order scheduling |
| 109 | Features |
| 111 | Order Integration |
| 127 | Scheduling Agreement Integration |
| 139 | JIT Call Integration |
| 147 | Delivery Proposals |
| 153 | Delivery Integration |
| 163 | Transportation Relevance |
| 167 | Integration Time Range |
| 180 | Dangerous Goods |
| 187 | Business Processes |
| 211 | Prerequisites |
| 223 | Advanced Intercompany Sales |
| 243 | Advanced Intercompany Stock Transfer |
| 266 | Incoterms and Incoterm Locations |
| 290 | Stage Building |
| 300 | Transfer of Control |
| 316 | Example of an Advanced Intercompany Sales Process |
| 335 | Customer |
| 343 | Material availability date and requested delivery date |
| 380 | Loading date and delivery date |
| 424 | Related Information |
| 434 | Use |
| 440 | Prerequisites |
| 444 | Activities |
| 448 | Integration |
| 450 | Logistics Integration |
| 454 | Define Control Keys for Document Integration |
| 462 | Define Logistics Integration Profile |
| 474 | Activate Integration of Sales Documents |
| 490 | Activate Integration of Purchasing Documents |
| 513 | Activate Integration of Delivery Documents |
| 527 | Determine Transport-Driven Process Relevance for Deliveries |
| 547 | Assign SD/MM Text Types to TM Text Types for SO/PO |
| 553 | Assign Logistics Execution Text Types to TM Text Types for Deliveries |
| 559 | Define Usage of Packaging Information |
| 569 | Definition |
| 573 | Structure |
| 630 | Source and Destination Location Determination |
| 646 | Prerequisites |
| 660 | Integration |
| 662 | Logistics Integration |
| 666 | Define Logistics |
| 677 | Improved Location Determination / Advanced Shipping and Receiving |
| 691 | Agreements |
| 701 | One Time Locations |
| 709 | One-Time Location |
| 715 | Definition |
| 721 | Structure |
| 729 | Integration |
| 739 | Common Settings |
| 741 | Freight Unit Building Rule |
| 752 | Condition for Freight Unit Building Rule Determination |
| 760 | Automatic Freight Unit Building |
| 766 | Stage Building Variant |
| 782 | Order-Related Settings |
| 784 | Plan on Requested or Confirmed Quantities |
| 788 | Feight Unit Building for Partly Complete Sales Documents |
| 796 | Integration Based on Actual Quantity |
| 800 | Improved Location Determination |
| 812 | Definition |
| 822 | Structure |
| 830 | Integration |
| 838 | Common Settings |
| 840 | Freight Unit Building Rule |
| 844 | Condition for Freight Unit Building Rule Determination |
| 852 | Stage Building Variant |
| 860 | Definition |
| 864 | Structure |
| 870 | Decentralized |
| 880 | Common Settings |
| 882 | Freight Unit Building Rule |
| 886 | Condition for Freight Unit Building Rule Determination |
| 894 | Stage Building Variant |
| 907 | Compliance Check |
| 911 | Related Information |
| 915 | Reports for Logistics Integration |
| 931 | Administration |
| 935 | Reports |
| 939 | Technical Name: /SCMTMS/ACTIVATE_MMSAG_WO_DLV |
| 947 | Technical Name: /SCMTMS/LI_ACTIVATE |
| 953 | Technical Name: /SCMTMS/ADAPT_START_MM_WO_DLV |
| 961 | Technical Name: /SCMTMS/DLV_BATCH |
| 967 | Technical Name: /SCMTMS/DEACTIVATE_MMSAG_W_DLV |
| 980 | Technical Name: /SCMTMS/UPDATE_INT_TIMERANGE |
| 986 | Technical Name: /SCMTMS/REACTIVATE_MMSAG_W_DLV |
| 992 | Technical Name: /SCMTMS/FIX_INT_TIMERANGE |
| 998 | Technical Name: /SCMTMS/SUBSEQENT_FUB_LOGINT |
| 1004 | Technical Name: /SCMTMS/TM_SAG_PLANNING_SYNC |
| 1012 | Use |
| 1057 | Process |
| 1111 | Integration of Orders |
| 1119 | Use |
| 1125 | Prerequisites |
| 1131 | Process |
| 1165 | Result |
| 1171 | Related Information |
| 1175 | Integration of Stock Transport Orders |
| 1191 | Prerequisites |
| 1193 | General Prerequisites |
| 1197 | Other Prerequisites |
| 1205 | Integration |
| 1209 | Internal TM |
| 1211 | Component Integration |
| 1219 | Integration |
| 1221 | Logistics Integration |
| 1233 | Integration |
| 1235 | Logistics Integration |
| 1239 | Define Transportation- |
| 1247 | Integration |
| 1257 | Shipping |
| 1263 | Point Determination |
| 1267 | Use |
| 1275 | STOs in the Advanced Shipping and Receiving Scenario |
| 1291 | Purchase Order |
| 1316 | STOs in Other Scenarios |
| 1324 | Use |
| 1334 | Process |
| 1370 | Use |
| 1387 | Materials Management (MM) orders |
| 1395 | Prerequisites |
| 1415 | Freight Order |
| 1427 | Features |
| 1429 | Background Report |
| 1439 | Interactive Delivery Creation |
| 1466 | From the Transportation Cockpit |
| 1476 | Source of Data |
| 1480 | Dates |
| 1486 | Quantities |
| 1490 | Consolidation |
| 1514 | Incoterms |
| 1516 | Shipping conditions |
| 1538 | Consumption of Schedule Lines in LE |
| 1559 | Execution and Planning Blocks in LE |
| 1567 | Exclude freight units or freight orders that are blocked for execution |
| 1599 | Delivery Proposals with Freight Document Hierarchies |
| 1619 | Delivery Proposals for Bulk Material |
| 1642 | Use |
| 1648 | Process |
| 1650 | Integration of LE Deliveries Without Integrating Order into TM |
| 1674 | Use |
| 1686 | Prerequisites |
| 1692 | Freight Unit |
| 1696 | More Information |
| 1713 | Use |
| 1721 | Process |
| 1723 | Update of an Order |
| 1737 | Deletion of an Order |
| 1759 | Use |
| 1778 | Process |
| 1780 | Update of a Delivery |
| 1806 | Deletion of a Delivery |
| 1822 | Split of a Delivery |
| 1830 | Use |
| 1842 | Prerequisites |
| 1846 | Process |
| 1873 | Prerequisites |
| 1879 | Process |
| 1881 | Outbound Delivery Split |
| 1916 | Outbound Delivery Update |
| 1941 | Assignments |
| 1965 | Prerequisites |
| 1971 | Transportation Unit |
| 1973 | Define Transportation Unit Types |
| 1977 | Features |
| 1983 | Related Information |
| 1996 | Load Planning |
| 1998 | Delivery Updates in TM Triggered by Logistics Execution |
| 2014 | Prerequisite |
| 2024 | Collection |
| 2030 | Integration |
| 2032 | Logistics Integration |
| 2034 | Internal TM Component Integration |
| 2038 | Process |
| 2062 | Goods Movement in Logistics Execution (LE) Triggered by TM |
| 2083 | Departure |
| 2095 | Unloading end |
| 2101 | Prerequisites |
| 2109 | Freight Order |
| 2113 | Integration of Scheduling Agreements |
| 2119 | Features |
| 2125 | Forecasts |
| 2131 | Planning Delivery |
| 2139 | Related Information |
| 2145 | Integration of Stock Transport Scheduling Agreements |
| 2154 | Integration of Purchase Scheduling Agreements |
| 2170 | Prerequisites |
| 2176 | Integration |
| 2178 | Logistics Integration |
| 2182 | Define |
| 2186 | Features |
| 2188 | Create or Update Schedule Lines |
| 2196 | Process Planning |
| 2210 | Communication to Suppliers |
| 2216 | Create Deliveries |
| 2222 | Integration with JIT and nJIT |
| 2249 | Restrictions |
| 2261 | Integration Time Range for Purchase Scheduling Agreement |
| 2273 | Prerequisites |
| 2277 | Integration |
| 2279 | Logistics Integration |
| 2281 | Internal TM Component Integration |
| 2283 | Define Rule Groups to Determine Integration Time Range |
| 2291 | Integration |
| 2293 | Logistics Integration |
| 2297 | Define Logistics |
| 2301 | Concept |
| 2303 | Determining an Integration Time Range |
| 2330 | Figure 1: How the Start Date is Determined |
| 2340 | Figure 2: How the End Date is Determined |
| 2344 | Setting an Integration Time Range: Rule Groups and Rules |
| 2352 | An additional offset type |
| 2360 | A safety margin |
| 2381 | Correcting Customizing Errors |
| 2389 | Example |
| 2393 | Start Date |
| 2401 | End Date |
| 2471 | Delivery Integration |
| 2487 | Prerequisites |
| 2493 | Integration |
| 2499 | Define Transportation |
| 2505 | Integration |
| 2507 | Logistics Integration |
| 2509 | Internal TM Component Integration |
| 2519 | Integration |
| 2521 | Logistics Integration |
| 2525 | Define Logistics |
| 2529 | Key Features |
| 2572 | Don't consider any deliveries |
| 2600 | Related Information |
| 2607 | Agreement Integration |
| 2613 | Prerequisites |
| 2617 | Use |
| 2631 | Establishing an Integration Time Range End Date |
| 2652 | Deactivating the Integration of Purchase Scheduling Agreements |
| 2666 | Remove the freight units from your transportation plan |
| 2687 | Reactivating the Integration of Purchase Scheduling Agreements |
| 2701 | Activities |
| 2707 | Administration |
| 2724 | Related Information |
| 2732 | Integration of Sales Scheduling Agreements |
| 2744 | Prerequisites |
| 2750 | Integration |
| 2752 | Logistics Integration |
| 2756 | Define |
| 2760 | Features |
| 2762 | Create or Update Schedule Lines |
| 2772 | Freight Unit Building |
| 2784 | Create Deliveries |
| 2799 | Integration of Orders |
| 2809 | SACO |
| 2817 | Related Information |
| 2821 | Integration of Stock Transport Scheduling Agreements |
| 2849 | Prerequisites |
| 2859 | Integration |
| 2861 | Logistics Integration |
| 2863 | Internal TM Component Integration |
| 2871 | Integration |
| 2873 | Logistics Integration |
| 2892 | Integration |
| 2894 | Logistics Integration |
| 2896 | Internal TM Component Integration |
| 2906 | Integration |
| 2910 | Warehouse Management |
| 2914 | Sample Process |
| 2995 | Integration of Sales Order Scheduling |
| 3003 | Prerequisites |
| 3009 | Integration |
| 3021 | Integration |
| 3027 | Define |
| 3035 | Order |
| 3037 | Order Without Charge |
| 3047 | Header |
| 3112 | Scheduling Schema |
| 3122 | General Settings |
| 3136 | General Settings |
| 3140 | Activate BPS for Sales |
| 3166 | Use |
| 3187 | Sales Order Scheduling Based on TM Durations |
| 3201 | Sales Order Scheduling Based on TM Scheduling |
| 3217 | Backorder Processing |
| 3225 | Customizing Input Data |
| 3231 | Business Process Scheduling |
| 3261 | Process |
| 3289 | Integration of Stock Transport Order Scheduling |
| 3297 | Prerequisites |
| 3299 | Prerequisites in Transportation Management |
| 3307 | Integration |
| 3309 | Logistics Integration |
| 3331 | Prerequisites in ATP |
| 3372 | Scheduling Schema |
| 3380 | General Settings |
| 3402 | Use |
| 3414 | How Scheduling Works |
| 3447 | Customizing Input Data |
| 3453 | Business Process Scheduling |
| 3465 | Process |
| 3477 | Integration of Next Generation Just-In-Time |
| 3509 | Prerequisites |
| 3515 | General |
| 3547 | Deliveries |
| 3569 | Forwarded JIS Call |
| 3582 | Advanced Shipping Notification |
| 3602 | BAdI: Change Transient TRQ Data |
| 3606 | BAdI: Changing Source / Destination of Business Transaction Documents |
| 3612 | Integration |
| 3630 | Logistics Integration |
| 3640 | Integration |
| 3687 | Integration |
| 3689 | Logistics Integration |
| 3693 | Define Logistics |
| 3786 | Related Information |
| 3804 | Sample Process |
| 3905 | Related Information |
| 3930 | Sample Process |
| 3962 | Related Information |
| 3982 | Sample Process |
| 4045 | Related Information |
| 4065 | Prerequisites |
| 4075 | Features |
| 4077 | Inbound Deliveries |
| 4111 | Outbound Deliveries |
| 4121 | More Information |
| 4129 | Related Information |
| 4206 | Extensibility |
| 4235 | Process |
| 4241 | Phase |
| 4245 | Details |
| 4247 | Web Service |
| 4281 | Based on the BTDRef |
| 4418 | Related Information |
| 4428 | External TM System Integration |
| 4434 | Use |
| 4456 | Integration |
| 4466 | Features |
| 4470 | Type of Integration |
| 4505 | Delivery Proposals |
| 4511 | Delivery Integration |
| 4521 | Dangerous Goods |
| 4527 | ERP-TM Communication |
| 4533 | Use |
| 4539 | Prerequisites |
| 4547 | Master Data |
| 4551 | Activities |
| 4562 | Settings in TM |
| 4568 | Integration |
| 4574 | Integration |
| 4582 | Plan on Req/Cnf Qty |
| 4588 | FU Building Rule Condition |
| 4592 | Integration |
| 4598 | Integration |
| 4602 | Define Delivery-Based Transportation Requirement Types |
| 4628 | Settings in SAP ERP |
| 4636 | Logistics Integration |
| 4644 | Management |
| 4675 | Logistics |
| 4685 | Integration of ERP Orders Without Sending Deliveries to TM |
| 4693 | Logistics Integration |
| 4701 | Integration of ERP Deliveries Without Sending Orders to TM |
| 4709 | Logistics Integration |
| 4717 | Definition |
| 4721 | Structure |
| 4760 | Use |
| 4764 | Process |
| 4783 | TRSR: TransportationRequestSUITERequest |
| 4903 | Use |
| 4907 | Prerequisites |
| 4911 | Process |
| 4924 | Transportation Planning Based on SAP ERP Order |
| 4997 | Result |
| 5009 | Definition |
| 5019 | Structure |
| 5027 | Document flow |
| 5031 | Items |
| 5046 | Statuses in the Order-Based Transportation Requirement |
| 5054 | New |
| 5058 | Planned |
| 5062 | Description |
| 5092 | Completed |
| 5104 | Canceled |
| 5112 | Status |
| 5114 | Description |
| 5116 | Execution Not Started |
| 5122 | Executed |
| 5151 | Status |
| 5155 | Description |
| 5161 | Consumed Partially |
| 5167 | Blocks |
| 5185 | Delivery block |
| 5193 | Integration |
| 5197 | External TM System Integration |
| 5203 | Credit Check |
| 5211 | Integration |
| 5215 | Freight unit |
| 5219 | Delivery-based transportation requirement |
| 5227 | Use |
| 5244 | Process |
| 5250 | Creation of ERP Deliveries from SAP TM |
| 5256 | IDCR: InboundDeliveryCreateRequest |
| 5337 | Use |
| 5350 | Prerequisites |
| 5374 | Freight Order |
| 5382 | Integration |
| 5386 | External |
| 5388 | TM System Integration |
| 5394 | Types |
| 5400 | Features |
| 5402 | Background Report |
| 5420 | Interactive Delivery Creation |
| 5457 | From the Transportation Cockpit |
| 5469 | Send |
| 5479 | Source of Data |
| 5483 | Dates |
| 5489 | Quantities |
| 5493 | ERP document references |
| 5497 | Consolidation |
| 5536 | Incoterms |
| 5538 | Shipping conditions |
| 5560 | Consumption of Schedule Lines in SAP ERP |
| 5574 | Execution and Planning Blocks in SAP ERP |
| 5626 | Delivery Proposals with Freight Document Hierarchies |
| 5646 | Delivery Proposals for Bulk Material |
| 5662 | Use |
| 5670 | Process |
| 5672 | Integration of ERP Deliveries Without Sending ERP Order to TM |
| 5722 | Integration of ERP Deliveries With Order Integration |
| 5734 | Integration of ERP Deliveries With Order Integration |
| 5779 | Definition |
| 5785 | Structure |
| 5793 | Document flow |
| 5797 | Items |
| 5805 | Statuses in the Delivery-Based Transportation Requirement |
| 5809 | Lifecycle Status |
| 5820 | New |
| 5824 | Planned |
| 5830 | Canceled |
| 5834 | Description |
| 5872 | Status |
| 5874 | Description |
| 5876 | Execution Not Started |
| 5882 | Executed |
| 5902 | Blocks |
| 5908 | Execution block |
| 5927 | Integration |
| 5935 | Requirements |
| 5941 | Integration |
| 5949 | Requirements |
| 5953 | Credit Check |
| 5961 | Packaging Information |
| 5969 | Integration |
| 5979 | Integration |
| 5983 | Freight units |
| 5987 | Order-based transportation requirement |
| 5995 | Use |
| 6003 | Features |
| 6005 | Determination of Freight Units |
| 6013 | Reassigning Freight Units to the Delivery-Based Transportation Requirement |
| 6034 | Splitting Freight Units |
| 6048 | Updating the Open Quantity of the Order-Based Transportation Requirement |
| 6054 | Updating the Status of the Order-Based Transportation Requirement |
| 6064 | Handling Units |
| 6080 | Example |
| 6121 | Posting Goods Issue from TM |
| 6129 | Use |
| 6147 | Integration |
| 6151 | Prerequisites |
| 6157 | Features |
| 6167 | Activities |
| 6179 | Use |
| 6185 | Prerequisites |
| 6198 | Integration |
| 6204 | Integration |
| 6212 | Features |
| 6218 | Not Relevant |
| 6222 | Not Processed |
| 6226 | Partially Processed |
| 6230 | Completely Processed |
| 6241 | Planning Not Started |
| 6245 | In Planning |
| 6249 | Partially Planned |
| 6253 | Planned |
| 6259 | TM Planning Status |
| 6273 | Partially Processed |
| 6282 | TM Planning Status |
| 6286 | Planned |
| 6288 | Completely Processed |
| 6292 | Use |
| 6312 | Features |
| 6322 | Deleting and Canceling Freight Units |
| 6330 | Use |
| 6338 | Process |
| 6340 | Update of an Order |
| 6351 | Update of Order in SAP ERP |
| 6383 | Deletion of an Order |
| 6394 | Deletion of Order in SAP ERP |
| 6426 | Use |
| 6445 | Process |
| 6447 | Update of a Delivery |
| 6451 | Update of Delivery in SAP ERP |
| 6502 | Deletion of a Delivery |
| 6506 | Deletion of Delivery in SAP ERP |
| 6541 | Split of a Delivery |
| 6551 | Use |
| 6559 | Prerequisites |
| 6565 | Integration |
| 6589 | Integration |
| 6595 | Delivery- |
| 6597 | Based Transportation Requirement |
| 6601 | Process |
| 6642 | Use |
| 6654 | Prerequisites |
| 6660 | Distribution status: Distributed |
| 6662 | Goods movement status: Partially Completed or Completed |
| 6668 | Integration |
| 6676 | Define |
| 6680 | Process |
| 6682 | Outbound Delivery Split |
| 6757 | Outbound Delivery Update |
| 6785 | Transportation Request Based on Outbound Delivery Update Confirmation |
| 6806 | Result |
| 6829 | Assignments |
| 6853 | Prerequisites |
| 6859 | Transportation Unit |
| 6861 | Define Transportation Unit Types |
| 6865 | Features |
| 6879 | Package Unit |
| 6883 | Load Planning |
| 6887 | Use |
| 6907 | Prerequisites |
| 6909 | Integration of Purchase Scheduling Agreements |
| 6913 | SAP ERP under |
| 6921 | Define |
| 6925 | Integration of Sales Scheduling Agreements |
| 6929 | ERP under |
| 6937 | Define Settings |
| 6941 | Transfer of Purchasing Documents |
| 6953 | Purchasing Documents |
| 6955 | Controlling the Sales Document Transfer |
| 6965 | Order Integration |
| 6971 | Features |
| 6982 | Sales scheduling agreements |
| 6996 | Materials Management (MM) scheduling agreements |
| 7010 | Restrictions |
| 7079 | Prerequisites |
| 7107 | Customer Side: Returns Handling |
| 7150 | Related Information |
| 7152 | Advanced Shipping and Receiving |
| 7154 | Integration with Advanced Shipping and Receiving |
