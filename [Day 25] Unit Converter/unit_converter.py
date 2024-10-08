def user_input(conversion_dict):
    # conversion_dict is a dictionary where it contain the data necessary for conversion
    input_unit = conversion_dict["original"]
    output_unit = conversion_dict["converted"]
    formula_constant = conversion_dict["number"]
    is_division = conversion_dict["is_division"]

    while True:
        try:
            num = int(input(f"Enter the value of {input_unit} to be converted into {output_unit}: "))
            print(f"{num} {input_unit} is equal to {num * formula_constant ** (-1 if is_division else 1)} {output_unit}")
            break
        except:
            print("The input must be a number. ")
            continue

def length():
    length_conversion_list = [
        {
            "original":"cm",
            "converted": "in",
            "number": 2.54,
            "is_division": True
        },{
            "original":"m",
            "converted": "ft",
            "number": 3.281,
            "is_division": False
        },{
            "original":"m",
            "converted": "yd",
            "number": 1.094,
            "is_division": False
        },{
            "original":"m",
            "converted": "mi",
            "number": 1609,
            "is_division": True
        },

        {
            "original":"in",
            "converted": "cm",
            "number": 2.54,
            "is_division": False
        },{
            "original":"ft",
            "converted": "m",
            "number": 3.281,
            "is_division": True
        },{
            "original":"yd",
            "converted": "m",
            "number": 1.094,
            "is_division": True
        },{
            "original":"mi",
            "converted": "m",
            "number": 1609,
            "is_division": False
        },
        
        {
            "original":"in",
            "converted": "ft",
            "number": 12,
            "is_division": True
        },{
            "original":"ft",
            "converted": "yd",
            "number": 3,
            "is_division": True
        },{
            "original":"yd",
            "converted": "mi",
            "number": 1760,
            "is_division": True
        },{
            "original":"mi",
            "converted": "yd",
            "number": 1760,
            "is_division": False
        }
    ] 

    while True:

        print("Enter the number you wish to use: ")
        for i,option in enumerate(length_conversion_list,1):
            print(f"[{i}] From {option["original"]} to {option["converted"]}")

        try:
            user_length_convert_input = int(input(">>> "))
            if user_length_convert_input in range(len(length_conversion_list) + 1):
                while True:
                    user_input(length_conversion_list[user_length_convert_input - 1])

                    print("Do you want to continue using this converter?[y/n]")
                    if input() in ["y","yes"]: 
                        continue
                    break

                print("Do you want to go back to the Main Menu? [y/n]")
                if input() in ["y","yes"]: 
                    break
        except KeyboardInterrupt:
            print("Break")
            break
        except:
            continue

def weight():
    print("WIP")
    pass

print("Welcome to the Unit Conversion App")

while True:
    print("Pick a category: ")
    print("[1] Length")
    print("[2] Weight")
    print("[3] Exit")
    try:
        user_category_input = int(input(">>> "))
        if (user_category_input in [1,2,3]):
            match user_category_input:
                case 1:
                    length()
                case 2:
                    weight()
                case 3:
                    break
    except KeyboardInterrupt:
        print("Exited using CTRL + C")
        quit(0)
    except:
        print("The input must be a number.")
        continue

print("Thank you for using the app and see you next time!")