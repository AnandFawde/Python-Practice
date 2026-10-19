# MultiThreading --> perform multipule tasks concerently
#                    threading.Thread(target = )

import threading
import time


def work_out(type):
    time.sleep(10)
    print(f"You Have Completed Your {type} Workout")

def pay_bills(bills):
    time.sleep(4)
    print(f"Finished paying the {bills} bills")

def git_pull(code):
    time.sleep(2)
    print(f"Posted your {code} code")

task1 = threading.Thread(target=work_out, args = ("Chest",))
task1.start()

task2 = threading.Thread(target=pay_bills , args = ("internet",))
task2.start()

task3 = threading.Thread(target=git_pull , args = ("threading",))
task3.start()

task1.join()
task2.join()
task3.join()

print("------------GOOD JOB------------")
print("-------All Tasks Completed--------")