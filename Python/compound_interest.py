principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("enter a principle amount:"))
    if principle <= 0:
        print("principle should be greater than 0")

while rate <= 0:
    rate = float(input("enter interest rate amount:"))
    if rate <= 0:
        print("rate should be greater than 0")

while time <= 0:
    time = int(input("enter the maturity time in years:"))
    if time <= 0:
        print("time should be greater than 0")

print(f"principle is :{principle}")
print(f"interest rate is :{rate}")
print(f"maturity time is :{time}")

Final = principle * pow((1 + rate/100),time)

print(f"balance after {time} years :${Final:.2f}")