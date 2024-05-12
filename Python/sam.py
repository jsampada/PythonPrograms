
class person:


    def __init__(self,nam,ag,cit):
        self.name=nam
        self.age=ag
        self.city=cit

    def info(self):
        print(f"name is : {self.name} age is : {self.age} city is : {self.city}")


n = input("enter name")
a = int(input("enter age"))
c = input("enter city")
p=person(n,a,c)
p.info()