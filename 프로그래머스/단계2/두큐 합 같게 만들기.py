
from collections import deque


def solution(queue1, queue2):
  count=0
  queue1=deque(queue1)
  queue2=deque(queue2)
  sum1=sum(queue1)
  sum2=sum(queue2)
  lenthmax=len(queue1)*3
  while sum1!=sum2:
    if count>lenthmax:
      return -1
    if sum1>sum2:
      data=queue1.popleft()
      queue2.append(data)
      sum1-=data
      sum2+=data
      count+=1
    else:
      data=queue2.popleft()
      queue1.append(data)
      sum2-=data
      sum1+=data
      count+=1
  return count

