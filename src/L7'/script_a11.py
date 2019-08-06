#####################Conditions#################
####Python uses boolean variables to identofy the conditions. The boolean values True or False are returned when expression is evaluated or compared.###


number =16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]
if number > 15:
	print ("Condition 1 Satisfied")
if first_array:
	print ("Condition 2 Satisfied")
if len(second_array) == 2:
	print ("Condition 3 Satisfied")
if len(first_array) + len(second_array) == 5:
	print ("Condition 4 Satisfied")
if first_array and first_array[0] == 1:
	print ("Condition 5 Satisfied")
if not second_number:
	print ("Condition 6 Satisfied")
