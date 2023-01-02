
import math


def solution(n, k):
  numberlist=[]
  total=1
  answer=[]
  for i in range(1,n+1):
    numberlist.append(i)
    total=total*i
  
  div=total//n
  k-=1
  while True:
    answer.append(numberlist[int(k/div)])
    numberlist.pop(int(k/div))
    k=k%div
    n-=1
    try:
      div=div//n
    except:
      break
  return answer
print(solution(3,5))