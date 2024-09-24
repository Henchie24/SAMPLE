monthly_salary = int(input("Enter Amount Of Monthly Salary: "))
loan_amount = int(input("Enter Loan Amount: "))
valid_loan = monthly_salary * 10
months = int(input("How Many Months of Payment: "))




if monthly_salary <= 30000 and loan_amount >= valid_loan:
    print(months)
    payment_to_loan = loan_amount * 0.10
    print("Your Payment To Loan in"," ", months: payment_to_loan )
else:
    print("Loan Declined")
    
