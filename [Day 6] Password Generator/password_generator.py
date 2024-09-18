import string,random

print("Welcome to the Password Generator")

while True:
    try:
        no_of_chars = int(input(f"How many characters?"))
        if no_of_chars < 1: raise Exception
        break
    except:
        print(f"The input must be a positive number")
        continue

while True:
    try:
        have_symbols = input(f"Do you want it to have symbols? [y/n]")
        if not(have_symbols in ['y','n']): raise Exception
        break
    except:
        print(f"The input must be 'y' or 'n'.")
        continue

symbols = string.punctuation
digits = string.digits
capital_letters = string.ascii_uppercase
small_letters = string.ascii_lowercase

password = []

def random_char():
    characters = [digits,capital_letters,small_letters]
    if have_symbols == 'y':
        characters.append(symbols)
        return random.choice(random.choice(characters)) 
    else:
        return random.choice(random.choice(characters)) 
    

for i in range(no_of_chars):
    password.append(random_char())

password = "".join(password)

print(f"The new password is : {password}")