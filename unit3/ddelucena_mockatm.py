user_choice = input("Welcome to DD bank, would you like to, Withdraw, Deposit, or Exit: ")
money = 10000
#while money < 0:
#    if user_choice == ("Withdraw"):
#        take_out = int(input("How much would you like to take out? "))
#        money = money - take_out
#        print ("Your balance is " + str(money))
#        break
while money > 0:
    if user_choice == ("Withdraw"):
        take_out = int(input("How much would you like to take out? "))
        money = money - take_out
        print ("Your balance is " + str(money))
        break
    elif user_choice == ("Deposit"):
        put_in = int(input("How much would you like to put in? "))
        money = money + put_in
        print ("Your balance is " + str(money))
        break
    elif user_choice == ("Exit"):
        break

print ("Have a nice day.")


#while user_choice == ("Withdraw" or "Deposit"):


#while user_choice in range(1,5):
#    if user_choice != ("withdraw"):


#if user_choice != "withdraw" or "deposit" or "exit":
#    print (user_choice)