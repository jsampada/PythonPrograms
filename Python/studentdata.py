
class department:
    def __init__(self):
        self.dep_name=dep_name
        self.student_name=student_name
        self.roll_no=roll_no

        dep_name = input("enter dep_name: ")
        student_name = input("enter student name:")
        roll_no = int(input("enter roll_no"))
    def show(self):
        print("dep name is:", dep_name)
        print("student name is:", student_name)
        print("roll no is", roll_no)
d=department()
d.show()



