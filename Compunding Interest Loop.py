"""
Code Compound Interest Loops Instructions

1.
    Code a loop to enter your deposit
    This is going to be a float and it must be positive!

2.
    Code a loop to enter your interest rate
    This is going to be a float and it must be positive!

    You will need to divide this twice.
    Once by 100 to move the decimal place, and again by 12 to get the monthly interest rate.

3.
    Code a loop to enter your number of months
    This is going to be an int and it must be positive!

4.
    Code a loop to enter your goal amount
    This is going to be a float and it must be positive, though it CAN be zero!
5.
    Code another loop to print out a monthly report of your compounded interest up to your number of months variable.
    This can be either a while or for loop.

    Inside of this loop you will need to multiply your deposit by your monthly interest rate
    and add the result back onto your deposit.

    Also inside of the loop you will need to write a print statement that states the current month
    and the amount you've currently earned for that month.
6.
    Code one more loop that will go up to your goal amount.
    Because you don't know how many times you will need to loop, you will have to do this using a while.

    Inside of this loop, you will be doing the exact same math that you did for the loop in step 5.

    You will need to create a month counter that keeps track of how many times you looped through
    to determine the number of months that passed until you reached your goal.

    OUTSIDE of this loop, you will write a print statement which will state how many months it took to reach your goal.
    (HINT: Make sure to add the number of months variable onto this counter once you've finished this loop!)
Sample for inputs w/o goal :

Deposit = 1000
IntRate = 4.5
NumOfMonths = 12
Goal = 0

Output should be:

Month 1:               Account balance is:  $ 1,003.75
Month 2:               Account balance is:  $ 1,007.51
Month 3:               Account balance is:  $ 1,011.29
Month 4:               Account balance is:  $ 1,015.08
Month 5:               Account balance is:  $ 1,018.89
Month 6:               Account balance is:  $ 1,022.71
Month 7:               Account balance is:  $ 1,026.55
Month 8:               Account balance is:  $ 1,030.40
Month 9:               Account balance is:  $ 1,034.26
Month 10:              Account balance is:  $ 1,038.14
Month 11:              Account balance is:  $ 1,042.03
Month 12:              Account balance is:  $ 1,045.94

--------------------------------------------------------

Sample for inputs with goal :

Deposit = 1000
IntRate = 4.5
NumOfMonths = 12
Goal = 1200

Output should be:

Month 1:               Account balance is:  $ 1,003.75
Month 2:               Account balance is:  $ 1,007.51
Month 3:               Account balance is:  $ 1,011.29
Month 4:               Account balance is:  $ 1,015.08
Month 5:               Account balance is:  $ 1,018.89
Month 6:               Account balance is:  $ 1,022.71
Month 7:               Account balance is:  $ 1,026.55
Month 8:               Account balance is:  $ 1,030.40
Month 9:               Account balance is:  $ 1,034.26
Month 10:              Account balance is:  $ 1,038.14
Month 11:              Account balance is:  $ 1,042.03
Month 12:              Account balance is:  $ 1,045.94

It will take 49 months to reach $ 1,200.00.
"""

while True:
    try:
        iNum = int(input("enter a number: "))

        if iNum < 0:
            raise ValueError

        else:
            break

    except ValueError:
        print("You need to enter something numeric and it must be positive!")