'''name = input("enter your name :")

while name == "":
    print("You did not enter your name")
    name = input("enter your name :")

print(f"hello {name}")

age = int(input("enter your age :"))

while age < 0:
    print("That is not possible")
    age = input("enter a valid number for an age")

print(f"You are {age} years old")

food = input("enter food you like:")

while not food == "q":
    print(f"you like {food}")
    food = input("enter another food you like(q to quit) :")

print("bye")
'''
num = int(input("enter a number between 1-10 :"))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("enter a number between 1-10 :"))

print(f"your number is :{num}")