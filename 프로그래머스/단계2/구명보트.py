
from collections import deque


def solution(people:list, limit):
  people=deque(sorted(people))
  answer = 0
  while people:
    if len(people)==1:
      answer+=1
      break
    else:
      if people[0]+people[-1]>limit:
        people.pop()
      else:
        people.popleft()
        people.pop()
      answer+=1
  return answer


print(solution([70, 50, 80, 50]	,100))


# deque 이 진짜 개사기당 ㅎ헤헿
