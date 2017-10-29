class Staff:
    def __init__(self,name,salary,yob):
        self.name=name
        self.salary=salary
        self.yob=yob
    def showname(self):
        print("name od the staff is:",self.name)
    def showsalary(self):
        print("salary of the staff is:",self.salary)
    def showyob(self):
        print("year of birth is:",self.yob)
    def showid(self):
        print("id:",self._id)
stf1=Staff("abhishek",50000,1996,"apabhishek")
stf2=Staff("abhinav",70000,1991,"abhim")
stf1.showname()
class Doctors(Staff):
    def __init__(self,name,salary,yob,id,speciality):
        super().__init__(name,salary,id,yob)
        self.speciality=speciality
    def showspec(self):
        print("speciality is;",self.speciality)
stf3=Doctors("ananya",60000,1997,"ananyag","phisician")
stf3.showspec()
stf3.showid()
class Nurse(Staff):
    def __init__(self,name,salary,yob,section):
        super().__init__(name,salary,yob,id)
        self.section=section
    def showsection(self):
        print("section of nurse is:",self.section)
stf4=Nurse("anamika",30000,1997,"OPD")
stf4.showsection()
