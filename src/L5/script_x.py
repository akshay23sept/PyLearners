####################" String Formatting ##########
####### Python usees %  operator to format set of variables enclosed in tuple (a fixed size list) together with format string which contains normal text together with "argument specifiers"
##################### %s is used for strings ################""
##################### %d is used for integers ################""
##################### %f is used for floating point numbers ################""
##################### %f.<> is used for floating point with fixed amount of digits ################""
##################### %f is used for floating point numbers (lower case) ################""
##################### %f is used for floating point numbers (UPPER CASE) ################""

################### We want to print a String and numbers together ##############""""

data = ("Thomas", "Cadario", 25000)
format_string = "Hello %s %s, your account balance is %s."
print(format_string %data)
