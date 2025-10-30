# Electricity Bill Calculator - Initial Version

# Ask user for the number of units consumed
units = int(input("Enter units consumed: "))

# Cost per unit
rate_per_unit = 5

# Calculate total bill
total_bill = units * rate_per_unit

# Display total bill
print(f"Total Bill: ₹{total_bill}")
