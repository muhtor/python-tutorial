

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add_person(self):
        person_name = self.name
        person_age = self.age
        return person_name, person_age


class John(Person):

    person = Person(name='kimdir', age=20)

    def sos(self):
        person = super(John, self).add_person()
        print("Person...", person)


class Student:

    name = "muhtor"

    @classmethod
    def method_cls(cls):
        return cls().print_name()

    def print_name(self):
        return print("My name is ...", self.name)


if __name__ == '__main__':
    # Student.print_name = classmethod(Student.print_name)
    Student.method_cls()