#lst = [19,2,20,1,0,18]

def avg_val(lst):
    sum_of_list = 0
    for i in range(len(lst)):
        sum_of_list += lst[i]
    average = sum_of_list/len(lst)
    return average
    #print(average)

#avg_val(lst)