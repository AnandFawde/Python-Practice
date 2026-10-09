import time

my_time = int(input("Enter the time in seconds: "))

for i in range(my_time,0,-1):
     second = i%60                                #the remaning
     minutes = int((i/60))%60
     hour = int((i/3600))%24                      #i is in seconds

     print(f"{hour:02}:{minutes:02}:{second:02}") #format f is nessesory 
     time.sleep(1)                                

print("TIME'S UP!")