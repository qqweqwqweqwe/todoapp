def solution(strings:list, n):
  return sorted(strings, key= lambda x:(x[n],x))