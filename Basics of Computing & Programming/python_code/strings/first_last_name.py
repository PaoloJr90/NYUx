print("Please enter your name. Separate first and last name by a space:")
full_name = input()

space_ind = full_name.find(" ")
first_name = full_name[ : space_ind]
last_name = full_name[space_ind +1 : ]
initials = first_name[0] + last_name[0]

print("First name:", first_name)
print("Last name:", last_name)
print("Initials", initials)