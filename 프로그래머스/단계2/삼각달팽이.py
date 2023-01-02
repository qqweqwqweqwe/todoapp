def solution(n):
  board=[[0 for i in range(n)] for j in range(n)]
  x,y=-1,0
  turnlist=[[1,0],[0,1],[-1,-1]]
  turncount=0
  number=1
  for i in range(n,0,-1):
    for j in range(i):
      x+=turnlist[turncount][0]
      y+=turnlist[turncount][1]
      board[x][y]=number
      number+=1
    turncount+=1
    if turncount>2:
      turncount=0
  answer=[]
  for i in range(n):
    for j in range(i):
      if board[i][j]!=0:
        answer.append(board[i][j])

  return answer
  
