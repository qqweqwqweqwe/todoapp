def solution(rows, columns, queries):

  

  board=[[0 for i in range(rows)] for j in range(columns)]
  number=1
  for i in range(rows):
    for j in range(columns):
      board[i][j]=number
      number+=1
  print(board)
  numlist=[]
  for query in queries:
    for i in range(len(query)):
      query[i]-=1
    x,y=query[0],query[1]-1
    
    while y<query[3]:
      y+=1
      numlist.append(board[x][y])
    while x<query[2]:
      x+=1
      numlist.append(board[x][y])
    while y>query[1]:
      y-=1
      numlist.append(board[x][y])
    while x>query[0]+1:
      x-=1
      numlist.append(board[x][y])
    print(numlist)
    
      
      
  answer = []
  return answer


solution