def solution(citations:list):
  citations.sort(reverse=True)
  count=0
  for i in range(len(citations)):
    if i+1>citations[i]:
      break
    else:
      count=i+1
  
  return count

