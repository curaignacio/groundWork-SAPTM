# H06 - Freight Order Management.md — Sections
Source: src/md/sapHelp/H06 - Freight Order Management.md · 21798 lines · structure: markdown · built 2026-10-21

| Line | Topic |
|---|---|
| 9 | Public |
| 15 | Warning |
| 34 | Use |
| 62 | Rail |
| 72 | Integration |
| 80 | Integration Type |
| 86 | Forwarding Order Management |
| 90 | Planning |
| 100 | Freight Settlement |
| 106 | Dangerous Goods |
| 112 | Global Trade |
| 118 | Features |
| 175 | Definition |
| 185 | Use |
| 193 | Freight Order |
| 214 | Structure |
| 226 | Business partner |
| 230 | Locations and dates/times |
| 242 | Items |
| 272 | Diagrams |
| 303 | Communication history |
| 311 | Output management, for example, print documents |
| 321 | Transportation dependencies, in other words, logistical dependencies |
| 339 | Notes |
| 349 | Use of Seals |
| 359 | Scheduling |
| 372 | Use |
| 376 | Prerequisites |
| 384 | Order |
| 388 | Features |
| 394 | Manual Creation |
| 398 | Creation Using an Inbound Message |
| 422 | Creation from Transportation Planning |
| 449 | Creation from the Freight Unit |
| 457 | Creation by Copying |
| 495 | Freight Order |
| 499 | Creation Based on a Schedule |
| 505 | Editing and Displaying Freight Orders |
| 509 | Freight Order Table |
| 513 | Freight Orders |
| 523 | Transportation Cockpit |
| 540 | Use |
| 554 | Process |
| 562 | Used resources |
| 566 | Schedules |
| 570 | Driver |
| 576 | Notes |
| 623 | Background Processing |
| 689 | More Information |
| 691 | Deviating Business Partner Addresses |
| 702 | Use |
| 710 | Features |
| 724 | FWM business document type determines the freight order creation |
| 736 | FWM business document attributes determine the freight order creation |
| 750 | Quantity determines freight order creation |
| 770 | Creation of Forwarding Orders from Freight Orders |
| 778 | Use |
| 784 | Customer Self-Delivery |
| 790 | Collective Goods Traffic |
| 798 | Prerequisites |
| 806 | Forwarding Order |
| 812 | Features |
| 832 | Activities |
| 838 | Create Rail Freight Order |
| 859 | Definition |
| 863 | Use |
| 889 | Freight |
| 897 | Freight Order |
| 915 | Structure |
| 919 | General Data |
| 932 | Number of railcars |
| 952 | Invoicing carrier level |
| 956 | Items |
| 962 | Equipment group and equipment type |
| 976 | Stages |
| 980 | Invoicing carrier |
| 1008 | Agreement party |
| 1017 | Assigning Carriers by Stage |
| 1025 | Applying Default Routes |
| 1035 | Document References |
| 1041 | Status |
| 1047 | Multi-item |
| 1084 | Single item |
| 1107 | Freight Settlement |
| 1115 | Use |
| 1119 | Prerequisites |
| 1131 | Equipment |
| 1137 | Commodity codes |
| 1143 | Freight Order |
| 1157 | Define Transportation |
| 1194 | Process |
| 1252 | Example |
| 1265 | Location |
| 1279 | Not applicable |
| 1285 | Default Route |
| 1345 | Railcar Unit |
| 1349 | Use |
| 1353 | Prerequisites |
| 1361 | Define |
| 1373 | Freight Order |
| 1385 | Capacities |
| 1397 | Insert a railcar as an individual item |
| 1401 | Insert a railcar as a multi-item |
| 1417 | Multi-item with expansion |
| 1423 | Multi-item without expansion |
| 1441 | Weight |
| 1443 | Locomotive |
| 1461 | Railcar |
| 1479 | Utilization |
| 1490 | Maximum utilization in percent |
| 1502 | Length utilization in percent |
| 1510 | Use |
| 1516 | Prerequisites |
| 1546 | Order |
| 1550 | Features |
| 1554 | Assigning a single driver or a driver team |
| 1577 | Assigning drivers not defined in master data |
| 1596 | Document |
| 1602 | Activities |
| 1610 | Drivers |
| 1651 | More Information |
| 1657 | Use |
| 1665 | Prerequisites |
| 1699 | Features |
| 1742 | Activities |
| 1755 | Use |
| 1759 | Features |
| 1763 | Sales side |
| 1769 | Order Management |
| 1775 | Forwarding order |
| 1781 | Forwarding agreement quotation |
| 1787 | Purchasing side |
| 1793 | Master Data |
| 1828 | Define Freight |
| 1834 | Use |
| 1846 | Prerequisites |
| 1882 | Define Freight |
| 1892 | Sequence Type of Stops: Star-Shaped Based on FU Stages |
| 1911 | HBL Building Strategy: PRCL_SHP |
| 1915 | Web Dynpro Application Config.: /SCMTMS/FRE_ORDER_MANIFEST |
| 1925 | Add. Output Profile: /SCMTMS/TOR_PRINT_PARCEL_ROOT |
| 1935 | Order |
| 1969 | Process |
| 2058 | Use |
| 2087 | Activities |
| 2099 | Example |
| 2101 | Appointments |
| 2117 | Scheduling of Freight Orders |
| 2125 | Use |
| 2135 | Prerequisites |
| 2149 | Freight Unit |
| 2153 | Process |
| 2238 | Example |
| 2244 | Document |
| 2248 | Dates Copied |
| 2252 | Dates Changed |
| 2256 | Manually |
| 2262 | System |
| 2346 | Requested |
| 2427 | Document |
| 2431 | Dates Copied |
| 2435 | Dates Changed |
| 2439 | Manually |
| 2445 | System |
| 2459 | Planned |
| 2489 | Use |
| 2503 | Prerequisites |
| 2509 | Freight Order |
| 2525 | Basic Settings |
| 2529 | Features |
| 2543 | Example |
| 2562 | Stage |
| 2582 | Use |
| 2588 | Prerequisites |
| 2598 | Process |
| 2641 | Definition |
| 2647 | Use |
| 2659 | Freight Booking |
| 2687 | Structure |
| 2693 | Business partner |
| 2695 | Locations and dates/times |
| 2714 | Transportation stages |
| 2742 | Items |
| 2778 | Capacity requirements |
| 2799 | Define |
| 2811 | Subcontracting information |
| 2825 | Communication history |
| 2851 | Notes |
| 2857 | More Information |
| 2865 | FCL Freight Bookings |
| 2878 | Nature of Goods |
| 2884 | Freight Document Overview |
| 2888 | Use |
| 2892 | Prerequisites |
| 2900 | Freight Booking |
| 2942 | Features |
| 2944 | Creation of Freight Bookings |
| 2955 | Manual Creation |
| 2959 | Creation from a Forwarding Order |
| 2969 | Creation from the Transportation Cockpit |
| 2979 | Creation from the Freight Unit |
| 2987 | Creation by Copying |
| 3015 | Creation Based on a Schedule |
| 3021 | Editing and Displaying of Freight Bookings |
| 3025 | Freight Booking Table |
| 3036 | User Interfaces for Editing and Displaying |
| 3044 | Transportation Cockpit |
| 3060 | Usage |
| 3070 | Prerequistes |
| 3076 | Freight Booking |
| 3080 | Process |
| 3086 | Shipper, consignee, and carrier |
| 3092 | Number of containers |
| 3115 | Schedule |
| 3119 | Freight terms |
| 3191 | More Information |
| 3197 | Use |
| 3209 | Prerequisites |
| 3217 | Freight Booking |
| 3221 | Features |
| 3259 | Item changes |
| 3268 | Location changes |
| 3272 | Pick-up location |
| 3274 | Port of loading or airport of departure |
| 3280 | Delivery location |
| 3282 | Port of discharge or airport of destination |
| 3286 | Changes to dates/times |
| 3294 | Changes to the seals |
| 3306 | Entering or solving discrepancies |
| 3310 | Activities |
| 3320 | Use |
| 3330 | Prerequisites |
| 3367 | Order |
| 3399 | Forwarding Order |
| 3407 | Freight Order |
| 3413 | Features |
| 3435 | Activities |
| 3453 | Actions |
| 3459 | Use |
| 3467 | Prerequisites |
| 3501 | Features |
| 3544 | Activities |
| 3557 | Use |
| 3569 | Features |
| 3595 | Forwarding Settlement Documents |
| 3646 | Example |
| 3664 | More Information |
| 3670 | Use |
| 3676 | Prerequisites |
| 3695 | Integration |
| 3697 | Enterprise Services |
| 3701 | Process |
| 3751 | Use |
| 3763 | The weighing date and the weighing location |
| 3774 | VGM cut-off dates/times |
| 3792 | Prerequisites |
| 3814 | Order |
| 3820 | Process |
| 3879 | Use |
| 3885 | Prerequisites |
| 3891 | Freight Booking |
| 3899 | Features |
| 3901 | Capacity Management |
| 3909 | Entering Capacities |
| 3917 | Drawing MAWB Numbers |
| 3948 | Local carrier |
| 3950 | Purchasing organization |
| 3972 | Assigning documents to unit load devices |
| 3978 | Communicating with the warehouse |
| 4002 | More Information |
| 4006 | Co-Load |
| 4008 | Publication and Locking of Air Freight Bookings |
| 4017 | Nature of Goods |
| 4021 | Concept |
| 4027 | Co-load scenario |
| 4037 | Field Name |
| 4043 | Example |
| 4045 | Header Level |
| 4049 | Carrier |
| 4070 | Field Name |
| 4076 | Example |
| 4078 | Header Level |
| 4180 | Executing Carrier |
| 4221 | Field Name |
| 4227 | Example |
| 4229 | Header Level |
| 4339 | No./Global Carrier |
| 4366 | Field Name |
| 4372 | Example |
| 4374 | Header Level |
| 4454 | No./Global Carrier |
| 4492 | No./Global Carrier |
| 4525 | Field Name |
| 4531 | Example |
| 4533 | Header Level |
| 4541 | Export Organization |
| 4627 | Account |
| 4667 | Account |
| 4682 | Field Name |
| 4688 | Example |
| 4690 | Header Level |
| 4714 | XX_ABC_ATL |
| 4750 | Co-Load |
| 4756 | Use |
| 4762 | Features |
| 4764 | Air Cargo Security Check and Statuses |
| 4813 | Cargo Handover Party |
| 4833 | Shipper Known Long Enough |
| 4863 | Air Cargo Security Authorization Check |
| 4882 | More Information |
| 4888 | Configuration of Air Cargo Security |
| 4892 | Air Cargo Security Check |
| 4900 | Forwarding Order |
| 4906 | Freight Booking |
| 4912 | Freight Order |
| 4914 | Define Freight Order Types |
| 4918 | Air Cargo Security Statuses |
| 4924 | Security |
| 4940 | Air Cargo Security Status in Schedules |
| 4958 | Regulated Agent Code of LSP |
| 4972 | Cargo Handover Party |
| 4994 | Shipper Known Long Enough |
| 5004 | Security |
| 5006 | Define Offsets for Calculating |
| 5016 | Screening Methods |
| 5024 | Security |
| 5034 | Screening Exemptions |
| 5047 | Security |
| 5055 | Use |
| 5061 | Prerequisites |
| 5067 | Process |
| 5235 | Use |
| 5263 | Prerequisites |
| 5269 | Order |
| 5273 | Activities |
| 5344 | Use |
| 5360 | Prerequisites |
| 5366 | Freight Booking |
| 5382 | Process |
| 5390 | MAWB number |
| 5394 | Issuing carrier's agent |
| 5414 | Use |
| 5425 | Prerequisites |
| 5431 | General Settings |
| 5433 | Define Handling Codes . You can also specify here whether handling codes |
| 5443 | General Settings |
| 5447 | Features |
| 5468 | Manual entry |
| 5492 | Use |
| 5496 | Prerequisites |
| 5520 | Booking |
| 5536 | Loading type |
| 5547 | Service level |
| 5567 | Create |
| 5577 | Features |
| 5579 | Manual Publication |
| 5599 | Unrestricted visibility |
| 5605 | Restricted visibility |
| 5650 | More Information |
| 5660 | Use |
| 5670 | Freight terms |
| 5672 | Port of entry and exit |
| 5676 | Features |
| 5694 | Use |
| 5711 | Features |
| 5713 | Creation from an FCL Forwarding Order |
| 5733 | Creation for Consolidation of LCL Forwarding Orders |
| 5747 | Document |
| 5767 | Use |
| 5802 | Integration |
| 5808 | Prerequisites |
| 5816 | Freight Booking |
| 5818 | Define Freight Booking Types |
| 5826 | Applications |
| 5834 | PPF Settings |
| 5844 | Reusable Objects |
| 5854 | Example |
| 5866 | Use |
| 5889 | Features |
| 5891 | Supported Scenarios |
| 5947 | Internal Communication |
| 5974 | External Communication |
| 5992 | Export FWOs Created by Other Organizational Units |
| 6000 | A member of the import organizational unit directly creates an export FWO |
| 6026 | Forwarding Quotation |
| 6028 | Define Forwarding Quotation Types |
| 6063 | Basic Functions |
| 6091 | Define |
| 6095 | Manual Creation of Import Freight Bookings |
| 6099 | Customs Processing |
| 6109 | Use |
| 6119 | Prerequisites |
| 6137 | Forwarding Order |
| 6154 | Freight Booking |
| 6181 | Basic Functions |
| 6215 | Process |
| 6351 | Result |
| 6371 | Basic |
| 6373 | Functions |
| 6375 | Export/Import Processing |
| 6381 | Use |
| 6387 | Prerequisites |
| 6403 | Basic Functions |
| 6438 | Process |
| 6488 | Result |
| 6500 | Use |
| 6513 | Prerequisites |
| 6537 | Process |
| 6616 | Result |
| 6632 | Basic |
| 6634 | Functions |
| 6636 | Export/Import Processing |
| 6642 | Use |
| 6648 | Prerequisites |
| 6654 | Freight Booking |
| 6658 | Features |
| 6693 | Export/Import Processing |
| 6697 | Use |
| 6709 | Prerequisites |
| 6713 | Features |
| 6715 | Export Forwarding Order |
| 6725 | Export Freight Booking |
| 6737 | Import Freight Booking |
| 6743 | Import Forwarding Order |
| 6766 | Charges |
| 6774 | Settlement |
| 6786 | Example |
| 6800 | More Information |
| 6806 | Use |
| 6812 | Prerequisites |
| 6818 | Freight Booking |
| 6820 | Define Freight Booking Types |
| 6831 | Process |
| 6837 | Shipper, ship-to party, and carrier |
| 6843 | Number of containers |
| 6873 | More Information |
| 6879 | Use |
| 6897 | Prerequisites |
| 6901 | Features |
| 6903 | Export Forwarding Order |
| 6919 | Export Freight Booking |
| 6925 | Import Freight Booking |
| 6931 | Import Forwarding Order |
| 6937 | Charges |
| 6943 | Settlement |
| 6959 | Example |
| 6982 | More Information |
| 6988 | Use |
| 6994 | Prerequisites |
| 7000 | Freight Booking |
| 7002 | Define Freight Booking Types |
| 7006 | Process |
| 7012 | Shipper, ship-to party, and carrier |
| 7057 | More Information |
| 7073 | Prerequisites |
| 7081 | Booking |
| 7121 | Ocean Freight Bookings |
| 7138 | Container Units |
| 7156 | Resources |
| 7158 | General Settings |
| 7170 | Pick-Up Freight Orders and Delivery Freight Orders |
| 7176 | Define Transportation Mode |
| 7214 | Define |
| 7225 | Loading Cargo |
| 7229 | In the Load or Unload Freight Orders app |
| 7239 | Consignment Orders |
| 7247 | Automatic or Manual Creation of Consignments |
| 7261 | Create Consignment Order |
| 7275 | Port of Destination and Incoterms |
| 7297 | Handle Containers Left Behind at the Port |
| 7310 | Invoicing |
| 7316 | Message Exchange Between Shipper and Carrier |
| 7320 | Sending Container Units to (Pre-Carriage) Carrier |
| 7338 | Settings for Sending CU-Update Messages to (Pre-Carriage) Carrier |
| 7362 | Transportation Unit |
| 7374 | Checkout event is posted |
| 7427 | Identifying Locations by UN/LOCODES |
| 7439 | Update Port of Destination |
| 7466 | Sending ASN to Customer |
| 7490 | Related Information |
| 7494 | Consignment Order |
| 7502 | Advanced Shipping and Receiving |
| 7524 | Creating Ocean Freight Booking |
| 7559 | Creating Transportation Requirements |
| 7565 | Transportation Planning |
| 7585 | Performing Warehouse Activities |
| 7624 | In the Load or Unload Freight Orders app |
| 7630 | Via Radio Frequency (RF) in EWM |
| 7640 | Create Consignment Order |
| 7664 | Departure of the Vessel |
| 7710 | Reporting Arrival of Vessel |
| 7714 | Processing Delivery Freight Orders |
| 7720 | Create |
| 7728 | Related Information |
| 7746 | Prerequisites |
| 7754 | Booking |
| 7770 | Pick-Up Freight Orders and Delivery Freight Orders |
| 7803 | Consignment Orders for Carriers and Customers |
| 7809 | Carrier Plans Consignments on Flights |
| 7835 | Consignments Based on Top-Level Package |
| 7843 | Settings for Consignment Building on Top-Level Packages |
| 7851 | Automatic or Manual Creation of Consignments |
| 7886 | Air Freight Booking |
| 7896 | Document Errors |
| 7916 | Invoicing |
| 7920 | Message Exchange Between Shipper and Carrier |
| 7924 | Sending Consignments to the Carrier |
| 7930 | Settings for Sending Consignments to the Carrier |
| 7957 | Consignment Orders |
| 7969 | Adapter for Output Management |
| 7979 | Consignment Order |
| 8004 | Carrier number |
| 8018 | Update Messages |
| 8030 | Identifying Locations by IATA Codes |
| 8057 | Update Port of Destination |
| 8063 | Sending ASN to Customer |
| 8091 | Related Information |
| 8095 | Consignment Order |
| 8097 | Cargo Left Behind at Port/Airport |
| 8103 | Advanced Shipping and Receiving |
| 8134 | Creating Transportation Requirements |
| 8140 | Performing Warehouse Activities |
| 8160 | New |
| 8180 | Build Local Consignment Orders |
| 8184 | Create |
| 8265 | Departure of the Airplane from the Port of Loading |
| 8271 | Reporting Arrival of Airplane |
| 8275 | Processing Delivery Freight Orders |
| 8289 | Related Information |
| 8300 | Cargo Left Behind at Port/Airport |
| 8308 | Prerequisites |
| 8318 | Settings |
| 8326 | Freight Booking |
| 8336 | Freight Booking |
| 8344 | Activating the Left Behind Function |
| 8366 | Document Errors |
| 8401 | Invoicing Blocks |
| 8431 | Not Activating the Left Behind Function |
| 8468 | Example |
| 8492 | Transportation Unit |
| 8500 | Definition |
| 8504 | A trailer and its load |
| 8508 | A container and its load |
| 8512 | Use |
| 8532 | Management |
| 8534 | Transportation Unit |
| 8546 | Package Unit |
| 8552 | Definition |
| 8556 | Use |
| 8564 | Transportation Unit |
| 8576 | Structure |
| 8580 | General data such as locations and dates |
| 8590 | Transportation stages |
| 8598 | Transportation stage types |
| 8604 | Freight |
| 8620 | Overview |
| 8626 | Route the trailer will take |
| 8648 | More Information |
| 8656 | Triangulation |
| 8660 | Use |
| 8664 | Prerequisites |
| 8676 | Features |
| 8686 | Coupling not possible |
| 8690 | Coupling possible |
| 8696 | Coupling possible only during pickup or delivery |
| 8704 | Only trailer swap possible |
| 8712 | Activities |
| 8729 | Example: Trailer Swap |
| 8735 | Document |
| 8739 | Creation type |
| 8747 | C-B-A |
| 8761 | Document |
| 8775 | A-B-A |
| 8794 | Definition |
| 8798 | Use |
| 8839 | Structure |
| 8843 | General Data |
| 8849 | Number of railcars |
| 8853 | Resources/Equipment |
| 8859 | Equipment group and equipment type |
| 8863 | Seal information |
| 8869 | Applying Default Routes |
| 8877 | Triangulation |
| 8883 | Definition |
| 8889 | Use |
| 8932 | Structure |
| 8936 | General Data |
| 8942 | Number of containers |
| 8944 | Number of assigned freight documents |
| 8948 | Freight |
| 8950 | Container Details |
| 8952 | Transportation unit resource |
| 8958 | Equipment group and equipment type |
| 8968 | Equipment |
| 8972 | Document references |
| 8980 | Restrictions |
| 8996 | More Information |
| 9000 | Package Unit |
| 9010 | Prerequisites |
| 9014 | Use |
| 9020 | Assignment to Other Transportation Units |
| 9038 | Assignment of a Freight Unit to Several Package Units |
| 9071 | Display the Exact Position of Products in a Package |
| 9083 | Integration with Material Master Data |
| 9091 | Creating a Package Unit |
| 9095 | Creating a Package Unit |
| 9103 | Prerequisites |
| 9109 | Whether package building has been activated for this document type |
| 9117 | Transportation Unit |
| 9125 | Freight Order |
| 9137 | Features |
| 9139 | Manual Creation of a Package Unit |
| 9159 | Linear with Distribution |
| 9175 | Creation of a Package Unit from a Forwarding Order |
| 9181 | Creation of Package Units from a Freight Order |
| 9248 | Manual and Automatic Creation of a Package Unit Using the Transportation Cockpit |
| 9256 | Displaying the Origin of a Package Unit |
| 9263 | Deconsolidation |
| 9285 | Prerequisites |
| 9322 | Transportation Unit |
| 9330 | Freight Order |
| 9366 | Process |
| 9433 | Create Package Units . Alternatively, as described |
| 9490 | Planning of Main Carriage Stage |
| 9508 | Set Load |
| 9522 | Related Information |
| 9526 | Planning with Distribution Stops |
| 9537 | Load Plan Status Changes |
| 9545 | Initial situation |
| 9577 | Not Relevant |
| 9581 | Package building |
| 9601 | Planned |
| 9603 | Not Planned |
| 9607 | Planned |
| 9611 | Not Planned |
| 9615 | Planned |
| 9621 | Planned |
| 9625 | Planned |
| 9629 | Planned |
| 9631 | Not Relevant |
| 9653 | Planned |
| 9655 | Not Relevant |
| 9682 | Planned |
| 9686 | Planned |
| 9688 | Not Relevant |
| 9736 | Not Relevant |
| 9754 | Planned |
| 9762 | Planned |
| 9770 | Planned |
| 9774 | Not Relevant |
| 9776 | Related Information |
| 9780 | Planned |
| 9792 | Not Relevant |
| 9794 | Use of Normalized Quantities and Capacities |
| 9811 | Prerequisites |
| 9827 | Freight Unit |
| 9833 | Transportation Unit |
| 9839 | Freight Order |
| 9841 | Define Freight Order Types |
| 9849 | Normalized Quantities |
| 9881 | Schedule |
| 9895 | Create |
| 9911 | Normalized Quantities |
| 9938 | Settings |
| 9958 | Gantt Chart |
| 9960 | Define Field Lists |
| 9976 | Order |
| 9986 | Features |
| 9988 | Determination of Normalized Quantity |
| 10041 | Determination of Additional Normalized Quantity |
| 10057 | Packaging Material Overview |
| 10081 | Normalized Loading Space Capacity and Calculation of Maximum Utilization |
| 10097 | Check Normalized Quantities in Documents |
| 10109 | Example |
| 10130 | Use |
| 10134 | Prerequisites |
| 10142 | Transportation Unit |
| 10146 | Features |
| 10152 | Manual creation in the transportation cockpit |
| 10168 | Create Package Unit |
| 10174 | Automatic creation from a forwarding order |
| 10195 | Manual creation by copying |
| 10211 | Defining Logistical Processing |
| 10215 | Route |
| 10221 | Trailer unit |
| 10229 | Railcar unit |
| 10237 | Container unit and package unit |
| 10251 | Trailer units |
| 10272 | More Information |
| 10278 | Creating a Package Unit |
| 10282 | Use |
| 10292 | Features |
| 10294 | Forwarding order already contains railcar item |
| 10337 | Definition |
| 10343 | Use |
| 10349 | Calculate charges for the services |
| 10378 | Freight Order Management |
| 10384 | Service Order |
| 10396 | Structure |
| 10426 | Notes |
| 10428 | Attachments |
| 10432 | Administrative data |
| 10434 | Output management information |
| 10443 | Service Order Types, Service Item Types, and Service Types |
| 10451 | Service Order |
| 10475 | Service Items |
| 10479 | Use |
| 10483 | Prerequisites |
| 10507 | Freight Booking |
| 10515 | Freight Order |
| 10523 | Features |
| 10525 | Creation of Service Orders |
| 10546 | Editing and Displaying of Service Orders |
| 10568 | Distribution of Costs |
| 10580 | Use |
| 10584 | Prerequisites |
| 10594 | Process |
| 10629 | Service order type |
| 10633 | Service order number |
| 10673 | Consignment Order |
| 10687 | Use |
| 10717 | Define |
| 10721 | Consignment Order |
| 10739 | Consignment Order Creation Based on Top-Level Packages |
| 10755 | BAdI to Determine Consignment Order Type |
| 10785 | Structure |
| 10805 | Creating a Consignment Order |
| 10817 | Worklist and Search Options for Consignment Orders |
| 10823 | Related Information |
| 10827 | Automatic Consignment Building |
| 10833 | Creation and Editing of a Consignment Order |
| 10841 | Prerequisites |
| 10847 | Management |
| 10849 | Consignment Order |
| 10853 | Creation Options |
| 10864 | Manual creation |
| 10870 | Creation from a freight order |
| 10882 | Freight Order |
| 10886 | Creation using an inbound message |
| 10906 | Creation during manual planning using the transportation cockpit |
| 10912 | Creation by copying |
| 10930 | Automatic building for freight units of a freight order |
| 10940 | Process |
| 10961 | Notes |
| 11070 | Consignment Order |
| 11076 | Automatic Consignment Building |
| 11084 | Features |
| 11098 | Consignment Building Profile |
| 11153 | Freight Order Type |
| 11157 | Creating Local Consignment Orders and Consignment Order Documents |
| 11185 | Automatic building when the freight order is created and saved |
| 11193 | Manual triggering with subsequent automatic update |
| 11224 | Creating consignment order documents |
| 11226 | Manual triggering of document creation for all consignment orders |
| 11244 | Automatic document creation based on the profile settings |
| 11266 | Consignment Order |
| 11270 | Consignment Orders for Customer Pick-Up |
| 11280 | Prerequisites |
| 11286 | Integration |
| 11290 | Internal TM |
| 11292 | Component Integration |
| 11325 | Process |
| 11354 | AI-Assisted Goods Receipt Analysis |
| 11390 | Related Information |
| 11396 | Working with Attachments |
| 11398 | Automated Processing of Delivery Document Data |
| 11421 | Prerequisites |
| 11443 | Extraction |
| 11449 | Process |
| 11451 | Overall Process |
| 11476 | Document Errors |
| 11496 | Example |
| 11557 | Related Information |
| 11563 | Error Handling |
| 11569 | Error Handling |
| 11581 | Connection Errors |
| 11593 | Extraction Errors |
| 11605 | Processing Errors |
| 11628 | Item Mismatch |
| 11634 | Product ID |
| 11640 | External delivery note's item ID |
| 11648 | Quantity Mismatch |
| 11662 | Header Data Mismatch |
| 11676 | Related Information |
| 11683 | Information Extraction |
| 11695 | Example |
| 11705 | Worklist |
| 11713 | Not Started |
| 11725 | Unified Package Building Engines |
| 11727 | Application Log for Document Information Extraction |
| 11731 | Enable Log |
| 11741 | Check Log |
| 11753 | Object: /SCMTMS/GENAI |
| 11762 | Sub Object: TMDOX |
| 11768 | Additional Business Document Attributes in FOM |
| 11774 | Items |
| 11776 | Transportation Stops |
| 11790 | Use of Seals |
| 11802 | Use |
| 11814 | Features |
| 11818 | Capacity |
| 11820 | Vehicle resource |
| 11835 | Container |
| 11841 | Container |
| 11853 | Packaging material |
| 11857 | Product |
| 11865 | Quantities |
| 11873 | Discrepancies |
| 11887 | Equipment |
| 11891 | Overview |
| 11895 | Stages |
| 11910 | Item Types |
| 11916 | Management |
| 11934 | Freight Order |
| 11940 | Freight Booking |
| 11946 | Freight Unit |
| 11952 | Transportation Unit |
| 11958 | Consignment Order |
| 11962 | Multi-Items |
| 11972 | Container |
| 11976 | Multiple railcars of the same category |
| 11986 | Multiple locomotives in a train |
| 12021 | Related Information |
| 12025 | Use of Auxiliary Packaging Materials |
| 12033 | Prerequisites |
| 12047 | Product |
| 12063 | Define Item |
| 12077 | Define |
| 12081 | Features |
| 12114 | Items |
| 12120 | Definition |
| 12128 | The time at which this action is performed |
| 12138 | Current Transportation Stop |
| 12175 | Items tab page |
| 12194 | Execution activities |
| 12200 | Structure |
| 12206 | Stop type |
| 12212 | Fixing |
| 12222 | Assignment to capacity |
| 12230 | Use |
| 12243 | Dates/Times |
| 12251 | Meaning |
| 12267 | Planned departure and arrival dates/times |
| 12271 | Loading/coupling times |
| 12301 | Times for preparation and finalization |
| 12307 | Availability dates/times |
| 12329 | Dates/times confirmed by carrier |
| 12339 | Transportation Stops |
| 12341 | Deviating Business Partner Addresses |
| 12351 | Use |
| 12381 | Features |
| 12385 | Name |
| 12387 | Address |
| 12395 | Propagation |
| 12434 | Print Documents |
| 12446 | Activities |
| 12468 | International Address Versions |
| 12472 | Features |
| 12488 | Activities |
| 12494 | International Settings |
| 12511 | Define Business Partner |
| 12515 | Define Location |
| 12525 | Transportation Distance and Transportation Duration |
| 12537 | Field |
| 12541 | Level |
| 12543 | Definition |
| 12551 | Net duration |
| 12553 | Transportation stage level |
| 12567 | Header level |
| 12601 | Display Format |
| 12619 | Use |
| 12635 | Prerequisites |
| 12641 | Freight orders |
| 12645 | Transportation units |
| 12653 | Freight Order |
| 12659 | Freight Booking |
| 12665 | Transportation Unit |
| 12671 | Freight Unit |
| 12675 | Features |
| 12681 | Add a transportation stage |
| 12702 | Interaction with Default Route and Schedule |
| 12712 | Locations are not identical or the default route contains a transportation zone |
| 12726 | Transportation distance or duration is identical |
| 12736 | Default route or schedule do not contain any values |
| 12754 | More Information |
| 12762 | Use |
| 12769 | Quantities |
| 12784 | If you set a business document item to Quantity Received as Planned |
| 12790 | Integration with SAP Event Management |
| 12794 | Level |
| 12882 | Package |
| 12924 | Product |
| 12990 | Capacities |
| 13004 | Utilization |
| 13034 | More Information |
| 13036 | Capacities and Utilization in Rail Freight Orders |
| 13045 | Example of Quantity Totaling |
| 13049 | Quantity totaling |
| 13065 | Level |
| 13071 | Net Weight |
| 13110 | Net Weight |
| 13192 | Use |
| 13204 | Prerequisites |
| 13212 | Features |
| 13230 | Planning and execution block for freight units |
| 13275 | More Information |
| 13279 | Resolution of Discrepancies |
| 13285 | Use |
| 13301 | Prerequisites |
| 13316 | Features |
| 13348 | Activities |
| 13356 | Other Discrepancies |
| 13360 | Resolution of Discrepancies |
| 13366 | Use |
| 13389 | Prerequisites |
| 13397 | Features |
| 13401 | Discrepancy type |
| 13405 | Discrepancy date |
| 13415 | Activities |
| 13423 | Quantity Discrepancies |
| 13427 | Resolution of Discrepancies |
| 13433 | Use |
| 13443 | Prerequisites |
| 13451 | Activities |
| 13499 | Other Discrepancies |
| 13505 | Outer Volume |
| 13511 | Use |
| 13517 | During the manual creation of package units |
| 13546 | Display of Outer Volume |
| 13568 | Packaging Material Data |
| 13582 | Utilization |
| 13590 | Prerequisites |
| 13596 | Resources |
| 13610 | Resources |
| 13622 | Use |
| 13632 | Utilization |
| 13636 | Utilization with complete context |
| 13655 | General Data |
| 13663 | Overview |
| 13669 | Calculation of Utilization |
| 13687 | Remaining capacity |
| 13710 | Use |
| 13714 | Distributing Freight Units |
| 13726 | Splitting Partial Quantities |
| 13736 | Deleting Items |
| 13740 | Features |
| 13742 | Distributing Freight Units |
| 13779 | Splitting Partial Quantities |
| 13813 | Deleting Items |
| 13821 | Items do not belong to a freight unit |
| 13825 | Items belong to a freight unit |
| 13831 | Delete individual items of a freight unit |
| 13868 | Activities |
| 13888 | Use |
| 13894 | Features |
| 13918 | Use |
| 13931 | Insurable value |
| 13933 | Goods value for customs |
| 13939 | Prerequisites |
| 13945 | Features |
| 13959 | Use |
| 13963 | Prerequisites |
| 13967 | Relationships |
| 13981 | Business Partners |
| 13985 | Features |
| 14007 | A_EU |
| 14033 | Communication Party |
| 14083 | Company Codes |
| 14093 | Prerequisites |
| 14107 | Freight Order |
| 14113 | Freight Booking |
| 14119 | Service Order |
| 14125 | Consignment Order |
| 14129 | Features |
| 14131 | Procuring Company Code |
| 14155 | Paying Company Code |
| 14172 | Intercompany settlement is allowed |
| 14182 | Intercompany settlement is not allowed |
| 14188 | Company Codes in the Transportation Cockpit |
| 14206 | Use |
| 14214 | Features |
| 14216 | Document Check |
| 14228 | Resource check |
| 14238 | Check for Cross-Document Time Conflicts |
| 14263 | Incompatibility Check |
| 14267 | Dangerous Goods Check |
| 14273 | Capacity Check |
| 14277 | Resource Usage Check |
| 14285 | Downtimes |
| 14309 | Check Readiness for Transportation Execution |
| 14324 | That there are no execution blocks |
| 14326 | That the load plan for multi-assigned package units has been finalized |
| 14338 | Whether a driver has been assigned |
| 14348 | Air Cargo Security Check |
| 14352 | Activities |
| 14356 | Related Information |
| 14362 | Use |
| 14366 | Prerequisites |
| 14372 | Features |
| 14411 | Assignment of schedules at transportation stage level |
| 14423 | Activities |
| 14439 | Transportation cockpit |
| 14445 | Use |
| 14453 | Shipper |
| 14464 | Customs |
| 14476 | Features |
| 14480 | Seal numbers |
| 14486 | The partner who seals and unseals |
| 14494 | Activities |
| 14500 | Use |
| 14506 | Prerequisites |
| 14520 | EQUI for equipment |
| 14537 | LSO for the display of load plans |
| 14551 | Features |
| 14557 | Activities |
| 14571 | More Information |
| 14577 | Use |
| 14583 | Prerequisites |
| 14610 | Features |
| 14626 | Use of Batches and Serial Numbers |
| 14638 | Batch Management |
| 14654 | Display |
| 14660 | Serial Numbers |
| 14670 | Basics |
| 14672 | Serial Numbers |
| 14678 | Use |
| 14701 | Features |
| 14705 | Status |
| 14707 | Status Values |
| 14713 | New |
| 14719 | Canceled |
| 14733 | Not planned |
| 14737 | Planned |
| 14743 | Status |
| 14749 | Freight unit |
| 14755 | Freight order |
| 14763 | No Subcontracting Result |
| 14771 | Sent |
| 14777 | No Confirmation Yet |
| 14785 | Confirmed |
| 14789 | Update Sent, No Confirmation Yet |
| 14798 | Status |
| 14802 | Status Values |
| 14806 | Status |
| 14814 | Published |
| 14818 | Completed |
| 14836 | Canceled by Shipper |
| 14844 | Pending |
| 14860 | Delivered |
| 14868 | Freight unit |
| 14872 | Cargo receipt status |
| 14881 | Status |
| 14883 | Status Values |
| 14891 | Status |
| 14893 | Freight order |
| 14899 | Freight unit |
| 14911 | Canceled |
| 14929 | Freight order |
| 14933 | Freight booking |
| 14937 | Transportation unit |
| 14941 | Consignment order |
| 14947 | Not Loaded |
| 14951 | Loaded |
| 14985 | Freight booking |
| 14991 | Cargo Unloaded |
| 15000 | Status |
| 15002 | Status Values |
| 15006 | Status |
| 15014 | Not Uncoupled |
| 15022 | Partially Uncoupled |
| 15028 | Uncoupled |
| 15032 | Uncoupled |
| 15040 | Not Coupled |
| 15048 | Partially Coupled |
| 15056 | Coupled |
| 15062 | Cargo Loaded/Coupled |
| 15066 | Not Planned |
| 15084 | Consignment order |
| 15090 | Freight order |
| 15101 | Status |
| 15103 | Status Values |
| 15115 | Not Sent |
| 15119 | Status |
| 15127 | Freight order |
| 15133 | Sent |
| 15137 | Received |
| 15139 | Cancellation Requested |
| 15151 | Publishing status |
| 15157 | Finalized |
| 15167 | Freight booking |
| 15175 | Shipped on Board |
| 15183 | Uplift Confirmed |
| 15209 | Delivered |
| 15236 | Status |
| 15238 | Status Values |
| 15254 | Status |
| 15260 | Service order |
| 15266 | Freight order |
| 15274 | Transmission Successful |
| 15284 | Freight order |
| 15294 | Freight Order |
| 15298 | Freight Booking |
| 15302 | Not Yet Checked |
| 15310 | Traffic Light |
| 15322 | Not Archived |
| 15326 | Archived |
| 15328 | Fixing of Business Documents |
| 15336 | Freight unit |
| 15338 | Transportation unit |
| 15365 | More Information |
| 15377 | Use |
| 15383 | Features |
| 15387 | Life Cycle Status |
| 15391 | New |
| 15395 | In Process |
| 15405 | Complete |
| 15413 | Canceled |
| 15419 | Driver Assignment Status |
| 15436 | Not Relevant |
| 15440 | Underassigned |
| 15444 | Fully Assigned |
| 15448 | Overassigned |
| 15452 | Planning Status |
| 15460 | Not Planned |
| 15464 | Partially Planned |
| 15468 | Planned |
| 15472 | Not Ready for Planning |
| 15476 | Not Published |
| 15484 | Unplanned |
| 15488 | Planned |
| 15492 | Planned, Conflict Between FU and Freight Order/Booking Times |
| 15505 | Not Ready for Planning |
| 15511 | Subcontracting Status |
| 15519 | No Subcontracting Result |
| 15523 | In Tendering |
| 15527 | Carrier Assigned |
| 15531 | Sent |
| 15537 | Changed After Sending |
| 15543 | Changes to dates/times |
| 15551 | Confirmation Status |
| 15561 | No Confirmation Yet |
| 15565 | Invalid Confirmation Received |
| 15569 | Rejected |
| 15580 | Confirmed |
| 15584 | Confirmed with Changes |
| 15588 | Update Sent, No Confirmation Yet |
| 15592 | Document Changed After Confirmation |
| 15596 | Document Changed After Rejection |
| 15600 | Tendering Status |
| 15610 | Not Published |
| 15616 | Published |
| 15622 | Review Required |
| 15626 | Completed |
| 15634 | Not Sent |
| 15638 | Open |
| 15644 | Closed |
| 15657 | Omitted |
| 15665 | Draft |
| 15671 | Sent |
| 15679 | Not Started |
| 15685 | In Process |
| 15689 | Completed |
| 15695 | Omitted |
| 15699 | Booking Confirmation Status |
| 15705 | Not Sent to Carrier |
| 15709 | Sent to Carrier |
| 15713 | Rejected by Carrier |
| 15717 | Confirmed by Carrier |
| 15721 | Canceled by Shipper |
| 15732 | Partially Confirmed by Carrier |
| 15736 | Shipping Instruction Sent to Carrier |
| 15740 | Acknowledged by Carrier, Confirmation Is Pending |
| 15744 | Confirmed by Carrier with Deviations |
| 15748 | Canceled by Shipper and Acknowledged by Carrier |
| 15752 | Cargo Receipt Status |
| 15762 | Missing Cargo |
| 15772 | On Hand |
| 15782 | Shipped |
| 15788 | Delivered |
| 15792 | Delivery Failed |
| 15831 | Execution Status |
| 15879 | In Execution |
| 15894 | Executed |
| 15902 | Interrupted |
| 15906 | Canceled |
| 15910 | Not Relevant |
| 15916 | Handling Execution Status |
| 15936 | On stop level |
| 15960 | Date/time when the status was set |
| 15977 | Not Determined |
| 15983 | Not Unloaded |
| 15987 | Unloaded |
| 15995 | Not Loaded |
| 15999 | Loaded |
| 16007 | Not Coupled |
| 16011 | Coupled |
| 16015 | Not Uncoupled |
| 16019 | Uncoupled |
| 16025 | Not Determined |
| 16033 | Cargo Ready for Loading |
| 16052 | Arrived |
| 16098 | Unloaded |
| 16108 | Not Unloaded |
| 16112 | Not Loaded |
| 16116 | Loaded |
| 16157 | Departed |
| 16173 | Cargo Execution Status |
| 16183 | Not Determined |
| 16189 | Cargo Not Unloaded |
| 16193 | Cargo Partially Unloaded |
| 16197 | Cargo Unloaded |
| 16201 | Cargo Not Loaded |
| 16205 | Cargo Partially Loaded |
| 16216 | Cargo Loaded |
| 16232 | Load Plan Status and Unload Plan Status |
| 16258 | Not Planned |
| 16262 | Not Relevant |
| 16266 | Invalidated |
| 16272 | Planned |
| 16276 | Finalized |
| 16307 | Load Plan Item Status and Unload Plan Item Status |
| 16321 | Packaging not Relevant |
| 16325 | Transmission-to-EWM Status |
| 16339 | Not Sent |
| 16343 | Sent |
| 16347 | Partially Received |
| 16353 | Received |
| 16357 | Cancellation Requested |
| 16361 | Cancellation Confirmed |
| 16374 | Not Sent |
| 16378 | Partially Sent |
| 16382 | Sent |
| 16386 | Partially Received |
| 16390 | Received |
| 16394 | Cancellation Requested |
| 16398 | Cancellation of TM Document Requested |
| 16402 | Cancellation Confirmed |
| 16406 | Publishing Status |
| 16412 | Not Published |
| 16416 | Published |
| 16420 | Waybill/Bill of Lading Finalized Status |
| 16426 | Not Finalized |
| 16430 | Finalized |
| 16447 | Shipped-on-Board Status |
| 16457 | Not Shipped on Board |
| 16469 | Uplift Confirmation Status |
| 16479 | Uplift Not Confirmed |
| 16483 | Uplift Confirmed |
| 16491 | Master-Bill-of-Lading Status |
| 16507 | Manifest Status |
| 16520 | Manifest Not Created |
| 16524 | Manifest Created |
| 16528 | Delivery Status |
| 16542 | Not Delivered |
| 16546 | Partially Delivered |
| 16550 | Delivered |
| 16554 | Transmission-to-ERP Status |
| 16568 | New - Not Yet Transmitted |
| 16572 | Initial Transmission Started, Not Yet Confirmed by ERP |
| 16578 | Transmission Successful |
| 16589 | Retransmitted after Changes in TM, Not Yet Confirmed by ERP |
| 16595 | Invoicing Status |
| 16603 | Not Invoiced |
| 16607 | Partially Invoiced |
| 16611 | Completely Invoiced |
| 16615 | Over-Invoiced |
| 16619 | Not Up-to-Date |
| 16635 | Schedule Data Status |
| 16641 | Data Is Up-to-Date |
| 16645 | Data Is Not Up-to-Date |
| 16649 | Document Check Status |
| 16662 | Last Check with Errors |
| 16666 | Last Check Without Errors or Warnings |
| 16670 | Last Check with Warnings |
| 16674 | Not Yet Checked |
| 16678 | Cross-Document Check Status |
| 16702 | Not Yet Checked |
| 16706 | Archiving Status |
| 16710 | Not Archived |
| 16714 | Archiving in Process |
| 16718 | Archived |
| 16724 | More Information |
| 16741 | Use |
| 16747 | Features |
| 16749 | Handling Execution Status on Stop Level and Item Level |
| 16755 | Loaded |
| 16759 | Partially Loaded |
| 16767 | Unloaded |
| 16771 | Partially Unloaded |
| 16783 | Load Plan Status on Item Level and Load Plan Status on Stop Level |
| 16789 | Handling Execution Status on Stop Level and Execution Status |
| 16810 | Transportation Stops |
| 16815 | Use |
| 16841 | Features |
| 16843 | Handling Execution Status and Cargo Receipt Status |
| 16896 | Transportation Stops |
| 16900 | Use |
| 16910 | Manually |
| 16912 | Prerequisites |
| 16918 | General Settings |
| 16930 | Management |
| 16934 | Features |
| 16938 | Manual setting of blocks |
| 16948 | Automatic setting of blocks |
| 16969 | The type and reason for the block |
| 16971 | The date on which the block was created and the person responsible |
| 16977 | Removal of blocks |
| 16995 | More Information |
| 17001 | Use |
| 17013 | Container units |
| 17017 | Features |
| 17056 | Use |
| 17080 | Prerequisites |
| 17100 | Calculation Method at Stage Level |
| 17191 | Example |
| 17218 | Calculation Method at Freight Unit Item Level |
| 17256 | Use |
| 17283 | Features |
| 17289 | Mix tendering types |
| 17305 | Tendering to one or more carriers |
| 17309 | Background execution of tendering |
| 17339 | Charge Management to calculate price limits |
| 17345 | Freight agreements |
| 17351 | Use |
| 17359 | Prerequisites |
| 17367 | Freight Order |
| 17369 | Define Freight Order Types |
| 17380 | Freight Booking |
| 17382 | Define Freight Booking Types |
| 17390 | Basic Functions |
| 17404 | Process |
| 17416 | Communication settings |
| 17420 | Default settings |
| 17426 | Tendering |
| 17450 | The value of the attribute you've defined with the data access definition |
| 17471 | Definition |
| 17477 | Use |
| 17493 | Create Tendering |
| 17505 | Structure |
| 17509 | Tendering step |
| 17513 | Tendering type |
| 17525 | Tendering process mode |
| 17535 | Carrier |
| 17550 | Get Carriers from Ranking List |
| 17558 | Relative price limit |
| 17562 | Maximum response duration |
| 17566 | Manual evaluation |
| 17570 | Price details |
| 17574 | Price Limit Only |
| 17584 | Visibility settings |
| 17588 | Communication Channels in Tendering |
| 17592 | Communication using e-mail |
| 17598 | Enter a valid e-mail address for the contact person |
| 17606 | Tendering |
| 17610 | Communication using B2B messages |
| 17625 | Use |
| 17629 | Prerequisites |
| 17635 | Carriers |
| 17639 | Locations |
| 17645 | Features |
| 17651 | More Information |
| 17661 | Change Controller in Tendering |
| 17675 | Stop current tendering |
| 17690 | Freight Order |
| 17696 | Freight Order |
| 17702 | Freight Booking |
| 17708 | Use |
| 17718 | The default freight agreement |
| 17726 | Price Limit Only |
| 17748 | Prerequisites |
| 17752 | Activities |
| 17781 | Use |
| 17797 | Accept or reject a freight RFQ |
| 17801 | Propose a price, if allowed by the visibility settings of the tendering process |
| 17813 | Prerequisites |
| 17819 | Text content for e-mails |
| 17823 | Keywords to enable the system to process FQs received by e-mail |
| 17827 | Tendering |
| 17835 | Tendering |
| 17850 | Communication Settings |
| 17860 | Features |
| 17876 | Tendering |
| 17886 | More Information |
| 17890 | Carrier Notification Process Management |
| 17894 | Library |
| 17902 | Connectivity |
| 17918 | Connectivity |
| 17922 | Telephony |
| 17934 | Use |
| 17952 | Prerequisites |
| 17960 | Tendering |
| 17970 | Features |
| 17976 | Tendering |
| 17980 | Tendering |
| 18004 | Tendering |
| 18013 | More Information |
| 18015 | Communication Channels in Tendering |
| 18019 | Library |
| 18027 | Connectivity |
| 18043 | Connectivity |
| 18047 | Telephony |
| 18057 | Creation of a Tendering Plan |
| 18065 | Use |
| 18079 | Prerequisites |
| 18093 | Process |
| 18115 | Result |
| 18121 | More Information |
| 18127 | Tendering |
| 18135 | Freight Order |
| 18150 | Freight Booking |
| 18158 | Use |
| 18166 | Example |
| 18178 | Definition |
| 18182 | Use |
| 18200 | Definition |
| 18210 | Use |
| 18236 | Visibility Settings |
| 18258 | Definition |
| 18266 | Use |
| 18281 | Use |
| 18307 | Prerequisites |
| 18315 | Process |
| 18336 | Tendering type |
| 18340 | Response time |
| 18355 | One or more carriers |
| 18377 | Use |
| 18381 | Features |
| 18391 | Communication Channel |
| 18401 | Notification e-mail |
| 18407 | Freight RFQ by B2B message |
| 18415 | Notification e-mail |
| 18428 | Communication Channel |
| 18440 | Cancellation |
| 18444 | Cancellation |
| 18446 | Notification e-mail |
| 18462 | FQ by B2B message |
| 18474 | Tendering Alerts |
| 18486 | Define |
| 18492 | Use |
| 18498 | Prerequisites |
| 18508 | Process |
| 18530 | Freight Order |
| 18538 | Freight Booking |
| 18550 | Use |
| 18560 | Prerequisites |
| 18572 | Features |
| 18576 | Accept or reject freight RFQs |
| 18613 | More Information |
| 18619 | Tendering |
| 18625 | Use |
| 18641 | RFQs |
| 18645 | Lowest price |
| 18655 | Fastest carrier |
| 18663 | Prerequisites |
| 18671 | Tendering |
| 18689 | S_BTCH_NAM |
| 18693 | Process |
| 18707 | Update of a Freight Order or Freight Booking |
| 18719 | Submitted price |
| 18727 | Use |
| 18750 | Process |
| 18755 | Messages |
| 18767 | Prerequisites |
| 18775 | Freight Order |
| 18783 | Consignment Order |
| 18787 | Separate or Combined Inbound Messages |
| 18863 | Creating Consignment Orders |
| 18883 | A combination of material number and vendor |
| 18887 | No Matching Freight Units Found |
| 18895 | Updating Consignment Orders |
| 18910 | Update product or package data |
| 18930 | Fixing of Packages |
| 18960 | Handling of Updates by Inbound Messages After Manual Changes |
| 18968 | Freight Order |
| 18972 | Consignment Order |
| 18976 | Displaying External ID Numbers |
| 18984 | External package ID |
| 18992 | Related Information |
| 18996 | Correction of Errors in Business Documents |
| 19002 | Prerequisites |
| 19010 | Freight Order |
| 19016 | Consignment Order |
| 19022 | Freight Booking |
| 19032 | Features |
| 19044 | Master data error |
| 19058 | Freight Order Management |
| 19062 | Correcting Master Data Errors |
| 19070 | Locations |
| 19079 | Business partners |
| 19117 | Correcting Reference Errors |
| 19125 | Automatic Correction of Document Errors |
| 19137 | Automatic Correction of Reference Errors in Related Documents |
| 19147 | Blocking the Document |
| 19168 | Consignment Order |
| 19172 | Example Checks to Find Errors in Business Documents |
| 19180 | Overdelivery of Quantity |
| 19186 | Prerequisites |
| 19196 | Order |
| 19200 | Consignment Order |
| 19202 | Define Consignment Order Types |
| 19206 | Features |
| 19269 | Features |
| 19289 | Package-Related Errors |
| 19295 | Prerequisites |
| 19305 | Features |
| 19352 | Features |
| 19382 | Features |
| 19396 | Goods Movement Posting |
| 19409 | Freight Unit Building |
| 19421 | Delivery update from TM to LE |
| 19427 | Delivery Update from EWM to TM |
| 19437 | Features |
| 19467 | Related Information |
| 19471 | Intelligent Resolution of Document Errors |
| 19484 | Prerequisites |
| 19496 | Define |
| 19504 | Error History |
| 19510 | Features |
| 19534 | Additional Information About Error Resolution |
| 19544 | Clean-Up Report |
| 19552 | Web Services for External Planning Scenarios |
| 19571 | Prerequisites |
| 19589 | Freight Order |
| 19611 | Process |
| 19642 | Phase |
| 19646 | Details |
| 19648 | Web Service |
| 19708 | Sample XML Payloads |
| 19801 | More Information |
| 19807 | Related Information |
| 19813 | Execution of Freight Documents |
| 19833 | Event Profiles |
| 19841 | Handling of Skipped and Recalled Events |
| 19853 | Checks and Post Processing |
| 19863 | Propagation to Related Documents |
| 19877 | Related Information |
| 19881 | Event Profiles |
| 19885 | Prerequisites |
| 19889 | Integration |
| 19893 | Processes and Documents |
| 19899 | Execution Settings |
| 19909 | Use |
| 19946 | Mandatory: Event is derived and reported automatically |
| 19962 | Optional: Report event manually or via a service |
| 19984 | Propagation of Events |
| 20019 | Exceptions to Event Propagation |
| 20037 | Integration |
| 20061 | Event Propagation for Bookings |
| 20075 | Aggregation of Events |
| 20127 | Checks for Handling Execution Status-Relevant Events |
| 20141 | Events Requiring Different or Extra Checks |
| 20145 | Cargo Ready for Loading |
| 20151 | Unload end for item |
| 20180 | Load end for item |
| 20206 | Load end for stop |
| 20245 | Execution Settings |
| 20247 | Define Event Profiles . For more |
| 20253 | Recalling Events |
| 20277 | Processing of Customs-Relevant Documents |
| 20297 | Follow-Up Processes |
| 20301 | By Freight Order Type |
| 20324 | Consignment Orders |
| 20332 | Advanced Shipping and Receiving |
| 20376 | Use |
| 20403 | Features |
| 20470 | Freight unit 2 goes from A to B |
| 20487 | Use |
| 20493 | Create |
| 20495 | Freight Settlement Document |
| 20503 | Condition |
| 20507 | Your Response |
| 20513 | Subcontracting |
| 20529 | General |
| 20543 | Blocking |
| 20547 | Information |
| 20553 | Document Flow |
| 20567 | Condition |
| 20573 | Missing Information |
| 20579 | General Data |
| 20585 | Organizational Data |
| 20613 | Items |
| 20625 | Carrier not specified |
| 20633 | Business Partner |
| 20639 | General |
| 20645 | Data |
| 20647 | Document Currency |
| 20659 | BP – |
| 20670 | Condition |
| 20674 | Your Response |
| 20684 | Currency |
| 20692 | Basic Settings |
| 20696 | Local Currency |
| 20702 | Cargo |
| 20708 | Items |
| 20716 | Condition |
| 20720 | Your Response |
| 20746 | Booking |
| 20774 | Booking |
| 20780 | Freight Tendering |
| 20782 | Charge Correction Advice Management |
| 20788 | Use |
| 20796 | Material valuations |
| 20813 | Your own company resources |
| 20821 | Customer billing for LSPs |
| 20831 | Sales returns |
| 20835 | Outbound |
| 20839 | Purchase returns |
| 20841 | Intercompany or intracompany stock transfers |
| 20886 | Prerequisites |
| 20904 | Basic Settings |
| 20906 | Define Charges Profiles |
| 20916 | Change |
| 20918 | Organizational Model |
| 20934 | Order |
| 20940 | Freight Bookings |
| 20948 | Order |
| 20956 | Settlement |
| 20958 | Freight Settlement |
| 20973 | Features |
| 20975 | Method, Rule, and Level |
| 20981 | Distribution method |
| 20998 | Distribution rule |
| 21004 | Distribution level |
| 21008 | Service Orders |
| 21016 | Link |
| 21020 | Cost Distribution for Shippers |
| 21024 | Cost Distribution for LSPs |
| 21034 | Group Logistics Company Process |
| 21038 | Cost Pull |
| 21050 | Use |
| 21066 | Features |
| 21079 | Retry Delivery |
| 21095 | Return to Loading Location |
| 21109 | Remove Freight Unit, Keep Items in Freight Document |
| 21131 | Activities |
| 21141 | Example |
| 21184 | Use |
| 21202 | Nature and quantity of goods |
| 21228 | Nature of goods for manifest |
| 21257 | Prerequisites |
| 21265 | Defined standard texts in transaction SO10 using text type ST |
| 21273 | Process |
| 21378 | Printing |
| 21383 | Use |
| 21396 | Document |
| 21402 | Freight orders |
| 21416 | Prerequisites |
| 21418 | Building of House Bills of Lading and House Air Waybills |
| 21428 | Forwarding Order |
| 21430 | Define Forwarding Order Types |
| 21434 | Freight Order ManagementFreight BookingDefine Freight Booking Types |
| 21450 | Printing of House Bills of Lading and House Air Waybills |
| 21462 | Freight Unit |
| 21486 | Charge |
| 21490 | Basic Settings |
| 21511 | Charge |
| 21515 | Basic Settings |
| 21541 | Features |
| 21543 | Building of House Bills of Lading and House Air Waybills |
| 21590 | Printing of House Bills of Lading and House Air Waybills |
| 21604 | Activities |
| 21608 | Forwarding orders |
| 21624 | Freight orders |
| 21638 | Ocean freight bookings |
| 21652 | Air freight bookings |
| 21660 | Freight units |
| 21678 | More Information |
| 21680 | Process Controller Configuration |
| 21685 | Use |
| 21691 | Prerequisites |
| 21701 | Process |
| 21707 | Follow-Up |
| 21711 | Load Plan Status |
| 21715 | Load Plan Status |
| 21725 | All assigned forwarding orders including the items |
| 21729 | Seal information, if this exists |
| 21782 | Discrepancies |
| 21784 | Updated seal information, if this exists |
| 21794 | References to business transaction documents |
