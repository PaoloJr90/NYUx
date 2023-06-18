#print("Please enter a sentence:")
#sentence = input()
#spaces_count = sentence.count(' ')

def remainingwords(sentence):
    if  sentence.count(" ") == 0:
        #print("")
        return ""
    elif sentence.count(" ") >= 1:
         space_index = sentence.find(" ")
         remain = sentence[space_index + 1 : ]
         #print(remain)
         return remain
        
#remainingwords(sentence)   
#print(len(remainingwords(sentence)), len(sentence))
#print(spaces_count)

