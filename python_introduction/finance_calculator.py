#script that calculates user's savings over a period

monthly_income = int(input("Enter your monthly income: "))
total_monthly_expense = int(input("Enter your total monthly expense: "))

monthly_savings = monthly_income - total_monthly_expense

projected_savings = monthly_savings * 12 + int((monthly_savings * 12 * 0.05))

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
