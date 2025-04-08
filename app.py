name = input("enter your full name: ")
course = input("what program do you offer? ")
year = int(input("enter your current year: "))
p1 = input("what is your grade for operating systems? ")
p2 = input("what is your grade for database fundamentals? ")
p3 = input("what is your grade for computer networks? ")
p4 = input("what is your grade for critical thinking? ")
if p1 == 'A':
    gpa1 = 12 / 3
    print(gpa1)
elif p1 == 'B':
    gpa1 = 9 / 3
    print(gpa1)  
elif p1 == 'C':
    gpa1 = 6 / 3
    print(gpa1) 
else:
    print("N/A")

if p2 == 'A':
    gpa2 = 12 / 3
    print(gpa2)
elif p2 == 'B':
    gpa2 = 9 / 3
    print(gpa2)  
elif p2 == 'C':
    gpa2 = 6 / 3
    print(gpa2) 
else:
    print("N/A")

