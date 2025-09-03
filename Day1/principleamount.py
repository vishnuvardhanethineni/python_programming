principle_amount = float(input("Enter the principle amount: "))
rate_of_interest = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in months): "))
simple_interest = (principle_amount * rate_of_interest * time) / 100
print("Simple Interest is:", simple_interest)
total_amount = principle_amount + simple_interest
print("Total Amount is:", total_amount)
print("Thank you!")