print("Enter an odd length string:")
line = input()
len = len(line)
mid = line[len//2]
first = line[0:len//2]
second = line[len//2 + 1: ]

print("Middle character: ",mid)
print("First half: ", first)
print("Second half: ", second)
