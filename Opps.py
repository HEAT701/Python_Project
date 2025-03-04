class Student_Detelis:
    def __init__(self):
        self.Roll_Number = []
        self.Name = []
        self.DepartMent = []
        self.Year = []
    def add_Studnet(self):
        Roll_Nmber = int(input("Enter The Roll Number"))
        Name = input("Enter The Studnet Name :")
        Department = input("Enter The Studnet Dipartment")
        Year = int(input("Enter The Years Of Studnet"))
        self.Roll_Number.append(Roll_Nmber),self.Name.append(Name),self.DepartMent.append(Department),self.Year.append(Year)
    def Print_Detelis(self):
        print(f"My Name  is: {self.Name} And My roll Number is: {self.Roll_Number}")
        print(f"I Study in {self.DepartMent} : I am in {self.Year} Student")
class Subject_Marks(Student_Detelis):
    def __init__(self):
        super().__init__()
        self.Math = []
        self.Phy = []
    def add_marks(self):
        Math = int(input("Enter The Math Marks: "))
        Phy = int(input("Enter the phy Marks: "))
        self.Math.append(Math), self.Phy.append(Phy)
    def Print_Student_detelis(self):
        print(f"My Math Marks is  {self.Math}")
Stu_1 = Student_Detelis()
Stu_1.add_Studnet()
Mark= Subject_Marks()
Mark.add_marks()
Stu_1.Print_Detelis()
Mark.Print_Student_detelis()