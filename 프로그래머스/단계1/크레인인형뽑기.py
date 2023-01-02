
def solution(board, moves):
  num=0
  stack=[]
  while len(moves)>0:
    current=moves.pop(0)-1
    i=0
    while i<len(board)-1:
      if board[i][current]!=0:
        break
      i+=1
    if board[i][current]!=0:
      stack.append(board[i][current])
    board[i][current]=0
    if len(stack)>=2 and stack[-1]==stack[-2]:
      stack.pop()
      stack.pop()
      num+=2
  answer = num
  return answer




board=[
[0,0,0,0,0],
[0,0,1,0,3],
[0,2,5,0,1],
[4,2,4,4,2],
[3,5,1,3,1]
]	


moves=[1,5,3,5,1,2,1,4]

print(solution(board,moves))
