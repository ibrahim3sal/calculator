while True:
    calc = input("Enter your calculation: ")

    if "+" in calc:
        float_num1, float_num2 = calc.split("+")
        result = float(float_num1) + float(float_num2)

    elif "-" in calc:
        float_num1, float_num2 = calc.split("-")
        result = float(float_num1) - float(float_num2)

    elif "*" in calc:
        float_num1, float_num2 = calc.split("*")
        result = float(float_num1) * float(float_num2)

    elif "/" in calc:
        float_num1, float_num2 = calc.split("/")
        if float(float_num2) == 0:
            print("Error: Division by zero is not allowed.")
            continue
        result = float(float_num1) / float(float_num2)
    else:
        print("Invalid calculation. Please use +, -, *, or /.")
        continue

    print("Result:", result)

    another_calc = input("Do you want to perform another calculation? (y/n): ")

    if another_calc.lower() != "y":
        break