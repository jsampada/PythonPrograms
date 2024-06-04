class plane:
    def flying(self):
        print("plane is flying")
    def takingof(self):
        print("plane is taking off")
    def landing(self):
        print("plane is landing")
class cargo(plane):
    def carryc(self):
        print("plane is carrying cargos")
class passenger(plane):
    def carrypas(self):
        print("plane is carring passenger")

class fighter(plane):
    def carryw(self):
        print("plane is carring w")

c=cargo()
p=passenger()
f=fighter()
c.flying()
c.takingof()
c.landing()
c.carryc()
p.landing()
p.flying()
p.carrypas()
f.carryw()