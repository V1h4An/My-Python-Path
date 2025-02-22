credit_number = "1234-5678-9012-3456"

print(credit_number[0])
print(credit_number[0:4])   # alsow written as print(credir_number[:4])
                            # default starting index is 0
# LHS of : is inclusive 
# RHS of : is exclusive
print(credit_number[5:])    # prints 5th element onwards
print(credit_number[::2])   # prints every second character of the string
print(credit_number[-1])    # prints last element

last_digits = credit_number[-4:]
print(f"xxxx-xxxx-xxxx-{last_digits}")

reverse = credit_number[::-1]
print(f"reverse credit_number is: {reverse}")