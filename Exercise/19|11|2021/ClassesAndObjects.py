class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality

    def print(self):
        print("My name is " + self.name + " " + self.family + ".\nI am " + str(
            self.age) + " years old from " + self.nationality)


class Student(Person):

    def __init__(self, name, family, age, nationality, university, yearOfStudy):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.yearOfStudy = yearOfStudy

    def print(self):
        print("My name is " + self.name + " " + self.family + ".\nI am " + str(
            self.age) + " years old from " + self.nationality + "\nI am student in "
              + self.university + " for the " + self.yearOfStudy + " year\n")


class Lecturer(Person):

    def __init__(self, name, family, age, nationality, university, experience):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.experience = experience

    def print(self):
        print("My name is " + self.name + " " + self.family +
              ".\nI am " + str(self.age) + " years old from " + self.nationality +
              "\nI am lecture in " + self.university + " for the " + self.experience + " year\n")


person = Person("Pesho", "Petrov", 32, "Bulgaria")
student = Student("Pesho", "Petrov", 32, "Bulgaria", "Technical University", "second")
lecture = Lecturer("Dimitar", "Dimitrov", 45, "Bulgaria", "Technical University", "fifth")
student.print()
lecture.print()
