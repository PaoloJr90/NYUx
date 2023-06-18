day = input("Enter the day the call started at:")
time = input("Enter the time the call started at (hhmm):")
dur = int(input ("Enter the duration of the call (in minutes):"))


if(day in ["Mon", "Tue", "Wed", "Thr", "Fri"] and("0800" <= time <= "1800")):
    cost = dur * 0.40
elif(day in ["Mon", "Tue", "Wed", "Thr", "Fri"] and(time > "1800" or time < "0800")):
    cost = dur * 0.25
else:
    cost = dur * 0.15

txt = "This call will cost ${:.2f}"
print(txt.format(cost))