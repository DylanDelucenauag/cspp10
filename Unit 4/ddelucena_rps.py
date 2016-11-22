import random
#does_p1_want_to_play = input("Do you want to play Rock, Paper, Scissors?")
#if does_p1_want_to_play == ("yes")

pscore = 0
cscore = 0
ties = 0
    
def get_p1_move():
    p1_move = input("Choose r for rock, p for paper, and s for scissors: ")
    if p1_move == "r":
        return "Player move = rock"
        
        
    elif p1_move == "p":
        return "Player move = paper"
        
        
    elif p1_move == "s":
        return "Player move = scissors"
        
        
    else:
        get_p1_move()
        

def get_comp_move():
    comp_move = random.randint(1,3)
    if comp_move == 1:
        return "Computer move = rock"
    
    elif comp_move == 2:
        return "Computer move = paper"
    
    else:
        return "Computer move = scissors"
  
  
def get_rounds():
    rounds = int(input("How many rounds do you want to play?: "))
    rounds = rounds + 1
    for x in range(1, rounds):
        return "4"
    
    
def get_round_winner(p1_move, comp_move):
    if p1_move == "r" and comp_move == "p":
        return comp_move
        
    elif p1_move == "r" and comp_move == "s":
        return p1_move
        
    elif p1_move == "r" and comp_move == "r":
        return "tie!"
        
    elif p1_move == "p" and comp_move == "r":
        return p1_move
        
    elif p1_move == "p" and comp_move == "s":
        return comp_move
        
    elif p1_move == "p" and comp_move == "p":
        return "tie"
        
    elif p1_move == "s" and comp_move == "r":
        return comp_move
        
    elif p1_move == "s" and comp_move == "p":
        return p1_move
        
    elif p1_move == "s" and comp_move == "s":
        return "tie"
        
def get_full_move(shortmove):
    if shortmove == "r":
        return "Rock"
        
    elif shortmove == "p":
        return "Paper"
        
    else:
        return "Scissors"

def print_score(pscore, cscore, ties):
    pscore == int(pscore)
    cscore == int(cscore)
    ties == int(ties)
    print("Player Score: {}".format(pscore))
    print("Computer Score: {}".format(cscore))
        

p1_move = get_p1_move()
comp_move = get_comp_move()


def rps():
    pscore = 0
    cscore = 0
    
    rounds = get_rounds()
    p1_move =get_p1_move()
    comp_move = get_comp_move()
    
    print ("Player chose {}".format(get_full_move(p1_move)))
    print ("Computer chose {}".format(get_full_move(comp_move)))
    
    winner = get_round_winner(p1_move, comp_move)
    if winner == "p1_move":
       print ("Player one")
    elif winner == "comp_move":
        print ("Computer won")
    else:
        print ("It's a tie")

print (get_rounds())
#print(get_p1_move())
#print(get_comp_move())
#print (get_round_winner(p1_move, comp_move))
#print (winner)
#print (rps())