def convertTime(n):
    h = n // 100
    m = n % 100
    return h * 60 + m

def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        s = startday
        schedule = convertTime(schedules[i])
        for time in timelogs[i]:
            if s in [6,7]:
                s+=1
                if s == 8:
                    s = 1
                continue
            t = convertTime(time)
            if schedule + 10< t :
                break
            else: 
                s += 1
        else:           
            answer += 1
            
    return answer