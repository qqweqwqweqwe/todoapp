def solution(n, computers):
  visited=[0]*n
  answer=0
  for i in range(n):
    visit_list=[]
    if visited[i]==1:
      continue
    else:
      answer+=1
      visit_list.append(i)
    while visit_list:
      cur=visit_list.pop()
      visited[cur]=1
      for i in range(len(computers[cur])):
        if computers[cur][i]==1 and visited[i]==0:
          visit_list.append(i)
  return answer

solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])