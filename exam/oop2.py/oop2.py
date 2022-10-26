from atexit import register


class Employee:
    def __init__(self, name, age, empcode, gender, phoneno):
        self.name = name
        self.age = age
        self.empcode = empcode
        self.gender = gender
        self.phoneno = phoneno

    # def employee():
    # def getters():
    # def setters():
    def calculateSalary(basic_salary, PF, gratuity):
        salary = basic_salary-PF+gratuity
        return salary
class permanentEmployees(Employee):
        def __init__(self, name, age, empcode, gender, phoneno):
            super().__init__(name, age, empcode, gender, phoneno)
            # self.a=name
            insureAmount=5000
            return

        def display_per(self):
            print(self.name, self.age, self.empcode, self.gender, self.phoneno)



class contractEmployees(Employee):
        def __init__(self, name, age, empcode, gender, phoneno,salary):
            super().__init__(name, age, empcode, gender, phoneno)
            self.salary = salary
            insureAmount=3000

        def display_con(self):
            print(self.name, self.age, self.empcode, self.gender, self.phoneno, self.salary)


permanent_employee=permanentEmployees('john', 35, 1001, 'male', 123678)
permanent_employee.display_per()
contract_employee=contractEmployees('mary', 24, 1002, 'female', 9823672, 10000)
contract_employee.display_con()

class Customers:
    def __init__(self, name, place, phone, email):
        self.a=name
        self.b=place
        self.c=phone
        self.d=email


    def display_customer(self):
        print(self.a,self.b,self.c,self.d)


customer1=Customers('ram','calicut',9823123,'ram@gmail.com')
customer1.display_customer()


class Insurance:
    def __init__(self, insuranceNo, insureAmount, totalEMI):
        self.no=insuranceNo
        self.amount=insureAmount
        self.total=totalEMI

    def  registerInsurance():
        insureAmount=5000


         

    


