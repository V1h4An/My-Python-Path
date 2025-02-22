menu = {"Pizza":3.50,
        "Nachos":3.00,
        "Popcorn":5.00,
        "chips":1.00,
        "Fries":2.50,
        "Pretzel":3.50,
        "Soda":3.00}
print("----------MENU----------")
for key, value in menu.items():
    print(f"{key:10} : $ {value:.2f}")
print("------------------------")

cart = []
total = 0 

while True:
    food = input("select an item(q to quit):")
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("----------Your Order----------")
for food in cart:
    total += menu.get(food)
    print(food , end=" ")

print()
print(f"Total is : ${total:.2f}")
