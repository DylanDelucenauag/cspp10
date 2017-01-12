import random

def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print ("Rolled 2 dice:\n{} and {}, {} in total!".format(dice1,dice2,dice_sum))
    return dice_sum
    
def get_bet(user_bank):
    while True:
        ask_bet = int(input("How much would you like to bet?: $"))
        if ask_bet > user_bank:
            print ("You don't have that much money.")
            ask_bet = int(input("How much would you like to bet?: $"))
        elif ask_bet < 0:
            print ("NO negative numbers please.")
            ask_bet = int(input("How much would you like to bet?: $"))
        else:
            return ask_bet

def get_range(dice_sum):
    while True:
        if dice_sum > 7:
            return ("over7")
        elif dice_sum < 7:
            return ("under7")
        elif dice_sum == 7:
            return ("7")

def choose_range():
    ask_range = input("What range do you want?\nOver 7 Under 7 or Equals 7: ")
    if ask_range == ("Over 7"):
        return "Over 7"
    elif ask_range == ("Under 7"):
        return "Under 7"
    elif ask_range == ("Equals 7"):
        return "Equals 7"

def overunder7():
    user_bank = 100
    
    print ("/***********************\ ")
    print (" Welcome to Over/Under 7")
    print ("\_______________________/")

    while user_bank > 0:
        bet = get_bet(user_bank)
        user_range = choose_range()
        dice = roll2dice()
        dice_range = get_range(dice)
        
        if user_range == dice_range:
            print("You win!")
            user_bank = user_bank + bet
            print ("Your bank amount is now {}".format(user_bank))
            if user_bank == "7":
                user_bank = user_bank + (bet * 4)
                print ("Nice job you won 4 times your bet. Your bank amount is now {}".format(user_bank))
        else:
            print ("You lost!")
            user_bank = user_bank - bet
            print ("Your bank amount is now {}".format(user_bank))
            new_round = input("Do you want to continue? yes or no: ")
            if new_round != "yes":
                break
    print ("Game over! Your bank amount is now {}".format(user_bank))
    
overunder7()