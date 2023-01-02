def solution(grid):
  cycle=[]
  d=[[0,1],[1,0],[0,-1],[-1,0]]

  
  check= [[[0 for _ in range(4)] for _ in range(len(grid[0]))] for _ in range(len(grid))]

# 일단 방향 바꾸고 위치 바꾸는것
  for i in range(len(d)):
    curposition=[0,0]
    garo=curposition[1]
    sero=curposition[0]
    curdirection=d[i]
    positionlist=[]
    directionlist=[]
    directionlist.append(curdirection)
    positionlist.append(curposition)
    if check[sero][garo][i]==1:
      continue
    else :
      check[sero][garo][i]=1
    check[sero][garo][i]=1
    while True:
      if grid[sero][garo]=='R':
        i=(i+1)%4
        curdirection=d[i]
      elif grid[sero][garo]=='L':
        i=(i+3)%4
        curdirection=d[i]

      directionlist.append(curdirection)
      garo+=curdirection[1]
      sero+=curdirection[0]

      if garo<0:
        garo=len(grid[0])-1
      elif garo>len(grid[0])-1:
        garo=0
      if sero<0:
        sero=len(grid)-1
      elif sero >len(grid)-1:
        sero=0
      positionlist.append([sero,garo])
      check[sero][garo][i]=1

      if positionlist[-1]==positionlist[0] and directionlist[-1]==directionlist[0]:
        cycle.append(len(positionlist)-1)
        break
  cycle.sort()
  a=[2,3,1]
  a.sort()
  print(a)
  return cycle


print(solution(["S"]	))




