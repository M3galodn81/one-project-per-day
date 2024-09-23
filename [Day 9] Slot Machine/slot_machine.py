import random
import sys,time
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8') # for emojis

print("Welcome to the Slot Machine")

print("""
Here are the rules:
You were given 1,000 coins in the beginning of the session, and of course, you want to earn a lot of money.
The slot machine allows you to place bets using your coins, and for each spin, you have a chance to win or lose coins depending on the outcome.

- You can bet between 1 to 1000 coins per spin.
- The slot machine has different symbols, each with its own payout:
    - Three cherries (🍒): 10x your bet
    - Three lemons (🍋): 5x your bet
    - Three stars (✨): 50x your bet
    - Two matching symbols: 2x your bet
    - No match: You lose your bet

- If you run out of coins, the game ends.
- If you reach 69,000 coins, you win the game and can cash out.

Good luck and spin wisely!
""")

symbols = ["🍒","🍋","✨","🍇","🍊"]
final_roll = []
balance = int(1000)

def roll(amount:int):
    global balance
    print(f"\nCurrent Bet: {amount} coins")
    
    final_roll = []
    for _ in range(0,3):
        final_roll.append(random.choice(symbols))

    print("You rolled.\n") 
    typewriter_effect(final_roll)


    count = Counter(final_roll)
    duplicates = [element for element, freq in count.items() if freq == 2]

    if final_roll[0] == final_roll[1] == final_roll[2] :
        match final_roll[0]:
            case "🍒":
                balance += (win(amount,10))
            case "🍋":
                balance += win(amount,5)
            case "✨":
                balance += win(amount,50)
            case "🍇":
                balance += win(amount,15)
            case "🍊":
                balance += win(amount,25)
    elif duplicates:
        balance += win(amount,2)
    else: 
        print(f"No matches. You lost {amount} coins.")
        balance -= amount

def win(bet,multiplier: int):
    print(f"You win {bet * multiplier} coins")
    return bet * multiplier

def typewriter_effect(rolls):
    print("-------------")

    sys.stdout.write("| ")
    
    for slot in rolls:
        sys.stdout.write(f"{slot} | ")  
        sys.stdout.flush()  
        time.sleep(0.5)
    
    print("\n-------------")



while True:
    
    try:
        if balance >= 69000:
            print("You're a professional gambler. You win")
            break
        if balance <= 0:
            print("You broke now pain.................................................")
            break

        bet = int(input(f"How much do you want to bet? [Current Balance: {balance}] : "))
        if bet in range(1,1001):
            roll(bet)

        else:
            raise Exception
    except:
        print(f"The bet must be a number within 1 to 1000:")

    