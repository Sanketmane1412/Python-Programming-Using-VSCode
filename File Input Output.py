# Read the file
# f=open("demo.txt","r")
# data=f.read() 
# print(data)
# f.close()

# Read Lines of file
# f=open("demo.txt","r")
# data1=f.readline()
# data2=f.readline()
# print(data2)

# Reas lines with passing parameter
# f=open("demo.txt","r")
# data=f.read(5) 
# print(data)
# f.close()


# Write the file means it truncate existing info in file and add new one
# f=open("demo.txt","w")
# data=f.write("Hello\nI'm a boy\nWe live in pune.") 
# f.close()

# Append in file
# f=open("demo.txt","a")
# data=f.write("\nfrom maharashtra") 
# print(data)
# f.close()

# WITH syntax in file handling
# with open("demo.txt","r") as f:
#     data=f.read()
#     print(data)

# Deleting file
# import os
# os.remove("demo1.txt")

# Practice Questions
# 1)WAF that replaces all occurances of java with python in a file
# with open("demo.txt","r") as f:
#     data=f.read()
#     print(data)
#     new=data.replace("java","python")
#     print(new)
# with open("demo.txt","w") as f:
#     f.write(new)

# 2) Search if the word "learning" exist in the file or not
# def check_word():
#     word="learning"
#     with open("demo.txt","r") as f:
#         data=f.read()
#         if(word in data):
#             print("found")
#         else:
#             print("not found")

# check_word()

# 3)Search if the word "learning" exist in the file or not amd exact line number of occurance
# def check_word():
#     word="learning"
#     data=True
#     line=1
#     with open("demo.txt","r") as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print("found",line)
#             line+=1
#     return -1

# check_word()

# 4)try,except,finally
# try:
#     x=10/0
# except ZeroDivisionError:
#     print("you cant divide by zero")
# finally:
#     print("any work can performed")