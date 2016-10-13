number_input = input("Enter a non-negative number: ")
number_int = int(number_input)
noun_input = input("Enter a singular noun: ")

if (noun_input[-2:] == "fe") and ((number_int > 1) or (number_int < 1)):
    print (number_input + " " + noun_input[:-2] + "ves")
elif number_int == 1:
    print (number_input + " " + noun_input)
    
elif (noun_input[-2:] == "ay") and ((number_int > 1) or (number_int < 1)):
    print (number_input + " " + noun_input + "s")
elif number_int == 1:
    print (number_input + " " + noun_input)
    
elif (noun_input[-2:] == "oy") and ((number_int > 1) or (number_int < 1)):
    print (number_input + " " + noun_input + "s")
elif number_int == 1:
    print (number_input + " " + noun_input)
    
elif (noun_input[-2:] == "ey") and ((number_int > 1) or (number_int < 1)):
    print (number_input + " " + noun_input + "s")
elif number_int == 1:
    print (number_input + " " + noun_input)
    
elif (noun_input[-2:] == "uy") and ((number_int > 1) or (number_int < 1)):
    print (number_input + " " + noun_input + "s")
elif number_int == 1:
    print (number_input + " " + noun_input)

elif (noun_input[-1:] == "y") and ((number_int > 1) or (number_int < 1)):
    print (number_input + " " + noun_input[:-1] + "ies")
elif number_int == 1:
    print (number_input + " " + noun_input)

elif (noun_input[-2:] == "sh") and ((number_int > 1) or (number_int < 1)):
    print (number_input + " " + noun_input + "es")
elif number_int == 1:
    print (number_input + " " + noun_input)
    
elif (noun_input[-2:] == "ch") and ((number_int > 1) or (number_int < 1)):
    print (number_input + " " + noun_input + "es")
elif number_int == 1:
    print (number_input + " " + noun_input)
    
elif (noun_input[-2:] == "us") and ((number_int > 1) or (number_int < 1)):
    print (number_input + " " + noun_input[:-2] + "i")
elif number_int == 1:
    print (number_input + " " + noun_input)
    
elif ((number_int > 1) or (number_int < 1)):
    print (number_input + " " + noun_input + "s")
elif number_int == 1:
    print (number_input + " " + noun_input)







# Ending in -fe ex. knife

#noun_end_fe = noun_input[-2:]
#noun_end_fe_replace = noun_input[:-2]
#if (noun_end_fe == "fe") and ((number_int > 1) or (number_int < 1)):
#    print (number_input + " " + noun_end_fe_replace + "ves")
#elif number_int == 1:
#    print (number_input + " " + noun_input)
    
# Ending in -y ex. family

#noun_end_y = noun_input[-1:]
#noun_end_y_replace = noun_input[:-1]
#elif (noun_end_y == "y") and ((number_int > 1) or (number_int < 1)):
#    print (number_input + " " + noun_end_y_replace + "ies")
#elif number_int == 1:
#    print (number_input + " " + noun_input)