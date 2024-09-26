#data
monthly_salary = int(input("enter amount Of monthly salary: "))
valid_loan = monthly_salary * 10
print("=========================") #breaker

if monthly_salary>=30000:
    print(f"you are eligible for a loan!\nloan available: ${valid_loan:.2f}")

    while True:
        loan_amount = int(input("enter loan amount: "))

        if loan_amount>valid_loan:
            print("=========================\nloan declined, your demand is too high")

        else:
            months = int(input("how many months of payment: "))
            interest = loan_amount * 0.10
            payment_to_loan = loan_amount + interest
            print(f"=========================\nloan interest: ${interest:.2f}\ntotal payment for The loan: ${payment_to_loan:.2f}")
            monthly_payment_to_loan = (payment_to_loan / months)
            print (f"to be payed monthly in {months} months: ${monthly_payment_to_loan:.2f}")
            break
        
else:
    print("loan declined, your salary is either low or too high")


