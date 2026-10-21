# H09 - Settlement.md — Sections
Source: src/md/sapHelp/H09 - Settlement.md · 19298 lines · structure: markdown · built 2026-10-21

| Line | Topic |
|---|---|
| 9 | Public |
| 15 | Warning |
| 34 | Use |
| 64 | Internal settlement for resources |
| 148 | Payment to the carrier for providing the truck |
| 150 | Payment to the resource organization (RESOURCE_1) for providing the trailer |
| 209 | Settlement for Shippers |
| 225 | More Information |
| 229 | Subject |
| 231 | More Information |
| 241 | Agreement Management |
| 245 | Forwarding Order Management |
| 253 | Freight Order Management |
| 257 | Forwarding Settlement |
| 261 | Subject |
| 263 | More Information |
| 267 | Agreement |
| 273 | Freight Settlement |
| 277 | Cost Distribution Management |
| 281 | Cost Distribution for Shippers |
| 292 | Example |
| 310 | Term Explanation |
| 318 | Gateway |
| 337 | STA-NUE |
| 341 | STA-DLS |
| 345 | Incoterms |
| 369 | Cargo Movement |
| 385 | Agreements |
| 395 | Forwarding agreement |
| 405 | Forwarding agreement |
| 417 | Forwarding agreement |
| 427 | Dallas as the business partner |
| 442 | Freight agreement |
| 452 | Freight agreement |
| 462 | Freight agreement |
| 472 | Internal agreement |
| 484 | Forwarding Settlements |
| 506 | Freight Settlements |
| 524 | Internal Settlements |
| 545 | Consolidated Shipment |
| 563 | Settlement Based on Agreed Rates |
| 571 | Settlement Based on Freight Costs |
| 591 | Subject |
| 593 | More Information |
| 597 | Forwarding Settlement |
| 601 | Freight Settlement |
| 609 | Use |
| 615 | Integration |
| 626 | Component |
| 628 | Integration Type |
| 630 | Forwarding Order Management |
| 650 | Constraints |
| 656 | Definition |
| 660 | Use |
| 670 | Structure |
| 676 | General Data |
| 690 | Business Partner |
| 705 | Charges |
| 715 | Basic Settings |
| 725 | Orders |
| 749 | Document Flow |
| 757 | Application Log |
| 769 | In Process |
| 773 | Posted |
| 777 | Description |
| 789 | Cancellation Requested |
| 806 | Description |
| 812 | Canceled by Credit Memo |
| 830 | Posting Failed |
| 840 | Cancellation Successful |
| 848 | Integration |
| 858 | Forwarding Order Management |
| 862 | Charge Management and Service Product Catalogs |
| 868 | Agreement Management |
| 880 | Charge Calculation |
| 884 | Creation and Editing of Transportation Units |
| 895 | Features |
| 903 | Buyer’s Consolidation |
| 915 | Execution-Based Criteria |
| 933 | Settlement Basis in TM |
| 955 | Settlement item |
| 1008 | Constraints |
| 1020 | Example |
| 1030 | Rates each of the forwarding orders individually |
| 1042 | Use |
| 1062 | Prerequisites |
| 1076 | Features |
| 1078 | Settlement as a Variant of an Execution-Based Settlement |
| 1086 | Settlement Fallback |
| 1092 | Settlement for Container Items |
| 1100 | Example |
| 1125 | Main carriage |
| 1147 | More Information |
| 1164 | Features |
| 1180 | Charge Type |
| 1202 | Charge Type |
| 1232 | Features |
| 1238 | Multiple pickup and single delivery |
| 1249 | Single pickup and multiple delivery |
| 1255 | Multiple pickup and multiple delivery |
| 1261 | Predefined start and end |
| 1332 | Deliver FWO2 and FWO3 at location D |
| 1378 | More Information |
| 1386 | Use |
| 1388 | Business Requirement |
| 1448 | Freight order 2 to pick up FWO2 and bring it to location C |
| 1460 | Base freight |
| 1464 | Flat charge per truck |
| 1470 | Base charge for trailer |
| 1474 | System Settings |
| 1478 | Line Item |
| 1492 | Route |
| 1500 | Route |
| 1502 | Trailer Document for Main Carriage |
| 1508 | Pre-Carriage and On-Carriage |
| 1518 | Settlement Documents |
| 1551 | Charges |
| 1565 | Charges |
| 1641 | More Information |
| 1647 | Use |
| 1663 | Agreements |
| 1669 | Types of FWSD and number range intervals |
| 1679 | Forwarding settlement profile |
| 1695 | Basic Settings |
| 1705 | Master Data |
| 1709 | Organizational Model |
| 1729 | Calculation profile |
| 1733 | Charge |
| 1737 | Basic Settings |
| 1745 | Functions |
| 1749 | Basic Settings |
| 1757 | Data |
| 1761 | Organizational Model |
| 1781 | Process controller |
| 1789 | Settlement |
| 1795 | Define default agreement partner functions for stages |
| 1810 | Management |
| 1814 | Master data for Charge Management |
| 1820 | Business partner determination |
| 1828 | Business Partners |
| 1838 | Forwarding order |
| 1858 | Organizational Model |
| 1862 | Integration settings for posting to SD |
| 1868 | Forwarding Settlement |
| 1874 | Customizing under |
| 1884 | Required execution status for settlement creation |
| 1892 | Executed |
| 1898 | Management |
| 1900 | Forwarding Order |
| 1904 | Settlement Creation Status |
| 1908 | Define |
| 1910 | Settlement Profile |
| 1912 | Status for Settlement Creation |
| 1935 | Process |
| 1981 | Posted |
| 1985 | Canceled |
| 2057 | Tracking Manual Changes |
| 2065 | Payment terms |
| 2069 | Charges |
| 2073 | Service date |
| 2082 | Payer |
| 2084 | Deviating address for a bill-to business partner |
| 2088 | Creation Method |
| 2096 | Manual |
| 2104 | Create Forwarding Settlement Document |
| 2110 | Background Processing |
| 2118 | Change and Background Processing |
| 2124 | Follow-Up Forwarding Settlement Documents |
| 2165 | A zero amount where you have completely invoiced your customer |
| 2189 | See |
| 2197 | Execution-Based Settlement |
| 2217 | Use |
| 2231 | Prerequisites |
| 2241 | A calculation sheet for the shipper’s consolidation |
| 2252 | Example |
| 2272 | Main carriage |
| 2305 | More Information |
| 2311 | Use |
| 2323 | Settlement |
| 2331 | Minimum execution status |
| 2337 | Service date rule |
| 2343 | Billing schedule |
| 2353 | Settlement group |
| 2364 | Settlement rule |
| 2380 | Prerequisites |
| 2382 | General Prerequisites |
| 2396 | Settlement Group Prerequisites |
| 2426 | Basic Settings |
| 2432 | Settlement Rule Prerequisites |
| 2444 | Calendar |
| 2450 | Activities |
| 2454 | The set of charges you include in forwarding settlement documents |
| 2460 | Example |
| 2462 | Business Requirements |
| 2477 | Demurrage |
| 2489 | Service date for demurrage charges is the system date |
| 2499 | Customizing Settings |
| 2503 | Define |
| 2507 | Basic freight charges |
| 2511 | Demurrage |
| 2515 | Other VAS |
| 2525 | Execution status: In Execution |
| 2537 | Service date rule: leave empty |
| 2556 | Execution status: In Execution |
| 2564 | Use |
| 2590 | Prerequisites |
| 2592 | Types of settlement document and number range intervals |
| 2602 | Freight settlement profile |
| 2606 | Define |
| 2618 | Display in BP Role: Carrier |
| 2643 | Basic Settings |
| 2655 | Master Data |
| 2661 | Change Organizational Model |
| 2681 | Calculation profile |
| 2685 | Charge |
| 2689 | Basic Settings |
| 2701 | Logistics |
| 2705 | Master Data |
| 2707 | BP - Maintain Business Partner |
| 2711 | Vendor Org. Data . Choose |
| 2729 | Basic Settings |
| 2733 | Purch. Calc. Profile |
| 2741 | Master Data |
| 2747 | Change Organizational Model |
| 2751 | Org. Data |
| 2769 | Process controller |
| 2790 | Master data for charge management |
| 2796 | Business partner determination |
| 2808 | Business document |
| 2812 | Integration |
| 2822 | Freight Order Management |
| 2832 | Charge Management and Service Product |
| 2836 | Catalogs |
| 2851 | Management |
| 2857 | Prerequisites |
| 2870 | General Settings |
| 2872 | Define General Settings for TM . This setting |
| 2882 | Tax determination settings under Tax |
| 2890 | Freight Settlement |
| 2906 | Invoice Integration |
| 2924 | Company code and Plant |
| 2928 | Process |
| 3009 | Settlement |
| 3057 | Posting Periods |
| 3070 | Open the closed posting period |
| 3080 | Ledgers |
| 3084 | Posting Periods |
| 3098 | Other |
| 3114 | Freight Settlement |
| 3122 | Define Tax at Charge Type Level for Countries/Regions |
| 3126 | Assign Tax Indicators for Charges |
| 3140 | Settlement |
| 3203 | Subject |
| 3205 | More Information |
| 3217 | Verify Invoices for TM documents |
| 3227 | Changes After Posting |
| 3233 | Reversing a Freight Settlement Document |
| 3247 | Freight Settlement Document |
| 3253 | Use |
| 3285 | Structure |
| 3293 | General Data |
| 3301 | Procuring company code |
| 3307 | Net amount |
| 3311 | Verified invoice amount |
| 3315 | Business Partner |
| 3321 | Charges |
| 3333 | Basic Settings |
| 3335 | Define Calculation Profiles . In the case of collective freight settlement |
| 3341 | Orders |
| 3349 | Document Flow |
| 3357 | Application Log |
| 3380 | In Process |
| 3384 | Ready for Accruals |
| 3388 | Posting Started |
| 3394 | Posted |
| 3400 | Invoice Verified |
| 3404 | Cancellation Requested |
| 3410 | Canceled |
| 3414 | Reversal Requested |
| 3420 | Reversed |
| 3424 | Credit Memo Created |
| 3436 | Not Posted |
| 3440 | Not Confirmed |
| 3444 | Confirmed |
| 3446 | Posting Failed |
| 3452 | Cancellation Posting Failed |
| 3456 | No Confirmation |
| 3462 | Reversal Failed |
| 3466 | Purchase Order Creation Failed |
| 3474 | SES Creation Failed |
| 3482 | SES Cancellation Failed |
| 3499 | Description |
| 3501 | Purchase Order Cancellation Failed |
| 3509 | Cost distribution document creation failed |
| 3517 | Cost distribution document cancellation |
| 3527 | SES Reversal failed |
| 3535 | Cost distribution document reversal failed |
| 3543 | Integration |
| 3547 | Freight Order Management |
| 3551 | Charge Management and Service Product Catalogs |
| 3557 | Agreement Management |
| 3571 | Charge Calculation |
| 3575 | Reversing a Freight Settlement Document |
| 3626 | Result |
| 3652 | Reversed |
| 3664 | Credit Memo Created |
| 3688 | Related Information |
| 3692 | Company Code and Plant in Posting Freight Settlements |
| 3707 | Procuring Company Code |
| 3733 | Company Code |
| 3741 | Settlement |
| 3743 | Freight Settlement |
| 3759 | Invoicing |
| 3763 | Plant |
| 3771 | Freight Settlement |
| 3777 | Assign |
| 3789 | Invoicing |
| 3801 | Freight Settlement |
| 3817 | Invoicing |
| 3846 | Company Codes |
| 3850 | Changes After You Post Accruals |
| 3890 | Follow-Up Freight Settlement Document |
| 3951 | Related Information |
| 3956 | Business Process |
| 4023 | Processes |
| 4025 | Advanced Intercompany Sales |
| 4048 | Advanced Intercompany Stock Transfer |
| 4068 | Prerequisites |
| 4078 | Basic Settings |
| 4086 | Settlement |
| 4088 | Freight Settlement |
| 4094 | Posting Using |
| 4096 | Settlement Management |
| 4102 | Document Category: always specify 1 Settlement |
| 4118 | Viewing Freight Cost Allocation Documents |
| 4122 | Manage Freight Cost Allocation Documents |
| 4130 | Monitor Freight Cost Allocation Document Items |
| 4145 | Schedule Document Release - Freight Cost Allocation |
| 4161 | Related Information |
| 4171 | Use |
| 4177 | Self-billing |
| 4217 | Dispute Case |
| 4242 | Subject |
| 4244 | More Information |
| 4266 | Features of Dispute Management |
| 4282 | Dispute Management for Invoice Submission |
| 4377 | Subject |
| 4379 | More Information |
| 4395 | Features of Dispute Management |
| 4403 | Freight Settlement Dispute Case |
| 4411 | Use |
| 4435 | General Data |
| 4443 | Source location and destination location |
| 4447 | Status information |
| 4451 | Logistics Details |
| 4467 | Charge Details |
| 4479 | Currency: USD |
| 4494 | Dispute Charge Amounts |
| 4506 | Proposed Charge Amounts |
| 4516 | Taking Action on a Dispute Case |
| 4552 | Notes |
| 4558 | Attachments |
| 4571 | Tolerance Check Log |
| 4587 | Freight Settlement |
| 4593 | Work Items |
| 4601 | Integration |
| 4627 | Subject |
| 4629 | More Information |
| 4643 | Features of Dispute Management |
| 4664 | Use |
| 4674 | Prerequisites |
| 4678 | Freight Settlement |
| 4700 | Services |
| 4716 | Integration |
| 4718 | Enterprise Services |
| 4720 | Carrier Invoice Integration . The system |
| 4734 | Tax |
| 4738 | Integration |
| 4742 | Freight settlement dispute case |
| 4754 | Posting of the carrier invoice to MM |
| 4783 | Freight Settlement |
| 4805 | Master Data |
| 4815 | Features |
| 4817 | Possible Actions for Carrier Invoice |
| 4821 | Action |
| 4825 | Reject Invoice |
| 4837 | Post |
| 4845 | Has a life cycle status of other than Rejected |
| 4853 | Release |
| 4863 | Set to Draft |
| 4876 | Life Cycle Status |
| 4884 | New |
| 4886 | Draft |
| 4888 | Status Description |
| 4896 | In Process |
| 4906 | Not yet posted to MM |
| 4910 | Ready for posting |
| 4916 | Has a life cycle status of other than Rejected |
| 4926 | Posting started |
| 4930 | Carrier invoice posted |
| 4934 | Rejected |
| 4940 | Dispute Case Status in a Carrier Invoice |
| 4952 | Status |
| 4956 | No Dispute |
| 4962 | Awaiting Your Approval |
| 4977 | Resolved |
| 4979 | Status Description |
| 4985 | Rejected by You by Carrier |
| 4989 | Invoice |
| 4993 | Block Status |
| 5017 | Settlement |
| 5023 | Dispute Management |
| 5031 | Functions |
| 5033 | General Settings |
| 5037 | Confirmation Status |
| 5043 | Status |
| 5047 | Not Posted |
| 5051 | Not Confirmed |
| 5055 | Confirmed |
| 5059 | Invoice Posting Failed |
| 5063 | Tax Handling |
| 5081 | Integration |
| 5085 | Carrier |
| 5097 | Management |
| 5124 | Subject |
| 5146 | Web Services |
| 5150 | Use |
| 5166 | Process Flow |
| 5211 | Restrictions |
| 5219 | Complete Cancellation |
| 5243 | Repeating of Condition Types |
| 5316 | Through-Rate Calculation |
| 5334 | Stage B to stage C |
| 5340 | Partial Charge Line Resulting in a Dispute Case |
| 5350 | Different Currencies |
| 5364 | Carrier Invoice |
| 5370 | Working with Resolution-Based Charges |
| 5469 | Related Information |
| 5471 | Determine Logistical References Automatically |
| 5480 | Determine Logistical References Automatically |
| 5534 | Cargo Item |
| 5538 | UoM |
| 5542 | UoM |
| 5590 | Resolution Base |
| 5610 | Package |
| 5717 | Line |
| 5729 | Reference |
| 5844 | Line |
| 5912 | Line |
| 5993 | Line |
| 6061 | Settlement Profile Settings |
| 6065 | Define Settlement Profile , you can specify the freight |
| 6081 | Dispute Management Settings |
| 6089 | Management |
| 6093 | Dispute item types |
| 6112 | Dispute item profiles |
| 6130 | Use Example |
| 6132 | CHARGELINE.DISPUTE |
| 6142 | MANUAL.CHARGE.DISPUTE |
| 6146 | Loading charges |
| 6158 | ROOT.DISTANCE |
| 6166 | ROOT.GROSS.VOLUME |
| 6174 | ROOT.GROSS.WEIGHT |
| 6188 | Tolerance rules |
| 6202 | Overall amount in a freight order |
| 6229 | Dispute case reason codes and types |
| 6243 | Printouts, email, and enterprise service |
| 6251 | Freight Settlement |
| 6265 | Approval levels and workflow |
| 6291 | Settlement |
| 6305 | Subject |
| 6307 | More Information |
| 6317 | Features of Dispute Management |
| 6326 | Subject |
| 6328 | More Information |
| 6340 | Features of Dispute Management |
| 6348 | Tolerance Check |
| 6358 | Dispute Case |
| 6368 | Dispute Resolution Cycle |
| 6382 | Workflow and Work Items |
| 6398 | Dispute Cases Statuses |
| 6402 | Status |
| 6406 | Life cycle status |
| 6410 | Action status |
| 6421 | Status |
| 6425 | Workflow status |
| 6435 | Dispute status for total amount |
| 6441 | Dispute Case Status in Freight Order |
| 6449 | Status |
| 6451 | No Dispute |
| 6453 | Status Description |
| 6459 | Awaiting Your Approval |
| 6471 | Awaiting Carrier Approval |
| 6489 | Resolved |
| 6501 | In Dispute |
| 6546 | Dispute Resolution Statuses |
| 6572 | No Dispute |
| 6584 | No Dispute |
| 6602 | No Dispute |
| 6616 | Dispute Resolved |
| 6620 | Edit Dispute Case on Behalf of Carrier |
| 6630 | Subject |
| 6632 | More Information |
| 6647 | Subject |
| 6649 | More Information |
| 6663 | Life Cycle Status |
| 6669 | Status |
| 6671 | In Dispute |
| 6673 | Status Description |
| 6681 | Cancelled |
| 6695 | Dispute Resolved |
| 6703 | Accepted the claim from the service provider |
| 6713 | Dispute Rejected |
| 6717 | Action Status |
| 6723 | Status |
| 6727 | Awaiting Your Approval |
| 6733 | Completed |
| 6745 | Workflow Status |
| 6751 | Status |
| 6759 | Status Description |
| 6787 | Completed |
| 6793 | Dispute Item Status |
| 6801 | New |
| 6803 | Status Description |
| 6809 | Approved by You |
| 6813 | Accepted by You with Proposal |
| 6821 | Rejected by You |
| 6827 | Approved by Tolerance Check |
| 6837 | Workflow for Dispute Management |
| 6862 | Features |
| 6864 | Workflow Configuration |
| 6886 | Object Name |
| 6902 | Applications |
| 6924 | User and Role Specification |
| 6934 | Define Approval |
| 6938 | Settings |
| 6969 | Subject |
| 6971 | More Information |
| 6991 | Information on specifying roles |
| 7013 | Role |
| 7017 | Workflow Error Resolution for Dispute Management |
| 7029 | Resolution of Specific Errors |
| 7033 | Users not assigned to your purchasing organization |
| 7043 | Incorrect roles assigned to approval levels |
| 7049 | Settlement |
| 7051 | Freight Settlement |
| 7074 | Role |
| 7078 | Josephine Green |
| 7084 | John Brown |
| 7088 | Settlement specialist |
| 7096 | Role |
| 7110 | Purchasing clerk |
| 7122 | Freight Settlement |
| 7126 | Define Approval Levels and Roles |
| 7136 | Incorrect logic in BAdI: User Determination for Dispute Case Workflow |
| 7146 | Settlement |
| 7148 | Freight Settlement Dispute Management |
| 7166 | Displays a workflow status of Workflow Not Enabled |
| 7172 | Subject |
| 7174 | More Information |
| 7182 | Prerequisites for Dispute Management |
| 7191 | Subject |
| 7193 | More Information |
| 7203 | Standard SAP workflow process |
| 7225 | SAP Business |
| 7251 | Role |
| 7257 | System Administrator |
| 7263 | Administration |
| 7267 | Diagnosing |
| 7271 | Dispute Case Resolution and Accruals Update |
| 7283 | Change Process for Freight Settlement Documents |
| 7289 | Define |
| 7313 | New/In |
| 7325 | Accruals |
| 7350 | Accruals |
| 7354 | Verified |
| 7410 | Canceled |
| 7430 | New/In |
| 7442 | Accruals |
| 7448 | Accruals |
| 7454 | Posted/Invoice |
| 7460 | Verified |
| 7466 | Canceled |
| 7509 | Background Function to Create and Transfer Freight Settlement Documents |
| 7519 | Subject |
| 7521 | More Information |
| 7539 | Integration with MM |
| 7545 | Use |
| 7571 | Process |
| 7626 | Example |
| 7636 | Comment |
| 7644 | None |
| 7652 | Regular FSD |
| 7658 | None |
| 7674 | None |
| 7719 | Comment |
| 7751 | None |
| 7759 | Regular FSD |
| 7769 | None |
| 7803 | None |
| 7819 | Related Information |
| 7825 | Freight Settlement Integration using Lean Services |
| 7831 | Prerequisites |
| 7844 | General Settings |
| 7858 | Freight Settlement |
| 7862 | Service |
| 7886 | Freight Settlement |
| 7898 | Company Code and Plant |
| 7906 | Process |
| 7997 | Posting Periods |
| 8003 | Open the closed posting period |
| 8013 | Ledgers |
| 8017 | Posting Periods |
| 8031 | Other |
| 8082 | Subject |
| 8084 | More Information |
| 8108 | Invoicing Freight Documents |
| 8110 | Life Cycle Status of Freight Settlement Documents |
| 8122 | Description |
| 8128 | Posted |
| 8130 | Not Confirmed |
| 8159 | Confirmed |
| 8175 | Confirmed |
| 8181 | Posting failed |
| 8189 | SES Creation Failed |
| 8209 | Posting Failed |
| 8243 | SES Cancellation Failed |
| 8276 | Lean Services |
| 8291 | Prerequisites |
| 8305 | Freight Order |
| 8311 | Freight Booking |
| 8317 | Consignment Order |
| 8321 | Procuring Company Code |
| 8333 | Plant |
| 8343 | Settlement |
| 8345 | Freight Settlement |
| 8353 | Freight Cost Confirmation and Posting |
| 8359 | Prerequisites |
| 8371 | Air freight bookings: Uplift Confirmed |
| 8379 | Freight Cost Confirmation Based on Execution Status |
| 8389 | Freight Order |
| 8395 | Freight Booking |
| 8401 | Consignment Order |
| 8403 | Define Consignment Order Types |
| 8429 | Automatic Freight Cost Confirmation |
| 8443 | Enable automatic confirmation |
| 8449 | Related Information |
| 8453 | Invoicing Freight Documents |
| 8466 | Prerequisite |
| 8476 | Key Features |
| 8486 | Variances in Freight Invoices |
| 8498 | Unplanned Freight Cost |
| 8516 | Invoice Processing |
| 8520 | Create Supplier Invoice - Advanced |
| 8532 | Related Information |
| 8543 | Submission of Carrier Invoice |
| 8553 | Prerequisite |
| 8557 | Freight Settlement |
| 8563 | Integration |
| 8567 | Freight settlement dispute case |
| 8581 | Posting of the carrier invoice to MM |
| 8603 | Freight Settlement |
| 8617 | Master Data |
| 8629 | Features |
| 8631 | Possible Actions for Carrier Invoice |
| 8642 | Action |
| 8646 | Reject Invoice |
| 8658 | Post |
| 8674 | Release |
| 8684 | Set to Draft |
| 8690 | Life Cycle Status |
| 8698 | Draft |
| 8700 | Status Description |
| 8706 | In Process |
| 8716 | Not yet posted to MM |
| 8720 | Ready for Posting |
| 8726 | Has a life cycle status of other than Rejected |
| 8737 | Status |
| 8739 | Status Description |
| 8747 | Carrier invoice Posted |
| 8751 | Rejected |
| 8757 | Dispute Case Status in a Carrier Invoice |
| 8769 | Status |
| 8773 | No Dispute |
| 8779 | Awaiting Your Approval |
| 8785 | Resolved |
| 8791 | Rejected by You by Carrier |
| 8795 | Invoice |
| 8799 | Block Status |
| 8825 | Settlement |
| 8829 | Freight |
| 8831 | Settlement Dispute Management |
| 8839 | General Settings |
| 8843 | Confirmation Status |
| 8856 | Status |
| 8864 | Description |
| 8876 | Invoice Posting Failed |
| 8882 | Subject |
| 8900 | Process a carrier invoice using |
| 8904 | Web Services |
| 8916 | Resolution Based Charges |
| 8940 | Key Features |
| 8955 | Repost the failed variance posting for the carrier invoice |
| 8959 | Additional Details |
| 8973 | Tablet |
| 8975 | Reversing a Freight Settlement Document |
| 9015 | Result |
| 9023 | Reversed |
| 9044 | Result |
| 9052 | Reversed |
| 9066 | Credit Memo Created |
| 9096 | Related Information |
| 9100 | Invoicing Freight Orders |
| 9102 | Setting Up Tax Rates for Purchasing Transportation Services |
| 9134 | Transportation service for export of goods |
| 9142 | Transportation service for import of goods in EU |
| 9155 | Country/region of the freight procuring company |
| 9181 | Freight |
| 9261 | Different region |
| 9305 | Different region |
| 9317 | Description |
| 9319 | Tax country/region departure |
| 9332 | KOMK- SLAND1_Z |
| 9342 | KOMK- PSTLZZ |
| 9350 | Target postal code |
| 9370 | Key Features |
| 9386 | Additional Details |
| 9429 | Tablet |
| 9437 | Key Features |
| 9441 | Unblock or cancel blocked freight settlement documents |
| 9451 | View posting failed freight settlement documents |
| 9461 | View posted freight settlement documents |
| 9469 | View cancellation failed freight settlement documents |
| 9481 | Tablet |
| 9490 | Smartphone |
| 9492 | Posting of Allocated Freight Costs |
| 9569 | Additional Details |
| 9620 | Prerequisites |
| 9622 | Distribution profile |
| 9636 | G/L account settings |
| 9646 | Supply Chain |
| 9654 | Example of Freight Cost Distribution with a Business Use Case |
| 9683 | Flexibility in Freight Charge Changes |
| 9730 | Settlement |
| 9746 | Changes to Invoice Verified Freight Documents |
| 9762 | Description |
| 9764 | Agreement Redetermination |
| 9791 | Description |
| 9793 | Change in Logistical Data |
| 9797 | Unplanned Charges |
| 9825 | Changes to Posted Freight Documents |
| 9847 | Impact |
| 9849 | Charge Element |
| 9885 | Examples |
| 9891 | Change to charge amount in Posted charge line |
| 9942 | Documents |
| 9986 | Posted |
| 10062 | Documents |
| 10095 | Posted |
| 10141 | Documents |
| 10163 | Confirmation |
| 10169 | Related Information |
| 10173 | Blocking and Unblocking of Freight Documents |
| 10191 | Profile |
| 10205 | Blocking during Mismatched Charges |
| 10216 | Mismatches which are acceptable and can be overridden |
| 10226 | Mismatches which are inconsistent and can't be overridden |
| 10240 | Examples |
| 10242 | Scenario: No mismatch in charges |
| 10339 | Scenario: Amount Mismatch |
| 10391 | Scenario: Missing charges due to change in master data |
| 10435 | Scenario: Charges mismatch due to agreement redetermination |
| 10448 | Freight Order |
| 10482 | BASE |
| 10509 | Procurement |
| 10523 | Freight Charge Changes in Freight Settlement Documents |
| 10586 | Background Function to Publish Freight Settlement Dispute Cases |
| 10598 | Background Function to Create and Transfer Freight Settlement Documents |
| 10608 | Subject |
| 10610 | More Information |
| 10628 | Handling Calculated Charges in Lean Services |
| 10663 | Amount based calculation bases, such as GOODS_VALUE |
| 10669 | Deficit Weight Rate (DWR) Calculation Method |
| 10711 | Charge Line |
| 10745 | Not sent to PO |
| 10893 | Charge Type |
| 10919 | Charge Type |
| 10947 | Charge Type |
| 10953 | Weighted |
| 10975 | Value |
| 11014 | Charge Type |
| 11040 | Charge Type |
| 11068 | Charge Type |
| 11074 | Weighted |
| 11082 | Value |
| 11098 | Total amount |
| 11126 | Use |
| 11137 | Damaged goods |
| 11139 | Delays in transports |
| 11143 | Overcharges for transportation service |
| 11171 | Prerequisites |
| 11187 | Charges |
| 11199 | Related Information |
| 11207 | Use |
| 11220 | Prerequisites |
| 11222 | Types of credit memo and credit memo reason codes |
| 11236 | Influence invoicing status |
| 11244 | Automatically enter credit amount |
| 11252 | Settlement |
| 11266 | Settlement |
| 11286 | Customizing under |
| 11292 | Invoice Integration |
| 11296 | Forwarding settlement documents |
| 11302 | Features |
| 11304 | Credit Memo Preview |
| 11312 | Credit Memo Posting Started |
| 11325 | Canceled |
| 11329 | Activities |
| 11345 | Credit Memos |
| 11351 | Use |
| 11364 | Prerequisites |
| 11366 | Types of credit memo and credit memo reason codes |
| 11380 | Influence invoicing status |
| 11403 | Automatically enter credit amount |
| 11427 | Business document |
| 11447 | Master Data |
| 11455 | Integration settings for posting freight settlement documents |
| 11463 | Tax determination setting under Tax |
| 11475 | Customizing under |
| 11481 | Invoice Integration |
| 11485 | Activities |
| 11510 | Example |
| 11520 | Comments |
| 11532 | None |
| 11556 | None |
| 11570 | None |
| 11574 | Credit of 2400 using |
| 11578 | PO based on returns |
| 11608 | Regular freight |
| 11644 | Credit Memos |
| 11650 | Use |
| 11673 | Prerequisites |
| 11695 | Forwarding Settlement |
| 11739 | Organizational Mode |
| 11749 | Settlement |
| 11751 | Forwarding Settlement |
| 11759 | Customizing under |
| 11765 | Invoice Integration |
| 11798 | Settlement |
| 11800 | Forwarding Settlement |
| 11816 | Settings |
| 11826 | Billing |
| 11842 | Features |
| 11844 | Intercompany Settlements |
| 11848 | Intracompany Settlements |
| 11860 | Related Information |
| 11866 | Use |
| 11883 | Prerequisites |
| 11887 | Management |
| 11915 | Settlement |
| 11917 | Forwarding Settlement |
| 11923 | Activities |
| 11925 | Determining the Appropriate Agreement |
| 11933 | Manually Creating an Internal Settlement Document |
| 11943 | Sales organization of the overall forwarding order |
| 11949 | Creating Multiple Internal Settlement Documents |
| 11988 | Organizational Data , see the Purchasing Organization |
| 11992 | Ready for Settlement checkbox in the forwarding order |
| 12002 | BAdI: Readiness for Invoicing of Header-Level Charges |
| 12018 | Working with Forwarding Orders for Internal Settlement |
| 12034 | Specifying a Forwarding House |
| 12049 | Example |
| 12065 | Manually from the Forwarding Orders for Internal Settlement screen |
| 12081 | See |
| 12091 | Agreement |
| 12095 | Forwarding Settlement |
| 12099 | Cost Distribution for LSPs |
| 12107 | Use |
| 12117 | Prerequisites |
| 12134 | Freight Order |
| 12144 | Logistics |
| 12148 | Master Data |
| 12200 | Organizational Model |
| 12210 | Forwarding Settlement |
| 12216 | Customizing under |
| 12222 | Invoice Integration |
| 12236 | Customizing under |
| 12244 | Billing |
| 12260 | Billing |
| 12283 | Features |
| 12301 | Activities |
| 12311 | Create |
| 12313 | Internal Settlement Document |
| 12323 | Purchasing organization of the overall freight order |
| 12351 | Link |
| 12355 | Internal Settlement Management |
| 12364 | Topic |
| 12370 | Link |
| 12374 | Trailer Unit |
| 12382 | Use |
| 12390 | Material valuations |
| 12400 | Your own company resources |
| 12408 | Customer billing for LSPs |
| 12418 | Sales returns |
| 12422 | Outbound |
| 12426 | Purchase returns |
| 12428 | Intercompany or intracompany stock transfers |
| 12473 | Prerequisites |
| 12491 | Basic Settings |
| 12493 | Define Charges Profiles |
| 12503 | Change |
| 12505 | Organizational Model |
| 12521 | Order |
| 12527 | Freight Bookings |
| 12535 | Order |
| 12550 | Settlement |
| 12552 | Freight Settlement |
| 12568 | Features |
| 12570 | Method, Rule, and Level |
| 12576 | Distribution method |
| 12586 | Distribution rule |
| 12592 | Distribution level |
| 12596 | Service Orders |
| 12604 | Link |
| 12610 | Cost Distribution for LSPs |
| 12620 | Group Logistics Company Process |
| 12624 | Cost Pull |
| 12643 | Use |
| 12705 | Integration |
| 12711 | Prerequisites |
| 12726 | Settlement |
| 12728 | Freight Settlement |
| 12738 | Settlement |
| 12744 | Settlement Posting |
| 12756 | Mapping for Cost Distribution |
| 12762 | Settlement |
| 12764 | Freight Settlement |
| 12786 | Invoice |
| 12788 | Integration |
| 12792 | Example |
| 12805 | Processing Distributed Costs |
| 12831 | More Information |
| 12840 | Subject |
| 12842 | More Information |
| 12846 | SAP S/4HANA |
| 12852 | Chain |
| 12866 | Freight Cost Allocation |
| 12876 | Billing the Freight Cost in TM to a Customer in SD |
| 12902 | Example |
| 12910 | Item |
| 12944 | Charge |
| 12969 | Charge |
| 12975 | Packaging |
| 12981 | Packaging |
| 12999 | Details |
| 13067 | Related Information |
| 13075 | Use |
| 13096 | Internal settlements to settle with your internal organizations |
| 13104 | Integration |
| 13106 | Financial Accounting |
| 13112 | Analysis of Profitability in Forwarding Order |
| 13118 | Charge Management |
| 13136 | Prerequisites |
| 13144 | Freight Order |
| 13150 | Booking |
| 13156 | Calculated charges in the freight document |
| 13185 | Between the sales organization and the agreement party in the forwarding order |
| 13205 | Example |
| 13209 | Organizations |
| 13217 | Role |
| 13229 | Agreements |
| 13235 | Agreement |
| 13243 | Reason |
| 13276 | Agreement |
| 13284 | Reason |
| 13300 | Agreement |
| 13308 | Reason |
| 13336 | Orders |
| 13342 | Cost Distribution |
| 13400 | Trailer |
| 13428 | Internal Settlement with Distributed Costs |
| 13441 | Pays the execution costs |
| 13479 | Subject |
| 13483 | See |
| 13485 | Agreement |
| 13487 | Create and change calculation sheets |
| 13503 | Analyze profit |
| 13505 | Profitability Analysis |
| 13509 | Cost Pull |
| 13515 | Create an invoice for TM |
| 13521 | Use |
| 13531 | Prerequisites |
| 13539 | Cost |
| 13541 | Distribution |
| 13549 | Basic Settings |
| 13551 | Define Charges Profile |
| 13576 | Service Order |
| 13582 | Features |
| 13584 | Changing a Logistics Item |
| 13602 | Add, delete, or reposition a logistics item |
| 13610 | Changing a Freight Document |
| 13622 | Link |
| 13624 | Example 1 for a shipper |
| 13628 | Example 2 for a shipper |
| 13634 | Example 2 for an LSP |
| 13641 | Booking |
| 13684 | Container |
| 13694 | Delivery |
| 13702 | Delivery |
| 13710 | Delivery |
| 13718 | Delivery |
| 13754 | Service Order |
| 13768 | Item |
| 13877 | Delivery |
| 13907 | Delivery |
| 13937 | Delivery |
| 13967 | Delivery |
| 14056 | Reference |
| 14104 | Container |
| 14114 | Delivery |
| 14122 | Delivery |
| 14130 | Delivery |
| 14138 | Delivery |
| 14180 | Service Order |
| 14223 | Item |
| 14301 | Delivery |
| 14321 | Item |
| 14341 | Item Type |
| 14353 | Container |
| 14390 | Item |
| 14400 | Item Type |
| 14454 | Service Order |
| 14468 | Item |
| 14611 | SO71000 – |
| 14621 | SO71000 – |
| 14711 | Product |
| 14766 | Service Order |
| 14798 | Item |
| 14860 | FB77000 – |
| 14892 | Use |
| 14919 | Lower transportation costs |
| 14929 | Standardized logistics process |
| 14935 | Visibility |
| 14988 | More Information |
| 14999 | See |
| 15013 | Process |
| 15017 | Use |
| 15025 | Agreements |
| 15035 | Internal Agreement |
| 15056 | Business Partner |
| 15060 | External Agreement |
| 15082 | Cost Distribution |
| 15086 | Freight order |
| 15100 | Freight settlement document |
| 15108 | Pay the external LSP for all the transportation costs |
| 15114 | Internal settlement document |
| 15167 | Example of Recovering the Cost of Providing Transportation Services |
| 15184 | Logistics |
| 15188 | Master Data |
| 15196 | Billing |
| 15263 | Change Process |
| 15271 | Change the charges and recalculate in the existing internal settlement document |
| 15293 | Updates to TM Settlement Documents |
| 15307 | More Information |
| 15318 | See |
| 15322 | Group Logistics Scenario |
| 15330 | Company Process |
| 15340 | Company Process |
| 15344 | Use |
| 15364 | Purchase |
| 15382 | Order |
| 15396 | None |
| 15434 | None |
| 15566 | None |
| 15579 | Order or Delivery |
| 15587 | Sales order |
| 15591 | None |
| 15601 | None |
| 15621 | Purchase return |
| 15625 | None |
| 15669 | Define Default |
| 15681 | Settlement |
| 15704 | Use |
| 15717 | Item |
| 15723 | Business scenario |
| 15779 | Purchasing organization |
| 15795 | Charge calculation |
| 15890 | Item |
| 15902 | Not required |
| 15922 | Item |
| 15928 | Organizations |
| 15946 | Posting of freight |
| 16040 | Not required |
| 16073 | Item |
| 16077 | Group Logistics Company |
| 16125 | See |
| 16129 | Group Logistics Scenario |
| 16147 | Company Process |
| 16152 | Organizational Settings |
| 16177 | Company |
| 16187 | Entity ID |
| 16199 | Company |
| 16205 | Company |
| 16265 | Master Data |
| 16299 | Group |
| 16303 | Organizational Settings for Internal Settlement |
| 16342 | Model |
| 16350 | Settings |
| 16352 | Business Partner |
| 16360 | See |
| 16364 | Partner Function Codes in an OTR or DTR |
| 16374 | Company Process |
| 16384 | Group Logistics Company Process |
| 16388 | Document Type Settings |
| 16390 | Integration of orders and deliveries |
| 16404 | Internal settlement |
| 16410 | Stage profile, to determine the stage type in a freight unit |
| 16433 | Freight order type |
| 16453 | Freight settlement document type |
| 16459 | Freight Settlement |
| 16473 | Internal settlement document type |
| 16497 | Cost distribution methods |
| 16503 | Define |
| 16507 | Cost distribution profile |
| 16511 | Cost Distribution |
| 16515 | Cost distribution profile assignment |
| 16529 | Profile Settings |
| 16531 | Forwarding settlement profile and calculation profile on the sales side |
| 16539 | Freight settlement profile and calculation profile on the purchasing side |
| 16547 | Default Agreement Partner Function for a Stage |
| 16555 | Calculation Level for a Purchasing Organization |
| 16567 | See |
| 16571 | Group Logistics Scenario |
| 16585 | Company Process |
| 16589 | Partner Function Codes in an OTR or DTR |
| 16607 | Company Process |
| 16612 | Integration |
| 16621 | Internal settlement integration |
| 16631 | Freight settlement document integration |
| 16637 | Has its own cargo in a freight order |
| 16641 | Creates a freight settlement document for that freight order |
| 16649 | Tax determination setting under Tax |
| 16651 | Mapping for Cost Distribution, when cost distribution is enabled in FSD in TM |
| 16655 | Mapping Settings |
| 16657 | Map charge type to condition type |
| 16663 | SAP Components |
| 16669 | Billing |
| 16673 | Types |
| 16685 | Invoice Integration |
| 16687 | Mapping for Cost Distribution |
| 16693 | Settlement Management Document Settings |
| 16701 | Management |
| 16705 | Billing |
| 16709 | Other Settings |
| 16717 | More Information |
| 16728 | See |
| 16732 | Group Logistics Scenario |
| 16746 | Company Process |
| 16762 | Use |
| 16784 | Missing cargo in the transit warehousing process |
| 16796 | Direct change in your freight order from your carrier |
| 16808 | Direct change to the charges in your freight order |
| 16831 | Your Role |
| 16835 | Business Document |
| 16867 | LSP or carrier |
| 16899 | Forwarding order |
| 16905 | Credit memo |
| 16915 | Purchase order |
| 16921 | Credit memo |
| 16929 | Subject |
| 16931 | More Information |
| 16941 | Automatic Change Management for Freight Settlements |
| 16950 | Subject |
| 16952 | More Information |
| 16968 | How EWM handles discrepancies |
| 16974 | Use |
| 16976 | Forwarding and Internal Settlement Change Management Process |
| 16984 | Action |
| 17046 | Change Management Process Settings |
| 17061 | Change Process FWSD . You |
| 17071 | General Settings |
| 17081 | Reverse and repost a settlement document |
| 17198 | Delta amount only |
| 17247 | Settlement |
| 17255 | Delta Only |
| 17311 | None |
| 17337 | None |
| 17367 | None |
| 17383 | None |
| 17399 | None |
| 17556 | General Settings |
| 17602 | Forwarding Settlement Document and Credit Memo Settings |
| 17616 | Settlement |
| 17633 | Forwarding Settlement |
| 17641 | Forwarding Settlement |
| 17655 | Subject |
| 17657 | More Information |
| 17667 | Forwarding Settlement Scenario |
| 17682 | Use |
| 17769 | Subject |
| 17771 | More Information |
| 17781 | Use |
| 17820 | Change Management Process Settings |
| 17834 | General Settings |
| 17844 | Default credit memo type |
| 17850 | Settlement |
| 17860 | Lifecycle status of the freight settlement document |
| 17866 | Additional Detention Charge |
| 17876 | Additional Discount due to Better Volume |
| 17886 | Decrease in Rate for the Base Freight |
| 17903 | Increase in Rate for the Base Freight |
| 17915 | General |
| 17929 | Example |
| 17935 | Additional Detention Charge |
| 17951 | Volume |
| 17987 | Scenario |
| 18043 | Scenario |
| 18047 | Better Volume |
| 18060 | Example |
| 18116 | Freight |
| 18162 | CCAD Already Exists |
| 18166 | Scenario |
| 18168 | Additional Detention Charge |
| 18181 | Example |
| 18197 | Scenario |
| 18217 | Freight |
| 18231 | Canceled/Reversed |
| 18247 | Volume |
| 18269 | Example |
| 18304 | Example |
| 18308 | Volume |
| 18400 | Volume |
| 18445 | Example |
| 18483 | Exists |
| 18499 | Volume |
| 18523 | Canceled/Reversed |
| 18539 | Volume |
| 18558 | Example |
| 18602 | Charge Correction Advice Document |
| 18622 | Subject |
| 18624 | More Information |
| 18630 | Working with a dispute case |
| 18632 | Dispute Management for Freight Settlements |
| 18641 | Subject |
| 18643 | More Information |
| 18647 | Charge Correction Advice Management |
| 18652 | Settlements |
| 18660 | Define Settlement |
| 18668 | General Settings |
| 18674 | Scenario |
| 18684 | Not Up-To-Date |
| 18692 | Not Up-To-Date |
| 18708 | Related Information |
| 18714 | Use |
| 18743 | Integration |
| 18753 | Comment |
| 18765 | KOMK-ALAND |
| 18771 | Org |
| 18773 | KOMK-SLAND1_A |
| 18775 | Source Country/Region |
| 18781 | KOMK-SLAND1_Z |
| 18783 | Destination Country/Region |
| 18791 | BP Tax Group |
| 18799 | Charge Type Tax Group |
| 18815 | None |
| 18823 | KOMK-ALAND |
| 18829 | KOMK-SLAND1_A |
| 18831 | Source Country/Region |
| 18848 | Comment |
| 18850 | KOMK-SLAND1_Z |
| 18852 | Destination Country/Region |
| 18858 | KOMP-TAXIM |
| 18860 | Material Tax Indicator |
| 18864 | Prerequisites |
| 18886 | Integration |
| 18894 | Invoicing |
| 18896 | Tax Setting for TM |
| 18916 | Integration |
| 18924 | Invoicing |
| 18926 | Tax Setting for TM |
| 18941 | Settlement |
| 18951 | Settlement |
| 18957 | Features |
| 18967 | More Information |
| 18980 | Credit Memos |
| 18984 | Use |
| 18998 | Features |
| 19000 | Split Criteria for Forwarding Settlement Documents |
| 19008 | Payer |
| 19018 | Calculation level |
| 19030 | Split Criteria for Freight Settlement Documents |
| 19036 | Purchasing organization |
| 19038 | Carrier or additional agreement party |
| 19049 | Payee |
| 19055 | Calculation level |
| 19059 | Example |
| 19061 | Forwarding Settlement |
| 19083 | Party / Payer |
| 19103 | FWSD |
| 19141 | Freight Settlement |
| 19149 | Purchasing |
| 19183 | Company |
| 19187 | Company |
| 19228 | Document |
| 19268 | Company |
| 19286 | Company |
| 19290 | Related Information |
| 19294 | Forwarding Settlement |
