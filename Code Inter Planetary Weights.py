# Author : Joshua-Mark Campbell
# Date : 10/07/24
# File : Code Inter Planetary Weights.py

#Constants -
fMERCURY_WEIGHT = 0.38
fVENUS_WEIGHT = 0.91
fPLUTO_WEIGHT = 0.063
fMOON_WEIGHT = 0.165
fJUPITER_WEIGHT = 2.4
fSATURN_WEIGHT = 0.93
fNEPTUNE_WEIGHT =1.12
fURANUS_WEIGHT = 0.92

sName = input("What is your name")
fWeight = float(input('What is your weight?'))

print(f"Hello {sName}, your weight on Earth is {fWeight}. Here's your weight on other planets:")
print(f"{"Mercury:":14s} {fWeight * fMERCURY_WEIGHT:12.2f}")
print(f"{"Venus:":14s} {fWeight * fVENUS_WEIGHT:12.2f}")
print(f"{"Pluto:":14s} {fWeight * fPLUTO_WEIGHT:12.2f}")
print(f"{"Moon:":14s} {fWeight * fMOON_WEIGHT:12.2f}")
print(f"{"Jupiter:":14s} {fWeight * fJUPITER_WEIGHT:12.2f}")
print(f"{"Saturn:":14s} {fWeight * fSATURN_WEIGHT:12.2f}")
print(f"{"Neptune:":14s} {fWeight * fNEPTUNE_WEIGHT:12.2f}")
print(f"{"Uranus:":14s} {fWeight * fURANUS_WEIGHT:12.2f}")