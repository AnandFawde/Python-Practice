item = []
prices = []
total = 0
while True:
    item_new = input("Enter the item you want to buy (Press q to quit): ")

    if item_new.lower()=="q":
        break
    else:
        item.append(item_new)
        prices_of = int(input("Enter the prise of the item: "))
        prices.append(prices_of)
for i in prices:
    total = total + i
    

print("-----YOUR CART-----" )
print(item , end = " ")
print()
print("YOUR TOTAL WILL BE :",total , end = " ")