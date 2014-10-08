#08/10/2014
#Jess Howard
#development exercises
#write a program that reads in the temperature of water in a container(in centigrade and displays a message stating whether the water os frozen,boiling or neither.

temp= int(input(" Please enter the water temprature in the unit of centigrade:"))
if temp<= 0:
   print(" Your water is currently frozen")
elif temp >=100:
   print("Your water is currently boiling")
else:
    print("Your water is niether froezen or boiling")

