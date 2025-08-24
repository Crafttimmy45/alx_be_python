# Get user input
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses # Subtract expenses from income

# Project annual savings with 5% interest
total_savings = monthly_savings * 12       # Total saved in a year 
interest = total_savings * 0.05            # 5% interest on total_savings
projected_annual_savings = total_savings + interest # Add interest to the savings 

# Display the results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projectd savings after one year, with interest,is: ${projected_annual_savings:.2f}.")