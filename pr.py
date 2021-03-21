# try:
	# a = 1
	# y = a/0
# except ZeroDivisionError as e:
	# print(e.message)

# a = [1,2,3]
# sum = sum(a)
# print(sum)

# Write a Python program to get the Python version you are using.
# import sys
# print("Python version")
# print (sys.version)
# print("Version info.")
# print (sys.version_info)
# Write a Python program to display the current date and time.
# import datetime
# now = datetime.datetime.now()
# print ("Current date and time : ")
# print (now.strftime("%Y-%m-%d %H:%M:%S"))
# # Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them
# fname = ("prakash")
# lname = ("surya")
# print("hello "+lname+fname)

# def char_frequency(str1):
#     dict = {}
#     for n in str1:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     return dict
# print(char_frequency('google.com'))
# Write a Python program wich accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
# values = input("inputvalue: ")
# list = values.split(",")
# tuple = tuple(list)
# print('List : ',list)
# print('Tuple : ',tuple)


# import json
# a =  '{ "name":"John", "age":30, "deg":"btech"}'

# b = json.loads(a)

# print(b)


# try :
# 	m = {"name": "surya","age":23}
# 	print(m.get("city"))
# except keyerror as d :
# 	print("i got a keyerror")

# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0],color_list[3])
# exam date
# exam = (10,2,2010)
# print ("%i/%i/%i"%exam)

# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# n = int(input("enter the number n:"))
# temp =str(n)
# temp1=temp+temp
# temp2=temp+temp+temp
# comp=n+int(temp1)+int(temp2)
# print("the value of n :",comp)
import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))

