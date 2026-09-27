# Week 3 - Python OOP Assignment
# Topics: Classes, Objects, Inheritance, Polymorphism


# 1. CLASS AND OBJECT

class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def display_info(self):
        print("Name:", self.name)
        print("Course:", self.course)


# Creating objects
student1 = Student("Namrata", "B.Tech CSE Cyber Security")
student2 = Student("Rahul", "B.Tech CSE")

print("----- Classes and Objects -----")
student1.display_info()

print()
student2.display_info()


# 2. INHERITANCE

class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)


class StudentPerson(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def show_course(self):
        print("Course:", self.course)


print("\n----- Inheritance -----")

student3 = StudentPerson("Namrata", "Cyber Security")

student3.show_name()
student3.show_course()


# 3. POLYMORPHISM

class PythonDeveloper:
    def work(self):
        print("Python Developer writes Python programs.")


class CyberSecurityExpert:
    def work(self):
        print("Cyber Security Expert protects computer systems.")


class DataAnalyst:
    def work(self):
        print("Data Analyst analyzes data.")


print("\n----- Polymorphism -----")

developers = [
    PythonDeveloper(),
    CyberSecurityExpert(),
    DataAnalyst()
]

for developer in developers:
    developer.work()