#Mcdonalds Simulator
#use lists
#big mac = $4
#Quarter pounder with cheese = $3.79
#Hamburger = $2.49
#cheeseburger = $2.79
#mcchicken = $1.29
#mcwrap = $4
#filet o fish = $3.79
#mcrib = $3

def get_p1_order():
    p1_order = input("Welcome to Mcdonalds, What would you like to order\nThis is our menu today:\n(1)Big Mac (2)Quarter Pounder with Cheese (3)Hamburger (4)Cheeseburger\n(5)McChicken (6)McWrap (7)Filet O Fish (8)McRib\n(9)Oreo McFlurry (10)M&M McFlurry\nChoose a number to order:")
    if p1_order == "1":
        return p1_order
    elif p1_order == "2":
        return p1_order
    elif p1_order == "3":
        return p1_order
    elif p1_order == "4":
        return p1_order
    elif p1_order == "5":
        return p1_order
    elif p1_order == "6":
        return p1_order
    elif p1_order == "7":
        return p1_order
    elif p1_order == "8":
        return p1_order
    elif p1_order == "9":
        print ("Sorry ice cream machine is broken today.")
        return get_p1_order()
    elif p1_order == "10":
        print ("Sorry ice cream machine is broken today.")
        return get_p1_order()
    else:
        get_p1_order()

def get_food_name(shortname):
    if shortname == "1":
        return "Big Mac"
    elif shortname == "2":
        return "Quarter Pounder with Cheese"
    elif shortname == "3":
        return "Hamburger"
    elif shortname == "4":
        return "Cheeseburger"
    elif shortname == "5":
        return "McChicken"
    elif shortname == "6":
        return "McWrap"
    elif shortname == "7":
        return "Filet O Fish"
    elif shortname == "8":
        return "McRib"


def order_list(p1_order):
    p1_order_list = []
    p1_order_list = p1_order_list.append(p1_order)
    add_to_order = input("Anything else (yes or no): ")
    while True:
        if add_to_order == ("yes"):
            add_to_order = input("What would you like to order\nThis is our menu today:\n(1)Big Mac (2)Quarter Pounder with Cheese (3)Hamburger (4)Cheeseburger\n(5)McChicken (6)McWrap (7)Filet O Fish (8)McRib\n(9)Oreo McFlurry (10)M&M McFlurry\nChoose a number to orderOr to remove an item write it as a negative number:")
            p1_order_list.append(add_to_order)
            print (p1_order_list)
            return p1_order_list
            
        elif add_to_order == ("no"):
            break


def McSim():
    
    p1_order = get_p1_order()
    p1_order_list = order_list(p1_order)
    
    "1" == 4
    "2" == 3.79
    "3" == 2.49
    "4" == 2.79
    "5" == 1.29
    "6" == 4
    "7" == 3.79
    "8" == 3
    print (p1_order_list)

    
    
McSim()