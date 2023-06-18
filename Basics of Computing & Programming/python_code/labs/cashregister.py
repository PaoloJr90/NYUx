first = float(input("Enter price of the first item: "))
second = float(input("Enter price of the second item: "))
club = str(input("Does customer have a club card? (Y/N): "))
tax = float(input("Enter tax rate, e.g. 5.5 for 5.5% tax: "))
tpbase = first + second

# first vs. second pricing
if(first < second):
    first = first * 0.5
elif(second < first):
    second = second * 0.5
elif(first == second):
    first = first * 0.5
else:
    tp = first + second

# club card pricing (cp) if applicable
if(club == "Y"):
    tp = (first + second) * (1 - 0.10) 
elif(club == "y"):
   tp = (first + second) * (1 - 0.10)   
else:  
    tp = first + second

# sales tax
if(tax == 0):
    tptax = round(tp * (1 + (tax/100)),2)
else:
    tptax = round(tp * (1 + (tax/100)),2)


txtbase = "Base Price = {:.2f}"
print(txtbase.format(tpbase))
txtdisc = "Price after discounts = {:.2f}"
print(txtdisc.format(tp))
txttp = "Total Price = {:.2f}"
print(txttp.format(tptax))
