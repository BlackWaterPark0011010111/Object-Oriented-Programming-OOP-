#dataclasses for simplicity and typing for annotations.


from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Student:
    name: str
    age: int
    grade: int

    def __str__(self) -> str:
        return f"Student: {self.name}, Age: {self.age}, Grade: {self.grade}"

@dataclass
class Teacher:
    
    name: str
    subject: str
    years_of_experience: int

    def __str__(self) -> str:
        return f"Teacher: {self.name}, Subject: {self.subject}, Experience: {self.years_of_experience} years"



@dataclass

class Course:
    name: str
    teacher: Teacher
    students: List[Student]

    def add_student(self, student: Student) -> None:
        if student not in self.students:
            self.students.append(student)
            print(f"Added {student.name} to {self.name}.")
        else:
            print(f"{student.name} is already in {self.name}.")

    def remove_student(self, student: Student) -> None:
        if student in self.students:
            self.students.remove(student)
            print(f"Removed {student.name} from {self.name}.")
        else:
            print(f"{student.name} is not in {self.name}.")

    def list_students(self) -> None:
        print(f"Students in {self.name}:")
        for student in self.students:
            print(f"- {student.name}")

    def __str__(self) -> str:
        return f"Course: {self.name}, Teacher: {self.teacher.name}, Students: {len(self.students)}"
    


@dataclass

class School:
    name: str
    courses: List[Course] = None

    def __post_init__(self):
        if self.courses is None:
            self.courses = []

    def add_course(self, course: Course) -> None:
        if course not in self.courses:
            self.courses.append(course)
            print(f"Added course {course.name} to {self.name}.")
        else:
            print(f"Course {course.name} already exists in {self.name}.")

    def remove_course(self, course: Course) -> None:
        if course in self.courses:
            self.courses.remove(course)
            print(f"Removed course {course.name} from {self.name}.")
        else:
            print(f"Course {course.name} is not in {self.name}.")

    def list_courses(self) -> None:
        print(f"Courses in {self.name}:")
        for course in self.courses:
            print(f"- {course.name} (Teacher: {course.teacher.name})")

    def __str__(self) -> str:
        return f"School: {self.name}, Courses: {len(self.courses)}"

# Let's test the system.

#Create students
student1 = Student(name="Alice", age=15, grade=9)
student2 = Student(name="Bob", age=16, grade=10)
student3 = Student(name="Charlie", age=14, grade=8)
## Create a teacher
teacher1 = Teacher(name="Mr. Smith", subject="Math", years_of_experience=10)
## Create a course and add students
math_course = Course(name="Mathematics", teacher=teacher1, students=[])
math_course.add_student(student1)
math_course.add_student(student2)
math_course.add_student(student3)

#add the same student again
math_course.add_student(student1)
# List students
math_course.list_students()
#  Remove a student
math_course.remove_student(student2)
math_course.list_students()
#Create a school
school = School(name="High School")
school.add_course(math_course)#add the course
#List courses
school.list_courses()
# removing a course that doesn't exist
fake_course = Course(name="Fake Course", teacher=teacher1, students=[])
school.remove_course(fake_course)
#school details
print(school)
# course details.
print(math_course)
#teacher details
print(teacher1)
#student details
print(student1)
print(student2)
print(student3)

