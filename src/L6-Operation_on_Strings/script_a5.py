########################################  String Operations ####################
## Strings are some texts which can be defined anywhere between the quotes###

s = "Strings are amazing!"
print ("Length of s = %d" % len(s))
print ("The first occurance of e is at =%d" %s.index("e"))
print ("e occurs %d times"  % s.count("e"))
print ("The first 10 characters are %s" %s[: 10])
print ("The next 10 characters are %s" %s[10 :])
print ("The fourteenth character is %s" %s[14])
print ("The  characters with odd indices are '%s'" %s[: 10])
print ("The last five characters are '%s'" % s[-5:])
print ("String in uppercase:%s" %s.upper())
print ("String in uppercase:%s" %s.lower())
print ("Split the word of string: %s" %s.split(" "))
if s.startswith("String"):
	print ("Strings starts with 'String'. Nice!")
if s.endswith("zing!"):
	print ("Sting ends with'zing!'. Great!")

