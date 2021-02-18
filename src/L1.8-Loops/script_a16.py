#################### LOOP #####################
######################### Python uses two types of loop for and while

#######Use of else clause for the while loop #####

##### When the loop condition of "for" or "while" statement fails then code part in "else" is executed. If break statement is executed inside for loop then the "else" part is skipped. Note that "else" part is executed even if there is a continue statement.##########
count = 0
while(count<5):
	print(count)
	count +=1
else:
	print("count value reached %d" %(count))
for i in range (1,10):
	if(i%5==0):
		break
	print(i)
else:
	print ("This is not printed because for loop is terminated because of break but not due to fail in condition")




