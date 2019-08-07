#################### LOOP #####################
######################### Python uses two types of loop for and while

###Loop through and print out all even numbers from the numbers list in the same order they are received. ##Don't print any numbers that come after 237 in the sequence.

numbers = [ 951, 4712, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 665, 575, 219, 390, 984, 492, 236, 105, 942, 741,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 241, 892, 394, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    858, 609, 142, 451, 688, 753, 854, 685, 93, 457, 440, 380, 126, 721, 328, 753, 470,
    943, 229
]

for number in numbers:
	if number ==248:
		break
	if number % 2 ==1:
		continue
	print(number)

