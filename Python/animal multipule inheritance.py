class animal:
    def eat(self):
        print("animals  are eating")
    def sleep(self):
        print("animals are sleeping")
    def run(self):
        print("animals are sleeping")
class monkey(animal):
    def eat(self):
        print("monkey is eating")
class deer(animal):
    pass
class tiger(animal):
    def eat(self):
        print("tiger is eating")

m=monkey()
d=deer()
t=tiger()
m.eat()
d.eat()
d.run()
m.sleep()
m.run()
t.run()
t.eat()