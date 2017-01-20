liste = []
while True:
    user_input = input("What number do you want?: ")
    if user_input == "sum":
        num = sum(liste)
        print ("Your list is now {}".format(num))
        
    elif user_input == "clear":
        liste = []
        print ("Your list is now {}".format(liste))
        
    elif user_input == "print":
        print ("Your list is now {}".format(liste))
        
    elif user_input == "length":
        num = len(liste)
        print(num)
        
    elif user_input == "exit":
        break
    
    else:
        liste.append(int(user_input))
