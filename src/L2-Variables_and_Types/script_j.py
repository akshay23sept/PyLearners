############   Variables and Types ##################"
############# In python you do not need to declare variables before using them, or declaring there type, since Python is object oriented. We should keep in mind that in Python each variable is an object.

We want to create  an integer,  a floating point number and a string. The string should be named my_string and should contain the word "learn". The floating point number should be named my_float and should contain the number 16.0, and the integer should be named my_int and should contain the number 40.

my_int = 40
my_float = 16.0
my_string = "learn"

if my_string == "learn":
	print ("String: %s" % my_string)

if isinstance(my_float, float) and my_float == 16.0:
	print("Float: %f" % my_float)

if my_float == 16.0: 
	print("Float: %f" % my_float)

if my_int == 40: 
	print("Integer: %d" % my_int)













