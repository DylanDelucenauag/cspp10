import random
#Need a shortcut to scramble the list called: list.shuffle()
#Need a function called scramble_word() that scrambles a single word
#Need a function scramble_phrase() that uses scramble_word() to scramble a series of words
#Phrase will be hard coded and the words must be 4 letters or larger
#Make sure to keep the first and last word the same

word = "Microsoft"
def scramble_word(word):
    if len(word) >= 4:
        good_word = list(word)
        first_letter = good_word[:1]
        last_letter = good_word[-1:]
        middle_letters = good_word[1:-1]
        
        random.shuffle(middle_letters)
        middle_letters.insert(0,first_letter)
        middle_letters.append(last_letter)
        end_word = ''.join(middle_letters)
        print (end_word)
        
    
scramble_word(word)