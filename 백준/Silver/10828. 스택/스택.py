import sys

input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    order = input().split()
    if order[0] == 'push':
        stack.append(order[1])
    elif order[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            pop_num = stack.pop()
            print(pop_num)
    
    elif order[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif order[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    
    else:
        print(len(stack))