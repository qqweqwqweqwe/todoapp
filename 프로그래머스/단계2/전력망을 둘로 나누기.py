def solution(n, wires):
  maxcount=n
  dicts={}
  for i in range(1,n+1):
    dicts[i]=[]
    
  for wire in wires:
    dicts[wire[0]].append(wire[1])
    dicts[wire[1]].append(wire[0])
  answer=[]
  
  print(dicts)

  for wire in wires:
    firstcount=0
    secondcount=0
    first=wire[0]
    second=wire[1]
    dicts[first].remove(second)
    dicts[second].remove(first)
    stack=[]
    visited=[]
    stack.append(first)
    visited.append(first)
    while stack:
      cur=stack.pop()
      if cur not in visited:
        visited.append(cur)
      
      for i in dicts[cur]:
        if i not in visited:
          stack.append(i)
    firstcount=len(visited)
    visited=[]
    stack.append(second)
    visited.append(second)
    while stack:
      cur=stack.pop()
      if cur not in visited:
        visited.append(cur)
      
      for i in dicts[cur]:
        if i not in visited:
          stack.append(i)

    secondcount=len(visited)
    if abs(firstcount-secondcount)<maxcount:
      maxcount=abs(firstcount-secondcount)
    dicts[first].append(second)
    dicts[second].append(first)
  return maxcount    

  


solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])