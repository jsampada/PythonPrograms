class Demo:
    z=100
    def __init__(self):
        self.x=4
        self.y=5
    def display(self):
        print(self.z)
        print(self.y)
    @staticmethod
    def disstatic():
        print(Demo.z)
    @classmethod
    def disclass(cls):
        print(cls.z)