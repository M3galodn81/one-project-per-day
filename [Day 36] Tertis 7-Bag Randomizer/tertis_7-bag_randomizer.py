import random

def generate_bag():  
    bag_stack = ["I","L","O","Z","S","T","J"]
    randomized_bag = []

    for x in range(len(bag_stack)):
        piece = random.choice(bag_stack)
        randomized_bag.append(piece)
        bag_stack.remove(piece)

    return randomized_bag

def main():
    print(generate_bag())
    print(generate_bag())
    print(generate_bag())
    print(generate_bag())

if __name__ == "__main__":
    main()