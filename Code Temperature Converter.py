#Author : Joshua-Mark Campbell
#Date : 10/18/24
#File : Code Temperature Converter.py

print("Welcome to my Super Amazing Code Temperature Converter")
fTemperature = float(input("What is the Temperature ")) #Had to make it a float in order to be able to do math
sConvert = input("Is the temperature in degrees Fahrenheit or Celsius? (ENTER 'F' FOR FAHRENHEIT OR 'C' FOR CELSIUS) ").upper() #Scott showed me a cool way of forcing an upppercase


if sConvert == "C": #Only if they give me C I go into my If statements
    if fTemperature > 100:
        print("Temp cant be more than 100")
    else:
        fFahrenheit = ((9.0/5.0)*fTemperature) + 32
        print(f"Your converted temperature is now {fFahrenheit:.1f} ") # .1f outside the colon to know where to set the decimal point

elif sConvert == "F": #Only if they give me F I go into my If statements
    if fTemperature > 212:
        print("Temp cant be more than 212")
    else:
        fCelsius = (5.0/9.0)*(fTemperature - 32)
        print(f"Your converted temperature is now {fCelsius:.1f} ") # .1f outside the colon to know where to set the decimal point

else:
    print("YOU NEED TO ANSWER EITHER 'F' OR 'C' ") #I am telling them that they did not give me the correct answer!!
input("Press ENTER to close Program") #Input for exit to program SCOTT WITH THE TIPS MAN!!!