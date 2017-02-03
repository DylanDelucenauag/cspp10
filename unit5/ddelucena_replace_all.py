#Tahj and Dylan
def replace_all(original,to_replace,replace_with):
    for index in range(len(original)):
        if original[index] == to_replace:
            original[index] = replace_with
            
        
    
    

original = [1,5,4,1,3,1,2,6]
to_replace = 1
replace_with =8
replace_all(original,to_replace,replace_with)
print(original)
    