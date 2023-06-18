print("Enter a character:")
char = input()



if (type(char)==str) and char.isupper() == True:
    print(char, "is an upper case letter.")
elif type(char)==str and char.islower() == True:
    print(char, "is a lower case letter.")
elif char.isdigit():
    print(char, "is a digit.")
else:
    print(char, "is a non-alphanumeric character.") 
