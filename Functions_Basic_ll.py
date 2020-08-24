# PYTHON FUNDAMENTALS

# Alyssa Falshaw
# August 21st, 2020

# ASSIGNMENT: FUNCTIONS BASIC 2

# Objectives:
# Learn how to create basic functions in Python
# Get comfortable using lists
# Get comfortable having the function return an expression/value

# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]

# def countdown(num):
#     new_list = []
#     for i in range(num, -1, -1):
#         new_list.append(i)
#     return new_list    

# print(countdown(5))

# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

# def par(alist):
#     print(alist[0])
#     return(alist[1])

# par([1,2])
# confirm_return = par([1,2])
# print(confirm_return)

# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

# def fpl(alist):
#     sum = alist[0] + len(alist)
#     return(sum)

# confirm_return = fpl([1,2,3,4,5])
# print(confirm_return)


# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

# def vgts(alist):
#     if len(alist) < 2:
#         return False
#     new_list = []
#     for i in range(len(alist)):
#         if alist[i] > alist[1]:
#             new_list.append(alist[i])
#     print(len(new_list))
#     return new_list

# confirm_return = vgts([5,2,3,2,1,4])
# print(confirm_return)

# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

# def tltv(size, value):
#     create_list = []
#     for i in range(size):
#         create_list.append(value)
#     return create_list

# print(tltv(4,7))
# print(tltv(6,2))

# if __name__ == '__main__':
#     print(tltv(4, 7))
#     print(tltv(6, 2))