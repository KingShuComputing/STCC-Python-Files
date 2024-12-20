"""
Comparison Operators

<       Less than
<=      Less than or equal to

>       Greater than
>=      Greater than or equal to

==      Equal to
!=      Not equal to
"""
#from INteger import sName

"""
Grade Analyzer Instructions

1. 
    Code a variable to take in your name.

2. 
    Code 4 variables that take in 4 grades and convert each to ints.

3.
    Using an if-statement(s), ensure that each grade entered is positive (at least 0).

4.
    Code a variable that prompts for whether the user wishes to drop the lowest grade.
    This will take in either "Y" or "N" for yes or no.
5.
    Using if-statements, code three possible paths for the program to take.

        A.
            If the user types in "Y", determine the lowest grade and then find the average.
            You can find the average by adding all the grades together, subtracting the lowest grade, and then dividing by 3.

        B.
            If the user types in "N", just determine the average.
            You would do this by adding all the grades together and then dividing by 4.  

        C.
            If the user types in anything else, print to the console that the user must enter "Y" or "N" and then exit the program.
6. 
    Using if-statements, determine the letter grade based off of the average acquired from step 5.    

    These are the following ranges for each letter grade:
        97 and Above - A+
        Between 96.9 and 94 - A
        Between 93.9 and 90 - A-

        Between 89.9 and 87 - B+
        Between 86.9 and 84 - B
        Between 83.9 and 80 - B-

        Between 79.9 and 77 - C+
        Between 76.9 and 74 - C
        Between 73.9 and 70 - C-

        Between 69.9 and 67 - D+
        Between 66.9 and 64 - D
        Between 63.9 and 60 - D-    

        Below 60 - F

7.
    Output the average and the appropriate letter grade to the console.
"""


sName = input("What is your name?")

igrade1 = int(input("Enter grade1: "))
if igrade1 < 0:
    print("We need a Positive Number")
elif igrade1 == 0:
    print("Zero")
else:
    print()
igrade2 = int(input("Enter grade2: "))
igrade3 = int(input("Enter grade3: "))
igrade4 = int(input("Enter grade4: "))

sFindlowest = input("Do you want to find the lowest number? Y/N ").upper()

if sFindlowest == "Y":
    if igrade1 < igrade2 and igrade1 < igrade3 and igrade1 < igrade4:
        ilowest = igrade1

    elif igrade2 < igrade3 and igrade2 < igrade4:
        ilowest = igrade2

    elif igrade3 < igrade4:
        ilowest = igrade3

    else:
        ilowest = igrade4

    print(f"Lowest number is {ilowest}")

scutthelowest = input("Do you want to cut the lowest number? Y/N ").upper()

if scutthelowest == "Y":
    sAverage = print( "The average without the lower grades is", (igrade1 + igrade2 + igrade3 + igrade4 -ilowest)//3)

elif sFindlowest == "N":
    sAverage = print("You've chosen not to cut the lowest number!", (igrade1 + igrade2 + igrade3 + igrade4)//4)
else:
    print("You must enter Y or N.")

sgradeletter = int(input("Enter your Grade Average"))

if sgradeletter >= 90
    print("Your grade is an A+")