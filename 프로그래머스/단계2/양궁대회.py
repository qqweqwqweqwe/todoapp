from copy import copy
from itertools import combinations
'''
def solution(n, info:list):
  result=[]
  for i in range(len(info)):
    result.append([10-i,info[i]+1])
  
  
  resultcomb=list(combinations(result,n))
  diff=0

  for i in resultcomb:
    total=0
    count=0
    for j in i:
      if count+i[1]>n:
        break
      else:
        count+=i[1]
        total+=i[0]
    

    print(i)

  answer = []
  return answer

solution(5,[2,1,1,1,0,0,0,0,0,0,0])
'''

arrowlist=[0]*11
def brute(count,curnum,arrowlist):
  copylist=arrowlist.copy()
  if curnum!=-1:
    copylist[curnum]+=1
  if count==2:
    print(copylist)
    return
  for i in range(len(arrowlist)):
    brute(count+1,i,copylist)
  if curnum!=-1:
    copylist[curnum]-=1

brute(0,-1,arrowlist)