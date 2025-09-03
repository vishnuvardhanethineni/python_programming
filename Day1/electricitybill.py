consumer_number=int(input("Enter consumer number: "))
consumer_name=input("Enter consumer name: ")
present_reading=int(input("Enter present reading: "))
previous_reading=int(input("Enter previous reading: "))
units_consumed=present_reading-previous_reading
current_bill=units_consumed*3.80
print("Electricity Bill Details:")
print("Consumer Number:", consumer_number)
print("Consumer Name:", consumer_name)
print("Present Reading:", present_reading)
print("Previous Reading:", previous_reading)
print("Units Consumed:", units_consumed)
print("Current Bill:", current_bill)