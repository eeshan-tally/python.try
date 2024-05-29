#importing class Fact from pyfactorial.py
from pyfactorial import Fact 

class NCR:
    def __init__(self):
        self.fact = Fact()
    #fuction to calculate ncr
    def calculate_ncr(self, n, r):
        # Calculate n!
        self.fact.num = n
        n_factorial = self.fact.Find_factorial()
        
        # Calculate r!
        self.fact.num = r
        r_factorial = self.fact.Find_factorial()
        
        # Calculate (n-r)!
        self.fact.num = n - r
        nr_factorial = self.fact.Find_factorial()
        
        # Calculate nCr
        ncr = n_factorial // (r_factorial * nr_factorial)
        return ncr
    
if __name__ == "__main__":
    n = int(input("Enter value for n: "))
    r = int(input("Enter value for r: "))
    
    obj = NCR()
    result = obj.calculate_ncr(n, r)
    print(f"{n}C{r} = {result}")