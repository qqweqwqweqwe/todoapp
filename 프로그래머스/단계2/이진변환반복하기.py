def solution(s:str):

  def totwo(x):
    x=len(x)
    newx=""
    while x!=0:
      newx+=str(x%2)
      x=x//2
    newx=list(newx)
    newx.reverse()
    newx="".join(newx)
    return newx
  removecount=0
  count=0
  while s!='1':
    print(s)
    removecount+=s.count('0')
    s=s.replace('0','')
    s=totwo(s)
    count+=1
  answer = [count,removecount]
  return answer

print(solution("110010101001"))