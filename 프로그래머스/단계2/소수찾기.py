from itertools import permutations

def isit(num):
  if num<2:
    return False
  for i in range(2,int(num**0.5)+1):
    if num%i==0:
      return False
  return True

def solution(numbers):
  numset=set()
  for i in range(1,len(numbers)+1):
    per=list(permutations(numbers,i))
    for number in per:
      answer=""
      for j in number:
        answer+=j
      answer=int(answer)
      if isit(answer):
        numset.add(answer)
  return len(numset)

  
