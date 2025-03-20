#Square star pattern
n=4
print("")
for i in range(n):
  print("*"*n)

#Hallow square star pattern
n=4
print("")
for i in range(n):
  if i==0 or i==n-1:
    print("*"*n)
  else:
    print("*","","*")

#Rhombus star pattern
n=4
print("")
for i in range(n):
  print(" "*i, "*"*n)

#Rectangular star pattern
a=6
b=4
print("")
for i in range(b):
  print("*"*a)

#Hallow rectangular star pattern
a=6
b=4
print("")
for i in range(b):
  if i==0 or i==b-1:
    print("*"*a)
  else:
    print("*"+" "*(a-2)+"*")

#Parallelogram star pattern
a=6
b=4
print("")
for i in range(b):
  print(" "*i, "*"*a)

#Hallow pyramid star pattern
n=7
print("")
for i in range(1,n+1):
  if i==1 or i==2:
    print(" "*(n-i)+"* "*i)
  elif i==n:
    print("* "*n)
  else:
    print(" "*(n-i)+"*"+" "*(2*i-3)+"*")
    
#Inverted pyramid star pattern
n=7
print("")
for i in range(n,0,-1):
  print(" "*(n-i),"* "*i)    

#Inverted Hallow pyramid star pattern
n=7
print("")
for i in range(n,0,-1):
  if i==1:
    print(" "*(n-i)+"* "*i)
  elif i==n:
    print("* "*n)
  else:
    print(" "*(n-i)+"*"+" "*(2*i-3)+"*")

#Basic Square 1 pattern
n=4
print("")
for i in range(n):
  print("1"*n)

#Basic square incrementing pattern
n=4
print("")
for i in range(1,n+1):
  print(str(i)*n)

#Internal varsity square pattern
n=4
print("")
for i in range(1,n+1):
  if i==1 or i==n:
    print("3"*(n-1))
  else:
    print("3"+str(i-1)+"3")

#Basic right triangle number pattern
n=4
a=1
print("")
for i in range(1,n+1):
  for j in range(i):
    print(a,end="")
    a+=1
  print("")

#Inverted Basic right triangle number pattern
n=4
a=10
print("")
for i in range(n,0,-1):
  for j in range(i):
    print(a,end="")
    a-=1
  print("")

#Basic incrementing triangle pattern
n=4
a=6
print("")
for i in range(n,0,-1):
  print(str(a)*i)
  a-=1
