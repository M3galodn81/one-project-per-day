import json,random

questions = [
    {
        "question": "An IP address is a numeric quantity that identifies ...",
        "answer": "A network adapter to other devices on the network",
        "fake_answers": ["the manufacturer of a computer", "the physical location of a computer", "a router that separates the internal and external networks and provides basic security functions."]
    },
    {
        "question": "Which device is used to connect multiple devices on a network?",
        "answer": "Router",
        "fake_answers": ["Modem", "Switch", "Hub"]
    },
    {
        "question": "What is the primary function of DNS?",
        "answer": "Translate domain names to IP addresses",
        "fake_answers": ["Translate IP addresses to domain names", "Provide web hosting services", "Encrypt internet connections"]
    }
]

with open('[Day 24] Basic Quiz App/questions.json', 'w') as file:
    json.dump(questions, file, indent=4)

with open('[Day 24] Basic Quiz App/questions.json', 'r') as file:
    loaded_questions = json.load(file)

def quiz_game(questions):
    score = 0
    total_questions = len(questions)

    random.shuffle(questions)

    for i, question in enumerate(questions):
        print(f"\nQuestion {i+1}: {question['question']}")

        options = question["fake_answers"] + [question["answer"]]
        random.shuffle(options)

        for n,option in enumerate(options,1):
            print(f"[{n}] {option}")

        try:
            user_answer = int(input("Enter the number of your answer: "))
            if user_answer < 1 or user_answer > len(options):
                raise Exception
        except ValueError:
            print("Invalid input! Please enter a number corresponding to the choices.")
            continue

        if options[user_answer - 1] == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question['answer']}")

    print(f"\nYou answered {score} out of {total_questions} questions correctly!")

quiz_game(questions)