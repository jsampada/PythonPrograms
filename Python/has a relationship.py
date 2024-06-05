class radio:
    def turnon(self,x):
        if(x == 1):
            print("radio is on")
        else:
            print("radio is off")

class car:
    def __init__(self,min,max):
        self.min = min
        self.max = max
        self.r = radio()

c1=car(60,2000)
print(c1.min)
print(c1.max)
c1.r.turnon(1)