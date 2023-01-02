def solution(board):
  maxval=0
  for i in range(len(board)):
    for j in range(len(board[0])):
      if i==0 or j==0 or board[i][j]==0:
        maxval=max(maxval,board[i][j])
        continue
      board[i][j]=min(board[i-1][j],board[i][j-1],board[i-1][j-1])+1
      maxval=max(maxval,board[i][j])
  return maxval**2

