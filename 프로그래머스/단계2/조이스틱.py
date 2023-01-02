
joy={}
for i in range(65,91):
  joy[chr(i)]=min(i-65,91-i)

minvalue=10000000000



def solution(name):
  global minvalue
  s='A'*len(name)
  recursive(0,0,s,name,0)
  return minvalue



def recursive(cur, direction, s, name,answer):
  global joy
  global minvalue
  temp=cur
  if s==name:
    minvalue=min(minvalue,answer)
    return 
  if direction=='left':
    while name[temp]==s[temp]:
      temp-=1
    answer+=cur-temp
    cur=temp
    answer+=joy[name[cur]]
    s=list(s)
    s[cur]=name[cur]
    s="".join(s)
  elif direction=='right':
    while name[temp]==s[temp]:
      temp+=1
    answer+=temp-cur
    cur=temp
    answer+=joy[name[cur]]
    s=list(s)
    s[cur]=name[cur]
    s="".join(s)
  recursive(cur,'left',s,name,answer)
  recursive(cur,'right',s,name,answer)

