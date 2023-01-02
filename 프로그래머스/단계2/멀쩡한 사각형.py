import math
def solution(w,h):
  total_count=w*h
  point_list=[[h,0]]
  change=w/h
  a=0
  count=0
  
  while h>0:
    h-=1
    a+=change
    point_list.append([h,round(a,3)])
  
  for i in range(len(point_list)-1):
    front=point_list[i][1]
    back=point_list[i+1][1]
    
    count+=math.ceil(back)-math.floor(front)
  return total_count-count


(solution())