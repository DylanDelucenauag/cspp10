import random
comp_number = random.randint(1,100)
player_guess = int(input("Guess a number from 1 to 100: "))

while (player_guess != comp_number):
    if player_guess > comp_number:
        print ("Too high!")
        print ("Try again")
        player_guess = int(input("Guess again: "))
        
    elif player_guess < comp_number:
        print ("Too low!")
        print ("Try again!")
        player_guess = int(input("Guess again: "))
    
    
if (player_guess == comp_number):
    print ("Good Job")
    print ("The number was " + str(comp_number))
    print("You're like the best person ever!")




#first_guess = input("Guess a number")

