"""# Python program to find the factorial of a number provided by the user.

# change the value for a different result
num = 7

# To take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
      factorial = factorial*i
   print("The factorial of",num,"is",factorial)
"""

class Assignment1:
   def __init__(self):
      self.num=0
      self.factorial=1
      self.is_avail=True
      self.stored=list()
   def take_input(self,text=None):
      self.num=int(input(text))
      return self.num
   def Factorial(self,num=None):
      if num is not None:
        self.num=num
      if self.num < 0:
        self.is_avail=False
        self.stored.append(self.is_avail)
      elif self.num == 0:
        self.Factorial=1
      else:
       for i in range(1,self.num + 1):
        self.factorial = self.factorial*i
        self.stored.append(self.factorial)
   def display_result(self):
      if self.is_avail==False:
         print("Sorry, factorial does not exists for negative numbers")
         exit()
      else:
         return self.factorial
   def get_stored_data(self):
     return self.stored





