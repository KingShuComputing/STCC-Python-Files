principle = 0
rate = 0
time = 0
compounding = 0

while principle <= 0:
    principle = float(input("Enter the principle amount"))
    if principle <= 0:
        print("Principle can't be less than or equal to zero")

while rate <= 0:
    rate = float(input("Enter the Interest Rate"))
    if rate <= 0:
        print("Interest rate can't be less than or equal to zero")

while time <= 0:
    time = float(input("Enter the time in years"))
    if time <= 0:
        print("Time cant be less than or equal to zero")

while compounding <= 0:
    compounding = float(input("Enter the compounding "))
    if compounding <= 0:
        print("Time cant be less than or equal to zero")


print(principle)
print(rate)
print(time)
print(compounding)

total = principle * pow((1 + rate / compounding), time)
print(f"Balance after {time} years/s: ${total:.2f}")




