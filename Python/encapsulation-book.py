class Book:
    def __init__(self,value):
        self.page=value
    def setdata(self,value):
        if(value>0):
            self.page=value
    def getdata(self):
        return self.page
b=Book(100)
print(b.page)
b.setdata(114)
pg=b.getdata()
print(pg)
b.setdata(-99)
a=b.getdata()
print(a)