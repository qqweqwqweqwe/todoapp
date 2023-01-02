
def solution(d, budget):
  d.sort()
  answer = 0
  while len(d)>0 and budget>=d[0]  :
    budget-=d[0]
    d.pop(0)
    answer+=1
  return answer