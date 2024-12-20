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



def getMedian(real_estate_list,length_of_list):
    divide_list = length_of_list // 2
    if length_of_list % 2 == 0:
        return (real_estate_list[divide_list] + real_estate_list[divide_list - 1]) / 2
    else:
        return real_estate_list[divide_list]


def main():
    real_estate_list = []

    while True:
        sales_value = getFloatInput("Enter property sales value: ")
        real_estate_list.append(sales_value)
        while True:
            yes_or_no = input("Enter another property sales value 'Y' or 'N': ").upper()
            if yes_or_no == "Y" or yes_or_no == "N":
                break

        if yes_or_no == "N":
            break

    real_estate_list.sort()

    length_of_list = len(real_estate_list)
    sum_of_list = sum(real_estate_list)
    for iIndexFor in range(0, length_of_list):
        print(f"Property {iIndexFor + 1} is ${real_estate_list[iIndexFor]}")


    print(f"{"Minimum:":12s}{"$":8s}{min(real_estate_list):,.2f}")
    print(f"{"Maximum:":12s}{"$":8s}{max(real_estate_list):,.2f}")
    print(f"{"Total:":12s}{"$":8s}{sum_of_list:,.2f}")
    print(f"{"Average:":12s}{"$":8s}{sum_of_list / length_of_list:,.2f}")
    print(f"{"Median:":12s}{"$":8s}{getMedian(real_estate_list,length_of_list) :,.2f}")
    print(f"{"Commission:":12s}{"$":8s}{sum_of_list * 0.03:,.2f}")

main()
