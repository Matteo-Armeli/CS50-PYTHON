#introducing dict for keys and values (dictionary for words and definitions)
students = {
    "Hermione": "Gryffindor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor",
    "Draco": "Slytherin"}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

#or we can use a loop but it will print only the keys (names of the students)
for student in students:
    print(student)

#to print both
for student in students:
    print(student, students[student], sep=", ")

#more dict adding the patronus
students = [ 
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Rusell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": "None"}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")