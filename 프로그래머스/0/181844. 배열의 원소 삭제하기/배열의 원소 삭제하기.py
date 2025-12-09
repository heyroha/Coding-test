def solution(arr, delete_list):
  for val in delete_list:
    if val in arr:
      arr.remove(val)

  answer = arr
  return answer