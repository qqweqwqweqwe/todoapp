from math import ceil
from typing import Counter
def solution(progresses, speeds):  
  days=[]
  answer = []
  for i in range(len(progresses)):
    days.append(ceil((100-progresses[i])/speeds[i]))
  for i in range(len(days)-1):
    if days[i]>days[i+1]:
      days[i+1]=days[i]
  co=Counter(days)
  for i in co.keys():
    answer.append(co[i])
  return answer
print(solution([93, 30, 55],[1, 30, 5]))