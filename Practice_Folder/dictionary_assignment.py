import pprint 
dictionary = {}
def add():
    while True:
        key = input("What key value would you like to add?: ")
        value = input("What value are you gong to assign this key?: ")
        if key in dictionary:
            print ("Sorry that key is already in your dictionary.")
            add()
        else:
            dictionary[key] = key
            dictionary[value] = value
    
        print (dictionary)
    


def remove_key():
    while True:
        remove_key = input("State the name of the key that you want to remove: ")
        if remove_key in dictionary:
            del dictionary[remove_key]
        else:
            print("That is not an existing key in your dictionary.")
            remove_key()
        

#add()
remove_key()