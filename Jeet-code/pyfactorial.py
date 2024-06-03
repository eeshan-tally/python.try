

class factorialClass:
   
#integerInput is a method to invalidate non integer inputs recusrsively until valid integer inputs are provided.
    
   def integerInput(self):
      try:
            a=int(input())
      except ValueError:
            print("Invalid character Enter a valid integer value")
            a=self.integerInput()
      return a
      


#a method to calculate factorial
   def calculateFactorial(self,n):
      factorial=1
      num=n
      if num < 0:
         return 0
      elif num == 0:
         return 1
      else:
         for i in range(1,num + 1):
            factorial = factorial*i
      return factorial                                                        

      

# method to calculate nCr. 
   def calculate_nCr(self):
      print("Enter n")
      self.n=self.integerInput()     
      print("Enter r")
      self.r=self.integerInput()     
      n=self.n
      r=self.r
      nCr=self.calculateFactorial(n)/(self.calculateFactorial(r)*self.calculateFactorial(n-r))
      return nCr



# x is an instance of factorialClass
x=factorialClass()
ncr=x.calculate_nCr()
print("nCr is ",ncr)
