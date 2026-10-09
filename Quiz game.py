question1 = ("What is the largest animal in the world",
             ["Tiger" , "Elephant", "Whale", "Giraffe"],
              4)
question2  = ("Whats the formula for force",                                          
             ["ma", "pa", "mc", "bc"],
              1)
question3  = ("Whats radius times length",                                          
             ["Mass", "Force", "Torque", "None"],
              3)
question4  = ("Whats MLT",                                          
             ["Moment", "Moment of inertia", "side" , "Paskal"],
              2)

questions = [question1,question2,question3,question4]

score = 0 

for question in questions:
    print(question[0])
    print(question[1])
   
    correct_answer = question[2]
    guess = int(input("Enter 1. 2. 3. 4. : "))
    if guess == correct_answer:
        print("correct answer ")
    else:
        print("Wrong answer")
     
