
n=int(input("Enter a number: "))

def humpty_dumpty(n):
  if((n%3==0 and n%5==0)):
    return str("Humty_Dumpty")
  elif(n%3==0 ):
    return str("Humty")
  elif(n%5==0):
    return str("Dumpty")


r=humpty_dumpty(n)

print(r)