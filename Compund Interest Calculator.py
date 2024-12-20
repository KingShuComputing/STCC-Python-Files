iprincipal_Investment = float(input('Enter the starting Principal'))
iInterest_Rate = float(input('What is the annual Interest Rate?'))
iCompounding = float(input('How many times per year is the interest compounded?'))
iNumber_of_Periods = float(input('For how many years will the account earn interest?'))

while iprincipal_Investment <= 0:
    principle = float(input("Enter the principle amount:"))
    if principle <= 0:
        print("Principle cant be less than or equal to 0")

while iInterest_Rate <= 0:
    principle = float(input("Enter the principle amount:"))
    if principle <= 0:
        print("Principle cant be less than or equal to 0")