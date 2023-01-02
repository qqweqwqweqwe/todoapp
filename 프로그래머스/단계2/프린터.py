from collections import deque
def solution(priorities, location):
  prilist=deque()
  answer=0
  for count,priority in enumerate(priorities) :
    prilist.append([count,priority])
  target=prilist[location]
  print(target)
  while True:
    maxval=max(prilist, key=lambda x:x[1])
    answer+=1
    while True:
      cur=prilist.popleft()
      if cur[1]==maxval[1]:
        break
      prilist.append(cur)
    if target[1]==maxval[1] and target[0]==maxval[0]:
      return answer


print(solution([1, 1, 9, 1, 1, 1],0))