foods = []
prices = []
total = 0

while True:
    food = input("what item would you like to buy (q to quit) :")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"enter the price of {food} : $"))
        foods.append(food)
        prices.append(price)
print("-----Your cart-----")
for food in foods:
    print(food,end = " ")
print()
for price in prices:
    total += price
print(f"The Total is : ${total:.2f}")