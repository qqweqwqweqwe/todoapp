def solution(N, roads, K):
  inf=10001
  answer=0
  village=[[inf for j in range(N+1)] for i in range(N+1)]
  for i in range(len(village)):
    village[i][i]=0
  for road in roads:
    village[road[0]][road[1]]=min(road[2],village[road[0]][road[1]])
    village[road[1]][road[0]]=min(road[2],village[road[1]][road[0]])
  

  for a in range(1,N+1):
    for b in range(1,N+1):
      for c in range(1,N+1):
        village[b][c]=min(village[b][c],village[b][a]+village[a][c])
  
  for i in village[1]:
    if i<=K:
      answer+=1

  return answer

solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4)