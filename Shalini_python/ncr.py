def fact(n):
  #To Calculate Factorial of a number
  if n==0:
    return 1
  else:
    return n*fact(n-1)
def nCr(n,r):
  #To Calculate nCr value
  if r>n:
    return 0
  else:
    return fact(n)/(fact(r)*fact(n-r))
def main():
  try:
    n=int(input("enter the value of n:"))
    r=int(input("enter the value of r:"))
    result=nCr(n,r)
    print(f"{n}C{r}={result}")
  except ValueError:
    print("Invalid input.Please enter n and r values")
if __name__=="__main__":
  main()