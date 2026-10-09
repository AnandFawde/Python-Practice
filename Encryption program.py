import random
import string

char = " " + string.punctuation + string.digits + string.ascii_letters

char = list(char)
key = char.copy()
#print()
#print(char)
#print(key)

random.shuffle(key)
#print(key)

user_input = input("Enter a message to Encrypt: ")
cyper_text = ""
for letter in user_input:
    index = char.index(letter)
    cyper_text += key[index]

print(f"The original message :{user_input}")
print(f"The cryptic message :{cyper_text}")

cyper_text = input("Enter the Cyper text: ") 
user_input = "" 
for letter in cyper_text:
    index = key.index(letter)
    user_input += char[index]

print(f"The cryptic message :{cyper_text}")
print(f"The original message :{user_input}")                                                       


