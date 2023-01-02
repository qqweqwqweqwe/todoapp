def solution(n, s):
  if n>s:
    return [-1]
  answer=[]
  q=s//n
  r=s%n
  while s:
    if r>0:
      answer.append(q+1)
      r-=1
      s-=1
    else:
      answer.append(q)
    s-=q
  answer.sort()
  return answer
  

print(solution(2,8))