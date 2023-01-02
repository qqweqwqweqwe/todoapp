def solution(s):
  answer=list(map(int,s.split(' ')))
  maxnum=max(answer)
  minnum=min(answer)
  
  return str(minnum)+' '+str(maxnum)



print(solution("1 2 3 4"))