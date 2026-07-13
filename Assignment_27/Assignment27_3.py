class Numbers:

    def __init__(self,val):
        self.Value = val
    
    def ChkPrime(self):
        if self.Value <= 1:
            return False
        
        for i in range(2,self.Value):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        sum = 0
        for i in range(1,self.Value):
            if self.Value % i == 0:
                sum =sum + i
        
        if sum == self.Value:
            return True
        else:
            return False

    def Factors(self):
        print("Factors are : ",end= " ")
        for i in range(1,self.Value):
            if self.Value % i == 0:
                print(i,end = " ")
        print()

    def SumFactors(self):
        sum = 0
        for i in range(1,self.Value):
            if self.Value % i == 0:
                sum = sum + i
        return sum
 
obj1 = Numbers(21)
obj2 = Numbers(12)
obj3 = Numbers(5)

print("========Object 1 ==========")
print("Number is prime : ",obj1.ChkPrime())
print("Number is perfect : ",obj1.ChkPerfect())
obj1.Factors()
print("Sum of factors : ",obj1.SumFactors())

print()

print("========Object 2 ==========")
print("Number is prime : ",obj2.ChkPrime())
print("Number is perfect : ",obj2.ChkPerfect())
obj2.Factors()
print("Sum of factors : ",obj2.SumFactors())

print()

print("========Object 3 ==========")
print("Number is prime : ",obj3.ChkPrime())
print("Number is perfect : ",obj3.ChkPerfect())
obj3.Factors()
print("Sum of factors : ",obj3.SumFactors())