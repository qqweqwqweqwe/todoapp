from collections import deque
def solution(n):
  dq=deque()
  answer = 0
  while n!=0:
    dq.appendleft(n%3)
    n=n//3
  for i in range(len(dq)):
    answer+=3**i*dq[i]
  return answer
print(solution(45))

#int 함수 진법 사용 ㅋㅋ