class Human:
    def __init__(self):
        self.name=""
        self.age=""

    def printinfo(self,name,age):
        self.name=name
        self.age=age
        print(f"Name: {self.name}, Age: {self.age}")


person = Human()
person.printinfo("侍", 23)
