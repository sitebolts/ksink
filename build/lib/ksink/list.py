#Are any of the items in list 1 equal to any of the items in list 2?
def do_lists_have_any_matches(list_1, list_2):   
    return (len(set(list_1).intersection(list_2)) > 0)
