def solution(records):
  userlist={}
  results=[]
  for record in records:
    command=record.split()
    if command[0]=='Enter':
      userlist[command[1]]=command[2]
    elif command[0]=='Change':
      userlist[command[1]]=command[2]
  
  for record in records:
    command=record.split()
    if command[0]=='Enter':
      results.append(userlist[command[1]]+"님이 들어왔습니다.")
    elif command[0]=='Leave':
      results.append(userlist[command[1]]+"님이 나갔습니다.")

  return results  
  


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])