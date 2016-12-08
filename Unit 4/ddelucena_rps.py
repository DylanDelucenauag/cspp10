import random

def get_p1_move():
    p1_move = input("Choose r for rock, p for paper, and s for scissors: ")
    if p1_move == "r":
        return "r"
        
    elif p1_move == "p":
        return "p"
        
    elif p1_move == "s":
        return "s"
        
    else:
        return get_p1_move()

def get_comp_move():
    comp_move = random.randint(1,3)
    if comp_move == 1:
        return "r"
    
    elif comp_move == 2:
        return "p"
    
    else:
        return "s"
  
def get_rounds():
    rounds = int(input("How many rounds do you want to play?: "))
    return rounds

def get_round_winner(p1_move, comp_move):
    if p1_move == "r" and comp_move == "p":
        return "computer"
        
    elif p1_move == "r" and comp_move == "s":
        return "player"
        
    elif p1_move == "r" and comp_move == "r":
        return "tie"
        
    elif p1_move == "p" and comp_move == "r":
        return "player"
        
    elif p1_move == "p" and comp_move == "s":
        return "computer"
        
    elif p1_move == "p" and comp_move == "p":
        return "tie"
        
    elif p1_move == "s" and comp_move == "r":
        return "computer"
        
    elif p1_move == "s" and comp_move == "p":
        return "player"
        
    elif p1_move == "s" and comp_move == "s":
        return "tie"

def get_full_move(shortmove):
    if shortmove == "r":
        return "Rock"
        
    elif shortmove == "p":
        return "Paper"
        
    elif shortmove == "s":
        return "Scissors"

def print_score(pscore, cscore, ties):
    print("Player Score: {}".format(pscore))
    print("Computer Score: {}".format(cscore))
    print("Ties: {}".format(ties))

def rps():
    rounds = get_rounds()
    pscore = 0
    cscore = 0
    ties = 0
    for x in range(rounds):
        
        p1_move = get_p1_move()
        comp_move = get_comp_move()
        print ("Player chose {}".format(get_full_move(p1_move)))
        print ("Computer chose {}".format(get_full_move(comp_move)))
    
        winner = get_round_winner(p1_move, comp_move)
        if winner == "player":
            print ("Player won")
            pscore = pscore + 1
            print ("------------")
        elif winner == "computer":
            print ("Computer won")
            cscore = cscore + 1
            print ("------------")
        elif winner == "tie":
            print ("It's a tie")
            ties = ties + 1
        print_score(pscore, cscore, ties)
        print ("------------")
        
    if pscore > cscore:
       print ("You won!")
    elif cscore > pscore:
        print ("You lost!")
    elif pscore == cscore:
        print ("It's a tie!")

rps()