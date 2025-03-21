def solution(A,B):
    answer = 0
    
    A.sort()
    B.sort()
    for i in range(len(B)):
        answer += B[i] * A[len(B) - i -1]
        
    return answer