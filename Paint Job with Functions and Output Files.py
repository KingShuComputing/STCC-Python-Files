import math
from fileinput import filename


def getFloatInput(string):
    """This function recieves a string and returns it as a float"""
    while True:
        try:
            float_value = float(input(string))
            if float_value <= 0:
                print("You have to enter a positive number! ")
            else:
                return float_value
        except ValueError:
            print("Invalid Input. Make sure it is a number")


def getGallonsOfPaint(square_feet_of_wall,feet_per_gallon):
    return int(math.ceil(square_feet_of_wall/feet_per_gallon))



def getLaborHours(labor_hours_per_gallons, total_gallons):
    return labor_hours_per_gallons * total_gallons

def getLaborCost(labor_hours_per_gallons, labor_charge_per_hour):
    return labor_hours_per_gallons * labor_charge_per_hour

def getPaintCost(total_gallons, paint_price):
    return total_gallons * paint_price


def getSalesTax(job_state):
    if job_state == "CT" or job_state == "VT":
        state_tax = 0.06
    elif job_state == "MA":
        state_tax = 0.0625
    elif job_state == "ME":
        state_tax = 0.085
    elif job_state == "RI":
        state_tax = 0.07
    else:
        state_tax = 0.0
    return state_tax

def showCostEstimate(gallons_of_paint, labor_hours, paint_cost, labor_cost, sales_tax, last_name):
    total_labor_cost = labor_cost * gallons_of_paint
    total_sales_tax = (total_labor_cost + paint_cost) * sales_tax
    total_cost = total_labor_cost + total_sales_tax + paint_cost

    print(f"Gallons of Paint: ${gallons_of_paint}")
    print(f"Hours of Labor: {labor_hours}")
    print(f"Paint Charges: ${paint_cost:,.2f}")
    print(f"Labor Charges: ${total_labor_cost:,.2f}")
    print(f"Tax: ${total_sales_tax:,.2f}")
    print(f"Total Cost: ${total_cost:,.2f}")

    with open(f"{last_name}_PaintJobOutput.txt", "w") as file:
        file.write(f"Gallons of Paint: {gallons_of_paint}\n")
        file.write(f"Hours of Labor: {labor_hours}\n")
        file.write(f"Paint Charges: ${paint_cost:,.2f}\n")
        file.write(f"Labor Charges: ${total_labor_cost:,.2f}\n")
        file.write(f"Tax: ${total_sales_tax:,.2f}\n")
        file.write(f"Total Cost: ${total_cost:,.2f}\n")

    print(f"{last_name}_PaintJobOutput.txt was created.")

def main():
    square_feet_of_wall = getFloatInput("Enter Square feet of the wall: ")
    paint_price = getFloatInput("Enter Paint Price: ")
    feet_per_gallon = getFloatInput("Enter Feet per Gallons: ")
    labor_hours_per_gallon = getFloatInput("Enter Labor Hours per gallon: ")
    labor_charge_per_hour = getFloatInput("Enter Labor charge per hour: ")
    job_state = input("What State is the job located in? ").upper()
    last_name = input("What is Your Last Name ")

    total_gallons = getGallonsOfPaint(square_feet_of_wall,feet_per_gallon)
    showCostEstimate(
        total_gallons,
        getLaborHours(labor_hours_per_gallon, total_gallons),
        getPaintCost(total_gallons, paint_price),
        getLaborCost(labor_hours_per_gallon, labor_charge_per_hour),
        getSalesTax(job_state),
        last_name)

main()