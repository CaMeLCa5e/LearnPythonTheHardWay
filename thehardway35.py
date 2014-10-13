# 35 

from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"
	
	choice = raw_input ("> ")
	if "o" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("...learn to type a number.  You are dead")
		
	if how_much < 50:
		print "Nice, you are not greedy, you win!"
		exit (0)
	else:
		dead("you greedy bastard")
		
def bear_room():
	print "There is a bear here."
	print "That bear has a numch of honey"
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	
	while True: 
		choice = raw_input ("> ") 
		
		if choice == "take honey":
			dead("You just got slapped by a bear")
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can enter"
		elif choice == "open door" and bear_moved: 
			gold_room()
		else:
			print "you die in the hallway."
			
def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane"
	print "Do you flee for your life or eat your head"
	
	choice =  raw_input("> ")

	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		cthulhu_room()
		
def dead(why):
	print why, "Good job!"
	exit(0)
	
def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	choice = raw_input ("> ")
	
	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("you starve in the hallway")		
		
start()

