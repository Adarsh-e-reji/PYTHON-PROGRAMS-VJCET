n=int(input("enter a number:"))
temp=n
rev=0
while(n>0):
      a=n%10
      rev=rev*10+a
      n=n//10
if(temp==rev):
    print("The number is pallindrom")
else:
    print("The number is not pallindrom")   
