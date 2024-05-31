class Student:
    def __init__(self):
        self.__name1=''
        self.__name2=''
        self.__name3=''
    def setdata(self,value1,value2,value3):
        self.__name1=value1
        self.__name2=value2
        self.__name3=value3
    def getdata(self):
        return self.__name1,self.__name2,self.__name3
res=[]
s=Student()
s.setdata('sampada',"anil",'joshi')
res=s.getdata()
print(res)
print(type(res))
