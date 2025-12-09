def solution(my_string, overwrite_string, s):
    my_string_li = list(my_string) 
    my_string_li[s:len(overwrite_string)+s] = overwrite_string

    answer = ''.join(my_string_li)
    return answer