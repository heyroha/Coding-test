import sys

input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    order = input().split()
    # push 명령어인 경우
    if len(order) == 2:
        q.append(order[1])
    # 그 외(5가지)
    else:
        if order[0] == 'pop':
            if len(q) == 0:
                print(-1)
            else:
                pop_num = q.pop(0)
                print(pop_num)
        elif order[0] == 'empty':
            if len(q) == 0:
                print(1)
            else: 
                print(0)
        elif order[0] == 'front':
            if len(q) == 0:
                print(-1)
            else: 
                print(q[0])
        elif order[0] == 'back':
            if len(q) == 0:
                print(-1)
            else:
                print(q[-1])
        else:
            print(len(q))
        