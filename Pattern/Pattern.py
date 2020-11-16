start=65
num=int(input())
for i in range(1,num+1):
  print(chr(start),end="")
  start=start+1
start=start-2
for i in range(1,num):
  print(chr(start),end="")
  start=start-1
