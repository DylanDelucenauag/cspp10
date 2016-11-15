import random
#does_p1_want_to_play = input("Do you want to play Rock, Paper, Scissors?")
#if does_p1_want_to_play == ("yes")

#p1_input_rounds = input("How many rounds would you like to play?")
def get_p1_move():
    p1_move = input("Choose r for rock, p for paper, and s for scissors: ")
    if p1_move == "r":
        return "r"
        
        
    elif p1_move == "p":
        return "p"
        
        
    elif p1_move == "s":
        return "s"
        
        
    else:
        p1_move = int(input("Choose r for rock, p for paper, and s for scissors: "))
        

def get_comp_move():
    comp_move = random.randint(1,3)
    if comp_move == 1:
        return "r"
    
    
  
    
    
print(p1_move())
    
    
    