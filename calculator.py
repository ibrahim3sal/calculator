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
        result = float(float_num1) / float(float_num2)
        print("Result:", result)

    another_calc = input("Do you want to perform another calculation? (y/n): ")

    if another_calc.lower() != "y":
        break
