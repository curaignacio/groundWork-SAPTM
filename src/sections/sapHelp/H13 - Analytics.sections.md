# H13 - Analytics.md — Sections
Source: src/md/sapHelp/H13 - Analytics.md · 7109 lines · structure: markdown · built 2026-10-21

| Line | Topic |
|---|---|
| 9 | Public |
| 15 | Warning |
| 32 | Analytics |
| 42 | Analytics Overview Pages |
| 66 | Detailed Views |
| 86 | CDS Views |
| 104 | Summary |
| 108 | Detailed Views |
| 114 | Transportation Allocation |
| 120 | Business Share |
| 128 | Cost Analysis |
| 164 | Freight Order Execution |
| 184 | Tendering |
| 188 | Metadata Extensions to Replace Delivered Time Filters |
| 198 | Allocation Analysis |
| 212 | Key Features |
| 214 | Trade Lane Weight Load Analysis |
| 227 | Trade Lane Volume Load Analysis |
| 233 | Trade Lane Container Load Analysis |
| 239 | Transportation Mode Category Analysis |
| 245 | Overall Weight Utilization Distribution |
| 253 | Overall Container Utilization Distribution |
| 259 | Detailed View |
| 271 | Tablet |
| 285 | Subject |
| 287 | More Information |
| 291 | Carrier Selection |
| 300 | Subject |
| 302 | More Information |
| 314 | Transportation Allocation Detailed View |
| 326 | Information filter |
| 340 | Graphics view |
| 346 | Field view |
| 354 | Bar chart |
| 366 | Table |
| 389 | Example |
| 401 | Technical Basis |
| 413 | Allocation Analysis |
| 421 | View Type |
| 425 | Purpose |
| 433 | Prerequisites |
| 470 | T_ADMIN |
| 476 | T_TAL |
| 482 | ACTVT |
| 490 | ACTVT |
| 494 | ACTVT |
| 533 | BRGRU |
| 541 | ACTVT |
| 551 | Structure |
| 553 | Business Objects |
| 557 | Main Input Parameters |
| 561 | P_Language |
| 565 | P_TodayDate |
| 573 | P_DisplayWeightUnit |
| 577 | P_DisplayVolumeUnit |
| 581 | P_DisplayQuantityUnit |
| 585 | P_TrAlcMinToleranceInPercent |
| 589 | P_TrAlcMaxToleranceInPercent |
| 595 | Measures and Attributes |
| 605 | YearMonth |
| 609 | TranspAllocType |
| 613 | TranspAllocValdtyEndDateTime |
| 642 | TradeLane |
| 652 | MeansOfTransport |
| 686 | TrAlcCurGrossVolumeInDspUnit |
| 733 | Units |
| 745 | Business Share Analysis |
| 757 | Key Features |
| 766 | Weight Fulfillment Ratio |
| 774 | Volume Fulfillment Ratio |
| 782 | Trade Lane Fulfillment |
| 796 | Sea Fulfillment Distribution |
| 802 | Air Fulfillment Distribution |
| 808 | Detailed View |
| 820 | Tablet |
| 832 | More Information |
| 841 | Subject |
| 843 | More Information |
| 847 | Business Share |
| 857 | Business Share Detailed View |
| 869 | Information filter |
| 883 | Graphics view |
| 889 | Field view |
| 895 | Bar chart |
| 907 | Table |
| 930 | Example |
| 946 | Technical Basis |
| 966 | View Type |
| 970 | Purpose |
| 978 | Prerequisites |
| 1015 | T_ADMIN |
| 1070 | BRGRU |
| 1081 | Value |
| 1093 | Structure |
| 1095 | Business Objects |
| 1099 | Main Input Parameters |
| 1103 | P_Language |
| 1107 | P_TodayDate |
| 1115 | P_DisplayWeightUnit |
| 1119 | P_DisplayVolumeUnit |
| 1125 | Measures and Attributes |
| 1131 | BusinessShare |
| 1135 | Carrier |
| 1139 | YearMonth |
| 1147 | BusShrValidityEndDateTime |
| 1158 | TradeLane |
| 1194 | Units |
| 1204 | Cost Analysis |
| 1231 | Key Features |
| 1235 | Cost Distribution |
| 1241 | Cost and Quantity Analysis |
| 1247 | Logistic Network Analysis |
| 1255 | Carrier Cost Analysis |
| 1261 | Cost and Quantity Analysis |
| 1267 | Charge Type Analysis |
| 1275 | Purchasing Organization Cost Analysis |
| 1285 | Invoicing Block Analysis |
| 1293 | Detailed View |
| 1316 | Tablet |
| 1340 | Subject |
| 1342 | More Information |
| 1346 | Settlement |
| 1360 | Freight Settlement Cost Query |
| 1364 | C_TranspOrdInvcgBlockStsQ |
| 1368 | Transportation Costs Detailed View |
| 1387 | Information filter |
| 1397 | Graphics view |
| 1403 | Field view |
| 1409 | Bar chart |
| 1419 | Table |
| 1433 | Example |
| 1449 | Technical Basis |
| 1468 | Cost Analysis |
| 1470 | Transportation Invoice Blocked Detailed View |
| 1482 | Information filter |
| 1494 | Graphics view |
| 1500 | Field view |
| 1506 | Bar chart |
| 1516 | Table |
| 1532 | Example |
| 1553 | Technical Basis |
| 1565 | Cost Analysis |
| 1571 | View Type |
| 1575 | Purpose |
| 1585 | Prerequisites |
| 1618 | Value |
| 1632 | ACTVT |
| 1636 | Activity |
| 1646 | TM_OT |
| 1660 | TM_OT |
| 1670 | ACTVT |
| 1706 | Activity |
| 1742 | Activity |
| 1750 | TM_SF_CAT |
| 1756 | TM_SF_TYPE |
| 1762 | ACTVT |
| 1766 | Activity |
| 1785 | Value |
| 1789 | BEGRU |
| 1799 | ACTVT |
| 1805 | Structure |
| 1807 | Business Objects |
| 1817 | Main Input Parameters |
| 1821 | P_Language |
| 1825 | P_TodayDate |
| 1833 | P_DisplayTimeUnit |
| 1837 | P_DisplayWeightUnit |
| 1841 | P_DisplayVolumeUnit |
| 1845 | P_DisplayQuantityUnit |
| 1849 | P_DisplayLengthUnit |
| 1853 | P_DisplayCurrency |
| 1866 | Measures and Attributes |
| 1908 | Carrier |
| 1910 | InvoiceDate |
| 1918 | InvoiceDateYear |
| 1928 | TransportationMode |
| 1939 | MeansOfTransport |
| 1953 | Consignee |
| 1991 | TranspChargeCalcReslnBase |
| 2001 | TranspOrdNumberOfCtnsInDspUnit |
| 2022 | Units |
| 2044 | View Type |
| 2048 | Purpose |
| 2054 | Prerequisites |
| 2087 | Value |
| 2099 | ACTVT |
| 2103 | Activity |
| 2113 | TM_OT |
| 2127 | TM_OT |
| 2137 | ACTVT |
| 2173 | Activity |
| 2209 | Activity |
| 2217 | TM_SF_CAT |
| 2223 | TM_SF_TYPE |
| 2229 | ACTVT |
| 2233 | Activity |
| 2246 | Value |
| 2250 | B_BUPA_GRP |
| 2258 | BEGRU |
| 2270 | ACTVT |
| 2276 | Structure |
| 2278 | Business Objects |
| 2288 | Main Input Parameters |
| 2292 | P_Language |
| 2296 | P_TodayDate |
| 2304 | P_DisplayWeightUnit |
| 2308 | P_DisplayVolumeUnit |
| 2312 | P_DisplayQuantityUnit |
| 2316 | P_DisplayCurrency |
| 2322 | Measures and Attributes |
| 2337 | TransportationOrder |
| 2351 | MeansOfTransport |
| 2363 | PurchasingGroup |
| 2373 | Carrier |
| 2395 | TranspOrdExecutionIsBlocked |
| 2444 | InvoiceDate |
| 2452 | InvoiceDateYear |
| 2462 | TranspChargeCalcLevel |
| 2466 | TranspOrdGrossWeightInDspUnit |
| 2493 | Units |
| 2507 | Freight Booking Execution Monitoring |
| 2527 | Key Features |
| 2533 | Life Cycle Status Analysis |
| 2552 | Execution Block Analysis |
| 2562 | Planning Block Analysis |
| 2572 | Delayed Freight Bookings in Transit |
| 2590 | Blocking Discrepancies |
| 2596 | Non-Blocking Discrepancies |
| 2604 | Carrier On Time Performance |
| 2616 | Location On Time Performance |
| 2624 | Activity On Time Performance |
| 2639 | Unexpected Events |
| 2647 | Detailed View |
| 2665 | Tablet |
| 2687 | Subject |
| 2689 | More Information |
| 2693 | Freight Booking |
| 2703 | C_FrtBkgExecutionStsQ CDS view |
| 2712 | Subject |
| 2714 | More Information |
| 2722 | Freight Booking Execution Detailed View |
| 2738 | Unexpected events |
| 2744 | Information filter |
| 2760 | Graphics view |
| 2766 | Field view |
| 2772 | Bar chart |
| 2782 | Table |
| 2803 | Example |
| 2811 | Technical Basis |
| 2821 | More Information |
| 2827 | Freight Booking Execution Status Detailed View |
| 2843 | Freight orders delayed in transit |
| 2849 | Information filter |
| 2872 | Graphics view |
| 2878 | Field view |
| 2884 | Bar chart |
| 2896 | Table |
| 2910 | Example |
| 2916 | Technical Basis |
| 2926 | More Information |
| 2928 | Freight Booking Execution Monitoring |
| 2943 | View Type |
| 2947 | Purpose |
| 2955 | Prerequisites |
| 2985 | T_ADMIN |
| 2991 | T_TOR_PUR |
| 2997 | ACTVT |
| 3005 | ACTVT |
| 3018 | T_TOR_EXE |
| 3028 | TM_OC |
| 3034 | TM_OT |
| 3038 | TM_XPORG |
| 3042 | TM_XPGRP |
| 3046 | TM_RP |
| 3050 | TM_MOT |
| 3054 | ACTVT |
| 3058 | TM_OC |
| 3064 | TM_OT |
| 3068 | TM_XEORG |
| 3072 | TM_XEGRP |
| 3076 | TM_RP |
| 3080 | TM_MOT |
| 3084 | ACTVT |
| 3111 | Object |
| 3120 | ACTVT |
| 3150 | BRGRU |
| 3162 | ACTVT |
| 3166 | Structure |
| 3168 | Business Objects |
| 3172 | Main Input Parameters |
| 3176 | P_Language |
| 3180 | P_TodayDate |
| 3188 | P_DisplayTimeUnit |
| 3199 | P_DisplayWeightUnit |
| 3203 | P_DisplayVolumeUnit |
| 3207 | P_DisplayQuantityUnit |
| 3211 | P_DisplayLengthUnit |
| 3217 | Measures and Attributes |
| 3251 | Consignee |
| 3255 | DiscrepancyType |
| 3261 | SourceLocationType |
| 3290 | Country |
| 3332 | NumberOfOnTimeTranspOrdEvents |
| 3345 | Units |
| 3365 | View Type |
| 3369 | Purpose |
| 3381 | Prerequisites |
| 3418 | T_ADMIN |
| 3424 | T_TOR_PUR |
| 3430 | ACTVT |
| 3434 | ACTVT |
| 3438 | TM_OC |
| 3444 | TM_OT |
| 3448 | TM_XPORG |
| 3452 | TM_XPGRP |
| 3456 | TM_RP |
| 3460 | TM_MOT |
| 3464 | ACTVT |
| 3468 | TM_OC |
| 3474 | TM_OT |
| 3478 | T_TOR_EXE |
| 3491 | Value |
| 3493 | TM_XEORG |
| 3497 | TM_XEGRP |
| 3501 | TM_RP |
| 3505 | TM_MOT |
| 3509 | ACTVT |
| 3513 | ACTVT |
| 3523 | Object |
| 3564 | BRGRU |
| 3572 | ACTVT |
| 3576 | Structure |
| 3578 | Business Objects |
| 3582 | Main Input Parameters |
| 3593 | P_Language |
| 3597 | P_TodayDate |
| 3605 | P_DisplayTimeUnit |
| 3609 | P_DisplayWeightUnit |
| 3613 | P_DisplayVolumeUnit |
| 3617 | P_DisplayQuantityUnit |
| 3621 | P_DisplayLengthUnit |
| 3627 | Measures and Attributes |
| 3655 | TransportationOrderExecSts |
| 3668 | Consignee |
| 3718 | Units |
| 3728 | DisplayVolumeUnit |
| 3741 | Freight Booking Quantity Analysis |
| 3757 | Key Features |
| 3759 | Gross Weight Distribution |
| 3767 | Gross Volume Distribution |
| 3775 | Quantity Distribution |
| 3783 | Transportation Mode Category Analysis |
| 3791 | Logistic Network Analysis |
| 3799 | Carrier Quantity Analysis |
| 3805 | Shipper Quantity Analysis |
| 3811 | Ship-To Party Quantity Analysis |
| 3824 | Utilization Distribution |
| 3830 | Quantity Analysis |
| 3838 | Distance Analysis |
| 3846 | Detailed View |
| 3858 | Tablet |
| 3872 | Subject |
| 3874 | More Information |
| 3878 | Freight Booking |
| 3890 | Freight Booking Quantity Query |
| 3899 | Freight Booking Quantity Detailed View |
| 3911 | Information filter |
| 3923 | Graphics view |
| 3929 | Field view |
| 3935 | Bar chart |
| 3947 | Table |
| 3959 | Example |
| 3966 | Technical Basis |
| 3983 | More Information |
| 3993 | View Type |
| 3997 | Purpose |
| 4005 | Prerequisites |
| 4035 | T_ADMIN |
| 4045 | ACTVT |
| 4060 | Value |
| 4062 | T_TOR_PUR |
| 4068 | T_TOR_EXE |
| 4073 | TM_OC |
| 4079 | TM_OT |
| 4083 | TM_XPORG |
| 4087 | TM_XPGRP |
| 4091 | TM_RP |
| 4095 | TM_MOT |
| 4099 | ACTVT |
| 4103 | TM_OC |
| 4109 | TM_OT |
| 4113 | TM_XEORG |
| 4117 | TM_XEGRP |
| 4121 | TM_RP |
| 4125 | TM_MOT |
| 4127 | TransportationMode |
| 4146 | ACTVT |
| 4167 | ACTVT |
| 4194 | BRGRU |
| 4202 | ACTVT |
| 4206 | Structure |
| 4208 | Business Objects |
| 4212 | Main Input Parameters |
| 4216 | P_Language |
| 4220 | P_TodayDate |
| 4235 | P_DisplayTimeUnit |
| 4239 | P_DisplayWeightUnit |
| 4243 | P_DisplayVolumeUnit |
| 4247 | P_DisplayQuantityUnit |
| 4251 | P_DisplayLengthUnit |
| 4257 | Measures and Attributes |
| 4297 | PurchasingOrganization |
| 4306 | PurchasingGroup |
| 4322 | Carrier |
| 4328 | Consignee |
| 4370 | TranspOrdMaxUtilznMassRatio |
| 4403 | Units |
| 4419 | Freight Order Execution Monitoring |
| 4433 | Key Features |
| 4439 | Life Cycle Status Analysis |
| 4458 | Execution Block Analysis |
| 4470 | Planning Block Analysis |
| 4482 | Delayed Freight Orders in Transit |
| 4500 | Blocking Discrepancies |
| 4506 | Non-Blocking Discrepancies |
| 4514 | Carrier On Time Performance |
| 4526 | Location On Time Performance |
| 4541 | Activity On Time Performance |
| 4549 | Unexpected Events |
| 4557 | Detailed View |
| 4575 | Tablet |
| 4597 | Subject |
| 4599 | More Information |
| 4603 | Freight Order Management |
| 4612 | Subject |
| 4614 | More Information |
| 4634 | Freight Order Execution Detailed View |
| 4648 | Unexpected events |
| 4654 | Information filter |
| 4670 | Graphics view |
| 4676 | Field view |
| 4682 | Bar chart |
| 4699 | Table |
| 4713 | Example |
| 4720 | Technical Basis |
| 4730 | More Information |
| 4736 | Freight Order Execution Status Detailed View |
| 4750 | Freight orders delayed in transit |
| 4754 | Screen Areas |
| 4763 | Information filter |
| 4779 | Graphics view |
| 4785 | Field view |
| 4791 | Bar chart |
| 4803 | Table |
| 4817 | Example |
| 4823 | Technical Basis |
| 4833 | More Information |
| 4850 | View Type |
| 4854 | Purpose |
| 4862 | Prerequisites |
| 4892 | T_ADMIN |
| 4898 | T_TOR_PUR |
| 4904 | ACTVT |
| 4921 | T_TOR_EXE |
| 4931 | ACTVT |
| 4935 | TM_OC |
| 4941 | TM_OT |
| 4945 | TM_XPORG |
| 4949 | TM_XPGRP |
| 4953 | TM_RP |
| 4957 | TM_MOT |
| 4961 | ACTVT |
| 4965 | TM_OC |
| 4971 | TM_OT |
| 4975 | TM_XEORG |
| 4979 | TM_XEGRP |
| 4983 | TM_RP |
| 4987 | TM_MOT |
| 4991 | ACTVT |
| 5018 | Object |
| 5027 | ACTVT |
| 5058 | BRGRU |
| 5070 | ACTVT |
| 5074 | Structure |
| 5076 | Business Objects |
| 5080 | Main Input Parameters |
| 5084 | P_Language |
| 5088 | P_TodayDate |
| 5096 | P_DisplayTimeUnit |
| 5107 | P_DisplayWeightUnit |
| 5111 | P_DisplayVolumeUnit |
| 5115 | P_DisplayQuantityUnit |
| 5119 | P_DisplayLengthUnit |
| 5125 | Measures and Attributes |
| 5159 | Consignee |
| 5163 | DiscrepancyType |
| 5169 | SourceLocationType |
| 5198 | Country |
| 5240 | NumberOfOnTimeTranspOrdEvents |
| 5253 | Units |
| 5273 | View Type |
| 5277 | Purpose |
| 5289 | Prerequisites |
| 5326 | T_ADMIN |
| 5332 | T_TOR_PUR |
| 5338 | ACTVT |
| 5342 | ACTVT |
| 5346 | TM_OC |
| 5352 | TM_OT |
| 5356 | TM_XPORG |
| 5360 | TM_XPGRP |
| 5364 | TM_RP |
| 5368 | TM_MOT |
| 5372 | ACTVT |
| 5376 | TM_OC |
| 5382 | TM_OT |
| 5386 | T_TOR_EXE |
| 5399 | Value |
| 5401 | TM_XEORG |
| 5405 | TM_XEGRP |
| 5409 | TM_RP |
| 5413 | TM_MOT |
| 5417 | ACTVT |
| 5421 | ACTVT |
| 5431 | Object |
| 5472 | BRGRU |
| 5480 | ACTVT |
| 5484 | Structure |
| 5486 | Business Objects |
| 5490 | Main Input Parameters |
| 5501 | P_Language |
| 5505 | P_TodayDate |
| 5513 | P_DisplayTimeUnit |
| 5517 | P_DisplayWeightUnit |
| 5521 | P_DisplayVolumeUnit |
| 5525 | P_DisplayQuantityUnit |
| 5529 | P_DisplayLengthUnit |
| 5535 | Measures and Attributes |
| 5563 | TransportationOrderExecSts |
| 5576 | Consignee |
| 5626 | Units |
| 5636 | DisplayVolumeUnit |
| 5649 | Freight Order Quantity Analysis |
| 5665 | Key Features |
| 5667 | Gross Weight Distribution |
| 5675 | Gross Volume Distribution |
| 5683 | Quantity Distribution |
| 5691 | Transportation Mode Category Analysis |
| 5699 | Logistic Network Analysis |
| 5707 | Carrier Quantity Analysis |
| 5713 | Shipper Quantity Analysis |
| 5726 | Ship-To Party Quantity Analysis |
| 5732 | Utilization Distribution |
| 5738 | Quantity Analysis |
| 5746 | Distance Analysis |
| 5754 | Detailed View |
| 5766 | Tablet |
| 5780 | Subject |
| 5782 | More Information |
| 5786 | Freight Order Management |
| 5796 | Freight Order Quantity Query |
| 5805 | Freight Order Quantity Detailed View |
| 5817 | Information filter |
| 5831 | Graphics view |
| 5837 | Field view |
| 5843 | Bar chart |
| 5855 | Table |
| 5867 | Example |
| 5885 | Technical Basis |
| 5895 | More Information |
| 5905 | View Type |
| 5909 | Purpose |
| 5917 | Prerequisites |
| 5947 | T_ADMIN |
| 5970 | ACTVT |
| 5974 | T_TOR_PUR |
| 5980 | T_TOR_EXE |
| 5986 | TM_OC |
| 5992 | TM_OT |
| 5996 | TM_XPORG |
| 6000 | TM_XPGRP |
| 6004 | TM_RP |
| 6008 | TM_MOT |
| 6012 | ACTVT |
| 6016 | TM_OC |
| 6022 | TM_OT |
| 6026 | TM_XEORG |
| 6030 | TM_XEGRP |
| 6034 | TM_RP |
| 6036 | TranspOrdResponsiblePerson |
| 6047 | TM_MOT |
| 6051 | ACTVT |
| 6055 | ACTVT |
| 6065 | Object |
| 6106 | BRGRU |
| 6114 | ACTVT |
| 6118 | Structure |
| 6120 | Business Objects |
| 6124 | Main Input Parameters |
| 6128 | P_Language |
| 6132 | P_TodayDate |
| 6147 | P_DisplayTimeUnit |
| 6151 | P_DisplayWeightUnit |
| 6155 | P_DisplayVolumeUnit |
| 6159 | P_DisplayQuantityUnit |
| 6163 | P_DisplayLengthUnit |
| 6169 | Measures and Attributes |
| 6205 | PlngAndExecOrganization |
| 6218 | PurchasingGroup |
| 6234 | Carrier |
| 6240 | Consignee |
| 6278 | NumberOfTransportationOrders |
| 6315 | Units |
| 6331 | Tendering Analysis |
| 6349 | Key Features |
| 6358 | Open Requests |
| 6368 | Overdue Requests |
| 6374 | Acceptance Analysis |
| 6382 | Tendering Peer-to-Peer Cycle Analysis |
| 6394 | Tendering Cycle Time Analysis |
| 6404 | Tendering Ratio |
| 6412 | Original Carrier Changed |
| 6422 | Detailed View |
| 6434 | Tablet |
| 6455 | Subject |
| 6457 | More Information |
| 6461 | Freight Tendering |
| 6465 | Tendering Detailed View |
| 6471 | Tendering Query |
| 6473 | Tendering Detailed View |
| 6485 | Information filter |
| 6495 | Graphics view |
| 6501 | Field view |
| 6507 | Bar chart |
| 6524 | Table |
| 6536 | Example |
| 6548 | Technical Basis |
| 6568 | View Type |
| 6572 | Purpose |
| 6588 | Prerequisites |
| 6618 | T_ADMIN |
| 6624 | T_TOR_PUR |
| 6630 | ACTVT |
| 6634 | TM_OC |
| 6640 | TM_OT |
| 6644 | TM_XPORG |
| 6648 | TM_XPGRP |
| 6652 | TM_RP |
| 6656 | TM_MOT |
| 6660 | ACTVT |
| 6679 | Value |
| 6681 | T_TOR_EXE |
| 6687 | TM_OC |
| 6693 | TM_OT |
| 6697 | TM_XEORG |
| 6701 | TM_XEGRP |
| 6705 | TM_RP |
| 6709 | TM_MOT |
| 6713 | ACTVT |
| 6735 | ACTVT |
| 6775 | Structure |
| 6783 | BRGRU |
| 6791 | ACTVT |
| 6797 | Main Input Parameters |
| 6801 | P_Language |
| 6805 | P_TodayDate |
| 6813 | P_DisplayTimeUnit |
| 6817 | P_DisplayWeightUnit |
| 6821 | P_DisplayVolumeUnit |
| 6825 | P_DisplayQuantityUnit |
| 6829 | P_DisplayCurrency |
| 6835 | Measures and Attributes |
| 6841 | TransportationOrder |
| 6884 | ChangedDateTime |
| 6898 | Carrier |
| 6908 | TenderingType |
| 6914 | TenderingHasCompletedCycle |
| 6985 | IsProposedFreightQuotation |
| 7018 | NumberOfTenderings |
| 7056 | NumberOfTenderingRequests |
| 7091 | Units |
