""""no=input("enter any no:")
print(int(no[0])+int(no[1]))"""


"""weight=float(input("enter weight"))
height=float(input("enter height"))
Bmi=weight/height**2
print(Bmi)
bmi1=int(Bmi)
print(bmi1)"""

'''Create a program using maths and f-Strings that tells us how many days, weeks, 
months we have left if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:
You have x days, y weeks, and z months left.
Where x, y and z are replaced with the actual calculated numbers.
Hint
1) There are 365 days in a year, 52 weeks in a year and 12 months in a year.
2) Try copying the example output into your code and replacing the relevant
 parts so that the sentence is formated the same way.'''

age=input("enter your age:")
Age_x=100-int(age)
days=Age_x*365
weeks=Age_x*52
month=Age_x*12
print("you have",days, "days and",weeks,"weeks and",month,"months to live")
