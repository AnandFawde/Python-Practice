

# Each question is a tuple: (question_text, options_tuple, correct_answer_index)
questions = [
    ("What does CPU stand for?",
     ("Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Central Processor Utility"),
     1),
    ("Which keyword is used to create a loop that repeats a fixed number of times in Python?",
     ("while", "loop", "for", "repeat"),
     2),
    ("Which data type is immutable (cannot be changed) in Python?",
     ("list", "dict", "tuple", "set"),
     2),
    ("What is the output of len('hello')?",
     ("4", "5", "6", "Error"),
     1),
    ("Which symbol is used for a single-line comment in Python?",
     ("//", "#", "<!-- -->", "/* */"),
     1),
    ("What will [1, 2, 3] + [4, 5] give in Python?",
     ("[1, 2, 3, 4, 5]", "[5, 7, 8]", "Error", "[1, 2, 3, [4, 5]]"),
     0),
    ("Which of these creates an empty tuple?",
     ("()", "[]", "{}", "tuple[]"),
     0),
    ("What does the 'in' keyword check for in a list?",
     ("The index of an item", "If an item exists in the list", "The length of the list", "Nothing, it's not valid"),
     1),
]

score = 0
total = len(questions)

print("=" * 40)
print("       WELCOME TO THE PYTHON QUIZ")
print("=" * 40)
print("Answer each question by typing 1, 2, 3, or 4.\n")

question_number = 0

for question in questions:
    question_number = question_number + 1
    text = question[0]
    options = question[1]
    correct_index = question[2]

    print(f"Q{question_number}: {text}")

    option_number = 1
    for option in options:
        print(f"  {option_number}. {option}")
        option_number = option_number + 1

    user_answer = input("Your answer: ")

    # Validate input and convert to index
    if user_answer == "1" or user_answer == "2" or user_answer == "3" or user_answer == "4":
        user_index = int(user_answer) - 1

        if user_index == correct_index:
            print("Correct!\n")
            score = score + 1
        else:
            correct_option = options[correct_index]
            print(f"Wrong. The correct answer was: {correct_option}\n")
    else:
        print("Invalid input, skipping this question.\n")

# Final results
print("=" * 40)
print("QUIZ COMPLETE")
print("=" * 40)
print(f"Your score: {score} out of {total}")

percentage = (score / total) * 100
print(f"Percentage: {percentage:.1f}%")

if percentage == 100:
    print("Perfect score! Amazing work.")
elif percentage >= 75:
    print("Great job! You know your stuff.")
elif percentage >= 50:
    print("Not bad, but there's room to improve.")
else:
    print("Keep practicing, you'll get there!")
