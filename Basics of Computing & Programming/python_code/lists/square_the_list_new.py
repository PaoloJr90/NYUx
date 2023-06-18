#implement the following function:
    #def create_sqr_list(list)
        #will create and return a new list containing the square of the corresponding elements in list
        
def create_sqr_list(lst):
    res_lst = []
    for elem in lst:
        res_lst.append(elem*elem)
    return res_lst