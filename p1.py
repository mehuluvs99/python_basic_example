# # https://www.w3resource.com/python-exercises/python-basic-exercises.php
# import datetime
# print(datetime.datetime.now())

"""Write a Python program that accepts the user's first
and last name and prints them in reverse order with a space between them."""

# print(input("First name"), input("Last Name"))

"""Write a Python program that accepts a sequence of 
comma-separated numbers from the user and generates a list and a tuple of those numbers"""

# x = input("Enter Number using comma").split(",")
# z = tuple(x)
# print(x, z)

"""8. Write a Python program to display the first and last colors from the 
following list. color_list = ["Red","Green","White" ,"Black"]"""

# color_list = ["Red","Green","White" ,"Black"]
# print("%s %s"%(color_list[0],color_list[-1]))

"""
9. Write a Python program to display the examination schedule. (extract the date from exam_st_date). 
"""

# exam_st_date = (11, 12, 2014)
# print("%i/%i/%i"%(exam_st_date))

"""10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn."""
#Sample value of n is 5

# a = int(input("Input an integer : "))
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# print (n1+n2+n3)

"""Write a Python program to calculate the number of days between two dates."""
"""Sample dates : (2014, 7, 2), (2014, 7, 11)"""


# from datetime import date
# Sample_dates = date(2014, 7, 2)
# Sample_dates1 = date(2014, 7, 11)
# delta = Sample_dates - Sample_dates1

# print(delta.days)

"""Write a Python program to calculate the difference between a given number and 17.
If the number is greater than 17, return twice the absolute difference."""

# x = int(input("Enter Number:"))

# if x <= 17:
#     print(17-x)
# else:
#     print((x-17)*2)

"""Write a Python program to test whether a number is within 100 of 1000 or 2000."""
# def near_thousand(n):
#       return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
# print(near_thousand(1000))
# print(near_thousand(900))
# print(near_thousand(800))   
# print(near_thousand(2200))


"""Write a Python program to calculate the sum of three given numbers.
If the values are equal, return three times their sum."""

# a,b,c = int(input("Enter Number 1 : ")), int(input("Enter Number 2 : ")), int(input("Enter Number 3 : "))
# if a==b==c:
#     print((a+b+c)*3)
# else:
#     print(a+b+c)

# def x(a,b,c):
#     sum = a+b+c
    
#     if a==b==c:
#         sum = sum*3
#     return sum

# print(x(1,2,3)) 

"""
 Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front.
 Return the string unchanged if the given string already begins with "Is"""

# def s(st):
#     if st[:2] == "Is":
#         return st
#     return "Is"+st
# print(s("IsEmply"))
# print(s("Array"))

"""Write a Python program that returns a string that is n (non-negative integer) copies of a given string."""

# def large_string(s,n):
#     result = ''
#     for i in range(n):
#         result = result+s
#     return result

# print(large_string("abc",2))
# print(large_string(".py",3))


"""Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user."""

# n = int(input("Enter Number  "))
# if (n % 2) < 0:
#     print("Even")
# else:
#     print("odd")

"""Write a Python program to count the number 4 in a given list."""

# def l(search,arr):
#     count = 0
#     for i in arr:
#         if search == i:
#             count +=1
#     return count
# m = l(4,[1,4,1,2,4,6,7,9,4])
# print(m)


"""Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string.
Return n copies of the whole string if the length is less than 2"""

# def substring_copy(text, n):
#   flen = 2
#   if flen > len(text):
#     flen = len(text)
#   substr = text[:flen]
#   result = ""
#   for i in range(n):
#     result = result + substr
#   return result
# print(substring_copy('abcdef', 2))
# print(substring_copy('p', 3))


"""Write a Python program to test whether a passed letter is a vowel or not"""

# def letter(search):
#     text = "aeiou"
#     for i in text:
#         if search == i:
#             return True
#     return False


# print(letter("i"))
# print(letter("c"))

"""Write a Python program that checks whether a specified value is contained within a group of values."""

# def letter(text, search):

#     for i in text:
#         if search == i:
#             return True
#     return False


# print(letter([1,5,8,3],3))
# print(letter([1,5,8,3],-1))

"""Write a Python program to create a histogram from a given list of integers."""
def histogram(x,y):

    for i in y:
        print(i)
        return str(x)*i,end("\n")


print(histogram("#",[2,3,6,5]))