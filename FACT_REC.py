def fact(n):
 if(n==1):
  return(1)
 elif(n==0):
  return(1)
 elif(n<0):
  return("factorial can't be found !")
 else:
  return(n*fact(n-1))
a=int(input("Enter the number: "))
print(fact(a))
