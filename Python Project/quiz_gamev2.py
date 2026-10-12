#=================================
# Quiz game version 2.0
# language: Python
#==================================
import random

questions = [
    {
      "question":"what's the correct extension for python files?",
      "options":[".py",".python",".pyt",".pt"],
        "answer":".py"
    },
    {
      "question":"what is the correct syntax to output 'Hello World' in python?",
      "options":["echo('Hello World')","print('Hello World')","p('Hello World')","printf('Hello World')"],
        "answer":"print('Hello World')"
    },
    {
      "question":"How do you insert COMMENTS in python code?",
      "options":["//This is a comment","/*This is a comment*/","#This is a comment","<!--This is a comment-->"],
        "answer":"#This is a comment"
    },
    {
      "question":"Which one is NOT a legal variable name?",
      "options":["my-var","my_var","_myvar","myvar"],
        "answer":"my-var"
    },
    {
      "question":"What is the correct file mode for reading in binary?",
      "options":["r+b","rb+","br+","b+r"],
        "answer":"rb+"
    }
]

while True:
  print("=====================Welcome to the Quiz Game!========================")
  print("1. Start Quiz")
  print("2. Exit")

  choice = input("Enter your choice (1 or 2): ")
  if choice == "1":
    score = 0
    questions = questions.copy()  
    random.shuffle(questions)

    for q in questions:
        print("\n" + q["question"])
        for i, option in enumerate(q["options"], start=1):
            print(f"{i}. {option}")
        try:
            answer = input("Enter the number of your answer: ")
            if q["options"][int(answer) - 1] == q["answer"]:
              print("Correct!")
              score += 1
            else:
              print(f"Wrong! The correct answer is: {q['answer']}")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number corresponding to the options.")
            
    print(f"\nYour final score is: {score}/{len(questions)}")
  elif choice == "2":
    print("Thank you for playing! Goodbye!")
    break
  else:
    print("Invalid choice. Please enter 1 or 2.")