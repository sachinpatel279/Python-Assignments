class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0
    
    def Accept(self):
         self.Radius = float(input("Enter radius : "))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CaluculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius
    
    def Display(self):
        print("Radius : ",self.Radius)
        print("Area : ",self.Area)
        print("Circumference : ",self.Circumference)

obj1 = Circle()
obj2 = Circle()

print("Display first circle ")
obj1.Accept()
obj1.CalculateArea()
obj1.CaluculateCircumference()
obj1.Display()

print("-"*30)

print("Display second circle ")
obj2.Accept()
obj2.CalculateArea()
obj2.CaluculateCircumference()
obj2.Display()


