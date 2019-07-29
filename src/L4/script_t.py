################################  Arithmatic operatrs ####################

We want to create two list a and b  which contains 15 items or instances of variables x and y, further we want to create a very big list which should contain variable a and b 15 times by concentating the two list that we created.

a = object ()
b = object ()
a_list = [a] * 15
b_list = [b] * 15
Very_big_list = a_list + b_list
print (" a_list contains %d objects" % len (a_list))
print (" b_list contains %d objects" % len (b_list))
print (" Very_big_list contains %d objects" % len (Very_big_list))

if a_list.count(a) ==15 and b_list.count(b) ==15:
	print ("Almost There")

if Very_big_list.count(a)==15 and Very_big_list.count(b)==15:
	print ("Super Good, Bravo !!!!!")
