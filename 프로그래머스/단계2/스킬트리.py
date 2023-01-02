def solution(skill, skill_trees):
  skilldict={}
  for s in range(len(skill)):
    skilldict[skill[s]]=s
  count=0  
  for skill in skill_trees:
    temp=""
    count+=1
    for i in skill:
      if i in skilldict.keys():
        temp+=str(skilldict[i])
    for i in range(len(temp)):
      if int(temp[i])!=i:
        count-=1
        break
  return count
        

        

      

solution("CBD",["BACDE", "CBADF", "AECB", "BDA"])