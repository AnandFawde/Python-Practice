# f = open("file.01","a")

# data = f.read()
# print(data)
# f.a()
# f.close()

# import os

# os.remove("file.01")

with open("file.01","w") as f:
    f.write("hi everyone\nwe are learning python\ni like programming in java")
    data = f.read()
data = data.replace("java","python")
print(data)