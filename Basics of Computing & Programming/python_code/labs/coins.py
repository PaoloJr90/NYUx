print("Please enter the amount of money to convert:")

dollars = int(input("# of dollars:"))
cents = int(input("# of cents:"))
tc = (dollars*100) + cents

q = 25
d = 10
n = 5
p = 1

quarters = int(tc // q)
quarters_2 = int(quarters * q)
dimes = int((tc - quarters_2)//d)
dimes_2 = int(dimes * d)
nickels = int((tc-dimes_2-quarters_2)//n)
nickels_2 = int(nickels * n)
pennies = int(tc-dimes_2-quarters_2-nickels_2)


print("the coins are", quarters,"quarters" + ",", dimes, "dimes" + ",", nickels, "nickels and", pennies, "pennies")