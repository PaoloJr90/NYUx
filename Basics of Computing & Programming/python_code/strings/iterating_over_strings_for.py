print("Please enter a line of text:")
line = input()
spaces_count = 0

for ind in range(len(line)):
    curr_char = line[ind]
    if(curr_char == ' '):
        spaces_count += 1
    
number_of_words = spaces_count + 1
print("You typed", number_of_words, "words")
