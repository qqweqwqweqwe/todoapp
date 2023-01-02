def same(i,j,board):
  if board[i][j]=='0':
    return False
  elif board[i][j]==board[i+1][j]==board[i][j+1]==board[i+1][j+1]:
    return True
  else:
     return False

def solution(m, n, board):
  answer=0
  bb=[]
  for b in board:
    bb.append(list(b))
  board=bb
  flag=True



  while flag:
    flag=False
    #동일한거 다 삭제 리스트에 쳐 박아넣기
    removelist=set()
    for i in range(m-1):
      for j in range(n-1):
        if same(i,j,board):
          flag=True
          removelist.add((i,j))
          removelist.add((i,j+1))
          removelist.add((i+1,j))
          removelist.add((i+1,j+1))
    # 다 0으로 만들어 버리기
    answer+=len(removelist)
    for removeblock in removelist:
      board[removeblock[0]][removeblock[1]]='0'
    
    
    if flag:
      for i in range(n):
        for j in range(m-1,-1,-1):
          if board[j][i]=='0':
            continue
          a=j
          b=i
          while a+1<m and board[a+1][b]=='0':
            a+=1
          board[j][i],board[a][b]=board[a][b],board[j][i]
  return answer
solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"])
          
