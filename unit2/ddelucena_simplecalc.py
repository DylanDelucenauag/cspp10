user_equation = input("Enter an eqution: ")
#takes the first number of the equation and makes it its own variable
num_1 = user_equation[0]
#takes the second thing which is the operator
operator = user_equation[1]
#takes the last number from the input and makes it its own variable
num_2 = user_equation[2]
if operator == "+":
    print ("The result is " + str(int(num_1) + int(num_2)))
elif operator == "*":
    print ("The result is " + str(int(num_1) * int(num_2)))
elif operator == "/":
    print ("The result is " + str(int(num_1) / int(num_2)))
elif operator == "-":
    print ("The result is " + str(int(num_1) - int(num_2)))
else:
    print ("The result is " + str(int(num_1) % int(num_2)))
    

#print ("The result is " + str())


#equation_entered = int(user_equation)

#user_input1 = input("Enter your first number: ")
#user_input2 = input("Enter your operation: ")
#user_input3 = input("Enter your second number: ")