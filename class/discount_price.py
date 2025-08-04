# Create a class Product, assign value for product id, name, price

# If price is >2000  → 20% discount
# If price 1000- 2000  → 10% discount
# Price <1000           → 5% discount

# Display id, name actual price & discounted price 

class product:
    def __init__(self,product_id,name,price):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.__discounted_price = self.__cal_discounted_price()
        
    def __cal_discounted_price(self):
        if self.price > 2000:
            disc = 0.2
        elif 1000 <= self.price <= 2000:
            disc = 0.1
        else:
            disc = 0.05
            
        return self.price * (1 - disc)
        
    def display(self):
        print(f"Product id: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Discounted Price: {self.__discounted_price}")
        print("\n")
        
P1 = product(1,'abc',50)
P2 = product(2,'xyz',1500)
P3 = product(3,'bbb',3000)

P1.display()
P2.display()
P3.display()
