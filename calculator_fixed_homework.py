from functions_for_caluclator import plu_operation, minus_operation, multiply_operation, divide_operation

print("Hello! This is a simple calculator")
continue_calculation = input("Do you wanna calculate? press 'Y' if you wanna see history press 'h':")

if "h" in continue_calculation:
    with open("History.txt", "r") as history_print:
        history = history_print.read()
        print(history)

while continue_calculation == "y":
    while True:
        first_number = input("Enter first number: ")
        if "," in first_number:
            print("Please use '.' for numbers")
        elif not first_number.replace(",", "", 1).isdigit():
            print("Please enter a valid number what does't have coma")
        else:
            break

    while True:
        operator = input("+ , - , * , / : ")
        if operator in ["+", "-", "*", "/"]:
            break
        else:
            print("Enter correct operator")
        operator = operator[0]

    while True:
        second_number = input("Enter second number: ")
        if "," in second_number:
            print("Please use '.' for numbers")
        elif not second_number.replace(",", "", 1).isdigit():
            print("Please enter a valid number")
        else:
            if operator == "/" and float(second_number) == 0:
                print("You can't devide wit 0, try again")

        break

    if operator == "+":
        operation_result = plu_operation(first_number, second_number)
    elif operator == "-":
        operation_result = minus_operation(first_number, second_number)
    elif operator == "*":
        operation_result = multiply_operation(first_number, second_number)
    elif operator == "/":
        operation_result = divide_operation(first_number, second_number)
    else:
        exit("something wrong try again")

    operation_result = round(operation_result, 2)

    result = f"{first_number} {operator} {second_number} = {operation_result}"

    with open("History.txt", "a") as history_print:
        history = history_print.write(f"{str(result)}\n")

    print(result)

    print("Do you want to calculate sometging else?")
    continue_calculation = input("y/n: ")

print("Bye!")