number_input = input("Enter a non-negative number: ")
number_int = int(number_input)
noun_input = input("Enter a singular noun: ")

# Ending in -fe ex. knife

noun_end_fe = noun_input[-2:]
noun_end_fe_replace = noun_input[:-2]
if (noun_end_fe == "fe") and ((number_int >= 1) or (number_int <= 1)):
    print (number_input + " " + noun_end_fe_replace + "ves")