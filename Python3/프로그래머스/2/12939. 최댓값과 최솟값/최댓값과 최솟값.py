def solution(s):
    
    numbers = list(map(int, s.split())) #문자열을 공백 기준으로 나눈 후, 정수로 변환하여 저장
    
    answer = ''
    a = min(numbers)
    b = max(numbers)
    answer = f"{a} {b}"
    print(answer)
    
    return answer