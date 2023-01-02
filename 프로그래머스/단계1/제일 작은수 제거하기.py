

def solution(arr:list):
  a=min(arr)
  arr.remove(a)
  if len(arr)==0:
    arr.append(-1)
  return arr