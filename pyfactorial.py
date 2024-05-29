# Python program to find the factorial of a number provided by the user.

class Fact:
   #initialising the constructor
   def __init__(self):
      self.num=None
      self.factorial=None
  # function for taking the valid input
   def Input_from_user(self):
      while True:
         try:
               self.num = int(input("Enter a number: "))
               return self.num
         except ValueError:
               print("Invalid input. Please enter a valid integer.")
   # function to find the factorial
   def Find_factorial(self):
      self.factorial = 1
      # check if the number is negative, positive or zero
      if self.num < 0:
         print("Sorry, factorial does not exist for negative numbers")
      elif self.num == 0:
         print("The factorial of 0 is 1")
      else:
         for i in range(1,self.num + 1):
           self.factorial = self.factorial*i
      return self.factorial
   #function to print the output
   def Print_output(self):
      print("The factorial of",self.num,"is",self.factorial)

#object creation

obj = Fact()
obj.Input_from_user()
obj.Find_factorial()
obj.Print_output()







   



