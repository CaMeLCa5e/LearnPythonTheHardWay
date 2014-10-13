#39 
# Create mapping
states = {
	'Oregon': "OR",
	"Florida": "FL", 
	"California": "CA", 
	"New York": "NY",
	"Michigan": "MI"

}

#set of cities
cities = {
	"CA" : "San Francisco", 
	"MI" : "Detroit", 
	"FL" : "Jacksonville"
}

#more cities
cities['NY'] = "New York"
cities ["OR"] = "Portland"

#print some cities
print "-" * 10
print "NY State has: ", cities ["NY"]
print "OR State has: ", cities ["OR"]

#print some states
print '_' * 10
print "Michigan's abbreviation is:", states["Michigan"]
print "Florida's abbreviation is: ", states['Florida']

#
print "-" * 10
print "Michigan has:", cities[states['Michigan']]
print "Florida has: ", cities[states ['Florida']]

print "-" * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)
	
print "-" * 10 
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (
		state, abbrev, cities[abbrev])
		
print "-" * 10
state = states.get('Texas')

if not state: 
	print "Sorry, no Texas."
	
city = cities.get ('TX', "Does not exist")
print "The city for the state 'TX' is %s" % city










