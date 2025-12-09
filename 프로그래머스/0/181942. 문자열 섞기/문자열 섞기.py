
def solution(str1, str2):
  new_list = []

  for i in range(len(str1)):
    new_list.append(str1[i])
    new_list.append(str2[i])

  answer = ''.join(new_list)
  return answer