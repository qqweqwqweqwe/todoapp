def move_to_end(start, middle,end,n,routelist:list):
  if n==1:
    routelist.append([start,end])
  else:
    move_to_end(start,end,middle,n-1,routelist)
    routelist.append([start,end])
    move_to_end(middle,start,end,n-1,routelist)
  

def solution(n):
  rlist=[]
  move_to_end(1,2,3,n,rlist)
  return rlist


print(solution(3))