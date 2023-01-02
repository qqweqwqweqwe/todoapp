from hashlib import new


def solution(dartResult:str):
  newstr=[]
  dict={
    'S':1,
    'D':2,
    'T':3
  }
  answer=0
  dartResult=list(dartResult)
  for i in range(len(dartResult)):
    if dartResult[i]=='0':
      continue
    if dartResult[i].isdigit():
      if dartResult[i+1].isdigit():
        newstr.append((10**dict[dartResult[i+2]]))
      else:
        newstr.append((int(dartResult[i])**dict[dartResult[i+1]]))
    elif dartResult[i].isalpha():
      continue
    else:
      newstr.append(dartResult[i])
  
  for i in range(len(newstr)):
    if newstr[i]=='#':
      newstr[i-1]=newstr[i-1]*-1
    if newstr[i]=='*':
      newstr[i-1]=newstr[i-1]*2
      if i!=1:
        if type(newstr[i-3])==int:
          newstr[i-3]=newstr[i-3]*2
        else:
          newstr[i-2]=newstr[i-2]*2

  for i in newstr:
    if type(i)==int:
      answer+=i
      
  return answer
