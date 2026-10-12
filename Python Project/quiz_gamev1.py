#===========================================
# Quiz Game
# language : Python
#===========================================
while True:
    questions = [
    "What keyword is used to create a function in Python?",
    "Which function displays output?",
    "Which symbol is used for comments?",
    "What data type stores True or False?",
    "Which loop repeats while a condition is true?"
     ]


    answers = [
    "def",
    "print",
    "#",
    "boolean",
    "while"
    ]

    print("\n===========================")
    print("       Quiz Game")
    print("===========================")

    print("1. Start Quiz")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        score = 0
        for i in range(len(questions)):
            print(f"\nQuestion {i + 1}: {questions[i]}")
            user_answer = input("Your answer: ").strip().lower()
            if user_answer == answers[i]:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {answers[i]}")

        print(f"\nYour final score is: {score}/{len(questions)}")

    elif choice == '2':
        print("Exiting the quiz game.")
        break

    else:
        print("Invalid choice. Please try again.")
