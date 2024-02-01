
import sys
class Person:
    def __init__(self, Name, lastName):
        self.Name = Name
        self.lastName = lastName
    def __str__(self):
        return f'{self.Name} {self.lastName}'

class Student(Person):
    def __init__(self,Name, lastName):
        super().__init__(Name, lastName)
        self.course = None
    def __str__(self):
        if self.course == None:
            return f'{self.Name} {self.lastName} is not registered to any course'
        else:
             return f'{self.Name} {self.lastName} is registered to {self.course}'
    def setCourse(self, course):
        self.course = course



if __name__ == "__main__":
    if  len(sys.argv) > 1:
        print("No argoumets")
        sys.exit(1)
    Name = input("Insert first name: ")
    lastName = input("Insert last name: ")
    y_n = None
    i = 0
    while(y_n != "y" and y_n != "n"):
        if i == 0:
            y_n = input("Are you a student?(y/n)")
        else:
            y_n = input('Please type "y" or "n":')
        i += 1
    if y_n == "y":
        course = input("Please insert your degree course: ")
        People = Student(Name, lastName)
        People.setCourse(course)
    else:
        People = Person(Name, lastName)

    print(People)

    