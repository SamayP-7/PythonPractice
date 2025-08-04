class Book:
    __id=None
    __name=None
    __price=None
    
    # setters
    
    def setId(self,id):
        self.__id=id
    
    def setName(self,name):
        self.__name=name
    
    def setPrice(self,price):
        self.__price=price
        
    # getters
    def getId(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def getPrice(self):
        return self.__price
    
    
    def __str__(self):
        return f'Id= {self.__id}, Name={self.__name}, Price={self.__price}'
    
b1 = Book()

b1.setId(101)
b1.setName('python')
b1.setPrice(1000)

print(b1.getId())
print(b1.getName())
print(b1.getPrice())

print(b1)