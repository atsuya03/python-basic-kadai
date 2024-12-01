class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_adult(self):
        if self.age >= 20:
            print(f"{self.name}は大人です。")
        else:
            print(f"{self.name}は大人ではありません。")

human_list = [
    Human("侍花子", 19),
    Human("サムライ武太郎", 25),
    Human("山田太郎", 18),
    Human("田中花子", 22)
]

for human in human_list:
    human.check_adult()



    

