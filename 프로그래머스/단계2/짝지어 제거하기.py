def solution(s:str):
  stack=[]
  for i in range(len(s)):
    stack.append(s[i])
    while len(stack)>=2 and stack[-1]==stack[-2]:
      stack.pop()
      stack.pop()
  
  if len(stack)==0:
    return 1
  else:
    return 0


print(solution("baabaa"))