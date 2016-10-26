user_input = input("Enter a number: ")
num_user_input = int(user_input)

for num_user_input in range(1,num_user_input + 1):
    if num_user_input % 3 == 0 and num_user_input % 5 == 0:
        n = ("fizz")
        x = ("buzz")
        print (n + x)
    elif num_user_input % 3 == 0:
        n = ("fizz")
        print (n)
    elif num_user_input % 5 == 0:
        x = ("buzz")
        print (x)
    else:
        n = num_user_input
        print (num_user_input)