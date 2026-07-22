


print("==== Student Grade repport====")

Students = ["Daan", "Alex", "Lena", "Ann", "Ruth", "George", "Kaya", "Kelly","Maria"]
Grades  = [75, 65, 40, 85, 55, 90, 45, 80, 50, 70]
for i in range(len(Students)):
    name = Students[i]
    grade = Grades[i]
    if grade >= 80:
        print(name ,grade, "Excellent")
    elif grade>= 60:
        print(name, grade, "Good")
    else:
        print(name, grade, "Need improvement")


average = sum(Grades)/len(Grades)
print("Average:", average)

print("Highest grade:", max (Grades))

print("Lowest grade:", min(Grades))
print("Number of student:", len(Students))
