class Human:
    def printinfo(self, name, age):
        self.name = name
        self.age = age
        print(f"Name: {self.name}, Age: {self.age}")


person = Human()
person.printinfo("侍", 23)
