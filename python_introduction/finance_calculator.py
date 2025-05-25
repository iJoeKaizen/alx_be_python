#Financial details
monthly_income = input("Enter your monthly income:")
monthly_expenses = input("Enter your total monthly expenses:")

#calculate monthly savings
monthly_savings = int(monthly_income) - int(monthly_expenses)

rate = 0.05  # Assume a fixed interest rate of 5%
# Calculate the projected monthly_ after one year
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * rate)

print(f"Your monthly savings are: {monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
