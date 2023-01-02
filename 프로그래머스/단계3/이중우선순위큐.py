from queue import PriorityQueue


def solution(operations):
  
  PQ=heap()
  for operation in operations:
    operation=operation.split(' ')
    if operation[0]=='I':
      PQ.put(operation[1])


  print(PQ[0])
  answer = []
  return answer

solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])