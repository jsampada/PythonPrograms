

class branch:
    def __init__(self,branch_name,year):
        self.branch_name=branch_name
        self.year=year
    def display(self):
        print("the branch name is.",self.branch_name)
        print("the year is.",self.year)
b=branch('DS',2021)
b.display()