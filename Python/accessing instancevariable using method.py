class student:
    def __init__(self):
        self.name="sampada"
        self.age=22
        self.place="pune"
    def print_name(self):
        print(self.name)
        print(self.age)
        print(self.place)
        print(self.phone)
s1=student()
print(s1.name)
print(s1.age)
print(s1.place)
s1.phone=9422
s1.print_name()