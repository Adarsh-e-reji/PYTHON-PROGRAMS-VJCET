s=str(input("enter the string"))
s.lower()
v=0
c=0
w=1
qm=0
for i in s:
 if(i=="a"or i=="e" or i=="i"or i=="o"or i=="u"):
       v=v+1
 elif(i=="?"):
      qm=qm+1
 elif(i==" "):
      w=w+1
 else:
    c=c+1
print("number of vowels=",v)
print("number of words=",w)
print("number of question marks=",qm)
print("number of consonants=",c)