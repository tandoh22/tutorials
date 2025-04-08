# cgpa calculation
name = input("enter your full name: ")
course = input("what program do you offer? ")
year = input("enter your current year: ")
p1 = input("what is your grade for operating systems? ")
p2 = input("what is your grade for database fundamentals? ")
p3 = input("what is your grade for computer networks? ")
p4 = input("what is your grade for critical thinking? ")
if p1 == 'A':
    gpa1 = 12 / 3
    print(f"your gpa for operating systems is {gpa1}")
elif p1 == 'B':
    gpa1 = 9 / 3
    print(f"your gpa for operating systems is {gpa1}")  
elif p1 == 'C':
    gpa1 = 6 / 3
    print(f"your gpa for operating systems is {gpa1}") 
else:
    print("N/A")

if p2 == 'A':
    gpa2 = 12 / 3
    print(f"your gpa for database fundamentals is {gpa2}")
elif p2 == 'B':
    gpa2 = 9 / 3
    print(f"your gpa for database fundamentals is {gpa2}")  
elif p2 == 'C':
    gpa2 = 6 / 3
    print(f"your gpa for database fundamentals is {gpa2}") 
else:
    print("N/A")

if p3 == 'A':
    gpa3 = 12 / 3
    print(f"your gpa for computer networks is {gpa3}")
elif p3 == 'B':
    gpa3 = 9 / 3
    print(f"your gpa for computer networks is {gpa3}")  
elif p2 == 'C':
    gpa3 = 6 / 3
    print(f"your gpa for computer networks is {gpa3}") 
else:
    print("N/A")

if p4 == 'A':
    gpa4 = 12 / 3
    print(f"your gpa for computer critical thinking is {gpa4}")
elif p4 == 'B':
    gpa4 = 9 / 3
    print(f"your gpa for computer critical thinking is {gpa4}")  
elif p4 == 'C':
    gpa4 = 6 / 3
    print(f"your gpa for computer critical thinking is {gpa4}") 
else:
    print("N/A")

total_gpa = (gpa1 + gpa2 + gpa3 + gpa4) / 4
print(f"your current CGPA is {total_gpa}")