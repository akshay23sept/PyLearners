#################### LOOP #####################
######################### Python uses two types of loop for and while

############ Break and Continue Statements #############
count = 0
while  True:
	print(count)
	count += 1
	if count  >= 5:
		break
### Normally this should print 0,1,2,3,4 but break has its influence,
##Break is used to exit for loop or while loop, whereas continue is used to skip current block, and return to the for and while statemennt###
for x in range(10):
	if x%2 ==0:
		continue
	print(x)




