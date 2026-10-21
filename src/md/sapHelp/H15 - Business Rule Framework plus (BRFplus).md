10/15/26, 3:15 PM

Business Rule Framework plus (BRFplus)

Generated on: 2026-10-15 15:15:43 GMT+0000

ABAP platform | 2025 FPS02 (Oct 2026)

Public

Original content: https://help.sap.com/docs/ABAP_PLATFORM_NEW/9d5c91746d2f48199bd465c3a4973b89?locale=en-

US&state=PRODUCTION&version=202510.002

Warning

This document has been generated from SAP Help Portal and is an incomplete version of the official SAP product documentation.

The information included in custom documentation may not reflect the arrangement of topics in SAP Help Portal, and may be

missing important aspects and/or correlations to other topics. For this reason, it is not for production use.

For more information, please visit https://help.sap.com/docs/disclaimer.

This is custom documentation. For more information, please visit SAP Help Portal.

1


10/15/26, 3:15 PM

Business Rule Framework plus (BRFplus)

Use

Business Rule Framework plus (BRFplus) provides a comprehensive application programming interface (API) and user interface

(UI) for defining and processing business rules. It allows you to model rules in an intuitive way and to reuse these rules in different

applications.

Here are some examples of scenarios in which applications use BRFplus:

Validation of data and detection of invalid data and states

Matching responsibilities, suitable products, and locations

Calculation of costs, overhead, and risks

BRFplus as a technical configuration engine

Major BRFplus components include application, function, catalog, expression, action, data object.

The interface between a business rule modeled with BRFplus and an application using that rule is provided by a BRFplus function.

The function serves as a container for the entire business logic of a rule, no matter how complex it may be. Rules are implemented

as expressions which are assigned to a function. The rule input is known as context and the rule output is called result. Context and

result consist of data objects of one of the following types: element, structure, and table.

BRFplus supports features such as simulation, trace, transport, XML export and import.

This is custom documentation. For more information, please visit SAP Help Portal.

2


10/15/26, 3:15 PM

BRFplus Overview

Implementation Considerations

BRFplus is an ABAP-based framework and is therefore best suited for integration into an ABAP-based system environment, for

example, as an extension to an existing component of the SAP Business Suite. However, if your system environment is mainly Java-

based, or if you plan to implement business rules for a system landscape based on service-oriented architecture (SOA), you may

consider using the Java-based SAP Business Rules Management (BRM). SAP BRM is available with SAP NetWeaver 7.1 EhP1 or

higher.

It is also possible to implement a scenario where both components are used simultaneously: In a mixed environment with ABAP as

well as Java parts, both engines may be used in their respective area. BRFplus and SAP BRM can call each other. This means that,

for example, you can maintain rules in SAP BRM and call them via remote calls to be used in BRFplus and vice versa.

Finally, even in an SOA environment it may be a good idea to use the web services of BRFplus. This is true for scenarios where the

major part of the data to be processed is stored in an ABAP backend system. Here, using BRFplus brings advantages in terms of

performance, sizing, and the availability of the integrated workbench.

Getting Started

Use

This section provides introductory information to help you get started with BRFplus.

This is custom documentation. For more information, please visit SAP Help Portal.

3


10/15/26, 3:15 PM

Understanding the User Interface

Introduces the user interface (UI) of the BRFplus workbench.

Typical Workflow

Provides an overview of all the stages involved to model and implement business rules in BRFplus.

Before Project Start

After you have made yourself accustomed to the BRFplus workbench with the help of the first three chapters mentioned above, we

highly recommend reading this chapter before you actually start into your first BRFplus project. You will be directed to a wealth of

important, but not-so-obvious information about the concepts of BRFplus and best practices of working in that environment.

  Note

Before you begin working with BRFplus, ensure that the following SICF core services are active:

/sap/public/bc/icons

/sap/public/bc/icons_rtl

/sap/public/bc/its/mimes

/sap/public/bc/pictograms

/sap/public/bc/ur

/sap/public/bc/webdynpro/*

/sap/public/bc/webicons

/sap/public/icman

/sap/public/myssocntl

/sap/public/ping

/sap/bc/echo/*

/sap/bc/error/*

Understanding the User Interface

Use

The BRFplus user interface (UI) consists of a workbench that enables you to maintain your business rules. You can create, modify,

and delete objects. The workbench provides access to all the BRFplus objects available in a system. While the workbench enables

you to model all the BRFplus-specific rules content, it also provides some tools for integrating a BRFplus application into your host

application from which you want to call BRFplus. To accomplish this, you need to implement the respective calls in the source code

of your application. The workbench can help you with that task by generating web services, function modules, and code snippets

that you can use to connect your ABAP code to a particular BRFplus function.

You can start the BRFplus workbench in one of the following ways:

In the backend system with transaction BRFPLUS.

This is custom documentation. For more information, please visit SAP Help Portal.

4


10/15/26, 3:15 PM

In the web browser with the BRFplus workbench URL that is specific for your system landscape.

  Note

The BRFplus workbench is based on SAP Netweaver's WebDynpro ABAP technology. Therefore, you can apply generic modifiers

and parameters to the browser URL to fine-tune the workbench behavior. For example, you could add the sap-

accessibility=X switch to the URL to provide screen reader support to the UI.

Prerequisites

The role BRFplus Administrator ( SAP_BC_FDT_ADMINISTRATOR) has been added to your user profile. Of course, you can as

well use a custom role with a subset of the authorizations contained in SAP_BC_FDT_ADMINISTRATOR.

Features

The BRFplus workbench consists of two main panels, the Navigation Panel on the left and the Work Area panel on the right. The

workbench also provides a couple of general features through the Menu Bar. The System Status dialog that is available from the

Help menu shows the backend system and client where you are currently logged on, the logon user and language, and the current

UI mode.

The workbench has the following two UI modes:

Simple Mode

This UI mode is recommended for the business user. It concentrates on business-relevant settings and hides most of the

technical details that are only needed for administrative tasks.

Expert Mode

This UI mode is for the business expert or developer. In Expert Mode, you have access to a number of additional tools

needed for administrative or cleanup tasks. Besides, some of the more technical functions are only available in Expert

Mode (for example, the Return to active version function used to discard changes that have been made to an inactive

object).

You can switch between the two modes using the Personalization dialog.

This is custom documentation. For more information, please visit SAP Help Portal.

5


10/15/26, 3:15 PM

Menu

The Menu consists of the following:

Workbench

You can perform workbench operations such as create an application, show the current objects in the repository,

synchronize the object that is currently loaded into the workbench with the repository tree, and add the current object as

favorites.

Tools

The availability of tools depends on the UI mode you choose. The simple mode activates only the simulation tool. The other

tool components are available only in expert mode.

Application Administration

You can delete unused objects from the application using the application administration tool. You can also discard

old versions of objects that are no longer needed, delete objects that have been marked for deletion, and reorganize

objects.

Application Usage

You can use the application usage tool to query the applications that are being used by the selected application or

query other applications using the selected application.

Lean Trace

This tool lets you review and analyze the runtime behavior of a BRFplus function on a general level. The name "lean

trace" indicates that this tool works on a relaxed granularity level so that certain execution steps are aggregated or

completely hidden.

Mass Change

This is custom documentation. For more information, please visit SAP Help Portal.

6


10/15/26, 3:15 PM

With this tool, you can create a selection of BRFplus objects based on different criteria and then apply a particular

change to all selected objects at once.

Simulation

You can provide input for the context data objects of a function and simulate the execution for test and debugging

purposes. Simulation is similar to function module testing.

Transport Analysis

You can analyze and check the consistency of all the BRFplus objects in a transport request.

Web Service Generation and RFC Generation

A third party user can process the rules defined in BRFplus using the web service generation tool. A similar approach

is possible when you have an SAP system landscape installed and want to access a BRFplus application from a

system, but the application resides in a different system. For this, you can use the RFC Generation tool to set up the

necessary environment.

XML Export and XML Import

You can easily transport active versions of the BRFplus objects from one system to another with the help of the

BRFplus-specific XML conversion (provided both systems support BRFplus). For more information, see Export and

Import of XML Data.

Help

The Help menu lets you directly access the context-specific Application Help that is attached to the particular type of

object you are currently working on.

You can also open the Help Center pane at the right border of the window. Here, you find a link that leads you to the entry

page of the BRFplus application help from which you can explore the various help topics. In addition, the menu offers a

legend that explains the most important icons used in the workbench as well as the meaning of the typographic

conventions used in the user interface. Finally, you can find the System Information here.

  Recommendation

If you are new to the BRFplus workbench, we recommend you right-click on the UI background and choose Display

Quick Help from the context menu. You will then be provided with additional help texts on the UI (either static texts, or

texts that are only visible when you hover the mouse on a text with a green underline) meant to help you understand the

purpose of a particular screen element, or the idea behind a particular feature on that screen. Once you are accustomed

to the workbench, you can let these explanation texts disappear by choosing Hide Quick Help from the same context

menu.

Navigation Panel

You can browse through the BRFplus object repository using the Navigation Panel on the left hand side of the workbench window.

In the Personalization settings, you can decide whether the objects shall be displayed with their technical name or with their short

text.

The objects shown in the navigation panel are not simple entries in a flat list. Rather, each object is the entry point to a hierarchy of

subelements and usages. You can drill down through the object hierarchy by clicking on the triangle sign to the left of each object.

An application entry in the navigation panel serves as an entry point to the different object types of which the application consists,

all the object instances for each type, their usages in other objects, which again serve as the starting point for a new drilldown.

For each object, the system provides a visual indication of the object's status:

This is custom documentation. For more information, please visit SAP Help Portal.

7


10/15/26, 3:15 PM

Object type: The symbol to the left of an object's name indicates what type of object it is (application, various expression

types, functions, and so on)

Typeface: Objects shown in bold characters are transportable (otherwise, they are local to the current system).

  Note

This setting is inherited from the application to which an object belongs. Whether an application is transportable or not

depends on the development package to which the application is assigned.

Traffic light: Objects with a green traffic light are active and can be used in an application.

The BRFplus objects presented in the Navigation Panel can be arranged in different views. In the Personalization settings, you can

define for each view whether it shall be displayed or not. In addition, you can define which of the different views shall be active

when the system starts up. The following views are available:

Repository

You can access all objects of all applications in the repository. The Repository view allows for an in-depth analysis of an

object via a recursive drilldown into the object's subobjects as well as into the object's where-used list.

Recently Used

You can easily access those objects that you have recently been working on. This list can hold up to 20 objects. Its content

is automatically maintained by the system, following the “first in, first out” approach.

Favorites

You can view all the objects that you have added as your favorites. This is useful if you want to keep a permanent list of

objects you are interested in but do not work with every day. To add an object to the Favorites view, first locate the desired

object in the Repository view and then choose Add to Favorites from the object's context menu.

Catalog

You can define catalogs that serve as a container for a subset of objects and access it from the repository.

  Note

The Recently Used and Favorites views present a flat list of objects without the additional drilldown capabilities of the

Repository view. However, you can easily access the drilldown function by choosing Show in Repository View from each

object's context menu.

Work Area

The work area panel is the place where you can display and edit objects. On top of the screen, the system displays the General

section with the header data of the object. This section is generic and is available for all types of objects supported by BRFplus. The

settings that are specific for a particular object type are shown in the Details section below the General section.

Check Results

Under certain conditions, the work area may contain a third section, namely Check Results. For each object type available in

BRFplus, the system offers type-specific consistency checks that are implicitly run upon object activation. You can also start the

checks manually by clicking the Check button in the workbench. Whenever the checks find any kind of problem (be it serious or

not), the system displays the Check Results section on top of the work area and lists all messages that have arisen during the

check. You can then start investigating the problems. The message list stays visible on the screen until you explicitly close the

Check Results section with the Close button.

This is custom documentation. For more information, please visit SAP Help Portal.

8


10/15/26, 3:15 PM

Sometimes, the checks return a great number of messages, depending on the complexity of the checked object and its

relationships to other objects. In such a case, navigating through those many messages in the relatively small section can be

cumbersome. To overcome this problem, the Check Results section offers a download facility that lets you save the entire message

list in a Microsoft Excel file. With that, getting an overview is much easier, and you may want to use the spreadsheet as a worklist

that helps you keep track of all the issues that you have already solved and those that are still to be done.

System Info

The System Info dialog available from the Help menu provides the following administrative data related to the running session:

System

System ID

System client to which you are logged on

System mode (either regular or deployable; deployable mode is relevant only for Business ByDesign systems)

User

User name

Logon language

Current UI mode ( Simple vs. Expert, see section above)

Timezone used for object timestamps (local time of the logged on user, or UTC). This setting can be changed in the

Personalization dialog.

Keyboard Support

Using the mouse is not always the fastest way to interact with the workbench. You can access the Workbench as well as the Tools

menu via the keyboard by typing  Alt +  W  or  Alt +  T , respectively. Also, a list of standard user actions is available that you can

execute with the help of keyboard shortcuts. These shortcuts can be customized in the Workbench Personalization dialog.

More Information

Workbench Personalization

Workbench Personalization

Definition

The BRFplus workbench is the central place for modeling and testing business rules. BRFplus offers many opportunities to

configure the look and feel of the workbench so that it best suits your individual requirements. To access the personalization

settings, choose

 in the upper right corner of the workbench window.

  Note

Most of the changes that you make to the personalization settings are effective immediately after closing the Personalization

dialog and navigating to another object. However, some of the personalization settings require that you restart the workbench

before changes take effect.

Features

This is custom documentation. For more information, please visit SAP Help Portal.

9


10/15/26, 3:15 PM

User Mode

BRFplus addresses business users as well as business experts and developers. Since both types of users have different

requirements concerning their working environment, and since sometimes the same person has to act in both roles, BRFplus lets

you customize the BRFplus workbench according to your needs. This includes the possibility to differentiate the look and feel of the

workbench between two role-oriented modes per user, simple mode and expert mode.

The user mode setting has two aspects:

Scope for personalization settings

The changes that you make to the personalization settings are recorded by the system with respect to the currently

selected user mode. That is, if you change for example the Views settings in simple mode, this does not affect the Views

settings for expert mode and vice versa.

User mode selection

When you open the personalization dialog, the system displays the user mode that is currently in effect in the workbench.

To change the user mode, make the desired selection and choose Save. The system adapts the workbench rendering

according to the settings that have been defined for the newly selected user mode.

  Note

As a system administrator, you can create additional modes tailored to the needs of different users or roles in your company. By

default, these custom UI modes inherit their settings from simple mode unless you explicitly change a particular setting. In

addition, custom UI modes can be used to integrate additional tools, web services, or Web pages into the BRFplus workbench.

Categories

The personalization settings are grouped into the following categories:

General

Settings for cross-area aspects and the system startup behavior

Views

Settings for controlling the availability of the different workbench views

Repository

Settings for controlling the behavior of the Repository view

Catalogs

Settings for controlling the behavior of the Catalog view

Expression

Settings for specific expression types

Filters

Settings for defining object filters

The system has predefined default values for all of the personalization settings. If you should ever run into problems because of

changed settings, you can simply click the Restore Default Settings button to return to the system defaults.

General

This is custom documentation. For more information, please visit SAP Help Portal.

10


10/15/26, 3:15 PM

Maximum Number of Query Results

With this setting, you can define an upper limit for the number of matching items that the system displays in response to a

query. Reducing this number can be helpful if your system contains very many objects and you are experiencing slow

system performance. This setting affects the object lists presented by the system when you search for an existing object. If

the number of matching objects for a query is higher than the setting that you define here, the system notifies you

accordingly. You can then decide either to increase this value or to refine your search criteria.

Default: 200.

  Note
The number of objects listed in the Repository view is not affected by this setting. Here, the system always displays all

objects that were found as the result of the last search action that you have performed.

Show Technical Names

With this setting, you can define whether the system shall use the technical name or the short text for displaying objects.

Using the short text is normally more convenient since this text is in natural language and may be translated into different

languages. The technical name, however, has the advantage of remaining the same, regardless of the logon language. This

can ease communication between persons who use to log on to the system with different languages.

This setting affects the display behavior in the workbench navigation panel as well as in the work area header for an object

that you are currently working on, and also for all references to dependent objects (for example, all rules in a ruleset, the

data objects used by an expression, and so on).

Show Technical Aspects

With this setting, you can control whether or not the system shall display those tools in the Tools menu that are more

technical in nature and meant for system administrators and programmers, like Application Administration or XML Export.

For business users, we recommend that you keep this setting off to avoid confusion.

Show Technical Attributes

With this setting, you can define whether the system shall display additional technical data for some of the BRFplus objects.

For example, you can see the internal IDs of a decision tree node or of a catalog node. This data is mostly needed for

technical investigations and debugging and not necessary for business users.

In addition, this setting controls whether the number of decimal places of an elementary data object with subtype Amount

is visible. This information is ignored anyway because at runtime, the number of decimals for an amount is automatically

derived from the central settings in the currency tables. In other words, displaying the number of decimals for an amount

data object or not does not make any difference for the system behavior.

  Note

The common nature of all the data that is controlled by the Show Technical Attributes flag is that setting this flag or not

does not impose any functional restrictions on the user. This is the major difference to the Show Technical Aspects

setting discussed in the earlier section, which is used to hide major parts of the tool functionality from the user.

Show XML Schema

With this setting, you can define whether during XML export, the user can decide which XML schema shall be used for the

data to be exported. If you leave this setting switched off, the user cannot influence the schema selection. In that case, the

system uses the internal schema by default.

Object Timestamps Based on UTC Reference Time

With this setting, you can decide how the system shall render the object-related timestamps. This setting affects the

creation date and time as well as the change date and time of an object, the timestamps of object versions, and the validity

period of rule objects. It has the following effect:

This is custom documentation. For more information, please visit SAP Help Portal.

11


10/15/26, 3:15 PM

On

All displayed timestamps are transformed into their UTC equivalent (UTC = Universal Time Coordinated). This

provides you with a standardized time base for all BRFplus objects in the system, regardless of where, when, and by

whom they have been created or changed. This setting is recommended whenever you have to compare, or operate

on, objects based on their timestamps.

Off

All displayed timestamps are shown according to the timezone settings of the user who has created or saved an

object. This setting is normally considered convenient from a user's perspective, but can lead to confusion if

different users in different timezones are working on objects in the same system and you need an overview over

different objects based on their timestamp.

In summary, using UTC timestamps is advisable for administrative tasks with lots of objects to be processed, while local

timestamps help the user to better understand when a particular object has been created or changed.

  Note
The timestamp setting has no effect on date and time values that you use in data objects of type timepoint, nor on date

and time functions in formula expressions. Here, the system always expects UTC timestamps.

General Section Expanded

With this setting you decide whether the system shall display an object's administrative data by default or not. If you switch

this setting on, the system expands the General section on top of the work area whenever you navigate to a BRFplus object.

This gives you a comprehensive overview of all the data recorded for an object, but displaying the data consumes some

space on the UI. Switching this setting off hides this information and grants you considerably more space for effective work

with the object settings.

Views

On this tab, you can define which of the different views shall be offered in the workbench navigation panel, and which one of the

selected views shall be presented when the workbench is started. This setting provides some built-in consistency checks to make

sure that at least one view is selected, and that the default view is among the selected ones.

Repository

Include in Repository

With this setting, you can define which objects shall be presented in the Repository view of the workbench, depending on

their storage type. You can, for example, decide that system objects shall be hidden as you would not change these anyway.

You can also control whether you want to see a dedicated column for the transport behavior of each single object in the

navigation panel (Display Transport Column). However, since the transport behavior of an object depends on application-

wide settings you may decide that you rather hide this column so that additional space is available to show the object

names.

The same holds for the Display Change Date Column. If you decide to have this column displayed in the repository tree, the

system does the following:

A Change Date column is added to the tree, showing when the current object has last been changed.

When you expand an object's node, an additional category Last changed (<number of changed objects>) is

displayed. This category is then broken down by different predefined period categories (for example, Today, Last

Week, and so on) where you can find the depending objects of the top level object grouped by the date of their last

change. Note that the period names (last week, last month, and so on) should be understood as indicators of the

period duration, not as calendar dates. For example, the period category Last Week means "changed within the last

7 days", not "changed in the previous calendar week".

This is custom documentation. For more information, please visit SAP Help Portal.

12


10/15/26, 3:15 PM

In the Display Last Changed Objects dropdown list, you can specify the number of objects that you want to see in

the Last Changed category. Keeping this number small can improve the system performance. If, however, the

number that you specify is lower than the number of objects that exist in that category, the system makes you aware

of that by changing the display style to Last changed (<number of changed objects>/<total number of objects>).

Deleted Objects

BRFplus provides a multilevel deletion strategy that is used to keep objects in the system available for a defined period of

time although, from a business perspective, they are considered obsolete or no longer needed. With this setting, you can

decide whether such objects shall be displayed in the Repository view or not.

Object Grouping in Applications

You can decide how the system presents the objects that belong to an application. You can choose from the following

alternatives:

Types and Subtypes: Objects are grouped by their type and subtype, if applicable. With this setting, within an

application, you find, for example, an entry Expressions (= object type), followed by the different Expression types (=

subtype), followed by the objects of this type. This setting is useful for applications that contain a high number of

objects as it provides you a better overview and can improve the system performance because the number of

objects to read from the database is reduced. On the other hand, navigating to an object requires more mouse clicks

and the additional tree levels lead to a higher likelihood of cut-off object names.

Types: Provides a one-level grouping of objects and serves as a compromise between the Types and Subtypes and

the Flat List setting.

Flat List: All objects within an application are listed in alphabetical order, regardless of the object type. This setting is

suitable for giving you a quick overview of small applications but can lead to significant performance issues when

used with applications containing a high number of objects.

Catalogs

With this setting, you can define which of the object catalogs in the system shall be available in the Catalog view of the workbench

navigation panel, and which one of these shall be presented by default.

Catalogs are a means to reduce complexity and to protect the user from getting lost in the multitude of objects that may exist in

the system. This principle of complexity reduction is further enforced by the concept of catalog personalization. As opposed to the

Repository view, where all objects belonging to an application or being part of a search result are presented, the system does not

present all existing catalogs in the Catalog view. Rather, using the Catalog view requires that you choose one of the following

options:

In the Repository view, choose Display in Catalog View from the context menu of a catalog object.

Configure the view in the Personalization dialog. This configuration is done in a two-step procedure:

1. Click the Add button and select from the list of all catalogs in the system the ones that you want to make available in

the Catalog view.

2. From the catalogs that you have selected in the previous step, make one the default catalog by clicking the Is

Default column.

Once you are done with the view configuration, you can use the Catalog view. When you open the Catalog view, the system

presents the default catalog. All other catalogs that you have selected as your personal catalog list are available via Switch

To Other Catalog in the Catalog view.

  Note

It is possible to bypass the preparatory steps for catalog use outlined above. In the Repository view, choose Display in Catalog

View from the context menu of a catalog object. The system then swaps from Repository view into Catalog view, with the

This is custom documentation. For more information, please visit SAP Help Portal.

13


10/15/26, 3:15 PM

selected catalog ready for use. Although this mechanism is not recommended for daily use, it is definitely helpful for test

purposes when you are about to define a new catalog and want to have a quick look at the result.

In contrast to all other settings in the Personalization dialog, the system does not make a difference between the user modes

with respect to catalogs. In other words, there is only one set of catalog settings that is effective both for Simple Mode and

Expert Mode.

Expression

On this tab, you find additional settings for some of the more complex object types available with BRFplus.

Decision Table

Show Table Settings

When you are editing a decision table expression, the system initially hides the detailed definition screen for column and

row settings. If you want to change this definition, you first have to click the

 button at the rightmost border of the Detail

section toolbar. With the Show Table Settings setting, you can define whether this button shall be displayed or not. If you

decide to hide the

 button, a user has no access whatsoever to the row and column definition, but can still create and

maintain rules in the table. This setting can be useful to protect very complex decision tables from unwanted changes.

Display Row Numbers

Indicates whether the system displays an additional column for the row numbers. Displaying row numbers is helpful for

orientation in tables with many rows, and even inevitable when it comes to discussions on certain table content between

different persons. On the other hand, displaying a row number column occupies space that could otherwise be available for

data columns.

  Note

If you decide to let the system display the row number column, you can still move that column via drag&drop to any

desired position. It is not designed to always occupy column number 1. Dragging it to a position more to the right can

free some space for data columns but still gives you a chance to always find out the current row number.

Number of Visible Rows

With this setting, you limit the number of rows that are shown for a decision table at once to a particular amount. This is

useful in case of large decision tables with several thousands of rows that otherwise would lead to performance problems.

Of course, you can scroll down to see the other rows. The system then reads the required table rows from the database and

displays them accordingly.

Minimum Columns for Horizontal Scrollbar

With this setting, you define the lowest number of columns in a decision table that lets the system display a horizontal scroll

bar. Tables with a complex structure and many fields tend to have a wide horizontal scroll range, so that it is impossible for a

user to have a complete overview of the entire table row. When you increase this setting, the system reduces the width of all

columns so that the given number of columns is displayed. Only if there are still more columns beyond that limit, the system

displays a scroll bar. Increasing the number of columns reduces the column width and can sometimes lead to cropped cell

content (though still accessible via the cell tooltip), but lets you benefit from a better overview of the table content.

  Note
The system takes all table columns into account that are actually displayed when it calculates the column width. This

includes result data columns as well as the row number column that can be displayed on demand, whereas columns that

have been hidden in the table settings are ignored.

Ruleset

This is custom documentation. For more information, please visit SAP Help Portal.

14


10/15/26, 3:15 PM

Number of Rules Expanded

With this setting, you limit the number of rules that are shown for a ruleset in expanded form to a particular amount. This is

useful in case of large rulesets with dozens of rules inside that otherwise would lead to performance problems. The rules

that are beyond the value that you enter here are initially displayed with only one line per rule. You have to expand them

manually to see their details.

Show Ruleset Header

This setting lets you control whether a ruleset object that you load into the workbench is displayed with the ruleset header

data section expanded or not. The header section contains some administrative data describing the ruleset, plus

information on the ruleset variables. Depending on the complexity of the ruleset, especially the variables listing can

consume a lot of space on the screen. It can therefore be preferable to leave this option unchecked so that the available

space can be used for displaying the rules without having to scroll. By default, this option is not set.

Show

Filters

On this tab, you can maintain the assignment of object filters to applications. With the Add button, you create a new filter

assignment. For each assignment, you can choose whether the filter shall be applied to all applications in the system or not. If not,

you can create additional lines per filter to define the individual applications for which a given filter is in effect. If you switch the All

Applications setting from No to Yes, all individual assignments that you may have defined are lost.

  Note
Maintaining filter assignments is an administrative task and should normally be done in a system-wide consistent manner

rather than being seen as an individual preference of single users. Therefore, this tab is mainly meant for information purposes

and presented in read-only mode for most of the users.

Hotkeys

On this tab, you find a predefined list of user actions that are commonly used across all kinds of BRFplus object types, like saving,

deleting, checking, and so on. For each of these actions, you can define a custom hotkey out of a list of possible hotkeys that

encompasses the following ranges:

CTRL +  0 ...  CTRL +  9

CTRL +  A ...  CTRL +  Z

CTRL +  F2 ...  CTRL +  F12

  Note

If a user action that is associated with a hotkey is unavailable (for example, the Back button is disabled if there has been no

previous navigation step yet), then the hotkey is propagated to the web browser and might trigger an action that has been

associated with that hotkey by the browser manufacturer. For example, the Back action is by default associated with the

CTRL +  B  hotkey. If the Back button is disabled, pressing  CTRL +  B  would instead trigger the Organize Favorites function

defined in Microsoft Internet Explorer, or open the Bookmarks sidebar in Mozilla Firefox.

In contrast to the aforementioned behavior, the  CTRL +  F4  hotkey is handled directly by the operating system. Pressing this

key always leads to the current browser tab closing immediately, without giving a user the chance to decide whether this is

wanted or not. Since BRFplus cannot override this behavior, the  CTRL +  F4  hotkey is not offered in the list of assignable

hotkeys.

This is custom documentation. For more information, please visit SAP Help Portal.

15


10/15/26, 3:15 PM

Custom UI Modes

Explains how you can define additional UI modes of the BRFplus workbench to better adapt the tool to your company's needs.

The BRFplus workbench is shipped with two predefined sets of UI settings, Simple Mode and Expert Mode. Although an end user is

free to modify the settings that are currently in effect, the multitude of different settings that are offered in the Personalization

dialog may sometimes be confusing. Also, from an end user support perspective, it can be desirable to have a unified set of

settings assigned to the BRFplus users in your company.

As a system administrator, you can create additional UI modes tailored to the needs of different users or roles in your company. By

default, these custom modes inherit their settings from simple mode unless you ecplicitly change a particular setting. In addition,

custom modes can be used to integrate additional tools, web services, or web pages into the BRFplus workbench. Once you have

defined such additional tools, an Extensions button appears in the toolbar of the BRFplus workbench. Clicking the button presents

a menu of the different tools you have defined.

To accomplish this, you need to create a class that implements the IF_FDT_WD_UI_MODE~GET_CONFIGURATION interface

method. Here is an example of how this can be done:

METHOD if_fdt_wd_ui_mode~get_configuration.

    ro_configuration = super->if_fdt_wd_ui_mode~get_configuration( ).

    DATA: lth_customer_tools TYPE if_fdt_wd_configuration=>th_customer_tools,

          ls_customer_tools  TYPE if_fdt_wd_configuration=>s_customer_tools.

    ls_customer_tools-position = '1'.

    ls_customer_tools-menu_type = if_fdt_wd_configuration=>gc_ct_menu_type_action_item.

    ls_customer_tools-description = 'Our homepage'.

    ls_customer_tools-url = 'HTTP://www.mycompany.com'.

    INSERT ls_customer_tools INTO TABLE lth_customer_tools.

    CLEAR: ls_customer_tools.

    ls_customer_tools-position = '2'.

    ls_customer_tools-menu_type = if_fdt_wd_configuration=>gc_ct_menu_type_action_item.

    ls_customer_tools-description = 'My favorite Tool'.

    ls_customer_tools-url = 'HTTP://www.mycompany.com/?mytool.js'.

    INSERT ls_customer_tools INTO TABLE lth_customer_tools.

    ro_configuration->set_customer_tools ( lth_customer_tools  ) .

ENDMETHOD .

Once you are done with defining the desired menu items, you need to write a simple report to launch the BRFplus workbench with

the changed settings as defined in the method shown above:

REPORT  zstart_brfplusworkbench.

DATA: lo_ui_execution    TYPE REF TO if_fdt_wd_ui_execution,

      lo_ui_mode         TYPE REF TO if_fdt_wd_ui_mode.

*********************************************************************

lo_ui_execution = cl_fdt_wd_factory=>if_fdt_wd_factory~get_instance( )->get_ui_execution( ).

This is custom documentation. For more information, please visit SAP Help Portal.

16


10/15/26, 3:15 PM

CREATE OBJECT lo_ui_mode TYPE zcl_fdt_wd_ui_simple_mode.

lo_ui_execution->set_ui_mode( lo_ui_mode ).

"Standard call to launch the workbench

lo_ui_execution->execute_workbench( ).

  Note
When you start the BRFplus workbench with a modified configuration as shown in the sample code snippets, the Workbench UI

mode is set to Simple Mode and cannot be changed to Expert Mode during the session.

Typical Workflow

Use

The following steps describe the typical workflow of integrating BRFplus functionality into your application.

  Note

Note that in the following overview, the term "application" which is used in the first as well as in the last step refers to two

different, but related concepts:

In the first step, Create an Application, "application" refers to the BRFplus element type Application which serves as a

super-ordinate object for collecting all objects used to model the business logic that you want to integrate into your

solution.

In the last step, Integrate with Application, "application" refers to your solution which you want to enhance by the

business logic encapsulated in the BRFplus rules.

Procedure

This is custom documentation. For more information, please visit SAP Help Portal.

17


10/15/26, 3:15 PM

Business Rule Workflow

1. Create an application.

For more information, see Creating an Application

2. Create a function.

For more information, see Creating a Function

Assign context and result to the function.

For more information, see Assigning Context and Result to a Function

Assign top expression to the function.

For more information, see Assigning Top Expression to a Function

3. Activate the objects.

4. Simulate the function.

For more information, see Simulating a Function

5. Integrate the BRFplus function with your application.

Before Project Start

Summary of valuable information worth knowing before you start a BRFplus project.

This is custom documentation. For more information, please visit SAP Help Portal.

18


10/15/26, 3:15 PM

In this chapter, we have compiled a comprehensive list of topics worth to consider before you start a BRFplus implementation

project. The purpose of this compilation is to help you avoid running into a wrong direction when you proceed on your way through

a project. This holds especially for some less obvious concepts in BRFplus where things may look easy at first glance but can have

significant implications at a later stage in the project, depending on which decisions you take.

By raising your awareness for the topics mentioned in this chapter at an early point in time, we hope to protect you from finding

yourself in a dead-end street at some point in time, and from having to make time-consuming and tedious corrections to the rules

you may have modeled so far. The selection of topics is based on years of project experience with BRFplus, both inside and outside

SAP. The target of this overview is to present important topics in a condensed manner and to point you to the places in this

documentation as well as to selected material on SAP's Web site where you can find more details.

UI Configuration

It may sound surprising, but the way you define the personalization settings in the BRFplus workbench may have a significant

influence on how well you can get an overview of your project. Some of the major (and often unrecognized) aspects here are:

The possibility to hide or display objects that are deleted or have been marked for deletion (see also the Object States

section below).

The option to display a column indicating when an object has last been changed in the repository tree.

The dependency tree that is available for each object shown in the navigation pane that lets you find out easily everything

about the usage relationships of your rule objects.

For more information, see:

Understanding the User Interface

Workbench Personalization

Object Names

For the technical names of the objects that you create in BRFplus, certain formal restrictions apply that you have to follow. For

more information, see:

Naming Conventions for BRFplus

However, while the system checks automatically the formal correctness of technical names, there is more to names than the

technical view alone. From a project perspective, it is even more important to assign self-explaining and easy-to-understand names

to all of your objects to make it clear what purpose each of your objects serves. We therefore recommend making extensive use of

the Text, Short Text, and Documentation fields that are provided for each BRFplus object. For more information, see:

Administrative Data

Object States

BRFplus objects can take different status values throughout their lifecycle, starting with status inactive, followed by their

productive status active, and finally leading into different states of obsolescence and deletion. The state of an object (in

combination with versioning and personalization settings) controls which particular version of an object is actually executed at

runtime, and whether an object is visible in the BRFplus workbench or not. With respect to the various deletion states, it is

especially important to consider the implications that may arise from object dependencies in scenarios where objects are involved

that have a status like deleted but still exist physically in the system. For more information, see:

Creating Objects

This is custom documentation. For more information, please visit SAP Help Portal.

19


10/15/26, 3:15 PM

Deleting Objects

Versioning

Storage Types

All objects in BRFplus are assigned to an application object. The application has a storage type property indicating the purpose of

the objects belonging to the application. Each object inherits this setting from the application. Depending on the storage type, the

transport behavior of the objects is different. We therefore recommend clarifying the storage types that you want to use at an early

project stage. With that, it is easier to avoid running into deadlock situations where transporting your rule objects might be difficult,

if not impossible. For more information, see:

Storage Types

Access Level

In many projects, it is clear right from the start that besides a number of highly specific rules and calculations there will also be a

notable number of objects that are needed by all, or many, of the specific parts in the same way. Such highly used objects are

natural candidates for reuse, and you can accomplish this by assigning your objects the right access level. Assigning one of the less

restrictive access levels to an object makes it available across application boundaries. For more information, see:

Setting an Access Level

Object Lifecycle

All of the objects that you create in BRFplus go through a well-defined lifecycle. Depending on the lifecycle phase, certain object

settings can be modified while others cannot. Also, the object behavior may vary depending on its lifecycle phase. For more

information, see:

Creating Objects

Deleting Objects

Versioning

Versioning

BRFplus comes with a sophisticated versioning system that you can individually adjust to the needs of your project. But before you

start having the system create one version after another, there are several questions that you should be aware of, including the

question whether it might be better not to use versioning. For more information, see:

Versioning

Transport

(more information to follow in one of the next support packages)

XML Exchange

When it comes to transferring BRFplus objects from one system to another, there is a built-in alternative to the sometimes slow

and inflexible Change and Transport System (transaction SE09). In BRFplus, you can transfer single objects as well as entire rule

applications with the help of an XML exchange service. For more information, see:

This is custom documentation. For more information, please visit SAP Help Portal.

20


10/15/26, 3:15 PM

Export and Import of XML Data

In addition, you can gain maximum performance and flexibility in terms of deploying rule objects in your system landscape with

SAP NetWeaver Decision Service Management, which is available as a separately licensed add-on solution.

Troubleshooting

(more information to follow in one of the next support packages)

Administration

Related Information

Integration with SAP Cloud Platform Business Rules

Inbound Communication

Outbound Communication

Integration with SAP Cloud Platform Business Rules

Related Information

Inbound Communication

Outbound Communication

Inbound Communication

For inbound communication, you have to create destination, managed system and activate the ODATA services.

For more information, see

Configuring Destinations.

Activating OData Services.

Activating OData Services

Context

The following procedures are only relevant for on-premise installations and should be performed in the back-end server.

Procedure

1. Start transaction /IWFND/MAINT_SERVICE.

2. Choose Add Service and set the following parameters.

System Alias - LOCAL or the name of your system alias

Technical Service Name - RULE_INBOUND_SRV

This is custom documentation. For more information, please visit SAP Help Portal.

21


10/15/26, 3:15 PM

External Service Name - RULE_INBOUND_SRV

3. Choose Get Services.

4. In the Select Backend Services list, select the service you created, then choose Add Selected Services.

5. In Add Service, set Package Assignment as $TMP or choose local object.

6. Choose Confirm.

Outbound Communication

For outbound communication, you have to create HTTP destinations, maintain communication and configure OAuth client.

Creating HTTP Destination

Procedure

1. Log on to the SAP S/4HANA system.

2. Go to transaction SM59.

3. Choose HTTP Connections to External Server (Type G).

4. Create a new HTTP destination by following the steps.

5. Provide the following details in Table Settings section.

Option

Description

Host

Port

https://bpmrulesrepositoryrules-<sap cloud platform

subaccount-id>.<datacenter id>.hana.ondemand.com

Maintain 443 for HTTPS connection.

Path Prefix

Not required.

Proxy Settings

Maintain if applicable.

6. Provide the following details in Logon & Security section.

Option

Description

User/Password

Provide the user credentials of SAP Cloud Platform account.

SSL

Active

SSL Certificate

Provide default SSL Client (Standard).

7. Maintain STRUST settings if applicable.

Maintaining Communication Settings

Procedure

1. Log on to the SAP S/4HANA system.

This is custom documentation. For more information, please visit SAP Help Portal.

22


10/15/26, 3:15 PM

2. Go to transaction FDT_CP_SETTING.

3. Choose  Display

 Change .

4. Choose New Entries.

5. Provide the created HTTP destination in RFC Destination.

6. Choose Save.

Configuring OAuth Client

Prerequisites

If SAP Cloud Platform Business Rules is in the Cloud Foundry environment, you have determined the service configuration

parameters. For more information, see Determine Service Configuration Parameters.

Context

  Note

The following procedure is applicable only if the OAuth configuration is done in SAP Cloud Platform system.

Procedure

1. Log on to the SAP S/4HANA system.

2. Go to transaction OA2C_CONFIG.

3. Choose Create, then provide the following details.

Option

Description

OAuth 2.0 Client Profile

Choose FDT_CP_OAUTH2_CC from the dropdown menu.

OAuth 2.0 Client ID

Provide the client ID, which you have generated in creating

OAuth client.

4. Choose OK.

5. For SAP Cloud Platform Business Rules in the Neo environment, create a new client by providing the following details:

Option

Description

Client Secret

Provide the secret or password, which you have generated in

creating OAuth client in cloud platform system.

Authorization Endpoint

oauthasservices-<sap cloud platform subaccount-id>.

<datacenter-

id>.hana.ondemand.com/oauth2/api/v1/authorize

Token Endpoint

oauthasservices-<sap cloud platform subaccount-id>.

<datacenter-id>.hana.ondemand.com/oauth2/api/v1/token

Client Authentication

Basic

Resource Access Authentication

Header Field

This is custom documentation. For more information, please visit SAP Help Portal.

23


10/15/26, 3:15 PM

Option

Selected Grant Type

Client Credentials

Description

6. For SAP Cloud Platform Business Rules in the Cloud Foundry environment, create a new client by providing the following

Description

Client Secret

Provide the secret or password, which you have generated in

creating OAuth client in cloud platform system.

Authorization Endpoint

url

Token Endpoint

url /oauth/token

Client Authentication

Basic

Resource Access Authentication

Header Field

Selected Grant Type

Client Credentials

details:

Option

7. Choose Save.

Concepts

Use

This section explains the basic concepts involved in defining and processing of rules. Among others, the following topics are

covered:

Applications

Storage Types

Naming Conventions for BRFplus

Administrative Data

Context and Result

Data Objects And Types

Binding

Comparison Operations

Expressions

Action Types

Function

Modes of Operation

Rule

Rule Set

This is custom documentation. For more information, please visit SAP Help Portal.

24


10/15/26, 3:15 PM

Catalog

Object Filter

Versioning

Creating Objects

Deleting Objects

Export and Import of XML Data

Application

Use

A BRFplus application object is a container of different BRFplus objects. You can think of the BRFplus application as a reflection of a

particular system functionality that you want to enhance by some business rules modeled with BRFplus. It is then recommended to

collect all the BRFplus objects that contribute to a given system functionality in one BRFplus application.

Features

Object Hierarchy and Application Assignment

The application object type is located at the highest level in the classification hierarchy for objects. Nevertheless, you can define as

many applications as you like. All objects must be assigned to an application. The system supports you to accomplish this by

offering two ways of assigning an application to an object:

You can create new objects out of the context of a given application by choosing Create Object on the Contained Objects

tab of the application. All objects created this way are automatically assigned to the application from which you started.

You can create new objects from the navigation panel of the BRFplus workbench. In this case, you have to create the new

object with the help of the context menu of one of the already existing objects. The new object is then assigned

automatically to the same application as the object from which you started.

  Note

In case of a system that is completely empty with no BRFplus objects inside at all, you would start working in the BRFplus

workbench by choosing  Workbench

 Create Application .

Storage Types

There are three types of application referred to as storage types:

System application (default)

Master data application

Customizing application

Depending on the storage type, the system behaves differently when it comes to system transports. System and customizing

applications can be local while master data applications are always local. The storage type as well as the locality setting of an

application is inherited by all objects that are assigned to that application. All three types of application can be assigned to a

development package.

This is custom documentation. For more information, please visit SAP Help Portal.

25


10/15/26, 3:15 PM

Customizing applications delivered by SAP are always installed in client 000 in systems located at the customer site. If you need to

copy such an application into a system client that is used for development, you can accomplish this with the help of a transport

request of type Customizing. For further details, refer to SAP note 1908227

.

  Note

The storage type must be defined when you create an application. Once the new application has been created, this setting

cannot be changed anymore.

Versioning

Like all other types of objects, you can decide whether the system should keep the previous versions of an application in the

system database after the application has been modified. In addition, you can also define a default versioning setting for objects

that you newly create and add to the Contained Objects list of the application. The newly created objects inherit the versioning

setting that has been defined by the application.

  Note

The inherited versioning setting of an object is a default setting only and can be changed individually for each object at any

time.

Keep in mind that the versioning default setting for objects assigned to the application does not affect the versioning behavior

of the application itself. The versioning setting for an application object is controlled in the same way as for all other object

types.

  Note

Under certain circumstances, using object versions can lead to potential side-effects, which can lead to error situations that are

difficult to resolve. This is why SAP has decided to qualify the default versioning modes Versioning On as well as Versioning

Enforced as "not recommended". For more information, see Versioning: Pros and Cons.

Further Settings

An application also offers attributes for the application component and the software component. The application component and

software component have to be the same as defined for the development package. The application and software component are

automatically derived from the development package if they are not set explicitly.

An application also helps you control reuse, changeability, and visibility with access levels.

  Recommendation

For the definition of the development package, application component, and software component, we recommend that you

choose the same values that are in effect for the software solution that you want to enhance by a new BRFplus application. This

simplifies all activities related to the software infrastructure, especially transports.

Restrictions and Interdependencies

The settings for development package, application component, and software component of an application (and the objects

belonging to an application) are partially dependent on each other. The following restrictions apply:

The development package assigned to an application determines whether the application is either transportable or local.

The definition of an application as transportable or local is irreversible. Once the application has been saved for the first

time, this setting cannot be changed anymore. If you try to reassign a local application to a transportable package or vice

versa, the system rejects this and sends an error message.

This is custom documentation. For more information, please visit SAP Help Portal.

26


10/15/26, 3:15 PM

For a local application, defining a software component is not needed. As opposed to that, for a transportable application it is

essential to define the software component because the SAP transport system is based on this attribute.

Application Exit Class

If your application requires special processing routines (for example, for auxiliary calculations, validations, etc.), you can

implement such additional functionality with methods of an ABAP class. These methods can then be used, for example, to extend

the functionality of a formula expression in the form of additional formula functions. The exit class must be registered for the

application to which it belongs. To accomplish this, fill in the name of the class in the Application Exit Class field.

For an application exit class, the following applies:

For a BRFplus application, you can define no more than one exit class.

An application exit class must implement the IF_FDT_APPLICATION_SETTINGS interface.

Once you have started to use the functionality provided by an exit class, we highly recommend not to change the exit class

assignment from that point in time. If changes to the functionality are needed, try to implement this within the scope of the

already assigned class.

  Note

If, for whatever reason, you cannot avoid changing or deleting the exit class assignment of an application, you have to

check manually where the implemented functionality has already been used. For each usage, you are responsible for

either providing a workaround or canceling the using object. Be aware that these usages may be hard to find (for

example, a formula expression using a function that used to be provided by the exit class to be changed).

Object Type-Specific Settings

While all of the aforementioned settings directly affect the application itself, there is another set of settings used to control the

properties and behavior of particular object types that are created inside of the application's scope. The following application-wide

settings can be made on the Miscellaneous tab:

Setting

Comment

Restart Rule Set Enabled

Processing rule sets can be done in two different modes:

Standard mode: All rules in a rule set are executed one after

another. Processing stops either after the last rule in the

rule set has been processed or if an exit condition is met.

Deferred mode: Like standard mode, but with the possibility

to restart the rule set processing at the point where it had

stopped due to an exit condition.

With this setting switched on, rule set processing in deferred mode

is supported.

Secondary Database Connection

Expressions of type Procedure Call (subtype Database Procedure)

and Dynamic Database View can operate on database objects not

only in the local database, but also in an alternative database

belonging to a different system, or even in a stand-alone database

that is not part of an SAP system. With this setting, you can choose

a database from the database connections that have been defined

in the local system. The system offers all entries that have been

maintained in backend transaction DBCO. If a secondary database

has been maintained for an application, the Procedure Call and

This is custom documentation. For more information, please visit SAP Help Portal.

27


10/15/26, 3:15 PM

Setting

Default Settings for New Objects

Comment

Dynamic Database View expressions in that application

automatically refer to the secondary database.

All BRFplus objects have a number of administrative data fields in common. For some of these fields, it is very likely that for the

majority of objects in an application, the respective settings are identical. Therefore, it is possible to define default values for these

fields on application level so that newly created objects carry these default values. The values can of course be changed if need be.

Setting

Comment

Application Log Object, Application Log Sub Object

Defines the application log objects used for recording the log

Save Log Data

Default Enforcement

entries that are created by objects belonging to the application (for

example, actions of type Log Message). For more information, see

Log Message Action.

Controls whether the log data shall be permanently stored in the

database or not. If not, log data is only kept in memory during

runtime and is lost after the session.

Controls if and to what degree of compulsion the objects of the

application have to follow the application-wide default setting

concerning application log.

Allowed Message Types

Controls which message types you can use in an application when

you define a Log Message action.

Versioning Mode

Controls whether newly created objects are put under version

control by default or not.

  Note

This setting affects objects of all types except for catalogs.

Catalogs are always created with versioning off.

Controls whether texts and documentation of newly created

objects shall be maintained dependent on language, version, both,

or none of all. Object names, however, are treated as technical

names and are therefore not affected by these settings.

Language Settings

More Information

Storage Types

Versioning

Creating an Application

Setting Properties

Adding Objects

Setting an Access Level

Setting Versions

This is custom documentation. For more information, please visit SAP Help Portal.

28


10/15/26, 3:15 PM

Storage Types

Use

BRFplus provides a number of different storage types for objects to be stored. The storage category is selected on the basis of how

the application objects are intended to be used. The storage type is defined as a property of a BRFplus application. When creating

an object, the new object inherits its storage type from the application to which it belongs. There is no way for an object to override

this inherited setting.

  Note

You set the storage type of an application when you create an application. This setting is irreversible after the application has

been saved for the first time. It cannot be changed at a later point in time.

Features

System Data

Objects defined as system objects should not be changed. The metadata for system objects is stored in client-independent

tables of delivery class S. This metadata can only be transported via a workbench transport. All system object database

table names end with S. System objects cannot refer to Customizing or master data objects. However, system objects can

be referred to by Customizing and master data objects.

Customizing Data

Customizing objects are objects that allow you to create or make changes in your system environment. The metadata for

customizing objects is always stored in client-dependent tables of delivery class C. Customizing objects can only refer to

system objects.

Master Data

Master data objects are client-dependent objects, local by default and cannot be transported. The metadata for master

data object is stored in client-dependent tables of delivery class A. Master data objects can refer to system and customizing

objects.

The following table summarizes how the storage type of an application affects the usage of objects that belong to it:

Storage Type

Client

Transport

Cross-Application Usage

System

client-independent

transportable or local

Can use system objects.

Customizing

client-dependent

transportable or local

Master Data

client-dependent

local

Can use system and

customizing objects.

Can use system, customizing,

and master data objects.

More Information

Application

Naming Conventions for BRFplus

This is custom documentation. For more information, please visit SAP Help Portal.

29


10/15/26, 3:15 PM
Use

The names of the objects that you create and work with in BRFplus are used in the sense of technical names. As opposed to the

Text and Short Text properties of an object, the Name property is always language-independent. Referring to an object by its name

is therefore a good practice for global companies where employees with different mother languages have to communicate. Here,

the language-independent name can help to overcome misunderstandings.

The following naming conventions apply for BRFplus objects:

The name of an application must be unique within the scope of a system.

  Note

If the system in question is set up as a customer system, it is sufficient for an application name to be unique within the

scope of the system client.

The name of a function must be unique within the scope of an application.

A valid name can contain any character from the following set of characters: "

0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_/"

BRFplus does not differentiate between lower and upper case. All object names are automatically converted to upper case.

Blank characters or hyphens are not allowed in object names. BRFplus automatically replaces blanks and hyphens (" ", "-")

with underscores ("_").

The first character must be a letter or a slash (but not a number). Slashes are allowed only for the purpose of assigning an

object to a namespace. For more information, see section Using Prefix Namespaces below.

BRFplus objects created by customers have to start with one of the reserved letters Y or Z as it is common practice for

customer objects in the ABAP Dictionary.

The name TABLE_LINE is not permitted for all kinds of BRFplus objects as it is a reserved word.

  Note
You can also create unnamed objects in BRFplus. However, this is possible only for objects that depend on another object (for

example, a new data object that you create as an expression's result data object). Unnamed objects cannot be reused.

As an exception to the rules listed above, the name of a node in a catalog can be defined freely. For these non-technical

elements, there is no check against the set of allowed characters mentioned above.

Using Prefix Namespaces

BRFplus supports an informal approach to use object names qualified by namespaces. Informal means that in BRFplus, a

namespace is not a distinct element type of its own. Rather, it is just a prefix preceding the name of the object itself, thereby

assigning that object to the given namespace. Although this is a very simple concept, you can still take advantage of it by using it

for grouping objects semantically, thereby reducing complexity in case of large projects.

If an object name starts with a slash, the system interprets this as the beginning of a namespace designation. This leads to

additional requirements for formal correctness of the object name:

The first character of the name must be a slash (indicating that a namespace is being used).

There must be at least one more slash as part of the name string (indicating the end either of the namespace or of a

particular level in case of a multi-level namespace).

An empty string is not allowed as a namespace ("//").

This is custom documentation. For more information, please visit SAP Help Portal.

30


10/15/26, 3:15 PM

The last slash in the object name must be followed by at least one more character (indicating the name of the object itself,

without the namespace).

  Note
Using prefix namespaces can be restricted depending on your system settings. If you encounter problems when trying to use

prefix namespaces, see SAP note 150451.

  Example

Here are some examples of valid and invalid object names:

Name

MY_OBJECT

ZMY_OBJECT_1

1_MY_OBJECT

/APP/MY_OBJECT

APP/MY/OBJECT

/APP/MY/OBJECT

/APP_MY_OBJECT

Valid

Comment

yes

yes

no

yes

no

yes

no

Object name in customer namespace Z.

Name must not start with a number.

If namespaces are used, the first

character must be a slash.

If namespaces are used, at least two

slashes are required.

/APP/FINANCIALS/COSTING/MY_OBJECT

yes

A valid three-level namespace.

Renaming Objects

You define an object's name during the creation of that object. Due to the technical character of the Name property, it is good

practice to keep this name. Adhering to this principle may save you many problems that may be hard to track. In the BRFplus

workbench, keeping an object's name is supported by displaying the name always in read-only mode.

However, it is still possible to change a name because BRFplus identifies its objects by their ID, not by name. Changing the

technical name of an object is therefore uncritical within the scope of BRFplus. However, it is possible that an object is directly

referenced by name from an ABAP backend program calling the BRFplus framework. It is up to you to ensure that all external

name-based references to BRFplus objects are kept in sync with the changes made inside BRFplus.

If you still decide that an object's name must be changed, the system offers the following ways to accomplish this:

Renaming an individual object

To rename an individual BRFplus object, make sure the administrative data of that object is displayed in the workbench's

General section. On the General tab, click Rename to open a dialog where you can redefine the object name.

Renaming multiple objects

To rename multiple objects, start the Mass Change tool. Select the objects to be renamed and click Rename. In the dialog

that appears, define the prefix or suffix to be added to the existing names.

More Information

This is custom documentation. For more information, please visit SAP Help Portal.

31


10/15/26, 3:15 PM

Administrative Data

Mass Change

Administrative Data

Definition

All of the objects you can create in BRFplus have, in addition to their type-specific properties, a common set of properties that are

independent of the particular object type. These properties are referred to as administrative data.

Use

You use these properties for identifying, searching, or grouping the BRFplus objects that are available in the system. In the BRFplus

workbench, the administrative data can be found in the General section at the top of the maintenance screen for each object. You

can decide whether you want this section be expanded or not by clicking

 at the right border of the section header. Displaying

the section content gives you a quick overview of an object's administrative data, while hiding it gives you additional screen space

for defining an object's settings.

Features

Overview

When you open a BRFplus object for viewing or editing, the system populates the work area of the UI with the respective object

data. Whether the object's administrative data are initially displayed or hidden is subject to the respective setting in the

Personalization settings.

Details

The detailed view of the administrative data is divided into the following tabs:

General

Here, the system displays a group of settings that have either been defined at creation time of an object (for example, the

application to which an object belongs) or are automatically derived from activities in the system (such as the creation or change

date). These settings are therefore presented in read-only mode, with the exception of the object's Access Level, which can be

changed by the user. For more information about access levels, see Setting an Access Level.

Texts

With the text settings, you can control how the descriptive name (not the technical name) of an object is presented in the user

interface. The different options offered by the system depend on the Source that you select for the object texts:

Free text input

With this option, the short and long text have to be entered manually by the user.

Text symbol

With this option, the text defined for a given text symbol (also known as text element) of a given ABAP report in the backend

system is used as the object's text.

Unlike the other options, the Text symbol option supports only one text field and therefore cannot be used to differentiate

between short and long texts.

This is custom documentation. For more information, please visit SAP Help Portal.

32


10/15/26, 3:15 PM

Exit class

With this option, the short and long text provided by the given exit class are used as the object's text.

The following section describes the text options depending on the Source that you select:

Free text input

Dependency

For object texts to be entered manually, you can specify whether these texts remain constant across all versions and

languages, or if the texts shall be distinguished by language, version, or both.

Language dependency

For language-dependent texts, the system displays an additional field where you can select the desired

language. This field offers all the languages that are available in the system. Once you have chosen the

desired language, you can maintain the texts for this language. This option is useful and it can even be legally

required if you plan to use a BRFplus application in countries with different languages.

Version dependency

For objects that are under version control, you can define that the texts shall also be version-dependent. With

this setting, each new version of an object contains a copy of the object texts that are carried over from the

previous version. These texts can then be overwritten in the new version without affecting the texts that were

in place in the previous version. This can be useful if a complex object like a formula expression has been

changed substantially from one version to another, or if an object text must properly reflect the name of an

external entity that has been renamed in the course of time.

Language

From the available languages, choose one and maintain the short and long text for this language. This field is

available only if you have defined the object texts as language-dependent.

Short Text, Text

Enter the texts for the current object. Short texts can hold up to 20 characters, texts up to 80 characters. The short

text that you enter is used by the BRFplus workbench for displaying the object unless you decide that you want to

see technical names only. To control the display behavior, choose

 and then  General

 Display Technical Names

.

  Note
The system has a fallback mechanism in case the text to be used according to the personalization settings is not

available (for example, because the required text has not been maintained for the current logon language, or the object

in question is unnamed). The system then tries to display a text according to the following order of precedence:

1. Short text

2. Long text

3. Dynamic string representation of significant elements of the object definition (for example, the value of a

constant as a string)

Text Symbol

Program Name

Enter the technical name of the ABAP report for which a text symbol is defined that you want to use as the current

object's text.

This is custom documentation. For more information, please visit SAP Help Portal.

33


10/15/26, 3:15 PM

Key

Enter the ID of the text symbol defined for the above report that you want to use. Once you have entered the symbol

ID and press  Enter , the string maintained for the text symbol is displayed as Text.

Language

From the list of languages available in the system, choose one to check which text is displayed if a user is logged on

in that language.

  Note

Be aware that the Language list is only meant to help you find out which different language versions of the

selected text symbol exist. As opposed to this, it cannot be used to maintain additional language versions. This

can only be accomplished by using the appropriate translation tools for the text elements assigned to the

referenced report.

Exit class

With this option, the short and long text provided by the given exit class is used as the object's texts.

  Note

The exit class that you enter here must implement the IF_FDT_TEXT_DOCU_EXIT interface. The workbench uses the

methods provided by this interface to retrieve the texts for the object. The workbench supports you in finding a suitable

class by restricting the classes shown in the value help to those that fulfill this prerequisite.

Note that this class setting is not related to the application exit class.

Documentation

BRFplus offers you the possibility to maintain a documentation for each single object you create, like functions, expressions, data

objects, etc. This is especially useful for complex objects like formulas or decision trees that have an immediate influence on how

the system handles a particular business case but can sometimes be difficult to understand.

The options available for object documentation are very similar to those offered for texts. Therefore, the following part only

describes the documentation-specific features, while those features that text and documentation have in common are left out.

Please refer to the Texts section above.

Free text input

With this option, you can manually enter a documentation text of any length.

SAPscript object

With this option, the text contained in the specified SAPscript document is referenced as the object's documentation.

Exit class

With this option, the documentation provided by the given exit class is used as the object's documentation.

The following section describes the text options depending on the Source that you select:

Free text input

Dependency, Language

Same as described above in Texts section.

SAPscript object

This is custom documentation. For more information, please visit SAP Help Portal.

34


10/15/26, 3:15 PM

ID

Document class ID of the SAPscript document you want to use for the object's documentation. Examples of possible

values are TX for general texts, RE for report documentation, DT for dialog texts, etc.

Object

Technical name of the SAPscript document you want to use for the object's documentation.

Exit class

Exit Class

Enter the name of the exit class you want to use for providing the object's documentation.

  Note

The exit class that you enter here must implement the IF_FDT_TEXT_DOCU_EXIT interface. The workbench

uses the methods provided by this interface to retrieve the documentation for the object. The workbench

supports you in finding a suitable class by restricting the classes shown in the value help to those that fulfill this

prerequisite.

Note that this class setting is not related to the application exit class.

Documentation

In this field, the BRFplus workbench displays the documentation text provided by the exit class you have entered in

the Exit Class field.

If the predefined functionality of dynamically providing object documentation with the help of an exit class is still not

flexible enough for you, you might want to develop individual extensions to this concept. For example, if you have a user

license for SAP Knowledge Warehouse, it would be possible to create additional documentation in the Knowledge

Warehouse and have the interface method implemented by the exit class display the topic related to a particular BRFplus

object. However, such extensions are completely customer-specific and are not supported by SAP.

  Note

For data objects that have been bound to a DDIC object, the Text and Documentation parts of the administrative data

automatically inherit the respective data stored in the DDIC for the bound object. This does also comprise all the different

language versions that may be available in the DDIC. Text and documentation are treated differently by the system in the

following respect:

The inherited texts are imported into the BRFplus repository as default values for a bound data object but can be

overwritten if desired.

The inherited documentation is imported into the BRFplus repository by reference and cannot be changed.

For more information, see Data Binding.

Versions

You can access all versions of a given object that are stored in the system. The version list always contains at least one entry (the

current version). For each version, the system displays the following information:

Property

Version

Description

Version number. In case of complex object types, this column does

also contain a triangle icon that you can use to expand the object

structure in the Object Type column (see below).

This is custom documentation. For more information, please visit SAP Help Portal.

35


10/15/26, 3:15 PM

Property

User Name

Time Stamp

Description

Logon name of the user who saved the object version

Date and time when the object version was saved

Processing-relevant changes

Gives access to the list of changes made in a version that are

relevant for processing and may influence the process flow. Here

are some examples for this kind of change:

Constant value changed

Formula expression modified

Constant expression replaced by decision table

Non Processing-relevant changes

Gives access to the list of changes made in a version that are not

Versioning

Object Type

relevant for processing and have no influence on the process flow.

Here are some examples for this kind of change:

Short text changed

Versioning switched off

Dependency type changed for object documentation

Indicates whether versioning is switched on, and if so, which

versioning mode is in effect. This setting is either On, Transported

by <transport ID>, or Not transported for versions preceding the

current version and may be either on or off for the current version.

Type of the current object. In case of complex objects, this column

displays the expanded object structure. For example, a table data

object version can be expanded to show its structure and elements

that were present in a particular version.

Depending on the definition of a particular object, the object name displayed in the Name column may be preceded by a small

triangular icon. This indicates that the object version contains nested objects that are also versioned. After expanding the list of

nested objects, you can directly access the nested objects' version.

Additional Information

With the additional information presented on this tab, the system helps you to identify the origin of a BRFplus object. Here you can

find out the name of the system where an object has originally been created, the ID of the transport request used to import the

object into the current system, and the client number in the source system from which the object has been exported.

If a non-local object has been changed and therefore been recorded in a transport request waiting for release, the respective

transport request is displayed. In that case, the transport ID displayed serves as a link. When you click it, the system opens the

transport analysis tool with detailed information on that transport request.

The degree to which the fields are populated with values gives you a hint of the current system's nature with respect to the current

object: If your current system is the same as the object's original system, then only the system field contains a value while the

other fields remain empty (because there was no transport needed).

More Information

Versioning

This is custom documentation. For more information, please visit SAP Help Portal.

36


10/15/26, 3:15 PM

Context and Result

Use

Context and result define the input and output parameter interface. In BRFplus, input parameters are referred to as context while

output parameters are referred to as result. Context and result are data carriers.

Features

General

Both context and result are a set of data objects, such as an element, structure, or a table. A context or a result of type element can

be a text, number, Boolean, quantity, amount, and timepoint.

Functions as well as expressions, actions, and rules have a context. A set of attributes defined by the context is used as input values

to be processed by a function or an expression. The context can consist of one or many elements, structures, or tables, each of

which is addressed by its name.

The context data of a function can be used by all subexpressions that belong to the function's top expression or ruleset. The input

parameters of the expressions are filled either with the function's context or with the result of other expressions.

In contrast to this, a function or expression can always have only one result data object. Given that, if a business rule is to return

more than one value at once, this can only be accomplished by assigning a structure or a table as a result data object.

When you create a function with execution mode Event Mode, the system assigns the predefined Actions table as the function's

result data object. However, you can overwrite this default assignment with any data object that may suit better.

Context Overview

For each object that has a context, you can easily inform yourself of the available context data objects. To accomplish this, navigate

to the object in question in the BRFplus workbench and choose Context Overview. The system then displays a list with all data

objects that are available via the object's context. For each context data object, the system displays its origin (function context or

result). Likewise, in the same dialog you can inform yourself of potential other context data objects that are currently not available

for use by the expression.

  Note

If a function is run in event mode instead of functional mode, the context can be changed and can be a part of the result. In this

case, the result parameter is not relevant.

If an expression, action, or rule is assigned to more than one function, the list of available context data objects represents the

intersection of the context data objects of all involved functions. This is necessary to ensure that the expression, action, or rule

can be processed properly, regardless by which function it is called.

  Example
A decision table expression DT is used by three different functions F1, F2, and F3, either directly as the function's top expression

or indirectly as a nested expression. The following table shows the context data objects for each of these functions:

Function

Parameters

F1

F2

NUM1, TXT1, BOOL1

NUM1, TXT1

This is custom documentation. For more information, please visit SAP Help Portal.

37


10/15/26, 3:15 PM

Function

Parameters

F3

NUM1, BOOL1

In this scenario, there is only one context data object that all three functions have in common, namely NUM1. Consequently, an

expression like decision table DT that is used in all three functions can only access this one common context data object. Using

any of the other context data objects would lead to a situation where the expression's context would be partially undefined for

at least one of the three function, which is not permitted.

If, in the scenario described, you would decide to assign DT to a fourth function F4, and if F4 has only one number data object

NUM2 in the context that is not available in any of the three other functions, then the intersection of context data objects that

can be used in DT would be empty.

Implicit Result Type Conversion

The result data object of a BRFplus object must be compatible to the context data object to which the result is passed as input

data. For example, if a decision table cell contains a value range expression, then the range parameters must be populated by direct

values, data objects, or expressions of the same type as the value range parameters. However, there is one exception to this rule:

For a function with a result data object of type text, you can assign any expression as its top expression, regardless of the result

data object type of that expression. If the result data object type of the expression differs from the text data object defined for the

function, BRFplus performs an implicit type conversion of the expression's result value into text. The conversion logic is the same

as the one that is used for the ToString function that is available for formula expressions. For the details of this logic, see the

formula function documentation that is available in the BRFplus workbench.

Creating Objects

Definition

In BRFplus, you create objects of all kinds to model the business rules that shall support your decision making in the use cases of

your everyday business. You can create objects in different ways. Depending on the situation, different implications may apply.

Concept

General

All BRFplus object types provide a set of administrative data that consists of the same attributes. Most of these attributes are

specific for each individual object, but some of them depend on the application object to which an object belongs. These

dependent attributes are:

Strict dependency

The following application attributes are inherited by all objects that you create in the context of an application and cannot

be changed on object level:

Storage type

With the storage type, you control whether an object is treated as a system object, a customizing object, or a master

data object. You define the storage type of an application and all of its objects when you create the application. There

is no way to change this setting afterwards, neither for the application itself nor for the objects that belong to the

application.

Local vs. transportable objects

This is custom documentation. For more information, please visit SAP Help Portal.

38


10/15/26, 3:15 PM

For an application, you must define the package to which the application belongs. The transport behavior of the

application and its objects is determined by the transport settings of the assigned package. Theoretically, you could

change the transport behavior of the BRFplus objects by assigning a different package to an application. However, in

most cases, such a change has far-reaching effects and is therefore not recommended.

Loose dependency

The following application attributes are inherited by all objects that you create in the context of an application, but can be

changed for each object individually:

Application log settings

Versioning behavior

Language and version dependency of object texts and documentation

Save, check, activate

Once you have maintained and saved the mandatory data for a newly created object, you can continue your work. It is not

necessary to maintain all possible settings at once. However, keep in mind that many object types require detailed settings to make

them ready for productive use. The system helps you to detect any missing or incomplete settings with the built-in check routines

for each object type.

  Example

You create a decision table expression with 10 condition columns and hundreds of rows for the different combinations of

condition values. At first sight, the table seems to cover perfectly the business case that you have in mind. However, the check

may remind you that the data objects you have used in the condition columns have been taken deliberately from the repository

rather than from a function context that is needed for proper operation. Therefore, the decision table may be consistent and

complete in itself but still cannot be activated as long as the table is not connected to a function providing all the data objects

used.

You can check an object either explicitly with the Check button or implicitly with the Activate button. The system then runs all the

check routines defined for the object type in question. If the checks detect any errors or inconsistencies, the system displays a

message. Many of these check messages have a long text attached with detailed explanations of the problem and possible

solutions.

Many object types in BRFplus contain references to other objects. If you try to activate an object containing such references, the

system determines whether there are any inactive objects among the hierarchy of used objects. If so, the system offers to

recursively drill down the object hierarchy and activate all inactive objects it may find. This is a prerequisite for the top level object

to be activated successfully.

If any of the subordinate objects cannot be activated, the process stops with an error message. If this happens, we recommend

that you thoroughly read the message explanation text to find out where exactly the problem occurred, since this is not always

obvious.

Usage Consistency Check

In addition to those checks that are defined to detect any inconsistencies in the object definition, there is another check type

available, namely Usage Consistency Check. With this check, you can let the system check whether an object that you are

currently maintaining is used by any other objects, and if there are any problems with respect to these usage relationships, or with

respect to the using objects. Of course, this check only makes sense for objects that are used by other objects and is therefore

normally not relevant upon object creation time.

To perform this check, open the desired object in the work area of the BRFplus workbench and choose  More

 Usage

Consistency Check .

This is custom documentation. For more information, please visit SAP Help Portal.

39


10/15/26, 3:15 PM

  Example

An element data object of type text has been defined with a maximum text length of 20 characters. This data object is used as

the result data object of a decision table expression, where a number of different result strings has already been defined. If you

reduce the maximum text length of the data object to only 10 characters, and if there are result values in the decision table

exceeding this reduced maximum text length, the usage consistency check would make you aware of this potential problem.

  Note

When the usage consistency check traverses the data model, it may also find objects that are using the current object, but

reside in a different system client. For using objects of this kind, the system cannot perform any further checks. However, the

system makes you aware of the fact that there are affected objects in other clients and leaves it up to the user to run the same

check in these clients.

Manual Creation vs. Programmatic Creation

Creating objects manually

The usual way to create BRFplus objects is to create them one after another in the BRFplus workbench. You can accomplish this in

any of the following ways:

Repository view

In the Repository view, right-click any category node or object type node. In the context menu, choose Create. The system

then presents the types of objects that you can create in the context of the node where you opened the menu.

  Note

In the context menu of an application object, the Create menu offers subitems for creating BRFplus objects of all types,

including application.

Catalog view

If you have a catalog defined, you can create new objects from the catalog's context menu. In this case, the newly created

objects are at the same time assigned to the catalog node from where you started.

Favorites or Recently Used view

In these two views, you can create new objects from the context menu of an application object. If there is no application

object listed in these views, you cannot create new objects here.

Creating objects programmatically

You can of course also create objects programmatically through the interfaces (APIs) offered by BRFplus, with the

CL_FDT_FACTORY class as a starting point. This is especially helpful if you have to create a large number of objects, for example, if

you want to test the system performance with many thousands of objects before you actually start a development project of such

a dimension. In that case you have to take care that those objects that are connected by a usage relationship must be activated

from the bottom up. For more information, see the tutorials on the BRFplus pages in SAP Developers Network (SDN).

Single vs. Multiple Objects

As outlined above, the most common way to create single BRFplus objects is using the BRFplus workbench, and the most efficient

way to handle large amounts of objects is via programming. However, there is a third alternative that may serve as a good

compromise between these two approaches.

Experience shows that in a rules project, the highest number of objects is of type element data object. Here, the BRFplus

workbench offers a mass creation tool with a table-like layout where you can enter the basic attribute values for any number of

This is custom documentation. For more information, please visit SAP Help Portal.

40


10/15/26, 3:15 PM

objects in a row. Once you are done, you choose OK and the system creates all the data objects at once. This is much faster than

creating single objects. To start the mass creation tool, open a view in the BRFplus workbench where you can create objects and

choose  Create

 Data Object

 Elements (Mass Creation)

 from the object tree context menu.

  Note

Mass creation is available for element data objects only.

Reusability

In many situations, it is desirable to use the same BRFplus object at different places in an application or even in different

applications. Reusing objects can reduce the complexity and improve the consistency of an application. BRFplus therefore

encourages you to create reusable objects. This is accomplished by setting the Is reusable flag that is available in most object

creation dialogs by default. With this setting, defining a name for the new object is mandatory, which in turn is the prerequisite for

object reuse.

Making an object reusable has no drawbacks whatsoever. Therefore, in the BRFplus workbench, the Is reusable flag is not only set

by default, it is even impossible to unset it in most cases. There are only rare cases where you can decide to create an object that is

not reusable. The prerequisites for this are the following:

Only expressions can be defined as non-reusable.

This is only possible when you create an expression from the context of another object rather than from the object tree in

the Repository view. For example, you can create an unnamed (and therefore non-reusable) expression in the context of a

function by assigning a top expression with the help of the Create command from the Top Expression field's object menu.

Object Nesting and Unnamed Objects

Instead of creating objects from the object tree in the workbench navigation pane, there are some situations where you can directly

embed a new object into another object. This is possible for the following tasks:

Assigning a new expression to a superordinate object (for example, assigning a top expression to a function, a range

expression to the cell of a decision table, and so on)

Assigning a new rule to a ruleset

Creating objects by nesting them into a container object is comfortable because you do not have to leave the context where you

are currently working in. Besides, this is the only way to create objects without having to define an object name. The consequences

of working with unnamed objects are the following:

Unnamed objects can only be used by the container object for which they have been created.

Unnamed objects are neither listed in the repository object tree nor in the object query dialogs nor in the hit list of the

advanced search.

As a consequence, unnamed objects are not reusable.

If the container object is deleted, its nested unnamed objects remain in the system. Since these objects are invisible, you

cannot access and delete them like other objects. To remove unused unnamed objects from the system, choose  Tools

 Application Administration  and execute the Delete unused objects operation.

Implicit Object Creation via Data Binding

You can create data objects of all kinds (element, structure, table) not only by manually defining all their attributes but also by

defining a reference to an existing object in the data dictionary of the backend system. This kind of object creation is called data

binding. When you use this option, the system determines the dependencies of the referenced dictionary object and automatically

This is custom documentation. For more information, please visit SAP Help Portal.

41


10/15/26, 3:15 PM

tries to reflect the dictionary object as good as possible on BRFplus side. Depending on the situation in the dictionary, this feature

can help you save significant amounts of time. The system can do the following for you:

Element data objects

When you bind an elementary data object to a data element in the dictionary, the system determines if the data element

itself is bound to a domain. If so, the system automatically populates the BRFplus data object with all the domain values

defined in the dictionary.

Structures and tables

When you bind a structure or a table data object to a dictionary structure or table, the system automatically creates an

element data object for each field in the structure or table. In addition, the system establishes a binding relationship to the

corresponding dictionary data element. Again, for each element data object, the system imports the domain values that are

defined in the dictionary for that field.

More Information

Administrative Data

Naming Conventions for BRFplus

Data Binding

Deleting Objects

Searching Objects

Use

It is a common experience that the BRFplus object repository can grow rapidly. This can lead to situations where it is difficult to find

a particular object. To make it easier for you to always find the objects that you are looking for, the BRFplus workbench offers a

number of different methods and tools for this purpose:

Catalogs

With catalogs, you can define a subset of objects that belong to a particular business domain, thereby hiding the multitude

of objects that exist in the repository but do not contribute to that business domain. You can also set up different catalogs

for the same domain and fill them with objects related to different tasks, for example, one catalog for end users and another

catalog with objects needed for rule administration. For more information, see Catalog.

Workbench Views

The workbench views My Applications, Search Result, Favorites, and Recently Used help you organize the objects to be

presented according to different strategies. For more information, see Understanding the User Interface.

Object Search

BRFplus comes with a powerful object search supporting you to easily find the objects you are looking for. The following

sections in this topic explain in detail the BRFplus object search.

Features

Starting a Search

This is custom documentation. For more information, please visit SAP Help Portal.

42


10/15/26, 3:15 PM

You can start a search in different ways. Depending on the current working context, the search dialog is displayed in slightly

different forms of appearance that are designed to support you best in getting your current task accomplished:

Search button in navigation panel

This is the most obvious way to start a search. The search dialog is displayed in its standard layout, and you can specify the

search criteria as desired. The search result is displayed in the navigation panel of the BRFplus workbench.

Searching for an object ID

Each BRFplus object that you create is automatically assigned a unique ID that is stored in the object's ID property.

Addressing an object by its ID is the only reliable way because even the technical name of an object can be ambiguous when

it comes to cross-application scenarios. When you know an object's ID, you can use an easy abbreviation to look it up by

choosing  Workbench

 Open Object

 from the workbench menu. The system then displays the search dialog with the

first search criterion set to Object ID is equal to. All you have to do is to insert the ID into the entry field and start the

search. If an object with the given ID exists, it is loaded directly into the work area of the workbench.

Searching for objects to be assigned to an object under maintenance

Setting up a rules model with BRFplus means reuse of existing objects to the highest possible degree. Therefore, it is a very

common situation for rule modelers to search for existing objects they can assign to the object they are currently working

on, for example as a context data object, a result data object, or a nested expression. In all these situations, the BRFplus

workbench presents an object menu near the position of the object to be assigned. When you choose the Select option

from that menu, the system displays the search dialog and automatically inserts sensible values into some of the search

criteria fields, starts the search, and displays the result in a result list underneath the search criteria. You can then either

choose one of the objects offered in the search result or modify the search criteria and repeat the search until the desired

object appears in the result list.

Customizing the Search Criteria

The BRFplus object search is flexible not only with respect to the freely defined search terms that you may enter, but also to the

layout and predefined restrictions of the search itself. You can take advantage of the following options:

Number of search criteria

By default, the search dialog is displayed with three lines for your search criteria. In each line, you can choose the desired

search criterion from a list, the comparison operator, and the value you want to search for. If you use more than one

criterion, the effect on the search process depends on whether you define different criteria, or multiple occurrences of the

same criterion, but with different values: If you define two or more different criteria, these criteria are internally connected

with a logical AND operator. In other words, the more search criteria you define, the more specific are your search results.

Different criteria: If you define two or more different criteria, these criteria are internally connected with a logical

AND operator. In other words, the more search criteria you define, the more specific are your search results.

Same criterion, but different values: If you define two or more lines for the same criterion, but with different values,

these criteria are internally connected with a logical OR operator. In other words, the more search criteria you define,

the more hits can be collected in the search result.

If you need more than three search criteria for a search, you can simply click the "+" button at the end of a criterion line. The

system then provides an additional line, for which by default the same criterion is preselected as in the previous line where

you clicked the button. If you prefer to see less criterion lines, click the "-" button instead. The system takes care, however,

that at least one criterion line remains visible in the search dialog.

Mutual relationship of search criteria

In principle, the search criteria that you use in a search are independent of each other and can be combined as needed. The

only thing to keep in mind is that adding search criteria means refining the search result.

This is custom documentation. For more information, please visit SAP Help Portal.

43


10/15/26, 3:15 PM

Despite of their independence, some of the available search criteria are related. The main purpose of such related criteria is

to help you define a search with fewer parameters. Here is an example of a search using different parameter sets:

  Example
You want to search the database for table data objects whose name starts with "ZTBL_CRM_" in all applications you

have set up for CRM-related use cases. As a first approach, you define the search using generic criteria that all BRFplus

object types have in common:

Application Name is equal to *CRM*

Object Type is equal to Data Object

Name is equal to ZTBL_CRM_*

With this parameter set, a possible problem might occur if the name prefix ZTBL_CRM_ has not only been used for

tables, but also for structures or elements. You can refine the search result by taking advantage of one of the more

specific criteria:

Application Name is equal to *CRM*

Data Object Type is equal to Table

Name is equal to ZTBL_CRM_*

Here, the generic Object Type criterion has been replaced by the Data Object Type criterion. With this criterion, the

system implicitly assumes that the search is dealing with data objects only, while all other object types are not taken into

account. It is not necessary to keep the Object Type is equal to Data Object criterion in the search.

Inclusion of BRFplus default objects

When you define BRFplus expressions or rules, it is an important task to assign different objects to the one you are currently

editing. For example, each expression needs a result data object assigned, and nearly all expressions need context data

objects. The usual way to make such an assignment is to choose Select from the object menu near to the position where

the object to be assigned is displayed. The system displays the search dialog with the proper object type preselected and

the result list of the search with that selection. That is, if an expression needs a result data object of type number, all

number data objects are shown in the result list that are available for the assignment.

If you prefer to use any of the predefined data objects shipped with BRFplus instead of assigning your own objects, you can

accomplish this by choosing Also include objects from default BRFplus application. The system then includes the possible

predefined objects in the search result, in addition to your own objects.

Maximum number of results

If you expect that a particular search might yield much more hits than needed, you may limit the number of objects

displayed in the result list. If the number of search results exceeds the maximum number that is currently in effect, the

system notifies you accordingly.

The number of objects that is displayed initially in the search dialog is subject to customization. You can preset this value in

the workbench personalization settings. The lowest allowed value is 10.

Hide/Display the search criteria

If you have defined many search criteria, you may find that the criteria occupy too much space in the search dialog, while

the result list is pretty short. In that case, you can expand the height of the result list by hiding the search criteria, which

gives all the space available to the list.

Special Selection Criteria

This is custom documentation. For more information, please visit SAP Help Portal.

44


10/15/26, 3:15 PM

Most of the selection criteria offered in the search dialog are self-explanatory. However, the following may deserve an additional

discussion:

Search Criterion

Application Name

Action Type

Expression Type

Data Object Type

Element Type

Example

Description

It is a common mistake that a user searching for a particular

application enters the application name in the Application Name

field and starts the search. However, instead of presenting the

desired application object, the result list is populated with all

objects contained in that application, including the desired

application object itself. This is because the Application Name is

one of the administrative data fields that are common to all

BRFplus objects. It is not restricted to objects of type application.

To search for an application object, define the search as follows:

Object Type is equal to Application

Name is equal to <your application name>

These three criteria help you simplify the search definition. They all

make an implicit assumption with respect to the type of objects to

be searched, namely action, expression, and data object. Therefore,

if you use any of these criteria, it is not necessary to define an

additional Object Type search criterion.

This is a further refinement of the Data Object Type criterion

mentioned above. With this criterion, you can directly express that

you want to search, for example, for text or number data objects. It

is not necessary to explicitly restrict the Object Type to Data

Object, and the Data Object criterion to Element.

In the course of a rules implementation project, you need to find out whether all formula expressions in a specified BRFplus

application have been named according to the naming conventions set forth for that project. You want to concentrate on formula

expressions that have been created before the year 2012. To accomplish this, proceed as follows:

1. In the BRFplus workbench, choose

.

2. In the Personalization dialog, on the General tab, make sure the Show Technical Names option is in effect.

3. In the workbench, make sure that the navigation panel is in Repository mode.

4. Choose Search.

5. In the Search dialog, define the following search criteria:

Application Name is equal to <your application name>

Object type is equal to Expression

Expression Type is equal to Formula

Created on is less than 01.01.2012

The search dialog should now look as shown in the following graphic:

This is custom documentation. For more information, please visit SAP Help Portal.

45


10/15/26, 3:15 PM

Search dialog showing the criteria described above

6. Choose Search to start the search.

The system determines the objects matching the criteria that you have entered and displays the objects in the navigation panel.

Since you have made sure in the first steps that objects shall be displayed using their technical names, the hit list contains the

technical names so that you can see at one glance whether the naming conventions have been observed or not.

More Information

Catalog

Workbench Personalization

Understanding the User Interface

Deleting Objects

Use

Deleting objects from the BRFplus database is a well-defined, multiple-step process that helps you to clean up your work

environment without any risk of unwanted loss of data. This process encompasses different pre-deletion and deletion stages with

an ever-decreasing degree of object availability and visibility. Only after an object has run through most of these stages (if not all)

can it be deleted physically and irretrievably. With this delayed and stepwise approach, BRFplus helps you to keep control over your

objects even after, at first glance, they have been deleted. As long as an object has not been physically deleted, an administrator

can still reactivate it and make it available for auditing or check purposes, or even for productive use.

Features

Technically, the different steps to bring an object to its final, physical deletion are implemented as an internal status assignment

rather than a real deletion. This makes it possible to let an object appear to be in different "degrees of deletion", where each degree

corresponds with a set of restrictions that apply to an object in that particular status. Only for the last step in this process (physical

deletion), the internal processing turns from a status assignment to a real physical deletion of an object from the system database.

This is custom documentation. For more information, please visit SAP Help Portal.

46


10/15/26, 3:15 PM

After that, an object is irretrievably lost. The following sections describe the different steps of an object from productive use to its

physical deletion.

Marking Objects as Obsolete

When you check your business rules, you may notice that from time to time, certain objects do not reflect the business case in

question properly anymore. There may be nothing wrong with these objects at the moment, but you may foresee that future

changes in the business environment might lead to a need for a change of the rule object.

  Example

In a business rules application for calculating income taxes, you have modeled the income/tax relationship with a decision table

where each row represents a certain income range and yields the proper tax that is due for that income. However, the

government in your country has announced that the taxation system shall be changed in principle, with a number of complex

calculation steps needed to determine the legally prescribed tax for a given income.

In such a situation, it is pretty clear that the decision table approach that used to be appropriate in the past will not be suitable

to meet the future requirements. Given that, you mark the decision table as obsolete to remind yourself that there is no use in

trying to make the decision table fit for the new taxation system. Rather, you would have to think of a different approach using

more powerful expression types, such as formula expressions.

Marking an object as obsolete has the following effects:

An obsolete object cannot be changed.

Marking an object as obsolete does not affect its activation status.

Rules and expressions already using an obsolete but active object remain functional and are still available for productive

use.

Inactive rules and expressions already using an obsolete object cannot be activated.

An obsolete object cannot be assigned to another object anew. The system enforces this restriction by hiding obsolete

objects in all kinds of object selection lists.

The obsolescence flag of an object can be removed at any time. Once removed, the object is reverted to its original state in

which it was before it was marked as obsolete.

  Note

Marking an object as obsolete is not a prerequisite for deleting an object. There is no workflow or state transition connection in

the system that would force you to always declare an object as obsolete before you delete it. However, looking at an object as

obsolete is in many cases the first step of a process that ends with deleting the object. In addition, the effects for an object

marked as obsolete are similar to those that apply for objects marked for deletion. This is why the two aspects of marking an

object as obsolete, or marking it for deletion, are covered together in this topic.

Marking Objects for Deletion

You mark an object for deletion to make it clear that this object is outdated or no longer up-to-date and shall no longer be used.

Marking an object for deletion has the same effects as the ones that have been listed above for obsolete objects, plus one

important additional effect:

Objects marked for deletion can be centrally removed from the system either with the application administration tool

(logical deletion, see section below) or with report FDT_DELETE that is executed either on demand or periodically based on

a user-defined schedule. This report can be used for deleting all objects that are marked for deletion since, or for longer

than, a given retention time.

This is custom documentation. For more information, please visit SAP Help Portal.

47


10/15/26, 3:15 PM

As a consequence of this additional effect, it is clear that after an object has been marked for deletion, you should replace it as

soon as possible wherever it is used. This is true even though an object marked for deletion still remains functional in all contexts

where it is already in use.

Deleting Objects (Logical Deletion)

Logically deleting a BRFplus object is most similar to any delete operation you may know from other applications. When you delete

an object, the object disappears from all object lists like the repository tree, the list of recently used or favorite objects. There is no

way for a user to undelete a logically deleted object. For deleting an object, the following rules apply:

You can delete an object only if it is not used by any other object. Keep in mind that in case of versioned objects, usage

relationships may exist between the object that you want to delete and historical versions of another object. In this case,

you must first remove the out-of-date usage before you can delete the referenced object.

It is good practice to delete an object only after it has been marked as obsolete or marked for deletion before. However, this

is not a technical prerequisite. If necessary, you can also delete any object regardless of its current status, provided it is not

used by any other object.

You can logically delete objects in the following ways:

Manually by navigating to the particular object and using the Delete command for that object.

Automatically by using the Delete Objects Marked for Deletion command in the application administration tool.

This command does of course only operate on objects that have been marked for deletion. Also, the objects to be

deleted must have been marked for deletion for the defined retention time or longer (default: 90 days).

Once an object has been logically deleted, it is removed from all kinds of object lists in BRFplus.

BRFplus offers no tools whatsoever to recover an object that has been deleted. However, this can still be accomplished by

system administrators because even deleted objects are not physically removed from the system immediately. For details,

see the following section Deleting Objects (Physical Deletion).

Deleting Objects (Physical Deletion)

Once an object has been logically deleted, it is no longer available in BRFplus. However, this logical deletion does not lead to an

immediate physical destruction of that object. Rather, the deleted object still exists in the system but is hidden such that there is

no way to retrieve it within BRFplus.

There are different ways to physically remove a deleted object from the database:

In the BRFplus workbench, choose  Tools

 Application Administration . From the list of Operations, choose Clean up

Database.

In the backend system, run report FDT_DELETE.

Let the system clean up the database with an automatic cleanup run. This cleanup run is carried out without manual

intervention. It removes objects from the database that have been logically deleted for 180 days or more.

As long as the physical deletion has not taken place, the object is kept in the system and can be restored by a system administrator

in case inevitable reasons should arise that force you to do so (for example, a forensic investigation).

Activities

You can carry out the activities related to object deletion in two different ways, either individually for a single object or as a mass

activity.

Single objects

This is custom documentation. For more information, please visit SAP Help Portal.

48


10/15/26, 3:15 PM

To mark a single object as obsolete, proceed as follows:

1. Open the object to be deleted in the BRFplus workbench.

2. Choose  More

 Mark as obsolete .

To mark a single object for deletion, proceed as follows:

1. Open the object to be deleted in the BRFplus workbench.

2. Choose  Delete

 Mark for Deletion .

To delete a single object, proceed as follows:

1. Open the object to be deleted in the BRFplus workbench.

2. Choose  More

 Display Where Used List

 to make sure that the object is not used by any other objects.

3. Choose  Delete

 Delete .

Multiple objects

To perform any of the activities related to deletion for multiple objects at once, proceed as follows:

1. Choose  Tools

 Mass Change .

2. In the mass change tool, select the objects that you want to change.

3. Choose (Perform actions on marked items: Set as obsolete, mark for deletion, delete), followed by the desired

menu option.

More Information

Mass Change

Data Objects and Types

Use

A data object describes data and serves as a data carrier in the context or the result of an expression or an action. Data objects can

be further described by their type, namely element, structure, or table.

For an elementary data object, you can define the set of comparison operations that is supported by a particular data object. This

is helpful when a data object is used in a comparison against a range expression. If the data object does not support the

comparison type in question, the system can determine this mismatch already at design time and thus prevent you from running

into problems at runtime.

An elementary data object must have one of the following subtypes:

Element Type

Text

Text (Description)

Character string (maximum length 255 characters)

  Note

The maximum length of text data objects refers to the

maximum string length that can be stored in the database. In

contrast to this limitation for persistent strings, you can use

This is custom documentation. For more information, please visit SAP Help Portal.

49


10/15/26, 3:15 PM

Element Type

Text (Description)

much longer strings as long as they are only used for internal

calculations during a BRFplus session. For example, you can

concatenate a number of strings to one very large string in a

BRFplus formula, then search this large string for a particular

string pattern and finally return a formula result (for example,

the number of occurrences of the pattern in the large string).

Number

Number with decimals

Boolean

Amount

If a data object is bound to a DDIC data element of type NUMC, the

BRFplus data object is automatically set to type text, not number.

For more information, see the Type Derivation section in Data

Binding.

Boolean value

Number and currency

  Note

The number of decimal places of an Amount element is always

set to 10 and cannot be changed by the user. This is because

this setting is only for formal reasons. At runtime, the actual

number of decimals to be used is derived from the central

currency tables in the backend, that is, the number of decimals

is currency-dependent. Consequently, you can completely hide

the formal setting in the BRFplus workbench with the help of the

Personalization by choosing  General

 Display

 Show

Technical Attributes .

Quantity

Number and unit of measure

In addition to the mandatory definition of the unit of measure at

runtime, you can optionally specify the quantity dimension at

design time (for example, length, mass, time). This additional

specification has the following effects:

At runtime, the system checks if the unit of measure

provided is valid for the specified dimension.

If data objects with a specified quantity dimension are used

in calculations of a formula expression, the system

performs additional formula consistency checks to detect

semantic errors that could lead to an error at runtime.

  Note

Even if there is a predefined number of decimals to be displayed

for a particular unit of measure in the central dimension tables,

the number of decimals defined by the user for the data object

takes precedence over the system default. This is to ensure the

transparency of decisions based on quantities. Otherwise,

situations could occur where two values that are only slightly

different are displayed with the same decimals after being

rounded. In such a situation, a user could be confused why the

system uses one value and not another one during rule

evaluation. To prevent such ambiguities, and based on the fact

that BRFplus is a generic tool that is not tailored to the needs of

This is custom documentation. For more information, please visit SAP Help Portal.

50


10/15/26, 3:15 PM

Element Type

Timepoint

Text (Description)

a specific business scenario, BRFplus always displays quantities

with the user-defined number of decimals.

Local date

Local time

Local date and time

Universal time (UTC) timestamp

Local date and time with offset to universal time (UTC)

  Note

The first three subtypes listed above are abstract values, i.e.,

there is no explicit time zone information stored along with

values of that type. If you need precise and unambiguous date

and time information in your application, you have to use the

two UTC-based timepoint subtypes.

For a timepoint data object, it is not required to set the object's

subtype at design time. You can leave this part of the object

definition open so that the object can hold any valid kind of date

and time data. This is useful in scenarios where the particular

subtype of an incoming date and time value is not known.

However, if you decide to leave the type setting undefined, you

have to pay extra attention to objects using the timepoint

element because the type-specific consistency checks cannot

be applied to a timepoint element without a specified subtype.

Rather than explicitly defining the type of an elementary data object, you can also let an object inherit its type and properties from

another object. The other object may either reside in the BRFplus repository or in another repository in the backend system. For

more information, see Data Binding.

Structure

The structural relationships between the different types of data objects are shown in the following table:

Data Object Type

Consists of

Element

Structure

Table

Predefined data types (see table above)

Element (0..n)

Structure (0..n)

Table (0..n)

Element (0..1)

Structure (0..1)

According to the relationships shown in the table above, it is useful to know how the different data object types are built upon each

other:

This is custom documentation. For more information, please visit SAP Help Portal.

51


10/15/26, 3:15 PM

An element represents a predefined, elementary data type that can neither be reduced to smaller parts nor extended in any

way.

A structure is a combination of an arbitrary number of elements, of structures, or a combination of both. Especially the fact

that a structure can consist of other structures (which again may consist of structures) enables you to model data

structures of almost any desired degree of hierarchical complexity.

  Note

Although from an architectural point of view there is no theoretical limit to structure complexity, the following limitation

must be observed for practical use: In case of deeply nested, multi-level structures, addressing a particular field via its

name may result in a long sequence of concatenated strings needed to represent the fully qualified name of that field. If

such a name consists of more than 255 characters, it can no longer be handled by the tool infrastructure of the ABAP

backend system. If this limit is exceeded, code generation is no longer possible for such an object.

The fields in a table are defined by either assigning exactly one element or one structure to the table. In other words, the

field structure of a table is not implicitly built up by adding one field after another to the table. Rather, the table can only

adopt the fields of a structure data object that has been created before. If you choose, however, to assign an element rather

than a structure data object to a table, this results in a one-column table (that is, a simple list).

More Information

Creating Data Objects

Data Binding

Comparison Operations

Data Binding

Use

Data objects can be bound to elements in the ABAP Data Dictionary (DDIC) or to the global data types (GDT) in Enterprise Service

Repository (ESR). In addition, you can also bind an elementary data object to an already existing BRFplus data object. This enables

you to implicitly define a data object's settings, as opposed to explicitly assigning a data type to a data object, manually creating a

value list for it and so on.

In simple use cases where you just need a field that, for example, can hold a string for an intermediate result during rule

processing, it is normally the easiest way to define the data object manually. However, when you have to handle complex data

structures that are already defined in a different repository, then binding a BRFplus data object to such an already existing element

is an effective way to accomplish this in a consistent and fast manner.

The advantages of using data binding are not restricted to complex structures. There are also use cases where binding a data

object to a simple DDIC data element can save you a lot of work. For example, if you need to access a list of ISO country codes, you

would just look up a data element in the DDIC that is used for the same purpose and has the country codes already assigned as a

list of domain values. After binding the BRFplus data object to that data element, you are done: The data object has the same data

type and field length as the bound data element, and all the domain values are made available to the data object.

Data binding can also help you keep your system consistent in cases where you have one or more fields that are reused at many

places throughout your application. The following example shows what binding can do for you in such a scenario:

  Example

This is custom documentation. For more information, please visit SAP Help Portal.

52


10/15/26, 3:15 PM

The name of customer company Akron Heating Inc. shall be used in your BRFplus application at a number of different

places. If you have to change the name from Akron Heating Inc. to Akron Heating Ltd., this change has to be done

at all these places for reasons of consistency. By binding the data object, you can avoid such repetitive and error-prone tasks.

1. Create an element data object Company_Name of type text with a length of 30 characters.

2. On the Domain Values tab, choose Create Value.

The system displays a dialog for defining a constant expression for the name string.

3. Define a name for the constant and enter the company name Akron Heating Inc. into the Value field.

4. Click the Create button.

The system navigates back to the Company_Name data object and displays the newly defined company name in the

Value List on the data object's Domain Values tab.

5. Create another element data object named Customer_Name.

6. From the Binding Type list, choose Bind to existing BRFplus element.

The system presents the Object Query dialog.

7. In the Object Query dialog, look up and select the previously defined Company_Name.

The system navigates back to the Customer_Name data object that is now bound to the Company_Name data object.

8. Click Create and Navigate to Object.

The system navigates to the newly created Customer_Name data object. On the data object's Domain Values tab, you

can see the company name Akron Heating Inc. that is inherited from the definition of the bound data object.

You can now start populating your application with the Customer_Name data object wherever this entity is needed. Once you

are done, change the associated text constant's value from Akron Heating Inc. to Akron Heating Ltd.. The new

name is visible at all places where you have used the Customer_Name data object.

Prerequisites

The object you want to bind to a BRFplus data object must be active. This does not only apply to the bound Data Dictionary objects

but also to BW master data (see section BRFplus data objects and SAP BW information objects below).

Features

Supported Binding Types

Depending on the type of the BRFplus data object that you want to bind to another element, you have different possibilities. This is

explained in the following table:

Data Object Type

Supported Binding Types

Comment

Element

DDIC object

GDT

BRFplus element

Table

DDIC table type

Table type structure with all contained fields

is imported automatically into BRFplus

This is custom documentation. For more information, please visit SAP Help Portal.

53


10/15/26, 3:15 PM

Data Object Type

Supported Binding Types

Comment

Structure

  Note

DDIC structure

GDT structure

DDIC structure with all contained fields is

imported automatically into BRFplus

Client/MANDT is filtered out in data objects that are bound to DDIC structures and tables. Raw / binary fields are also

filtered out, when not UUIDs.

As an alternative to binding a BRFplus table data object to a DDIC table type, you can also associate a BRFplus table with

a database table in the backend system. To accomplish this, leave the Binding Type setting as No Binding and choose

Create Structure from DB Table instead. The system then reads the table line type of the given database table, creates a

new BRFplus structure including the structure elements, binds the new BRFplus structure to the database table

structure and assigns the BRFplus structure to the current BRFplus table data object.

Binding BRFplus objects to GDTs is currently only supported for a limited scope of SAP-internal development projects.

This feature is not supported for external applications.

Type Derivation

When you bind an elementary data object to a dictionary type, the system determines the dictionary type and adjusts the subtype

of the BRFplus data object such that it matches best the bound dictionary type. While this sounds trivial for basic dictionary types

likeCHAR orINT1, there are also some more sophisticated cases. For example, the BRFplus elementary type Boolean has no direct

corresponding elementary type in the data dictionary. Here, data elements used for Boolean purposes are set up by referencing a

one-character domain of type CHAR with two, sometimes three, fixed values. For a derivation of a BRFplus data object of type

Boolean, the bound dictionary element must fulfill the following conditions:

Elementary type:CHAR1

Domain: Exactly two values defined: 'X' (True) and ' ' (False).

These two conditions are fulfilled by the standard domain BOOLE.

As an alternative, BRFplus does also accept the standard data element SYBATCH as a valid binding reference for a Boolean

data object.

Another example of a type derivation that may be surprising at first sight is the handling of the widely used built-in typeNUMC.

Although this type accepts only digits from 0 to 9, it is still technically designed as a string of number literals. Therefore, aNUMC

field in the dictionary is always converted to an elementary data object of type text (not number) during data binding. this would

normally lead to the consequence that within BRFplus, such fields cannot be used for mathematical operations like SUM or

AVERAGE in a formula or table operation expression. However, you can still control whether such a data object shall be treated as

numeric or alphanumeric. You can accomplish this on application level with the Numeric Comparison for NUMC Fields setting

located on the Default Settings tab.

Domain Value Lists

Most of the business-specific data elements in the dictionary have a domain object assigned. The domain is then used to define

the data type of the referencing data element and a number of technical settings. In addition, a domain can provide a predefined

list of values for the referencing data elements. Value lists can be defined in different ways:

Single Values: A list of single fixed values (for example, 1, 2, 3, 10, 20, 30, ...).

Intervals: A list of value ranges (for example, 'a'..'f', 'h'..'m', 'x'..'z', ...).

This is custom documentation. For more information, please visit SAP Help Portal.

54


10/15/26, 3:15 PM

Value Table: A reference to a dictionary table where each table entry serves as a value for the referencing domain.

In addition to the domain values itself, the system lets the developer maintain a descriptive text for each value. An application can

take advantage of this by using unique technical values stored in the value field while presenting the business-oriented descriptive

text to the user.

When you bind a BRFplus data object to a data element in the dictionary, the system imports the domain values and presents them

on the Domain Values tab in the BRFplus workbench. In addition, the system tries to import the descriptive texts associated with

the values. Here, the system behavior differs with respect to the different ways of defining the texts:

Single Values:

The system imports the descriptive texts as defined in the domain definition.

Intervals:

For intervals, the system does not import any descriptive texts. This is because in this case, descriptions can only be

associated with each defined interval as a whole, but not with the individual values within each interval.

Value Table:

The system analyzes the associated table in order to determine a field that is likely to be meant as the description field for

the values. Among others, the following criteria are tested by the system to find out if a particular field is a candidate for

descriptions:

Field type is Text.

Field length is 15 characters or more.

Field name contains 'DESC', 'DSCR', 'NAME', 'TEXT', or 'TXT' as a substring.

The first field that matches all of the above criteria is considered to be a value description field, and the system imports the

field contents as value descriptions for the BRFplus data object. If none of the table fields matches the criteria, no value

descriptions are associated with the data object's domain values.

  Note
In the BRFplus workbench, only the first 500 domain values are displayed. This is to avoid performance problems in case of very

large value lists. At runtime, however, you can of course access all the domain values that have been defined in the dictionary for

the referenced data element.

Inheritance

Data objects inherit their attributes such as data type, allowed comparisons, or field length from the bound type. Value help for

data objects is implemented by binding a data object to the data dictionary (DDIC) or a BRFplus data object with a defined list of

domain values. Binding an elementary data object to the DDIC or to ESR enables you to reuse a list of values that has been defined

in the distant repository.

Of course, a data object can only inherit attributes that are available in the bound data object. For example, a data object inherits

the type of a bound DDIC object whereas the setting for allowed comparisons of the data object is not inherited and can still be

defined for the inheriting data object directly. This is evident because a DDIC object does not support the concept of allowed or

restricted comparison operations.

If you bind a data object to another BRFplus data object, be sure that the other data object has explicitly defined attributes rather

than being bound to a third data object itself. This kind of cascading inheritance over more than one level is not supported and

leads to an error message.

This is custom documentation. For more information, please visit SAP Help Portal.

55


10/15/26, 3:15 PM

In contrast to this, however, it is possible to bind one BRFplus data object to another data object that is bound to a DDIC object. In

this case, the attributes of the DDIC object are inherited by the involved BRFplus data objects on both levels.

BRFplus data objects and SAP BW information objects

A topic related to data binding is the association of BRFplus element data objects with data elements in the Data Dictionary that

are referenced by information objects (especially characteristics) modeled in SAP Business Information Warehouse (SAP BW). In

nearly all cases, these objects are accompanied by comprehensive master data tables as well as text tables. At the same time, the

data element associated with a BW characteristic has normally no domain values maintained (because the already existing tables

serve the same purpose). Therefore, when you establish a binding relationship between a BRFplus element data object and a data

element, the system applies the following processing steps:

1. Check if the data element is referenced by a BW characteristic. If yes, determine the related master data table and text

table (otherwise, establish a standard data binding as described in this chapter above).

2. Use the related tables as a source for domain values and texts for the BRFplus data object.

With that, from your BRFplus application, you can take advantage of the data modeling that has already been done in SAP BW.

Constraints

Binding data objects to GDT structures is only supported for systems that have been defined as AP (Application Platform) systems

using the Switch Framework. This kind of system is used for running SAP Business ByDesign. For more information, see the Switch

Framework documentation in the SAP NetWeaver Library on SAP Help Portal.

More Information

Creating Data Objects

Comparison Operations

Definition

Comparison operations are used to define how the system shall perform a comparison between an incoming value that has been

passed to an expression as context parameter and a predefined value or value range. The test parameter may also be supplied as

the result of a nested expression, rather than by a context parameter.

Use

You can use comparison operations mainly to discriminate between different processing paths in a business rule. For example, in a

decision table, the predefined values in the condition columns serve as the comparison parameters against which an incoming

value is compared.

Structure

All types of comparison operations supported by BRFplus are used to compare one incoming elementary data object (the test

parameter) to a predefined value or value range (the comparison parameter). The formal description of a comparison operation is

therefore:

<test parameter> <comparison operator> <comparison parameter>

This is custom documentation. For more information, please visit SAP Help Portal.

56


10/15/26, 3:15 PM

  Example

You want to determine whether an incoming value lies within a predefined value range.

Test parameter: tp = 24

Comparison operator: is between

Comparison parameter: cp = [18..25]

Comparison: tp is between cp (that is, "24 is between [18..25]")

Result: true

The formal description given above is also valid for operators that, from a user's perspective, have no comparison parameter ( is

initial and is not initial). The operators belonging to this group (group 3 in the following table) compare the test parameter against

an implicit comparison parameter that the system derives internally. Therefore, it is not needed (and not possible) to manually

provide a comparison parameter for these types of operations.

Groups of Operators

Whether a particular operator can be used or not depends on the type of the parameters involved. In order to reduce the

complexity of possible combinations of operators and parameter types, the comparison operators provided by BRFplus can be

grouped by their allowed usages. For each of the groups explained below it is possible to say which parameter types can be

combined with the operators of that group.

  Note

In this section, all comparison operators supported by BRFplus are described. However, it depends on the definition of an

elementary data object whether all of the comparison operators can be used or not. This behavior is controlled by the Allowed

Comparisons setting on the Element Properties tab of the data object. For more information, see Creating an Element Data

Object.

Group

Description

Operators

Constant

1

Ordinal comparisons

is equal to

GC_OPTION_EQUAL

is not equal to

GC_OPTION_NOT_EQUAL

is less than

GC_OPTION_LESS

is less than or equal

GC_OPTION_LESS_EQUAL

to

is greater than

is greater than or

equal to

is between

is not between

GC_OPTION_GREATER

GC_OPTION_GREATER_EQUAL

GC_OPTION_BETWEEN

GC_OPTION_NOT_BETWEEN

2

String comparisons

contains any

GC_OPTION_CONTAINS_ANY

does not contain any

GC_OPTION_CONTAINS_NOT_ANY

contains only

GC_OPTION_CONTAINS_ONLY

does not contain only

GC_OPTION_CONTAINS_NOT_ONLY

ID

EQ

NE

LT

LE

GT

GE

BT

NB

CA

NA

CO

CN

This is custom documentation. For more information, please visit SAP Help Portal.

57


10/15/26, 3:15 PM

Group

Description

Operators

Constant

contains string

GC_OPTION_CONTAINS_STRING

does not contain

GC_OPTION_CONTAINS_NO_STRING

string

matches pattern

does not match

pattern

starts with

GC_OPTION_CONTAINS_PATTERN

GC_OPTION_NOT_CONTAINS_PATTERN

NP

GC_OPTION_STARTS_WITH

GC_OPTION_NOT_STARTS_WITH

does not start with

GC_OPTION_ENDS_WITH

ends with

dos not end with

GC_OPTION_NOT_ENDS_WITH

Implicit comparisons

is initial

GC_OPTION_INITIAL

is not initial

GC_OPTION_NOT_INITIAL

is valid

GC_OPTION_VALID

is not valid

GC_OPTION_IS_NOT_VALID

Special comparisons

currency equals

GC_OPTION_CURRENCY_EQUALS

currency differs

GC_OPTION_CURRENCY_DIFFERS

unit equals

GC_OPTION_UNIT_EQUALS

unit differs

GC_OPTION_UNIT_DIFFERS

3

4

  Note

ID

CS

NS

CP

SW

US

EW

DE

I1

I2

IV

NV

CE

CD

UE

UD

The implicit comparison operations "is valid" and "is not valid" (group 3) are defined for the following data types only:

Amount

Quantity

Timepoint

For amount and quantity, the system checks whether the supplied currency or unit of measure is defined in the central

customizing tables of the backend system. For timepoint data objects, the system checks whether the supplied date and time

values can be translated into a valid date (for example, no "April 31st").

The operators "is supplied" and "is not supplied" (technical IDs S1, S2) are no longer supported. Legacy objects referring to

these operators must be adapted.

The operators are all represented internally by constants that are defined for the affected interfaces (for example, IF_FDT_RANGE

).

The operator IDs given in the last column of the above table are the technical names used internally. Mostly, they are referring to

the corresponding comparison operators as defined in ABAP. Actually, BRFplus passes the execution of comparison operations to

the equivalent ABAP expressions. Therefore, the detailed processing behavior of the BRFplus comparison parameters is identical to

the respective ABAP expressions.

Data Type Combinations For Comparisons

This is custom documentation. For more information, please visit SAP Help Portal.

58


10/15/26, 3:15 PM

The way how the system actually performs a comparison depends on the operator and the test parameter type. The following table

presents an overview of the different comparison approaches, grouped by the involved data types:

Data Type

Text

Number

Amount, Quantity

Timepoint

Comments

Alphanumeric comparison of values. In order to reduce complexity,

text parameters are internally converted into a sortable byte

sequence according to the ABAP command CONVERT TEXT. This

normalization helps to avoid problems that can occur if characters

belonging to different codepages are compared. At the same time,

this approach may lead to results that differ from what you would

expect.

Numeric comparison of values

If the parameters have different currencies or units, the parameters

are first internally converted into one of the involved currencies or

units. Then, the system performs a numeric comparison of the

values.

Date and time values are compared numerically. If the values to be

compared have different subtypes, then only the matching parts of

both values are taken into account for the comparison. For

example, if you want to compare a timestamp with date and time

given against a mere date (without time), the system ignores the

time part of the timestamp and concentrates on the date only.

Boolean

Equality check

As a general rule, it is correct to say that a comparison can only be performed by the system if both involved parameters are of the

same type. However, as an exception to this general rule, the system supports some additional comparison operations under the

following conditions:

Ordinal comparisons (group 1) can be performed if both involved parameters can be converted into a valid number. In this

case, the system performs a numeric comparison. Otherwise, both parameters are treated as text and a string comparison

is performed.

String comparisons (group 2) can be performed with parameters of different types. To accomplish this, the system carries

out an implicit type conversion so that both parameters are treated as text.

The following tables present the various combinations grouped by the question whether the comparison is possible at all (with or

without a previous internal type conversion) or not. The tables are of course only dealing with operator groups 1 and 2, because in

group 3, a type conflict is by definition impossible.

The following table shows all sorts of comparison operations that the system can perform without having to make any implicit type

conversions:

Test Parameter Type

Comparison Parameter Type Comparison Operator

Comparison Type

Number

Number

Text

Text

Amount

Quantity

Text

Text

Amount

Quantity

Group 1

Group 1

Group 2

Group 1

Group 1

Numeric

Text

Text

Amount

Quantity

This is custom documentation. For more information, please visit SAP Help Portal.

59


10/15/26, 3:15 PM

Test Parameter Type

Comparison Parameter Type Comparison Operator

Comparison Type

Timepoint

Boolean

Timepoint

Boolean

Group 1

Timepoint

Equal to, Not equal to

Boolean

The following table shows all sorts of comparison operations that the system can perform, but only after an implicit type

conversion of at least one of the involved parameters:

Test Parameter Type

Comparison Parameter

Comparison Operator

Comparison Type

Comments

Number

Type

Number

Group 2

Text

Numbers are converted

to text internally

Number

Text

Group 1

Numeric or Text

1. The comparison

Number

Text

Group 2

Text

parameter of type text is

converted to number and

a numeric comparison is

performed.

2. If this is not possible,

then the test parameter

is converted to text and a

text comparison is

performed.

Test parameter is

converted to text.

Text

Number

Group 1

Numeric or Text

1. The test parameter of

Text

Number

Group 2

Amount

Number

Group 2

Text

Text

Amount

Text

Group 2, Group 4

Text

Quantity

Number

Group 2

Text

Quantity

Text

Group 2, Group 4

Text

Timepoint

Number

Group 2

Text

type text is converted to

number and a numeric

comparison is

performed.

2. If this is not possible,

then the comparison

parameter is converted

to text and a text

comparison is

performed.

Comparison parameter

is converted to text

Both parameters are

converted to text

Test parameter is

converted to text

Both parameters are

converted to text

Test parameter is

converted to text

Both parameters are

converted to text

This is custom documentation. For more information, please visit SAP Help Portal.

60


10/15/26, 3:15 PM

Test Parameter Type

Comparison Parameter

Comparison Operator

Comparison Type

Comments

Timepoint

Type

Text

Group 2

Text

Test parameter is

converted to text

The following table shows all sorts of comparison operations that the system cannot perform:

Test Parameter Type

Comparison Parameter Type

Comparison Operator

Number

Number

Number

Number

Text

Text

Text

Text

Amount

Amount

Amount

Amount

Amount

Amount

Quantity

Quantity

Quantity

Quantity

Quantity

Quantity

Timepoint

Timepoint

Timepoint

Timepoint

Timepoint

Timepoint

Amount

Quantity

Timepoint

Boolean

Amount

Quantity

Timepoint

Boolean

Amount

Number

Text

Quantity

Timepoint

Boolean

Quantity

Number

Text

Amount

Timepoint

Boolean

Timepoint

Number

Text

Amount

Quantity

Boolean

Group 1, Group 2

Group 1, Group 2

Group 1, Group 2

Group 1, Group 2

Group 1, Group 2

Group 1, Group 2

Group 1, Group 2

Group 1, Group 2

Group 2

Group 1

Group 1

Group 1, Group 2

Group 1, Group 2

Group 1, Group 2

Group 2

Group 1

Group 1

Group 1, Group 2

Group 1, Group 2

Group 1, Group 2

Group 2

Group 1

Group 1

Group 1, Group 2

Group 1, Group 2

Group 1, Group 2

This is custom documentation. For more information, please visit SAP Help Portal.

61


10/15/26, 3:15 PM

Test Parameter Type

Comparison Parameter Type

Comparison Operator

Boolean

Boolean

Boolean

Boolean

Boolean

Boolean

Number

Text

Amount

Quantity

Timepoint

Boolean

Group 1, Group 2

Group 1, Group 2

Group 1, Group 2

Group 1, Group 2

Group 1, Group 2

Group 1 (however, is equal to and is not

equal to are allowed), Group 2

Additional Information on Selected Comparison Operators

The following table provides some more detailed information on how exactly the comparison operators work. The table mentions

only those operators whose behavior is not self-evident.

In addition to the detailed information given in the table below, the following general rules apply:

For string comparisons, case-sensitivity is controlled via the respective setting of the value range expression that is used as

comparison parameter.

As opposed to the previous rule, pattern matching comparisons are performed case-insensitive.

For string comparisons, leading and trailing whitespace is removed from the test parameter before the comparison is

executed. Whitespace inside of a string, however, is retained.

For ordinal comparisons of strings (for example, is less than), case-sensitivity is not taken into account. For example,

'a' is less than 'B' is evaluated as true although 'a' has a higher ASCII code value than 'B'.

As opposed to the previous rule, equality checks ( is equal to) of text parameters are performed like string comparisons,

that is, the system respects the case-sensitivity setting during evaluation.

Comparison Operator

Comment

is between

Returns true if the test parameter value lies between the low and

contains any

contains only

contains string

is equal to

high value of a range, including these values (that is,

value >= low AND value <= high).

Returns true if the test parameter contains at least one character

that is also contained in the comparison parameter. The character

sequence, however, can be different, as well as the number of

occurrences of matching characters.

Returns true if the test parameter contains only characters that
are also contained in the comparison parameter. The character

sequence, however, can be different, as well as the number of

occurrences of matching characters.

Returns true if the string contained in the comparison parameter

is also contained in the test parameter. The character sequence

must be identical in both parameters.

Returns true if the test parameter value is identical to the

comparison parameter value.

This is custom documentation. For more information, please visit SAP Help Portal.

62


Comment

Returns true if the supplied test parameter matches the pattern

used in the comparison parameter. The following wildcard

characters are supported:

+ - matches exactly one character

* - matches any number of characters

  Example

Wildcard = '*':

Test parameter: tp = 'Hello'

Comparison parameter: cp = 'He*o'

Comparison: tp matches pattern cp

Result: true

Wildcard = '+':

Test parameter: tp = 'Hero'

Comparison parameter: cp = 'He+o'

Comparison: tp matches pattern cp

Result: true

10/15/26, 3:15 PM

Comparison Operator

matches pattern

starts with

ends with

More Information

Value Range Expression

Expressions

Use

Expression types define the computational power of BRFplus. Each expression type defines a self-contained computational unit

with a well-defined logic. Expressions use a context or nest other expressions to calculate, determine, or derive a result. An

expression can be considered to be an instance of an expression type behaving according to the expression type's logic. An

expression can be reused as a nested building block for a rule, starting with a function as its assigned top expression.

BRFplus comes with a set of common expression types and is regularly enhanced by new expression types. You can create your

own expression types and use it in rules.

The predefined types of expression are:

Boolean Expression

BRMS Connector Expression

Case Expression

Constant Expression

DB Lookup Expression

This is custom documentation. For more information, please visit SAP Help Portal.

63


10/15/26, 3:15 PM

Decision Table Expression

Decision Tree Expression

Dynamic Expression

Formula Expression

Function Call Expression

Loop Expression

Procedure Call Expression

Random Number Expression

Search Tree Expression

Table Operation Expression

Value Range Expression

  Note

The following expression types that were part of earlier BRFplus releases are now deprecated. They are no longer supported by

SAP:

Step Sequence

XSL Transformation

For further details, see SAP Notes 1845412

 or 1904368

.

Boolean Expression

Use

The Boolean expression is used to test a logical condition according to the rules of boolean logic. For your convenience, BRFplus

offers a number of predefined expression templates with two or three operands that cover many use cases. When defining a

boolean expression, you replace the formal operands ( <1>, <2> etc.) by BRFplus objects that can be evaluated to a boolean value

(context data objects of type boolean or expressions with a boolean result data object).

Predefined Templates

The predefined templates for frequently used logical conditions are:

Any operand is true

All operands are true

<1> and <2>

<1> or <2> or <3>

(<1> and <2>) or <3>

(<1> or <2>) and <3>

<1> and <2> and <3>

This is custom documentation. For more information, please visit SAP Help Portal.

64


10/15/26, 3:15 PM

The formal structure of the predefined templates is fixed. The only modification you can make is to invert each of the operators

(that is, add a logical Not to the operator, or remove it if already added).

User-defined Logic Schema

If you have to solve more complex scenarios that are not covered by the predefined templates listed above, you can define your

own logical condition by choosing the User-defined menu option. Here, you are free to define as many operands as you may need.

Supported operators are And, Or, and Not. You can control the logical precedence by enclosing parts of the expression in brackets.

Once you have defined and checked the structure of a user-defined boolean expression, you apply the formal structure to the

expression and assign objects or expressions to the operands. Should you feel the need to modify the user-defined structure of

your expression at a later point in time, you can easily accomplish this by simply adding more operands or selectively remove some

of them. Changing the structure of a boolean expression is supported only for user-defined expressions.

  Note

The definition of a user-defined logic schema might lead you to the idea that a schema that you have defined for a user-defined

boolean expression could be reused to instantiate more boolean expressions with the same schema. However, this is not

possible. If you need to instantiate multiple boolean expressions with the same structure, you can accomplish this by copying

the entire boolean expression and assigning a new name to it.

More Information

Creating a Boolean Expression

BRMS Connector Expression

Use

The BRMS (Business Rule Management System) connector enables you to use SAP BRM or any other external rule engine with

BRFplus.

Depending on the connection type (SAP NetWeaver BRM or External) the expression uses the appropriate function module to

invoke the external rule engine. The expression allows you to specify the signature for the call based on the available vocabulary.

Once the signature is defined, you can export metadata associated with the call as an XML schema.

The XML schema includes information about the input data objects, texts, and documentation associated with the data objects

and return parameters that the rule engine should populate.

When defining the expression, you can also specify any parameters specific to the rules engine being used. For a call to SAP

NetWeaver BRM the two parameters, project and rule set, should be populated. While the call is being executed, BRFplus creates

an XML document corresponding to the above XML schema and passes it to the other rules engine.

More Information

Creating a BRMS Connector Expression

Case Expression

Use

This is custom documentation. For more information, please visit SAP Help Portal.

65


10/15/26, 3:15 PM

The Case expression is used for modeling use cases where you want to compare an incoming value against a predefined list of

discrete values that you already know in advance. Examples of such a closed list of known values could be values indicating

different country or region codes, means of transportation, tax codes, and so on. If an input value occurs that has not been

foreseen, you can deal with that with an optional Otherwise branch, covering all the values that are not explicitly treated by the

expression.

Structure

The BRFplus Case expression is similar to the ABAP CASE statement. The expression takes an input parameter from the context

(the case parameter) and checks its value against a number of test parameters.

For each of these test parameters, a corresponding return parameter is specified in the When table. As soon as one of the test

parameters matches the case parameter, the corresponding return parameter is evaluated and a result is returned. If none of the

specific test parameters matches the case parameter then a generic parameter is evaluated in order to specify the result.

All parameters can be context data objects or nested expressions. Typically, the case parameter is a context data object, the test

parameters are constants and the result parameters are nested expressions.

Features

Result Type

You can decide whether a case expression shall return a value or perform an action:

Return Value: In this mode, you have to take care that all comparison values have a return value or expression assigned with

the same type as the result data object of the case expression.

  Note
When defining a case expression in the BRFplus workbench, first assign a result data object to the expression before you

start to define the results for the comparison values. Only under this condition the system gives you access to suitable

expressions, default objects (like the current user or the logon language), or lets you enter result values directly. With no

result data object defined, you can only assign element data objects to a comparison value as a result.

Perform Action: In this mode, the case expression triggers the action assigned to the return value that matches the input.

The result data object is automatically set to the predefined Actions table that returns the list of IDs of the actions (result

action plus follow-up actions that may be associated with that action) that are executed.

Once the result type settings have been made and the expression has been saved, the system displays these settings in the Detail

section of the UI by default.

  Note

Changing the result type settings leads in most cases to the need for a complete reassignment of objects to the comparison

values of the expression. We therefore recommend to take extra care before you decide to change the result type settings of an

already defined case expression.

Case-Sensitivity

If you assign a context data object of type text as the expressions case parameter, the system lets you define whether the value

comparisons shall be done in case-sensitive mode or not.

More Information

This is custom documentation. For more information, please visit SAP Help Portal.

66


10/15/26, 3:15 PM

Creating a Case Expression

Constant Expression

Use

A constant expression is the simplest of all expression types. It allows you to create an expression and set a constant value that is

returned after processing. A constant expression can be used for various purposes:

Define result values for other expressions

Define test parameters for comparison operations.

Define a value list for elementary data objects

There are six types of Constant expressions:

Constant Expression Type

Text

Number

Boolean

Amount

Quantity

Timepoint

  Note

Text (Description)

Character

A text constant can hold a string with a maximum length of 255

characters.

Number with decimals

A number constant can have a maximum length of 46. The length

represents the number of digits without exponent or sign.

Boolean value

Number and currency

Number and unit of measure

You can set abstract Date, abstract Time, abstract Data Time,

Global Date Time, Local DateTime Offset

The type of a constant expression can only be defined upon creation. Once the expression has been saved, the constant type

cannot be changed anymore.

More Information

Creating a Constant Expression

DB Lookup Expression

Use

The DB lookup expression performs a database lookup from within BRFplus. It is used to access the records stored in a data

dictionary (DDIC) table or to retrieve information about a table.

This is custom documentation. For more information, please visit SAP Help Portal.

67


10/15/26, 3:15 PM
Features

Modes of Operation

Data Retrieval Mode

In this mode, the data is retrieved from a database table. The expression performs a simple selection operation in the

specified table. The selection is defined by the following settings:

Selection Flag

Specifies whether a multiple select ( All Entries) or a single select ( Single Entry) should be performed.

  Note

If you choose All Entries for the selection, the result data object assigned to the DB lookup expression must be of

table type.

Table Name

Specifies the database table from which data is read. You can access any table available in the data dictionary of the

backend system. It is not necessary to bind the database table to a BRFplus table data object.

Field Conditions

Specifies the conditions applied to the different table fields for refining the search result. Based on the field

conditions, the WHERE clause of the performed selection is built.

The value that is actually selected from the table depends on the result data object type:

If the result data object is an element with a name corresponding to one of the table fields, the expression only

selects that one value.

If the result data object is a structure, then the database fields corresponding to the structure fields are read.

If the result data object is a table, then the source table fields corresponding to the result table fields are read. As

opposed to using an elementary or structure data object, multiple entries can be read.

  Note

The system tries to map the context data object fields to the fields of the result data object, based on the field type and

name. However, there is no guarantee that the mappings are complete or adequate for the given use case. You should

therefore always check the field mappings and adjust them where necessary. For more information, see the Field

Mapping section below.

Aggregation Mode

In this mode, the result of an aggregation function applied to a database table is returned. The following aggregation

functions are supported:

Maximum

Minimum

Sum

Average

Count

The aggregation functions can be applied on distinct fields or on entire table records (all fields in a row). The following

example illustrates the effects of changing this setting:

This is custom documentation. For more information, please visit SAP Help Portal.

68


10/15/26, 3:15 PM

  Example

You create a DB lookup expression that reads from DDIC table T100, which is used for storing message short texts in an

SAP system. The expression shall return the number of records (aggregation function Count) with German short texts (

SPRSL = DE). In a given system, the expression may yield the following results, depending on the distinction setting:

Setting

Result

Comment

Select Count of Records From T100 With SPRSL = DE

110650

Select Count of ARBGB From T100 With SPRSL = DE

1615

Select Count of SPRSL From T100 With SPRSL = DE

1

Total of table rows with the

language field (SPRSL) set

to DE

Total of message classes

(ARBGB) with at least one

message in language DE

Total of unique table rows

with the SPRSL field set to

DE. Though there are more

than 100000 rows in the

table that satisfy the

condition, the distinct

selection for the SPRSL

field lets the search stop

after the first match

because the second

match would already yield

a duplicate.

It depends on the type of an elementary data object to determine which aggregation functions are supported:

Type

Supported Aggregation Functions

Number, Amount, Quantity

All aggregation functions

Boolean, Text

Maximum, Minimum, Count

Timepoint

Count

Existence Check Mode

In this mode, the result data object yields either true or false depending on whether a line exists in the DDIC table that

satisfies the WHERE condition.

Field Mapping

When you are working with a DB lookup expression in data retrieval mode, this means that you want to collect a particular subset

of records from the database table used as the context data object, and that you want to transfer the selected records into a

BRFplus table data object used as the expression's result data object.

Generally, the two table data objects involved are not identical (because otherwise, you would overwrite the original table content

with the result of the selection). As a consequence, you need to define a mapping relationship between the fields from the source

table to the fields in the target table. The maximum number of possible relationships is determined by the number of fields

available in the target table. To define the field mapping, you can use the following features:

This is custom documentation. For more information, please visit SAP Help Portal.

69


10/15/26, 3:15 PM

Automatic mapping

As soon as you have defined both the source and the target table, the system automatically scans the source table for fields

with the same name and type as the fields in the target table. Each matching source field is assigned to the corresponding

target field. If you are familiar with the ABAP programming language, you may already know this mechanism that is

available with the MOVE-CORRESPONDING statement. The automatic field mapping is just a proposal and can be

overwritten manually.

Manual mapping

You can manually associate source fields to the target fields. This is useful to map fields that have the same semantic but

different names, so that the automatic mapping mechanism cannot recognize their correspondence. You can also manually

choose from the source fields for already existing automatic mappings.

For manual mapping, the system offers you the list of source fields in a menu. However, this menu is restricted to the first

nine fields of the table. If the source table contains more fields, you can access these fields by choosing Select other

element from the menu.

Field aggregation and grouping

You can define that a target field receives an aggregated value derived from the values found in the corresponding source

field. For this, the system offers the same aggregation functions that are also available in aggregation mode of operation

(maximum, minimum, average, count, sum). For an overview of the supported aggregation functions for different data

types, see the respective table in the Modes of Operation section above.

If you use field aggregation, all other target fields that are currently not using aggregation are automatically assigned the

Group By flag. This is to make sure that only the set of unique tuples of these fields is written to the target table, rather than

repeating the value of the aggregated field for each single record in the selection.

  Note

If an aggregated source field is of type amount or quantity, the system automatically adds a grouping by the currencies

or units of measure that appear in the source field. This additional grouping is not visualized in the DB lookup UI in the

BRFplus workbench, but you can check it in the SQL view of the selection criteria.

SQL view

All the settings that you make with respect to field mapping, aggregation, and grouping have an impact on the way how the

system accesses the table used as the expression's context data object. If you are a programmer, you may find it helpful to

see the SQL code that the system generates in order to reflect the settings that you make in the UI. For this, the system

offers you an insight into the SQL representation of the current settings. You can have a look at the SQL statement by

choosing View SQL.

Restoring default settings

After having applied different manual modifications to the default field mapping, it may sometimes turn out that the

expression behavior changes into an undesired direction. In such a situation, it can be helpful to undo all the changes and

start right from the beginning. For that purpose, you can choose Restore Default Mapping. This function reverts all manual

mappings and restores the automatic mapping based on the MOVE-CORRESPONDING logic.

Constraints

The DB lookup expression is subject to limitations with respect to the complexity of the database access command ( WHERE

clause) that the system generates depending on the given fields and conditions. The following limitations apply:

Maximum number of fields: 255

Maximum number of conditions: 255

This is custom documentation. For more information, please visit SAP Help Portal.

70


10/15/26, 3:15 PM
More Information

Creating a DB Lookup Expression

Data Binding

Table Operation Expression

Decision Table Expression

Definition

A decision table expression is used to compare a given input against a list of predefined combinations of conditions. Each

combination has an individual result assigned which is returned as the expression result when the input data matches the

particular combination.

Structure

The decision table is built up as a table with the following elements and settings:

One or more columns representing the different conditions against which the input data is compared

One or more columns used to hold the result that is returned by the expression if all the conditions in a row are satisfied

One or more rows that are unique in terms of their combined conditions

Features

General Concept

A decision table expression sequentially processes business rules based on a set of inputs. At runtime, the input data that is

supplied to the decision table is compared against the defined conditions, starting with the first row. All cells are evaluated by

checking the column value against a number of range comparisons. For each cell, a boolean result is returned. If all cells in a row

are evaluated as true, the evaluation stops and the expression returns the result associated with the current conditions. Otherwise,

processing continues with the next table row until either a matching set of conditions is found or the end of the table is reached.

  Note

Due to the sequential processing of the rules defined in the table from top to bottom, we recommend that you define the rules

starting with the most specific condition in the first row, followed by rules with a decreasingly specific set of conditions

assigned. Otherwise, situations could occur where a given input that satisfies an unspecific condition would lead to the

expression result defined for that condition, without giving the system a chance to test whether there is a more specific

condition that would match the input data even better.

The check functions of BRFplus can detect many of this kind of sequential arrangement errors and make you aware of the

problem. Also, with the Rearrange function you can let the system correct at least the most obvious misarrangements

automatically (cells with unspecified values are moved to the bottom of the table).

  Example

A decision table consists of two condition columns, Region and Country, and a result column Payment Target. For region

Europe alone, the payment target is defined as 60 days, while for region Europe and country Germany the payment target is 30

days. The input data is Region= Europe and Country= Germany. If the condition for region only is evaluated before the

This is custom documentation. For more information, please visit SAP Help Portal.

71


10/15/26, 3:15 PM

combination of region and country, then the unspecific region check would already yield a result, and the more specific

condition for country and region would never be tested. That is, the payment target for the input with Country= Germany would

be erroneously evaluated as 60 days although it should be 30 days.

The decision table data consists of a set of nested expressions for each table cell. With the cells in condition columns, the

expressions are typically value ranges or constants, and they use the corresponding column data object as a test parameter.

Normally, a condition column is defined by assigning a data object to it. However, condition columns can also be derived from

nested expressions. Each cell in a row can be either a single value, an enumeration of distinct values, or a range of values against

which the inputs are checked.

Result Columns and Result Data Object

The data structure of the result column is derived from the result data object. A decision table can also have multiple result

columns. This can be achieved either by assigning a structure data object as the result data object, or simply by providing several

elementary data objects as result columns. In the latter case, the system offers to create a new structure data object containing

the selected elements. This structure is then automatically assigned as the decision table's result data object.

For special purposes, it is also possible to define the result column as Action Column. In this case, you define an action for each

combination of conditions that shall be triggered if the input data matches the condition defined in a table row.

  Note

You can use a combination of an action and a data object value in the result column of a decision table. However, there can be

no more than one action assigned to the result column.

Modifying Technical Settings

The following sections deal with the various technical settings that you can fine-tune to adapt a decision table's behavior to your

use case. These settings include the definition of condition and result columns, as well as many other details that are not needed in

everyday's use. To avoid confusion, these settings are therefore hidden by default when you maintain a decision table. You can

access the technical settings as follows:

When you create a new decision table, the system presents you the technical settings screen so that you can define the

necessary features like condition and result columns.

When you maintain an already existing decision table, you can access the technical settings by clicking

 at the rightmost

border of the Detail section toolbar.

  Note

Access to the technical settings of a decision table is subject to the personalization settings in effect. For more information, see

Workbench Personalization, section Expression - Decision Table.

In addition, changing the technical settings is disabled as long as a filter restricting the decision table's content is active. This is

to prevent unexpected and ambiguous system behavior: For example, if a filter is active so that only rows 5 and 12 are visible out

of a total of 25, inserting a new row between rows 5 and 12 would leave the question open where exactly to insert the new row.

Therefore, the system consequently disables features that could cause confusion in filter mode.

Single vs. Multiple Match Mode

A decision table can be run in two different modes of operation, depending on the setting of the Return all matches found

indicator:

Single match mode ( Return all matches found= false)

This is custom documentation. For more information, please visit SAP Help Portal.

72


10/15/26, 3:15 PM

In single match mode, the input data is tested against the conditions defined in a table row. If the input satisfies all the

conditions, the associated result is returned and processing of the decision table stops. In other words, the system returns

the result associated with the first matching row. This is the default mode.

Multiple match mode ( Return all matches found= true)

In multiple match mode, the input data is tested against the conditions defined in all of the table rows. All matching results

are collected in the result data object and returned as the result of the evaluation.

  Note

Since multiple match mode is designed for delivering more than one value as the expression's result, the result data

object for a decision table in multiple match mode must always be a data object of type table.

Handling of Partial Matches

Both single match mode as well as multiple match mode follow the basic principle that only if the input data passed to a decision

table matches all of the specific condition values in a row this is considered a match. However, use cases may exist where the input

does not match any of the decision table rows, but simply raising an exception is not sufficient. This is where partial match

handling comes into play. This processing mode is used to address the following scenario:

Context data passed to the decision table does not match any of the condition rows defined in the table.

You want to continue processing not only based on the fact that there is no match, but on the information about how near

the context data came to a matching result (but still failed to match a condition completely).

For this purpose, you can set the Return exception for partial match flag. Setting this flag has the following effect: While

processing the decision table, the system keeps track of the maximum number of matched conditions per row. If the last row in the

table has been processed and there is still no matching row, the system raises exception CX_FDT_PARTIAL_MATCH with the

highest observed match count passed to attribute CX_FDT_PARTIAL_MATCH->MV_MAX_COND_MATCHED. It is then up to the

calling application to handle this exception and implement the desired system behavior based on the maximum number of

matched conditions for the given input.

  Note

Setting the Return exception for partial match flag has a negative impact on system performance. This is due not only to the

necessary counter comparison for each row but also to the fact that certain optimization measures cannot be applied during

code generation. We therefore recommend to set this flag only if you definitely need to access the maximum number of

matched conditions for your use case.

Initial Value

If no matching condition is found for a given input, the decision table raises an exception instead of returning a result. You can

override this default behavior by setting the Return initial value if no match is found indicator. If this indicator is set, the decision

table returns the initial value that is defined for the type of the result data object. With this setting, it is possible for you to consider

the unsuccessful processing as a defined result rather than an error and continue with processing.

  Note

If you use this option, it may be necessary to take additional measures in order to make sure that further processing steps do

not confuse an initial value with a well-defined result. For example, the initial value for a result data object of type number is 0,

which could of course be the intended result for a satisfied condition as well.

Table Content Checks

This is custom documentation. For more information, please visit SAP Help Portal.

73


10/15/26, 3:15 PM

In addition to the standard checks for technical consistency, you can carry out additional checks to ensure that the decision table

data is error-free and yields the expected results from a business perspective. For more Information, see Decision Table Content

Checks.

Table Optimization

BRFplus offers some tools that help you condense the table content and optimize the table arrangement for better performance.

For more information, see Decision Table Optimization.

Optional vs. Mandatory Entry of Condition Data

The default behavior for evaluating a decision table is as follows:

The value of an input data field is compared to the value in the corresponding condition column of the table.

If the two values match, the condition cell is evaluated as true.

This process is repeated for each condition in the table row until either all the conditions are satisfied (row is a match) or

until a condition is not satisfied (processing continues with the next table row).

If this default behavior does not fulfill your needs, you can modify it for each condition column individually in the following way:

Mandatory input

With this indicator set, the system forces you to provide a condition value at design time for the respective column in each

row that you enter in the table definition. Such a condition can therefore not be used for providing an unspecific empty

condition that would be evaluated as true regardless of the input data.

  Example
In the example outlined above with the two condition columns Region and Country, the Region column would be defined

as a mandatory entry to make sure that an input must at least match one of the regions provided by the decision table

to be further evaluated. As opposed to this, the Country column is not mandatory so that an input with a matching

region but an unknown country can still be processed. To accomplish this, you need to provide an additional table row for

each region combined with an undefined country.

Retrieving Table Content

Depending on the use case, decision tables can contain a high number of cells (many thousands of rows, dozens or hundreds of

columns). This can make it sometimes difficult to retrieve a particular cell you are interested in. For this purpose, BRFplus offers the

following tools that help you navigate through the content of a decision table:

Row Filter

You can define filter criteria that a table row must match to be displayed. For each column, you can define a separate filter that

applies to that particular column only. If filters are defined for more than one column, the filter criteria are combined with a logical

AND operator before they are evaluated. That is, a row is only displayed if all filter criteria that are currently in effect are satisfied by

the affected columns of a row at the same time.

Filter conditions remain in effect either until you explicitly change or reset the conditions, or until you navigate to a different object.

It is not possible to permanently associate certain filter conditions to a decision table.

To define a filter for a column, move the mouse cursor over the header cell of the desired column and click on the small triangle in

the lower right corner. If a filter is already defined for a column, the system displays a filter symbol on the column header cell.

Find

This is custom documentation. For more information, please visit SAP Help Portal.

74


10/15/26, 3:15 PM

With this tool, you can search the table content for a string. If the search string exists in the table, the row containing the searched

string is highlighted. With the Next and Previous buttons, you can navigate to further occurrences of the search string.

  Note
For both tools, the following applies: The comparison between the filter condition, or search string, and the actual cell content is

done via an implicit content conversion into text form. This means that everything that is displayed in a cell must be taken into

account when you define the filter condition. For example, if a cell contains a value range that is displayed as [10..20] and

you want to include this cell in a filter, you have to mention the square brackets explicitly in the filter criterion, like [10*. Using

10* as a filter criterion (without the bracket) instead would exclude the cell although the square brackets are not really part of

the cell content and only displayed for the sake of giving a visual hint on the fact that the cell contains a value range.

Both tools support wildcards (' +' matches any single character, ' *' matches any string). All searches and string comparisons

are case-insensitive.

If a search is performed while a filter condition is in effect, the search is restricted to those rows that are included in the folder

and therefore visible.

Table Data Export And Import

You can exchange the condition and result data of a decision table with Microsoft Excel. This enables you to share your table data

with people who may not have access to BRFplus but might give input from a business perspective. The necessary steps for

exporting and importing data are described in Exchanging Decision Table Data With Microsoft Excel.

Column Protection

One of the big advantages of BRFplus is that it makes the criteria for the business decisions in your company transparent and easy

to change. While such transparency can be counted as an asset in itself, it can still be inappropriate for certain parts of your

business. Here, you may want to decide that the decision criteria for a particular business case shall be protected against

unauthorized change or even be completely invisible. You can accomplish this with the help of the Column Accessibility setting,

both for condition columns and result columns of a decision table:

Full Access (Changes Allowed)

With this setting, a user can deliberately change the values of the column cells. This is the default.

Display Only (No Changes)

With this setting, a user can see the values in the column cells without being able to make any changes.

Hidden

With this setting, the column is hidden completely in the BRFplus workbench at design time as well as at runtime. Without

checking the table settings, a user does not receive any visual indication that the column exists.

Example

The following table illustrates the decision table example given above to determine the payment target for a customer invoice:

Region *

Country

Company

Payment Target (Days)

Americas

Americas

USA

USA

Europe

Germany

Miller Inc.

90

75

30

This is custom documentation. For more information, please visit SAP Help Portal.

75


10/15/26, 3:15 PM

Region *

Europe

Europe

Country

France

Company

Payment Target (Days)

45

60

In this table, you see a list of different payment targets being defined to match the different business habits in different places in

the world. The Region, Country, and Company columns represent the condition criteria (context data) while the Payment Target

(Days) column holds the resulting value to be returned for each of the conditions (result data object). The table reflects the

common experience that in Germany customers usually pay their invoices in relatively short time upon invoice receipt, while in

other regions or countries this time can be longer. It may also be useful to define special payment targets for individual customers,

depending on their assumed financial strength or on your company's experiences with these customers in the past.

Note that the entries in the table are sorted by the amount of specific information available, starting with the most specific entry

for an individual company in the USA and ending with a generic entry for all customers based in Europe who do not satisfy the

conditions in the more specific rows.

  Note
Do not confuse this sort order with the alphanumeric sort function known from most table controls. Rather, sorting the entries

of a decision table means that you have to manually arrange the entries such that they best match the business case you want

to cover. So this is a semantic sort order based on business decisions, not an alphanumeric sorting based on names.

The asterisk ("*") in the Region * column header indicates that an entry in this column is always required - in other words, at least

the customer's region information is needed for the decision table to determine a payment target for a customer.

The decision table entries for the Americas region define only payment targets for customers based in the USA. If, for example, you

would supply a customer from Canada or Brazil as input data at runtime, the decision table would raise an exception because

neither a specific condition for these countries nor a generic condition for all countries in the Americas region (except USA) has

been defined.

More Information

Creating a Decision Table Expression

Decision Table Content Checks

Decision Table Optimization

Exchanging Decision Table Data With Microsoft Excel

Decision Table Content Checks

Definition

In addition to the checks for technical correctness that are available for all BRFplus object types, you can perform some content-

oriented checks for a decision table. These checks are used to ensure that the decision table definition is error-free and yields the

expected results from a business perspective. Unlike the more technical checks, you can explicitly perform these checks with the

respective commands assembled under the Additional Actions menu. These checks are:

Completeness Check

This is custom documentation. For more information, please visit SAP Help Portal.

76


10/15/26, 3:15 PM

With the completeness check, or gap check, the system verifies that the values of a particular condition column are defined

as a continuous sequence of values with no gaps in between. With gaps in the sequence of values, it could happen that an

input value could not be processed although, from a business point of view, all possible values within a given range must be

processed by the decision table.

Once the check has finished and value gaps have been determined, the system tries to make a suggestion for additional

table rows that would close the gaps. This is an easy way for you to make sure that the table returns a defined result for the

value combinations that are not yet covered. However, in certain situations, these row suggestions lead to a state of formal

completeness only that may still need further manual refinement to meet your business requirements.

  Example

A decision table has, among others, a Travel Class condition column with a data object assigned that is bound to a list of

three domain values, namely Economy Class, Business Class, First Class. During the completeness check, the system

detects that for a particular combination of conditions, only Business Class and First Class are taken into consideration,

but there is no table row for Economy Class. The check would then notify you of this potential gap so that you can

decide whether the missing value has been omitted intentionally or not.

Overlap Check

With the overlap check, the system detects whether the value ranges assigned to the condition columns are distinct and

free of overlappings. With overlapping ranges, the system would not be able to handle correctly an input value that falls into

the overlapping zone.

  Example

A decision table has an Invoice Total condition column with value ranges defined as 500...1000 in one row and

750...1500 in another row. With an invoice total of 900 as input, it would be impossible for the decision table to

determine which of the two rows is the correct one. The system would simply choose the first matching row, regardless

of whether this is, from a business point of view, the intended decision or not.

The checks described above are always carried out by the system when you explicitly force the system to do the check, or as an

implicit check when you activate the decision table. However, since these checks are focused on correctness in terms of business

adequacy, not on technical consistency, you can decide how the system shall behave if one of the checks detects a problem. In the

Table Settings dialog, you can choose from the following options:

System Default

In case of a problem, the system sends the corresponding message with the message type as defined in the backend

system (in most cases, message type 'warning' is used).

Show Messages as Error

This forces you to solve the problem in the table definition. Otherwise, the decision table cannot be activated.

Show Messages as Warning

The system makes you aware of the problem but still lets you activate the decision table.

Do not show any messages

Although the problem was detected, the system does not make you aware of it. Activation of the decision table is possible.

  Note
The table content checks are performance-critical because they partially imply operations where each cell in the table must be

compared with all other cells. To avoid overloading the system, the checks can only be executed as long as certain fixed

This is custom documentation. For more information, please visit SAP Help Portal.

77


10/15/26, 3:15 PM

limitations are not exceeded. For example, the completeness check can only be performed with tables that have no more than

10000 rows.

Decision Table Optimization

Definition

The decision table is the most popular and frequently used of all the expression types offered by BRFplus, and experience shows

that customers tend to build up very complex tables with dozens of columns and thousands (sometimes tens of thousands) of

rows. Complexity is of course a threat to performance. Therefore, BRFplus offers some tools that help you condense the table

content and optimize the table arrangement for better performance. These tools are available in the Additional Actions menu:

Rearrange

The purpose of this function is to help you shift all table rows containing unspecified cells to the bottom of the table. This is

to make sure that the more specific conditions in a table are processed first.

When you execute this function, you are first prompted to define a sort priority for the table columns. By default, the system

processes the columns from left to right. For each column, the system determines the unspecified cells and moves the

corresponding rows to the bottom of the table. Rows that have already been shifted remain at their position, whereas rows

that are shifted due to unspecified cells in lower priority columns are shifted on top of the already shifted rows, but

underneath the rows with specified cells.

  Example

In this example, you can see the effect of the Rearrange function. The table to be rearranged has unspecified cells at

position A5 and B3.

#

1

2

3

4

5

6

#

1

2

4

6

3

5

A

P100

B

1

P300

0..2

P100

<...>

P300

<...>

P200

A

P100

2

3

3

B

1

P300

0..2

P300

P200

2

3

P100

<...>

<...>

3

This is custom documentation. For more information, please visit SAP Help Portal.

78


10/15/26, 3:15 PM

In the first stage, the system analyzes column A and finds an unspecified cell in row 5, so row 5 is moved to the table

bottom. After column A has been processed, the system continues with column B. Here, an unspecified cell is found in

row 3. The system moves row 3 down, but one row above row 5 that has already been moved to the bottom. All other

rows remain at their original position.

#

1

2

4

6

5

3

A

P100

B

1

P300

0..2

P300

P200

<...>

2

3

3

P100

<...>

With the changed sort order, the system starts with column B. Consequently, row 3 is now moved to the table bottom,

and row 5 is moved to the position one row above the already moved row 3.

Merge Rows

With this function, you let the system analyze a set of rows to find out whether it is possible to cover the conditions defined

in different rows by one single row. If the system finds a suitable solution, it creates a new row containing the combined

conditions and deletes those rows whose conditions have been joined in the new row. This function requires that all selected

rows have the same result data value assigned, and that at least two rows are selected.

  Example

You want to condense a table as much as possible. For this, you select all rows of the following table and choose

Additional Actions

 Merge Rows .

#

1

2

3

4

5

6

#

1

2

3

6

A

P100

P100

B

1

2

Result

high

low

P100

<...>

high

P100

P100

P200

3

4

3

high

high

high

A

B

Result

P100

1; 3..4

high

P100

2

low

P100

<...>

high

P200

3

high

This is custom documentation. For more information, please visit SAP Help Portal.

79


10/15/26, 3:15 PM

After the merge, table rows 1, 4, and 5 have been condensed into row 1. Rows 4 and 5 have been deleted. The remaining

rows cannot be merged for the following reasons:

Row 2 has a different result than the other rows.

Row 3 has an unspecified cell that cannot be combined with specific values.

Row 6 has a different value in column A.

Exchanging Decision Table Data With Microsoft Excel

Use

You can exchange the condition and result data of a decision table with Microsoft Excel. You can take advantage of this function in

the following situations:

You can share your table data with people who may not have access to BRFplus but might give input from a business

perspective.

The use case that you want to address with the decision table has already been dealt with in your department, so a lot of

well-defined rules for the decision table may already exist and only need to be adapted to BRFplus.

You can export the decision table data to a spreadsheet so that you can continue working on the conditions while you are

offline or while the system is not available.

You can use the export function for creating an additional backup of the table data that can easily be retrieved.

  Recommendation
During the import of data from an Excel spreadsheet, BRFplus tries to match the data to be imported with the columns of the

decision table. To clearly understand what the spreadsheet data must look like for a successful import into a particular decision

table, we recommend that you start by exporting some data from the decision table to the spreadsheet file. The spreadsheet

file then contains the columns and data formats that are required for an error-free import.

When you choose to export decision table data to an Excel file, the exported file contains three worksheets:

Data: In this worksheet, you find all the condition and result data that you have maintained for the decision table in BRFplus.

Help: In this worksheet, you find detailed information on the correct data format for values and operators as expected by

the BRFplus import function. This information worksheet is part of every Excel file that you create with the BRFplus export

function.

Column Details: In this worksheet, you find technical information on the respective elementary data object referenced by

each table column. This helps you to decide whether a manually entered value can be imported without problems or not.

Again, this information worksheet is part of every Excel file that you create with the BRFplus export function.

Handling of unsupported data types

Data exchange between BRFplus decision tables and Excel files is only supported for discrete values and range expressions. If a cell

contains any other type of data (for example, a boolean expression), the system handles this situation according to the following

rules, depending on the transfer direction and the setting of the Override Expressions With Fixed Values indicator (only relevant

for import):

This is custom documentation. For more information, please visit SAP Help Portal.

80


10/15/26, 3:15 PM

Override Expressions

Export

Import

false (default)

Expression text is written into XLS cell for

Cell data other than single values or ranges

reference reasons.

true

are skipped during import; corresponding

cell in decision table remains unchanged.

Cell data other than single values or ranges

raises an error message, and import is

stopped.

If the receiving cell in the decision table

contains an expression, but the XLS cell

contains a single value or range, the

expression is overwritten by the imported

value.

Prerequisites

Exchanging data with Microsoft Excel is done with the help of the XML-based file format (file extension .XLSX) introduced with

Microsoft Excel 2007. If you are using an older version of Microsoft Office, you can download the Microsoft Office Compatibility

Pack to upgrade the supported file formats from the Microsoft Download Center ( http://www.microsoft.com/en-

us/download/details.aspx?id=3

). Once you have downloaded the Compatibility Pack, you have to install it on every workstation

that has an older version of Microsoft Office installed.

  Note

Installing the Compatibility Pack on your workstation requires administrator authorizations.

Activities

Exporting Decision Table Data to Microsoft Excel

1. In the BRFplus Workbench, open the decision table whose data you want to export in the Object Manager panel.

2. Choose  Additional Actions

 Export to Excel

.

The system prompts you to either open or save the Excel file. Depending on your choice, the system performs the following

actions:

Open: The exported data is written to an Excel file in a folder for temporary files on your local machine, and the file is

loaded for reviewing in Microsoft Excel.

Save: The system displays a Save As ... dialog where you can enter the desired file name and storage location. By

default, the system suggests <name of the decision table>.xlsx.

Importing Decision Table Data from Microsoft Excel

1. In the BRFplus Workbench, open the decision table into which you want to import data from an Excel file in the Object

Manager panel.

2. Choose  Additional Actions

 Import from Excel

.

3. In the Excel File Import dialog, enter the name of the Excel file you want to import.

4. Decide how the system shall proceed in case the Excel file contains data that does not fulfill the requirements for proper

import.

This is custom documentation. For more information, please visit SAP Help Portal.

81


10/15/26, 3:15 PM

For details, see section "Handling of unsupported data types" above.

5. Once the data has been imported, save the decision table.

  Note
Keep in mind that BRFplus data objects of type text can hold a maximum of 255 characters. If a spreadsheet cell contains

alphanumeric data exceeding this threshold, the imported cell content will be truncated after character 255.

Decision Tree Expression

Use

A decision tree expression allows the definition of a binary tree of expressions. The non-leaf nodes are called condition nodes.

These nodes return a result of type Boolean. Depending on the result, the left or the right node is processed. Once a leaf node is

reached, the assigned expression is processed and the corresponding result is returned as the result of the whole expression.

Structure

The decision tree structure is a concatenated list of yes/no decisions. Each condition node is broken up into two branches

representing the true or the false alternative for that condition. Each branch can either lead to another condition for further

refinement or to a leaf node with an assigned result. The following picture illustrates the basic principle:

Decision Tree Schema

Features

Result Types

This is custom documentation. For more information, please visit SAP Help Portal.

82


10/15/26, 3:15 PM

You can decide whether a decision tree expression shall return a value or perform an action:

Return Value: In this mode, you have to take care that all leaf nodes have a value or expression assigned with the same type

as the result data object of the decision tree expression.

  Note

When defining a decision tree in the BRFplus workbench, first assign a result data object to the tree expression before

you start to define the results for the different leaf nodes. Only under this condition the system gives you access to

suitable expressions or lets you enter result values directly. With no result data object defined, you can only assign

element data objects to a node as a result.

Perform Action: In this mode, the decision tree expression triggers the action assigned to the leaf node that matches the

input. The result data object is automatically set to the predefined Actions table that returns the list of IDs of the actions

(result action plus follow-up actions that may be associated with that action) that are executed.

Once the result type settings have been made and the decision tree has been saved, the system displays these settings in the

Detail section of the UI by default.

  Note

Changing the result type settings leads in most cases to the need for a complete reassignment of objects to the leaf nodes of

the decision tree. We therefore recommend to take extra care before you decide to change the result type settings of an already

defined decision tree.

More Information

Creating a Decision Tree Expression

Search Tree Expression

Action Types

Dynamic Expression

Use

The dynamic expression is used to call another expression dynamically. The called expression is not statically defined at runtime.

Rather, it is dynamically determined at runtime based on the evaluation result of a nested expression that is assigned to the

dynamic expression at design time. This can be useful if you have a set of specialized expressions that are optimized to handle

specific use cases that are different in certain details but similar in nature. With the help of the dynamic expression, it is possible to

determine the most suitable expression at runtime.

Features

Context Mapping

The dynamic expression offers the following modes for the context mapping:

Complete context but not expression variable

All available context data objects of the dynamic expression are supplied to the called expression.

This is custom documentation. For more information, please visit SAP Help Portal.

83


10/15/26, 3:15 PM

Matching context

Only those context data objects of the dynamic expression that can be matched to the context data objects of the called

expression are supplied to the called expression.

Called Expression

You choose one expression and assign it to the dynamic expression. The assigned expression is called by the dynamic expression

at runtime. The called expression must be configured such that it handles the context data provided by the dynamic expression,

and returns a text data object as result. The result must contain the ID of a particular expression to be processed, depending on the

context data. The result of this secondary expression is then passed back to the dynamic expression.

Result Data Object

For the result data object, you can use any kind of data object. However, it is important to make sure that the result data object of

the dynamic expression and the result data objects of all the secondary expressions must be compatible.

Constraints

The flexibility that you gain with dynamic expressions also has a logical drawback. Due to the dynamic nature of this expression

type, a number of checks that BRFplus can perform for most other expression types at design time are not supported for dynamic

expressions. It is therefore possible that any potential design flaw remains hidden until it becomes effective at runtime.

Unlike most other object types in BRFplus, there is no code generation support for dynamic expressions. Therefore, this expression

type is not recommended for time-critical tasks, or scenarios where high data load is expected. Another consequence of the fact

that dynamic expressions cannot be generated is that they are not supported in service deployment scenarios that you may want

to set up with SAP Decision Service Management (DSM).

Example

In a rule system for a social services authority, you want to handle application forms for different types of services such that they

can be entered into the system with the help of an expression serving as a single point of entry for the business user. Then, you use

a dynamic expression to determine the type of the application form to be processed. In the dynamic expression, you use a decision

table as nested expression. By passing the application form type information to the decision table as context data, the decision

table determines the expression associated to the application form type in question and hands the form over to that expression for

further processing.

More Information

Creating a Dynamic Expression

Formula Expression

Use

A formula expression allows you to perform a wide range of calculations. The formula expression offers the basic mathematical

operations (addition, subtraction, multiplication, division), more advanced operations (such as exponentiation or binary AND),

comparisons (greater than, less than, etc.), and a wide variety of formula functions for different purposes and data types (date and

time calculation, string handling and manipulation, conversion functions, system functions, etc.). You can also enter comments into

a formula to help others better understand the purpose of a particular calculation step.

This is custom documentation. For more information, please visit SAP Help Portal.

84


10/15/26, 3:15 PM
Features

Editing Mode

The system offers two different editing modes for maintaining a formula expression, Normal Mode and Expert Mode:

Normal Mode

In Normal Mode, the system tries to preserve the formula integrity by preventing the user from directly editing the formula

text. Rather, a user would make use of the various predefined options offered in the BRFplus workbench by clicking the

respective function buttons or choosing an option from a list. This is true even for constant values you might want to enter

as a formula operand. To accomplish this, you have to use the buttons provided for entering a Number or a String value.

Expressions and data objects that are used as formula operands are displayed with their technical name.

Expert Mode

In Expert Mode, the system allows the user to manually edit the formula text. This can speed up formula maintenance

significantly, but the user is completely responsible for the syntactical correctness of the formula text. Expressions and

data objects that are used as formula operands are displayed with their ID.

Operands

In a formula expression, you can use elementary data objects and expressions as operands. In addition, structure or table data

objects may also be used in a formula if the formula contains a function that expects a data object of these complex types as a

parameter (for example, all table functions expect a table data object as a parameter).

Context Data

In the BRFplus workbench, the system presents a list of data objects that can be used as formula operands. The data objects in the

list are inherited from the context of the function to which the formula expression is assigned. In other words, a stand-alone

formula expression that has not yet been assigned to a function cannot offer any context data objects.

  Note

If a formula expression is assigned to more than one function, the list of context data objects available as formula operands

represents the intersection of the context data objects of all involved functions. This is necessary to ensure that the formula can

be calculated properly, regardless by which function it is called.

Formula Functions

In a formula expression, you can choose from a large number of formula functions that help you retrieve, transform, and analyze

data. For a better overview, the functions are grouped into categories as follows:

Function Category

Date and Time

Examples

Calculation of difference between two points in time, in different

units of measures; determination of leap years; extraction of

different parts from a given point in time; etc.

String Functions

Concatenation and extraction of strings; string length; string

similarity; etc.

Mathematical Functions

Logarithms; exponentiation; trigonometric functions; etc.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

85


10/15/26, 3:15 PM

Function Category

Examples

Parameters passed to the trigonometric functions must be

given in radians (one full circle = 2 Pi).

System Functions

Retrieval of system-specific information like factory calendar,

Table Functions

operating system, logon language, etc.

Retrieval of information about, or stored in, a BRFplus table data

object like maximum or minimum value, sum, average, row count,

etc.

Miscellaneous Functions

Conversion of quantities and amounts; number rounding; check for

initial values; etc.

In addition to the function grouping, the system offers another way of finding a function: In the Filter by Text field, you can enter

the name of a function (or a part of it) and let the system display all function names that match the search string. This is helpful if

you know the function name already. Combined with the Show All Functions function category, this gives you the fastest access to

the desired function.

For the details of each function, there is online documentation available. There you find all the information about parameters,

types, calling conventions, examples, and more for each function. To display the function documentation, navigate to the respective

function in the list and click the Show link in the Documentation column.

Customer-defined Functions

You can extend the functional scope of the formula expression type by defining additional functions according to the individual

requirements of your use case. You can accomplish this by defining methods in the exit class assigned to the application and

registering these methods as formula functions. For an in-depth documentation of customer-defined formula functions, see the

How to Create Formula Functions paper on SDN (

http://www.sdn.sap.com/irj/sdn/go/portal/prtroot/docs/library/uuid/10e9c96f-0c8b-2b10-6885-f00adbeb314b

).

Rounding Behavior for Amount Data

Internally, BRFplus uses always maximum precision for all calculations where numeric values are involved, according to the number

of decimals defined for the involved data objects. However, there is a special case where the maximum precision of a calculation is

not reflected in the result, namely if the result data object of a formula expression is a data object of type Amount. In this case,

BRFplus uses the number of decimals that has been defined for the currency of the result data object, while the number of

decimals defined in BRFplus is ignored.

  Example

In a formula expression, the following calculation is processed:

25 € / 8

Although the internally calculated result of 3.125 € is precise, the result data object of the formula expression yields a rounded

value of 3.13 € because for European Euros, only two decimals are defined in the Customizing tables.

Quantity Dimension Checks

In addition to the standard consistency checks that are available for all types of BRFplus objects, the system performs some

specific checks for formula expressions containing calculations with data objects of type quantity that have a quantity dimension

assigned. The challenge here is that each unit of measure belongs to a particular quantity dimension (time, length, speed, and so

on), but there is only a limited number of combinations of operands and result data objects with different dimensions that make

sense. Here are some examples:

This is custom documentation. For more information, please visit SAP Help Portal.

86


10/15/26, 3:15 PM

Formula

Result Data Object Valid

Length / Time

Speed

Length / Mass

Number

yes

no

  Note

In the first example given in the above table, do not confuse the Time operand with the BRFplus data object type Timepoint.

The Time operand is in fact a data object of type Quantity with dimension Time. This is used for expressing time durations,

whereas the Timepoint object type is used to refer to a particular point in time.

The system performs quantity dimension checks only for formula expressions with data objects of type quantity where the

Dimension property has been maintained. If there is no dimension information available, this part of the check is omitted. In

case of an undetected dimension mismatch, an error occurs at runtime.

Examples

The following formula shows the usage of one of the system functions embedded in a simple IF statement. The formula returns a

numeric value of 10 if the current logon language is English ("EN"), otherwise the result is 0. instead:

NUMBER = IF ( SYS_INFO_LANGUAGE ( ) = 'EN' , 10 , 0 )

  Note

For complex If Then Else scenarios, we recommend using the Boolean expression.

The following formula demonstrates how the trigonometric functions can be used to calculate the air-line distance between two

locations on Earth. To keep things simple, we assume that the shape of the Earth is a perfect sphere.

Context

The context of the function to which the formula belongs consists of quite a number of data objects that are partially filled by the

user (Departing Town, Destination Town), partially by a decision table (Longitude, Latitude), and partially calculated by the formula

(Distance).

Name

Coordinates

Description

Structure (Longitude, Latitude). Values are determined with the

help of a decision table, depending on the chosen departure and

destination location.

Departure Town, Destination Town

Text data objects filled in by the user interactively.

Distance

Number data object that serves as the formula's result data object.

Longitude Start, Longitude End, Latitude Start, Latitude End

Helper variables used for the calculation.

Pi

Formula

Constant value

6378.137 * ARCCOS ( SIN ( Latitude Start * Pi / 180 ) * SIN ( Latitude End * Pi / 180 ) + COS

This is custom documentation. For more information, please visit SAP Help Portal.

87


10/15/26, 3:15 PM

More Information

Context and Result

Application

Creating a Formula Expression

Function Call Expression

Use

A function call expression calls a BRFplus function, maps the expression context to the function context, and returns a result. A

function call expression can call different functions based on the input.

For example, a function call expression can be used to calculate the tax for different countries. The function call expression calls the

respective functions based on the country and passes the context data.

More Information

Creating a Function Call Expression

Procedure Call Expression

Loop Expression

Use

A loop expression processes a set of rules on a given context for a number of times. The number of repetitions for executing the

rules is defined by a numeric constant, a condition, or by iterating over the rows of a table. The expression can also contain exit

conditions as well as continue conditions for the rules. The loop expression can either return a result that can be used for further

processing or trigger actions.

Features

Processing Mode

A loop expression can be executed in either of the following processing modes:

Perform Action

In this processing mode, the system automatically assigns the predefined Actions table object as result data object. After

loop processing has finished, this table returns the list of all actions that have been triggered by the loop expression.

Return Value

In this processing mode, you can assign any kind of data objects as the expression's result data object. If you use this

setting, it is up to you to make sure that the rules processed at runtime make changes to the value of the selected data

This is custom documentation. For more information, please visit SAP Help Portal.

88


10/15/26, 3:15 PM

object.

Loop Mode

You can choose between the following loop modes to further specify how exactly the loop expression shall operate:

Repeat ... Times

For this mode, you must specify a number indicating the number of iterations that the loop shall run through. You choose

this loop mode for use cases where you know in advance the exact number of iterations needed. The only way for a so-

defined loop expression to run through less iterations than defined is that an optional exit condition is fulfilled.

  Example
You need to calculate a one-year-ahead forecast of sales numbers for a particular product. This forecast shall be broken

down by month. To accomplish this, you define a loop expression of type Repeat ... Times with a fixed iteration number

of 12 to calculate the numbers for each month of the year ahead from now.

Do ... Until ...

For this mode, you have to define a cancellation criterion that must be fulfilled to make the loop expression stop processing.

The cancellation criterion is tested after each iteration. This means that in a Do ... Until ... loop, the rules that have been

defined for the expression are processed at least once.

While ... Do ...

For this mode, you have to define a continue criterion that must be fulfilled for the loop expression to continue processing.

The continue criterion is tested before each iteration. This means that in a While ... Do ... loop, the rules that have been

defined for the expression may not be processed at all.

For Each Entry In ...

In this mode, the number of iterations depends on the number of entries in a table that shall be used as the loop iteration

controller. The object that you select as a controller must be either a table data object or an expression that has a table data

object assigned as its result data object. This is the case, for example, for several of the table operation subtypes, or for a

decision table or search tree expression in multiple match mode. The number of iterations can be further restricted by

additional selection criteria that you may define for the table.

The iteration controller object can be freely selected from all suitable objects in the system. It is not necessary to include

that object in the expression context.

  Caution

For the Do ... Until ... and the While ... Do ... loop mode, it is up to you to make sure that the cancellation or continue criterion is

updated and evaluated during each iteration. Otherwise, the system might be caught in an infinite loop, which must be

terminated manually.

  Note
If you have defined the loop control conditions and decide to change the loop mode afterwards, the reference to the involved

objects as well as the additional selection criteria you may have defined are deleted immediately from the loop expression.

Once you have saved the expression with the new loop mode, the only way to recover the previous settings is to revert to an

older version. This is possible, of course, only under the condition that versioning is turned on for the loop expression.

Loop Conditions

For all loop modes, you can define additional exit or continue conditions for each of the rules to be processed during one iteration.

By doing so, you can override the loop behavior as defined by the loop mode. Conditions enable you to make the loop processing

This is custom documentation. For more information, please visit SAP Help Portal.

89


10/15/26, 3:15 PM

dependent not only on the iteration counter but on any kind of additional test criteria, as long as the test result is expressed in a

boolean value. For example, you may test in a condition if the current user is authorized to perform a particular rule, if the current

date and time lies within a predefined validity period, if the number of articles passed to the loop context qualifies for additional

discount calculations, and so on.

Exit condition

With an exit condition, you can perform any additional tests. If the test result is True, processing of the entire loop

expression is cancelled.

Continue condition

With a continue condition, you can perform any additional tests. If the test result is True, the current loop iteration is

cancelled. Expression processing continues by increasing the iteration counter by 1 and executing the first rule in the rule

sequence.

More Information

Creating a Loop Expression

Random Number Expression

Use

You use the random number expression to intentionally integrate an unpredictable element into your application. This can be

useful for test purposes when you want to check how an application behaves through many iterations with permanently changing

input parameters. Another possible use case could be to let this expression calculate a value that you might assign automatically

to mass objects in your application (provided that no systematic numbering is needed for that), like customer ID, order number,

and so on.

The random number expression is based on the standard ABAP pseudo-random number generator. Whenever the expression is

evaluated, this number generator is started in the backend with a new seed value to ensure that the generated number sequence is

different.

  Note

Keep in mind that the algorithm used for generating random numbers is made for normal business use cases only. This is

because the generated number sequences are identical as long as the same seed value is used. Therefore, the random number

expression is neither intended nor sufficient for security-relevant purposes like password encryption, access codes, or any other

kind of cryptographic use cases.

Features

Modes of Operation

The random number expression offers two modes of operation: The expression can either return a random number between two

boundaries (minimum and maximum) or return a boolean value with a user-defined probability between 0 and 1.

Number

In this mode, the expression returns a random number between two borders (minimum and maximum). You can influence

the range of possible results not only by these two borders, but also by setting the number of decimals. Here, the maximum

number of decimals depends on the definition of the result data object that is assigned to the expression.

This is custom documentation. For more information, please visit SAP Help Portal.

90


10/15/26, 3:15 PM

Probability

In this mode, the expression returns a boolean value. You can fine-tune the expression behavior by setting the statistical

probability for the expression to return the value TRUE. The probability value is given as a decimal fraction between 0 and 1,

with a maximum of three decimals. A probability of 1 means that the expression returns always TRUE.

  Note

You can take a look behind the scenes by simulating a random number expression. Here, you see that even in probability

mode, the expression internally still calculates a random number. However, this number is not used as the expression

result but as an operand of an internal comparison operation: The expression checks whether the calculated number is

less than or equal to the value passed as context to the expression. If so, the expression returns TRUE, otherwise FALSE.

Value Assignment

If you have set the mode of operation to Number, you can choose between the following ways of defining values for the sample

space:

Direct Input

In direct input mode, you define the values for the lower and upper boundaries of the sample space directly. As a

consequence, there is no need for context data objects in this mode. For the system, this static value assignment is easy to

check so that potential errors can already be detected at design time.

Reference

In reference mode, you define the values for the lower and upper boundaries of the sample space indirectly by assigning a

context data object or an expression to each of the boundaries, rather than defining a fixed static value. This dynamic value

assignment gives you more flexibility at runtime. However, it also increases the risk of formal errors (like a minimum value

higher than the maximum value) that can lead to an exception.

Automatic Adjustments

BRFplus helps you defining a random number expression with several checks that are either running in the background or that you

trigger with the Check button:

When you create the expression in number mode, BRFplus automatically assigns the built-in data object NUMBER to it as

the result data object. In most cases, this is exactly what you need since the result of a random number expression is always

a numeric value. However, you are still free to choose a user-defined data object of type number.

If you create the expression in probability mode, the same applies, but with the built-in data object BOOLEAN.

In direct input mode for numbers, the system automatically swaps the values for minimum and maximum if the minimum

value is greater than the maximum value.

More Information

Creating a Random Number Expression

Search Tree Expression

Use

The search tree expression is a non-binary tree structure with conditions and results. It is used for assigning different business-

relevant conditions to different tree branches. The system checks the input and compares it to the conditions defined for each

This is custom documentation. For more information, please visit SAP Help Portal.

91


10/15/26, 3:15 PM

node. Search tree nodes have always a condition assigned, and they can have a result assigned. A condition has to be assigned to

each node, except for the root node. A node can have several child nodes or subnodes. All the subnodes in one level (that is, with

the same parent node) are called sibling nodes. A node without any subnodes assigned is called leaf node.

The search tree searches in a top-down approach, according to the rules of the selected match mode. If the condition assigned to a

search tree node is evaluated as true and the expression is in First Match or Multiple Match mode, the expression returns the

result assigned to the current node.

In Multiple Match mode, the rule evaluation then branches down to the lower subnode and continues the search in a similar

fashion. If the condition node returns false then the search jumps to the next sibling node from left to right. It continues with the

search in this node and its subnodes.

  Note

Due to the sequential processing order of the search tree expression, it is necessary to clearly analyze the use case that you

want to model with the search tree and distribute the conditions properly over the tree nodes. Otherwise, it might happen that a

particular combination of conditions is never tested because of its position inside the tree structure - even if that combination

would result in a match of higher quality.

Features

Mode of Operation

You can decide whether the search tree shall yield a result data object upon an input value matching a node condition, or whether

an action shall be triggered.

Match Mode

The search tree expression supports different modes of operation to control the way how the expression processes a given input

value and decides whether a particular value is matched by one of the tree nodes. You can choose between the following match

modes:

First Match: In First Match mode, the search proceeds until the first node whose condition matches the input value and

returns the corresponding result, if there is one assigned to that node. Any further processing down the tree is stopped.

Multiple Match: In Multiple Match mode, the search is carried out across the entire tree (all levels, all branches). All result

values assigned to nodes whose conditions are evaluated as true are collected during the search and stored in the

expression's result data object. If the condition of a node is evaluated as false, processing continues with the next sibling of

the parent node or the next yet unprocessed branch. This goes on either until the tree has been completely processed or

until a node in the last branch is evaluated as false.

  Note

In Multiple Match mode, the result data object must be of type table.

Qualified Match: In Qualified Match mode, an input value is tested against a chain of semantically independent conditions

associated to the different tree nodes. As opposed to First Match mode, processing does not stop at the first matching

node but continues until a node condition is not met. An input that satisfies best the different conditions in a particular

search tree branch is referred to as a qualified match. The result assigned to the last node of the matching branch is

returned as the expression's result data object.

More Information on Qualified Match Mode

In contrast to many other tree constructs, climbing down the search tree branches does not necessarily mean to start with a

general condition which would then be refined with each level of the tree (for example, "region = EMEA" -> "subregion = Eastern

This is custom documentation. For more information, please visit SAP Help Portal.

92


10/15/26, 3:15 PM

Europe" -> "member of European Community = yes" -> "country = Poland"). Rather, each level can have a condition assigned which

is semantically completely independent from the condition on the previous level (e.g., "region = EMEA" -> "industry = banking" ->

"revenue >= 50 billion Euro" -> "is listed at NYSE" etc.; but this path could as well be defined in reverse order, starting with the

NYSE listing and finishing with EMEA - this only depends on the nature of the business case to be modeled).

Drilling down through such lists of conditions stops at a point where a condition is not met anymore. Once the evaluation has

reached this point, it is correct to say that the current input matches all the different previous conditions up to this point. The

expression then returns the result value (or trigger the action) associated to the last matching node as a qualified match.

Additional Settings

Context Data Object

In contrast to most other expression types, the search tree expression does not have one central context data object. Rather, each

single node of the tree can have a different data object or expression assigned which is used as input value to be tested against the

node condition.

Result Data Object

For the result data object of a search tree expression, the following rules apply:

You have to make sure that all result values used in the tree are type-compatible with the result data object so that the node

result can be properly assigned to the result data object.

In Multiple Match mode, the result data object must be a table data object because in this mode, the result is typically a list

of values.

If the search tree expression is defined to trigger an action rather than returning a result value, the result data object is

automatically set to the predefined Actions table.

Allow Results Only at Leaf Node

With this flag set, the search tree expression only yields a result if all the conditions in a complete tree branch from the root node

down to one of the leaf nodes (with no further subnodes) are satisfied. Setting this flag has the following consequences regarding

the assignment of results to the nodes of the tree:

Nodes that have subnodes must not have a result assigned.

Leaf nodes with no further subnodes must have a result assigned.

Return Initial Value If No Match Is Found

With this flag set, the search tree expression returns the initial value defined for the type of the result data object if none of the

conditions defined in the tree matches the input value. Otherwise, the rule evaluation stops and an exception is raised.

  Note

If you decide to use this option, be very careful that you can make a clear distinction between a well-defined result value that

was returned by a node with a matching condition and the type-specific initial value that was returned as the result of an

unsuccessful rule evaluation. For example, if the result data object of a search tree expression is a data object of type number,

you should make sure that none of the tree nodes carrying a result has the value 0 assigned because for the system it would be

impossible to decide if this is meant as a valid numeric value or as an indicator for a failed rule evaluation.

More Information

Creating a Search Tree Expression

This is custom documentation. For more information, please visit SAP Help Portal.

93


10/15/26, 3:15 PM

Decision Tree Expression

Procedure Call Expression

Definition

A procedure call expression enables the execution of function modules as well as of methods of an ABAP OO class in the backend

system. You can also use this expression directly to execute procedures that are stored in a database.

  Note

The procedure call expression type is the renamed and extended successor expression type of the static method call expression

that was offered in previous releases of BRFplus. The procedure call expression covers the full scope of the former static

method call so that all existing static method call expressions from migrated legacy applications remain fully functional.

However, it is not possible to create new static method call expressions.

Use

You use this expression to take advantage of the full functional power offered by the ABAP programming language when processing

BRFplus business rules. You can do so in order to access routines for data validation, data conversion, or any other kind of data

manipulation regardless of the degree of complexity of such routines.

Values can be passed to the parameters of the called procedure by using a list of parameter mappings that are maintained for the

expression. Once the called procedure has determined a result, it is returned to the result data object of the procedure call

expression.

If the procedure that you want to execute is stored in a database (stored procedure), you can directly access this kind of procedure

without having to define a wrapper method manually in an ABAP OO class . This saves you programming effort and the number of

steps in the execution path is reduced, thereby improving performance.

Features

Supported Procedure Types

You can assign the following types of procedures to a procedure call expression:

Function modules

Methods of ABAP classes

Database procedures

Interface Methods

It is not only possible to assign a class method to a procedure call expression, but also to assign methods of a class interface that

has been implemented by the selected class. To do so, proceed as follows:

1. Choose a class.

2. Select the Use Interface Method checkbox.

The Interface Name entry field is changed to edit mode.

3. To select from the interfaces that are implemented by the class, use the value help.

This is custom documentation. For more information, please visit SAP Help Portal.

94


10/15/26, 3:15 PM

4. To select from the implemented interface methods suitable for the procedure call expression, use the value help in the

Method Name field.

Automatic Filtering of Suitable Methods

When using the BRFplus workbench for modeling a procedure call expression, the system automatically determines which

methods of a given class can be used for the expression at all. Only these suitable methods are then offered for selection using the

value help.

  Example

You can use only methods declared as public and static. However, this type of method is still not sufficiently qualified. For

example, if the method signature contains a mandatory parameter whose type is determined dynamically or defined via

indirection (for example, with theTYPE REF statement), it cannot be used for a procedure call expression because the exact

type of that parameter can only be determined at runtime and is therefore unknown in the modeling environment.

However, if the same parameter is optional rather than mandatory, the method itself can be used for the procedure call

expression. If this is the case, the optional parameter remains unusable and is presented in a list of Unsupported Parameters

that you can check.

You can still enter a method that is not offered by the value help. In this case, using the check function for the expression makes the

system trigger error messages that inform you about the reasons why the method cannot be used. It is then up to you to decide

whether the method can be modified so that the system requirements are met. To see an overview of all methods of the selected

class or interface that are currently not supported for a procedure call, choose Unsupported Methods.

Parameter Mapping

Once you have assigned a method, function module, or database procedure to the expression, the system presents a list of the

method parameters. The list contains all of the parameters that are either mandatory or not and have a type that can be

determined at design time assigned to them. At the same time, this means:

Non-mandatory parameters whose type can only be determined at runtime are omitted because no mapping can be done

for these at design time. These types of parameters are logged in the list of Supported Parameters below.

Mandatory parameters, for which the type can only be determined at runtime, lead to the system qualifying the entire

method as not suitable for the procedure call expression as described above in the Automatic Filtering of Suitable Methods

section.

From the list of parameters, you choose the ones for which you want to provide a value and associate them with a static value

assignment or an expression of the appropriate data type.

Automatic Parameter Mapping

If the method or function module contains any of the following parameters, BRFplus autzomatically maps them to the

corresponding internal BRFplus objects:

Name

Type

IV_TIMESTAMP

IF_FDT_TYPES=>TIMESTAMP

IV_EXPRESSION_ID

IF_FDT_TYPES=>ID

IO_TRACE

REF TO IF_FDT_TRACE

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

95


10/15/26, 3:15 PM

Automatic mapping can be done only if the parameter names and types of the method or function module are exactly the same

as given in the table above. In addition, the importing parameter for the trace object ( IO_TRACE) must be declared as optional.

For the same reason, there is no automatic parameter mapping for an assigned database procedure. This is because the

internal representation of the data types used in the database differs substantially from the data types available in BRFplus. The

system can therefore only offer a technical description of the database type in the parameter's Description field. Automatic

mapping is not supported for procedure call expressions that have a database procedure assigned to them.

The following table lists the supported parameters:

Parameter Type

Import Change

Export

Return

Tables (FM only)

Supported Parameters

'Simple' Type

Yes

Yes

Reference

No

No

NUMERIC

Yes

Yes

ANY TABLE

INDEX TABLE

CLIKE

CSEQUENCE

ANY

HEX

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Other Generic Type

No

No

RAW16

Yes

Yes

Raw Fields

No

No

Database Procedures

Yes

No

Yes

Yes

Yes

Yes

Yes

No

Yes

No

Yes

No

Yes

No

Yes

Yes

Yes

Yes

Yes

No

Yes

No

Yes

No

Only tables

No

N/A

Yes

Yes

N/A

N/A

No

N/A

No

N/A

No

In a procedure call expression, you can directly call a stored procedure that resides in the database. This helps you saving

additional programming effort, as well as improving the performance of database accesses because there are fewer execution

steps.

A procedure is always assigned to one of the various database schemas that may exist in the database. Therefore, a fully qualified

definition of the procedure to be used consists of the procedure's name plus the containing database schema. In the BRFplus

workbench, the value help supports you in retrieving the desired procedure by offering matching procedures across the different

schemas. In other words, although the schema is needed for identifying the database procedure, you don't need to delve too

deeply into the database to find the object you are searching for.

The database where the procedure to be called resides can either be the database that is associated with the system in which you

execute the expression, or it can be a database that runs in a different system within your landscape. In the latter case, you have to

set up a secondary database connection. This can be accomplished in the scope of the application to which the procedure call

expression belongs.

  Note
Procedure call expressions of type Database Procedure are currently supported only for the SAP HANA database.

This is custom documentation. For more information, please visit SAP Help Portal.

96


10/15/26, 3:15 PM

Exception Handling

It is common programming practice to define exception handlers to ensure safe and controlled system behavior if errors occur at

runtime. If a procedure that you have assigned to a BRFplus procedure call expression contains one or more code lines in which an

exception is raised, the system presents these exceptions in the BRFplus workbench. It is then up to you to decide what BRFplus

should do if in case an exception actually occurs at runtime:

Propagated Exceptions

If any of the exceptions in this list occurs at runtime, the corresponding exception instance is propagated to the application

that has called the BRFplus application. The calling application is then responsible for proper exception handling. By default,

the system adds all exceptions that may be raised by a called procedure to this list.

Ignored Exceptions

If any of the exceptions in this list occur at runtime, the corresponding exception instance is not propagated to the

application that has called the BRFplus application. In other words, the exception is suppressed and BRFplus tries to

continue processing as if nothing had happened. In this scenario, it is the responsibility of the BRFplus application designer

to make sure that exceptions are ignored only if this is safe with respect to the processing flow.

  Caution

Whenever a called procedure raises an exception, this means that the processing is aborted immediately. There is no

way to influence this elementary system behavior with the BRFplus exception handling options. From a BRFplus

perspective, this means that the result value of the procedure call expression is initial, and the expression context

remains unchanged.

You control the system behavior by assigning the available exceptions to either of the two lists with the help of the buttons ( Ignore

Exception and Propagate Exception).

More Information

Creating a Static Method Call Expression

Function Call Expression

Table Operation Expression

Definition

The table operation expression provides numerous functions for accessing and maintaining the data stored in a BRFplus data

object of type table.

Use

With this expression type, you can carry out a number of different administrative tasks as well as retrieve statistical data about a

table data object. The available features resemble those offered by the aggregation and existence check modes of the DB lookup

expression, but the scope is slightly different. The following table aims at clarifying the differences between the two expression

types:

Criterion

Table Operation

DB Lookup

Context data object

BRFplus table data object

DDIC table

This is custom documentation. For more information, please visit SAP Help Portal.

97


10/15/26, 3:15 PM

Criterion

Usage

Table Operation

DB Lookup

Business-oriented approach

Database-oriented approach

Access style

read/write (various delete operations

read only

available)

Features

Supported Table Functions

The following table shows the different functions provided by the table operation expression for accessing table data objects:

Name

Has at least

Has exactly

Has not exactly

Has less than

Has more than

Comment

Returns True if the specified table contains at least the given

number of rows matching the given condition.

Returns True if the specified table contains exactly the given

number of rows matching the given condition.

Returns True if the specified table contains either more or less
than the given number of rows matching the given condition.

Returns True if the specified table contains less than the given
number of rows matching the given condition.

Returns True if the specified table contains more than the given

number of rows matching the given condition.

Has no more than

Returns True if the specified table contains no more than the given

Count

Minimum

Maximum

Total

Average

First line

Last line

All lines

Sort

number of rows matching the given condition.

Returns the number of rows matching the given condition in the

specified table.

Returns the lowest value found in the specified table column

matching the given condition.

Returns the highest value found in the specified table column

matching the given condition.

Returns the total of all values found in the specified table column

matching the given condition.

Returns the average of all values found in the specified table

column matching the given condition.

Returns the first row matching the given condition in the specified

table.

Returns the last row matching the given condition in the specified

table.

Returns all rows matching the given condition in the specified table.

Sorts the rows of the specified table by the values in the given

columns and sort order.

This is custom documentation. For more information, please visit SAP Help Portal.

98


10/15/26, 3:15 PM

Name

Delete first line

Delete last line

Delete all lines

Comment

  Note

Unlike most other table operations, the Sort operation does not

return a value. Rather, the sorting is done directly on the table

data object specified in the expression context.

The sorting result is kept in memory only and not permanently

stored in the database.

You can sort a table by a maximum of five different columns.

Removes the first row in the specified table matching the given

condition. The changed table (without the removed row) is returned

as the result.

Removes the last row matching the given condition in the specified

table. The changed table (without the removed row) is returned as

the result.

Removes all rows matching the given condition in the specified

table. The changed table (without the removed rows) is returned as

the result.

  Note
For all operations, it is also possible not to provide a selection condition. In that case, the operation is applied to all the rows in

the specified table.

Of the operations listed above, the following can only be used together with a numeric table field:

Minimum

Maximum

Total

Average

The BRFplus workbench supports you in finding the appropriate columns of a given table by only offering those fields that match

the requirements of a particular operation.

More Information

Data Object

DB Lookup Expression

Value Range Expression

Use

You use value range expressions to check if the value of a test parameter lies within a certain range. The result of a value range

expression is always of type boolean. The expression returns the value as true or false depending on whether the value falls within

the defined range.

This is custom documentation. For more information, please visit SAP Help Portal.

99


10/15/26, 3:15 PM
Structure

Static vs. Dynamic Range Boundaries

Defining fixed boundaries for a range comparison at design time is a good starting point and easy to be done. At runtime, the

system compares the values passed to the expression context with the values defined for the range and returns the appropriate

result. However, in certain use cases it may be necessary to evaluate the range boundaries dynamically, as the following scenario

illustrates.

  Example

For an insurance company, you want to classify the tobacco consumption of a customer. You may define the following value

range expressions for this:

Cigarettes per day = 0

Cigarettes per day between [1..10]

Cigarettes per day between [11..20]

Cigarettes per day between [21..50]

Cigarettes per day greater than [50]

The ranges listed above are ready for insertion into the rows of a decision table where you can assign a classification result to

each degree of tobacco consumption.

However, in the course of time it may turn out that the assumed threshold (> 50) for the highest risk class seems to be

unreliable and must be adapted by taking additional factors into account that influence the risk of physical affection. You can

then decide to redesign the first approach as follows:

For the fourth and fifth of the ranges defined above, replace the static boundary value of 50 by a reference to a formula

expression that dynamically calculates a more reliable value by considering additional influencing factors. For example, smoking

50 cigarettes per day may have different effects depending on a person's age or whether a person lives in the mountains or in

an industrial town, and so on.

With this modification, the threshold between the highest and the second-highest risk class turns from a static value into a

dynamic value, which is more adequate to properly reflect real-world conditions.

Explicit vs. Implicit Ranges

In BRFplus, ranges can be maintained either explicitly by defining a value range expression that can be reused by other objects, or

implicitly by defining the range condition directly inside of a superordinate object where the range is needed. Implicit ranges are

often used, for example, to test the context data passed to a decision table expression.

The decision whether you use explicit or implicit ranges is based on the need for reusability:

If certain value comparisons exist that are typical for your use cases and important for the flow control of your business

processes (for example, clustering of ages, income, product groups, countries, and so on), and if these comparisons are

needed at many different places in your application, you use explicit, reusable value range expressions.

If the comparisons that you want to model are mostly created in an ad-hoc manner and are rarely recurring elsewhere in

your scenarios, it may be more convenient to use implicit ranges, thus accepting the loss of reusability.

Constraints

This is custom documentation. For more information, please visit SAP Help Portal.

100


10/15/26, 3:15 PM

Although theoretically, you can define value range expressions consisting of a virtually infinite number of range comparisons

combined in one expression, there are practical limits to the complexity that the system can handle. This is true regardless of

whether you use explicit or implicit ranges. The following constraints apply:

Backend

In the backend, the system can handle value range expressions that consist of several thousands of comparisons. However,

the higher the complexity, the higher the system workload when it comes to code generation. Under extreme

circumstances, it could even happen that the generated class methods would exceed the maximum code size limit that can

be handled by the ABAP code engine. Therefore, we recommend to limit the maximum value range complexity to

approximately 1000 comparisons per value range expression.

Frontend

Rendering complex value range definitions using ABAP Web Dynpro technology imposes high workload on the system,

especially in terms of high memory consumption. System overload can already occur at a degree of complexity that is

significantly lower compared to the processing capacity of the backend. Therefore, displaying value range definitions in the

UI is limited to a maximum of 99 comparisons per value range expression.

  Note

If you need to define value range expressions with 100 value comparisons or more, you can only accomplish this

programmatically. Due to the frontend limitation, there is no way of interactively defining value ranges with that degree

of complexity in the BRFplus workbench.

Example

In the tariff table for a courier company shown below, the rates are calculated based on the region and weight of the consignment.

In the table, each cell in the weight column can be represented as value range expressions. The cell values become the value range

parameters and the column becomes the test parameter. Each cell in the weight column returns a boolean value depending on the

input and the condition described in the table.

Region

Weight

Asia-Pacific

Less than 10 kg

Tariff

$40

Asia-Pacific

Between 10 kg and 50 kg $55

Asia-Pacific

Above 50 kg

Europe

Europe

Europe

$70

$30

Less than 10 kg

Between 10 kg and 50 kg $45

Above 50 kg

$60

More Information

Creating a Value Range Expression

Comparison Operations

Expression Type

This is custom documentation. For more information, please visit SAP Help Portal.

101


10/15/26, 3:15 PM
Definition

User-defined expression types can be used to enhance the functional scope of BRFplus by features that are not supported by the

built-in expression types.

Concept

BRFplus comes with a number of predefined powerful expression types like decision table, search tree, or formula. While these

predefined expression types cover a broad range of business rule usage scenarios, it can still happen that for a particular use case,

the predefined expression types are not sufficient or not easy to use. To overcome such potential shortcomings, BRFplus offers you

the option of creating your own company-specific expression types completely on your own.

The conceptual approach of user-defined expression types is exactly the same as for the built-in expression types. This means, the

built-in expression types are set up by SAP using exactly the same technical infrastructure that you can make use of for your own

expression types. Therefore, you can expect that your own expression types behave just like the built-in ones in terms of

performance, access control, etc. because they are treated as a horizontal scope extension of the BRFplus concept rather than as a

vertical add-on.

Features

Settings and Objects

With the BRFplus element Expression Type being a completely generic vehicle for any kind of processing behavior whatsoever, it is

necessary for you to provide a set of ABAP OO classes and interfaces that implement the desired system behavior. The following

settings and objects have to be provided for a user-defined expression type:

Name

Action Type

Class

Interface

Status

mandatory

mandatory

mandatory

Query Class

optional

UI Class

optional

Data Exchange Class

optional

Comment

Indicates whether the expression type is

used to perform an action or to return a

result data object.

ABAP OO class used to implement the

business logic of the expression type.

ABAP OO interface used to access the

public methods of the class.

ABAP OO class used to search the BRFplus

database for instances of the expression

type and their attribute values.

ABAP OO class used to access the Web

Dynpro application associated with the

expression type.

ABAP OO class used to define a document

type definition (DTD) and data conversion

routines for XML-based data import and

export related to the expression type.

Transport Objects

For each user-defined expression type in a transportable application, it is normally necessary to define individual transport objects

that take care of collecting all the required parts when it comes to transporting the expression from one system to another. The

required information is stored in the following transport objects:

This is custom documentation. For more information, please visit SAP Help Portal.

102


10/15/26, 3:15 PM

Customizing data (mandatory)

System data (mandatory)

Deployable data (optional)

For the built-in standard expression types shipped by SAP, BRFplus uses the transport objects FDT0000 (Customizing), FDT0001

(system), and FDT0002 (deployment). These transport objects are reserved for the standard expression types. You can only use

them for your own expression types under the following condition: The new expression type must be an exact copy of one of the

standard expression types, with no extensions or changes whatsoever. Such a cloned expression type can be useful if you want to

build your own non-standard UI for an expression type, or if you want to associate the expression type with specialized check

routines that are not part of the standard shipment.

  Note

For a user-defined expression type that does not perform any data manipulation whatsoever, it is not required to assign

transport objects. For example, this would be true for an expression type designed to read some input data and to visualize

them in a graphics control.

If you create user-defined expression types in a local application, there is no need to make any transport object settings.

Consequently, the corresponding tab is not offered in the BRFplus workbench in that case.

For more information about transport objects, see the BC - Central Maintenance and Transport Objects documentation in the

SAP NetWeaver Library on SAP Help Portal.

Actions

Use

Actions can be seen as a special flavor of expression types that you can use to define the interactive part of BRFplus. Under certain

conditions, actions can be used as an alternative to expressions. For example, in a decision table you can define that for a condition

row, the system shall perform an action rather than returning a result value. Here is a list of possible usages for actions:

Action triggered by a rule

Action triggered as a result of a matching condition in a decision table, decision tree, search tree, or case expression

Action triggered as a followup action of another action

However, actions do not have any output. As a consequence, you can only use them as an element for the final step in each

processing branch. Here, an action can be used to respond to the results of the rule calculation so far. But there is no way of, and no

sense in, performing any rule calculations as a response to an action that has been previously triggered.

Depending on the action type, it is still possible to use an action as the trigger for system activities of considerable complexity. This

is true, for example, for action types Workflow or Call Procedure. But still, once an action has been carried out, it is not possible to

define any further processing as a specific response to any kind of changes that may have been made by that action.

Some of the action types correspond to a related expression type. To avoid confusion whether a given object is an action or an

expression, the action type names are all marked by a trailing (Act) in the system. In addition, the action type names follow the

linguistic pattern 'verb - object' (for example, as in Call Procedure (Act), as opposed to the Procedure Call expression type), where

possible.

BRFplus supports the following action types:

This is custom documentation. For more information, please visit SAP Help Portal.

103


10/15/26, 3:15 PM

Call Procedure Action

Log Message Action

Send Email Action

Start Workflow Action

Workflow Event Action

More Information

Creating Action Types

Call Procedure Action

Use

A Call Procedure action allows the execution of function modules as well as of methods of an ABAP OO class in the backend

system. This action type is functionally equivalent to the procedure call expression, with only the following object type-related

differences:

Like all action types, the Call Procedure action does not return any result data.

Like all action types, you can define followup actions that are automatically triggered after the Call Procedure action has

been executed.

More Information

Procedure Call Expression

Log Message Action

Use

With a log message action, you can define system messages that the system writes into the application log during rule processing

under certain circumstances. This can be useful for documenting the flow of processing in an application, and may even be legally

required for auditing purposes, depending on your business case, region, and legislation.

Whether messages shall be logged at all, and if so, to what extent, depends largely on the respective settings for the application

object to which a log message action belongs. All of these settings on application level are inherited by the log message actions. It

is also on application level where you can define whether the default settings for log handling may be individually adapted by an

action, or whether these settings represent a fixed guidance that must be followed.

  Note

You can use report FDT_DEPLOYMENT_LOG to analyze the application logs of BRFplus.

Features

The following table lists the features related to the logging details:

This is custom documentation. For more information, please visit SAP Help Portal.

104


10/15/26, 3:15 PM

Setting

Comment

Application Log Object, Application Log Sub Object

Defines the application log objects used for recording the log

entries that are created by objects belonging to the application (for

example, actions of type Log Message). For more information, see

the Application Log Guidelines for Developers (BC-SRV-BAL)

documentation in the SAP NetWeaver Library on SAP Help Portal.

Defines whether an additional tag shall be added to the log entries,

and if so, how this shall be accomplished. You can choose from the

following options:

None

No external identification is written to the log.

Free Text Input

Enter any text string that may help you identify the relevant

log entries. The maximum length is 100 characters.

By Reference Object

Assign a data object or expression to the action. At runtime,

the value of this reference object is written to the log when

the action is triggered.

Controls whether the log data shall be permanently stored in the

database or not. If not, log data is only kept in memory during

runtime and is lost after the session.

External Identification Mode

Persist

Messages

Number of Messages

In the Log Messages area, you define which messages shall be written to the log when the action is triggered. You can assign any

number of messages to each log message action.

Free Text versus Message Reuse

You can decide either to enter a free message text or to make use of any of the messages that already exist in the system. If you

use an existing message, you have to enter the message class and number. Also, if the message contains parameters, the

workbench prompts you to provide values for these parameters. Here, you can choose again between either providing a freely

defined text for the parameter, or to assign a data object or expression that is evaluated at runtime.

Message Type

Regardless of whether you define a free text message or reuse an existing message, you must define the message type. The

following message types are available:

Abort

Error

Exit

Information

Status

This is custom documentation. For more information, please visit SAP Help Portal.

105


10/15/26, 3:15 PM

Warning

  Note

Should any of the message types listed above not be available for an action, this is due to a message type restriction that has

been defined on application level.

More Information

Application

Send Email Action

Use

You use the Send Email action to notify a person about a particular situation in the system. It is then up to the person who receives

the mail to decide whether specific measures have to be taken to cope with the situation. The situation itself may be critical or not,

depending on what you think is useful for your business. It is always a good idea to notify a responsible person when a critical

situation occurs. However, there may also be situations or activities that do not indicate a problem but simply occur infrequently

and on an irregular basis. Here, an automatic notification sent to you by the system helps you to get rid of routine checks and lets

you spend your time on more useful tasks.

Prerequisites

The SAPconnect component (BC-SRV-COM) has been set up for internet services. You must create an appropriate node in the

SAPconnect administration and enter an RFC destination of the type TCP/IP connection with which you establish a connection to a

mail server. For more information, see the SAPconnect (BC-SRV-COM) documentation in the SAP NetWeaver Library on SAP Help

Portal.

Features

General

You use the Send Email action to enable the system to send an email with a predefined text using the standard SMTP protocol. This

is useful when your rule processing flow contains points at which critical situations that need user experience may arise. The same

holds for workflow scenarios in which different workflow agents are assigned and processing can only continue after a specific role

owner has taken the necessary action.

Recipients

You can either enter a static email address or use expression to determine the recipient dynamically. You can also combine both

ways of addressing recipients in the same action. This enables you to make sure that a particular person is always notified (for

example, the quality manager), as well as the person who is currently in charge of reacting to the notification (for example, the

responsible employee in the current shift of a three-shift operation company).

You can enter any number of static email addresses into the Direct Email entry field, separated by semicolons. Note that you may

enter a string of addresses that exceeds the visible length of the entry field.

If you choose to let the recipients be determined dynamically, make sure that you choose an expression, a constant, or a context

data object of the text type. The string returned by the chosen object must follow the same syntactic rules as in the To field. You

can define up to four different expressions for recipient determination in one action.

This is custom documentation. For more information, please visit SAP Help Portal.

106


10/15/26, 3:15 PM

  Note

If you have to send different emails to a distribution list, you can model this use case by assigning a table data object as a

dynamic recipient that has previously been filled with the email addresses. To accomplish this, make sure that the table

structure consists of only one text field to hold one address per entry. You can, for example, fill the table data object with the

help of a decision table expression in multiple match mode.

Mail Body

In the Body field, you can, again, enter either a predefined static text, a text that is dynamically put together at runtime with the

help of message placeholders, or a combination of both. You may define up to eight placeholders per Send Email action, each of

which may be replaced at runtime by a constant, the result of an expression, or an elementary context data object.

Example

In the ruleset that you use to manage customer requests for an insurance contract, you differentiate between standard incoming

requests and other requests that need special handling for a variety of reasons, such as:

Unusually high insurance amount

Requestor is located in a different country

Inconsistent request form data

All of these reasons would have to be considered as exceptions to the standard request handling and need intervention. To

accomplish this, you create an additional processing path in the ruleset in which a Send Email action is triggered. In this action, you

enter a predefined text describing the issue and enrich this text with dynamic content such as the contract request ID or the

requested insurance amount, both taken from the ruleset context. You can also use an expression to determine the employee in

your company who is currently in charge of resolving issues of the type in question and assign this employee as the email recipient.

Start Workflow Action

Use

With a Start Workflow action, you can integrate workflow processing into BRFplus. You can access each of the workflows that have

been defined in the backend system, assign it to a Start Workflow action and let the system perform the predefined steps once the

action is triggered by a BRFplus expression.

For a discussion of the differences between the Start Workflow action and the workflow event action, see Workflow Event Action.

Prerequisites

Your backend system contains software component SAP_BASIS with a release lower than 800. In SAP_BASIS 800 or higher, the

underlying workflow functionality of this action type is not supported.

You have created a workflow definition with the Workflow Builder (transaction SWDD) in the backend system.

Features

After having entered the desired workflow ID, click Update Workflow Container. The system analyzes all the data dictionary

elements that are used in the workflow definition. For each of these data dictionary elements, the system automatically creates a

BRFplus data object in the current application and defines a binding relationship to the corresponding element.

This is custom documentation. For more information, please visit SAP Help Portal.

107


10/15/26, 3:15 PM

You can provide input data to all of the workflow container elements. Depending on the element, you can either directly enter a

value or insert a reference to a context data element or an expression that is evaluated dynamically at runtime.

In case of complex container elements (structure or table), you can provide the data for such elements by assigning a decision

table expression as input source for such elements. Each of the structure or table fields would have to be covered by a

corresponding result data object of the decision table. With the help of additional context data objects for the decision table, you

can control which of the predefined results shall be used for populating the workflow container.

You can define that the workflow shall not start immediately after the Start Workflow action has been triggered. Rather, you can

define an execution delay of up to 9999 days, 23 hours, 59 minutes, and 59 seconds.

  Note

When you check or activate a Start Workflow action, the system does not only check whether the BRFplus-specific settings are

correct. Moreover, it also detects any inconsistent or incomplete settings that must be corrected in the definition of the

underlying workflow definition, for example, a missing assignment of workflow agents.

Example

You are running an application designed for managing insurance contracts for household belongings. While the major factor for

calculating the insurance rate is the value of the household belongings, your application contains a value-dependent discriminator

that ensures that contract values exceeding a certain threshold cannot be entered in the system directly. Rather, with an initial case

expression, the system separates the allowed values from the exceeding ones. While the allowed values are immediately passed

over to a decision table used for the value/rate assignment, the contract values exceeding the threshold are sorted into a

processing branch where a Start Workflow action is triggered. This workflow is defined such that additional approval steps have to

be performed first before the contract can be further processed. With this scenario, you can make sure that the appropriate risk

mitigation steps are taken to protect your company from having to pay amounts insured that are not covered by your company's

overall risk calculation.

Integrating BRFplus into an existing workflow

Both workflow-related action types offered by BRFplus take a BRFplus rule application as the starting point from which you may
decide to make use of the SAP Business Workflow functionality. However, it is also possible to turn this scenario and start from the
other side. That is,you already have a workflow implemented and want to enhance it by calling a particular BRFplus function. If you
are interested in this usage scenario, please refer to the "Integration between SAP Business Workflow and BRFplus" whitepaper on
the BRFplus pages of the SAP Community Network (see Related Links section below).

More Information

Workflow Event Action

Data Binding

Decision Table Expression

See also the SAP Business Workflow: Reference Documentation in the SAP NetWeaver Library on SAP Help Portal.

Related Information

Integration between SAP Business Workflow and BRFplus

Workflow Event Action

This is custom documentation. For more information, please visit SAP Help Portal.

108


10/15/26, 3:15 PM
Use

With a workflow event action, you can integrate workflow processing into BRFplus. In contrast to a Start Workflow action, you do

not have to specify a particular workflow to be triggered. Rather, you specify an event that has been defined for an object in the

backend system. Whenever the event is raised, all the workflows that have been registered for that event are triggered.

Prerequisites

Your backend system contains software component SAP_BASIS with a release lower than 800. In SAP_BASIS 800 or higher, the

underlying workflow functionality of this action type is not supported.

Features

General

BRFplus supports the following types of objects that you can use for referring to an event:

ABAP Objects Class ( CL)

Business Class ( BC)

Business Object (BOR object; BO)

After having entered the required event details, click Update Event Container. The system analyzes all the data dictionary

elements that are used as event parameters. For each of these data dictionary elements, the system automatically creates a

BRFplus data object in the current application and defines a binding relationship to the corresponding dictionary element.

Once the event container has been populated with the parameter fields, you can define the values to be passed to the event.

Depending on the parameter type, you can accomplish this by either directly entering a value or by assigning an expression that is

evaluated at runtime.

ABAP Objects Class

For events defined in classes of type ABAP Objects as well as of type Business Class, it is required that the class implements the

IF_WORKFLOW interface. If you use the value help (  F4 ) to search for classes, the system automatically restricts the search

results to classes that meet this requirement.

All parameters of an event you want to use must have a direct, explicit type definition. That is, the type definition must refer to a

type that exists in the data dictionary. If at least one event parameter has an indirect type assignment (for example, realized by the

TYPE REF or LIKE statement), the event cannot be used for the workflow event action.

Object Instance ID

At runtime, events are raised by an instance of the given class or business object. For a class, you can identify this instance by its

local persistent object reference (LPOR). A business object (BO) instance can be identified via the business object key. For a

BRFplus workflow event action, the LPOR or BO key must be passed to the Object Instance ID field at runtime. You can accomplish

this by either passing the respective value to the action via a context data object or by evaluating an expression. It is up to the

calling application to pass the relevant instance ID to the called function's context.

Comparison of Workflow Event Action and Start Workflow Action

The main differences between the workflow event action type and the Start Workflow action type are the following:

A Start Workflow action has always exactly one workflow assigned, and the assignment is part of the action's definition. In

contrast to this, a workflow event action can have any number of registered workflows (including zero) that listen for the

This is custom documentation. For more information, please visit SAP Help Portal.

109


10/15/26, 3:15 PM

event that has been defined in the action.

As a consequence of the statement above, triggering a workflow event action does not guarantee that any workflow is

started at all in response to the action. If there is no workflow event handler listening to the action's event, nothing will

happen.

Unlike the Start Workflow action, the workflow event action provides no way to see which workflow exactly will be triggered

by the action. This is determined by the fact that a particular workflow instance has been registered for the event in

question. The workflow event handler permanently listens to the events that are raised in the system. As soon as a

registered event is raised, the workflow starts.

Business Class, Business Object

These constructs refer to older class concepts found in SAP systems. BRFplus supports these legacy class types for compatibility

reasons. We do not recommend to create new classes of this kind.

Integrating BRFplus into an existing workflow

Both workflow-related action types offered by BRFplus take a BRFplus rule application as the starting point from which you may
decide to make use of the SAP Business Workflow functionality. However, it is also possible to turn this scenario and start from the
other side. That is,you already have a workflow implemented and want to enhance it by calling a particular BRFplus function. If you
are interested in this usage scenario, please refer to the "Integration between SAP Business Workflow and BRFplus" whitepaper on
the BRFplus pages of the SAP Community Network (see Related Information section below).

More Information

Start Workflow action

Data Binding

See also the SAP Business Workflow: Reference Documentation in the SAP NetWeaver Library on SAP Help Portal.

Related Information

Integration between SAP Business Workflow and BRFplus

Function

Use

A function is the rule interface in BRFplus and acts as a link between the application code and the BRFplus code. For your

convenience, you can let the system generate an ABAP code snippet that you can use for easy integration of a BRFplus function

into your application.

A function carries a context and a result. It imports the context from the calling application and passes the context data to the

assigned top expression or ruleset for further processing. After processing, the function returns the calculated result to the calling

application.

Features

Mode of Operation

A function can be designed for one of the following modes of operation:

This is custom documentation. For more information, please visit SAP Help Portal.

110


10/15/26, 3:15 PM

Functional Mode

In functional mode, function execution starts with the assigned top expression. From this top expression, the processing

may run through any number of nested subexpressions until a result is returned.

Event Mode

In event mode, the function is associated with a list of rulesets that are executed according to their execution priority and

their position in the list.

Functional and Event Mode

This mode is a combination of the modes mentioned above. At runtime, the function starts processing the assigned top

expression. Once the expression evaluation is finished, function execution continuous with the associated rulesets.

For more information, see Modes of Operation.

Signature

The function signature consists of two parts:

Context

The context is a container for data objects that you can assign as import parameters for the function. You choose the

context data objects of a function according to the requirements of the calling application by which the BRFplus function is

invoked. Also, the context data objects of a function define the scope of objects that can be accessed by the expressions

that are evaluated during function execution.

Result

The result data object returns a result value that has been calculated by the expressions of which the function consists.

  Note

For functions in event mode, the result data object is automatically set to the predefined Actions table where the

actions are recorded that have been triggered by the assigned rulesets.

Rulesets

For a function where you have set the mode of operation to either Event Mode or Functional and Event Mode on the Properties

tab, the system expects that you assign one or more rulesets that are processed when the function is processed. You can create a

new ruleset to be assigned to a function directly from the editing work area of a function. For an already existing ruleset, however,

you first have to navigate to that ruleset and define the desired function as the ruleset's trigger. Once this assignment has been

made, the ruleset is listed on the Assigned Rulesets tab of the function.

  Note

When you execute a function that triggers more than one ruleset, the system starts by executing the first ruleset and waits for

its termination before it starts the execution of the next ruleset, and so on. This is a prerequisite for the system to be able to

pass parameters that may have been modified by a ruleset from one ruleset to another. There is no parallel processing of the

assigned rulesets. Also, there is no way for an assigned ruleset to prevent the execution of a subsequent ruleset once the

function has been started.

Assigned Rulesets versus Executable Rulesets

In the BRFplus workbench, you can choose between two different view modes with respect to rulesets:

Assigned Rulesets

This is custom documentation. For more information, please visit SAP Help Portal.

111


10/15/26, 3:15 PM

In this mode, the system displays all rulesets that have been assigned to the current function, regardless of their activation

status. This means that there may be one or more rulesets listed that are currently not ready for execution and will be

skipped without further notice when the function is triggered. Also, choosing this view mode enables the Create Ruleset

button that you can use to create a new ruleset and assign it to the current function in one single step.

Executable Rulesets

In this mode, the system displays only those rulesets that have been assigned to the current function and are either

currently active or for which an older active version is available that can be used for ruleset execution.

  Note
The system lists all assigned rulesets that are executable from a technical point of view. Therefore, a ruleset that is

currently disabled is still listed as long as there is an active version available. As opposed to the activation status,

enabling or disabling a ruleset is a business-driven decision, not a technical question. At runtime, the function triggers all

executable rulesets. However, a disabled ruleset terminates immediately without taking any actions, and returns control

to the trigger function.

Ruleset Execution Priority

In case there is more than one ruleset assigned to a function, the rulesets are triggered according to the order in which they appear

in the function's list of assigned rulesets. You can influence the execution order for the rulesets by defining a priority for each

involved ruleset. The priority is a numeric value between 0 and 99 that you can define for a ruleset. The default priority for a newly

created ruleset is 0, meaning that there is no priority defined for that ruleset. The list of assigned rulesets is sorted by that priority

in ascending order so that the ruleset with the lowest priority value is executed first, followed by the ruleset with the second-lowest

priority, and so on.

You set the ruleset execution priority in the ruleset maintenance screen of the BRFplus workbench. To accomplish this, enter the

desired value as Priority in the Detail section.

  Note

In contrast to the general rule outlined above (lower priority number means higher priority), the system treats the default value

0 differently. A priority of 0 means that there is no priority at all for such a ruleset. In other words, a ruleset with priority 0 is

triggered only after all other rulesets of the same function that have a priority > 0 assigned have been executed. The system

gives you a visual hint for that by displaying "undefined" in the priority column for a ruleset with priority level 0, whereas for all

other priority levels, the numeric value is displayed.

Dependencies, Cardinality, and Visibility

The relationship between a function and its assigned rulesets is not absolutely obvious at first glance. For a better understanding

of the underlying concept, keep the following in mind:

Function and ruleset are modeled in a 1:n relationship. That is, one function can have any number of rulesets assigned,

whereas a ruleset can only be triggered by exactly one function.

The relationship between function and ruleset is established from the ruleset's perspective, not vice versa. As a

consequence, the system keeps track of which function is assigned to a particular ruleset, but not the other way round. This

means that a function does not know the rulesets for which it is assigned as a trigger. This is true although the assigned

rulesets of a function are listed in the BRFplus workbench for a function.

The one-way perspective from ruleset to function is also reflected in the following aspects of the system behavior:

If a function has been assigned to one or more rulesets as a trigger, these rulesets are shown in the where-used list

of the function, but not in the Uses section of the repository tree in the BRFplus workbench.

This is custom documentation. For more information, please visit SAP Help Portal.

112


10/15/26, 3:15 PM

When you activate a function and request that also the subordinate objects of the function are activated if

necessary, this recursive activation does not touch any rulesets for which the function may have been assigned as a

trigger.

The same applies for all other activities related to a function that can be carried out recursively, like copying or

checking a function. Here, too, any rulesets to which the function may be assigned are not taken into account.

Code Generation

BRFplus provides a built-in code generation facility used to compile source code for as many rule constructs in a function as

possible. With the help of generated code, BRFplus rules can be executed significantly faster than in interpretation mode.

Simulation

You can simulate the function processing to test the function's behavior in a sandbox environment. Here, you can gain an in-depth

insight into the system status for every single step the system takes during function processing.

Trace

In BRFplus, you can request the system to create a processing log to keep track of all processing steps during function execution.

The trace information is stored in the system and can be reviewed at any point in time.

Generation Services

For a BRFplus function, you can take advantage of different services that automatically generate code and other objects that are

needed to bridge the gap between the ABAP backend system where a BRFplus function is hosted and other systems or

environments that wish to access BRFplus. The different services available address different usage scenarios. These can be

categorized as follows:

Code Templates

A code template is a predefined snippet of ABAP code that you can use to call a BRFplus function from your application in

the same system.

Function Module

You can use a generated RFC-enabled function module to call a BRFplus function that resides in a remote backend system.

This is useful in cases where you cannot bring BRFplus and the calling application into the same system - be it for technical

reasons (for example, different releases) or for organizational reasons (for example, missing authorization to develop in the

remote system).

Web Service

You can use a generated web service to call a BRFplus function from a web application that is not ABAP-based, or that you

can only integrate via its exposed services interface. From a technical point of view, web service generation is reusing the

function module generation component of BRFplus and generates additional system objects needed for service

enablement.

Code Templates

BRFplus comes with predefined code templates that you can use to let the system generate an ABAP code snippet. After having

made some minor adaptations to this snippet, you can copy and paste it into the code section of your application from where you

want to invoke BRFplus rule execution. You can choose whether the function is called with or without trace information, and you

can decide whether the explanatory in-line comments are visible in the code or not.

Web Service and Function Module Support

This is custom documentation. For more information, please visit SAP Help Portal.

113


10/15/26, 3:15 PM

For function invocation, BRFplus supports the generation of web services as well as of RFC-enabled function modules. This enables

you to integrate the rule execution power of a BRFplus function into a service-oriented software environment, or into a remote

ABAP system calling BRFplus via RFC (Remote Function Call).

Advanced Checks

In addition to the standard consistency checks that are available for each BRFplus object via the Check button, the system offers

additional checks for functions:

Assigned Rulesets

With this check, the system analyses the correctness and consistency of all the rulesets that are assigned to a function.

This check is only available for functions running in Event Mode or Functional and Event Mode.

Unversioned Objects

With this check, the system drills down through the hierarchy of all objects assigned to a function and determines whether

there are any objects for which versioning has not been switched on.

Inactive Objects

With this check, the system drills down through the hierarchy of all objects assigned to an activated function and

determines whether there are any objects that are currently inactive. For each inactive object, the system sends a

corresponding message to help you analyze the object. However, due to technical restrictions of the system architecture, it

may sometimes be impossible to present the complete path to the inactive object in the message. In such a case, you have

to look up the respective object manually.

  Note

According to the cascading activation strategy of BRFplus objects, a situation where an active object is using an inactive

object can normally not occur. However, the following scenarios are valid and can lead to this kind of situation:

An active function run in functional mode uses an active top expression (or any of its dependent objects) that is

changed and deactivated at a later point in time. Here, the function remains active. When the function is

processed, it uses the last active version of the top expression, not the latest inactive version. In this scenario,

reactivating the function solves the issue.

An active function run in event mode has been assigned to an inactive ruleset. Here, the BRFplus activation

strategy cannot directly detect the problem because the relationship between functions and ruleset is internally

modeled such that only a ruleset knows its assigned function, whereas a function is not aware of its assigned

rulesets. As a consequence, reactivating the function does not solve the issue. Rather, you have to activate all

assigned rulesets.

This check is especially helpful if rule modeling is set up as a shared task with several involved persons with different

responsibilities. In this kind of working scenario, it can easily happen that changes to dependent objects are made that are

not brought to your attention. The Inactive Objects check lets you keep track of such unexpected changes.

More Information

Modes of Operation

Building Functions

Generating Web Services and Function Modules

Expressions

This is custom documentation. For more information, please visit SAP Help Portal.

114


10/15/26, 3:15 PM

Ruleset

Tracing

Versioning

Modes of Operation

Use

BRFplus provides three modes of operation for processing a function: Functional mode, Event mode and Functional and Event

Mode. The different modes have the following characteristics:

Functional Mode

Functional mode requires a top expression to be assigned to the function. During processing, the function triggers and

evaluates the top expression. The top expression may use a number of nested expressions to find a result. The result of the

top expression is the result generated for the function. For example, a decision table can be assigned as a top expression to

a function. The context data objects are used as input for those columns of the decision table that are used for formulating

the conditions. As a result, the decision table nests a formula expression. The result of the decision table is returned as the

function result. Typically, the functional mode is used for more simple use cases with a clear output of the function.

Event Mode

Event mode uses rulesets to trigger processing instead of a top expression. A function can have numerous rulesets

assigned. Each ruleset contains a number of rules. A rule consists of a condition and an action part. These rules with

additional restrictions determined by preconditions, time dependency, enabled/disabled status are triggered when the

function is processed. If a rule condition is satisfied, the action is processed. An action can simply change the values in the

context or initiate additional activities, such as starting a workflow or writing error messages to a log. All the actions that are

performed while the function is executed are collected in the predefined Actions table that is automatically used as the

function's result data object in event mode.

Rulesets may also contain other expressions such as decision table or formula expressions. Typically, event mode is used

for more complex use cases and for use cases where a result is not needed.

Functional and Event Mode

Functional and Event mode is a combination of functional mode and event mode. As with functional mode, assigning a top

expression and a result data object is mandatory. In addition, rulesets can be processed so that actions can be performed,

thereby possibly changing the context. At runtime, the function starts processing the assigned top expression. Once the

expression evaluation is finished, function execution continuous with the associated rulesets.

More Information

Function

Rule Set

Tracing

Use

This is custom documentation. For more information, please visit SAP Help Portal.

115


10/15/26, 3:15 PM

In BRFplus, you can request the system to create a processing log to keep track of all processing steps during function execution.

The trace information is stored in the system and can be reviewed at any point in time. The trace functionality follows an approach

of only writing a minimum of data to the system. This is accomplished by logging object references and data changes rather than

explicitly writing down all available information about a given object at a certain point in time. This strategy keeps the database

small and reduces performance decreases. You can control the trace functionality with the help of the IV_TRACE_MODE

parameter of method IF_FDT_FUNCTION~PROCESS.

The trace tool is also used by the simulation tool that is available for functions, expressions, and actions. Here, the trace contains

all the processing steps that the system performs for the given parameters in a simulation run.

Prerequisites

One of the following prerequisites must be fulfilled:

All objects to be traced are versioned.

If not all objects to be traced are versioned: The timestamp of all objects in a trace is equal or older than the timestamp of

the trace itself.

For more information, see the Trace and Versioning section below.

Features

Lean Trace versus Technical Trace

You can decide to which degree of detail information shall be logged by the system. The following alternatives are available:

No trace

If the calling application does not request any sort of trace for a function, the system simply executes the function, and

returns the calculated result. None of the processing steps are logged. This leads, of course, to the best performance

results.

Lean trace

In lean trace mode, the system records only those steps of the process flow that directly lead to the end of the process. For

example, if the program contains a CASE statement where an input value can be tested against five different values and

only the last attempt leads to a matching result, then lean trace does not mention the four unsuccessful attempts but only

the fifth one.

Technical trace

As opposed to lean trace, the technical trace records each single step of the process flow, regardless of whether a step

contributes to the successful completion of the processing or not. If, for example, a routine walks through 20 different steps

until it finally turns out that this was the wrong path, the technical trace would make this visible, while lean trace would hide

these steps from the user.

Trace and Versioning

The strategy of writing only a minimum of trace data requires that all BRFplus objects that are involved in the traced function must

be versioned. Otherwise, the system could not identify the involved objects properly. This would lead to errors when the trace data

is displayed. The versioning requirement is relaxed only under one special condition: If all objects involved in a trace have not been

changed since the trace was recorded, then the system is still able to evaluate and display the trace. Otherwise, the system

displays an error message when you try to access the trace.

This is custom documentation. For more information, please visit SAP Help Portal.

116


10/15/26, 3:15 PM

When a function is called with the request for logging trace data, but with objects involved that are not versioned, the system

behavior depends on the setting of the IV_TRACE_MODE parameter of method IF_FDT_FUNCTION~PROCESS:

L (for L ean Trace)

The system executes the function in interpretation mode. Code generation is not possible in this situation.

R (for Lean Trace R equired)

The system does not execute the function and raises an exception. This is due to the conflict of a function that cannot be

traced and, at the same time, is required to be traced. This conflict cannot be resolved, so execution stops here.

In addition to the parameter values mentioned above, the IV_TRACE_MODE parameter can also hold the following values:

T (for T echnical Trace)

With this parameter value, the system writes a verbose and complete log while the function is being executed. The technical

trace contains information about every processing step of the function, including all the steps that do not directly lead to

the successful completion of the processing. This trace mode is mainly intended for code analysis and debugging. It is not

recommended for productive use due to performance reasons.

"" (empty)

If no value is passed to the parameter, this indicates that no trace information shall be written while the function is

executed.

Constraints

In certain use cases, information to be recorded in the trace is passed to the trace dynamically via parameters. For technical

reasons, this can lead to trace lines where the information provided exceeds the maximum line length and therefore must be

truncated. However, if you look at the trace in the context of the function simulation tool, the complete information is available by

hovering the mouse over the truncated line. Here, the untruncated information is given in the tooltip.

More Information

Versioning

Simulation

Simulation

Use

Simulating the processing of a function, expression, or action is useful to test the object's behavior in a sandbox environment.

Here, you can gain an in-depth insight into the system status for every single step the system takes during function processing.

  Note
Although simulation is a tool that lets you easily test the object behavior, the object to be run in simulation mode must have

been saved before. Changes to an object that you have only made on the fly without saving are not reflected in simulation mode.

Prerequisites

This is custom documentation. For more information, please visit SAP Help Portal.

117


10/15/26, 3:15 PM

The function and all of its referenced objects (both direct and indirect) are active, or there is at least an older active version

available in the system (prerequisite valid only for simulation in generation mode).

Features

Simulation Mode

The simulation tool offers the following modes of operation:

Interpretation Mode

In this mode, the system uses the objects involved in the simulation by drilling down through their design-time definition.

For a quick one-time simulation run, this can be faster than using generation mode. Direct simulation of expressions or

actions (that is, without being assigned to a function) is supported only in interpretation mode.

Generation Mode

In this mode, if there is no source code available for the function, the system first generates source code for the objects

involved in the simulation when you click Execute. This leads to a short execution delay because of the time needed for the

generation of classes and methods. However, using generation mode has the following advantages over interpretation

mode:

Executing generated code is much faster than interpreting the structure of the objects involved every time the

simulation is run. Especially if you want to simulate a function that is the entry point to a very complex structure of

rulesets and expressions, or if you need to simulate a function in many iterations with different test data, it is usually

recommendable to use generation mode rather than interpretation mode.

Moreover, code generation is only necessary if any of the involved objects has been changed since the last time code

was generated. If no changes have been made, the system immediately loads and executes the source code that is

already available, thereby further accelerating execution.

In generation mode, simulating a function is done in exactly the same way as the system executes the function in a

live system at runtime. Therefore, generation mode gives you an exact preview of the function's live behavior in

terms of performance or potential problems.

  Note

Generation mode can only be used with functions, not with expressions or actions. Also, only functions that are currently

active or for which an active version exists can be simulated in generation mode.

Action Settings

When you perform a simulation, it is normal that you want to investigate the system behavior without causing any effects that

could interfere with productive business processes. Running a simulation as an isolated process is relatively secure as long as

there are only expressions and rules to be simulated. As opposed to that, things can be different if during the simulation, actions

are triggered. Actions can trigger system activities that go beyond the boundaries of BRFplus and may have a significant impact on

current business processes. For example, under normal circumstances you would not want a simulation to send real emails to real

persons, or to start a system workflow.

Because triggering actions can have these unwanted side effects, actions are by default only partially executed during a simulation

run, thereby bypassing all business-critical steps. However, if you need to know whether a triggered action is working properly, you

can force the system to trigger actions during simulation by setting the Execute Actions flag.

  Note
To avoid any misconceptions, here is a more detailed explanation of what the Execute Actions flag does internally and what not:

This is custom documentation. For more information, please visit SAP Help Portal.

118


10/15/26, 3:15 PM

From a technical perspective, actions that are part of the execution path of any function, expression, or superordinate

action to be simulated are always executed. This is true regardless of the setting of the Execute Actions flag. As a

consequence, actions are always shown in the detailed simulation log. Also, if you are debugging a simulation session,

you will realize that the system actually processes the code related to an action.

However, with the Execute Actions flag set to false, the system processes the code related to an action but, unlike

normal processing, does not commit the pending changes or activities defined for the action before exiting the action-

related source code. With this execution strategy, you can check the system behavior during simulation to the largest

possible extent, but still without having to care for any unwanted side effects as outlined above.

Object Types

The simulation functionality is basically a feature offered for BRFplus functions. However, you can also directly simulate a particular

expression or action without having to assign it to a function first. This makes it easier for you to quickly check the runtime

behavior of your expressions.

  Note

From the system's perspective, simulation is always done for a function. This is true even if you choose to directly simulate an

expression or an action. In that case, the system automatically creates a temporary function in the background, assigns the

expression or action to it, and then simulates the temporary function.

Version

If the object that you want to run in simulation mode is under version control, the system lets you decide which of the available

versions should be simulated. You can choose from the following options:

Last Active Version

With this option, the system checks the version list of the object for the most current version that has been activated,

starting with the current version and then moving back to the past. If the object has never been activated (or if there once

was an active version that has been deleted in the course of time), starting the simulation with this option will raise an error

message. This option is the version default for simulation runs.

Latest Version (Inactive)

With this option, the system uses the most recent version of the object for the simulation, even if it is currently inactive. This

allows you to check the effects of a change even in a productive system without endangering the correctness of rule

processing for real business transactions. It is up to you to decide whether the simulated behavior should be made

productive or not: If yes, activate the object; if not, revert the object to its previous active version (or simply leave the

changed object without saving). This option is only available for objects whose current version is not active.

As of Date/Time

With this option, you can define a point in time for which you want to simulate how the runtime behavior of the object in

question would have been at that time. The system compares the given date and time with the time stamps of the object

versions that have been stored in the database. The system looks up the next available active version of the object that has

been activated earlier than the given date and time. If such a version exists, it is used for the simulation. Otherwise, the

system raises an error message. This option is only available for objects for which versioning is set on.

Context Data

For simulating a function or expression, the system offers two different ways of passing values to the context data objects of the

object to simulate:

Manual Data Entry

This is custom documentation. For more information, please visit SAP Help Portal.

119


10/15/26, 3:15 PM

In this mode, the system offers you an entry field for each context data object (broken down to each data object's elementary

constituents). Once you have entered the desired values, you can execute the simulation and check the result.

Test Data Import

In this mode, you can import test data for the simulation that have already been collected in an external spreadsheet file. This is

helpful for the following reasons:

If you have a complex scenario with a wide variety of different input data, using a spreadsheet can help you to automatically

generate the necessary test data. This takes away the burden from you of having to enter endless lines and columns of data,

which can be both tedious as well as error-prone.

Executing the simulation in batch mode for all records in the import data file produces a result file where you can find the

calculated result for each combination of input data. This result file can serve not only as a simulation log but also as a

means of process documentation that helps you to prove which context data records have already been tested in the

simulation.

If you want to use the test data import for the first time for a particular function or expression, we recommend that you start using

the Create Import Field Structure function first. With that, the system creates a spreadsheet file that reflects the structure of the

context data exactly as it is expected by the import function. You can then populate this export file with test data and finally import

the data for simulation.

Once you have your test data ready for import into the simulation, there are two approaches for processing the data:

Single data processing: With this approach, you select always one of the imported test data records per simulation run. You

can then choose between the simple Execute option (only the result is displayed after simulation execution) or the detailed

Execute and Display Processing Steps option (a detailed log of all the calculation steps is displayed). Note that both

options are only available if there is no more than one record selected for the simulation.

Batch processing: With this approach, you can select any number of the imported test data records and let the system do a

simulation for each of them. To accomplish this, proceed as follows:

1. In the simulation tool, make the desired adjustments with respect to the selection and click Continue.

2. In the Simulation Data section, choose Import Test Data, select the spreadsheet file that contains the data, and

choose Import.

3. Once you have successfully imported the data, select the records you want to be included in the simulation and

choose Export Result to Excel.

When the simulation is done, the system creates a spreadsheet file that contains one row for each of the selected test data

records in which you can find the context data and the calculated result for that context.

Rule

Use

In BRFplus, a rule object is used as the technical representation of a simple business rule to be applied to a particular business

case. Rules can be adapted to the increasing complexity of business cases by adding additional actions or expressions to the rule,

and by combining any number of rules to a rule set. Actually, rules can only be triggered in the context of a rule set to which a rule

is assigned. They cannot be triggered as stand-alone objects.

Features

This is custom documentation. For more information, please visit SAP Help Portal.

120


10/15/26, 3:15 PM

A rule consists of an embracing If condition tested by the system once the rule is triggered. Based on the result of the condition,

the rule performs a set of operations. The condition must have a True branch, whereas the False branch is optional.

  Note
In addition to the integrated condition of each rule, you can make rule execution dependent on numerous other conditions, such

as rule enablement, time dependency, and others. You can control these additional conditions in the context of the rule sets to

which a rule is assigned.

In a rule, you can access and manipulate context data. This seems surprising at first glance because the rule itself does not have a

context of its own. Rather, accessing context data from within a rule means accessing the context data that are available to the rule

through the rule set to which the rule is assigned.

  Note
One rule can be assigned to many rule sets. Therefore, the system grants the rule access only to those context data objects that

all of the referencing rule sets have in common (that is, the intersection of all context data objects of all rule sets referencing the

rule). This is necessary for consistency reasons.

The following operation types are supported:

Triggering an action

Processing an expression. The result of the expression can be used to update the context.

Initializing or updating context data objects

More Information

Creating a Rule

Rule Set

Ruleset

Use

A ruleset is a collection of rules to be processed in a particular business case. It serves as an entry point for rule processing and can

be used as an alternative to a top expression assigned to a function.

Features

Function Assignment

For a ruleset to be processed, a function has to be assigned to the ruleset. The mode of operation setting of the assigned function

must be either Event Mode or Functional and Event Mode. A ruleset can be assigned to only one function, whereas one function

may have any number of rulesets assigned.

If a function has more than one ruleset assigned, the question arises how you can influence the execution order of the different

rulesets. To control the execution order, you can assign a priority to a ruleset that is evaluated at runtime when the assigned

function is executed. To set the ruleset priority, open the Detail section and enter the desired value (from 00 to 99) in the Priority

field. For more information, see Function, section Ruleset Execution Priority.

This is custom documentation. For more information, please visit SAP Help Portal.

121


10/15/26, 3:15 PM

  Note

In the BRFplus workbench, the Where used function does not yield a result for rulesets. However, in the Ruleset Header section

you can find out easily to which function a particular ruleset is assigned.

In previous releases of BRFplus, it was also possible to have each single rule assigned to a function as its trigger, rather than

assigning the function to the ruleset. This is no longer supported. However, if you have legacy applications that make use of the

individual assignment of rules and functions, the system is still able to process such rules.

Rule Assignment

The rules contained in a ruleset can be either named or unnamed:

Named rules are references to rule objects that you have defined in your BRFplus application. Such rules are stand-alone

objects and can be reused by different rulesets.

Unnamed rules are defined in the scope of a particular ruleset and are not accessible for other objects. Unnamed rules may

either contain a reference to a named rule or an immediate definition of the tasks to perform.

  Note

When you create a rule from inside a ruleset and enter a text in the Description field, this rule still counts as an unnamed

object. The system copies the text that you enter in the rule-specific Description field of the ruleset to the Text field of

the rule object, while the rule's Name field remains empty.

In addition to the trigger function, a ruleset also defines the precondition and validity period for each rule. The precondition and

validity period determine if the rule is triggered or not. Given that, the system provides numerous conditional levels to determine

whether the activities defined in a rule are to be carried out or not:

Assigned function is called.

Ruleset is enabled.

Ruleset precondition is fulfilled.

Ruleset-specific rule precondition is fulfilled.

Rule is enabled.

Current date and time falls into the rule validity period.

Precondition for an activity defined in the rule is fulfilled.

Variables

If you need to exchange additional data between the function assigned to a ruleset and the rules inside of the ruleset, you can

extend the ruleset's signature by adding variables to it. You can use any of the data objects available in the application as variables.

Inside of the ruleset, the variables are treated very much like context elements and can therefore be accessed by most of the

context-related actions like Assign Value to Context or Initialize Context. The near relationship between context data and

variables is also illustrated by the fact that for a ruleset, the Context Overview function displays not only the context data objects

of the assigned functions but also the ruleset variables.

  Note

Although variables can be used similarly to context data objects, it is not possible to define a ruleset precondition based on

variables. For a ruleset precondition, it is mandatory to refer to context data objects. In contrast to this, it is perfectly allowed to

define a ruleset exit condition based on variables.

This is custom documentation. For more information, please visit SAP Help Portal.

122


10/15/26, 3:15 PM

Deferred Ruleset Processing

As described above, you can define exit conditions for a ruleset that let you stop ruleset processing at a defined point in the

process flow if a condition is fulfilled. The default behavior here is that all data changes that were applied during processing of the

preceding rules are kept in the system, while any potential changes that would result from processing the remaining rules are of

course missing. Depending on the circumstances of a given business case, this may lead to data inconsistencies.

To overcome this potential problem, you can define that a ruleset may be restarted at the point where processing stopped in a

previous run. With this option set, you can continue an interrupted processing run, which helps you to complete the data changes

that result from the rule processing. This is helpful in cases where the exit conditions that you define for a ruleset are likely to be

fulfilled in your particular business case, that is, when a fulfilled exit condition is the rule rather than the exception.

  Example

You have a ruleset defined to calculate the energy fees for the apartment owners in an apartment building. However, not all of

the apartment owners send the electricity meter count in due time. In this situation, you can start a ruleset to calculate the

energy fees for those apartments for which the meter count is already known. However, if there are additional rules in the

ruleset for a statistical analysis of the building's energy consumption based on the apartment data, these rules require a

complete set of input data.

With deferred ruleset processing, you would place an exit condition before the statistics rules to check whether all required data

is available. If not, ruleset execution stops here but can be restarted at a later point in time when all the required data is

available, so that the remaining rules can be processed.

To enable deferred ruleset processing for a BRFplus application, proceed as follows:

1. Navigate to the application to which the ruleset belongs.

2. On the Miscellaneous tab, choose Restart Rulesets Enabled.

Once you have gone through these preparatory steps at application level, you can start using the additional features that are

available for deferred ruleset processing. You can access these features in the BRFplus workbench in the form of additional settings

for exit conditions in a ruleset.

  Note
For a complete understanding of the deferred ruleset processing concept, it is important to be aware of the following facts:

Deferred processing can be controlled on application level only for all rulesets belonging to an application. It is not

possible to control deferred processing for selected rulesets in an application.

Using deferred processing is possible only via appropriate program calls to the BRFplus API. There is no support for

interactive use of this feature in the BRFplus workbench UI.

Deferred processing is supported via the following API objects:

Name

Use

IF_FDT_RS_INTERRUPT_HANDLER

Provides methods to retrieve system interrupts created by

the system when a ruleset exit condition was fulfilled.

CL_FDT_RS_INTERRUPT_HANDLER

Implements interface IF_FDT_RS_INTERRUPT_HANDLER.

This is custom documentation. For more information, please visit SAP Help Portal.

123


Use

Provides methods to save an interrupt instance to the

database, to restart the associated ruleset, and to delete a

saved interrupt from the database.

10/15/26, 3:15 PM

Name

IF_FDT_RS_INTERRUPT

More Information

Creating a Ruleset

Function

Modes of Operation

Rule

Catalog

Use

A catalog simplifies the rule maintenance process for the business user by hiding the repository and displaying only the relevant

objects that are necessary for the maintenance of business rules in a given business scenario. It serves as a filter for the entirety of

all objects that exist in the repository.

For business users, a typical catalog offers only those elements of a BRFplus application that are needed for business-relevant

adjustments or extensions (for example, decision tables). All of the remaining elements like functions, data objects, constants,

formulas, or actions are not part of such a business-oriented catalog and remain invisible to the user.

  Recommendation

To take full advantage of the complexity reduction that you can accomplish by using catalogs, we recommend that for business

users working with BRFplus, you disable all other views in the BRFplus workbench so that only the catalog view remains. To do

so, choose

, then  Views  and disable all views except Catalog.

Features

Object Types

For each catalog, you can define a set of object types that can be added to that catalog. Restricting this set is a suitable means to

ensure that only those objects that you consider as useful for the target group can be added to the catalog. This prevents the users

from being exposed to objects that are highly technical in nature, or, from a business perspective, do not contribute directly to the

solution of a particular use case.

  Note

Restricting the list of allowed object types does not only prevent a user from adding objects that are not covered by the list.

Rather, if the catalog already contains objects of a type that you remove from the list of allowed object types, the system

considers this as a violation of the catalog consistency. In this situation, you can either decide to add the previously removed

object type to the list again, or to remove those objects from the catalog that correspond to the removed object type.

This is custom documentation. For more information, please visit SAP Help Portal.

124


10/15/26, 3:15 PM

Among others, the list of allowed object types contains the Expression object type. For technical reasons, this object type does

not only refer to expressions of the BRFplus expression types (decision table, formula, and so on). Rather, it also covers actions

and rules.

Node Types

A catalog can contain any number of folder nodes, object nodes, and catalog nodes. Here is a short description of the different

node types:

Folder Nodes

Folder nodes allow you to create a folder structure in a catalog. You can use these folders for grouping the objects by

different use cases or any other criteria that you consider to be helpful for business users.

Object Nodes

An object node is a catalog element carrying a reference to a BRFplus object like an expression or a function.

Catalog Nodes

With a catalog node, you can establish a reference to a node from a different catalog, thus allowing you to embed parts of

already existing catalogs into a given catalog. With this node type, you can reuse an already defined group of objects that

may be relevant for different catalog scenarios.

Object Nodes

The most common way of populating a catalog is by referencing existing BRFplus objects, or by creating a new object and

simultaneously establishing a reference from the catalog to that object. You can add references to objects of all kinds to a catalog,

as long as the object type has not been excluded for use in that catalog.

When you add an object reference to a catalog, the object's short text is copied into the catalog for display purposes. You can

modify this standard behavior as follows:

Overwrite

The object text that has been copied into the catalog technically belongs to the reference that points from the catalog to

the referenced object. As a consequence, you are free to overwrite this text by something different that may better suit your

needs within the scope of the catalog. The original text of the referenced object itself is not affected.

Text Binding

With the Bind Text option, you can decide that in the catalog, always the original short text of the object is displayed. Should

the object text be changed, that change is reflected immediately in the catalog. With this setting, the text field in the catalog

is read-only to avoid any unwanted change to the referenced object.

When text binding is active, the system activates an additional fallback mechanism to ensure that there is always a proper

text being displayed: If the referenced object happens to have only the longer Text attribute maintained, while the Short

Text is empty, then the Text attribute is bound to the catalog automatically. In that case, it may happen that the object text

cannot be displayed completely in the catalog because of field length restrictions.

Placeholder Nodes

The standard procedure for creating object or catalog nodes is to create a new node and assign an object or catalog node to it,

either by selecting an existing object or by creating a new one. However, you may find yourself in situations where you have a clear

idea of the relevant objects from a business perspective, but the technical details are not yet clarified.

With placeholder nodes, you can solve this dilemma by postponing the technical assignments. Here, you define the set of objects

that are needed in a catalog from a purely semantic point of view, without having to take any technical decisions. Later on in your

This is custom documentation. For more information, please visit SAP Help Portal.

125


10/15/26, 3:15 PM

project, when the technical requirements have been clarified, you walk through all the placeholder nodes in your catalog and assign

the elements that have been agreed upon.

Folder and Node Attributes

In a catalog, you can define an individual set of attributes for folders, object, and catalog nodes. Once you have attributes defined,

you can assign values to each attribute of each node or folder in your catalog. Such attribute values are not used by BRFplus itself.

Rather, you may find it useful to access the attribute values stored in a catalog from the calling application in the backend system.

Or, you may decide to store some administrative information on node level that can be accessed from the BRFplus workbench for

reference purposes.

  Example

For folder nodes in a catalog, you define two attributes:

Use Case

In this text field, you can enter a short description of the use case for which the objects assembled in a folder are meant.

Reused

With this boolean field, you can indicate that a particular folder is referenced by a catalog node from a different catalog.

This could help you as an administrator to decide whether it is safe to remove a folder.

For an attribute, you may choose from a subset of the elementary data objects that can be accessed from your application. This

subset is made up of the following data types:

Boolean

Number

Text

Versioning Behavior

Unlike all other BRFplus object types, newly created catalog objects always have the versioning setting switched off. This is true

even if the application default setting for versioning is on. However, you can still switch versioning on manually for a catalog if

desired.

  Note

The reason for the special versioning behavior of catalog objects is the fact that the changes done to the catalog structure is

hardly ever relevant for your business. Therefore, there is usually no need for logging the different states that a catalog has been

in. Besides, catalogs are subject to frequent changes, so versioning can lead to unwanted high storage space requirements.

More Information

Working with Catalogs

Workbench Personalization

Object Filter

Use

This is custom documentation. For more information, please visit SAP Help Portal.

126


10/15/26, 3:15 PM

With an object filter, you can define a subset of object types that should be available in a BRFplus application at design time. This

helps you to ensure that for business rules of all kinds in an application, only those object types can be used that can pass through

the filter. Defining object filters as well as assigning them to user profiles is a typical administrative activity.

  Example

In a productive BRFplus application, you have imported a number of custom expression types to enhance the functional scope

of BRFplus. However, these expression types are partially still prototypes and not released for productive use. To protect your

application against unwanted effects caused by the prototype expressions, you can define a filter that lets users instantiate only

those expression types that have been shipped by SAP. All custom expression types would be hidden to those users for whom

the filter is applied.

Features

General

Object filters are used for administrative purposes at design time, namely to control the types of objects that are available for

setting up a business rule. As a consequence, the access level in effect for other object types is not relevant for the usage of object

filters. Although you create an object filter in the context of a particular application, its usage is not restricted to that application. In

other words, object filters are cross-application objects.

There are two main areas in the BRFplus workbench that are affected by the object filter settings:

Creating new objects

If a filter is assigned to an application, you can only create objects of those types that have been allowed in the filter

definition. Object types that have been filtered out are not offered for creation.

Selecting object types in the Object Query dialog

If a filter is assigned to an application, you can only select objects of those types that have been allowed in the filter

definition. Object types that have been filtered out are not offered for selection.

  Note
The effect of a filter assignment is limited to the creation of new objects, or the selection of already existing objects in the

Object Query dialog. As opposed to this, all objects that already exist in the application are not affected by a filter. They remain

visible and ready for productive use. This is true even for those objects whose type has been excluded by a filter.

Details

Applications

On the Applications tab, you select the applications where the filter shall be effective for selecting objects in the Object Query

dialog.

Object Types

On the Object Types tab, you find the list of object types that are available across the entire system. By default, all available object

types are allowed. You define the filter by deselecting certain object types according to the use case you want to model.

  Note

In this list, you find all object types that exist in the system, including custom expression types, regardless of the original

application or access level. Therefore, if you decide to allow the use of a particular object type, there is no guarantee that this

decision has any visible effect in a particular application.

This is custom documentation. For more information, please visit SAP Help Portal.

127


10/15/26, 3:15 PM

Some object types are always allowed and cannot be deselected. For example, this is true for data objects of all types.

Filter Assignment

Once you have defined the filter settings and activated the filter, you need to assign the filter to one or more applications for the

filter settings to take effect. You can accomplish this with the help of the Personalization dialog.

  Recommendation

After having changed the assignment of filters to applications, we recommend that you restart the workbench session to ensure

that the changed settings take effect.

Process

Maintaining an Object Filter

To create an object filter, proceed as follows:

1. From the context menu of an application in the repository tree, choose  Create

 Object Filter

.

2. Define a name and a text for the filter.

3. Click Create and Navigate to Object.

The system displays the new filter in the work area.

4. On the Applications tab, decide whether the object selection filter shall be effective for all applications or only for those

applications that you specify.

5. On the Object Types tab, decide which object types can be used for creating new objects in the applications to which the

filter has been assigned.

6. Save and activate the filter.

Assigning an Object Filter

To make an object filter effective in the BRFplus workbench, proceed as follows:

1. Choose

 in the upper right corner of the workbench window.

2. On the Filters tab of the Personalization dialog, choose Add Filter to specify the object filter you want to use. You can

choose from all filters that exist in the system, regardless to which application they belong.

3. In the All Applications column, specify whether the filter shall be effective for all applications in the system. If you choose

No, you have to specify the desired applications in the Application column.

Repeat the steps above for any other object filters you may want to make effective.

Versioning

Use

Versioning allows you to track the changes that have been done to a BRFplus object over time. It is based on the timestamp that

the system assigns to objects when they are saved and activated. Different versions of the same objects can be kept in the system

and processed based on the timestamp.

This is custom documentation. For more information, please visit SAP Help Portal.

128


10/15/26, 3:15 PM

The system creates a new version every time an active object is changed and saved (except for versioning mode Transport-

dependent- see section Default Versioning Behavior below). As opposed to that, any changes done to an inactive object do not

create a new version. Versioning can be switched on or switched off.

Old versions can be accessed by passing the timestamp to the PROCESS method or the GET<...> methods. If you pass a

timestamp and access an object, a version of the object at that particular time is returned. If no timestamp is passed then the most

recently activated version is used for processing. In the case of a GET<...> method, the latest object properties (active or

inactive) are returned.

  Example
A constant expression has been created on June 24, 2007 (date) at 01:56:19 (time). The value assigned to the constant is ABC.

The value is changed to XYZ on July 14, 2007 at 04:46:17. The change is activated and saved. The value is again changed to HIJ

but is not activated. The table below summarizes the changes:

Incident (Event)

State

Change timestamp

Version

Constant Value

Text

(Date Time format)

A new object is

Inactive

created.

The object is

Active

activated.

The constant value

Active

is changed and

activated.

The constant value

Inactive

is changed and

saved.

2007-06-24

01:56:19

2007-06-24

01:58:35

2007-07-14

04:46:17

2007-08-12

01:56:19

1

1

2

3

text ABC

text ABC

text XYZ

ABC

ABC

XYZ

HIJ

The current version of the constant has the value HIJ and is not activated. The BRFplus Application Programming Interface

(APIs), however´, processes only activated versions. The last active version (in this example, the last active version is 2) is valid

until another active version is created.

  Note
Versioning only makes sense for objects that are relevant for processing. This is true for almost all BRFplus object types, with

the exception of the following object types that are never versioned:

Catalog

User-defined expression type

User-defined expression types are not versioned although they are processing-relevant. This is due to the fact that

BRFplus has no control over the design of user-defined expression types. It is therefore possible that a given expression

type is totally redesigned and shows completely different behavior over time.

Features

Default Versioning Behavior

You can define whether newly created objects are put under version control or not by default. This default setting is done on

application level and affects all objects that are created in the scope of that application. You can adjust this setting for an

This is custom documentation. For more information, please visit SAP Help Portal.

129


10/15/26, 3:15 PM

application in the BRFplus workbench on the Default Settings tab.

  Note

Under certain circumstances, using object versions can lead to potential side-effects, which can lead to error situations that are

difficult to resolve. This is why SAP has decided to qualify the default versioning modes Versioning On as well as Versioning

Enforced as "not recommended". For more information, see Versioning: Pros and Cons.

You can choose from the following default versioning modes:

Off

Objects that you create have the versioning attribute set off by default. You can manually set versioning for all objects in the

application on or off at any point in time. The versioning setting of already existing objects is not affected by this default

versioning mode.

On (Not Recommended)

Objects that you create have the versioning attribute set on by default. You can manually set versioning for all objects in the

application on or off at any point in time. The versioning setting of already existing objects is not affected by this default

versioning mode.

Enforced (Not Recommended)

Objects that you create have the versioning attribute set on by default. As long as this default versioning mode is in effect,

versioning of all objects in the application is enforced and cannot be set off.

When you set this default versioning mode, the system offers to set versioning on for all objects that already exist in the

application. If you confirm, versioning is set on for all existing objects in the application. If you reject, the version setting for

all existing objects is left unchanged. In both cases, newly created objects will have versioning set on, and versioning cannot

be set off.

Depending on the system status, the confirmation dialog mentioned above can contain additional controls:

Transport Objects: Tick this checkbox to make sure that the changed objects are recorded on a transport request.

This checkbox is available only if the application is transportable, and the system client has been configured such

that changes to client-specific objects are not automatically recorded.

Transport Request: ID of the transport request to be used for recording the changes. If the application is already

assigned to a transport request, the respective transport ID is displayed and cannot be changed. Otherwise, you can

choose a suitable transport request.

  Note

If you decide to let the system set versioning on for all existing objects, you should be aware that this is only possible for

objects that are active and in a consistent state. If there are any inactive objects in the application, the system does not

change the versioning setting of these objects. You can manually activate these objects, either individually or with the

mass change tool.

If, at a later point in time, you decide that the Enforced versioning mode is no longer needed, you can easily choose one

of the other default versioning modes. This is a prerequisite for you to set versioning off for selected objects if you so

desire.

Transport-dependent

Objects that you create have the versioning attribute set on by default. This mode is a refinement of the

Versioning=Enforced mode and is specially designed to reduce the number of versions to a reasonable amount, thus saving

storage capacity. This versioning mode shows the following behavior:

This is custom documentation. For more information, please visit SAP Help Portal.

130


10/15/26, 3:15 PM

Transport-dependent versioning is possible only for objects in applications that are transportable (storage type

System or Customizing; development package properly assigned).

When you modify an already active object, the system creates a new version for that object. As opposed to the other

versioning modes, this new version remains in effect until the object is transported from the design time system to

other systems. This means that during the time between the first change to the object and the time it is transported,

you can apply as many changes to it as you like, and you can activate it as often as you like, without creating a new

version for each single modification.

Versioning is mandatory for all objects in an application and cannot be set off for individual objects.

This versioning behavior is useful in design time systems where objects under development are frequently changed, while

these changes have no impact on your company's business because the changes are done in a separate, non-productive

system. Also, this versioning mode results in an automatic synchronization of object versions in both the development

system and the productive systems.

When you set this default versioning mode, the system offers to set versioning on for all objects that already exist in the

application. If you confirm, versioning is set on for all existing objects in the application. If you reject, the version setting for

all existing objects is left unchanged. In both cases, newly created objects will have versioning set on, and versioning cannot

be set off.

Timestamp

For each version of an object, the system maintains a timestamp. Depending on the object version status, the meaning of this

timestamp varies:

Inactive: As long as a version is still inactive, the version timestamp indicates the point in time when the object has last been

saved.

Active: For an active version of an object, the version timestamp indicates the point in time when the object has been

activated.

It can be helpful to keep in mind these two different notions of the timestamp when you need to understand clearly which object

version is used at runtime. For example, a situation may occur where a versioned object for which an active version already exists is

changed, but the activation of the changed version is postponed to a later point in time. The system then continues to use the older

active version at runtime as long as the changed current version is not activated. In other words, for the changes to take effect, the

relevant date is the moment when the changed version is activated, not the moment when it was changed. Therefore, the version

timestamp holds the most relevant data with respect to the object version status. As a side effect of this system behavior, it is not

possible to tell for an active version when the last changes have been applied to the object.

Versioning of Texts And Documentation

For objects under version control, you can decide that the object texts and documentation shall also be version-dependent. With

this feature, you can keep track of naming changes that have been applied between different versions.

  Example

In a BRFplus application for compensation management, you may have modeled a number of data objects representing

different tax amounts that are applicable in a country. After a government change, some of the taxes are still in place but have

been renamed by the authorities. You would then reflect the new tax name by creating a new version-dependent name for the

affected data objects, while keeping the previously used names in an older version due to legal compliance.

Also, if the internal structure of a particular object changes significantly over time, it may be a good idea to mention this in the

object documentation.

  Example

This is custom documentation. For more information, please visit SAP Help Portal.

131


10/15/26, 3:15 PM

In a BRFplus application, you have a complex formula expression used for risk assessments as a basis for insurance premium

calculation. Over time, you may have to add a number of risk factors that were not in scope at the beginning. To clarify what the

formula in its revised state can do, you maintain a version-dependent documentation for the expression.

  Note
Versioning of texts and documentation leads to significantly higher consumption of database storage capacity. We therefore

recommend to use this feature only in cases where this is mandatory from a use-case perspective.

Versioning Status

Depending on the different versioning modes explained in the Default Versioning Behavior section above, the status of an object

version can take different values. These values are:

Versioning Status

Not versioned

Versioned

Versioned by transport

Not transported

Description

Only one version exists for an object. All changes to an object are

stored in the same version, thereby overwriting the object without a

possibility to revert to the previous state.

In addition to the initial version that exists for each object, this

status leads to the creation of a new version whenever a previously

activated object is changed. The cumulated changes to an object

version are frozen in that version by activating it.

Similar to Versioned. However, a version is frozen not by activation,

but by transporting the activated object to another system. In other

words, the same version can be activated several times as long as it

is not transported.

A version that was created while the versioning behavior was set to

Versioned by transport, but the behavior was changed before the

respective transport was released.

The following table explains how a particular change that is done to an object corresponds with its versioning status:

Object Changes

Version No.

Versioning Status

New object O created with versioning

switched off.

Versioning switched on for O.

O activated.

Versioning behavior of the application set to

transport-dependent.

O changed.

Versioning behavior of the application set to

Versioning enforced.

O activated.

Transport request containing O released.

1

1

1

1

2

2

3

3

Not versioned

Not versioned

Versioned

Versioned

Versioned

Not transported

Versioned

Versioned by transport <transport ID>

This is custom documentation. For more information, please visit SAP Help Portal.

132


10/15/26, 3:15 PM

The table shows that with transport-dependent versioning, two additional status values have been introduced, Versioned by

transport <transport ID> and Not transported. The two values denote the following situations with respect to versioning:

Versioned by transport <transport ID>: Transport-dependent versioning is in effect for the application to which the object

belongs. The object has been recorded on transport request <transport ID>, and the transport has been released.

Not transported: Transport-dependent versioning was initially in effect for the application to which the object belongs.

However, before the transport was released, the versioning mode has been set to Versioning enforced. As a consequence,

the system creates a new version for the object. The previous version that should have been related to the release of a

transport is now marked as Not transported.

More Information

Versioning: Pros and Cons

Application

Tracing

Setting Versions

Versioning: Pros and Cons

A discussion of both the advantages and disadvantages of the different versioning modes.

Although keeping track of object versions is a powerful feature and, under certain circumstances, can even be legally required, it

can also lead into potential problems: Keeping object versions always leads to a larger footprint in the database because for each

version, all the data that makes up a particular object version is stored again in the database. That is, there is no way of storing only

the delta between two versions. However, in addition to simply blowing up the database size, there are also other potential side-

effects, which can lead to error situations that are difficult to resolve. This is why SAP has decided to qualify the default versioning

modes Versioning On as well as Versioning Enforced as "not recommended". The intention behind this decision is to make it clear

to BRFplus users that these two versioning modes imply potential maintenance problems that are not obvious at first sight, as well

as an increase of storage consumption that is in most cases unwanted and not needed. When it comes to the decision which

default versioning mode should be used, we recommend the following process:

1. Decide whether versioning is needed at all for the application in question. If not, choose Versioning off.

2. If versioning is needed for legal reasons or to comply with binding organizational rules, choose Versioning Triggered by

Transport. With this setting, a new version is created only when an object is transported to a test or productive system.

3. Only if you have strong reasons for recording a gapless sequence of all object versions (for example, for test purposes or to

meet special quality assurance requirements), choose any of the versioning modes that are not recommended. If you take

this decision, we still recommend you make sure that the versioning mode is reverted to one of the recommended settings

as soon as possible, just to avoid the potential problems outlined in this chapter.

The more versions of objects exist in the database, the higher the number of interdependencies between the objects as well as the

risk of hidden object dependencies. For example, you may want to delete an object Object1 from the BRFplus repository. You first

check whether the object in question is still used by other objects. If so, you make sure that you remove these usage relationships

so that object Object1 can be deleted. However, it can easily happen that the system refuses to delete the object due to

"historical" usage relationships that are still in effect for an older version of object Object1. That is, although the current object

version is no longer used by any other object, there may still exist usage relationships between an older object version and some

other object. If this happens, the system would not allow to delete the object.

This is custom documentation. For more information, please visit SAP Help Portal.

133


10/15/26, 3:15 PM

To overcome this issue, you could either delete the referencing object (but this might not be an option if that object is still needed)

or delete the versions of the referenced object Object1. For deleting old object versions, BRFplus offers report

FDT_TRUNCATE_VERSIONING that you can start from within transaction SA38 or SE38, respectively. The report is also included

in the auxiliary reports collection presented by transaction FDT_HELPERS ( BRFplus - Deletion

  BRFplus: Discard Old Versions

). Finally, the same functionality is available in the BRFplus workbench via  Tools

  Application Administration , operation

type Discard Old Object Versions. Note that the backend version of the report offers additional features compared to the BRFplus

workbench tool, especially with respect to extended object selections that go beyond the boundaries of a particular BRFplus

application. Also, you may want to use the backend version of the report in a batch job that you can define to let old object versions

be removed from the database on a regular schedule in the background.

When using the cleanup report, you should be aware of the following implications:

Cleaning up object versions by running the report is always limited to the system where you are currently logged on. If

object versions have already been transported into your system landscape, you should run the report in all affected

systems.

When you delete an entire object (that is, not only an object version) and the deletion is recorded in a transport request, you

would of course expect that the object will also be deleted in the systems into which the transport request is imported.

However, if the system determines that the object to be deleted is still referenced by an object in the target system, the

object is only marked for deletion rather than being actually deleted in the target system.

Export and Import of XML Data

Use

You can convert BRFplus objects into an XML representation. This is helpful if you want to transfer objects between systems that

are not located in the same system landscape, or if there is no transport connection provided by the SAP transport system.

Prerequisites

You are running the BRFplus workbench in Expert Mode.

Features

Export

The XML export function works in an object-based manner, that is, you start by selecting a BRFplus object that you want to export.

However, it is possible to extend the scope of an XML export in the following ways:

Include Referenced Objects: With this option set, the selected object is exported together with all objects that are directly

or indirectly referenced by the selected object.

Include Application: With this option set, the selected object is exported together with the BRFplus application to which the

object belongs.

In addition to the scope selection as described above, you can further fine-tune the export by choosing a particular XML version

and an XML schema for the export. Depending on the selection you make, the system adapts the format and syntax of the

exported data. This is helpful in situations where you have to transport BRFplus objects to a system with a lower release than the

source system. Of course, it is always recommendable to choose the highest XML version for the export that is supported by the

target system so that the system can profit from as many features as possible.

The purpose of the XML schema selection is to let you choose between different flavors of an XML-based object representation:

This is custom documentation. For more information, please visit SAP Help Portal.

134


10/15/26, 3:15 PM

Internal

As the name suggests, the Internal schema renders the schema element names in the same way that is used internally by

BRFplus. Therefore, with this schema, the system does not need to perform any transformations during XML import or

export.

External

The External schema is functional equivalent to the Internal schema, but renders all schema element names in upper

camel case notation rather than in capitals. This makes the XML data more readable, which is useful if you want to analyze

the XML data manually.

  Note

To find out which is the highest XML version supported by the target system, start the import function in the target system. The

highest version supported is displayed on the screen.

The XML schema selection is only available if you have chosen the respective setting in the Personalization dialog.

Import

The XML import function is the complementary to the export function. It is used to reimport XML data that have previously been

exported from BRFplus into a different system.

Prior to actually importing data, we recommend to first start the import as a Test Run. The system then checks the import data to

be uploaded for inconsistencies and other possible problems, without actually writing any data into the target system. You can use

the check results for cleaning up and correcting the import data before you start the actual data import.

If the target system into which you want to import the data is not located at the end of the transport chain in your system

landscape, the imported data has to be transported to the subsequent systems. To accomplish this, you have to enter the ID of a

suitable transport request that you have previously created in the import target system.

Import Types

For XML data to be imported into the system, BRFplus offers the following import types:

Standard

With this option, you can import changes for objects that are changeable in the target system.

Repair

With this option, you can repair content that is normally not changeable in the system due to the fact that it was imported

to the system by a normal transport. The repair option should only be used to import content changes provided by an SAP

correction note. You may use this option to apply a content correction to a system before the corresponding support

package with the corrected content is imported into the system.

Local Copy

With this option, you can create a local copy of a non-local application in the source file.

  Note

You can use this option only if the application in the source file is not local and has not yet reached the target system via

a normal transport. This check ensures that local copies cannot overwrite transported data. This is important because

this option results in an exact copy of the imported objects, including the original ID of the imported objects. With that,

the ID of the affected objects is no longer globally unique, and any further transport would lead to unpredictable results.

This is custom documentation. For more information, please visit SAP Help Portal.

135


10/15/26, 3:15 PM

Note that selecting a particular import type is only possible if the corresponding personalization setting has been activated.

Otherwise, the import type selection is not visible, and the system uses the Standard import type.

Handling of Import Conflicts

If the system detects an object in the import data with the same ID as an already existing object in the target system, the further

processing depends on the versioning setting of that object:

Versioning is active

The object contained in the import data is imported as a new version of the object in the target system.

Versioning is not active

The object contained in the import data overwrites the existing object in the target system without further notice. There is

no way for a user to influence this behavior.

Export and Import Across Applications

Both export and import of XML data can only be performed for objects belonging to the same BRFplus application. If you have to

transfer objects from different applications, you have to split the export and import process such that for each application involved,

you have to use a separate data file. When importing such a multi-application project into the target system, make sure that the

data files are processed according to the usage relationships between the different applications: Start by importing objects that

are used by objects from a different application before importing the using objects. Otherwise, the import fails due to object

references that the system cannot resolve.

Activities

Export

To export a BRFplus object from the current system, proceed as follows:

1. Choose  Tools

 XML Export

.

The system displays the XML Export screen.

2. Click Select an Object to choose from all BRFplus objects that are available in the current system the one that you want to

export.

3. Choose Include Referenced Objects if you want to include all objects in the export that are referenced by the selected

object.

4. Choose Include Application if you want to include the application object in the export to which the selected object belongs.

5. From the XML Version dropdown list, choose the highest version number that is supported by the target system.

6. From the XML Schema dropdown list, choose the XML schema that fits your needs best.

7. Click Generate XML File to start the XML conversion process.

  Note
The Generate XML File is active only after you have selected an object for export.

8. Click Download XML File to define a folder in the file system where the system shall store the XML file generated in the

previous step.

Import

This is custom documentation. For more information, please visit SAP Help Portal.

136


10/15/26, 3:15 PM

To import a file containing BRFplus object data into the current system, proceed as follows:

1. Choose  Tools

 XML Import

.

The system displays the XML Import screen.

2. Make sure the XML version of the data to be imported is less than or equal to the Highest XML Version Supported as

outlined on the XML Import screen.

3. Enter the name of the XML File to be imported. You can also select the file by clicking the Browse button and navigating

through the file system.

4. Choose the appropriate Import Type.

5. Decide whether the data to be imported shall be written to a transport request:

For BRFplus objects that are used only local in the target system, no transport is needed. The same applies if there

are no subsequent systems in your system landscape receiving transports from the import target system.

For BRFplus objects defined as customizing objects, enter a Customizing Transport Request ID. This is necessary

for customer-defined objects.

For BRFplus objects defined as system objects, enter a Workbench Transport Request ID. This is necessary for

objects delivered by SAP.

6. Decide whether you want to execute the XML import as Test Run or not.

The Test Run mode is a simulation mode where the system performs all import steps except for actually writing data into

the target system. You can use this mode for checking if the import data is consistent and complete before making physical

changes to the target system.

7. Click Upload File to start either the test run or the XML data import.

More Information

Storage Types

Versioning

Authorizations

Use

The different activities that you can carry out in BRFplus are covered by the SAP authorization concept. This means that you can

assign different access rights to rule modeling and execution to the people who work with BRFplus.

Integration

The different authorization objects described in the Features section below are assembled in the predefined user role BRFplus

Administrator ( SAP_BC_FDT_ADMINISTRATOR) that is shipped with BRFplus.

Features

For BRFplus, the following authorization objects exist:

This is custom documentation. For more information, please visit SAP Help Portal.

137


10/15/26, 3:15 PM

FDT_ADMN: You use this authorization object to control the access to various administration and monitoring tools. These

tools are only needed by developers and system administrators.

FDT_WORKB: You use this authorization object to control user access to the BRFplus workbench. For a user who has been

granted authorization to start the workbench, you can fine-tune the user's access to the different workbench tools like XML

data transfer or web service generation.

FDT_OBJECT: You use this authorization object to control the authorization to display, create, change, or delete objects in

BRFplus (including functions, expressions, expression types, filters, and applications).

FDT_TRACE: You use this authorization object to control the authorization to display, create, or delete the trace information

recorded for the execution of a function in BRFplus.

FDT_PROC: You use this authorization object to check if a user is allowed to process the rules associated with a BRFplus

function.

  Note

Currently, this authorization check is only executed if a function is triggered via a web service or a function module, and

the user has activated the authorization check during the generation of the web service or function module.

Activities

Create the user profiles you require and then assign authorization objects to these profiles. Then assign the newly created user

profiles to possible users.

  Note
You can find further information on the activities associated with the different authorization objects in the online

documentation on the authorization objects themselves. You can call this up in the maintenance transaction Role maintenance

( PFCG).

More Information

BRFplus Administrator

BRFplus Administrator

Role SAP_BC_FDT_ADMINISTRATOR

This role provides access to the BRFplus workbench, that is, the user interface for creating rule objects (such as expressions or

data objects) and for modeling and testing rules. Business Rule Framework plus (BRFplus) is an ABAP-based business rules

modeling system that all applications built on the Netweaver ABAP stack can use.

With this rule assigned to a user profile, a user can carry out all kinds of activities in the BRFplus workbench. These activities

include creating, changing, deleting, or versioning of all types of objects that are supported by BRFplus. Due to the comprehensive

scope of authorizations granted by this role, you should assign it only to persons who are in charge of performing administrative

tasks with BRFplus. For all other users, you can use this role as a copy template to derive more restricted roles.

Activity

The role comprises authorization objects for the following tasks.

This is custom documentation. For more information, please visit SAP Help Portal.

138


10/15/26, 3:15 PM

Accessing individual objects

Rule processing via web service or RFC-enabled function modules

Rule processing with trace data

Accessing the different tools offered in the BRFplus workbench for administrative tasks

Integration

You need to assign this role (or an individually restricted copy of this role) to users who work directly with the BRFplus workbench.

You also need to assign this role to users who work with an application that uses BRFplus functions and makes use of any of the

features listed in the Activity section above.

Tasks

Use

This section describes the tasks you need to perform using BRFplus to model applications.

The tasks are grouped as follows:

Modelling Applications

Describes how to create application and set properties to the applications

Building Functions

Describes how to create function and set properties to the function

Creating Expressions

Describes tasks that you need to perform to create different expressions

Creating an Expression Type

Describes task that you need to perform to create an expression type

Creating Data Objects

Describes how to create different types of data object

Creating a Rule

Describes task that you need to perform to create a rule

Creating a Rule Set

Describes task that you need to perform to create a rule set.

Working with Catalogs

Describes tasks that you need to perform to create a catalog

Creating Action Types

Describes how to create and use actions in an application

Working with Tools

This is custom documentation. For more information, please visit SAP Help Portal.

139


10/15/26, 3:15 PM

Describes tasks associated with the various tools

Modelling Applications

Use

This section describes how to create and set attributes for applications in BRFplus.

Topics in this section include :

Creating an Application

Setting Properties

Adding Objects

Setting an Access Level

Creating an Application

Procedure

1. In the menu bar, choose  Workbench

 Create Application...

2. In the Object Creation dialog box that appears, enter the following data in the General Data section:

Name

  Note

The application name has to be unique.

For more information, see Naming Conventions

(Optional) Short Text

You can add a brief description about the application in the Short Text field.

(Optional) Text

You can add additional information about the application in the Text field.

3. In the Application section of the Object Creation dialog box, choose the storage type.

  Note

To create a test or demo application, select the Create Local Application checkbox.

Local applications are not transported to other systems.

For more information, see Storage Type

4. Enter the development package and choose Create or Create and navigate to object.

Results

The application node appears in the Navigation panel and the application opens in the Object Manager panel.

This is custom documentation. For more information, please visit SAP Help Portal.

140


10/15/26, 3:15 PM
Next Steps

Setting Properties

Setting an Access Level

Adding Objects

Setting Properties

Procedure

1. Open the application in the Object Manager panel.

2. Under the Detail section, under the Properties tab, enter the application context in the Application Component field.

3. Choose the software component in which you want to save the application.

4. Enter the class in the Application Exit Class field.

BRFplus provides exits for applications which require special needs. A class is created to fulfill the special needs of the

application. To implement the methods, the class name has to be registered in the above field.

Next Steps

Creating an Application

Adding Objects

Setting an Access Level

Adding Objects

Procedure

1. Open the application in the Object Manager panel.

2. Under Detail section, choose the Contained Objects tab .

3. On the Contained Objects tab page, choose the type of object that you want to create and choose Create Object.

The Object Creation dialog box opens.

For more information on creating objects, see

Creating Data Objects

Creating Expressions

Creating an Expression Type

Creating a Function

Creating a Rule

Creating a Rule Set

Creating a Catalog

This is custom documentation. For more information, please visit SAP Help Portal.

141


10/15/26, 3:15 PM

Creating Action Types

Next Steps

Creating an Application

Setting Properties

Setting an Access Level

Setting an Access Level

Context

By setting an access level for an object, you can define the scope of objects that are allowed to access the current object. Access

levels are supported for all object types in BRFplus. By default, each object is assigned the most restrictive access level (

Application). Choosing one of the other access levels therefore extends the scope of objects that are permitted to access the

current object. It is advisable to always use the most restrictive access level and only extend the scope if needed. This is because

with an extended scope, the risk of unwanted side effects increases.

  Note

From a technical perspective, it is uncritical to extend the access level of an object. As opposed to this, restricting the access

level of an object (for example, from Top Component to Application) can lead to unexpected results if the object is already used

by an external application that depends on the extended access rights.

For data objects, the system prevents the restriction of an object's access level once the object has already been transported

into another system. This is to ensure that references to the object that may have already been created in the subsequent

systems remain valid.

The following access levels are available:

Application

Object can be accessed by all other objects that belong to the same BRFplus application.

Application Component

Object can be accessed by other objects belonging to an application assigned to the same component like the object's

application.

Superordinate Component

Object can be accessed by other objects belonging to an application assigned to a component with the same superordinate

component as the component assigned to the object's application. For example, an object assigned to component FI-GL

can access an object assigned to FI-AA with access level Superordinate Component because both objects have the same

superordinate component, FI

Top Component

Objects can be accessed by all other objects under the same top component. For example, three objects A, B, and C

assigned to components FI-GL, FI-AR, FI-AA-AA can all access object O belonging to any of the FI-* components if O is

assigned to access level Top Component because all three objects have the same top component as O, namely FI.

Global

This is custom documentation. For more information, please visit SAP Help Portal.

142


10/15/26, 3:15 PM

Object can be accessed by other objects from all other applications, regardless of their assigned component.

  Note

Of all the object types supported by BRFplus, there is one that is not affected by access level settings. This is the case for object

filters. Here, the system does not observe access level settings, with the following consequences:

Like all other object types, object filters have an attribute for defining the access level. However, the system ignores the

access level setting of an object filter. As a result, all object filters defined in the system are visible and usable in all

applications.

The object types that you can restrict in an object filter are presented as a system-wide cross-application list, regardless

of the access level that has been defined for the object type.

Procedure

1. Open the object in the Object Manager panel.

2. Under the General section, choose the level in the Access Level field.

Building Functions

Use

This section describes how to create and work with functions in BRFplus.

More Information

Creating a Function

Setting Properties

Assigning Context and Result

Assigning Top Expression

Creating a Function

Context

A function imports context and returns result.

Procedure

1. Open the application in the Object Manager panel.

2. Under the Detail section, choose the Contained Objects tab.

3. In the Contained Objects tab page that appears, choose Function from the Type field and choose Create Object.

4. In the Object Creation dialog box that appears, enter the following data:

Name

This is custom documentation. For more information, please visit SAP Help Portal.

143


10/15/26, 3:15 PM

For more information, see Naming Conventions

(Optional) Short Text

(Optional) Text

5. Choose Create or Create and navigate to object.

  Note

If you choose Create the newly created function appears under the Contained Objects tab.

If you choose Create and navigate to object, you are directly navigated to the Properties section.

Next Steps

Setting Properties

Assigning Context and Result

Assigning Top Expression

Setting Properties

Context

The application supplies a context and processes the function using a mode of operation.

Procedure

1. Open the application in the Object Manager panel.

2. Under the Detail section, under the Properties tab, choose the mode of operation in the Mode field.

There are three modes of operation:

Functional mode

Event mode

Functional and Event mode

  Note

If you choose Functional Mode or Functional and Event Mode, a top expression has to be assigned to the function.

In the Event mode, you do not need to assign a top expression to the function.

For more information, see Modes of Operation

3. Enter the context class.

Next Steps

Creating a Function

Assigning Context and Result

This is custom documentation. For more information, please visit SAP Help Portal.

144


10/15/26, 3:15 PM

Assigning Top Expression

Assigning Context and Result

Context

The function can import a context and can return a result after processing. The context and result are optional in the event mode of

operation.

Procedure

1. Open the function in the Object Manager panel.

2. Under the Detail section, choose the Signature tab.

The Signature tab page opens.

3. Assign a context.

You can add an existing data object, a new data object or multiple elements.

Add an Existing Data Object

a. Choose Add Existing Data Object button.

b. In the Object Query dialog box that appears, select the data object and choose Select.

The data object is added as the context.

Add a New Data Object

Choose  Add New Data Object

 Add New Data Object

For more information, see Creating Data Objects

Add Multiple Elements

a. Choose  Add New Data Object

 Add New Elements

b. In the Create New Elements dialog box that appears, select the type from the type column.

c. Select the element type, enter a name and choose Create button.

The new element is added as the context.

4. Assign a result.

This is custom documentation. For more information, please visit SAP Help Portal.

145


10/15/26, 3:15 PM

You can assign a default object, an existing data object or a new object.

Select a Default Object

a. Choose

.

b. In the context menu, choose Default Objects and choose the data object type.

Select an Existing Data Object

a. Choose

.

b. In the context menu, choose Select....

c. In the Object Query dialog box that appears, select the data object.

The data object is added as the result data object.

Select a New Data Object

a. Choose

.

b. In the context menu, choose Create....

c. In the Object Creation dialog box that appears, create the data object.

For more information, see Creating Data Objects

Next Steps

Creating a Function

Assigning Top Expression

Setting Properties

Assigning Top Expression

Context

You need to assign an expression as Top Expression when you choose Functional or Functional and Event mode of operation.

For more information, see Modes of Operation

Procedure

1. Open the function in the Object Manager panel.

2. Assign an existing expression or a new expression as the top expression.

Assign an existing Expression

a. In the Detail section, under Properties tab page, choose the mode of operation.

b. Choose

 next to the Top Expression field.

c. In the context menu, choose Select....

d. In the Object Query dialog box that appears, select the expression from the list.

This is custom documentation. For more information, please visit SAP Help Portal.

146


10/15/26, 3:15 PM

Create an Expression

a. Choose

 next to the Top Expression field.

b. In the context menu, choose Create....

c. In the Object Creation dialog box that appears, enter the following data in the General Data section:

Name

Short Text

d. Select the type of expression from the Type field and choose Create or Create and navigate to object.

  Note
If you choose Create the newly created expression appears next to the Top Expression field.

Next Steps

Creating a Boolean Expression

Creating a BRMS Connector Expression

Creating a Case Expression

Creating a Constant Expression

Creating a DB Lookup Expression

Creating a Decision Table Expression

Creating a Decision Tree Expression

Creating a Dynamic Expression

Creating a Formula Expression

Creating a Function Call Expression

Creating a Loop Expression

Creating a Random Number Expression

Creating a Value Range Expression

Creating a Search Tree Expression

Creating a Static Method Call Expression

Creating a Step Sequence Expression

Creating a XSL Transformation Expression

Creating Expressions

This is custom documentation. For more information, please visit SAP Help Portal.

147


10/15/26, 3:15 PM
Use

This section describes the tasks one needs to perform while creating different types of expressions. If you want to learn more

about the details of each of the different expression types, see Expressions. If you want to set up a custom expression type in order

to handle requirements that are not covered by the predefined BRFplus expression types, see Expression Type.

More Information

Creating a Boolean Expression

Creating a BRMS Connector Expression

Creating a Case Expression

Creating a Constant Expression

Creating a DB Lookup Expression

Creating a Decision Table Expression

Creating a Decision Tree Expression

Creating a Dynamic Expression

Creating a Formula Expression

Creating a Function Call Expression

Creating a Loop Expression

Creating a Random Number Expression

Creating a Search Tree Expression

Creating a Static Method Call Expression

Creating a Step Sequence Expression

Creating a Value Range Expression

Creating a XSL Transformation Expression

Creating a Boolean Expression

Procedure

1. Open the application in the Object Manager panel.

2. Under the Detail section, choose the Contained Objects tab.

The Contained Objects page appears.

3. Choose Expression from the Type field and choose Create Object.

4. In the Object Creation dialog box that appears, choose Boolean in the Type field.

This is custom documentation. For more information, please visit SAP Help Portal.

148


10/15/26, 3:15 PM

5. Enter the following data:

Name

(Optional) Short Text

(Optional) Text

6. Choose Create and navigate to object.

The newly created boolean expression appears in the Object Manager panel.

  Note

If you choose Create the boolean expression appears under the Contained Objects tab.

7. Under the Detail section, choose Template and select the template type.

The following template types are available:

Any operand is true

All operands are true

<1> and <2>

<1> or <2> or <3>

(<1> and <2>) or <3>

(<1> or <2>) and <3>

<1> and <2> and <3>

Choose your own template

The template type which is selected appears next to the Template.

8. Depending on the template selected, add condition to the boolean expression.

You can create a value range expression using the selected data object or expression as the test parameter.

Use Value from Standard Type as Condition

a. Choose

 next to if.

b. In the context menu, choose  Use Direct Value Range From

 Default Objects  and choose the standard

type.

Use Value from an Existing Context Data Object as Condition

a. Choose

 next to if.

b. In the context menu, choose  Use Direct Value Range From

 Other Context Parameter...

.

c. In the Context Query dialog box that appears, select the data object.

Use Value from an Existing Expression as Condition

a. Choose

 next to if.

This is custom documentation. For more information, please visit SAP Help Portal.

149


10/15/26, 3:15 PM

b. In the context menu, choose  Use Direct Value Range From

 Expressions...

.

c. In the Object Query dialog box that appears, enter the name of the expression and choose Search.

The expression appears below the Search button.

d. Select the expression.

You can also directly select an expression or a data object as a condition. The selected expression should have result

of type Boolean and the selected data object should be of type Boolean.

Use Operand from an Existing Expression as Condition

a. Choose

 next to if.

b. In the context menu, choose  Select Operand...

 Select Expressions...

 Select...

.

c. In the Object Query dialog box that appears, enter the name of the expression and choose Search.

The expression appears below the Search button.

d. Select the expression.

Use Operand from an Existing Context Data Object as Condition

a. Choose

 next to if.

b. In the context menu, choose  Select Operand...

 Select Data Object...

 Other Context Parameter...

.

c. In the Context Query dialog box that appears, select the data object.

Use a New Expression as Condition

a. Choose

 next to if.

b. In the context menu, choose Create Expression...

c. In the Object Creation dialog box that appears, create the expression.

For more information, see Creating Expressions

9. Choose the Activate button.

10. Save the expression.

Creating a BRMS Connector Expression

Procedure

1. Open the application in the Object Manager panel.

2. Under the Detail section, choose the Contained Objects tab.

The Contained Objects tab page appears.

3. Choose Expression from the Type field and choose Create Object.

4. In the Object Creation dialog box that appears, choose BRMS Connector in the Type field.

5. Enter the following data:

Name

(Optional) Short Text

This is custom documentation. For more information, please visit SAP Help Portal.

150


10/15/26, 3:15 PM

(Optional) Text

6. Choose Create and navigate to object.

The newly created BRMS Connector expression appears in the Object Manager panel.

  Note
If you choose Create, the BRMS Connector expression appears under the Contained Objects tab.

7. Assign a result data object. You can assign a standard data object type, an existing data object or a new data object.

Select a Standard Type

a. Choose

.

b. In the context menu, choose Default Objects and choose the data object type.

Select an Existing Data Object

a. Choose

.

b. In the context menu, choose Select....

c. In the Object Query dialog box that appears, choose the data object.

Create a New Data Object

a. Choose

.

b. In the context menu, choose Create....

c. In the Object Creation dialog box that appears, create the data object.

For more information, see Creating Data Objects

8. Choose the connection type. You can either choose NetWeaver BRMS Connection or External BRMS Connection.

9. Choose the destination.

The destination needs to be specified in the rules so that the call can be routed correctly.

10. Enter the base currency.

This is custom documentation. For more information, please visit SAP Help Portal.

151


10/15/26, 3:15 PM

11. Add context to the expression. You can either add an existing object or create a new object.

Add an Existing Object

a. Choose Add Existing Object.

b. In the Object Query dialog box that appears, choose the object and choose Select.

Add a New Object

a. Choose Add New Object.

b. In the Object Creation dialog box appears, create the expression.

For more information, see Creating Expressions

12. Assign result parameter. You can assign a standard data object type, an existing result parameter or create a new result

parameter.

Select a Standard Type

a. Choose

.

b. In the context menu, choose Default Objects and choose the data object type.

Select an Existing Result Parameter

a. Choose

.

b. In the context menu, choose Select....

c. In the Object Query dialog box that appears, choose the data object.

Create a New Result Parameter

This is custom documentation. For more information, please visit SAP Help Portal.

152


10/15/26, 3:15 PM

a. Choose

.

b. In the context menu, choose Create....

c. In the Object Creation dialog box that appears, create the data object.

For more information, see Creating Data Objects

13. Choose Generate Vocabulary Schema.

The generated rule XSD is used to define the rule vocabulary in the external BRMS engine.

14. To set connection parameters, choose Connection Parameters tab.

15. Under the Connector Call Parameters section, enter values for the project and the rule set.

16. Choose the Activate button.

17. Save the expression.

Creating a Case Expression

Procedure

1. Open the application in the Object Manager panel.

2. Under the Detail section, choose the Contained Objects tab.

The Contained Objects page appears.

3. Choose Expression from the Type field and choose Create Object.

4. In the Object Creation dialog box that appears, choose Case in the Type field.

5. Enter the following data:

Name

(Optional) Short Text

This is custom documentation. For more information, please visit SAP Help Portal.

153


10/15/26, 3:15 PM

(Optional) Text

6. Choose Create and navigate to object.

The newly created case expression appears in the Object Manager panel.

  Note
If you choose Create the case expression appears under the Contained Objects tab.

7. Choose the result type. You can select return value or perform action.

Select Return Value

a. Choose Return Value in the Result Type field.

b. Assign the result data object. You can select a standard type, an existing data object or create a new data

object.

Select a Standard Type

i. Choose

.

ii. In the context menu, choose Default Objects and choose the data object type.

The element is added as the result data object.

Select an Existing Data Object

i. Choose

.

ii. In the context menu, choose Select....

iii. In the Object Query dialog box that appears, enter the name of the data object in the Object

Name field and choose Search.

The data object appears below the Search button.

iv. Select the data object.

The data object is added as the result data object.

Create a New Data Object

i. Choose

.

ii. In the context menu, choose Create....

iii. In the Object Creation dialog box that appears, create the data object.

For more information, see Creating Data Objects

Select Perform Action

Choose Perform Action in the Result Type field.

An action is added as the result data object.

8. Define the case parameter. You can choose a standard type, an existing data object, expression or create a new expression.

Select a Standard Type

a. Choose

 next to When.

b. In the context menu, choose Default Objects and select the standard type.

Select an Existing Data Object

This is custom documentation. For more information, please visit SAP Help Portal.

154


10/15/26, 3:15 PM

a. Choose

 next to When.

b. In the context menu, choose Other Context Parameter....

c. In the Context Query dialog box that appears, select the data object.

The selected data object is added as a case parameter.

Select an Existing Expression

a. Choose

 next to When.

b. In the context menu, choose Select Other Parameter....

c. In the Object Query dialog box that appears, enter the name of the expression in the Object Name field and

choose Search.

The expression appears below the Search button.

d. Select the expression.

The expression is added as the case parameter.

Create a New Expression

a. Choose

 next to When.

b. In the context menu, choose Create New Parameter....

c. In the Object Creation dialog box that appears, create the expression.

For more information, see Creating Expressions

9. Enter values in the fields next to ...equals.

  Note
If none of the when table test parameters matches the case parameter, an other parameter is evaluated in order to

specify the result.

10. Choose

 next to then perform action.

You can assign an existing action or create a new action.

Select an Existing Action

a. In the context menu, choose Select....

b. In the Object Query dialog box that appears, select the action.

Create an Action

a. In the context menu, choose Create....

b. In the Object Creation dialog box that appears, create the action.

For more information, see Creating Action Types

11. Define an other parameter. You can assign an existing expression, create a new expression or insert a value.

Select an Existing Expression

a. Choose

 next to Otherwise perform action.

b. In the context menu, choose Select....

This is custom documentation. For more information, please visit SAP Help Portal.

155


10/15/26, 3:15 PM

c. In the Object Query dialog box that appears, enter the name of the expression in the Object Name field and

choose Search.

The expression appears below the Search button.

d. Select the expression from the list.

Create a New Expression

a. Choose

 next to Otherwise perform action.

b. In the context menu, choose Create....

c. In the Object Creation dialog box that appears, create the expression.

For more information, see Creating Expressions

12. Choose the Activate button.

13. Save the expression.

Creating a Constant Expression

Context

A constant expression is used to define result values for other expressions.

  Note
A constant expression can take only element data types.

Procedure

1. Open the application in the Object Manager panel.

2. Under the Detail section, choose the Contained Objects tab.

The Contained Objects tab page appears.

3. Choose Expression from the Type field and choose Create Object.

4. In the Object Creation dialog box that appears, choose Constant from the Type field.

The Constant section appears.

5. Enter the following data:

Name

(Optional) Short Text

(Optional) Text

6. Under the Constant section, choose the type of constant from the Type field.

Depending on the type of constant you choose, the fields in which you have to enter values appear.

For more information, see Constant Expression

7. Choose Create and navigate to object.

The result data object appears under the Detail section.

This is custom documentation. For more information, please visit SAP Help Portal.

156


10/15/26, 3:15 PM

By default, the type of the constant selected appears as the result data object.

  Note

If you choose Create, the constant expression appears under the Contained Objects tab. Click the name of the created

object.

8. If you want to change the result data object, choose

.

You can select a standard element, select an existing data object or create a new result data object.

Select a Standard Type

In the context menu, choose Default Objects and choose the data object type.

The element is added as the result data object.

Select an Existing Data Object

a. In the context menu, choose Select...

b. In the Object Query dialog box that appears, select the data object.

The data object is added as the result data object.

Create a New Data Object

a. In the context menu, choose Create....

b. In the Object Creation dialog box that appears, create the data object.

For more information, see Creating Data Objects

9. Choose the Activate button.

10. Save the expression.

Creating a DB Lookup Expression

Procedure

1. Open the application in the Object Manager panel.

2. Under the Detail section, choose the Contained Objects tab.

The Contained Objects page appears.

3. Choose Expression from the Type field and choose Create Object.

4. In the Object Creation dialog box that appears, choose DB Lookup in the Type field.

5. Enter the following data:

Name

(Optional) Short Text

(Optional) Text

6. Choose Create and navigate to object.

The newly created DB Lookup expression appears in the Object Manager panel.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

157


10/15/26, 3:15 PM

If you choose Create the DB Lookup expression appears under the Contained Objects tab.

7. Select the mode.

You can choose data retrieval mode, aggregation mode or existence check mode.

Select Data Retrieval Mode

In this mode, the data is retrieved from the database table.

a. Choose All Entries or Single Entry.

b. Enter the name of the table in the text box and press  Enter .

c. Assign a condition using the fields of the database table.

You can select an existing data object, create a new data object or create a result from the table.

Select an Existing Data Object

i. Choose

.

ii. In the context menu, choose Select....

iii. In the Object Query dialog box that appears, select the data object.

Create a New Data Object

i. Choose

.

ii. In the context menu, choose Create....

iii. In the Object Creation dialog box that appears, create the data object.

For more information, see Creating Data Objects

Create Result from Table

i. Choose

.

ii. In the context menu, choose Create Result From Table.

iii. In the dialog box that appears with the field of the database table, select the required fields.

iv. Enter a name for the structure, table or element.

Select Aggregation Mode

In this mode, the result of the aggregation is returned from the database table.

a. Choose Aggregation from the Selection Mode field.

b. Enter the name of the table in the text box and press  Enter .

c. Choose the aggregation type. You can choose maximum, minimum, average, count or sum.

d. Choose Distinct or All.

e. Assign a condition using the fields of the database table. You can select an existing data object or create a

new data object.

Select an Existing Data Object

i. Choose

.

ii. In the context menu, choose Select....

This is custom documentation. For more information, please visit SAP Help Portal.

158


10/15/26, 3:15 PM

iii. In the Object Query dialog box that appears, select the data object.

Create a New Data Object

i. Choose

.

ii. In the context menu, choose Create....

iii. In the Object Creation dialog box that appears, create the data object.

For more information, see Creating Data Objects

Select Existence Check Mode

In this mode, the result object is assigned true or false based on whether atleast one entry satisfies the WHERE

condition that exists in the DDIC table.

a. Choose Existence Check from the Selection Mode field.

b. Enter the name of the table in the text box and press  Enter .

c. Assign a condition using the fields of the database table.

You can select an existing data object, create a new data object or choose a Boolean.

Select an Existing Data Object

i. Choose

.

ii. In the context menu, choose Select....

iii. In the Element Query dialog box that appears, enter the name of the data object and choose

Search.

The data object appears under the Search button.

iv. Select the data object.

Create a New Data Object

i. Choose

.

ii. In the context menu, choose Create....

iii. In the Object Creation dialog box that appears, create the data object.

For more information, see Creating Data Objects

Select a Boolean

i. Choose

.

ii. In the context menu, choose Boolean.

8. Choose the Activate button.

9. Save the expression.

Creating a Decision Table Expression

Procedure

1. Open the application in the Object Manager panel.

This is custom documentation. For more information, please visit SAP Help Portal.

159


10/15/26, 3:15 PM

2. Under the Detail section, choose the Contained Objects tab.

The Contained Objects tab page appears.

3. Choose Expression from the Type field and choose Create Object.

4. In the Object Creation dialog box that appears, choose Decision Table in the Type field.

5. Enter the following data:

Name

(Optional) Short Text

(Optional) Text

6. Choose Create and navigate to object.

The newly created decision table expression appears in the Object Manager panel.

  Note

If you choose Create, the decision table expression appears under the Contained Objects tab.

7. Assign the result data object. You can assign a standard data object, an existing data object or a new data object.

Select a Standard Type

a. Choose

.

b. In the context menu, choose Default Objects and choose the data object type.

Select an Existing Data Object

a. Choose

.

b. In the context menu, choose Select....

c. In the Object Query dialog box that appears, select the data object.

Create a New Data Object

a. Choose

.

b. In the context menu, choose Create....

The result column for the decision table is added automatically when the Column is result is selected.

c. In the Object Creation dialog box that appears, create the data object.

For more information, see Creating Data Objects

  Note

If you are creating a decision table expression as the top expression in a function, the assigned result data object

of the table should either be of the same type as assigned to the function or should be exactly the same object as

used in the function.

8. Add columns to the decision table. Choose Append Column or Insert Column depending on where you want to add the

column.

You can add a function context, data object, expression or action as column.

  Note

To add a column at the end of the table, choose Append Column.

This is custom documentation. For more information, please visit SAP Help Portal.

160


10/15/26, 3:15 PM

To insert a column at a current selection, choose Insert Column.

Add a Function Context

a. Choose  Append Column

 From Context Data Objects...

.

b. In the Context Query dialog box that appears, select the context and choose Select.

Add Any Other Context

a. Choose  Append Column

 From Other Data Objects...

.

b. In the Object Query dialog box that appears, select the data object and choose Select.

Add an Existing Expression

a. Choose  Append Column

 Select Expression...

.

b. In the Object Query dialog box that appears, select the expression and choose Select.

Add a New Expression

a. Choose  Append Column

 Create Expression...

b. In the Object Creation dialog box that appears, create the expression.

For more information, see Creating Expressions

Add an Action

Choose  Append Column

 Create Actions Column...

.

The action column appears in the decision table.

9. Define the decision table by adding rows. To add rows, choose Append Line under the Table Data section.

10. Add values to the decision table. You can directly add values or define an expression as the value.

  Note

You can also import data from an excel file.

For more information, see Exchanging Decision Table Data With Microsoft Excel

Add Value

a. Choose ... next to

.

b. Enter the relevant values and choose Done.

Add an Existing Expression as Value

a. Choose

.

b. In the context menu, choose Select....

c. In the Object Query dialog box, select the expression.

Add a New Expression as Value

a. Choose

.

b. In the context menu, choose Create....

c. In the Object Creation dialog box that appears, create the expression.

This is custom documentation. For more information, please visit SAP Help Portal.

161


10/15/26, 3:15 PM

For more information, see Creating Expressions

11. Choose the Activate button.

12. Save the decision table.

Creating a Decision Tree Expression

Procedure

1. Open the application in the Object Manager panel.

2. Under the Detail section, choose the Contained Objects tab.

The Contained Objects tab page appears.

3. Choose Expression from the Type field and choose Create Object.

4. In the Object Creation dialog box that appears, choose Decision Tree in the Type field.

5. Enter the following data:

Name

(Optional) Short Text

(Optional) Text

6. Choose Create and navigate to object.

The newly created decision tree expression appears in the Object Manager panel.

  Note

If you choose Create the decision tree expression appears under the Contained Objects tab.

7. Choose the result type. You can select return value or perform action.

Select Return Value

a. Choose Return Value in the Result Type field.

b. Assign the result data object.

You can assign a standard data object, an existing data object or a new data object.

Select a Standard Type

i. Choose

.

This is custom documentation. For more information, please visit SAP Help Portal.

162

ii. In the context menu, choose Default Objects and choose the data object type.


10/15/26, 3:15 PM

Select an Existing Data Object

i. Choose

.

ii. In the context menu, choose Select....

iii. In the Object Query dialog box that appears, select the data object and choose Select.

Create a New Data Object

i. Choose

.

ii. In the context menu, choose Create....

iii. In the Object Creation dialog box that appears, create the data object.

For more information, see Creating Data Objects

  Note

The result data object can be an element, a structure or a table data object.

8. Assign a root node to the decision tree. You can choose direct input, an existing expression or a new expression.

Select Direct Input

a. In the context menu of the node, choose  Set Condition

 Direct Input

.

b. Choose

 to define the incoming parameter.

You can choose a standard type, an existing data object or an expression.

Select a Standard Type

In the context menu, choose Default Objects and select the standard type.

Select an Existing Data Object

i. In the context menu, choose Other Context Parameter....

ii. In the Context Query dialog box that appears, select the data object.

Select an Existing Expression

i. In the context menu, choose Expressions.

ii. In the Object Query dialog box that appears, select the expression.

c. Choose the comparison operator and enter values.

d. Choose Done.

Select an Existing Expression

a. In the context menu of the node, choose  Set Condition...

 Select...

.

b. In the Object Query dialog box that appears, select the expression.

Create a New Expression

a. In the context menu of the node, choose  Set Condition...

 Create...

.

b. In the Object Creation dialog box that appears, create the expression.

For more information, see Creating Expressions

This is custom documentation. For more information, please visit SAP Help Portal.

163


10/15/26, 3:15 PM

  Note

The root node can only be a condition.

The selected expression is set as the root node and two child nodes appear under the root node.

9. Add a condition or a result to the child node. You can assign an existing expression or a new expression to the child node

depending upon the outcome of the condition in the root node.

Assign an Existing Expression as a Result

a. In the context menu of the positive child node, choose  Set Result...

 Select...

.

b. In the Object Query dialog box that appears, select the expression.

Assign a New Expression as a Result

a. In the context menu of the positive child node, choose  Set Result...

 New...

b. In the Object Creation dialog box that appears, create the expression.

For more information, see Creating Expressions

Choose Direct Input

a. In the context menu of the node, choose  Set Condition

 Direct Input

.

b. Choose

.

You can choose a standard type, an existing data object or an expression.

Select a Standard Type

In the context menu, choose Default Objects and select the standard type.

Select an Existing Data Object

i. In the context menu, choose Other Context Parameter....

ii. In the Context Query dialog box that appears, select the data object.

Select an Existing Expression

i. In the context menu, choose Expressions.

ii. In the Object Query dialog box that appears, select the expression.

c. Choose the comparison operator and enter values.

d. Choose Done.

Assign an Existing Expression as a Condition

a. In the context menu of the negative child node, choose  Set Condition...

 Select...

This is custom documentation. For more information, please visit SAP Help Portal.

164


10/15/26, 3:15 PM

b. In the Object Query dialog box that appears, select the expression and choose Select.

Assign a New Expression as a Condition

a. In the context menu of the negative child node, choose  Set Condition...

 Create...

b. In the Object Creation dialog box that appears, create the expression.

For more information, see Creating Expressions

  Note

There is no restriction to the level of nodes that you can create in the decision tree.

All leaf nodes have to be result nodes.

10. Activate the expression.

11. Save the expression.

Creating a Dynamic Expression

Procedure

1. Open the application in the Object Manager panel.

2. Under the Detail section, choose the Contained Objects tab

The Contained Objects page appears.

3. Choose Expression from the Type field and choose Create Object.

4. In the Object Creation dialog box that appears, choose Dynamic Expression in the Type field.

5. Enter the following data:

Name

(Optional) Short Text

(Optional) Text

6. Choose Create and navigate to object.

The newly created dynamic expression appears in the Object Manager panel.

  Note

If you choose Create the dynamic expression appears under the Contained Objects tab.

7. Assign result data object. You can select a standard type, an existing data object or create a new data object.

Select a Standard Type

a. Choose

.

b. In the context menu, choose Default Objects and choose the data object type.

Select an Existing Data Object

a. Choose

.

b. In the context menu, choose Select....

This is custom documentation. For more information, please visit SAP Help Portal.

165


10/15/26, 3:15 PM

c. In the Object Query dialog box that appears, select the data object.

The data object is added as the result data object.

Create a New Data Object

a. Choose

.

b. In the context menu, choose Create....

c. In the Object Creation dialog box that appears, create the data object.

For more information, see Creating Data Objects

8. Choose the mode. You can choose Complete context but not expression variable or Matching Context.

The Complete context but not expression variable mode forwards the available context to the dynamically determined

expression. The Matching Context mode forwards only the matching context objects.

9. Choose the called expression. You can select an existing expression or create a new expression.

Select an Existing Expression

a. Choose

.

b. In the context menu, choose Select....

c. In the Object Query dialog box that appears, select the expression.

Create a New Expression

a. Choose

.

b. In the context menu, choose Create....

c. In the Object Creation dialog box that appears, create the expression.

For more information, see Creating Expressions

10. Activate the expression.

11. Save the expression.

Creating a Formula Expression

Procedure

1. Open the application in the Object Manager panel.

2. Under the Detail section, choose the Contained Objects tab.

The Contained Objects tab page appears.

3. Choose Expression from the Type field and choose Create Object.

4. In the Object Creation dialog box that appears, choose Formula from the Type field.

5. Enter the following data:

Name

(Optional) Short Text

(Optional) Text

6. Choose Create & Navigate to Object.

This is custom documentation. For more information, please visit SAP Help Portal.

166


10/15/26, 3:15 PM

  Note

If you choose Create button, the created formula object appears under the Contained Objects tab.

7. Add the result data object. You can select a standard type, create a new data object or add an existing data object.

Select a Standard Type

a. Choose

.

b. In the context menu, choose Default Objects and choose the data object type.

Select an Existing Data Object

a. Choose

.

b. In the context menu, choose Select....

c. In the Context Query dialog box that appears, select the data object.

Create a New Data Object

a. Choose

.

b. In the context menu, choose Create....

c. In the Object Creation dialog box that appears, create the data object.

For more information, see Creating Data Objects

8. Create the formula using expressions, data objects, mathematical and logical operators.

  Example

If you want to create a formula, 3*1, then in the formula builder,

a. Choose Number.

b. In the Insert dialog box that appears, enter 3 and choose OK.

The number 3 appears in the Formula field.

This is custom documentation. For more information, please visit SAP Help Portal.

167


10/15/26, 3:15 PM

c. Choose *.

d. Choose Number.

In the Insert dialog box that appears, enter 1 and choose OK.

9. You can also create the formula in the expert mode.

a. Choose Switch to Expert Mode.

A text box appears next to the Formula field.

b. You can insert expressions, data objects, string, number, amount, quantity and comment in the formula.

In the context menu of the text box:

To create an expression.

i. Choose

Insert Expression

 Create .

ii. In the Object Creation dialog box that appears, create the expression.

For more information, see Creating Expressions

To select an existing expression.

i. Choose

Insert Expression

 Select

.

ii. In the Object Query dialog box that appears, select the expression.

To create a data object.

i. Choose

Insert Data Object

 Create .

ii. In the Object Creation dialog box that appears, create the data object.

For more information, see Creating Data Objects

To select an existing data object.

i. Choose

Insert Data Object

 Select

.

ii. In the Context Query dialog box that appears, select the data object.

This is custom documentation. For more information, please visit SAP Help Portal.

168


10/15/26, 3:15 PM

  Note

You can also create complex formulas using nested operands.

10. Choose the Activate button.

11. Save the expression.

Creating a Function Call Expression

Procedure

1. Open the application in the Object Manager panel.

2. Under the Detail section, choose the Contained Objects tab.

The Contained Objects tab page opens.

3. Choose Expression from the Type field and choose Create Object.

4. In the Object Creation dialog box that appears, choose Function Call from the Type field.

5. Enter the following data:

Name

(Optional) Short Text

(Optional) Text

6. Choose Create and navigate to object.

  Note
If you choose Create button, the function call expression appears under the Contained Objects tab.

7. Assign result data object.

You can assign a standard data object, an existing data object or create a new data object.

Select a Standard Type

a. Choose

.

This is custom documentation. For more information, please visit SAP Help Portal.

169


10/15/26, 3:15 PM

b. In the context menu, choose Default Objects and choose the data object type.

Select an Existing Data Object

a. Choose

.

b. In the context menu, choose  Select...

c. In the Object Query dialog box that appears, select the data object.

Create a New Data Object

a. Choose

.

b. In the context menu, choose Create....

c. In the Object Creation dialog box that appears, create the data object.

For more information, see Creating Data Objects

8. Assign target function to the expression.

You can select a standard type, create a new function or use an existing function as the target function.

Select a Standard Type

a. Choose

.

b. In the context menu, choose Default Objects and select the standard type.

Create a New Function

a. Choose

.

b. In the context menu, choose Create...

c. In the Object Creation dialog box that appears, create the function.

For more information, see Creating a Function

d. Assign top expression to the function.

For more information, see Assigning Top Expression

e. Assign context and result to the function.

For more information, see Assigning Context and Result

Select an Existing Function

a. Choose

.

b. In the context menu, choose Select....

c. In the Object Query dialog box that appears, select the function.

The context data object of the target function appears under the Target Function Context Data Object in the

Mapping section.

This is custom documentation. For more information, please visit SAP Help Portal.

170


10/15/26, 3:15 PM

9. Map the context objects between the source expression and the target function.

You can choose a data object or an expression.

Select a Standard Type

a. Choose

.

b. In the context menu, choose Default Objects and select the standard type.

Choose an Existing Data Object

a. Choose

 under the Source Context Data Object/Expression column.

b. In the context menu, choose Other Context Parameter....

c. In the Context Query dialog box that appears, select the data object.

The context data object appears under Target Function Context Data Object in the Mapping section.

Choose an Existing Expression

a. Choose

.

b. In the context menu, choose Expressions....

c. In the Object Query dialog box that appears, select the expression.

The context expression appears under Target Function Context Data Object in the Mapping section.

Create a New Expression

a. Choose

.

b. In the context menu, choose Create Expression....

c. In the Object Creation dialog box that appears, create the expression.

For more information, see Creating Expressions

10. Activate the expression.

11. Save the expression.

Creating a Loop Expression

Procedure

This is custom documentation. For more information, please visit SAP Help Portal.

171


10/15/26, 3:15 PM

1. Open the application in the Object Manager panel.

2. Under the Detail section, choose the Contained Objects tab.

The Contained Objects page appears.

3. Choose Expression from the Type field and choose Create Object.

4. In the Object Creation dialog box that appears, choose Loop in the Type field.

5. Enter the following data:

Name

(Optional) Short Text

(Optional) Text

6. Choose Create and navigate to object.

The newly created loop expression appears in the Object Manager panel.

  Note

If you choose Create the loop expression appears under the Contained Objects tab.

7. Choose the result type. You can select return value or perform action.

Select Return Value

a. Choose Return Value in the Result Type field.

b. Assign the result data object. You can select a standard type, an existing data object or create a new data

object.

Select a Standard Type

i. Choose

.

ii. In the context menu, choose Default Objects and choose the data object type.

Select an Existing Data Object

i. Choose

.

ii. In the context menu, choose Select....

iii. In the Object Query dialog box that appears, enter the name of the data object in the Object

Name field and choose Search.

The data object appears below the Search button.

iv. Select the data object.

Create a New Data Object

i. Choose

.

ii. In the context menu, choose Create....

iii. In the Object Creation dialog box that appears, create the data object.

For more information, see Creating Data Objects

Select Perform Action

Choose Perform Action in the Result Type field.

This is custom documentation. For more information, please visit SAP Help Portal.

172


10/15/26, 3:15 PM

An action is added as the result data object.

8. Select the loop mode.

Choose Repeat... Times... Mode

a. Choose Repeat...Times... from the Loop Mode field.

b. Enter value in the Do following operations field.

c. Assign rule for the operation.

Choose Do... Until... Mode

a. Choose Do...Until... from the Loop Mode field.

b. Assign rule for the operation.

c. Assign the exit condition. You can select an existing expression or create a new expression.

Select an Existing Expression

i. Choose

 next to Until under the Detail section.

ii. In the context menu, choose Select....

iii. In the Object Query dialog box that appears, enter the name of the expression in the Object

Name field and choose Search.

The expression appears under the Search button.

iv. Select the expression.

Create a New Expression

i. Choose

 next to Until under the Detail section.

ii. In the context menu, choose Create...

iii. In the Object Creation dialog box that appears, create the expression.

For more information, see Creating Expressions

Choose While... Do... Mode

a. Choose While...Do... from the Loop Mode field.

b. Assign the exit condition. You can select an existing expression or create a new expression.

Select an Existing Expression

i. Choose

.

ii. In the context menu, choose Select....

iii. In the Object Query dialog box that appears, enter the name of the expression in the Object

Name field and choose Search.

The expression appears under the Search button.

iv. Select the expression.

Create a New Expression

i. Choose

.

ii. In the context menu, choose Create....

This is custom documentation. For more information, please visit SAP Help Portal.

173


10/15/26, 3:15 PM

iii. In the Object Creation dialog box that appears, create the expression.

For more information, see Creating Expressions

c. Assign rule for the operation.

Choose For Each Entry in... Mode

a. Choose For Each Entry in... from the Loop Mode field.

b. Assign the exit condition. Choose

 next to For Each Entry in under the Detail section.

c. In the context menu, choose Select....

d. In the Object Query dialog box that appears, select the object.

9. Assign a rule.

Select an Existing Rule

a. Choose

 next to Operations section.

b. In the context menu, choose  Add Rule at First Position

 Select an Existing Rule...

.

c. In the Object Query dialog box that appears, enter the name of the rule and choose Search.

The rule appears below the Search button.

d. Choose the rule.

Create a New Rule

a. Choose

 next to Operations section.

b. In the context menu, choose  Add Rule at First Position

 Create Rule...

A new rule appears under the Operations section.

For more information, see Creating a Rule

10. Activate the expression.

11. Save the expression.

Creating a Random Number Expression

Procedure

1. Open the application in the Object Manager panel.

2. Under the Detail section, choose the Contained Objects tab.

The Contained Objects tab page appears.

3. Choose Expression from the Type field and choose Create Object.

4. In the Object Creation dialog box that appears, choose Random Number in the Type field.

5. Enter the following data:

Name

(Optional) Short Text

(Optional) Text

This is custom documentation. For more information, please visit SAP Help Portal.

174


10/15/26, 3:15 PM

6. In the Random Number section that appears, choose the mode.

You can either choose Number or Probability mode.

In the number mode, a random number within a specified range is returned.

In the probability mode, the expression returns a Boolean true value, if the specified probability between 0 and 1 is met.

Select Number Mode

a. Choose Number from the Mode field.

b. Enter values in the Minimum and Maximum fields.

Select Probability Mode

a. Choose Probability from the Mode field.

b. Enter value between 0 and 1 in the Probability field.

7. Choose Create and navigate to object.

The random number expression appears in the Object Manager panel.

  Note

If you choose Create, the random number expression appears under the Contained Objects tab.

8. Choose Show Result Data Object.

A default data object is set automatically depending on the mode selected.

For number mode, a data object of type number is set whereas a data object of type Boolean is set for probability mode.

You can also assign a standard type, an existing data object or create a new data object as the result data object.

Select a Standard Type

a. Choose

.

b. In the context menu, choose Default Objects and choose the data object type.

  Note

There are two standard types, number and boolean, which are available depending on the mode you

choose.

Select an Existing Data Object

a. Choose

.

b. In the context menu, choose Select....

c. In the Object Query dialog box that appears, select the data object.

Create a New Data Object

a. Choose

.

b. In the context menu, choose Create....

c. In the Object Creation dialog box that appears, create the data object.

For more information, see Creating Data Objects

9. (Optional) You can also use expressions as values for the modes.

This is custom documentation. For more information, please visit SAP Help Portal.

175


10/15/26, 3:15 PM

a. Choose the Switch to Referencing Mode button.

The values present in the value field will be discarded when you switch to referencing mode.

The

 icon replaces the value field.

b. Select an existing expression or create a new expression.

Select Other Context Parameters

i. Choose

.

ii. In the context menu, choose Other Context Parameters....

iii. In the Context Query dialog box that appears, select the data object.

Select an Existing Expression

i. Choose

.

ii. In the context menu, choose Expressions....

iii. In the Object Query dialog box that appears, select the expression.

Create an Expression

i. Choose

.

ii. In the context menu, choose Create Expression....

iii. In the Object Creation dialog box that appears, create the expression.

For more information, see Creating Expressions

10. Activate the expression.

11. Save the expression.

Creating a Search Tree Expression

Procedure

1. Open the application in the Object Manager panel.

2. Under the Detail section, choose the Contained Objects tab.

The Contained Objects tab page appears.

3. Choose Expression from the Type field and choose Create Object.

4. In the Object Creation dialog box that appears, choose Search Tree from the Type field.

5. Enter the following data:

Name

(Optional) Short Text

(Optional) Text

6. Choose Create and navigate to object.

The search tree opens in the Object Manager panel.

  Note

This is custom documentation. For more information, please visit SAP Help Portal.

176


10/15/26, 3:15 PM

If you choose Create, the created rule object appears under the Contained Objects tab.

7. Choose the return type. you can select return value or perform action.

Select Return Value

a. Choose Return Value in the Result Type field.

b. Assign the result data object.

You can assign a standard type, an existing data object or create a new data object as the result data object.

Select a Standard Type

i. Choose

.

ii. In the context menu, choose Default Objects and choose the standard data object.

Select an Existing Data Object

i. Choose

.

ii. In the context menu, choose Select....

iii. In the Object Query dialog box that appears, select the data object and choose Select.

  Note

To return multiple matched results, select Return all matches found checkbox.

The assigned result data object should be a table data object.

Create a New Result Data Object

i. Choose

.

ii. In the context menu, choose Create....

iii. In the Object Creation dialog box that appears, create a data object.

For more information, see Creating Data Objects.

Select Perform Action

Choose Perform Action in the Result Type field.

An action is added as the result data object.

8. Assign a condition to the root node.

Under the condition column, you can select the direct input option, an existing expression or create a new expression.

Select Direct Input

a. In the context menu of the root node, choose  Set Condition...

 Direct Input

.

b. Choose

 to define the incoming parameter.

This is custom documentation. For more information, please visit SAP Help Portal.

177


10/15/26, 3:15 PM

You can choose a standard type, an existing data object or an expression.

Select a Standard Type

In the context menu, choose Default Objects and select the standard type.

Select an Existing Data Object

i. In the context menu, choose Other Context Parameter....

ii. In the Context Query dialog box that appears, select the data object.

Select an Existing Expression

i. In the context menu, choose Expressions.

ii. In the Object Query dialog box that appears, select the expression.

c. Choose the comparison operator and enter the values.

d. Choose Done.

Select an Existing Expression

a. In the context menu of the root node, choose  Set Condition...

 Select...

.

b. In the Object Query dialog box that appears, select the expression.

Create a New Expression

a. In the context menu of the root node, choose  Set Condition...

 Create...

.

b. In the Object Creation dialog box that appears, create a new expression.

For more information, see Creating Expressions

9. Assign a result to the root node.

Under the result column, you can select an existing expression or create a new expression.

Select an Existing Expression

a. In the context menu of the root node, choose  Set Result

 Select...

.

b. In the Object Query dialog box that appears, select an expression.

Create a New Expression

a. In the context menu of the root node, choose  Set Result

 Create...

.

b. In the Object Creation dialog box that appears, create an expression.

For more information, see Creating Expressions

10. Create a child node.

In the context menu of the root node, choose  Node Operations

 Create Child node .

  Note
You have to create all required child nodes before you assign a condition and result to the first created child node.

11. Assign conditions and results to the child node.

12. Activate the expression.

13. Save the expression.

This is custom documentation. For more information, please visit SAP Help Portal.

178


10/15/26, 3:15 PM

Creating a Static Method Call Expression

Procedure

1. Open the application in the Object Manager panel.

2. Under the Detail section, choose the Contained Objects tab.

The Contained Objects page appears.

3. Choose Expression from the Type field and choose Create Object.

4. In the Object Creation dialog box that appears, choose Static Method Call in the Type field.

5. Enter the following data:

Name

(Optional) Short Text

(Optional) Text

6. Choose Create and navigate to object.

The newly created static method call expression appears in the Object Manager panel.

  Note

If you choose Create the static method call expression appears under the Contained Objects tab.

7. Assign result data object. You can select a standard type, an existing data object or create a new data object.

Select a Standard Type

a. Choose

.

b. In the context menu, choose Default Objects and choose the data object type.

Select an Existing Data Object

a. Choose

.

b. In the context menu, choose Select....

c. In the Object Query dialog box that appears, select the data object.

The data object is added as the result data object.

Create a New Data Object

a. Choose

.

b. In the context menu, choose Create....

c. In the Object Creation dialog box that appears, create the data object.

For more information, see Creating Data Objects

8. Enter the name of the class or choose

 in the Class Name field.

9. In the list that appears, select a relevant class and choose OK.

The selected class is added.

10. Add sub-expression to the expression. You can choose an existing expression or create a new expression.

Select an Existing Expression

This is custom documentation. For more information, please visit SAP Help Portal.

179


10/15/26, 3:15 PM

a. Choose Select Expression.

b. In the Object Query dialog box that appears, select the expression.

Create a New Expression

a. Choose Create Expression.

b. In the Object Creation dialog box that appears, create the expression.

For more information, see Creating Expressions

11. Activate the expression.

12. Save the expression.

Creating a Step Sequence Expression

Procedure

1. Open the application in the Object Manager panel.

2. Under the Detail section, choose the Contained Objects tab.

The Contained Objects tab page opens.

3. Choose Expression from the Type field and choose Create Object.

4. In the Object Creation dialog box that appears, Choose Step Sequence in the Type field.

5. Enter the following data:

Name

(Optional) Short Text

(Optional) Text

6. Choose Create and navigate to object.

The step sequence expression appears in the Object Manager panel.

  Note

If you choose Create the newly created step sequence expression appears under Contained Objects tab page.

This is custom documentation. For more information, please visit SAP Help Portal.

180


10/15/26, 3:15 PM

7. Assign a result data object.

You can assign a standard type, select an existing data object or create a new data object as the result data object.

Select a Standard Type

a. Choose

b. In the context menu, choose Default Objects and choose the data object type.

Select an Existing Data Object

a. Choose

.

b. In the context menu, choose Select...

c. In the Object Query dialog box that appears, select the data object.

Create a New Result Data Object

a. Choose

b. In the context menu, choose Create....

c. In the Object Creation dialog box that appears, create a new object.

For more information, see Creating Data Objects

8. Assign sequence of functions. Choose Insert Step.

A new step appears in the table.

  Note

Before a step is processed, the corresponding pre-condition is evaluated. The pre-condition is an expression which has

to return a boolean value. If the value of the pre-condition is evaluated as true, the corresponding step will be skipped.

9. (Optional) Add a pre-condition.

You can add a standard type, an existing expression or a new expression as the pre-condition.

Select a Standard Type

a. Choose

.

b. In the context menu, choose Default Objects and choose the standard type.

Select an Existing Expression

a. Choose

.

b. In the context menu, choose Select.

c. In the Object Query dialog box that appears, select the expression.

Create a New Expression

a. Choose

.

b. In the context menu, choose Create....

This is custom documentation. For more information, please visit SAP Help Portal.

181


10/15/26, 3:15 PM

c. In the Object Creation dialog box that appears, create the expression.

For more information, see Creating Expressions

10. Add a function.

Select a Standard Type

a. Choose

.

b. In the context menu, choose Default Objects and choose the standard type.

Select an Existing Function

a. Choose

.

b. In the context menu, choose Select....

c. In the Object Query dialog box that appears, select the function.

Create a New Function

a. Choose

.

b. In the context menu, choose Create...

c. In the Object Creation dialog box that appears, create the function.

For more information, see Creating a Function

11. (Optional) You can also add an exit condition.

You can create a new expression or select an existing expression.

  Note

Exit conditions have to be expressions with a boolean result data object.

Select a Standard Type

a. Choose

.

b. In the context menu, choose Default Objects and choose the standard type.

Select an Existing Expression

a. Choose

.

b. In the context menu, choose Select....

c. In the Object Query dialog box that appears, select the expression.

Create a New Expression

a. Choose

.

b. In the context menu, choose Create....

c. In the Object Creation dialog box that appears, create the expression

For more information, see Creating Expressions

12. Assign content in the Content of the Work Area field.

You can add an existing data object or a new data object.

Add an Existing Data Object

This is custom documentation. For more information, please visit SAP Help Portal.

182


10/15/26, 3:15 PM

a. Choose Add existing Data Object.

b. In the Object Query dialog box that appears, select the data object and choose Select.

Create a New Data Object

a. Choose Add new Data Object button.

b. In the Object Creation dialog box that appears, create the data object.

For more information, see Creating Data Objects

13. Activate the expression.

14. Save the expression.

Creating a Value Range Expression

Procedure

1. Open the application in the Object Manager panel.

2. Under the Detail section, choose the Contained Objects tab.

3. In the Contained Objects tab page that appears, choose Expression from the Type field and choose Create Object.

4. In the Object Creation dialog box that appears, choose Value Range in the Type field.

5. Enter the following data:

Name

(Optional) Short Text

(Optional) Text

6. Choose Create and navigate to object.

The range expression appears in the Object Manager panel.

  Note
If you choose Create the value range expression appears under Contained Objects tab.

7. Define the incoming parameter. You can choose a standard type, an existing data object or expression as the incoming

parameter.

Select a Standard Type

a. Choose

.

b. In the context menu, choose Default Objects and choose the standard type.

Select an Existing Data Object

a. Choose

.

b. In the context menu, choose Other Context Parameters....

c. In the Object Query dialog box that appears, select the data object.

Select an Existing Expression

a. Choose

.

This is custom documentation. For more information, please visit SAP Help Portal.

183


10/15/26, 3:15 PM

b. In the context menu, choose Expressions....

c. In the Object Query dialog box that appears, enter the name of the expression in the Object Name field and

choose Search.

The expression appears under the Search button.

d. Select the expression.

8. Under Detail section, choose the comparison operator and enter the value for the incoming parameter.

9. Activate the expression.

10. Save the expression.

Creating a XSL Transformation Expression

Procedure

1. Open the application in the Object Manager panel.

2. Under the Detail section, choose the Contained Objects tab.

The Contained Objects tab page appears.

3. Choose Expression from the Type field and choose Create Object.

4. In the Object Creation dialog box that appears, choose XSL Transformation in the Type field.

5. Enter the following data:

Name

(Optional) Short Text

(Optional) Text

6. Choose Create and navigate to object.

The XSL transformation expression appears in the Object Manager panel.

  Note
If you choose Create the XSL transformation expression appears under the Contained Objects tab.

7. Choose Show result data object. You can assign a standard type, select an existing data object or create a new data object

as the result data object.

Select a Standard Type

a. Choose

.

b. In the context menu, choose Default Objects and choose the data object type.

This is custom documentation. For more information, please visit SAP Help Portal.

184


10/15/26, 3:15 PM

Select an Existing Data Object

a. Choose

.

b. In the context menu, choose Select....

c. In the Object Query dialog box that appears, select the data object.

The selected data object is added as the result for the XSL transformation expression.

Create a New Data Object

a. Choose

.

b. In the context menu, choose Create....

c. In the Object Creation dialog box that appears, create the data object.

For more information, see Creating Data Objects

8. Choose Add Parameter button.

A new line appears in the Parameter for XSL Transformation table. You can assign a standard type, an existing data object

or an expression or a new expression as the parameter.

Select a Standard Type

a. Choose

.

b. In the context menu, choose Default Objects and choose the standard type.

Select an Existing Data Object

a. Choose

.

b. In the context menu, choose Other Context Parameter....

c. In the Object Query dialog box that appears, select the data object.

The selected data object is added as the parameter for the XSL transformation expression.

Select an Existing Expression

a. Choose

.

b. In the context menu, choose Select Expression....

c. In the Object Query dialog box that appears, select the expression and choose Select.

The selected expression is added as the parameter for the XSL transformation expression.

Create a New Expression

a. Choose

.

This is custom documentation. For more information, please visit SAP Help Portal.

185


10/15/26, 3:15 PM

b. In the context menu, choose Expressions....

c. In the Object Creation dialog box that appears, create the expression.

For more information, see Creating Expressions

9. Activate the expression.

10. Save the expression.

Creating an Expression Type

Procedure

1. Open the application in the Object Manager panel.

2. Under the Detail section, choose the Contained Objects tab.

3. In the Contained Objects tab page that appears, choose Expression Type from the Type field and choose Create Object.

4. In the Object Creation dialog box that appears, enter the following data:

Name

(Optional) Short Text

(Optional) Text

5. Choose Create and navigate to object.

The newly created expression type appears in the Object Manager panel.

  Note

If you choose Create the newly created expression type appears under the Contained Objects tab page.

6. In the Detail section, enter the following data:

Class

Enter the name of the class that implements the interface.

Interface

Enter the name of the interface which contains the specific attributes for the expression type.

Query Class

Enter the query class. Query class provides an interface that searches for objects and returns details of the object

which satisfies the selection criteria.

UI Class

The UI class provides a corresponding expression type object needed to create the expression type.

Data Exchange Class

7. Activate the expression type.

8. Save the expression type.

Creating Data Objects

This is custom documentation. For more information, please visit SAP Help Portal.

186


10/15/26, 3:15 PM
Use

You can build a context or result object using different data objects. The data objects represent fields, structures and table in

BRFplus.

There are three types of data objects:

Element Data Object

Structure Data Object

Table Data Object

More Information

Creating an Element Data Object

Creating a Structure Data Object

Creating a Table Data Object

Creating an Element Data Object

Procedure

1. Open the application in the Object Manager panel.

2. Under the Detail section, choose the Contained Objects tab.

The Contained Objects tab page appears.

3. Choose Data Object from the Type field and choose Create Object.

4. In the Object Creation dialog box that appears, choose Element from the Type field.

The Element section appears.

5. Choose the type of element you want to create from the Element Type field, under the Define Element Properties section.

For more information, see Data Object

6. Under the General Data section, enter a name for the element and choose Create and navigate to object.

The data object appears in the Object Manager panel.

  Note
If you choose Create button, the element data object appears under the Contained Objects tab. Click the name of the

created object to define the element properties.

7. Add values to the element data object that you have created. You can create values, or refer to existing values or bind the

data object.

Create New Values

a. In the Domain Values tab page, choose Create Values.

b. In the Object Creation dialog box that appears, enter name and value for the data object.

c. Choose Create.

This is custom documentation. For more information, please visit SAP Help Portal.

187


10/15/26, 3:15 PM

d. Depending upon the element you create, the related value fields appear in the Object Creation dialog box.

Enter the related values in the fields that appear.

The following table helps you to create new values and set element attributes:

Element Type

Values

Element

Description

Attributes(Optional)

(all types)

Name and Text fields

(Optional) If you want to

appear for all the element

set additional attributes of

types. You can enter name

an element, choose

and text appropriately for

Element

all the element types

Attributes(Optional) tab.

Text

Enter text in the Value

Length

field.

Number

Enter a number in the

Length

Value field

Decimals

You can enter an attribute

with a maximum length of

255 in the Value field.

You can enter an attribute

with a maximum length of

31.

The length represents the

number of digits without

exponent or sign.

You can enter up to 10

maximum number of

decimal places.

Positive values only

Select the checkbox to

enter only positive values.

Boolean

Amount

Quantity

Timepoint

You may choose True or

False from the Value field.

Enter amount and

currency in the Value and

Currency fields.

Enter quantity and unit in

the Value and Unit fields.

You can choose the

following different

timepoint options:

Date

In the Date field,

choose

. Choose

the date from the

calendar.

Time

In the Time field

that appears,

enter time in

hh:mm:ss format.

Date Time

This is custom documentation. For more information, please visit SAP Help Portal.

188


10/15/26, 3:15 PM

Element Type

Values

Element

Description

Attributes(Optional)

In the Date and

Time fields that

appear, choose

and select the

date from the

calendar. In the

Time field enter

time in hh:mm:ss

format.

Universal Time

In the Date field,

choose

 and

select the date

from the calendar.

In the Time field

enter time in

hh:mm:ss format.

  Note

i. You can set element attributes only for Number, Timepoint and Text element types.

ii. If the value of a constant does not fit to the element attributes (for example, exceeds the length)

then you will get a warning message. You can still activate the object and such calculations are

carried on with decfloat precession.

iii. The element attributes only affect the design time and not the runtime of the BRFplus.

Select from Existing Values

a. In the Domain Values tab, choose Select Values.

b. In the Object Query dialog box that appears, select the value and choose Select.

Bind the Element Data Object

You can bind the data object if you want to have a value help from where you can select values. Under the Element

Properties tab, choose one of the following options from the Select Binding Type dropdown list:

Bind to an Existing Element

a. Choose Bind an existing BRFplus element option to bind the object to an existing element.

b. In the Object Query dialog box that appears, select the data object.

Bind to a Data Dictionary object

a. Choose the Bind a data dictionary (DDIC) element to bind the object to an element object in the data

dictionary.

b. In the Bind DDIC dialog box that appears, select the DDIC element and choose Select.

For more information, see Data Binding

This is custom documentation. For more information, please visit SAP Help Portal.

189


10/15/26, 3:15 PM

8. If you want to to restrict the number of allowed comparison types for an element, choose the relevant allowed comparison

from the Allowed Comparisons field on the Element Properties tab.

  Example

You can set restrictions on comparisons of an element, for example, in decision tables or decision trees. If you select

Equals comparison for an element that is used in a decision table, then you can have only one or no value and you

cannot use less or greater comparisons.

The following table lists the allowed comparison types for an element:

Allowed Comparisons for an element

Description

Data object can be used in all types of comparison operations

which are supported by the system for the particular type of the

data object. This is the default for elementary data objects of

type Text.

Data object can only be tested for equality against one single

value.

Data object can only be tested for equality or unequality against

one single value. This is the default for elementary data objects

of type Boolean.

Data object can only be tested for equality or unequality against

a list of values.

Data object can be used in all types of comparison except for

string comparisons (like contains string or matches

pattern). This is the default for elementary data objects of

the following types:

Amount

Number

Quantity

Timepoint

Data object can be used in those types of comparison

operations that are explicitly mentioned in a list of allowed

operations. This list has to be defined individually for that

particular data object. For example, you can define that a data

object may be used in greater than and greater than or equal

to comparisons, but not in less than and less than or equal to

comparisons.

No Restriction

Equals

Single Value

Value List

Non-textual

User-Defined

9. Activate the data object.

10. Save the data object.

Next Steps

Comparison Operations

Creating a Structure Data Object

This is custom documentation. For more information, please visit SAP Help Portal.

190


10/15/26, 3:15 PM
Procedure

1. Open the application in the Object Manager panel.

2. Under the Detail section, choose the Contained Objects tab.

The Contained Objects tab page appears.

3. Choose Data Object from the Type field and choose Create Object.

4. In the Object Creation dialog box that appears, choose Structure from the Type field.

5. Enter a name for the structure data object and choose Create and navigate to object.

You are directly navigated to the structure data object that you have created.

  Note

If you choose Create button, the structure data object appears under the Contained Objects tab. Click the name of the

created structure object.

6. Define data binding.

You can bind the data object to a data dictionary (DDIC) structure or a GDT structure. In the Select Bind Type dropdown

list, choose from the following options:

Choose Bind a data dictionary (DDIC) structure and in the Bind DDIC structure dialog box that appears, select the

DDIC structure and choose Select.

Choose Bind a GDT structure and in the Bind GDT structure dialog box that appears, enter the relevant details.

For more information, see Data Binding

7. Define the structure. You can add an existing data object or a new data object to the structure.

Add a New Data Object

a. Choose Add New Data Object and in the drop down menu, select the data object type you want to create.

b. In the Object Creation dialog box that appears, create the data object.

Add an Existing Data Object

a. Choose Add Existing Data Object.

b. In the Object Query dialog box that appears, select the data object and choose Select.

8. Activate the data object.

9. Save the changes.

Creating a Table Data Object

Procedure

1. Open the application in the Object Manager panel.

2. Under the Details section, choose the Contained Objects tab.

The Contained Objects tab page appears.

3. Choose Data Object from the Type field and choose Create Object.

4. In the Object Creation dialog box that appears, choose Table from the Type field.

5. Enter a name for the table and choose Create and navigate to object.

This is custom documentation. For more information, please visit SAP Help Portal.

191


10/15/26, 3:15 PM

You are directly navigated to the table data object.

  Note

If you choose Create, the created table data object appears under the Contained Objects tab. Click the name of the

created data object.

6. Bind the data object if you want to have a value help from where you can select values.

a. Choose Current object should be bound in the DDIC Binding field.

b. Choose Bind DDIC Table Type.

c. In the Bind DDIC dialog box that appears, select a DDIC table type and choose Select.

For more information, see Data Binding

7. Assign table line type.

You can refer to an existing data object or create a new data object.

  Note
You can assign table line type only when you choose Current object should not be bound in the DDIC Binding field.

Select an Existing Data Object

a. Choose

 next to Table Line Type.

b. In the context menu, choose Reference existing BRFplus type....

c. In the Object Query dialog box that appears, select the data object.

Create a New Data Object

a. Choose

 beside Table Line Type.

b. In the context menu, choose Create new BRFplus type....

c. In the Object Creation dialog box that appears, create an element data object.

For more information, see Creating an Element Data Object

d. In the Element section, define the binding.

Bind the Object

i. Choose Current object should be bound in the Binding Definition field.

ii. Choose the bind type.

You can either choose Bind a data dictionary (DDIC) element or Bind a GDT element or Bind

an existing FDT element.

e. Choose the element type.

  Note

You can define the element type only when you choose Current object should not be bound in the

Binding Definition field.

8. Activate the data object.

9. Save the changes.

This is custom documentation. For more information, please visit SAP Help Portal.

192


10/15/26, 3:15 PM

Creating a Rule

Procedure

1. Open the application in the Object Manager panel.

2. Under the Detail section, choose the Contained Objects tab.

3. In the Contained Objects tab page that appears, choose Rule object from the Type field and choose Create Object.

4. In the Object Creation dialog box that appears, enter the following data:

Name

(Optional) Short Text

(Optional) Text

5. Choose Create and navigate to object.

The newly created rule opens in the Object Manager panel.

  Note

If you choose Create button, the created rule object appears under the Contained Objects tab.

6. Assign a condition to the rule.

You can assign a standard type, an existing context data object, an existing expression or create a new expression as the

condition.

a. Use Value Range as Condition

Select a Standard Type

i. Choose

 next to No expression assigned.

ii. In the context menu, choose  Use Value Range From...

 Default Objects  and choose the standard

type.

Select an Existing Context Data Object

i. Choose

 next to No expression assigned.

ii. In the context menu, choose  Use Value Range From...

 Other Context Parameter...

.

iii. In the Context Query dialog box that appears, select the data object.

b. Use Expression and Data Object as Condition

Select an Existing Expression

i. Choose

 next to No expression assigned.

ii. In the context menu, choose  Select Condition

 Select Expression...

 Select...

.

iii. In the Object Query dialog that appears, enter the name of the expression in the Object Name field

and choose Search.

The expression appears below the Search button.

iv. Select the expression.

Select a Standard Data Object

This is custom documentation. For more information, please visit SAP Help Portal.

193


10/15/26, 3:15 PM

i. Choose

 next to No expression assigned.

ii. In the context menu, choose  Select Condition

 Select Data Object...

 Default Objects  and

choose the data object type.

Select an Existing Data Object

i. Choose

 next to No expression assigned.

ii. In the context menu, choose  Select Condition

 Select Data Object...

 Other Context Parameter...

.

iii. In the Context Query dialog box that appears, select the data object.

c. Use a New Expression

i. Choose

 next to No expression assigned.

ii. In the context menu, choose Create Expression....

iii. In the Object Creation dialog box that appears, create the expression.

For more information, see Creating Expressions

  Note

The condition should be a context data object or a nested expression whose value or result can be converted into

a Boolean type.

7. Assign an action to the rule.

Assign Action

You can either choose an existing action or create a new action.

Select an Existing Action

a. Choose Add next to Then.

b. In the context menu, choose  Perform Action

 Select...

.

c. In the Object Query dialog that appears, select the action.

Create a New Action

a. Choose Add next to Then.

b. In the context menu, choose  Perform Action

 Create...

.

c. In the Object Creation dialog box that appears, create the action.

For more information, see Creating Action Types

Assign Value to Context

Select an Existing Context Parameter

a. Choose Add next to Then.

b. In the context menu, choose  Assign Value to Context

 Other Context Parameter...

.

c. In the Context Query dialog that appears, select the data object.

d. Enter values for the data object.

Assign an Expression

This is custom documentation. For more information, please visit SAP Help Portal.

194


10/15/26, 3:15 PM

Select an Existing Expression

a. Choose Add next to Then.

b. In the context menu, choose  Process Expression

 Select...

.

c. In the Object Query dialog that appears, select the expression.

Create a New expression

a. Choose Add next to Then.

b. In the context menu, choose  Process Expression

 Create...

.

c. In the Object Creation dialog box that appears, create the expression.

For more information, see Creating Expressions

8. Similarly, add actions to the Else section of the rule.

9. Activate the rule.

10. Save the rule.

Creating a Rule Set

Procedure

1. Open the application in the Object Manager panel.

2. Under the Detail section, choose the Contained Objects tab.

The Contained Objects tab page appears.

3. Choose Rule Set from the Type field and choose Create Object.

4. In the Object Creation dialog box that appears, enter the following data:

Name

(Optional) Short Text

(Optional) Text

5. Choose Create and navigate to object.

The rule set opens in the Object Manager panel.

6. Add a pre-condition to the rule set.

a. Choose Assign Pre-Condition.

This is custom documentation. For more information, please visit SAP Help Portal.

195


10/15/26, 3:15 PM

b. In the Object Query dialog box that appears, select the expression.

The expression appears under the Detail section.

  Note
The selected expression has to return a Boolean result.

7. Assign a function to the rule.

a. Choose Assign Function.

b. In the Object Query dialog box that appears, select the function.

The function appears under the Detail section.

8. Assign rules to the rule set. You can add an existing rule or a new rule.

Create a New Rule

a. Choose

Insert Rule

 Create...

.

A rule is added.

b. Enter the description for the rule.

c. Assign condition and action to the rule.

For more information, see Creating a Rule

Select an Existing Rule

a. Choose

Insert Rule

 Create...

.

b. In the Object Query dialog box that appears, select the rule.

The rule appears under the Rules section.

9. Add an exit condition.

You can create or select a condition.

Creating a Condition

a. Choose

Insert Exit Condition

 Create...

.

In the Object Creation dialog box that appears, create the expression as a condition.

Selecting a Condition

a. Choose

Insert Exit Condition

 Select...

.

b. In the Object Query dialog box that appears, select the expression as a condition.

10. Add another rule. You can add an existing rule or create a new rule.

Create a Rule

Choose  Rule Operations

 Insert Next Rule by...

 Create...

The rule appears under the Rules section.

For more information, see Creating a Rule

Add an Existing Rule

a. Choose  Rule Operations

 Insert Next Rule by...

 Select...

This is custom documentation. For more information, please visit SAP Help Portal.

196


10/15/26, 3:15 PM

b. In the Object Query dialog box that appears, select the rule.

11. Activate the rule set.

12. Save the rule set.

Next Steps

Creating a Rule

Creating Action Types

Working with Catalogs

Use

This section describes the different tasks you need to perform for a catalog in BRFplus.

More Information

Creating a Catalog

Maintaining Object Types

Adding Attributes

Creating a Catalog

Procedure

1. Open the application in the Object Manager panel.

2. Under the Detail section, choose the Contained Objects tab.

The Contained Objects tab page opens.

3. Choose Catalog from the Type field and choose Create Object.

4. In the Object Creation dialog box that appears, enter the name of the catalog and choose Create and navigate to object.

The newly created catalog appears in the Object Manager panel.

This is custom documentation. For more information, please visit SAP Help Portal.

197


10/15/26, 3:15 PM

5. You can add folder, object and link nodes to the root node of the catalog.

Add a Folder Node

a. Under the Structure subsection, in the context menu of the catalog, choose Create Folder Node....

The folder node appears below the root node.

b. Enter the following data in the General tab.

Name

The name is displayed in the tree hierarchy in the catalog maintenance view. The name is used as a

backup if the text is not available.

Text

The text is displayed in the catalog browser mode.

  Note

You can also add sub-nodes to the folder.

Add a Object Node

The object node has reference to BRFplus objects. You can add an initial node, select an existing object or create a

new object.

If you want to create a node which has no binding then use the create an initial node option.

Create an Initial Node

This is custom documentation. For more information, please visit SAP Help Portal.

198


10/15/26, 3:15 PM

a. Under the Structure subsection, in the context menu of the catalog, choose  Create Object Node

 Create Initial Node...

.

The object node appears.

b. Enter the name of the leaf node under the General tab.

c. Assign an object to the object node. You can either assign an existing object or a new object to the

object node.

Assign an Existing Object

i. Under the General tab, choose

.

ii. In the context menu, choose Select Object.

iii. In the Object Query dialog box that appears, enter the name of the expression in the

Object Name field and choose the object type.

iv. Choose Search

v. Select the object.

Assign a New Object

i. Choose

.

ii. In the context menu, choose Create Object.

iii. In the General Data section, enter the name and choose the type of object from the

Type field.

iv. Choose Create and navigate to object button.

The object opens in the Object Manager panel.

  Note

If you choose Create button, the object is created and assigned to the object node.

Select an Existing Object

a. Under the Structure subsection, in the context menu of the catalog, choose  Create Object Node

 Select Existing Object...

.

b. In the Object Query dialog box that appears, enter the name of the expression in the Object Name

field and choose the object type.

c. Choose Search.

The object appears below the Search button.

d. Select the object.

Create a New Object

Under the Structure subsection, in the context menu of the catalog, choose Create Object Node and

create the object.

Add a Link to Catalog

Create an Initial Node

This is custom documentation. For more information, please visit SAP Help Portal.

199


10/15/26, 3:15 PM

a. Under the Structure subsection, in the context menu, choose  Create Catalog Node

 Create Initial

Node...

b. Enter the name of the link node.

c. Choose

.

d. In the context menu, choose Select Catalog Node.

e. In the Select a Node dialog box that appears, under the Select Catalog tab, choose the catalog and

choose Select.

f. In the Select Node tab that opens, select the node and choose OK.

The catalog is assigned to the link.

  Note

The root node can also be linked.

Select an Existing Catalog Node

a. Under the Structure subsection, in the context menu, choose  Create Catalog Node

 Select

Catalog Node...

b. In the Select a Node dialog box that appears, under the Select Catalog tab, choose the catalog and

choose Select.

c. In the Select Node tab that opens, select the node and choose OK.

The catalog is assigned to the link.

  Note

The root node can also be linked.

6. Activate the catalog.

7. Save the catalog.

Next Steps

Adding Attributes

Maintaining Object Types

Maintaining Object Types

Procedure

1. Open the catalog in the Object Manager panel.

2. In the Object Types tab, choose Add Type.

A new row is added to the table.

3. In the new row, enter the object type.

You can also select the object type from a list.

a. Choose

.

This is custom documentation. For more information, please visit SAP Help Portal.

200


10/15/26, 3:15 PM

b. In the dialog box that appears, select the type and choose OK.

Next Steps

Creating a Catalog

Adding Attributes

Adding Attributes

Procedure

The root node of the catalog contains the properties of the catalog.

Add Attributes to Structure Node

1. Open the catalog in the Object Manager panel.

2. Under Catalog, choose the Attributes Folder tab.

The Attributes Folder tab page opens.

3. Choose Add Attribute.

4. In the Object Query dialog box that appears, select the data object.

Add Attributes to Object Node

1. Open the catalog in the Object Manager panel.

2. Under Catalog, choose the Attributes Link to Object tab.

The Attributes Link to Object tab page opens.

3. Choose Add Attribute.

4. In the Object Query dialog box that appears, select the data object.

The data object gets added to the object node.

Add Attributes to Link Node

1. Open the catalog in the Object Manager panel.

2. Under Catalog, choose the Attributes Link to Catalog tab.

The Attributes Link to Catalog tab page opens.

3. Choose Add Attribute.

4. In the Object Query dialog box that appears, select the data object.

The data object gets added to the link node.

  Note

For each node type, you can define six different attributes.

More Information

This is custom documentation. For more information, please visit SAP Help Portal.

201


10/15/26, 3:15 PM

Creating a Catalog

Maintaining Object Types

Creating Action Types

Use

This section describes the tasks one needs to perform while creating different types of actions.

More Information

Creating a Message Log Action

Creating a Send Email Action

Creating a Static Method Call Action

Creating a Message Log Action

Use

The message log action is used to write messages into an application log. Messages are created from the message class definition

in the backend or by entering free text with parameters. The parameters of the messages are filled directly or derived either from

context data objects or a nested expression at runtime.

Procedure

1. Open the application in the Object Manager panel.

2. Under the Detail section, choose the Contained Objects tab.

The Contained Objects tab page opens.

3. Choose Action from the Type field and choose Create Object.

4. In the Object Creation dialog that appears, choose Message Log (Actn) from the Type field.

5. Enter the name of the action.

6. Choose Create and navigate to object.

You are directly navigated to the action object that you created.

  Note
If you choose Create, the action object appears under the Contained Objects tab.

This is custom documentation. For more information, please visit SAP Help Portal.

202


10/15/26, 3:15 PM

7. Under the Detail section, enter the application log object and sub-object.

The Application log object field and the Application log subobject field indicate the location in which the object and the

sub-object reside.

8. Select the external identification type. You can choose from the following:

No External Identification in log

Choose No External Identification in log

External Identification as Free Text Input

a. Choose External Identification as Free Text Input.

The free text field appears.

b. Enter text in the Free Text field.

External Identification as Reference Object

a. Choose External Identification as Reference Object.

The reference object field appears.

b. Assign reference object. You can select a standard type, an existing data object or an existing expression.

Select a Standard Type

i. Choose

.

ii. In the context menu, choose Default Objects and select the standard type.

Select an Existing Data Object

i. Choose

.

ii. In the context menu, choose Other Context Parameter...

iii. In the Context Query dialog box that appears, select the data object.

Select an Existing Expression

i. Choose

.

ii. In the context menu, choose Expressions...

This is custom documentation. For more information, please visit SAP Help Portal.

203


10/15/26, 3:15 PM

iii. In the Object Query dialog box that appears, enter the name of the application in the Object

Name field and choose Search.

The expression appears below the Search button.

iv. Select the expression.

9. To save the messages in the database, select the Persist checkbox.

10. Choose

.

A message template appears.

You can use an existing message or create a new message.

Create a New Message

a. Enter the text for the message.

b. Choose the type of action message from the Type field.

The different types of action messages are:

Information

Abort

Error

Status

Warning

Exit

Use an Existing Message

a. Choose the Use Predefined Message button.

b. Enter the message class, number and type.

If the message contains any dynamic placeholders, enter the value either directly or use the reference.

11. Activate the action.

12. Save the action.

  Note

If you want to assign a message with parameters to a message log action, make sure that the parameters used in the message

short text are numbered ( &1, &2, &3, &4). Although it is syntactically allowed to omit the numbers, BRFplus will not

recognize such unqualified parameters as a parameter and will display them literally as "&" instead of replacing them with a

value.

More Information

This is custom documentation. For more information, please visit SAP Help Portal.

204


10/15/26, 3:15 PM

Adding Followup Actions

Creating a Send Email Action

Procedure

1. Open the application in the Object Manager panel.

2. Under the Detail section, choose the Contained Objects tab.

The Contained Objects tab page opens.

3. Choose Action from the Type field and then choose Create Object.

4. In the Object Creation dialog that appears, choose Send Email (Actn) from the Type field.

5. Enter the name of the action.

6. Choose Create and navigate to object.

You are directed to the action object that you have created.

  Note

If you choose Create, the action object appears under the Contained Objects tab.

7. Under the Detail section, enter the following data:

Email address of the recipient in the To field.

You can enter the email address of more than one recipient by using a semi-colon (;) to separate the addresses.

Enter the subject and body of the email.

  Note

You can enter dynamic placeholders in the subject and body of the email and bind the placeholders to a data

object or an expression. A placeholder is composed of an ampersand and a numeric value, for example, &1, &2…

When the email is triggered, the system evaluates the data objects or the expressions. The value replaces the

placeholders in the email.

a. Enter the placeholders in the Subject and Body field.

b. Choose the Refresh Placeholder button.

The Message Placeholders section appears.

c. You can bind the placeholders to a standard type, an existing data object or expression.

i. Bind to a Standard Type

1. Choose

.

2. In the context menu, choose Default Objects and choose the standard type.

ii. Bind to an Existing Data Object

1. Choose

.

2. In the context menu, choose Other Context Parameter....

3. In the Object Query dialog box that appears, select the data object.

This is custom documentation. For more information, please visit SAP Help Portal.

205


10/15/26, 3:15 PM

iii. Bind to an Existing Expression

1. Choose

.

2. In the context menu, choose Expressions....

3. In the Object Query dialog box that appears, select the expression.

iv. Bind to a New Expression

1. Choose

.

2. In the context menu, choose Create Expression....

3. In the Object Creation dialog box that appears, create the expression.

For more information, see Creating Expressions

d. Similarly, perform the above steps to bind the placeholders in the body of the email.

8. Activate and save the action.

Next Steps

Adding Followup Actions

Creating Action Types

Creating a Static Method Call Action

Context

A static method call action is used to call a static method in a class that implements a special interface. It takes a class that

implements the interface and calls the static method on that class.

Procedure

1. Open the application in the Object Manager panel.

2. Under the Detail section, choose the Contained Objects tab.

The Contained Objects tab page opens.

3. Choose Action from the Type field and choose Create Object.

4. In the Object Creation dialog box that appears, choose Static Method (Actn) from the Type field.

5. Enter the name of the action.

6. Choose Create and navigate to object.

You are directly navigated to the action object that you have created.

  Note

If you choose Create button, the created action object appears under the Contained Objects tab. Click the name of the

created object to define the action messages.

This is custom documentation. For more information, please visit SAP Help Portal.

206


10/15/26, 3:15 PM

7. Enter the name of the class or choose

 in the Class field.

8. In the list that appears, select a relevant class and choose OK.

The selected class is added.

9. Add parameters to the action.

You can add an existing expression or create a new expression.

Add an Existing Expression

a. Under Detail section, choose  Add Parameter

 Select...

.

b. In the Object Query dialog box that appears, enter the name of the expression in the Object Name field and

choose Search.

The expression appears below the Search button.

c. Select the expression.

Add a New Expression

a. Under Detail section, choose  Add Parameter

 Create...

.

b. In the Object Creation dialog box that appears, enter the name, select the type of expression and choose

Create.

For more information, see Creating Expressions

10. Activate the action.

11. Save the action.

Next Steps

Adding Followup Actions

Adding Followup Actions

Procedure

You can add followup actions to message log actions and static method call actions.

1. Open the action in the Object Manager panel.

2. Under the General section, choose the Followup Actions tab.

The Followup Actions tab page opens.

3. You can add a new action or add an existing action to the message log action.

Add a New Action

This is custom documentation. For more information, please visit SAP Help Portal.

207


10/15/26, 3:15 PM

a. Choose Add New Action.

b. In the Object Creation dialog box that appears create a new action.

Add an Existing Action

a. Choose Add Existing Action.

b. In the Object Query dialog box that appears, select the action and choose Select.

The selected action is added as a followup action.

4. Activate the action.

5. Save the action.

More Information

Creating a Message Log Action

Creating a Static Method Call Action

Creating a Send Email Action

Configuring the User Settings

Use

You can configure the UI look and feel according to your needs and personal preferences.

Procedure

1. In the menu bar, choose  Workbench

 Personalize .

2. In the Personalization dialog box that appears, make the desired changes on the different tabs.

3. Choose Save to make the current settings effective.

  Note

You can reset all settings offered in the Personalization dialog box to their system defaults. To accomplish this, click Restore

Default Settings.

Some of the personalization settings will only become effective after restarting the BRFplus workbench.

Transporting Objects

Context

BRFplus provides a transport mechanism to transfer system and customizing objects from one system to the other.

Procedure

This is custom documentation. For more information, please visit SAP Help Portal.

208


10/15/26, 3:15 PM

1. Open the application in the Object Manager panel.

2. Choose the Transport button.

3. In the Confirmation of transportation dialog box that appears, enter the transportation request in the Request field.

4. Choose OK.

Setting Versions

Procedure

1. Open the application in the Object Manager panel.

2. Choose

 next to the General section.

3. In the context menu, choose Set Versioning On.

4. In the Confirmation of change of versioning mode dialog box that appears, select the Include reference objects check box

and choose OK.

The list of affected objects appears.

5. Choose OK.

Next Steps

Versioning

Adding Current Objects to Favorites

Procedure

1. In the Navigation panel, choose the object you want to add to Favorites..

2. In the menu bar, choose  Workbench

 Add Current Object to Favorites...

The object appears in the Navigation Panel under the Favorites section.

Checking Usage of Objects

Context

The where-used list allows object dependencies to be set and retrieved. Checking the usage of objects is needed while using the

trace and simulation tool. The where-used list prevents inconsistencies when users want to delete objects that are still used by

other objects.

Procedure

1. Choose the application from which you want to check the usage of objects from the Navigation panel.

The application opens in the Object Manager panel.

2. Choose the Contained Objects tab.

The Contained Objects tab page opens.

This is custom documentation. For more information, please visit SAP Help Portal.

209


10/15/26, 3:15 PM

3. In the Type field, choose the type of object.

4. Select the object from the list, choose  You can also

 Display Where Used List

.

The usages for the selected object appear in the Where-used list dialog box.

Deleting Objects in an Application

Procedure

1. Choose the application in which the object is located from the Repository or Recently Used panel.

2. In the Detail section, under Contained Objects, choose the object type you want to delete from the Type field.

A list of the selected object type appears.

  Example

If you want to delete a data object, choose Data Object in the Type field.

3. Choose the object you want to delete from the list.

  Note

Before deleting an object, use the Where-Used List to check the usage of objects.

For more information, see Checking Usage of Objects

4. You can either delete it directly or you can mark it for delete.

Delete an object which is not used any more in any version

a. Choose  Delete

 Delete .

b. In the Confirmation of Deletion dialog box that appears, choose OK.

Delete an object which is marked for delete

a. Choose  Delete

 Delete Only Objects Marked For Delete .

b. In the Confirmation of Deletion dialog box that appears, choose OK.

Mark an object which is not used any more

a. Choose  Delete

 Mark For Delete .

b. In the Confirmation of mark for deletion dialog box that appears, choose OK.

The confirmation message appears above the menu bar.

Results

The object gets deleted.

Working with Tools

Use

This section describes the different tool components that are available in BRFplus.

This is custom documentation. For more information, please visit SAP Help Portal.

210


10/15/26, 3:15 PM

  Note

Except for the simulation tool, the tools are available only in expert mode. To switch to expert mode, choose

in the upper right

corner of the workbench window, then User Mode.

Checking Application Usage

Deleting Unused Objects

Analyzing Object in Transport Request

Simulating a Function

Importing Values from an Excel File during Simulation

Exporting Content to Excel File during Simulation

Generating Web Services

Export and Import of XML Data

Application Administration

Use

The application administration tool serves as a starting point for different operations that you can execute to clean up the BRFplus

database and remove out-of-date, unused objects or object versions. This helps you keeping the database focused on the

productive objects only, which in turn leads to a reduction of potential problems in terms of cross-dependencies and transport-

related problems.

All operations offered by the application administration tool are based on reports that are also available in the backend via the

FDT_HELPERS transaction. The backend versions of the reports offer even more features than the application administration tool.

Consequently, the backend version is recommended for system administrators, while the application administration tool addresses

occasional users. On the other hand, using the application administration tool in the BRFplus workbench has advantages with

respect to giving the user a detailed overview of what an operation is about to do. Once you have defined a selection, the system

collects all affected objects and presents them in a list. This overview on the level of single objects is available only in the

application administration tool, not in the backend.

Features

The application administration tool offers the following operations:

Selection

All of the operations available in the application administration tool are executed for the minimum object scope of an application.

Some of the operations allow for multiple applications and additional selection criteria, like transport behavior, storage type,

application component, software component, and so on.

Once you have defined the object scope and clicked Apply, the system determines the applications that match the criteria and

contain objects that are about to be touched by the operation that you want to perform. These applications are listed in the UI for

you to check if this is the desired scope. If not, you can easily modify the selection criteria.

From the list of selected objects, you can make the system perform the operation in question for single objects only, rather than for

the entire selection. For example, from a list of unused objects to be deleted, you can choose to delete only a few and then cancel

the mass operation.

This is custom documentation. For more information, please visit SAP Help Portal.

211


10/15/26, 3:15 PM

  Note

If you have defined selection criteria for an operation that supports different criteria at the same time, and then switch to

another operation type that only supports selecting an application, then all the additional selection criteria are lost. However, in

this situation, the system notifies you so that you can preserve your selection.

Operations

Delete Unused Objects

With this operation, you can delete all objects in an application that are not referenced by any other objects. Objects may be

unused because of different reasons:

Objects that have only been created for test purposes.

Objects that were used once but have been replaced by another object.

Objects that were created as an embedded object of a container object, and the container has been deleted in the

meantime.

Unused objects fall into two different categories:

Named objects

Named unused objects are mostly covered by the first two groups listed above.

Unnamed objects

Unnamed unused objects are automatically created behind the scenes by the system as a reaction to a particular user

action. For example, in previous releases of BRFplus, when you entered a range into the condition cell of a decision table, the

system would automatically create an unnamed range expression in the same application and establish a reference

relationship between the decision table and the range expression. This kind of object is particularly hard to find because

they are not shown in the repository tree or any other kind of object list.

Once you have made your selection and click Apply, the system collects the affected objects. If named unused objects are found,

they are shown in a list, and the Delete button is enabled. If unnamed unused objects are found, the Cleanup Unnamed Unused

Objects button is enabled.

  Note
Unlike most other operations offered by the application administration tool, the Delete Unused Objects operation cannot be

run in test mode. If you click the Delete or Cleanup button, the system performs that operation and removes the affected

objects from the database. However, keep in mind that the missing test mode is substituted by the list of affected objects that is

populated when you apply the selection data to the tool. In addition, the objects collected by this operation are by definition

unused, so there is no threat of data loss.

When you have performed this operation successfully, we recommend that you reapply the same selection once again. This is to

find out if there are any new unused objects in the application after the first deletion run. New unused objects can occur if there

are objects in the system that were previously used by an unused object that has been deleted in the previous run. After the run,

an object that was previously used by a now deleted object only becomes unused itself after the previous run, thus becoming

subject to the same operation in a second run, and so on.

Delete Objects Marked for Deletion

With this operation, you can logically delete all objects in a given set of applications that have been marked for deletion and are not

referenced by any other objects. Once you have made your selection and click Apply, the system collects the applications with

affected objects.

This is custom documentation. For more information, please visit SAP Help Portal.

212


10/15/26, 3:15 PM

Besides being marked for deletion and not being referenced by any other object, there is a third criterion that must be fulfilled

before an object is actually deleted by this operation: Based on the current system date, the system subtracts a predefined amount

of time referred to as the data retention period. The resulting date after this subtraction serves as a threshold: Only objects that

have been marked for deletion before that threshold date are actually deleted.

The default value for the data retention period is 90 days. However, the resulting threshold date can be manually adjusted in the

Application Administration tool.

  Note

This operation can only be performed on entire applications. It is not possible to include or exclude individual objects from the

processing.

Discard Old Object Versions

With this operation, you can logically delete outdated object versions in a given set of applications. The system cuts off all object

versions that are older than the given threshold date. The version that was in effect at the threshold date is modified such that the

threshold date is assigned as the version's start date. The system takes care that all dependencies between the affected objects

are properly preserved, so that it is still possible to revert the system to the state it was in at the threshold date. The discarded

object versions remain physically in the database after processing but can no longer be accessed. They are physically removed

after a retention period from the system by an additional cleanup run.

  Caution

Keep in mind that there may be important reasons for object versioning, most typically for reasons of legal compliance and

auditing. Therefore, be very careful when you use this operation. You should make it totally clear that the object versions to be

discarded won't be needed for whatever purpose ever again.

Clean up Database

With this operation, you can explicitly clean up the database from the deactivated objects and object versions that exist in the

database as a result of the operations described above, Delete Objects Marked for Deletion as well as Discard Old Object

Versions. By executing this operation, hidden object versions as well as logically deleted objects are physically deleted from the

database and cannot be retrieved anymore.

Reorganize Objects

With this operation, you can reorganize the internal structure of certain expressions (for example, decision table, loop, case,

boolean) in a BRFplus application that have been taken over from an older release of BRFplus. This helps to improve performance

as well as to simplify the maintenance of such legacy objects.

More Information

Deleting Objects

Versioning

Checking Application Usage

Prerequisites

You are working in the expert mode.

This is custom documentation. For more information, please visit SAP Help Portal.

213


10/15/26, 3:15 PM
Procedure

1. Choose  Tools

 Application Usage .

The application usage page opens.

2. Enter the application's name in the Application field and choose Select.

3. In the Object Query dialog box that appears, select the application from the table list.

The selected application appears in the application usage page.

4. Choose the query type.

You can select applications used by the selected application or select applications using the selected application.

5. Choose the query scope.

You can select the latest version or the version at timepoint or all the available versions.

6. Choose Start Query button.

The query result appears below the Start Query button.

Checking Dictionary Usages

Use

One of the powerful features of BRFplus is its ability to let you build up a data model that is based on the original data objects as

defined for the calling application in the Data Dictionary of the backend system. With this tool, you can analyze all of the usages of

Dictionary objects in the given scope.

Prerequisites

You are running the BRFplus workbench in Expert mode.

Features

Selection

There are several different approaches to control both the scope of objects where the tool searches for potential usages (search

domain) as well as the scope of objects that are actually bound to Dictionary elements:

Search Domain

When you start the tool from the Tools menu, all entry fields available for scope reduction are empty. Starting the search with this

setting would yield the results of a search throughout the entire system. This would be by far too time-consuming. The system

therefore requires that you enter a Dictionary type or a BRFplus application as a search domain (or both).

This is custom documentation. For more information, please visit SAP Help Portal.

214


10/15/26, 3:15 PM

In addition, you can further restrict the search domain to a particular application component. If you decide to do so, the tool yields

only those Dictionary usages that are found in BRFplus applications that are assigned to the given application component.

  Note
Both for entries in the Dictionary Type as well as Application field, you must use distinct names. Wildcards are not supported

here.

Object Scope

Dictionary elements can only be bound to BRFplus data objects. However, you can define if the tool shall yield a list of usages

across all kinds of data objects, or if you want to restrict the result list to contain only elementary data objects, structures, tables,

or any combination of these.

Result

Once you have defined the selection criteria and click Start Search, the system determines all data objects matching the criteria

and populates the result list with these matches. For each entry in the list, the system displays the name of the BRFplus data

object, its type (element, structure, or table), the Dictionary type to which is it bound, and the BRFplus application to which it

belongs. Both the data object name as well as the application name are rendered as links, so that you can navigate to the

respective object by clicking the link.

Updating the Data Binding

In the Binding column, the system uses a traffic light icon to indicate whether the binding between the data object and the

Dictionary element is still up-to-date or not. If the traffic light is red, you need to check the data object and refresh the binding. To

do so, proceed as follows:

1. Click the name of the data object.

The system displays the details screen for the data object.

2. Choose Edit.

3. Choose Refresh Binding.

The system updates the data object according to the current status of the Dictionary element to which it is bound.

4. Choose Activate to save and activate the updated data object.

5. Choose Close to return to the Dictionary Usages tool.

  Note

Depending on the root cause for the fact that a binding relationship is flagged as out of date, the steps listed above may not

necessarily be successful. For example, if the bound Dictionary element has been deleted after the binding has been set up, it is

of course not possible to update the data object by simply clicking on Refresh Data Binding. In such a case, you have to

investigate what has happened to the Dictionary element and either set up a new Dictionary element with the same structure or

establish a binding relationship to another Dictionary element that may have replaced the original element.

Even if refreshing the data binding is successful and after activating the data object, there is no guarantee whatsoever that the

rules using the data object work as before. This is because BRFplus cannot keep track of the changes to the properties and the

structure of bound Dictionary elements. The reason for an out-of-date binding may be a change in the short text of a data

element, but it may as well be the elimination of 10 fields from a Dictionary structure. It is up to you to analyze the nature and

the consequences of the change that has taken place.

This is custom documentation. For more information, please visit SAP Help Portal.

215


10/15/26, 3:15 PM
More Information

Data Binding

Deleting Unused Objects

Procedure

1. Choose  Tools

 Application Administration .

The application administration tool is displayed.

2. From the Operation dropdown list, choose Delete Unused Objects.

3. In the Object Scope section, enter the name of the application where you want to search for, and delete, unused objects and

choose Apply.

  Note

You can enter the name of only one application for this function. There is no support for wildcards.

The system populates the Named Unused Objects list with the unused objects that currently exist in the chosen

application, broken down by object type.

4. Decide how you want to proceed:

If you want to delete all unused objects in the application that you have chosen, click the Delete button.

If you want to delete only individual objects, navigate to the desired object and click

 in the Delete column.

The Messages section displays the number and other details on the objects deleted from the application.

Analyzing Objects in a Transport Request

Prerequisites

You are working in expert mode.

Context

The tool displays, analyzes, and checks BRFplus objects that are recorded on a certain transport request. It performs different

activities, depending on whether it is run in the source or the target system:

In the source system, unreleased transports are shown with objects that contain errors or inconsistencies. The tool also

provides an option to navigate to the affected objects and to correct the errors or inconsistencies so that the transport can

be released without errors from the Before Export Processing check.

In the target system, transports are shown where problems during the After Import Processing check have occurred, with

the consequence of imported objects that have not been activated in the target system. You can restart the After Import

Processing check for these transports after the root cause of the problem has been fixed.

  Example

This is custom documentation. For more information, please visit SAP Help Portal.

216


10/15/26, 3:15 PM

Possible problems can be caused by data objects bound to a DDIC object that does not exist in the target system. Also, a

customer-defined expression type can cause this kind of error if instances of this expression type have been transported

although the underlying classes and interfaces for the expression type are not yet present in the target system.

Procedure

Choose  Tools

 Transport Analysis .

The transport analysis page opens.

Simulating a Function

Use

The simulation tool works similar to function module testing in the ABAP workbench. The tool allows you to provide input for all

kinds of data objects, processes the input, and returns a result.

Prerequisites

The function is activated.

Procedure

1. Open the function in the Object Manager panel.

2. Choose the Start Simulation button.

The Start Simulation button is active only with an activated function.

3. In the Simulation dialog box that appears, under Maintain Context Data Object Values section, enter values next to the

context field.

You can also import values from an excel file.

For more information, see Importing Values from an Excel File during Simulation

4. Under the Simulation Mode section, you can choose Show only Result or Show also Results of Intermediate Steps.

5. Choose Run Simulation.

The result appears in the simulation page.

  Note

Note that not only the function has to be activated, but also the expressions and other objects that are processed. If the

simulation yields unexpected results or error messages, chances are that this is due to a correction you may have made to one

of the involved objects without having activated that object afterwards.

Importing Values from an Excel File during Simulation

Procedure

This is custom documentation. For more information, please visit SAP Help Portal.

217


10/15/26, 3:15 PM

1. Open the function in the Object Manager panel.

2. Choose the Start Simulation button.

The Start Simulation button is active only with an activated function.

3. In the simulation page, choose Browse... next to Select Excel File.

4. In the Choose File dialog box that appears, select the excel file.

The path of the selected file appears in the box next to the Select Excel File field.

5. Choose Import Test Data.

Exporting Context to Excel File during Simulation

Procedure

1. Open the function in the Object Manager panel.

2. Choose the Start Simulation button.

The Start Simulation button is active only with an activated function.

3. In the simulation page, choose Export Context to Excel.

4. In the File Download dialog box that appears, choose Open or Save.

Generating Web Services and Function Modules

Use

The generation tool for web services and RFC-enabled function modules helps an application developer as well as a third-party

user to process the rules defined in BRFplus. The tool helps to create web services and function modules in a highly automated

fashion with minimal interaction.

  Example

You have created a BRFplus function for rule-based calculation of freight costs. This function is called by application A. It may

now turn out that the cost calculation logic is so generic that the same rules could also be used to support freight cost

calculation in a second application B. However, B is a Java-based web application that cannot directly call the BRFplus function

in the ABAP backend system. To solve this scenario, you generate a web service for the BRFplus function in question. This

enables web application B to call the BRFplus function via the generated web service.

Procedure

Generating a Web Service

1. Choose  Tools

 Web Service Generation .

2. In the web service generation page that appears, choose Select Function.

3. In the Object Query dialog box that appears, enter the name of the function and application and choose Search.

4. Select a function from the list.

The selected function appears under the Function section.

This is custom documentation. For more information, please visit SAP Help Portal.

218


10/15/26, 3:15 PM

  Note

To choose any other function, choose Select Other Function.

You can also start the generation tool from the context menu of a function in the navigation panel of the BRFplus

workbench, or with the Generate button in the work area of a function that you are currently editing. With both

approaches, the function to be generated is then already preselected by the system.

5. Configure the web service. In the Web Service section, enter the following data:

a. To create a new function group, select Create Function Group checkbox. Otherwise the function module is

generated in the existing function group provided.

b. To use an existing function group, enter the name of the function group in the Function Group field.

c. Enter the name of the function module for the generated Remote Function Call (RFC) function module in the

Function Module field.

d. Enter name and short text for the web service in Web Service Name and Web Service Short Text fields.

e. To choose the level of security, open the value help of the Web Service Security Profile field. From the different

security profiles offered, choose the one you want to use.

6. In the Transport section, make the required entries:

a. The development package in which you want to generate the web service.

Select the Local Package checkbox if the web service does not need to be transported to other systems. You may as

well enter $TMP in the Development Package field for this purpose.

  Note

You have to transport the objects if you generate the web service in a development package that is not local and if

the package is transportable.

For more information, see Transporting Objects

b. Enter the workbench request.

7. Choose Generate.

The web service is automatically generated with all the required objects.

Activating the generated web service

Once you have walked through all the steps listed above, the system has generated all the required objects. However, the newly

generated web service cannot be used immediately. This is due to applicable security standards that require that web services

must be explicitly activated by an authorized user. As a consequence, you have to carry out the following steps manually:

1. In the backend system, start transaction SICF.

2. In the Service Name field, enter the name of the service you have generated and choose  Program

 Execute .

The system expands the services tree until the services is visible.

3. Choose  Service/Host

 Display/Change .

The system displays all the settings that have been created for the generated service.

4. Check all the settings and modify them where necessary.

5. Save your changes and leave the transaction.

This is custom documentation. For more information, please visit SAP Help Portal.

219


10/15/26, 3:15 PM

6. Start transaction SOAMANAGER.

The system starts the SOA Management tool in a new browser window.

7. Choose  Service Administration

 Single Service Configuration .

8. Enter the service name (or a part of it) into the Search Pattern field.

9. In the Search Results table, select the row containing the desired service and click on Apply Selection.

10. On the Configurations tab, click on Create Endpoints. Check the default settings for Service Name, Description, and New

Binding Name that the system suggests.

11. Once the system has generated the newly defined endpoint, you can maintain the configuration details for it (Provider

Security, Transport Settings, and so on).

After you have completed the steps above and successfully saved the settings, you can use the web service.

Generating a Function Module

Generating an RFC-enabled function module for a BRFplus function is a subset of generating a web service. Therefore, the steps

related to function groups and function modules as described above apply to the generation of a function module as well.

Export and Import of XML Data

Use

You can convert BRFplus objects into an XML representation. This is helpful if you want to transfer objects between systems that

are not located in the same system landscape, or if there is no transport connection provided by the SAP transport system.

Prerequisites

You are running the BRFplus workbench in Expert Mode.

Features

Export

The XML export function works in an object-based manner, that is, you start by selecting a BRFplus object that you want to export.

However, it is possible to extend the scope of an XML export in the following ways:

Include Referenced Objects: With this option set, the selected object is exported together with all objects that are directly

or indirectly referenced by the selected object.

Include Application: With this option set, the selected object is exported together with the BRFplus application to which the

object belongs.

In addition to the scope selection as described above, you can further fine-tune the export by choosing a particular XML version

and an XML schema for the export. Depending on the selection you make, the system adapts the format and syntax of the

exported data. This is helpful in situations where you have to transport BRFplus objects to a system with a lower release than the

source system. Of course, it is always recommendable to choose the highest XML version for the export that is supported by the

target system so that the system can profit from as many features as possible.

The purpose of the XML schema selection is to let you choose between different flavors of an XML-based object representation:

This is custom documentation. For more information, please visit SAP Help Portal.

220


10/15/26, 3:15 PM

Internal

As the name suggests, the Internal schema renders the schema element names in the same way that is used internally by

BRFplus. Therefore, with this schema, the system does not need to perform any transformations during XML import or

export.

External

The External schema is functional equivalent to the Internal schema, but renders all schema element names in upper

camel case notation rather than in capitals. This makes the XML data more readable, which is useful if you want to analyze

the XML data manually.

  Note

To find out which is the highest XML version supported by the target system, start the import function in the target system. The

highest version supported is displayed on the screen.

The XML schema selection is only available if you have chosen the respective setting in the Personalization dialog.

Import

The XML import function is the complementary to the export function. It is used to reimport XML data that have previously been

exported from BRFplus into a different system.

Prior to actually importing data, we recommend to first start the import as a Test Run. The system then checks the import data to

be uploaded for inconsistencies and other possible problems, without actually writing any data into the target system. You can use

the check results for cleaning up and correcting the import data before you start the actual data import.

If the target system into which you want to import the data is not located at the end of the transport chain in your system

landscape, the imported data has to be transported to the subsequent systems. To accomplish this, you have to enter the ID of a

suitable transport request that you have previously created in the import target system.

Import Types

For XML data to be imported into the system, BRFplus offers the following import types:

Standard

With this option, you can import changes for objects that are changeable in the target system.

Repair

With this option, you can repair content that is normally not changeable in the system due to the fact that it was imported

to the system by a normal transport. The repair option should only be used to import content changes provided by an SAP

correction note. You may use this option to apply a content correction to a system before the corresponding support

package with the corrected content is imported into the system.

Local Copy

With this option, you can create a local copy of a non-local application in the source file.

  Note

You can use this option only if the application in the source file is not local and has not yet reached the target system via

a normal transport. This check ensures that local copies cannot overwrite transported data. This is important because

this option results in an exact copy of the imported objects, including the original ID of the imported objects. With that,

the ID of the affected objects is no longer globally unique, and any further transport would lead to unpredictable results.

This is custom documentation. For more information, please visit SAP Help Portal.

221


10/15/26, 3:15 PM

Note that selecting a particular import type is only possible if the corresponding personalization setting has been activated.

Otherwise, the import type selection is not visible, and the system uses the Standard import type.

Handling of Import Conflicts

If the system detects an object in the import data with the same ID as an already existing object in the target system, the further

processing depends on the versioning setting of that object:

Versioning is active

The object contained in the import data is imported as a new version of the object in the target system.

Versioning is not active

The object contained in the import data overwrites the existing object in the target system without further notice. There is

no way for a user to influence this behavior.

Export and Import Across Applications

Both export and import of XML data can only be performed for objects belonging to the same BRFplus application. If you have to

transfer objects from different applications, you have to split the export and import process such that for each application involved,

you have to use a separate data file. When importing such a multi-application project into the target system, make sure that the

data files are processed according to the usage relationships between the different applications: Start by importing objects that

are used by objects from a different application before importing the using objects. Otherwise, the import fails due to object

references that the system cannot resolve.

Activities

Export

To export a BRFplus object from the current system, proceed as follows:

1. Choose  Tools

 XML Export

.

The system displays the XML Export screen.

2. Click Select an Object to choose from all BRFplus objects that are available in the current system the one that you want to

export.

3. Choose Include Referenced Objects if you want to include all objects in the export that are referenced by the selected

object.

4. Choose Include Application if you want to include the application object in the export to which the selected object belongs.

5. From the XML Version dropdown list, choose the highest version number that is supported by the target system.

6. From the XML Schema dropdown list, choose the XML schema that fits your needs best.

7. Click Generate XML File to start the XML conversion process.

  Note
The Generate XML File is active only after you have selected an object for export.

8. Click Download XML File to define a folder in the file system where the system shall store the XML file generated in the

previous step.

Import

This is custom documentation. For more information, please visit SAP Help Portal.

222


10/15/26, 3:15 PM

To import a file containing BRFplus object data into the current system, proceed as follows:

1. Choose  Tools

 XML Import

.

The system displays the XML Import screen.

2. Make sure the XML version of the data to be imported is less than or equal to the Highest XML Version Supported as

outlined on the XML Import screen.

3. Enter the name of the XML File to be imported. You can also select the file by clicking the Browse button and navigating

through the file system.

4. Choose the appropriate Import Type.

5. Decide whether the data to be imported shall be written to a transport request:

For BRFplus objects that are used only local in the target system, no transport is needed. The same applies if there

are no subsequent systems in your system landscape receiving transports from the import target system.

For BRFplus objects defined as customizing objects, enter a Customizing Transport Request ID. This is necessary

for customer-defined objects.

For BRFplus objects defined as system objects, enter a Workbench Transport Request ID. This is necessary for

objects delivered by SAP.

6. Decide whether you want to execute the XML import as Test Run or not.

The Test Run mode is a simulation mode where the system performs all import steps except for actually writing data into

the target system. You can use this mode for checking if the import data is consistent and complete before making physical

changes to the target system.

7. Click Upload File to start either the test run or the XML data import.

More Information

Storage Types

Versioning

Mass Change

Use

The BRFplus workbench provides an easy-to-use interface for creating and maintaining the various objects that make up a

business rules application. However, when it comes to changes that have to be applied to many objects in the same way, navigating

between the objects can become tedious and uncomfortable. To overcome this problem, BRFplus offers a mass change tool that

lets you carry out object changes with little effort, regardless of how many objects are affected by a particular change.

The following mass change activities are supported by the tool:

Check

Activate

Mark as obsolete

Remove obsolete flag

This is custom documentation. For more information, please visit SAP Help Portal.

223


10/15/26, 3:15 PM

Mark for deletion

Remove deletion flag

Delete

Set access level

Set versioning status

Rename

Copy

Export to XML

The mass change tool is also useful in situations where you want to change several objects, but the change itself slightly differs

from object to object rather than applying exactly the same change to all selected objects.

  Example

You have built up a new business rules application. You have created a set of data objects and to ease your life, you created them

all quickly by copying the first data object, with no further modifications. You can now load all these data objects into the mass

change tool and edit the names and texts of all the objects individually. Once you are done, you click Save to let the system

write all the changes into the database at once.

Features

Scope

The scope of objects that are loaded into the mass change tool depends on how you start the tool. You have the following options:

Main Menu

Choose  Tools

 Mass Change . The system behavior depends on the current workbench status:

No object selected

The system loads all applications into the tool that have been created by the currently logged on user.

Object selected

The system loads the application to which the selected object belongs into the tool, with the selected object marked.

Context Menu in Navigation Panel

From the context menu of an object displayed in the navigation panel, choose  Tools

 Mass Change . The system loads

the application to which the selected object belongs into the tool, with the selected object marked.

Search Inside Mass Change

With the mass change tool running, choose Search and enter the search criteria. All objects matching the search criteria are

loaded into the tool. This is the only option where the root element in each row is not necessarily an application.

  Note

Inside the mass change tool, you can force the system to display the contents of all applications created by the currently logged

on user by choosing Show My Applications. This option results in the same object scope as if you would have started the mass

change tool with no object currently selected (see above).

This is custom documentation. For more information, please visit SAP Help Portal.

224


10/15/26, 3:15 PM

Once the system has populated the list of objects, you can recursively expand each of the listed objects to access all the objects

being used by it.

Object Selection

You mark objects to build up a selection of objects to which you want to apply a particular change. Changes can be made to all

objects that are currently loaded into the tool. This is even true for objects that belong to different applications.

Selecting Individual Objects

You select the objects to be changed by clicking the respective table row with the row selection button at the beginning of the row.

To select more than one object, click the table row while holding the  Shift  key or the  Ctrl  key. To select all objects that are

loaded into the tool, choose Select All Items.

Selecting Object Hierarchies

It is often necessary to ensure that a change is not only applied to a particular object but also to all objects that are used by the

first object. You can accomplish this by setting the Uses flag for the first object. With that, the system includes all subordinate

objects into the selection.

  Note

The tool cannot resolve object relationships that go beyond application boundaries. Such cross-application constellations can

occur with objects whose access level has been set to a less restrictive level than the Application level defined as the system

default. Here, the object drilldown stops whenever the tool determines a dependent object that originates from a different

application. Any activities that you initiate for the selected objects stop at that point, leaving the objects in the different

application unchanged.

Depending on how you have defined the scope of objects loaded into the mass change tool (see section Scope above), selecting

object hierarchies can lead to a system behavior where the same object is shown multiple times in the object list. If you select

such an object, the system marks it as selected at all places in the list where that object occurs. This is because each object can

be seen as a self-contained entity and as part of other objects at the same time.

Uses Flag: Additional Information

The semantics of the Uses flag for objects shown in the mass change tool may not be obvious at first glance. Here is a description

of the different states for this flag:

Status

selected

Description

Indicates that all the subobjects of the top-level object (direct as

well as indirect) are marked. Only objects from the same

application as the top-level object are considered.

This state requires that the system has all the needed information

available. For example, this is not the case if the object tree has not

been expanded after the mass change tool has been started. Note

that this can even lead to situations where the same object is

displayed more than once in the tree, where one occurrence has the

Uses flag selected while another occurrence does not - depending

on the expansion state of the tree.

  Note

For reasons of the BRFplus object architecture model, there is

no practical way of providing the tool all the necessary

information for a comprehensive marking indication at once.

This is custom documentation. For more information, please visit SAP Help Portal.

225


10/15/26, 3:15 PM

Status

Description

Due to the fact that the objects are internally organized in a

network rather than in a hierarchy, there is a potentially

unlimited number of bidirectional relationships between them.

Therefore, there is no technical indication for the tool where to

stop when following these relationships. This is why the system

restricts the analysis of marked objects to those that have

already been brought into the tool's focus by expanding certain

tree branches.

not selected

Indicates one of the following alternatives:

The system has insufficient information about the current

object's subobjects.

None of the subobjects is marked.

not specified

Indicates that some of the subobjects are marked, but at least one

of them is not.

  Note
Objects that cannot have any subobjects are always shown with Uses state not selected. This is true for element data objects.

You can decide whether the system shall display or hide the Uses column. To accomplish this, choose  Other Actions

 Show/Hide Uses Column . This can be useful if your monitor has a low screen resolution, and you want to gain space for the

other columns.

Object Data

For each object loaded into the mass change tool, the system displays the most important administrative data in the list:

Name

Text

Type

Versioning Status

Access Level

If you need more information for a particular object to decide whether it shall be subject to a change or not, you can easily access

the complete set of information for that object by clicking its name in the Object column. The system then presents you the same

information for the object as you would see it in the workbench's work area when editing an object.

Change Buffer

Change Buffer and Undo Functionality

With the only exception of the check function, all activities that you can perform in the mass change tool imply a write access to

the marked objects. To protect you from any inadvertent changes being written to the database, the system first writes the

changes for each activity into a buffer area. After that, all the activity buttons are disabled except for the Save and Undo buttons.

This gives you the opportunity to have a thorough look at the changed objects in the list and decide whether everything has been

changed the way you wanted it. Then decide how you want to proceed:

This is custom documentation. For more information, please visit SAP Help Portal.

226


10/15/26, 3:15 PM

If everything is OK, click Save.

If you find any unwanted changes, click Undo. This lets the system revert all marked objects to their previous state.

After having chosen either Save or Undo, the system reenables the activity buttons. The previously marked objects remain marked

for possible further changes.

  Note

The Undo function is not only available for undoing global changes that you have applied with the different activity buttons.

Rather, it is also available for direct changes that you have manually applied to individual objects listed in the mass change tool

(for example, changed texts). However, keep in mind that the Undo function can only operate on those items that are currently

selected in the list.

Notification Concept

For each selected object that you want to change, the system first checks whether the desired change can be applied or not. If the

system determines any problems that prevent the object from being changed, the system alerts you with a corresponding

message. In addition, you find an icon in the Messages column that gives you a hint whether the change was successful or not.

  Note

When you apply a change to a large number of objects, and if the desired change fails for many of them, this results in a long list

of messages in the message area. In this situation, it can be difficult to find out which message refers to which object. To help

you navigate between an object and the corresponding system message, you can click the symbol in the Message column of the

object in question. This lets the system clear the message area and only display the message for the object in question. When

you click the message symbol of any other object, the message area is updated accordingly.

Mass Change Activities

Check

With this function, you let the system perform a consistency check for all marked items. Once the check is done, the system

presents all check messages in sequential order on top of the screen. In addition, for each item where the system has detected an

issue, you find a small icon in the Messages column indicating what kind of problem has been detected for this particular item. This

two-fold type of message output enables you to both detect recurring issues that apply to a bigger number of objects as well as

object-specific issues.

  Note
Checking objects is the only activity in the mass change tool where no write access to the marked items is implied.

Consequently, the Save and Undo buttons are not needed after a check has been performed.

Activate

With this function, you activate all marked items. This is helpful because in the BRFplus workbench, you are normally not forced to

activate an object. This can easily lead to a situation where you have created quite a number of inactive objects, which would be not

much fun to activate manually. Here, the mass activation function comes in handy.

  Note
Unlike activating a single object in the BRFplus workbench, the mass change tool does not support automatic activation of an

object's subobjects. However, you can easily accomplish this by setting the Uses flag.

Mark as obsolete/Remove obsolete flag

This is custom documentation. For more information, please visit SAP Help Portal.

227


10/15/26, 3:15 PM

With this function, you mark the marked items as obsolete. Objects marked as obsolete remain functional in the contexts where

they are already in use, but cannot be used in combination with any new rule statements. You can also use the complementary

function to remove the obsolescence flag from all marked objects again, so that these objects are available again for productive

use.

Mark for deletion/Remove deletion flag

With this function, you mark the marked items for deletion. Objects marked for deletion remain functional in the contexts where

they are already in use, but make it impossible to apply any changes to the referencing objects without replacing the reference. You

can also use the complementary function to remove the deletion flag from all marked objects again, so that these objects are

available again for productive use.

Delete

With this function, you delete the marked items. The affected objects are no longer available in BRFplus.

  Caution

The Mark as Obsolete, Mark for Deletion, and Delete actions should be handled with care. For an in-depth insight into the

implications of these actions, see Deleting Objects.

Set Access Level

With this function, you change the access level of all marked items. This is extremely helpful when you find yourself in a situation

where it turns out that the access level of an entire BRFplus application must be changed. For example, this might happen due to

changed security requirements or changes in the system landscape.

Set Versioning Status

With this function, you switch the versioning status of all marked items on or off. This can be helpful, for example, if you had

versioning switched on for an application for testing reasons and are finally convinced that the application works as desired and

needs no more version control. Or vice versa, due to changed legislation, you are forced to run a particular application under

version control where this was not required in the past.

Rename

With this function, you can perform a simple renaming action for the marked items. The system prompts you to enter a prefix, a

suffix, or both, to be added to the name of the marked items. Although this is a very simple action, it can still help you save a lot of

time since changes to the technical name of an object is not considered an everyday task and is therefore secured by additional

navigation steps in the workbench. In the mass change tool, you can simply bypass these security steps.

  Note

BRFplus identifies its objects by their ID, not by name. Changing the technical name of an object is therefore uncritical within

the scope of BRFplus. However, it is possible that an object is directly referenced by name from an ABAP backend program

calling the BRFplus framework. It is up to you to ensure that all external name-based references to BRFplus objects are kept in

sync with the changes made inside BRFplus.

Renaming does only affect the technical name of an object, not the short text or text. You can still change the text of the

affected objects manually in the mass change tool. For the short text, however, any changes must be made in the workbench for

each affected object.

Due to the logic of the renaming mechanism, the current name of the involved objects will always be kept as a part of the

resulting name. There is no replacing of the original name with this function.

This is custom documentation. For more information, please visit SAP Help Portal.

228


10/15/26, 3:15 PM

Copy

With this function, you can create a copy of the marked items, either in the current application or in a different application. This is a

sophisticated function that offers you several different types of result, depending on the options you choose. For more information,

see Copying Objects with the Mass Change Tool.

Export to XML

With this function, you can create an XML version of the marked items and export it into an external file. This function is based on

the standard XML export function of BRFplus, with the additional option to put together a set of deliberate objects whose XML

representation is contained in the same export file. This is helpful, for example, in situations where a number of objects have been

corrupted in a remote system and you want to replace the corrupted objects by importing the original version via XML, without

touching any of the other objects in the target system.

More Information

Administrative Data

Export and Import of XML Data

Versioning

Deleting Objects

Copying Objects with the Mass Change Tool

Use

You use the mass change tool for copying BRFplus objects mainly for the following reasons:

You need a copy of a number of already existing objects for a new business rule scenario that is identical in structure to an

already existing application, with only a few changes.

You need a copy of a particular complex object and want to make sure that all dependent objects of that object are copied,

too.

Features

The mass change tool offers different options that let you control how exactly objects are copied and what copied objects look like

with respect to their dependent objects. These options are available through different menu commands combined with the status

of the Uses flag of the objects to be copied:

Scenario 1: Copy marked items, leave references to dependent objects unchanged

For this scenario, choose the following:

Copy

 Copy Marked Items

Uses flag: not set

In this scenario, the system copies all marked items. The newly created objects contain references to exactly the same dependent

objects like the original objects that have been copied.

This is custom documentation. For more information, please visit SAP Help Portal.

229


10/15/26, 3:15 PM

  Example

You want to create a copy of function F. F has decision table DT attached as its top expression. DT uses three data objects DO1,

DO2, and DO3. Copying F with the settings mentioned above leads to the following result:

Before

Function F

After

Function F

Function F'

Comment

Refers to DT

New function F' refers to DT like F (that is,
to the same object)

Decision Table DT

Decision Table DT

Used by F and F'

Data object DO1

Data object DO2

Data object DO3

Data object DO1

Data object DO2

Data object DO3

Used by DT

Used by DT

Used by DT

Scenario 2: Copy marked items and dependent objects, leave references to dependent objects unchanged

For this scenario, choose the following:

Copy

 Copy Marked Items

Uses flag: set

In this scenario, the system copies all marked items. Due to the Uses flag being set, the dependent objects of the higher-level

objects are copied as well. However, the newly created higher-level objects still refer to the same dependent objects like the original

objects.

Setting the Uses flag for function F leads to the selection of all objects involved in this example:

Function F

Decision table DT (used by F)

Data objects DO1, DO2, DO3 (used by DT)

  Example

You want to create a copy of function F. F has decision table DT attached as its top expression. DT uses three data objects DO1,

DO2, and DO3. Copying the marked objects with the settings mentioned above leads to the following result:

Before

Function F

After

Function F

Function F'

Comment

Refers to DT

New function F' refers to DT like F (that is,

to the same object)

Decision Table DT

Decision Table DT

Used by F and F'

Decision Table DT'

New decision table DT' has been created
as a copy of DT, but is currently unused.

Data object DO1

Data object DO1

Used by DT and DT'

This is custom documentation. For more information, please visit SAP Help Portal.

230


10/15/26, 3:15 PM

Before

Data object DO2

Data object DO3

After

Data object DO2

Data object DO3

Comment

Used by DT and DT'

Used by DT and DT'

Data object DO1'

New data object, currently unused

Data object DO2'

Data object DO3'

New data object, currently unused

New data object, currently unused

Scenario 3: Copy marked items and dependent objects, change references to copies of dependent objects

For this scenario, choose the following:

Copy

 Copy Marked Items Recursively

Uses flag: not set

In this scenario, the system copies all marked items. For each item, the system also recursively copies the complete hierarchy of

dependent objects. The objects being copied are the same as in Scenario 2 described above, although only function F has been

marked. Once all objects have been copied, the system recreates the original object hierarchy using the newly created objects. In

other words, the original objects are completely mirrored by the newly created objects.

  Example

You want to create a copy of function F. F has decision table DT attached as its top expression. DT uses three data objects DO1,

DO2, and DO3. Copying F with the settings mentioned above leads to the following result:

Before

Function F

After

Function F

Function F'

Comment

Refers to DT

New function F' refers to DT'

Decision Table DT

Decision Table DT

Used by F

Decision Table DT'

New decision table DT' used by F'

Data object DO1

Data object DO1

Data object DO2

Data object DO2

Data object DO3

Data object DO3

Used by DT

Used by DT

Used by DT

Data object DO1'

Used by DT'

Data object DO2'

Used by DT'

Data object DO3'

Used by DT'

Further Considerations

With the Copy Marked Items Recursively command used in the last of the above scenarios, the system implicitly drills from the

marked top-level objects down to all of their components and subcomponents. Therefore, the Copy Marked Items Recursively

cannot be used in combination with the Uses flag set.

This is custom documentation. For more information, please visit SAP Help Portal.

231


10/15/26, 3:15 PM

Although you can use the mass change tool for copying objects from one application to another, the tool cannot resolve object

relationships that go beyond application boundaries. Such cross-application constellations can occur with objects whose access

level has been set to a less restrictive level than the Application level defined as the system default. Here, the object drilldown

stops whenever the tool determines a dependent object that originates from a different application. For a working copy, you have to

add the missing objects manually.

This is custom documentation. For more information, please visit SAP Help Portal.

232
