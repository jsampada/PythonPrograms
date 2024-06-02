class Student:
    def __init__(self):
        self.__name = ''
    def getter(self):
        return self.__name
    def setter(self,value):
        self.__name = value
    getset=property(setter,getter)
s1=Student
s1.getset = 'sampada'
res = s1.getset
print(res)
