#validate user input
#username should not be more than 12 char
#should not have numbers
#should not contain spaces

username = input("enter your usename :")

if len(username) > 12:
    print("Your username should be only 12 char long")

elif not username.find(" ") ==-1:
    print("Your username should not contain spaces")

elif not username.isalpha() :
    print("Your username should only contain alphabets")
     
else :
    print(f"welcome {username}")