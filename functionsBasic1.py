# PYTHON FUNDAMENTALS

# Alyssa Falshaw
# August 21st, 2020

# ASSIGNMENT: FUNCTIONS BASIC 1 

# For each of the following code snippets, first predict the output (what you will see printed to the terminal). 
# Once you've made a prediction, run the code snippet to see if you are correct!

# # 1
# def a():
#     return 5
# print(a())

# OUTPUT: 5
# Function a() becomes 5, then a() is printed which is 5.

#2
# def a():
#     return 5
# print(a()+a())

# OUTPUT: 10
# Function a() becomes 5, then a() is added to another a(), which is 5 + 5 = 10.

# # 3
# def a():
#     return 5
#     return 10
# print(a())

# OUTPUT: 5
# Function a() becomes 5, then is printed. Return 10 is skipped because it is unreachable, only the first return is read and then the function ends.

# OUTPUT:

# # 4
# def a():
#     return 5
#     print(10)
# print(a())

# OUTPUT: 5
# Function a() becomes 5, then is printed. Print(10) is skipped becasue it is unreachable, once a return is stated, the function ends.

# # 5
# def a():
#     print(5)
# x = a()
# print(x)

# OUTPUT: 5, None
# 5 is printed. x becomes function a(), but nothing is returned so None is printed for x.

# # 6
# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))

# OUTPUT: 3, 5, TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
# 3 is printed from 1st set of arguments, 5 is printed from second set of arguments. print(a(3)) + a(5)) cannot be performed because of TypeError.

# # 7
# def a(b,c):
#     return str(b)+str(c)
# print(a(2,5))

# OUTPUT: 25
# Arguments are converting to strings, concat 2 + 5 = 25; no longer integers so you don't add them like numbers.

# # 8
# def a():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(a())

# OUTPUT: 100, 10
# b = 100 and then is printed, 10 is returned because b = 100 which is > 10. return 7 is skipped because function has ended.

# # 9
# def a(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a(2,3))
# print(a(5,3))
# print(a(2,3) + a(5,3))

# OUTPUT: 7, 14, 21
# 2 < 3 returns 7 from first set of arguments. 5 is not < 3, therefore 14 is returned from second set of arguments. 7 + 14 = 21 from third set of arguments.

# # 10
# def a(b,c):
#     return b+c
#     return 10
# print(a(3,5))

# OUTPUT: 8
# 3 + 5 = 8 is returned, return 10 is skipped because the function has ended.

# # 11
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
# print(b)
# a()
# print(b)

# OUTPUT: 500, 500, 300, 500
# b = 500 is printed, function not yet called, print b = 500 is printed once again, function is called, b = 300 is printed, complete block with last print(b) which b = 500.

# # 12
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# a()
# print(b)

# OUTPUT: 500, 500, 300, 500
# b = 500 is printed, function not yet called, print b = 500 is printed once again, function is called, b = 300 is printed, b is returned, complete block with last print(b) which b = 500.


# # 13
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=a()
# print(b)

# OUTPUT: 500, 500, 300, 300
# b = 500 is printed, function not yet called, b = 500 is printed once again, b becomes function a(), function called, b = 300 is printed, b is returned -> b = a(), function called again, b = 300 is pritned.

# # 14
# def a():
#     print(1)
#     b()
#     print(2)
# def b():
#     print(3)
# a()

# OUTPUT: 1, 3, 2
# function a() is called first, 1 is printed, function b() is called within a(), 3 is printed, return back to finish function a() block, 2 is printed. 

# # 15
# def a():
#     print(1)
#     x = b()
#     print(x)
#     return 10
# def b():
#     print(3)
#     return 5
# y = a()
# print(y)

# OUTPUT: 1, 3, 5, 10
# y = a() function which is called, 1 is printed, x = b() function which is called, 3 is printed, 5 is returned, return back to finish a(), 5 is printed, 10 is returned and printed since y = a()
