# PYTHON FUNDAMENTALS: ASSIGNMENT

# Alyssa Falshaw
# August 15th, 2020


# ASSIGNMENT: HELLO WORLD

# 1. TASK: print "Hello World"

print("Hello World")

# 2. print "Hello Alyssa!" with the name in a variable

name = "Alyssa"
print("Hello ", name, "!", sep="")    # with a comma
print("Hello " + name + "!")	# with a +

# 3. print "Hello 49!" with the number in a variable

name = 49
print("Hello ", name, "!", sep="")   # with a comma
# print("Hello" + name + "!")	# with a +	-- this one should give us an error! TypeError: can only concatenate str (not "int") to str
# Figure out how to resolve the error from above, without changing the + sign to a comma
print("Hello " + str(name) + "!")   # convert the int to a string

# 4. print "I love to eat sushi and pizza." with the foods in variables

fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(fave_food1, fave_food2))    # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}." )     # with an f string
