sName = input("what is your name?")
sAge = input("What is your age?")
sRAce = input('What is your racial association')
sOccupation = input('What is your current occupation')
sAddress = input("What is your address")
sSocial = input("What is your Social")

iAge = int(sAge)


print(sName, type(sName))
print(sAge, type(sAge))
print(iAge, type(iAge))
print(sSocial, type (sSocial))
print(sAddress, type(sAddress))
print(sRAce, type(sRAce))

print(sName,'Racial Association is', sRAce)
print(sName,'Currently works as a', sOccupation)
print(sName,"currently resides at", sAddress)

iYears_to_the_Retirement = 70 - iAge

print(sName, "you can retire in", iYears_to_the_Retirement,'years')
print(sName, 'you have a decent amount of time in the workforce left, we appreciate all of your hardwork')
sfeedback = input(
    'My Creator has worked very hard on my code and put a lot of time into refining my responses and my way of thinking,Do you think he has done well?'
                )
print('Thank you for your feedback hope to type with you again, hopefully I learn more about you the next time we chat!! ˶ᵔ ᵕ ᵔ˶ ')
if sfeedback =="Yes" or sfeedback== "Y" or sfeedback== "yes":
    print('I appreciate your kind words young sir/maam i look forward to typing with you in the future agin sometime soon.')

else:
    print("I am greatly offended at such a remark My Creator ahs put his sweat and absolute tears into my code and thats what you reply with, uh Despicable!!!")



iFuture_Value = float(iprincipal_Investment*(1+iCompounding//iInterest_Rate) **(iCompounding*iNumber_of_Periods))

iFuture_Value =iprincipal_Investment * pow((1 + iInterest_Rate/iCompounding), iNumber_of_Periods*iCompounding)

Rubber DUCK METHOD = talk to something and see if it makes sense
