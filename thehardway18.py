
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
def print_one(arg1):
	print "arg1: %r" % arg1
	
#this takes no args- 
def print_none():
	print "nope"
	
print_two("Jack", "Martin")
print_two_again ("Jack", "Martin")
print_one("Jack!")
print_none()

