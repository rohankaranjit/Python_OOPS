class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def average(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Your average score is" , sum/3)


s1 = Student("Rohan",[99,95,93])
s2 = Student("NIsha", [88,78,53])   
s1.average()
s2.average()