N = int(input())

for i in range(1,N):
  print('*'*i + " "*(2*(N-i))+'*'*i)
for j in range(N):
  print('*'*(N-j) + ' '*(2*(j+1)-2) + '*'*(N-j))
