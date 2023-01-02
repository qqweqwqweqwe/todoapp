def stackpop(stack):
  if (stack[-1]==')' and stack[-2]=='(') or (stack[-1]==']' and stack[-2]=='[') or (stack[-1]=='}' and stack[-2]=='{'):
    return True
  else:
    return False
def solution(s:str):
  count=0
  for i in range(len(s)):
    temp_s=str(s)
    answer=temp_s[i:len(s)]+temp_s[0:i]
    stack=[]
    for i in range(len(answer)):
      stack.append(answer[i])
      while len(stack)>=2 and stackpop(stack):
        stack.pop()
        stack.pop()
    if len(stack)==0:
      count+=1
  return count
