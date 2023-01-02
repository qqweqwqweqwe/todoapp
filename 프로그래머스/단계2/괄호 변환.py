

def is_it_balanced(s:str):
  if s.count('(')==s.count(')'):
    return True
  else:
    return False

def cannotbeseperate(s:str):
  total=0
  for i in range(len(s)):
    if s[i]=='(':
      total+=1
    else:
      total-=1
    if total==0 and i!=len(s)-1:
      return False
  return True
    


def is_it_right(s:str):
  stack=[]
  if is_it_balanced(s):
    for i in range(len(s)):
      stack.append(s[i])
      if len(stack)>=2 and stack[-1]==')' and stack[-2]=='(':
        stack.pop()
        stack.pop()
    if len(stack)>0:
      return False
    else:
      return True
  else:
    return False


# 올바른게 아니면 앞뒤 자르고 
def solution(p:str):
  if p=="":
    return ""
  for i in range(2,len(p)+1):
    u=p[0:i]
    v=p[i:len(p)]
    if is_it_balanced(u) and is_it_balanced(v) and cannotbeseperate(u):
      if is_it_right(u):
        return u+solution(v)
      else:
        empty='(' + solution(v) + ')'
        u=u[1:len(u)-1]
        newu=""
        for i in range(len(u)):
          if u[i]==')':
            newu+='('
          else:
            newu+=')'
        return empty+newu

      



  

print(solution("()))((()"))



  

    
    

  