print("Please enter a time in a 24-hour format:")
hour24 = int(input("Hour: "))
minutes24 = int(input("Minutes: "))

minutes12 = minutes24
if(0 <= hour24 <= 11):
    period = "am"
    if(hour24 == 0):
        hour12 = 12
    else:
        hour12 = hour24
else:
    period = "pm"
    if(hour24 == 12):
        hour12 = 12
    else:
        hour12 = hour24 - 12

print(hour24, ":", minutes24, "is", hour12, ":", minutes12, period, sep = "")