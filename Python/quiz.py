questions = ("How many elements are in the periodic table? :",
             "Which animal lays the largest egg? :",
             "What is the most abundant gas in Earth's Atmosphere? :",
             "How many Bones are in the Human Body? :",
             "What is the Hottest Planet in the Solar System? :")

options = (("116","117","118","119"),
           ("Whale","Crocodile","Elephant","Ostrich"),
           ("Nitrogen","Oxygen","Hydrogen","C02"),
           ("205","206","204","200"),
           ("Earth","Venus","Mercury","Mars"))

answers = ("118","Ostrich","Nitrogen","206","Venus")

question_no = 0

score = 0

guesses = []

for question in questions:
    print("------------------------------------")    
    print(question)
    for option in options[question_no]:
        print(option)
    guess = input("Enter answer: ").lower()
    guesses.append(guess)
    if guess.capitalize() in answers:
        print("Correct answer")
        score +=1
    else:
        print("Wrong answer")
    question_no += 1

print(score)

for guess in guesses:
    print("----------------------")
    print(guess)