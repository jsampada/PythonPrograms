class Book:
    def __init__(self,value):
        self.__pages=value
    def setdata(self,value):
        self.__pages=value
    def getdata(self):
        return  self.__pages
b=Book(100)
res=b.getdata()
print(res)
b.setdata(114)
result=b.getdata()
print(result)