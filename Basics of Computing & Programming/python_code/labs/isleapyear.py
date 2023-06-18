#print("Enter a year:")
#mybirthyear = int(input())

def isleapyear(mybirthyear):
    if ((mybirthyear % 400) == 0) and (mybirthyear % 100 == 0):
        #print(mybirthyear, "is a leap year")
        return True
    elif (mybirthyear % 4 == 0) and (mybirthyear % 100 != 0):
           #print(mybirthyear, "is not a leap year")
           return True
    else:
        #print(mybirthyear, "is not leap year")
        return False

#isleapyear()