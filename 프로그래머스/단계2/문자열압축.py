

from collections import deque


def solution(s):
  minlen=len(s)
  lenlist=[]
  for i in range(1,len(s)+1):
      lenlist.append(i)
  
  for l in lenlist:
    tempqueue=deque()
    answer=""
    count=1
    start=0
    while True:
      if start+l>=len(s):
        tempqueue.append(s[start:len(s)])
        break
      else:
        tempqueue.append(s[start:start+l])
      start+=l
    cur=tempqueue[0]
    for i in range(1,len(tempqueue)):
      if tempqueue[i]==cur:
        count+=1
      else:
        if count==1:
          answer+=cur
        else:
          answer+=str(count)+cur
        count=1
        cur=tempqueue[i]
    if count==1:
          answer+=cur
    else:
      answer+=str(count)+cur
    minlen=min(minlen,len(answer))
  return minlen

      


      

solution("abcabcabcabcdededededede")