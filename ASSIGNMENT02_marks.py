# Write a program to store marks of 5 students in ascending order in a list

b1=int(input("Enter the marks of student-1: "))
b2=int(input("Enter the marks of student-2: "))
b3=int(input("Enter the marks of student-3: "))
b4=int(input("Enter the marks of student-4: "))
b5=int(input("Enter the marks of student-5: "))

b=[b1,b2,b3,b4,b5]

b.sort()
print(b)