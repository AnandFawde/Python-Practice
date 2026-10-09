questions = ("What the inertia of mass? :",
             "Whats the hottest celistial in solar system? :",
             "Whats the name of the largest trench? :",
              "The most reputable country in the world?:",
               "The biggest river in the world?: " )

options = (("A. MOMENT", "B. TORQUE", "C. OMEGA", "D. NONE" )
           ,("A. SATURN", "B. URANUS", "C. NEPTUNE", "D. VENUS" )
           ,("A. MARIANA", "B. PACIFIC", "C. ATLANTIC", "D. NONE" ),
           ("A. USA" , "B. GERMANY", "C. INDIA", "D. CHINA"),
           ("A. GANGA", "B. BLACK LAKE", "C. NILE", "D. NONE"))


answers = ("A" , "D" , "A" , "C" , "C")
guesses = []
q_options = 0   

score = 0
for question in questions:          
    print("--------------------")
    print(question)
    
    for option in options[q_options]:
        print(option)

    guess= input("Enter your Answer (A. B. C. D):").upper()
    guesses.append(guess)
    if guess==answers[q_options]:
        score = score + 20
        print("Correct Answer")

    elif guess not in ("A","B","C","D"):
            print("Invalid option")
    
    else:
        print("Incorrect Answer")
        print("Correct Answer is",q_options)
    q_options = q_options + 1

print("----------------------")
print("        RESULT        ")
print()
print("----------------------")

print("Your guesses: ",guesses)
print("Correct answers:  ",answers)

print("Your score will be: ",score)

if score >= 100:
    print("A")
elif score>=80:
    print("B")
elif score>=60:
    print("C")
elif score>=40:
    print("D")
elif score>=20:
    print("E")
else:
    print("F") 



    



