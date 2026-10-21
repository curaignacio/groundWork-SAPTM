S4611

Basic Transportation Management
in SAP S/4HANA

.

.

.

PARTICIPANT HANDBOOK
INSTRUCTOR-LED TRAINING

Course Version: 20
Course Duration: 2 Day(s)
Material Number: 50158523



SAP Copyrights, Trademarks and
## Disclaimers

© 2022 SAP SE or an SAP affiliate company. All rights reserved.

No part of this publication may be reproduced or transmitted in any form or for any purpose without the
express permission of SAP SE or an SAP affiliate company.

SAP and other SAP products and services mentioned herein as well as their respective logos are
trademarks or registered trademarks of SAP SE (or an SAP affiliate company) in Germany and other
countries. Please see https://www.sap.com/corporate/en/legal/copyright.html for additional
trademark information and notices.

Some software products marketed by SAP SE and its distributors contain proprietary software
components of other software vendors.

National product specifications may vary.

These materials may have been machine translated and may contain grammatical errors or
inaccuracies.

These materials are provided by SAP SE or an SAP affiliate company for informational purposes only,
without representation or warranty of any kind, and SAP SE or its affiliated companies shall not be liable
for errors or omissions with respect to the materials. The only warranties for SAP SE or SAP affiliate
company products and services are those that are set forth in the express warranty statements
accompanying such products and services, if any. Nothing herein should be construed as constituting an
additional warranty.

In particular, SAP SE or its affiliated companies have no obligation to pursue any course of business
outlined in this document or any related presentation, or to develop or release any functionality
mentioned therein. This document, or any related presentation, and SAP SE’s or its affiliated companies’
strategy and possible future developments, products, and/or platform directions and functionality are
all subject to change and may be changed by SAP SE or its affiliated companies at any time for any
reason without notice. The information in this document is not a commitment, promise, or legal
obligation to deliver any material, code, or functionality. All forward-looking statements are subject to
various risks and uncertainties that could cause actual results to differ materially from expectations.
Readers are cautioned not to place undue reliance on these forward-looking statements, which speak
only as of their dates, and they should not be relied upon in making purchasing decisions.

© Copyright. All rights reserved.

iii


## Typographic Conventions

American English is the standard used in this handbook.

The following typographic conventions are also used.

This information is displayed in the instructor’s presentation

Demonstration

## Procedure

Warning or Caution

## Hint

Related or Additional Information

Facilitated Discussion

User interface control

Window title

Example text

Example text

iv

© Copyright. All rights reserved.


Contents

vii

Course Overview

1

3

11

19

21

25

27

33

35

38

47

53

59

61

74

81

86

89

99

100

109

115

119

Unit 1:

Transportation Management as Part of SAP S/4HANA Enterprise
## Management

Lesson: Describing SAP S/4HANA Enterprise Management:

## Motivation and Overview

Lesson: Explaining Basic and Advanced Transportation

Management (TM)

Unit 2:

New User Experience – Working with TM

Lesson: Describing the SAP Fiori UX Strategy

## Lesson: Using Worklists in TM

Exercise 1: Work with SAP Fiori Apps and Transportation

Management

Unit 3:

Master Data for Logistical Processes

Lesson: Creating Business Partners

Lesson: Creating the Transportation Network

Exercise 2: Create Transportation Zones and Transportation

## Lanes

Lesson: Explaining Organizational Units

Unit 4:

Creation of Transportation Requirements

Lesson: Defining Transportation Relevance

## Lesson: Creating Freight Units

Exercise 3: Create Freight Unit Types and Explore Freight Unit

## Building Rules

## Lesson: Defining Conditions

Exercise 4: Create Sales Orders and Deliveries

Unit 5:

## Transportation Planning

Lesson: Creating Freight Orders and Freight Bookings

Exercise 5: Create Freight Order Types and Freight Orders

## Lesson: Subcontracting to Carriers

Exercise 6: Subcontract a Freight Order to a Carrier

© Copyright. All rights reserved.

v


125

127

129

135

139

145

155

157

168

173

181

188

193

199

207

209

Unit 6:

## Transportation Execution

Lesson: Describing Freight and Transport Execution

Lesson: Creating (Print) Freight Documents

Exercise 7: Create Freight Documents

Lesson: Exploring Warehouse Integrations

Exercise 8: Pick, Load, and Post Goods Issue

Unit 7:

Settle Transportation Charges and Distribute Costs

Lesson: Describing Charge Calculation Master Data

Lesson: Calculating Transportation Charges

Exercise 9: Calculate Transportation Charges

Lesson: Settling Transportation Charges with Carriers

Lesson: Distributing Transportation Costs

Exercise 10: Settle Transportation Charges with a Carrier

Exercise 11: Verify a Freight Invoice

Unit 8:

## Outlook – Advanced Transportation

Lesson: Describing Advanced Transportation Management

vi

© Copyright. All rights reserved.


Course Overview

## TARGET AUDIENCE
This course is intended for the following audiences:

● Project Manager

● Project Stakeholder

● Application Consultant

●

Industry / Business Analyst Consultant

● Business User

● Business Analyst

© Copyright. All rights reserved.

vii


viii

© Copyright. All rights reserved.


UNIT 1 Transportation Management as
Part of SAP S/4HANA
Enterprise Management

Lesson 1

Describing SAP S/4HANA Enterprise Management: Motivation and Overview

Lesson 2

Explaining Basic and Advanced Transportation Management (TM)

3

11

## UNIT OBJECTIVES

● Explain the motivation behind SAP S/4HANA Enterprise Management

● Describe the main components of SAP S/4HANA Enterprise Management

● Explain how LE-TRA relates to basic shipping

● Describe the differences between basic shipping and advanced transportation

management

© Copyright. All rights reserved.

1


Unit 1: Transportation Management as Part of SAP S/4HANA Enterprise Management

2

© Copyright. All rights reserved.


Unit 1
Lesson 1

Describing SAP S/4HANA Enterprise
Management: Motivation and Overview

## LESSON OBJECTIVES
After completing this lesson, you will be able to:

● Explain the motivation behind SAP S/4HANA Enterprise Management

● Describe the main components of SAP S/4HANA Enterprise Management

## Motivation Behind SAP S/4HANA
As your enterprise plans to implement SAP S/4HANA, you want to get some insights into the
new SAP S/4HANA Enterprise Management logistic solution.

There has been an exponential growth of digital information (social, mobile, and big data), an
increase of globalization and the spread of business networks, and the Internet of Things.
These changes have resulted in more complex business processes, more complex
organizations, and more complex software solutions. The exponential proliferation of mobile
devices, social media, cloud technologies, and the staggering amounts of data they generate,
have transformed the way we live and work.

Machine learning (ML) is the study of algorithms and statistical models that computer
systems use to progressively improve their performance on a specific task. Machine learning
algorithms build a mathematical model of sample data, known as "training data", in order to
make predictions or decisions without being explicitly programmed to perform the task.

Artificial intelligence (AI) is an area of computer science that emphasizes the creation of
intelligent machines that work and react like humans. Some of the activities that computers
with artificial intelligence are designed for include:

● Speech recognition

● Learning

● Planning

● Problem solving

These advancements have improved our lives and provided us with greater opportunities for
innovation than ever before. The world may be getting smarter, but it is not getting any easier.

© Copyright. All rights reserved.

3


Unit 1: Transportation Management as Part of SAP S/4HANA Enterprise Management

SAP Strategy - Deliver the Intelligent Enterprise

## Figure 1: SAP Strategy - Deliver the Intelligent Enterprise

As the figure, SAP Strategy – Deliver the Intelligent Enterprise, shows, the digital value
network starts with a digital core, which interconnects all aspects of the value network in real
time to drive business outcomes. The digital core gives companies a new platform for core
business processes and bring together business processes with analytics in real time. This
enables a smarter, faster, and simpler enterprise, which includes connecting every aspect of
internal operations. It also enables real-time processes.

SAP is heading in the direction of Machine Learning and the Intelligent Enterprise. Machine
learning technologies are critical to empowering this vision of the Intelligent Enterprise. By
embedding algorithms directly into multiple SAP systems, we can continuously learn and
adapt to new data as it comes in, without a user having to be involved.

The information is presented to knowledge workers in the transaction screens they are
familiar with, but are enhanced with new information to make them more effective at their job.
Not only is SAP delivering these types of embedded self-adapting algorithms into all our core
applications, we are making it possible for our customers to customize these models or
deliver entirely new models of their own with SAP Predictive Analytics, application edition.

This entire value chain, including the core, is digitized, and serves as the platform for
innovation and business process automation.

4

© Copyright. All rights reserved.


Lesson: Describing SAP S/4HANA Enterprise Management: Motivation and Overview

The Next Generation Business Suite

## Figure 2: The Next Generation Business Suite

SAP S/4HANA is a new product. With SAP S/4HANA, we are building on the success of the
SAP Business Suite, powered by SAP HANA, with a completely new and reimagined suite.

SAP S/4HANA runs on SAP HANA and provides simplicity. For example, a simplified data
model with no indexes, no aggregates, no redundancies. It also promotes innovations. For
example, open in-memory platform for advanced applications predicting, recommending, and
simulating.

SAP S/4HANA is natively designed with SAP Fiori UX, and offers an integrated user
experience with modern usability and instant insight on any device (role-based), a maximum
of three steps to complete a job, mobile-first, consistent experience across lines of business
(LoB).

SAP S/4HANA is natively connected to the Internet of Things and business networks for real-
time collaboration in the networked economy. It is natively engineered, providing a choice of
deployment options (on-premise, cloud, and hybrid). It is also natively born for easy adoption.
For example, guided configuration and easy on-boarding, from the discovery of the solution
through cloud trials to deployment with preconfigured best practices.

## Animation: The Next Generation Business Suite

For more information on The Next Generation Business Suite, please view the
animation in the lesson Describing SAP S/4HANA Enterprise Management:
Motivation and Overview in your online course.

© Copyright. All rights reserved.

5


Unit 1: Transportation Management as Part of SAP S/4HANA Enterprise Management

The Next Generation Intelligent ERP

## Figure 4: The Next Generation Intelligent ERP

SAP S/4HANA improves the order and data records entry management. Orders can come in
via business networks or via cloud systems. IoT data are easily imported.

Execution of data is improved by heuristics, machine learning and fast batch processing. The
user just has to react if an exception is raised.

Real time analytics and transactional data are brought together to support fast and suitable
decisions.

## Animation: The Next Generation Intelligent ERP

For more information on The Next Generation Intelligent ERP, please view the
animation in the lesson Describing SAP S/4HANA Enterprise Management:
Motivation and Overview in your online course.

6

© Copyright. All rights reserved.


Lesson: Describing SAP S/4HANA Enterprise Management: Motivation and Overview

The Evolution of the SAP S/4HANA Architecture

## Figure 6: The Evolution of the SAP S/4HANA Architecture

In SAP S/4HANA Finance 1503, the Unified General Ledger (U-GL) was introduced. It brings
together the once-separate components - Financial Accounting (FI) and Controlling (CO) -
into one pool of relevant business data. This single source of truth collects all accounting-
relevant transactions and makes them available to all relevant application components:
Financial Accounting (General Ledger), Controlling, Asset Accounting, and Material Ledger.

Animation: The Evolution of the SAP S/4HANA Architecture

For more information on The Evolution of the SAP S/4HANA Architecture, please
view the animation in the lesson Describing SAP S/4HANA Enterprise
Management: Motivation and Overview in your online course.

With SAP S/4HANA 1511, the optimized data model for logistics with Business Partners (BP)
and Material Ledger (ML) was introduced.

With SAP S/4HANA 1610, Extended Warehouse Management (EWM), Production Planning
and Detailed Scheduling (PP/DS) where embedded and advanced ATP (aATP) was
developed.

With SAP S/4HANA 1709, Transportation Management (TM) was embedded and Commercial
Project Management (CPM), Portfolio & Project Management (PPM) and Financial Closing
Cockpit (FCC) were added.

With SAP S/4HANA 1809, Group Reporting (GRep), Sales Force Automation, Central
Procurement (CPro) (central requisitioning was available as of 1709; 1809 adds central
contract and central purchasing) were added.

© Copyright. All rights reserved.

7


Unit 1: Transportation Management as Part of SAP S/4HANA Enterprise Management

SAP S/4HANA Enterprise Management Lines of Business

Figure 8: SAPS/4HANA Enterprise Management Lines of Business

At the center of SAP S/4HANA Suite is SAP S/4HANA Enterprise Management, which has
been built by simplifying the SAP ERP solution and reintegrating and simplifying portions of
the SAP Business Suite products, such as SAP SRM, CRM, and SCM into this core. SAP
S/4HANA Enterprise Management is available on premise and in the cloud, with different
licensing and subscription models.

The SAP S/4HANA Suite is completed by the integration of dedicated Lines of Business (LoB)
and industry solutions natively into SAP S/4HANA Enterprise Management. These solutions
can be cloud-based, like SAP SuccessFactors, or delivered on-premise as well (for example,
SAP Transportation Management), depending on the market need.

SAP S/4HANA Deployment Options

## Figure 9: SAP S/4HANA Deployment Options

SAP S/4HANA is available as an on-premise edition and as a cloud edition. This training
focuses on the SAP S/4HANA on-premise edition.

8

© Copyright. All rights reserved.


Lesson: Describing SAP S/4HANA Enterprise Management: Motivation and Overview

Although SAP S/4HANA on-premise edition and SAP S/4HANA cloud private option have the
same code line, there are important differences as follows:

● SAP S/4HANA cloud private (single-tenant) option; you don’t buy the software but you

rent it

● The cloud provider is responsible for sizing, upgrades, and so on

● Modifications are not allowed in a cloud environment

To set up the SAP S/4HANA cloud public (multi-tenant) option:

● You get one company code with one plant per country as a template.

● You can use the migration workbench to import master data.

● You can use the Adobe Designer to change or create forms.

You can extend your system using Platform as a Service (PaaS) using the build in services in
SAP HANA or the SAP Cloud Platform (SCP) environment.

## LESSON SUMMARY
You should now be able to:

● Explain the motivation behind SAP S/4HANA Enterprise Management

● Describe the main components of SAP S/4HANA Enterprise Management

© Copyright. All rights reserved.

9


Unit 1: Transportation Management as Part of SAP S/4HANA Enterprise Management

10

© Copyright. All rights reserved.


Unit 1
Lesson 2

Explaining Basic and Advanced Transportation
Management (TM)

## LESSON OBJECTIVES
After completing this lesson, you will be able to:

● Explain how LE-TRA relates to basic shipping

● Describe the differences between basic shipping and advanced transportation

management

## Transportation Management
Logistics Execution provided you with functions for the entire logistic processing (warehouse
management, shipping processes, and transportation processes) available to you as part of
SAP Enterprise Resource Planning (SAP ERP).

## Figure 10: Shipments in Logistics Execution

Transportation (or shipment) is an essential element in the logistics chain. It affects both
incoming and outgoing goods. Effective transportation planning and processing ensure that
shipments are dispatched without delay and arrive on schedule. Transportation costs play an
essential role in the calculation of the price of a product. It is important to keep these

© Copyright. All rights reserved.

11


Unit 1: Transportation Management as Part of SAP S/4HANA Enterprise Management

transportation costs to a minimum so that the price of a product remains competitive.
Efficient transportation planning and processing helps to keep these costs down.

Effective transportation processing is required so that deliveries are shipped on time and are
received on schedule at the customer's site. SAP ECC provides essential functions for
transportation and shipment cost processing for goods issues and goods receipts.

Inbound shipments are an integral part of the process chain in Procurement and are
processed based on inbound deliveries.

## Animation: Shipments in Logistics Execution

For more information on Shipments in Logistics Execution, please view the
animation in the lesson Explaining Basic and Advanced Transportation
Management (TM) in your online course.

The basis of the procurement process is the purchase order. This is followed by confirmation
of the delivery by the vendor. The inbound delivery is created with reference to the purchase
order. The inbound delivery is the basis for creating the inbound shipment, that is, the
shipment of the ordered goods from the vendor to the company's plant. Goods receipt is then
posted. Invoice verification completes the purchasing process.

Outbound shipments are part of the Sales and Distribution (SD) process and are processed
based on outbound deliveries. The basis of the Sales and Distribution process is the sales
order. The subsequent document is the outbound delivery, which documents the shipping of
the goods. The outbound delivery is the basis for creating the outbound shipment, that is, the
shipment of the goods from the company's plant to the customer. Goods issue is then posted
and the invoice is created.

Basic Shipping - LE-TRA and TM

## Figure 12: Basic Shipping - LE-TRA and TM

Software component LE-TRA that provided transportation-related content in SAP ECC is part
of the compatibility scope (SAP Note 2269324 – Compatibility Scope Matrix for SAP
S/4HANA on-premise). That means, its code line is kept within SAP S/4HANA Enterprise

12

© Copyright. All rights reserved.


Lesson: Explaining Basic and Advanced Transportation Management (TM)

Management until end of 2030. The functionality offered from this component is called basic
shipping.

From SAP S/4HANA 1709, Transportation Management becomes part of S/4HANA
Enterprise Management. It offers much more comprehensive and sophisticated functionality
in the domain of transportation. Use of its advanced functions require an additional license.
However, it can also be used with limited scope, that is, offering the same capabilities that
have been offered by LE-TRA. Use within this limited scope does not require a specific license.

Note:
Before release 2020, the solution capability name Basic Shipping has been used
not only for the LE-TRA functionality but as well for the base variant of SAP
S/4HANA TM. With the release 2020 the solution capability has been renamed to
Transportation Management.

Both technical solution capabilities – Basic Shipping and Transportation Management - are
independent from each other and can be used in parallel on the same SAP S/4HANA
database instance. They have no data exchange and no integration within the shipping
process.

This course will explain the (new) Transportation Management.

Basic Shipping is a defined collection of business processes relevant for shipping within SAP
S/4HANA Enterprise Management. The processes can be implemented with SAP S/4HANA
Release 1511 with LE-TRA and used until end of life of the compatibility scope. The main
functions of LE-TRA will be eventually replaced with the Transportation Management
functions within SAP S/4HANA Enterprise Management. Due to the development of the
freight processes in Transportation Management, the functions might have been realized
differently than they did in LE-TRA. It is planned that the processes can be implemented with
selected functions of SAP S/4HANA TM.

Both technical applications are independent of each other and can then be used next to each
other on the same SAP S/4HANA database instance. They have no data exchange /
integration within the shipping process. Long term the collection of transportation
management processes will only be realized by using selected functions of SAP S/4HANA
TM. The shipment from LE-TRA will be replaced by the freight order from TM.

© Copyright. All rights reserved.

13


Unit 1: Transportation Management as Part of SAP S/4HANA Enterprise Management

Comparison of Basic Shipping and Advanced Transportation

Figure 13: Comparison of Basic Shipping and Advanced Transportation

Advanced TM addresses not only the shipping industries, but also freight forwarders. It allows
early planning based on orders (sales orders, purchase orders, MM scheduling agreements)
in addition to planning based on deliveries (outbound and inbound), which is the only option in
basic shipping / transportation management. Combined planning of inbound and outbound
deliveries within one freight order is allowed in the advanced transportation management
option. Sophisticated planning and optimization options in the domain of vehicle scheduling
and routing, carrier selection, load consolidation and load planning are key differentiators
between advanced transportation management and basic shipping / transportation
management.

SAP note 3065464 provides a comprehensive overview on which objects and functions are
part of the (basic) Transportation Management scope and which require an additional licence
(Advanced Transportation Management).

There is also a tool available helping to analyze the usage of an LE-TRA installation and how to
migrate it to S/4HANA TM. This tool is available via SAP note 3097186.

Transportation Management - Overview

## Figure 14: Transportation Management - Overview

A typical transportation process starts with “Order Management”. Order management is the
process of creating a transportation requirement. Transportation requirements can be
outbound or inbound deliveries. In a second step, these transportation requirements are

14

© Copyright. All rights reserved.


Lesson: Explaining Basic and Advanced Transportation Management (TM)

planned. Transportation management offers manual planning functions. Different aspects of
planning supported by SAP TM are means-of-transport selection (for example, rail vs. road)
and carrier selection. Once the planning process is finished, SAP TM supports also the
execution of transports. Execution includes document creation (print or electronic, like
waybills), track and trace integration as well as warehouse integration (SAP EWM integration
via advanced shipping and receiving). If you do not operate an own fleet, you need to make
sure, that the external carrier is paid for his services. SAP TM allows you to maintain freight
agreements, calculation sheets, and rate tables to accurately define real carrier costs, which
can be used for charge calculation, but also for settlement processes after the transport has
been executed. Analytics and reporting functionalities complete the available functional
scope of SAP TM.

## Animation: Transportation Management - Overview

For more information on Transportation Management - Overview, please view
the animation in the lesson Explaining Basic and Advanced Transportation
Management (TM) in your online course.

## Best Practice Scenarios

Best Practices have been defined for the implementation of transportation management
scenarios. The following notes describe the details:

● 2535942 - SAP Best Practices for S/4HANA Supply Chain for Transportation Management

1709 on premise

● 2849554 - SAP Best Practices for S/4HANA Supply Chain for Transportation

Management 1809

● 2970208 - SAP Best Practices for S/4HANA Supply Chain for Transportation

Management 1909

## LESSON SUMMARY
You should now be able to:

● Explain how LE-TRA relates to basic shipping

● Describe the differences between basic shipping and advanced transportation

management

© Copyright. All rights reserved.

15


Unit 1: Transportation Management as Part of SAP S/4HANA Enterprise Management

16

© Copyright. All rights reserved.


Unit 1

## Learning Assessment

1. What is included in SAP S/4HANA Enterprise Management?

Choose the correct answers.

X A A new ERP system

X B An SAP HANA database

X C Embedded SAP SuccessFactors

## X D Embedded SAP APO

2. Which functions are part of the basic shipping / transportation management scope?

Choose the correct answers.

X A Delivery-based planning

X B Order-based planning

X C  Manual carrier selection

## X D Automatic carrier selection using the optimizer

3. Which documents are relevant for the transportation management scope using SAP

S/4HANA Supply Chain for Transportation Management?

Choose the correct answers.

X A Shipment

X B Sales Order

X C Outbound Delivery

## X D Freight Order

© Copyright. All rights reserved.

17


Unit 1: Learning Assessment

18

© Copyright. All rights reserved.


UNIT 2 New User Experience – Working

with TM

Lesson 1

Describing the SAP Fiori UX Strategy

Lesson 2

## Using Worklists in TM

Exercise 1: Work with SAP Fiori Apps and Transportation Management

21

25

27

## UNIT OBJECTIVES

● Describe the SAP UX strategy based on SAP Fiori

● Explain the elements of personalization within SAP Fiori

● Describe the screen layout of worklists

● Create a query to filter transportation requirements

© Copyright. All rights reserved.

19


Unit 2: New User Experience – Working with TM

20

© Copyright. All rights reserved.


Unit 2
Lesson 1

Describing the SAP Fiori UX Strategy

## LESSON OBJECTIVES
After completing this lesson, you will be able to:

● Describe the SAP UX strategy based on SAP Fiori

● Explain the elements of personalization within SAP Fiori

## SAP Fiori UX
SAP Fiori provides a consistent and holistic user experience for SAP software. By creating
visually pleasing designs with a strong focus on ease of use, the experience is intuitive and
simple across all devices. With effortless interaction patterns, the SAP Fiori UX is designed for
a powerful impact across your enterprise.

Based on SAPUI5 technology, SAP Fiori focuses strongly on users and the way they work. It
allows users to concentrate on core tasks while still keeping track of activities in other areas.
Improvements to the existing SAP Fiori launchpad allow the user a higher degree of flexibility
and guidance supported by Machine Learning and Artificial Intelligence.

These improvements include the enhanced discovery and navigation features, the opening up
of surface interaction via the viewport, access to action-oriented personal notifications,
improved collaboration using the SAP CoPilot, and much more.

SAP CoPilot is your digital assistant and bot integration hub for the enterprise. Interact with
your business apps through one single interface by talking or typing. Get your work done
quickly on mobile, desktop, iOS, and external channels.

## Intuitive User Experience and a Responsive Design

SAP Fiori offers a state-of-the-art web UI, based on HTML5 and UI5 (SAP technology) and
provides capabilities to personalize the screen. SAP Fiori provides technology that creates the
right screens for the new end users. SAP Fiori design principles make it possible to adjust the
screens to every front-end device and adopt it automatically to future design principles. This
ensures that screens are always state of the art.

SAP Fiori is also a development and design principle for SAP. For example, the screens are
role-based, and will be designed and adapted to the needs of the end user of this particular
role. This capability puts the user at the center of the business process. With this principle, we
ensure that the software is not targeting a “neutral individual” that enters all information into
one screen, but that the software is aware of the business context. That is, the tasks and the
exceptional situation the user is working in. As a result, it provides all the relevant information
that the user needs to perform the tasks.

The terms User Interface (UI) and User Experience (UX) stand for two different ways of
thinking.

UI, from a software perspective, describes the interaction between humans and devices, and
aims at maximum efficiency during use.

© Copyright. All rights reserved.

21


## Unit 2: New User Experience – Working with TM

UX takes on the perspective of the end user, and aims at motivation and emotion, not only
during use, but also before and after. UX tries to achieve a sustainably positive attitude for the
user. It also tries to create a motivating experience.

Role Based User Experience

## Figure 16: Role Based User Experience

A role-based user experience means that end users only get all the information and functions
they need for their daily work. They do not receive unnecessary information. The classic SAP
User Interface (UI) offers a single complex transaction for many user roles. The tasks of a
single user then make it necessary to use multiples of these transactions, or additional
applications.

SAP Fiori decomposes these big transactions in several discrete apps suiting the user roles.
All apps are connected to each other, so all tasks of the transaction are still possible but are
only performed if the user really wants. The SAP Fiori launchpad then serves as the central
entry point for all apps of a user.

## Animation: Role Based User Experience

For more information on Role Based User Experience, please view the animation
in the lesson Describing the SAP Fiori UX Strategy in your online course.

22

© Copyright. All rights reserved.


Lesson: Describing the SAP Fiori UX Strategy

Elements of Personalization

Figure 18: Elements of Personalization

## Animation: Elements of Personalization

For more information on Elements of Personalization, please view the animation
in the lesson Describing the SAP Fiori UX Strategy in your online course.

The end users can personalize their own variant of the SAP Fiori launchpad. Besides general
settings like language, they can rearrange groups and tiles, create new groups, and add or
delete tiles to or from an existing group.

Tiles are organized in catalogs in the system. These catalogs hold all technical information to
start an application. To show a tile in the SAP Fiori launchpad, it must be embedded in a
group. Groups can be created centrally in the system and then added to the launchpad, or the
user creates his or her own group and adds tiles from catalogs.

All SAP Fiori apps utilize the SAPUI5 and SAP Gateway technologies. The three types of SAP
Fiori apps differentiate in the following ways (in terms of usage of additional technologies):

● Transactional Apps

- Use of ABAP to provide the classic approach for functions of a business system

- Available for SAP S/4HANA and Business Suite on any DB

● Analytical Apps

© Copyright. All rights reserved.

23


## Unit 2: New User Experience – Working with TM

- Use of analytical capabilities of SAP HANA to provide insights in business data

- Available for SAP S/4HANA and Business Suite on HANA

● Fact Sheet Apps

- Use of Enterprise Search capabilities of SAP HANA to provide search results

- Available for SAP S/4HANA and Business Suite on HANA

SAP Fiori - Useful Transactions and Links

Figure 20: SAP Fiori - Useful Transactions and Links

Animation: SAP Fiori - Useful Transactions and Links

For more information on SAP Fiori - Useful Transactions and Links, please view
the animation in the lesson Describing the SAP Fiori UX Strategy in your online
course.

This figure, SAP Fiori - Useful Transactions and Links, gives you an overview of valuable
transactions in terms of SAP Fiori and links to further information.

## LESSON SUMMARY
You should now be able to:

● Describe the SAP UX strategy based on SAP Fiori

● Explain the elements of personalization within SAP Fiori

24

© Copyright. All rights reserved.


Unit 2
Lesson 2

Using Worklists in TM

## LESSON OBJECTIVES
After completing this lesson, you will be able to:

● Describe the screen layout of worklists

● Create a query to filter transportation requirements

## Worklists in TM
This lesson looks at using personal object worklists to streamline users’ work processes and
bring clear focus to relevant transportation requirements.

## Figure 22: Personal Object Worklists

One of the more flexible tools available to users in TM is the personal object worklist. The
personal object worklist provides central, personalized access to document lists. It gives
users a portal-based interface that they can use to define (and optionally store) queries in a
similar way they are used to from SAP ERP selection screen variants. This tool allows users to
easily access queries, and create, change, delete, or categorize queries. Application-related
buttons provide object-based functions. The data table can be filtered and other settings
applied. Users can personalize the data table and refresh a single query or all queries. The
user sees the very latest information thanks to a high performance refreshing and caching
mechanism. Updates run asynchronously and worklists remain available until results are
refreshed.

© Copyright. All rights reserved.

25


Unit 2: New User Experience – Working with TM

Work with SAP Fiori Apps and Transportation Management

Simulation: Work with SAP Fiori Apps and Transportation Management

For more information on Work with SAP Fiori Apps and Transportation
Management, please view the simulation in the lesson Using Worklists in TM in
your online course.

26

© Copyright. All rights reserved.


Unit 2
Exercise 1

Work with SAP Fiori Apps and Transportation
## Management

## Business Example

You need to show your colleague how to work with SAP Fiori apps, how to find SAP Fiori apps
that are missing in your configuration, and how to work with TM in general. Therefore, you
demonstrate to your colleague, how to add an SAP Fiori app to your menu, how to work with
worklists in TM, and how a user-specific query is created.

Note:
In this exercise, when you see ##, replace the characters with the two-digit
number (01 to 30) assigned to you by your instructor.

1. Add the Create Ocean Freight Booking and Edit Ocean Freight Booking apps as links in the

Order Management screen area.

2. In the Freight Order Worklist, create a view, Status_##, which shows the Life Cycle Status,
Execution Status, Logistical Execution Status, Charge Calculation Status, and Invoicing
Status next to the freight order number.

3. Create a query for delivery-based freight units based on freight unit type BS##.

© Copyright. All rights reserved.

27


Unit 2
Solution 1

Work with SAP Fiori Apps and Transportation
## Management

## Business Example

You need to show your colleague how to work with SAP Fiori apps, how to find SAP Fiori apps
that are missing in your configuration, and how to work with TM in general. Therefore, you
demonstrate to your colleague, how to add an SAP Fiori app to your menu, how to work with
worklists in TM, and how a user-specific query is created.

Note:
In this exercise, when you see ##, replace the characters with the two-digit
number (01 to 30) assigned to you by your instructor.

1. Add the Create Ocean Freight Booking and Edit Ocean Freight Booking apps as links in the

Order Management screen area.

a) In the SAP Fiori launchpad, choose your user icon in the upper right corner and, from

the dropdown menu, select Edit Home Page.

b) In the Order Management group, choose the + tile.

c) In the Search in Catalog field in the upper right corner, enter Ocean Freight and

press Enter.

d) To add the apps to your menu, choose the pin for Create Ocean Freight Booking and

Edit Ocean Freight Booking.

e) Choose Back (< arrow in the upper left corner) twice.

f) Drag both apps from the tile section to the links section.

g) Choose Close.

2. In the Freight Order Worklist, create a view, Status_##, which shows the Life Cycle Status,
Execution Status, Logistical Execution Status, Charge Calculation Status, and Invoicing
Status next to the freight order number.

a) In the SAP Fiori launchpad, navigate to Order Management → Freight Orders

(Worklist).

b) Open the All Road Freight Orders query.

c) Choose the Open Settings dialog.

d) In the Displayed Columns table, select all fields, except for Document, Life Cycle

Status, Execution Status, Logistical Execution Status, Charge Calc. Sts, and Invoicing
Status.

28

© Copyright. All rights reserved.


Lesson: Using Worklists in TM

e) Choose Remove.

f) Choose Save as.

g) As Description, enter Status_##.

h) Choose Save.

i) Choose OK.

3. Create a query for delivery-based freight units based on freight unit type BS##.

a) In the SAP Fiori launchpad, navigate to Logistics Integration → Delivery Integration

(Worklist).

b) Select Define New Query.

c) In the Select Object Type dropdown, select the Freight Unit (Delivery-Based) object

type.

d) In the Select Existing Query as Template dropdown, select Freight Units – All Delivery-

Based Freight Units.

e) Choose Next.

f) In the Document Type field, enter BS##.

g) Choose Next.

h) In the Enter Query Description field, enter Freight Units BS##.

i) For Select Category, select Freight Units.

j) Choose Finish.

© Copyright. All rights reserved.

29


Unit 2: New User Experience – Working with TM

## LESSON SUMMARY
You should now be able to:

● Describe the screen layout of worklists

● Create a query to filter transportation requirements

30

© Copyright. All rights reserved.


Unit 2

## Learning Assessment

1. Which of the following characteristics apply to SAP Fiori Launchpad?

Choose the correct answers.

X A It requires Google Chrome as a browser.

X B It can be used side-by-side with other UIs.

X C  It can be personalized.

X D It is role-based.

2. Which of the following are options of worklists in SAP TM?

Choose the correct answers.

X A Filtering and sorting.

X B Creation and change of existing queries.

X C Switch between different views.

X D Quick criteria maintenance.

© Copyright. All rights reserved.

31


Unit 2: Learning Assessment

32

© Copyright. All rights reserved.


UNIT 3 Master Data for Logistical

Processes

Lesson 1

Creating Business Partners

Lesson 2

## Creating the Transportation Network

Exercise 2: Create Transportation Zones and Transportation Lanes

Lesson 3

Explaining Organizational Units

35

38

47

53

## UNIT OBJECTIVES

● Explain the role of business partners

● Create business partners for customers and carriers

● List the master data elements supporting the different activities in TM

● List the master data elements that define the transportation network

● Create locations, transportation zones, and transportation lanes

● Explain the purpose of organizational structures

● Maintain the link between MM organizations and TM organizations

© Copyright. All rights reserved.

33


Unit 3: Master Data for Logistical Processes

34

© Copyright. All rights reserved.


Unit 3
Lesson 1

Creating Business Partners

## LESSON OBJECTIVES
After completing this lesson, you will be able to:

● Explain the role of business partners

● Create business partners for customers and carriers

## Business Partners
SAP TM can be integrated into SD and MM processes and use corresponding master data
(customer, vendor, material). Some examples of business scenarios where SAP TM is
integrated with these components are as follows:

● Domestic / international outbound transportation

In these scenarios, outbound delivery integration is initiated from SD as a shipper needs to
perform transportation activities with TM. Delivery integration is the key to this process.
Thus, master data for customers, plants, shipping points, and material master data has to
be available to TM to support consistency between planning and execution.

● Domestic / international inbound transportation

In this scenario, TM is integrated with MM and the process is triggered by inbound delivery
integration. Consequently, master data like vendors, plants, shipping points and material
master data needs to be available to plan and execute the SAP TM processes.

## Figure 24: Business Partner Approach in SAP S/4HANA

There are redundant object models in the traditional SAP ERP system where the vendor
master and customer master are used. The (mandatory) target approach in SAP S/4HANA is

© Copyright. All rights reserved.

35


## Unit 3: Master Data for Logistical Processes

the Business Partner approach. Using this approach, it is possible to centrally manage master
data for customers and vendors. Business partners can be categorized as a person, group, or
organization (legal person or part of a legal entity, for example, department). An organization
represents units such as a company, a department of a company, or an association.
Organization is an umbrella term to map every kind of situation in the day-to-day business
activities. A group represents a set of organizations.

Animation: Business Partner Approach in SAP S/4HANA

For more information on Business Partner Approach in SAP S/4HANA, please
view the animation in the lesson Creating Business Partners in your online
course.

Business partners represent a person, organization, group of persons, or group of
organizations in which a company has a business interest. This business object is used for a
variety of business transactions. You create and manage your business partners (BPs) and
the roles they assume for your company centrally. You define the general business partner
data once and assign business partner roles (BP roles) to the business partner. Specific data
is stored for each business partner role. In this way, you do not store redundant data, since
the general data is independent of a business partner’s function or application-specific
extensions. When you first create a business partner in the system, the BP role General
Business Partner is automatically assigned to the business partner.

Assigning partner functions in the SAP system determines the functions of particular
partners in the process. One partner may have several functions. For example, when all the
partner functions within the customer partner type are assigned to one business partner, the
same customer is the sold-to party, ship-to party, payer and bill-to party.

## Relevant Business Partner Roles

In the context of transportation management, these are the roles:

● Business Partner (general) (000000)

● Customer (FLCU01)

● FI customer (FLCU00)

● Vendor (FLVN01)

● FI vendor (FLVN00)

● Carrier (CRM010)

●

Invoicing Party (BBP006)

A customer is defined as a business partner with whom a business relationship involving the
issue of goods or services exists. For TM customers represent a destination location in the
case of a sales order, or a source location in the case of a returns order.

A vendor is defined as a business partner from whom materials or services are procured. The
vendor master is master data, whether it is created for a one time purchase or as a partner
with whom your organization engages continuously. Carriers are vendors from whom
(transportation) services are procured.

36

© Copyright. All rights reserved.


Lesson: Creating Business Partners

How to Maintain Business Partners

## Simulation: How to Maintain Business Partners

For more information on How to Maintain Business Partners, please view the
simulation in the lesson Creating Business Partners in your online course.

## LESSON SUMMARY
You should now be able to:

● Explain the role of business partners

● Create business partners for customers and carriers

© Copyright. All rights reserved.

37


Unit 3
Lesson 2

Creating the Transportation Network

## LESSON OBJECTIVES
After completing this lesson, you will be able to:

● List the master data elements supporting the different activities in TM

● List the master data elements that define the transportation network

● Create locations, transportation zones, and transportation lanes

## The Transportation Network and its Creation
Master data is an integral part of any system. You create and maintain master data over the
course of an object’s lifecycle. It offers companies consistency when executing their various
business processes. In this lesson, you will learn what master data is relevant for SAP
Transportation Management. SAP TM can work with master data (for example, customer,
material) in order to support an end-to-end scenario for a manufacturer or distributor.

## Figure 27: Transportation Network Overview

In the SAP ERP system, each inventory-relevant location can be assigned one or more
shipping points. A shipping point is an independent organizational unit at a fixed location that
processes and monitors inbound and outbound deliveries. The physical address of a shipping
point is represented as a location in master data.

38

© Copyright. All rights reserved.


Lesson: Creating the Transportation Network

Locations in the Transportation Network

Figure 28: Locations in the Transportation Network

The following are examples of location purposes:

● Freight is moved between locations.

● A freight unit always has both a source location and a destination location.

● A freight unit may travel through a number of locations.

Locations are the most granular objects in the transportation network. They are used for
further definitions, such as transportation lanes and so on. They are classified using a location
type.

## Animation: Locations in the Transportation Network

For more information on Locations in the Transportation Network, please view
the animation in the lesson Creating the Transportation Network in your online
course.

The following location types exist:

Table 1: Location Types

ID

1001

1002

1003

1010

1011

Location Type

Production Plant

Distribution Center

Shipping Point

Customer

## Vendor

© Copyright. All rights reserved.

39


Unit 3: Master Data for Logistical Processes

ID

1021

1030

1040

1100

1110

1120

1130

1140

1150

1160

1170

1180

1190

1191

1200

Location Type

Business Partner

Terminal

Store

## Port

## Airport

## Railway Station

Container Freight Station

## Hub

## Gateway

Container Yard

## Warehouse

Carrier Warehouse

## Rail Junction

Border Crossing Point

## Loading Point

Transshipment locations are used for unloading goods from one freight order and loading
them onto another freight order during the transportation process. This function is necessary
when different means of transport or different transportation service providers (carriers)
have to be used to execute a transportation process, for example, truck-ocean-truck; truck-
rail-truck.

Transshipment locations may also be used when consolidating or de-consolidating goods to
be transported.

## Creation of Locations

Figure 30: Creation of Locations

Creating Locations Using a Report

40

© Copyright. All rights reserved.


## Lesson: Creating the Transportation Network

You can use report /SAPAPO/CREATE_LOCATION to create new locations for plants,
shipping points, and business partners. This is useful if you have a lot of entities for which you
require locations.

The following steps are performed when executing the report:

● Creates a location using the existing address of the entity

● Creates a transportation zone for the location if needed

● Updates the location to transportation zone assignment

## Creating Locations Out of Business Documents

If you create or update a document that is relevant for Transportation Management (TM), the
system checks that all necessary locations needed to represent plants, shipping points and
business partners in TM are present in the system. If a location has not already been created,
the system creates it. You can create locations, on demand, from the following TM-relevant
business document categories:

● SD Documents

- Sales Order (SO) (not within (basic) transportation management)

● MM Documents:

- Purchase Order (PO) (not within (basic) transportation management)

- Stock Transfer Order (STO) (not within (basic) transportation management)

● Deliveries

- Outbound Deliveries

-

## Inbound Deliveries

## Creating Locations out of Business Partner Master

For business partners, the system can be configured to immediately create locations when
you create and save a business partner. To do so you need to implement BAdI /SAPAPO/
LOC_CREATE which allows you to specify the conditions for creating or updating a location
when a business partner is saved. Once you create a location, the system triggers any
updates as you make a change to the business partner address.

## Updating Locations Using a Report

You can use the report /SAPAPO/UPD_LOC_SP_PL to update locations for plants and
shipping points. You can trigger this report:

● After making changes in the address data that are relevant for the geocodes of plants and

shipping points

● On a scheduled basis to capture any changes made during a specific period

If a location name already exists when creating a location, a number suffix (for example, ‘_01’)
is added to the location name.

You can work with one-time locations in business processes that require the input of locations
that have not been defined as master data objects. In this case, the system creates one-time
locations based on one-time address details.

Geo-coordinates are required to determine distances and durations. SAP recommends to use
HANA spatial services (HSS) to determine geo-coordinates distances and durations. HSS

© Copyright. All rights reserved.

41


## Unit 3: Master Data for Logistical Processes

needs to be licensed separately. However, the integration from TM to HSS is contained in the
(basic) transportation management scope.

## Transportation Zones

## Figure 31: Transportation Zones

Transportation zones are used to group together a number of locations, as required by
transportation and logistics processes. Again, transportation zones are in turn used to define
other objects such as transportation lanes that define legitimate supply routes.

You can group locations into transportation zones. The system can partly transfer the
properties that you assign to a transportation zone to all its locations. This function reduces
the volume of master data stored in the system.

Transportation zones can group locations (customers, vendors) as well as other zones. One-
time locations are also included in transportation zones.

The following assignment types of locations to transportation zones are possible:

● Direct Assignment – locations are assigned directly to a zone

● Postal Code (Range) Assignment – specified by a postal code or postal code range

● Region Assignment – specified by a country or region, for example, the state of Florida in

the USA

You can mix different assignment types within one transportation zone definition.

42

© Copyright. All rights reserved.


Lesson: Creating the Transportation Network

## Transportation Lanes

Figure 32: Transportation Lanes

## Animation: Transportation Lanes

For more information on Transportation Lanes, please view the animation in the
lesson Creating the Transportation Network in your online course.

Transportation lanes represent the relationship between two locations, two transportation
zones, or a combination of locations and transportation zones that expresses the direct
reachability of the locations or of all locations within the transportation zones for a specific
means of transport (MTr).

Using transportation zones as the source, destination, or both, considerably reduces the
amount of transportation lanes to maintain. A transportation lane points only in one direction.
To model the reverse direction, you need to create another transportation lane.

© Copyright. All rights reserved.

43


Unit 3: Master Data for Logistical Processes

## Default Route

## Figure 34: Default Route

You can use default routes to define a sequence of transshipment locations. For each default
route you can specify the transportation mode, carrier, schedule, and so on, for each
transportation stage. The system considers default routes as possible routes for a shipment
between two locations.

## Animation: Default Route

For more information on Default Route, please view the animation in the lesson
Creating the Transportation Network in your online course.

44

© Copyright. All rights reserved.


Lesson: Creating the Transportation Network

## Means of Transport

Figure 36: Means of Transport

## Animation: Means of Transport

For more information on Means of Transport, please view the animation in the
lesson Creating the Transportation Network in your online course.

Means of transport are classes of (similar) resources, for example, a container ship or a cargo
ship.

The means of transport is used to represent a “method” of transportation such as a truck with
full truck load capacity or a refrigerated truck. The means of transport are assigned to
transportation lanes according to their (geographical) availability. Examples of Means of
Transports are ship, aircraft, truck (15 to), and truck (25 to). A Means of Transports could
also represent refrigerated trucks with a specific cost structure and geographic availability.

Capacities are not defined on the level of means-of-transport, but on equipment type and
equipment group level. You can use equipment types and equipment groups to define
capacities (mass, volume).

How to View the Transportation Network

Simulation: How to View the Transportation Network

For more information on How to View the Transportation Network, please view
the simulation in the lesson Creating the Transportation Network in your online
course.

© Copyright. All rights reserved.

45


Unit 3: Master Data for Logistical Processes

Create Transportation Zones and Transportation Lanes

Simulation: Create Transportation Zones and Transportation Lanes

For more information on Create Transportation Zones and Transportation Lanes,
please view the simulation in the lesson Creating the Transportation Network in
your online course.

46

© Copyright. All rights reserved.


Unit 3
Exercise 2

Create Transportation Zones and
Transportation Lanes

## Business Example

In a transportation process, two different business partner roles are important. The customer
(sold-to-party, ship-to-party) as a recipient of the materials and the carrier (vendor) to whom
transporting the freight is subcontracted to. This exercise shows how to analyze customer
and carrier master data. Furthermore, you will create a transportation network, consisting of
locations, transportation zones and transportation lanes. For this purpose you need to create
locations for your customers and group them into transportation zones. These transportation
zones can then be linked to your shipping point using transportation lanes.

Note:
In this exercise, when you see ##, replace the characters with the two-digit
number (01 to 30) assigned to you by your instructor.

1. What is the address of customer TMBS##-01?

2. To which purchasing organization is carrier CAR_TM3_## assigned?

3. Create locations for your customer business partners TMBS##*.

4. Create a transportation zone, TMZONE## and assign customer locations TMBS##-01,
TMBS##-02, and TMBS##-03 to this transportation zone. Calculate the coordinates of
your transportation zone.

5. To which transportation zone is your location TMBS##-02 assigned? Is it assigned to the
transportation zone created in the previous step exclusively or is it assigned also to other
transportation zones?

© Copyright. All rights reserved.

47


## Unit 3: Master Data for Logistical Processes

6. Why is your location also assigned to other transportation zones?

7. Create a transportation lane from shipping point SP_1010 to your transportation zone

TMZONE##. Assign means-of-transport TRUCK to this transportation lane.

48

© Copyright. All rights reserved.


Unit 3
Solution 2

Create Transportation Zones and
Transportation Lanes

## Business Example

In a transportation process, two different business partner roles are important. The customer
(sold-to-party, ship-to-party) as a recipient of the materials and the carrier (vendor) to whom
transporting the freight is subcontracted to. This exercise shows how to analyze customer
and carrier master data. Furthermore, you will create a transportation network, consisting of
locations, transportation zones and transportation lanes. For this purpose you need to create
locations for your customers and group them into transportation zones. These transportation
zones can then be linked to your shipping point using transportation lanes.

Note:
In this exercise, when you see ##, replace the characters with the two-digit
number (01 to 30) assigned to you by your instructor.

1. What is the address of customer TMBS##-01?

The address of customer TMBS##-01 is Carl-Benz-Straße 1, 68167 Mannheim, Germany.

a) In the SAP Fiori launchpad, go to Master Data →  Manage Customer Master Data.

b) In the Search field, enter TMBS01*.

c) In the Role field, remove any selected roles.

d) Choose Go.

e) Select Customer TMBS##–01.

f) Choose >.

The standard address is displayed in the header.

2. To which purchasing organization is carrier CAR_TM3_## assigned?

Carrier CAR_TM3_## is assigned to purchasing organization 1010.

a) In the SAP Fiori launchpad, go to Master Data →  Maintain Business Partner.

b) In the Business Partner field, enter CAR_TM3_## and press Start.

c) Double-click on business partner CAR_TM3_##.

© Copyright. All rights reserved.

49


## Unit 3: Master Data for Logistical Processes

d) In the Display in BP role dropdown menu, select business partner role Carrier.

e) Choose Purchasing.

f) The assigned purchasing organization is 1010.

3. Create locations for your customer business partners TMBS##*.

a) In the backend, execute transaction SE38.

b) Enter program name: /SAPAPO/CREATE_LOCATION.

c) Press Execute (F8).

d) In the selection field for Business Partner , enter TMBS##*.

e) Press Execute (F8).

f) Exit the transaction.

4. Create a transportation zone, TMZONE## and assign customer locations TMBS##-01,
TMBS##-02, and TMBS##-03 to this transportation zone. Calculate the coordinates of
your transportation zone.

a) In the SAP Fiori launchpad, go to TM Master Data → Define Transportation Zone.

b) Choose Create.

c) In the Zone field, enter TMZONE##.

d) In the Description field, enter Transportation Zone Group ##.

e) Choose Continue.

f) On the Zone – Location tab, choose Create.

g) Enter Location TMBS##-01.

h) Choose Continue.

i) On the Zone – Location tab, choose Create.

j) Enter Location TMBS##-02.

k) Choose Continue.

l) On the Zone – Location tab, choose Create.

m) Enter Location TMBS##-03.

n) Choose Continue.

o) Choose Save.

p) Press the Calculate Coordinates button. It is the calculator icon.

q) Choose Save.

50

© Copyright. All rights reserved.


## Lesson: Creating the Transportation Network

5. To which transportation zone is your location TMBS##-02 assigned? Is it assigned to the
transportation zone created in the previous step exclusively or is it assigned also to other
transportation zones?

The  location  is  assigned  to  the  transportation  zone  defined  in  the  previous  step  plus  at
least one more transportation zone DE-SOUTH.

a) In the SAP Fiori launchpad, go to TM Master Data → Define Transportation Zone.

b) Choose Open Advanced Search.

c) In the Locations Included field, TMBS##-02.

d) Choose Advanced Search.

e) Check how many entries the location is assigned to.

6. Why is your location also assigned to other transportation zones?

The location is assigned to other transportation zones that are defined based on address
data  automatically.  The  assignment  to  transportation  zone  DE-SOUTH  is  based  on  the
region code maintained in the address data.

7. Create a transportation lane from shipping point SP_1010 to your transportation zone

TMZONE##. Assign means-of-transport TRUCK to this transportation lane.

a) In the SAP Fiori launchpad, go to TM Master Data → Define Transportation Lane.

b) In Transportation Lane Maintenance, enter the following data:

Start Location/Zone: SP_1010

Dest. Location/Zone: TMZONE##

c) Choose Create.

d) In the Means of Transport screen area, choose Create.

e) Enter the following information:

Means of Transport: TRUCK

Start Date: 01.01.2021

End Date: 31.12.2050

f) Choose Copy and Close.

Note:
If a pop-up appears, asking to create a proposal for the transportation
distance/duration, choose Yes.

g) Choose Save.

© Copyright. All rights reserved.

51


Unit 3: Master Data for Logistical Processes

## LESSON SUMMARY
You should now be able to:

● List the master data elements supporting the different activities in TM

● List the master data elements that define the transportation network

● Create locations, transportation zones, and transportation lanes

52

© Copyright. All rights reserved.


Unit 3
Lesson 3

Explaining Organizational Units

## LESSON OBJECTIVES
After completing this lesson, you will be able to:

● Explain the purpose of organizational structures

● Maintain the link between MM organizations and TM organizations

## Organizational Units
Organizational Management is a means for creating and managing the organizational and
staffing structures in your company that use an organizational model as its basis.

In Transportation Management (TM), the organizational structure consists of the following
organizational units:

● Corporate organization:

This organization unit is optional and serves as a single entry point into the organizations
structure in TM.

● Company organization:

This organization unit corresponds to the ERP company code containing the local
currency. The company organization unit is used by transportation charge management
(TCM) for invoicing and charging.

● Sales organization, office, and group (not relevant for basic shipping)

● Purchase organization and group

● Planning and execution organization and group

A variety of transportation tasks are assigned to different people in an organization. SAP TM
enables you to structure these staffing concepts with the help of organizational models. Other
TM concepts, such as the use of workflow mechanisms, rely on these models to assign tasks
to individuals who participate in these workflows.

SAP TM is a system especially designed for transportation. Due to the particularities of the
business, TM offers a modified organizational model that is easy to maintain.

The following are characteristics of organizational units in SAP TM:

● Organizational units are used to represent the organizational structure of a company.

A company may be structured based on different points of view, such as sales, planning
and execution, or purchasing of freight services.

● These units also build a framework in which all relevant business processes can be

processed.

© Copyright. All rights reserved.

53


## Unit 3: Master Data for Logistical Processes

● Organizational units are used to determine responsibilities; for example, for approval

processes.

● Organizational units are used to allocate revenue and costs to different groups within a

company, such as profit or cost centers.

● Organizational units in SAP TM can be maintained independently of SD and MM. The

organizational structure in SD, MM and TM can be different.

● Organizational units define the responsible persons who are allowed to see the data or to

perform certain actions (authorization).

● Organizational units can be determined automatically based on predefined conditions.

Organizational Classification

Figure 40: Organizational Classification

## Animation: Organizational Classification

For more information on Organizational Classification, please view the animation
in the lesson Explaining Organizational Units in your online course.

The organizational units in SAP TM can be divided into organizational units for purchasing,
and organizational units for planning and execution.

54

© Copyright. All rights reserved.


Lesson: Explaining Organizational Units

Organizational Structures

## Figure 42: Organizational Structures

The hierarchical relationship of organizational units is fixed. For organizational units with a
Purchasing or Planning and Execution unit function, you can only assign organizational units
with a Group unit role to organizational units with an Organization unit role.

TM and MM Purchasing Organization

Figure 43: TM and MM Purchasing Organization

© Copyright. All rights reserved.

55


Unit 3: Master Data for Logistical Processes

## Animation: TM and MM Purchasing Organization

For more information on TM and MM Purchasing Organization, please view the
animation in the lesson Explaining Organizational Units in your online course.

The MM Purchasing Organization is assigned to the corresponding TM Purchasing
Organization in transaction PPOME, which is used to maintain the organizational structure for
TM.

## LESSON SUMMARY
You should now be able to:

● Explain the purpose of organizational structures

● Maintain the link between MM organizations and TM organizations

56

© Copyright. All rights reserved.


Unit 3

## Learning Assessment

1. Which of the following are business partner roles relevant to transportation management?

Choose the correct answers.

X A Customer (FLCU01)

X B  Carrier (CRM010)

X C  Invoicing Party (BBP006)

X D Driver (TM0001)

2. Which of the following are location types?

Choose the correct answers.

X A Shipping Point

X B Transshipment Location

X C Incoterm Location

## X D Business Partner

3. Which master data object defines connectivity in the transportation network.

Choose the correct answer.

X A  Location

X B Transportation Zone

## X C Transportation Lane

4. How can you create locations from business partners?

Choose the correct answers.

X A Using a BAdI implementation

X B Using Output Management

X C Using the CIF Interface

## X D Using a Report

© Copyright. All rights reserved.

57


## Unit 3: Learning Assessment

5. Which of the following organizational unit functions are available and relevant to TM?

Choose the correct answers.

X A Purchasing

## X B Production

X C Planning and Execution

X D Forwarding

58

© Copyright. All rights reserved.


UNIT 4 Creation of Transportation

Requirements

Lesson 1

Defining Transportation Relevance

Lesson 2

## Creating Freight Units

Exercise 3: Create Freight Unit Types and Explore Freight Unit Building Rules

Lesson 3

## Defining Conditions

Exercise 4: Create Sales Orders and Deliveries

61

74

81

86

89

## UNIT OBJECTIVES

● Describe the overall transportation process

● Explain SAP ERP logistics integration

● Describe the integration of SAP ERP deliveries

● Determine routing based on Incoterms

● Define freight unit types

● Create freight units and freight unit building rules

● Determine the conditions used to customize a business process

● Display a condition

© Copyright. All rights reserved.

59


Unit 4: Creation of Transportation Requirements

60

© Copyright. All rights reserved.


Unit 4
Lesson 1

Defining Transportation Relevance

## LESSON OBJECTIVES
After completing this lesson, you will be able to:

● Describe the overall transportation process

● Explain SAP ERP logistics integration

● Describe the integration of SAP ERP deliveries

● Determine routing based on Incoterms

## The Transportation Management Process
The initial Process Flow - Freight Units event that triggers the transportation management
process is a transportation requirement. In the (basic) transportation management scenario,
an outbound or inbound delivery can act as a transportation requirement. In advanced
transportation management scenarios, also order-based planning is possible, that is, sales
orders, purchase orders, stock transfer orders, or MM-scheduling agreements can act as
transportation requirements.

© Copyright. All rights reserved.

61


Unit 4: Creation of Transportation Requirements

Figure 45: Process Flow

## Animation: Process Flow

For more information on Process Flow, please view the animation in the lesson
Defining Transportation Relevance in your online course.

The figure, Process Flow, shows the overall process flow within a (basic) transportation
management scenario. Starting point is the delivery (outbound or inbound). Based on the
delivery, a freight unit will be created, which is the basis of a planning process, if several
freight units are to be consolidated into one transport. In the normal (consolidation) process,
freight units are grouped into a freight order. The freight order is used for subcontracting
processes and execution. In subcontracting processes, the freight charges need to be settled.
For this purpose a freight settlement document can be created. The freight settlement
document can be posted to a service purchase order and service entry sheet. To allow cost
distribution of freight, a settlement document can also be created. The process may
ultimately conclude with an invoice verification.

62

© Copyright. All rights reserved.


Lesson: Defining Transportation Relevance

## Delivery Integration

## Figure 47: Delivery Integration

The delivery document controls, supports, and monitors numerous subprocesses for
shipment processing, such as picking, packing, loading, and posting the goods issue. In
addition, the delivery document can be used as a reference document for the creation of
other shipment documents, such as a bill of lading.

Outbound deliveries and inbound deliveries are created in SAP S/4HANA. They act as a
starting point for TM processes.

## Control Keys
In SAP S/4HANA, you can display the available control keys for document integration with the
internal TM component.

Figure 48: Control Keys

© Copyright. All rights reserved.

63


## Unit 4: Creation of Transportation Requirements

Control keys are configured in Customizing, under Transportation Management → Integration
 → Logistics Integration → Internal TM Component Integration → Define Control Keys for
Document Integration. The control key defines, whether an outbound or inbound delivery is
relevant for transportation management.

## Animation: Control Keys

For more information on Control Keys, please view the animation in the lesson
Defining Transportation Relevance in your online course.

In the Define Transportation-Relevance of Delivery Documents customizing activity, assign a
control key to your delivery document types to integrate corresponding deliveries. The
control key that you assign must have the Outbound Deliveries checkbox selected. If you want
to transfer outbound deliveries. If you want to transfer inbound deliveries, the Inbound
Deliveries checkbox must be selected in the control key.

## Defining Transportation Relevance by Assigning Control Keys
Transportation Relevancy for document integration into TM is configured in Customizing for
Transportation Management, Integration  →  Logistics Integration  → Internal TM Component
Integration → Define Transportation Relevance for Delivery Documents.

Figure 50: Defining Transportation Relevance

## Animation: Defining Transportation Relevance

For more information on Defining Transportation Relevance, please view the
animation in the lesson Defining Transportation Relevance in your online course.

When you define your different document integration scenarios, you then assign the control
key to a shipping point, delivery type, and shipping condition. In addition you define the
logistics integration profile which you will be using for this combination of shipping point,
delivery type, and shipping condition.

64

© Copyright. All rights reserved.


## Lesson: Defining Transportation Relevance

When the delivery is relevant for document integration, the control key is copied to the
delivery document. The logistics integration profile can be used to differentiate the freight unit
building logic, if multiple logistics integration profiles are used.

The following Business Add-In (BAdI) is available to control the transportation relevance for
document integration to TM:

● CHANGE_TM_CTRL_KEY: You can use this BAdI method to change the control key

assigned to the delivery from the control key that was determined using the maintained
Customizing.

## Logistics Integration Profile

The logistics integration profile determines the basic settings for transportation
management.

Settings Defined in the Logistics Integration Profile

● Freight Unit Building Rule / Condition

● Stage Profile / Condition

●

## Incoterm Location Stage Building

If freight units are to be built, you can identify a rule directly or a condition to determine the
freight unit building rule.

## Incoterms

Integrating routing information based on Incoterms:

Incoterms are intended to clearly communicate the tasks, costs, and risks associated with the
transportation and delivery of goods. They define a contractual agreement between shipper
and consignee to determine who is responsible for which stage of the transport and where
and when the responsibilities of each partner start and end.

© Copyright. All rights reserved.

65


Unit 4: Creation of Transportation Requirements

## Figure 52: Incoterms

Frequently used incoterms are described in the table:

Table 2: Incoterms

Incoterm

EXW

FAS

FOB

CFR

CIF

CPT

DES

DEQ

DAF

DDP

DDU

FCA

CIP

Description

## Ex Works

Free Alongside Ship

Free On Board

## Cost and Freight

Cost, Insurance, and Freight

Carriage Paid To

Delivered Ex Ship

Delivered Ex Quay

Delivered At Frontier

Delivered Duty Paid

Delivered Duty Unpaid

## Free Carrier

Carriage and Insurance Paid To

Some of these incoterms require a location, at which tasks, costs, and risks are transferred
from the shipper to the consignee. The incoterm location is the place where the goods are
physically handed over and where the responsibilities for the goods change. The incoterm
location is a master data location in TM and can be used for routing purposes.

66

© Copyright. All rights reserved.


## Lesson: Defining Transportation Relevance

In case of delivery integration with TM, the Incoterms (Part 2) field can be used to define the
incoterm location. You can map Incoterms (Part 2) to an TM master data location with the
app Assign Location to Incoterm Location. You can use this information for stage building.

Stage Building Based on Incoterms

## Figure 53: Stage Building Based on Incoterms

In TM, you can build stages based on the incoterm location. The Incoterm Location Stage
Building field in the logistics integration profile customizing defines how stages are built based
on source location, incoterm location, and destination location. The system uses the incoterm
location for stage building if the incoterm has set the Incoterm Location flag (a flag that
indicates that you must enter a location with this incoterm). If no incoterm is specified, the
system does not use the incoterm location for stage building and the system creates only one
stage from the source to the destination location. If an incoterm is specified but this incoterm
has not set the Incoterm Location flag, the system does not use the incoterm location for
stage building. Instead the system creates only one stage from the source to the destination
location.

The following stage building rules are possible:

●

Initial Value - Two Active Stages:

This setting is set as default. Two planning-relevant stages are created.

● 01 Source Location to Incoterm Location - Type 1

One stage from the source to the incoterm location is created.

● 02 Source Location to Incoterm Location - Type 2

Two stages are created:

© Copyright. All rights reserved.

67


Unit 4: Creation of Transportation Requirements

- An active stage from the source location to the incoterm location

- An additional stage from the Incoterm location to the destination location which is not

relevant for planning

● 03 Incoterm Location to Destination - Type 1

One stage from the incoterm location to the destination. This is relevant, for example, for
the consignee who plans only the route from Incoterm location to the goods receipt.

● 04 Incoterm Location to Destination - Type 2

Two stages are created:

- An active stage from the Incoterm location to the destination location

- An additional stage which is not relevant for planning from the source location to the

Incoterm location

● 05 Two Active Stages

Two planning-relevant stages are created.

## Integration of Text Types
Texts are stored in various objects. You can define different text types for each of these areas.
A sales note, a marketing note, and a shipping specification are examples of sales-specific
text types.

Documents contain texts at header and item level. You can enter texts in several different
languages.

You can store texts in the master data and then copy them into sales and distribution
documents. You can also copy texts from a reference document to another sales and
distribution document, for example, from a quotation to an order, or from an order to a
delivery document. Texts can be copied in a specific language.

Text control is used to determine texts automatically when you create a text object. Texts on
LE documents can be integrated to TM. In TM, you need to define text types and map LE text
types to TM text types. A set of text types is defined as a text schema.

## Delivery Updates
Delivery updates can be triggered both from SAP ERP and from SAP TM. Updates from SAP
TM are based on planning changes.

68

© Copyright. All rights reserved.


Lesson: Defining Transportation Relevance

## Figure 54: Delivery Updates

If a delivery is changed or deleted, this information is sent to TM. The freight units are
adjusted according to the changes. If the quantity of the delivery has changed, the freight
units are adjusted.

You can also update the goods issue date, loading date, transportation start date, and
delivery date in the outbound delivery based on changed planning dates in TM.

You perform planning or change the existing planning of freight units that are based on an
outbound delivery. Dates are changed during planning. Alternatively, you change the dates of
the relevant freight order. When you save the planning results or the changed freight order,
TM determines that the dates in the freight order no longer match the dates in the original
delivery.

TM determines whether the delivery can still be changed by checking the delivery status. If
the delivery can be changed, TM sends the changed dates and requests the update of the
outbound delivery.

Note that TM can trigger the update of outbound deliveries only. It cannot trigger the update
of inbound deliveries.

## Delivery Splits
Delivery splits can be triggered both from SAP S/4HANA and from TM. Splits triggered from
TM are based on planning changes.

© Copyright. All rights reserved.

69


Unit 4: Creation of Transportation Requirements

## Figure 55: Delivery Splits

A delivery that has already been sent to TM and created freight units can be split
subsequently.

Afterwards, there are two deliveries, the changed original one and the new one.

The changed original delivery updates its freight units.

The new delivery that has been created for the items split from the original delivery. For this
new delivery, new freight unit(s) will be created.

Technically, TM first creates the new freight unit(s) by reassigning the freight units from the
original delivery to the new delivery. It then updates the freight units from the original delivery.

The system determines the required changes to freight unit planning for the freight units
assigned to both deliveries. After reassigning the freight units, the system must determine
whether the planning of the freight units in the new or the original delivery is to be discarded
or kept.

You can split an outbound delivery based on planning changes in TM. You perform planning or
change the existing planning of freight units that are based on an outbound delivery. When
you save the planning results, the system determines that a delivery split is required. For
example, freight units that belong to the same delivery have been assigned to different freight
orders, or only some of the freight units that belong to a delivery have been assigned to freight
orders and the other freight units have not been assigned. Note that the split is required only
if the first stage or the last stage of the transportation chain is affected.

TM determines whether the delivery can still be changed by checking the delivery status. If
the delivery can be changed, a new outbound delivery is created and the original outbound
delivery is adapted (that is, it removes the relevant items from the original delivery and
creates a new delivery for these items).

70

© Copyright. All rights reserved.


Lesson: Defining Transportation Relevance

Transportation Planning Changes

## Figure 56: Transportation Planning Changes

Changes to transportation planning in TM can result in several actions, as summarized in the
figure, Transportation Planning Changes.

## Block Handling
You can define how shipment planning blocks of outbound and inbound deliveries are handled
in TM, specifying whether a shipment planning block is creating a planning block, an execution
block, or both.

Therefore, shipment planning blocks can prevent further planning or execution in TM.

You can define a block in customizing by selecting a shipment blocking reason, a document
type, and either the flag for planning block, execution block, or both. The shipment planning
block description is entered automatically according to the block reason.

## Handling Units
A handling unit (HU) is a logistic unit consisting of packaging materials and goods (materials).
Typically, a company does not move individual pieces of different materials, rather quantities
of materials grouped together as packages. You can depict this situation using Handling Unit
Management.

© Copyright. All rights reserved.

71


Unit 4: Creation of Transportation Requirements

Figure 57: Handling Units

## Animation: Handling Units

For more information on Handling Units, please view the animation in the lesson
Defining Transportation Relevance in your online course.

When you use Handling Unit Management, the system tracks the entire HU rather than
individual materials. The HU is the common unit for material and information flow. A business
transaction for a HU implies corresponding business transactions in the background for the
materials and packaging materials it contains. In this way, one business transaction entry
takes the place of several individual material-movement entries.

You can use handling units and can pass them to partners throughout the supply chain.
Handling units have a single identification number that uniquely identifies the handling unit
across the various processes through which it moves. Using handling units in a cross-system
logistics chain usually requires an identification number that is unique worldwide. You
therefore have the option of assigning a Serial Shipping Container Code (SSCC) number to
each handling unit.

Within the framework of unified package building (UPB) you can use packaging specifications
and packing instructions as part of (basic) transportation management.

## Packaging Materials
Packaging materials are intended to enclose or hold together the materials that are to be
transported. The packaging materials and the goods material together comprise the handling
unit, as we have seen.

The material that is to be packed can be packed into or onto the packaging material. The
packaging material can also be a load carrier, such as a pallet. The most important packaging
materials include crates, boxes, containers, wire baskets, and pallets.

You have to maintain the material master data for each packaging material you want to use.
When creating material master records for packaging materials, enter either material type,
VERP (packaging) or a customer-specific material type that you have already defined in
Customizing.

72

© Copyright. All rights reserved.


Lesson: Defining Transportation Relevance

How to View Integration Relevance for Delivery Integration

Simulation: How to View Integration Relevance for Delivery Integration

For more information on How to View Integration Relevance for Delivery
Integration, please view the simulation in the lesson Defining Transportation
Relevance in your online course.

## LESSON SUMMARY
You should now be able to:

● Describe the overall transportation process

● Explain SAP ERP logistics integration

● Describe the integration of SAP ERP deliveries

● Determine routing based on Incoterms

© Copyright. All rights reserved.

73


Unit 4
Lesson 2

Creating Freight Units

## LESSON OBJECTIVES
After completing this lesson, you will be able to:

● Define freight unit types

● Create freight units and freight unit building rules

## Freight Unit Types
This lesson examines the freight planning process in SAP TM, including freight unit building
rules, the definition of freight unit types, and strategies for freight unit building.

Figure 60: Process Flow - Freight Units

## Animation: Process Flow - Freight Units

For more information on Process Flow - Freight Units, please view the animation
in the lesson Creating Freight Units in your online course.

74

© Copyright. All rights reserved.


## Lesson: Creating Freight Units

Freight units are created from preceding business documents such as deliveries.

The system uses either the freight unit type from the freight unit building rule, or the default
freight unit type defined in customizing.

## Freight Units

Figure 62: Freight Units

## Animation: Freight Units

For more information on Freight Units, please view the animation in the lesson
Creating Freight Units in your online course.

Note:
The freight unit type consists of a four-character identifier. The freight order type,
freight booking type, transportation unit type, and freight unit types must be
unique across these four business document types.

Within the freight unit type, you can define if a freight unit can be deleted or if it must be
canceled.

© Copyright. All rights reserved.

75


Unit 4: Creation of Transportation Requirements

Freight Unit Type Customizing

## Figure 64: Freight Unit Type Customizing

The most important customizing settings of the freight unit type with respect to the (basic)
transportation management scenario are the following:

● Change Controller Settings:

You can assign several different settings related to the change controller. These settings
impact how TM responds to document changes (for example, quantity changes).

● Additional Strategies:

There are a number of additional strategies:

- Creation Strategy: Specifies tasks that should be performed when creating a freight

unit.

- Save Strategy: Specifies tasks that should be performed when saving a freight unit.

- Deletion Strategy: Specifies tasks that should be performed when a freight unit is

deleted or canceled.

● Planning Settings

- Distance/duration determination

- Rule/condition for pickup/delivery window determination

● Default Units of Measure

- Weight

- Volume

● Organizational Unit Determination

- Condition: Conditions can be created to determine the organizational unit.

76

© Copyright. All rights reserved.


## Lesson: Creating Freight Units

- Consider Organizational Unit of User check box: Considers the organizational unit

assigned to the user that creates the freight unit in the determination of the
organizational unit responsible for the freight unit.

- Default Org Unit: Execution Organization, Purchasing Organization, Execution Group,
Purchase Group. These are the organization numbers that are defaulted if none of the
previous criteria was successful for the determination of the organizational units.

● Basic Settings:

Track Changes checkbox: Select this box if document changes are to be tracked.

● Output Options

- Assign output profile, additional output profile, text type and text schema here.

## Freight Unit Building Rules
Freight unit building rules are required to plan freight in TM and define how freight units are
built. The system determines which freight unit building rule will be taken into account for the
business document during planning.

There are three freight unit building rule determination options, as follows:

1. The system checks the condition defined in the logistics integration profile. If there is no
condition or the condition cannot determine a result, the system moves to the second
option.

2. The system checks if a freight unit building rule has been maintained in the logistics

integration profile. If no freight unit building rule is maintained, the system moves to the
third option.

3. The system applies standard settings.

## Figure 65: Reasons for Freight Unit Splits

Freight units are created automatically if transportation-relevance is determined for the
delivery. When creating freight units, the system first groups all delivery items that share the
same source and destination location, and pick-up and delivery dates as well as the same
incoterm.

© Copyright. All rights reserved.

77


## Unit 4: Creation of Transportation Requirements

The system considers freight units that already exist for the delivery. It creates freight units
depending on the split quantity and the checkbox for the item split allowed, the system
considers these entries when creating multiple freight units. You can use strategies to create
freight units in accordance with your own requirements. SAP delivers the standard strategy
FUB_AUTO for freight unit building.

Freight Unit Building Rule

Figure 66: Freight Unit Building Rule

## Animation: Freight Unit Building Rule

For more information on Freight Unit Building Rule, please view the animation in
the lesson Creating Freight Units in your online course.

Within the freight unit building rule, you must specify the critical quantity. This parameter
defines the primary unit of measure that allows a line item on a transport requirement to be
split into multiple freight units. Besides that, several planning quantities can be defined, for
example, weight and volume. Every planning quantity is considered for capacity checks of
resources during transportation planning, and every planning quantity is copied to the freight
unit.

The split quantities define the maximum capacity of a freight unit. The system calculates the
freight unit as a multiple of the rounding quantity. If Item Split Allowed is selected, the freight
unit splits the item while it is being built, if it is over the split quantity. The process controller
strategy allows you use strategies to define the way in which freight units are created in
accordance with your requirements. If you maintain an equipment type in the freight unit
building rule, the capacity of the equipment is considered during freight unit building and the
items consolidated into one freight unit are loaded into the equipment.

78

© Copyright. All rights reserved.


## Freight Units

Lesson: Creating Freight Units

## Figure 68: Handling Units and Freight Units

When a delivery includes handling unit items, the freight units are adjusted accordingly. All
product items that have been packaged into one handling unit are included in one freight unit;
they are not split across several freight units. In this way, it is ensured that parts of a handling
unit are not assigned to different freight orders during transportation planning.

If, for example, separate freight units were built per product initially, and these products are
consolidated into one handling unit, the separate freight units are merged into one freight
unit.

There is not necessarily a one-to-one relationship between handling units and freight units.
One freight unit can contain several handling units. If desired, freight unit building can be set
up to create one freight unit per handling unit.

How to Create Freight Unit Types and Freight Unit Building Rules

Simulation: How to Create Freight Unit Types and Freight Unit Building Rules

For more information on How to Create Freight Unit Types and Freight Unit
Building Rules, please view the simulation in the lesson Creating Freight Units in
your online course.

© Copyright. All rights reserved.

79


Unit 4: Creation of Transportation Requirements

Create Freight Unit Types and Explore Freight Unit Building Rules

Simulation: Create Freight Unit Types and Explore Freight Unit Building Rules

For more information on Create Freight Unit Types and Explore Freight Unit
Building Rules, please view the simulation in the lesson Creating Freight Units in
your online course.

80

© Copyright. All rights reserved.


Unit 4
Exercise 3

Create Freight Unit Types and Explore Freight
Unit Building Rules

## Business Example

As a consultant responsible for the configuration of a basic shipping scenario in S/4HANA
you need to show your customer how to create freight unit types and how these document
types are being determined.

Note:
In this exercise, when you see ##, replace the characters with the two-digit
number (01 to 30) assigned to you by your instructor.

1. Create freight unit type BS## with the settings from the table:

Freight Unit Type

Description

## BS##

Freight Unit BS##

Number Range Interval

01

Condition for PU/DLV Window Determina-
tion

FU_TIMEWIND_S4611

Change Controller Strategy

## DEF_CHACO

Purchasing Organization

50000721

Web Dynpro Application Configuration

/SCMTMS/FRE_UNIT

2. What is the purpose of the Rule for Pick-Up/Delivery Window?

3. Which strategies can be used based on the freight unit type?

4. Check the condition Z_FU_TYPE_S4611 that will determine your freight unit type.

© Copyright. All rights reserved.

81


Unit 4: Creation of Transportation Requirements

Note:
Do not make any changes to this condition.

Which criteria is used in condition Z_FU_TYPE_S4611 to determine your freight unit type?

5. From which object / process step is condition Z_FU_TYPE_S4611 triggered?

82

© Copyright. All rights reserved.


Unit 4
Solution 3

Create Freight Unit Types and Explore Freight
Unit Building Rules

## Business Example

As a consultant responsible for the configuration of a basic shipping scenario in S/4HANA
you need to show your customer how to create freight unit types and how these document
types are being determined.

Note:
In this exercise, when you see ##, replace the characters with the two-digit
number (01 to 30) assigned to you by your instructor.

1. Create freight unit type BS## with the settings from the table:

Freight Unit Type

Description

## BS##

Freight Unit BS##

Number Range Interval

01

Condition for PU/DLV Window Determina-
tion

FU_TIMEWIND_S4611

Change Controller Strategy

## DEF_CHACO

Purchasing Organization

50000721

Web Dynpro Application Configuration

/SCMTMS/FRE_UNIT

a) In the back-end system, go to Customizing by entering transaction code spro.

b) Choose SAP Reference IMG.

c) In Customizing, go to Transportation Management → Planning → Freight Unit → Define

Freight Unit Types.

d) Choose New Entries.

e) Maintain the settings as defined in the table.

f) Choose Save.

© Copyright. All rights reserved.

83


Unit 4: Creation of Transportation Requirements

2. What is the purpose of the Rule for Pick-Up/Delivery Window?

The  purpose  of  the  Rule  for  Pick-Up/Delivery  Window  determination  is  to  define  the
acceptable and requested start and end times for pick-up and delivery.

3. Which strategies can be used based on the freight unit type?

Based  on  the  freight  unit  type,  you  can  define  a  creation  strategy,  change  controller
strategy, save strategy and deletion strategy.

4. Check the condition Z_FU_TYPE_S4611 that will determine your freight unit type.

Note:
Do not make any changes to this condition.

a) In the SAP Fiori launchpad, go to Profiles and Settings → Edit Condition.

b) Select Condition Z_FU_TYPE_S4611.

c) Choose Continue.

Which criteria is used in condition Z_FU_TYPE_S4611 to determine your freight unit type?

Freight unit type determination is based on the consignee (left column in decision table of
condition Z_FU_TYPE_S4611).

5. From which object / process step is condition Z_FU_TYPE_S4611 triggered?

Condition  Z_FU_TYPE_S4611  is  used  to  determine  the  freight  unit  type  because  it  is
defined here as document type determination condition.

a) In the SAP Fiori launchpad, go to Profiles and Settings → Edit Freight Unit Building

Rule.

b) Select Freight Unit Building Rule FUBR_S4611.

c) Choose Continue.

84

© Copyright. All rights reserved.


Lesson: Creating Freight Units

## LESSON SUMMARY
You should now be able to:

● Define freight unit types

● Create freight units and freight unit building rules

© Copyright. All rights reserved.

85


Unit 4
Lesson 3

Defining Conditions

## LESSON OBJECTIVES
After completing this lesson, you will be able to:

● Determine the conditions used to customize a business process

● Display a condition

## Defining Conditions
In this lesson, we examine how conditions are used in TM. Conditions provide a means (of
configuration) to flexibly maintain project-specific requirements. For example, conditions can
be used in the determination of business document types, the determination of a freight unit
building rule, or the determination of organizational units.

Conditions Can Determine Dependent Values

● Determine freight unit building rules (FUB rules)

● Determine freight unit types

● Determine organizational units

● Determine change controller strategies

● Determine pickup and delivery time windows

Conditions can be used throughout TM to represent project/customer-specific rule-based
decisions. They are based on field content which is stored in business documents. The
system uses standard operators (that is, greater than, less than, equal to, and so on) to
compare field values with the customer conditions in a true/false decision-making process.
The values can be defined in the Business Rule Framework plus (BRF+) decision table. Using
the Data Access Definition tab, you define the criteria for which you want to determine
different parameters.

Let's say that you want to define the freight unit building rules that the system uses when
dealing with dangerous goods and with goods that are not dangerous. Basically, there are
three things to consider, as follows:

● An input

● A decision (based on the input and a condition that you have specified)

● An output

In this example, the input value that it is important for the decision to take into account is
whether or not the goods comprising the delivery are dangerous. You can define this using a
data access definition.

86

© Copyright. All rights reserved.


## Lesson: Defining Conditions

The decision itself is based on the input value and a condition. The condition is based on a
condition type, and specifies what should happen in response to a specified input value.

The output value is the result of the decision. In this example, it will be a specific freight unit
building rule.

Conditions, Input Values, and Output Values

● Origin of Condition:

- Direct Business Object Access

- BRF+ Decision Table

- BRF+ Expression

●

Input Value, determined by the following factors:

- Direct Business Object Access

- Data Crawler

- Determination Class

● Output Values:

- Depending on Condition Type (field or structure)

Conditions can have different origins. In SAP TM, there are three different origins:

● The Direct Business Object Access condition returns directly the value determined by the

data access definition. There is no evaluation of the data.

● The BRFplus Decision Table condition takes the input of the data access definition(s) and
evaluates it in a table. This condition table can be maintained from the condition user
interface.

● The BRFplus Expression can be maintained in the form of nested if/then statements.

Define input values for each condition by defining business object fields including user-
specific fields, or values determined in external determination classes. The available input
values depend on the condition type chosen. If you need additional fields for the condition
types to be delivered as standard, or if you want to use customer condition types, create new
data access definitions and extend the assignments in Customizing. You can also change or
add to the data access definitions used by default.

The condition type defines the area in which the system is to take the condition into account.
SAP delivers a number of condition types in the standard system. The condition type must be
identified when defining a condition in TM. A condition type is a configurable object that is
based on field contents stored in various business object nodes. Each condition type is
assigned to a business object (structure) and the node name.

When defining a condition type, you can identify when a result is found, if it is stored in a
structure, and whether one or more conditions may exist for this condition type. The output
values are determined by the condition type. For example, the FUB rule is a result of FUB rule
determination.

The system generates a BRF+ decision table from input and output values. The system
processes this table from top to bottom during determination. When the system finds a row in
the BRFplus decision table whose input values match the current input values, it copies the
corresponding output values and processes them in the area that made the call.

© Copyright. All rights reserved.

87


Unit 4: Creation of Transportation Requirements

## Create Sales Orders and Deliveries

Simulation: How to View Freight Units and Deliveries

For more information on How to View Freight Units and Deliveries, please view
the simulation in the lesson Defining Conditions in your online course.

## Simulation: Create Sales Orders and Deliveries

For more information on Create Sales Orders and Deliveries, please view the
simulation in the lesson Defining Conditions in your online course.

88

© Copyright. All rights reserved.


Unit 4
Exercise 4

Create Sales Orders and Deliveries

## Business Example

You are a consultant and want to show your customer how to work with transportation
functionality in SAP S/4HANA. A prerequisite to use basic shipping functionalities are
deliveries. For this purpose, you want to create three sales orders for different customers and
corresponding to these three sales orders also three deliveries. You want to show that basic
shipping functionality is independent of whether you use or do not use packaging information.
Therefore, you pack only one delivery.

Note:
In this exercise, when you see ##, replace the characters with the two-digit
number (01 to 30) assigned to you by your instructor.

1. Create a sales order for customer TMBS##-01 with order type ZTMB. Use the following

organizational data:

Sales Organization: 1010

Distribution Channel: 10

Division: 00

You want to sell 1 PC of material TM-MAT-01 and the customer reference is 12345##.

Note down the order number of your Sales Order.

____________________________________________

2. Create a sales order for customer TMBS##-02 with order type ZTMB. Use the following

organizational data:

Sales Organization: 1010

Distribution Channel: 10

Division: 00

You want to sell 2 PC of material TM-MAT-01 and the customer reference is 12345##.

Note down the order number of your Sales Order.

____________________________________________

3. Create a sales order for customer TMBS##-03 with order type ZTMB. Use the following

organizational data:

Sales Organization: 1010

Distribution Channel: 10

Division: 00

© Copyright. All rights reserved.

89


## Unit 4: Creation of Transportation Requirements

You want to sell 3 PC of material TM-MAT-01 and the customer reference is 12345##.

Note down the order number of your Sales Order.

____________________________________________

4. Create deliveries for the three sales orders created in the previous steps and note down

Sales Order No.

Delivery No.

the delivery numbers.

Customer

TMBS##-01

TMBS##-02

TMBS##-03

5. Pack the 2 PCs of material TM-MAT-01 which are included in the delivery to customer

TMBS##-02 into one handling unit using packaging material T-PKP100.

6. How many freight units are displayed on your query Freight Units BS##?

7. Verify the packaging data in your freight unit to customer TMBS##-02. What is the total

gross weight of the freight unit and how is it calculated?

8. What is acceptable end date for the delivery at customer location TMBS##-02?

9. What are the predecessor documents of this freight unit?

10. What is the lifecycle status and the planning status of the freight unit?

90

© Copyright. All rights reserved.


Unit 4
Solution 4

Create Sales Orders and Deliveries

## Business Example

You are a consultant and want to show your customer how to work with transportation
functionality in SAP S/4HANA. A prerequisite to use basic shipping functionalities are
deliveries. For this purpose, you want to create three sales orders for different customers and
corresponding to these three sales orders also three deliveries. You want to show that basic
shipping functionality is independent of whether you use or do not use packaging information.
Therefore, you pack only one delivery.

Note:
In this exercise, when you see ##, replace the characters with the two-digit
number (01 to 30) assigned to you by your instructor.

1. Create a sales order for customer TMBS##-01 with order type ZTMB. Use the following

organizational data:

Sales Organization: 1010

Distribution Channel: 10

Division: 00

You want to sell 1 PC of material TM-MAT-01 and the customer reference is 12345##.

a) In the SAP Fiori launchpad, go to Sales Documents → Create Sales Orders.

b) Enter the following information:

Order Type: ZTMB

Sales Organization: 1010

Distribution Channel: 10

Division: 00

c) Choose Continue.

d) Enter the following data:

Sold-to-Party: TMBS##-01

Customer Reference: 12345##

Material: TM-MAT-01

Order Quantity: 1

e) Choose Save.

The order number is displayed on the bottom of the screen.

© Copyright. All rights reserved.

91


Unit 4: Creation of Transportation Requirements

Note down the order number of your Sales Order.

____________________________________________

2. Create a sales order for customer TMBS##-02 with order type ZTMB. Use the following

organizational data:

Sales Organization: 1010

Distribution Channel: 10

Division: 00

You want to sell 2 PC of material TM-MAT-01 and the customer reference is 12345##.

a) In the SAP Fiori launchpad, go to Sales Documents → Create Sales Orders.

b) Enter the following information:

Order Type: ZTMB

Sales Organization: 1010

Distribution Channel: 10

Division: 00

c) Choose Continue.

d) Enter the following data:

Sold-to-Party: TMBS##-02

Customer Reference: 12345##

Material: TM-MAT-01

Order Quantity: 2

e) Choose Save.

The order number is displayed on the bottom of the screen.

Note down the order number of your Sales Order.

____________________________________________

3. Create a sales order for customer TMBS##-03 with order type ZTMB. Use the following

organizational data:

Sales Organization: 1010

Distribution Channel: 10

Division: 00

You want to sell 3 PC of material TM-MAT-01 and the customer reference is 12345##.

a) In the SAP Fiori launchpad, go to Sales Documents → Create Sales Orders.

b) Enter the following information:

Order Type: ZTMB

Sales Organization: 1010

Distribution Channel: 10

Division: 00

92

© Copyright. All rights reserved.


Lesson: Defining Conditions

c) Choose Continue.

d) Enter the following data:

Sold-to-Party: TMBS##-03

Customer Reference: 12345##

Material: TM-MAT-01

Order Quantity: 3

e) Choose Save.

The order number is displayed on the bottom of the screen.

Note down the order number of your Sales Order.

____________________________________________

4. Create deliveries for the three sales orders created in the previous steps and note down

Sales Order No.

Delivery No.

the delivery numbers.

Customer

TMBS##-01

TMBS##-02

TMBS##-03

a) In the SAP Fiori launchpad, go to Shipping and Warehouse Management  →  Create

Outbound Deliveries.

b) Fill in the following filters:

## Ship-to-party: TMBS##*

Planned Creation Date: Remove filter

c) Choose Go.

d) Select the three sales orders.

e) Choose Create Deliveries.

f) Choose Display Logs.

g) Enter the delivery numbers by Ship-to-party (customer) in the spaces provided.

5. Pack the 2 PCs of material TM-MAT-01 which are included in the delivery to customer

TMBS##-02 into one handling unit using packaging material T-PKP100.

a) In the SAP Fiori launchpad, go to Shipping and Warehouse Management  →  Change

Outbound Delivery.

b) For Outbound Delivery, enter the Delivery number for customer TMBS##-02.

c) Choose Continue.

d) Choose Pack.

e) If a dialog box appears, choose Continue.

© Copyright. All rights reserved.

93


## Unit 4: Creation of Transportation Requirements

f) To create a handling unit in the upper part of the screen, enter packaging material as

T-PKP100.

g) Select the handling unit (in the upper part of the screen) and the material (in the lower

part of the screen) and choose Pack.

h) Choose Save.

6. How many freight units are displayed on your query Freight Units BS##?

There are three freight units displayed. There is one freight unit for each delivery.

a) In the SAP Fiori launchpad, go to Logistics Integration → Delivery Integration

(Worklist).

b) Select your Freight Units BS## query.

c) Press Refresh to refresh the content of your query.

7. Verify the packaging data in your freight unit to customer TMBS##-02. What is the total

gross weight of the freight unit and how is it calculated?

The  total  gross  weight  is  1392  KG.  It  is  calculated  as  the  gross  weight  of  material  TM-
MAT-01 (1370 kg) and the tare weight of the packaging material T-PKP100 (22 kg).

a) Click the link (Document) of your freight unit to customer TMBS##-02.

b) Expand the Items section on the bottom of the screen.

c) Verify that the item structure consists of one PC of package (T-PKP100) and 2 PCs of

product (TM-MAT-01).

8. What is acceptable end date for the delivery at customer location TMBS##-02?

The acceptable end date for the delivery varies, but is approximately 3 weeks in the future
(from today).

a) On the General Data tab, check the End Date (Acceptable) at the destination location.

9. What are the predecessor documents of this freight unit?

Check the Document Flow tab. The predecessor documents are the outbound delivery and
sales order.

10. What is the lifecycle status and the planning status of the freight unit?

The status is displayed on the Statuses tab.

a) Check the Statuses tab.

Lifecycle Status

New

94

© Copyright. All rights reserved.


Planning Status

## Not Planned

Lesson: Defining Conditions

© Copyright. All rights reserved.

95


Unit 4: Creation of Transportation Requirements

## LESSON SUMMARY
You should now be able to:

● Determine the conditions used to customize a business process

● Display a condition

96

© Copyright. All rights reserved.


Unit 4

## Learning Assessment

1. What are triggers for a delivery update by TM?

Choose the correct answers.

X A Packing items into a handling unit

## X B Changing the dates on a freight order

X C Re-assigning freight units to a freight order with different dates

2. Which of the following may be the result of a shipment block on a sales order in TM?

Choose the correct answers.

X A Planning block

X B Execution block

## X C Invoicing block

3. A handling unit can be represented by several freight units in SAP TM.

Determine whether this statement is true or false.

X True

## X False

4. A freight unit can only be assigned to a single freight order or freight booking.

Determine whether this statement is true or false.

X True

## X False

© Copyright. All rights reserved.

97


## Unit 4: Learning Assessment

5. What are allowed relationships between freight units and handling units?

Choose the correct answers.

X A 1:1

X B 1:n

X C n:1

6. How are input values for a condition determined?

Choose the correct answers.

X A Using direct business object access

X B Using the data crawler

X C Using a determination class

X D Using a process controller strategy

98

© Copyright. All rights reserved.


UNIT 5 Transportation Planning

Lesson 1

Creating Freight Orders and Freight Bookings

Exercise 5: Create Freight Order Types and Freight Orders

Lesson 2

## Subcontracting to Carriers

Exercise 6: Subcontract a Freight Order to a Carrier

100

109

115

119

## UNIT OBJECTIVES

● Define freight order types

● Create freight orders for road transportation

● Explain and configure the short-cut process

● Assign carriers to freight orders

● Explain status changes in the carrier assignment process

© Copyright. All rights reserved.

99


Unit 5
Lesson 1

Creating Freight Orders and Freight Bookings

## LESSON OBJECTIVES
After completing this lesson, you will be able to:

● Define freight order types

● Create freight orders for road transportation

● Explain and configure the short-cut process

## Freight Orders and Freight Bookings
Freight orders and freight bookings are the result of transportation planning and the freight
document for execution.

Freight orders represent a single shipment or load departing from one of your facilities
(outbound scenario) or arriving in one of your facilities (inbound scenario).

The goal of planning in Transport Management (TM) is to enable customers to (manually)
plan their transportation requirements (deliveries). This includes the ability to perform order
consolidation, where a company can group deliveries with the same ship-from and ship-to
locations for more efficient transportation quantities. If multiple deliveries are being shipped
within a predefined transportation zone, your company can schedule and route the multiple
deliveries efficiently, and chose the appropriate carrier.

Order consolidation is the grouping of orders with the same ship-from and ship-to locations to
create more efficient shipment quantities. The result of order consolidation is that one or
more freight units are combined into one freight order. A freight unit is a business object
representing the smallest possible transportation unit. Business examples of order
consolidation are multiple orders that have been received over time and can be planned to be
shipped together. This can be at individual line item level. Customers who make-to-order, and
do not ship complete orders to their customers, may consolidate line items from multiple
orders as they are produced and as their delivery-due lists are created.

TM supports different transportation modes. Depending on the transportation modes,
different execution documents are created in TM. For transportation mode Air and Sea,
freight bookings are created in TM. For all other transportation modes, freight orders are
created.

## Freight Order Types
A freight order type defines parameters that influence how the system processes the freight
order. When manually creating a freight order, the user has to select a freight order type.

100

© Copyright. All rights reserved.


Lesson: Creating Freight Orders and Freight Bookings

Figure 73: Freight Order Type Customizing

## Animation: Freight Order Type Customizing

For more information on Freight Order Type Customizing, please view the
animation in the lesson Creating Freight Orders and Freight Bookings in your
online course.

The following are some of the settings that can be configured in the freight order type:

● Basic Settings:

- Determining shipper and ship-to-party

- Specifying if a freight order can be subcontracted

- Defining whether a freight order is to be deleted or only canceled

● Charge Calculation and Settlement Document Settings:

-

-

Enabling charges and settlement

Enable cost distribution

● Execution Settings

● Organizational Unit Determination:

You can define how the system determines the purchasing organization and the execution
organization.

● Change Controller Settings:

You can define settings for the change controller, for example, a default change strategy
and a condition for change strategy determination.

© Copyright. All rights reserved.

101


Unit 5: Transportation Planning

● Output Options:

You can define an output profile and a text schema, for example.

Organizational Unit Determination

## Figure 75: Organizational Unit Determination

You can configure the automatic determination of the purchasing/execution organizations in
freight documents.

Automatic determination can be customized in the freight order or freight booking document
types in the following ways: with a default organization assignment, based on the user
assignment, and by specifying an organization determination condition of type /SCMTMS/
TOR_ORGUNIT.

The system first checks the condition. If you have not entered a condition, or if the condition
does not return a result, the system checks whether the Consider Organizational Unit of User
checkbox is selected, and whether the user is assigned to a purchasing organization and/or
an execution organization. If the checkbox is not selected or the user is not assigned to a
purchasing organization and/or an execution organization, the system uses the data
maintained as default organization.

102

© Copyright. All rights reserved.


Lesson: Creating Freight Orders and Freight Bookings

Sequence Type of Stages

## Figure 76: Sequence Type of Stages

The following sequence types are available for freight order types:

● Defined and Linear: The sequence of stages is linear, which means that there is a single
start stage and all other stages have one predecessor stage. There is also a single end
stage and all other stages have one successor stage.

● Non-Linear (Star-Shaped): All stages have the same start location but different end
locations. The graphical structure of the transportation chain has a star shape.

● Disconnected: All stages are separate from each other and each stage has its own start

and end location.

● Star-Shaped Based on FU Stages: Based on the information from the freight units, the

stages have the same start location but different end locations.

● Star-Shaped Based on FU Stages (Reversed): Based on the information from the freight

units, the stages have the same end location but different start locations.

How to View Star-Shaped Freight Order Types

Simulation: How to View Star-Shaped Freight Order Types

For more information on How to View Star-Shaped Freight Order Types, please
view the simulation in the lesson Creating Freight Orders and Freight Bookings in
your online course.

© Copyright. All rights reserved.

103


Unit 5: Transportation Planning

## Freight Order Creation

## Figure 78: Creating Freight Unit Stages

Freight units can have one or more stages. Stages can be created in the freight unit to split
the overall transportation chain, for example, based on the mode of transportation. A freight
unit with a source in Germany and destination in the US, may be split into three stages to
reflect:

● Pre-carriage from source to port-of-loading (PoL)

● Main-carriage from port of loading to port of discharge (PoD)

● On-carriage from port of discharge to destination

In this way, the individual stages may be used to create separate freight orders/freight
bookings for each stage to subcontract these different stages to three different business
partners/carriers.

Freight orders are the result of planning and the consolidation of freight units on a vehicle-
booked capacity or scheduled means of transport. Once this has been completed, transport
order execution can be triggered and follow-on settlement processing can begin.

Note:
Please note that an advanced transportation management license is required if a
freight order is picking up at (outbound) or delivering to (inbound) multiple
shipping / receiving points.

104

© Copyright. All rights reserved.


Lesson: Creating Freight Orders and Freight Bookings

## Freight Orders

Figure 79: Freight Orders

## Animation: Freight Orders

For more information on Freight Orders, please view the animation in the lesson
Creating Freight Orders and Freight Bookings in your online course.

Freight orders/bookings contain the following:

● Planning information, for example, planned means of transport and stages, routing,

planned pickup and delivery dates, durations, and distances

● Document dependencies, as well as predecessor and successor documents

● Transportation charges and cost distribution

● Cargo information: quantities and weights, goods information

● Execution information

● Business partner information

● Output management

● Status information and blocking information

● Subcontracting Information

© Copyright. All rights reserved.

105


Unit 5: Transportation Planning

Creating Freight Orders

## Figure 81: Creating Freight Orders

Manual creation is generally used when you already know the most important transportation
data, such as source location, destination location, and business partner, because you
regularly transport goods for a certain customer using a certain carrier.

To manually create a freight order, you require the following information: general data for the
freight order (shipper, consignee, carrier, resource, locations, dates and times, and terms of
payment), information about any additional intermediate stops, the items involved (add
freight units to the freight order or enter the items directly on the freight order), and
information about the charges involved (as calculated, or configure the system to calculate
charges).

Once the required information has been entered, you can check the consistency and save the
freight order. The freight order can then be sent over to the carrier and confirmed or rejected
on behalf of the carrier. Necessary documents can be printed, and a freight settlement
document created after the execution

Some of the information like source and destination location are automatically populated in
the freight order, if you create the freight order from the freight unit worklist.

You can create a freight order by copying an existing one (a reference document). The system
copies the header data and the logistical data. However, it does not copy references to freight
units and execution information.

Finally, you have the option to create freight orders via webservice. The Service
Transportation Order Generic Request can be used for inbound and outbound communication
scenarios to exchange freight orders or freight bookings. See note 2474539 for details.

106

© Copyright. All rights reserved.


Lesson: Creating Freight Orders and Freight Bookings

Note:
Please note that when the freight order is scheduled, that is its dates are
determined, only embedded scheduling is allowed as part of (basic)
transportation management.

Create Freight Order Types and Freight Orders

Simulation: Create Freight Order Types and Freight Orders

For more information on Create Freight Order Types and Freight Orders, please
view the simulation in the lesson Creating Freight Orders and Freight Bookings in
your online course.

© Copyright. All rights reserved.

107


Unit 5: Transportation Planning

108

© Copyright. All rights reserved.


Unit 5
Exercise 5

Create Freight Order Types and Freight Orders

## Business Example

As a consultant responsible for the configuration of a basic shipping scenario in SAP
S/4HANA, you need to show your customer how to create freight order types and how to
create freight orders for these document types.

Note:
In this exercise, when you see ##, replace the characters with the two-digit
number (01 to 30) assigned to you by your instructor.

1. Create a freight order type TM## with the settings in the table:

Freight Order Type

## TM##

## Description

Freight Order TM##

Number Range Interval

Transportation Mode

03

01

Freight Order Can be Subcontracted

Relevant for Subcontracting

Sequence Type of Stages

## Defined And Linear

Shipper/Ship-To-Party Determination

Determination Based on Predecessor Doc.

Planning Profile

Output Profile

PLAN_S4611

/SCMTMS/TOR_PRINT_ROAD

Document Creation Relevance

No External Document Creation

Purchasing Organization

50000721

Enable Charge Calculation

Enable Settlement

Enable Cost Distribution

Selected

Selected

## Selected

Default FSD Type

Freight Settlement S4611

Default Change Strategy

## DEF_CHACO

Web Dynpro Application Configuration

/SCMTMS/FRE_ORDER

© Copyright. All rights reserved.

109


## Unit 5: Transportation Planning

2. What are the options that you can choose from for the Sequence Type of Stages? What

are they used for?

3. Create a freight order with freight order type TM##. Assign vehicle group ZTK and vehicle
type ZTRUCK to the freight order. Finally, assign the three freight units created in the
previous exercise to this freight order.

4. What is the total gross weight of the freight order?

5. What is the maximum utilization of the freight order?

6. Change the sequence of stages of your freight order, such that you first visit the customer
in Stuttgart (TMBS##-03), second the customer in Karlsruhe (TMBS##-02), and last the
customer in Mannheim (TMBS##-01).

7. What is the planned departure time at shipping point SP_1010 and planned arrival time at

the last stop at customer TMBS##-01 of the freight order?

8. Save your freight order and note down the freight order number.

Freight Order Number

_____________________________

110

© Copyright. All rights reserved.


Unit 5
Solution 5

Create Freight Order Types and Freight Orders

## Business Example

As a consultant responsible for the configuration of a basic shipping scenario in SAP
S/4HANA, you need to show your customer how to create freight order types and how to
create freight orders for these document types.

Note:
In this exercise, when you see ##, replace the characters with the two-digit
number (01 to 30) assigned to you by your instructor.

1. Create a freight order type TM## with the settings in the table:

Freight Order Type

## TM##

## Description

Freight Order TM##

Number Range Interval

Transportation Mode

03

01

Freight Order Can be Subcontracted

Relevant for Subcontracting

Sequence Type of Stages

## Defined And Linear

Shipper/Ship-To-Party Determination

Determination Based on Predecessor Doc.

Planning Profile

Output Profile

PLAN_S4611

/SCMTMS/TOR_PRINT_ROAD

Document Creation Relevance

No External Document Creation

Purchasing Organization

50000721

Enable Charge Calculation

Enable Settlement

Enable Cost Distribution

Selected

Selected

## Selected

Default FSD Type

Freight Settlement S4611

Default Change Strategy

## DEF_CHACO

Web Dynpro Application Configuration

/SCMTMS/FRE_ORDER

© Copyright. All rights reserved.

111


## Unit 5: Transportation Planning

a) In the back-end system, go to Customizing by entering transaction code spro.

b) Choose SAP Reference IMG.

c) In Customizing, go to Transportation Management → Freight Order

Management → Freight Order → Define Freight Order Types.

d) Choose New Entries.

e) Maintain the settings as provided in the table.

f) Choose Save.

2. What are the options that you can choose from for the Sequence Type of Stages? What

are they used for?

The F1-help explains the different concepts for the sequence type of stages.

a) Open the drop-down menu for Sequence Type of Stages.

b) Select the F1-help to understand what the options are used for.

You can choose between the following options:

● Defined and Linear

● Non-Linear (Star-Shaped)

● Star-Shaped based on FU-stages

● Star-Shaped based on FU-stages (reversed)

● Linear with (De-)Consolidation Stages

● Disconnected

● Undefined

3. Create a freight order with freight order type TM##. Assign vehicle group ZTK and vehicle
type ZTRUCK to the freight order. Finally, assign the three freight units created in the
previous exercise to this freight order.

a) In the SAP Fiori launchpad, go to Order Management → Create Road Freight Order.

b) Enter Freight Order Type: TM##.

c) Choose Continue.

d) Navigate to the Items tab.

e) Select the Active Vehicle.

f) On the Details tab for the active vehicle, enter vehicle group ZTK and vehicle type

ZTRUCK.

g) Choose Insert →  Insert FU based on Freight Unit ID.

h) In the dialog box, enter the three freight unit numbers created in the previous exercise

and choose OK.

i) Save the freight order.

112

© Copyright. All rights reserved.


Lesson: Creating Freight Orders and Freight Bookings

4. What is the total gross weight of the freight order?

The total gross weight is 4,132 kg.

a) On the Items tab, you can find the gross weight: 4,132 kg.

b) On the General Data tab, you can find the total cargo weight: 4,132 kg.

5. What is the maximum utilization of the freight order?

The maximum utilization is 21 %.

a) On the General Data tab, you can find the maximum utilization: 21 %.

6. Change the sequence of stages of your freight order, such that you first visit the customer
in Stuttgart (TMBS##-03), second the customer in Karlsruhe (TMBS##-02), and last the
customer in Mannheim (TMBS##-01).

a) On the Overview tab, select the line to location TMBS##-03 and choose Move-up, so

that this customer appears directly after the shipping point SP_1010.

b) On the Overview tab, select the line to location TMBS##-02 and choose Move-up, so

that this customer appears directly after the previous customer TMBS##-03.

c) Choose Save.

7. What is the planned departure time at shipping point SP_1010 and planned arrival time at

the last stop at customer TMBS##-01 of the freight order?

The date/time varies.

a) On the Overview tab, you can find the scheduling result (planned departure and arrival

times for each location).

8. Save your freight order and note down the freight order number.

Freight Order Number

_____________________________

a) Choose Save.

The Freight order number varies.

© Copyright. All rights reserved.

113


Unit 5: Transportation Planning

## LESSON SUMMARY
You should now be able to:

● Define freight order types

● Create freight orders for road transportation

● Explain and configure the short-cut process

114

© Copyright. All rights reserved.


Unit 5
Lesson 2

Subcontracting to Carriers

## LESSON OBJECTIVES
After completing this lesson, you will be able to:

● Assign carriers to freight orders

● Explain status changes in the carrier assignment process

## Subcontracting to Carriers
The carrier is the business partner that you subcontract the freight order to. The carrier can
be different from the executing carrier, which is another business partner role that you can
assign to your freight order, if the carrier itself subcontracts the execution of the freight order
to a third party. That way, you have the options to differentiate between the party you
contracted with and the party actually executing the freight move.

## Figure 83: Assigning Carriers

There are two different ways how you can assign a carrier to a freight order manually. You can
individually assign carriers to the freight order in the freight order app or you can use a
worklist for freight orders and use the Mass Change function to assign a carrier to one or
multiple freight orders.

© Copyright. All rights reserved.

115


Unit 5: Transportation Planning

## Animation: Assigning Carriers

For more information on Assigning Carriers, please view the animation in the
lesson Subcontracting to Carriers in your online course.

If you want to assign the carrier to the freight order automatically, there are several options
available:

1. You can assign the carrier to the default route. That way, the carrier is added to the freight

unit when it is created using the freight unit building rule.

2. You can pass the carrier from the delivery directly to the freight unit by maintaining the

carrier with partner function SP - Forwarding Agent into the delivery.

3. You can retrieve the carrier from the partner determination profile, that you assign to the
freight order type when you have assigned the carrier as a fixed business partner for
business partner role Carrier in the partner determination profile.

4. You can implement a BAdI logic and retrieve the carrier via this logic through the partner
determination profile that you assign to the freight order type when you have selected
BAdI for business partner role Carrier in the partner determination profile (this requires
custom code).

5. You can implement a process controller strategy (for example, creation strategy) that you

assign to your freight order type (this requires custom code).

Status Management in Subcontracting

## Figure 85: Status Management in Subcontracting

The figure Status Management in Subcontracting shows which statuses change during the
subcontracting process. Within (basic) transportation management only manual award
confirmation is supported as part of the tendering process.

116

© Copyright. All rights reserved.


Lesson: Subcontracting to Carriers

Subcontract a Freight Order to a Carrier

Simulation: Subcontract a Freight Order to a Carrier

For more information on Subcontract a Freight Order to a Carrier, please view
the simulation in the lesson Subcontracting to Carriers in your online course.

© Copyright. All rights reserved.

117


Unit 5: Transportation Planning

118

© Copyright. All rights reserved.


Unit 5
Exercise 6

Subcontract a Freight Order to a Carrier

## Business Example

You want to show your customer how a freight order is subcontracted to a carrier and how the
statues of the freight order change in the subcontracting process.

Note:
In this exercise, when you see ##, replace the characters with the two-digit
number (01 to 30) assigned to you by your instructor.

1. Assign carrier CAR_TM3_## to your freight order created in the previous exercise.

2. What is the life cycle status of the freight order? What is the subcontracting status of the

freight order? What is the execution status of the freight order?

## Lifecycle Status

________________________________

## Subcontracting Status

________________________________

## Execution Status

________________________________

3. Send the subcontracting information to the carrier. What is the life cycle status of the
freight order? What is the subcontracting status of the freight order? What is the
confirmation status of the freight order? What is the execution status of the freight order?

## Lifecycle Status

________________________________

## Subcontracting Status

________________________________

## Confirmation Status

________________________________

## Execution Status

________________________________

4. The carrier calls you to confirm the freight order. Change the freight order to acknowledge

the status change. What is the life cycle status of the freight order? What is the
subcontracting status of the freight order? What is the confirmation status of the freight
order? What is the execution status of the freight order?

## Lifecycle Status

________________________________

## Subcontracting Status

________________________________

## Confirmation Status

________________________________

## Execution Status

________________________________

© Copyright. All rights reserved.

119


Unit 5
Solution 6

Subcontract a Freight Order to a Carrier

## Business Example

You want to show your customer how a freight order is subcontracted to a carrier and how the
statues of the freight order change in the subcontracting process.

Note:
In this exercise, when you see ##, replace the characters with the two-digit
number (01 to 30) assigned to you by your instructor.

1. Assign carrier CAR_TM3_## to your freight order created in the previous exercise.

a) In the SAP Fiori launchpad, go to Order Management → Freight Order (Worklist).

b) Select the All Road Freight Orders query and press Refresh.

c) Filter the query for your freight order type TM## (by selecting the column header

Document Type and choosing document type TM## in the dropdown list).

d) Open your freight order by clicking the document number.

e) Press Edit.

f) On the General Data tab, enter Transportation – Carrier: CAR_TM3_##.

g) Choose Save.

2. What is the life cycle status of the freight order? What is the subcontracting status of the

freight order? What is the execution status of the freight order?

## Lifecycle Status

________________________________

## Subcontracting Status

________________________________

## Execution Status

________________________________

a) Navigate to the Statuses tab of the freight order.

Lifecycle Status

## In Process

Subcontracting Status

Carrier Assigned

Execution Status

## Not Started

3. Send the subcontracting information to the carrier. What is the life cycle status of the
freight order? What is the subcontracting status of the freight order? What is the
confirmation status of the freight order? What is the execution status of the freight order?

120

© Copyright. All rights reserved.


Lesson: Subcontracting to Carriers

## Lifecycle Status

________________________________

## Subcontracting Status

________________________________

## Confirmation Status

________________________________

## Execution Status

________________________________

a) From the dropdown menu, choose Subcontracting → Send to Carrier.

b) Choose Save.

c) Navigate to the Statuses tab of the freight order.

Lifecycle Status

Subcontracting Status

In Process

## Sent

Confirmation Status

No Confirmation Yet

Execution Status

## Not Started

4. The carrier calls you to confirm the freight order. Change the freight order to acknowledge

the status change. What is the life cycle status of the freight order? What is the
subcontracting status of the freight order? What is the confirmation status of the freight
order? What is the execution status of the freight order?

## Lifecycle Status

________________________________

## Subcontracting Status

________________________________

## Confirmation Status

________________________________

## Execution Status

________________________________

a) From the dropdown menu, choose Subcontracting → Set to confirmed by carrier.

b) Choose Save.

c) Navigate to the Statuses tab of the freight order.

Lifecycle Status

Subcontracting Status

Confirmation Status

Execution Status

In Process

## Sent

Confirmed

## Not Started

© Copyright. All rights reserved.

121


Unit 5: Transportation Planning

## LESSON SUMMARY
You should now be able to:

● Assign carriers to freight orders

● Explain status changes in the carrier assignment process

122

© Copyright. All rights reserved.


Unit 5

## Learning Assessment

1. Which method of freight order creation is available within basic transportation

management scope?

Choose the correct answers.

## X A Manual Creation

X B Creation via Background Report

X C Creation using the VSR Optimizer

## X D Creation by Copying

2. When automatically determining organizational units in freight orders, which of the

following does the system check first?

Choose the correct answer.

X A Whether the user is assigned to a purchasing organization.

X B Whether the Consider Organization Unit of User checkbox is selected.

X C Whether there is a condition in the Condition field.

X D Whether the user is assigned to an execution organization.

3. For which of the following transportation modes does TM create freight bookings?

Choose the correct answers.

X A Air

X B Road

X C Rail

## X D Sea

4. The carrier is the business partner that you subcontract the freight order to.

Determine whether this statement is true or false.

X True

## X False

© Copyright. All rights reserved.

123


Unit 5: Learning Assessment

124

© Copyright. All rights reserved.


UNIT 6 Transportation Execution

Lesson 1

Describing Freight and Transport Execution

Lesson 2

Creating (Print) Freight Documents

Exercise 7: Create Freight Documents

Lesson 3

Exploring Warehouse Integrations

Exercise 8: Pick, Load, and Post Goods Issue

127

129

135

139

145

## UNIT OBJECTIVES

● Describe the freight and transport execution process in transportation management

● Understand the integration in SAP S/4HANA and basic shipping in transportation

execution processes

● Check relevant customizing for BOPF PPF Settings

● Generate outputs for your freight order and preview the documents

● Understand the Output Management in Basic Shipping

● Pick and load the demands on the delivery

● Post goods issue for the deliveries

© Copyright. All rights reserved.

125


Unit 6: Transportation Execution

126

© Copyright. All rights reserved.


Unit 6
Lesson 1

Describing Freight and Transport Execution

## LESSON OBJECTIVES
After completing this lesson, you will be able to:

● Describe the freight and transport execution process in transportation management

● Understand the integration in SAP S/4HANA and basic shipping in transportation

execution processes

## Transportation Execution
In this lesson, we look into the transportation execution and monitoring process and
corresponding functionalities in Transportation Management. With the (basic) transportation
management solution the system supports employees working in logistics departments of a
shipper to fulfill their responsibilities in a compliant manner and create an audit trail with full
transparency for the cargo movement.

In the previous lessons, the focus was on how to use the TM functionality to identify
transportation requirements and to record, plan and subcontract them. The cargo (pallets,
containers, and so on) were not loaded yet. Freight movement processes are executed and
monitored in the Freight Order Management.

In the Freight Order Management component within (basic) transportation management, not
only the planning phase is supported. It is also used until the vehicle has left the loading
location and for status tracking even after the departure the freight order is the central
document containing all transport execution relevant information.

## Figure 87: Transportation Execution Process

Before and during execution, the Freight Order Management component allows you to create
documents related to the cargo movement and its compliance to document actual quantities

© Copyright. All rights reserved.

127


## Unit 6: Transportation Execution

and details of the cargo. You can record discrepancies that occur between order and
execution time. Moving the cargo can also be documented in the loading status manually in
SAP TM.

The execution of the freight order can be monitored on the Execution tab of the freight order
using local events (not integrated to SAP Event Management within the (basic) transportation
management scope). External events can be reported via the TOR_GENERIC web service. The
webservice TransportationEventBulkNotofication to integrate into Global Track and Trace
(GTT) can only be used within (basic) transportation management if LBN is licensed. In
addition, milestone tracking is supported via LBN. Status handling is supported in the freight
order and reflected on the Statuses tab of the freight order.

On the Items tab of the freight order, you can create local container or package items. (Basic)
transportation management also allows the creation of cross delivery handling units manually
by assigning several freight units into one package item locally in the freight order. In the item
structure of the freight order you can also maintain seal data.

## LESSON SUMMARY
You should now be able to:

● Describe the freight and transport execution process in transportation management

● Understand the integration in SAP S/4HANA and basic shipping in transportation

execution processes

128

© Copyright. All rights reserved.


Unit 6
Lesson 2

Creating (Print) Freight Documents

## LESSON OBJECTIVES
After completing this lesson, you will be able to:

● Check relevant customizing for BOPF PPF Settings

● Generate outputs for your freight order and preview the documents

● Understand the Output Management in Basic Shipping

## Creation of (Print) Freight Documents
In this lesson, you learn how to configure settings to enable the printing of documents in the
freight order.

Before, during and after execution, each of the users and parties involved needs to be notified
when a task is required to be executed or a report on a recent activity is made. Users need to
view the result of business process activities and generate output in response along the
process. Output management automates the output of business documents, such as
printouts, mail or fax to certain events.

Figure 88: Output Types

## Output Management in TM Documents

The Output Management in TM is available for the following documents:

© Copyright. All rights reserved.

129


Unit 6: Transportation Execution

● Freight Units

● Freight Orders

● Freight Bookings

● Freight Agreements

● Freight Settlement Documents

In the previous lesson, you defined a freight order type with an output profile /SCMTMS/
TOR_PRINT_ROAD. The output profiles assigned to TM documents are defined in customizing
as part of the Post Processing Framework (PPF).

You can find the general customizing of PPF under: Cross-Application Components → Process
and Tools for Enterprise Applications → Reusable Objects and Functions for BOPF
Environment → PPF Adapter for Output Management  → Maintain PPF Settings.

Since the Post-Processing Framework (PPF) is used in various SAP Applications, the
customizing relevant to transportation management is linked to application /SCMTMS/
TRANSPORTATION .

Here, you manage the action profiles. An action profile is the smallest set of action definitions
that can be investigated during one call of the action determination of the PPF. Output profiles
defined in document type customizing of transportation management map to action profiles
in PPF.

## Output Management Adapter

PPF can perform the following processing types:

● Trigger alert

● Method Call

● Workflow

● Smart Form Actions

● External Communication (for example, Adobe Document Server Connection)

● BI Data Upload

130

© Copyright. All rights reserved.


Lesson: Creating (Print) Freight Documents

Figure 89: Output Management Adapter

## Animation: Output Management Adapter

For more information on Output Management Adapter, please view the
animation in the lesson Creating (Print) Freight Documents in your online course.

You can connect the PPF at the level of the individual BO nodes. You can also set up PPF
triggers on a BO node specific (use case) basis and specify whether they are critical or non-
critical.

When you selected /SCMTMS/TRANSPORTATION, you can manage the action profiles
assigned to this application. An action profile is the smallest set of action definitions that can
be investigated during one call of the action determination of the PPF.

Each action profile contains a set of multiple action definitions (1:n). An action definition
defines all possible realizations. The realizations are modeled in the so-called processing type.
The processing type represents the technical realization of an action definition, for example
the start of a workflow, sending out a PDF Form by fax or mail. The action definition
determines whether business partner data is required for the execution and the business
partner which the data relates to. An action definition therefore has the character of an
business task and defines the “what” should be done with this action (mail, fax, and so on).

If the system has identified the action, definitions from the action list the conditions come into
place. There are two important types of conditions for the PPF/Output Management.

© Copyright. All rights reserved.

131


Unit 6: Transportation Execution

Output Management Conditions

Figure 91: Output Management Conditions

## Animation: Output Management Conditions

For more information on Output Management Conditions, please view the
animation in the lesson Creating (Print) Freight Documents in your online course.

The first one is the scheduling condition. This condition is checked during the PPF action
determination. It decides whether an action should be executed or not. The identification of
the scheduling condition is done from the assignment to the configured action definition. The
scheduling conditions define the “why” so to say, for example, lifecycle of the predecessor
document is X or document is canceled.

The second important condition is the starting condition. This condition is checked just before
an execution of an action will be started. These conditions should only influence the point in
time when an action will be executed. They define the “when” so to say, for example, they
define that the message is sent “on save”, or “one day before pickup”, and so on.

Post-Processing Framework (PPF)

As a summary you can imagine the PPF as the way to answer the three questions:

● What (should be done in the activity)

● Why (is this activity done)

● When (is the activity done)

Table 3: Post-Processing Framework (PPF) Answers Three Questions

The following table lists some examples:

132

© Copyright. All rights reserved.


Lesson: Creating (Print) Freight Documents

What

## Why

Send whole shipping list via
EDI

Shipping list has been creat-
ed

When

## Next batch job

Send whole shipping list via
mail

Shipping list has been
changed

When saving the document

Send shipping list changes
via fax

Business object is in state “in
## Process”

When saving the document

Output Management Logic

## Figure 93: Output Management Logic

In the /SCMTMS/TRANSPORTATION application, all relevant action profiles are configured.
In the Action Profile /SCMTMS/TOR_PRINT_ROAD the Action Definition shows all defined
actions that are available for this action profile. In this action profile you will find a lot of freight
documents to be triggered during the execution process (for example, CMR, Waybill,
Packaging Labels). Here, you can also define the processing type of the selected document.

## Output Management Capabilities

Output Management provides the following capabilities based on the business document:

● Automated (backend), rule-based dispatching of outbound communications in response

to business events such as creation of an order, saving a document, and so on

● Preview of output and manual (front end) outputs in the user interface (UI)

● Archive output dispatched in relation to business documents

● Mass output from a worklist

© Copyright. All rights reserved.

133


## Unit 6: Transportation Execution

If you want more insights into PPF Settings within SAP S/4HANA, see the setup guides at SAP
Business Suite → SAP Supply Chain Management  → SAP SCM 7.0 → Processes and Tools for
Enterprise Applications (CA-EPT) →  Reusable Objects and Functions for BOPF Environment
(CA-EPT-BRC). Also, see SAP Note 489334.

In general, it is important to note that PPF actions can only process information that is already
saved to the database. This prevents you from accidentally sending preliminary
transportation labels to a spool in the warehouse, for example.

Create Freight Documents

## Simulation: Create Freight Documents

For more information on Create Freight Documents, please view the simulation
in the lesson Creating (Print) Freight Documents in your online course.

134

© Copyright. All rights reserved.


Unit 6
Exercise 7

Create Freight Documents

## Business Example

As a consultant responsible for the configuration of a basic shipping scenario in SAP
S/4HANA, you need to show your customer how to create freight document print outs.

Note:
In this exercise, when you see ##, replace the characters with the two-digit
number (01 to 30) assigned to you by your instructor.

1. You received the information that your freight order is ready for transportation execution.
Set the corresponding status in the freight order to reflect the situation. What is the life
cycle status of the freight order? What is the execution status of the freight order?

## Lifecycle Status

Logistical Execution Status

## Execution Status

2. You want to verify if documents are printed for your freight order, and, if so, which

documents. Where can you find the printed documents?

© Copyright. All rights reserved.

135


Unit 6
Solution 7

Create Freight Documents

## Business Example

As a consultant responsible for the configuration of a basic shipping scenario in SAP
S/4HANA, you need to show your customer how to create freight document print outs.

Note:
In this exercise, when you see ##, replace the characters with the two-digit
number (01 to 30) assigned to you by your instructor.

1. You received the information that your freight order is ready for transportation execution.
Set the corresponding status in the freight order to reflect the situation. What is the life
cycle status of the freight order? What is the execution status of the freight order?

## Lifecycle Status

Logistical Execution Status

## Execution Status

a) In the SAP Fiori launchpad, go to Order Management →  Freight Order (Worklist).

b) Select the All Road Freight Orders query.

c) Filter the query for your freight order type TM## (by selecting the column header

Document Type and choosing document type TM## in the dropdown list).

d) Open your freight order by clicking the document number.

e) Choose Edit.

f) Choose Execution Status → Set to Ready for Transportation Execution.

g) Navigate to the Statuses tab and verify the document statuses.

## Lifecycle Status

Logistical Execution Status

In Process

## Not Loaded

## Execution Status

Ready for Transportation Execution

h) Choose Save.

2. You want to verify if documents are printed for your freight order, and, if so, which

documents. Where can you find the printed documents?

136

© Copyright. All rights reserved.


## Lesson: Creating (Print) Freight Documents

a) In the SAP Fiori launchpad, go to Order Management →  Freight Order (Worklist).

b) Select the All Road Freight Orders query.

c) Filter the query for your freight order type TM## (by selecting the column header

Document Type and choosing document type TM## in the dropdown list).

d) Open your freight order by clicking the document number.

e) Navigate to the Output Management tab. You might need to use the ellipsis ( “…”)

button to see the this tab.

f) In the row for Road Waybill (Europe), click on the Document Preview icon in the Actions

column.
A new tab will open showing the PDF document.

© Copyright. All rights reserved.

137


Unit 6: Transportation Execution

## LESSON SUMMARY
You should now be able to:

● Check relevant customizing for BOPF PPF Settings

● Generate outputs for your freight order and preview the documents

● Understand the Output Management in Basic Shipping

138

© Copyright. All rights reserved.


Unit 6
Lesson 3

Exploring Warehouse Integrations

## LESSON OBJECTIVES
After completing this lesson, you will be able to:

● Pick and load the demands on the delivery

● Post goods issue for the deliveries

## Warehouse Integration
With SAP S/4HANA, there are various ways to model the execution process. This depends on
the complexity of your warehouse processes. SAP offers solutions for warehouse execution
from simple (none) warehouse processes to full scale-out warehouse setups. In (basic)
transportation management all of them are integrated via the delivery.

Ways to Handle Stock in Combination with (Basic) Transportation Management

●

●

## Inventory Management

Inventory Management with Handling Unit Management

● Stockroom Management (former LE-WM)

● Extended Warehouse Management (SAP EWM)

The simplest way to model a process for transport execution is without a dedicated
warehouse setup. Therefore, the transportation demand represents the delivery in logistics
execution which will lead to a freight unit that can be planned on a freight order and the
transportation execution can be started.

© Copyright. All rights reserved.

139


Unit 6: Transportation Execution

## Inventory Management

Figure 95: Inventory Management

## Animation: Inventory Management

For more information on Inventory Management, please view the animation in
the lesson Exploring Warehouse Integrations in your online course.

Note that Handling Unit Management (HUM) is optional and could be used to create deliveries
with Handling Units or just take care of the items itself, for example if you want to model a
very lean process and do not have to take care which item is shipped on what load carrier
system-wise.

If you decide to use Handling Unit Management, the customizing can be found in Logistics –
General  → Handling Unit Management.

## Extended Warehouse Management

For complex setups of your warehouse, maybe even with automated guided vehicles (AGV),
complex conveyer techniques and high frequent warehouses, the SAP Extended Warehouse
Management solution is designed to fulfill these requirements. Even here, the integration is
done towards basic transportation management via the LE delivery. The delivery in this case
is also replicated to the EWM solution and the warehouse tasks will be executed there
according to the setup in EWM. EWM will update the LE delivery and therefore the freight unit
in transportation management is also updated with the relevant information from the WMS
system.

140

© Copyright. All rights reserved.


Lesson: Exploring Warehouse Integrations

## Figure 97: Extended Warehouse Management

From SAP S/4HANA 2020, the advanced shipping and receiving functionality has been made
available in order to integrate the shipping and receiving process directly into the
transportation management document (freight order). The advanced shipping and receiving
functions support both, EWM and IM integration. They can be used within the (basic)
transportation management scope as long as no other criteria for advanced transportation
management are met (for example, EWM and TM running side-by-side).

Figure 98: Advanced Shipping & Receiving

## Advanced TM - EWM Integration

Note that there is also an advanced integration between EWM and TM that requires the
advanced transportation management license. In the process described above, the
integration from ECC/TM to EWM is done only via the delivery, the so-called delivery-based

© Copyright. All rights reserved.

141


## Unit 6: Transportation Execution

integration. There is also the possibility to use much more planning capabilities by creating
deliveries already on a plan made based on sales orders in TM and hand over a load plan from
TM to the WMS System for execution. Therefore, in EWM the transportation unit is needed.
The transportation unit in this scenario is created based on the freight order in TM that is
created during TM planning.

Hint:
For additional information about TM - EWM Integration requiring the advanced
transportation management license, please refer to SAP Notes 1984252 and
2269324.

Figure 99: Advanced TM - EWM Integration

## Stockroom Management

For small to medium warehouse setups, there is a third option available called SAP
Stockroom Management. Stockroom Management is integrated directly to the LE delivery
and the warehouse transportation orders are triggered as a subsequent task to the LE
predecessor documents.

Stockroom management is a specific offering for installed base customers to continue
running their light warehouse management implementation in the context of SAP S/4HANA.
Its license is included in SAP S/4HANA Enterprise Management component.

The main reason for creating the offering named Stockroom Management is to give existing
customers of LE-WM an opportunity to keep these warehouses untouched that do not benefit
immediately from moving to embedded EWM.

Stockroom management is basically the ECC warehouse management component (LE-WM)
without capabilities supporting more complex warehouses. Relevant for small warehouses
with manual operations (that is, storage bin management).

142

© Copyright. All rights reserved.


Lesson: Exploring Warehouse Integrations

Figure 100: Stockroom Management

## Stock Room Management Exclusion List

Functionalities of LE-WM that are not part of stock room management are:

● Task & Resource Management (WM-TRM)

● Warehouse Control Unit interface (WM-LSR)

● Value Added Service (WM-VAS)

● Yard Management (WM-YM)

● Cross-Docking (WM-CD)

● Wave Management (WM-TFM-CP)

● Decentral WM (WM-DWM)

There are no innovations planned in this area and EWM remains the strategic product.

Hint:
For additional information, please also refer to the SAP Note 257742.

## Warehouse Integration

Within SAP S/4HANA there are two offerings of warehouse management options and both
can be integrated into basic and advanced transportation management.

1. Customers innovating their warehouse processes follow SAP´s strategic direction and will

convert/implement embedded EWM with the option to run basic and/or advanced
transportation management scope (which has license implications) .

© Copyright. All rights reserved.

143


## Unit 6: Transportation Execution

2. Customers with no desire to manage or even optimize complex warehouse processes, and
who want to keep their established offering, can technically stay on LE-WM and use the
stockroom management functionality with certain restrictions.

Both options can also co-exist within one deployment and customers looking for a
decentralized approach can use SAP S/4HANA EWM standalone for some or all of their
warehouses.

Figure 101: Warehouse Integrations

Pick, Load, and Post Goods Issue

## Simulation: Pick, Load, and Post Goods Issue

For more information on Pick, Load, and Post Goods Issue, please view the
simulation in the lesson Exploring Warehouse Integrations in your online course.

144

© Copyright. All rights reserved.


Unit 6
Exercise 8

Pick, Load, and Post Goods Issue

## Business Example

As a consultant responsible for the configuration of a basic shipping scenario in SAP
S/4HANA, you need to show your customer how to pick the deliveries for your freight order
and post goods issue on delivery level.

Note:
In this exercise, when you see ##, replace the characters with the two-digit
number (01 to 30) assigned to you by your instructor.

1. What is the picking status of your deliveries? What is the overall status of your delivery?

What is the overall packing status of your deliveries?

Delivery to TMBS##-01

Picking Status

Packing Status

Overall Status

Delivery to TMBS##-02

Picking Status

Packing Status

Overall Status

Delivery to TMBS##-03

Picking Status

Packing Status

## Overall Status

2. Pick the delivery amount for all your deliveries. Use Storage Location 0001.

© Copyright. All rights reserved.

145


Unit 6: Transportation Execution

What is the status of your deliveries?

3. Post goods issue on your deliveries. What is the status of the deliveries?

Delivery to TMBS##-01

Picking Status

Packing Status

Goods movement status

Delivery to TMBS##-02

Picking Status

Packing Status

Goods movement status

Delivery to TMBS##-03

Picking Status

Packing Status

## Goods movement status

4. After the truck is loaded and the loading report is received from the warehouse staff, set
the status in the freight order. What is the life cycle status of the freight order? What are
the execution and logistical execution statuses of the freight order?

Lifecycle Status

## Execution Status

## Logistical Execution Status

5. Report the departure of the truck and verify the statuses in the freight order. What is the
life cycle status of the freight order? What are the execution and logistical execution
status of the freight order?

Lifecycle Status

## Execution Status

Logistical Execution Status

146

© Copyright. All rights reserved.


Unit 6
Solution 8

Pick, Load, and Post Goods Issue

## Business Example

As a consultant responsible for the configuration of a basic shipping scenario in SAP
S/4HANA, you need to show your customer how to pick the deliveries for your freight order
and post goods issue on delivery level.

Note:
In this exercise, when you see ##, replace the characters with the two-digit
number (01 to 30) assigned to you by your instructor.

1. What is the picking status of your deliveries? What is the overall status of your delivery?

What is the overall packing status of your deliveries?

Delivery to TMBS##-01

Picking Status

Packing Status

Overall Status

Delivery to TMBS##-02

Picking Status

Packing Status

Overall Status

Delivery to TMBS##-03

Picking Status

Packing Status

## Overall Status

a) In the SAP Fiori launchpad, go to Shipping and Warehouse Management → Manage

Outbound Deliveries.

b) For Ship-To-Party, enter TMBS##* .

c) Set Overall Status to All.

© Copyright. All rights reserved.

147


Unit 6: Transportation Execution

d) Choose Go.

e) Choose the delivery and choose >.

f) Verify the Overall Status on the delivery header.

g) Navigate to the General Information tab and verify the Picking Status and Overall

Packaging Status.

h) Repeat the previous steps for the remaining deliveries.

Delivery to TMBS##-01

Picking Status

Packing Status

Overall Status

Delivery to TMBS##-02

Picking Status

Packing Status

Overall Status

Delivery to TMBS##-03

Picking Status

Packing Status

Overall Status

Not Yet Picked (A)

Packing not required

## Open

Not Yet Picked (A)

Completely Packed (C)

## In Process

Not Yet Picked (A)

Packing not required

## Open

2. Pick the delivery amount for all your deliveries. Use Storage Location 0001.

a) In the SAP Fiori launchpad, go to Shipping and Warehouse Management →  Pick

Outbound Delivery.

Note that you can get to the same application using the SAP Fiori app from the last
exercise by choosing the Pick button in the overview list.

b) On the Delivery Items tab, choose your item and choose >” on the right side of the

table.

c) Enter the delivery quantity as picking quantity.

d) Enter Storage Location 0001.

e) Choose Apply.

f) Choose Save.

148

© Copyright. All rights reserved.


Lesson: Exploring Warehouse Integrations

What is the status of your deliveries?

The status is Ready to Post GI.

3. Post goods issue on your deliveries. What is the status of the deliveries?

Delivery to TMBS##-01

Picking Status

Packing Status

Goods movement status

Delivery to TMBS##-02

Picking Status

Packing Status

Goods movement status

Delivery to TMBS##-03

Picking Status

Packing Status

## Goods movement status

a) In the SAP Fiori launchpad, go to Shipping and Warehouse Management → Manage

Outbound Deliveries.

b) For Ship-To-Party, enter TMBS##* .

c) Set filter value for Overall Status to Ready to Post GI.

d) Choose Go.

e) Choose all your deliveries delivery and choose Post GI.

f) In the dialog box, enter today as Goods Issue date and choose Post GI.

g) Set filter value for Overall Status to All.

h) Choose Go.

i) Choose the delivery and choose >.

j) Verify the Overall Status on the delivery header.

Delivery to TMBS##-01

Picking Status

Packing Status

Fully Picked (C)

## Packing not required

© Copyright. All rights reserved.

149


Unit 6: Transportation Execution

Goods movement status

## Completed

Delivery to TMBS##-02

Picking Status

Packing Status

Fully Picked (C)

Completely Packed (C)

Goods movement status

## Completed

Delivery to TMBS##-03

Picking Status

Packing Status

Fully Picked (C)

Packing not required

Goods movement status

## Completed

4. After the truck is loaded and the loading report is received from the warehouse staff, set
the status in the freight order. What is the life cycle status of the freight order? What are
the execution and logistical execution statuses of the freight order?

Lifecycle Status

## Execution Status

## Logistical Execution Status

a) In the SAP Fiori launchpad, select Freight Orders (Worklist).

b) On the Freight Orders Workslist screen, choose the All Road Freight Orders query.

c) Open the freight order by clicking the document link.

d) Choose Edit.

e) Select Execution Status and choose Set to Loaded.

f) Save the freight order.

g) Go to Status tab and verify the statuses.

Lifecycle Status

Execution Status

## In Process

Ready for transportation execution

Logistical Execution Status

## SP_1010 Loaded with timestamp

5. Report the departure of the truck and verify the statuses in the freight order. What is the
life cycle status of the freight order? What are the execution and logistical execution
status of the freight order?

Lifecycle Status

Execution Status

150

© Copyright. All rights reserved.


Lesson: Exploring Warehouse Integrations

## Logistical Execution Status

a) In the SAP Fiori launchpad, select Freight Orders (Worklist).

b) On the Freight Orders Workslist screen, choose the All Road Freight Orders query.

c) Open the freight order by clicking the document link.

d) Choose Edit.

e) Select Execution Status and choose Set to Departed.

f) Save the freight order.

g) Go to Status tab and verify the statuses.

Lifecycle Status

Execution Status

In Process

## In execution

Logistical Execution Status

SP_1010 Departed with timestamp

© Copyright. All rights reserved.

151


Unit 6: Transportation Execution

## LESSON SUMMARY
You should now be able to:

● Pick and load the demands on the delivery

● Post goods issue for the deliveries

152

© Copyright. All rights reserved.


Unit 6

## Learning Assessment

1. Before and during execution, the Freight Order Management component allows you to

create documents related to the cargo movement and its compliance to document actual
quantities and details of the cargo.

Determine whether this statement is true or false.

X True

## X False

2. PPF used in the output management is comparable to the SAP Workflow.

Determine whether this statement is true or false.

X True

## X False

3. Which of the following are conditions that can be used in PPF Output Management?

Choose the correct answers.

X A Scheduling Condition

X B Spool Condition

X C Starting Condition

## X D Update Condition

4. Which of the following predecessor documents can be used for an integration in (basic)

transportation management and can trigger a Freight Unit creation?

Choose the correct answers.

X A Sales Order

X B Inbound Delivery

X C Stock Transfer Order

## X D Outbound Delivery

© Copyright. All rights reserved.

153


## Unit 6: Learning Assessment

5. Which of the following business documents can be used for to trigger output

management?

Choose the correct answers.

X A Freight Units

X B Transportation Units

X C Freight Orders

## X D Forwarding Orders

6. The customer wants to model a warehouse process and integrate it into (basic)

transportation management. Which of the following SAP Solutions can be used with
respect to the compatibility scope?

Choose the correct answers.

X A Basic Warehousing (EWM)

X B Warehouse Management (LE-WM)

X C Advance Warehousing (EWM)

X D Stockroom Management

154

© Copyright. All rights reserved.


UNIT 7 Settle Transportation Charges
and Distribute Costs

Lesson 1

Describing Charge Calculation Master Data

Lesson 2

Calculating Transportation Charges

Exercise 9: Calculate Transportation Charges

Lesson 3

Settling Transportation Charges with Carriers

Lesson 4

## Distributing Transportation Costs

Exercise 10: Settle Transportation Charges with a Carrier

Exercise 11: Verify a Freight Invoice

157

168

173

181

188

193

199

## UNIT OBJECTIVES

● Describe a freight agreement in transportation charge management

● Display the elements of a charge calculation sheet

● Describe rate tables in charge management

● Display a scale

● Calculate transportation charges

● Generate a freight settlement document

● Post freight charges to MM

● Verify freight invoices

● Distribute freight costs

© Copyright. All rights reserved.

155


Unit 7: Settle Transportation Charges and Distribute Costs

156

© Copyright. All rights reserved.


Unit 7
Lesson 1

Describing Charge Calculation Master Data

## LESSON OBJECTIVES
After completing this lesson, you will be able to:

● Describe a freight agreement in transportation charge management

● Display the elements of a charge calculation sheet

● Describe rate tables in charge management

● Display a scale

## Charge Calculation Master Data
In this lesson, we will look at the master data (agreements, calculation sheets, rate tables, and
scales) that governs how transportation charges are calculated for suppliers. This is an
integral step and must occur before the process of charge calculation and settlement is
triggered.

Figure 103: Integration Of Charge Management

© Copyright. All rights reserved.

157


Unit 7: Settle Transportation Charges and Distribute Costs

## Animation: Integration Of Charge Management

For more information on Integration Of Charge Management, please view the
animation in the lesson Describing Charge Calculation Master Data in your online
course.

When shipping products to customers via a third party, an organization needs to account for
and recognize the costs involved in moving goods. TM provides a broad and flexible
calculation process. With the integration into MM, integration to the Financial Accounting (FI)
and Controlling (CO) applications allows an organization to perform payment and execute
billing transactions, as well as trigger the settlement process to accrue the proper
transportation charges to financial accounts.

Transportation Charge Management Master Data

## Figure 105: Transportation Charge Management Master Data

Freight agreements (FAs) are the basis for calculating transportation charges. You require
FAs to calculate transportation charges billable to you by your carrier.

## Freight Agreements Contractual Data

An agreement includes contractual data, such as the following:

● Organizational unit (purchasing organization)

●

Involved business partners (carrier)

● Terms of payment

● Validity dates

## Freight Agreement
The system determines the agreement based on organization, business partner, and validity
period. A freight agreement is most commonly determined by the purchasing organization
and business partner (carrier). In the Freight Agreement Type Customizing activity, you can

158

© Copyright. All rights reserved.


## Lesson: Describing Charge Calculation Master Data

configure whether one or multiple parties can be entered in the agreement. That is, if you
have one freight agreement with a carrier valid for multiple purchasing organizations.

## Figure 106: Freight Agreement Overview

Freight agreements represent a long-term contract between a shipper and a carrier. Each
freight agreement can point to one or more calculation sheets (CS).

## Charge Calculation Sheet
Depending on how a shipment will be transported, various charges may be incurred for
different means of transport. In TM, companies can create calculation sheets that reflect all
possible charge elements for a given carrier. These charges essentially mimic the terms of the
freight contract.

The calculation sheet (CS) is a hierarchical table used to calculate transportation charges.
The calculation sheet combines the charge types permitted for a document and the sequence
in which the system takes these charge types into account during the calculation. The system
uses the calculation sheet to specify which transportation charges to calculate and how to
calculate them. This helps to pay suppliers or carriers for subcontracted transportation
services. The calculation sheet points to charge items and each charge item can result in a
calculated amount.

© Copyright. All rights reserved.

159


Unit 7: Settle Transportation Charges and Distribute Costs

## Figure 107: Calculation Sheet Overview

The calculation sheet includes transportation charge elements, subtotals, and totals.
Calculation sheet maintenance is a step in the process of setting up master data in Charge
Management, and is integrated with agreements, rate tables, and scales. You can use a
template to create a calculation sheet and calculation sheet line items.

## Calculation Sheet Items

The calculation sheet can consist of the following items:

● Charge Type

● Rate

● Dimensional Weight Profile

● Calculation Resolution Base (for example, root, container, product, and stage)

● Calculation Method (for example, standard or breakweight)

In more detail, the items above refer to the following:

Rate:

Rates contain details of the rate table for each standard charge item. It is also possible to
enter fixed rates or percentages of other lines in the calculation sheet.

Dimensional Weight Profile:

The dimensional weight profile the system uses to calculate the transportation charges
for the line item. The system uses the dimensional weight factor in the dimensional
weight profile to convert a product's gross volume into dimensional weight. The system
then uses the dimensional weight to apply the correct rate. Note that a dimensional

160

© Copyright. All rights reserved.


## Lesson: Describing Charge Calculation Master Data

weight profile at the line item level of a calculation sheet has priority over a dimensional
weight profile in an agreement.

Calculation Resolution Base:

During charge calculation, the system determines the calculation resolution base by the
origin of the data upon which the charge aspect is based. You can define the charge
aspect in the resolution base objects, for example, container, product, and stage.

● Root: This is the header of the document such as freight order, or freight booking.

● Stage: To utilize stage attributes such as distance between the shipper location and

the port of loading.

● Container: When gross weight of the container will be used for the calculation.

● Product: When product attributes like product quantity, weight or volume need to be

used.

For example, you want to determine the freight rate based upon the gross weight of the
order. To do this, you will need to use the calculation resolution base of root. If, however,
you want to calculate the freight on a per package basis, the calculation resolution base
should be package.

Calculation Method:

The calculation method defines how the rates determined from the rate table are to be
interpreted. The break weight calculation method compares and selects the lower rate
from either the actual scale item or the lower end of the next scale item. With clipping, the
system works through the pricing scale level by level. The calculation results from each
scale level are then added up to produce the overall result.

## Charge Type

A charge type is the classification of a charge line that plays an important role in how the
system calculates the transportation charges for the charge line, for example, a base rate,
surcharge, or discount.

A charge type can result in a positive or negative value for a charge line. You can also specify
whether a charge type can be an amount or a percentage value.

## Animation: Charge Types

For more information on Charge Types, please view the animation in the lesson
Describing Charge Calculation Master Data in your online course.

© Copyright. All rights reserved.

161


Unit 7: Settle Transportation Charges and Distribute Costs

## Figure 109: Charge Types

Charge types can be grouped into charge categories. A useful code list is the UN/EDIFACT
codelist 5237. You can use the charge subcategories of charge types to group and categorize
charge types in a more granular way than charge categories. A suitable example is the code
list resulting from UN/EDIFACT Recommendation 23: "FREIGHT COST CODE # FCC
Harmonization of the Description of Freight Costs and Other Charges". All three entities
(charge type, charge category and charge subcategory) are freely definable in Customizing.

You define charge categories for charge types in the following Customizing activity:
Transportation Management  → Basic Functions  → Charge Calculation → Basic
Settings → Define Charge Categories.

You define charge subcategories for charge types in the following Customizing activity:

Transportation Management  → Basic Functions  → Charge Calculation → Basic
Settings → Define Charge Subcategories.

Charge categories and subcategories can be assigned in the charge type Customizing
activity, and can be used to determine the service material during settlement.

In the Define Charge Types Customizing activity, you define charge types that you can assign
to calculation sheets and rate tables. Once assigned to a calculation sheet line item or a rate
table, a charge type plays an important role in how the system calculates the transportation
charges for that line.

You can define the charge types in the following Customizing activity: Transportation
Management  → Basic Functions  → Charge Calculation → Basic Settings →  Define Charge
Types.

When defining charge types, you can use the following settings:

● Specify whether a charge type can result in a positive or negative value.

● Specify whether a charge type can be an absolute value or a percentage value.

● Specify whether you want to set the charge type as an absolute value or a percentage

value each time you assign the charge type.

● Assign a charge type to a charge category and charge subcategory.

162

© Copyright. All rights reserved.


Lesson: Describing Charge Calculation Master Data

●

Indicate if the charge is a tax.

● Specify if and how the system rounds a value.

● Assign a default calculation base to the charge type so you do not need to assign a

calculation base each time you create a calculation sheet line item.

## Rate Table

A rate is a price for a certain transportation service that applies only during its validity period.
In TM, rates are listed in a rate table.

Figure 110: Rate Table Overview

## Rate Table Elements

You can define the following elements in the rate table:

● Charge Usage

● Charge Type

● Dimensions

● Calculation Base (for each scale)

● Relevance for Calculation Method

Additional information on elements you can define in the rate table is as follows:

● Charge Usage: You can define the charge usage as relevant for paying your carrier.

● Charge Type: The system only assigns rate tables to a charge item in a calculation sheet if

the charge types match. You can use this field to search for a rate table.

● Dimensions: You add each dimension on which you want your rate to be defined and

looked up. For example, if you want the rate to be defined based on destination location
and weight, add a dimension for destination location and for weight. The number of
dimensions that you can use in one rate table is restricted to three for the (basic)
transportation management scope.

© Copyright. All rights reserved.

163


## Unit 7: Settle Transportation Charges and Distribute Costs

● Calculation Base: You can define the calculation base for the scale. The calculation base is

the actual base or the factor on which the rate retrieval is performed.

● Rel. Calc. Method (Relevant for Calculation Method): If you select this checkbox, you

define whether you want the system to apply a special calculation method, such as break
weight or clipping, to the rate table on the level of a charge item.

Rate tables also contain the freight rates for transportation services and allow you to maintain
rates for certain validity periods. Within (basic) transportation management the number of
dimensions of a rate table is restricted to three (3). The rates are reusable and can be referred
to in multiple calculation sheets. The rates can be imported or exported using Microsoft Excel.

Example of Rates include the following:

● Weight / volume rates

● Volumetric rate calculation (bulkiness factors)

● Distance rates

● Freight of all kind and commodity rates

● Various origin and destination point classifications such as point-to-point, point-to-zip,

point-to-state, zip-to-zip, and state-to-state

● Rates based on equipment (container type or size) or packaging class

● Handling charges: loading and unloading, document handling, security surcharge, and so

on

You can maintain a large rate table, with or without scale items, using Microsoft Excel. You
can enter the rates and scales into a Microsoft Excel file and upload the file to your TM
system.

Alternatively, you can define an empty reference rate table with validity periods in TM and
download it to Microsoft Excel. You can then maintain the rate table in the Microsoft Excel file
and upload it afterwards to your TM system.

Other than using Excel integration, you can also use the Update Rates function in the rate
table maintenance to update rates (for example, increase or decrease by a fixed amount or
percentage value).

## Scales

If a rate is a price for a certain transportation service that applies only during its validity
period, a scale represents a dimension of the rate. In effect, a scale is used to define a
parameter that then defines a rate. For example, if a rate depends upon distance and weight,
you must define a separate scale for distance and for weight. The distance and weight scales
are then used to define the rate.

164

© Copyright. All rights reserved.


Lesson: Describing Charge Calculation Master Data

## Figure 111: Scale Overview

Scale maintenance is a prerequisite for the maintenance of rates, as scales are the
dimensions of rate tables. You maintain scales independently of the agreement and the rates,
and can reuse them in multiple rate tables. A scale has a scale base, which is essentially a
database field tied to an attribute of the freight order. The scale base defines how the system
interprets the scale. For example, a rate based on distance has to have the distance
maintained.

Possible Scale Bases include:

● Product quantity

● Package type

● Weight

● Volume

● Means of transport

● Location

● Distance

● Business partner

Each scale is based on a scale type. The scale type controls how the scale levels are defined. It
indicates whether the scale values that were specified represent the upper or lower
boundaries for the scale levels.

Depending upon the scale base, a scale unit of measure can be defined. This is a mandatory
field if the unit of measure is relevant for the scale base. Weight, for example, requires a unit
of measure.

© Copyright. All rights reserved.

165


Unit 7: Settle Transportation Charges and Distribute Costs

In relation to calculation type, you can choose between absolute and relative. For non-
numeric scales, you can only choose absolute. The system uses the calculation type on scale
level as the proposed value for rate table maintenance.

You can also assign rounding profiles. Before the system accesses the scale to look up a rate
in a rate table, it rounds the input value based on the rounding profile to determine the right
scale level.

## Calculation Base

A calculation base identifies the actual base or factor with which the system calculates the
charges for the scale.

## Figure 112: Calculation Base

There can be various scenarios in which the system must calculate a charge for different
forms of weights, for example, gross weight and net weight.

In this case, both gross weight and net weight correspond to the scale base Weight (W),
whose dimension is mass. However, by definition, gross weight and net weight are two
entirely different charge aspects. Therefore, they have two different calculation bases, such
as "W1" for gross weight and "W2" for net weight.

To follow the scenario given here, you define a calculation base for every scale base. This
calculation base is the final element in the charge determination. This means that the
calculation base is used to determine the charges.

## Animation: Calculation Base

For more information on Calculation Base, please view the animation in the
lesson Describing Charge Calculation Master Data in your online course.

In the figure, Calculation Base, the charges are dependent on weight and the destination
location. The scale has the scale base Location. This scale base defines that the scale uses
locations only. The scale base can be used for both the source and destination location. The

166

© Copyright. All rights reserved.


## Lesson: Describing Charge Calculation Master Data

calculation base DESTLOC determines that the destination location of the freight order is
used. Technically, in the customizing of the calculation base, you define which field is to be
used and which program or class the system will call to determine the field value.

If the resolution base in the calculation sheet points to the freight order stage, the system will
derive the values from the specific stage and use it in the calculation.

## LESSON SUMMARY
You should now be able to:

● Describe a freight agreement in transportation charge management

● Display the elements of a charge calculation sheet

● Describe rate tables in charge management

● Display a scale

© Copyright. All rights reserved.

167


Unit 7
Lesson 2

Calculating Transportation Charges

## LESSON OBJECTIVES
After completing this lesson, you will be able to:

● Calculate transportation charges

## Agreement Determination
Freight Agreements (FAs) are the basis for calculating transportation charges. In this section,
we look at how agreements are determined.

The system determines the agreement based on organization, business partner, and validity
period.

If there are several matching agreements, which can be determined on the data from freight
order/booking, it is possible to have a leading charge type (defined in charge type
Customizing), and the first agreement where the defined leading charge type can be
calculated is picked. Besides using leading charge types, it is possible to maintain priorities.

If the system finds multiple matching agreements during agreement determination, the
agreement priority defines the sequence in which the subsequent determination is executed.

The agreement priority can be maintained on the General Data tab in the details section

## Charge Calculation Customizing and Assignment
The calculation profile provides a central location to define the settings that you want the
system to use when calculating transportation charges.

The following are examples of settings you can define in a calculation profile:

● Specify the date type that the system uses as the basis for the rate, exchange rate, and

agreement validity, and ultimately the charge calculation. For example, the order date, the
invoice date, or the expected end date of the main carriage.

● Specify the level at which the system calculates the charges, for example, at header level

or stage level.

● Specify the default dimensional weight profile for the organizational unit and the condition

that the system uses to determine the dimensional weight profile.

In the Define Calculation Profile Customizing activity, you define the settings that you want the
system to use when calculating transportation charges. You find it in Customizing at
Transportation Management → Basic Functions → Charge Calculation → Basic Settings for
Charge Calculation → Define Calculation Profiles.

## Charges Profile

You can enable charge calculation for a purchasing organization by assigning a charges
profile to the purchasing organization (see the PPOCE transaction). The charges profile

168

© Copyright. All rights reserved.


## Lesson: Calculating Transportation Charges

groups together the general settings for charge calculation, such as the calculation profile you
want the system to use when calculating transportation charges.

## Figure 114: Charge Calculation Customizing

In the Customizing activity Define Freight Order Types, the following settings influence charge
calculation:

● Enable Charge Calculation: This must be selected to enable the system to calculate the
charges. This setting does not influence manual freight charges, as they can be entered
even when this setting is not selected.

● Save Strategy: Calculate Charge After Each Save: When this save strategy is selected, the
system performs charge calculation after each save. If a mandatory charge type cannot be
determined or is missing, the freight order cannot be saved.

To define freight order types, in Customizing, choose Transportation Management → Freight
Order Management → Freight Orders → Define Freight Order Type.

© Copyright. All rights reserved.

169


Unit 7: Settle Transportation Charges and Distribute Costs

Freight Order Charge Calculation

Figure 115: Charge Calculation

## Animation: Charge Calculation

For more information on Charge Calculation, please view the animation in the
lesson Calculating Transportation Charges in your online course.

During freight charge calculation in the freight order, the following steps occur:

1. Collect the data from the following objects:

● Transaction business object: freight order, freight booking

● Configuration objects

● Charge Calculation Rules (BRF+ conditions)

● Relevant master data

● Any BAdI implementation

2. Determine the freight agreement.

3. Calculate the values of each charge type in the calculation sheet.

4. Show the calculated results in the freight order.

170

© Copyright. All rights reserved.


Lesson: Calculating Transportation Charges

## Example Calculation

Figure 117: Example Calculation

## Animation: Example Calculation

For more information on Example Calculation, please view the animation in the
lesson Calculating Transportation Charges in your online course.

The example demonstrates how the system calculates the charge for a container ocean
freight booking from Newark to Rotterdam based on master data.

Calculate Transportation Charges

## Simulation: Calculate Transportation Charges

For more information on Calculate Transportation Charges, please view the
simulation in the lesson Calculating Transportation Charges in your online
course.

© Copyright. All rights reserved.

171


Unit 7: Settle Transportation Charges and Distribute Costs

172

© Copyright. All rights reserved.


Unit 7
Exercise 9

Calculate Transportation Charges

## Business Example

You need to show your colleague how to create charge management master data. For this
purpose, you need to create a rate table and freight agreement. Subsequently, you need to
show this master data in action by using it to calculate the freight cost in a freight order.

Note:
In this exercise, when you see ##, replace the characters with the two-digit
number (01 to 30) assigned to you by your instructor.

1. Create a rate table HANDLING_RATE_##, based on rate table type 1000. The rate table

should be used for settling charges with service providers and valid for charge type HNDL.
The rate table should have one scale based on calculation base QUANTITY_VAL. It should
be a Same-Scale with Unit of Measure PC. There shall be one validity period from
beginning of this year to end of next year. The prices for handling cargo should be as
follows:

Quantity

1

2

3

4

5

40

30

25

20

18

EUR per PC

EUR per PC

EUR per PC

EUR per PC

EUR per PC

Note:
Don’t forget to release the validity period of your rate table.

2. Copy freight agreement S4611_FA_TM-CAR-99 to a new freight agreement FA_BS_##. In

the new freight agreement, replace carrier TM-CAR-99 with carrier CAR_TM3_##.
Release and save your freight agreement.

3. Calculate the charges in your freight order.

© Copyright. All rights reserved.

173


Unit 7: Settle Transportation Charges and Distribute Costs

What is the total amount?

4. What is the amount of the base charge? How is it calculated?

5. What is amount of the fuel surcharge? How is it calculated?

6. What is amount of the handling charges? How are they calculated?

7. Which freight agreement and rate table has been used to calculate the handling charges?

Freight Agreement

Rate Table

174

© Copyright. All rights reserved.


Unit 7
Solution 9

Calculate Transportation Charges

## Business Example

You need to show your colleague how to create charge management master data. For this
purpose, you need to create a rate table and freight agreement. Subsequently, you need to
show this master data in action by using it to calculate the freight cost in a freight order.

Note:
In this exercise, when you see ##, replace the characters with the two-digit
number (01 to 30) assigned to you by your instructor.

1. Create a rate table HANDLING_RATE_##, based on rate table type 1000. The rate table

should be used for settling charges with service providers and valid for charge type HNDL.
The rate table should have one scale based on calculation base QUANTITY_VAL. It should
be a Same-Scale with Unit of Measure PC. There shall be one validity period from
beginning of this year to end of next year. The prices for handling cargo should be as
follows:

Quantity

1

2

3

4

5

40

30

25

20

18

EUR per PC

EUR per PC

EUR per PC

EUR per PC

EUR per PC

Note:
Don’t forget to release the validity period of your rate table.

a) In the SAP Fiori launchpad, go to Charge Management → Create Rate Table Definition.

b) Enter Rate Table Type: 1000.

c) Choose Continue.

d) On the General Data tab maintain the following entries:

## Rate Table

## HANDLING_RATE_##

© Copyright. All rights reserved.

175


Unit 7: Settle Transportation Charges and Distribute Costs

Description

Charge Usage

Charge Type

## Value Type

Rate Table for Handling Charges ##

Service Provider

## HNDL

## Absolute Value

e) Choose Insert Scale.

f) In the table, enter the following values:

Calculation Base

Scale Type

QUANTITY_VAL

## Same Scale

Scale Unit of Measure

PC

g) On the Dates and Values tab, enter a new validity period by choosing Insert – with scale

items.

h) Enter the following values:

Valid from

Valid to

## Currency

i) In the rate table enter the following values:

Quantity

1

2

3

4

5

Beginning of this year

End of next year

EUR

Rate

40

30

25

20

18

j) On the Calculation Rules tab, enter the following values:

Calculation base

Price Unit

## Price Unit UoM

k) Save the rate table.

QUANTITY_VAL

1

PC

l) On the Dates and Values tab, select the row with your validity period and choose Set

Status → Released.

176

© Copyright. All rights reserved.


Lesson: Calculating Transportation Charges

m) Save the rate table.

2. Copy freight agreement S4611_FA_TM-CAR-99 to a new freight agreement FA_BS_##. In

the new freight agreement, replace carrier TM-CAR-99 with carrier CAR_TM3_##.
Release and save your freight agreement.

a) In the SAP Fiori launchpad, go to Contract Management → Freight Agreement

(Worklist).

b) Select the row with freight agreement S4611_FA_TM-CAR-99.

c) Choose Copy.

d) Enter the name of the freight agreement FA_BS_## and a description.

e) In the Carrier field, enter CAR_TM3_##.

f) Choose Set Status → Released.

g) Choose Save.

3. Calculate the charges in your freight order.

a) In the SAP Fiori launchpad, go to Order Management →  Edit Road Freight Order.

b) Enter the Freight Order Number (this varies).

c) Choose Continue.

d) Navigate to the Charges tab.

e) Choose Charges/Settlement → Calculate Charges.

f) Press Save.

g) Check the total amount.

What is the total amount?

The total amount 1,285.68 EUR.

4. What is the amount of the base charge? How is it calculated?

On  the  Charges  tab  of  the  freight  order,  expand  the  charge  hierarchy  and  check  the  line
Basic  Freight  Charge.  The  price  is  2.4  EUR  per  10  kg  and  the  net  weight  is  4,132  kg.
Therefore, the total amount is 4,132 / 10 * 2,4 = 991.68 EUR.

5. What is amount of the fuel surcharge? How is it calculated?

On the Charges tab of the freight order, check the line Fuel Surcharge. The price is 12 % of
the basic charge (line 10). Therefore, the total amount is 991.68 EUR * 12 % = 119 EUR.

6. What is amount of the handling charges? How are they calculated?

On the Charges tab of the freight order, check the lines Handling Charge. There are three
lines.

© Copyright. All rights reserved.

177


Unit 7: Settle Transportation Charges and Distribute Costs

a) For the line with 1 PC, the price is 40 EUR.

b) For the line with 2 PCs, the price is 2 * 30 EUR = 60 EUR.

c) For the line with 3 PCs, the price is 3 * 25 EUR = 75 EUR.

d) The total handling charge is 40 + 60 + 75 = 175 EUR.

7. Which freight agreement and rate table has been used to calculate the handling charges?

Freight Agreement

## Rate Table

a) Select one of the lines for the handling charges and choose the Show/Hide Details

button.

Make sure, that only one line is selected. You may need to de-select the total line.

b) On the Charges tab of the freight order, check the lines Handling Charge.

Freight Agreement

FA_BS_##

## Rate Table

HANDLING_RATE_##

178

© Copyright. All rights reserved.


Lesson: Calculating Transportation Charges

## LESSON SUMMARY
You should now be able to:

● Calculate transportation charges

© Copyright. All rights reserved.

179


Unit 7: Settle Transportation Charges and Distribute Costs

180

© Copyright. All rights reserved.


Unit 7
Lesson 3

Settling Transportation Charges with Carriers

## LESSON OBJECTIVES
After completing this lesson, you will be able to:

● Generate a freight settlement document

● Post freight charges to MM

● Verify freight invoices

## Freight Settlement Processing
After services have been rendered for the freight order, the settlement process must be
initiated. In this lesson you will examine the steps TM performs to assist in the process of
settling transportation costs with your carriers.

What is Freight Settlement?

When an organization ships via a third party to a customer, costs may be incurred that have
to be charged. After services have been rendered, the following activities should take place:

● Accruals are posted

●

Invoices are verified

● Vendors are paid

To manage this process properly in an integrated environment, a freight settlement
document is created and posted to MM.

Figure 120: Freight Settlement Processing

© Copyright. All rights reserved.

181


Unit 7: Settle Transportation Charges and Distribute Costs

Freight charges are settled with the carrier (supplier).

Settlement includes the following:

● Assigning and transferring shipment costs to Financial Accounting to generate accruals,

and assigning costs to a CO object.

● Settlement of costs with the carrier: posting payables by canceling the accruals.

You need to have entered and accepted the services provided before you can transfer costs
to Financial Accounting. The system automatically creates the service entry sheet based on a
purchase order for external services.

Before you can settle costs with the carrier, you need to create an invoice using manual
invoice verification or create a credit memo using the credit memo procedure.

## Freight Settlement Document
A freight settlement document (FSD) is a business document that is posted to MM to create a
purchase order and service entry sheet in order to verify an invoice received from a supplier
or carrier. When the invoice is received, it should be checked against the data from the freight
settlement document. If performing an evaluated receipt settlement, the automatically
generated invoice is based on the data from the freight settlement document.

The transportation charges are calculated in TM based on a freight order or freight booking.
The actual invoice verification takes place in MM. You can create an individual FSD for one
freight order, or freight booking. You can create a collective FSD for multiple freight orders or
freight bookings. You can also create multiple FSDs at the same time.

Figure 121: Freight Settlement Document Overview

182

© Copyright. All rights reserved.


Lesson: Settling Transportation Charges with Carriers

## Animation: Freight Settlement Document Overview

For more information on Freight Settlement Document Overview, please view the
animation in the lesson Settling Transportation Charges with Carriers in your
online course.

An FSD contains the following information:

● General data: Document type, the purchasing organization, payment terms, document

currency, and so on

● Business partner information: Invoicing party, payee, additional business partners, which

can be entered manually or automatically determined by the system

● Orders: The business documents or the business document items that are being settled

using the FSD

● Charges: For each FSD item the Charges tab page has the charges relevant for settlement

with the carrier

Freight Settlement Document Creation

Figure 123: Freight Settlement Document Creation

## Animation: Freight Settlement Document Creation

For more information on Freight Settlement Document Creation, please view the
animation in the lesson Settling Transportation Charges with Carriers in your
online course.

© Copyright. All rights reserved.

183


Unit 7: Settle Transportation Charges and Distribute Costs

The FSD can be created in the following ways:

● You can create an individual FSD for one freight order, or freight booking, or a collective
FSD for multiple freight orders, or freight bookings. To do this, access freight orders, or
freight bookings from the worklist, in the relevant document overview, or in the freight
settlement overview. The system automatically creates the FSD based on the data in the
freight orders, or freight bookings and calculates the transportation charges.

● You can create FSDs directly out of the freight booking or freight order apps.

● You can create partial FSDs for previously invoiced freight documents.

● You can create multiple freight settlement documents using the mass creation of FSD

report.

Figure 125: Freight Settlement Document Creation

## Animation: Freight Settlement Document Creation

For more information on Freight Settlement Document Creation, please view the
animation in the lesson Settling Transportation Charges with Carriers in your
online course.

When the FSD creation is triggered for a freight booking/freight order (FB/FO), the
corresponding document type is used to determine the FSD type used.

The purchasing organization specified in the FB/FO is used to determine the settlement
profile. All of this information is then used to create FSDs for the selected FO/FB.

184

© Copyright. All rights reserved.


Lesson: Settling Transportation Charges with Carriers

Supplier Freight Processing - Process Flow

Figure 127: Supplier Freight Processing - Process Flow

Animation: Supplier Freight Processing - Process Flow

For more information on Supplier Freight Processing - Process Flow, please view
the animation in the lesson Settling Transportation Charges with Carriers in your
online course.

As you can see in the figure, Supplier Freight Processing - Process Flow, the typical freight
settlement process flow is as follows:

Based on a delivery, the planner carries out several planning steps and creates a freight order
or a freight booking to subcontract to a carrier.

On settlement, the system creates a Freight Settlement Document (FSD). This document
contains all relevant logistical data as well as the charges and other commercial data. The
charges can be copied over from the freight order or freight booking (most common) or
another charge calculation is triggered based on the freight agreement between the
purchasing organization and the carrier. It is possible to manually change charges in the FSD.
FSDs can be created online or in batch. It is possible to do a collective settlement (several
freight orders or bookings are settled with one FSD). The FSD can then be posted to MM.

A purchase order and a service entry sheet are created in MM. This constitutes the working
list for invoice verification. You also have the option of self-billing.

© Copyright. All rights reserved.

185


Unit 7: Settle Transportation Charges and Distribute Costs

Note:
The purchase order and service entry sheet are only used for technical purposes
to post accruals. The service entry sheet comprises a list of services performed by
a vendor on the basis of a purchase order, containing service descriptions and
details of quantities and values. The descriptions of planned services deriving
from the purchase order are used as default descriptions in the service entry
sheet.

You can create a partial freight settlement document for a previously invoiced freight order.

The invoicing status of the freight order changes from Completely Invoiced to Partially
Invoiced before the additional freight settlement document is created. You can add charges to
an invoiced FO, but it is not possible to remove them. Invoice verification can be done with
reference to the freight order, carrier, bill-of-lading, air waybill, flight number, and voyage
number.

Purchase Order and Service Entry Sheet

Figure 129: Purchase Order and Service Entry Sheet

## Animation: Purchase Order and Service Entry Sheet

For more information on Purchase Order and Service Entry Sheet, please view
the animation in the lesson Settling Transportation Charges with Carriers in your
online course.

Each service entry sheet is based on an external service purchase order. Determining a valid
purchase order is required for transfers to Financial Accounting and for settlements.
Important criteria for the service purchase order include carrier, purchasing organization,
purchasing group, plant, and item category.

When the system has automatically determined a valid purchase order, a service entry sheet
is created that refers to the purchase order. During posting, you accept services and, in
Financial Accounting, an accounting document for generating accruals is created.

186

© Copyright. All rights reserved.


## Lesson: Settling Transportation Charges with Carriers

During account assignment, the system determines the correct G/L account in Financial
Accounting for each cost item and the assignment for Controlling. Account assignment can
be carried out at different levels, depending on the level of detail at which you want to track
costs.

The transfer to Financial Accounting to establish accruals requires entering and accepting the
services rendered. The system automatically creates a service entry sheet. Using the credit
memo procedure, also referred to as the Evaluated Receipt Settlement (ERS) procedure, you
can settle the freight costs with the carrier without having received invoices. You can choose
from different settlement periods. You transfer the calculated freight costs to Financial
Accounting. The invoices are verified by the carrier. If the carrier discovers variances, you can
post these as subsequent debits or credits.

If you receive invoices from the carrier, you can also verify the invoices manually and create
the invoices manually.

## Freight Settlement Document Changes
There can be late changes in the freight order requiring changes to logistical data which may
result in the change in the charges (increase or decrease). These changes can occur at time
when the old values are already transferred to settlement documents and / or the settlement
documents have also been transferred to financials.

Business example:

Accruals are posted as soon as the financial liability is known (example: departure or
confirmed pickup of the freight by the carrier). However, there can be mid-execution changes
(example: diversions (consignee changes), loss of cargo (in transit), unavailability of cargo,
unplanned costs due to detention, demurrages, loading and unloading activities, tolls, etc.)

These changes may only be known after execution or during the invoicing process (when
carrier sends the invoice).

The configuration of the FSD change process is done in the settlement profile.

When an order is changed and the invoicing status changes to Over Invoiced, the system
automatically applies the reverse and repost strategy.

## LESSON SUMMARY
You should now be able to:

● Generate a freight settlement document

● Post freight charges to MM

● Verify freight invoices

© Copyright. All rights reserved.

187


Unit 7
Lesson 4

Distributing Transportation Costs

## LESSON OBJECTIVES
After completing this lesson, you will be able to:

● Distribute freight costs

## Freight Costs
Freight costs incurred by the organization need to be allocated to individual cost or profit
centers so that profitability can be properly assessed. In this lesson, you will examine the
steps performed by the system in assisting the allocation of freight costs.

To compute true profitability for any manufacturing organization, all operational costs need to
be computed correctly. Most organizations would like the freight costs for material
procurement to be included in the material cost. Similarly, for customer deliveries, the freight
cost for the delivery needs to be considered for margin and profitability computation. TM can
distribute each of the charges used in the freight cost calculation to the item level of the
delivery. The item level cost then can be processed when the accrual is posted for the supplier
freight invoices.

Figure 131: Cost Distribution Concept

## Animation: Cost Distribution Concept

For more information on Cost Distribution Concept, please view the animation in
the lesson Distributing Transportation Costs in your online course.

188

© Copyright. All rights reserved.


## Lesson: Distributing Transportation Costs

The figure, Cost Distribution Concept, shows the data flow. Deliveries are the starting point
for this process. These create freight units, which are subsequently planned to create freight
orders or freight bookings. In addition to the charges in the freight order/booking, the
calculated charges are distributed to the delivery items contained in the freight order/
booking. Afterwards, freight settlement documents are created. When the FSD and
distributed costs are posted, a purchase order and service entry sheet are created in MM for a
subsequent invoice verification process. Additionally, a settlement document is created to
post the entries to CO-PA, CO or material valuation.

Cost Distribution Configuration

## Figure 133: Cost Distribution Configuration

Cost distribution needs to be enabled in the Freight Order / Freight Booking / FSD type
Customizing. Further settings for cost distribution include distribution profiles, methods,
rules, and levels. The distribution profile is assigned to the organizational unit for charge
calculation via the charges profile.

## Cost Distribution Profiles, Methods, and Rules
Cost distribution profiles are used to identify the rules for distributing freight costs. A cost
distribution profile consists of distribution method, distribution rule (basis for distribution),
and distribution level.

TM provides two methods for cost distribution, as follows:

● Direct:

This method is normally used when all charges incurred can be distributed directly to
individual line items of a delivery based on gross weight or volume without taking the
packaging hierarchy into account.

● Hierarchical:

© Copyright. All rights reserved.

189


Unit 7: Settle Transportation Charges and Distribute Costs

This method may be used when the packaging hierarchy may include other levels such as
container or rail cars. In such case, there may be charges for individual container or rail car
in addition to other charges. So, other charges need to be distributed to the container level
first and then the final distribution should take place to allocate the cost to the line item
level.

If required, you can add your own distribution methods.

SAP TM supports the following distribution rules to be used for cost distribution:

● Gross Weight

● Gross Volume

● Net Weight

● Distance times Weight

As a fifth option you may implement a BAdI to define your own logic.

The distribution level specifies the target level to which the system allocates transportation
charges for a freight order or freight settlement document. In the (basic) transportation
management scenario, the only possible distribution level is ERP item (delivery item).

Settlement Management configuration needs to be completed before cost distribution data
can be posted.

Posted data can be viewed using the transaction code WLFLTM2 or via Display Cost
Distribution Documents. Distribution data can be searched using the FSD number as the
reference document number.

Various scenarios are supported, including the following:

● Transfer freight costs for inbound deliveries and stock transfers into material valuation.

● Post distributed costs to CO so that material-relevant costs can be tracked at the profit

center level. In such cases, material valuation is not impacted.

● Post freight costs back to CO-PA for the customer outbound delivery to be accounted

during profitability analysis.

How to View a Settlement Document from Cost Distribution

Simulation: How to View a Settlement Document from Cost Distribution

For more information on How to View a Settlement Document from Cost
Distribution, please view the simulation in the lesson Distributing Transportation
Costs in your online course.

## Bill freight costs to customers in SD
When you sell your products to a customer, you may also take the responsibility of delivering
these products to that customer. For this, you incur costs for transportation, for example,
through a carrier. You can pass on these costs to your customer.

You use deliveries to facilitate transportation planning and execution in SAP Transportation
Management (TM). The SAP TM component creates or updates freight units directly for
deliveries. You plan transportation for these freight units by creating freight orders that you
then subcontract to the carrier. The freight order determines the freight costs to be paid to
the carrier. You configure SAP TM to distribute the freight costs in the freight order according

190

© Copyright. All rights reserved.


to delivery items. You can then add the distributed costs for each delivery item to the final
amount in the billing document that you send to your customer.

Lesson: Distributing Transportation Costs

## Figure 135: Billing Freight Costs in SD

Billing freight costs involves the integration of the following processes:

● Freight orders in TM

● Pricing in SD

● Billing in SD

Note:
You can only include the freight cost in a billing document when you have one
freight order document for the delivery and the freight order has only one
currency in which you calculate the cost.

Settle Transportation Charges with a Carrier

Simulation: Settle Transportation Charges with a Carrier

For more information on Settle Transportation Charges with a Carrier, please
view the simulation in the lesson Distributing Transportation Costs in your online
course.

© Copyright. All rights reserved.

191


Unit 7: Settle Transportation Charges and Distribute Costs

192

© Copyright. All rights reserved.


Unit 7
Exercise 10

Settle Transportation Charges with a Carrier

## Business Example

You want to show your colleagues how freight settlement documents for freight orders get
created and also show the distribution of costs to the corresponding delivery items.

Note:
In this exercise, when you see ##, replace the characters with the two-digit
number (01 to 30) assigned to you by your instructor.

1. Open the freight order for which you have calculated charges in the previous exercise and

create a freight settlement document for this freight order.

Write down the document number.

______________________________________________________

2. How are the different charges distributed among the three delivery items included in the

freight order?

Delivery

Charge
## Type

Assigned / Allocated Distribution Percent-

age

To customer TMBS##-01

BASE

FUEL

## HNDL

To customer TMBS##-01

BASE

FUEL

## HNDL

To customer TMBS##-01

BASE

FUEL

## HNDL

3. Can you explain the allocation/assignment of costs?

© Copyright. All rights reserved.

193


## Unit 7: Settle Transportation Charges and Distribute Costs

4. Post the settlement document to create a purchase order and service entry sheet. Check

the life cycle status of the freight settlement document.

5. Choose Refresh until the life cycle status changes to Posted. Note down the number of the

purchase order and service entry sheet that have been created.

Purchase Order

Service Entry Sheet

194

© Copyright. All rights reserved.


Unit 7
Solution 10

Settle Transportation Charges with a Carrier

## Business Example

You want to show your colleagues how freight settlement documents for freight orders get
created and also show the distribution of costs to the corresponding delivery items.

Note:
In this exercise, when you see ##, replace the characters with the two-digit
number (01 to 30) assigned to you by your instructor.

1. Open the freight order for which you have calculated charges in the previous exercise and

create a freight settlement document for this freight order.

a) In the SAP Fiori launchpad, go to Order Management →  Edit Road Freight Order.

b) Enter your Freight Order number (this varies).

c) Choose Continue.

d) From the dropdown menu, select Charges/Settlement →  Create freight settlement

document.

A new tab opens with the freight settlement document.

e) Choose Save All.

Write down the document number.

______________________________________________________

2. How are the different charges distributed among the three delivery items included in the

freight order?

Delivery

Charge
## Type

Assigned / Allocated Distribution Percent-

age

To customer TMBS##-01

BASE

FUEL

## HNDL

To customer TMBS##-01

BASE

FUEL

## HNDL

To customer TMBS##-01

## BASE

© Copyright. All rights reserved.

195


Unit 7: Settle Transportation Charges and Distribute Costs

Delivery

Charge
Type

FUEL

## HNDL

Assigned / Allocated Distribution Percent-

age

a) In the freight settlement document, navigate to the Cost Distribution tab.

The charges are distributed as follows:

Delivery

Charge
## Type

Assigned / Allocat-
ed

Distribution Percent-
age

To customer TMBS##-01 BASE

Allocated

## FUEL

Allocated

## HNDL

## Assigned

To customer TMBS##-01 BASE

Allocated

## FUEL

Allocated

## HNDL

## Assigned

To customer TMBS##-01 BASE

Allocated

## FUEL

Allocated

## HNDL

Assigned

16.7%

16.7%

100%

33.3 %

33.3 %

100%

50%

50%

100%

3. Can you explain the allocation/assignment of costs?

The BASE and FUEL charges are allocated proportional to the weight of the material being
transported.  The  HNDL  charges  are  not  allocated  proportional  to  their  weight  because
they have been calculated individually on item level and are therefore assigned directly.

4. Post the settlement document to create a purchase order and service entry sheet. Check

the life cycle status of the freight settlement document.

a) Choose Post.

b) Open the Statuses tab.

The life cycle status of the freight settlement document is Posting Started.

5. Choose Refresh until the life cycle status changes to Posted. Note down the number of the

purchase order and service entry sheet that have been created.

Purchase Order

## Service Entry Sheet

a) Open the Document Flow tab.

Purchase Order

Number varies

196

© Copyright. All rights reserved.


Lesson: Distributing Transportation Costs

Service Entry Sheet

## Number varies

© Copyright. All rights reserved.

197


Unit 7: Settle Transportation Charges and Distribute Costs

Verify a Freight Invoice

## Simulation: Verify a Freight Invoice

For more information on Verify a Freight Invoice, please view the simulation in
the lesson Distributing Transportation Costs in your online course.

198

© Copyright. All rights reserved.


Unit 7
Exercise 11

Verify a Freight Invoice

## Business Example

As a final step to conclude the process, you have to post the incoming invoice from the
carrier. You need to demonstrate this final step to your customer.

1. Post the invoice for your freight order for company code 1010 via transaction MIRO.

Note down the invoice number.

Invoice Number: _______________________________________

2. Review the full document flow of your freight order.

© Copyright. All rights reserved.

199


Unit 7
Solution 11

Verify a Freight Invoice

## Business Example

As a final step to conclude the process, you have to post the incoming invoice from the
carrier. You need to demonstrate this final step to your customer.

1. Post the invoice for your freight order for company code 1010 via transaction MIRO.

a) In the back-end, execute transaction MIRO.

b) In the pop-up window enter company code 1010 and press Continue.

c) For the Invoice Date, enter today’s date.

d) Enter the freight order number.

e) On the Basic Data tab, select tax code V1 from the dropdown menu and select the

checkbox Calculate Tax.

f) In the Amount field, enter the total cost of the freight order (this is the same as balance

on the top of the screen).

g) Verify that the balance is now zero.

h) Choose Simulate.

i) Choose Post.

Note down the invoice number.

Invoice Number: _______________________________________

2. Review the full document flow of your freight order.

a) In the SAP Fiori launchpad, go to Order Management →  Edit Road Freight Order.

b) Enter your Freight Order number (this varies).

c) Choose Continue.

d) Navigate to the Document Flow tab.

200

© Copyright. All rights reserved.


Lesson: Distributing Transportation Costs

## LESSON SUMMARY
You should now be able to:

● Distribute freight costs

© Copyright. All rights reserved.

201


Unit 7: Settle Transportation Charges and Distribute Costs

202

© Copyright. All rights reserved.


Unit 7

## Learning Assessment

1. Based on what you have learned about calculation sheets, place a tick beside each of the

options below which is true.

Choose the correct answers.

X A The calculation sheet is closely connected to rate tables and scales.

X B The calculation sheet provides a clear view on how the final amounts owing to

carriers are arrived at.

X C In the calculation sheet, you define a calculation method for each charge type.

X D A new calculation sheet must be created for each delivery.

2. Which of the following charge lines can a charge type classify?

Choose the correct answers.

X A Whether a charge line can be a positive or a negative value

X B Whether a charge line can be an absolute value or a percentage value

X C  Whether the charge line has a default calculation base

X D Whether the charge line has a minimum amount and a maximum amount

3. Using a rate table, a rate can be determined based on different dimensions.

Determine whether this statement is true or false.

X True

## X False

© Copyright. All rights reserved.

203


## Unit 7: Learning Assessment

4. When calculating carrier charges in a freight order, the freight agreement is determined

based on what?

Choose the correct answers.

X A Sales organization

X B Purchasing organization

## X C Carrier

X D Ordering party

5.

If you assign a calculation profile to an organizational unit and to a business partner role,
which calculation profile is applied during charge calculation?

Choose the correct answer.

X A The system applies the profile assigned to the organizational unit.

X B The system applies the profile assigned to the business partner

X C Depending on the scenario, the system will apply the relevant profile.

X D The system applies both and determines which profile is cheaper and uses that.

6. During freight settlement, a separate FSD is created for every freight order.

Determine whether this statement is true or false.

X True

## X False

7. Which of the following business documents are created when posting a freight settlement

document?

Choose the correct answers.

X A Sales order

X B Purchase order

X C Service entry sheet

X D Shipment cost document

204

© Copyright. All rights reserved.


8. Which of the following options are methods of cost distribution provided in TM?

Unit 7: Learning Assessment

Choose the correct answers.

X A Direct distribution

X B Indirect distribution

X C Hierarchical distribution

## X D Sequential distribution

9. Cost distribution takes place in which of the following documents?

Choose the correct answers.

X A  Freight order

## X B Freight booking

X C Freight settlement document

## X D Delivery

© Copyright. All rights reserved.

205


Unit 7: Learning Assessment

206

© Copyright. All rights reserved.


UNIT 8 Outlook – Advanced

Transportation

Lesson 1

Describing Advanced Transportation Management

209

## UNIT OBJECTIVES

● Describe the functionality included in Advanced Transportation

© Copyright. All rights reserved.

207


Unit 8: Outlook – Advanced Transportation

208

© Copyright. All rights reserved.


Unit 8
Lesson 1

Describing Advanced Transportation
## Management

## LESSON OBJECTIVES
After completing this lesson, you will be able to:

● Describe the functionality included in Advanced Transportation

## Advanced Transportation Management
This lesson highlights the functionality included in the advanced transportation management
scope.

Figure 138: Functions of Advanced Transportation

## Animation: Functions of Advanced Transportation

For more information on Functions of Advanced Transportation, please view the
animation in the lesson Describing Advanced Transportation Management in
your online course.

Advanced Transportation Management covers much more sophisticated functionality and
process-support compared to (basic) Transportation Management. The differences between
(basic) transportation management and advanced transportation management cover all
areas:

© Copyright. All rights reserved.

209


Unit 8: Outlook – Advanced Transportation

● Order Management

● Planning

● Freight Execution and Monitoring

● Charge Calculation and Settlement

● Analytics and Reporting

Order-Based Transportation Management

## Figure 140: Order-Based Transportation Management

One of the key differentiators in Order Management is that the transportation process can
already be initiated by the order (purchase order, sales order, stock transport order, MM
scheduling agreement) instead of the delivery. This allows to start transportation planning
processes well before the creation of the delivery. Subsequent delivery creation will update
the corresponding (order-based) freight units and all subsequent documents.

Furthermore, freight units cannot only be created based on documents from the same SAP
S/4HANA system, but different deployment options become available. For example, you can
create freight units based on orders (purchase order, sales order, stock transport order, SD
or MM scheduling agreement) or deliveries from another SAP ERP or SAP S/4HANA systems.

In addition, you can create freight units based on forwarding orders, which represent
transportation requirements without a preceding document from SD or MM.

210

© Copyright. All rights reserved.


Lesson: Describing Advanced Transportation Management

VSR Optimizer Constraints

Figure 141: VSR Optimizer Constraints

## Animation: VSR Optimizer Constraints

For more information on VSR Optimizer Constraints, please view the animation
in the lesson Describing Advanced Transportation Management in your online
course.

In the advanced transportation management scope, there are various optimization algorithms
included from VSR (vehicle scheduling and routing) to derive optimal routing decisions, VSO
(vehicle space optimization) to maximize use of truck space considering constraints like axle
weight limitations, to CS (carrier selection) to choose the right carrier based on real costs,
allocations and business shares.

The VSR optimizer considers all types of constraints listed in the figure, VSR Optimization
Constraints.

© Copyright. All rights reserved.

211


Unit 8: Outlook – Advanced Transportation

## Mixed Package Building

Figure 143: Mixed Package Building

## Animation: Mixed Package Building

For more information on Mixed Package Building, please view the animation in
the lesson Describing Advanced Transportation Management in your online
course.

Package building allows you to:

● Consolidate multiple products for the same customer into one mixed carton, and to

● Consolidate products for multiple customers into one mixed pallet.

Therefore, the physical positions of cartonized and non-cartonized products on mixed pallet,
considering stackability, incompatibilities, height, volume and weight constraints, and
orientation constraints of the products are determined.

212

© Copyright. All rights reserved.


Lesson: Describing Advanced Transportation Management

## Warehouse Integration

## Figure 145: Warehouse Integration

In the area of freight execution, highlights of the advanced transportation scope are:

● EWM integration (both to embedded and decentral EWM)

● Event Management integration for tracking and tracing via SAP EM and SAP LBN (GTT

option)

● Delivery Creation triggered from TM

● Discrepancy Management

● Tendering (Peer-to-Peer, Broadcast) direct and via SAP LBN

© Copyright. All rights reserved.

213


Unit 8: Outlook – Advanced Transportation

Charge Calculation and Settlement

Figure 146: Charge Calculation and Settlement

## Animation: Charge Calculation and Settlement

For more information on Charge Calculation and Settlement, please view the
animation in the lesson Describing Advanced Transportation Management in
your online course.

Advanced charge calculation functionality includes specific for air, ocean and rail transport:

● Commodity based charges

● Air freight charges based on TACT rules and regulation

●

Index table based fuel surcharge calculation

● Prepaid and collect on ocean booking

● Through Rate calculation

● Rule 11 on rail transports

Group logistics scenarios including internal settlement as well as dispute management with
external carriers are supported processes within the advanced transportation scope.

214

© Copyright. All rights reserved.


Lesson: Describing Advanced Transportation Management

## Embedded Analytics

## Figure 148: Embedded Analytics

Embedded analytics and reporting via CDS views are supported as part of advanced
transportation scope. These include, for example, the following card elements:

● Gross Weight Distribution

● Gross Volume Distribution

● Quantity Distribution

● Transportation Mode Category Analysis

● Logistic Network Analysis

● Carrier Quantity Analysis

● Shipper Quantity Analysis

● Consignee Quantity Analysis

● Utilization Distribution

● Quantity Analysis

● Distance Analysis

## LESSON SUMMARY
You should now be able to:

● Describe the functionality included in Advanced Transportation

© Copyright. All rights reserved.

215


Unit 8: Outlook – Advanced Transportation

216

© Copyright. All rights reserved.


Unit 8

## Learning Assessment

1. Which of the following documents can be predecessor documents of a freight unit in the

advanced transportation management scope?

Choose the correct answers.

## X A Sales Order

X B Order-based Transportation requirement

## X C Forwarding Order

X D Delivery-based Transportation Requirement

## X E Delivery

2. Which optimization algorithms are part of advanced transportation?

Choose the correct answers.

X A DS – Detailed Scheduling Optimizer

X B VSO – Vehicle Space Optimization

## X C CS – Carrier Selection

X D VSR – Vehicle Scheduling and Routing

## X E SEQ – Sequencing Optimizer

3. Package building allows to consolidate materials from different customers onto one pallet.

Determine whether this statement is true or false.

X True

## X False

© Copyright. All rights reserved.

217
