1/14/26, 2:15 PM

Transportation Management (TM)

Generated on: 2026-01-14 14:15:38 GMT+0000

SAP S/4HANA | 2025 (Oct 2025)

## Public

Original content: https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2?locale=en-

US&state=PRODUCTION&version=2025.000

## Warning

This document has been generated from SAP Help Portal and is an incomplete version of the official SAP product documentation.

The information included in custom documentation may not reflect the arrangement of topics in SAP Help Portal, and may be

missing important aspects and/or correlations to other topics. For this reason, it is not for production use.

For more information, please visit https://help.sap.com/docs/disclaimer.

This is custom documentation. For more information, please visit SAP Help Portal.

1


1/14/26, 2:15 PM

## Introductory Information

Before you start working with Transportation Management (TM), we recommend that you familiarize yourself with the following

important information.

## Working with Web Applications

The SAP Fiori launchpad is the access point for all web-based applications (apps) for TM. Apps are displayed as tiles, and you can

launch each app by clicking the corresponding tile on the launchpad. The tiles displayed on your launchpad home page are

arranged into groups, with the group title displayed at the top of each group.

The set of tiles initially visible to you on the launchpad depends on the business catalogs assigned to the business roles that your

business user is assigned to. The business catalogs and the corresponding tile groups are delivered as part of SAP S/4HANA.

In the Fiori launchpad frontend system, you can use the roles SAP_BR_TRANSPORTATION_MANAGER,

SAP_BR_TRANSPORTATION_PLANNER, SAP_BR_FRGHT_CTRC_SPECIALIST, and SAP_BR_FRGHT_SETTLEMENT_CLERK as

templates. These contain references to the Fiori tile catalogs that are listed in the following table. This enables you to access all

applications that are relevant for TM.

Business Catalogs for Transportation Manager Role

## Business Catalog

Transportation – Order Management

Transportation – Planning

Transportation – Settlement

Technical Name

SAP_TM_BC_OM

SAP_TM_BC_PLN

## SAP_TM_BC_STLM

Transportation – Contract Management

## SAP_TM_BC_CTRM

Transportation – Charge Management

## SAP_TM_BC_CHGM

Transportation – Master Data

## SAP_TM_BC_MD

Transportation – Profiles and Settings

## SAP_TM_BC_PRFS

Settlement Management - Manage Freight Cost Allocation

SAP_SM_BC_FCADOC_MNG

## Documents

Settlement Management - Monitor Freight Cost Allocation

SAP_SM_BC_FCADOC_ITM_MON

## Document Items

Settlement Management - Freight Cost Allocation Document

SAP_SM_BC_FCADOC_REL_JOB

## Release Scheduling

Sales – Billing Document Display

SAP_SD_BC_BIL_DOC_DISPL

Sales – Billing Document

## SAP_SD_BC_BIL_DOC

Sales – Sales Order Display

## SAP_SD_BC_SO_DISPL

Sales – Sales Order Processing

## SAP_SD_BC_SO_PROC_OP

Purchasing – Purchase Order Processing

SAP_PRC_BC_PURCHASER_PO

Purchasing – Contract Management

## SAP_PRC_BC_PURCHASER_PUC

This is custom documentation. For more information, please visit SAP Help Portal.

2


1/14/26, 2:15 PM

Business Catalog

## Technical Name

Logistics Execution – Inbound Deliveries Display

## SAP_LE_BC_IBDLV_DISPLAY

Logistic Execution – Inbound Delivery Processing

## SAP_LE_BC_ID_PROC

Logistic Execution – Outbound Deliveries Display

## SAP_LE_BC_OBDLV_DISPLAY

Logistic Execution – Outbound Delivery Processing

## SAP_LE_BC_OD_PROC

Accounts Payable – Supplier Invoice Processing

## SAP_PRC_BC_INVOICER

Project Management – Commercial Project Management

SAP_CPA_BC_COMMPRJ_MANAGE

Asset Accounting – Master Data

## SAP_SFIN_BC_AA_MASTER_DATA

You can rearrange the tiles within a group by dragging and dropping them. By using Edit Home Page, you can add tiles, remove

tiles, or relocate tiles beween groups. We recommend to create own roles, referencing only the necessary catalogues required by

the various groups of business users.

If you want to use apps on the launchpad, you need to set up a role in role maintenance. To do so, on the SAP Easy Access screen,

choose  Tools

 Administration

 User Maintenance

 Role Administration

 Roles .

  Note

FPM BOPF Integration (FBI) offers configurable and codeless integration of Floor Plan Manager (FPM) technology and

BOPF-based business objects (BOPF = Business Objects Processing Framework).

If you press the Refresh button on the user interface of a business document, Customizing data and master data is

loaded from the buffer and not read from the database. That means, changes made to the database are not taken into

account. However, if you use the browser refresh or reload, the system reopens the business document and reads

Customizing data and master data from the database.

For more information about SAP Fiori launchpad, see SAP Fiori Launchpad.

## Delivery Customizing

If you want to use delivery Customizing for TM, see SAP Note 2516155

.

## Displaying Application Help

For displaying context-sensitive help in WebDynpro apps and in Fiori apps, select the upper question mark in the upper right

corner.

For displaying the application help on the internet, we recommend to use the quick link https://help.sap.com/s4_op_tm.

## Displaying Field Help

To view field help in the SAP ABAP system, choose the field and press  F1 .

For displaying in-app help in WebDynpro apps and in Fiori apps, select the upper question mark in the upper right corner.

To view a screen area explanation in an app, right-click anywhere on the screen and choose Display Quick Help.

This is custom documentation. For more information, please visit SAP Help Portal.

3


1/14/26, 2:15 PM
## Described Feature Scope of the Product Assistance

For some of the features that are described in this product assistance for TM, you need a separate licence. For more information,

see the Feature Scope Description for SAP S/4HANA and the following SAP Note: 3065464

.

Furthermore, some features that are described in this product assistance are currently not released. For more information, see the

notes in the corresponding chapters of this product assistance and the following SAP Note: https://me.sap.com/notes/

.

This is custom documentation. For more information, please visit SAP Help Portal.

4
