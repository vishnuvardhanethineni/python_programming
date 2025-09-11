def division(num1,num2):
    try:
        result = num1 / num2
        print(f"✅ Division successful: {num1} ÷ {num2} = {result:.2f}")
    except ZeroDivisionError:
        print("❌ Error: Division by zero is not allowed.")
    finally:
        print("⚡ Operation completed.\n")
division(5,6)
division(5,0)