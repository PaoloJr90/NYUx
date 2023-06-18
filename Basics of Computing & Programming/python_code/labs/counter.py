print("Please enter the number of coins:")

quarter = int(input("# of quarters:  "))
dime = int(input("# of dimes:  "))
nickel = int(input("# of nickels:  "))
penny = int(input("# of pennies:  "))

q = quarter*0.25
d = dime*0.10
n = nickel*0.05
p = penny*0.01
t = (q+d+n+p)*100
tf = int(t//100)
tr = int(t%100)

print("The total is", tf, "dollars and", tr,"cents")        