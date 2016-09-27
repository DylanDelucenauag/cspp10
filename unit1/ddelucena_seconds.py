time = input("Enter a number, no negative numbers please. ")
time = int(time)
x = time % 60
y = time - x
minutes = y / 60
a = minutes % 60
b = minutes - a
hours = minutes / 60
seconds_string = str(x)
minutes_string = str(a)
hours_string = str(hours)
print (hours_string + " hours " + minutes_string + " minutes " + seconds_string + " seconds ")