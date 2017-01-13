user_input = input("Say something anything im loneley: ")
liste = []
listr = []
while True:
    if user_input == "sum":
        sum(int(liste))
        user_input = int(input("What number do you want?: "))
        
    elif user_input == "clear":
        listr.append(liste)
        print ("Your list is now {}".format(liste))
        user_input = int(input("What number do you want?: "))
        
    elif user_input == "print":
        print ("Your list is now {}".format(liste))
        user_input = int(input("What number do you want?: "))
        
    elif user_input == "length":
        print (liste).len
        user_input = int(input("What number do you want?: "))
        
    elif user_input == "exit":
        break
    
    else:
        liste.append(user_input)
        print (liste)
        user_input = input("What number do you want?: ")
