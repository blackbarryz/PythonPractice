# Named Constants
MONTHS_IN_YEAR = 12

# Input Validation Loops using the Walrus Operator (:=)
# Validate monthly investment amount (must be positive)
while (monthly_investment := float(input("Enter a monthly investment amount: "))) <= 0:
    print("Error: investment must be a positive number")

# Validate yearly interest rate (must be positive)
while (yearly_interest_rate := float(input("Enter a yearly interest rate: "))) <= 0:
    print("Error: yearly interest rate must be a positive number")

# Validate investment period in years (must be positive integer)
while (investment_years := int(input("Enter how many years to invest: "))) <= 0:
    print("Error: investment period must be a positive number of years")

# Process Initialization
# Calculate total months and the monthly interest rate multiplier
total_months = investment_years * MONTHS_IN_YEAR
monthly_interest_rate = (yearly_interest_rate / 100) / MONTHS_IN_YEAR # Convert yearly interest rate to a monthly decimal rate by dividing by 100 to convert percentage to decimal and then by 12 for monthly rate

# Accumulator variable tracking the total account balance month-by-month
current_balance = 0.0

# Month-by-month compound calculation loop
for month in range(1, total_months + 1):
    # Step 1: Add the monthly investment to the existing balance
    current_balance += monthly_investment
    
    # Step 2: Apply the compound monthly interest to the new balance
    current_balance += current_balance * monthly_interest_rate
    
    # Output the ongoing balance tracking for each month
    print(f"Month {month:^4} revenue: ${current_balance:,.2f}")

# Final Output using F-string formatting
print()
print(f"After {investment_years} years, you will receive a total investment revenue of ${current_balance:,.2f} at a yearly rate of {yearly_interest_rate:.1f}%.")
print()