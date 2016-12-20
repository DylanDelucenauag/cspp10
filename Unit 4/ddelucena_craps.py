import random
user_bank = 100

print ("Welcome to Craps!")


def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    if dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
        print ("You lost your bet!")
        #return dice_sum
        return "lose"
        
    elif dice_sum == 7 or dice_sum == 11:
        print ("You won")
        #return dice_sum
        return "win"
    else:
        print ("Rolled 2 dice: {} and {}, {} in total.".format(dice1,dice2,dice_sum))
        print ("Your point number is: " + str(dice_sum))
        return dice_sum


    
def p1_bet():
    user_bank = 100
    ask_bet = int(input("How much would you like to bet?: "))
    if ask_bet < 0:
        while ask_bet < 0:
            print ("No negative numbers!")
            ask_bet = int(input("How much would you like to bet?: "))
    elif ask_bet > user_bank:
        while ask_bet > user_bank:
            print ("You don't have that much!")
            ask_bet = int(input("How much would you like to bet?: "))
    elif ask_bet <= user_bank:
        user_bank = user_bank - ask_bet
        return ask_bet
        
    

def phase3(dice_sum):
    dice_sum_phase3 = roll2dice()
    if dice_sum_phase3 != 7 or dice_sum_phase3 != dice_sum:
        while dice_sum_phase3 != 7 or dice_sum_phase3 != dice_sum:
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            dice_sum = dice1 + dice2
            print ("Rolled 2 dice: {} and {}, {} in total.".format(dice1,dice2,dice_sum_phase3))
            return dice_sum_phase3
            
    elif dice_sum_phase3 == 7:
        return "House wins"
        
    elif dice_sum_phase3 == dice_sum:
        return "You win"

def craps():
    dice_sum = roll2dice()
    dice_sum_phase3 = phase3(dice_sum)
    
    while dice_sum_phase3 != dice_sum:
        if dice_sum == "lose":
            print ("You lost2")
            break
        elif dice_sum == "win":
            print ("You won2")
            break
        else:
            return dice_sum



p1_bet()
roll2dice()
dice_sum = roll2dice()
phase3(dice_sum)

#craps()