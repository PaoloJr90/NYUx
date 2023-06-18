print("Please enter an integer:")
user_input = int(input())

abs_value = user_input
if(user_input < 0):
    abs_value = user_input * (-1)

print("|", user_input, "| = ", abs_value, sep="")   