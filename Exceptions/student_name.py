class ReQNameError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Student:
    def __init__(self, name=None):
        if not name or name.isspace():
            raise ReQNameError("name is required")
        self.name = name

try:
    
    s1 = Student("")  
    
except ReQNameError as e:
    print(f"Error: {e}")
    
else:
    print(f"Student name: {s1.name}")
