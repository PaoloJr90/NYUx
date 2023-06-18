print("Please enter 3 words:")
word1 = input("#1: ")
word2 = input("#2: ")
word3 = input("#3: ")

if(word1 <= word2 and word1 <= word3):
    print(word1)
elif(word2 <= word1 and word2 <= word3):
    print(word2)
else:
    print(word3)
