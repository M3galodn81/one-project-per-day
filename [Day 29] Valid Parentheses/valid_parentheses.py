import string

def check_valid_parentheses(user_input):
    user_input = "".join(char for char in user_input if char in set("([{}])"))
    print(user_input)
    parentheses = {
        "(":")",
        "[":"]",
        "{":"}"
    }

    stack = []

    for i,char in enumerate(user_input):
        print(char,i,stack)
        
        if char in parentheses.keys():
            stack.append(char)
        elif char in parentheses.values():
            if len(stack) == 0:
                return False
            
            print(char,parentheses[stack[len(stack)-1]])
            if (char) == (parentheses[stack[-1]]):
                stack.pop()
            else:
                print("B")
                return False

    print(stack)
    if len(stack) != 0:
        return False
    return True
    
def main():
    print(check_valid_parentheses("(]"))
    # print(check_valid_parentheses("{{{{[]{}}}}}"))
    # print(check_valid_parentheses("({}{()})"))
    # print(check_valid_parentheses("()))"))
    # print(check_valid_parentheses("())"))
    # print(check_valid_parentheses("(((()"))


if __name__ == "__main__":
    main()