operator=input("Enter the operator from +,-,*,/: ")

num1=int(input("Enter the 1st no: " ))
num2=int(input("Enter the 2nd no: "))

if operator=="+":
   result=num1+num2
   print(result)
elif operator=="-":
    result=num1-num2
    print(result)
elif operator=="*":
    result=num1*num2
    print(result)
elif operator=="/":
    
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        result=num1/num2
    print(result)
else :
    print("Invalid operator used")   
    
