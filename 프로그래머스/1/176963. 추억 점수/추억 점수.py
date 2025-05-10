def solution(name, yearning, photo):
    score_map = dict(zip(name, yearning))
    answer = []
    
    for photo_row in photo:
        total = sum(score_map.get(person, 0) for person in photo_row)
        answer.append(total)
        
    return answer