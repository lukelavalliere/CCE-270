**Concrete Slab Calculator**

**Purpose**

Create a simple web app that calculates how much concrete is needed for a rectangular slab and estimates the total concrete cost.

**Inputs**

Slab length in feet
- Slider
- Range: 5 to 100 ft
- Default: 20 ft
- Step: 1 ft

Slab width in feet
- Slider
- Range: 5 to 100 ft
- Default: 30 ft
- Step: 1 ft

Slab thickness in inches
- Slider
- Range: 4 to 12 in
- Default: 6 in
- Step: 0.5 in

Waste factor in percent
- Slider
- Range: 0% to 15%
- Default: 5%
- Step: 1%

Concrete price in dollars per cubic yard
- Number input
- Default: $150 per cubic yard

**Calculations**

Convert slab thickness from inches to feet:

thickness_ft = thickness_in / 12

Calculate volume in cubic feet:

volume_ft3 = length * width * thickness_ft

Convert cubic feet to cubic yards:

volume_yd3 = volume_ft3 / 27

Add the waste factor:

volume_with_waste = volume_yd3 * (1 + waste_factor / 100)

Round the concrete amount up to the nearest 0.25 cubic yard.

Calculate total cost:

total_cost = rounded_concrete_amount * price_per_cubic_yard

**Outputs**

The app should display:
- Concrete volume in cubic yards
- Concrete amount rounded up to the nearest 0.25 cubic yard
- Total estimated concrete cost
- A plan-view diagram of the slab
- Labels showing the slab length, width, and thickness

**Look and Feel**

Use a clean and professional layout.

Put the input controls on the left side of the page.

Put the calculated results and slab diagram on the right side of the page.

Clearly label all values and units.

The slab diagram should update when the user changes the dimensions.

**Validation**

Test values:
- Length = 20 ft
- Width = 30 ft
- Thickness = 6 in
- Waste factor = 5%
- Concrete price = $150 per cubic yard

Hand calculation:

6 / 12 = 0.5 ft

20 * 30 * 0.5 = 300 ft³

300 / 27 = 11.11 yd³

11.11 * 1.05 = 11.67 yd³

Rounded up to the nearest 0.25 cubic yard = 11.75 yd³

11.75 * 150 = $1,762.50

Expected output:
- Concrete volume = about 11.11 yd³
- Concrete order = 11.75 yd³
- Total cost = $1,762.50

**Out of Scope**

Do not include:
- Reinforcing steel calculations
- Labor costs
- Excavation costs
- Formwork costs
- Delivery fees
- Pumping costs
- User accounts
- Saved projects