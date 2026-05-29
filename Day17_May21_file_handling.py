#mode = 'r'

# file = open("demo.txt",mode='r')
# read_data = file.read() #read entire file
# print(read_data)
# file.close()

# file = open("demo.txt",mode = 'r')
# read_data = file.readline() # will read first single line
# print(read_data)
# file.close()

# file = open("demo.txt",mode='r')
# read_data = file.readlines()
# print(read_data)
# file.close()

#mode = 'a'
# file = open("demo.txt",mode='a')
# write_data = file.write("\nwrite operations perfrmd by using mode = a ")
# file.close()

# #mode = 'a'
# file = open("demo1.txt", mode = 'a')
# write_data = file.write("write operations perfrmd by using mode = a ")
# file.close()

#mode ='w' to create a file

# file = open("demo2.txt",mode='w')
# write_data = file.write("write operations perfrmd by using mode = hi ")
# file.close

# voter_data = ["naren\n","eeshu\n","vinnu\n"]
# file = open("demo1.txt",mode='w')
# write_data = file.writelines(voter_data)
# file.close()


# file = open("sample.txt",mode= 'w+')
# write_data = file.write("eeshwar vinnu")
# print(file.tell())
# file.seek(0)
# read_data = file.read(8)
# print(read_data)
# file.close() 

# file = open("demo.txt",mode='r')
# read_data = file.readlines()
# print(read_data)
# print(read_data[2])
# file.close()

# import os

# fn = "demo.txt"
# nn = "samp.text"

# os.rename(fn,nn) 

# import os
# os.remove("demo2.txt")

# file = open("C:\\Users\\naren\\OneDrive\\Desktop\\naren.txt", mode = 'r')
# read_data = file.read()
# print(read_data)
# file.close() 


# mode a+

# file = open ("demo1.txt", mode = 'a+')
# write_data = file.write("\nprathibha")
# print(file.tell())
# file.seek(0)
# read_data = file.read()
# print(read_data)
# file.close()

# file = open("naren.txt",mode = 'a+')
# write_data = file.write("welcome to my world")

# print(file.tell())
# file.seek(0)
# read_data = file.read()
# print(read_data)
# file.close()

# mode = r+

# file = open ("eeshu.text",mode='r+')
# write_data = file.write("dhurandhar")
# file.close()  # r+ mode will not create new file

# file = open ("samp.txt", mode = 'r+')
# write_data = file.write("fa")
# print(write_data)
# # print(file.tell())
# # file.seek(0)
# # read_data = file.read()
# # print(read_data)

