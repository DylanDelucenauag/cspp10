#Dylan and Tahj
def replace_all(original,to_replace,replace_with):
    to_replace = int(input("what number would you like to replace? "))
    for element in original:
        original.insert(to_replace)
    

original = [2,5,4,7,9,1,2,7]
replace_all(original,7,"d")
    