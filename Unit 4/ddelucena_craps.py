import random
user_bank = 100

print ("Welcome to Craps!")
dice_sum = 0

def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    if dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
        print ("Rolled 2 dice: {} and {}, {} in total.".format(dice1,dice2,dice_sum))
        print ("You lost your bet!")
        
    elif dice_sum == 7 or dice_sum == 11:
        print ("You won")
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
    dice1_phase3 = random.randint(1,6)
    dice2_phase3 = random.randint(1,6)
    dice_sum_phase3 = dice1_phase3 + dice2_phase3
    if dice_sum_phase3 != 7 or dice_sum_phase3 != dice_sum:
        while dice_sum_phase3 != 7 or dice_sum_phase3 != dice_sum:
            print ("Rolled 2 dice: {} and {}, {} in total.".format(dice1_phase3,dice2_phase3,dice_sum_phase3))
            break
            
    elif dice_sum_phase3 == 7:
        return "House wins"
        
    elif dice_sum_phase3 == dice_sum:
        return "You win"

p1_bet()
roll2dice()
phase3(dice_sum)