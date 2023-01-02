def solution(s):
  # 1부터 len(s)//2 까지 
  maxcount=len(s)
  for i in range(1, int(len(s)/2)+1):
    answer=""
    if len(s)%i==0:
      j=0
      strlist=[]
      while j<=len(s)-1:
        strlist.append(s[j:j+i])
        j+=i
      temp=strlist[0]
      count=1
      for i in range(1,len(strlist)):
        if temp!=strlist[i]:
          answer=answer+str(count)+temp
          temp=strlist[i]
          count=1
        else:
          count+=1
        
        if i ==len(strlist)-1:
          answer=answer+str(count)+temp
          temp=strlist[i]
          count=1
      answer=answer.replace('1','')
      print(answer)
      maxcount=min(maxcount,len(answer))  
  return maxcount




      
    
    
    



solution("abcabcdede")