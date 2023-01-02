def solution(new_id:str):
  answer = ''


  new_id=new_id.lower()
  
  for i in range(len(new_id)):
    if new_id[i].isalpha() or new_id[i].isdigit() or new_id[i]=='-' or new_id[i]=='_' or new_id[i]=='.':
      answer+=new_id[i]

  new_id=answer

  while ".." in new_id:
    new_id=new_id.replace('..','.')


  if new_id[0]=='.':
    new_id=new_id.lstrip('.')
  if len(new_id)!=0 and new_id[-1]=='.' :
    new_id=new_id.rstrip(".")
  
  if len(new_id)==0:
    new_id+='a'


  if len(new_id)>=16:
    new_id=new_id[0:15]

  if new_id[len(new_id)-1]=='.':
    new_id=new_id[0:len(new_id)-1]

  if len(new_id)<=2:
    last=new_id[len(new_id)-1]
    while len(new_id)<=2:
      new_id=new_id+last
  
  answer=new_id

  return answer


print(solution("=.="))