# TUPLES

# tup=(85,69,23,45,78,75,72,15,45,96,45,48,72,23,56,96,74,12,45)
# print(tup)

# Accessing value from tuple with help of index
# tup=(85,69,23,45,78,75,72,15,45,96,45,48,72,23,56,96,74,12,45)
# print(tup[12])

#Empty tuple
# tup=()
# print(tup)

#Single value in tuple always separeted by comma 
# or it will assume as integer not value of tuple
# tup=(2,)
# print(tup)

#Slicing in Tuple
# tup=(85,69,23,45,78,75,72,15,45,96,45,48,72,23,56,96,74,12,45)
# print(tup[5:15])

#Methods in tuple
# 1) Index method
# tup=(85,69,23,45,78,75,72,15,45,96,45,48,72,23,56,96,74,12,45)
# num=tup.index(15)
# print(num)

# 2) Count method
# tup=(85,69,23,45,78,75,72,15,45,96,45,48,72,23,56,96,74,12,45)
# num=tup.count(15)
# print(num)

#PRACTICE QUESTIONS
# 1)Append movie names in list from user
# movies=[]
# n1=str(input("Enter 1st movie name :"))
# n2=str(input("Enter 2nd movie name :"))
# n3=str(input("Enter 3rd movie name :"))
# movies.append(n1)
# movies.append(n2)
# movies.append(n3)
# print(movies)

# 2)Palindrome in list
# n1=int(input("Enter 1st number :"))
# n2=int(input("Enter 2nd number :"))
# n3=int(input("Enter 3rd number :"))
# pal=[]
# pal.append(n1)
# pal.append(n2)
# pal.append(n3)
# print(pal)
# c1=pal.copy()
# c1.reverse()
# if(c1==pal):
#     print("palindrome")
# else:
#     print("not palindrome")

# 3)Count number of occurance in tuple
# a=(85,69,15,45,78,15,72,15,45,96,15,48,72,23,15,96,74,15,45)
# print(a.count(15))

# 4) Store values in list and sort in ascending order
# pal=[]
# n1=int(input("Enter 1st number :"))
# n2=int(input("Enter 2nd number :"))
# n3=int(input("Enter 3rd number :"))
# n4=int(input("Enter 4th number :"))
# n5=int(input("Enter 5th number :"))
# pal.append(n1)
# pal.append(n2)
# pal.append(n3)
# pal.append(n4)
# pal.append(n5)
# print(pal)
# pal.sort()
# print("sorted list :",pal)
