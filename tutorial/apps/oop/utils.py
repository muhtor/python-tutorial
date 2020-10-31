

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
        name = f"My name is ...{self.name}"
        # return print("print_name:...", name, type(name))


class Person:
    def __init__(self, *args, **kwargs):
        # print("**kwargs... ", kwargs, type(kwargs))
        self.name = kwargs.get('name', '')
        self.age = kwargs.get('age', '')

    def create_person(self):
        person = f"Person name: {self.name} / Person age: {self.age}"
        return print("create_person:...", person, type(person))


class George(Person):

    def get_person(self):
        super().__init__(name='muhtor', age=25)
        self.create_person()


George().get_person()

# print("Human...", George().create_person(), type(George().create_person()))
# print("Human...", hm, type(hm))


if __name__ == '__main__':
    # Student.print_name = classmethod(Student.print_name)
    Student.method_cls()