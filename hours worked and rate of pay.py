#Jess Howard
#6/10/14
#class exercises
#Write a program that asks the user for the number of hours worked this week and their hourly rate of pay. The program is to calculate the gross pay
#If the number of hours worked is greater than 40, the extra hours are paid at 1.5 times the rate. The program should display an error message if the number of hours worked is not in the range 0 to 60.

hours= int(input("How many hours did you work this week?:"))
pay= int(input("How much do you get payed an hour?:"))
answer= hours*pay
if hours>40:
 answer= hours*(pay*1.5)
print("You have earned £{0} this week!".format(answer))
