class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printinfo(self):
        print(f"Name: {self.name}, Age: {self.age}")


person = Human("侍",23)
person.printinfo()
