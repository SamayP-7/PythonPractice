# Create a class Circle accept the value of radius & initialise using initializer

# Calculate the area of circle

class circle:
    def __init__(self,r):
        self.__radius = r
        self.__area = self.__cal_area()
        
    def __cal_area(self):
        return 3.14 * self.__radius * self.__radius
    
    def display(self):
        print(f"Area of circle with radius = {self.__radius} is {self.__area:.2f}")
        
c1 = circle(10)
c2 = circle(5)

c1.display()
c2.display()
