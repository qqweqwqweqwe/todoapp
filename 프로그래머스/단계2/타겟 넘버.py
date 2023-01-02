answer=0
def dfs(count,target,current,numbers):
  global answer
  count+=1
  if count==len(numbers):
    if target==current:
      answer+=1
    return
  dfs(count,target,current+numbers[count],numbers)
  dfs(count,target,current-numbers[count],numbers)
def solution(numbers, target):
  dfs(-1,target,0,numbers)
  return answer
  
