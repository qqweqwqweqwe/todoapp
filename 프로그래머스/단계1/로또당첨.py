

def solution(lottos, win_nums):
  same=len(list(set(lottos) & set(win_nums)))  
  numofzero=lottos.count(0)
  answer = []

  best=7-same-numofzero
  if best>=6:
    best=6
  worst=7-same
  if worst>=6:
    worst=6
  answer.append(best)
  answer.append(worst)
  return answer


lottos=[45, 4, 35, 20, 3, 9]
win_nums=[20, 9, 3, 45, 4, 35]

print(solution(lottos,win_nums))
