


def solution(elements):
  result=set()
  length=len(elements)
  elements=elements*2
  for i in range(1,length+1):
    total=0
    start=0
    next=start+i
    
    for j in range(i):
      total+=elements[j]

    result.add(total)
    while start<length:
      total-=elements[start]
      total+=elements[next]
      start+=1
      next+=1
      result.add(total)
  
  return len(result)

solution([7,9,1,1,4])
