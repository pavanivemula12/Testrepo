class students:
    def __init__(self, name):
        self.name = name
        self.marks = []
    def enterMarks(self):
        for i in range(3):
            m = int(input("Enter the marks of %s in %d subject: "%(self.name, i+1)))
            self.marks.append(m)
    def display(self):
        print(self.name, "got", self.marks)
name = input("Enter the name of student:")
s1 = students(name)
s1.enterMarks()
s1.display()
name = input("Enter the name of student:")
s2 = students(name)
s2.enterMarks()
s2.display()
name = input("Enter the name of student:")
s3 = students(name)
s3.enterMarks()
s3.display()

