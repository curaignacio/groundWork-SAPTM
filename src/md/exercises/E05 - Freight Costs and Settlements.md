Explain a Freight Agreement

Explain a Freight Agreement

Explanation

## Screenshot

1. Choose the Freight
## Agreements
Worklist app to open
the corresponding
app.

2. The freight
agreement worklist
includes all freight
agreements detailing
the involved parties,
such as the
purchasing
organization and
carrier, along with
their validity periods
and current release
status.

Choose the freight
agreement
FRAGR_S4TM1_CA
R10 to proceed.

1


Explain a Freight Agreement

Explanation

Screenshot

•

3. On the General
Data tab of the freight
agreement, you will
find information like:
•  Agreement
version
Involved parties
(purchasing
organization
and carrier)
•  Validity period
•  Agreement
priority
•  Document
currency

Choose in the area
below the scroll bar
to scroll down.

 The freight
agreement items
(there is only one
item in this example)
are in the lower part
of the screen.

The items can have a
deviating validity
period (from the
header).

For each item, a
calculation sheet
defines the logic for
how charges are
calculated within this
freight agreement.

This concludes this
simulation.

2


Explain a Freight Agreement

Explanation

Screenshot

3


Explain a Calculation Sheet

Explain a Calculation Sheet

Explanation

Screenshot

1. Choose the
Charge Management
Worklist app to
access a worklist for
all master data
elements involved in
charge calculations.

2. Choose the All
Calculation
Sheets query to
display calculation
sheets.

3. Choose the
calculation sheet
S4TM1_CALCSHET_
CAR10 to open it.

1


Explain a Calculation Sheet

Explanation

## Screenshot

4. In the charge
calculation sheet you
will find all charge
types defined in the
calculation sheet in
the items section.

Choose in the area
below the scroll bar
to scroll down.

5. Additional details,
such as basic data,
rate information, and
classification data,
can be defined for
each item.

Choose the checkbox
to deselect the Sum
line to continue.

6. Choose the
checkbox for the
Basic Freight Charge
to display its details.

2


Explain a Calculation Sheet

Explanation

## Screenshot

7. On the Basic Data
tab, you can define
whether a charge is a
manual charge item
or whether it will
calculated
automatically.

Furthermore, you can
assign a rounding
and adjustment
profile to each charge
line.

Choose the Rate tab
to continue.

8. On the Rate tab,
you can either define
a rate amount, assign
a rate table or define
a rate table
determination rule
that determines the
rate table.

Choose the
Classification tab to
proceed.

3


Explain a Calculation Sheet

Explanation

Screenshot

9. In the
Classification tab,
you can view the
charge category and
subcategory.

Additionally, you can
specify whether a
charge line is
mandatory, a
statistical charge, or
a tax.

Choose the checkbox
to deselect the Basic
Freight Charge to
continue.

10. Choose the
checkbox for the
Handling Charge to
display its details.

4


Explain a Calculation Sheet

Explanation

## Screenshot

11. Choose in the
area below the
scroll bar to scroll
down.

On the Basic Data
tab for the handling
charge, the
calculation resolution
base is defined as
PRODUCT. This
means, that the
charge line is applied
multiple times in the
freight order, once for
each product, that is
transported.

This concludes this
simulation.

5


Work with Rate Tables

Work with Rate Tables

Explanation

## Screenshot

1. Choose the Edit
## Rate Table
Definition app to
open the
corresponding app.

2. For your
convenience the rate
table
BASE_RATE_00 was
already entered.

Choose Continue to
proceed.

3. On the General
Data tab of the rate
table, you define for
which charge type
the rate table can be
used.

Choose in the area
below the scroll bar
to scroll down.

1


Work with Rate Tables

Explanation

## Screenshot

4. Additionally, you
define the structure of
the rate table, which,
in this example,
consists of two
dimensions or scales.

The first dimension
relates to the
destination country of
the freight order.
## The second
dimension pertains to
the gross weight of
the freight being
transported.

Choose in the area
above the scroll bar
to scroll up.

5. Choose the Dates
and Values tab to
proceed.

2


Work with Rate Tables

Explanation

## Screenshot

6. On the Dates and
Values tab you can
define one or multiple
validity periods. At
the moment only one
validity period
(01.07.2021 -
31.12.9999) exists.

Choose in the area
below the scroll bar
to scroll down.

7. At the bottom of
the Dates and Values
tab, you will find a
detailed table of
rates.

This rate table is
structured based on
two dimensions
defined in the Basic
Data tab:

1.  The destination
country and

2.  The gross
weight

Now, how are these
rates applied?

To find out, choose
the Calculation Rules
tab.

3


Work with Rate Tables

Explanation

## Screenshot

8. The Calculation
Rule tab specifies the
calculation rule.
The rates on the
Rates tab are
charged per distance
and refer to a
distance of 100 km.

Choose the Rates tab
to return to the
previous screen.

9. If you need to
update rates you can
use the Update Rates
function.

Choose Update
Rates to proceed.

10. In the Update
Rates tab, you
define, what you want
to change.

In this example, you
want to increase
rates by 10%.
The new rates should
be valid in a new
validity period for the
calendar year 2025
(01.01.2025-
31.12.2025).

Choose in the area
below the scroll bar

4


Work with Rate Tables

Explanation

Screenshot

to scroll down.

11. Before you apply
your changes, you
want to simulate your
changes.

Choose the checkbox
for the simulation
mode to proceed.

12. Choose Update
to proceed.

13. The simulation
was successful. All
messages are green.

Choose in the area
below the scroll bar
to scroll down.

5


Work with Rate Tables

Explanation

## Screenshot

14. Uncheck the box
for simulation mode
to continue.

15. Choose Update
to proceed.

16. Choose OK.

6


Work with Rate Tables

Explanation

## Screenshot

17. The initial validity
period has been
divided into three
separate validity
periods:

•  01.01.2026 -
31.12.9999
(using the old
rates)

•  01.01.2025 -
31.12.2025
(using the new
rates)
•  01.07.2021 -
31.12.2024
(using the old
rates)

Note, that the first
validity period is
currently selected,
and the first two rates
shown for destination
country AT are 120
EUR and 60 EUR.

Please select the
radio button for the
second validity period
to check the new
rates.

7


Work with Rate Tables

Explanation

## Screenshot

18. The new rates
are 10% higher as
per your update
request.

The first two rates for
destination country
AT are now 132 EUR
and 66 EUR.

You are happy with
the result and choose
Save to proceed.

19. In the following,
rate changes are
applied using the MS
Excel integration.

Choose the Excel
Integration tab to
proceed.

20. Choose
Download to
download the current
rate table for all
validity periods.

8


Work with Rate Tables

Explanation

## Screenshot

21. The downloaded
MS Excel sheet is
protected. This
means you can
change the values,
but you should not
alter the structure of
the sheet. The
workbook contains
three sheets, each
corresponding to a
different validity
period.

To proceed, select
the tab labeled with
the new rates' validity
period (effective
January 1, 2025).

22. For the cell
highlighted, type the
value 135 and
confirm your entry by
pressing the Enter
key.

9


Work with Rate Tables

Explanation

## Screenshot

23. In addition, new
rates for France
should be entered.

Enter FR in the box.

Note, that a value list
of existing country
code keys of SAP is
checked/a dropdown
list is offered!

Confirm your entry by
pressing the Enter
key.

24. For your
convenience, several
rates for France have
already been
entered.

Choose Save to
proceed.

25. Once you return
to the Rate Table
## Definition
maintenance screen,
you need to enter the
local file to allow a
correct update.

Choose Upload to
proceed.

10


Work with Rate Tables

Explanation

## Screenshot

26. Choose Save.

27. Choose the Dates
and Values tab to
check the result of
the upload.

The updated values
are now visible in the
rate table.

The minimum amount
for country AT has
been changed to 135
EUR and the rates for
country FR have
been added.

This concludes this
simulation.

11


Work with Rate Tables

12


Explain Scales

Explain Scales

Explanation

## Screenshot

1. Choose the Edit
Scale app to open
the corresponding
app.

2. For your
convenience the
scale
## S4LG1_COUNTRY
was already entered.

Choose Continue to
proceed.

3. On the General
Data tab, the scale is
linked to a scale
base.
In this simulation, the
scale pertains to
countries.

Choose the Items tab
to proceed.

1


Explain Scales

Explanation

## Screenshot

4. On the Items tab,
the countries used to
establish rates based
on this scale are
defined.

Choose the SAP logo
to navigate back to
your home page.

5. Choose the Edit
Scale app to open
the corresponding
app again.

6. For your
convenience a
second scale
## S4LG1_WEIGHT
was already entered.

Choose Continue to
proceed.

2


Explain Scales

Explanation

## Screenshot

7. This is a numerical
scale. In addition to
the scale base, you
can specify the type
of scale (either From
Scale or To Scale),
the unit of measure
for the scale, and the
rounding profile.

Choose the Items tab
to proceed.

On the Items tab, you
can define the scale
values.

In this example, the
following rates for
weights were
established based on
this scale:

•  up to 100 kg
•  up to 200 kg
•  up to 500 kg
•  up to 1.000 kg
•  up to 5.000 kg
•  up to

999.999.999 kg

This concludes this
simulation.

3


Calculate Transportation Charges and Analyze the Results

Calculate Transportation Charges and Analyze the Results

Explanation

## Screenshot

1. Choose the freight
order 200000109 to
open it.

2. Choose Calculate
Charges from the
dropdown menu to
proceed.

3. Choose the
Expand all icon to
see more details of
the calculation result.

1


Calculate Transportation Charges and Analyze the Results

Explanation

## Screenshot

4. The calculation
result is displayed in
detail.
You can analyze how
each charge type
was calculated by
selecting it.

Choose the checkbox
for the Basic Freight
Charge to proceed.

5. Choose Show/Hide
Details to display the
details for the basic
freight charge.

6. Choose in the area
below the scroll bar
to scroll down.

2


Calculate Transportation Charges and Analyze the Results

Explanation

## Screenshot

7. In the Overview
tab, you can see
which agreement,
calculation sheet, and
rate table were used
to calculate the
charge. Additionally,
the rate amount and
the calculated
amount are displayed
here.

Choose the
Calculation Rules tab
to see how these
values have been
computed.

8. On the Calculation
Rules tab, you can
see that the charge is
based on the net
weight of 5.180 KG,
and the determined
rate amount is per 10
KG.

Choose the checkbox
for the basic freight
charge to deselect it.

3


Calculate Transportation Charges and Analyze the Results

Explanation

## Screenshot

9. For the second
handling charge,
which has already
been selected for
your convenience,
you can find the
relevant details on
the Overview tab.

Again, the
agreement,
calculation sheet, and
rate table used to
determine the charge
are shown as well as
the rate amount and
the calculated
amount.

Choose the
Calculation Rules tab
to check how these
values have been
calculated.

The Calculation
Rules tab shows that
the charge is based
on a quantity of 2
pieces, and the
determined rate is
applied per 1 PC.

Finally, you want to
add a 50 EUR waiting
time surcharge.

Confirm the value
already maintained
by pressing ENTER
to proceed.

4


Calculate Transportation Charges and Analyze the Results

Explanation

## Screenshot

10. Choose Save and
return to the freight
order worklist.

11. Choose
Refresh to check,
whether there are still
freight orders with the
status Not
Calculated.

12. Four freight
orders have already
been selected for
your convenience.

Choose Calculate
Charges to proceed.

5


Calculate Transportation Charges and Analyze the Results

Explanation

Screenshot

13. Choose
Refresh to check the
calculated amounts.

The selected freight
orders show the
charge calculation
status
Calculated and the
amount determined
(net amount in
document currency).

This concludes this
simulation.

6


Create and Post a Freight Settlement Document and Verify the Invoice

Create and Post a Freight Settlement Document and Verify the Invoice

Explanation

## Screenshot

1. Choose Edit to
allow changes for the
freight order
20000109.

2. Choose Create
Freight Settlement
Document from the
dropdown menu to
proceed.

3. The freight
settlement document
is initially created with
a temporary order
number ($1).

Choose Save All.

1


Create and Post a Freight Settlement Document and Verify the Invoice

Explanation

## Screenshot

4. The settlement
date and the
responsible
organization
(purchasing
organization) are
some of the fields
shown in the General
Data tab of the freight
settlement document.

Choose in the area
below the scroll bar
to scroll down.

5. In the Charges tab,
you will find the
charges that will be
settled with this
freight settlement
document. These
charges are the same
as those in the
related freight
order(s).

Choose the Orders
tab to find out, which
freight orders are
settled with this
document.

2


Create and Post a Freight Settlement Document and Verify the Invoice

Explanation

## Screenshot

6. Only one freight
order is settled with
this freight settlement
document.
It is freight order
20000109 from which
we have created this
document.

Choose in the area
above the scroll bar
to scroll up.

7. Choose the
Business Partner tab
to find out which
business partners
(roles) are involved in
this settlement
process.

8. The payee, carrier,
and invoicing party
are involved in this
process.

Choose the
Statuses tab to
proceed.

3


Create and Post a Freight Settlement Document and Verify the Invoice

Explanation

## Screenshot

9. The Life Cycle
Status is Ready for
Accruals and the
Freight Settlement
Confirmation Status
is Not Posted.

Choose Post to post
the freight settlement
document.

10. The Life Cycle
Status changed to
Posting Started and
the Freight
## Settlement
Confirmation Status
changed to Not
Confirmed.
This is an
asynchronous
process that has
been triggered in the
background.

Choose Refresh to
check for the
completion of the
posting process.

4


Create and Post a Freight Settlement Document and Verify the Invoice

Explanation

Screenshot

11. The posting
process is completed.

The Life Cycle Status
has changed to
Posted and the
Freight Settlement
Confirmation Status
has changed to
Confirmed.

Choose the
Document Flow tab
to proceed.

In the Document
Flow tab, you can
find all documents
involved in this
process. The
documents that
precede the freight
settlement document
include the following
logistical documents:
•  Freight order(s)
•  Freight unit(s)
•  Outbound

deliveries and
outbound
delivery orders

•  Sales orders

Financial documents
created in the MM
module succeed the
freight settlement
document.

•  Purchase order
•  Service entry

sheet

5


Create and Post a Freight Settlement Document and Verify the Invoice

Explanation

## Screenshot

You want to post the
invoice of the carrier,
which will be done
using the classical
SAP GUI.

Choose Next to
continue.

12. Enter miro in the
Transaction box.

Confirm your entry by
pressing the Enter
key.

13. Enter company
code 1010.

Confirm your entry by
pressing the Enter
key.

6


Create and Post a Freight Settlement Document and Verify the Invoice

Explanation

## Screenshot

14. Enter the invoice
date 10.10.2024.

Confirm your entry by
pressing the Enter
key.

15. Enter freight
order number
200000109.

Confirm your entry by
pressing the Enter
key.

16. The tax code for
the freight order has
been determined as
V1.

Choose the
corresponding tax
code from the
dropdown menu to
calculate the taxes
accordingly.

7


Create and Post a Freight Settlement Document and Verify the Invoice

Explanation

Screenshot

17. Select the
Calculate Tax check
box.

18. Enter the full
amount of
1961,62 EUR.

Confirm your entry by
pressing the Enter
key.

19. The amount
almost matches the
calculated result from
the freight order plus
taxes.
## The remaining
balance is calculated
as 0,05 EUR.

Choose Simulate to
check to which
accounts the charges
will be posted.

You can also press
Ctrl+Shift+F7.

8


Create and Post a Freight Settlement Document and Verify the Invoice

Explanation

## Screenshot

20. You can verify
that the charges are
posted to the
intended G/L
accounts.

Choose Post to post
the invoice finally.
You can also press
Ctrl+S.

Afterward, navigate
back to your freight
settlement document.

21. Choose
Refresh to refresh the
freight settlement
document.

9


Create and Post a Freight Settlement Document and Verify the Invoice

Explanation

## Screenshot

The invoice becomes
visible in the
Document Flow and
the status of the
freight settlement
document has been
updated to Invoice
Verified.

This concludes this
simulation.

10


Distribute Freight Costs and Bill Transportation Charges to Customers

Distribute Freight Costs and Bill Transportation Charges to Customers

Explanation

## Screenshot

1. Choose the Cost
Distribution tab to
review how the
freight charges are
distributed to the
delivery items
transported with this
freight order.

2. Choose Expand to
analyze which
charges have been
distributed to delivery
delivery 80000175.

## The delivery
80000175 must cover
390.15 EUR of the
total freight charges.
The handling charge
has been fully
assigned to this
delivery.
Other charges have
been allocated
proportionally based
on gross weight.

Click Next to
continue.

1


Distribute Freight Costs and Bill Transportation Charges to Customers

Explanation

## Screenshot

3. Create billing was
already entered into
the search bar for
your convenience.

 Choose the Create
Billing Document
app.

4. Delivery 80000175
was already selected
for your convenience.

Choose Create Billing
Documents.

5. Choose Save to
save the invoice
document.

2


Distribute Freight Costs and Bill Transportation Charges to Customers

Explanation

## Screenshot

6. Choose Pricing
Elements to check
whether the
distributed freight
charges have been
billed to your
customer.

The pricing elements
include one condition
type (FB00) to
represent freight
charges.
The freight charges
are 390,15 EUR,
which has been taken
over from the freight
order/freight
settlement document.

This concludes this
simulation.

3
