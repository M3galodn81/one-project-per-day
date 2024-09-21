import random
import string
import time

valid_letters = string.ascii_lowercase
words = ["property","coat","pillow","attract","performer","trial","estate","scenario"]


word_to_guess = random.choice(words)
letters_of_word_to_guess = list(word_to_guess)

word_reference = letters_of_word_to_guess
word_display = []
used_letters = []

for x in letters_of_word_to_guess:
    word_display.append("_")

def guess_letter(answer):
    if not(answer in used_letters):
        if answer in letters_of_word_to_guess:
            for x in range(len(word_reference)):
                if word_reference[x] != word_display[x]:
                    word_display[x] = answer
                    used_letters.append(answer)
                    return True
        else:
            print(f"The letter {answer} is not a letter of that word. ")
            used_letters.append(answer)
            return True
    else: 
        print(f"The letter {answer} already used to guess the word. ")
        return False
    

def display_progress():
    print(f"\nWord: ")
    print(word_display)

def answer_validation():
    while True:
        answer = input("Guess a letter: ")
        if answer.lower() in valid_letters:
            if guess_letter(answer): break
        else:
            print("Only letters are valid")
            continue


print("Welcome to the Word Guessing Game!")


while True:
    print("The game will decide what the word your guessing will be . . .")
    time.sleep(3)
    

    while True:
        display_progress()
        answer_validation()
        if "_" not in word_display:
            break
            
    print(f"You guessed the word {word_to_guess}")
    retry = input("Do you want to continue? [y/n]").lower()
    if retry == "y":  
        continue
    else:
        print("See you next time!")
        break          
