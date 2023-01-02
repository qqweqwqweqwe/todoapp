from collections import deque
from sys import flags


def solution(order):

  stack=[-1]
  count=1
  order=deque(order)
  answer=len(order)
  flag=

  while flag:

  while order:
    while True:        
      
      if order and order[0]==count:
        order.popleft()
        count+=1
      elif stack and stack[-1]==count:
        stack.pop()
        count+=1
      else:
        if order:
          stack.append(order.pop())
        break


solution([4, 3, 1, 2, 5])