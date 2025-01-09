num = int(input())
li = []
for i in range(num):
  a,b = map(int,input().split())
  li.append(a+b)

for j in li:
  print(j)