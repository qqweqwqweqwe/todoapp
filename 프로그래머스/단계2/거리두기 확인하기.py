def valid(i,j):
  if i<0 or i>4 or j<0 or j>4:
    return False
  else:
    return True
def solution(places):
  result=[]
  for place in places:
    plist=[]
    flag=0
    for i in range(5):
      for j in range(5):
        if place[i][j]=='P':
          plist.append((i,j))
    # P인 부분들 다 리스트에 일단 넣기
    for p in plist:
      stack=[]
      visited=[]
      stack.append(p)
      distance=[[0]*5 for i in range(5)]
      while stack:
        cur=stack.pop()
        visited.append(cur)
        i,j=cur[0],cur[1]
        if place[i][j]=='P':
          if distance[i][j]>0 and distance[i][j]<=2:
            flag=1
            break
        if valid(i+1,j) and place[i+1][j]!='X' and (i+1,j) not in visited:
          stack.append((i+1,j))
          visited.append((i+1,j))
          distance[i+1][j]=distance[i][j]+1
        if valid(i-1,j) and place[i-1][j]!='X' and (i-1,j) not in visited:
          stack.append((i-1,j))
          visited.append((i-1,j))
          distance[i-1][j]=distance[i][j]+1
        if valid(i,j+1) and place[i][j+1]!='X' and (i,j+1) not in visited:
          stack.append((i,j+1))
          visited.append((i,j+1))
          distance[i][j+1]=distance[i][j]+1
        if valid(i,j-1) and place[i][j-1]!='X' and (i,j-1) not in visited:
          stack.append((i,j-1))
          visited.append((i,j-1))
          distance[i][j-1]=distance[i][j]+1
    if flag==1:
      result.append(0)
    else:
      result.append(1)
  return result

solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])