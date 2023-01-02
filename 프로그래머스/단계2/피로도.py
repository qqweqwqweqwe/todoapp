maxval=0

def solution(k, dungeons):
  visit=[]
  search(k,dungeons,visit,-1,0)
  return maxval



def search(k,dungeons,visited:list,curidx,count):
  global maxval

  
  
  if curidx!=-1:
    if curidx in visited:
      return 
    visited.append(curidx)
  maxval=max(count,maxval)
  for i,dungeon in enumerate(dungeons):
    if k>=dungeon[0]:
      search(k-dungeon[1],dungeons,visited,i,count+1)
      
  if curidx!=-1:
    visited.remove(curidx)
  

print(solution(80,[[80,20],[50,40],[30,10]]))
