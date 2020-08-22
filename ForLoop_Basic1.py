
# PYTHON FUNDAMENTALS: ASSIGNMENT

# Alyssa Falshaw
# August 21st, 2020


# FOR LOOP BASIC 1

# Objectives:
# Learn how to use basic for loop statements in Python
# Practice some basic algorithms in Python

# 1 Print all integers from 0 to 150.

for a in range(151):
    print(a)


# 2 Print all the multiples of 5 from 5 to 1,000.

for b in range(5, 1001, 5):
    print(b)


# 3 Print integers 1 to 100. If divisible by 5, print "Divisible by 5" instead. If divisible by 10, print "Divisible by 10".

for c in range(1, 101):
    if c % 10 == 0:
        print("Divisible by 10")
    elif c % 5 == 0:
        print("Divisible by 5")
    else:
        print(c)


# 4 Add odd integers from 0 to 500,000, and print the final sum.

sum = 0
for d in range(500001):
    if d % 2 != 0:
        sum += d
print(sum)


# 5 Print positive numbers starting at 2018, counting down by fours.

for e in range(2018, 0, -4):
    print(e)


# 6 Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult.
# For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lowNum = 2
highNum = 9
mult = 3

for f in range(lowNum, highNum + 1):
    if f % mult == 0:
        print(f)

