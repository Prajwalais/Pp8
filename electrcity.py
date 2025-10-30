# Electricity Bill Calculator - Initial Version

# Ask user for the number of units consumed
units = int(input("Enter units consumed: "))

# Cost per unit
rate_per_unit = 5

# Calculate total bill
total_bill = units * rate_per_unit

# Display total bill
print(f"Total Bill: ₹{total_bill}")




# Apply 10% discount if bill exceeds ₹1000
if total_bill > 1000:
    discount = total_bill * 0.10
    final_bill = total_bill - discount
    print(f"Discount Applied: ₹{discount}")
    print(f"Final Bill: ₹{final_bill}")
else:
    print("No discount applied.")
    print(f"Final Bill: ₹{total_bill}")
