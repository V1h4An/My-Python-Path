num1 =float(input("enter first number: "))
num2 =float(input("enter second number: "))
operator=input("enter operator to use(+,-,*,/,^): ")

if operator == '+':
    result = num1+num2
    print (round(result,2))
elif operator == '-':
    result = num1-num2
    print(round(result,2))
elif operator == '*':
    result = num1*num2
    print(round(result,2))
elif operator == '/':
    result = num1/num2
    print(round(result,2))
else:
    print("not a valid operator")