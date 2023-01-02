def solution(str1:str, str2:str):
  str1=str1.lower()
  dict1={}
  str2=str2.lower()
  dict2={}
  gyo={}
  hap={}
  
  for i in range(len(str1)-1):
    if str1[i:i+2].isalpha():
      if str1[i:i+2] in dict1.keys():
        dict1[str1[i:i+2]]+=1
      else:
        dict1[str1[i:i+2]]=1

  for i in range(len(str2)-1):
    if str2[i:i+2].isalpha():
      if str2[i:i+2] in dict2.keys():
        dict2[str2[i:i+2]]+=1
      else:
        dict2[str2[i:i+2]]=1

  for d1 in dict1.keys():
    if d1 in dict2.keys():
      gyo[d1]=min(dict1[d1],dict2[d1])
      hap[d1]=max(dict1[d1],dict2[d1])
    else:
      hap[d1]=dict1[d1]
  
  for d2 in dict2.keys():
    if d2 not in hap.keys():
      hap[d2]=dict2[d2]
  
  
  if sum(hap.values())==0:
    return 65536

  else:
    return int((sum(gyo.values())/sum(hap.values()))*65536)
  

print(solution('E=M*C^2','e=m*c^2'))