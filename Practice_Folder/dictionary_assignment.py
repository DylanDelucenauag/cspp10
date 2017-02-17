from pprint import pprint 
dictionary = {}
def add():
        key = input("What key value would you like to add?: ")
        value = input("What value are you gong to assign this key?: ")
        if key in dictionary:
            print ("Sorry that key is already in your dictionary.")
            
        else:
            dictionary[key] = key
            dictionary[value] = value
            return key, value
            
    
        print (dictionary)
    


def remove_key():
    while True:
        remove_key = input("State the name of the key that you want to remove: ")
        if remove_key in dictionary:
            del dictionary[remove_key]
        else:
            print("That is not an existing key in your dictionary.")
            remove_key()


def update(key,value):
    find_key = input("What key do you want to change?: ")
    if find_key in dictionary:
        update_key = input("What would you like to change this key name to?: ")
        update_value = input("What would you like to change this value name to?: ")
        dictionary[key] = update_key
        dictionary[value] = update_value
    else:
        print ("This key is not in your dictionary.")
        update(key,value)



def print():
    pprint (dictionary)

#def dictionary():

add()
remove_key()