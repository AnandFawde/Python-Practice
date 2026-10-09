while True :
    principle = float(input("Enter the principle amount: "))
    if (principle<0):
        print("Principle can't be negetive")
        print("kindly enter the correct principle")
    else:
        break
while True :
    rate = float(input("Enter the rate: "))
    if (rate<0):
        print("rate can't be negetive")
        print("kindly enter the correct rate")
    else:
        break
while True :
    time = float(input("Enter the time: "))
    if (time<1):
        print("time can't be negetive")
        print("kindly enter the correct time")
    else:
        break
while True :
    num = float(input("Enter the number of times rate is compounded: "))
    if (num<1):
        print("time can't be negetive")
        print("kindly enter the correct number")
    else:
        break                                        
# while True :                                          
#     if

Total = round(principle*pow((1+rate/num),time*num),2)

print("The total compound interest will be",Total)