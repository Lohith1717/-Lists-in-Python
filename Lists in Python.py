students = []

n = int(input("How many students? "))

for i in range(n):
    name = input("Enter student name: ")
    students.append(name)

print("\nStudent List:")
for name in students:
    print(name)
