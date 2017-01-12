#Dylan and Tahj

liste = []

choice_of_num = int(input("What number do you want?: "))
while choice_of_num != 0:
    if choice_of_num > 0:
        liste.append(choice_of_num)
        print (liste)
        choice_of_num = int(input("What number do you want?: "))
    
    elif choice_of_num < 0:
        choice_of_num = choice_of_num * -1
        liste.remove(choice_of_num)
        print (liste)
        choice_of_num = int(input("What number do you want?: "))