# Create a class IncomeTax

# Accept the annual income

# 0- 5lcs  → 0 % tax
# 5- 10  → 20% tax
# 10-15 → 40%
# Above 15 → 45 % tax

# Display name of person, annual income  & tax amount to pay


class IncomeTax:
    def __init__(self,name,income):
        self.name = name
        self.income = income
        self.__tax = self.__cal_tax()
        
    def __cal_tax(self):
        if self.income <= 500000:
            tax = 0
        elif self.income <= 1000000:
            tax = (self.income - 500000)*0.2
        elif self.income <=1500000:
            tax = 100000 + (self.income - 1000000)*0.4
        else:
            tax = 300000 + (self.income-1500000)*0.45
            
        return tax
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Income: {self.income}")
        print(f"Tax to pay: {self.__tax}")
        print("\n")
        
p1 = IncomeTax("abc", 2000000)
p2 = IncomeTax("xyz", 50000)
p3 = IncomeTax("ddd", 1200000)

p1.display()
p2.display()
p3.display()
        