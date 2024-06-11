class os:
    def __init__(self):
        self.status=True
        print("os is ready")
    def getos(self):
        print("os is installing")

class mobile:
    def __init__(self,name):
        self.name=name
        self.o=os()
        print("mobile is ready")
        print("os is installed")
m=mobile("iphone")
print(m.o.status)
print(m.o.getos)
print(m.name)
del m
print("after del")
print(m.name)