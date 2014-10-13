print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input ("> ")

if door == "1":
	print "There is a giant bear here eating cake.  What do you do?"
	
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	bear = raw_input ("> ")
	
	if bear == "1":
		print "Bear eats your face off."
	elif bear == "2":
		print "Bear eats your legs off."
	else:
		print "Well, doing %s is probably better.  Bear runs away " % bear
		
elif door == "2":
	print "you start into the eyes of Cthulhu"
	print "1. blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Unterstanding revolvers yelling melodies."
	
	insanity =  raw_input ("> ")
	
	if insanity == "1" or insanity == "2" :
		print "you die"
	else:
		print "you die"
	
else: 
	print "You fall on a knife and die."
	
	
	
	
	
	
	
	
	
	
	
	