class Student:

    def __init__(self):

        self.__name = ''

    @property
    def dataAccess(self):

        return self.__name

    @dataAccess.setter
    def dataAccess(self , value):

        self.__name = value

s1 = Student()


s1.dataAccess = 'sampada'
res=s1.dataAccess
print(res)
