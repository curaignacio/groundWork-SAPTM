Review Carrier Information

Review Carrier Information

Explanation

Screenshot

1. The Maintain
Business Partner
app and the search
string TM*CAR* for
the Business
Partner object were
already entered for
your convenience.

Choose Start to view
the list of available
carriers.

2. Choose TM-CAR-
10 to proceed.

3. To review carrier
data, choose the
Carrier role from the
dropdown menu.

Note: When the BP
role is changed to
Carrier, the Transport
Data tab appears.

1


Review Carrier Information

Explanation

Screenshot

4. Choose the
Transport Data tab to
proceed.

The role CRM010
(Carrier) includes the
data from role
FLVN01 (Vendor)
along with additional
TM-specific data,
such as:

•  Regulated

•

Agent Code
IATA Agent
## Code

•  CASS Account
•  SCAC Codes
•  Airline Codes
•  Service Level

## Codes

•  Carrier Service

## Codes

Choose Next to
continue.

2


Review Carrier Information

Explanation

Screenshot

5. Choose
Purchasing to
proceed.

The roles FLVN01
(Vendor) and
CRM010 (Carrier)
permit data
maintenance at the
purchasing
organization level.

On this level, you can
maintain attributes
like the order
currency and
payment terms you
agreed with the
carrier.

This concludes this
simulation.

3


Review Conditions

Review Conditions

Explanation

Screenshot

1. Choose the
Conditions Worklist
tile from the Profiles
and Settings group.

2. Choose the value
list for the Condition
Type field to access
the list of all existing
condition types.

3. The list includes 74
condition types and
their respective
application areas.

## The TCM_Rate
condition type is used
to determine a rate
table for charge
calculation.

Choose TCM_Rate to
proceed.

1


Review Conditions

Explanation

Screenshot

4. Choose the
condition
S4TM1_HAND_RAT
E_DET to proceed.

The origin of
condition F indicates
that this type of
condition uses a
BRFplus (Business
Rule Framework
plus) decision table.
The grey columns in
the decision table
represent the
decision criteria,
which, in this case, is
the destination
location.

The green columns
represent the
decision results,
specifically the rate
table. This means
that this condition is
utilized to determine
which rate table
should be used for
charge calculations
based on the
transport's
destination location.

2


Review Conditions

Explanation

Screenshot

Choose Next to
continue.

5. The decision
criteria in the decision
table are based on
data access
definitions that inform
the system on how to
retrieve these criteria.

Choose Data Access
Definition to proceed.

In the data access
definition, you specify
the values that the
system should use as
inputs for a decision
table and the sources
from which this data
will be retrieved. In
this case, the data
access definition
identifies the
destination location
for the data.

This concludes the
simulation.

3


Review Incompatibility

Review Incompatibility

Explanation

## Screenshot

1. Choose the Edit
Incompatibility app
from the Profiles and
Settings group to
proceed.

2. Choose the icon
for the value help list
to check for existing
definitions of
incompatibility.

3.
Incompatibilities
specify which objects
should not be
combined during
transportation.

For instance, ice
cream should not be
transported with
vehicles that lack a
cooling unit, as this
would cause the ice
cream to melt.

1


Review Incompatibility

Explanation

## Screenshot

Choose the selection
box for incompatibility
INC_S4TM1_VEH_F
U to continue.

The incompatibility
area defines where
the system should
account for an
incompatibility.

In this example,
incompatibility area
01 is used. This
means that
incompatibilities
maintained are
checked in all
automatic planning
applications, such as
VSR optimization,
load planning, load
consolidation, and
the creation of
transportation
proposals, as well as
during all manual
planning activities.
Further areas, as
listed in the search
box, are also
available to specify
the usage of
incompatibilities.
Choose Next to
continue.

2


Review Incompatibility

Explanation

## Screenshot

The incompatibility
type is used to define
the business objects
between which an
incompatibility should
be valid.

In this example, the
incompatibility
INC_S4TM1_VEH_F
U is defined between
Freight Unit(s) and
## Vehicle
Resource(s)/Vehicle
Type(s).

Choose Next to
continue.

In addition to the
incompatibility type
04 used in this
example, several
other incompatibility
types exist to support
the maintenance and
coverage of various
business processes.

Choose Next to
continue.

3


Review Incompatibility

Explanation

Screenshot

## When defining
incompatibilities, it is
possible to specify
whether the system is
permitted to violate
these
incompatibilities
during manual
planning or VSR
optimization.

This determination
can be made
independently for
manual planning and
automated planning.
For instance,
violations may be
forbidden during
automated planning,
while manual
overrides may be
allowed, resulting in
only a warning.

Choose Next to
continue.

Freight units for
which the condition
## INC_S4TM1_FU
returns a result of X
(these may be all that
include ice cream)
are deemed
incompatible with
vehicle resources or
vehicle types that
meet the second
condition,

4


Review Incompatibility

Explanation

Screenshot

INC_S4TM2_RES,
yielding a result of T.
(these may be all,
that do not have a
cooling unit)

Choose Next to
continue.

Through this
simulation, you have
learned how to
manage the
transportation of
specific freight units,
such as those with
particular
temperature
requirements.

This can only be
accomplished using
specific truck
resources, like those
equipped with cooling
units. These
limitations are known
as incompatibilities
and can become
quite complex in real
business
environments.

This concludes this
simulation.

5


Review Scenario Builder

Review Scenario Builder

Explanation

## Screenshot

1. The search string
Scenar was already
entered.

Choose the Scenario
Builder app from the
result list to proceed.

2. Choose the
S4TM1_SCENARIO
template.

A scenario template
consists of master
data and
configuration objects.

The master data
indicates which
objects are assigned
to the template and
the quantity of each.

The scenario
template
S4TM1_SCENARIO

1


Review Scenario Builder

Explanation

Screenshot

includes four
locations.

Choose Next to
continue.

3. Choose the
arrow next to the
figure 4 to view the
locations.

The locations

•  SP_1010
•  TMAT00-01
•  TMAT00-02
•  TMAT00-03

are assigned to this
template.

Choose Next to
continue

2


Review Scenario Builder

Explanation

## Screenshot

You can check which
transportation zones
are assigned to the
scenario template
and how these are
defined, including
their components.

Choose Next to
continue.

4. The Scenario
Builder's download
and upload functions
enable users to
manage scenario
templates as .zip
files.

Choose Download
to proceed.

There is a
corresponding
spreadsheet file
within the .zip file for
each object.

Click Next to
continue.

3


Review Scenario Builder

Explanation

Screenshot

5.
Double Click on the
locations
spreadsheet to view
details.

All the fields required
to create a location
are included in this
template. The
spreadsheets can be
updated, and the
revised template can
be uploaded into the
Scenario Builder.

Click Next to
conclude this
simulation.

4
