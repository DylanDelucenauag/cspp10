import random

def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print ("Rolled 2 dice: {} and {}, {} in total!".format(dice1,dice2,dice_sum))
    return dice_sum
    
def first_roll(dice_sum):
    if dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
        print ("You lost!")
        return "lose"
        
    elif dice_sum == 7 or dice_sum == 11:
        print ("You win!")
        return "win"
    else:
        print ("{} is now your point number.".format(dice_sum))
        return dice_sum
    
    
def p1_bet(user_bank):
    while True:
        ask_bet = int(input("How much would you like to bet?: "))
        if ask_bet <= user_bank:
            return ask_bet
        elif ask_bet < 0:
            while ask_bet < 0:
                print ("No negative numbers!")
                ask_bet = int(input("How much would you like to bet?: "))
        elif ask_bet > user_bank:
            while ask_bet > user_bank:
                print ("You don't have that much!")
                ask_bet = int(input("How much would you like to bet?: "))
        
        
def point_number(dice_sum):
    while True:
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        dice_sum_check = dice1 + dice2
        point_number = dice_sum_check
        print ("Rolled 2 dice: {} and {}, {} in total.".format(dice1,dice2,dice_sum_check))
        if point_number == dice_sum:
            print ("You win")
            return "point win"
        elif point_number == 7:
            print ("You lost")
            return "point lose"


def craps():
    
    user_bank = 100
    
    
    print ("Welcome to Craps!")
    print ("\_______________/")


    while user_bank > 0:
        ask_bet = p1_bet(user_bank)
        dice_sum = roll2dice()
        dice_sum_first_roll = first_roll(dice_sum)
        if dice_sum_first_roll == "win": 
            user_bank = user_bank + ask_bet
            print ("Your bank amount is now {}.".format(user_bank))
            print ("-----------------------------")
        elif dice_sum_first_roll == "lose": 
            user_bank = user_bank - ask_bet
            print ("Your bank amount is now {}.".format(user_bank))
            print ("-----------------------------")
        else:
            point_number_var = point_number(dice_sum)
        

            if point_number_var == "point win":
                user_bank = user_bank + ask_bet
                print ("Your bank amount is now {}.".format(user_bank))
                print ("-----------------------------")
            elif point_number_var == "point lose":
                user_bank = user_bank - ask_bet
                print ("Your bank amount is now {}.".format(user_bank))
                print ("-----------------------------")


craps()
#print ("get out")