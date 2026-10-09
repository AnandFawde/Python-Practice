menu = {"pizza":300,
        "pasta":100,
        "ice creem":60,
        "potato":30}

cart = []
total = 0
print("---------MENU---------")
for key,value in menu.items():
    print(f"{key:12}:${value:.2f}")
print("----------------------")
print()
while True:
    food = input("Press your order (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)


print("-------YOUR ORDER---------")
for food in cart:
    total = total + menu.get(food)
    print(food,end=" ")
print()
print(f"Total is: ${total}")

        

