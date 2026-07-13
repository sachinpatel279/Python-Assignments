class Demo :
    #class variable
    value = 10

    def __init__(self,A,B):
        #instance variable
        self.No1 = A
        self.No2 = B

    def Fun(self):
        print("Inside Fun ")
        print(self.No1)
        print(self.No2)

    def Gun(self):
        print("Inside Gun")
        print(self.No1)
        print(self.No2)

obj1 = Demo(11, 21)
obj2 = Demo(51, 101)

obj1.Fun()
obj2.Fun()

obj1.Gun()
obj2.Gun()