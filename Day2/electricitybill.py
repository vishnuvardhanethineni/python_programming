consumer_number=int(input("Enter consumer number: "))
consumer_name=input("Enter consumer name: ")
present_reading=int(input("Enter present reading: "))
previous_reading=int(input("Enter previous reading: "))
units_consumed=present_reading-previous_reading
current_bill=0
if units_consumed>300:
    current_bill+=(units_consumed-300)*7.5
    units_consumed=300
if units_consumed>200:
    current_bill+=(units_consumed-200)*6.3
    units_consumed=200
if units_consumed>100:
    current_bill+=(units_consumed-100)*5.1
    units_consumed=100
if units_consumed>50:
    current_bill+=(units_consumed-50)*4.2
    units_consumed=50
current_bill+=units_consumed*3.8
print("Electricity Bill Details:")
print("Consumer Number:", consumer_number)
print("Consumer Name:", consumer_name)
print("Present Reading:", present_reading)
print("Previous Reading:", previous_reading)
print("Units Consumed:", units_consumed)
print("Current Bill:", current_bill)