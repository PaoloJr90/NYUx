#implement the following function:
    #def sqr_list_in_place(lst)
        #will square, in-place, each element in list

def sqr_list_in_place(lst):
    for i in range(len(lst)):
        lst[i] = lst[i]*lst[i]