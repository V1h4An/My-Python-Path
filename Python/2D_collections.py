#list= [list1,list2,list3]

fruits = ["apple","orange","banana","coconut"]
vegetables = ["celery","carrots","potato"]
meats = ["chicken","fish","turkey"]

groceries =[fruits,vegetables,meats]

#print(groceries)    #prints individual list seperated with commas (1D)
#print(groceries[0]) #prints the whole list "fruits"
#print(groceries[1]) #prints the whole list "vegetables"
#print(groceries[2]) #prints the whole list "meats"

#print(groceries[0][0])  # prints element at idex 0 of the sublist(fruit)
                        # at index 0 of main list(groceries) apple

#print(groceries[1][0])  # prints element at idex 0 of the sublist(vegetables)
                        # at index 1 of main list(groceries) celery

#print(groceries[2][0])  # prints element at idex 0 of the sublist(meats)
                        # at index 2 of main list(groceries) chicken

#can also be declared as 
groceries = [["apple","orange","banana","coconut"],
             ["celery","carrots","potato"],
             ["chicken","fish","turkey"]]

for row in groceries:
    for food in row:
        print(food, end= " ")
    print()
