#Financial details
income = input("Enter your monthly income:")
expenses = input("Enter your total monthly expenses:")

#calculate monthly savings
savings = int(income) - int(expenses)

rate = 0.05  # Assume a fixed interest rate of 5%
# Calculate the projected savings after one year
projected_savings = savings * 12 * (1 + rate)

print(f"Your monthly savings are: {savings}")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}")
