import random
#does_p1_want_to_play = input("Do you want to play Rock, Paper, Scissors?")
#if does_p1_want_to_play == ("yes")

    
def get_p1_move():
    p1_move = input("Choose r for rock, p for paper, and s for scissors: ")
    if p1_move == "r":
        return "Player move = rock"
        
        
    elif p1_move == "p":
        return "Player move = paper"
        
        
    elif p1_move == "s":
        return "Player move = scissors"
        
        
    else:
        p1_move = int(input("Choose r for rock, p for paper, and s for scissors: "))
        

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
        print 
    
print(get_p1_move())
print(get_comp_move())
    
    
    
    
    
    
    
    
    
    