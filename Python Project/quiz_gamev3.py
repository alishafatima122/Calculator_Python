#==============================================
# Quiz Game version 3.0
# language: Python
#==============================================
import random

# ================= EASY LEVEL =================

easy_questions = [
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["func", "def", "function", "create"],
        "answer": "def"
    },
    {
        "question": "Which function is used to display output in Python?",
        "options": ["print()", "show()", "display()", "output()"],
        "answer": "print()"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/* */", "<!-- -->"],
        "answer": "#"
    },
    {
        "question": "What is the correct extension of Python files?",
        "options": [".py", ".python", ".pt", ".pyt"],
        "answer": ".py"
    },
    {
        "question": "Which data type stores text?",
        "options": ["int", "float", "str", "bool"],
        "answer": "str"
    }
]


# ================= MEDIUM LEVEL =================

medium_questions = [
    {
        "question": "Which loop is used to iterate over a sequence?",
        "options": ["while", "for", "repeat", "loop"],
        "answer": "for"
    },
    {
        "question": "Which method adds an item to a list?",
        "options": ["add()", "append()", "insert()", "push()"],
        "answer": "append()"
    },
    {
        "question": "What does len() return?",
        "options": ["Value", "Length", "Type", "Index"],
        "answer": "Length"
    },
    {
        "question": "Which keyword handles errors?",
        "options": ["catch", "error", "try", "handle"],
        "answer": "try"
    },
    {
        "question": "Which file mode is used to add data?",
        "options": ["r", "w", "a", "x"],
        "answer": "a"
    }
]


# ================= HARD LEVEL =================

hard_questions = [
    {
        "question": "Which concept allows inheritance?",
        "options": ["Inheritance", "Looping", "Indexing", "Iteration"],
        "answer": "Inheritance"
    },
    {
        "question": "What does __init__ do?",
        "options": ["Creates objects", "Deletes objects", "Prints output", "Imports modules"],
        "answer": "Creates objects"
    },
    {
        "question": "Which module works with dates?",
        "options": ["random", "datetime", "timepass", "calendar"],
        "answer": "datetime"
    },
    {
        "question": "Which keyword creates an anonymous function?",
        "options": ["func", "lambda", "anonymous", "def"],
        "answer": "lambda"
    },
    {
        "question": "Which method removes the last list item?",
        "options": ["remove()", "delete()", "pop()", "clear()"],
        "answer": "pop()"
    }
]


# ================= FILE HANDLING =================

def save_score(name, level, score, total):

    with open("high_scores.txt", "a") as file:
        file.write(f"{name} | {level} | {score}/{total}\n")

def view_scores():

    try:
        with open("high_scores.txt", "r") as file:
            scores = file.readlines()

        if not scores:
            print("No scores available.")
            return
# strip use for make a new line like \n remove
        scores = [score.strip() for score in scores]
# lambda function is used to sort the scores based on the score value in descending order and an anonymous function..
# split is use to splite like here it will spilt | and \ from the scores ..
        scores.sort(
            key=lambda x: int(x.split("|")[2].split("/")[0]),
            reverse=True
        )

        print("\n========== TOP SCORES ==========")
# enumerate is used to push an index number..
        for index, score in enumerate(scores[:10], start=1):
            print(f"{index}. {score}")

    except FileNotFoundError:
        print("No scores available.")

# ================= QUIZ FUNCTION =================

def start_quiz(questions, level):
    score = 0
    questions = questions.copy()
    random.shuffle(questions)

    for q in questions:
        print("\n" + q["question"])
        for i, option in enumerate(q["options"], start=1):
            print(f"{i}. {option}")

        try:
            answer = int(input("Enter answer number: "))
            if q["options"][answer - 1] == q["answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! Correct answer: {q['answer']}")

        except (ValueError, IndexError):
            print("Invalid input!")

    print(f"\nFinal Score: {score}/{len(questions)}")


    name = input("Enter your name to save score: ")
    save_score(name, level, score, len(questions))
    print("Score saved!")

# ================= MAIN MENU =================
while True:
    print("\n================ QUIZ GAME ================")
    print("1. Start Quiz")
    print("2. View High Scores")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\nSelect Difficulty")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")

        level_choice = input("Enter level: ")

        if level_choice == "1":
            start_quiz(easy_questions, "Easy")
        elif level_choice == "2":
            start_quiz(medium_questions, "Medium")
        elif level_choice == "3":
            start_quiz(hard_questions, "Hard")
        else:
            print("Invalid level!")

    elif choice == "2":
        view_scores()

    elif choice == "3":
        print("Thank you for playing!")
        break

    else:
        print("Invalid choice!")