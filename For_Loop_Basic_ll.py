# PYTHON FUNDAMENTALS

# Alyssa Falshaw
# August 22nd, 2020


# ASSIGNMENT: FOR LOOPS BASIC 2

# Objectives:
# Get comfortable writing functions only using basic building blocks of Python (i.e. using your own skills rather than relying on built-ins)
# Get comfortable using for loops, functions, lists, and other data types

# 1
# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

# def biggie_size(alist):
#     for i in range(len(alist)):
#         if alist[i] > 0:
#             alist[i] = "big"
#     return alist

# print(biggie_size([-1,3,5,-5]))


# 2
# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. 
# (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

# def replace(alist):
#     counter = 0
#     for i in range(1, len(alist)):
#         if alist[i] > 0:
#             counter += 1
#             alist[len(alist)-1] = counter
#     return alist

# print(replace([-1,1,1,1]))
# print(replace([1,6,-4,-2,-7,-2]))


# 3
# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

# def sum_total(alist):
#     sum = 0
#     for i in range(len(alist)):
#         sum += alist[i]
#     return sum

# print(sum_total([1,2,3,4]))
# print(sum_total([6,3,-2]))


# 4
# Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5

# def average(alist):
#     sum = 0
#     for i in range(len(alist)):
#         sum += alist[i]
#         avg = sum / len(alist)
#     return avg

# print(average([1,2,3,4]))


# 5
# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

# def length(alist):
#     print(len(alist))

# length([37,2,1,-9])

# def length(alist):
#     count = 0
#     for i in range(len(alist)):
#         count += 1
#     return count

# print(length([37,2,1,-9]))


# 6
# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

# def mini(alist):
#     if len(alist) == 0:
#         return False
#     minimum = alist[0]
#     for i in range(len(alist)):
#         if minimum > alist[i]:
#             minimum = alist[i]
#     return minimum

# print(mini([37,2,1,-9]))
# print(mini([]))


# 7
# Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

# def maxi(alist):
#     if len(alist) == 0:
#         return False
#     maximum = alist[0]
#     for i in range(len(alist)):
#         if maximum < alist[i]:
#             maximum = alist[i]
#     return maximum

# print(maxi([37,2,1,-9]))
# print(maxi([]))




# 8
# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

# def analysis(alist):
#     my_dictionary = {
#         'sumTotal' : 0,
#         'average' : 0,
#         'minimum' : alist[0],
#         'maximum' : alist[0],
#         'length' : 0,
#     }
#     for i in range(len(alist)):
#         sumTotal += alist[i]
#         average = find_sum / len(alist)
#         if minimum > alist[i]:
#             minimum = alist[i]
#         if maximum < alist[i]:
#             maximum = alist[i]
#         length += 1
#     return my_dictionary
        
# print(analysis([37,2,1,-9]))



# 9
# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

# def reverse(alist):
#     i = 0                 # first item
#     j = len(alist)-1      # last item
#     while i < j:
#         alist[i], alist[j] = alist[j], alist[i]
#         i += 1
#         j -= 1
#     return alist

# print(reverse([37, 2, 1, -9, -7, 3]))
