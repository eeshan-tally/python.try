#Combination formula
from  pyfactorial import Assignment1

class Combination :
    def __init__(self):
        self.n=Assignment1()
        self.r=Assignment1()
    def calculate(self):
        self.nvalue=self.n.take_input("Enter the n value")
        self.rvalue=self.r.take_input("Enter the r value")
        self.n.Factorial()
        self.r.Factorial()
        self.storen=self.n.display_result()
        self.storer=self.r.display_result()
        if self.nvalue<self.rvalue:
            print("Sorry!!, r value is greater than n value ")
        else:
            self.jvalue=self.nvalue - self.rvalue 
            self.j=Assignment1()
            self.j.Factorial(self.jvalue)
            self.storedj=self.j.display_result()
            self.ncr=self.storen // (self.storer * self.storedj )
            print("The Combination value is ",self.ncr)
check1=Combination()
check1.calculate()
