# syntax errors
#runtime errors
#logical errors


#logical error
# num_1 = 10
# num_2 = 5 
# result = num_1 + num_2
# print(result)

#syntax error

# print(f"hi"

# for i in range(10)
# print(i)

#runtime error

# num_1 = int(input("enter the num_1: "))
# num_2 = int(input("enter the num_2: "))

# print( num_1 + num_2 )
# print( num_1 - num_2 )
# print( num_1 * num_2 )
# try:
#     print( num_1 / num_2 )
# except:
#     print(f"error occured")
# else:
#     print("no error")
    
# finally:
#     print("everything done")

# print( num_1 + num_2 )
# print( num_1 - num_2 )

# list_1 = [10,20,30,40]
# print(list_1[2])
# print(list_1[0])
# try:
#  print(list_1[9])
# except:
#     print("index out of range")
# print(list_1[1])

#value error ip ten

# try:
#  num_1 = int(input("enter the num_1: "))
#  num_2 = int(input("enter the num_2: "))
# except  ValueError as e:
#     print(e)
# else:
#  print( num_1 + num_2 )

#zero division error

# num_1 = int(input("enter the num_1: "))
# num_2 = int(input("enter the num_2: "))
# try:
#  print( num_1 / num_2 )
# except ZeroDivisionError as e:
#     print(e)

#index error

# list_1 = [10,20,30,40]
# print(list_1[2])
# print(list_1[0])
# try:
#  print(list_1[9])
# except IndexError as e:
#     print(e)

# try:
#  num_1 = int(input("enter the num_1: "))
#  num_2 = int(input("enter the num_2: "))
#  print(num_1 / num_2)
#  list_1 = [10,20,30,40]
#  print(list_1[8])
# except Exception as e:
#     print(e)
      
#TypeError

# age = "30"
# try:
#  result = age + 5
# except TypeError as e :
#     print(e)

# age = "30"
# try:
#  result = age + 5
# except Exception as e :
#     print(e)

#FileNotFoundError

# try:

#  file = open("ert.txt", mode= 'r')

# except FileNotFoundError as e:
#     print(e)

# try:

#  file = open("ert.txt", mode= 'r')

# except Exception as e:
#     print(e)

#key error

# dict_1 = {
#     1 : "naren",
#     2: "eeshwar",
#     3: "vinnu",
#     4: "prathibha"}
# try:
#     print(dict_1[6])
# except KeyError as e:
#     print(e)

# dict_1 = {
#     1 : "naren",
#     2: "eeshwar",
#     3: "vinnu",
#     4: "prathibha"}
# try:
#     print(dict_1[6])
# except Exception as e:
#     print(e)


# AttributeError

# name = "naren"
# try:
#  name.append("a")
# except AttributeError as e:
#     print(e)

# num_1 = 10
# try:
#  num_1.upper()
# except AttributeError as e :
#     print(e)

#overflow error

# result  = 10**1000
# print(result)

# import math

# try:
#     print(math.exp(1000))

# except OverflowError as e:
#     print(e)

# try:
#     result = 10.0 ** 1000
#     print(result)

# except OverflowError as e:
#     print(e)

#IOError (Base class for I/O-related errors):
# try:
#     file = open("abc.txt", "r")
#     data = file.read()

# except IOError as e:
#     print(e)

#runtime error

# age = -7

# if age < 0:
#     raise RuntimeError("Age cannot be negative")