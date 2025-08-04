class Employee:
    def __init__(self,id,name,basic):
        print('employee class')
        self._id=id
        self._name=name
        self._basic=basic
        
    def calculate(self):
        print('calculate from employee class')
        self._hra=self._basic*0.40
        self._da=self._basic*0.20
        self._pf=self._basic*0.12
        self._gross=(self._basic+self._hra+self._da)-self._pf
        
    def __str__(self):
        return f'Employee Info \nId={self._id}\nName={self._name}\nGross Salary={self._gross}'
    
# child class
class Manager(Employee):
    def __init__(self,id,name,basic,bonus):
        super().__init__(id,name,basic)
        print('manager class')
        self.__bonus=bonus  # private
        
        
    def calculate(self):
        super().calculate()
        print('calculate from manager class')
        self._gross=self._gross+self.__bonus
        
    def __str__(self):
        return f'Manager Info \nId={self._id}\nName={self._name}\nGross Salary={self._gross}'
    

class CEO(Employee):
    def __init__(self,id,name,basic,bonus):
        super().__init__(id,name,basic)
        print('CEO class')
        self.__bonus=bonus  # private
        
        
    def calculate(self):
        super().calculate()
        print('calculate from CEO class')
        self._ta=self._basic*0.05
        self._food=self._basic*0.04
        self._gross=self._gross+self.__bonus+self._ta+self._food
        
    def __str__(self):
        return f'CEO Info \nId={self._id}\nName={self._name}\nGross Salary={self._gross}'

    
m1=Manager(1,"Amol",45000,5000)
m1.calculate()
print(m1)

print('---------------------------------')
e1=Employee(2, "Ajay", 34000)
e1.calculate()
print(e1)
print('---------------------------------')
c1 = CEO(3, "xyz",500000,100000)
c1.calculate()
print(c1)