def Digitsum(a):
  sum=0
  while(a>0):
    rem=a%10
    sum+=rem
    a=a//10
  return sum

n=int(input())
while(len(str(n))>1):
  n=Digitsum(n)
else:
  print(Digitsum(n))
