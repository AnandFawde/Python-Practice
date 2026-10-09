"""
BEGINNER Python Quiz Game
--------------------------
This version is kept as simple as possible.
Concepts used: variables, strings, lists, tuples, if/elif/else, and a for loop.
Every step is explained with comments.
"""

# STEP 1: Store our questions.
# Each question is a "tuple" -> a small fixed group of 3 things:
#   1) the question text
#   2) a list of 4 possible answers
#   3) the number of the correct answer (1, 2, 3, or 4)

question_1 = ("What color do you get by mixing blue and yellow?",
              ["Red", "Green", "Purple", "Orange"],
              2)

question_2 = ("How many days are there in a week?",
              ["5", "6", "7", "8"],
              3)

question_3 = ("What is the capital city of France?",
              ["London", "Paris", "Rome", "Berlin"],
              2)

question_4 = ("Which animal is known as the 'King of the Jungle'?",
              ["Tiger", "Elephant", "Lion", "Bear"],
              3)

question_5 = ("What do bees make?",
              ["Milk", "Honey", "Silk", "Butter"],
              2)

# STEP 2: Put all the questions together in one list, so we can loop through them.
all_questions = [question_1, question_2, question_3, question_4, question_5]

# STEP 3: Set up a score counter, starting at zero.
score = 0

# A simple counter to show "Question 1", "Question 2", etc.
question_number = 1

print("Welcome to the Beginner Quiz!")
print("Type 1, 2, 3, or 4 to answer each question.")
print("")

# STEP 4: Go through every question one at a time.
for question in all_questions:

    # Each question tuple has 3 parts, so we can "unpack" it into 3 variables:
    question_text = question[0]
    answer_choices = question[1]
    correct_answer = question[2]

    # Show the question
    print("Question", question_number, ":", question_text)

    # Show the 4 answer choices
    print("1.", answer_choices[0])
    print("2.", answer_choices[1])
    print("3.", answer_choices[2])
    print("4.", answer_choices[3])

    # Ask the player to type their answer
    player_answer = input("Your answer: ")

    # Check the answer.
    # We compare it as text first, then turn it into a number to check.
    if player_answer == "1" or player_answer == "2" or player_answer == "3" or player_answer == "4":

        player_answer_number = int(player_answer)

        if player_answer_number == correct_answer:
            print("That's correct!")
            score = score + 1
        else:
            print("That's not right. The correct answer was option", correct_answer)

    else:
        print("That wasn't a valid choice (please type 1-4 next time).")

    print("")  # blank line for spacing
    question_number = question_number + 1

# STEP 5: Show the final score once all questions are done.
print("You finished the quiz!")
print("Your final score is:", score, "out of", len(all_questions))
