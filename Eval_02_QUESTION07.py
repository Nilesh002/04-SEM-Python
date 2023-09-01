p=int(input("Enter the limit: "))

def sumofmult(p):
  i=0
  sum=0
  for i in range(p+1):
    if(i%3==0 or i%5==0):
      sum+=i
  return(sum)

a=sumofmult(p)
print(f"The of multiples of 3 and 5 till {p} is {a}")