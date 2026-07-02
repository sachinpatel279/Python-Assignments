import sys

value = input("Enter a value :")

print("Data Type : ",type(value))
print("Memory Address : ",id(value))
print("Size in bytes : ",sys.getsizeof(value))

#output : - 
#Enter a value :10
#Data Type :  <class 'str'>
#Memory Address :  2396687322592
#Size in bytes :  43 