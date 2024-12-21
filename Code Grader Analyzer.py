from ctypes import c_int

sName = input("What is your name?: ")
test_score1 = int(input("What is the first test score?: "))
test_score2 = int(input("What is the second test score?: "))
test_score3 = int(input("What is the third test score?: "))
test_score4 = int(input("What is the fourth test score?: "))

if test_score1 < 0 or test_score2 < 0 or test_score3 < 0 or test_score4 < 0:
    exit("Test scores should be greater than 0 ")

drop_lowest = input("Enter 'Y' or 'N' to Drop the lowest Grade: ").upper()

if drop_lowest != "Y" and drop_lowest != "N":
    exit("Please Enter 'Y' or 'N' to Drop the lowest Grade. ")

if drop_lowest == "Y":
    if test_score1 <= test_score2 and test_score1 <= test_score3 and test_score1 <= test_score4:
        lowest_score = test_score1
    elif test_score2 <= test_score3 and test_score2 <= test_score4:
        lowest_score = test_score2
    elif test_score3 <= test_score4:
        lowest_score = test_score3
    else:
        lowest_score = test_score4

    divisor = 3

else:
    lowest_score = 0
    divisor = 4

average = (test_score1 + test_score2 + test_score3 + test_score4 - lowest_score) / divisor

#Joseph Harris taught me this trick btw
if average >= 90:
    letter = "A"
elif average >= 80:
    letter = "B"
elif average >= 70:
    letter = "C"
elif average >= 60:
    letter = "D"
else:
    letter = "F"

if average % 10 >= 7:
    letter += "+"
elif average % 10 <= 3.9:
    letter += "-"

print(f"Hello {sName} your average is {average:.1f}, which is a(n) {letter}")
