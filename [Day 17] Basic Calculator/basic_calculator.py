print("Welcome to the Calculator App")

# The users will type the first and the second numbers that they needed then select an operation to be performed

while True:
    try:
        first_num = float(input("Enter the first number: "))
        second_num = float(input("Enter the second number: "))

        print("Enter the operation that you want to use: ")
        print("[1] Addition")
        print("[2] Subtraction")
        print("[3] Multiplication")
        print("[4] Division")
        operation = input(">>> ")
        match operation:
            case "1":
                print(f"The sum of {first_num:g} and {second_num:g} is equal to {(first_num+second_num):g,}")
            case "2":
                print(f"The difference of {first_num:g} and {second_num:g} is equal to {(first_num-second_num):g,}")
            case "3":
                print(f"The product of {first_num:g} and {second_num:g} is equal to {(first_num*second_num):,g}")
            case "4":
                print(f"The quotient of {first_num:g} and {second_num:g} is equal to {(first_num/second_num):g,}")
            case _:
                raise Exception("Please enter 1, 2, 3 or 4 only")

        is_reset = input("Do you want to use the app again [yes/no (any other input will be converted into no)]")
        if is_reset in ['y','yes']:
            continue
        break

    except KeyboardInterrupt:
        break

    except:
        continue
