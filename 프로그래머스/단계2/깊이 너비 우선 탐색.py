from collections import deque
# 스택에 들어가는게
# 그때의 좌표와 그때까지의 거리
def solution(maps):
  def valid(y,x):
    if y>=0 and y<len(maps) and x>=0 and x<len(maps[0]):
      return True
    else:
      return False


  
  visited=[[0 for i in range(len(maps[0]))] for j in range(len(maps))]
  queue=deque()
  y,x=0,0
  queue.append((0,0,1))
  visited[0][0]=1
  dx=[1,0,-1,0]
  dy=[0,1,0,-1]
  distance=0
  while queue:
    curpos=queue.popleft()
    y,x=curpos[0],curpos[1]
    distance=curpos[2]
    if y==len(maps)-1 and x==len(maps[0])-1:
      return distance
    for i in range(4):
      if valid(y+dy[i],x+dx[i]) and visited[y+dy[i]][x+dx[i]]==0 and maps[y+dy[i]][x+dx[i]]==1:
        queue.append((y+dy[i],x+dx[i],distance+1))
        visited[y+dy[i]][x+dx[i]]=1
  return -1


# visited 배열을 자꾸 찾지말고 그냥 첨부터 이차원 배열로 선언하여도 된다

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))