#Dylan and Tahj
def extend(original,extension):
    
    for value in extension:
        original.append(value)
        
original = [1,2,3]
extension = [33,3,1]
extend(original,extension)
print (original)