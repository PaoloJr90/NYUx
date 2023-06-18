print("Please enter a line of text:")
line = input()
spaces_count = 0

for curr_char in line:
    if(curr_char == ' '):
        spaces_count += 1

words_count = spaces_count + 1
print("You typed", words_count, "words")