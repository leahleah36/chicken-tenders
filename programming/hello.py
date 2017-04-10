name = raw_input("enter your name")
age = int(input("enter your age"))
birthday = raw_input("have you had a birthday this year? y/n ")
print "your name is:" + name
print "your age is:", age

year = 100 - age
year = year + 2017

if(birthday != "y"):
	year = year - 1
	
	
print "you will turn 100 in year: ", year




name = raw_input("ni jiao shenme mingzi?")
age = int(input("ni ji sui?"))
birthday = raw_input("ni jinian you meiyou shengri ma? you/meiyou")
print "ni jiao:" + name
print "ni", age, "sui"

year = 100 - age
year = year + 2017

if(birthday != "you"):
	year = year - 1
	
print "ni", year, "shi yi bai sui"


