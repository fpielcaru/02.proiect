from student import Student
import os 

def scrie_in_fisier(studenti):
    fisier = open("studenti.txt", "a")
    fisier.write(str(studenti) + "\n")
    fisier.close()

def citire_in_fisier():
    fisier = open("studenti.txt", "r")
    studenti = []
    for line in fisier:
        studenti.append(line.strip())
    fisier.close()
    return studenti

student1 = Student("Ana Popescu", 16, 9.5, "10A")
student2 = Student("Mihai Ionescu", 17, 8.0, "11B")
student3 = Student("Elena Georgescu", 16, 9.8, "10A")

student = []
student.append(student1)
student.append(student2)
student.append(student3)

for s in student:
    print(s)