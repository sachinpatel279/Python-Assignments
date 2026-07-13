class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
    
    def Accept(self):
        self.Value1 = int(input("Enter first number : "))
        self.Value2 = int(input("Enter second number : "))
    
    def Addition(self):
        return self.Value1 + self.Value2
    
    def Substraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value1 > 0 and self.Value2 > 0:
            return self.Value1 / self.Value2
        

obj1 = Arithmetic()
obj2 = Arithmetic()
obj3 = Arithmetic()

print("------Display first arithmetic operation----------")
obj1.Accept()
print("Addition is : ",obj1.Addition())
print("Substraction is : ",obj1.Substraction())
print("Multiplication : ",obj1.Multiplication())
print("Division is : ",obj1.Division())

print()

print("="*30)
print("------Display second arithmetic operation----------")
obj2.Accept()
print("Addition is : ",obj2.Addition())
print("Substraction is : ",obj2.Substraction())
print("Multiplication : ",obj2.Multiplication())
print("Division is : ",obj2.Division())

print()

print("="*30)
print("------Display third arithmetic operation----------")
obj3.Accept()
print("Addition is : ",obj3.Addition())
print("Substraction is : ",obj3.Substraction())
print("Multiplication : ",obj3.Multiplication())
print("Division is : ",obj3.Division())

